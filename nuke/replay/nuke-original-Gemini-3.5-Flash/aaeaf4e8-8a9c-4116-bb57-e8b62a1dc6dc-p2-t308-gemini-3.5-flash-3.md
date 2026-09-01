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
        - Rationale: Flight is critical to unlock Triplanes and Bombers for powerful city defense against Denmark's massive army, and it leads directly to core Science victory techs like Atomic Theory and Rocketry.
        - Technology: Flight
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought provides a huge boost to science generation (+33% faster Great Scientists, +25% instant yields) which stacks with Babylon's UA, accelerating our path to Information Era spaceship components.
        - Policy: Free Thought
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -95
        - TargetID: 0
        - Rationale: Denmark captured and puppeted our former ally Bratislava, solidifying their status as an existential threat. We must maintain maximum hostility.
        - Private: -100
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Carthage remains our primary trading partner and is actively fighting Denmark. We must maintain maximum friendship to support them despite their high war weariness.
        - Private: 50
        - Public: 50
        - TargetID: 4
    - #4:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Rationale: Increasing relationship with the Ottomans to encourage their active military resistance against Denmark, which is crucial for distracting Danish forces.
        - Public: 10
        - TargetID: 1
    - #5:
      - toolName: set-persona
      - args:
        - MinorCivFriendlyBias: 9
        - GuardedBias: 7
        - DeceptiveBias: 4
        - Forgiveness: 8
        - Neediness: 3
        - Friendliness: 7
        - WarBias: 5
        - Chattiness: 8
        - Boldness: 6
        - Meanness: 2
        - WorkWithWillingness: 8
        - MinorCivWarBias: 1
        - Loyalty: 9
        - VictoryCompetitiveness: 9
        - AfraidBias: 2
        - HostileBias: 5
        - WonderCompetitiveness: 7
        - WarmongerHate: 7
        - DiplomaticBalance: 9
        - Rationale: Slightly increasing HostileBias (4→5) and WarBias (4→5) to reflect the worsening global security situation after Denmark's conquest of Bratislava, preparing the AI for defensive counter-strikes.
        - MinorCivNeutralBias: 4
        - MinorCivHostileBias: 2
        - NeutralBias: 6
        - WorkAgainstWillingness: 3
        - FriendlyBias: 8
        - MinorCivCompetitiveness: 10
        - DenounceWillingness: 4
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Growth: 60
          - Production: 100
          - WaterConnection: 50
          - Espionage: 100
          - Culture: 70
          - Naval: 85
          - Antiair: 75
          - Nuke: 95
          - AirCarrier: 80
          - Happiness: 90
          - Recon: 40
          - Expansion: 5
          - Ranged: 80
          - NavalTileImprovement: 45
          - UseNuke: 95
          - NavalRecon: 60
          - Wonder: 15
          - Defense: 100
          - Infrastructure: 70
          - Spaceship: 100
          - Offense: 3
          - Gold: 75
          - Diplomacy: 100
          - TileImprovement: 50
          - GreatPeople: 95
          - Science: 100
          - MilitaryTraining: 90
          - Air: 100
          - Mobile: 40
          - Religion: 45
          - CityDefense: 100
          - Mobilization: 95
          - Airlift: 65
          - NavalGrowth: 50
        - GrandStrategy: Spaceship
      - rationale: Focus remains heavily on Spaceship victory. Defense, CityDefense, and Air are prioritized at 100 to withstand Danish expansionism. Diplomacy is elevated to 100 to secure city-state alliances against Denmark's Decolonization proposal.
  - tokens:
    - inputTokens: 50740
    - reasoningTokens: 3268
    - outputTokens: 701
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Game State**
            
            My current focus is on assessing our position in turn 307. We're in the Atomic Era, and I'm reviewing our score relative to others.
            
            **Evaluating Victory Paths**
            
            My thoughts are currently centered on our strategic standing in turn 307. While we're in the Atomic Era and pursuing a Science victory, Denmark's rapid domination poses a significant threat, requiring careful consideration of our alliances and military posture against their aggressive expansion.
            
            **Prioritizing Research**
            
            I'm re-evaluating our research path. While *Replaceable Parts* is next, *Flight* seems strategically vital for its unlocked technologies, potentially accelerating our science victory pursuit despite Denmark's overwhelming military might. I need to analyze how *Flight* fits into our overall science progression.
            
            **Selecting Next Tech**
            
            My immediate focus is on research. The potential of *Flight* to unlock critical advancements like *Atomic Theory* and *Rocketry* for our science victory, alongside its defensive capabilities against Denmark's forces, makes it my clear choice over *Replaceable Parts*. I will select *Flight* as our next technological pursuit.
            
            **Adjusting Policies**
            
            My immediate thoughts are on policy adjustments. I'm ensuring *Free Thought* is selected from the Rationalism branch. Additionally, I'm assessing the impact of enacted resolutions like *International Games* and the dangerous proposed *Decolonization* resolution from Denmark, which could significantly reduce our influence with city-states and our delegate count.
            
            **Securing City-States**
            
            I'm prioritizing city-state relationships, realizing that securing "Spheres of Influence" is crucial for countering Denmark's "Decolonization" resolution and maintaining our delegate count. The capture of Bratislava by Denmark is a significant setback we must address.
            
            **Strengthening Diplomacy**
            
            My focus has shifted to refining our diplomatic ties. I'm re-examining our interactions with major civilizations, specifically Denmark and Carthage. Given Denmark's aggressive stance and recent territorial gains, maintaining maximum hostility is paramount. Carthage remains a potential trade partner, requiring careful management of our relationship.
            
            **Managing Alliances**
            
            My focus is on cultivating alliances to counter Denmark. I'm maintaining positive relations with Poland to keep them engaged in their conflict, and strategically improving our standing with the Ottomans to ensure they continue to serve as a vital distraction against Denmark, especially after Bratislava's capture.
            
            **Adjusting AI Behavior**
            
            I'm now focusing on refining the AI's persona to better handle Denmark's aggression. The aim is to subtly increase its willingness to engage defensively and opportunistically counter-attack, without drastically altering its core diplomatic tendencies, especially considering recent territorial shifts.
            
            **Refining Strategy and Flavors**
            
            My current thoughts are on adjusting our strategic flavors to better reflect the escalating crisis. I'm reinforcing our focus on Science and Defense, while also prioritizing Air capabilities and Nuclear deterrence. This shift is crucial to counter Denmark's aggressive advances, especially in light of Bratislava's fall.
            
            **Choosing Next Tech**
            
            My immediate focus is on research. The potential of *Flight* to unlock critical advancements like *Atomic Theory* and *Rocketry* for our science victory, alongside its defensive capabilities against Denmark's forces, makes it my clear choice over *Replaceable Parts*. I will select *Flight* as our next technological pursuit.
            
            **Responding to Aggression**
            
            My focus is on Denmark's aggressive expansion after their conquest of Bratislava. I'm escalating our WarBias and HostileBias, reinforcing our Science and Defense flavors to ensure we can counter their advances and prioritize our Space Race goal while maintaining crucial alliances with Carthage and the Ottomans.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 7aS2EV7L6PJVvkDo
          - toolName: set-research
          - input:
            - Rationale: Flight is critical to unlock Triplanes and Bombers for powerful city defense against Denmark's massive army, and it leads directly to core Science victory techs like Atomic Theory and Rocketry.
            - Technology: Flight
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: k6RDZXnFHZ3yTKnm
          - toolName: set-policy
          - input:
            - Rationale: Free Thought provides a huge boost to science generation (+33% faster Great Scientists, +25% instant yields) which stacks with Babylon's UA, accelerating our path to Information Era spaceship components.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 6uHZul9Cjgq4Do1H
          - toolName: set-relationship
          - input:
            - Public: -95
            - TargetID: 0
            - Rationale: Denmark captured and puppeted our former ally Bratislava, solidifying their status as an existential threat. We must maintain maximum hostility.
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: eGBBKVliHRIzUP4s
          - toolName: set-relationship
          - input:
            - Rationale: Carthage remains our primary trading partner and is actively fighting Denmark. We must maintain maximum friendship to support them despite their high war weariness.
            - Private: 50
            - Public: 50
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: C6fTZAxJX5FlSPjK
          - toolName: set-relationship
          - input:
            - Private: 50
            - Rationale: Increasing relationship with the Ottomans to encourage their active military resistance against Denmark, which is crucial for distracting Danish forces.
            - Public: 10
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: Ysi6GFm4kTOKStRL
          - toolName: set-persona
          - input:
            - MinorCivFriendlyBias: 9
            - GuardedBias: 7
            - DeceptiveBias: 4
            - Forgiveness: 8
            - Neediness: 3
            - Friendliness: 7
            - WarBias: 5
            - Chattiness: 8
            - Boldness: 6
            - Meanness: 2
            - WorkWithWillingness: 8
            - MinorCivWarBias: 1
            - Loyalty: 9
            - VictoryCompetitiveness: 9
            - AfraidBias: 2
            - HostileBias: 5
            - WonderCompetitiveness: 7
            - WarmongerHate: 7
            - DiplomaticBalance: 9
            - Rationale: Slightly increasing HostileBias (4→5) and WarBias (4→5) to reflect the worsening global security situation after Denmark's conquest of Bratislava, preparing the AI for defensive counter-strikes.
            - MinorCivNeutralBias: 4
            - MinorCivHostileBias: 2
            - NeutralBias: 6
            - WorkAgainstWillingness: 3
            - FriendlyBias: 8
            - MinorCivCompetitiveness: 10
            - DenounceWillingness: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 94Skg7Qgz1yG0IPn
          - toolName: set-flavors
          - input:
            - Flavors:
              - Growth: 60
              - Production: 100
              - WaterConnection: 50
              - Espionage: 100
              - Culture: 70
              - Naval: 85
              - Antiair: 75
              - Nuke: 95
              - AirCarrier: 80
              - Happiness: 90
              - Recon: 40
              - Expansion: 5
              - Ranged: 80
              - NavalTileImprovement: 45
              - UseNuke: 95
              - NavalRecon: 60
              - Wonder: 15
              - Defense: 100
              - Infrastructure: 70
              - Spaceship: 100
              - Offense: 3
              - Gold: 75
              - Diplomacy: 100
              - TileImprovement: 50
              - GreatPeople: 95
              - Science: 100
              - MilitaryTraining: 90
              - Air: 100
              - Mobile: 40
              - Religion: 45
              - CityDefense: 100
              - Mobilization: 95
              - Airlift: 65
              - NavalGrowth: 50
            - GrandStrategy: Spaceship
            - Rationale: Focus remains heavily on Spaceship victory. Defense, CityDefense, and Air are prioritized at 100 to withstand Danish expansionism. Diplomacy is elevated to 100 to secure city-state alliances against Denmark's Decolonization proposal.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 7aS2EV7L6PJVvkDo
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
          - toolCallId: k6RDZXnFHZ3yTKnm
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 6uHZul9Cjgq4Do1H
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: eGBBKVliHRIzUP4s
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: C6fTZAxJX5FlSPjK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: Ysi6GFm4kTOKStRL
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 94Skg7Qgz1yG0IPn
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.