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
      - toolName: set-persona
      - args:
        - MinorCivNeutralBias: 3
        - Neediness: 6
        - Friendliness: 10
        - DenounceWillingness: 2
        - WorkWithWillingness: 9
        - WarmongerHate: 10
        - GuardedBias: 7
        - NeutralBias: 6
        - Forgiveness: 10
        - WonderCompetitiveness: 6
        - Chattiness: 9
        - WarBias: 1
        - Meanness: 1
        - MinorCivCompetitiveness: 5
        - FriendlyBias: 10
        - Rationale: Adjusting diplomatic persona to be highly peaceful and forgiving while minimizing denunciation willingness to foster peace negotiations with our neighbors. This is critical to end the global conflict and survive to secure our Cultural Victory.
        - Loyalty: 8
        - HostileBias: 1
        - MinorCivFriendlyBias: 10
        - AfraidBias: 5
        - DiplomaticBalance: 9
        - MinorCivWarBias: 1
        - DeceptiveBias: 4
        - MinorCivHostileBias: 1
        - Boldness: 3
        - VictoryCompetitiveness: 10
        - WorkAgainstWillingness: 5
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Setting extremely friendly relationship targets for The Inca to encourage our delegates and staff to accept peace as soon as possible, reducing their diplomatic victory threat and ending our military conflict.
        - Public: 50
        - TargetID: 0
        - Private: 50
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 50
        - TargetID: 1
        - Private: 50
        - Rationale: Fostering peace with America to alleviate severe war weariness and secure our eastern border.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 50
        - TargetID: 4
        - Public: 50
        - Rationale: Seeking peace with Morocco to halt their military pressure and avoid any further nuclear threats near our western borders.
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Maintaining friendly relations with Ethiopia to support a peaceful post-war global order.
        - TargetID: 5
        - Public: 50
        - Private: 50
    - #5:
      - toolName: set-research
      - args:
        - Technology: The Internet
        - Rationale: The Internet is our next tech priority as it provides a massive 50% Tourism boost to finalize our Cultural Victory, and unlocks Nanotechnology, Particle Physics, and Globalization.
    - #6:
      - toolName: set-policy
      - args:
        - Policy: Great Leap Forward
        - Rationale: Choosing Great Leap Forward as our next ideological tenet to obtain a free technology and significantly boost our science output, accelerating our path to the required late-game victory technologies.
    - #7:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Wonder: 100
          - Production: 100
          - Growth: 50
          - Espionage: 40
          - Diplomacy: 60
          - Gold: 80
          - CityDefense: 100
          - Culture: 100
          - Science: 80
          - GreatPeople: 60
          - Defense: 100
        - GrandStrategy: Culture
      - rationale: Shifting focus towards science, growth, and espionage to rapidly research the final technology required for the Citizen Earth Protocol, while maintaining maximum production and defense to protect our cities during global war.
  - tokens:
    - inputTokens: 19570
    - reasoningTokens: 8640
    - outputTokens: 592
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Pursuing Cultural Dominance**
            
            I'm currently focused on advancing our Cultural Victory. We're positioned as a strong contender, and I'm evaluating the most effective strategies to push this objective forward and maximize our progress.
            
            **Securing Cultural Supremacy**
            
            I'm diligently working towards securing a Cultural Victory. We're making excellent headway, with only The Inca remaining to become Influential. My immediate focus is confirming the existence and construction status of the Citizen Earth Protocol wonder.
            
            **Researching Key Technologies**
            
            My focus has shifted to identifying the precise technology that unlocks the Citizen Earth Protocol wonder. I've reviewed the economic briefing, which points to Mecca as the sole city capable of its rapid construction. Now, I'm verifying which of our available research paths, particularly "The Internet," will grant access to this crucial late-game technology.
            
            **Finalizing Global Influence**
            
            My latest analysis confirms that completing "The Internet" research will not only boost our tourism significantly, accelerating our path to influencing the remaining civilizations, but it also unlocks crucial advancements. Once all major civs are influenced, the Citizen Earth Protocol will be our sole remaining hurdle.
            
            **Prioritizing Internet Research**
            
            I'm ensuring "The Internet" remains our next research target after the current "Satellites" project concludes. I've confirmed this is indeed the intended path, and I'm evaluating if any urgent strategic shifts necessitate altering this selection from the available options.
            
            **Evaluating Policy Options**
            
            My current thought process is assessing available policy options to complement our research into "The Internet." I'm particularly keen on "Great Leap Forward" due to its immediate technology gain, which could further accelerate our progress.
            
            **Assessing Global Conflicts**
            
            I'm currently re-evaluating our position amidst the widespread global conflict. While "Great Leap Forward" remains a strong policy choice for accelerating research, the ongoing wars with America, Ethiopia, and Morocco necessitate a careful review of our military status, especially after being nuked by Morocco.
            
            **Rebalancing Military Posture**
            
            I'm recalibrating our defensive priorities given the widespread conflicts. Our heavy focus on defense and city defense flavors remains, but I'm assessing if specific tactical adjustments are needed in key cities like Tenochtitlan against the current Moroccan threat.
            
            **Analyzing Defensive Imperatives**
            
            My immediate focus is on analyzing our current defensive situation, particularly the heavy American pressure on Damascus and naval superiority in Baghdad Sea. I'm weighing whether to prioritize mobilization or offense against our current defensive posture, remembering our proximity to cultural victory.
            
            **Confirming Ideological Requirements**
            
            I'm verifying our adopted Order tenets to ensure we meet the ideological requirements for a Cultural Victory. I need to confirm if we have secured two Tier 3 tenets, specifically looking at "Cultural Revolution" and its level.
            
            **Securing Tier 3 Tenets**
            
            I've confirmed that "Cultural Revolution" is a Tier 3 tenet. This, combined with "Dictatorship of the Proletariat" and "Workers' Faculties," means I've now met the ideological prerequisite for a Cultural Victory. My next step is to check the Citizen Earth Protocol wonder completion.
            
            **Verifying Ideological Tenets**
            
            I'm reassessing our current Order tenets to confirm we meet the Cultural Victory ideological requirements. I'm specifically checking for Tier 3 tenets, and it appears I may have misidentified "Cultural Revolution" as Tier 3. I need to verify this and explore if any other Order tenets qualify.
            
            **Adopting Correct Tenets**
            
            I'm re-evaluating our Order tenets to meet the Cultural Victory requirements. It appears I incorrectly identified "Cultural Revolution" as Tier 3. I need to confirm the actual Tier 3 tenets available and ensure we adopt two. The absence of Tier 3 options requires further investigation into unlocking them, potentially by adopting more Tier 2 policies like "Great Leap Forward."
            
            **Seeking Diplomatic Resolutions**
            
            My current focus is on navigating the ongoing conflicts. I'm exploring avenues for peace with America, Ethiopia, and Morocco, specifically examining potential shifts in our diplomatic stance or policy choices that might facilitate such resolutions.
            
            **Negotiating Peace Treaties**
            
            I'm actively seeking diplomatic resolutions to our ongoing conflicts. I'm analyzing war weariness levels and current relationships with America and Morocco, aiming to leverage these factors to secure favorable peace terms.
            
            **Improving Diplomatic Standing**
            
            I am adjusting our diplomatic standing with key civilizations to facilitate peace negotiations. My goal is to leverage relationship modifiers to make our peace offers more appealing, especially with America, Morocco, and the formidable Inca, to clear the path for a swift Cultural Victory and the completion of the Citizen Earth Protocol.
            
            **Adjusting Diplomatic Persona**
            
            I'm fine-tuning our persona to maximize diplomatic success. I'm increasing friendliness and reducing any inclination to denounce others, ensuring our leader's inherent peaceful nature is fully leveraged to secure the necessary peace treaties and advance our Cultural Victory.
            
            **Preventing Diplomatic Collapse**
            
            I'm analyzing the World Congress vote, which is imminent. The Inca's overwhelming delegate count (48, 111% of victory threshold) threatens an immediate Diplomatic Victory if "Global Hegemony" passes. I must adjust our diplomatic settings to prevent denouncements and maximize friendliness to counter this, while also preparing to vote against their proposal.
            
            **Preventing Diplomatic Victory**
            
            My immediate concern is the Inca's impending Diplomatic Victory via "Global Hegemony" in the World Congress. I've identified that their delegate count exceeds the victory threshold. My priority is to prevent this by ensuring "Decolonization" passes, as it will significantly reduce their delegate support from city-states.
            
            **Countering Diplomatic Aggression**
            
            I'm working to counteract the Inca's overwhelming delegate support in the World Congress. My strategy involves voting for "Decolonization" to weaken their city-state alliances and prevent their imminent Diplomatic Victory. I'm also scrutinizing their active resolutions for potential vulnerabilities.
            
            **Analyzing Delegate Impact**
            
            I've discovered that while "Decolonization" would reset influence for most city-states, the Inca's permanent alliances remain untouched. However, crucial city-states like Vatican City, currently boasting high Inca influence, would be significantly impacted, dramatically reducing their delegate count and bolstering our chances against an imminent Diplomatic Victory.
            
            **Securing Delegate Influence**
            
            I'm analyzing the World Congress voting dynamics. While I can't secure more delegates through alliances due to ongoing wars with city-states, I'm investigating if peace treaties with major civilizations will automatically resolve our city-state conflicts, thus granting me more delegate influence to counter the Inca.
            
            **Forging Alliances and Peace**
            
            I am now prioritizing peace with major civilizations like the Inca and America. My aim is to leverage positive relationships to secure alliances with their allied city-states, which will directly increase my delegate influence in the World Congress and prevent the Inca from achieving a Diplomatic Victory.
            
            **Confirming Ideological Tenets**
            
            I am verifying our current Order tenets to ensure they align with Cultural Victory prerequisites. My primary focus is confirming the existence of two Tier 3 tenets. I need to double-check "Cultural Revolution" and identify any other qualifying options should it not meet the criteria.
            
            **Unlocking Ideological Paths**
            
            I'm currently investigating why Tier 3 Order tenets aren't appearing as options. My initial belief was that I simply needed to adopt more Tier 2 policies, but upon reviewing the available options, none are Tier 3. I suspect there might be an unstated prerequisite or a need to unlock them through specific game events or technologies, prompting a deeper dive into the Order tree's structure.
            
            **Confirming Ideological Requirements**
            
            I'm double-checking our adopted Order tenets to fulfill the Cultural Victory prerequisites. I need to verify we possess two Tier 3 tenets, specifically re-examining "Cultural Revolution" and identifying any other potential candidates to ensure ideological alignment for victory.
            
            **Adopting Essential Policies**
            
            I'm prioritizing "Great Leap Forward" as my next policy, as the free technology it provides is critical for accelerating my research towards "The Internet." I am continuing to examine other Level 2 policies like "Five-Year Plan" for potential benefits, but the immediate technological boost from "Great Leap Forward" is the most compelling option.
            
            **Adjusting Strategy Focus**
            
            My current thoughts are centered on refining our overall strategy. I'm analyzing our existing flavors, which are heavily skewed towards defense, to see if a pivot is needed to better support wonder production, culture, and science, crucial for securing "The Internet" and ultimately the Citizen Earth Protocol.
            
            **Optimizing Victory Strategy**
            
            I'm currently re-evaluating our strategic flavors to better align with victory conditions. My focus is on boosting science and growth, while also reinforcing our defenses and espionage to protect our technological advancements and secure a win, particularly in light of late-game technology requirements.
            
            **Adjusting Diplomatic and Flavor Settings**
            
            I'm focusing on fine-tuning our diplomatic approach and strategic flavors. This includes adjusting friendliness towards key civilizations, setting specific relationship values with The Inca, America, Morocco, and Ethiopia, and updating our overall flavors to prioritize science, growth, and defense while also boosting wonder and culture production. Additionally, I'm confirming our research target is "The Internet" and the next policy adoption is "Great Leap Forward."
            
            **Confirming Policy Selection**
            
            I am confirming the exact nomenclature for game actions. Specifically, I am verifying whether to use "Great Leap Forward" or the full designation "Great Leap Forward (Level 2 Tenet of Ideology Order)" when setting the next policy. This precision is critical for ensuring accurate execution of our strategy.
            
            **Executing Diplomatic Adjustments**
            
            I'm confirming the precise settings for our diplomatic persona, ensuring maximum friendliness and minimal denouncement to facilitate peace treaties. Simultaneously, I'm fine-tuning our strategic flavors to heavily emphasize science, culture, and wonder production, directly supporting our path to achieving "The Internet" and the Citizen Earth Protocol. The execution of these parameter adjustments is now underway.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: skHofl766LTkGLm3
          - toolName: set-persona
          - input:
            - MinorCivNeutralBias: 3
            - Neediness: 6
            - Friendliness: 10
            - DenounceWillingness: 2
            - WorkWithWillingness: 9
            - WarmongerHate: 10
            - GuardedBias: 7
            - NeutralBias: 6
            - Forgiveness: 10
            - WonderCompetitiveness: 6
            - Chattiness: 9
            - WarBias: 1
            - Meanness: 1
            - MinorCivCompetitiveness: 5
            - FriendlyBias: 10
            - Rationale: Adjusting diplomatic persona to be highly peaceful and forgiving while minimizing denunciation willingness to foster peace negotiations with our neighbors. This is critical to end the global conflict and survive to secure our Cultural Victory.
            - Loyalty: 8
            - HostileBias: 1
            - MinorCivFriendlyBias: 10
            - AfraidBias: 5
            - DiplomaticBalance: 9
            - MinorCivWarBias: 1
            - DeceptiveBias: 4
            - MinorCivHostileBias: 1
            - Boldness: 3
            - VictoryCompetitiveness: 10
            - WorkAgainstWillingness: 5
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: YfsOP0GitPFCZtYF
          - toolName: set-relationship
          - input:
            - Rationale: Setting extremely friendly relationship targets for The Inca to encourage our delegates and staff to accept peace as soon as possible, reducing their diplomatic victory threat and ending our military conflict.
            - Public: 50
            - TargetID: 0
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Ro9bXANMU6g3NfCA
          - toolName: set-relationship
          - input:
            - Public: 50
            - TargetID: 1
            - Private: 50
            - Rationale: Fostering peace with America to alleviate severe war weariness and secure our eastern border.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: oeNQ8HjfYS1T3Hkr
          - toolName: set-relationship
          - input:
            - Private: 50
            - TargetID: 4
            - Public: 50
            - Rationale: Seeking peace with Morocco to halt their military pressure and avoid any further nuclear threats near our western borders.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: WkAzg6jA8LlJRmL9
          - toolName: set-relationship
          - input:
            - Rationale: Maintaining friendly relations with Ethiopia to support a peaceful post-war global order.
            - TargetID: 5
            - Public: 50
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 9q5BQw5pY6BgIHJ7
          - toolName: set-research
          - input:
            - Technology: The Internet
            - Rationale: The Internet is our next tech priority as it provides a massive 50% Tourism boost to finalize our Cultural Victory, and unlocks Nanotechnology, Particle Physics, and Globalization.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: rmMidjbU5tF9x2Eb
          - toolName: set-policy
          - input:
            - Policy: Great Leap Forward
            - Rationale: Choosing Great Leap Forward as our next ideological tenet to obtain a free technology and significantly boost our science output, accelerating our path to the required late-game victory technologies.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: XJiB5mLxFNqFP3qa
          - toolName: set-flavors
          - input:
            - Flavors:
              - Wonder: 100
              - Production: 100
              - Growth: 50
              - Espionage: 40
              - Diplomacy: 60
              - Gold: 80
              - CityDefense: 100
              - Culture: 100
              - Science: 80
              - GreatPeople: 60
              - Defense: 100
            - Rationale: Shifting focus towards science, growth, and espionage to rapidly research the final technology required for the Citizen Earth Protocol, while maintaining maximum production and defense to protect our cities during global war.
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: skHofl766LTkGLm3
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: YfsOP0GitPFCZtYF
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Ro9bXANMU6g3NfCA
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: oeNQ8HjfYS1T3Hkr
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: WkAzg6jA8LlJRmL9
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 9q5BQw5pY6BgIHJ7
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: rmMidjbU5tF9x2Eb
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: XJiB5mLxFNqFP3qa
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.