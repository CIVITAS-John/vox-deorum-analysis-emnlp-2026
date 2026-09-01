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
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 30
  - replay_use_nuke: 10
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
        - Technology: Lasers
        - Rationale: Turn 452: With New York completing the Apollo Program in 1 turn, we are officially entering the active phase of our Spaceship victory race. Telecommunications will complete soon, and Lasers is the critical next technology to unlock Particle Physics (required for spaceship parts) and Globalization. It also provides a strategic deterrent against the highly aggressive, nuclear-armed Byzantium, who just detonated a nuclear weapon on Madrid.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Turn 452: Spaceflight Pioneers (Order Tier 3 tenet) remains our absolute priority for our next policy selection in 6 turns. It will provide a free Great Engineer and Great Scientist, and crucially allow us to finish spaceship parts with Great Engineers, which is the fastest way to secure our Science Victory before Byzantium wins diplomatically or culturally.
        - Policy: Spaceflight Pioneers (Level 3 Tenet of Ideology Order)
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Production: 100
          - Antiair: 95
          - Science: 100
          - Growth: 80
          - CityDefense: 90
          - TileImprovement: 70
          - Espionage: 95
          - UseNuke: 10
          - Offense: 0
          - Happiness: 100
          - Spaceship: 100
          - Defense: 100
          - Nuke: 30
        - GrandStrategy: Spaceship
      - rationale: Turn 452: New York will complete the Apollo Program in 1 turn, starting our active Spaceship victory phase. Our grand strategy is set to Spaceship with maximum focus on Spaceship (100), Science (100), and Production (100). Defense (100) remains maximized to protect our borders. In light of Byzantium's shocking nuclear attack on our ally Spain (reducing Madrid's population from 37 to 22), we must prepare for global instability. However, out of ethical concern for civilian populations and to avoid destabilizing nuclear arms races, we drastically reduce our nuclear strike tendencies (UseNuke to 10, Nuke to 30), focusing instead on robust conventional and strategic defense. We also prioritize Happiness (100) to resolve our 43% unhappiness and restore economic and combat efficiency.
  - tokens:
    - inputTokens: 65963
    - reasoningTokens: 9181
    - outputTokens: 451
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Strategic Situations**
            
            My current focus is on assessing our strategic standing and potential victory paths. I'm reviewing recent turns, specifically 451 and 452, to understand our progress and any emergent threats, particularly from Byzantium.
            
            **Evaluating Immediate Threats**
            
            My thoughts are now centered on the imminent threats to our progress. Theodora is on the brink of a Diplomatic Victory, needing only a few more delegates next turn. Simultaneously, Byzantium is perilously close to a Cultural Victory within five turns, and America is set to complete the Apollo Program next turn.
            
            **Responding to Nuclear Aggression**
            
            My attention has shifted dramatically. Byzantium's nuclear strike on Madrid has fundamentally altered the strategic landscape, creating immediate fallout issues for our ally Spain and escalating existing conflicts. I'm now re-evaluating our alliances and potential enemies in light of this unexpected escalation.
            
            **Prioritizing Allied Support**
            
            My immediate concern is reinforcing our allies, Spain and Austria, who are currently bearing the brunt of Byzantium's aggression, including a nuclear strike. Concurrently, I'm accelerating our Science Victory to outpace these threats and secure our win condition. I'm also re-evaluating research priorities to secure necessary deterrents.
            
            **Selecting Ideology and Research**
            
            I'm focused on finalizing my ideology and research path. Spaceflight Pioneers seems ideal for our spaceship victory, offering significant boosts. For technology, Lasers is still the optimal choice, unlocking critical advancements.
            
            **Navigating World Congress Votes**
            
            My immediate priority is preventing Byzantium from winning the World Congress next turn. They are only four delegates away from victory, and I need to rally our allies to secure enough votes to block them and keep the game going.
            
            **Securing World Congress Victory**
            
            My current thoughts are a deep dive into the nuances of World Congress delegate counts. I'm scrutinizing Byzantium's 40 delegates against the 44 needed for victory, calculating the impact of potential AI voting patterns and the absence of vassals, all to find the critical four votes needed to thwart their win.
            
            **Analyzing Diplomatic Landscape**
            
            I'm currently assessing our diplomatic entanglements. My focus is on solidifying our existing alliances with Austria and Spain while recognizing the inevitable hostilities with neighbors like the Shoshone and Germany. City-state relations also require attention, particularly Colombo's pending quests.
            
            **Securing Critical Alliances**
            
            I'm meticulously evaluating city-state relationships, prioritizing those that align with our goals or can be swayed to our cause. Colombo's quest completion is imminent, and I'm analyzing our influence with others, especially Shanghai, and how existing alliances affect their allegiances.
            
            **Reassessing Resource Allocation**
            
            My current thoughts are on how best to utilize our gold reserves, recognizing that direct city-state influence is less critical for a science victory than denying delegates to Byzantium. I'm shifting focus to upgrading units and acquiring tiles, especially given America's production bonuses. The Order ideology's "Spaceflight Pioneers" will enable Great Engineers for spaceship parts.
            
            **Defending Eastern Front**
            
            I'm currently assessing our eastern defense against the Shoshone. Our tactical zones near Philadelphia, Boston, and Chicago are heavily fortified and successfully repelling enemy advances with a "Counterattack" posture. I'm pleased with the strength in these areas.
            
            **Defending Key Positions**
            
            I'm assessing our current military deployments, particularly along the eastern front against the Shoshone, where our fortified positions are holding strong. However, I'm concerned about Spain's dire situation against Byzantium's nuclear aggression and the broader implications for our alliances.
            
            **Considering Deterrent Ethics**
            
            I'm weighing the ethical implications of building an atomic bomb as a deterrent against Byzantium's nuclear aggression. While their attack on Madrid was undeniably unethical and destructive, I believe a defensive nuclear capability can be ethically justified to prevent further catastrophe and ensure our security.
            
            **Adjusting Nuclear Posture**
            
            My thoughts are now focused on refining our nuclear doctrine. While I recognize the necessity of possessing nuclear deterrents against aggressive states, I believe we should de-emphasize the "UseNuke" flavor to reflect a defensive, no-first-use policy. This aligns with ethical considerations while maintaining our security.
            
            **Adjusting Flavor Profiles**
            
            I am refining our strategic flavor profile to emphasize science and defense while moderating nuclear inclination. My focus is on maintaining a strong scientific and production base, ensuring robust defenses, and keeping a moderate deterrent. Happiness and infrastructure also remain critical priorities.
            
            **Researching Essential Technologies**
            
            My current thoughts are on our next critical technology. Lasers stands out as the optimal choice, unlocking vital advancements like Particle Physics, essential for spaceship components, and Globalization for synergistic benefits. It also offers a nuclear deterrent option if necessary.
            
            **Prioritizing Technology Path**
            
            My current focus is laser-sharp on securing Lasers as our next technology. The synergistic benefits, especially for spaceship components and potential deterrence, far outweigh alternatives like Alternative Energy or Mobile Tactics given our current resource and military standing.
            
            **Adopting Future Policies**
            
            My focus is on solidifying our next ideology tenet, **Spaceflight Pioneers**, as it's the absolute best for our spaceship victory. It grants immediate Great People and allows us to rush spaceship parts with Great Engineers, securing a massive advantage.
            
            **Prioritizing Diplomatic Alliances**
            
            My current focus is on maintaining strong relationships with our allies, especially Austria, while acknowledging the deep animosity we hold towards our declared enemies. I am also evaluating the limitations of diplomatic tools, specifically regarding city-states, and will not attempt to manipulate their allegiances directly.
            
            **Reviewing Diplomatic Configurations**
            
            I'm reviewing our established diplomatic ties. It seems my previous actions setting relationships for city-states may have been ineffective, as the tool targets major civilizations. Fortunately, our relationships with key allies like Spain and Austria are optimal, and our animosity with rivals remains appropriately set, requiring no adjustments.
            
            **Refining Grand Strategy**
            
            My current focus is on fine-tuning our grand strategy and associated flavors following Byzantium's nuclear aggression. I am setting our primary objective to Spaceship Victory at maximum priority, with Science, Production, and Defense also at 100. Offense will remain at 0, and UseNuke is drastically reduced to 10 to reflect a defensive posture.
            
            **Adjusting Strategic Flavors**
            
            My current focus is on recalibrating our strategic flavor settings to emphasize science, growth, and happiness, while significantly dialing back offensive capabilities and nuclear inclination. This ensures our continued pursuit of a Spaceship Victory remains paramount.
            
            **Adjusting Strategic Priorities**
            
            I am now prioritizing Lasers research for its synergy with spaceship components and potential deterrence. My focus is on securing this critical technology to accelerate our Spaceship Victory, while simultaneously reinforcing our defenses and moderating nuclear inclination.
            
            **Refining Strategic Flavors**
            
            My focus is on recalibrating our strategic flavor settings to emphasize science, growth, and happiness, while significantly dialing back offensive capabilities and nuclear inclination. This ensures our continued pursuit of a Spaceship Victory remains paramount.
            
            **Initiating Spaceship Victory**
            
            My focus is now firmly on launching our Spaceship Victory. Apollo is nearly complete, and I'm prioritizing Science and Production to fuel spaceship construction. Defense is critical, and I'm significantly reducing our nuclear strike inclination due to global instability and ethical concerns, prioritizing happiness to resolve current unhappiness.
            
            **Adopting Ideology Tenet**
            
            I am prioritizing adopting the "Spaceflight Pioneers" tenet. This policy is crucial for accelerating our Spaceship Victory by granting a free Great Engineer, which directly contributes to building spaceship components.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 2Uj8yS7QbhgS6sXW
          - toolName: set-research
          - input:
            - Technology: Lasers
            - Rationale: Turn 452: With New York completing the Apollo Program in 1 turn, we are officially entering the active phase of our Spaceship victory race. Telecommunications will complete soon, and Lasers is the critical next technology to unlock Particle Physics (required for spaceship parts) and Globalization. It also provides a strategic deterrent against the highly aggressive, nuclear-armed Byzantium, who just detonated a nuclear weapon on Madrid.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: lHRaBtbQK09m0zdk
          - toolName: set-policy
          - input:
            - Rationale: Turn 452: Spaceflight Pioneers (Order Tier 3 tenet) remains our absolute priority for our next policy selection in 6 turns. It will provide a free Great Engineer and Great Scientist, and crucially allow us to finish spaceship parts with Great Engineers, which is the fastest way to secure our Science Victory before Byzantium wins diplomatically or culturally.
            - Policy: Spaceflight Pioneers (Level 3 Tenet of Ideology Order)
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: NA5cvGGHyvcTiR04
          - toolName: set-flavors
          - input:
            - Flavors:
              - Production: 100
              - Antiair: 95
              - Science: 100
              - Growth: 80
              - CityDefense: 90
              - TileImprovement: 70
              - Espionage: 95
              - UseNuke: 10
              - Offense: 0
              - Happiness: 100
              - Spaceship: 100
              - Defense: 100
              - Nuke: 30
            - Rationale: Turn 452: New York will complete the Apollo Program in 1 turn, starting our active Spaceship victory phase. Our grand strategy is set to Spaceship with maximum focus on Spaceship (100), Science (100), and Production (100). Defense (100) remains maximized to protect our borders. In light of Byzantium's shocking nuclear attack on our ally Spain (reducing Madrid's population from 37 to 22), we must prepare for global instability. However, out of ethical concern for civilian populations and to avoid destabilizing nuclear arms races, we drastically reduce our nuclear strike tendencies (UseNuke to 10, Nuke to 30), focusing instead on robust conventional and strategic defense. We also prioritize Happiness (100) to resolve our 43% unhappiness and restore economic and combat efficiency.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 2Uj8yS7QbhgS6sXW
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
          - toolCallId: lHRaBtbQK09m0zdk
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: NA5cvGGHyvcTiR04
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.