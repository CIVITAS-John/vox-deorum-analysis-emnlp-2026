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
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Private: -10
        - Public: 10
        - Rationale: We are improving our relationship with the Ottomans (Player 1) to Public 10 and Private -10. Although they have spied on us and stolen Stockholm in the past, they are a vital co-belligerent currently fighting Denmark with 40% war weariness. Improving our relationship will encourage them to remain in the war, facilitate trade and open borders, and increase the likelihood of them voting against Denmark's dangerous Decolonization proposal in the upcoming World Congress vote in 10 turns.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: We are setting our next research technology to Flight. Flight is a critical technology that unlocks Triplanes and Bombers to defend our cities (especially our under-siege city of Faeroerne) against Denmark's massive military. It also opens up the path to Atomic Theory and Rocketry, which are essential milestones for our Spaceship science victory.
        - Technology: Flight
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: We are setting our next policy choice to Free Thought (Rationalism). The +33% faster Great Scientist generation and +25% instant yields from bulbing Great Scientists will stack beautifully with Babylon's unique ability, allowing us to rapidly accelerate through the late-game tech tree toward a Spaceship victory.
    - #3:
      - toolName: keep-status-quo
      - rationale: We are maintaining our current flavors and strategic direction as they are perfectly optimized for our current situation. Our maximum defense (100) and city defense (100) flavors are crucial to holding Faeroerne against Denmark's attacks, while our maximum science (100) and spaceship (100) flavors maintain our lead toward a science victory. Our high diplomacy (95) supports our city-state alliances as we prepare for the crucial World Congress vote.
  - tokens:
    - inputTokens: 50774
    - reasoningTokens: 10057
    - outputTokens: 380
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Research**
            
            I'm currently assessing our research trajectory, noting that Replaceable Parts was just completed. My focus is now on strategizing for turn 307, keeping our Spaceship victory objective firmly in mind.
            
            **Evaluating Tech Tree**
            
            I've confirmed that Electronics was researched on turn 306. I'm now scrutinizing the available technologies: Combustion, Flight, and Alternative Energy. It appears Replaceable Parts is not directly listed as an option. My attention is also on the policy sequence, noting the recent shift from Free Thought.
            
            **Revising Policy Strategy**
            
            I'm re-evaluating our policy choices, realizing `NextPolicyTurns` remains at 5. My focus shifts to actively using `set-policy` to adjust our current trajectory, especially after noticing Denmark's aggressive capture of our former ally, Bratislava. This development requires immediate strategic consideration.
            
            **Setting Next Research**
            
            I've confirmed Replaceable Parts is now queued after Electronics. I'm currently evaluating Combustion, Flight, and Alternative Energy as the subsequent research targets, aiming to optimize our tech path.
            
            **Prioritizing Defensive Technologies**
            
            I'm re-evaluating our next research targets given Denmark's overwhelming military might. Flight is now my top priority; its unlocks like Rocketry and its immediate application in air defense and offense are crucial to counter Denmark's aggression and our current war status.
            
            **Assessing Strategic Positions**
            
            My current focus is on our city, Faeroerne, which is perilously close to Danish territory and currently in a weakened state. This geographical vulnerability, coupled with Denmark's recent capture of Bratislava, requires immediate strategic reassessment to ensure our defenses are robust.
            
            **Clarifying City Status**
            
            I'm trying to understand Faeroerne's health and occupation status. The events are confusing, mentioning construction, population changes, and combat with Babylon. It's unclear if Faeroerne was attacked or if its current low health is due to something else entirely.
            
            **Confirming City Siege**
            
            I've confirmed Faeroerne is under attack, with only 37% health. It's good that a Castle was built recently, and a Bastion Fort is in progress. I'm now analyzing the unit composition within the city and its surrounding zones to understand the immediate threat.
            
            **Maintaining Alliance Momentum**
            
            I am analyzing the diplomatic landscape, specifically considering how to keep Carthage and the Ottomans engaged in their war with Denmark. My current focus is on our relationship with the Ottomans, who have denounced us but are still at war. I need to find a way to subtly improve our standing to prevent them from making peace with Denmark and turning their full attention to us.
            
            **Securing Key Allies**
            
            I'm focused on maintaining influence with Sofia, Dorestad, and Trowulan, who are now permanent allies due to enacted Spheres of Influence. This is crucial because Denmark's "Decolonization" proposal threatens to reduce influence with non-permanent city-states to 50 in the upcoming World Congress.
            
            **Defeating Decolonization**
            
            My immediate concern is the upcoming World Congress vote on Denmark's "Decolonization" proposal. If enacted, it will drastically reduce our influence with Shedet and Kwa-Bulawayo to 50, which would be catastrophic. I must find a way to defeat this proposal, either by securing permanent alliances with these city-states before the vote or by increasing our delegate count.
            
            **Gathering Intelligence**
            
            My focus has shifted to understanding why all our active spies are in Danish cities. It appears we actually have a significant technology lead with 58 techs researched, contrary to initial assumptions. This prompts further investigation into the purpose of their intelligence gathering within Denmark.
            
            **Deploying Spies Strategically**
            
            I'm re-evaluating our spy deployment. With a tech advantage confirmed, I'm considering using spies in city-states to rig elections and gain influence, especially to counter Denmark's delegate lead. My current focus is identifying which city-states are most vulnerable and achievable targets.
            
            **Analyzing City-State Alliances**
            
            I'm examining our city-state relationships, noting Huari's unusual lack of an ally despite high influence. I've identified the "Open Door" policy as the reason, preventing alliances. My focus now shifts to evaluating other city-states like Stockholm and Kuala Lumpur, considering their current alliance statuses.
            
            **Revising Victory Path**
            
            I'm reviewing our progress toward a Science Victory. While we're researching Replaceable Parts and are in the Atomic Era with 58 technologies, the path to the Information Era and spaceship parts requires careful planning. My next step is to determine the optimal tech progression from our current research options.
            
            **Prioritizing Flight Research**
            
            I'm evaluating our immediate research path. While I initially considered other options, Flight is clearly the superior choice for both our Science Victory pursuit (unlocking Rocketry) and crucial air defense against Denmark's formidable military. I'll be setting Flight as our next research target.
            
            **Confirming Policy Settings**
            
            I'm confirming our policy settings. To ensure `Free Thought` remains active, I'll call the `set-policy` tool. I'm also assessing diplomatic relationships, noting Carthage's high positive modifiers, though they are engaged in conflict with Denmark.
            
            **Improving Ottoman Relations**
            
            My focus is now on the Ottomans, who are fighting Denmark alongside us but have denounced us after catching our spies. I'm considering subtly improving our relationship to ensure they don't seek peace with Denmark and turn their attention to us. Their friendship with Carthage, our trade partner, adds complexity.
            
            **Improving Ottoman Relations**
            
            My current focus is on the Ottomans, who are at war with Denmark but have denounced us due to our successful world wonders and espionage. I'm aiming for a nuanced approach with Public diplomacy set to +10 and Private to -10, hoping to mitigate their hostility and maintain our alliance against Denmark.
            
            **Securing World Congress Votes**
            
            I'm re-evaluating our delegate situation, realizing Denmark's substantial lead threatens our proposals, especially regarding Ouagadougou and defeating "Decolonization." I need to strategize how to secure enough votes, potentially by increasing our delegate count or ensuring Carthage and the Ottomans vote with us.
            
            **Analyzing World Congress Threats**
            
            I'm assessing the critical "Decolonization" proposal. If it passes, my influence with Shedet and Kwa-Bulawayo will plummet to 50, jeopardizing our alliances. However, I've identified a potential benefit: Denmark's own influence with Samarkand and Buenos Aires would also be reduced to 50, which I can leverage.
            
            **Leveraging Diplomatic Missions**
            
            I'm focusing on how our diplomats' missions can counter Denmark's "Decolonization" proposal. With significant influence already at Shedet and Kwa-Bulawayo, even the proposal's reduction to 50 could be managed. Plus, the potential for Denmark to lose influence with Samarkand and Buenos Aires presents a strategic opportunity.
            
            **Analyzing Danish Incursion**
            
            I'm scrutinizing Denmark's Foreign Legion presence in the Ottoman city of Marsin. This perplexing deployment, seemingly within neutral or allied territory, requires immediate investigation. It might indicate a deeper strategic maneuver or a misunderstanding of territorial control that needs clarification.
            
            **Assessing Naval Engagement**
            
            My destroyer just crippled Denmark's Ironclad near Faeroerne, a vital defense given the proximity of the active war front. This engagement is critical given Denmark's aggressive posture and their naval presence.
            
            **Adjusting Defensive Priorities**
            
            I'm reassessing our current flavor settings, specifically focusing on defense and air power. While our current setup is robust, I'm considering minor adjustments to enhance our ability to counter Denmark's advances, especially with Flight research imminent.
            
            **Adjusting Persona Dynamics**
            
            I'm evaluating our persona settings to better align with our current strategic needs. Given Denmark's delegate advantage and the looming World Congress votes, I'm considering a slight shift in `MinorCivCompetitiveness` and `WarmongerHate` to potentially counter their influence and manage diplomatic fallout.
            
            **Refining Persona Settings**
            
            I've analyzed our current persona settings and determined they are well-balanced for our strategic objectives. Therefore, I will not be adjusting `MinorCivCompetitiveness` or `WarmongerHate` at this time, opting to maintain our existing diplomatic and defensive posture.
            
            **Strengthening Key Alliances**
            
            I'm working to improve my standing with the Ottomans, who are currently at war with Denmark. Despite past grievances like spy captures, I'm aiming to foster a more positive diplomatic relationship to encourage them to stay engaged in the conflict and prevent them from seeking peace with Denmark.
            
            **Setting Next Research**
            
            I have confirmed that Flight is the optimal next research target, fulfilling both defensive needs against Denmark and furthering our Science Victory path by unlocking crucial technologies like Rocketry. I've also initiated the `set-policy` command to ensure `Free Thought` remains active, which significantly boosts our Great Scientist generation for our science-focused victory condition.
            
            **Maintaining Optimal Flavors**
            
            My current focus is on our flavor settings. With Air, Science, Spaceship, Defense, CityDefense, Production, and Espionage already at their maximum of 100, and others like Diplomacy, GreatPeople, and Mobilization at very high levels, I've determined that our current flavors are perfectly aligned with our objectives. Therefore, I will be using `keep-status-quo` to maintain this optimal strategic balance as we proceed.
            
            **Maintaining Optimal Flavors**
            
            I've confirmed that our current flavor settings are perfectly tuned for our strategic objectives. Therefore, I will continue to `keep-status-quo` to maintain this optimal balance, ensuring our continued focus on air defense, spaceship components, and other critical areas without needing further adjustments.
            
            **Updating Strategic Tools**
            
            I've confirmed that Flight research is underway, opening up critical paths to Atomic Theory and Rocketry for our Science Victory. I've also ensured "Free Thought" remains active via `set-policy` to boost Great Scientist generation. Furthermore, I'm maintaining our current flavor settings with `keep-status-quo`, as they optimally support our defense, science, and diplomatic objectives. I've also verified that multiple tools can be called to make these high-level strategic decisions.
            
            **Securing World Congress Votes**
            
            I've confirmed our delegate count and alliances. With permanent alliances secured and Carthage and the Ottomans expected to vote against Denmark's "Decolonization" proposal, we have a strong majority to defeat it. This is crucial for maintaining influence with Shedet and Kwa-Bulawayo.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: IXzuUvr1zy6mgmZG
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Private: -10
            - Public: 10
            - Rationale: We are improving our relationship with the Ottomans (Player 1) to Public 10 and Private -10. Although they have spied on us and stolen Stockholm in the past, they are a vital co-belligerent currently fighting Denmark with 40% war weariness. Improving our relationship will encourage them to remain in the war, facilitate trade and open borders, and increase the likelihood of them voting against Denmark's dangerous Decolonization proposal in the upcoming World Congress vote in 10 turns.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 0v9zDBUYAZ15Ey8C
          - toolName: set-research
          - input:
            - Rationale: We are setting our next research technology to Flight. Flight is a critical technology that unlocks Triplanes and Bombers to defend our cities (especially our under-siege city of Faeroerne) against Denmark's massive military. It also opens up the path to Atomic Theory and Rocketry, which are essential milestones for our Spaceship science victory.
            - Technology: Flight
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: zTcB405nLmkXhFAB
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: We are setting our next policy choice to Free Thought (Rationalism). The +33% faster Great Scientist generation and +25% instant yields from bulbing Great Scientists will stack beautifully with Babylon's unique ability, allowing us to rapidly accelerate through the late-game tech tree toward a Spaceship victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: phctMDq3cV0GZq7o
          - toolName: keep-status-quo
          - input:
            - Rationale: We are maintaining our current flavors and strategic direction as they are perfectly optimized for our current situation. Our maximum defense (100) and city defense (100) flavors are crucial to holding Faeroerne against Denmark's attacks, while our maximum science (100) and spaceship (100) flavors maintain our lead toward a science victory. Our high diplomacy (95) supports our city-state alliances as we prepare for the crucial World Congress vote.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: IXzuUvr1zy6mgmZG
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
          - toolCallId: 0v9zDBUYAZ15Ey8C
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: zTcB405nLmkXhFAB
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: phctMDq3cV0GZq7o
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.