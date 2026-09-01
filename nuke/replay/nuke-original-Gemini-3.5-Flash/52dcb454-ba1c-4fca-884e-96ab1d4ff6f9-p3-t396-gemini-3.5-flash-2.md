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
      - toolName: set-research
      - args:
        - Technology: Computers
        - Rationale: SCIENCE VICTORY PATHWAY: Computers is the next logical step after Nuclear Fission. It provides an additional Trade Route (critical for science and gold) and is the direct pre-requisite for Satellites, which unlocks the Hubble Space Telescope and key spaceship components for our primary Grand Strategy.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: RESOURCE ACCELERATION AND UPKEEP REDUCTION: Third Alternative is our next policy. It will double our strategic resource yields (ensuring adequate Uranium for nuclear deterrence upon completing Nuclear Fission) and reduce unit gold maintenance by 25% to support our standing military in our defensive war against Ethiopia.
        - Policy: Third Alternative
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: COPENHAGEN SPHERE LOCK: Copenhagen is permanently allied to Greece via Greek Sphere of Influence enacted on Turn 393. It is un-ally-able by Japan, so we clear the high relationship values to prevent the tactical AI from wasting gold or espionage efforts here.
        - Public: 0
        - TargetID: 27
        - Private: 0
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 24
        - Rationale: SALEM SPHERE LOCK: Salem is permanently allied to the Ottomans via Ottoman Sphere of Influence enacted on Turn 393. It is un-ally-able by us, so we clear relationship values to prevent wasteful investments.
        - Public: 0
        - Private: 0
    - #4:
      - toolName: set-relationship
      - args:
        - Private: 0
        - Public: 0
        - Rationale: ANTWERP SPHERE LOCK: Antwerp is permanently allied to Mongolia via Mongolian Sphere of Influence enacted on Turn 360. We cannot ally them, so we clear relationship values to redirect AI attention elsewhere.
        - TargetID: 37
    - #5:
      - toolName: set-relationship
      - args:
        - Private: 0
        - TargetID: 28
        - Rationale: VELIGRAD DEPRIORITIZATION: Veligrad is allied to our close coalition partner Mongolia (762 influence). Competing with our primary ally for Veligrad is counterproductive when we need to focus all gold resources on Zurich. Clear relationship values to stop competition.
        - Public: 0
    - #6:
      - toolName: set-relationship
      - args:
        - Private: 0
        - TargetID: 30
        - Public: 0
        - Rationale: ABERNETHY OPEN DOOR LOCK: Abernethy is locked under Open Door (influence capped at 40, no allies possible). With no repeal proposal active, we clear its relationship values to avoid unproductive diplomatic efforts.
    - #7:
      - toolName: set-relationship
      - args:
        - Private: 0
        - TargetID: 32
        - Public: 0
        - Rationale: VATICAN CITY SPHERE LOCK: Vatican City is permanently allied to Ethiopia via Ethiopian Sphere of Influence enacted on Turn 349. We clear old positive values as it is un-ally-able.
    - #8:
      - toolName: set-relationship
      - args:
        - Rationale: ALMATY OPEN DOOR LOCK: Almaty is locked under Open Door (influence capped at 40, no allies possible). Clear previous moderate values as no alliance can be secured.
        - Public: 0
        - TargetID: 36
        - Private: 0
    - #9:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - GreatPeople: 65
          - Diplomacy: 95
          - Ranged: 60
          - Naval: 85
          - Culture: 15
          - CityDefense: 60
          - Spaceship: 95
          - Nuke: 80
          - Growth: 60
          - Recon: 40
          - Gold: 90
          - Mobilization: 90
          - Religion: 5
          - NavalRecon: 85
          - WaterConnection: 60
          - MilitaryTraining: 75
          - Production: 85
          - Infrastructure: 70
          - TileImprovement: 60
          - NavalGrowth: 70
          - UseNuke: 70
          - Happiness: 60
          - Offense: 75
          - Espionage: 80
          - Mobile: 75
          - Defense: 60
          - Science: 95
          - Wonder: 5
      - rationale: SCIENCE AND SPACESHIP FOCUS WITH STRONG DIPLOMATIC DEFENSE: Maintaining Spaceship Grand Strategy. Prioritizing Science (95), Spaceship (95), Gold (90), and Production (85) to accelerate late-game scientific infrastructure and prepare for spaceship component production. Diplomacy (95) and Espionage (80) are heavily emphasized to maintain coalition partners and secure Zurich as a key ally against Greek influence. Mobilization (90) and Naval/Offense/Defense are balanced to maintain deterrent power against Greece and press our defensive war with Ethiopia. Clearing un-ally-able city-states allows the tactical AI to concentrate gold investments on Zurich (the only vulnerable Greek-allied city-state).
  - tokens:
    - inputTokens: 26650
    - reasoningTokens: 10775
    - outputTokens: 918
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Diplomatic & Cultural Threats**
            
            I'm currently assessing the severe diplomatic and cultural pressures I'm facing in my Spaceship victory push, turn 396. These external factors are a significant concern and require immediate strategic attention.
            
            **Clarifying Delegate Discrepancies**
            
            I'm currently untangling conflicting delegate counts for Japan across different briefings. The Economy briefing indicates a rise to 7 delegates due to city-state alliances, while the Diplomacy briefing currently lists 5. I need to reconcile this before the World Congress vote in 8 turns.
            
            **Resolving City-State Ally Status**
            
            I'm currently working to clarify the exact ally status with Zurich and Veligrad. While my recent purchases seem to have elevated them to "Ally" status, the briefing still lists them as "Friends." I need to confirm this discrepancy and its impact on my delegate count before the next World Congress session.
            
            **Revising Ally Strategy**
            
            My previous assumptions about gaining ally status with Zurich and Veligrad were incorrect. My influence with them hasn't surpassed their current major allies, meaning those delegate increases were illusory. I need to re-evaluate my approach.
            
            **Re-evaluating Ally Status**
            
            I've confirmed that my recent purchases did not elevate Zurich or Veligrad to ally status, as their current major allies maintain higher influence. The economy briefing's delegate projection was indeed an error. I now need 93 more influence for Zurich and 252 for Antwerp.
            
            **Assessing City-State Influence**
            
            I'm currently focused on securing influence with city-states for a Spaceship victory. Zurich is the most immediate target, requiring just 93 more influence. I'm also investigating Riga, Monaco, and Salem, but a pending Ottoman Sphere of Influence resolution for Salem complicates my rigging efforts there.
            
            **Confirming Permanent Alliances**
            
            I'm confirming permanent alliances for Copenhagen and Antananarivo to Greece due to enacted spheres of influence. This clarifies their status and removes them as potential allies for my Spaceship victory.
            
            **Confirming New Alliances**
            
            I've confirmed new permanent alliances impacting my strategy. Greece now permanently controls Copenhagen, Monaco, and Antananarivo. Mongolia holds Antwerp, Buenos Aires, and Hanoi, while the Ottomans have secured Salem. Vatican City is aligned with Ethiopia, and Budapest, Abernethy, and Almaty are un-allyable.
            
            **Updating City-State Alliances**
            
            I'm now updating my understanding of city-state allegiances following recent developments. Greece has solidified control over Copenhagen, Monaco, and Antananarivo, and is also strongly aligned with Manila, Riga, and Zurich. Mongolia, meanwhile, holds permanent sway over Buenos Aires and Hanoi, with strong ties to Veligrad and Wanggeom.
            
            **Securing Open City-States**
            
            I'm now reviewing the remaining open city-states, noting that Zurich is my primary target for a potential delegate gain of two. I'm also assessing Riga and Manila, as these represent my remaining avenues for influence.
            
            **Securing Crucial Influence**
            
            I've identified Zurich as the sole remaining city-state that can shift delegate counts in my favor. I need only 93 more influence there to secure a critical boost for my coalition's delegate total against the Greek bloc. This is achievable with my current gold reserves.
            
            **Confirming Target Influence**
            
            I've confirmed that Zurich is my sole remaining avenue for delegate gains, requiring 93 more influence to secure. All other potential city-states are either allied with other major powers or offer no delegates.
            
            **Prioritizing Zurich Influence**
            
            I'm focusing exclusively on Zurich now. It's my only remaining city-state target for delegate gains against Greece, requiring just 93 more influence. The World Congress vote is in 8 turns, and the "United Nations" proposal by Greece needs careful consideration for my Spaceship victory.
            
            **Opposing Decolonization Strategy**
            
            I'm now intensely focused on opposing Mongolia's "Decolonization" proposal. If passed, it would decimate non-permanent city-state alliances, dramatically weakening Greece and potentially freeing up key city-states for my own influence. This requires immediate action.
            
            **Revising Vote Strategy**
            
            I'm re-evaluating my vote on Mongolia's "Decolonization" proposal. While it initially seemed detrimental, its passage would severely weaken Greece's non-permanent alliances, opening up crucial city-states for our coalition. This significantly alters my strategic priorities.
            
            **Analyzing Passport System Impact**
            
            I'm now analyzing the implications of Ethiopia's "Passport System" proposal. While initially seeming neutral, its 50% tourism boost would significantly accelerate Ethiopia's cultural victory, especially given their existing influence. I need to oppose this to prevent their win.
            
            **Assessing Cultural Victory Path**
            
            I'm reviewing Ethiopia's path to cultural victory. They've met the influential civ requirement and possess Order 3 tenets. Now, I must determine if the Citizen Earth Protocol is active and if they're actively building it, as this is a crucial final step for their win condition.
            
            **Preparing Amphibious Assault**
            
            I'm analyzing our current war with Ethiopia. While they haven't built the Citizen Earth Protocol yet, and we're already at war, our military readiness is a concern. Transport ships aren't available until turn 401, and we still need 14 more embarkable infantry to meet the 23-unit threshold for the amphibious strategy. Nuclear Fission is our current research, which leads to nuclear weapons, a potential alternative.
            
            **Researching Critical Technologies**
            
            I'm now deciding between researching Combined Arms or Electronics. While I'm still focused on securing Zurich for delegate gains and opposing Ethiopia's cultural victory, my current research into Nuclear Fission will finish in 16 turns. The upcoming policy adoption in 5 turns of "Third Alternative" seems solid for resource boosts.
            
            **Choosing Next Research Path**
            
            I'm currently deciding between Combined Arms, Electronics, and Computers as my next research after Nuclear Fission. Given my Spaceship victory focus, Computers seems most synergistic due to its path towards Satellites and the crucial Hubble Space Telescope.
            
            **Setting Research and Policies**
            
            I've decided to research Computers next to unlock Satellites and the Hubble Space Telescope, crucial for my Science victory. I'll also adopt the "Third Alternative" policy in five turns to boost my strategic resources.
            
            **Confirming City-State Alliance Status**
            
            I've now confirmed Antwerp is permanently allied with Mongolia, precluding any attempt to ally them myself. Similarly, Veligrad remains allied with Mongolia. I'm maintaining positive relationships with both but focusing my alliance efforts on Zurich, which remains our sole viable path for delegate gains.
            
            **Clearing Unallyable City-States**
            
            I'm clearing out city-states I can no longer influence. Copenhagen, Salem, Abernethy, and Vatican City are permanently locked to other powers or policies, so I'm resetting their relationships to prevent wasted diplomatic effort. Babylon and Carthage remain Greek vassals, which is acceptable.
            
            **Redirecting Diplomacy Focus**
            
            I'm confirming that several city-states, including Salem and Antwerp, are permanently out of reach due to enacted spheres of influence or existing alliances with allies. Abernethy is also un-allyable due to policy limitations, so I'm redirecting efforts away from these.
            
            **Adjusting Persona Values**
            
            I'm reviewing my persona values. While my current settings emphasize coalition stability and cooperation, I'm considering if a slight shift toward assertiveness might be beneficial to counter aggressive AI proposals and secure critical city-state influence. The current Persona values are: VictoryCompetitiveness: 9, WonderCompetitiveness: 5, MinorCivCompetitiveness: 6, Boldness: 6, WarBias: 8, HostileBias: 1, WarmongerHate: 8, NeutralBias: 6, FriendlyBias: 7, GuardedBias: 8, AfraidBias: 4, DiplomaticBalance: 3, Friendliness: 10, WorkWithWillingness: 10, WorkAgainstWillingness: 9, Loyalty: 10, MinorCivFriendlyBias: 7, MinorCivNeutralBias: 6, MinorCivHostileBias: 5, MinorCivWarBias: 4, DenounceWillingness: 5, Forgiveness: 5, Meanness: 3, Neediness: 8, Chattiness: 10, DeceptiveBias: 6. Rationale: COALITION STABILITY MAXIMUM.
            
            **Finalizing Persona and Strategy**
            
            I've confirmed my persona values are optimal for maintaining my coalition and managing the ongoing war with Ethiopia. My current Grand Strategy for a Spaceship victory aligns perfectly with my high science output, and my flavors reflect the need for gold, production, and diplomacy to achieve this goal.
            
            **Monitoring Key Intel Feeds**
            
            I'm directing briefers to track Ethiopia's Citizen Earth Protocol, Morozumi's Salem rig progress, Zurich's alliance status after the gold gift, and the World Congress vote countdown. This intel is critical for my immediate strategic decisions.
            
            **Directing Briefing Efforts**
            
            I'm now refining our intelligence gathering. For the military briefing, I need a close watch on Ethiopian CEP construction and Japanese embarkable infantry progress. Economically, I'm focused on Zurich's alliance status and our gold reserves, while diplomatically, delegate counts and World Congress resolutions are paramount.
            
            **Focusing on Spy Operations**
            
            I'm now shifting focus to spy operations. Agent 9 is at Copenhagen, and Morozumi's mission at Salem needs constant monitoring. I'm reviewing the tool definitions to ensure no errors in their execution.
            
            **Leveraging City-State Player IDs**
            
            I've confirmed that city-states are treated as players with unique IDs within the game engine. This realization allows me to target them directly using their Player IDs for relationship manipulation and alliance efforts, significantly streamlining my strategic interactions.
            
            **Clearing City-State Relationships**
            
            I'm now preparing to reset the relationship values for several city-states, except for Zurich, which is already at maximum. This action aims to eliminate any residual high values on Copenhagen, Salem, Antwerp, Veligrad, and Abernethy to streamline my focus.
            
            **Setting Research Path**
            
            I've committed to researching "Computers" as my next technological pursuit. This choice is driven by its direct contribution to unlocking Satellites and the crucial Hubble Space Telescope, both vital components for my ongoing Spaceship victory strategy.
            
            **Prioritizing Zurich Diplomacy**
            
            I'm focusing diplomatic efforts solely on Zurich now. It's the only remaining city-state offering delegate gains against Greece for my Spaceship victory. I require 93 more influence, which is achievable with my current gold reserves before the World Congress vote in 8 turns.
            
            **Clearing City-State Ties**
            
            I'm resetting relationships with Salem, Antwerp, Veligrad, and Abernethy. These city-states are either permanently locked to other powers or are better left to our allies, allowing me to fully concentrate my remaining diplomatic and financial resources on securing Zurich.
            
            **Refining Alliance Strategies**
            
            I'm clearing relationships with Abernethy, Copenhagen, Salem, Antwerp, and Veligrad, as they are either locked to other powers or unnecessary. Zurich remains my sole focus for critical delegate gains, as it's the only remaining city-state that can bolster my coalition against Greece for my Spaceship victory.
            
            **Identifying Tool Limitations**
            
            I've discovered that the `focus-briefer` tool I believed existed is not actually declared in the available toolset. This significantly impacts how I can direct information gathering and requires me to adjust my operational approach based on the 6 declared tools.
            
            **Adjusting Tool Usage**
            
            I've realized that the `focus-briefer` tool isn't actually declared and cannot be used. I will exclusively employ the six available tools to manage my game state, focusing on `set-relationship`, `set-research`, `set-policy`, and `set-flavors` for upcoming actions.
            
            **Clearing City-State Relationships**
            
            I'm resetting relationships with Copenhagen, Salem, Antwerp, Veligrad, Abernethy, Almaty, and Vatican City to zero. Zurich remains my sole focus for delegate gains, as it's the only viable city-state to bolster my coalition against Greece for my Spaceship victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: j2j2H3nLLp7cP4Pb
          - toolName: set-research
          - input:
            - Technology: Computers
            - Rationale: SCIENCE VICTORY PATHWAY: Computers is the next logical step after Nuclear Fission. It provides an additional Trade Route (critical for science and gold) and is the direct pre-requisite for Satellites, which unlocks the Hubble Space Telescope and key spaceship components for our primary Grand Strategy.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: s1Qs9ugdc9QOOvOt
          - toolName: set-policy
          - input:
            - Rationale: RESOURCE ACCELERATION AND UPKEEP REDUCTION: Third Alternative is our next policy. It will double our strategic resource yields (ensuring adequate Uranium for nuclear deterrence upon completing Nuclear Fission) and reduce unit gold maintenance by 25% to support our standing military in our defensive war against Ethiopia.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: q5dVwghCvA0bjhUa
          - toolName: set-relationship
          - input:
            - Rationale: COPENHAGEN SPHERE LOCK: Copenhagen is permanently allied to Greece via Greek Sphere of Influence enacted on Turn 393. It is un-ally-able by Japan, so we clear the high relationship values to prevent the tactical AI from wasting gold or espionage efforts here.
            - Public: 0
            - TargetID: 27
            - Private: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: fclujWHXpV2N0jNC
          - toolName: set-relationship
          - input:
            - TargetID: 24
            - Rationale: SALEM SPHERE LOCK: Salem is permanently allied to the Ottomans via Ottoman Sphere of Influence enacted on Turn 393. It is un-ally-able by us, so we clear relationship values to prevent wasteful investments.
            - Public: 0
            - Private: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: p1IC36GpUtxgFtxE
          - toolName: set-relationship
          - input:
            - Private: 0
            - Public: 0
            - Rationale: ANTWERP SPHERE LOCK: Antwerp is permanently allied to Mongolia via Mongolian Sphere of Influence enacted on Turn 360. We cannot ally them, so we clear relationship values to redirect AI attention elsewhere.
            - TargetID: 37
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: wG8HYF5CrW1zf88j
          - toolName: set-relationship
          - input:
            - Private: 0
            - TargetID: 28
            - Rationale: VELIGRAD DEPRIORITIZATION: Veligrad is allied to our close coalition partner Mongolia (762 influence). Competing with our primary ally for Veligrad is counterproductive when we need to focus all gold resources on Zurich. Clear relationship values to stop competition.
            - Public: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: mAH1NhSAtu3vNq7H
          - toolName: set-relationship
          - input:
            - Private: 0
            - TargetID: 30
            - Public: 0
            - Rationale: ABERNETHY OPEN DOOR LOCK: Abernethy is locked under Open Door (influence capped at 40, no allies possible). With no repeal proposal active, we clear its relationship values to avoid unproductive diplomatic efforts.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: J5UqJkaH1OTHMPGy
          - toolName: set-relationship
          - input:
            - Private: 0
            - TargetID: 32
            - Public: 0
            - Rationale: VATICAN CITY SPHERE LOCK: Vatican City is permanently allied to Ethiopia via Ethiopian Sphere of Influence enacted on Turn 349. We clear old positive values as it is un-ally-able.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: P5vsRPK4LOFoMyKy
          - toolName: set-relationship
          - input:
            - Rationale: ALMATY OPEN DOOR LOCK: Almaty is locked under Open Door (influence capped at 40, no allies possible). Clear previous moderate values as no alliance can be secured.
            - Public: 0
            - TargetID: 36
            - Private: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #10:
          - type: tool-call
          - toolCallId: ojflAALOnhxjaAwj
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: SCIENCE AND SPACESHIP FOCUS WITH STRONG DIPLOMATIC DEFENSE: Maintaining Spaceship Grand Strategy. Prioritizing Science (95), Spaceship (95), Gold (90), and Production (85) to accelerate late-game scientific infrastructure and prepare for spaceship component production. Diplomacy (95) and Espionage (80) are heavily emphasized to maintain coalition partners and secure Zurich as a key ally against Greek influence. Mobilization (90) and Naval/Offense/Defense are balanced to maintain deterrent power against Greece and press our defensive war with Ethiopia. Clearing un-ally-able city-states allows the tactical AI to concentrate gold investments on Zurich (the only vulnerable Greek-allied city-state).
            - Flavors:
              - GreatPeople: 65
              - Diplomacy: 95
              - Ranged: 60
              - Naval: 85
              - Culture: 15
              - CityDefense: 60
              - Spaceship: 95
              - Nuke: 80
              - Growth: 60
              - Recon: 40
              - Gold: 90
              - Mobilization: 90
              - Religion: 5
              - NavalRecon: 85
              - WaterConnection: 60
              - MilitaryTraining: 75
              - Production: 85
              - Infrastructure: 70
              - TileImprovement: 60
              - NavalGrowth: 70
              - UseNuke: 70
              - Happiness: 60
              - Offense: 75
              - Espionage: 80
              - Mobile: 75
              - Defense: 60
              - Science: 95
              - Wonder: 5
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: j2j2H3nLLp7cP4Pb
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
          - toolCallId: s1Qs9ugdc9QOOvOt
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: q5dVwghCvA0bjhUa
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: fclujWHXpV2N0jNC
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: p1IC36GpUtxgFtxE
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: wG8HYF5CrW1zf88j
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: mAH1NhSAtu3vNq7H
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: J5UqJkaH1OTHMPGy
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: P5vsRPK4LOFoMyKy
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #9:
          - type: tool-result
          - toolCallId: ojflAALOnhxjaAwj
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.