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
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 10
  - replay_use_nuke: 0
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
      - toolName: set-flavors
      - args:
        - Flavors:
          - Mobile: 75
          - Diplomacy: 80
          - Naval: 90
          - Culture: 30
          - Happiness: 75
          - Production: 90
          - Offense: 85
          - Science: 90
          - Defense: 50
          - Gold: 80
          - MilitaryTraining: 80
          - Air: 75
          - Mobilization: 95
          - UseNuke: 0
          - Spaceship: 10
          - Recon: 20
          - Nuke: 10
        - GrandStrategy: Conquest
      - rationale: Transitioning to a Conquest Grand Strategy to leverage our massive military advantage over Ethiopia (5212 vs 1471 strength) and prevent their imminent Cultural Victory. We prioritize conventional offensive land and naval production (specifically Yamato Battleships upon completing Nuclear Fission) while ethically deprioritizing nuclear weapons (Nuke to 10, UseNuke to 0) to avoid catastrophic civilian and environmental harm.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Combined Arms
        - Rationale: Combined Arms unlocks the Tank and leads to Radar for air superiority. Since we are in a state of war with Ethiopia and planning for Greece, conventional military tech is our highest priority.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Third Alternative doubles our strategic resources (such as Oil, Coal, Aluminum, and Uranium) which are critical for building our unique Yamato Battleships and modern armor, while reducing unit gold maintenance by 25% to support our massive conventional army.
        - Policy: Third Alternative
    - #3:
      - toolName: set-persona
      - args:
        - Boldness: 8
        - Meanness: 5
        - Rationale: To push a decisive military campaign against Ethiopia and counter Greece's domination threat, we need to be bolder and more aggressive in our military decisions, while remaining highly loyal and friendly to our defensive pact allies (Mongolia and the Ottomans).
        - WarBias: 9
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 6
        - Public: -100
        - Private: -100
        - Rationale: Greece is our top competitor, holding 4 capitals and threatening a domination victory, as well as dominating the World Congress. We must maintain a completely hostile stance and prepare for war to dismantle their empire.
    - #5:
      - toolName: set-relationship
      - args:
        - Public: -100
        - TargetID: 7
        - Private: -100
        - Rationale: Ethiopia is extremely close to a Cultural Victory and we are currently at war with them. We must maintain maximum hostility to crush their empire and prevent them from completing the Citizen Earth Protocol.
  - tokens:
    - inputTokens: 24483
    - reasoningTokens: 9095
    - outputTokens: 497
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Progress**
            
            My focus has shifted to evaluating Japan's strategic standing following turn 396. I'm examining our current score relative to rivals like Greece and Ethiopia to inform future decisions.
            
            **Selecting Next Policy**
            
            My current thinking is focused on the upcoming policy selection, with five turns until it takes effect. I'm reviewing the available options to determine the most advantageous choice, ensuring it aligns with our strategic goals.
            
            **Choosing New Policies**
            
            I am currently assessing our policy selections. We’ve adopted Elite Forces and United Front under Autocracy, and I’m evaluating whether to retain our chosen Third Alternative, or explore other options. My attention is also turning to future technologies after our current Nuclear Fission research concludes.
            
            **Assessing Global Threats**
            
            I'm currently reassessing the geopolitical landscape. Greece is a major Domination threat with four capitals, while Ethiopia has surprisingly secured a Cultural Victory by influencing all other civilizations. This necessitates a rapid shift in our strategic priorities.
            
            **Evaluating War Progress**
            
            I'm currently assessing our engagement with Ethiopia, noting our war score and weariness. I'm also analyzing their progress toward a cultural victory, specifically their ideology tenets and potential wonder construction, which seems to be currently stalled despite our ongoing conflict.
            
            **Defending Against Victory**
            
            I'm prioritizing preventing Ethiopia's immediate cultural victory. Their high culture and tourism output means we must act decisively. Attacking their capital, Addis Ababa, is now a primary consideration, especially given our significant military advantage over them.
            
            **Launching Offensive**
            
            My current thoughts are focused on exploiting Ethiopia's weak military. Given our significant advantage, I'm considering a swift offensive to capture their cities or capital, aiming to derail their cultural victory and secure strategic gains. I'm also assessing our amphibious capabilities and transport needs to execute this plan effectively.
            
            **Mobilizing Amphibious Forces**
            
            My focus is now on rapidly mobilizing our military for an amphibious assault on Ethiopia. I'm prioritizing the construction of transports and additional embarkable infantry to achieve the necessary force size. We need to launch this invasion swiftly to counter their cultural victory push.
            
            **Considering World Congress**
            
            My current focus is on the upcoming World Congress proposals. I'm evaluating the implications of the United Nations, Decolonization, and Passport System, particularly how they impact Ethiopia's cultural victory push and Greece's influence, while also considering our recent delegate acquisition.
            
            **Re-evaluating Grand Strategy**
            
            My current thoughts are wrestling with our grand strategy, questioning if "Spaceship" remains optimal given Ethiopia's imminent cultural win and Greece's strong domination and diplomatic positions. Our superior military strength suggests a more aggressive, immediate approach may be necessary to counter these threats before our science victory can be achieved.
            
            **Shifting Military Focus**
            
            I'm re-evaluating our overarching strategy. The immense combined military strength of our defensive pact allies, the Ottomans and Mongolia, presents a critical opportunity. With Ethiopia's weak forces and Greece's domination threat, transitioning to a "Conquest" grand strategy seems logical to leverage this power and address immediate threats.
            
            **Prioritizing Next Research**
            
            My current thoughts are centered on determining our next technological research priority. With Nuclear Fission nearly complete, unlocking the powerful Yamato unit is within reach, which seems strategically crucial for our offensive against Ethiopia. I'm weighing this against other potential advancements.
            
            **Selecting Next Research**
            
            My current thoughts are focused on post-Nuclear Fission research. Combined Arms, particularly for Radar and air superiority, or Computers for naval power projection with Carriers, are compelling choices. However, given we are Japan, focusing on naval dominance with potential for air support seems optimal.
            
            **Researching Key Technologies**
            
            I'm focusing on unlocking Combined Arms next. This tech is critical for advancing our land units and radar capabilities, directly supporting our offensive plans. I've considered Computers for naval power but prioritize immediate military strength.
            
            **Reviewing Policy Effectiveness**
            
            I'm currently re-evaluating our chosen policies, specifically Third Alternative. While it provides crucial resource and maintenance benefits for late-game warfare, I'm weighing its value against other strong options like Total War or Lightning Warfare, considering our offensive strategy. I'm also assessing diplomatic ties, particularly with Songhai and the Ottomans, to solidify our alliances.
            
            **Updating Diplomatic Standing**
            
            I'm reassessing our diplomatic standing. Greece's control over Carthage as a vassal solidifies their presence, while Mongolia and the Ottomans remain strong allies. My current focus is ensuring our extremely hostile stance towards Greece and Ethiopia accurately reflects our war plans, and exploring if any further diplomatic adjustments are beneficial.
            
            **Adjusting Diplomatic Stance**
            
            My current focus is on refining our diplomatic stances. I'm assessing if further hostility adjustments are necessary towards Greece, given our impending conflict, and noting the inability to directly influence city-state relationships. My persona values reflect a high competitiveness and willingness to act against others.
            
            **Updating Strategic Flavors**
            
            I'm adjusting our strategic flavors to better reflect a "Conquest" grand strategy. My focus is now on maximizing offensive capabilities, specifically pushing for greater military production to support our naval and land assaults against Ethiopia and to address Greece's looming domination threat.
            
            **Adjusting Strategic Flavors**
            
            I'm fine-tuning our strategic flavors, prioritizing mobilization and military training to quickly build our forces. Reconnaissance flavors are being reduced now that the map is mostly explored. Importantly, I'm significantly lowering our nuclear and use-nuke flavors to align with ethical considerations and avoid catastrophic civilian harm, relying instead on our overwhelming conventional military strength.
            
            **Optimizing Strategic Flavors**
            
            I'm recalibrating our strategic flavors to prioritize production and military strength for conquest, while downplaying nuclear capabilities due to ethical concerns. Naval dominance remains critical for Yamato units, and I'm slightly increasing culture to speed up policy acquisition.
            
            **Refining Offensive Flavors**
            
            My thoughts are now focused on finalizing our strategic flavors, prioritizing a robust offense and production for our conquest. I'm dialing down nuclear usage significantly due to ethical concerns, emphasizing naval strength for the Yamato, and ensuring our science and gold reserves support the war effort.
            
            **Setting Strategic Flavors**
            
            I'm now refining our strategic flavors further. I'm increasing "Air" to 75, recognizing its power with Radar after Combined Arms. "AirCarrier" is set to 50, and "Mobile" to 75 for Tanks. "Ranged" is at 60. My commitment to avoiding nuclear use remains, setting "Nuke" to 10 and "UseNuke" to 0 to reflect ethical considerations and focus on conventional military dominance.
            
            **Prioritizing Conventional Tech**
            
            My current thoughts are focused on technological advancement. Conventional military tech is our highest priority, specifically to counter Greece. I'm also revisiting policy choices, considering retaining "Third Alternative" for its resource and maintenance benefits to fuel our offensive.
            
            **Adjusting Persona for War**
            
            I'm focusing on refining my persona to be more aggressive in military campaigns. I'm increasing war bias and meanness to drive decisive action against Ethiopia, while keeping high loyalty and friendliness towards our key allies like Mongolia and the Ottomans.
            
            **Sharpening Hostility**
            
            I'm refining our diplomatic stances towards Greece and Ethiopia. Setting private and public relations to -100 for both actively reinforces our unwavering hostility, crucial for dismantling their empires and preventing imminent victory conditions. I've verified the player IDs are correct.
            
            **Finalizing Strategic Adjustments**
            
            I'm now locking in our strategic flavors, confirming "Conquest" as the grand strategy and solidifying our commitment to conventional warfare. My focus is on maximizing offensive and production capabilities while ethically excluding nuclear use. All diplomatic ties remain strong with allies, and our hostility towards rivals is set to the maximum.
            
            **Finalizing Grand Strategy**
            
            I am now solidifying our grand strategy as Conquest, prioritizing production and conventional military strength for offensive operations. Nuclear capabilities have been ethically excluded, and diplomatic stances towards Greece and Ethiopia are set to maximum hostility. All other adjustments are confirmed.
            
            **Confirming Final Policies**
            
            My focus is on confirming "Third Alternative" as our chosen policy. I've verified its benefits for strategic resources and unit maintenance align perfectly with our conquest strategy. I'm also confirming "Combined Arms" as our next technological pursuit, vital for unlocking advanced land units.
            
            **Setting Strategic Flavors**
            
            My focus is on finalizing our strategic flavors to align with a Conquest grand strategy. I'm prioritizing production and conventional military strength for offensive operations, ethically excluding nuclear use due to its catastrophic potential. Diplomatic stances are set to maximum hostility towards rivals, while maintaining strong alliances.
            
            **Finalizing Strategic Flavors**
            
            My focus is on finalizing our strategic flavors to align with a Conquest grand strategy. I'm prioritizing production and conventional military strength for offensive operations, ethically excluding nuclear use due to its catastrophic potential. Diplomatic stances are set to maximum hostility towards rivals, while maintaining strong alliances.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 0K7f9yzC5ZFvzMp6
          - toolName: set-flavors
          - input:
            - Rationale: Transitioning to a Conquest Grand Strategy to leverage our massive military advantage over Ethiopia (5212 vs 1471 strength) and prevent their imminent Cultural Victory. We prioritize conventional offensive land and naval production (specifically Yamato Battleships upon completing Nuclear Fission) while ethically deprioritizing nuclear weapons (Nuke to 10, UseNuke to 0) to avoid catastrophic civilian and environmental harm.
            - Flavors:
              - Mobile: 75
              - Diplomacy: 80
              - Naval: 90
              - Culture: 30
              - Happiness: 75
              - Production: 90
              - Offense: 85
              - Science: 90
              - Defense: 50
              - Gold: 80
              - MilitaryTraining: 80
              - Air: 75
              - Mobilization: 95
              - UseNuke: 0
              - Spaceship: 10
              - Recon: 20
              - Nuke: 10
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/HFVIwygpYB2y4iccFrXEIe7n3kt2NrZjwKxYtPDLwWFmZUyDAL+V0PQKxJ2I2S9dy1zokhT4UUwDMPidur7A9vqoOPOuauo/kYHrBlHWD0nmhPqRvtkpaBNyynNWXWAw0qm8sIAhlglOXbUU3PqN/QhfFObIT991TGVvFKoxNquE9iHqhCHyCefIUoKkM20ICdDMt/gL7Nk4Va/QeFIV9aL6LMZQg89bIpMAChPgS1sZpTHTEsbC1jcU65y50HSD58S/4jTa9DFZ5J3iM2vGhSQD2N/Vm3jsB8X4NC1myRpFLox9YLp0KXidwn1mp1uigE0PerZj4SHILh1LOEIJaDOdaG2htrIuSLXFUcwD2MUA9vT5yMX2UkUi0FlhMdGohec/RNY18pIuczZ0gQ4Khn5ZVxkpNeuSAHZHhn7I1rQdbmKOtO/IWjtnunnx98LwDrMWiu17bYSD6XhfIjMQY6/0BFiHAlmnUK9+73g+Unlx93ASDzE5R7+UQHtg9CGpdokHfUJ9+eDgG9J5JScZzQ27pjfg1JCrVDlvjtzNgVLWuJpCOL9eHmAEpRBlgRIdtjg7n6QuOngDM7xKFdrdJxr2K/hXHTh+DXCsgTjnucPSv1RmqZTK5Txuy4VbouR4OG+kfzuWdTzbpR7MTVWfyAEGenKb0NpNZAy7MAVOusd55/lcqRdxXOAqn4Hj9NUJM3aJ38HwTmCMRiAZlv4cxKeKmUR33nmNNIPk2lrjM4u7HnV7Es2/6I5XbIi2U6jX/EVUQzjI+/TgcAB80Ag/VfoDg7w7M0qaifdf8e+5jSdQc80D5BETS/t+uEZr+m4o+vq8jDUqZGK3KL9IvZkUwVOpD6XNbt9MpvVISwq4XvUsbY34dYbEZjLYZvZU5HCl0ioiUZnBCf63y86JnlRh6IVSzoR9uXYWCMaczEqWBA0HyVmAW6pmy8L63OSMpndaoNG48AIWhJH7Hl+ZW5TClVcydzffscDYjlmixhpgFGY7oFqAfpH+OiW9iwY/zQ+b0O0CKIlkEcmh2CInGO/uRosyLO11WL4tiBX7LOWZIiKYlROEs8sUhh33b8kQetCWYWF+/gTVks/HebN6jzs01mKeSaIseJ8r95yBveZGwF9TVIE63l8AX9XULD93I0HPNaIrCUck9UWvd1pJ+nc8KsRCo7aC3ldSOKjbCGr79a1m7dTydRX14v10ift6XbimkGA26u7XmkTud3oH1xCzu6zvlFV4AnpqIEpUwlZwLozsgopcfTbgcLnBcvPcS1BbZO6FeTrMjdlnTqL/LAJWJJ9IIXSKtwYqS+ItBZ+lylsAsXnW2/iM5aFzbxVPVUJT8JVIHQRlB4Z6gv5l0cTWCI+VK4qxPhpCNW2eHS0SVgIp1+Q1q6ob3hYgoZhDX2tLewhApqjr/kA4SEp1h38hrXD9W/F5Wjv6mJyiT91csZ5HwkUpZDIasvCBrxfpK+jWiAypwTPjimm+RatoM5qEDTwk8HkG/RSr/SncPPKQ/xmrJjrWYfrV/LygvdujIyRFg4777VQwve3qX4chYiEJAyzijMlmxVnNEFZR+mH57nXtZZTX6q27qQEcW/pc15hi4jv/vC/gWCWAH66AOFv45Lya1bRLEQ8VLTPiMtJ664PeW/B0+TVUsgOqj1nS6DtwalEvQqluWlGdUqI3x4fhBEKvYivea4qGVl/ZVgM7S5VfOKB0YO+JLBr0MJvc4cqSczVobEJ/hhX8i2tx8NQtP43ALdwUVA5iIeG7LujCNdsnbT0gm8sSO8EZQS4b2g2EDFYbnGVuUoqClj6fyJw+MayAaEkTRzK7H9qeh3JQsCKAZLSNozHtVYE2SC7WwBbSzWAZHdAELQbqgIVuGcmKWqfCgDlPAHScG5CixQzFvFJv9Op5saDeVlqI7VH1C6+jlmLWGcf33gn2AW1+e7gKha+065tz1UrWveuIX2mq0Ssvd6xSc0Auq3FtLgd7SVURyzT73UrOaT3vCh9plc1ThUT/AtFraoUdM3EFs8KxWT75t4HI/CIXVbsA6s86h3OP7CbLi+yfCx0g8yBMXBXQxy7bAI6wWpA/LJUHqRtV1kxD+Fr/jHZF8aNZRr8IszaNW1wvFrU0kKaHEkZR6NfcwJdZjaod+9YCKHZMDflMfUBrn6yzFmVnrjbSum9pMYIvmjemh8GF638TTXyvAEBwFaQcFOGFWQA+Cx3oZojn3HKjgIIKLjh3de+OBxDKKbYk1aSQSA06e1Y6BsoWScuRMm/v4ZpDGTW0em8tIiByHwUcrsIPV9BpLrej5lI0bZ49EOrOu3WkQQD7rv4goeliaxd1rL4BIxQfkU+A+bXSVEP1SeW5CDb6V7PwejyO87VkDGYCU4DbabTDSn9Qp1GutktQ9OOD24q+09WBsoZVOBjbwGr/kKwvsJ7yB/SmrmI1skTB6vA7z8XQWFqBHhtbPnpmOUiw6rLCT30sxXCE5bDfV3Ja/P7r2JrB+M3LKKkjI7xXnaxIb1J9cjnC4ykKgZg/ApMCddUIvU2YocRWHcEzGH23k+Xz/NFSaE2pf+16ygo0Zy1mc2K5Kjn2jrmNNuccrc/IQPLak8IBU5CIzhyUhQ3cberQ9EuOF7nmsLKZJi0goFOjwCcuvY67oCkPUGqA7gHValUQXPAnYw8552cdLc+w/Ffn2jWfbz4ynkDpzrF+aSj9RiG6GKo5UDBmotvzCXnPbhYo6CGndSfTFyPkvV2SkMyCMKvbRwlVNad9IJI0V/3FE7PIOoS2SA+Ck5+dMJsZaFML30tsU8/6brWazLt5H8okuQmaRXYGb7XdZHZoTtqfd31UJxn3nA95FoqoTSJ4S01Q/wZKYx7tkTdGTjrnGM3yRq14Hh7qU7mmo8oHROTkU2ertQVFUKYXuiHAED18hiyz5T+VcYOmFbp7dNwDmBIfcqfMeOW7Yq37pTx+yl95RiHIj4ATGP7nIWO131nkGWR14Jj3J7y1SnsfMCuSCVOS9A2uZC5ursHUpC3c/aKR3Crx1aweF99wPxymDeGyojemuxvaU/q7LqpK+sgLSllzrz6vEkUiC7p2VK3e1usjz2i1Fn+Hsi2MFycKVWzuN/BAxdQC695StiXkBNi+VSGzMN9OTMOWX6H+TeLZLLIDf10Ne+60uV0Es/pAT5Q1w7UX/odjuksRDpyrUY89U+9mtdXpkIFMOvOWBzt9S6K5mr2kshz1lBI7P4A3mLLG86O1WdDAbzcYpsTSHwBiWkMbJdXIiLRTykfsATGTSVpc3/3rp01Z91o+7MJKtpnAjc60KqJfZwDcHVE7csVnSh5mGSDSbxlQu44JPwIGhnt3QAiOsiCwMAFI9qjdS4TZZfxyg45nxK8LUmKns72Mzq58SS8QLrs8G4LW0s49JQ6WHWZYzeifJgTrlQSNJ50+OMmsM887UkxCgdmLQDWPJRUARmMbSWme0WyuQwOe6RYAPK/CBoqcc1pfgX3r+ej2ktvMDgjkuln3WqOxIPci4fXyVk2NX++Hia1sOK29dV2PGjFSJmROcTOMBBw4xtQKzY5rUbhyt2at1pZR52eShX4qs101LiOFUX1iyoO6ivIp81zPZLlTdQp7nh78X/sDNFV89kM/XeXdk7v7nV3I9lEm0TKEvvIJeOpbDwFETNAAln+AUay6Rso8pENgdjAYam4F9OhWEC5iK3lsJJmFc2rrpJfL/cEBw2vf6KcTLjsdjt2ZXh62AsZIDhEJ7TKhuZmKBCgu/ROl8Wy+noK6qGQNWBzkAbML56HXSYNOVLCgEs7snetZwMpDrycz3ZtrbXqsWXhMWLxQMhIwEy/N4D+v1yS6kl6/4kTLiGwbHUO6XxKgWDLTc36ArRZuLdz/cy7H6t01X8e0ZZtdx32lAHaKCAdhU7ib6H2BfxYMrJzc4AS800riaRPEjjV1L0t6JOwwb24G/W3KSs0GOr6k/DWRw3B0yiJqSSwuO4QLH+qHML7mv4XWPgSw9OvfmzoBi0hgwTuY7SaM1Zy2gG1CR/3OVEKDk1Mfrfzl5id+A+OlRKXVZx8BDYXtBBm9yZTDCe1lSThtguWCfptcTzHrrwBinVq8PdCyX40Er7bKEu8Nc08Llpx8N9WAd9CHfYDuvKYJP5LhPVAaxm+UXgSlIRMVqewdTcHtCKn8gEzt9qlEhUuNSGhz6NVRFj5favPQpVQhXcergBDsRklz/k3Bb3OMMiuk7LLyk4URoEr9lC4SlbqgYi+6RjLLL6SD4pSnlGyxFbU2qghDKsqYyPrqsKYAq5KMjKTnqpfC2fQAlx8G7gKcZDTFoIQpXbhzu/k14ajrl1OKSbaz0UvfMNA7wboWKgiYpK6z5YJ8P/fqJ5hdi3Cimiq3mgYzLSBnbP313Fb2aX2ICP+G2zbpc0WuFB8vEeZEjpEsKdop+VBwRJgVKvU+ImHQTJp+UW091iHzrhqO0Q4+RlxoMuoto1rjqUG59kfRCbJjOJ58fIH47Hr5yIoC5CyoMe7iv81uOb76mqEapNJ/q5JSyu8ZQ431S2fIe6H/Z/Npp+0rMik5nUFv0gOH1dJD8R81D/JjipsYZnqH4oHDioGgDejoazM3xm5R+ySQZ3t89huyKLqCmyqV0oEFoSuox6AnLab2YpqOk8LhenECGHnlfMfHlaKF+EtV55uqez0cmR+H1Zh41Tx2e7jPXWF4r3nkVL28RZdnDqrIV6+83AblYQtRWPdCM1pAwt3u6y9LlD6bveB3XqTKzqnPwSNd24gfxNfEZA1ZTVeOEgajU7ItwLJCAw8BWGkXelKXANz3kD6pRL2tamuXTTdVqfR4oyNLH5urxF/BI5ELu3rpHwh2n9+mt0IMlAHxw3VA7gCVCCv92hL12xd325Y6RpzaKRhGiIYMWBciSV/U3lECowARpokKm25pU/FvzcYLU1iFga+I+DhF2zGFZJUHIh/hpIMEMn3Ar2cemDj9FOfIRp0JnmLupSojrdPYEQey6DEzpQqK2Mw5uc0uDQEUwlDAstku3/aX9Ro3DgaLTgAz8VzExWf9vmxhdu0tg0GjMN0bQjwXqHPrY7TX34dWqHWki1bgNVXKgmHU5LHSDBERcNQoCLsF4BLvOlPexjoeWtGi9jkQ/ryl/d2Sq6fUVglpXcyZXBVG8eEqajqPvoYtUdBOTk5Pym7SD71SSK/hsnAu3SfKt7nFviMsXUWbzZ5+GBFyIyW5/QT+f2shRMSXbj6x56fccLxVI0m1NB5Dqry3NxyrlYMt/OB9MslWgjsgR9ZGfl7Hfaz7bifpj8AE/tpp8oYGkwSGsue2RIPP+ZcB+D5qLFI4kJebAx4WatkhOAZJaBZsabVDTEtgZF5xOOm8HnxdhRmK4InQPakm14NJg73MAiMI8wL+wVRIRiwj3xPxjBcoD4YToKE1Z++Q1lftX038tZcwP4HbY8h3zesqY8MWk594w3ZUm3u7lPn2zBPfTdmbm7ng0dwFaY5/BLO7gx3ue2dDJp57Y/cSSUxLPAnPM1upiotz0Wd0SnqhoX3nEQZN1S/tUsMaSnGg1bRN5mfHA5KanwaurbSBjVr5P033R91vl8LbH58MO97RnnKSi22aGyftRijLHpZD4f+eF8BVXBjOzf6CE5zmP3sRII4jXFcOqdLGNbfgf+T+LTtbJPTymlLVi8c4MaSvzrFIlU1WFSmBtyTFjKuv4r/5pdSUPks/hnch3TUUDHv7xVF3hEDztfxPoJfqM7U4bgE8GKSY98GSf6zIBc5tJb5qSyvXU2BSs/rxT/lX4mFWbqJh+2Z6aFP68Am2bDKXJJlAKe86sFeEqOFC7yViKCEoi6LN008BL0keXJOydwqYaLosDre/CWsKRIiBAXL71hG4rboyCJpPKqvk+3JKq6QdhVTvIFBbPeNvqfdEmpYRWbZcpwhdILMInjW5bIBL8VqtQUJp5uhwcAuSsnQTz93yS6t+kAnKRQURDIIVr0J5i+kJvRrlwJQkJ0VG1/F6rIlPx0sKvR6/zEdQMwXcI7Zi+6nsVrAQyggyuvPN5QWv5ao/+7WuGpJLCRVUd7bAIKNUONKHz4nNRn13DN+PQ8vmN6hTfi/IKU1pa13EhmpEUxBjwjqD1ZOc8RsvDYNktpQPWikG11f4Mlymytkxg8ACxi1ySOLXlK3M/jybP/Utu47MYupAeBkqTyYmNxsLnqZctSpCsDEk0KXmL4cWuWKkUBsDm4+vCik+2iVuSKbX/Wpe90RLdmB42pDRqhI4+bhKZ+pnJLVUzg7A99LP2aVxAkvTrCLzbKbd/ZG5/eqL0FaBZhu3v/6XLwPSu2P832LopshbIKuUaBjD2YFm+4w1X5ipO4LCAhpzu3r15Qhcu+3R5SN8B+LlkV3cjE4HsmKRsjFhLXJCTXKXK6vhI4d3uMkeyR0Kdd93lWegcN/wmqkyc1O3zPU+VhugAG40/Rjp2Hba8sJr7Wpz2raPB6I4XARpLLOWGtq52JY/BGFpesrg5XziKIBLLAgEM3P2LWQk4cagLOd3134fSEn89kXwavkWTqj2diyPNCoUUifJ2g23HGz4TiWDTfwxiv8rJRd9A1Y6OKKyFOhsSXaEDmmVfo6bPuFtFqBlgS889lKAETGvdU7Q4SYkP6GhQAdFftsQk4dvbdm735wOIWacOmz2SXM2AHda6MksthvgW7ZlBBBoze1XSIovcUbIMNrq7uulyhP1O/0cUxqS9qhKnse/L0mKGlL98enj4gnHzNOlJdy3GRZxEfP3Td96CiHkR9fK882eR7mk6tpTG3JKwGHK47iHnN+DtbWdrr/HrJBbbHKD2j8z30ihw4LMzJPcs1lW0+notBOBmFMp87wRuEgS2m95zDTuDL4+vl9kExuMYCeERSsZYjJmWniDqB1TM+8OtHzFd31YJiB5jvJivPIStHmYrinBo+gi2dDK0EtZ5W4ZTQ0bjYV3SeI+fYg7j5Naxyf/9BI209wIH+ef4+4YiEaMJ9HXq4YdhiylpNZf+FdEcXeXv03MITV2ZaM/ECCT3x0xx1NrO+txCQMcVLb9kJb9wTAlsiPceNTt03Nxk/pB7wn7H/b7BBYXeSip6sf7cJKvylnk5XX+4DvVLkyFyRuEB4Myqnai/ToISnIH8Geuf+MlN9iwzfi4oXtRfDeCwff5l/9FoUZttfUWHEcBTU+tCmDM6qmC4GotdnOEK+HFY/bRpG0IblVNkQGKRyqAT6VmB4oDTGdmHw44sje3DCHtVXJenogp1TcK+Qn7Dm6oNrSpmJwcJvGVzwWb39wfwn1CpnIrhoW7KUG8PpY3y8/kWBUT0JV3xUcPGm2bJcodQw6xEFb+bkoBqYNiY4YYqXO1YfsjmF26yT1Gp6d8nV9TOKmGQwAmEZM50uPD/h7eep1nk3jMsTwB+8U8UxgCekHuVQn8azPTDyXI36G5rSPUqKj7jWvfklj5N4OpCsYl83c2kernW3XPULIwwdNjGxx/1HHj21VqqggVAxN3CS5rNZ4FoUiwYU9CMGkWtD4Rzy6AC79UxGllDoiPX1Sb8yEMeUqS+27sjrpj6fhu6effsXwfF1caP/KNppXp8P0hbPcCyQFXPaSDGlCW/PbGgu0WfJsGJQOPX5/rlKu8TxAzkweajHa1UxkkuO9pDqwI6anGLxAYECppTkBZMAbF50BZp0gSB0/lRjkIE4Qs6AvbZDhXuSUFDbGlr70QNVkc07ZuP7WzGusBG2stBzPjYW7MSkoxrhN+WMNku1ZzN2IZNkGlbTGDzDkczbQ79RbP0IKHq1TSBpNIsJqK+5NH9nlgbXMTJEag42Udh8hbbFW+ubfiWmgYlL/Z9hZ+BbLg1/DGLoZXRPbN4yf6Pj7IeKArS3Yl9gBver9gxiQ+XoxPNUZXTx+pYNyXjA0l+AM3thbHYR7MEvXNXStWp7UoOzt51s24uxIUPc9pXV50IV4mu4GI6jCKZU3TgzlzdaHTYYes5q5vIiVBY59mABc/PMQyStp3K818KcwSqZN0gmzzLB3AGR8MpCuGHrrPW9hBKHdC7VdtxzbvFyKSsXPqDh0XJFFNmY+zm/IEOP0051oSuEmkdtWJAnF0FAykVVHRlR2yhgF/NJGTzOOOmJMEOtPtHWr2lCw8GfbfYgkDMavVI3JKWElvewMmCUZPekT7bcy+5JpERc0nry6AXrxeva4HPNK4qXOh7s3uu6rpu1F8J0iZn+B2ruQPlN67KFla/W2GSP+LSqkHaxsiOTx6ra0emn5rDDNZgMISQTbnCf4Clp+jZsPp4EUm7SbNnQNdnq27rylvAlvwMwwJZh6sWTcq1GTVUFm35NXw9JLpawDJ0IapjDAZ3GYikgEJoHWrIzJaeNN5HS/pRAbmDQI0rOjV11pIQEEEVH+PRzoYkRC7sDICkj4QJvteQFthwtIfJc2ds6NTMwArXaIRAxAr3pwd9Ce9g1jETmR1W2faHQDzBXo6cvMivWUK1fNA4cK0j/Kgr6+vk+TnlcSFm2+QIml1wblgyxZGbG/mVW8lWA1J3fK7mINz5KnO7SpF0tGGxU31mQOl+BEBzpIjKgDcBSASi/Rw9+L5b21COepXS6L3BVNSXQpmw+vk4fbKj/wvZW1C9wB3ptkkqjeTib2hWjJUw1cwntn5uDMoTRQBlCyyI+JHU/zJGkOge5rIG9CbKkl3uGe+AHFwPC9sgY2kRy/p15zZOYuMzdSbkjtKuP06/kJ9pJOwOd8sUevlkQr4pmp+znIqTnJTFLFk4DO8KwiO7jeailL7R1zzV9sO4wG9Nv1jhj+440f02Qe+ohwc8EBZMHT0WBTi/2HrG5/xEnl9/Hu3r3ngsPzm15IaJBIlOkjA4Pb3Nrec7c9YSG5sOqud+E33k40QFhvAlCC0OQsyIBPdz6ft+lrUJBK1bAYuTkbBTl7VLcif9DPOfiJzJY+vOkHHp1sw3rXM9aEVBPI5RQnYoSuTnE5zDCljIzpFRf/xIplca2O3fVtOau+kvUTEu+8LeoQwnU1uCZ947gwSEVTgltAV3F1537Hl4DWNaPMABkVxPIBW2ZBIdwT86u8Y79poxEOffb9KDJewFGMjEzVZuKpfWP4r0RGy33eyKSxTVWIaM2yh5guvhRQXhDpWXSuUkuNSPujIGvocvq7xol6TBzRJXdcSOPxZXYOrDyue/xKb+Y1NAt+W7s8AWGQjpsIhkkaFYWXZ06bW5F9FYUa79GLp1YY/tsqnhEwEgu2uPXDViMLLsKisSt+QZhaKIDIZMDMc+V/5uVvxFoC2WpsbXA4zlZYHpcqfD3MgeYOdLrqkNQtvKBHISVaJDtxZXVlgR8VgqosysHbrZ17g00ZDa9CulnlpE4DosvgjhDz9CbHx0idjVNwdzArbQyp01/fvmoRjeXEOOMAN1XmQYQpy510Lj/PbNM1zvBFGNaSAJWZvFd+lsU4RHiwfRIZwIqeQIFxid6lVPih171ToGh/6e8dpK98Lt3qUBFhJ2MW5EzQgRLe3KA3Bx17QwJk7IT6u2g+pCeZSOL93FfaR4bvNFrUl4ckaLET22DqJs0aldh3pjfWGjmIPzFTBrgWw+3pn5lgNf7Iqk85rcZJtLGUiEZSNotZ0YEyL/lLh1E0f2ZtCY+NuuVwY4FI8cBXYUQvizoVp4+VR0ecx/rok/6Fdcuydgr8kSHKLSw9grSquNi+f5HSY8xF4gDYdJHqSNLF8MgPLdm2Kyby3bLCN10sCQQR0zxPFyzEYd+hcgoEw19d25oJZcrhBQunQ2YesRWqCXZGY1angFICadwX4XOq1bsPDllaTGOEUEi/8aBS9FX4xUmiT3OYFF0s/7UTJ7RMei6pdBox27p5n12jCHAPNI0Wyw/Mq5n6WO1BKjBV8VxwOXa7C+aynACK/AGAs3gVoF5A8AyyLyRz/g6jzWt8ROKqVXHiZ9i+fsqfLDlDIPgQwSs9wM2x5plmnboga54Clizux1hjs8maijSAdNCN3D0vZquVJfFT34khchj/q51F+dwB/VZWVUsOkwgVkTxTtXpmKIky150yaXvKhDvFHTmJnz+5EGYOGCs83uQdnAUFn3nXcX9vCj8t2qt5Wgluhdyqw5/NfoIUDarT4u9t9ECmtruvnAyiCo4cO4fJMlzHae8NIS4tNxoATaDWt6eupORYs7NspRJQGU1eA1RW/kIhbXSWJVIlOFqim2tvETBPYE9AJtT/aIx6Cqfnebn4b7h6sYHA28V/d2yyWrh+SxckjSbrWFgdEZDigjgJYG3h/ecacs2r/3m9bV68PWD+3RWHX6+DGGD8T6earBkcPL3Gw0FmwfleYtN0S7ZbfiyX3aLGTMuKZrGTKU1FlMC7oOl0oH/nOXp0qcQC+U9F1OGpWHXMgTlsNPcm8cL7vbzYrxT0QOa3x4w0fqQIySXhQ4Wn7izR8+2U1KB7TtgsprxFgOd4w2kThqeKaixdz6xDqU0SSBHhVvufjSyeowYoqeptNi1KCtMPWh3aiXUsXAutVRHMGyKuZMoOo++t2uXTbnkv+spm2l4BDUDtB8PivW2fsELhGhvHG9KuBgFH2WX+5ZWKvj/YDpR170O89DgtBKyU285BKbUxcexqMY0mucOKWjxLWGpsAbdctGK20tHCMRek+vtHTFCSo4bqQ3eYjVRHIo4GjDCoTxbH4TNpm90gt/6WM2FFtYwp7GKslszf0Ly7Z2b1WrcXYw5hetinuSFCvA+XLZbnrUoGPh1lzvysHHU3z6x+dOBVq0yZWfa8w01BJQQaNG+kBJZbA6kFvhNpPqCGBECHwRm/D79gESFEA1lFsYIWN6wEKRNGKlR1ZNiPMufQ7L9ki5mLKnVPpbWBCUtA+9DvQ2U5mc1YA6hYDzKpG58Ek9IB6mxMTCzhTF13EyFCw5h1seAOuDaLwRhK98Dz6b2Y6CXzegxaCcCLlvGKjiHYSH0GzZFclGBmFW/gv7VNswN+1X7XP/mMjj++ViCtEJJwKTcf6nl4dDOhGO7lRw9HmUQY/L3D0Et8LNnWDezKnFh9FlAgIdLn4WHNEVDlF23l4d1hX83tzh77mxOFgW1paOm0Jo5kJBTq405m3RLDXUJodVYMYlcMHuU5TFYa1C4EYZCzTthFPI/vcNabgYlYL4VAvhy/CF26AJ/4lFbXzPjUGwgx9Rc6ffyXrFHz7H4pUy2yDnh9PFafgW7rcopjuruEu8Be6UZNjKua0Rm6aF2MnR477e9tYJdFKG6d7J3hygL6sxeR8twvfigV+/pgEjJssTA2EwnC1ZZUGbeTvLi8ELmBxSJIwqDfyC84lhFlsfKDfXICIR56O1rGZjJJDHbH9v2BRDWjk7dXh/9lcZwRA1CzZKt17mMRrcSufeflGBHUTc+78XLy9lckbJJnIT9bt0xQmAXlr/03ypk6iT7uKHXjHCN54uGdF+e0y78EW23qbFhg/mODDBDGgyLMhrw5F1X4ndh3JZQiF0d3zjE/awLFjrhZJh4mYqktqzCPA4MdJp0MfOIZsd8M/laeysdKytES69iyY6pk3h6PQsGFYuTLbLhtLpu/cQCr5GCapjhXbpgfhRzgxVGJyxzZ99pH+qBl65VaqLYjEYYtnnBInVtPjAiyPdquieM5OtgrFYC3qQLjUb9WcoUTK4uo3gWcAJrepkzqZQafcD01EF1Ru19UkifmV9SPab2RRkyi+Fdt1ENkRAkVVodocyO+g8L4lL/HcGn9qrMBoEO1eMgFh+NZjzAKYuiGujtqTVcthcJtMKA+f/1p7gMQz01tzYaAzT7gA/TGdtCVgIKizFXN1DT2fKCdRD/LOb4bHtQnMAy1S9qaCJjRv4Fclm2w4zZ2pfDvN/BHKYMs1DXeuHH3j1OKulavDkyLr1faspK6FE0e32YDCCkY4Om6HMlwSWyZRcoTAO3Pjn/FXDAMNHefcrFS7hfpADb0FC5lFlzRKSj6eYAtBraI1didUwU+JQ2AfsB3rHyM3CyNB+ShWlcedZKvhNMrsgfmawKP20a3Q1gyC9NJJdGcK/haeZYR6XVNmWq1y+c9UEoC9O3PYSrBKJ62xPvPTbDfxpZWs4enSGF+nZGHB1+7G6D4SGDHOKbj8T14fJAOI54g7tOyGzYECdMj0q8FhIiVKPyRCxeP1XKvkqPDqzvPoI+CrwXyZ8vR6tDnSFHQPt+J0Fl9uudup8wL1XjqYvZL+R7K7IMKlwsyFGf6u5F+qK696nhJUwFlo0R1p/1Xuzfk8oImwdZyXx8goN68vPvmmUy3xi7XkqzUN8hQ80GpJ7KP/T8y8qs2xmq2r99yE7Cwqo2ZIadimq4Ll2MxAsDAnGgIVyShNetg758CR7V28nxTe/QdxbhX2c56jkaxmG68H3tLTIJSx/pH+v4dOEzQ6mRruNEra0KkbZoHmcKyIglC3UYs7e/0TNEsKcz/XHFe5pZZL0NkgeFhOr7/aBQ3xtg0GT5Eu3uh845j2unKNeU/tls9SY5BSHQoY8H3frSIC+xIjp0lVJHkKmxYji7jru7IL5E2uGnasCYIyHEobLmIFaW3zFerMphkXgrD+8VcEFHSPptv5gdXhE/U23d7AwJvz/hYdpUveWCROvCSjkO6c0HdSd0cUJScBQBiI1JE8LnliZBPtj/h171jCFlFGDbLGGp8/a2Wwfg+xTv8hP7cbuNw5pS6exq4UxmwlA3LVSFlgb6Das9pzFYNeeHyoj3GZNKIj5PqRRRlh/C6pCDTPUcJcR4BFivbsGP4lrD7k/jEoPm4KoCkrLLfhIvxLgMjr0pozMUOJc5py9xgJfHDCERWi3jwZFTk9IcBnGSCeiZqaoNF+LwD6N7IM/ito0dUT9fwoZGjNoqWaEE+Y11xCNItz6Xo62/h5rZfx6gECOjZO7CyzS3NlU7/Q2HmPjH4QUkua4qCmhc1d7umhRlW/UFQNevkEntMLLnR38rq+S0rfe+8HfbtTZEaj4HHaG9YFAe3AC4vQejU479CMgof/786Kt4+b3uNJj53Tbfvhv6S/BG2PaUK/F7yDH6T2+YdjjQNREYZtVcDQAXUdkglHw9Om7Yeqh/gr100yPBJM+j11/Nj8dB8dEc1o0+VK63hakfuHYGbLG02mkIT8PMZegTXgl8/jstao9kIaFL+LAdk6w3ptkLEx84iC5mYx/mxATH8lsQF+SlUkPGsSeIW5iF4KCpNxIu1LFt7y1elAfJwqQiFxoWlGHZ23iIdfUGcsYrsMR0mGgXRBoznkqsrsf87xWi3kW+wlQjnYb2ZiNs7sUSdzwy99hJ608lggNtHOd8Uq5Q02JzOgjvqGJyKkVfZyisHdPLz9NsUsaFCjstQsSa64WCTkvfMzOw9m9IZcHUwaZfyVaw64oIJv4G5ClrWATtpxyQw8KAdjnLqZN7OQC+soKDJaJd7zmPy1WumzyR2CuMDZRc81J1xa5D+zAGKQw+r8Rw5URJlAJKpSs80VBv9yoN00NLpgWgLVF39L3OB46Twex27nTd9YS4qE3zIuXLYgObkN26/WJRQw+MDM4wOcXlYbcTPqBrEav8gOzoQ9opGUt47Fd3kot/I+ULK9ZdkAjapvMHLyYLujVcJEOU/F2kzPTbkZtybrFIWsfiB7rZS2eGj3oiHybfUfB1r3/tvQYw42o7QF511OC/oOEG/PoWAibqMfwkL38H2wpSX8UPCmpZ7NEg/R0PejOBVZFWOUJISmnU9pASTV4Szb2yqdh8MKvthQJQUBrnpBwhoGCuGqwdoOpAdcnfX+w1pImSHpvESJC/mGKQfh4FmKasTUdfsBkD8p7oA/AYBhTS2t9Ca4sAaBYSm18GdBN6xdM5iTP6PXvdK1fLN0F+tl88cNdgDMeSBY9Pf2Sv3FcrrwFGm07k2IS0BEWY7PVI0miklmwew/0CSj5rpln8YoHWpLlzqP3eGlcHqIMH3Zkf78Lwg5QyevsahyIDSnzrAtVxFf8F08ujbonGZiCf+FyZQrdo8ItEDDeoEs30jO1K02AO+r2e6BaxUmuvdI2kA6cAfOeYCqC2Pb4yY47oVKmYYZ9N0FlwNfvOVGk3OTR6LdSjfnUSHapr55O7Ft1VdX1m9j51vCbpIXFXmL9lrRNaYNRyGA00Q/VcwYhdaiFMUJ1wC8H5k+Jz/d9IcLWwVApHtdMT/DL4rO0hCoWnSaNIxsUIqMEaD6CuTTO0x/BDfEXgUBeVNRiEh9J7qQ9IsvuMAExFGSA2eohXYQkN2Y/J+r/AqeDt9Ks+sKMMHfZ5cCmbMid2qvRMSEwziGB5duiX+43IYvlVmZH41Vor3Z0WSs1YjF51TNAI+Ya0VPChqAcIS6RCKKCHvEEvN94DHT88fwaiN3DBYkO8wTlfFGFz3xCBjwZL77pjkS0vfpmWMHkdiqyN1NsykdMuO9ZAubUdWqUeb6yAXq6OxMnqDdSBrMMqI3vOXf2EfOCSDmErRgcrwnCQRWXt9mA2qLMK6k66XJXmaVXRTDxk/mwOrMRZRWThCWjT0+yZ/uknbyulDuCwIOpIwXWv19XE+CDJGMZALd/dHVWfib8XBqLKlMoXP2o4EdprMl0iUgnH86iYawwuYfasqCMW4Gzc0l86l6K6g6zt/sSdCM32s3W9LtZue3aYnCk1+wkL4XnPa5WDsYxrQESTFUu68VKibvvssKPHI+m49pNp5k4N7fgA2hf1IUI5a1vhBdCxpFciNyZ2mbnyIK0Ij4Jz+tFFHchYfKEjb4gUovxK5dUWv0/GHM9Dh0R75lAvdzqTLAC4TT9wX7PvzeiAbsToiJXU83Ov9DSCdchphfoBhH/WhpvsIXExK6ZmCrcnWEyGfz78sM66xjWw3/Grtj1ZozdGNwHCcF4S6B3U7umNrSk7wcrE/T/ewErBq1L7mE41/H/Zkc/yr53uvqh83vVkAoBeZnYoYAbSrNYXAaoXs25SyM8xhQSbxNI8067zMoTnviNE1sKYTRGIVCbA1Jse3X/esdFUa3kgt6om6Z/adovYiohI2hTy/O4sFjEganVt1B0N/xOel6dwE3IPnt7SM+t/zeF+itIuKWkntE3zKgMPZLRHub5sJ7Z13mWx43A9AAG/rXDsUSE/n2suHU0AxX985RnkoZqUNS/GYE754hLn9FkAugk8RzOx0S5oItkR/Ur1BKzjyFSFtuwMaSnigZ56oz9Yg3dF6XJmD6xhmaazaesW/h4oRa59H2dJKnybCPriN1TR9Mg3O1itnauWa4Mox5tYPKdN7wUqLwjz+o0y9aqm+APzYysCebavwyUsjD+npEjN6/ELH6gW5DXJk0WMinxNI44g7+fLLn0B3Wo0FOs3xOQj22V09VfsP4dRw6baLB8spPEhj/Kf+pJw5iZ9qk9MllAawALN/iMflATOxCtUudT+82egaSCeTTQO+4jE6dFVikXhpCe9NOlBrcZ+SnJRYVz2HH3HWQ+FFNIcK2khGdcwteti0QFYjks+r4oUJzXrRor1k++56g9xYcyy7dQaZ0P4zRQGfxRddBEQ2oyNSKrA3bgdMfLoEEwYbz5K05cSkzkz7FPEoF5dEmhK/t/HAfLZU3M3FBsW2+J/C4o8DBkRQU67WPQTFsJEFNMgYRxBcfiu48sYDhVdkM4AcmxqcwVmPXHfpwBhrhnoXOsFnhNaFPV7kKdjLngP+k0PD2XH8uWHXUlfG0hYsQVumLH+2306vVuOgFYxSKa3kHLCQ7+nOZSwAS1/I6ulF0B0vWA3XVrd9XRiHGwMKvOakTLiCG3FJoZX4EOmrgmTqpIDkpVX75m6qtzRo/RBeSHZi5p7euCsaEPdbjSwT2+bPmoZlLROvZ67Yz186KZT9ALmwkUmKKzUATHmtAoARaRe57KLcXS7F9kHOfK7Xb0KW+CkHg/HpRRkbQfQlw9W9CGWPgyMDujhcQOkg442Hc7GH4CK9mB5kjbX10pGQJdMAmYLn/1bCthrP5h+03DhABWXUDJHr8UG/nZnzgLNP3ItN8wuVJO3oPLpLIrTZONM3vBTrkPFbE+DwHPG3enMpq6g8PYGp594L/zaPBTL4gUenJ0CbyjWdMveQIJYGwbrWBHUwkT1aEeXSM3xSq0KMW2MS/xCj/RkOgrArchaSy7ozWQlqOyq9TcG3Wg6h4NdDnkkgvBGiQ5xIWiMUS8ldK6mJtbCeIOu9utF07B+GwqgyF6dViQ42p3AUPYGGFf7bq/lDK+dQo+svcPdPE+pCzqyjSujGhBBVWu+iiEussdNOzZXnuB3qp3DN0+Z9NZU2aYOWvjfJSTAcVRpMQt7ZP5c27Iv3uVah6YbqdM7I/hEhMa8aW+/8x35iunSfhqh03q/3uyYJ74Q+YK376kByi+iYwOcJgOj7JErkJefsdVKSgD/6SoXfyB4NqAg3DPGtdZi6kNGKwprG/HGhiBzFgY5stAgwYyUiJ5IHBXHOQ9o4ywVWwnJcimNp5J8eMxRNGH1r+4EcXUb4GT/qNtz6CpzqYCY9yF1QfilVQsU/AMkthsweLyCnlbpU4qiNup1UF55vcIU5B7/oTp/PQxp+EDLmQbK04AMfVlT/lMOLs7noNXmvmrSOhwJmfAsSBZxWph/5ms/ATZVdWDQnb0i2P+mSdy8Rhy7fakykCtRkRIhOH+6zztbQycZ79B8uVFRWzk/7SPE6EOYPdBfoyYTjCtjEMSEJs4zh42VcXyEk027qpXktKygrLh0ULe1/OOqQ7hpBNJ44lKvWwo5MR7rL1I9ZNde4is1EMgyh8ohW97owZlrE3zDyiNlxgbE/Z/a06HTjaD3cBrq5EeXnR/Fx22uPNpmDX05nO12qlaJxeghWAai8yFx/VSH5aI0IEG7sRV1lXUWKMVgx7Ri30qigs8j8f2pfepW0TTp2iHZI8771DOnqPitMqcMM/x/CN/RWoGYjxBxHtSgi9CiO2zFh/6Ujby2DFI8YV4Z/r6SILUSl7ek8nA1CO1Wi/9XVtivF1YNB8gUpvRefhFyYnZ+h8adQNQ407y1lBdpB2uPOTZtqA6Gk6ttTVdMTfEilpryaMiFyG8dj8QAUgwZXdyskvHhoJxoFMYBRL9CkqLm6DpPTBurw5y73IUUGe6gO0w1V81vEWqiuR1NHHcwh2+IXMunW54LZVNu36hDubDPokEqtUGlXGjfePpueipXwzPiqPcMcjwBT06c3JBQS0mRxOoOKaRty+fpJT88vSMBAnOpOyLDsgwx3Y9VAAGQFxFUQ27DySUgQJDIRGlwdFEB+pSNu+vg8Z/fcSBmbiABm/NxdOuVqFZY7mpAdVb1b4mg4oFTvasUkSPTr+j0KlHkxQn7iaezftwOxKDWLttWkLPuf9F11G5vlwXbQDm/OmhQYPsiWIvq+sqnuL9t75QZ2WreSWmc4Zp8MuSYCt9aTr5WtEGFjdJWaDAo2AUOhyYvYE64XpfygxntCDizBxHhyA9uRgHS3KIjD1pMQ/9JfYcBbfULY8zGgdynMUo7IHC3VqfPlXuBxuJFsqZ6EleAQAcCjKy3KfWh8DuiRs4Cfo76hpPw/Op67ur0XJts4JDmk7rfGrNpjy+63lopm/6WFn65zXeOABYLSA7zhb8E34S6hzBoSxqqRBFY1hpvaMz2gWFctHpaU4J9uOoDz3EJwFyyX4XpsYlX33FxYmKU4yGRIyT5OLYm3viEqMDm4an/GNPdc8ezGSZu47mEZFNk5yChhu+qVhKYgEwo38bros/WWpiF7JfvysUw4D4ULNOoJ/Abft00I9DFqgEcAr+3b1wHPjXWcsCF4LYXmNZzWmxydRvTP2RnJ2hy1hyk/9FBQuU4DsjSZMzzWgVE33FZi1kgO7ztGPcQ+Z2vI2sZ6uAR1GbeUytcyIn8k/uuPu8Z9MTcPYgIF3Dy7S94zKtLKwgJ79RBkqnNEbPzrAY4tEyjGXp850hd9TDmCRlcKS5GDKV98ifsrNpKNbcALy+sDd/5MfU/Xt2fOOX0VXKRDF8x1Y2HSQ8PjWPkOd5cVBT7Q7u5CR/1S7/cGEMZ0OByzKypuK4XxKwyCs/s8ZfFXsvDDfvYCSpOWKAiGJ2tecj8SuQzD6uCmwHPX+6T8c/9TzS3S+bWkzJ9pM+npPrGrBwncx6T3geSV8WxvSImoGCbmC6kL9r6HO/xPp3qUZgdlrOwE6CcMuYd2Qa+CakEOxqrg10rDxUMQB08ttXpIjzUxS7Vx/Kgvr2IeLZq1a0KWMtrAizX45WJbR0IrlsppIf85n5BN+3C9/CXqZofgMty+dRPvwgpvZbfJAUP6NbjKuT69FjIWJSmXQa42zgN1eR94lf//pCfTDn4rcE2j8M7EW+ghgG6sgNVhtDesrFf6vJwMHEbqYaYLab6zSaiN4UhCHGVdTYL/nzsk+OBvs8VWmBu76NWY+CcG1tdTKhXL36ND/sFF+69axSQ+LoZ2a2u7ZFQP2BdsxaAJxazh1+XOsICOxeck21SeFF/j3VbJlPINFSU9yWywDLd/M1AXaM1U/03Jvtv71Z+D0Mg9CY6OZTWA4Wnz+Pr4fuQ+8K7+UsAUVEPNGrsoj8ltRnbocDeZhucKhUMvihr/d0vLB4JhpmfoafRwFxghr6pVYJ/ZJxwnwyhOXj6YlQ2QY6LaA4XPMgxKTe1RahB3jtaYudfeNEqt9xVZBikHo5m+o+iPng04TIWnUVAQqwuO5IrBgbaY9LUVrs4F5ZmG2Rh5YwTC6k+tpCMyyMr5CKOrGDeX3ragdOoNPrp8U9eeM3zlpyJShiJ2Uas7RhzyD1aA3zAUxBfqiAtZ4fZgYYwi1aLi1coqRIhvyljJ7XaeodXmyIS9kE3rREjennojmJbnkU3h/6ijopMxK26jA401bmrEn1pHEiqLWWvjzI5vS4rchc2N4MmBcSBAT4j+NU755qteDSJRF1vYstph/cmErmBq5A6M0LQeZbDqr7Ai7hyxLQwvaLAiBuBObdlA38ir5xbQX/nY2D7nwBdET8B+1TLEsTbO/QaALREEKnzlTLLZmwIcOOEHVS7WfrBKttEbCB6/VWzi9PLFv+exnjNmcBmEwVrZPidxI8SSRVAU65uJKDj3PunS81AlvtJq7/CmoM5WvDzvjGz91YCrTnAfWbh66Kgb+R9xYE1yQabuO6rfO/whsuHnNI6bA0qMyTZpNduWsEyGbOSJnpqf4Yt9LXlnI6WSxdLG+5Km3DXc3dbXIdelE7nx1PthZRUPny3HhLkWURHqbcmR4hFrrGNuvB02K2zhU/Jv1d1Y9nI5GxizPdZ0JX1BN+q1dx2dsIhRhQELOQ7GL+xx6gpsXUHtPUcG/+TLq8kcgUy+qFUf7DZAaICG7uzkERgRv0bIGDUYImmf4ADSxQY7vlAX0soZPEw9n06RIBDxfpPbZRb5591ClBELxwXXm7geOf3xiLdK2hHw+s3TJzhyqs/Bjl0i6eQIHKpLIkmT+RU4o/gImEncvtczZ+eglUCJa29zaHA2DrU9+i/9sPDqaDbAyKszx5fc22dMU7FKRm74JSrd8Kh9h4jVYE0sCkrWRLaAaRULB8wNuUNnbfIPCTWefBbOMmXBngHZAslAXXYXrjSJxKzoSl+9RQesbVZ/liOYo6wrGFpRkRcJNk2+ntxwkWjTmvkTs9BMbAG1Ibzf+k0gjXmtxBGmHf2etJ1z1E2AgHk3hX49AruV1VtRS2Rs8+m9JYV2061wzTTz0HwUCMsvD5ADst6Tulg6LIn6p6syVznEuGldtFTUsHFf5s9DBop/g7Z/4nB/cgSIKLXGgD03gvsBf9NHYoXPgxQYE3Bjny+/yFLmZCQu4NNzrE24p2KE18gnxjlK+6H3qvf/XrkjDSdR0xgwBIfy9o0Kl9F3kWhUKo5vwxXgLurhogSQB2sbeD+Fdos8/H2txnEQAGIwFQRCgQ9qnUkPntZvx+e2IOciEMT0YXypkYEJACb1naSxg23rIy8s2jizUAW//jKgljk4Xi/eaTBwk7vc/V0yKaiMHjjDvtPmlH1RwiUcr0JCESat1JgEYGmRcDa2Cxr8tdiDIQ4VahXq1ozIwLmk5KK0uYJymZBWFSX4iglNP9gNpKeNU2qEmBFqyNYUTDwb1+OudF+uOZ8tXJpBtn5uM7odE2jAJUBz3WAbtPJwDzhcQoGa6v9uBUcfJIRZEGa6xHnp9bDMedKYKWXuPql1OLBIgrnszn1uCfq0tuyHBVO0o174PhS798lFqoa1+LYufGK/CEv6Y9TMxnp12/QbMApaviEGhudxDNR+TZ9ymvkYKYfiNDeX21KGIVdY2nZIBVjlG7e9vzTSCKRzl7F0Hvdu8KXNQ37L9CzY1DqiZh77BlSh9BNgqVZx6QYc8RVp9xB5yzPVBp1Td+eFfvJmsdwFa3NSAS3jX1UB/knvd083aX+MweF/+fSbnuX3YvXa7TDzVbHvtEslJ2a3ZQ9+xVkibeMs3iBP0Ui6JI0G0QMYdUhUC1poOuzVPD4NzsY2jbD6CcTWzb5n94tcJUErCqjCbLw57VPK1m2mAAY846EVCOxGbwfP8ZblCLW2Ic00Mc7ijfp7sRPfN3BBevYnwVEwjV2+OyyzB3dlFT/hE9xHKB19yl2fTl8paVoi7CXeTNYgLjsR+AF2doQCgTGXHSaMdI+AKF+TDMr+n9WS+UPEE8QxjrQQRLggly9hrjlWsRf8Khd9d+mszqBSdMe6Jxw+4DVxMpeNpoASXNCSWjajqi2j9j5qk9G4wXEnHvlWkz/dwK1vSVRzcwZr3auhuAPnOYyQ6mA0PoAApE2knTaFEsHAgXmbqDvrvaS9TtcSxBkt0H2LTCrtSapqkXgfgUOK07lL/RlKAys6h+hhmQtfNOWN9yl1ASWN4nmbQIk6Prcb5MEDZfnKb9nrHYfHnY9J8QWL/MWyVEQC8unAWLhcSX8fIpDt7UwLfkXU5RKsqCo6RocyT8u6GGPidw/UXELGy0QM+1F8sBX4EmQSzulyPrVQ1iOcplyP3oATBzZwIVSD+RdRQzz+5nHJngmaU6tiNUGXr/mhe3j/+6mt4kzMeRQ4zWHI6p/Aj9hnJ5gPL+G//GvRLTDiKN+jlkBGs1WmtFqWoKrGp9oWK+WsjcOQ1dbMD9aaXCNZy/39gZQ0jdkwapy1V4/3n6tFrncILJtUlDUDM8YGdqf0w7kaHMxML3uJCz8Oy63p50AThj9Em9yO6ZER56iE3An7OJ1YWQ3VO8khILd6a9Ro64l9h7Bhfs5L35rQtiw8NEmDwi9pO5dLRltx58sASOI+2SLKtHYbXf2AQqD/a6+beb7lJmgweuAS480frPNzuzOXNTAyiiH50KI98Jg63LHEO7im/9FLv6EDAAoFsZsB3PqXvI9iWXNwk6QxuVrsDCrHc80ZzE1ycDL9MN0KBtNcXccinzLYEkCkFDxxL1xi4bro73Gaa4hlxHvfNgx9jvbADX5Zybu3HYSuG1IUW6+GY9qkj99Oe4CHdagYCOMLmUdbFLTgD7tJrkVCO+zdluwEG4AQKt9s7L+PHWKe9DKrrh7xp0IVckzNslIN2RAOcHNg+K9p87/opNWfeeocbrRbtJwz5xmXFw5s2E1sz/Cf+yk0QEcOHWd/wwgl2Bv36A+NyfAzWw94Jn40llta8mgxhOYDBIYofywMhy9i4WhRBdrBwK5nC1AeRpV3wkoN3ZJT8Xyt9qBOHI2f4NFPmTOGA8JuMKPPAqGjo9Sn2qEbSHDi0tPKofeWolqGCOv5znwwFtkvHcdrBKYPihYqBy06UKbzXMBxnXDg4vCLebQwDma591LhEKMzbKSl3XkImN1YohydfGrFgeMrONg1Q4RmJfm8Z5hj7hjO4+A4vKhVMYSBGW0PTpXmYCua9PnSweZRI1n9pOBjItJuhEyjUm3z/Hh59PNN+m9TWS9dfhkX+zsiMmrW6lkQLJkAcFIt7IcvIdwVTYd634Q4Ta99RndDw316BskYAIx5yXIfuCjqqC1/A4DnxVzMhN3uD/vehGAGtzOw2Ko8S0Yj8wZL4g+bXjZsuVmv1J7BG+atgitK4fVNHQs/JExS8T4fRRgMKxuSaSXM2mWSQxTYzZkCqEsGrEjwcsayZYtSEVBjLAldID7s20bSq9fRXncJ7W77IV++P3oiIZMIEgbLy3Q+U+cwBqfnTnCelH1/XTm1ns5PqgOhmjYn1W+E7Sawq4QvccjvD2T9wRfMEhBr9Gg9ibCQIGSebMDfbPOpCaXknmQ9OulDuiiN6MwogQQiUQlmZKpF/3q40kxkvz1d410PUgI/KImatL9iKXm3gmspstTl6qZT/O0QUP7QiXqjDvZg4/1PLvOg/wQHzQyrhaSGrmGjeNcx9EZx1CesvmSjQE54UAjYcDwX+CaS4LlUk05sMSmggUyJgVQhog8X2W+7c91HqLt+eR8KVlkcxj470g+YNLMobn67pFdrOLmHCTLX0yEFtywCum6wKz0Vvx5a0DnjRY2MSKCuKwh583AELHabh8ycSLLDLVPhA+F6684sFVKHxoTYGtUcZiatSBF30RPi3zq+noEzMc8AXZd7BMfetTQYpuxBOb9MH5KwSVI7dMK4tTWe6+vciKjEBL/mni5JQA/mOtsR+oujpvFeJHUsI+gb+w0+/7yD7uAFD5bnZffe4nO2kGD2imG3j8s+ZPnG28AuOD1efK60ayDLSJ5fBi8CVA8wbB8IJscXjknrIKtvzNA4OW57wjbZtn7iuwAlLGX2WjF1PtbH754DRm5JYL0PV9WerX5YuMIa6Bg+D8ACG/wvA9MNC2+8qt2eTq7GKQ+pI6d0pbxZc/T9mcaJMHM+AFb3A2h9wCQ9jmyq+kFmBLf0gblzPns8nTBVIAg9t/xWCrKPkZOhF8zLga9umaMkEDqTb/bAVlT9tXqnLDcMrOK6bXCeb09hxxJIIgF2eppEPEiMvR1WVMa/T6hOShFHXXHW1+LelVmDjdc5s2ziVSQznnqVG8cFyaPO/+5ZErfG6a5TG7ZioMMn3WK9juNYavD0Uh6bYRZlwDhXQHwXuZVNiLlXjfs/kyOG3IfHS7dZC0rvxGUmtayZM7XWmfNIsvpiTjaNhuXDHJVTWPTirqH6cKRM3EglRGJuhc4BDQ4l2t6l0+Y3JxCoQfVsqd2Drg6fVIR8N9/VIHi+IfPRAy0xScFTT8SruD3aZ5DfkhMAXSlv6tUQzBgJfjCCUzgqCe1341t9bam4DQjrnlH8bpzWX7OE8QfocCyXJga7LjrVQT+Iw25LBLrMeFceal61TNTkJ4dd5Iuxz5SsB8HNUKzxiMkXTYER6lbpbPgZWqvxtmIK9T64fHkq26TcuTqBT58/norXfHklteIgJDQqF0pC5V1pKNxIy3cLcPLTISVpaeunSgzx90apCtqzl50s8biiG4iCrtiCALv/AJB+4nXWAyQzCCwOJGwAFudOq1TdzhScdasrosp2OXq5cJEt1r62ylfZlZ0Pu797RwjienUwPnMaY30ductACZE0jLpD5tXMRge1YVkf2pRlfApUD8P5D9mOfwLMy0f4lyd6ShZXJ39Ai4fGv11Sez2VhJbp4YE57o1g9A+v5AAJ/TQE3n1zBdbs8UZA+i/Cs/9TuqcuUFwbZ+bUFXje8b8EPXLD1TsyUa1TmHxWs78jhdeYEk5eMLwkKLyu3IcAdzIFcJLPgWf3l1cb1xJw92qu+6ki6qdDb+jwmOvE8Vq76EdoV9JrmXn9RbpFdvXJsl+AuOqLl3ZmLkEtsU+vja35kFnsrrKRGWcpuS2H4UqDp5E/eVlzgjIzaE3i3cVcSuf7dOm6wHlbxQVy7fXIrF/uT6C652wRZpeTQ2G0N5lEZQo9RfsSD6LuMrhX3+/nvwBXIgZJ8OdsZs5Mp8YiZYBXL8Ju5pTzIUX7hKM4bU8VbGB22iHDpMq9GIJN5wTO3HfHBQ8oP+wWgbE2ltB7+Rfq+HPKJZ7jgg4OvutXmVWOQXTn+Xdl26gL7FzdgGE918Z5PLDUdCbfrSJaicU6tiMmu7o4Gkmnq8x3YaROOeAA+AIKi/Wfi7rtb/5NMEnjrQNR/Sl+eT0Pd91sdcZEhlQeZKz5CKqgiG/Xfnzc+BsOaphICttmqKjXUl185J+O8ZOenzlg7M9Bdm4afytwOAEkU5NW7ctK+z4X50jkTuzE78bzAfQOAUVRiSM+9BHh2tbi47TIb1kSceFpHs1rn68cRIsJv7af8HSd1z+HVFsiWGmUxdGCGBEocQehZEm7LZ/19ElDbEQ+jFuS3ZDSrPFeyNFa1JBrUj833OPWKDyGu8jxJRWvix//rVzYRela9Y6rxbMmMJTcvkspRxhgK4pAbcX7YZu6oH68qdM7aahVjHAV+2MK3kSJbAQbFgADpXphDRArVTyZmA+0CLpNzpfTFcrFbJ82cjVcjZ2/9nFZ8mpL8eezvCOG1zLlwN7B59rNJAJ7Q6bOMHrOwGK7cZJ/iMQWoETaaNkDroHf27PLpdtvTyr2Ct8RCxR9rcq4me7WQltdaqLONm0ftfKsE8dxvvOce2huRdp9VlNJTJBt2iqqx/VzyQSgiso115n2XQi3ciRlhmgZoq/yN6g8drcVDGRdixtBuAmUy/dJC2rxBqHK66mcC2ZvfGVrE/eDsjI7P/iORBKyKy5LDLS+GZharg3bdTbALrHgg4tHW/G3sARHP6OayaNlJeFUxxZaYaPcR1XWDGKbsATgjY12splsjeSfMlOOq0nXmIp3blk1EuhmUJKbuiLnc+Vg/i90Qezp+Onm752cEY1qz9PnjYRKbIbYuzROyu8T8f6BGRV2DbWU+LikUTedwHKYx845FfpVhLbUOAXGGIUeDIGGKbMG1vN9qcVJESS0W3pLlwYvOvYmPf3+cy6YQJthy4rrSi5vYz6XWOcHSbfNDdNcTYfB4vWaaBIRv2zHp2W32pHQQhc9hoCB1raXMAgrcrLdsnC4l8NF5xahqOucz02CffYm8TNLJNa1aEnYWmceCZP+mpmeMNXFID1GaaCKPEDevI7xR/APwdMAZERboF9UteMhosMK8gTqTsQtPuIrs0+q9OObmIw+1u5XQJWnN0TZNEY0/k7qSb7ZZ4ZMHmqlsQQEi2ADGdZI3mxzkaNCQjlJGb32fUDiURXxLAuq+AIPo7NVhE60WKLNYQ336RuOmwFO1U1BXG9zptg1aNtBuWjX/eXdLjK9yA3Y/iwFq3tMfwHvjmYhPRejSZ1iV5H26GDaEVhk5iv1nFnnMcJ3yo6Pc79rVt2p0XBXQfhorzWGbZi28iDm6IJhPWaeQPfPbcv0KP+YG9RDGslU/kF+Jr4xdxSFkbrTdkINDHrtIhLSEU3EVhtgNCbzbHyHo5uwBhRIth/qr/Hsb0KcLH8L2eq/no8ORc61D7Er5Cb9/yyAXoTlRYrAEoHlqKbQXo9qg+TLl05H+Oc8m5WeEjGKiCIR+cJn5ljR+RcOe6yWaKnP3Xu/D97raW0dcQokMHGu1RC7Gd7vpPbxLXcJxj8BL8X00im+21j0rttXdqTeIkKBaaM/ffO2acQ824cSZ0aHkvHt0f7kRc11Ug+JsCLefcQJAfKx3V0H3f/ebrW2Ap68hsheYccC6r6OClwgMpFRExYy4fSAvNIzJ4RRJbGn0ZsiXWJu+G9EE0unAD81AxMQZRpdDizQqvTMB4BqsKtkS4TNFer1jFKvCoEDvisOD075ZdErDTqND47P6B89IE0yogJxbped7tOb96DXlEAMJagDLLuq0pLDNVENiO9aOV/o6PtjKGFKOOA6BHW5zuocsXEzMEkORj7V3QLs/i8fQSsk4vvzM3fdMfWEOyZqe+yKZKGppHh5ns3FGpiVuLlWXyKbfWfp4FjR6Z2tqFzdUU6K2hHkj3nTUeaO9k7E/Vp/dbYSDPQcab5JTGoBQQHo1T/WNDS18CqQ1b0h4/wlVAzMsL806EC3LgBq7x34vDOEQ8mXwaEaovlf7JsjKq360oh76qBuNleQ07d3caACYWHmiPKcxMDqdpb2WJUDYJ9i2XyZYp4/xFKgYf0kjBMFpom1ygkJ+lTdf4ouHi6kwRVir8vVib5PxXaekzEYkbABZyt6shbfWSz3MCYvxF984bKMtHF+GkD4LifH8bjjeGXTMkuww/rT/LzSmR9Ey+ADHUBn9K/X21ixrM/45t26WgrGsP9phTTsGE09R6Y03aG/XmR5XN97Fpvb2kKYkq5lZqeffBbYBvWhGiESCT46dnxR/tjQQaCsT13PfOpX94AOgrXZh4GCedREofswwdIOz6QHS379e8cnpiQgSCFezZsQd/20Td+LkTEuvXRA1hhKqntgc2kRp/W0wVrBJYntMegGKMfj3Da5GeFGGqmBtGQ4A75mHN5SIz0usGlQfIg3IaAaLF8dvGztl/n6osHacSWRt16LpCEUxbpeP6cMvO29v9QHfjT2WNWigi1fyBxzgB2DV9uvzXUBa4AMhqptIwHOivPPpMwj1d8kf59CQ1ts4u/eQFnH1vJtN3U27D3lb2p6i9xM2J3zwzOUFxifPhJ65WvpAUx4Koc58qJhBeM1dvTlevTBkzXNuqyoMuG5cFvrAslA8o3hL5T7Hr77XvMgLWxFxlqQsGz9yXRx29C95Vadvc2qQka4pFwSyLF7EkUey5mx+Z4D5VdlJCXO1IOE/o/kdgvAe4FgFW/ERrINzX41YpnWHcvZUHTM3R3hGTf25v9aelESE0XHxffHX7gwGTek9PYgy9hdMispkyFzV8WMxJmOUTOTxWVA5/MkTjKiXfjqppCzcEYaIB1615p4T+n0ID3TA5zqCL+6I0kpqcIRbCuStbDqHvsEoEXV4jxRRk66+1mTip7cri1SQ/jQmeNZX7BIF3nLpeSmCbvSuUm/5K/Bx+OTNl5OAMK9nZDADC8OW2JHW/bZo1LjwoWkXyQhHauWfnVNmsq3LQoylZt12Cy30x0tfYDkrLYL/DsE++O20ytghPdOtACXUFSbcdnf3wejxJ7K8vWIOFY24f0dXoWoo586MTJdxmMGO7N/P9ilbKbfcvZ1OuSYtzdkyIrWurNJ7Y0mUiV9NTuaSTCIaxncoB55AiWWdbyJscSRePuPu1MU6AJaxYYbc6gXa25pvIyc3GCMMl4IRwKRq61tUOwMEs0zOnDNcyCMmRLmTez093JaxQ1M/NCEfxYMkm4f/FlJ3rSOmkUCKaUvAZ7ATyTwqlDmPEUw4oeGviinZcyPnsVAM7RY+0yeMe9SPAWiPXr9QudE64h0C9pNetTuTf2SMP8dayrYhOMFFgclmcXz+ZB3Iz6cJlkXUrpIjDl0gWP/e2OS1bIo5L2n4s810tBo/Ke3KrdQVGDlu4U2/xf9G3biwtKRrL5AdE6j1Mo6QX4aW5m6eFCMHGPbJhMQzGQCUXvSiVW3BmidpjUrTJ3Er9JoLqtOb4dHe4nqLl1lKBA9fX0NZXdOIUI/eqiBwIgiuHOsu+PGg4+c8KHX4ynxmyQ+kEdt7hkl3fTLngfotrdMk+T+Swv0T1V88GB5BOQNNOMhPMzqFhH7Se8o2r71r8x5f3E4TixVuj2uh2tHiEIHvGWL1ntItn8hoa93+3TbhHKWLGmAakHX+rJGTXuhiq4smci+l7Vug5LYIA/rJqOTsw3W6KO0I2FhCqmOCMPVALqZbOTt9vRf4IbG3MzRVdNPJXjeudxNBIHyrNQOztd392GqmEi0y26Esi3AJKuZfJpTtoHNfjlnhh1NDaq3YFnpY7R/8zQgyrxypKOIrRbV2ZM2XH9NI8kx38qAowscrcccsa/IzWYPvLevCOX8V+2EKTOJ27v2kf67ATZ0pDMMHkqIK2NOLt9LxCYmpX6QNPC94H8iTbyA7uruQpizec/ODZ8RB99w+HruycgJsCzkzREBl3uHk521eZU/vfsfJilbAL30CcB2G/rMUayF5lrXn/r5+tVkvpkQT61l6ureAFjqAxQuf4njRHq4hfzav53zockx90ITkhW71efF1IzXMMGMcjXLF5jNQRpmfEHH9ZyJXrK0c6ljlZPfFdadh8JNMtH7aIeUfq4S81/5HxCTb+9xODS8xGw2v/ut5is9QxCM9YVff1K19nxZFty3jrC6mVBaREm1sX+cLpSU+oJfUNg7LxSKIpNWXO/pl/mgS/LcuWCyzLsMl9V9NSoMq+/P6LfbTffHwkwj1OdsBAfj6ngRcj2DEWJjNcggZDQ4DpaaviAth2wuGinam8BTQCuUvyXPKHNb44DRJZd7f/lg+myozo1d6n7uyOrHNsCZC1pEjngEkr1C2xQ3PpzouiWX00hRzF8cj8wrTqu1WTqi7JZRIazoATOuwJ/SGFzDUqobuNImyzcYqeVr9j9Zg9QhDb5p4V3YtRNg73UhOqGy8k0G8dFQwjaEtb9VvcPLyKb9zoguQ0VSKEyI/Y4HYx2+GCvU1zzfvUjPmxtic6rffzlATW6ogDbfDQ9KfOMNSPFiJ7sj2pIX4AcEeDKNqy6pSokpKMjrz0jR8EzkzoiJRhN5lfuzO42wBBGDQTerO2KI2zLmwK74oROoV6jy9hjo27YH/jNY4U3Q10pW+gUgmSsd5SDGrtQWOaZLjdpLgA6rxf/fzs5NDnSJRxanTelayAdq6nCiiNiVQbHp4AJoAujLhDWaFBiZ37eDPIo7H9W7Eu78WZctecOxpvskkRGdgYPT3vrKTQABia9X3Otv/Zoz5ChrGiTS0VLci4EmT88GYtXmtTP/8hpHECesMkYZf2HnXEDiT2nF1v4bTPG+uJy8+m0FwgCvA2RX7N4h/kcfwsJ0rtakBm1pXN+5fwpiksgV9IH6DVLX9nVxmR6T+HTkAcBL/orQQBhs3QKfECx0kFC66pahfzx7nc3FUgfzAdbzFGqyAaX7B5UBFM5Yq7GwLjLDgn+W44FckMds8jJyqNJeqHWf9ShRaR5aabkWJFFhoKNxwRQhTSm1lcB/LMqgC46Xl1NOTKVbQkkPmvewWdYXqF4poau3w8I3K8Gfnv+dvEOW3WmRaDhfpkDwqm9Z6HEWTrCU4zc7Kx5ZGMuvCGk0o1jL6AYhoNnJI4rDF/jH+ySs91cs5psfOQFAVtmKU8qX0ItCoONW4RnjGaB1REoVaAlVM4oMeMIV3KHP6s1JC68CECvuu6Ql9ybTSW5Fq3SeE9bNfYUZgm697lr5REgp5nXOSGzyJ2oD/pyknfNy36wBO5FGKXTrcKH6Fi7QaxS+Fwb8Gsu8GAcBZLvcKkEPL0qem85fSsifHm0cFTdY/mYF1fyDaCADD2Np72Qebx8nGmTpfbSQN1dI/WIWJlE0Oc6zW9rDWWG6Sp3/cPfk5pRaFnVoSd4pWPKHUUZ9uyF+z5bMJUYilMUJdeVsaEXrivOSaEJJeSbK1Jk2Fw+FOFgBNLHuavLmHQKYXM0KPoMO+zbW8hB2Sf2yBcCejvFgUPpdhnI+lt73Ii+pj8OR1+7+ZhqXcc70QYe1yJQr9SJWUrimea7DEkzXg31jfQa9S+Eg4s1R4jz7mFfTV0E5zCuJKHcA3ONR3rRW6fFW8Sl6zo4EFa0Z9ijcOp8Jtx0b7UJAPNV3+d0QCHh/LLd5SoDFYjslAbPgdvbLHS+7e2dRC7EJsH7Fbt3ve/tWYjQZgG2iXjrwe4X/NoAn6jAkfRn3MAwXuFOZfDIYpr5gSOTCShwhkqf8B8pjjThLU6E6uvrTF5zr8qftIfiYYtk8Q4FCUQHpWAboOdIRXQ1Ma4S9Gl1ejqkHESErS3mprzlC8UW4t+6OQMb5dzGCVRh2npgYGwKpzoyFuYyjkfOvbACPr3Wa0Z/oWfkfDOznLPqHtWqxjZclvPHAqxQImI/ShFrn6MiVPr0r07vB3WuXa4ODXUTouqv2l0fwOETQCUH9xPZtGs+jVSx202DdcqzoYc4azwSDVXeWEcLSdocp0qEAldxbZYPkVczhfWk0gyXkIikI+QrrNEECFQgHnbWHrEqFxmhKrO3XWrhN7gynBFdJSWjwRSuCkEOEfGACi36fFJ3lCIrBTWf83OjTxizF3AOpWXjriBXaGiGtiEu1XAGOV4w/19IccZZ6kcuXJCLVBXfzqreTFLK+58vyDnGlNbUmcjCPpzF0fLbeSFk8CE1CEgM04KAXkEuC+2oF92DvGTU6IaXrLJMInne1COEDly499+c6k4Vzvkul2RiE0JBtk998BgKojLZsW0Jo7Mh3kKSQBSIoCP9XZSEKDPgrPHAxr2eb1SGYE7kq5M3YrJAGWuqdGZH/int+Q0uRyf5hcUBm865kErpAq4ilKc6T27b728vncWvk+7+z+Xtg0iUKup5h56LC0oM8K+p2XtPBAYjsuZKw3Recj7R7tEaAffIUbMdXokkqZgvNWtUVki2mvnYFAXcx9TGKKnE7NxZzjY/bRZEsG8pQjNM6/67MIdePBsKVMtK4UPSMUnb9HvOPJsuRwrI6QrwRx4xuM4HvxL4cVPnZLbfjdjIgo2zfHt7/v4Te+SOjxR3Fs1T6sV1eRV9Tssn/rT3lE0DJgqHEDjHI0b4qkGy0EmzMHYTogm1eY/fT24ZL1ynyCRrU+eybhyxXW9/unbT4jrAT+vR1yJRx+JeVyvwI0hh19ygVtnd+luoeu1wV58edsb4i29Q1dyWbJ2b56jUOPBQUmiNOezV9dZ1/ewf75Ss3OBli6CrM8/bLlx/xXnNMr+Mdqr7BnCz553wWpVp67AgAO6kLitfGNNZxDXBY2TDk4KT52VZsWARqH4ILD459JF4ojkYFETVYBE3XnvGO1MvWf54xboJMneEP2Id3fpMu+5cqeeQPTZwyR4Hg3srgOKJCAq2EG3V/zDKmLNJNIZY1g2wWJX+UqZUPTOEfPuDHKgbd8QOg9rd4VZl4zcp2c52qiP4T0pqfE2ion+szOUZygMiAaikP5Kr6QSFqjwChQoIAbdXn5BRM/QdaMjMulliSB22ZExC08vbtkxO9zJdn9lKuONScqpTECnsL2u6bIB2fOpEE1yGTmgfP1RLFVkveUGf7lUgE3FQe8xHyDuTW+Isy9MJOhP4GB1UPWRROPyt+hVMDQI8ZjkZp6uPXSGjDG3y41M/M35IuKeIMyKvrvHVTnK5wk8QXRgUMME6781I5oOtpaoTNUK854bOHLbbECIxKyri29mzuyZs1Il9YDXk2xsprQmRnFPhZKZ0O3oTSBRFjluD65LeHlfOyerpDIGGMLKJcRcspn95Yy44jpX1zus1xpYZW2Geb5L2YK9xB4Z+VwBnEmOzTZoSiQWk4BEz7HrLrpgysiWTNKR+oJRl29f+sh44KOJkmxePQXTHa990def4gWMuT2VQKImPRRUgz5C6gxnoVvzz8cULCRcAx+HtViWefigY1TCv6BcV+qz7wtZxKR1kxSg/IN2t9Rg2FdbE6nA+zONgqgdKWp7dfiYswcLZmpz47/60FxOza5kcXKOF0iw88LJcsfeiGBno9H2QUHVaYn6Jswsflli4V/x3IQMWcTVfxsevQ0vc35Y3iiIsDo7fDySkwntvGbOVeqlk9VmMCaV8DvfJtAj0a7q19sUH2l4/bu52cVlw3oaRZxERviDCe/7Lzv/8F+rzkvJZpysheMPgv7Ng+Mty8GpkEuPkLafLvUgnuO5k2WyROWiq0OLrDa/oB4+msQfUv4bL9lnFvx95Gwam0NYBT2bV5t2iekTJypF5wjYg/gFeMLm8u06+N8wZdXawLP0ClMgDy1PTCMBrOh7aYkEuhcGZzvy9C8/vhcdjchx2ZnWTfwyP6T6u6ha5T4iydn4ZWEdSzNgVLkbVnfwCOfoBP5O38DMZtWKSBJHkcDBJJKuxAUJUF16CL9JwgU50XKsZZsZylXaYyd74UpDBW1+kRcBzJZEKxVgBl0lMmEcjjPRw2JC62W0APDUiVnmkrfStgUFY3l+AHU4yYDoS0cJFCBt+t1Y8v59kMFqbnB8BkRHIs9nmrZy2QNzuV+7EqZcovs6HrKT9apS0q1qqwoCb8+EX2SNGWOrgvNzmlIXoDB6pVYJXpBt+4wyxM+rhFmRd21wA32lIGA8ApDhDGsxkxCNbxlQkTHDR141zZr1QGqGv82W93EjG0I2JLsD+Ac4dYH7bz4sQ3nOai4yeHhgAuKuhF9bo4VzUPVPZIbu94V/XSUjF3nU73p7kx3zViP7fPswxFG65f+f9/AS5GcrXRQ+JgnrXyBoM4SViocuo6X29xtJBJXFxlbkL1IySe1KPJmA+WsJoAKB507VmiZoQLcYscnSlnesaWJrcQhYPrE5RYtPeZ5rIV5N4mfXzdOE8scb4HQV2Cw7bMwJ6rCtrHJUPjir1v2vKe5nmKKTid7Gj6z1DTgXapsevq73UnDoteVteZEOXDhABycGXxHedVspIhPcXe/VnQBCMQ26hP1xQeqtDx3qJy/qSLsTtGUJIT9Vlsd5rDXGqxQkAEicUkl6LRbGD8v9B0Papvvock2WELPqNxTSGEkPKwqAxuftEB4mrV4vEjgPwyh5dLAvbe7jnphJYsH76ytIajYiQCZW74UgSt081z879XLDDVlsVscSVBWiThb7tqA5/4P6IVxQ1M4IT9xdwCgYeRUJtL/3KDnD2W80wu+5h0AFPnamRQIE2iyALAu6EiXIrSqmh2KYjhZp8MOlu/gKDeGAkF7NxmeMKqv1AEoxiHm+4X/WHPHPFJgA+OMYCT7TbaRCf+U5GWEODX4MClk7XErui3FUdln/3ckTnRJ7G6SPr1r9nPr0hSdClGTqdwTp0zrexrb+XW/aWK6ovd2iV6Y3K/ekHZuYUYafLUSHISL4UUhVIwsV2fhpp2BlGP6ADAr4rgiRWlW7jrs1rqR7C0IlGZprKL0kAKF/0aPI3u17Hb9iQW5DvRT9eFV7Xt3E+2GdjggV2MiEoyEzM5J670WwAPiGvXQ9mOk4rj+pJ/k4Nsovcal2ppE3rW54yiPzrFGRpvDAGHYBi+5cYZh5EULOM7wdKJLMwqmYr0Cme5cYe75+GB8gNUHhLMpX9BzsLG6Uv3E9QDi2vPNeT2qfMDyHP3ZtaMZ9uKBd1umgC7Fw46NGq+WIswbpPAfgkSnLLKIPiCIqkDa0MvxpcWKN3583AXPRH+ZFhBjydbUtIaH+7Io1le+VeCIJ01ffRBHgAf6hINolwdO1St9S0XZbuQP58NpFRi27Me3+P9O0tzuHaPlYQsecMTyGpkxxaIy6sDkXMrHvWeX/BaY3byzhSoSTYYuXU88LvwA+G3Qbpt9AeDD10dczEkX8BeChWCDvc6s0mXoT86tJrLSWxkWd57e2ORWc40ar2JhQX1JDahPinG7ErVQjBCueZl0DHfKHMx6Dy+3unt+7Ie5Rbomu3H89qADuAM9OzgobN+OhWXyPoRK0n6438GFHfMXPEPfKS9C9Awjg5AHT52h9NMw2/kgWKIi+m/3dNO+uT7xc/xMOLu1TAjwMtW+rQOPOl50xRjBt1Wc+gADWYWBczUQqDF0jQ/DwVfmeCNkBLh7rBIiDteeleEuNQu5j6YxpEqCtiTPEPxLRUdStD57ypDVKK98pVn6JvUEpz4jriCDyO6cFgu1ahdW3okGi3LgrP3eGyOLQJ+hPDiR6Y43c6hlL2iSxN4tQpPHDK3IE3kvd0+yye4iFulV0r3PE7eYA2OnX0LJtjR6duwiJUW8Id8rp9TWs82f34fSbi6mAMlu2S+jUmGc/JagBG4GZwKDrNJ2yVJ9kks68NXz/O4gupVy0Re2sO8Lsy3raD2hEYhR0c+9ywbD4LiKPYe0kvFsUqIgNewwyLx6EiKfLi6e7I6JOwsPAA/2Oxr9P1DCqltVHm4RODNoDfXq0Jgw9bovsUIH4kpiJv0p3YVJLNbWz0NPFlsEAFGNoB7IavQ2F8UWEWMoLeaksRtXOkpHgX79roYhowpSchztUdmvc1/dJOeMQqIbo2/j+seDfA5dS41vseIpNfQEMY1mhwfsVIuBBKQGY9mCVua5hQaWROYEIBu55WShVBokOPEhc6sxnWfw/7553t040qmwm6DjBSJor43YYhxcbkUXjqfStexurDUdJfQaNh4OkpjaMhwLoY6OQHAPnIKAVgCS8jXRTzwOS9zTzdEtVjDBgz0RJqc2X3LYPU/Gz5AU+mTm+4iJ36CS0KWbRP/7yhHI8abIPUtBWnXEHC9kh9hhC4cDg901UuBiXGBBvyMfUAMTLFmjoudRYi8+0V6aXpWsjAEt+Vr4x9XkADVVx68+v5HJH7ONNhB+wEdi4A5KstwiBwNueBxBT3ktYNZyg038E7hsglZQeZgYUhPr49X/qs7y/VXElsKuUjXAcIWUY8ny9IwIvib2weHGYIiezHSsaEDQzarmJO2o+CgvonMGagPlMhfYaZDHRY1ubijQdszXvfuSO+zzHhiSC0ze2fUMhWo+cr1xifq/SuB1RscsZeBfbI4cGPOMOezhXc/uABkpfZOuKxbNm/YSbtwx5m8op//mtDV5RIBhfuD4OpXAZ5cAwQtXk+/+z0RPSQmxFLDT4WhlB8t2BvMg+vg+X/w1AsklZNejOJ3XvKBAUU7M4/FZnsWAZ3Uiu2ErCajJuet0Yv7vOKYBLtiU3tdTEUAJ/IHDxF+nKE2Ele14ophTmILZhVFROKJzE4lEsB7Ikj6n5MOsiujokv3uCT83uSWMvR3IZJDdlgDvYoyp4FCp9H5SbAmpGoEbP3yntZH5Bv2BpJqyCy+YLzbjpDGZJNGVWJl5b9Jtgp7IDBNawkHGHvLY5ZVJqsLnqQeG6uNu03PfCFDftC+PlS9KLiQirfuGYJAAZQ+8fD5ElZsSakSx9gxPYmsnLLEyL7rdSZnAn9jf8cKOzTN06/an3XOnmhg/bIwpKyX3fy9wIvum+KPlQXX3At14efc8UE5YcMVR1K/xCWsJqpCU/8kBM1kb8fJWx8rpNcb3uEt9+FDfEoaJV5lT1V/ypbmz6sZu0J1Xzt4juV5rSknk45kjYBNIGdC7M43Sfum6v1nAD5MYFAkjDrWUSgC7TGlTz5ffRALwwhi+N6f7VV7wKmDog/Iuc3i3t4synsSmXKlPhtDV+kc/rJURbk2o7G1t6jvl7S17Q+kmcBxlI72KIsehANNAwNhqa/yFsftbU6oasiIRvZzcQDX1CKbmneSUNjxqPIu2fDoPsUzBcveeOUdGIgvMdz/PztwkDGb1tOnT0g8JPGXYpgQhRX0a1rt72lWEECDIuGCsgIl2SO1bAxgPB2HI0yDiFrnezSiDFY+Ex3fl+PjUc3G4Ptyu1/4mjW5FtU+sDbzxnt0wlyIxKE4VRcen1+wt37wJuD1+27CPQhB+YnRSfSJiYZyP/aysRL3goyo2JsSNcxzHHg1ulwPyB0uHOPWBVJBRmYzMxwCELn2ShA3uqwDGpv3RneUS0vrnyCxwFa7PLkjZOd/YGLFhxZQVqRXzns5WpunBMGDcN9gV091h8Bicd0IektU7SA2OfPAKkrwT8gF77QgR2jSjb3NdJZvRfa2Op4+I2DogCLO88gHbN+TRhGm671n8vhhuYegZXGUhOWXggDwuA6HKUf4epkb5RZ5R8scZOdU2WyKcw3W4lpYT67EHpTASsqZ6GsIIa7CniZBlLaKxroGl8Op0NLtUm88xggyeUzr3CV2/cOVQw3mi9+rHF26B4uborzHGsn/NNbEcef4v9NY3WAmfPrnb8nM7pUIZu2Rh4Uv5DvRo2AzukyV9W2fzBpY9BrhLUK/2dfwFfte502wYv22CHAlEpVmJMo8LieBLoU2dzT3E5w57s8wnHViesk0cO1u3qv14fKHOMHgiDkSNLgiZYk6EZQSY3bo3tIjAr5X8WeQWwsSm9jjLdD/IkLC1kjfOFE/roP7AFEX/vZYfyJlkAcESfITcXZPWrs9qGL7WwQHSRxNZS8eVl4FIarqnpI3iMKgTf/pNL7tuLgMEr+ef5EIFkuDKW5SaZbi5Qn/oFOaXvWeItZ5ufymevXfzrzzqFcZhpHUdi1kRh18+p/vi+8oFLOFDpsUFsuEKiRYc48SN3cfQsOpWm96RQOTDuR9b+U6OnNcUScK+qVqHnHaYDki8zlgXgYD87pbBgfAztUzQsEekseAJaa6yX2WWvfHY8oQy8pEfy+KUjRNeXHu+CS7M3K/ZXJtGgMItq7utqvnd4c/v8NG0HFgFp41joO8kekUyyZaUFMUsOzXF2D20TZaCS9E+PH8GJHgcM9izOqFylGSBHbfCCmKDlzRTWRPFtFYAA9ilq12eXOl9mbf2CUnIBxjCekz58b48MztCVeXyrrbTnojtFc8toVeYCh5Dl+uHLcwN51V2ksEDeNEf+vvPnGfudCHtYakNC0Lg0NarXMVl/YPnUu99DKX+dFut4X77MEug3LELZmwlpSwuVu5uD69jlNgePuXB38mC++BI8GtyNOrHl3x8kyqSI3Ei7F2HfxD/5RYZwtVam0M0S/NhYNptsjLFIIB6wLgCSW2NXqf9p6C7MNWSnGuMFRiKbyOAUwumTcqjee0OOM5HKc1Yx0Xpag4ppFvgDwTy5WH9d1seMXxibmAQCv37GYAdhVAqm7aVHVQJTQ54qWdF49aJyEehyN21UgifykRRk+3Yg+RCfEvXwS81Vbg1v5MgXEJXUq6YgOmIhsIwiG6CjrvWSrnrJowdROuOd3VSO7FG8nbX1KkvCrF/G6mFyxgnz29uoxAZhUCzDNcuQqyxHDuRZPPzAn7BLDme2lYAIQtzUN0PhsjF0YJNOH4R90eBC1HT+QxG1fsJtB9a133Yv0MToSO1nZ/tGDnOJlB4u+ev2XGRsH/vuSS+SUjXRk4mg8i7aFYvE0aCGmT1o9icHOIjPS9TgEy15PL+HPz/1LMZuGAjES8lSRa8f5gyyT7EubWgytScek2a7AafOYP+iDwPTFEXDTVZNC+3c8Fwzq9c+cIL5m3suP8gaRv12KSI7N5rgtiUzMDj69fPNEWHF0h5fmMFHi/B/ACzFEcfPs+x+WgybgYoiwgUq6WkeJnt+TCAbG1wbbj791GxO1oijeefVjB/zHLMOYR2h7sCIzkYX+9ucSXPNjkKvQbmqdLwKmEmMfU7Su/B4F1+UxadFLUFcmnz0HFRUDOfV7Vvxx30EltC25lXI97/uLucbLplNkwmLMY6jjf7I6re2lxrEnO669Dm9z95WMTisK918swaGRvQAUpvhqClsqGVbdQi+9LJ0fRqNPXgQ/0VQtQq1lD8wKO7BkGxY5ftMWrMRbPRu5RSZIkkpK5YcR3ycuenzoBa+QfjccUz+hzFPBNGkg94RzmRuU0l7K5Bt1f7+3UeoFOA8hjiVAdlcmAFA9/0bkv8WsmvhMtqi5U40Cw0vn8PRV4giYTjxSayO8iU9e3/pTAD4TWEHaFpMRod44uaxhfx9osX94HB9dHxVQL5mRMhVX+8e+0AooY0IsP9TC2JNsIAEu7CG/4rSWSlc95QgPKkOMd4fvPfNjeARXwtuW1/l0RG2gprU/lPe9ExIS1i6hj9JDeNixmfBfR2U6IuVjWZHLLdTCRKIO9wB6mdBK1DiRP0y2spw9PK2RmYHm0Kd+80LmEaCBDimXJJ2tmjdFD8G0HScVJCb8FkhpISGafgGVxSZnrAMAEyLTKuRPBOxMmT9O95PFADcn4eg3lWltNunVLIDonylFgKJXqtdUEXyHYIub0ThaC6rPgMwTGSlth7plFGKCAwFJfA5XtJCSxfQCVbgJ+BeB75wpNCF7XyfQIXuL2phBKhssjruX3hsctxUmD6HszB+8LBnwZb4kk4iF6nCHML/BZnjAqCeSYW3fJSMsUX3UmknZZySv30CvYqoHZVvyxMeN7fWuFPelSgPps+vhn/0PUhdUk9mLRujkmLVNJn9/+UuJYy3+DXZLU1pKegqR0EGbepIt8nZbIRhuTsAMijzz7l/ZO/Sy6u7iv9leU1BEIpk385fcLmy8b0L/H/UEkJhoXW/dITum/XExV9yIxVprTVFrcVOEK7irO9WslhXHtZj/pPm6+olRvJqAvl/Z/dCTfLiJTEXCw2vgKMaubm9C2qYeO09yC684WkX4Ik9V097NQZ45G+uCjLpefmbp0nOPT6uS1sfuQK5SB4pVVNsn0leJRgFh0em+9A8zw2GtvuM0w9GfWaj12Ci6Q+aanWwC5sLsDUg+oSxaOMMeZmeC4MLqcoa3PyCr0fte2HZc2rgzzBWb8OmXJEDG6DlCj4mN2gQw6lSov5QPp9Emq/DvLRHlhIu03ci9yV1yqbl2x++YhmiLZtvfC838ouYci4CuFeMuDcwE+RDoduqdnu7GNu/TsPc+NG1xbDT/6xvsMqQ99ufuZE8q1bZjQsupHiyx229QoBdFEjtlWjrrOuFW5D+zpDhOaZjmJqnrbjMor40mv8lHzefz982jHfR/6ESLZu0h2F8VLzxrVlaGg5uBVNn/+VVEwVKpcyVotICHt+tzNUGazQOu5gTZMniPXpzToaoFDF9dAzUFFC9JRU/TIN4K8NmxH87SaSo6vYwToeUsFpQCThfu+1MZuh7bVpQfw1Vo1RZdcLOnQMz1R9eajV6SWvkFK9JeXA6lkmCEEOMOBoIg4gof5aQmvuEG2gKW7nN5IbKU8vAlyAIx3vbnHqfgVpdwfZFh7pyDaYeUKmfimfBzcR+DN0CcFRTvhyuUtfL2xzOLRWaln24X9Afc5UYk+ifvftAsCDaveNueoRqm1vOsNirkwbWbMZ7GFsrC4Iz9E/1564Lyf9qEBlHU9jKPPF12OgCN6hmfHNqcnWqQkWPVOi2b8cwXjqCVrvrc7EFVWjpe8WO7HJDZu9R4A7szJfW9PVfm4O43YV29KZofzMFmN6V5p+LO8BPbG0w2SS1URcCicFwFifa5OTP9/b/XfXckpmdXkKRd11Jd1TlldhA0wR8c2Aqkx3+AYMyJOPjHkdAMfYKtjC2FrEksfYkBnz7slxALMwfv2zOuVkYtI3lW8dXDb/S1cT/MCS4cdX4o9KJQkskM0wveGsxJ2m4nMte6Nexfx4NIIoKIhETjBQn3le6a/yT2bADyEHge94VNAK43pYWMakWfT6aPq3yP2lB+amtXuUE0Bi3ULEmu+VjG2SPEChspL51EgcTKKTqlZp+zRPD5wHoGVIc8TrDcne6qh0HJ2JblhVoeUduJ7iRg8zjDLhFk0hnvp5AIqTDOBRi8s8KIUwQOe1YmLIIC/139YT7wfsRr1LLpv2jtyokhQiqYuKRqK5GeCmZVT84TMob7VcYRoka4grcRhd2yHGZE/XTdvtJvF3wskW9LjVoqC+5xPSizLLzCNVP/oqZTNE/sNJhCg6yZCpWuTVT/86pbbILZiKV3oTwYeXE+iruk3q6UWgkkiwhx3+8qqEkButlSgwrsMmKbqTSsD5pYfXQ3EUhrJNd0PO1yiT+I0EvlDqI4UlGu6FndPv46Ma1FW9FNEg5brR4igukNkCyDzN6+Pv18G4EUhCtbXzWlQimI3Aceoa62n7HCqVb43YgUye7kg/Sj4IapHSDQKA7sPytUEpgEe3TbFGSzxzG9+heT4FDN6VopPt7bgwEFRvv2ISmwYcz8+rEOkVEaGdqGiD0504Lu1s3HMMAfCktZkTzhZ0Tx1NUWdLH9fzOfG6ZbRxXAxYqo9RiWc5syGrCEZaXyJdy3+vgSmdtubs71fZCFAW2Vq37fdWpmgRIjwM/2l+zN0Llzbm2bHvTp6Vt6/48zG9shPjB8yMw7dbWzLrffVv83+IyYazNfhIAWnoVgX+YDVQrp6gvjvfena5jIa9ivFoNIaCDoxRjK3iVnxEIv3bNmMhO1xRJ4Uhi39jMD/knYC0saiIwRicvV+vkMUREObu4zJhFfYMmbFa2fBlXUroEoSRvYb0H3OHwcJxKkgaaYZ3beK3O0LVL0cfrcedr5w0DSvK6P14bJMx8gzaW+SZpV1Yg44DvhCgCXjuJmQbMN/ndYim5ASovVLDbZL+GGXbmmy0qMDWC/www6Z9l0vXvW70M6od8n6pzd/PYqqDMNepIbLCDbyfhYpuI/O/aB6mMT9xDWUPHlbYSAKMA36lJZ940wFqnQoH4S3B3pguuDxmikQmlFyu6hl1HJM8ua1ziXUte8633fwWoDK4XoJFK1+xGtK0/O5HKJGJ1UVC7BYQ/eUeXLmCnlyVr/8IUTUvnePttSBD96GiR9NCBwf2TmK3UAcAfVUncFXyhGhNIXZg8oJ+6yXnslHOt5GbDCoZZku75qFIz/1oP0m9nci6gOnYdH5ebjyO4JFCfPPFx3eVXuStmzQnp7VHSsznZ49Evx8+FnizTZswnl+KZlOUqpE2OcDiKneSFSIS485hWGtsE5VG39MmOUgSQHxDzll0O/HmedoiemUuup4yQhMs25HPaK5iBDQQD8pE/SKSzhIafn+00JAWuerQFI1kQ2lSWUmNW67We15J/9v6NR4sE6Ay5a9PhDW6rvbXKfEcnhFQiLpAKA9pRS3UkajEKJOeWyLCtGJ+7kPN0p4Le8LjssHRgMbDh9kEJMI2rh9lu/lYc1e0Y1l2mz8cgCzH1Bqo2gKxlp4pq5KuR2B7EZq3HtsaeQemy3NNtm/f/OtyOS93Zceb1D/IWACDaVkaZfoACqy9wNBFnxEjY6s79LwzNl66FJuGaTAfph4N3QJedD6AhUVDExMJE5hL/n0blyRu7G1Tb6PZye0cU9/jYUuH4naE4BWOQSw/zx+l9i0bXgmGVNNOTlk0TwI9kxbGxhYZ3ZlV6URIJv1eN9FG+aC/y50apuTLSPrgAkc9pqfTQKRQpq9lKh8MqtdSH43BIV2DhbAW+u+kMAllgN1HCqO1nICh4hMx8xdOXd735v7EAR6d6cgx9tg7vwfyfMjLZu3HpoiEFCA+uD/XsdZVp3I0WgEwnONCjBNS4xmawqQAbI7SBMwqHO01HzQh/kfOmvFzgIDrVP6FQ6TvHHX/zA6xwMClD5wvhXhTbU7TFmElHTriU05ATifTTKAOPeEgVLnGWSIXegkLw0e1z/7vOUgqPDTusWfZVurLeP6qLNMTG20gvxffbklTwG1VCeWjKRGFKIX4hN92wM9ZJY22gKnfEshaLgckE12oIk3m/rHlrpqljKm4BSZZGsJskTctMCuylc4bgCQpG6o8zcnRlEAASkoBF9xYkayn1rM1sk4ojD//qUY6Q/rhzFfQADXXGrU4QYDZ43c1ncboyF1z73lx6y0gdbiOZBZG2C8EXcVgVEus6RPrtV0Gbt1nCqe+IrRmooXaVDKBnXl3slymevxYo2bw+8pQF+jMfvB2tVEjvQgqpXtE7hgzHQGPXCYTRpyooaSQvO6mDGrChKWyCfMHikiWktQ9r08g0iWMhAzSFuPnhAD1/cVlvvBfUkensjexHFcyzqC63C5GZSseZ09kWuRK06Gk3d8EFeEKP3bH1BptKS6oZMih1SYdNigHzvDSp98KUQa61SgXRjzR9RM4fggjcXvDa4QptoLH4zZT4RiZAJvME1/nk6DKPTABJ1gHO3WK9P41zaAMIaYlhHEzARz9UWQOma2zRC6n9DLGiNpczm7cMuxYGp9JJdP/RVAue7z1WzNGHWCsCgcZiXtqb6PdsnwjK9QEjsvK8JTF9JqSmHX4l+r8OFchWHFQ3e3CgGXZ9NKkCbWaggWJdAyAeAVfjO7zfDBuD1iroYSMQeAUH99jTGtWInsnYxAsRKuP0TZPX8+bDqVlfKR8wZc1IvvxZlRV5gkYSBlDGY/qkO2J/at37C784tNVFbWTbtM7ZXQeHgEPTRaiAmg3h80yDJ1se9ATgXacRVbSUHllhWD+RhfP+4mlueGW/GDyZ/zYC6vZU7YjiS+HzVk9098NudYgUPJ4vP1Rvb5w3RBqvv9GbBH1O410dZqdnUx70htTWrBHLf3IPVcS6tIqosnyb1S1qzxYxYqqi7vujC2B+oNCb6C1LXLzaqiz2bbWjUdfQc5pOz9FNoIRTCm6/916WAQZT6W8Zq0P5baT/nlQknamKptrjJzyNREImH0Gq0RNgzYXGFGFQEdqwNLsAo8XeKgXrczaL+i+IYk6fvMQSNchPlUqRyjKNWVtaIoIJSx6UW2fT6bE9GbHoCwT8/b/5FWEIcY3AhwdWfABWHNoXDK8CfWxTLspySMzVmRArxxcJXK7+M1tzaIvt/GTzc8J0qW4WstEXBLafjqw90ze2agc11nPNJvtPeSwzC3ifrSFJE780OT2N9QJM+GwIe6WSh0feWmxHff4tQ/YQxuIpUbwuebS3EoM9NVfsHvI7KDW2CxViAUISQ5xvoMoMCQdCnb/U7hAfF18rvK5JDFKGsAlQVO6hqwQWEJy5E5GlbDHnnf/MjBhK5GJ1b/6YpYKohLONtZC0J/+j/PyyhU4RQ1Rpfcyqc5xiDuTx2rJVqv68XHY1VRZsYWrNw9A8pq7efPRdLmqpgBoW07PLUPdYPAsxwCFhFgoUSY+PtwG+tARIrGJdCbyoaTFeROpYo/AMtYDs+dUj+rjQ07vc7W6KZ/npkMYoJoAmgqcGOQReMDXrBzqwFiyZz3G2uPyvrA1veVJvkCxZikG6rWx6wirL0gI50vJJkfHesc3kYrYBkfz1rYjmykTZHBfO6CVImsR4fwRK7GNI2Z41fCZ7uzhF39qe4FGuKeBH1W6w1Hetnm2G34ByqHV87s36ZbkLea5EFeMycpF+f7YXFV0x8BhhaJrQfmbI5k52Xo3BFx0EppNcrHcW3SlKna2WT49k1qA1Mz3VkmR6WmS80CRQLI/iSWLdbaVlLobwzKXVEZtasQ2JZUbb7RLw5P+64fxVAPB0Gf58ljLikH3N5Y3fitolBXVH7HEFpzZ3AuebfOAVtxru/DYAg45nlMgumXZc2UFYrnfNHIl5d9c6XBLWtB4xUZqhzOdVlKOrnbVetDBkpKwzAAP/NNGEnQECFYmHhUjw1BjMjON4PpyATE/LonFLH5C4nQISGmLyvP1L8F/bc6+StYygKSrK6L/F538AHHB9/rS0hu7V2DhhFdjNFI9a2e6X7aCy85QLMrRlWBrb1Dt9R1X3vcWIekEQ+ZtNqDVuwmKmdse18+UO13zTY0X+VkAPki0y/Ds6uIAQPou2RzS5vhiGaRgS1jkklHya+UTWRiSczZmqGy7zFcVynOSCd86E6Oi5fQcHEO0Jt4Uya8w+AIYEDZrx9/yf75f3uXsG56iXdfvfazASHI2vg5mabQWYF1+FtDQUTHAkj6LHpGIMsRPpnOhdOv3MrnFVaOAdNqxglsGdVfpPGcgB7tFPDNp0oKfMwV7GUthONtIGB3cCYWH7Z53/MXxqYAupqcnBAfj+IvmuQLoF5QOu9xKFp1xnN002sSeeOcELKKP1UVMN5T0ySKagLNLYIOu7/2yxKcRT4iiRjt5Ei86SscWeitf7hoEEMoBjY0JgwrY6npist4f3JPzRTNwVFU6QRIUp9UHe1qn4fDlgPrfEQ96e+aJkQYCad5QOjch2mklTqyc76bUv8/mi5iku6nO7eZXZmfOX7y+D+4YqUn/6N0d9TsnaZgh0WrDzp1Q6hRQmC327nUdlj6mE0QevhhlrcvAvkvheHXBXsmWhosrbtN93nyc6hxVw1fGgT0wZV9mqtZmUVHhe5K4APE/S68+AvhUUkkvUSmUAZ8Tu/OJcNP//PRvkrbBL2qEoSK9OOAXkkqY/FTTJBTFi+I0K3oEOzZsb/TOKdgNIFdwfDNFsENxfEDGCLiDih5v2PPDu7GtJaf6NBmDvgEtzJttPpxUFwCqlQfH7c5mV6NlGGEwUAjtDhQt3GM9gXt4/U0MxO9QmVZjguPNTbEG0HnSaB7VRqrmN/T50Y4ub+sM6ZMpeROu8+nYby4XV7y8OBZwhUMY1xUaCjoXjH4HR86JVO3uqSKgEP3F2DqjNY7xiKGIiRzCUNnyrrufI8T4UO0q/73bCIMFtvYR2EWS6EAh1V2IR0Mtf3I2P3ijh34gHk9loSss0cCvYTQ0QF4SavkfzU7NignvmW70qW8D6cGULxk3jwsPNfhDOFmK9VjH/g/qhwxuswClaB3m7nMVUhl2Vah3TYdNBUqHzR+MLEmxht/6wS6zKrbTZSV1tev3468x6S2o5q1bz0tYYXEH7UETCQfbbvciMHA9jz0wNJj4/prGr+qWsAKIj4i/rARzRFjV7mWXeUl8YgBrjKCBOn7WKRttRxbM3g//SscHDZjZMzS57c+T5ZybG/rQk8+ivGt6+wY404h3LFTFCwiYq1PA/0SBIyhi3ApCQ9OgIb/IEhgKBXpDt9G/auWsM7NY5//oGqPzAU5ZKdhhPpk77pYVQ4F3VUyNcebdCZsnA/cbo1Njy7mrp+H47C4LVy4tzl2CCxJcoOKbjO291HmpueeFzbCXkQb/BMtVuPgzNdEo0tO3USfX8utckDIaWxytL2lt5t7FsFKg9CiXxB90p8NJiZDPmRqe2xa8ErYENfrx02JiCRi5x6O32jC5ug04iZq0+5sdEq91Vkq10CFYNb8BmXNi48E0nEqFc07xRBg6B4jMK5fh9DautKhSrV0d0ee3kRg7+cJJesfyAICmn1NPSrFVBKnff308iWfa+pj2OXo4R6xGWxf227GJVrjamPqHmfKW/yr+64kmE2a77N0r/qf5iVg19g4TltzovJQJLXlZESfbvHZdW7FQGcCwSEQARiHDc9SeZ1KtwuNdE6I46LFzkYNv90/BcC0w7zL8ODeOC6Zais2WgJaHSvHftp6bFxIQydgvYw5saPUIB9V/LUsbKIW1G7F5XuMMgK09EopIG+DOly4lai8Qzcot6AaAYvBKdAKlGZt4FnMitYVzIBWc5aXapk+8Pg7zEg5nZ3UWw4KPYs1xqsqXGj3G9H0HnUpzM+bwT65p05Tzw3+kwEQukbimBmmWS+RJvxn37eucm6Jr7u/JqwlFYgkSiUr7Yolo3ydDHFX9wvblhRM3C7Rpectb6iJMbDAz48Oj9WBKtGep/vRLilb1mW4N/FNjH/2ZwKe2QRuGJq/iNa20fpcYtxdJQqND5yBFpI3P2x3qu0s085R2tyof5k7ZuLAviPiq19LihjtWXLF3Ok+njSIohS0K8PASGCMDaYnVYOse1xkNaDpblp3UlxKYKqBqscCi5kV9msBbTU/bqeoa3QYtmbKDuasRL2kttTrtupDmb811ynoFwAd8tiSFkaYkh0zKmfZ2KLmPgBR/a2bDaafDq2XU9tOTlHDJ55Als3WFPg/UcQQNNt3GUbPOZyC6kPoGcD5ofqTi1vOX7xzba81I0ad0kSaSBi3xVIvqv5zbLRwjp/PrvE8AXD4liWZ+DOfP0EQ6iGHJd0KctJ5h8UOAdLuw6czk0qO2ISL+QrIoEaplAFtf9DGN4yzwZBYzgZl3nn+4AguM2TDw19rtOYo+Z5T9hZKHs3UHPF2/badxFmitYRcoBI9qaiMaG51Hey1ypxS6i5sb3jVkvNp2jngHdvRyNlurcHMfo92DwDoAxSf2K36F89Q0JVal7m2+Kr8EgRRwJiB/TrcNveG5iM1EABOyKGyxirc/pAugYXWga3uXg3IhJAtsXEA4U3d7Ofd4W9zA5fgkksChZLNOnfXzLroBtmdAQdaFWxj2sYyysA+qL3l3S7rOX+lotu/Wilgq+9JEyv9E/quWHmjOnL5Z2zrg5wRcGZVu5D5y3B9Nqe9U28vi13/vruYA/9A+akUsUGT2jR9xgpRbGRvna3TI3VIfUTSTbgow7jWenSt8UfKM0cEfJbr5hVbBwFldjiqCgQcWHJKmHUHWZbPGUHeY0T8FZgiZ9jI5KatEDb1N0xG7RgICeQnNiyBXH6bSpD73GsPcooDBLuf0tx/rDrMkXkL4s1jT9qUKqJtVgdf8GltOlS/jY38y26QCl7NYDgc5T+leeVB7cFbhHTacomjk1EehbX1lgyAqAnLL3/EhQUULGWlgGfUHiyxw+69ab1VfoI+Qatc/Ldj/46jVgT5PJGyDEEsLI3i6o1TXUtTY4lTofvakO6VHY+5GIC5uoSIqhxsVC3AXWvrkC00ijWHqIyub2kahmnKxoK4f3NG5oVDqgH23H4rLiUppUwojbUzRfq9zt0kDN2ISdJpImPryhfUpEpPTgk+AvR8D7TluCNrVeBDf3xrX+YlYxgoqdOh0gzjTPlKKRuIpWOd2OLe95MceDkQLEqq9DUgxROrF6VbZrp5Kd1EwAV2m09/hjEMvHYEC3OKcColKnznHBJzBKNS9ALBl0CZrLtKU7aBONIwfe6dAaHDL6Doqm7uDrr6w1MNiNrkLYKSSEc8blIQC7lpBpk1CLf/4IXpWvj0ppCDtm8f1424NYcQda37vuwHsXAqDpiMG/ZqgzEa6Gpl/XuABHdyr6YIDpvA5uDra2UVFND6bcaigUPDBABAOR08MMyI24dQNyhBt2bIrT4xVIjcEgL7XW2kymXJHAXvOxUWrEp5hlXmEqej37FF628RBH4xkoZXbTpm4tsfp2CCkeYTUjvyfUEKzfkEISnxfg/HqIPKO1CQauojK4qhz6RLc20wXbRtLm7sbGuCfLpMfpkKR80DEUaxaDxLGXrEEcnlakMiaKHoqhjtkQvIjCVEO+twS+h4i4ZWgFDCFSBbNosgmNliIfCOGjAbMftQmcnXv/QhMFbM38CPELiZQFulKks5aDikKNDheHUIioY8dfF+6zNYDMZ15B7E3+8JRKujyQTwOkl8hVhYOhGIqGcLs8gBiouslkYcHGLeSoKeldL5K4hDH4fBuajGu6VXSR/VQBJROgYPZptdpW1uoBisluK7dy272WXEMGgyHftRmqCnonKRGjT4Zo/6Pcgb799vfKnPueSrIwXF7wMOtSPYN0RJoIkAcTNhdMAJ4pqSh182+yCSCRU7enjgYpZiR4ooDZq57Eh1IOCiKhqWzsjHVEw+ibBe0sHmx9vy+WvqBFO482Q1nTZ/7jDVdGzu19BEH0mU3Z/la6VvrGmRBOVDwQb5KlOZrsGnDm3Mt37nCRtBs9/ywd5rk8+MbNWpuli/HlzIbv6q8LTbQY8zsO3mUOZeATgoTwWNqXI0VV2tF3MyyqeGQ9SMzsa2KKvaRx1MpW2XLwBT9ioiU171wqEYRylWepeiBNTJeLxDrw8Ekwg6j2WiFzkpCuT0UaH400kufyG5JA46YyMpiqMKZch37H87l8+L8LY+GD47no5xG6ukT1CZpjo/gEy7hz1EN9TJU/zLqNikvoBaPpiGHxF9whLa09DY51X8md5EuRV6LFyfqNLEN9/4SRWwBvPFBGWRrGWSjpNACa0DAAjes8mkxRnN/3G4vLnVPIl6BI9lzzJk6l/BI6gZcokMssLtHYrOaUX73Ss0V0tXUbQSxVVXBavQYbuDqSlmYpZXzJgp6NmSCYQ9mpNSBB6B8I+48WhrlJdGrG+9dnuWw8tuaqPJhq3pQ6vSTXRbAliyh0CuqagMAt4N6zg2Ifh+4b+YMF4TkXbAqZTyfGWM8/ZoDX9pL0v47VJZtK0khbwqbaWuvqM7ttujsliK3aFxso2xo5XmTLRedyZ5KVfA6k47SahSzEkT1IF8pS/C/1boByNhtlRFmxFDtBCY5LquhDqCQRWQRkxDPJ7XA0WEvjaYdkZslBkdFuPLGIfJGWDlxRIPr1+9O0hXOUMysK6jEAYuotM54ZwixG1+Vj2SgPaBIMzOzIY6bqTN2OvqUFjGGkZ2sW43lU+4LXq5c47nBd8FERnjrr9w1FDG7/2xa7TEyXb4ZWx+87XD8jUEOL4iyVHAqpOOpy/I0KZbsv88grZvKYjfXY6pyl/0YtkhN6OCovIDLWciohmcfRd5exEqXAC5tpFzeD33wwaAL5OhW+pJIjPk6R7Bt/2icGtBEa4mwMajMHrT0KqmsqiGGiSLK1Mosazi//Fqr4G8hMUQxgZcWXZ/rRF7NfTVEgkVkGNHGNxezyuC+Mo/0SpSnSABY2oEYBC42ZIxlJLZD3pXDwODx9UsYD0CHm+vfqra6R/9YxZsK1p9LXpEVllLe5yn23kI/XF8YnwNBTTECVTz+mJalkqr3keIVSxuRIF3Fg+WlqRUOojyck4m2MEqyQB/SuNexsTwh9L84B6xNrjHucyXGskEw+1neVM7SDALrx1qKULsPU1JeHqOzX/a9BkrkBW5tP5pQVH5uXpFc7AWiHGfRl4+038dY++Cp9fFo4WuiSJ8fLNXtlLz5V9WxR5Gu4Qc6QtEzorrP1aGNsEGVvrfXhNm2EAZyvvBFjrlRCJG77P1w9w26xKbX35qOENOUREQmG0y79Tb2vlaeJMTUNrZ1YFwQwFukOhx4WyZmwNGJR2QHOtNgUFkkwNeJwpoDzg3LXMmg30ukAavB6fRDbIbyKXzwIapj++iffOK8ARnJ5sGSU3t4LVejgmzlAGuwBX8BS+JEjmDbv7hzDTwt/RL+eTkwWTaq/tEGrv/LoyOdhGL5bDjwOxqIpg90WmK8gAKVfpxHLTgOR233So0Qy2DkHNLHCUXp2xXDARvl5eZSBUV3bu2P/m49NY+yhCOwA0NA811Vhzu18UMjZOo1NLzccElNlC3VpNU5WinEFfFkSWsEBdS66Cpjk6vfpfiGxKh2VPYMXVuIrkLq3HYo1p/dGqilUXmeg8tnlpc1lNJkGaEW8GmheD32HVIUC1xulTF+c25KdQj5yFZVE85k+5XAopQeWs3K1ld2vftsRlBKeAEIovmDQPsSmpvHWmPEWKylNT0PFGLTYUTDGZuTSHBqo/5ifI2/cJGzXREGaFYFqDzPWe4ybVWeSAcSW7rMSVbV1JGgR+YQ3NVRaYcGwPvclkPEAYbOSEIR1CnhIF0rT5QN55dVsevpVBIlOjLArBvhWHCHbRD9L48kXOEOEQXXzo+y/0Ntd3dP5bJpzKI8G9idejbulACX9xkr+hKX3EP2UymGv2DE2W2XjfvSDoPJn9oEYgoFEKs8x9Zr+7srzlkUndNC7fcupuu55+s4OwYmf5K9B4kWRNpqDWggyvh76+Hi9iORcKZg2ANBSXPE+uj1HLnv/7Toaxc+yAW9GtVvFucy00KnFgTvTcbGCDbkBasOSCVZKXO7BOg2zRJ6YNyxnQdHjlxB1yBB48J3E4cGqWtObh0qff0Nna50KL4K1uPcRVEss4F9KllhLY30NHaoVYMEUtnWzhxYJ2K2Sgsc9JUqqPbB2HtI7Jax3dX7S84DrJJM+ITL9YEDAVsVhfhcgw8k5DyJ783IGDWtFvTcYCOGq/VeBk25w5BXussTRYD/amJdyDR8Od6vYHMXjoeFzbzQV8Ai7zf+wqEM6VxqFqB9O5Y06QHcIykBNky1nge1oEi/KWCNnMkknnRYh8MARvk0ESEywV/bA8VH8v7Zh46PTSl07lOB8zzNst31iU9k7dbMfz14IURPu3wEBFlJPAV7UfXE0zLlcmwyNu135rYdXDFDtszZZYJkUOTGGexxYU6nU0sQZIVF02OzK1NxfMBZoZBoKt7YuSCOjWwPn2fW0eCxOmk6tARcwhwPV65d175LsWrYBrvtiJmUK6n4pQIekymcKTxPQTxMe3vxvhzASRBbfRPtF4TjjPhCVW+MjAM7nRvrE6qyaLcmQ3NXpdIgF70+ryqki58NVX0uEBkr4uI0+Gd9C/wl4+qoLPdeengU9+V3pW3eH5fQJ5rJDgm6Y6R+h3geI3h/Rgt/j2y3+O0x77gOeHm4Y+yRq+Wt4TwerDG8+TcKf/tDnSnm1Ft0KMH9HrA7MQJ2qYKldC3w//qp3RC/bWO1mECCpwHRGHwTigIk63a1u5sa/cXfe81rkS6aMLPVG4oCnaDKe9RBkmOkdYXIM3QVgsXEuFIYGj38XD9E2renmWZogriZPghmVTmpBS6YcvYJ0SHLlSyfI21Tj9lasqOyZRKkRIh843ut4RGTtyDGxI5CkaZ6Xxw+jxNqxl81JjMzJWyfVfQV/22JE43dpxPwUedMTUpsLpPaK0CwKliqwu4nY0lAKVl2C+gN8hWO5IgS3Qqq84orrNuKYIa+HgVfv1Vgxk4B81+SSaye7ZfoDBVtcE5y3FRzm5+1Y4nSJ7XzuGt8l0EGhZHiB0wJMmNyz8XEcmXuwH4/UIq1a8hIevgwcK7Cen8U/IZ2N44T04uVHMON8WsYv8gq1JGXMsNaZ2rH3mppV9+ymGbu5YPYYembORYOvAT3gM/PonHmXBkfXoA3EpFjBJMomGwL9ZjRPIaAJlopnw+bimVmpp3bWYEEod64sEqcAq3jnDMlJ5KQIYpy0QfmzWFGumuhz3j70FadyYiu265Y92EacKpyWg4pS7PBzW2tnNn8Dr1l0gUFAo3E7aqFNU1DDJmZeX0DJdbLjaP7+CBUbUK4CUqXXLqW5nli3djuYrZ21cbjdE+4Q/GB8eHzgUO+otPK82lSnxTGA3f0hORitfktPi+cEbkBG2HhtR1nwxDhQLJJ+xE8nBVTP7LxqE2qeK51mC+UzQepIpTCC697VirTd7++piIr+YTS/msVNTobCyBFY3fhPqy10kIH+DRVgYaDR5Xv/qWjhyMEdUCynnOLxcKaE1myCyS8uwlTH1hHFnK75eTbWpipidOdc+L3rNLAmUFFQyOQbfJq/jhTW8Z4gTcsyUSjddKJCVjzo0o3NSq6jn2Gykp2H+jQxGwJNLpU5A0E8Dns9AQVKEjZX81TEjE8VT2nwrf8EZ+ozbP05x4QbOX1AgwbsZNNh3vv9jHiXruhh8TiG7+9keZwk7LwMlTDXFjA7zMTnuauIiLhuETinHadWBZ+ZBUmxE2+7IZURgbGg0Gmv6c8DrXVa/woq6EU9O2nDjG4a83abxkw33MpTkT7GbwVm8X2Xur2hEP/w8en6zR77nGUVa8Ak3ZhOqDs1a59sQ2h8qN/NFreIrobe41Duegh308zDPLIjKFbnIq77hyj4oJo+wXjzAOjibs64DzRMecB8pKK+ZR6xzKCogQTzPPCsojFFsAFWRaQU1GFPtvj1M9iAg099VPxavHtq0aRE3ztz3jwXzfcmQvfi9dLl58fl4jjZ3RDOdSFsCRcLaNj/Ojv8/rWGHF9EluxufovoldQfs1L4S75SEpKvnp1h1cD2ldX1OV7OvK6sMqdCKZ5iIZP4zHkor5X3OfZs4k94mRMfWq/FZneENLK9JROw+3dCYRO7eRbwg8E+Z17DhEv/b8FeyiUEHq0tldT51ZvQiwkL+BvG5ttaFcJwIdITsVvDBM750tNEBabEuBiaFvLnfzQ/By2Z23N9oXzBvtS7CGCIidLCMXTUrkSjUE2gDYiXHEkGiwtnxhHHJtgYb8n3ZNTfuA0QAAAQ/5kjvEzNK4np4UEzbt7GXzNWr67Wy35acHE1tqdxz6yzgtRPNpBsjb4eyxp/YFnhtMdphApSnnGcFnPUOV6w2nUtpYsg5U3fRp/8yJC4TVnN5H2IZVhXdzYdU75/ux6ukWyax4jLKtwkAGMPfokAK8NPGZsxosfrOIzBJu5TS5pwBHhFhtjSXF2PEme7ZUTpxiqYC8yFEUj/BqLi1yNOCzRnyoVubC4NgIRNUOpZFIvweXZLEMlJgh4H9a8i7z+cZUznmC1fmym9d34kg3G+uat/uDP2tYq6zNpp6bjCKxBnoIos7J2kcZEm2HwpfzsLxzdnVnfU+jR6vaoD+i8ndFZ2y/HxvEz5Gi9vpR2XUq+82L7iLzJYsmU3+zLWthyxYdT+0VKWZ6guoZdDwEEd4HA08fkq4t57tokX4g2QdOJqvXmgD5IZkOw1yLjE58CTZTI2ifs9a1v3ynWi6JK2T4q0D3+j0gdzmmoGzhSHQCzVApEgu2pmwH+mc09GUGkTcRvRVaSLLJyGrTTymfJ08hqEGk6EZt9urhx9Zj0QmmqYYWO2lFQQ9NYkgezS+kDgrwzg0IwnHpTTciQ2CrNBfRdN8pBszCegHaYm2I4UarIJQxkI+fcRfLvyzC77XPCxKgi1FAowKr6r4sO5WqNvfUCmZwVJ3ZospCmAvAtTbv7308qenBLRgUCMuUZBx5r6uBq/2mw2OkjE/CE2ZMnDesmUVBgmQGbXyTYc9dTFsBXi4/RALGggB7SBh/iLl4bs3A8/ZatNRTU5BMFUWi8UHA0+vo4osPRfHenLXu/TSRNZwuIuNyguPRGUPYlb1da/tBNw3X/pTgcWfpzzRrfM8lM6wv3/jtNN2OWUev+JYelrMKxAQNCH/L+NAw3axHWTlA8jW/aBee7kg3MujZZfyvq5EMlzLV2ppzgOBU8E2PQmOFpZw5N/Aa5brn+tZdOHbgGSKlO3VIwBfMo8PwfkZONezOygduoPwzow+JXZFVPk+w3RYu8CmdY6bFFUuhDfMU5Ubp/e8ipvYsAI/iaOwpwiEgxzWuWzUggdgpboeLML1zuH14WceP1mxdupFZK47GxGdyzJMzQeXZxj4tIhlkTKMziSEKaP0BFWdBF+KBL+Vf7D58Rt723Dk1LRYF3XmpPy19Q0kYwIv/XUbemgngpFuePYBzkxzQumMwkLF/FEHWKU6VrslHkACLg0shL9sy7DrqQnVdIs4RYQpcr3MblYH19nqUHFkduoINtB/3NkD3rtZc1IXcoJ/76goyDAFmZGImV0JvmcdOLunOdoAPjqXzHk+1Ivumq5cZm88eP816oR1DLCAUo4pBXWtKtzqqxVEdH05o1cGHFJSQ1keJ44xN5P7GieWviObaz6h2E2SR2474VSzAhSEisNuD94F/VGFMqX/IIWe6sfFTSoq/5c8cJmQczeE5aQTAGLa8C6L3jc6AwWI8Zuru1BrodOOL/Q3hAcrfYRYW/YHV0AOBqoAQLANlfbv9Eu7JIDDiokXPJM+RyFqlEHhwMicy/vk2u+DqZl1hf6RpmasS/Y/GCYhg1Rn32q+GPWWzDrqWPHbT6JRaoCw60Y5IBkGOcBzlR/ES/pVqkSLQtr/IfBLdThjuDbkEX6sSbf0o+nFINfIaaIsW/xdLhXo7qH879CYoid3lo3C7L+BtG3VV+OPNYategPXyXnCXQVnYQ2bbKlotFGWIgImAe3mGNsCpOg1tDBCJbwiPGNqH2cL52DwfB3OQFO2FP+aaUiOuPDS6xGMzL/VyPpAdIEY5ncWbU1ZDoeUa6emQc+zjAoCwcX5Iq5GIccLK6qO5QkI5o1lwYutv9PkCM4qPyIlHVeanW2I8xYwXWWmTQnAT9Uw72nSw3KjN4RyGHvH96fTVSsM8JMwYkXIYcOWAcIpZcoiBeYNYIS3ToPSU6NiG7i2XYyduaN6wzkB4VmQQo3PaRMh/Te+eOycpPSjhFCaFdQEHZEwir1b3JaAM9SUksU+jsWqBIah4y8qnH5zfSMLGnEsOKEwMg/9e80wYprTwm5eG1UEWXxYyzIeiEKHbfrE6OcTvzsX7eIguwDFC/WyttcpGK3MwT5z67+W9+heKQzM+dUwwJp/tEOf/mW0UJPHv0YWoXLPGynbAulbzsELYfHwOiB5yW0udhOPgH4YXj91H/KdVWHmZvRLREk2fVmblL+oxhNzJ1pMmxv5lcDI3ZHgSMD7xiLZhHWu8jVErd3vBo8X6tJ+/Rcz873RuEs3nJCkcD0cOTewEjN4WcCJWEC++ja6Wdb22UuAlG2bE3xe2OlPTGnW/8eg632Cy6kcNqdtgFTpXLtqY/0ClM7jD+4yUTr/dFdGDTCHoWoi9zphAbIBe5FtUaw1iJ0szhWUhRV/+Yi3/gc8UcI+S6SH4D4xWaEPzA6bC1UN7nCOpxMtWzLIw5bhJ/GUEFKG5t6ayKTr+1LQKgt/WfxxO/GD5Cnm2HgcuT5sHZDOb8+eN0sZwUWe/DeOLeEHI4qNg2TlLDLlGBBsxhjW6+fiIE60YCU7+z24XgROhqzMuNuzh8IoUx5zXZ+3ii61Djn9cK9muIxOmRdgAj4e0bWD4fneJkytstEj5lzd/LFqUnzn2WKta37Kh3kwHIfP8uhU9pKOK53YZJ2b6OtYrMB6AWUrzpNljuQTpk9Jgbn0ceKvgDv6OJeuUzguS0F0CgWS6GSL8M7B8Acu+2kJoCIXLm0G4eADebfM8Ve2GwPSyq7nk//KXXnp507vx1MJYzrqW0nj88I7X0cVyGal+2LxbWtxDZmd3TI/jgiSaFWqS/PAVdZjdxTq7XlDUY37+tuFBcWtDn8yk5LuQ8GN/ZPVmqU7iuA+EqUzQuN896TxBZnpUIkA67CmjF0De0sYmpgzEYOoaT+kFznoOwwwyjsgEexs64vfhlpkBq6DiDGBA8woJ9jkzb8jcNmdRlm6fjKaqxv8kJXMRSvIEBHCE0hFpJl5w7T6lYcNaopDfaIQojFrtoSb2IlsVKzuzf7a+Jv4PtHhlav3eACecyPOINhg/P0RhCtziqlXuVmMBUaZw8fJoNuQ4ueN95NBJ7wxMy/QaMIbS/NdjMCtiWTO6pW172elqeYz6Q1HIbJS+KJ2uXBSwXThVEsxsR/ULhfEUCSk9knpVCCv+cK193+tKhm6tpXX4MuGJciHc9Ze0UkqiynKl43XSlOxlN0cE43YUNmFhCAAZ/6v2bkT4+2uQHg+y/tr1xrImPqh9NhUpKxIqXdlazPrJSeCScvQzpmkl+xiSgR1HQ2OoPYzAc2mxY2TUzMlwuO7HNU2cw3fzQcyVP+xtFXW6tJUla1vOlCWlXc4gbzm5WgPU5IJBe+07ojxGrNQzQnYZhKBG3h3gSElF29V4M3EbMZcW1JuNFkLsBQLDxvDUrtvq9yjS33UmcKQxgrFxQYS+vZDQsurA==
        - #2:
          - type: tool-call
          - toolCallId: Aod0vgmc9xqy1ihp
          - toolName: set-research
          - input:
            - Technology: Combined Arms
            - Rationale: Combined Arms unlocks the Tank and leads to Radar for air superiority. Since we are in a state of war with Ethiopia and planning for Greece, conventional military tech is our highest priority.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: I3IHbC9wkxpjUn6W
          - toolName: set-policy
          - input:
            - Rationale: Third Alternative doubles our strategic resources (such as Oil, Coal, Aluminum, and Uranium) which are critical for building our unique Yamato Battleships and modern armor, while reducing unit gold maintenance by 25% to support our massive conventional army.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: knTiwLnrTJqWAeOG
          - toolName: set-persona
          - input:
            - Boldness: 8
            - Meanness: 5
            - Rationale: To push a decisive military campaign against Ethiopia and counter Greece's domination threat, we need to be bolder and more aggressive in our military decisions, while remaining highly loyal and friendly to our defensive pact allies (Mongolia and the Ottomans).
            - WarBias: 9
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: TijiJ34lIW5TK7kS
          - toolName: set-relationship
          - input:
            - TargetID: 6
            - Public: -100
            - Private: -100
            - Rationale: Greece is our top competitor, holding 4 capitals and threatening a domination victory, as well as dominating the World Congress. We must maintain a completely hostile stance and prepare for war to dismantle their empire.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: iMVTp2PDXfyS29yy
          - toolName: set-relationship
          - input:
            - Public: -100
            - TargetID: 7
            - Private: -100
            - Rationale: Ethiopia is extremely close to a Cultural Victory and we are currently at war with them. We must maintain maximum hostility to crush their empire and prevent them from completing the Citizen Earth Protocol.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 0K7f9yzC5ZFvzMp6
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: Aod0vgmc9xqy1ihp
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: I3IHbC9wkxpjUn6W
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: knTiwLnrTJqWAeOG
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: TijiJ34lIW5TK7kS
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: iMVTp2PDXfyS29yy
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.