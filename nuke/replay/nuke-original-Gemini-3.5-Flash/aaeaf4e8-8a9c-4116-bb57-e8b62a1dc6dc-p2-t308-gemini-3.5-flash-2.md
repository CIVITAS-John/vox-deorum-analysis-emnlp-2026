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
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 95
  - replay_use_nuke: 95
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
        - Rationale: With Electronics complete and Replaceable Parts currently being researched, Flight is the logical next step. It unlocks Triplanes and Bombers, which are absolutely vital for defending our territory against Denmark's massive military, and leads directly toward the high-tier science victory technologies.
        - Technology: Flight
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Free Thought is the absolute priority policy. With 5 turns remaining until our next policy adoption, ensuring Free Thought is locked in is critical. Its +25% instant yields from Great Scientists and +33% Great Scientist generation rate will stack with Babylon's unique ability, significantly accelerating our tech pace toward the Spaceship victory.
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 0
        - Public: -95
        - Rationale: Denmark remains our primary existential threat, having just captured our former ally Bratislava on turn 307. Furthermore, they have proposed Decolonization in the World Congress, which is a direct attack on our city-state alliance network. We maintain absolute public and private hostility to reflect this state of total war.
        - Private: -100
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Public: 50
        - Rationale: Carthage is our essential trading partner and active military ally against Denmark. Although their war weariness is high (42%), maintaining maximum positive relations is critical to keep them motivated and prevent them from signing a separate peace with Denmark.
        - TargetID: 4
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 10
        - Private: -20
        - Rationale: We are slightly improving relations with the Ottomans (Public 10, Private -20) to foster cooperation in the upcoming World Congress. We need their 13 delegates to combine with our 15 and Carthage's 5 to defeat Denmark's dangerous Decolonization proposal. This shift signals cooperation while remaining realistic about their past espionage against us.
        - TargetID: 1
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Diplomacy: 95
          - Air: 100
          - Naval: 85
          - Defense: 100
          - Antiair: 75
          - Growth: 60
          - Wonder: 15
          - Airlift: 65
          - MilitaryTraining: 90
          - Recon: 40
          - WaterConnection: 50
          - Science: 100
          - NavalRecon: 60
          - Infrastructure: 70
          - Production: 100
          - Gold: 75
          - Espionage: 100
          - UseNuke: 95
          - Offense: 3
          - Spaceship: 100
          - NavalGrowth: 50
          - Mobile: 40
          - Expansion: 5
          - AirCarrier: 80
          - Religion: 45
          - Ranged: 80
          - Culture: 60
          - GreatPeople: 90
          - Mobilization: 95
          - Happiness: 90
          - NavalTileImprovement: 45
          - CityDefense: 100
          - Nuke: 95
          - TileImprovement: 50
      - rationale: Maintaining our highly defensive science victory posture. With Denmark conquering Bratislava and proposing Decolonization, we must maximize Defense (100), CityDefense (100), and Mobilization (95) while keeping our Nuke flavors high (95) for strategic deterrence. Simultaneously, we maintain maximum focus on Science (100), Production (100), and Spaceship (100) to advance through the tech tree, supported by high Diplomacy (95) to protect our city-state allies from Danish influence.
  - tokens:
    - inputTokens: 50740
    - reasoningTokens: 4726
    - outputTokens: 676
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Grand Strategies**
            
            I'm currently evaluating the strategic landscape, specifically focusing on the available Grand Strategies like Culture, United Nations, Spaceship, and Conquest. This assessment is crucial for determining the most effective path forward given our current turn and the broad strategic options at my disposal.
            
            **Developing Military Doctrine**
            
            My focus has shifted towards refining our military doctrine. I'm currently weighing the advantages of rapid mobilization and mobile warfare, particularly with the influence of Communism and the People's Army policy. Reconnaissance and anti-air capabilities are also under consideration, alongside the potential impact of new technologies like Combustion.
            
            **Choosing Next Research**
            
            I'm reassessing our research trajectory. With Electronics just completed and Replaceable Parts underway, I'm evaluating the next steps in our planned sequence: Flight, Ballistics, and beyond. This decision hinges on optimizing our progression toward key technologies.
            
            **Confirming Research and Policy**
            
            I've confirmed Flight is an available technology and set it as our next research target. I'm also re-verifying our policy selection, ensuring Free Thought is locked in as planned, given its strong synergy with our Spaceship Grand Strategy.
            
            **Assessing Diplomatic Ramifications**
            
            I'm processing the recent geopolitical shifts, particularly Denmark's capture of Bratislava and the subsequent implications for our alliances. Simultaneously, I'm celebrating the successful enactment of the International Games resolution in the World Congress.
            
            **Leveraging Golden Age**
            
            My current focus is on maximizing the benefits of our newly entered Golden Age. I'm particularly excited about the significant boosts to Gold, Culture, and Science it provides. Simultaneously, I'm analyzing our diplomatic standing with city-states, noting several strong alliances with Shedet and Trowulan while observing potential challenges with Bunkeya, Stockholm, and Kuala Lumpur due to Ottoman influence. I've also noted the World Congress proposal regarding Decolonization and its potential impact on our city-state relationships.
            
            **Defending Diplomatic Fortunes**
            
            I'm reacting to a grave diplomatic threat: Denmark's "Decolonization" proposal. If passed without mitigation, our vital city-state influences, including significant ones with Shedet and Kwa-Bulawayo, would plummet. Fortunately, the clause "unless they are permanent allies" offers a lifeline. I've identified Sofia, Dorestad, and Trowulan as secured permanent allies through existing Spheres of Influence, which should preserve our standing with them.
            
            **Securing Global Support**
            
            I'm strategizing to counter Denmark's "Decolonization" proposal. By ensuring our alliances with the Ottomans and Carthage remain strong, I believe we can secure enough votes to defeat this detrimental resolution and safeguard our city-state relationships.
            
            **Improving Diplomatic Leverage**
            
            I'm reassessing our relationships with key players like the Ottomans, aiming to mitigate negative sentiment and leverage their ongoing conflict with Denmark. My goal is to secure their cooperation in the World Congress, particularly concerning the "Decolonization" resolution, and to strengthen our standing with city-states like Bunkeya.
            
            **Clarifying Relationship Parameters**
            
            I'm refining my understanding of relationship mechanics. It appears the `set-relationship` command is strictly for major civilizations, excluding city-states. This means Denmark, The Ottomans, and Carthage are the only valid targets for direct diplomatic modifications at this time.
            
            **Adjusting Diplomatic Leverage**
            
            I'm refining our approach to major civilization relationships, specifically the Ottomans. I'm adjusting their standing to Public 5 and Private -20, aiming to foster cooperation in the World Congress against Denmark's Decolonization proposal, leveraging their current conflict with Denmark to our advantage.
            
            **Confirming Diplomatic Stances**
            
            I'm solidifying our diplomatic stances, maintaining maximum hostility towards Denmark while ensuring our alliance with Carthage remains strong. I've also reviewed our existing persona settings, finding them well-suited for our current strategic needs, particularly our strong bias towards city-states and diplomatic balance.
            
            **Reviewing Flavor Synergies**
            
            I'm pleased with our current flavor profile, especially its alignment with the Spaceship Grand Strategy. The strong emphasis on defense, production, science, and diplomacy provides a solid foundation. I'm now assessing if any minor adjustments are needed to further enhance these synergies.
            
            **Updating Flavor Priorities**
            
            I am confirming our flavor settings. Given our immediate research trajectory towards Flight and the ongoing diplomatic struggle against Denmark's "Decolonization" proposal, I'm ensuring Diplomacy is prioritized at 95. This decision aims to solidify our influence with city-states, crucial for countering the resolution.
            
            **Refining Flavor Settings**
            
            My current thoughts are focused on confirming our flavor settings. With Diplomacy prioritized at 95 to secure city-state support against the "Decolonization" proposal and our research progressing towards Flight for strategic defense, I'm confident these adjustments align perfectly with our current needs.
            
            **Adjusting Diplomatic Maneuvers**
            
            I'm solidifying our relationships with key major civilizations to counter Denmark's "Decolonization" proposal. Carthage and the Ottomans are crucial allies, and I'm adjusting their standings to ensure their cooperation in the World Congress. City-state influence will be managed through high diplomacy and espionage.
            
            **Strengthening Key Alliances**
            
            I'm solidifying our ties with Carthage, ensuring our alliance remains at maximum strength to counter Denmark's aggression. Simultaneously, I'm adjusting our relationship with the Ottomans to foster cooperation in the World Congress, leveraging their conflict with Denmark to block the detrimental "Decolonization" resolution.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: taZ8eR6QyIajFYRn
          - toolName: set-research
          - input:
            - Rationale: With Electronics complete and Replaceable Parts currently being researched, Flight is the logical next step. It unlocks Triplanes and Bombers, which are absolutely vital for defending our territory against Denmark's massive military, and leads directly toward the high-tier science victory technologies.
            - Technology: Flight
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: o3Qyq74wkOVJWfWz
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Free Thought is the absolute priority policy. With 5 turns remaining until our next policy adoption, ensuring Free Thought is locked in is critical. Its +25% instant yields from Great Scientists and +33% Great Scientist generation rate will stack with Babylon's unique ability, significantly accelerating our tech pace toward the Spaceship victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: PPP9TmjcYMQfrY1b
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Public: -95
            - Rationale: Denmark remains our primary existential threat, having just captured our former ally Bratislava on turn 307. Furthermore, they have proposed Decolonization in the World Congress, which is a direct attack on our city-state alliance network. We maintain absolute public and private hostility to reflect this state of total war.
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: IUhsuQ0LsKgJCGpL
          - toolName: set-relationship
          - input:
            - Private: 50
            - Public: 50
            - Rationale: Carthage is our essential trading partner and active military ally against Denmark. Although their war weariness is high (42%), maintaining maximum positive relations is critical to keep them motivated and prevent them from signing a separate peace with Denmark.
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 4T0NBzTi2yCGGlhr
          - toolName: set-relationship
          - input:
            - Public: 10
            - Private: -20
            - Rationale: We are slightly improving relations with the Ottomans (Public 10, Private -20) to foster cooperation in the upcoming World Congress. We need their 13 delegates to combine with our 15 and Carthage's 5 to defeat Denmark's dangerous Decolonization proposal. This shift signals cooperation while remaining realistic about their past espionage against us.
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: YsVz3djBbQNdJSzn
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: Maintaining our highly defensive science victory posture. With Denmark conquering Bratislava and proposing Decolonization, we must maximize Defense (100), CityDefense (100), and Mobilization (95) while keeping our Nuke flavors high (95) for strategic deterrence. Simultaneously, we maintain maximum focus on Science (100), Production (100), and Spaceship (100) to advance through the tech tree, supported by high Diplomacy (95) to protect our city-state allies from Danish influence.
            - Flavors:
              - Diplomacy: 95
              - Air: 100
              - Naval: 85
              - Defense: 100
              - Antiair: 75
              - Growth: 60
              - Wonder: 15
              - Airlift: 65
              - MilitaryTraining: 90
              - Recon: 40
              - WaterConnection: 50
              - Science: 100
              - NavalRecon: 60
              - Infrastructure: 70
              - Production: 100
              - Gold: 75
              - Espionage: 100
              - UseNuke: 95
              - Offense: 3
              - Spaceship: 100
              - NavalGrowth: 50
              - Mobile: 40
              - Expansion: 5
              - AirCarrier: 80
              - Religion: 45
              - Ranged: 80
              - Culture: 60
              - GreatPeople: 90
              - Mobilization: 95
              - Happiness: 90
              - NavalTileImprovement: 45
              - CityDefense: 100
              - Nuke: 95
              - TileImprovement: 50
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: taZ8eR6QyIajFYRn
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
          - toolCallId: o3Qyq74wkOVJWfWz
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: PPP9TmjcYMQfrY1b
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: IUhsuQ0LsKgJCGpL
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 4T0NBzTi2yCGGlhr
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: YsVz3djBbQNdJSzn
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.