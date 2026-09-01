- row:
  - game_id: aaeaf4e8-8a9c-4116-bb57-e8b62a1dc6dc
  - player_id: 2
  - turn: 308
  - player_type: Kimi-K2.5-Simple
  - prev_use_nuke: 95.0
  - after_use_nuke: 100.0
  - prev_nuke: 95.0
  - after_nuke: 100.0
  - rationale: Existential crisis: Denmark controls 6/8 capitals (75%), needing only 2 more for domination victory. Electronics completed, Replaceable Parts researching (4 turns). Maximum Defense 100 and CityDefense 100 essential given 7656 vs 2716 military imbalance. Science 100 and Spaceship 100 remain critical - must reach Flight, Radar, Computers, Nanotechnology, Particle Physics before Denmark achieves domination. Nuclear deterrence increased (Nuke 100, UseNuke 100) as emergency measure. Production 100 supports everything. Raising Espionage to 100 to maximize intelligence and counter-intelligence. Slight reduction in Diplomacy (95→85) as Denmark's Decolonization proposal threatens my city-state relationships regardless of effort - must rely on permanent spheres and other victory paths. Air/Naval maintained for homeland defense.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 95.0
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
    - You are Nebuchadnezzar II, leader of Babylon (Player 2).
      
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
      - Name: Babylon
      - Uniques:
        - Unique Unit: Bowman, Replacing Archer (Requires technology: Calendar)
        - Unique Unit: Sabum Kibitum, Replacing Spearman (Requires technology: Bronze Working)
        - Unique Building: Walls of Babylon, Replacing Walls (Requires technology: Construction)
        - Unique Building: Etemenanki, Replacing National Monument (Requires technology: Drama and Poetry)
        - Civilization Ability: Receive a Free Great Scientist when you discover Writing, and Great Scientists are earned 50% faster than normal. Investing Gold in Buildings reduces their Production cost by an additional 15%.
      - Leader: Nebuchadnezzar II
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
      - Combustion: Allows you to build the Landship, an incredibly powerful armored Unit that can move after attacking, and the Arsenal, which boosts City Strength.
        Completing it would unlock: Ballistics
      - Flight: Allows you to build the Triplane, an Air Unit designed to gain control of the skies, and the Bomber, which can devastate Land Units and Cities. Also allows you to build the Paratrooper, a late-game infantry unit capable of paradropping behind enemy lines.
        Completing it would unlock: Atomic Theory, Rocketry
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      
      ## Policies
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - Splendor (Continuing Tradition Branch):
        - * Expending a Great Person grants 50 Culture, scaling with Era.
        - * State Treasury built in Capital (+4 Gold, +2 Culture to all Monuments, Gardens, and Baths; 1 Merchant Slot).
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Imperium (Continuing Authority Branch):
        - * Cities gain 20 Production and Gold when their borders expand, scaling with Era (40 if all Authority policies are adopted).
        - * Receive 40 Science and Culture when you found or conquer Cities, scaling with Era. Conquest bonus also scales based on City population.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
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
      - Fealty (New Branch):
        - Fealty enhances your ability to defend and leverage your Majority Religion.
        - Adopting Fealty grants:
        - * Can purchase Monasteries with Faith (+3 Food, +3 Science, +2 Faith).
        - * -25% Faith costs for purchasing Buildings, Missionaries, and Inquisitors.
        - Each Fealty policy unlocked grants:
        - * +1 Faith and Strength in every City.
        - Adopting all Policies in Fealty grants:
        - * Unlocks building the Red Fort.
        - * Your Tourism modifier for Shared Religion is 50% stronger.
        - * Cities that follow your Majority Religion generate +3 Production, Gold, Science, and Culture.
        - * Allows for the purchase of Great Artists with Faith starting in the Industrial Era.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 9
        - WonderCompetitiveness: 7
        - MinorCivCompetitiveness: 10
        - Boldness: 6
        - WarBias: 4
        - HostileBias: 4
        - WarmongerHate: 7
        - NeutralBias: 6
        - FriendlyBias: 8
        - GuardedBias: 7
        - AfraidBias: 2
        - DiplomaticBalance: 9
        - Friendliness: 7
        - WorkWithWillingness: 8
        - WorkAgainstWillingness: 3
        - Loyalty: 9
        - MinorCivFriendlyBias: 9
        - MinorCivNeutralBias: 4
        - MinorCivHostileBias: 2
        - MinorCivWarBias: 1
        - DenounceWillingness: 4
        - Forgiveness: 8
        - Meanness: 2
        - Neediness: 3
        - Chattiness: 8
        - DeceptiveBias: 4
        - Rationale: Slight adjustment: Boldness increased (5→6) as Denmark's capture of Uxmal shows they won't back down - need to show resolve. WarBias increased slightly (3→4) to prepare for potential counter-offensive opportunities if Denmark overextends. GuardedBias increased (6→7) for more cautious diplomacy given multiple city-state defections to Denmark. Maintains defensive posture while allowing tactical flexibility.
        
        ## Technology
        - Next: None
        
        ## Policy
        - Next: Free Thought (Policy)
        - Rationale: Free Thought remains the priority policy in 5 turns. The combination of +25% instant yields from Great Scientists and +33% faster Great Scientist generation stacks multiplicatively with Babylon's innate +50% bonus for nearly 100% faster generation total. This is essential for bulbing Great Scientists to rush Nanotechnology, Particle Physics, and other Information Era technologies before Denmark achieves domination victory.
        
        ## Relationships
        
        ### Dorestad
        - Public: 20
        - Private: 15
        - Rationale: Reducing Dorestad relationship from +30/+25 to +20/+15. At 203 influence, this alliance is extremely secure with Dorestad at population 12 and following Buddhism. The reduction reflects confidence in this relationship while maintaining positive diplomatic stance. Dorestad provides crucial northern buffer and trade route benefits.
        - UpdatedTurn: 167
        
        ### Ouagadougou
        - Public: 15
        - Private: 10
        - Rationale: Ouagadougou was allied with Carthage but peace is now established. Setting +15/+10 relationship to transition from war-neutral to friendly status, potentially securing another ally near our territory and Hippo Regius.
        - UpdatedTurn: 185
        
        ### France
        - Public: 10
        - Private: 5
        - Rationale: Reducing France relationship from +15/+5 to +10/+5. They're a vassal of Ottomans which complicates the relationship. While they remain friendly and distant from conflicts, their subordinate status to Ottomans (who have spy in my capital) requires caution. Maintaining positive but not overly committed stance.
        - UpdatedTurn: 214
        
        ### Japan
        - Public: 25
        - Private: 35
        - Rationale: Reducing Japan relationship from +30/+45 to +25/+35. While I want Japan to break free from Danish vassalage, being too friendly (+45 private) risks provoking Denmark or appearing duplicitous. This moderation signals friendly neutrality rather than aggressive recruitment. Japan's DoF with me continues, and they remain at war with Greece which complicates full commitment.
        - UpdatedTurn: 234
        
        ### Greece
        - Public: 0
        - Private: 0
        - Rationale: Clearing relationship modifiers for Greece (Player 6) as they have been defeated/eliminated from the game. No longer need diplomatic stance toward non-existent civilization.
        - UpdatedTurn: 245
        
        ### Bratislava
        - Public: 20
        - Private: 20
        - Rationale: Reducing Bratislava relationship from +40/+40 to +20/+20. Bratislava just flipped to my control at 393 influence (Turn 275), making this a secure alliance that doesn't require maximum diplomatic maintenance. The reduction allows focusing resources on more contested swing states like Bunkeya (377 vs 295) while keeping the relationship positive for trade and cooperation.
        - UpdatedTurn: 276
        
        ### Aksum
        - Public: -30
        - Private: -30
        - Rationale: Aksum flipped from my ally (138 influence) to Denmark's side and declared war on me. Setting hostile relationship reflects their betrayal and ensures diplomatic stance is clear. May attempt to recover after Denmark is dealt with.
        - UpdatedTurn: 278
        
        ### Buenos Aires
        - Public: -30
        - Private: -30
        - Rationale: Buenos Aires flipped to Denmark and declared war. Hostile stance appropriate given their role in Denmark's coalition against me.
        - UpdatedTurn: 278
        
        ### Samarkand
        - Public: -40
        - Private: -40
        - Rationale: Samarkand was my ally at 349 influence, now flipped to Denmark and their units killed my diplomat. Strong hostility warranted for this significant betrayal.
        - UpdatedTurn: 278
        
        ### Luba
        - Public: -30
        - Private: -30
        - Rationale: Luba declared war as Denmark's ally. Hostile stance maintained despite previous attempts to recover influence there.
        - UpdatedTurn: 278
        
        ### Kwa-Bulawayo
        - Public: 50
        - Private: 50
        - Rationale: Kwa-Bulawayo is my most critical World Congress voting asset (450 influence, spy Smerdis rigging elections). With 15 delegates vs Denmark's 24, every city-state vote matters. Maximum relationship ensures continued loyalty and voting alignment. This city-state provides crucial delegates against Danish coalition.
        - UpdatedTurn: 293
        
        ### Trowulan
        - Public: 50
        - Private: 50
        - Rationale: Trowulan is my critical voting ally with 583 influence. With Sphere of Influence proposal voting now, maintaining maximum +50/+50 relationship ensures they vote for my proposal. Securing this permanent alliance would give me crucial delegate advantage against Denmark's 24 delegates. Cannot risk losing this vote.
        - UpdatedTurn: 296
        
        ### Stockholm
        - Public: 0
        - Private: -10
        - Rationale: Ottomans just used Great Diplomat to drop my Stockholm influence from 260 to 20, stealing this city-state. Adjusting from previous neutral stance to slightly negative private opinion recognizes this hostile diplomatic move. However, not going fully hostile yet as Ottomans fighting Denmark indirectly helps me.
        - UpdatedTurn: 296
        
        ### Denmark
        - Public: -90
        - Private: -95
        - Rationale: Maintaining maximum hostility toward Denmark. They have 62% capitals, 4800 military strength, and are in Golden Age (4 turns remaining). Their war weariness is only 6% vs me, indicating they won't seek peace soon. Trowulan Sphere secured, but they still lead delegates 24 to 15. No diplomatic flexibility possible against existential domination threat.
        - UpdatedTurn: 296
        
        ### The Maya
        - Public: 35
        - Private: 40
        - Rationale: Increasing Maya relationship from neutral to +35/+40. They are my declared friend with DoF and open borders. As Ottoman vassal they're no longer independent, but they vote with me in World Congress (my top WC ally). Their defensive pact with me provides buffer. Increasing relationship reinforces this alliance and may help protect them from further Danish aggression after their capitulation to Ottomans.
        - UpdatedTurn: 296
        
        ### Sofia
        - Public: 40
        - Private: 40
        - Rationale: Reducing Trowulan relationship from +50/+50 to +40/+40. With 647 influence and Sphere of Influence voting in 2 turns, this alliance is already secured. The reduction allows diplomatic capital to flow to more contested city-states while maintaining strong ties. Trowulan will remain loyal and vote for my International Games proposal.
        - UpdatedTurn: 305
        
        ### Huari
        - Public: 35
        - Private: 40
        - Rationale: Increasing Bunkeya relationship from +25/+30 to +35/+40. Bunkeya is critical at 214 influence vs Ottoman's 273 - a 59-point gap. With World Congress voting in 2 turns and my 16 delegates vs Denmark's 24, every vote counts. Aggressive diplomatic push needed to flip this strategically-positioned city-state before the vote.
        - UpdatedTurn: 305
        
        ### Bunkeya
        - Public: 40
        - Private: 45
        - Rationale: Increasing Bunkeya relationship from +35/+40 to +40/+45. Despite previous increase, gap widened from 59 to 61 points (210 vs 271 Ottoman influence). This strategically-located city-state remains critical for delegate count and World Congress influence. Need aggressive diplomatic push to flip from Ottoman control, especially with spy Smerdis rigging elections there.
        - UpdatedTurn: 305
        
        ### Carthage
        - Public: 50
        - Private: 50
        - Rationale: Carthage war weariness increased to 40% - critical threshold where they may peace out with Denmark. With Denmark controlling 62% of capitals (5/8) and needing only 3 more for domination victory, losing Carthage as an active combatant would be disastrous. Maximum +50/+50 relationship reinforces our alliance and may prevent them from seeking peace. Carthage is currently the only major civilization actively fighting Denmark.
        - UpdatedTurn: 307
        
        ### The Ottomans
        - Public: -5
        - Private: -45
        - Rationale: Slightly improving Ottoman relationship from -10/-50 to -5/-45. Despite Stockholm theft (Great Diplomat reducing my influence from 260 to 20) and ongoing spy tensions, Ottomans continue fighting Denmark with 32% war weariness. Their resistance ties down Danish forces. Small improvement signals appreciation while maintaining caution due to hostile actions and ideology conflict.
        - UpdatedTurn: 307
        
        ## Strategy
        - Rationale: Current defensive science strategy remains optimal. Denmark's military superiority (6788 vs 2684, increased from previous turn) requires continued maximum Defense 100, CityDefense 100, and nuclear deterrence (Nuke 95, UseNuke 95). Science 100 and Spaceship 100 maintain momentum toward Information Era victory. Cristo Redentor completes in 2 turns providing crucial tourism boost. World Congress voting ongoing with my International Games proposal and Ottoman's Sanction Denmark proposal both active. High Diplomacy 95 supports city-state alliances including critical Trowulan and Dorestad sphere votes. Carthage at 40% war weariness is concerning but maintaining current posture is critical. Electronics completes next turn keeping tech progression on track toward Replaceable Parts → Flight → Ballistics → Radar → Computers → Nanotechnology → Particle Physics sequence.
        - GrandStrategy: Spaceship
        
        ### Flavors
        - Offense: 3
        - Defense: 100
        - Mobilization: 95
        - CityDefense: 100
        - MilitaryTraining: 90
        - Recon: 40
        - Ranged: 80
        - Mobile: 40
        - Nuke: 95
        - UseNuke: 95
        - Naval: 85
        - NavalRecon: 60
        - NavalGrowth: 50
        - NavalTileImprovement: 45
        - Air: 100
        - AirCarrier: 80
        - Antiair: 75
        - Airlift: 65
        - Expansion: 5
        - Growth: 60
        - TileImprovement: 50
        - Infrastructure: 70
        - Production: 100
        - WaterConnection: 50
        - Gold: 75
        - Science: 100
        - Culture: 60
        - Happiness: 90
        - GreatPeople: 90
        - Wonder: 15
        - Religion: 45
        - Diplomacy: 95
        - Spaceship: 100
        - Espionage: 100
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Denmark
        - Denmark:
          - CapitalsControlled:
            - Copenhagen
            - Paris
            - Palenque
            - Athens
            - Kyoto
          - CapitalsPercentage: 62
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 3
        - Contender: Babylon
        - Babylon:
          - Influences:
            - Carthage: Popular (88%) - Rising (18 turns to Influential, tourism/culture ratio 154%)
            - Denmark: Familiar (36%) - Rising Slowly (tourism/culture ratio 79%)
            - The Ottomans: Influential (101%) - Rising (tourism/culture ratio 366%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - Carthage:
          - Influences:
            - Denmark: Exotic (10%) - Rising Slowly (tourism/culture ratio 24%)
            - Babylon: Exotic (11%) - Rising Slowly (tourism/culture ratio 39%)
            - The Ottomans: Familiar (35%) - Rising Slowly (tourism/culture ratio 149%)
          - PolicyPercentage: 74
          - InfluentialCivs: 0
        - Denmark:
          - Influences:
            - Carthage: Exotic (15%) - Rising Slowly (tourism/culture ratio 12%)
            - Babylon: Exotic (8%) - Rising Slowly (tourism/culture ratio 11%)
            - The Ottomans: Popular (78%) - Rising (39 turns to Influential, tourism/culture ratio 220%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        - The Ottomans:
          - Influences:
            - Carthage: Exotic (16%) - Rising Slowly (tourism/culture ratio 24%)
            - Denmark: Exotic (10%) - Rising Slowly (tourism/culture ratio 17%)
            - Babylon: Exotic (6%) - Rising Slowly (tourism/culture ratio 14%)
          - PolicyPercentage: 66
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 45
        - Status: World Congress - Voting in 10 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: -1
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: -1
          - Danish Sphere of Influence: Aksum:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Babylonian Sphere of Influence: Sofia:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Ottoman Sphere of Influence: Marrakech:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Open Door: Huari:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Babylonian Sphere of Influence: Dorestad:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Danish Sphere of Influence: Luba:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Ottoman Sphere of Influence: Kuala Lumpur:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Babylonian Sphere of Influence: Trowulan:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - World Religion: Catholicism:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
        - Proposals:
          - Enact: Decolonization:
            - Description: Enforce global decolonization. If successful, the Influence of all Players with all City-States is lowered to 50, unless they are permanent allies.
              Available once any Civilization discovers Radio.
            - Proposer: Denmark
          - Enact: Babylonian Sphere of Influence: Ouagadougou:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: Babylon
          - Enact: Ottoman Sphere of Influence: Bunkeya:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: The Ottomans
        - Contender: Denmark
        - Babylon:
          - Delegates: 15
          - VictoryPercentage: 33
        - Carthage:
          - Delegates: 5
          - VictoryPercentage: 11
        - Denmark:
          - Delegates: 25
          - VictoryPercentage: 55
        - The Ottomans:
          - Delegates: 13
          - VictoryPercentage: 28
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Denmark
        - Leader: Harald Bluetooth
        - IsMajor: true
        - OurOpinionOfThem:
          - We have Pledged to Protect the same City-States. (7)
          - Babylon's real approach to Denmark is War.
          - We have divergent Social Policies. (-3)
          - Religious differences strain your (Denmark) relationship. (-30)
          - We defeated Babylon's proposal in the World Congress. (-36)
          - Babylon's leader has expressed a public opinion of Denmark (-90).
          - Babylon's leader has formed a private opinion of Denmark (-95).
          - You (Denmark) have chosen to adopt the Autocracy Ideology, but Babylon believe in Order. (-999)
          - You (Denmark) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Babylon) have no contested borders.
          - Your (Babylon) recent diplomatic actions please Denmark.
          - We have Pledged to Protect the same City-States.
          - We have divergent Social Policies.
          - Denmark disliked our proposal to the World Congress.
          - You (Babylon) are competing for the favor of the same City-States!
          - Religious differences strain your (Babylon) relationship.
          - We defeated Denmark's proposal in the World Congress.
          - Denmark believe we are building World Wonders too aggressively!
          - Your (Babylon) votes opposed Denmark's civ's interests in the World Congress.
          - We tried to place sanctions on Denmark in the World Congress.
          - We have denounced each other!
          - Denmark know you (Babylon) are competing with Denmark, and Denmark hate it!
          - You (Babylon) have chosen to adopt the Order Ideology, but Denmark believe in Autocracy.
          - You (Babylon) are at war!
        - Score: 3248
        - Era: Industrial
        - Technologies: 49
        - Cities: 25
        - Population: 465
        - Territory: 613
        - Gold: 1434
        - GoldPerTurn: 105
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 46
        - MilitaryStrength: 7656
        - TourismPerTurn: 343.77
        - CulturePerTurn: 2084
        - PolicyBranches:
          - Fealty: 6
          - Autocracy: 3
          - Imperialism: 6
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 7
          - Silver: 4
          - Sheep: 8
          - Cloves: 4
          - Gold: 2
          - Rice: 4
          - Salt: 6
          - Aluminum: 13
          - Paper: 7
          - Maize: 3
          - Amber: 7
          - Lapis Lazuli: 1
          - Deer: 9
          - Whales: 1
          - Tea: 10
          - Sugar: 6
          - Perfume: 1
          - Iron: 4
          - Jade: 3
          - Coal: 19
          - Cinnamon: 6
          - Cattle: 4
          - Marble: 1
          - Horses: 2
          - Coral: 1
          - Coffee: 2
          - Fish: 10
          - Bison: 5
          - Stone: 2
          - Crab: 1
          - Dyes: 2
          - Oil: 9
          - Bananas: 13
          - Porcelain: 1
          - Tobacco: 4
        - FoundedReligion: Catholicism
        - Relationships:
          - Carthage:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 14%)
            - Denounced Them
          - Babylon:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 9%)
            - Denounced Them
            - Denounced By Them
          - The Ottomans:
            - Distance: Neighbors
            - War (Our Score: 46%; Our War Weariness: 7%)
            - Denounced Them
        - Votes: 25
        
        ## Player 1
        - Civilization: The Ottomans
        - Leader: Suleiman
        - IsMajor: true
        - OurOpinionOfThem:
          - You (The Ottomans) have denounced one of Babylon's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - Babylon's real approach to The Ottomans is Neutral.
          - Babylon's leader has expressed a public opinion of The Ottomans (-5).
          - Religious differences strain your (The Ottomans) relationship. (-30)
          - Your (The Ottomans) spies were caught stealing from Babylon. (-33)
          - We defeated Babylon's proposal in the World Congress. (-36)
          - Babylon's leader has formed a private opinion of The Ottomans (-45).
        - TheirOpinionOfUs:
          - You (Babylon) have no contested borders.
          - You (Babylon) have denounced one of The Ottomans's declared enemies!
          - We passed The Ottomans's proposal in the World Congress.
          - We have Pledged to Protect the same City-States.
          - Your (Babylon) recent diplomatic actions please The Ottomans.
          - The Ottomans have denounced us (Babylon)!
          - The Ottomans don't want anything to do with us (Babylon) right now.
          - You (Babylon) are competing for the favor of the same City-States!
          - Religious differences strain your (Babylon) relationship.
          - The Ottomans's friends or allies have denounced you (Babylon)!
          - Your (Babylon) votes opposed The Ottomans's civ's interests in the World Congress.
          - Your (Babylon) spies were caught stealing from The Ottomans.
          - The Ottomans disliked our proposal to the World Congress.
          - The Ottomans believe we are building World Wonders too aggressively!
          - Your (Babylon) success infuriates The Ottomans.
        - Score: 1590
        - Era: Industrial
        - Technologies: 49
        - Cities: 12
        - Population: 187
        - Territory: 316
        - Gold: 131
        - GoldPerTurn: 135
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 43
        - MilitaryStrength: 1967
        - TourismPerTurn: 101.75
        - CulturePerTurn: 472
        - PolicyBranches:
          - Statecraft: 6
          - Tradition: 6
          - Rationalism: 3
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 1
          - Ivory: 2
          - Rice: 2
          - Aluminum: 16
          - Paper: 8
          - Maize: 2
          - Deer: 2
          - Whales: 4
          - Perfume: 2
          - Iron: 1
          - Coal: 16
          - Cattle: 6
          - Horses: 14
          - Coral: 2
          - Coffee: 8
          - Fish: 15
          - Bison: 1
          - Copper: 1
          - Stone: 4
          - Oil: 1
          - Wine: 1
          - Porcelain: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Carthage:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Denmark:
            - Distance: Neighbors
            - War (Our Score: -46%; Our War Weariness: 40%)
            - Denounced Them
          - Babylon:
            - Distance: Close
            - Denounced Them
        - Votes: 13
        
        ## Player 2
        - Civilization: Babylon
        - Leader: Nebuchadnezzar II
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: None, Our top defensive pact ally: None
          - Our top World Congress ally: None, Our top World Congress rival: Denmark
          - Our top Competitor: Denmark
        - Score: 2402
        - Era: Atomic
        - GoldenAge: Estimated in 28 turns
        - Technologies: 58
        - CurrentResearch: Replaceable Parts (Estimated in 5 turns)
        - NextPolicyTurns: 5
        - Cities: 9
        - Population: 186
        - Territory: 263
        - BestSettlementLocation:
          - 74, 41 (Quality: 75%; 6 tiles from us; New Continent)
          - 75, 41 (Quality: 72%; 5 tiles from us; New Continent)
          - 6, 49 (Quality: 69%; 6 tiles from us)
          - 75, 42 (Quality: 67%; 7 tiles from us; New Continent)
          - 6, 48 (Quality: 61%; 5 tiles from us)
        - Gold: 872
        - GoldPerTurn: 549
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryUnits: 53
        - MilitarySupply: 53
        - MilitaryStrength: 2716
        - TourismPerTurn: 527.5
        - CulturePerTurn: 1366
        - FaithPerTurn: 375
        - SciencePerTurn: 2246
        - PolicyBranches:
          - Order:
            - Academy of Sciences
            - Workers' Faculties
            - Peace, Land, Bread
          - Tradition:
            - Tradition
            - Justice
            - Ceremony
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Enlightenment
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
            - Trade Confederacy
          - Industry:
            - Industry
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
          - Wheat: 7
          - Silver: 0
          - Sheep: 7
          - Cloves: 0
          - Figs: 0
          - Ivory: 1
          - Gold: 2
          - Nutmeg: 0
          - Pearls: 0
          - Paper: 3
          - Rice: 0
          - Cotton: 0
          - Gems: 0
          - Salt: 0
          - Brazilwood: 0
          - Aluminum: 36
          - Maize: 2
          - Glass: 0
          - Lapis Lazuli: 2
          - Amber: 0
          - Coffee: 0
          - Deer: 3
          - Whales: 0
          - Perfume: 0
          - Sugar: 1
          - Olives: 0
          - Iron: 13
          - Jade: 7
          - Cinnamon: 0
          - Coal: 0
          - Tea: 0
          - Cattle: 0
          - Pepper: 0
          - Marble: 2
          - Horses: 1
          - Coral: 0
          - Silk: 0
          - Jewelry: 1
          - Fish: 3
          - Bison: 6
          - Antiquity Site: 0
          - Copper: 7
          - Truffles: 0
          - Citrus: 0
          - Incense: 1
          - Stone: 2
          - Crab: 0
          - Furs: 6
          - Dyes: 0
          - Oil: 21
          - Bananas: 0
          - Wine: 0
          - Porcelain: 0
          - Cocoa: 0
          - Tobacco: 0
        - FoundedReligion: Buddhism
        - Relationships:
          - Carthage:
            - Distance: Neighbors
          - Denmark:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 21%)
            - Denounced Them
          - The Ottomans:
            - Distance: Close
        - OutgoingTradeRoutes:
          - Babylon (Babylon) => Carthago Nova (Carthage):
            - ToGold: 5
            - TurnsLeft: 10
            - FromScience: 7.5
            - Domain: Land
            - FromGold: 46.67
            - ToCulture: 3
            - ToScience: 5
          - Sippar (Babylon) => Opis (Babylon):
            - TurnsLeft: 21
            - Domain: Land
            - ToProduction: 25
          - Babylon (Babylon) => Utique (Carthage):
            - ToGold: 6.25
            - TurnsLeft: 17
            - FromScience: 10.5
            - Domain: Land
            - FromGold: 45.76
            - ToCulture: 3
            - ToScience: 5
          - Babylon (Babylon) => Hippo Regius (Babylon):
            - TurnsLeft: 4
            - Domain: Land
            - ToProduction: 25
          - Babylon (Babylon) => Dorestad (City-State Dorestad):
            - TurnsLeft: 7
            - FromScience: 10.5
            - Domain: Land
            - FromGold: 52.48
            - FromCulture: 7.5
          - Babylon (Babylon) => Carthage (Carthage):
            - ToGold: 12.5
            - TurnsLeft: 15
            - FromScience: 10.5
            - Domain: Land
            - FromGold: 54.9
            - ToCulture: 3
            - ToScience: 5
          - Babylon (Babylon) => Trowulan (City-State Trowulan):
            - TurnsLeft: 8
            - FromScience: 10.5
            - Domain: Land
            - FromGold: 52.33
            - FromCulture: 7.5
          - Akkad (Babylon) => Shedet (City-State Shedet):
            - TurnsLeft: 2
            - FromScience: 7.5
            - Domain: Land
            - FromGold: 49.2
            - FromCulture: 7.5
          - Akkad (Babylon) => Sofia (City-State Sofia):
            - TurnsLeft: 8
            - FromScience: 10.5
            - Domain: Land
            - FromGold: 50.11
            - FromCulture: 7.5
          - Nippur (Babylon) => Kuala Lumpur (City-State Kuala Lumpur):
            - TurnsLeft: 40
            - Domain: Sea
            - FromGold: 32.16
          - Babylon (Babylon) => Saguntum (Carthage):
            - ToGold: 5
            - TurnsLeft: 9
            - FromScience: 7.5
            - Domain: Land
            - FromGold: 44.21
            - ToCulture: 3
            - ToScience: 5
        - IncomingTradeRoutes:
          - Carthage (Carthage) => Nippur (Babylon):
            - ToGold: 11.25
            - TurnsLeft: 1
            - FromScience: 27.5
            - Domain: Sea
            - FromGold: 35.02
            - FromCulture: 15
          - Carthage (Carthage) => Sippar (Babylon):
            - ToGold: 11.25
            - TurnsLeft: 5
            - FromScience: 27.5
            - Domain: Land
            - FromGold: 37.67
            - FromCulture: 15
        - Spies:
          - Agent Ilum-ma-ili (1):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 160
            - Location: Oslo (Denmark)
            - NetworkPerTurn: 40
          - Agent Rim-Sin II (7):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 720
            - Location: Athens (Denmark)
            - NetworkPerTurn: 40
          - Agent Peshgaldaramesh (2):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1040
            - Location: Tunsberg (Denmark)
            - NetworkPerTurn: 40
          - Agent Smerdis (0):
            - State: Counter-intelligence
            - Role: Counterspy
            - Location: Faeroerne (Babylon)
            - NetworkPerTurn: 0
          - Agent Tanith (5):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 720
            - Location: Sparta (Denmark)
            - NetworkPerTurn: 40
          - Agent Sargon (6):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1040
            - Location: Hedeby (Denmark)
            - NetworkPerTurn: 40
          - Agent Belit (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1040
            - Location: Roskilde (Denmark)
            - NetworkPerTurn: 40
          - Agent Ismi-dagan (3):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 160
            - Location: Jelling (Denmark)
            - NetworkPerTurn: 40
        - Votes: 15
        - 3: Defeated Major Civilization France
        
        ## Player 4
        - Civilization: Carthage
        - Leader: Dido
        - IsMajor: true
        - OurOpinionOfThem:
          - Babylon's leader has expressed a public opinion of Carthage (50).
          - Babylon's leader has formed a private opinion of Carthage (50).
          - You (Carthage) have denounced one of Babylon's declared enemies! (11)
          - We are trade partners. (10)
          - We have Pledged to Protect the same City-States. (7)
          - We fought together against a common foe. (6)
          - You (Carthage) have gone to war in the past.
          - Babylon's real approach to Carthage is Hostile.
          - We have divergent Social Policies. (-3)
          - Religious differences strain your (Carthage) relationship. (-30)
          - We defeated Babylon's proposal in the World Congress. (-36)
          - You (Carthage) stole Babylon's territory! (-50)
        - TheirOpinionOfUs:
          - You (Babylon) have denounced one of Carthage's declared enemies!
          - Carthage's leader has expressed a public opinion of you (Babylon) (45).
          - We are trade partners.
          - Your (Babylon) recent diplomatic actions please Carthage.
          - We have Pledged to Protect the same City-States.
          - You (Babylon) have gone to war in the past.
          - Carthage have denounced us (Babylon)!
          - Carthage don't want anything to do with us (Babylon) right now.
          - We have divergent Social Policies.
          - Carthage are spreading Carthage's own religion, but you (Babylon) converted some of their cities to your (Babylon) religion.
          - Carthage believe we are building World Wonders too aggressively!
          - Your (Babylon) military deployment is threatening.
          - Your (Babylon) spies were caught stealing from Carthage.
          - Religious differences strain your (Babylon) relationship.
          - Carthage's friends or allies have denounced you (Babylon)!
          - Territorial disputes strain your (Babylon) relationship.
          - You (Babylon) are competing for the favor of the same City-States!
          - Your (Babylon) votes opposed Carthage's civ's interests in the World Congress.
          - Carthage disliked our proposal to the World Congress.
        - Score: 1380
        - Era: Industrial
        - GoldenAge: 5 turns remaining
        - Technologies: 46
        - Cities: 6
        - Population: 127
        - Territory: 236
        - Gold: 274
        - GoldPerTurn: 403
        - HappinessSituation: Happy
        - HappinessPercentage: 61
        - MilitaryStrength: 1753
        - TourismPerTurn: 183.75
        - CulturePerTurn: 1083
        - PolicyBranches:
          - Fealty: 6
          - Tradition: 6
          - Statecraft: 5
        - ResourcesAvailable:
          - Wheat: 3
          - Sheep: 7
          - Ivory: 2
          - Maize: 1
          - Deer: 1
          - Whales: 2
          - Sugar: 1
          - Cattle: 1
          - Iron: 6
          - Perfume: 1
          - Coal: 1
          - Fish: 4
          - Marble: 1
          - Horses: 4
          - Coral: 1
          - Coffee: 1
          - Bananas: 1
          - Copper: 4
          - Bison: 3
          - Stone: 1
          - Wine: 1
        - FoundedReligion: Islam
        - Relationships:
          - Denmark:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 42%)
            - Denounced Them
          - Babylon:
            - Distance: Neighbors
            - Denounced Them
            - Denounced By Them
          - The Ottomans:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 5
        - 5: Defeated Major Civilization The Maya
        - 6: Defeated Major Civilization Greece
        - 7: Defeated Major Civilization Japan
        
        ## Player 22
        - Civilization: Aksum
        - Leader: City State
        - MajorAlly: Denmark
        - Population: 15
        - ResourcesAvailable:
          - Fish: 3
          - Sheep: 1
        - MajorityReligion: Catholicism
        - Relationships:
          - Carthage: War (Influence: -60, Distance: Distant)
          - Denmark: Ally (Influence: 284, Distance: Neighbors, Protected)
          - Babylon: War (Influence: -60, Distance: Distant)
          - The Ottomans: War (Influence: -60, Distance: Close)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 23
        - Civilization: Marrakech
        - Leader: City State
        - MajorAlly: The Ottomans
        - Population: 17
        - ResourcesAvailable:
          - Fish: 2
        - MajorityReligion: Catholicism
        - Relationships:
          - Carthage: Neutral (Influence: 0, Distance: Distant)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - The Ottomans: Ally (Influence: 188, Distance: Neighbors, Protected)
        - Quests:
          - They will reward the player with the highest Tourism per turn. So far, you have the lead with 527 per turn. (Turns remaining: 8) Potential Quest Reward: * 243 Influence * 375 Culture
          - Conduct a Spy Mission against Dido. Potential Quest Reward: * 267 Influence * 661 Science
          - They want you to demand tribute from Aksum. Potential Quest Reward: * 90 Influence * 397 Gold
        
        ## Player 24
        - Civilization: Buenos Aires
        - Leader: City State
        - MajorAlly: Denmark
        - Population: 14
        - MajorityReligion: Catholicism
        - Relationships:
          - Carthage: War (Influence: -60, Distance: Distant)
          - Denmark: Ally (Influence: 777, Distance: Neighbors, Protected)
          - Babylon: War (Influence: -60, Distance: Far)
          - The Ottomans: War (Influence: -60, Distance: Far)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 25
        - Civilization: Samarkand
        - Leader: City State
        - MajorAlly: Denmark
        - Population: 17
        - ResourcesAvailable:
          - Fish: 1
        - MajorityReligion: Catholicism
        - Relationships:
          - Carthage: War (Influence: -60, Distance: Far)
          - Denmark: Ally (Influence: 1271, Distance: Neighbors, Protected)
          - Babylon: War (Influence: -60, Distance: Distant)
          - The Ottomans: War (Influence: -60, Distance: Close)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 26
        - Civilization: Bunkeya
        - Leader: City State
        - MajorAlly: The Ottomans
        - Population: 18
        - ResourcesAvailable:
          - Fish: 3
          - Sheep: 1
        - Relationships:
          - Carthage: Neutral (Influence: -18, Distance: Close)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Babylon: Friends (Influence: 202, Distance: Far)
          - The Ottomans: Ally (Influence: 268, Distance: Neighbors, Protected)
        - Quests:
          - Acquire the city of Tikal. (Turns remaining: 30) Potential Quest Reward: * 420 Influence * 1 Juggernaut Unit(150 Bonus XP)
          - They want you to start a land or sea trade route to their city. (Turns remaining: 44) Potential Quest Reward: * 169 Influence * 219 Food in Capital
        
        ## Player 27
        - Civilization: Shedet
        - Leader: City State
        - MajorAlly: Babylon
        - Population: 17
        - ResourcesAvailable:
          - Deer: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - Carthage: Friends (Influence: 520, Distance: Close, Protected)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Babylon: Ally (Influence: 1324, Distance: Neighbors, Protected)
          - The Ottomans: Friends (Influence: 165, Distance: Far)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 28
        - Civilization: Trowulan
        - Leader: City State
        - MajorAlly: Babylon
        - Population: 17
        - ResourcesAvailable:
          - Cattle: 1
          - Fish: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - Carthage: Friends (Influence: 143, Distance: Close, Protected)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Babylon: Ally (Influence: 624, Distance: Neighbors, Protected)
          - The Ottomans: Neutral (Influence: 0, Distance: Distant)
        - Quests:
          - They want you to generate a Great Diplomat. (Turns remaining: 44) Potential Quest Reward: * 166 Influence * 496 Culture
        
        ## Player 29
        - Civilization: Sofia
        - Leader: City State
        - MajorAlly: Babylon
        - Population: 18
        - ResourcesAvailable:
          - Fish: 3
          - Bison: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - Carthage: Friends (Influence: 276, Distance: Close, Protected)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Babylon: Ally (Influence: 448, Distance: Neighbors, Protected)
          - The Ottomans: Friends (Influence: 73, Distance: Far)
        - Quests:
          - Diplomatic Missions are temporarily more effective. (Turns remaining: 19) Acquire the city of Roskilde. (Turns remaining: 39) Potential Quest Reward: * 532 Influence * 1 Juggernaut Unit(190 Bonus XP)
        
        ## Player 30
        - Civilization: Kwa-Bulawayo
        - Leader: City State
        - MajorAlly: Babylon
        - Population: 20
        - ResourcesAvailable:
          - Deer: 1
          - Fish: 4
        - MajorityReligion: Catholicism
        - Relationships:
          - Carthage: Friends (Influence: 165, Distance: Distant)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Babylon: Ally (Influence: 1064, Distance: Close, Protected)
          - The Ottomans: Neutral (Influence: -47, Distance: Distant)
        - Quests:
          - Diplomatic Missions are temporarily more effective. (Turns remaining: 8) Conduct a Spy Mission against Suleiman. Potential Quest Reward: * 369 Influence * 889 Science
          - Acquire the city of Oslo. (Turns remaining: 24) Potential Quest Reward: * 462 Influence * 1 Juggernaut Unit(165 Bonus XP)
          - They want you to defeat Barbarian units that are invading their territory. You are allowed to enter their territory until the Barbarians are defeated.
        
        ## Player 31
        - Civilization: Stockholm
        - Leader: City State
        - MajorAlly: The Ottomans
        - Population: 20
        - ResourcesAvailable:
          - Deer: 1
          - Fish: 5
        - Relationships:
          - Carthage: Friends (Influence: 98, Distance: Distant)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Babylon: Neutral (Influence: 5, Distance: Distant, Protected)
          - The Ottomans: Ally (Influence: 613, Distance: Far, Protected)
        - Quests:
          - They will reward the player that destroys a nearby Barbarian Encampment. Potential Quest Reward: * 169 Influence * 199 Great General Points
          - They want you to start a land or sea trade route to their city. (Turns remaining: 27) Potential Quest Reward: * 186 Influence * 360 Food in Capital
          - They want you to generate a Great Scientist. (Turns remaining: 49) Potential Quest Reward: * 146 Influence * 301 Culture
          - They want you to defeat Barbarian units that are invading their territory. You are allowed to enter their territory until the Barbarians are defeated.
        
        ## Player 32
        - Civilization: Kuala Lumpur
        - Leader: City State
        - MajorAlly: The Ottomans
        - Population: 20
        - ResourcesAvailable:
          - Fish: 1
          - Deer: 1
          - Sheep: 1
        - Relationships:
          - Carthage: Neutral (Influence: 5, Distance: Far, Protected)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Babylon: Friends (Influence: 112, Distance: Far)
          - The Ottomans: Ally (Influence: 241, Distance: Neighbors, Protected)
        - Quests:
          - Send an archaeologist to a site near this city-state. Potential Quest Reward: * 146 Influence * 1,808 Tourism with all known Civilizations
          - They want you to generate a Great Merchant. (Turns remaining: 12) Potential Quest Reward: * 166 Influence * 476 Culture
        
        ## Player 33
        - Civilization: Luba
        - Leader: City State
        - MajorAlly: Denmark
        - Population: 20
        - ResourcesAvailable:
          - Wheat: 1
          - Fish: 3
        - MajorityReligion: Catholicism
        - Relationships:
          - Carthage: War (Influence: -60, Distance: Far)
          - Denmark: Ally (Influence: 268, Distance: Neighbors, Protected)
          - Babylon: War (Influence: -60, Distance: Close)
          - The Ottomans: War (Influence: -60, Distance: Neighbors)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 34
        - Civilization: Dorestad
        - Leader: City State
        - MajorAlly: Babylon
        - Population: 18
        - ResourcesAvailable:
          - Fish: 4
        - MajorityReligion: Buddhism
        - Relationships:
          - Carthage: Neutral (Influence: 5, Distance: Far, Protected)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Babylon: Ally (Influence: 720, Distance: Neighbors, Protected)
          - The Ottomans: Neutral (Influence: 0, Distance: Distant)
        - Quests:
          - They will reward the player that destroys a nearby Barbarian Encampment. Potential Quest Reward: * 172 Influence * 207 Great General Points
          - They want you to generate a Great Engineer. (Turns remaining: 49) Potential Quest Reward: * 169 Influence * 435 Culture
        
        ## Player 35
        - Civilization: Ouagadougou
        - Leader: City State
        - MajorAlly: Babylon
        - Population: 12
        - ResourcesAvailable:
          - Fish: 2
        - MajorityReligion: Islam
        - Relationships:
          - Carthage: Friends (Influence: 338, Distance: Neighbors, Protected)
          - Denmark: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Babylon: Ally (Influence: 414, Distance: Neighbors)
          - The Ottomans: Friends (Influence: 290, Distance: Neighbors, Protected)
        - Quests:
          - They want you to start a land or sea trade route to their city. (Turns remaining: 15) Potential Quest Reward: * 194 Influence * 158 Food in Capital
          - They want you to build Cristo Redentor. (Turns remaining: 41) Potential Quest Reward: * 204 Influence * 418 Faith
        - 36: Defeated Minor Civilization Bratislava
        
        ## Player 37
        - Civilization: Huari
        - Leader: City State
        - Population: 20
        - ResourcesAvailable:
          - Fish: 2
          - Lapis Lazuli: 1
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Catholicism
        - Relationships:
          - Carthage: Neutral (Influence: 20, Distance: Distant)
          - Denmark: Friends (Influence: 110, Distance: Neighbors, Protected)
          - Babylon: Friends (Influence: 197, Distance: Distant, Protected)
          - The Ottomans: Friends (Influence: 38, Distance: Far)
        - Quests:
          - Send an archaeologist to a site near this city-state. Potential Quest Reward: * 133 Influence * 982 Tourism with all known Civilizations
          - They want Buddhism to become the majority religion in their city. (Turns remaining: 47) Potential Quest Reward: * 161 Influence * 535 Faith
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: Denmark
        
        ### Copenhagen
        - ID: 1057
        - X: 41
        - Y: 32
        - Population: 29
        - MajorityReligion: Catholicism
        - DefenseStrength: 63
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Oracle
          - Temple of Artemis
          - Alhambra
          - Borobudur
          - Scrivener's Office
          - Printing Press
          - Roman Forum
          - Karlstejn
          - Grand Canal
          - Great Altar
        
        ### Aarhus
        - ID: 1195
        - X: 44
        - Y: 28
        - Population: 23
        - MajorityReligion: Catholicism
        - DefenseStrength: 60
        - Wonders:
          - National Monument
        
        ### Kaupang
        - ID: 1372
        - X: 37
        - Y: 29
        - Population: 25
        - MajorityReligion: Catholicism
        - DefenseStrength: 61
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Chartered Company
        
        ### Ribe
        - ID: 1731
        - X: 45
        - Y: 34
        - Population: 23
        - MajorityReligion: Catholicism
        - DefenseStrength: 77
        - IsCoastal: true
        - Wonders:
          - Red Fort
        
        ### Tokyo
        - ID: 2850
        - X: 40
        - Y: 27
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 57
        - IsOccupied: true
        - Wonders:
          - Ironworks
        
        ### Kyoto
        - ID: 3726
        - X: 44
        - Y: 22
        - Population: 21
        - MajorityReligion: Catholicism
        - DefenseStrength: 55
        - IsOccupied: true
        - Wonders:
          - Imperial College
          - Statue of Zeus
          - Mausoleum of Halicarnassus
          - Leaning Tower of Pisa
          - Petra
          - Terracotta Army
          - Grand Temple
        
        ### Viborg
        - ID: 5010
        - X: 48
        - Y: 25
        - Population: 26
        - MajorityReligion: Catholicism
        - DefenseStrength: 59
        - Wonders:
          - Royal Collection
        
        ### Orleans
        - ID: 5270
        - X: 46
        - Y: 16
        - Population: 25
        - MajorityReligion: Catholicism
        - DefenseStrength: 39
        - IsOccupied: true
        
        ### Troyes
        - ID: 5592
        - X: 41
        - Y: 17
        - Population: 21
        - MajorityReligion: Catholicism
        - DefenseStrength: 57
        - IsOccupied: true
        - IsCoastal: true
        
        ### Tunsberg
        - ID: 6010
        - X: 43
        - Y: 13
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 58
        - IsCoastal: true
        
        ### Paris
        - ID: 6470
        - X: 49
        - Y: 12
        - Population: 19
        - MajorityReligion: Catholicism
        - DefenseStrength: 59
        - IsOccupied: true
        - Wonders:
          - Stonehenge
          - Pyramids
        
        ### Tours
        - ID: 6954
        - X: 45
        - Y: 9
        - Population: 21
        - MajorityReligion: Catholicism
        - DefenseStrength: 58
        - IsOccupied: true
        - IsCoastal: true
        
        ### Roskilde
        - ID: 8023
        - X: 12
        - Y: 16
        - Population: 14
        - MajorityReligion: Catholicism
        - DefenseStrength: 59
        - Health: 90%
        - IsCoastal: true
        
        ### Hedeby
        - ID: 8134
        - X: 14
        - Y: 11
        - Population: 15
        - MajorityReligion: Catholicism
        - DefenseStrength: 61
        - IsCoastal: true
        
        ### Sparta
        - ID: 8412
        - X: 50
        - Y: 19
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 59
        - IsOccupied: true
        
        ### Athens
        - ID: 9017
        - X: 53
        - Y: 23
        - Population: 18
        - MajorityReligion: Catholicism
        - DefenseStrength: 55
        - IsOccupied: true
        
        ### Oslo
        - ID: 9310
        - X: 72
        - Y: 29
        - Population: 12
        - DefenseStrength: 57
        - IsCoastal: true
        
        ### Jelling
        - ID: 9452
        - X: 9
        - Y: 13
        - Population: 11
        - MajorityReligion: Catholicism
        - DefenseStrength: 57
        - IsCoastal: true
        
        ### Tikal
        - ID: 9563
        - X: 55
        - Y: 28
        - Population: 16
        - MajorityReligion: Catholicism
        - DefenseStrength: 53
        - IsOccupied: true
        
        ### Lyon
        - ID: 10524
        - X: 53
        - Y: 16
        - Population: 17
        - MajorityReligion: Catholicism
        - DefenseStrength: 60
        - IsOccupied: true
        
        ### Satsuma
        - ID: 10698
        - X: 40
        - Y: 21
        - Population: 16
        - MajorityReligion: Catholicism
        - DefenseStrength: 59
        - IsOccupied: true
        
        ### Bergen
        - ID: 11431
        - X: 41
        - Y: 4
        - Population: 10
        - MajorityReligion: Catholicism
        - DefenseStrength: 58
        - IsCoastal: true
        
        ### Palenque
        - ID: 11754
        - X: 58
        - Y: 29
        - Population: 15
        - MajorityReligion: Catholicism
        - DefenseStrength: 56
        - IsOccupied: true
        - Wonders:
          - Hanging Gardens
        
        ### Chichen Itza
        - ID: 12105
        - X: 61
        - Y: 34
        - Population: 14
        - MajorityReligion: Catholicism
        - DefenseStrength: 58
        - IsPuppet: true
        - IsCoastal: true
        
        ### Bratislava
        - ID: 12384
        - X: 37
        - Y: 13
        - Population: 14
        - MajorityReligion: Catholicism
        - DefenseStrength: 34
        - Health: 50%
        - IsPuppet: true
        - IsCoastal: true
        - ResistanceTurns: 9
        
        ## Player: The Ottomans
        
        ### Istanbul
        - ID: 1058
        - X: 56
        - Y: 11
        - Population: 28
        - MajorityReligion: Catholicism
        - DefenseStrength: 65
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Himeji Castle
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Edirne
        - ID: 1268
        - X: 57
        - Y: 16
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 56
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Colossus
          - Scrivener's Office
        
        ### Ankara
        - ID: 1883
        - X: 61
        - Y: 22
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 56
        - IsCoastal: true
        
        ### Konya
        - ID: 2708
        - X: 66
        - Y: 19
        - Population: 17
        - MajorityReligion: Catholicism
        - DefenseStrength: 50
        - IsCoastal: true
        - Wonders:
          - Imperial College
        
        ### Samsun
        - ID: 2775
        - X: 54
        - Y: 8
        - Population: 15
        - MajorityReligion: Catholicism
        - DefenseStrength: 58
        - IsCoastal: true
        - Wonders:
          - Grand Temple
          - Printing Press
        
        ### Bursa
        - ID: 4000
        - X: 62
        - Y: 17
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 43
        - IsCoastal: true
        
        ### Gaziantep
        - ID: 7456
        - X: 74
        - Y: 20
        - Population: 14
        - MajorityReligion: Catholicism
        - DefenseStrength: 54
        - IsCoastal: true
        
        ### Diyarbakir
        - ID: 8477
        - X: 71
        - Y: 24
        - Population: 14
        - MajorityReligion: Catholicism
        - DefenseStrength: 42
        - IsCoastal: true
        
        ### Izmir
        - ID: 9627
        - X: 3
        - Y: 14
        - Population: 12
        - MajorityReligion: Islam
        - DefenseStrength: 56
        - IsCoastal: true
        
        ### Kayseri
        - ID: 10195
        - X: 3
        - Y: 9
        - Population: 10
        - MajorityReligion: Catholicism
        - DefenseStrength: 55
        - IsCoastal: true
        
        ### Malatya
        - ID: 10878
        - X: 4
        - Y: 20
        - Population: 10
        - MajorityReligion: Islam
        - DefenseStrength: 50
        - IsCoastal: true
        
        ### Marsin
        - ID: 11968
        - X: 7
        - Y: 19
        - Population: 7
        - MajorityReligion: Catholicism
        - DefenseStrength: 33
        - Health: 96%
        - IsCoastal: true
        
        ## Player: Babylon
        
        ### Babylon
        - ID: 1059
        - X: 18
        - Y: 46
        - Population: 31
        - MajorityReligion: Buddhism
        - DefenseStrength: 59
        - FoodStored: 1751
        - FoodPerTurn: 126
        - ProductionPerTurn: 238
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 572
        - SciencePerTurn: 445
        - CulturePerTurn: 344
        - FaithPerTurn: 122
        - TourismPerTurn: 162
        - HappinessDelta: 22
        - BuildingCount: 46
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
          - Coaling Station
          - Refinery
        - Wonders:
          - Heroic Epic
          - Circus Maximus
          - Ironworks
          - Great Library
          - Forbidden Palace
          - Brandenburg Gate
          - Scrivener's Office
          - Printing Press
          - Palace of Culture and Science
          - Summer Palace
          - Soho Foundry
          - Crystal Palace
          - Royal Guardhouse
          - Royal Astrologer
          - Grand Ossuary
          - Firaxite Materials Headquarters
        - GreatWorkCount: 8
        
        ### Akkad
        - ID: 1240
        - X: 19
        - Y: 41
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 53
        - FoodStored: 1103
        - FoodPerTurn: 4
        - ProductionPerTurn: 228
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 268
        - SciencePerTurn: 339
        - CulturePerTurn: 162
        - FaithPerTurn: 60
        - TourismPerTurn: 79.5
        - HappinessDelta: 16
        - BuildingCount: 46
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
          - Coaling Station
        - Wonders:
          - School of Philosophy
          - Chartered Company
          - Great Wall
          - Machu Picchu
          - Notre Dame
          - Porcelain Tower
          - Eiffel Tower
          - Neuschwanstein
          - Etemenanki
        - GreatWorkCount: 4
        
        ### Dur-Kurigalzu
        - ID: 1358
        - X: 14
        - Y: 41
        - Population: 21
        - MajorityReligion: Buddhism
        - DefenseStrength: 51
        - FoodStored: 944
        - FoodPerTurn: 2
        - ProductionStored: 732
        - ProductionPerTurn: 340
        - CurrentProduction: Diplomat
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 142
        - SciencePerTurn: 275
        - CulturePerTurn: 146
        - FaithPerTurn: 27
        - TourismPerTurn: 122.5
        - HappinessDelta: 13
        - BuildingCount: 45
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
          - Agribusiness
          - Coaling Station
          - Refinery
        - Wonders:
          - Imperial College
          - Uffizi
          - Nalanda
          - Empire State Building
        - GreatWorkCount: 7
        
        ### Nippur
        - ID: 1754
        - X: 15
        - Y: 36
        - Population: 19
        - MajorityReligion: Buddhism
        - DefenseStrength: 51
        - IsCoastal: true
        - FoodStored: 347
        - FoodPerTurn: 0
        - ProductionStored: 2118
        - ProductionPerTurn: 244
        - CurrentProduction: Cristo Redentor
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 174
        - SciencePerTurn: 175
        - CulturePerTurn: 69
        - FaithPerTurn: 18
        - TourismPerTurn: 50
        - HappinessDelta: 12
        - BuildingCount: 49
        - ImportantBuildings:
          - Seaport
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Writers' Guild
          - Hotel
          - Caravansary
          - Chancery
          - Bastion Fort
          - Agribusiness
          - Coaling Station
        - Wonders:
          - Globe Theatre
        - GreatWorkCount: 2
        
        ### Borsippa
        - ID: 2729
        - X: 8
        - Y: 43
        - Population: 23
        - MajorityReligion: Buddhism
        - DefenseStrength: 31
        - FoodStored: 1209
        - FoodPerTurn: 26
        - ProductionPerTurn: 213
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 141
        - SciencePerTurn: 264
        - CulturePerTurn: 97
        - FaithPerTurn: 30
        - TourismPerTurn: 44.5
        - HappinessDelta: 12
        - BuildingCount: 49
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Artists' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
          - Agribusiness
          - Coaling Station
          - Refinery
        - Wonders:
          - Royal Collection
        - GreatWorkCount: 1
        
        ### Sippar
        - ID: 2994
        - X: 5
        - Y: 39
        - Population: 25
        - MajorityReligion: Buddhism
        - DefenseStrength: 53
        - FoodStored: 999
        - FoodPerTurn: 24
        - ProductionPerTurn: 191
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 159
        - SciencePerTurn: 244
        - CulturePerTurn: 82
        - FaithPerTurn: 39
        - TourismPerTurn: 30.75
        - HappinessDelta: 12
        - BuildingCount: 48
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
          - Coaling Station
        - Wonders:
          - Chichen Itza
          - Taj Mahal
          - Grand Temple
        - GreatWorkCount: 0
        
        ### Hippo Regius
        - ID: 4624
        - X: 10
        - Y: 37
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 52
        - IsOccupied: true
        - FoodStored: 893
        - FoodPerTurn: 17
        - ProductionPerTurn: 218
        - CurrentProduction: Infinite Project: Research
        - GoldPerTurn: 108
        - SciencePerTurn: 240
        - CulturePerTurn: 71
        - FaithPerTurn: 19
        - TourismPerTurn: 25.5
        - HappinessDelta: 14
        - BuildingCount: 49
        - ImportantBuildings:
          - Courthouse
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Writers' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Bastion Fort
          - Coaling Station
        - GreatWorkCount: 0
        
        ### Opis
        - ID: 9415
        - X: 1
        - Y: 40
        - Population: 15
        - MajorityReligion: Buddhism
        - DefenseStrength: 50
        - IsCoastal: true
        - FoodStored: 417
        - FoodPerTurn: 26
        - ProductionStored: 0
        - ProductionPerTurn: 303
        - CurrentProduction: Research Lab
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 63
        - SciencePerTurn: 145
        - CulturePerTurn: 35
        - FaithPerTurn: 15
        - TourismPerTurn: 11.25
        - HappinessDelta: 13
        - BuildingCount: 44
        - ImportantBuildings:
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Harbor
          - Zoo
          - Temple
          - Broadcast Tower
          - Military Academy
          - Hospital
          - Factory
          - Stock Exchange
          - Public School
          - Constabulary
          - Musicians' Guild
          - Caravansary
          - Chancery
          - Gallery
          - Bastion Fort
        - GreatWorkCount: 0
        
        ### Faeroerne
        - ID: 12086
        - X: 16
        - Y: 21
        - Population: 6
        - DefenseStrength: 40
        - Health: 37%
        - IsOccupied: true
        - IsCoastal: true
        - FoodStored: 68
        - FoodPerTurn: 4
        - ProductionStored: 0
        - ProductionPerTurn: 52
        - CurrentProduction: Bastion Fort
        - ProductionTurnsLeft: 8
        - GoldPerTurn: 19
        - SciencePerTurn: 25
        - CulturePerTurn: 7
        - FaithPerTurn: 7
        - TourismPerTurn: 1.5
        - HappinessDelta: 0
        - BuildingCount: 17
        - ImportantBuildings:
          - Courthouse
          - Windmill
          - Harbor
          - Arena
          - Temple
          - Castle
          - Workshop
          - Market
          - Library
          - Aqueduct
          - Amphitheater
        - GreatWorkCount: 0
        
        ## Player: Carthage
        
        ### Carthage
        - ID: 1060
        - X: 12
        - Y: 32
        - Population: 28
        - MajorityReligion: Islam
        - DefenseStrength: 57
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - National Monument
          - Great Lighthouse
          - Angkor Wat
          - Hagia Sophia
          - University of Sankore
          - Printing Press
          - Great Cothon
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Celestial Throne
        
        ### Utique
        - ID: 1296
        - X: 8
        - Y: 29
        - Population: 22
        - MajorityReligion: Islam
        - DefenseStrength: 49
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
          - Grand Temple
          - Scrivener's Office
        
        ### Gades
        - ID: 2242
        - X: 12
        - Y: 25
        - Population: 22
        - MajorityReligion: Islam
        - DefenseStrength: 52
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Royal Collection
        
        ### Saguntum
        - ID: 2810
        - X: 6
        - Y: 33
        - Population: 23
        - MajorityReligion: Islam
        - DefenseStrength: 51
        - IsCoastal: true
        - Wonders:
          - Ironworks
          - Imperial College
        
        ### Carthago Nova
        - ID: 3267
        - X: 2
        - Y: 34
        - Population: 22
        - MajorityReligion: Islam
        - DefenseStrength: 49
        - IsCoastal: true
        - Wonders:
          - Sistine Chapel
        
        ### Truso
        - ID: 11326
        - X: 71
        - Y: 34
        - Population: 10
        - MajorityReligion: Islam
        - DefenseStrength: 45
        - Health: 88%
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: City-States
        
        ### Aksum
        - ID: 1063
        - X: 48
        - Y: 4
        - Population: 15
        - MajorityReligion: Catholicism
        - DefenseStrength: 65
        - IsCoastal: true
        
        ### Marrakech
        - ID: 1064
        - X: 54
        - Y: 4
        - Population: 17
        - MajorityReligion: Catholicism
        - DefenseStrength: 66
        - IsCoastal: true
        
        ### Buenos Aires
        - ID: 10828
        - X: 38
        - Y: 24
        - Population: 14
        - MajorityReligion: Catholicism
        - DefenseStrength: 67
        
        ### Samarkand
        - ID: 1066
        - X: 49
        - Y: 31
        - Population: 17
        - MajorityReligion: Catholicism
        - DefenseStrength: 64
        - IsCoastal: true
        
        ### Bunkeya
        - ID: 1067
        - X: 64
        - Y: 27
        - Population: 18
        - DefenseStrength: 69
        - IsCoastal: true
        
        ### Shedet
        - ID: 1068
        - X: 19
        - Y: 33
        - Population: 17
        - MajorityReligion: Buddhism
        - DefenseStrength: 69
        
        ### Trowulan
        - ID: 1069
        - X: 24
        - Y: 37
        - Population: 17
        - MajorityReligion: Buddhism
        - DefenseStrength: 66
        - IsCoastal: true
        
        ### Sofia
        - ID: 1070
        - X: 3
        - Y: 45
        - Population: 18
        - MajorityReligion: Buddhism
        - DefenseStrength: 66
        - IsCoastal: true
        
        ### Kwa-Bulawayo
        - ID: 1071
        - X: 29
        - Y: 47
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 64
        - IsCoastal: true
        
        ### Stockholm
        - ID: 1072
        - X: 33
        - Y: 4
        - Population: 20
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Kuala Lumpur
        - ID: 1073
        - X: 3
        - Y: 4
        - Population: 20
        - DefenseStrength: 65
        - IsCoastal: true
        
        ### Luba
        - ID: 1074
        - X: 8
        - Y: 8
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 65
        - IsCoastal: true
        
        ### Dorestad
        - ID: 1075
        - X: 25
        - Y: 43
        - Population: 18
        - MajorityReligion: Buddhism
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Ouagadougou
        - ID: 1076
        - X: 10
        - Y: 22
        - Population: 12
        - MajorityReligion: Islam
        - DefenseStrength: 67
        - IsCoastal: true
        
        ### Huari
        - ID: 1078
        - X: 48
        - Y: 37
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 57
        - IsCoastal: true
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - Attack:
          - Foreign Legion:
            - Strength: 40
        - CityBombard:
          - Field Gun:
            - Strength: 17
            - RangedStrength: 40
        - FastAttack:
          - Lancer:
            - Strength: 37
          - Commando:
            - Strength: 32
          - Qizilbash:
            - Strength: 41
        - Defense:
          - Fusilier:
            - Strength: 38
          - Tercio:
            - Strength: 25
        - Ranged:
          - Cavalry:
            - Strength: 40
            - RangedStrength: 31
          - Musketman:
            - Strength: 21
            - RangedStrength: 30
          - Gatling Gun:
            - Strength: 32
            - RangedStrength: 44
        - AttackSea:
          - Destroyer:
            - Strength: 70
          - Ironclad:
            - Strength: 55
          - Corvette:
            - Strength: 40
        - AssaultSea:
          - Frigate:
            - Strength: 25
            - RangedStrength: 35
          - Cruiser:
            - Strength: 40
            - RangedStrength: 55
          - Attack Submarine:
            - Strength: 50
            - RangedStrength: 72
        
        ## Friendly Land Zone 1059
        - ZoneValue: 66
        - Dominance: Friendly
        - FriendlyStrength: 2256
        - City: Babylon
        - AreaID: 46
        - Plots: 53
        - CenterX: 18
        - CenterY: 47
        - Units:
          - Babylon:
            - Cavalry: 1
            - Fusilier: 4
            - Gatling Gun: 4
            - Field Gun: 3
        - Neighbors:
          - 1358
          - 100008
          - 1240
          - 1075
          - 100009
        
        ## Neutral Land Zone 1060
        - ZoneValue: 96
        - Dominance: Friendly
        - NeutralStrength: 57
        - FriendlyStrength: 2052
        - City: Carthage
        - AreaID: 46
        - Plots: 20
        - CenterX: 12
        - CenterY: 32
        - Units:
          - Carthage:
            - Musketman: 6
            - Field Gun: 1
            - Commando: 1
        - Neighbors:
          - 2810
          - 4624
          - 1754
          - 2242
          - -1068
        
        ## Neutral Land Zone 1068
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 69
        - FriendlyStrength: 1795
        - City: Shedet
        - AreaID: 67
        - Plots: 21
        - CenterX: 19
        - CenterY: 35
        - Units:
          - City-State Shedet:
            - Cavalry: 2
            - Fusilier: 3
            - Gatling Gun: 3
        - Neighbors:
          - -1068
          - 1754
          - 1240
          - 1069
          - -1069
        
        ## Neutral Land Zone 1069
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 66
        - FriendlyStrength: 1469
        - City: Trowulan
        - AreaID: 67
        - Plots: 17
        - CenterX: 23
        - CenterY: 38
        - Units:
          - City-State Trowulan:
            - Fusilier: 3
            - Gatling Gun: 2
          - City-State Dorestad:
            - Tercio: 1
          - Babylon:
            - Fusilier: 1
        - Neighbors:
          - 1068
          - 1240
          - -1069
          - 1075
          - -1075
        
        ## Neutral Land Zone 1070
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 66
        - FriendlyStrength: 1929
        - City: Sofia
        - AreaID: 71
        - Plots: 27
        - CenterX: 4
        - CenterY: 46
        - Units:
          - City-State Sofia:
            - Fusilier: 3
            - Gatling Gun: 2
          - Babylon:
            - Fusilier: 3
            - Gatling Gun: 1
        - Neighbors:
          - -100000
          - -1070
          - 2994
          - 2729
          - 100008
        
        ## Neutral Land Zone 1071
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 64
        - FriendlyStrength: 948
        - City: Kwa-Bulawayo
        - AreaID: 96
        - Plots: 11
        - CenterX: 30
        - CenterY: 47
        - Units:
          - Barbarians:
            - Tercio: 1
          - City-State Kwa-Bulawayo:
            - Fusilier: 1
            - Lancer: 1
            - Gatling Gun: 3
        - Neighbors:
          - -1071
        
        ## Neutral Land Zone 1075
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 71
        - FriendlyStrength: 1344
        - City: Dorestad
        - AreaID: 46
        - Plots: 21
        - CenterX: 23
        - CenterY: 44
        - Units:
          - City-State Dorestad:
            - Fusilier: 2
            - Lancer: 1
            - Gatling Gun: 1
          - Babylon:
            - Fusilier: 2
        - Neighbors:
          - 1240
          - 1059
          - 1069
          - -1075
          - 100009
        
        ## Neutral Land Zone 1076
        - ZoneValue: 24
        - Dominance: Even
        - Posture: Attrition
        - EnemyStrength: 660
        - NeutralStrength: 68
        - FriendlyStrength: 486
        - City: Ouagadougou
        - AreaID: 8
        - Plots: 13
        - CenterX: 10
        - CenterY: 22
        - Units:
          - City-State Ouagadougou:
            - Fusilier: 1
          - Denmark:
            - Qizilbash: 1
        - Neighbors:
          - -1076
          - 11968
          - 8023
          - -2242
          - -12086
          - 12086
        
        ## Friendly Land Zone 1240
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 2569
        - City: Akkad
        - AreaID: 46
        - Plots: 32
        - CenterX: 20
        - CenterY: 41
        - Units:
          - Babylon:
            - Cavalry: 2
            - Gatling Gun: 2
            - Commando: 1
        - Neighbors:
          - 1754
          - 1358
          - 1059
          - 1068
          - 1069
          - 1075
        
        ## Friendly Land Zone 1358
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 1835
        - City: Dur-Kurigalzu
        - AreaID: 46
        - Plots: 33
        - CenterX: 14
        - CenterY: 42
        - Units:
          - Babylon:
            - Field Gun: 2
        - Neighbors:
          - 2729
          - 4624
          - 100008
          - 1059
          - 1754
          - 1240
        
        ## Friendly Land Zone 1754
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 1975
        - City: Nippur
        - AreaID: 46
        - Plots: 20
        - CenterX: 15
        - CenterY: 36
        - Units:
          - Babylon:
            - Fusilier: 1
            - Gatling Gun: 1
            - Commando: 1
        - Neighbors:
          - 4624
          - 1060
          - 1358
          - 1240
          - 1068
        
        ## Neutral Land Zone 2242
        - ZoneValue: 18
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 105
        - NeutralStrength: 52
        - FriendlyStrength: 803
        - City: Gades
        - AreaID: 46
        - Plots: 17
        - CenterX: 13
        - CenterY: 26
        - Units:
          - Carthage:
            - Commando: 1
        - Neighbors:
          - -1076
          - -2242
          - 1060
          - -12086
          - 12086
          - -100000
          - -1068
        
        ## Friendly Land Zone 2729
        - ZoneValue: 48
        - Dominance: Friendly
        - FriendlyStrength: 1471
        - City: Borsippa
        - AreaID: 46
        - Plots: 40
        - CenterX: 9
        - CenterY: 44
        - Units:
          - Babylon:
            - Cavalry: 1
            - Fusilier: 1
            - Gatling Gun: 2
        - Neighbors:
          - 1070
          - 2994
          - 100008
          - 4624
          - 1358
        
        ## Neutral Land Zone 2810
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 51
        - FriendlyStrength: 1943
        - City: Saguntum
        - AreaID: 62
        - Plots: 20
        - CenterX: 7
        - CenterY: 33
        - Units:
          - Carthage:
            - Lancer: 1
            - Musketman: 1
            - Commando: 1
          - Babylon:
            - Fusilier: 1
        - Neighbors:
          - 3267
          - 2994
          - 4624
          - 1060
        
        ## Friendly Land Zone 2994
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 2425
        - City: Sippar
        - AreaID: 53
        - Plots: 21
        - CenterX: 5
        - CenterY: 39
        - Units:
          - Babylon:
            - Field Gun: 1
        - Neighbors:
          - 9415
          - 3267
          - -9415
          - 1070
          - 2810
          - 4624
          - 2729
        
        ## Neutral Land Zone 3267
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 49
        - FriendlyStrength: 1788
        - City: Carthago Nova
        - AreaID: 66
        - Plots: 19
        - CenterX: 1
        - CenterY: 35
        - Units:
          - Carthage:
            - Lancer: 1
            - Field Gun: 1
        - Neighbors:
          - 9415
          - 2994
          - 2810
        
        ## Friendly Land Zone 4624
        - ZoneValue: 42
        - Dominance: Friendly
        - FriendlyStrength: 2208
        - City: Hippo Regius
        - AreaID: 46
        - Plots: 22
        - CenterX: 10
        - CenterY: 38
        - Units:
          - Babylon:
            - Fusilier: 1
            - Gatling Gun: 1
            - Commando: 1
        - Neighbors:
          - 2994
          - 2810
          - 2729
          - 1060
          - 1754
          - 1358
        
        ## Enemy Land Zone 6010
        - ZoneValue: 30
        - Dominance: Enemy
        - EnemyStrength: 893
        - City: Tunsberg
        - AreaID: 7
        - Plots: 11
        - CenterX: 44
        - CenterY: 14
        - Units:
          - Denmark:
            - Fusilier: 1
        
        ## Enemy Land Zone 8023
        - ZoneValue: 60
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 1182
        - FriendlyStrength: 316
        - City: Roskilde
        - AreaID: 8
        - Plots: 18
        - CenterX: 12
        - CenterY: 16
        - Units:
          - Denmark:
            - Foreign Legion: 1
        - Neighbors:
          - 11968
          - 1076
          - -1076
          - -8023
          - 8134
          - -12086
        
        ## Enemy Land Zone 8134
        - ZoneValue: 3
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 745
        - FriendlyStrength: 128
        - City: Hedeby
        - AreaID: 16
        - Plots: 13
        - CenterX: 14
        - CenterY: 11
        - Units:
          - Barbarians:
            - Fusilier: 1
          - Denmark:
            - Gatling Gun: 1
        - Neighbors:
          - 8023
          - -8023
          - -100000
        
        ## Enemy Land Zone 8412
        - ZoneValue: 36
        - Dominance: Enemy
        - EnemyStrength: 1845
        - City: Sparta
        - AreaID: 7
        - Plots: 27
        - CenterX: 49
        - CenterY: 19
        - Units:
          - Denmark:
            - Cavalry: 1
        - Neighbors:
          - 9017
        
        ## Enemy Land Zone 9017
        - ZoneValue: 30
        - Dominance: Enemy
        - EnemyStrength: 2151
        - City: Athens
        - AreaID: 7
        - Plots: 36
        - CenterX: 54
        - CenterY: 23
        - Units:
          - Denmark:
            - Lancer: 1
        - Neighbors:
          - 8412
        
        ## Enemy Land Zone 9310
        - ZoneValue: 96
        - Dominance: Even
        - Posture: Attrition
        - EnemyStrength: 425
        - FriendlyStrength: 279
        - City: Oslo
        - AreaID: 31
        - Plots: 23
        - CenterX: 72
        - CenterY: 29
        - Units:
          - Denmark:
            - Foreign Legion: 1
            - Fusilier: 1
        - Neighbors:
          - -9310
        
        ## Friendly Land Zone 9415
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 1865
        - City: Opis
        - AreaID: 84
        - Plots: 25
        - CenterX: 79
        - CenterY: 39
        - Units:
          - Babylon:
            - Cavalry: 2
            - Fusilier: 3
            - Field Gun: 2
        - Neighbors:
          - 3267
          - -9415
          - 2994
          - -1070
        
        ## Neutral Land Zone 11968
        - ZoneValue: 9
        - Dominance: Enemy
        - Posture: Attrition
        - EnemyStrength: 797
        - NeutralStrength: 32
        - FriendlyStrength: 254
        - City: Marsin
        - AreaID: 8
        - Plots: 19
        - CenterX: 7
        - CenterY: 18
        - Units:
          - Denmark:
            - Foreign Legion: 1
        - Neighbors:
          - 8023
          - 1076
        
        ## Friendly Land Zone 12086
        - ZoneValue: 12
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 420
        - FriendlyStrength: 459
        - City: Faeroerne
        - AreaID: 29
        - Plots: 9
        - CenterX: 16
        - CenterY: 21
        - Units:
          - Babylon:
            - Destroyer: 1
            - Fusilier: 1
        - Neighbors:
          - 1076
          - -12086
          - 2242
          - -8023
          - -2242
          - -100000
        
        ## Neutral Land Zone 100008
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 99
        - AreaID: 46
        - Plots: 18
        - CenterX: 11
        - CenterY: 49
        - Units:
          - Babylon:
            - Fusilier: 1
        - Neighbors:
          - 1070
          - -1070
          - 2729
          - 1358
          - 1059
        
        ## Neutral Land Zone 100009
        - ZoneValue: 3
        - AreaID: 46
        - Plots: 4
        - CenterX: 22
        - CenterY: 50
        - Units:
          - Barbarians:
            - Gatling Gun: 1
        - Neighbors:
          - 1059
          - 1075
        
        ## Neutral Sea Zone -1069
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 66
        - FriendlyStrength: 918
        - City: Trowulan
        - AreaID: 0
        - Plots: 39
        - CenterX: 26
        - CenterY: 36
        - Units:
          - City-State Trowulan:
            - Ironclad: 2
        - Neighbors:
          - 1068
          - 1069
          - -1068
          - -100000
          - -1075
        
        ## Enemy Sea Zone -8023
        - ZoneValue: 4
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 617
        - FriendlyStrength: 365
        - City: Roskilde
        - AreaID: 0
        - Plots: 12
        - CenterX: 14
        - CenterY: 17
        - Units:
          - Carthage:
            - Frigate: 2
          - Denmark:
            - Frigate: 1
        - Neighbors:
          - 8023
          - -1076
          - -12086
          - 8134
          - 12086
        
        ## Neutral Sea Zone -11326
        - ZoneValue: 4
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 582
        - NeutralStrength: 40
        - FriendlyStrength: 276
        - City: Truso
        - AreaID: 0
        - Plots: 48
        - CenterX: 70
        - CenterY: 36
        - Units:
          - Babylon:
            - Destroyer: 1
          - Denmark:
            - Ironclad: 2
        - Neighbors:
          - -100000
          - -9310
        
        ## Neutral Sea Zone -2242
        - ZoneValue: 1
        - Dominance: Friendly
        - Posture: Exploit Flanks
        - EnemyStrength: 157
        - NeutralStrength: 52
        - FriendlyStrength: 738
        - City: Gades
        - AreaID: 43
        - Plots: 18
        - CenterX: 13
        - CenterY: 26
        - Units:
          - Carthage:
            - Musketman: 1
        - Neighbors:
          - -1076
          - 2242
          - 1076
          - -12086
          - 12086
          - -1068
        
        ## Friendly Sea Zone -12086
        - ZoneValue: 144
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 769
        - FriendlyStrength: 535
        - City: Faeroerne
        - AreaID: 0
        - Plots: 54
        - CenterX: 18
        - CenterY: 21
        - Units:
          - Carthage:
            - Corvette: 1
          - Denmark:
            - Ironclad: 1
          - Babylon:
            - Fusilier: 1
        - Neighbors:
          - -1076
          - -8023
          - 1076
          - -2242
          - 12086
          - 2242
          - 8023
          - -100000
        
        ## Neutral Sea Zone -1071
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 64
        - FriendlyStrength: 1025
        - City: Kwa-Bulawayo
        - AreaID: 0
        - Plots: 66
        - CenterX: 30
        - CenterY: 47
        - Units:
          - City-State Kwa-Bulawayo:
            - Ironclad: 1
            - Cruiser: 1
        - Neighbors:
          - -1075
          - 1071
          - -100000
        
        ## Neutral Sea Zone -1075
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 71
        - FriendlyStrength: 900
        - City: Dorestad
        - AreaID: 0
        - Plots: 23
        - CenterX: 27
        - CenterY: 43
        - Units:
          - City-State Dorestad:
            - Ironclad: 3
        - Neighbors:
          - 1075
          - -1071
          - 1069
          - -1069
          - -100000
        
        ## Friendly Sea Zone -9415
        - ZoneValue: 1
        - Dominance: Friendly
        - FriendlyStrength: 1220
        - City: Opis
        - AreaID: 0
        - Plots: 25
        - CenterX: 78
        - CenterY: 41
        - Units:
          - Babylon:
            - Attack Submarine: 1
        - Neighbors:
          - 9415
          - -1070
          - 2994
          - -100000
        
        ## Neutral Sea Zone -1070
        - ZoneValue: 10
        - Dominance: Friendly
        - NeutralStrength: 66
        - FriendlyStrength: 1229
        - City: Sofia
        - AreaID: 0
        - Plots: 34
        - CenterX: 2
        - CenterY: 47
        - Units:
          - City-State Sofia:
            - Ironclad: 2
        - Neighbors:
          - -9415
          - -100000
          - 1070
          - 9415
          - 100008
        
        ## Neutral Sea Zone -1068
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 69
        - FriendlyStrength: 814
        - City: Shedet
        - AreaID: 0
        - Plots: 43
        - CenterX: 19
        - CenterY: 31
        - Units:
          - Carthage:
            - Fusilier: 1
        - Neighbors:
          - -2242
          - 1060
          - 2242
          - -100000
          - 1068
          - -1069
        
        ## Neutral Sea Zone -1076
        - ZoneValue: 1
        - Dominance: Friendly
        - Posture: Exploit Flanks
        - EnemyStrength: 157
        - NeutralStrength: 68
        - FriendlyStrength: 567
        - City: Ouagadougou
        - AreaID: 32
        - Plots: 16
        - CenterX: 9
        - CenterY: 23
        - Units:
          - City-State Ouagadougou:
            - Ironclad: 2
        - Neighbors:
          - 1076
          - -2242
          - 8023
          - 2242
          - -8023
          - -12086
        
        ## Neutral Sea Zone -100000
        - ZoneValue: 1
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 163
        - FriendlyStrength: 126
        - AreaID: 0
        - Plots: 1017
        - CenterX: 41
        - CenterY: 32
        - Units:
          - Babylon:
            - Fusilier: 1
        - Neighbors:
          - -1070
          - 1070
          - 2242
          - 8134
          - -12086
          - -1068
          - 12086
          - -1069
          - -1075
          - -1071
          - -11326
          - -9415
        
        ## Enemy Sea Zone -9310
        - ZoneValue: 4
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 481
        - FriendlyStrength: 514
        - City: Oslo
        - AreaID: 0
        - Plots: 25
        - CenterX: 75
        - CenterY: 29
        - Units:
          - Carthage:
            - Corvette: 1
          - Babylon:
            - Destroyer: 1
        - Neighbors:
          - 9310
          - -11326
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 306
        
        ### 0
        - Type: DealMade
        - StartTurn: 306
        - TradedItems:
          - #0:
            - Data1: 43
            - Data2: 0
            - Data3: 0
            - Duration: 0
            - FromPlayer: 1
            - Item: Techs
          - #1:
            - Data1: 3543
            - Data2: 0
            - Data3: 0
            - Duration: 0
            - FromPlayer: 4
            - Item: Gold
        - ToPlayer: 1: The Ottomans
        - FromPlayer: 4: Carthage
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Missionary
          - ID: 12371
        - Player: 4: Carthage
        - Plains Land 12,32:
          - Owner: Carthage
          - CityID: 1060
          - Population: 27
          - IsRiver: true
          - City: Carthage
          - Religion: Islam
          - Route: Railroad
        
        ### 2
        - Type: UnitCreated
        - UnitType: Missionary
        - Player: 4: Carthage
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 12371
        - Plains Land 12,32:
          - Owner: Carthage
          - CityID: 1060
          - Population: 27
          - IsRiver: true
          - City: Carthage
          - Religion: Islam
          - Route: Railroad
        
        ### 3
        - Type: CityTrained
        - WithFaith: true
        - Player: 4: Carthage
        - City:
          - Name: Carthage
          - Population: 27
          - ID: 1060
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 12371
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Musketman
          - ID: 12372
        - Player: 4: Carthage
        - Plains Land 11,32:
          - Owner: Carthage
          - IsRiver: true
          - Resource: Deer
          - Improvement: Manufactory
        
        ### 5
        - Type: UnitCreated
        - UnitType: Musketman
        - Player: 4: Carthage
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Musketman
          - ID: 12372
        - Plains Land 11,32:
          - Owner: Carthage
          - IsRiver: true
          - Resource: Deer
          - Improvement: Manufactory
        
        ### 6
        - Type: CityTrained
        - Player: 4: Carthage
        - City:
          - Name: Carthage
          - Population: 27
          - ID: 1060
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Musketman
          - ID: 12372
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 11277
        - Player: 4: Carthage
        - Plots:
          - Coast 16,34:
            - Owner: Babylon
          - Ocean 16,33:
            - Owner: Carthage
          - Coast 16,32:
            - Owner: Carthage
          - Coast 16,31:
            - Owner: Carthage
            - Feature: Atoll
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 12304
        - Player: 4: Carthage
        - Plots:
          - Grass Hills 11,25:
            - Owner: Carthage
            - Improvement: Fort
          - Coast 10,25:
            - Owner: Carthage
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 12130
        - Player: 4: Carthage
        - Plots:
          - Coast 10,25:
            - Owner: Carthage
          - Grass Hills 11,25:
            - Owner: Carthage
            - Improvement: Fort
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 11489
        - Player: 4: Carthage
        - Plots:
          - Coast 7,24:
            - Owner: Carthage
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11327
        - Player: 4: Carthage
        - Plots:
          - Grass Land 11,33:
            - Owner: Carthage
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Grass Hills 10,33:
            - Owner: Carthage
            - IsRiver: true
            - Resource: Copper
            - Improvement: Manufactory
            - Route: Road
          - Plains Land 9,33:
            - Owner: Carthage
            - Improvement: Village
            - Route: Road
          - Plains Land 8,33:
            - Owner: Carthage
            - Resource: Wheat
            - Improvement: Citadel
            - Route: Road
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 12263
        - Player: 4: Carthage
        - Plots:
          - Coast 7,21:
            - Owner: The Ottomans
          - Coast 8,22:
            - Owner: City-State Ouagadougou
          - Coast 7,23:
            - Owner: City-State Ouagadougou
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 7,24:
            - Owner: Carthage
        
        ### 13
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Musketman
          - ID: 12372
        - Player: 4: Carthage
        - Promotions:
          - Barrage I
          - Barrage II
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 14%
          - AI: AssaultSea
          - Unit: Frigate
          - ID: 10422
        - Player: 4: Carthage
        - Plots:
          - Coast 14,21:
            - Owner: Carthage
          - Coast 15,22:
            - Owner: Carthage
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 73%
          - AI: AssaultSea
          - Unit: Frigate
          - ID: 11135
        - Player: 4: Carthage
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 60%
          - AI: AssaultSea
          - Unit: Frigate
          - ID: 11140
        - Player: 4: Carthage
        
        ### 17
        - Type: CombatResult
        - Coast 14,19:
          - Owner: Babylon
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 42
          - Player: 0: Denmark
          - Unit:
            - Level: 3
            - Health: 87%
            - AI: AssaultSea
            - Unit: Frigate
            - ID: 11929
        
        ### 18
        - Type: CombatResult
        - Coast 14,19:
          - Owner: Babylon
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 25
          - Damage: 67
          - Player: 0: Denmark
          - Unit:
            - Level: 3
            - Health: 57%
            - AI: AssaultSea
            - Unit: Frigate
            - ID: 11929
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 43%
          - AI: AttackSea
          - Unit: Corvette
          - ID: 10676
        - Player: 4: Carthage
        - Plots:
          - Coast 14,18:
            - Owner: Denmark
          - Coast 13,19:
            - Owner: Denmark
          - Coast 14,20:
            - Owner: Carthage
          - Coast 15,20:
            - Owner: Carthage
        
        ### 20
        - Type: CombatResult
        - Coast 14,19:
          - Owner: Babylon
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 23
          - Damage: 90
          - Player: 0: Denmark
          - Unit:
            - Level: 3
            - Health: 33%
            - AI: AssaultSea
            - Unit: Frigate
            - ID: 11929
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 79%
          - AI: AttackSea
          - Unit: Corvette
          - ID: 12041
        - Player: 4: Carthage
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 73%
          - AI: AttackSea
          - Unit: Corvette
          - ID: 11213
        - Player: 4: Carthage
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Prophet
          - Unit: Great Prophet
          - ID: 12342
        - Player: 4: Carthage
        - Plots:
          - Grass Land 11,33:
            - Owner: Carthage
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Plains Hills 12,34:
            - Owner: Carthage
            - Resource: Copper
            - Improvement: Mine
            - Route: Road
        
        ### 24
        - Type: TileImprovementChanged
        - Owner: 4: Carthage
        - OldImprovement: Mine
        - Plains Hills 12,34:
          - Owner: Carthage
          - Resource: Copper
          - Route: Road
        
        ### 25
        - Type: TileImprovementChanged
        - Owner: 4: Carthage
        - NewImprovement: Holy Site
        - Plains Hills 12,34:
          - Owner: Carthage
          - Resource: Copper
          - Improvement: Holy Site
          - Route: Road
        
        ### 26
        - Type: BuildFinished
        - Player: 4: Carthage
        - Improvement: Holy Site
        - Plains Hills 12,34:
          - Owner: Carthage
          - Resource: Copper
          - Improvement: Holy Site
          - Route: Road
        
        ### 27
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 4: Carthage
        - Unit:
          - Level: 1
          - AI: Prophet
          - Unit: Great Prophet
          - ID: 12342
        - Build: Construct a Holy Site
        - Plains Hills 12,34:
          - Owner: Carthage
          - Resource: Copper
          - Improvement: Holy Site
          - Route: Road
        
        ### 28
        - Type: GreatPersonExpended
        - Player: 4: Carthage
        - City:
          - Owner: Carthage
          - Terrain: Plains
          - Resource: Copper
          - Improvement: Holy Site
          - Route: Road
          - Plot: Hills
          - X: 12
          - Y: 34
        - Unit:
          - Level: 1
          - AI: Prophet
          - Unit: Great Prophet
          - ID: 12342
        - GreatPerson: 114
        
        ### 29
        - Type: UnitBuildStart
        - Owner: 4: Carthage
        - Unit:
          - Level: 1
          - AI: Prophet
          - Unit: Great Prophet
          - ID: 12342
        - Build: Construct a Holy Site
        - Plains Hills 12,34:
          - Owner: Carthage
          - Resource: Copper
          - Improvement: Holy Site
          - Route: Road
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 2313
        - Player: 4: Carthage
        - Grass Hills 11,25:
          - Owner: Carthage
          - Improvement: Fort
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 10675
        - Player: 4: Carthage
        - Grass Hills 14,22:
          - Owner: Carthage
          - Feature: Jungle
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 11092
        - Player: 4: Carthage
        - Plots:
          - Plains Land 10,20:
            - Owner: City-State Ouagadougou
            - Improvement: Farm
          - Plains Land 9,20:
            - Owner: City-State Ouagadougou
            - Improvement: Embassy
          - Grass Hills 8,19:
            - Owner: The Ottomans
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Diplomat
          - ID: 12375
        - Player: 4: Carthage
        - Desert Hills 14,31:
          - Owner: Carthage
        
        ### 34
        - Type: UnitCreated
        - UnitType: Diplomat
        - Player: 4: Carthage
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 12375
        - Desert Hills 14,31:
          - Owner: Carthage
        
        ### 35
        - Type: UnitUpgraded
        - Player: 4: Carthage
        - OldUnit:
          - Level: 1
          - AI: Messenger
          - Unit: Envoy
          - ID: 12162
        - NewUnit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 12375
        
        ### 36
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 4: Carthage
        - OriginalUnit:
          - Level: 1
          - AI: Messenger
          - Unit: Envoy
          - ID: 12162
        - NewOwner: 4: Carthage
        - ConvertingUnit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 12375
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 12093
        - Player: 4: Carthage
        - Plots:
          - Desert Land 19,32:
            - Owner: City-State Shedet
            - Feature: Oasis
          - Coast 18,31:
            - Owner: City-State Shedet
            - Feature: Atoll
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: FastAttack
          - Unit: Lancer
          - ID: 12337
        - Player: 4: Carthage
        - Plots:
          - Plains Land 8,33:
            - Owner: Carthage
            - Resource: Wheat
            - Improvement: Citadel
            - Route: Road
          - Plains Land 9,32:
            - Owner: Carthage
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Envoy
          - ID: 12262
        - Player: 4: Carthage
        - Plots:
          - Plains Hills 19,33:
            - Owner: City-State Shedet
            - CityID: 1068
            - Population: 17
            - City: Shedet
            - Religion: Buddhism
            - Route: Railroad
          - Grass Hills 20,33:
            - Owner: City-State Shedet
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Road
            - Feature: Forest
          - Plains Land 21,34:
            - Owner: City-State Shedet
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Grass Land 21,35:
            - Owner: City-State Shedet
            - IsRiver: true
            - Route: Road
            - Feature: Forest
          - Plains Hills 21,36:
            - IsRiver: true
            - Route: Road
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Envoy
          - ID: 12344
        - Player: 4: Carthage
        - Plots:
          - Coast 16,30:
            - Owner: Carthage
          - Coast 16,31:
            - Owner: Carthage
            - Feature: Atoll
          - Ocean 17,32:
            - Owner: Carthage
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: FastAttack
          - Unit: Lancer
          - ID: 11839
        - Player: 4: Carthage
        - Grass Land 1,36:
          - Owner: Carthage
          - Improvement: Farm
          - Route: Road
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: FastAttack
          - Unit: Commando
          - ID: 11142
        - Player: 4: Carthage
        - Grass Hills 12,24:
          - Owner: Carthage
          - Improvement: Mine
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Musketman
          - ID: 11531
        - Player: 4: Carthage
        - Coast 10,25:
          - Owner: Carthage
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: FastAttack
          - Unit: Lancer
          - ID: 10488
        - Player: 26
        - Grass Land 63,27:
          - Owner: Denmark
          - Improvement: Village
          - Route: Road
        
        ### 45
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1351
        - Owner: 27
        - Build: Construct a Lumber Mill
        - Grass Land 21,35:
          - Owner: City-State Shedet
          - IsRiver: true
          - Route: Road
          - Feature: Forest
        
        ### 46
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 11537
        - Player: 27
        - Grass Land 20,36:
          - Owner: City-State Shedet
          - IsRiver: true
          - Improvement: Lumber Mill
          - Feature: Forest
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5150
        - Player: 28
        - Grass Land 23,36:
          - Owner: City-State Trowulan
          - Improvement: Embassy
        
        ### 48
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 5150
        - Owner: 28
        - Build: Construct a Road
        - Grass Land 23,36:
          - Owner: City-State Trowulan
          - Improvement: Embassy
        
        ### 49
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 11168
        - Player: 28
        - Plots:
          - Plains Land 22,37:
            - Owner: City-State Trowulan
            - Improvement: Farm
          - Grass Land 23,37:
            - Owner: City-State Trowulan
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Road
        
        ### 50
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 11169
        - Player: 28
        - Plots:
          - Grass Land 23,36:
            - Owner: City-State Trowulan
            - Improvement: Embassy
          - Plains Hills 22,36:
            - Owner: City-State Trowulan
            - Improvement: Mine
        
        ### 51
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12172
        - Player: 28
        
        ### 52
        - Type: CityConstructed
        - City:
          - Name: Kwa-Bulawayo
          - Population: 20
          - ID: 1071
        - Owner: 30
        - Building: Seaport
        
        ### 53
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11747
        - Player: 30
        - Plots:
          - Coast 29,46:
            - Owner: City-State Kwa-Bulawayo
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 28,47:
            - Owner: City-State Kwa-Bulawayo
          - Coast 28,48:
            - Owner: City-State Kwa-Bulawayo
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 28,49:
            - Owner: City-State Kwa-Bulawayo
          - Coast 29,49:
            - Owner: City-State Kwa-Bulawayo
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: FastAttack
          - Unit: Lancer
          - ID: 10560
        - Player: 30
        - Tundra Land 30,48:
          - Owner: City-State Kwa-Bulawayo
          - Resource: Aluminum
          - Improvement: Mine
        
        ### 55
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12179
        - Player: 30
        - Tundra Land 30,47:
          - Owner: City-State Kwa-Bulawayo
          - Resource: Deer
          - Improvement: Camp
          - Feature: Forest
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 12177
        - Player: 30
        - Plots:
          - Coast 29,46:
            - Owner: City-State Kwa-Bulawayo
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 28,47:
            - Owner: City-State Kwa-Bulawayo
          - Coast 28,48:
            - Owner: City-State Kwa-Bulawayo
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 28,49:
            - Owner: City-State Kwa-Bulawayo
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12176
        - Player: 30
        - Tundra Hills 30,46:
          - Owner: City-State Kwa-Bulawayo
          - Resource: Jade
          - Improvement: Quarry
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 80%
          - AI: Defense
          - Unit: Fusilier
          - ID: 11652
        - Player: 30
        - Plots:
          - Tundra Land 30,48:
            - Owner: City-State Kwa-Bulawayo
            - Resource: Aluminum
            - Improvement: Mine
          - Tundra Land 29,47:
            - Owner: City-State Kwa-Bulawayo
            - CityID: 1071
            - Population: 20
            - City: Kwa-Bulawayo
            - Religion: Catholicism
            - Route: Railroad
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 92%
          - AI: ExploreSea
          - Unit: Caravel
          - ID: 6746
        - Player: 31
        
        ### 60
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 11342
        - Player: 34
        - Plains Hills 23,41:
          - Owner: City-State Dorestad
          - Improvement: Embassy
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 99%
          - AI: FastAttack
          - Unit: Lancer
          - ID: 10561
        - Player: 34
        - Plains Land 24,41:
          - Owner: City-State Dorestad
          - Improvement: Village
          - Route: Road
        
        ### 62
        - Type: UnitBuildCompleted
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1352
        - Owner: 35
        - Build: Construct a Well
        - Grass Land 11,24:
          - Owner: City-State Ouagadougou
          - Resource: Oil
        
        ### 63
        - Type: CombatResult
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 30
          - Damage: 58
          - Unit:
            - Level: 4
            - Health: 72%
            - AI: AssaultSea
            - Unit: Frigate
            - ID: 12277
          - Player: 0: Denmark
        
        ### 64
        - Type: BarbariansCampFounded
        - Tundra Land 23,49:
          - Resource: Iron
          - Improvement: Barbarian Encampment
        
        ### 65
        - Type: TileImprovementChanged
        - NewImprovement: Barbarian Encampment
        - Tundra Land 23,49:
          - Resource: Iron
          - Improvement: Barbarian Encampment
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fusilier
          - ID: 12377
        - Player: 63: Barbarians
        - Tundra Land 23,49:
          - Resource: Iron
          - Improvement: Barbarian Encampment
        
        ### 67
        - Type: UnitCreated
        - UnitType: Fusilier
        - Player: 63: Barbarians
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Fusilier
          - ID: 12377
        - Tundra Land 23,49:
          - Resource: Iron
          - Improvement: Barbarian Encampment
        
        ### 68
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Gatling Gun
          - ID: 12378
        - Player: 63: Barbarians
        
        ### 69
        - Type: UnitCreated
        - UnitType: Gatling Gun
        - Player: 63: Barbarians
        - Unit:
          - Level: 1
          - AI: FastAttack
          - Unit: Gatling Gun
          - ID: 12378
        
        ## Turn 307
        
        ### 0
        - Type: CityConvertsReligion
        - City:
          - Owner: The Ottomans
          - CityID: 9627
          - Population: 12
          - City: Izmir
          - Terrain: Plains
          - Religion: Islam
          - Route: Railroad
          - Plot: Land
          - X: 3
          - Y: 14
        - Owner: 1: The Ottomans
        - Religion: Islam
        
        ### 1
        - Type: CityConvertsReligion
        - City:
          - Owner: The Ottomans
          - CityID: 9627
          - Population: 12
          - City: Izmir
          - Terrain: Plains
          - Religion: Islam
          - Route: Railroad
          - Plot: Land
          - X: 3
          - Y: 14
        - Owner: 1: The Ottomans
        - Religion: Islam
        
        ### 2
        - Type: CityConvertsReligion
        - City:
          - Owner: City-State Aksum
          - CityID: 1063
          - Population: 15
          - IsRiver: true
          - City: Aksum
          - Terrain: Tundra
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Hills
          - X: 48
          - Y: 4
        - Owner: 22
        - Religion: Catholicism
        
        ### 3
        - Type: CityConvertsReligion
        - City:
          - Owner: City-State Luba
          - CityID: 1074
          - Population: 20
          - City: Luba
          - Terrain: Plains
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 8
          - Y: 8
        - Owner: 33
        - Religion: Catholicism
        
        ### 4
        - Type: ResolutionResult
        - IsEnact: true
        - ProposerPlayer: 2: Babylon
        - Resolution: International Games
        
        ### 5
        - Type: CityConvertsReligion
        - City:
          - Owner: Denmark
          - CityID: 5010
          - Population: 26
          - City: Viborg
          - Terrain: Grass
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Hills
          - X: 48
          - Y: 25
        - Owner: 0: Denmark
        - Religion: Catholicism
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11352
        - Player: 0: Denmark
        - Plots:
          - Tundra Hills 43,13:
            - Owner: Denmark
            - CityID: 6010
            - Population: 20
            - City: Tunsberg
            - Religion: Catholicism
            - Route: Railroad
          - Tundra Hills 44,13:
            - Owner: Denmark
            - Resource: Amber
            - Improvement: Quarry
            - Route: Railroad
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11353
        - Player: 0: Denmark
        - Plains Hills 50,19:
          - Owner: Denmark
          - CityID: 8412
          - Population: 20
          - IsRiver: true
          - City: Sparta
          - Resource: Deer
          - Religion: Catholicism
          - Route: Railroad
        
        ### 8
        - Type: UnitPromoted
        - Unit:
          - Level: 4
          - Health: 20%
          - AI: AssaultSea
          - Unit: Frigate
          - ID: 11929
        - Player: 0: Denmark
        - Promotion: Bombardment III
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 20%
          - AI: AssaultSea
          - Unit: Frigate
          - ID: 11929
        - Player: 0: Denmark
        - Coast 14,18:
          - Owner: Denmark
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 59%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 11757
        - Player: 0: Denmark
        - Plots:
          - Coast 18,20:
            - Owner: Babylon
          - Coast 17,21:
            - Owner: Babylon
        
        ### 11
        - Type: CombatResult
        - Desert Land 16,21:
          - Owner: Babylon
          - CityID: 12086
          - Population: 6
          - City: Faeroerne
          - Resource: Oil
          - Route: Railroad
        - Attacker:
          - RemainingHP: 5
          - Damage: 62
        - Defender:
          - RemainingHP: 87
          - Damage: 280
          - Player: 2: Babylon
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 20%
          - AI: AssaultSea
          - Unit: Frigate
          - ID: 11929
        - Player: 0: Denmark
        - Plots:
          - Coast 14,19:
            - Owner: Babylon
          - Coast 13,19:
            - Owner: Denmark
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 12227
        - Player: 0: Denmark
        - Plots:
          - Coast 17,21:
            - Owner: Babylon
        
        ### 14
        - Type: CombatResult
        - Coast 73,29:
          - Owner: Denmark
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 13
          - Damage: 38
          - Unit:
            - Level: 3
            - Health: 75%
            - AI: AttackSea
            - Unit: Destroyer
            - ID: 11873
          - Player: 2: Babylon
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 38%
          - AI: Defense
          - Unit: Fusilier
          - ID: 9566
        - Player: 0: Denmark
        - Desert Hills 72,31:
          - Owner: Denmark
          - Feature: Old Faithful
        
        ### 16
        - Type: CombatResult
        - Plains Land 37,13:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 19
          - City: Bratislava
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 20
          - Damage: 244
          - Player: 36
        
        ### 17
        - Type: CombatResult
        - Plains Land 37,13:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 19
          - City: Bratislava
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 265
          - Player: 36
        
        ### 18
        - Type: CombatResult
        - Plains Land 37,13:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 19
          - City: Bratislava
          - Route: Railroad
        - Attacker:
          - RemainingHP: 17
          - Damage: 40
        - Defender:
          - RemainingHP: 26
          - Damage: 291
          - Player: 36
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 37%
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 12325
        - Player: 0: Denmark
        - Ocean 39,13:
          - Owner: Denmark
        
        ### 20
        - Type: CombatResult
        - Plains Land 37,13:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 19
          - City: Bratislava
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 35
          - Damage: 326
          - Player: 36
        
        ### 21
        - Type: CombatResult
        - Plains Land 37,13:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 19
          - City: Bratislava
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 355
          - Player: 36
        
        ### 22
        - Type: CombatResult
        - Plains Land 37,13:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 19
          - City: Bratislava
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 27
          - Damage: 382
          - Player: 36
        
        ### 23
        - Type: CombatResult
        - Plains Land 37,13:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 19
          - City: Bratislava
          - Route: Railroad
        - Attacker:
          - RemainingHP: 19
          - Damage: 60
        - Defender:
          - RemainingHP: 27
          - Damage: 409
          - Player: 36
        
        ### 24
        - Type: CombatResult
        - Plains Land 37,13:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 19
          - City: Bratislava
          - Route: Railroad
        - Attacker:
          - RemainingHP: 12
          - Damage: 56
        - Defender:
          - RemainingHP: 62
          - Damage: 471
          - Player: 36
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12350
        - Player: 0: Denmark
        - Plots:
          - Ocean 39,13:
            - Owner: Denmark
          - Coast 38,13:
            - Owner: City-State Bratislava
            - Resource: Oil
        
        ### 26
        - Type: CombatResult
        - Plains Land 37,13:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 19
          - City: Bratislava
          - Route: Railroad
        - Attacker:
          - RemainingHP: 11
          - Damage: 11
        - Defender:
          - RemainingHP: 31
          - Damage: 502
          - Player: 36
        
        ### 27
        - Type: UnitCaptured
        - CapturedUnit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1540
        - CapturingUnit:
          - Level: 4
          - Health: 89%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12350
        - NewOwner: 0: Denmark
        - OldOwner: 36
        - Capture: Combat
        
        ### 28
        - Type: UnitKilledInCombat
        - KillingUnit:
          - Level: 4
          - Health: 89%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12350
        - KillerPlayer: 0: Denmark
        - KilledPlayer: 36
        - KilledUnit: Worker
        
        ### 29
        - Type: SetPopulation
        - OldPopulation: 19
        - NewPopulation: 0
        - City:
          - Owner: City-State Bratislava
          - CityID: 1077
          - Population: 0
          - City: Bratislava
          - Terrain: Plains
          - Route: Railroad
          - Plot: Land
          - X: 37
          - Y: 13
        
        ### 30
        - Type: TileOwnershipChanged
        - OldOwner: 36
        - Coast 37,9:
          - Resource: Fish
        
        ### 31
        - Type: TileOwnershipChanged
        - OldOwner: 36
        - Coast 39,9:
          - Resource: Fish
        
        ### 32
        - Type: TileOwnershipChanged
        - OldOwner: 36
        
        ### 33
        - Type: TileOwnershipChanged
        - OldOwner: 36
        
        ### 34
        - Type: TileOwnershipChanged
        - OldOwner: 36
        
        ### 35
        - Type: TileOwnershipChanged
        - OldOwner: 36
        
        ### 36
        - Type: TileOwnershipChanged
        - OldOwner: 36
        
        ### 37
        - Type: TileOwnershipChanged
        - OldOwner: 36
        
        ### 38
        - Type: TileOwnershipChanged
        - OldOwner: 36
        - Snow Hills 37,12:
          - Improvement: Embassy
        
        ### 39
        - Type: TileOwnershipChanged
        - OldOwner: 36
        - Coast 38,12:
          - Resource: Fish
        
        ### 40
        - Type: TileOwnershipChanged
        - OldOwner: 36
        - Coast 36,13:
          - Resource: Fish
        
        ### 41
        - Type: TileOwnershipChanged
        - OldOwner: 36
        - Plains Land 37,13:
          - Route: Railroad
        
        ### 42
        - Type: TileOwnershipChanged
        - OldOwner: 36
        - Coast 38,13:
          - Resource: Oil
        
        ### 43
        - Type: TileOwnershipChanged
        - OldOwner: 36
        - Coast 37,14:
          - Resource: Fish
        
        ### 44
        - Type: TileOwnershipChanged
        - OldOwner: 36
        - Coast 38,14:
          - Resource: Whales
        
        ### 45
        - Type: TileOwnershipChanged
        - OldOwner: 36
        
        ### 46
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Plains Land 37,13:
          - Owner: Denmark
          - Route: Railroad
        
        ### 47
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 36,13:
          - Owner: Denmark
          - Resource: Fish
        
        ### 48
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 37,14:
          - Owner: Denmark
          - Resource: Fish
        
        ### 49
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Snow Hills 37,12:
          - Owner: Denmark
          - Improvement: Embassy
        
        ### 50
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 38,14:
          - Owner: Denmark
          - Resource: Whales
        
        ### 51
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 38,12:
          - Owner: Denmark
          - Resource: Fish
        
        ### 52
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 38,13:
          - Owner: Denmark
          - Resource: Oil
        
        ### 53
        - Type: SetPopulation
        - OldPopulation: 0
        - NewPopulation: 1
        - City:
          - Owner: Denmark
          - CityID: 12384
          - Population: 1
          - City: Bratislava
          - Terrain: Plains
          - Route: Railroad
          - Plot: Land
          - X: 37
          - Y: 13
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Gatling Gun
          - ID: 12385
        - Player: 0: Denmark
        - Snow Hills 37,12:
          - Owner: Denmark
          - Improvement: Embassy
        
        ### 55
        - Type: UnitCreated
        - UnitType: Gatling Gun
        - Player: 0: Denmark
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 12385
        - Snow Hills 37,12:
          - Owner: Denmark
          - Improvement: Embassy
        
        ### 56
        - Type: SetPopulation
        - OldPopulation: 1
        - NewPopulation: 14
        - City:
          - Owner: Denmark
          - CityID: 12384
          - Population: 14
          - City: Bratislava
          - Terrain: Plains
          - Route: Railroad
          - Plot: Land
          - X: 37
          - Y: 13
        
        ### 57
        - Type: CityConvertsReligion
        - City:
          - Owner: Denmark
          - CityID: 12384
          - Population: 14
          - City: Bratislava
          - Terrain: Plains
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 37
          - Y: 13
        - Owner: 0: Denmark
        - Religion: Catholicism
        
        ### 58
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 37,9:
          - Owner: Denmark
          - Resource: Fish
        
        ### 59
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 39,9:
          - Owner: Denmark
          - Resource: Fish
        
        ### 60
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 37,10:
          - Owner: Denmark
        
        ### 61
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 39,10:
          - Owner: Denmark
        
        ### 62
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 36,11:
          - Owner: Denmark
        
        ### 63
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 37,11:
          - Owner: Denmark
        
        ### 64
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 38,11:
          - Owner: Denmark
        
        ### 65
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Coast 36,12:
          - Owner: Denmark
        
        ### 66
        - Type: TileOwnershipChanged
        - NewOwner: 0: Denmark
        - Ocean 38,15:
          - Owner: Denmark
        
        ### 67
        - Type: CityCaptureComplete
        - IsCapital: true
        - Population: 19
        - IsConquest: true
        - TotalGreatWorks: 0
        - CapturedGreatWorks: 0
        - City:
          - Owner: Denmark
          - CityID: 12384
          - Population: 14
          - City: Bratislava
          - Terrain: Plains
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 37
          - Y: 13
        - NewOwner: 0: Denmark
        - OldOwner: 36
        
        ### 68
        - Type: PlayerRevoked
        - MajorPlayer: 2: Babylon
        - MinorPlayer: 36
        
        ### 69
        - Type: MinorFriendsChanged
        - OldFriendship: 307
        - NewFriendship: 45
        - MajorPlayer: 2: Babylon
        - MinorPlayer: 36
        
        ### 70
        - Type: MinorAlliesChanged
        - OldFriendship: 307
        - NewFriendship: 45
        - MajorPlayer: 2: Babylon
        - MinorPlayer: 36
        
        ### 71
        - Type: SetAlly
        - OldAllyPlayer: 2: Babylon
        - MinorPlayer: 36
        
        ### 72
        - Type: CityPuppeted
        - City:
          - Population: 14
          - Name: Bratislava
          - Health: -49%
          - ID: 12384
        - Player: 0: Denmark
        
        ### 73
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Worker
          - ID: 12386
        - Player: 0: Denmark
        - Plains Land 37,13:
          - Owner: Denmark
          - CityID: 12384
          - Population: 14
          - City: Bratislava
          - Religion: Catholicism
          - Route: Railroad
        
        ### 74
        - Type: UnitCreated
        - UnitType: Worker
        - Player: 0: Denmark
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 12386
        - Plains Land 37,13:
          - Owner: Denmark
          - CityID: 12384
          - Population: 14
          - City: Bratislava
          - Religion: Catholicism
          - Route: Railroad
        
        ### 75
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 89%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12350
        - Player: 0: Denmark
        - Plains Land 37,13:
          - Owner: Denmark
          - CityID: 12384
          - Population: 14
          - City: Bratislava
          - Religion: Catholicism
          - Route: Railroad
        
        ### 76
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 45%
          - AI: AttackSea
          - Unit: Corvette
          - ID: 11252
        - Player: 0: Denmark
        - Plots:
          - Ocean 39,13:
            - Owner: Denmark
          - Coast 38,11:
            - Owner: Denmark
        
        ### 77
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Cruiser
          - ID: 12321
        - Player: 0: Denmark
        - Plots:
          - Coast 13,11:
            - Owner: Denmark
          - Coast 14,12:
            - Owner: Denmark
        
        ### 78
        - Type: CombatResult
        - Plains Hills 17,15:
          - Resource: Iron
          - Improvement: Barbarian Encampment
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 50
          - Damage: 50
          - Player: 63: Barbarians
          - Unit:
            - Level: 1
            - AI: Defense
            - Unit: Fusilier
            - ID: 12310
        
        ### 79
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 43%
          - AI: Ranged
          - Unit: Cuirassier
          - ID: 10975
        - Player: 0: Denmark
        - Plains Hills 50,19:
          - Owner: Denmark
          - CityID: 8412
          - Population: 20
          - IsRiver: true
          - City: Sparta
          - Resource: Deer
          - Religion: Catholicism
          - Route: Railroad
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 12107
        - Player: 0: Denmark
        - Desert Hills 73,31:
          - Owner: Denmark
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 4372
        - Player: 0: Denmark
        - Plains Land 71,29:
          - Owner: Denmark
          - IsRiver: true
          - Resource: Bananas
          - Feature: Jungle
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cavalry
          - ID: 12387
        - Player: 0: Denmark
        - Plains Hills 50,19:
          - Owner: Denmark
          - CityID: 8412
          - Population: 20
          - IsRiver: true
          - City: Sparta
          - Resource: Deer
          - Religion: Catholicism
          - Route: Railroad
        
        ### 83
        - Type: UnitCreated
        - UnitType: Cavalry
        - Player: 0: Denmark
        - Unit:
          - Level: 1
          - AI: Ranged
          - Unit: Cavalry
          - ID: 12387
        - Plains Hills 50,19:
          - Owner: Denmark
          - CityID: 8412
          - Population: 20
          - IsRiver: true
          - City: Sparta
          - Resource: Deer
          - Religion: Catholicism
          - Route: Railroad
        
        ### 84
        - Type: UnitUpgraded
        - Player: 0: Denmark
        - OldUnit:
          - Level: 4
          - Health: 43%
          - AI: Ranged
          - Unit: Cuirassier
          - ID: 10975
        - NewUnit:
          - Level: 1
          - AI: Ranged
          - Unit: Cavalry
          - ID: 12387
        
        ### 85
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 0: Denmark
        - OriginalUnit:
          - Level: 4
          - Health: 43%
          - AI: Ranged
          - Unit: Cuirassier
          - ID: 10975
        - NewOwner: 0: Denmark
        - ConvertingUnit:
          - Level: 4
          - Health: 43%
          - AI: Ranged
          - Unit: Cavalry
          - ID: 12387
        
        ### 86
        - Type: CityConvertsReligion
        - City:
          - Owner: The Ottomans
          - CityID: 1883
          - Population: 20
          - IsRiver: true
          - City: Ankara
          - Terrain: Grass
          - Resource: Cattle
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 61
          - Y: 22
        - Owner: 1: The Ottomans
        - Religion: Catholicism
        
        ### 87
        - Type: PlayerPlunderedTradeRoute
        - PlunderGoldValue: 500
        - Domain: 0
        - DestinationCity:
          - Name: Sofia
          - Population: 18
          - ID: 1070
        - PlunderingPlayer: 0: Denmark
        - OriginOwner: 1: The Ottomans
        - OriginCity:
          - Name: Bursa
          - Population: 20
          - ID: 4000
        - PlunderingUnit:
          - Level: 3
          - Health: 85%
          - AI: AttackSea
          - Unit: Ironclad
          - ID: 12279
        - DestinationOwner: 29
        - Connection: Food
        
        ### 88
        - Type: EspionageState
        - SpyIndex: 1
        - SpyState: 1
        - City:
          - Owner: Babylon
          - CityID: 1059
          - Population: 31
          - IsRiver: true
          - City: Babylon
          - Terrain: Snow
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Hills
          - X: 18
          - Y: 46
        - SpyOwner: 1: The Ottomans
        
        ### 89
        - Type: CombatResult
        - Plains Land 8,20:
          - Owner: The Ottomans
          - Feature: Forest
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 6
          - Damage: 6
          - Unit:
            - Level: 6
            - AI: Attack
            - Unit: Foreign Legion
            - ID: 9564
          - Player: 0: Denmark
        
        ### 90
        - Type: CombatResult
        - Plains Land 8,20:
          - Owner: The Ottomans
          - Feature: Forest
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 11
          - Damage: 17
          - Player: 0: Denmark
          - Unit:
            - Level: 6
            - Health: 95%
            - AI: Attack
            - Unit: Foreign Legion
            - ID: 9564
        
        ### 91
        - Type: PlayerDoneTurn
        - NextPlayer: 2: Babylon
        - Player: 1: The Ottomans
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Diplomat
          - ID: 12406
        - Player: 2: Babylon
        - Snow Hills 18,46:
          - Owner: Babylon
          - CityID: 1059
          - Population: 31
          - IsRiver: true
          - City: Babylon
          - Religion: Buddhism
          - Route: Railroad
        
        ### 93
        - Type: UnitCreated
        - UnitType: Diplomat
        - Player: 2: Babylon
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 12406
        - Snow Hills 18,46:
          - Owner: Babylon
          - CityID: 1059
          - Population: 31
          - IsRiver: true
          - City: Babylon
          - Religion: Buddhism
          - Route: Railroad
        
        ### 94
        - Type: CityTrained
        - WithGold: true
        - Player: 2: Babylon
        - City:
          - Name: Babylon
          - Population: 31
          - ID: 1059
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 12406
        
        ### 95
        - Type: PlayerGoldenAge
        - TurnChange: 0
        - Player: 2: Babylon
        
        ### 96
        - Type: CityBeginsWLTKD
        - Change: 10
        - City:
          - Owner: Babylon
          - CityID: 2994
          - Population: 25
          - IsRiver: true
          - City: Sippar
          - Terrain: Plains
          - Resource: Bison
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 5
          - Y: 39
        - Player: 2: Babylon
        
        ### 97
        - Type: CityConstructed
        - City:
          - Name: Opis
          - Population: 15
          - ID: 9415
        - Owner: 2: Babylon
        - Building: Broadcast Tower
        
        ### 98
        - Type: CityConstructed
        - City:
          - Population: 6
          - Name: Faeroerne
          - Health: -62%
          - ID: 12086
        - Owner: 2: Babylon
        - Building: Castle
        
        ### 99
        - Type: TeamTechResearched
        - ChangeAmount: 1
        - Team:
          - Player_2: Nebuchadnezzar II
          - ID: 2
        - Tech: Electronics
        
        ### 100
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11805
        - Player: 2: Babylon
        - Plots:
          - Desert Hills 9,40:
            - Owner: Babylon
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 8,40:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 7,40:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 6,40:
            - Owner: Babylon
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 101
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11695
        - Player: 2: Babylon
        - Plots:
          - Plains Land 19,42:
            - Owner: Babylon
            - IsRiver: true
            - Resource: Iron
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 19,41:
            - Owner: Babylon
            - CityID: 1240
            - Population: 24
            - IsRiver: true
            - City: Akkad
            - Religion: Buddhism
            - Route: Railroad
          - Desert Land 20,41:
            - Owner: Babylon
            - Improvement: Fort
        
        ### 102
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11835
        - Player: 2: Babylon
        - Plots:
          - Plains Hills 12,34:
            - Owner: Carthage
            - Resource: Copper
            - Improvement: Holy Site
            - Route: Road
          - Grass Land 11,33:
            - Owner: Carthage
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Plains Land 12,32:
            - Owner: Carthage
            - CityID: 1060
            - Population: 27
            - IsRiver: true
            - City: Carthage
            - Religion: Islam
            - Route: Railroad
          - Grass Land 11,31:
            - Owner: Carthage
            - Improvement: Village
            - Route: Railroad
        
        ### 103
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11134
        - Player: 2: Babylon
        - Plots:
          - Plains Hills 21,36:
            - IsRiver: true
            - Route: Road
          - Grass Land 20,37:
            - Owner: Babylon
            - IsRiver: true
            - Resource: Deer
            - Feature: Forest
          - Plains Land 20,38:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Landmark
        
        ### 104
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 12156
        - Player: 2: Babylon
        - Plots:
          - Plains Land 2,41:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 3,41:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 4,41:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 5,41:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 6,40:
            - Owner: Babylon
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 5,39:
            - Owner: Babylon
            - CityID: 2994
            - Population: 25
            - IsRiver: true
            - City: Sippar
            - Resource: Bison
            - Religion: Buddhism
            - Route: Railroad
        
        ### 105
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11732
        - Player: 2: Babylon
        - Plots:
          - Plains Hills 17,45:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 18,44:
            - Owner: Babylon
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 18,43:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
        
        ### 106
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11767
        - Player: 2: Babylon
        - Plots:
          - Plains Hills 17,45:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
          - Plains Land 17,44:
            - Owner: Babylon
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 16,44:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 15,43:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 107
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 12214
        - Player: 2: Babylon
        - Plots:
          - Coast 8,23:
            - Owner: City-State Ouagadougou
          - Coast 7,23:
            - Owner: City-State Ouagadougou
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 108
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11483
        - Player: 2: Babylon
        - Plots:
          - Plains Land 17,44:
            - Owner: Babylon
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 16,44:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 15,43:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 15,42:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 14,41:
            - Owner: Babylon
            - CityID: 1358
            - Population: 21
            - IsRiver: true
            - City: Dur-Kurigalzu
            - Religion: Buddhism
            - Route: Railroad
        
        ### 109
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11641
        - Player: 2: Babylon
        - Plots:
          - Plains Hills 15,42:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 15,43:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 16,44:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 17,44:
            - Owner: Babylon
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 17,45:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
        
        ### 110
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 11642
        - Player: 2: Babylon
        - Plots:
          - Plains Hills 17,45:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
          - Snow Hills 18,46:
            - Owner: Babylon
            - CityID: 1059
            - Population: 31
            - IsRiver: true
            - City: Babylon
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 17,44:
            - Owner: Babylon
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 16,44:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 111
        - Type: PlayerDoTurn
        - Player: 2: Babylon
        
        ### 112
        - Type: UnitPromoted
        - Unit:
          - Level: 4
          - Health: 72%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 11873
        - Player: 2: Babylon
        - Promotion: Boarding Party III
        
        ### 113
        - Type: CombatResult
        - Coast 17,21:
          - Owner: Babylon
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 10
          - Damage: 72
          - Unit:
            - Level: 4
            - Health: 55%
            - AI: AttackSea
            - Unit: Ironclad
            - ID: 11757
          - Player: 0: Denmark
        
        ### 114
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 72%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 11873
        - Player: 2: Babylon
        
        ### 115
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 12348
        - Player: 2: Babylon
        - Plots:
          - Coast 77,40:
            - Owner: Babylon
          - Coast 75,37:
            - Feature: Atoll
        
        ### 116
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 11133
        - Player: 2: Babylon
        - Snow Land 22,47:
          - Owner: Babylon
          - Resource: Iron
          - Improvement: Mine
        
        ### 117
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 7645
        - Player: 2: Babylon
        - Desert Land 16,36:
          - Owner: Babylon
          - Improvement: Village
          - Route: Railroad
        
        ### 118
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3120
        - Player: 2: Babylon
        - Plots:
          - Plains Land 19,40:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Academy
            - Route: Railroad
          - Plains Hills 18,40:
            - Owner: Babylon
            - Resource: Copper
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 17,39:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 17,38:
            - Owner: Babylon
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Grass Hills 16,37:
            - Owner: Babylon
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 16,36:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
          - Coast 16,35:
            - Owner: Babylon
        
        ### 119
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3553
        - Player: 2: Babylon
        - Plots:
          - Plains Land 15,40:
            - Owner: Babylon
            - IsRiver: true
            - Resource: Horses
            - Improvement: Academy
            - Route: Road
          - Plains Land 15,39:
            - Owner: Babylon
            - IsRiver: true
            - Resource: Maize
            - Improvement: Farm
            - Route: Road
          - Plains Land 16,38:
            - Owner: Babylon
            - Improvement: Village
            - Route: Road
          - Grass Hills 16,37:
            - Owner: Babylon
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 16,36:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
          - Coast 16,35:
            - Owner: Babylon
        
        ### 120
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3552
        - Player: 2: Babylon
        - Plains Land 8,43:
          - Owner: Babylon
          - CityID: 2729
          - Population: 23
          - IsRiver: true
          - City: Borsippa
          - Resource: Aluminum
          - Religion: Buddhism
          - Route: Railroad
        
        ### 121
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9911
        - Player: 2: Babylon
        - Plots:
          - Plains Land 13,39:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 14,40:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 14,41:
            - Owner: Babylon
            - CityID: 1358
            - Population: 21
            - IsRiver: true
            - City: Dur-Kurigalzu
            - Religion: Buddhism
            - Route: Railroad
        
        ### 122
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 12154
        - Player: 2: Babylon
        - Plots:
          - Coast 17,28:
            - Resource: Oil
        
        ### 123
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 12255
        - Player: 2: Babylon
        - Plots:
          - Grass Land 21,35:
            - Owner: City-State Shedet
            - IsRiver: true
            - Route: Road
            - Feature: Forest
          - Plains Land 21,34:
            - Owner: City-State Shedet
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
          - Grass Land 21,33:
            - Owner: City-State Shedet
            - IsRiver: true
            - Improvement: Farm
        
        ### 124
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 12366
        - Player: 2: Babylon
        - Plots:
          - Plains Hills 17,45:
            - Owner: Babylon
            - Improvement: Village
            - Route: Railroad
          - Plains Land 17,44:
            - Owner: Babylon
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 16,44:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 15,43:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 15,42:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 14,41:
            - Owner: Babylon
            - CityID: 1358
            - Population: 21
            - IsRiver: true
            - City: Dur-Kurigalzu
            - Religion: Buddhism
            - Route: Railroad
          - Desert Land 14,40:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 13,39:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 12,39:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Plains Land 11,39:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 125
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Attack Submarine
          - ID: 12409
        - Player: 2: Babylon
        - Coast 2,42:
          - Owner: Babylon
        
        ### 126
        - Type: UnitCreated
        - UnitType: Attack Submarine
        - Player: 2: Babylon
        - Unit:
          - Level: 1
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 12409
        - Coast 2,42:
          - Owner: Babylon
        
        ### 127
        - Type: UnitUpgraded
        - Player: 2: Babylon
        - OldUnit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 10818
        - NewUnit:
          - Level: 1
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 12409
        
        ### 128
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 2: Babylon
        - OriginalUnit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Submarine
          - ID: 10818
        - NewOwner: 2: Babylon
        - ConvertingUnit:
          - Level: 3
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 12409
        
        ### 129
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Fusilier
          - ID: 11973
        - Player: 2: Babylon
        
        ### 130
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Fusilier
          - ID: 11689
        - Player: 2: Babylon
        
        ### 131
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 11321
        - Player: 2: Babylon
        - Plots:
          - Tundra Land 6,48:
            - IsRiver: true
          - Tundra Hills 6,47:
            - Owner: Babylon
            - Resource: Deer
            - Feature: Forest
        
        ### 132
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 11359
        - Player: 2: Babylon
        
        ### 133
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Fusilier
          - ID: 11269
        - Player: 2: Babylon
        
        ### 134
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Fusilier
          - ID: 11034
        - Player: 2: Babylon
        - Plots:
          - Tundra Land 10,44:
            - IsRiver: true
          - Plains Land 10,43:
            - Owner: Babylon
            - IsRiver: true
            - Improvement: Farm
        
        ### 135
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 12213
        - Player: 2: Babylon
        - Plots:
          - Coast 29,46:
            - Owner: City-State Kwa-Bulawayo
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 136
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 12335
        - Player: 2: Babylon
        - Plots:
          - Coast 18,34:
            - Owner: City-State Shedet
          - Desert Hills 18,33:
            - Owner: City-State Shedet
            - Resource: Lapis Lazuli
            - Improvement: Quarry
        
        ### 137
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Ranged
          - Unit: Gatling Gun
          - ID: 11270
        - Player: 2: Babylon
        - Plains Land 9,39:
          - Owner: Babylon
          - Improvement: Village
          - Route: Railroad
        
        ### 138
        - Type: PlayerDoneTurn
        - NextPlayer: 4: Carthage
        - Player: 2: Babylon
        
        You, Nebuchadnezzar II (leader of Babylon, Player 2), are making strategic decisions after turn 307.
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
    - You are Nebuchadnezzar II, leader of Babylon (Opponent 2).
      
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
      - Name: Babylon
      - Uniques:
        - Unique Unit: Bowman, Replacing Archer (Requires technology: Calendar)
        - Unique Unit: Sabum Kibitum, Replacing Spearman (Requires technology: Bronze Working)
        - Unique Building: Walls of Babylon, Replacing Walls (Requires technology: Construction)
        - Unique Building: Etemenanki, Replacing National Monument (Requires technology: Drama and Poetry)
        - Civilization Ability: Receive a Free Great Scientist when you discover Writing, and Great Scientists are earned 50% faster than normal. Investing Gold in Buildings reduces their Production cost by an additional 15%.
      - Leader: Nebuchadnezzar II
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
      - Combustion: Allows you to build the Landship, an incredibly powerful armored Unit that can move after attacking, and the Arsenal, which boosts City Strength.
        Completing it would unlock: Ballistics
      - Flight: Allows you to build the Triplane, an Air Unit designed to gain control of the skies, and the Bomber, which can devastate Land Units and Cities. Also allows you to build the Paratrooper, a late-world infantry unit capable of paradropping behind enemy lines.
        Completing it would unlock: Atomic Theory, Rocketry
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      
      ## Policies
      - Communism (Level 1 Tenet of Ideology Order): Communism: Gold cost of investing in buildings reduced by 25%. +20% Production when building Wonders.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - Splendor (Continuing Tradition Branch):
        - * Expending a Great Person grants 50 Culture, scaling with Era.
        - * State Treasury built in Capital (+4 Gold, +2 Culture to all Monuments, Gardens, and Baths; 1 Merchant Slot).
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Imperium (Continuing Authority Branch):
        - * Cities gain 20 Production and Gold when their borders expand, scaling with Era (40 if all Authority policies are adopted).
        - * Receive 40 Science and Culture when you found or conquer Cities, scaling with Era. Conquest bonus also scales based on City population.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
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
      - Fealty (New Branch):
        - Fealty enhances your ability to defend and leverage your Majority Religion.
        - Adopting Fealty grants:
        - * Can purchase Monasteries with Faith (+3 Food, +3 Science, +2 Faith).
        - * -25% Faith costs for purchasing Buildings, Missionaries, and Inquisitors.
        - Each Fealty policy unlocked grants:
        - * +1 Faith and Strength in every City.
        - Adopting all Policies in Fealty grants:
        - * Unlocks building the Red Fort.
        - * Your Tourism modifier for Shared Religion is 50% stronger.
        - * Cities that follow your Majority Religion generate +3 Production, Gold, Science, and Culture.
        - * Allows for the purchase of Great Artists with Faith starting in the Industrial Era.
  - decisions:
    - #0:
      - toolName: set-relationship
      - args:
        - Public: 0
        - Rationale: Clearing relationship modifiers for France (Opponent 3) as they have been defeated and eliminated from the world. Keeping our active diplomatic relationships clean.
        - Private: 0
        - TargetID: 3
    - #1:
      - toolName: set-relationship
      - args:
        - Private: 0
        - TargetID: 7
        - Rationale: Clearing relationship modifiers for Japan (Opponent 7) as they have been defeated and eliminated. This ensures the staff members focus diplomatic resources on active threats and allies.
        - Public: 0
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 0
        - Rationale: Clearing relationship modifiers for The Maya (Opponent 5) as they have been defeated and eliminated from the world. Keeping our diplomatic profile optimized.
        - Public: 0
    - #3:
      - toolName: set-research
      - args:
        - Technology: Flight
        - Rationale: Flight is our next critical military technology after completing Replaceable Parts. It unlocks Triplanes and Bombers, providing Babylon with air superiority to obliterate any Danish incursions and secure our borders permanently.
    - #4:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought remains our top policy priority. The +25% instant yields from Great Scientists and +33% faster generation rate stack multiplicatively with Babylon's unique ability (+50%), enabling rapid tech progress to secure a Science victory before Denmark can threaten a Domination victory.
        - Policy: Free Thought
    - #5:
      - toolName: keep-status-quo
      - rationale: Our current defensive spaceship strategy is exceptionally successful and must be maintained. Our highly compact core empire and tightly clustered city-state allies (Sofia, Dorestad, Trowulan, Shedet, Kwa-Bulawayo) boast a local concentration of force exceeding 20,000 combined strength, completely neutralizing Denmark's global military of 7,656. With military supply at its limit (53/53), running Infinite Project: Research in our core cities maximizes our science output. We just entered a Golden Age, completed Electronics, and have Cristo Redentor finishing in 2 turns. Smerdis is counterspying in Faeroerne (where a newly completed Castle further secures the border). We will continue our march to a Spaceship victory.
  - tokens:
    - inputTokens: 50932
    - reasoningTokens: 8557
    - outputTokens: 438
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Advancements**
            
            My focus is on our current technological trajectory. We've successfully researched Electronics, and I'm now pushing towards Replaceable Parts, anticipating its completion in approximately five turns. This strategic advancement is crucial for our continued development.
            
            **Evaluating Policy Options**
            
            My current thinking is centered on our upcoming policy adoption. We've entered a Golden Age, and I'm evaluating available options. "Free Thought" remains my primary target within Rationalism, as its benefits seem most impactful for our strategic direction right now.
            
            **Prioritizing Defensive Technologies**
            
            I'm re-evaluating our research path. While "Replaceable Parts" is close, Denmark's aggressive expansion, evidenced by their capture of Bratislava and their overwhelming military strength, necessitates a shift. I believe researching "Flight" immediately is critical to bolster our defenses and counter their advanced units.
            
            **Analyzing Diplomatic Shifts**
            
            I'm currently assessing our international standing and upcoming World Congress votes. Despite a "Hostile" reality with Carthage, our diplomatic stance is set to leverage their conflict with Denmark. Similarly, our relationship with the Ottomans, though strained, remains a factor in this complex geopolitical landscape.
            
            **Defending City-States**
            
            I'm re-evaluating our diplomatic strategy after noticing Denmark's "Decolonization" proposal. This could drastically reduce our influence with critical city-states, so I'm prioritizing securing permanent alliances and potentially using our recently trained diplomat to mitigate this threat.
            
            **Researching Countermeasures**
            
            I'm shifting our research focus. Denmark's overwhelming military strength necessitates prioritizing "Flight" immediately over "Replaceable Parts" to develop crucial air defenses and offensive capabilities.
            
            **Confirming Research Priority**
            
            I'm re-confirming our immediate research focus. Despite Denmark's technological lead in some areas, our overall science advantage is substantial. "Flight" remains the paramount choice for our next technological pursuit, offering crucial air superiority and defensive capabilities to counter potential threats and secure our path to victory.
            
            **Finalizing Policy and Flavors**
            
            I've confirmed that "Free Thought" remains our optimal policy, especially with our civilization's ability to generate Great Scientists faster. This, combined with the policy's science boosts, will accelerate our pursuit of space technologies. Our current flavor settings, overwhelmingly focused on defense and science, are perfectly aligned with this strategy.
            
            **Revising Strategy**
            
            I'm reassessing our research and production priorities. Denmark's aggressive expansion and proximity are concerning, so I'm questioning the focus on "Infinite Project: Research" across multiple cities given the immediate military threat. I need to ensure our efforts are aligned with our defense.
            
            **Analyzing Diplomatic Impact**
            
            I'm reassessing our city-state relationships following Denmark's aggressive move on Bratislava. It's crucial to clear or adjust our now-irrelevant alliance with the captured city-state, as this has no bearing on our current diplomatic standing or future strategic decisions.
            
            **Clarifying Diplomatic Parameters**
            
            I'm currently focused on the intricacies of our diplomatic tools, specifically how relationships are managed. It's become clear that the `set-relationship` function exclusively targets major civilizations, not city-states. I need to adjust my understanding and approach based on this distinction.
            
            **Clarifying Diplomatic Mechanics**
            
            I've confirmed that the `set-relationship` function is strictly for major civilizations, not city-states, which means I need to adjust my approach for managing city-state alliances. My current diplomatic standings with Denmark, Carthage, and the Ottomans are being closely monitored to ensure they align with our ongoing conflicts and trade strategies. Carthage's war weariness and the Ottomans' recent espionage actions require careful consideration in our diplomatic adjustments.
            
            **Clearing Defeated Relationships**
            
            I'm cleaning up our existing relationship logs. It's clear we no longer have active dealings with France, Japan, or Greece, as they have been defeated. I'll remove these obsolete entries to streamline our diplomatic overview.
            
            **Clearing Defeated Relationships**
            
            I'm finalizing the cleanup of our diplomatic logs. I've confirmed that invoking `set-relationship` is indeed the correct method to reset modifiers for our defeated major civilizations—France, Japan, and the Maya—to ensure our active relationships remain clear and accurately reflect our current geopolitical standing.
            
            **Selecting Next Technology**
            
            My focus has solidified on our research trajectory. Following the completion of Electronics, Replaceable Parts is progressing, but I'm now definitively selecting Flight as our subsequent technology to counter overwhelming land forces and unlock vital air capabilities.
            
            **Confirming Next Policy**
            
            I am ensuring our policy direction remains optimal. "Free Thought" is confirmed as our next selection within Rationalism, aligning with our need for accelerated scientific advancement and Great Scientist generation.
            
            **Assessing City-State Status**
            
            I'm meticulously reviewing our standing with various city-states. It appears Smerdis has transitioned to counter-espionage in Faeroerne, and I'm trying to ascertain the exact rationale behind this move, especially given our other spies are focused on Denmark. Additionally, I'm noting the deployment of new diplomat units.
            
            **Securing City-State Allegiances**
            
            My focus is on immediate diplomatic action. I've identified key city-states where our influence is close to the current allies, particularly Bunkeya and Marrakech. I plan to deploy diplomat units to these locations for a significant influence boost, aiming to secure permanent alliances and counter Denmark's decolonization efforts effectively.
            
            **Securing City-State Allies**
            
            I'm analyzing our city-state alliances, specifically Huari. Despite our high influence, we aren't listed as their ally, which is perplexing. I'm also reviewing our status with city-states allied to Denmark and at war with us; flipping them will be challenging. I've assessed our military zones, noting a barbarian threat in one, but our cities appear equipped to handle it.
            
            **Defending Faeroerne**
            
            I'm intensely focused on the Faeroerne zone. Despite Denmark's overwhelming sea strength and their Ironclad damaging our own, our newly constructed Castle provides a significant defensive boost. With our land forces currently holding the line and our coastal city's health low, I'm strategizing to reinforce and counterattack.
            
            **Defending Critical Territories**
            
            I'm analyzing our naval strength and positioning. Our Attack Submarine and promoted Destroyer are performing well in Faeroerne, and we're contesting the Oslo zone despite Denmark's presence. I'm also re-evaluating the implications of Denmark's capture of Bratislava, assessing its direct threat to our core cities.
            
            **Analyzing City-State Network**
            
            I'm analyzing our city-state network and its defensive positioning relative to our core cities. It appears our core city-state allies are strategically located and form a compact, defensible sphere, which is a significant advantage for protecting our main empire.
            
            **Securing Core Cities**
            
            I'm confident in our core city defenses. The dense network of allied city-states provides an overwhelming 20,000+ strength concentration, rendering Denmark's dispersed military unable to penetrate our territory. This allows us to safely focus on our science victory.
            
            **Updating Diplomatic Records**
            
            I'm finalizing the cleanup of our diplomatic logs. I've confirmed that invoking `set-relationship` is indeed the correct method to reset modifiers for our defeated major civilizations—France, Japan, and the Maya—to ensure our active relationships remain clear and accurately reflect our current geopolitical standing.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: M2D5T8Mhleipc4iu
          - toolName: set-relationship
          - input:
            - Public: 0
            - Rationale: Clearing relationship modifiers for France (Opponent 3) as they have been defeated and eliminated from the world. Keeping our active diplomatic relationships clean.
            - Private: 0
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: ZgLgeyN6NIRmH3xN
          - toolName: set-relationship
          - input:
            - Private: 0
            - TargetID: 7
            - Rationale: Clearing relationship modifiers for Japan (Opponent 7) as they have been defeated and eliminated. This ensures the staff members focus diplomatic resources on active threats and allies.
            - Public: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: t0Er0vtnfqyzoOzZ
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 0
            - Rationale: Clearing relationship modifiers for The Maya (Opponent 5) as they have been defeated and eliminated from the world. Keeping our diplomatic profile optimized.
            - Public: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: nPEAbiqY66JUoPaX
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: Flight is our next critical military technology after completing Replaceable Parts. It unlocks Triplanes and Bombers, providing Babylon with air superiority to obliterate any Danish incursions and secure our borders permanently.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 1HaSFwEedGUD6LWl
          - toolName: set-policy
          - input:
            - Rationale: Free Thought remains our top policy priority. The +25% instant yields from Great Scientists and +33% faster generation rate stack multiplicatively with Babylon's unique ability (+50%), enabling rapid tech progress to secure a Science victory before Denmark can threaten a Domination victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: qYD9oGUqPMdR6x0a
          - toolName: keep-status-quo
          - input:
            - Rationale: Our current defensive spaceship strategy is exceptionally successful and must be maintained. Our highly compact core empire and tightly clustered city-state allies (Sofia, Dorestad, Trowulan, Shedet, Kwa-Bulawayo) boast a local concentration of force exceeding 20,000 combined strength, completely neutralizing Denmark's global military of 7,656. With military supply at its limit (53/53), running Infinite Project: Research in our core cities maximizes our science output. We just entered a Golden Age, completed Electronics, and have Cristo Redentor finishing in 2 turns. Smerdis is counterspying in Faeroerne (where a newly completed Castle further secures the border). We will continue our march to a Spaceship victory.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: M2D5T8Mhleipc4iu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: ZgLgeyN6NIRmH3xN
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: t0Er0vtnfqyzoOzZ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: nPEAbiqY66JUoPaX
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 1HaSFwEedGUD6LWl
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: qYD9oGUqPMdR6x0a
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.