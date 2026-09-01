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
  - replay_nuke: 90.0
  - replay_use_nuke: 75.0
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
      - toolName: set-policy
      - args:
        - Policy: Workers' Faculties
        - Rationale: We are aiming for a Spaceship victory and currently facing a severe production and happiness deficit due to the ongoing wars. 'Workers' Faculties' provides 5 Free Factories, which will massively boost our production capabilities and add a +10% Science bonus to those cities. This directly accelerates our progress toward the Space Race while strengthening our industrial base for unit production.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Atomic Theory
        - Rationale: Our current research is Rocketry. For the next technology, 'Atomic Theory' is the ideal choice. It reveals Uranium, which is a critical late-game strategic resource for clean power and defense, and unlocks Manhattan Project, Computers, and Nuclear Fission, laying the groundwork for high-tier science and defensive deterrence.
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - CityDefense: 95
          - Production: 85
          - Happiness: 100
          - Science: 100
          - Spaceship: 100
          - Espionage: 85
          - Defense: 95
          - Gold: 80
          - Antiair: 90
      - rationale: Maintain Spaceship Grand Strategy while heavily prioritizing Happiness to combat war weariness, and Antiair/Defense to withstand heavy enemy military pressure.
  - tokens:
    - inputTokens: 49474
    - reasoningTokens: 5204
    - outputTokens: 262
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Assyrian Position**
            
            My current focus is on understanding Assyria's standing in the game. With a score of 1895, placing us fourth among major civilizations, and our current research being Rocket, I'm evaluating our strategic options for Turn 361 to leverage these strengths effectively.
            
            **Evaluating Happiness and Wars**
            
            My attention has shifted to our current unhappy status, stemming from war weariness with the Netherlands and Ethiopia. I'm assessing the impact on combat and exploring how our alliance with China might help mitigate these conflicts.
            
            **Researching Atomic Era**
            
            I'm now prioritizing research towards Atomic Theory. This is crucial given the overwhelming military strength of the Netherlands and Ethiopia, and our own ambition for a spaceship victory, which necessitates access to uranium and the Manhattan Project.
            
            **Prioritizing Atomic Theory**
            
            I'm focused on researching Atomic Theory. It's vital for securing Uranium, unlocking Computers and Nuclear Fission, which are essential for both defense and our spaceship victory goal. I'm also considering the implications of policies like "Rights of Man" for rationalism.
            
            **Choosing Next Policy**
            
            My current focus is on selecting our next Ideology policy, which is 12 turns away. Given our unhappiness and the pursuit of a spaceship victory, I'm weighing the benefits of policies that address happiness and boost science or production.
            
            **Selecting Order Policy**
            
            I am prioritizing the selection of an Order ideology policy. "Workers' Faculties" is my top choice for its significant production and science boosts, directly supporting our spaceship victory. I'm also considering "Militarism" for its potential happiness and culture gains, alongside maintenance reductions.
            
            **Choosing Ideology Policy**
            
            My current thoughts are on selecting the optimal Order ideology policy. While "Rights of Man" addresses our happiness crisis, "Workers' Faculties" provides a crucial production and science boost, directly accelerating our spaceship victory. I've chosen "Workers' Faculties" for its powerful benefits.
            
            **Selecting Next Technology**
            
            I am now prioritizing the selection of our next technology, which is Atomic Theory. This is essential for revealing Uranium, a critical resource for both defense and our ultimate goal of a spaceship victory, and unlocks vital late-game technologies.
            
            **Reviewing Diplomatic Relations**
            
            I'm now reassessing our diplomatic standings, particularly with Rome, which has denounced us. I'm also reviewing our existing agreements with Polynesia and Ethiopia to understand the implications for potential peace negotiations and ongoing conflicts.
            
            **Proposing World Congress**
            
            My current focus is on the upcoming World Congress vote in 5 turns. I've proposed sanctioning the Netherlands to hinder their diplomatic victory bid, and I'm also evaluating the threat of their proposal for the United Nations. My strong alliance with China is a key factor in these decisions.
            
            **Voting on World Congress**
            
            I'm focused on the World Congress. China's proposal to repeal the Passport System is a strategic move to counter Ethiopia's cultural victory, which aligns perfectly with our spaceship victory goal by preventing other paths to win.
            
            **Defending Key Territories**
            
            I'm currently assessing the defensive posture of Ur and Arnhem. Given the significant naval strength of Ethiopia and the Netherlands in these sea zones, I'm prioritizing the deployment of destroyers and dreadnoughts to counter their presence and maintain our strategic advantage.
            
            **Adjusting Unit Priorities**
            
            I'm focusing on naval and air defense at Ur and Arnhem due to strong enemy fleets. I'm also considering adjusting unit priorities, like increasing anti-air, while ensuring happiness and spaceship victory remain paramount given our current war weariness and resource needs.
            
            **Adjusting Game Flavors**
            
            I'm now fine-tuning our strategic priorities by adjusting game flavors. My focus is on bolstering defense, happiness, anti-air, science, spaceship production, and espionage, while ensuring our GrandStrategy remains set to Spaceship. I'm also confirming our spy placements and checking policy names.
            
            **Selecting Ideology Policy**
            
            I'm confirming my choice of "Workers' Faculties" as the next Order Ideology policy. Its substantial production and science bonuses are paramount for accelerating our spaceship victory, even though "Rights of Man" could help with happiness. I've also confirmed "Atomic Theory" as our next technology.
            
            **Confirming Grand Strategy**
            
            I am confirming our Grand Strategy as Spaceship, adjusting flavors to prioritize defense, happiness, and science. I've also finalized "Atomic Theory" as our next technology and confirmed "Workers' Faculties" as our chosen Order policy to accelerate our victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: LHvNLcg6XSc1WrOY
          - toolName: set-policy
          - input:
            - Policy: Workers' Faculties
            - Rationale: We are aiming for a Spaceship victory and currently facing a severe production and happiness deficit due to the ongoing wars. 'Workers' Faculties' provides 5 Free Factories, which will massively boost our production capabilities and add a +10% Science bonus to those cities. This directly accelerates our progress toward the Space Race while strengthening our industrial base for unit production.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 7YwyTLwMmcXFoSrF
          - toolName: set-research
          - input:
            - Technology: Atomic Theory
            - Rationale: Our current research is Rocketry. For the next technology, 'Atomic Theory' is the ideal choice. It reveals Uranium, which is a critical late-game strategic resource for clean power and defense, and unlocks Manhattan Project, Computers, and Nuclear Fission, laying the groundwork for high-tier science and defensive deterrence.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: A31LWR90trHHEKmZ
          - toolName: set-flavors
          - input:
            - Rationale: Maintain Spaceship Grand Strategy while heavily prioritizing Happiness to combat war weariness, and Antiair/Defense to withstand heavy enemy military pressure.
            - GrandStrategy: Spaceship
            - Flavors:
              - CityDefense: 95
              - Production: 85
              - Happiness: 100
              - Science: 100
              - Spaceship: 100
              - Espionage: 85
              - Defense: 95
              - Gold: 80
              - Antiair: 90
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: LHvNLcg6XSc1WrOY
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: 7YwyTLwMmcXFoSrF
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: A31LWR90trHHEKmZ
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.