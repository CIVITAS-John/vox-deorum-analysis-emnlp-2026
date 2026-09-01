- row:
  - game_id: 73adfbe2-d542-4abd-a59b-25f16a13c91d
  - player_id: 6
  - turn: 362
  - player_type: GLM-4.7-Simple
  - prev_use_nuke: 75.0
  - after_use_nuke: 80.0
  - prev_nuke: 90.0
  - after_nuke: 95.0
  - rationale: Adjusting for strategic balance: Defensive posture against two nuclear-armed enemies (Ethiopia, Netherlands). Happiness prioritized to 100 - critical at 42% with combat penalty affecting all operations. NavalRecon increased to 90 - enhanced Ethiopian Submarine/Destroyer activity detection around Ur and coastal cities. Nuke/UseNuke raised to 95/80 - matching Ethiopia Manhattan Project urgency, nuclear deterrence is now primary security requirement. Switched to Conquest grand strategy to better coordinate multi-front war management while maintaining Spaceship. Diplomacy increased to 75 - World Congress voting in 5 turns against Netherlands sanctions needs support. Espionage at 90 - Ethiopian spies detected in Halab, Harran, Kar-Tukulti-Ninurta require counter-intelligence.
- originalModel: chutes/zai-org/GLM-4.7-TEE@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 80
  - replay_use_nuke: 80
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
    - You are Ashurbanipal, leader of Assyria (Player 6).
      
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
      - PlayerID: 6
      
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
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Atomic Theory: Reveals Uranium and allows you to start working on the Manhattan Project, setting the stage for the production of nuclear weapons.
        Completing it would unlock: Computers, Nuclear Fission
      
      ## Policies
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - Workers' Faculties (Level 1 Tenet of Ideology Order): Worker Faculties: Factories increase City Science output by 10%. +100% Production towards Factories, and receive 5 Free Factories in your Empire.
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Imperium (Continuing Authority Branch):
        - * Cities gain 20 Production and Gold when their borders expand, scaling with Era (40 if all Authority policies are adopted).
        - * Receive 40 Science and Culture when you found or conquer Cities, scaling with Era. Conquest bonus also scales based on City population.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Militarism (Continuing Authority Branch):
        - * +1 Happiness and +2 Culture in Cities with at least 10 Strength.
        - * -15% Unit Maintenance.
        - * -50% Route Maintenance.
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
      - Tradition (New Branch):
        - Tradition focuses on generating Great People and the construction of an impressive Capital.
        - Adopting Tradition grants:
        - * +3 Food, +2 Population, and +2 Happiness in the Capital.
        - * +1 Culture in the Capital for every 2 Citizens.
        - Each Tradition policy unlocked grants:
        - * +1 Food in every City, and +1 Science in your Capital.
        - Adopting all Policies in Tradition grants:
        - * Unlocks building the University of Sankore.
        - * +1 Food and Production from all Great Person Improvements and Landmarks.
        - * Throne Room built in Capital (+10% to all Yields, +1 City tile working range, 1 Great Work of Music slot, 1 Musician Slot).
        - * Allows for the purchase of Great Engineers with Faith starting in the Industrial Era.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 9
        - WonderCompetitiveness: 5
        - MinorCivCompetitiveness: 8
        - Boldness: 6
        - WarBias: 6
        - HostileBias: 3
        - WarmongerHate: 9
        - NeutralBias: 4
        - FriendlyBias: 6
        - GuardedBias: 6
        - AfraidBias: 3
        - DiplomaticBalance: 8
        - Friendliness: 5
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 6
        - Loyalty: 5
        - MinorCivFriendlyBias: 6
        - MinorCivNeutralBias: 5
        - MinorCivHostileBias: 5
        - MinorCivWarBias: 3
        - DenounceWillingness: 3
        - Forgiveness: 8
        - Meanness: 2
        - Neediness: 4
        - Chattiness: 5
        - DeceptiveBias: 1
        - Rationale: DeceptiveBias reduced from 1 to 0. Multi-front warfare (Netherlands war, impending Ethiopia conflict) requires clear diplomatic signaling. China alliance (10/10) and openly hostile Netherlands stance should be transparent to avoid confusion. Our strategic goals are obvious: Ethiopia Oil acquisition, Netherlands containment. Deception wastes diplomatic capital when our military intentions are already visible.
        
        ## Technology
        - Next: None
        
        ## Policy
        - Next: None (Policy)
        
        ## Relationships
        
        ### Okilis
        - Public: 5
        - Private: 5
        - Rationale: Okilis relationship reduced from 10/10 to 5/5 after securing ally status. We lead significantly (182 vs China 76), providing a comfortable buffer. This allows resource reallocation toward higher priorities: new continent settlement, Samarkand diplomatic challenge, and technology advancement. The 5/5 baseline maintains positive diplomatic foundation without demanding continued attention. Our稳固 alliance with Okilis remains strategically important for regional security and China relationship management, but we can now confidently focus diplomatic resources on expansion and competition rather than alliance maintenance.
        - UpdatedTurn: 197
        
        ### Samarkand
        - Public: 55
        - Private: 55
        - Rationale: Samarkand relationship reduced from 60/60 to 55/55. China's dominance (281 vs 34) remains significant - Samarkand quest for Salt connection expires in 6 turns (95 influence potential). With Statecraft adoption pending (~30 turns), our efficiency gains for diplomatic missions will improve. Slight reduction reflects prioritization: new continent settlement (multiple 100% quality locations), Spaceship acceleration (Science 95), and Ur zone stabilization over contested city-state investment. Our 55/55 baseline keeps Samarkand accessible for future influence campaigns once core expansion and technology priorities advance, acknowledging that China's massive lead requires long-term strategic positioning rather than immediate competition.
        - UpdatedTurn: 200
        
        ### England
        - Public: 15
        - Private: 15
        - Rationale: Increasing England relationship from 5/5 to 15/15 to leverage shared strategic interests. England shares enemies (Rome, Netherlands) - they're at war with both, and we sanction England but recognize potential alignment. Their Golden Age ended, and their limited military (145 strength vs our 1319) presents no threat while their relative isolation creates diplomatic opportunities. Positive positioning opens potential for coordinated action against the Netherlands-Rome-Polynesia coalition without requiring significant resource investment. England could become a diplomatic counterweight or intelligence source against our primary naval adversary Netherlands.
        - UpdatedTurn: 256
        
        ### Polynesia
        - Public: -5
        - Private: -5
        - Rationale: Polynesia neutral (-5/-5) as peace treaty expires in 1 turn. De-escalation allows focus on Rome/Ethiopia and contributes to World Congress positioning.
        - UpdatedTurn: 292
        
        ### Ur
        - Public: -40
        - Private: -40
        - Rationale: Ur relationship maintained at -40/-40 consistency with active military operations. Field Gun bombardment confirmed successful (killed Gatling Gun). Diplomatic stance must match military actions to prevent AI confusion. China (Ur's ally via Defensive Pact to us) can mediate if negotiations desired, but our hostile posture should align with ongoing conquest. Ur's small population (11) and limited military value make it secondary priority to Ethiopian Oil-bearing cities. Maintains clearer war positioning while preserving diplomatic flexibility through China relationship.
        - UpdatedTurn: 324
        
        ### The Netherlands
        - Public: -20
        - Private: -20
        - Rationale: Netherlands hostility reduced from -30/-30 to -20/-20. They possess 57 Oil and 5802 military strength. With peace treaty potentially active, escalating to -30 risks multi-front war while also fighting Ethiopia for Oil. China's military (3899) provides alliance buffer, but avoiding provocation prevents diplomatic isolation during Ethiopia campaign.
        - UpdatedTurn: 339
        
        ### China
        - Public: 10
        - Private: 10
        - Rationale: Increasing China relationship from 8/10 to 10/10. China is fighting Netherlands alongside us (war score 4%) - they're our key ally. Their Golden Age just ended, their navy engages Netherlands forces. Strengthening this alliance is crucial for coordinated operations against Netherlands and potential Ethiopia Oil campaign once happiness stabilizes. China also provides diplomatic counterweight in World Congress. Maximum 10/10 reflects our most important diplomatic relationship.
        - UpdatedTurn: 347
        
        ### Rome
        - Public: 20
        - Private: 20
        - Rationale: Increasing England relationship from 15/15 to 20/20. England fights both our enemies (Rome, Netherlands) with limited military (145 vs our 1319), making them a safe diplomatic counterweight. They share DoF with Netherlands but are at war with Rome like us. Slight increment maintains positive positioning without significant investment, potentially useful intelligence source against Netherlands-Rome-Polynesia coalition while we focus on Ethiopia Oil cities.
        - UpdatedTurn: 353
        
        ### Ethiopia
        - Public: -20
        - Private: -20
        - Rationale: Ethiopia just declared war this turn and sank our Cruiser and Ironclad near Ur. Reducing from 10/10 to -20/-20 to reflect new hostile reality. Their Golden Age (2 turns) makes them temporarily stronger. With 29% happiness, we cannot afford positive diplomatic signaling toward an active aggressor. This also aligns AI expectations with our defensive response against their naval attacks near Ur.
        - UpdatedTurn: 355
        
        ## Strategy
        - Rationale: Adjusting for severe multi-front war crisis: MilitaryTraining increased to 90 to accelerate critical upgrades (Gatling Gun→Machine Gun upgrades completed this turn). Mobilization boosted to 80 to prioritize military production for defense. Happiness raised to 95 - at 41% happiness with combat penalty, addressing war weariness is critical for military effectiveness. NavalRecon increased to 85 as Ethiopian naval forces near Ur require enhanced detection. Science remains 100 - nuclear deterrent (Nuclear Fission) is ultimate security against Ethiopia's nuclear capability. Nuke/UseNuke maintained at 90/75 given Ethiopia's Manhattan Project and active aggression. Slightly reduced Growth/TileImprovement to reallocate capacity to urgent military and happiness needs. Spaceship at 100 as long-term goal continues despite wartime pressures.
        - GrandStrategy: Spaceship
        
        ### Flavors
        - Offense: 20
        - Defense: 95
        - Mobilization: 80
        - CityDefense: 90
        - MilitaryTraining: 90
        - Recon: 75
        - Ranged: 80
        - Mobile: 60
        - Nuke: 90
        - UseNuke: 75
        - Naval: 75
        - NavalRecon: 85
        - NavalGrowth: 65
        - NavalTileImprovement: 60
        - Air: 85
        - AirCarrier: 90
        - Antiair: 85
        - Airlift: 70
        - Expansion: 0
        - Growth: 70
        - TileImprovement: 70
        - Infrastructure: 75
        - Production: 80
        - WaterConnection: 75
        - Gold: 75
        - Science: 100
        - Culture: 65
        - Happiness: 95
        - GreatPeople: 65
        - Wonder: 5
        - Religion: 20
        - Diplomacy: 70
        - Spaceship: 100
        - Espionage: 80
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Ethiopia
        - Ethiopia:
          - CapitalsControlled:
            - Addis Ababa
            - Stockholm
          - CapitalsPercentage: 25
        - The Netherlands:
          - CapitalsControlled:
            - London
            - Amsterdam
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 5
        - Contender: Ethiopia
        - Assyria:
          - Influences:
            - Rome: Exotic (24%) - Rising Slowly (tourism/culture ratio 65%)
            - The Netherlands: Exotic (13%) - Rising Slowly (tourism/culture ratio 38%)
            - Ethiopia: Exotic (11%) - Rising Slowly (tourism/culture ratio 33%)
            - China: Familiar (39%) - Rising Slowly (tourism/culture ratio 108%)
            - Polynesia: Familiar (29%) - Rising Slowly (tourism/culture ratio 70%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - China:
          - Influences:
            - Rome: Familiar (38%) - Rising (499 turns to Influential, tourism/culture ratio 127%)
            - Assyria: Popular (78%) - Rising (17 turns to Influential, tourism/culture ratio 340%)
            - The Netherlands: Exotic (22%) - Rising Slowly (tourism/culture ratio 85%)
            - Ethiopia: Exotic (18%) - Rising Slowly (tourism/culture ratio 63%)
            - Polynesia: Familiar (45%) - Rising (495 turns to Influential, tourism/culture ratio 131%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Ethiopia:
          - Influences:
            - Rome: Influential (183%) - Rising (tourism/culture ratio 636%)
            - Assyria: Influential (108%) - Rising (tourism/culture ratio 571%)
            - Polynesia: Influential (149%) - Rising (tourism/culture ratio 481%)
            - China: Popular (86%) - Rising (8 turns to Influential, tourism/culture ratio 354%)
            - The Netherlands: Popular (93%) - Rising (4 turns to Influential, tourism/culture ratio 386%)
          - PolicyPercentage: 100
          - InfluentialCivs: 3
        - Polynesia:
          - Influences:
            - Rome: Popular (51%) - Rising (83 turns to Influential, tourism/culture ratio 180%)
            - Assyria: Familiar (41%) - Rising (115 turns to Influential, tourism/culture ratio 215%)
            - The Netherlands: Familiar (25%) - Rising Slowly (tourism/culture ratio 93%)
            - Ethiopia: Exotic (24%) - Rising Slowly (tourism/culture ratio 88%)
            - China: Familiar (31%) - Rising Slowly (tourism/culture ratio 115%)
          - PolicyPercentage: 88
          - InfluentialCivs: 0
        - Rome:
          - Influences:
            - Assyria: Familiar (39%) - Rising (215 turns to Influential, tourism/culture ratio 180%)
            - The Netherlands: Familiar (30%) - Rising Slowly (tourism/culture ratio 99%)
            - Ethiopia: Familiar (34%) - Rising Slowly (tourism/culture ratio 108%)
            - China: Familiar (31%) - Rising Slowly (tourism/culture ratio 108%)
            - Polynesia: Popular (56%) - Rising (108 turns to Influential, tourism/culture ratio 161%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Netherlands:
          - Influences:
            - Rome: Influential (123%) - Rising (tourism/culture ratio 379%)
            - Assyria: Popular (70%) - Rising (20 turns to Influential, tourism/culture ratio 366%)
            - Polynesia: Influential (103%) - Rising (tourism/culture ratio 322%)
            - Ethiopia: Popular (54%) - Rising (64 turns to Influential, tourism/culture ratio 198%)
            - China: Popular (57%) - Rising (58 turns to Influential, tourism/culture ratio 223%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        
        ## DiplomaticVictory
        - VotesNeeded: 44
        - Status: World Congress - Voting in 5 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: -1
          - Dutch Sphere of Influence: Sogut:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: -1
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: -1
          - Chinese Sphere of Influence: Holmul:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Chinese Sphere of Influence: Warsaw:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - EnactedOn: -1
          - Polynesian Sphere of Influence: Utica:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Scholars In Residence:
            - Description: Civilizations have -20% Research cost for Technologies already discovered by another Civilization. Additional -2% for every City-State Ally, up to -50%.
            - EnactedOn: -1
          - Chinese Sphere of Influence: Okilis:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Chinese Sphere of Influence: Samarkand:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
        - Proposals:
          - Enact: Sanction: The Netherlands:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - Proposer: Assyria
          - Enact: United Nations:
            - Description: Begins the United Nations project. Once underway, Civilizations can contribute Production towards its completion by selecting it in the city production list. When complete, Civilizations receive bonuses based on how much they contributed.
              : United Nations wonder appears in Capital. (Receive 1 Additional Delegate in the World Congress for every 8 City-States originally in the World. Also, when you expend a Great Person, earn 25 Influence with all City-States you have met. Triggers a Golden Age, as well as the United Nations Special Session of the World Congress if the world has reached the Atomic Era.)
              : Receive an immediate boost of 25 Influence with all City-States. The Consulate National Wonder appears in Capital. (Receive 1 Additional Delegate in the World Congress for every 8 City-States originally in the World.)
              : Receive a free Great Diplomat.
              Available once any Civilization discovers Atomic Theory.
            - Proposer: The Netherlands
          - Repeal: Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - Proposer: China
        - Contender: The Netherlands
        - Assyria:
          - Delegates: 9
          - VictoryPercentage: 20
        - China:
          - Delegates: 12
          - VictoryPercentage: 27
        - Ethiopia:
          - Delegates: 11
          - VictoryPercentage: 25
        - Polynesia:
          - Delegates: 10
          - VictoryPercentage: 22
        - Rome:
          - Delegates: 7
          - VictoryPercentage: 15
        - The Netherlands:
          - Delegates: 20
          - VictoryPercentage: 45
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Ethiopia
        - Leader: Haile Selassie
        - IsMajor: true
        - OurOpinionToThem:
          - You have both chosen to adopt the Order Ideology. (999)
          - Our real approach is War.
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Our leader has expressed a public opinion to this player (-20).
          - Our leader has formed a private opinion to this player (-20).
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have both chosen to adopt the Order Ideology.
          - You are not competing for World Wonders.
          - You are not competing for cultural advancement.
          - You have no contested borders.
          - They have denounced us!
          - They are spreading their own religion, but you converted some of their cities to your religion.
          - Your votes opposed their civ's interests in the World Congress.
          - Your success worries them.
          - Religious differences strain your relationship.
          - Your spies were caught stealing from them.
          - You have made a Defensive Pact with one of their enemies!
          - You have made a Declaration of Friendship with one of their enemies!
          - You have denounced a leader they made a Declaration of Friendship with!
          - Their friends or allies have denounced you!
          - They disliked our proposal to the World Congress.
          - You are at war!
        - Score: 2442
        - Era: Atomic
        - Technologies: 60
        - Cities: 9
        - Population: 195
        - Territory: 294
        - Gold: 987
        - GoldPerTurn: 230
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 4289
        - TourismPerTurn: 1199.5
        - CulturePerTurn: 2186
        - PolicyBranches:
          - Progress: 6
          - Order: 7
          - Rationalism: 6
          - Artistry: 6
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 5
          - Ivory: 1
          - Gold: 1
          - Paper: 6
          - Glass: 1
          - Maize: 1
          - Gems: 1
          - Salt: 3
          - Aluminum: 40
          - Lapis Lazuli: 2
          - Bison: 4
          - Amber: 4
          - Deer: 11
          - Jade: 2
          - Dyes: 1
          - Iron: 3
          - Coal: 5
          - Fish: 9
          - Uranium: 7
          - Citrus: 1
          - Stone: 4
          - Marble: 1
          - Furs: 6
          - Oil: 5
        - FoundedReligion: Eastern Orthodoxy
        - Relationships:
          - Rome:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Assyria:
            - Distance: Close
            - War (Our Score: 4%; Our War Weariness: 1%)
            - Denounced Them
          - Polynesia:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - China:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - The Netherlands:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
        - Votes: 11
        - 1: Defeated Major Civilization England
        
        ## Player 2
        - Civilization: Polynesia
        - Leader: Kamehameha
        - IsMajor: true
        - OurOpinionToThem:
          - You have both chosen to adopt the Order Ideology. (999)
          - We are trade partners. (10)
          - We have Pledged to Protect the same City-States. (7)
          - Our real approach is Guarded.
          - They are spreading their own religion, but you converted some of their cities to your religion. (-2)
          - We have divergent Social Policies. (-3)
          - Our leader has expressed a public opinion to this player (-5).
          - Our leader has formed a private opinion to this player (-5).
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the World Congress. (-36)
        - TheirOpinionToUs:
          - You have both chosen to adopt the Order Ideology.
          - You are not competing for World Wonders.
          - We have Pledged to Protect the same City-States.
          - We are trade partners.
          - You have gone to war in the past.
          - We have divergent Social Policies.
          - They don't want anything to do with us right now.
          - You have conquered City-States under their protection!
          - They are spreading their own religion, but you converted some of their cities to your religion.
          - Your military deployment is threatening.
          - Territorial disputes strain your relationship.
          - You have made a Defensive Pact with one of their enemies!
          - You have made a Declaration of Friendship with one of their enemies!
          - Religious differences strain your relationship.
          - We defeated their proposal in the World Congress.
          - Your votes opposed their civ's interests in the World Congress.
          - Your recent diplomatic actions disappoint them.
          - Their friends or allies have denounced you!
          - Your spies were caught stealing from them.
          - They fear you are competing with them.
          - They are jealous of our superior culture!
          - We have denounced each other!
          - They disliked our proposal to the World Congress.
        - Score: 1811
        - Era: Modern
        - Technologies: 57
        - Cities: 7
        - Population: 147
        - Territory: 300
        - Gold: 1726
        - GoldPerTurn: 688
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 3522
        - TourismPerTurn: 500.25
        - CulturePerTurn: 1261
        - PolicyBranches:
          - Statecraft: 6
          - Order: 2
          - Tradition: 6
          - Industry: 6
        - ResourcesAvailable:
          - Wheat: 2
          - Ivory: 1
          - Gold: 1
          - Paper: 9
          - Gems: 6
          - Salt: 2
          - Aluminum: 10
          - Lapis Lazuli: 1
          - Amber: 2
          - Deer: 2
          - Whales: 1
          - Coal: 1
          - Cattle: 1
          - Horses: 1
          - Jewelry: 1
          - Fish: 10
          - Bison: 1
          - Incense: 1
          - Stone: 1
          - Crab: 1
          - Furs: 1
          - Dyes: 1
          - Oil: 8
        - FoundedReligion: Catholicism
        - Relationships:
          - Rome:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Assyria:
            - Distance: Neighbors
            - Denounced Them
          - The Netherlands:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - China:
            - Distance: Close
            - Denounced Them
        - Votes: 10
        
        ## Player 3
        - Civilization: The Netherlands
        - Leader: William
        - IsMajor: true
        - OurOpinionToThem:
          - You have both chosen to adopt the Order Ideology. (999)
          - We have Pledged to Protect the same City-States. (7)
          - Our real approach is War.
          - We have divergent Social Policies. (-3)
          - They are spreading their own religion, but you converted some of their cities to your religion. (-8)
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Our leader has expressed a public opinion to this player (-20).
          - Our leader has formed a private opinion to this player (-20).
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have both chosen to adopt the Order Ideology.
          - We passed their proposal in the World Congress.
          - We have Pledged to Protect the same City-States.
          - You have no contested borders.
          - They have denounced us!
          - You have conquered City-States under their protection!
          - You are competing for World Wonders.
          - We have divergent Social Policies.
          - You have denounced a leader they made a Declaration of Friendship with!
          - Religious differences strain your relationship.
          - Their friends or allies have denounced you!
          - We tried to place sanctions on them in the World Congress.
          - You have made a Defensive Pact with one of their enemies!
          - You have made a Declaration of Friendship with one of their enemies!
          - They disliked our proposal to the World Congress.
          - Your votes opposed their civ's interests in the World Congress.
          - You are at war!
        - Score: 2741
        - Era: Atomic
        - Technologies: 61
        - Cities: 16
        - Population: 313
        - Territory: 536
        - Gold: 8832
        - GoldPerTurn: 1673
        - HappinessSituation: Happy
        - HappinessPercentage: 86
        - MilitaryStrength: 7879
        - TourismPerTurn: 1010.5
        - CulturePerTurn: 2258
        - PolicyBranches:
          - Tradition: 6
          - Rationalism: 1
          - Statecraft: 6
          - Order: 6
          - Industry: 6
        - ResourcesAvailable:
          - Wheat: 3
          - Sheep: 6
          - Figs: 2
          - Ivory: 1
          - Gold: 2
          - Paper: 11
          - Maize: 3
          - Rice: 4
          - Gems: 4
          - Salt: 2
          - Aluminum: 14
          - Lapis Lazuli: 4
          - Fish: 19
          - Amber: 1
          - Deer: 4
          - Whales: 1
          - Sugar: 1
          - Jade: 2
          - Iron: 3
          - Dyes: 7
          - Coal: 78
          - Cattle: 2
          - Uranium: 6
          - Horses: 8
          - Bison: 1
          - Citrus: 1
          - Crab: 1
          - Incense: 1
          - Stone: 3
          - Furs: 1
          - Bananas: 7
          - Oil: 64
          - Porcelain: 1
        - FoundedReligion: Buddhism
        - Relationships:
          - Rome:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Assyria:
            - Distance: Neighbors
            - War (Our Score: 10%; Our War Weariness: 14%)
            - Denounced Them
          - Polynesia:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
          - China:
            - Distance: Close
            - War (Our Score: -2%; Our War Weariness: 15%)
            - Denounced Them
        - Votes: 20
        - 4: Defeated Major Civilization Sweden
        
        ## Player 5
        - Civilization: China
        - Leader: Wu Zetian
        - IsMajor: true
        - OurOpinionToThem:
          - You have adopted their religion in the majority of your cities. (60)
          - We fought together against a common foe. (43)
          - We are trade partners. (40)
          - We have made a Defensive Pact! (20)
          - We have opened our borders to each other. (12)
          - You have denounced one of their declared enemies! (11)
          - Our leader has expressed a public opinion to this player (10).
          - Our leader has formed a private opinion to this player (10).
          - We have made a public Declaration of Friendship! (9)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Our real approach is Friendly.
          - You have chosen to adopt the Freedom Ideology, but they believe in Order. (-999)
        - TheirOpinionToUs:
          - Your votes supported their civ's interests in the World Congress.
          - The leader has expressed a public opinion to you (100).
          - We passed their proposal in the World Congress.
          - We have made a Defensive Pact!
          - We are trade partners.
          - They liked our proposal to the World Congress.
          - Your recent diplomatic actions please them.
          - You have denounced one of their declared enemies!
          - We have similar Social Policies.
          - We have made a public Declaration of Friendship!
          - We fought together against a common foe.
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - They have happily adopted your religion in the majority of their cities.
          - We have shared embassies.
          - You have chosen to adopt the Order Ideology, but they believe in Freedom.
          - They desire friendly relations with our empire.
        - Score: 2359
        - Era: Modern
        - Technologies: 58
        - Cities: 15
        - Population: 317
        - Territory: 361
        - Gold: 11623
        - GoldPerTurn: 690
        - HappinessSituation: Happy
        - HappinessPercentage: 63
        - MilitaryStrength: 4727
        - TourismPerTurn: 553.5
        - CulturePerTurn: 1275
        - PolicyBranches:
          - Freedom: 3
          - Tradition: 2
          - Rationalism: 1
          - Progress: 2
          - Authority: 3
          - Fealty: 1
          - Industry: 2
          - Artistry: 2
          - Statecraft: 6
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 3
          - Ivory: 3
          - Paper: 4
          - Rice: 3
          - Cotton: 6
          - Salt: 3
          - Aluminum: 6
          - Maize: 3
          - Deer: 9
          - Whales: 2
          - Sugar: 1
          - Iron: 4
          - Jade: 1
          - Coal: 2
          - Cattle: 5
          - Marble: 2
          - Horses: 1
          - Coral: 1
          - Jewelry: 2
          - Fish: 18
          - Bison: 3
          - Citrus: 4
          - Stone: 3
          - Crab: 1
          - Bananas: 1
          - Wine: 1
          - Porcelain: 1
          - Cocoa: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Rome:
            - Distance: Far
          - Assyria:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Close
            - War (Our Score: 2%; Our War Weariness: 15%)
          - Ethiopia:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
            - Denounced By Them
          - Polynesia:
            - Distance: Close
            - Denounced Them
        - Votes: 12
        
        ## Player 6
        - Civilization: Assyria
        - Leader: Ashurbanipal
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: China, Our top defensive pact ally: China
          - Our top World Congress ally: China, Our top World Congress rival: The Netherlands
          - Our top Competitor: Ethiopia
        - Score: 1895
        - Era: Atomic
        - GoldenAge: Estimated in 69 turns
        - Technologies: 61
        - CurrentResearch: Rocketry (Estimated in 14 turns)
        - NextPolicyTurns: 12
        - Cities: 12
        - Population: 218
        - Territory: 322
        - BestSettlementLocation:
          - 66, 49 (Quality: 0%; 4 tiles from us)
          - 67, 48 (Quality: 0%; 4 tiles from us)
          - 66, 50 (Quality: 0%; 4 tiles from us)
          - 67, 49 (Quality: 0%; 5 tiles from us)
          - 68, 48 (Quality: 0%; 5 tiles from us)
        - Gold: 95
        - GoldPerTurn: 505
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 42
        - MilitaryUnits: 32
        - MilitarySupply: 51
        - MilitaryStrength: 2107
        - TourismPerTurn: 268.25
        - CulturePerTurn: 963
        - FaithPerTurn: 431
        - SciencePerTurn: 1269
        - PolicyBranches:
          - Fealty:
            - Fealty
          - Order:
            - Peace, Land, Bread
          - Artistry:
            - Artistry
            - Refinement
            - National Treasure
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Shadow Networks
            - Trade Confederacy
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Enlightenment
            - Free Thought
          - Progress:
            - Progress
            - Organization
            - Liberty
            - Expertise
            - Equality
            - Fraternity
          - Authority:
            - Authority
        - ResourcesAvailable:
          - Wheat: 3
          - Silver: 0
          - Sheep: 3
          - Cloves: 0
          - Figs: 0
          - Ivory: 1
          - Gold: 0
          - Nutmeg: 0
          - Pearls: 0
          - Paper: 6
          - Rice: 1
          - Cotton: 2
          - Gems: 0
          - Salt: 0
          - Brazilwood: 0
          - Aluminum: 13
          - Maize: 5
          - Glass: 0
          - Lapis Lazuli: 0
          - Amber: 0
          - Coffee: 0
          - Deer: 4
          - Whales: 2
          - Perfume: 0
          - Sugar: 1
          - Olives: 0
          - Iron: 2
          - Jade: 1
          - Cinnamon: 0
          - Coal: 0
          - Tea: 0
          - Cattle: 5
          - Pepper: 0
          - Marble: 2
          - Horses: 7
          - Coral: 7
          - Silk: 0
          - Jewelry: 0
          - Fish: 10
          - Bison: 6
          - Antiquity Site: 0
          - Copper: 0
          - Truffles: 0
          - Citrus: 1
          - Incense: 0
          - Stone: 4
          - Crab: 0
          - Furs: 0
          - Dyes: 0
          - Oil: 0
          - Bananas: 2
          - Wine: 1
          - Porcelain: 1
          - Cocoa: 1
          - Tobacco: 0
        - FoundedReligion: Zoroastrianism
        - Relationships:
          - Rome:
            - Distance: Close
          - The Netherlands:
            - Distance: Neighbors
            - War (Our Score: -10%; Our War Weariness: 19%)
          - Ethiopia:
            - Distance: Close
            - War (Our Score: -4%; Our War Weariness: 3%)
          - China:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Polynesia:
            - Distance: Neighbors
            - Denounced Them
        - OutgoingTradeRoutes:
          - Kanesh (Assyria) => Raiatea (Polynesia):
            - ToGold: 3.5
            - TurnsLeft: 13
            - FromScience: 5
            - Domain: Land
            - FromGold: 25.31
            - ToScience: 3
          - Dur-Sharrukin (Assyria) => Macau (China):
            - ToGold: 9
            - TurnsLeft: 15
            - FromScience: 5
            - Domain: Land
            - FromGold: 36.58
            - FromCulture: 15
            - ToScience: 2
          - Assur (Assyria) => Shanghai (China):
            - ToGold: 11.25
            - TurnsLeft: 4
            - FromScience: 5
            - Domain: Sea
            - FromGold: 46.41
            - FromCulture: 15
            - ToScience: 2
          - Available: 5
        - IncomingTradeRoutes:
          - Shanghai (China) => Halab (Assyria):
            - ToGold: 7
            - TurnsLeft: 24
            - FromScience: 20
            - Domain: Land
            - FromGold: 57.36
            - ToCulture: 2
          - Xian (China) => Kar-Tukulti-Ninurta (Assyria):
            - ToGold: 13.75
            - TurnsLeft: 27
            - FromScience: 20
            - Domain: Land
            - FromGold: 61.75
            - ToCulture: 2
          - Beijing (China) => Carchemish (Assyria):
            - ToGold: 5.25
            - TurnsLeft: 20
            - FromScience: 20
            - Domain: Land
            - FromGold: 41.58
            - ToCulture: 2
          - Xian (China) => Nuku Hiva (Assyria):
            - ToGold: 8.75
            - TurnsLeft: 34
            - FromScience: 20
            - Domain: Sea
            - FromGold: 57.04
            - ToCulture: 2
          - Shanghai (China) => Nimrud (Assyria):
            - ToGold: 8.75
            - TurnsLeft: 25
            - FromScience: 20
            - Domain: Land
            - FromGold: 59.62
            - ToCulture: 2
        - Spies:
          - Agent Asnappar (2):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 577
            - Location: Stockholm (Ethiopia)
            - NetworkPerTurn: 27
          - Agent Pazuzu (6):
            - State: Counter-intelligence
            - Role: Counterspy
            - Location: Ur (Assyria)
            - NetworkPerTurn: 0
          - Agent Qingu (1):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 585
            - Location: Harar (Ethiopia)
            - NetworkPerTurn: 27
          - Agent Shamash (5):
            - State: Traveling
            - Role: Counterspy
            - Location: Arnhem (Assyria)
            - NetworkPerTurn: 0
          - Agent Nisroch (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 581
            - Location: Axum (Ethiopia)
            - NetworkPerTurn: 27
          - Agent Naramsin (3):
            - State: Killed In Action
            - Role: Spy
            - Location: Unassigned
            - NetworkPerTurn: 0
          - Agent Ugallu (0):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 610
            - Location: Honolulu (Polynesia)
            - NetworkPerTurn: 40
          - Agent Seruya (8):
            - State: Traveling
            - Role: Spy
            - Location: Abernethy (City-State Abernethy)
            - NetworkPerTurn: 0
          - Agent Nukimmut (7):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 839
            - Location: Gondar (Ethiopia)
            - NetworkPerTurn: 28
        - DiplomaticDeals:
          - China:
            - #0:
              - WeGive:
                - 17 Gold per Turn
              - TheyGive:
                - 1 Ivory
                - 2 Iron
              - TurnsRemaining: 1
            - #1:
              - WeGive:
                - 1 Jade
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 3
            - #2:
              - TheyGive:
                - 99 Gold per Turn
              - TurnsRemaining: 4
            - #3:
              - WeGive:
                - 1 Wine
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 14
            - #4:
              - WeGive:
                - Open Borders
              - TheyGive:
                - Open Borders
              - TurnsRemaining: 16
            - #5:
              - WeGive:
                - Defensive Pact
              - TheyGive:
                - Defensive Pact
              - TurnsRemaining: 19
            - #6:
              - WeGive:
                - 1 Coral
              - TheyGive:
                - 6 Gold per Turn
              - TurnsRemaining: 23
            - #7:
              - WeGive:
                - 24 Gold per Turn
              - TheyGive:
                - 1 Porcelain
              - TurnsRemaining: 39
            - #8:
              - WeGive:
                - 31 Gold per Turn
              - TheyGive:
                - 1 Cocoa
              - TurnsRemaining: 42
        - Votes: 9
        
        ## Player 7
        - Civilization: Rome
        - Leader: Augustus Caesar
        - IsMajor: true
        - OurOpinionToThem:
          - Our leader has expressed a public opinion to this player (20).
          - Our leader has formed a private opinion to this player (20).
          - We have similar Social Policies. (3)
          - You have gone to war in the past.
          - Our real approach is Guarded.
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Religious differences strain your relationship. (-30)
          - You have chosen to adopt the Autocracy Ideology, but they believe in Order. (-999)
        - TheirOpinionToUs:
          - We have similar Social Policies.
          - You have no contested borders.
          - Your votes supported their civ's interests in the World Congress.
          - You have gone to war in the past.
          - They have denounced us!
          - They suspect we might be a threat to them.
          - Religious differences strain your relationship.
          - You are competing for the favor of the same City-States!
          - You have made a Defensive Pact with one of their enemies!
          - You have made a Declaration of Friendship with one of their enemies!
          - You have denounced a leader they made a Declaration of Friendship with!
          - Your recent diplomatic actions disappoint them.
          - Their friends or allies have denounced you!
          - They disliked our proposal to the World Congress.
          - You have chosen to adopt the Order Ideology, but they believe in Autocracy.
        - Score: 1755
        - Era: Modern
        - Technologies: 54
        - Cities: 7
        - Population: 149
        - Territory: 160
        - Gold: 959
        - GoldPerTurn: 488
        - HappinessSituation: Happy
        - HappinessPercentage: 62
        - MilitaryStrength: 3957
        - TourismPerTurn: 500.25
        - CulturePerTurn: 998
        - PolicyBranches:
          - Autocracy: 2
          - Rationalism: 2
          - Tradition: 1
          - Artistry: 1
          - Statecraft: 6
          - Imperialism: 2
          - Progress: 2
          - Authority: 5
        - ResourcesAvailable:
          - Wheat: 1
          - Silver: 1
          - Sheep: 3
          - Figs: 24
          - Gold: 7
          - Paper: 7
          - Rice: 3
          - Gems: 1
          - Salt: 1
          - Maize: 2
          - Lapis Lazuli: 1
          - Amber: 2
          - Deer: 4
          - Iron: 4
          - Coal: 6
          - Marble: 1
          - Horses: -2
          - Jewelry: 1
          - Fish: 1
          - Citrus: 1
          - Crab: 1
          - Furs: 1
          - Dyes: 2
          - Oil: 8
          - Bananas: 3
          - Porcelain: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Assyria:
            - Distance: Close
            - Denounced Them
          - The Netherlands:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - China:
            - Distance: Far
            - Denounced Them
          - Polynesia:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 7
        
        ## Player 22
        - Civilization: Abernethy
        - Leader: City State
        - MajorAlly: Polynesia
        - Population: 20
        - ResourcesAvailable:
          - Fish: 1
        - MajorityReligion: Zoroastrianism
        - Relationships:
          - Rome: Friends (Influence: 377, Distance: Close)
          - Assyria: Neutral (Influence: 16, Distance: Close)
          - The Netherlands: Friends (Influence: 414, Distance: Neighbors, Protected)
          - Ethiopia: Friends (Influence: 71, Distance: Far)
          - China: Neutral (Influence: 4, Distance: Close, Protected)
          - Polynesia: Ally (Influence: 441, Distance: Neighbors, Protected)
        - Quests:
          -  They want you to demand tribute from Singapore. Potential Quest Reward: * 140 Influence * 385 Gold
        
        ## Player 23
        - Civilization: Singapore
        - Leader: City State
        - MajorAlly: Rome
        - Population: 16
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Rome: Ally (Influence: 512, Distance: Neighbors, Protected)
          - Assyria: Friends (Influence: 45, Distance: Far)
          - The Netherlands: Friends (Influence: 105, Distance: Neighbors, Protected)
          - Ethiopia: Friends (Influence: 103, Distance: Close)
          - China: Friends (Influence: 45, Distance: Far)
          - Polynesia: Friends (Influence: 475, Distance: Close)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 24
        - Civilization: Utica
        - Leader: City State
        - MajorAlly: Polynesia
        - Population: 23
        - ResourcesAvailable:
          - Fish: 4
        - MajorityReligion: Zoroastrianism
        - Relationships:
          - Rome: Neutral (Influence: 0, Distance: Distant)
          - Assyria: Friends (Influence: 44, Distance: Close, Protected)
          - The Netherlands: Friends (Influence: 101, Distance: Close, Protected)
          - Ethiopia: Friends (Influence: 98, Distance: Close)
          - China: Neutral (Influence: 0, Distance: Far)
          - Polynesia: Ally (Influence: 219, Distance: Neighbors, Protected)
        - Quests:
          -  They want you to demand tribute from Sogut. Potential Quest Reward: * 109 Influence * 457 Gold
          - They want you to generate a Great Diplomat. (Turns remaining: 46) Potential Quest Reward: * 124 Influence * 320 Culture
        
        ## Player 25
        - Civilization: Venezia
        - Leader: City State
        - MajorAlly: Ethiopia
        - Population: 14
        - ResourcesAvailable:
          - Fish: 1
          - Deer: 2
          - Sheep: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Rome: Neutral (Influence: 29, Distance: Far, Protected)
          - Assyria: War (Influence: -60, Distance: Distant)
          - The Netherlands: Friends (Influence: 53, Distance: Neighbors)
          - Ethiopia: Ally (Influence: 440, Distance: Neighbors, Protected)
          - China: War (Influence: -60, Distance: Distant)
          - Polynesia: Neutral (Influence: 0, Distance: Far, Protected)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 26
        - Civilization: M'banza-Kongo
        - Leader: City State
        - MajorAlly: Ethiopia
        - Population: 16
        - ResourcesAvailable:
          - Fish: 3
          - Deer: 1
          - Stone: 1
        - Relationships:
          - Rome: Friends (Influence: 59, Distance: Close)
          - Assyria: War (Influence: -60, Distance: Neighbors)
          - The Netherlands: Friends (Influence: 84, Distance: Close, Protected)
          - Ethiopia: Ally (Influence: 101, Distance: Close, Protected)
          - China: War (Influence: -60, Distance: Distant)
          - Polynesia: Neutral (Influence: -19, Distance: Neighbors)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 27
        - Civilization: Warsaw
        - Leader: City State
        - MajorAlly: China
        - Population: 22
        - ResourcesAvailable:
          - Deer: 1
          - Fish: 3
        - MajorityReligion: Zoroastrianism
        - Relationships:
          - Rome: Friends (Influence: 45, Distance: Distant)
          - Assyria: Neutral (Influence: 0, Distance: Far)
          - The Netherlands: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - China: Ally (Influence: 398, Distance: Neighbors, Protected)
          - Polynesia: Friends (Influence: 70, Distance: Far, Protected)
        - Quests:
          -  Conduct a Spy Mission against Augustus Caesar. Potential Quest Reward: * 345 Influence * 817 Science
        - 28: Defeated Minor Civilization Ur
        
        ## Player 29
        - Civilization: Kathmandu
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 21
        - ResourcesAvailable:
          - Fish: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - Rome: Friends (Influence: 251, Distance: Neighbors, Protected)
          - Assyria: War (Influence: -60, Distance: Distant)
          - The Netherlands: Ally (Influence: 628, Distance: Neighbors, Protected)
          - Ethiopia: Friends (Influence: 71, Distance: Close, Protected)
          - China: War (Influence: -60, Distance: Distant)
          - Polynesia: Neutral (Influence: -42, Distance: Far)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 30
        - Civilization: Lutetia
        - Leader: City State
        - MajorAlly: Ethiopia
        - Population: 16
        - ResourcesAvailable:
          - Deer: 2
          - Fish: 1
        - MajorityReligion: Zoroastrianism
        - Relationships:
          - Rome: Friends (Influence: 192, Distance: Distant)
          - Assyria: War (Influence: -60, Distance: Distant)
          - The Netherlands: Friends (Influence: 53, Distance: Far, Protected)
          - Ethiopia: Ally (Influence: 361, Distance: Distant, Protected)
          - China: War (Influence: -60, Distance: Close)
          - Polynesia: Neutral (Influence: 17, Distance: Distant)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 31
        - Civilization: Holmul
        - Leader: City State
        - MajorAlly: China
        - Population: 20
        - ResourcesAvailable:
          - Fish: 2
          - Sheep: 1
        - MajorityReligion: Zoroastrianism
        - Relationships:
          - Rome: Friends (Influence: 45, Distance: Distant)
          - Assyria: Friends (Influence: 203, Distance: Far)
          - The Netherlands: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - China: Ally (Influence: 653, Distance: Neighbors, Protected)
          - Polynesia: Friends (Influence: 45, Distance: Distant)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        - 32: Defeated Minor Civilization Harappa
        
        ## Player 33
        - Civilization: Sogut
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 22
        - ResourcesAvailable:
          - Fish: 2
        - MajorityReligion: Zoroastrianism
        - Relationships:
          - Rome: Friends (Influence: 42, Distance: Distant)
          - Assyria: War (Influence: -60, Distance: Close)
          - The Netherlands: Ally (Influence: 554, Distance: Neighbors, Protected)
          - Ethiopia: Friends (Influence: 175, Distance: Close)
          - China: War (Influence: -60, Distance: Far)
          - Polynesia: Friends (Influence: 67, Distance: Close, Protected)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 34
        - Civilization: Byblos
        - Leader: City State
        - MajorAlly: Rome
        - Population: 17
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Rome: Ally (Influence: 207, Distance: Close, Protected)
          - Assyria: Neutral (Influence: -27, Distance: Close)
          - The Netherlands: Friends (Influence: 53, Distance: Close, Protected)
          - Ethiopia: Friends (Influence: 78, Distance: Neighbors, Protected)
          - China: Neutral (Influence: 17, Distance: Distant)
          - Polynesia: Friends (Influence: 146, Distance: Close, Protected)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 35
        - Civilization: Brandenburg
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Rome: Friends (Influence: 55, Distance: Neighbors, Protected)
          - Assyria: War (Influence: -60, Distance: Far)
          - The Netherlands: Ally (Influence: 450, Distance: Neighbors, Protected)
          - Ethiopia: Friends (Influence: 232, Distance: Neighbors, Protected)
          - China: War (Influence: -60, Distance: Distant)
          - Polynesia: Friends (Influence: 45, Distance: Far)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 36
        - Civilization: Samarkand
        - Leader: City State
        - MajorAlly: China
        - Population: 20
        - MajorityReligion: Zoroastrianism
        - Relationships:
          - Rome: Friends (Influence: 45, Distance: Distant)
          - Assyria: Friends (Influence: 364, Distance: Neighbors)
          - The Netherlands: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - China: Ally (Influence: 648, Distance: Neighbors, Protected)
          - Polynesia: Friends (Influence: 45, Distance: Far)
        - Quests:
          -  Diplomatic Missions are temporarily more effective. (Turns remaining: 24) They want you to start a land or sea trade route to their city. (Turns remaining: 24) Potential Quest Reward: * 204 Influence * 163 Food in Capital
        
        ## Player 37
        - Civilization: Okilis
        - Leader: City State
        - MajorAlly: China
        - Population: 19
        - ResourcesAvailable:
          - Fish: 1
        - MajorityReligion: Zoroastrianism
        - Relationships:
          - Rome: Neutral (Influence: 0, Distance: Far)
          - Assyria: Friends (Influence: 60, Distance: Neighbors, Protected)
          - The Netherlands: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - China: Ally (Influence: 377, Distance: Neighbors, Protected)
          - Polynesia: Friends (Influence: 158, Distance: Far)
        - Quests:
          -  They will reward the player(s) with the largest number of new Followers. So far, you have the lead with 97 new Followers (Turns remaining: 4) Potential Quest Reward: * 206 Influence * 185 Great Person Points in all Cities
          - They want you to start a land or sea trade route to their city. (Turns remaining: 45) Potential Quest Reward: * 173 Influence * 230 Food in Capital
          - They want you to demand tribute from Abernethy. Potential Quest Reward: * 128 Influence * 359 Gold
          - They want you to defeat Barbarian units that are invading their territory. You are allowed to enter their territory until the Barbarians are defeated.
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: Ethiopia
        
        ### Addis Ababa
        - ID: 1057
        - X: 12
        - Y: 43
        - Population: 28
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 69
        - Wonders:
          - Heroic Epic
          - Circus Maximus
          - Ironworks
          - Hagia Sophia
          - Porcelain Tower
          - Sistine Chapel
          - Forbidden Palace
          - Taj Mahal
          - Eiffel Tower
          - Palace of Culture and Science
          - Karlstejn
          - Grand Ossuary
          - Giorgio Armeier Headquarters
        
        ### Harar
        - ID: 1292
        - X: 7
        - Y: 42
        - Population: 23
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 61
        - IsCoastal: true
        - Wonders:
          - Colossus
          - Hanging Gardens
          - Grand Temple
          - Globe Theatre
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
        
        ### Adwa
        - ID: 1410
        - X: 13
        - Y: 48
        - Population: 21
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 68
        - IsCoastal: true
        
        ### Lalibela
        - ID: 1787
        - X: 16
        - Y: 40
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 68
        - Wonders:
          - School of Philosophy
          - National Monument
          - Chartered Company
          - Imperial College
          - Royal Collection
        
        ### Gondar
        - ID: 2021
        - X: 6
        - Y: 38
        - Population: 25
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 61
        - IsCoastal: true
        
        ### Axum
        - ID: 5761
        - X: 5
        - Y: 13
        - Population: 23
        - DefenseStrength: 62
        - IsCoastal: true
        
        ### Dire Dawa
        - ID: 6096
        - X: 7
        - Y: 31
        - Population: 21
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 63
        - IsCoastal: true
        
        ### Stockholm
        - ID: 10059
        - X: 21
        - Y: 39
        - Population: 24
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 71
        - IsOccupied: true
        - Wonders:
          - Pyramids
          - Louvre
          - Statue of Zeus
          - Mausoleum of Halicarnassus
          - Terracotta Army
        
        ### Hilo
        - ID: 13053
        - X: 76
        - Y: 41
        - Population: 10
        - DefenseStrength: 41
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Polynesia
        
        ### Honolulu
        - ID: 1059
        - X: 25
        - Y: 11
        - Population: 33
        - DefenseStrength: 72
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Royal Collection
          - Great Lighthouse
          - Stonehenge
          - Great Library
          - Oracle
          - Great Wall
          - Angkor Wat
          - Grand Temple
          - Borobudur
          - Scrivener's Office
          - Printing Press
          - Roman Forum
          - Nalanda
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Samoa
        - ID: 4352
        - X: 29
        - Y: 16
        - Population: 21
        - DefenseStrength: 61
        - IsCoastal: true
        
        ### Tonga
        - ID: 4569
        - X: 27
        - Y: 7
        - Population: 21
        - DefenseStrength: 59
        - IsCoastal: true
        - Wonders:
          - Imperial College
        
        ### Raiatea
        - ID: 6009
        - X: 63
        - Y: 37
        - Population: 18
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 69
        - IsCoastal: true
        
        ### Helsinki
        - ID: 7686
        - X: 26
        - Y: 41
        - Population: 20
        - DefenseStrength: 74
        - IsOccupied: true
        - IsCoastal: true
        
        ### Aotearoa
        - ID: 7857
        - X: 68
        - Y: 39
        - Population: 17
        - DefenseStrength: 66
        - IsCoastal: true
        
        ### Tahiti
        - ID: 8829
        - X: 72
        - Y: 46
        - Population: 17
        - DefenseStrength: 66
        - IsCoastal: true
        
        ## Player: The Netherlands
        
        ### Amsterdam
        - ID: 1079
        - X: 29
        - Y: 30
        - Population: 42
        - MajorityReligion: Buddhism
        - DefenseStrength: 81
        - Wonders:
          - Heroic Epic
          - National Monument
          - Chartered Company
          - Royal Collection
          - Kremlin
          - Palace of Westminster
          - Brandenburg Gate
          - Temple of Artemis
          - Grand Temple
          - Uffizi
          - Broadway
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - Palace of Culture and Science
          - Summer Palace
          - Menin Gate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Mausoleum
          - Hexxon Refineries Headquarters
        
        ### Rotterdam
        - ID: 1284
        - X: 27
        - Y: 37
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 67
        - IsCoastal: true
        
        ### Utrecht
        - ID: 1433
        - X: 27
        - Y: 25
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 78
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Ironworks
          - University of Sankore
          - Neuschwanstein
        
        ### Groningen
        - ID: 2097
        - X: 24
        - Y: 20
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - Wonders:
          - Imperial College
        
        ### Breda
        - ID: 2445
        - X: 22
        - Y: 15
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Nijmegen
        - ID: 3016
        - X: 18
        - Y: 17
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 75
        - IsCoastal: true
        
        ### The Hague
        - ID: 4765
        - X: 28
        - Y: 21
        - Population: 19
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - Wonders:
          - Cristo Redentor
        
        ### York
        - ID: 7923
        - X: 9
        - Y: 35
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 67
        - IsOccupied: true
        - IsCoastal: true
        
        ### Haarlem
        - ID: 8090
        - X: 65
        - Y: 26
        - Population: 17
        - DefenseStrength: 69
        - IsCoastal: true
        
        ### London
        - ID: 9932
        - X: 13
        - Y: 28
        - Population: 20
        - MajorityReligion: Buddhism
        - DefenseStrength: 71
        - IsOccupied: true
        - IsCoastal: true
        
        ### Zutphen
        - ID: 10212
        - X: 14
        - Y: 15
        - Population: 17
        - DefenseStrength: 46
        - IsCoastal: true
        
        ### Maastricht
        - ID: 10822
        - X: 9
        - Y: 20
        - Population: 17
        - MajorityReligion: Buddhism
        - DefenseStrength: 67
        - IsCoastal: true
        
        ### Tilburg
        - ID: 11695
        - X: 35
        - Y: 11
        - Population: 16
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - IsCoastal: true
        
        ### Adama
        - ID: 12042
        - X: 3
        - Y: 6
        - Population: 13
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - IsOccupied: true
        - IsCoastal: true
        
        ### Eindhoven
        - ID: 12467
        - X: 3
        - Y: 49
        - Population: 14
        - MajorityReligion: Buddhism
        - DefenseStrength: 73
        - IsCoastal: true
        
        ### Dordrecht
        - ID: 14459
        - X: 77
        - Y: 36
        - Population: 7
        - MajorityReligion: Buddhism
        - DefenseStrength: 46
        - IsCoastal: true
        
        ## Player: China
        
        ### Beijing
        - ID: 1060
        - X: 44
        - Y: 22
        - Population: 34
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 58
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Ironworks
          - Imperial College
          - Chichen Itza
          - Notre Dame
          - Leaning Tower of Pisa
          - Grand Temple
          - Printing Press
          - Foreign Bureau
          - International Finance Center
          - Soho Foundry
          - Grand Canal
          - Crystal Palace
          - Royal Astrologer
          - TwoKay Foods Headquarters
        
        ### Shanghai
        - ID: 1267
        - X: 39
        - Y: 23
        - Population: 29
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 52
        - IsCoastal: true
        - Wonders:
          - Scrivener's Office
        
        ### Guangzhou
        - ID: 1573
        - X: 41
        - Y: 18
        - Population: 25
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 57
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
        
        ### Nanjing
        - ID: 1925
        - X: 43
        - Y: 13
        - Population: 22
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 56
        - IsCoastal: true
        
        ### Xian
        - ID: 2294
        - X: 47
        - Y: 19
        - Population: 23
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 56
        - IsCoastal: true
        - Wonders:
          - Chartered Company
        
        ### Chengdu
        - ID: 3200
        - X: 53
        - Y: 17
        - Population: 25
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 54
        - IsCoastal: true
        - Wonders:
          - Royal Collection
        
        ### Hangzhou
        - ID: 4445
        - X: 42
        - Y: 9
        - Population: 21
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 57
        - IsCoastal: true
        
        ### Tianjin
        - ID: 4926
        - X: 38
        - Y: 27
        - Population: 21
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 56
        - IsCoastal: true
        
        ### Macau
        - ID: 6056
        - X: 51
        - Y: 20
        - Population: 21
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 57
        - IsCoastal: true
        
        ### Shandong
        - ID: 6084
        - X: 42
        - Y: 5
        - Population: 22
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 57
        - IsCoastal: true
        
        ### Kaifeng
        - ID: 8104
        - X: 59
        - Y: 12
        - Population: 18
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 54
        - IsCoastal: true
        
        ### Ningbo
        - ID: 9553
        - X: 63
        - Y: 8
        - Population: 19
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 57
        - IsCoastal: true
        
        ### Bahir Dar
        - ID: 11657
        - X: 67
        - Y: 5
        - Population: 15
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 29
        - IsOccupied: true
        - IsCoastal: true
        
        ### Baoding
        - ID: 13970
        - X: 47
        - Y: 13
        - Population: 10
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 52
        - IsCoastal: true
        
        ### Harappa
        - ID: 14612
        - X: 57
        - Y: 17
        - Population: 12
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 32
        - Health: 50%
        - IsOccupied: true
        - IsCoastal: true
        - ResistanceTurns: 4
        
        ## Player: Assyria
        
        ### Assur
        - ID: 1061
        - X: 53
        - Y: 35
        - Population: 25
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 64
        - IsCoastal: true
        - FoodStored: 1132
        - FoodPerTurn: 3
        - ProductionStored: 360
        - ProductionPerTurn: 184
        - CurrentProduction: Destroyer
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 232
        - SciencePerTurn: 222
        - CulturePerTurn: 166
        - FaithPerTurn: 102
        - TourismPerTurn: 0
        - HappinessDelta: 2
        - BuildingCount: 41
        - ImportantBuildings:
          - Water Mill
          - Windmill
          - Customs House
          - Harbor
          - Zoo
          - Temple
          - Armory
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Gallery
          - Bastion Fort
          - Coaling Station
        - Wonders:
          - Heroic Epic
          - National Monument
          - Circus Maximus
          - Himeji Castle
          - Royal Library
          - Holy Council
        - GreatWorkCount: 6
        
        ### Nineveh
        - ID: 1268
        - X: 50
        - Y: 32
        - Population: 22
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 76
        - FoodStored: 598
        - FoodPerTurn: 1
        - ProductionStored: 539
        - ProductionPerTurn: 145
        - CurrentProduction: Machine Gun
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 130
        - SciencePerTurn: 210
        - CulturePerTurn: 231
        - FaithPerTurn: 47
        - TourismPerTurn: 145.75
        - HappinessDelta: 3
        - BuildingCount: 47
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Armory
          - Arsenal
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Coaling Station
        - Wonders:
          - Ironworks
          - Imperial College
          - Royal Collection
          - Grand Temple
          - Scrivener's Office
          - Empire State Building
        - GreatWorkCount: 12
        
        ### Nimrud
        - ID: 1521
        - X: 58
        - Y: 36
        - Population: 20
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 36
        - IsCoastal: true
        - FoodStored: 569
        - FoodPerTurn: 0
        - ProductionStored: 490
        - ProductionPerTurn: 115
        - CurrentProduction: Stock Exchange
        - ProductionTurnsLeft: 7
        - GoldPerTurn: 89
        - SciencePerTurn: 89
        - CulturePerTurn: 76
        - FaithPerTurn: 32
        - TourismPerTurn: 22
        - HappinessDelta: 2
        - BuildingCount: 37
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Customs House
          - Harbor
          - Zoo
          - Temple
          - Armory
          - Hospital
          - Workshop
          - Bank
          - University
          - Amphitheater
          - Constabulary
          - Writers' Guild
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
        - Wonders:
          - Printing Press
        - GreatWorkCount: 2
        
        ### Kar-Tukulti-Ninurta
        - ID: 1882
        - X: 45
        - Y: 32
        - Population: 25
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 63
        - IsCoastal: true
        - FoodStored: 766
        - FoodPerTurn: 0
        - ProductionStored: 713
        - ProductionPerTurn: 29
        - CurrentProduction: Destroyer
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 154
        - SciencePerTurn: 118
        - CulturePerTurn: 55
        - FaithPerTurn: 26
        - TourismPerTurn: 7.25
        - HappinessDelta: -19
        - BuildingCount: 40
        - ImportantBuildings:
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Harbor
          - Zoo
          - Temple
          - Armory
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Amphitheater
          - Constabulary
          - Artists' Guild
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
        - Wonders:
          - Chartered Company
        - GreatWorkCount: 0
        
        ### Dur-Sharrukin
        - ID: 2209
        - X: 55
        - Y: 30
        - Population: 18
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 78
        - IsCoastal: true
        - FoodStored: 737
        - FoodPerTurn: 2
        - ProductionStored: 302
        - ProductionPerTurn: 87
        - CurrentProduction: Dreadnought
        - ProductionTurnsLeft: 7
        - GoldPerTurn: 99
        - SciencePerTurn: 71
        - CulturePerTurn: 75
        - FaithPerTurn: 24
        - TourismPerTurn: 8.5
        - HappinessDelta: 0
        - BuildingCount: 38
        - ImportantBuildings:
          - Water Mill
          - Customs House
          - Harbor
          - Zoo
          - Temple
          - Armory
          - Arsenal
          - Hospital
          - Workshop
          - Stock Exchange
          - University
          - Amphitheater
          - Constabulary
          - Writers' Guild
          - Caravansary
          - Bath
          - Chancery
        - GreatWorkCount: 0
        
        ### Halab
        - ID: 3023
        - X: 49
        - Y: 36
        - Population: 22
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 34
        - IsCoastal: true
        - FoodStored: 609
        - FoodPerTurn: 0
        - ProductionStored: 364
        - ProductionPerTurn: 34
        - CurrentProduction: Machine Gun
        - ProductionTurnsLeft: 9
        - GoldPerTurn: 101
        - SciencePerTurn: 111
        - CulturePerTurn: 54
        - FaithPerTurn: 26
        - TourismPerTurn: 12
        - HappinessDelta: -9
        - BuildingCount: 42
        - ImportantBuildings:
          - Windmill
          - Customs House
          - Observatory
          - Harbor
          - Zoo
          - Temple
          - Museum
          - Armory
          - Medical Lab
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Writers' Guild
          - Caravansary
          - Chancery
          - Bastion Fort
          - Coaling Station
        - GreatWorkCount: 0
        
        ### Carchemish
        - ID: 3719
        - X: 44
        - Y: 27
        - Population: 19
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 63
        - FoodStored: 555
        - FoodPerTurn: 5
        - ProductionStored: 620
        - ProductionPerTurn: 138
        - CurrentProduction: Wire Service
        - ProductionTurnsLeft: 5
        - GoldPerTurn: 114
        - SciencePerTurn: 109
        - CulturePerTurn: 80
        - FaithPerTurn: 34
        - TourismPerTurn: 29
        - HappinessDelta: 5
        - BuildingCount: 45
        - ImportantBuildings:
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Armory
          - Hospital
          - Workshop
          - Stock Exchange
          - Public School
          - Constabulary
          - Artists' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
          - Coaling Station
        - GreatWorkCount: 0
        
        ### Kanesh
        - ID: 7477
        - X: 59
        - Y: 43
        - Population: 17
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 63
        - IsCoastal: true
        - FoodStored: 678
        - FoodPerTurn: 27
        - ProductionStored: 567
        - ProductionPerTurn: 75
        - CurrentProduction: Research Lab
        - ProductionTurnsLeft: 11
        - GoldPerTurn: 71
        - SciencePerTurn: 93
        - CulturePerTurn: 43
        - FaithPerTurn: 36
        - TourismPerTurn: 11.25
        - HappinessDelta: 5
        - BuildingCount: 40
        - ImportantBuildings:
          - Water Mill
          - Customs House
          - Garden
          - Harbor
          - Zoo
          - Temple
          - Armory
          - Hospital
          - Workshop
          - Bank
          - Public School
          - Amphitheater
          - Constabulary
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
        - GreatWorkCount: 0
        
        ### Harran
        - ID: 8428
        - X: 64
        - Y: 46
        - Population: 14
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 65
        - IsCoastal: true
        - FoodStored: 417
        - FoodPerTurn: 1
        - ProductionStored: 67
        - ProductionPerTurn: 67
        - CurrentProduction: Public Works
        - ProductionTurnsLeft: 13
        - GoldPerTurn: 68
        - SciencePerTurn: 57
        - CulturePerTurn: 49
        - FaithPerTurn: 22
        - TourismPerTurn: 7.5
        - HappinessDelta: -4
        - BuildingCount: 37
        - ImportantBuildings:
          - Windmill
          - Customs House
          - Harbor
          - Zoo
          - Temple
          - Armory
          - Hospital
          - Workshop
          - Bank
          - University
          - Constabulary
          - Musicians' Guild
          - Caravansary
          - Chancery
          - Gallery
          - Bastion Fort
        - GreatWorkCount: 0
        
        ### Nuku Hiva
        - ID: 9430
        - X: 39
        - Y: 36
        - Population: 15
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 34
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 533
        - FoodPerTurn: 2
        - ProductionStored: 124
        - ProductionPerTurn: 102
        - CurrentProduction: Dreadnought
        - ProductionTurnsLeft: 8
        - GoldPerTurn: 62
        - SciencePerTurn: 57
        - CulturePerTurn: 75
        - FaithPerTurn: 45
        - TourismPerTurn: 19.75
        - HappinessDelta: 0
        - BuildingCount: 38
        - ImportantBuildings:
          - Courthouse
          - Windmill
          - Customs House
          - Harbor
          - Zoo
          - Temple
          - Military Academy
          - Hospital
          - Workshop
          - Stock Exchange
          - University
          - Amphitheater
          - Caravansary
          - Chancery
          - Bastion Fort
        - GreatWorkCount: 0
        
        ### Arnhem
        - ID: 10892
        - X: 31
        - Y: 46
        - Population: 10
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 55
        - Health: 28%
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 254
        - FoodPerTurn: 6
        - ProductionStored: 426
        - ProductionPerTurn: 18
        - CurrentProduction: Dreadnought
        - ProductionTurnsLeft: 25
        - GoldPerTurn: 37
        - SciencePerTurn: 44
        - CulturePerTurn: 23
        - FaithPerTurn: 16
        - TourismPerTurn: 2.5
        - HappinessDelta: -4
        - BuildingCount: 26
        - ImportantBuildings:
          - Courthouse
          - Circus
          - Forge
          - Harbor
          - Barracks
          - Bank
          - University
          - Aqueduct
          - Amphitheater
          - Shrine
          - Chancery
          - Bastion Fort
        - GreatWorkCount: 0
        
        ### Ur
        - ID: 12599
        - X: 61
        - Y: 32
        - Population: 11
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 54
        - Health: 91%
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 300
        - FoodPerTurn: 2
        - ProductionStored: 684
        - ProductionPerTurn: 52
        - CurrentProduction: Destroyer
        - ProductionTurnsLeft: 4
        - GoldPerTurn: 36
        - SciencePerTurn: 42
        - CulturePerTurn: 25
        - FaithPerTurn: 14
        - TourismPerTurn: 2.75
        - HappinessDelta: -2
        - BuildingCount: 27
        - ImportantBuildings:
          - Courthouse
          - Customs House
          - Garden
          - Harbor
          - Arena
          - Barracks
          - Workshop
          - Bank
          - University
          - Caravansary
          - Grocer
          - Bastion Fort
        - GreatWorkCount: 0
        
        ## Player: Rome
        
        ### Rome
        - ID: 1062
        - X: 21
        - Y: 32
        - Population: 31
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 61
        - Wonders:
          - School of Philosophy
          - National Monument
          - Ironworks
          - Imperial College
          - Royal Collection
          - Machu Picchu
          - Fornix
          - Civilized Jewelers Headquarters
        
        ### Antium
        - ID: 1296
        - X: 17
        - Y: 29
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 53
        - Wonders:
          - Circus Maximus
          - Chartered Company
        
        ### Cumae
        - ID: 1472
        - X: 25
        - Y: 32
        - Population: 21
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 52
        - Wonders:
          - Scrivener's Office
          - Printing Press
        
        ### Neapolis
        - ID: 3487
        - X: 18
        - Y: 23
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 51
        - Wonders:
          - Grand Temple
        
        ### Ravenna
        - ID: 5823
        - X: 23
        - Y: 28
        - Population: 18
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 50
        
        ### Sigtuna
        - ID: 7594
        - X: 18
        - Y: 35
        - Population: 18
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 51
        - IsOccupied: true
        - Wonders:
          - Petra
        
        ### Nottingham
        - ID: 9897
        - X: 14
        - Y: 24
        - Population: 19
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 50
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Alhambra
        
        ## Player: City-States
        
        ### Abernethy
        - ID: 1063
        - X: 31
        - Y: 23
        - Population: 20
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Singapore
        - ID: 1064
        - X: 22
        - Y: 24
        - Population: 16
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 71
        
        ### Utica
        - ID: 1065
        - X: 67
        - Y: 35
        - Population: 23
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Venezia
        - ID: 6707
        - X: 7
        - Y: 49
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### M'banza-Kongo
        - ID: 1067
        - X: 25
        - Y: 48
        - Population: 16
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Warsaw
        - ID: 1068
        - X: 47
        - Y: 4
        - Population: 22
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 72
        - IsCoastal: true
        
        ### Kathmandu
        - ID: 1070
        - X: 12
        - Y: 19
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 75
        - IsCoastal: true
        
        ### Lutetia
        - ID: 1071
        - X: 57
        - Y: 4
        - Population: 16
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 72
        - Health: 100%
        - IsCoastal: true
        
        ### Holmul
        - ID: 1072
        - X: 66
        - Y: 12
        - Population: 20
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Sogut
        - ID: 1074
        - X: 67
        - Y: 29
        - Population: 22
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Byblos
        - ID: 1075
        - X: 19
        - Y: 48
        - Population: 17
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 77
        
        ### Brandenburg
        - ID: 1076
        - X: 13
        - Y: 35
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 75
        
        ### Samarkand
        - ID: 1077
        - X: 51
        - Y: 25
        - Population: 20
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 86
        - IsCoastal: true
        
        ### Okilis
        - ID: 1078
        - X: 40
        - Y: 31
        - Population: 19
        - MajorityReligion: Zoroastrianism
        - DefenseStrength: 71
        - IsCoastal: true
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - CityBombard:
          - Field Gun:
            - Strength: 17
            - RangedStrength: 40
        - FastAttack:
          - Landship:
            - Strength: 60
        - Defense:
          - Infantry:
            - Strength: 62
          - Rifleman:
            - Strength: 50
        - Ranged:
          - Cavalry:
            - Strength: 40
            - RangedStrength: 31
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
        - AssaultSea:
          - Cruiser:
            - Strength: 40
            - RangedStrength: 55
          - Dreadnought:
            - Strength: 50
            - RangedStrength: 65
        - AttackAir:
          - Bomber:
            - RangedStrength: 50
        - Paradrop:
          - Paratrooper:
            - Strength: 42
        
        ## Neutral Land Zone 1059
        - ZoneValue: 3
        - Dominance: Enemy
        - EnemyStrength: 291
        - NeutralStrength: 720
        - City: Honolulu
        - AreaID: 23
        - Plots: 15
        - CenterX: 25
        - CenterY: 11
        - Units:
          - Polynesia:
            - Rifleman: 1
        
        ## Friendly Land Zone 1061
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 1417
        - City: Assur
        - AreaID: 4
        - Plots: 13
        - CenterX: 53
        - CenterY: 35
        - Units:
          - Assyria:
            - Rifleman: 1
        - Neighbors:
          - 1268
          - -1061
          - 2209
          - 1521
        
        ## Neutral Land Zone 1077
        - ZoneValue: 9
        - Dominance: Friendly
        - NeutralStrength: 86
        - FriendlyStrength: 1831
        - City: Samarkand
        - AreaID: 4
        - Plots: 26
        - CenterX: 50
        - CenterY: 25
        - Units:
          - City-State Samarkand:
            - Cavalry: 1
            - Rifleman: 1
            - Gatling Gun: 1
        - Neighbors:
          - 3719
          - 1268
        
        ## Neutral Land Zone 1078
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 71
        - FriendlyStrength: 3308
        - City: Okilis
        - AreaID: 4
        - Plots: 19
        - CenterX: 40
        - CenterY: 30
        - Units:
          - City-State Okilis:
            - Cavalry: 1
            - Rifleman: 2
            - Landship: 1
            - Gatling Gun: 1
          - Assyria:
            - Cavalry: 1
          - China:
            - Gatling Gun: 3
            - Field Gun: 1
        - Neighbors:
          - -1078
          - 3719
          - 1882
        
        ## Friendly Land Zone 1268
        - ZoneValue: 30
        - Dominance: Friendly
        - FriendlyStrength: 1779
        - City: Nineveh
        - AreaID: 4
        - Plots: 22
        - CenterX: 50
        - CenterY: 31
        - Units:
          - Assyria:
            - Machine Gun: 1
        - Neighbors:
          - 3719
          - 1882
          - 1077
          - 2209
          - 1061
        
        ## Enemy Land Zone 1292
        - ZoneValue: 36
        - Dominance: Enemy
        - EnemyStrength: 1657
        - City: Harar
        - AreaID: 57
        - Plots: 22
        - CenterX: 8
        - CenterY: 42
        - Units:
          - Ethiopia:
            - Cavalry: 1
        - Neighbors:
          - 2021
        
        ## Friendly Land Zone 1521
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 229
        - NeutralStrength: 358
        - FriendlyStrength: 1713
        - City: Nimrud
        - AreaID: 4
        - Plots: 21
        - CenterX: 58
        - CenterY: 36
        - Units:
          - Assyria:
            - Ironclad: 1
            - Rifleman: 1
            - Field Gun: 2
        - Neighbors:
          - -1061
          - 1061
          - 2209
          - -12599
          - 12599
          - 6009
          - 7477
        
        ## Friendly Land Zone 1882
        - ZoneValue: 18
        - Dominance: Friendly
        - FriendlyStrength: 2437
        - City: Kar-Tukulti-Ninurta
        - AreaID: 4
        - Plots: 16
        - CenterX: 45
        - CenterY: 31
        - Units:
          - Barbarians:
            - Rifleman: 1
          - City-State Okilis:
            - Rifleman: 1
          - Assyria:
            - Rifleman: 1
            - Machine Gun: 1
            - Gatling Gun: 1
        - Neighbors:
          - 1078
          - 3719
          - 1268
        
        ## Enemy Land Zone 2021
        - ZoneValue: 30
        - Dominance: Enemy
        - EnemyStrength: 1553
        - City: Gondar
        - AreaID: 101
        - Plots: 12
        - CenterX: 6
        - CenterY: 39
        - Units:
          - Ethiopia:
            - Field Gun: 1
        - Neighbors:
          - 1292
        
        ## Friendly Land Zone 2209
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 1893
        - City: Dur-Sharrukin
        - AreaID: 84
        - Plots: 22
        - CenterX: 54
        - CenterY: 31
        - Units:
          - China:
            - Infantry: 1
          - Assyria:
            - Machine Gun: 1
            - Gatling Gun: 2
        - Neighbors:
          - 1268
          - 1061
          - -2209
          - -1061
          - 1521
          - 12599
        
        ## Friendly Land Zone 3719
        - ZoneValue: 24
        - Dominance: Friendly
        - FriendlyStrength: 3148
        - City: Carchemish
        - AreaID: 4
        - Plots: 31
        - CenterX: 45
        - CenterY: 27
        - Units:
          - China:
            - Cavalry: 1
            - Field Gun: 1
          - Assyria:
            - Machine Gun: 1
            - Field Gun: 1
        - Neighbors:
          - 1078
          - 1882
          - 1077
          - 1268
        
        ## Enemy Land Zone 5761
        - ZoneValue: 30
        - Dominance: Enemy
        - EnemyStrength: 1631
        - City: Axum
        - AreaID: 20
        - Plots: 18
        - CenterX: 5
        - CenterY: 13
        - Units:
          - Ethiopia:
            - Paratrooper: 1
            - Bomber: 2
        
        ## Neutral Land Zone 6009
        - ZoneValue: 24
        - Dominance: Even
        - Posture: Attrition
        - EnemyStrength: 730
        - NeutralStrength: 1099
        - FriendlyStrength: 769
        - City: Raiatea
        - AreaID: 93
        - Plots: 26
        - CenterX: 63
        - CenterY: 38
        - Units:
          - Polynesia:
            - Landship: 1
            - Gatling Gun: 1
        - Neighbors:
          - 1521
          - -12599
          - 7477
          - 12599
          - 8428
        
        ## Friendly Land Zone 7477
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 263
        - FriendlyStrength: 797
        - City: Kanesh
        - AreaID: 99
        - Plots: 21
        - CenterX: 60
        - CenterY: 42
        - Units:
          - Assyria:
            - Machine Gun: 1
        - Neighbors:
          - 1521
          - 8428
          - 6009
        
        ## Enemy Land Zone 8090
        - ZoneValue: 3
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2720
        - NeutralStrength: 100
        - FriendlyStrength: 61
        - City: Haarlem
        - AreaID: 75
        - Plots: 11
        - CenterX: 64
        - CenterY: 27
        - Units:
          - The Netherlands:
            - Landship: 2
        - Neighbors:
          - -12599
        
        ## Friendly Land Zone 8428
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 63
        - FriendlyStrength: 1200
        - City: Harran
        - AreaID: 99
        - Plots: 41
        - CenterX: 65
        - CenterY: 46
        - Units:
          - Assyria:
            - Machine Gun: 4
            - Gatling Gun: 1
        - Neighbors:
          - 7477
          - 6009
        
        ## Enemy Land Zone 10059
        - ZoneValue: 36
        - Dominance: Enemy
        - EnemyStrength: 1907
        - NeutralStrength: 967
        - City: Stockholm
        - AreaID: 14
        - Plots: 39
        - CenterX: 21
        - CenterY: 40
        - Units:
          - Ethiopia:
            - Rifleman: 1
            - Bomber: 2
        
        ## Friendly Land Zone 10892
        - ZoneValue: 672
        - Dominance: Enemy
        - Posture: Hedgehog
        - EnemyStrength: 540
        - NeutralStrength: 321
        - FriendlyStrength: 176
        - City: Arnhem
        - AreaID: 113
        - Plots: 11
        - CenterX: 31
        - CenterY: 48
        - Units:
          - Assyria:
            - Paratrooper: 1
        - Neighbors:
          - -10892
        
        ## Friendly Land Zone 12599
        - ZoneValue: 72
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 1694
        - NeutralStrength: 511
        - FriendlyStrength: 1070
        - City: Ur
        - AreaID: 87
        - Plots: 14
        - CenterX: 61
        - CenterY: 32
        - Units:
          - Assyria:
            - Rifleman: 2
            - Gatling Gun: 1
            - Field Gun: 2
        - Neighbors:
          - 2209
          - -12599
          - 1521
          - 6009
        
        ## Neutral Sea Zone -1078
        - ZoneValue: 1
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 105
        - NeutralStrength: 71
        - FriendlyStrength: 2380
        - City: Okilis
        - AreaID: 0
        - Plots: 14
        - CenterX: 39
        - CenterY: 32
        - Units:
          - Assyria:
            - Cavalry: 1
          - City-State Okilis:
            - Destroyer: 2
        - Neighbors:
          - -9430
          - 1078
        
        ## Friendly Sea Zone -9430
        - ZoneValue: 8
        - Dominance: Friendly
        - FriendlyStrength: 1398
        - City: Nuku Hiva
        - AreaID: 0
        - Plots: 53
        - CenterX: 38
        - CenterY: 37
        - Units:
          - Assyria:
            - Cavalry: 1
            - Field Gun: 1
            - Dreadnought: 1
        - Neighbors:
          - -1078
        
        ## Friendly Sea Zone -12599
        - ZoneValue: 48
        - Dominance: Enemy
        - Posture: Hedgehog
        - EnemyStrength: 3141
        - NeutralStrength: 108
        - FriendlyStrength: 475
        - City: Ur
        - AreaID: 0
        - Plots: 32
        - CenterX: 61
        - CenterY: 31
        - Units:
          - The Netherlands:
            - Destroyer: 1
            - Gatling Gun: 1
          - Ethiopia:
            - Destroyer: 2
            - Ironclad: 1
            - Dreadnought: 1
          - City-State Sogut:
            - Destroyer: 1
        - Neighbors:
          - -2209
          - 1521
          - 12599
          - 6009
          - 8090
        
        ## Friendly Sea Zone -1061
        - ZoneValue: 4
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 503
        - FriendlyStrength: 766
        - City: Assur
        - AreaID: 91
        - Plots: 16
        - CenterX: 53
        - CenterY: 38
        - Units:
          - Assyria:
            - Cruiser: 1
        - Neighbors:
          - 1061
          - 2209
          - 1521
        
        ## Neutral Sea Zone -7686
        - ZoneValue: 4
        - Dominance: Enemy
        - EnemyStrength: 1916
        - NeutralStrength: 629
        - City: Helsinki
        - AreaID: 0
        - Plots: 17
        - CenterX: 28
        - CenterY: 42
        - Units:
          - Polynesia:
            - Dreadnought: 2
        - Neighbors:
          - -1067
          - -10892
        
        ## Friendly Sea Zone -10892
        - ZoneValue: 224
        - Dominance: Enemy
        - Posture: Hedgehog
        - EnemyStrength: 1323
        - NeutralStrength: 485
        - FriendlyStrength: 8
        - City: Arnhem
        - AreaID: 0
        - Plots: 59
        - CenterX: 32
        - CenterY: 46
        - Units:
          - Polynesia:
            - Destroyer: 2
          - The Netherlands:
            - Destroyer: 1
            - Ironclad: 1
            - Dreadnought: 1
        - Neighbors:
          - -1067
          - -7686
          - 10892
        
        ## Friendly Sea Zone -2209
        - ZoneValue: 24
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 761
        - FriendlyStrength: 946
        - City: Dur-Sharrukin
        - AreaID: 0
        - Plots: 17
        - CenterX: 57
        - CenterY: 28
        - Units:
          - The Netherlands:
            - Destroyer: 2
        - Neighbors:
          - 2209
          - -12599
        
        ## Enemy Sea Zone -1067
        - ZoneValue: 1
        - Dominance: Enemy
        - EnemyStrength: 1209
        - NeutralStrength: 431
        - City: M'banza-Kongo
        - AreaID: 0
        - Plots: 31
        - CenterX: 26
        - CenterY: 49
        - Units:
          - City-State M'banza-Kongo:
            - Dreadnought: 1
        - Neighbors:
          - -7686
          - -10892
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 360
        
        ### 0
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 13512
        - Player: 7: Rome
        - Plots:
          - Grass Hills 27,32:
            - Owner: The Netherlands
            - Improvement: Mine
          - Plains Land 28,32:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Dyes
            - Improvement: Manufactory
          - Plains Land 28,31:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 29,30:
            - Owner: The Netherlands
            - CityID: 1079
            - Population: 41
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
        
        ### 1
        - Type: MinorFriendsChanged
        - OldFriendship: 47
        - NewFriendship: 17
        - MajorPlayer: 6: Assyria
        - MinorPlayer: 22
        
        ### 2
        - Type: ElectionResultFailure
        - DiminishAmount: 3000
        - Capital:
          - Owner: City-State Abernethy
          - CityID: 1063
          - Population: 20
          - City: Abernethy
          - Terrain: Grass
          - Religion: Zoroastrianism
          - Route: Railroad
          - Plot: Land
          - X: 31
          - Y: 23
        - Player: 6: Assyria
        
        ### 3
        - Type: ElectionResultFailure
        - DiminishAmount: 0
        - Capital:
          - Owner: City-State Venezia
          - CityID: 6707
          - Population: 14
          - IsRiver: true
          - City: Venezia
          - Terrain: Snow
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 7
          - Y: 49
        - Player: 6: Assyria
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 13581
        - Player: 26
        - Ocean 27,48:
          - Owner: City-State M'banza-Kongo
        
        ### 5
        - Type: ElectionResultFailure
        - DiminishAmount: 0
        - Capital:
          - Owner: City-State Kathmandu
          - CityID: 1070
          - Population: 21
          - IsRiver: true
          - City: Kathmandu
          - Terrain: Desert
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Hills
          - X: 12
          - Y: 19
        - Player: 6: Assyria
        
        ### 6
        - Type: ElectionResultFailure
        - DiminishAmount: 0
        - Capital:
          - Owner: City-State Lutetia
          - CityID: 1071
          - Population: 16
          - City: Lutetia
          - Terrain: Tundra
          - Resource: Glass
          - Religion: Zoroastrianism
          - Route: Railroad
          - Plot: Land
          - X: 57
          - Y: 4
        - Player: 6: Assyria
        
        ### 7
        - Type: ElectionResultFailure
        - DiminishAmount: 0
        - Capital:
          - Owner: City-State Harappa
          - CityID: 1073
          - Population: 17
          - City: Harappa
          - Terrain: Grass
          - Resource: Jewelry
          - Religion: Zoroastrianism
          - Route: Railroad
          - Plot: Land
          - X: 57
          - Y: 17
        - Player: 6: Assyria
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 90%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13934
        - Player: 33
        
        ### 9
        - Type: ElectionResultFailure
        - DiminishAmount: 0
        - Capital:
          - Owner: City-State Byblos
          - CityID: 1075
          - Population: 17
          - IsRiver: true
          - City: Byblos
          - Terrain: Tundra
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Hills
          - X: 19
          - Y: 48
        - Player: 6: Assyria
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Light Tank
          - ID: 14581
        - Player: 6: Assyria
        - Plains Land 46,32:
          - Owner: Assyria
          - Resource: Wheat
          - Improvement: Town
          - Route: Railroad
        
        ### 11
        - Type: UnitCreated
        - UnitType: Light Tank
        - Player: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14581
        - Plains Land 46,32:
          - Owner: Assyria
          - Resource: Wheat
          - Improvement: Town
          - Route: Railroad
        
        ### 12
        - Type: MinorGiftUnit
        - MajorPlayer: 6: Assyria
        - MinorPlayer: 37
        - Unit: Light Tank
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Rifleman
          - ID: 12798
        - Player: 37
        - Plots:
          - Grass Hills 40,31:
            - Owner: City-State Okilis
            - CityID: 1078
            - Population: 19
            - City: Okilis
            - Religion: Zoroastrianism
            - Route: Railroad
          - Plains Land 41,31:
            - Owner: City-State Okilis
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 42,31:
            - Owner: City-State Okilis
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: FastAttack
          - Unit: Landship
          - ID: 13780
        - Player: 37
        - Plots:
          - Plains Land 39,31:
            - Owner: City-State Okilis
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 40,31:
            - Owner: City-State Okilis
            - CityID: 1078
            - Population: 19
            - City: Okilis
            - Religion: Zoroastrianism
            - Route: Railroad
          - Grass Land 41,29:
            - Owner: City-State Okilis
            - IsRiver: true
            - Resource: Sugar
            - Improvement: Embassy
        
        ### 15
        - Type: CombatResult
        - Grass Land 43,30:
          - Owner: City-State Okilis
          - IsRiver: true
          - Resource: Horses
          - Improvement: Pasture
        - Attacker:
          - RemainingHP: 1
          - Damage: 1
        - Defender:
          - RemainingHP: 61
          - Damage: 176
          - Unit:
            - Level: 1
            - Health: 4%
            - AI: FastAttack
            - Unit: Rifleman
            - ID: 14304
          - Player: 63: Barbarians
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 99%
          - AI: Defense
          - Unit: Rifleman
          - ID: 12798
        - Player: 37
        - Grass Land 43,30:
          - Owner: City-State Okilis
          - IsRiver: true
          - Resource: Horses
          - Improvement: Pasture
        
        ### 17
        - Type: UnitBuildCompleted
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1131
        - Owner: 37
        - Build: Construct a Railroad
        - Grass Land 38,31:
          - Owner: City-State Okilis
          - Improvement: Farm
          - Route: Road
        
        ### 18
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 12797
        - Player: 37
        - Plains Hills 39,29:
          - Owner: China
          - Improvement: Mine
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 80%
          - AI: Ranged
          - Unit: Cavalry
          - ID: 12403
        - Player: 37
        - Plots:
          - Coast 38,30:
            - Owner: China
          - Grass Land 39,30:
            - Owner: City-State Okilis
            - Improvement: Farm
        
        ### 20
        - Type: CombatResult
        - Grass Land 43,30:
          - Owner: City-State Okilis
          - IsRiver: true
          - Resource: Horses
          - Improvement: Pasture
        - Attacker:
          - RemainingHP: 43
          - Damage: 86
        - Defender:
          - RemainingHP: 18
          - Damage: 19
          - Unit:
            - Level: 2
            - Health: 99%
            - AI: Defense
            - Unit: Rifleman
            - ID: 12798
          - Player: 37
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 25%
          - AI: FastAttack
          - Unit: Rifleman
          - ID: 14115
        - Player: 63: Barbarians
        - Plots:
          - Coast 52,41:
            - Resource: Fish
          - Coast 53,40:
            - Owner: Assyria
          - Coast 53,39:
            - Owner: Assyria
            - Resource: Fish
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Health: 45%
          - AI: FastAttack
          - Unit: Rifleman
          - ID: 14419
        - Player: 63: Barbarians
        - Plots:
          - Plains Land 43,31:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
          - Desert Land 43,32:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Feature: Flood Plains
        
        ## Turn 361
        
        ### 0
        - Type: CityConvertsReligion
        - City:
          - Owner: Assyria
          - CityID: 10892
          - Population: 10
          - City: Arnhem
          - Terrain: Tundra
          - Religion: Zoroastrianism
          - Route: Railroad
          - Plot: Land
          - X: 31
          - Y: 46
        - Owner: 6: Assyria
        - Religion: Zoroastrianism
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Submarine
          - ID: 14585
        - Player: 0: Ethiopia
        - Desert Land 6,38:
          - Owner: Ethiopia
          - CityID: 2021
          - Population: 25
          - City: Gondar
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 2
        - Type: UnitCreated
        - UnitType: Submarine
        - Player: 0: Ethiopia
        - Unit:
          - Level: 1
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 14585
        - Desert Land 6,38:
          - Owner: Ethiopia
          - CityID: 2021
          - Population: 25
          - City: Gondar
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 3
        - Type: CityTrained
        - Player: 0: Ethiopia
        - City:
          - Name: Gondar
          - Population: 25
          - ID: 2021
        - Unit:
          - Level: 1
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 14585
        
        ### 4
        - Type: EspionageState
        - SpyIndex: 0
        - SpyState: 3
        - City:
          - Owner: Assyria
          - CityID: 3023
          - Population: 22
          - City: Halab
          - Terrain: Desert
          - Religion: Zoroastrianism
          - Route: Railroad
          - Plot: Land
          - X: 49
          - Y: 36
        - SpyOwner: 0: Ethiopia
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14390
        - Player: 0: Ethiopia
        - Plains Land 7,42:
          - Owner: Ethiopia
          - CityID: 1292
          - Population: 23
          - IsRiver: true
          - City: Harar
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 6
        - Type: EspionageState
        - SpyIndex: 3
        - SpyState: 1
        - City:
          - Owner: Assyria
          - CityID: 8428
          - Population: 14
          - City: Harran
          - Terrain: Tundra
          - Religion: Zoroastrianism
          - Route: Railroad
          - Plot: Hills
          - X: 64
          - Y: 46
        - SpyOwner: 0: Ethiopia
        
        ### 7
        - Type: UnitPromoted
        - Unit:
          - Level: 4
          - Health: 57%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13390
        - Player: 0: Ethiopia
        - Promotion: Hull III
        
        ### 8
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 14585
        - Player: 0: Ethiopia
        - Promotions:
          - Torpedo I
          - Torpedo II
          - Torpedo III
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 57%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13390
        - Player: 0: Ethiopia
        - Plots:
          - Coast 62,33:
            - Owner: Assyria
          - Coast 62,34:
            - Owner: Polynesia
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 85%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13513
        - Player: 0: Ethiopia
        - Plots:
          - Coast 62,32:
            - Owner: Assyria
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 57%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13390
        - Player: 0: Ethiopia
        - Coast 61,35:
          - Owner: Polynesia
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 77%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12742
        - Player: 0: Ethiopia
        - Plots:
          - Coast 61,29:
            - Owner: Assyria
            - Resource: Fish
          - Coast 61,30:
            - Owner: Assyria
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 76%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13522
        - Player: 0: Ethiopia
        - Plots:
          - Coast 61,35:
            - Owner: Polynesia
          - Coast 60,35:
            - Owner: Assyria
          - Coast 59,35:
            - Owner: Assyria
          - Coast 59,36:
            - Owner: Assyria
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 77%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12742
        - Player: 0: Ethiopia
        - Coast 61,29:
          - Owner: Assyria
          - Resource: Fish
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: WorkerSea
          - Unit: Work Boat
          - ID: 14512
        - Player: 0: Ethiopia
        - Coast 5,37:
          - Owner: Ethiopia
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 14585
        - Player: 0: Ethiopia
        - Coast 5,38:
          - Owner: Ethiopia
        
        ### 17
        - Type: TileOwnershipChanged
        - NewOwner: 2: Polynesia
        - Desert Hills 63,34:
          - Owner: Polynesia
        
        ### 18
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 2: Polynesia
        - City:
          - Name: Raiatea
          - Population: 18
          - ID: 6009
        - Desert Hills 63,34:
          - Owner: Polynesia
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 13243
        - Player: 2: Polynesia
        - Plains Land 25,11:
          - Owner: Polynesia
          - CityID: 1059
          - Population: 33
          - IsRiver: true
          - City: Honolulu
          - Route: Railroad
        
        ### 20
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 2: Polynesia
        - DestinationCity:
          - Name: Groningen
          - Population: 23
          - ID: 2097
        - DestinationPlayer: 3: The Netherlands
        - OriginCity:
          - Name: Honolulu
          - Population: 33
          - ID: 1059
        - Connection: Food
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 14587
        - Player: 2: Polynesia
        - Plains Land 25,11:
          - Owner: Polynesia
          - CityID: 1059
          - Population: 33
          - IsRiver: true
          - City: Honolulu
          - Route: Railroad
        
        ### 22
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 2: Polynesia
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14587
        - Plains Land 25,11:
          - Owner: Polynesia
          - CityID: 1059
          - Population: 33
          - IsRiver: true
          - City: Honolulu
          - Route: Railroad
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 14167
        - Player: 2: Polynesia
        - Plots:
          - Coast 37,31:
            - Owner: City-State Okilis
        
        ### 24
        - Type: EspionageState
        - SpyIndex: 2
        - SpyState: 1
        - City:
          - Owner: Assyria
          - CityID: 1882
          - Population: 25
          - IsRiver: true
          - City: Kar-Tukulti-Ninurta
          - Terrain: Desert
          - Religion: Zoroastrianism
          - Route: Railroad
          - Plot: Land
          - X: 45
          - Y: 32
        - SpyOwner: 2: Polynesia
        
        ### 25
        - Type: UnitBuildCompleted
        - Owner: 2: Polynesia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2905
        - Build: Construct a Mine
        - Plains Hills 63,40:
          - Owner: Polynesia
          - Route: Railroad
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 14214
        - Player: 2: Polynesia
        - Plots:
          - Plains Hills 62,39:
            - Owner: Polynesia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 63,38:
            - Owner: Polynesia
            - Improvement: Mine
            - Route: Railroad
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 14588
        - Player: 2: Polynesia
        - Plains Land 25,11:
          - Owner: Polynesia
          - CityID: 1059
          - Population: 33
          - IsRiver: true
          - City: Honolulu
          - Route: Railroad
        
        ### 28
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 2: Polynesia
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14588
        - Plains Land 25,11:
          - Owner: Polynesia
          - CityID: 1059
          - Population: 33
          - IsRiver: true
          - City: Honolulu
          - Route: Railroad
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Machine Gun
          - ID: 14590
        - Player: 3: The Netherlands
        - Grass Hills 28,29:
          - Owner: The Netherlands
          - Improvement: Town
          - Route: Railroad
        
        ### 30
        - Type: UnitCreated
        - UnitType: Machine Gun
        - Player: 3: The Netherlands
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14590
        - Grass Hills 28,29:
          - Owner: The Netherlands
          - Improvement: Town
          - Route: Railroad
        
        ### 31
        - Type: CityTrained
        - WithGold: true
        - Player: 3: The Netherlands
        - City:
          - Name: Amsterdam
          - Population: 41
          - ID: 1079
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14590
        
        ### 32
        - Type: SetPopulation
        - OldPopulation: 41
        - NewPopulation: 42
        - City:
          - Owner: The Netherlands
          - CityID: 1079
          - Population: 42
          - IsRiver: true
          - City: Amsterdam
          - Terrain: Grass
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 29
          - Y: 30
        
        ### 33
        - Type: CityConvertsReligion
        - City:
          - Owner: The Netherlands
          - CityID: 1079
          - Population: 42
          - IsRiver: true
          - City: Amsterdam
          - Terrain: Grass
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 29
          - Y: 30
        - Owner: 3: The Netherlands
        - Religion: Buddhism
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 13290
        - Player: 3: The Netherlands
        - Plots:
          - Plains Land 28,31:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 29,30:
            - Owner: The Netherlands
            - CityID: 1079
            - Population: 42
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
        
        ### 35
        - Type: UnitPromoted
        - Unit:
          - Level: 6
          - Health: 97%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13694
        - Player: 3: The Netherlands
        - Promotion: Naval Siege
        
        ### 36
        - Type: UnitPromoted
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 14277
        - Player: 3: The Netherlands
        - Promotion: Torpedo III
        
        ### 37
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14590
        - Player: 3: The Netherlands
        - Promotions:
          - Barrage I
          - Medic I
        
        ### 38
        - Type: CombatResult
        - Tundra Land 31,46:
          - Owner: Assyria
          - CityID: 10892
          - Population: 10
          - City: Arnhem
          - Religion: Zoroastrianism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 4
        - Defender:
          - RemainingHP: 128
          - Damage: 275
          - Player: 6: Assyria
        
        ### 39
        - Type: UnitKilledInCombat
        - KilledPlayer: 6: Assyria
        - KillerPlayer: 3: The Netherlands
        - KilledUnit: Cavalry
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 75%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 14050
        - Player: 3: The Netherlands
        - Coast 31,44:
          - Owner: Assyria
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12470
        - Player: 3: The Netherlands
        
        ### 42
        - Type: CombatResult
        - Tundra Land 31,46:
          - Owner: Assyria
          - CityID: 10892
          - Population: 10
          - City: Arnhem
          - Religion: Zoroastrianism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 55
          - Damage: 330
          - Player: 6: Assyria
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 35%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14474
        - Player: 3: The Netherlands
        - Ocean 28,45:
          - Owner: Polynesia
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 13455
        - Player: 3: The Netherlands
        - Coast 31,44:
          - Owner: Assyria
        
        ### 45
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 87%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13544
        - Player: 3: The Netherlands
        - Plots:
          - Coast 56,29:
            - Owner: Assyria
          - Coast 55,29:
            - Owner: Assyria
            - Resource: Coral
        
        ### 46
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 13406
        - Player: 3: The Netherlands
        - Plots:
          - Coast 63,30:
            - Owner: The Netherlands
          - Coast 62,31:
            - Owner: Assyria
          - Coast 62,32:
            - Owner: Assyria
          - Coast 62,33:
            - Owner: Assyria
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 38%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 13320
        - Player: 3: The Netherlands
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 13455
        - Player: 3: The Netherlands
        
        ### 49
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 3: The Netherlands
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2673
        - Build: Construct a Quarry
        - Grass Land 63,29:
          - Owner: The Netherlands
        
        ### 50
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 14458
        - Player: 3: The Netherlands
        - Tundra Hills 21,39:
          - Owner: Ethiopia
          - CityID: 10059
          - Population: 24
          - City: Stockholm
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 51
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Rifleman
          - ID: 13133
        - Player: 3: The Netherlands
        - Plots:
          - Coast 5,38:
            - Owner: Ethiopia
          - Coast 5,37:
            - Owner: Ethiopia
        
        ### 52
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14470
        - Player: 3: The Netherlands
        - Plots:
          - Grass Land 28,28:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
          - Grass Land 27,27:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 53
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 14522
        - Player: 3: The Netherlands
        - Plots:
          - Plains Land 28,33:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
          - Plains Land 29,32:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Plains Land 28,31:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 29,30:
            - Owner: The Netherlands
            - CityID: 1079
            - Population: 42
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
          - Grass Hills 28,29:
            - Owner: The Netherlands
            - Improvement: Town
            - Route: Railroad
          - Grass Land 28,28:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
          - Grass Land 27,27:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14420
        - Player: 5: China
        - Plots:
          - Grass Land 45,30:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 45,31:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 45,32:
            - Owner: Assyria
            - CityID: 1882
            - Population: 25
            - IsRiver: true
            - City: Kar-Tukulti-Ninurta
            - Religion: Zoroastrianism
            - Route: Railroad
        
        ### 55
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14554
        - Player: 5: China
        - Plots:
          - Grass Land 43,25:
            - Owner: China
            - IsRiver: true
            - Improvement: Farm
          - Grass Land 44,26:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Rice
            - Improvement: Manufactory
          - Plains Land 44,27:
            - Owner: Assyria
            - CityID: 3719
            - Population: 19
            - IsRiver: true
            - City: Carchemish
            - Religion: Zoroastrianism
            - Route: Railroad
          - Plains Land 45,28:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 14555
        - Player: 5: China
        - Plots:
          - Grass Land 43,25:
            - Owner: China
            - IsRiver: true
            - Improvement: Farm
          - Grass Land 44,26:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Rice
            - Improvement: Manufactory
          - Plains Land 44,27:
            - Owner: Assyria
            - CityID: 3719
            - Population: 19
            - IsRiver: true
            - City: Carchemish
            - Religion: Zoroastrianism
            - Route: Railroad
          - Plains Land 45,28:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12174
        - Player: 5: China
        - Grass Land 42,31:
          - Owner: City-State Okilis
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 13706
        - Player: 5: China
        - Plots:
          - Grass Land 41,29:
            - Owner: City-State Okilis
            - IsRiver: true
            - Resource: Sugar
            - Improvement: Embassy
          - Plains Land 42,29:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Lumber Mill
            - Feature: Jungle
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 11810
        - Player: 5: China
        - Plots:
          - Grass Land 42,27:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Cotton
            - Improvement: Plantation
          - Grass Land 43,27:
            - Owner: Assyria
            - Improvement: Village
        
        ### 60
        - Type: CombatResult
        - Grass Hills 44,30:
          - Owner: Assyria
          - Improvement: Mine
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 34
          - Damage: 120
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 28%
            - AI: FastAttack
            - Unit: Rifleman
            - ID: 14488
        
        ### 61
        - Type: PlayerDoneTurn
        - NextPlayer: 6: Assyria
        - Player: 5: China
        
        ### 62
        - Type: TileOwnershipChanged
        - NewOwner: 6: Assyria
        - Ocean 52,40:
          - Owner: Assyria
        
        ### 63
        - Type: CityBoughtPlot
        - WithFaithCulture: true
        - Player: 6: Assyria
        - City:
          - Name: Assur
          - Population: 25
          - ID: 1061
        - Ocean 52,40:
          - Owner: Assyria
        
        ### 64
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 13756
        - Player: 6: Assyria
        - Plots:
          - Plains Land 60,42:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 60,41:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 61,40:
            - Owner: Assyria
            - Improvement: Mine
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 13919
        - Player: 6: Assyria
        - Plots:
          - Grass Land 52,29:
            - Owner: Assyria
            - Resource: Cattle
            - Improvement: Pasture
          - Grass Land 53,30:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Feature: Jungle
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 13231
        - Player: 6: Assyria
        - Plots:
          - Coast 42,33:
            - Owner: City-State Okilis
          - Ocean 43,34:
            - Owner: Assyria
          - Coast 44,34:
            - Owner: Assyria
          - Coast 45,34:
            - Owner: Assyria
        
        ### 67
        - Type: EspionageState
        - SpyIndex: 5
        - SpyState: 0
        - SpyOwner: 6: Assyria
        
        ### 68
        - Type: EspionageState
        - SpyIndex: 5
        - SpyState: 1
        - City:
          - Owner: Assyria
          - CityID: 10892
          - Population: 10
          - City: Arnhem
          - Terrain: Tundra
          - Religion: Zoroastrianism
          - Route: Railroad
          - Plot: Land
          - X: 31
          - Y: 46
        - SpyOwner: 6: Assyria
        
        ### 69
        - Type: EspionageState
        - SpyIndex: 8
        - SpyState: 0
        - SpyOwner: 6: Assyria
        
        ### 70
        - Type: EspionageState
        - SpyIndex: 8
        - SpyState: 1
        - City:
          - Owner: City-State Abernethy
          - CityID: 1063
          - Population: 20
          - City: Abernethy
          - Terrain: Grass
          - Religion: Zoroastrianism
          - Route: Railroad
          - Plot: Land
          - X: 31
          - Y: 23
        - SpyOwner: 6: Assyria
        
        ### 71
        - Type: PlayerDoTurn
        - Player: 6: Assyria
        
        ### 72
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 56%
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 11267
        - Player: 6: Assyria
        - Promotion: Field III
        
        ### 73
        - Type: CombatResult
        - Coast 31,44:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 15
          - Damage: 40
          - Unit:
            - Level: 5
            - Health: 75%
            - AI: AssaultSea
            - Unit: Dreadnought
            - ID: 14050
          - Player: 3: The Netherlands
        
        ### 74
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 13815
        - Player: 6: Assyria
        - Plots:
          - Tundra Land 31,47:
            - Owner: Assyria
            - Improvement: Village
          - Tundra Land 31,46:
            - Owner: Assyria
            - CityID: 10892
            - Population: 10
            - City: Arnhem
            - Religion: Zoroastrianism
            - Route: Railroad
        
        ### 75
        - Type: CombatResult
        - Coast 61,33:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 22
          - Damage: 41
          - Unit:
            - Level: 4
            - Health: 86%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 13333
          - Player: 0: Ethiopia
        
        ### 76
        - Type: CombatResult
        - Coast 61,33:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 33
          - Damage: 74
          - Player: 0: Ethiopia
          - Unit:
            - Level: 4
            - Health: 70%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 13333
        
        ### 77
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Machine Gun
          - ID: 14615
        - Player: 6: Assyria
        - Plains Land 44,27:
          - Owner: Assyria
          - CityID: 3719
          - Population: 19
          - IsRiver: true
          - City: Carchemish
          - Religion: Zoroastrianism
          - Route: Railroad
        
        ### 78
        - Type: UnitCreated
        - UnitType: Machine Gun
        - Player: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14615
        - Plains Land 44,27:
          - Owner: Assyria
          - CityID: 3719
          - Population: 19
          - IsRiver: true
          - City: Carchemish
          - Religion: Zoroastrianism
          - Route: Railroad
        
        ### 79
        - Type: UnitUpgraded
        - Player: 6: Assyria
        - OldUnit:
          - Level: 2
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 11998
        - NewUnit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14615
        
        ### 80
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Assyria
        - OriginalUnit:
          - Level: 2
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 11998
        - NewOwner: 6: Assyria
        - ConvertingUnit:
          - Level: 2
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14615
        
        ### 81
        - Type: CombatResult
        - Coast 59,35:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 20
          - Damage: 80
          - Unit:
            - Level: 3
            - Health: 52%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 13522
          - Player: 0: Ethiopia
        
        ### 82
        - Type: CombatResult
        - Coast 55,29:
          - Owner: Assyria
          - Resource: Coral
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 10
          - Damage: 23
          - Unit:
            - Level: 5
            - Health: 87%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 13544
          - Player: 3: The Netherlands
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Machine Gun
          - ID: 14616
        - Player: 6: Assyria
        - Grass Hills 55,30:
          - Owner: Assyria
          - CityID: 2209
          - Population: 18
          - IsRiver: true
          - City: Dur-Sharrukin
          - Religion: Zoroastrianism
          - Route: Railroad
        
        ### 84
        - Type: UnitCreated
        - UnitType: Machine Gun
        - Player: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14616
        - Grass Hills 55,30:
          - Owner: Assyria
          - CityID: 2209
          - Population: 18
          - IsRiver: true
          - City: Dur-Sharrukin
          - Religion: Zoroastrianism
          - Route: Railroad
        
        ### 85
        - Type: UnitUpgraded
        - Player: 6: Assyria
        - OldUnit:
          - Level: 4
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 11943
        - NewUnit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14616
        
        ### 86
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Assyria
        - OriginalUnit:
          - Level: 4
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 11943
        - NewOwner: 6: Assyria
        - ConvertingUnit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14616
        
        ### 87
        - Type: CombatResult
        - Desert Land 43,32:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Farm
          - Feature: Flood Plains
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 26
          - Damage: 91
          - Unit:
            - Level: 1
            - Health: 45%
            - AI: FastAttack
            - Unit: Rifleman
            - ID: 14419
          - Player: 63: Barbarians
        
        ### 88
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Machine Gun
          - ID: 14617
        - Player: 6: Assyria
        - Desert Land 45,32:
          - Owner: Assyria
          - CityID: 1882
          - Population: 25
          - IsRiver: true
          - City: Kar-Tukulti-Ninurta
          - Religion: Zoroastrianism
          - Route: Railroad
        
        ### 89
        - Type: UnitCreated
        - UnitType: Machine Gun
        - Player: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14617
        - Desert Land 45,32:
          - Owner: Assyria
          - CityID: 1882
          - Population: 25
          - IsRiver: true
          - City: Kar-Tukulti-Ninurta
          - Religion: Zoroastrianism
          - Route: Railroad
        
        ### 90
        - Type: UnitUpgraded
        - Player: 6: Assyria
        - OldUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 11999
        - NewUnit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14617
        
        ### 91
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Assyria
        - OriginalUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 11999
        - NewOwner: 6: Assyria
        - ConvertingUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14617
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 87%
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 13866
        - Player: 6: Assyria
        - Plots:
          - Desert Hills 58,34:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 59,34:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Plains Land 59,33:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 60,32:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
        
        ### 93
        - Type: CombatResult
        - Coast 59,35:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 30
          - Damage: 110
          - Player: 0: Ethiopia
          - Unit:
            - Level: 3
            - Health: 36%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 13522
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 87%
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 13866
        - Player: 6: Assyria
        - Plots:
          - Plains Land 59,33:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 59,34:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
        
        ### 95
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 63%
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 10894
        - Player: 6: Assyria
        - Plots:
          - Plains Land 59,33:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 60,32:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
        
        ### 96
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 86%
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12179
        - Player: 6: Assyria
        - Plains Land 57,35:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 97
        - Type: CombatResult
        - Coast 59,35:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 15
          - Damage: 125
          - Player: 0: Ethiopia
          - Unit:
            - Level: 3
            - Health: 12%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 13522
        
        ### 98
        - Type: UnitKilledInCombat
        - KilledPlayer: 0: Ethiopia
        - KillerPlayer: 6: Assyria
        - KilledUnit: Destroyer
        
        ### 99
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 70%
          - AI: Defense
          - Unit: Rifleman
          - ID: 12766
        - Player: 6: Assyria
        - Plots:
          - Plains Hills 60,32:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Plains Land 61,32:
            - Owner: Assyria
            - CityID: 12599
            - Population: 11
            - City: Ur
            - Religion: Zoroastrianism
            - Route: Railroad
          - Desert Hills 61,31:
            - Owner: Assyria
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 100
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 63%
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 10894
        - Player: 6: Assyria
        - Plains Land 59,33:
          - Owner: Assyria
          - Improvement: Farm
          - Route: Railroad
        
        ### 101
        - Type: CombatResult
        - Coast 61,33:
          - Owner: Assyria
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 25
          - Damage: 99
          - Player: 0: Ethiopia
          - Unit:
            - Level: 4
            - Health: 47%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 13333
        
        ### 102
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 3081
        - Player: 6: Assyria
        - Plots:
          - Plains Hills 59,34:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Plains Land 59,33:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
        
        ### 103
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 86%
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12179
        - Player: 6: Assyria
        - Plots:
          - Desert Hills 58,34:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 59,34:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Plains Land 59,33:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 60,32:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
        
        ### 104
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 3081
        - Player: 6: Assyria
        - Plains Hills 60,32:
          - Owner: Assyria
          - Improvement: Village
          - Route: Railroad
        
        ### 105
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 83%
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 13249
        - Player: 6: Assyria
        - Coast 52,38:
          - Owner: Assyria
        
        ### 106
        - Type: CombatResult
        - Coast 53,39:
          - Owner: Assyria
          - Resource: Fish
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 30
          - Damage: 120
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - Health: 25%
            - AI: FastAttack
            - Unit: Rifleman
            - ID: 14115
        
        ### 107
        - Type: UnitKilledInCombat
        - KilledPlayer: 63: Barbarians
        - KillerPlayer: 6: Assyria
        - KilledUnit: Rifleman
        
        ### 108
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12062
        - Player: 6: Assyria
        - Plots:
          - Grass Land 44,29:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 45,30:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 44,31:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
        
        ### 109
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 70%
          - AI: Defense
          - Unit: Rifleman
          - ID: 14421
        - Player: 6: Assyria
        - Plots:
          - Grass Land 44,31:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Farm
          - Desert Hills 44,32:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Manufactory
        
        ### 110
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 70%
          - AI: CityBombard
          - Unit: Field Gun
          - ID: 11156
        - Player: 6: Assyria
        - Plains Land 43,29:
          - Owner: Assyria
          - Improvement: Lumber Mill
          - Feature: Jungle
        
        ### 111
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 14557
        - Player: 6: Assyria
        - Plots:
          - Grass Hills 52,34:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 52,33:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 53,33:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Grass Land 54,32:
            - Owner: Assyria
            - Resource: Cattle
            - Improvement: Town
            - Route: Railroad
          - Grass Land 54,31:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 54,30:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Lumber Mill
            - Feature: Jungle
        
        ### 112
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 14487
        - Player: 6: Assyria
        - Grass Land 55,28:
          - Owner: Assyria
          - Improvement: Farm
        
        ### 113
        - Type: CombatResult
        - Coast 55,29:
          - Owner: Assyria
          - Resource: Coral
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 23
          - Damage: 46
          - Player: 3: The Netherlands
          - Unit:
            - Level: 5
            - Health: 77%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 13544
        
        ### 114
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 3081
        - Player: 6: Assyria
        - Plots:
          - Plains Land 59,33:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 59,34:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 58,34:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 57,35:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 58,36:
            - Owner: Assyria
            - CityID: 1521
            - Population: 20
            - IsRiver: true
            - City: Nimrud
            - Resource: Bison
            - Religion: Zoroastrianism
            - Route: Railroad
        
        ### 115
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 14187
        - Player: 6: Assyria
        - Tundra Land 67,44:
          - Owner: Assyria
          - Resource: Deer
          - Feature: Forest
        
        ### 116
        - Type: UnitBuildCompleted
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3127
        - Build: Construct a Railroad
        - Tundra Hills 66,44:
          - Owner: Assyria
        
        ### 117
        - Type: TileImprovementChanged
        - Owner: 6: Assyria
        - OldImprovement: Academy
        - NewImprovement: Academy
        - Grass Land 50,37:
          - Owner: Assyria
          - Resource: Bison
          - Improvement: Academy
        
        ### 118
        - Type: BuildFinished
        - Player: 6: Assyria
        - Grass Land 50,37:
          - Owner: Assyria
          - Resource: Bison
          - Improvement: Academy
        
        ### 119
        - Type: UnitBuildCompleted
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 10618
        - Build: Repair an Improvement
        - Grass Land 50,37:
          - Owner: Assyria
          - Resource: Bison
          - Improvement: Academy
        
        ### 120
        - Type: UnitBuildStart
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 10618
        - Build: Repair an Improvement
        - Grass Land 50,37:
          - Owner: Assyria
          - Resource: Bison
          - Improvement: Academy
        
        ### 121
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2127
        - Player: 6: Assyria
        - Plots:
          - Plains Land 59,39:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 60,40:
            - Owner: Assyria
            - Improvement: Fort
            - Route: Railroad
          - Plains Land 60,41:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 61,42:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 61,43:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 62,44:
            - Owner: Assyria
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
        
        ### 122
        - Type: TileImprovementChanged
        - Owner: 6: Assyria
        - OldImprovement: Lumber Mill
        - NewImprovement: Lumber Mill
        - Grass Land 55,37:
          - Owner: Assyria
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 123
        - Type: BuildFinished
        - Player: 6: Assyria
        - Grass Land 55,37:
          - Owner: Assyria
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 124
        - Type: UnitBuildCompleted
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9432
        - Build: Repair an Improvement
        - Grass Land 55,37:
          - Owner: Assyria
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 125
        - Type: UnitBuildStart
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9432
        - Build: Repair an Improvement
        - Grass Land 55,37:
          - Owner: Assyria
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 126
        - Type: TileImprovementChanged
        - Owner: 6: Assyria
        - OldImprovement: Village
        - NewImprovement: Village
        - Grass Land 52,35:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 127
        - Type: BuildFinished
        - Player: 6: Assyria
        - Grass Land 52,35:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 128
        - Type: UnitBuildCompleted
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1677
        - Build: Repair an Improvement
        - Grass Land 52,35:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 129
        - Type: UnitBuildStart
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1677
        - Build: Repair an Improvement
        - Grass Land 52,35:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 130
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3173
        - Player: 6: Assyria
        - Plots:
          - Grass Land 57,36:
            - Owner: Assyria
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
          - Grass Land 57,37:
            - Owner: Assyria
            - Resource: Cattle
            - Improvement: Pasture
          - Coast 58,38:
            - Owner: Assyria
            - Resource: Coral
            - Improvement: Fishing Boats
        
        ### 131
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9219
        - Player: 6: Assyria
        - Grass Hills 56,36:
          - Owner: Assyria
          - Improvement: Mine
        
        ### 132
        - Type: TileImprovementChanged
        - Owner: 6: Assyria
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Grass Hills 56,36:
          - Owner: Assyria
          - Improvement: Mine
        
        ### 133
        - Type: BuildFinished
        - Player: 6: Assyria
        - Grass Hills 56,36:
          - Owner: Assyria
          - Improvement: Mine
        
        ### 134
        - Type: UnitBuildCompleted
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9219
        - Build: Repair an Improvement
        - Grass Hills 56,36:
          - Owner: Assyria
          - Improvement: Mine
        
        ### 135
        - Type: UnitBuildStart
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9219
        - Build: Repair an Improvement
        - Grass Hills 56,36:
          - Owner: Assyria
          - Improvement: Mine
        
        ### 136
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4370
        - Player: 6: Assyria
        - Plains Land 45,31:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 137
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4370
        - Build: Repair an Improvement
        - Plains Land 45,31:
          - Owner: Assyria
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 138
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3954
        - Player: 6: Assyria
        - Plots:
          - Grass Land 57,37:
            - Owner: Assyria
            - Resource: Cattle
            - Improvement: Pasture
          - Plains Land 58,36:
            - Owner: Assyria
            - CityID: 1521
            - Population: 20
            - IsRiver: true
            - City: Nimrud
            - Resource: Bison
            - Religion: Zoroastrianism
            - Route: Railroad
          - Plains Land 57,35:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 56,35:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Hills 55,35:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 54,35:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
        
        ### 139
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5548
        - Player: 6: Assyria
        - Plots:
          - Grass Land 52,35:
            - Owner: Assyria
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 51,35:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 51,36:
            - Owner: Assyria
            - Improvement: Farm
        
        ### 140
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5548
        - Build: Repair an Improvement
        - Plains Land 51,36:
          - Owner: Assyria
          - Improvement: Farm
        
        ### 141
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 12600
        - Player: 6: Assyria
        - Plots:
          - Grass Hills 52,34:
            - Owner: Assyria
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 51,35:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 50,35:
            - Owner: Assyria
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 50,36:
            - Owner: Assyria
            - Improvement: Farm
        
        ### 142
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 12600
        - Build: Repair an Improvement
        - Plains Land 50,36:
          - Owner: Assyria
          - Improvement: Farm
        
        ### 143
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 10893
        - Player: 6: Assyria
        - Plots:
          - Grass Land 46,28:
            - Owner: Assyria
            - Improvement: Lumber Mill
            - Feature: Jungle
          - Plains Land 45,28:
            - Owner: Assyria
            - Improvement: Village
            - Route: Railroad
        
        ### 144
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1623
        - Player: 6: Assyria
        - Snow Land 31,49:
          - Owner: Assyria
        
        ### 145
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1623
        - Build: Construct a Fort
        - Snow Land 31,49:
          - Owner: Assyria
        
        ### 146
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Machine Gun
          - ID: 14618
        - Player: 6: Assyria
        - Tundra Land 65,45:
          - Owner: Assyria
          - IsRiver: true
          - Resource: Deer
          - Improvement: Camp
          - Feature: Forest
        
        ### 147
        - Type: UnitCreated
        - UnitType: Machine Gun
        - Player: 6: Assyria
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14618
        - Tundra Land 65,45:
          - Owner: Assyria
          - IsRiver: true
          - Resource: Deer
          - Improvement: Camp
          - Feature: Forest
        
        ### 148
        - Type: UnitUpgraded
        - Player: 6: Assyria
        - OldUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12257
        - NewUnit:
          - Level: 1
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14618
        
        ### 149
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 6: Assyria
        - OriginalUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12257
        - NewOwner: 6: Assyria
        - ConvertingUnit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14618
        
        ### 150
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14560
        - Player: 6: Assyria
        - Tundra Hills 65,44:
          - Owner: Assyria
          - Improvement: Mine
          - Route: Railroad
        
        ### 151
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14562
        - Player: 6: Assyria
        - Tundra Land 66,46:
          - IsRiver: true
        
        ### 152
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12223
        - Player: 6: Assyria
        - Tundra Hills 67,46:
          - IsRiver: true
        
        ### 153
        - Type: PlayerDoneTurn
        - NextPlayer: 7: Rome
        - Player: 6: Assyria
        
        You, Ashurbanipal (leader of Assyria, Player 6), are making strategic decisions after turn 361.
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
    - You are Ashurbanipal, leader of Assyria (Player 6).
      
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
      - PlayerID: 6
      
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
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Atomic Theory: Reveals Uranium and allows you to start working on the Manhattan Project, setting the stage for the production of nuclear weapons.
        Completing it would unlock: Computers, Nuclear Fission
      
      ## Policies
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - Workers' Faculties (Level 1 Tenet of Ideology Order): Worker Faculties: Factories increase City Science output by 10%. +100% Production towards Factories, and receive 5 Free Factories in your Empire.
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Imperium (Continuing Authority Branch):
        - * Cities gain 20 Production and Gold when their borders expand, scaling with Era (40 if all Authority policies are adopted).
        - * Receive 40 Science and Culture when you found or conquer Cities, scaling with Era. Conquest bonus also scales based on City population.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Militarism (Continuing Authority Branch):
        - * +1 Happiness and +2 Culture in Cities with at least 10 Strength.
        - * -15% Unit Maintenance.
        - * -50% Route Maintenance.
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
      - Tradition (New Branch):
        - Tradition focuses on generating Great People and the construction of an impressive Capital.
        - Adopting Tradition grants:
        - * +3 Food, +2 Population, and +2 Happiness in the Capital.
        - * +1 Culture in the Capital for every 2 Citizens.
        - Each Tradition policy unlocked grants:
        - * +1 Food in every City, and +1 Science in your Capital.
        - Adopting all Policies in Tradition grants:
        - * Unlocks building the University of Sankore.
        - * +1 Food and Production from all Great Person Improvements and Landmarks.
        - * Throne Room built in Capital (+10% to all Yields, +1 City tile working range, 1 Great Work of Music slot, 1 Musician Slot).
        - * Allows for the purchase of Great Engineers with Faith starting in the Industrial Era.
  - decisions:
    - #0:
      - toolName: set-persona
      - args:
        - Rationale: Strengthen our loyalty and friendliness to reinforce our vital alliance and defensive pact with China during this challenging global war.
        - Friendliness: 7
        - Loyalty: 8
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Cultivate a very close and trusting relationship with our key ally China to ensure our defensive coalition remains steadfast.
        - Public: 40
        - Private: 40
        - TargetID: 5
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Maintain a highly hostile posture against Ethiopia, our primary competitor, who is aggressively pursuing a cultural victory and is at war with us.
        - Private: -50
        - Public: -50
        - TargetID: 0
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Maintain a highly hostile stance against the Netherlands, who possesses a massive military force and is currently sieging our cities.
        - Private: -50
        - TargetID: 3
        - Public: -50
    - #4:
      - toolName: set-research
      - args:
        - Technology: Atomic Theory
        - Rationale: Atomic Theory reveals Uranium, which is essential for nuclear deterrence and high-tier scientific infrastructure, aligning perfectly with our spaceship victory path.
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Workers' Faculties
        - Rationale: Workers' Faculties provides 5 free factories and a 10% science boost from factories, enormously boosting our industrial capacity and science output for the Spaceship victory.
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Espionage: 80
          - Offense: 20
          - Defense: 95
          - Science: 100
          - Gold: 75
          - Nuke: 80
          - Production: 85
          - Happiness: 100
          - Spaceship: 100
          - UseNuke: 80
          - Infrastructure: 75
          - TileImprovement: 75
          - Growth: 70
          - CityDefense: 90
          - Mobilization: 90
          - MilitaryTraining: 90
          - GreatPeople: 65
        - GrandStrategy: Spaceship
      - rationale: Maintain focus on the Spaceship victory, maxing out Science and Spaceship flavors, while aggressively targeting Happiness to resolve our severe unhappiness crisis. Boost defense and mobilization to withstand attacks from the Netherlands and Ethiopia.
  - tokens:
    - inputTokens: 49474
    - reasoningTokens: 5167
    - outputTokens: 410
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Status**
            
            My focus is on evaluating our current standing in Civ V, particularly concerning Ashurbanipal's strengths and weaknesses. I'm considering our strategic position around turn 361 and identifying immediate objectives.
            
            **Prioritizing Future Research**
            
            I'm now refining the immediate research path. Given our Spaceship Grand Strategy, Atomic Theory seems the most advantageous next step. It unlocks crucial technologies for science victory and offers defensive benefits via the Manhattan Project.
            
            **Evaluating Research Options**
            
            My thoughts are now weighing the merits of Atomic Theory against Combined Arms, given our ongoing conflicts with the Netherlands and Ethiopia. While Atomic Theory advances our Spaceship Grand Strategy, Combined Arms offers immediate defensive capabilities with tanks. I'm also reviewing our diplomatic status, particularly the complex ideological differences with China despite our ongoing Defensive Pact and Declaration of Friendship.
            
            **Assessing Victory Threats**
            
            My current focus is on the imminent cultural victory threat from Ethiopia. They are dangerously close to being influential with all remaining civs. I'm also monitoring the diplomatic and domination progress of the Netherlands and considering the implications of China's ideology.
            
            **Supporting Diplomatic Initiatives**
            
            I'm now prioritizing diplomatic actions. China's proposal to repeal the Passport System is excellent for hindering Ethiopia's cultural victory, so I'll support that, and sanction the Netherlands simultaneously. I'm also reviewing policy options for our Spaceship Victory path.
            
            **Adopting Social Policies**
            
            I'm evaluating our next social policy choice. We have Rationalism, so continuing down that path with `Rights of Man` is strong. However, `Workers' Faculties` from the Order tree offers significant science and production boosts, which seems more impactful given our 12 cities and need for factories.
            
            **Choosing Next Policy**
            
            I’m selecting `Workers’ Faculties` as our next social policy. This seems more beneficial given our substantial city count and production needs for factories, outweighing `Rights of Man` for now.
            
            **Strengthening Our Bloc**
            
            I'm reassessing our diplomatic ties, focusing on strengthening our alliance with China against the hostile bloc of Ethiopia, Netherlands, Polynesia, and Rome. We must ensure China remains our steadfast ally as we navigate this significant global conflict.
            
            **Fortifying Diplomatic & Defensive Posture**
            
            I'm focusing on solidifying our alliances, especially with China, by increasing our relationship score to ensure continued support. I'm also evaluating our defensive stances against Rome and Polynesia, and considering the optimal relationship settings for our ongoing wars with Ethiopia and the Netherlands, while addressing our critical happiness deficit which impacts combat effectiveness.
            
            **Analyzing Military Imbalance**
            
            My thoughts are now dominated by the dire military situation. The Netherlands' massive fleet and army present a significant threat, and even Ethiopia's forces are larger than ours. Our alliance with China helps, but the balance remains challenging. I must prioritize defense, mobilization, and science to counter these threats and secure our vulnerable sea zones and cities, especially Arnhem.
            
            **Addressing Happiness Deficit**
            
            I'm prioritizing our critical happiness deficit. Kar-Tukulti-Ninurta is at -19, and Halab at -9, impacting combat effectiveness. I'm initiating `set-flavors` to ensure Science, Defense, Mobilization, Spaceship, and Happiness remain paramount, considering available options to rectify this imbalance.
            
            **Adjusting Grand Strategy Focus**
            
            I'm recalibrating our grand strategy priorities, emphasizing Spaceship victory and Science at 100. Defense and City Defense are set to 90, with Mobilization slightly increased to 90 to bolster our forces. Crucially, Happiness is now at 100 to address our critical deficit and combat penalties.
            
            **Strengthening Ally Bonds**
            
            I am refining our diplomatic persona to bolster our alliance with China. By increasing loyalty and friendliness, I aim to ensure our continued strategic partnership against the current global conflict and secure our survival.
            
            **Solidifying Diplomatic Ties**
            
            I'm focusing on reinforcing our strategic alliance with China through increased relationship scores, ensuring steadfast support against the current global conflicts. Simultaneously, I'm adjusting our stances with Ethiopia and the Netherlands to reflect our active wars with them.
            
            **Refining Policy Choice**
            
            I'm confirming `Workers' Faculties` as the optimal next social policy due to its substantial production and science boosts for our numerous cities, outweighing `Rights of Man` for now. The free factories will also indirectly aid our happiness concerns.
            
            **Executing Strategic Directives**
            
            I am now implementing the finalized strategic directives. This involves setting our diplomatic persona towards China, formalizing our negative relationships with Ethiopia and the Netherlands, initiating research into Atomic Theory, enacting the Workers' Faculties social policy, and adjusting our grand strategy flavors as planned.
            
            **Executing Strategic Directives**
            
            I am now implementing the finalized strategic directives. This involves setting our diplomatic persona towards China, formalizing our negative relationships with Ethiopia and the Netherlands, initiating research into Atomic Theory, enacting the Workers' Faculties social policy, and adjusting our grand strategy flavors as planned.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: R9eXIDVwYPAw4BDI
          - toolName: set-persona
          - input:
            - Rationale: Strengthen our loyalty and friendliness to reinforce our vital alliance and defensive pact with China during this challenging global war.
            - Friendliness: 7
            - Loyalty: 8
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: IIT7vroy7N6u8bDF
          - toolName: set-relationship
          - input:
            - Rationale: Cultivate a very close and trusting relationship with our key ally China to ensure our defensive coalition remains steadfast.
            - Public: 40
            - Private: 40
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: kf0ibprBRaSH1m7u
          - toolName: set-relationship
          - input:
            - Rationale: Maintain a highly hostile posture against Ethiopia, our primary competitor, who is aggressively pursuing a cultural victory and is at war with us.
            - Private: -50
            - Public: -50
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: KuIf1dZVX0Jbl3UA
          - toolName: set-relationship
          - input:
            - Rationale: Maintain a highly hostile stance against the Netherlands, who possesses a massive military force and is currently sieging our cities.
            - Private: -50
            - TargetID: 3
            - Public: -50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: pnh59qqMAYUeU9Lm
          - toolName: set-research
          - input:
            - Technology: Atomic Theory
            - Rationale: Atomic Theory reveals Uranium, which is essential for nuclear deterrence and high-tier scientific infrastructure, aligning perfectly with our spaceship victory path.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: z3JG5TEtn2J46CzK
          - toolName: set-policy
          - input:
            - Policy: Workers' Faculties
            - Rationale: Workers' Faculties provides 5 free factories and a 10% science boost from factories, enormously boosting our industrial capacity and science output for the Spaceship victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: ulohSLdWrYi69aJ7
          - toolName: set-flavors
          - input:
            - Rationale: Maintain focus on the Spaceship victory, maxing out Science and Spaceship flavors, while aggressively targeting Happiness to resolve our severe unhappiness crisis. Boost defense and mobilization to withstand attacks from the Netherlands and Ethiopia.
            - Flavors:
              - Espionage: 80
              - Offense: 20
              - Defense: 95
              - Science: 100
              - Gold: 75
              - Nuke: 80
              - Production: 85
              - Happiness: 100
              - Spaceship: 100
              - UseNuke: 80
              - Infrastructure: 75
              - TileImprovement: 75
              - Growth: 70
              - CityDefense: 90
              - Mobilization: 90
              - MilitaryTraining: 90
              - GreatPeople: 65
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: R9eXIDVwYPAw4BDI
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
          - toolCallId: IIT7vroy7N6u8bDF
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: kf0ibprBRaSH1m7u
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: KuIf1dZVX0Jbl3UA
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: pnh59qqMAYUeU9Lm
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: z3JG5TEtn2J46CzK
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: ulohSLdWrYi69aJ7
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.