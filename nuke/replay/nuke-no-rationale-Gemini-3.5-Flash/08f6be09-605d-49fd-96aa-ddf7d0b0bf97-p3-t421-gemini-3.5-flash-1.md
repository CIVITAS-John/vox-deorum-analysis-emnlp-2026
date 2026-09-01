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
      - toolName: set-relationship
      - args:
        - Private: 100
        - TargetID: 0
        - Rationale: We are very close to a Cultural Victory (99% Popular with the Inca and Influential with everyone else), but we are currently engaged in a multi-front war. Maxing out our relationship values with the Inca will dramatically increase their peace acceptance, helping us secure a peace treaty and safely turtle towards the Citizen Earth Protocol wonder.
        - Public: 100
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Private: 100
        - Rationale: America is a direct neighbor and currently pressing Damascus hard. Maximizing our relationship values will make America highly receptive to peace offers, relieving critical military pressure on our western front so we can focus on building our victory wonder.
        - Public: 100
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 100
        - TargetID: 4
        - Public: 100
        - Rationale: Morocco recently nuked Calixtlahuaca and represents a major threat. By boosting our relationship modifiers to the absolute maximum, we maximize their peace acceptance to end this devastating conflict and prevent any future nuclear strikes.
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 100
        - Rationale: Ethiopia is the Inca's vassal. Aligning our relationship values with them will ensure a smooth transition to peace once we resolve hostilities with their master, stabilizing our eastern flank.
        - Public: 100
    - #4:
      - toolName: set-research
      - args:
        - Technology: The Internet
        - Rationale: The Internet is the ultimate Cultural Victory technology, granting +50% Tourism to all cities. This ensures we stay dominant and influential over all civs while we work on our final victory conditions.
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: Great Leap Forward provides a free technology, which will let us instantly secure an expensive late-game tech (like Robotics or Nanotechnology) to reach Future Tech and unlock the Citizen Earth Protocol wonder much faster.
        - Policy: Great Leap Forward (Level 2 Tenet of Ideology Order)
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Wonder: 100
          - Offense: 0
          - Gold: 80
          - Growth: 30
          - CityDefense: 100
          - Production: 100
          - Science: 80
          - Defense: 100
          - Diplomacy: 60
          - Espionage: 50
          - Mobilization: 0
          - Culture: 100
          - GreatPeople: 50
        - GrandStrategy: Culture
      - rationale: We maintain our Culture Grand Strategy. We keep Defense, CityDefense, Production, and Wonder at maximum (100) to withstand attacks and prepare Mecca to build the Citizen Earth Protocol. We increase Science to 80 to speed up our progress toward Future Tech, and raise Espionage to 50 to protect our research cities from technology theft.
  - tokens:
    - inputTokens: 19513
    - reasoningTokens: 6758
    - outputTokens: 541
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Research Path**
            
            My focus is on evaluating our current research trajectory, specifically the completion of Satellites and the subsequent tech choices. I'm weighing the immediate benefits against long-term strategic gains for our Culture Grand Strategy.
            
            **Selecting Policy and Tech**
            
            I've confirmed "Great Leap Forward" as our chosen policy. For research, "The Internet" is locked in, crucial for our cultural victory push. I'm currently assessing our standing in the ongoing global conflict and our cultural influence progression.
            
            **Confirming Victory Conditions**
            
            I'm double-checking our cultural victory requirements. We're almost influential with everyone, and I need to confirm our ideology tenets. "Great Leap Forward" is a Level 2 Order tenet, but I'm scrutinizing to ensure we have two Level 3 tenets active for the win.
            
            **Prioritizing Future Research**
            
            I'm re-evaluating our tech path, specifically the trade-off between "The Internet" for its tourism bonus and "Alternative Energy" to unlock Robotics for the "Citizen Earth Protocol" wonder. This decision impacts our cultural victory pursuit.
            
            **Deciding Research Priority**
            
            I've realized we'll become influential with all remaining civs in two turns, making "The Internet" less critical for that specific goal. My current priority is confirming the tech path required for the "Citizen Earth Protocol" wonder, as it's essential for our cultural victory. I'm evaluating if "Alternative Energy" or "The Internet" should be researched first to unlock the necessary end-game techs, while also considering the "Great Leap Forward" policy for a free technology.
            
            **Defending the Realm**
            
            I'm prioritizing our defense given the heavy attacks on Damascus and Tenochtitlan. While our current defense and city defense flavors are strong, I'm evaluating if increasing mobilization is necessary given the pressure, despite existing defensive construction underway.
            
            **Determining Research Order**
            
            I'm re-prioritizing research. Since "The Internet" is no longer immediately critical for influencing the Inca, my focus has shifted to unlocking "Citizen Earth Protocol" via "Future Tech." I'm now evaluating the Information Era techs, specifically whether "Alternative Energy" or another path is the fastest route to "Robotics" and subsequently "Future Tech."
            
            **Choosing Research Path**
            
            I've confirmed "The Internet" as my next research target. This decision aligns perfectly with the upcoming "Great Leap Forward" policy, which will grant a free technology, allowing us to efficiently pursue both "The Internet" and the crucial "Robotics" for the "Citizen Earth Protocol" wonder.
            
            **Reviewing Strategic Options**
            
            I'm reviewing our current research and policy settings. "The Internet" is confirmed as our next technology, and "Great Leap Forward" is the selected policy. My priority is now to consider whether to make any changes to these selections, or maintain the current status.
            
            **Improving Peace Prospects**
            
            I'm now focused on improving our chances for peace. Given our current war weariness, I'm investigating how to strategically adjust relationships with belligerent civs to increase the likelihood of peace proposals being accepted. This is crucial for shifting focus to our cultural victory.
            
            **Assessing Peace Viability**
            
            I'm re-evaluating my peace strategy. Morocco's nukes and America's overwhelming military presence near Damascus are significant concerns. I need to assess their war weariness and our diplomatic standings to see if peace is even a remote possibility.
            
            **Improving Diplomatic Standing**
            
            I've implemented significant relationship boosts with both America and Morocco, aiming to facilitate peace talks. This proactive diplomatic approach should increase the likelihood of peace proposals being accepted, allowing me to focus on our cultural victory without further conflict.
            
            **Adjusting Diplomacy and Research**
            
            I'm maximizing diplomatic relationships with the Inca, America, and Morocco to secure peace and end our wars. Concurrently, I'm confirming "The Internet" as the next research and "Great Leap Forward" as the policy, ensuring rapid progress towards cultural victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 5zGueEDSw8ZZAcSd
          - toolName: set-relationship
          - input:
            - Private: 100
            - TargetID: 0
            - Rationale: We are very close to a Cultural Victory (99% Popular with the Inca and Influential with everyone else), but we are currently engaged in a multi-front war. Maxing out our relationship values with the Inca will dramatically increase their peace acceptance, helping us secure a peace treaty and safely turtle towards the Citizen Earth Protocol wonder.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/y4ZYpeZpLz2sWVx5Sz4Mt8FysVog9A6BOgjk6OHzs71ieifsG6f+MPJxCjNQdOE7Rd1+hXVH8mfWtbuKtubK13Ooazqlsrz24UwYpfFof4wwF68zoPvBot5ZkZ0urH3Tvk/t+AtAciEmeuaFvm+kbX+tZpw1hNTMMlzyv+TQxr8WN3FQluZca33Q6U6pBfS7/VSzqtBk7tuWNIuOQ/SpzBDLwUY9nM5V8zvjCRkcvJUJa4tOG3B/04ZAfjl6Z6qcTnmsR3FkjGAWEvdkwrelTy5wzfvRYNjKvctwdwoOdh4NVVbb48oFk4oehpGA6e383dm1GOLgplGgX7BYTfWUSKhAxYV4FSvHGELzM+wKYzLVoXts00XqL8kSaqg6uA993Wr22Xuy/kbKniCiqY08MlnKNSRBd/C634IR3H1w15MAZNDgAzhD6ExR38JQ8mD60q3kVKcXY9ORZ72Cs2qix8FaUlTZGaW6wBtScSNUW63AyOSDfE2UxN5Hzm3qf/ITDG1ulXm72k/WinVi2u5SgWIN/04spH+c+e9HDASnV/8tru8B27nMLF27WoeKjrNoHtXK5JbfMepllVaAaK6r+ZKA9E/22SLcL72/LfLdeg/4DxJEtM14qUcfa90qRFsK1iMXvjZVKRyNEh5e8hNUgv1n/PL1xIJneU/9dKgUgr1Yc0eJGv3sLf2unuY76w2GvvWcPSxnKLMIOQbcBDgjDs0HYQGx2b0hnyGSkxBe+QyJzvJ1/hy9UcvwakzsVFE1M1y8EzBjgivOjiWQi11UlSlmVO3sWyz0b1T48YKEz8+K3nQD5ru5N16f8UCbrr79ln2eTRH+gBhrrVRa1vR9iegac2+hCwgahIY1l98jab/RoUwb+ZIp0OoEZYErQp/DzpQi1bd0jbcumYUDRYMPlI0oN7E4XZKGo917nj6arkjsMggvzKf8tmJRFU7QVmftr7U47zwNMImS56vEw+r5UAjEjvgVFMJEZjpqvba9gvlbX9TEVRvSoS5GJ5ctb1MyrFkS1O0YzwW3jx95G+PiSeV6gxKw0j4R05mnl4OHE7RoabPGe88yVYidZeQId7/l6oHdz+COJDRewkvr6m5VaIwICi0hW0z5MSSp2Nzb6EPep8jRbTYXdhvnEX9GbR5u6ojek/5ykStY8HADFzNtQ7Q6k/sZzUgHqz4PJdlmzgS/CQJsr0AVf9DvTJyk+9G0xElQySy2bLkks+fiRn0eWtk117vHu82eyoYeYSgV6se2A837bDy4Ct725TjOOAwwrb9Xe9yQUQ5Bke3pQ1boNbvRzWMWjOrwc91gM0d0s0nAWuQNkpNBPScsmELdl9GKZsd1DqVKfPoOn5fuHsNWppiQQkGUH+rjKm+9EuXDP5JeyW2bo3fwIu37xslQgmhDx6kksfYQ2tgBDXhklcT7pNO9I1TmjHs0mv5V9B92aWFKpsoqE1+7gNM4slCgiDLX37z2lJ6hY6+x/F78CR//SF1G6oBlhhFPwaziY/lckGPskxvPiHJmEtsGda5oXLfbh8cswFuXcpU+4kHwAzIsdl8/zmNaSK1mqCtTFibNA+itYNOTxeQTH7jKNphpkY8PNjGcTpkt2PLUWW6OLI93oFpqa8jxcSv+CHz55UTA9q7W7sNcz8v94VrGGW0tlUZGbzIDr/j+A4+Y2PsAG1LlikBS/J6nNKOGh8oTUZ4AZV7DORVJR2eLuihkpdv5cbsh/jyV0g7ywqFqcPl73vnDPUDdEAAqLY9Ks/NP67wdqGYaXoySjaqLgo14pfpqLsGMkyW5eFIRfWNV5FidqEc91/wRcHNElJwSOsmiWePfsQRJFtrQBhixRXC+U6dK8cB/6HsTFCG5ZQ9FKRcibZtITyC1eepsVdSLsvNC14+K85gOV3el02JS0/9mYGX6cg9SHomt08Wa1gaMTvBYGwuvVHUClhihMk1ivatIFhtdLyXMn5IEn4vxCc7mTi3hL/h8EdkMsr70xtu0ySni79zQ5NjG8PTy7hLaatnT5B1i6sEzzZWomq3Xf7E+B15C423TxevG3dK6EOIMfjCHf+k0ItA+AI2dFCukbLFUUyNySxyAWQcwiAHnxKTM+lIVrV0A11cMxM3y6QpRljOHM8ElB+nK5zzKyBkvNzYSGo6FZ+yXDSRfo/RXWlV8b6JYjsxJE0NNiQ1nIisIu0RorXZl/g7Mn89dbEbVtKyZMImGu54xQ/B9PN1PZaU7SWIijTkRu6X3+Yz1lEtcVEbV+nMLmiNub43VDngUpJAjGuiN9MTtCNJ+cSqxVEbHAKGhBndl9GtSi7lBpPcMwxBZE98XPU0MghCxMSWgwKy0LdRRfzGQe3VRHuo7bIeCmvQtm2X3FRtUm+sumJDhoPf3xHd4aWLUv7KdoFam9/Bnvk1XbcXV+rpKDf05O4Y/1ew+EqRYbfuy/hrTjGYg6dXtGvG/pcOk5EDj9I1GhICItjVrWNzoqm5atEB4DOXn9yFTGbGCQAIk40kexHulnlMd6zS8ySjiAND6KmGXuCiaSwcWBXRQsWxZd8VeqrCJKyRw9mpeI3+nMHop6nv7rQtLBhdJ7y7IaJyhgYAJOiRkRP5krU8UpHg08nwKBSMDDXLaoCC6PyLnL4HA4D6nqhkS9xYHwYcLjR8DFOY2w/WgReUNaEzfp1Cn7PKso5Fj5MDZXm71+kN9J51f+gTwGylY0SXtuUlCYGpJSaMAjCdXGx4GrSF+jvRNfpyY0cSqxLyQu0gWlephyiJY15QU7tfZ/ChyO6MisdXfwQhWLuLwclT1voLWhMvkGbEx2pYtk2e2m9Wb9Ob1xSfplUC11+f4p+wG6ib9PoCKgHbOfPXVi/5fNHO0PAdnE4UhVZ2hau90er0MBzn8pEVPxvjPfUm50M1vWNsYTVLNkgnuQqqMbuSgm67vYPTtXPmMwiyAr+PZUoUyvjp1uXipfHxxCeoJneizWlpvloeh4GpBZXZtmhpkZCYpH13XcDbUmGwI2bxQ0SZbS3yhowUAuWUPzmwKxQ/G/4UPHpP41Rjw22KbZzJK6/ecfhQVSYsc9LHCl4+SwsTDYhoEj+8AsTLHXCbE3zAN5vg7c8L9DBNlIoC95biJmEvEhAcgemTkA30SVm6m8TTW4S8bM63OjOKrLWgldWeX6cUqnW+/eT41GCYzX/JzAJvTmQE2PnEakw5vmlQoCchXAQ/o5d8YUDCbz5rV7qPqg3DcS9ZMedzE3mZdMgUDZUYXA2IZ3LVuFQzwnDpBQaXr/aJ+ySESC5zEXqvpXy+IdKLZLsSncsM4+8Vs1atsVEN6Tq1Avf/FBH8szH1sNhVJJ5Y7/STBQ3fdIiO16GuEErWujUve7Ij+qZa8DSGcOEgj2t/xmhyk2zmRDWYURKazVl5iHYQb31hO/62a3/XOPDrnpUibceYVvGcCPLSl4aM9u12pmh3Qm25zGEM258oEAPBn8pB58nCNSDvEvd9SMxjfcuiOERr2u3E1TJuAN6f60Saio5q3gWYIzcEqfUPom+hqHPkqb+BD/dzUhUCJ43ChHPexpt03oAjnyIr1HLE9tSM65KrcDZjyUNX3ezNWWl6nutq7uZmMgsvFGqTQ/AVxOWg8rNRhTtleCHV++A7EgGeq9eqosiyphwCbiFMSbBb4mkwU2MHHFbvNpj5JRSQfeoPg0bE8o4Eu68Fv/zOT7QV8Q9LDpVAGl2Lmf7PcC/hfOL9xPRAAUlVPSu+VXRg8EHbq5CUHBsqW+nmOGp07mIguGTLkVTAGFz1XdYhkAl3xbykFMpJb50IdTvsc9V8HoLuzHW9TLjnD2tGubtYSnIOlo6HKjNTLVq12+JPz6iM9652iM7sCKujJHufXfS9KqIN4yWxvWNfwmAVTqQFzBacAXOhaipej0dA+ppBBpWUXfOdaG0f6XbgHYs0sfqWuOQLiNlzP9vwssYXLHn+pfsW9lUnY1XhyGMQCTp1Mni1JCXW3HfrilF05pr28drRBs7n607+xqswmSDcerearQJDjMwpVYDTtbpWXa3gJMN+2T+Fhv2GRgC9CIueDN7ABmHUWABH+ohv7MTcNEjufuScD3KdU+JN3py5rzSDdWQ9HFYhJc9LfEG72lL1S3gLX9sh5cOYiPEyKlFjF6/lIQFL4X2DrNAzTwigLnUKZCPvhIDbbBZOtHBmFc8PkHW1w/DS1YeIxiQVejG8oWDMJrAqRZj0xPxs93shdg5sq3K0kAwcUl1n3USjwcu6DyvlJLhbCRTsxn87iuUFbKuPo/9SpLNB7PAjO5MqhsUYxqablWCedVj7kcQnRl6ub//9ysWs9/zWIWt8jhQzFrVhYuhyAV0aXF0p9MU7qHaWkXrLis+4KpfviObZikJ9FaL2eT35ucQuEMV1p0bTi7uKeEorzcCS3pmvF0Dc1qXaF+N3UOISnxj++AQ8nLfH7iKF1VW+IDA+vCdLdiJIXj88gmmkt2queT3ron1hHT0fmWZwnV0+ARkKMY1lag48DP/wXY9kKV1PvN/0xHcoZOqZhuxZbo3TbGNevExiaTe0QVSzuE0AFXvApIwhv2wMFq3zxxNVH30d8uk/pIc3QcX0mUCJvSHPW1JvRGr4R4aJvh/WvbWPAewzaTU8e02zgI3sjZzAsNO+t2PO0fva6teCa7JgoxFL22E/i9+eCG5/zZD7Gzn2/AAlNZz6v0+Gk0RGLC9gozePvlVV8PDLYW/5nWXVb6jBsBJIkhL75As7IJIxDk0+r7j9+tLLf8WhlADfBhk//gkUtMEfPtIhi9xFqd1hTh7GMcL7JOr/Y8DGAs5mR2mRiUR85LhI9pK7yJUOf3+dSlwVzav1NyKD5xWb8HorjEXEgxrB+NZbvf6JbUuazhnmUMklQ5hEE0yVdi7qXmT9KjuDVLCTKDpPBgoOG2xawyIcEstRuHfPTQvXIespILrhg6Dqfjo/XtEycOTS23i+aoGYAQ3rQuH0OZxhxdm+j1rK/KBuCVBUkzmh2sbMkoYFI8KmkYHhVlNElgHkyWc5msk3uW3R3lKmgbms4WQORyxJQN5g60C/jR6HBY2SKa2L4BuRb0KkKz1xBUpbXIcsZZ+t9+wUmpGvaNsuExh1FrqQItdyiU3QxhzsLSfoC9629ztTSyfZIjtjTgAg9z56G2E59xtv+8IeOfPDRooksjNzrOqlfNr4j1Z/7oKZie2HeGLTNdt+4gwDNU69oq82hnA4vkdPE+74x8ynYIg1wubJOU4/Vpn6crgrDVnFfA4xPsucQofNniulm/cppxfEdJhm7Ai/ITKYuFQ6rFYuZ85MxgDS6J5Sn8cizt6fBTgr1naZn3pfNeRozx7g4xIQ4xMgxY22TCv1DAN4cmj1bPRnljmBhE6grQZ4eRe8EZpA6H3DkhSQff2QYtgnc1l0YFc0/pDiLJpE55GPHlA3DkIabl+foPMFAD+w3h/vtyyUTXMOaUMdOqMRi/8YCIVmaylZirkPSBFTYdMEU89WQggDpHQG20VrdqmaxQk+p+O+XPYE91BJr9bCyCiR5WkgLfXX0fptLVsUJcgEcdoq8w0EsVEKnVxInyH8r+IEKNof6wjORcNxyAMFE0gE1MtiThzrdQ8KJpFf40g+xJhg1yEumEPK0B8iskLjmHA/0MpXAujC24nC4YjEZDIlLK3jarW3DwvhGwXwthYT/tZ3qqpI8yHv8cKOTBlPqy1J4DSsSd2Iny5JAecNvthyRct2+bImB9hIvjG9eueCu9918GwcgtQ7LrJCS7zp7K+lzJkDcdcizcr1X7IqnEOKVLpOR9x+W0U8J09Qt5tsHN3y63uIzNKYuUXixLAJ/aHZtoqMqDT77qY5nWS+FVvkLGivUJSpmxvaNK4QT1RRDSm3vWHaVRhK3h7mBQXTdLlDsEMOjbPO5XQLNIWmDNG9bf7loU+Drmlo85IAdx/TP7DRlVzTjiVFPnElc8qPJYRjHGEKwbRjJTdolPCrJjwJNFjjUILLDpMKRFRLYQg4Qm6BF8CFIXV1HljDDcrbmhI1aYYKfvYzi6MrdyW/l/GA8utk6+ngTUZ1Dl7uokjV01BDT0ypHZupXya75puLPUIRkpDz3RBWHTzGpbvl6+9gB5O0GpFLwT1zphtq4/onEze5WznmUmEyWk8r2di+H/HUGFnqwOWUsD1CjoM2yVhJtWsC6/CLy6U+FZIzPoXEVhGTJ0xkYOy5+ulLPzSwttJv/DLRq0NdQqctUXqQu1tviHe/t6VjgMA5/YugvzKmmcdx13emKW12Q4M7/ieQ8zO3Z0d9WH1W0XTunVAeXiAmlx1QnlqTW0LG40KuZ7FHTdknK4i1Mr0kPL/GpwsLrbqy9wkCyKvR7mZiXuXyc7xBdgCDhbHAVZ8tufApH4GnKMJYRtNqWO1yL4ubwto8tYgIa0LLX40exAmit2rdwC99pLCmJby2afZOPiMgcta/PezvPSkyQdH+5oUwLQxDHXih9l3zLi2wMmh1Imj13CQz+CyumIuHItL7IrKQkZrS07KUGFw0qS7dBMhRwhnpE/Pi2yPxAVvEN1IAYP8EWlX8zXs007JggiLN04dXUhZG8WbGIjYRUR0xudkQbNDT9qQzZCUPxfysDk/6Xz3cfXa50ab95vqmW3MxJxbPRsUHh/AaHAjEEf7f2KWZlR1nSjLw296Idz+V5yQgMpH8VL+7JOnwc5KfF+i1rmag+sxXtp9yqTlJdgvAX4H95TEOHUpulXzIBmt1V29N98DTTsy19/opN6SIaG9lKUfYd3BwXL1J37KjUBtVa52kxYD5/PMb2IPppSnhtDMmEwGN6Nzq00wIwesKuqDOAMg/uWJnS9fdZ0KYWXMVq469PVWK5haBa9vr0gecANbu/MXqivwyhhq04gMLawDVb9jZsE3DxmfVPnAjfeXVn4nAWme40hGmE9j/1gHWYHYMyoj445/n0EQbDRxaZGnW4VxxiCVDaCx46PpCI2dEt+H3QPBtwFN3Iqy71tqu8z6P3mR5zXSvwN3RYzktb2WqGsJsod2MZs2ZVWS4FAE5nNY3RhBp+Q+aIVROhOnjKmjqEOpsASlvqyAOLIDLx4dcQ2sw86xMPy91spQ+P8tQmcVEN7jSI61M/SW803SLYu3ewp0VOWUoswh/mHWNqGoWy2RgsPrcsYaYrsRpw83Bptlk+mlxoPCrMCSGWYVlNV/YXrxx6RJbPdPBR/DzS2xLES2IvSNfA2mSy4kmLnN/XgCspMvoj/HJDS+jx2tJRmwRbJKLuFiN6vD7bg60PB7GaM9i085xLnMWbj5fvKJ9D4iNIqyk/uDiPgNpwfr55ALx5EqdUMcgAr7Rbb5LXCQ9mc5wckWpoYxC0g11pjM3xNgU0u6IIT082ZGkjxgUi0cDmreNgIjrHYuki0klUKP1iHmaiMF+IoCK+VFBeXF7s4l/wybWKMxmJovxD1UzJBpsTyI7BlA9JiD5ChYzuBYUTky7LPUgJ+y9THQaIEd3ZJwxOHymdCBnTSkGcOskp4R+zj7if8AubDwqUaajzwpZ9FhYkW0E+QLFtYj3iEXVBV22DeJHI9b0lL0Xl/ObY4Q6Jbis8gAPcvgZZvEvwsBgP1ucbCIokojsund/7YqLKHmHhjihNOgXFTd3xt8QKmvfMYFUtPzOslE2q8/+6lIJNB4Ea/5c6PvAd1x0jCEsGYkcFyaG3at4d3bzL7sZVnBPKhYdoC06bGf/ZXiGkbczHFck9YTOahKXPxbZzspT5uRf1yAIWQ9LWlBqQMBwnRqNJRvw3347i4HbbYhNH40MImUUU2rlJXIijmiI06mTV281nEyhxi7jMf7YAvC1Mmw4SBiad+YV4uFfS1RPSMyjtrVYQFDkKjYyLziJxi3GKSQ2+1lHZM1+VHEgGemPBYgc4/LmHHAskiCgX9pF1Sno867wxs/IP6x2DV1kNEhdE+Ky9kNgNs76d4iZ7PViDEfCsT6N5fhdfzHaclsyZh9DycxKC4XA6xdLvSXNNcYGdhswGYHz5UZdWgdYJB1DLqtyplKbXbilakf5jYrzTLiEPLHEcPaoISODAiOHJhMSVyY2fYOi2w5mJsSg2THNhTsXC85/wZBbLjYe+RKtBu9AEtnU7HbTPQmYk0hHQUC+mxI4vaMN+hOCLPLSamV6+nsTnU8YFobU3T+ivo/eSwSFplSkxHjuwrA8B8cLhwDcXFNi3qsDAbeMRrdD7ig5afgPE3aJp4mNepcR9CYq7Dw+puk3yN0fogb6UziA2OGro4JBIJfwbOTh3/9IarIk/OGfezaJ81bVaDOKV3nclKCgZxEdEmQzVJLYu/1TL1ady2Ww3LVcSrCw3XV+A+s3O91iZb+6fAZhNPtIRWW0kBmXu6VVLpbWqHBsCOv8hdvk8Zrg3rTEwO0H3xvTLPhBibYZp5QemdN4DGmV9objBvz2rXoSjhpvp02fjl6QUF0lTcln5WcgcWtZVkSb83LCyXpSoyncykcBSDVeXXpVa+4ot0xOklE0J9fXkWRvrQp/Z40nVKy+zueQibRnXMrPMPAVXDYxgtaTb5PxkKpyjcqCsc4gLRRi9E38CTX9fHIJwn5J1ucuIcCyWycLTQ1C1AoQbH2qUIVe3ZrZR0yUfQQBuZnPGGMYV7qKAgJ7Cy1P8Nkwnhf+yETWlHxgvxVvq/xU/mcjkgE/Hh7QpVau2LUPuNy2P2BnukMAOx37kVUHrWkk1W4XNsB3gx+6AZpGvxvQANkLKfgr98P8CYT2C8dIPykGHrPhE25Pl4QeWTFdyHVZ1Z1aIGn26ydsG4VjG8o84lqWw6NQEZ3Nji3JRcdBtHcrqCC89863h7EZb56leX5oPoD6Wt1tbpuw8Bj35gL0M8zUe9erLmgNXlAflv4As3nckQGfSos1abN3/nWGUkQzEkU/z4y0WyLVxyeErxAJjQlypd9UX2XQYDuWzEhEGFE8YJiigE8qW7Fapjf2ZmG70LhKBcLtZRRUIVDuNFeJW6CaM4KYm/rlyf+SS/QsWrYxJ3Mx+s2hHjUl05C3sKwnBQdwQleAtQVNOaPYHhEEncyfI5OO3WbpUgGsifj2bUrY9Sd8n47M+RNERkCYy58IjA7ku9Qy9ZxR1HRf9AFMICdYD5d8nVvldfX/kED5RnTb7aT2UiUngT/oqtuJeYN43QPh1o/lmhPbmS1Q+rTrPlfiDBWzmRg5MJZuCCY2UUirxFFTrBMb2Do4HPgPEGKLAJyWikrgynHCKwx2rPbZ1Bxzz2lojQvOE+FHNOm0bgwWQZvKYxumaCLamh1tHGBnA+E0usctR1KXIDTNNvGrlKXLoxlm3GhLII65LzHUN/KZYGWcqotQyDGgNpAa5ynbtapzNCjeUlNUaq3ZI/LMEnLKjocDYAS2eQw0fC4JIxquIhI8PPAr1PAqW575sBMB8IgHTISsDxgmJqBDfnxuOynZ3XziFyKaxkEt3/LxLzY9Nh9I2l9K/LKuQMwZqvM9Ui5FaEJ60UTNPA+4646DcpWiRIjJMLq7VbeGNB7xyCJNMZ+axUD3axdvpBmYodpxsEKtE7ToHenfppxiLlNKB4YoQaBCNgBtdw5jsG3VP3fBLXrXKedIKwNZABEdRf1BFbXl2RmHzfYSRqLU42+QGusZo7rkz6HA7AfvWLT6jcJBk0Bj858gTCoqWv8arNrpbjJKzRAY1PUtSIF3W0wGHfLO1AvamePhDYgHzox+H/lrsBnXcLw1IfVsnuLnjx5hMaqTj2NoWcrjHeoj20V9f8XRd957U718+RCglD++USlm8155ASdbf3beOk4y3mu7qbXaxkgFIcqPd361zo6/O+OIstayRTGVT7QDAq4t558hUnX2ybDL64LBTW80omd27JIaAgB6oC5/TkYp2EPhUlxDKirhHltTe90uNRz9UAnnv4IDvJva8QCxCgABFm+kdQJXClKZYYNT03JSaMzbWRDgNYpPRGPppD3QAIqSCqvHohSYtP1P83z2g5BDpFE8f/4H9UWjUBuO1b8ny+PMvvH3gkpOC8U4Clotry3KArtzOJmORVB0QK05ZW/5lS465v5glaK5BK0Gh9EuAmq4LhdMbyoS8NKFrcPriU5bNOI8CHxZGK5CUCpqTDM3lOEAu2R6spDM40qgGdYNm1E/vOCWNGnSsx0ofceZsqGWt/Zw2Tch9LVeslqoBAIbHZ1SEzfVTn2m78+umdUJV4tVbJIh07aRrO/znAhTgnJQOFSYN9SZfINwap41GZs5RxuRMMvSowFQpbM8OxeR35w+mFqmEmFn4qr5YQhibMDuS/jLO5j3PO++n8l7lvkMH2Dk/VxjKnmNxUp8eKaJjTxaATO2q1mGHP28l44uriGUW+mui2ZfWymZNOvNhrdUkSIotxlvIEHRF6YxXvRdFsOdN30bJUWwDDPvjPKCVCK7yfqjZKYytTm2iRT5y2L1Gq+841WccSiFVAdsMa9yLR5zhAi+hNyhtnqhMPwUsY4jXr51RCgqsy+18MoDbr5Pjs9LhB6GVdwIfLywBt7+lyqxTCU5EigK+Un3HTDk+iMii6tltcnAbvtAvFSB7XoRdXerMhvw0A3y1UU8+wwFnQVVGOlPFkaB2HZBn79Yjef4G8d+/TysTr6d8Y1WumFWPLP4pu2cZ+tdYy/6oUBV2JD90d/NqFvUNSG8LH7OL4L/G7nWFZ1q1dtIFQI7M2EZJHnIRcgVNfydJRR1chmZUWBhSUlEHTSnv2LKKe6GfTHDCbd+6vcI4cieKoK5bb1bIjBjZf/Zg3Ajf3U3lg59Oa5CSieWQqrCpDcUq5r3Px83pgJRTzOgOAHXSCJsF23T6JCnWVodC3ToFSbpAz3a3MY4uMpVuHVfP6klrxA6KkUrMuTbMkDlFL9B/Zl/njCWE0yxAiIDPb+RUej0GvWOHvywxCIGF/HL20Z1hAtBdY4TzEsafZUEKSiofLW5eOYTPHv6EqnoNdWMtO8uCIeoWLkLD+FzaJS2lfCQq7mJqOEB0ZvesyM5tp9BsUoYbLMjsysebZrmUXtvBMy9iqhf9dtISQzSfmcndpKB0JaWIqvg9ThcgXCR17xoShHmJa7FFL6lGfITs8Hek619pNoy1sQQ9PRTe/oQe9QYvO6Zi/gXuJgF5yHqRAoyQkGh7ZSAjMGhAug0dXwZ+F/ZgLh2Ty8kXNwXIaBHDRr6a4pmhHXVPPWZnSQh4WPrzF4nLRyMlegem9nYl4Y16z3HJXex0EiNJ8SagJgQcoOoo1+xfyg1zduS2EQ/YeTBsNllCHXc/a0ETH5N7BXO26cNDOTE7fXIboQMtBg7eoLI6L5WFkk7nyTlDE//5br3B8hRVOReVjpznxLFf8C7Yrf+Y81JtAblwILpQt8CztUniqBAmGwBz3EQiyFQ4xy5ahY3vDrNBT+vlRiwYUdoMLeCE1n5SwkhAV5YSl7Gopu0qjK7ICQL50LG3SvergM3IEaP4i5oSTP9jc46F5mJ5vlgbRgGJQ2vRSooTzPAkIdSDHHZQJ5Vk+FvMrSUKOAWfQVE9bhw6PbqxNb4lOA94dJ+WqBIi3hbBmegfD9yrGs3TB2GkY2uOXKItDP0ThQReYb1CJBFH1ki557tVopg2HpocyKwV4SBmsfT1tL4JF8hH9/r3uiEYtoG/XOny/+nW60cE0sHWcXUFu10ez0zQOASxm1K3TBa5aALnl36GGmgav457epe3pBYn6PjPpPhJM27X9ZFjNLQZLFgnxXeS+n6sgpYIDY/w80lunhcbDROGJB7AJC/NndqpnT4807EMtnP93mACrZwgxyXSfMoYuji4Xj8F4Ihg/N+tqjDgMjCedpju5tsAt7ZIbBJ8jIqFhU9Rg47Uf43nJ/8bsSRPowZB9fNci3E2W96E82NfPoGGX3yV47mk7qiJefr6MsJdxbpyYH1ARw+WUA1/fUY1dpGbWYNw7ssxhGx0L7T5+1kJ8GgxAGUddhn6tnsAtDtFc83NxMIfmU9FWZKN9CDWEWSi1V39nlxW8DV3HxZ6Dlp3lu0ET4PY35MiYJ1QAx+rgC/QIHVizNAbKg/K0TKBagYZbkJhMnI20U+DE/n8yfdWInZjwQ0Bwp/TBXp8Xb2ll5pKaveQGQLo8BJRhptmYdMnXo10mSUK/gKl3lrzwqxeqHyZ2tgspLUeL6ZIIF4vZxBNLIWynr/8eT9kIzG2WJJpL+Sj2WPwh06V9uJzYHz5o3y4f7bxVRNxj+a4UjS0jx0OurHB3rR7rcbtwiYjsE8BNEomVv8wZzbhKxq22mlAw97nfkEPlOGbvdgXDp/Qjm0EXx3AU0Vt4nmeNFFRZERO9VoMe1mmIMZmtaVK19CTT+0DzlcEM1uwV6cHRlt1fQ50VpHXCxlEWwTOj+NJUxwl26S92PsB0a7nLEVB5/C/2y73gRCVBvJFiwuaeAqn3MssgGJa6v3JRezc1mBD+knHP9uQKsqmZkeOOXjRYEsm/7Sa88c8Of1hov5y2Aj1+EZR5klWb8VRY/CnWEq6KmJ90ivkHoQwo3GJiz0oQvegjVzbF+QnXD0jevyzVOAOL4Oq3NjY1WatKkAANEBunEpHe6gAmRT0VcTnu28cBEndr37GFYZKDfSnshNd0FZ5GXsAQ7p3zLPKclKhIMAAfp9WgkL5zr/C2DKOMw2rwfXjUQX1vIuwfyKV5W602IAFX5umBCApf3q3G8XcyLFKM+txxfGUIg/ZdZU/4K7e36e5BqlglH50kAliT5iCnqIHh4vjMJLhSkOducXOCGAZH/OITu0z/7pEU6jSSGIbPeUdWKeGg52lFUeOVe8UHO/kxK62CBVIrLfWps1F+5R32TSXXznA2eqfy28YIWZUj93kaLEor4LN/YfVE000EvqdWUiamPOhHz7EKr1Hy7WxV1r1c+vGkxLAtlb0+8s4tmugVE9SPOnQQSKF/6jxftGd4OVVwhz0IoucV4MdHPahVbsPHBDJ0UDNHeOBvXZQ1JdX5KrtKm/ccYs6B+X5NcsdLESPIQZ4lnUAzXO5v3+AWFE9P7vR02pLNIJO5VCp6bUyYN78cOq/P3C17xaGT8tB+2xhgXr9VcjBC+cc4fXoE0lT7zh6bA2xkJSXcrmMWq7MuHsseWOGuTH81CLIANi4ryAsV/WEuFACjs65gvytfSEm8PSQ+gbhxtH1e2M53xP1OqdfEpKXPDpycbYAEQIsmgIvHu5EuwMIN8rys5Kz1p10fXvNwfjcILb1dfdKIx7aCoBKsVReoaJs7uvojq0h1/il+wRYaCKWJGM8L9gYMLG5YaBQ6k3Mb/b5b9VipKzxGAYlEr/HQEieYufdR5KPlNj7/mqImtwxMB1WBwfoBR5fzbpiO9CUSSAcuTZwXdYz1+kn9zok2G8BfPh6AQ21F8lmVJPLXfMuQ1DAJu/YHAel4tIInQnDRENDZq3A/KwO4YYHfeHn+9eJs2Yqo4BFKCM+7wuWN4Lt5xO7+mlvm78O4hRKQh3miITPHICyE/CmlNEjIKfMIu/VlBUuXjV53nr2z5XCGTXndvFA8GgKplFAM8Ay+VMxTR3LRL92giq+Rnp7Q1FEt7MlB8C4p+KYBaNwKdPx2p7B0LYdBdhbTA8QwxRyDSfhpBRzw0x+9MT4T7t/VQ0b7z31Lq44+shLNQeDYwxrkaPqket1FhY2yoTmr5B4Kbug5dXXNtik7AkqRI15WJ/3YMVkGSkkeQC6G/MJ7tEXzOz0Cyb21vN50BCX+bBCrdQjoGeOBPLaKAvr9mIwPzHDdMQ9yDc9sZ2YeLRWpYN53OyH9WkHTdjj81xiXT8oL84yK+TmpJUq40dgxSXeYjAKTxjRO1wkzYkP2sP/z6IY8M/JZcbAHrT/A39w2xKoS5+1f5FRIaG3+36s3PukGpXGTkdSWWmDuJMLK2RsxFgt+6/pKdRw/sErp8ES39me9/zqcQ55yZ8lRyOZTCRrWNpW0RtKIq82pvayxIgHzIrjyVn02qUzOesr0hYMf3Tfz651M/oD5k91GJk/cCC21hJ7OLxO7tu9ZVdBW5hA2HKLJC/jnCQWPN5xrsSPEaIItZm2iZjHcd+16JmhMQX7tuFmzi3Afim5glnn4dQhw1mYZtrLfhZIobhaY3BUQ16hJvAmgm4f4FqtC+38aRA+Ab7au7AGDtY6hiXBue0N6qmOAgCNL4TN1Yi3QnLStohMsAHEO5cE5EazKUvntKtpOx3qKlnK78Rv2vD4rEo3FCb1K53udyP2SrxCURSNiDPfxaYO3DhdunCujn5EfmQ280olq9YJ4HIkFYG0vwUm0Yiq8Zt4AzKyrF7lLh+F3ioa5xgHbYSiWNfdJkhWi394Ti5C4KZ6y6yaNQTuJbt9Q0GFh+rb7EU9o9jtgtPGCCoo3i0h0kNWnx3ec9hgYB4uzXb3YfMxn6srCZVpQkVNrbGdsFV7hO5mCaU5ciqW5E6UsQYvECxC2lH6ldq85tNPRr1Qcu9aMtYHKwn8huwuaKUOpCY0D5/X2xZ8Nf42EpsL22jZD3+lVsGvmwqK8KUdLrmkOh6T+Zi6i0vsdVuaPyXBU47pcazbwyHI/C5M+pNZX6AH6ZFg+K99VYaPribvOClLN1hb9++Zuoeleu5Nf0YZF+z0YBbjO3DB0WyO334DGCxx501RDlq6YXMRxfDUPevdQvY3pRyr3uM2jTWWWiGeDwyH+kmt/K0fXwRjyAVktoCWQteEOQs9VqyDKsQ+qn5ie7AnrnJNC+l140ewfEbO5OVyibioy6+teT5av4VXV/OpMn8uoTnzZhs2WxuVJbj456emqS6M5GwzdVWwx6gr5p3m/ZEfOZg7nen+j5WVifcBkquR0Ug1B8wFrVQo0N8wRcE/+dHb/7W9AwsU0tmN4Sov0MZuT8fqaCOO/yD3bZOJaoQ+ek501iURMMqEM9qRsAl7cL5XSrg2EgeKj9ksIYxVL2OR6lGoN3IdMUYxLWu9cdTVa1hQFku6b1D3kkPILKv7xVnl/fLC/HXxa2gZEuTUQ1sllA76rzbzCw/PEpVWtalvxQwp3tSwkWH1E29zIy+pk8QRsDOMAYCUX5EQM8yNep4dCUD6HofVIQIZYP/b+sNdvnaZMrM8Tj+QowqFNW9DMGA6RWHDzuU+l1cC9AWq/hXTsL+0QTJmzAabtV/ZQoKnACfvWgtzhSkiVDEgfV+m/N/zG+iQx9pjkgnbDuiP/b+T4AcBMd4B2UD0B2AFOyK+4UxXPQ1oQr060R6efyXjB+460MalRs7pwK//FS0U4OCMIGij2b1LNSHvpGlgL0KFbLBVw/oxHjyPLCztUNbl0MTslYb5U75OsL1Y1ilyMgEZzU+2NgwPHc4olDnkxjMSw3uSXDwPGA2UW5TPJECpSl3m2jBtLu7tyv/M+34+FhuN3Rx5G+mYcgakQ9UNb7cVm/LdSG5CxWEuUDizpJfg+54TeEd1gpNPmXexwAte9Tj/WXkkP03GXn9yRwdi+QmbisUB5nDOTS79eRVjgYv5RCsR7ysw8nA9A6VVuqnowBO+nWB8z/SC33evQZ0QWJES+qRIOzbn6ir6rWaw/3FKILr80cbOTvHizG6S9kCkurFzco7V/GWfD38VmnbHiKcoXYeusYyL7r0V94rt8YzIkST1uUXaf4ClmcGnwUVVNYugKLwpCEfbNsHX1y6CQ8Yu1DUICU2hUFYzD7k+EDWvwX1txiDM8u52wY6KycLO3LS0MvGoZjeEPzlfxaPPPEvyEciNH91bXFQyKnz6nNdQjeThkn4e7jAoanc6Gl0Z4M4LcTuDptL9i4e5QhwMYi3+N2n2+KgsdVUHKX7YC8T5c2bmknGFbVh5Iji3e2lklDZqKkZeb2lJMv36nWghcC2sBMjzHvkge8LbTLy1zzcAX9BbP9C06oW6pgEqeDdIvyGys4lENZmWcVdmKQHv4Mn0VndyzRcOwh1nzJgVnBvNmHQggIvExvCmktPrOY0FEEVgjFGPhIV8Q+zRu6Qm17J4SIq9siz+KAv6pYMKzAuXLJpZF8LWNEs0ESv+Rdl9WWM1yqXE5+jXB5f8KyMFl8NWgKARYTFjIyxV8GaNSbmqJ+940jL/LAMHnvUpeVBL2IXydLh2d6T9W2M9yh60bUwqqrrO3qgRng01gr5ZWoi83Yd1r7h5btug5P5lPA9jklTJ8sEfqaYlOO45TwFvBsDQTyQBU/AbeCIoblxdSyBrp+CXmQ0+GCLtPeqDLbDZMKbqJEeqXGzPU+U410NIR4AWloa7kkOARyzxbJJVp51kH4JA1HwUDKcOzvaT8MnMtzu2exnLNN0eAlYu8lAnHuXgm1VTZ5XQQy9g5yWXG7YE+0MzmBU5DmtfFjNRbq+XHrtIkBw6XgFJP2rY7DSkQ/f0Z36nLjDvcqCE7lxJ46YwsWHrpQWDtlrcmIeIcEXY+Q7NacXII9MnL0l30j9awRTcK/mSc/baj1kg7Hk+ZbKYkdMoxoxzePMkrNqL6Eb2MAIqjLMVM2v3ccqFVkqtl+RdR27a4CdC8qYk+n0eVx3ULSTXDvIkDm0+DwRV0FG1W8d/EMa0gY7McOc/D+388njgpnTsR9B8Yn+h8GkY780JrsgX5EIpAODaBeeft8Mz3xyYQV7ywGJL649IScvTim/k4Qw5oeuVgF2vIFEWay+6soTiDQ6C7/A+TuSt5C5qHsVU28pHfR8K5/K0NIB0+PkGsEQfQURtq8uIeOzQZspwaIAcU1EN/4BZCFCsDmRfP0b9qOMvnkUAMjIg8jRzDYPxulObKYmBop6TaO3QiDVa6uE/2ODw4/pZrEf0tm+UcrrT4Vs2W0s2V2fPQFfGHKRxOt/nKJ40pEnhsKZDV65d3OUbbpLFsqWKzy4Cj6ClBCDpIg4uL5V0l/kN0HZAIo3u01RTILRLfXVqNAdhXjgO+PTRKnCiaacpIb7hg8+DyThKLdDhYqqcgHduHCvvvOv8NTeqIbV9TovPFWthfKit7VIaAo7JcLQnoBtYKYDzczL5A4Y26J0j2TbPOM5c7TQVHjRPtu4s/+5chm/VC3NJAgGbPEx3TFg2cbD43RS/72H0leU1l3uZ2sloSX98qUYgwYRUZnL3KzGaFyetXVOJAKltazFilR+IM3lCd05SbuWRSxcTrDA2fCuIpgmcZ06gYqvb79ZpnzyBtUOQEg8WeiSWYklkKg2CU7ihmQVg2viyIHtBZzME+o6g6PFj+eyU874TKtr9tgfT1tO8h6Xj7jdVpQwRZyND3MKHDUA/yBDwGDHcCygcKgeyTr4mvpcfHzzxS3L8aLK3EA5NX9l7f7Jx7nJr2y3AW1YzPRxjSQGfW7Y6b29UoEkp31Dl7j5p5QPhRBtu3FeyXi6MqwH9id4Fph6a6W3kkYrFCRcJ55Rt4Ik3e2PHcDaZFZw1Zg+RaPPGV9VHWnDqR/6TnuDQSiD1skO2xW+2nL9p4hV9K2Q1fIYY2oET5CD/68LiRPIbjUeNmPu1QtmxsSa0kxowvhjL4KlXC1l3niZFit6Vqa9Cbeyu5phJxtAjXLRzPTZl15PmCQpAHn2NMNYmd+pg9BREfiih+5jedZB1IWyTFKW266eMLQkvN9q62UWfgtnnm0aLx5KSUJnbHIvAfbQDvVhibC46hUuYUhcwAbqvNkKFgtXKSOpW1QvTUVfLU70gowAqikdJi3R3nI1WnAc6/b/+uOOWuE/dvRQ7AHUW1n6wEk7/kq1DdFJZmcLDRV/ZR965JumF1IKS5p7Zl7ngvHwfpr/VY13NlDzhZJ/QiXUr59jz4lkevlYjqHUUe/MBKz6qpzqm8YkO5KFBE3zGMXzMk0EgYaY0kgalvkF2BJMq7/wwHkbXv17aKfnWzlKdVmhSrSFgnX/4iIc2qYWxpb4qEExplM7+uDfj5RozdrgsYVh4ap3CRN7Fu7mvtAGAd4PigXoryorrczz+1aiP8efDipI3Rk7c5jHpzRNrETa/j9s+GDk933JeF4eFOg/vGJ9U2/KPBI5bOSElMtUX2V6d4p+8hbDQtgZCJe5o0a0cX50kAmkJgGaIml2D56GxK58tu+WJsgbf61GZX+b7UT9QBtagIuR1cYxJs8fGaeGj7hEpB1Sc+ZkXhL4SIiqKEl6O1TFou4NSstAZLtoHefiLHYJPREw6EWMY9oIJYvlcLxDWISC6roixsd7YkqpIXk9XrVE5zWZdWNo+P5SI9eDEXdRXfTUEvTEzKVq8Ul3eoRtGXJ90w6uQJ7K477bNwzZi6IEf9M+XBJO8Hp7hLZd9FV8g8S1iq+QogtLF0wkh0xsD6lEk/wN4KjI91rmB2a9+rVvYrqZM331NMSwl2IiBzgIg0Tm6Ora7jbsAqQdJtraAftHD9YkhK8awU8LTmRfJeApfzEB0zKbLzuSapRxyOizqhb8/OzZOSZAfKfS4y3RIfzsftZcBqF31ZuiYqWsuaH0t7fOGL+MjQlBEZE5oMVEzR1pmTv48rGEY+2MQiXaNv92jhNRu/sX8Ch6sv53rLzZsau91A21aK8hj2ijNmnj9muA9fskYCnEoC/aGKjSaAtOBMIwx/W1uCnVVc1Yei1OKaHv9xa8lHDoDTAy8NwOvDayRB/wMmHxqGUlx7cBGTKs1Qq9jlDKxBsWfs1fmOwvbC7547ggoeC+qIUU7JUkBTAkN9/lqjOu3uWPSex/FIhZ0a5Tn8/03uODZKIhiYcYne/Xk7h767NYt+7fhMnWkz8zB/rVYU8HbTBboZZcp1h/6NbVC4jdbTf2i6sdsXNiPoX/0Qem3vkrU1u1G+D/VoU/GOdSK8dCFkqLfYVGWoJpnLN06Zy1S3L0ygFXne22Agjma44BN56nwQ+vkqRPVxMj1X9rdtCqK0OtqGQSb/7Sp0oCBpm87HlXDWUnM/Q1cW/26CdKgz2HiK1jyPAMRusvl4ZCVAMCi/JIn08hAC2nPI3CUSwCr0lC7wG/7uOWyaTtbUadmlOOsDx7B8RJN749U6YfDMaxpv403VR62uhTRUrehM+tp2URPdpNkfunRONoZdfceMYoguXCrH7OkB8bM4hy/vy9bbxudODca3ujj3oPUJUDIe0Uk3WbWJ7M0oyvQGoczHEjysPPhogCLne7eKoh/lbWhZXltffLK5lzDkvUwGWeDcJcA+3EHJaLeJbJlfZvxjYbfFrW/pQ+6M8ugFO00wxNGWqz6NyEvS31a1+b0Takn5Pio3XaadAOb0zYx9mG17YCcxRabOi7Q1EjZpIlX+8vBLVEPGRgIfDU0lPTCP8sS/D20MPBv2nenlTwmGCrGcea4csqLjJG4HepoTC+OoJbmn4s9GhRQyj0NVnlsqc2gbrSqaGpS9aGdF0/LJXAyZIPmsjZyKktbBrnxVsh1tO99Gx2lgSPvrn+WUdGmUT+3lycOCGx1b03p2JHWAROkSTLE+aGIx8e92l/8xHw79zmUQNOVnXj/uUhMuFJvI/xdzFfbYEDQMbDFR/1IiNaFgUkfyV5SW0/HziiboCTH6jF78llS+fKIr+eeljP9oZ/ssgk9KDZAkWwEOYHjrdf2HAnn5zP9V81fjEmzxeApKX8MzutYznhskdfFOUeMGAPIWwlpYWsBE+GtnVN9lI/loJTeJOFXU0MbslqP6wGo8ULEtCPgeaQeIbegAThDlXNs2gV8Lx99SoJ+ZILypXiPZDZy4/v7z0Dm0c3hwSP9gLvJugEMUQTMCV81AJwTXeXiX6Ps7TlwxDgWN0Q7dv5piKnPXLjm6D/6WvbKuSM+7NKMAPSR/XXFm9y15+JqG+PUw37WV1WT77sMAc6UGfej+1TuYk+Ym0KFDJMXMIRAdr2+P8bJX3OkXES9WUq9GrHsj0aZ+tbiKaPXL3z+RdSK0PXDFU3Pp1EwMyEqeBsm6VpCMeU6NiTjKccXzTcU3POwXiwLT8tifsTmZOY+53Wv4232ngMBpK1p04zY8oD/2K5LkA1zvWvVSgL1MIBus8Tjp3TQrsm19f9jYr5L47siDqYUop/byNrCuEBhP21EEZjH0pyvbey4DxGrtzUrHq8ZHOvnEfDHULHbeHSSrWzT877KZQOLVYqMzy76e5fYXPoAGeqAcxNIOIL+BFnWBOF/HmWQR31Bsx0F3g14qr+NXUyA5z/WHpomghtFIqD65CKobo9kV4fdK5MZ2o80KSDcn9i6AuT41f66HTgT9cEftpZH/txkzffRmK7og9tzFblbm7WsSgqO4QVD0Z4ZygFlyarnFXJAGY24b3c0KvQNbnIwvuB9RL0LCf14iuXf9pGE73chMtubtqBjWd8U1+/WeC4+o+d3KXuJjyA0VJWfqEFHKSy9vRpKK2X5RxiZyoN1L8KHJU79HckQaT4et121KbY9TAvc53U3nyW5APBZWVKmQDVTeGZ9j4DUVXOMq92N8PlIGxPtopKsuVovbF+5g1oFWYep2gt1CdiKrD+54ZQzwMnYU+xBKpu9lAvm1YeiZsfo4/kMPm2/7cDy9ynmwLZzAEchRHavc0kE2NZHd50sxmEOajOLPqOjpEiIrfiWQgm3EbMAtubR9MW4ZegPi/7e5ruj2tjNr4DbYwkD9zefnfvm5+b1tTHMjHMPAHTAf/+xyGYzp5SGmrCgT6COnODnb4klR2r02E0rLXcRIEY7BN2JVjky5KaXqFtkq4xwG6XpXGhjfw+Uax8km3mtrwGi6R1esQuzozlmymAEEqIrpKVDq3wNDgOGaq2K77CiaUJHMJcfKCfZ/O9hgqw2mmNNLk9KSJ9V6J6xWjuDdUELIS7x3Bw9xYjfslGHVEDvTBfd8wySIP0AGWv9GJw9tO2rjRDjtCI+/RI3YaMo1ZYjAIBOq/BB9Ig/t1HN+VQbgbThyAgCZtknSc2ZkzEU99iPKjOisFiEL1/UDUMfrmeUeCWGprnhHABEm16ooDIXpZ7cf9NpYWTL8eJ9H69w6YPbrovCjPxqmNhZL8gno/efgRtLS4Gm5QmbyX/pnkC0sAZANXzTsKFKkpw8dl9mrtwbAGCV6CBs+oA86FUfQ4OxFw6GRzBX3ZQxeuoK2XWkrlMPI6u+DVOpZzK7JXjQLxKRhLtcYJOlTPW8RF0d12LONrkFjy9HPIFIKlGZabQnggGFD3O0jnmD4Ql/nnvUvK+fnfwdj5TYlRyEHM0P5d3Am7+G6iKKFgfngF0CBf6IHp1p+Ui5s7dLTHdzAKQLKNsEbmcy9yLVdXEIYsl2SHlFanK8v1oZyj66qm/OnM5W8z1kKwoGWX6XWkTJLZGv60bxBulW4dZIcW4jW0yWpcLUk9Q3VxO7tYAcW4HptHbOUSqGJZq+XK8QluAHpldjFEUwsfbpjsEviAiY8GqmTnOL4ylFjzwYFIW6ci2JK53YVLO1d0RONGrSNYb40zyAlxEzIXgxzL+jqD/5L4jrAzklmeryhY9xWpSqKkCGPt73LDmWwOYfg0gzdyDSxOXWJs2YeFQb7YmlLlvAvZgnQ4gztEmIiWKjKnj4cmzaHXHwwp/R9NuS4lfvHVFR7pCpR6grGZ7ti58ukeOUiFqiTneC/vcBaVm0YNfWAe5WQeULkb9mTfTqCEWtSUJymrzmtrywQhLK3NzqyaQVbnK2mbRl/29VtUrIY/KRVMBG/2q8kNEgCj0YnryuXXJ543VMHaS5vbjuatNQmzmKWcpl1+7OmvCcI9djZphQhbxcIx4ldjyE0oXQ3RNBGT4avt4sdwYyJ5d8zPI9eLKSFhHYt3Ks/o08iYb2ILJWlvAXxu2wtw4mAulROKUg/AJVD3QyN+JRYb5RT7j9wJfjXDgh2jWjENJdBxhFOk310OgvKRereDy7E71g0D30yK8w9KuNiNUoDqQiZ9KT6OgNzkZ/+DMjaoeuyBefX+jCcbfExEzx35FV6ADX+al4HbDezJikux1Pa0YuEqsF4jGKQwMyONoqWqQPQ7R6vvyB4r4aY7KTq3s2m3sReiBCbTxFK7NUfNbkQpWhStf8ven7q93Vqc75O6S+vRuuI/+JDEOrYAItu78xggGiWf11Pv0CHUVVInbVhUD0FkD4Uzyd3Z6jZ79LDX7VXj1DIXwMVkyUES4kua5yy0E3rcE/AS2AmI259VxfWP8s8KgN72lVwPPF3YE9tE1B/6qxH3FgLLwE5hlvsbRwhGfMsy8hLnx6ZVEtsrQby8MOOKD9KKKTjbHP7GHIt7vnMfX6n144MI8ToEPTl11Hpren8apToQmUkjz7zZ1OGik+Kmkyam1FcfCPg5O1LW3RQmCAP9I8qr5LYFtg5nI3SHh7iKQU8jYcFb0HxNKdcRgJoOBSRBx2I/JXhWGf9ycWA45nCUmyx8xqMwb9MIes3KMyHq0UCQYwKkIc4OfKMVi9Zh5hv5KUyT6gek4fuPWP85jO0eSgjFd/Qkdd7Y1YPttq0ed0tZj+uBpBF4D0KSUIkWMs7uWgNAWyksPVIcJltiArXyO3e8Tp+uQK2hTNT0c2g6hg/AyY938sHJ6eauc+cwxMAAkkpBVWUDlbHlpguJ5SyxBNkNvJeM7IhFTyOPuaIkLQQwqQSG+qES1avxHF4IX5GgZs+utPZbincEhr74FGrcueIR2LUC6GtHiu/kyxTrxdD+yOjYMUwzNTZ4uoUHBLN+5gbPwaIX7+vZW74g981BHV1YOAOkiuVRJR1e8FfxnP+f1r5ninMjshslMsAQQJUwhbAmfhft61jCSDRVY/MkgnoRphf5cX/71bvJ3eOCPj+rK+D2naEC2IbwjueW9tjUrRQ7Pj6hye6iXF1FrhmaHF2Iw7V7miV1o28HKYl6CHAN9O+0Sv3CeY0VbKQgpWY4fbqLTHnxqi0uLG3cIVVRGNgtaY3tdSgx8UnzjGk1ChPK7gByoXedinG11jpxYjKjybYGbtrIg4E+2GT6W2bNDA+sHyVX/+UXaIQL7O308Q2ne+ijzJAa38x3ONw7hZm2K/5Fx42W1vt+6oxwuxIi8E1m/ALpxttBcYEUsnqkVfUcGP7bteHepV0DapUZjdtXIDQq1gOae8qFLGZIbTb/Kii72BPDgMutspt4d+SrcRZapnDRy89Gx6HTFqANDVTqIrqxjclbldOY/GEjIgrI1eZO69/DYjA0W+kTNBhG+j65916wC04e0K3Ck1rd46OZvT8aV2XfkKIYwAux7xnbbOqLLFhI9FtUdPBDuE+pryna44ETsKHh7lJMyJqU7H68ro3AMBmysDREwGfGFrh7kuNDKrgRWODDMFkZmsAOpqpETbGVOJ3oHL9Jt/9x/gIh5MiYpCpkHnR7sMtnNydJmy4kUwMLFeLFiUaB4XPU3nXo3oW1tHQBctlWEPbm+eN2Y5PVlvfCDPXq5AHJixZ0zMXDcM86RmLXMY1og/BWOXL4D7dOLCExJrK0fILArV+XcagiuV1lSw42YfpjhUHje2ebJE7lYyfeqNfqmJDOwNP/5S6FOWfLKi+hqfv/3YsDf9svYE9kd3VkextYhvTYmRVQ0+pJiwExWtYQJpFoajkkm9ZNpeLKrrza20yJ/XyJNh7ZwAJ4PUD4U8Yb4gC6YUe9+kcpfQO1yDjjU7JDY6sLbejk7KdzRJwlcMRd8gHIKwxr7LEthjHvKGa+hntGIWsevSCAIOqNfBehrPydekEMpiJkJIEPtWDFYnVLPJ6v46/FeRCk7NcfXDlRc1lF0yd/dWdIfk9Myp13sgYrGUHXPBawrvIeUfhuVb+pLk9rFBQ2rhtklnbjqAypLuYsNnanha0b4ZM+DFn3CXnj/LhSGZDIdBGHXnO9XsSO0rv04SDdXkuLHCLpN3wfZ3Dg77Vb2CHayX/mEuTzgOcBUKOyukGo+bxipOkySD9hCr2+qNVLPMJHSwdHEjqu5PZAi2T0sNj4WFmt1lvn5ThXMBHjYHlEmJRiIE1x7+CWTnq7gC4TyHYqjs28sw7ZqpcAw4FznMd6+Lf1e0l4gYeGew3wZPp2Yrqybl+uJ6LOwj7JNL5Fu4EdTw2AY7QSy7diQg+cssBqK9lNns1EPriTYqXEvdxRLBoIOG7kgr0UVRK4C3vjpFYJxpM9cV4Kl3RqWpxtd1ahsYXK9pCtR7dtnEy4yrzlckO8cQaT0tmAnWuIAFzaxyNyiednmUMHkAPrVfh6hY41qj+tvCn/MqyS040cdicrqUthxLBnSD99+HPWSSGd8y2uz1T7K+4ezjUi8ERM6mG+99Uj5Ml/teePGZoVUTjEDY7wkUq10HQbjlS5/BVluv5fBgCA0BxTv24jKosyORKEI+DM87NVhAWR0gTyuxosT542IGsfN33197XEAmAoWh5plYdEGhw4SvxqhJ01J8jUVJfFYXHfkRItNZXNDtMyD6QAbOpNFI34mQ5zu98T7Bdh/GDA35bp3UvdSQYwwPQM5H7EmtJDq4Vd2PAo/2JsQO4yDrrE1+RGJ3WrJOEwKqy+UJ5zFg0O50zQeQ4IubJsEnKmDEIGRU1cyff8uNUaVuqp/wAJ/vX8hQ33A/uS5nxJxqn6HFxOhOKOAqGdj0bK3epIXLPFIk5pYYvSKjcb1m2a61f/iFkBtXNDzXSAdtKE7WbABjEsms6gjwoArkbUp872w6jb2BtyJgBr8B4M/MXNXWGIc6Lij624vqxYL5LosO7S1tNMQYBSfdhRO4KeLnAsTy0LoGL1UNOdXSlmOoFoCAWobxAlaGjyrgUaDEJHsV2zvk0tTRNqkUZTetFSUeoGO/vQFmTfRjIF+39BFqUdIEZnqJP+JvnQEZjM6XpcEQa3S4CbH2BZ2kFbJZL3VanfxTClox6mw5fbt7P3WdzvGo6nXHdg9L1X0OSdTjPWsEZRVnYtxtYiVsVBbBAQt+gibIcUZyGTQBhSFCBfWLNncZUbmBR/X3lMmwrKSJz+1uFlYHR5iFZ9mHjxHiOD0JtInZwWXcpSa0C8PHqQUodFuHhHnZ3MroDmexHyf0827XzGZ00TaSIGVNbGd2gXutEpExjrnpGj7vipempqZe6rs+JRy0cl2vggAr82w+uqQbmCgOeSqQil6UhImYz3cUyELtul11CTYlAEClVN5ZSB/Sj10NBI/dmtCwVV733wVv149m+mETPJN4zJbQIDYecKW2zb0eN8LxiEKZELxNgFmmifKEkAfQqZy1IhdSNJB9mBiYiEWqUxKAvb63Ncs1LO4mMda7kDE7bsZp9ojclQKjKwewINvHrfEO0LCFSV7R6TOSW6UNWysE1Izo4alZrNScDVMu/R4XQ39YadItLKXvcWmH86e7y+eK0FCZSvCmnxKkUfBH5UZe1hVHkaFHPeLdRtIE5+hsMRs9Bb27n3XTFT7VcJjyIGmhrpQcpEDwPePPpn/qeTYsVq9B+p8tLuzEehYgzoAl/0u9T+AF8RJSQpTH7Zo27ofChFwladrxQ6PpOuDxYCKdL4QkRtCuw7I5PO6RXabrCXGo68JeIOre/6XbGc3RZeoSYJBo13xUlZzoVPZ1UiCKhBlxq96HPPgQL4F2atty9EsyQvtlWLKYNoUJTzKAgjbsykXkyzlVO7VW/VFCJfb2xM0RNT9h24j/Wx3lRRK3Gs5qHCzTM+CA4zRJYsdkPkS/Yqc4rsH0JskE95aFY230yUjddOpVy53i6Su83GhdiJvd5n5MCcQoE5WhbyjRM58BVyCI/vBZIor06QQiTrSxC6U0176Iqp4wdF9R1pGJCD8UtCcseoBGxROmKK4vCVJCUgd0RVK5syAs0p6lbXLQDfdlSS8SbHwGpCpdRAsTqFK15DihERszlMyxLxvM9j3Ne+/HeHVlxmYUmL65PMJki4ey0i5eiwhQIjoxZvSzJkqWQqiPTmWiPVRe9PQh55upsSpa9OZzTH4E2y07GQNdoSn893mJxL4B+EkHQE0/P3ldBpsdD+pENtn0YxV9GFLbqhgoxlyTQhT1zlLDA3vHVv9937pvyNove3+9k9565zhOiu6VG9vaEDhPC6s4fU4jafk5U7moRcfJJu0d6m4EhpC4Wmh6xUE5ztKGgHw9sEjVbAglv1SW7hhGCLMZxXfVcc+5lJxxju88eW9B2MEZ9orV/bIn0UhovQuPyKiiwnHegN2rSY14S4dzEzADCP5sTgylh2AJSKOsEq7Zip+/qs4l4k9/zmxg60kQpHsnGMKzlySEZuBy25VDZqpP721zLGwb8hAyiyIxZnoUylrULgkjNuIHR8woVKow9qq3jmW7aVUjWLMQkFCPgsL10AiWC/rMFWY+EpZmrB1v/GVVIbkwWSVf0dWLZkFKGHBMPyXd+rkEznM6IrPS2x9bz/bA0YPktiPRQ/5gTTmbtixGCCGEMQkIkKEmUgAqgrDv8F9AZr5cCUNsfec25Ex6AbVXqdHKpvCwA7ohDFXZ/epHDXHhJYnAs4mA3e7qNnHgcT4091R/JF8JGUZ+Xat5saYbrGywD1I6EBKIVqvOD1+KyRwvuvZORWDP3jPJcVF4LQhbTiE1Ttz59YpvCquS0CUwH/tZVry1aB3Y9hwGea/m7HM4kZ3LvQ9wnYglQgiNwZH2COFH/ixM7SV2Uw0p4D85d/eOonhBWTh3m3jn91EjoVmUy6qMzFficKTbdSmlp+V2rGRHwWvK2gYbaRyh5UAlp0aSU0NhWK0HDHnl6lqTzoseX6EZZdrb4bV3IW7OrpPEBQg7cQ6hJKUJNFK2zePu5FX4yPpZt8Ohf3C894s3k5v+l3RY7UyyL8+njvLAWkADve7sMEilie40vfghlH+8yqi8qjRNv6vB42PQBo5dhiXCB6R8CwZbxBNpdo8/9tH7R/mmx0nGk+YZWw5VvQo2Rt91Yv0sHZS1yL4N6dArLpDk296mZ/PG2cFtefqun33ctFfwuCltkLDi/bsmRNX3ftsWFfvdqzfw9vdBNKolbFAu/fiyEP6Pnd4wt69gbtv7S5f4guD+J20gDyvF5cb38ThESzl1Hfstpg+LygwNk1wBr81XhCts9ZsOM7nAudtGX+2vVPK+RHY9UH4doHyXDn0QECV3MvIt7/elTqtpz3vDyakeC5GpezMnYO9J3zF2lL2++39C1X0PTQAxrj2BAvTbO+Clo67izEViBjGqNRqMEnz/tTQ7tC95zz5XLM5GpPTah9TefYKq5h2OqAlCoo1h5Hv3ErUn4NlbFCeakys8SX1hzVE7rQ0CehDZQU5c515n8WLRxfMcRPU64FSvbsq8EkbuiMp9IZFrWzbf01NE3bONlnd6IyOjuTlh8PT7d/ihkfsAwgnh+AwdgPygyyDvzppAZ38+nmmJf9WFpsfe7pi3tN6m56dXvYeZ2TIWJfT3gwED2Tn9OaBBP3fqZLb3ojsq0Esy/Reubo9kh0tsR8TvdxDujpXH0kykg3qdo3wQrqsrbiBLJbxQYGTRGdepwDrYhj1oUyQAhct+QLhklNsyN+pNCkWI/1B/4K78/eh4+EGUTaidmizoD7K3lpCftv1BY4rYumixusobPj6Tqc86/Jt0li7ECMCA4+hLRJSNHXLQUInWqnmAUKHoQgvjye0KoCiwXTW9p9Hnwi5XsfBgETRoUmSkCmuJq0DbWdfTC4tZm3i8zIhviSWYWKvMCxWq9MijXRg/jyQVqmmmW5/f8fuFQBYoVVqyxtQBzxQ3oMJNGooVGJ6ONctVKMnrpaRDxP4e6poDZV9xpwZ4fRWcoqETyBMxvsyRIcErLYZMehQGw5T0Rgloromofaa2ZtOblonhBPK+szDRRH2gms6dFmcfu5dO9Cyzli6CrKqayC9oCuTdTT63bsbOjz+SDfymN/z5tlVGHcQtFx3nivxT9qEaIpjCCCDj69rclxpJiAAfw8XILRD8xDFKhxGtTzNq6x4j8KacCuuDIccbS6tEDQY0xy1CyDkWnIboZ1st2BC01aLkHCNtJDIsMakGbgPGfnZPy+++IT/9tBw40iVOjeo1QuvvRQTH5qcW/VLDtfXfBY+He1PA+z2qjScfgemtfxjndIV4EQuacx+gdNJmhePxJnqMxZ6vmXESED34hoX09vY7DyKdltlW36msr+BxkVoyNjQZbM9BBc+6Hd1vEOSvcTR8+jy76z3QVhyVEL8FD+++rAl/VBIc7a/slA6n5t0tnqRs9RS2xjMkkY9IascSOifWaAHIaC5MSdqhHq4nY+eAu+UuVpEVuz7CpzIHmLDvNHhzwMsTXc3G6C+TWP5eAigTWEDQ0oIoZSDJ1+m2FodohPT9YkX3JCc4Q8oSFh/2pGTqG4X4qlVdZGXtGRJ7GnDE94sk34jrkubtiTOAmF7PZLgb3RxdG2IC0BUwAySN1YwYVzeV4bWu2sfkLgdhhlvN2hJ1MRma5DItGy9TZv6Y64/ceHjWy0MOY+buNXBsqnENqxWLlmc4CS9jsBYJ0V1mq7gLOUMSWXP5cwgyyCxUqrMss+lHoiuQ63keLfHHFZKLv/vvwzA5AeRZNJSO/b8uSDROFLU4hqQWQG20IUqVY/Hz1sSnWuCV4PU+aCGJLHFwamw5Hpta9EaSc+EZXeQPj2EOeeygmdFzT9C4JfFI4N4ZA/ZqGqHjhmBCg5Qkw1yBT+oujAZ+36X8kENHgATAmZmASRZIJf9KZW/WW8kngERx3l0is+Qe9hccEv1xu9cGua2AnisWgjCjrm2Xqbfsj/HS2iPKVGVtF9TxLVLV8YUwnCA+KbTs3GcJ9PkC8fV+Qs3d8AdM5ctb100kthKHAf1eOQYAEnOa9iUK2uXhXZUbsOSDsAyKq1k6F3vvae4zd/HkmLofnTHLGfVG7D6XTTHD7zJNElURH+eL1Ew5f9Lr926c5go9PQYFPmN4CT7+EqAbPX7w15t0RuqvHg47vFAhH8C9UAoDqnji+MooVlscA+gCXZVw48XkhYEZNPBZjGkCHuJTROEaveBeTOuYNmL8yEdLJrL/4soaVCTa/GL+6Av+lSQE1gSZfZRFA5W6v6sb096DeQAwUalXETAJkLBNwxts84j/txD50nQCIH1JkrsAu86cHaxLqjDUoE7wHd3YG8U0t8BKS792Uc/hHlZctO+yaPRvMXNLHcxMH+FQ6NBqTqqoA/8V+qD/6ZOV1KCyg8gRnj81byRVHilUSFS8e6zmWAv4uNbiflA7lj9UTpS0qoCg3RdSTlI51OBXOqfWrTkuKzu0EeieFwVSHOvgetDwBlJ/rgTPT3HSJaWDLb8nnyp+kEyucGxTSqJ4iEsvd+zGRC/I0pbB53bhV/Uczp2d41MF1smLQp6DVTeVNa3VTWe0Za/RALS8FlFXGwlnVn8o9OF2FmDO/FVdiE9ShCRhKO2k+oJZ1OKd5H0g/ukg91UDUYQLay9vo/JsTxzRkVwX5eO6XzvJTXlyJ7ZNQlbMg/PLcbf5kI5h7a9R0Ayntyg/S0jElQk6xxLaFgQz+j1XDGZGPu/CjhsPmKMIlbGlK/ZO7tomKk1eueO4m8Uim/9lgehwEcqFiYOblFcTCz9GDlDXfGLj+M3ZRSNfPd6COKrOtPHl49RRRT/SkkxMZajpBbbgT8YtgoRroyoqelCIe+c75oa8h1GjwCoR8KNqS+eeVww+lnc1Pd89IA3M+2F24WwBt7e8QFhox2eJ+eSqf9tXT0scyy0Oev1U6Mc+Iq1W9s+KrZQ9Ebp4XXfCmviHzmxiQnLgECsjvF07a3ErrpYaBGkZgTTaO9/+c76iuoC93suxIpcQ4F+VqlSFeHBrmUzoEjjl/Blh3i7/yKCEBYQduQgBM2j0/L++fMCWy2AjI4bv7/9e7HN2AOUDbiq+VuUonGOSo8o2deoRFkaauy/Q03fLKOsL2cC38HvQTxxKvkgLTJLeLYWEgbn9abO2IAzK+89I4wVDlnX2dKBewv4L7+01mWiTiRwvfH0HZTCSKnouR/PYslO02GjWyiUK9aBQbWGIrBQ039fdk1m5b7I3Z99zycatCU6gI5viEFuZEjVV5iPF3QucuaKP8u0I51gca7Ygtxi7vly+tvSWWTq2KLdTXfw2uwfGDp++6dru3pNl2dQueHUMXwDGpZ/eDDmrzWrEazndhevLDXlimOs+i5QOGC2pVn5BIcibrQW+UrL7s7EFF0CueqQKgMNZekoU3RTH0GaaNiD51D49gflhz7DuIMJJ8oXLRgCuQniMqhytQ+tqZW7j+/5Iey/Viv125AiXb+aMTyO8fnTLxE9WpiTmRoAa38XbMU6Db0IUkqOzm06p0aKlVEYy0symC6C5R0p+RMKdH2j0nWscwGfMyupt9At9hDLrNq0PoOJLpBVG5Dr8OflBbk8tD3E3kHHRXN0HdkFn+xLHDt3oH5nU9/ePxXVs5ADrVXC/WKDyxRClOliVjr2r2yrCyvI3NPC02COBB5UpWyOXPqL9fUKOq0orJhmWQiFKzxNzVm+FrP/avltx8lSv3csK2JZtyU9NF6nP8EV/CzTMrU/jD98VXyg2oKLEb8PPSgAZwdOzHO1B4JDHCEHslEzg5YAvvjQQaB04g1IbgDlYf0eySpBf0hyMQQBLY8pWK87C8gbK5IQiutBhrpfNS+GmJbUpvLivZYUKT5yuu+U9nkNzIPSaBLF3cawWPpae2gBKvhNOUOaKb7wrJ+eEaiMhmL2NNrJTuEVtKPWFG8Ibt0Bvhm6+xaG1D0T0WN7s7FwPG79rUMz09QhLIpS9Q2x64ykzWvdHo6tDHM31pzb8LMC6zibHpqRke1kuZefn70Z4pmpoNmGRMxKZ2N3fzA3fNAq+wM63ulN1uYWCSNGPaMtrSZ42lKlukoeicBpFN422xSk5ZbojzhU2yCqSczqzn4j/I683xIlZkZ3uM+mLkj32UY3KkZHQBvlyhr/1ddH6r8Y6W/jkoOZYGAWoL//aHKgF40I0oLvwLrLfP6fi6Z18aFTIQq7qRtgHXo7KEAv7QvndCAjHnqRYKFgSQqH+A9KBHfsSjJrXcT0I72BV91nrXyGVSMcjR32z97K2tDs0vEN5lTH8yGjShTiMjouc7QbNowODQjVLRs51EwStCyVybxx38NNmd5hiiaBUarv91YEtnqQEpK8By5pGTVb6CLscpFG1YgThTyr6dTB2WV+QWiEbGZNOKvDmM9TOT+891emSkPUtIlfLEV/vpqE9eaSf5kZj3QVVrkYQFBOkCYRw7LSHDXZ0a2+L2xV1UXt1zcZE1HdnHNW9JyOHUMMic0CXuyuLhxb0gLTcbd3FLQTd5VnzETFJ6MYlDMccukJY5pbh1eH3cTnkJYqhO1TIJEc2oDzJHvE9UubI2mshkGWp0ASt6HhuM5KYRPm6cbyiZbHc0OMhS5A45WUt1JmIRTL09bU3ZC7klGH0WJrjg59SIz4bAtp4wJug03Jzk4XQuxgOQrNWs95F1es74Cz3V0VuErpPMoWLLxb6RtD2KWjZnMErP870JNH20UK7nacVbmt5Lf3Adi6fw7Q7q61RYCLyIWli9pX0voGRfAVF6zTY61MuydPdrcmW6EcoUl89tP83CAzpTa0NHlugkWd6/Rm/hPv3gjN6ry50InOwli49P2KpNbQS050hJszILZYU9spP4sjDTDRcBuz+RB1yoqytyp9pvUIQnSXH3uqkOYF93g47dk+cnN9/PC6zANIJVi/21UfJAA1Pzi4s4J4bWiNCxGPCd2N9pkW0uOeP7QcpPPXVjMpzyJj3c1S5456eXFO67aCp3Oydz7LqnLMRysoXgAWOoMDXGBGe7dQfbOyjYRQpVoYQeoJCdCo5vdXGUqjZhLI1sJpUQR1DZhJ3sSmknyFs4lWgT7udnSXMkzusJKAjMm7O414+0MTL8IelF6klrOUr/LMVv2/D2V2bdJxYEa5zWCqFx2/3vmIruQS+fwF1exRkyp0/dOAIN40tf39QVhk+o+sJPIWU/fxN9W2gOTGa6lzfe5vDla1iVxcslNn4HoxWHUPTY+WaaVW5FSgRZ5G7dY+unn8vgoKW8EO0hgqkYmAYU6wY+rpPzGfwjXVZ7PYSHi9oV0f/UT5p4HtJL5wZX8R1zmKTrjayhZVPUXKZ32ZRNfAaS6OiNf0lPea/zwiz1Isqzwbc2CSFewSEflZJ3fSoz1BJn6rrnnEgNjoQZ03CHrwgjtOWqjACLYBQ0ldIrrBkZG4tgcKYBEMCNjUCRyo7UNrL+YYasWdRV1lXoywfkHT2d6Bxo7saXyUGYjP1bWfadAN+WiLrVnBxMaMqvs1fIhAya7vhFxi08yfxPlyPw9ksqWYT9J8G+6LzIjlikFyk1qtl7ee5B665y9hAXgT1GAAbtvm8+HkYRMXeg3aeCnsUU46G3pfT2VHtyzoJGivYwvjhGdqZ1lt71rs9/sWixAJLeMch57sRKABQLFH8q13nprH9jsWgj19NV9/AgTHdDSc/c7kxjbtlgc3/sc+28g5c5aI8Ah4sZCKnpdQ+ruDL3vabIasNvl71uFcOpcwbwL9S+pB2SFM06K9lSmK5ZM9dDPOnqx9xtL38B6TduD0mdvgINURPbQaczN+aa3rtneQ8NMMtI7OugcK1ZQ/fB7hRHE0UCUbPwGk2YuYCwdGnBMur7n8lNyU5HqpGtA1muh5kBWlECANalzI/WJeeTSFqFJQo8qsX8qftpgYXS3xPOoPLOBhhJMH3elM+bmnzkS88nBGbGv/8maoNKm6do01iro/5/sN50Tskd4FZ7xwnEOSJIRyqu2CjguLpYVzNX+ILJGBu+I5S0fnFcPzOUhoEvmkdqoFknkW6d3zxkGwamC/goLJ93LkZ5E+Lo18BKeSG9ICWvZCGgwthXgN77Pc7VswJKzGw5XEjt8No8BEVSHCq44N2FTK/tfh413MMtJr3Sn2Xwe2bJLtJJ75zRitKJ5icAXVsizDpRGVhW8mmiizV0OPYhNptAWLmqXrTN2nd+z5UPz6azOaw57g5QYxFlRg6u3Sv568dPqCBR8SEe77m78sKvmgSZYDpEJ3yMd8ZSqPCkZWpIldRwK8X6oCddAOMP91la4zTt9VBzt2pputX2qtMdhd3Tt8sWlI5luKh/Wc8R6ZQ5s865roUJhAoOvCFnqry4e1QKJJcz0MlLG7EcxMWZeMmxl7lJ+JBV4cpEjJZb1VJPHNzJKy8mhTI46Cwo6m+yazpuq+hTvUkY5QLemcSVNpGkfX3DAdRpJU1AtAxYjHidY4zQJ+ysXaHDJa1Ys3plxl+CTUIMLbauDlUNQSQ5D0D4gMytm2a3hDLMPKJzWct9Xfmsag1osybyCsNQjbIVDLIDmBZUjqf3uRW1sfz/B/rMaK6QR7EUHbhLurLURnH7Tc+nxnp7gtfIB+8r2oCmftQoNFbECb/8RZ5jE6SsbQ8Ri/MltnR0VA7n7kx1CxNEpzASLQadKUgVQaot9ZJDgw16kbkt2ppN4M2bZ4erZhLlEJYa0kIOTsd6vc6P2nvBOapnqBdBOHfsLWFtY851JLQnmltU6jQid2aiuCg0LItWpI4U1wYWQCgz4HnVHZdRPuDdz/VlOR23DX4ogykq4sIcLfQPL0CkVlufwkDulxLF06OgfLfJt8kt3+tew5DfHmuxUwK+6uj/mStBMmnv8BvQK7z87EuWFVfHrqGmUwf+p4WIunt9fMPiBRdm09NWqpvcwNy6c4usBNupBe4i2GTQAg4tJIdNo4T1BWF+XYvsZKirll4KM9ebp80c0fB91/NYCW/mrUtl1qMiE9Q99MjNprtylgH+m4lD/tYYpZtVpsSvsk1VWH23dsYL9JibLLGivvCpYb7qMU2oB915NoC0/yAhKWdcJf+Jy/ogBkc/Y9G/pPN1wt9NYeZmKmiY2yTpsZG31yanTrY1hpwwdNCFdy5hnGR2O3B9vEchZ0uOxKZTPzuF/nUqOchU/4IqwOnRcLieu4nwDZXmcGsDdEyIX7VJUh/Ye7AvreY1w8thj+MEWO0oOdFFfO/d2kupqXhRHFffndj/D1dhybee7z/oU5WnOr3X345jlgijkL5h3pbdHqKvYFZIThquCeKzBaSm3GZmfq1hHToELpfAlc60nre0lqGtGe63fMsBFWPLMwRa3BFV8YQN4WRkVCxo8CqQH2xrR28GlZsmRXzS1QYIKB1cdmLYj9g+WLbOK4TxF1SqaZ8oK0mskG1LB7QqXyERskp+E0Ve8XlVSWn3ofpc/JmjnHrZ7SBpKtAASXDc6rFZEoLtvRYbgC36JdNY8+k0K2gsJ7w3SqYv7MZ2boRrgCYiEQeKyC1SUyfqIr2bCtEg4rp4ptgjK6GDeavpZx01oeBm6AEqHoF7NZShJC+/qwHsjBisFF7DdOfLCgE996BRmyf9tHvbHdql68r0UpKoky5cYgGHNrw4IABRksw6kXW+iY9fjOLLIgFuzrzMYnSvbtPkU9O+mhVBTaKP560xvksu+Jut/de5b8Fg62SnGxwyjPbFt6Pkg1FrQ1j2nd3/ASFgaJzq695Og7aTias0upX3RoGByqLgVR7iQSCommifiGUE+DSKTsXssTA/6ugq2Pfus7EKnU4XhjUV4G2wXK2tMymhQVFJg16YX4Y9MnE/noLNrYwznasbyi8wIn+0AejdvEmISxIYxSQvhIFCSJJ6kNm6wXVDIpIfj5J2caZbIgu89TLu3sjBOQGxmhDT7AjyTsaO76gm63zXw3EZEpmiL9FsD8CBRNAogGI8n6PvEoILJsdYdVRWHk3BBHXPvGUC2Lpr6B9FHJgfpVCKiL9nyOptUtJSUpHXx0UYAJUf3KPgUelbCqXlQBE2NXmxFCD0XqmsR+xQjXDu2QIjfvC0ZUrGl+l+Gy6YjyOtohBim0IGzM/A8/esXVZ1182YKf3NcsfN4JSV1ADdDtestfckKeiRxtDm8m614N1ziDAaeBL5jjqyMsUBS4LhaQgH3nJUzLoFAxNJokgzlTI/tLBmcbL3CHZMZfy7fjZc02tDzEGWqlR8T0Jt2h7TYYh/8nKwE8RcNXN3yD/kfO1301eXO09ChauYRfNpo7KMdi40Dk/1x0CxDG/f5zAyJ5HcAhGdJHdOIwhj7Lz7OG38jqKSu66nPvJ4XgYDrw8cF892utjCmfMCotr5CWlW21EU1A5H2tNUA/bfPbMhUkZOjZhDCb9wjqj6VRfYvDNk536v/7QCZ4eiN/qzzmqnEimgsRcIvjjgQou/Zh6sslbKxMaw7GX7xQzvGpMyop9+y/dWI/vd8W6AzVdkbsUoQb/69Ps2ahfOmKeeztf3SXmTcQMgR3GAEBZHVFrZJuUNAPu4MXK1M2p6OdqxgqZFUM3MoVc+wg1JGzg8+xReTR9/7Lv16ENQP87I32awFpZAP5rdiK7KjBUFuR9eUnK652geHS1aJhyXxJf8zvJAY/fdbF6ku+mCL6x5/FKelEKUjlQEcSHkwhUsG1tNuGZp0a+3u3mJoMRY4FTXUHKzbjd7XSj5iYCUqXI5pLKxkwvhCdea/uw5y9Q6p2MRMiltWWoe9DMreQ0A7c/fuZoLTwwY32/m/ktziA6BFIpyKp/YIVtyOBsMFHF0MafZWnFQqB9oR+2yP7FbDbO24D6L4NqEyb3LAcgDbF1d2/cn8NJQxaXTtQ+CMoMqzPtlmIPt6ySJQG7m1oTZUdc8L5pVQrG565I4KnHXaIVAvh4qlVNwXtswBaXEzYbWsIQPgVga+JACK7RznPBb5eMaxgP4CyHvLbfbaULD9XblQn1yhKybyk9GRIZvg++EYq0IMStCrhKOQvvmcWWJMUucb/y3L864HAwq+eWjw17D+7FaM0NnRnWVKVN7cH+cBQ7tIWQWIJFmFbJ1o1T0pUDk4xad3QJ/G6GbVOn7qdD/TXGR9bToKPzfCNSuU8mJJTxQEBfTnM9elRPoGLwx0FG5BrM9Kd4RSDg955qRHAuEG0oHXmIm+9UmGMQu/ZRVfWnLny17crkdzuqBs3Mo2c5nzVaiytUBpdtXmlPFTxy9G88Dwm8NgAopinu5xdhGn5J95xNwqXiXbEIfyOHNQeQwIT89pDqhLJdbT93k/2SL0p2bJduvQx34BPw4oYQyI59yHns3GdTElm9iIkkq1ZcWilXwtH9673l83K79SVSeJL5SpBynUp+QaErWC+Odk49H85wgWUEz9kPge0tP62ip1Y94/3pRvDU/9V3PBeyArd15EuHRB6AUN67fcW0K6gxkymTpzlRTxKVjC4Joj3WMhFLPSitAedHZI6I3Es8U5JQGAclq44VQ49qnZqWYepJz40BzyZcK0JytZO7iBpQ5sjyOlNSbDEqlqwRKTRMqES4PYdYzZYghah3m+nbqr2Sg79QRmhQvYUf99Bu9J4UPYgyR6dC1EaKC5aOUcPIIuBQIe/xNBP8XltNTdu2yrfwM6SQndRqEPdtPi06quZNjo1328V8/d2JsRfBLjPgbS4Z74rgz+bME4XsHuVas5Xq0lXbJvNXeUib/vDlfJkT2R2G0n5GH5bp1Oq3hWbFfZvHxDbpqW4pih8+qzUgQXLbkkTlS6P4++YKD44shsn4HH0tfvkgpnqZ4r9+1ZrFK8HRE351e1TeAruU4VmhD8RkXozTW8zCGap/gGUiPN7QNScTmEjkT08DarC1SrbTzw6NKb8vKim1XronQKGyeeLvYGeDEniDh90S5SwWiKK0Foz1OalgumB6yesiIOgUzSGhqwnYTc2+xGMqZ+PVUfwMI4mdUcAvbrBOuI/rSLsfvhSrcETzNhJXEmv32BMpUHx3M3QT0T+S0PcQpckdAyAqjfYKjkYjafefTykV9wPDoqga7ni0EC3/h5CHYaDgP+QHc9YqNUGxg4NT+1+rLdD7HqMIzkZHl04UMrDDtKwamCR5i122N6jZj2eWEsSM3i5JnZ60PzIX+C/lmkMW5ie00O86YO2/A8wK3IMGc+CX5oTsRk7CIW/vZ9fseKYHjPlTmCNKGhoAk4BoPjQqe8z5sL6IPivbLRz/Cvr4uIZfg4bYwYUvE5qOmgkI6VVXrPXhf5OMdvY2Uo2CFxpZL7qUuZM0PjidtDTAY5zx0l9TaerDShOvBfxLfVtlpQnh6j5eoWRz7/sskTIAEryB1j1AxnfFEyKo8tIh0uqlSxns74FbxmrnCLhmMICUBMWlb4SmT+OaCfO5Eii/kYrlHCFnkxWdwd8GFwxszyBM7dL/s8jKQvVMld8ApgJvIrjlXKv3JSjCRlR5eGlyWTKufCp2HWBQkAZbw61C26dTZaoWb88zUwK4sy1mxoCgCRKghId8B6eGDZblnAc0Dh5jfGM4BdNHfd4TMJcQKnLPpJ1h9nfxZrRKkE8YkC3m7fiPQ7VvRSik15MFHHK7pomxvCIzUyDko/xX5/ckSzqBSaa91eNmvTAkKI5hwEue4YchU4/BxoYURPlTQ1NkeBK+E76BBc+5k0Zw7cLmfu3Jj6BSk/F8mjDHgyRwyp3h9dZ7b7s/gB21eJ4zRWicF3kaiACFWjHZKQhDHYurpkAqrZ5K+JnjpL8L4HIsx6K+pHFt2qF0yyUmQFNJ+CL16noJa+qCYbQE5A2klxaA94jv2rkVuaQMtNJCRTNWV1dgwWxncGfpJ8TB8KyTWJsTJLUW17xOr+ftT8Hd5GiZAohKdRr2Y6D1it7THGn6/MH9s73HstITfhkJ3n1dS99+ZK/EGXNsDmpRkXTPJvELtas3f+5GullsmwQh02dFBE6GcJperwV0ISTm0Nb/bwo2gxztDeecCFxItuVmy22z5znGfr7mC8pxdu85MDwYQ5yXi8/XSBXvD16LJjnKCdteuLsu50IZohhy8bNbVJPEWI8zTRGQyRFTNnV1c811rUs1sBoSB1ZAZyyxG4lX8DpZhs1Y43UWjWrvvaIj5/ATksAFYw8ESni712k7fS2y/sNDb0f6RhCAxfhtqtN/xkWasiCkbnnbKJxuKgVMQNJdTuFO+5uyTyLOuY0zHDEO8nHVnz7KWZ2pHnWcnRNh0F9t0mXciqdHoGgGsGtfvh/XMxRoANb0sG+BUbj5z9pBXDEbHnkSyL4zz0tv8xMV6YSqqTu2eQ3JJ8uue0y/ArJvR/t2RxYlryjRok4x/bD16KGOGi0mJmdehArnLLPq15DfSXpARj7up1UxQ/EaOObe/sflTK/jaYCEnDKXmFTrYIbBTg8wt31Xk7mnDiuonHQ+jmhUGdBxuCzZQdO2is9+z/dLJ60hHOpt/8GtCCenZ1l8et2eRD4RLBwJNf2VMrIhbdG2/fkXxm9sO9g8CJl3B09tJXyOD9U/3t+tUuIvkDvsg+5xiQQGPE2w7ulU0MB/tutcbsPp06SZ5flmc1rxTdgad37zV6r03wecpf16VqZpS5OJi7t7n1icAx5GPJjnZNsh5sI+bOl6A75QPEmkie7fvqnGLvT8aRxjKOzI4yyMB0zIyqA355OGHt0CW3w5ZV6AmCJgrY01pV1M+u7jrduKcrWcfltaUT4C8SZcI3c+ysj4W8ODb/q1Safj3uwEdCirjPMGof8VlCIBKgUiFm1sBwv8vmAuEyRHnXLlW/0hCDIdBFQqwUAKk5As9EDmAvOeOS7QTwnop5EIkbPhdbLFLoj+dg5CjZFKQ/+k3SbMNQATabpDdBLOY5ub5MxqGxtNaIg0Ab6uNIQPgGILOHt4VInITiElPHhqPRK86yxeHfhA3Z+o16PXn7aB08o+BKXEtcdAumHNTk9kyMmvuO3yNcl8sfmozdmuE/0ch0HmuZiLYf2psbxSaosunfDAX4zdBtKav0Og5JIfTROPLM3DGoj9vuW/fjRl/c/Zfjs/RZRAG4fVoRzDE9SfP6j6oOR1e9db5VmZC3rfAzIFwCbwQ5gHMOhv/9QvyhVbIv1eNECFcQXjc8V0d/xbrU9uvuk1F9p8qsOutwWpryvcI4eiG2KMqHS1IjkwCuD8B7Z4XMyIojQhAY0w9lATThUTTTa9gCfmd3G8ZWOYRTSIH0ylHJs/Nta+FpugslKgLr3LNfLCJc9kEYSjtIeaYXHAmOSr5q3hPqo9GLMeD0rApDdiDxCgmhFjZCTa681HubA8EMRqaHaSYvfEFcVqmrsy1VDqV9ZzBtMCTl1UDJIWRLmNZY62cHKd/KQvf35gXfGKmwQulsW48rADtQkRRNo6gF8Xbd+hEV+13nJa5CswwsvFDC3XtAQG1QsZ+dgFyt1lJ/z+/dgvnKFIDEwByOMPVNpejM7hVPABZy3lFtQ7AIfiZTfL4ABoIw4GlkMGc87Bg2jigvb13oJky3NjxxxpE/1O44A==
        - #2:
          - type: tool-call
          - toolCallId: ofrcOp1247lGh16O
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Private: 100
            - Rationale: America is a direct neighbor and currently pressing Damascus hard. Maximizing our relationship values will make America highly receptive to peace offers, relieving critical military pressure on our western front so we can focus on building our victory wonder.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: WRxO3JOSxiQPAIgi
          - toolName: set-relationship
          - input:
            - Private: 100
            - TargetID: 4
            - Public: 100
            - Rationale: Morocco recently nuked Calixtlahuaca and represents a major threat. By boosting our relationship modifiers to the absolute maximum, we maximize their peace acceptance to end this devastating conflict and prevent any future nuclear strikes.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: fS4wuNQuGyajQ0IK
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 100
            - Rationale: Ethiopia is the Inca's vassal. Aligning our relationship values with them will ensure a smooth transition to peace once we resolve hostilities with their master, stabilizing our eastern flank.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: hAORIOksYqLYbKem
          - toolName: set-research
          - input:
            - Technology: The Internet
            - Rationale: The Internet is the ultimate Cultural Victory technology, granting +50% Tourism to all cities. This ensures we stay dominant and influential over all civs while we work on our final victory conditions.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: N3ZOru5bNpJcB247
          - toolName: set-policy
          - input:
            - Rationale: Great Leap Forward provides a free technology, which will let us instantly secure an expensive late-game tech (like Robotics or Nanotechnology) to reach Future Tech and unlock the Citizen Earth Protocol wonder much faster.
            - Policy: Great Leap Forward (Level 2 Tenet of Ideology Order)
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: YgpvzJ4DyJ2Llxh0
          - toolName: set-flavors
          - input:
            - Rationale: We maintain our Culture Grand Strategy. We keep Defense, CityDefense, Production, and Wonder at maximum (100) to withstand attacks and prepare Mecca to build the Citizen Earth Protocol. We increase Science to 80 to speed up our progress toward Future Tech, and raise Espionage to 50 to protect our research cities from technology theft.
            - Flavors:
              - Wonder: 100
              - Offense: 0
              - Gold: 80
              - Growth: 30
              - CityDefense: 100
              - Production: 100
              - Science: 80
              - Defense: 100
              - Diplomacy: 60
              - Espionage: 50
              - Mobilization: 0
              - Culture: 100
              - GreatPeople: 50
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 5zGueEDSw8ZZAcSd
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
          - toolCallId: ofrcOp1247lGh16O
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: WRxO3JOSxiQPAIgi
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: fS4wuNQuGyajQ0IK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: hAORIOksYqLYbKem
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: N3ZOru5bNpJcB247
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: YgpvzJ4DyJ2Llxh0
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.