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
  - activeToolsModified: true
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
      - toolName: set-policy
      - args:
        - Rationale: Great Leap Forward grants a free technology upon adoption, which is critical for rapidly unlocking the late-game technologies (Robotics and Future Tech) needed for the Citizen Earth Protocol wonder, our final bottleneck to cultural victory.
        - Policy: Great Leap Forward (Level 2 Tenet of Ideology Order)
    - #1:
      - toolName: set-research
      - args:
        - Technology: Alternative Energy
        - Rationale: Alternative Energy is the prerequisite technology for Robotics, which is essential to reaching the end-game technologies required for the Citizen Earth Protocol wonder.
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Mobilization: 0
          - GreatPeople: 50
          - Wonder: 100
          - Culture: 100
          - Growth: 30
          - Religion: 15
          - Science: 50
          - Nuke: 80
          - CityDefense: 100
          - UseNuke: 80
          - Gold: 80
          - Production: 100
          - Espionage: 30
          - Infrastructure: 40
          - Diplomacy: 50
          - Defense: 100
          - Offense: 0
        - GrandStrategy: Culture
      - rationale: We are 2 turns away from becoming Influential with the final civilization (The Inca), making the Citizen Earth Protocol wonder our primary victory bottleneck. We maintain maximum focus on Production, Wonder, Culture, and Defense to safeguard our borders. Since we are under heavy attack and Morocco has nuclear weapons, we boost Nuke and UseNuke flavors to allow our upcoming Atomic Bomb (finishing in 2 turns in Baghdad) to be deployed defensively to decimate hostile armies.
  - tokens:
    - inputTokens: 19513
    - reasoningTokens: 5837
    - outputTokens: 305
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Focusing on Satellites**
            
            My current focus is on finalizing Satellite research, a crucial step for my Cultural Victory aspiration. This technology is estimated to take approximately 13 more turns to complete.
            
            **Refining Strategy for Victory**
            
            I'm re-evaluating my research path. While Satellites were initially planned, my progress towards Cultural Victory is accelerating. I'm already influential with America, Ethiopia, and Morocco, and anticipate becoming influential with the Inca soon, which is a significant step. This shift means I should prioritize research that directly supports my tourism output.
            
            **Verifying Policy Tiers**
            
            I'm currently cross-referencing my active policies against the expected tier levels for "Order" in Vox Populi. My priority is confirming if "Peace, Land, Bread" and others qualify as Tier 3 tenets, or if I need to acquire more policy choices to unlock advanced bonuses.
            
            **Prioritizing Future Technologies**
            
            I'm now shifting focus to unlock the necessary Future Tech for the Citizen Earth Protocol, as Mecca is our best bet for its rapid construction. My current tech options are being reviewed to determine the most efficient path forward, considering the Internet's tourism boost and Alternative Energy's prerequisite for Robotics.
            
            **Prioritizing Defense and Wonder**
            
            I'm re-evaluating my current tech path. Given the widespread war and significant military disadvantage, the immediate priority must be shoring up defenses. While the Internet offers a tourism boost, I need to secure my existing cities and ensure I can even build the Citizen Earth Protocol. I'm exploring if Alternative Energy is a necessary prerequisite for a defensive tech or if I can bypass it to research technologies that bolster my military capabilities before focusing on the wonder.
            
            **Assessing Immediate Threats**
            
            I must prioritize immediate survival. Morocco's nuclear strike and the enemy's overwhelming strength near Damascus and Tenochtitlan demand a shift from cultural pursuits to defense. I need to secure our cities before considering any further progress, as holding them is paramount.
            
            **Securing Ideological Victory**
            
            I am close to achieving Influential status with all four other civs, a critical step towards my victory condition. However, I am still verifying if "Peace, Land, Bread" is indeed a Tier 3 tenet in Vox Populi's Order ideology, as acquiring a second such tenet seems impossible with current policy options.
            
            **Re-evaluating Technology Path**
            
            The recent nuclear attack and significant military disadvantage have forced me to re-evaluate my technology priorities. My focus must now shift to bolstering defenses, potentially bypassing technologies like Alternative Energy if they don't directly contribute to immediate military strength or survival.
            
            **Adapting to Moroccan Aggression**
            
            Morocco's unexpected nuclear attack is a dire development, and I'm assessing its immediate impact on my cities. Baghdad's production of an Atomic Bomb is a concerning counter-response, and I need to understand if Damascus or Tenochtitlan are truly in immediate danger, given the enemy's numerical superiority and naval presence.
            
            **Securing Policy Bonuses**
            
            I'm confirming that "Great Leap Forward" is indeed selectable as my next ideology policy; its free technology bonus is too valuable to pass up. Once secured, I'll prioritize researching "Alternative Energy" to unlock "Robotics," essential for the Citizen Earth Protocol wonder.
            
            **Prioritizing Production Efficiency**
            
            My current focus is on optimizing production, especially since I'm at war. I'm re-evaluating my research path to ensure it supports our strong defense and production capabilities, as well as our wonder-building ambitions. While defense and production are crucial now, I need to see how other research options might complement our existing strengths.
            
            **Boosting Nuclear Flavors**
            
            I'm now considering a shift to increase "Nuke" and "UseNuke" flavors. With an Atomic Bomb nearing completion and critical cities under threat, leveraging these flavors could enable a tactical nuclear strike for defense. This adjustment would significantly bolster our immediate strategic options.
            
            **Adjusting Nuclear Strategy**
            
            I'm now fine-tuning the AI's flavor settings, aiming to leverage our imminent Atomic Bomb defensively. I'll boost 'Nuke' and 'UseNuke' to 80, prioritizing high defense and production to weather attacks while ensuring the bomb can be used tactically against enemy armies, as well as slightly increasing science for faster research.
            
            **Confirming Ideological Policies**
            
            I'm verifying that "Peace, Land, Bread" and similar policies are indeed qualifying as Tier 3 Order tenets. My primary goal is to ensure I can unlock the most potent ideology bonuses for my cultural victory push.
            
            **Adopting Policy and Research**
            
            I'm adopting "Great Leap Forward" for its free technology bonus, crucial for accelerating research towards the Citizen Earth Protocol. Concurrently, I'm setting research to "Alternative Energy" to unlock Robotics and further boost my wonder construction plans. My core strategy remains focused on culture, with adjustments to flavor settings for defense.
            
            **Adjusting Defense Priorities**
            
            I'm shifting my focus to prioritize immediate survival. My current technology path will now emphasize bolstering defenses and production, with a goal of leveraging our imminent Atomic Bomb tactically against enemy armies. This includes adjusting AI flavor settings to maximize 'Nuke' and 'UseNuke' to 80, while keeping defense and production at 100.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: RjsXYI2tEtRsxMIL
          - toolName: set-policy
          - input:
            - Rationale: Great Leap Forward grants a free technology upon adoption, which is critical for rapidly unlocking the late-game technologies (Robotics and Future Tech) needed for the Citizen Earth Protocol wonder, our final bottleneck to cultural victory.
            - Policy: Great Leap Forward (Level 2 Tenet of Ideology Order)
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 4Z7i8RY0RJWvCHJj
          - toolName: set-research
          - input:
            - Technology: Alternative Energy
            - Rationale: Alternative Energy is the prerequisite technology for Robotics, which is essential to reaching the end-game technologies required for the Citizen Earth Protocol wonder.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: kosagISJoesEy98G
          - toolName: set-flavors
          - input:
            - Flavors:
              - Mobilization: 0
              - GreatPeople: 50
              - Wonder: 100
              - Culture: 100
              - Growth: 30
              - Religion: 15
              - Science: 50
              - Nuke: 80
              - CityDefense: 100
              - UseNuke: 80
              - Gold: 80
              - Production: 100
              - Espionage: 30
              - Infrastructure: 40
              - Diplomacy: 50
              - Defense: 100
              - Offense: 0
            - GrandStrategy: Culture
            - Rationale: We are 2 turns away from becoming Influential with the final civilization (The Inca), making the Citizen Earth Protocol wonder our primary victory bottleneck. We maintain maximum focus on Production, Wonder, Culture, and Defense to safeguard our borders. Since we are under heavy attack and Morocco has nuclear weapons, we boost Nuke and UseNuke flavors to allow our upcoming Atomic Bomb (finishing in 2 turns in Baghdad) to be deployed defensively to decimate hostile armies.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: RjsXYI2tEtRsxMIL
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a189bH01/a8thw+6P8YAcoxs6z80rZWR91VZVKmrlES6LyXunlULf0ukKqVdY+I7hDPXbnTIIoHaVzvjrF0hXkZBdFEFDR5uPpN+gb4wekyagcPOMlfXOSKoPZ4cMuZL1I6T+POnPFh2SPT0BQDqXuIuWrVT+rf9WvJG5Fo9q4xnR1Bo3JJEF2eKsjkaClPMy/vqQL4phzNqeAxamn0oQTckqG1dRyNOk1gJia9KyL8pBF+w+LyHUUT2NlLQft+yqGMJM1z3TW0OtnlmL+8ZlWL/5SvV/lk39+yVGhlTzNMR4V8nROFGTIFtdtsC8H1FPnK3p+3vxVTJ+hTkszy5bDz+kBZrZRs9BXmLnZF7B2fCWxfrWhtAKSG2f5LQcYe6V8OUfKBe2nOPZDH+a6kammdAkQUxBBkkM12Oe/ot0q+9ocVbdA+6P8MLTy3o2XK7nopLxT3SD8dMPZASwisArh2dbIJZ87rx8QQVycveo6Ff+J02cVyhQbTCxueveLlgzy+YFOMkairD5504pW3SwTlCowfuGY9glVT4rXxYwYpJ7+LeNmL9nc6bKxgiffMsqEYFRaMhuYipQ9/42zQkpIOIlOvWTD95uBzvn6UYVoXd4Ew+xJP0fMDxsbyFzWJaXbv2B2SnPLL2BBA3abr3CfzoXyu8dApBRW2dqZ1dj2Thiidx5NUuHIV6yTibqAYOJ7Qc8Mhu5ukz6GrqtnwuuID2/l+9qLnahPt8TaNsA84aCVUQfpK1rDi6CAAQtVKVKYtnrK27RSY79slobxb3h4qSi2VVNzuwnbzhvxFtH/CrK2Xh8POTZ5JBVtel8583TUI1JuChNO9befa1DJWfI4IGVO4hpxE552+kEO73oAVN//QtaDXCyu6g4s+WtXuIVc96Sy78VZFoAgAvnhsqVWYG+odjZLpPQdCArYlA1sU8x5wilTTQq8+vrVvGUimlLJd6xEmwoY+eZW0+BWnaRC+9gtdcGAHzHRQ028+9WMbw2oZjg+cPJ7XaoDPR9P/OrD4TJVNYNtDe/2f1hKGEqj74byXmUAKPmas5Dd/oR0SpkGL0Za3dTRxfAWDlLipea4DeSkqkyw7ldO0ehJ4pnsokHysnO7JPQQukNi9l7envW+Z7yvO61fMu3pFy48sG/CaDmvJzSqO48bnCjgcLXmDIub/tL1rqXu/JTYVRqxpN+hldEuUq6kpuSTWst+256YpcyzxBvjNwWDsNhubFtIhAi7Ut34WfQCWmPhN0C8tJ1PANpKieFRuoHa6AUtQpnMR+Zp/3x3Mg+xySvpp16+/f3xtczOhFXjJImDyqDQFIq+RguPWcgDcV7sibXt0dOl9dbqf1YeNRS237HNqyB3PmkNeXNDTRGmLPWd2sgM7fV0OterITs07MMTnBCjepy7CvIqYt1D0TXM2xUdmcD6S9R/XfkL9Mpks3aOpW/AHT6HPch1Cgo6xL3pGQ4X9Vp6tfMbnY/EGL8JrcvLfU+cN2EsUUDDXcLAAkEn6WR3he4aRMdxrI1fQuK4a2rUPs6vo6NTDB9XY15k2fvNJCbWHt/NUOL/Hq8Xunm/4/vzfEN7MPU3Ah/SApDKDoZ+yto5Oc3fwq9UA7/ESrGEMCpNyUUCivnY7uRpJjnXUWufacfyJn6S4vjtLHM+kQ+PRZJfmlJDqMPsYIXPHDDaQBFbFqjpcHzasAlrxUvMmnh/MNfaGq/QCoaLStF9rU7zPnLG79/6/sYTpNbTqcPsZ7yuRbIVtVT/6wPXnyRucrhavTs3kntwJbVZq1WqMTOoX18H63GFWVcPP6b5F9HLHg0lZ4zWVF0PNv7BIrB6RRNpq49XzZfxOh9ujmuVkHXEmrUK2FfFHGTm7vFvgUfS7iczlQ2CmM/Q0AKTPC534GoQhNEQDLPV4kH6quDbJP3lB5CxZyAhyoAEN5ZfCIJ6GuHKS1i/lqR07woX9zPRwscKts0Eixj4BQV0Vao2fOeUMOhZn5R5Om3WRmJfRoYCxlWuKmEe46T4YRVCXFe5dRrnJ/TEIUE6wLRvejltKDxzsPPfqwOAAO+VH+a6vBCsCkO/KV7kVtUPpXcM1oQM2JX3GQvcRayst+lzeVCS5qz41dTA4ggUVv/if6LLtgAnuf8qp25VVFIw1pb8Ke/1+93JBXhKQH0A7iiRfjvWsx3SXyif1c6a9R4x/BKfljEh8rX1Y53bXBYJrfq6KphkygDyYkTr4jiurEi/ZmE4s93eHkc3DMVVLNiJ0b5tfPWXENI7lw64gntm365CL5m62QGjdH2vTgdBcIgp2CevFW7jlYeG+7lz+7z0jE5TwqUkPAWefZxGNoZcOsgPawGXLkzWvlAWVlnD6VQlTiWj8GYdiCdA3DpA5ofX6KHakzCvtj2/mkPEvaGJvHlSjrP6L13K13Gbni4P6vM0UC9N+8WnnibkrZ+ZyPhME8VBZQg7Lu6a2DXYWXAzynoB3ZQsf4gx0+UytD2VYzvGZZhTV681mr3FwSRkF+s37WrgHTV0DIJ2cn6/SUIIG3pu+26itlt7sPoeK6s427w9OtmkLxlUz5TSMvrKtT3i7a4k9tBKzUTyRq9gVyVbevFQYiSW5N11HQlf9DqV+u457GvisBpAvSf5bs0XUcSjDExY1PofkKSgsIuFlMjzpT/k3eyPydBxjhW0aYyfpT/3W/k6sH5REn0v9cnu3Dvt9srcxAeq07HEjVj25bJmJebrnJ7Z0kp+etlahYmMI+hb6JI3UWFTFWaCSPdQQA2jLJaz4q8hqRVFpvGeTFcywasEKxMxABC4rrLqrhbZPJ+7CuRx1UDxrUK5UHZ7QaX4oLgLme0K07wHsFnyMVOFvMNcxxEZ2UUj5b8ORGajdpV+rmVNTCMxyt4k4/He0CW1ByqRu/VLfBLE+JOU4f+nh7LVcGP59EMF+G6hvp3Ia7Odu/RC0hb1ZniwohEZzL7jcG60ijueXuh8Akjd+8mbdbFkeFByb60aKu4XQvNIZS6sdmIf9zkk1u42radhtb9ZCqWjG5q3ycr8EjuhGyiLq0LeUb++wB/ufH3nQY+9YqFhFhsOvUop5YTzsmsplr35SuxqUqgGPrYBPJqfEYFa7CSqzYFaBa/27/UEQKFz8EY7ZRQyhEO5Hlwtzsh+u50gv7yh1l+E7gM0UHbKQQj4NPBPhkI1pDaYK9ZHKn/odR2MWqoBXuoMeBWZ5X7NGXkmfxC3z38S9Pt5S6DXiLNYkttVR4fgS7sYSV4EJ0O4Fns78Kw/BsA+wlTupPocBIdW1P2QrMDK3nulaRMsRmlSVl418X9bkWHj+qN2zrDSowGrcqocPpZZHLF2Jcpj2DrVyKkvqPsZw9kiGxMGpcDeTiWs6TCO4lH3Trrg9JMbJx8Kt2pS0lfubEZghwCA+YUMQ4u+gR4QsDjJgPO1qZtw+CIukVGLIkTiZoH/LgggrOY/+zl5vqvfXRvhoTscX7tzxnNiJSeYo0zv/77xNe1wZKqiVBMOPAMeVKyGVHf3EPFS+cPz4+F8+2tO2bIlndPxRb1gtTAYzXWEUZ7+MB2nHgvMMZzZRH8rEYHrkYCu3CB4bWEm/FV1HJFJO90wPCwByt9vIn/DY4OVTFo9m5682S70J/s24SCs/FqubrrJth0OhuI9Vo4zLgQbSV9D6GPtlXM2C/EaqQdPW1fpWGDvfmFxqvzYPq4exeohB9dZ7RY0RdKDZV5WYdVBjNODWg3eVhEhb4HabahDkqTvd6RMaHlMWAduMRLEiPKnBw3TyxHdAjMndqAYL/B/lyZiUh+YAQlFVuzEyBNLT0HHnFDVjc/RYaE3xX6CmyVFRv6NtICYc0r8cwSexB5WlOtJ6yk0FZwhQRj17ONxuBBqgksEGIkqbH+cVYczp20wVaAf7S9cxL+tL+WTcQSC6rC5SV50z/1vcyog78YGecpUL6a005s9ezOJyOTL/aifvLrSDECaVB1lCXIElYBpUKkrC/H5cVJPz+A72WAbpcqwieVP0pXR6+hw/VAiqDXW7NE8knYSvlyhVcxARFxDFThyllIS1zFm9jAdSVjdx6I7uZvQzVcklTGbsXveVu2zzo3/CiC2fAcvdMz16GwCFY8z9H9TEywv89I2/6aFyHC9uzBiTBKrdCbZL1j6WyD8mxKaTeOUDQ8peuTrxeyDvj0CJV5ad7f39QVJvNPibefupSuF1m0vC2kWuwyZGrgakUjtYZcbZ9RGNGHhUo9RJD4RaMhX5gdabeVyxAYxxujPFQvjIfVQ0Pa1NVDKZ56omLxs6urYGw8m/fG08ErRa52Z/U2wBVJxIiXCnmLKLy0oEfCauxnvx+oiUuvdfancwbiDQDOS4kAtGNtQt91OBWvF/xZ21TqU6DwegxZGnsER9ETXkY4OZwiWvHH0IUl0IKzQ9NLBVD5BF7DysT3fr995nxcD2YQT5x2PTGS9GK7UX6gODh5pD3H1ZtXJ4rTKJrC7c4x/hndMyQR44SFYW4nX9tMv0+cScB/gMC+h6fd51Yq/yBeR3qOYxol5he7/jXaVOLqxrJtgmZBJ3znLg4inx8Xr8J4W7H3DsNegkkvjtSu2WwXLt3N//ejugMTrmn9zQQ5hPSEw2+uhapZ31O8KUbMtrWFGkd0oEVHoTNfApxIx6gl672W9u+CNGouf0qk6Mm4JYilId+LXTSfIaO2zOl3EW48pHZMcaQ2thbsDle/xGpNWgafJLQirRXAnZcEQdmERWe2mbJth+bcL7uGl32Ai62dhOkQ65Zu20DUSUovSMU+JQxcFAKfbzdcVJQH6BP+lH9Z2z1IfXgXgV4cNo799zv7CnEtjqez2p7iYQO7yhgEEvYcMuuolBknYGfQco+LRFJ9PM1xow8+uJiMN7agAkonDDryWGmV14NfYRrJdv2BnBoabyM9XJRcXsMISuT0FGQhVvB5HNe4ZTiTGA/BrzLtBVXnUa27wH2yJNmi8NQGRk457U6V+QPl1l+SejeD9YB5CR0CkrY5qW/O0aM/0PiCh/9IhxOpMt1gU15M9+eFVyLVq8+mOO6T8uLlCj0mZ/MQ6d9hVn7XYCZoe7ALPfezM6lZxFuIf6OmxqLza//0a+Y53XjyiD1LUUy3C/Qudix1i0v+2NOLKG6yQ2p0kXY4GdGfZovjBjcHcMjdvXjeKpGwbWNdmGUMs7S1vCtjNHBv4W06e4cG033Wb++bvgxDZDGNuh4P0XtY411NcsBw9AOJnawRz2B9VPQykQWxepN7gjmSLdQrDtOGuiIJSYAFR3McrjjS5IDVvMdfMcaKUyodYSfQBcOJfo3hP+icd0K1XJZkI7SGVpcYL+TLabS8fNXyYScDaaaLO9KdUxtOUTsuEBxEj4B0HP0HzAZDWBb0O1HikjOtjKCWSEtEb+MBlhtLMva0isHJEDkDP32c9p0XkW9iqbAHbNNsxGuST6R0FSx3pI1R5f6QhgIxCnkmH/umzkWJBHCu1eI9RLQUPsLUTAjjaJuLt6wN/CRrHvdY659z7SFWiwdbcLDNWwoZQxTuQ5Zam4FJEscL2FHbPc/UdDgUK/kehMrHgDtPLwW0C3BIQ3M7mchUtW1yUSTqyEO8I4dD0bryqpAEBPhoyi/Zfztdo0Gfp80M3pMh58k09GKD/zgDT+hlmP3cYw2TF/P6LP+VzQHyAlj3iCmrUxyxDQMfyEn26eGSZyjBeL3yRb03GKDgjQ0PK/qKJEsS2UfRjJOUuAT/XjbfFcsKHO8a5llo5tdiVauvoZOEudwXvyUFr+ZnWGTVwbIF6fePfTzrjj/ZgTSVea2w/b8+nIuvdXwBN2iB0DYH1kIptXlFeQopw+3tRmrYATBGBIZeURv+PpKERmmALPjKJIciNuult2BmHTISk61afU8PAulc5WyqGMgaNnGGSC9PC+BueA61L45xgfsSAdlpb2/Iswy2vYivU/P/tN3AmrcWXUaNOJfFBLW1pFeq2ihbaNAxoWjMEybVUBWnRRs8b0JwPjsX0Z6ipA9gUpQ01j0e52flGNrX6Kn181krgwBkgMqeG9VU4WeivxBCIgL2vPOEB9bQ/QjBJEU4oTxk7TAiMqlx3AxiHvomzt83N/xX97sMEJ3Glp8QlR9ycemIvKPQGTnkZlzs37wfAsRe9RHjR6Ag6/eJAkut6+vGsZJWEyNQ9xON9YnspXJrjKFulTMvzhwPtF92c4eHTIimYX7+ymSyrlFKBMxkyJnOUVApR4Fsa8UQuxVJCOsPCAa6ZZvOX3qdkE+iOxIR0fq7EOIY9K6FKXX/sMvKsRY+EleODnhl3vkPSSInusu43Qgvkf+oW9VPh7F4YDSgHrX3ksBuaIFbWAe3UQRDW1POziMxs/zHoqNsomEYF8rMfhseb2rRMmUYXeujdDXMHAjdx0fOKnG2vJDSdBAqpef8fOtbzqLW0vHQy4eeq0+Yn5Mr4F20licAZ1znIKdGFu5R2A71GEe047tI8a5/ohHj77t96wqrcTHjHN9fk9LqXsgeNx+EGO69MAaNYwlZbOXmSF0cxjX25YvPGwRdZQKdh3jeSIe8/HtPSHEVJygBs53dl2R7alv2YeBZKWZ/BZJXK1WlFdVZwW/lFM1amLV0I9xWc3I9uecAVBlfWmZNpEganJKYRbSQjEIdYj3StbGbsyhQDj54nlJoLGycq4ZN/RYxNjkzhC4XDtlyOxND7JE26wcY8QLlv/4/vrLpmwKwV3P6JOoRHlabMtC77nu8ztRgNAyQBaDAvrYOQDSaWvbz3Ym/Ayv2eHyewqZBcrYHBRc85EpDbsxogioXWUSPwju3syywSWwfi295xVSbK9ouv8CJAuce0Cwr/CePsevVkooBmHv8uR7ZbBEbtpJ8zymEDM6SJ0ln7l0vGJnFYdKY0OMxKFG//R6YXTPAPluFfTTqujHRonq3lTb0evmOyAyI82qPqji1MMigDhpCzJYI7E59bRU32hTZUX91kjsDJnRDKOJWmih6mpaEXzng1QJC/bn3sWQyDYCYEwmrk3C3pOWuGYiAD9ORFS3YIybnvemZSR5s1YtiIOPHPq3iVbz+rWC4eNQRBzIjdZTHzsrBfBLB4rIABICgxVQsJlF7PopwZL1gZzLicjs4952/RnDvfq/F2ynAo+/FhR1uSO1LoT0Nw0xWg8Dn9F21p94R1xuj3f2GyHR6ITiv5yRPkBZHNie2zwlXOM0y9pf250nJrJW6q3DiLhLtfTEZXTFrDbXodLnHkpsdEkFJUBzX2uNc/7ER19Xq055qWSUo928m9JvhgedXAAcHUorE6fupreGcARPSgRPbTELRQNSq5kkxis2VM9c2E+n6QHCKE+7hPp+DPBuO9SUpSB+ct8hqdi6OtBUlMBDckKh1W0Mtcb8uy4Ky+B5E5N9fpisVR1GBQTSravJmkHymo96Or/1yPFtojPOjMWk1DLqMgBH/23w358ph1a+RMQtNTLxNaqcdHF37HlJbzsxlTYfFuwuV2YQgmHNCq+5aSE2C4mH4/V9/uYQXMR2+SZdUXaqZnOF8NqDODKpoYN1+Ol2h38G4AWdpY/XLd9W9uSBSotmnxpAeLdqqaoIYb0CwWn1lJ0095BV8Gh7YUoR1LWn/TsP8/yRjbv4AMjkAKQDDD6bhsoFBfODLacS3bgFCtQ4VzUOPBjWtTMNb3Vd564b4MgJpytuQMF1pFQiRyx7ip04nfgAHDqLUQmucJ5xNHx171mSiqQI/DS8kOMktAUclFMPLKmoPT+dzC8vyUgRAmfQjhZY2VaquEe5WRcjW462XbGr/9OwA/dAB7pEU8dSMzZnUTWTvzjeKLJv5UVnq/xN2rXtXcKSDe72qH1278jep7uPEifFOfJsp0sASs0ckyNf9r4JCE65TJ90jbhAPREqFIWqPpjhFHD+BQtaBo68MQD+UFzGUsK5m1hmLH7DAejLNsKTycFCQo94FFaKaw14qv2cnJtucC8JtbgkHQ/0FH0paBxILS5Ufgdg/RkIf/Bc9F4OrZZTgiOaVLEJLgMy9+B39Dp12BREqdeuUKi5crWuSZQV6FZVzRcvk3NFLGn84Src5Vemy22cxpeMCHJ9xqgcpW24sedRfn77pizAjrbkW/+uKOZ4vqmGFaiNqsB1PrmMbMi23719uMHKFcPLWliqj4X+PQp+iWW1DQtuf4Slv8nmznSV8xPBLUG3o8h9Kfm6AlbdN+E01mr8Nug43JA4D11h67SH4hf+Cve4tuHCCNGRqm77n7eSJ7t5+z5LdSKfrNfCwGLO6RapwqWTIcdq/OnGJ6pOmtBCvZq13B0tTnxQUZyTL6hAQ/YWrKEzuR7LgGtalmW1smE2wlatGpJyHe1rIHO4aDbSFKQoSMyC5y7rjc7G4VJaiAKjQw+U+GrW6LfH6GH5BsRwc15FaplIeAZhknYLo7nI0Lb5lgVWiq7HXQVHf4jQ81lW55bpiepOAjV/+GhLmCjOYRYorKD4bgPtvGA+Fn0jLFnm1ANySlkW8CF74B5qgcFXMzKWmAEGwepcn7PlBFmwTC2i7EwrvjdPCIep/uiU4i7Z0qE99zSYTW8XSuvEM8jb721ol7UUyY9P90/t8T1nsqzx6eqnGGGi12TRnKkpS75VsoEFD5BAy5LBuG2QUaSZojyYgPZexA9PAQCO4vTisKMO/VQeld9FzZ/hEk35aDxKZ46g5A5jna8Ig3lu/T3N5UnhOuyzTDPUP36tC7C3vB5hGspVKCCf7GX9NF+TBVztT3EF1wpnongw5ccDUhQmMo84ajVcXGQRvf7v9o5s1QPpHKjUCXj/OnpIj7qv97I6CdZqEF6SKjMC/ZwDGf6zXhbx5rEELszC6ObmQ2eYbPJD7fXn99exLAue481pbYzxjXGPNGATYeMH/bCJ2AGKjWUqDM//r8gp+f4YVfYt/t/tQ4aiheRCnSRqqC1I/yrqmzn3t9+YPny2Q+1jtYfYa2ewutvpMSOSCcIQ27kwVgpbA5LlyzlHix9MmECNNBjquOjn/YRWB4dbtXxAp0KT8bx+E5n4tQefzRjk0StRc16y68unu5AO02QunYmnQn/5dykxhWzwDfMZhYC6ZiVnH/BD3ndU7JFtkPGts0+wNSRahN9V95OR1VxicFPguFJKOd7aBTRD2FjnLzwYbRdgxVgAS0V5fuR5tToXRh+jEJQxsQrfKlbuSZMC2AHJubFuirDB0X6uSo1H3z6nYQkwB8iw2c6+MLtXmLL9+VERdHas8+8BzblOW06ZHJz31U5/RAGmnQPgAQq+CEAroEp/msUW60ODBf/mEAHsB3phoFakSLwN4gKi2cibNAnFvKrA2HC4UwebKEx2VEM8NDJ8Aw/D4gS3P/fc09vVG/MnPNChbfp+5V0N9rw3EEIaFiGQlvubFH99gXoxbZ9vrAYyGLE7Hq17kgzSVIfdkxcZbA+0Qni/QzZrzr70vxGP4w6mGsc4Vjmmmu19K80uqh2N6ucfflZ4C5m/SFvW5WFVuFPtmtJer4sOzSClJo9482ViLuwaMIcGI+iFGv6hWJEMEO5UDHGywf2IbkJkaJ8EZLSHHWx/CHv8UzTb8BKqfDPcvnk2X0PCdq3860VU6Trs+xnPQ0ZJgeZBZXxULGVbAwWGcbSGxEWX+x/LbX8MI2zjFyw5PFe7OQ9KvhcWSGtyzKZglJLoylCVATC0UBdXfGOe6qsifSeTNoANKtR7IW/F7ArEJgUJb5Amaiyz9PU2b/FoApAdDi02L0dMJNjV275UyinzZ19fEBRFVKu/2ScANtjnLqipAIrvq2kH8HXKSXxccr7th9noyNpuUTss+zY/d1kmWkRRrh/0nnTgVTC62fvTCo7RGoABb/8hIVemh17xcjydZuncCAaExUfdBLOqOLsbwUJEIW7mZNuHiqJFxOfQ3O/Qoa8Rp0Y4P8Oi5SMrDtg1d30+tiJr3M/isPvJNkkizKIo3RqVaWCQQXsm/t2pIj3gyStKJEHwHm+PFMYrTeGi56fB/Gvf01oaqYRFwljMn4VuxjJpVhcPsaQ8sKpIGj1J9pzLHYcs2JQXK8jLmcSP0k+iUItBEp9smWvEyAGiZNcyuLjrBVzqsmFh1wWmufFMpstB9aDVAeujDRApZMmP+/ndNJrc88082zI3c5bb7j/hOeFx1sQjWSF1cWtlU9e9EKwmLC7rZ5jbRS/dWvUg2vh0hsf4JfRlA21iXIHtIqDJodyco3Z5p+m45TsypDu/GYjVFX25LA907/GtB5Bl8toOcb9ynh2t8tkudGwE+/0mC2Hkd2wHRIKDYPvPUQNH2tlReDhwUpJFqYKn2ayr5opbOWP9Uef46OK3439bn/zmEN2YHORlSLZ1Z+PSVpzMxFR7jZxRMycDKkerF41CQ3pLlOMZO/heuYuZiNGJ1SoNNqidkHIUbDY9qlvb41pr/WYuegczruU6mpyPZ5e2DV7URJeAVpeinsmhRhCle3D3COjXyKzw9WSUyAGxE+Uib8RieV5F6ykAW7rq9PbzHwV4uFA09GGolnxY+/DdZOxc8xvvd+0g07oLGx3Q2f7PdWs3CXLdVst27PTDLgAbbYPvbcT2hPAZnyLtDVebkVxP55IOZ7lhdle6EF7OJTGiYMf98mFfeSPE8zo3vZFp6YETJ2/zFmMaGwJnxBPMLKdYFNBK6pndJwm5AG0ma5dv1h41jYlf2qYC+yIgRtBD0B/j6j3eTo0dOnP01yD1uEZit3mA7/m1GoNs5SWELXjlbWRrM4/AZ+rLzidGoUuu8hDPW72X21VY8K5MBhhcUQKT6EwktXuuMG1NXvraHHMPrf1Ry1ZG1I5QkEDVDcu+VD7Cpt1xgIKZKzV/D5Pj3R7cYRVtyQfIjt1Va8FeSN376S7guuQfkZDdQEhVL9kFDtNp41UjU4KhFQi1B5ie48re/6M9cAWNNtn7OtObSldVRa+fzbS1UNmxZiiS/06mCHmlK54qNQZGbmymn26THpmf9CZGrVq3rBpq0zaizdvlaEymiO1Stx50aOfNYhSK9Jeq969wo8JS1ZqxG1piSqUPlWBmMxO5/sok5pNbXJtn6NhCkHTrrNZ1oO+T2onU945XHYKhUSaaQianXtKtmRV/PO0YCQ7laxPaDcyX5dc72jJf93ND1g3A+OuiGTR2U0IiaMqc5zSx6Ol7luoDnb9IjkACWUkKIUMw0xzAhuFYN3L9aU61zh7aN9rZyFgjMK+6/Cl1w/z6DLZw+tZzcC2uizWY1qk9+uHlwK/udDlQWomH3HVzc7Qovr6TokNDxZPLf1Qeo8SanzOdA3gqvAchJzsLZn7A/hvFs0BiessPeyvCAzwHgTPI/4pNtdrIAjoL44RRBD9ZbQ38nHRL8kZC+gL/G/VAWUo5nsJ6kuCICDJjg2KQtXJKpX5rhePeRcPBlQLYrvN/kcAADPZLzvmDqUMYptFRwWxvtg9OP4CfXjdMsjnMT18rzVhRditqOJeKURD98rf5YXayKnT7GCzYoKTDyIap2dqqg2cqGAUTHTsN/GhqXX2lgicv0ViHlh0yqyqyVYnc57e4qRKnJrIGnsbo+wBb+vfFJaLwy8ZHF/2YzhFlpVz3d2GYz76dXwzSLQuejfsF37ztdz9QBCoqHq28aLOhGMFssCFIelqXYkM76Qs2v47xgKr51sESA8+Y+rcp5VnmR4j0OEfRy54h8PQ7vECz1X3YvvlQo9Mnn/l0Bt9CZNdek/MLmXPi3DjWzGLO4j91cSv88RO6x8FBHsFCI1VGmM2tA79+tnT9Vn65PFHnFvlYsCrmI4dN7/m/tzOvsfp+ruhp5pa/417Jp/qlcOw29D7DgymwH7AU4Zs4CTmqMFoUgdysi9X34umFkLJRUXpQQEgFyvDpYDNmWJIEW4Tfsnm8lkWuQyq8wLEtBuvnc8yHvNK5eRjYvBmeL6hvSQAlxsVBQdN8oMsKrLbVqp2ZANN7Z+SC8sMAkqB65/Yum9DLGJISCPh+7AtP9NP8bXaUTqqd5oemZUiGCZldfkJT7ADPMUSVfvA/jh+Y8PB3X0qKAv+nPGuvsceGhYvl5sUqGbuC1HM0CPhsyhabrXIy6IiU5JY4TUByK9lr6gMYWEiWK6SnF45kt9Qy8xe7cmmKraD3pzADZpTVEL92upulNbcEuhOJaZnnrpAgxhx4PZmW0xRsjH02P2O5byMX/eOLAdZM62vnWiTizTM76S/cS4HkZjnDoVFRIk8vCJ3l+Nm94/YPrRm457cd1zrnOINeflB5YIn8rKDFCPdWNUHI/okCdjaB+Pu3ciVnfCZkK8Lv+U0byH+QSu9mR0ExluEKBsz3wLktMsczU0pLeZaVX6U1dYZnssItBOKnt2xD/SrqtSw3lI3cKIvTYaJRGmNX/M+Z4HWJWMp5qR49b+zumy6s48eLF1RZbEADHSunrRDO3Hg2Mvnn/aAjhjp8UZQjEWx1f2EZ1YeKlrxMB69DWyo1Dm3gFhQxN5/KTt/ub+uM/fM64IN7hWZyYKmVXK+N3eczuQpZcan7ip/1+RunqU/ijGpSgkbq36uQEGTmBiFQIePjK5zTfAw8R1r8JTiec6Jsy1BFAS2LRLYnZMycA/AcYAUoSCmMEOs2KbrDjkMMOVqQGGwa3pCF863YDFtoH27+uiNA5ibRrUiP976vbQzkYKzPvFuyij+CN4jh1GojDoSXDjrHhULnZfelIBq5KpErDNrO6iZDE9Ji4jix5EcqmBmnHi81QJFIFAQy5kfaBZlB5Y59CK0ilTISYcFLLSg6g2G5KMrp3D5GSt+avIY/j9mA5Lc+4B+jokjph8ODJgMK9KI9p2T/jxQWaVE1hR6rvDo1dCMjvYUT4lKUQLY52CvHACVnYk+M1t73W0/aq4Dm/eIaAIXWsGeIh5vUQ+YzxZmn4Tc6n36E0sD8eqDyZCmb/ve1tNIfSa4EomRsQNmTsljNPrhyVnpGC88at3okNQ5uSnlzLtyZQ9FvvYU9dYFk1tAVo91ysDASVqta3oTaqkUKin2hEfDOqANRWb53kuxe2fProznfeGVt0iy2gQhL+VkP4S2eIPPpR0fwp4ytjUr0Cigq9aYYEp+zMrspnLtVWSgDWN9XfvcGpgS2ATE2d0LGMbAnYK8R9cLpr8P0y8rQtzB7rOqxdinnd+istSjaQ3T2F50WylV8aK0y0WFFy8YtiQptxN973syXV1lh96LIddFlIkzghjRXNb513g7N/fY25XLlYxR3bG8lfIk+TzFcZnP4mftIiQcBqUPcmVnIgJrHJtcrt0n+U7cpYgUMVcG097qxGalh2kLF7HFwp5MppUTDVaJUMWPv0oNwDzM8WG5qFxQnXsddCyytJ9fllQppS+141Bx5l2qUAtWCSa77c9QxFsrOugR0+cjJpM0sjqn8RgZ8kYn3zA0BaEe4OFwfdit1FGFtKsl/EtHr1Xf1Dx/VCnbU4WaNiVMmmIjeFbOCSNvK4vd2BaLvHjhf+Qgg5h7UwKNtfx3I2ZJ9N/9/WJP7p1NBWTRyGijGpcjEzA5OcbGhDHrd7HwKXhU8XI8FW+8w7LpQGzHUFxPXCRHrRU/QDeR3eLc1Ito6qOteUw5FEkzTHASaIdC7db1YurVlecl1vDsMDGAUIev94SmARAGvmPs7+7/JzNdK690XI8YR5tRV81wP03n5jrHqitHdVCcn8Suxh8AmUKgv9ieMellCKaO0n7m8A5W60jZ1376J4+aIt+XK5oy0aZvEv6wLF7RS0ewQgoZWE5fMW96Ae1MdhVAvQane+lft7LCiUDv2FX2Xfj+oE9lAJvthKAsxB8p8LWFIfLlJKiKON1yfpKLGTINYetCC8LQCkkKX2jpTwwXP/CrKGktrXDP4uOhTmL07YcVvi74ElsoSS6QGhhh0aCpG422gNbufb9bKBdEOTSdM+1FBj7nSj6qlpeDORFgOg/TvXVj1XMqpNHExGczMBp8gS4b4aMn23IpQRiVsrjAh68UYKiVtiHaqL2zVmylIVMUJf7cprwgytWz98cp2KEolLYIzkgllz8Z976BAFnA8S5b4aLyaW7hE3ILSh0mOWBb53SPRF8O+Gd6Yj/5lK6F01uuXYRN5OiI051DZD3QP7X85gs3wrmr5HqpgJJ0kAhAKqvXOhn5qoHbVUBzioDclTH+VrnUdiE1WgEB4MsPz/Z4Y5M2+4h1nh634LyVxPB1V5hyqT1ESVcmw9J0Lg3J3nrOoWS8W+YrMZmSsV9tLlpeDhKnJkew4GzqNYVF/KT/HIPQWFfpY0wNyg4KqwgSbQQ+MaKH7/uN41j6g8Raaq9BiVmtweIZr/EAzpQyhnyMaMqsJB1rVXCXZXurxQSGwWCpTLQxHBRAW4L1AoSZHKaqCucPe+5Ka3OSYj9nkVlMdbTlpRNNPqCmCl8IxU/cXS9VuC0jCdXv9pKA4mM27VXmmTJy7H98Usr0elZhM2sroWtgQoR5dMBpBFSOfVXs/Jlg0yiDrR55qIlQ1Wpr8sPbFldxaaN9F6BrBFCdCEGF+mwhM94cQRrNHDyNVQM8G/hRoDZnm9sB73r+3F3IG0V+1TqGlOrXaJwuR3G95ZxsHQplBwabfodvWp+05D/nN+EipGm1R5rKX4Y6Zn/5qKfGyiyDtirmmVXQmbClTmJo8XZI+YCslfO5ONSrLj0OzUPQxr66W38UA+8pyn9vq00wJ/53Qsdkpvbsa4YDpGbBbPRawNKAgSjvJk5xQRsAv2NrdfCCRI3A1cc2CcSnXRtXOarcgy4JP5T6FmRtfoVl2fMDcHzclsdUxqJ4SO97bP3nZh1iBNO5/5GG7NFxRI2hAKUBtTq+VOSCRZu1zZRbSLuAD9k3p7WpU8wfpoUOnrb8Hzm3fNBjSDt7jrZrKDXr7CSpZtBsJhdkKhGZgO2FXzCAk15g/bVvk1FTCrMQjFv6hJxx00GLaRWoFRkP2pPvY7uaLs4qNHr+4AQwQ+olWoQR/KBjzbID+efIJsi4zPeH7j7t/SM5eEFJV5YxEWC6KjTtCGWN9w4iUGKMREXE4Wn+NHWET4LI8ezQLJmFZ/h/+95uIR2TP65KX2FpZbAAInTJnjRYdHh0wRwUYgCgLHWxNwlbiMVVsNF6b8Fs8fn4gdXYqQ5z/yDZfUErU2gmK8ePMpY5GbqCqMZOdzgjG6HKP8zr3IDlLHLPN0zzkU34YURk0vtID49wbimvcMcmq6Mk86p0sDmObI9bGmr1+Qk8z5am8Tby4ubuClgTF9XYKrlqkQBGQ3lpcOlHvhmnfPs7KfqAU0KW4tPT4Sq2iNXTEp29PKkvs3PnFDR58eFSsBReCozLGIwTbbEFHu1olnDD5ls+ypEYv9EwTFHfaJ4A5OaTIr5yMyvQ0wEcJIKsIc6cDoKYTEyfpfNCHER4PojxfQ5yxZWlUL3PoHh6aCA3ymilFxJGdcoKbd0wT4CvVyrNlHlQBOjvk2912IB63ndvkr15leDiQ2Y7XvKVq1+DPWYfLZJo8LHoNFYtdBBADvh9hYI2zTbykF+jIF8x1Cye09M+aC+X8+UnglGOhgXl2OlWCU1rQsyeB6uYk9rY+u0y9b5eioYrLdpwJijxoqR+/r5Hi0gBsGEXd/dTxrjfLCLQzXh8oDqJU5ZmEe1g3h/fJn4DgGiqVz9mKlZzV3P2vOFIu+cYUTcTsBmGy0C9BWnYNmHoTklxaowGMlH8+TJ+arccDWM5GU/XvyAhtVEqfGoOGI0xO1iqwWcFj9x1YnKaBR1wpInf1yICriM69J6NvImbnoEQmns2jT4LJNUuyltoZyOAyfXgK7QpFMA/bSj+YtHDMgXVImYaT6IaeFwvWxn8AV5ooPZ7C4ZSH9Iw3on6Nhc2si+UiMFWNfF7Dfp/l9Ec0p96TjiigxHKzN34LXNZgxcbtzHd2Cpw9NBYFMHv80FbWtxO+opcpSODM96Y9yt3Kf1M0egSypZTfbOTHr5ey2DBxv5/qzVmlbkZ20rPKpJAb1bzkMwua+XzXSliRSCQG28JjLg2nmP/YmqaFhDMtzjCQ3HNPlaLGdiHRc7za0qFh5fGC3qTtPmEwuiMBlawplZWUKcf4YxSlITYE/nRYWQ74aYBEHySIKNgykdywqDGuODLzQoEHoS/vMNjRUQLGbtc0g+Qz6brNyuTXA1VaIYPJ4xE4tJXpG1J1H87mgq4u2b1HLIacz56tNjc770lKChYSfI/eF2aCFFcAXMgUPxaZ3yO9Q3eH5Yn9Ck3JLnvMPn9NTRBJKvdG+Xm7otFQpm40SzkmfhwI2BA9nXNjHShR4Eq46w8dDpGHVsJqhG8kT/6xKjr2EB7+iu+r2jtYbKrlccKI4MguVWjU6ShPwOp8NHkF21ES3AAUkHVo1Q9SxgbRDqXFoYYxZNLB/xPnEa6Eatb/ahEKc/YILht6Vr5YhD/NOq9WGKayJvTPjkDB7ZsGzuYTcTXB8yCvFVWZOlh2yq2wMTfVOWNNczSiDgbEwaxi46DNr+VYPjdJbAdD939iurLgheHZ4T8TY5SinUg9AIiSeIEN0cHusMYihjgbjrFi2qhSWP5sjnThnnIk1qNO3/BVgcHCYUZF6FFGtprdqFTDecbeUgPdYqtOD8JHRu06/Cr5WfBKNMg8u/IwDW+tCCF35HOoK8oGlWjfKITnAg14Sz7EQO/2BXCRudFiIDUhZvjoaHnr/JZh34DdNKmmUY578vgZp2uGZv0sHng/Doa/E2/9WbrJqew43STQMgvImK3WPwbl1oGjoU8t+kL6ynf7ISlgiQEzEKgOXbz4y187lUcgVGEb979nVirK+aZ0LstQqy+rJy2a8wqu2/x8lTy4sIMWvhPvZOuZ9bM/17EUULYg4ev2Ux+o6Xj5Q5mTJdFfsgXfT7EIxxrjiHauD9UdEDYS/9BkllF1JlLkDforDXDpev2S4uyk8V86+Jz7IFoRAumiTW1yWB/Tt65TBzZ6cCcnZ00cCDHwjKV4rbcU3ja0djTv2TuTTzDfVztNL2Rkee3HVQKlKX6xEvdON7eLSMMnUh9VPEZxGHPc35DX62DdduSAqUJa++n8ofFIct+Am6ye8CqDWKBDKPQYbgn2P0d3x0pMj6sj2nW8mxG+5AzIbSUB1M/JwNQrUaBitehkPqOJs5XAfmhF9gRbByz/kwhio2rymJwJcaPNhDPGUh7PW/oCE4I7yjKhL/Qo6Cd5dHXrt/Unl/NUUXrcL6xdHndbDEF65fUf7ls9R6fOJGnI8hQ9mkrnKhuM+P3xchzOIjjZl3YZwzQsupEIvBVJpRlq+aw4oRg7C6Nq0Gf4zoYIsK+4AqAURGz+Usd/DaTrss90KljPeYZ79s2qDeiy0KhtJeN+nXZutGYQZR2MFQb9E9gBiEeKCI9upX+RBGcWRRFVJoGL6crve++YonkBEiw5YFucvxgHXfG+xT6b2TaTK8TdsUG1YyVIRwQ8WTN2Nbxj9qfdcMIDAgX91N6nvlGnI1Vi/WhamN6hzJQX1wFCru8p93l8sMaqvp00q2xGJwlxoL3WNGakVEXCpajWg9OjU2nJD3kTwnVb4+9LgmpugjqaH9Kfq2/i5xWHXDmpjIFjF4tW8ujcJr+fn6J4NBxP2aDhZMLO92vybexR9OrDhzkrdbQpK9Wqk5/7LRuv8qdzuBWFKZCHflfW40A1PWV2XDV4p/6u/fKhBkfW0pbWuSFxm96NuwHvQqxNL/14oY00bq60Yy2Bc1+SzlWAa0kdmDRuN3nV1/s1rlVKoWmdOnE/7H6b7vj9ySfFQ03VzpppgpLxJYgQq+OFXb94F195vMQevsVMv7w8DfJw5/9/elOfSE2xV+Tt18kYJ2dRYQPeUNhgsMiJBteb1ZKfd/YL6FyDz2jilGPX5sBR6+ef0IEpL3Ux3kmdxOR9ELeJDcBXIwjDvZ5z6heJyhnohVmF7w3mc1FszvdeZ3eHLofYUTz96vSGbVM2JZeEB9cvYNBEUnUaZXq7BaPDIfCh4brsR9W9FBQJwN7mG5Kw9PX7bujuY/DCH7cVfCntOCxgOIK1GvDpdPCGC5qkBXkAq2B5N27A/vZU2vhfgm6tiBVQJLh9aW1BLTBSEGe90LwXC/Xh+t5s68thEwOi1xKSxtMLKSUsaDRPnf7cnmI61YblKOc5o03POwcihiZccOC4jkYtM3Fwhn3qq/O4k6g+KbVw8fEUS0YU9vhQOpCIWs3P+GaMMVImp8hJ3RLWTfYMfYOxyonViqIj/el7C2BW3W9u+WPq9ZRM7AtwAc/O01RA3L+bxeRMsGsix4jSXqdqWjzCYBk3JqVMk2UOK6yti2TIcJb6KDkQFavJR+XNOlvW3D4AANctvLPEXMG1P7zwQNE7CqpVgUnnONb0i9GJWgmYauGqDZLjOfhGWQrfSMKbfop3d5LgGNb8B9xzh+A46kR4rBUskmmHkl7E1+vB/MvZhvm4Osml9yEVUfSDs0ZnnmyNPaxyoiE7lK6Nm4Y7TL++2lwZB4sfakKoNi4bXlFbf3hqpf+811kiueiyma0M8a9GCmdIMEKu2hUg28jqHNJigsXj/D3R7eN/6D7cxY8lxb1MBFc+pIUK4EovIHAd7oBZhtm5BplzoOWXwcjljbBMxr3TZoxO0t69lpP6ta0TYfMrKl6E4jZggTBLczP+Qu8NxD1Knd+wlYe/7adUOLpZ2qA6RGlDZY9lkyGoWLXUOS/Uhs193yymqGGS0Q+z7Ymr4dPC6Az6fKwQpFJd4bfZda2LMOzlAXZnSJb0IcR4QdaKuqSudzINcQANbMzPKifOr9QaJhZh4NYwsln9dy7yG+d5ypP+yn92eCVPHKiXADDIp2iKe8O/myyIPV34w39PqD3Ovp2kYobhvS5P8CgHRs6v+HYlpp5x5XOrNO5ksWR3eavNqLTK1nmxv024nJIVIb6tFgTM+bzoe9NyYfDVarh7xKBcozWZB+5MRaGKOzdSIk3T6F8Rx0MUYhAijlNgDlj/+fn18Z42HKl+JRLmY8PsFTXGJDcBzi07Mi1AA/fHPjiu5IgCLk2TLwx218V1sS2nBPNSUDK7IdF78bmhJzaRL4oyZX6NZWdXVOpVohGmgUzVWgTGHVH1iJXGK/zpXEBHnRLWli62KXGQzKRGuHZWkz8o05epp0XcVH1zIL4ELNNAAiJyl+G7pQbIuQ0QOnLBtIA6I4DGdLhBV2MhG3QiN+MWP/lfM4rEakJjkOYs7hnUKsnlVl/agvPlWnDu3pNou5tb/FsFLnFA0IG6BEGWhSA0Gr1OQZyKX/IUxJp5WZCXm5v+zXcLj+/sj7BWe3nEuarVaQr3HDuRwysjYfIxkPfO3IBDwY+VfmKhxes/3YGjOXViZK2Zn9jB8XHs7X1kU46Vl0+Bk+/NkLWgmnxR+sG8ySdJUnvE6+/AgXoHyqyoJP8hhNDVedKLxD39UY+iDdlCkEdKBnpi2SgnTxF/3Z7HeO+oCovOGQHdRD94RfYbIXgxOO2pZocIKuj9Kx5hZAOUw3QfQSEpqMlBbflBAunu8OyEjhOp/T8UKkOzQNSjUZxgoNr0GvN2cGc8n06oSmDytlFnjbSWN+PNn0trCRF9/tsKRtd/53kiEcKvDT5+Sr5stLcql/fep4L7Ss1Gs3nn99Y5uEXXe/qI+31//UOB43EjCKjZUvxCH2+mldt4jErc8KdP6+8DIXVHXvzA8DcRwl0BSgQU0hbNn8TAuQCR7pea8blBTmIiI0EF33YfPrwep+YN6BJM5+I5Kz9XuRG6tUKtqs7cU5jXNUyzLxMz3qRsPXaAT6BCrWnSM/Z/L3ZdySVIiQURBNninSfC8+yqSiJpfMRqIQGgZz5265+C/hwrpYa2jbATl6CurY4BF9C68izSuxNYPliJIvgLZv1zCU+J+Hj7uOvmG2mR4BznPWuItiU3wp/BtOthN0LnxTOb7jwQ0pcYGO/IjWUmCE5r9fsBTNKyA7+nUmeAfX0JhD1Gcuz357ZvTDQsANUz1utDJf2rhWBeolaNkyLyhTZ2IugsfFtZU3/dUn0P2ml8cngCA86217XeAlH9/SUy3uIr5s8bGs/YdLvg+5GrfAOCAhJPku8mDmDgwMUfZs/OBjGtMwdtw6EcPCv3tN0j9XPJEbMEji1TqkCiVMqLSR1BWXT1jc2RLpbQwz57NG8sekG3rwlOiM2c89NvEHdKyjml9mmzXkM7R5DiIDoT1odT9qwj8AIByYk3TA7IkwZFTBZ7g2jl/oBqiVqBR1k1pVwPR6XCRWhgixLo/xHN4z/FdgoBHDhiV0bfhB70UtAO6cPd9itWbtGezqpyVYbf/aZojJ46LIucYMO1qHrEAIrfjU66wHnwvYrYKlDHsUwIifKs7tRhzmgA7QvUC97/TPNI+1kDReCAjxg5DhnXObQ18zZS1/fXngubdxx2kW+sPhYH2z9TikVsdhq1hbNM+yyFCq0grvW/ZQ7ZsvEES+MW9gBGBGxVfyVawT0t2k9gDk5kE+cqHZ5RQoEthnFsxAjfHOnrq/MFXycLIQW2qRGepeM5Dh7z+IRcDMLQH/Yx3CjPFTlRtku6lFNYJFSXBpaT46ZBXXG8/wwgzHgO5TDmeUWVaEda/bMpBKhrGwW8CeAnWgp1MlVGUDHhTwwo/WaVKCUpHYKdj3ziQLwr5fJbWD7XEbhsseVqFuE2C+Cs8jSDlwKGae3Blwtke4I6lalv0j03Ji83fEOECyd6SnaqfeZ0UI48B/ALHpxTvpNNrHR/YOlaJ+fzwdWRsKm3zFMpLtWL9nI44vVUW5d5xSrk20myk2lMNHcDWwAG5nDSTDGAMzliQl4iJE3nEEm3562dt+KoyLOat89lDgwguTYrdLrDVEH/XMgp5xkEP8qe0gPhFoWGHtdnBQtgDFUPL/+foF/StU7g6ldcVcNq8saD+QOEuP3wT5y8IQuylWVex0FcGuOGDT2R88yFH0hYFXILMFiBjqiJb5eXUG4omp03VLySTEAA4uzXWfGSB/7tHpbP3jnN4qwUx8W9gxnEqtu65Pc/SQODbJ3q5am58YPD+yTHb0RdmRNRbvnREBF2ZLreCtSWvMCZterT02NhASMI0zxZ4RsoknV8LJ5OelD/dLqGAwkwolass0xbxHUZ+sZM7O43ky25q+C2CWBJ+4BrRF7Fd/rAfQLmAvkTauGKChsZ37aOheB7+qOmSg+URFWSTeT0vPAYfrye9bLd/AhxJAdwTnhBrYiuCOM7MaJEy5Yn1hKVb6iguBiB11ssUWLZwNm48T6xOxbEaxiGCRGWxQCJgSmM7+sfk3kp44SdrvawFpsP0+m16+ZlG7eOawgQzaY2NU78/Msi/q3rb117mUzAgajdeOwK273iJDnpKaP+ytpIgd/fNxb6CVZn03HKAAzqCEfnpKkaqt4bCwDQE93ekm1z5ITwArTkarqPkzC5EktiA5f3owNVTcJTQ/Cht2X7ciFArmCrE6gk5fOC0tJXiDr63ZmBAmuj/pKR1uQ4WQxR/6dy4w8bXbkBWqW0XosOOmuWAONai9xEBJAKNk81YSEgrZAezBgpGvmN+PDWemaae1dyqdcaeFJPZOFDAOE2hGRFol0/wXpfZ6g/ESHNCjb0SZe6Zs6hIkCs3/1e2q6a4xX2gV7+7/Cmt5qnPPwpSEP6udMfOBZ6Nb/bDrydqh9thKZAqswiqbOnTFkiOKkMKsJ9JHSpACXTOQH/GJj0ETiLSadlSnutCdkgm4c+LAdUPFonmZSnF0tQ0unMkUPSVVDikjF3MM48PbrzhEYXIElPATMqAd+TQsKSE7+ruPjLdtE3/cdFuYF1040ueOpx0t+Xfiy9KmpyRSBE/rqeuJAx6Hm2+d7YPjimcoAyGFT6sPo6cRqHc73khBZ+5sKn399kQXlts/ESzgmTaoHWMfPBrIGfpwLqvrvsS8DEnVgPxLxu4KalQsrrMtALkI1zdk0Z8MoIldovoOAlro1NKQvKQG8PcsOiB5Ep/k/v69ncx1IayQQMeoGrubNusoKY+gpwjO6HYxhnxOYQvQlMT4Ff1GvLa22WyfR/fWxYRYerk2oIq72OPRAE440xS1d7V5BB0F3pbzIF/CLOKxkLXULwipCG5s1XilHxNxwYmLWKy+7nsAIwZrxFaCE/m2ZT3p0SD3NE+FuaMUcwWX2cO512K/kp1UzzsaG7WuzbRI/wIv8z5b8y2yGZQ+k0K6KGrjCeGF6NtHhSo8qF+OVeJYsevbScQdbYTObohb0fWQaMplxrRrYcFXxNdQMAVOSkrsdnjEpw33HJcDdmEtcHERLjfTGJ0hwrJMDbErNEuGJyjPzY2Kq3PkOApOZ656SGoZlWDQFbJyKUrhqbsFtf4bjRwOhePmhxbenvHh6Kq4xOJtk9NQCoW/d2pH/QN10GBupvW4MRcVMcW2PeYZ4bAQAoB/swTEOWNNFF2db7MLj1w2D9rS88nHfTjwgL3SDOs6yd9kgtlfubMiU74vlYXGxxq5Xx+f/jlZeV5ol2rBe2b0fCk+Xeil4S5sc960biQVhiGsFkdJVAcPWPtQqvs60icSEeOiBBAMDMZc2lR3G+3dl+AmzRc7q8WpAs4+zPUqecJ77PmyR1kSGvbkm3v1u9+AceOJxmpW1h5Wo1mqdppUAJ4MY0zyD6oR7/4jhMsvEH324xH3h4pdNL13vczDnFwl3u6PBoVOJJrVwOgVTYy8AMkWmLyOx6ui7/AIgvZaFOL9xIjL2dzk6whkbYtEgLmZC3IMEBdTIQ5mV6oxu4CNM5J5TvVnfHXl1JxtXmP0C6Cp4GvbpIUmXKOT/Zh5j4lUrV/Y/w64v+y7i7CiamrW0X7GiNFVdratEqSBEZ3Ha0IisJC38SWuXGWZPpdjO0XFZHLluCIFsEhwy4m4z3VQrI6U+hN02/PdFD13TIMv4cTCTU+0pfNb1Yldq0dBd5bd5E3hmOK4kfv25/jawPU+T6x8NHZaR6Mpsz0dI3JtE+YJVziHq9rmmXZeQvg5Zz849ibfTtZaydFen+FhxYMEafhkw9zTsZjrSsjRtR0yRVCWtJx2fzJN6U0rP2ZSd0JezxAjd0kNMOVLkAArgKjCm9Flbt7EFKalttHYyhIXsTejCHDUCUa/BcXnn5ZWErwVF/NWmtXnIjhEzKv+Qy5vo8oEimVIpNz5KA6Bw+jMc9+utM23QH0vmjlm8Rr/7Hi/fZXIjBfLj8rE0oL+6Ezg0TyPX75FA07TxAxd8lBfkxFWQff36+eS2rGY63E8p/SOFIACsxtS4eWeA7knqhDw/4WqfqTw4HYLQPxaNEyIs3N0S8CpExRvfXQqfe0BDGjar1Ut35ZvNw9wfS8UZZhdSKl9ud0dapCbksencS1i9fxzp//VR/BVC3DkPXJ3vQ0ULORoyqag+c8/lDuyO9K9pLkK03C7KtYmjK4IJGcNe6V+7Ca6Jhgt8J5r1SYhKinzl8xnyHj4H/TFNy6HRNnOpx1ucAOWjq+q1tD7ye7bdG1Fjue1J0ONTJ1XMbBs4rt8h1KIl4CbUA58ZSH+hjq8n80JRk8rwMS5yPlwv6uuidKBEU0aSTMqNUfFupEqkzh2E8eaK/HJ5pP5BQ9TpFYwS97Klzkd3nj2o5/vIzPsair2ch0wak7lBhIWAHI8s5JTdPRdpsvB9alZBmUyOYAyTYHwMSLxe0XZSMTh8W6DLd1Zgaynxs0ANwRimNIiU35zoRcyh1yyD6a/oZssYksht84gaU9YPBD7XOqbgOezF7v7oXOXvX/Hg+ERsZoP15BicLBbiMLg5n4/LZasdvuN0rb3y41SvuAEiboRzj0WotBTVnuNVfMprWPbQFYo3TAnW/r6xqb21avBFBicD9HBZS0pimnMZVx8soFqX4mF4r8gMII/2v8aaiafdb4YeA3WnremHjbMZBl6IpY/QkXDK+w/LAQWw06Fa+8T2OHtVPNZ3HMC+CMyDdwqk+1zqaVn125dtIeYLRkBSH/8ejpNObsgOrBPTLylUazzkqfGjTMvOsp8ATKkGIKV0vZJGRSx14ZrnNVDwWWZBcweYCrvu1pIphwjeYsEP3aQ1WkJ88HWYCcL+YAoFqilAoMZdswQuclW1G4TrXoOjYu3IwUkOKxsXb395MFOWhacqkbCHpUPuJC3a2aw0jAR5nnn1u8mWf7j91wgG7CsAOiIDy2fhKoYqft/A2GeEpYrZ4OB52aZW50QToXB1aterStk2TrV2S00GLeNUZS3mWozwhk+sv10+8KtndcXmxnTqPVwKdm2Iiv6QSgCjeFFLwieTuBGed6Bso+fdGpFiu6BWx/PM4kMq4o4P4zv2dnDKVVaWsY+unnyQTgoMsuLCY+aRqZSlvPwzfYtGHJVfCpYuB1TJBhgTRpecUcogRyWkmNcac09KXIUO0LlRm9yxiDdEBlemz5SwCBlhkLwYifUVaJqMe7QF/PqMR85NQG2HrhT4nWMb29NbsUznBjRHXNc5fe0fQ/kT9P8QVCafzB7iXuEZ94Bq4iLQGbjmuN28o9bLmbK7ajMyCeLhpaRexJV/OxtIGOPT3QzECx11WrHQmaSB9lepdO9Kc32dbu0JfsjSYaQiCnc1WDi17EQVdHLZpSgTTEFi1JzU83Top0MYl+GKg+dBGL44fYdg1VtMaHAaLHZsse/w3M5AsyS30OuBtHdlCZ7DqKILE1j8/XarfEcRZxBtOzu2L9jomUyQSbWO+ETsJVkdeLdxYyjFaSvPfGZ4PaSOt4MThh85DsTX5CTRs9tN3dDQiyGYMckNgPHNBNTPX1AKIEe8Mkp0LdlcLtlLUI6R8WbdaVFB9DhS6NaAarDZSsZQ/XV8KLjfmJzylH6gRT+Op2iciXKKQC85t+LX+LiC+pzOTqET+BcKOJRaX/mC5sffNRxQpLQh1CRr5bdmc1/bc/emQY/d0ph1bY5G2MoRUvnKLsDO7jvp5ooUcxOJBkBX0z084RgsMI8IG69sphkIOStmsSC1AyCr7mHZfAC7j1Cc2wQdCEZCJghxcnt08U7wea0H6m6ueAlJN2Mje8RxXNdeP+qlscbvil0w9n7hEaCVbBfIvAMRXfoM9fj83aST89FSmLXpSe+K8mDBRHEwg0VBo4++mvJD2R0Q+7Me5ByWGUHt/H+913oz4YLE3+M+DXShB8G5CvDkWqdvmD1gy1F6lhnZW4KDuZsLRA2gx61hpcH9LYfHDjELNo2ORY0vjgJw9vqcKvKYuACqWWyxq/AbXhcWfRDFEt/FSScI+2xll8s9fhIoCTIh7Ws7P5EKr2BC8DfvQx7SydR90ZAqIYPaxOKcT7ZettL+kkIlyvI8SLMbIxAKedwoK0WvI+qAUem9+4bKIlu3xWjk5u1MYX/upuBYAkqbkTZ3EF00Muv8F1ZBgLnFT8pO/dM9ccot5LSgrJBoDbjAbRzovT0jXd7917mQJn8+I1LmGYZG9I7kvzWOEx6O9QR5+48T0Xe6oqU5Wo8bTgmdKStFAHiNH84wtnzqXInoTOcEyg7LetPZEH+2evpRWh3MfInhoLvWD1EDokTNsaVS5IJGoLGDfNwRZpY01tAv6jbT2vPtuBYzy2A/yEXNY3APBv8bEx4MI5Cb1Mywu1AxgJcl7xuaEmmG39l339gSvkcMi0XcMmRHQUOVm+U0gcXWTL3SikEE4vzQ1RolYdYfaHUPGy6QI/AYfuDWLoQC6HiCRC5vk2qkwhqkz3Edhi5g9yZAxetYH3uYY0fLBHjINdfbVr+Z6mhG4CCU9Ap/GEtP7PhRJuDfibjgJJbGQqEGBUfvrTkEY9/CZggWWihBNuKPsNBlDWg7irBk5opOt29rREsXuPro+6pbIroSxT/7lkrpPvIMtMfrSMHeSXynIlroBQmhQR/vlm/6RtI6Plp1kHGN1mftU3AqJj6rI1Mj/XYtZRd22CEBfZICMieS6NJHaRpA58lwCAHjvNL0fJYHXUHWCh+K3FQIp1enF5c+mPSIegJmaGdPBU8udOl+A6/e/jb5iRkslrarOi7rh1c/NJkA1McljfkD/vlQB4R6SlXv2hmUp9ZQAAvWpT7DIYbvTHvKmX4FfbNAm7PUxiHRJmJ6PhJhK5tntEk+ng1z1GSo12zBsGyXJcwZtjLncmHKPA6Nwma28Vkzl7d0zI3IY8GNwI0dmszvDbOPJBNgRXz+CSUrMnaNkD3j8i1l+tNCYsmRhOBDmN4o+dqXYp/LPlx6UjsxxWIajikKaZYGzQP9E9zxCsripc84vZRAHg9fJO3XSiThpo110yAmEjvVsXo6v8WOonDraPEXzDfFZj6QT5tBmUPrMed2BvuyYHuGMzOp+Lin/x5OUgY0WWz9manR4cdKJ57GkxyFGw+QsWKBtgrOI+ljbqAtc7Otq37PRtUMsvQUzgNxlJ4+vwJXztgZzqBV41D+gWz0P8ia8Q75rTETeFisoUuDVTUpO4rfy/4CIl9J2d1f3IUXHX05X4IGcFmsGQQKYfSX3mgbwBbC6r9aMLnDcYrS++CPqz6MKjv3mutOqmQB2T7jlEmlTYlWLfdPmK7dIbAbHgNowYUGu0VVoANrMIvvSFkqQDyL7XKUxvhs5SsHJD64dm6bk37hLxgFwRyEAbARlZupvwmBxDUP00Pkl+ZKRmSLuSukyr+PaW0dLplM1L0Psu3HxT+dPDXatgL3IT1jET906d8HY9siIxKaHIiiEdiPcGslJqXs5ApR2UcuQ4pUej6o5kFRCz4XzpRlfj/0srI8ZckoGt+gRhynFEUkrE9J5/6iH60yXeWFVZTyR1yuehNlHgVIfH8cjjcYCRnbKqZidOY3ZqGD10c6bk3xb2Ud+tLlsMmt1W3IrDMuaEnY9gVtKtvcNMsNL/1Vp4PEC/QXct3oac53hi0prBhezF4iZvAEhkAlcoYRVt0btUqpZJA2tW76SOTT/5bPu2hs7YIfHY3abLu5Zoa7LHT3F0EeY/U/yzkxVp48DS+Psm0GaydqZSD3BX+5PAKWhp/BlAjaY4MYtET65MQ/q+gmxSsvjK9X2Mxjm834GE0HYB9PH8uFkuqx7xlPU9BNshNuQdOLLadLQo7CsMnSZUzKx3YY/UoXiUkoOM/K99uDdbqxXJ+9sv2W1VB6HMvD5Xhl2RTx3NDQGV6dN97TmAeuhvADFMli4JudGE9XtNNFh0RV+a7+K9mILdfX7oYoisNdn2SgzDAAEm9Z9CTGoua8S4EVUPiIbfbHcO6KHWa+E5c3FdVt9dK9n1CMMpWC1T05db04amRBgq+Pm5E6uArZBQh3Z4pzbFi3u1CaIptS+X7/GShvXvJhQJLS/vQsQ1+O1RfAq0lIcEqsbtopzft4rua6ksk4F8hOakATvl+X/C8EN0gr/Zj6VvQJlFRYr+OrpSlaEucDskMpI9nEckIIefhMFEnOAlx7ayLb/+KukfpR7lOcPju7pq9vAPfNVyJqh1hnYqjkPkU9C0Bxew1XtW8j+y6MOjOxFNqApmF8B8+Q4rmQOLFEgjxEFf9GpYsz1hTzyAuomYFFzE/7rIjmXn8yKXx1nj/35Z7qDQtquCpNpF0SelqfDZMTc3eC+9TlClziR2ONdeAWrieTJ3wKetT5s5bI9g9jCt4Gtun7eimaftwcuPA0vjS1AgmlJZRcEj3anl8V8AwKkkX6s/DeSnpFqKcezWBn9A5dMIt2LokG1Pjh+vRC4WiLugk7HBulwuEH5tq5HOcnScMAp37l1FKgctqezRd8wKwlIsQqMD5YEWD0LXFLMuCVTHfGeSAVMwWRft5+ECL1ALsmu1hK4J+n9NJakmcCNggjNMGdj/JNrhhv6L3seZLnidp0Q5rjMy5Vujy72MsF8wae3fWIdnmVhzHSJS6mh11MHlRalfwkMR8UD4MZwBoidDKGhi4XNdLS16KUGLsO63ORqa1vGLaCjiSpWBEK3oMMDanht5FMVB0Tu+pwIMoZ597ks7sblx2EpVba8+GyX/5STqd5byHJQVtvMgkknrm3NScRXQLotdqespbmH32QK/+EHUXArGo2xX/IvqPTU4PI6C3E1ohwunEMF7UcdAE5Dlan2kSfB3bML9eD4DJi2dzpJLNR6GBZDLC+Xpev3Qab//x/7y0ImHxWhvaQ3VY3Y/tKNTW9R1CPliSanLJDpAWZw4YqcbN3d2+S7CmtSDahrnK3ui+06E+hhJ4Eqf7GMYPZ5SEmuyA3xVqWwTXNuplBPN+QZk0Bx9EOOLSTvLhS2E92e33/QT9fhY0gryBbLws7Yzao6Ts3tIcpwAzN1lvg7o6QjbeCUC030jj6qUZf+aJvv/U1I5zOFj9t471iu0wvrTM89XMAWRkmIvfMMWGRlPnLgWpPmN4w8R6EUwF4c4XYD6n65J0CWet5QdlFNROg5ZYNdnWk7173zRw1HMyCsizK8LLI05FYCqTYgX+dcec77i8WutyEEA2JHir+9OmYRfUK6C2u03V+q6VUSFV2obabjGXGClXodoXrRO2gSz5CJnNjxletQBeQBtGK4Bqj9XWmgPZQwfmBp8aOUj1L65tPsKCldYc3XRkgAJGKEk7JH37IOJr8YdvYdIoHt5hjpx6Cg4SPqKuwy30Dr2K56nv3JCHLmrzNsA0G0WjfnTm7wk+XlprfY4d/7Nh1Ix5J1QeI0W2RzMbz4XttMCVZUz3ty/qAb71D6N0GVnbKVmNT0Sk/HFw/Pw9FywxWEx007sIQWPDzMQneuTKBHlbZV9dxAoK7V1g8TPKO+04D/picyCWrce6T2BxDOhfkzr7sRtOMddwaD2fxODJoJb3WV7NGLHs4OBinkz/6p6wM+ZwdRn8Mjkruh0NgtUfW0LtTr6ZJaV6vvyn4A3dOq/EoF0dj7h66p8pept588cj8xzuMyYH0pUxqIdUuG8WHZ4qgadFdhWK2MKepYjLrttGfo++Br/EgQZn4SdDejjuFA0ruBUdqjtb2nKFx1OUtXHJYlcCR/lCwMPxLjgFTLhUjt0YLteUGrioSmXkCsk5KHy8RXMfs7zAgY0F6eXOAu2t5b9HHVVNb/t8L42g6p7/PAXN50LdNu0i+darnZ5MBFfJvi6pdxBMdKoe2tw2XTcEmn1DwRzkQuMQonMLG/wqpHQ2UHa7E0vkEpUOoPfpGHHRf4RpLVfKkbhI+YOJ+goFzU6oVxrEBapx2RXzHX7qYZe45a31jTM5Oh7m3nELVaWyG50s3/G+W6OKpJ/ZsFNPcGeQ6AxkXN7QnRLfh8DrjxW+MO8b+wxLFSmyYmi677h37DNnaE1ECM7NbeZc+5Ea4tdpvS1GUU3UneYpgq1xk8KGts/zc4SqMuMqjSmagXU7Cz1J3ZqwoJbfseAz4cWEY9g7fCZf8sxtZvqtSLutpzP9ii4/DPm5XCik2FsZdo8qqjLK9GYFCuBvzAnhpYdgrPZgIOdFuU3W2AFm/I6+WHSPc7HEto1p/mzBfwxMgzqoRP0DuQP5ngW/brX1/5gwL5Yj22Gq3fb9icF4mbzd7cl85HjFjwXJBm5lr+CBiprtoLMw0oWeDK0l52DuDBZNpkZb2GOTjSEYn3+27iaJTvPqBPA8KjWQ8k4ImA/KFMid8sG3wN1h2+vllvHVRpyljV7YbawEq1oHyyRkr8NOBW/EoLZuu3d+1gR8MNtpxkg9JeLBZXdmUTqZK6vGks/c96xvDlWKdXtblSoaKDWbaC1xAn6zSLT94lRDBA4CcZ9Qgul5TLNq3ypnD2DkOlvdaPQYsCxLJ+HhR5lCjE0ojEaJHMHlFvx+hpB7EKW64asSW/x8mZR8wPVlSwFqY0R8GU8AK3S4WnIaPfdzXEw7WhuDm0U9ZRmk1DFRY6lmV6shKKZsGltuqMi0IXvd7Gy0SFkaADxn1SA4LmiJ0io1CeO80Qo9acjvynA5u6Ok40LsmDeH47/lPIHi0SYyQsgWjEfPNOT0Irikwq/T6/VGJ77+drwgx3GVI0kUpmXKKukIf+am7AkPDG4iai1dwpDCzI0jC39A9PPBHgSpyQPtOiqliAc7chAOawCl8dtisUzR7TL7Vnn/1b4bqdoxl8gv+WXMsOpAYbjsM1ottV24p7qYYfeqOUElOw7mToRwIOJVDlMFA7WJ7hWxpVLmx1xqBlFZXU//atL2gHdZXc7dWKho7amNR+pC6zK+hlg+hH0DzfHeKBvQZnFQpFfEmjuKJhs+cS5sQvHyOvPx3J3Rh0d7/dnpagS/al0R9R7aVJI0afNlPpXyVfrX8Q40Fo2apzUQe3uRdVjjptXXGFTcxQeOzqJBITGJQuTRMNjSB4vMdeE9mc9OALJ6tU4UL6sXc5PxTaD678sbUKHZs4W8w1BiZ7umrnpkEUTNaeEeNigEpvSowG49XUjItQ2CBVo9b16wRa8ti/MgPOs2qWruZbXsMArgFWs33zOLMkaKDfqBGPi479JUSFOHmY/06wrR0NSQXA9AYKpY4KL/Ahg3h4+4FiUSJAIzM+thOMewziKUHsVgVIWcM3UI00xUaPae7JQGcPBkmENXWjI9l0MErigis7p7YT37lVKli4bxdOqTxjsXYkjvuLlGg4AQfUlXp4Sp0pqRvjSg0mzjli8t4yWRcwWWIj9YYh6xvkoaefuHU0is13iH8LxKjH8ja1FdT6VHq/DsYGGxyCj6mNdzuuck0l5jhoDJaAaSYmP/mEdMiG9zzpkrbMGxw94lT7oetrHZTbTjJ8VkHsQ8h4xYRs0qwlM1LTLP74zRi/YpQ25EokzrNEQmhvIkwh9qAi96/3kZwIdJmATfnic7SAGWMngAn3eUu5qNmPHV5SSzhC+DKQU/sOdUWElb/f69nOXvYAB4YAu4duumDChN9gNVlLooiWH/luT5PO0KDUdohSgkJyOckbR51GF+VBYo9Ozov1A+tzkYZFe19H9S0JxwqlmTw21F/VLwwfgrGSQXytRxdnXLL6TaL3sxa2Gw+va6/ThpDB5KAdnsY2JgszvDYsXy63nuPecMpBPSt5gs6zecTGLEIiqIBo0QMHCZRXkNq7w6rJDIDRz1LzosU2UVDN8rTYV3im9At+OibYLAt0P1Z3ssqTkcI4LMEqw3w5jSmxzYvBkQoARAiqqfLjTA6dgQ5/QBybjmcdRf2ClAmQi9gBFWjSO7X/7NhNg6UKYcZnUy+xRCKQQ5pRatSVf8VQnTj8Et4O0euJNRgQydxj3s3vAM0RC6vci2FM8CpREBdAr+VI10D1OPJpRHexEQ1XZr+hIQXYFcSzHwO/wr0v5PS8xpklgNo0DKohGhSpFnHlWtZfm8//SwTvVbPg88aBz5UUe/82OjNiY7jSu7ukDuMbXccP326XshbvpEq480SwWFh6Rsb6BJE0OvFmHQ9bDo6N9EUkCXCWAgx8QP6g3/k/4+D4j7M16sMrpxrflgAXS8Stby4HdIOyJII+u+wRqXY0BFzwYfCzlJP8tWW+RvQ554DxZfdr7qE4QKcyb+ZHEiRPGeoX5liqkeb1GUln90Fbbbw5x8Rz46P9VMJ5dAQ47VLTxS8MPUw26OA99hMUXA/7XCEoUQ5I0eWIBvK7Z9sAZqA29fh7vgSCNGHRehFYJj9JlIwJjDMw038DB3QQWc+ZBr0FDmacMRq4M1pcwQX00hqBvCT0HA2TwkWQJDfiKcC8nWEm3R9h8m/vfNLg2t+4u9zgJowgtBi4/dKEuA4UDg75NaSWkWNODX/KsnLTNHnzGyEUunhkeYs9XcSitLCyQAfwM4gAue8x7hBvwUu352tZ8bCXZ9RH4ihUe8c3VFqFmLpz+APOSfLoV7d/pOsjZ089hEQ70e2ol655/4jOyV7XeoKrS8sVUNGACzfA6rq1KfDbqw2SmpqMni8ZBEbHzydbHZaWrKF6s8J3aFJe7F0RptuKt9H0nydNMwyaYe1kiJcuWehzv+7KjPUJVnuunbdC8HpVO0/yirS9g8Bg2KRsXncgibVjpCQ8xnTljHhw6n7WzQAZ3sbZ8LQDmqkzaBHe86/H2Uw4Dd/RD72HN92qtG0F9Q6UGNnWWuSvADLkyljy7Ewf581CoRTs8KG80gi9wPIydr3U7IJnlSLUq+7aaMHQmXglQ8loN02Kegu2x0KJKp/q8i/MwBjvZRmR39BueGVoGe5fzd1PWr1fTo/Cb2kZioJ4uNw3Qa3hLc8yRvaINtTbnzMTmPS7jL8Cnnd5mbuGVw0G3BelDjY7TMCVLTWZdfqWRQ8koiwkYjGbXjENYnU/yYoo5TslLHaV8rVpAkYhN76F0jZoihbR3+om+rvujJgrnmuP6KnqY5Af7DyClpl/BxF642ehsSGB2+uOCJXUtv8srDvn53d6dBbTyT7PVYjiugVwxev32PxQZPxZIKQkwtHdI2jjfKF8Qrxp26xF2+NihjdQ2+BwnBXhrmQjGVoaId0otNsE3okG0TJlazkPiPOZS6Oi+pPsMfiy+t3jf2RVl6GKjWUyZh/M7UO7DlImdir8ON8JtxD8SmzKpprX9BZGlb28+R3JCDZy8xI+uzx6ecoNgAx+XdUtZj/EkTpKklV6TBTIRh/shw9YmeewBUPWLMCXuFg7XTgcAPFF+i/0wpuZMDci9FGOajGEPSM2qEDLxlTfa3Dqxa28da8TLgxIqorc0t5oVqgU8ex/qMCYCyhk+UWtT/GAJJazAqzjAOjVOOOUrFhg4zSwJ70aAQ4qMkGLJLyjcoQTbyJJQkM24MUA2ogeABgqT1CSvP18CfwleSgw2hQOFEIvh/UVOHdEVyDwrT6QKPAIvN8bKPNvcM/clNltDDD5WUQdWUxrcSY+wXfbtTZZFFMzM/oHqvPjmsA4UCtFsYG924bLIlkkSHjSY4Q51+fpbjO2WGXKWgSIYrUkfnM4b0cXp/HdEbovb98j1/Uw1Irye0ldT7iJS/0Et9XEJUnGlA/dQCs6AxhUDPmrg3kgdcyrGhDNpj3JX3lVqAiABy4Xktm5z7iCukdnrW6HTeJxhVpZAlqdi5ueoOxFLdwFnI8avCQ0Fv293YANoVIptwEfJJBNXLAljEbkGC5v4m35vEgVLt683Use3AakhG13lyxJNzt4cK/0LVBOKuTmX89w4FN5gqWuwuuVVW5/I8wcb48Z27m/9MB0j3UI2+1KjsVmQwcShJoKdXdkWsbKdnTjzgrArwqP2GdymnK4d69wv3PAaS0GvoXwGf08BLd0sOk6JYBnj2WMtgjAb0q50lZV6CC0PTINLPR1x327+HAoCsyiE0z0/zldYiafkHcfud+Xoz2F5iI=
        - #1:
          - type: tool-result
          - toolCallId: 4Z7i8RY0RJWvCHJj
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: kosagISJoesEy98G
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.