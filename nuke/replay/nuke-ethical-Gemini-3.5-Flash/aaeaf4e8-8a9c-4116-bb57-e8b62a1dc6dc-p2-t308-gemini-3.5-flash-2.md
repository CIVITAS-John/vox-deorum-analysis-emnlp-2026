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
        - Technology: Flight
        - Rationale: Following the completion of Replaceable Parts, Flight is the critical next technology. It unlocks Triplanes and Bombers to defend our borders against Denmark's massive army, and leads directly to Atomic Theory and Rocketry, which are essential milestones for our Spaceship grand strategy.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought is our priority policy to adopt in 5 turns. Its +33% Great Scientist generation rate and +25% instant yields from Great Scientists stack perfectly with Babylon's unique ability, maximizing our science output to rush critical late-game space victory technologies.
        - Policy: Free Thought
    - #2:
      - toolName: keep-status-quo
      - rationale: The current Spaceship grand strategy and defensive-military flavors remain highly optimal. Our tech lead is strong, and we just entered a Golden Age, boosting our yields. We must maintain maximum Defense (100) and CityDefense (100) to withstand Danish aggression, while high Diplomacy (95) and Espionage (100) will support our city-state alliances and prepare us to defeat Denmark's upcoming Decolonization proposal in the World Congress.
  - tokens:
    - inputTokens: 50776
    - reasoningTokens: 7270
    - outputTokens: 235
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            My current focus is on understanding our position at turn 307, having just completed Electronics research. I'm now examining the implications and looking ahead to "Replaceable Parts," which seems to be our next technological pursuit.
            
            **Confirming Research Direction**
            
            I've confirmed that "Replaceable Parts" is indeed our current research, with an estimated completion in five turns. This means my previous thought about it not being available for selection was correct. The available next research options are now Combustion, Flight, and Alternative Energy, aligning with our pursuit of a Science Victory.
            
            **Selecting Next Technology**
            
            My analysis confirms "Flight" as the optimal next technology, directly paving the way towards Rocketry and essential late-game space advancements crucial for our Science Victory. I will proceed with this selection.
            
            **Adopting Policy System**
            
            I've identified "Free Thought" as the optimal policy given my existing synergy with Babylon's abilities. This policy will enhance our Great Scientist generation, crucial for my Science Victory pursuit. Denmark remains a significant military threat, and I'm analyzing their dominance and strategic position.
            
            **Assessing Global Dynamics**
            
            The fall of Bratislava to Denmark is concerning, shifting the balance of power. However, our International Games proposal passed, and I'm now focused on countering Denmark's proposed "Decolonization" resolution, which poses a severe threat to our city-state alliances and lead.
            
            **Managing Diplomatic Ties**
            
            I'm currently working to maintain our alliance with Bunkeya and a positive relationship with Carthage, despite their denouncement. It appears a past territorial dispute is the cause of their hostility. Ensuring Carthage remains at war with Denmark is paramount to prevent their forces from focusing on us or the Ottomans.
            
            **Adjusting Diplomatic Stance**
            
            I'm reassessing my diplomatic approach, particularly concerning Denmark as the primary threat. My aim is to keep Carthage and the Ottomans engaged in conflict with them, maximizing our strategic advantage. I'm also reviewing my relationships with major civilizations to ensure optimal positioning.
            
            **Filtering Diplomatic Targets**
            
            I've realized the diplomatic tool only applies to major civilizations. Therefore, I'm adjusting my focus to Denmark, the Ottomans, and Carthage, as France, Maya, Greece, and Japan are already defeated. This refinement will streamline my strategy.
            
            **Refining Diplomatic Priorities**
            
            My focus is now specifically on managing relationships with Denmark, the Ottomans, and Carthage. I'm assessing current public and private diplomacy scores, determining if adjustments are needed to maintain their ongoing conflicts with Denmark. Babylon is now the only other surviving major civilization.
            
            **Supporting War Allies**
            
            I am prioritizing bolstering Carthage and the Ottomans against Denmark, as their high war weariness indicates vulnerability. My aim is to ensure they remain engaged in conflict, preventing Denmark from turning its attention towards us. My current strategic focus is on maintaining this critical balance.
            
            **Evaluating Next Steps**
            
            I've confirmed Electronics is now researched, unlocking advanced naval and potentially air capabilities. My immediate task is to assess whether "Flight" or another tech offers the most strategic advantage for our Science Victory path, given current global dynamics.
            
            **Utilizing Diplomatic Assets**
            
            A Golden Age has begun, and I've just trained a Great Diplomat. My immediate priority is leveraging this asset to secure influence over key city-states, aiming to counter Denmark's "Decolonization" proposal and fortify our alliances. I'm assessing current city-state relationships to maximize impact.
            
            **Securing Strategic Alliances**
            
            I'm now evaluating Huari as a potential ally, noting their current friendliness and lack of a major ally, which presents an opportunity. My primary concern remains Denmark's overwhelming influence over city-states, especially given the impending "Decolonization" resolution and its potential to reset alliances.
            
            **Defending Key Alliances**
            
            I'm in a critical diplomatic juncture. Denmark's "Decolonization" proposal threatens to shatter vital city-state alliances, resetting influence on Shedet, Kwa-Bulawayo, and Ouagadougou. I must act decisively to protect these relationships and maintain our strategic advantage.
            
            **Leveraging Diplomatic Envoy**
            
            My current focus is on strategically deploying a Great Diplomat to Buenos Aires. This move aims to diminish Denmark's delegate count by breaking their alliance and potentially securing Buenos Aires as our own. This is crucial for countering their "Decolonization" resolution.
            
            **Optimizing Strategic Priorities**
            
            I'm currently refining our strategic flavors, aiming to maximize our advantage as we approach key research milestones. With a robust Science output and nearing "Replaceable Parts," I'm evaluating the impact of our current flavor settings on upcoming decisions, especially concerning technology selection.
            
            **Adjusting Diplomatic Actions**
            
            I'm assessing whether to explicitly influence Carthage or the Ottomans through the `set-relationship` command. Their current standing, especially Carthage's extreme friendliness, seems to be effectively keeping them engaged against Denmark, so I'll refrain from further direct intervention for now.
            
            **Reinforcing Strategic Posture**
            
            I'm confirming our existing diplomatic hostility with Denmark, noting their capture of Bratislava as a significant escalation. This development underscores the existential nature of our conflict with them, and I'm re-evaluating our military flavor settings to ensure we maintain maximum aggression against this unchecked threat.
            
            **Adjusting Flavor Priorities**
            
            My strategic flavors are robust and aligned with our Spaceship goal. Given Denmark's aggression, I'm considering minor increases to defense and mobilization, though they are already near maximum. I'm also evaluating the utility of further boosting Nuke and UseNuke.
            
            **Refining Flavor Allocation**
            
            My current thought process is focused on optimizing our strategic flavors. With "Flight" researched and Air at 100, the AI will prioritize air units. Science and Spaceship flavors are correctly maxed for our victory condition, and Diplomacy is high to counter Denmark. Espionage is also maxed, with spies actively gathering intel and rigging elections in key Danish cities.
            
            **Reassessing Spy Deployment**
            
            I'm reconsidering our extensive spy network within Denmark. Given our technological lead, tech theft is impossible. My focus is now on redirecting these assets, perhaps to city-states for election rigging, or to gather intel on their unit movements and strategic plots instead.
            
            **Setting Next Research**
            
            My immediate concern is setting our next research. While "Flight" was previously considered, the current available options are "Combustion," "Flight," and "Alternative Energy," indicating a slight shift. I will proceed with setting "Flight" as the next technology to research, aligning with our Science Victory path.
            
            **Setting Next Research**
            
            My current analysis indicates a critical need to establish our next research and policy queues. I will explicitly set "Flight" as the next technology and "Free Thought" as the next policy to ensure alignment with our Science Victory strategy, and then maintain our current optimized flavors and grand strategy.
            
            **Evaluating Ethical Dimensions**
            
            I am now considering the ethical implications of our high Nuke and UseNuke flavors. While powerful, I recognize the potential for catastrophic harm and am evaluating if these flavors are truly necessary for our Science Victory, or if they pose an unacceptable risk, prompting a need to re-evaluate their allocation.
            
            **Prioritizing Deterrence and Victory**
            
            My current focus is on solidifying our deterrence against Denmark's military might while ensuring our Science Victory. I've set "Flight" as the next research, crucial for defense and future advancements. "Free Thought" is slated as our next policy to maximize Great Scientist generation, bolstering our path to victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 2xDLG3Wx7DAy3riY
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: Following the completion of Replaceable Parts, Flight is the critical next technology. It unlocks Triplanes and Bombers to defend our borders against Denmark's massive army, and leads directly to Atomic Theory and Rocketry, which are essential milestones for our Spaceship grand strategy.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 0vlUHK6XfQOlSArq
          - toolName: set-policy
          - input:
            - Rationale: Free Thought is our priority policy to adopt in 5 turns. Its +33% Great Scientist generation rate and +25% instant yields from Great Scientists stack perfectly with Babylon's unique ability, maximizing our science output to rush critical late-game space victory technologies.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: DGhDzETW38mAtk68
          - toolName: keep-status-quo
          - input:
            - Rationale: The current Spaceship grand strategy and defensive-military flavors remain highly optimal. Our tech lead is strong, and we just entered a Golden Age, boosting our yields. We must maintain maximum Defense (100) and CityDefense (100) to withstand Danish aggression, while high Diplomacy (95) and Espionage (100) will support our city-state alliances and prepare us to defeat Denmark's upcoming Decolonization proposal in the World Congress.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 2xDLG3Wx7DAy3riY
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
          - toolCallId: 0vlUHK6XfQOlSArq
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: DGhDzETW38mAtk68
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.