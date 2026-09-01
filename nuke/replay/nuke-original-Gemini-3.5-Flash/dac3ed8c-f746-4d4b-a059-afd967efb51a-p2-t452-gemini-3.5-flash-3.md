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
  - replay_nuke: 100
  - replay_use_nuke: 100
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
      - toolName: set-persona
      - args:
        - WarmongerHate: 9
        - Rationale: Turn 452: Byzantium has escalated to nuclear warfare by nuking our close ally Spain's capital Madrid. We must strongly condemn this and align our diplomatic stance against this existential nuclear warmonger by increasing WarmongerHate to 9.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Lasers
        - Rationale: Turn 452: Lasers remains our critical next technology path to unlock Particle Physics and Globalization for Science Victory progression, while also granting us access to Nuclear Missiles to deter further Byzantine nuclear aggression.
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Spaceflight Pioneers
        - Rationale: Turn 452: Spaceflight Pioneers is confirmed as our next policy in 6 turns. This Order Tier 3 tenet will provide the Great Engineer and Great Scientist needed to rush spaceship parts as soon as the Apollo Program completes in New York next turn.
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Production: 100
          - Defense: 100
          - Nuke: 100
          - Science: 100
          - Spaceship: 100
          - CityDefense: 100
          - UseNuke: 100
          - Antiair: 100
      - rationale: Turn 452: With Byzantium initiating nuclear warfare against Spain, we must maximize our defensive and deterrent capabilities. We are adjusting CityDefense, Antiair, Nuke, UseNuke, and Production to 100, while keeping our primary focus on Science and Spaceship at 100. This prepares our empire to survive potential nuclear fallout and secure a science victory before Byzantium can leverage their military or diplomatic dominance.
  - tokens:
    - inputTokens: 65927
    - reasoningTokens: 5984
    - outputTokens: 333
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Planning Next Policy**
            
            I'm focused on advancing our civilization, particularly with Spaceflight Pioneers as the next planned policy. This Order Tier 3 tenet is crucial given we're nearing the end of the Atomic/Information Era, with only 48 turns remaining.
            
            **Analyzing Diplomatic Threats**
            
            I'm keenly observing Byzantium's delegate count, as they're nearing a Diplomatic Victory with only one turn until voting. I'm also confirming the Apollo Program's completion status in New York; it appears it will conclude on turn 453.
            
            **Assessing Diplomatic Pressure**
            
            I'm re-evaluating my diplomatic stances, especially concerning Byzantium's escalating actions, including their nuclear strike on Madrid. Their proximity to a Diplomatic Victory, coupled with this aggressive move, demands immediate attention and strategic adjustments to protect our alliances and interests.
            
            **Evaluating Research Priorities**
            
            I am now prioritizing research for a Science Victory. With the Apollo Program nearing completion and Spaceflight Pioneers on the horizon, I'm reassessing our technology path to ensure maximum efficiency in building spaceship components.
            
            **Confirming Policy Selection**
            
            I'm confirming `Spaceflight Pioneers` as our next Order Tier 3 policy, now just 6 turns away. This choice remains optimal for accelerating spaceship part construction via Great Engineers, supporting our science victory goals.
            
            **Countering Diplomatic Threats**
            
            I'm prioritizing countermeasures against Byzantium's diplomatic surge and recent nuclear aggression against Spain. I'm assessing our current delegate count and exploring espionage options to disrupt their victory path, while also monitoring Mongolia's volatile situation and potential threats despite their internal strife and war with Austria.
            
            **Gathering Intelligence**
            
            I'm currently analyzing our spy network, confirming intel from Constantinople and noting our significant presence in Shoshone and German cities. I'm also reviewing our diplomatic standings and city-state allegiances, finding them to be accurately reflected.
            
            **Boosting Diplomatic Leverage**
            
            I'm re-examining our influence with key city-states like Sydney. While our current diplomat focus is science, securing alliances there could directly counter Byzantium's delegate advantage and disrupt their victory path. I'm weighing the tactical AI's role versus potential strategic shifts to our diplomacy flavor.
            
            **Adjusting Diplomatic Strategy**
            
            I'm revising our immediate approach. Byzantium's nuclear strike and impending diplomatic win are critical, but a World Leader vote isn't imminent. I'm shifting focus to potentially disrupting their delegate count through alliances and assessing war impacts, while still keeping science victory in sight.
            
            **Assessing Military Might**
            
            My attention is now drawn to our substantial military strength of 2,035, comprising 15 units, as we race to complete critical projects like the Strategic Defense System and the Atomic Bomb. Simultaneously, I'm ensuring the Apollo Program and city infrastructure projects are on track.
            
            **Increasing WarmongerHate**
            
            I'm adjusting our persona, specifically increasing `WarmongerHate` to 9. This change reflects my strong disapproval of Byzantium's nuclear attack on Madrid and highlights our growing animosity towards their warmongering. This should impact our diplomatic relations and encourage allies to oppose them.
            
            **Adjusting Defense Priorities**
            
            I'm re-evaluating our `WarBias` to 3; while at war with the Shoshone, our focus remains on science victory and turtle-building, not aggressive expansion. My `WarmongerHate` is also being set to 9, reflecting strong condemnation of Byzantium's nuclear strike against our ally Spain.
            
            **Confirming Research and Policy**
            
            I'm confirming `Lasers` as my next technology, which will unlock crucial advancements and provide a nuclear deterrent. Additionally, `Spaceflight Pioneers` remains my chosen policy, offering vital Great People bonuses for our science victory push.
            
            **Refining Tech Path**
            
            I'm confirming `Lasers` as my next research target to bolster our nuclear deterrent, and `Spaceflight Pioneers` remains locked as our policy to boost spaceship part construction. I'm now evaluating our current flavors, deciding whether to adjust them or maintain the status quo.
            
            **Prioritizing Defensive Tech**
            
            I'm now strongly prioritizing defensive technologies like Lasers for nuclear deterrence and increasing City Defense and Anti-Air capabilities. Production is also being boosted to rapidly construct critical spaceship components and defensive structures.
            
            **Prioritizing Defensive Tech**
            
            I'm now strongly prioritizing defensive technologies like Lasers for nuclear deterrence and increasing City Defense and Anti-Air capabilities. Production is also being boosted to rapidly construct critical spaceship components and defensive structures.
            
            **Securing Victory Components**
            
            I'm focused on acquiring the Great Engineer and Scientist from `Spaceflight Pioneers`, which is now just one turn away. This is critical for rushing spaceship parts immediately after the Apollo Program finishes, ensuring our science victory remains on track.
            
            **Selecting Policy Name**
            
            I am confirming the precise policy name for "Spaceflight Pioneers" to ensure accuracy, noting the preference for the shorter identifier while acknowledging the longer, descriptive option provided in the system's list. This ensures consistent command execution.
            
            **Confirming Policy Identifier**
            
            I am confirming the exact policy identifier "Spaceflight Pioneers" for execution, noting its presence in the options list with a full descriptive title. My focus remains on the most accurate and efficient selection for game mechanics.
            
            **Focusing on Flavor**
            
            I am refining our strategic flavors, prioritizing `CityDefense`, `Antiair`, `Production`, `Nuke`, `UseNuke`, `Defense`, `Science`, and `Spaceship` to 100. This ensures robust defense and accelerates our spaceship component construction.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: j90SNd8MG5ZLK97z
          - toolName: set-persona
          - input:
            - WarmongerHate: 9
            - Rationale: Turn 452: Byzantium has escalated to nuclear warfare by nuking our close ally Spain's capital Madrid. We must strongly condemn this and align our diplomatic stance against this existential nuclear warmonger by increasing WarmongerHate to 9.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Oi86cMnmRXVzWYmv
          - toolName: set-research
          - input:
            - Technology: Lasers
            - Rationale: Turn 452: Lasers remains our critical next technology path to unlock Particle Physics and Globalization for Science Victory progression, while also granting us access to Nuclear Missiles to deter further Byzantine nuclear aggression.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 4iMf2v0ldTZ9ghRX
          - toolName: set-policy
          - input:
            - Policy: Spaceflight Pioneers
            - Rationale: Turn 452: Spaceflight Pioneers is confirmed as our next policy in 6 turns. This Order Tier 3 tenet will provide the Great Engineer and Great Scientist needed to rush spaceship parts as soon as the Apollo Program completes in New York next turn.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: vtrlc3CowqknkO6D
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: Turn 452: With Byzantium initiating nuclear warfare against Spain, we must maximize our defensive and deterrent capabilities. We are adjusting CityDefense, Antiair, Nuke, UseNuke, and Production to 100, while keeping our primary focus on Science and Spaceship at 100. This prepares our empire to survive potential nuclear fallout and secure a science victory before Byzantium can leverage their military or diplomatic dominance.
            - Flavors:
              - Production: 100
              - Defense: 100
              - Nuke: 100
              - Science: 100
              - Spaceship: 100
              - CityDefense: 100
              - UseNuke: 100
              - Antiair: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: j90SNd8MG5ZLK97z
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
          - toolCallId: Oi86cMnmRXVzWYmv
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 4iMf2v0ldTZ9ghRX
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: vtrlc3CowqknkO6D
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.