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
        - Public: 100
        - Private: 100
        - TargetID: 0
        - Rationale: The Inca is the most powerful civilization and the master of Ethiopia. We are only 2 turns away from achieving influential status with them, which will fulfill our cultural influence requirement for all civilizations. Establishing peace with them will secure our borders and allow us to focus entirely on the final research and production goals.
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Rationale: America is our immediate neighbor and is putting heavy pressure on Damascus. Establishing peace with them will stabilize our frontiers, protect our cities, and allow us to focus on peaceful victory conditions.
        - TargetID: 1
        - Private: 100
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Morocco is our neighbor and recently nuked Calixtlahuaca. We must seek peace immediately to prevent further nuclear strikes and devastation to our cities as we prepare for the final stages of our cultural victory.
        - TargetID: 4
        - Private: 100
        - Public: 100
    - #3:
      - toolName: set-research
      - args:
        - Rationale: The Internet is the ultimate cultural victory technology, providing a +50% Tourism boost to all cities. This will secure our influential status with all civilizations and pave the way to victory.
        - Technology: The Internet
    - #4:
      - toolName: set-policy
      - args:
        - Policy: Great Leap Forward
        - Rationale: Great Leap Forward is an Order Level 2 tenet that provides a free Technology. This will accelerate our progress toward the late-game technologies required for the Citizen Earth Protocol.
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Production: 100
          - Wonder: 100
          - Defense: 100
          - Culture: 100
          - Science: 70
          - Gold: 80
          - CityDefense: 100
        - GrandStrategy: Culture
      - rationale: We are focusing on a Cultural Victory. We maintain our high emphasis on Culture, Wonder, Production, and Defense, while increasing our Science flavor to 70 to speed up our research to the end of the tech tree for the Citizen Earth Protocol.
  - tokens:
    - inputTokens: 19534
    - reasoningTokens: 10507
    - outputTokens: 399
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Trajectory**
            
            I'm currently assessing our position in this Information Era, specifically our research progress. Satellites are a priority, with an estimated thirteen turns remaining. This informs my strategic considerations as Arabia, under Harun al-Rashid's leadership, on Prince difficulty and Standard world speed.
            
            **Revising Research Path**
            
            My immediate focus is recalculating our technology trajectory. The prior assumption of continuing satellite research appears to be a misstep, as "The Internet" is now an available option. Given our pursuit of a Cultural Victory and its significant tourism boost, prioritizing "The Internet" is imperative. We are mere turns away from influencing the final civilization needed for victory, making this a critical juncture.
            
            **Checking Victory Conditions**
            
            I'm re-evaluating the cultural victory requirements. It seems I overlooked needing an ideology with two Tier 3 tenets and the Citizen Earth Protocol wonder. I need to verify our current ideology and available tenets.
            
            **Verifying Ideological Tenets**
            
            I'm scrutinizing our current ideological policies. It appears there are no explicit "Tier 3" tenets as I expected; the highest level listed seems to be Level 2. This requires a reinterpretation of the victory condition's wording regarding tenets.
            
            **Investigating Tenet Levels**
            
            I'm perplexed by the absence of explicit Level 3 tenets. I'm reviewing our current Order policies and cross-referencing them with Vox Populi's ideology structure. My immediate priority is to confirm if "Communism" or "Dictatorship of the Proletariat" might qualify as Tier 3, as our proximity to a Cultural Victory hinges on understanding this and securing the Citizen Earth Protocol wonder.
            
            **Confirming Prerequisites**
            
            I am verifying the exact technology prerequisite for the Citizen Earth Protocol. My current assessment is that it might be "Future Tech" or potentially "The Internet" or "Robotics," which requires a deep dive into the available tech tree and our current research queue.
            
            **Prioritizing Internet Research**
            
            I've identified a critical update: "The Internet" is now an available research option, which directly supports our Cultural Victory goal with a significant tourism boost. Given we're nearing the Influential status with The Inca and the need to unlock the Citizen Earth Protocol, I'm prioritizing research on "The Internet."
            
            **Securing Protocol Prerequisite**
            
            I've discovered "Robotics" is the prerequisite for "Future Tech," which itself is required for the Citizen Earth Protocol. Since "Alternative Energy" unlocks "Robotics," and "The Internet" is also available, I'm prioritizing "Alternative Energy" to get "Robotics" unlocked and subsequently "Future Tech," as our current tourism is sufficient to reach influential status with The Inca in two turns.
            
            **Securing Tenet and Technology**
            
            I've realized "Great Leap Forward," a Level 2 Order tenet, grants a free technology. With "Great Leap Forward" already set as my next policy, I will leverage this to obtain a crucial technology, potentially fast-tracking the path to the Citizen Earth Protocol.
            
            **Prioritizing Technology Path**
            
            I'm recalculating our research queue. Given "Alternative Energy" unlocks "Robotics," which leads to "Future Tech" and potentially the "Citizen Earth Protocol," I'm now prioritizing "Alternative Energy" over "The Internet" or "Advanced Ballistics" to secure the necessary prerequisites for our Cultural Victory.
            
            **Researching Critical Technologies**
            
            I'm recalibrating our research focus. Realizing all remaining technologies are prerequisites for the Citizen Earth Protocol, and given our proximity to the end of the tech tree, I'm prioritizing "The Internet" for its substantial tourism boost, especially with upcoming ideological conflict.
            
            **Assessing Military Posture**
            
            I'm currently analyzing our military standing, noting a significant strength disparity with The Inca but a favorable position against our immediate neighbors, America and Morocco. The imminent completion of an Atomic Bomb, along with other unit and infrastructure developments, provides critical strategic options despite potential threats.
            
            **Defending Strategic Locations**
            
            I am reassessing our defensive capabilities in light of increased enemy presence around Tenochtitlan. Despite a significant enemy concentration, our city defenses are strengthening, and a timely reinforcement from Najran and the imminent completion of an Atomic Bomb offer potential strategic counter-measures to repel the Moroccan and American forces.
            
            **Securing Victory's Prerequisites**
            
            I'm now focusing on the technologies needed for the Citizen Earth Protocol, realizing "Robotics" and "Future Tech" are crucial. My plan prioritizes "Alternative Energy" to unlock "Robotics," then "Future Tech," ensuring we can build the wonder and achieve our Cultural Victory before enemy threats escalate.
            
            **Confirming Tenet Levels**
            
            I'm re-examining our ideological tenets to clarify their tiers. It appears I was mistaken about "Tier 3" tenets existing as I initially assumed. My current focus is confirming if any of our existing Level 2 Order tenets, like "Communism" or "Dictatorship of the Proletariat," fulfill the victory condition's requirement.
            
            **Clarifying Tenet Tiers**
            
            I'm definitively confirming the tiered structure of our Order tenets within Vox Populi. My recent analysis reveals that "Communism" and "Dictatorship of the Proletariat" are indeed Level 2 tenets, and we have acquired enough of these to unlock the potential for Level 3 tenets. This clarifies my understanding of the victory conditions.
            
            **Confirming Tenet Levels**
            
            I'm verifying if "Dictatorship of the Proletariat," "Cultural Revolution," "Communism," or "Workers' Faculties" are considered Level 3 tenets in our current Vox Populi version, as older versions classified some of these as Tier 3. My priority is to understand how our existing policies and available options align with the victory condition's requirements.
            
            **Securing Ideological Advantage**
            
            I'm confirming "Great Leap Forward" is locked in as my next policy, securing a free technology. This is crucial as I evaluate our path to victory. The next step is to analyze the implications of this free tech on our research queue and wonder acquisition.
            
            **Revising Strategic Priorities**
            
            My current focus is a tactical re-evaluation, shifting emphasis to defense given the escalating global conflict and the presence of nuclear threats from Morocco. While "The Internet" is critical for our Cultural Victory, I must ensure our survival by prioritizing advancements like "Advanced Ballistics" for defensive capabilities.
            
            **Prioritizing Peace Initiatives**
            
            I'm reassessing our diplomatic approach. Realizing peace with potential adversaries like the Inca, America, and Morocco is paramount for securing our Cultural Victory, I'm now prioritizing diplomatic initiatives that foster positive relationships. This will not only grant open borders and increased tourism but also allow us to redirect our production from military units to crucial wonders like the Citizen Earth Protocol.
            
            **Assessing Peace Prospects**
            
            My current focus is identifying the most viable path to peace with potential adversaries. America and Morocco are currently hostile due to ideological differences and direct conflict, respectively. Ethiopia is also a factor, being a vassal of The Inca. I am now examining our relationships with each of them to determine who might be receptive to peace overtures, as this is crucial for securing our Cultural Victory and building the Citizen Earth Protocol.
            
            **Pursuing Peace Initiatives**
            
            I'm shifting focus to aggressive peace negotiations. Increasing our relationship scores with The Inca, America, and Morocco to +100 should incentivize staff to secure peace. This is critical to halt devastating wars, especially against Morocco and America, and to finally focus on securing the Citizen Earth Protocol for our Cultural Victory.
            
            **Adjusting Diplomatic Persona**
            
            My current focus is verifying our diplomatic persona in light of aggressive peace initiatives. It seems my persona is already heavily skewed towards friendliness and peace, with low WarBias and HostileBias. Therefore, no adjustments are needed to my persona; I will proceed with `set-relationship` commands to achieve the desired diplomatic standing.
            
            **Boosting Diplomatic Ties**
            
            I am actively working to mend diplomatic fences. My current strategy involves directly improving our relationships with The Inca, America, and Morocco to facilitate peace treaties. This diplomatic maneuver is crucial for halting ongoing conflicts and redirecting our efforts towards securing the Citizen Earth Protocol for our Cultural Victory.
            
            **Prioritizing Tourism Boost**
            
            I'm recalibrating our research queue. "The Internet" offers a substantial +50% tourism boost, which is vital for solidifying our Influential status with all civilizations and preventing them from surpassing our tourism output. This security outweighs the immediate path towards "Future Tech" or "Robotics."
            
            **Confirming Policy Selection**
            
            I'm verifying that "Great Leap Forward" is indeed slated as my next policy. Its ability to grant a free technology is critical, and I need to ensure it's correctly queued to leverage this advantage for our Cultural Victory.
            
            **Finalizing Policy Choice**
            
            I am confirming "Great Leap Forward" as my next policy to secure a free technology. This decision is solidified, and I will proceed with its selection to accelerate our progress towards the Cultural Victory, ensuring all necessary prerequisites are met before the end of this turn.
            
            **Adjusting Scientific Priorities**
            
            My immediate focus is on fine-tuning our strategy. I'm increasing our Science flavor to 70 to accelerate research towards crucial late-game technologies, especially for the Citizen Earth Protocol, while maintaining our core cultural victory focus.
            
            **Boosting Diplomatic Ties**
            
            My current focus is directly improving our relationships with The Inca, America, and Morocco to facilitate peace treaties. This diplomatic maneuver is crucial for halting ongoing conflicts and redirecting our efforts towards securing the Citizen Earth Protocol for our Cultural Victory.
            
            **Securing Final Technologies**
            
            My focus is now on securing the final technologies for the Citizen Earth Protocol. I've decided to prioritize "The Internet" for its immediate tourism boost, which will solidify our cultural victory. "Great Leap Forward" is confirmed as the next policy to grant a crucial free technology.
            
            **Leveraging Delegate Advantage**
            
            I'm analyzing how to maximize our influence in the World Congress, particularly concerning delegate counts. Dublin's alliance and quest provide a significant delegate advantage, which I will leverage. My immediate plan is to secure peace with The Inca, America, and Morocco, as this will allow us to protect Dublin and potentially complete its quest to liberate Antwerp.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: FM5AD7uSWfZkbwQx
          - toolName: set-relationship
          - input:
            - Public: 100
            - Private: 100
            - TargetID: 0
            - Rationale: The Inca is the most powerful civilization and the master of Ethiopia. We are only 2 turns away from achieving influential status with them, which will fulfill our cultural influence requirement for all civilizations. Establishing peace with them will secure our borders and allow us to focus entirely on the final research and production goals.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Xhnumoart2IPSllV
          - toolName: set-relationship
          - input:
            - Public: 100
            - Rationale: America is our immediate neighbor and is putting heavy pressure on Damascus. Establishing peace with them will stabilize our frontiers, protect our cities, and allow us to focus on peaceful victory conditions.
            - TargetID: 1
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: BSIHVvy1BgurTgKT
          - toolName: set-relationship
          - input:
            - Rationale: Morocco is our neighbor and recently nuked Calixtlahuaca. We must seek peace immediately to prevent further nuclear strikes and devastation to our cities as we prepare for the final stages of our cultural victory.
            - TargetID: 4
            - Private: 100
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: sNeKDZxCCaR8EuNq
          - toolName: set-research
          - input:
            - Rationale: The Internet is the ultimate cultural victory technology, providing a +50% Tourism boost to all cities. This will secure our influential status with all civilizations and pave the way to victory.
            - Technology: The Internet
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 5ZmvHouZ7s3w6YDl
          - toolName: set-policy
          - input:
            - Policy: Great Leap Forward
            - Rationale: Great Leap Forward is an Order Level 2 tenet that provides a free Technology. This will accelerate our progress toward the late-game technologies required for the Citizen Earth Protocol.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 67rxyPo3eoq53u2H
          - toolName: set-flavors
          - input:
            - Flavors:
              - Production: 100
              - Wonder: 100
              - Defense: 100
              - Culture: 100
              - Science: 70
              - Gold: 80
              - CityDefense: 100
            - Rationale: We are focusing on a Cultural Victory. We maintain our high emphasis on Culture, Wonder, Production, and Defense, while increasing our Science flavor to 70 to speed up our research to the end of the tech tree for the Citizen Earth Protocol.
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: FM5AD7uSWfZkbwQx
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
          - toolCallId: Xhnumoart2IPSllV
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: BSIHVvy1BgurTgKT
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: sNeKDZxCCaR8EuNq
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 5ZmvHouZ7s3w6YDl
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 67rxyPo3eoq53u2H
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.