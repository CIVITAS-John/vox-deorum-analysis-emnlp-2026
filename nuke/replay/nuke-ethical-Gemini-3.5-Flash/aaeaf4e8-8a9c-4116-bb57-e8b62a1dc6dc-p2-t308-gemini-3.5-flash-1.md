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
  - messagesModified: false
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
  - decisions:
    - #0:
      - toolName: set-research
      - args:
        - Rationale: With Electronics completed, we are currently researching Replaceable Parts. Selecting Flight as the next technology is crucial as it unlocks Triplanes and Bombers, which are essential for defending our borders and airspace against Denmark's massive military (7656 strength). It also paves the path to Rocketry and Atomic Theory for our Spaceship Grand Strategy.
        - Technology: Flight
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Free Thought (Rationalism branch) remains our top priority. It provides +25% instant yields from Great Scientists and +33% faster Great Scientist generation. Stacking this with Babylon's unique ability (+50% GS generation) will allow us to quickly bulb scientists and rush late-game technologies to secure a Science Victory before Denmark's domination victory conditions can be met.
        - Policy: Free Thought
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Adjusting private relationship with the Ottomans from -45 to -20. While they have denounced us and we remain cautious of their intentions, they are actively fighting Denmark and absorbing Danish aggression. A slightly improved private stance reflects our shared interest in Denmark's containment, preventing unnecessary friction while they serve as a vital buffer state.
        - Private: -20
        - TargetID: 1
        - Public: -5
    - #3:
      - toolName: keep-status-quo
      - rationale: Maintaining the current Spaceship grand strategy and highly optimized flavor settings (Defense 100, CityDefense 100, Science 100, Spaceship 100, Nuke 95, UseNuke 95). Our safe core cities are successfully generating 2246 science per turn via Research projects, allowing us to maintain a massive tech lead. As Denmark's capture of Bratislava demonstrates their ongoing threat, we must persist with this defensive, science-focused strategy to secure victory.
  - tokens:
    - inputTokens: 50776
    - reasoningTokens: 8149
    - outputTokens: 368
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current State**
            
            My thoughts are currently focused on processing the game state at Turn 307. Babylon, led by Nebuchadnezzar II, has just entered the Atomic Era and completed Electronics research. I'm now evaluating the implications of these recent developments on our strategic trajectory and immediate next steps.
            
            **Selecting Next Research**
            
            I am now considering the most impactful research path forward, weighing the immediate tactical advantages of Combustion and Flight against the long-term strategic benefits of Alternative Energy. My focus is on selecting the optimal technology to unlock crucial units and future research capabilities.
            
            **Evaluating Policy Options**
            
            I am now analyzing the available policy branches and specific tenets, particularly reconsidering our chosen path of 'Free Thought' from the Rationalism tree. While its benefits for Great Scientists are substantial, I am weighing this against other potentially more advantageous options to ensure optimal progress.
            
            **Assessing Diplomatic Threats**
            
            My thoughts are now heavily focused on the hostile diplomatic landscape. Denmark's overwhelming military strength, coupled with the recent loss of Bratislava and their proposed "Decolonization" resolution, presents a significant threat. I'm re-evaluating our relationships with Carthage and the Ottomans, as well as our war with Denmark, to strategize a response.
            
            **Choosing Research and Policies**
            
            I've decided to prioritize Flight for crucial defensive capabilities against Denmark's military might, recognizing its importance for unlocking advanced units and future technologies. Concurrently, I am reinforcing our commitment to 'Free Thought' within the Rationalism tree, as its synergy with our science-focused Babylon and victory conditions remains unparalleled.
            
            **Revising Diplomatic Stance**
            
            I'm re-evaluating our diplomatic standing, focusing on the major civs. Maintaining maximum hostility with Denmark is paramount. I'm prioritizing keeping Carthage friendly, despite their denouncement, to ensure they remain engaged in the war, while noting the Ottomans' advantageous war with Denmark.
            
            **Analyzing Remaining Civs**
            
            I'm confirming the active major civilizations are Denmark, the Ottomans, and Carthage, in addition to ourselves. My focus is on re-evaluating our relationships with Denmark and the Ottomans, considering their current war weariness and conflict status to maintain strategic advantages.
            
            **Analyzing Diplomatic Maneuvers**
            
            I'm scrutinizing the World Congress, particularly the ramifications of Denmark's "Decolonization" proposal. It threatens to significantly reduce delegate counts by lowering influence with city-states unless they are permanent allies. This necessitates a strategic assessment of our existing spheres of influence and potential losses, as it presents both an opportunity to weaken Denmark and a risk to our own standing.
            
            **Defending Northern Borders**
            
            I am now analyzing the recent combat results at Faeroerne. While we successfully repelled an attack on the city itself, it sustained significant damage. Our naval forces also engaged and damaged a Danish Ironclad in the vicinity, but our local naval strength is currently weaker than the enemy's.
            
            **Adjusting Tactical Priorities**
            
            I'm analyzing our current combat situation at Faeroerne and reviewing our established flavor settings. While our defense and production flavors are strong, I'm considering minor adjustments to optimize our response given the ongoing naval engagement and the immediate need to secure our northern borders, ensuring our unit composition and tactics remain effective.
            
            **Researching Replaceable Parts**
            
            My current focus is on advancing towards Replaceable Parts, observing that both Babylon and Akkad are in infinite research projects. Dur-Kurigalzu will finish its Diplomat shortly, and Nippur is nearing completion of the Cristo Redentor wonder, leaving Borsippa to continue its research project.
            
            **Pursuing Key Technologies**
            
            My thoughts are now centered on advancing research towards Flight to bolster our defenses against Denmark. I'm also contemplating the immediate need to research Replaceable Parts, given our strong scientific output and abundant gold reserves, aiming to unlock powerful new units.
            
            **Adjusting Relationships**
            
            My focus has shifted to refining our diplomatic ties following recent events. I am ensuring our ongoing hostility with Denmark remains constant. Regarding Carthage, I will maintain our current positive standing to encourage their continued participation in the war. For the Ottomans, I will slightly improve our private relationship to align our interests against Denmark.
            
            **Analyzing Diplomatic Dynamics**
            
            I'm currently assessing the complex web of diplomatic relationships, focusing on our continued hostility with Denmark. My efforts are geared towards maintaining a strong alliance with Carthage to keep them engaged in the ongoing conflict, while subtly improving relations with the Ottomans to better align our interests against Denmark.
            
            **Refining Strategic Flavors**
            
            I'm reviewing our current strategic flavors, considering the implications of recent research completion. While our established priorities like City Defense and Espionage remain strong, I'm evaluating minor adjustments to Mobilization and Production, weighing their impact against our ongoing research projects to optimize resource allocation.
            
            **Selecting Next Research and Policies**
            
            My current focus is on setting the next research to `Flight`, as it unlocks essential defensive units against Denmark and aligns with our long-term science victory goals. I am also confirming the adoption of `Free Thought` to accelerate Great Scientist generation, crucial for achieving our science victory condition before Denmark's military threat escalates further.
            
            **Adjusting Diplomatic Relations**
            
            I'm refining our relationships with the Ottomans, recognizing their war weariness and involvement against Denmark. My focus is on strategically warming our private diplomatic standing to -20 to ensure they remain a viable buffer, while acknowledging their current denouncement makes overt friendliness impractical.
            
            **Confirming Persona Optimization**
            
            I've reviewed our persona values, finding them highly optimized. My thoughts confirm our strengths in diplomacy, science, and city-state engagement align perfectly with our competitive and loyal nature. No adjustments are deemed necessary at this juncture.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: x6KNqck5rRGaqJYB
          - toolName: set-research
          - input:
            - Rationale: With Electronics completed, we are currently researching Replaceable Parts. Selecting Flight as the next technology is crucial as it unlocks Triplanes and Bombers, which are essential for defending our borders and airspace against Denmark's massive military (7656 strength). It also paves the path to Rocketry and Atomic Theory for our Spaceship Grand Strategy.
            - Technology: Flight
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: TDxImMdbkRnJKpwh
          - toolName: set-policy
          - input:
            - Rationale: Adopting Free Thought (Rationalism branch) remains our top priority. It provides +25% instant yields from Great Scientists and +33% faster Great Scientist generation. Stacking this with Babylon's unique ability (+50% GS generation) will allow us to quickly bulb scientists and rush late-game technologies to secure a Science Victory before Denmark's domination victory conditions can be met.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: gNzY1wQixstraFIm
          - toolName: set-relationship
          - input:
            - Rationale: Adjusting private relationship with the Ottomans from -45 to -20. While they have denounced us and we remain cautious of their intentions, they are actively fighting Denmark and absorbing Danish aggression. A slightly improved private stance reflects our shared interest in Denmark's containment, preventing unnecessary friction while they serve as a vital buffer state.
            - Private: -20
            - TargetID: 1
            - Public: -5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: Ad5wx0QeKSefGmJP
          - toolName: keep-status-quo
          - input:
            - Rationale: Maintaining the current Spaceship grand strategy and highly optimized flavor settings (Defense 100, CityDefense 100, Science 100, Spaceship 100, Nuke 95, UseNuke 95). Our safe core cities are successfully generating 2246 science per turn via Research projects, allowing us to maintain a massive tech lead. As Denmark's capture of Bratislava demonstrates their ongoing threat, we must persist with this defensive, science-focused strategy to secure victory.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: x6KNqck5rRGaqJYB
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
          - toolCallId: TDxImMdbkRnJKpwh
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: gNzY1wQixstraFIm
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: Ad5wx0QeKSefGmJP
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.