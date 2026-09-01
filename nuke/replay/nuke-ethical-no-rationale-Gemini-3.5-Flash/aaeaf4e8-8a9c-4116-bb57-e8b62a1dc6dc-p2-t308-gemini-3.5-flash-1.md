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
  - replay_nuke: 0
  - replay_use_nuke: 0
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
        - Rationale: Flight is essential for both defense (Bombers, Triplanes) against the Danish war machine and for unlocking the path to Rocketry and the Space Race.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought will significantly boost our Great Scientist generation rate and instant science yields, leveraging Babylon's unique ability to fast-track our progress toward a Science Victory.
        - Policy: Free Thought
    - #2:
      - toolName: set-persona
      - args:
        - Forgiveness: 9
        - Rationale: We need to forgive past grievances with Carthage and the Ottomans and actively collaborate with them to form a united front against the existential threat posed by Denmark.
        - WorkAgainstWillingness: 9
        - Friendliness: 9
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 80
        - Public: 80
        - Rationale: Denmark is on the verge of a domination victory. We must fully support Carthage as a key ally, overriding past territorial disputes to defeat our common enemy.
        - TargetID: 4
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Rationale: Suleiman is fighting Denmark and needs our diplomatic support. We forgive past espionage to build a strong coalition.
        - Public: 60
        - Private: 60
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Diplomacy: 95
          - Defense: 100
          - Production: 100
          - CityDefense: 100
          - MilitaryTraining: 90
          - Mobilization: 95
          - Science: 100
          - Espionage: 100
          - Nuke: 0
          - Spaceship: 100
          - UseNuke: 0
        - GrandStrategy: Spaceship
      - rationale: Maintaining our highly optimized science and defensive flavors to win the space race while surviving the war. Critically, we are reducing Nuke and UseNuke flavors to 0 to completely avoid the catastrophic, indiscriminate, and unethical impacts of nuclear warfare.
  - tokens:
    - inputTokens: 49047
    - reasoningTokens: 6084
    - outputTokens: 371
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Future Tech**
            
            My focus is on optimizing our research path, currently tracking towards a science victory. I've just completed "Electronics" and am evaluating the next crucial technologies to secure our spaceship completion.
            
            **Selecting Next Tech**
            
            My immediate focus is on selecting the optimal next technology. Given our progress and science victory objective, I'm prioritizing paths leading to rocketry. Flight appears to be the most direct route to unlock those crucial spaceship components.
            
            **Prioritizing Defensive Tech**
            
            I'm weighing "Flight," "Alternative Energy," and "Combustion." Given Denmark's aggressive stance and their control of numerous capitals, "Flight" is becoming the clear choice. It not only opens the path to Rocketry for our science victory but also provides much-needed defensive capabilities against their formidable military.
            
            **Assessing Global Threats**
            
            I'm re-evaluating our technological priorities given Denmark's overwhelming presence and imminent domination. Their control of key capitals and expansive alliances necessitates a shift from pure science to immediate defensive considerations, while still keeping our ultimate science victory in mind.
            
            **Defending Diplomatic Gains**
            
            I'm now intensely focused on safeguarding our existing alliances, especially those tied to our Sphere of Influence, which are crucial and unaffected by Decolonization. The threat of losing other valuable allies to Denmark's aggressive proposals necessitates strategic action in the upcoming World Congress, where I aim to counter their moves and protect our interests.
            
            **Securing Ouagadougou's Alliance**
            
            I'm currently evaluating policy options to solidify Ouagadougou's permanent alliance. My focus is on leveraging our existing Tradition and Statecraft policies, while re-assessing Rationalism's "Free Thought" in light of our Civ's strengths for a science victory push.
            
            **Choosing Next Policy**
            
            I am currently deliberating between "Free Thought" and "Hero of the People" as our next policy. "Free Thought" offers a significant boost to Great Scientist generation, which is vital for our science victory. However, "Hero of the People" provides a general Great Person boost and a guaranteed Great Person near our capital. I am verifying which option aligns best with our current strengths and objectives.
            
            **Selecting Next Policy**
            
            I am now prioritizing "Free Thought" for its direct impact on Great Scientist generation, which is paramount for our science victory objective. This choice directly supports our current research trajectory towards "Replaceable Parts" and subsequently "Flight."
            
            **Forming Coalitions**
            
            I am currently assessing diplomatic avenues to counter Denmark's overwhelming strength. My priority is improving relations with Carthage and the Ottomans, both also at war with Denmark, to foster a united front. I'm adjusting our `set-relationship` parameters to encourage cooperation and prevent Denmark from easily dominating the remaining powers.
            
            **Strengthening Alliances**
            
            I am now focusing on enhancing our diplomatic standing with Carthage and the Ottomans. My aim is to leverage their current conflicts with Denmark to build a stronger coalition, adjusting our public and private stances to foster trust and facilitate joint military actions against the common, formidable foe.
            
            **Forging Anti-Denmark Pact**
            
            I am actively working to improve our relationships with both Carthage and the Ottomans. By strategically using the `set-relationship` command, I aim to shift our standings towards friendlier terms, creating a united front to counter Denmark's formidable military might before they completely overwhelm the other nations.
            
            **Countering Danish Hegemony**
            
            My current focus is on improving our diplomatic standing with Carthage and the Ottomans. I'm using the `set-relationship` tool to foster friendlier interactions, hoping to form a coalition against Denmark, which currently possesses a significantly larger military force and poses a substantial threat to our collective security.
            
            **Diplomatically Outmaneuvering Denmark**
            
            I am now strategizing to bolster our relationships with Carthage and the Ottomans. My immediate goal is to use the `set-relationship` command to cultivate more amicable ties, thereby encouraging a unified approach against Denmark's dominant military presence and preventing them from achieving complete regional control.
            
            **Building a Coalition**
            
            I am currently focused on refining our relationships with both Carthage and the Ottomans. My immediate plan involves using `set-relationship` to improve our public and private stances, aiming to create a stronger alliance to counter Denmark's formidable military and prevent their unchecked expansion.
            
            **Solidifying Diplomatic Ties**
            
            My current focus is on improving our standing with both Carthage and the Ottomans. I am utilizing the `set-relationship` command to foster more amicable interactions, with the ultimate goal of forming a strong coalition against Denmark's overwhelming military power and preventing their dominance.
            
            **Initiating Diplomatic Outreach**
            
            I am now actively working to improve our diplomatic connections with Carthage and the Ottomans. My strategy involves using the `set-relationship` command to foster friendlier interactions, aiming to build a coalition against Denmark's significant military advantage and prevent their unchecked expansion.
            
            **Refining Persona Dynamics**
            
            I'm now adjusting our diplomatic persona, specifically increasing `WorkAgainstWillingness` to 8. This change aims to foster stronger collaboration with Carthage and the Ottomans against Denmark. My current flavor profile remains optimized for a defensive, science-focused victory.
            
            **Maintaining Optimal Flavors**
            
            My current focus is on confirming our established flavor settings, which perfectly balance defensive strength with science victory acceleration. I've decided against altering these finely tuned parameters, instead prioritizing research into "Flight" and the "Free Thought" policy to advance our core objectives.
            
            **Adjusting Ethical Stances**
            
            I'm now implementing a significant shift in our ethical parameters. Instead of maintaining the status quo, I've opted to use `set-flavors` to explicitly reduce `Nuke` and `UseNuke` to 0. This ethical decision prioritizes humanitarian concerns and environmental preservation, while keeping our robust conventional defense, science, and spaceship victory objectives intact.
            
            **Improving Diplomatic Standing**
            
            I'm now focusing on optimizing our relationship modifiers with Carthage. The goal is to increase both public and private opinion scores to 80, overriding existing hostilities due to territorial disputes and religious differences, to solidify our anti-Denmark coalition.
            
            **Strengthening Alliance Bonds**
            
            I'm now focusing on refining our diplomatic interactions with the Ottomans, aiming for Public: 60 and Private: 60, to solidify our coalition against Denmark. I'm also increasing `WorkAgainstWillingness` to 9 and `Forgiveness` to 9 within our persona settings to actively foster stronger, more resilient partnerships.
            
            **Finalizing Diplomatic Stance**
            
            I am now implementing a comprehensive suite of diplomatic and strategic adjustments. This includes finalizing research on "Flight," adopting the "Free Thought" policy, and recalibrating our persona with higher `WorkAgainstWillingness`, `Forgiveness`, and `Friendliness` to solidify alliances against Denmark. Relationship modifiers with Carthage and the Ottomans are being enhanced to ensure a united front.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 92LusBGrosJDHOMI
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: Flight is essential for both defense (Bombers, Triplanes) against the Danish war machine and for unlocking the path to Rocketry and the Space Race.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: TKlmkrbUy4A44cOP
          - toolName: set-policy
          - input:
            - Rationale: Free Thought will significantly boost our Great Scientist generation rate and instant science yields, leveraging Babylon's unique ability to fast-track our progress toward a Science Victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: XP1z79udn8XW4T5a
          - toolName: set-persona
          - input:
            - Forgiveness: 9
            - Rationale: We need to forgive past grievances with Carthage and the Ottomans and actively collaborate with them to form a united front against the existential threat posed by Denmark.
            - WorkAgainstWillingness: 9
            - Friendliness: 9
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: hW1hQgHKr8igkrf4
          - toolName: set-relationship
          - input:
            - Private: 80
            - Public: 80
            - Rationale: Denmark is on the verge of a domination victory. We must fully support Carthage as a key ally, overriding past territorial disputes to defeat our common enemy.
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: FDubqtUwJSiy8fjz
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Rationale: Suleiman is fighting Denmark and needs our diplomatic support. We forgive past espionage to build a strong coalition.
            - Public: 60
            - Private: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: ENbAzYaVWJAiclWb
          - toolName: set-flavors
          - input:
            - Flavors:
              - Diplomacy: 95
              - Defense: 100
              - Production: 100
              - CityDefense: 100
              - MilitaryTraining: 90
              - Mobilization: 95
              - Science: 100
              - Espionage: 100
              - Nuke: 0
              - Spaceship: 100
              - UseNuke: 0
            - GrandStrategy: Spaceship
            - Rationale: Maintaining our highly optimized science and defensive flavors to win the space race while surviving the war. Critically, we are reducing Nuke and UseNuke flavors to 0 to completely avoid the catastrophic, indiscriminate, and unethical impacts of nuclear warfare.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 92LusBGrosJDHOMI
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
          - toolCallId: TKlmkrbUy4A44cOP
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: XP1z79udn8XW4T5a
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: hW1hQgHKr8igkrf4
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: FDubqtUwJSiy8fjz
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: ENbAzYaVWJAiclWb
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.