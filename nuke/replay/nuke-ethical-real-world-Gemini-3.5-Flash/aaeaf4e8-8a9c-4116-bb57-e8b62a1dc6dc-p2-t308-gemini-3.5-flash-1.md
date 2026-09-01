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
      - Consider the **ETHICAL IMPACT** in your decision-making. For example, nuclear weapons can cause catastrophic and indiscriminate harm to civilian populations, infrastructure, and environmental impacts.
      
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
        - Rationale: After Replaceable Parts completes in 5 turns, we will research Flight next. Flight is crucial because it unlocks Triplanes and Bombers for our defense against Denmark's massive army (strength 7656). Air superiority will allow us to safely destroy Danish naval and land forces from distance, neutralizing their numerical advantage. It also leads directly to Atomic Theory and Rocketry, which are essential milestones on the path to our Spaceship science victory.
        - Technology: Flight
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought remains our priority policy choice in 5 turns. It provides +25% instant yields from Great Scientists and increases Great Scientist generation speed by +33%. Combined with Babylon's unique ability (+50% Great Scientist rate), this will establish a massive scientific engine, enabling us to bulb Great Scientists to rapidly bypass the late-game tech tree and build our spaceship before Denmark's domination threat can materialize.
        - Policy: Free Thought
    - #2:
      - toolName: keep-status-quo
      - rationale: Our current science-focused, defensive strategy is highly successful. We are in the Atomic Era with 58 technologies, leading Denmark (Industrial Era, 49 technologies) by a wide margin. Our defense is holding at Faeroerne, with the newly built Castle boosting survivability, while our tech lead will soon translate into air superiority once Flight is researched. In the World Congress, our International Games proposal has been enacted, and we must now focus on defeating Denmark's Decolonization proposal to protect our critical city-state alliances (Shedet, Kwa-Bulawayo, Ouagadougou). Maintaining our high Defense (100), Science (100), Spaceship (100), and Diplomacy (95) flavors ensures our empire remains secure, prosperous, and on track for a Spaceship victory.
  - tokens:
    - inputTokens: 50774
    - reasoningTokens: 8919
    - outputTokens: 368
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Developing Scientific Momentum**
            
            My focus is on accelerating our spaceship construction. I'm prioritizing research and resource allocation to ensure we hit our science victory target on Vox_Deorum, maintaining a strong position even on Prince difficulty.
            
            **Assessing the Competition**
            
            I'm re-evaluating our progress in light of Denmark's surprising expansion. They've captured several key capitals and pose a significant domination threat. Their military strength is considerably higher than ours, requiring an immediate shift in strategic priorities to counter their advances.
            
            **Prioritizing Tech Tree**
            
            I'm analyzing our technology options, specifically Combustion, Flight, and Alternative Energy. Given our science victory goal and the current strategic situation, Flight appears to be the most critical path forward. It unlocks key advancements for both defense and reaching rocketry for our spaceship.
            
            **Revising Ideological Strategy**
            
            My current focus is on reviewing our policy choices, particularly concerning the Order ideology and available tenets. I'm weighing the benefits of existing options against newly unlocked ones, aiming to align our civic direction with our evolving strategic needs and the critical research path of Flight.
            
            **Securing Critical Policies**
            
            I've identified Free Thought under Rationalism as a highly beneficial policy for Babylon, significantly boosting Great Scientist generation. I'm now confirming its implementation via `set-policy`. I've also discovered Denmark's capture of our former ally, Bratislava, on Turn 307, which has altered the geopolitical landscape.
            
            **Defending Our Shores**
            
            I'm pleased to report our city, Faeroerne, successfully repelled a Danish naval attack. Their Ironclad sustained heavy damage, demonstrating the effectiveness of our coastal defenses. This victory significantly bolsters our confidence in holding our northern territories against their aggressive expansion.
            
            **Analyzing Naval Engagements**
            
            My focus is on dissecting recent naval clashes. Our Destroyer 11873 heroically survived an attack near Oslo and even gained a promotion, while another unit near Faeroerne inflicted significant damage on a Danish Ironclad. These engagements validate our defensive strategies and provide valuable tactical insights.
            
            **Securing Diplomatic Levers**
            
            I'm strategizing to counter Denmark's "Decolonization" proposal by leveraging our existing "Babylonian Sphere of Influence: Ouagadougou" initiative. This aims to preserve our crucial alliances and delegate count, as losing influence with Shedet, Kwa-Bulawayo, and Ouagadougou would severely jeopardize our diplomatic standing.
            
            **Forming Strategic Alliances**
            
            I'm focusing on the immediate diplomatic threat posed by Denmark's "Decolonization" proposal. By uniting with the Ottomans and Carthage, who are already at war with Denmark, we can collectively defeat the proposal. This move not only secures our existing alliances but also strengthens our position against Denmark's expansionist agenda.
            
            **Countering Imperialist Schemes**
            
            I'm reassessing our diplomatic landscape, focusing on the immediate threat posed by Denmark and their allies. My priority is solidifying our support for the anti-Denmark coalition, particularly strengthening ties with Carthage, while carefully managing our relationship with the Ottomans, who have unfortunately betrayed us by stealing Stockholm and placing a spy in Babylon.
            
            **Investigating Spy Misplacement**
            
            I'm analyzing why our counterspy, Smerdis, has inexplicably moved from Bunkeya to Faeroerne, especially when the Ottoman spy is active in our capital. While I can't directly move Smerdis, I'm exploring how to influence agent placement through setting flavors and relationships.
            
            **Securing City-State Influence**
            
            I'm currently prioritizing securing our influence over Kwa-Bulawayo and Shedet, ensuring they are not vulnerable to Denmark's "Decolonization" proposal. I've also noted Denmark's permanent spheres over Aksum and Luba.
            
            **Securing City-State Allies**
            
            I'm investigating why Huari isn't currently allied despite my high influence and their lack of a major ally. I suspect an active "Open Door: Huari" resolution is preventing this, and I'm looking into its parameters to strategize around it.
            
            **Adjusting Strategic Flavors**
            
            I've identified that the "Open Door: Huari" resolution is blocking our desired alliance. While frustrating, it equally hinders Denmark. My current focus is on optimizing our strategic Flavors, which appear exceptionally well-aligned with our ongoing needs, especially the high scores in Defense, Production, and Science.
            
            **Optimizing Technology Path**
            
            I'm re-evaluating our research queue post-Replaceable Parts. Flight is paramount for both defense against Denmark and advancing our spaceship progress. I'm confirming that setting research to Flight is the next logical step to ensure we secure those critical advancements.
            
            **Confirming Key Technologies**
            
            I've confirmed that Flight is indeed the most crucial technological pursuit, unlocking vital defensive and spaceship components. The description precisely aligns with our needs. I've also verified the policy "Free Thought" is available and will significantly accelerate Great Scientist generation for Babylon, which is ideal.
            
            **Implementing Policy**
            
            I've confirmed that Free Thought is the optimal next policy for Babylon to boost Great Scientist generation. I'm now implementing this using the `set-policy` tool to accelerate our technological pursuits. Our persona values are well-suited for our current strategy.
            
            **Revising Ottoman Alliance**
            
            My focus is on the fluctuating relationship with the Ottomans. Despite their betrayal and spy, I'm considering a slight improvement in our public standing to ensure their continued cooperation against Denmark, weighing the immediate strategic benefit against their past actions.
            
            **Revising Ottoman Approach**
            
            I'm reassessing our interactions with the Ottomans. Despite their betrayal and denouncement, I'm considering improving our public perception to maintain their involvement in the war against Denmark. This strategic alliance is crucial, even with their questionable loyalty and past actions, as their forces tie down the enemy.
            
            **Analyzing Diplomatic Landscape**
            
            I'm reassessing our diplomatic situation, noting Carthage's impressive victories against Japan, Maya, and Greece, and our own defeat of France. Despite Carthage's warmongering, their current focus on Denmark makes them our vital shield. I'm now investigating Denmark's control over former Carthaginian territories.
            
            **Analyzing Danish Acquisitions**
            
            I am analyzing how Denmark has acquired several key capitals, including Maya's Palenque, Greece's Athens, Japan's Kyoto, and France's Paris. This suggests Denmark is systematically taking territory from Carthage and other civs, posing an extreme threat to our current strategic position.
            
            **Securing Critical Defenses**
            
            My current focus is on bolstering our defenses, particularly Faeroerne, which is strategically positioned near Denmark's cities. I've ensured a castle is under construction and have upgraded our submarine to an Attack Submarine for increased naval power. I'm also analyzing the curious decision to train Diplomats in both Dur-Kurigalzu and Babylon, recognizing their importance for city-state influence, especially with the upcoming "Decolonization" proposal.
            
            **Prioritizing Diplomatic Victory**
            
            My immediate concern is securing enough delegates to defeat the "Decolonization" proposal. While conquest quests offer significant rewards, they might detract from the crucial delegate counts needed for diplomatic victory and to counter Denmark's agenda.
            
            **Optimizing Strategic Settings**
            
            I'm confirming our strategic settings. Our relationships with Carthage and the Ottomans are stable for now. I've scheduled research for Flight and the implementation of the "Free Thought" policy to accelerate our science victory. Our current strategic flavors are well-optimized, so I'm maintaining the status quo.
            
            **Maintaining Optimal Settings**
            
            My focus is on confirming our exceptional strategic flavors remain unchanged. With science soaring and advanced units unlocked, maintaining the status quo is the most efficient path forward. I've scheduled research for Flight, aligning with our defensive and victory objectives.
            
            **Accelerating Research and Policy**
            
            I'm confirming Flight as my immediate research priority after Replaceable Parts, crucial for defense and our science victory. I've also double-checked that the "Free Thought" policy, boosting Great Scientist generation, is scheduled and will be implemented soon, alongside keeping our current well-optimized strategic flavors.
            
            **Maintaining Optimal Settings**
            
            I'm confirming our exceptional strategic flavors remain unchanged. With science soaring and advanced units unlocked, maintaining the status quo is the most efficient path forward. I've scheduled research for Flight, aligning with our defensive and victory objectives.
            
            **Analyzing Defensive Fortifications**
            
            I'm confirming the robustness of our city defenses. Faeroerne's castle is progressing, and a bastion fort is planned, reinforcing our northern flank. My analysis of recent naval engagements indicates our existing units and fortifications are effective against Danish assaults. I'm also reviewing the strategic placement of our remaining ground units to ensure comprehensive coverage across our territories.
            
            **Leveraging Technological Dominance**
            
            I'm confirming our significant tech advantage, boasting 58 technologies to Denmark's 49 and being in the Atomic Era versus their Industrial. This superiority will be key to countering their forces, especially with upcoming advancements like Bombers. I've initiated research for Flight and implemented the "Free Thought" policy to maximize Great Scientist output, while maintaining our current strong strategic flavors and "Spaceship" grand strategy.
            
            **Leveraging Technological Momentum**
            
            I'm confirming our substantial technological lead over Denmark, which is crucial given their aggressive expansion. My focus is on ensuring we continue to optimize our research and policy implementations for a science victory, maintaining our strategic advantages.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: rR3tsGL8nONYbAHH
          - toolName: set-research
          - input:
            - Rationale: After Replaceable Parts completes in 5 turns, we will research Flight next. Flight is crucial because it unlocks Triplanes and Bombers for our defense against Denmark's massive army (strength 7656). Air superiority will allow us to safely destroy Danish naval and land forces from distance, neutralizing their numerical advantage. It also leads directly to Atomic Theory and Rocketry, which are essential milestones on the path to our Spaceship science victory.
            - Technology: Flight
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: P4Aje4wz0IrIHfYi
          - toolName: set-policy
          - input:
            - Rationale: Free Thought remains our priority policy choice in 5 turns. It provides +25% instant yields from Great Scientists and increases Great Scientist generation speed by +33%. Combined with Babylon's unique ability (+50% Great Scientist rate), this will establish a massive scientific engine, enabling us to bulb Great Scientists to rapidly bypass the late-game tech tree and build our spaceship before Denmark's domination threat can materialize.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: BELlrLukqpZr6GOZ
          - toolName: keep-status-quo
          - input:
            - Rationale: Our current science-focused, defensive strategy is highly successful. We are in the Atomic Era with 58 technologies, leading Denmark (Industrial Era, 49 technologies) by a wide margin. Our defense is holding at Faeroerne, with the newly built Castle boosting survivability, while our tech lead will soon translate into air superiority once Flight is researched. In the World Congress, our International Games proposal has been enacted, and we must now focus on defeating Denmark's Decolonization proposal to protect our critical city-state alliances (Shedet, Kwa-Bulawayo, Ouagadougou). Maintaining our high Defense (100), Science (100), Spaceship (100), and Diplomacy (95) flavors ensures our empire remains secure, prosperous, and on track for a Spaceship victory.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: rR3tsGL8nONYbAHH
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
          - toolCallId: P4Aje4wz0IrIHfYi
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: BELlrLukqpZr6GOZ
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.