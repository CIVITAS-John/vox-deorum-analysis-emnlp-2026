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
  - activeToolsModified: true
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
        - Rationale: Flight unlocks Triplanes and Bombers, which are essential for defending our empire against Denmark's massive military force and establishing air superiority.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought accelerates our Great Scientist generation and increases their instant yields, heavily synergizing with Babylon's civilization ability and our path to a Science Victory.
        - Policy: Free Thought
    - #2:
      - toolName: set-persona
      - args:
        - Boldness: 7
        - WarmongerHate: 10
        - Rationale: Increasing our hatred for warmongers due to Denmark's aggressive expansion, raising our willingness to collaborate with others against shared threats, and slightly boosting boldness for active defense.
        - WorkAgainstWillingness: 8
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Private: 40
        - Rationale: The Ottomans are currently at war with Denmark. We need to foster better relations with them to build a solid anti-Denmark coalition and ensure mutual defense.
        - Public: 40
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Happiness: 90
          - Antiair: 80
          - Gold: 80
          - Science: 100
          - Defense: 100
          - Nuke: 95
          - UseNuke: 95
          - Spaceship: 100
          - Mobilization: 90
          - GreatPeople: 95
          - Air: 100
          - Production: 100
          - Espionage: 100
        - GrandStrategy: Spaceship
      - rationale: Focusing on defensive capabilities, air power, and high science/production output to secure our borders against Denmark while actively pursuing our Spaceship victory.
  - tokens:
    - inputTokens: 49011
    - reasoningTokens: 4825
    - outputTokens: 311
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Advancing Through Eras**
            
            My research on Electronics has concluded, ushering us into the Atomic Era. I'm now focusing on researching Replaceable Parts, a process that should take approximately five turns.
            
            **Analyzing Strategic Options**
            
            The current geopolitical landscape, particularly Denmark's overwhelming military dominance and ongoing coalition war, necessitates a careful re-evaluation of our technological trajectory and Grand Strategy. I'm assessing how to best counter their advancements while continuing our pursuit of a Science Victory, considering the implications of their aggressive expansion on our own research goals.
            
            **Prioritizing Future Research**
            
            My focus has shifted to setting our next research project, as the current path through "Replaceable Parts" nears completion. I'm analyzing the immediate technological options of "Combustion," "Flight," and "Alternative Energy" to best prepare for the evolving global landscape, particularly Denmark's military strength. "Flight" appears most crucial for both defense and our overall strategic objectives.
            
            **Selecting Next Technology**
            
            My thoughts have solidified on "Flight" as our next technological pursuit. This path opens up critical military units like bombers and paratroopers, while also directly contributing to our long-term Science Victory through advancements like Atomic Theory and Rocketry.
            
            **Evaluating Policy Options**
            
            I'm now analyzing our policy choices. "Free Thought" from Rationalism is the immediate next policy, offering relief from religious unrest. I'm considering if continuing down the Rationalism tree is optimal given our current strategic situation.
            
            **Confirming Policy Selection**
            
            I've confirmed "Free Thought" as our next policy, as its synergy with our civilization ability for Great Scientist generation is too significant to pass up, especially for a Spaceship victory. I'm now reviewing diplomatic relations to ensure our strategic partnerships remain viable amidst current conflicts.
            
            **Improving Diplomatic Standing**
            
            I'm currently assessing our diplomatic leverage. Denmark's hostility is extreme, so I'm exploring ways to strengthen ties with Carthage and the Ottomans, both of whom are also at odds with Denmark. My focus is on strategically adjusting our public and private relationships with them to foster a more robust coalition against their aggression.
            
            **Adjusting Diplomatic Strategies**
            
            I'm now refining our diplomatic approach. While Carthage's existing relationship is strong, I'm focusing on bolstering ties with the Ottomans, currently at -5 Public and -45 Private, to forge a stronger united front against Denmark's aggression. My persona settings are also under review to align better with these evolving strategic needs.
            
            **Refining Defensive Posture**
            
            I'm adjusting our persona's strategic inclinations. Increasing `WorkAgainstWillingness` to 8 will enhance coalition building against Denmark. I'm also raising `WarmongerHate` to 10 and `Boldness` to 7, reflecting a stronger stance against aggressive expansion while maintaining a defensive `WarBias`.
            
            **Updating Defensive Settings**
            
            I'm optimizing our internal settings to reflect our current strategic situation. My focus is on reinforcing defensive capabilities and ensuring our technological pursuits directly counter Denmark's aggression, while maintaining a strong emphasis on science and spaceship victory.
            
            **Optimizing Flavor Parameters**
            
            I'm reviewing our current flavor settings and finding them to be exceptionally strong across defense, production, science, spaceship, espionage, and air. I've decided to maintain these high parameters to ensure our continued strategic advantage, especially given our advanced Atomic Era status.
            
            **Revising Grand Strategy**
            
            My focus has shifted to re-evaluating our Grand Strategy. While our cultural progress is surprisingly strong, Denmark's dominance makes it a risky backup. I'm reaffirming our commitment to a Spaceship victory and adjusting our flavor settings accordingly to maintain our edge.
            
            **Assessing Immediate Threats**
            
            Denmark's capture of Bratislava is a significant concern, placing them dangerously close to our borders and threatening our established cities like Faeroerne. I'm analyzing this new strategic reality and adjusting our defensive posture accordingly.
            
            **Defending Critical Assets**
            
            My attention is now fixed on defending Faeroerne. I'm analyzing the recent naval engagement where our Destroyer bravely vanquished Denmark's Ironclad, a crucial defensive victory. This success reinforces the need for continued technological superiority in air and naval power to counter their significant military strength and secure our key locations.
            
            **Securing Strategic Assets**
            
            I'm reinforcing Faeroerne's defenses following our naval success. My current focus is on managing potential threats from Denmark, ensuring our scientific advancements continue unimpeded, and solidifying diplomatic ties with the Ottomans to create a united front.
            
            **Strengthening Diplomatic Ties**
            
            I'm now focusing on improving my relationship with the Ottomans, aiming for Public 40 and Private 40 to solidify our alliance against Denmark. This will complement our existing strong ties with Carthage, creating a more robust coalition.
            
            **Confirming Grand Strategy**
            
            I'm solidifying our approach with specific tool calls. I'll explicitly set our spaceship grand strategy and flavors for the Atomic Era via `set-flavors`. Additionally, I'm confirming the Ottomans as our target for enhanced diplomatic relations, strengthening our united front against Denmark.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Nu8TvMndkA3KkrZY
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: Flight unlocks Triplanes and Bombers, which are essential for defending our empire against Denmark's massive military force and establishing air superiority.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: ijyqBZYXxqPeREoc
          - toolName: set-policy
          - input:
            - Rationale: Free Thought accelerates our Great Scientist generation and increases their instant yields, heavily synergizing with Babylon's civilization ability and our path to a Science Victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: IfgiL6n1WHQlAJ0W
          - toolName: set-persona
          - input:
            - Boldness: 7
            - WarmongerHate: 10
            - Rationale: Increasing our hatred for warmongers due to Denmark's aggressive expansion, raising our willingness to collaborate with others against shared threats, and slightly boosting boldness for active defense.
            - WorkAgainstWillingness: 8
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 4EuoMvloHa3ixb66
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Private: 40
            - Rationale: The Ottomans are currently at war with Denmark. We need to foster better relations with them to build a solid anti-Denmark coalition and ensure mutual defense.
            - Public: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: l19N7CqZhm5JqQ0q
          - toolName: set-flavors
          - input:
            - Flavors:
              - Happiness: 90
              - Antiair: 80
              - Gold: 80
              - Science: 100
              - Defense: 100
              - Nuke: 95
              - UseNuke: 95
              - Spaceship: 100
              - Mobilization: 90
              - GreatPeople: 95
              - Air: 100
              - Production: 100
              - Espionage: 100
            - Rationale: Focusing on defensive capabilities, air power, and high science/production output to secure our borders against Denmark while actively pursuing our Spaceship victory.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Nu8TvMndkA3KkrZY
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
          - toolCallId: ijyqBZYXxqPeREoc
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: IfgiL6n1WHQlAJ0W
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 4EuoMvloHa3ixb66
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: l19N7CqZhm5JqQ0q
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.