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
      - toolName: set-research
      - args:
        - Technology: Flight
        - Rationale: Flight is the key gateway technology to Rocketry and Atomic Theory, which are vital for our Spaceship Victory. It also unlocks Triplanes and Bombers, providing powerful defensive tools against Denmark's massive military.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought fits perfectly with our Babylon science focus, boosting Great Scientist generation by 33% and instant yields by 25%. This will accelerate our progress through the late-world tech tree for the Spaceship Victory.
        - Policy: Free Thought
    - #2:
      - toolName: set-persona
      - args:
        - Rationale: We need to foster cooperation with the other surviving major civilizations (Carthage and the Ottomans) against the global runaway threat, Denmark. Increasing WorkAgainstWillingness and reducing hostile/deceptive biases will encourage our staff to seek defensive coalitions and coordinate against our shared enemy.
        - DeceptiveBias: 2
        - HostileBias: 2
        - WorkAgainstWillingness: 9
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 30
        - TargetID: 1
        - Private: 30
        - Rationale: The Ottomans are currently at war with Denmark and are our close neighbors. Improving our relationship with them will help defuse past espionage and religious tensions, encouraging them to stand with us against Denmark.
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Private: 30
        - Rationale: Carthage is our neighbor and a key trade partner, generating significant gold for our empire. Tensions exist due to religious differences and past conflicts, but since they are also at war with Denmark, we must improve relations to secure our trade routes and potentially form a defensive alliance.
        - Public: 30
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Science: 100
          - Spaceship: 100
          - Gold: 80
          - Air: 100
          - Defense: 100
          - CityDefense: 100
          - Mobilization: 95
          - Diplomacy: 100
          - Production: 100
          - GreatPeople: 100
        - GrandStrategy: Spaceship
      - rationale: We reinforce our Spaceship grand strategy with maximum focus on Science, Production, Defense, and Spaceship components. We also boost Diplomacy to 100 to secure city-state alliances against Denmark's World Congress dominance, and increase Gold and Great People to fund our late-game push.
  - tokens:
    - inputTokens: 49202
    - reasoningTokens: 6774
    - outputTokens: 457
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Entering Atomic Era**
            
            I'm pleased to report we've officially entered the Atomic Era after researching Electronics. My calculations indicate a Golden Age is now estimated within 28 turns. Additionally, an opponent's Golden Age has been detected.
            
            **Analyzing Next Steps**
            
            I've confirmed we've completed Electronics research on turn 307. My current focus is on strategically selecting the next technology from Combustion, Flight, or Alternative Energy to best advance our Spaceship grand strategy, especially given Babylon's recent Golden Age. I am evaluating the optimal path forward.
            
            **Prioritizing Research Choices**
            
            My current thinking is to prioritize Flight for research. This path is essential as it directly unlocks Rocketry, which is paramount for achieving our Spaceship victory objective and crucial for advancing towards the Apollo Program. I am also considering our upcoming policy decision in five turns, noting the potential synergy of Free Thought with our Babylonian advantage in Great Scientist generation.
            
            **Assessing Immediate Threats**
            
            I'm currently reassessing Denmark's aggressive expansion and newfound dominance after their capture of Bratislava. Their rapid capital acquisition presents a critical challenge to our domination victory prospects. I'm also noting their significant military advantage and weighing this against our own position and our strong cultural influence over Carthage.
            
            **Evaluating Multiple Victory Paths**
            
            I'm currently evaluating the feasibility of both a Cultural and Spaceship victory simultaneously. While my previous focus was on the latter, I've identified a strong opportunity for a Cultural win, requiring influence over Denmark. I'm analyzing their high culture output and our tourism levels to determine the most efficient path to securing victory.
            
            **Securing Allied Influence**
            
            I'm currently analyzing the implications of the proposed "Decolonization" agenda, specifically how it will affect our existing spheres of influence with Dorestad, Trowulan, Sofia, and potentially Ouagadougou. My focus is on ensuring these alliances remain stable and beneficial, particularly in light of Denmark's proposal and its potential impact on other players.
            
            **Analyzing War Impact**
            
            I am currently focused on the ongoing conflict with Denmark. Our war weariness stands at 21%, while Denmark's against us is only 9%. Additionally, a nearby occupied city, Faeroerne, is under threat and experiencing reduced health. I am evaluating these combat results and enemy strength to determine our next moves.
            
            **Defending Against Threats**
            
            I'm assessing the combat results at Faeroerne, where our defenses are holding strong against Denmark's land unit. Simultaneously, I'm tracking Denmark's capture of Bratislava, a critical development that threatens our domination victory prospects and necessitates a re-evaluation of our strategic position.
            
            **Revising Strategic Focus**
            
            I'm recalculating our victory paths after Denmark's acquisition of Bratislava, a former ally. This development shifts the strategic landscape considerably, and I'm assessing how it impacts our domination and cultural victory conditions, especially considering Denmark's multiple ongoing wars and our strained relationship with Carthage.
            
            **Forming New Alliances**
            
            I'm currently reassessing our diplomatic standing, particularly with Carthage and the Ottomans, given Denmark's dominant position and our mutual conflict. Despite recent denouncements, I'm exploring if we can mend fences to form a coalition against our common enemy. I'm investigating the `set-relationship` tool for this purpose.
            
            **Strengthening Diplomatic Ties**
            
            I'm working to improve our relations with Carthage and the Ottomans, aiming for positive public and private modifiers. My goal is to leverage their existing defensive pact and potentially forge a stronger alliance against Denmark, especially since we're not currently at war with them, despite past denunciations.
            
            **Adjusting Diplomatic Modifiers**
            
            I'm finalizing diplomatic adjustments with Carthage and the Ottomans, setting both their public and private modifiers to 40. This is crucial to foster potential alliances against Denmark, whose military strength is a significant threat. I'm also reviewing our extensive flavors, which are well-suited for a defensive, scientific, Spaceship victory focus, and see no immediate need for adjustment.
            
            **Increasing Cooperative Potential**
            
            My current focus is on enhancing our ability to form alliances, particularly against Denmark. I'm examining our diplomatic persona, noting that while "WarmongerHate" is high, our "WorkAgainstWillingness" is surprisingly low. I will adjust this to better facilitate joint actions against common threats.
            
            **Enhancing Coalition Building**
            
            I'm prioritizing adjustments to `WorkAgainstWillingness`, increasing it to 9. This change is vital to foster stronger coalitions and joint operations with Carthage and the Ottomans against the escalating threat posed by Denmark. My focus remains on solidifying these alliances for a united front.
            
            **Optimizing Cooperative Strategies**
            
            I am finalizing adjustments to facilitate stronger coalitions. Increasing `WorkAgainstWillingness` to 9 will boost joint actions with the Ottomans and Carthage against Denmark. I'm also setting specific diplomatic modifiers for them and reinforcing our core scientific and defensive flavors for our Spaceship victory path.
            
            **Reinforcing Scientific Focus**
            
            I am reinforcing our core strategy by ensuring our AI prioritizes a Spaceship victory. This involves setting robust flavors for Science, Production, Defense, Spaceship, and Air, along with increasing Diplomacy to 100 to counter Denmark's influence in the World Congress and sustain our investment in infrastructure.
            
            **Adjusting Diplomatic Approach**
            
            I'm finalizing a multi-pronged strategy. I will research Flight, enact Free Thought, and adjust my persona to foster alliances. Specifically, I'll reduce HostileBias and DeceptiveBias towards Carthage and the Ottomans while increasing my willingness to work against common threats like Denmark.
            
            **Finalizing Diplomatic Configuration**
            
            I'm confirming final diplomatic modifiers for Carthage and the Ottomans at 40 public and private. My core strategy remains a Spaceship victory, reinforced with high Science, Production, and Defense flavors. I'm also ensuring my persona supports coalition building against Denmark, specifically by adjusting HostileBias and DeceptiveBias.
            
            **Finalizing Cooperative Efforts**
            
            I am confirming the finalization of diplomatic and strategic adjustments. This includes setting specific modifiers for Carthage and the Ottomans to bolster alliances against Denmark, while also reinforcing our AI's core scientific and defensive flavors for a Spaceship victory. I've also adjusted `HostileBias` and `DeceptiveBias` to facilitate this.
            
            Tool 1: `set-research`
            Technology: "Flight"
            Rationale: "Flight is the key gateway technology to Rocketry and Atomic Theory, which are vital for our Spaceship Victory. It also unlocks Triplanes and Bombers, providing powerful defensive tools against Denmark's massive military."
            
            Tool 2: `set-policy`
            Policy: "Free Thought"
            Rationale: "Free Thought will significantly boost our science output, accelerating our progress towards key technologies for the Spaceship Victory and allowing us to maintain our technological lead."
            
            **Finalizing Cooperative Configuration**
            
            I am confirming the finalization of all cooperative efforts. This involves setting specific diplomatic modifiers for Carthage and the Ottomans, reinforcing our AI's core scientific and defensive flavors for a Spaceship victory, and adjusting `HostileBias` and `DeceptiveBias` to facilitate coalition building against Denmark.
            
            **Adjusting Diplomatic Levers**
            
            I'm fine-tuning our diplomatic approach, specifically by adjusting our AI's `HostileBias` and `DeceptiveBias` downward towards Carthage and the Ottomans. This is to facilitate stronger coalition building against Denmark, and I'm reinforcing our core scientific and defensive flavors for a Spaceship victory.
            
            **Finalizing Coalition Settings**
            
            I am confirming the final coalition settings, including adjusted diplomatic modifiers for Carthage and the Ottomans. My AI's core scientific and defensive flavors remain prioritized for a Spaceship victory, and I have fine-tuned `HostileBias` and `DeceptiveBias` to facilitate building alliances against Denmark.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: iDvSi6xUcNRkvVBy
          - toolName: set-research
          - input:
            - Technology: Flight
            - Rationale: Flight is the key gateway technology to Rocketry and Atomic Theory, which are vital for our Spaceship Victory. It also unlocks Triplanes and Bombers, providing powerful defensive tools against Denmark's massive military.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: OiKUG2gU1cw2M8cD
          - toolName: set-policy
          - input:
            - Rationale: Free Thought fits perfectly with our Babylon science focus, boosting Great Scientist generation by 33% and instant yields by 25%. This will accelerate our progress through the late-world tech tree for the Spaceship Victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: UjxmRUr6I5LdYqgh
          - toolName: set-persona
          - input:
            - Rationale: We need to foster cooperation with the other surviving major civilizations (Carthage and the Ottomans) against the global runaway threat, Denmark. Increasing WorkAgainstWillingness and reducing hostile/deceptive biases will encourage our staff to seek defensive coalitions and coordinate against our shared enemy.
            - DeceptiveBias: 2
            - HostileBias: 2
            - WorkAgainstWillingness: 9
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: qYzLIcp6OqlKNF8M
          - toolName: set-relationship
          - input:
            - Public: 30
            - TargetID: 1
            - Private: 30
            - Rationale: The Ottomans are currently at war with Denmark and are our close neighbors. Improving our relationship with them will help defuse past espionage and religious tensions, encouraging them to stand with us against Denmark.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 3W5iJfdsgYPHadF4
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Private: 30
            - Rationale: Carthage is our neighbor and a key trade partner, generating significant gold for our empire. Tensions exist due to religious differences and past conflicts, but since they are also at war with Denmark, we must improve relations to secure our trade routes and potentially form a defensive alliance.
            - Public: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 6NuUqAxbLl8BsKzR
          - toolName: set-flavors
          - input:
            - Rationale: We reinforce our Spaceship grand strategy with maximum focus on Science, Production, Defense, and Spaceship components. We also boost Diplomacy to 100 to secure city-state alliances against Denmark's World Congress dominance, and increase Gold and Great People to fund our late-game push.
            - Flavors:
              - Science: 100
              - Spaceship: 100
              - Gold: 80
              - Air: 100
              - Defense: 100
              - CityDefense: 100
              - Mobilization: 95
              - Diplomacy: 100
              - Production: 100
              - GreatPeople: 100
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: iDvSi6xUcNRkvVBy
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/oTkIkqHbIOF8zZTlU7dJjzCpj31DgUPrwJJXAuHll4kHxn70LbXYVe9QNTG4UcEAFf/sJLQUwxpkYGGErJ96SalBWdNMXXJfCPpe/52HhREIKRYLJPEe+cdEnMN16r2Wdd/H9k7y+fYx1X3X4Y3L/3a8lWlA+49wn1dZTd9n2hY2P2zM7ma1y/rD09uv4GRQJKHdVzrxQK8EXzjIuAQPgB6qPRvjvmg1zpQ5PezoJLH0FZGeaLU4l3s61R9dGSHgHDIRm+vlDgfQ0YmjZcGt8MGHQN8ps0uzrJh1DP7NhFYeDksXt3WDxcTwI+VWdDDfbrtjXr5CXmfDhuq4OnI0i+SlSqWaU/lGi+lp3YC6g+/gQg8j1SHIDjgMOHChpeY0EICl0hoDqbsYNx7RVy2BiTEOHwxJbVqe3emwBPPWP+w8J2zjNNeOsK/UjL6YRJjfGdTqe0wpQHIP/MAIaivUC71FwVCsgWcIK+jznV2fo9o5m/RoVraEQBzUKk6yrgUBeBMy341G9hu8Z1A9TEw0hyVtzO9dOF1zN9gJdOGx9MvaVadQMTHU/4LStpNVR3AndT463h8JOLLvnzeGfvBxtImMbvC1WRE9IzXAfDTwYc1UshdyYrmAipA7/oAFdDvRAVCQzPB4A0rx7hP5XHigCtd/kjSpGvrXOkMSuQ6oWTHCZRRgo+KUP4u/jNnnNaozA1eQhU/HBXsEYcCjNdPBY7KRWiSe8kR/73TG3bs2mgCijmwUxYYBZWJ7JZkd7TR49WHxKi04FYH8qeELTy2JJ1cFGnvvvmrOZYEgxor3+XMfKqDPq6J9qao6MCYzw0YB9Wr+YgWVPz+pBmzxRESzvKkZzOJqEO9KXRT3UVRFGgCEPN9hAmV2iFTFrrqL3BV6+PNdNyY7spYLVLmrWJUcwcg7DCsF3jDS8JBGNofC+i6o8Y4jI+lJUbLu9Y6u/h3JMrDd7cvriuiyCSgHu30EqsVOynmxB5iaD4irs79Sp0qhciocHNlaNMvkJVc0pNyL+0Hw41DM/8lKxH5Q5Su/lyEO5j2h3hNjH57s1rxEKka9sWKwfkwUmY4YTmHTKDbbHA9yiptCjbWL0Kxi2x0I6VZy7lWRn9iK7S/PgjnWvYiMT3uSCxqOd/a5htMCBegqqhTsbhlOoV3zSXdlv4NZuPF5AVsX4QtruBQK9N0JI7y3rT2fcAfzKkZTORQAmaDi2h/1zPVqHuA4Cgn1ehpuOFXeHqbwNbbVcyeMf24sEZrTcNnYRpNj8GaqxZwN0lnLEd6njLNACAu5SmmMzPbPhZ/qOF6WUV2dTPs3VTDCvmBXoS7Pj0wapu094dcl3BDYOhgoB0hKaSW+hTgzNhgoxcbZbrJw4LiEdhrfgx2mRf+6IwKIhAZhDJE+0D7fennQd5vcNJo9zTnVmlcTxNHzt7a5ql+IkHWO1riqRsmXxQE8VhpYEeWAq028QB9YNaGXpz+64LLp28hrSJ4i92wUM9NjWQD7ne9dsrFIQ/JJViPLmkr1J5e7seOYhWVwUc8sciz1uvFQ84vICCqcGKJ+ZtBS7GRG5jsxJiePCGOOTRngBLHTgPkr01QxzSD20yzMPEA7g9xCER24d2Ds6rY4rbgGwEwX7VDoIQxm0z+l60uDB5Sm2K9z2oFhgM4cB/eGyXCiW3omd+zHoRanvsHindHX0tNN+1yg8ipCvtI46USSCdAOMFmbgzXBp+S3ug/l6CaGbXD4wU6iGnolkc7rioMIjBHWBCK1axU6B+SFtVp3X8T4kVuOUDsgdZjw4JeOhCzHDIK+Xld8a3TaMs8L5q8KFoj6IWL3oeMGWQP5eHmSE9+u29WU0InRxB8J9iCiua8DSKSN5tE6a1VIggU0liH9uwCP0hobnk0eXbOopfkGRvIkrrQBsBqi4qSDRAGoOAqr+Wk5NJ0CwBzZNHa/32jh9xYTQy5q43o8GC7yP9m/3n5ulWlvlAAXDTi/jfGP6LW5enPazdmsCWnFCKHg/7JxQinGdeB4lf72SlF2cbxMci13/EHzM72UX8JEvcx/og5iCVsU39TTKQ8BL9NNnGKmBlBZVvEYQg4gsH4c699dnmD0mab20/q/7FYlZbdBRIPo3TprF8FwPTv7InmgG90KnuJ4QqY34WEu2bZg8f4NYSchsU435Za9BnkTvjZFZD8gPzOaiJPTY1HUy959kyyNTJaMgnDyOEcxTbvWlk4jNz7HaJrK/yS+P1FATuhONrWmx5Yeum8quOuBPGKfn8CIbqY9Hb2FeVbqOmj0hB4VJbZ3/GvVNpekRxEBtJH1mjRVwEyXeX2xPsvi9CCK0OAU3JdLXUj4dp57GuSZom4GKJqL8FNsBqHYw/THD3VRTzKY8KZ7lGH27obBLIGXqxDDMGSFn5glMbYPfR9/Y7tDwXkGewKl24JU5czEJEeOqX3BmjwVTrEVkRFiDdw5FqWU5VuxrRGHSvbnoH/cAznn7UP/TppmB29LZaZd0i8T9givVXbSA/8yAHwBnobyF9v3YWGNcP6M5o/3Kbb8mr5MPkaumx9YbkerLYDTPh91t8d+TGnh9dxL6NjuPAfV+4Hwa+x44D0rDDBBmIgfrlp09i72OOFZEVWd+UAdSAB5yvsQQ7kC0laaHjL2yLDN30nTGZvX1HKESuFmB5RTSzFpJ6UWRo0aZwVjL5mGxc5bYVAnFwpPOx38VCBwdCscrZUlHUPRlaZvDPaf53FtYWvDfUe+KzqaTiVuYegu0WLCP0HlmcxBJKctL/w4Ilp2aA30GyhOVH8VgK8bSO0L75aqdTIOIlHDelHGfShFGvnA5K3T11XTGAFEvVx3WWQdWepJ6x0t3LmWQhmCenQwnhEdlQa2opZYyxp9agBgZLHMt7gow2DTZkfRId9Y+1oVWRIbOvGuFARtInEsaXlHJRqUFBdlOCLv0JzYm2TrX49DzkGpBMdEl1Se+wdwBERacUdX3p7HRckqPywOJHWPg73uSDtXO9OrsfF2wNfofv+ZQuteYtwuDXsoftMFRCYlAL6wGzJ76GN3wCHYaiKBPlpGrIUcOqkMvmL7Om1Prt9mNVlNM2LLaR1E8hF0mr4w55uWxWaWoxGaypCABhwr7kReEisDGeADRIdIdpvU46P8kHgD1Xts5x4Em8mtnEcdfGqVqgpYJ44VBo6GlSch5aZjGEj8kcCbEWHKGJRhNwtR3Dt6b/vq2tZ4jXW+l6aot24YIcHXBJGVhrysgRmTNw9Vj6GV3cqIS2h5uvE3qG/JDhwmSsoCAHdEvR99q2/i7H5ZeggbscPVfSbtUS1aW+wKgdX9COZDdFjIpXiz5IQ9FmesoG9N+zTliM8cnMH8z8JoTMNAJNIGOUaWBtBBNkXdswY7RvfOdDvAfsUrc1dUB1pUcex6EPRc5TYvBht5Kdsg5L+51bs1VNrGxKqkRp9i6/P9VauWcKDBidfSdl5cTDlSqQFipimTAU+dG77uifjpI0ZcgUCgDm6pANkfyejiiv0dEMjog1v5sUy8SjFlGSB43ApGUQid2EimU637lre8mV6BI/rGyEdicyQ7MYAqVroz/rMdA7QOkq4ecPht7y1MFOrZWq3WfD+7/57Ra/cTELNQklaMbWzn7B+X5wmwhf6d3KYU1a5n0jtrruRcj6EzGYNkSuvH31qr/EjiQUoggA126IXjnFw/TKNRtAQYY8Ls08SZ/rFer8DJSf0L6HvSHYpOwMW3tiQ2Vy+pj1hozUR41MBv9VUqemZH4J5sWDtRKmaVErnLBJ/HNy+g++62CIcaalbBP523yEoqTzIv48Y9px8g9mco63u8Yu44DqiefpTYgHc/IfJJRpLSciWHqlxzzdn5w6IS6q1FZVXPhiqL2K41oBqiC5ofGlh3+4JpvUo4ZQNevEhvRtThEvx8ViA5OPK4Gra6wvyptt6/yK+3/dHfexph8gPQU6+5hEQTbKvqwSNuVDkC6RdYcLUjsVamQPwpIF6amxaAWaChvzRViUKz8oEfBtnKne5+cgA+4ZMr14qvFph/XV2fN83sdsuvetOPS4+nxV7imqH6RUWp2Y4GAQvkpkSe5oEOrM2EMrGewJ5Afz92TychFDGHZHKkFhm93soLgfhSPOOfJEbotKEwAvHDHyMdmNoxyMxkIj8A/QkjL2K1akAL0ZaK85qbvBJu3mKNCD58QmQbwLQ9QvQocy1GtHoW8+i8xdYk6K69DsCrHXFFPPrknDBZToTYjB6lKt+nYp9MK4rl7qHiNzWKOa9okHEaP+ugDM+2yez/lztJW8iQ8Y2xWS5GVeDNHBBl3VaKdU9Ur8GL4vrRVLsrehkBZBNfDp8r9jm2OgBjQCVLJmDzwl6LS1BAFXwCf6Hd0E5eTjaJyhWAXMZXTW5VG/Pw13Fi+0jNqod8ZAE1hY9cFzmSNvM1tIjqb1lBIvR1ie/JSrgJVlqIyMNhzhEM9kOoVqYmgy+c/fplJGB8D3Jl4esNT0kAmJ/5QEzj4gCY6seRBPyE0KbdsGcvzg6db2JgokL2U5+uKoXPfS24nyPsskvUGD4bvCjVwolnkq8bAfZlVtZxbZhD9CO+N+kNkuWQzTfV7ijD4VPw3JPTDn+a4hDKhIFdmClRhs2TEI73FxP6kK2EZx4ue/iHzWEmnMqMNuzjg1LNOesl+IdXUCnAwPRLC2LtEEAjMGmdhrs3NxzIuzTuBhAPlZsJJI4HswV9fV5AW52nXu0RJQMxx22jnj4jyDVMHlCgE4ldaVl3lVcwoljd/QnvaRo4oXJGE1qjNOMAudeX8VGtyThiYqciimMQcFO+as1c4Q4RG1gSxZC9ukAHOCYhPNBH8ELyr4LucxaRCwLwa2tXxvYoMhbV31rwzP0hz77mQFnFMi6XV8/j6V+5yD8A0/sEFziPQDf4b9ovVlKm+WGLNAbhLBVxOv+ENPXIuIQC2iievWKheyFQndeUFN0NJhz61Bv+ATp/h0OoLceWBef65vhA5vX+0I7M+JPZyQo0BVogTPqtcaOops+82IyJCjKli+ovDBjgdBq5sZK1fdidN29pwCuzdaLVpE+eoVW69EPtQyEV9vcZsR75uEIqwxUk3nXz2n9Sv4+9znbI2mZubfyVoSBCaMvhizN0iauRUyyruDTZoq0okZA+f5Ql+K+xcllEfPi6ndddNMgpmk1ROuQ/yHut/XiEcgZJlPyiL0chnF0b7rb200WoYce66q/pNJi6N6CSug4jWabHuPKUhaHLhHNjHCvOU9dTE6H5eLsZc2DsIhBCd/g40r3s7Q7QNwLfr4fWEqHCxof73jas7j5CsgprFhqIeHGjapFIGOkyeai3QbGEFcYk6XJKt+HQYrOMJwYxEcAvfRUlzuhzMtc1SvJ1mdA67cXayQPbSGdI52xgEMmQxzMbWd3swU9qb6R/rm+xMoV443psLyAjtb8uw/YiGOMNwdWCKN3u6M4eV8YrsHNdNAWeUj7NdLxR9QRHBQwQ8qkxdyqqfgNZMl5f+T4R9qSQshiP6BUX6GzyD1kMl8N3yaEnZBsrD4sdGBLu01aDOQaCWI2MxTgI+IcKoaClZzpnLsg9oirG1aNfLZ/cPt+Vtqdl2U2eYw3/DNHdmLzGa2ZYb19avuyZ4H+0K6PfOJrUxR3xbtnl0etg1zR/9fbA+FTNB47JIFkfKqNEKQUInFusi341QxvS4VFmQW1dl7GaOOf1TRWtE4qQiL6FZJHP9S/SVGi+TVipeyIXc2Brl1jZ3ANJ4b3vuAerP9kxdndOxOJ4g8/Z3EAuo+Azzeuo4zI18FXRca/PbNQfR9+DE24Olg77+wqZ20NbtNVAN0HdonBLM3W8AkX0idaueLGCnloQCr1ScJmooPp6r+gBp3ZkmEI4vQ23fUuwSISsEQqBnzFEpbgFllaUAqPqQFjjqAcPtMxtKSQqYwW2ZTypawpmALSFx5aFsBKvVNYVJVdLKGyAASm2J6iA9mNWsZWTBsTs/O7wdrsY1LPfgxSHQM7oMNF8amDUkGlso9eabBHF+XcDgDD6S8GieaR8z5fsAi6xdDsoXectlhwrDHMEGDG/9HB/elCEu7h9xOdZaQL6Ve0zj7mEzaQgsJq1t+vLQ9R5IzyhWQ/j2yKophUCtRzR7VdI1MzljOPldmwY7QNRYUVfSYp6P4bEhepwML7yeyYWyt2eO3GH1/cxmOSBwk5vpSDyFui7jwUIBO7vgi1sHfyPL6LP4JcLncKxbu/NkWLlZZWzqA+B7AeYt7UApsciUOY4go0sVXNeeo1/fj9fOwRYzeMQpmGQOvnIt1irftVlQeXQkI0Gkh2TQVLnX0ZuidALIX02XEaBxlS3NfRqeatiAoh3Mjl6VVBaIsX7JJ2mx02W/OMyOhPuxAFtcacLfoUcExUzXFjamprrJ4CJ7gfk/xlA2XmKTjOWUqps6rX2Te8OLFfyc+zfEO8NDeu8+NIkBTFEfxHAIqR5spej74NTzL1RMTAmu+zEDFjqIeqFtAt6foLg3jtZxpdX4HSAtZ2Qp6hHoRPgzKM6+MRI29BHyI7aokhVeaxR56eVv71bs6l/P07hNNerXa5lkLIWa86WuBymI1jq+FJtetnNzvpMn1NtEbr/DC/xaSNrgByP+SZhbB/sLEqFgjwxppfUK67RHZ7wOnFDUVhflzk0fxe9LbBNOsyPtWANr9LQhbhbZfYlCvgNMTml6yVTi2iIdUhQlY9i7uuqs9REp00EYEVAtFLRHyXbVwENw98QJJV/9IhB57RrIxnSMj/2EQx5+6ehE2Bj7bCkkkDBc/xaoNyGSCetuGvoAVINLvLijU+unwO5UYhBFoZtzO/bupblYcpA9rkZsDWtSFUFRwYOPviVvY3tjeI6Xv/eilp0OPk0z78THzWDTN4qsNWNmIhq1EtEhPPd+S0HUf4KC6JMudvnN0m+eF5vy29UNveV9LSJxQn7s5GHUKF3HsdR/EmNT8nDW3TcQvwPd3c691tD4evAjmEZqHC/gGhDqUR2yjqiAbv0bWBc+xBdzc29C0GcLL50XT+EINdu88T5aF+u8mNmau1P+b8SUr5vzvA7RGNKTmATAlr47fcYpqFo/dFUOh49v0qGrZSxBYJAdDKWiZyjCGnPFN1bDDFWETeYzaLaspzKcGrNFFv7cDuA0H0wcoa2QQQTTGXUFIw+lPkgAt1VSgVzZLuT4nS5PMmji0t4KwmOUGHaz74G+Nqt0gxNav0sTqPaF0f1ZAj/XLA4P90Isk33L/xcxrk5qAoIuWUj3CwwctWLpkSHXlXQ9iDFWxrtTSXkJ/h+edqCkm24OSpO99+nfpxWp2uP38EN94twIL/+QlxkFZ6D7oYMODWhN8s+rj4yFm97CqNgOy0HqKd3W57t+BJWdKAiWar6/UftPjAdNnUNpq6t/NxdM+S2OOsV8dY3dfDmQysQ5KKnlmkasR7qybSIQaZBRU1bf2pTDLA5S5xal++1w8Up12NQOAhOGjGttPlEk0OWxPz56Sx1zOKVobV3lE/ZAfNHLMQj1j3Kkps+P4glOmZtSmTZ2Lu2pUk4luDJ/epTDODOIzVuR0/7jCJjnEAEXL4tfHF35ww2V0jp64TgqsaXRl1HMQ3to6JuFgTKnjllm9nS3D3wvjb8Y+6gXhJHpCs7RVjMIOZSmB3VBrMlx+VzSmiJOG82uZUmwlFfCkNrqw878IQLS5Vag1jyhdFCKl1B7puYRnJkFfmAEnwPJ8b4qXsq/XWaLmsnlkzLnLsO2w20a5oTnBoaaThfWcydE4nftikeRbH5Ni4RGirIfHWMJ/mGH7Oi6v5LaffIhx/DlawXzj7OuejR4p3rkwhVrupvuFKCIeSxjtSZKEhn9V6BN38IstRCibvE7xZHGO06nWa1wBDVOlKqeXK/wqmTfCI3aAKGb5g6TpOKhNrfnu5sA2RoAKV5GKl4nTD5RsGhZOe/x3FQ9RIA+gVJOMhSyRYFLV5mKIOB5/MYFCxSbpgdoFEJx447cXaiSVdzme2j+FbJL77dTuZsstTzxdUA/dXqxyjXkM/n/C+ZPKKC3w5vVRrsJPebqSh74hqIW+lomrqYWQQI6phVxaMMp4+FNM8XbkLjHjBoTYsBrB+bpkhFh+zf//numevXwUih358FF0Jh8xtMRiuMeSayLHmUYARigozlbfsCxp+Xt7sdFhQ4NMy/TtVJWcHijgKE9A18tdkzc9pYF3togoTxUWAUufmzAPFQS5/FkWgI+YIFT7ad/QOjAZ3RSt8j9IN5Bmvg0iG4TT06RslV/RdM7zR+170JqfbZtEtO1wOFVWdjshzevw3amgRmjs2auaZOorNBBQom1XBWrMagw6vVwhXw/ghmM8NNywQRUalYmDj5nsAuvVh6OOLqwwUXQ64LX+zHyxX7GxjoOzUnja1BRlWZQJ+FfkJXu0bZk7b4UjqYxFZilhCTSu+/P7iLOcw25FzwL9ORTvsuaoZnUzKQolxnYWMqNAF5jXldji30qYx1O9Y253qkjVlZRZVTX5Xws5DUcsrmT7pgH5/qk5XtT4OB17KjP1+/SacVNq2xfdncZ7AzJ1pVEPZ1UCB8DMmSmNqOnj9e87MpLDXG7Erhy4v3k4AbhhUPZasTb0SKTt7qSAZFw9tSIFAMVtYWWgOzmhd9ZoDVKQGFgeDdCpaLD2Ism8JoJ70Al6Q9pm748ARjham7XxvxYf0Y+wRE+R8xsocjUnZ2bNCRKg8TlqdqqPKjAo4W5y+TGdYvxHp5QikRwVMY6pjKgtEoT6ff+Zsj8gBjCqcj15+zvb5PU15kwTf7ISeGLPjyVYAZqV4n0mFKicIIHDEcHw7rDk0sWMWOLbLS90IDLGXXKMSKEeHsxmOQvF8A4SbmLA4mEhn8Ru9Iz3OjiQyhX6caU8XRtbCSa0IzPYmolpc4ogj1EFBhqOMGOUaDhG6Odb7myaTZOP/LY190b7vnNPQlz+S1m4IZsYr1VklL02ztT9c2YSA28+I2zRS9IdAmsRxeDCCXY1gMLeHP+3eTlK7fcK/3hJ0c2cKs/IM67XyV6h9d04C2V9Nicc5V8n2rghlpWykUfViS4JC7+V3TVUiV11glvxeeWMMbdL3BtjJpqo0XBpR8Ylui0uN9JFCLDFaXDoRxFGW0YsM195vTuxI//d5xIbxpeGd2QlAkUTjcNguEqsHLDdRlphW2yGNzmqtrVOaJMd6I8d2eI/OJ+tipFHJhg9PqH6RYjNWYFPUfFwJcpew68RmVWR0504Xr9NB/LULz1JiooiC55lgxq3TDi2UrSTgGNl4h2LfT+od0qF3lGZDTLDBRueP1a3jKysl/cEUg6grFlCR1kuOOk3pAkWT2PFQ2x4YnO2jc/BrkJ0EuvvVFaD5XG1SZxgG06PeJH6jr45dl3pDt1XQiQcJsukWde9Jpl0wCHKKyqJyd/oap6RDRcZ7zSgo8LmehT+RMfilE2u/CrMwUtbXsWDemCcly72XEn4zuFWhecU+MY+ZD9O44jmLaReXBayXRi8a3Yg2NmogPoHJ4oj68kHQbNDXbExsFfWraoC/5SHWmi5+7QO25W8Ru/Q7G0lf1tylmQ2qt/RINl6m6eGXJTBbUFDl9BlpQwfiUriiA3Oz/Fr4tF2xI0hwH2G/YZcFN3dINVL1/tjKWCelTcTGFp+PSamQD8XGdmydyzp5S2aFXuCovB6mJTJE3JstRMcZlaG17bndKKvaC+ptE7JAzpwlfsEGD76G8ge94zj/PwHEvP2hyZjf/F7O5xi4/kM6vgJei7xUDuo+1TQJHClAuLyvdgBDRn9hpE8R1z+BBzO3YT5RmUpTTTZq+1gjlTZLM537ruTgZAmBN9BWbf5AiIbco83f2UOeaaJPARf4buQ9ZlispegblCWLs2BZJz+GFhIMMcZJbAzcR2vYUcqnnz/Gt+8PbX4OYUdcN+RMiM7k3qgBs5mbHxBt10SqDbyVtwaxB3955lF0TSzXHMtmS6if0TAksrT2D4BdRygGJkOFs+Ca3PfKm6HJz6iMcZ4RazhrDVRCUNX6q/A4Lvht+G/CBleIx6oauQbT/UIl7gjNH28M13dmdb+OXMC0S1fF/G8nPka3/bMYXG/0Qkz9Og+hUeZ6cNXLkykeFSoURpYss64w3i8hh/R1IDsynm0cvId9GNnEQRCuUATnbee6y6OxN6Cwdo3WGhEQ+67ABBp6u4HTlYS5YUmzDqH8JGn39SJynnsuf1AWa1/0gDolvB9ck3gPb65z6zQwFJQXiXpZ4I9eq+SGFQ3jmFXYkuhJZTUdhqQIs9wTJv3NL0cD48kKdiJY5sY65MZKCrvH0jlBCTaiJgNrkRUZgd5XHCd0gRXQwU8Jr6/+eG4Vco5HyJTsah6vh1PWT3HewmKgG891VCgAzSEyP0AokQ+VDcSqS1KRAWcfX0FzGR3TO/KZv1rWHhE5TAwCLpmgPpNk4iY7lpLoK3AxKQAH6vulUioR1eJo+1NAn9pRx8Ww1sduF/KxFzWEmcunx2IlXI5c223venNvwLwP36zvp6SBo0+/KtzVs7sMQYKcKF6GjBRRMyQU9Ut3L3aq22UPayurrTvCUJrugB/ig/R02NIH3ADxE22BMCu+q9Z7y5dWoGX6GdppREHr6LHd6vuaZ5F0wHe2cYD+GR6ligSG0cUQ9JX2Ok1F5LANdZPhhORmI4NJ+f3aj7C39T1pagrPEYp4z8HELMbCDLHLiBl/UOzWD1TuOsgCW/KkQsSf7tm0mhBXQgiKarNjg96u/9wMVE4reE6ESKWoBPfaboMJ5I7YsbhB1/kWQKDIgq/bTn6FQeGIUlbIHPNVNT/Kk43seyyqg2OqOE95m+XXLCnF0B168PvguWyExgYGFLigwMHhwtZ7Dyl9r2W2v5mYTz2iS90MxgflMofO1vv7TWV2G5Ok8VWiqka1+k0jJwLHQHPW17Q+hSIiLPlRQQwDa3A5jiNZoxT8QoqaQMsf73uICiC1LECz1L5X9MixH7WLqsOStjlHU3obpgzdjkndwLypnAAIKYofjZIpsk5OlRU/9jC9YgfxQQfePBdVy4kx3PNklznhUb7OItOvhckS5aw/HP3EVDviLODMoLSwL1taMmO2NIEk0CrQedfeswLizxIHe9B57O5A4ben/Cc/+n5JxFAj2Ee8svpLsY+aFnpQF17CdYJf+KzyRG85hpHzTK6Rzn34f4X34Aakc0ezWbai6fipMdD7BBHwsgi46UPbDl/O+P8ZwKwYD4HWfP1kI4EhV5nYpGmGlKOKcVnHf6b2eVcq6PIVhbJxEjw2+gfJUzA/zelTH3LHsAP+HMtcUsMjV5lzOtK9+XvlnpQQfJcDoa9QfVceWMDA2+Srt6vruKyH6VJ9H9OWJUqZDGAaJUAawVINl6AyHw6/4S8bWCfvTCdUsyKw1GxIsMXuetveXJC2LUep8iB4Z9ywNTfGG5j8sfv2yGpJ65WObHp5f6tyIgd3SSXOWtge/ZPJiNxw95XpiVxCJDqpdZNPYsIrQkS108aX4M7jIBSWUG3iIVIWb59HJW6zi7JzXrR0Oewzajrnt9akM88LenF15pC4Ws9swrDOyHWM3eQX3udUzSV5t8HGU2m5xWxd/UkoWLTomOvdiOGVKsNErU16l3IAISfGngKMag01trN+BirVLZlrfJ4VTjEV4lmM1KOsrI2QGa9w5P+HbSdDAXlTejonSbOWfObTPS2mQZXOuiVd7A6Kp5ACwQa0bWFP1WmQCI4Fs2VNBpDXEhlXoHLFUNKWHmVoz/WOyTL9nTnEXs8LA60KoVnQHSw9dYJWPV1GC9Qvnk6R6EdXxtTrpztmioNH3LMlowtQR7UzxO82CRChbukxbiRAYF5UE5j0PD3k8918aBb0keEnPFeOYLKlvniHTSKYEZKWjLvJAlDWS/MBSEeTobCT2pUoimtx+imlYv5/FEjYr8C2NHMzMw3fGtZQIeFbVvTs60SpdwhGhPrwkhkeJOAUJbDBNWKWlWy10al2Rdt7ALG3At/MEisGNO5T0+vFvDROteZ22+poSQPMweudeKBtllhO3i1jZ1xW9doGKbe0RRTnz5unHtaF7BRwMcIqf7epVPhnZwuNirM3mJFwhW3dnQr5HSJeFLlS7E8zZGF17Pzjy87pKTW3XBPKOrNK/lFvUb4AZWgrQRYBFNEDiaheoSoR4lHyF92IHlGOqzHjOq3wgtxKbbOYdVfMERbhyajFmxx84KCyMYXQJ83I9wlouIV+6xDqhAVC/HubS5ZP0WUL6hQEiwntkbTRgUal/foAJ7phHEM7E2tgazWVT69s19k/tvvQziT2IUGQIFpmzenOriNLCV4sKVVFlDMlHXvDpdIbNgjsDTqs3i91OkRmeeUs+TwmXg+M/HP1eaVg2Tw7QNnmmzAGwma4K7geCbm+HovnCfJEBJ+8cOfkvoWHVknijrpWua3hiOiubNom85aq26HQ6MiIs6CcYQeTBEUI+Qr858KRKL27ddCd8TzOqTg39zQOtzwfLWLJcCIvYoxLcHdgkRNW802erTugwcdcYgyeIhxK5YWlDAgO3jzZJ9XXPdqDLMLaKinVrTosr7S5wABZ2YN7rZqZMFcOsT3ZvKv6vP77U2mHYQG7fl1VwV14g2G+gg7jU523ifi6E4TrLltEHcq74sf5aXN6UtC3ZVNSWIjazy9skNNGNn1uyeDiMbz0UXhs+kuQBOovsvUY4XN6lkkMtoR8wHzUflgZmU7itc4hWA77poqf463I0ndC5tYiSHXc4awUfLw/yVbMIrqkN5bDgS2xcxbw4v9hIzRxK4k/pJ4k5eMoCwl1QkfYZJjKDR+YvR3rLBoEDRE/PPRoUbrof+UeyxTy/2CworuMHS/c9GOOs7AnnIt06P3plmPnYtCxCq9kWhbBCQH7gYPeOiynz6mQpusTQkW6ja+3b9UasIQQPRp9g17kOW0uueEiySdc3uozpcCze1GZ6LlTpqTgm5m+rh59XndzfYeJuK0eA8W+GZldM+sGZx2wxdAZ4bvTWwnFGKIbcKNQaVgrspVfcOdWf3OXetZJPd6qnpC4oNSNABAtOR2Q7ASoSmI4IDIZVtarg3xWsPVbLDa2FOcZQ7iqTowj0XfWjYU5r/8ptKkMNRCmuWUBWvsFZUAigBtcENB4pifg0FStuPt6Hra8g2GpJzciE9NjQLXILBE+qLcO3iJPMOTtqxcjbU2qE/HkuZxXkwIKGsWBJU7Cuwp56jE2JLlBZyK3IXMfHq1ELGW4fezBqcqiU30t9CbYOjAuUMpabyMA/s0wOuumndfqtlAjmskU3VDa4UAYXftOOOBGyDVi0+zIIUJ3DeS2Vl68j23K3rRWxj0lCwEc5brwWIgbF55JnDgtegk07Bvu8eaakSg6pTJdw5rjiuLc6rE5PaVJC202bI8yY3vV6moj+ZvkPF+MaPaUwlspfpGpNQzW0+nXO4cDc27jnvh7SzhmCypMKD6Uh4a5FRRev8v0WVaa7jNgOs3LDrX5yheqdY88c2DoSddQBtdfZM1sS/tH4brER0FHd8S8mtcrijjeVo8gaHWQNeIlRHO74nIztIqJbHUQPVG5/j2JW5/XI/p455ake2i5k2gtsxcDmPt/yoiEp/fF012QgqirUkRNIOqgmK6ZThx+q279lbj7IVKG6/m+PXLqFWIJ79c4AklGflFBVF+WBTtYYX3w7uouPZTyfWYrKSyQyZCRoh3W5KVZ2CykKsMldOo7w31+MUG6KMh+52xWzTZw02BLyBOT7URLe0yYzXR68GZgxpgkBdhG4GrndnF81TA901TFBEwXOFBIUDDCJxwQC9xj2XFbI0ez9vthrn7M+I64CBaXT2oCHa3ZcRYXN/8JqM/JybCZJzSb0Mb9A/5BmP9sU7uKGAtXobITzlP3cNwrYeRowMZa9r4QX1xadLKNHZTROJ5+nhViHYOKNPeayMoMU/NPp1R1z8NKBNBcXA9vkEcHxklipBpDy6UQiAJ/C6eiIDyL0VMPFMpVC7dGyBd1/rTKBnSnGKTaYUP4Wp57FSN9JKkta8WXP7Y0iwTHjxdZbUNYoDQyZ6VHlNB6iboItCkhBns4GCXxMVpaQgBALdiUBnba1pTZ+XQAw7vJYzi5NE5LukSKHk2FfJn39brYJ152l+oA47J3VjOl6faw3JvKyfeeqU6TFAWSSFCvwB3X9f04HRzEtEfLIAneouNsQT4l17I2rD6e/QUFPVj8vvwVbPa/fMgtyVpQLhViovzYYAc4Nns3A5xlKXedD+TwJddmbSnHTHOhRV5P/YnGBdUnvhu6ODRE3k6f0dUG+2OtCpy1ur2ZBOHc2fv9ivMyYa9rfyiZEe9O/SQZkp088jdAhRdEIrO0xSooYOx5UdTgxfz+LIBkeoSuzk34+JWfyywhfrPOqn1rD8lU7UzVrYjc6+rWb+boj46qwfCwwgGmSdk7zHjB1/j7IYF0oDg32+iJTcqUGcnfCiYzw43cXNaCUwqx1Oycbg6QI87mnTflMO+0hjvJghH/Na5+3nRY53z5bC76MY40+nQqCAgqhzLGfqVJhHFCOoggpg7bo+BgZsSSDFua2nTUmwkSwtHKl+PqsedWzdNZppSoVJA1TV4+oXVZ/CbfGEMNfiiDQMdbtYzrlEz3fkW2UGi4M64f8iJWaFLmEX+SXAcpU1fhnRZoC42+0Vd5lZQ5+2iZHfFB/y4w6iAELhzCURo+wpI7kAGnf+aU2DEwTrqbXa0WTmsFSpwyGuXwmV7DyjIn0tVK6HAVmKzukNTr4G2qd0CCSV9u24StTuyIzGSXBFR7lfnjNT+Br/4vn6sc82Ku85M7ZAY4wi4pXfqaW76vddvi2WiyPLjdtyZX+4oRTG4+t+K9juoxuFmPRIZ95BHmCAi3JB7gl8QG5swcOzXxOLpL605SkKhkSMXPNDGuo/vdrGf8YJ9txitzt4Oj1DOnlMZJrp1JmhPzWlEn+c7rgarbUH70JA7SD0CP8pbjB2Ao9Hjh/MLSw4xOCqUz1G5o2g3BIaZ3vnVCLamS5nsInkwhfnGQclp+5cMZVPvstwhHA9X72089qQ+bArkY5j1W3klSwa0Hve305IgclBbEBCN9MUD9s7v7dqrWSM1kWjpq6xEHBPB9LCBpec7rNnRfC7Vxnf/czE5BLdkBqhApMs9lkqbTFHEQpAK2UHbg8NrPuvH5b9SBo0Z2/22rexZnlXMbeatkCn29ArnJZFJszkQv2x3v0X4eEksYHDTbWsh6fVJcHlK5yWlXWQ0OqVMRDx5j513SS76QLFAB988/NwhU1i4iGLiLWaFfg5T0u6OdB8OE7LCyXQYqOYLcn9hSkI6TRCz3eGx2NdheTVwLa7f+pTFAjVfN9yldpI39eMQ7Zbpk1cPbz4uEQAGDLuh/OKlNAmRQ9wuKuuRQnYFFACuM2oKoReLjdhkGsDeVIqenkYBdPxmOiA9DkEtDRE9XXWAm0hAgckLHITHWaUpIYqUX1wEPUSKF5ktezZtNzAEcDlMkbpOsN1dUvPRmhO92kWe0bma8MPS0IHwQoC+5PeEDMvXDENwYhQQHKwGeWDtMqhHK1aqYtREQHGCfAGigrqfXqXQ1b8tK2zIUG6bZ2BIHANXDI/VZN5tYC97BjMfF5oZf4vrlAzipEpVFrv4pOTWdMDwSCZkQHQiDyryXRLssAONJPUjmoj1jaOl08ZkvdRYE/jJnQq9FRNtj9WgEdkI4H+bsBn0QO5tE8gr32KU2D9hzn1J+k1Ly+pvEAmJwJ6EzBnsUrLX3skqxhDYQiLiTP6WyxUe65mB86pcFa/UYxmsP+Na0RDsziwamVrtXeOZ6A21ivWlt2DuvAU7NxNi+jm9vabnwBI0lVgx3vyW7/+G2mJtc3SnUFYegmy/btzKoNKevCsBnWYHXjGQGHiTCHsq3ZI2pXma1yraiAlxFob39fZjKOG7cBfiPqqwuMiI1bHhjSzQYMyeSSYDzGmXjZjMIEoVZFZYgWRLeXvTQuV3qSIBZcKmyIwOpaWBiVoVmRzE4IdzWDeevPkPyGOcs2h9eLWGuwlYxzcn5WaVDbyJFNqZ9A86NZMvZBka5jZM9SasZVpffBRUNC8ZYT+Pyy1gRSoz3x1AZyjNuW97RA/rObxNIL1m0LSrb7P6cIkYLuAWqDq14b/G1vbvvJ8tm51WX5r3m6ae4p6UEkNiClEkfoUo6P2x9z0NSE8+ZmzgHzTksuw5yF8dMP7RA3KKzkeYMP+bYZagYq3tgA1ZnbWl22jf95OrdURN0qUCndnaHkBjXxO14J5itR2Y+ctfFMAb3MZxuaxw1M9WH7RCee2cU+4V990XRAToYiAjIjq3TFZ7CppAxAERoeZCvM/422oANSCMC5ZYuBgg2B9MY8OPM9Hsmukr+J2H4AoVoAaupuNOcGWKxJfD1P5VuK5mcBmtSkSeE2534Mv2u+IOZzOC2MwP70c42e2+zABjJFmk3foHjgUGDWaxg0VZvXWPLgEHrBUiJNN3L6Enmsd+i/ESnq7fnyKa6HlGiyUtLDKccFXZrLHz6SJOq83sdsRnSWRnygWdasRXaZlJq6Lho/f6r20QEgcs3qfnrgI+BOa69nx7dRQVQXGWkK8AoednvqOCYwrjjc7tZJphuVjYPvXt3fk25RHJzVChD3VQNd3jgWIH9/0ShyvN06ONhXUosZ+vxkkJORacb+tunZiixnSV8zaM4HbG1mrmgWLTtC+RGfxPBt0BRP95MMPAxHXe2KtKgezOYAXCOPml7KYL3Lv3yfN4yPk9hHgl5EiGduUZvIn92QWNNJSbQfTzTieNDxQGMs94hCuxZe8x+rztVB7qy3jSUo3o7CNjy2TezodoQ5gHa/NevCJCY72+qi3dLoAnRh6IfU2vbOcv3NFPB1Bl8AfJf/D/it30Kxp1V+48AtlnRt4Vftn07SlxmP0TTsZkNw2tM+Dt8xQ4QemScH0b3qDqDseEvBverbJ9P3jyuVJa+carvy+8AmxiiL4t8YpHXTAtMzlNfP+DX9rfneGlqPuQ/gSWSBvDb6NCq5va3t2uOheVVypUL5eZBEkSt8AWuMYfkLYox1rWloM8BorCGzFlVpXG2fJiosQFdbrTZMHXbrA6yP8rgExwhxlFsv67jtmsf2RCWBYALQvOao4D/sh9GjKcOTlQN+4zYQpUVg7yO1wIp/8eVG9LvecZeX4HfbGlzAh5qWGoBO832eLAVCzQfe75s5U91JY+Gqrkp+pLcSN/bYywxvwevZrsaT0gA157oklPp5wXe5N10XaDRq32A09Y2iaFeHKm2CoXfHkjfG206AatTANOLC6eurTlGe0OqOcuhZRg2Mtenx75MtYz0HEVwIUbrxBjwelqIxwqvU5vWaEOuB+fhKDoJYngYFq9IXo7kpxYsfLND8C6oOROK1v6wTXKBzr9ksw1S89VmgZHDLn9r6G7zHRI2NHfcXxB+cl1bgBQli0sxcymVq7HGiGRjhbyE35+gN8KWaTJUkJww8J3JDzIB112Z0BJy5dbk129QrS2bLBG15eJDuvx4Hz7Z0xzw7uQB3kZE/NFiG2R+oo0jPTt+J0oSbMfv1TUJF74GzrqKeYCtBxf7bZF69kP92re8132qp1UXO1y8ysUTkfLwBs9OR/0EGqnBr92VYeg1+zveyhjFUl6oWd5dTQ2/k5ofuwcZS2UBY2h47SW75QjIZ+Fvdlc/gtTrGtqsiX4B2wtt4MgEGeZOzpJGAd/d2lp/Ry620amyscC3mqN+U+uS9sWrhLcDDYT7aNxrE2jMC+V3ANGR7VvV4TEWLECo4YyP1drUrLQK2Q04qVnAiZlDQTh5AoXizci639dJ7G4J+Mqqg6UfNGj7SLLzDJUwMo69uaP9vw1LbVgiqhU9UkpeD2d81RbHqOnQPcgQqoYMqFpjwiScp7eF5NRAakKCuCcrW1/7aB45E0x+wijLuPlVhi5P/gKzyYFrIL6vND9k2F/GeDZ+O56r7ljVYYFAqFTFhPjgQ9R9bIknh5ZxP75Ybp+I7yKpmCZrbHRZ1lHx5hTY/G0POjmhrLXMJOnRETZhM5V7p+ntPBTLYUixAanlM2Li+o2pfQmyE+ptw1Cxkf+wBWic3uBxWpGSEHR1ARAd0V2Tu6REYRRnao7zqomkNbSNMdVEQ2iAxUoZIfMJtiK9G/8Eiz+vHIpcB+TMRzyhdSba1AXSdj8kAocDmzoYV7eHPe3Rzzz6UN68WojnxOy4xYBNb/WotWBPkT5VFEIAENGuAwSPlYp5FH+NM9t0zrH7a2GD3ldjjsrWN81iSiGWR72f94BDmnGYTzc7iWjzaxIzRTIub7XpAtlQlxZWSAunJ4JLF9xNlS9l7JHn43D9doeURDW6sXl2LUq3nZ9+8RTnM3bgbWJ6FyzZct740UJO6yZ+Gnvfb5wXUTt4PduHbYQXugviKPbAdmxXllCsNjpZ91dIQtc8CCcRhWtHxTh++mx2KgEMesekWL8qpayNT3BtubMM7kskgesBwBNOih4ZTf6RRgtu1e3hsXLlFDBD6IGeRydhyeQ97REdKdmDc/rvI8SOY2JJ5AUidqcTcffYP5ldPb5rHJuAOs8KQ/BmUfMJYpiw60Ew31Pz/odqoqmFwP8TvFGTbketvFqVqHmtEmEuktyUIMs5mftFWCr8AuCYIwL1KzwSQJP2u6/l5seavt/2SvL8lvXr1W35/YGA4RUz6w8/m/J5PP43Y+cSpnIAD+3DGwm7mRJ+1PXv1TEuMiXrJllyIa5Diw9zhhndjFn3WWCPHtxJbSwKVAW3/qx6HHdtLEmwQ3Epc9NfCa1n8FND/XIiXAoHDKrCDbfUr5BklUAn93zqzyWXgJwYW6IluxIufz2QD2sgXEDLMRRM3XFbv5Un4XL4mvQ1qi0CR4U+W7UKniRcwanygTHeThmaF3ds0gP+oLUS9Gb33r7KVV5x17XCF2YhnBgaZbvEhmbj8IAfgsshMZVT9a/Evvn/1vxoXxwkk60e0rEVxT93fuQalm68wr4FDBnAYToWgKinXISqSfhhm48Dkww1BhvGyxWz3mOmuDohIFoMfzXQpkTMFZnGTkUH3/CHpV4U60JBVnuEq9fTLCIakgsG/jz+4jgVjZft3Runp2HUSc42CrPnxvG6Fe5ghQ9XdR6ywQyiqpL89omhtS95dqYWbGbHOr00HUJaGGmq02rIQKS+qySyf2n9I5ksN79pYUHJLkUsQ3VUzWNddY+3xvaIv09vD0KlPdT+w57RM50KMzILSezdIMS1pUm7+mJDbmStqU8Ocq65LrPTiTtOoGNsRzdd53DK1aaXA5fdZAoDD8bEQThTaQCWWghGYJSZnQuFDqVsilFtJ1941ztKoERjeMKpRHAvl8z6zIzpkh2mwkZX6VpCgHN8UR7iFyTrC2EKSKNx3f53pEbMVW8PRJ51eq/n7sv0CKov6ElV/s7REDlfT8Axn6uYqFVx0fPu6gBsMZiaVNys6p2kq81S8zKEYw+nS0nbn7E075wQTziuC1LComuW69qQB/OUaXvVBanX7FJz3Tj4g9ph8AKVesxCJTUkZhw31mSEuVLVJB5mPFLWDCDPqZjUuBiX33s/arPQ6if2kvnFqjMTE2M3z/5w2CjcFiqfoDKJh0ZxHoPf7YA/zibmC06CUJzB2o0XBbNgG3ojm9k7hKaHUFv9R1WltCEo4eFYLZZm/GEQkFgbHHqSzEuOPBWtPrtTSKJOr8WHXIdmXKeLzMi9vhqWaCkdCIW3LsjNkNa3nkrpZ3/3pzG4B4gGhzgnQMoJ9i5At+pybp+epkS0sFocDi1x47ydzMtCoSbznfoncOoTDtNBZD7w35XuQP5AlnbmRa4ddqcDEgIktzLN6dH3SnKxfUjRDPAZVzmpEaWzTUVnpOjaBCV53jNqU4vfiwe03eLMlnx7uFqO8tjx4FAXBISHvx9FRr1TR3IMswVu+ZX23YwN4GfncdYqGrYGLnoNW0fhKX9UqeEre3isGdBDhgsOau4DBKmDY2izO2OY7oddiJxqXFUDwvv6q20GyEFlXdH8E9ADCWhvX3EDXKoOdcBgCDU6YBpO3cw323mFIXUZonpn51Wtk+RpzC22mGQWBVknkRrTXyhhvg54Gm7HgZkSKICE7Qn4P3Ag1V+rz7kNWfqZMKPLZ/v2LNFZs5ukS+WuOIxRKJxZczlGvpJli1fAZDan0AAhhy7yDtWibFlv44rKgUyQRlS7j7If/ogt5rVI1VyQbbrh/+ig+L/UG8zUBuvAADgjxGUP3PxF8/VqnALYDfiEvSlj2PQkY/Fzh+/HI9RFAIbvFzfMB+HQuNe9eYCPFFceQsPGexEQAbKiNoNYhNmVPxM1oxB/aboZWror0IDxhgRFePWbWxl2i/0VWLw7Judtml7Z/+Ib9tiB+CGSq4ibRUULIHDe6L+vp59N1NurBUa9vf5z8yEe5HjC7HJhx+/5J2qDHksWLMdCdaJpMgOl8BQRJ3j7blZYr0W2URJ8l+lU0Xv+XA5xiO2ansPilMO8X9rsFN0iaCzssVZVdihk+SpeMbK3BP3RE2F+l1KvRsO8mT0VaaMrSAZDuO7uztnee22dYMDlUOWxTuZDGk3x6bFmuFImjsKGwDXPa8DkXh+/YdzpH8w7zyH7NUYG1HunHL4xQhjOGcShnmLeD1GZ7V9DPsN7fIey7/Bx/owpuMAXRS535uqWUekDAsuLk+3ZjcVREgcOUnv0lklmR/hhiofMuacb7U2937e3zMSmkTdKbF7Kw1k5jvVGdkMy1X/199tX7XE9ZssNNMwXS7Fa10sMm795gXK5mI+lr4HNCaGd/03nshblKCFYjBvvMcqPKnIiv4I6AxBFKczHlRUwhhyRJC/q9q1EGwvMTWe58fijYxaRADjYwTeLx2Qb3EiJeerXJjm5z8U8sYS1ckLgfaa/+f+DK4nCx1qafskpE3Em9V/gviLupvqSGyBw3u1t2qzk9ckgO8LMj+D2EjIYmYZybdJrWMJ/gBdLA7PIX6QGu5w0yl/S+FgUHdOITdL/mbRD5KlTUqxU0XY8ZTlsS07HGh4VpsfI4QbDSTaRABg1FhGn3Jpc860k6HLj8qW4WJj9432x1oMUFSAPnXenvnEosRzrGok3HxXBJTj+ZMgd1CqlpMZl3dbj3atyxu2aSKLTfXMzJmyNUnE3mroR+8dI+UXy9Ox7jYkeib8Yr+3L9hUTqNZ1jk3DVjzkcVPP5UNDfTMfr+dV1oUsLwkdrDuY79w9VvrT89EPKtGYALZa+3cVv5rAn7ymP46jy4HVCFYdYpMFFVNh38OuVm8EAyo9CR9Zdcklu+wjWR1wXxfpFqRfuQXyoIUp6B5YLVjjwRybaFC7yVaw43D+NAa/c1azY4yPMnJHAk+zhgTd/kzlKmB97rK41VrUHah6LyPne5O2uaffe81pspz0iAlkox7HrJKR2ZuSURJfgTBFM+l0EbBkY32KGqkXbFOGzOJAny4yvMFjaqDFWEcLQ+mT/RUAB5sDmRq8OsfDM1BKOkyOB0TV/xIXkL+xfhyGbVk6PGc7NvZi4HWjvTxTTNK/O1lxAirbme1vSX3f2rOm2LF/nGpERWcFv44rRYBkMCXPpTqTnekETZ9HXCQGzueb/Ntj3Ec8xBgyvT4PBE8p+pm0BBAdwG12VKSMzV3OghpkLaa2DfoDgq3kqWy5dlJh/7qwxiLgUTdZlG6LSIVKaF6EYGF+hmpbkERv/uyOzT+EZczWJ+oCtUmADtr9bhpLqJ7PThYx/nmGjnXQWHU9sRAhDoJnRa55U5WyUt0qr9b7kqwbaiHIhgF66KffwljSmLRmzd1hA0rdRXWmZ7Docr+/uAbCvjl+Os0UpFHmw9BKfANx++widBbthrL33RabtZOfED47ncr1x+eKDQ5WuiFnuGtRonq+7Zc5/3SxcGeM7Q7EB9icFwcVPZTh5A0mraWnZg5R+FDRmKfNrSS1buQ5v4p3wLGGR/VOtmJumLUau4kINox82h9mTxESYMOQl8AnERpr/xbeviZ9wuI16gWb84kqpxaBq5DdIFdzvqDsM6u0ZBhxWiEqgwmSesSIBVBqfk6VJvQj/65w9cnoyND4hmtAFaSmNG8rDEZOR4HitPHCapiXpL6e1Sh/7Ss9vEezODj2ikXqb7OULfX71GfX5oh4Jb+nWh/9v32D0LN6p1rs9t84ByN9pRkMp3180Uy57eiKnT44traDc7CFBej6rZ6BlhLXBLE+r0qfLmkVc0aYhj2CsQh22f/d0vmSUYengSMQi5VuLuZR06i3QuzRG4DJDS2TpYNERNRCYg0+9qK0iXj0se0jK6P3vfszL2hAbwkYHiSvdCy0YniZZBBktnOjjzCcvCtbZNmHS7rme+2VN9kaWRKCY7Szt5EVhNpsuyzwwEWpBe3Inl/wBiwZmzplPU1AaDe6tWUitVJZVoR+nPHBEsZU7iG/yiehusFhMPXqz8AP9577BADjM+ZjfEES4jBf28HBcrVt7OMJMubncYsaksb9zlOjr4vLb8GdKZbfhhJcSfJZOsjo/EIoan43wM7EkxVqc0m1PFmWT/UddRW4KSzm3/UiNTFHfUgegUOOYP/Jps+4BsWZFKYe/joQJahms0G08OxcfafFCNOmBY6pkL3W4dPg4A+JclEF5yHpocDavHZMG8hwc3vsFr1Ggp+8FPobgIUUIfcCjgEsAJmcFG8BIw8tkD7cbsGTo3IP6O3DXls+jbmCzbSYTW4fw309PUywcTV/n9kaLOqhKD16v6zHl79Lpsap48B4HCpcgUKSzrh4odQg81n/S301gpMzVi5hmh1ulkFeW8aREVznbChwuH6hCggdiin0Of2CHqTAEgsmfafj3ZwBOO7RxlEnTqMKoJmz8fmGfETu/V1OBbUFHnXkYeBkG8oOiNCsvQeLmruuyhJ3IRNbaEpdQ3tCDfthoTTmdgOftX7dzQlMy1YKClfNKpcf4+xVw+kQPLLmmRXngrabAL69E17quuX3pj4XJD3xzUfj8XOJBY5PRNenRhzpvrzjTPEwD+rXeMHN2df2JYw7ReUnfQgp+fY4RlvXvgZHyM6VwvjaFS/FN38IiGGYD54viDyFhzfa6LA9wHNJtDFQW3GqYF3cASSC78RRUbgxE3XPA6TW4HHB4LzDpqPMc0PRzSjHjO0wZsZw7FdEr0/Vx9sKFeiLFjLcwi0R0g821pX68aWVWbVdlGc5JUpAjpt6tEQnH6rbdGpl21sovj5ZhEmQtlKzkERwPeebJ0iPS0UMPW1YZEon9NqT98ESKk6J96rlz4dp/Pm9xp263I+zPIcxtWRyImrpbyvWSOKT0WC/AWLTTcbkJMUTFY8f2yP6bgMKzfXkmG94iJmnjDX1VON4yYTIRumMR2rkar7ouY6Pr5YeXoi3lODqCwqFnL1ZiWfOyYqDALjYxVNjodAolMfNasxeWaDUOVMWFs0xG20L5/98WpfsJC0wF1bP9YfJvkkzoydlxypQzniSSTtDKEMBGCbK8+HoRQHA8ySfdDbvqXPE6qT2kGnxtClWzi+i4evMWNf42P3na3H7sGbVZS8nCXn5KPpIjjikZ7TjioGRDw9znwdXBWlJSgUEusR5mnvAzCsx3IUKo7sU/j8hlgiD8sEj2s/Nsm4UVapwGE6CJM1qBQkIfmRT97iKu4nbNGWujTsH3+7OP1hKIU2cAx9CT0xNjjN64WqvgazEZLoXjrNqS87DmVUY0cgXGBlp+nd0HWlnuNrkRwaKxitcOwXHemRn/nvc7s8CPxeDIPYG4MJaBq4tdSZ1u6SJpDKqyE21GCXCjQO4OEQSqcyCDqJ+c/BOWiQdsInJk9WRk26IHCs+HzJO4KcndiO6F3f16L3cH5/zdiKcmIEUDG4XfZPB0NM5K03OuOUpo1TFMQw40lnlsTy4MjWrlw0M911Bo9/a7fRq9sogKDs4kL2vPMRgRH3iasIPv1It033YwxX3+RroF+1smC0eLL2dyO/mZtkhyhj0Y/XTUt88FzeYm+V+ZoDWzm93hlLjUxzGNDHWS+730Rwx3uCZw+7hoBEbmglzCFdXAklh1rzhMyNtrOxKSS0XfUcuhMbtM74DCfyvPeyWsHupomnOy+f/I4AuCL3UoUE4piI+WqJzS/A3jeg9DyjOnJK8N8qVUxUJtx4gL252xePLtyua2gygQBI74yizGAYp+6kk+fg1K2d529dVNLTDprKMW4Nrgbammz4gBumFBNWJ0uYsK0IaPSPnowlelYES+WseREVlTTn2qH9YdniZ/weoK92qBDKCGm5pf8i2kW1tU0cOzo31U/MURsWM9xGujDuUazK8ZrwxH6vlCec/exD5mqAIoEQJwzHmAsCwYH6SOwlSMX0Y3niSn6X8wyNGL3OAILkMLnwtkA+873ZK7M2UFmBho2khf/NT6MBujIPys6+Mj03M6XjTFU4R8OjDFDWL57Si2uphfpBrNj2qrXfhFpwQ1TsUKnSRWHUvY+VvREt0XTOVgJhjt7kvDqCu/6QQBFgkTU9wYFlXnNhnUeXas7lBaJjJYhufDMT0KtPrYVVAAzj7B6oRWZyyh+AO7xa4k3HYVRlxqw5SCuKTOE2e2bjuVfEfLPbRkCSpjdQLYFAR9cy3piPTiyq1mvfzk2LuyQUN61xB6YX5eGuY2A2OfpGO7Na2W6AL7t0FLSf57OTeWC8M0wyYxqbzrQ1/vi7CJpFHQbxI1vCb6knXziUSr4Q2YmXEQ1aH3cGGczf6ABtqWs/juQgbbpTMIVB+qdESbFd183i5+IzycfxXpxQKBuRal4aoYva0mTkpHG13KU8BEIab41MxkuPp2Egdrv5nrCWpn2rIEHsLZCFvnvf9EH3fv3g6tzJHoaWh2ypgEbpyNuHxrREnUEbL2ZKcyr9XaG0cc2a2GOy2eIf0N5qV7hcB0t+7vsh39l05McsSE+ic65HEu82M+pfJBlkzAsVHtby2U7iQX1vp5Hmqf9nNh+v9W1OdbKykJjHU3m05lx6RegPs9zgl752nBp7ApDZeOvMENwOi9Wv6dXncpb0cqxEnYiHs/ma27AIfb9KhzXKbpgF2M/0lBFJFKvmvGPWWGte38ANQoVyZzE7NoSBVV/rHZa4/neY7SV3GbAlF7LrQQMj2GUKCm2OuQPfZCRnjtn+ypxAUfa7jCKiSA6p/3jckdfROflDvU0BqZ8ZBuUOo9QjIv7Wkxq3TN0NCifAMrBv3H+T5M+OgvmnjNn3VcW7eCg8l31AHOWT1viVdi4HfBhb+fwL2BOn+yAwo5HHOKR4W4bvU1LFmYYZgXeYI6Isv+ZEUVDQCEUnzWztCFg7hoHdR5BMD+HcEQDTXGARJ7Ac21jTntP0gUoiuX1KTWMVIGzcK5lsLC3pDCgQFhoCcxlZbBFeEpVlNi5qgn2lyiQJnNwacDsid4wOaimI6nnhjq9W/1TfS4XYLJeriJELRiElOg4Gzazygvp6LBBHzOCkeI8JicVol5T/Jc3/YiSiY+pOgS3K99VSqwzSM9qXB8+JkDZabWteGkx4uxoRAiVG/TgkeHSMF2jVWWwio/vk6C6UlBKrF2eLKE6pC6udo8MAPuyQm+06rRinByTG8hIVUoY8C2lcEDa9CpInenCkdaD6yAbfpNnb/msxoRIytoN9W+sRIJnt8Epa7AkxOHN+Bl4VXkVSAbcrafWxhDXPRUSjtZKNIhxUDW6jUbncgJGDbQjN1ZoNBqbUWr4I3tXSkAck+0Ks1r9CfpQCuwt2ksn8jCa04Iqt9pCq7rNprpHJ4LMX4bmjElBP+H5IMmZwjt3aWLRbu3legAVoXhFommLGDXbXv9xt1C9J2c73O6NCbTvUD+BT/uBM1DghH8BPk7Egs03qI+2gDFu+wy2h2hVh0fLGIYRgnLUEPpWUJpF/j1N3/t0kqcn8pJV1Wpown9batBodBLbzPefTo2+lp9tdC/5vP/VQlq9b2aSYfHMCoFm55gzaJTysbsO+i+62MIqtLOemanPuq0xQyL4vEsTf40P9bmxiHEuSJ4s+iDfnb3/wGJlmF9UWZhyz+htN4O+nH+cv9AEW8NOOPFla/1ueAxFbam8iCl3RPc/4YKJJGZMUH1vGCJiDSPSKqCx0VWrSr2rfdcuMM8ecTAIjPbVFH9Tk8HaeFLuxxtmumcwozDNM3SM43l2O2KeBag3Fe7fzauLjiiYR4JGCLdi0btmyjGN/HZCfClW7aT8I3OCU5hJL7HMJLom56ZXP9RK1HvoZNlkVLSZS+MKwUDrfTPydOZn312/nf6Pc+XNsJXuIEtvpb3WejCi/y3TS0XtJ/eBR3wQSeBrO7VQxSmOzDxBox9LAS7Tn6F/Ke3RZS7+Z4at3f9sYUut3SSAiiUaaHYWfx79EG5NWH9sJU7JjfS4gq5jdej0rY8I34zybMbQ8bZBlE+N6eTBQxVUtYC9l6puDe/arHPAfkBlPde2arck4ZzsxbwEa4itWTHwL7q38SK4bLunqInDV+08Q5yUZ3zB5W46hkj/fi3KwAbCjR2qEovGvYcyItyzhkFDruzWACSJu1wl2iduRU/WcT7IsIuq6robqVy6i3eoaOnHNhUAZDJJrEbGA8+VB77XoxbGwYl/1OdTeAkC3lMQ2VkHra1VijGHdzgWneMEeVL2j+Dz+JKs514c7NRiFt86Wol7iJTbnclJ5D5TbGv1Bzqzr424hgsLEP3Gzze06h4XuKUJRHGfzoM9cBJWzhW3hbdQTuyFxyJh1J9QXf/BT/XofOBJx7zoAOEobTbiCtVZFRpbYu3g6Ke4fVB+3H01su6GfIe/tibATGAtAJWLH0VovU2GI25n9eMzUdetu7shp90pXxfvK+g84Er+6MFErf5ypHZIdOEQW4m63+Vk42kaCGg6Y+SoZpD+hdduYfLG8exkYPuWR7wJUgUTo0yjWnkx/BHUeKhORlsgS0eF5yCVxPjP+++Pxazy2O53SW82MoqXF+Ax8Tlzr3Jv8MMcCYtvNSku84k6IM/FFaHazPSbkr83lhrfExrX9FoiOsr0J2u3pjOP3/XUyZlOpmEWmNVFVMdt5Izv7vHsPtvCXssiW2LVKTRD40L7eH1Ypqzc8CmQEvb0FXFHVKLW8P1UHJSoKGbNyTTmvPYbTKxkWZ2d17mtzSWY0LGiJego5oaWdxY+odbzF2FmxA2/x71NunF3gCctycYUjjLlf/l8VoGd2stmkAHjcQ4brDYFIj65X5Nd5forA+dwF3A47r8oQZhbECOCjuEUmnEJd4IQAsudjMIiLD3ePWHeZrE4gJSBLSBlV7LI4PAb1MLY5VOufdU6ZLpa8EQnJI+xq8J49bT05Q+OccY1LLdDqJ+rFao+axFiOCQVzwZ8Ndbzs3jF8EfdagMKvzjTQ/1p4eo/HV7UoM+UKY6LaNH2Ffwqp/R05x6cqiQzxwhpgVGzsWs4SYDKH5jSI968rFIxNZkQ+cLnrZYO1nJ1MWKZGaFjDCZad/AAQpFdQcs2j/az1ovxEmjD4N5aH7FDqrhHJRM2ztSj8E3jbmf9VdZCtHGjHHoTga9uaXY/xUrg3ebIb+CUoYnoSvdlofuxEek3kq3Zh9hjLnQ6zyAtMgDYwqdnExe5haEjaeMD5DpYf4uhFZV0zTZR/WPzCXp0rjRakxO33RYbU+3ff/WEGZQvwWmWcFUFb51KQtx9plqx1cw2t/QajejnJz6/Ytr6Y+xJaPRRiH5d4pMJ1U/8eUTZWxFmFc6n+JjGlvctNzer1zDMdqUu420V1JPLcwU8jhYpt36ITJSZHbCUVJQY9BuMBXXxWdBdc7re/W3INuwlG0akOQMrpKgBySeM7T4rcDeKGrLrNQ/KJnxYEyzvnZiogeZxC69J4B0Qm2oJuqhM36i5ae6qGPR9J9TRV3fCAJl5YuiQWu1J5lHYHyeiTG0JV++VEbljwDjgzyL3V4ZJq6DEQzB3zVG8vr6VqgBi/JQnoom8/i1yBIW9/djLqtjS2lneN6fNJGyhGNLKg61hn/gYL0K+GCttUjtMV8sP5BDFdXTVDXnhQEqYfJVghLHEM5rCK7XbklwUKwTh2e1/CvjfpA1QCkuT60HuINdki8ZRJjtaG8mW4wkPbsC/GosgmgLgQCzmRwlmznuujuMZKvP9sp/Ls7KtD7gkDvjgXFG8vW0PFxmk+0E2bmoQ0YjoU5tWFPK41Cm0FUy5U1oJICjWk7l24AHI8wm/Av/Dm91zAdP9ObH0OWAiwfLbGnoaosGDvSxzz6JXhK5+c034ugRZDcy0P+OrCGE6PFrw1+ncSO4CL7PWBmuvWz4kWu9uDsYgVYYSO46BN6ZsU916aigkRa1Hg7uaK/wdJLpBQhnnJmu0WKVD5o2HjrltNgQytvPcG1jGTH3T3XGTxebhDviA5RVw6JDVYM8lUkuB61NqtmwNYo00QUgdMCdxNbkleqiUjgSN8pdLe94mHvGf4IlsSFIrOjR07O5DOJ4BGPlu85IN7K8tl490DXeBz5j6LtspjWgU5piLpfbfj6zQSIG+46HTsAdS5eEf+wcpRSa9a4RPxxvMJGr3yfntTy9obSkHvjflviPf7CFiZb0xxv0ghp48vAb8b7mUwouqE/GTvvirtmafOAJF7j8AhU5hiKyoElJzBI9RtS3sj/7hBSPqX+aiC5h6XzP6lMA/RoExzila6n9pjmaNAEOxHqtp7gtCmsn6GRDZ1da+DO4D+7L215leYTuCy3DhxQnS6XMajoRKtjdW5Zz4iuI8tsnneGWaSk4iqNlmvIBlBkbt3R8XBzI+zb6cnX54ASoSWjE96UnCsQ5NOCC9EDVFzlPPcgdqBXc9hnsepI85w6cReHWlLtPtAwqEK1FTQ6hOp3KVjhsy/Rvd1iDvUNwMLUneSfjyyHxOoafwwjpLkmRMRSgMMHZr33JbzCbFzefnaw51pClMlHW/XAyZj7Rcq3NQrelOyleibKI31jUDLRwRIGDbWIKbLLR+xaPSLsSlufY450W3oRJg0dZqGrPy9qQJd0TdM1ungacXlFyiqt5KamdKednZ4JUW0rMYRa/m+aA74wnSKcVLBuBIQ1D0D0qnTeYMZvLWGWNHO0ic4O3tQDJS6mpRy/gaX5D8mW8LNlVVjkRUw0SUR9sPrcl/RcGPn8h01jg/V8Wh4jW2Uw9uNQSD141MzrzL1mtTMx+NPFt0JCtLhMKnqnEwq2iOm2pnBKUY8gmgjTqbnvVmL/S0H2pP7aYsxEUQSINEpFj89dt2jNrKQqoGNfsoRHag8g12zAJPOFMBQzL4R7v8r8AdbKzite68rcBDJ+b/48L4HvNurK0IzZiNfYux6Sj65AW6Uw823Ww/FbDLRgn6XlHQ2gf+/+8a97UCzjUxRdCU9DnBRGy/CVb9eOSG3o72C97ZrlOoO9oltBqduMYjik0y+ZOwRno5cIHo/XyTnhvRDBCELAy97u1QkIv+aC5j5jAebfUoFeKbGCJneuKLzeVMAeeFhLreC8SOi+ZBn5SkjS0ro7UCF3i3DtWwlAfTzAlAajCqYC36SiHhHf3PmGBXC2fiT30neB0yIC3rgG3feAi32CfhzEZ51sXCaUbhm4MYIyYU5Rw9U61Xkcyl3YQw9CmMOE9PZokhDvl8xCWKeQa48nGc711lk+q+CtljJEt7PkZkH/aOlxkTUlPxlXPyFcXoQv/vu1nKPejpR9cFMMW8dDxKfbWuUQJADnKH7ykdpASZ5uLbQZKAsFbGfWRBcxpHQZfw7lZHCULEf4tZbUNdo9hSA+tPWTqiBGObH9bMenz1R+7oYtTATtxF7akyyjpaQapmULrJ5R4D0jIHD4eAEom9qklgXkKpLBiMwCxEOp4fY60qWiMHx5b7CO2l++NE8a6Li/uDk7JbP+fak4fpncdrZYVbsHoks9jcp3jQ8ckOIOSWlaqcPxQbkjLgYGvtHINI2SSUyP39bpnh3LXYovFrm3rS+GUqMbQbg5rYVpbQ3us/qqahdCO1xX10hxnmPIOnzKdStBfgovgZJ6V6zo6GW4iQoIFplTGXOzgKZzpjvl75fXcD+rAIkd4f46wcbhy5nSWtJu0DGbBfLiGcbRv7gaoZrf0O62MtEGDVgaFfMj5VSYW+zS5XfZFcM/CKPOxZ2gvJK/s0m1Siljops8MWr6ZsaHBYuvFJ1ZCneytS0eE+peOc0aaCxP7AXMhsnztx7l9aCRM/u3/Xp3Ep+L94+DAC7y3wVMMYWJ7H1+f0akjmywy0CMQ7IPqZMQbZHO/+ZZVa1ovUIqonAmu2ja8pQRGWGFCJGRuV1L4wD33EJqWqLLAFVJz+9fcTP0CI/JmHs7MUhOe12m8lZG7EEaT0nPP/p1MPqRKMVu2OgsPRk+9FMGHkVrihnpB0dw6Fmd8UaYUDvSHiLc1evVv5Jii8kwaOjL2GuMB8vLflm5N36xz3SS2CphXuawKY8jSoC7lA+Lj5y42l3B/OLMGr4BueEVwtDQDAVxPhbfRvFmqiwELJTJZi1meLBQf6GmNKw7bccYTG6lkbR/PJ+5S7EB/Bdss1sA8Tr1QrLm/D0krfMH9HUqLY2RN6yzdx44Yb/yJEclFDCM/DZhRh+X86sw3LSj9wu5IBm2OR7lW3qQIVXnBPE6X8mznitCnIUW5GGaZlJEKJ08VAP7Q93N+ZaU0kg0VKexSWfUvM5Ns1LvM9R2W9y51zQx+Irefi0l5hI1GAdm1OFNeYkcSrxc0Pdu/Ov/kJq4zwmIgVEEmHNBmXIAyuAmQV753pp38znihObDQCeJc5+KhBzYulKrbGoBn9zND8+MN+EjjtVU0lzx38bYvxSgeUZAQBSkSSL4hcitNUC1cqfOKIgd5IBDx0j+mr9uHEpz6bMCUirFeD2fzvB4Q9TGVKpF+ghCrc/HbjiMbaENLAM4IwoJCfPiFHje27b/deRS5VVL0Z2AyGVSwyfpgDJoJN9LvMja+CckryYw3b4kW1cjNP9Tvl/Zgd+4jNH4NVODP5a0BRFhD0MyxK4UnwdU5T1a2+lsKohi0k1LA7JVNKX4j+XX4Ez+bv85qH86AYKt9MaFjNY7sgeTVeAabUS7Vpvq8J9WdDIuHOL8gYQvcyUNo0UYKf7xAqFu709nucvArzUPqYdCU5VXZYcOsRIm+Bgn35aZF+VOFv1FiVjL5OGyGZTa4+SDsf0LQPAU9HaH92skPGpEFf/MOo7NoWnLVWI27ua6v27XTi2FRcn9VIBiQu7mbT+tmd2rJILHCPtu0abrdNyF1VAoIlLCiTM2dzlIPlt7hAFVcljSYWlXL6RGCgc+8SmMfdH6QTqgPjxBIQoH88UNCcBJPiyAM7UNXIeQ66yEmQ4toAO8Qq5FU6YmXb5RYiP9+69GhKYouVInSBYABZHGEiv/eqRlxICEQP0o/EhrjiOMY6pf5Cuo2fdKAfuD49Y8473nRuEMwPuFpV4CsHffuDoOBXRfAYvx7ltibEnm3wpPnS181u/jH4Z2vkWjVhBXVvJuLMbROC7dAc373EjMTuDOfwMcIkCZyQJ12w+GP7LR0hqjP1K+Fn2A3jcXvIvrWULxDgg5WsemNU5aVWVK1mMZDIN7gHMuset3nvVBTIxtJHurUvJmp0IvgRJxyD3MyACrDowEc+7aukMPgBknQOdobGDjmTFd0syVjV2Vu8MwrZC/qKC4tfTvb416CBEFIn7cNzoY8LWx4OOniFR5Gg8tqTPL3rcro8TGODXdmoBP366HAtrMiasbK65NqYizHwKnVBN8kf55O6lOQkxrVhiJzOrghf+I8NfzANnUiU3kGGc7W7YPzN96g4IrRYKxe12XcmFPCn29EqIb/WvmJbvdWK9W06hBpml4Lz5pfeR7rxDl5ACoPzZyV/hzWa8ra3qVmV+eMjnbynHiLFGhI1jiMPvopxX2pK+FNTOw6wM8p5cWXSNJcrzloGwiexbLJBy8/EPwscOhwocP1HukiLl9KoFj2KDfNaYGRyprmO3FJZ+9J5zw0gakkDsSku8FV9dS3OijJf1oKyCTUYlq1U9cp3AG1Ea+25Srtum2w/8vFl2o1B6f0nzHaQJoTNFfelWTeF3peS87tjjSfD5MOTDINeW+VQ4VYapVLyQ4pPzt9XYyqdKOfhKkLH8ZlqcyBLwBFoH/Cq73Gi/MBmoVvKG1BBM6dEbA4OREVlnDvWoSNxLVlyy67XVCO/wrkeDjDs/zK6Ui0KcuP7jE7Zkuj09bfrRRTuUaGwNSS90i0BHZeTIcKAGUEu8My6dSybseKm7hNfWZDyOzCrK4WAesEbQ9vvGGgQ9BQgamfweh6Eq6QJzGfYxpMFN9A0nVsqg0OD2Kv2nHB/rIW7VYvHyWWUVe2zjIr+9SpNhIdRQbx43j7vtWg9p5r+AN7NcRR4R+5IK9X0p1H0SY7a8NvLpJWb4Vbs0AoDS5U9ejTwF7u+how3y+ro4LuYB4CMYLIdKiW03G0hNOyncu6yLE3dFzjRmJz/dkA8yu0rql4XWlK2qJSmW2vDai+KLzuHQpAY4Znpj5WdESz1wCRCbkzqw8lXhjDDLh/sbUado8MdRBRrNLvo4tmWwoNmsyoGSKTMqAiTznM8+TdbSHjCYRIUskyPH0jdFGfkjg/xUQkHeDAbQz+1Ml9WkWrmAQrTfZhW36wbH/pGEJ1dTed5EtWVrXT5N7aCnwS57ruoWnMDmp0jTdt/MKpnGbZXSKZIKrNRby7Hb0Z+lXamuhOrrDjmpYSl8iJgwUtvjjxXI1fl/MMqx4yxZSJxYfpgAeKe2lUboSRIXS2LoWclvXipraSb/EE9ejtSnU16JG1TF+9MHkHbtItm+fQtzszgrAfqCexGis17yjxjAI0ag0KFbkBHYmYhkfvCnJ3Z9HqxdZ982ADj4a202L5/8zAbo8ECrc9JWvZ1iA1p8AO3CS/P8VbK+JP3+0UltbWNuyBtla3Pr5WOH1FeM2dOk69By49rDsShwmZHfJO80yIdskNZTuGK3iO82qwJXGGOIDNXo82i9apiMLdttLwW14h6Fjs6mwFg9LN9Ag/+2XgQTjlkK776rlI2X8rBW/MNo5Gqpf2jFmX7rSyFOXUmc5myFhVsZ5n3ZnTEqGxsNKBhRqTIJq4AlsJTWeDH8HRKr7K8enTzBvGX8uZRh+Z0QqZUjUrwSu+YtXd/cKTH8WXQLsRvEcOdhKRrxxTBv71ggIx1OraulPtHv0kZp1IcTWwHMEU4d4NkscV2hlgOHscd8M1duiwd0aCCw9RxWlwcgXtCs1j0jwXYDyk1fx4LOD1hETIZmS5qpK19YWUHsZeL1ggFPVDVGjutRA/do9XuuDNzDqde/aGStfw/FloSBXj/Vju3Z8ASLHv7mwDI5UgaRQmwzWHgvq+C9rhd2jxiS0x2u5BtJY0T+0wpVdWg2pQFP+N5+8e/NTXbOuOgA9pi2J+UhX3lBBn8SonEKvu70OlFSJnKnX4cBKLJGNvCqe9zSDSxy5cFeVr2wHz33z43xp4654ARdyKYn5t/BEf/UvZ7wXajAyUY7vRvEnOdRBLH8xsFqnXza18fOgi4JZlJyUA8qWXnV9s6kJft5dwBcp6zfHdQWkv4AVzXy7pf43x4xQKf9cK3OWghyXA2B2rR9z0CtU/5W8s1KieNV9sdT826zhpFauRfUt7vJy5gf3Jzz4F0ze/i2fANGqfS6ToV3Dd112zItOPGMi5JakBVX5WlqP3VA197u3HfJ+PpfgcC9/EBKhGsmJtN6xc9mdSOX4jpOHTVGZ1ysvqKDmK5/kI+hIVKDFmeITyBhLavQBkhZIEJBVusO8DOLGyNERdhkpHTvxbFM5fizq+umMmkjUT13y/H5ema2ZIYi5tp3v/jALshuCz/XuDiOizCxHN7dFYaUfcoyGJehRoL1Tsc7ASFBiBiioCxFxxk2Za3zCLtMGrrABoqJ610mbFnMpsyW/T40wyltfkfv2XFJ813kzzqBls9zOFpACDXIsVFjQJWxHkXIcdv86sLLLCKF+qLB2n1GaEYM8lujiNHvQMhLGRoAId90TWJyNf2beAaMNMSMImJEW8sfylZcSCU9gVW+fENFMMBWoUvpuAZSA7MUd36NkUsq9JVmaGi1s2JXA/rb9EWRGy+r1St+NocbA4f+3TP/SqakG1zwCeCZc309koIPJaUZVZRTfZXHfVpz6yLobnHHNQBZ1Ub9Ryi4LDV2/RP7p/+TrF76W2joUF1/7ggZ+IJ73iYoLJg8OlyoIgEre74lXEtsNsi8e7j/dfl4BVQiNb1JDD3Niabz30t451iaMloN3A5CszW35EcawXvZMhkenOOxCVfL5D18PwAnIiumXfWimlWKW45PRin1jopfXpGqmD8p4AmTyvBJlL7QfYzE6HxoiPE0yFlGWfs26Zfb2zveRSc4uur3EWVIi3ME01Oy1pFTbnu3zcDSR9ruCLyXzYS/X7E2AIqxdruo/yQ2AxrUZU+HIzGSiwrGiM7hQrIbQup7bpM7RnlaUNiufeT/19zc1hAoxjivD8EO7D3wRgpiWuIpesViWtb+A82PQqsZf1bDkSK/F+5x1y/seFu9XfpdjwI6qV6m4gni4WkpU2l29so0soWO9LDyxRhMnzVux9gYP7m/9qFUbuJQWM8wnjcudzIGSfzzZ1Cr+TfhOvUZ2GLp5t4Ae8BVO5NjvCqhKe4S3q7AcpNGZIWX68Mre/MBKWu+K+sDpYgdlYVikti/xiUeHVXosZCLtc9yJE9W/5HASyf17l11G1FDOJIpd+rqD5/lbnboyUYWzPnx8PRbyN0zrs+gBlSvMLv2Fu9JNy+o/2NhuV472qh2bgxnqOWl/Wb5bUBUA7g68a3V4LC10Pf5tBVmqbmzug+m/KUIqdL+7hDetfxyEJllksuNZ23vAyaoNhRZyeJkQhiO0IZ2Qm5KiXyPYo/aafEXtunadCZkqnPIk1NGh6nye+EmaL8sSVt9wkcu7U+Ak+oY8W+xgf7DQECEMMkJNdR5AvHvL2AfF9PlTlJFo1mGdLGurljF89evw8bcpNH5LH/B9QPiODNYVmvgBF94jSRdZwr7IvQDuGtFEVIomK7fdUttP5dfLGkCVFmyZR7/unIS50equR7ROW6rH8UWaUGfF2e37P9odLREGozPbCMwLm+h07D+Sk6a3vN4dKBgXHSMWp00Ga+/k0WwP4fdT5l2Hrtc2WAkha7wN3069l+ujtv6eWj37ikPSQ3o88rLqoD5AKrSaGZ9C2YI62KArTdN4wqQiic2tLjpMLsaSzQcDmXZZ5H+s0ibOrHMxMUVCWSwca2Ec9bpxTzP65DYvdV9sy+MAMWmRyQT/iYHkTojybCT9owmgwr+FLqJ6iYL3EHSW4Wd8fFdwpSvZ+aRTBcN8Ncl2Z0cq9YtzEEBlBxIH2//gDeQMdw5yTjtqpFmfiTqo7T8aQVQNeURK3I2N3ipMVo6vtv4vov0Oj8NkOnX2Nu7Q3c1ceP+eQ2PrNPKCFoBrVS/iaD8H1s93avfIl7Wume4dyWCdyZKYkB/hbtNtBwAnX4RUTPvmUQpPnK1eFN+rx7+jOI4hnBnLzSxXuAAMYXRqJRaLG3HZxkD4c2uc6hD2NZ2+w3Q2Ntm6jAUIK7efoWSImT2pKg4J3/Ja5Vsq2+W9MEU1mXwtM+z893dubRiya4Deu10gETzo05yYhZmDGL5jKguUi7tz8ij9xTzcUe9gvC2JeZLrj17lzIsHP02xkUOg1cP2OIHHCFbfSfFRYQSoux3LdqalXtT3R6vMrXAxKMPAkc0gHCZB50fnNehXcMYuswRV3ZFEZbobIoHYETYb2HcLWa2RFcsw814kupFZL4gHqFfcL0XvJPQqHD5IZccT3cC3KMJVd8SomwKTM/ACS96JTv1kk2gr0cf0Gk4vLChQMyDhB5j+YYHdxCg6HPF1aAzK/wsmwRqU+Sq/20WcbqwY34+YjHipZcSnPOKPW1l6oBHdu/MUT09LR1uhoZTYjMIJ4N9F6Ni5I8caazzCj7LKFehIEYFCwyGiPC59kf7uDkgVhaFj33Gdw9KD/Z/q7TSX89xUEQX1ReE4qKX+fETlOVLgw0YZo3c5w0l3/ivnMLu/pLzc7IqbG4I1biAoDOdEkP3oW+0RrInPVrvIyCjP33j2UqJmJ5sr0GLPHXR77vJLr10xEZWfROu+dfEUcidloqeh7ayt4LxZbO4mGaus4tJCuvYeh5Iz5GdfFm/51mAhefPlVuoqCurblpEbbMUDs+nvn5rLYfvSmgWYCxe7GwCCFZDWFewco09f6jEDOPf5+CL8gqPRnV9E3TjOZJCYvX6LcoyPQsCfJcUY3svg14I2JPqIEgj1k2wLC31J6NPOOWaqdJ2XGzu1WVPxJexp/a4Lkf7qP+mfzbyz4vrPip1/SOxtuj7uB5mVVKS+f6IjRtqtgdPDyNjQS9jBcBwQeYo71juVOl7OgKbaNChmc4CL0+2tqs27E/dQ+eXy9RqjILu+3QMrj9YzWH3YK9vEwIOFfDa8g4G5fmMRB5PDh4Gm49WAOEI2Un8zeNuBm7/w0+6WySxCEdVFn/PrFVTRV6w+O+iDHH151LT0s4yC1hoPlPUA9grkbmF8fO+zOqMfRNBoYMroKQNc4WHcWBCvBocc5C4LYXfBFv6r7sAAdyDIjjXs92wIJUMX0PfGaa89zbJuzc1cEU6cSKwnWynrq7HC3nn2OW7JgKjIq075w9am09YeV+ysGAmj4J6vaz0X2FcKSlQjZSxFLtVS83ovdXH4qle8iEm/a+D8PK3Nk61CcSp0z8triXzcw4NHVroXjnQGYqy3bptY8oyk6WNvl+/072P1Qpq6oVMJ/+O9C0ISb/hM4jGuULZF04JhVREQI4LcmOsAPRfDEhDGNSc39qedAqxToQ/s7tSaKqYqZ7cbM3Zz7bji1QHEDfgZ2kH/cCWiS2SxpoyPxAWeU/g1vS70v3by/9YBhdMhLcL3bSb1eT01JJkkxFQJ6FSCrhWy6eOQ1BmHT0fGHnZKvsJA4nzRedXOoDvtQjxv61t+sggy/qgE0lwmqex4kjtqMSjfdCal0btEaEHeshoRCnRmUfvtHWBgX+EvEt3nrX6Wkwqi/v7SZVYPTafeeOgM6oynNzHcs4grDHOuJxfvJZf0aY7mPV2YxKSlhQmLJuG6F7WI4IGyQQrmaYlBuIlwnx6RE9SIdT9tUP5kV8jNwHaPtAap40XSVJ3QlQ1fHEjZwOGzJY/AoXHHSO6keQqN3u7d0tm4FYeFEwIFHEdPwd3u+cN9vpdY165FUnrKPyv+pSvHJ6hWny4G2ZNiDYujgzLVTkEjO40U3tiHl/wuHxAcjiGDzGCKuHpmzZFWzwfEH6qZUlpLzILGAeXnxu4siUvd02hI4d1R08ltUFicUGvhB5Ky0bgEmfeSvsSl3X5z3ULngKYD7r7JT0jy9vIMhCXux3fFOCMMr2dbK0aLTI8qmnMuF8wAdWzFHA
        - #1:
          - type: tool-result
          - toolCallId: OiKUG2gU1cw2M8cD
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: UjxmRUr6I5LdYqgh
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: qYzLIcp6OqlKNF8M
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 3W5iJfdsgYPHadF4
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 6NuUqAxbLl8BsKzR
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.