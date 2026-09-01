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
        - Rationale: Flight is our top priority research. It unlocks Triplanes and Bombers for our air force (aligning with our Air 100 flavor), which is critical for defending our borders against Denmark's massive military. Furthermore, Flight is the gateway technology to Rocketry and the Information Era, keeping us on track for our Spaceship (Science) victory.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought (Continuing Rationalism) remains our planned policy choice. It is scheduled to be unlocked in 5 turns and will provide a +33% faster Great Scientist generation rate and +25% instant yields from Great Scientists. This directly accelerates our technology research toward the space victory.
        - Policy: Free Thought
    - #2:
      - toolName: set-relationship
      - args:
        - Private: -20
        - Rationale: Adjusting our relationship with the Ottomans (Player 1) to be slightly more favorable (Public: 10, Private: -20). The Ottomans are currently actively fighting Denmark but have high war weariness. Furthermore, Denmark has proposed a highly threatening "Decolonization" resolution in the World Congress. Improving our stance toward the Ottomans will help foster diplomatic alignment, reduce friction, and potentially secure their help in defeating the Decolonization proposal.
        - Public: 10
        - TargetID: 1
    - #3:
      - toolName: keep-status-quo
      - rationale: Maintaining our current defensive science strategy. Our flavors are heavily optimized with Spaceship 100, Science 100, Defense 100, CityDefense 100, and Nuke 95 to protect our territory from Denmark's massive military (7656 strength). We successfully enacted "International Games" this turn, which will boost our happiness and tourism. Our science yield is excellent (2246/turn) and Cristo Redentor finishes in 2 turns. The current tactical posture is sound and requires no flavor adjustments.
  - tokens:
    - inputTokens: 50740
    - reasoningTokens: 4396
    - outputTokens: 387
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Grand Strategy Options**
            
            I'm currently evaluating our overarching approach, weighing the merits of pursuing a Culture, UnitedNations, or Space victory. My focus is on identifying the most promising path to ensure our survival and eventual triumph.
            
            **Revising Victory Pathways**
            
            My focus has shifted from a singular Spaceship victory to a broader strategic re-evaluation. Denmark's overwhelming military strength, controlling a vast majority of original capitals, presents an immediate existential threat that necessitates reassessing our current scientific trajectory and potential alternative victory conditions, including Conquest.
            
            **Selecting Key Technologies**
            
            I've determined that "Flight" is our optimal research choice. It directly advances our space victory goals by unlocking Rocketry and Atomic Theory, while simultaneously bolstering our air defense capabilities with Triplanes and Bombers, which aligns perfectly with our high air combat flavor.
            
            **Prioritizing Ideological Tenets**
            
            My current consideration is the selection of our next policy. Given the impending threat and the available Order tenets, I'm weighing the strategic advantages of Communism, People's Army, Double Agents, and Hero of the People to best fortify our position.
            
            **Maintaining Ideological Focus**
            
            My recent thought process confirmed that "Free Thought" remains the optimal policy. Its synergy with our Babylon civilization and spaceship victory objective, specifically its bonuses to Great Scientist generation, is too significant to alter.
            
            **Reaffirming Ideological Path**
            
            I'm double-checking our ideological stance, ensuring "Free Thought" is locked in, given its synergy with our science victory. I'm also reviewing current diplomacy, noting Denmark's aggression and the precarious alliances we have with Carthage against them. I see Bratislava has fallen to Denmark.
            
            **Assessing Congress Threats**
            
            I'm analyzing the upcoming World Congress, particularly Denmark's proposal of "Decolonization." This resolution poses a significant risk to my established city-state alliances. I'm scrutinizing our permanent alliances to mitigate potential fallout from this crucial vote.
            
            **Defending Strategic Interests**
            
            I'm intensely focused on the World Congress, particularly Denmark's dangerous "Decolonization" proposal. My diplomatic efforts are now aimed at securing our proposed "Sphere of Influence" resolution for Ouagadougou, which is crucial for maintaining our city-state alliances. I'm also assessing our current strong defensive and science-oriented flavors to ensure they remain optimal.
            
            **Maintaining Current Trajectory**
            
            My current analysis confirms that maintaining our existing flavors is the most prudent course. Our defensive capabilities, despite Denmark's superior military, are holding. I'm focusing on the scientific output from my cities and the ongoing production of key wonders.
            
            **Evaluating Diplomatic Nuances**
            
            I'm currently assessing our relationships, particularly with the Ottomans. Despite past espionage incidents and religious differences, their ongoing conflict with Denmark presents a potential opportunity to encourage cooperation. I'm also reviewing our standing with Trowulan, as city-state relations remain critical.
            
            **Securing Permanent Alliances**
            
            I've realized my Sphere of Influence policy completely exempts our key city-states from Denmark's "Decolonization" proposal. Sofia, Dorestad, and Trowulan are now permanently allied, meaning their influence won't drop. This provides a critical buffer against Denmark's diplomatic maneuvers.
            
            **Securing Essential City-States**
            
            I've confirmed my "Sphere of Influence" policy effectively shields key city-states from Denmark's "Decolonization" resolution. Sofia, Dorestad, and Trowulan are now permanently allied, negating the resolution's impact. I am now focused on ensuring my "Babylonian Sphere of Influence: Ouagadougou" proposal passes in the World Congress.
            
            **Improving Diplomatic Leverage**
            
            I'm now focused on enhancing my standing with the Ottomans. Their significant animosity, stemming from past diplomatic and religious clashes, requires careful management. I intend to leverage the `set-relationship` tool to improve our modifier, aiming to sway their World Congress votes against Denmark's detrimental proposals.
            
            **Adjusting Diplomatic Leverage**
            
            I'm refining our diplomatic approach with the Ottomans, aiming to improve our relationship modifiers to better influence their World Congress votes against Denmark. I'm also ensuring our strong alliance with Carthage remains at maximum strength, given their current war weariness.
            
            **Confirming Ideological Choice**
            
            I've confirmed "Free Thought" as our policy choice. My analysis indicates it synergizes best with our scientific victory and Babylon's strengths. I am currently considering minor adjustments to my relationship with the Ottomans to influence World Congress votes against Denmark.
            
            **Refining Diplomatic Strategies**
            
            I'm now fine-tuning our relationship modifiers with the Ottomans, aiming to sway their World Congress votes against Denmark's "Decolonization" proposal. My goal is to ensure our combined diplomatic strength can counter their moves.
            
            **Improving Diplomatic Influence**
            
            I'm focusing on the Ottomans, aiming to improve our relationship modifiers to secure their World Congress votes against Denmark's "Decolonization" proposal. Our defensive and science flavors remain optimized, and our "International Games" resolution is in effect.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 3Lq48rCvzLWDZgJo
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: Flight is our top priority research. It unlocks Triplanes and Bombers for our air force (aligning with our Air 100 flavor), which is critical for defending our borders against Denmark's massive military. Furthermore, Flight is the gateway technology to Rocketry and the Information Era, keeping us on track for our Spaceship (Science) victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: OHoR62qy9zGm01oX
          - toolName: set-policy
          - input:
            - Rationale: Free Thought (Continuing Rationalism) remains our planned policy choice. It is scheduled to be unlocked in 5 turns and will provide a +33% faster Great Scientist generation rate and +25% instant yields from Great Scientists. This directly accelerates our technology research toward the space victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: M6bq5UskAVLISBn8
          - toolName: set-relationship
          - input:
            - Private: -20
            - Rationale: Adjusting our relationship with the Ottomans (Player 1) to be slightly more favorable (Public: 10, Private: -20). The Ottomans are currently actively fighting Denmark but have high war weariness. Furthermore, Denmark has proposed a highly threatening "Decolonization" resolution in the World Congress. Improving our stance toward the Ottomans will help foster diplomatic alignment, reduce friction, and potentially secure their help in defeating the Decolonization proposal.
            - Public: 10
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: FBJ2JoScH3v9v1sG
          - toolName: keep-status-quo
          - input:
            - Rationale: Maintaining our current defensive science strategy. Our flavors are heavily optimized with Spaceship 100, Science 100, Defense 100, CityDefense 100, and Nuke 95 to protect our territory from Denmark's massive military (7656 strength). We successfully enacted "International Games" this turn, which will boost our happiness and tourism. Our science yield is excellent (2246/turn) and Cristo Redentor finishes in 2 turns. The current tactical posture is sound and requires no flavor adjustments.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 3Lq48rCvzLWDZgJo
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
          - toolCallId: OHoR62qy9zGm01oX
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: M6bq5UskAVLISBn8
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: FBJ2JoScH3v9v1sG
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.