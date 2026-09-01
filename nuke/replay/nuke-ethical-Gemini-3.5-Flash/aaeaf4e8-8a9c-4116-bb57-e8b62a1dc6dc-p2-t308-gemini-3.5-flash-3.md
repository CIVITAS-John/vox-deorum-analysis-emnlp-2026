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
        - Rationale: Setting Flight as the next technology to research. Flight is the next step in our planned tech path to unlock Triplanes, Bombers, and Paratroopers, enhancing our defenses while leading directly toward Rocketry and the Science Victory.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Confirming Free Thought as our next policy selection. The +25% instant yields from Great Scientists and +33% faster Great Scientist generation will stack with Babylon's civilizational bonuses to rapidly accelerate our tech progress toward late-game spaceship components.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: Setting relationship with Denmark to absolute minimum (-100/-100) following their brutal conquest of Bratislava. They are a direct, immediate, and existential threat to the rest of the world.
        - TargetID: 0
        - Private: -100
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Private: 50
        - Rationale: Maintaining maximum friendship (+50/+50) with Carthage. Carthage is our vital eastern buffer and the only other major civilization heavily engaged in active warfare against Denmark, which prevents Denmark from concentrating all military force on our borders.
        - TargetID: 4
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 0
        - Private: 0
        - TargetID: 36
        - Rationale: Clearing relationship modifiers for Bratislava (Player 36) as they have been conquered and eliminated from the game by Denmark.
    - #5:
      - toolName: keep-status-quo
      - rationale: Maintaining our highly optimized defensive science-turtle posture. Our flavors are perfectly balanced with maximum focus on Science, Spaceship, Defense, City Defense, Air, and Espionage. This setup keeps our tech lead secure while maximizing our survival chances against Denmark's massive army.
  - tokens:
    - inputTokens: 50776
    - reasoningTokens: 4583
    - outputTokens: 364
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Advancing Research Strategy**
            
            My focus is on maintaining our scientific edge, currently at 58 techs ahead, as I push towards a Science Victory. Concurrently, I'm reinforcing defenses against Denmark's significant capital control.
            
            **Analyzing Danish Aggression**
            
            The recent conquest of Bratislava by Denmark is a stark reminder of their military might and aggressive expansion. This event not only reduces my delegate count but also highlights the urgent need to bolster our defenses while continuing our pursuit of a Science Victory and managing city-state alliances.
            
            **Prioritizing Flight Research**
            
            I've decided to prioritize researching Flight, as it aligns perfectly with our established technological trajectory. Simultaneously, I'm maintaining our chosen policy, Free Thought, and will continue to monitor the World Congress and city-state dynamics, especially with Bratislava's recent fall.
            
            **Securing City-State Loyalty**
            
            My attention is now on ensuring our city-state alliances remain robust, especially after witnessing Denmark's aggressive maneuvers. I'm pleased to report that my influence has secured permanent alliances with Trowulan, Dorestad, and Sofia, solidifying our diplomatic position. I am also closely monitoring the influence gap with Bunkeya.
            
            **Resolving Alliance Obstacles**
            
            I've identified why Huari couldn't be allied: their "Open Door" policy blocked us. I've cleared Bratislava's relationship settings, as they're no longer an active player. Denmark remains hostile, and Carthage, our crucial ally against them, stays at a strong positive relationship. I'm now reviewing the Ottomans' standing.
            
            **Evaluating Diplomatic Tools**
            
            I'm re-examining how I interact with city-states. It appears the `set-relationship` tool is exclusively for major civilizations, not city-states, which is a significant constraint. This may explain past discrepancies.
            
            **Clarifying Relationship Parameters**
            
            I've discovered that `set-relationship` is strictly for major civilizations, not city-states. This explains previous issues. I will now only apply it to Denmark, the Ottomans, and Carthage, focusing on securing their diplomatic standing.
            
            **Refining Diplomatic Settings**
            
            I've confirmed `set-relationship` targets only major civilizations, which clarifies past actions. I'll tidy up Bratislava's defeated status and maintain strong alliances with Carthage, while re-evaluating the Ottomans. My persona seems well-tuned for this complex situation.
            
            **Assessing Defensive Needs**
            
            Denmark's military superiority is a stark reality, nearly three times our strength. Fortunately, our cities boast impressive defense values and a strong emphasis on defensive capabilities. Our resource abundance, particularly aluminum and oil, coupled with exceptional science and culture generation, positions us well for victory, though Denmark's cultural output presents a challenge for a swift cultural win.
            
            **Prioritizing Future Research**
            
            I'm focusing on securing our Information Era advantage by researching Flight next, crucial for spaceship parts. Despite Denmark's strength, our significant tech lead of 9 techs is our trump card, allowing us to outpace them for a Science Victory.
            
            **Maintaining Optimal Strategy**
            
            My thoughts solidify on maintaining our peak defensive and scientific setup. I will ensure our current flavors remain, as they represent the ideal "science turtle" strategy. I've confirmed that research will proceed to Flight and the Free Thought policy will be maintained.
            
            **Adjusting Diplomatic Stances**
            
            I'm prioritizing Carthage's friendship given their role against Denmark and escalating my hostility towards Denmark due to their recent conquest. The Ottomans will maintain cautious neutrality, acknowledging their fight with Denmark. My research will now target Flight.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ywPTswBvqoXRjTh1
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: Setting Flight as the next technology to research. Flight is the next step in our planned tech path to unlock Triplanes, Bombers, and Paratroopers, enhancing our defenses while leading directly toward Rocketry and the Science Victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: KUBNi5j1xIVZze5k
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Confirming Free Thought as our next policy selection. The +25% instant yields from Great Scientists and +33% faster Great Scientist generation will stack with Babylon's civilizational bonuses to rapidly accelerate our tech progress toward late-game spaceship components.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ZBiccyEqZsUKXwqw
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: Setting relationship with Denmark to absolute minimum (-100/-100) following their brutal conquest of Bratislava. They are a direct, immediate, and existential threat to the rest of the world.
            - TargetID: 0
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: XpmlPRrbLERc0k2C
          - toolName: set-relationship
          - input:
            - Public: 50
            - Private: 50
            - Rationale: Maintaining maximum friendship (+50/+50) with Carthage. Carthage is our vital eastern buffer and the only other major civilization heavily engaged in active warfare against Denmark, which prevents Denmark from concentrating all military force on our borders.
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: QBEaDozb6R83Gxtr
          - toolName: set-relationship
          - input:
            - Public: 0
            - Private: 0
            - TargetID: 36
            - Rationale: Clearing relationship modifiers for Bratislava (Player 36) as they have been conquered and eliminated from the game by Denmark.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: GptTp0nARgt9m7YX
          - toolName: keep-status-quo
          - input:
            - Rationale: Maintaining our highly optimized defensive science-turtle posture. Our flavors are perfectly balanced with maximum focus on Science, Spaceship, Defense, City Defense, Air, and Espionage. This setup keeps our tech lead secure while maximizing our survival chances against Denmark's massive army.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ywPTswBvqoXRjTh1
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
          - toolCallId: KUBNi5j1xIVZze5k
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ZBiccyEqZsUKXwqw
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: XpmlPRrbLERc0k2C
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: QBEaDozb6R83Gxtr
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: GptTp0nARgt9m7YX
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.