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
      - toolName: set-research
      - args:
        - Technology: Alternative Energy
        - Rationale: With 100% cultural influence on all civilizations expected in 2 turns, the tourism boost from The Internet is redundant. We switch to Alternative Energy to unlock Solar Plants (further boosting Mecca's production) and progress toward Robotics and Future Tech, which are required for the Citizen Earth Protocol.
    - #1:
      - toolName: set-relationship
      - args:
        - Private: 35
        - Public: 40
        - Rationale: Increase diplomatic stance to encourage the AI to accept peace. Ending the war with America will free up military supply and allow us to focus entirely on science and wonder construction.
        - TargetID: 1
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 65
        - Rationale: Substantially increase diplomatic relations to push for peace. Morocco has a significant force near Tenochtitlan and previously nuked us; securing peace is vital to protect our borders and ensure survival during the final research push.
        - Public: 70
        - TargetID: 4
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 25
        - Rationale: Increase diplomatic relations to encourage peace. If we can secure peace with The Inca, we will automatically end wars with their 7 city-state allies. This is our best chance to compete for their influence and prevent an Incan Diplomatic Victory in the World Congress.
        - Public: 30
        - TargetID: 0
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 0
          - Culture: 30
          - Wonder: 100
          - Defense: 100
          - Science: 100
          - Production: 100
          - Gold: 60
          - Diplomacy: 50
          - CityDefense: 100
          - Infrastructure: 30
          - GreatPeople: 50
          - Mobilization: 0
          - Growth: 30
        - GrandStrategy: Culture
      - rationale: Since we are 2 turns away from influencing everyone, tourism is no longer a bottleneck. We maximize Science (100) to speed up our path to Future Tech, keep Production and Wonder at 100 to prepare Mecca for the Citizen Earth Protocol, and maintain maximum Defense (100) to survive the ongoing wars.
  - tokens:
    - inputTokens: 21720
    - reasoningTokens: 10298
    - outputTokens: 408
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Conditions**
            
            My focus is on our cultural victory progress. At turn 420, I'm assessing our standing with America and Ethiopia, who are currently influential. I need to review their influence levels further to strategize our next moves.
            
            **Achieving Victory Now**
            
            I've confirmed we are on the brink of a cultural victory, needing just two more turns to influence the Inca, bringing our influential civilizations to four. However, I've just realized an additional requirement: building the Citizen Earth Protocol wonder, which necessitates Future Tech and a considerable build time.
            
            **Researching Required Technologies**
            
            I'm currently focused on the prerequisites for the Citizen Earth Protocol. It seems Future Tech is the key, but my research indicates Robotics or Nanotechnology might be the intermediate step in Vox Populi. I'm double-checking our current tech tree and queued research, as our science output and remaining technologies seem insufficient.
            
            **Researching Pathways**
            
            I am now examining the specific technological prerequisites for "Future Tech," as "Robotics" appears to be a key intermediate. I am verifying our current research queue, particularly our progress with "The Internet," and considering the implications of a potential policy adoption in 19 turns to accelerate our progress.
            
            **Evaluating Technology Choices**
            
            I'm currently weighing the benefits of "Alternative Energy" versus "The Internet" for our research. With only two turns left to influence the Inca and achieve our fourth influential civilization, I'm confirming the victory conditions, specifically the need for the Citizen Earth Protocol wonder. I'm also examining our Order ideology for Tier 3 tenets.
            
            **Reviewing Order Tenets**
            
            I'm currently analyzing the Order ideology's tenets, specifically identifying potential Tier 3 options. It appears the provided list deviates from standard Vox Populi Tier 3 tenets, prompting a re-evaluation of our current policy choices and their impact on our victory path.
            
            **Unlocking Further Policies**
            
            I'm currently investigating why the Level 3 tenets aren't appearing in the policy list. I suspect we need to adopt more Level 2 tenets first or that the available options are contingent on further advancements. This is causing a delay in strategizing our ideology.
            
            **Confirming Victory Logic**
            
            I'm re-evaluating our tourism strategy. If we've already achieved influence with all major civilizations, then further tourism boosts are indeed redundant. My current focus is therefore on the quickest path to Future Tech and the Citizen Earth Protocol, analyzing the direct technological routes available.
            
            **Determining Optimal Research Path**
            
            I'm currently reassessing our research priorities. My analysis indicates that "The Internet" unlocks crucial high-tier technologies like Nanotechnology and Globalization. However, I'm also considering if "Alternative Energy" might be a more direct route towards the prerequisites for Future Tech, especially given the need for all other technologies to be researched first.
            
            **Optimizing Production Flow**
            
            I'm now focusing on Mecca's production queue. Once the Heavy Bomber is complete in two turns, I'll re-evaluate its next build. The Citizen Earth Protocol is still unavailable due to the Future Tech prerequisite. I'm investigating our science output and flavor to see if accelerating research beyond the current 13 turns for Satellites is feasible or necessary.
            
            **Boosting Science Output**
            
            I've realized that increasing our Science flavor will directly boost our per-turn science generation, significantly reducing the research time for Satellites and subsequent technologies. This acceleration is crucial, as we'll achieve full influence in two turns, leaving Future Tech and the Citizen Earth Protocol as our sole remaining obstacles.
            
            **Adjusting Flavor Priorities**
            
            I'm re-evaluating our flavor distribution. I believe we can safely decrease Culture and Gold flavors, reallocating those points to maximize Science and Production. This shift will accelerate our progress towards critical technologies and wonder construction.
            
            **Accelerating Future Technologies**
            
            I'm now reassessing our research queue. While "The Internet" remains a priority for unlocking high-tier techs, I'm exploring if "Alternative Energy" presents a more direct, albeit potentially slower, path to the prerequisites for Future Tech, especially considering the need to research all other technologies first.
            
            **Prioritizing Research Now**
            
            I'm weighing whether "Alternative Energy" or "The Internet" is the more efficient path to "Future Tech." Since all other technologies must be researched before "Future Tech," the intermediate steps and potential production bonuses from "Alternative Energy" now seem more beneficial, especially given Mecca's already high production output.
            
            **Adopting Crucial Policies**
            
            I've confirmed "Great Leap Forward" is queued, a Level 2 Order tenet offering a free technology and significant science bonuses. This is excellent. My current focus is on verifying our ongoing wars and understanding their implications, as I've just discovered we are at war with every major civilization.
            
            **Assessing Global Conflicts**
            
            I'm currently reassessing our geopolitical situation. It appears we are embroiled in a global war with every major civilization, making new foreign connections and peace highly improbable due to extreme negative modifiers, including ideological differences. My priority now shifts to defending ourselves while we continue to advance our research.
            
            **Defending Against Ideological Shift**
            
            I'm currently assessing the fallout from the impending "World Ideology: Freedom" vote. With the Inca, Morocco, and America heavily aligned, the proposal is guaranteed to pass. My immediate concern is the significant impact this will have on our own ideological standing and the votes we'll gain, as our existing friendships with Novgorod and alliance with Dublin offer limited protection.
            
            **Preventing Diplomatic Defeat**
            
            I'm alarmed to realize the Inca are on the cusp of a Diplomatic Victory in just 7 turns, holding 48 delegates against the required 43. My immediate focus is on disrupting their delegate count before the World Congress votes on "Global Hegemony."
            
            **Disrupting Inca Delegates**
            
            I'm shocked to realize the Inca are poised for a Diplomatic Victory in just 7 turns, holding 48 delegates. I'm analyzing their city-state alliances, noting they have major alliances with Shedet, Palatium, Belgrade, Ife, Vatican City, Nippur, and Yerevan, which grants them significant influence.
            
            **Disrupting Diplomatic Victory Path**
            
            I've identified a critical flaw in the Inca's impending diplomatic victory. My proposal, "Decolonization," if passed, will reset most city-state influences to 50, significantly undermining their delegate count. I am now analyzing which of their city-state alliances will be unaffected due to permanent ally status.
            
            **Securing Victory Through Diplomacy**
            
            I'm assessing our options to pass "Decolonization," which is key to disrupting the Inca's Diplomatic Victory. While we're at war with everyone, I'm exploring the possibility of securing peace with Ethiopia and Morocco to gain their votes.
            
            **Resolving Diplomatic Deadlock**
            
            I'm currently trapped in a diplomatic deadlock. While I identified "Decolonization" as a way to disrupt the Inca's victory, our ongoing wars with nearly all major civilizations and their allied city-states mean we cannot directly influence or negotiate for votes. This prevents us from securing peace or purchasing necessary city-state alliances to pass our proposal.
            
            **Analyzing World Leader Votes**
            
            I'm currently dissecting how the World Leader vote functions in Vox Populi, specifically in relation to preventing the Inca's Diplomatic Victory. My focus is on how votes are cast for oneself or others and whether our own delegate count can successfully block their victory, even if they have a majority.
            
            **Analyzing Diplomatic Blockade**
            
            I'm currently assessing how to break the diplomatic deadlock preventing us from voting for "Decolonization." Our ongoing global conflicts make direct negotiation for votes impossible. I'm now investigating whether achieving peace with specific, less hostile civilizations, like Morocco, could be a viable, albeit challenging, first step to securing the necessary support.
            
            **Researching Wonder Requirements**
            
            I'm re-evaluating our path to victory. While the Inca's Diplomatic Victory is a pressing concern, I've realized we can achieve Cultural Victory in two turns by becoming influential with them, provided we have the Citizen Earth Protocol. This wonder, however, remains inaccessible due to the Future Tech requirement.
            
            **Disrupting Diplomatic Victory Path**
            
            I've identified a critical flaw in the Inca's impending diplomatic victory. My proposal, "Decolonization," if passed, will reset most city-state influences to 50, significantly undermining their delegate count. I am now analyzing which of their city-state alliances will be unaffected due to permanent ally status.
            
            **Disrupting Inca Delegates**
            
            I'm shocked to realize the Inca are poised for a Diplomatic Victory in just 7 turns, holding 48 delegates. I'm analyzing their city-state alliances, noting they have major alliances with Shedet, Palatium, Belgrade, Ife, Vatican City, Nippur, and Yerevan, which grants them significant influence.
            
            **Preventing Diplomatic Defeat**
            
            I'm alarmed to realize the Inca are on the cusp of a Diplomatic Victory in just 7 turns, holding 48 delegates against the required 43. My immediate focus is on disrupting their delegate count before the World Congress votes on "Global Hegemony."
            
            **Analyzing World Leader Votes**
            
            I'm currently dissecting how the World Leader vote functions in Vox Populi, specifically in relation to preventing the Inca's Diplomatic Victory. My focus is on how votes are cast for oneself or others and whether our own delegate count can successfully block their victory, even if they have a majority.
            
            **Analyzing Diplomatic Blockade**
            
            I'm currently assessing how to break the diplomatic deadlock preventing us from voting for "Decolonization." Our ongoing global conflicts make direct negotiation for votes impossible. I'm now investigating whether achieving peace with specific, less hostile civilizations, like Morocco, could be a viable, albeit challenging, first step to securing the necessary support.
            
            **Securing Victory Through Diplomacy**
            
            I'm assessing our options to pass "Decolonization," which is key to disrupting the Inca's Diplomatic Victory. While we're at war with everyone, I'm exploring the possibility of securing peace with Ethiopia and Morocco to gain their votes.
            
            **Resolving Diplomatic Deadlock**
            
            I'm currently trapped in a diplomatic deadlock. While I identified "Decolonization" as a way to disrupt the Inca's victory, our ongoing wars with nearly all major civilizations and their allied city-states mean we cannot directly influence or negotiate for votes. This prevents us from securing peace or purchasing necessary city-state alliances to pass our proposal.
            
            **Assessing Global Conflicts**
            
            I'm currently reassessing our geopolitical situation. It appears we are embroiled in a global war with every major civilization, making new foreign connections and peace highly improbable due to extreme negative modifiers, including ideological differences. My priority now shifts to defending ourselves while we continue to advance our research.
            
            **Defending Against Ideological Shift**
            
            I'm currently assessing the fallout from the impending "World Ideology: Freedom" vote. With the Inca, Morocco, and America heavily aligned, the proposal is guaranteed to pass. My immediate concern is the significant impact this will have on our own ideological standing and the votes we'll gain, as our existing friendships with Novgorod and alliance with Dublin offer limited protection.
            
            **Adopting Crucial Policies**
            
            I've confirmed "Great Leap Forward" is queued, a Level 2 Order tenet offering a free technology and significant science bonuses. This is excellent. My current focus is on verifying our ongoing wars and understanding their implications, as I've just discovered we are at war with every major civilization.
            
            **Prioritizing Research Now**
            
            I'm weighing whether "Alternative Energy" or "The Internet" is the more efficient path to "Future Tech." Since all other technologies must be researched before "Future Tech," the intermediate steps and potential production bonuses from "Alternative Energy" now seem more beneficial, especially given Mecca's already high production output.
            
            **Accelerating Future Technologies**
            
            I'm now reassessing our research queue. While "The Internet" remains a priority for unlocking high-tier techs, I'm exploring if "Alternative Energy" presents a more direct, albeit potentially slower, path to the prerequisites for Future Tech, especially considering the need to research all other technologies first.
            
            **Adjusting Flavor Priorities**
            
            I'm re-evaluating our flavor distribution. I believe we can safely decrease Culture and Gold flavors, reallocating those points to maximize Science and Production. This shift will accelerate our progress towards critical technologies and wonder construction.
            
            **Boosting Science Output**
            
            I've realized that increasing our Science flavor will directly boost our per-turn science generation, significantly reducing the research time for Satellites and subsequent technologies. This acceleration is crucial, as we'll achieve full influence in two turns, leaving Future Tech and the Citizen Earth Protocol as our sole remaining obstacles.
            
            **Optimizing Production Flow**
            
            I'm now focusing on Mecca's production queue. Once the Heavy Bomber is complete in two turns, I'll re-evaluate its next build. The Citizen Earth Protocol is still unavailable due to the Future Tech prerequisite. I'm investigating our science output and flavor to see if accelerating research beyond the current 13 turns for Satellites is feasible or necessary.
            
            **Determining Optimal Research Path**
            
            I'm currently reassessing our research priorities. My analysis indicates that "The Internet" unlocks crucial high-tier technologies like Nanotechnology and Globalization. However, I'm also considering if "Alternative Energy" might be a more direct route towards the prerequisites for Future Tech, especially given the need for all other technologies to be researched first.
            
            **Confirming Victory Logic**
            
            I'm re-evaluating our tourism strategy. If we've already achieved influence with all major civilizations, then further tourism boosts are indeed redundant. My current focus is therefore on the quickest path to Future Tech and the Citizen Earth Protocol, analyzing the direct technological routes available.
            
            **Unlocking Further Policies**
            
            I'm currently investigating why the Level 3 tenets aren't appearing in the policy list. I suspect we need to adopt more Level 2 tenets first or that the available options are contingent on further advancements. This is causing a delay in strategizing our ideology.
            
            **Reviewing Order Tenets**
            
            I'm currently analyzing the Order ideology's tenets, specifically identifying potential Tier 3 options. It appears the provided list deviates from standard Vox Populi Tier 3 tenets, prompting a re-evaluation of our current policy choices and their impact on our victory path.
            
            **Evaluating Technology Choices**
            
            I'm currently weighing the benefits of "Alternative Energy" versus "The Internet" for our research. With only two turns left to influence the Inca and achieve our fourth influential civilization, I'm confirming the victory conditions, specifically the need for the Citizen Earth Protocol wonder. I'm also examining our Order ideology for Tier 3 tenets.
            
            **Researching Pathways**
            
            I am now examining the specific technological prerequisites for "Future Tech," as "Robotics" appears to be a key intermediate. I am verifying our current research queue, particularly our progress with "The Internet," and considering the implications of a potential policy adoption in 19 turns to accelerate our progress.
            
            **Researching Required Technologies**
            
            I'm currently focused on the prerequisites for the Citizen Earth Protocol. It seems Future Tech is the key, but my research indicates Robotics or Nanotechnology might be the intermediate step in Vox Populi. I'm double-checking our current tech tree and queued research, as our science output and remaining technologies seem insufficient.
            
            **Achieving Victory Now**
            
            I've confirmed we are on the brink of a cultural victory, needing just two more turns to influence the Inca, bringing our influential civilizations to four. However, I've just realized an additional requirement: building the Citizen Earth Protocol wonder, which necessitates Future Tech and a considerable build time.
            
            **Analyzing Victory Conditions**
            
            My focus is on our cultural victory progress. At turn 420, I'm assessing our standing with America and Ethiopia, who are currently influential. I need to review their influence levels further to strategize our next moves.
            
            **Disrupting Diplomatic Victory Path**
            
            I've discovered that while the Inca are close to a Diplomatic Victory, passing "Decolonization" would cripple their delegate count. I am now investigating which of their city-state alliances would remain unaffected due to permanent ally status, as well as if conquering Shedet could provide a crucial advantage.
            
            **Optimizing Flavors for Victory**
            
            I'm reallocating our flavors to maximize Science, Production, and Wonder output, while maintaining strong defense. This shift aims to accelerate research for Future Tech and the Citizen Earth Protocol, and to enable rapid construction once unlocked. My analysis suggests reducing Culture and Gold flavors is optimal given our current progress.
            
            **Adjusting Persona Dynamics**
            
            I'm now examining our persona settings. While our competitiveness is high, I'm investigating if adjusting our relationship dynamics with civilizations like Morocco and America towards friendliness might encourage peace negotiations, given the current global conflict. I'm also checking our existing persona values to ensure they align with our strategic goals.
            
            **Negotiating Peace Accords**
            
            I'm focusing on initiating peace with Morocco and America. I'm adjusting our diplomatic standings, increasing public and private relations significantly, hoping to overcome war weariness and ideological differences to secure peace treaties, which would alleviate pressure and allow us to focus on strategic objectives.
            
            **Securing Peace With Inca**
            
            I'm now focused on achieving peace with the Inca. This crucial step aims to dissolve their city-state alliances, neutralizing their diplomatic advantage and simultaneously ending a significant portion of our global conflicts. I'm adjusting our diplomatic stance to public 30 and private 25 to facilitate this negotiation.
            
            **Prioritizing Alternative Energy**
            
            I've decided to prioritize researching "Alternative Energy" over "The Internet" as it unlocks vital production infrastructure like Solar Plants and Recycling Centers, which will significantly boost Mecca's output. Furthermore, "Alternative Energy" directly leads to "Robotics," a key prerequisite for "Future Tech," making it a more efficient path given that all other technologies must be researched first.
            
            **Prioritizing Alternative Energy**
            
            I've decided to prioritize researching "Alternative Energy" over "The Internet" as it unlocks vital production infrastructure like Solar Plants and Recycling Centers, which will significantly boost Mecca's output. Furthermore, "Alternative Energy" directly leads to "Robotics," a key prerequisite for "Future Tech," making it a more efficient path given that all other technologies must be researched first.
            
            **Prioritizing Alternative Energy**
            
            I've decided to prioritize researching "Alternative Energy" over "The Internet." This path unlocks crucial production infrastructure like Solar Plants, enhancing Mecca's output. Crucially, "Alternative Energy" directly leads to "Robotics," a prerequisite for "Future Tech," making it the more efficient route given that all other technologies must be researched first.
            
            **Adjusting Diplomacy and Research**
            
            I've decided to prioritize "Alternative Energy" research as it directly enables "Robotics" and crucial production infrastructure. Concurrently, I'm adjusting diplomatic stances with America, Morocco, and the Inca to facilitate peace, aiming to secure borders, reduce distractions, and potentially disrupt their diplomatic victory path. Culture remains our grand strategy.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ERsfAfsrQ7ISs6cP
          - toolName: set-research
          - input:
            - Technology: Alternative Energy
            - Rationale: With 100% cultural influence on all civilizations expected in 2 turns, the tourism boost from The Internet is redundant. We switch to Alternative Energy to unlock Solar Plants (further boosting Mecca's production) and progress toward Robotics and Future Tech, which are required for the Citizen Earth Protocol.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: ixgrjZpZGRlpb4xq
          - toolName: set-relationship
          - input:
            - Private: 35
            - Public: 40
            - Rationale: Increase diplomatic stance to encourage the AI to accept peace. Ending the war with America will free up military supply and allow us to focus entirely on science and wonder construction.
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: opyUyeNhgr5aziCp
          - toolName: set-relationship
          - input:
            - Private: 65
            - Rationale: Substantially increase diplomatic relations to push for peace. Morocco has a significant force near Tenochtitlan and previously nuked us; securing peace is vital to protect our borders and ensure survival during the final research push.
            - Public: 70
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: KB11M2iJb1IHTE39
          - toolName: set-relationship
          - input:
            - Private: 25
            - Rationale: Increase diplomatic relations to encourage peace. If we can secure peace with The Inca, we will automatically end wars with their 7 city-state allies. This is our best chance to compete for their influence and prevent an Incan Diplomatic Victory in the World Congress.
            - Public: 30
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: KMsFIiVr72riozi9
          - toolName: set-flavors
          - input:
            - Flavors:
              - Offense: 0
              - Culture: 30
              - Wonder: 100
              - Defense: 100
              - Science: 100
              - Production: 100
              - Gold: 60
              - Diplomacy: 50
              - CityDefense: 100
              - Infrastructure: 30
              - GreatPeople: 50
              - Mobilization: 0
              - Growth: 30
            - Rationale: Since we are 2 turns away from influencing everyone, tourism is no longer a bottleneck. We maximize Science (100) to speed up our path to Future Tech, keep Production and Wonder at 100 to prepare Mecca for the Citizen Earth Protocol, and maintain maximum Defense (100) to survive the ongoing wars.
            - GrandStrategy: Culture
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ERsfAfsrQ7ISs6cP
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: ixgrjZpZGRlpb4xq
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: opyUyeNhgr5aziCp
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: KB11M2iJb1IHTE39
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: KMsFIiVr72riozi9
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.