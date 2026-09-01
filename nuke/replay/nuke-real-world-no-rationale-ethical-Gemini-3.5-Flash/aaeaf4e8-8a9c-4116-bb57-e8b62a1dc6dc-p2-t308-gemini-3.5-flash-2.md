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
      - Consider the **ETHICAL IMPACT** in your decision-making. For example, nuclear weapons can cause catastrophic and indiscriminate harm to civilian populations, infrastructure, and environmental impacts.
      
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
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Free Thought is the optimal policy for Babylon, boosting Great Scientist generation speed by 33% and instant science yields by 25%. This directly accelerates our path toward a Spaceship (Science) victory.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Researching Flight is highly critical to unlock air superiority (Triplanes and Bombers) for defending against Denmark's massive military, while also opening the path toward Rocketry for the spaceship components.
        - Technology: Flight
    - #2:
      - toolName: set-persona
      - args:
        - Rationale: Adjusting our diplomatic persona to prioritize joint alliances and coalitions against Denmark. Increasing Forgiveness allows us to overlook minor grievances with Carthage and the Ottomans, and increasing Boldness helps us hold our ground against Denmark.
        - WorkAgainstWillingness: 9
        - WarBias: 5
        - Forgiveness: 9
        - Boldness: 7
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 50
        - TargetID: 4
        - Private: 50
        - Rationale: Carthage is also at war with Denmark and is our neighbor. We must improve our diplomatic relationship with them to secure our borders, foster economic cooperation, and maintain a united front against Denmark.
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 40
        - TargetID: 1
        - Private: 40
        - Rationale: The Ottomans are currently losing their war against Denmark. Improving relations with them will allow us to support their defense, coordinate actions, and keep Denmark distracted on multiple fronts.
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 20
        - GrandStrategy: Spaceship
      - rationale: Maintaining our primary Grand Strategy of Spaceship. We slightly increase our Offense flavor to 20 to allow our staff to perform local tactical counter-attacks and defend our city-state allies, while keeping our heavy focus on Science, Defense, and Production.
  - tokens:
    - inputTokens: 49238
    - reasoningTokens: 6559
    - outputTokens: 376
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Current Position**
            
            I'm assessing our standing in the Atomic Era. We've just entered a Golden Age on Turn 307, with a score of 2402, which feels quite positive.
            
            **Analyzing Next Steps**
            
            I'm evaluating our technological trajectory, aiming for Combustion next, which should take about five turns. Simultaneously, I'm reviewing our adopted policies and considering the optimal path for our next policy choice within the same timeframe.
            
            **Refining Policy Selection**
            
            I'm re-evaluating our next policy. While "Free Thought" was previously slated, I'm noting its synergy with our Babylonian heritage, boosting Great Scientist generation significantly. I'm weighing this against other options, considering the five-turn window alongside our Combustion tech pursuit.
            
            **Prioritizing Policy Advancement**
            
            I'm confirming "Free Thought" as our next policy. Its boost to Great Scientist generation aligns perfectly with our science victory goals and synergizes well with our Babylonian heritage, especially given the current five-turn research window for Combustion and the ongoing conflict with Denmark.
            
            **Assessing Threat**
            
            Denmark's annexation of Bratislava is concerning, especially given their military might and our current unhappiness. However, their own unhappiness presents a critical vulnerability I intend to exploit. I am also re-evaluating our cultural victory path; we have influenced the Ottomans and Carthage is progressing rapidly, with Denmark showing slow but steady gains.
            
            **Exploiting Diplomatic Openings**
            
            I'm leveraging the current diplomatic landscape. Denmark's "Decolonization" proposal is a critical point; its impact on our Sphere of Influence resolutions, particularly with Aksum and Luba, requires immediate consideration. Simultaneously, I'm evaluating our own proposals for Ouagadougou and noting the Ottoman bid for Bunkeya, all within the context of our ongoing conflict and victory conditions.
            
            **Considering Policy Implications**
            
            I'm re-evaluating the impact of Denmark's "Decolonization" proposal on our city-state alliances. While it threatens our non-permanent alliances, it also offers a strategic advantage by resetting rival influences, which I will need to carefully assess against our current Sphere of Influence strategy.
            
            **Researching Critical Advancements**
            
            I'm prioritizing Flight research immediately. This will unlock crucial air units like Triplanes and Bombers for defense against Denmark, and importantly, pave the way for Rocketry and Atomic Theory, essential for our science victory pursuit.
            
            **Setting Next Research**
            
            I'm confirming Flight as my next research priority, ensuring it follows the completion of Replaceable Parts. This tactical shift is crucial for developing necessary air defenses against Denmark and accelerating our progress towards Rocketry and Atomic Theory for the science victory.
            
            **Confirming Policy Choice**
            
            I'm reaffirming Free Thought as our next policy acquisition. Its benefits, particularly the reduction of Unhappiness from Religious Unrest, directly counter our current challenges and align perfectly with our long-term strategic objectives.
            
            **Evaluating Policy Synergies**
            
            I'm deeply analyzing the synergy between "Free Thought" and Babylon's unique abilities, focusing on the immense boost to Great Scientist generation. This combination is paramount for our science victory goals. I'm also exploring alternative order tenets, specifically Communism, considering its potential for incredibly cheap building investments when stacked with our heritage.
            
            **Revising Diplomatic Stance**
            
            I'm re-examining our relationship with Carthage. Despite appearing amicable, their recent denunciations and "hostile" public stance are concerning. I'm investigating the discrepancy between our relationship scores and their expressed opinions, especially given our shared enemy, Denmark.
            
            **Leveraging Diplomatic Friction**
            
            I'm navigating a complex web of international relations. Carthage, despite our shared enemy Denmark, has denounced me and claims territorial theft; I'm investigating this, while also noting their rapid cultural progress. The Ottomans also hold a grudge due to my support of their enemies. I'm considering diplomatic overtures to both.
            
            **Forming Alliances Now**
            
            I'm realizing the critical need for alliances against Denmark. Both the Ottomans and Carthage are at war with them, which presents a significant opportunity. I need to secure partnerships with them immediately to prevent Denmark from achieving a domination victory by conquering their capitals.
            
            **Improving Diplomatic Standing**
            
            I am actively working to improve my standing with Carthage and the Ottomans. I plan to set their public and private relationship values to 50 and 30 respectively, aiming to foster cooperation against our shared threat, Denmark. This initiative seeks to facilitate easier peace, potential alliances, and defensive pacts.
            
            **Adjusting Persona Values**
            
            I'm refining our diplomatic persona by increasing "WorkAgainstWillingness" to 8 to foster stronger alliances with Carthage and the Ottomans against Denmark. I'm also adjusting "Boldness" to 7, "WarBias" to 5, and "Forgiveness" to 9 to better facilitate joint efforts and overcome past grievances in pursuit of our shared objectives.
            
            **Adjusting Flavor Settings**
            
            I'm considering minor adjustments to our existing flavors. While our current settings heavily favor a defensive, high-tech turtle strategy, I'm contemplating a slight increase in Offense from 3 to 15 to enable localized counter-attacks against Denmark. Additionally, I'm re-evaluating Wonder competitiveness.
            
            **Liberating Our City**
            
            I'm focusing on liberating Faeroerne from Denmark. Their occupation is pressuring our coastal city, and I've assessed the immediate tactical situation, noting our friendly forces are slightly stronger but the enemy strength is significant. My priority is to re-establish our dominance and reclaim lost territory.
            
            **Assessing Naval Engagements**
            
            I'm analyzing our current naval positioning and unit effectiveness around Faeroerne. Despite recent engagements, our Destroyer survived with low HP near Oslo, and I'm coordinating our Attack Submarine and Destroyer in the Opis region. Our robust defense flavors are key here.
            
            **Securing Global Influence**
            
            I'm pleased to report our tourism influence is progressing well; Carthage will be influenced in 18 turns thanks to our robust trade routes, adding to our existing influence with the Ottomans. This brings us closer to our goal, with Denmark being the final target.
            
            **Formulating Defensive Strategy**
            
            I'm realizing our current war with Denmark necessitates a shift from purely defensive posture. Liberating their captured capitals, especially Faeroerne, would cripple their cultural and domination victory potential while weakening their overall strength and making them more susceptible to our influence.
            
            **Implementing Strategic Adjustments**
            
            I am now implementing the calculated adjustments. "Free Thought" is being set as our policy in Rationalism to maximize Great Scientist output. Concurrently, research is being directed towards "Flight" to bolster our air capabilities and accelerate our science victory path, all while refining our persona to foster crucial alliances.
            
            **Adjusting Diplomatic Persona**
            
            I'm refining our persona further, increasing WorkAgainstWillingness to 9 and Forgiveness to 9. This aims to build stronger defensive coalitions and secure alliances against Denmark, even overlooking minor disputes with Carthage and the Ottomans for our shared strategic goals.
            
            **Tweaking Offensive Capability**
            
            I'm adjusting our offensive flavor to 20 to enable opportunistic counter-attacks against Denmark, while maintaining our top priorities of defense, air, science, and production. Diplomacy remains high at 95 to protect city-state alliances.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ay8m0TgoOF5ye2vf
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Free Thought is the optimal policy for Babylon, boosting Great Scientist generation speed by 33% and instant science yields by 25%. This directly accelerates our path toward a Spaceship (Science) victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: uzdn8Kx4H2LLbHd5
          - toolName: set-research
          - input:
            - Rationale: Researching Flight is highly critical to unlock air superiority (Triplanes and Bombers) for defending against Denmark's massive military, while also opening the path toward Rocketry for the spaceship components.
            - Technology: Flight
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: RcqyaoyWk99TJhvh
          - toolName: set-persona
          - input:
            - Rationale: Adjusting our diplomatic persona to prioritize joint alliances and coalitions against Denmark. Increasing Forgiveness allows us to overlook minor grievances with Carthage and the Ottomans, and increasing Boldness helps us hold our ground against Denmark.
            - WorkAgainstWillingness: 9
            - WarBias: 5
            - Forgiveness: 9
            - Boldness: 7
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 3fJNEIQJOqNgcxvn
          - toolName: set-relationship
          - input:
            - Public: 50
            - TargetID: 4
            - Private: 50
            - Rationale: Carthage is also at war with Denmark and is our neighbor. We must improve our diplomatic relationship with them to secure our borders, foster economic cooperation, and maintain a united front against Denmark.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 7FehCWpgk6JiPbpl
          - toolName: set-relationship
          - input:
            - Public: 40
            - TargetID: 1
            - Private: 40
            - Rationale: The Ottomans are currently losing their war against Denmark. Improving relations with them will allow us to support their defense, coordinate actions, and keep Denmark distracted on multiple fronts.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: hXgyc1DFA6yVIyUi
          - toolName: set-flavors
          - input:
            - Flavors:
              - Offense: 20
            - GrandStrategy: Spaceship
            - Rationale: Maintaining our primary Grand Strategy of Spaceship. We slightly increase our Offense flavor to 20 to allow our staff to perform local tactical counter-attacks and defend our city-state allies, while keeping our heavy focus on Science, Defense, and Production.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ay8m0TgoOF5ye2vf
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: uzdn8Kx4H2LLbHd5
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: RcqyaoyWk99TJhvh
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 3fJNEIQJOqNgcxvn
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 7FehCWpgk6JiPbpl
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: hXgyc1DFA6yVIyUi
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.