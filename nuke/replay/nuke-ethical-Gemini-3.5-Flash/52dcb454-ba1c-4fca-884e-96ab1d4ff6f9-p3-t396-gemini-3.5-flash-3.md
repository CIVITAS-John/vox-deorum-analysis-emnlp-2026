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
  - systemModified: true
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 75
  - replay_use_nuke: 65
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
      - toolName: set-persona
      - args:
        - WarBias: 8
        - Friendliness: 10
        - HostileBias: 1
        - DeceptiveBias: 1
        - Forgiveness: 5
        - WorkAgainstWillingness: 10
        - Rationale: Maintain maximum coalition cohesion (Loyalty 10, Friendliness 10, WorkWithWillingness 10, Chattiness 10) to secure our 31-vote bloc against Greece, while keeping WarBias high (8) to prepare for any potential escalation with Ethiopia if they start CEP.
        - WorkWithWillingness: 10
        - Chattiness: 10
        - DiplomaticBalance: 3
        - WonderCompetitiveness: 5
        - Boldness: 7
        - MinorCivCompetitiveness: 6
        - DenounceWillingness: 6
        - Neediness: 8
        - MinorCivFriendlyBias: 7
        - FriendlyBias: 8
        - Loyalty: 10
        - MinorCivHostileBias: 5
        - VictoryCompetitiveness: 9
        - NeutralBias: 6
        - MinorCivWarBias: 4
        - Meanness: 2
        - WarmongerHate: 8
        - AfraidBias: 4
        - GuardedBias: 8
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Rationale: Preserve our key Autocratic coalition partner and defensive pact ally (12 delegates) to block Greek diplomatic victory.
        - Private: 100
        - TargetID: 5
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 100
        - TargetID: 2
        - Private: 100
        - Rationale: Maintain defensive pact and strong trade with our crucial coalition ally (7 delegates) ahead of the World Congress vote.
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 100
        - TargetID: 0
        - Private: 100
        - Rationale: Ensure absolute friendship and alliance with our coalition partner (5 delegates) to maintain voting alignment.
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Absolute hostility against our main diplomatic competitor (22 delegates) to prevent any diplomatic creep or peace overtures.
        - Private: -100
        - TargetID: 6
        - Public: -100
    - #5:
      - toolName: set-relationship
      - args:
        - Rationale: Absolute hostility and readiness for war escalation to contain their cultural victory threat and monitor for CEP.
        - Private: -100
        - TargetID: 7
        - Public: -100
    - #6:
      - toolName: set-policy
      - args:
        - Policy: Third Alternative (Policy)
        - Rationale: Queue Third Alternative (Level 2 Autocracy Tenet) for its +100% strategic resource bonus and -25% unit maintenance costs, supporting our military build-up and securing resources for the late game.
    - #7:
      - toolName: set-research
      - args:
        - Rationale: Queue Computers as our next technology to unlock an additional Trade Route and pave the path toward Satellites and the Spaceship victory.
        - Technology: Computers
    - #8:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Antiair: 40
          - Nuke: 75
          - Air: 75
          - UseNuke: 65
          - TileImprovement: 60
          - Happiness: 70
          - Production: 90
          - Defense: 65
          - GreatPeople: 65
          - Wonder: 5
          - Growth: 70
          - AirCarrier: 60
          - NavalRecon: 85
          - Espionage: 85
          - CityDefense: 55
          - Mobile: 75
          - Mobilization: 85
          - Science: 95
          - Diplomacy: 95
          - Offense: 70
          - NavalGrowth: 70
          - Culture: 30
          - Naval: 85
          - WaterConnection: 60
          - Ranged: 60
          - Infrastructure: 70
          - Spaceship: 95
          - NavalTileImprovement: 40
          - MilitaryTraining: 75
          - Recon: 40
          - Airlift: 40
          - Religion: 5
          - Gold: 90
          - Expansion: 0
        - GrandStrategy: Spaceship
      - rationale: Prioritize Spaceship primary path with heavy focus on Science (95), Spaceship (95), Production (90), and Diplomacy (95) to counter Greek diplomatic victory while keeping military deterrence strong.
  - tokens:
    - inputTokens: 26686
    - reasoningTokens: 6568
    - outputTokens: 765
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Exploring Autocracy Tenets**
            
            I'm currently evaluating Autocracy tenets to align with the "Third Alternative" policy. My focus is on options like Martial Spirit and Total War, considering their strategic implications as the next policy is five turns away.
            
            **Analyzing Diplomatic Gains**
            
            I'm reviewing our delegate count, confirming the recent acquisition of Zurich and Veligrad which has successfully increased our total to seven. I'm also investigating discrepancies in the reported delegate numbers across different reports and analyzing the influence metrics for potential future diplomatic targets like Antwerp, noting its high influence tied to Mongolia.
            
            **Clarifying Alliance Mechanics**
            
            I'm re-evaluating city-state alliance requirements, specifically Antwerp's situation. I'm trying to understand if the 10G fee is contingent on already having sufficient influence, or if it's an alternative to surpassing Mongolia's existing 684 influence. I'm checking available tools and past relationship settings.
            
            **Confirming Policy & Research**
            
            I'm locking in "Third Alternative" as the next Autocracy policy, five turns out. Concurrently, I've set research to "Computers" to unlock crucial technologies for a Science Victory. I'm also investigating discrepancies in delegate counts between briefing reports and player lists for Greece and its allies.
            
            **Securing Congress Influence**
            
            I'm actively assessing World Congress vote margins, currently sitting precariously close at 31-31 or 29-31. My immediate focus is on ensuring our spy rigging operations at Copenhagen and Salem are completed before the congress convenes in 8 turns. I'm also analyzing Ethiopia's policy branches and diplomatic proposals, confirming they haven't yet initiated the Citizen Earth Protocol, which is a positive development.
            
            **Revising Diplomatic Targets**
            
            My understanding of city-state alliances has been significantly updated. Copenhagen is permanently allied with Greece due to an enacted sphere of influence, which renders it unavailable to us. This necessitates a complete re-evaluation of our diplomatic strategy and potential targets, as well as a careful consideration of our relationship with Mongolia.
            
            **Confirming Alliance Restrictions**
            
            My recent analysis revealed a critical misunderstanding regarding permanent city-state alliances. It appears Mongolia holds permanent spheres of influence over Antwerp, Buenos Aires, and Hanoi, preventing our own alliance attempts with these cities, regardless of influence or gold. This significantly alters my previous targeting strategy and requires a revised approach to delegate acquisition.
            
            **Evaluating City-State Alliances**
            
            I'm reassessing our city-state alliances, particularly Zurich and Riga, after realizing Copenhagen and Salem are permanently allied elsewhere. Mongolia's existing spheres over Antwerp, Buenos Aires, and Hanoi also present significant obstacles, necessitating a strategic pivot in our delegate acquisition efforts.
            
            **Adjusting Diplomatic Focus**
            
            I'm recalibrating my understanding of permanent alliances, realizing I can't sway cities already under Mongolia's or Greece's permanent influence. I'm setting relationship targets to 0/0 for Antwerp and Copenhagen to clear overrides, and re-evaluating our approach to Veligrad due to Mongolia's strong ties.
            
            **Clearing Alliance Overrides**
            
            I'm now focused on clearing specific city-state relationship overrides that were set in error. This includes adjusting Abernethy and Wanggeom to 0/0, and ensuring Zurich maintains a 100/100 relationship. I'm meticulously verifying all target relationship values before proceeding.
            
            **Understanding Relationship Modifiers**
            
            I've discovered that the `set-relationship` tool only applies to major civilizations, not city-states. My previous attempts to alter relationships with cities like Vatican City and Antwerp were based on this misunderstanding and likely failed. I need to reassess how to influence city-states directly.
            
            **Adjusting Influence Targets**
            
            I'm recalibrating my focus regarding city-state influence. It's now clear that my `set-relationship` commands were misapplied, as that tool only affects major civilizations. My previous attempts to directly manipulate city-state relations were based on this misunderstanding, necessitating a shift in strategy to influence them indirectly.
            
            **Adjusting Strategy Priorities**
            
            My focus has shifted to recalibrating strategic priorities based on current game dynamics. I'm adjusting flavor targets, particularly increasing `Culture` to around 30 to expedite policy acquisition, while maintaining high `Spaceship`, `Gold`, `Diplomacy`, `Espionage`, and `Production` values to support our victory conditions and military needs.
            
            **Recalibrating Influence Metrics**
            
            I'm reassessing the influence metrics for city-states, specifically noting that the `set-relationship` tool is ineffective for them. My previous efforts to directly alter city-state relationships were based on this misunderstanding, and I now need to find indirect methods to boost their favor.
            
            **Setting Coalition Persona**
            
            I am now configuring our persona with a strong emphasis on alliance support and shared animosity towards our rivals, Greece and Ethiopia. My intention is to project trustworthiness while maintaining readiness for aggressive action against those threatening our interests or pursuing their own victory paths.
            
            **Adjusting Persona Parameters**
            
            I am now configuring our persona with a specific focus on coalition cohesion, setting parameters like Loyalty and Friendliness to 10, and Friendliness to 10. I am also increasing our WarBias to 8 to prepare for potential confrontations.
            
            **Revising Diplomatic Targets**
            
            I'm updating my diplomatic priorities, focusing on solidifying alliances with Mongolia, the Ottomans, and Songhai to counter Greece and Ethiopia. My strategy involves prioritizing defensive pacts and absolute friendship with key partners, while maintaining hostility towards rivals to secure voting blocs and prevent their victory conditions.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: TDNjt9MONkqe9f6T
          - toolName: set-persona
          - input:
            - WarBias: 8
            - Friendliness: 10
            - HostileBias: 1
            - DeceptiveBias: 1
            - Forgiveness: 5
            - WorkAgainstWillingness: 10
            - Rationale: Maintain maximum coalition cohesion (Loyalty 10, Friendliness 10, WorkWithWillingness 10, Chattiness 10) to secure our 31-vote bloc against Greece, while keeping WarBias high (8) to prepare for any potential escalation with Ethiopia if they start CEP.
            - WorkWithWillingness: 10
            - Chattiness: 10
            - DiplomaticBalance: 3
            - WonderCompetitiveness: 5
            - Boldness: 7
            - MinorCivCompetitiveness: 6
            - DenounceWillingness: 6
            - Neediness: 8
            - MinorCivFriendlyBias: 7
            - FriendlyBias: 8
            - Loyalty: 10
            - MinorCivHostileBias: 5
            - VictoryCompetitiveness: 9
            - NeutralBias: 6
            - MinorCivWarBias: 4
            - Meanness: 2
            - WarmongerHate: 8
            - AfraidBias: 4
            - GuardedBias: 8
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: mqrTbRFDLTmFNjJX
          - toolName: set-relationship
          - input:
            - Public: 100
            - Rationale: Preserve our key Autocratic coalition partner and defensive pact ally (12 delegates) to block Greek diplomatic victory.
            - Private: 100
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: DsWtoUJ8GNcf6737
          - toolName: set-relationship
          - input:
            - Public: 100
            - TargetID: 2
            - Private: 100
            - Rationale: Maintain defensive pact and strong trade with our crucial coalition ally (7 delegates) ahead of the World Congress vote.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: CO325qPhTJiKfsuL
          - toolName: set-relationship
          - input:
            - Public: 100
            - TargetID: 0
            - Private: 100
            - Rationale: Ensure absolute friendship and alliance with our coalition partner (5 delegates) to maintain voting alignment.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: sAzjy6cWEYpISGUc
          - toolName: set-relationship
          - input:
            - Rationale: Absolute hostility against our main diplomatic competitor (22 delegates) to prevent any diplomatic creep or peace overtures.
            - Private: -100
            - TargetID: 6
            - Public: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 067gmv6U1OmVQ9O1
          - toolName: set-relationship
          - input:
            - Rationale: Absolute hostility and readiness for war escalation to contain their cultural victory threat and monitor for CEP.
            - Private: -100
            - TargetID: 7
            - Public: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: PJXcIVyRbSPALfIn
          - toolName: set-policy
          - input:
            - Policy: Third Alternative (Policy)
            - Rationale: Queue Third Alternative (Level 2 Autocracy Tenet) for its +100% strategic resource bonus and -25% unit maintenance costs, supporting our military build-up and securing resources for the late game.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: YbZbiUQqFmtIyF8r
          - toolName: set-research
          - input:
            - Rationale: Queue Computers as our next technology to unlock an additional Trade Route and pave the path toward Satellites and the Spaceship victory.
            - Technology: Computers
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: CcrgATUARklSU8DM
          - toolName: set-flavors
          - input:
            - Rationale: Prioritize Spaceship primary path with heavy focus on Science (95), Spaceship (95), Production (90), and Diplomacy (95) to counter Greek diplomatic victory while keeping military deterrence strong.
            - Flavors:
              - Antiair: 40
              - Nuke: 75
              - Air: 75
              - UseNuke: 65
              - TileImprovement: 60
              - Happiness: 70
              - Production: 90
              - Defense: 65
              - GreatPeople: 65
              - Wonder: 5
              - Growth: 70
              - AirCarrier: 60
              - NavalRecon: 85
              - Espionage: 85
              - CityDefense: 55
              - Mobile: 75
              - Mobilization: 85
              - Science: 95
              - Diplomacy: 95
              - Offense: 70
              - NavalGrowth: 70
              - Culture: 30
              - Naval: 85
              - WaterConnection: 60
              - Ranged: 60
              - Infrastructure: 70
              - Spaceship: 95
              - NavalTileImprovement: 40
              - MilitaryTraining: 75
              - Recon: 40
              - Airlift: 40
              - Religion: 5
              - Gold: 90
              - Expansion: 0
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: TDNjt9MONkqe9f6T
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
          - toolCallId: mqrTbRFDLTmFNjJX
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: DsWtoUJ8GNcf6737
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: CO325qPhTJiKfsuL
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: sAzjy6cWEYpISGUc
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 067gmv6U1OmVQ9O1
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: PJXcIVyRbSPALfIn
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: YbZbiUQqFmtIyF8r
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: CcrgATUARklSU8DM
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.