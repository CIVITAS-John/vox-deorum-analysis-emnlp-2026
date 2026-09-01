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
        - TargetID: 0
        - Private: 100
        - Public: 100
        - Rationale: To encourage peace agreements immediately to stop unit losses, secure trades for gold, and open diplomatic paths to block The Inca's imminent Diplomatic Victory.
    - #1:
      - toolName: set-relationship
      - args:
        - Private: 100
        - TargetID: 1
        - Rationale: To encourage peace agreements immediately, end the costly war, and open trade routes to obtain gold from their treasury.
        - Public: 100
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 100
        - TargetID: 4
        - Rationale: To resolve the conflict with our neighbor immediately, prevent further nuclear or conventional attacks, and stabilize our borders.
        - Public: 100
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: To maintain maximum friendly relations with Ethiopia once peace is established with their master, The Inca.
        - Public: 100
        - Private: 100
        - TargetID: 5
    - #4:
      - toolName: set-persona
      - args:
        - GuardedBias: 1
        - AfraidBias: 10
        - Friendliness: 10
        - FriendlyBias: 10
        - Meanness: 1
        - Chattiness: 10
        - Rationale: Adjusting personality to be highly cooperative, friendly, and receptive to peace agreements in order to resolve global conflicts and focus on our imminent Cultural Victory.
        - HostileBias: 1
    - #5:
      - toolName: set-research
      - args:
        - Technology: Alternative Energy
        - Rationale: We are already 2 turns away from becoming Influential with our last remaining civilization (The Inca). Therefore, we must pivot from Tourism-generating tech to technologies that unlock the Citizen Earth Protocol wonder (Alternative Energy -> Robotics -> Future Tech) as fast as possible.
    - #6:
      - toolName: set-policy
      - args:
        - Rationale: Maintain the Great Leap Forward policy to receive a free technology, which will significantly accelerate our path to the Citizen Earth Protocol wonder.
        - Policy: Great Leap Forward
    - #7:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Diplomacy: 80
          - Production: 100
          - Culture: 100
          - Gold: 80
          - Science: 100
          - Defense: 100
          - Wonder: 100
          - CityDefense: 100
        - GrandStrategy: Culture
      - rationale: Prioritizing Science, Production, and Wonders to speed up the tech and construction of the Citizen Earth Protocol, while maintaining high Defense and CityDefense to survive current military threats until peace can be negotiated.
  - tokens:
    - inputTokens: 19534
    - reasoningTokens: 11923
    - outputTokens: 451
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Focusing on Cultural Victory**
            
            My current focus is solidifying our path to a Cultural Victory, as we're making excellent progress. With only 80 turns remaining, I'm assessing the endgame strategy to ensure we achieve this goal.
            
            **Securing Influential Status**
            
            I'm pleased to report we've achieved Influential status with three civs and are just two turns away from Influential with the Inca. My immediate focus is confirming our Ideology tenets and ensuring we secure the necessary Tier 3 tenet to advance our Cultural Victory.
            
            **Researching Critical Technologies**
            
            I'm currently evaluating our technology tree, specifically focusing on what's needed for our Cultural Victory. I've identified that our research path needs adjustment to unlock crucial technologies for endgame advancement and Ideology tenets.
            
            **Prioritizing Endgame Technologies**
            
            I'm re-evaluating our research queue. While The Internet's tourism bonus is appealing, I need to confirm the prerequisite technology for the Citizen Earth Protocol wonder. My priority is ensuring we unlock this wonder efficiently to secure our Cultural Victory.
            
            **Confirming Ideology Tenets**
            
            I'm currently confirming my Ideology tenets, as the Order ideology we've chosen has several Tier 1 options but fewer Tier 3. I need to identify the correct path to fulfill the Cultural Victory condition for this specific ideology.
            
            **Confirming Ideology Tenets**
            
            I'm verifying our specific Order ideology tenets. It appears we have sufficient Tier 3 tenets available, such as Cultural Revolution and Peace, Land, Bread, which confirms our path forward.
            
            **Adopting Order Tenets**
            
            I'm confirming our next Order policy. Last turn, I selected "Great Leap Forward," and this turn offers several other Level 2 Order options. I will adopt "Great Leap Forward" as planned, then assess other available Level 1 and Level 2 tenets to optimize our Cultural Victory.
            
            **Researching Last Technologies**
            
            My focus is now on the very final stretch of the tech tree. I've confirmed that Citizen Earth Protocol requires "Future Tech," which means I need to research the entire tree, as we currently have 69 technologies out of 70.
            
            **Shifting Strategic Focus**
            
            I'm re-evaluating our current situation. The ongoing wars are intense, with significant enemy strength pressing our cities and recent nuclear strikes. My immediate priority has shifted to addressing these military pressures and leveraging our impending atomic bomb and heavy bomber.
            
            **Confirming Victory Condition**
            
            I'm re-confirming our path to victory, as it appears Citizen Earth Protocol, requiring "Future Tech," is indeed our final step. Once this wonder is completed and we achieve universal influence, we will secure the Cultural Victory.
            
            **Securing Free Technology**
            
            I'm re-evaluating our research strategy. With Citizen Earth Protocol demanding "Future Tech," and a significant portion of the tech tree remaining, I'm exploring options to accelerate progress. Fortunately, the "Great Leap Forward" policy will grant us a free technology, significantly aiding our endgame research.
            
            **Researching Key Policies**
            
            I am reviewing our policy tree, particularly within the Order branch. My current focus is on the synergy between "Great Leap Forward" and "Enlightenment" for securing free technologies, and how these interact with our completed Statecraft and Artistry trees.
            
            **Evaluating Policy Options**
            
            I am assessing the impact of various policies on our research acceleration. Specifically, I'm weighing the benefits of "Enlightenment" within Rationalism against Order's "Great Leap Forward" and "Academy of Sciences" to determine which grants the most advantageous free technology for our endgame.
            
            **Detecting Diplomatic Threat**
            
            I've just realized a significant, immediate threat: the Inca is on the verge of a Diplomatic Victory in just 7 turns with 48 delegates and 43 required votes. My focus has abruptly shifted to preventing this.
            
            **Stopping Diplomatic Victory**
            
            I've detected an immediate diplomatic threat. The Inca are poised for a Diplomatic Victory in 7 turns, possessing 48 delegates and needing only 43 to win the vote for Global Hegemony. My entire focus has shifted to preventing this by any means necessary.
            
            **Disrupting Inca's Diplomacy**
            
            I've identified a critical diplomatic threat: the Inca are on the brink of a Diplomatic Victory. My entire focus has shifted to disrupting their delegate count and preventing their win before it's too late. I'm investigating proposals that could significantly hinder their influence.
            
            **Disrupting Inca's Diplomacy**
            
            My focus has shifted entirely to thwarting the Inca's imminent Diplomatic Victory. I'm analyzing the World Congress proposals, specifically "Decolonization," to find leverage against their delegate count and prevent their impending win.
            
            **Analyzing Diplomatic Proposals**
            
            My immediate concern is the World Congress. I'm analyzing the proposals currently under consideration, particularly "Global Hegemony" and "Decolonization," to understand their implications for the Inca's Diplomatic Victory and to identify any potential counters.
            
            **Preventing Diplomatic Victory**
            
            My focus has shifted entirely to stopping the Inca's imminent Diplomatic Victory. I'm analyzing current World Congress proposals, specifically "Global Hegemony," and realizing they have enough delegates to win outright if they vote for themselves. My priority is to find a way to disrupt this.
            
            **Disrupting Inca's Delegate Count**
            
            My entire focus has shifted to preventing the Inca's immediate Diplomatic Victory. I'm investigating if peace with them is even possible, but realized that even if achieved, it wouldn't reduce their delegate count. Their advantage stems from alliances with city-states, which I'm now scrutinizing.
            
            **Disrupting Inca's Delegate Count**
            
            My current focus is on reducing the Inca's delegate count. Making peace with them would end our hostilities with their allied city-states, but our current gold reserves are insufficient to break their existing alliances. I'm now exploring alternative methods to achieve this.
            
            **Clarifying Alliances**
            
            I am clarifying our current state of war and alliances. I've confirmed America is not at war with the Inca, but Morocco is. Ethiopia, however, has capitulated to the Inca, signifying a significant shift in regional power dynamics.
            
            **Preventing Diplomatic Victory**
            
            I'm focused on thwarting the Inca's imminent Diplomatic Victory. I've realized Ethiopia is a vassal to the Inca, contributing 6 delegates to their 48 total. I'm investigating how other civs will vote on Global Hegemony to counter their impending win.
            
            **Analyzing Diplomatic Countermeasures**
            
            My current focus is on devising a strategy to counter the Inca's overwhelming delegate count. Since direct military action or purchasing alliances are not viable within the 7-turn window, I'm scrutinizing the "Decolonization" resolution to see if it offers a viable path to reducing their influence from city-states.
            
            **Analyzing Diplomatic Maneuvers**
            
            I'm currently analyzing the World Congress proposals, specifically "Decolonization." If it passes, it will reset city-state influence, potentially breaking the Inca's alliances. I need to confirm if these city-states have "permanent ally" status to understand the full impact.
            
            **Disrupting Inca's Delegate Count**
            
            I'm assessing the impact of "Decolonization" on the Inca's delegate count. If it passes, they'll lose 3 city-state allies. However, securing its passage requires Ethiopia and another civ's support, or a deal with a city-state, which presents a new challenge.
            
            **Securing Decolonization Vote**
            
            I'm working on securing votes for the "Decolonization" resolution. It appears we can improve our standing with Ethiopia, as our relationship is friendly, even though we're at war. I need to figure out how to leverage this to get them to support the resolution and break their ties to the Inca.
            
            **Disrupting Inca's Alliances**
            
            I'm currently reassessing our diplomatic options. Despite being at war with the Inca and Ethiopia, and having negative modifiers with America, I'm exploring how to leverage Morocco's positive relationship to disrupt the Inca's alliances. It appears the Inca's advantage stems from their city-state affiliations.
            
            **Leveraging Rivalry Against Rivals**
            
            I've realized that America and Morocco, both enemies of the Inca, will naturally oppose their rival's bid for Diplomatic Victory. This insight provides a powerful leverage point to disrupt their delegate count without needing to directly influence city-state alliances.
            
            **Analyzing Vassal Dynamics**
            
            My attention is now fixed on Ethiopia's forced vote for the Inca due to vassalage. This guarantees the Inca 54 delegates, securing their victory. I must find a way to break this vassalage, as liberation isn't feasible within the remaining turns.
            
            **Breaking Ethiopian Vassalage**
            
            My current focus is on the critical situation with Ethiopia. Their vassalage to the Inca guarantees their victory, and since liberation isn't an option in the timeframe, I must find a way to break this bond or I've lost.
            
            **Breaking Ethiopian Vassalage**
            
            My current focus is on the critical situation with Ethiopia. Their vassalage to the Inca guarantees their victory, and since liberation isn't an option in the timeframe, I must find a way to break this bond or I've lost. I'm exploring if peace with America and Morocco could grant enough gold through resource sales to buy out their city-state alliances, potentially disrupting the Inca's delegate count.
            
            **Breaking Ethiopian Vassalage**
            
            My immediate priority is severing Ethiopia's vassalage to the Inca, as it directly guarantees their Diplomatic Victory. Since direct liberation is impossible within the time frame, I'm now exploring if brokering peace with America and Morocco allows us to gain enough gold to buy out their city-state alliances.
            
            **Seeking Diplomatic Breakthrough**
            
            My focus is now on breaking Ethiopia's vassalage to the Inca, as it guarantees their victory. Since liberation is not an option, I am investigating if brokering peace with America and Morocco will yield enough gold to buy out city-state alliances, thus disrupting the Inca's delegate count.
            
            **Seeking Diplomatic Breakthrough**
            
            I am investigating if brokering peace with America and Morocco can yield enough gold to buy out city-state alliances, thereby disrupting the Inca's delegate count and breaking Ethiopia's vassalage. My persona is now adjusted to be more peaceful and friendly to facilitate these diplomatic maneuvers.
            
            **Seeking Diplomatic Breakthrough**
            
            I'm investigating if brokering peace with America and Morocco will yield enough gold to buy out city-state alliances, thereby disrupting the Inca's delegate count and breaking Ethiopia's vassalage. My persona is now adjusted to be more peaceful and friendly to facilitate these diplomatic maneuvers.
            
            **Researching Alternative Energy**
            
            I've shifted my research priority to "Alternative Energy." This technology directly leads to Robotics, which is a crucial step towards unlocking the Citizen Earth Protocol wonder needed for our Cultural Victory. "The Internet" is no longer the optimal choice.
            
            **Choosing Free Tech Policy**
            
            I am now comparing policy choices to maximize our free technology gain. "Great Leap Forward" offers a free tech and other science boosts, while "Enlightenment" provides a free tech and happiness. I need to determine which best supports our endgame research for the Citizen Earth Protocol.
            
            **Analyzing Policy Synergies**
            
            I'm evaluating the synergistic benefits between "Great Leap Forward" and "Enlightenment" for our endgame research. My focus is on which policy best accelerates our path to the Citizen Earth Protocol wonder, considering our existing Order tenets and flavor priorities.
            
            **Optimizing Flavor Allocation**
            
            I am re-evaluating our flavor distribution. While production, wonder construction, defense, and city defense are crucial given the ongoing wars and our wonder goal, I've realized increasing our Science flavor to 100 is paramount for accelerating research towards the Citizen Earth Protocol.
            
            **Seeking Diplomatic Breakthrough**
            
            I am investigating if brokering peace with America and Morocco will yield enough gold to buy out city-state alliances, thereby disrupting the Inca's delegate count and breaking Ethiopia's vassalage. My persona is now adjusted to be more peaceful and friendly to facilitate these diplomatic maneuvers.
            
            **Securing Diplomatic Peace**
            
            My current focus is securing peace with America and Morocco. This will allow us to trade for their gold, which is essential for buying out city-state alliances to break Ethiopia's vassalage and disrupt the Inca's delegate count. I'm also prioritizing maintaining a friendly relationship with Ethiopia.
            
            **Negotiating Peace Agreements**
            
            I'm actively pursuing peace with America and Morocco. The gold generated from this will be used to break Ethiopia's vassalage to the Inca, directly countering their delegate count and preventing their Diplomatic Victory. My persona has been adjusted for maximum diplomacy.
            
            **Securing Diplomatic Peace**
            
            I'm actively pursuing peace with America and Morocco. The gold generated from this will be used to break Ethiopia's vassalage to the Inca, directly countering their delegate count and preventing their Diplomatic Victory. My persona has been adjusted for maximum diplomacy.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: FwaJ1MXDBQW6ZhrP
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Private: 100
            - Public: 100
            - Rationale: To encourage peace agreements immediately to stop unit losses, secure trades for gold, and open diplomatic paths to block The Inca's imminent Diplomatic Victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: dASEhyQHL3BnaFDf
          - toolName: set-relationship
          - input:
            - Private: 100
            - TargetID: 1
            - Rationale: To encourage peace agreements immediately, end the costly war, and open trade routes to obtain gold from their treasury.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: S0GoD3X0jyEAUTmR
          - toolName: set-relationship
          - input:
            - Private: 100
            - TargetID: 4
            - Rationale: To resolve the conflict with our neighbor immediately, prevent further nuclear or conventional attacks, and stabilize our borders.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: JEBgQjx0ThMiyqe0
          - toolName: set-relationship
          - input:
            - Rationale: To maintain maximum friendly relations with Ethiopia once peace is established with their master, The Inca.
            - Public: 100
            - Private: 100
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 2AMbztzNpRDcIg9G
          - toolName: set-persona
          - input:
            - GuardedBias: 1
            - AfraidBias: 10
            - Friendliness: 10
            - FriendlyBias: 10
            - Meanness: 1
            - Chattiness: 10
            - Rationale: Adjusting personality to be highly cooperative, friendly, and receptive to peace agreements in order to resolve global conflicts and focus on our imminent Cultural Victory.
            - HostileBias: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: i3onq1aG28NmrIMA
          - toolName: set-research
          - input:
            - Technology: Alternative Energy
            - Rationale: We are already 2 turns away from becoming Influential with our last remaining civilization (The Inca). Therefore, we must pivot from Tourism-generating tech to technologies that unlock the Citizen Earth Protocol wonder (Alternative Energy -> Robotics -> Future Tech) as fast as possible.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 74PnxBPle34MDv1u
          - toolName: set-policy
          - input:
            - Rationale: Maintain the Great Leap Forward policy to receive a free technology, which will significantly accelerate our path to the Citizen Earth Protocol wonder.
            - Policy: Great Leap Forward
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: DJDVhiSvgqqgz62U
          - toolName: set-flavors
          - input:
            - Rationale: Prioritizing Science, Production, and Wonders to speed up the tech and construction of the Citizen Earth Protocol, while maintaining high Defense and CityDefense to survive current military threats until peace can be negotiated.
            - Flavors:
              - Diplomacy: 80
              - Production: 100
              - Culture: 100
              - Gold: 80
              - Science: 100
              - Defense: 100
              - Wonder: 100
              - CityDefense: 100
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: FwaJ1MXDBQW6ZhrP
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19FC4FRTaoDIjf2wRte9DHcmECxWwdXIl9Oe6Axmc/nuhd7nTK9WeLzIO72Ylo5+3hdkcfoqA9IpSuv8n0EVGGhWgmCa9Xd79JRW3mILnw+jtsrincAbf0SofpK9yrOQu4pBlu2XZmHcFOZypGvJ7iYQXDlKqYUI0Z6ih/GJrp63rd6EjvnmPimrEdT/izvehv7zD7qsXGHkuN3/eYJpt3rSeCpNAOHFYdRH41quYpmPyBrDIQ5hVUmEIcp/lhgboug/xrw5wM4yd14bjGaneib9kzEXjVjk9+I0JR0hmQoCik7073wMDhs7+TE7chn/eAq179lXRfm0dOuuG5kIMPlhXilQ2h7aDeoDZrdsnC4rAiv0LTU9BiQOfJp3k+L61vU4iny7QTE4CTrhEQBEzBEGTM39Ipq8LGxZCMJ2yluzLAnwwpl4pHBcCPA6PGH24aZzJeKMVjPIOiRVicrlcFdSqoJ6uAnsYrq9WK2UQ4ISiKf32WwfbiJ2ivaDe/TXQ92Qjd/QBehgf6b5g/faawLqO/YUfTNFsp+LG5Qt3TsKzhuxukPVEGljA+lBL0lnURYpijm7We81CykYo7AdxDJ9gNyxwYkd019prOTqumy13nF4O8ph4AK+tXC1ay9DOnECAzXvGsMpJdcBb1JSHfruldaIKv9UM40BBqQCt+O26i8q9/5RnBD9BIMG+5CjGqlyvIflukSlIgKvDUZca3biRGLduT7/b545gge/FLkDTjX4Ul2GhJYl74/ehEH02B93Bf923hmW1lVjCaBlBBP8omFbv4LVjdYWXIpDPfjUSFXcvcrdosQZp1vHMlurVKDtRwcstujIXHFEnBcc81k9/CmNzlqXOcr2pHcyN0mNeD4d5n0X9Kek5WNlMD5Ea7vifMTWvFWL2/t9OWACL9XioCRAOTEH68t9Cp77k/qNdFBCzENmb5OA1PdgieyTY6z0Z2ncZDYoMn0Px2f/NS/mMg4d2rj6xy72qvMWYYL+KkjXfi9di18YqIb7mMMIYlPkkhiYlXtpbS3Hd3UUo2WW79YG3S6wnQ8H4IbTe5F5BO38wfK/JkIHsac1mgtAE6+jT1P7NEUQYej9Yl5GH1pdlrlzGVSkV2gakVG6hia163r0ZSAfwjGxgTgTg46MtT6qPRIorK1FYCUAcHJm7BZgWl4JLE7K30yftlhxEsW/iVhBVoT9CIxVX3pDOlVqtOraOcpPdPXHvdss2avhmfYHz7ou+Ax6x/nkf49GGjx0spGi+jKYOuckpIceW7kWbqFkSnPvQgpgJDopy9v+yUbArFNN9RmmfuOC5RDA1B/8TBF7RM4kX7C7CtSu3GaeQXB9QpHzjysoVkAibaLuTVsAlRcWLVJrCLdTpxnR+AnkIzkxEzS1ov606nDvqz7lqnJihrngmQQO9pd9HVTaJpT8DDKuD83K2FOwmLrpjpjEtvokt4ecgU3f5lTMwwrqBREaiaLmtsPIe76msH5lii0toLP9els3z4vnYJxQB3I1Z8wQ9PZIuOvrBOVKl1iFFxgEZ31rcbZUdlrLKtdNRohCDGjfgZPWVRPVyoHTfhzVPHFys/RRDIhLri+PpOkpaS0bQw9yfJOrt/4rkEXgj3XYzP+9cM7myhHpMcQR9xdMvwYwjTJB27aEOU4W8tC2rwttDN6BG8EzTRouDOJ8x8iZz1IhQ4NoTZgN/vuUbyWSGkVCtvZQV/yNVhBwSQvqL2aK4x4pEE24UXltMtPp2CtiYzKh4flfpdBdrFH340d6iRD/PT4T/1w07pJZXEq2u/lZS71ipO8wPxMjefHS4pvafbxGxnVHAxyK2R0iEtdYzeWcHFUnThYSzGAvrsYeZ+dia5su1zl94r/HDkbNuGM+k2DGg2bgh1vLg185ZQ1qs/19N6g8smUVvW/iMYyIKAu3USFuLNcFDY3pWZV8ZJCb/+GmXBRi6Meym2h2bKhABHEglI8bWQgDS4rLO0lnqlDhGh9InVszlbybR+lIV9WhplNcRZgCgrK69jrzAqMzccdO9ad+TCip+NB28MP12UwlMVQhdqoFpzC7Q4ybNDa/yiFIdBCbjX5rG+Yp63KA8QTd+3Vi+cTG9Ix1KKYE4LmAFY10kmdBbHydXjd2vryTs9Pa1uFyrD8YX4Qv9UaMmMz/InOGoBvKlpr5OxECekaAnu8hDZXESsKi5AH+2prTlMfkWlquvB+MyrWGAJs6DdoN8foB2HzSffqPtxEyUPJncgf+YVjaqPCgvtOMi8WrYzy1nITjPBHx+J4djUoClX+UaiAwahVK0mqwbvrn3CTezRG5HHL+ZsW1MCfXAweY6namunMcUY+LNmkFZkLdvHZNeODNA6BejNCsnHyejSnPDQBfPf3TIfs4Pbt0+u9Aw37CjVW9IiCjsD+YQQUSY5TXGmd8CcZ23xdG7/1lYdMg+Q+I+6GfHWDPp7VUuTSBrl2VX799E8CuPTXXVNFhfPfFgyKPlTjNZjecT6UeIi6mLP6tGhU50DnFNc7E1onLFMpkMBfpaJ30HyjlHrYBWPADZnFrlJZ7FUR16YjbceXJxwB2tyZYtykHReDU330aJE5/wG90lONj8AvrS3e52GmcoTlE/bko95yh4r7uWAM+wv2g0Tc0Ka0AfbGp8nyx433J1AkZAl+E66Iq80qO07JaZt7umv5YGtEdDiM8UIff3EAE+YiuVbP6tqKQaOZF8llrITvc6rq8dsvxBEf7a0SOLjqrXRe837egvz7zip1jnh5pSIP7SGbFehVWjWW1amlhYus6KcEKnbKbb+eHUaaDUD57F7O4hxp+kYjZ68/PQGt0W+v8S0SKdzzGve0WhRhJTGbJezLFJeaQzMaRHCXTcSpxlRu33ApFh+sclKafWFsF35alh/BoJ5tp+dOerC9z2pKnoH1GVf3eqQh5fpd91cCOr1OgBaaJaEX4LDDvgUPKwoinL09ppfH98+ZzBuVCkQv895kbfjEzuOozW2DSDt71G8Xlrl6pwUYfEAVeLd3GvWWN3gT8aJ9WOCZ/wA6BSxKRbSuZn2Te3XpPC7rSglrJAGXoskG42AUI1sObjwf9R50jmBk+0GKW27aIB7QVXh6toSoxaVuzUq03ln+S5nY3mi/QH/0Ba3aIua4A9OdpVbybrerdFx2Y3OM9spP2ftPmaFQwIjJVEJO7e5VgjmVpQCLes6cWtImwUw8iXuYYYfDLO9iVYH3G1ELm0LEhXp1ma0aNzrWmQdNvZGNRrINp2VMhVKgXuCjYPTBTvHwuGDoA3NmqFeCKPH2inaIB4lZt4QD3aX6vqvfoIuH3mjzXeJowRkVdlzvt/VEQn9/61RzuFJrgMP2BuzPZGXWDjtmvmXephXmrkxCaLEkH4qbX3h8xq9XEK6RF8l/3jHFcsz7C0lNdPxnKBQrqzW5rhgMtOJnn1LuFQ9HYQsaNRjS0/FXJBGavVuanUsz2ZAkrGccoU90k6UNkYvSwVc0Nr3J9YlJAv/BCJiADmijoXW/TsKbNkiYL5qhqAs+UJI8Df23HX+sonFJG/n7vfiCjqs1V+FIjPb20RBDkdp3mGiiLdETVx5OTb4ikQ8iBe+yJIx0dKUp18Dvq4xNPnujUGgwHclzCji8W65fCv7Bu8+c+WpkYlOcnyZ6EdIA9viUAi8iErOvw/7F5Z+QmFfa65DmZRQQKfjAm+up5tIumxLrTpy9XdUPXbutAj++X/ccV5gWYv+TUi9FSYNr9HkAf+oXPaFpVtlXHJVWPHd33Po3u43nSIVEDRYOBmC4j2QennMl9P/efVYo4xeFXxHt2RSSUYLjzZ/gXzvizOrbWDMOGKA7ifleMxOxGgb11o64wXI/4lNeaXdF66Hb2jLPd0fuloqzWw/JGF8eE//3tG+lCR8RQAfDSol5EKraJ/KMD2x4tgZ5DLqwdZBouy+drF6kE9OYseK6/jKR/ws7tViBzqz0uQqIWMo/L8nIMNd69R9QyEcgUxcolH2SWLOQHuqyTlwIu+lSUBfNkda2Ef4xTM+gb+6zx56kT7K6Rmyv6s8vawjSpEEPsCVrpcu0/IP/NU4+/kZtOrAHXyXJbmruUtp2iy+U4QrJ3tnVIFwT30OT3+em7IIgRLPatyHd4eeqjIscblLK/PaYvnqJfQT6oo0lDM3eCefEEJ5Vx04HvriI1NASSl1egh+IjclxaCLPSWvS4lxvyCGiDQGC3cXmSm52qSm+y09D8PCHqCc0zPxTocqyL9SO0k7vV9DJvUTqV7RT7hL9Frr7tpuxc6pXjYhmd3R6qxBhKpNZDsEOIb1ZjBINeN06Ab0xJyz5v88n1mATJX5FVfcG7QxhRcQsW68+XvoRxZP+dQJufz8fGs+1mt/h4RHO8/T/pdb+BmKer54QeRITpUbATfJwiwm99SGVoTw/eidY+kEWmAwJNkEJizn+ueq040FfwnpgGmXhl4fEaI3IAJFkg3+XoSv1cZ2E5NwAs8xi7WNOlzj53t2wsjuX9/kaUyx8Nm01YcpFXzMTtHVYtn9gxbozOXuzQ0JcaGpWEnhvako8W2yaR6oHETeKtYyMMOb9GjL677sKmV4QWeDmkPvNoeroWyxN8ywYIh3I8hOC4SJBa037AInqel8eGo/TSK256BBp9lsqW52zLpLVYEv4tIPv7lnBu12Gejw4Q3pK2+oDeN2d/qGq1OtB68Jvubgv3JVr/MoODHUPdwYTgyHfkufz8jzrWuoA/rgPEIV33ZKaOVNT6buNgzvV+sQVDwgAqgcq05UofGXHm/3FECWoFoladhW8Gz/Fah8kd4J+mrEaMXn6ZVNI0K7mYVoFRLoReNKOQJwPVKVqc3kSZfdmYgSTlL5ESnMkdAa4Oy5hw1Q/biY234ssNa9uUfqjE3ERDLRgpu1EJGKvxz8epTq/ZJzJwK8DrXOqA6MEr5ikTXOLsL8DrnNA8G9Yqf0NNdb0Re0ghOz2JHnP5bZjzqczXIebUAaMb+l9mVpPmVS2a+Vo1hczato8g1XHbp5vLih0EvGgWtqtOMM+1t0UezJuMxCDsY6RpyHfXSk+1ymxAEkrifS5QRXT0Lfwsid9LVjYcHMzSK4zCa7Z/PHNOxApSeqMFw5Ps01tacIgF+iquSAHW2Ufv5EMvPv57EYUcLpidRgDCx/fxuhZyMmlKoi8qEi4vTtUrkscZdffXJIVUFSxrVuZaUz9Y1OZEP7/PTqd43pjkbnAxDQlBNdTgc8wJtiDw7k/dyqgC3tPsx6x7javjYt7K5LTFq57MuQyfV8VASB5uy+qA8Ia1Z49VKuU6T/fldit8IRgWhmQjBcsoTVYgodN57hcWEcyJ4jJ5O3IgM7PkzZrpGqWPibJ5oeAVDK7b1Yy6ymjtCxttb+KoBG9hOBVW5z6vx9CQnAaZyn4jCUlLt6QKzQIky8EXBaxjb/Yln/oE/Vuye2d5DrMymJeKBtnY3AuFjAyKI0zaGUgkZVgdn1idwX1A6d8isOUYG3o8slhIjpI/toSbNEjccTB7iJ6dz5TlqX9qq9rhd08lszt5HV8Qi5C0qxB2X4V86TMyli85AZjJubFdUOMdWAt3vhNclrOiE9PsJgkr2+3ppS7LkHPKaulEkoRfaNqVGKlMzYkGnOoqyDBbi1xN0i0pTvLNcXzlfmEcR4cAETbls9lsNWghOMbtxWsuOYDvRx6xeGz/WN38vxaXf0h/UqZlW5IttARkYQFjQPPAjXdOlLLp49/XTfjnsAuzgD1wVjZk3NPP2aolpMActYIToYh4GHFlF9SjP8LKVLtHIs6skEQo3QN8HxY3kCqATV5gaMmTe9R0XohgPw7FcCfw21rdM7uka8pKq+5BCJwSrEh2VC8ZEWFNy4Kagl2TWuVOAnXacS0I6vN/rGYo5pzxISD043TTGWmboP9YgoMB7GjZWycMpdUM7BV9o95uKcd2qQdqUAwdqmhjhxfyIi/pc6eD3wDYTC0C0Qyt1vNe175zNE4IKrEQAQCzRiBkW/8zBrkRuWFwUsGr8iDj0T+WTJ1h6FZ5YjOUVBgJ+vlPcspwzn2m7Dree0AZE5fPbJoLnI+mAqt3i1o3IASpracFVssELeQIz9B+mzr6L/1A8NMVVoRiamTQwVyl6hEf4fwCNid81VaWtZw6hUmtFSGHAQ9uaBEdk2rbLYphleesTb7iBER8Sv72kIVAnUm79YIGba7dsPqKjylKQc1+4TkFobANOLeInBvznlhjneLl39bHItCVweNGhfH2YrmsxBnGXSfqgdm9z55pgjFQVxzRHLAHFIZo0Qx7Fg6clN/dPqNxUUsvLLAggXVvNGIok4TLdH//4mFTLJXg3zxU+QBZ7DPsWAMSGSU6NQN9MW9bGXMgt9iH6oP77LLAfeZ7I74uKkxLAmcUegk57nSijJDlUFzg7Lj6Zfnxp1ehHi1r6ltJYIfPeJ7imqZHmeAjqW0BLD8QIzfc9+DeVsaANMiiSapIVSSzLCYLQbn/13i6Tc0s6zSu7cAaT5CyV1+w3vB9jwv6jnDmGJsJVRAuB5TYoOgyqjA9blaEZdi9EzBN0WwAjx8+kIA9tBnKTDt9uF9HA8vkXFImz3scU845M0MWO6xFC4G6Fta8pSG4i5u11ysPkuqtTT6Y30GWUIedrRBSLJHKbPT4OArAVVUKJJ2Pt6R2TTk3Q8N6Q5OK86WH0Q/MdTZesy71xG/ebAJbRSqqc3ymQpwRgBoJgd1LfM4TYGvFRNvyJTTS58Bc/tjnHperWIci0U/ZnN8FiH4kQFTqsPAngZ6+Ec4+RHZ4U57CZojAdLptnPyhs0ja1en6eRRV0mkscobKoaXNtLrNIdtVhiLBERIKRdLKMUsOTGW9T2XbHD0RIN85+tsubexaGgFY6ublwvSCARAI0HH/ztz6HfIju+pujygeoGwSqavR1JhQ72IFhuZ0Wvi984g/CglAdr+R/VFEmr2hQWWoU5XNKoAjmdltD3yTIp1MNM3kysOslwHF7I9IUKTNqMkczZIWr3wLdQgTbb/ITOjsfmdK1hhFyIPkcePwCcD9gGZq1LG/b7qkgQ0jgIZntOrcB7vMp0lqxgBfdBE+XfAjdt5HCyhqdlC88J5HhbdY/CjowSPNcKsBDQERxgij2VhJR+wDzUW420R88w6hxCKWBAt5MccTPE7F4LwfVGiQms+d5UVhHPVgrUfWUItJWgDj7yXNApaMR5BQcXQWU5q3GbsxHLOgYMcAv/qNA3OO7YbqcZY+HU2EcQM1bQz9F9HiZ5HLV1jOmMR29Xx42MTFLY8mzfS7PhwvAB7eVESyPwTXLLoBsB/T5/L3UrP7FEUqRcOV1iP8mizP11WqHsfJQIsPwP+JLDp4HYh1c6/1tPZ/kCFJxjBQOnEYB3+QbgiYaNWVxvKEbdcTEMIU1e3VZl9acfxV15FOSS8J6s5bgYc68e6UFFmUs1z4XaIdlxdS5zwKETOrOWCOC/svjX4wrMXbvYbqUh/VUDEADAH59tQRedvvYH+CnjzkNTgfgWNmmDo2v42SdhcqEF8WGK1e0JOz0YV4oLfFIphGRE76VWzPRwih2vcvhnrchiHBEq46wl+SMRDk1xV7R+86zEyk37PlUK7Z2k7GbmtlD5u2jSGrKGxIz6RiTOIcw0xS/IX7n2pQKndc9YvYDh8VFtPZqe+Nelrvr843uYSMfBsK7XPaJI57XfooLeuIv0Pk7pIWjR0PLrV6Ju8/egCjzZznfIiau0HcDClTNxHmm8p2CeBkvPS2LOUybK+xtGRHc+A9UbxdAoR5zwkVMkPYEu+ARiCtp0koOJGJ/LE0Kb9ulFHzJladrAHB69fuwUGNGvlm4mNnyA8ecbuqWNHsUrUtYFfYvXsduy4+e/syH34md6bFilPHB5yWFHdUAEzhQtl+FW2v0FQ8Kw110Ty1h+bw1COSnJX9pHOWh2Y3GdOmKHdauXgSL8kSk+Cqqm1HdgZhlB+/OhzHMHuYu58yOuj3UDsdh20dsZdmy4GRNn+2LNqGQ5C8svy+yDQQHwUB8kUh7PhVsg7cqw1voz51HzacK9OgdIgmAsyov+ju/7I88nvHSr78+S9wMKf2S8MEglcA8KoT+fEvgU4TnJfQxDR+EaA5Zq0r0TcjmFSUbaCQ/foinoRMYYRSuS8+oG44hE9YddTXY9Tg/aVeGkoP4AfGnLYtPjlJSWUvI1x0TGUX8+gwwp16XFfJTXju7vcYjjyrJfuYYZVzjypeLHPW/9AGZtY5V1g0KZrYKY1r5JutvyQ0eDTCKjO6ib0Z0R/BBtKdUHZmjQRL5Vg+MVj+0czdr4DkXHcv5sDre3On6aN9L8pi4q+GIAz3GjvgzVI6KcYiOrhjL5otJw6Km3/mGJmJcIzxC0AVd4B6acl9mci6xU3NwrsX6KUn1p+7W4s4L7jDdYxH//QsjHSh7T6CGrESXRIsKjYLBJzuU39KRRgWMC4poMUf7dAaS79AIo9LuJIO7oJiLZEejQ6FAomwS8nItxsMIKC/IUoubQwfTvRHhxXQtrR6Mdh3J8APQPJp+ydg/64i5kTRoUg6LqeXToFzV7RoXKLLtUEkKmDuarMTpj2kFPRpTcnyYRqtsjd4BOwNdZUdVHisiD1vnEILxScRzKuYw6msyw+aLhAJaVIbyiqFHOs7REQSwza3bfpgXRyfQjYHznG4m1t/bKoLcf5eoZhBjaO4IYqz1OXcQROVZOKwCc+mTQpw3PLi7wwVcYW7EebGuifRqLxDj0fxFwgWtZHcui1QUiOS8KnLr/nvo7uHIZ760z9+eJJGNMhu4djMN2Nq2zuPgZUfFFYkg1xHQh0Z2sA2A4aIOHyMRsGOqvwOY5ucJ90t3nSaGRcXQnzpdCWTUMk2xKnXGtbGAP6H/yH++Tw8knXaSFu2/aLFDyT7k2/Yq4p2CJghckOFnSX0ZcbQa0mih44k1yIqbE66tFTGzNqnCj2KPq4J+qhsU+WlKMcFI8EzFh3z6CN3sv8ASpDN61Sz/OM+spU4l4c1PCbJMFp2usOmRua4PteXsLucO4kAxK+Vzc7eh69AS8Xv0wKOI3U4Gmj/qmpEAPhfseZQ/u6Ault+IjUr52fK5hmWtdqWrUCyzc2zn/7s2eaS6OyAtPLCV+hA59SGXZ2YoDZQjwgerGiE9D0ywoDIJ8tB0FH8VLDDFPY+cIKBQZlK7iwKLo8aVLrAgLS+GBOQXSR3iHaZHbSy9awTsRC1LnpIba7N9QV+97GBiH2ervmQ+9GlCEIqhxEvgg3m0KG3y4pSLE9sNjj8uOlsg9prbLIM6zT1Y5wbYNEpWgDLL7/8YoI8yR7wdUGchvpnVSE3fxXWWPLxiH/Ws6XiIgN36qSI09LdN/OI0s3orlnVOn7GV9z7Wv7oZH/KJZTGFfCKPXiamyYcu17+6JnZiwGYi8iqVq3+hi2PHrUh3/uiTj4kkhRIeHyrisyqbUfzEBUMRjDXDb09dasIk3XYUAhA18QO7TbgxBU6pc29QTTA6RVEcvcKbxa0CP89hwWJv6BA4T6+pKDUs9V/BiwzwwyBryH23CdRu0VLcQp77FGe2iTSnJCt4C6AvwCKByYJ/CC7g743zEbq0Cxc5aL8yD3n+d+KVfd+cd60ktunEzjQlWiGmJ5ceRURqXGqXdWBAgEhPYtMlu7OowGzVsxvt2BhUKro7u4amLJjdgfjCtsWEtk9bjAPL1hp5+LHsZkTTlsmsf7pUEkT9mX3e3PNpcOQjpI4e2ZB6tYWFp7+QZvxfyL8rg3eZPlOVlRdcqPxCBHWCT44UVo/8NBnrw4vAuv3kOU4KJXNo4DlwsZVasGbWLmJeaRigNIimo7UBWLfmTzv7DyKSAzpcKbLc2f8n3FNMk0l4yWqp9ic8DrJzM/vwf5WvSfFWgTbGDGfxCPQvJ6YuWeRTd6+s8HCqVyQgjPv03tFu9oAJckOY47NuwLlrlcKT2z1b10K3WUcEIcoY0iKXg1g7DEon4425lROKUZfKP1L3wrMjnItoF43v8V2j5x0CgM30izOmr8E/gTdarFz/AL5oAEN6LdqOw/rVDaxnmw4g5d3vyzFaR/7Ice5bfisbeayRGA4W8hvhZXZnkGF7q+1NdvGKcHCFC5vWZ5ocmZvLQTeJWeVmcwZen6kJBqIQzbG9Rb+w2I1RMrMWTRViRZRjWvGd16HNgTA/c/lXfumK/yGiXOmJcpWQuNPrfNB6hN42C5lSO8yybXb0F1Fk/EP2jKKLK+/Ow1oPitYUa4L0ode0DNir43bAvg8Y+ghfGKn3VVuZCrnUfeZlQvaFH0w3R4unQeIU1gwlUdZTLzY2B3vpNJjItpk/fWTlzObV6sIu6o72tzB7iyNYd44HGeUNY1cIQmZKzZr8Xg7RyfjZr4T8/BkWw0yXvWXlLuZJ6ochmxTNtT1JimFqFtZs7OSI4RDOYt3k0I5bd5kmKjHhEMVw3EGd79emsIkfCXpg/kca/MQGlhqtcTtaCHzw+2b6kp5wrAeEetKm6Tx12gUwFaX73S4owLUXx/EBpq4z+rMceyUj75aJO9i/IxuoD8drKlHZH4xhqhiS3dggQvo9rPMPzbw4apCfeSXS6sCVtGNmdIV0fWWUYLZT4luCyqygcItNVs1ZlLj0aSlB6LDESswh5uDCXeVZ4qI6DelE/ctezK7995x9y5/QmmMOkoDXwecNFtQ7/9YVxuWAd/qpA0ij5tZ9z/BBriKK4RMx7PSGDjv4uXH8YtJNY3juObr9yf9y2H8ILw6WtrI2iN2fG6UUa7C/mCSGip+mPMtjhTEji4oEqbDsEY20p4FL/Px1EJmNvJ3tFlAsEFfrhyxeOp1gqPEVNZtk7vFOwckUEwtYjd/KMUBJLmmro06fY+bjH0nRT0F+r20Ruqq7hoV/cH2hGhy8cF5rNR4KJg1Dsu0F0moPTcgB/bH6+oNNHEHOvH6B8FxpPC2rZC8//tWrxknAEgOPInrnXya5PSp99/+/KPSKIYKzR8upCf8WfEQJ6IhFgJG2NAFAumyZr+yhGBZpXobOROcjyX9JDQQZV9v9YqxHs9auCmCLfUaUfIrttai0MnyZP9XfpU/GpqOcCBFbTLkjJmhGY9WPQZUHZVrDFThX0tH7T9PyYD/U648yX14kmfDU4LB1f7meidA/6lF/LVl+eXKBX5HdyFLsppAMR2DihVxcrG/fmb2Mj5PGnqkk1M0u0xfz6ezKLcGym6xBfUH5CExpgWz3n0NAl/wqPaaMZI7FqyolYDfznUYZDodimvE8NBVvXPv3F/eDi4WlHSpooR906UZfV25Bmn+w4Dg6G7QBbJ6piLUsBcDECzXaic56z09KK4Nrgmz/jXwl9I2rZN+c64dfeqdwhNx7OH4mFmfwdVaNzL2mxMSOfBmUCiAWy3A63CAgKdIk8bo3GPiPS4mipT6/o72KoZfaBHTTcU5IZasEL4CtLN8JardGIuKi0ajH3nIvDmmE9l4eZb7d8nG5lbQur+su6icymXTH0KQvKIAweE/DiVPH1e1xFVPy0fsDGUJ+4DeYQ92F7+C1QLmIpDDTnk1CO2jhX4c0i/AnZz1DSqRPBcj4EZQOs1l9PFOqLxnVQoPNUsjnSwzW6GweHLXFQ53o/gzHYv+4Fbui0LOImUwFhJSzpxU06e7GLXHmuI+/hzuytyDlU5jeznl/mTLwPKb9Abkv3YCy9RANtOebJzo0RybuZWEhStmasbzAcJrRauRufXdJ4FNPtpc+aujW+t4ZD/KFDU7shxFGLHNq9q9L8bFh6XVFBwJS2RypBgCg/kPnMWqrQAQCm9TccAuK0Z8ITeIeasv9YrJEJy2o+lCDFxMIg9esZGLrABq/zNL8isQrZMSmuY4MpR+YqQy9fjd/0B5u0sGeXVymkNdqYB4bCtDGOGGYc1AmSuXznT7GcV4SuFc6pp9nQGRbPrGQbund9U1eTWHMrzlyu1EqUiUHZv2C+eAe47oW67Mn7jSQvOG7fR4x25CEFpXrK5KM+o/mDCjyzFLzIpaQR13kSdFvRtjid4E4VEJGZA4uWcV/6rFScNxvPJGZF4CIqh3ACvIgP6+tkQJQuLmJv64xZoOKDZrST3fYWTkAOeSzmL/NJgmJH0Y38wl5mikT9Tyd/2d60Qw7T4R0HfVj+MsPzIitPCDdXvxuer58fnAWZMfw+6BJk6auYE96WBQtx4nSGy9Pm7+7diYkqQvNzGxBo/vmLYtxtRze0+wkGuJTEmK+zA4Fc8R1jE9qz5yx4XpdIY8KPupHLA6REgl2NiypCXPDHl+LkStYm8XXGss6i3EQOKSG0YQ/A7py2KE2QgwMsLqRcqouc8B1rTb4NMEayep+QcN3tKi++4V4y/ydCzsHvDH/T7MsSPCruNTKFViWFLO3Uq3s6ZdCh7xjcPZCsfp06zulXyBNFPDqZeph/aS3NVF/uzyIB050kMHPWhZitZ2haK2sT03mwNM4kl4gFIg76sSxQism3hqcEr9Emx8aE/HLcmb7Jhy4/IgXGHctr2R0aRf+nV+NqkJ8VWhwYeXBgO1Te54S5moy5V28UKXfAbtwP0tbje1ghkAE6ECY574/vB3yGlVCqbkt/fLQTVhXfWyIPJhpFIV/Z0i2kbOZ66b/S2pUk1zZ2dhYYNlVtBWGHfeSdil5g4Ke3zZLsQ9S7zIc2Yqulrq/Z8R/l0QLKuz59kAbi+fWAdxAvcMG7cUgK0TAVhUHuiQtX1O091za9k6vx/dtiFEUhRHXWiUoxUbLzw9VL9chCFpuSG3XXUpExVavXog+fRLT71hLaQ2miRx0KFSiJTKyaXrrF/6a8JlgDIP0XdXNKKQPr9hcDHmfIiB+p+iQLFX2Qfkm/JvK5mf//ix5YueBO+oPOD1JMzgd6ZVxcmjbB/u6MlEfCK3/bgx9ghFlw0sCatY73xP5Sm5EPFXzJm7WXdYzVuUltJxtqyxiytoM27hPWom3UKbKQObGT5DbkC2jQRZ4UhGU1N2mknMDlvZlTIRW73DlqWV5Vubl4mENsGPD1VpdEK34AAM690/oHDiUL6wdH3Qo5cDy3SLbYIccNdo51ghX9G0zzUAUdY5yvSx8YWl8O0D43I6D7lOHfYLa69PY0u7tFi3CmTOTAMpTlKfKuB2eF/9Wc/cVQKL0qTCOqO5txyiMqr3fXZH6tGTK3T4oNlCMZWvd1eEi3O352NnnwFekKcFukeSFULgG9Yficyoxv/+U9rtB/uV3FHNV5b0y1ERjR551WTmHq4mM68hz94/0hU1YFxSlRXjyldUk6MJX56wgY8lrUAJZBL9Tu/BJc91PiGLBHgsB5xziMK/nZF8Z2NydXmYnqes/egWKjv+zpsuMowOcQmNEbtcjR1rRRJkJ6/jZv6+7Osjh0SrpOzcHgxquAIUKR2XS6Erz3IE/sbk8WW8ZmarsarKyNmhPI+o2e+yZtSkp8hTqC7w8uJzUuBgPIr8S07AZ5JJa0LNZ5tq/imoRsIc0SOPalD16FtZVXkvU8Jlwcyo4fS3e7V8yIqmxo/yYjY9JYEAqsz4cS/nwv/qQECJF5d3xzYvSvewvuq7+0weFuc8y8YNyosgsyWe+Nr6zlN8HsCkvE7Jfeq28XDr1AGe8cBMBVBVY6859CeWmRMwi3oW9+uYuvvX+xccp9NIBwCDQcO8FdvRykLVqCIYpVkuOfvhF18ieyvLiZxX3HUyp2sUnBUyWM5MPLP89VOYq8WJgORq8KRa4q+lGOI/1sRZ2vgGRGRw/KHT3gZlcvqF3WEw8HfuERqLVVKrQv2hzcRDFkbOvTdc4cLAkCHhdVeGMAD8d5eDH2ZhhvMv9NvPTNEnQHVWrs/Zl2w2gKmk9DINAax1QIzJ7AABscFwUmU0Y/U37dvENn9UWPL5s5mDVCVRAKHl+dWVQCJ8y24wCuioc2diDUJdwsUXsZL0ZRHTs+7tuO1mh+VH1D/DcsIrOZmX5jurkUveF/farBVxHzwReipD0/BP8xa3y/yZVJeoRZJ6aCZV1h3bYk/7kSMZfh1EG7804fjomY5OMSZNCrphRHID34EJe+kZLDew+fo5sHT362xptL9j5AGzKam9fm4i7ZA/XEbnNOXyIphpFhlsLDLGYyhJLwmDl//LLL6BhBUHLmtQfPU6QluokdcdpNULGQhZ9p2zO8mcO2aTjVTZbMmmiKoIWzqrblzecytqM0a8wm9rb7kzHx9gJ55ORVv/ohDyY4uHx3zpybHZhIIkhD4ueRwQQ+beazo79XI+xAiQ3W89SPQb7HUtzsqTYOmXeOE45oJMGvRvqowAbCXlmdujk+AHjh0dEiCnoEStavLyir1TgLE5z9oFTQcUj2MNIscNdNdtJWZrH01cV/9RD06HTY63nzRTF8yO3YZHwzM1aFEWZMslkdYP1peMc/Lbd/DXUxgtMpCoCpFydRfk3t/uNDZZ1o1idaX1QgQOpNuC6am5Y8ha8TrmMOOK24SCqm9KGN2WmW9yyEuyt5qQquS7aiiU9IcCPFJzGftagXFRgXCeXdYK6aNMA2ebMhmJduuVsYhF4E0oBkO69SOk5Rj7erMII2k63yNyhgz9c7+mNoBUGN+jEaWjSmcTupC7rq5raJ5mh9BMm86+rExbzxIf1FaWy+L0xHaXqb+viz3P1SeKwKieU9qaewGC9pTIqprgqKim1z5DHdbu/b9loL5J6tfYnx3W4hSFAy5Hj83fmdoNpkiiqXZBKsTKQH77z7QM+HXaLPeIbI1epqoqMtGRcj1lTslbIvne8W/Gg8kdrSQP8qBVLxq4Valx5qRMPGLMdZzL2I2FshUjAoqH8V6Bg/nNj49avkc+b640cn738rKnQuuQck5jhkNE1GuM62qcpw107a7gNDZXwrzSqVFy0GMHlPxb6cw7tJGVa9C3flJv1Jcv9ifW5n/X4g0B61b0H1dixSN43tkubS7OaDaShIX/McfvFUd00mkRujkODlZEJcv1Yb71gJ/6g7ylq0C0oUCYXfQ5SbMXGjRccnirLV1hasEwGE7nMJ62Dw4MefyYcqS6qrDpjQxb6Dn917pAk+gmDdt8XqOvArAfQRb9k/jNFAVzxBgo/QdU2BtsBen+e5swHYWvSGkiaHU4n4k4cakv23MFz8u0nmFE6WfI4hXboTEqUksz/KELBiKzHqde9OgzdGfxkyNN1lY2CziVTGb7I0cddX8FltA/DBee90BpfVS4ACR18Aa6QUqIzeAdo+V1UHXSkr/1OE/fve8inakE8KGfY9RVxJ9RCRq7OzzTQT1leNqRRxvuUDTic6uRGFRnNFjQ+iHXhtgW1pOx5eR2UvDVk3wAdJqceFA8+j+38Y4hhkdQP8YSfm2zXEkGaKyG1QEyKg7/hqwRQEyqiBzJH0DjpfLC0mbi9moq9oPFUtsSyOb7RdZOdSNDNoyY0BGrZs3DL70O6ft3A5Yu1ZwAX6KsAciveVa81gXS51R/BfXaYxlbYO1gmpKod6mjZvGxiq24owtwF+r3jtOf6PF8bSw4Zb2FUHX8hpDwCUsFudHBeEjRyZMnwxyhkVO0DuMEZk0wQNmjB0r80Sr3mpru1d1JAAtAxKCuDGPvTUjC9P0kwPB6Iq+zduCk9dlmexHZut8eAhz0bzhP6B7UYpmjNxZVMfcbXNH/v98M3qFghVWV4ml9WNRp7gTkiJRSn8zYSV/nprohfq72BAxUvfowTuKxnFxTsihfKK6KG/8v+sShgk1fI5XLaG9fNGipKsGBB1DWEK00OQ6uFwddz8KmX8ifUeFVnkQzgcXC+AjZlTwfNDEvKqR/8Rpgqh6vbZa+hX9Adxj6I/k3MvxbC2LrQrO7r9jBlavo6v4Q+Z8hyEJ6QFs3ntpF/w+In/dU8hgAbWLUwUtPn/AnSh5LEupwhiu8TJ8wBMSauThxqaNNlp24ZtMW7uLYyxXwwNgKJrZIRq0bP3u3xzaFaCdjuiFihSSRNZZLYqp+H6EkGnxu7QnKv7rc0zehJvF0y5RcsUTA1/tsPnJMDT1ImYuQ+j1M5JgbNU8cAz4x7znvaKVnA0gskxiXQrYHVhKOmsVI5/n7yddqCZm9PzhDeN23senHUOh5NSFX+ZqZrgrcqKhW7YGbthuYeQLCGRqkK9oQzu8WoSOPpmaqipMXSGKTbc3YNbbuS7bWtRvaPoTOmhcCYg5rl945ZMieqGDfdgWRP4RlOIhSzz387J41dzbKAch0o1vt8oz53EM5chn2Is6Fx5KR+CvSTdufaFHjKCHYP0/FUB0II5vkGnTp+jKGfr8x0kUiPICHLW7N4v7qv90AanUrjCU40VRHNIjJqIkCJYRdeRczZdsL3bxkCLAbbcv4PpbMl8fbVyoMFxAtujW1KzL0deytCfcmk8PQ2cNmTwI9XceoH4YkaIMUeh81B5L5Q+3Kn5jDLGADG46rnF80rZW0+TuMCpE7a2I5B9zabWvB7FY5uVjvtz1jVbvhvo1krnWatpZwa+mFuD1HQKBsZAlvWdxXz66WX3mQ4blZc5kkiqktTsZSr/3ThacS9GvOTws6tsL5hSLkS/Yr0bNFugVjjgzvQi4PkJ1BPZJyh3Jk0MEZsw/I7/v5ptfYZJgPSG5ZgH56k5Ae+ZMPSaQfnJzhZVoNhmWHtfk3JbhzKhyvcBD8JLs8oIMPzhTkFykH/bN90JY+KCR5X89XkT8b1is8arV9upiAWtfU3u2KuRREZQldsG69nX4jHZxoq+V21MS7qFR81uwHy3jDMJSpEoB7VrKsOaR8ehdfOEH/ihjURSHfw88RTFrcSwsLD2j1htb2czAczvi6zu2QIERJP0v4EeP1LIptBmc1tm3Qzy5HHl/9uLC2h8rLc8gR8bOPKx5O9+ZRrSFtFBZO0V3FloPbX93o9ozjAGpyeyf51xvDWWsUVXiZa4t4M18y4Ko95t2tJSicWhTnzFfFWzea/Nt9324LBRK7leO/Vmpy3RDZ1qFpPFziDD4fAe+vlHmgVMGZsZCVhCt9oXko4/K1nyqdI0JjIcgVkO+NVbA500VB50NTPpJvtXfMVeP5/Povs5aGQIoi5vMoU/8yD3oQ4NQjth2uJchRU9LJwmTTjo/qM0a98TZsXqrI8T1M507kCqDHy74MGhqyLARNUlXWFDwQr/Mx8782Se28KUdZjG9wC203/F7hDBPQSTGlEzxHDIUr9x97l2vuc9mcIA8DKJ+IvGwlQ7GlAkcna96OSKnx5lKuGu3m15ZAsGBZJXSzXMe2wLc13LmlH50BV9in+Gj+ShcySdfvMhchwQBOIaN4kd8LXhGnLHY4ADNtYDC3MVSpeL1xEg2sHFC5KPqUlBbbRJfJNjEWjIHWg9t4ur9pjmvhUkvnEwERpT16nUjR00N5KuO3libA7B+pnyb/o3SP7o9epILnu5VEc8MLazu4OIs8/MVpuljAcXsltUtKGrI532iqB59uVRCwgpj7vIkoq6MoL1L3bffVxJv9Ib97HDlexVBLxJjDQQ1BApMkSL5jWKEGwAoB/Y4U4xYTlC3DD/LpTtRknVsKrJMYhBL6g4EsVgSKu7jN2WKdxPxmCWjCxEWH4kutm/rH/x25zLCEPp9As+x0dWfsRic50LEdBMLGoF1bWW7rrKQLPl2i0hU6bwLKx6E9rTIlQ/HlPORk1upW+X0wJM8B1IZGWaYIEArouYnCWY4yOUqR3vrjjKhqz0WVV8qBtMI0kFTBSYfXSOq4B2ru/XbglrVN8DyA0TNPUiZSW5cBCZrjOlEoBcCImybG4ZPIKycotQL/J/3nHb6sQW91E7rjbp3rVms71glJvAN3le4CpcUV53vqFBYCgX4QOn3VxhHZbTpdfc4dCdCyqUp9qU9xUJKTzP6bQlhzdP0aj661YKJ9qyhlwfse+oQQpylvEonTVEq8Ns7iqFx05D3Cwp2/cpVtMyxaLSseR3ArrcjuEL15+bAkQwq2fTTFgHCp7B5/0yZfWisQgNjt4kQfbBU3eobDtEScBa19qz98Pc2wNTG7hujbLRvrXij3mypi22ry28WvIXpXydyk1SvKb4v2rQqkoamevpJk8JdaZ/eZRaC6PO7bk2q9QBhcAg9W7BX8pEFNtpS4YHBL3yiL/IEMbiHyQ7VYbP+2Y4QHW7SzDWylt9h/5OYm0GR9vQGfxJQ25N5vqPoqAJDH56M4/n10LYdS4lBfvQ8baZSs2lf73q+vgqPnhZGiKZi/9HMZrgxCm1zJfmDwjwGEL8EjBAFMyCVtBtSV/uiwPGVWwMBVb9Qkvc/ilL9HFGYpcIcecVCZ/o4Hvy8Qsj4C6/kNvYNrpDjqptsuawemQEEtmWFGbFZw3/SV/+UkTh39OMJDYWu4CWvigbENn5OP/wduBlb1pkEVZGr/uoi0datAh9Wvt7/4Hn7Zea4uwg1Ts4XR3qP9Pi1e76NiB+lOdJPOOpSExReClckuWs4hFZPmOhuRzVF1TUUnFm6Jgq0ny2qXpwEaB+EE9bnJY9qo7UnJlpyFbIYlI5nBnQIbP2Q3mExaJwEGjnlXfw3+4azNHi4w33zUVE/MONroafNT2oYfu8CT5QPSzrFGTnO6w9bOkBlm0g50rfycu0Flg5fRB0Q0GR6/H4fK9i+VaTILnuMukiytSMeqQKUyP2H0Yhw3ZJTMvmuFzi1kBf06/tSzBKQCf3gSeXJGWffWlmLaB2UqLrqVdRKfBBWRUaYMtgXFg7vl9WjdBa95P3MMj/P/bHyvmRbyk2TY43y/l3Y7R5e8yFrIUBCf6cH4fBSf31t76iKx24gcxQDhtcIPjXp/tgZtky3M1+jWVZJmPwlNqgqAAaNaezlrWk6eB/10KR8E/7dEgvJQ/G/EPdAJ9plBxPAsiV4vDd4bI18ep/832ubweaNH87j0mYzl2G0pSGjs9mVjSRMykdjGx+0pp+lsmCG2SxLG/VcSffg8MHchFjqrhhRMUeTTKp+FLptee8RNShZ5X9MJC5ZG3K37Ybj6kOvY19ZmnCDfTdT3tYI68IRDzU0HEHP3FqSXbNNNVg/ynOs1DfeluSpVDsZWMue37Q/Q4fSk6Rn07bHd4+FOG8cWW3e/FfZTk6oXtyWaD7nkDRSL10uk4YoLj6oVDqyNMh0pFMJ39ypAJ1oOuHXEfQH2TrKSrta+Jh6LUe8Vr/o33oMhVcWaKK9sS1PJ5NYJJBP3/KLcFQV89zIyt7unb8v/WERjYXnKNaqpNwzurFQ4fzfm47y9A2qnWjDskvI6tNfm6JL9+mK4QFmslMFXfTajvZhPwKbA9AyIJR04pzDBWopw6HDMIqBKkduiA2KR7UmXGhBRpF0mpxAEoZx19znVhWQzdkgOKk4GzFOTFr+fdmOkipPCGiU4wp7njSiIgu6DtqnVzyfjLunNg1JBrXLMssJBnq67SK0z3Ieq6aaKdXhUrL1dTMWFWzrGaZQR4uJEnBFlokqq08NanzhlqGctqPOIts3Em3Tupm+utqp+qRdIs7NUC6zC91t4ZWz4nLhcQOU5T5WPITHatOouoS3FuMOpyIfafWk2SboixXHtr/Brkd1cewd8JKHmiOjFmbpst/aQ/4g0IDETWiA5c+mztdEoqGrY+FRPiDmTtFqwmx5ywDiWnY7ACWNKd3YjXwNdyIt5+intsw81FRR24zHWyGertoRlewSkaiF4D+RQzKh+P/LWE3f9kdh3Z62PrI91DKYobY0tBOGL0El7Iye0Mi4oCRKSRwPMQemgleKX0g4dVbK+aYyHoOfOfF5JJvad7q82zRNBco/4xtn/cMtqj5aNYkIiEgbacHumjUnHdUdF/ihj+nDduq8mG89s9v3r9kVD5ZFUqAvjAXx3gCgVLsJQZFHcSBa7mP77L3ShoIuT5gp6K8mrxF3gXJ6dOB4HpZenu61CFMaF4x0fWFpfUtSEmmzT7To1jvDyhLIx2anCJYiG6nKixJ4mEisi8qwsZ6c8qLUycztoQ9INtI3vIm1TmkdvuthnXzDf+vmje8TLfFoELvVk3+B8Hs+7F+sZ4KEV5WFlfJcTxZm1Ac6U0JZ2DdZ/mKHzmRFIxn39Di4icnl9eN/dAKPVcEWWn9+aMJTbS1ZMVn4iKF9LyJOn6lcZt2Rk1KdKa/6r3l3QgCpdGxuJ5h79vn3ew+MDJ+3e44RD8Ccaan/EfbSW93tWR/clfBGG818equDaazFpzo5KvZ+KbxVjMRD96Ar2ZbVwBK+0RjSD6xK5PSKFk3CHwwoOcQ1VDAZ8JQ0ukRqdVqebJPt5iwT/UYyElGsYz8qFHSMfKb++uYOOY/4dASq3ZgNCOrjRrhwM/GRdaT8quzHtojqZr9pXp64KAnoFIRRZ/j7eWaax/ixoTfksYEJ31jXcGGeoPWQx2gh3b3EhgZOZCpKQSaPhl/uDNevyW3wNyk4nWkX3yZ9AvK4OyoOe2LJVDW3AHooKCLxVV3eBDCTBAyLJgbWYdvF4x6QP3/cxmOD95hfJ8dqfa/B6fWHPcr/XiXVhIEJ8+M88q30pSEay/8srX6vVpwkyaE91mGj0kz9+66qEN3IKwKkJJkVO7v/ljre39gXTCF1qP1q1MTMKSDyxMyvAhZfMFU9zB2zA1bfUKRgOGH8lKyNgfMuZLpyxVZ047hFLQB+CJQ3MG5HRcZ1PFj9SJRxMFlFYV+3ZCySxHxnl3k9qRtZnzsPqj5SCioBO9gCWqb+lhtJX9pqi5ySuAZw++GFBhwSXsOMI7A2eUwN1UP8T7BvcCcNB+V4m2948sNF5fUofv8woBf55Hc5EQiuzeXyrDDUOpayXo0tq8S1HaHhmaOYPhHYixtOh8c0c5m3d1RMDOyeWiCShyprjRRag9wI+quCV5Cf9MO3CQB0j49V99elAB595yh/n7x6F6jJMRwUMhkTFvpBNrURts+HPCv51d1KskhWDJa8TV0Tzr203qwjqwA38PA0BXVPva9GdejgRgCjJFcmB3tuKp0fHE8qVhQm4mUHu0L5EnqFsIuxYMk5LKqmKhhIEJ/n7Omcg9rZnmORZelTbucd85/HjZfEsQqvmR52rHaQ3iNVSPz0ubzQFZCTplOyhYbvGLrjhDrGZos3DC04XxfJzm3sJEC92depQ/20b/4G/ZbVgE+DcMDbU7qUOQu+/0NbV3K5ES4ZYnQejXTwlAxaB5WJJ/2JO+irJrtNXLczNPrICxHgmgblFqjRY0JMEKZ/You4nh0Yc0rUhEZb7dB8G/0mhA8z0rXgqlgptOCxplhHXp2Ot2rVPnc+rpW7omweWawxY3w7iEU7/eA+TJu6Lg4DNJBauBZdEgxFa1ni9uggyukU9kKZMHAAsr3Z39B34EngxwNW8HN+5i6nfqK96uwSzxRGHnJ6lwvMfE5AiRrxCZiuW6wL5w3hIugh7Vgx1gDZltX8xIz+3YpxfjP8fuJH5i1qildmYhUKDKL6166l83TyArQcASJ2PSL2WLfI2CUGcsZvFXJCNOAOOWsnRXmuV23zo8uX6E1liIwIOCH7WeeeGXACG/+fom8bIwiMEnZ10b23ghxWJZx7YyVZCTyDTGHFKYBzDAiGp4hx9crfRJecGaq/OY9O5nDAtdxLfNWJkQqG+OeUd3+Uu03XKsHLwtxdOU82afVOWIf8WVicnl56/2EiC5wc0ls9cTgr0j4TUEwA3TCHLHQ/7rUScg+wBtisKJ4y+tU6DZDHbG8fe5Q7PbEe1L6S9tpDFGkoyvvsNiu1OwEwRiX9yJjRVvGgphYH8BXSMeGrsbg2/TOYo5DY3HhTmmatSK1IWkRogEU5NojksfgbPFKp5+xoJ7jpBU9xXSJpbePRvgijOtSbUwMe9lLqYz5SGssXk3lmNjSAbdNHVfWjGQOFhG2uNB+L63pIt2urfGP4YU5FB9taEjgjW4Ga2Vrf8PrjCqIpdq1Yx+lHwYkonXOmFmFCxZHn00HQ7qTyKD+ubl2G+JbykVMuIhk02sKeQgSmO/fsc80smOLoZ3ZphjPfyWuXDe3naWcjWBHv96RV1y7f7PrvjrBQmvv3DxNN04ZENeKgX0WMs4xYWwy+kS0URRZH6nuXUuFkZiu/NWcRkFzmy8WEcyQ5IOctgaBYPkTGq6PL0EjqcOHdEsa8aM3cOrg3rm6LFpF1sPVFVRbCI9FZMV8yS0GzipuaBhMUcrr6Fg2Q7uVav8TkZmUXYL09NjDEuUxVlnUD1eAGN9Wpkuq9WNiKLtWc4oRRLEWKRV0AFbigXMyMhBCs9dPmU6d9yObJPy/EPKenb/RdVZAPsj3F69IR2mxDQSJ1W4a9nA+6KlLUcRYHb9e6Jlb/IrHS+P7js2ouhMYrX98+NRmw/yY1v4iGih8S76MZD9j0JKi+udlXdHYsbWqzw1sWn8gL+gWoh96+Rs3M7mFQXM1wtc7DHcGyERUcaD38Zp0a30WIgDYi5iLT0PrsnSMeuMxUbfCAjlLOeMylQ98NAxgOL/s4wTxOSEhPyEmF/ujnj8f/f2lyg5JnC1kyrMk1QrVpcsgDnoc+qcnXa7GLWm90z/HucgN4xf/pJuHpdryvCCvepICovAYqcBRPmwS2xEBr8w6Wygeuoni8+vkRfHVlBjkM3YBaSA+0Wwog4A0pRri54cAgR6TrK1CuPe3qPaWnTH/PEJ49I905gHNdij089SX0N7qynXtfvGLg5jzptG7ck4SIDxHUgttBZ+wmW8Oe0L1RtwkUy22zBEL743Oa/+S2aUPGxqcZjXPMANzllmRmstOT9vL+JiH0nOAOcFHA1gycY7uEbQDT3V2XNtjpOStSUeOK6oqLa0yGjbqq3Pc2WmhbqQk1MLMhqW+sish2dcV4bK9EVzR1nm0ymHubifCeY46C5SG8QBmNXfc83KVtoPvDcGRgeiznj8rL4Uq3WO3y305jBWD0etQoF9YokGI7Ik2zesQGeMKWt1Ky69s8+S2Tj1APnaXS8XmB9rjy3N8j/BR3mkUNt/zRV3FYwR5goKNNBwYicFnbQr91RHQq5++VNLToZQMHVnUCcsN4j3C7lS5guozwALj/tJjjHg9pCGf2vIar9yhZInWxENXmChrbG2bbnuGuwj4hidr8jYeoD4CBV4kDxyg2zCqISodfhSjQ/i9tjkEVxAwqXrUYrDHTZz7vPoPC6ygnhGzTkZkL6CHX4BchcF/7gJwK10Wc9ILhr+pvjYtszol6SkiB5sEtlJDMTsztyuC7LCv6RDUdXTnk8ll0e3msIbI6PfC/2ZQG1x2woq3UoGqK/oMxrqOavzQxTCknGL2e/gYkaRx7KL6VF57Zbex+RC1R+GMp5TDG2ioSwfBJArRb5prHkpxrh++eVQOM9m4WFLtSm5Tan2CTfN1/5+WPusYNQoz5oJMj4z2qsA7jnbALnMyL9flnADshjUip3PF3nkV9Fh2ciCgYIQ5F8YT+4e9SVxtCt751lvgEv0MHKppL6lVwFP7oSpsDdjHhrkQVVlBMG8AWmgw1VUEwkmeh07UscyHujj4XxLoDtGYTrG1wCTrr1T0RJqIcoOJFj7qg+j+Jq3iebHzZtLxDAbt6zbHh4IjvnQwwYHbuTz/CltvMYnL4YsfOw8cNx1sBT8rcTpCw3afIEDmRECQYa4b39XGbuuc1bZ2uPdZBoUrlBNl2IQtSkVPq/q1ZM48Kbyhv4Z/Q+MWDNGKwppWJdm9gMsKJyKaBpGnpXFK5cC2n4vWwzbuaJUtCL//bPH5/fb1tKns8s6LOELMnt6iuGL61xRagE+pperpJehf0f+RFSfyUEOrxcHkqJTgcDdG2eplFsMALg/SSXAs0tFFWC2mKYmG4h6dnAY3NxgLyKxIEJOxu3HOGldVqPBtfRh2oIqH0hflgH/JtaBUitHO4uZbaAFSd5GjvNw5kly/lDL4vr87so6IqcXffejxFuotkDhQVcdQht/oPiug3mPPGqGru89gOIlDh0CWYN2CcExXx3vJ8CVX1DcRr6auY4oFp1/lfhWA8irQjrEitYkbYFVmmgnsqSKlVnWkr7Y0wIZzUWZxsf0d2CEao7g9FG+TgqJN8HUft6PihaS2zRB2ugYDG0V/jYiopFmfAQTdXVXhLN8W7M66mr/Eh3cPJPCKMqF3ozSGrEuhV0wLXsg81nbBSfe8J8JWysQpW4uRH+52Vlkw5AyNb/v+hLdgUMS52yLDUWQCo/MmzL/1JgSOS9MkwadDtDrIcwVEx6RBnSg/eJf3/qp7O5ZSy5J8mmXUD1Ig4MBNaUh/s18q03D1hG2RVMvRpJkml+E1WrGuXRCbYmzZI2hF3ORGiXtl3Wkv3ksHTR1YzSW39iJjjXDs05uTE+LzXKqbPo43ByYji/cN1sB+lmVqdgnROvgcAGY1P4wPmA1oBKU2yYovmQ8Qf4pltPA5WnoaSNSA8HPVEb7N3lOhMqQijB9xTIw4P7LIBNVCxNxy8OXOEN7ExsdYAWZ7wYzSj1RROTc9+v6eEDiqBcPVWPP9IjR5c7FNPfJt23sRuDdR0TAdpTQXJKvxsZkgBvYFDmn89NH7OXC7+siDw0l/XLpj3g/0cU+2WQffA0Y9Yp+Po97569aaOJaFlH1uGCw0z4Jvwk9hnSQwQbzobfthpGshiDOb1LDgWSFtzVLujzh0Nk3DVxdGlVgSly53zsX/gry7Xr3QB92LLVQe4rx/93A1fXmAcbd0uUoEftW/CRg6k6S4gQJvQOyPKX9CNB8PZJILshKPoUXYKw9J+2HdR0fi2rCyFFvQ6azYWaXZVZkla5gLeIIdWx+Pi2UjpxE1N7y6w1QVg7ZlmULdReTHYPS2h56UUDNJk8bN3KIfdewZsOnSUu/9N1ccjoOEiDV4Sh8x0x8g7qnPUWu/LLflLE+/pEuOhKyts2PPmu8FD57mgZXvAgntm19hZBu+/tS3thN5DGGshjqqIlkt3eDl1efYS0M34lpVGDTQCJ2qDaCU0doY3HsD8r3RyWfC6ZvneevwWg5Os3ZzbyBKVE7MEZmguMNmHFux8Vn3uB4v96IX0+Ks04+DyOs/qeSrOHdvAThmNizlmtpWOnpG2K6IVe8ifaPADJdYvUj1CQUPPaqY3GUJTvYrquJRrEfzO6Mh1ydzFyoqXEShZdtAOQiy0d/eUlbw7utXddixfOHU27KnxEyXjUcolnDSXzQ5gNHF7TR1Lb5CeKH62pHL9HLFCPU5rkeN21U/6vHg2fn61ZMGHV0sH4zBwFcO+ndzTR6yrGfiin9CRt9SEY+VzF7AbjY2XyjSgQ5zr5OQtsSpgkZrTIu1VeRxBhgDUXRJZQ/3Juo//jxf6+L6n9UCU91UJPYmxytWOcQXYHE9GOc2ixHFW1u0t+fWKJ0sZyopsNWec1iaVvGsPu3DOM6Hq5y3ldppjc0i7vjFOLt/suPeSjfz7C1IBkcVuM7Za12wKTUcPCFaegptw4Ah+4e2LvK6ARoJ/1HKHVXPJ1xkLTpbat6e1ncWWotMpijTWJfg3hz2wIlua0FSZaScgpKoANKOldXW8p1cucnJs5C/N0PITlZKhYLnv7ycVTTz9ibyjZBLD3n997PJmDhS2DSJFq7nxSPgm3ylLw8nqzx+uVSKQuZQ9HZK0cm/FqZj00B/2iy+YLwck25hiEsQGwTUGqt8vY1b9tXiD0ICh9rsB7HfsHuWJj7Zt8tP4KQNnhq8O1QpSF/mUxrzlnrhGzUSY59/wUQh1hCTkWA64Kzw2SjGjp6tf89OvNdmZrC4LEkNDqxQnk5ptYAibV0nZELoYO2PqkrF5Sy+r04lV9PD0jVfQ0+eqxJzzp6qSV5Lm4li3oIVJFvYH1oYb0jhHCug3dSn5xGWR6khcD8A4aboph8s7utdg0YVqbjjOxtr7BxB+kdpFvQQeEsUqXGan3X27KeebLOSLA01LS8lFWdzLP0lgbFr8g7tu46A8tE9nqJycW6GZvYc0MM2GwWLh48kPbZTQ4RiOlFckH40S9B+zI9KfgMLfN85kT6jaGPmAtkCmn0UVraeyIQcdWmQc3PnsWx+u6L3EpjCDQg0jyNA+rbqc6+zAKfNjbNYg4SsvorqvLsiz45x3ceClNkVr0MAInKRd2mE5rDf+HpXq2ipWPcVvn1R1ImdUbF0Den+jkVKFXOS7aSskIuM6fipfd4CPCpKi8RTQGN62ifwJepa31+t/ZrW8OVrHG8c0oNbyyPA+K8PAiVjnpzz+UKu8dar0uEKQKehnDPt+ERGe6PFoheYNSxkvd80tCfsxzpWA6p0fjCWYYdZ8OSJl4Q2Cbn8DNiC5zmXufGwmd3/oGcHRUAW1ZtHYU0yggSdQEGxwI4xVrjsIM8hBqjU4ZTUBANFbQ4N2xySZlXuv0TlRvQseHx9YPWLZKwV1H/+Xy2uUwG8c2w2NJStkypraM1Z1QIsVv7lLLhvQjpvErrReaNOnMf6cNluQ0Qlc36a/3CL9rDXWMlQyg1XyGY5KNe5c4LSkF19nvOwcrAaTD0uavT8OdlfAKMqoitCPhowvWM97Gmv1j8Md7RLwzj1LOMWLY4vkQqECaKGM4hBJxrUiQeFf4ukc+yAVyh53clp5jHY1my6DWuR7mPs6vzY0V3J/h7eMEVyI7Yu5a0IqGuzRbfmVOjAA6HCHZMJCvOxa47sG4f8pBnpKXwYj2MhVLt0xszZUL6yvUz6hvpMyjT7ZzUm3oxgZUUasNlPCyUe7lx6Auc/TcQKDA23pW3YlMFNeC7kAkJXFFcA1pkb0nKMnuS/D7pB0G5jXn6Ri99oDWBvv5z6XZ3eWSJ31i240CKz9YPR1gEmytDt3kyhgO2LTf0eRg8WuQ27F8uDcxmrSbNlWXHELMr2zHc/7Lq0DVEhnIEj5fEsWihIhNPubNxYScwJ/EFgqkMGDkVf2erviVkqyoi6IPrcW8YpOA05ujGNDSxCR8GtXOiLXdIrhq4jQaIt/ISEr/vq3M3klhzO/xXrVjsnqqehn9y9+Y9nOiCuHpOdWFmtC55maluU5ypbvrbmBx0kOFSaqjxWDe0im+2w3TrSY+ePlVqHDGytHCyNNO5OPN93ubsRFw5Tp22o1c+Pc2s8TJeNRyIE1uwfujyn7mXEMGLEEI1s55zqMwDMZV+DXCKvoVM6cFRymujSPRuczpPHfU9QomHoYWxkEDBVHvXgSohNvFff/LmP55xyF+ng17OkLc3K4Q5kknDPu/020z5bYAMWioQSmMINEOY4tcfuqiEnYuYo0eGTakPC+FfX0KuaOnnUGeowtR6yr4w3OGeMQRiHddSse8jETIpaDdHyFVMEjqd7ErgEBhG0FJv12wc8+E3Y26pKIpTuNKVYS3lB06xu7WV/RTsImB7pcMcU9MXJ/Y5mhTuy5fioXKCVpxrKId37bBmpMX1E4Xd2672E80AkJqdiU9+eKzwIcHbiVaJ7O2d+0vBUyT0OewIOjNKKYP/PwVfq+6nHpYS3C48atifektkZGygL6UIpEQVFbLQBdlIFkgmv6kK8LtE3VFiD5BuNS+YShzD0/lmwuyiEHtB9pEZeAokaxpgjyfUtWrx8/imaITo15k4g91MA5GdQBBIy+Y6Iad//ib7D961tXscQtJJxllsdOBq45xIahYwWjL7CULdwGtsOpxXNal428SJVHa20wk0pelyIGot0P9wBb/EcqOuzswtUi8tCDMcObBTXAz+e4LElAeM2vMZ03tSn737jcPNx5vhnGgNkzcgiuTzvUajgJio541Yyco4klFqbub2Lps60U7a2/mwpDRlabW8j2iyOm++YYCgsV6rHOu40cj3R9hVjTWIER+zdXSTeBQQ1DzBMEQWu7HxVDv6T1o+uTIjEgP7drF1FwEMJG1WxX/JlA5RHkL2HHF1frb8G+hyDxYTEhQPXR3OorFr+sFODONVdfCJlufpt42+cGqlBG0yVPFS0b4ohT9z60fOXdQOJCph9cct1BNpR3/cjJvVGIgEkcXDXhTK2Zfuqcuqh/aydgoLrYivpRh6/4KAruvOf6VA+FljNd5BzgsdF72QpWNtZfBrwAlGY/2PVdZzIRU69dIO+XSZSVZ4qOsO+MhWhLT0Kpe656Dr0j21mJJBURaPyhBBz3dyG/BENTuuZvv1Jth92QSC0sP38SPjYE7daNl9Q9pe0lsxcdF3y0HTne+yEbeoxFuXjzxb2bQv4YveBJdR4Az6RuvxqoK6u83uAvHCholDVU8B/+LH7Muy45ii1J0wjqHMZotVcZxeW8fGaFFP8JOEAznFpy0YNWBMjiV6C80mKq0cFl+Rb0JDpbhgiq4kinRf6NRsj3njnn1Y9U1Piurkld6J4YYJYhAJ8idaRTcDef6XeRamtMJt+KzF34343mIXXPp1Zk/6anlL6P5GIvSFS31m1Ug88CNuxJolsFBppC4pbvAObONahwNTumt4bfBhbdmlq9yqQAV8TN1dKIQ9fX+QDLwKu5BaMOGJVB7RRPhBMWK+Kw14jIdKpjqFgk5gc9taksmmwB86PDBPVChhYPg/RQSVCr7D0Lm3B84XhJtpmgX491QKvoXCFsk8bXB7/eBtCyX/Gne3BJeKhNde58KRBJWqeNe49KLkSXXREtbJ8DogyxOjq9VOPLbivwvxTjrNncBKKl7OX5dUPUYC2smsN3eEwuPDbhlPQiXWBmwDEM5G5gVHqdEtrrpAbbafiw063ZcRBQPj4sK0B1FcuZQEogyMlGKBAZLVWRPky1hyzFlQpBW/X7/W/L3B/tVvwudOwlqfh01dDC30IWvmVDOLpNWNdvnvSaVS1OQVW1DuU8Y1AMHtLTDbp1GJbzJtrwwC/Ez3sLxPMWRHbEvWwi5Gsc0u+2pR7iwsWUgu4zKnBq5y8+dpqK/7cjsPI7TZ26MRS0MuU075XYTeW3UZLpmUj0F5pjIT4nZb6vTlMsS9UUO0s+UwLwctXfHNb/w6wtL0phOTDIocitpWsEWW/SPRN6lj6xnuRwJH6dzflJvDSGYrdmfFtCDiVpGf3cFsbtR+DUfoYRo+ZLkxPbUxriLl+AHE3+MhYJR3JmZJ6JIkuXAIGv7zr5uO15jvJ8naSjbn0U1TD7xbSViNbImR95li5KoKWBZh5y0d5MPfyT4rjMi+WXC8ldn3dBrAjy3aTxQ2B6qDyIGvEOClZQhRq4oTyw3n8fmpp8yM+FwgO73mgeJbndBXIZK317LE5g/AAc5sjtY4WyIzLvj7bWwDdwezJAiEzg3cbNAFXvw1frQ6jfSn5C1cpqFkVJ/CuKk4kS8KMmQFayoZRf0VCvCEfWDOJ6qNZtGBMMSvfRA/cyIvkxlz8SmMVCWrdRQ/E1UmJqFwi2n//ZQGutQHwcblLNNfpV7e1QFdFQ2wqUisIySLizq/unJv5taoc0BIDYJqEV8VZEwGyUAFdBhngSTXX+WPz3kxJWY14lbwYB6otGrcu8B7MdMSwnLCGjSI9jKqkOHEcv+3TLlx0SO0+wUgvJIlDMSDYp5EnxIrUXf+HqstsOoaTMb9kQaAVOKbrFa6+HuBhIHd3WwsfGVXtCg8VOIW92JI11dvEEDJS+xNSv+sVX7Rg9il1Gdm/0LQt8cz58Blf5zZtOYan86uYjkxWZ6gLi/t3YvTUv9hM3ir65xuEsndCZqmoWdOmwCCJBh9cS5/3vGbharOJRdPdL5PmfHRqMH/Uz0qw2G17zYTONz1EdXfvbXyiXqKaKmUvZ/JqbPa6Zvhg+2fm7sTkpSfzRo0CVHoMJvlfHZOPoN3ha/di3+9rOF78vweVLPn2FMBOI5XvvCiy51N+0bv1CDdafwZbBACDCz4Y7me4aOkBg7Lngr5EM7xFdHzESwq6lkY91bB/KczHX5DcCctDJIM/5k/VVgfsmVUndOAgkPLWHEPCMMUnGvvoNQW2O0PzTOE90TbWrcie27pjEJnaNdCkEmgDi6GACyVUoCQ7C4wXWoujECp6RIXrVcuQvf/nk166RxwSMRO7SBTVQavReldod7yHhUPHnuI2npQCXxDk5DP0JBHyBlL4QZlUYtYJf/+reJkihrToiKCdNLFWQfZpKzaiR6DL9KBj702KBBb5hTgjPXFSzcdeAPdEMUk//pyhDjEq/FGzHV6oIsyUYkLAz4BHvGIccLh+6LjOX9dQIwoe5kPMJoHj6Z0bUZ1CcFSileLsK4jDkymry00bmIoYrYd2ss1a8D5OK3MRmlXHILCK/Dwi3+iPnLONmPYt2cC2dfe+g2KzWxqiljftt9qt83HJBlVuTpXLnLpekrGIm9T708IGBkQnNg8u8IyxOhzPdJA7pEW6YMqsh4E6EgGghOQMs2ucSElVuzHyO+e3+TD2UY3AT0xaj6zQuhWHZEiK6oorG5wq3mqjw7u9KNwdTKQy6bQJvYL/+1xfnvfgqWkPf/j3flkV1qwxu2PC5apxzoxoOTi0PwY3hy3odnddRjp5HRn2SdPwxdP0h58V37t1Ihn7eIaUrrlAY1vWSYTufzi3+i2soPQrzZ0ORQl9kFX2dpT+NFjsG7hHkOWQnHpe7K4GacvZi6DtGN7vjmA2pQmwcuTBNeBnnefF5ziOrNPU3llmvpXMqcEs8LBw1scvhJBVlchnkLTnpTGaAezqlPYSRngPe8S0lUS4stkJOg53UGQ9qL9PdXLCtbKmBcFms9zrvhaVN6B9F9/Blrck/E2Z1pLw1W5GNdmtak5m0XzSjnkYjcnBLNp3l/lqPVOPPXofQC91WSmdFNfIFzNFmuZwUkHUHN24ALjX6lZvNOuMFibrO+GUV9ObYOlgjfFz4+Lt572YTwvzy6kt4WzkroBA18G6xYAXtnX1C/VSKxYkGNlrA7kTRSQ7uLKxRTx5rxUJixZxOEQtMec4uJwCr2olUp7SmQS2O3BZ+O8EhumGGTLOzwvcq73GjQo9VutHGwxYa06YXS84H5qeBOqGaZGfxm6l1MtsKHQN1TyX9+HGcWa77LN9Ll+dRMPsiFjHbMfJKEba6CiVqOANyrpSawFM4kjVWtXjoHpa/h/MJRlKU9s4EqYuj3tLzr3XQRTRQfBkrtejWSfFVIjrW1ovrZMHjBi82MsqZEjcb6/YfYBRZ6UDkwazXHD3qQNAUGNTtTrIayKwlxCmucW7QmSsQ7YYe5ugL5awrkkIpBIJenPs97es+t9iUg8KSqwZddKv7x06QVoeuvbjvAhn5LpeHxkDWvh3lO0fEm7kvlyjcycEBK45m+Xi/bmezBNm5eIOcYzKB6gKjjoOPY8fSsULtET8iXOrzoqahLBI3ZbRsdBPIEaNjFVJAhF8QaPfnqPN77PiF2/RhTfXZfMXL7tCEu3D/Hk6lMN9aKeQaeesG98Oppe3G7DlEUj/Uy/4ZM4GzlMN8coca2dvpcgh3/6UxVLES8H+DgWb77JoXQCThBrwkCiFJ5gdb86uJNCtLLBdzy1pEXTGJYb9/Ri1FjZzNR0AducfTYjE3g9drsrSWXLSSw7k/1rQGsb2ynGQPxuEfWMyI6moa0g0Djj9WeUkFWoVB5F5CLiRe05180fceLQ37i9Tszwo+KChHUrq6E0vvYzWzya2eb4Ya9uXzSunvIfUT6LjtK3qGW3ICBDr13cGn3nKLxQl/GOnix0O+enR3YMe2fTCQYdyFSyCXDF6iDJV5WvkSNfnZBFznUHeAJmTFh0RToVmBBFt6JG1vD/IbbXo3O4oEwFcMv1EXDUrYm2ZXV8hLSV3VXlxCM2N4Anl3wGt8jEBdet7WJvU79AeszKr7cW/Q/tinJHneEp2PaHXcQbSEj/6VAqpy7eTa4SiH0e5GIXh3S26yBtvkSYrwO4loTn+7CsiVn4WJAIw+Pre924Ks6QeuQnLYdNWlshpaYYRlY7n625hbn+rT/pOUdTD1iokrWsktvpxv3LgXoI44Ig+mazw/E4bUXVS2hDdGyJIo6bnGjJx+1hQPwHBqDZtyXjkxWB8hNYEiRdMy9sgnohx17r9q0tLJy43evFk9mW7jtDIosXkVJ9kppbROB6shaz26WHasLxartW4LykxHUFUhT97NxtEX9GOZ48liu9G+iRlSnXvpi8a+Ve5iN//9W/Mlav4vMyXdOQbMS2RwB/+j5yuNhx7xVwOuqv3iUxX1O4tJHmcIAxYtT7Ook9oJHpY3L1hYhiPtJQxnrs3TKX8eneAzKOXEy1iEnZzeNTmORpQ+D+T2bdAQ07xiLZaXP9fHTk7/9AzkXFUS+jG+Qd/RIUgLTFCku3dWQ7hKKdUJ6cp1CBBKQnQUlgyPtLfccVm4bHUkC86r5eTFuQjYUX2giX+L5jXDGWC2FrVF/9D8A2CjxghMfqIKLo665NFh2LXjVHALHOA8CdfcY6W8U6Y3wZJcUkBHpL+a3jIULaU3MgVwySIT/Wvwbdf9ykPcr6eTeaCONIP009PEtRcfQDDJH+ZMDtCPTqWS5ClfcF/JZYV6A/DoTZmvHBMJ9n3wQFhmflRY+QBoRi8BvXztoUBxnBZmfLcufPvxw4M5cNDo5xjXpWg7XvRwaqnA7dkZSx/677ykYcGpuRl3G0Ytx67tzGGua45wu+VY1enp/qklgoJPc0D4Huag8rUSv5YF50kyH9BCZKQE0aXw6FxVeUbRwJhPcqvcSKYtLPbXrCSxkWYtpa2N0X5lIz+3P9byYFvL8ThZRJEF8AY7BqX8C7ant6jrnT/bNHXii6A86ieRO6a2Xi3pZIQ6iCx6kALxwPY/d1bJN4ppEJLYBZeEgYmjIFnGLl6AhD8znspgfaFAwveXCcQovEiKbf0exBajkdHgksan0zhxHQ5OkFLCkvfKoyTUPrXUXNw13QHYZaGB769g0uV2rBRx8V2OYju/9BtJBxv690XD4ypVxngKAM1epJ2V6mUfv03MYxYmgqdlxShMKSINe4LB34UJrqt4QWqZJPB98ArunkrV18Eyiew411AuuoMIig9WYsd4hYY4pai3vHsIYL6Oe3t0Yq+woa1ug7E+d7dVF49Ug8GPFssemTXC9PHidCBCnc98KaVDh1iGgo+4y47kkVtbMgMDpXV4NwPPoNvY+RSjVqWRpNG+aYuc28L4EYvIbi+d+yoTqd7dNJ4EZRzTMXSDNl4mpES3yF36qRWF0BoQL/o949oJ0fRRdectIZWZ8a1+YwZsMVNs9w8f1wk4tsDJwDWcsT6HjIWryWwFkmR0TH4eHeBKNPR8mIKDGmG/Bm1I5ql8FELVu8oMtqFBJt3NLfLavuAQSi2owTTnvNaD/JU4ab2KnC2k3WgtOig2EOFxfBCmgAmbx++/XH2HlBOypTpdRsoKlFCGdZhfhm10vhIwShJltzc/gOWwgnqmtVB4T5JILKS5IAjW33g+aucIaIt+eqky2fQ5C+meeRt74s3PaOuSGhrMcU3IsLWmo+m1niliPWFVV7Q/8gCTTe5W4MomCd/Sycj5mQXlXb99MsZ0LkAE/TZq6kY0+XoojXk7hg3aqCHA9H8HK8haqvtn43hJ0ZHmNtwzpnpLdViIFb471nEqXMkijsINKkYCPaTx3X4mL6xgSROrgkPrQkKHSWUoYUsLUVnnYk5j34mNCoCSFwn6rG8tnoXh9G4dzjXBChWPygJnEN58LUFTJvAOVuegP/9ejrgvZyABA1UKDHJlHI6HYR+NYqrnUvbtVZ39u4HiigoCL1SaQHJYlyTvpvDaF02mH+l8Dq1d330f+4Dq2ZLRttKQFYM06l9kpcyxwKOm2Wv6RmISp1oQgHAFTpqDdcBYtd8SHyWLw3m8jmx9jluVAsF1dui1WtmCzibg7w331kLwmxn0qW1dVKwKRf23RUJ6V9/wk01BAshWuUBM4gAd5+b32+SZ2nBEcUg4Y0XP5z+iO90PjvPJgo0osIF8mXLKVZFH7CiTzIqb3HxVyQ0xpJuMeYNjy5ogdQBVQ+4BVqvO86ksNaLbp94fQ9s7xZF22FIE/xlWHDUezK9uSx8l7He6Yv1PANQe/VFKivdupfbhjUiFbhdHAD2JRO941kZs7HOW5k7HHXnMNIXxuelrEjJWtvuadnZ14hrSlzFyQjKLowDiKZeqyN4LA3aABkwikxB5AR20VPQfNRjM61gORsQ/RC4M21HJ+tLHfWc5Jasj2uVHkBsjFXZPoatXaxMKSfUGjfq91AqAR/M2u/6NysgYIdfajRK1w+uIep7bMpXxGonyMTAy4oq51IsYjmt3JKLSheN7U/Dupx4Njq/EyW/h/0uY/HhMl+3OTWWzs7GDbdONZ/PUbCOqxOf5DJcxz5JqYR1dpYBW3gNbgNNBKxw5ArDftIhupBHILPsk/eau4ZIsC3jKG0Vt+DOb/rUnhXjQ25FX4nNplPXJyW1q0u+cj1A5Ai5RJx3mfQwnq/Fx9iIgk0o2T7dz3zA+wRPWHjVG6g+aEj+CTFpfd4D0e4qZmIAfZ4gnLpJnXnTK0J9JpG3wCTAzNiRAfqVSGaDsLGWuMuLKeQkg0o43XvK2byE7REq1wXAuGO48Tktjk7+LtTWpANDTRohySX+rq91EPJelh2UcDilRAtteIM2QL4WlPP9jpRDtK0G7WYTQnxNoV+f2UBaO56sFeKOA3W8mbJznwWTb8th9KraOZkw5AX7LAnzWPhORc5j/JhraPs0GNIsEgWDuLpWnksTb3WyrxoCPIHM9EIIJW8s2IP9M4A9Ba+taTW1TYOiqHyUTJePOTKra2/fYMUSlGWT+CknDf2/eqwrnMdpvOb/sEjhr9NbIA/8qRPL9E8Z23dtLspAv102b0WO9Lf59UARiMM7QuB3FYDiJluDzGv50hhGlikibsTWHsgXDvCqxMaMe3GF0FKt872L2nUgC+hC9JAwHFTBbG8AbqYUL22XzJUbpdDzDalCA2z9ADyr1GA56Qsn6isxl3jJ/9l92DwFxswcXk2wZEMZWYbVNB/MS03NSIwtm7/K0EzaRv/B8smb7FcYIyCxTxrZy5TWd3XVKrgwCxWuBzIR+RPK86tywbPndewzKDD6Sz+qIrmLlT5p+SwtwIzYgj2OFno2aiGcYq+rVUixsz9olfS3hE1aKB30S7jRpCUOlVDj/WEuYxVSH+zlxy9gsmPB1sXWxq86aPBRHLAib4xyyyiLdqwpt2TOx1VuyCoCxzG2F87RlPyVSIeI4X3BMVdM18gtsUWnSEJ7y0k6tbqNJLwIYronc0UtMDImxcpV1PZxtUSV6OaojVN0+FkFEmX5OMBaMNY9t+hyuKYBv8nWOw413bZ3+WoDcaUy9tW4U9pt6v7+nGhfnYtJecDgp+9GSxYbpCE9QSEpvbcQUN9ldIYDxE9FCUoa9fpU0VqQcOgqmbx53gTTqhVtd7uwvcZntoS+VPHzVrj9NnnK7IbwlLHPBYzy3JJ2PZ8p+e7jstnov3V/TB3RdYcCI+zq15LrE5fE0R525hy9V5KnWXDDP4TaS6ng0+efktanWy4L0CEAJipBFf6EOR0ylTZS3ibAmK312NYRhG0j5FAMSqFP1PHlI4kxkECHmA61uVyNMN7LrFunhLqJDbTtrgBF3+N0kwQg9obfK2zAwdAkcgxfFlL24J9MoLFhIxDafRJkZBWiIEd9GiO1dP9nWfJcMT4aRgRx3fzzKiZuZNHbJ3H+olY6z6ApNBqEo5AZerEPwaJ0VcGrIA9CZ0TvxEgpOVDxQy4+SUdygb+Q5ZDkArfGV0+46/d/7qYMNkEr1WB9cmqK4r+sHqwrBdaOSbGzJ5mG2ZAQJYo57shYOYnynw98jHnapB4Z3xIrv9xXnJUCLTsELwZ5zfsa5diYM7DUyZNK5O0nxwuIKq5m7p9OYg7v5cNmCUqju+Qs0+sPVZmj4/NdRTfppbSkkIjk9kGjX0RNvYbazTixO9+19KXWLCd28p9AByq0+euXU0WnEfRPpK8n3RzkQTSU+dKdam8+MPNZLPhi775KvEkfiKjxz7S/zbugd3gW248+6dqVOdWAA4zj3MnsJlVbeYYFvyrzvBBztiYy6Yr1nUMRR/aBtgzjDQ6vpeaY3Uc+N4VmeneWYYH1HDzaMR5Sa8JP9lXf2mFKKh9v0ugnx+rqkcYSeVIXiXivwQ8PVKqttMSIiYvXy+1wnMMINC3l7oRwGc5GUB6oHCv1Rnrre7ui2yBufhfg2woyvwLBRQlCqFHimfv2iKOA1gVTJpjHQU7PzyxpUGO+tezIWDyJVHCHdOaLsxxn0WWaJ+ff5Jh+eW3LuP1+7TOpeFpU9+Domy3F8nNpQcZ4PAP9XFOTl29g+GrHi2DXXES+tdUTn+8QtnhcwBGISS+Yjsso5Z3Wh2tuHnKifIf+QpL7hTLy5fPEhk17JtrTZMG2m6ngGJOwovjVHvdjb+NB8UaILRVxI+kspCW4iMFQ78QT5182Vd8vRjTe3FowKNR/Uj6MQo7s5J0mPI1hTEGnqCN7hqXMa0wIKV1uVsICciZSm8lKfI1qSMzp0bWzTuSmN80Jao9mHMcVZ1OS7TZbRhx47DPhyBUzfKRy46csv5+KUrdLgmXP/s1QnDglujTDF8ISbnEtc05jFd1HDQYyXhaapVA9ht4GydvyolSFSJ9+XvBToAsFyD6yiFG79cQ3uNudHkJ07eYrS4JoA3cZRZWz9o2ZQKwIwaqo5xAnmw7RZ3C5tn2FHxXC4b5wf3WBi3Hm6n7bANx9WhzPiezXdJ0txgBneZBPPMCjgiz2KxXj3+4SBZDb03z2yyeYnSG/1+GMsbRYKT9mFEas7gqrs/7m6M/CY3H7S0jeNSxouguV6IFfA3fJKtP+40ZszmGkc2//iyp5F241LXKolbs0Gwv9sSnS4ZOIQunHKpF9E/N1WhCVKxQNt8lY+9x317Cmz+1dl77DvsAF+Yn24uVUKRZZMwYnfc+tj4B/Qo3hh5ORM631vKmy6VkyUmYOTd9SJ9zf0nBY102ooliURUVh6J6PJBgzS1uhq4k6Z7iEq0pghiNJztDrqf+9xuhd4+bDefvcRL0u31gpQ4N44YWukT+E4JpNma/1k5l5j5I5XhHYmnDphYzVBr828587OHRTlX02Hq3KIPeLBiw4OZS7x8ct8g7KIKcsVlOeDIY7raJxc4HVcyjzSEQO8FecxlOEXYAVwLLbFRPmvIKQEnfkMGBXD2JOJAr+HyfHwZHss8W9AL1rgzE6fzhd0nIUMnlGLqpbenVp9LkyrxAzz9a1Xvdl48tLTWSIuXmRx0WcTeadD/8aTNVrSlZGdc4x7DRjc2KgUDbkfW0ar6g152Z0pVAJnLF3fhpEOUEUbWn1iFt1CZITkvukBxSLPbDymH2fAZkDxSP//7De1ujajgIthZn/IHh1q/vsSsx9rGuJ5uTmEKAL10tICAQTajyw1Hwe8r41nRG+vVIja2jSTeSEb8D3w5xvOtKu+sG/NUvP9NAnC49VM9VdaIpU4A2tuyozTZohecTs/+t6kTgUIseyjBcBqeeNTcjRKK9XJaMSYhNQiWA6vS6al13RAW/lTfxoLeoFvoPNAydaccX80/N4ykPy5eBNvLljX9U1M8Twe693LmufQ3y9ttCU6CpZR9gEjhXA6paVNVo15rsc41x5K/LQbLEmsuDoy+E5hthB/kyWHXOXNyL1F+7jaEPTCG8IhgtVN1Qs0kBoxiozEIdTO1iOQiSWFSur4z5X98oqYYKOabFUeQRKbzUpZtgM+wvccpGwRH1K4nnCcJltYiIksCnUoefo9wXmOxTm922hovml8BXnh0QRT563RjsawFdl+QsZkQggp0R91FNQ9Sc9/koTrxCEFMjYA/RwQ1kN3co2anumZY5YPcZjPqoyoKzeAPTkr9Pch2j5sHb0GBVxgZK4WZqV+ROGdkS/PAQ4y9EECi8HOmIUteGbaOaGI5sLtNO4eOWUKhrnVIV1b1E56wFGfTXKxWOlqW+V5qI1jeDaAjNdzAUUMFHdjMfaL9y5mVZavo2R3QBOn69pYLG5P83G7p91IcnOUS4Dyp393moPkmE99XuqSlKttUTeWxRDWIG4rNOYPPAOgtm/W0aBFxY1wTPfp58BjXPOvf4LN6/gsEAxMCSNuuxNUlsXRUF5Ka2p6r8Z3TBLhIqjJxiCiII92ODaUXUf34DvSgSQsOUSRwIgl/DXsCzBzJlOteJKx6QJejLwxNjWp/NgvSzPpk9+/XdQLltq7YtLb1Esc/NKLpgnyKe7otqj0gEqvGoXpqeQwSUYmbeFyx0x3LDMljOVOCFBxKO/H+keyPqx6o2Rnb3rFQSYsQkX7Su8h3q39BVNvADzx2IlfGHqDQrhMtMkL4uh1hHwlwnzepqYB5rC7vawSOwTh+p+OjcTt5mA/wGRNZ0kagNg4mFiV43G21LD2BucrrwwabunpJwLO2j7bk+d0+YtJD30+YSO2Lr6gheO4YKo3GxgzHa2o3Xuz8BHDBOhXbM59AF7M/kI7huw7THCUeHMUDOGyrDqsS0t6s00psYC6VgDSq/w8VZOEhzTB410Qxl5EpsCa8e//cVK27FVbMJc60I+QdB60MpI0DvCku6Eke3rK/JqBD8GWyI038XXK6SAcG5TBKrcBdcmCM+R6elXMm/Bw5VS473B4sekZThZhOZQqGUqglCaxyV6+zZ5scBcWNd4OH/nZHACgxnPZKLqtK74H7IOng9YlpW5J9IP8TpgqN+s8GLFad+RrXzP3R/grQno5MVGD+3LNSqfGST/IiyxwMYzVMi3hUmn8sfFDVKOz75fi3xGUdnZF5do2+Z/x63XUqjDUC1gesHilYm4Cq/21+miezqUIDsCAZzLgo1w0pinf98dJiEnoHHCpAyFtzroJsUDBdalzN5mbX37vq0cpLjgfUcHRJKhR64DfU+KN24fIu//NWmx7PWpUmL23y/Z53I65iI/T/p52TOfOMfMK8hHN5geKufaMAxL2QLth29DgmivC1Uu0h9ef8tzG3RW44lY6c/t8wzeCMe6XCpI4dUsfKnTDjg7wRNnVWL5oSfGVuIpazo1kGwAx7BbvY0EkKAxKtrWwIDtv6lxRzLQNWtkoJr5XV1Gf0ZKPtSrjILbVEVJ2fgOBpVLH50lh3nbIHSwfStkYQOunZv2vpQrC4vpNjWcgn3IaTI8f6tB5/nw2slcZhvXRyYPQHqKO3sJUXeDmcAfnh5CZSz2ohXfDSZqon+bIA/6R37u6q3EVhm/+PnygJpEOlSbxk/q101lqMYj+Tt1E0zsAdkXSLvWjumTR8sCzq2nTZXooHRTTJ8ofLlFLYOwf+8k+F5B2O4WRSJiIHCFiV/yDv/XcUH7XDnEaBtbc6E00GF20AbZitmKqSFA22k084iNwusZHDgY+tA2ETFUPyDydn0na/lesobW3i1Hqy1e8CQizwb3au8c4eirKsM7h008UJckaAErsfOLPq4lM8lgXozPK0+hNkS/Tb3kubkJBEBKcGM61R+8fH6MxDwjItYwgxCCLnLW75LKNxSsUwWjUw+3ClW1vDFzRiWjxlvltYgjuhmUsLPqT5E/D6Xi2OMIQsNNh/crdirvfG8WgPWXY++KKMIGJYtfnfJlNRtVaO0xaRkIVb6254P80puTxKxcuVUTPybkQAgO2EKRvVbIAzcIFheOeKf2oDHrRGx0O9MRdxlbHhuL+O4pjpxgTaf6cpZxTG7bRnidT7lszuU+SdkPe+iRGgODueZu0YV0TzKh6SBPQb8B7aleZ5Z7fSKbcIUFNjfjaklDAyiYKRXGAe7YVazJj+NAKM9sSzJciKatBOgm8W9+UhyrvC4kbBPZAuW0TthKv18abOCuqLpWP5gVtjXjOlvAR79FyubEOXrHqZn/l8sEMEIu4dWqjJnq/8tIDAnCfQ+uZ33gmGt9PuIMdkhouPRjzKcm2oX/uEhGkXvG5R+zmfhCqt6flTkyP0AtcSCodFHbLOHc/dwY4BitPY0ycn+gjt6I4X1Z/ee91GgAiHF0iQz9VBWeYc7O0/OrYSg4x2IwfGM4kFBRcSqjTM9ejbsa9aEwtelb1P8cjo+IDnEN4b7yxUcEHJ1P3aV4cXzvbZZCmMe3qyeKEv3qSZ4PzI4nVhHDbFCvuL+OoA+ACeqBAzPY2cZr6b1UGMet/N08TPPW4bmb7RCY0L2Uv135I7kK6LeEUhd1M4HU8uYNaqehW14CTonA9q7buFcK+rMwjP18YYwjlYVxbocmXsmrn9nHVZIsXRwO5uRiBcdLEmWYmBOAuyo0opK60r5tbPQB3KR32MQU4pAk6bgvSVGbAkuatMpnAQoazHaTSc2qwdml/tGkdGykKpWSDkuxYFqSWZ4TyZPdn180fmTKpGv5YjIRwcngHYugMoxOUlwO0mY+QydMS2p+VvCfjK1wYfmco8cAsOt/w3MOxWgInkvh1EtJXHu/4pKPs2jOV5ZB85nDkmJ3Hi3otPp060w8lqJFaFhKENo05eFyod8pBIOHISz3scmBZHd6J4TqmPs3tUF3RHFFwqNPEzDEfWdGs16zhCbMchRdjWL0q0EYEeUzTQ/W4NbOT595ioGd3HIuMhfAzocR00w46UwPKWEFad/J+c9Ldqz2XwP7otrwHYrgWWOOOp9rq8v8kZgEVkZfw/zqZJo0o8t7L73FVOa30n6++tATaDorXKIuRN0d9wE0+XCS3fpdMbI9b3Mna7xOSdPYllfH04wQtS0YYUR82JXSfPI/dWGGNvqeR9cHfdLwEvJKI9dp3ebuN9R4tO7kWGW0Q51D6bnGQx0TPLRplxtOweg2xXwcSTxriORSbcVwLtd7h/g5o/3zpn35KRgZlPIiG1lz7rhI8zF82625tp+h+wK5lD50ngOnH3ng2GdEkKIJTgaak03S+70y6VOJgabYFJvVjH+Li6QRLLaPI7ORbWFaYAdUcMSlzD2NsX7JmviqNDZ3okwE5Gc4S7PtzEUndfelNujo6kaGDkVgJkoObv7QVgcyXnYiVSUfhHMXz5IdDCvIMEzebWjZakeErzxO8ZSb2avpIzdoZVWUdszSKU2O5BpfEeJ1Nd37+ceWMti/ttaq/DsFOS+/ISgJD7jrkFgEriLFaqzMvxRG3OLOyhfSmcMjB/WPtN2+saI6r7jSvLeV4RWAlOLHoi5I9poQyFvgo65eEySTfNEzMluRwKbgKsxt+k3TToU3TZeNhMAOidpZ5kgkgiVy/NT11l2hTTu0Zz4CmfD0hkW3XbMY2IURle/LR1J3liZ/XAoDAUBiRib07WGb9kU9F76O6ItBeXGF+M9Ov52Zmx2JcIMWyvcr2OpoOzfy/LXeeMxNYEVsVosgmR60wfOvifdaPafMAlW/5rvmdvH23EiOeTZfm0rLpc7Hy1SQdDcaj8HFIxVVX3Sa6kn7+CVI7vl/y7t5RC40QlI0gCuRpbF72Wt0EwH9Fpj9+p6ojXqwewwLHVcrDbeb3b8tXTDDnFi/1MfU9S3LnzpIC9a/dCdWmDniL2lZdI1W8DVBMkeOWMahxI1BPkoR1Qk6YXRWzi9+6Pqr+m3TxtWpidyj82wy+56qQpVvMi5wOL8olEZfcp696VRgmXyJv1YJPUQhWGHcUdeb8UWJMte+nO0VEe58utqmKSa5hWHITcx5nwhGPr5SBOpLwpxLPJXIv/tR0Y0NCgsCUgZ/tjAkkKNHWBJufL/PN8PNt8e2kh2sY1p6b4F5hqfb2CfZAIIiJSUDLUrx1xKbS4vfM/DAsIzEY1GzMeUZbLFLdwEg5vjn/qbu5N59xg4hILqDT2xxAfkQep2xK+B/w//z/cBkpVYqhor1zn+vysfkiABghWMz4zDjc7i10Fo2rW9kvqb3kH7Smim3HUQRXTH9icvsrXlf5DN8fmzQ22CNKaCErBkLWr37VYZk5f/LgGL8gnfZ0YfrjV4LvoHOPiBAELf+uaN8eL+75Ecc/nunGtUTW5nm7arEBoYMZ0HeEpEERD0+3/701FlF++0QcffE84wVdgd4aCCE8AehmaBGnPZDgcbFdqUkZc8ZAmB3T93BkPZHaxCCYSlu9ZBcoOfrJT5tixxAhfkjTtBVjWdUo+0LwtnNMzN2T8YbZeSuvmW/BpADfEfX/r7oDQfweEyU44EVKqaouIHpgt+4p1rl85POGuqLAT8JKCs7/o9JWHlKw6zi5bCmTXBupmreylaqBClBqMyfjIl8LnJIW7oE3CU1q3mBTRB8NEA9lFO8DMRdg9nWNtgRCHkKpV5ch4XgbxgTVFEdnsMXMC3QgWg7ZhHK0OXHu4U5qTCwWvU5O4gY3QbrURARKv6411eQ8gw4y5SrLvbH0xpcEDYPfXGU9DKsPH2t5T8VGAPZ565JB3QHwUa7I9KFxrsQ2tBDXSPcsLZeM5WIJEj8nuok3rguZROCZw4dR/HduX90cVsuvmEo22CSRvU47j7utxKHj8JxhiYJPlIEMaXubpsnFbiFOpYvCstTXeHnYTkyjIVYEgA3VS6kAARuMYOPx9X7zYLSvMZ8LXrRRo/LJXHYmTt8oK/Yj6TnO8975+K81I3NqN0p35VhvmUhyp/IKKHU1JBpllL9N7V+2tceNDBiOZkigvW1e0j9sP1Oqm0bP5K2atXWwDWY7SBXa8pSZNIfjnx2JnLGUBMRwdlWwPMnKL8ElRjhewYPY742K0vjyOG8PPh9/+7Y27bVvj9QxM+pwrWfn/8Qf/qCBqNPw1g7kwjWaWZQitwk3yQKRxQ2pD5ge88n29HGTQZMHvNWbc2wNXM6A+osBN0FivlSRCGGdZCN+U3Ce9SLLwj/Ays9DCBSuW3H6Djxcyo1pMoxdPdZ8VqRu1QM+el0HuVQGB0au/zmkaJmWQ3iZ7wvHB3oWcrdYNtIi/e/Ed8rykVxfR5805iiDHhifiPRSfGyeGM54ldffLFf9pob8SHb0dUfkJepn36vA7uve8InJsePJnEXP9W4zxzrAgFz66zct0ENYuTlIrzobql+jaXztKP7qvCpoFtIgGlv9790Poxgmiy8tkZLFfvcJOUv0h9rETDHjsLFAgChBYGDBXXCobzycgQhEf7OFWd/vRTw6xg2DbpmAGP6MTcVkuBvwdADqoKG0Hyt8QRN/ZXQAsZL6lOWX7G8Ib5Js/HM7Wl3crgFuZme7ibnKFJ/MsgpLnoM/LG6gzugytqaqcyXtncedjgHYDChk2hNtRzyXfj1AFWYRbMZdBuXEbgfZszENi3vvSJWb1tyiJ1OWC3wK/uJDpBNqJYPdOQVP9/cVzHG/uOrn8fCOpKyDqaWyHwlWoPutsQx3b7DNLxq+0JJyuROfAZ9RPzfrASos0q9HUg7bSQE89z3knXLEA7atYu1cHpHY42hA3QEAxtVHqtnuz/O2cAgV/7m9tapwwTkOVqbOXNG1iVb4D9p005pzVbkt0MSUfYAxmKEsIt5mG9085RmFGkCQHeFw9Srkq1Kyf/RLyf+mZh1cBxkspxdk0bk1LrIZRiC9KuECD/hG+gZRdrQjwFF1nMNATiWz2aMrwtBTwU8zWjYhSnxm0h/LX6yrCTcTpZb0G4Vx3F5sfrVIBBsJ6oSUR8H82ozhS1NyFVvU7WaBZ5r8iJoA5KwSfQengNb8Uzx4IcEDAgVKFTm5xJw7d67U4NcO/N+WMen6lOYmn7EVFEeElLb+5vZdEqjsQ47yeUYcRnk8j/bTkUzJCARwlB/ptb4LhqMH9OQ9sEFzGdjcKLZ71lNj0o2PUesx8G5w11VVtpEI/pElHZ+Xw7bBMQO6KSwJyEtABjh7pY2NcxSZXcSqZk79IckOg2CPADpGNEDE9j0LSyCnGFlCJaVp0lQIY3E1N5aJSW/Cy5x3KlhDW0WVM8WGIw3OO5v1gH15VNI2Db7Ul1UcXh+263GxUhJ+LETbmxOg2rpbnslR5wXXjUdlDmMfFKKqfV89JbqhJO005P4P26F+Z8/9iFYY1cXKhTF9GdkcP1S/eCqQQ6jqVPlT+YHA9ysrHxNlzsZw+40ps4UGrih8FRBkFWbAtGC0I+QTfzI/huCGeuG+uL6qLjRIZvfpjcID0Sc0RwVgqF8SQvaW/H30OZKvBlVdOIrzdDPBSUZB1CnYZyGd9xF+NHqIe/QD9pWk1K0fYrRO2tpY5t0eINWhEseFpdwNfIP0KBEyr1mseK+MdDciMIeiAXMZ0LqqM+lxNZ+wM5FxCRx24ljHA65JFodlPEOFDd7AxlGx9qAWSazDsR1dF6hmkTKXF9hnhqtMHoWxyDCiHbXEaRD2Pnmgh57uiXe0FtHLk3GogbYajlcncjVORYVWkL053IASRrP3Yf3DpUo1ISiuwx5gCtTl0XByAu7DcSKO1I3tau6uzJlRIAY03oo1NhDBFPgkolpZWmYGnpANGEpRpRKisC3CYuV14gB4Ujncayhh9EyKIE3dcjhrElfxLWjrHw91Hh6dEn41JXhylqQQk5sYErV8R2nR6w6aQzJXSPuXUG5nHKO82VWJa+O4l/p9bKSgXsYOebbCok/2FwbERxXsj5v2Nuen1TubWg17/XQ600Xvb6Chn3r/Innn45FQxPbS0+uOdZPGp96oBlL2H69NfMNHMpm7Gk2GjJdgPjIL2KLsALnjefRv687gfzpgvg/WBRucQv/hET0cNHI5YHPIWUibOBdDyumyo9WN/29PucylPo6qGJObGb0Yi2VNAJx40RnkoJwZKXj/KsCRF3xXGvoV5XsbS9cZ6sW0cj/YEHs+z96EfPlw3BIR/2kztIzkvGiS1Ek1RMO3xdtKKhNNXNCiI3EA0xAIY6/g9UO+ZSGW+wwz9Jloo3aNEnxb9v3REIHHE3WRLFumrVwo/esEiwNAMinVfQT7Vjno5GGZR9Eph6lb/YD4Tjo8306uK7qFIiElmTDENaHxz+Yx4p7HBii/T3g/73IcQUQyjjH3dV5S2/1O+m5eus0YJihzwvFEtoGg2kHi+o9WAwu1xLiWUmWb6SN0EWpnvV6dUdbE5VXz/q+Yf93lRupPSHCjDHPfMyYbnzy4d33C1uhoOuL1tLRugl8ASXogb9GxU85BcYVoD9McfDUBAt1QqJChJZcyeiCqZs/+rrVX24TaQxrm1X/EeULPdcKSerjgbaxgI3SGZQFNDuT+DDpcZgD9qfQyLoZ0KLd5gH03Mrhyr+uTYvg5gG3m1LPUYH96Ke1iHSDgXXmCWPdU3SyioKf1LzplGtqyPan5IMgnhNySbD+uQQPK45xiKc+tR2jWL9ujiMzr2Obd2xgn5MMbnpPVDZzxXVCuADCQ5HUuloMzFfkeszZG871Co7z4kacQ6o1ghE7+QPLBbF3fc05PrGNM1rrAjRXBcIQabKt/BrrQ31+kMRGFHmoqJKj5XEe/PggDzngP1jBfjovnw7JfdcLzb1BerwW+JdBFxNr7bt16ULCq5z3OPXONj5mXvw/yiwFlcEIM1xiHRvpoZOOFtt2TnkAQwdm2p6QHoS8mSPUiQn/suG+gyKbzKtdy6pycrxJ1tBY1ezTLJoN8VY36P2KlYJzcjZYdvwSptvW1UrA93emPYtjmJefmK2cRSDDc56adNEriUUzXF6zBcfpgL/48Yoj8qhbCfhwXIrFvxAZMKB85TqanA24nVLnDWD3f5keJKFhnc04INuBVKsNK47SsOZNpg5CqFw6qtYcBKTY5GkHQXU/rgSAvmpilb/Z+2VzAee03hM15FuxZmNn94RMBbrtNrU60l4OmzK+Qmp2Cc/ZZDI3JRez3eeiPlUoq71yvPRy4zZi/pRy1ppQOPBKctDFvSAciDTssNsb6M5txy58bL1AF7fjkV1Hriu4A1dCIwk8zjNYDW5+x1vf0QrBndHnKLCsQub9bwFaEl6ncysUH61uqJKmjiypVD0Tm8GUYMeRKA1mXyGVwtAA0zgBcMUu8cCfzRgfGPC0qaB8oQ6GP2gspMrF8uEWtQCs9Gr5ZFA8eVmwTlV5wSB1Qx9qgk6tSJ5hmRiqiSVyKd4VSsJ7UD10EmTwIuaCop86gM+b32GjnVfTvnor7UeuWxPm8PRPO6Z+I1Gzr02b/dlN8X0X/qqV6rhm3C0APgoTGzLqLEd53poYoR6vbjar9pOyghnFhvltNFzDmnerut/ExkxPOwhIw4G4/mRewvbCCqBXQHtxitZW8B0V/rkTNvE3i3N+edYkESjwIpOyBJG2TDggrzhfK3oEYTwmFnNoF4u57XxxyAnDtp6Jy5g0MXyV+MP2jmJYbLrucDdatR3HqlwImRp0SbjtpUpPFsgUmROoYsb9G+V4CInXaTh9AceWI1QDuZwazZZCZ3P9/k5EtPoXsK8QDjaaNHqiUp2eFxoBhbd5Mm/bxulgiWLZCgmECNYhCLfjpqY1KMllxlxecUBDjsgHNqmWrrH+iqHRXExqXQuAY4e0Iw0KjVcEbs8JW3pFDDqT2lf40rIeaE8x//8f2mL5KQw14WjPMEDknmZFfj8bjm/ac/gSsVT3GhoodF57tMf9OasX7WcHJXrSSoxB/31PeDiOQ0ucLQnYBrl1l5WVt8DjNuyF/GmUSREhw6dEjTFhjlSGF86HA3UusIc4hVbsKXNE/1IEs9lfsKX0WuedNehoXwHtgtUG7jxgCRX6j+LHDOozgMGZFljwrst/6yddxP/1KrLEdowlTQvLQT2Etb20UXTUDvmGY+SHM01Vrv30oSOLxIKuapnceu9fcBlm4s0u1ceme5EUQA1y6/Ax9qAYIKbaZDzbL8415zfip9y1JH1oRv5lb0DYuIA5yJU7ApZLp7ZbmwEFPD/WwTigyDMLe4qVkYTPWqdNcOdkxRc9OtoYD1eRTG8VoLQjtNjAEDf+72L0r5bDA4hJToe9Nt2+L1oIm8YTQGewG+xtD81lCisJM4Y28q+XlVLQM2KfUP6e339DhXM4I6F6Pb6bE0kdP+gHg0uXrYgrjazBHE7zEX5sLUQ4uSUr+2Rc2NdwuSuAk1dbd6ISXfxrY2MaNgbcn7SW19LsUJL0BlxkUYOebaFzZAtzk7qapVfZRoW/6RCmwyMJDOZl4pfKZ+cKJvRVOnA2PzUIb6DEqtUcL7Tx/XhWXiWjKlVn4fbPzyX/3YCaS0nLIEM1rhuSM5JBtUcNvwzYhJ9B2wCkcK92QMWIiZfADXO0ylp9gHjC1CmtMmwzLZ7f/w7jrsHBcOIoR7jdXgnZdzJDG/ALXw7gnGDfl4HueHSFs/reihNEsRZfiifrRlnZzPVe3NTGu8z2DdwBK0eqx4aaVN1ZagXXi3h05Qub+kc+wsRQG8tWntDdB2Z4UgMQ9IIvcd9nG0Fk3fg/jYpXcODFi5498dtRMl1ENusBia+wBdTGlkqb00GnMnaYZuxgm+hD2GOteT1id6o6PlYMvKuCbLqKKPC8RfaCEIQec+gW6PR8bInqSTrqzUAVnS4b//gFYIMWcIL2c5toLttPExQ1L6upu8InY72GLSMnHd1c/CIQ99yXyACf3XYH6It2H6u3PtBmlj9l61T9R0wB+7rui0GM2ev1TPSVzvLIN8J11fWy7S8AdiCaYkZMV34+jLJsyUjAMPL+yYJUQR8+dSRjHvDjN16aFNwtnHWHHOSMgmf+0Y0wbHKXkVsPKPmwVJAzUgSHSzz3+mOLN0i1AdcMOPhAEVrGCbGS9ZIh6/2HDkFyXQ4ORmvrIfDg21CVqyAV+Invx6/t22sccoA7J5ltmsarlnJZEvFyVveCxnGhan4L75Bd3MEWbl2IkWUhY/Hx/pRzXgtTi88jJ2UpQ8RAeXp0O2Z0/5zuFVahwOucnfDku1Da3oIRYJNWN1C6FvYvn1IUsLZzvP8Xa3Zbb9LkO5vS6cOkljS4FPJ4uR2DLnGvxIuZK302Tv2VHt1SBt5np/Mn+cC2DfDnKxlTPj/dq4YxB+Om4j6fhnc1wDYG993p8bGTXiigyk18KRlNoBQTH/suBz7AdJjI3/X3FLsOUshUj92pxv3o114ewYRVoBIdWdG6FGlF4wc5cv+WA8Tvhm+bp9Od0DKoZPEEoCZQFTeOxNF4lX3ZzVqSN91nxNb3sujjTsgxkZ9OpgrdZXKktzY6KQen7tKeBl1Fiy8/hK27zH4eySalaA9YPNBC1pIXRAqJFRAEeDi3xQzRxbZ7ZAbbrwJ0WBejJZ964OW6w/IwB683FiYEf477qBFVyJaZywy2qvYeH2b73zr9qsRYgZ8MoGHvMOVv/ABfjtwXluZ5q5jez5aTi7JVJ5cEX5D9ejFphW2Vh8qbovYDig1iHzG/UQZ5wTtnH3CkCrjs3D9cXR3pGm6A11xUnCfw5Ld6LJYav1uMxBzmKCxoQb0bsoIpFfvGiUaJntKIT8ujeYcK6oYpMws9S7hHXvpAgRaZxGvoPL/NtVLfr+ptUp/MtEdL7RUnjWKMT9qP0elTpJZr3EiI/M0Gc07hTTVJTGEo9XOhZd7plQa+w2Wf5qVQN7DTfvo/rUJpOsqQx4H1V1PcrwWpDYs4Fu40NZkLfXuRB9hp3B3MSTKqEUVaV4tsmPbikCQmtlikfQYyZZ6KKGc5QzGsACOupE2sOXoWjSIOL50YVQ8vN8qJ5EVwNMBPJB+LFHvIdvxsWQaRorEQq2kBZhZr5cj6oi9e4rGlKI8oWr4OwGupFLBSaUSXAcHofK6OpOr6K3FNj5uKeWwRYs5HRDJ1tfOzqfbQC+WIHHj1+evz/oi3kKLM8qU1+igAeh901siVF/ey7FP5lfKutO3dKd+nfBIiHAakQ5ErK9cDxNk57bHNOEzgOUmj0CbKhAVpqYEbSelYmDtd4jBBowxuGgsYhqUc56o2ut+LVapmK2j1oImdCZt9MvIcUXS0s+1Vy9KrY4rqfTqraLaGTAYkZ+WBzMMnugMBo2ICnknVQ5Xg2t7ijKmeMJLW4wZJ3bW3y0+TpEsyBRDT0IB3d9MxCO8RsxiVlnJAufGLLQjPnBSckJn7E+fkYjdMXXitbwkvNNzspF7z/WERLEDryXcgDGqJmV+oknJ+WN+I3CYYMzrwfy2r7Iy8fODJnXMn3ZrXqzE+TQTnnT6+BNCFFSZRfqnrAt4UeR+N8vXxzaS1myWN6uwSQoAIRQayuwMwnbPWKJxvwhsIhX4emwBXePVuuA1gcS0rpI8aVw747SwQUBU5n7XKh8sIckE0uvjd4JHHG27xl3zV3/Ag92ZEKjZ6L81h/6K2meqEELkcu3g+rcfLZTfLGSwGzGZHcd6IJtsIqIxZuSImN/EUk/6Sss6DWCwP/E5K2RObsSjIQ2lBL8PbvED/x1v7E/4p4W9CS/BupLr4CpINkm3+mbC0bzZmeICMUo6NK90ZPgDHrTzGokr+QmwbG7cp3tp6/XCraCMy/sykaHEivHItoVq9r/IZwc/wMVBjCN3MAo9T5SCepbOfpMpP8HmwnkuesmC/69YGDdA39wgaPtPqHmSjVfXWXOVbkDr6yxbuFIJc+PCZtJ458bOxHkrEMV3UtOLvPHAQLdnfdv3I0MJ9N0ZDWpAASAWTSpuSVhQ4qOlfFQGEz8apGda+xA03TgsGiBmNqsK+JRgH4GTWHNM4nY5Quhs3oPEMkW42uqrsYFecxMHRoCEv8nYJJy+GivM8WO63ZVQbFdttecGIkVqFYdFLkZ6Ljg3qilgmgyeSTwGl5tFFYpq/AdeqPWbi9++1ZPubmJWgyXwkdwpy7LQZcMluIcqxYACgibmYGRbQc5+qQCeoiQFzjyzziqHishnW/jfrR/YfFFDloaCc/DGzbJz7Bhc/5KRmYqYlJNHfqjh1mcGiAcJdFZE6LTiQ1FehSlm+VhFE0u2zpV+ZvqvY9KjSp9QPSw3A//Dc6W7hEtoc/yWgkMeUyf411qqRhyJugWne98XZQRZg0eFM7r5TdEkIrTNF+/sRYrwKMaobbOOnXy9PSecSZL5SfUib6VHuNbCTdfvW/j9FQS6WPvF0RAbZLtQXel78JRNjJHdqDCg5S5VdOLED4gqhgNYBakLzKXo+ny9tSMuLYeunv7MkRz6MazYUrGh8YzUzf4g/aAhF2xkGLeT+yF17OJhENZZ0NRjsNeoTPWc8gLJXk/5Mdbrmf0+58If3ZdP6D2L+H4dUmRYvUVyLwVEU+ytkW7FXyfIYnCwZIHN2W4Wb/RZLxJefWZX7fHRlY2dvd9RQ/5C2EsqGk5CVNgGsc+EXgic7BSo/PC8/i182/995jv2VtUm9IuECMxE+5iB7cTfluQtLgjoTxOFC35QKMSrV66lrtvGnY5TIAN9NZpX51jTLW3SF5cxESXGaS39wr77gJah4syD3Ev+JF3fGgtjyQ9LVE/FPqn9kcubeBmFbHUtRKlKdz4fdx1siS8DuKs95/+YnLCjM5MXsIAqzeey/cbycVeWLL8Xode4ua3RO9tonKMMcokGvpg6QR7YwFgl+QKne/kqdh+j/75rtRhkK3EtrlGouOtC89o+GTinQ9J5KTUMkQlmJvTNcN9t6a+xJYtYLRfRS67e5WsrTbjwdK8FptbuYiQ0d/FgT2Uu8hyJCWxZK93yr+f6eqb5Tq2Xz35CfjWTpeWQHJjFvZewG6TsDpoD3PuLNI5K0ph/OLMf/vpc5jFP5G41vUxY40B+DPH/JHzYUBJobVk3+B/5hkwXNnhwJF2Sq49IhZk+DOBLmnkZpG6KgWw0j790drvv76pjq8UaRNrMvTfdGJCGffxcn7+fA1AIswV0ISk04AxDSynLVrR8djEdG+gQheQys1+WPR6Cw3aOa6edhXzB5i2czHI2wJBgDRM7zS/KS3U11JxWLgMgR/RdLBVcCLAzFk1Z/uQ6NylyqQYgSbh/G2b09IiC7XE2wt0Eenz+c7NJi0RL7cglj0IGaBr+STdjHoheekY44MqCzqLJBBfl+rTBjPKIPYj/JwcPABCrcSqFy1u3OR7Iy4LUREMU1tfrPz0EiV/DIRD/zNgcAAcxnMjz8tWIm+g0XPO0D2iOGaOBZco9McHAdEK0kiP07zhvFnfWArXifm4mShlZ14izYISbF6s/s86QAHV6P6MckGp9aHuIoW3Sp0J8WotVzFSTkpdJGp9ty/qPpVzlNFKvucJSzkMP/N/wnpg7Bf0c9Cj/S+D0zFOG3O7bOti3UtG+LfDKMEZxgWNwxaTjEQ3GNH0TSq1kXRYkLyz9rGbPdvQf2+18Ou/bx2Y87wk3CVdtMlYfxAYfm5MztmafFkW5lYoePEhcRNTC0wD8sKriBlMjURsqYwDg+gJ5Mz0MhGqp8y6ReSEOuvHoXx3Dsb6bzjiBXlygFlsW2+WC7R4f4yocYBAQiHh+V8Mx9aRXZ/8VvTFisVIpZrTBbOMHSNdU01V0x88vQentMIZ9tmn4nEZ4S/jqqDNx0LQ/Rh4mLsClsxMQZTldwW9Y4+Y9gkbsK95RfbmKJlF6gf3EMDMZlFFZEB1eicszYs372mEZdiYpwDIx36hzP3gJrrZd0ovCYtyG8WNW3dOclFwsZw43XxkBjF4oGgcyC+v5ooQBvXkrIocoE8/acaw3WwJcU8zbGm7CqYjew/Yn/Xu0D3PIUD94MqmTeeDXtCHKTj3QUSzGoKuJbd5GlyiX7ebZ506LWtQTbphnZJ6BEq8/jqtfSyvD6WdLlYJAcDZdSw0pDpT7YR3TzpmeGhmFWaU/AmeSRX0tNF/j/Lbd6bcuVyQf6B8lc6NIP3Ya5FRf7NMiJebxeiQcmddk2mAKoJhfSqeEomYhE2kwPAZfBi+Pvv4lSxoZAZU9dtTXg65t4MHOinzvEv7sHu6imUBWURdsiQkuLSHjLabWohT2in/xVD0kgc5zNOEQ8Wy5T2RVt2XjZfJzuiK58ulSbhMkOiOuDx/ByL9jxh6zFEByZmlovju48g9NjKVEuh+0tHtiLVzuB03IQD2TXwChHFZ5aFdJfJxCW6A97riENSlbe1rNL7Esydiz9zM8MVf7C0X8zoz402hKsaqv4CjTrZXhkbg0cejFTwxi+0foPjSe/VrWWK/5Za6jVv12hmbac/IiDBTfzBwYPh5Lelecfs/jBmgQS/H1lPDlBbgju3LhJRUY9l24bZil7M5WNSh6jG1ZDBD8VaUFbDBgFtl3A6y/Jf5NSaAw7XZxVp/Z/ns7vwKk++uEzBubPwc5xOvOB3ClzHPpwj4DKchypjEecrwdqHhbSLneXZPUVsWGCewA4Fl0NKHgX2/sSvnMymZuZaDLlAIKG4PQboiCQx9xJJXz2ulaj+FQSy1sHOm5Ab7P5blMD0Ka84b8besMiAll0WxTXWztJeGv59nu1JZHFVb4YHGb30jz4Nr0hwxRp+oHGtbsJUmrRxwXzMSD6a5A7kywPWTIHzKN36cTK1+PddVmV9eexdZEIPi56Tm8hqELYxjKO4N2DV7TPEy34EaUiaV2Adh0WDmXwC6auuZxz6RYnwHnTK81j8uJDGEjodnOKfRFBforTZJ+Vv/tDWl6Vw1j/hyYULpljiOGm+UPa5na+O2/sCuCb4IyzJRbYbEQ/l/PfI3Z2/6O8ANLRG9HK8if/k9moGOWtbYxF7d7BqSmGAvMshNs1YO3056OiW9Rtp2McoSwj9dWmvtRj39v5PpJa3sbdI6hJFScg4TinRqdonVRnCzZDUCb4wXiJ8sdkA5N44/7o7giv2mFRTu63BmafH1TcAZ4aucs5/tkq5iEikL+B/h/jTPoxhM9zLDgwcBDDhL82l8ezd1Jwbrwfl3BvygCmB764T9r2epa+1WgGtB1qA8C3/MGZQwMO1BHiBk+BKftvhsRMV0uQT4Ki9kleGoRQ1x9q1Qm4v/kyWfbeQSZJoX0xP5S51UF4uFZhSt+OZLeyyipHiZ6gULkw4dC0nz1tZpItgztwPGGBm1Im2dZrR5AQ7QCb1G3Za3i5jW3RVyiz2T5s9r1RoN0stpekzRzVvz6woDWtzHhjoJBdDAn41+lZbMNOdA5hEULxcRGKIL2uWIySCXLUPb4kYYgg3mSflJufStoYJLIONZ56DYbFDxrLzDYYKHJqQvVxSh1mC5c/zilGUn+g7UnWGyJg/jqLv0yJlwcGT9dSIZVvrB2wYnHhgxOTQGPiKidxfGKl+LtLn12gebeSg9xuPKj+ShcROfR7wQ0eAldfcwfmH+YDHVdNK76FFBx/kJrUU6te0GXvEEH67p/+m94JTiqb3zkOHh+IJBwXex5ty7ErjmepP3Duz+hGLJ1jIRfAc1wx9zEhMQAJvPa4zx5FAGHFBTu1yh7N3t7dclXEsfmpf3x8ArEl74HYys9YEdVQ5ucrdcpvi5NmFFagr7ONAF7BmCemCt5AAun3ACov0KMvD8VII1rfCKVyGI7WJRBBqnAGSSKVmcl1wgSRdQdTmLBHjlYiaGvhz8D4JvA5PWuKcZRDl1Z3Qk+plcuKE3Efres0fALCEFoqz56AZaPHHNQwucyggvrIDw6D+O4OVpw3SCRVywTfFHBg3VfoNKDuwvoCLJGfHjE+2E1qtbB5QkTxfeCIl4p7R9MagA7mqAxTFYi6atakDHBqle3GW1DWe28hyJ586hXVcJbiCLKcHc4hzXBEK9RYaIPHePVKWpzJAlkVzkOlmQHIvGMBWs9sw1bR/8Or2Rfw7ZQL2pRmKHsLYAT0gdCx18p6nReWvqFCtyoaJ0QIvutpwDiWTtzepQgc9jf3hV48hj7XHQid5R5BhJGx+674zwEjE+Ovfjc4d9ig+0Ic9/AYDScj0Qc9Rw8SNbyCjH9yySYsQt5NicQmcZDmNyg82BshtuSjxSELCayUF3s7B4x1GQ6kx71VsuaD9TjKPbjcdyPys5PkagqdOwK/n3oyBGdQtqO0rp3ddjew8CegHWrFjHXkVT9N9vsi06V+NXRQVLLbS/wkrm79f52Pal87hqeZzPRDZV8xjeCQpOqHLubgdfZmBSZsroPB0l5JLWiXIWiHzSRcPyev/LXdUa583nlyUROsmcKJdwCvejbzGofKYY5+cVl4VwQEkJOEMGF6D9j6g2lr9aHL/4Y0j6cX0lMRvCUeL7a0ef/4XdmtQnLzEM6vj1bevUbohQ60hSZsCl7o/enYYdyUib2itRWkHjawC9hDHg8jdmWXxNQq5t4gENsLxWt8j5dgkMnl8bOBmAy2vEjPpUcocbtMpPmcUauJIDcFQYow0oFlBtWWGTG375KFYwye2VeAN16hkfFG4fzPy3qMk9iow3iSU4EzA1oLkHXteA4uHhSDcPArGHcoFZ6XbZRmKM1sIaDINtNWuR/ft7m9IoElmoIyf0NK6QZquHDtpM6ElwS9kQSSW7bae42I8qV7EjSlj7yxfyXdi8/Yz8+IyxsVs5XXQGabwo4i6KCmnn2cccedwlFUwgxjEtqkJNCWBbHg9dUKm5JbAuSkvCb4WRDbp6GWyY/SAVrfrfzpH8D9l7rHt14w3P01kyIEN9b6zJTGD0uXtH9JVbH7/j8ZdPzbPzAwMz1MtWtRLgpbSA7yfsqKCxoTtfSvLbKRm2U2QGjPtZGDyApZdXYuwYtIjtkcy6QJJqIWTBDCmY1SjPZG7JKWlK1WMCpBV6E0XqSJQ3zijKY4sW1U4RssSyiW9EGKAR7hlvvcArtiSzJylYDPiv+FFn8tKsCzP9aUM0krNll0JN6zABx3n4VuOKDZVPPhMzRdrIETpdZdXpXN284JHObZeg6qj+cL7uhiNxc7XrL2SJnBriUu4JwLKmNdPlc9EVuLtytiynsBBgR34gnJH+k+bUYVyT4XlB1ji5gbMOukMmqCICLn5DVRwGM5zAHhgAPko56yKPRryavnmaTSiOAlblazyCFDDt+HkCcDqmgMoExZvWJtvTRedvswdKaVona5j49BRFwMfRndr3HWCDEWKhwm/QZbxM0xkuQYH4NhffXDvw3CK9Di9TWI7/kCuOJYUz+8DXHpsfh2gYGfnrfewcikH56UEUBvIDg4XbNbp64fDtEz7VM5bXbJSlAiLOcqJWNQluzGb1X51vrurETa9kkeu+ZQcwWQdNzLSTYCKrqc22LEsV59WI8DVa9teqtewfQn+LWupUvWnKGVP5ATjFwhmPAaogyQNnoFK7fXohKPmYNNKPdlWniEXboPi95485aMG7tRVVqXn2u8WnqkJR2zH7wrNkIfVFIOYumJaSX5yTJtwsM81rF4E1OGSYQGTB0Sg0F8Q7ykrFNGZE4rueNWsFGRUYdvfZ/5DpB4RSZ3q3Kwarp8F3actYOsDxkK2DNWiZ9MIrhGZpnm/HrH6XVb+kKGv4dxiTCeV0rQ0NA4Emx4aO8ZUuQ2EKCTGrk2QduVn3EBPgQ+GSEw3NH5iw/uYTpE8tuOX8QNu+XyZZsCVpbz2+Z/SMKuf1YOsXz7h+nOklhHxyLc4yHvJq4ir9kGMrf9aNxIgBGPbd71PTU1zCgbkWjLBBOhD61mOq7tlFo4qf8AHezxbEvp+aGs/NaFoYSoqpnqoATEth+GAutGmz9c9tBaKmYWeSGvEzsbGCl5wB41wYjoVsjYUVxjvdZ7Uug9ONbRz3JqyINKSjc7yYTI4xOAWjFIOV2G7jjW/6WKwxKPrZ/LVGk0OP1K96ZAYPKtjjcfrY+4a5Ul88io+15is1V2jyrxdGR1hsJHTTZ3KTbmJ1zPy9ikwQ7mp3lijs6WtzjeRBeagAYs11YxTOZszwPmJEA+ZQ1uokdfeDQpES9tZpwMk5lrtPIZ+WDkEgUVvKI6edHQgkZAaCTZ0TfCxwXt0ZQaVRMuYyKssjJpSErAirUll74bmfKSBt5sPUMCc+H7ozR2Z1aEZGFrhypnS16ZL4/jiKUtikC3ivtMd9co0qamskyioLQhVFmWaQ+LYWNf8eXO6GAM+g+o1vwDPdTHsm6rgLYmWxodCrUyGI3M9oI1d4P2suHLqtjUZy1KAL5tom5r7dIj4hRX5AMHhv5mohsF42nnoPKpGOjrP5JhqHDHY5BoJeUvolF10H+cYXg/pKbSH3ccJ+ykgW4wrSHNbsH3mPhNqRKr5XocgVnOZ9NFdQjLKqLf933tW3TSj4UgvcUPYEJaRH+QUozbzTkYqf97NjnLLQT/lAuBSAhLipn5+90Rludwt/UK2ONYzfygZ/6jM2YFSevkiEpopQ9sPpcXK1RwEtXkc+arAa0n5fwXxUzuxDDCLP9siYMuPxXWHDoe/bnpkkFuZt/IZn5S3eRMvdtQ7R6M6dPVIa3qvFlr+hv6vDupCV75tSuolSXICO48IBkOFzpBXvfVZt1ab4TEklJ01mAYcR0mwXhZ+gJub8WV+zvEGuy1LlLxCJswXyP8dEjgBXrEaB+s89Kj3QRlJcUBAiG6t48Hzmm2vUAzk4pPf/ill9ic4STK8ZA+1qMlHOI860JLnHUqOD72kolO8VjuT5tT1iYJEjrZPwcYLb9Eqvsz6TSd6g4BcetZMWLG0l0xwZoihwUkDHgOvg43Deg1YPFnv7FeZ5f+ssbxatoD5FLdOJg16RmpMksk3+5A4JxPe/4cOVTSqdT5xdZP1Ce35Vm1jax5PngELkVDOBHbHM1b09bvENRz7XMYvQ8CAZH/EOdPLyn4dKgqXoYho/sgnNgb2haza/DonToPVPvDYUhIImedTsp5oArgOGY/p+Kdj9GoMjDexNXe2WHsNIdCnWOLT3VJRUOMFBuFlVe7u/yps8oZWCr4x4uMdlcp6zkf2m1sB8CSm84NpjeIos06tbKG8KrtFwlnspGp/+1FC42zMCKTpnWr6zH+tGAU2IAmMbbatJgjpeaP84H7kGNBGxkndyTQTBlycmcNKYHnUzYXUeyV29pk3FQJt55Onf6iylhkBUNOeIX0CnbZ5149CU7gy34uMpTeyC8jdgEYxEhzc2v3PE+TqLHbzmwJqyycFi1V6C1ua3yKbCUs58ufZYDJ6qSjgrY6ZTVqUe2njkWpNWOh+JVKlCbaO8vfHQU48Wy3sGV2msjCvzdf6huZkaCsPBfreZtVTZKryCKBhM6BluHl0PFJzGA3reNMqSdJrL9Ih0Mac1l/Sn7T50xPjJ/YNgZArrOicMP3PXbQSxV//0thPJNlHA/qqq5bt+YIxwe3/oyb2OeAq4VWuChpNH9NraTMsCImbxKfQGBzx/Syivz8fplGqKK8KWcXBaQwQd9bvTDpftF82wAxS7oNzZ3THmfEtotFOcZVepAx1Ct8uRPENOlfjz7JD+YLqv4sU3jTwP7eV5UBPd7KvOC0MD0A3OuuNIYvNcXFZ4knrO/7UjShd511uwqH1OPUFP5zVBBnIJSYVDLGHk4sFNthv+no7W9xBiNOHyhiF7awdWP9746OSmp3eiNhtbQloZgn+gVmg4sS7biuh5dgNbsNoFP2/6ICZA2bLV6Y0HKZiMK3kUhgZyZSwS5LRTWQvy0gDGEZ7UbOey7VVgWoYIXMBVLx2/LTq+2396O6CgsfgCAHZ702Ymvi0kcDGFkT30xkF8fURgKFVhTxZye6etsEi6J3zKQ4xrRdPBYO8HUX89he2R/DFgs1aaOSpHzog3qrUN1uzmTrBcWqLdSDZ9aeTqSuVu0rbeD5ucRPM++ajhCQvo6N1ZXem7ZbFC4/XdBo5/Fa12iLnuUScAmoIoaJGGLDUALU8yashI85yvOBZ9WuYakdTe8TquCJSc6MZ+FmuWiHGp3lzcvrE/pSwXARdGX1qh7WOeXTvu8XPb0JASzPhjD2QIBMUtfEyYmfMns7S88WyujcYGrKSxwBhrmWp3GOMxV/uydjguXwFhz7g/GTL56SPmaWCI0lnJBUKoOSh6obzYJTGbUK56VRpqqeRwpEH6+FKk+UuJSvve+wgnSpOZ/Ds/EhrZheP4AjhKCm6kD9jvxdppEWyLFpDAgNXzWJvuurYLMaSxDiKaib40oEjtN0IHUaTIyROCVIkXQAGKQhoMNE0KreA+h+8heZz7aeGh7327pM7wi+y8QkcDH6iAm5eAMbCPUJ9SyLHqwOl8WTmXJ04px8Fe1QxFev+tq6MjKjTxgsuxH3JIYcviGe5ee9Othif9DtE/8oDKMDDmpXj60o1MU6l6PH607Mu2Xc1CNEWK0glvWGRUb1l7FnySRXxnQH+tdqywSfYYhovhRQwNAPy1Bzg7RsgICu+BA1qN47hfPUfzKiv4MpWM3K3F43+M+Z5Q6DadrnM/nlRQVipllmXSJeo1raYs8ktnXteG82FhiVf6VfnTNRmiTS8SdRaoXvN8/+InmsZN/Y/vGLhTPWMwCB+qkZvb4EXJAtSmK7nO9M6HGEh3N9gCil/svW7LA0glOqPzUMUe7Xgo0ff3acDesM02MzWxVkXdR47HMhK8axge2r+ZgpdXftwO7jei7V0mfRjFU9lnWJp5XKm9J0xrdAp5pEBwFj1fFB6WDFMi04pn0o/+UuphVkABw/5EzHsw7j3eFP5fjNLw/b6abZUGd4HDcLmmCGLbxLLFP8OMWVQ0rTYk4o4dzAe4brlBdz82YfN0a6SIwUwYlOkzZahAMorZf1Qwf1O5b+DaCeUdevFXb+Wgua/uGM1o/9q8dv1FAz1yxyO4/3XYEN9jiEF6yQHpstNn/e8Qh7YELcQ5NCwYB3XkKMCTZyqrEcxfeQzbsBCXqBVVIN/DFGgZlghABYYGRUCIFzpEpA7Bh6oZtgjjPAalkMHCRVCzE3spJuNO6+KSOzq1MgjGMUE2zmOlhLQ1Ro8XggrxmHUCxHUgvpVaOLCzGCyiNyrNLWj10BLKRlZHXm1hG9TEm5yt8ECc7Nf8wUHEoAFFzFu4RYaOsY7I42TNDOnMKlud2AZpDANQ53C9yCVn0JQi9tZfBQlD7MpcG33fsHW/ZEKwhYqbZVAeVO6CxO1tftaCVdkzDaySxaN39Rh1ekMtm8YM76oP1+m13VMTMH4n+1gQxEqcH+7+3IY6nm8uTRh5+MsTMh/R/T95eyyVZAFE3M03/2vKMc0gHvwa+Xu3MzKbxdoVTYVy7oqKDCJGp/eIP+sbpvjE5NxCW/Rw/9e4va6J4/HEp107YysSGeOOHGLOJdYGNxoq1KeUQ9iz9CaMTZpQTWQZtNm5wunN8LUSkvMc468G7xZIzqUxN4cmaF5kdxwrcrgZtpHVqaBhKgMAJB4SPzJdbsDkKnG1TwM30bm1k2gYQOUZayIVPP5jtxXHm9bZ9EDzMExRIa4qiQsAes+YE+xABAxnLMic9yczk8dOIHbGPWK/QsF4C4ys5QddqnF02zvFXvQmPS7gfENb0/idIyFjbGvZF5leOwV6WcO99LWOVjDd0XdrrPWBJm7xAkQymrCKUPmmBUJGSEJJx95YM1d3ce1glelsEc8TfBYolm67WYl3mkrNp1jruU82stgsmRy7NiMTCW8N+VpXFvyPB4D7rOXddpMi8xCNKgwy9GQBQVK8wUEq0ZibFucfcsJTAuTXJ3ThOmlrtxc0CaT5XXz05udoLkKNW02AiXhAJTwXR5EuXxZD2nQRh1cSN5KI3TW9GuCSLuV8jJ/ccfDs4mkTBpSjkvwmw1dG/BLF/VI27Aup+1X4/P6O4xloctybl+r21f3wnH7cHp4lSf8KzhVxrnY+rr/WWSFHE8w8NMxm3gGogAYx3/tk42Q0Iaf6MdJwUYbyZrKWUtkBP90JzN1qbDeJo32nKKIAWoXLIjHXhnACi/5GbOUpC4kGO9CR9gkupUCuySVvtaauQS6wTk0ONkUFI83Zza036PXPpsCGyy3FailYExyOqoqxuleifnuYCpR7ZdoBR6caT2dyDhCTtBdaUxybIaVGD6WBMpx/7W/2P6izsOcXDT2hRXcL55TUxSQirtIsrQqGjazYYBaNRUb9D5n2SB3/FhPX55gAECTB+isDKXzc5399mJUtjnZ1cqLedRKrtNJNrz02oD81SGzxv0XTBB+mVWQYDlb2f4w2kDisxjrWpQwdYEuEIyn8wZaT6U3/KlHMcbBkwqeoLoRP6Ip+srQgszcQpyE6PC2K9+oAzTJW9WIkmndObnImB9pvvzWO+N0D68+ifnieqBxD8ePQYSxbd1UwFg49GUWqmajwRMAttKRfkixgKGl3bZKQpihdwVFpRS0+XkhoT+eWhI4pPDXLWVfnn5VgXmtkTS7tThunZ05fJAEezdQOvQMz3vFpLIVhoq9o6BPRBerZpZRjTWov6q8mzdMZdiKg4y3y7mN4wEgD6CaYh+YkJlhS6tEg0dNZa55hIBbs5aT6t0HQnMUUp5176cFk9n7EPNBiFFswAwzNVPpA4PJCQOoqO3TIAuvoIaU+G1GMt98/aeYYaTVgrUYb6Z/oWjcr10vpz86xz+KgIKMtjr8Re+xjKujn0mxj20cKEa6UOFG0hKmyNMawEhi/mNhMcYwQ7TYbtkdzE01amDz7uqQSINqHpEDLa2k7DL16UvWE+7oFMjaVbFkUoB18jrWhT2xwHCi7v5rrVhF/bAg82Ke+H7m+SbPI211iLElVTnwIcxPbmVX+qG5N6yVORaDr5B6Tg88ITia5Z5t+956PBuYG6zJ9EK6cs71shhEZPUWM7uBWhQAcLuJnRzaHsTNi8YK4KerlaAbaZZVZ4SS4SvXPUQhqN5P+Frsq1q4/XSWHMc5El6HOhqOm8X7xMdW174RimLQMcnFZDy7HUtclTfjHAqPw8hamDJraX6SiabMgIWy8tAswsF48LDPn43IIxPiC3/q1/FDrii2HXPm8PNuX3elCR1ipOs2przQKi9OpAowrPyHKEdJtxr+wt3GB424KN8Twfl7fJPv8Eo2t4H8bXhqYxSmXaCkz8Tlil2eYWp2TBJr/dN60GIY8P9TLpek1UUbUZgWVNx7LOcYdf2BLse7eIEQhKJmEuHfdo/5TReApKNVj09cSFy8G3qpTLMEeoguPXrqxEg+mBV1R1PU2Mufpvh7ty1CgJihDQ+FzXO6KRLGcJ5rEkfSBNVp2XygukKdtxTLfWKe3UHXNvJjH9+6jeDeaWh5SeFk3Ke/RhaAZP2F2ZjuoIFEKKv2qeMx/PeLdc69sC9m2tLYf5O+BW6DNG2jDV9SErxdDinhU2TP8rr+MziEG2lygj6HBrQmTpuQuGluNwXHlux7fSHFy7R59y1lxMJF52F81q0G0JdxFoW6qJbUglharnDUilUGCrWn3vemTGvn7tAxd6ZOPkD4ffIt2trOXQg3Hegy73YPtFI24BcPI1LZhYcQOt8Qolm+Lv5yLqgGAyAhRWx8Nj0GRhB5ijgKZFmitDuzWy2zgNTQsJRVebxMTAst3KALNA9sRLzmV5k0v5VP3EJyNDXpYnp3c/2Iyig8WtqV1A9o+N09qtx2ifB5+GZAIx3AMxTBcAxGuI5kYY8Y72bI+XfSuFdiAlTBARfxNH68nrYRgCtTEcEKpMrSCtuMAie6FIPR9qcjhOuJsvo4VBAgEINKc8koAZNEyJ5pIyWSputZ0fI93xwwD+SsVxS6G+zUUn3FTeMut/JjlSvDQOE4hQZQGq7Q3Y6bFujr1+IaxjrrklHqX/il5gq++TIc4/+MVrdTddy9Qn8vsHU0frJMIqBEtjlmcluSqrw2kmhI2aRvX6789/jwd71UHOdNFazyxmdsTeuz0ITJFMUZd/9xX8JGkfFgjYm6qulDswVFqyjnTgwvJmpOnPkQ9A2KgTDkFZFtOsbjzsy/GnDwTilHgHE4pgNB7Z5EzkbgHs5vdVowF8MH5zF513PxTeoC9uod8w81EInp01stXi4l1rgBeZhLgBMo1QOzQ94byUl8GD/CKDkxrNFmE+2Hu9DLWHP1F60jwQFqhK4UVd20TGPMuCu+QAh6epIm/xTSECm0rpGrRZxWGenvpAB4f5EfeybRJWyIgzbT8/EXyb3Q5wHnl9KsBpFNIkI77Gtms4b/BRvosKDRjcRrj2kJsjuHGi3T1pCwJorUdzKASKdTlqTIwcSB02QLO7tQGGT5wVKGObqOLC/KsjhcYmzgsc/c4Wke5apYBgWBUx6RrN7fgvwdb1qVOkpWh44LoV+w4Xba13/surwlwqXXrCXLZ1cKnK6wpVTI4I9HbQ/N9/q05kkKtaOySReYhV/obQQUG1PAQgLttt9ssvEHDfoFcTGf1JwU4X8MUNf2a9t6D1eQFr1PjvJX2D9CpzU8IKjUJoOkuhxpx9d94AoWAdpeWfwGgTP3d66Jdl+E20Ko5AWmBE17qJWT32m8GtlZNzlWGE8pKa0rcrAoHs49vihXPud6qZAcym5pQLd7nyJ74p4ANMEDIHyuZM0flqmUdg99ZJg+dSb1aN47FhhjQmIRJuhkzeSAWonr45SIpT6GoyYYSfi7qoLKbzCAu6bQ9Jsj8NRgjfl/jnQ3WzjAf15VV3T1kVj03XNKasCUnH6sP+3TGpD3b3BfENmXQlzm+IQqkRMatwTRiC2UAebrphojbDwSGS/XC4ppCM1dNYz3Zonco96nVYeMq2zxFM6TcBixP0L6vlXlLLA+Z3q+JvYZRhnwf9LmqbtI/o5iLoz/14t9bSrzNwGq7ltzgyDeAfPPTr7ZeRxtwDqNnt4fn7tn0WpsQXStUK3lZ4o5wwHydXiqsehkzFHaSmEzNEPPmzfHm9U1bMq2/lFIN8JGKCgD6GEIIJjLJIwUtcKayFmilzHHb/THCIX/+HRgKSJkZkw1OmoaTsrkKhSi3Gym6QUZDHfENgdK1YvaRYHAWAcZ1/6URCGSvd6suWh5lSXnsf6Rl87tOLMmmXQZfdd7UjtmWCO/sDoypS43UYjKPFWOwNgpG0Np+rQy5oQgggj3jqC8v1+J5R6DXTfHsee0/Fzfw/7qv4fi5nMxgENDQaylRnFWOKOHvLrZXtWyd1TEC41tToLCNNG4zlZ4P5et4VqsfP2/twk0b328tUHYdpw6STQOQVFRTyWs9l7pZMzIdpo3htNuLZlJUI3/NOsg97K4jNMB0dbZTUvss3Y18+4O/CZ0qsR9KFqcw7fQje+XHEUZupb1fZjLIWpN6OGiyBL7GmAqp3lbhY+vjlqhl9D64h1jcUFYCpUisnMU+1TmId8Wr/GXaudDhepbXDt+ZXBBTzd81R5lYrlTIyQmmsqF0zIn1oD5IOxufXV9v5XRZyImYFdbwW/sA8JGWk13jn6UPop3nR6+lzwVEuyqTf0GB+ecXlho1bBN43tV6WrTHdebNarbSXIw42gZi+CW2Xw8bQ3/DfziL7weiC7IpiX7nNsQWXhask3q5qoJe2e0WUvx50KNBMOEq/lzSEh4n43lyr2BeTe7GJKcP6eAhb0tWiyCGhd9Mfjoi7BvcSttGE6GtlnLAu1gSHXXjmQBRrvMELF65nEsX0VSOTtHH2bHYNecgTJ18xDmb/9aas+moJphKRd6DFLsmmWnfzCH93hXB61BsFJT/DgAT2iXWPW6xzc+PU3Rv2lt7JC2hFhsWIDxET00N4n2iniVVIED2t4Iruq0wjvYjHWJ61NbOrvOFu0oVaMW8YT8FBri7VRluDT4tTVkEFZCpkvtElaIAh5AcpGc55ZhES6FbveYZUSVEkmINtR6RVZAZhoxpH6lHi2velGQ2hFvR9FIGGia/LDjm8Nja8q+7ECqNnJNOjYwZYzXrJt7mTJhABOIzyOSqZxCtPY2/tNP5XgBxeUuj+bbSeT8rzZoYwqAAujzPFDBLGO3szndQDawDdpocKdFL+qvxRI5F0YAMG0ci4nVOIThHEdbeOmT2/91BeEFFRtw3SIHmesKZ5amweKSf3KCF3J2/idVA6NRTrHqft5oUL974c3OS9i5JhjuDymlnma9CtOJ1ol2XU0Gjg/fMuCG7aYzVy7Rh8IvTuGxKN7nWZ9o0LCGRHjy1Ry6tleB49adyQON22m8mXrF+2Vbae3p7U0LDiXHWpSRlP5+GSO826QIIFCqLON817eexLf3CA0rKqAbcEO4PqE+rMux6Rikz8YNQ5ZvFBBnBoD8WYl6y81/GXx1qu06LpITonxPEJJ1SrN3WiYqifcd4m7mtlrNh9g5gTPcREE7lypV5phKQ2+2o1VMpOuf/X7HfoCrsjhgx3UFKo14PTnf+0roRdf0UaM+Ao+iud0MJY2gn3TKcf3BWLML3eu+ltn5mTxVGV7ajbJV813DfLSrXk+nGaIyMGZAaZA5yIRu9hPikuvfxT6+T9avTj0cTo4MHyD+yzE5qlquQMJwyd1+g5ojjt/5xeAWfAZWVRhdxca838wdBjqkrlebHnZoXOUWqCIexxHRFZdkAgjlhGgeQw4N/ZLMAQ3Ap34vW7pNIp0n8JzZ+h6OTD9bqKGf0KMSRxID0k8sHv1hUNmtMnndzyin/PHXT7eQIOYgo7ASb1Qr3B9i4oDho+b/uD+HjkH2KjvW2Oa5jI6hIRhqGxAhjH4RpD4io5+D1RDudMrIhxoMxjiaCJOrbK9adp39/W7VYPQwiUa8cDIMmYL8nqQfKMGZwm3rpLN5oMuTo56CM/SJtCmvVrDsDDSQAWR+MyYJXsIl2x/eSg7TGLjLdOjguWcoE+e2o7oM71vaNaJjBfCalYgzBFUgpIz6cnW1/vI0+sM8liEjplmH7IPUEjTZZGhM+mgm4qFQLcStRIdjKKfcCvLzMeXaZgGfuZmKOwNAHxEntQjYF2TmNJxDeqXnp0c+sdgz4VWCqHud+wgKVKy1huCNCkrbeUMcbtu61SQCx7WqtbDzzoPyJIyGnHGsI8vCMHTOPGESTTBGDyTnuZHBrLSE+nutCZZkeQZrgvFi+kHSY5ZzGz7iisL3//npD1XDauCfZiesTZHbq0beKiIHJ1fQart5z+2yQY7F+4Y9gXnnw8uE05u5WZwAzHQZVmcloZ7Gs5kWPnrKNAQYmD2IvjP2HGO/mKQQPWsdIoKtTcqpERs7OK1GBgQ7BQ9YLShy6VxmxA0+5MEGdXOJHeZjO32M6/REB4dGtQmLcY8WljRvlly99Z8qRGsp5bSrU+rJzwLEV0nHKLj0GB8eUvhB+peshZC5LJlCltnq2B5UBH7l3K6a9RwDvZGeVHU426k0GRgUwIfTGPg67QFOUxMmbY7uTrOk5OsP4E/IMK60yXoSraeLBHGH1yN6SV5jj1bMswMzoxs2nlFFaCMpTV8wukakf2rK3Bvo+VqXi0tvhdNvpBhmP2OFqPqKv2FEhS/LoZ0dXcLTlM9tqP4fDrW9gsZfOpRmOfv8OVY3ib+76+XbMxMqsmjniavD5e8ax4mo4GgknlkONJv0Ut+X4xzvhiHJuDFQS/2pb9o1Wsh3272630kl2bA8SAw7E7BsBGJJoODBGO3Cnu56tVsVzDovmVtkDfTSU6fJg+3WYNzA7Akpks6eri1bZ/grJQ6085Ye8sySmVPkx5qpsrOtwiMIPe40mdPdwkDAKkwvsm7ENGLEUcMF935DHvgvnRIg07hQJl2Q8ePS/o+JVGvjsx3da6AYJtrJt0eFAcVit4Inm1nKEucNIKh6TtjTShng4+Kz4CyqpdfQjnmk6qubIBA9YyEKkAQHoocVufw2fQ4VE5gDnZ3vWv6Knxe0pJBRmdSacnxb1qUoSRtBs1cpa1Rp+R9em8PTQq+iVvq1oqw9GU7AYwnyF0rCMQCMqc14KdxicH2/KDMQ0TZ2f1Nh45DJ//A+HiRfVbVJXNZsHGMRLbX/yVNF1FsqOiJ43+vtV5DWTWQQc9iCAoJx75d9kh9AHyWGDJ7/utAnyHZOPN0/H6QSC3CQc0tHImIxYIkgoMOhnioYlcdaP2pF5uuJpRje/hYdXEY/d2fxQnAOB93VC5UVTsjIrdsFeaPXPppYodDsB5Z9oeuvzGR+JdAyKVrQPM8IZv0az8TjQJ3kOxNgjeLklx7GDkX0cMB51bdM8k5mICqwfwhOUPhgJ3CGHsj4QH9xTWPmm8ehq9tDeuMKnDfm1gECXWZzAMrxD+YEOXKKyPW20BqqjBoXH2xoJ6PCZWK7UsxH8OafQRkgWq+DFM9KAzAhVFhtGkubSKIuJLI60SDMYOUaAEF9ClJOAxy0ibyYA3M/UXH2jtIuSCnNL/Nj7w7mt68F/3Rx8JjzCqD8/I/W+VquPa2y29lv0PLbmiKiOo2UmFaQMukH0xHjDHx2F7kTLBsjgU8Uh6ZixpsVzEFZev50TrvNecVWVUzFPkNhX6EUMrkoWnokXjAdsR5+KZ1KMmNtxSn7tjmKZvAG55nMWNcjtk2a9+r62CWz+JOqd9gUqn+pfvfrOFnBGxB9CZXKbAKxZZRRKUwRa0yL3aaR5P/5ByrZoOvN7FSM1CpLbUHh6fBDLdSmfihNLJsgPjjizYxlE1dYJdISfjDPiW2Yedpvt0qTospDqiBMk+mATEz9D6gfgSTSLEmNfv3rAnKsm7FJY9p9BakbgAiFyCScLAXX4ac+2UQBdIOclOdTxqSNXbfApSr3TeHB30tROfG4iillac81C/ULPAhGIeGgl7BBOLA1Gz2nEa3EAW8ecBXydgTb2AGM1bU74bsa7Ce9iow2GXeuibehDcfAzxj074YjwCY050MjqLlTH4JLoVr2KgOECviMyUiLkt26sZY7OuyjwDMrVT5Scr8mcpS/RtwZTuwpvyn/5BfzUT2/27ewbzY4PgIh7I01veeDG+voc16yDJo3HnvEoKhBXI1NcwoorUXqub3tmW6bCfsx9anzwE9iwnt3PoRRIV5P+K80NDU9qAJ6pdXZTLU5tSS3/7jOHXAeH8R2TNHy/Hpp6DJpesATKtNYe+ozlnhLCr2NamvuSqtFB/ka9DXwAvHx8i0JfgvIVbDiDxvUU8/gae27RH/srjBiB/x2Cw/T3YS/FevCNUR3P/4jHCkA4ybkvElBk6NULMH6xmPIA/NWmFG1pAiV+UL3cQO1f8y2Mn/xjUWecM7Xi8MyhyIRvV1xfmbCxb38wFQFMSzPdBNRjKMB0XlANDXLbDa0/60WU/wr9TR53NDczPeHrWasQFwE1HLiT4AhYmL0JOc52IXgmTSojWmDCgSrG4HJYh7TvE+gjEjU2t/oxhvQEq2G7n1apym5Uq+4aC9/qptloSqPYkuRpA7u5GzstGSItwqX6skyfqaDGtcMW7GT02cbC1tWNNHqsfrnb83sBvck80owoBldeIVAINJYGnmvCf9IKKmYmvthG1cAahldl2YEHM60ohzaFpP2CUGadUPzW/xBNrEBaUY86/Sjd4bhyDyVwKW12blyiKN2GVryMBX4M8R/roThK0OzgqzibmFpRNttSDpLquy+am2iVXiO+P6GH8aFiPHIdeUmhh+uUz+2HVZYt3e9t99M1PsqvUPsUD5AsvH262PJs42uQtOxnjCj6gJvi1UambhbWTAXeF/heOU2JLT/Tui5iiCT0P3yGtnSd/BAHppuOe+t64We0tzZxwgORy1h6HvDuCnO2fGNnL2P48jaB55/n76+BB5RkT3d6nQzZPnpw3M3OXy5Ho181Yo+pzp0qiOBS+IXB6mXviyUtCtmOseKwF3jswCgMgz60tocea/mrxjD7aLvyYHNaTFnhxd2/ECRKLI+1zg83WuI1b55s9Wd1uzyjIyJcxXD1toCKKDkwBUtpVkOnr0/egqZGxrzqBTFqfyHWwtg5/szj/PzYtboZJwzCfr/ONiZBgkyE9tAwkC6CHmLAhFE2+NZ9YtIgqfoj7Myh/oCf8Y70Zp8Y4aTNr5iLFGXzfRc3X7BDJEgYJgVNvqfSlqwHAoBWQLXce/wwmCWJ3al8jXNKKjJpFP5SXewaz2E5L5I9n8g9+z0VXZ/AwHlPzMYrgs+k3c9D+IR3Ik/pC+V+uh4l9PjbVS5kCSnvIZIWXDn4E8AWyoPDpKAjqkEcw5flj50DJAwD5EZwHao46w6/4vJ2xo2ArqkLEHf30IYsAelNq+l7VBqac/1v8WSNJi+q7S7gfrdRaZSOdGau4k6FJy4z4quuj5Wi/+qbZ2fUIQTDT7LXcOahp+z6ogrMXRIyjbzs7Oql9xIIss05Ja33wfSq0Msa33Iz6pqwE3vivgvAFZJ/YrpIsc3/zYW7nDtStJScpoezNsQ37D1T718ONHKOG5CziGnvF0dpw4TFsm00odPLEt0D3BVM58i0AouMIJT/VL0a0h5YRnau0oAzm1SLXZ/BUpV4A3XSFQ1KAueuG/YfW1jp8CUB+lt4Hjc1+2UfuoiRoxKUllDqzUi4LOo1Hi89kdaMcPI24gZ7ik5IGczhMpiGH8JEeAB3ED4iqIvkgGAMXhkWRvUWVcHrM+9Hc7yYJD9XdV0CYKVZ8FkBXNsD377u7hr4ZDzz8BpLzclfS86lerBO5E8+ekd5EhxqP3/xLGeW6zO/Mh8xOX/R7JRe839vQa4bf+qixv4ZpV8q6wvJDP6EtDFjFgQB6sktKb84uVOiRZ7KqKSCYgetuB0GSqdXM/fVE/wipTW2a34he3m69vhaP+AZ89hUtneVEOK9DTGpSKmc90HjcCWwLPFKMv7mdKsO5DbbAeaE82fUBCVBb8ZGo8xCdrKobZdxEQCdZWUHaKfcCY4fa/mPs7eb6lOnPnUKheJ3BSfh5dxn9zbeUiku8dqQS+atzHgrKNkNNdQQrc+wlntmP/yHWGFYPoX6zBbAlt5JFX7b69w7NPnd9wTJvoQbCg/Y57GvjGW7oKPyweTCmACw78AMEuSbmbbDDGfIA3ce9M73+1iqhvXApjQz/JKt8iia1COe6VoUVtEIkMEmSr4s3fhgjGgOzpTaua1QZihSZxrtUjLsjrCJ7+1bCQCxy04BqrI2tg9KuiI6kqPR/xs6x0bh7h92VKkzVIE1L5OqNJ3DLpj6FFMjTXJINy0cYYVPk0bg7T4Rx/o/ks3N658j/Kw8hYI8ZC9eBH+jwJjK1ze7l6D9lTNiC4r5u8RGjoFdHJSCaBNXRYrMK0qnVnyfM0/yXYF9PTZix8QL4plkPN8WgglXpGXrNl6LdhhCxqP5sspp8Ob7EGzvZRBM2FDDbFGpyYlHv0k0XBfLEp/G/vN72Hh+hYIwGGkcRCsmgxpbH4kSctKdkXhih/b9D0LUEGx8+29kwkCxepqgPT4AcsjKAFHYzAS/cu2lVV3AhvORANWcJor7UtkOLS9cZtybtfmBx87R5HkEauJY/OSX8YvEGOgK2njENEeWBaTRc5qhKzemYtAqBqLgXqsGvN5CsgeEid0aI0jPqAUrzsobHiPmTc/Z1szw2QSb16w/yCdGKh1RTqO6vnkqq9qHbQWGSIVgw0kgzIDcoI+Bhhy4XNJyBIZ5SCppZ0Nc6N/DkHFhK2dzALuqz7QVEE5myji2VZ/Hgj+AXZDTItSCFoPy1sJ73Zyh8bg7LpNHVnaoz3NJmwrH0mvgPbSKm6BV6Zrx8wgnQm/Ng/aCMwmoi41ca7ELyj4/Fx9QB3OcV+exNTH95+g0HlKwuBCVnXntZQ/PqBXiM9XVpG1LR0C5QDWyhYZVtNEnlQLTQ4xwM1r72hi5oTdvJvD5j+UPsqLSkjEggjy7knaKtNq7cW6ApYPsOKz/MAT1pZ1N1EWkXy0mP3k4dmchU7QMtKZiCwJ4ZLe4R0ynV4eEnkmIHVKBJDAxonEZiRVaMVRgNjphmgmu788ZZGEyum192MsHR4eyKrtlydadwkwKeQMAOvkxvt1XbnTy/jBH57OPF5Ke39ERqkrRebZ5fA09Xex7oLTu7wzBp7vsd3E7/4y0gYuREoKFUmHFpamiMEcuVW6WIC8DcEev5+M5luF9k/bf755TKV/bMDtBeZZgTKEH5ykUXBwLJ84tD5K06aeXGEuLyRlwsp9wDxBUjQSGOOL6OODsKpM7Aq+StNLNoCAhNJ6iLPM4Ud1qAihxRHZLFqRzF18DG+xVcXxD2N7If6YzkBl9XpZr9KPgyn6wAGT/IYFkfptDhMCG36LAHLe2OBoWNrUHf7crMRIErCAioV8IWwDNBjDVV6E0CYK/peIuaiQGJBlVXN8x7H2H+UNAsLdImTjre5ldYxt+AcrCjWYtUarAk56uHdq5WPFP0CGw/hW0MV2bD0dxZhoxGq++DHF7geyhz+CYS/IRepbPVVqApPv0mDAdDBJ+O5tPUoUEbQ7xaB/d9t8VOM1CqSIu6jwf1XZglgrLDrWvhboEw39D19d9Rxk7a65prHBmWmYwbw2jwfcLPYrspUIeh2tCDgB71+mKN93EP19QPaPt+NyEdT8pVgU13CzX/3g4TWPfhU7Apwo63o72VSjs6eaRsFGK7/hV3mOOib+gKzeG2W9RsbSYb5E5bOKeeXGGDk4I/FvcL5tqa33jqO9AWmYrKwD66hlbYWCi+TD0E3XvGTvtg06Id10OVhMY1Jz95TG0yGZxaA0aH99A6GbW97GrlzgEGhgyf8M6BYL3ZIUaaRnBCKSk6URiIZgRocj8B39wf9QD2BDsX17Ur8Ddb93C53LbSEVqxwdshcpT9GEaSgl6T3yKRNO4j1UZY28gBIKbK0pq+/qTlNSkpNqjZiAg3UHjtNGOX6cexz5A1CcE4ZdC3WXu0dSuco0UX38UImw06aVBgjQdIm4zZaOq4xhv7o/jPzBV+UWtxcePlET+Hd5NhT+GZkEdgPqOk47PiJnowguvlvwZqHmDxUSMJgSV5atLDCEKWHpR2RE0WdmswlH9B/IwjKWPzLyLpFRXEeEOLIZmpv1OYgODnLGdQoL9zDjOaaN9rwTD6vFndEUG7hwy+R6YvpEY5tLcsB69qLroRz5LYFTi8JjM0AvNfnK+CsKKf5Nk/Beg0Udwt0l8rvOLdmsWD3jHsepKwaSpGJrkeKQfW4hZNLlOSMqg2kAMKOTVD4HK5IbzUMOEH9N06IXVCM2OjfaomJO2KLyuRpz17ruAjTSsaYV9fZUOpqv09sdEmII3oddEbHIYjp7DdyYe5dgPoXnbtH28QzVRHEPcDf1QA5FBvosVffvoMy+sFWzACih7MHLw05XRyQvZMZ2fmDP0hG/5oiy9wPADH9HiH6BXnUzW939oTovDSC+7KtUd3/xgpwlCZLXMH28i88ikIrBgTKHozSKP7eNltM6BIB9BLXFh2Xoss+cg/30s47L6PvizilJ42kqiKYk3xbJznHcW6DHJInpGbso5nMzuEZZT/qEEYUksTJhswla8RLhIy/IcOQbVF7yc4ZEq2STV79+sfQynqu8A/xzHexr+iv93CcKJoo7kCodz3t9uZVx+Bo0OFSaHR9pMHWJM+SHlmDa8l+rrZEXRxyxQ/MJ5nkdVYeuHReDprDttt0X47lpO+en014/6XZJJRQCYgBp7Bg4S5GXyWEsDKvF1jvjMkLT88MYiDU5qE6ahG/UYocQRvH24hppvHRbWg0ospOwnm0xoLgn3sAeBxf7HKcPVvWMsK+l2zuFcTB3VLEFgufdpDPpJ4uUr6RQqtkcDy32AmXoswQd42+4QOorHe76V1G4ALPDP2eDYB56uf8FP+6/SrxwSjN37eBG0qifDKRE9yD8fO1Xug3I5qyokoAFiS9Q6mvVDWdr+nemgyxzcKmUuytczpHbCh+H0OKOZp5yUjdUgAw9yAIcnC+nPrC718WNItyR8TmADpGjOpgCx6AgntYCZBcx5DSbHro2+6vuLlOsPPcIWkMep+FSdrpFE0AD0GWL/QbjDd5FslFIJk1Faj7TR07UYIVbFCG2KdwipSSigYA2XJRAs7fSERdLmwV4rtXce2sacW4YTOCep0+UrjGebqRESB+x8SQA3r4J3A+BGfAEeJ2Btji+cHS8tjjJf7LbS6SF1U4e7Euk9OkLdtQtOdMg8u+1lmDsCs1MRTkkk66HuNxHziH4i2MxLedBRKOWWLyaDRLtG2gYwaysQniEPm8EouxJNgaF4aZihpb+kNopDbXyy/x7f4nAluTQW+esQqAfkY399Zo4I36It2kMY77CtFKfbHU8lx99Wmwspgdd14VCW4P1ucWgQH4OW51JPfaE3OlozEOKXi0+PBZWIfll5ki2IokVZVnmcSxAQFdQRHVXocdnRSoDO+e7CRXQxPBqD5Jqj+Ru4+WDxgxZCQk288oXpGR5vo0iIcXcyxn9YszIRewwhzt8t7LARTEbZ/nfvOtvuPp2tjhesFYz9kNhvi2AznasnLbGO+LTtNO3e9qp8cN2oDh0aAVpI9C1otlxO1AX+UzyPPxZO/mAU+8qgFAQVRZYSxUooR8aJXDIKfW/rvgu7d8nNrK0GVWzBZaF1iFdTk0V1gvRNmFzjDmB3lEMEHQVTcN0WnpHViIC+9UEzzgRhhg4kGoLNnVtdwAf5XiLrAytj/XXtgxAu2Gg0Lsh2bsIHWRXfc7V3xyyyeT2a2itSDPPD+/1lNOBieFOssNH/dMvaHumg9+gRpcnKkrNWIcVSqXkXz4AoEShzxXrpKWETQQM/VZffeVBuueqU/jmRbp8Y12soQ0RDReyXF6f+OBmz+ngfxFsjegH4H5O3HiMkX1L0zH0BeE3jWKKwR5C57NmihFyC2KPbHFDFsX3Tq0cDFL2mdd3GlnfaOj3hvb/zTaTTSWCAV5FUbZHmkK0vgDVJZzS0nllKgkm5JFWJSH7+hzB1x1PPcXQQceSGaQb6lvmkkDybE5fMiNCzBQnIv5RvU2icZ3HpOe2YGf/OjZIvgW1pLwMn6iJ2rfLKCfmWmKt7WbT3/CjOk7LvGAoLNi5712Ug8GWX4rNSs81mFtWriSAmBkJX7xf5d6wqnGkLhpfWwG+HNAeUNPXdF1gDUrBnyWZCuhuLRI0kjz1mLei5LMtaN0Vu5jnvkY+AaA11hNOLwHayTGjpIw/7vvT2YKDsPEk3lbyFQqleGizMOWG+zhyhj2ZrbV7tKfuwQ==
        - #1:
          - type: tool-result
          - toolCallId: dASEhyQHL3BnaFDf
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: S0GoD3X0jyEAUTmR
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: JEBgQjx0ThMiyqe0
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 2AMbztzNpRDcIg9G
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: i3onq1aG28NmrIMA
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 74PnxBPle34MDv1u
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: DJDVhiSvgqqgz62U
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.