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
      - toolName: set-relationship
      - args:
        - Private: 50
        - Public: 50
        - Rationale: Denmark is a massive global threat and has already captured Bratislava. We must overcome past espionage and religious differences to forge a friendly relationship with the Ottomans and prepare a joint defense against the common enemy.
        - TargetID: 1
    - #1:
      - toolName: set-research
      - args:
        - Technology: Flight
        - Rationale: We have completed Electronics and are currently researching Replaceable Parts. Setting Flight as the next technology will unlock Triplanes, Bombers, and Paratroopers, allowing us to establish air superiority and defend against Denmark's massive land army.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Free Thought will significantly boost our Great Scientist generation rate (+33%) and their instant yields (+25%), perfectly aligning with Babylon's scientific focus and accelerating our progress to a Spaceship victory.
        - Policy: Free Thought
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 10
          - Diplomacy: 95
          - Spaceship: 100
          - Science: 100
          - Air: 100
          - Espionage: 100
          - Mobilization: 95
          - Gold: 80
          - CityDefense: 100
          - Production: 100
          - Defense: 100
        - GrandStrategy: Spaceship
      - rationale: Reinforce our Spaceship grand strategy with high defense, air force, science, and production priorities to counter Denmark's military hegemony while maintaining our technological lead.
  - tokens:
    - inputTokens: 49047
    - reasoningTokens: 6211
    - outputTokens: 284
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Domination Threat**
            
            My current focus is analyzing Denmark's overwhelming domination victory progress. They hold a significant advantage, controlling 5 out of their 8 original cities. This necessitates immediate strategic recalibration to counter their expansion.
            
            **Refining Cultural Victory**
            
            I'm re-evaluating our path to cultural victory. While our science lead is substantial, Denmark's military might and capital control are concerning. I'm focusing on increasing our cultural influence with Carthage and Denmark to secure the win.
            
            **Analyzing Diplomatic Landscape**
            
            I'm assessing the upcoming World Congress, particularly Denmark's significant delegate lead and their "Decolonization" proposal. Given our ongoing war and their territorial gains, I'm prioritizing immediate defensive measures and exploring alternative victory conditions beyond science.
            
            **Analyzing Diplomatic Landscape**
            
            I'm assessing the upcoming World Congress, particularly Denmark's significant delegate lead and their "Decolonization" proposal. Given our ongoing war and their territorial gains, I'm prioritizing immediate defensive measures and exploring alternative victory conditions beyond science.
            
            **Updating Technology Path**
            
            My current thoughts are on our technology progression. We've just unlocked Electronics and Replaceable Parts is next. I'm reviewing available research options like Combustion, Flight, and Alternative Energy, and noting our policy advancements within Order, considering potential branch unlocks from Tradition and Statecraft.
            
            **Shifting Policy Focus**
            
            I'm re-evaluating our next policy based on Babylon's bonuses. Free Thought seems ideal, significantly boosting Great Scientist generation and yielding instant bonuses, aligning perfectly with our science-focused strategy. I'm also checking if we can dynamically change this selection.
            
            **Revising Alliance Strategy**
            
            I'm recalibrating our diplomatic stance. My recent realization is that despite a shared enemy in Denmark, our relationships with Carthage and the Ottomans are currently unfavorable, even hostile with Carthage. I'm now considering adjustments to these relationships, aiming for an anti-Denmark coalition.
            
            **Improving Diplomatic Standing**
            
            I'm adjusting our stance with Carthage and the Ottomans. Despite shared animosity towards Denmark, our current relationships are strained. I'm focusing on improving our standing with them to foster a potential anti-Denmark coalition and secure defensive pacts against their overwhelming military might.
            
            **Prioritizing Aerial Defense**
            
            I'm re-evaluating our immediate research priorities. Given Denmark's aggressive posture, I've decided to focus on unlocking Flight. The introduction of aerial units like Triplanes and Bombers will be crucial for both defending our cities and projecting power effectively.
            
            **Evaluating Policy Shift**
            
            I am reconsidering our current policy choice. While Free Thought provides excellent science bonuses, the tenets of Order, particularly those enhancing production and military strength, are becoming increasingly appealing given Denmark's dominance and our precarious position. I'm weighing the long-term scientific advantage against immediate survival needs.
            
            **Assessing Cultural Pressure**
            
            I'm re-evaluating the cultural landscape. Denmark's immense culture output presents a significant challenge to influencing them, despite my scientific lead. I'm now considering if a late-game tourism push, coupled with a spaceship victory focus for defense, is a viable alternative.
            
            **Adjusting Alliance Dynamics**
            
            I'm reassessing our diplomatic and military alliances. Denmark remains the primary threat. While I'm focused on building an anti-Denmark coalition with Carthage and the Ottomans, our relationship with the Ottomans is surprisingly hostile, necessitating urgent improvements to secure a united front.
            
            **Improving Ottoman Relations**
            
            I am focusing on strengthening our bond with the Ottomans. Given our shared adversary in Denmark and their current disadvantage in that conflict, I believe increasing our relationship modifier to positive levels will foster crucial cooperation and potentially deter future aggression.
            
            **Improving Ottoman Relations**
            
            I'm adjusting our relationship with the Ottomans. Realizing we previously set it to a negative modifier, I'm now initiating a change to a positive 40/40. This is crucial for forming a united front against Denmark, especially considering their overwhelming military strength.
            
            **Analyzing Congress Impact**
            
            I'm scrutinizing the impending World Congress, especially Denmark's "Decolonization" proposal. Its potential to sever non-permanent city-state alliances is a serious threat, jeopardizing crucial relationships like Kwa-Bulawayo. I'm prioritizing securing permanent alliances to mitigate this risk before the vote.
            
            **Securing City-State Allies**
            
            I've realized we can decisively counter Denmark's "Decolonization" proposal in the World Congress by voting against it with the Ottomans and Carthage. This alliance, totaling 33 votes against their 25, will protect our vital city-state relationships. Our strong AI focus on diplomacy ensures this coordination.
            
            **Researching Flight for Defense**
            
            I've just finalized research into Electronics and am now prioritizing Flight. With our strong production capabilities, I intend to quickly build Bombers to counter Denmark's formidable military presence. This aerial advantage will be crucial for defending our cities and projecting power effectively.
            
            **Developing Aerial Superiority**
            
            My immediate focus is on researching Flight. With our strong production, I'm confident we can quickly build Bombers, providing a much-needed aerial advantage to counter Denmark's overwhelming military might and defend our cities effectively.
            
            **Researching Flight and Alliance**
            
            I'm prioritizing research into Flight to counter Denmark's military. Simultaneously, I'm reinforcing our alliance with the Ottomans to secure a united front, setting their relationship to a robust 50/50, and confirming our science-focused Grand Strategy with specific flavor allocations.
            
            **Securing Diplomatic Coalition**
            
            I'm solidifying our alliance with the Ottomans, aiming for a 50/50 relationship, to create a united front against Denmark. This diplomatic effort, alongside prioritizing Flight research for aerial defense, is critical for our survival and eventual victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: z3J363pL9TOeZKMs
          - toolName: set-relationship
          - input:
            - Private: 50
            - Public: 50
            - Rationale: Denmark is a massive global threat and has already captured Bratislava. We must overcome past espionage and religious differences to forge a friendly relationship with the Ottomans and prepare a joint defense against the common enemy.
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19hxFcIP5/ClgV3T2t9dXfjYOlHExigE7dubKQLwrhmjKzFC/XKeUs2AcI91yig0ih0OxoDC9+La2LDRBCMWHEvFPnLXBsDTcg6C/3ac+6Wt+VLFFI8Ek+J4sz5X89Rdg1BM19/f6HcOSdKJz1nuerUnWyLbLr9bf/UhcxRVwbtMyNJympy+qzUlBHIoObcPldmX+Cku8dgzRdHM+SELKog8hxbNAwDin39Xe0iahD8HcQjaIz4m0xr+U0hzT9Elh/d16c2DrHmKHB4AjU8BlJ2KROkooc6ZKCHXMSIQiYS9u2LkYL/nQdkf+1R43iIO85rAi4je5fHiHVInoLxTbUqbuSxIS5+NssiEAlQlrFw3hKmWtaT5vwQZ3tCCA2qPxEwPfkEmkjzthtjV6pzeIEsXdJgBOrx26wm+FbJSF7XTIIoxhxHrQh96OPQy/XsgUFaCT7Y30UuphpFasHXDUQ90Nc6hScey2jlAf1pjJfmHOC+0a0DcMlri2OnnaMqDpMevTS1SyXu8frRMJFr8aSGJYXTZGn5uD1Q1GPssiZMOJeZj6lcOA/cShWbNsJI+K7+Zf4Wh/UVVYCsdKHlHDEkyZQl8Q9Lr29jDEE96m9ex1yCZgdP81Mxf5jhPdGIFUnWgzb6y4MRbs10YnOZKClCbngLHlvbZ3L9rBERIdEWUfxODokmhqmtQHwPRz2V3/8agRV++KDaodap2eU30AnNd99RT6gAWvYDN4cFfpA3U7j2jwLL3dKIrbWNYVJDrvRBtuFTJkJI3RiEyRTcunKcTW4jorY6i05wJov6IK0ZLS8MJ/satUKT9g3g2+rHxLLn2TtCWqe83GVC20emJ00Wl2Af9xoAJB4WscEIiboPkr0MaO6DLa6dCKGFcU8sxGQHoC7sz7pjgchY6bOYCWi8M4ufiHSPme7EsmiMh3h2x3CS7m7307IgSUhJ65LfxJ/iT8lQYwWfbsMEfuD2GepXEiloZ0lEKPIxnbmJc5JhnW57I02LeFskjVDoNcdgafadlP1o0jX2ZqJXi8a7NnrbK7R+B2TlKGDo1XHflPHWuHKR3BVvFtZDPYzc7UP4wQVzf23pqHU+GAyD3E4CHEnVFu4OHARM7WeM4ujmEzQEo3UzirFOE3crYMZyJqqEGdtmqlgBblIljX2IBjyf6xTQi/iKb1cQoJBEVAWitvgx+hfYUrlEWk7SUPO6eB8CiF+8riBgUyNRYjoJdBV3gU0J7ecOSmzKCW1MT41XZfVtUMfdg3w/iHLTks7UrUPy3GnzXyJwxjBkLKcp2+qOrJ0nYYoPSTmp+SPxzJ2Y5vXCcc0QwoyzRqo0HhlCxK50UXr3U4TYINv87PogqHDde+Jx7b31CMuF5SOYxxBiYgJ5b2euTSER+wVCZwzMLc8w6QMAIGHSDmyw/i8E6PIaGoRweg05cnTMB4eVzivbKVUO/uVXyCHprTpUcrzp0u0XxFwdgD58Uex7AZgB1dnklywsvvF9DyNlQD2OYFV7nmJ9QSYiwAxjtzYLepYNX/rMsmDhHw7JRSrfEYELmNfWW+fUKxHk73xpSi2ktQmRZ7ANyowGjY1u5U/j6Dw7C5ac8Hn+mK9YXkKxq72vv2gcUGq/BMtOj9pvZ/f5ddmjpdPhY4F+0Kv1c5UiIe3nw9Cy/eDKlIKKRQKSm9TIvy1vY0wt+dOqESanCo9cQseAD07Bf7qypPHfX53k/cPzInOW8AoqHzX9g8kXzmdgcYM0t3TD+Gsw1O73I8zC28JZik/Vro+ZHJDos/u5ocQ4iyL6yCcYIoDrIQ/JeCou5y4h6qnV9kqy/iYqaE/LD6SZNPl6ghL8p/+uswhEe6j0qrOZh9s9wnXyELWs1KB1WHaGdoxj3ZD8/l/nTRT3mbnQfrwmkQHcflvU5S+dO7fJ/8T6qlkFwtwwrDqp8EHBcehvYWg1Ro/UlMsJdTtKlHaEAboUFc8Qy7GETXIN+gh5bLX6N1d5O0EJiAtrfrlQr4xEgOZZXl2ora3DJE0D2nx2cYi4dOXd48LteSt3ObOVuq04vQ919YIcsVLLejsb3zJPrBtJWoDpME7OnH7GPZ6Jm/joQiUVCMnxyCr2biRQJgBqyXbcyudt+HZXTYa3MkEr/p0YAOCH5AsIxzh6JcVGjR6hMlLdB761kvCTu6UHmVfVIcihmQPA61XHVsIarnMMuuNcMc+NF+nN89jhPmCUi+adGDw3lGSpi+Bcr+ZPm36UJdyM0mnv5qmmoATjIqmnQLphfQArzbcEdZ4SFPWMVMVmyHjr5PqcVN2bl01JpUdcHYFArQm9/v2aXjPeEtBgJwZ8a6u2qNNcPfFuyn/zK0C3pCfZ8Id35u1b/p+/txxjhWBUvQOLDEdXpIx2XW9RlMkwWU60E35w7+JxJs0Sr+BhC8FIsiHG//kcH1kjDRxQFS4Y87Nao5YGmT2RuS49mdems9Q4VS+rtDkrYMzdQANHJ5Lam8sQ28pwvlr/voooT5jqLxeaFA/RTrc+OraVnVUwVCFciHTkvCQUGbG2Zw/Ijls3Q58CqmlXioOCvuD7nGMjFVeUdlzXMsBQVgsxZx2FdJOfItgOjQQWx4BZElxiC9J//0Xjup5hRzIlC/GoeBuBrSzkv9WhmL8/bB7ii3QoYyHiKQH8X4wlWeXPzHxEDlb+lWigyB2abZ3ziNiBC6Whgcgt4l4GxzUPgzxm4u62Wp0d9w7zoc4iQA8qfLq+76qTWXeJyZHSRTVHH9YfcI3LSZgF3HUwOx4HjPfJpN5uLFm2CU63pD/QvJTbJXWMIDRAENwSqS8EQDScV/9gp+gJ1CD6GVAF9lbBAScfssdoR+w/U2axvLpK4s78kE17zMlPnZvUc75+HHj/vW8XvisyAYWTJqehb7SHoBJO0jB94vYS6wnzaRcfL5jxhn+YGswRqxK8kxrpGm0/hc+uvIMn8NjkVMUBfYoTN+fX1hOquyXeE7ef+NRwgzFHFQvQ4m6ObUS2mcMvknA9MZNNJt53YZSHL6wVt+ZfowmVKqPpBSHXUZSqv1JP+fbGBY7Pti6Gf5MKlu0IIPDpzVcH3tJjUOmhmO8xNTHd259sf0YGBen5C4Z6Nt1X8j4M2tGecLFT4UrocLxoNhT+jLCguxXbLUGVnAhB9C20aY8Zbpw3/Rb7ENe4HLcj8l67tmnLghLxwcximeeQaRytZUNuDGr6byAHVfNthHw6KsAoRVVpvAFlkl2yfQ3HuyzNMGW2Km1LlBG/VxhwppMhuVDf64VYvg2/Sd8O/ec76S6IExcrYCYP9V0C5OykIUXLv/mj17i/0s/FypiabE8zdXMxqvB//ICZnUktdF1IPLrIms6wQn0EgAEuYBzXnvZERSDM/Pt3WFWGC9PjWl7noUcjcVu6CBo4BY6SLFX8iIlUJVBe1TvJB2BNl8+IbefdHeiTsBEy3NoDZZ8Ra6pZ8FP2V2/7yE95EURFWuPZnsbDZkvKK1GRqGp6ldHb0IrIEuC6ooXVjt/nb/Ihe4FEMuwhmnhO3FVtR9rAfZ6tQxV32rjyThxFkFdZvYhU08nqC1Si97dFTpXexOPc2f/CrO2YLax9E9PHoYiaumwD4jYaRyq+xDz669O65EIzW0jhLxvFMTX2KbD3Q/jO3MWKJmC+ERjebilR2cqcP9Y6hMPLPVh0P2rLB+uCgYKcdi3DA45S5jL+BYxTjOAj4n8U3qJdXX+S5Wd6feckPQ3subxDN2HjWLGUoxEzYnbb2gDYKeY3AwrteOh8C2ziH6bg0AKO+43cXQDwzasNb0+CW0HFYmWGJDWpShQY2YiPtUyN2k8LwnFDu6fZISkfEQhKP85I1rNSez6VuPDbcx+uMX6OdwV5bfbgWdYiY/uaortEOYejXk+pK21IscWEDGOrvRmc8VmtCQgyhBmulsLYsuqcyLXKA5lkpe8clcljiV1qy5nLoBBFkzAOQdgE53H6zhm9QGXUOyj+AKp5A9RKsoQJuvCIFbETLHO2sCWvzkCLKJEZgLs6GjJx/THixDUhjnpLE21Ylj9B9aRe8xumFaI9O0JuNfnStGkctBd6pJvC58L42H6HfGMPh/EYggmaVk81PCLu0k0510qtaEDyYuIYA46TYWyNK+312dQ3U2yvaI9zcXLd7x05cj+I2vvbr9en6m/C0eImIaUJwm7qg9J9SFcnlEUMNS+cbY9vN9Rv2lZGpdVZcE/UxTpVEsqZDN6Y56w53zrytbyZAMtPrEYQ2iGzfVaYpLw3Z1gNOOg51kZkve1B/Uqw6LFUcV+pDaDaZYmDgXHm2TcAU6YGvkXUE+e0iFMEnKP1eptuwjKWF+U43upbWHR+p0ce9Yktgk2Z/HGPFHp5bMjUUd/dz3U4T/ZS9TJqjv/eNsdPPvQS81DRpjpRgsbqaqVs70iGdhsEK6s//I8ib2+h2ji0BY0PvnXPseB1oJHNzDEp+2NAzx6Ntb0XGK0m2L21mOz3nsS+4MXEXMrdy4na1+anB6Ikny2P30FPLgjIV9Sa71HOAkYTFigwC9Ukq4vCs77xY62ONFiRwTOBUy8O7rv43wPk8kzOgEWer1XU+YNc14SMbY+Je3NXE5GPnkJg1u6frPQTtQYadf4XDngEGGM2sWYHE1EpwTfhb6IGCUp5eih/8d5+QUisneIaifPis0ARuV9n7HcBiCzlqv6eRwO99ssvPiNVJGLzs9QV23f0lh3Fcg40IiDIQROTVOQa5kiWjIN0XCiRz+8/IGAy4fjwPsWSCUG2cGA6Q40sScZSvLRNqzjhJ7JdDN68KOZSq5snKCPjFQqcKjU7NlUDSuFitskRqzmyRp+eFqVWp1dIJ5ljH17JeInO43j7IYkdFUhbBfu7W70XDk/WAvXIa0fuyzrhRmbGnzcxkyz0Ei7V7epJkUrRfzvJxBrlzFQWqDeWjy3cfGQh1AVGx3qstEhB/DtcE/XKGvCWuj4mRxnllbjBFIP/RUXf78Ch9VwVffPlW9j2+6IzTAiFfEpZVbCDbsH9yIgnOChRJZd2tQODgddRu3YiuYxUY2XhuoV9TdlVROsTrt7rfN5dP8VlPWIG6n+c6kYtapMA0UGY9egHCVgvxAdoCI1uxoRB08T3LLfXAnSaX8AQ90bIZnK6K/3NfWphifhU7IZ62IS4yDuyOoya94hRbB8idAiGGAPHo7TZY7zdKFX4gN4Ikohi1ktLtplLxcSeSLKwUYX7CFmmgI0bNxWaw6SV0+t/AdkJn7TxP06ulN01qOUm92/wIQVT9sb1e2b2MPcy+Ws10zue/ITj+bg1UT9q9bwkRDPCeGMwTTR5n95/aJwSKX3P4na5ZZstn1ZOrfqBgJqN9SdR7nMZO4UXlDAalb4WVqrYPYN7mtsNBz8t7J7jhWVgmXAxv32boSI2knH9Eeljz1lEUxD9k+2lM1OnduvoQtDHuAexPkpNqEQnByuXz5Ql9/kcPyzYtFnx6EXiHykTIGVSHBPtGjVUvaAVMroImlLBo3fBwHaN1GY8QBKhgafDHTD/jGGX0hv5TRUlk4OV4LQJdyQh2RyRtiHoUcrXaaAuAEdGo4UgUcgJ9txdjAS4+8oCj4qKVTwqr6insC0iY5R58eco8216WAqitprn4KRP7bUVraEvPpVMo5SEvbZpz9eeDSb/QGYPzdlxQWiK2RKCTlX8yk2NI1/sYyJaNVHkLPdQYOPn+zsmJjINZwYJ938xHX22G5VUalDUHdqI2yERrGkUREqnDE5U5xd0VEy57sQc808KXumXfKQkXtOSLiH5V2XiopscLs0dW5RORO53okelbIVvGdNthuz+NviZWUbuPq7NMWsiZScgDqIGUyJhy5UV7hb6881tTXPrRbGlxzI88ur8ucWcPxgUYGIZOO6Y3la0LQh0Hxv63O0qpr6dFGciDacQl47nCxkpKmRa7Ztmuy69jNkCPKGghLSAsTT1zJiJq8D0cBLdk+gKMZqvwulkYZVPT9/xLUt5NAjxwNVWLSCvW27g37Q1dPFJIjvUzhrbipScj3wySrILmcDUQ6lwYXQwC/KrZM0qtwvd/cTjiMNZqXcIZsPbKGJhKDhaq2SidihJxyYeVGZP08GGWpy8PLEdX2qIqF8PGjdPsAjy6Ma5TwaFs/GRJ4aLuOQ6rX9hx4Bfnu26h2UpM1MaZks6HQf+bU4pkQkNkXFJQRBlYHJZcZjq9fSLoK675eRkMzCjYaX0gFvpk4OSuuxL5ZEBPQvDX3shupg/Q/EDkfu3OyrEFmLRYsUF2yoHKtISmMTFVAhpQKE8J4CPUYoOWcn81fhOlC9LlHQEQXVfoQ8asNB1in3uA53pi+7rzbsN5oyG732EqbRALDXD/T150JV58KeW9y2KRDFH+GA+gqph0Zh2+J7iakevZYnu9Qzz+MJs1kF16iX82wL8CWzmpU0Yhh72kJdZ07YZFTZcleu1OnLbre952Jrm8oiVVAdpwF+5U6dtxJV8+1dO6lcHMjpt6fDekr/Ocp1NrvS/Gxh4bhuQsVSOAu3t2He1A7eXq77DWJAz6AoRZWV+SEt+OzBGrxGLGOHpIsN7lnQbZUBwnN6MZZO/cWpnhVZbGYJGnNsrE/Bf1aOV2Elmyjqo0hgqQ6jGjBdYN0+ox4/8LK6/sNTJn9jmodGUrR3CZip6wXXXBOri6EIcZIadludvX4sdu7qDhX9v3Qkxxv+SWTHf8kiGbKXbn4Jf6EqJMEkpyp1IEX33wf5sUBRER0TGTNuKMtz45ckPbx70O+MAo/i7Kg6Ay5nSRWP9JLRwusg5JmUU+rG/jwUub0vWHjL/Oz387ryF0jtbmyAMoNob5QQhehu11tLJf78kKEs1xWjRSwswXHcmju6Bjj9CdbVE79xkdm6mYQkWWnmiovtFtqz2VurBe2rki6zuKj4J3GmdaiqjwO89x/PFfIngucuhW509/NqM0BfyYrqHBwLhqAgtcqD5yVKISFEzQN/9uk4LNCO25FpNWuOqXTPBdsq/htIfq50os+Uz+E8dnt4YyPikhluGJdg8lXgvgixL5yrMiSwyUuteGae71LEmJjTZKMbtAfVAQrRX4/+u/qF2qc+kNu7oba6Xv2QRehkT4fpdbMJ4ytyVKEYi3AOcdGm56JnmN0jzOWoBbcu8FwA1TRpt99fuO7LaA97IDRxEyGcenRnshxijfrxboeYpzGS63l0qh0Q9LJoGmPrWVfKe9A5foVmHCyrBPBrvuzVsI/NqqSE6taVtuBkdShA+X4xILa95pcHmXeZK38QzZKtaGeTagapAADZ15g6to4hdyQ+BSizHYzl4M19+4wXOGnIrTN41KWk1JeqfW5n5AXCill+3obJUI25QhQAnqYWdM/AMe4YutAPtgJt8TQLqEJMBVrWHHbSUbIEYfn6HC8uqT4/TeACeyBbU7FATreuDhFSiPbDcYtKUGR8y0CXqKpuldvuLXQmxtjhjjPGmACZgRFrK4MlNyiGlC2bcOO4zLfJJTTyh5iLtF7HO7WoG4r/mcdSU19YUsNia3TLVVWgebtKyNdL6zolGPyiLwjZ3TiI9sWf1XllMtMx2Gu/+WT6Cd5omj5E0TzQUVvSixAItJlRDNjio/QhBzGXwG9tRwTkZUMi5p2IMdpX4KEhya6p1Q1tm9sazhs17AIjoDA1sSMXAAY6ClC0hLJDYlqnw1IJNzGIE6daJCOg7Cmimp+zw547ISf1CvtPhhBK3H2Gg58+67bC0CgcZZg4hRPejnxY1bbgVfZarBiYKpo7FB0eJUYpSUOgJiNKNMl9htyetGzkmGx8HVvi2zoqQs66GBBZ85OAe0nqZVTljjZBFub7AK5mOOWiA0n2xdz5lnCoF/AmYmuasZJa47dN7SZlh0aeU/VyeZJwhYK1rp6n3bjlFPg7MmT9FWxUkLtLnqIaNZp4biCx/IWwgX1auMUVqpqsJlqhY95uKWyEA8P88OKdVnA7W+E07X41CgIpeFFgx1Mwa1MlKMUMC/XFrHsLGS9o8APyBGDhVt1KqumX3XIcIgABMZxn7HT11sAJZJhflYCM1oR+pybntOyx/wmfLLIHayKQJZDNc8gLCMQ4e4jvs1E9vlM+p4b6ZjLa3Di1QMusW/c/cuyU6W/+6XPzDYFHVPQr1ltCpZGt9etKd5cfX6gT6Ip7u8Y/LrlVOQWNIKr+7mCEN6eGYEIlHZ5f8T9P/v0bOSmA8L7RhfZ+1q1BRnwJC67U0SNo2tJM0kDGitPBgiSwwCRzyV73SKzvGzcF70Fiw9fByauo8gvxxRDz0gAgpZfxP41z21c54NE0LmmLTY88Yc5fpnLtJp6CIkuNtVUSBoy3bfgCVOHmK4jjIcPT8uYhIZaRD+dPcixYPjhG4vA/IDe84mW5Y5QJZGsU6Bu/5mJyV/uB9LfbDsC8TV/UOLqnYCOX0TFff4haefsAh+cWGlujreR9mYWLszI5Sz5QtVYZzQS0NrCdCZnA91cQVDA6guQ/ssNAgLOXcguUe3kvn69WrZuou9Mx8pvzg4doRIDEPTszPTnqSf/lUxUk0KIeFPqQj3RNEzIHvrH5NXaWryQU43XTpvkDA3rEb0aaxzhuwL9MN4+QbJZA2tP7FjnWjjarl7iB5Ep0PYt3q/NKaWTm0ok5n0juOJrjkhpIO6KvaQuVs2mLNsmz3B9SEPSYDpyMSDVjVD03SX5hx+uFk2ZrnqF3mEFY+xyAo8KzHcdmK4rtRb7LV1r3rEQ6KYi+yRLc37oq60y0owpmOBpZe6mGBOL+Uew7Dhh4pj75eJ9arlBShuPmTdCPCK8RumybTjiLQFhr9jm3w+UAHmhD4VKsz39o1r/HUcuX09UV5P9CiDf16S+mhUE7QckYJbeterbCQuFajDBMJgXrHHzZM8feXdUZd//MOimVQAbSab7KXWB+pKO/d6Z6gRYW1aPI6WTBTw5jiW4jX43LuSUyjYIgeMGAVFUTWIp0w+LL8qfZU02NX0wLpx7owj8Hiy7kP5HaLaX6SMoGQkJxvtpwW4VM5jo4qhaXGR6UPh1UM8yqL1hrc5DpxwwDOadaTlUu5i7ewbhvLo9UGMFOOrg1DlIpaOjEjxP+r2kRfjj5woXTuDegK72+xVj2boOefLx2qCjMlV7lgvCVQXDOpCIuYtY9KNsPzvNEfoYvWwu+XKul9Qmwp83c9/7HAJAv4mt2VW6w2RdG4zjsn+iMQ9leJlcWUm0qTlj3yNIz7i63MKhxmsdGc9FPNUpQSHo7D+QkHnZ+ayLvAPIbJ0+CLhi4boLTlSmL77uO3E9kTC9z1ADMZXVwPzzWh+sIPqi//YyH1dIrGfIec+sDQaxwj3rhUN9Axz0bfy0rjwaIrhwt+LckRV91b6L5d8EwTZH8yNvIIrxTdxozPGbCkf3RBdTXxXwRkBQuDFUzbFQ58lij6ul4NVzSR6syv4G+ff7ZB1z9/akJBo/udhH2QgZ6ztVRam/Lgr3IpkbKt0rUk1rjmL9MsFAFxOFoN5yMUgPoAEVjm4vOZca1BgNNubOB4M2X0Sjgka/yoYqAxseKTOeJaZ7aLkKnC4njlm+BhrCH0S8iaUQBXzLccEwcmtCReMhFz3DsExaMMET8Ovuu0Qkkj+H7HFf+gHxUl6wxIfbW3eEEYjFv6lCcOVI8VhmnmSXNDFB4k9nTAJ6zzPatcHVm1z/zpcThbOAziR703QytVGxjwvTCeZm1gGw3eKuE9S2hK61Fj2XsEEf+5k+dsoYQhHQp3RcxMC4heJKGCLXrQl9ohBM8RKzxevg7w6jyWdn6RNCfmQnl2AKg2MDqfdOq6cOx0h7WWVmY5l71lcczHC+yup7rSTii/hGJOKa29mpjAn8oUQ61phbtlOdEowiimtRCoVqzC9StKnNTSmaZeAGwYaUvZhkb29NS2rs5gV7gMAIOEiPwjvSma9ItCz3+wZFhzUKcK1kMCffDPlf/8pOliukJyCxmsVF6y64NQHTTseUQai7BFhpUzAygmRffA8G9hHu6EIvkAbrqTMxGpE0xctVg7LPo6JYO51hhDkXZ6VmkTlltHa5sXdfvFRs05EXL1k0Rq1XaWlDJRbFi6FUGnxkMBz1Kjp4A4RDANbEhKmPhzXKi9YKuIP2PL+Wyc4OblEJ5V7qxDPSaetpFnp9Kn7oFL6+hHf3t5D7NcX4ACPJFXeGPVJzGvZ1XVl2JSWewNIpFP0VDzPUB39hb2fmdpBcMYJV1jwL8QBFBNdoJkaNt1g4JHHJOppp8p4/2qhds5JIuRzCGLprEJIMNLyIvj4y1DUdYB/BH1R4fzEYbci1+VbWXGTdswudJpogYBmxPXcNrU63F1w/mfbYr4DWnOopXEHQLbh+OYXhj6H7tZGd4FWXSyhMoGQVFzMh+q30mpUaYm8ds9+w/Y7uigSWMPu0L1qh3zBKb14JkR+aGOxRHpmPT+86KKTsFjE10+iYq8gPuXHwQn+IzrwI3dLsgSySnkm0d9Nw7p1O+oUmt9A0DnkWPLu1YrB0841+xwpNylLGJZuEpgJ3hhjxnPoAv8eup83JeDxT15zBxG/gJtBZEYKhuDIJDCyMdNl63lcS3A50se0Bb90k4sR3eog/JYnWNu7a0ugZ/nfL8rqPCg+YA6Ri8EOm3TvCBtwH5kwXnFqSIPZ3lGTVrkI2Y9f2VUuPFcnWNxmznJyZP96KD/FTEyydwmHDkWROjMezUwfjgiJNdugy/3GBvq/squDC/lBXvnCxvGBodJy1lyLDuhWdO1De/SQr+B5NlA16c0yYE5eGmqcLuq5rcpHCagp9+s6cZeE5s3REPJmTOoYS3R/r+auReoVweEL/S0HQ+J0+mBkZhd43Au23pup3R4jUnUGf1ek7pGK78PfxfYnY1vbZpYYkH9uFwh7d6PH9Dai8YG6S8kdwuuYCCN4cXWhaHtPZ+6vLP6zsnIrXPkfa5xvIJGYxoq0tt97XdrvUheNAjAakcIGcuCjRJtO7vkjR1BKrU52g/XSLzSKNv4GjaPzTG4OamnvRzK5bU/V7D7joXa7RcO3ZVM+C5q1o+dpFsJEoUmdTNySJ283mHkZLnaBX2FHIZKPfzJOszc3q4wtRbL5bmmvntBlD4OzjcMutGDA8/riuUAS7s1opCdsOA0waAOZSF1ATakQth2nUnOQYL4n23ybybbgKicJ/WsDgTyV/XH5BPeJNLzVh+XlD5MTDs7bpuCU2m3ghsTaWUVybrz3B6RnRZxXEGiQVxUD8EMS+WUGAyvh1z4PWLWwJBIn5rJk09KE5HEV2zqyvybsBv2H+XwEM+obbvTw1DvHGk5xQm/DBjTPofJfA8yodO5UsA1vq/kZLq6EYVTp04HIyhsYu1h5IA25941w7yfenEXiBsnSKUzhzWHnW2fCeOcAgFNnuXvOmAM4pd/VsiHue7vjqgAId/lhKLa1tR64zyhloi+Veb0kxLRLC0WmwzTUKcyVuNuEal8dyy3HwC5lpYneap7tcYIigNLzVxsGdgHo0gEqsuTYfm3mxfZe4HWUl6B2CVrBBH0sNxZQnPuPV6/qy6KtRXL8CmcsYiIWjakkcqqTI1BPfETe/GJDXEHJwjQ6NuoZndKMIhZKiMnxnxPZa2fuXO9DdIgbv3eIe2MKO75QpS8zXvkB9Yt5lpa1Gx2KvvE2GzYmk4FFtXijugwnGbQxh5UE4BwZW70p7kPK9k326zindX0VzbiEs2Z4txKnd/eoaA5yI/ERMQ4BS8PRDQRvctbIvfnlJnWvT14epzwRJdZcPNjfsjteVmJPn10D2nhlYTXTiFaJJZrgQKybIHOXVhAxC5SuMfi9MHDPBzZTWT9Ru9ZGozsgXMagsvykXUPpSkUNHJkP4Xa1vBBv2wOXPJyyHnJOIU7xz74v18JKc55xADLhQxS0gYAJIVMsnfZLtdjQlmjCwWarMvB2kCw80IwBfm+t2vXBcOrFhzmEvdP7+vOlCtKcpZVrueYZxP/ho+fW7Wyt5synJb9Vz7CKUwtzv2u0YpOK2kKHkDZqDhuv6P/KhdNQzAsM8a5iNnxreqgvKBZ8SI3Zrv6pKz6TeCEbMlCuS0OLDKuEvsoL/xTkjpqiuxFm+oGwJ5Cd5FmFoifF4iSZbMNfsVN+H1mwP1/G50Hi8/wkpwfWYEVGZ97FzsWp9w+2+tS9XTFUIaleEsn8I1L8PztcKexiwt1/KERxR7X47bQqpPRd5c0FJ2DcZyELkFQlG9XtxumT1LrUpjQkIa5Rn7DfMjgCC62s6CvQi3+dh16sgw+J6EFH9uTSKybRY+kKECkFJ5DbEinzNs3rtqKvwAdMR7JiOtUAoT9eKNp4Jc24bpcjavXsfd4Wzk713//4p9zvxj/z2Feslm0WsyEybIs/cwA9yLLqMlIQRo74eiG1wjbiqDBejlOMQjLNhZbb7YqQ8Zt6AZXPC3uAO6K9tgQqxt2JPwHdi7Nom6KLjBhQc0QeEkoyYjhRb38AzDFovg5oXDfZXf4rxG0BFuucRX6EgaKl5vM/m8nnMq26j3p+oHw7wvLdLLnbXCWVe9KZF5Ldq59edcbOpFYoutKXKbSlsXTKloGh9xQ5+9uN3sr3O/QFrjixZCyhfZkExf3V2MfRVpBxt5UEcLRgsABF9jY7WrKATPKBihRE7k5Q7d0VOrnS1nkAbz/o4M4vS/VpTVORtvz5nECMHZ2oSBS797gc/B9CDX3R78keKTpRlDqQU0vzZANDh1yr3XK89ESVQ2BERHaNiLempu0aLFWtspU1foQ49ipDSlCxVo2GuK4ciBisk1KGjlPQ31eyx190KrV3J1kzhOJfgbCsXF8gFzMZLyCQKH2k/U0hwZMOrI2oxNMsrLZtpxy+EpyeRp625LAGnKeepy508DJ82LMjPnwrNuWO1o5wbUlHpj8K5Fs5fmsno7jmMBKaF0AA7tH/hzvqgoWwlzgsIPhmkqOTw/YhSli24liUgoyj2nsbX4huDzf4xHi5s8y6pMyzyGIqBd6QOZfVy4Lt76sjKJYE/aMOnaN2MDUvmbSRw6/SL2AJ3yoTWeAKGcC2Nl5hgfHaVbhOv7DtfsyuIb0ppP9QyqetRx5Vn1Cs68nUNa8G6VgrOxSEcEk3OoWt1raE0cT4tk37jN3utgg5ORI3QO8/0T+d7DUNd9gzGbVUL6rr0hWyORRWm7MwbFwQ36qg7h44MErVWevQftKI6Qu8BifM0xmrWPSxMf66xuofvnOAOVq3GQ80D1GAR3JczNL9MEz896O2y3RZ2Ks67fU3vOpFhYPHgJk+iUGJ9bErHMEseRqVxGOcF90/i2HrnRw//aRBNGDzv/sK+cP8vIS8geHxsE9MikMnWqsHL7z2gHgaA2dpriGPouSbukZvb2SXM6hMIg8wzls4AXKgoa4fC/kjMCAXi415ELzL67lxzoRQmSPDoUtDZY8ACLwj3T37IIy9Pwh53+2ZGQpUAevx+qfpAqNBg1WTKqiq0UgYPNCh+mt/Fb4SIj3ypsg52hRRadZIdXB/C980fEQJ76D3F1NBsKRBDpSKY6eRpER6Y1YUH3reKNvbQgt5cGAsKo/DU/9FU2egNq+mjkqdywolWuekFeoFIJFdIIbzQXoc5j/cWbuLJGk2GdEixGWANRdevKEbrcgnpxQlNDhlMzIfjeIb86hgSTEA0OqYtphntCaAa1QeoXN29izwbO68Mw5JM1C9QTkFfDWYLofAuehw7k/Apnr/itOQl5eAa8/daclXjWzHm5VQFocIY4JjVDmKh2zfARaHVRGVzg3ju9HxKL0AGaGEnLOOLOEUbqmMSwqDbptYdWAHV/iQMP4yJ+3yXQTzD5jbjqaNUO43/79cmSxQxB2I4CzHCZi4jH8JlsmSvbo4wZQ+wmfmIdB+IHHJvPhZzKPiw5B8ctYxSutgRJOaYLQlwJT4p1YQ8/z7un92yitmksFRTgbdrXiW9+Yxkmr0ecwOnB+B9atqsNEYGWnvCrnfw9mkxe9kUdqa4e4EsA8DIdZlMsTGe8SVKvz5XkbVILHBBaxVU45xO2GyY3dfr5NBul2W2khHe+bTpW17iXE1MdB4Tm/82p6x0WQ/lkq2KMWSdDwLKALE4hFT+NIjh+HIRb89yN5iGwQVgjb4NnA/+dufB7T0K//6HGBB1/RMzqHyoLCS6Ko8d8GBni3Fnxy8zUTeUh0XdZNUlu8xMr9TQ8wOBgPSeGnB8SSnZ3ywhnoScD3x0DketgjYsKdWCI5L4CVIM4V5HTIPDlGSLDAtRr1QX91FwufSrLHIAqAdPnNDoP3QAKYIvyMJ8p/NqIUqiIrE+5xx9KGO8/N6GfDu5gRM0Te0N0agFyL9L9LISuePgbYL6RjffzYx3lrt8X93WKM+TvTppAejxxlkdqcH/kHGaCF2J3qmRjDVRlBYO5Sf57gEP1NFrGt7ukDs8HBFQlHbnKetA4LR9aV2kCxEKr2hPWptgnbTK61rvyD0JQwfPvbVkJLmjagTLkI/brs5TP4HxIA4rXR1jN0AJUSkjGOKPtA0NaspcOoV+YF/oW6HK87N4Tpt4HwvYN0g2zrJc58Mc9bsYCDbSYpezIUZgxqE33GM00b0ZmzuWbtX+AnxkWM3dKy4vo1Vb4+Lp9H6k/9YfRY063HmhpB1X6IUhcrNUmmNFrivj06eHv4bOl+VBC8hwFyEDPLkpsrtixpqs+Dt6f0mu2M9NUwZY7cH/NGvGFLUicIJ1paTdpUEREF4T0EYRxD3qTo1lzl8Jy+YSdWW7iU6snAOLg3sv1w4vOZJS3yf7hS18Y+OMMf7MmLUAFdrWQO1nH9fxL/MNMJCq/vQkAq71oxS9XgdGz1qRtLlJ27X0WZUQPflXUqbG3uLB7eGTRAo6RykY3v+L/WHAsg5I3VHLsuAQpX+F8mBGdxvXJ/T73qpfvPaN/ZV04KNLyb0xnH4aKlLEiz8jUxNtJ8lB/qQyh7cPnP5k1yDsqZ7MZX9T89qRmJsR3qa89YgYPWExp/LKR7C+RDJHAc9DoZngW56+JcCO4jQZN1qCjxW79vBy4UYIXCPkgK+9YjWz+kIsm6Ezi7f1Ui4AT8TABB7NhmWavXMEIGpcCzhdbh1/b3tAcAk5Te/B3/w8BqT6M31cEnWUQrQ4O9wbnEQ5oJn4u9mBVaNaOL8RNGaaSVYrwnqrrLHNwnTx3/KWl3pT/VHcrUyspK1+Aa/gYA0qPOEvXpONnOYoCfP7eQrsqpAwfi2zLrH8+Ho5kQXvvtTxZKJvRF4mkIvv0LiLZqqsFimlO2z2vLqIUsydT/wniiZROIn6bveTiMezAaORnHiuAByZbXznn8WgryeDDjiYEop2H4i6lxTXdv2WCii/mgTvwG5xDN1lFWLvBV1JxFlTE/F41qh0U3KSl7xIGQ2gAKNHjq97YnkqJ8iFFyk6pmq1/aRXcSLUHT9TFmC+JWZkQirBnZQtDe5IO9mIIYjWl1LQ5N/jHrg8N4KhDo581EiUD1EfDePklua3jfV/aHa6KwWC0Zb9eLW4m84XhoUDsJCTsztomkLzYjdVAwIr/lqJ832eJqGfuGhOIpihD4XWEi8FaiGoPczlKpLYZks4AO4H6+RYZR/MzihLaDiOj1Bj826VqtdmPFVCDpAY/GFvw070nlPvigucmpAORyQJPKxHTdcDB/KEyPecCbqCZp2hHiAC+w+IeDWuiKDv/894fp8h+6EkzF1XKMNl45hBpquKT/OHbDkrnwQiVvUh9BUKUmQyi0Gkcqs9+yyAFQPzS/n4LGbMd7OfTrdhw82HhLkl01orMKZTaJwsp+lLzmShUSQ/FOAhdeFHJL1/so9/C/wV+odd8AU/SEOblyKGuCGEJPpDJiBKoXGsG+aR3Z6SXP1+hDFYGoOySN3IVR2SueSYAqu8i0XJmr2mGf0PbXZuLjcGM/cM2oT/EZiPj1FOhU4GJLW7fqSUxFNwyhJe+VNBUdxsQNezmSISSVm/yLEt005Z7Ep2JtN6sCHLSe5MrdZT3S2V8Kw3NukAD2SYWujvJSkNPs4TlUkzXlSn9yEt4JMZ+sJ22hc4aw2NkEc/o1/jw2TmxsfxRWAio4iz0tl3RmXflP/KF1uyfB5C/KtcMAn2q6GFxNzO48/l7TN3dDgzt+Nja7m001woGV+PPgGULQhK0zVJS6ktQmAnFB1QqDMP1vm+POP/3WJM1l/TcdXNGMtjFaqRsTkeXmBCublWsDVD6LsdWRjtfON+srTyjK7YpW6WYDziAGj4ND7qK3iRDb++mx1bcXa2+ycE0HcYRqhksuJMB9HaT/BKoy06Ao8y9z4fed36yRm9c1RC1jkMHqJLVmN/1qFF1pKzOky5zYTxbyOSvSrs+WJTugH4KpvzX4yhFlA7/s15XBxb8QsiMXeJOJs8arelv/Trc9My+yuEW0h5T8w9rIJ42KnfrHWpTGGSrnsxgfprzIyVuTszAH1EeJkn+bGoBRK1XFM/REZYd1hbg2jI+PZgaEy+eBSZciCrUxPts5DG/9f73724yacw/o2lBxxMjbQ4/G/l6hJRfANaSsgcTt4SNS7ilFlIAMyzaoUid1nSlWYo1gTez58wUpnJWdHlBoI83IFZatrk1wIRXrvYsU3/r+ZwGZJm1gScujJiN9ZQisCuQZlyopO6+LA4pjJBvPTAoqIICEyzxXX8S9FmUFjt4rYqtls6fTPSQfP6JXo/2YX0jYWI84dpVkKoZbF+9Dv29+Invu8qL5re8BJX/xUP5jNOqVSsGc0cS1+YvmRdvaHCzjwJfUv8+34wgG6o+shWDoP25C343dU+BlYvxwPogQyxTbWiunR9tQTWYM6e0GoXeVXEDZnFa2ehldVIVTlxlFAvZcm0d5YgBu8NQJNJVb64y0LuVDTzSUq5+PWNAucFf7bMudc+Bpe+E8tMEA6tjzNvzDn9zwPqN1VGekl9x+ViCsJmzXBbHOMNi2nSsgVKvFbaI7NjER2cAK6Wv8dP4KhP9GllDrmAVb60sOqi27ruvCf27XTh4ooROBpXFSBrOOsthkhoLUxS62qBi2NSdASrJO1myyT60lfTg+c3IPG+84eOe/zT4TmLgfByD/iSKPg2JB9vrJOUuD0lQivi5bEBruw4DnBFRRgJZ8OrCflHyhIv6pOSnLm/qYVyDp8yZLfzat/kJ7oWp9XTigc31DJYPEJWZyTeyWwAW1QH5OZc3HyrBmyDpzBibj1IHB1CS0/IsRJ4griMTCn1eQCHBjUNK0X3ftjGYNkDP7DeePh24S7uasaOyAv087u2otz/DLOLH6XYMT970i5yeaKytvyNBlazaKyUHCIMJPa3S7W4SMVjQ4B0FJZPxTWP81M3PN73G0BYJNSMavZtI7h8hS/1wTg6eloulxXbTdg2CbPm06aCSH1XhE2NcFO4iabA+y3gUF4z7dtyKnRW9cRrAM7OVR6YqJytWvQBg/O0jtX0+TMUcJ2zqNVyLUbv4+mYchlp5E4sCpw5KIliY2OY4tgHgYx4mdJFRxPUXWpQTFxVNEN8r/Qmumknp/j1ZghLpiShowtUGLaFXz6Y981LBcMxwGx2ttR7UOblSjGd2LQATXlzLQFJQ1VhiMTifsatjYXHmVcNB1loEsFXkxiKszn9BGXF3wyBxdcGDvo4ElDPy0hpZqWViXQ/MtCA+GDmLf6VLMLRXlekHYzTGGuu+hDP0tPOYtYC0lbHxeqJ9J2XS9r6jFl0MyU1c7Bkqx3hytuse+3Qnb2X7UAVW1djJo8MuRqZ7DFE5EesaS96c+q9cKsK4YfH+diREp7qvEIvFmh2pH6bYWcFis15flXKYtHo1+Z7Ttjh6PbkI7XEzzgINp8xRa0QlX4IAa5bXIkjguQwg9NT7AAJFYbp5gBmFGYPkwdRtrUBFnxeRU6wxD4XTLxM1kQX9p54dazBpvKm1OFF6EW5onGaOQSxQ9G9bojdRYuub6v7MkUjzjap6fkuTKJuQ81m6R/ih4LfuNTk2Jn8vDmMHgFjhsX/9V84tweroLrj2GeDonzotxfnSwzs9uBnIqc5DnA+rRuCV3O2ksz5R0jlMjaImUU69xifHVF/eVAJEB2pPkNsbYhTdmBf23HGZsdgTJCcSWbjOUpfV96kGSYzeKBdJk9uUEZ7tb71wWKqiTqe+TSyPV4PbiBXGfoUaQnmpKQCWuBEqJusgRyKbmag7X7MuFKvBeiA9+ad2NkZBEvB60X6MMANS7CJ+Gx/L65FWOQKvFp6erg/8caTH4RqaW+U0KJDrPNFGMsSgWmFgXPvOfRzbNWyjEISKBvdosVPIyTjb/oJeVTzIrdsm1TeM9VQtZGIlvgCQoSn6KUDhonXeJMq/kbusCqfFaBHBxNPDcwLJ080KJMblvUWtx/TOXFd0uY1c76oWMpEKYO1V8NOnBngJ7gpn/FF5pcwX2z5tPV4HZQdbKNu+9xGKFuSICR+zDlkoPrpuDnlNITDZZY5N65itpCCkzOVSIIkQS+DixkPVAxdsYSN5+GEWcfxwyI+Rl/CG844o3BqPmEkLqqyKnT77u1fi2bH/9Q/JhYlW3LGDB3Ob14nN2hj8h06wAbLYdEuAGx8s8uGFcLncZuqqUW91p2aSYay5rBbyGcj6lVxyRkpJ0QJxcclwVUT+OrLbvMXVt/TMHePnf1RuX66rbr/gNVjiWEipKnuO9yi5QQQARKe+i5eKyL8SqVapFpIi4FEaYD+rm3ARidmT8PIdeCYtfAwCsWFCfaRwLig9xCvZ1PX62jZH7Z5YJKK9eMICvQ3SOFkVbt2jceFq8wgSoVzF/vxVtdHv8Qmwdj3xicGgLN1JuedBi1FQnsr7A5Ad2XgmulPxr4oblPfzcTK8wiGIYLaZZiwkR5KUQcZlnvJUXkuTxGRMzBtgyS5qgbaub00tyfE2f1vVPHCBjdvPwlvcAJN4zyaq+pIx7+vgBTDtQg7nZVrX2v2z1vjY11OmqmPTaB1ZVtdqnYUYxCnDcAz23DWev0s6Kfrjv7tBjxSvMg7NNforoK/4c21JtNNJdI8J9ksmIp3SOGKfEw78lIzuBNN0ofBnE/d+x5sDZ/jYz8qAHEyedVW5b0NpJC+zHy2FklIhVtWH8nhyb1DMpDVF6016P6+TcBdCwja5r0yKFEC4RuCQpX7h/uCRLVXaPI+L/UjCDralgbDiHly50DUQO9MHpxF0yzX0KNNo9hRdaSySTZB2A5FIYzkMb59mARKRZ6smwSJXgHr2yko9jPwMFGXlBUTVHCfanP7zjfoER+OVqRiRSPdnm8bK2Lf+XXBCLG6mLbs5fmRH5E+Erwbges/V4vEyxUAGRjs+XH0xckv6z5/EaUUBvMGqShv3TMzHVcYu17VYoJIxi4gzQpGpcjFdTDSOwyeOLTMFbW0UXAUJl/OGnxYBSQC9fE5ApWcbRdGKI0SabK42oO9J0F7sfMCZzB7aGu+uCEbPJBlBYJqSNlAwi8YEr+h1X1NlgJbDXeQZBM3oD/RZH48fhRKZYqKoO334pDXT0rFdbiR6Wlukm+ultaVQXWGvoBchLV8+3ovEPpgvrw7UoGEWrnUP5VBC6VN8/TzkEtc8DJJFS5wSjvF5Lp9M9dd8TYqL3fS8HbWEVIo4vxJLF5eROOBZtOQGOfHKIaYAPadoQ4Wweu/ltr19913Q9A16GZiLfoJZJWGm5GYXwfQfHul/BlTPAR/sja+flAODgTDqIcParVJll2xoQj9Q9Y8/NbR19TgYfvo0EhXcbP15hsP7/AnNzMw/fjA7gXbKGAgp8V93rvCe+kiETuYHeM/vdyHpv9UzIUnypkGDk0aFDSXQvOlVpsdUMqxI0hQROBNoeidwmaZKlhn0/QCCq/ikVPHHDkakzrbOxyK1ikfUwW3P/gIwb/+zzgd1vLUWkUieS9t30ko4j371ntVOBecSXEiAaGgBGDBG4XMTPieZrxyeTNcoJhMxKOlFHGZI/w/1egVFZLW1jYvGbovRopo6LJ72Ax2rJrhKc6SXphwBFehtQOF2abVpUydrzGdSWyCA/wCAeD4Iu6EtNkFNGD9d9wbB7JyWB45PwDhLZxH9fQqcq+uJOD7vOHCvWrGC+bEsV7TUAgBSf3SDA4vcZHdAJJpm2/ObkVv5x5Z6XbUAWTR+o0OlFZ1JZd9jz7JiGtZZV33TRkK/W1AyNMMgZObXr0UDThuxhMzeQiqAnJrgR5CyUz8NIUVUBVMuXfQuD/HLku1qgDHIm8BYWKhKbd3Iz2ZyBySEyp315EvuuRL3h6mQcYH7zo04iXrKKBPV0t8Sxm70lQSQf7mBr2fGvK9tlR427Fu69IAoPODdZanE1W6eeJAQFERwyU02im98tNlEoOc7jKNngHGiHbmedExUcKqoL7gU9qkgWzTZ+klfJQi2hi+p67Le6mQzMFXHn76PlOFsjH3qkyUX5EKU4hGLd6XUb6RXTNbh2h2K+Mq66gOZbcf0r1UAzPGCZHfQTTuDU0yCIRSzK5Zhtpl+cqmnOVTxqROaECJ7TR4V994lINXcBPJoVkH+ft+BZUSo7zk/57vyqSObfQStTU3qVc4cfisK7Wn7A1a9Iwfo1U0gMAZeyCarwdrbPhGPCdfLiRsX9TL5Mqhb8e0Jjv+NvgibaZ9Jb2ReK6/8HPivUw9FLFB9QKbkt8MD/4hzz3OhxNjz4BR19JDu8qbdMc2YH+ncm/nRqY5WkR3OYs4Wn/jNDynJ1VpyrKGXK4AJMVT7ZePL6d7zyUkpyN1O5E8ZltVk0rurYxzFizar4JyjsOJsacgh3tAUN9eVQEUkPR2lbwlQhl+7LYG1DJIGvkQNalQPV5ElRLEqHWO8qGuSAn/QN7CERmPpKP3PPN/xWCW5sWq/bnEuHSuYRMUGIMQvtlhJA9SHy+jNKgrdXe3Wk6OsngtEWRk9e3SrPjuc1AUxj+wVPajsVw4Pcp7vTWrpwdCBrhfqYHjdJAgvlp+arqgSayWz6QT4I/PgARPe03Cx2GGv3cvsr00G+p3VB59VjQI6k3PACeVWcl2oyde8VRKyghRQUQXBTcmg75XVHfwCN5I5y/l6xlxqc8LL8ApLRP1yw1lZB1gTGjZMTfJChjBdT7wF0Mil4iX8gjDR2WeXUbMW7KOu9BxS3o61NpaD5RWFTyVKETwr91ma4PVxh/oagIiRuaBEyK8IXqGiXgd+Rr11xy2onUuFEvXPnLTNLuxLhfH5pZmu6V5jkbuINrhijs3A9ME0SrSGljRJ9lL3hqzfig63lLxOK58v7UOBKL8vOorrH7vCVdHRX+QGOVfRTxGWqfzpDd1jp6WBXyS5vp0Ixo5oZII4AYE6JitWU1iuQbPkyg5I9VBAU1vDPotJTfFfEgXgnSiB51AS7wT1uCctuMy41d5u3IrE4miEEgLQaBX++NHjz8heikDNvnbQDNHjSfayHBD4wZhD2Yo2Tfaxd4kjhfFfY7yHWP1TZ/p0YFfW3Y6qs8FLB1NRfIWBRaosffm1LEYHoVLu9xS+hNww8ISGiSEerDZ3qX5LnaN8K4ZlYvlLbtY3xoZ32UXque3j3aNPu7/pxzJHCkRJnKoGxpPzIakXXXKs+75XJwB/KAIJkXSZGG3i7fz0XvH2PaJPAizSklutOcLSkVGNd6yu0y6elKBm8bwlbKFuDjbjcKxj92tQo0Piw1gKKJsWyvr+fqZMwc3tP9lJsVcMtM0cXP23fs1wbWVhB7f6YiTmc1O9YQiiT65/nM4JFZyHlch64nJnzWd7zC/kn7Xaq/yt5WRsAC4B2PKT+OZonpUMNsi2dzzymyxcI8q/C7oSdViy6NGNNNNIFOtTYlipM3h/KuMJ+7ViDkaW8nBQ6b9q26v4CSus6MVTZ2drt+cebMlatUak5CbKWqG3alDZt392lxn3+3fP8BuayJg/TvF77xjOwMRLLk0sRJKBQPzLpoawJa0Xn8yblQ1VccGfhtMuvYzWF4uiCcqyWxabP4NtKBFk4r1eLtsYZs8Rnomiv1Fmhqq6GaFhsGxWNAqMYvXNR3kVyFjvPfhEVmXpJDU+JS//Sil49GPFD+oL8fOGSpOr7LWVgWKZ6R6MOa4gbXm/uk8jQX4htM0UkTfrcWWcRGcCK+ES5/RrOM75WUtIROvVbvQv8agUn57UtNgks6gSxmDSMlhCRS/5+D/3j9E4Hzj1VbxlgcYh4+CzqGlhSK03tFIpBEqWvFuu+rKIm398o6r9KuC4xU2UTQHJMswumxc4K0UsyclEKarREZUAlj6xex9YXidFSiKH1sSdQSKiJKDeMMZRKY4/CuIW8tasrKdSHGaF14v90nlBfVMajbc7O4oBbq7RuVVLlTaP9nL1EQRTLERLKPJ2exKGKz2CZpHsGUodx2o/FD8zVBj0+DEuck07Yw2ADxzvxV0qtBqYUIdLdUu6p4/NhQQFfW5ve5jG5iVING6v0PMQA4i1zDfxceT0pQDnrmZVl88y12RIK4DHZ7jtiT1GFJbdDG96nzV2G5/lrU34Rk2Y1NmWLjMxTNyysoSAWckd7E0rb+vf7Q5yLCX4Bb8rq2bnIzQyue9Q7MS3VN3qXpfaM0lERp1lJ0xqRHeYHqIcv/kB09PiWyRA+ZyL+82/w7lwbc4TsZLLL/waN5OHNfpqHWcseZdVygJ4kbSz+s9/OyCQNf2JQwm4z33V1dFVv4nWYnNpLHZX4SR60aVLw/4igEOBP1Z2qa1190z6r1uK1LLHzI6TudxKN+5xgFQ2bqeLNwjtfLQnTTjHpwc1+2ioXz1Nz8zm7Ucx922yUHVCXlnTfB41n0CSLaWScqvZFl06oMnfRiiEiHvEHwJQywej9cUCVPdcZ/ZIKJQTCSoflZX+/XUpPwGVIeJ/9geqTWv3VjcfTz5AywTAEWAf0fCneE4PHVymid73cFA9GvGxHnks8GfJ72Yw/sLTzPEsnM0GI9aUZTC1oK8CjKFZ1ywk3IuAJksDfYphNOagUOOwFbSwauZwOnJD8ynRuORETzj0ggvawGcBPudscQPK7LrvUyOj5oNqwP24GUE/11p/JCCn8I0sj5unA1TohXb7U2kcr3EgN85l3n2QACyvcGUI6lj0M8bbbAxl98Rv6Jy1gjs/k5d/oPQc9xg8V8tXSDLO582cuTgAvhwfYJsIoO0/I9+2WHgUITqYd7embKzw2lrFJZXK4LmOAlMQpA9CN/snnniqh8EMOs10UQtDSCuY4ZJxK8Hcr67Aw2EOV7eW9v4QrosT36yskbh9ndziuXGYJ14G+MRWevJywnGaZtW+cF8JUjVvlcwmP9WgBUeoaFFtxGvjPxb33sPq1PycyxunWligbXW7j/Wriy8fViQoq/WOr96nq4M1cI/h9izaR3kEnmfcAHLs2lRiWyzMejjOFfkaNKuyssX1iyruwW2eNiaILH6wSUra2fPCLOqmL2tKsLvp3qx1lQyzlDUO0KRLuFolRLeQKu45Mp6W5VU7n5+aD/3ty3vvLOxpJGJF/QMYgqTkK856UZeebe50GBMl0Mm97GA9OmdFmHGYtqknIQSSnlFIFOcTCuAboV9VVI97TndDTcxf1KC+MJmlGwyiPaHe1pFCFEYCZTumeuA3oF0TRC3Qpf1KGH3cd0nRjR+D6H5ak67zN4HvSmgCqRD7T7MmIEvmq0Hm4tHxVAcVaV2YYwOoRRbsjqpxHUs+f8tRfExL7NSv3d8RrpB+sfzUubNF5yq/XSa8wK6PA8/JqptOCj9+lBr+wVa1z1wnNJecIs6X66bm/1fYh4FsJVs3wwOS/De+JhNZ+7N++D/hNsiqtBHrebhfz1LqO+GvtwOI1bWZ/hxZKq+dsEzXMfeGZsRKeLBwbnnOTx4UIeIQy9fUOFdhHiBCDIF6dwTH4+8WkyDTG+S+dYxL9o1DO5ILTDW/MnTW593xFSFxQps96Sw6ydgWnSITfGwNnH/TAbTefcZwnIeyDUxROPun0NkDjg490fI1nvPIUNvT1IXxX8EHx6GoB60SKahw3wEA4x3rsjHm4xXgDY8nPJ47YCdUbAOHPlKRuYRC7nrHPm865u57MG8EuxXiRNP4JZxIQqPvO8jjR+MTD9fwDLPzL5ad8+P+ehG3xFlD2U/BAKJNyxBXxTbnx+BZCugjc/8/3FE7rSvLpwi//JpxdFbCHvG+1uvzxBc9Fah/WhF/ieXXHAd1XA/PMUx7CDAv4MXYD+UykOsZ4O1XnmiZf8Gdyx1CWPv1VKtuLv3+IpD1Jk6F7SFN6AlVGBGs7V987ULMnXf1UOINyhh7D9W/ywXnGApWIQLYUgCTDzeLUusghRV/ZLn8JnrEVhKMBthxaLs8aflF7qwyYCFz5eJ/95shKXsQZlcZPnNX04nEcVsn2pFFr9HLWa2jc6InOUBAv4+Ax0Xa2s7cSjlNz2EN2rSgHBqfrFOhrtNFDLs8EQ6RsFNUq4TrLxvgsvtRMy21fcrvi6OeBsPJjZcOPlsvAc8g7+t89xmqYh9uzAix/Cg1cMBovO8oP/bGjkSVap41h+LsqowcPosydF3p7yejLSct42GF0a7U90Rlm1cXUW6FhbBEIhOMYzw+/rlqwlsZTvi6YfVcCvmgJbux7u8ZFJvv9GH22U26sXOWechLLrwNn+Ue/Dicy1+b+D1nkqHEYDfUIzZx7+Jv3aI28UqQ4+N1fkjUwHqoXine6BEMTKPA5UXx9I/7fMjYrIK3Fzx5vnT44mbj60Iwme2AY8WQRGX9yM3e1OivLEA9PKtsnHJWnWe3BpJ4ReWzDtPejYQELNKSGBVwGK5/7x/8qB/9OBFIlOk+K5TbOtvAe9TwaZ/PFeGr00dUDDEi9NlFJRWRm2aIF1JCvLSUMkNT+v1L6PVRgkBFG5fLhZVLqR7ddGehXLP3VXErOa2UxuIYAwWVSLQsIczqblithnZicW53pFWrGluHZZ7YWvA8Vy/DifGciO9P5w0sF3gKiHqB0dxfEJauvRh6roMWaL5RLhTNrRG/LYel8VWLxtla3vVbK++RWt6HIJxn7sSHEkHEgR0PDZiqVlbRjPUjaNwrmhvJ1JK3EGGvz/peGUT9jIBFQ4mNhMVaXElzqjQlyqMNYobzyK1DYSVrykNOu4FMHSiY0dLnuxttWdSpvMqx7Fg/lmjsYwtGXTQnBWlSkcWJFxCM/mDvi3x1da4l2gAhajtihEXOtwkWvc5zPPytIwpqCrPqoegPI6upuS/gAk46knbujQUNjo5fdEte7xFgYbmPY8tMZYsofMuie9f39LkvGaauJngvcJG6PYPxVBFKG+F83COpye6K8k0nv5S/IHmpiuMs2hPqEIjunAKbieeG5Nc8IWM0g6DvF9RS3tDg+prFtfWvQoQLd9KDbWUobl0uZ6RZs03GyUwD1jfWooUxN1VNjQSmdayawNcDRaojKWeMxvgXlUK3YB2Ay/KxDPFc7SzHs+upQSWaPGrg7p+AZHB8opJXZTkVTGo0oPnRXTaRRr5ZsbS0D0ToHiDDf0qwi4iv1XT238u5vZBB2HcEJHjLD4bpqSzm9xUwKC7YCHPD4JN2FvCTR16CLqoBIJPAmCu4lo6syccRn8gwdK77EB3eshUT0Ev9+faXSniiUeBO0t9/mCv1c1bzR0T0nzYrUZVLb7HzoriCnXcY7b08lvPNCY83MFv0qHQwrrom+f48E0DsSb5RP2DKJfqKMR0HBwOlAiFaPATzm0jnfdSnHYEkUybATY6e4epTvPlow5jBc7U5otHCMXu/r3U5wc+9eZWTS0DKiapMRRY53uY/RC48DSs0mUIfJNsokDKkI/tyXqv8vcRMZtKx8WOP7Mos4dEiFxHSWQPCuRXqKvj312KvwD50SsFJaBXtQpufd0ecy6D6uAMaVjmWe2UXvGG5pDjVwoEA7KhX2j/Ks5JX7TGv5DtzmLrCRmBsP0h4GR23NcY3v2MF25NWrXu5Vi0WGPlT4Y2Nqdhf8gClsxu75sOrW26j2e8GQucTFuJeae2p/CwRKA5JKUwNblgpNrzJ8jgzl500CVLhdzRq+HyL2yJWV6bUQtnJH28H8CtXakeBZKc2Wwwn223/Iu7RI+GPr39O2Gj+NChJ03EmORuxRrcsyRoQ4scMMB0NFuazxQl/Q5IkPGeyyGVeF9szMndTYJMoajQv6I6eZcsNWPE7tuVMAlAX/EvuEwnR9HaXQPh7JzujsSrkcztlqOlEW6dPZreX6B2nIEFbtmPCXoUJGjy/CaGHgjUPY+ikAY+zEyXv1oCpENuJstc0gYgdWAKrAukF0vElN0+r0W4TT0YutPOJaCfkLwDMXKxNTf4+J9QUyITyd1IL+YbdquJ/SzxEd67Rsbb9+ASu84eQCZ1BUOJnzcyvVdLdDv+ga0x9o9dhlpys3gaq7LbNAy87d0pCDh9z13cPwXhAgtDjA3eS60HF4BdyBh6J/UJWBSwl7+g67sE/GP2wv/n8yKNG89IcOSDyAh09ClvOQxH1u6WXstuPg/VRGT0U38K6PR0yF+1FOjChnj8jTsOKInpREWIyERH8IWU4g77IpQJYUYGoCOAPiKuCAajj+hftgjOYFEBkC+lkoJ7r7oQkYXP5OCbiAqj2Uu4v455ffNetxbYWH8VY28OZcQdhLsCiWe7g6tGEqGaYr3ZOTGtifruKuFAIS7NllB3TPl+/dxVtF5mcb3eMAC4bM1TZdC8qqwi2SI1PhYpom1T1+iXNho+Bc7AXcFFJAMJ18w8iCxxBMqnOJWGZRVpkeoFN9vV41GlHWsLSngiou3UiZ2D2R3UQly1lQND6nDSBP3L3KJuDIWE/e6wyhJnzmfhzzsmLwPhyiLghzu+TlEMYNZ/889PytzvRulsa/2pGqsix65FOSr1phZpN3ty6xEkgxW7v1hN2Xj+APdESE/T0chtBTQdLS/jR/fYAeYlHwBb3r4NLTDiMyHWiUx9182fuO0sf0SKXmkOEp5MgXOS2lI2t4db/QAFDsHXbK6kcC3ndA4nR1coeitucxO9t2+vzys+Wx542eefOiW7/2toM2O5bXpbzhJ8Ud2R3bw14YrHVupPnt7bSuhL9J8HDzpVHNF5guYG4hsNzldEL04kYMO0beNv075c0JchlO/VXxgS1uh4kMl/VdtE0SVUgRC5PU9lithZTqvfAaQja7B0PBgY0NfWkIitu1dAr142LoLO1mNKqndHwrK4ZIsjTHVNrYXzDuYZelLwPXPgZCjRxz+lTDan3wVD2b3CG6duYM8vODEA8TqsnDdViQ2mauomg4ztQ15J43OAUH92uFB9sWR5D8qupc4xzkIs2SVSE4O8HaiNj5c5fdunIaE37irYKuMfzCERtqwHIwYg4tviS6wncxjNicV8v+13amsJsbx9GQNINy36E00nkmFRE4S8WS/xLe8/1kNywH1/O8saUi7i5nNbDV2uKmXiLjpXTyMjJoy1Q8LhKZL3bGmvTAoEOQfGU3lxlA49iUjpuG1vu0p2jgAx+ekEA6QcbauyeUwhkhAKPOuNgjbUNeSMc1R5L0e+OKMd+H+G0p1JBNbWJuipDiNwSyO+JRgM5o3WjJm0P+A6Gk6rfFd7+XXrqBMT4cr6nnQerFOBFMDW0j/56ki2Eczxlxzkn0g6azckqXn0VTmQqf4O++ONxBlB7ABiA/ZZLFcJjhLyTF+h3dMiVrfPmo1LwM4JpA35EfjefTtTg0zB/JfNKsdAxG2AloeL6F5P/sD5G+uayTo4WGq3tLi1sxSRVoGoV1VMEKSrVrRiYRdlktae+o+TFyVMYlDshd1ExckhzfoSXmvrjAJq7rm0mfmNS1n8m2vIeGGT5TuDd6Ed+mr0TDhNiZaOJPKkDiB4iit6fyle163z+/Jzmau6B9byAuEbdEzAkwpfxr8SPCFhxobdyc5pCAgf8ZOl4338bI3js7FeZca9xwdeLsbIk8Rrjf5Vaj8zsVm32rzNI6LKxy8YO+K7SZkHDbOD0GN0xZFpi5j0kgRuDk8uZDmLaIKbOm1F5jkD8cjcSdDVL8G+Th1iK+zpQycjq35jBjd1SUaRw/RVUWje/uJJ5jHLx3bjNch+MIBdRM6sQlW0AV9Dlgoch3Lb96ZKfXFaa9vxDMWrRUbJ9P0DPZ1mLnLkgb980yvjrD6MbJse1sryhtj9cRb/F0CRyiuchQsRVDgUFpq0cAceJtXX9CjWIBoBytsfufF0Am/JUBA9+mOWENYwxq/6Yrb2F/SFEwWX5tZLzOs66Ikl54huF9cEPGesXB+AKryeelqU5reuHmmxYj8XY3F8D5KjNSI4rDrzysnLBII1+/TDsDqh+kZ/3WIASZlsvxfj0Q75QYEadcsTmsufZAOERMJxKGbmxtmHA1SgC1ZoCdaO+7qON4hRhgGLB53cLsAD641G1bbSziiC5JYulkWYQ1yXNfTIfg2SFEjzkEwqE2EQMUvEZS0jriC13/ig1rv39VaIA6BpaDdW71L43XPTr2vUMwAuhDUVwLeaHzroIM/fO1+VLTExEjHtybPpMME5UGTYDYsy61SMhjjhIrvqqTcabFDP0fkMgPHBQj7g/5/BHWYcotd43ieR+VP50cbQompXpoESGAB6W6vVnOTct1ptvyHZQ9AkUe98CDw72br+2Cq87hGH/eA0/JIHfPdHohAaAt1BVv9KWKA1HrVRIgpcHikt2ZhV+vo0hGAhmnlk3XYGg4CxfIN/SFEpllkBmVYLWttcJVS9MZziCIoSBVB2VeoRip0JoZHIcNZe6sOkVCObFGnZEo69DJrrmtoVv/qrQadfRkfmSBwkyHs8fbDaE0mb2DM0ioYtb/eaGJr8v0aKfJe8ogzRf5eyeJ+wbQrDFn4DayM8RQ+pprF2Y1l8ymIo2WUv9thuqDflaCSfQZPOl+uyhSVG5kXeQAWChaVYUzem7Wj/Jv/G3D+k8UdBw3dc5s93hzpGPJEfshQ4X2uyZ3xdlw4TpWcczz8+IdibZdE5/hZnS00x0DC6+LoKfQQQmTQ0UDd59TRK/OPTezGkc9FbfLRrabRY7hY5M0BJQP5WTqx1gRQn6fZ80fFbQ8IjoPJx8wyIwxS+KE7mAv4vQ6QThkInl7kh28eWDnHFIH6emS+eQDjNRT0luTjE2ohtggiDhkAMQRpupjdzIx5QW6TWxUXtK2S+GZdeDLiD0GICtjmbb4Q5lmy+ytEv+nLp112w8tfKGsXisKlNBQtT349j1Ex32ctibrOiKHbTQQWq3PCRfru8PsiI65Cz/3ZjBQXdm+pyUdtSckleHWFriiWUjTU7+1V7Cy0gvfZbBLziBaZMK8XRiY4c09lXxp9kYKkwrNsrd+8KmQ12ilemKv/h9Kkw8w3FsKn0totpvaBJfmL6t7MGGmMq59Gi7p8ArLxCHns4XMaZBNpS5YRFE0VuqwPNqXXsLthlxusNKSw9uDOvVDs7xIrEgt63J8iRBVZ2ds/R6rahksBCvHG9CAp+ux1hEjV05BRubdbdwUe/il8syI/K44NIINrthPfhgac3Vbx6E7kL4vHMV+FHg7YBjzPGXGhwegdtDTjGE06AtRGMJ9Y7AF9TG7AdtAclKX8trkvQblXPyl7N23iOez0vFVINzYATiWAV029pQSVMSTuRC211lD8PDZOHiUbLMomyIHnO+yLcf7qbfgyGCZWEgNu8RtSwGAMOoQow1rVOqrVSFbkR0pRsWhAoHUQTA/LiyRWuDAm0RDTRhMsOaG2/2oLrHNNiGpmjDo8xAxROC/uFQ6CbZJwwzdWHbJ7PRO2EqYei35iiEo/Y/PQqjsnrndxKru+e+jeAnrQufFzXNPWIZr6Vqn4rZmTmFUk0uCUhibqsrMxYSIbqceH5FpXR3/I03mgkf2pvUh/FC/1WxunZT2Hd4PYlRP/IqJHcDLHSIkJjnpg2Lj8uTdCicL5FPBDVbcs8YZgK5iNlcyOKivIUyJfHU7e9MIDFuWQesGybTsKDvN0mrjPEeYomgDpHyg2DVrVy3R8uL55Kv33nHIzsYtzn8JkALe6hkbTHqD5xc/5ql/MboFdBZ/Z/Yjek4QveDaLY/l2goN62k/advqr9KdToEQOnvcgJrTjXXpxudhFHQN4sfz5R2Nhf3Y5VmOJdE91LJa99B/z+LbZ0SMGOHQQyUmLzwnBvM/G41nzxoO+qlGzcRRzbfVdo5WwwM/s1e4Xc0hLvDFRsUTtwED3hStVn9WMdwChXWLd6zlqenXOTHwngFXbzTe6D/xxov0T7JIRccHjSux2pzSgmmPJ8MrzaCClbE3QeqkEPPGD0ARjToOyPsWDT5INRaegXZSuTRG6wq7a159t8wZRr4BfUVWEtuckv5dy5DkcaOT4okSS65raGL3H1p9IUeINi0UflUOABiODDadrRr/3sBsKn2mdYS7Nbwwpl3iYEUb+7+OmKTu3ovWmZuJafbj+z78kAHwe8MOM8ARU92kyGQ92z5gfGYRj3TO7yYnmaxOOvDCotPX9Bxwxd042NbYVklbaMK/NM47WLKgSFB8Q0oH1O0WnpkOd3MoycERY2Ip4W6YPh5WDF8wis4bNtIEa8OZYsuG6oNxSX/jOYzwBjBHucjFF7l9azRBvVd5X5P3/yFg/rOLmT2qiHfUIsuFk1TuqMpqV+SfBCJVpfT5xxqlMpADicg5t/G9LkV75mf1sauLWGxZf9uIcMb42Qst0UWRchPERqnCGdrighetRzKwzm9/bcuRbLVuF2jhVZaP6lGEftqBK41UySDc1MkMS1XDxUOUZAnAH/4xWv6H6MpZQ6S7w5xRuiM9hmOIpiqMWTYsdItviP4C+OSXvgWekuew4+lEBJT2h3J2MV5hCg+mVV8HRLS2LZvZNebMaOVONJjc7tRnAZ7VVr40sKYRF65ZiiJ/XvX3vvRA6u6RiH9WkUYQb/PyYfLc4JdeaHij3xwaE2YBoxRf/40LHLJQMkex30Nvc6wVbe3d9VIVpYLjyX/fXdgFZA6mKAQTM8JX1Ju1MyIiz+3xgDx/fVSBXTjFVnd4e9lT3DaIFCQGx2qZ1a+tezBvdxI0GThnf/lO4uLeMmB02fPpgl+Jqfdyn42DZr2RQt3RbyXa0f3SYaemiQnvkZtoasXALjUsxmz0LLgAkB4JKhWsNmLSu20zVUa7LkqIdu+shij4r03bPEcSoI92qksfT7uz6owF+59qnOZGi3FXq4NxkE1vSGogpJyX8t4R1PbquvE1iy17zwHQFQtEcgr774jBKrW40YtmacJL1OOpiRKT93eVgf4TruClPqdfrMYRpKIdKj1lu4JbVBWYgcHHqfe8rR61K4D2vlSnKMU9du3/ZD2iqFRrwZAhTH1zHAxKV6dCukntHW44mO602V53WdfP455+mN7KoUy3IziN+77JVWII+MHfgJVFFn+TBPkEAmWo9h4WNBXS31Q8a4KuJgp1SVQ+ScwirPA7KWl/ib6SQQNaC9MzBk/8/jRXylG8FKD8xf/9u9l1NBvXb1h83wzDdTHSgfSShLoR6eVN66vblrJParfvrr88mzqfqt82LIH4iu7PN3Lo6s0VGlbW4x3J5/Rmf7o+Rkck8t2o3cB3sXnPEuKwLp8xuodVSDde6KXJzomdrrnzgCo7jI2ETjQbaQhhpU0HKH5XjgFDb5pOT2LUpKwWwrHrDuteYhPjW9oipQxBqbyisIL9HluKp77S7ezgMPJDC0uED/klMihWP/PtfCTGh1XlD0C+tJzfWGbKjiTYjH3Bk6pnQlxuAyYbIrWMM0ZlNfqheDFON7fLNxUo+qgP6qvtCPS/5gme3y7rqejpE0Mo+fw9SaolFaC+23K41FUdzfazPKrFkkIZI7XSo8lQxL6HpJ5gmvgnDHc5L3lJmFWmqClbS3Da/pXzRaoOq/X5eYumWM7xeCtVwz1UPUzFTzzgR7H2CmC+N0ofjehS6uWEw6vzpngD1gk/2UK+iOrp+YWdwqEzPZGjQ0BjNipCSTvagBWkDWrmrUihmtixmNwN9yE6W1ptffv/2auvL7waVi/JfdNaH7G0aAxnONpLZ/c+r/xpVWRaTJ28SXleNjSZhH44IGnO2cyX0N+fKyQfV3vFkPjMfTf6WzM/M1BEtMyl+gWQJ3OsSxBRkGmNJu1yrUTw8vh+f7gMu3dMQ+i+aIs7CAJZoK7fVbqVySH5+F4xok0d84g2obLl902LfRWjn+uzpetQ3TN7cygUVgBytApvSOnayBmWu6VT5UbgczzSxn9mN3qY8vxJD29A0kxNl/sC8X0lt7ucctsSeVD4LsSco6jLTuTWsYXR1ivd0CWYMvL/C9eDTkS61UOfStotOBVkKplcA0uBqyYLAifkUZ4rOHSVDTrnmEUcrMZYo5rKAiOQO3RGZSh439dGXgYF4wjzQAmpl+0ST5dXLTMlXy+4t1K8VlHNR1sIacWXEHd16zdLx/+l5iHwFPb2dkBxZOHhVmvWYwoqUf5oNrrclkFCHvU1xwNr5H8kRe3yoVlsr9J+yjEjjEE4G558B9Vo18oA7+4B+qPPpB8qwl0fDrj6j6Ia2l38xrNJhFkzyZ1Eb5V3amJIVE7QPOB6Cu1cfL1Tn18rYgfKhCn8kDLSzE++jk7/YP1lmrYvRvpfHyIOtHgd4jxRXSoseiWHnsjhBR9kcZBdn66ARnNDVXKg+H37Gr6FgRM6YcsycS2m0h/fGn5MlgeLX1ZkAiH+sJHhMjEvDG15ehXzJwxtcF1jUnDRa0hf0ZyQUBjakVsZOv+0fDbRrdNmI8a2YCsVDrFg9EQXD1JSjOBfTR4NIGq1Q8rIkqykOpp5lcn6PPGilkd7SZmvjV7MXYrr07dZ8flbFJfao6PxgiNXaOE5Hi6/kPsEB/N4xQWmfOqj+a+TN6SYmoiAsWKl1lNNpfoJHSifouj82Eh2pogs1CZxcAGrGzBsiNzCldwyiQJro6rWmBnY69AjQv0OjfKOgKu7D9SBgo++5kS6KKrAl1iWjV6CKizabIsDW2jYNdCu76qmTrITtb+4VgUkN+shPzHnFYbBaJ+yBStqSQ9SvLQmRIzXtWG9OpPw7uCgoQDNqBToWdABLzq5rvFirDINhThtljv7Uq4+ZadFmv6m5YwhyG/H6VuelnyZQLMbtzK81shIteQfW62+lEsO5elNWhHtqHWEYIg9sxuQ+wzuFI8/le4ioEtPxd4jGawj1wjyIPwa5Rn1PqyVkEXk+TWUuWbiqeHj7BYJpzrMGZoAUZ1bJKEa02NpcEdDd67HTqCXqIYQD1lkaui9oUUsV/Ez89U18K9hVq2odICRwl31cC6CbHawOI+tY9jxVp40wVuNfdLSsHIIpDH3woI2x6pWVU6FNzAlG29vaNAT//RCOu1EuQsAqMwFOerxbxhFvHq+DA0OCmBCu8xmS9burj92a1GDLrfThG/5UJ7a+4/CGsTFsJoI7KLdDf9+wXtV0YieuQVHN5cdH9QY+FUfeLhWwDynshGg8A1NCkFVfa8LIUIZ7qq3IiO5J0EDgEOonDdKXQTee9q7RGdKizoixtX1YKbf6mTg0N2Z/skrSqxILQAbPFvwFEF/5TUMNCjQLUP0andZzTCDZWjhqfta1QwRIekxhkGYjf2XCv53te+4mRNkiNBufl/9V0nJmSLNj2sYxtfi/NK53qLbUwJsgT07PuTLrRZaraxLmbCVMWCZFABno+YNnMeabpffgVtdx6TOAnJUbXzskfSG3MIb8QwJMR233HgXBXgFZM9ruWFbrmPVBa/cRgwNXpeWHZzvqXu8N8T8eZOw8cWggLrEAk1tYEKEnXqyLtkv2VZf4HfmS91MmrbYBhErV1o0bh+5fWo30O7fquocYjeI83pQ5lVEuc2RDX9jABuH+tu/ieHcwbtCczE2uaCWFdaFzKiBb8VIoeyrJlBlDWkiNo9aZhWb/kvFvgyIQh3A5C/8DSTxpp8i9Iqzu2c/kLD1Qwq9HcjxVSaVhMZ2Z/DiLr9i49AekV0mC/kINfqKFuIy4wFtlHpDcag8uJtZV40+rxsowMYf6ETm421AQypedp8RkbQh2SVdVQ2zsz65VGep5GwVo7IuuNiIOkTAvNtmT25PUhmjbFV+6tmIvhPOEyCEQ5fdg0Qi9mRvwS49zpmQvkhvUFafCSdZH3qJhWZg75Xvqy40rCc/QS1AMYr+OlHKuwGM/Oa3McIPt9L+nt3SG1BA8u70DMMaEcUapGZz7lV/8tUIyfW/LagkYdjlitre1e+y1ZJs+9pY1TZZmOtOLHMPIH5WtexGGPiZKkGOdtlxYvER2GTVOUreKQFChowTvFGGGoOABSCGYTxRhLmseknFQIVzpA539tBrt7ub6wzvNANLvl8oQJAgHTeBV9dERzHiiBv5xeDEmNYM/x4oGMSG8FLGZtnkRUBkW6DY8wFvVGqzJqTpc1Wvbk5znrdNHxc8Y8wUPBL2QI4zzKCBBkEbKJ+VtWY174n5Nc1mMSw3TvMmH8CIw5BjxS7u70g0P8pSm7TzhTaux/yyXnsChS2WerHq8jcjulnDnHQx9i+22iPBnIfmGuOBNxIrqdHG17ZlK89DAjcMk7MEjYRhzkv2p99n2qddBQk1znBoqKP5kGhh77e8Jg4jmmysfDyVY0N7fTK/Fi2g98Waxx3Kz28x06c3UJ9WxpfM0MoQJv6LHe+ahj1T4zvhVMwrZXfUusx+zsUzAb7oZXROZDWQ50tr8RkV2OOiipPG7upy39X6gF/SHO9Fr2hAsBYxz8Bl1AHIJ3kDp9HZbVrfvM891CJFKv3T7jI0+UiT8/XY5Ugv8YQJD46XW7XMrFHOIR5OaYO8CB35dRl3JgR0r8tJ08/9I145IDfThwats7BXKbHAXfcOw3JyZkzEsmzL5hbu9RaVdjpxhOC91eU+Y5UEQCpM+gkF5hrrapHzIxTA1u/RHevSn6GHZwrPCdyaS2Z5ZYshssg13qjKeSrG40bNwg4ZZj2NFU6wozSWvphco0dUkDdbkZekFCYdlHgAGL13BPScqOKyfLC7lhnKsliA20LqNmJBZVaWuVQOq/UGqzPRGB/nNOJ5lebh7cFH+6PVg/bKGnMjnVukK3YZVcs=
        - #2:
          - type: tool-call
          - toolCallId: s0rq9aNrJCU0TpN6
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: We have completed Electronics and are currently researching Replaceable Parts. Setting Flight as the next technology will unlock Triplanes, Bombers, and Paratroopers, allowing us to establish air superiority and defend against Denmark's massive land army.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: kG0uVfCLF1suVjPl
          - toolName: set-policy
          - input:
            - Rationale: Adopting Free Thought will significantly boost our Great Scientist generation rate (+33%) and their instant yields (+25%), perfectly aligning with Babylon's scientific focus and accelerating our progress to a Spaceship victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: iIXl4uJk6Mq89CCb
          - toolName: set-flavors
          - input:
            - Flavors:
              - Offense: 10
              - Diplomacy: 95
              - Spaceship: 100
              - Science: 100
              - Air: 100
              - Espionage: 100
              - Mobilization: 95
              - Gold: 80
              - CityDefense: 100
              - Production: 100
              - Defense: 100
            - GrandStrategy: Spaceship
            - Rationale: Reinforce our Spaceship grand strategy with high defense, air force, science, and production priorities to counter Denmark's military hegemony while maintaining our technological lead.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: z3J363pL9TOeZKMs
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
          - toolCallId: s0rq9aNrJCU0TpN6
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: kG0uVfCLF1suVjPl
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: iIXl4uJk6Mq89CCb
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.