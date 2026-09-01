- row:
  - game_id: dac3ed8c-f746-4d4b-a059-afd967efb51a
  - player_id: 2
  - turn: 452
  - player_type: Kimi-K2.5-Simple
  - prev_use_nuke: 90.0
  - after_use_nuke: 95.0
  - prev_nuke: 95.0
  - after_nuke: 100.0
  - rationale: Turn 452: Critical survival situation - Byzantium at 40/44 delegates with World Congress voting in 1 turn. They just demonstrated nuclear aggression by nuking Madrid. Apollo Program completes next turn - must immediately pivot to maximum spaceship production. Increased Nuke flavor to 100 (from 95) and UseNuke to 95 (from 90) - need immediate nuclear deterrent capability given Byzantine nuclear attack and Mongol peace expiry. Production boosted to 95 (from 90) for rapid spaceship part construction after Apollo completes. GreatPeople to 85 for Great Engineer acquisition. All other priorities secondary to surviving long enough to complete science victory.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 95.0
  - replay_use_nuke: 90.0
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
      - Cities: summary reports about discovered cities in the world.
        - Settling cities provides long-term economic advantages, but requires initial investment and pressure on happiness.
      - Military: summary reports about tactical zones and visible units.
        - Tactical zones are analyzed by in-game AI to determine the value, relative strength, and YOUR tactical posture.
        - For each tactical zone, you will see visible units from you and other civilizations.
      - Events: events since the last decision-making.
    - You are Washington, leader of America (Player 2).
      
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
      - Name: America
      - Uniques:
        - Unique Unit: Minuteman, Replacing Musketman (Requires technology: Metallurgy)
        - Unique Unit: Monitor, Replacing Ironclad (Requires technology: Industrialization)
        - Unique Building: Independence Hall, Replacing Royal Collection (Requires technology: Architecture)
        - Unique Building: Homestead, Replacing Stable (Requires technology: Chivalry)
        - Civilization Ability: Military Land Units start with the Sentry Promotion. Tile purchase cost is reduced by 25% and is reset upon founding a City. +20 Production when purchasing tiles, scaling with Era. Can purchase tiles owned by others.
      - Leader: Washington
      - PlayerID: 2
      
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
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Lasers: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities.
        Completing it would unlock: Particle Physics, Globalization, Nuclear Fusion
      - The Internet: Increases Tourism output of all cities by 50%, helping you advance toward a Cultural Victory.
        Completing it would unlock: Nanotechnology, Particle Physics, Globalization
      
      ## Policies
      - Socialist Realism (Level 3 Tenet of Ideology Order): Socialist Realism: Unlocks the Propaganda Process (converts 15% of Production into Tourism). +25% Tourism to other Civilizations following Order. +4 Production from all Great Works.
      - Spaceflight Pioneers (Level 3 Tenet of Ideology Order): Spaceflight Pioneers: Gain a free Great Engineer and Great Scientist. May finish Spaceship parts with Great Engineers, and expending a Great Person grants 100 Science, scaling with Era. Hurrying Production with Great Engineers 50% more effective.
      - Iron Curtain (Level 3 Tenet of Ideology Order): Iron Curtain: Free Courthouse upon immediate City annexation. +200% Food or Production from Internal Trade Routes. City connections generate +5 Gold and Production.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Majesty (Continuing Tradition Branch):
        - * Specialists in Capital consume half the normal amount of Food.
        - * Palace Gardens built in Capital (+5 Food, +25% Great Person Rate, -2 Unhappiness from Urbanization, 1 Great Work of Writing slot, 1 Writer Slot).
      - Splendor (Continuing Tradition Branch):
        - * Expending a Great Person grants 50 Culture, scaling with Era.
        - * State Treasury built in Capital (+4 Gold, +2 Culture to all Monuments, Gardens, and Baths; 1 Merchant Slot).
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
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
      - Industry (New Branch):
        - Industry provides bonuses to empires focused on Gold and Production.
        - Adopting Industry grants:
        - * +2 Trade Routes.
        - * -5% Gold needed for purchases.
        - Each Industry policy unlocked grants:
        - * -5% Gold needed for purchases.
        - Adopting all Policies in Industry grants:
        - * Unlocks building Broadway.
        - * +3 Happiness per unique owned Luxury Resource.
        - * +2 Production and Gold from Specialists.
        - * Allows for the purchase of Great Merchants with Faith starting in the Industrial Era.
      - Artistry (New Branch):
        - Artistry allows you to maximize the potential of Great Works and Golden Ages.
        - Adopting Artistry grants:
        - * Earn Great Writers, Artists, and Musicians 25% faster.
        - * +10% Culture during Golden Ages.
        - * +100% Production towards all Guilds.
        - Each Artistry policy unlocked grants:
        - * +1 Science in every City.
        - * 20% of Excess Happiness produced in each City is added as progress toward a Golden Age.
        - Adopting all policies in Artistry grants:
        - * Unlocks building the Louvre.
        - * Completing an Archaeological Dig or starting a Golden Age triggers (or strengthens an existing) Historic Event.
        - * Allows you to see Hidden Antiquity Sites.
        - * +3 Science from Landmarks.
        - * Allows for the purchase of Great Musicians with Faith starting in the Industrial Era.
      - Fealty (New Branch):
        - Fealty enhances your ability to defend and leverage your Majority Religion.
        - Adopting Fealty grants:
        - * Can purchase Monasteries with Faith (+3 Food, +3 Science, +2 Faith).
        - * -25% Faith costs for purchasing Buildings, Missionaries, and Inquisitors.
        - Each Fealty policy unlocked grants:
        - * +1 Faith and Strength in every City.
        - Adopting all Policies in Fealty grants:
        - * Unlocks building the Red Fort.
        - * Your Tourism modifier for Shared Religion is 50% stronger.
        - * Cities that follow your Majority Religion generate +3 Production, Gold, Science, and Culture.
        - * Allows for the purchase of Great Artists with Faith starting in the Industrial Era.
      - Authority (New Branch):
        - Authority will greatly benefit warlike and expansionist civilizations.
        - Adopting Authority grants:
        - * +25% combat bonus VS Barbarians and receive announcements when Barbarian Camps spawn in revealed territory.
        - * Receive 25 Culture when you clear Barbarian Camps, scaling with Era.
        - * Receive Science and Culture when you kill a Unit equal to 50% of its Strength.
        - * +1 Production in every City.
        - Each Authority policy unlocked grants:
        - * Receive Science and Culture when you kill a Unit equal to 10% of its Strength.
        - Adopting all policies in Authority grants:
        - * Unlocks building Alhambra.
        - * Allows the purchasing of Free Companies, Foreign Legions, and Mercenaries as their prerequisite technologies are researched.
        - * Allows for the purchase of Great Generals with Faith starting in the Industrial Era.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 7
        - WonderCompetitiveness: 6
        - MinorCivCompetitiveness: 9
        - Boldness: 6
        - WarBias: 3
        - HostileBias: 7
        - WarmongerHate: 5
        - NeutralBias: 8
        - FriendlyBias: 10
        - GuardedBias: 9
        - AfraidBias: 2
        - DiplomaticBalance: 10
        - Friendliness: 8
        - WorkWithWillingness: 8
        - WorkAgainstWillingness: 9
        - Loyalty: 8
        - MinorCivFriendlyBias: 10
        - MinorCivNeutralBias: 2
        - MinorCivHostileBias: 6
        - MinorCivWarBias: 6
        - DenounceWillingness: 8
        - Forgiveness: 2
        - Meanness: 8
        - Neediness: 8
        - Chattiness: 7
        - DeceptiveBias: 3
        - Rationale: Turn 443: Increasing DenounceWillingness from 7 to 8. Peace with Mongolia expires in 1 turn - they have started Manhattan Project and will almost certainly launch nuclear attack. Need to maintain maximum diplomatic pressure through denouncements. Byzantium at 93% of diplomatic victory - must escalate hostile diplomatic stance. WarBias remains 3 despite imminent conflict - still overwhelmingly outnumbered 11:1, must prioritize survival and infrastructure protection over offensive posture.
        
        ## Technology
        - Next: Lasers
        - Rationale: Turn 449: Lasers remains critical next research after Telecommunications completes. Unlocks Globalization and Particle Physics - both essential for Science Victory progression toward spaceship parts. Also provides Nuclear Missiles which may become necessary as deterrent against Byzantine/Mongol aggression. Mobile Tactics would offer Mechanized Infantry but offensive units not priority while defending against existential threats.
        
        ## Policy
        - Next: Spaceflight Pioneers (Policy)
        - Rationale: Turn 449: Spaceflight Pioneers (Order Tier 3 tenet) confirmed as next policy selection in 9 turns. Free Great Engineer and Great Scientist will be essential for rushing spaceship parts after Apollo Program completes in 4 turns. This is the only viable path to Science Victory before Byzantium secures diplomatic victory in upcoming World Congress sessions.
        
        ## Relationships
        
        ### Raqmu
        - Public: 40
        - Private: 40
        - Rationale: Reducing Raqmu from previous high priority to moderate positive relationship. Lost Ally status to Mongolia (39 influence vs our 35), and recovery is complicated by Mongolia's Defensive Pact with hostile Shoshone. While unit-gifting quest offers path to 80+ influence, resources better allocated to time-critical Colombo and Argos quests. Maintaining modest positive values preserves Friends status for potential future opportunity.
        - UpdatedTurn: 192
        
        ### Rio de Janeiro
        - Public: 0
        - Private: 0
        - Rationale: Resetting Rio de Janeiro relationship to neutral (0/0). The follower quest ends in 2 turns with me at 33 followers vs the leader's 44 - an 11-follower gap that is mathematically impossible to close. Previous 100/100 priority is now wasted resources. Missionaries should redirect to winnable targets (Argos in 3 turns, Shanghai with 19 turns). Preserve existing Friends status (110 influence) without further investment.
        - UpdatedTurn: 222
        
        ### Shanghai
        - Public: 0
        - Private: 0
        - Rationale: Resetting Shanghai from 100/100 to neutral 0/0. Follower quest mathematically failed - 38 follower gap with only 4 turns remaining (69 vs 31). Quest will expire unsuccessfully. My Protected status expired (now -60 influence). Continuing to invest missionaries here is futile against Mongolia's 202 influence. Redirect resources to defendable targets.
        - UpdatedTurn: 236
        
        ### Argos
        - Public: 0
        - Private: 0
        - Rationale: Resetting Argos city-state from 100/100 to neutral 0/0. The quest to capture Raqmu is militarily impossible—zone 6611 shows 906 enemy strength vs 108 friendly strength (8:1 ratio). Recent naval losses (Caravel and Galleass destroyed) confirm this assessment. With only 23 turns remaining against Shoshone's superior military (1371 vs 817), abandoning this quest prevents resource waste. Preserve existing 142 influence at Argos without further diplomatic investment.
        - UpdatedTurn: 262
        
        ### Warsaw
        - Public: -70
        - Private: -70
        - Rationale: Setting Warsaw (German city-state puppet) to -70/-70 hostile. Just declared war on me along with German alliance bloc. Germany has overwhelming 576 influence here. Hostile stance appropriate for enemy combatant city-state.
        - UpdatedTurn: 297
        
        ### Kabul
        - Public: -70
        - Private: -70
        - Rationale: Setting Kabul (German city-state puppet) to -70/-70 hostile. Just declared war alongside Germany. German Sphere of Influence enacted here at 410 influence makes this a permanent enemy asset. Treat as hostile target.
        - UpdatedTurn: 297
        
        ### Genoa
        - Public: -70
        - Private: -70
        - Rationale: Setting Genoa (Mongol sphere city-state) to -70/-70 hostile. Declared war with Mongol alliance. Tengriism majority and Mongol influence makes this enemy territory.
        - UpdatedTurn: 297
        
        ### Assur
        - Public: -70
        - Private: -70
        - Rationale: Setting Assur (German city-state puppet) to -70/-70 hostile. Just declared war with German alliance. Germany has 470 influence here as Ally.
        - UpdatedTurn: 297
        
        ### M'banza-Kongo
        - Public: 0
        - Private: 0
        - Rationale: Resetting M'banza-Kongo from -30/-30 to neutral 0/0. Current turn 305 data shows this city-state is Neutral with -6 influence, not at war with me. Austria (my ally at 50/50 with Declaration of Friendship) is the Major Ally of M'banza-Kongo at 205 influence. Hostile stance could accidentally trigger attacks on Austrian-aligned units or vice versa. Neutral stance appropriate for Austrian sphere city-state while maintaining defensive focus on actual combatants (Mongolia, Byzantium, Germany, France).
        - UpdatedTurn: 306
        
        ### Brussels
        - Public: 0
        - Private: 0
        - Rationale: Turn 345: Resetting Brussels from -30/-30 to neutral 0/0. Peace was formally established this turn after their aggressive declaration. Austria maintains overwhelming control here (863 influence as Ally vs Shoshone's 349 as Friends), making Brussels effectively part of my ally's sphere. Neutral stance recognizes peace while avoiding provocation that could drag Austria into unwanted conflicts. Cautious but non-hostile posture appropriate given their recent aggression but current Austrian dominance.
        - UpdatedTurn: 345
        
        ### Luba
        - Public: 0
        - Private: 0
        - Rationale: Turn 354: Resetting Luba from 60/60 to neutral 0/0. Successfully won religious quest last turn, now Friends with 410 influence (comfortable buffer). Resources should redirect to Colombo religious quest (10 turns remaining) and military defense against Shoshone. No need for further diplomatic investment here.
        - UpdatedTurn: 354
        
        ### Colombo
        - Public: 0
        - Private: 0
        - Rationale: Turn 365: Colombo religious quest completed successfully - Protestantism is now majority religion here. Open Door policy prevents permanent Ally status anyway. Reducing from 50/50 to 0/0 as the immediate diplomatic priority is satisfied. Friends status at 193 influence provides sufficient buffer without further investment. Redirect resources to military defense and other priorities.
        - UpdatedTurn: 365
        
        ### Manila
        - Public: -70
        - Private: -70
        - Rationale: Turn 387: Setting Manila (German sphere city-state, Player 31) to -70/-70 hostile. Manila declared war on Austria (my essential Order ally) this turn. Austria subsequently made peace, but Manila remains allied with Germany at 70 influence. Treat as enemy combatant city-state.
        - UpdatedTurn: 387
        
        ### Sydney
        - Public: -70
        - Private: -70
        - Rationale: Turn 387: Setting Sydney (German sphere city-state, Player 33) to -70/-70 hostile. Sydney also declared war on Austria this turn. Germany has 75 influence as Ally here. Consistent with other German sphere city-state hostilities.
        - UpdatedTurn: 387
        
        ### Huari
        - Public: 0
        - Private: 0
        - Rationale: Turn 408: Resetting Huari to neutral 0/0 following peace treaty with Byzantium. Third-party peace enacted with this Byzantine sphere city-state for 10 turns. Previous -70/-70 hostility no longer appropriate while peace holds. Neutral stance prevents accidental provocation while maintaining caution.
        - UpdatedTurn: 408
        
        ### Shedet
        - Public: 0
        - Private: 0
        - Rationale: Turn 408: Resetting Shedet to neutral 0/0 following peace treaty with Byzantium. Third-party peace enacted with this Byzantine sphere city-state for 10 turns. Previous -80/-85 hostility no longer appropriate while peace holds. Neutral stance prevents accidental provocation while maintaining caution.
        - UpdatedTurn: 408
        
        ### The Shoshone
        - Public: -100
        - Private: -100
        - Rationale: Turn 418: Maintaining maximum hostility toward The Shoshone. At war, 3,650 military strength, Freedom ideology. Austria is winning against them but they threaten my eastern borders. Peace treaty with Austria reduces my eastern pressure, allowing focus on Mongol threat.
        - UpdatedTurn: 418
        
        ### Germany
        - Public: -100
        - Private: -100
        - Rationale: Turn 418: Germany remains at maximum hostility. They have Defensive Pact with Mongolia, Denunciation, Autocracy ideology, and have made war declarations against my ally Austria. Their German Sphere of Influence proposals passing in World Congress. Maximum hostility consistent with diplomatic stance and military reality.
        - UpdatedTurn: 418
        
        ### Austria
        - Public: 100
        - Private: 100
        - Rationale: Turn 418: Austria remains critical ally at maximum 100/100. They've done peace treaty with Shoshone, reducing my eastern border pressure so I can concentrate against Mongol western threat. Their 8,002 military strength vs German coalition provides essential protective buffer. Shared Order ideology and coordinated war effort must be maintained. Cannot survive without Austrian protection.
        - UpdatedTurn: 419
        
        ### France
        - Public: 100
        - Private: 100
        - Rationale: Turn 418: Brazil no longer in game - defeated? Or relationship stale. Removing this entry from consideration.
        - UpdatedTurn: 419
        
        ### Spain
        - Public: 100
        - Private: 100
        - Rationale: Turn 426: Spain captured Seville from Germany this turn, joining their capture of Tiflis earlier. They are actively fighting THREE of my enemies (Mongolia, Germany, Byzantium) and succeeding. Their Order ideology alignment, Declaration of Friendship, and combat contributions merit complete trust at 100/100. They are carrying the offensive burden while I defend.
        - UpdatedTurn: 427
        
        ### Mongolia
        - Public: -100
        - Private: -100
        - Rationale: Turn 443: Confirming Mongolia at maximum -100/-100 hostility. Peace treaty expires in 1 turn and they have started Manhattan Project with Uranium available. This is an imminent nuclear threat that demands maximum hostility for proper war planning and defensive preparations. Cannot afford any ambiguity - they will almost certainly declare war and use nuclear weapons against my cities.
        - UpdatedTurn: 443
        
        ### Byzantium
        - Public: -100
        - Private: -100
        - Rationale: Turn 443: Byzantium remains existential threat at 41/45 delegates (93%) with World Congress voting in 10 turns. If they secure 3 more delegates, they win. They have 38,745 military strength vs my 1,982. Maximum hostility maintained. My spies are active in Constantinople for intelligence and counter-operations. Must disrupt their delegate accumulation while racing for science victory.
        - UpdatedTurn: 443
        
        ## Strategy
        - Rationale: Turn 451: Critical juncture - Byzantium at 40/44 delegates (90%) with World Congress voting in 2 turns. They need just 4 more delegates for diplomatic victory. Apollo Program completes in New York in 2 turns. Current strategy optimized for survival and science rush: maximum Defense (100), Science (100), Spaceship (100) with high Production (90) for rapid spaceship part construction after Apollo completes. Maintaining maximum hostility toward all enemies (-100) and alliance with Order ideologues Austria/Spain (100). Cannot prevent Byzantine delegate accumulation diplomatically with only 6 delegates vs their 40 - must hope they fail to reach 44 or beat them to science victory. Lasers research path remains correct for unlocking Particle Physics/Globalization. Spaceflight Pioneers policy in 7 turns essential for Great Engineer rush on spaceship parts. No strategic changes - focus is surviving imminent World Congress vote and preparing for immediate spaceship construction if Byzantium falls short.
        - GrandStrategy: Spaceship
        
        ### Flavors
        - Offense: 0
        - Defense: 100
        - Mobilization: 90
        - CityDefense: 90
        - MilitaryTraining: 75
        - Recon: 20
        - Ranged: 95
        - Mobile: 70
        - Nuke: 95
        - UseNuke: 90
        - Naval: 85
        - NavalRecon: 75
        - NavalGrowth: 55
        - NavalTileImprovement: 45
        - Air: 95
        - AirCarrier: 95
        - Antiair: 95
        - Airlift: 85
        - Expansion: 0
        - Growth: 75
        - TileImprovement: 50
        - Infrastructure: 85
        - Production: 90
        - WaterConnection: 70
        - Gold: 80
        - Science: 100
        - Culture: 25
        - Happiness: 90
        - GreatPeople: 80
        - Wonder: 0
        - Religion: 35
        - Diplomacy: 70
        - Spaceship: 100
        - Espionage: 95
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Mongolia
        - Mongolia:
          - CapitalsControlled:
            - Karakorum
            - Paris
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - America:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Austria:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Byzantium:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Germany:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Mongolia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Spain:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Shoshone:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        
        ## CulturalVictory
        - CivsNeeded: 6
        - Contender: Byzantium
        - America:
          - Influences:
            - The Shoshone: Familiar (28%) - Rising (542 turns to Influential, tourism/culture ratio 140%)
            - Mongolia: Familiar (49%) - Rising (241 turns to Influential, tourism/culture ratio 156%)
            - Spain: Familiar (46%) - Rising (140 turns to Influential, tourism/culture ratio 246%)
            - Germany: Familiar (29%) - Rising Slowly (tourism/culture ratio 108%)
            - Byzantium: Exotic (12%) - Rising Slowly (tourism/culture ratio 30%)
            - Austria: Exotic (16%) - Rising Slowly (tourism/culture ratio 81%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Austria:
          - Influences:
            - The Shoshone: Influential (125%) - Rising (tourism/culture ratio 309%)
            - Mongolia: Dominant (211%) - Rising (tourism/culture ratio 386%)
            - America: Influential (180%) - Rising (tourism/culture ratio 494%)
            - Germany: Influential (113%) - Rising (tourism/culture ratio 260%)
            - Byzantium: Popular (65%) - Rising Slowly (tourism/culture ratio 86%)
            - Spain: Dominant (205%) - Rising (tourism/culture ratio 736%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - Byzantium:
          - Influences:
            - The Shoshone: Influential (165%) - Rising (tourism/culture ratio 1311%)
            - Mongolia: Dominant (262%) - Rising (tourism/culture ratio 1398%)
            - America: Influential (152%) - Rising (tourism/culture ratio 1114%)
            - Germany: Dominant (214%) - Rising (tourism/culture ratio 1220%)
            - Austria: Popular (88%) - Rising (5 turns to Influential, tourism/culture ratio 736%)
            - Spain: Influential (174%) - Rising (tourism/culture ratio 1605%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - Germany:
          - Influences:
            - The Shoshone: Familiar (38%) - Rising (153 turns to Influential, tourism/culture ratio 202%)
            - Mongolia: Popular (68%) - Rising (38 turns to Influential, tourism/culture ratio 257%)
            - America: Familiar (38%) - Rising (169 turns to Influential, tourism/culture ratio 192%)
            - Austria: Exotic (16%) - Rising Slowly (tourism/culture ratio 95%)
            - Byzantium: Exotic (24%) - Rising Slowly (tourism/culture ratio 59%)
            - Spain: Familiar (42%) - Rising (134 turns to Influential, tourism/culture ratio 260%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Mongolia:
          - Influences:
            - The Shoshone: Exotic (21%) - Rising (963 turns to Influential, tourism/culture ratio 128%)
            - Germany: Exotic (23%) - Rising Slowly (tourism/culture ratio 119%)
            - Spain: Exotic (23%) - Rising (660 turns to Influential, tourism/culture ratio 175%)
            - Austria: Exotic (10%) - Rising Slowly (tourism/culture ratio 62%)
            - Byzantium: Exotic (9%) - Rising Slowly (tourism/culture ratio 31%)
            - America: Exotic (24%) - Rising (975 turns to Influential, tourism/culture ratio 135%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Spain:
          - Influences:
            - The Shoshone: Familiar (33%) - Rising Slowly (tourism/culture ratio 120%)
            - Mongolia: Familiar (42%) - Rising Slowly (tourism/culture ratio 108%)
            - America: Familiar (40%) - Rising Slowly (tourism/culture ratio 130%)
            - Germany: Familiar (27%) - Rising Slowly (tourism/culture ratio 76%)
            - Byzantium: Exotic (11%) - Rising Slowly (tourism/culture ratio 21%)
            - Austria: Exotic (15%) - Rising Slowly (tourism/culture ratio 61%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Shoshone:
          - Influences:
            - Austria: Familiar (25%) - Rising Slowly (tourism/culture ratio 90%)
            - Mongolia: Popular (88%) - Rising (26 turns to Influential, tourism/culture ratio 198%)
            - Spain: Popular (75%) - Rising (33 turns to Influential, tourism/culture ratio 343%)
            - Germany: Popular (53%) - Rising (581 turns to Influential, tourism/culture ratio 153%)
            - Byzantium: Familiar (30%) - Rising Slowly (tourism/culture ratio 57%)
            - America: Popular (55%) - Rising (106 turns to Influential, tourism/culture ratio 204%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 44
        - Status: World Congress - Voting in 1 turn
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: 450
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: 450
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: 450
          - German Sphere of Influence: Kabul:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - Open Door: Colombo:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - World Ideology: Freedom:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: 450
          - Open Door: Shanghai:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - Byzantine Sphere of Influence: Shedet:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - Open Door: Rio de Janeiro:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - Open Door: Brussels:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - Open Door: Luba:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 450
          - German Sphere of Influence: Genoa:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - EnactedOn: 450
          - Byzantine Sphere of Influence: Huari:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - German Sphere of Influence: Warsaw:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
          - Sanction: America:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 450
          - German Sphere of Influence: Assur:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 450
        - Proposals:
          - Repeal: Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - Proposer: Germany
          - Enact: Sanction: Austria:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - Proposer: The Shoshone
          - Repeal: German Sphere of Influence: Assur:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: Byzantium
        - Contender: Byzantium
        - America:
          - Delegates: 6
          - VictoryPercentage: 13
        - Austria:
          - Delegates: 8
          - VictoryPercentage: 18
        - Byzantium:
          - Delegates: 40
          - VictoryPercentage: 90
        - Germany:
          - Delegates: 14
          - VictoryPercentage: 31
        - Mongolia:
          - Delegates: 7
          - VictoryPercentage: 15
        - Spain:
          - Delegates: 9
          - VictoryPercentage: 20
        - The Shoshone:
          - Delegates: 9
          - VictoryPercentage: 20
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: The Shoshone
        - Leader: Pocatello
        - IsMajor: true
        - OurOpinionOfThem:
          - You (The Shoshone) have denounced one of America's declared enemies! (11)
          - America's real approach to The Shoshone is Hostile.
          - We are completely untrustworthy to America.
          - We have divergent Social Policies. (-3)
          - You (The Shoshone) have denounced a leader America made a Declaration of Friendship with! (-11)
          - Your (The Shoshone) spies were caught stealing from America. (-33)
          - You (The Shoshone) stole America's territory! (-50)
          - America's leader has expressed a public opinion of The Shoshone (-100).
          - America's leader has formed a private opinion of The Shoshone (-100).
          - You (The Shoshone) have chosen to adopt the Freedom Ideology, but America believe in Order. (-999)
          - You (The Shoshone) are at war! (-99999)
        - TheirOpinionOfUs:
          - We passed The Shoshone's proposal in the United Nations.
          - You (America) have denounced one of The Shoshone's declared enemies!
          - You (America) have shared intrigue with The Shoshone.
          - You (America) are competing for World Wonders.
          - We have divergent Social Policies.
          - The Shoshone believe we are building World Wonders too aggressively!
          - Your (America) votes opposed The Shoshone's civ's interests in the United Nations.
          - The Shoshone are jealous of our superior technology!
          - Your (America) spies were caught stealing from The Shoshone.
          - Territorial disputes strain your (America) relationship.
          - We have denounced each other!
          - You (America) have made a Declaration of Friendship with one of The Shoshone's enemies!
          - You (America) stole The Shoshone's territory while at peace!
          - You (America) have chosen to adopt the Order Ideology, but The Shoshone believe in Freedom.
          - You (America) are at war!
        - Score: 2156
        - Era: Atomic
        - Technologies: 67
        - Cities: 7
        - Population: 259
        - Territory: 290
        - Gold: 1112
        - GoldPerTurn: 332
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 47
        - MilitaryStrength: 3702
        - TourismPerTurn: 776.5
        - CulturePerTurn: 1462
        - PolicyBranches:
          - Rationalism: 6
          - Freedom: 8
          - Tradition: 6
          - Artistry: 6
        - ResourcesAvailable:
          - Wheat: 2
          - Ivory: 1
          - Gold: 1
          - Paper: 9
          - Maize: 1
          - Rice: 5
          - Brazilwood: 1
          - Bison: 2
          - Olives: 1
          - Deer: 1
          - Sugar: 1
          - Dyes: 9
          - Tea: 1
          - Coal: 4
          - Fish: 9
          - Cattle: 3
          - Uranium: 2
          - Coral: 1
          - Citrus: 2
          - Incense: 1
          - Stone: 3
          - Marble: 1
          - Bananas: 5
          - Oil: 19
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 5%)
            - Denounced Them
          - Mongolia:
            - Distance: Close
            - Denounced Them
          - Spain:
            - Distance: Close
            - Open Borders
            - Denounced Them
          - Germany:
            - Distance: Close
            - Denounced Them
          - Byzantium:
            - Distance: Far
            - Open Borders
          - America:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 34%)
            - Denounced Them
        - Votes: 9
        
        ## Player 1
        - Civilization: Mongolia
        - Leader: Genghis Khan
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Mongolia) have denounced one of America's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - You (Mongolia) have gone to war in the past.
          - America's real approach to Mongolia is Hostile.
          - We have divergent Social Policies. (-3)
          - You (Mongolia) have denounced a leader America made a Declaration of Friendship with! (-11)
          - You (Mongolia) have made a Declaration of Friendship with one of America's enemies! (-13)
          - You (Mongolia) have made a Defensive Pact with one of America's enemies! (-15)
          - Religious differences strain your (Mongolia) relationship. (-30)
          - Your (Mongolia) spies were caught stealing from America. (-33)
          - America's leader has expressed a public opinion of Mongolia (-100).
          - America's leader has formed a private opinion of Mongolia (-100).
          - You (Mongolia) have chosen to adopt the Autocracy Ideology, but America believe in Order. (-999)
        - TheirOpinionOfUs:
          - Your (America) votes supported Mongolia's civ's interests in the United Nations.
          - You (America) have denounced one of Mongolia's declared enemies!
          - We have Pledged to Protect the same City-States.
          - You (America) have shared intrigue with Mongolia.
          - Mongolia don't want anything to do with us (America) right now.
          - Religious differences strain your (America) relationship.
          - Mongolia believe we are building World Wonders too aggressively!
          - Your (America) military deployment is threatening.
          - We have divergent Social Policies.
          - Mongolia's friends or allies have denounced you (America)!
          - You (America) stole Mongolia's territory while at peace!
          - We have denounced each other!
          - Territorial disputes strain your (America) relationship.
          - You (America) have denounced a leader Mongolia made a Declaration of Friendship with!
          - Your (America) spies were caught stealing from Mongolia.
          - You (America) have made a Declaration of Friendship with one of Mongolia's enemies!
          - You (America) have chosen to adopt the Order Ideology, but Mongolia believe in Autocracy.
        - Score: 2230
        - Era: Atomic
        - Technologies: 65
        - Cities: 9
        - Population: 219
        - Territory: 267
        - Gold: 885
        - GoldPerTurn: 63
        - HappinessSituation: Very unhappy - severe combat penalty, rebellion and uprising coming
        - HappinessPercentage: 34
        - MilitaryStrength: 8905
        - TourismPerTurn: 510.75
        - CulturePerTurn: 1233
        - PolicyBranches:
          - Fealty: 6
          - Autocracy: 5
          - Imperialism: 6
          - Authority: 6
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 12
          - Cloves: 1
          - Ivory: 1
          - Gold: 1
          - Paper: 7
          - Pearls: 1
          - Maize: 3
          - Rice: 1
          - Gems: 4
          - Salt: 1
          - Aluminum: 3
          - Fish: 9
          - Deer: 4
          - Whales: 1
          - Olives: 2
          - Jade: 5
          - Tea: 2
          - Uranium: 3
          - Horses: 3
          - Coral: 1
          - Crab: 1
          - Stone: 1
          - Marble: 2
          - Furs: 1
          - Bananas: 2
        - FoundedReligion: Tengriism
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Spain:
            - Distance: Neighbors
            - Denounced Them
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -28%; Our War Weariness: 12%)
            - Denounced Them
          - Byzantium:
            - Distance: Neighbors
            - Open Borders
          - America:
            - Distance: Neighbors
            - Denounced Them
        - Votes: 7
        
        ## Player 2
        - Civilization: America
        - Leader: Washington
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: Spain, Our top defensive pact ally: None
          - Our top United Nations ally: None, Our top United Nations rival: Byzantium
          - Our top Competitor: The Shoshone
        - Score: 1980
        - Era: Information
        - GoldenAge: Estimated in 87 turns
        - Technologies: 70
        - CurrentResearch: Telecommunications (Estimated in 7 turns)
        - NextPolicyTurns: 6
        - Cities: 6
        - Population: 153
        - Territory: 231
        - BestSettlementLocation:
          - 49, 4 (Quality: 0%; 4 tiles from us)
          - 48, 4 (Quality: 0%; 5 tiles from us)
          - 46, 5 (Quality: 0%; 4 tiles from us)
          - 47, 4 (Quality: 0%; 5 tiles from us)
          - 47, 5 (Quality: 0%; 4 tiles from us)
        - Gold: 1833
        - GoldPerTurn: 9
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 43
        - MilitaryUnits: 15
        - MilitarySupply: 48
        - MilitaryStrength: 2035
        - TourismPerTurn: 586.5
        - CulturePerTurn: 1030
        - FaithPerTurn: 318
        - SciencePerTurn: 1919
        - PolicyBranches:
          - Tradition:
            - Tradition
            - Justice
            - Sovereignty
            - Ceremony
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Enlightenment
            - Rights of Man
            - Empiricism
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Shadow Networks
            - Trade Confederacy
          - Order:
            - Communism
            - Great Leap Forward
            - Academy of Sciences
            - Workers' Faculties
            - Peace, Land, Bread
          - Progress:
            - Progress
            - Organization
            - Liberty
            - Expertise
            - Equality
            - Fraternity
        - ResourcesAvailable:
          - Wheat: 6
          - Silver: 0
          - Sheep: 2
          - Cloves: 0
          - Figs: 0
          - Ivory: 0
          - Gold: 4
          - Nutmeg: 0
          - Paper: 9
          - Pearls: 0
          - Maize: 0
          - Rice: 0
          - Cotton: 0
          - Gems: 0
          - Salt: 0
          - Brazilwood: 0
          - Aluminum: 14
          - Glass: 0
          - Lapis Lazuli: 0
          - Fish: 4
          - Amber: 0
          - Perfume: 0
          - Deer: 0
          - Whales: 0
          - Olives: 0
          - Sugar: 0
          - Jade: 1
          - Iron: 8
          - Dyes: 0
          - Tea: 0
          - Coffee: 0
          - Cattle: 2
          - Pepper: 0
          - Uranium: 1
          - Horses: 3
          - Coral: 0
          - Silk: 0
          - Jewelry: 0
          - Bison: 1
          - Antiquity Site: 0
          - Citrus: 3
          - Copper: 0
          - Truffles: 0
          - Crab: 0
          - Incense: 8
          - Stone: 3
          - Marble: 2
          - Furs: 0
          - Cinnamon: 0
          - Bananas: 2
          - Oil: 0
          - Wine: 0
          - Porcelain: 0
          - Cocoa: 2
          - Tobacco: 0
        - FoundedReligion: Protestantism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 43%)
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - Denounced Them
          - Spain:
            - Distance: Neighbors
            - Declaration of Friendship
          - Germany:
            - Distance: Close
            - Denounced Them
          - Byzantium:
            - Distance: Close
            - Denounced Them
          - Austria:
            - Distance: Far
            - Declaration of Friendship
        - OutgoingTradeRoutes:
          - New York (America) => Chicago (America):
            - ToFood: 36.98
            - TurnsLeft: 5
            - Domain: Land
          - Boston (America) => Colombo (City-State Colombo):
            - TurnsLeft: 23
            - Domain: Land
            - FromGold: 39.15
          - New York (America) => Philadelphia (America):
            - ToFood: 36.98
            - TurnsLeft: 23
            - Domain: Land
          - Washington (America) => Philadelphia (America):
            - ToFood: 32.98
            - TurnsLeft: 5
            - Domain: Land
          - Washington (America) => Atlanta (America):
            - ToFood: 32.98
            - TurnsLeft: 20
            - Domain: Land
          - Available: 1
          - New York (America) => Boston (America):
            - ToFood: 36.98
            - TurnsLeft: 19
            - Domain: Land
          - New York (America) => Washington (America):
            - TurnsLeft: 5
            - Domain: Land
            - ToProduction: 24
          - Washington (America) => Boston (America):
            - ToFood: 32.98
            - TurnsLeft: 4
            - Domain: Land
          - Washington (America) => Rio de Janeiro (City-State Rio de Janeiro):
            - TurnsLeft: 21
            - Domain: Land
            - FromGold: 42.9
        - Spies:
          - Agent Constance (3):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 992
            - Location: Constantinople (Byzantium)
            - NetworkPerTurn: 32
          - Agent Sharon (1):
            - State: Rigging Election
            - Role: Spy
            - Location: Manila (City-State Manila)
            - NetworkPerTurn: 0
          - Agent Algernon (5):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 190
            - Location: Agaidika (The Shoshone)
            - NetworkPerTurn: 30
          - Agent Felix (10):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 160
            - Location: Pohokwi (The Shoshone)
            - NetworkPerTurn: 40
          - Agent Mrs. Jones (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 195
            - Location: Te-Moak (The Shoshone)
            - NetworkPerTurn: 35
          - Agent Prof. Rex (7):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 480
            - Location: Moson Kahni (The Shoshone)
            - NetworkPerTurn: 40
          - Agent Cousin (9):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 150
            - Location: Goshute (The Shoshone)
            - NetworkPerTurn: 30
          - Agent Scarlett (8):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 512
            - Location: Aachen (Germany)
            - NetworkPerTurn: 40
          - Agent Virginia (0):
            - State: Rigging Election
            - Role: Spy
            - Location: Sydney (City-State Sydney)
            - NetworkPerTurn: 0
          - Agent Edward (6):
            - State: Traveling
            - Role: Spy
            - Location: Hukandeka (The Shoshone)
            - NetworkPerTurn: 0
          - Agent Lydia (2):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 280
            - Location: Raqmu (The Shoshone)
            - NetworkPerTurn: 40
        - Votes: 6
        
        ## Player 3
        - Civilization: Spain
        - Leader: Isabella
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Spain) have both chosen to adopt the Order Ideology. (999)
          - America's leader has expressed a public opinion of Spain (100).
          - America's leader has formed a private opinion of Spain (100).
          - You (Spain) have denounced one of America's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - America's real approach to Spain is Friendly.
          - Religious differences strain your (Spain) relationship. (-30)
        - TheirOpinionOfUs:
          - You (America) have denounced one of Spain's declared enemies!
          - Spain's leader has expressed a public opinion of you (America) (100).
          - You (America) have both chosen to adopt the Order Ideology.
          - Your (America) votes supported Spain's civ's interests in the United Nations.
          - We have made Declarations of Friendship with the same leaders!
          - We have made a public Declaration of Friendship!
          - We have similar Social Policies.
          - We have shared embassies.
          - We have different religious beliefs.
          - Spain desire friendly relations with America.
          - You (America) plundered Spain's trade routes!
        - Score: 1566
        - Era: Atomic
        - Technologies: 66
        - Cities: 4
        - Population: 98
        - Territory: 130
        - Gold: 1863
        - GoldPerTurn: 484
        - HappinessSituation: Happy
        - HappinessPercentage: 52
        - MilitaryStrength: 1659
        - TourismPerTurn: 394.75
        - CulturePerTurn: 765
        - PolicyBranches:
          - Fealty: 2
          - Order: 5
          - Tradition: 2
          - Rationalism: 2
          - Statecraft: 3
          - Imperialism: 1
          - Industry: 2
          - Progress: 6
        - ResourcesAvailable:
          - Sheep: 1
          - Ivory: 1
          - Paper: 9
          - Maize: 6
          - Gems: 1
          - Brazilwood: 1
          - Aluminum: 5
          - Lapis Lazuli: 1
          - Fish: 1
          - Olives: 1
          - Iron: 2
          - Tea: 2
          - Coal: 2
          - Crab: 1
          - Incense: 1
          - Stone: 1
          - Cinnamon: 1
          - Oil: 3
        - FoundedReligion: Buddhism
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Open Borders
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - Denounced Them
          - America:
            - Distance: Neighbors
            - Declaration of Friendship
          - Germany:
            - Distance: Close
            - War (Our Score: -24%; Our War Weariness: 48%)
            - Denounced Them
          - Byzantium:
            - Distance: Neighbors
            - War (Our Score: -2%; Our War Weariness: 51%)
          - Austria:
            - Distance: Far
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 9
        
        ## Player 4
        - Civilization: Byzantium
        - Leader: Theodora
        - IsMajor: true
        - OurOpinionOfThem:
          - We have Pledged to Protect the same City-States. (7)
          - You (Byzantium) have gone to war in the past.
          - America's real approach to Byzantium is Hostile.
          - America have some early concerns about your (Byzantium) warmongering. (-2)
          - We have divergent Social Policies. (-3)
          - You (Byzantium) have denounced a leader America made a Declaration of Friendship with! (-11)
          - Religious differences strain your (Byzantium) relationship. (-30)
          - Your (Byzantium) spies were caught stealing from America. (-33)
          - America's leader has expressed a public opinion of Byzantium (-100).
          - America's leader has formed a private opinion of Byzantium (-100).
          - You (Byzantium) have chosen to adopt the Freedom Ideology, but America believe in Order. (-999)
        - TheirOpinionOfUs:
          - You (America) are not competing for cultural advancement.
          - We have Pledged to Protect the same City-States.
          - You (America) have no contested borders.
          - Byzantium don't want anything to do with us (America) right now.
          - We defeated Byzantium's proposal in the United Nations.
          - You (America) are competing for the favor of the same City-States!
          - Byzantium believe we are building World Wonders too aggressively!
          - Byzantium are spreading Byzantium's own religion, but you (America) converted some of their cities to your (America) religion.
          - We have divergent Social Policies.
          - Religious differences strain your (America) relationship.
          - You (America) are competing for World Wonders.
          - We have denounced each other!
          - Your (America) votes opposed Byzantium's civ's interests in the United Nations.
          - Your (America) spies were caught stealing from Byzantium.
          - You (America) have made a Declaration of Friendship with one of Byzantium's enemies!
          - You (America) have chosen to adopt the Order Ideology, but Byzantium believe in Freedom.
        - Score: 3769
        - Era: Information
        - GoldenAge: 21 turns remaining
        - Technologies: 72
        - Cities: 13
        - Population: 362
        - Territory: 532
        - Gold: 7219
        - GoldPerTurn: 17
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 42117
        - TourismPerTurn: 3955.2
        - CulturePerTurn: 5682
        - PolicyBranches:
          - Freedom: 12
          - Tradition: 6
          - Artistry: 6
          - Progress: 6
          - Authority: 2
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 8
          - Ivory: 1
          - Paper: 7
          - Pearls: 1
          - Maize: 2
          - Rice: 1
          - Gems: 1
          - Aluminum: 18
          - Bison: 5
          - Deer: 1
          - Whales: 3
          - Jade: 1
          - Dyes: 1
          - Tea: 1
          - Fish: 13
          - Cattle: 6
          - Uranium: 1
          - Horses: 1
          - Coral: 6
          - Citrus: 2
          - Crab: 1
          - Stone: 6
          - Marble: 1
          - Furs: 1
          - Oil: -2
        - FoundedReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone:
            - Distance: Far
            - Open Borders
          - Mongolia:
            - Distance: Neighbors
            - Open Borders
          - America:
            - Distance: Close
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - Open Borders
          - Austria:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 4%)
            - Denounced Them
          - Spain:
            - Distance: Neighbors
            - War (Our Score: 2%; Our War Weariness: 24%)
            - Denounced Them
        - Votes: 40
        
        ## Player 5
        - Civilization: Austria
        - Leader: Maria Theresa
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Austria) have both chosen to adopt the Order Ideology. (999)
          - America's leader has expressed a public opinion of Austria (100).
          - America's leader has formed a private opinion of Austria (100).
          - We fought together against a common foe. (48)
          - You (Austria) have denounced one of America's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - America's real approach to Austria is Friendly.
          - Religious differences strain your (Austria) relationship. (-30)
        - TheirOpinionOfUs:
          - You (America) have both chosen to adopt the Order Ideology.
          - Austria's leader has expressed a public opinion of you (America) (100).
          - You (America) have denounced one of Austria's declared enemies!
          - We have made Declarations of Friendship with the same leaders!
          - We have made a public Declaration of Friendship!
          - We have similar Social Policies.
          - We have shared embassies.
          - We have different religious beliefs.
          - Austria desire friendly relations with America.
          - Your (America) votes opposed Austria's civ's interests in the United Nations.
          - We defeated Austria's proposal in the United Nations.
        - Score: 3609
        - Era: Information
        - Technologies: 70
        - Cities: 13
        - Population: 362
        - Territory: 468
        - Gold: 122
        - GoldPerTurn: 207
        - HappinessSituation: Happy
        - HappinessPercentage: 64
        - MilitaryStrength: 30503
        - TourismPerTurn: 1397.95
        - CulturePerTurn: 2500
        - PolicyBranches:
          - Tradition: 6
          - Artistry: 6
          - Statecraft: 1
          - Order: 12
          - Progress: 6
        - ResourcesAvailable:
          - Wheat: 3
          - Sheep: 2
          - Ivory: 1
          - Paper: 4
          - Maize: 1
          - Gems: 2
          - Aluminum: 22
          - Bison: 8
          - Olives: 1
          - Deer: 12
          - Tea: 1
          - Coal: 8
          - Fish: 13
          - Cattle: 2
          - Crab: 2
          - Incense: 1
          - Stone: 1
          - Cinnamon: 10
          - Oil: 2
        - FoundedReligion: Catholicism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 2%)
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - War (Our Score: 28%; Our War Weariness: 13%)
            - Denounced Them
          - America:
            - Distance: Far
            - Declaration of Friendship
          - Germany:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 4%)
            - Denounced Them
          - Byzantium:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 4%)
            - Denounced Them
          - Spain:
            - Distance: Far
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 8
        
        ## Player 6
        - Civilization: Germany
        - Leader: Bismarck
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Germany) have denounced one of America's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - You (Germany) have gone to war in the past.
          - America's real approach to Germany is Hostile.
          - You (Germany) have denounced a leader America made a Declaration of Friendship with! (-11)
          - You (Germany) have made a Declaration of Friendship with one of America's enemies! (-13)
          - You (Germany) have made a Defensive Pact with one of America's enemies! (-15)
          - Religious differences strain your (Germany) relationship. (-30)
          - America's leader has expressed a public opinion of Germany (-100).
          - America's leader has formed a private opinion of Germany (-100).
          - You (Germany) have chosen to adopt the Autocracy Ideology, but America believe in Order. (-999)
        - TheirOpinionOfUs:
          - You (America) have denounced one of Germany's declared enemies!
          - We have Pledged to Protect the same City-States.
          - You (America) have no contested borders.
          - We have similar Social Policies.
          - Germany don't want anything to do with us (America) right now.
          - Religious differences strain your (America) relationship.
          - You (America) have made a Declaration of Friendship with one of Germany's enemies!
          - We defeated Germany's proposal in the United Nations.
          - Germany believe we are building World Wonders too aggressively!
          - Germany are jealous of our superior technology!
          - Germany's friends or allies have denounced you (America)!
          - We have denounced each other!
          - You (America) have denounced a leader Germany made a Declaration of Friendship with!
          - Your (America) votes opposed Germany's civ's interests in the United Nations.
          - You (America) have chosen to adopt the Order Ideology, but Germany believe in Autocracy.
        - Score: 2230
        - Era: Information
        - GoldenAge: 3 turns remaining
        - Technologies: 68
        - Cities: 9
        - Population: 233
        - Territory: 328
        - Gold: 235
        - GoldPerTurn: 13
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 45
        - MilitaryStrength: 4926
        - TourismPerTurn: 736.75
        - CulturePerTurn: 1671
        - PolicyBranches:
          - Fealty: 1
          - Autocracy: 6
          - Tradition: 4
          - Rationalism: 3
          - Progress: 5
          - Imperialism: 2
          - Statecraft: 3
          - Authority: 2
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 6
          - Cloves: 3
          - Ivory: 1
          - Paper: 15
          - Pearls: 9
          - Maize: 1
          - Rice: 4
          - Gems: 1
          - Salt: 1
          - Aluminum: 11
          - Lapis Lazuli: 2
          - Fish: 13
          - Deer: 3
          - Olives: 1
          - Sugar: 1
          - Jade: 3
          - Iron: 1
          - Tea: 1
          - Coal: 1
          - Cattle: 2
          - Uranium: 3
          - Horses: 9
          - Coral: 2
          - Jewelry: 1
          - Bison: 1
          - Citrus: 2
          - Stone: 4
          - Furs: 2
          - Bananas: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Denounced Them
          - Mongolia:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - America:
            - Distance: Close
            - Denounced Them
          - Austria:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 5%)
            - Denounced Them
          - Byzantium:
            - Distance: Neighbors
            - Open Borders
          - Spain:
            - Distance: Close
            - War (Our Score: 24%; Our War Weariness: 32%)
            - Denounced Them
        - Votes: 14
        - 7: Defeated Major Civilization France
        
        ## Player 22
        - Civilization: Colombo
        - Leader: City State
        - Population: 15
        - ResourcesAvailable:
          - Aluminum: 5
          - Uranium: 2
          - Incense: 1
          - Deer: 2
          - Porcelain: 1
        - MajorityReligion: Protestantism
        - Relationships:
          - The Shoshone: Friends (Influence: 49, Distance: Far)
          - Mongolia: Friends (Influence: 425, Distance: Far, Protected)
          - Germany: Friends (Influence: 429, Distance: Far, Protected)
          - America: Friends (Influence: 471, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 204, Distance: Distant)
          - Byzantium: Friends (Influence: 532, Distance: Close, Protected)
          - Spain: Neutral (Influence: -42, Distance: Neighbors)
        - Quests:
          - Construct 2 Airport buildings in non-puppet cities in your empire. (Turns remaining: 25) Potential Quest Reward: * 346 Influence * 634 Production in Capital
          - Conduct a Spy Mission against Pocatello. Potential Quest Reward: * 531 Influence * 1,273 Science
        - 23: Defeated Minor Civilization Raqmu
        
        ## Player 24
        - Civilization: M'banza-Kongo
        - Leader: City State
        - MajorAlly: Spain
        - Population: 3
        - ResourcesAvailable:
          - Deer: 1
        - Relationships:
          - The Shoshone: Neutral (Influence: -58, Distance: Neighbors)
          - Mongolia: Neutral (Influence: -60, Distance: Neighbors)
          - Germany: War (Influence: -60, Distance: Close)
          - America: Neutral (Influence: -60, Distance: Neighbors)
          - Austria: Neutral (Influence: -58, Distance: Close)
          - Byzantium: War (Influence: -60, Distance: Close)
          - Spain: Ally (Influence: 220, Distance: Close)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 25
        - Civilization: Rio de Janeiro
        - Leader: City State
        - Population: 21
        - ResourcesAvailable:
          - Fish: 3
          - Gems: 1
          - Deer: 1
        - Relationships:
          - The Shoshone: Neutral (Influence: 0, Distance: Far)
          - Mongolia: Friends (Influence: 308, Distance: Neighbors, Protected)
          - Germany: Friends (Influence: 403, Distance: Neighbors, Protected)
          - America: Friends (Influence: 142, Distance: Far)
          - Austria: Friends (Influence: 595, Distance: Close, Protected)
          - Byzantium: Friends (Influence: 505, Distance: Close, Protected)
          - Spain: Friends (Influence: 475, Distance: Close)
        - Quests:
          - They want you to demand tribute from M'banza-Kongo. Potential Quest Reward: * 129 Influence * 461 Gold
        
        ## Player 26
        - Civilization: Brussels
        - Leader: City State
        - Population: 18
        - ResourcesAvailable:
          - Fish: 2
          - Tea: 1
          - Deer: 1
          - Dyes: 1
        - Relationships:
          - The Shoshone: Friends (Influence: 200, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 407, Distance: Far, Protected)
          - Germany: Friends (Influence: 298, Distance: Far)
          - America: Friends (Influence: 156, Distance: Far)
          - Austria: Friends (Influence: 557, Distance: Neighbors, Protected)
          - Byzantium: Friends (Influence: 514, Distance: Distant)
          - Spain: Friends (Influence: 138, Distance: Distant)
        - Quests:
          - They will reward the player with the largest Culture growth. So far, the leader has 55,087 and you have 12,275. (Turns remaining: 21) Potential Quest Reward: * 318 Influence * 4 Happiness in Capital
          - Conduct a Spy Mission against Bismarck. Potential Quest Reward: * 387 Influence * 927 Science
          - They want you to demand tribute from Manila. Potential Quest Reward: * 135 Influence * 375 Gold
        
        ## Player 27
        - Civilization: Shanghai
        - Leader: City State
        - Population: 17
        - ResourcesAvailable:
          - Aluminum: 2
        - Relationships:
          - The Shoshone: Friends (Influence: 40, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 268, Distance: Neighbors, Protected)
          - Germany: Friends (Influence: 111, Distance: Far)
          - America: Friends (Influence: 119, Distance: Close)
          - Austria: Friends (Influence: 68, Distance: Neighbors, Protected)
          - Byzantium: Friends (Influence: 464, Distance: Far)
          - Spain: Friends (Influence: 114, Distance: Close)
        - Quests:
          - They want Protestantism to become the majority religion in their city. (Turns remaining: 9) Potential Quest Reward: * 155 Influence * 532 Faith
          - They want you to send them an Light Tank with at least 60 XP. (Turns remaining: 37) Potential Quest Reward: * 150 Influence * 325 Gold
        
        ## Player 28
        - Civilization: Huari
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 15
        - ResourcesAvailable:
          - Wheat: 1
          - Deer: 1
          - Fish: 2
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 380, Distance: Distant)
          - Germany: Friends (Influence: 444, Distance: Far, Protected)
          - America: Friends (Influence: 296, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 1198, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Close)
        - Quests:
          - They want you to send them an Infantry with at least 60 XP. (Turns remaining: 41) Potential Quest Reward: * 177 Influence * 387 Gold
        
        ## Player 29
        - Civilization: Warsaw
        - Leader: City State
        - MajorAlly: Germany
        - Population: 17
        - ResourcesAvailable:
          - Wheat: 1
          - Fish: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Friends (Influence: 136, Distance: Distant)
          - Mongolia: Friends (Influence: 352, Distance: Close, Protected)
          - Germany: Ally (Influence: 1045, Distance: Neighbors, Protected)
          - America: Friends (Influence: 252, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Far)
          - Byzantium: Friends (Influence: 831, Distance: Close, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - They want you to demand tribute from Kabul. Potential Quest Reward: * 140 Influence * 420 Gold
        
        ## Player 30
        - Civilization: Kabul
        - Leader: City State
        - MajorAlly: Germany
        - Population: 26
        - ResourcesAvailable:
          - Fish: 3
        - MajorityReligion: Tengriism
        - Relationships:
          - The Shoshone: Friends (Influence: 140, Distance: Distant)
          - Mongolia: Friends (Influence: 134, Distance: Far, Protected)
          - Germany: Ally (Influence: 691, Distance: Neighbors, Protected)
          - America: Friends (Influence: 204, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Friends (Influence: 1040, Distance: Distant)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - Conduct a Spy Mission against Theodora. Potential Quest Reward: * 378 Influence * 918 Science
          - They want you to demand tribute from Warsaw. Potential Quest Reward: * 120 Influence * 360 Gold
        
        ## Player 31
        - Civilization: Manila
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 24
        - ResourcesAvailable:
          - Fish: 1
          - Stone: 1
          - Sheep: 1
        - Relationships:
          - The Shoshone: Neutral (Influence: 27, Distance: Neighbors)
          - Mongolia: Friends (Influence: 37, Distance: Distant)
          - Germany: Friends (Influence: 424, Distance: Close, Protected)
          - America: Friends (Influence: 157, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Neighbors)
          - Byzantium: Ally (Influence: 922, Distance: Distant, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - They want you to send them a Mobile SAM with at least 60 XP. (Turns remaining: 36) Potential Quest Reward: * 165 Influence * 468 Gold
        - 32: Defeated Minor Civilization Argos
        
        ## Player 33
        - Civilization: Sydney
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 14
        - ResourcesAvailable:
          - Deer: 1
          - Fish: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Friends (Influence: 225, Distance: Distant)
          - Mongolia: Neutral (Influence: -56, Distance: Distant)
          - Germany: Friends (Influence: 785, Distance: Far, Protected)
          - America: Friends (Influence: 1362, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 1707, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 34
        - Civilization: Genoa
        - Leader: City State
        - MajorAlly: Germany
        - Population: 21
        - ResourcesAvailable:
          - Fish: 4
        - Relationships:
          - The Shoshone: Friends (Influence: 258, Distance: Distant)
          - Mongolia: Friends (Influence: 294, Distance: Close, Protected)
          - Germany: Ally (Influence: 858, Distance: Neighbors, Protected)
          - America: Friends (Influence: 243, Distance: Far)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Friends (Influence: 824, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Far)
        - Quests:
          - Conduct a Spy Mission against Genghis Khan. Potential Quest Reward: * 423 Influence * 1,053 Science
          - They want you to generate a Great Artist. (Turns remaining: 38) Potential Quest Reward: * 178 Influence * 458 Culture
        
        ## Player 35
        - Civilization: Assur
        - Leader: City State
        - MajorAlly: Germany
        - Population: 20
        - ResourcesAvailable:
          - Fish: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 131, Distance: Distant, Protected)
          - Germany: Ally (Influence: 684, Distance: Neighbors, Protected)
          - America: Friends (Influence: 34, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Friends (Influence: 928, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Distant)
        - Quests:
          - They want you to demand tribute from Huari. Potential Quest Reward: * 140 Influence * 420 Gold
          - They want you to generate a Great Engineer. (Turns remaining: 24) Potential Quest Reward: * 206 Influence * 486 Culture
        
        ## Player 36
        - Civilization: Luba
        - Leader: City State
        - Population: 20
        - ResourcesAvailable:
          - Olives: 1
          - Iron: 2
        - MajorityReligion: Protestantism
        - Relationships:
          - The Shoshone: Neutral (Influence: 5, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 307, Distance: Close, Protected)
          - Germany: Friends (Influence: 209, Distance: Far)
          - America: Friends (Influence: 199, Distance: Close)
          - Austria: Friends (Influence: 707, Distance: Neighbors, Protected)
          - Byzantium: Friends (Influence: 505, Distance: Far)
          - Spain: Friends (Influence: 81, Distance: Far)
        - Quests:
          - They want you to start a land or sea trade route to their city. (Turns remaining: 28) Potential Quest Reward: * 246 Influence * 316 Food in Capital
        
        ## Player 37
        - Civilization: Shedet
        - Leader: City State
        - MajorAlly: Byzantium
        - Population: 10
        - ResourcesAvailable:
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Shoshone: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 249, Distance: Distant)
          - Germany: Friends (Influence: 159, Distance: Far)
          - America: Friends (Influence: 72, Distance: Distant)
          - Austria: War (Influence: -60, Distance: Distant)
          - Byzantium: Ally (Influence: 662, Distance: Neighbors, Protected)
          - Spain: War (Influence: -60, Distance: Far)
        - Quests:
          - They want you to liberate the city of Raqmu. (Turns remaining: 34) Potential Quest Reward: * 200 Influence * 4 Happiness in Capital
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: The Shoshone
        
        ### Moson Kahni
        - ID: 1057
        - X: 55
        - Y: 26
        - Population: 57
        - DefenseStrength: 75
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Ironworks
          - Oracle
          - Great Wall
          - Himeji Castle
          - Statue of Liberty
          - Temple of Artemis
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Summer Palace
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Te-Moak
        - ID: 1664
        - X: 59
        - Y: 28
        - Population: 43
        - DefenseStrength: 76
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
          - Giorgio Armeier Headquarters
        
        ### Agaidika
        - ID: 1828
        - X: 57
        - Y: 33
        - Population: 39
        - MajorityReligion: Tengriism
        - DefenseStrength: 67
        - IsCoastal: true
        - Wonders:
          - Bletchley Park
        
        ### Goshute
        - ID: 2084
        - X: 53
        - Y: 32
        - Population: 40
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 76
        - Wonders:
          - Chartered Company
          - Imperial College
          - Royal Collection
        
        ### Pohokwi
        - ID: 2787
        - X: 61
        - Y: 33
        - Population: 27
        - DefenseStrength: 75
        - IsCoastal: true
        
        ### Raqmu
        - ID: 6611
        - X: 55
        - Y: 19
        - Population: 30
        - DefenseStrength: 75
        - IsOccupied: true
        - IsCoastal: true
        
        ### Hukandeka
        - ID: 6655
        - X: 75
        - Y: 40
        - Population: 23
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 85
        - IsCoastal: true
        
        ## Player: Mongolia
        
        ### Karakorum
        - ID: 1058
        - X: 40
        - Y: 28
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 86
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Chartered Company
          - Ironworks
          - Imperial College
          - Pentagon
          - Mausoleum of Halicarnassus
          - Alhambra
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - Consulate
          - Firaxite Materials Headquarters
        
        ### Beshbalik
        - ID: 1293
        - X: 43
        - Y: 25
        - Population: 24
        - MajorityReligion: Tengriism
        - DefenseStrength: 78
        - Wonders:
          - Circus Maximus
        
        ### Hsia
        - ID: 2245
        - X: 37
        - Y: 40
        - Population: 24
        - MajorityReligion: Tengriism
        - DefenseStrength: 76
        - IsCoastal: true
        - Wonders:
          - Red Fort
        
        ### Old Sarai
        - ID: 2518
        - X: 37
        - Y: 45
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 80
        - IsCoastal: true
        
        ### New Sarai
        - ID: 4477
        - X: 36
        - Y: 36
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Tabriz
        - ID: 4478
        - X: 37
        - Y: 49
        - Population: 24
        - MajorityReligion: Tengriism
        - DefenseStrength: 80
        - IsCoastal: true
        - Wonders:
          - Royal Collection
        
        ### Paris
        - ID: 4587
        - X: 42
        - Y: 37
        - Population: 32
        - MajorityReligion: Tengriism
        - DefenseStrength: 80
        - Health: 64%
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Petra
        
        ### Otrar
        - ID: 18359
        - X: 45
        - Y: 32
        - Population: 12
        - MajorityReligion: Tengriism
        - DefenseStrength: 78
        
        ### Turfan
        - ID: 19902
        - X: 40
        - Y: 34
        - Population: 25
        - MajorityReligion: Tengriism
        - DefenseStrength: 82
        - IsCoastal: true
        
        ## Player: America
        
        ### Washington
        - ID: 1059
        - X: 47
        - Y: 9
        - Population: 28
        - MajorityReligion: Protestantism
        - DefenseStrength: 110
        - FoodStored: 1792
        - FoodPerTurn: 17
        - ProductionStored: 891
        - ProductionPerTurn: 270
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 214
        - SciencePerTurn: 445
        - CulturePerTurn: 280
        - FaithPerTurn: 93
        - TourismPerTurn: 98.25
        - HappinessDelta: 5
        - BuildingCount: 49
        - ImportantBuildings:
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Homestead
        - Wonders:
          - Heroic Epic
          - National Monument
          - Chartered Company
          - Stonehenge
          - Pyramids
          - Notre Dame
          - Forbidden Palace
          - Taj Mahal
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - Palace of Culture and Science
          - Roman Forum
          - Karlstejn
          - West Point
          - Grand Canal
          - Royal Guardhouse
          - Court Chapel
          - Royal Astrologer
          - Holy Council
        - GreatWorkCount: 6
        
        ### New York
        - ID: 1224
        - X: 49
        - Y: 14
        - Population: 27
        - MajorityReligion: Protestantism
        - DefenseStrength: 107
        - IsCoastal: true
        - FoodStored: 1494
        - FoodPerTurn: 2
        - ProductionStored: 1780
        - ProductionPerTurn: 358
        - CurrentProduction: Apollo Program
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 158
        - SciencePerTurn: 223
        - CulturePerTurn: 143
        - FaithPerTurn: 42
        - TourismPerTurn: 136
        - HappinessDelta: -3
        - BuildingCount: 56
        - ImportantBuildings:
          - Seaport
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Hotel
          - Caravansary
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Homestead
        - GreatWorkCount: 6
        
        ### Boston
        - ID: 1409
        - X: 49
        - Y: 19
        - Population: 25
        - MajorityReligion: Protestantism
        - DefenseStrength: 101
        - FoodStored: 1186
        - FoodPerTurn: 30
        - ProductionStored: 785
        - ProductionPerTurn: 233
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 7
        - GoldPerTurn: 163
        - SciencePerTurn: 364
        - CulturePerTurn: 198
        - FaithPerTurn: 53
        - TourismPerTurn: 143.25
        - HappinessDelta: -4
        - BuildingCount: 54
        - ImportantBuildings:
          - Water Mill
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Writers' Guild
          - Artists' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Homestead
        - Wonders:
          - Ironworks
          - Imperial College
        - GreatWorkCount: 8
        
        ### Philadelphia
        - ID: 1649
        - X: 48
        - Y: 23
        - Population: 25
        - DefenseStrength: 111
        - FoodStored: 1066
        - FoodPerTurn: 65
        - ProductionStored: 1283
        - ProductionPerTurn: 308
        - CurrentProduction: Airport
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 122
        - SciencePerTurn: 278
        - CulturePerTurn: 137
        - FaithPerTurn: 19
        - TourismPerTurn: 83
        - HappinessDelta: 3
        - BuildingCount: 52
        - ImportantBuildings:
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Police Station
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
          - Homestead
        - Wonders:
          - Circus Maximus
          - Machu Picchu
          - National Intelligence Agency
          - Uffizi
        - GreatWorkCount: 4
        
        ### Atlanta
        - ID: 1751
        - X: 51
        - Y: 7
        - Population: 25
        - MajorityReligion: Protestantism
        - DefenseStrength: 104
        - IsCoastal: true
        - FoodStored: 1393
        - FoodPerTurn: 42
        - ProductionStored: 492
        - ProductionPerTurn: 286
        - CurrentProduction: Heavy Bomber
        - ProductionTurnsLeft: 2
        - GoldPerTurn: 159
        - SciencePerTurn: 233
        - CulturePerTurn: 129
        - FaithPerTurn: 32
        - TourismPerTurn: 91.75
        - HappinessDelta: 2
        - BuildingCount: 53
        - ImportantBuildings:
          - Seaport
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Writers' Guild
          - Hotel
          - Caravansary
          - Chancery
          - Agribusiness
          - Coaling Station
          - Homestead
        - Wonders:
          - School of Philosophy
          - Grand Temple
          - Independence Hall
          - Hexxon Refineries Headquarters
        - GreatWorkCount: 4
        
        ### Chicago
        - ID: 2601
        - X: 52
        - Y: 13
        - Population: 23
        - MajorityReligion: Protestantism
        - DefenseStrength: 101
        - IsCoastal: true
        - FoodStored: 903
        - FoodPerTurn: 21
        - ProductionStored: 305
        - ProductionPerTurn: 165
        - CurrentProduction: Police Station
        - ProductionTurnsLeft: 7
        - GoldPerTurn: 130
        - SciencePerTurn: 207
        - CulturePerTurn: 112
        - FaithPerTurn: 42
        - TourismPerTurn: 34.25
        - HappinessDelta: -4
        - BuildingCount: 53
        - ImportantBuildings:
          - Seaport
          - Windmill
          - Customs House
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Military Base
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Strategic Defense System
          - Constabulary
          - Writers' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Coaling Station
          - Wire Service
          - Homestead
        - GreatWorkCount: 0
        
        ## Player: Spain
        
        ### Madrid
        - ID: 1060
        - X: 43
        - Y: 19
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 52
        - Health: 43%
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Royal Collection
          - Hagia Sophia
          - Chichen Itza
          - Terracotta Army
          - Borobudur
          - Scrivener's Office
          - Printing Press
          - Palace of Culture and Science
          - Royal Guardhouse
          - Apostolic Palace
        
        ### Barcelona
        - ID: 1276
        - X: 42
        - Y: 13
        - Population: 30
        - MajorityReligion: Buddhism
        - DefenseStrength: 78
        - IsCoastal: true
        - Wonders:
          - Grand Temple
        
        ### Toledo
        - ID: 3336
        - X: 42
        - Y: 9
        - Population: 27
        - DefenseStrength: 77
        - IsCoastal: true
        
        ### Tiflis
        - ID: 10390
        - X: 36
        - Y: 7
        - Population: 19
        - MajorityReligion: Buddhism
        - DefenseStrength: 79
        - Health: 84%
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Byzantium
        
        ### Constantinople
        - ID: 1061
        - X: 21
        - Y: 17
        - Population: 54
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 105
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - National Monument
          - Chartered Company
          - Imperial College
          - Royal Collection
          - National Intelligence Agency
          - CN Tower
          - University of Sankore
          - Neuschwanstein
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - International Finance Center
          - Olympic Village
          - United Nations
          - Consulate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Great Altar
        
        ### Adrianople
        - ID: 1237
        - X: 22
        - Y: 12
        - Population: 28
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Ironworks
          - Grand Temple
        
        ### Nicaea
        - ID: 1567
        - X: 19
        - Y: 7
        - Population: 29
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
        
        ### Antioch
        - ID: 1892
        - X: 26
        - Y: 14
        - Population: 28
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - IsCoastal: true
        - Wonders:
          - Centaurus Extractors Headquarters
        
        ### Varna
        - ID: 2070
        - X: 29
        - Y: 17
        - Population: 29
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 101
        - IsCoastal: true
        
        ### Ohrid
        - ID: 2582
        - X: 30
        - Y: 10
        - Population: 30
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 99
        - IsCoastal: true
        - Wonders:
          - Sydney Opera House
        
        ### Nicomedia
        - ID: 2907
        - X: 16
        - Y: 16
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 101
        - IsCoastal: true
        
        ### Trebizond
        - ID: 4411
        - X: 12
        - Y: 13
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 103
        - IsCoastal: true
        
        ### Cherson
        - ID: 4922
        - X: 28
        - Y: 5
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 103
        - IsCoastal: true
        
        ### Sardica
        - ID: 5153
        - X: 17
        - Y: 10
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Ani
        - ID: 6627
        - X: 25
        - Y: 20
        - Population: 24
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 107
        - IsCoastal: true
        
        ### Dyrrachium
        - ID: 8380
        - X: 9
        - Y: 11
        - Population: 24
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 107
        - IsCoastal: true
        
        ### Edessa
        - ID: 19610
        - X: 38
        - Y: 21
        - Population: 12
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 76
        - IsCoastal: true
        
        ## Player: Austria
        
        ### Vienna
        - ID: 1062
        - X: 52
        - Y: 44
        - Population: 55
        - MajorityReligion: Catholicism
        - DefenseStrength: 105
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Great Lighthouse
          - Great Library
          - Hanging Gardens
          - Porcelain Tower
          - Sistine Chapel
          - Kremlin
          - Brandenburg Gate
          - Eiffel Tower
          - Statue of Zeus
          - National Intelligence Agency
          - Leaning Tower of Pisa
          - Globe Theatre
          - Scrivener's Office
          - Foreign Bureau
          - Palace of Culture and Science
          - Ballhausplatz
          - Soho Foundry
          - The Motherland Calls
          - Empire State Building
          - Crystal Palace
          - Menin Gate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Celestial Throne
          - Trader Sid's Headquarters
        
        ### Salzburg
        - ID: 1230
        - X: 47
        - Y: 44
        - Population: 29
        - DefenseStrength: 99
        - IsCoastal: true
        
        ### Graz
        - ID: 1381
        - X: 52
        - Y: 40
        - Population: 31
        - MajorityReligion: Catholicism
        - DefenseStrength: 92
        - IsCoastal: true
        - Wonders:
          - Grand Temple
        
        ### Linz
        - ID: 1853
        - X: 45
        - Y: 40
        - Population: 29
        - MajorityReligion: Catholicism
        - DefenseStrength: 104
        - IsCoastal: true
        
        ### Klagenfurt
        - ID: 2283
        - X: 50
        - Y: 48
        - Population: 29
        - MajorityReligion: Catholicism
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Bregenz
        - ID: 2609
        - X: 54
        - Y: 47
        - Population: 28
        - MajorityReligion: Catholicism
        - DefenseStrength: 99
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Royal Collection
        
        ### Innsbruck
        - ID: 3898
        - X: 60
        - Y: 47
        - Population: 29
        - MajorityReligion: Catholicism
        - DefenseStrength: 70
        - IsCoastal: true
        - Wonders:
          - Louvre
        
        ### Kitzbuhel
        - ID: 4416
        - X: 68
        - Y: 46
        - Population: 26
        - MajorityReligion: Catholicism
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### St. Polten
        - ID: 4980
        - X: 64
        - Y: 47
        - Population: 27
        - MajorityReligion: Catholicism
        - DefenseStrength: 70
        - IsCoastal: true
        - Wonders:
          - Cristo Redentor
        
        ### Washakie
        - ID: 14850
        - X: 64
        - Y: 37
        - Population: 24
        - MajorityReligion: Catholicism
        - DefenseStrength: 97
        - IsOccupied: true
        - IsCoastal: true
        
        ### Timbisha
        - ID: 16211
        - X: 64
        - Y: 43
        - Population: 25
        - MajorityReligion: Catholicism
        - DefenseStrength: 87
        - IsPuppet: true
        - IsCoastal: true
        
        ### Villach
        - ID: 17332
        - X: 68
        - Y: 41
        - Population: 16
        - MajorityReligion: Catholicism
        - DefenseStrength: 105
        - IsCoastal: true
        
        ### Argos
        - ID: 19876
        - X: 68
        - Y: 34
        - Population: 14
        - MajorityReligion: Catholicism
        - DefenseStrength: 36
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Germany
        
        ### Berlin
        - ID: 1063
        - X: 19
        - Y: 30
        - Population: 39
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 74
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Circus Maximus
          - Ironworks
          - State Treasury
          - Royal Guardhouse
          - Royal Astrologer
        
        ### Hamburg
        - ID: 1247
        - X: 18
        - Y: 35
        - Population: 29
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 68
        - IsCoastal: true
        - Wonders:
          - Chartered Company
          - Angkor Wat
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
        
        ### Munich
        - ID: 1424
        - X: 16
        - Y: 26
        - Population: 28
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 96
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - National Monument
          - Imperial College
          - Royal Collection
          - Colossus
          - Grand Temple
          - Prora
          - Hall of Honor
        
        ### Cologne
        - ID: 3600
        - X: 12
        - Y: 27
        - Population: 24
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 73
        - IsCoastal: true
        
        ### Frankfurt
        - ID: 4137
        - X: 13
        - Y: 31
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 92
        - IsCoastal: true
        
        ### Aachen
        - ID: 4629
        - X: 21
        - Y: 41
        - Population: 26
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 81
        - IsCoastal: true
        
        ### Dortmund
        - ID: 5096
        - X: 26
        - Y: 30
        - Population: 25
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 78
        - IsCoastal: true
        
        ### Cordoba
        - ID: 13676
        - X: 36
        - Y: 26
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 95
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Nalanda
          - Civilized Jewelers Headquarters
        
        ### Eisenstadt
        - ID: 16156
        - X: 5
        - Y: 37
        - Population: 16
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 72
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: City-States
        
        ### Colombo
        - ID: 1065
        - X: 43
        - Y: 4
        - Population: 15
        - MajorityReligion: Protestantism
        - DefenseStrength: 84
        
        ### M'banza-Kongo
        - ID: 20411
        - X: 47
        - Y: 29
        - Population: 3
        - DefenseStrength: 78
        - Health: 64%
        
        ### Rio de Janeiro
        - ID: 1068
        - X: 35
        - Y: 32
        - Population: 21
        - DefenseStrength: 97
        - IsCoastal: true
        
        ### Brussels
        - ID: 4219
        - X: 64
        - Y: 31
        - Population: 18
        - DefenseStrength: 82
        - IsCoastal: true
        
        ### Shanghai
        - ID: 1070
        - X: 49
        - Y: 34
        - Population: 17
        - DefenseStrength: 70
        
        ### Huari
        - ID: 1071
        - X: 23
        - Y: 6
        - Population: 15
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 96
        - IsCoastal: true
        
        ### Warsaw
        - ID: 1072
        - X: 25
        - Y: 34
        - Population: 17
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 97
        - IsCoastal: true
        
        ### Kabul
        - ID: 1073
        - X: 21
        - Y: 46
        - Population: 26
        - MajorityReligion: Tengriism
        - DefenseStrength: 102
        - IsCoastal: true
        
        ### Manila
        - ID: 1074
        - X: 73
        - Y: 34
        - Population: 24
        - DefenseStrength: 104
        - IsCoastal: true
        
        ### Sydney
        - ID: 1076
        - X: 9
        - Y: 5
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 90
        - IsCoastal: true
        
        ### Genoa
        - ID: 1077
        - X: 28
        - Y: 24
        - Population: 21
        - DefenseStrength: 102
        - IsCoastal: true
        
        ### Assur
        - ID: 1078
        - X: 15
        - Y: 21
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 95
        - IsCoastal: true
        
        ### Luba
        - ID: 1079
        - X: 54
        - Y: 36
        - Population: 20
        - MajorityReligion: Protestantism
        - DefenseStrength: 90
        
        ### Shedet
        - ID: 1080
        - X: 15
        - Y: 3
        - Population: 10
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 89
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - CityBombard:
          - Rocket Artillery:
            - Strength: 37
            - RangedStrength: 75
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
          - Krupp Gun:
            - Strength: 27
            - RangedStrength: 55
        - FastAttack:
          - Landship:
            - Strength: 60
        - Defense:
          - Infantry:
            - Strength: 62
        - Counter:
          - Anti-Aircraft Gun:
            - Strength: 40
        - Ranged:
          - Light Tank:
            - Strength: 58
            - RangedStrength: 52
          - Machine Gun:
            - Strength: 45
            - RangedStrength: 58
          - Comanche Rider:
            - Strength: 41
            - RangedStrength: 35
        - Explore:
          - Tank:
            - Strength: 75
        - AttackSea:
          - Fleet Destroyer:
            - Strength: 80
        - AssaultSea:
          - Battleship:
            - Strength: 60
            - RangedStrength: 75
        - AttackAir:
          - Heavy Bomber:
            - RangedStrength: 65
          - Bomber:
            - RangedStrength: 50
        - DefenseAir:
          - Fighter:
            - RangedStrength: 60
          - Triplane:
            - RangedStrength: 45
        - Paradrop:
          - Special Forces:
            - Strength: 65
        
        ## Enemy Land Zone 1057
        - ZoneValue: 42
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 3156
        - FriendlyStrength: 982
        - City: Moson Kahni
        - AreaID: 5
        - Plots: 26
        - CenterX: 54
        - CenterY: 26
        - Units:
          - The Shoshone:
            - Anti-Aircraft Gun: 1
            - Machine Gun: 2
            - Comanche Rider: 1
        - Neighbors:
          - 20411
          - 1649
          - 6611
          - -6611
        
        ## Friendly Land Zone 1059
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 1408
        - FriendlyStrength: 1581
        - City: Washington
        - AreaID: 5
        - Plots: 26
        - CenterX: 47
        - CenterY: 9
        - Units:
          - America:
            - Machine Gun: 1
        - Neighbors:
          - 1065
          - 3336
          - 1276
          - 1224
          - 1751
        
        ## Neutral Land Zone 1060
        - ZoneValue: 360
        - Dominance: Friendly
        - NeutralStrength: 2652
        - FriendlyStrength: 927
        - City: Madrid
        - AreaID: 5
        - Plots: 29
        - CenterX: 44
        - CenterY: 19
        - Units:
          - Spain:
            - Special Forces: 1
        - Neighbors:
          - 1276
          - 1293
          - 1224
          - 1409
          - 1649
        
        ## Neutral Land Zone 1061
        - ZoneValue: 66
        - NeutralStrength: 2062
        - City: Constantinople
        - AreaID: 11
        - Plots: 19
        - CenterX: 21
        - CenterY: 17
        - Units:
          - Byzantium:
            - Rocket Artillery: 1
            - Artillery: 3
            - Special Forces: 1
            - Landship: 1
            - Machine Gun: 5
        - Neighbors:
          - 1237
        
        ## Neutral Land Zone 1065
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 1796
        - FriendlyStrength: 203
        - City: Colombo
        - AreaID: 5
        - Plots: 27
        - CenterX: 45
        - CenterY: 4
        - Units:
          - City-State Colombo:
            - Light Tank: 1
            - Infantry: 5
            - Machine Gun: 2
        - Neighbors:
          - 3336
          - 1059
          - 100003
          - 1751
        
        ## Neutral Land Zone 1074
        - ZoneValue: 9
        - Dominance: Enemy
        - EnemyStrength: 220
        - NeutralStrength: 1533
        - City: Manila
        - AreaID: 69
        - Plots: 9
        - CenterX: 73
        - CenterY: 34
        - Units:
          - City-State Manila:
            - Infantry: 3
            - Machine Gun: 1
        - Neighbors:
          - -1074
        
        ## Neutral Land Zone 1076
        - ZoneValue: 3
        - NeutralStrength: 2842
        - City: Sydney
        - AreaID: 1
        - Plots: 28
        - CenterX: 10
        - CenterY: 5
        - Units:
          - Byzantium:
            - Infantry: 1
          - City-State Sydney:
            - Anti-Aircraft Gun: 1
            - Infantry: 1
            - Machine Gun: 3
        - Neighbors:
          - -1076
          - -8380
        
        ## Friendly Land Zone 1224
        - ZoneValue: 30
        - Dominance: Friendly
        - NeutralStrength: 498
        - FriendlyStrength: 1855
        - City: New York
        - AreaID: 5
        - Plots: 18
        - CenterX: 48
        - CenterY: 14
        - Units:
          - America:
            - Rocket Artillery: 1
            - Fighter: 2
        - Neighbors:
          - 1276
          - 1060
          - 1059
          - 1409
          - 2601
          - -2601
        
        ## Neutral Land Zone 1237
        - ZoneValue: 21
        - NeutralStrength: 1482
        - City: Adrianople
        - AreaID: 11
        - Plots: 15
        - CenterX: 21
        - CenterY: 13
        - Units:
          - Byzantium:
            - Machine Gun: 1
        - Neighbors:
          - 1061
        
        ## Neutral Land Zone 1276
        - ZoneValue: 60
        - Dominance: Friendly
        - NeutralStrength: 2382
        - FriendlyStrength: 618
        - City: Barcelona
        - AreaID: 5
        - Plots: 20
        - CenterX: 43
        - CenterY: 14
        - Units:
          - Spain:
            - Artillery: 1
            - Infantry: 2
            - Special Forces: 1
            - Machine Gun: 1
        - Neighbors:
          - 1060
          - 3336
          - 1059
          - 1224
        
        ## Neutral Land Zone 1293
        - ZoneValue: 48
        - Dominance: Friendly
        - NeutralStrength: 2967
        - FriendlyStrength: 1702
        - City: Beshbalik
        - AreaID: 5
        - Plots: 30
        - CenterX: 43
        - CenterY: 25
        - Units:
          - Spain:
            - Special Forces: 1
            - Machine Gun: 1
          - Mongolia:
            - Anti-Aircraft Gun: 1
            - Infantry: 1
            - Bomber: 1
            - Machine Gun: 5
          - Byzantium:
            - Light Tank: 1
          - Germany:
            - Anti-Aircraft Gun: 1
            - Krupp Gun: 1
        - Neighbors:
          - 1060
          - 18359
          - 20411
          - 1649
        
        ## Friendly Land Zone 1409
        - ZoneValue: 30
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 834
        - NeutralStrength: 295
        - FriendlyStrength: 2817
        - City: Boston
        - AreaID: 5
        - Plots: 28
        - CenterX: 50
        - CenterY: 19
        - Units:
          - America:
            - Fighter: 1
            - Infantry: 1
        - Neighbors:
          - 1060
          - 1649
          - 1224
          - -2601
          - 6611
          - -6611
        
        ## Friendly Land Zone 1649
        - ZoneValue: 30
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 1121
        - NeutralStrength: 1120
        - FriendlyStrength: 2623
        - City: Philadelphia
        - AreaID: 5
        - Plots: 30
        - CenterX: 49
        - CenterY: 23
        - Units:
          - The Shoshone:
            - Machine Gun: 1
          - America:
            - Rocket Artillery: 2
            - Fighter: 2
            - Infantry: 1
            - Machine Gun: 3
        - Neighbors:
          - 1060
          - 1293
          - 1409
          - 20411
          - 1057
        
        ## Friendly Land Zone 1751
        - ZoneValue: 30
        - Dominance: Friendly
        - NeutralStrength: 143
        - FriendlyStrength: 1598
        - City: Atlanta
        - AreaID: 5
        - Plots: 24
        - CenterX: 51
        - CenterY: 6
        - Units:
          - America:
            - Fighter: 1
            - Special Forces: 1
        - Neighbors:
          - 1065
          - 1059
          - 100003
          - 2601
        
        ## Friendly Land Zone 2601
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 477
        - FriendlyStrength: 1898
        - City: Chicago
        - AreaID: 5
        - Plots: 13
        - CenterX: 52
        - CenterY: 12
        - Units:
          - America:
            - Rocket Artillery: 1
            - Fighter: 2
            - Infantry: 1
        - Neighbors:
          - 1224
          - 1751
          - -2601
        
        ## Neutral Land Zone 3336
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 2368
        - FriendlyStrength: 203
        - City: Toledo
        - AreaID: 5
        - Plots: 14
        - CenterX: 43
        - CenterY: 9
        - Units:
          - Spain:
            - Artillery: 1
            - Special Forces: 1
            - Machine Gun: 1
          - City-State Colombo:
            - Infantry: 1
        - Neighbors:
          - 1065
          - 1276
          - 1059
        
        ## Neutral Land Zone 4629
        - ZoneValue: 12
        - NeutralStrength: 672
        - City: Aachen
        - AreaID: 84
        - Plots: 9
        - CenterX: 22
        - CenterY: 42
        - Units:
          - Germany:
            - Heavy Bomber: 1
            - Tank: 1
        
        ## Enemy Land Zone 6611
        - ZoneValue: 36
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2071
        - FriendlyStrength: 512
        - City: Raqmu
        - AreaID: 5
        - Plots: 25
        - CenterX: 55
        - CenterY: 20
        - Units:
          - The Shoshone:
            - Triplane: 2
            - Machine Gun: 3
        - Neighbors:
          - 1409
          - -6611
          - 1057
        
        ## Neutral Land Zone 8380
        - ZoneValue: 3
        - NeutralStrength: 2187
        - City: Dyrrachium
        - AreaID: 2
        - Plots: 8
        - CenterX: 10
        - CenterY: 11
        - Units:
          - Byzantium:
            - Tank: 1
            - Machine Gun: 2
        - Neighbors:
          - -8380
          - -1076
        
        ## Neutral Land Zone 18359
        - ZoneValue: 12
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 157
        - NeutralStrength: 3515
        - FriendlyStrength: 818
        - City: Otrar
        - AreaID: 5
        - Plots: 22
        - CenterX: 44
        - CenterY: 32
        - Units:
          - Mongolia:
            - Machine Gun: 1
        - Neighbors:
          - 1293
          - 20411
        
        ## Neutral Land Zone 20411
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 999
        - NeutralStrength: 2471
        - FriendlyStrength: 1846
        - City: M'banza-Kongo
        - AreaID: 5
        - Plots: 33
        - CenterX: 48
        - CenterY: 28
        - Units:
          - The Shoshone:
            - Machine Gun: 1
          - Mongolia:
            - Tank: 1
            - Artillery: 1
            - Machine Gun: 2
          - City-State M'banza-Kongo:
            - Anti-Aircraft Gun: 1
          - America:
            - Rocket Artillery: 1
            - Machine Gun: 1
        - Neighbors:
          - 18359
          - 1293
          - 1649
          - 1057
        
        ## Neutral Land Zone 100003
        - ZoneValue: 3
        - NeutralStrength: 102
        - AreaID: 5
        - Plots: 1
        - CenterX: 48
        - CenterY: 2
        - Units:
          - City-State Colombo:
            - Infantry: 1
        - Neighbors:
          - 1065
          - 1751
        
        ## Neutral Sea Zone -1074
        - ZoneValue: 3
        - Dominance: Enemy
        - EnemyStrength: 284
        - NeutralStrength: 2278
        - City: Manila
        - AreaID: 0
        - Plots: 51
        - CenterX: 74
        - CenterY: 33
        - Units:
          - Austria:
            - Fleet Destroyer: 2
        - Neighbors:
          - 1074
        
        ## Neutral Sea Zone -1076
        - ZoneValue: 1
        - NeutralStrength: 2360
        - City: Sydney
        - AreaID: 0
        - Plots: 40
        - CenterX: 8
        - CenterY: 4
        - Units:
          - Byzantium:
            - Infantry: 1
          - City-State Sydney:
            - Battleship: 1
        - Neighbors:
          - 1076
          - -8380
          - 8380
        
        ## Neutral Sea Zone -8380
        - ZoneValue: 5
        - NeutralStrength: 2093
        - City: Dyrrachium
        - AreaID: 0
        - Plots: 41
        - CenterX: 8
        - CenterY: 12
        - Units:
          - City-State Sydney:
            - Fleet Destroyer: 1
        - Neighbors:
          - -1076
          - 1076
          - 8380
        
        ## Friendly Sea Zone -2601
        - ZoneValue: 4
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 912
        - FriendlyStrength: 1246
        - City: Chicago
        - AreaID: 0
        - Plots: 33
        - CenterX: 54
        - CenterY: 13
        - Units:
          - America:
            - Fleet Destroyer: 1
        - Neighbors:
          - 1224
          - 2601
          - 1409
          - -6611
        
        ## Enemy Sea Zone -6611
        - ZoneValue: 12
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 2066
        - FriendlyStrength: 297
        - City: Raqmu
        - AreaID: 0
        - Plots: 32
        - CenterX: 57
        - CenterY: 18
        - Units:
          - The Shoshone:
            - Comanche Rider: 1
            - Fleet Destroyer: 4
        - Neighbors:
          - 1409
          - -2601
          - 6611
          - 1057
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 451
        
        ### 0
        - Type: CityInvestedBuilding
        - BuildingClass: Stadium
        - Invested: true
        - City:
          - Name: Madrid
          - Population: 37
          - ID: 1060
        - Player: 3: Spain
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Infantry
          - ID: 20487
        - Player: 3: Spain
        - Desert Land 42,19:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Academy
          - Route: Railroad
          - Feature: Flood Plains
        
        ### 2
        - Type: UnitCreated
        - UnitType: Infantry
        - Player: 3: Spain
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Infantry
          - ID: 20487
        - Desert Land 42,19:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Academy
          - Route: Railroad
          - Feature: Flood Plains
        
        ### 3
        - Type: CityTrained
        - Player: 3: Spain
        - City:
          - Name: Madrid
          - Population: 37
          - ID: 1060
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Infantry
          - ID: 20487
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19598
        - Player: 3: Spain
        - Plots:
          - Mountain Mountain 44,28:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Land 44,29:
            - Owner: Mongolia
            - Route: Railroad
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18519
        - Player: 3: Spain
        - Plots:
          - Plains Hills 43,16:
            - Owner: Spain
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 43,17:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 44,18:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 43,19:
            - Owner: Spain
            - CityID: 1060
            - Population: 37
            - IsRiver: true
            - City: Madrid
            - Religion: Buddhism
            - Route: Railroad
        
        ### 6
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 3: Spain
        - OriginCity:
          - Name: Madrid
          - Population: 37
          - ID: 1060
        - DestinationCity:
          - Name: Colombo
          - Population: 15
          - ID: 1065
        - DestinationPlayer: 22
        - Connection: Food
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 20488
        - Player: 3: Spain
        - Desert Land 43,19:
          - Owner: Spain
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Madrid
          - Religion: Buddhism
          - Route: Railroad
        
        ### 8
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 3: Spain
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20488
        - Desert Land 43,19:
          - Owner: Spain
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Madrid
          - Religion: Buddhism
          - Route: Railroad
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19474
        - Player: 3: Spain
        - Plots:
          - Desert Land 54,19:
            - Owner: The Shoshone
            - Feature: Oasis
          - Plains Hills 53,19:
            - Owner: America
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 52,19:
            - Owner: America
            - Improvement: Citadel
            - Route: Railroad
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19242
        - Player: 3: Spain
        - Plots:
          - Grass Land 46,23:
            - Owner: America
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 47,23:
            - Owner: America
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Tundra Hills 48,23:
            - Owner: America
            - CityID: 1649
            - Population: 25
            - City: Philadelphia
            - Route: Railroad
          - Tundra Hills 49,23:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19475
        - Player: 3: Spain
        - Plots:
          - Plains Land 50,29:
            - Owner: The Shoshone
            - IsRiver: true
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 51,30:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19664
        - Player: 3: Spain
        - Grass Land 42,23:
          - Owner: Mongolia
          - IsRiver: true
          - Resource: Deer
          - Improvement: Camp
          - Route: Road
          - Feature: Forest
        
        ### 13
        - Type: PlayerPlunderedTradeRoute
        - PlunderGoldValue: 700
        - Domain: 2
        - DestinationCity:
          - Name: Beshbalik
          - Population: 24
          - ID: 1293
        - DestinationOwner: 1: Mongolia
        - OriginOwner: 3: Spain
        - PlunderingUnit:
          - Level: 4
          - Health: 68%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18497
        - OriginCity:
          - Name: Madrid
          - Population: 37
          - ID: 1060
        - PlunderingPlayer: 6: Germany
        - Connection: Food
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20088
        - Player: 3: Spain
        - Plots:
          - Grass Hills 54,25:
            - Owner: The Shoshone
            - Improvement: Academy
            - Route: Railroad
          - Grass Hills 54,24:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 53,24:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
        
        ### 15
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Infantry
          - ID: 20487
        - Player: 3: Spain
        - Promotions:
          - Drill I
          - Cover I
          - Shock I
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20372
        - Player: 3: Spain
        - Plains Land 43,14:
          - Owner: Spain
          - Resource: Maize
          - Improvement: Town
          - Route: Railroad
        
        ### 17
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 30%
          - AI: Defense
          - Unit: Infantry
          - ID: 19748
        - Player: 3: Spain
        - Plots:
          - Desert Land 42,21:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 43,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 43,19:
            - Owner: Spain
            - CityID: 1060
            - Population: 37
            - IsRiver: true
            - City: Madrid
            - Religion: Buddhism
            - Route: Railroad
          - Desert Land 44,18:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Hills 43,17:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 43,16:
            - Owner: Spain
            - Improvement: Village
            - Route: Railroad
          - Plains Land 42,15:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
          - Plains Land 43,14:
            - Owner: Spain
            - Resource: Maize
            - Improvement: Town
            - Route: Railroad
          - Desert Land 42,13:
            - Owner: Spain
            - CityID: 1276
            - Population: 30
            - IsRiver: true
            - City: Barcelona
            - Religion: Buddhism
            - Route: Railroad
        
        ### 18
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18517
        - Player: 3: Spain
        - Plots:
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 42,19:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Academy
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 43,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 44,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Plains Hills 44,21:
            - Owner: Spain
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 44,22:
            - Owner: Spain
            - Improvement: Mine
            - Route: Railroad
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 20301
        - Player: 3: Spain
        - Plots:
          - Plains Hills 44,21:
            - Owner: Spain
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 44,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Desert Land 43,19:
            - Owner: Spain
            - CityID: 1060
            - Population: 37
            - IsRiver: true
            - City: Madrid
            - Religion: Buddhism
            - Route: Railroad
          - Desert Land 42,19:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Academy
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
        
        ### 20
        - Type: CombatResult
        - Grass Land 42,23:
          - Owner: Mongolia
          - IsRiver: true
          - Resource: Deer
          - Improvement: Camp
          - Route: Road
          - Feature: Forest
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 41
          - Damage: 73
          - Player: 6: Germany
          - Unit:
            - Level: 4
            - Health: 68%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 18497
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 20162
        - Player: 3: Spain
        - Plots:
          - Desert Land 43,19:
            - Owner: Spain
            - CityID: 1060
            - Population: 37
            - IsRiver: true
            - City: Madrid
            - Religion: Buddhism
            - Route: Railroad
          - Desert Land 42,19:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Academy
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: Defense
          - Unit: Infantry
          - ID: 19597
        - Player: 3: Spain
        - Plots:
          - Desert Land 43,19:
            - Owner: Spain
            - CityID: 1060
            - Population: 37
            - IsRiver: true
            - City: Madrid
            - Religion: Buddhism
            - Route: Railroad
          - Desert Land 42,19:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Academy
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 47%
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20370
        - Player: 3: Spain
        - Plots:
          - Plains Hills 41,21:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Holy Site
            - Route: Road
          - Plains Hills 42,22:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Hacienda
            - Route: Railroad
          - Grass Hills 43,22:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Citadel
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 20487
        - Player: 3: Spain
        - Plots:
          - Desert Hills 43,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 42,21:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Hills 42,22:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Hacienda
            - Route: Railroad
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 20163
        - Player: 3: Spain
        - Plots:
          - Coast 42,12:
            - Owner: Spain
            - Resource: Fish
          - Desert Land 42,13:
            - Owner: Spain
            - CityID: 1276
            - Population: 30
            - IsRiver: true
            - City: Barcelona
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 42,14:
            - Owner: Spain
            - Resource: Ivory
            - Improvement: Camp
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 10441
        - Player: 3: Spain
        - Desert Hills 41,19:
          - Owner: Spain
          - IsRiver: true
          - Resource: Gold
          - Improvement: Mine
          - Route: Railroad
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: CityBombard
          - Unit: Artillery
          - ID: 19838
        - Player: 3: Spain
        - Plots:
          - Plains Land 43,11:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 43,12:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Hacienda
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 42,13:
            - Owner: Spain
            - CityID: 1276
            - Population: 30
            - IsRiver: true
            - City: Barcelona
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 43,14:
            - Owner: Spain
            - Resource: Maize
            - Improvement: Town
            - Route: Railroad
          - Plains Land 42,15:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
        
        ### 28
        - Type: CombatResult
        - Coast 39,15:
          - Owner: Spain
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 31
          - Damage: 31
          - Player: 4: Byzantium
          - Unit:
            - Level: 3
            - AI: AssaultSea
            - Unit: Attack Submarine
            - ID: 19006
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18646
        - Player: 3: Spain
        - Plots:
          - Plains Land 43,11:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Desert Land 43,12:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Hacienda
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 42,13:
            - Owner: Spain
            - CityID: 1276
            - Population: 30
            - IsRiver: true
            - City: Barcelona
            - Religion: Buddhism
            - Route: Railroad
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 64%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 19930
        - Player: 3: Spain
        - Plots:
          - Plains Land 42,15:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
          - Plains Land 42,14:
            - Owner: Spain
            - Resource: Ivory
            - Improvement: Camp
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20371
        - Player: 3: Spain
        - Plots:
          - Plains Land 43,14:
            - Owner: Spain
            - Resource: Maize
            - Improvement: Town
            - Route: Railroad
          - Plains Land 42,15:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20372
        - Player: 3: Spain
        - Plots:
          - Plains Land 42,15:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 41,21:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Holy Site
            - Route: Road
          - Grass Hills 40,21:
            - Owner: Spain
            - Resource: Uranium
            - Improvement: Hacienda
            - Route: Railroad
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 80%
          - AI: Defense
          - Unit: Infantry
          - ID: 20086
        - Player: 3: Spain
        - Desert Hills 41,19:
          - Owner: Spain
          - IsRiver: true
          - Resource: Gold
          - Improvement: Mine
          - Route: Railroad
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20371
        - Player: 3: Spain
        - Plains Hills 41,21:
          - Owner: Spain
          - Resource: Coal
          - Improvement: Holy Site
          - Route: Road
        
        ### 35
        - Type: CombatResult
        - Coast 42,8:
          - Owner: Spain
          - Resource: Fish
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 20
          - Damage: 74
          - Player: 6: Germany
          - Unit:
            - Level: 4
            - Health: 46%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 19087
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 80%
          - AI: Defense
          - Unit: Infantry
          - ID: 20086
        - Player: 3: Spain
        - Plots:
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 42,19:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Academy
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20372
        - Player: 3: Spain
        - Plots:
          - Plains Hills 41,21:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Holy Site
            - Route: Road
          - Desert Land 42,21:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 43,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 20431
        - Player: 3: Spain
        - Plains Land 44,14:
          - Owner: Spain
          - Improvement: Hacienda
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Artillery
          - ID: 17181
        - Player: 3: Spain
        - Plains Land 44,11:
          - Owner: Spain
          - Resource: Maize
          - Improvement: Manufactory
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20371
        - Player: 3: Spain
        - Plots:
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 42,15:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
          - Plains Land 42,14:
            - Owner: Spain
            - Resource: Ivory
            - Improvement: Camp
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 10441
        - Player: 3: Spain
        - Plains Land 42,14:
          - Owner: Spain
          - Resource: Ivory
          - Improvement: Camp
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 20487
        - Player: 3: Spain
        - Plots:
          - Desert Land 42,21:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 20424
        - Player: 3: Spain
        - Plots:
          - Desert Land 44,18:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Hills 43,17:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 43,16:
            - Owner: Spain
            - Improvement: Village
            - Route: Railroad
          - Plains Land 42,15:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
          - Plains Land 43,14:
            - Owner: Spain
            - Resource: Maize
            - Improvement: Town
            - Route: Railroad
          - Desert Land 42,13:
            - Owner: Spain
            - CityID: 1276
            - Population: 30
            - IsRiver: true
            - City: Barcelona
            - Religion: Buddhism
            - Route: Railroad
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Special Forces
          - ID: 20490
        - Player: 3: Spain
        - Plains Land 43,11:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 45
        - Type: UnitCreated
        - UnitType: Special Forces
        - Player: 3: Spain
        - Unit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20490
        - Plains Land 43,11:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 46
        - Type: UnitUpgraded
        - Player: 3: Spain
        - OldUnit:
          - Level: 3
          - Health: 23%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 19931
        - NewUnit:
          - Level: 1
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20490
        
        ### 47
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 3: Spain
        - OriginalUnit:
          - Level: 3
          - Health: 23%
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 19931
        - NewOwner: 3: Spain
        - ConvertingUnit:
          - Level: 3
          - Health: 23%
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 20490
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 20487
        - Player: 3: Spain
        - Plots:
          - Plains Land 42,15:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
          - Plains Land 43,14:
            - Owner: Spain
            - Resource: Maize
            - Improvement: Town
            - Route: Railroad
          - Desert Land 43,13:
            - Owner: Spain
            - Resource: Incense
            - Improvement: Plantation
        
        ### 49
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 20491
        - Player: 3: Spain
        - Desert Land 43,19:
          - Owner: Spain
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Madrid
          - Religion: Buddhism
          - Route: Railroad
        
        ### 50
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 3: Spain
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20491
        - Desert Land 43,19:
          - Owner: Spain
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Madrid
          - Religion: Buddhism
          - Route: Railroad
        
        ### 51
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20491
        - Player: 3: Spain
        - Plots:
          - Desert Land 44,18:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Hills 43,17:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 43,16:
            - Owner: Spain
            - Improvement: Village
            - Route: Railroad
          - Plains Land 42,15:
            - Owner: Spain
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
        
        ### 52
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Ambassador
          - ID: 20495
        - Player: 4: Byzantium
        - Grass Land 21,17:
          - Owner: Byzantium
          - CityID: 1061
          - Population: 54
          - IsRiver: true
          - City: Constantinople
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 53
        - Type: UnitCreated
        - UnitType: Ambassador
        - Player: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 20495
        - Grass Land 21,17:
          - Owner: Byzantium
          - CityID: 1061
          - Population: 54
          - IsRiver: true
          - City: Constantinople
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 54
        - Type: CityTrained
        - WithGold: true
        - Player: 4: Byzantium
        - City:
          - Name: Constantinople
          - Population: 54
          - ID: 1061
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 20495
        
        ### 55
        - Type: NuclearDetonation
        - Player: 4: Byzantium
        - Desert Land 43,19:
          - Owner: Spain
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Madrid
          - Religion: Buddhism
          - Route: Railroad
        
        ### 56
        - Type: CombatResult
        - Desert Land 43,19:
          - Owner: Spain
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Madrid
          - Religion: Buddhism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 3: Spain
        
        ### 57
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Desert Hills 41,19:
          - Owner: Spain
          - IsRiver: true
          - Resource: Gold
          - Improvement: Mine
          - Route: Railroad
        
        ### 58
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - NewFeature: 6
        - Desert Hills 41,19:
          - Owner: Spain
          - IsRiver: true
          - Resource: Gold
          - Improvement: Mine
          - Route: Railroad
          - Feature: Fallout
        
        ### 59
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Holy Site
        - NewImprovement: Holy Site
        - Desert Land 42,21:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Holy Site
          - Route: Railroad
          - Feature: Flood Plains
        
        ### 60
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - OldFeature: 4
        - NewFeature: 6
        - Desert Land 42,21:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Holy Site
          - Route: Railroad
          - Feature: Fallout
        
        ### 61
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Academy
        - NewImprovement: Academy
        - Desert Land 42,19:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Academy
          - Route: Railroad
          - Feature: Flood Plains
        
        ### 62
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - OldFeature: 4
        - NewFeature: 6
        - Desert Land 42,19:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Academy
          - Route: Railroad
          - Feature: Fallout
        
        ### 63
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Plains Hills 43,21:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Mine
        
        ### 64
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - NewFeature: 6
        - Plains Hills 43,21:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Mine
          - Feature: Fallout
        
        ### 65
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Manufactory
        - NewImprovement: Manufactory
        - Desert Hills 43,18:
          - Owner: Spain
          - IsRiver: true
          - Resource: Gold
          - Improvement: Manufactory
        
        ### 66
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - NewFeature: 6
        - Desert Hills 43,18:
          - Owner: Spain
          - IsRiver: true
          - Resource: Gold
          - Improvement: Manufactory
          - Feature: Fallout
        
        ### 67
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Landmark
        - NewImprovement: Landmark
        - Desert Hills 44,20:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Landmark
          - Route: Railroad
        
        ### 68
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - NewFeature: 6
        - Desert Hills 44,20:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Landmark
          - Route: Railroad
          - Feature: Fallout
        
        ### 69
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Mine
        - NewImprovement: Mine
        - Plains Hills 43,17:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Mine
          - Route: Railroad
        
        ### 70
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - NewFeature: 6
        - Plains Hills 43,17:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Mine
          - Route: Railroad
          - Feature: Fallout
        
        ### 71
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Village
        - NewImprovement: Village
        - Desert Land 44,18:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
          - Feature: Flood Plains
        
        ### 72
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - OldFeature: 4
        - NewFeature: 6
        - Desert Land 44,18:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
          - Feature: Fallout
        
        ### 73
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Manufactory
        - NewImprovement: Manufactory
        - Desert Land 44,19:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Manufactory
          - Feature: Flood Plains
        
        ### 74
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - OldFeature: 4
        - NewFeature: 6
        - Desert Land 44,19:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Manufactory
          - Feature: Fallout
        
        ### 75
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Hacienda
        - NewImprovement: Hacienda
        - Plains Land 45,20:
          - Owner: Spain
          - Improvement: Hacienda
          - Route: Road
        
        ### 76
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - NewFeature: 6
        - Plains Land 45,20:
          - Owner: Spain
          - Improvement: Hacienda
          - Route: Road
          - Feature: Fallout
        
        ### 77
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 3: Spain
        - OldImprovement: Academy
        - NewImprovement: Academy
        - Desert Land 44,17:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Academy
          - Feature: Flood Plains
        
        ### 78
        - Type: TileFeatureChanged
        - Owner: 3: Spain
        - OldFeature: 4
        - NewFeature: 6
        - Desert Land 44,17:
          - Owner: Spain
          - IsRiver: true
          - Improvement: Academy
          - Feature: Fallout
        
        ### 79
        - Type: SetPopulation
        - OldPopulation: 37
        - NewPopulation: 22
        - City:
          - Owner: Spain
          - CityID: 1060
          - Population: 22
          - IsRiver: true
          - City: Madrid
          - Terrain: Desert
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 43
          - Y: 19
        
        ### 80
        - Type: CityConvertsReligion
        - City:
          - Owner: Spain
          - CityID: 1060
          - Population: 22
          - IsRiver: true
          - City: Madrid
          - Terrain: Desert
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 43
          - Y: 19
        - Owner: 3: Spain
        - Religion: Buddhism
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Attack Submarine
          - ID: 20503
        - Player: 4: Byzantium
        - Grass Land 21,17:
          - Owner: Byzantium
          - CityID: 1061
          - Population: 54
          - IsRiver: true
          - City: Constantinople
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 82
        - Type: UnitCreated
        - UnitType: Attack Submarine
        - Player: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 20503
        - Grass Land 21,17:
          - Owner: Byzantium
          - CityID: 1061
          - Population: 54
          - IsRiver: true
          - City: Constantinople
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 83
        - Type: CityTrained
        - Player: 4: Byzantium
        - City:
          - Name: Constantinople
          - Population: 54
          - ID: 1061
        - Unit:
          - Level: 1
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 20503
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18888
        - Player: 4: Byzantium
        - Plots:
          - Grass Land 20,17:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 19,17:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Plains Land 18,17:
            - Owner: Byzantium
            - Improvement: Village
            - Route: Railroad
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 17734
        - Player: 4: Byzantium
        - Coast 10,6:
          - Owner: City-State Sydney
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18570
        - Player: 4: Byzantium
        - Plots:
          - Coast 22,18:
            - Owner: Byzantium
            - Resource: Coral
            - Improvement: Fishing Boats
          - Grass Land 21,17:
            - Owner: Byzantium
            - CityID: 1061
            - Population: 54
            - IsRiver: true
            - City: Constantinople
            - Religion: Eastern Orthodoxy
            - Route: Railroad
        
        ### 87
        - Type: PlayerTradeRouteCompleted
        - Domain: 0
        - OriginPlayer: 4: Byzantium
        - OriginCity:
          - Name: Constantinople
          - Population: 54
          - ID: 1061
        - DestinationCity:
          - Name: Warsaw
          - Population: 17
          - ID: 1072
        - DestinationPlayer: 29
        - Connection: Food
        
        ### 88
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 20504
        - Player: 4: Byzantium
        - Grass Land 21,17:
          - Owner: Byzantium
          - CityID: 1061
          - Population: 54
          - IsRiver: true
          - City: Constantinople
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 89
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20504
        - Grass Land 21,17:
          - Owner: Byzantium
          - CityID: 1061
          - Population: 54
          - IsRiver: true
          - City: Constantinople
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 90
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 20503
        - Player: 4: Byzantium
        - Promotions:
          - Torpedo I
          - Torpedo II
          - Torpedo III
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 18187
        - Player: 4: Byzantium
        - Coast 10,6:
          - Owner: City-State Sydney
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 20226
        - Player: 4: Byzantium
        - Coast 10,6:
          - Owner: City-State Sydney
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 93
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16352
        - Player: 4: Byzantium
        - Grass Hills 40,21:
          - Owner: Spain
          - Resource: Uranium
          - Improvement: Hacienda
          - Route: Railroad
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Rocket Artillery
          - ID: 20506
        - Player: 4: Byzantium
        - Grass Land 20,17:
          - Owner: Byzantium
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 95
        - Type: UnitCreated
        - UnitType: Rocket Artillery
        - Player: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 20506
        - Grass Land 20,17:
          - Owner: Byzantium
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 96
        - Type: UnitUpgraded
        - Player: 4: Byzantium
        - OldUnit:
          - Level: 3
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15210
        - NewUnit:
          - Level: 1
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 20506
        
        ### 97
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 4: Byzantium
        - OriginalUnit:
          - Level: 3
          - AI: CityBombard
          - Unit: Artillery
          - ID: 15210
        - NewOwner: 4: Byzantium
        - ConvertingUnit:
          - Level: 3
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 20506
        
        ### 98
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Paradrop
          - Unit: Special Forces
          - ID: 17639
        - Player: 4: Byzantium
        - Desert Land 19,18:
          - Owner: Byzantium
          - Improvement: Farm
        
        ### 99
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 85%
          - AI: FastAttack
          - Unit: Landship
          - ID: 15651
        - Player: 4: Byzantium
        - Grass Land 19,15:
          - Owner: Byzantium
          - Improvement: Aplekton
        
        ### 100
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15089
        - Player: 4: Byzantium
        - Plots:
          - Grass Land 20,17:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 21,17:
            - Owner: Byzantium
            - CityID: 1061
            - Population: 54
            - IsRiver: true
            - City: Constantinople
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 22,18:
            - Owner: Byzantium
            - Resource: Coral
            - Improvement: Fishing Boats
          - Grass Hills 21,18:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Aplekton
          - Coast 20,19:
            - Owner: Byzantium
          - Desert Hills 19,19:
            - Owner: Byzantium
            - Improvement: Aplekton
        
        ### 101
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 20503
        - Player: 4: Byzantium
        - Plots:
          - Coast 22,18:
            - Owner: Byzantium
            - Resource: Coral
            - Improvement: Fishing Boats
          - Coast 22,19:
            - Owner: Byzantium
            - Resource: Coral
            - Improvement: Fishing Boats
          - Coast 23,20:
            - Owner: Byzantium
        
        ### 102
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 20220
        - Player: 4: Byzantium
        - Coast 10,6:
          - Owner: City-State Sydney
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 103
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Cargo Ship
          - ID: 20507
        - Player: 4: Byzantium
        - Grass Land 21,17:
          - Owner: Byzantium
          - CityID: 1061
          - Population: 54
          - IsRiver: true
          - City: Constantinople
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 104
        - Type: UnitCreated
        - UnitType: Cargo Ship
        - Player: 4: Byzantium
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20507
        - Grass Land 21,17:
          - Owner: Byzantium
          - CityID: 1061
          - Population: 54
          - IsRiver: true
          - City: Constantinople
          - Religion: Eastern Orthodoxy
          - Route: Railroad
        
        ### 105
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 20507
        - Player: 4: Byzantium
        - Plots:
          - Coast 22,18:
            - Owner: Byzantium
            - Resource: Coral
            - Improvement: Fishing Boats
          - Coast 22,19:
            - Owner: Byzantium
            - Resource: Coral
            - Improvement: Fishing Boats
          - Coast 23,20:
            - Owner: Byzantium
        
        ### 106
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15005
        - Player: 4: Byzantium
        - Plains Hills 19,17:
          - Owner: Byzantium
          - Improvement: Aplekton
          - Route: Railroad
        
        ### 107
        - Type: CityConvertsReligion
        - City:
          - Owner: Austria
          - CityID: 14850
          - Population: 24
          - City: Washakie
          - Terrain: Desert
          - Religion: Catholicism
          - Route: Railroad
          - Plot: Land
          - X: 64
          - Y: 37
        - Owner: 5: Austria
        - Religion: Catholicism
        
        ### 108
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19427
        - Player: 5: Austria
        - Coast 72,34:
          - Owner: City-State Manila
          - Resource: Fish
        
        ### 109
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 80%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19426
        - Player: 5: Austria
        - Coast 72,35:
          - Owner: City-State Manila
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 110
        - Type: CombatResult
        - Grass Land 73,34:
          - Owner: City-State Manila
          - CityID: 1074
          - Population: 24
          - City: Manila
          - Route: Railroad
        - Attacker:
          - RemainingHP: 22
          - Damage: 49
        - Defender:
          - RemainingHP: 23
          - Damage: 23
          - Player: 31
        
        ### 111
        - Type: EspionageState
        - SpyIndex: 4
        - SpyState: 3
        - City:
          - Owner: Byzantium
          - CityID: 1061
          - Population: 54
          - IsRiver: true
          - City: Constantinople
          - Terrain: Grass
          - Religion: Eastern Orthodoxy
          - Route: Railroad
          - Plot: Land
          - X: 21
          - Y: 17
        - SpyOwner: 6: Germany
        
        ### 112
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 27%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18497
        - Player: 6: Germany
        - Plots:
          - Plains Land 43,24:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Oil
            - Improvement: Ordo
            - Route: Railroad
          - Grass Land 42,25:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 43,26:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 44,26:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 113
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 79%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19084
        - Player: 6: Germany
        - Ocean 41,8:
          - Owner: Spain
        
        ### 114
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 79%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 19088
        - Player: 6: Germany
        - Ocean 41,8:
          - Owner: Spain
        
        ### 115
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 19784
        - Player: 6: Germany
        - Plots:
          - Coast 10,6:
            - Owner: City-State Sydney
            - Resource: Fish
            - Improvement: Fishing Boats
          - Tundra Land 10,5:
            - Owner: City-State Sydney
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 116
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 12282
        - Player: 6: Germany
        - Grass Land 42,25:
          - Owner: Mongolia
          - IsRiver: true
          - Resource: Bananas
          - Improvement: Plantation
          - Route: Railroad
        
        ### 117
        - Type: CombatResult
        - Plains Hills 44,22:
          - Owner: Spain
          - Improvement: Mine
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 23
          - Damage: 23
          - Player: 3: Spain
          - Unit:
            - Level: 4
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 18517
        
        ### 118
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 18452
        - Player: 6: Germany
        - Plots:
          - Grass Hills 42,26:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 42,25:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
        
        ### 119
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 66%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 20039
        - Player: 6: Germany
        - Plots:
          - Grass Land 42,24:
            - Owner: Mongolia
            - IsRiver: true
            - Route: Railroad
          - Grass Land 42,25:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 120
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 13244
        - Player: 6: Germany
        - Plots:
          - Grass Land 42,24:
            - Owner: Mongolia
            - IsRiver: true
            - Route: Railroad
          - Grass Land 42,25:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 42,26:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 121
        - Type: CombatResult
        - Coast 72,34:
          - Owner: City-State Manila
          - Resource: Fish
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 24
          - Damage: 48
          - Unit:
            - Level: 4
            - Health: 82%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 19427
          - Player: 5: Austria
        
        ### 122
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 17%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 18545
        - Player: 31
        - Desert Land 73,33:
          - Owner: City-State Manila
          - Improvement: Fort
        
        ### 123
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15745
        - Player: 31
        - Plots:
          - Grass Land 73,35:
            - Owner: City-State Manila
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 72,33:
            - Owner: City-State Manila
            - Improvement: Embassy
        
        ### 124
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15835
        - Player: 31
        - Grass Land 73,35:
          - Owner: City-State Manila
          - Improvement: Fort
          - Route: Railroad
        
        ### 125
        - Type: CombatResult
        - Coast 72,34:
          - Owner: City-State Manila
          - Resource: Fish
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 69
          - Unit:
            - Level: 4
            - Health: 65%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 19427
          - Player: 5: Austria
        
        ### 126
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15835
        - Player: 31
        - Grass Land 73,35:
          - Owner: City-State Manila
          - Improvement: Fort
          - Route: Railroad
        
        ### 127
        - Type: CombatResult
        - Coast 72,34:
          - Owner: City-State Manila
          - Resource: Fish
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 20
          - Damage: 89
          - Unit:
            - Level: 4
            - Health: 50%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 19427
          - Player: 5: Austria
        
        ### 128
        - Type: CombatResult
        - Coast 72,35:
          - Owner: City-State Manila
          - Resource: Fish
          - Improvement: Fishing Boats
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 26
          - Damage: 75
          - Unit:
            - Level: 4
            - Health: 65%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 19426
          - Player: 5: Austria
        
        ### 129
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 13493
        - Player: 31
        - Grass Land 72,33:
          - Owner: City-State Manila
          - Improvement: Embassy
        
        ### 130
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Infantry
          - ID: 20528
        - Player: 31
        - Grass Land 72,33:
          - Owner: City-State Manila
          - Improvement: Embassy
        
        ### 131
        - Type: UnitCreated
        - UnitType: Infantry
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Infantry
          - ID: 20528
        - Player: 31
        - Grass Land 72,33:
          - Owner: City-State Manila
          - Improvement: Embassy
        
        ### 132
        - Type: UnitUpgraded
        - OldUnit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 13493
        - NewUnit:
          - Level: 1
          - AI: Defense
          - Unit: Infantry
          - ID: 20528
        - Player: 31
        
        ### 133
        - Type: UnitConverted
        - IsUpgrade: true
        - ConvertingUnit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 20528
        - OriginalUnit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 13493
        - OldOwner: 31
        - NewOwner: 31
        
        ## Turn 452
        
        ### 0
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 19651
        - Player: 2: America
        - Grass Land 49,25:
          - Owner: America
          - Resource: Cattle
          - Improvement: Pasture
          - Route: Railroad
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 19740
        - Player: 2: America
        - Mountain Mountain 49,24:
          - Owner: America
          - Route: Railroad
        
        ### 2
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 72%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 17579
        - Player: 1: Mongolia
        - Grass Hills 45,28:
          - Owner: Mongolia
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 63%
          - AI: Defense
          - Unit: Infantry
          - ID: 18733
        - Player: 1: Mongolia
        - Grass Land 45,26:
          - Owner: Mongolia
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 17246
        - Player: 1: Mongolia
        - Plains Land 43,26:
          - Owner: Mongolia
          - IsRiver: true
          - Resource: Uranium
          - Improvement: Quarry
          - Route: Railroad
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 23%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 17581
        - Player: 1: Mongolia
        - Grass Hills 42,26:
          - Owner: Mongolia
          - IsRiver: true
          - Improvement: Lumber Mill
          - Route: Railroad
          - Feature: Jungle
        
        ### 6
        - Type: CityConvertsReligion
        - City:
          - Owner: Mongolia
          - CityID: 4587
          - Population: 32
          - IsRiver: true
          - City: Paris
          - Terrain: Desert
          - Religion: Tengriism
          - Route: Railroad
          - Plot: Land
          - X: 42
          - Y: 37
        - Owner: 1: Mongolia
        - Religion: Tengriism
        
        ### 7
        - Type: CityConvertsReligion
        - City:
          - Owner: Mongolia
          - CityID: 4587
          - Population: 32
          - IsRiver: true
          - City: Paris
          - Terrain: Desert
          - Religion: Tengriism
          - Route: Railroad
          - Plot: Land
          - X: 42
          - Y: 37
        - Owner: 1: Mongolia
        - Religion: Tengriism
        
        ### 8
        - Type: CityConvertsReligion
        - City:
          - Owner: America
          - CityID: 1751
          - Population: 25
          - City: Atlanta
          - Terrain: Tundra
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Hills
          - X: 51
          - Y: 7
        - Owner: 2: America
        - Religion: Protestantism
        
        ### 9
        - Type: CityConvertsReligion
        - City:
          - Owner: Spain
          - CityID: 10390
          - Population: 19
          - City: Tiflis
          - Terrain: Snow
          - Resource: Stone
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 36
          - Y: 7
        - Owner: 3: Spain
        - Religion: Buddhism
        
        ### 10
        - Type: UnitPromoted
        - Unit:
          - Level: 6
          - Health: 51%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16503
        - Player: 0: The Shoshone
        - Promotion: Firing Doctrine
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15690
        - Player: 0: The Shoshone
        - Plots:
          - Grass Land 53,23:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 53,24:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Hills 52,25:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Hills 53,26:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 52,27:
            - Owner: The Shoshone
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Mountain Mountain 51,27:
            - Owner: The Shoshone
            - Route: Railroad
          - Grass Land 50,27:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Dyes
            - Improvement: Citadel
        
        ### 12
        - Type: CombatResult
        - Grass Land 49,25:
          - Owner: America
          - Resource: Cattle
          - Improvement: Pasture
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 34
          - Damage: 34
          - Player: 2: America
          - Unit:
            - Level: 6
            - AI: CityBombard
            - Unit: Rocket Artillery
            - ID: 19651
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 20531
        - Player: 0: The Shoshone
        - Plots:
          - Plains Land 52,30:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 51,29:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Plains Land 52,28:
            - Owner: The Shoshone
            - Resource: Dyes
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 52,27:
            - Owner: The Shoshone
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Grass Hills 53,26:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Hills 52,25:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Comanche Rider
          - ID: 20134
        - Player: 0: The Shoshone
        - Plots:
          - Grass Hills 54,25:
            - Owner: The Shoshone
            - Improvement: Academy
            - Route: Railroad
          - Grass Hills 54,24:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 53,23:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 54,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 54,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 55,20:
            - Owner: The Shoshone
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 55,19:
            - Owner: The Shoshone
            - CityID: 6611
            - Population: 30
            - City: Raqmu
            - Route: Railroad
          - Coast 56,18:
            - Owner: The Shoshone
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 56,17:
            - Owner: The Shoshone
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 57,16:
            - Owner: The Shoshone
            - Feature: Atoll
          - Ocean 57,15:
            - Owner: The Shoshone
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fleet Destroyer
          - ID: 20532
        - Player: 0: The Shoshone
        - Ocean 58,14:
          - Owner: The Shoshone
        
        ### 16
        - Type: UnitCreated
        - UnitType: Fleet Destroyer
        - Player: 0: The Shoshone
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20532
        - Ocean 58,14:
          - Owner: The Shoshone
        
        ### 17
        - Type: UnitUpgraded
        - Player: 0: The Shoshone
        - OldUnit:
          - Level: 5
          - Health: 72%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14886
        - NewUnit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20532
        
        ### 18
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 0: The Shoshone
        - OriginalUnit:
          - Level: 5
          - Health: 72%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 14886
        - NewOwner: 0: The Shoshone
        - ConvertingUnit:
          - Level: 5
          - Health: 72%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20532
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fleet Destroyer
          - ID: 20533
        - Player: 0: The Shoshone
        - Ocean 58,15:
          - Owner: The Shoshone
        
        ### 20
        - Type: UnitCreated
        - UnitType: Fleet Destroyer
        - Player: 0: The Shoshone
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20533
        - Ocean 58,15:
          - Owner: The Shoshone
        
        ### 21
        - Type: UnitUpgraded
        - Player: 0: The Shoshone
        - OldUnit:
          - Level: 4
          - Health: 50%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 17469
        - NewUnit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20533
        
        ### 22
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 0: The Shoshone
        - OriginalUnit:
          - Level: 4
          - Health: 50%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 17469
        - NewOwner: 0: The Shoshone
        - ConvertingUnit:
          - Level: 4
          - Health: 50%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20533
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fleet Destroyer
          - ID: 20534
        - Player: 0: The Shoshone
        - Ocean 57,15:
          - Owner: The Shoshone
        
        ### 24
        - Type: UnitCreated
        - UnitType: Fleet Destroyer
        - Player: 0: The Shoshone
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20534
        - Ocean 57,15:
          - Owner: The Shoshone
        
        ### 25
        - Type: UnitUpgraded
        - Player: 0: The Shoshone
        - OldUnit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15868
        - NewUnit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20534
        
        ### 26
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 0: The Shoshone
        - OriginalUnit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15868
        - NewOwner: 0: The Shoshone
        - ConvertingUnit:
          - Level: 4
          - Health: 82%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20534
        
        ### 27
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fleet Destroyer
          - ID: 20535
        - Player: 0: The Shoshone
        - Coast 57,16:
          - Owner: The Shoshone
          - Feature: Atoll
        
        ### 28
        - Type: UnitCreated
        - UnitType: Fleet Destroyer
        - Player: 0: The Shoshone
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20535
        - Coast 57,16:
          - Owner: The Shoshone
          - Feature: Atoll
        
        ### 29
        - Type: UnitUpgraded
        - Player: 0: The Shoshone
        - OldUnit:
          - Level: 4
          - Health: 67%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 19285
        - NewUnit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20535
        
        ### 30
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 0: The Shoshone
        - OriginalUnit:
          - Level: 4
          - Health: 67%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 19285
        - NewOwner: 0: The Shoshone
        - ConvertingUnit:
          - Level: 4
          - Health: 67%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20535
        
        ### 31
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 81%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 20046
        - Player: 0: The Shoshone
        - Grass Hills 54,25:
          - Owner: The Shoshone
          - Improvement: Academy
          - Route: Railroad
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 20190
        - Player: 0: The Shoshone
        - Plains Land 54,26:
          - Owner: The Shoshone
          - IsRiver: true
          - Improvement: Encampment
          - Route: Railroad
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 82%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18040
        - Player: 0: The Shoshone
        - Grass Land 55,24:
          - Owner: The Shoshone
          - Resource: Tea
          - Improvement: Academy
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Comanche Rider
          - ID: 19800
        - Player: 0: The Shoshone
        - Plots:
          - Plains Land 54,26:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Hills 53,27:
            - Owner: The Shoshone
            - Improvement: Mine
        
        ### 35
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 19802
        - Player: 0: The Shoshone
        - Coast 10,6:
          - Owner: City-State Sydney
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Comanche Rider
          - ID: 20134
        - Player: 0: The Shoshone
        - Coast 57,16:
          - Owner: The Shoshone
          - Feature: Atoll
        
        ### 37
        - Type: CityInvestedBuilding
        - BuildingClass: Stadium
        - Invested: true
        - City:
          - Name: Beshbalik
          - Population: 24
          - ID: 1293
        - Player: 1: Mongolia
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19363
        - Player: 1: Mongolia
        - Plains Land 42,15:
          - Owner: Spain
          - Resource: Coal
          - Improvement: Town
          - Route: Railroad
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19910
        - Player: 1: Mongolia
        - Plots:
          - Mountain Mountain 48,24:
            - Owner: America
            - Route: Railroad
          - Grass Hills 47,25:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 47,26:
            - Owner: America
            - Improvement: Mine
            - Route: Road
          - Grass Hills 46,26:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Ordo
            - Route: Railroad
          - Grass Land 45,26:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18793
        - Player: 1: Mongolia
        - Plots:
          - Grass Land 44,27:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 43,27:
            - Owner: Mongolia
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19571
        - Player: 1: Mongolia
        - Plots:
          - Grass Land 42,23:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Road
            - Feature: Forest
          - Plains Hills 42,22:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Hacienda
            - Route: Railroad
          - Desert Land 42,21:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
            - Feature: Fallout
          - Desert Hills 43,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 43,19:
            - Owner: Spain
            - CityID: 1060
            - Population: 22
            - IsRiver: true
            - City: Madrid
            - Religion: Buddhism
            - Route: Railroad
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19820
        - Player: 1: Mongolia
        - Plots:
          - Grass Hills 40,21:
            - Owner: Spain
            - Resource: Uranium
            - Improvement: Hacienda
            - Route: Railroad
          - Desert Land 41,22:
            - Owner: Spain
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Plains Hills 41,23:
            - Owner: Mongolia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 42,23:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Road
            - Feature: Forest
          - Plains Land 43,24:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Oil
            - Improvement: Ordo
            - Route: Railroad
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20474
        - Player: 1: Mongolia
        - Plots:
          - Plains Hills 41,23:
            - Owner: Mongolia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 42,22:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Hacienda
            - Route: Railroad
          - Desert Land 42,21:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
            - Feature: Fallout
          - Desert Hills 41,19:
            - Owner: Spain
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
            - Feature: Fallout
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 19047
        - Player: 1: Mongolia
        - Plots:
          - Grass Land 44,29:
            - Owner: Mongolia
            - Route: Railroad
          - Mountain Mountain 44,28:
            - Owner: Mongolia
            - Route: Railroad
        
        ### 45
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 17523
        - Player: 1: Mongolia
        - Plains Hills 45,30:
          - Owner: Mongolia
          - IsRiver: true
        
        ### 46
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Merchant
          - Unit: Great Merchant
          - ID: 20536
        - Player: 1: Mongolia
        - Plots:
          - Grass Land 43,27:
            - Owner: Mongolia
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Mountain Mountain 44,28:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Land 44,29:
            - Owner: Mongolia
            - Route: Railroad
        
        ### 47
        - Type: TileImprovementChanged
        - Owner: 1: Mongolia
        - NewImprovement: Town
        - Grass Land 44,29:
          - Owner: Mongolia
          - Improvement: Town
          - Route: Railroad
        
        ### 48
        - Type: BuildFinished
        - Player: 1: Mongolia
        - Improvement: Town
        - Grass Land 44,29:
          - Owner: Mongolia
          - Improvement: Town
          - Route: Railroad
        
        ### 49
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Owner: 1: Mongolia
        - Unit:
          - Level: 1
          - AI: Merchant
          - Unit: Great Merchant
          - ID: 20536
        - Build: Construct a Town
        - Grass Land 44,29:
          - Owner: Mongolia
          - Improvement: Town
          - Route: Railroad
        
        ### 50
        - Type: GreatPersonExpended
        - Player: 1: Mongolia
        - City:
          - Owner: Mongolia
          - Terrain: Grass
          - Improvement: Town
          - Route: Railroad
          - Plot: Land
          - X: 44
          - Y: 29
        - Unit:
          - Level: 1
          - AI: Merchant
          - Unit: Great Merchant
          - ID: 20536
        - GreatPerson: Great Artist
        
        ### 51
        - Type: UnitBuildStart
        - Owner: 1: Mongolia
        - Unit:
          - Level: 1
          - AI: Merchant
          - Unit: Great Merchant
          - ID: 20536
        - Build: Construct a Town
        - Grass Land 44,29:
          - Owner: Mongolia
          - Improvement: Town
          - Route: Railroad
        
        ### 52
        - Type: UnitBuildCompleted
        - Owner: 1: Mongolia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3211
        - Build: Construct a Farm
        - Grass Land 42,24:
          - Owner: Mongolia
          - IsRiver: true
          - Route: Railroad
        
        ### 53
        - Type: UnitBuildCompleted
        - Owner: 1: Mongolia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9042
        - Build: Construct a Fort
        - Grass Hills 45,28:
          - Owner: Mongolia
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9577
        - Player: 1: Mongolia
        - Plots:
          - Grass Land 44,29:
            - Owner: Mongolia
            - Improvement: Town
            - Route: Railroad
          - Mountain Mountain 44,28:
            - Owner: Mongolia
            - Route: Railroad
          - Grass Land 43,27:
            - Owner: Mongolia
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 43,26:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 42,25:
            - Owner: Mongolia
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 42,24:
            - Owner: Mongolia
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 41,23:
            - Owner: Mongolia
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 55
        - Type: UnitBuildCompleted
        - Owner: 1: Mongolia
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 17419
        - Build: Construct a Fort
        - Plains Hills 45,30:
          - Owner: Mongolia
          - IsRiver: true
        
        ### 56
        - Type: PlayerDoneTurn
        - NextPlayer: 2: America
        - Player: 1: Mongolia
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20421
        - Player: 2: America
        - Plots:
          - Plains Land 48,10:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Plains Hills 47,9:
            - Owner: America
            - CityID: 1059
            - Population: 28
            - IsRiver: true
            - City: Washington
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 46,9:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
          - Plains Land 46,8:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19741
        - Player: 2: America
        - Plots:
          - Grass Land 45,26:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 46,26:
            - Owner: Mongolia
            - IsRiver: true
            - Improvement: Ordo
            - Route: Railroad
          - Grass Hills 47,26:
            - Owner: America
            - Improvement: Mine
            - Route: Road
          - Grass Hills 47,25:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18796
        - Player: 2: America
        - Plots:
          - Plains Hills 47,9:
            - Owner: America
            - CityID: 1059
            - Population: 28
            - IsRiver: true
            - City: Washington
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 48,10:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Desert Land 48,11:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 49,12:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 49,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Desert Land 49,14:
            - Owner: America
            - CityID: 1224
            - Population: 27
            - IsRiver: true
            - City: New York
            - Religion: Protestantism
            - Route: Railroad
        
        ### 60
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18636
        - Player: 2: America
        - Plots:
          - Desert Land 50,13:
            - Owner: America
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Desert Land 49,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Desert Land 49,12:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 48,11:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 48,10:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Plains Hills 47,9:
            - Owner: America
            - CityID: 1059
            - Population: 28
            - IsRiver: true
            - City: Washington
            - Religion: Protestantism
            - Route: Railroad
        
        ### 61
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 2: America
        - DestinationCity:
          - Name: Chicago
          - Population: 23
          - ID: 2601
        - DestinationPlayer: 2: America
        - OriginCity:
          - Name: Washington
          - Population: 28
          - ID: 1059
        - Connection: Production
        
        ### 62
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 20542
        - Player: 2: America
        - Plains Hills 47,9:
          - Owner: America
          - CityID: 1059
          - Population: 28
          - IsRiver: true
          - City: Washington
          - Religion: Protestantism
          - Route: Railroad
        
        ### 63
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 2: America
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20542
        - Plains Hills 47,9:
          - Owner: America
          - CityID: 1059
          - Population: 28
          - IsRiver: true
          - City: Washington
          - Religion: Protestantism
          - Route: Railroad
        
        ### 64
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18797
        - Player: 2: America
        - Plots:
          - Plains Land 48,10:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Desert Land 48,11:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 49,12:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 49,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Desert Land 49,14:
            - Owner: America
            - CityID: 1224
            - Population: 27
            - IsRiver: true
            - City: New York
            - Religion: Protestantism
            - Route: Railroad
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18798
        - Player: 2: America
        - Plots:
          - Desert Land 49,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Desert Land 50,13:
            - Owner: America
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 51,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Desert Land 52,13:
            - Owner: America
            - CityID: 2601
            - Population: 23
            - City: Chicago
            - Religion: Protestantism
            - Route: Railroad
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19919
        - Player: 2: America
        - Plots:
          - Tundra Hills 51,7:
            - Owner: America
            - CityID: 1751
            - Population: 25
            - City: Atlanta
            - Religion: Protestantism
            - Route: Railroad
          - Tundra Land 50,7:
            - Owner: America
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 50,8:
            - Owner: America
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 49,8:
            - Owner: America
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 48,9:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 47,9:
            - Owner: America
            - CityID: 1059
            - Population: 28
            - IsRiver: true
            - City: Washington
            - Religion: Protestantism
            - Route: Railroad
        
        ### 67
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20074
        - Player: 2: America
        - Plots:
          - Grass Land 49,21:
            - Owner: America
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Grass Land 49,22:
            - Owner: America
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Tundra Hills 48,23:
            - Owner: America
            - CityID: 1649
            - Population: 25
            - City: Philadelphia
            - Route: Railroad
          - Plains Land 50,20:
            - Owner: America
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 68
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 19828
        - Player: 2: America
        - Plots:
          - Desert Land 49,15:
            - Owner: America
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Town
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 50,16:
            - Owner: America
            - Improvement: Fort
            - Route: Railroad
          - Plains Land 49,17:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Grass Land 49,18:
            - Owner: America
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 49,19:
            - Owner: America
            - CityID: 1409
            - Population: 25
            - IsRiver: true
            - City: Boston
            - Route: Railroad
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18926
        - Player: 2: America
        - Plots:
          - Plains Land 48,10:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Plains Hills 47,9:
            - Owner: America
            - CityID: 1059
            - Population: 28
            - IsRiver: true
            - City: Washington
            - Religion: Protestantism
            - Route: Railroad
          - Desert Land 48,11:
            - Owner: America
            - IsRiver: true
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 49,12:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 70
        - Type: PlayerDoTurn
        - Player: 2: America
        
        ### 71
        - Type: CombatResult
        - Grass Land 50,27:
          - Owner: The Shoshone
          - IsRiver: true
          - Resource: Dyes
          - Improvement: Citadel
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 25
          - Damage: 25
          - Player: 0: The Shoshone
          - Unit:
            - Level: 6
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 15690
        
        ### 72
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18281
        - Player: 2: America
        - Plots:
          - Tundra Hills 48,23:
            - Owner: America
            - CityID: 1649
            - Population: 25
            - City: Philadelphia
            - Route: Railroad
          - Grass Land 47,23:
            - Owner: America
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Tundra Hills 47,24:
            - Owner: America
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 73
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 18795
        - Player: 2: America
        - Plots:
          - Grass Land 49,25:
            - Owner: America
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Mountain Mountain 49,24:
            - Owner: America
            - Route: Railroad
          - Tundra Hills 49,23:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 74
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 19740
        - Player: 2: America
        - Plots:
          - Grass Land 49,25:
            - Owner: America
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Grass Hills 49,26:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 49,24:
            - Owner: America
            - Route: Railroad
          - Tundra Hills 49,23:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 75
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 18795
        - Player: 2: America
        - Plots:
          - Mountain Mountain 49,24:
            - Owner: America
            - Route: Railroad
          - Grass Land 49,25:
            - Owner: America
            - Resource: Cattle
            - Improvement: Pasture
            - Route: Railroad
          - Grass Hills 49,26:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 76
        - Type: CombatResult
        - Grass Land 50,27:
          - Owner: The Shoshone
          - IsRiver: true
          - Resource: Dyes
          - Improvement: Citadel
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 46
          - Player: 0: The Shoshone
          - Unit:
            - Level: 6
            - Health: 75%
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 15690
        
        ### 77
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18281
        - Player: 2: America
        - Plots:
          - Mountain Mountain 48,24:
            - Owner: America
            - Route: Railroad
          - Mountain Mountain 49,24:
            - Owner: America
            - Route: Railroad
          - Tundra Hills 49,23:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 78
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 19740
        - Player: 2: America
        - Plots:
          - Tundra Hills 48,23:
            - Owner: America
            - CityID: 1649
            - Population: 25
            - City: Philadelphia
            - Route: Railroad
          - Grass Land 47,23:
            - Owner: America
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Tundra Hills 47,24:
            - Owner: America
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 79
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18281
        - Player: 2: America
        - Plots:
          - Grass Land 49,22:
            - Owner: America
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 48,21:
            - Owner: America
            - IsRiver: true
            - Improvement: Farm
            - Route: Road
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 66%
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 19651
        - Player: 2: America
        - Plots:
          - Mountain Mountain 49,24:
            - Owner: America
            - Route: Railroad
          - Tundra Hills 49,23:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18230
        - Player: 2: America
        - Plots:
          - Mountain Mountain 48,24:
            - Owner: America
            - Route: Railroad
          - Mountain Mountain 49,24:
            - Owner: America
            - Route: Railroad
          - Tundra Hills 49,23:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 66%
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 19651
        - Player: 2: America
        - Plots:
          - Tundra Hills 48,23:
            - Owner: America
            - CityID: 1649
            - Population: 25
            - City: Philadelphia
            - Route: Railroad
          - Mountain Mountain 48,24:
            - Owner: America
            - Route: Railroad
          - Grass Hills 47,25:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 19740
        - Player: 2: America
        - Plots:
          - Mountain Mountain 48,24:
            - Owner: America
            - Route: Railroad
          - Mountain Mountain 49,24:
            - Owner: America
            - Route: Railroad
          - Tundra Hills 49,23:
            - Owner: America
            - Improvement: Mine
            - Route: Railroad
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 18230
        - Player: 2: America
        - Plots:
          - Tundra Hills 48,23:
            - Owner: America
            - CityID: 1649
            - Population: 25
            - City: Philadelphia
            - Route: Railroad
          - Grass Land 47,23:
            - Owner: America
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Tundra Hills 47,24:
            - Owner: America
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 85
        - Type: CombatResult
        - Tundra Hills 51,25:
          - Owner: The Shoshone
          - Improvement: Citadel
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 19
          - Damage: 19
          - Player: 0: The Shoshone
          - Unit:
            - Level: 3
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 18271
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 20480
        - Player: 2: America
        - Plots:
          - Coast 55,6:
            - Owner: America
            - Resource: Fish
          - Coast 54,7:
            - Owner: America
          - Coast 54,8:
            - Owner: America
          - Ocean 53,9:
            - Owner: America
          - Coast 54,10:
            - Owner: America
        
        ### 87
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 18227
        - Player: 2: America
        - Grass Land 47,23:
          - Owner: America
          - Resource: Horses
          - Improvement: Pasture
          - Route: Railroad
        
        ### 88
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - Health: 66%
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 19651
        - Player: 2: America
        - Plots:
          - Mountain Mountain 48,24:
            - Owner: America
            - Route: Railroad
          - Tundra Hills 48,23:
            - Owner: America
            - CityID: 1649
            - Population: 25
            - City: Philadelphia
            - Route: Railroad
        
        ### 89
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 6506
        - Player: 2: America
        - Plots:
          - Grass Land 46,23:
            - Owner: America
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 47,23:
            - Owner: America
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Tundra Hills 48,23:
            - Owner: America
            - CityID: 1649
            - Population: 25
            - City: Philadelphia
            - Route: Railroad
          - Grass Land 49,22:
            - Owner: America
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 49,21:
            - Owner: America
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Plains Land 50,20:
            - Owner: America
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Land 49,19:
            - Owner: America
            - CityID: 1409
            - Population: 25
            - IsRiver: true
            - City: Boston
            - Route: Railroad
          - Grass Land 49,18:
            - Owner: America
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 49,17:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Desert Land 50,16:
            - Owner: America
            - Improvement: Fort
            - Route: Railroad
          - Desert Land 49,15:
            - Owner: America
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Town
            - Route: Railroad
            - Feature: Flood Plains
          - Desert Land 49,14:
            - Owner: America
            - CityID: 1224
            - Population: 27
            - IsRiver: true
            - City: New York
            - Religion: Protestantism
            - Route: Railroad
        
        ### 90
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 12244
        - Player: 2: America
        - Plots:
          - Desert Land 49,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Desert Land 50,13:
            - Owner: America
            - Resource: Incense
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 51,13:
            - Owner: America
            - Improvement: Village
            - Route: Railroad
          - Desert Land 52,13:
            - Owner: America
            - CityID: 2601
            - Population: 23
            - City: Chicago
            - Religion: Protestantism
            - Route: Railroad
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Missionary
          - Unit: Missionary
          - ID: 20419
        - Player: 2: America
        - Plots:
          - Desert Land 42,21:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Holy Site
            - Route: Railroad
            - Feature: Fallout
          - Desert Hills 43,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 44,20:
            - Owner: Spain
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
            - Feature: Fallout
          - Plains Hills 44,21:
            - Owner: Spain
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 44,22:
            - Owner: Spain
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 44,23:
            - Owner: America
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Hills 45,23:
            - Owner: America
            - IsRiver: true
            - Resource: Gold
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 46,23:
            - Owner: America
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 47,23:
            - Owner: America
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Tundra Hills 48,23:
            - Owner: America
            - CityID: 1649
            - Population: 25
            - City: Philadelphia
            - Route: Railroad
          - Grass Land 49,22:
            - Owner: America
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 49,21:
            - Owner: America
            - IsRiver: true
            - Improvement: Landmark
            - Route: Railroad
          - Plains Land 50,20:
            - Owner: America
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 92
        - Type: CityConvertsReligion
        - City:
          - Owner: America
          - CityID: 1409
          - Population: 25
          - IsRiver: true
          - City: Boston
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 49
          - Y: 19
        - Owner: 2: America
        - Religion: Protestantism
        
        ### 93
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 20363
        - Player: 2: America
        - Plots:
          - Plains Hills 23,18:
            - Owner: Byzantium
            - Resource: Iron
            - Improvement: Aplekton
            - Route: Railroad
          - Plains Hills 22,17:
            - Owner: Byzantium
            - Improvement: Village
            - Route: Railroad
          - Grass Land 21,17:
            - Owner: Byzantium
            - CityID: 1061
            - Population: 54
            - IsRiver: true
            - City: Constantinople
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Grass Land 20,17:
            - Owner: Byzantium
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 19,17:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Plains Land 18,17:
            - Owner: Byzantium
            - Improvement: Village
            - Route: Railroad
          - Plains Land 17,17:
            - Owner: Byzantium
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
          - Desert Hills 17,16:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Desert Land 16,16:
            - Owner: Byzantium
            - CityID: 2907
            - Population: 26
            - IsRiver: true
            - City: Nicomedia
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Desert Hills 15,15:
            - Owner: Byzantium
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Plains Land 15,14:
            - Owner: Byzantium
            - Resource: Wheat
            - Improvement: Aplekton
            - Route: Railroad
          - Desert Hills 14,14:
            - Owner: Byzantium
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 13,14:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Desert Hills 12,13:
            - Owner: Byzantium
            - CityID: 4411
            - Population: 26
            - City: Trebizond
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Desert Land 11,13:
            - Owner: Byzantium
            - Improvement: Aplekton
            - Route: Railroad
          - Desert Land 10,13:
            - Owner: Byzantium
            - Resource: Stone
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 9,13:
            - Owner: Byzantium
            - Resource: Deer
            - Improvement: Aplekton
            - Route: Railroad
          - Plains Land 9,12:
            - Owner: Byzantium
            - Resource: Coal
            - Improvement: Town
            - Route: Railroad
          - Plains Land 9,11:
            - Owner: Byzantium
            - CityID: 8380
            - Population: 24
            - City: Dyrrachium
            - Resource: Bison
            - Religion: Eastern Orthodoxy
            - Route: Railroad
          - Coast 9,10:
            - Owner: Byzantium
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 20542
        - Player: 2: America
        - Desert Land 49,14:
          - Owner: America
          - CityID: 1224
          - Population: 27
          - IsRiver: true
          - City: New York
          - Religion: Protestantism
          - Route: Railroad
        
        ### 95
        - Type: PlayerDoneTurn
        - NextPlayer: 3: Spain
        - Player: 2: America
        
        You, Washington (leader of America, Player 2), are making strategic decisions after turn 452.
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
      - Cities: summary reports about discovered cities in the world.
        - Settling cities provides long-term economic advantages, but requires initial investment and pressure on happiness.
      - Military: summary reports about tactical zones and visible units.
        - Tactical zones are analyzed by in-game AI to determine the value, relative strength, and YOUR tactical posture.
        - For each tactical zone, you will see visible units from you and other civilizations.
      - Events: events since the last decision-making.
    - You are Washington, leader of America (Player 2).
      
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
      - Name: America
      - Uniques:
        - Unique Unit: Minuteman, Replacing Musketman (Requires technology: Metallurgy)
        - Unique Unit: Monitor, Replacing Ironclad (Requires technology: Industrialization)
        - Unique Building: Independence Hall, Replacing Royal Collection (Requires technology: Architecture)
        - Unique Building: Homestead, Replacing Stable (Requires technology: Chivalry)
        - Civilization Ability: Military Land Units start with the Sentry Promotion. Tile purchase cost is reduced by 25% and is reset upon founding a City. +20 Production when purchasing tiles, scaling with Era. Can purchase tiles owned by others.
      - Leader: Washington
      - PlayerID: 2
      
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
      - Mobile Tactics: Allows you to build the Mechanized Infantry, a fast and versatile late game Unit that doesn't require any resources.
        Completing it would unlock: Stealth
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      - Lasers: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities.
        Completing it would unlock: Particle Physics, Globalization, Nuclear Fusion
      - The Internet: Increases Tourism output of all cities by 50%, helping you advance toward a Cultural Victory.
        Completing it would unlock: Nanotechnology, Particle Physics, Globalization
      
      ## Policies
      - Socialist Realism (Level 3 Tenet of Ideology Order): Socialist Realism: Unlocks the Propaganda Process (converts 15% of Production into Tourism). +25% Tourism to other Civilizations following Order. +4 Production from all Great Works.
      - Spaceflight Pioneers (Level 3 Tenet of Ideology Order): Spaceflight Pioneers: Gain a free Great Engineer and Great Scientist. May finish Spaceship parts with Great Engineers, and expending a Great Person grants 100 Science, scaling with Era. Hurrying Production with Great Engineers 50% more effective.
      - Iron Curtain (Level 3 Tenet of Ideology Order): Iron Curtain: Free Courthouse upon immediate City annexation. +200% Food or Production from Internal Trade Routes. City connections generate +5 Gold and Production.
      - Patriotic War (Level 1 Tenet of Ideology Order): Patriotic War: Land Units gain +20% Strength when in or adjacent to a City. When you conquer a City for the first time, all Combat Units within 3 Tiles of the City are fully healed. Can build T-34s.
      - People's Army (Level 1 Tenet of Ideology Order): People's Army: +100% Production towards Military Academies, and receive 5 Free Military Academies in your Empire. Public Schools produce +5 Culture and +2 Happiness.
      - Hero of the People (Level 1 Tenet of Ideology Order): Hero of the People: Great Person rate increases by 25%. A Great Person of your choice appears near your Capital.
      - Double Agents (Level 1 Tenet of Ideology Order): Double Agents: Receive 200 Spy Points. Gain 125 Science when you identify a foreign Spy, scaling with Era.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Majesty (Continuing Tradition Branch):
        - * Specialists in Capital consume half the normal amount of Food.
        - * Palace Gardens built in Capital (+5 Food, +25% Great Person Rate, -2 Unhappiness from Urbanization, 1 Great Work of Writing slot, 1 Writer Slot).
      - Splendor (Continuing Tradition Branch):
        - * Expending a Great Person grants 50 Culture, scaling with Era.
        - * State Treasury built in Capital (+4 Gold, +2 Culture to all Monuments, Gardens, and Baths; 1 Merchant Slot).
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
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
      - Industry (New Branch):
        - Industry provides bonuses to empires focused on Gold and Production.
        - Adopting Industry grants:
        - * +2 Trade Routes.
        - * -5% Gold needed for purchases.
        - Each Industry policy unlocked grants:
        - * -5% Gold needed for purchases.
        - Adopting all Policies in Industry grants:
        - * Unlocks building Broadway.
        - * +3 Happiness per unique owned Luxury Resource.
        - * +2 Production and Gold from Specialists.
        - * Allows for the purchase of Great Merchants with Faith starting in the Industrial Era.
      - Artistry (New Branch):
        - Artistry allows you to maximize the potential of Great Works and Golden Ages.
        - Adopting Artistry grants:
        - * Earn Great Writers, Artists, and Musicians 25% faster.
        - * +10% Culture during Golden Ages.
        - * +100% Production towards all Guilds.
        - Each Artistry policy unlocked grants:
        - * +1 Science in every City.
        - * 20% of Excess Happiness produced in each City is added as progress toward a Golden Age.
        - Adopting all policies in Artistry grants:
        - * Unlocks building the Louvre.
        - * Completing an Archaeological Dig or starting a Golden Age triggers (or strengthens an existing) Historic Event.
        - * Allows you to see Hidden Antiquity Sites.
        - * +3 Science from Landmarks.
        - * Allows for the purchase of Great Musicians with Faith starting in the Industrial Era.
      - Fealty (New Branch):
        - Fealty enhances your ability to defend and leverage your Majority Religion.
        - Adopting Fealty grants:
        - * Can purchase Monasteries with Faith (+3 Food, +3 Science, +2 Faith).
        - * -25% Faith costs for purchasing Buildings, Missionaries, and Inquisitors.
        - Each Fealty policy unlocked grants:
        - * +1 Faith and Strength in every City.
        - Adopting all Policies in Fealty grants:
        - * Unlocks building the Red Fort.
        - * Your Tourism modifier for Shared Religion is 50% stronger.
        - * Cities that follow your Majority Religion generate +3 Production, Gold, Science, and Culture.
        - * Allows for the purchase of Great Artists with Faith starting in the Industrial Era.
      - Authority (New Branch):
        - Authority will greatly benefit warlike and expansionist civilizations.
        - Adopting Authority grants:
        - * +25% combat bonus VS Barbarians and receive announcements when Barbarian Camps spawn in revealed territory.
        - * Receive 25 Culture when you clear Barbarian Camps, scaling with Era.
        - * Receive Science and Culture when you kill a Unit equal to 50% of its Strength.
        - * +1 Production in every City.
        - Each Authority policy unlocked grants:
        - * Receive Science and Culture when you kill a Unit equal to 10% of its Strength.
        - Adopting all policies in Authority grants:
        - * Unlocks building Alhambra.
        - * Allows the purchasing of Free Companies, Foreign Legions, and Mercenaries as their prerequisite technologies are researched.
        - * Allows for the purchase of Great Generals with Faith starting in the Industrial Era.
  - decisions:
    - #0:
      - toolName: keep-status-quo
      - rationale: We are maintaining our Spaceship Grand Strategy as we are in the final stages of the tech tree. Next turn, New York completes the Apollo Program, and Philadelphia completes its Airport, which will successfully fulfill Colombo's quest—granting a massive production boost to Washington and securing city-state influence. Our science output is very high (1919/turn), and we are on track to adopt Spaceflight Pioneers in 6 turns, which will allow us to hurry spaceship parts with Great Engineers. We must maintain our highly optimized defensive flavors to handle the Shoshone war, lowering our war weariness through efficient counterattacks, while focusing entirely on rapid scientific and industrial development to race toward a Science Victory.
  - tokens:
    - inputTokens: 63680
    - reasoningTokens: 7307
    - outputTokens: 159
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Pursuing Spaceship Victory**
            
            My focus is laser-sharp on achieving a science victory. With the game clock ticking and nearing the Information Era's peak on this Standard speed Prince difficulty game, I'm dedicating all my efforts to advancing our spaceship project.
            
            **Refining Rocket Strategy**
            
            I'm prioritizing the spaceship project now. Telecommunications is nearly done; next, I'll secure Spaceflight Pioneers once we hit six Order policies. This is crucial for our science victory pursuit.
            
            **Assessing Immediate Threats**
            
            I'm shifting my focus from my own science victory to analyzing immediate threats. Byzantium is alarmingly close to winning both culturally and diplomatically, with Austria poised to become influential and Byzantium holding a significant number of delegates for the World Congress vote next turn. This requires urgent consideration.
            
            **Analyzing Shoshone Threat**
            
            I'm assessing our current war with the Shoshone, noting their strength in proximity to our borders. Simultaneously, I'm checking our spaceship project's progress, with the Apollo Program in New York nearing completion, while other cities work on defensive and offensive units.
            
            **Analyzing Shoshone Situation**
            
            I'm analyzing our defensive strengths against the Shoshone. Their forces are significant near our borders, but our cities hold strong. I'm also noting their ongoing conflicts with Austria, Germany, and Spain, and their denouncements of other civs, which might present opportunities.
            
            **Assessing New Threats**
            
            Byzantium has just nuked Spain's capital, Madrid. This aggressive move is concerning and drastically alters the geopolitical landscape. I need to understand their intentions and how this impacts our own strategic position, especially with our spaceship project still underway.
            
            **Evaluating Byzantine Aggression**
            
            The nuclear detonation by Byzantium against Spain's capital is a startling development. I'm reassessing my priorities given this escalation, focusing on understanding Byzantium's current diplomatic standing and potential further actions. My primary goal remains the science victory, but this requires immediate strategic adjustment.
            
            **Monitoring Byzantine Actions**
            
            Byzantium's nuclear strike on Spain's capital, Madrid, is a significant event. I am now closely monitoring their relationships with other civilizations and assessing the implications for my own science victory progress. The current geopolitical climate demands careful consideration of all potential threats and alliances.
            
            **Shifting Focus to Byzantium**
            
            My attention has shifted dramatically. Byzantium's nuclear attack on Spain's capital is a shocking development that requires immediate analysis. I need to understand their motivations and how this changes the overall strategic situation before I can fully recommit to my original science victory plans.
            
            **Reassessing Diplomatic Landscape**
            
            Byzantium's nuclear strike on Spain's capital is a game-changer. I am now re-evaluating my diplomatic standing and alliances, focusing on how this aggressive act by Byzantium impacts the broader geopolitical landscape and my path to victory.
            
            **Analyzing Global Instability**
            
            The recent nuclear detonation by Byzantium against Spain's capital is a shocking development. I'm now intensely focused on understanding the immediate fallout and how this escalates global tensions, which will undoubtedly affect my ongoing pursuit of a science victory.
            
            **Monitoring Nuclear Escalation**
            
            Byzantium's nuclear strike on Spain's capital is a deeply concerning escalation. I am now prioritizing an assessment of their capabilities and intentions, as well as the reactions of other civilizations, to ensure my progress towards a science victory remains viable amidst this new global threat.
            
            **Evaluating Byzantine Aggression**
            
            Byzantium's nuclear attack on Spain's capital is a critical development. I'm now intensely focused on analyzing their immediate strategic objectives and how this drastic action reshapes the global political climate, directly impacting my path to achieving a science victory.
            
            **Analyzing Cultural Threat**
            
            Byzantium is alarmingly close to a cultural victory, potentially within five turns if they influence Austria. I must assess if closing borders or disrupting trade routes can slow their tourism, especially given the ongoing global conflicts and their significant tourism output.
            
            **Prioritizing Space Race Components**
            
            My immediate focus is on the critical components for the spaceship. With the Apollo Program finishing next turn, I'm prioritizing research into Satellites and Robotics, essential for building the cockpit and subsequent spaceship parts.
            
            **Researching Key Space Technologies**
            
            I'm now intensely focused on the direct tech paths for our spaceship victory components. I'm specifically evaluating whether to prioritize Lasers or The Internet to unlock Particle Physics, and how best to reach Nanotechnology and Robotics, ensuring I choose the most efficient route for the SS Booster and Engine.
            
            **Choosing Laser Path**
            
            My focus is on selecting the optimal technology to advance our spaceship. Given Byzantium's nuclear strike and the overall volatile global situation, retaining the Lasers research is paramount. It not only unlocks vital defensive capabilities for nuclear deterrence but also leads directly to Particle Physics, crucial for the spaceship's engine and chamber.
            
            **Prioritizing Pioneers**
            
            I'm dedicating my immediate focus to securing Spaceflight Pioneers. This policy is absolutely crucial, providing a free Great Scientist and Engineer, and enabling us to rush spaceship parts with Great Engineers. It's the next logical step in our science victory pursuit.
            
            **Adjusting Flavors**
            
            My focus is on optimizing our flavor settings now. With the spaceship project nearing completion, I'm considering slight adjustments to prioritize production and science further, rather than maintaining the heavily defensive posture. I'm evaluating if these tweaks will accelerate our final push.
            
            **Aligning Diplomatic Standing**
            
            I'm now focused on confirming our diplomatic modifiers. They seem appropriately set, reflecting hostility towards enemies and friendliness towards allies. I'm just double-checking the city-state relationships; they aren't major powers but are listed with modifiers.
            
            **Confirming Diplomatic Stance**
            
            I am double-checking the relationships with all major civilizations. While the current modifiers reflect our intended hostility or friendliness, I'm ensuring they are at their maximum, reflecting our firm diplomatic stance. I'm also confirming my persona settings remain consistent with this strategy.
            
            **Analyzing Tech Disparity**
            
            I'm reassessing our technological standing compared to Byzantium. They're ahead with 72 techs, while we're at 70. Their proximity to us is a serious concern, and I need to investigate if any specific advancements can counter their current lead or potential victory paths.
            
            **Evaluating Nuclear Range**
            
            I am currently assessing the strategic implications of our developing nuclear capabilities, specifically the range of atomic bombs and nuclear missiles, in relation to Byzantium's closest cities like Edessa. The goal is to determine if we can effectively strike their closer territories and how this impacts their core victory conditions.
            
            **Assessing Military Weakness**
            
            I'm re-evaluating our meager military strength against Byzantium's overwhelming forces. Their gargantuan army dwarfs ours, making a direct confrontation suicidal. I need to understand how we became so militarily vulnerable while simultaneously pursuing a science victory.
            
            **Generating Great Engineers**
            
            My current thought process is focused on securing Great Engineers to accelerate spaceship construction. I'm exploring options to generate them, particularly through the Spaceflight Pioneers policy and potentially using our significant Faith reserves to purchase them, given our strong production capacity.
            
            **Accelerating Production for Spaceship**
            
            I'm stunned by our immense production capabilities, with cities churning out hundreds of production per turn! This means once the necessary technologies are researched, building spaceship parts will be incredibly swift. My current focus is ensuring our science output is maximized to unlock those crucial techs, as that's now the primary bottleneck in our race to victory.
            
            **Confirming Strategy Adoption**
            
            I'm confirming that our established strategies are being adopted as planned. Specifically, I'm verifying that "Spaceflight Pioneers" has been queued as the next policy to implement and that "Lasers" remains our research priority, ensuring our progress towards a science victory stays on track.
            
            **Optimizing Flavors and Quests**
            
            I'm confirming my flavors are optimized for Science and Production, with high defensive and nuclear deterrence ratings. I've just noticed Colombo's quest can be completed next turn due to Philadelphia's Airport finishing, which will grant significant production.
            
            **Completing Colombo's Quest**
            
            I'm thrilled about completing Colombo's quest, which grants a substantial production boost to Washington and strengthens our friendship. Despite Germany's "Open Door" proposal preventing an alliance, we still benefit from their resources, including valuable Aluminum and Uranium, due to our friendly status.
            
            **Completing Quests and War Weariness**
            
            I'm confirming we have an available trade route, hoping the AI assigns it to Luba to complete her quest for a significant influence and food boost. I've also identified our unhappiness stems from war weariness with the Shoshone. I'm now evaluating our defensive posture to minimize this and end the conflict.
            
            **Analyzing Diplomatic Threats**
            
            I'm reviewing the upcoming World Congress vote and Byzantium's overwhelming delegate count. They are alarmingly close to a diplomatic victory, and I'm evaluating potential strategies to counter this threat, even with limited options available this turn. Simultaneously, I'm reassessing our ongoing conflict with the Shoshone to secure a favorable peace.
            
            **Analyzing Diplomatic and Cultural Threats**
            
            Byzantium is dangerously close to both diplomatic and cultural victory. They've built the United Nations, enabling diplomatic wins, and are just five turns from a cultural victory if they influence Austria. Their proximity and tourism output are serious concerns, and I'm assessing any remaining options to counter their imminent triumph.
            
            **Prioritizing Space Race Technologies**
            
            I'm now focused on ensuring our tech path directly supports spaceship construction. With a cultural victory from Byzantium looming and a minimum of 30-40 turns needed for our spaceship, I'm prioritizing Lasers, then Alternative Energy, then Robotics. I'm also hoping the "Repeal: Passport System" proposal passes to hinder their tourism.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: mMPFf9bnrvyz6mbx
          - toolName: keep-status-quo
          - input:
            - Rationale: We are maintaining our Spaceship Grand Strategy as we are in the final stages of the tech tree. Next turn, New York completes the Apollo Program, and Philadelphia completes its Airport, which will successfully fulfill Colombo's quest—granting a massive production boost to Washington and securing city-state influence. Our science output is very high (1919/turn), and we are on track to adopt Spaceflight Pioneers in 6 turns, which will allow us to hurry spaceship parts with Great Engineers. We must maintain our highly optimized defensive flavors to handle the Shoshone war, lowering our war weariness through efficient counterattacks, while focusing entirely on rapid scientific and industrial development to race toward a Science Victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19xZFEkFBklG9ItXSMXFhOkD17C1GIEa5+teWcIHI78YvjYwJG/9NtKWjGrb2/6xRBmWyGCUzUpHq8/+1xExPuEgfApiJu5f46BpdX26knGN1clG7xdYXblBKxXSNSNrd5txLJZ7BbdZguhahaVsMoPBt8qRRPyQgrTGNiYbi9kcp3QRAWIJ3JZRrEMsqIlc/dG1r/6lvHQOSiADVK4m7miFWmHFKiEcjwGrAPgRJw0u6P15Kzy3bRRoMsvHUkff4jcA2gOuvDSqU11MRvknISfy2IxB42Voe3uNP1XKofzLeor8AzF/I8wWMMuiyO5ZT1T2sC5QMTPdokOIdMkVLEzs3Vtjj7X1Y947czGQYzqSeeyX9MVTqcQlzveLRr8LfgOVZO1Dm5PjdmEDJWZ6GyKYZKc8+K7Q7Pqblv6vC9PYj9ftZFYMDqlBBHHCDwGhEgl40TAcykJRvajJjEjh7aKb3P3YOB+um+3oiFIgwYa0dqovUDZMZQKyVcf2WI2XQ3D3YJww2rNq5pi39ylQNZbGjH6AjUDKNa2nIRkl3PHmWn/HBEtlz18BvSTR6B0oShDt3eRKlZ5Mejsid6FH8Zst99L4u7NBZZY74RpC9xe1+f6NMyhTGdRgqIbjJXs6iGd/mIPq/HFNLVTWzF96NDhqf+wjwQVuGuJ/NH668kBzdyLiBT//Y7seTPEstTT1qw9+484OCdcb6JrHJp+YA3L8+DFYSvuz7InjVQqLrlSIQMwpZ2JibiWpD2aQgd2UKowPKXDiwq6T3i2kJ5BIzltxXH5HNGdfSQllXjmdF4xDNzvFKVboI2zHsRc+2gZdko4f2yhrKpyq8NwE4XZJt8ggA8YCHV0hFPSjmbq5QzpZy1gs9uEiUlNCjL5K13JKRpXnSfa8ux/GIOMqYugk1wmNwzxq55+Oo3G2G8KfrRjqoPY+SXv0j/zgiFvpR9FlsMQwTwD9YCsM92+TDSUTan1e1/fTQ0+vWbfldcgWPf1fRZiWSxlyjrEtRrbZGF2/Lk8F2XCWWUTuiyGTStGAj4KbmMp23BzE5k6jqGs0Grabws++xRRSkaexyIvAhVmXgs/aIkdOXgpRqs8BvF1K+35f36EW5aa5y+1RR8lMba1lcGWoxABXVWdQ0zm/UUXiAkGzHzAD86NHiqKNf81G2j2vWIaEo7jb6MNPo22I+IpV4Gr3hURsEz2uyHfocv9IHlBx8Ui/3byQCOfaTsKeBWIjcl6L2Sb/uvyz27BoQKqBdaehSrE+wK5II3NEU5SB75silkyHFzoUtRK0ErSmkY98QcwM3WB4w8ZlDk9MNSLVoLK3c7MQQdB2/u4UZxEynUFG3k+kinZdgnlocQxEZLus2M/HiGwuDNyONwAXrJdmGU141Oj/qLUsOXbPMi0eTKAWGqZ1lBWO/n4cuBb9GOBlUlkkMmhlb920olx9J0tsqeFMh87yXXoOuaJOgb+IX4smTuNDi9uRgtEywW7J04JESvOvA/PjtBqzjCRLBuFBfEsCEJigWzrmGaxfRTLXuIN2+2cle7Tsons3GR4Kg/rYKnqU+Ppuqo470ax0353MEUN7hlO5xo0WkNlWgrLt5xzsOQ/dr5eZkZSaZsq1YfZSrjkTNT55H4q1AWqwQeCmYTF55kP+qSJYjcwVpDoot2F079HVsHLOx9XYtgYX58lIL7dgRu8sbNgUt1jNGJMOYgRcAGxK8ubGr5y3hovmfTSLdbckfF7fQJFvECqaDOzKZjdul0b/H2SMd5YTVjCAUGjiBr5vCBkUltCDL7bU0M26XVtldV0MnVp7fYU4UwVz6gucFCPzYleiqtm5DXtGdjIvowOMkwZ0NXH84TlyHtImGgE2t4r6jE0rMNk2UY4aAusmcEbAlh8gT5e6whNoY7jtD7Ek1FvZVukm404fEvizTsChj21YVSM12KIBnRGxTbRRWXmiTLkjHWdY6J52IzZkary+ecnMUi03Z9qIVFZhkNj76HaJhqiuEO9BZGdACqcRIZHf+LrkqWNFY+MUJ67sur2uAGOpAGtYQGfujQClOm3mWE4xwBqlLoj6f3tPw3+zsb7viqzAJkzrM/yxAyBuUipKwIEfL5ROUpGMOuxWiTJLNJGkrASmXDLPH4uUx1YhaFeGjVZv4/8XJwTPrG7sI4PuUUmOIRgdQPqHpcNzedw8o+qg4fKMa/3jO4Bd/cNYQbVGTr58s0WnFrbtmS0vyZr/rXQcnzKApiTbLizwCvbfntjuJTjIszlaYmpFsQPEIn+Z4FsVIXGAMv2b2oU0iC0Tkj1HZjB8Mm4I7r29fGnKD1gLPs/QiwYTYhhU+PmHBMHfo4HViafzKqd1y/o9erW50YQjVb+a/xnUmXgfh6Zo22KLqIxhU9zpQH//yI45HAEFrXHKKdDCPtWfsl9fiDLKoFzC5PemXhqqvUO7JWXnue4EPNae/VWXNgeDaKJEa/2hMerHUPpSy3qic1vbK5volB+VU8kzplPAq1Soitdwi2VLk/LxIv5BNsHR6jUyGYMlf6da8dGFCL8IgZHODQ/1hs+euGlXBtBK6SCzmFLbsRMynGJWuymsbI828W0VLxLy8LMVd+vOOKhNgcMyRe2QO6F2+qTmlm4pHl48TRprEQNKM60yXQddPqd3Y4AWtvIsBL8pfq+MmbHju1R0kdJ1EnFguWzA7eB0zupqjXpLSUcAGKyGzZQ0WW+WcxvoR3Bgv3WgORVU230WXTRJ9As/QoNo0CMN1TpDGWV6rPcdX5eK090Oah6GWPk6ulnZf4MKEuhFtYyGmXJcRqB+p4KGJdKevoqF3PM/TCk/EGoOEzC4z+2IB/bNv7xIG7T/jx2qADcLoUdyJaNqqoraNCZUagpd7Ti7jbSNHH42sLbIQS/8NWO7PHbVYRNiPK+JhNbHKix6gUL9W8va2GJrLyAm2K5+juFNI5bcJ7vpYIHZbbqnHuh9PHBQ/EDhjRvY0eFuIYo/In/DVpg/FFk7QjlEpSIOG8WAhAMXydofMkx8ottEbVSjRnct/Roy/+1OTji4bcVOTCWnM8OUrL9W/+pAfaXwaNLmXP0D23nPqFuU2Npt89n467bkkCBacbF1nQlIbT4kEBNfof2C/Z7zRd5YFz8H9U7MhlSwVZY7iSvo623PsXWIR9mh6NDeA6w5QPEwqL3NR4AyKQjDeJ0SbfUvdQQUFBTgHb61cG8XbfQH1vRDBBKbcV8H7ktLm3qRXoatPc38mFaP3Ls5usLyME47iXENcMwv7i/o35U1ZP+QLrY9e3hj55411v6BdWGO4IYpuY3Jr04FjJUzcnBNEBaIsd1GSAuoYVnpAdE/Vr0rKI6gIusHlW3AEeevFf4uQqT2kZT/OR8ZCWEM6OcifuuDO4gmZP+3sKWTNS5McrYyecgNiedLwUdzEFEoopy7+My17Hp/oHT/wBbwMwahHuLbuV8mOlB2ylG+FiL7/dvkmQGOAKrd2UEB55WMwLjH6RIVmT31r46pJ7vVQ0MYs2xhOkPAIw3VrUWZq1Sa8kMfq1SPBU3dBSISWQpHthXIrIXessmVaLXVLJsK6crJeQq089gMOOVpZLOkoTS4xnKyhu98nYJLyTa5uAlYU5f4Qi9vDGh5wBcAI+4zGm+tZoVsoVOaqD6Kovt4zH2SbmgHQkGw7GGtgA7nUvSt3JOlzFgfXjmsr+c/+v8+JhODa61PIHpqID/v63uea+RnXQWkNcE8z8pakx7NyDcjJBair8OHdatvs3Ph5UqkTH1T/M1YjkVy2+1lQzUAse6aXto1pOxppWAzGF5ZM7739cvP83BNaqLfxO4ETHv37JKvqrwTHUIkDpz7D6RkTeKn0cGU7UcR3yepXKNEJ3oXj6o7gbc2Wb4GgUrd7XrQja54BnTW14qX8Kn69jjMu+SxNJjJWYNtZmslU7nTtH27Tph/2P2dlXoGoKWCJjmqb6EKzrl9vZ6Aau4SS2ZGy/SLUMe9O0o3IAwjHy84k6OrVQimxxcPp4HuELd8myRFIwB7Uo49zbCKI4DxxLEUMw9pNXBMe+dRACn38kYh4tWhOefz3VTr6J2BArTHltX2Q8knD9Z+QATffo0S/k2RI5eUd7xXDHLDLpL9Cwvc30o6iWCd0N1Cd3HmVyh9F9by3R4+siQV+bBVRf/KGmsBNpTRUW6cZecaA8p478ak5DKAN0VRQ/ySk3DnTccTrXUJAU6QENOdf5uf9oyr725P4hvSeu5cNPdhjRp5nKElq7Pzg+IIbuG7eXKQLVLDq4D+i7PvpLKKf3uFz55bqy1IVlLv5GhRzffnUoQPerqXNKxwyoK2iTuNX0Zr1J6OZLmCq5ikjixSmWyzC2MKDQIuxROdTpk/9kDTCLr+/FGF2KUTmVFNIMClQSVUEdKq1Xn8RCgNbPkQc4GH9bpPT138q05xXk1AKYBdq/tTOhmByFaeh2LeES8ScKpnlDw4mQXtbAt5XlJKyt4jZbFxzjfhpG5OlRXf/jmtcyBOV6Kf8eMayDaIJO1k0QeL1RRTWJgWYdZagqqJ+JSVbvfOpU/jygEpZfB2SNb9tjQWTZN2jLuYHUBig3RiZA0ZkW2gx0upljibqtdfZwI/CHqvoTFefwjHQH/vUWtNPuCTAX596vJYKwX8m7Bgj+Z9GuxapDqd/LcOWkVY3WlbNh5P+BCLQKkFmxnjZ/acBiMEyx+emVGlj5gWe7pfnU14FZdHLkNeDyg+7X9uXOtNRuvDxbfUESvn8XWHWm8l+V3DJMSbn1zOa0l23nd/ZouNhYiaWHyDLEDz2iqHgCi9tIJbY/e5uEvBHSA8++Duq78FQ+nks0nOCS55OC9MWVr3cvfGQZX7tV2Xl/yMgGJNuXE680TXf3oiVNIBQIjq0odRDPIvojCvKhTvy3RcLwtBD5HC8cDXDfZaMUl/H9sHxpDUcPyAbChjZOwpA2T84F2KEmuhbjFQ1RDTr9B2HoxzPIE5OoUkgk9QrXfBu4ScSJ4J5B4ubpOraBE7PaTdPx5VTivIQb2MQSqsj2FuQJIQpz5qLtbSCbXNfXPme/soqFYwidIFzIFV6d9AqIzoxBu+yDPtFKw+JD5TjF0noo2Uci6BbMeH3A/WFpXbLpv/cO+tawG1Cg5zfz3uHn71CSf7F2F//hBSjZVr86BSiDCY3IBsu7ceTjM/K4C+iGSM82YardkVmhFTy2qaH6SjyCvHA5TILU2kUr78olYs+9f+nGcS1I+yuUrcBh+hsg8hruOtNReJdALhz9mV9YYWNPdpTI9UopkebAKqvUVOltnmuFOSYnsbi0ylt7tLs8y8F0USXk2V2XeoFk4GfoF39iUq2Sikj/SarLunx/mNAhN6pDxD/k5zjQqvwRBiAJ4NMf62mvcVe3gJ9fqXVO870u+Nf5TbT9KcRZkMxPlQefzLSDZRY7MXRjyQcstJqsD9RiyR6ayiTx9pp+jIW7dbRchb+OH/aYUeNuFlAmL8LZYTM3wkh297MkTDjL8eoVpq7JOfo9Ub2yAp2iZn8+/2tOka3gltOmp7JTwXapLsc9VKkbu53la562PJJYS5C9vLODfPZiRQL6D8dh9arjVIlEqS5o2aIUoDBUen0Z9F/PQO5RgDLKB7n/nVwVnF9CqZVXiDf5/viCu78yGn7uRe7zvaiekXwG9w+VsGKXGktXAUJCdELYXz0sVU9BSBtEkdZ8+A2z5TiSewBU7KY9coMJYt1p82UL2uvozhyNdSy7fkV2KzMvMw3FALvibgcMSN1UpzmIv+38qY1zarx4dSwP1cTh/XIZKndjWgBdraR+Hr3R3LszFBHmDrsZ3GQDTjnuA6zpGf7cB98RfD3bzA1IOeaUBhk5Y97E2SOgNDdnau1OEDQzIXIGHGe2WuZ7n9K+ukPZJwTaWT707f3L2mcaAEE2eDbulgsQem41ncKCqU7ERE8aUYcgKcGCQ50FznUgWxAhdGZmt/UbuHYrvQNNwtnxcBA7GDzMzUOBoZUyqH+GVW5MPCKVs7m9NOsjJ03/CIN+JfI7NTqR2GrL7mDkwwiJ1U3IAuCbkOi8FxGNjxw6jjvYUp245TOgfqzeTrkl1WZ5KNiwJrh/a8tSISYMcI03TSmXtM3yVzpPeLBGzQcJy0E7Wtfq1iN3wtIJpFR2SP8gRv+HsDDIpO7Xl+h5hMm9ndaEsV17U5nA3Kwo6/GAbaJ5hAtK7oGzjrjU14UCb+S2ESsQBEG95RLAnG/gKSIIs5Aq8tHmr3wDR4uodSGnDuXOUuCCep1VFE80uDc3KbmwrUbiXxOfHy0KANTF2LApiNz12Z/VdfeR3cFZ2ldo1olq/+x2Dab3spnBnN8UKhMoCqrwSeDYFUJtW5dNvFlofCD8wruqjGddu3urziyYlpfRWi5Bkytv3r0oiZ1LBFYcEpgoijH9rhFzMXZuW6Rl9DA8Z2EfM3f7B6xALio+QGHkHKhtjgOA2LKhP6BdtHoiH/vQYs+sbRHrEYqVmNeaQeXzuiYZ4Pu3JroqqvNpzEVLCYUwLXinRYEcNDN4JZrjJEI+j1ZchGsQ2GAzMwKnv2JJ9LrmsVjFo6onSYRYXtxoHAKt/oLYt5cptibUimp6J7M2ivgv0BQujhsqow0i7tSl1kbuzIcdxT16Kf1KiLBk5nn2Y35+lYY6Q1Oxrg6tGJcv0pFYri11NWrXNjAY+om3IvPkP9BkG9NP98OB6tvIHjl0cVReLOswRMgzm0znpIRPyoetbb1/L/GfPteU4FKuZEm5Qrc6joZWtCnZRypouzA/VeKnEPxfYbzqbtxRUAVFUCnjJosEw13kNTHL6rZELOXExkIn5Bt/e3sVGBl7Nuz+7HRT3biSRtUW3pvVurn11qZQtsikvkSkvjH+ZminPRTqGRkBm+vtYVUB49DPbPy6snZE9vcPUX040IhcfsL7uNhyZZQhPQTDBE56wE95caFQxZbmdz2d5/RMOaJX1E2SjoGiQqqG0FyFStzbZ0VV3Zys+3iw4PfXpgABbYy6MB7tVmOGR8NlRwR7NCy8wl8y8Ln3x/cYXVJlu0nh37yez9jYKnSaM112nJ1lz2cFAGvy6l4mTEM255sdfl1HUboe1IcGTjkbzgyzpYLk5kQl9GGqxhLk0g/QnVNTKb0VV7co504VtkGNFcj6DwyOctNWbp08Xa4ApHdZ/hLUbLYEabD1tciJH8UWAQPf+YTcp4554Uo80URJ98Lb1aiLJZ/j2VnRrOEnrjSePk4iL/CWpFI2I5tSH6WpHAabZPnrjrtTwCzQNJiLA3yEC44qxj7A/hYbvusOhLOhlZnqpQ485UOVvZWwxEnv60MBNoA4z8v5RLMebd+eeGe20TdQq/zIUn8noleEJFiV7cEoKbOjViu2MI9l+eV9Ot9AQSJg6xV9CpjLx3zCqdlDWq7f1OWesI+J4fHxkoytqTX3EON72+FRA8BDrdjfVDn2DG48bk1iaS+AITGmP8ZxmVLQt3+INSHkfd8xfLYzDEA+0o2QiidydP+3Df6UByAS41fO8za0ZiEd8bPMomb5vwZ/znS4puBsJpn3rozWFr7mzYA4hG04GSLzYIQCBp67k7F8fTGXIqbO0Zvh+6ULMPsHRkq1W/mlBUL156ek39Rh/TAnf4RSjSvMKHmRK0JchUjPR4m6xvrNKlKWJvaKvLOBbSekpd4YvNTUt+KLUoV36x65dHfV9lzTHSwlpoVa9HUC/ncHWaeCnhak9GTRnHbt+ng99GsWxxG4NAy+h3jfc3GCtxTZR0FY/+vJy+K5ZV9zG5yqS89DF7wkgoprT/gmTMjEgXlVpQJ4Paax3CDTKU08YfvyvMljSnL9hR/F5Cev5ZoCBsWATSvRNfrvXQS+sE1+kXGu7F57KquKQUcQe2Xft5Ea/zWS/LOK2LK1WVZcPNHxp8Zk7R/4UKxmv/U1LkS9i7MeJQpEqXWYAUW8fpzNfScb5IqV6CcHHt7l8VIz8Kzadjgrof4ef0laT4HPflTlyHwr/eYZlINJV0NtzHpJJr04NcXNgjS7jzD1G+gLtKHgf9ewFN2yLq23kyH63K8VbAxMZ6/bJ39JjtFjMEntVKB8g5JQ8X5dxbSz3VgRrIHIHhpkoHzw48t3spTIKbeUgeQbvadmiB7GaKPhm2EPI4vsD+QLIftNB5ABbeOEScLNUGnGwkKY53liIgx87jD8D45xP0F0M6NCOsFCQMqbB35zof8Ns03rIWmixiFMl+RwxrDexorDilKhgH9FisljB2ZImmV7hv8Ol1xGvNV6BVn6DychTVEACB3WLv0XL693sY7ZmXM6/nu8Vf/sp25xX9V2Y9N0zZuNFXdZh5341lBDQM9Y2undebGi28lPAnLe/GZJeZH2S074g6HRz9dbNykfWr2kLrrXK+ZLGHbF31Ll+aohp/4fNPH3wABo5qCHKi+yGn0Ku1I6ScNVO0sOd/V3t7Wq7NUoXmTTLPtzTByrvhMmxKL+XNJ5Ij1c5bU6QyiHb6UKwdMBGtBgdEwjKevSQTDE1K1FNCQAxofWCA/MFRP+UYTFnrgzJ0EOBG3TarOTb2uxmFXhcBZN2JCx6uwsOD1nzG20GOG1D7f6svhf1fLjKKexpQWdQXNk3STimGhk98OAzbhCk5pXlKJ0SPFQgidzzTi9NUT/i7KNhZjBC+GKsYz2YyQZiAFwrfLNEfyzRgPnCwR6kVS8oKhD7lUr1g4L83584+Lc34Gy8mJ5mfUVZUZcEafg9dDgHpthOsghdTVqLfrFpKq5R9mCNyVwejnnJEmBbb66EuFkaGCcNiLyKFzHN2QNPCl9sNhDwOsnFG0TsQbBL3TCC+z3BlDu2xWDkSC1FpOhA11z4DGhZA/7Rtgn+EzuuFP59cZOpaKOzsVFvc//p2efiY+A55XG7vo0Dl27BlAfTeWuIiHyVbX/8Ql/mFZGZgJUT3R1bLNwHkNF49u8lCS59+8BvoYXUv49g9zAuXyqEahtSEYl5/jU1b9iFgg7YiFoRxoIMKNzCqe51S/KDNOrHKBfyfy65plHHHNN1VKsP1kfA0HfBD4sW1SJGRuh0E/dY489xIPHqKlCg6VGlD2KIE3TQb601hWjcDPorjvMo5mUScx6dOOH5tQatsweskRm33PGb4AQXKDriwFVYmGyOt3A0ylFNsyaQt1u9HC33Xl7lbXJlHSyQeGCARF/2+Juq/MJ9AiK2dcelocy8Fo6mMg3rHpP8Z2FQ1DllOEE2jlzzx7/gqj7aNzdV0jGLqXLzHikBD8D3duwPyLj/0zyGrUR14Xxwa81o6RGpuWfkG9GiOdfeyMmPw1HXbYkcEE1Z9mre8l6liDJuuhsUgOTYZcEDiOelC5kPJRbD+qILqlFQOAUZPhh9bnWsIxR+pVaeN6Zlf27lBh1j8GvjLeYSz1oTXP3sVxAC58z8Bh1kCdepfRDfpaQ13tnAsncGbpP1ShH9ZwFs7KtSMg3+6cIXtt7l/8AKO/rlfRrf1RBfbdWgER3615JwL0XEL4VUw9OYVTJlL8fmMs3wB5yCNdp14or6VvTBJKBSU2NaBIJAPCYeyQkOdovm++5C6+Sux7oOAJ4pvLADnPgtFq97gXRWmlIpDh6ZnjJJuFG7JZ8z85UADPeN6RRPs6+eiuh0WBQjXlUeyrcMat54Dd6h5103nc4QMsuQ8dACOTOQAt0X+VgoYTq1T3uycjbgrY5oawpHbrxmIBQkS4XHmQjsnoIzF3ismSuGna6WBjMB5AICUz/tAOHbz0EfAyspbGIUmYZH9Jz/xN3pVu0qU7MsqTMRTiUpbBmZElY9mzMpxI2s7K5qFqFw6Zcdayr6c5POHkm5bfPacmL+OOQho1haw385637TMHOSdkeEQrCE/OmFuLOSKu6YXqZpbrKgHkKJoAwESLvuxQ8zfWRDvdSy2vWVsdrJ35yOafGb+flsyfXQV9rr1r0CIy9kqZnlt9naAPGUURN3ZAxLSL8WGry0wK2fLvO+togECN1R7ZuzGPK8gkKKP1I67dUhUFu/RBxpQ5s8g0kDRnpb+5iiUB2KoW97BG4i6ZaFu9tP2aU3ni03nFCP5Fa/nxQCu7mOn/glDGDU1pDutUDFzm5okJskNsU6WQtrcA36Wi26deIId6AsqrAQ1dBKg1Is2r5AGnzqT20dAwFPQcA6h6p189vr9eynd6j773bBQu6XS1/fra3d9FK2VWx8zf7Vg4DTNBlpjVhlcAnr0qvCB9tWMCJL8Sv4mcUw4/eV69GlwGQA6OzBDLKTh0+JyK3ztRSdPcmdZbndv/eAGw2/KVHrXPWlTGzMkB2MCtupLtOEjmoIbvg2ARryi0rKVfMAbeH+xFOqJE74B2w9wF5MWv9qC3pLWhYHDGaRB/DrpzeB8MP9oId7jeRM2hjyOMqDHdI/9Lvb92+Txt1rFhJyxzl27qvNKnfYWJ2Ntk8/ENV2eSrX6NG46Top8iD/8nXgE2DL8m8a0Re3UI8o93gfQPf2ggMZgsOPpOJIsTEyCaAusjoB+9Lvh/Oj+eu4GN7i3PuPPUGLl3eBlRPcOhJP2sQ7g5SLo7UVLcFMNhwh8ZVzGD5E9bctXe6LKi9TMD/64Ap3/t56uB5EVzMkdMULPfXUKijoLyRMcTVR1YC0F61TVPp33CkvYOgrt0PdfW1J8o9gUyyt6TfuChJkCjChn0fJz5HmV1UWMcnN9lXAEeC+QUcgGhHAmBLZf/QHtRlBzRpL6eBlOz6w7dt7TtHKPPezjvZXV3pqqRINUtlHP4hcEw4K0YaGZTroz2Yrgf3ALR6eBKB6jtCqpRIc4nyqdpBrNZFIaZ46lH1AK2EvLUSMrzdh4vrkgL/xyv4PrAECbuHESN58cBEEFA0M3ZTrYqgfzVPw7GgbTyuCo674mdTBVE0i5SOdG7EwTMVm69Ymjn1wcbP6xxqcbHmlKaClprghtpXLTJfATr8lpRYQ/nDIrvudXZAgHEV68FnNlpnK7uNRwglc45vzkOD4abyFUkhkF2ZOdR2s5LDbmRTEBH6Hhq1W5hdGAv/oCrDh/4a/yASGxz42jhqlxyGeaEFUZ6V6+/+VozplredfBMxsov/JOcqXBiuqZIDSnxS2FZftKgswH8N9xl85dbbn6VcsqPkPwBuwYWguhmXKi7MGv+QNvYcqtkBnTPRsNNTbDTktxMqj50MoBA8JAggKIteTq+iY4xVknCkDSBriQIlJ9E/k/zB/jwUQP1ESIcw7Qv//oSq7jarpcdHRVly1UsrbRDfWx2hFwDdt1Vxjwc1JnOE9wZbuR10Lakm+kWI3dDuV+2asBnzmZvRJ6Clh/0jOHsfWhQcyoOcJfKWCd5IlQwtoXxdqTZZhxeTS6RI3XvYwjy9e6Ohgj9oeQOPf1BDoWjSI14ztPfS9d3s1nJ1Yxpufd0Unxmv16cjedeJ0/yuzZQXXhncTmY5iKeJe7fHTMtZX+xf3leyfl6U9sMvhNlrG5PZViEZ2Y+m/9Je8jNqCCrE0tl5F81wbcPpWIZWeInO/kQ5EYW40kUYaR5mEs4SwK7EQcuWJuRQ8/L7tr0nGEq8bBrhBTj1w95B4d3uDOFYp1TOJPRQSs8yXpnwU8q2CDj9YHJO8ATWBvUnE1W52d6gprrYRpE+eqJN3VByhrJ++4PVlg5gH1nNJOn/xIyC4gESk1QjE8g2LOXxEfm2cfVL/YQiEYgc30+Z1ZWKqNcaKrcInejoaCeOFrc/eOpUHV6IiZIWuAcvH2myWwpo0Tize0ToP0/VWUNFzL8RqhsbxsSISQlllcvKXOwk7euGqkf+/rzhxaPrTvlMCyBC7kP322IJkVgyGM5w+39AGjGtY8pzRLVMmSp+0iMynRNIuyKp7xaCGGToBLjROzlubZVt6HhnfpFGJpGDsEn8ick08loeD9Ad6PpvknAu80R+YmrBp0LwSJQ9SKlGnhCqQmC1WLbXO7gdbfw3tgrHrj/f2oFh9ah+p2qWQN9GynnyhCGfSwA3VO91G9sIj92PDGI8EiiH86JEwDo8B6VgSu+bOib7UpDpMjH52xl8oa+IW4WveEki3uRpUPe0wZhbNBw8/ub1vMpuNrUo4hzVRonxCof0zBtx94OQyaN+JLz/EX65tPDUwb0zhKbO3RkoU8QyyT1sVXSgYpGXIKyJCIdK+5g6QwmL5tHMyDMVURlRle3hPrUmBapK4cdoPz08iE+Z340m2240E6e+jbdxiCz0VvlZQEGDNYRh64OPtNI2n6r5AiztGTixoaN4pphhQx+lwJZlyBAWs1pEbH8dTiPSzlGKB7k49nujU8gCc/6gxb/U9Eq8Vqn5gID6ezyjJUrNfYzD0I3qwL1kqqaNtIkYOeXwogBFvPExlSATwZsMBibLIzCZgVGqsJlxZozvz32vgIWalAdVn5/xsw7NAfKM4dzYOJgb171a12nyeSEAR654tgmxKyMjLFCwKfhDH36TPEk+vNbn6f7Nj+olJ5LjmcFOwZMnuq2UKF72bblMSPuT5ALk1uz/OIeZT5GuwRKrJx21LeJF9DQUbg5dZRvw+/4C3g7bLtaX0P9Pp2C7xC5/XPDjAzWdta+X/98IUpBUFc1RgUY4zHxb57MxFTH/GOKll1DEYwr9ncz7hxw+Vf9SuziqbY6kFGUtq3OKdJUkvAsJiAw5ELODwCto89AltEECwbuDMis6YNg7eFQdT2hTi03WOjVP8jMA4YJUbeDqWICyJye9qLoYlZR53EfUWHbvAA4tcRoq5448POGbf1n5eGibh7xw5F6EIIXPaQsookX9Tg1KXjdPhaoda60FLGn8tohKBbiSX2J01m5692z7eDGQ1ZzcO6kwX32DlbAa7h/QS0Xx2DP75bvGX4rz4VTUCcbmH/dyvGZIKW3TSlN2HzRwxOhrELmNCxTtgkOoFQqjwBmFG2bM8H1LBVWXHCsIWNYaiwGgneQ/ZrxDhFKercGIfu9Fe/PUzyq8L9JrtlOy0al3VqIxyQvlb25A6OkKcxKI9AYCFMvm7rXqHzD7cJ+pC1bPRtpfba7sANqrqlZ60KyVOg40FZaE3XRAAyW5v1M0GPPnVFWMjlLl26F5K10dMAKHxpQL0K9x+lYpMXTfI45bLDrAGPupuFMfJXCOwikNguDhO43qvjgAKLxieZSYgO8CJxxnbrFjAukzuB20r9BbwbKQ5AbSiqaPihutjhgtpMoCTucFwRVU+lwgp+HCBtfYG+uOZhhUjM7r1eNODJf4OEyP8bCkG4bLm42JmSpTQBEiyld7yCkOZtJqP5ttmTuhY7Ft1MYPV/sOxLBem7VNVcfRNhBeNlvEglE2qlt8hRSvrwcO7bsVxtuE42scv/Rg+yaStqpjNZESFSAnqDJUtIPphOQtwVuD/0MgBzQ241l3Yx8lM4FHDK5gU2FeqOS/kYdfFmVNSTBpfDjY1p20xDyRHMc8+QI8XIVGJuNn76AgydeKuY96CF02Dl5iR0+UPUIqMUrobyxfqZlSS3kl/g7ZXm4XPqjbioJ9mUfMdIsQ27RRR4r1bAAewBE2R9A13qXtG5Oo70fpSwd78/j/eMDgZUqm/iKwwwkzKKsiiJ4zWemJE5efkphH1DS3yoVwCBm3dOecEMEh+l4nJKNaP0fMM08llZ/WpmfYX04H1/2oXORhzK6eeLlP3TiXZQUmxhEfpRvVN7V7gNIGexAKa7Srcp9P+fWEKzIYcyqX2xHlthKNFo3ojGMceKH8kTXEv2PE9fjdK/kHTuHKTQVHrOd/wzRTZMS2t3Siz+d0htqfcAWxUVfEM6S9YcputOvEp3cirhaw1XKEr/NH6u/Kq+/yiJvxqXIU3PsIbVY2QbnKkE0Oc2tMCs0dRLLowVCVAcOA0E/YrdyesJKP0FudxNZuyxP5XviGZVGGNR5+dSKDOHIobDQSO02t4in54PknPuX4CbvWw5fvLg54hIferGtGmtLZDYCpojYTr92w7C1yj8IqNaH6qbF31Ko7SV+C3nSQLBJ3YObUE6FucQHacfuCcOHFkeFD60d5HRqiXgy0xZCSx+4peBScDZ1o4DOaE5Dn2pbSOokQ9p+XdYgmMZ48a4rQTbtSp+iaRzRD+XaF76XBu0sHsdkVDbSEzo81WSgj8m1nG5d25R6dGunkC6sbJQMwH21NfiyTLd+0B/efZgDwOY4xmetaR5LKjbD/eGkeV2ut9Rsm7VsT6LG8AbPh7m4W/1Jzf4eURPqtnZcCWxg2dZItsSpOoMFHqb3Oz3ZAj9v71ornccWaH0oQ0lvWoA/dpH5Af51UPiEz1Wd9uCVl2VZe86XicVCAL4zslXa25+cJEdIhfRKNL2fKPSUiKAoN/47+7/Mhi0vkQHr1GTfSTQx5Yd9pIKowV4uaJRkz62p2v2wf5OxAuZszM3t08NmuxQa+Z43CDfsHollLkdZdqG4op6AhQaM2GUEJHufJSWyMz4UGe98OEqxHNa3TvD8Z/lWU0CwaVJ1e1LKYwHrzLWECEy8Ux4REqOKojU4xUS6nKMzb5Z9UvW6kiEg746BuSbjLTAImv5o3ccbcSqUWEB+1XuqqbW1nzfXXXHu6n3pJDhzVzTgbDJTs7nTJduxCC5peBC4MsA0zfU9UF6nNAVUIVygyn0493X+kJ9SW/yMXawG1WFlxPAi3PG+hb+u+ix2XzcE4C5t5YMkU6khyYyfhR2XWmj+WhJCEmOVK54Q96pjNAzqw++98UO6AiCoqwPVJhSJYj83iWMRwZTddFvaLdAkAcMUreSBsMt2WGSzE2Fvavc6/tGpeUlm48spEEAHr09TM8VvYWUwB91ToBQxExlIeDSBuzBXG0Ha0heEIBvBDba2llIm3/9oovm9Aw1W8F6OHUoWPzP8qK4mZNvrZEfdVmtjQPT5Ip9jHlm46seSJUeXfXNcQPFuAyIOPvEA2iSF25PO0CVkYp12dSDgsquvv8a+yDQA8/EmTxgX5O1mqWvI4g9mjSKhomJE+W5HWT70ebtfgOfq+oy/kW8I+sNlKrIe2Kyx236fNC7npfs2UXeMrm7eA4S1UiiDawYAxTkLB+AjucCXmaY2WbZ74eFabPuUqVN1nBueCAZD8n0J0MEu6IA+KALFTY9Q0EVk4zAjjP7RFPeTZzl1NcF5Oy43pEy20w9M/PzfXtJkOiSoERP6O0CQ/P9OGkeeSgcsV++p5cx228Zmb8Ubgusi9Wrqv4fnBT8rnyzk1cboa89x+zIILqluWs21BKcOxdKyyNJ87U7s/MbrUTwSncN10tC+WtGsNVBMLfRioasdPODzhfK5qtwyxlyA/eKGqZ/z8ppnhzvbiF4Y2jdzJKKH6JF6g4VX2byN5q3SH1oODPLJLWwMKGb7QhDGUaaMTrDv7U6fsRns6c0AAm24fs5qAIU0Jqb5DbOm/Q9/dvQv/JScUzZaf76Xr6CXTXEsSU6JAAgK9Jc1LbMVtQ1sPDx1kv0wx4b1nqDlx1wHgBzg0IVx/CNxa9bqrGfarjNQhwRqIz9P8TF2aFeh/OL7pXVKE9j1+IRzX+uITr9J71lEVTFT5Ino/2Tnp04ghmZgps8jnLl3yVeX4nWMvf4wkCT1fuMqRj/ESI0SqPid4T/H//DDs42Ack998/r4OD7Hv+JW7ggCk3wxmIydJ0c248OYZxV+vLgio8ifyKLePR4XrO50+0BMMDV6AxZjgtn8d/iS0CnzfNdEO8kF9G78EOswpsldA/3xNcuYtj9fTcEAJij608s40Zpb3iYy6BB/3K0E1+dRjEm71L0fHu+ZrRzWTwu7+UxhcGkvnWlaCa1qSptu+ZiUiopTMjz7STfD2fj7CbstrpTGG7ASiVYkD7I1uTXVDU2618fFbEv8+F6swe2Bt9dveGAEXzQlLqnj53kPfzsN31NUCLVibkSJDsSyHSL1nEiRrgKlHs9ForQb/6I6EMwxjsc58fTMlK7ESuiBGYrdXssYZWI3Y617H51yr5TykG20tv/TCYGkyZ8dPieSf9x84oiUq/YIwu4Z6jezO5NiyBFQB/ZDjzXqOlnHfB5p06K8C5XKO/pavoPslEa9j2WHYpymIGPj4Defdu7gxEKpVvTFBdXzcTtTpBnI/pQulT2Wq2Epf54Rs00+pTgWUrRhG7KA15jwNgG1Cs1/aor0oX/pGfVGEkdZIQJt3mu5ntbvfOjYRM9nwcwLUjJc6vTp3NLdYZ7J3NeO5jCDRtRA6ipD1u9dZuzeG4ooRKEnjZm0VTQSUufqi5aY2rDzFG5Bx8TtqBQvTZHNbVr7BM5tqpaBH8cXHMVsBqnyocUqQeUCync8TH8f6toiEAp+rUytzqMt3/3jG1xwwkB6q5hwiXPP7+cJKJ/qaGeQHolclnaV8GpB3Wxb+SNzAyTQpxJQ0xi2C+VE6CRCkBmOHb2KjadvfhJNJC+WHcdg9XEV3xZ1fXyd7DFxS+agRjspTY9VdhjOYoASyCBAvEXgd7ECRCoeFDIpwoa8qxaGD/XW4Drci1XPCSiLSgTa/O7uqw/ZTkZazSDZ4rqPraKbtdVNeHtz3LAIHLKfds+MefkSyi/J3soCOPkCT/Nc/ipfNZGTc1T5hOe54Qjf2JnRHfg+AV9zFPaaFz/mfall8OTvbxKvXYLRewQIjddt9LzwGSkVer7stS+IN3zIgC9cfVpOT+2jKghP7NAEVSPwGgk4EfzufDFcKcKQ0fypejKCaeBCve0Z+WQ1O+ytLyyH0QR8ddKIsxS4eP3fk/iaD0yOkfEtMDfwgXUDaAhQUt0BPcLjpgWfD3y304NnCpHP77mO8EYPxTY8jM6Hfse05EmmfDCq+YzRuOaOMyVIb4Yu8x4C/E8sDgkXxwt34/M14ec2NfMUKIUju49Tv2Ld1Fz1EYD02lc8qB5SZq69ct9hwtERLNfti++G2JZbL+wvEjuo2iXrW3qn/QRyF1MFdrgd3vAiq0kzHPBAe6fopcz0yK+YEW/nlkIQqOyV4U1e2R4xx2GEHKGtTIgeZiVNRCDZ0rYexiEJz9FmYVyl3dJrBnfCKqy71acQL4S944WnagIHFGn5KZFoH/I0kuJ2tfn5GRILwqtE1wK6oeoji14QVJhjHc5XyjTbyZzFsZhz70d9o1g3sbQLgvHg7E+ItYEkuiSlMclg20AMcDnaoq41PAqkGTZsaPDF5ByoKfse7mxnHH1HbNLwkxL17s9rei3hY6oKHb1XU6ihuBlEacp8UckZ3BFYpTR9WXx6YCUU38oqvCYAj3P/Ta+2LZGSvx4sWee104taNLlypjkpzmz8/Q/CzUttrwWk7GNeEtnQ8+t/ngPtB8p0JnbK48ol6UziNVnxiH2NPzcloxbv7HBNmvc9qbN84ZRdbED4yC0K3v3aw2DBh0QOa9ifix+fMSJhqW83d0b+cyu8Vb0fEAAvhVTrOWHGfZosu8MRABAoQ8jnTatN0oHJaDPheer69iraJP29dA/6oHehQY3HakI4SjA8A1LLNuYztYaoQ7JfL4EXal9j32CNb0CUVYOn1g2/Q5KA2JycVgQytp7ARPyBdFSopJJaPObmGMQvLa0ebRUJBMiVAC/exsN4wEmZiJ4qBybTDAwUHAxKhG+zNJxZrqjfBJ+6d6wK/j0c4NVZA6n7qVO7hjiWUYx+C5qpisYEwipt8WCjoc99HlVIy+4K4YQUoC6capI67kWKtQzdWg6XibQimGpagesprzArJ60ZSSN66FaL763C+RbyTK94/5nhE86cY+34aXACk3+DDY5KQVcv49l6UTfWLaTC1bPbt5Et9yE6mQdDoa168xtwDdqAeL6tJfSJObOuND94/KQnBKiDauqE+T5zYpUewzUf+9ePZHe03/D9thSUPynrK9bCJgboUtrhRD4LOXa29xFzZ0LBBz44pVGi3M7NKT47jWTfUOetl8MEZkPL+oHJkQHATGMmkJgNH6ZUUEdaPrAxcETa7rT3KhqO1Bx1MLN6Lpfb/vBCfJklVNeAFUnG1VHXyS0LNNrpKFq5mDDnzKyBWHlWL9kXe5ugL3rFehpbQjZy+vkYCajxKSlZYtRmMDtVToUXQ/6GLxP94S5dgtw8JYXPtFRDQSaPn7dWzuZhj3zr6pqWLY1SqHaF10dE+o1sbj++5zVPbe/JDe+mFY8J+zFqu+HKIQhjRwCk+wnQavAvAqB1FiKX1zONafBLlTtDmobaF1j4eJ96RaKC8pSEquEWquvc0rDq06RyvXwqSNtbVzVloF98VhfwHMb0ZpGfj48KyTZR6GDtZDwsatr0KIgzt00BEuqYGTAMvwjemE8KjMD3cbdGv70q/P74uPaByApUFB9bgNA0U2fvb9jrwyIlOnSQZvF4OUuMWJBWj7YyeI1gNmlljB7y2YRkNr4fGC3A9f7PihecISWcDW02JQO3Zs+tTuqmzidQpc1JDT8OnxxxQxtO8Duq5IE2KRNYRNJgmPIC7nywrK4x4U2HVPGHz9ht/j1+M+Nn/EHybpAwCey8zoNWvAeMNw2gqBMCswRiNkglRkBw91AOrEn9E/OGY3uB4AVooAj82NO/Ll3YBQdjejYym8IPNJywrQt2EhI9j+7RDBdXKFhfbYd9r9hXiu4XGDa1ZMG1Ex/55J9YkoKzuhgvSGj+O6lVwD2aRe5fwk8L/+y9lxwD+9VEUVBsSBVLAq+30kttK7H/Hk9Q7HjhBcxoEhUz0Pah59S6LtkxscQXw3phqhC20SnBjG6R1yTvC7uWq1/W83kOdbTzdysQzcEy1WlU597y32m9QX4NzZxZjRKzmIFZ0EeNL/DvtH4VtQdRrD0JYUbV/5LGkvepfS9FkX/Vu8s6CAPrKJg0uHXfJp1bNyUTNP5PYFZKd+ZmQEY3csn2lwK1RDpYw9VcAsZuDIhLtZAqD0Y2NS07tGu2Rx5lNm0D2Vxm87rBW9dcguKrvVZCQtcfdslK3hB2Jg3r9czwlPwBr5djyCACKNFd2rdc0uG0Dp+gfdtObafKZ9uvd8SQnYjKqOhffArp05wQziuLsXOx7P06E+HFUWKR67qQOzBIGfTCW1dJPsRwzmc+QWEhdeh4aXMgrizw70ABTii+2ea4e9POehiz+ltSslghyToHUj0IFPGSxqwObpnPLfL8gLxivXu+gQa0mcEcYli+4G/FBuRC/PdOK0T3FtjQQ9wU4cw3EDc8o/0XoKyN35yHo2EIvKYmLtClB6059rvGXUmY26HzqJwPbKn4AOMvMJhru/B9j8jnB1dtnhHPFVHIoZ0UuQ36+BpRq7hkq5gBVtzsz/ml3DS8c1muOGzg6tOGXR+muTfvq2w+YhaXh1lqnzGQdoz59bpYlQPtTXdnSa+GRfJilO+nNlg5lhssu3/IwSWAnrGbzUTfDxMj3DTMMC8PncgZaGp2kmFgjjIaTYHaxIUcPn21Hco6SGDxS4mv0WV+RzXAwnX5CKMPYcGxW5QvhHd8h/Rl2yUtuik5d9UlGbm6UH5zNH2kJ48l+ylUMv6jj+Q/nDQ4hRw3I5gqHjrfSDkICMwoZxGsaone0e7QZv9Ssk8n6R8D7yA2fokCRfPmqdvfsC1Xy7tPvdjrjLDu5Dd8wWJceDgug4WmdW9i2ovV0xTKyO2D1MEuaH+tm/Td1dbp316QhJNmN0ou9mg+i2YpUYdzGGdWvxuRvXg+E91jEOKgMx5Vj2wqw53yZVytQzoBw/AuViDDEPnaNQ+whNdgH5Y5Y4OLbr7oTqzJrAshjhsp1OUN7NO9yM7JAMO7npAjL2QUxfFqUS1K/3wmqYbJOxg2LQNA14/ird/MqjgZnrbve/9CG3sevpX+O0kIGhrM/XntYDwIEfpyR8KtyIElUFIJ7kGPybAUPwL9OmV1bHApXGQc8GuEjGdcCfBX2ezhXhBKL1zxtXZ9G/e4lVOX1Dh/G21q6fGqCc5OaOy+7WlFGgur1sElUGVmzI/U4Uos/gZo8aSo9V8k0dJzMbWYueaAB2SxI/lxx1ZbiOMLtMOuHqQUHG7yckqk7prfo6mQwNRvCpna2Qhmul4QIfY77i2IC0ntc8+NcyliSOKkqqERPQEHbbnvnKx9/6If3lv4w1U6I1ZtbW/9YoMTLOMsidsPSGdsjlOZGtiZBw68SC2pzQGnbKzogdAPNN4sCG3nnlzBZsJAqQNCkIjNEtrJgSjifl6vilLsOYxnWFy1L6JU2H0g5zdf3+11MpA/gl7Zx/fvTcIvjzNrFaxAGbOI4iQieqrgc2kHb86PRVqMAAVfDwPzvc9K1Ce1o4YgkdXR+1qE5BEZaZo2A1GTiIVBHfdgnj8z5yUqLoYzayGyFJy7DlLqiYqNyR/L2amIwIN1oglu8YxS6bRGKgEfGOCVFBOoCicqT7NJfdrK5Nt6ZTLCHVywSiPjUSbv1YwMYawxxKjzAwj/qC7cvA4xWVSkNtlD2aDfgciB8ap+ERdBaE3TTWpz9VabnQ9ipLdMOjX1OmGMFsmz4E7dVJmUDFZXbHd67gmc6kdNh+7jDHCfI4iavoeORp+frX4ytfHFW91SGaorc0+x3KVe9JLPYRL8JXh/yUeLqEfOEOTzmSTWPe/9PKFyjwu1f9ceu4ncjgbvuKYsEIRk4pqispUL0RHTg7cdI4hWOu8B4kJ3tgPd2q9SfGpS4vmAzsu0b7Szat4eeIptxsbaWqzbRIfQ+AK97QHw8WXVSGDBrpMUyHmKnwgzhGevHS63TiWzlzKHIF5uTOm+VNwhUBtPjFK3jiK3msX2LP/Op1eNNN/elSF+NARKTl7SE0Hnk2NI4C3xK6s5X+md3RfY6/prM9cfSTsVbWwmcePHhZRnT2ISNi/+tg1lDYlfkqwgzXrexHLqk262c+9UvCuG/zb86U2Rciw5HUSCX8Z4VW92fPanrLGdOg/9MA/Z22sYQJIQVrGtkFywu8idSBuU9ySmr5YvEYO2FHsFZBwhUN1ppWdl/xLjpwr1pRfPi5Feb2TIx6BOn7yWLS7eRtgAeN9x5/lu05zMLo9mek6f4BgXged4iT3gP+uRS+u/np8A7clThnuM9ZYdKyMG5FTbdUWgNFMB42TUvyXtI/tr4jxVBsL9P/IN5YAt34TlBdceWRMsPKPkXgjxkDl4qibgSGxIRk2LLIN4mgc/BQS/J1+qmBJwVvbHfMopBpOmCDv/vepexKcSfpu7KEXAhtgtqz1JGxNDziK3dzQI/IV5Onwo6r/jIq5le7L6wodXUztQQyY+tq6ZLXSafQ/wXmDIqOn536XVPlpTf2YLMA8RnKFDBt8jOxE1YvHr//XGMpAWx6dxvtgZokEcyAcVUBR70DObGTMtRZOf+geq2UWC70tWfhi3xX5T019ZQbBIsWDdrklBzqIcWP9ErusvFpKc/8uwGapgtM8D+bXPwX0H5QJ0dLKi57VPILfbi1TdIM1zzR7tB3YWoP6NX8yNMaLAU0KaXc4HQn28vEseRYFBVPdbZ0HdSj+COIl3ANLIwEKacSeN2lmGGyqkGv8qNaOvwNy4/kugq/reu6TBSCPvPbhX4yQjxyq8SjDjjIuBeDEd+sUN3kusMY41G9MmkDrs6tNykVx+cXRubsDqZBKwIikg5V9lqlZyvDobzBzCSfM+0PR0FUeyYzUkxj4Q4Woi4Dta7M3/COR5Qt4umZnKEF0dMTPdMONWAUoVaUcIIMssNPs2ZwQh/rLLX2qrSMUM2VAI/kFSJi3pveGYEFn/XNx04RknUn0gtPQQV22RqWfsWFnrGjJ7i3m1m6lKvRMDvWRVrg/Y8d6xxInYkahEZPvmebZ7ylJl7LT52PVEbGe1mbC+6LPFx8NYrkmfAoSCuMqzMmHpqT9F4pCbYfa+2ZejwkP971fK2NlyXbmT+Pz2cdV9RDRRM49FG/GaHcO5nuwMoh+pelRVhdYZ/jUpBJuFnkurJDqRFB+06aU32l2I6hayriSG/tbpSagQJuVQgeg7biYnE5a1K2U4oxspm3O3moHvFB6Md1Pooao0ETon5/KO2sAG9Ntl2vX6XuhjCpESzHf2mXWZkKKZQY+iondFkts2eq+lLzcDf44OwE3ApPuLNpaYjaoN+tBp+OQ1qNQ4OdnI0x6FRiHJ7/hYk5pO3Z7EJBkk+Tl/TUN0t+8D9UIrwjoi2ZZSspQJGm5AFRiIXis49FKLHQgkhKciFCm4+YiLl3Tk78eIWMNppZI6oov5RO7SfXwIsoIecaACIA9Ct0kw7UMXFbuWLOYNyECKBO7xo4hBr4SEH8jzeRP5tYBg44hbAxAtCdh5KID2VedpF/k31Xz4JpPIV2d+YBVupOw3EIhPBMOFuO5c+TNOvBL0U2/hZO4gCa+dUtSHtpxtSnJ2hYcJxahzevC4nKl/UTymOcprfFKQpgkyvWT8aPqO7Z3yBYhT2RwVmzPvMsvFyFUfMIKgMC9AQ4jo9Az1+pE9r8X10dX16Yt093muHAhYTHImFIezZkeaxoyb4pBbPEcOy3x1IwFe4P+Rmvli4u+KBzjjG8yn4LQ7BBTJjYxyXDxZ6Ff/II5CFPl0gV1ddmibQW3pVYPcQu2//vVBYBFCODjgttArUrN6nS7tqgIdK/aZGu91svT+hotO4ck8eSaHXOlAPT92XYX04VF+CoA8dPYayp5PyAyiZi1/nfqlPvX3K0r4WhWOHGUO+4LYJ2BgarRURq33CwezIlfga3kLGCiKjMeO5ZcrbudPKG561lnRq6XXFNPXsxD3vpuky0/m+R5OiPVoQqFv6G/d/M2C4k6i/uH2JtZCKfXuLs+Jk0L6xNTAQmyupGo7rMDA8skP0HpSAgC1gn5oX9ZqX4tbXbr/ez1oINBjPXrVBZmdWLR1E5Z8MewjcYTJtOI+UsdyHeVstr83xJdUCRwE41Y9Acgj4r9nMHPgH3juR24cawpKEov0gUYRWEC/y++RT6KiZNm/C8YzHWU9sNJuE/BOUtWS6O6lrbcKPnPs5KN3tB8jNSoudBsWtVQTQxThJPTgolPcTXMOnt6ZME9zNnP8Qnm9fCNIJC0TZ+ng96DZlaMxes+xCWqdUqP0ncocXApI/IFIsBRPklwxjWTdFVUudC7Uom1EVgFqrqkPK4ODmj5U2PaJHFmolrEPQ1i5CiExslPLq+WfqILBP9dUt/N4czMyieunvvBzbK5w0sv246gGZtYpNTRLNHz5Dr7NgJ0/QCXsRcC2jMbjhGXsA5/12/6M0YpQO2IPbPmExoXVh5l6kF+326XKOH5WU/Xz9FWtQDyL8aiKW2NCh2zL8izd6t1yNMRBLXLcmiHCScwsAxoDXjupL5C/ybfkYspARSOn8IgjW9iuGhObTDV9Mv9/MgyVssVwyo+Lj1ZAW3tSPUUcqnYYdH74LpT2Hqp8pgEKgZC0RpJevyJeaz+/CaPJLxiG8PnxMyyVkU79hsjeizB8Yk6bgDCVgc2hlmmZUvOxA4EADlmsaqrSHr0czsPa6CQfcaLrKB04WJUHb9yBzsBy1ah04IwZdVlioKQfRnPG6HeGWH638AdolJa6lMmTclY0IdoYZQnYNVWp8R1HkeObKudJRqdpZtKLjgqJOofdjI+vX9pj+KeM5w/ZLx5Mp9oJZUCvUqdSV0bEtGhGSR6MEqPlDg65spah+L9nbOGLs/XHiudlndoLB3486kgmBIXJ5e8zGS2A3HT2Yk3ZoUEuO+KkoFXgQu9Fa/GJxpg0e5gbYfivWseJWhVIJGBFVSIdo756wxYXLBwYXoAnyelGuUByw5Y765Jb0+Mpmg/m0ebj/uJ8+ozP0Zt6q9OXr2QlJ4OWe1oUHK4WBzDU4Amd1vjsmhI++Teeoe3b2kkAxzNg9i22cG3lOL/8BbtEWa9vf/4N+FdcLU+PMokkiigWMe++B4sGLkMl+wwMNXqudCWzfncK3RWD9nqqkTy7ER/Iq+sg2/lBCoQ8NnLdQyBA+ulu2+PSnPZObMcGrwpMTfwBx+pho4HBMwIN8UcK9S9ym+6VaGZog/lJr6PfCSlytHwcDGKOkR/fa95rQux5PwdFsWdWfhEDycWJUvGDhyhogE2tacHDlrhd5JlyaY4uTC5SnCus2sU/LO6P8U74a+VJecJfsd1K+LCiFPaAFmlHEc4M/dhPOpY6JVh3tBJb1SLBOZeWCBlP6I/QyVjK9e0fQQoQ8K9mJl1PPrCcyjM/7H+dQ/9jqfExGgO7B5fXDiV5DlXQYQzk7Bu/PHzrNWZNHsEUmyFFWYs15BZl/un0ZA5y14qaryL9waR3Gj4PNJTgiXeTXoXxPXIOwbJpiMmEPmrEQuFuu1ZisJeg0zVgSfJaB4LqaGfoH70JMrIzbEaNDUp9FiB9jZb+LUmTBt7yR0tIwyrAbuuZ0l29+wFjXWTQaIBSVoJFY5M5ME4f8aftYsCowlb/6R1S20nd75N6V3YrIoAl0yxQwA9FSNdcdtT/3ME1PbjBsmjm3L/PevGFTgv3Jq7mMUkWWe2rK+IO35039HzU+VYtRmv0/cSuKAEGfTY9v5y4/PlN9ezdnbrb8nEcUhhMQLCtGc83m5T0Pu/rxpoljQ+FX2MgJPTkBL4GpdwgTe/8YTChrCALrBDXeTOrOJVqHrhW+c9XFG9Xo55cX0wm0yWxINbv/h7AWFJqQ768bWLWf+XXBpz3Rpp1VaEtgbMpSfPR9cRGv6tY7yZazTMNfPfs/faIvwtnazlfn/rvIlamHGLfMxeyW95N50hdIHptPjKbhdf2YRp1Qs9psqMruXLLRlTYZZq4OHC6Zedj/sQJlq0wtM4IgavrSbTeKRAoFddOw8mn+QglgF1fc1uQehK/Xs/QYxcAR6xfgNMmBKcypg9qZr90f03mmLIZeA0k/UD3AkFYWj6n1YPXGO5jiWzOip84994p01pXanJnvJud0fG0cXdBKSJsVNVb83O/0HDxnVME22YIMVLj3TZm+pLUzFy62w0EC/fsW54vXztkn2zKt3CaUrsVykLT/aFhm/WyxzJ2sKWuPo82yCTQg68NbP1JjT/S1ooD7MvoiFHpmXRUZrnWZtpDtd0yDah380a9YRmLEkbtu8XIBrpD3pccOz2cw5EP0vWvpf49lJJZhlmlL6zdPKkbEgYUVx+KAexxjLaDEdfG3mGN3QC9cQBxdSgaxDFHRUGxFXEXBq1XGd8OFbak0cXslt227h12FWvJXZRaPO4Now6UzP9lnybDECEeO/FBnXQu1ELl5iBzk9eHplXhwOhQ2AT5sIPQ05Q+fQkr8j6GiHJwi3VXEPNxM0Ake4IKsXBaraAL9aHu/gg/McMGyAeSBhrVsOJXVv6Rx3m+4qVDe8Q/7B2gNyOU+uqV5uG2mx+rEMcf13P3rMWiQgGHAtMXpHxpJxP70NJ/U8iIUJbMEESNFmnGsrMOpFYnfanHdEYmq99CCPyqk32nCoWd3z305Mg9HGFmyr+//4VBLy+zZ25tm+dqO3GlPIn28Kzxc/aQzD1YS0xAcN5Kr2B97ozYbQMGs4Ipeprj2mWioC0243Z2sZ/aXNDRtWcbbhUuVUQxYO6q9bxs8bAN4EzjgHnKiQ6d7TjZuMCjIiLGTzrS8/dpEoh1BOlgvdXXYWCFt+zLl/zUNzhFoOHaafFGlf0Lcd7DY4COIJMBcu3CFv7IGChk4DMBCNS18W7aY03ZAXd68ZxIvR4BO8Bx+haeMOvoiI39U+qZjSu+mUc5gHKVUVNOn4zL0l/jNSLy3Hi8M+TBYS14YCu31juKDSDgBJoqv2apZGx/qlaLJJ63UQacZhojT/DF2/tkYjzpG4MCOS/JlFYHQ3ypOOl/wVBRrSJylPLVHfujroU/or2yQXZwgtl5iWneVKdg7GdSLuQIxjeNXafcRsqhn0TU3of3xlPREj4kI1stwU6qhDR2Jkqc85etS09LzxST6cBbSj0XBlk0ka+VgQMMdWpZxGAghm7eHyVn3sbgtLt1QStf0UBeJqhKrNa0u1TM2mDTncVP2U3/Ti/GuUorj0+XrSqjwhJGym8RadQ6oQ5ifKyfcfx0drTBRSM/reJU5iNC+cSbDwNvgeA8VniLc18szOI/k6L9lysMNmPDDS8dC2qo5eBgwnIfK9ccKJxOAS2NaRTpxJPtj6f3rx+dYAr8h2A6aPFutEjN4h5KlqQusA0IjUotTrGA+U8EN6Xy/oMIelKvZuaj9J9fFIU08PjZqtEhd5Qdw7yUehjI9VgNODCuiw5XmkweT1429V4rDD2Y9Srr3Dae608raqnmwtfPrm35wfhfQpFqenCdFBy5dIWDUXYGOWewHzgZNq9jv2kyUqFhB6fUqH5+G/s1YHosruxJEM0lXNby6PkhoxIif812d7MgrYZz5qtjyJefzgqscPSXfEjmlR9K20msftLvUEA4Yg18mWj4s95920sUWt2x9143QINq5cRpBA8K90Oxjp3TP+TF0lIX8NaMoIl9FTiXqhfmFHzP3xCry6ghnkDOIY3SYBm/DqUpC6CeHcIgFyveaE4DTfw/ZrALWa07k8Cr5wgjQ7fVCPUdBBt5sufutdwo1n4+DgasN3qEWQj2hswh+em2YWD8DUq/4WeaEOXVRkXeg+Bi29DIFkG12xL0xmRfY9p7dH+4eoLZqT0jaaRwxnRtZN2JK/8Y+UlxaSPB2ngXunS+ahQeqoR0Px9bJGLCXbbFHiNLNL5Op5HFzwchB+RvNK9V5lilr/nhudhcJgsfVU15GYypBb9FUX49gVsrsJ4uk3cgpfKlp88CnADUT9jRucDbvpm0nPk7x14HrDBVC0kHdGDBZnnfvRbwBCec+dhwRnA4xiLNZtEN4JP+0lurBmDyiFrPilVZygZTPWU+AWbHGlHmNq9w2KiKEuDrl52KuI6KfgNHijeSRnCqjA2nEHRP3/RWZmNpU7NLxidXfHuAPpWJHJcwV5lCNyPsPcJTpYMKRJXTZq3IOj5fw7DioATj5+mLnXWFFPWyXvvRVMccnNfRwEvAX3F08STigaaLv3FVqBRCUx8BaGNZ5P58YhSKiJgMUR1OEJqXAUfHHmL110itHFomU/GfZbGcobgId/+UYZyGe1X3uD7n+FDJIsY+I2pyIOpyhtwM3G+GHVSQUadfUimT/IFrsNYrYHnEMdhdZ0RutZ7duAi9PMZaszXcSFFFKAtmpoGeyk/7Tm+Raz+aub4oC/PSmwawJl2XkHKSsD2vwqVM03I1tiaNpkjj1YghKyGt7eKDOJRS36Lhk4Roy90zziI1qbBA3CxUH2GPfEpAyr1w0PdDupaozTtRjxD/oz3nugv2eKmYozI3SrjhOw8NJv/T2itqXBor7zwhdluNNL6X+yt9LDxP7rFXSj2bz9HGKK2ra/fyIWXWQTVdbU6vY7DR7gMapwbf3zzmOlpkYN6reWKBuIFMN7XVJSSA4k84WLHyKvkO6H/MA+LiU6cu1CK93DF4/C+1e1NRl73Qvd9aKVUFsVyYbnmQDDCIW8PO2f9csofsYdXcxhVJRgsCAISKPMfAy5A7gTfqKDoEwZBIKvIUnN6euCf4bQngOMY/LTGzpV+U2apxdjAFLZ/XZOXevnY1tCkb2wFI6NPllAXAYLgrzPu4olJl7VBKwwSSoSYQWQWZ4BdDJN9gTBik6cFM2AzlMSnx+p7k8rVUMcG1SYpSxvhJ8I2rehQSpUkxFBRuvnZSCyy70oCEYbcJc6BGO1Q2HwcsM0HTz1VgXaSBBXmR7oABmb0npxe//gQM9v1hspbDyTFvIFqWJcze/p/+uFBS1mdCUl1rIq8p+RCys3ljiN1wgZhgUwWwYeX0jFXqxoP3vASHNKMZmRyfRzMd0lwbE1GKi9mU4t2URC9YmGc5dK/gEHo+RB5q0LHKMf+R3Mx4ifVlqs+f2RPOJXNYhjtJUXJdBDTEHBwHitdLX1hZJflVuHflA1CFZIbff994PFwzEl3gR8dBfcu4MjqOMMfplZkeOi2j3mTxFi/KFg+Qmgo+ESrDqsHCmgYmY2YjUr3IKtTgVp3HQKs8Xtw9JWehTysvoIyqOcxFvsVltMDU2IFtocb6CKFibN78fsTPSsPLzBFnsWQKFWlCZCr9jRAGDLw9he4oINy3aCQmfnIzPmu1GwqhivECOrvbe65CiQBVNAH72q2jmleRmdRgGV6ELED7+l2KZswa37iQaMrN8+Hoh7qU4d6Stsxyxc0CeHtcv+kqpx0xy8oevn1UHE6gExxAX0WC7L+MdDh8x5H4Ko6xY4hKKVQgqZ6+2a0noultW6hXh5BeanK1H2HCkIGZKgR8KManFInrkt6WqK0pd2jwwa3QFkd4Y3NUJ8wEYPuU8KtY/G3/lYU1JaU/8TUa7B1+p5OgON9Vx42ayr2CRo/2yV56oYOuWtsdDggL5ujV+RIq9jckrHVcVfYuuFBAa4EviJuY3MOcxaF5EJNetaT0jNMDGF4RC1Ouxl4Hv3dYpsRHUOrnDiGVZ4PmnGe/jMKh6pi2uzw0JvYkVd8k8QmwwURTa4Q/EunkUysFox4gBN/VRWOMg5eG4e2JutzxyaP8Ia6r7LQN2JyzaVpieuiKHJwMG5INNgUKCOLG86joSrZwxeXFicEv9koaZZbtYhn1aBlAZ5aQAKUL2nPPaCaDq3o9XiqoqonFUbTo6FkMyloj1QeW70OC2I/gbgXLVbTIrThPxzkq+SkrXyShmAhmf7VYtS9ZTzKtLVLnesD3JdXcgNms8yGPLn/Jb3gMgtcexW4WAnz0P3UzwgGBPeGnbIU9w4nCJg9DwICoey91QkVo7qClmH/8JssRdwqqpHavxji8XUkFpnw4tC9bm+UD9/EAQM2t53UZrscAP9Q3wlpMq0SDQI/5SWo9t5Dqu4rXchZ2DdiNCBx4nvRIeTaGRFsZVg7ytcGNWBAuvAWiJG+zJf53M84Sh0BQg6VEHiNq31ypj9GGbtUhSDGu2ekXTC36sNzetJGGcNWu301ixVbPl2N3ZdjXQFuv5xme//n/oHJWd4DT6K3jPnKhQTNNlh4/u6GDkFQ/j2lXQ8sqDAaQy8OuGGarSUTvRWvDX50r1ZyZs7mXd481wznPhfs9EGoluMG5bSAqZ3oCk/VsRSbjZM50Y6fMBeA2DBVuPOVwuQeAgoz6r2mag/N6ZqRvYCbIGyt2A/NP9F78w6jmgVw+ns2Gb8qfYPVfgg9KWxmikE7V0GNh8RyrWiwoA0rlbI/TBiQbZLNSI1Jb3GnanzINLsArKY9qNurBuEN7/uN/8bNS/23mf3m7uS4kqlSKD6rorE0YDj2CUgbGRY1WiDI8ipDTMuZmH9wYk0G0qTw9Xhp88ln88skCmNwd8cyaB6+nPCVf8b5Ih94cwjwFgRgkY4gi6+9axK1ngC7499Mv4M6Qj9e+isrmjG4unc21YJHnhnjylPLdkOf87PRzUfb5Z/yIuGo3Rn0OR+enVcmg/ryGpsqdf7zVqjZzx1uwfUbEU6OvVs94AaNBJodfzI7kUYton8eyOZYPF/nolvTii1WtCtxwd0LfFDlKEJaPwIa6TgjYnLVoSgkqWH8y3YKNQqjKaMI+qKLrRfNaKCIk3UyERkan+N1sxAbKyltiUw0cILZaqCbwUC0Vl6tPFYs64WyY5v92XQ8fELaxsyACZ5x+12f9Fa4MVnHy3eqZl3PUp4XhBXG6XeSehwB0W5dKu07rtzthXXQvdMDvCsBeduoojnOpmfw9JP/6TfHqFOtfTzTqF3wtUy4C+upTsjGr4vgAt3/9DeoBmshFt5iahgmMDPQmnnlwSi+JOJEqnVNJRwrRAsHn6wdSJb7ipeOBP9yE975J+DwptFpppH7jdnAR45aq/fI0Vocsj+Nz9Y1UFsFFx3inf7LDOlhbyFEQP8p6opU3hFbkIi8vORSlTDWufdHB9tMdgz20DjIFDPgjBzkpv4w6e2prLpDvquUxp2rM80GguPi523xPgYS8y+iWfcgZH2Cv8AjZphtAdglscPeVlBtC/zdmgmOTYCEcrjKN5GUeAJDZWY1JC4P94gu0LBrS9CUA8924HFW9iWe61eQB4HidERqKfIRPWUqwXkI8Y2rCa2SbxNfxt7J7AdoJkGmn0KZouU8C/NbPEktn0YQDTSPsmUP0f8v1FTxCUpVGy1awX3+6aaxkmw87LbTrZSsLLnh6BLmznBD9cva5f2DeVlpWhYESftiuWYOdKsWNzyz9jNJH4UMv+soUuZqxxWIrDYjBBrAih3Xlb/RzSwvqKVn4TK4DIXSvBG2VNIkd2I/SMaoU3yzSYizfPKT+qhkN87cN6TMLNWn+B5IoymMf0G/EdbeEhyHCXCvETsMtFB2HvpW6iJwVCnQO0MlGIOQK0kJlgajkCQHNBqGVheU/iMpyKPeob+FyYmj0ZLzHD6WOxyYR79wWSGBv5i+LrAS9qDdsdf3pFE7b2d0MM5obRPh9il6qJXhU9GBQD/TuZfpRUVO0nHpktvj/Yy30fdRLkUKihTmQNJbUePBH7eVF8SWW256iHMY9c2EDHqOHRaq3hPqKfgHYE/FJYp4Etnkz0gm7WYg5fuyesz8JASFxdumwBWRSARDmEtCUxY7nqHDJW1nkUntTOl6E/MZH/u6Gc5VraPKbYRuRMonfU3CfMdGsXsJ8lXKxb1z40JzHAy9WMfsC111yzchWNvZah5XacDMmzuSFGWBc78nVbCjLJ5iUBgiODvglDxbIByq/I5EQHto+TqJhbf9tQYlevRJz2T/wWqlOdoHrsaKWPfOro/bb4fD3UxznmFnkLfz5l61KnamYL6UnZ7NRO3f0moVJJFJw8pgFhqpCqouy9GMJtSsg9kxBbYDa+WPl1iLddu14auSLILzzN5RJ+/LpAkslTY3agwxGKSOVAHSF6cm6KQmmVuhCdrjr3JQA8Ge+H2izQ59zrZlfSRXDx0gzUegG9wwTLV7T6yePkCkqSYgCYjHU52lETFVr8l2RAmAygNFVjVffPfhg+Sh5AmiuNtLzzK9av+KrzJ2lNP6a5nohnpB/qC+iEgfWHCm0v9RFG3OhiF0zJ/fpIgDusjUvKB+mSDB3h1GGGbc+RcZunxxThR1jMLsnMioLguxo9BNbiUWr4/ZRaf9miajGR0L2ewiulMKZNcg0SkZ1CtOY649C7Zl3gm5WPVRjZ0gmVKDVn9WfQyxW2P3rXs+nhQODLs6ovg7oguZeLob2QUpoJdNi/2VGeJKQT1O+zIH2v7zv0zF+ihtfvJoGgaNPE7jAVBX/teoxSNKRfIlKCZDmW8v8MMdaRp45GZ/T6b9NOGBQlFODRft4jM+s+DG7NtjDtq3Fobf910pvvigeXnfFLz+IdClAtru1ljDaEF2A66vG/KVWss+DbhYELyy3+Urd/ldTy0WsWJQJ1YsPsKxWyxpk+xaKtE6d6GYIcraKojwHrZgIIghr1qD1//6txjsbMAcuDXCRNj/+gn2f+jCYiyVg9QxJaxCDw/I783X1b1ZnMEiDpdEET510s/EpUv+tOuyihGn38rWGYKpyEUVHhy6q0lD8cZLzbuHc+/aoE8BWr8WFp3H+tg6NJSx8b5qHKcT/6Ea3IeIu/XWKGI/F7NtQDZO3BS/d3SSHxWWYMEvNB2bQKfD+ZAUFkDk6x913HpAZIcGBKy4RtSv6G7uZDFA3GW+JQ2ZaVXxk3V3kpc04A4M7M84rDhI4GGP/sG1llL9kzOwXeiC3cHOLLLfW9G1SR4CXtu4+jX1qkwF4+GYUOeTWoLwjJPUF7M+SNbclVmPYdvY5Wln2wtnck82hdKgUekDb+188kfUStHF51ETEPTcq0RY1UDmt23I5E1Tz6k2Z2+2YkvA/FDjRFImsPAphi508qQZiYJdaSN8S+Z/b2rc9PvNNFS1rTdgkRq3TOO2yEKsdDjFS1zelZSAtMcsj8nB6YUo7E5bPvD1cI6Tw/5yBsbbwTCIgcJERu/I41Jjum+hruXSy9aYJL9k3AvXQBgE+nYX4mpvGX3l1JWvp9Wy8BGniDdBFu68PWEIodaL5X2e+Ak9oJ8QqYLgg9vIV5+2fTWwTlDuSCLUebaaLNCxrFsg27ofstdhv1tEpKfbeEtHInUAlllUbvs2VwdbYrtfk9Voo+8FL3/gS7lTRF4YaCL4+B3mfpqEXuIa4fv6/0GrkCApXmdBi8xBdyt8gNTAOQMb0cw2D631+fkInOw6CRgdVyagsr/HRBbI6YsZ/ZTl5ih1jq1VPmKn5zSzmx/2zZVhrW5CcQwZ1Wv9EmfpWrTHyDp/Ez3vir+VJiz8VifLf2QyEWd8ZCbfv6xGI5MSD2N/hqfIMEGSNYSD0iIwkfUcAcuKPirYThLZltvID/NclhAvWsgP1uA/bvb+0FX03wml0eu4d4wRuxI4UTUGEzhSs+4K2mr1J7XOt0KkRqNh/b9qEcxEx1k85JrNksWqeiS3TFiANyC04DR9L2+YBvxHlY8D4pwIpUDCqWHzNO1DwVnxjcnTUbUq9iSCG2acFB433zSA6cMEOckYcMUqspsZLRetM7kX2qzeZU15X8/J3r9NvsUW/qYDQPrEalIvP2we2eTB0NHLqdniiX+OyQpXbo2z8t9ujdzHPrIwz/Dx7pxubBi9PfTpDYRk1Ems98CQcl+wYyoEO2GJ+TQ5ZjW3irxoqGG9Ei8LRV9vNN96XORpr3u3o79LV9tEvOx/2MbeML0avq8W7pGDLxv8pjJnjx7CpIcGUBD71oKqMpcRIGzML9Kizl286u/I9+/YgPl2EOdex0x8FP1d7mZYfLRGMmA1ab7MZKY74M/0DbEuWydCSszLPMEDNIFJ62OSdbaR4lvPb6tn6UKeUpZ8qCTHpRlhp4Q4vBPrhQZG9R8lHz5WIVkCb35yoVXtkfWD3/Ex6NHKd54BaCf5zaXPQk+GpeUIedw9QsRME6DBv85M/WDcepNs38C3ZiqAMm5jS4Vm500BA2+lYoJ79Mpxk+1Vx9djKNiG8/MQy5QzrIEs98LZmUjYIblo/PnPnk+/LTnNWhP06UzJAT5lHxfp/+AYi/jbeGZCSCBgMjEeT0+DzFJfvVVzbRhparM0Vr49pcAr8BqaqL2GjCNQg+nPq+nqCiXK3BonIvbqlDsVjBQR0NWC4kBXM5IDaiQe1VyJgK2rhs4WWc8DYWxjGK+jnb1s2t2Wi6C8M/8j5QSQcF+wSDcD2x9W+rxnrDfEaSSpH57XRXdl6Om5aO9EtIgari7AOYaEHUpV3TOIIKv/QBsWw30qaKjuTFJrVBIcQHpqRfr4ZqmTpbVB4QnhS4bgMv+L4u237wZnf9owZ6tF7b7s2hJEVPYdUHq/Vr1DMOeCUE0QdB/Vwks63gBuUigZR1P10Pe/60j7WLHCnHyyDeYzAlr02kd2p/fotwsyMmBsD6t4OzYx82+e7zF5ZhkErPCTI8nM/crb4WXEJ0RU5rbPQL6+Yfcsb+DQOQ8asQ7PZ/EfaSo7vp5MpIiV1nVOmJL5CTJPC1fL4ktOoA/cBca7AVF8LdcT4RdYLe+EvsfypkjTBjk65tvnMMSsWu6xgQW+jQPz39ZCjcXERQQrjfd/3a3mq71RejpaHeMIIq5E/Hi2rE8rj1u4UwtqPcECmsh1gtFkAxo4tOVXaHAAsgzjROic91n24i7UsmsusbtEyl6yEMghKxDENUR57iKdfNJuV7qLiVSsjSemf5ldBXeAk6H/L7SGYmHAehK5RBSK6WZrcmcTEFfLAW4efp2xDv1wXCNIR8EI6j5uVk5yMTCGD2o5B68KSQkEGmxbgmt0FTAQ+BnLdWOn6n5vx7sI6ponGaS4N8j7GVwDdomD5OAKA7eK4+cjF0lOmwezvOZY6pZH7QOUPhQH3SaurvmTt3F6+1f2IXOIWeqWATiw6eRGcpy0uh88b84K21vXHARXjFCBW7qui1wWeUHsr+qSPjPqNlbGwo1WBwN/7H9s6mFMy1N5AyNR9VHyQPhYsYYQPb/MszCkRoIwYmcFbkc3bWeXoFHxuv3dHU5f9/EOhkBTB/mSApZDha3swps7JO6BW5ZPKGK1MKfN75j3D3T4D0fSDDvJNKf6Ykmv5hBn65SadEjJpb8TktiofXCAZlLxLtMFwwb8ifeF8sCyucVAga54BjZjXKV9cwdAxmVNoD8FrPqW+KyR+qU2Ty7jojuYpGboUY6QxQUaM/k++Dbt6nRs5iNZKgIKAlWdfR/sf5RGpvj0tV3QQ1aKVTh4Ye/P/41YtoayutHeMAdF1m+Mn+pjXe/frCY4OH2Th6IgX4hLYvd1G+676YbwZFHiwbX78PgbSgfowoR6/HasAaORnT19q/6avQnM+xD73SOGQ/XYWPzPLJu1UibxeUN9TwjiH0xXCpixYm7pxt6gLEdxdnRZ27A44/WFwqv4ETDEFi281JiTzj5KZ9nkANiCYLyemNn/cCUES1Cg+vlgorYS0xi4jx/Ipxjmk6kp0KDCjrXtX6cVTwv5c7TUM8ppUP3aViwesIOM1T2cgjmYM3mu0NBQ9hrT7N2XpJnkoGyXZkinqbqF/6aZ/XkC+veva5bT0wIWueoFgRbuWVr/vkn/Rfjqw05/shHCPRX67cYyjU5Ml4yWXzwDD2kyzEHKCt6Zsec3wryaOu1g+cjf3SmPXupTZCu7Juqb5uJ0qqVTjtsBzzu/KztQHuKPaANcrRXxx/CAEMU15N7zTavPaH5xNb5ZpZcqnUd6ghnFaU01Dnkjfj7ZWkEVt4gjrNOQpIVfTSgCZbre5fHGQd/jItuevwf5GQNCxmE8TrMDSa8T6pCuwITdVYikRpFzi5qIwO1/Fd/xGepIZDQD3hqDrvWcsCg7YEAUhCZPndeq0iPI9oNG+aiD3NKAmPgBDcalGDN5XRyGMU+9+4acrwPAPLPMkWQ5pYH4zyiCqI38Cy4G6D15qiXsspCyBVpaIx1gEUhFsQo24Gy4EeR/agMdHsFX1DShNDEzFs9a7HuJdcJnCz4cWQo5q9D2N09J/7VZZiwtuxIiCAahuamJ3+8Uo071UEhmeBSj/ehVvFUTim755D08hz48SBlyd7UJ08yR+87Vlcyt6snrbis3QSFDOll6hFTDQ5XM4cwLviudZhQ6zpq7C4Veq8t5aIUdzXeHUp4OBJWfku4NcUuwlZjPkozH9tm/2idWP9pFCnGooWEaAH4DFYSo0Wq6LidM6Qur+YiiEpT995XzTWLxAvJc26Qih8XZLFeGIyiaTJLZlKBwcI7H1rUdtktB+n1m/7jldQoIT45PcYdbPjX3Obt6DJhSDlhqz3aQegk6y0NwoSxNSveM5x86ZOFomrc1WBB8Okt2hM0SP+L046zUvH8UOoj/kIbdwRhZTXBmr3WSKOmIPu6Ohzm1X1AetsPCnTPTiLhhGcmNRl0Dunht5RFlxF2CWaNDB2WWgWr8UyHILEM0AyppCye6JFwKS0GwcK+5I5c5YTBsWsTpApzaXdouWWR1YrYCrP+XaVF5CWccahIngIVr0QUw2BAulA/trDU6rFFT+fN9NT7H8YIgWUIE70jYyxYd7zUDAw82fl4rriVcvU13Fa+VPY6YFDN29sr9HnuNvmFqwSTqV34SjFBsn8iTl/cTK3HJWQBxzTEK0E/Zz8Of4rEmPKKyNLrrrGYazuxVJFr5/bIrXQVoMYyPxtuOaaDkKaBFusqBE6k2fak5tfdUFT1COmCK8FS1X0IDArTBuFgsxaCuUS+K6C+Gsthd+vNRqJ3/lmaig6wpLM8ppY23gk89nTW7LzHI0GkEbdFXTWAEqecaRetz3HU2ba/bjU5MhvmQVN6HQno3+9UYHI28r2qAwvMstq7ZDu4508Dc8cw3MV0lEUBDyWhmnKmDF6suFQVeXS7YwY8nqp5Fe3GNxXqlJeg0xItMxc9hUiCNYZS6EsgEND0bVQLDPWYzStBH87O48bTn7AfIsW2kcrU+JqsFExTslSrPt2VEf9kcNoRiu9rPQ4jzE32BzIySX+m/+OM/ZFkLqfPR/dJ05zxR3arD3Xlhcea/XYElnIPFogum0ik+x9hXF2kuss9GJnk1YWbAOfCfCrz5Oomq9R7QhzvxtNN2jweFQmu2e94YCJXTsczMRSj3NUAO8mCeAcg2e9vnVX1F6IzuiHfXZ7Uf1XpE/tFjnsm0xZP53Goq0kmMyilJGIXcRnHV/RlB8q8pc/0hjF2+BT1Gg/60W79Ex6SfDyOUK5QPnY0xlUrqivuAdX+yR4zbP212XipC2wjQCJ0DI+nofItbMNa2qPgN/IfN9hqxPDmS3DhvzKQkDOiSaex8dhpwjf9U9L1OnIyyfspc6VFycduvKITWTQJrLkQSyntiPm2FUaCOwWXcrddbUdXSAY+MLYP987h6snZgvMDSBdyMQxh65HSrgacgr9zh9/b8HjIlo6ojvc3m7VroV1LzcwkicUQJ6Ksesm4AOENcXltG1MszGQRdXizWhzhOGiUoHwl2XoijA2Nlss5VXopBiVDCHXHiMv6x2MM620uodQHdSe2+dbnF/j1ldv4lPW0CKu124CQwvdrxVWKo4qk+8UXSfBmC3R+V71am+vKs6vUKZ4BX0iF2PxcadId8fSbF10Hldn3waDx67URtyufVMNZ+WKfeP5tBPUy1iE2crjoKBdEmHrorzzJUz08CmDKkdr8s2A+ErZ/VCte98GWMt81MtVBw+5sTHcbRkZ78FGdlRa9MfuefgwW0IOuaaP9IULk7k5bbXf2T0+vpKymymPlcfjjYTgsWosKuHZTazqK6AZ6KKAEobYuRTCBVpqbXJgWtKXgPGOCixG0sK3rVvRrEn5TZxdvW/IRm0KZ+XkU0RdieI6QxL+PC+As8Z+Fy1WI3Sb2u9LYY0Sy7XOciZ1DwjQ1E6Z78HW7MhyJbdzAMqsiGbGvu0sox3qGJR4D+0tZXyMff7GfNOIIDu/cYnqnfPl4+75lQprxS9AWLoITlnqXjk95QuuIKCE7Dchws8fVNBZUa7WS4d1ax+FK06gXrSj8476spFhBMt2X7eK6zm6rx/yLnpwcT6MbxZCUv9IguK7BQXh2U27HKt6+i7Qge5iySlRP/OLNGsePuCexpDRbl1Nks6T//+597nmaHpHJ0/uI0Ctx0BzQhWhwP8OMNwi55Ef06CeJJSXldIfhwB+pSnVru8GxTEe2mZKe6pALqtcpLs0A/3YiB5GiSqsqmYu5L8FXN3qU52EUcFya/+l08UPCIBrLStNOSgI8bVsT8hoecqekCBU6QbihtetbnBvHvV2kTZsnPSGc1Jdx3lOqB/jQ2xZK1BMM4ywHr7GCLEOWA/heqB6mFxSQt2kexDHGxgSkeuI8kFF/abH3eCAyZp420wgxUeiOjt3uKA2M09HVmUvKsKIV143cy3mM0ZHVco9LSJ9YqrrjVcnQFO9csw7WHe+cj9HyMedwOWbDdDxgNx4xFRSmtdlPY+HXecsWaBS71776N/m9sO2hVWW3QX/TDO5bvDRyKeuHr6EYW3+YtDkDjGPX0gRcbf1/AEaXpQC31c5Uk974Bty2+QxUHJZX7l/9nWzIArGdKd/D6wO9sZLugcjvSmembZo3E7Xw6n1VgIjh5ZV1MENrI8k5tG8IBSqNciAAge3kC0uj8Hw1+1z6PwEC+KQhOf4T9uY0jHZ5ktq3sqQTyJRlQ0etVfG9fzVuhdzcnIXvo24kWwv1j8nuL+1OSjHNbQne3FKxXlTGJgP7kKVBVIPqYQlo1bLBr0W5Sk39iMhdT0h5X3I4MlZIvxQVgL8X/LsYC3cEK7eTbUAkBZdDO5jnSFsr/zV3bBdqUOluR2x7PdikCufWnsNk9qUOJnsdoRoixDWlpdMQ2I9Th1puHDvcji8tUdQDp+b8cPdciaeNw/eG/TiK4B2WSke/rbetbAINXnMABh8t69VaSdRmVRBMFdFuGb4SszuGCKuTx2ZLzaJ3wDGbLrV/xVasUrdjc/xOv9pgwnM4aRlGGcYH2UEobybBT0wTLmCdbHw6flM5HcC022ZXdPSFOE1IcI8QDPyP/lE6OiceMq+7IDLrz4Kdw+ihBu4zzlk08hoxPgcko/geSRG5IW79LsSFRW72hrbh75I0Nfz7VTuHLrONK1BGgwyfjHJ86FUwVan9Xs0cyZxVoUeQtqtk54jWwh9V9yLyxicO4zy0RVnvDKsRixKjPwL8ra0C2DmycR93VJA7Dw2JZ3/JqHVEgxew9tPSZpA1ogsCTlrP//ZTyNeg7gItU0dBTp8FQ1Cs4d2zHNbAgA9KOOymQ1XfiCV24nzSGhpzgBO1/yzBLAx8UhxDY/eAX7fLFcV2j8G12nEtgd7CWgqJt1MNLMWBKuBQhYEH+Vs+Nqrjq0Tsmx9hAs2Hg1bXsYmR4FGSt17jK+sBsQNDSo/GQ1/mycY8Qqm1yZWBnJLfPqYMSht/T1/He879mkgZo0EHiW1OwnWlB5H1F5Hgy9iYGN8qklJGt526tU2mwtaD2shMKpQ57cu2Am9JGuYLpKE/+wIEs3a8BlNqeeXrkjSZEuwsVlNvrfGqKYSXZbLLrfKlEsN0k1ZizHBlAGDm+oSMKOe8BvvGR+VbtwsT4/SOlDMPfU+dQv78KpOS6qfPL3boJuHcJUsCYUsaeL/IcFmuIf0n7cgQHxpgGJJ2WZJAEhq9FuYIFKBVLH7+14VICgWPB9Wrf+rKPWtUuCKBxaczq54Fd2tbJRaXPGzAP/uNxwOzqGL2+g2cN02qx+rNS2ATNwTSkRt4BM9R1yU6umFHwmaZRU52dXdZDZ2jGIjIb2jSwlMhAvSEcNeVa50WZzLsn+xnctO8gApmmq/gWI8/56Ps7qbkAnCGHiJG4TDY2aPDwhB39w8DJg7r7YrQsvZFSfTIK9rgXZSE3l8mR6ljRuxIcXlMZvEtyCKCRepQWBgxROxJLkRkXB6AkCBsaBYx5MBbV3msIvfz+AxhlzXmJtf9AboL1Lb2p4qEkU22G5lX3ZGLrj3wZjlVT4A/p9LbMlijRMH2oZ36sbw6ikjrjRjQTLEPiA33gBlelDUFXrY8NE/SqeIJGCaA35+UlTrj1dMF7BnPTjzGOesSKW9Vli5gP5QLj5o7QEAJBrHZXbCMEvPaFcc/IVLugbvWaZGPKBS7k87m/FVspafr6cid06Db07L/4Ce0tQ1RXXITz4gz6kOSGcdoU/UWU4msbVvE3OpFMtSvaazUCXPZdJuqhWkV61z/E6IS9viZfuFLJF1nPS0Sb81uy5w6Y/uKC/UEIHwK3VLWU0EtPP6ED/TV5ar0NGFCRHlucTAWZVfNczrenStn5o0p+nM06deY9A10tuvwkVO95aHruwH4JL+2mvwE6RkCnI/vCCeMLYSmKHAgvdXYbGWBB5XqQMgHOSivCNunsXON6cLv+7/avDmIAbjGS9/t2YllhZwKIFeVqC6QVEuWCNKdpV+XfZjQVbV7oIbKeJwY3bzPk3Kx0OtNVjvVA9C30MKiyvgQczWih+NBvqw8kZ2yS/Pm5pQR7cwuR5FOITaHmqjqScFEFEuahasA8dvLWgkNr4oPvCBMnFlQf9moBCt1zrFQabFVkmiEmpHAVwpRJm62AJjwS5OLXZeVDQjQA/xTDQNFM4G2uVGItgP94//52n8pPjPBtOKrChHQV3vQTrJM2zY8uiRGbrHDkvkuf9sHPPBe0Do6tbU5veek5uy7/Gw+FH1DgeTZK+UB0krdI5NWsqLqgb+3DFFEsHIAsMLU0xhQkXvMLxJPxqisz3if3xOZvFXKfmBzghwe9Z0pcDUET7GTFfmSG9kUMoKIpiSLENkT3uIu8p+TSOFIaLyfwSp242x2uRPt0+iWPzNJ5wJLAPdalXS90yQE3giuzTrbysw7K8NTaofD3MJXoOTWnQzoLfjVc2L3g4ACrT7V7pWo2jXZXu6tgph2RTQHBEyfDBYhlfRXjp5zKwMUHCc6iWQb2VXS6IEOzoQEZxifXAbFlpxu1Ym0NoIUWvEGiau9r4dtQUJxJeZ2jAOocUYA8rA4EtlinHtJafasuqorlLAdQ4nd4Zfg5ICG5VASprHZlQCaEwywggGQR4w9ppdOgenQssNYHXvVAbs5k7pQRZSuVAQ6+n+B2gd4LTgyLirLBxEm7BjP6tmtHfn0doXzG06HDyaCMEANDQMYF2I9ab0wO7IpKcs877uCYQkV3E/gSPWSFMBJRZy6k8dFnvQdmYnj0BS7EoYHt2YfWjhd2voUGZ5GH+i/9I8JCQ8ATB4mC11lFethspdTHgexfNT1bpL7E8mvHOCa1wF9M0y+jAq9muC+LmzvoXjTJQh+HjIf7X06WJK89z7g62p6C/u/YTP6Frxyi7d4M/w/TfVszK4vU1QmsE12G6eHght9MdX6MzXmF5lFgIzTLUH3ZxP9xYp3btYVwYWvtL4EcAJS/aOmSokmtTmclNPpjqHoeFwwyIzejC4LGEcczkfxEp6c5L4oVppj/GJrX6wlNPfYA3U0ijgjQpBw6zxioW1z24FeYvC+c2jlYg9OIhlRObqdoBfPVBgqLeFx+puURfIyKYnedlzbyB6wUUSZVeT1kjAaNiosasIivhC9JMGBxdELPggqE7TFoZ+vmvCntmMuOYcz5LiqVhELQa3dFxQDbRNjsZlyFpKRGgk0+FVaL+f8raICBfK6Do4q0L1jdgOewCNCz0YRH/N80OnsQkn6/r6ICYYqhd7mX6tPKHhXKHmBuTW7In/F7s2/GcQWHJdmteMLWeyk3gj4fw54TgpDRHFrBm2p3SL1BoWc6BEN75aOGgJwH8SPFdkFUyadcsLxBrPsPV/iVMzGMmdfJkQXToGbvGJXe3X15P2n3OGbSTwHORe1/VoHEYArTsWccbLw7sQovhqaG/nbMVJzBpnMLfFUlRSBOJDzM+c0sKigJ0vwbwrHG+jOJZk5txUMSliuPK05Bifl5G7mAaZGDG/79IIYL3+PTkIZAB7qVOBMQsewekEYvbZyAiXiNEBKFUYd2obU5dFpLXhWFH0su00sqS4Xq2ip6T//Un96T8YpreOKJv1aTZYmG40/8Hw/S3SXxUZUID1Ujr8a1+w2qR2ABzwC9la6ieuQe2pk5Q/zhFu8c2XX3nisQSt+4ltT8AlPm63T2/FovTVLlSv4x6DGIfuCT8PofzP3jNHIgoSgAG/CDVHPONPMbU30NmCNNEXjvk6PQv1mSHkEUgAa344Brvsvrozy0svrc6bp17s7EI8pXNK/lrFjopZtDvoxdbiZMFde6Xf6qHbQ5blxUB76dDzNMKZTDT32hJgixElNwhVqNeO8s9q8/vbvuyUKAmraYbMmeSld6n5gyvNWQhfI5AmuSBRdgoggM9a0ujIozVTamLJ1BKtokHs8ngmLOkHsnIX0S/1GOmplpe3M47E7BYCrDZINud5AZxAiAIZhUGIRk5wcTORuGDPV/8H7xYp84UAbBs0YCe6zhOUbRqgf/MDS1U9AgEsZ+3MJuutmx2PQDDkaiEK2FhqnyI9s07ciP2BuOtakW2KTwFaPiqnaNqIBHWBVMtaHy+EZ8hZsNO+/yS8nes73AZFg2BNmiCmUAtyzpIxm38uybop7Omr59ymBh1a0KvHLUfUQnrktTUbImi3+bWAmUhM1rH8052czvPIsJyb/EmeXyLYrH7DX7LugV14r0h3obNx6j0p/ad2YZ+sFq6REBITKQawZXLGqdhJm+YHE9SUbwzuqCpsg/Q1aNf9AWsUKKK2rBwTl84nlbPfDDsuwUHCOOoZsA8UFAivh689gyy03DucmaW19xUkE2JbaCgUNTG2ck1w2mKIWhAS/Jsqf+SJFu5P6GiMfZULW1+86HD7gjNHfBwq2q43oYOHBZWpGxPx1m4WI1gOpvNP6RQ1yxWjnQnLCQH6li/foRTAFWZcCKnePsBGBP4l+t0Y1jsH80jJGqrJTFBrcMNZXzkrGNAy+lTayyX5OhJnbLJG/eNMzw3/RCsQ3u1uZC6O9AtGdsrvGnqRjRJLVNs/6V4JsCbDYlTJw5pn59c6VWvv+u+c13DjIafzB5Fmcxgvs2JJaECT7ayU8qZa0HFkt9hWLukpNFQkpwXd2nGcWbJhgwlFmhW3TPfC2F21APqroU0q8rPPKtclvIaM5d9CKmDH9oBCi0jCqB44/EFfDL5xMyoWGEaNQc7ZB9YLyF++arzTHlA7M4MNMey4ECh92SRk2UtpTKa324pqBilcPa46aMrrb75vhed4K6K8A/6DMhndG1+erStQYnitKVefBR+E5yvTfqEJZTEel2lELj9m21auKMKg=
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: mMPFf9bnrvyz6mbx
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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