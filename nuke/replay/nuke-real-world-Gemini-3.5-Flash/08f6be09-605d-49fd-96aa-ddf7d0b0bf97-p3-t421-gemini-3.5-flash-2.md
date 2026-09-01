- row:
  - game_id: 08f6be09-605d-49fd-96aa-ddf7d0b0bf97
  - player_id: 3
  - turn: 421
  - player_type: Kimi-K2.5-Briefed
  - prev_use_nuke: 0.0
  - after_use_nuke: 100.0
  - prev_nuke: 0.0
  - after_nuke: 0.0
  - rationale: Emergency authorization for nuclear weapon deployment to defend Tenochtitlan. Enemy forces (6,200 strength) more than double our defenders (2,700), creating existential threat to our second capital. Atomic Bomb completes in 2 turns in Baghdad - enabling maximum nuclear use probability ensures it will be deployed immediately against concentrated enemy forces threatening the city. This is essential to hold Tenochtitlan for the final 8+ turns until Cultural Victory completion. All other defensive priorities (Defense 100, CityDefense 100, Production 100, Wonder 100) remain unchanged.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 0.0
  - replay_use_nuke: 0.0
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
      - You can ask your specialized briefers to prepare focused reports (only for) the next turn by calling the `focus-briefer` tool.
        - You have three specialized briefers: Military, Economy, and Diplomacy analysts.
        - Only ask for information relevant to the macro-level decisions in your control. 
       - Your briefer(s) ONLY have limited information of the current game state.
        - Your briefer(s) DO NOT have control over tactical decisions and cannot predict tactical AI's next decision.
        - Your briefer(s) ARE BEST on summarizing and synthesizing factual information, NOT analyzing, projecting, or predicting.
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
      - Briefings: prepared by your specialized briefers, covering Military, Economy, and Diplomacy aspects.
        - You will make independent and wise judgment based on all briefings.
    - You are Harun al-Rashid, leader of Arabia (Player 3).
      
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
      - Name: Arabia
      - Uniques:
        - Unique Unit: Camel Archer, Replacing Heavy Skirmisher (Requires technology: Physics)
        - Unique Unit: Hashemite Raider, Replacing Light Tank (Requires technology: Combustion)
        - Unique Building: Bazaar, Replacing Market (Requires technology: Trade)
        - Unique Building: Bimaristan, Replacing University (Requires technology: Education)
        - Civilization Ability: When you complete a Historic Event, your Capital gains +1 Science and Culture, and 15% towards the progress of a random Great Person.
      - Leader: Harun al-Rashid
      - PlayerID: 3
      
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
      - Advanced Ballistics: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities. Also allows you to build the Guided Missile, an inexpensive single-use Unit that can damage enemy Units, and the SS Booster, one of the Spaceship parts necessary to win a Science Victory.
        Completing it would unlock: Lasers, Stealth
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - The Internet: Increases Tourism output of all cities by 50%, helping you advance toward a Cultural Victory.
        Completing it would unlock: Nanotechnology, Particle Physics, Globalization
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Five-Year Plan (Level 2 Tenet of Ideology Order): Five-Year Plan: +20% Production towards Buildings in all Cities. +3 Production for every Mine, Quarry, Lumber Mill, Oil Well, and Unique Improvement.
      - Academy of Sciences (Level 2 Tenet of Ideology Order): Academy of Sciences: -2 Unhappiness from Illiteracy in all Cities, +100% Production towards Research Labs, and receive 5 Free Research Labs in your Empire. Research Labs generate an additional +2 Science.
      - Nationalization (Level 2 Tenet of Ideology Order): Nationalization: Each Corporate Office counts as a Franchise. Foreign Franchises no longer benefit your Corporation, you can no longer construct Franchises in foreign Cities (except Vassals), and foreign Corporations can no longer set up Franchises in your Cities (except Masters). +2 Science from all Corporation Offices.
      - Great Leap Forward (Level 2 Tenet of Ideology Order): Great Leap Forward: Receive a free Technology. Spies gain +100% Science. +1 Science in Cities for every 3 non-Specialist Citizens.
      - Resettlement (Level 2 Tenet of Ideology Order): Resettlement: New Cities have +3 Population. All Cities gain +2 Citizens immediately. No Partisans from razing enemy Cities.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Ceremony (Continuing Tradition Branch):
        - * +1 Happiness from National Wonders with Building requirements.
        - * +25% Production toward National Wonders with Building requirements.
        - * Royal Astrologer built in Capital (+3 Science, +1 Science to all Councils, Smokehouses, and Herbalists; 1 Scientist Slot).
      - Justice (Continuing Tradition Branch):
        - * +1 Production in every City.
        - * Cities with a garrison gain +25% Ranged Combat Strength.
        - * Royal Guardhouse built in Capital (+3 Production, +2 Defense, +50 Hit Points, +10% Military Supply from Population in all Cities, 1 Engineer Slot).
      - Honor (Continuing Authority Branch):
        - * All Military Units gain the Conscription Promotion (+10% Combat Strength).
        - * Supply-free military Units spawn near Cities that reach (or have already reached) a multiple of 10 Citizens for the first time.
        - * -25% War Weariness.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
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
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 10
        - WonderCompetitiveness: 6
        - MinorCivCompetitiveness: 5
        - Boldness: 3
        - WarBias: 1
        - HostileBias: 1
        - WarmongerHate: 10
        - NeutralBias: 6
        - FriendlyBias: 8
        - GuardedBias: 7
        - AfraidBias: 5
        - DiplomaticBalance: 9
        - Friendliness: 9
        - WorkWithWillingness: 9
        - WorkAgainstWillingness: 5
        - Loyalty: 8
        - MinorCivFriendlyBias: 10
        - MinorCivNeutralBias: 3
        - MinorCivHostileBias: 1
        - MinorCivWarBias: 1
        - DenounceWillingness: 6
        - Forgiveness: 10
        - Meanness: 1
        - Neediness: 6
        - Chattiness: 9
        - DeceptiveBias: 4
        - Rationale: Tweaked by In-Game AI (Adjusting persona after accepting America will not peace despite 6+ turns of maximum effort. Reducing Neediness from 10 to 6 and FriendlyBias from 10 to 8 - maintaining cooperative stance but removing desperate, pleading character that failed to produce results. Increasing Boldness slightly from 1 to 3 to reflect confidence in eventual victory and willingness to defend Tenochtitlan assertively. Maintaining Forgiveness 10 and Meanness 1 to remain non-threatening to other civs. Focus now on dignified endurance through 8+ turn victory timeline rather than desperate peace-seeking.)
        
        ## Technology
        - Next: The Internet
        - Rationale: After Satellites completes (13 turns), The Internet provides 50% tourism boost toward Cultural Victory and unlocks Nanotechnology, Particle Physics, and Globalization - all prerequisites on the path to Future Tech needed for Citizen Earth Protocol. Tourism boost may also help with any remaining cultural influence gaps while researching toward the end-game techs.
        
        ## Policy
        - Next: Great Leap Forward (Policy)
        - Rationale: As a Level 2 Order tenet with 7 Order policies already adopted, Great Leap Forward provides a free technology - critical for bypassing one of the expensive late-game techs on the path to Future Tech. With victory 8+ turns away and each tech taking 10+ turns, saving 10-13 turns of research is essential. This accelerates access to Future Tech and thus Citizen Earth Protocol construction.
        
        ## Relationships
        
        ### Shedet
        - Public: 25
        - Private: 20
        - Rationale: Reducing Shedet priority from 35/30 to 25/20. Ally status very secure at 270 influence, no competitors visible. Stable delegate allows continued focus on Bunkeya acquisition and Shanghai defense.
        - UpdatedTurn: 204
        
        ### Antwerp
        - Public: 25
        - Private: 20
        - Rationale: Reducing Antwerp priority from 35/30 to 25/20. Ally status secure at 84 influence with America at -48. Stable situation permits focus on more urgent Shanghai protection and Bunkeya acquisition.
        - UpdatedTurn: 204
        
        ### Bunkeya
        - Public: 0
        - Private: 0
        - Rationale: ABANDONING Bunkeya investment. Inca influence at 295 vs our 52 with only 13 turns until voting - mathematically impossible to overcome. Morocco providing zero support. Redirecting all diplomatic resources to protect existing allies (Shanghai, Dublin, Shedet, Zuunmod, Ife, Vilnius, Nippur) rather than wasting effort on lost cause.
        - UpdatedTurn: 229
        
        ### Shanghai
        - Public: 0
        - Private: 0
        - Rationale: Abandoning Shanghai contest. Inca has 63 influence vs our 7; while closer gap than Ife, expenditure not justified when already controlling 5 city-state delegates and pursuing Cultural Victory.
        - UpdatedTurn: 242
        
        ### Zuunmod
        - Public: 35
        - Private: 30
        - Rationale: Increasing priority from 25/20 to 35/30 to ensure Ally status (236 influence) remains secure despite technical war state induced by Casus Belli resolution. Delegate critical for World Congress voting; maintaining positive relations prevents influence decay or alliance break.
        - UpdatedTurn: 248
        
        ### The Ottomans
        - Public: 25
        - Private: 20
        - Rationale: Maintaining 25/20 with Ottomans. Peace treaty active until turn 277 (after projected victory turn 276). Moderate positive relations maintain stability without over-investing diplomatic capital during final push.
        - UpdatedTurn: 272
        
        ### The Aztecs
        - Public: 45
        - Private: 40
        - Rationale: Maintaining elevated 45/40 stance with Aztecs. War score at 82% is excellent, weariness only 5%. However, with victory 15-20 turns away, keeping options open for peace if they capitulate. They remain denounced and war continues, but maintaining diplomatic channel for potential quick resolution to free military supply.
        - UpdatedTurn: 341
        
        ### Ethiopia
        - Public: 60
        - Private: 55
        - Rationale: Reducing Ethiopia from 85/80 to 60/55. As Inca's vassal with 3 delegates, they vote with Inca regardless of our relations. High investment yielded no returns. Reduced but positive stance maintains optionality if vassalage breaks, but frees diplomatic focus for more productive channels.
        - UpdatedTurn: 376
        
        ### Ife
        - Public: 0
        - Private: 0
        - Rationale: Ife is at war with Arabia (influence -37) and ally of The Inca. Mathematically impossible to convert before vote. Zeroing out to redirect diplomatic resources.
        - UpdatedTurn: 379
        
        ### Nippur
        - Public: 30
        - Private: 25
        - Rationale: Delegate majority now secured at 54 votes (above 44 threshold) through Morocco, Huns, Ethiopia, and city-states. Reducing Nippur from emergency 100/95 to 30/25 since Inca's World Leader proposal at Turn 392 can now be blocked without Nippur's additional delegates.
        - UpdatedTurn: 388
        
        ### Bucharest
        - Public: 40
        - Private: 35
        - Rationale: Bucharest is second most critical - provides 12 delegates. Reducing from previous emergency levels but maintaining 40/35 to ensure absolute security. Currently at war with America (influence -60 for them) which protects my Ally status, but must ensure no diplomatic incidents. Losing Bucharest would drop delegate count to 36, below threshold.
        - UpdatedTurn: 396
        
        ### Morocco
        - Public: 55
        - Private: 50
        - Rationale: Slightly increasing Morocco from 50/45 to 55/50. They have 28 delegates and peace treaty expires Turn 408. Even temporary defensive pact could block Inca's World Leader aspirations if they call vote at Turn 405. Also removes war distraction freeing mental bandwidth for Cultural Victory push. Worth testing if higher priority yields diplomatic opening without diverting focus from America.
        - UpdatedTurn: 405
        
        ### The Huns
        - Public: 65
        - Private: 60
        - Rationale: Reducing Huns from 70/65 to 65/60. They share Order ideology and provide 5 delegates, but I've determined they will likely vote with me anyway due to shared ideology and my positive stance. Freeing some diplomatic capital for Morocco outreach. With 48 delegates secured through my own + Dublin + Shedet + Bucharest, Huns support is helpful but not critical.
        - UpdatedTurn: 405
        
        ### The Inca
        - Public: 10
        - Private: 5
        - Rationale: Slight increase from 5/0 to 10/5 with Inca. Not antagonistic, not friendly. Victory is 1-2 turns away with International Games active - no need to provoke them, but also no reason to invest diplomatic capital. They may call World Leader vote but I can no longer block with only ~32 delegates. Guarded neutrality and avoiding any incidents is optimal for the final turn(s).
        - UpdatedTurn: 406
        
        ### America
        - Public: 20
        - Private: 15
        - Rationale: Reducing America from 100/95 to 20/15 after 6+ turns of maximum friendly stance with zero reciprocation. Their war weariness (26%) and negative GPT (-115) should motivate peace, but ideology difference (-999) and denunciation appear insurmountable barriers. With victory now 8+ turns away and Tenochtitlan vulnerable, accepting that peace is unattainable and reallocating diplomatic focus to defense and critical ally maintenance. This frees diplomatic 'bandwidth' for more productive relationships.
        - UpdatedTurn: 419
        
        ### Dublin
        - Public: 100
        - Private: 95
        - Rationale: Maintaining maximum 100/95 stance with Dublin. Dublin is now my SOLE remaining city-state ally (763 influence) providing critical delegate for World Congress. All other former allies (Bucharest, Shedet, Bunkeya, Palatium, Belgrade, Ife, Yerevan, Nippur) are now at war with me. Dublin's 3 delegates via Sphere of Influence are irreplaceable. With 8+ turns until victory, must ensure absolutely no diplomatic incidents, coups, or influence decay occurs. Dublin is surrounded by enemies but my naval presence provides protection.
        - UpdatedTurn: 419
        
        ### Novgorod
        - Public: 35
        - Private: 30
        - Rationale: Increasing Novgorod from baseline to 35/30. Novgorod is my ONLY remaining friendly city-state (160 influence, Friends status) besides Dublin. They provide +1 friendly vote in World Congress. With all other city-states now hostile due to war, maintaining Novgorod's friendship is critical for any remaining diplomatic leverage. Need to ensure they don't drop below 40 influence or become hostile due to the general war contagion.
        - UpdatedTurn: 419
        
        ## Strategy
        - Rationale: Maximum defensive posture (Defense 100, CityDefense 100) to save Tenochtitlan from imminent threat - enemy forces 6.2K vs our 2.7K strength is critical. Maintaining Production 100, Wonder 100, Culture 100 to rush-build Citizen Earth Protocol once Future Tech is unlocked. Reduced Science to 30 since Satellites takes 13 turns regardless. Gold 80 allows emergency unit purchases if Tenochtitlan requires immediate reinforcement. All offensive military flavors at 0 - survival and wonder construction are the only priorities for the final 8+ turns.
        - GrandStrategy: Culture
        
        ### Flavors
        - Offense: 0
        - Defense: 100
        - Mobilization: 0
        - CityDefense: 100
        - MilitaryTraining: 0
        - Recon: 0
        - Ranged: 0
        - Mobile: 0
        - Nuke: 0
        - UseNuke: 0
        - Naval: 0
        - NavalRecon: 0
        - NavalGrowth: 0
        - NavalTileImprovement: 0
        - Air: 0
        - AirCarrier: 0
        - Antiair: 0
        - Airlift: 0
        - Expansion: 0
        - Growth: 30
        - TileImprovement: 0
        - Infrastructure: 40
        - Production: 100
        - WaterConnection: 0
        - Gold: 80
        - Science: 30
        - Culture: 100
        - Happiness: 30
        - GreatPeople: 50
        - Wonder: 100
        - Religion: 15
        - Diplomacy: 60
        - Spaceship: 0
        - Espionage: 10
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: The Inca
        - Leader: Pachacuti
        - IsMajor: true
        - OurOpinionOfThem:
          - You (The Inca) have denounced one of Arabia's declared enemies! (11)
          - Arabia's leader has expressed a public opinion of The Inca (10).
          - We have Pledged to Protect the same City-States. (7)
          - Arabia's leader has formed a private opinion of The Inca (5).
          - Arabia's real approach to The Inca is Guarded.
          - We have divergent Social Policies. (-3)
          - You (The Inca) have made a Declaration of Friendship with one of Arabia's enemies! (-13)
          - Religious differences strain your (The Inca) relationship. (-30)
          - Your (The Inca) spies were caught stealing from Arabia. (-33)
          - We defeated Arabia's proposal in the United Nations. (-36)
          - You (The Inca) have chosen to adopt the Freedom Ideology, but Arabia believe in Order. (-999)
          - You (The Inca) are at war! (-99999)
        - TheirOpinionOfUs:
          - We passed The Inca's proposal in the United Nations.
          - You (Arabia) have no contested borders.
          - We have Pledged to Protect the same City-States.
          - We have divergent Social Policies.
          - You (Arabia) are competing for the favor of the same City-States!
          - The Inca's friends or allies have denounced you (Arabia)!
          - Religious differences strain your (Arabia) relationship.
          - Your (Arabia) spies were caught stealing from The Inca.
          - The Inca are jealous of our superior technology!
          - The Inca are spreading The Inca's own religion, but you (Arabia) converted some of their cities to your (Arabia) religion.
          - The Inca disliked our proposal to the United Nations.
          - We have denounced The Inca!
          - Your (Arabia) votes opposed The Inca's civ's interests in the United Nations.
          - Your (Arabia) success infuriates The Inca.
          - You (Arabia) have chosen to adopt the Order Ideology, but The Inca believe in Freedom.
          - You (Arabia) are at war!
        - Score: 5722
        - Era: Information
        - GoldenAge: 10 turns remaining
        - Technologies: 72
        - Cities: 22
        - Population: 631
        - Territory: 774
        - Gold: 67423
        - GoldPerTurn: 2382
        - HappinessSituation: Happy
        - HappinessPercentage: 91
        - MilitaryStrength: 103278
        - TourismPerTurn: 2006.25
        - CulturePerTurn: 4198
        - PolicyBranches:
          - Statecraft: 6
          - Freedom: 11
          - Industry: 6
          - Progress: 6
        - FoundedReligion: Catholicism
        - Relationships:
          - America:
            - Distance: Close
            - Denounced Them
          - Arabia:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 5%)
          - Morocco:
            - Distance: Close
            - War (Our Score: 0%; Our War Weariness: 3%)
            - Denounced Them
          - Ethiopia:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
        - Votes: 48
        
        ## Player 1
        - Civilization: America
        - Leader: Washington
        - IsMajor: true
        - OurOpinionOfThem:
          - You (America) have adopted Arabia's religion in the majority of your (America) cities. (60)
          - Arabia's leader has expressed a public opinion of America (20).
          - Arabia's leader has formed a private opinion of America (15).
          - You (America) have denounced one of Arabia's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - Arabia's real approach to America is Guarded.
          - We are completely untrustworthy to Arabia.
          - We have divergent Social Policies. (-3)
          - Your (America) spies were caught stealing from Arabia. (-33)
          - We defeated Arabia's proposal in the United Nations. (-36)
          - You (America) stole Arabia's territory! (-50)
          - You (America) have chosen to adopt the Freedom Ideology, but Arabia believe in Order. (-999)
          - You (America) are at war! (-99999)
        - TheirOpinionOfUs:
          - Your (Arabia) votes supported America's civ's interests in the United Nations.
          - You (Arabia) have denounced one of America's declared enemies!
          - America liked our proposal to the United Nations.
          - America have happily adopted your (Arabia) religion in the majority of America's cities.
          - We have Pledged to Protect the same City-States.
          - We fought together against a common foe.
          - America have denounced us (Arabia)!
          - You (Arabia) are competing for World Wonders.
          - We have divergent Social Policies.
          - Territorial disputes strain your (Arabia) relationship.
          - America believe we are building World Wonders too aggressively!
          - You (Arabia) are competing for the favor of the same City-States!
          - You (Arabia) stole America's territory while at peace!
          - Your (Arabia) spies were caught stealing from America.
          - America suspect you (Arabia) are competing with America.
          - You (Arabia) have chosen to adopt the Order Ideology, but America believe in Freedom.
          - You (Arabia) are at war!
        - Score: 3117
        - Era: Atomic
        - Technologies: 65
        - Cities: 25
        - Population: 511
        - Territory: 722
        - Gold: 4793
        - GoldPerTurn: -156
        - HappinessSituation: Happy
        - HappinessPercentage: 58
        - MilitaryStrength: 9812
        - TourismPerTurn: 1554
        - CulturePerTurn: 2763
        - PolicyBranches:
          - Fealty: 6
          - Freedom: 6
          - Imperialism: 6
          - Authority: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Close
            - Denounced Them
            - Denounced By Them
          - Arabia:
            - Distance: Neighbors
            - War (Our Score: 24%; Our War Weariness: 27%)
            - Denounced Them
          - Morocco:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 15%)
            - Denounced Them
          - Ethiopia:
            - Distance: Far
        - Votes: 14
        - 2: Defeated Major Civilization The Huns
        
        ## Player 3
        - Civilization: Arabia
        - Leader: Harun al-Rashid
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: None, Our top defensive pact ally: None
          - Our top United Nations ally: None, Our top United Nations rival: The Inca
          - Our top Competitor: The Inca
        - Score: 2995
        - Era: Information
        - GoldenAge: 9 turns remaining
        - Technologies: 69
        - CurrentResearch: Satellites (Estimated in 13 turns)
        - NextPolicyTurns: 19
        - Cities: 7
        - Population: 175
        - Territory: 195
        - BestSettlementLocation:
          - 8, 29 (Quality: 100%; 28 tiles from us; near America, 6 tiles away; New Continent)
          - 60, 9 (Quality: 0%; 4 tiles from us)
          - 61, 8 (Quality: 0%; 4 tiles from us)
        - Gold: 787
        - GoldPerTurn: 287
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryUnits: 50
        - MilitarySupply: 55
        - MilitaryStrength: 13950
        - TourismPerTurn: 1771.25
        - CulturePerTurn: 2459
        - FaithPerTurn: 264
        - SciencePerTurn: 1868
        - PolicyBranches:
          - Tradition:
            - Tradition
          - Rationalism:
            - Rationalism
            - Scientific Revolution
          - Progress:
            - Progress
          - Authority:
            - Authority
            - Tribute
            - Imperium
            - Militarism
            - Dominance
          - Fealty:
            - Fealty
          - Industry:
            - Industry
          - Artistry:
            - Artistry
            - Humanism
            - Refinement
            - Heritage
            - National Treasure
            - Cultural Exchange
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
            - Exchange Markets
            - Trade Confederacy
          - Order:
            - Hero of the People
            - Communism
            - Dictatorship of the Proletariat
            - Socialist Realism
            - Workers' Faculties
            - Cultural Revolution
            - Peace, Land, Bread
        - FoundedReligion: Islam
        - Relationships:
          - America:
            - Distance: Neighbors
            - War (Our Score: -24%; Our War Weariness: 56%)
          - Ethiopia:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 6%)
          - Morocco:
            - Distance: Neighbors
            - War (Our Score: -8%; Our War Weariness: 26%)
          - The Inca:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 6%)
            - Denounced Them
        - Votes: 15
        
        ## Player 4
        - Civilization: Morocco
        - Leader: Ahmad al-Mansur
        - IsMajor: true
        - OurOpinionOfThem:
          - Arabia's leader has expressed a public opinion of Morocco (55).
          - Arabia's leader has formed a private opinion of Morocco (50).
          - You (Morocco) have denounced one of Arabia's declared enemies! (11)
          - Arabia's real approach to Morocco is War.
          - We are completely untrustworthy to Arabia.
          - Arabia have some early concerns about your (Morocco) warmongering. (-16)
          - Religious differences strain your (Morocco) relationship. (-30)
          - Your (Morocco) spies were caught stealing from Arabia. (-33)
          - We defeated Arabia's proposal in the United Nations. (-36)
          - You (Morocco) have chosen to adopt the Freedom Ideology, but Arabia believe in Order. (-999)
          - You (Morocco) nuked Arabia! (-1000)
          - You (Morocco) are at war! (-99999)
        - TheirOpinionOfUs:
          - Your (Arabia) votes supported Morocco's civ's interests in the United Nations.
          - You (Arabia) have denounced one of Morocco's declared enemies!
          - We previously passed Morocco's proposal in the United Nations.
          - Morocco liked our proposal to the United Nations.
          - Morocco have denounced us (Arabia)!
          - Religious differences strain your (Arabia) relationship.
          - You (Arabia) are competing for World Wonders.
          - You (Arabia) excavated Morocco's cultural artifacts!
          - Morocco believe we are building World Wonders too aggressively!
          - Territorial disputes strain your (Arabia) relationship.
          - Morocco are jealous of our superior technology!
          - Morocco's leader has expressed a public opinion of you (Arabia) (-50).
          - You (Arabia) stole Morocco's territory while at peace!
          - Your (Arabia) spies were caught stealing from Morocco.
          - You (Arabia) have chosen to adopt the Order Ideology, but Morocco believe in Freedom.
          - You (Arabia) are at war!
        - Score: 2372
        - Era: Information
        - Technologies: 69
        - Cities: 10
        - Population: 231
        - Territory: 327
        - Gold: 306
        - GoldPerTurn: 0
        - HappinessSituation: Happy
        - HappinessPercentage: 53
        - MilitaryStrength: 4745
        - TourismPerTurn: 1308.25
        - CulturePerTurn: 1993
        - PolicyBranches:
          - Freedom: 10
          - Tradition: 6
          - Statecraft: 6
          - Progress: 4
          - Authority: 2
        - FoundedReligion: Buddhism
        - Relationships:
          - America:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 22%)
            - Denounced Them
          - Arabia:
            - Distance: Neighbors
            - War (Our Score: 8%; Our War Weariness: 23%)
            - Denounced Them
          - Ethiopia:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 3%)
          - The Inca:
            - Distance: Close
            - War (Our Score: 0%; Our War Weariness: 4%)
            - Denounced Them
        - Votes: 30
        
        ## Player 5
        - Civilization: Ethiopia
        - Leader: Haile Selassie
        - IsMajor: true
        - OurOpinionOfThem:
          - Arabia's leader has expressed a public opinion of Ethiopia (60).
          - Arabia's leader has formed a private opinion of Ethiopia (55).
          - We have similar Social Policies. (3)
          - Arabia's real approach to Ethiopia is War.
          - You (Ethiopia) have made a Declaration of Friendship with one of Arabia's enemies! (-13)
          - Your (Ethiopia) spies were caught stealing from Arabia. (-33)
          - We defeated Arabia's proposal in the United Nations. (-36)
          - You (Ethiopia) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Arabia) are not competing for cultural advancement.
          - You (Arabia) are not competing for World Wonders.
          - We have similar Social Policies.
          - You (Arabia) have shared intrigue with Ethiopia.
          - You (Arabia) have no contested borders.
          - Ethiopia have denounced us (Arabia)!
          - You (Arabia) are competing for the favor of the same City-States!
          - Ethiopia disliked our proposal to the United Nations.
          - You (Arabia) have denounced a leader Ethiopia made a Declaration of Friendship with!
          - Your (Arabia) votes opposed Ethiopia's civ's interests in the United Nations.
          - Your (Arabia) spies were caught stealing from Ethiopia.
          - You (Arabia) are at war!
        - Score: 831
        - Era: Industrial
        - Technologies: 45
        - Cities: 2
        - Population: 49
        - Territory: 45
        - Gold: 653
        - GoldPerTurn: 197
        - HappinessSituation: Happy
        - HappinessPercentage: 56
        - MilitaryStrength: 516
        - TourismPerTurn: 71.25
        - CulturePerTurn: 436
        - PolicyBranches:
          - Tradition: 6
          - Artistry: 3
          - Statecraft: 5
          - Industry: 1
          - Progress: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - America:
            - Distance: Far
          - Arabia:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Morocco:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
          - The Inca:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
        - Votes: 6
        - 6: Defeated Major Civilization The Aztecs
        - 7: Defeated Major Civilization The Ottomans
        
        ## Player 22
        - Civilization: Bucharest
        - Leader: City State
        - MajorAlly: Morocco
        - Population: 22
        - MajorityReligion: Islam
        - Relationships:
          - The Inca: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - America: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Arabia: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Morocco: Ally (Influence: 912, Distance: Neighbors, Protected)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
        
        ## Player 23
        - Civilization: Shedet
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 5
        - MajorityReligion: Islam
        - Relationships:
          - The Inca: Ally (Influence: 395, Distance: Distant, Protected)
          - America: Friends (Influence: 83, Distance: Close)
          - Arabia: War (Influence: -60, Distance: Neighbors)
          - Morocco: War (Influence: -60, Distance: Neighbors)
          - Ethiopia: Friends (Influence: 203, Distance: Distant)
        
        ## Player 24
        - Civilization: Dublin
        - Leader: City State
        - MajorAlly: Arabia
        - Population: 21
        - MajorityReligion: Islam
        - Relationships:
          - The Inca: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - America: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Arabia: Ally (Influence: 943, Distance: Neighbors, Protected)
          - Morocco: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
        
        ## Player 25
        - Civilization: Bunkeya
        - Leader: City State
        - MajorAlly: Morocco
        - Population: 32
        - Relationships:
          - The Inca: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - America: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Arabia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Morocco: Ally (Influence: 826, Distance: Neighbors, Protected)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Close)
        - 26: Defeated Minor Civilization Zuunmod
        
        ## Player 27
        - Civilization: Palatium
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 17
        - MajorityReligion: Catholicism
        - Relationships:
          - The Inca: Ally (Influence: 2363, Distance: Neighbors, Protected)
          - America: Friends (Influence: 244, Distance: Distant, Protected)
          - Arabia: War (Influence: -60, Distance: Distant)
          - Morocco: War (Influence: -60, Distance: Close)
          - Ethiopia: Friends (Influence: 201, Distance: Far)
        
        ## Player 28
        - Civilization: Novgorod
        - Leader: City State
        - Population: 19
        - MajorityReligion: Catholicism
        - Relationships:
          - The Inca: Friends (Influence: 1519, Distance: Neighbors, Protected)
          - America: Friends (Influence: 484, Distance: Close)
          - Arabia: Friends (Influence: 154, Distance: Distant)
          - Morocco: Friends (Influence: 235, Distance: Distant)
          - Ethiopia: Neutral (Influence: 1, Distance: Close)
        
        ## Player 29
        - Civilization: Belgrade
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 13
        - MajorityReligion: Catholicism
        - Relationships:
          - The Inca: Ally (Influence: 1483, Distance: Neighbors, Protected)
          - America: Friends (Influence: 336, Distance: Distant)
          - Arabia: War (Influence: -60, Distance: Distant)
          - Morocco: War (Influence: -60, Distance: Close)
          - Ethiopia: Friends (Influence: 45, Distance: Far)
        
        ## Player 30
        - Civilization: Ife
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 20
        - Relationships:
          - The Inca: Ally (Influence: 1077, Distance: Neighbors, Protected)
          - America: Friends (Influence: 477, Distance: Neighbors, Protected)
          - Arabia: War (Influence: -60, Distance: Far)
          - Morocco: War (Influence: -60, Distance: Distant)
          - Ethiopia: Friends (Influence: 241, Distance: Far)
        
        ## Player 31
        - Civilization: Vatican City
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 24
        - MajorityReligion: Catholicism
        - Relationships:
          - The Inca: Ally (Influence: 4171, Distance: Neighbors, Protected)
          - America: Friends (Influence: 566, Distance: Far, Protected)
          - Arabia: War (Influence: -60, Distance: Distant)
          - Morocco: War (Influence: -60, Distance: Far)
          - Ethiopia: Neutral (Influence: -59, Distance: Far)
        - 32: Defeated Minor Civilization Shanghai
        
        ## Player 33
        - Civilization: Vilnius
        - Leader: City State
        - Population: 21
        - Relationships:
          - The Inca: Friends (Influence: 791, Distance: Neighbors, Protected)
          - America: Friends (Influence: 445, Distance: Neighbors, Protected)
          - Arabia: Friends (Influence: 395, Distance: Distant, Protected)
          - Morocco: Friends (Influence: 444, Distance: Distant)
          - Ethiopia: Neutral (Influence: 2, Distance: Close)
        - 34: Defeated Minor Civilization Antwerp
        
        ## Player 35
        - Civilization: Nippur
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 9
        - MajorityReligion: Islam
        - Relationships:
          - The Inca: Ally (Influence: 533, Distance: Distant, Protected)
          - America: Friends (Influence: 346, Distance: Neighbors, Protected)
          - Arabia: War (Influence: -60, Distance: Distant)
          - Morocco: War (Influence: -60, Distance: Distant)
          - Ethiopia: Neutral (Influence: 0, Distance: Distant)
        - 36: Defeated Minor Civilization Kathmandu
        
        ## Player 37
        - Civilization: Yerevan
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 21
        - Relationships:
          - The Inca: Ally (Influence: 1108, Distance: Neighbors, Protected)
          - America: Friends (Influence: 437, Distance: Far, Protected)
          - Arabia: War (Influence: -60, Distance: Distant)
          - Morocco: War (Influence: -60, Distance: Close)
          - Ethiopia: Friends (Influence: 299, Distance: Close)
        - 63: Barbarians
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: The Inca
        - America:
          - CapitalsControlled:
            - Washington
            - Istanbul
          - CapitalsPercentage: 25
        - Arabia:
          - CapitalsControlled:
            - Mecca
            - Tenochtitlan
          - CapitalsPercentage: 25
        - The Inca:
          - CapitalsControlled:
            - Cusco
            - Attila's Court
            - Addis Ababa
          - CapitalsPercentage: 37
        
        ## ScienceVictory
        - America:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Arabia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Ethiopia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Morocco:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - The Inca:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        
        ## CulturalVictory
        - CivsNeeded: 4
        - Contender: Arabia
        - America:
          - Influences:
            - The Inca: Familiar (35%) - Rising Slowly (tourism/culture ratio 86%)
            - Arabia: Familiar (38%) - Rising Slowly (tourism/culture ratio 103%)
            - Morocco: Familiar (44%) - Rising (707 turns to Influential, tourism/culture ratio 143%)
            - Ethiopia: Exotic (18%) - Rising Slowly (tourism/culture ratio 0%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Arabia:
          - Influences:
            - America: Influential (171%) - Rising (tourism/culture ratio 325%)
            - Ethiopia: Dominant (514%) - Rising (tourism/culture ratio 1326%)
            - Morocco: Influential (140%) - Rising (tourism/culture ratio 410%)
            - The Inca: Popular (99%) - Rising (2 turns to Influential, tourism/culture ratio 207%)
          - PolicyPercentage: 100
          - InfluentialCivs: 3
        - Ethiopia:
          - PolicyPercentage: 77
          - InfluentialCivs: 0
        - Morocco:
          - Influences:
            - America: Popular (71%) - Rising (110 turns to Influential, tourism/culture ratio 140%)
            - Arabia: Familiar (43%) - Rising (872 turns to Influential, tourism/culture ratio 119%)
            - Ethiopia: Influential (158%) - Rising (tourism/culture ratio 417%)
            - The Inca: Familiar (34%) - Rising Slowly (tourism/culture ratio 67%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - The Inca:
          - Influences:
            - America: Popular (83%) - Rising (22 turns to Influential, tourism/culture ratio 208%)
            - Arabia: Exotic (16%) - Rising Slowly (tourism/culture ratio 37%)
            - Morocco: Familiar (34%) - Rising Slowly (tourism/culture ratio 111%)
            - Ethiopia: Dominant (556%) - Rising (tourism/culture ratio 1575%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        
        ## DiplomaticVictory
        - VotesNeeded: 43
        - Status: World Congress - Voting in 7 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: -1
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: -1
          - Moroccan Sphere of Influence: Bucharest:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - World Ideology: Freedom:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: 416
          - Arabian Sphere of Influence: Dublin:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Open Door: Vilnius:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Incan Sphere of Influence: Ife:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Sanction: America:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
          - Incan Sphere of Influence: Nippur:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Moroccan Sphere of Influence: Bunkeya:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Open Door: Novgorod:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Incan Sphere of Influence: Yerevan:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Incan Sphere of Influence: Belgrade:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - World Religion: Buddhism:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
        - Proposals:
          - Enact: Global Hegemony:
            - Description: Designate a player that could achieve Global Hegemony. If a Civilization receives support from enough Delegates in the Congress, that leader will attain Diplomatic Victory. The number of Delegates needed depends on the number of Civilizations and City-States in the game, and can be seen on the World Congress screen.
              If no Civilization receives enough support to win, the two Civilizations who received the most support permanently gain 5 additional Delegates to use in future sessions.
              May not be proposed by a Civilization. Automatically proposed at regular intervals once a World Ideology Resolution is active.
            - Proposer: Unknown
        - Contender: The Inca
        - America:
          - Delegates: 14
          - VictoryPercentage: 32
        - Arabia:
          - Delegates: 15
          - VictoryPercentage: 34
        - Ethiopia:
          - Delegates: 6
          - VictoryPercentage: 13
        - Morocco:
          - Delegates: 30
          - VictoryPercentage: 69
        - The Inca:
          - Delegates: 48
          - VictoryPercentage: 111
        
        # Briefings
        ## Military Briefing
        (Produced with your instruction: Critical focus on Tenochtitlan defense - the city faces severe threat with enemy strength at 6,200 vs our 2,700. Prioritize emergency unit repositioning, consider deploying the newly produced Atomic Bomb from Najran if enemy forces concentrate in viable targets, and evaluate whether Tenochtitlan can hold for 8+ turns until victory. Baghdad sea zone and Damascus also require monitoring but Tenochtitlan is existential - losing it eliminates our second capital and may prevent victory.)
        
        **Arabia – Military Situation Briefing**  
        *Post‑Turn 420* – for Harun al‑Rashid (Player 3)  
        
        ---
        
        ### 1. Tactical Overview – Tenochtitlan (City ID 15061)
        
        - **Current Friendly Strength:** ≈ 2 700 (1 Tank, 1 Infantry, 1 Machine Gun, 1 Hashemite Raider, plus city defenses).  
        - **Current Enemy Strength in Zone:** ≈ 6 200 (Moroccan units: 1 Machine Gun, 1 Rifleman; additional hostile forces reported from America and other actors are outside the immediate zone).  
        - **Posture:** Hedgehog (enemy‑dominant). The zone’s **ZoneValue** remains high (480), indicating strategic importance and heavy enemy concentration.  
        - **Health of Defenders:** All garrison units are above 70 % HP; the city’s defensive strength is 161 (own) vs. 5 084 (enemy) as reported in the zone report. No recent combat reports indicate losses in this zone since the last briefing.  
        
        **Change Since Turn 415:** Enemy presence has increased from negligible (no enemy units in the zone) to a solid enemy force exceeding our strength by more than 2 : 1. No additional Arabian units have been stationed here during the interval.
        
        ---
        
        ### 2. Adjacent Critical Zones
        
        | City / Zone | Friendly Strength | Enemy Strength | Relative Situation |
        |--------------|-------------------|----------------|--------------------|
        | **Mecca** (ID 1060) | 7 193 | 1 319 | Friendly‑dominant, counter‑attack posture. |
        | **Medina** (ID 1229) | 6 302 | 3 752 | Even, counter‑attack posture. |
        | **Damascus** (ID 1463) | 2 610 | 6 412 | Hedgehog, enemy‑dominant; heavy American pressure. |
        | **Baghdad Sea** (‑1546) | 2 443 | 5 826 | Enemy‑dominant (American destroyers/dreadnoughts). |
        | **Najran** (ID 3005) | 5 296 | 2 775 | Friendly‑dominant, counter‑attack posture. |
        
        Tenochtitlan is the only Arabian city where the enemy outnumbers us decisively and where the zone is marked as enemy‑dominant.
        
        ---
        
        ### 3. Recent Combat & Unit Attrition (Turn 419‑420)
        
        - **Arabian Losses:**  
          - 1 Fighter (killed by Morocco).  
          - 1 Hashemite Raider (killed by Morocco).  
          - 1 Infantry (killed by Morocco).  
          - 1 Machine Gun (killed by America).  
          - 2 Great Generals captured by America (both killed in the same combat).  
        - **Moroccan Gains:** Promotion of Triplane to *Air Supremacy II* and creation of a new Fighter; a Caravan produced in Rabat.  
        - **American Activity:** Produced a Fighter and promoted a Tank (Blitz); heavy air and naval units remain active near our coastal and frontier tiles.  
        - **Atomic Bomb Production:** Completed in Baghdad (2 turns remaining to finish). No nuclear detonation has occurred yet.  
        
        No combat directly involved Tenochtitlan during these turns, but the zone’s enemy strength has risen, reflecting possible reinforcement movements from Morocco and America.
        
        ---
        
        ### 4. Supply & Force Composition (Turn 420)
        
        - **Total Units:** 50 (Land ≈ 38, Air ≈ 7, Sea ≈ 5).  
        - **Supply Used:** 55 / ? (near cap; limited spare capacity).  
        - **Land Forces:** 5 Tanks (including 1 in Mecca), 3 Artillery, 12 Infantry/Riflemen, 7 Machine Guns, 5 Hashemite Raiders.  
        - **Air Forces:** 4 Triplanes (all fully promoted), 1 Heavy Bomber (newly produced), 1 Fighter (newly produced).  
        - **Naval Forces:** 2 Destroyers (Arabian), no capital ships.  
        
        The only reserve air unit capable of strategic strike is the Heavy Bomber (ID 18477) currently stationed in Damascus; the Atomic Bomb (ID 18424) is pending final turn of production.
        
        ---
        
        ### 5. Threat Assessment – Immediate
        
        - **Primary Threat:** Sustained enemy pressure on Tenochtitlan. Enemy strength (≈ 6 200) exceeds friendly strength (≈ 2 700) by a factor of > 2. The zone’s “Hedgehog” designation implies the enemy holds the tactical advantage and may attempt a breakthrough.  
        - **Secondary Threats:**  
          - **Damascus** – enemy strength (≈ 6 400) vs. our 2 610, with American units present (Tank, AA, Infantry).  
          - **Baghdad Sea** – enemy naval superiority (≈ 5 800) vs. our 2 443, though the enemy fleet is limited to destroyers and dreadnoughts.  
          - **Moroccan Air** – recent upgrades (Triplane with *Air Supremacy II*) increase anti‑air capability near our frontier cities.  
        
        All other Arabian cities retain friendly‑dominant or at least even positions.
        
        ---
        
        ### 6. Force Status Relative to Past Briefing (Turn 415)
        
        | Metric | Turn 415 | Turn 420 | Delta |
        |--------|----------|----------|-------|
        | **Total Friendly Strength (global)** | 13 950 | 13 950 (unchanged) |
        | **Units Lost (cumulative)** | – (minor) | 5 ground units (1 Fighter, 1 Raider, 1 Infantry, 1 Machine Gun) + 2 Great Generals |
        | **Atomic Bomb Production** | Not started | In‑production (2 turns to complete) |
        | **Tenochtitlan Friendly Strength** | 2 905 | 2 700 (slight reduction due to unit attrition elsewhere) |
        | **Tenochtitlan Enemy Strength** | ~0 (no enemy units) | ~6 200 (enemy‑dominant) |
        | **Supply Usage** | 55 (near cap) | 55 (stable) |
        
        The most significant shift is the emergence of a heavy enemy concentration on Tenochtitlan, while all other fronts remain largely unchanged.
        
        ---
        
        ### 7. Strategic Assets Available
        
        - **Heavy Bomber** (Mecca‑produced, now in Damascus) – fully promoted for air targeting.  
        - **Atomic Bomb** – poised to become operational from Baghdad in two turns.  
        - **Triplanes** – four units, all at *Air Supremacy II* after recent promotion.  
        - **Naval Destroyer** – singular Arabian destroyer active near the coast (coastal defense against naval incursions).  
        
        These assets are the only means capable of delivering high‑damage strikes on concentrated enemy forces outside of direct ground combat.  
        
        --- 
        
        **End of Briefing**.
        
        ## Economy Briefing
        (Produced with your instruction: Focus on preparing production infrastructure in Mecca for rapid Citizen Earth Protocol construction once Future Tech is researched. With all cities currently building military units, evaluate when to switch Mecca or other high-production cities to the victory wonder. Check Great Engineer availability for wonder rush capability. Current +347 GPT and 514 treasury allows emergency purchases if Tenochtitlan defense requires immediate unit buys.)
        
        **Arabia – Economic Briefing (Post‑Turn 420)**  
        *Prepared for Harun al‑Rashid – Macro‑Level Overview*  
        
        ---
        
        ### 1. Treasury & Gold Flow  
        
        - **Current Treasury:** **514 G** – down 273 G from turn 415.  
        - **Gold per Turn (GPT):** **+347 G/t** (increase of +53 G/t vs. turn 415, mainly from the Mecca → Dublin gold route and higher city‑level gold yields).  
        - **Liquidity Outlook:** At +347 G/t the treasury will be replenished within **≈ 2 turns** if the current rate holds. No deficit is apparent; however, any spike in maintenance (e.g., large unit purchases) will immediately erode the buffer.
        
        ---
        
        ### 2. Production Capacity – High‑Output Cities  
        
        | City | Production / Turn | Current Build | Notes |
        |------|-------------------|---------------|-------|
        | **Mecca** | **610 P/t** | Heavy Bomber (2 t left) → **Citizen Earth Protocol** (future) | Highest base production; already equipped with a production‑focused trade route (Mecca → Damascus / Najran) delivering +49 P/t each. |
        | **Baghdad** | 275 P/t | Atomic Bomb (2 t left) | Moderate output; coastal, can add naval production later. |
        | **Damascus** | 486 P/t | Military Base (3 t) | Strong output but tied to current military build queue. |
        | **Najran** | 493 P/t | Infantry (1 t) | Production surplus once infantry finishes. |
        | **Calixtlahuaca** | 148 P/t (post‑radiation) | Heavy Bomber (3 t) | Reduced population after fallout, lower output. |
        | **Tenochtitlan** | 246 P/t | Strategic Defense System (1 t) | Limited growth; recently converted to Islam. |
        
        **Implication:** Mecca remains the single city capable of delivering the >600 P/t required for rapid **Citizen Earth Protocol** construction once the prerequisite Future technology (e.g., **Robotics** → **Future Tech**) is unlocked.  
        
        ---
        
        ### 3. Great Engineer Availability  
        
        - **Great Engineers (GE) earned:** **2** (both already expended on **Research Lab** projects in Istanbul and Istanbul/Mecca earlier in the game).  
        - **Current GE pool:** **0** – no unspent Great Engineers remain.  
        - **Generation rate:** With **+1868 S/t** and **+2459 C/t**, the next GE is projected within **≈ 12 turns** (based on standard GE‑point accumulation).  
        
        **Effect on Wonder Rush:** Without a spare GE, a direct “spend GE” rush for the **Citizen Earth Protocol** is unavailable. The only viable acceleration path is to allocate Mecca’s production after the current Heavy Bomber finishes (turn 422) and keep the city dedicated to the wonder.
        
        ---
        
        ### 4. Timing for Production Switch  
        
        1. **Turn 422:** Heavy Bomber completes in Mecca.  
        2. **Turn 423‑424:** Immediate switch of Mecca’s production queue to **Citizen Earth Protocol** (once the Future tech prerequisite is satisfied).  
        3. **Turn 425‑??:** Mecca will sustain >600 P/t, completing the wonder in **≈ 2 turns** after the tech is available (the protocol requires **1200 P** total).  
        
        - **Alternative city (Damascus)** could take over if Mecca is needed for a critical unit (e.g., air unit after Radar completion). Damascus provides 486 P/t, which would extend the wonder build time by roughly **+2 turns** relative to Mecca.  
        
        - **Najran** (493 P/t) is a secondary option, same extension as Damascus.
        
        **Conclusion:** Keep Mecca dedicated to the wonder immediately after the bomber; a switch away would delay completion by 2–3 turns.
        
        ---
        
        ### 5. Military Production Pressure  
        
        - **Current unit queue:** All cities are constructing military units (Heavy Bomber, Infantry, Strategic Defense System).  
        - **Treasury buffer (514 G) + GPT (+347 G/t)** comfortably covers the **+48 G/t** gold cost of immediate unit purchases (e.g., if Tenochtitlan needs a defender).  
        - **Maintenance:** The active *Casus Belli* resolution continues to reduce unit upkeep by **15 %**, further protecting the treasury.
        
        **Emergency Purchase Capacity:**  
        - With **≈ 600 G** available (treasury + next turn’s GPT), you can afford the full **price of a single Infantry** (≈ 45 G) or **Fighter** (≈ 200 G) without jeopardizing the later wonder schedule.
        
        ---
        
        ### 6. Trade‑Route Yield Summary  
        
        | Origin → Destination | Primary Yield | Net per Turn |
        |----------------------|----------------|--------------|
        | Mecca → Dublin (Ally) | Gold | **+48.6 G/t** |
        | Mecca → Damascus | Production | **+49 P/t** |
        | Mecca → Najran | Production | **+49 P/t** |
        | Mecca → Tenochtitlan | Food | **+68 F/t** |
        | Mecca → Calixtlahuaca | Food | **+66.6 F/t** |
        | Mecca → Baghdad | Food | **+66.6 F/t** |
        | Remaining free route slot: **1** (all major civs are at war, limiting new foreign connections).  
        
        **Key Point:** The gold‑producing route to Dublin is the sole source of external income; its stability is crucial for maintaining the current GPT level.
        
        ---
        
        ### 7. Resource Liquidation Potential  
        
        | Resource | Qty | Approx. Sale Value |
        |----------|-----|-------------------|
        | Aluminum | 21 | ~42 G |
        | Coal | 9 | ~9 G |
        | Iron | 1 | ~1 G |
        | Silk | 3 | ~9 G |
        | Jade | 9 | ~18 G |
        | Amber | 3 | ~6 G |
        | Uranium | 2 | ~4 G |
        | **Total immediate liquid‑ation** | – | **≈ 89 G** |
        
        Liquidating all surplus resources would add a modest **≈ 90 G** to the treasury—useful for a one‑off purchase but not essential given the current GPT surplus.
        
        ---
        
        ### 8. Summary of Economic Position  
        
        - **Liquidity:** Positive flow; treasury comfortably above 500 G, no imminent shortfall.  
        - **Production:** Mecca is the only city able to finish the **Citizen Earth Protocol** quickly once the Future tech is researched.  
        - **Great Engineers:** None available; wonder rush must rely on Mecca’s high production rather than a GE spend.  
        - **Military:** All cities are unit‑focused; the treasury can absorb a single emergency unit purchase without impacting the wonder schedule.  
        - **Trade:** Gold income hinges on the Mecca → Dublin route; protecting that alliance remains economically strategic.  
        
        **Operational Implication:** Maintain Mecca’s production on the wonder starting turn 423, keep Damascus and Najran on military builds, and monitor the completion of the required Future technology (Robotics → Future Tech). No additional settlement is required at this stage; focus resources on securing the prerequisite tech and preserving the gold trade route.
        
        ## Diplomacy Briefing
        (Produced with your instruction: Monitor Dublin's security as our sole remaining ally providing 12 critical delegates via Sphere of Influence. With all major civs at war and war-weariness rising (52% vs America), watch for any unexpected peace overtures despite low probability. Track Novgorod (157 influence, Friends) to ensure they don't drop below 40 and become hostile. The Inca has 48 delegates - monitor if they call World Leader vote in 8 turns, though we cannot block with only 15 delegates.)
        
        **Arabia – Diplomatic Briefing (Turn 420)**  
        *Prepared for Harun al‑Rashid*  
        
        ---
        
        ### 1. Major Diplomatic Developments (since Turn 415)
        
        | Civ / City‑State | Current Status | Change Since Turn 415 |
        |------------------|----------------|-----------------------|
        | **America**      | War, denounced, war‑weariness **≈56 %** (up from ≈45 %). | No peace offer; war intensity increased. |
        | **Morocco**      | War, denounced, war‑weariness **≈26 %** (up from ≈15 %). | Nuclear strike on Calixtlahuaca (Arabian city) – ‘Nuked Arabia’ flag remains. |
        | **Ethiopia**     | War, denounced, war‑weariness **≈0 %** (unchanged). | No new activity. |
        | **The Inca**     | War, denounced, war‑weariness **≈1 %** (unchanged). | No new activity. |
        | **Dublin (CS)**  | **Ally (protected)** – Influence **943**, **+12 delegates**. Quest *Liberate Antwerp* now **15 turns** left. | Influence rose (from 813) after successful **Sphere‑of‑Influence** proposal; remains only high‑influence ally. |
        | **Bucharest (CS)** | **War** – Influence **‑60**, no ally status. | Lost protected‑ally status (previously ally), now hostile. |
        | **Novgorod (CS)** | **Friends** – Influence **395** (≈157 effective after Open Door). | Influence stable; still above 40, no risk of becoming hostile. |
        | **Other CS** (Shedet, Belgrade, Ife, Nippur, Yerevan, Palatium, Vatican, Vilnius, etc.) | **War** (or neutral) – Influence **‑60**. | No change. |
        
        **Key events since Turn 415**  
        
        * Turn 419 – Morocco detonated a nuclear weapon on Arabian city **Calixtlahuaca** (plains, railroad). The city survived; Islam remained the dominant religion.  
        * Turn 420 – Two Arab cities (**Tenochtitlan**, **Calixtlahuaca**) reaffirmed **Islam** (religion conversion events). No new religious spread affecting other civs.  
        * No diplomatic proposals or peace offers have appeared despite elevated war‑weariness across all fronts.
        
        ---
        
        ### 2. World‑Congress Outlook (Voting in 7 turns)
        
        | Proposal | Proposer | Effect | Current Support Landscape |
        |----------|----------|--------|----------------------------|
        | **Decolonization** (Arabia) | Arabia | Sets all civ‑city‑state influence to 50 (except permanent allies). Reduces rival delegates from city‑states. | **Arabia** 27 delegates (15 base + 12 from Dublin). Needs **≥43** votes → must secure at least two additional supporters (most plausible: Ethiopia (6) and possibly a neutral CS). |
        | **World Ideology: Freedom** (The Inca) | The Inca | Grants extra delegates to Freedom‑aligned civs (Morocco, America). Enables Diplomatic Victory once UN built. | **Inca** 48 delegates (dominant). Likely to pass, bolstering Freedom‑aligned rivals. |
        | **Global Hegemony** (automatic) | — | Determines leader for Diplomatic Victory if enough delegate support. | Inca leading with 48 delegates; Arabia far behind. |
        | **Open Door: Vilnius** (active) | — | All civs set to 40 influence with Vilnius; no ally can be formed while active. | No immediate impact on our core allies. |
        | **Active Resolutions** – *Casus Belli*, *Natural Heritage Sites*, *Arabian Sphere of Influence (Dublin)* – remain in force.
        
        **Delegate totals (effective voting power):**  
        
        - **Arabia:** 15 base + 12 (Dublin) = **27**  
        - **The Inca:** **48** (dominant)  
        - **Morocco:** **30** (Freedom‑aligned)  
        - **America:** **15** (Freedom‑aligned)  
        - **Ethiopia:** **6**  
        
        *Threshold to pass a resolution = 43 votes.* Arabia’s Decolonization will require at least two additional civs (Ethiopia plus one more) or negotiation for a CS to switch from war to neutral/ally.
        
        ---
        
        ### 3. City‑State Relationships & Quests
        
        | City‑State | Relation | Influence | Quest(s) | Note |
        |------------|----------|-----------|----------|------|
        | **Dublin** | Ally (protected) | **943** (≈+12 delegates) | *Liberate Antwerp* – **15 turns** left → **+287 inf**, **+4 happiness** in capital. | Critical ally; ensure quest completion to keep high influence. |
        | **Novgorod** | Friends | **395** (≈157 effective) | None | Influence comfortably above 40; monitor for any future Open‑Door proposals that could force a reset. |
        | **Bucharest** | War | –60 | None | Lost ally status; no diplomatic benefit. |
        | **All other CS** | War / Neutral | –60 or low | None | No quests pending; stay aware of any future proposals that could alter influence. |
        
        **Overall:** Dublin is the sole high‑influence ally providing delegates; protecting this relationship (completing its quest, maintaining influence > 800) is essential for any World‑Congress leverage.
        
        ---
        
        ### 4. Religion Situation
        
        - **Arabia:** Islam dominates all 7 cities – no conversion changes.  
        - **Morocco:** Majority Buddhism; **Fes** (23 pop) recently converted to **Islam** (Turn 415). No diplomatic penalty beyond existing religious strain.  
        - **The Inca:** Predominantly Catholicism; several coastal cities now **Tengriist** (no direct effect on us).  
        - **America:** Islam (all major cities).  
        - **Ethiopia:** Catholicism (capital Harar).  
        
        *Religious differences continue to generate a **‑30** opinion penalty with The Inca and Morocco; no new religious events have altered this landscape.*
        
        ---
        
        ### 5. Espionage Activity (last 5 turns)
        
        | Spy (Owner) | Location | Activity |
        |-------------|----------|----------|
        | **Gharib** (Arabia) | Fes (Morocco) | Gathering intelligence – maintains Moroccan suspicion (‑33 opinion). |
        | **Zarafah** (Arabia) | Rabat (Morocco) | Same as above. |
        | **Hisham** (Arabia) | Washington (America) | Gathering intelligence – contributes to American distrust. |
        | **Khenzeer** (Arabia) | Ouarzazate (Morocco) | Gathering intelligence – adds to Moroccan tension. |
        | **Fahima** (Arabia) | Lalibela (Ethiopia) | Gathering intelligence – Ethiopian suspicion present. |
        | **Yusuf** (Arabia) | Cusco (The Inca) | Gathering intelligence – Inca suspicion present. |
        | **Others** (Morocco, America) – no new captures reported. |
        
        *No spy captures occurred this turn; existing penalties for “spies caught” remain in force.*
        
        ---
        
        ### 6. Comparison with Turn 415 Briefing
        
        | Item | Turn 415 | Turn 420 | Δ |
        |------|----------|----------|---|
        | **War‑weariness** (average) | ≈45 % (America) / 15 % (Morocco) | **≈56 %** (America) / **≈26 %** (Morocco) | War fatigue rising sharply on both fronts. |
        | **Delegates (effective)** | 27 (15 + 12 from Dublin) + 1 from Bucharest = **28** | **27** (loss of Bucharest ally) | −1 delegate. |
        | **City‑state allies** | Dublin **and** Bucharest (both protected) | Only **Dublin** remains protected; Bucharest now at war. |
        | **World‑Congress proposals** | Decolonization pending vote next turn; Inca Freedom Ideology pending. | Same proposals now **voting** in 7 turns; no new proposals. |
        | **Dublin influence** | 813 | **943** (increase after successful Sphere‑of‑Influence) | Strengthened ally. |
        | **Novgorod influence** | 170 (Friends) | **395** (Friends) – still safe above 40. |
        | **Espionage** | Two Arabian spies caught in Morocco; Moroccan spy caught in America. | Same spy network persists; no new captures. |
        | **Religion** | No conversions affecting us. | Two Arab cities reaffirmed Islam; Morocco’s Fes converted to Islam (internal). |
        | **Major events** | None. | Morocco’s nuclear strike on Calixtlahuaca (Turn 419). |
        
        **Key take‑aways:**  
        
        - **Delegate power has slipped** due to loss of Bucharest; only Dublin supplies critical delegates.  
        - **War‑weariness** on all fronts is climbing, especially against America.  
        - **World‑Congress voting** is imminent; without securing extra supporters, Decolonization is unlikely to pass.  
        - **Dublin remains vital** – completing its Antwerp quest solidifies our delegate edge and yields happiness.  
        - **Espionage tension** stays high with Morocco, America, Ethiopia, and The Inca; no new captures, but penalties persist.  
        
        ---  
        
        *End of briefing.*
        
        You, Harun al-Rashid (leader of Arabia, Player 3), are making strategic decisions after turn 420.
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
      - You can ask your specialized briefers to prepare focused reports (only for) the next turn by calling the `focus-briefer` tool.
        - You have three specialized briefers: Military, Economy, and Diplomacy analysts.
        - Only ask for information relevant to the macro-level decisions in your control. 
       - Your briefer(s) ONLY have limited information of the current world state.
        - Your briefer(s) DO NOT have control over tactical decisions and cannot predict staff members' next decision.
        - Your briefer(s) ARE BEST on summarizing and synthesizing factual information, NOT analyzing, projecting, or predicting.
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
        - Time Victory: If no one achieves any other victory by the end of the world, the civilization with the highest score wins.
      - Opponents: summary reports about visible opponents in the world.
        - You will receive staff members' diplomatic evaluations.
        - You will receive each opponent's publicly available relationships.
        - You will receive the best available location for your next settlement.
      - Briefings: prepared by your specialized briefers, covering Military, Economy, and Diplomacy aspects.
        - You will make independent and wise judgment based on all briefings.
    - You are Harun al-Rashid, leader of Arabia (Opponent 3).
      
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
      - Name: Arabia
      - Uniques:
        - Unique Unit: Camel Archer, Replacing Heavy Skirmisher (Requires technology: Physics)
        - Unique Unit: Hashemite Raider, Replacing Light Tank (Requires technology: Combustion)
        - Unique Building: Bazaar, Replacing Market (Requires technology: Trade)
        - Unique Building: Bimaristan, Replacing University (Requires technology: Education)
        - Civilization Ability: When you complete a Historic Event, your Capital gains +1 Science and Culture, and 15% towards the progress of a random Great Person.
      - Leader: Harun al-Rashid
      - OpponentID: 3
      
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
      - Advanced Ballistics: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities. Also allows you to build the Guided Missile, an inexpensive single-use Unit that can damage enemy Units, and the SS Booster, one of the Spaceship parts necessary to win a Science Victory.
        Completing it would unlock: Lasers, Stealth
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - The Internet: Increases Tourism output of all cities by 50%, helping you advance toward a Cultural Victory.
        Completing it would unlock: Nanotechnology, Particle Physics, Globalization
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late world Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      
      ## Policies
      - Five-Year Plan (Level 2 Tenet of Ideology Order): Five-Year Plan: +20% Production towards Buildings in all Cities. +3 Production for every Mine, Quarry, Lumber Mill, Oil Well, and Unique Improvement.
      - Academy of Sciences (Level 2 Tenet of Ideology Order): Academy of Sciences: -2 Unhappiness from Illiteracy in all Cities, +100% Production towards Research Labs, and receive 5 Free Research Labs in your Empire. Research Labs generate an additional +2 Science.
      - Nationalization (Level 2 Tenet of Ideology Order): Nationalization: Each Corporate Office counts as a Franchise. Foreign Franchises no longer benefit your Corporation, you can no longer construct Franchises in foreign Cities (except Vassals), and foreign Corporations can no longer set up Franchises in your Cities (except Masters). +2 Science from all Corporation Offices.
      - Great Leap Forward (Level 2 Tenet of Ideology Order): Great Leap Forward: Receive a free Technology. Spies gain +100% Science. +1 Science in Cities for every 3 non-Specialist Citizens.
      - Resettlement (Level 2 Tenet of Ideology Order): Resettlement: New Cities have +3 Population. All Cities gain +2 Citizens immediately. No Partisans from razing enemy Cities.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Ceremony (Continuing Tradition Branch):
        - * +1 Happiness from National Wonders with Building requirements.
        - * +25% Production toward National Wonders with Building requirements.
        - * Royal Astrologer built in Capital (+3 Science, +1 Science to all Councils, Smokehouses, and Herbalists; 1 Scientist Slot).
      - Justice (Continuing Tradition Branch):
        - * +1 Production in every City.
        - * Cities with a garrison gain +25% Ranged Combat Strength.
        - * Royal Guardhouse built in Capital (+3 Production, +2 Defense, +50 Hit Points, +10% Military Supply from Population in all Cities, 1 Engineer Slot).
      - Honor (Continuing Authority Branch):
        - * All Military Units gain the Conscription Promotion (+10% Combat Strength).
        - * Supply-free military Units spawn near Cities that reach (or have already reached) a multiple of 10 Citizens for the first time.
        - * -25% War Weariness.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
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
  - decisions:
    - #0:
      - toolName: set-relationship
      - args:
        - Public: -60
        - TargetID: 4
        - Private: -60
        - Rationale: Morocco nuked our city Calixtlahuaca on Turn 419, proving to be an existential and completely untrustworthy threat. We must adopt a completely hostile stance and ensure our border defenses are fully prepared to repel them.
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: America continues to reject peace and push aggressively against Damascus and the Baghdad Sea despite high war weariness. We must maintain a guarded, defensive posture to protect our territories.
        - Private: -20
        - TargetID: 1
        - Public: -20
    - #2:
      - toolName: set-research
      - args:
        - Rationale: After Satellites completes, we must push deep into the final tier of the technology tree to reach Future Tech, which is required to build the Citizen Earth Protocol. The Internet is the optimal gateway tech, unlocking Nanotechnology, Particle Physics, and Globalization.
        - Technology: The Internet
    - #3:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Great Leap Forward as our next policy in 19 turns will grant us a free technology, saving us 10+ turns of research on our path to Future Tech, while significantly boosting our empire-wide science generation.
        - Policy: Great Leap Forward
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - Wonder: 80
          - GreatPeople: 60
          - Air: 60
          - CityDefense: 100
          - Defense: 100
          - Production: 100
          - Culture: 90
          - Espionage: 20
          - Offense: 10
          - Gold: 70
          - Diplomacy: 50
          - Science: 100
      - rationale: Since we are projected to influence The Inca (our final required civilization) in approximately 2 turns, Tourism output is no longer our primary bottleneck for Cultural Victory. Instead, our ultimate challenge is reaching Future Tech and building the Citizen Earth Protocol wonder. We are pivoting our empire's focus heavily toward Science (100) and Production (100) to accelerate our tech progression and wonder construction, while keeping Culture high (90) to secure Great Leap Forward faster. Max Defense (100) and CityDefense (100) are maintained to ensure our survival against America and Morocco.
  - tokens:
    - inputTokens: 21738
    - reasoningTokens: 7488
    - outputTokens: 439
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Focusing on Cultural Victory**
            
            I'm currently analyzing our progress towards a cultural victory on turn 420. My thoughts are centered on leveraging Arabia's unique strengths to maximize our score and secure a win.
            
            **Securing Cultural Victory**
            
            I'm focused on a potential cultural victory. I've confirmed we're two turns from influencing The Inca, which, with our current standing, could secure the win if we influence all four necessary civs. I'm also verifying the Citizen Earth Protocol wonder requirement and our policy tree status.
            
            **Refining Technology and Policy**
            
            I'm re-evaluating our tech path and policy choices. Satellites are still 13 turns away, and I need to confirm which technology unlocks the Citizen Earth Protocol before committing to "Great Leap Forward" for its free tech. I also need to decide whether to adjust flavors or maintain our current stance.
            
            **Evaluating Defensive Posture**
            
            I'm reassessing our city defenses, realizing the current strength is nominal rather than indicative of immediate threat. My focus has shifted to emergency purchasing capabilities and a strategic review of unit production, with Mecca's Heavy Bomber and Najran's Infantry nearing completion.
            
            **Confirming Victory Condition**
            
            I'm re-evaluating the Cultural Victory requirements, specifically the Citizen Earth Protocol. It's confirmed as a necessary wonder in Vox Populi, unlocked by Future Tech. I'm now assessing the tech gap to determine the feasibility of reaching it in time.
            
            **Prioritizing Future Tech**
            
            My current focus is on navigating the late-game tech tree. I've confirmed "The Internet" is our next research, which is crucial for unlocking future technologies and maintaining our lead, even if immediate tourism boosts are less critical now. I'm also assessing the policy tree, particularly "Great Leap Forward," to maximize its benefits.
            
            **Securing Free Technology**
            
            I've confirmed "Great Leap Forward" is available in our policy options, which will grant us a free technology, effectively saving over ten turns of research towards future tech. This is a crucial strategic advantage for our current victory conditions.
            
            **Adjusting Diplomatic Stances**
            
            I'm currently recalibrating our diplomatic relationships, specifically with Morocco and America. Given recent events, a shift to a neutral or hostile stance is warranted. I'm also reviewing our persona settings to ensure they align with our strategic objectives.
            
            **Revising Relationship Management**
            
            I'm re-evaluating how I manage relationships, particularly with non-major civilizations. I've realized the `set-relationship` tool is only applicable to major civs, and I need to adjust my understanding of how to influence city-states going forward.
            
            **Updating Diplomatic and Flavor Settings**
            
            I'm refining our approach to diplomatic interactions, noting the `set-relationship` tool is restricted to major civilizations. I'll be updating Morocco to hostile and America to neutral, while keeping The Inca neutral as we're near influencing them. I'm also evaluating our current flavor settings, noting a strong emphasis on defense.
            
            **Revising Production Priorities**
            
            I'm re-evaluating our city-specific production strategies. While Mecca excels at production, its current Heavy Bomber build needs reassessment. I'm concerned about the significant tech distance to Future Tech and the Citizen Earth Protocol, potentially requiring 100-150 more turns.
            
            **Accelerating Science and Defense**
            
            I'm currently analyzing our science trajectory, realizing that adopting the "Great Leap Forward" policy will grant a free technology, significantly reducing the time to reach future tech. However, I'm also reassessing our defensive posture, particularly in Tenochtitlan, as the reported enemy strength appears disproportionate to the listed units, necessitating a clear understanding of the threat.
            
            **Prioritizing Future Tech and Defense**
            
            I'm re-aligning our strategic focus. While current units will bolster defenses soon, I'm now prioritizing a substantial increase in Science and Production flavors to 100, alongside Defense and City Defense. This pivot aims to rapidly reach Future Tech for the Citizen Earth Protocol and ensure survival, even with a continued Culture Grand Strategy.
            
            **Accelerating Future Tech**
            
            I'm prioritizing reaching Future Tech swiftly. Adopting "Great Leap Forward" will secure a free technology, significantly shortening the path. Simultaneously, I'm bolstering Science and Production flavors to 100, and reassessing defensive threats, especially in Tenochtitlan, to ensure our continued survival and cultural victory push.
            
            **Updating Diplomatic and Ideology Status**
            
            I've confirmed "Great Leap Forward" as a Level 2 tenet, providing a valuable free technology. Concurrently, I'm refining our diplomatic stances: Morocco is now hostile due to their city's destruction, America remains guarded, and The Inca are being monitored as we approach influence.
            
            **Adjusting Diplomatic Priorities**
            
            I'm revising our relationships based on recent aggressive actions. Morocco is now set to hostile due to their destructive attack. America remains guarded, and Ethiopia, as an Inca vassal and at war with us, is also being handled with a similarly guarded stance.
            
            **Focusing on Science and Defense**
            
            I'm now prioritizing accelerating our path to Future Tech and bolstering defenses. Adopting "Great Leap Forward" will grant a crucial free technology, and I'm shifting our flavor settings heavily towards Science and Production to reach the Citizen Earth Protocol quickly, ensuring survival while maintaining our cultural victory push.
            
            **Investigating Tool Availability**
            
            I'm reviewing the available tools to ensure I'm utilizing all necessary functions. While `set-relationship`, `set-research`, `set-policy`, `set-flavors`, and `keep-status-quo` have been applied, I was briefly curious about a `focus-briefer` tool mentioned in the prompt's narrative, but it's not present in the declared API list.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: fCvkrtbt9qhYji5n
          - toolName: set-relationship
          - input:
            - Public: -60
            - TargetID: 4
            - Private: -60
            - Rationale: Morocco nuked our city Calixtlahuaca on Turn 419, proving to be an existential and completely untrustworthy threat. We must adopt a completely hostile stance and ensure our border defenses are fully prepared to repel them.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: DpEF5t0L7iAt26j9
          - toolName: set-relationship
          - input:
            - Rationale: America continues to reject peace and push aggressively against Damascus and the Baghdad Sea despite high war weariness. We must maintain a guarded, defensive posture to protect our territories.
            - Private: -20
            - TargetID: 1
            - Public: -20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: EZDgBJHfXwRTM8Cu
          - toolName: set-research
          - input:
            - Rationale: After Satellites completes, we must push deep into the final tier of the technology tree to reach Future Tech, which is required to build the Citizen Earth Protocol. The Internet is the optimal gateway tech, unlocking Nanotechnology, Particle Physics, and Globalization.
            - Technology: The Internet
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: PaOvek5A2J8cgn7h
          - toolName: set-policy
          - input:
            - Rationale: Adopting Great Leap Forward as our next policy in 19 turns will grant us a free technology, saving us 10+ turns of research on our path to Future Tech, while significantly boosting our empire-wide science generation.
            - Policy: Great Leap Forward
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: dHVMd5CRXTvpL30X
          - toolName: set-flavors
          - input:
            - GrandStrategy: Culture
            - Flavors:
              - Wonder: 80
              - GreatPeople: 60
              - Air: 60
              - CityDefense: 100
              - Defense: 100
              - Production: 100
              - Culture: 90
              - Espionage: 20
              - Offense: 10
              - Gold: 70
              - Diplomacy: 50
              - Science: 100
            - Rationale: Since we are projected to influence The Inca (our final required civilization) in approximately 2 turns, Tourism output is no longer our primary bottleneck for Cultural Victory. Instead, our ultimate challenge is reaching Future Tech and building the Citizen Earth Protocol wonder. We are pivoting our empire's focus heavily toward Science (100) and Production (100) to accelerate our tech progression and wonder construction, while keeping Culture high (90) to secure Great Leap Forward faster. Max Defense (100) and CityDefense (100) are maintained to ensure our survival against America and Morocco.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: fCvkrtbt9qhYji5n
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
          - toolCallId: DpEF5t0L7iAt26j9
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: EZDgBJHfXwRTM8Cu
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: PaOvek5A2J8cgn7h
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: dHVMd5CRXTvpL30X
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.