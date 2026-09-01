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
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
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
  - decisions:
    - #0:
      - toolName: set-research
      - args:
        - Rationale: Telecommunications is currently being researched and will complete in 6 turns. Lasers remains the absolute highest priority next technology to research. It unlocks critical late-game technologies (Globalization and Particle Physics) which are required for constructing spaceship parts. Additionally, it unlocks Nuclear Missiles, which provides an essential strategic deterrent against Byzantium (who just nuked our ally Spain's capital Madrid) and Mongolia.
        - Technology: Lasers
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: We will accumulate enough culture to adopt our next policy in 6 turns. We confirm Spaceflight Pioneers (Order Tier 3 tenet) as our selection. This tenet grants a free Great Scientist and Great Engineer, and enables us to finish spaceship parts with Great Engineers (with 50% more effectiveness). This is the cornerstone of our science victory sprint to rush expensive spaceship components once the Apollo Program completes.
        - Policy: Spaceflight Pioneers
    - #2:
      - toolName: keep-status-quo
      - rationale: Maintain our current grand strategy (Spaceship) and tactical flavors. The Apollo Program finishes next turn in New York, allowing us to immediately start building SS Boosters in our high-production cities. Furthermore, Philadelphia completes its Airport next turn, which successfully finishes the Colombo quest—granting us 346 influence and 634 production in Washington to complete its Strategic Defense System. Boston is training an Atomic Bomb as a deterrent. Our high defense, science, spaceship, and production flavors are perfectly configured for this transition phase. Status quo is maintained.
  - tokens:
    - inputTokens: 65927
    - reasoningTokens: 8720
    - outputTokens: 317
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Diplomatic Threat**
            
            I'm currently analyzing Byzantium's dominant diplomatic position. They've secured 90% of the delegates, posing a significant threat to my victory prospects. I need to devise strategies to counter their influence before it's too late.
            
            **Analyzing Diplomatic Leverage**
            
            I'm re-evaluating the delegate count. Byzantium is indeed strong with 40 delegates, but they still need four more to win. I'm examining alliances with city-states to see if I can shift even a small portion of that support.
            
            **Responding to Nuclear Escalation**
            
            Byzantium's nuclear strike on Madrid is a game-changer. I'm assessing the fallout's impact and recalibrating my diplomatic and military strategies, considering the sudden shift in power dynamics.
            
            **Evaluating Military Parity**
            
            I'm reassessing the military landscape; Byzantium's 42,117 strength is alarming, dwarfing others. Austria is their closest competitor. My immediate focus is countering their dominance and that of Austria.
            
            **Contesting Diplomatic and Cultural Victories**
            
            Byzantium's dual pursuit of Diplomatic and Cultural victory is my primary concern. They're nearing delegate majority and are poised to achieve Cultural victory by influencing Austria within five turns. I'm exploring rapid countermeasures.
            
            **Accelerating Spaceship Construction**
            
            I'm prioritizing science, specifically aiming to complete the Apollo Program next turn. Once done, I'll shift focus to spaceship parts, leveraging the Spaceflight Pioneers policy for Great Engineers to accelerate construction.
            
            **Leveraging War Alliances**
            
            I'm assessing the advantage of current wars. Spain and Austria are both fighting Byzantium, and Spain was just nuked. Since I'm not in a war with Byzantium directly, I'm exploring how to use their current conflicts to my benefit without joining the fray myself.
            
            **Analyzing Global Conflicts**
            
            I'm re-evaluating the current wars. Austria is indeed engaged on multiple fronts, but Spain and Germany are also at odds, and Spain was just nuked. My own war with the Shoshone is isolated; my high relationships with Spain and Austria offer leverage, while negative standings with Mongolia, Germany, and Byzantium are to be maintained. My immediate research priority is Lasers to unlock key technologies and nuclear capabilities.
            
            **Prioritizing Technology and Policies**
            
            I'm confirming my research focus on Lasers and noting Spaceflight Pioneers as my next policy choice. My current negative relationships with certain city-states and major powers offer strategic leverage, while my friendship with Colombo, despite its religion, is also being considered in my calculations.
            
            **Detecting Diplomatic Openings**
            
            I've discovered several city-states have "Open Door" resolutions, blocking alliances. This, along with the proposed repeal of the Passport System, significantly hinders Byzantium's cultural and diplomatic victory paths, offering a crucial opportunity to counter their progress.
            
            **Countering Diplomatic Maneuvers**
            
            I'm keenly observing proposed resolutions, particularly Germany's "Repeal Passport System" and the "Sanction: Austria" proposal. My limited delegate votes make direct intervention difficult, but I'm exploring ways to influence AI voting through diplomatic postures. The proximity of Madrid's nuclear devastation to my own cities is also a significant, immediate concern.
            
            **Defending Against Nuclear Fallout**
            
            The recent nuclear strike on Madrid has placed fallout dangerously close to our cities, including Boston. Fortunately, our major cities already possess the Strategic Defense System, and Washington's is nearly complete, providing crucial protection.
            
            **Completing Strategic Defenses**
            
            Our Strategic Defense Systems are nearly complete across our cities, with two turns remaining on the final build. This will provide crucial protection against nuclear fallout, a welcome development given the proximity of recent attacks. Our military strength within our friendly territory continues to far outweigh any immediate threats, though our posture in the Shoshone capital remains defensive.
            
            **Defending Coastal Cities**
            
            I'm focused on the immediate Shoshone naval threat to Boston, New York, and Chicago. Our naval strength in Chicago is adequate, but the Shoshone's presence in their sea zone necessitates reinforcing our coastal defenses against their destroyers and riders, despite our overall high defense flavors.
            
            **Prioritizing Spaceship Production**
            
            With the Apollo Program nearing completion and fallout concerns, my focus has shifted. I'm prioritizing spaceship part construction, leveraging high production and science. Nuclear deterrence remains a key consideration, especially with an atomic bomb in production for Boston.
            
            **Completing Critical Quests**
            
            I've discovered a city quest for Colombo that I'm about to complete next turn. This will grant a significant influence boost, solidifying our friendship with them, and a substantial production increase in Washington, likely completing our Strategic Defense System build.
            
            **Clarifying Spaceship Tech**
            
            I've realized my understanding of spaceship part unlocks was slightly off; Rocketry, an earlier tech, actually unlocks the SS Booster. This means I can begin constructing them immediately after the Apollo Program is completed, rather than waiting for specific Information Era technologies. I can build up to three boosters.
            
            **Accelerating Spaceship Assembly**
            
            My understanding of spaceship part unlocks has been refined; Rocketry grants the SS Booster, allowing immediate construction alongside Apollo's completion. The Spaceflight Pioneers policy, arriving in six turns, aligns perfectly to rush parts with a free Great Engineer, making our immense production capacity truly decisive.
            
            **Assessing Cultural Victory Race**
            
            Byzantium is nearing a cultural victory, requiring only Austria's influence, which they'll achieve in five turns. I'm urgently exploring any available counter-strategies to prevent this imminent win, as they currently hold five of the six necessary influences and appear to be building the Citizen Earth Protocol wonder.
            
            **Investigating Victory Condition**
            
            I'm re-examining Byzantium's victory path, specifically their Cultural Victory. My data suggests they haven't built the Citizen Earth Protocol wonder, and it might not even be unlocked yet. This could be a critical detail in derailing their progress.
            
            **Blocking Diplomatic and Cultural Victories**
            
            I've discovered Byzantium's cultural victory hinges on completing the Citizen Earth Protocol, which they haven't built and may not have unlocked. I'm now investigating ways to halt their tourism and boost Austria's culture, especially since Germany's "Repeal Passport System" proposal, if passed, would halve Byzantium's tourism.
            
            **Analyzing Delegate Votes**
            
            I'm reassessing the delegate count for the "Repeal Passport System" resolution. While Byzantium has 40 votes, the combined support of Austria, Spain, Germany, Mongolia, Shoshone, and America totals 53, enough to pass it. I'm now scrutinizing their Diplomatic Victory path; they currently hold 40 delegates and require only four more to win the upcoming World Leader election, which is imminent.
            
            **Blocking Diplomatic Gains**
            
            I've identified that "Open Door" resolutions prevent Byzantium from allying with several key city-states, locking them at 40 delegates. This means they can't easily acquire the four additional delegates needed to secure a Diplomatic Victory, a critical setback for them.
            
            **Defending Against Diplomatic Maneuvers**
            
            I'm tracking multiple resolutions now, particularly Byzantium's attempt to repeal the German Sphere of Influence for Assur. If they succeed, they'll gain more delegates. I'm also monitoring my defensive posture against the Shoshone in Philadelphia, where my forces hold a significant advantage despite their lingering presence.
            
            **Reinforcing Defensive Positions**
            
            I'm solidifying our defensive lines around Philadelphia and Boston against the Shoshone advance, utilizing our superior artillery and upcoming airport completion to secure the Colombo quest. Our primary focus remains the spaceship race, with Lasers as the current research priority to ensure a science victory.
            
            **Updating Diplomatic Alliances**
            
            I'm revising my understanding of city-state relationships. Manila and Sydney, allied with Byzantium and involved in ongoing conflicts, remain hostile assets. Huari and Shedet have been reset to neutral. My current diplomatic stance with major powers remains unchanged, reflecting ongoing threats and vital alliances.
            
            **Updating Diplomatic Strategy**
            
            I'm adjusting my diplomatic approach now that France and Brazil are defeated. Huari and Shedet will remain neutral to avoid antagonizing Byzantium, while other allied city-states within the enemy bloc will be kept hostile. Colombo's friendship is secured through an imminent quest completion.
            
            **Confirming Strategic Research**
            
            My current research focus on Lasers is confirmed. I'm also ensuring my tactical AI is perfectly aligned for spaceship construction with maximum flavors in Spaceship, Production, Science, and Defense. Nuclear capabilities are also prioritized with an atomic bomb in production.
            
            **Confirming Strategy Execution**
            
            My current research on Lasers is confirmed as the path forward. I'm also setting "Spaceflight Pioneers" to be adopted in six turns, aligning with the impending completion of the Apollo Program. My tactical AI flavors remain set for production, science, and defense, ensuring a cohesive strategy.
            
            **Researching Key Technologies**
            
            I'm confirming my research focus on Lasers, which is critical for spaceship parts and nuclear deterrence. I'll adopt Spaceflight Pioneers next to leverage Great Engineers for spaceship assembly. My tactical AI flavors will remain focused on production, science, and defense.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: GskNU0IantcPKv66
          - toolName: set-research
          - input:
            - Rationale: Telecommunications is currently being researched and will complete in 6 turns. Lasers remains the absolute highest priority next technology to research. It unlocks critical late-game technologies (Globalization and Particle Physics) which are required for constructing spaceship parts. Additionally, it unlocks Nuclear Missiles, which provides an essential strategic deterrent against Byzantium (who just nuked our ally Spain's capital Madrid) and Mongolia.
            - Technology: Lasers
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: JiYo4BnDt2z3BQkb
          - toolName: set-policy
          - input:
            - Rationale: We will accumulate enough culture to adopt our next policy in 6 turns. We confirm Spaceflight Pioneers (Order Tier 3 tenet) as our selection. This tenet grants a free Great Scientist and Great Engineer, and enables us to finish spaceship parts with Great Engineers (with 50% more effectiveness). This is the cornerstone of our science victory sprint to rush expensive spaceship components once the Apollo Program completes.
            - Policy: Spaceflight Pioneers
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: KjCDLeA5DCSymISs
          - toolName: keep-status-quo
          - input:
            - Rationale: Maintain our current grand strategy (Spaceship) and tactical flavors. The Apollo Program finishes next turn in New York, allowing us to immediately start building SS Boosters in our high-production cities. Furthermore, Philadelphia completes its Airport next turn, which successfully finishes the Colombo quest—granting us 346 influence and 634 production in Washington to complete its Strategic Defense System. Boston is training an Atomic Bomb as a deterrent. Our high defense, science, spaceship, and production flavors are perfectly configured for this transition phase. Status quo is maintained.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: GskNU0IantcPKv66
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
          - toolCallId: JiYo4BnDt2z3BQkb
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: KjCDLeA5DCSymISs
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.