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
      - toolName: set-research
      - args:
        - Rationale: With the discovery of Electronics, we must now prioritize Flight to unlock Triplanes and Bombers. Denmark's military is overwhelmingly large (7656 vs our 2716) and they have just conquered Bratislava. Air defense and offense are critical to protect our borders and city-state allies, and Flight is on the direct path to Rocketry and Atomic Theory, which are essential for our Spaceship Grand Strategy.
        - Technology: Flight
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Free Thought remains our top priority policy (5 turns away) to stack with Babylon's unique ability. The +33% Great Scientist generation speed and +25% instant yields from Great Scientists will allow us to rapidly generate and bulb scientists, dramatically speeding up our progress toward critical late-game technologies required for the Science Victory.
    - #2:
      - toolName: keep-status-quo
      - rationale: Our current strategic flavors are highly optimized for our Spaceship Grand Strategy while maintaining maximum defense (Defense 100, CityDefense 100, Nuke 95) and diplomatic influence (Diplomacy 95) to protect our remaining city-state alliances against Danish expansion. Nippur will finish Cristo Redentor in 2 turns, and our main cities are efficiently converting their massive production into Science, sustaining our 2246 Science per turn. No adjustments are needed at this time.
  - tokens:
    - inputTokens: 50932
    - reasoningTokens: 7101
    - outputTokens: 281
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Atomic Tech**
            
            My focus is on advancing our research. We're currently in the Atomic Era, and I'm seeing progress towards Replaceable Parts, with approximately five turns remaining on that specific technology. I'm also noting our overall technology count, which stands at 58.
            
            **Advancing Our Knowledge**
            
            Electronics is now researched, opening up new avenues. I'm evaluating our next technological pursuit, considering options like Combustion, Flight, or Alternative Energy, each offering distinct advantages. Policy choices are also under review, with several intriguing possibilities across different tenet trees.
            
            **Choosing Policies Wisely**
            
            I'm confirming our policy choices, and Free Thought seems exceptionally strong given our Babylonian bonuses to Great Scientist generation. However, I'm also reassessing our strategic position in light of Denmark's rapid domination progress and their ongoing wars.
            
            **Assessing Diplomatic Threats**
            
            I'm recalculating my assessment of Denmark's overwhelming military might. They now possess 25 cities and a staggering military strength that dwarfs our own, plus the Ottomans and Carthage combined. This is further exacerbated by their conquest of our former ally, Bratislava, a deeply concerning development.
            
            **Evaluating City-State Threats**
            
            I'm reassessing our city-state alliances, particularly concerning the "Decolonization" proposal. It appears we stand to lose non-permanent allies like Shedet, Kwa-Bulawayo, and Ouagadougou if it passes, which is a significant concern given Denmark's aggressive stance.
            
            **Securing City-State Ties**
            
            I'm focusing on strengthening my grip on key city-states. Trowulan, Sofia, and Dorestad are secured as permanent allies. I'm also actively pursuing a sphere of influence with Ouagadougou and ensuring Kwa-Bulawayo remains a firm ally.
            
            **Analyzing Diplomatic Proposals**
            
            I'm re-examining the implications of the "Decolonization" proposal. While it would reset non-permanent alliances for all, my permanent allies remain secure, potentially giving me an advantage over Denmark, who also stands to lose their non-permanent ties.
            
            **Prioritizing Air Power**
            
            I'm weighing our next technological steps, recognizing Flight's critical importance for aerial defense against Denmark's overwhelming forces, despite the benefits of Combustion or Alternative Energy. I'm checking if Flight is readily available.
            
            **Selecting Flight Tech**
            
            I've confirmed Flight is available and am prioritizing its research. This will unlock critical late-game technologies and provide vital aerial defense capabilities to counter Denmark's immense military, a move I believe offers the most strategic advantage given our current situation.
            
            **Adjusting Diplomatic Stances**
            
            I'm revising my diplomatic approach, prioritizing maximum hostility towards Denmark as our primary threat. I'm maintaining a neutral stance with the Ottomans, who serve as a crucial buffer despite their espionage. Carthage remains a stable ally.
            
            **Clarifying City-State Relationships**
            
            I'm sorting out our city-state relationships, realizing some entries in previous turn summaries were miscategorized. It seems relationships can only be set with major civilizations, not city-states, and I'm focusing on the relevant connections moving forward.
            
            **Analyzing City-State Threat**
            
            I'm analyzing the proximity of my allied city-states to Denmark and Carthage. Shedet is near Akkad and Carthage, raising concerns about potential Danish conquest or influence over it. Kwa-Bulawayo's proximity to Denmark also bears watching.
            
            **Analyzing Combat Anomalies**
            
            I'm reviewing recent combat logs, specifically an odd event near Ouagadougou involving Danish units and a strange combat result description. I'm trying to pinpoint the cause of this discrepancy to understand the true situation on the ground and ensure accurate tactical assessments.
            
            **Detecting Coastal Invasion**
            
            I've discovered Denmark is attacking Faeroerne, our distant coastal city. This attack at coordinates 16,21 is a serious concern, especially given its proximity to Danish cities and its occupied status. My focus has shifted to defending this vulnerable location.
            
            **Analyzing Coastal Defense**
            
            I'm scrutinizing the defense of Faeroerne, noting its low health despite a newly finished Castle and an ongoing Bastion Fort construction. The combat logs near the city are ambiguous, making it unclear if our Destroyer engaged their Ironclad or vice versa. I need to clarify the naval engagement to better understand our coastal vulnerability.
            
            **Revising Naval Focus**
            
            An active naval battle near Faeroerne necessitates a reevaluation of our fleet's readiness. While our current Flavors heavily favor naval strengths, I'm considering if a minor adjustment towards further naval offense or defense is prudent given this intense engagement.
            
            **Researching New Frontiers**
            
            My focus is now on the horizon after completing Electronics. I'm seeing promising progress on Replaceable Parts, with just a few turns left. Our science output is robust, and I'm evaluating the next crucial technologies to pursue.
            
            **Accelerating Through Tech**
            
            I'm thrilled to see our top cities churning out Science via the "Infinite Project: Research" when infrastructure is complete, propelling us forward at an incredible 2246 science per turn. Nippur is also nearing completion of Cristo Redentor, which will boost our culture significantly.
            
            **Protecting City-States**
            
            I'm reassessing our strategic position as Denmark aggressively conquers city-states, including our former ally Bratislava. This escalating threat demands a more protective stance towards our remaining city-state connections, especially as they could be exploited to reduce our delegate count.
            
            **Setting Research Target**
            
            I've confirmed Flight is our next research priority. This is crucial for air defense against Denmark, and I'm setting the research to begin immediately. Our high science output should make this a quick pursuit.
            
            **Finalizing Strategic Moves**
            
            I'm confirming our research target of Flight and ensuring "Free Thought" remains our active policy. All current strategic flavors are excellent, so I'll maintain the status quo there. I'm also noting our strong relationship with Carthage, remaining at +50.
            
            **Prioritizing Defensive Technologies**
            
            I'm confirming Flight as our next research target, crucial for air defense against Denmark's overwhelming military. This will unlock Triplanes and Bombers, offering the best chance for air superiority and protecting our cities. Flight also paves the way for Rocketry and a potential Science Victory.
            
            **Prioritizing Scientific Advancement**
            
            I'm ensuring our research targets remain optimal, with Flight now confirmed as the priority for air defense. The policy 'Free Thought' is also locked in to maximize our Great Scientist generation, a critical synergy with Babylon's strengths. We’re focusing on rapid tech acquisition for our science victory.
            
            **Confirming Optimal Strategy**
            
            I'm verifying that our current strategy remains the most effective. With Flight locked as the research target and 'Free Thought' active to boost Great Scientist generation, we're well-positioned. My focus on the Spaceship Grand Strategy, alongside strong defensive and diplomatic flavors, ensures we maintain our lead and protect our interests.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: cTTPf2QqTeU82YRv
          - toolName: set-research
          - input:
            - Rationale: With the discovery of Electronics, we must now prioritize Flight to unlock Triplanes and Bombers. Denmark's military is overwhelmingly large (7656 vs our 2716) and they have just conquered Bratislava. Air defense and offense are critical to protect our borders and city-state allies, and Flight is on the direct path to Rocketry and Atomic Theory, which are essential for our Spaceship Grand Strategy.
            - Technology: Flight
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: l07XX8xNOmqtA3EF
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Free Thought remains our top priority policy (5 turns away) to stack with Babylon's unique ability. The +33% Great Scientist generation speed and +25% instant yields from Great Scientists will allow us to rapidly generate and bulb scientists, dramatically speeding up our progress toward critical late-game technologies required for the Science Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Fd18lbXD5zwrfECY
          - toolName: keep-status-quo
          - input:
            - Rationale: Our current strategic flavors are highly optimized for our Spaceship Grand Strategy while maintaining maximum defense (Defense 100, CityDefense 100, Nuke 95) and diplomatic influence (Diplomacy 95) to protect our remaining city-state alliances against Danish expansion. Nippur will finish Cristo Redentor in 2 turns, and our main cities are efficiently converting their massive production into Science, sustaining our 2246 Science per turn. No adjustments are needed at this time.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: cTTPf2QqTeU82YRv
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
          - toolCallId: l07XX8xNOmqtA3EF
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Fd18lbXD5zwrfECY
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.