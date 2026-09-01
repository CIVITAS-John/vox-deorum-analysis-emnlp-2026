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
        - Rationale: The Inca is our main competitor and has a huge military. We want to establish peaceful relations to secure our cultural victory without military disruption.
        - TargetID: 0
        - Public: 50
        - Private: 50
    - #1:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Public: 50
        - TargetID: 1
        - Rationale: We want to seek peace with America to relieve defensive pressure on Damascus and stabilize our borders.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Private: 50
        - Rationale: Morocco nuked us, but we must prioritize ending the war to protect our cities and focus resources on building the Citizen Earth Protocol.
        - TargetID: 4
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Public: 50
        - TargetID: 5
        - Rationale: We want to seek peace with Ethiopia to eliminate a distant threat and potentially gain their support in the World Congress.
    - #4:
      - toolName: set-research
      - args:
        - Technology: The Internet
        - Rationale: The Internet is the key technology that increases our tourism output and is on the path to victory.
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: Great Leap Forward provides a free technology, which will significantly accelerate our path to the key endgame technologies.
        - Policy: Great Leap Forward
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Culture
        - Flavors:
          - Culture: 100
          - Mobilization: 0
          - Diplomacy: 60
          - Espionage: 10
          - Happiness: 30
          - GreatPeople: 50
          - Growth: 30
          - Gold: 80
          - Science: 30
          - Offense: 0
          - CityDefense: 100
          - Production: 100
          - Religion: 15
          - Infrastructure: 40
          - Wonder: 100
          - Defense: 100
      - rationale: Maintain extreme defensive focus to survive the world war, while maximizing production, gold, and culture to build the Citizen Earth Protocol as soon as it is unlocked.
  - tokens:
    - inputTokens: 19513
    - reasoningTokens: 7458
    - outputTokens: 369
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Grand Strategy**
            
            I'm currently revisiting our overall strategy given our position as Harun al-Rashid. My focus is on how our ancient era strengths align with the victory conditions, particularly in light of the Vox Deorum map type.
            
            **Achieving Cultural Dominance**
            
            I'm pleased to report our cultural influence is progressing rapidly. We'll achieve our goal of influencing all remaining major civilizations in just two turns when the Inca reach Influential status. This positions us perfectly to secure a Cultural Victory.
            
            **Evaluating Ideology Options**
            
            I'm now evaluating our ideology choices to secure the Cultural Victory, specifically checking the requirements for Vox Populi's tenets. It appears we need two Tier 3 tenets, and I'm confirming if our current selections meet this, especially concerning the Great Leap Forward.
            
            **Confirming Tenet Tiers**
            
            I'm re-examining our current ideology tenets to ensure we satisfy the Cultural Victory's requirement of two Tier 3 tenets. I'm verifying which of our existing Order tenets qualify as Tier 3 and if we've already met this criterion.
            
            **Investigating Wonder Prerequisites**
            
            I'm currently scrutinizing the prerequisites for the Citizen Earth Protocol wonder. Specifically, I'm verifying if our research path aligns with unlocking the necessary Future Technology. It seems "The Internet" is our next research target, but I need to confirm its role in this process.
            
            **Researching Future Technologies**
            
            I'm currently focused on determining which specific future technology unlocks the Citizen Earth Protocol. I'm examining the available options, "The Internet" being a key candidate, and cross-referencing the game's mechanics to confirm the precise prerequisite.
            
            **Confirming Wonder Technology**
            
            I'm clarifying the specific future technology that unlocks the Citizen Earth Protocol wonder. The economy briefing suggested "Robotics -> Future Tech," but I'm verifying if "The Internet," our current next research target, is indeed the correct unlock in the Vox Populi context.
            
            **Securing Victory Condition**
            
            I'm re-evaluating our path to victory, specifically the Citizen Earth Protocol wonder. I'm confirming if researching "The Internet" will unlock it, as I previously suspected, or if another future tech is required, especially given our current research trajectory.
            
            **Selecting Optimal Policy**
            
            I am confirming that "Great Leap Forward" remains our top policy choice due to the immediate technological advantage it provides, accelerating our endgame objectives. I've reviewed all available options and confirmed its superiority for our current cultural victory path.
            
            **Defending Key Territories**
            
            I'm now assessing our immediate defensive needs amidst this global conflict. With cities like Tenochtitlan critically outmatched, I'm prioritizing survival while pushing for our technological and wonder goals, considering the impact of nuclear threats.
            
            **Prioritizing Static Defense**
            
            I'm confirming our current unit composition and supply limitations. Given we're near capacity, focusing on robust city defenses and production for static defense and wonder building makes perfect sense, aligning with our extremely peaceful and friendly persona despite ongoing global conflict.
            
            **Enhancing Peace Negotiations**
            
            I'm now focusing on actively improving diplomatic relations to facilitate an imminent peace. I'm increasing our relationship values with America and Morocco, aiming to make them more receptive to peace proposals and hasten our return to a purely peaceful, wonder-focused game.
            
            **Improving Diplomatic Stance**
            
            I'm now actively working to improve relations with key civilizations. My focus is on ensuring America and Morocco are amenable to peace, thereby relieving pressure on Damascus and enabling our return to a purely wonder-focused game.
            
            **Improving Global Relations**
            
            I am now focusing on improving relations with all surviving major civilizations. My aim is to ensure they are amenable to peace, thereby relieving pressure on our empire and enabling a swift return to a purely wonder-focused game.
            
            **Clarifying Victory Conditions**
            
            I'm confirming that an active war doesn't inherently block a Cultural Victory, but peace is preferable for wonder construction and protecting our assets. I'm also strategizing for the upcoming World Congress, aiming to leverage diplomatic tools to secure necessary votes, especially by improving relations with Ethiopia.
            
            **Using Nuclear Assets**
            
            I'm assessing our nuclear capabilities. Given Morocco has already nuked us and our own Atomic Bomb is nearly complete, I'm considering the strategic implications of using it defensively or offensively to protect our interests and accelerate our victory.
            
            **Considering Nuclear Deterrence**
            
            I'm evaluating the strategic use of our impending Atomic Bomb. While a deterrent is valuable, especially after being nuked, actively deploying it carries significant diplomatic risks that could hinder our peace efforts. My current inclination is to avoid using it unless absolutely forced.
            
            **Confirming Grand Strategy**
            
            My current focus is on confirming our GrandStrategy remains "Culture." Given our near-complete influence over all other civilizations and imminent wonder completion, this aligns perfectly with our path to victory. The selected flavors also strongly support this objective.
            
            **Analyzing Diplomatic Tools**
            
            I'm now reviewing available diplomatic tools. I'm checking for any missed opportunities with city-states, like Dublin, and confirming if our current persona and relationship modifiers are optimally configured for our endgame strategy. I've ensured our arguments are perfectly formatted for tool execution.
            
            **Improving Global Relations**
            
            I am focusing on improving relations with all surviving major civilizations. My aim is to ensure they are amenable to peace, thereby relieving pressure on our empire and enabling a swift return to a purely wonder-focused game.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: F06Wgze4VYs2fFHW
          - toolName: set-relationship
          - input:
            - Rationale: The Inca is our main competitor and has a huge military. We want to establish peaceful relations to secure our cultural victory without military disruption.
            - TargetID: 0
            - Public: 50
            - Private: 50
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: PKnXonNAUyJb1AYw
          - toolName: set-relationship
          - input:
            - Private: 50
            - Public: 50
            - TargetID: 1
            - Rationale: We want to seek peace with America to relieve defensive pressure on Damascus and stabilize our borders.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 6P3uSmgfzvE06SLy
          - toolName: set-relationship
          - input:
            - Public: 50
            - Private: 50
            - Rationale: Morocco nuked us, but we must prioritize ending the war to protect our cities and focus resources on building the Citizen Earth Protocol.
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: CkymfXWC3HQWYmFz
          - toolName: set-relationship
          - input:
            - Private: 50
            - Public: 50
            - TargetID: 5
            - Rationale: We want to seek peace with Ethiopia to eliminate a distant threat and potentially gain their support in the World Congress.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: fV6FLlSjgqEtDH1y
          - toolName: set-research
          - input:
            - Technology: The Internet
            - Rationale: The Internet is the key technology that increases our tourism output and is on the path to victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 1S7lOAlVH1EwY6Ju
          - toolName: set-policy
          - input:
            - Rationale: Great Leap Forward provides a free technology, which will significantly accelerate our path to the key endgame technologies.
            - Policy: Great Leap Forward
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: SzHNlBEjx2d6m9BG
          - toolName: set-flavors
          - input:
            - Rationale: Maintain extreme defensive focus to survive the world war, while maximizing production, gold, and culture to build the Citizen Earth Protocol as soon as it is unlocked.
            - GrandStrategy: Culture
            - Flavors:
              - Culture: 100
              - Mobilization: 0
              - Diplomacy: 60
              - Espionage: 10
              - Happiness: 30
              - GreatPeople: 50
              - Growth: 30
              - Gold: 80
              - Science: 30
              - Offense: 0
              - CityDefense: 100
              - Production: 100
              - Religion: 15
              - Infrastructure: 40
              - Wonder: 100
              - Defense: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: F06Wgze4VYs2fFHW
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
          - toolCallId: PKnXonNAUyJb1AYw
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 6P3uSmgfzvE06SLy
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: CkymfXWC3HQWYmFz
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: fV6FLlSjgqEtDH1y
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 1S7lOAlVH1EwY6Ju
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: SzHNlBEjx2d6m9BG
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.