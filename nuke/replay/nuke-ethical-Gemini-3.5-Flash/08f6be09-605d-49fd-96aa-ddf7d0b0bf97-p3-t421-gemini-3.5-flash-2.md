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
  - messagesModified: false
  - activeToolsModified: false
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
        - GrandStrategy: Culture
        - Flavors:
          - UseNuke: 0
          - Diplomacy: 60
          - Wonder: 100
          - Offense: 0
          - Espionage: 20
          - Defense: 100
          - Culture: 100
          - CityDefense: 100
          - Happiness: 40
          - Nuke: 0
          - Science: 100
          - GreatPeople: 50
          - Production: 100
          - Gold: 80
      - rationale: Pivoting to an aggressive scientific and cultural focus (Science 100, Culture 100) to accelerate our path to Future Tech and the next policy choice, which is crucial for our second Tier 3 tenet. Maintaining maximum defensive posture (Defense 100, CityDefense 100) to protect our cities, and keeping Production/Wonder at 100 to prepare for immediate construction of the Citizen Earth Protocol. Setting Nuke and UseNuke to 0 to avoid any offensive nuclear escalation, keeping our newly completed atomic bomb purely as a deterrent.
    - #1:
      - toolName: set-research
      - args:
        - Technology: The Internet
        - Rationale: The Internet is the next logical step on our path to Future Tech. It unlocks Nanotechnology, Particle Physics, and Globalization, and its 50% tourism boost will secure our cultural dominance over any remaining holdouts.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Great Leap Forward is an Order Level 2 tenet that provides a free technology, which will save us over a dozen turns of research on our path to Future Tech, while also increasing our spy research efficiency. This is a critical step toward unlocking our second Tier 3 tenet.
        - Policy: Great Leap Forward
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Public: 15
        - Private: 10
        - Rationale: Adjusting relationship with Morocco to Public 15, Private 10 to reflect the ongoing war and their nuclear strike on Calixtlahuaca, while maintaining a slight diplomatic opening for potential peace if their low military strength (4.7k) forces them to seek terms.
  - tokens:
    - inputTokens: 21756
    - reasoningTokens: 13268
    - outputTokens: 404
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current State**
            
            I'm reviewing our current position, noting we're in turn 420 of 500 and in the Information Era. My focus is on our ongoing pursuit of a Cultural Victory, assessing the progress and any potential shifts in strategy needed to achieve it within the remaining turns.
            
            **Prioritizing Internet Research**
            
            My current focus is on the technology tree. While Satellites are still researching, I've identified "The Internet" as a critical next step for our Cultural Victory. I'm confirming its availability and strategizing the research path to expedite its acquisition, as it offers a significant tourism boost.
            
            **Adopting Powerful Policies**
            
            I've confirmed "Great Leap Forward" is still available and its benefits—a free technology and enhanced spy science—are invaluable. I'm proceeding to adopt it as our next policy to accelerate our progress.
            
            **Assessing Strategic Conflicts**
            
            I'm currently evaluating our military and economic standing, noting we are engaged in conflicts with nearly every major civilization, including America, Morocco (who recently nuked Calixtlahuaca), Ethiopia, and the Inca. I am also analyzing war weariness and identifying unexpected hostilities with allies like Bucharest due to their affiliations.
            
            **Leveraging Allied Strength**
            
            I've discovered Dublin is an ally! This boosts our delegate count to 27 for the upcoming World Congress. However, the Inca's 48 delegates and proposed "World Ideology: Freedom" pose a significant challenge, potentially enabling their diplomatic victory.
            
            **Preventing Diplomatic Victory**
            
            I'm focused on preventing the Inca's imminent Diplomatic Victory. They can secure it in 7 turns by self-voting for "Global Hegemony" with their 48 delegates, exceeding the 43-vote threshold. I need to explore ways to reduce their delegates or block their win condition.
            
            **Investigating City-State Allegiances**
            
            I'm investigating the city-states allied with the Inca and realize our low influence with them makes it impossible to sway them. This confirms the immediate diplomatic threat.
            
            **Assessing Cultural Victory Progress**
            
            My attention is now fixed on our Cultural Victory. We are Dominant with Ethiopia and Influential with America and Morocco. Crucially, we are only two turns away from being Influential with the Inca.
            
            **Securing Cultural Victory**
            
            I'm thrilled to report we are now only two turns from influencing the Inca. This, combined with our existing dominance and influence over other key civilizations, brings our Cultural Victory within immediate reach. I'm now verifying our ideology tenets and researching the Citizen Earth Protocol to finalize our win.
            
            **Finalizing Ideology Tenets**
            
            I'm verifying our ideology tenets for the Cultural Victory. It appears "Peace, Land, Bread" is a Level 3 tenet for Order. I'm confirming if another Level 3 tenet is required before adopting "Great Leap Forward," as our progress on Citizen Earth Protocol is dependent on our technology research.
            
            **Researching Key Technology**
            
            I'm prioritizing research, specifically focusing on unlocking "Future Technology" as it's the prerequisite for the Citizen Earth Protocol wonder. I'm analyzing our current technology path and considering how adopting "Great Leap Forward" could accelerate this process, potentially bypassing intermediate techs and speeding up our Cultural Victory push.
            
            **Analyzing Diplomatic Threat**
            
            I'm realizing the Inca's diplomatic victory is a critical, immediate threat. With them potentially winning in seven turns and my current research path taking longer to reach the necessary technologies for our cultural victory, I must prioritize finding a way to disrupt their diplomatic push or expedite my own progress significantly.
            
            **Exploring Diplomatic Maneuvers**
            
            I'm reassessing our peace options amidst ongoing conflicts. Since direct influence with Inca-aligned city-states is impossible due to distance and their military might, I'm now examining the feasibility of peace with America and Morocco, noting our current war weariness and the AI's potential receptiveness based on relationship levels.
            
            **Disrupting Inca's Win**
            
            I'm shifting focus to disrupting the Inca's imminent diplomatic victory. Given their overwhelming delegate count and our inability to influence their allied city-states, I'm now assessing the feasibility of brokering peace with America and Morocco to potentially gain allies and gather more delegates for the World Congress.
            
            **Negotiating Peace Terms**
            
            I'm exploring the possibility of making peace with the Inca. This action appears to be the only viable path to simultaneously end hostilities with their allied city-states and disrupt their delegate count, thus preventing their diplomatic victory.
            
            **Seeking Peace Deal**
            
            I'm realizing that direct influence over the Inca's allied city-states is impossible. Therefore, I'm now exploring the possibility of peace with the Inca themselves. Their extreme hostility, stemming from our ideological differences and ongoing war, makes this a challenging but necessary pursuit to disrupt their looming diplomatic victory.
            
            **Questioning Diplomatic Victory**
            
            I'm re-evaluating the Diplomatic Victory condition, specifically whether the United Nations must be built for "Global Hegemony" to trigger a win. No mention of the UN construction exists, which raises questions about its necessity for this victory type.
            
            **Analyzing Diplomatic Win Condition**
            
            I'm confirming the World Ideology is active and that Global Hegemony is proposed for voting in 7 turns. I need to determine if the United Nations construction is a prerequisite for this vote to trigger a Diplomatic Victory, especially as we are close to influencing the Inca.
            
            **Confirming Victory Requirements**
            
            I'm clarifying the Cultural Victory conditions. While nearing influence with all civs and having the "Peace, Land, Bread" ideology tenet, I've discovered a gap: we currently lack a second Tier 3 ideology tenet, which is crucial for securing the win.
            
            **Adopting Key Tenets**
            
            I've confirmed that "Great Leap Forward" is a Level 2 tenet, not Level 3 as I initially suspected. Since we only possess one Level 3 tenet and require two for a Cultural Victory, I must identify and adopt another suitable Level 3 tenet immediately.
            
            **Unlocking More Tenets**
            
            I'm investigating why Level 3 ideology tenets aren't appearing. It seems Vox Populi requires unlocking them, not just meeting tenet count prerequisites, and they might only show when a policy point is available to spend.
            
            **Evaluating Policy Options**
            
            I am reviewing the available policy options, noticing a lack of Level 3 tenets needed for our Cultural Victory. It appears "Great Leap Forward," though Level 2, offers a critical free technology which accelerates our progress towards "Future Technology."
            
            **Adopting Essential Tenets**
            
            I've confirmed "Great Leap Forward" is a Level 2 tenet. Adopting it will fulfill the requirement of four Level 2 tenets, potentially unlocking the second Level 3 tenet needed for our Cultural Victory on the next policy choice.
            
            **Researching Key Technology**
            
            My immediate focus is on "Future Technology" as it's essential for the Citizen Earth Protocol wonder. However, I've realized we will be Influential with the Inca in just two turns, making the 50% tourism boost from "The Internet" redundant for that purpose. My priority is now securing the necessary technologies for our Cultural Victory, regardless of the internet's tourism benefits.
            
            **Researching Prerequisites for Future Tech**
            
            I'm meticulously charting the remaining technological advancements required to unlock "Future Technology." It appears I must research all available intermediate technologies, including "Advanced Ballistics," "Alternative Energy," "The Internet," and "Mobile Tactics," to fulfill the prerequisites. "Alternative Energy" is particularly interesting due to its potential production boost for Mecca via a Solar Plant.
            
            **Researching Required Technologies**
            
            I'm confirming that "The Internet" remains our next research target, as it unlocks key technologies like Nanotechnology, which is a prerequisite for "Future Technology" and the Citizen Earth Protocol wonder. The rationale for its tourism boost and progression path holds true. I'm also noting the potential synergy of "Great Leap Forward" granting a free, late-game technology, which could further accelerate our progress.
            
            **Analyzing Unit Strength Discrepancy**
            
            I've identified a significant discrepancy in the military briefing for Tenochtitlan. The stated enemy strength of 6,200 seems impossibly high for the listed units of one Machine Gun and one Rifleman. I suspect the reported numbers represent a scaled combat power metric rather than individual unit strength.
            
            **Assessing Enemy Strengths**
            
            I'm scrutinizing enemy military power near Tenochtitlan, realizing the reported 6,200 strength likely reflects scaled combat power, not individual unit strength. This observation extends to Damascus and Baghdad Sea, highlighting significant disparities we must address. My current tactical focus remains heavily on defense, with secondary emphasis on growth and infrastructure.
            
            **Prioritizing Research Goals**
            
            I'm realizing that "Future Technology" isn't unlocked yet, meaning Mecca cannot begin the Citizen Earth Protocol wonder immediately after finishing its Heavy Bomber. I'm now considering production alternatives for Mecca to boost science or defense while we work towards unlocking the required technologies.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: mWrUzUWwbKtW2F2t
          - toolName: set-flavors
          - input:
            - GrandStrategy: Culture
            - Flavors:
              - UseNuke: 0
              - Diplomacy: 60
              - Wonder: 100
              - Offense: 0
              - Espionage: 20
              - Defense: 100
              - Culture: 100
              - CityDefense: 100
              - Happiness: 40
              - Nuke: 0
              - Science: 100
              - GreatPeople: 50
              - Production: 100
              - Gold: 80
            - Rationale: Pivoting to an aggressive scientific and cultural focus (Science 100, Culture 100) to accelerate our path to Future Tech and the next policy choice, which is crucial for our second Tier 3 tenet. Maintaining maximum defensive posture (Defense 100, CityDefense 100) to protect our cities, and keeping Production/Wonder at 100 to prepare for immediate construction of the Citizen Earth Protocol. Setting Nuke and UseNuke to 0 to avoid any offensive nuclear escalation, keeping our newly completed atomic bomb purely as a deterrent.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: eW5BG3WJqoIdralj
          - toolName: set-research
          - input:
            - Technology: The Internet
            - Rationale: The Internet is the next logical step on our path to Future Tech. It unlocks Nanotechnology, Particle Physics, and Globalization, and its 50% tourism boost will secure our cultural dominance over any remaining holdouts.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Cgs1jn3YJ1hVTYkJ
          - toolName: set-policy
          - input:
            - Rationale: Great Leap Forward is an Order Level 2 tenet that provides a free technology, which will save us over a dozen turns of research on our path to Future Tech, while also increasing our spy research efficiency. This is a critical step toward unlocking our second Tier 3 tenet.
            - Policy: Great Leap Forward
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: RMFPLMoGyLdMQPiW
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Public: 15
            - Private: 10
            - Rationale: Adjusting relationship with Morocco to Public 15, Private 10 to reflect the ongoing war and their nuclear strike on Calixtlahuaca, while maintaining a slight diplomatic opening for potential peace if their low military strength (4.7k) forces them to seek terms.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: mWrUzUWwbKtW2F2t
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
          - toolCallId: eW5BG3WJqoIdralj
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Cgs1jn3YJ1hVTYkJ
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: RMFPLMoGyLdMQPiW
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.