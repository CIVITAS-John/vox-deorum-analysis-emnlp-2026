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
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 80
  - replay_use_nuke: 80
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
  - decisions:
    - #0:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Wonder: 100
          - UseNuke: 80
          - Nuke: 80
          - CityDefense: 100
          - Culture: 80
          - Antiair: 60
          - Espionage: 40
          - Gold: 80
          - Offense: 0
          - Mobilization: 40
          - GreatPeople: 70
          - Science: 100
          - Diplomacy: 50
          - Air: 60
          - Production: 100
          - Defense: 100
          - Ranged: 40
          - Growth: 50
        - GrandStrategy: Culture
      - rationale: We are 2 turns away from becoming Influential with our final competitor, The Inca, which will complete the influence requirement for Cultural Victory. The sole remaining hurdle is researching all necessary technologies to reach Future Tech and constructing the Citizen Earth Protocol. Therefore, we are shifting our primary focus to Science (100) and Great People (70) to accelerate our research rate, while maintaining maximum defense (100) and city defense (100) to protect our territory from American and Moroccan forces. We also prioritize Air and Anti-air defenses (60) to counter enemy air power, and prepare nuclear options (80) for strategic deterrence after being nuked by Morocco.
  - tokens:
    - inputTokens: 21720
    - reasoningTokens: 7006
    - outputTokens: 241
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            I'm reviewing our current position, noting our ongoing research into Satellites. The estimated completion time is 13 turns. I'm also confirming my role as Harun al-Rashid, Player 3, in this current turn 420, post-turn 420.
            
            **Evaluating Victory Conditions**
            
            I'm re-evaluating our cultural victory progress. We currently have three influential civs and the Inca are poised to become the fourth within two turns. I need to confirm if completing the Citizen Earth Protocol wonder and possessing a suitable ideology will secure the win upon achieving influence with the Inca.
            
            **Verifying Ideological Tenets**
            
            I'm digging into our ideology's tenets to ensure we meet the requirements for a cultural victory. Specifically, I'm cross-referencing our current Order policies to confirm we have two Tier 3 tenets. This is crucial as we approach influencing our fourth civilization.
            
            **Confirming Wonder Prerequisites**
            
            I've confirmed we possess the necessary Tier 3 tenets for a cultural victory. My current focus is on verifying if the Citizen Earth Protocol wonder requires a specific Future Tech, as my research into Satellites and The Internet suggests a potential technological hurdle.
            
            **Confirming Wonder Prerequisites**
            
            I'm verifying the prerequisites for the Citizen Earth Protocol wonder. My current analysis suggests it doesn't require a specific Future Tech, making our pursuit of The Internet more direct for boosting tourism and cultural victory.
            
            **Securing Cultural Victory**
            
            I'm confirming our path to victory. With the Inca nearly influential and the Internet research progressing, we're set to influence all four civs soon. My immediate concern is the Citizen Earth Protocol wonder; I'm verifying if the "Great Leap Forward" policy can bypass specific tech prerequisites for its completion.
            
            **Confirming Policy Choice**
            
            My analysis confirms "Great Leap Forward" as a valid policy choice, which directly impacts our cultural victory strategy. I am now reassessing our diplomatic and military standings, as it appears we are at war with every major civilization. This widespread conflict significantly alters our immediate objectives and potential alliances.
            
            **Assessing Global Conflict**
            
            I'm re-examining our diplomatic status given the widespread war. Despite Friends designations with Novgorod and Vilnius, I'm baffled by being at war with all major civs. Military reports show significant enemy strength in key zones, though recent direct combat is unclear.
            
            **Analyzing Diplomatic Situation**
            
            I'm struggling to reconcile conflicting reports on our diplomatic status. While Novgorod and Vilnius are allies, I'm at war with every other major civilization, despite having "Friends" designations. It seems Morocco nuked our Calixtlahuaca, leading to war and significant war weariness with America, even though America denounced us for our divergent policies.
            
            **Resolving Diplomatic Conundrum**
            
            I'm trying to understand our current diplomatic state. Despite having allies, I'm at war with most major civilizations. It appears Morocco's actions initiated this, causing widespread war weariness. I'm now assessing potential peace options, as none have been offered.
            
            **Confirming Wonder Status**
            
            I'm verifying the Citizen Earth Protocol's technological requirements. It appears unlocked, and with the Inca soon to be influenced, victory hinges on its completion. My immediate focus is ensuring no advanced tech is needed to build it.
            
            **Accelerating Science Research**
            
            I'm realizing the Citizen Earth Protocol likely requires a Future Tech. With Satellites and The Internet next, my focus shifts to accelerating our science output. Great Leap Forward offers a tech, but our 1,868 Science per turn needs optimizing to bridge the gap to Future Tech.
            
            **Prioritizing Tech Completion**
            
            I'm realizing the Citizen Earth Protocol requires a Future Tech, pushing the need to accelerate my science output. With Satellites and The Internet next, I must optimize my 1,868 Science per turn, as the "Great Leap Forward" policy offers a tech boost, but the gap to Future Tech is still substantial.
            
            **Boosting Science Output**
            
            I'm re-evaluating our strategy to accelerate technological progress. Increasing our Science flavor is critical to researching future technologies faster, especially considering the Citizen Earth Protocol's potential tech requirements. I'm currently analyzing the impact of raising Science flavor from 30 to a higher level on our overall output.
            
            **Adjusting Flavor Priorities**
            
            I'm shifting our flavor priorities. Maximizing Science to 100 is key for reaching Future Tech quickly. Production and Wonders also remain at 100. While Culture is less critical now, I'm setting it to 100 for now, aiming to maintain our strong position and gain policies faster.
            
            **Revising Flavor and Relationship Settings**
            
            I'm recalibrating our flavor settings to prioritize Science at 100, alongside Production and Wonders, to expedite reaching necessary Future Tech for the Citizen Earth Protocol. I'm also reviewing relationships; Novgorod, as Friends with 154 influence, seems stable at current settings, and our war status with Morocco, America, and Bucharest makes adjustments less critical at this moment.
            
            **Researching Tech Tree**
            
            I'm re-examining the tech tree. Alternative Energy leads to Robotics and then Future Tech, which seems vital. "The Internet" is also next, boosting tourism, but I need to ensure we're on the fastest path to that crucial Future Tech for the Citizen Earth Protocol.
            
            **Prioritizing Technology Acquisition**
            
            I'm realizing Future Tech requires completing all other technologies. This means focusing on both the "Alternative Energy" branch towards Robotics and the "The Internet" branch to unlock Particle Physics and Globalization. My immediate goal is to determine the most efficient research path to secure Citizen Earth Protocol.
            
            **Choosing Next Technology**
            
            I'm weighing the immediate benefits of different technologies. While "The Internet" is next and boosts tourism, my current focus is securing the Citizen Earth Protocol. "Alternative Energy" could unlock Robotics and lead to Future Tech, which seems essential. Alternatively, "Mobile Tactics" or "Advanced Ballistics" could bolster our defenses in our widespread conflicts.
            
            **Choosing Next Technology**
            
            I'm prioritizing "The Internet" for its tourism boost, but also considering "Alternative Energy" to reach Robotics and potentially Future Tech for the Citizen Earth Protocol. I need to balance immediate gains with long-term victory requirements, especially with upcoming widespread conflicts.
            
            **Optimizing Flavor Settings**
            
            I'm refining our flavor settings to aggressively pursue Future Tech for the Citizen Earth Protocol. I'm maximizing Science, Defense, City Defense, Production, and Wonders, while keeping Gold high for emergencies. Offense and Recon are set to zero given our current defensive stance.
            
            **Adjusting Flavor Priorities**
            
            I'm recalibrating our flavor settings. Science is now paramount at 100, but I'm also prioritizing Defense, City Defense, Production, and Wonders. Gold is kept high for emergencies, while Offense and Recon are zeroed due to our current defensive posture.
            
            **Setting Science Flavor**
            
            I'm setting Science flavor to 100. Production and Wonders will also remain at 100. While Culture is less critical now, I'm setting it to 100 to maintain our strong position and gain policies faster. Diplomacy is set to 50 to maintain city-state alliances, and Espionage to 40 for counter-espionage.
            
            **Prioritizing Technology Research**
            
            I'm now setting my Science flavor to 100. Production and Wonders also remain at 100. While Culture is less critical, I'm keeping it at 100 to maintain my position and acquire policies. Diplomacy is at 50 to sustain city-state alliances.
            
            **Prioritizing Technology Choice**
            
            I'm confirming "The Internet" remains our next research target due to its tourism benefits, perfectly aligning with our cultural victory goals. Great Leap Forward is also the correct policy, so no changes are needed there.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: SM8AKuerXYSJBFmH
          - toolName: set-flavors
          - input:
            - Rationale: We are 2 turns away from becoming Influential with our final competitor, The Inca, which will complete the influence requirement for Cultural Victory. The sole remaining hurdle is researching all necessary technologies to reach Future Tech and constructing the Citizen Earth Protocol. Therefore, we are shifting our primary focus to Science (100) and Great People (70) to accelerate our research rate, while maintaining maximum defense (100) and city defense (100) to protect our territory from American and Moroccan forces. We also prioritize Air and Anti-air defenses (60) to counter enemy air power, and prepare nuclear options (80) for strategic deterrence after being nuked by Morocco.
            - Flavors:
              - Wonder: 100
              - UseNuke: 80
              - Nuke: 80
              - CityDefense: 100
              - Culture: 80
              - Antiair: 60
              - Espionage: 40
              - Gold: 80
              - Offense: 0
              - Mobilization: 40
              - GreatPeople: 70
              - Science: 100
              - Diplomacy: 50
              - Air: 60
              - Production: 100
              - Defense: 100
              - Ranged: 40
              - Growth: 50
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: SM8AKuerXYSJBFmH
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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