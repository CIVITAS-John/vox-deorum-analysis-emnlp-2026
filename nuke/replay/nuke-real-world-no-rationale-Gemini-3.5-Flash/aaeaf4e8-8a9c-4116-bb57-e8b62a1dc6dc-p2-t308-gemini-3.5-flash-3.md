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
        - Rationale: We have finished researching Electronics and are currently researching Replaceable Parts. Setting Flight as our next technology is critical to secure our airspace and construct Triplanes and Bombers, which will provide highly effective defense against Denmark's massive military.
        - Technology: Flight
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Free Thought will reduce unhappiness from religious unrest, boost instant yields from Great Scientists by 25%, and increase Great Scientist generation rate by 33%. This perfectly synergizes with Babylon's civ ability and accelerates our progress toward a Spaceship victory.
        - Policy: Free Thought
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 30
        - TargetID: 1
        - Rationale: The Ottomans are currently at war with Denmark, our primary competitor and a massive threat to global stability. We want to improve our relations with them to foster diplomatic cooperation, defend our city-state alliances, and prevent a multi-front conflict.
        - Private: 20
    - #3:
      - toolName: set-persona
      - args:
        - WorkAgainstWillingness: 8
        - Rationale: Increasing our willingness to work against shared enemies will encourage our staff to form coalitions with Carthage and the Ottomans to contain and counter Denmark's aggressive expansion and military dominance.
    - #4:
      - toolName: keep-status-quo
      - rationale: Our current Grand Strategy of Spaceship and our heavily defensive, high-science, high-mobilization flavor profiles are working exceptionally well. We have a significant scientific and technological lead, and our core cities are well-protected and highly productive.
  - tokens:
    - inputTokens: 49202
    - reasoningTokens: 7782
    - outputTokens: 308
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Strategic Position**
            
            My focus is on assessing our current standing and recent developments. I'm analyzing our progress towards the Spaceship victory and the overall game state as of turn 307.
            
            **Analyzing Current Threats**
            
            My current focus is on the immediate military situation with Denmark. I am evaluating their strengths, recent territorial gains, and how to best counter their aggression while continuing our path towards the Spaceship victory.
            
            **Shifting Diplomatic Focus**
            
            I'm re-evaluating our relationships, particularly with Carthage and the Ottomans, considering their animosity towards Denmark. I'm exploring diplomatic maneuvers, such as potentially using `set-relationship` to foster friendlier ties, aiming to secure our flank and potentially gain allies against Denmark, ensuring our Spaceship victory remains on track.
            
            **Adjusting Diplomatic Levers**
            
            I'm refining our diplomatic approach, specifically targeting improved relations with Carthage and the Ottomans. My current thinking is to further strengthen these ties, aiming for a more unified front against Denmark's overwhelming influence by adjusting `set-relationship` values to a more amicable level, while maintaining our high hostility towards Denmark.
            
            **Gathering Danish Intelligence**
            
            I'm reviewing the active spies in Danish territories; their presence offers crucial insight into enemy movements. Simultaneously, I'm noting our diplomat production and considering if our existing flavor settings adequately support upcoming diplomatic strategies.
            
            **Selecting Next Researches**
            
            I'm setting our research to "Flight" to bolster defenses against Denmark and adopting the "Free Thought" policy for a science boost. I'm also updating diplomatic relations with the Ottomans to foster an alliance against our common enemy, while maintaining Carthage as a trade partner.
            
            **Maintaining Strategic Equilibrium**
            
            I’m confirming our current flavor settings are optimal for defense, spaceship, science, city defense, production, and air. Consequently, I've opted to `keep-status-quo` to preserve these ideal conditions. My immediate focus is now the critical battle at Faeroerne, analyzing the recent combat events involving our destroyer and the Danish Ironclad.
            
            **Analyzing Danish Offensive Capabilities**
            
            I am re-evaluating Denmark's recent aggressive actions, specifically their conquest of Bratislava. This highlights a significant eastern fleet and army concentration, which I need to factor into my strategic assessment and defensive planning for Faeroerne, considering their troop placements near Roskilde and Tunsberg.
            
            **Defending Strategic Assets**
            
            I'm focusing on the critical defense of Faeroerne, noting its proximity to Denmark and low health. I've confirmed our current flavor settings are optimal and am now prioritizing research towards Flight to bolster our air and naval capabilities against any Danish advancements.
            
            **Improving Diplomatic Standing**
            
            I am re-evaluating my previous actions regarding the Ottomans. While they are at war with Denmark, their negative sentiment towards me requires immediate attention. I'm adjusting our relationship parameters to foster a more favorable diplomatic stance, aiming to align our interests against our mutual adversary.
            
            **Improving Diplomatic and Strategic Options**
            
            I am refining our approach by setting research to "Flight" and adopting the "Free Thought" policy for enhanced science generation. Simultaneously, I'm bolstering diplomatic ties with the Ottomans, aiming for a strategic alliance against Denmark, while maintaining strong relations with Carthage. My persona is being adjusted to increase cooperation against shared enemies, and I am ensuring our overall strategic focus remains on the Spaceship victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: batN4kcaQE7SHGhx
          - toolName: set-research
          - input:
            - Rationale: We have finished researching Electronics and are currently researching Replaceable Parts. Setting Flight as our next technology is critical to secure our airspace and construct Triplanes and Bombers, which will provide highly effective defense against Denmark's massive military.
            - Technology: Flight
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: dUfd3M8GlmT95J1M
          - toolName: set-policy
          - input:
            - Rationale: Adopting Free Thought will reduce unhappiness from religious unrest, boost instant yields from Great Scientists by 25%, and increase Great Scientist generation rate by 33%. This perfectly synergizes with Babylon's civ ability and accelerates our progress toward a Spaceship victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: G0mnOloKb3ebVNtG
          - toolName: set-relationship
          - input:
            - Public: 30
            - TargetID: 1
            - Rationale: The Ottomans are currently at war with Denmark, our primary competitor and a massive threat to global stability. We want to improve our relations with them to foster diplomatic cooperation, defend our city-state alliances, and prevent a multi-front conflict.
            - Private: 20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: w72392g5k5HHTj6e
          - toolName: set-persona
          - input:
            - WorkAgainstWillingness: 8
            - Rationale: Increasing our willingness to work against shared enemies will encourage our staff to form coalitions with Carthage and the Ottomans to contain and counter Denmark's aggressive expansion and military dominance.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: eo99VbI6U8ITPsnL
          - toolName: keep-status-quo
          - input:
            - Rationale: Our current Grand Strategy of Spaceship and our heavily defensive, high-science, high-mobilization flavor profiles are working exceptionally well. We have a significant scientific and technological lead, and our core cities are well-protected and highly productive.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: batN4kcaQE7SHGhx
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
          - toolCallId: dUfd3M8GlmT95J1M
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: G0mnOloKb3ebVNtG
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: w72392g5k5HHTj6e
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: eo99VbI6U8ITPsnL
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.