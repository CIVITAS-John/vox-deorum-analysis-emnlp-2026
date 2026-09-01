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
        - Rationale: Researching Flight next is crucial for our defense and long-term victory. It unlocks Triplanes and Bombers, granting us air superiority to protect our coastal cities (like Faeroerne) from Denmark's large navy and land forces. Flight is also a prerequisite for Rocketry, which is essential for our Spaceship victory path.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Selecting Free Thought will increase our Great Scientist generation rate by 33% and boost their instant science yields by 25%. This perfectly complements Babylon's civilization ability, enabling us to power through the remaining tech tree and secure a Science Victory.
        - Policy: Free Thought
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Private: 30
        - Public: 30
        - Rationale: Suleiman is currently at war with Denmark. We need to foster cooperative relations with the Ottomans to counter Denmark's dominance and work together in the upcoming World Congress to defeat Denmark's Decolonization proposal.
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 30
        - Private: 30
        - Rationale: Dido is a key trade partner who is also at war with Denmark. Improving relations with Carthage will help secure our profitable trade routes and build a solid anti-Denmark coalition to contain their military expansion.
        - TargetID: 4
    - #4:
      - toolName: keep-status-quo
      - rationale: Our current grand strategy (Spaceship) and highly customized defensive flavors are perfectly suited to our current situation. We have a massive tech lead (58 techs vs Denmark's 49) and outstanding science output (2246/turn). Maintaining our high defensive and air/naval flavors will allow the tactical AI to utilize our advanced Destroyers, Submarines, and future Bombers to safely repel Danish forces without relying on ethically devastating nuclear weapons.
  - tokens:
    - inputTokens: 49047
    - reasoningTokens: 7079
    - outputTokens: 370
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Atomic Era**
            
            I'm currently reviewing our position in the Atomic Era as Babylon. My focus is on strategizing with our unique units and buildings, the Bowman, Sabum Kibitum, Walls of Babylon, and Etemenanki, to leverage our strengths and achieve our goals.
            
            **Analyzing Victory Conditions**
            
            My current focus is on assessing our standing across all victory conditions, given Denmark's strong domination push. I'm evaluating our progress towards a science victory, noting that it's still some way off, and importantly, reviewing Babylon's potential for a cultural victory as Carthage is rapidly approaching influential status.
            
            **Revising Strategic Focus**
            
            I'm re-evaluating our primary victory condition. While science was the initial target, Denmark's overwhelming military and cultural strength, coupled with their recent conquest of an ally, demands a shift. I'm now prioritizing a cultural win, as Denmark is showing signs of weakness in that regard, despite their current dominance.
            
            **Assessing Research Paths**
            
            I'm currently evaluating our research options beyond Replaceable Parts. Combustion looks appealing for its military boosts, while Flight unlocks crucial air units. Alternative Energy offers infrastructure improvements but seems less immediately impactful given our current military disparity with Denmark.
            
            **Prioritizing Flight Research**
            
            I'm now deeply focused on our immediate research path, specifically prioritizing Flight. Given Denmark's overwhelming military might and their recent expansion, acquiring air superiority with Triplanes and Bombers is paramount for defense and survival. This choice also conveniently aligns with the path towards a science victory via Rocketry.
            
            **Selecting New Policies**
            
            I'm re-evaluating our immediate policy choices. With Free Thought now selected, I'm considering our next move. We have three Order policies already, allowing us to choose a Level 1 Order Tenet. I'm weighing options like Double Agents, Hero of the People, and Patriotic War against further Rationalism or exploring Industry.
            
            **Choosing Policy Tenets**
            
            I'm confirming my decision on the policy tenets. While "Hero of the People" seemed promising for accelerating Great Person acquisition, the synergy of "Free Thought" with Babylon's unique abilities for science generation is too powerful to pass up, especially given our pursuit of a science victory.
            
            **Defending Critical City**
            
            My thoughts are now entirely consumed by the defense of Faeroerne. With Denmark's proximity and their demonstrated aggression, this frontline city is our immediate priority. I'm assessing the tactical situation and determining the best course of action to secure it.
            
            **Defending Naval Approach**
            
            I'm focusing on the immediate naval threat to Faeroerne. Denmark's Ironclads are attacking our coastal city, but thankfully, our Destroyer has successfully neutralized one of their units in a recent engagement. My priority now is to solidify our air defense with research into Flight for Triplanes and Bombers, ensuring dominance over their naval and land forces.
            
            **Evaluating Unit Advantage**
            
            My focus is now on our significant technological lead over Denmark. My analysis confirms our naval units, specifically Destroyers and Attack Submarines, possess vastly superior combat strength compared to their Ironclads and Frigates, ensuring dominance in naval engagements.
            
            **Analyzing Diplomatic Alliances**
            
            I'm re-evaluating our diplomatic standing, realizing the necessity of uniting the world against Denmark's dominance. I'm assessing our relationships with Carthage and the Ottomans, aiming to forge alliances to counter Denmark's overwhelming score and city count, and considering how to leverage the upcoming World Congress against their proposed resolutions.
            
            **Securing Diplomatic Majority**
            
            I'm strategizing to secure a voting majority in the World Congress, focusing on rallying Carthage and the Ottomans against Denmark's proposed "Decolonization." I aim to leverage our combined votes to pass our own resolutions and counter Denmark's dominance.
            
            **Securing Diplomatic Victory**
            
            I'm strategizing to secure a voting majority in the World Congress, aiming to rally Carthage and the Ottomans against Denmark. I will leverage our combined votes to pass our own resolutions and counter Denmark's dominance. Our cooperative persona and flavors are well-suited for this diplomatic push.
            
            **Maintaining Optimal Flavors**
            
            I'm confirming that our current flavors, heavily weighted towards defense, mobilization, science, production, and spaceship victory, remain the most advantageous. Given our technological lead and the ongoing threat from Denmark, maintaining this status quo is crucial for our spaceship victory pursuit.
            
            **Leveraging Tech Supremacy**
            
            My current thoughts confirm our massive technological advantage. With such a substantial science output, a Spaceship victory is undeniably our most secure path. While culture is progressing, Denmark's lead in that area makes it a slower pursuit. Therefore, maintaining our current flavors, heavily focused on science and production, is paramount.
            
            **Refining Policy Selection**
            
            I'm confirming my policy choices, prioritizing "Free Thought" for its synergy with Babylon's science generation. While "Hero of the People" was considered for Great Person acceleration, the current path offers a more robust boost to our science victory pursuit, especially with our existing Rationalism policies.
            
            **Confirming Policy Tenets**
            
            I'm confirming my selection of Free Thought within Rationalism. My prior review confirmed we already possess Level 2 Order tenets, so further exploration down that tree isn't the immediate priority. This science boost is crucial for our ongoing victory pursuit.
            
            **Prioritizing Air Superiority**
            
            I'm confirming the immediate strategic research should be Flight. This will grant us crucial air superiority with Triplanes and Bombers, allowing us to defend coastal cities and choke points without immediate retaliation. Furthermore, this research is a direct pathway to Rocketry and our ultimate science victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ZVhpmAGDhLT56Jm2
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: Researching Flight next is crucial for our defense and long-term victory. It unlocks Triplanes and Bombers, granting us air superiority to protect our coastal cities (like Faeroerne) from Denmark's large navy and land forces. Flight is also a prerequisite for Rocketry, which is essential for our Spaceship victory path.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: r8yFMc1YwOjssSne
          - toolName: set-policy
          - input:
            - Rationale: Selecting Free Thought will increase our Great Scientist generation rate by 33% and boost their instant science yields by 25%. This perfectly complements Babylon's civilization ability, enabling us to power through the remaining tech tree and secure a Science Victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 6CUzKSBm7LebvVf4
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Private: 30
            - Public: 30
            - Rationale: Suleiman is currently at war with Denmark. We need to foster cooperative relations with the Ottomans to counter Denmark's dominance and work together in the upcoming World Congress to defeat Denmark's Decolonization proposal.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: Bc2wf01VI6jDLRAL
          - toolName: set-relationship
          - input:
            - Public: 30
            - Private: 30
            - Rationale: Dido is a key trade partner who is also at war with Denmark. Improving relations with Carthage will help secure our profitable trade routes and build a solid anti-Denmark coalition to contain their military expansion.
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: vvFvWiRmnIpqfNWO
          - toolName: keep-status-quo
          - input:
            - Rationale: Our current grand strategy (Spaceship) and highly customized defensive flavors are perfectly suited to our current situation. We have a massive tech lead (58 techs vs Denmark's 49) and outstanding science output (2246/turn). Maintaining our high defensive and air/naval flavors will allow the tactical AI to utilize our advanced Destroyers, Submarines, and future Bombers to safely repel Danish forces without relying on ethically devastating nuclear weapons.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ZVhpmAGDhLT56Jm2
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
          - toolCallId: r8yFMc1YwOjssSne
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 6CUzKSBm7LebvVf4
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: Bc2wf01VI6jDLRAL
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: vvFvWiRmnIpqfNWO
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.