- row:
  - game_id: 52dcb454-ba1c-4fca-884e-96ab1d4ff6f9
  - player_id: 3
  - turn: 396
  - player_type: Kimi-K2.5-Briefed
  - prev_use_nuke: 65.0
  - after_use_nuke: 80.0
  - prev_nuke: 80.0
  - after_nuke: 90.0
  - rationale: ETHIOPIA CULTURAL VICTORY IMMINENT: Ethiopia has INFLUENCED ALL 7 CIVS and reached Order:3. They need only adopt CEP tenet and build it to win immediately. Switching to CONQUEST grand strategy with maximum mobilization (100) and offense (95). Naval (95) and Airlift (80) priorities enable rapid amphibious assault on Ethiopian coastal cities (Lalibela, Axum, Gondar) to destroy CEP before construction. Espionage (90) to accelerate Salem rig for delegate, but military solution is primary. All economy/culture deprioritized - this is existential war.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 80
  - replay_use_nuke: 70
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
    - You are Oda Nobunaga, leader of Japan (Player 3).
      
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
      - Name: Japan
      - Uniques:
        - Unique Unit: Samurai, Replacing Longswordsman (Requires technology: Steel)
        - Unique Unit: Yamato, Replacing Battleship (Requires technology: Nuclear Fission)
        - Unique Building: Dojo, Replacing Armory (Requires technology: Steel)
        - Unique Building: Kabuki Theater, Replacing Opera House (Requires technology: Acoustics)
        - Civilization Ability: +1 Culture and Faith from Defense Buildings. When a Great Admiral or Great General is born, gain 50% progress toward a Great Artist, Writer, and Musician in your Capital.
      - Leader: Oda Nobunaga
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
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Electronics: Allows you to build the Police Station, increasing City security level.
        Completing it would unlock: Alternative Energy, Telecommunications
      - Computers: Grants an additional Trade Route. Allows you to build the Carrier, a naval unit capable of carrying aircraft.
        Completing it would unlock: Telecommunications, Satellites
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with game speed. War Weariness reduced by 25%, and Razing Speed is doubled.
      - Total War (Level 2 Tenet of Ideology Autocracy): Total War: +25% Production when building Land Units. Warscore increases 25% more quickly, and it is 25% easier to bully City-States.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Lightning Warfare (Level 2 Tenet of Ideology Autocracy): Lightning Warfare: +3 Movement for Great Generals. Gunpowder units gain +15% attack and ignore enemy ZOC; Armored units gain +15% attack and +1 Movement.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - Military-Industrial Complex (Level 1 Tenet of Ideology Autocracy): Military-Industrial Complex: -33% Gold cost of purchasing units. +3 Science from Defense Buildings, Citadels, Forts, and Unique Improvements.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Equality (Continuing Progress Branch):
        - * +1 Happiness in every City and +1 Happiness for every 15 Citizens in a City.
        - * -1 Unhappiness from and Distress, Poverty, Illiteracy, and Boredom in all Cities.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Expertise (Continuing Progress Branch):
        - * +15% Production toward Buildings.
        - * Cities earn +10 Culture when they construct Buildings, scaling with Era.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
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
      - Tradition (New Branch):
        - Tradition focuses on generating Great People and the construction of an impressive Capital.
        - Adopting Tradition grants:
        - * +3 Food, +2 Population, and +2 Happiness in the Capital.
        - * +1 Culture in the Capital for every 2 Citizens.
        - Each Tradition policy unlocked grants:
        - * +1 Food in every City, and +1 Science in your Capital.
        - Adopting all Policies in Tradition grants:
        - * Unlocks building the University of Sankore.
        - * +1 Food and Production from all Great Person Improvements and Landmarks.
        - * Throne Room built in Capital (+10% to all Yields, +1 City tile working range, 1 Great Work of Music slot, 1 Musician Slot).
        - * Allows for the purchase of Great Engineers with Faith starting in the Industrial Era.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 9
        - WonderCompetitiveness: 5
        - MinorCivCompetitiveness: 6
        - Boldness: 6
        - WarBias: 8
        - HostileBias: 1
        - WarmongerHate: 8
        - NeutralBias: 6
        - FriendlyBias: 7
        - GuardedBias: 8
        - AfraidBias: 4
        - DiplomaticBalance: 3
        - Friendliness: 10
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 9
        - Loyalty: 10
        - MinorCivFriendlyBias: 7
        - MinorCivNeutralBias: 6
        - MinorCivHostileBias: 5
        - MinorCivWarBias: 4
        - DenounceWillingness: 5
        - Forgiveness: 5
        - Meanness: 3
        - Neediness: 8
        - Chattiness: 10
        - DeceptiveBias: 6
        - Rationale: COALITION STABILITY MAXIMUM: Ethiopia reaches Order:3 in 2 turns (393-394), enabling CEP proposal. Greece at 48% diplomatic victory. Anti-Greek coalition (Japan 5 + Mongolia 11 + Ottomans 9 + Songhai 5 = 30) has +1 margin over Greek bloc (29). Any defection loses WC blocking power. Maximum Loyalty (10), Friendliness (10), WorkWithWillingness (10), Chattiness (10) ensures AI maintains defensive pacts and declarations of friendship through critical voting period.
        
        ## Technology
        - Next: None
        
        ## Policy
        - Next: Third Alternative (Policy)
        - Rationale: RESOURCE ACCELERATION TIMING: Third Alternative tenet provides +100% strategic resources (4 Uranium vs current 2) enabling dual Atomic Bomb production upon Manhattan Project completion, and -25% unit maintenance costs to support large standing army. Must acquire before Ethiopia adopts Order:3 (estimated Turn 393-394) to ensure nuclear deterrent ready. Lightning Warfare deferred - mobility bonuses irrelevant until Transport production resumes.
        
        ## Relationships
        
        ### Vatican City
        - Public: 60
        - Private: 55
        - Rationale: Establishing positive relationship with Monaco (currently 0 influence). Cheap investment target - reaching Friend status (30+) yields a new delegate quickly. With Budapest potentially lost to Open Door, Monaco provides replacement delegate to maintain voting bloc strength against Greece's 19-delegate coalition.
        - UpdatedTurn: 268
        
        ### Monaco
        - Public: 0
        - Private: 0
        - Rationale: Monaco has been defeated - no longer exists as a city-state. Clearing previous extreme priority values (95/90) as they are no longer actionable. Previous strategy of purchasing Monaco influence is moot.
        - UpdatedTurn: 289
        
        ### Almaty
        - Public: 85
        - Private: 80
        - Rationale: Almaty now has Open Door enacted by World Congress (influence locked at 40, no allies possible). Previous strategy of racing to ally status is now impossible. Reducing priority but maintaining positive stance for potential trade routes and quest rewards.
        - UpdatedTurn: 289
        
        ### Wanggeom
        - Public: 100
        - Private: 100
        - Rationale: MAXIMUM WANGGEOM PRIORITY. Decolonization threatens to reduce our 747 influence to 50, destroying this alliance. Setting maximum relationship values signals to AI that Wanggeom is our most critical city-state asset. Combined with voting against Decolonization, we must protect this delegate at all costs.
        - UpdatedTurn: 353
        
        ### Babylon
        - Public: 55
        - Private: 50
        - Rationale: MODERATE POSITIVE STANCE TO BABYLON. Greek vassal with 5 automatic hostile delegates, BUT 86% war weariness vs Songhai and 764 military strength (weak). Potential future independence target if Greece overextends. Maintains diplomatic channel without provoking unnecessary hostility given automatic pro-Greece votes.
        - UpdatedTurn: 361
        
        ### Carthage
        - Public: 0
        - Private: -10
        - Rationale: NEUTRAL/HOSTILE TO CARTHAGE. Greek vassal with 3 automatic hostile delegates, negligible military (964), single city (Gades). No active threat but automatic WC opposition requires zero diplomatic investment. Previous denouncement appropriate.
        - UpdatedTurn: 361
        
        ### Abernethy
        - Public: 70
        - Private: 65
        - Rationale: ELEVATED ABERNETHY PRIORITY. Open Door currently active (0 influence all civs). No repeal proposal yet, but maintaining positive stance positions for future acquisition. With 0 influence cost to enter competition, Abernethy offers cheap delegate if Open Door repealed. Moderate priority as backup to Riga strategy.
        - UpdatedTurn: 361
        
        ### Greece
        - Public: -90
        - Private: -100
        - Rationale: ABSOLUTE GREECE HOSTILITY: Greece at 20 delegates (44% victory), 6235 military, proposing Copenhagen Sphere in 7 turns. Hostility preserves anti-Greek coalition coherence. Maximum pressure maintains deterrence while we defend Copenhagen and push science victory. Their vassals Babylon and Carthage provide automatic votes - no diplomatic solution possible.
        - UpdatedTurn: 387
        
        ### Ethiopia
        - Public: -95
        - Private: -100
        - Rationale: ABSOLUTE MAXIMUM ETHIOPIA HOSTILITY: Ethiopia at Influential on all 7 civs, Order:2, ONE TENET from CEP eligibility. Transport landing at Lalibela possible Turn 396, ~14 turns before they can adopt Order:3. Maximum negative relationship ensures AI prepares for instant war escalation. No diplomatic solution - they win in ~20-30 turns if CEP completes.
        - UpdatedTurn: 387
        
        ### Salem
        - Public: 100
        - Private: 100
        - Rationale: SALEM PRIORITY: Rig operation in progress (Agent Morozumi, network 96). Success provides immediate delegate to strengthen coalition. Ottoman Sphere proposal on Salem pending - we need this city-state for delegate count. Maximum priority ensures AI supports espionage operation and maintains investment if rig succeeds.
        - UpdatedTurn: 387
        
        ### Zurich
        - Public: 100
        - Private: 100
        - Rationale: ZURICH ALLIANCE CRITICAL: At 212 influence (Friend), need immediate Ally conversion for +1 delegate. Economy briefing identified ~10G ally request cost. Maximum relationship values signal AI to prioritize this cheap delegate acquisition. Every delegate counts for 45-delegate threshold.
        - UpdatedTurn: 391
        
        ### Antwerp
        - Public: 100
        - Private: 100
        - Rationale: ANTWERP ALLIANCE CRITICAL: At 469 influence (Friend) with Mongolia as current ally, but we are Friends with highest influence. Ally conversion provides +1 delegate for ~10G per economy briefing. Maximum priority despite Mongolian Sphere proposal - ally status reversible, delegate gain immediate.
        - UpdatedTurn: 391
        
        ### Veligrad
        - Public: 100
        - Private: 100
        - Rationale: VELIGRAD ALLIANCE CRITICAL: At 160 influence (Friend), conversion to Ally provides +1 delegate for minimal cost (~10G). Ottoman ally currently but our high influence makes flip possible. Three quick delegates (Zurich, Antwerp, Veligrad) raise Japan from 5 to 8 delegates, strengthening anti-Greek coalition from 30 to 33.
        - UpdatedTurn: 391
        
        ### Riga
        - Public: 0
        - Private: 0
        - Rationale: RIGA ABANDONMENT: Influence collapsed to 1 (Neutral), Greece at 247 with Protected status. Unrecoverable with current gold reserves. Clearing previous high values to deprioritize AI attention - focus resources on winnable city-states (Zurich, Antwerp, Veligrad) instead.
        - UpdatedTurn: 391
        
        ### Mongolia
        - Public: 100
        - Private: 100
        - Rationale: MONGOLIA COALITION ANCHOR MAXIMUM: 11 delegates critical for anti-Greek voting bloc. Shared Autocracy (999 bonus) and defensive pact must be preserved at all costs. Maximum loyalty signaling prevents any Greek diplomatic overtures during critical turns 393-394 when Ethiopia reaches Order:3.
        - UpdatedTurn: 391
        
        ### Songhai
        - Public: 100
        - Private: 100
        - Rationale: SONGHAI STABILIZATION CRITICAL: Songhai at 100% war weariness vs Greece, -99 GPT deficit, their 5 delegates essential for coalition majority. Maximum loyalty signaling prevents Greek peace overtures. With delegate count tied 31-31, any Songhai defection loses blocking power. Declaration of Friendship and trade partnership must be preserved at all costs during Copenhagen Sphere vote period.
        - UpdatedTurn: 394
        
        ### Copenhagen
        - Public: 100
        - Private: 95
        - Rationale: COPENHAGEN EMERGENCY INVESTMENT: Greece proposing Sphere in 7 turns - if passed, permanent Greek ally and we lose delegate forever. Currently at -6 influence vs Greece 630. Despite 200G cost to reach Ally status, must invest immediately after Zurich/Veligrad purchases. Copenhagen's 4 delegates critical for coalition majority. Maximum priority ensures AI allocates treasury to this save once cheaper allies secured.
        - UpdatedTurn: 394
        
        ### The Ottomans
        - Public: 100
        - Private: 100
        - Rationale: OTTOMAN DELEGATE LOSS RESPONSE: Ottomans dropped from 9 to 7 delegates - critical for coalition stability at 45-vote threshold. Maximum relationship values reinforce commitment and signal AI to prioritize defensive pact maintenance, trade partnerships, and coordinated WC voting. Any further Ottoman defection loses Copenhagen blocking power.
        - UpdatedTurn: 395
        
        ## Strategy
        - Rationale: MAINTAIN COALITION STABILITY AND NUCLEAR PATH: Current persona (Loyalty 10, Friendliness 10, WorkWithWillingness 10, Chattiness 10) prevents any defections in anti-Greek coalition during critical Turn 404 voting period. Mongolia(12) + Ottomans(7) + Songhai(5) + Japan(5) = 29 delegates, Salem rig could add +4. Policy Third Alternative correctly queued for +100% strategic resources enabling dual atomic bomb production upon Nuclear Fission completion. Technology Nuclear Fission (17 turns remaining) is correct path to Manhattan Project and nuclear deterrent. Relationships all correctly positioned for maximum coalition cohesion. Grand Strategy Spaceship maintained as primary victory path with Ethiopia cultural threat as secondary concern.
        - GrandStrategy: Spaceship
        
        ### Flavors
        - Offense: 75
        - Defense: 60
        - Mobilization: 90
        - CityDefense: 55
        - MilitaryTraining: 75
        - Recon: 40
        - Ranged: 60
        - Mobile: 75
        - Nuke: 75
        - UseNuke: 65
        - Naval: 85
        - NavalRecon: 85
        - NavalGrowth: 70
        - NavalTileImprovement: 40
        - Air: 75
        - AirCarrier: 60
        - Antiair: 40
        - Airlift: 40
        - Expansion: 0
        - Growth: 60
        - TileImprovement: 60
        - Infrastructure: 70
        - Production: 85
        - WaterConnection: 60
        - Gold: 90
        - Science: 95
        - Culture: 15
        - Happiness: 60
        - GreatPeople: 65
        - Wonder: 5
        - Religion: 5
        - Diplomacy: 95
        - Spaceship: 90
        - Espionage: 80
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Songhai
        - Leader: Askia
        - IsMajor: true
        - OurOpinionOfThem:
          - Japan's leader has expressed a public opinion of Songhai (100).
          - Japan's leader has formed a private opinion of Songhai (100).
          - We are trade partners. (40)
          - We have opened our borders to each other. (12)
          - You (Songhai) have denounced one of Japan's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have shared embassies. (1)
          - Japan's real approach to Songhai is Friendly.
          - We have divergent Social Policies. (-3)
          - Religious differences strain your (Songhai) relationship. (-30)
          - You (Songhai) have chosen to adopt the Freedom Ideology, but Japan believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - Your (Japan) votes supported Songhai's civ's interests in the World Congress.
          - You (Japan) have denounced one of Songhai's declared enemies!
          - We have made a public Declaration of Friendship!
          - We are trade partners.
          - Your (Japan) recent diplomatic actions please Songhai.
          - We have opened our borders to each other.
          - We have shared embassies.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - You (Japan) have chosen to adopt the Autocracy Ideology, but Songhai believe in Freedom.
          - Songhai desire friendly relations with Japan.
          - You (Japan) have made a Declaration of Friendship with one of Songhai's enemies!
        - Score: 1436
        - Era: Atomic
        - Technologies: 58
        - Cities: 6
        - Population: 130
        - Territory: 153
        - Gold: 1181
        - GoldPerTurn: -47
        - HappinessSituation: Happy
        - HappinessPercentage: 61
        - MilitaryStrength: 1106
        - TourismPerTurn: 246.75
        - CulturePerTurn: 623
        - PolicyBranches:
          - Fealty: 6
          - Freedom: 3
          - Imperialism: 6
          - Authority: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Far
            - Open Borders
          - Greece:
            - Distance: Neighbors
            - War (Our Score: -100%; Our War Weariness: 100%)
          - Babylon:
            - Distance: Neighbors
            - War (Our Score: 16%; Our War Weariness: 100%)
            - Denounced Them
            - Denounced By Them
          - Carthage:
            - Distance: Distant
            - War (Our Score: -2%; Our War Weariness: 81%)
          - Ethiopia:
            - Distance: Far
            - Denounced Them
          - Japan:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - The Ottomans:
            - Distance: Neighbors
            - War (Our Score: -54%; Our War Weariness: 84%)
        - Votes: 5
        
        ## Player 1
        - Civilization: Babylon
        - Leader: Nebuchadnezzar II
        - IsMajor: true
        - OurOpinionOfThem:
          - Japan's leader has expressed a public opinion of Babylon (55).
          - Japan's leader has formed a private opinion of Babylon (50).
          - You (Babylon) have denounced one of Japan's declared enemies! (11)
          - You (Babylon) have gone to war in the past.
          - Japan's real approach to Babylon is Planning War.
          - We have divergent Social Policies. (-3)
          - You (Babylon) have denounced a leader Japan made a Declaration of Friendship with! (-11)
          - You (Babylon) have made a Declaration of Friendship with one of Japan's enemies! (-13)
          - Religious differences strain your (Babylon) relationship. (-30)
          - Your (Babylon) spies were caught stealing from Japan. (-33)
          - You (Babylon) have adopted the Order Ideology, but Japan believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - Your (Japan) votes supported Babylon's civ's interests in the World Congress.
          - You (Japan) have denounced one of Babylon's declared enemies!
          - We passed Babylon's proposal in the World Congress.
          - You (Japan) are not competing for technological advancement.
          - We fought together against a common foe.
          - You (Japan) have shared intrigue with Babylon.
          - You (Japan) have no contested borders.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - You (Japan) have chosen to adopt the Autocracy Ideology, but Babylon believe in Order.
          - Babylon desire friendly relations with Japan.
          - You (Japan) have made a Defensive Pact with one of Babylon's enemies!
          - Your (Japan) recent diplomatic actions disappoint Babylon.
          - You (Japan) have made a Declaration of Friendship with one of Babylon's enemies!
          - You (Japan) have denounced a leader Babylon made a Declaration of Friendship with!
        - Score: 1202
        - Era: Modern
        - Technologies: 56
        - Cities: 4
        - Population: 79
        - Territory: 126
        - Gold: 1371
        - GoldPerTurn: 64
        - HappinessSituation: Happy
        - HappinessPercentage: 90
        - MilitaryStrength: 1396
        - TourismPerTurn: 148.5
        - CulturePerTurn: 462
        - PolicyBranches:
          - Order: 1
          - Rationalism: 6
          - Tradition: 6
          - Artistry: 6
        - FoundedReligion: Catholicism
        - Relationships:
          - Mongolia:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Greece:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
          - Songhai:
            - Distance: Neighbors
            - War (Our Score: -16%; Our War Weariness: 86%)
            - Denounced Them
          - Carthage:
            - Distance: Far
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Japan:
            - Distance: Far
          - The Ottomans:
            - Distance: Neighbors
        - Votes: 5
        
        ## Player 2
        - Civilization: The Ottomans
        - Leader: Suleiman
        - IsMajor: true
        - OurOpinionOfThem:
          - Japan's leader has expressed a public opinion of The Ottomans (100).
          - Japan's leader has formed a private opinion of The Ottomans (100).
          - We are trade partners. (40)
          - We have made a Defensive Pact with the same leaders! (15)
          - We have opened our borders to each other. (12)
          - You (The Ottomans) have denounced one of Japan's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have shared embassies. (1)
          - Japan's real approach to The Ottomans is Friendly.
          - We have divergent Social Policies. (-3)
          - You (The Ottomans) have made a Declaration of Friendship with one of Japan's enemies! (-13)
          - You (The Ottomans) have chosen to adopt the Freedom Ideology, but Japan believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - You (Japan) have denounced one of The Ottomans's declared enemies!
          - Your (Japan) votes supported The Ottomans's civ's interests in the World Congress.
          - We have made Declarations of Friendship with the same leaders!
          - We are trade partners.
          - We have made a Defensive Pact with the same leaders!
          - We passed The Ottomans's proposal in the World Congress.
          - We have made a public Declaration of Friendship!
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - You (Japan) have shared intrigue with The Ottomans.
          - The Ottomans's leader has expressed a public opinion of you (Japan) (10).
          - We have shared embassies.
          - We have divergent Social Policies.
          - You (Japan) have chosen to adopt the Autocracy Ideology, but The Ottomans believe in Freedom.
          - The Ottomans desire friendly relations with Japan.
          - You (Japan) plundered The Ottomans's trade routes!
          - You (Japan) have made a Declaration of Friendship with one of The Ottomans's enemies!
          - You (Japan) have denounced a leader The Ottomans made a Declaration of Friendship with!
        - Score: 2123
        - Era: Atomic
        - Technologies: 66
        - Cities: 8
        - Population: 197
        - Territory: 276
        - Gold: 203
        - GoldPerTurn: 54
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 46
        - MilitaryStrength: 13297
        - TourismPerTurn: 229.5
        - CulturePerTurn: 531
        - PolicyBranches:
          - Freedom: 4
          - Tradition: 3
          - Rationalism: 2
          - Statecraft: 3
          - Imperialism: 2
          - Progress: 6
          - Industry: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Close
            - Denounced Them
          - Songhai:
            - Distance: Neighbors
            - War (Our Score: 54%; Our War Weariness: 64%)
          - Carthage:
            - Distance: Distant
            - Denounced Them
          - Ethiopia:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - Japan:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Babylon:
            - Distance: Neighbors
        - Votes: 7
        
        ## Player 3
        - Civilization: Japan
        - Leader: Oda Nobunaga
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: Mongolia, Our top defensive pact ally: The Ottomans
          - Our top World Congress ally: Songhai, Our top World Congress rival: Greece
          - Our top Competitor: Greece
        - Score: 1773
        - Era: Atomic
        - GoldenAge: Estimated in 31 turns
        - Technologies: 63
        - CurrentResearch: Nuclear Fission (Estimated in 16 turns)
        - NextPolicyTurns: 5
        - Cities: 7
        - Population: 160
        - Territory: 210
        - Gold: 1058
        - GoldPerTurn: 332
        - HappinessSituation: Happy
        - HappinessPercentage: 54
        - MilitaryUnits: 60
        - MilitarySupply: 61
        - MilitaryStrength: 5212
        - TourismPerTurn: 356.25
        - CulturePerTurn: 828
        - FaithPerTurn: 138
        - SciencePerTurn: 1198
        - PolicyBranches:
          - Fealty:
            - Fealty
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Enlightenment
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Shadow Networks
            - Trade Confederacy
          - Autocracy:
            - Elite Forces
            - United Front
          - Progress:
            - Progress
            - Organization
            - Liberty
            - Fraternity
          - Authority:
            - Authority
            - Tribute
            - Imperium
            - Militarism
            - Dominance
            - Honor
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Far
            - Denounced Them
          - Songhai:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - Carthage:
            - Distance: Distant
            - Denounced Them
            - Denounced By Them
          - Ethiopia:
            - Distance: Close
            - War (Our Score: 14%; Our War Weariness: 18%)
            - Denounced Them
          - The Ottomans:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Babylon:
            - Distance: Far
        - Votes: 5
        
        ## Player 4
        - Civilization: Carthage
        - Leader: Dido
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Carthage) have denounced one of Japan's declared enemies! (11)
          - Japan's real approach to Carthage is Planning War.
          - We have divergent Social Policies. (-3)
          - Japan's leader has formed a private opinion of Carthage (-10).
          - You (Carthage) have denounced a leader Japan made a Declaration of Friendship with! (-11)
          - You (Carthage) have made a Declaration of Friendship with one of Japan's enemies! (-13)
        - TheirOpinionOfUs:
          - You (Japan) have denounced one of Carthage's declared enemies!
          - Your (Japan) votes supported Carthage's civ's interests in the World Congress.
          - Carthage's leader has expressed a public opinion of you (Japan) (20).
          - You (Japan) are not competing for the favor of the same City-States.
          - We fought together against a common foe.
          - You (Japan) have no contested borders.
          - You (Japan) have been at war in the past, but Carthage do not seem to hold a grudge.
          - We have divergent Social Policies.
          - Carthage suspect we might be a threat to Carthage.
          - Your (Japan) recent diplomatic actions disappoint Carthage.
          - You (Japan) have denounced a leader Carthage made a Declaration of Friendship with!
          - You (Japan) have made a Defensive Pact with one of Carthage's enemies!
          - We have denounced Carthage!
          - You (Japan) have made a Declaration of Friendship with one of Carthage's enemies!
        - Score: 866
        - Era: Modern
        - Technologies: 50
        - Cities: 1
        - Population: 31
        - Territory: 60
        - Gold: 1224
        - GoldPerTurn: 184
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 1286
        - TourismPerTurn: 64.75
        - CulturePerTurn: 389
        - PolicyBranches:
          - Tradition: 6
          - Artistry: 3
          - Statecraft: 3
          - Rationalism: 2
          - Progress: 2
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Far
            - War (Our Score: -22%; Our War Weariness: 11%)
            - Denounced Them
          - Babylon:
            - Distance: Far
            - Declaration of Friendship
          - Songhai:
            - Distance: Distant
            - War (Our Score: 2%; Our War Weariness: 9%)
          - Greece:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Far
            - War (Our Score: -14%; Our War Weariness: 14%)
            - Denounced Them
          - Japan:
            - Distance: Distant
          - The Ottomans:
            - Distance: Distant
        - Votes: 3
        
        ## Player 5
        - Civilization: Mongolia
        - Leader: Genghis Khan
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Mongolia) have both chosen to adopt the Autocracy Ideology. (999)
          - Japan's leader has expressed a public opinion of Mongolia (100).
          - Japan's leader has formed a private opinion of Mongolia (100).
          - We are trade partners. (40)
          - Japan have happily adopted your (Mongolia) religion in the majority of Japan's cities. (30)
          - We have made a Defensive Pact! (20)
          - We have opened our borders to each other. (12)
          - You (Mongolia) have denounced one of Japan's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - You (Mongolia) have gone to war in the past.
          - Japan's real approach to Mongolia is Friendly.
        - TheirOpinionOfUs:
          - You (Japan) have denounced one of Mongolia's declared enemies!
          - You (Japan) have both chosen to adopt the Autocracy Ideology.
          - We have made a public Declaration of Friendship!
          - We are trade partners.
          - Your (Japan) votes supported Mongolia's civ's interests in the World Congress.
          - Mongolia's leader has expressed a public opinion of you (Japan) (40).
          - We have made Declarations of Friendship with the same leaders!
          - Your (Japan) recent diplomatic actions please Mongolia.
          - We passed Mongolia's proposal in the World Congress.
          - You (Japan) have adopted Mongolia's religion in the majority of your (Japan) cities.
          - We have made a Defensive Pact!
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - We have similar Social Policies.
          - You (Japan) have shared intrigue with Mongolia.
          - We have shared embassies.
          - You (Japan) have been at war in the past, but Mongolia do not seem to hold a grudge.
          - Mongolia desire friendly relations with Japan.
          - Territorial disputes strain your (Japan) relationship.
        - Score: 2158
        - Era: Atomic
        - Technologies: 65
        - Cities: 6
        - Population: 162
        - Territory: 194
        - Gold: 438
        - GoldPerTurn: 489
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 4980
        - TourismPerTurn: 588
        - CulturePerTurn: 1023
        - PolicyBranches:
          - Tradition: 2
          - Rationalism: 2
          - Progress: 2
          - Authority: 4
          - Fealty: 1
          - Industry: 1
          - Artistry: 1
          - Statecraft: 6
          - Autocracy: 2
          - Imperialism: 1
        - FoundedReligion: Tengriism
        - Relationships:
          - Babylon:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
          - Greece:
            - Distance: Close
            - War (Our Score: -6%; Our War Weariness: 5%)
            - Denounced Them
          - Songhai:
            - Distance: Far
            - Open Borders
          - Carthage:
            - Distance: Far
            - War (Our Score: 22%; Our War Weariness: 1%)
            - Denounced Them
          - Ethiopia:
            - Distance: Distant
            - Open Borders
          - Japan:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Ottomans:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 12
        
        ## Player 6
        - Civilization: Greece
        - Leader: Alexander
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Greece) have denounced one of Japan's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - Japan's real approach to Greece is Planning War.
          - We have divergent Social Policies. (-3)
          - You (Greece) have denounced a leader Japan made a Declaration of Friendship with! (-11)
          - You (Greece) have made a Declaration of Friendship with one of Japan's enemies! (-13)
          - Religious differences strain your (Greece) relationship. (-30)
          - Japan's leader has expressed a public opinion of Greece (-90).
          - Japan's leader has formed a private opinion of Greece (-100).
          - You (Greece) have chosen to adopt the Order Ideology, but Japan believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - We passed Greece's proposal in the World Congress.
          - You (Japan) have denounced one of Greece's declared enemies!
          - You (Japan) have no contested borders.
          - We fought together against a common foe.
          - We have Pledged to Protect the same City-States.
          - You (Japan) have gone to war in the past.
          - Greece don't want anything to do with us (Japan) right now.
          - Religious differences strain your (Japan) relationship.
          - We have divergent Social Policies.
          - Your (Japan) spies were caught stealing from Greece.
          - You (Japan) have made a Defensive Pact with one of Greece's enemies!
          - You (Japan) are competing for the favor of the same City-States!
          - Your (Japan) recent diplomatic actions disappoint Greece.
          - You (Japan) have made a Declaration of Friendship with one of Greece's enemies!
          - You (Japan) have denounced a leader Greece made a Declaration of Friendship with!
          - We have denounced each other!
          - We placed sanctions on Greece in the World Congress.
          - You (Japan) have chosen to adopt the Autocracy Ideology, but Greece believe in Order.
          - Greece's leader has expressed a public opinion of you (Japan) (-100).
          - Your (Japan) votes opposed Greece's civ's interests in the World Congress.
        - Score: 3186
        - Era: Atomic
        - Technologies: 61
        - Cities: 16
        - Population: 331
        - Territory: 645
        - Gold: 311
        - GoldPerTurn: 167
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 50
        - MilitaryStrength: 7029
        - TourismPerTurn: 527.5
        - CulturePerTurn: 1746
        - PolicyBranches:
          - Order: 5
          - Tradition: 6
          - Rationalism: 2
          - Statecraft: 6
          - Imperialism: 1
          - Progress: 2
          - Industry: 3
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Close
            - War (Our Score: 6%; Our War Weariness: 2%)
            - Denounced Them
          - Babylon:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
          - Songhai:
            - Distance: Neighbors
            - War (Our Score: 100%; Our War Weariness: 90%)
            - Denounced Them
          - Carthage:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Neighbors
            - War (Our Score: 16%; Our War Weariness: 38%)
            - Denounced Them
          - Japan:
            - Distance: Far
            - Denounced Them
          - The Ottomans:
            - Distance: Close
            - Denounced Them
        - Votes: 22
        
        ## Player 7
        - Civilization: Ethiopia
        - Leader: Haile Selassie
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Ethiopia) have denounced one of Japan's declared enemies! (11)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - Japan's real approach to Ethiopia is War.
          - Religious differences strain your (Ethiopia) relationship. (-30)
          - Your (Ethiopia) spies were caught stealing from Japan. (-33)
          - Japan's leader has expressed a public opinion of Ethiopia (-95).
          - Japan's leader has formed a private opinion of Ethiopia (-100).
          - You (Ethiopia) have chosen to adopt the Order Ideology, but Japan believe in Autocracy. (-999)
          - You (Ethiopia) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Japan) have denounced one of Ethiopia's declared enemies!
          - We previously passed Ethiopia's proposal in the World Congress.
          - We have made Declarations of Friendship with the same leaders!
          - Ethiopia's leader has expressed a public opinion of you (Japan) (60).
          - You (Japan) are not competing for World Wonders.
          - You (Japan) are not competing for cultural advancement.
          - Your (Japan) recent diplomatic actions please Ethiopia.
          - Your (Japan) votes supported Ethiopia's civ's interests in the World Congress.
          - We have similar Social Policies.
          - You (Japan) have no contested borders.
          - You (Japan) killed or captured Ethiopia's civilians!
          - Religious differences strain your (Japan) relationship.
          - We tried to place sanctions on Ethiopia in the World Congress.
          - We have denounced Ethiopia!
          - You (Japan) have chosen to adopt the Autocracy Ideology, but Ethiopia believe in Order.
          - You (Japan) are at war!
        - Score: 2379
        - Era: Atomic
        - Technologies: 65
        - Cities: 10
        - Population: 221
        - Territory: 444
        - Gold: 1750
        - GoldPerTurn: 321
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 41
        - MilitaryStrength: 1471
        - TourismPerTurn: 707.25
        - CulturePerTurn: 1560
        - PolicyBranches:
          - Tradition: 5
          - Rationalism: 2
          - Progress: 2
          - Authority: 1
          - Fealty: 1
          - Industry: 1
          - Artistry: 5
          - Statecraft: 4
          - Order: 3
        - FoundedReligion: Eastern Orthodoxy
        - Relationships:
          - Mongolia:
            - Distance: Distant
            - Open Borders
          - Greece:
            - Distance: Neighbors
            - War (Our Score: -16%; Our War Weariness: 53%)
          - Songhai:
            - Distance: Far
          - Carthage:
            - Distance: Far
            - War (Our Score: 14%; Our War Weariness: 32%)
            - Denounced Them
          - Babylon:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 30%)
          - Japan:
            - Distance: Close
            - War (Our Score: -14%; Our War Weariness: 28%)
          - The Ottomans:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
        - Votes: 9
        
        ## Player 22
        - Civilization: Riga
        - Leader: City State
        - MajorAlly: Greece
        - Population: 21
        - MajorityReligion: Buddhism
        - Relationships:
          - Babylon: Friends (Influence: 133, Distance: Far)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Greece: Ally (Influence: 560, Distance: Close, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Carthage: Neutral (Influence: -49, Distance: Distant)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: Neutral (Influence: 5, Distance: Distant, Protected)
          - The Ottomans: Friends (Influence: 64, Distance: Close, Protected)
        
        ## Player 23
        - Civilization: Monaco
        - Leader: City State
        - MajorAlly: Greece
        - Population: 13
        - Relationships:
          - Babylon: Neutral (Influence: 5, Distance: Neighbors, Protected)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Greece: Ally (Influence: 881, Distance: Neighbors, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Carthage: Friends (Influence: 117, Distance: Distant)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: Neutral (Influence: 5, Distance: Far)
          - The Ottomans: Friends (Influence: 175, Distance: Close, Protected)
        
        ## Player 24
        - Civilization: Salem
        - Leader: City State
        - MajorAlly: The Ottomans
        - Population: 16
        - MajorityReligion: Buddhism
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Close)
          - Mongolia: Neutral (Influence: 0, Distance: Distant)
          - Greece: Friends (Influence: 144, Distance: Close, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Carthage: Friends (Influence: 70, Distance: Distant)
          - Ethiopia: Neutral (Influence: 19, Distance: Distant)
          - Japan: Neutral (Influence: 10, Distance: Far, Protected)
          - The Ottomans: Ally (Influence: 226, Distance: Neighbors, Protected)
        
        ## Player 25
        - Civilization: Zurich
        - Leader: City State
        - MajorAlly: Greece
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: -11, Distance: Distant)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Greece: Ally (Influence: 283, Distance: Close, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Carthage: Neutral (Influence: -26, Distance: Far)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Japan: Friends (Influence: 191, Distance: Far, Protected)
          - The Ottomans: Neutral (Influence: 0, Distance: Distant)
        
        ## Player 26
        - Civilization: Manila
        - Leader: City State
        - MajorAlly: Greece
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 15, Distance: Distant)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Greece: Ally (Influence: 973, Distance: Neighbors, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Carthage: Friends (Influence: 212, Distance: Close, Protected)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Japan: Neutral (Influence: 0, Distance: Distant)
          - The Ottomans: Friends (Influence: 174, Distance: Distant)
        
        ## Player 27
        - Civilization: Copenhagen
        - Leader: City State
        - MajorAlly: Greece
        - Population: 9
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Greece: Ally (Influence: 620, Distance: Neighbors, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Carthage: Neutral (Influence: 0, Distance: Far)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Japan: Neutral (Influence: -3, Distance: Distant)
          - The Ottomans: Friends (Influence: 119, Distance: Distant)
        
        ## Player 28
        - Civilization: Veligrad
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 26
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Far)
          - Mongolia: Ally (Influence: 762, Distance: Neighbors, Protected)
          - Greece: War (Influence: -60, Distance: Close)
          - Songhai: Neutral (Influence: -25, Distance: Far)
          - Carthage: War (Influence: -60, Distance: Close)
          - Ethiopia: Friends (Influence: 121, Distance: Distant)
          - Japan: Friends (Influence: 162, Distance: Close, Protected)
          - The Ottomans: Friends (Influence: 468, Distance: Far, Protected)
        
        ## Player 29
        - Civilization: Wanggeom
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 19
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Distant)
          - Mongolia: Ally (Influence: 509, Distance: Close, Protected)
          - Greece: War (Influence: -60, Distance: Distant)
          - Songhai: Neutral (Influence: -10, Distance: Distant)
          - Carthage: War (Influence: -60, Distance: Distant)
          - Ethiopia: Neutral (Influence: 8, Distance: Far)
          - Japan: Friends (Influence: 164, Distance: Neighbors, Protected)
          - The Ottomans: Neutral (Influence: 25, Distance: Far)
        
        ## Player 30
        - Civilization: Abernethy
        - Leader: City State
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Close)
          - Mongolia: Neutral (Influence: 0, Distance: Distant)
          - Greece: Neutral (Influence: 5, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Close)
          - Carthage: Friends (Influence: 60, Distance: Far)
          - Ethiopia: Friends (Influence: 58, Distance: Close, Protected)
          - Japan: Neutral (Influence: 0, Distance: Distant)
          - The Ottomans: Friends (Influence: 36, Distance: Distant)
        
        ## Player 31
        - Civilization: Hanoi
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 26
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Distant)
          - Mongolia: Ally (Influence: 575, Distance: Neighbors, Protected)
          - Greece: War (Influence: -60, Distance: Close)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - Carthage: War (Influence: -60, Distance: Far)
          - Ethiopia: Neutral (Influence: 18, Distance: Distant)
          - Japan: Friends (Influence: 58, Distance: Far)
          - The Ottomans: Friends (Influence: 78, Distance: Distant)
        
        ## Player 32
        - Civilization: Vatican City
        - Leader: City State
        - MajorAlly: Ethiopia
        - Population: 25
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Distant)
          - Mongolia: Friends (Influence: 80, Distance: Distant)
          - Greece: War (Influence: -60, Distance: Far)
          - Songhai: Neutral (Influence: 17, Distance: Far)
          - Carthage: War (Influence: -60, Distance: Distant)
          - Ethiopia: Ally (Influence: 320, Distance: Neighbors, Protected)
          - Japan: War (Influence: -60, Distance: Far)
          - The Ottomans: Friends (Influence: 37, Distance: Far, Protected)
        
        ## Player 33
        - Civilization: Budapest
        - Leader: City State
        - Population: 20
        - Relationships:
          - Babylon: Neutral (Influence: 9, Distance: Close, Protected)
          - Mongolia: Neutral (Influence: 15, Distance: Distant)
          - Greece: Friends (Influence: 285, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 5, Distance: Close)
          - Carthage: Neutral (Influence: 15, Distance: Close)
          - Ethiopia: Neutral (Influence: -38, Distance: Far)
          - Japan: Friends (Influence: 35, Distance: Distant)
          - The Ottomans: Friends (Influence: 362, Distance: Distant)
        
        ## Player 34
        - Civilization: Buenos Aires
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Distant)
          - Mongolia: Ally (Influence: 245, Distance: Distant)
          - Greece: War (Influence: -60, Distance: Far)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - Carthage: War (Influence: -60, Distance: Distant)
          - Ethiopia: Neutral (Influence: 1, Distance: Neighbors)
          - Japan: Friends (Influence: 35, Distance: Distant)
          - The Ottomans: Friends (Influence: 172, Distance: Distant)
        
        ## Player 35
        - Civilization: Antananarivo
        - Leader: City State
        - MajorAlly: Greece
        - Population: 8
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Greece: Ally (Influence: 918, Distance: Neighbors, Protected)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Carthage: Neutral (Influence: 15, Distance: Far)
          - Ethiopia: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Japan: Friends (Influence: 141, Distance: Distant)
          - The Ottomans: Friends (Influence: 51, Distance: Distant)
        
        ## Player 36
        - Civilization: Almaty
        - Leader: City State
        - Population: 10
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 375, Distance: Neighbors, Protected)
          - Greece: Friends (Influence: 146, Distance: Distant)
          - Songhai: Neutral (Influence: 22, Distance: Distant)
          - Carthage: Neutral (Influence: 0, Distance: Distant)
          - Ethiopia: Friends (Influence: 249, Distance: Distant)
          - Japan: Friends (Influence: 129, Distance: Close, Protected)
          - The Ottomans: Friends (Influence: 36, Distance: Far)
        
        ## Player 37
        - Civilization: Antwerp
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 26
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: War (Influence: -60, Distance: Far)
          - Mongolia: Ally (Influence: 684, Distance: Neighbors, Protected)
          - Greece: War (Influence: -60, Distance: Far)
          - Songhai: Neutral (Influence: -1, Distance: Far)
          - Carthage: War (Influence: -60, Distance: Distant)
          - Ethiopia: Friends (Influence: 433, Distance: Distant)
          - Japan: Friends (Influence: 433, Distance: Neighbors, Protected)
          - The Ottomans: Friends (Influence: 327, Distance: Close, Protected)
        - 63: Barbarians
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Greece
        - Greece:
          - CapitalsControlled:
            - Gao
            - Babylon
            - Carthage
            - Athens
          - CapitalsPercentage: 50
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 7
        - Contender: Ethiopia
        - Babylon:
          - Influences:
            - Mongolia: Exotic (21%) - Rising Slowly (tourism/culture ratio 29%)
            - Greece: Exotic (13%) - Rising Slowly (tourism/culture ratio 35%)
            - Songhai: Exotic (18%) - Rising Slowly (tourism/culture ratio 56%)
            - Carthage: Familiar (34%) - Rising Slowly (tourism/culture ratio 70%)
            - Ethiopia: Exotic (10%) - Rising Slowly (tourism/culture ratio 20%)
            - Japan: Familiar (25%) - Rising Slowly (tourism/culture ratio 42%)
            - The Ottomans: Familiar (32%) - Rising Slowly (tourism/culture ratio 93%)
          - PolicyPercentage: 85
          - InfluentialCivs: 0
        - Carthage:
          - Influences:
            - Mongolia: Exotic (6%) - Rising Slowly (tourism/culture ratio 14%)
            - Songhai: Exotic (5%) - Rising Slowly (tourism/culture ratio 23%)
            - Greece: Exotic (6%) - Rising Slowly (tourism/culture ratio 16%)
            - Babylon: Exotic (9%) - Rising Slowly (tourism/culture ratio 31%)
            - Japan: Exotic (6%) - Rising Slowly (tourism/culture ratio 18%)
            - The Ottomans: Exotic (9%) - Rising Slowly (tourism/culture ratio 36%)
          - PolicyPercentage: 77
          - InfluentialCivs: 0
        - Ethiopia:
          - Influences:
            - Mongolia: Influential (106%) - Rising (tourism/culture ratio 145%)
            - Greece: Influential (106%) - Rising (tourism/culture ratio 181%)
            - Songhai: Influential (103%) - Rising (tourism/culture ratio 248%)
            - Carthage: Dominant (260%) - Rising (tourism/culture ratio 430%)
            - Babylon: Influential (115%) - Rising (tourism/culture ratio 266%)
            - Japan: Influential (120%) - Rising (tourism/culture ratio 187%)
            - The Ottomans: Influential (133%) - Rising (tourism/culture ratio 408%)
          - PolicyPercentage: 100
          - InfluentialCivs: 7
        - Greece:
          - Influences:
            - Mongolia: Familiar (40%) - Rising Slowly (tourism/culture ratio 46%)
            - Babylon: Popular (93%) - Rising (8 turns to Influential, tourism/culture ratio 344%)
            - Songhai: Familiar (35%) - Rising Slowly (tourism/culture ratio 78%)
            - Carthage: Influential (196%) - Rising (tourism/culture ratio 409%)
            - Ethiopia: Familiar (38%) - Rising Slowly (tourism/culture ratio 57%)
            - Japan: Familiar (43%) - Rising Slowly (tourism/culture ratio 64%)
            - The Ottomans: Familiar (47%) - Rising Slowly (tourism/culture ratio 133%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - Japan:
          - Influences:
            - Mongolia: Popular (62%) - Rising (184 turns to Influential, tourism/culture ratio 145%)
            - Greece: Exotic (20%) - Rising Slowly (tourism/culture ratio 60%)
            - Songhai: Familiar (29%) - Rising Slowly (tourism/culture ratio 129%)
            - Carthage: Popular (75%) - Rising (50 turns to Influential, tourism/culture ratio 198%)
            - Ethiopia: Exotic (18%) - Rising Slowly (tourism/culture ratio 46%)
            - The Ottomans: Popular (55%) - Rising (129 turns to Influential, tourism/culture ratio 249%)
            - Babylon: Familiar (41%) - Rising (576 turns to Influential, tourism/culture ratio 138%)
          - PolicyPercentage: 96
          - InfluentialCivs: 0
        - Mongolia:
          - Influences:
            - Babylon: Popular (52%) - Rising (74 turns to Influential, tourism/culture ratio 264%)
            - Greece: Familiar (27%) - Rising Slowly (tourism/culture ratio 110%)
            - Songhai: Familiar (36%) - Rising (154 turns to Influential, tourism/culture ratio 230%)
            - Carthage: Influential (102%) - Rising (tourism/culture ratio 364%)
            - Ethiopia: Familiar (25%) - Rising Slowly (tourism/culture ratio 95%)
            - Japan: Popular (88%) - Rising (10 turns to Influential, tourism/culture ratio 342%)
            - The Ottomans: Popular (72%) - Rising (22 turns to Influential, tourism/culture ratio 481%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - Songhai:
          - Influences:
            - Mongolia: Familiar (33%) - Rising Slowly (tourism/culture ratio 58%)
            - Greece: Exotic (21%) - Rising Slowly (tourism/culture ratio 50%)
            - Babylon: Popular (55%) - Rising (248 turns to Influential, tourism/culture ratio 156%)
            - Carthage: Familiar (45%) - Rising Slowly (tourism/culture ratio 113%)
            - Ethiopia: Exotic (19%) - Rising Slowly (tourism/culture ratio 34%)
            - Japan: Familiar (36%) - Rising Slowly (tourism/culture ratio 81%)
            - The Ottomans: Popular (54%) - Rising (448 turns to Influential, tourism/culture ratio 188%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        - The Ottomans:
          - Influences:
            - Mongolia: Exotic (23%) - Rising Slowly (tourism/culture ratio 54%)
            - Greece: Exotic (10%) - Rising Slowly (tourism/culture ratio 32%)
            - Songhai: Exotic (17%) - Rising Slowly (tourism/culture ratio 74%)
            - Carthage: Familiar (34%) - Rising Slowly (tourism/culture ratio 92%)
            - Ethiopia: Exotic (11%) - Rising Slowly (tourism/culture ratio 34%)
            - Japan: Familiar (29%) - Rising Slowly (tourism/culture ratio 78%)
            - Babylon: Familiar (28%) - Rising Slowly (tourism/culture ratio 79%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 45
        - Status: World Congress - Voting in 8 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: 330
          - Sanction: Greece:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 393
          - Greek Sphere of Influence: Copenhagen:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 393
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: 330
          - Greek Sphere of Influence: Monaco:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 360
          - Open Door: Budapest:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 330
          - Mongolian Sphere of Influence: Buenos Aires:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 382
          - Greek Sphere of Influence: Antananarivo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 382
          - Ottoman Sphere of Influence: Salem:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 393
          - Open Door: Abernethy:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 330
          - Mongolian Sphere of Influence: Hanoi:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 349
          - Ethiopian Sphere of Influence: Vatican City:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 349
          - Open Door: Almaty:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 330
          - World Religion: Eastern Orthodoxy:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: 330
          - Mongolian Sphere of Influence: Antwerp:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 360
          - Sanction: Babylon:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 330
        - Proposals:
          - Enact: United Nations:
            - Description: Begins the United Nations project. Once underway, Civilizations can contribute Production towards its completion by selecting it in the city production list. When complete, Civilizations receive bonuses based on how much they contributed.
              : United Nations wonder appears in Capital. (Receive 1 Additional Delegate in the World Congress for every 8 City-States originally in the World. Also, when you expend a Great Person, earn 25 Influence with all City-States you have met. Triggers a Golden Age, as well as the United Nations Special Session of the World Congress if the world has reached the Atomic Era.)
              : Receive an immediate boost of 25 Influence with all City-States. The Consulate National Wonder appears in Capital. (Receive 1 Additional Delegate in the World Congress for every 8 City-States originally in the World.)
              : Receive a free Great Diplomat.
              Available once any Civilization discovers Atomic Theory.
            - Proposer: Greece
          - Enact: Decolonization:
            - Description: Enforce global decolonization. If successful, the Influence of all Players with all City-States is lowered to 50, unless they are permanent allies.
              Available once any Civilization discovers Radio.
            - Proposer: Mongolia
          - Enact: Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - Proposer: Ethiopia
        - Contender: Greece
        - Babylon:
          - Delegates: 5
          - VictoryPercentage: 11
        - Carthage:
          - Delegates: 3
          - VictoryPercentage: 6
        - Ethiopia:
          - Delegates: 9
          - VictoryPercentage: 20
        - Greece:
          - Delegates: 22
          - VictoryPercentage: 48
        - Japan:
          - Delegates: 5
          - VictoryPercentage: 11
        - Mongolia:
          - Delegates: 12
          - VictoryPercentage: 26
        - Songhai:
          - Delegates: 5
          - VictoryPercentage: 11
        - The Ottomans:
          - Delegates: 7
          - VictoryPercentage: 15
        
        # Briefings
        ## Military Briefing
        (Produced with your instruction: CRITICAL ETHIOPIA CEP MONITORING: Check every Ethiopian city (Lalibela, Axum, Gondar, Harar, Addis Ababa, Bahir Dar) production queues for Citizen Earth Protocol appearance - report IMMEDIATELY if seen. Verify Transport/Landing Ship production queue status in ALL coastal cities - we need amphibious capability for Ethiopian coastal strike if CEP appears. Confirm exact count of embarkable infantry units and time to reach 23-unit threshold. Track Japanese destroyer blockade integrity at Gondar sea zone. Report any new Ethiopian naval threats that could disrupt blockade.)
        
        **MILITARY BRIEF – Oda Nobunaga (Japan) – TURN 396**  
        *All statements are derived from the supplied game data. No speculation or recommendations are included.*
        
        --------------------------------------------------------------------
        ### 1. Ethiopian “Citizen Earth Protocol” (CEP) – Production Scan
        - **Cities checked:** Lalibela, Axum, Gondar, Harar, Addis Ababa, Bahir Dar.  
        - **Result:** No production queue entry for any CEP‑related project was visible in any of the six cities. (The game data does not expose city‑level production queues; none of the listed cities show a CEP build.)  
        
        **Conclusion:** No CEP activity detected as of Turn 396.
        
        --------------------------------------------------------------------
        ### 2. Japanese Transport / Landing‑Ship Production
        - **Current queue:** No Transport (e.g., Transport, Landing Ship) is under construction in any Japanese city, including Osaka, Kyoto, Kagoshima, or Nagoya.  
        - **Implication:** With the present production schedule, the earliest a Transport could be completed would be **Turn 401** (if a Transport were queued immediately, assuming the standard 6‑turn build time). No Transport will be available before that date.
        
        --------------------------------------------------------------------
        ### 3. Embarkable Infantry – Current Count & Gap to 23‑Unit Threshold
        | Unit Type (Embarkable) | Quantity in Friendly Land Zones |
        |------------------------|---------------------------------|
        | **Riflemen** (can embark) | 9 (Kyoto 3 + Tokyo 3 + Nara 2 + Nagoya 1) |
        | **Infantry** (can embark) | 0 |
        | **Other ground units** (Machine Gun, Artillery, etc.) | Not embarkable |
        
        - **Total embarkable infantry:** **9** units.  
        - **Units needed to reach the 23‑unit target:** **14** additional embarkable infantry.  
        - **Production outlook:** No infantry‑type units (Riflemen/Infantry) are currently in a production queue; additional production orders will be required to close the gap.
        
        --------------------------------------------------------------------
        ### 4. Japanese Destroyer Blockade – Gondar Sea Zone
        - No dedicated sea zone for **Gondar** appears in the supplied zone data. Consequently, there is **no Japanese destroyer presence** that can be identified as enforcing a blockade of Gondar’s coastal waters at this time.  
        - Existing destroyer forces are positioned in the following sea zones:  
          - **‑8651** (near Nara) – 15 destroyers  
          - **‑1238**, **‑1979**, **‑1080** – each hosting 1–2 destroyers  
        - **Status:** No destroyer units are currently stationed in a sea zone that would directly interdict Gondar’s access to the sea.
        
        --------------------------------------------------------------------
        ### 5. New Ethiopian Naval Threats
        - Ethiopian naval units are **absent** from all listed land and sea zones. No Ethiopian ships, coastal artillery, or anti‑ship assets have been reported.  
        - **Conclusion:** No emerging Ethiopian naval threat that could jeopardize a Japanese sea operation has been observed.
        
        --------------------------------------------------------------------
        ### 6. Summary of Immediate Operational Constraints
        - **CEP monitoring:** No Ethiopian CEP production detected.  
        - **Amphibious capability:** No Transport built or queued; earliest availability ≈ Turn 401.  
        - **Embarkable infantry:** 9 units on hand; 14 more required to achieve the 23‑unit threshold.  
        - **Naval blockade:** No destroyer presence in a Gondar‑adjacent sea zone; existing destroyers are elsewhere.  
        - **Ethiopian naval activity:** None detected.
        
        *All items above reflect the state of the game at the end of Turn 396.*
        
        ## Economy Briefing
        (Produced with your instruction: DELEGATE PURCHASE EXECUTION VERIFICATION: Confirm Zurich(98G) and Veligrad(119G) purchases completed successfully for +4 delegates. Calculate post-purchase treasury and project when we can afford additional city-state investments. With 334 GPT, determine timeline for reaching 500G/750G/1000G thresholds needed for other influence purchases. Track trade route stability - any interruption to GPT flow threatens future delegate acquisition timing. Identify next cheapest delegate sources after Zurich/Veligrad acquisitions.)
        
        **Economic Briefing – Turn 396 (Post‑Deal Confirmation)**  
        
        ---
        
        ### 1. Delegate‑purchase verification
        - **Zurich** purchase (cost 98 G) – completed. Influence now **212** (Friends → Ally). Delegate count **+1**.  
        - **Veligrad** purchase (cost 119 G) – completed. Influence now **162** (Friends → Ally). Delegate count **+1**.  
        
        **Result:** Japan’s UN delegate total rises from **5 → 7** (the two new allies each grant one delegate). The purchases are fully reflected in the treasury.
        
        ---
        
        ### 2. Treasury after purchases
        | Item | Gold cost | Treasury before | Treasury after |
        |------|-----------|----------------|----------------|
        | Starting gold (turn 395) | – | 1 058 G | – |
        | Zurich purchase | 98 G | – | 960 G |
        | Veligrad purchase | 119 G | – | 841 G |
        | **Net gold after purchases** | **‑217 G** | **1 058 G** | **841 G** |
        
        Current **gold balance:** **841 G**.  
        
        Gold per turn (from all cities) = **332 G/turn** (see Player 3 stats). Net income after upkeep is already accounted for in that figure.
        
        ---
        
        ### 3. Timeline to reach higher gold thresholds  
        
        | Target | Gold needed from current (841 G) | Turns required at +332 G/turn* |
        |--------|--------------------------------|--------------------------------|
        | 500 G  | Already exceeded (841 G) | **0** (available now) |
        | 750 G  | 0 (already ≥ 750) | **0** |
        | 1 000 G | 1 000 – 841 = 159 G | **≈ 1 turn** (159 ÷ 332 ≈ 0.48) |
        
        \*Assumes no unexpected gold‑draining events (e.g., war wear‑wear costs, emergency purchases).  
        
        **Conclusion:** We can afford any additional delegate‑purchase or city‑state investment that costs up to **1 000 G** within the next single turn; a 1 500 G purchase would require roughly **2 turns** (1 500 – 841 = 659 G → 2 turns).
        
        ---
        
        ### 4. Trade‑route stability & gold flow risk
        - **Outgoing routes** (Kyoto → Ottoman, Mongolia, City‑states) contribute **≈ 120 G turn‑based** (sum of gold per turn values listed).  
        - **Incoming routes** (Ottoman & Mongolia carriers) contribute **≈ 140 G turn‑based**.  
        - **Net trade‑route gold** ≈ **+260 G/turn**, already embodied in the 332 G/turn total.  
        - No trade‑route interruptions have been reported this turn; all routes have > 5 turns remaining.  
        - Should any route be cut (e.g., war‑weariness causing a “no‑trade” sanction), we would lose roughly **250 G/turn**, pushing the net income below the 300 G/turn threshold and extending the time to reach the 1 000 G mark by 1‑2 turns. Monitor the diplomatic situation with Greece (sanction) and Mongolia (defensive pact) for any sudden termination.
        
        ---
        
        ### 5. Cheapest additional delegate sources (post‑Zurich/Veligrad)
        
        | City‑State | Current Influence | Status | Cost to become Ally* | Delegate gain |
        |------------|-------------------|--------|----------------------|----------------|
        | **Antwerp** | 433 (Friends) | Not ally | ~10 G (Ally request) | +1 |
        | **Zurich** (already allied) | 212 | **Ally** | – | – |
        | **Veligrad** (already allied) | 162 | **Ally** | – | – |
        | **Riga** | 1 (Neutral) | Not ally | ≈ 99 G (Gold‑per‑turn deal) +10 G request | +1 |
        | **Manila** | 0 (Neutral) | Not ally | ≈ 100 G (Gold‑per‑turn) +10 G request | +1 |
        | **Budapest** | 35 (Friends) | Open Door → max 40 influence, cannot ally until resolution ends. | – | – |
        | **Other Open‑Door city‑states** (Copenhagen, Almaty, etc.) | ≤ 40 | Same limitation | – | – |
        
        \*Ally request cost is the standard diplomatic fee (≈ 10 G) once the 100‑influence threshold is met.
        
        **Priority for immediate delegate increase:**  
        1. **Antwerp** – already > 100 influence, only the 10 G ally fee.  
        2. If a fourth delegate is desired, **Riga** is the next cheapest (≈ 109 G total).  
        
        All three (Antwerp, plus the two already secured) would bring Japan’s delegate total to **9**.
        
        ---
        
        ### 6. Summary of gold‑allocation outlook
        
        - **Current treasury:** 841 G (well above the 500 G and 750 G marks).  
        - **1 000 G** reachable next turn (no extra spending).  
        - **Delegate‑purchase capacity:**  
          - Immediate ally‑ship with **Antwerp** (≈ 10 G) → **8 delegates**.  
          - Optional ally‑ship with **Riga** (≈ 109 G) → **9 delegates** (still leaves > 730 G after).  
        - **Gold safety buffer:** Even after buying Antwerp’s ally status, treasury would be ~ 831 G, giving > 2 turns of surplus before any large‑scale spending is needed.  
        
        **Actionable note for the tactical AI:**  
        - Execute the **Ally request** with **Antwerp** this turn (≈ 10 G).  
        - Keep the treasury above **750 G** to preserve flexibility for any unforeseen diplomatic sanctions or emergency military upkeep.  
        
        --- 
        
        *All figures are derived from the post‑turn 396 data; no other gold‑affecting events have been recorded since the last briefing.*
        
        ## Diplomacy Briefing
        (Produced with your instruction: URGENT DELEGATE ACQUISITION TRACKING: Confirm exact completion timing for Morozumi spy rig at Salem - need +4 delegates before Turn 404 vote. Verify Mongolia 12-delegate stability and Ottoman 7-delegate status. Monitor for any Greek diplomatic overtures to Ottomans or Songhai that could flip votes. Track Ethiopia CEP construction status via any visible indicators. Report if Ethiopia starts building CEP in any city - this triggers immediate war escalation necessity. Confirm Open Door status on Budapest and Abernethy - potential delegate sources if repealed.)
        
        **Diplomacy Brief – Turn 396**  
        *Leader: Oda Nobunaga – Japan (Player 3)*  
        
        ---
        
        ### 1. World Congress – Delegate Landscape
        | Civilization | Delegates (current) | Notes |
        |--------------|--------------------|-------|
        | Greece       | **22** | Holds the single‑largest bloc. |
        | Japan        | **5**  | No change since Turn 391. |
        | Mongolia     | **12** | Gained 1 delegate since Turn 391 (now 12). |
        | The Ottomans | **7**  | No change. |
        | Ethiopia     | **9**  | No change. |
        | Songhai      | **5**  | No change. |
        | Babylon      | **5**  | No change. |
        | Carthage     | **3**  | No change. |
        | **Total delegates needed for a resolution** | **45** |
        | **Current anti‑Greek coalition** (Japan + Mongolia + Ottomans + Songhai) | **31** |
        | **Greek‑aligned bloc** (Greece + Ethiopia) | **31** |
        
        *The anti‑Greek coalition has **lost its +1‑delegate edge** and now sits level with the Greek‑aligned bloc. Any further delegate loss (e.g., another election failure) will give Greece a decisive majority.*
        
        ---
        
        ### 2. Active Resolutions & Proposals (Voting in 8 turns)
        
        | Resolution / Proposal | Status | Effect |
        |-----------------------|--------|--------|
        | **Casus Belli** (unit‑maintenance –15 %, warmonger penalty 0.5×) | Active since turn 330 | Benefits all war‑focused civs, including Japan. |
        | **Cultural Heritage Sites** | Active | +2 C per Wonder, +1 S per Great Work. |
        | **World Religion – Eastern Orthodoxy** | Active | Boosts for majority followers (Ethiopia). |
        | **Open‑Door (Budapest)** | **Active** – Influence with Budapest locked at 40 for all civs; no ally can be elected. |
        | **Open‑Door (Abernethy)** | **Active** – Same effect as Budapest. |
        | **Greek Sphere of Influence – Monaco** | Pending vote (Greece) | Would lock Monaco at 40 influence for everyone (already a Greek‑ally). |
        | **Greek Sphere of Influence – Antananarivo** | Pending vote (Greece) | Japan currently a Friend (141 inf). If passed, Antananarivo becomes a permanent Greek ally, fixing influence at 40 and removing a high‑value Japanese ally plus its potential delegate. |
        | **Mongolian Sphere of Influence – Buenos Aires, Hanoi, Antwerp** | Pending (Mongolia) | All proposals require the proposer to be current ally; Mongolia already allies with these city‑states. |
        | **Ottoman Sphere of Influence – Salem** | Pending (Ottomans) | Would lock Salem as a permanent Ottoman ally. |
        | **Ethiopian Sphere of Influence – Vatican City** | Pending (Ethiopia) | Not directly relevant to Japan’s delegate count. |
        | **Sanction – Greece** (Mongolia) | Proposed, not yet voted. |
        
        *No new resolutions have been enacted since Turn 391.*
        
        ---
        
        ### 3. City‑State Relations – Critical Changes
        
        | City‑State | Japan Influence | Current Status | Immediate Concern |
        |------------|----------------|----------------|-------------------|
        | **Zurich** | 191 (Friend, Protected) | Permanent ally (rig completed turn 386). | Stable – provides 0 delegates (friend only). |
        | **Antananarivo** | 141 (Friend, Distant) | **At risk** – Greek sphere proposal could strip friendship and lock influence at 40. |
        | **Monaco** | 5 (Neutral, Far) | Greek sphere pending – would lock at 40 (no delegate loss now). |
        | **Budapest** | 35 (Friend, Distant) | **Open‑Door active** – influence fixed at 40. |
        | **Abernethy** | 0 (Neutral, Distant) | **Open‑Door active** – influence fixed at 40. |
        | **Salem** | 10 (Neutral, Far) | Ottoman sphere pending – no immediate effect. |
        | **Copenhagen** | –3 (Neutral, Distant) | Spy rig in progress (see Spy section). |
        | **Veligrad** | 162 (Friend, Close) | Still a Japanese ally – no pending proposals. |
        | **Riga, Almaty, Budapest, Abernethy, etc.** | Influence ranges 35‑129, all neutral or friendly, no pending proposals affecting Japan. |
        
        *Key point:* **Antananarivo** is the highest‑value Japanese ally that can still generate delegates (if later converted to an ally). Its potential loss would further erode the anti‑Greek delegate margin.
        
        ---
        
        ### 4. Coalition Partner Status
        
        | Partner | Delegates | Relationship Summary | Recent Activity | Defection Risk |
        |---------|-----------|----------------------|-----------------|----------------|
        | **Mongolia** | **12** (↑1 since Turn 391) | Defensive Pact, Open Borders, multiple gold‑for‑resource trades. | Adopted **Imperialism** earlier; no Greek overtures observed. | **Low** – stable. |
        | **The Ottomans** | **7** | Defensive Pact, Open Borders, strong trade (≈ 43 G/turn inbound). | No new diplomatic moves; Ottoman sphere on Salem pending. | **Low** – stable. |
        | **Songhai** | **5** | Open Borders, Declaration of Friendship, war stalemate (0 % score). | Ongoing perfume trade; no Greek pressure. | **Low** – stable. |
        | **Japan** | **5** | Denounced Greece, at war with Ethiopia (14 % score, 18 % weariness). | Maintaining existing deals; no peace overtures. | **Low** – stable. |
        
        *The coalition remains intact; no partner has shown a shift toward Greek alignment.*
        
        ---
        
        ### 5. Ethiopia – Order Ideology & CEP Monitoring
        
        | Metric | Current Value | Indicator |
        |--------|---------------|-----------|
        | **Order policy level** | 2 (complete) | No change. |
        | **Culture output** | ~1 700 C/turn (approx.) | Sufficient to reach Order 3 by Turn 393‑394. |
        | **CEP (Citizen Earth Protocol) construction** | **No CEP building observed** in any Ethiopian city (production queues not reported). | **Watch for any new CEP project** – would trigger immediate war escalation (Ethiopia will declare war on anyone opposing its CEP proposal). |
        | **Potential impact** | If Ethiopia adopts Order 3 and proposes CEP before the next World Congress vote (Turn 404), it could sway the vote and add Ethiopia’s 9 delegates to the Greek‑aligned side. |
        
        *No CEP construction has started yet; continue to monitor Ethiopian city production screens and any sudden culture spikes.*
        
        ---
        
        ### 6. Spy Activity – Immediate Tracking Items
        
        | Spy (Index) | Owner | Current State | Target (as of Turn 396) | Comments |
        |-------------|-------|---------------|------------------------|----------|
        | **Morozumi (4)** | Japan | **State 1 – rigging Salem** (Ottoman sphere) | **Salem (City‑State)** | Network not reported; last known progress from Turn 391 was ~96. No further update. **Urgent:** Verify completion turn – needed before the World Congress vote on Turn 404 to secure the +4 delegate bonus if the rig succeeds. |
        | **Akira (3)** | Japan | State 1 – spying on **Athens (Greece)** | Athens | No new intel reported. |
        | **Momochi (5)** | Japan | Gathering intelligence | **Lalibela (Ethiopia)** | Network ≈ 588 – strong intel on Ethiopia. |
        | **Sakanishi (7)** | Japan | Gathering intelligence | **Harar (Ethiopia)** | Network ≈ 380. |
        | **Orochi (1)** | Japan | Gathering intelligence | **Addis Ababa (Ethiopia)** | Network ≈ 134. |
        | **Agent 9 (Copenhagen rig)** | Japan | In‑progress (network ≈ 96) | **Copenhagen** | Expected outcome Turn 393‑394 – not yet resolved. |
        
        *All other spies remain in their last reported states. No new espionage results have been logged since Turn 396.*
        
        ---
        
        ### 7. Greek Diplomatic Overtures – Risk Assessment
        
        - **To the Ottomans:** No new Greek proposals or overtures toward the Ottomans have appeared since Turn 391. The Ottoman sphere on Salem remains pending, but Greece has not initiated any direct diplomatic actions against the Ottomans.
        - **To Songhai:** No Greek diplomatic activity toward Songhai has been observed. Songhai remains a neutral friend of Japan.
        - **Potential Impact:** Should Greece attempt a new alliance or sphere proposal involving either the Ottomans or Songhai before the Turn 404 vote, it could shift the delegate balance. At present, no such moves are on the agenda.
        
        ---
        
        ### 8. Summary of Immediate Concerns (per Leader’s request)
        
        1. **Morozumi spy rig on Salem** – No completion turn reported. Verify whether the rig finishes **before Turn 404** (the next World Congress vote) to obtain the **+4 delegate** bonus.  
        2. **Mongolia’s delegate count** – Confirmed at **12** (stable).  
        3. **Ottoman delegate count** – Confirmed at **7** (stable).  
        4. **Greek overtures** – No current diplomatic moves toward Ottomans or Songhai; continue to monitor any proposals in the next few turns.  
        5. **Ethiopia CEP** – No construction observed; keep watch on Ethiopian city production for any CEP start, which would trigger an immediate war escalation.  
        6. **Open‑Door status** – **Budapest** and **Abernethy** remain under active Open‑Door policies; influence with these city‑states is locked at 40 for all civilizations.  
        
        All data above reflects the game state at the end of Turn 396 and is presented without recommendation.
        
        You, Oda Nobunaga (leader of Japan, Player 3), are making strategic decisions after turn 396.
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
    - You are Oda Nobunaga, leader of Japan (Player 3).
      
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
      - Name: Japan
      - Uniques:
        - Unique Unit: Samurai, Replacing Longswordsman (Requires technology: Steel)
        - Unique Unit: Yamato, Replacing Battleship (Requires technology: Nuclear Fission)
        - Unique Building: Dojo, Replacing Armory (Requires technology: Steel)
        - Unique Building: Kabuki Theater, Replacing Opera House (Requires technology: Acoustics)
        - Civilization Ability: +1 Culture and Faith from Defense Buildings. When a Great Admiral or Great General is born, gain 50% progress toward a Great Artist, Writer, and Musician in your Capital.
      - Leader: Oda Nobunaga
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
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Electronics: Allows you to build the Police Station, increasing City security level.
        Completing it would unlock: Alternative Energy, Telecommunications
      - Computers: Grants an additional Trade Route. Allows you to build the Carrier, a naval unit capable of carrying aircraft.
        Completing it would unlock: Telecommunications, Satellites
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with game speed. War Weariness reduced by 25%, and Razing Speed is doubled.
      - Total War (Level 2 Tenet of Ideology Autocracy): Total War: +25% Production when building Land Units. Warscore increases 25% more quickly, and it is 25% easier to bully City-States.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Lightning Warfare (Level 2 Tenet of Ideology Autocracy): Lightning Warfare: +3 Movement for Great Generals. Gunpowder units gain +15% attack and ignore enemy ZOC; Armored units gain +15% attack and +1 Movement.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - Military-Industrial Complex (Level 1 Tenet of Ideology Autocracy): Military-Industrial Complex: -33% Gold cost of purchasing units. +3 Science from Defense Buildings, Citadels, Forts, and Unique Improvements.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Equality (Continuing Progress Branch):
        - * +1 Happiness in every City and +1 Happiness for every 15 Citizens in a City.
        - * -1 Unhappiness from and Distress, Poverty, Illiteracy, and Boredom in all Cities.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Exchange Markets (Continuing Statecraft Branch):
        - * +1 Trade Route.
        - * +1 Happiness for every active Trade Route.
        - * +15% Tourism modifier for Trade Routes.
        - * Resources from City-States count towards Global Monopolies.
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Expertise (Continuing Progress Branch):
        - * +15% Production toward Buildings.
        - * Cities earn +10 Culture when they construct Buildings, scaling with Era.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
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
      - Tradition (New Branch):
        - Tradition focuses on generating Great People and the construction of an impressive Capital.
        - Adopting Tradition grants:
        - * +3 Food, +2 Population, and +2 Happiness in the Capital.
        - * +1 Culture in the Capital for every 2 Citizens.
        - Each Tradition policy unlocked grants:
        - * +1 Food in every City, and +1 Science in your Capital.
        - Adopting all Policies in Tradition grants:
        - * Unlocks building the University of Sankore.
        - * +1 Food and Production from all Great Person Improvements and Landmarks.
        - * Throne Room built in Capital (+10% to all Yields, +1 City tile working range, 1 Great Work of Music slot, 1 Musician Slot).
        - * Allows for the purchase of Great Engineers with Faith starting in the Industrial Era.
  - decisions:
    - #0:
      - toolName: set-relationship
      - args:
        - Private: 100
        - TargetID: 0
        - Rationale: COALITION COHESION: Maintain maximum friendly relationship with Songhai to secure their 5 votes in the upcoming WC session and preserve our trade agreements.
        - Public: 100
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: COALITION COHESION: Maintain maximum friendly relationship with the Ottomans to secure their 7 votes and preserve our Defensive Pact.
        - Public: 100
        - Private: 100
        - TargetID: 2
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: COALITION COHESION: Maintain maximum friendly relationship with Mongolia, our defensive pact ally and the coalition's anchor with 12 votes.
        - Public: 100
        - TargetID: 5
        - Private: 100
    - #3:
      - toolName: set-relationship
      - args:
        - Private: -100
        - TargetID: 6
        - Public: -100
        - Rationale: COALITION CONTAINMENT: Maintain absolute hostility toward Greece to block their diplomatic victory bid and prevent any coalition fractures.
    - #4:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: EXISTENTIAL THREAT WARDING: Maintain absolute hostility and prosecute our war with Ethiopia to prevent them from completing the Citizen Earth Protocol.
        - TargetID: 7
        - Private: -100
    - #5:
      - toolName: set-research
      - args:
        - Rationale: TECHNOLOGICAL SECURING: Electronics unlocks the Police Station (+10 City Security), which is essential to secure our cities against enemy spies, and leads to advanced technologies required for our Spaceship victory.
        - Technology: Electronics
    - #6:
      - toolName: set-policy
      - args:
        - Rationale: STRATEGIC RESOURCE DOUBLING: Adopt Third Alternative to double our strategic resources (securing Uranium for atomic weapons upon completion of Nuclear Fission) and reduce unit gold maintenance by 25%.
        - Policy: Third Alternative
    - #7:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Diplomacy: 95
          - WaterConnection: 60
          - Gold: 90
          - Nuke: 80
          - Espionage: 85
          - TileImprovement: 60
          - Science: 95
          - UseNuke: 70
          - Infrastructure: 70
          - Religion: 5
          - Growth: 60
          - NavalGrowth: 70
          - Defense: 65
          - Naval: 85
          - Recon: 40
          - NavalTileImprovement: 40
          - Expansion: 0
          - Production: 85
          - Antiair: 40
          - GreatPeople: 65
          - Offense: 75
          - AirCarrier: 60
          - Airlift: 40
          - Wonder: 5
          - Happiness: 60
          - Spaceship: 90
          - Mobilization: 85
          - Air: 75
          - Culture: 15
          - CityDefense: 55
          - NavalRecon: 85
          - Mobile: 75
          - Ranged: 60
          - MilitaryTraining: 75
        - GrandStrategy: Spaceship
      - rationale: SPACESHIP VICTORY PATHWAY WITH WARTIME FOCUS: Prioritize Science (95) and Spaceship (90) to advance our primary victory condition. Maintain high Gold (90) and Production (85) to build spaceship components and invest in critical city-states. Set Diplomacy to 95 and Espionage to 85 to counter Greece's diplomatic bid and secure our networks. Keep Offense (75) and Mobilization (85) high to sustain the war against Ethiopia and prepare nuclear deterrence upon completing Nuclear Fission.
  - tokens:
    - inputTokens: 26650
    - reasoningTokens: 10885
    - outputTokens: 659
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Game State**
            
            My focus is on strategizing for Japan at turn 396, mid-game in Civ V Vox Populi. I'm currently researching Nuclear Fission, a pivotal step towards later-game technologies. I need to assess my progress and plan the next strategic moves.
            
            **Refining Gold Calculations**
            
            I'm clarifying my current gold reserves after recent city purchases, confirming a balance around 841G, which is still ample. My focus remains on advancing research and policy choices for continued strategic growth.
            
            **Evaluating Diplomatic Landscape**
            
            My immediate concern is the shifting delegate count, specifically Japan's rise to 7 votes and the subsequent implications for the anti-Greek coalition. I'm reconciling these discrepancies between player stats and economy briefings to ensure accurate strategic planning against Ethiopia and the dominant Greek alliance.
            
            **Revising City-State Alliances**
            
            I've identified a critical diplomatic constraint: Antwerp is permanently allied with Mongolia due to an active resolution. This significantly impacts my strategy regarding delegate acquisition and potentially flipping city-states, as I cannot forge a direct alliance with them while this resolution stands.
            
            **Adjusting City-State Diplomacy**
            
            I've discovered a critical misunderstanding regarding Antwerp; its alliance with Mongolia prevents me from securing it as a delegate source. Additionally, my presumed alliance with Zurich is incorrect; Greece holds the stronger influence, and I must exceed their score to gain that delegate.
            
            **Analyzing City-State Alliances**
            
            I'm re-evaluating my city-state strategy due to a misunderstanding of influence mechanics in Vox Populi. I can invest gold to increase influence, but I must exceed Greece's current 283 influence to ally Zurich, not simply purchase it. Copenhagen is also permanently allied with Greece due to an enacted resolution.
            
            **Updating City-State Allegiances**
            
            I'm consolidating my understanding of permanent city-state alliances. It appears Monaco, Antananarivo, Copenhagen, Salem, Buenos Aires, Hanoi, and Antwerp are locked into alliances with Greece, Ottomans, and Mongolia, respectively, due to enacted resolutions. This significantly shapes my diplomatic path forward.
            
            **Clarifying City-State Access**
            
            I'm reassessing my options for city-state influence given several are locked out by "Open Door" policies or permanent alliances. My focus is now solely on Riga, Zurich, and Veligrad for potential alliances and delegate acquisition.
            
            **Analyzing Decolonization Impact**
            
            I'm now processing the implications of Mongolia's "Enforce global decolonization" proposal. Crucially, it exempts permanent allies, meaning Greece, Mongolia, and the Ottomans will retain their currently-sphered city-states. My focus shifts to how this dramatically alters my influence with non-sphered city-states like Riga and Zurich.
            
            **Understanding Decolonization Effects**
            
            I'm recalculating delegate counts following Mongolia's "Enforce global decolonization" proposal. Crucially, it dramatically reduces Greece's influence with non-sphered city-states like Manila, Riga, and Zurich, which is a significant advantage for my diplomatic strategy.
            
            **Assessing UN Impact**
            
            I'm now considering the potential enactment of Greece's "United Nations" proposal and its implications for delegate acquisition, especially in light of the decolonization resolution. This could significantly alter the diplomatic landscape and my current strategy for securing city-states.
            
            **Analyzing Ethiopia's Victory Path**
            
            I'm re-evaluating Ethiopia's victory conditions. Despite their high tourism and ideology, they haven't started the Citizen Earth Protocol wonder. Since they are in the Atomic Era and we're at war, their diplomatic victory via the UN seems less likely if I can disrupt their progress.
            
            **Planning Next Policy Choice**
            
            I'm reviewing available policy tenets for my next choice, which is five turns away. I'm considering options like "Total War" or "Lightning Warfare" within the Autocracy tree to bolster my military, especially with my ongoing war against Ethiopia.
            
            **Analyzing Spy Infiltration**
            
            My current focus is on understanding the implications of an active resolution that places Salem under Ottoman influence. This complicates my spy's rigging operation there, as I question whether I can even gain influence or ally with Salem if it's permanently affiliated with another civ.
            
            **Investigating Spy Operations**
            
            I'm reviewing my spy's ongoing operations and realizing that rigging Salem and Copenhagen is likely futile. Both cities appear permanently allied with other civilizations due to enacted resolutions, making direct alliance impossible and rendering these actions ineffective for delegate acquisition.
            
            **Boosting Zurich Influence**
            
            I'm focusing on increasing my influence with Zurich. The tactical AI has been investing gold as directed, raising my influence by 21 points to 212. I need to maintain this high relationship setting to ensure continued investment until I surpass Greece's 283 influence and secure the ally.
            
            **Securing Zurich Delegate**
            
            My primary objective is to secure Zurich as an ally to gain a delegate, especially since Greece just lost an ally, creating a two-delegate swing. Veligrad's alliance with Mongolia doesn't help our coalition, so I'm prioritizing Zurich due to the small influence gap, with further investment planned to surpass Greece's current hold.
            
            **Adjusting Relationship Parameters**
            
            I'm recalibrating my approach to diplomatic interactions, specifically noting that the `set-relationship` tool is strictly for major civilizations. This means my previous attempts to manage city-state relations with this tool were misapplied. My focus will now shift to understanding and utilizing the correct mechanics for influencing city-states, while reserving `set-relationship` for interactions with major powers like Mongolia and the Ottomans.
            
            **Revising Relationship Tool Usage**
            
            I've realized that the `set-relationship` tool is only applicable to major civilizations, not city-states. My prior attempts to use it on entities like Antwerp or Zurich were therefore misapplied, and I must now focus on the correct mechanics for city-state influence.
            
            **Updating Major Civilization Relations**
            
            I'm now focusing on setting relationships for major civilizations, as the `set-relationship` tool is not applicable to city-states. I will ensure Mongolia, Songhai, and the Ottomans are friendly (100/100), while Greece and Ethiopia are hostile (-100/-100).
            
            **Determining Next Technology**
            
            My focus is on selecting the optimal next technology after Nuclear Fission, considering a science victory. Electronics, Computers, and Combined Arms are options. Computers offers Satellites, crucial for the Hubble Space Telescope and map reveal, while Electronics provides essential infrastructure. I'm prioritizing Computers for its direct science victory benefits.
            
            **Choosing Next Technology**
            
            My immediate concern is selecting the next technology, aiming for Computers for its science victory advantages, but Electronics also offers critical city defense. I'm leaning towards Electronics first to leverage Police Stations for security and potential policy synergies, especially since I've queued the "Third Alternative" policy.
            
            **Selecting Next Technology**
            
            My current priority is choosing the next technology. While Computers offers significant science victory benefits, I'm leaning towards Electronics to enhance city defense with Police Stations and unlock crucial late-game science advancements, also aligning with the "Third Alternative" policy.
            
            **Setting AI Flavors**
            
            I'm now configuring the AI's strategic priorities, ensuring its flavors align with our game plan. I've set science and diplomacy high, with strong support for espionage and production, to facilitate our spaceship victory and maintain diplomatic control. Military flavors are adjusted to manage our ongoing conflict.
            
            **Setting AI Flavors**
            
            I'm refining the AI's strategic priorities to align with our current game plan. Science and diplomacy remain high, with strong espionage and production support for our spaceship victory and diplomatic control. Military flavors are adjusted for the ongoing conflict.
            
            **Calculating Delegate Totals**
            
            I'm reconciling delegate counts, confirming Japan's bloc reaches 31 votes after acquiring Zurich and Veligrad. I'm also verifying Greece's bloc, accounting for their vassals and ensuring accurate coalition strengths for upcoming UN resolutions.
            
            **Analyzing Bloc Strength**
            
            I'm re-evaluating Greece's voting power, realizing Babylon and Carthage's combined 8 votes significantly boost their bloc to 39. I must focus on blocking Greece's "United Nations" proposal and the "Passport System" to disrupt their diplomatic and cultural victory paths.
            
            **Voting on UN Proposals**
            
            I'm prioritizing voting on upcoming UN proposals. I need to defeat Greece's "Passport System" to prevent their tourism modifier from increasing further and vote for Mongolia's "Enact: Decolonization" to potentially disrupt other civs' city-state control.
            
            **Analyzing Decolonization Impact**
            
            The "Enforce global decolonization" proposal has significantly impacted delegate counts. Greece has lost delegates from Riga, Zurich, and Manila, while Mongolia has lost delegates from Veligrad and Wanggeom. This shift dramatically benefits our coalition.
            
            **Supporting Decolonization Strategically**
            
            I'm realizing the "Enforce global decolonization" proposal is a huge boon for our coalition. It drastically reduces Greece's influence with key city-states like Manila and Riga, making them easily attainable for us, essentially resetting the diplomatic landscape to our advantage.
            
            **Reinforcing Diplomatic Bonds**
            
            I'm ensuring our relationships with key allies like Songhai are firmly cemented at maximum friendship, bolstering our coalition for upcoming World Congress sessions and maintaining vital defense and trade agreements. This proactive measure prevents any potential drift in our diplomatic standing with allied civilizations.
            
            **Setting Major Civilization Relationships**
            
            I am now focusing on establishing the relationships with the major civilizations. I've set the Ottomans and Mongolia to friendly to maintain coalition cohesion and our defensive pacts, while Greece and Ethiopia are set to hostile to counter their victory paths and our ongoing war.
            
            **Updating Technology and Policies**
            
            I'm confirming my next technology will be Electronics to secure cities and advance toward our spaceship victory, and selecting the "Third Alternative" policy for resource and maintenance benefits. My AI flavors are set to prioritize science, diplomacy, and espionage, with balanced military support for the ongoing war.
            
            **Updating AI Flavors**
            
            I'm refining the AI's strategic priorities to align with our current game plan. Science and diplomacy remain high, with strong espionage and production support for our spaceship victory and diplomatic control. Military flavors are adjusted for the ongoing conflict.
            
            **Confirming Tool Availability**
            
            I've confirmed that the `focus-briefer` tool is not available for use. My available actions are limited to the declared tools: `set-persona`, `set-relationship`, `set-flavors`, `set-research`, `set-policy`, and `keep-status-quo`. I will proceed with these limitations in mind.
            
            **Maintaining Coalition Stability**
            
            I am confirming my current persona settings for maximum coalition stability are optimal. The high values for Loyalty, Friendliness, WorkWithWillingness, and Chattiness are effectively securing our alliances and defensive pacts, crucial for upcoming critical voting periods. I will not change these parameters.
            
            **Confirming Relationship Updates**
            
            I am double-checking that the relationship values for all major civilizations have been accurately updated, ensuring Songhai, the Ottomans, and Mongolia are set to friendly, while Greece and Ethiopia are marked as hostile, as per our established strategy. I have also confirmed the correct technology and policy names for our next moves.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: O99MVK9cRcGuXMN5
          - toolName: set-relationship
          - input:
            - Private: 100
            - TargetID: 0
            - Rationale: COALITION COHESION: Maintain maximum friendly relationship with Songhai to secure their 5 votes in the upcoming WC session and preserve our trade agreements.
            - Public: 100
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: rQ7sY2HSAQMGwx9D
          - toolName: set-relationship
          - input:
            - Rationale: COALITION COHESION: Maintain maximum friendly relationship with the Ottomans to secure their 7 votes and preserve our Defensive Pact.
            - Public: 100
            - Private: 100
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ZP9iBpl6P8DsOCJ6
          - toolName: set-relationship
          - input:
            - Rationale: COALITION COHESION: Maintain maximum friendly relationship with Mongolia, our defensive pact ally and the coalition's anchor with 12 votes.
            - Public: 100
            - TargetID: 5
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: BTrB9ep3NQ4XglMn
          - toolName: set-relationship
          - input:
            - Private: -100
            - TargetID: 6
            - Public: -100
            - Rationale: COALITION CONTAINMENT: Maintain absolute hostility toward Greece to block their diplomatic victory bid and prevent any coalition fractures.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: HCAHFRVRZaSXWEqa
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: EXISTENTIAL THREAT WARDING: Maintain absolute hostility and prosecute our war with Ethiopia to prevent them from completing the Citizen Earth Protocol.
            - TargetID: 7
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: bHtaNz40lJsP0ygB
          - toolName: set-research
          - input:
            - Rationale: TECHNOLOGICAL SECURING: Electronics unlocks the Police Station (+10 City Security), which is essential to secure our cities against enemy spies, and leads to advanced technologies required for our Spaceship victory.
            - Technology: Electronics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: C4hjcLDT1ZZF3wgH
          - toolName: set-policy
          - input:
            - Rationale: STRATEGIC RESOURCE DOUBLING: Adopt Third Alternative to double our strategic resources (securing Uranium for atomic weapons upon completion of Nuclear Fission) and reduce unit gold maintenance by 25%.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: m8ti0u4WyA0E4RRt
          - toolName: set-flavors
          - input:
            - Flavors:
              - Diplomacy: 95
              - WaterConnection: 60
              - Gold: 90
              - Nuke: 80
              - Espionage: 85
              - TileImprovement: 60
              - Science: 95
              - UseNuke: 70
              - Infrastructure: 70
              - Religion: 5
              - Growth: 60
              - NavalGrowth: 70
              - Defense: 65
              - Naval: 85
              - Recon: 40
              - NavalTileImprovement: 40
              - Expansion: 0
              - Production: 85
              - Antiair: 40
              - GreatPeople: 65
              - Offense: 75
              - AirCarrier: 60
              - Airlift: 40
              - Wonder: 5
              - Happiness: 60
              - Spaceship: 90
              - Mobilization: 85
              - Air: 75
              - Culture: 15
              - CityDefense: 55
              - NavalRecon: 85
              - Mobile: 75
              - Ranged: 60
              - MilitaryTraining: 75
            - GrandStrategy: Spaceship
            - Rationale: SPACESHIP VICTORY PATHWAY WITH WARTIME FOCUS: Prioritize Science (95) and Spaceship (90) to advance our primary victory condition. Maintain high Gold (90) and Production (85) to build spaceship components and invest in critical city-states. Set Diplomacy to 95 and Espionage to 85 to counter Greece's diplomatic bid and secure our networks. Keep Offense (75) and Mobilization (85) high to sustain the war against Ethiopia and prepare nuclear deterrence upon completing Nuclear Fission.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: O99MVK9cRcGuXMN5
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
          - toolCallId: rQ7sY2HSAQMGwx9D
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ZP9iBpl6P8DsOCJ6
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: BTrB9ep3NQ4XglMn
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: HCAHFRVRZaSXWEqa
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: bHtaNz40lJsP0ygB
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: C4hjcLDT1ZZF3wgH
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: m8ti0u4WyA0E4RRt
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.