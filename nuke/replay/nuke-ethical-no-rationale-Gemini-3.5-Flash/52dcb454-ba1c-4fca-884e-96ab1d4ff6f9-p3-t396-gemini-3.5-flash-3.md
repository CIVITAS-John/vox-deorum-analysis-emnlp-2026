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
  - replay_nuke: 0
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
      - toolName: set-research
      - args:
        - Technology: Combined Arms
        - Rationale: Researching Combined Arms next will unlock the Tank, providing us with a highly effective, fast-moving land unit to launch powerful offensives against Ethiopia's cities. This is vital to halting their imminent cultural victory.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Selecting the Third Alternative tenet is essential for our large military force. It will double our strategic resource yields (critical for building advanced tanks, planes, and Yamato battleships) and reduce unit upkeep costs by 25%, maintaining a healthy treasury for city-state investments.
        - Policy: Third Alternative
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 90
          - Diplomacy: 95
          - Culture: 35
          - Nuke: 0
          - Production: 90
          - Science: 85
          - Mobilization: 90
          - UseNuke: 0
        - GrandStrategy: Conquest
      - rationale: We are pivoting our Grand Strategy to Conquest to launch a decisive military campaign against Ethiopia, who is extremely close to a Cultural Victory. We must seize their cities and Great Works to neutralize this threat. Offense and Mobilization are maximized to speed up land and naval unit production, while Science and Production remain high to support modern warfare. Crucially, we set Nuke and UseNuke to 0 to completely renounce nuclear weapons, avoiding their catastrophic, indiscriminate, and unethical harm to civilian populations and the environment. Diplomacy remains a priority to secure city-state alliances against Greece.
  - tokens:
    - inputTokens: 24483
    - reasoningTokens: 7735
    - outputTokens: 306
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Strategic Landscape**
            
            My current focus is on assessing Japan's position at turn 396 in the Atomic Era of Civ V Vox Populi. I'm evaluating Oda Nobunaga's standing and identifying immediate strategic opportunities and challenges.
            
            **Refining Policy Choices**
            
            I'm currently reviewing our social policies. It appears "Third Alternative" was incorrectly identified as a policy; it's an Autocracy Tenet. I need to finalize our next policy acquisition within five turns and re-evaluate our overall branch progression, given our substantial gold reserves.
            
            **Evaluating Financial Status**
            
            My analysis reveals our gold reserves are significantly higher than initially stated, at 1058 gold with a substantial +332 gold per turn. This necessitates a re-evaluation of our research and policy choices to ensure optimal efficiency towards our Space Race victory. I am also prioritizing a clearer understanding of our primary victory condition.
            
            **Assessing Cultural Threat**
            
            I'm re-evaluating Ethiopia's cultural victory progress. While they have widespread influence, the critical "Citizen Earth Protocol" wonder appears unbuilt. I need to confirm their ideology tenets and production queues to definitively assess the immediate threat and adjust our strategy accordingly.
            
            **Escalating Conflict Pursuit**
            
            I've realized we're already at war with Ethiopia, which simplifies things. My focus is now on leveraging this conflict to prevent their cultural victory, likely by capturing their cities or at least maintaining the war to disrupt their progress. I'm assessing our current military strength against their potential, considering our unit shortages and lack of transports.
            
            **Clarifying Victory Paths**
            
            I'm re-examining our victory conditions. The United Nations election doesn't automatically grant World Leader status, but involves collective production. My primary focus now is confirming our chosen Grand Strategy, currently Spaceship, and ensuring our research into Nuclear Fission is prioritized to unlock our unique Yamato units.
            
            **Selecting Next Research**
            
            My thoughts are now focused on selecting the next technology after Nuclear Fission, considering its completion. I'm weighing Combined Arms, Electronics, and Computers, evaluating their benefits for a Spaceship victory or potential Conquest, and how they align with our Autocracy tenets like "Police State."
            
            **Refining Policy Acquisition**
            
            I'm re-examining our policy choices, specifically confirming "Third Alternative" is an Autocracy Tenet, not a standard policy. I need to finalize our next policy acquisition within five turns, carefully considering the available Autocracy tenets and other branching options, given our substantial gold reserves and focus on a Spaceship victory.
            
            **Prioritizing Autocracy Tenets**
            
            I'm evaluating the remaining Autocracy Tenets. While "Third Alternative" offers significant maintenance and resource benefits, I'm weighing it against options like "Total War" or "Lightning Warfare" for their combat bonuses, considering our current unit count and strategic needs.
            
            **Adjusting Diplomatic Stances**
            
            I'm reviewing our diplomatic standings with other major civilizations and city-states. My priority is to formalize our relationships to support our strategic goals, specifically planning to prepare for conflict with Greece and Ethiopia while strengthening alliances with Mongolia and the Ottomans. I am also investigating the possibility of adjusting diplomatic modifiers for city-states.
            
            **Clarifying Diplomatic Targets**
            
            I'm refining our diplomatic focus to target only major civilizations for relationship adjustments. I've confirmed our existing high standing with Songhai, the Ottomans, and Mongolia, and identified Greece and Ethiopia as critical adversaries, aligning with our immediate strategic objectives.
            
            **Analyzing Diplomatic Levers**
            
            I'm focused on leveraging diplomatic tools to manage our relationships. With Greece and Ethiopia as adversaries, and strong alliances with Mongolia, the Ottomans, and Songhai, my priority is fine-tuning our interactions to support our victory condition. I'm also evaluating the potential impact of vassal states on our diplomatic stance.
            
            **Choosing Next Tech Path**
            
            I'm prioritizing our next technology. Given Ethiopia and Greece's proximity and our ongoing conflict, Combined Arms seems most beneficial for unlocking Tanks and crucial air units for immediate land-based offensive operations, despite the allure of Computers' trade route bonuses.
            
            **Selecting Next Tech**
            
            I've decided to prioritize researching Combined Arms. This will unlock Tanks and critical air units, bolstering our land offensive capabilities against Ethiopia. I'm confident this choice aligns best with our immediate strategic needs and victory condition, despite other technological allure.
            
            **Finalizing Policy Choice**
            
            My current thought process is to finalize our next social policy acquisition. Given our substantial gold reserves and the imminent completion of our current research, I'm confirming "Third Alternative" as our next policy, focusing on its powerful strategic resource and unit maintenance benefits.
            
            **Confirming Policy Selection**
            
            My current focus is locking in "Third Alternative" as our next policy. I've thoroughly considered "Total War" and "Lightning Warfare," but the immediate need to manage unit maintenance and secure strategic resources for advanced units outweighs their benefits, especially given our current unit count.
            
            **Revising Victory Strategy**
            
            My thoughts have shifted dramatically; Ethiopia has already met the primary condition for a Cultural Victory. I must re-evaluate our Spaceship focus and consider how to pivot our strategy to counter their overwhelming cultural influence.
            
            **Shifting Grand Strategy**
            
            I realize my previous focus on a Spaceship victory is now secondary. Ethiopia is poised for a Cultural Victory, but critically lacks key Tier 3 tenets and the Citizen Earth Protocol wonder. This presents a vital window to pivot to a Conquest strategy and launch a decisive offensive to prevent their win.
            
            **Prioritizing Offensive War**
            
            I'm realizing that Ethiopia's cultural victory is an immediate threat, despite our scientific progress. My focus is now on pivoting to a Conquest strategy and launching a decisive offensive to prevent their win, leveraging our high military and production flavors.
            
            **Prioritizing Offensive War**
            
            I'm realizing that Ethiopia's cultural victory is an immediate threat, despite our scientific progress. My focus is now on pivoting to a Conquest strategy and launching a decisive offensive to prevent their win, leveraging our high military and production flavors. This also aligns with unlocking powerful naval units like the Yamato once Nuclear Fission is complete, which will aid in amphibious assaults.
            
            **Adjusting Strategy Priorities**
            
            I am now prioritizing a Conquest victory over a Spaceship one, given Ethiopia's imminent Cultural win. My focus is on leveraging our high military and production capabilities for a decisive offensive, and I will lower our nuclear-related flavors to avoid catastrophic consequences.
            
            **Revising Flavor Settings**
            
            I'm adjusting our AI flavor settings to reflect the pivot to a Conquest victory. Nuclear flavors are being minimized, while offense and mobilization are maximized to ensure rapid military buildup and aggressive action against Ethiopia. We'll also slightly boost culture to counter their influence.
            
            **Preparing for World Congress**
            
            I am reviewing upcoming World Congress proposals. Greece's United Nations vote is a concern given their delegate count, while Mongolia's Decolonization proposal presents an opportunity to reset influence and disrupt enemy alliances with city-states. I am also considering our own voting strategy.
            
            **Opposing Critical Congress Proposals**
            
            I'm intensely focused on the upcoming World Congress, particularly opposing Ethiopia's dangerous Passport System proposal, which would accelerate their Cultural Victory. I'm also reviewing Greece's Sphere of Influence on city-states, noting their enactments and pending actions. My priority is to secure alliances with Antwerp and strengthen ties with existing friends like Zurich and Veligrad.
            
            **Securing Diplomatic Advantage**
            
            My current focus is consolidating our diplomatic strength. With 7 delegates already secured and a low cost to ally Antwerp for an eighth, I'm prioritizing maintaining high diplomatic investment. This powerful four-way coalition against Greece and Ethiopia is crucial, especially given our hostile stances towards them and their vassal states.
            
            **Launching Decisive Offensives**
            
            My focus is on initiating aggressive offensives against Ethiopia's cities to halt their impending cultural victory. I am also finalizing "Third Alternative" as our next policy, which will significantly boost our strategic resource yields and reduce unit maintenance, and adjusting our Grand Strategy and AI flavors to heavily prioritize Conquest and military mobilization.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: LBkKiFvNaOdg7wMi
          - toolName: set-research
          - input:
            - Technology: Combined Arms
            - Rationale: Researching Combined Arms next will unlock the Tank, providing us with a highly effective, fast-moving land unit to launch powerful offensives against Ethiopia's cities. This is vital to halting their imminent cultural victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: qFS4QOa3QBr9iPso
          - toolName: set-policy
          - input:
            - Rationale: Selecting the Third Alternative tenet is essential for our large military force. It will double our strategic resource yields (critical for building advanced tanks, planes, and Yamato battleships) and reduce unit upkeep costs by 25%, maintaining a healthy treasury for city-state investments.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: tk8gp1JFlErx155j
          - toolName: set-flavors
          - input:
            - Flavors:
              - Offense: 90
              - Diplomacy: 95
              - Culture: 35
              - Nuke: 0
              - Production: 90
              - Science: 85
              - Mobilization: 90
              - UseNuke: 0
            - GrandStrategy: Conquest
            - Rationale: We are pivoting our Grand Strategy to Conquest to launch a decisive military campaign against Ethiopia, who is extremely close to a Cultural Victory. We must seize their cities and Great Works to neutralize this threat. Offense and Mobilization are maximized to speed up land and naval unit production, while Science and Production remain high to support modern warfare. Crucially, we set Nuke and UseNuke to 0 to completely renounce nuclear weapons, avoiding their catastrophic, indiscriminate, and unethical harm to civilian populations and the environment. Diplomacy remains a priority to secure city-state alliances against Greece.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: LBkKiFvNaOdg7wMi
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
          - toolCallId: qFS4QOa3QBr9iPso
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: tk8gp1JFlErx155j
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.