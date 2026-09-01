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
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Defense: 100
          - CityDefense: 100
          - Espionage: 100
          - Air: 100
          - Diplomacy: 95
          - Mobilization: 95
          - Production: 100
          - Spaceship: 100
          - Science: 100
      - rationale: We must prioritize a Science Victory (Spaceship) given our massive technological lead. To achieve this safely, we must maintain maximum defense, mobilization, and air capabilities to repel the aggressive Danish empire, while keeping Science, Production, and Spaceship flavors at maximum.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Flight
        - Rationale: Flight is a critical milestone on the path to Rocketry (essential for Science Victory) and unlocks Triplanes and Bombers, which will provide vital air superiority and defense against Denmark's massive land forces.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Free Thought from the Rationalism branch will significantly increase our Great Scientist spawn rates and the instant science yields when expending them, accelerating our progress towards the Spaceship victory.
        - Policy: Free Thought
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 20
        - TargetID: 1
        - Rationale: The Ottomans are currently at war with Denmark. We must improve our diplomatic relationship with them to foster a joint coalition and mutual defense against the dominant Danish threat.
        - Public: 20
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 10
        - Private: 10
        - TargetID: 4
        - Rationale: Carthage is also at war with Denmark. Minimizing diplomatic friction and aligning our stances more positively will help secure our borders and ensure Carthage remains focused on fighting Denmark rather than us.
    - #5:
      - toolName: set-persona
      - args:
        - MinorCivCompetitiveness: 10
        - Loyalty: 10
        - WorkWithWillingness: 8
        - Forgiveness: 7
        - AfraidBias: 2
        - Neediness: 3
        - WorkAgainstWillingness: 5
        - WarmongerHate: 9
        - VictoryCompetitiveness: 10
        - Boldness: 5
        - NeutralBias: 6
        - GuardedBias: 7
        - DeceptiveBias: 3
        - FriendlyBias: 8
        - WonderCompetitiveness: 7
        - DenounceWillingness: 5
        - Meanness: 2
        - Friendliness: 8
        - Rationale: Adjusting our diplomatic persona to highly prioritize victory competitiveness, defense, and loyalty, while expressing maximum hatred for warmongering, will guide our staff to coordinate effectively with other nations against the Danish hegemon.
        - HostileBias: 3
        - WarBias: 5
        - DiplomaticBalance: 9
  - tokens:
    - inputTokens: 49202
    - reasoningTokens: 3215
    - outputTokens: 517
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Standing**
            
            My focus is on assessing our current standing. Denmark is leading with a score of 3248, boasting 49 technologies and 25 cities. They currently hold five capitals: Copenhagen, Paris, and Palenque are among them.
            
            **Evaluating Domination Threat**
            
            I'm currently weighing the immediate threat posed by Denmark's aggressive expansion towards a Domination Victory. Their capture of multiple capitals, including Paris and Kyoto, places them in a precarious position. I'm also evaluating our current standing in terms of science and culture to ensure our own strategic objectives remain on track.
            
            **Assessing Diplomatic Plays**
            
            I'm prioritizing the upcoming World Congress. Denmark's "Decolonization" proposal is a serious concern, potentially jeopardizing our city-state alliances. However, their "Babylonian Sphere of Influence" proposal on Ouagadougou is an opportunity to secure a key city. Denmark's capture of Bratislava is also noted.
            
            **Researching Flight Technology**
            
            I am prioritizing research into Flight, recognizing its crucial role in unlocking Rocketry for a Science Victory and bolstering our defenses with advanced aircraft. My immediate focus is on countering Denmark's expansion and leveraging our military strength defensively. I also see an opportunity to mend ties with the Ottomans and Carthage, both sharing our common enemy in Denmark, to forge a stronger coalition.
            
            **Forming Alliances**
            
            I am actively seeking alliances to counter Denmark's dominance. Their conquest of Bratislava, a former ally, is unacceptable. I'm adjusting our persona to reflect this, aiming for high competitiveness and a strong diplomatic balance to foster an anti-Denmark coalition.
            
            **Adjusting Strategic Flavors**
            
            I'm updating our strategic priorities based on Denmark's aggression. My focus is now on high defense, mobilization, and city defense, alongside science, production, and spaceship victory components. I'm re-asserting strong flavors across these areas, particularly prioritizing Science, Production, Defense, and Spaceship at 100, and ensuring Air power is also maximized.
            
            **Strengthening Coalitions**
            
            I'm now focusing on solidifying alliances against Denmark, adjusting diplomatic stances with the Ottomans and Carthage to foster shared defense. My aim is to increase their public and private relations with us to present a united front. I am also reviewing our internal persona to reflect increased hostility towards warmongers, particularly Denmark, while maintaining a high diplomatic focus to achieve our goals.
            
            **Prioritizing Key Technologies**
            
            I'm now focusing on the research path, prioritizing Flight. This unlocks crucial air power for defense and is a stepping stone towards Rocketry, essential for a Science Victory. I'm also considering the 'Free Thought' policy to further bolster our scientific endeavors and counter Denmark's dominance.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: rIojHVujaduI4y5y
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Defense: 100
              - CityDefense: 100
              - Espionage: 100
              - Air: 100
              - Diplomacy: 95
              - Mobilization: 95
              - Production: 100
              - Spaceship: 100
              - Science: 100
            - Rationale: We must prioritize a Science Victory (Spaceship) given our massive technological lead. To achieve this safely, we must maintain maximum defense, mobilization, and air capabilities to repel the aggressive Danish empire, while keeping Science, Production, and Spaceship flavors at maximum.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 0pGhuzKXgw23Gp4Y
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: Flight is a critical milestone on the path to Rocketry (essential for Science Victory) and unlocks Triplanes and Bombers, which will provide vital air superiority and defense against Denmark's massive land forces.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: faTMo2aeKx0nZbvt
          - toolName: set-policy
          - input:
            - Rationale: Adopting Free Thought from the Rationalism branch will significantly increase our Great Scientist spawn rates and the instant science yields when expending them, accelerating our progress towards the Spaceship victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 96wBcS7u1iMwKKvj
          - toolName: set-relationship
          - input:
            - Private: 20
            - TargetID: 1
            - Rationale: The Ottomans are currently at war with Denmark. We must improve our diplomatic relationship with them to foster a joint coalition and mutual defense against the dominant Danish threat.
            - Public: 20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: d5hjIrnFHyTKQWrZ
          - toolName: set-relationship
          - input:
            - Public: 10
            - Private: 10
            - TargetID: 4
            - Rationale: Carthage is also at war with Denmark. Minimizing diplomatic friction and aligning our stances more positively will help secure our borders and ensure Carthage remains focused on fighting Denmark rather than us.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: itQwoxEXCrHakamt
          - toolName: set-persona
          - input:
            - MinorCivCompetitiveness: 10
            - Loyalty: 10
            - WorkWithWillingness: 8
            - Forgiveness: 7
            - AfraidBias: 2
            - Neediness: 3
            - WorkAgainstWillingness: 5
            - WarmongerHate: 9
            - VictoryCompetitiveness: 10
            - Boldness: 5
            - NeutralBias: 6
            - GuardedBias: 7
            - DeceptiveBias: 3
            - FriendlyBias: 8
            - WonderCompetitiveness: 7
            - DenounceWillingness: 5
            - Meanness: 2
            - Friendliness: 8
            - Rationale: Adjusting our diplomatic persona to highly prioritize victory competitiveness, defense, and loyalty, while expressing maximum hatred for warmongering, will guide our staff to coordinate effectively with other nations against the Danish hegemon.
            - HostileBias: 3
            - WarBias: 5
            - DiplomaticBalance: 9
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: rIojHVujaduI4y5y
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: 0pGhuzKXgw23Gp4Y
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: faTMo2aeKx0nZbvt
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 96wBcS7u1iMwKKvj
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: d5hjIrnFHyTKQWrZ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: itQwoxEXCrHakamt
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.