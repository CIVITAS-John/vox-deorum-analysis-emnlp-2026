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
  - replay_nuke: 80.0
  - replay_use_nuke: 65.0
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
        - Rationale: Researching Computers next will grant us an extra trade route to boost our gold income and unlock the Carrier for naval dominance, while paving the way to Satellites and the Hubble Space Telescope for our Spaceship victory.
        - Technology: Computers
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Third Alternative
        - Rationale: Adopting Third Alternative next is crucial to double our strategic resource yields (including paper and coal/oil) and reduce our military unit gold maintenance by 25%, which will sustain our massive offensive against Ethiopia.
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Mobilization: 100
          - Production: 95
          - Offense: 90
          - Gold: 90
          - Espionage: 80
          - Science: 95
          - Spaceship: 90
          - Diplomacy: 95
        - GrandStrategy: Spaceship
      - rationale: We maintain our long-term Spaceship victory path, but urgently shift our tactical focus to maximum offensive posture and military mobilization to counter and eliminate the imminent cultural victory threat of Ethiopia. High production, science, and gold will sustain this push and our space components, while high diplomacy keeps our city-state alliances intact to rival Greece's delegate lead.
  - tokens:
    - inputTokens: 24447
    - reasoningTokens: 5719
    - outputTokens: 241
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Fission**
            
            I'm prioritizing nuclear fission research, a critical step towards our ultimate Spaceship victory. The current focus is on accelerating this process to gain a decisive technological advantage.
            
            **Analyzing Global Politics**
            
            The diplomatic scene is dominated by Greece's overwhelming lead. I'm evaluating the strength of the anti-Greek coalition, noting their combined delegate count and the proposed UN resolutions. My focus is on understanding how to leverage our recent alliance acquisitions to counter Greece's influence and address the ongoing conflict with Ethiopia.
            
            **Acquiring Alliances**
            
            I've successfully integrated Veligrad as an ally, increasing our influence and delegate count. I'm now assessing the cost and requirements for securing Antwerp's alliance. My immediate focus is on researching technologies that will bolster our victory conditions.
            
            **Choosing Research Direction**
            
            My current thinking is to prioritize Computers for its direct path to Satellites, a critical component for a Science victory. While Electronics offers other benefits, the boost from Satellites seems paramount. I'm confirming Computers is indeed available to research next.
            
            **Evaluating Policy Options**
            
            I'm reviewing our policy choices, specifically the Autocracy Tier 2 options. Given our existing selection of Third Alternative and its significant economic and military benefits, I'm inclined to keep it unless a compelling alternative emerges for our Spaceship strategy.
            
            **Strategic Alignment**
            
            I'm re-evaluating our policy choices in light of our strong Offense and Mobilization flavors, and our overarching Spaceship victory goal. The current plan to research Computers and maintain the Third Alternative policy appears to align well, providing a solid foundation.
            
            **Refining Flavors**
            
            My thoughts are now focused on optimizing our flavor values. Considering our current strategic objectives and diplomatic landscape, I'm evaluating potential adjustments to ensure they align perfectly with our pursuit of a Spaceship victory and effective counter-strategies against Greece.
            
            **Selecting Next Technology**
            
            I am confirming that `Computers` is indeed the optimal next technology after `Nuclear Fission`, as it unlocks key units and trade route benefits crucial for our science victory, while also paving the way for `Satellites`.
            
            **Adjusting Relationships**
            
            I'm reviewing our diplomatic standing. Since our allies are stable, I'm focusing on Greece. They are our main competitor, and while currently hostile, I'm evaluating if any relationship adjustment is even possible or worthwhile at this stage.
            
            **Adjusting Persona**
            
            My thoughts are now centered on persona adjustments. Given our aggressive stance and ongoing conflict with Ethiopia, I'm considering how to best represent this. Our current high friendliness, while beneficial for allies, might be a mismatch for our war posture. I need to assess if a more appropriate persona would serve our immediate goals better.
            
            **Assessing Victory Conditions**
            
            I am re-evaluating Ethiopia's cultural victory progress. They've achieved influence with all seven other civilizations and seem poised to win, despite my focus on a Spaceship victory. I need to understand their specific requirements and how close they truly are to completion.
            
            **Investigating Victory Path**
            
            My attention is now fixed on Ethiopia's cultural victory. They have achieved widespread influence, yet the crucial Citizen Earth Protocol wonder remains unstarted according to our intel. This is a critical juncture requiring immediate military action to disrupt their win condition.
            
            **Prioritizing Military Action**
            
            My focus has shifted entirely to disrupting Ethiopia's cultural victory. Despite strong flavors in production and mobilization, their looming win condition necessitates an immediate military offensive. I need to assess if prioritizing troops over spaceship components is the necessary trade-off now.
            
            **Adjusting Flavors**
            
            My current thinking is to dramatically boost Offense, Mobilization, and Production flavors to 90-100. This is a tactical shift to counter Ethiopia's cultural victory, while maintaining our long-term Spaceship goal. Science must also remain high at 95 to keep pace.
            
            **Prioritizing Diplomatic Influence**
            
            My current focus is on reinforcing our diplomatic standing, especially against Greece's overwhelming delegate count. I'm ensuring our Diplomacy flavor remains high to secure city-state alliances, a crucial countermeasure to their diplomatic victory ambitions, and am closely monitoring proposed resolutions like the United Nations.
            
            **Adjusting Strategy Focus**
            
            I'm finalizing my plan. Computers remain the top research priority. Crucially, I'm re-allocating our strategic focus through advanced flavor adjustments, heavily prioritizing Offense, Mobilization, and Production to decisively counter Ethiopia's cultural victory while still maintaining high Science and Diplomacy.
            
            **Finalizing Grand Strategy**
            
            I am confirming the research of Computers as our next technological pursuit. Simultaneously, I'm enacting a significant flavor adjustment, heavily emphasizing Offense, Mobilization, Production, and Science to counter Ethiopia's cultural victory while safeguarding our ultimate Spaceship goal.
            
            **Confirming Tech Path**
            
            My focus is on confirming `Computers` as the next technology. Simultaneously, I'm ensuring our flavor settings remain optimized, heavily favoring Offense, Mobilization, Production, and Science to counter Ethiopia's cultural victory, all while sustaining high Diplomacy to counter Greece's delegate advantage and keep our Spaceship victory on track.
            
            **Executing Grand Strategy**
            
            My current focus is on executing the finalized plan. I am confirming the research of `Computers` and implementing the critical flavor adjustments to heavily emphasize Offense, Mobilization, Production, and Science. This decisive action aims to counter Ethiopia's cultural victory while maintaining high Diplomacy against Greece and safeguarding our Spaceship victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: GNZ4e3T6AjMyjmzr
          - toolName: set-research
          - input:
            - Rationale: Researching Computers next will grant us an extra trade route to boost our gold income and unlock the Carrier for naval dominance, while paving the way to Satellites and the Hubble Space Telescope for our Spaceship victory.
            - Technology: Computers
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/Ta82YquvVTYrzZe6bD4J24n6N7GVFib3MJVJe/o4ZgrZWUjfe8DRO8QuAlje+2iJ3C4myP5K8pYafFw/0ZtRT0u8AlX4Wc0P6frHVGICJBhBOFaJPmofJ+pF9RCO+Hnd2Q/GUK9bI93VDBO0Ej682TEp8dvK4XZMP6Ce1oc2JiLXUh8vdT8JAsL9g6qKXAP46DRowlFV/iWg9/0ep57iT5WhC/qV8cj25qQgcCFd+BGqalf4Sxpsec7ZvGA0DSeDFUxJR95QvhLEQ5lsvn1QNUxtxOx92TdLhdLGDCfDdAsVRZZkOs8i7CkLXA3SSE5cxVhtuGTG/VkEGTMxPPRQcNMgEn5DvzoU7vf1LD7Pq81HLEROVg4pNifiw3lcEn4wgi5ly7uTL5dHJCqomkGm1zq/4udATNwuBRkcrBpUYrWhmA4Tf/N0zfPLb5UENZYjdj/WOCOBFXBTlhqLys4RpPjcFvjvRZ0FQXdp0K+O0ojiKBBfsYNsQb8pdZFw6VivMKKf7ePTPst/yWLjirox3RYXS33wy5tF7URG2sGI5MuwwJ7i1SVL7s8EpC/ZpLOBEpiO1UBnkizzJv2x+cYF/J/v6u/fsDFwYhoqZ0cl9HQusXAxkN/ACxw2MNLRJquGzYc9JEvP2fjSQb+i/3f/dnRcRW8c0tEPFWlXcsFiPVQD/ij9qCWnB5LOOR2QzL1jIaS6tSYVd2+D+iXLjNVJW0v/NEYvUMd1Frcn4hn1ioThQ9uEaHOx/q7U8BjvYh8PgJmIT6I0GBJldhgHYAXvUy4N5b+1R2GK2puJD5hRiN+Rwf+EIe1npsQPjr4SHAW021gLzeFm9fH/elU0gYOi52fp2JTkb3jB7j9gVICIv3U8vE1dKMzJUn5sSO+WsZSs1p8grlzpTdtEQPmQHShMT9loSUoyxFNt7ADAX673ZRbhoQOgh8KWrDytmVl96XxxHAxGt+miuCbQdQ7LvxplggrKqFmBdBQAKG6LVGN5fWTHweNwXc6cqE1SS75hWsoj1zbZNkuid77yxMwGVLQsguj21x86j9xsFr9GcLo5wN6uyZSFkcNgXt/BPRMKss7twUgE7SERm/oobxvYIwH23wRVT1dTqvJ3cLqtDdHlzW1tLa7ItSHliHhFBFjA4rYqT8m5g29MN1Rv4kGcuYEDliBcqugzhlRKr63lGrCFVUyEhtJV0yIHmb7RoDSYrN3WB4wmDVVBrKZcW6N4SmtLpo3DFeOcZbkakLiGEOuTc6bNCBQ5Sb6wnht1W7xUd5SC83Nhsjs77j0TYuXpeyt7ORvwH75EleMP1PWb28S55422/FI6P5xlZZRK1zyiXdXEU3u6Y4gwZYuk4N1NHIQGUt6MhtHibZ2OucSNFNFpPmOla7KBpgDI7yLlMEGHXKCk54kV8v0+yBrJQ6KxbBls01Yv5m6qf965ZcOSWgZUR/ml6ABZFE9hEGJhNl2v+tdzv7RRXaNKzpqA1N2H4xxPZR96EzkmeTmGUgggp8OvLODuWZD3VMz1fd22uxGmSv5kbUskqiS4N/l7vPbDPeSQIx6iE9ijnnB8P+AO0+7LNbM3poyf1fs2B+7Le9Jh9DQb7t1YePOntVIt16FdKY0kaLr020ssJYbuuvb6nbnkgkooj0GW7J2Sg79a7CMX3zRivT9qvNI4KJKo+lI4UFIcD6Vn5D42OnCRvXdhU28hKS9QxgOtUGbZj1TI08Jci1Zk5Ba7c1e3idazil9/IfP7ndUIYY8+X16h4LnDcQ77NfgUh7wNG+U7W5UNyzYlCAsnuYE5RTgABZicVnjvlTSjdheT8qoFgi1AR4ROgeVAP+7PDCTYpoKC5uaqzn8j6lXJUdIjVG87D070+Ep5GevJUTijvcmYETOMJB2hH/7eWoLwgAc2eDUpC2Kh9IpmDK7DmaNVkd+vhmkUxVmtUvrEvkAAMSPhtjzOyPpxsUxToshldTG8IYkHlaGHpWjVse+sBqqNE1h7sgtyXKGpafCHsOPnUNMuqYBFVp5occr29O8P3rjO0YJA5OCpt7e0idjNHBQ4pKIutO6FxT/oRSSfBTK8ykYKbdwktlCqKqVWxwlKWIwWNGe61UBmj69ShBErBVMhvO0ir++JxZ/VpPGAuuhou99Pv5swK5iFuy2ezfdnXekaX60yby//ijlcqVRe4wAtiMw2uZQfkNBOoUAKQJYWuj7F7karQGQhfsWoex58TOHFd29Ifibef45AYifoksFztEc1bGXPtaXz9O/cIdACzVTT34Qp1VYiOtNvoea1M3I73hAbKERY2UOGV4l7M+kz3ZCiWYhJrRX7STuuqrXPK3dIGgpqo7kwCljivoYgTBSzPhAA7FmaA/MbPB/svd2RHsoo1IFrfZeesOJ3C49tL1+g589bROnwF7eG0as4myjgoe6VwV0WBs2cg0H+E/BQfi99ztFviNLpX2O3V5Qo41dB6KLQzkcq9tYm8TVP3y0IpWxkNhPAz/p9HUKPEE3lpHkCAq6977MBxwdo7oQb84QDMRrJYuh+otpLRLdAWbpcou+I+QVBpebT6gg9TVEoHZo26dOWvnLLM2msCBDmk6ubPspqAs7WvPKYHBpU9WtWv3N/tokptpoBsHgTV+mhZL21RkjhrSKCCD4lvlrdyd6uoNTjZs9SMzQKVcdabRbfEivP6di1bF4lBP6P8x7DcRHXw1SBRpHJa7/Rkdh0nCOP+ZUxiATXGvegrNz7+MUbsDbyDfoorrNjtLpbKdPXGSSD6FdF/HiEf0+8Y12ho+AkEnHSZ4FM+b8+TjATbRxKxw2lUKCxBtmPvdFwUbUc8HJDRxYjDt15SvrWHleLe9kQVInhl/C1xKKRJ4sZl+5cJoU5q7dSNDc4mltBjHACRcp1tN1w//414SIu7dZOJokLHWhtDA00BSj9Zpc7oOIhbdeTYLrTvV39CwbDhxe/zBRG3b/Iyb0szrLK98tO6d2A3zB9NT/uN23dPwqBlSSOI7KMZP9LO0pDjj7psYnSQUgo3yM0WHASzocfbsKzGWBzZVFH9Pl1eYwXY2aCBzeMVmdLp3lNq44dodneyHZvkYh/txVFaTGQVrFXVo/YJbcFNDzFJeWCCNIutmj5GpmIP5qGgmhFZItX0nkkaHGhnqZkuDhQjQVXd859k3+UqfPvA/dTd+tef1Pp6kG+yx5giVMYLL1XNBoWISlojTxOqua5CWKTM8OydCa3+8M7X6MTQCyOYHWSP/Yf8Vtpb0yb1CzrpjfstZU3C0hoNSFKEWVcT7WGAczYGIPhuaB4h1NEONbb9F9MTTj+VwcH6y+SUnRUJIAsb8K5MLFeN0thKeuxmCS0aLqgO60y/uPiNKx07MxtGunY89tOTuLnJY4qSLQCUhw7pPEm9mbYschWK+GdubpZ3k5fdry1hTTvbduvGKFnAmdUZzdsD0SK9D/xT6XojEP6KvOsDmqqZ/C7SwdEuWyS/ZrKKXjBCAJ24GxsWYuEoz4nTFPP6IfOEwTdxttm6I+WeouGKWT7fFyYHD17pGj75Kum7XZTwAhg7S3WfO9+G2PaF2UXX+Udgsp9WGJjoM/3mbzvEBbCNpHmcs1e2KIME/Ymi03zICHb4ea8/RTpytGqJSNIM9FCHWsA+wbMHM8IXbaVErbS1O6BlBNymXkM8PSX11llnwsvaymgM9vvr9dKT9svzFn4tvnph/SuVBQmpg0QMLC+kmtHOdMPR4yxReF+s4paOnKSpBobSXZrhejNfbh1wYlDzgj+/naA5SYzTEw80qJETSX/l0xEGIHiSnqStPektV+f/fbmYjF2f6CSuSre21CWOUntBqH4DNcIJRSvl3u3eyLG34pxT2etYE5eSW4Ne2Omp1smz0twYeA95ExHMUyxX2szmSy/p2oKiI7uWhyFfw7QJUq7CiHgtrYb/tZ5A9Ydn7LCktYTw8nfgG68MYVGzj9dDfzuTsT/Dh4okicBNpU4NkLpQWM6MmBELJhHB8dYloyLpCwfTI8ClsZObZ1ybDOpmqRct8JkC3U7m9LGTzggKUnYG9D27qZ926zOgO4ViK+yK3mndJPQoApHtLGv9DQVtmvsd/gBhiYpAJNwiPhUPfWhapVxhBF0Md1FP0g4rq8vcq0oFSvJGbYarl+0W/iRpZaLLxlQlyaEbjJuhGMv248C4yXPM/00KbQocuxzfRjFS4DA7jwLfLw4ecqJyLY+jUlmaTSol1xmCdVr/2QJhJxls5q+WMy2cql5HimBECA7cPZ/QIPz0OcHrQFljJeVSUMTFhQsdGuDk0PeHv1u/4LrfXHE17a7jh2pQFPne3peO178klqDYRttk0jGHa2WUshBuKEaTT1/6jHs1YszVrPjbsFkZ3FLE6JAouRltcA+uec/l6Hk5iRzU1zvJKi5H8eLWQ9NOCGXIb5yTbBi02yQE5TWO8LhxIqBUu8eByMhogz34ygbumJ4CBIlz25ltxsVgSP4nwMoSutGprWzvXSUIUbbVdL3J5uhKzWH+fDfbh9jCeylarlHwLRrJJqps1VDoVVxZUlc37+vgjNibfiIgohE5sMFVPBknVM5JLsty1jOYmI8FXCzn99RWbIa5NsLf02sX/EAxypAtxjqq1zOK08W/WPuVeocWWFa+QA02RE4Eb8AspsPm8PqGS5i7BddaWIHMiJaD5KnU1qzj4+OzTa5Ount2l7JXkJyxUJ8bPjUeYtuh7l4/HSSJbl8o9vrXizvm4KfSLPzGNM9fBVkkgKlDljBYs/4t7pm4mx6JHOwA27zedSf23b8t3d5nvxVmBwBCAAUkwKTx90woBG8JWNxsTvdDXLw7Cs53Rf+4Gl1ht0V4j/v1/8xrV/J7K7dSk0B6DUCzc3g4Ikw9MUQOUQWNslogzsyl/H9R3L9UDI0ZkhBEEnTX6je05tpbJZ5dcRVmnb3CWpo6qItA2nflX2GPNCV/gatNeLOB9Pjs0YglYJWAJrOz1Hurgj8KzuDzLSOS1F9471sSEu4I0cTwVfpcNUQk2m3uieOjVYjhpOI3rPMqVW7AvbRNvC8SZMalKINHnNKGj++ns2s/lsjoiIcbosHZcZooNV4xtn3V0QB672Z7NkTrhG91q+cdyZXCbCG1giaLV/31A88k8dyTJhDsN4uuridPR3iFewTS2fRMDuXgHZ2AqYhkFzE900glAMesQGLbCMDy+/pRJ7TFyfBLKuj/qLk7oq1rbIN+Mn64MGnmgELYDmxRDwabjLWgJAb9wuUpBjFOq6T9RjMtVjoFhZd80qG8Q1hH1hABC2TAkhC92i7PE/umGb5+ZwlsAlZLLuHzXFg+ruuE4Y9DpkWNnWdStfEmN1kD6lAyc8O38/cPnx5gTjGId4ubghhBCycHWUWg6xnavHoL1vdHMvT0b4cX+OE4pLe8Bd7qsDizKH5zYTnZUu2OPqTep/YYbbls+he25uu8TSzOjNG5ZW3v33DON5xmwzj1IksTtviVddzj+K0ExtxAVzHFc+khYx3N1bUsjq/ARVMdDKP0zcgIb6Us+z66zmIHFcX+5EsVf07pQ7/ncKij5FvAHQMPUxf/x15ueKRzxmzpBo1e1OgfrD6UxXo+4+QFUjW5ShpWf+WeiWPDvjmdlGgY4AcNBjh/X4MdNtcIM2NPEah8BXXPhxt3k4Oh4Dv2W9rwIvLeLLkw7fdoKrX9A2Mt2S47o+527LTmBDmk9EdfYvpdkaXiaxHFx2jDwgEXMm62+s8dGR2OcZyM2uF1LLqyAO411dTo08H9yjsPDI+VA3Fuo5erjh3a4FB14soMW1bUa+sRGjfTelgU2huPg7Fcy+aUsHjTiAwrVT6erkSKaOeR9z96GDr0uq5TOry2vlt+gJ11xmX+2XTBAyL/PIPfxp5j0Swnxjv2yrfHR845lHYiAke8FwHrIOkwT1CgMXL/E2E7m4QirbGm/2ez/ZWBn6mcqxGU5ukGqValY8O8NC8W1FCVI2I5d4urm15gXwMvTBT6DcvATqlJsU8wyXnmCbd1tUax3aUOohvI73XWrRpNoxOHhNAQZBZxZQU+VaYqL0caMMhv+DNRvXWAg2B8Nr++EfoJ1twb+7XLjQ2cKv8VslibCTSMiEKPxt/3tuRH7VNQEPHl1xy4l1S+uKCNM/wAgdo0TAnTLw95M5sVilJhLGgbIYUITzW9Ai9Og7LFaAlpM5C8SgQ6uvTh0vX2L6IQBBx56x+qbZDv3OTeFkz/xP6MXKACi90V92k7BlytwwCdOyZdpzR8Pr47TsomN9laj8a1mkfOxPiM8SMm7Pk5Su/bM733HdhiSzAh/1W/D14YoWNyRcuhhiymdXMg4orweNQSdkIWRaosB6646WCGqlxDqSHi97dw9rTvAeumy96RJgxtvsHgwO0iDnxyOKESDaPd2EfMiIUw2aFzkmr5/MTmBSgrXYyON52CrqDZ9Nt5AANWtxH1kveTnCHXVAT0wTIh5EArSKw0dMy0NYS00XDSs94tfsBqFBMST6YkCyWsQj38sdSTCAWFBQQpJNNaVBvG48u543HKteFBcZ1QC/W4M/kPqP8vQHQ4mCrY6/C8r8ZpgpxwbKyhfIVWITopdXFF1zfO1kCgZ6QBA4AG3gwxf/HAZSf/hQe7yIwXCTU9VB5vur0atPlJK/Qs+Mqa5e1BWWevSlZxVrZozZgW1/5GoWoPV/Ahk6R+WDPrcV24ZGTNvGDiyUEOTIjHK2xJFsdAb9pvT/Pc+svQD8E2LOnvGZS9ns7Q40j0TdlXU1sVcMf50lgeYfCzQ6GbQuqPJLL5jhvCQA2geZ+Iltf49m9S9YjtaVwCG2W5PmNBZpm6LeoIiJT0NIhV9zPWR24a3uhcg6go3x7kQgkn3fUuMimnEiwObfbsDPoe93/G2HOhOsdp7WIx4foOY1VC5RFEj/SRaKjWhB4pKyDFvR6BanMQ890x9kEQI2oRHKlXF4OFSZqapU3pGbRxXH5KD6qpvCZK6Uu6Z+n6TJHOKGlO9JexZtTsTdztu02s7ynHSCRCpNo0ycp5IpECBdFyiMcGGW6/KkelX8VXtzPchA45D0xCk3XtPmjaAPsNUSUVRp+6+qYWWuvV31dmhiQVpOiSJ09QTVy5Tvus+57rwOtV9+74B8CsxVvA80olR0unTdd/a7p3kVngTlFcCmIaHSnM6MpequyVTfwm2CzYhlZWXmkkxqNRQhtZ3ORCmDUF/nfJijaZNsoGAEzHkvHdbjTRCOn3hP7CTUgS0YEwBI4fzAPgf1xBNVcbM+xvGOVeTgu3EzPb7H4El6HpzWAHKBS9BLvs8JYdlU+7ewqhQ3B8ZAj9zAilK/VUSjeapbdDnM8eRIp/zP4zs11gZ9oxr43US0EhTgJvFygzIPj5jD7By5b8yzHS8W4YiqY3pPMi7UcLMwTU/Dh3O2htgzC575wLttTv05DDFHJl8HAaGZvQWQ2Y1LUlo8etXZa9Hg9kG9JfvASm3jKYEu1EXin/0WFJXbdG/sDeIeuUDS9LMYE6AlmD1rw4mXICBASm+c/u8R6WxIq/+MIRCYNaQv+tHMeOtFmAN0E/KbnFmeiBmNeEskCCxx3Uy/Ze3uuafjJZqvy1ztyAotsWtNiJLS9HL9jP++QniIJgXNDvgogGZ5bSkLbCf5oaSbXQKshnxAHnWus3RxCcLkDfIjKNYRyHOO8nMgKQaQjt9Bflkd+vezcZS4spmPe+z2za4QW3YxOiWyqcMC62EgSCl6iAd2nWSF8Hy25RbZMocwd3WTjZAxCcyleYYcAGzFW7jE7xJRPrOHN3V6ZSOMZhKInruv/pUTiMron7uJnd1VJKqD6So1Q82OXK5NZ4D6cEPk8FVhy6YDxKu70C5J6dietUoR730nExNfkJ9IJVllafqmkwOt/gYJRgrDk4i+5yzh4qSrtbM8IT4APo5mZxIXCCRuD8TH/9eVR+M66Fj92mc96dt1qReIoD3qJKpPqcatkWssm2G0dMhiE5OQu6OY4TwiSmvTMni428KsMvJAgovLB2T8/S1k/EnmTlsQG8gGR4VtrXQI+dCnnVEy3ZB40hZljEPwoVSfBH3Qm6sQVxKpcLMpg/4z1UVTLNqxD7mzM4VFklFYD4sQNdEx14u4BnKD2X99YVZES9m+sYAHyF3ItsyLXOARiCFASfbmyG+WQ63zl+GWsSNuSWNCyg1Sz1J9Jfq81iFizD6gUK4L2asBiKepytAMAlghDa2XgAg+wJD4PC3/DZ3GY59UcMWK6jVvmx70wCtxmYZ/ZmCaUufMUIzb4K1ayEd0UYuyYjaU8cez6LuKcoARBm/saUgnaAliMCTshnIcHcMASLwY6xUHB3vk8rxu0bftCx7mu9comhpsgobXY1a4eQqI54J5PHNjwXCXtKUCGEmeI134mH5XXY3Rpj8L0n7yw8zjW3gC/AAEnMl7FqOWAbAg/8PDFSjfLEXNaxLcidaFQQ1sEtEvwzKzIfAyIOYgkD9rRG46795DAme9aJKuECC4173aCysv7evjETpMres1eqDe1XXq45hUNbtI10Z6bpFyn1piTQxWs7YC3hICHZ7psoY94Ue1mAzTCxPhnlvKemH0uCYzlcGM4DuAXQl2FoOlhzgC4J3d0xugKp/pFjOD9CYcJRv+QhuJJabfum5XJlWZy5wNzw2iYQ5YzfEF8+0urlUMGaBpCEXeDq1zq9pVw0Krx7145LXHLZmqJcOjhgKN/ir2g3ODIlYZziC8E1nASaDyKdW8kGLUsox8StzEIoFMEsjQmcykEFTFFcAXKnogmGwWo7B9mSZsQEKTSkabJRPTrTyQqN45kCucoiOyt1YOJEnpNZLRanrviYbs0L1PlYI0ahdBRbLLzihz5AqMjm5if2VVg1irtfXC1QMqE39Gn9rj5H0u0QA2T0E1ZweUmXSutSvRtYAElAjcstPwxdg2RW7pNzyDVjApDkDHKMdL4Eip0RynXPNZjGnMX1ATKh1iK3O7xFeyww10zI7b7PDAWi/6NpBrFVbVMC2UsesSWmqFFRv7/Llb6wbD/MSzJ1V46PI+WyCM2zXarhSLJqCFQAjvrkcvMip19ELMDBi9ae0UiJhXNV9lZwfDTO/LpecLSB9PSqq0Mmm5z/I2fpk4TcE6XXGj1rC1MlARoxk2WroDh+8JZP3AzXwqUILrJ1Bvo5tjOSpY55WwtXlMXS5AuThdH1XP3lGh32bi/ATqPTft6r9EPZdN78e6b0MN9RSDE1BcuGLZz+8b1mOkzdvlcvmzt1LguVCBY/HmuGJgzrbaTg2xweFCI20uH+JcmRgeG5hnGsIjhPkBjpBMltwK83CklAXPwYIf9MOQ62PE4o8f9KjZqZRhW9v/h6OpDsxX56YdgrdrQWOLW3jsW4IlKh33Y7JvcFY4lfm9iYFpKY/cq6xC58kpB/3UPB3k5x6Un0SRxg8rl62vVjKVPSM7vywJ1C5ZPM9H8uVZtG1SlnCQnmzt87VEzyCmjaKVds4vyYslno0MERuRMUQVXNwiGkKum/R9DI3FrOxEb28fqUR210SZrz4XfXEpQg/DFG1rAPBm8ARcDv+EP4jGJAmtDBiCcntlG/2SckrzuSMuFEXuoWmzdJ0wguTPpzHCeKjaokqfUchDoxgPV+DUfn87whXItWw53MRybEtmdRa0WZHf7xOL016x2+TDCUZuqocCxcg00MFw7lSqMcyhnTvxXb53DQKEvtecobYrgnSaVPkbQwbOPqYJtghfHA4pHUpgQL4wkp09SeZrMyPCH5OWWSqzCbSg0QvfQhtpzL69TICVzTl6Fp1Icc8V1HD/SG4hoaWfuxNDSODM/8USD9lJGFNm2Ao2E1SRdBFoI4RYIFn5M4kLDtIvDeYCKT/tzi7swZtdNciKJLQ6zFVGJr6iXH86qCB/aBq+1VjE3D25+HUPnIorkgbdhpxfT9lGIutOQ4lq8VvUKUG33Pg3NB3pJeBXIPYdsbehuc+JZhUnuFVHS2lgjECfve8uglHfqeIxvMHX6bBMqCiWRyyAU8mgIMqN7bv69gxqsQ5R/RZhfDCcEc2ARzUxIjVSVpuynBush7o+NHcPZGRdneLX4sBKezQYyZOwUGDemjw6NP6IQK3CMybCo/4PmzlwuoZR7RHJ4z2g4fHAvx6GgMlZN5vz6kNg5UUYpvdCYqtagoQH9i981+0yB+UpxULaeY/l0lLtxujNBZX890pjNh+qLAebICG12p7ccq2UiKmcliVT1dX9Zf2Duuy2j2sleeg1vMm06i+jWFRYmPZTBjZ3WBqve0jIv5hexngJtLvzB2uYIZMcO/QYQXeBmkEywpH0smscWD3/jvqq4BctKNLK3smG0PUsjO9RkFF4FFyDnQZeZwAB5Ft+8aiqLFh2eghEQwHFK3x4WD4CdW1KGX+hTTQ54OE5C9LdQ37AMd3xInFsTDIhvba+ur1Su61B+Elq6x8ay7ySZdKDzJRsf3RYimHXYwP1JAZZ/ogjUK8+bspPiba9U9lpIBiGHrRH8Rhj1K30apQMrIR+Po4YqQeVRqKXBreThjGENN1EwPvYFShEAKyYseep7DcGjSfo5yCSpvg6JCo22LMvbAzkS4ELuxdxkvZDpqUmRAPuiv5rCYq0SV2oKzSTPF1hUspCSKYQ6tGWDbTv03KvCKfetuIPzh/GYK9jzz0D52Q/RJ0ggiGIxK5jUYp7i2fq/suIhAeIZK2o0vGDYmpGV5kcBS0qEAlrw1gQzAx0Q6RxRz5ZTxfDFXsb/s8CDUelOY2hDVeSdJu99mEXiAXeHnKaYt7tbDDvG8Ca1WnNWQGPcfvhHPEcHCKJBEus2AVUTS0dom22clrLZcAszX2LG/z+ZW3PioQkWPyNMBLqVUXsl4Tjss3DnUHYtuyN7xM0dW8iAC2Lt5CGu7R2R2BLD3Mr4s5hafukJi33RqBzz/BUlrpql903FZTGTvDW1xpPj4QgLajhvgRul0G7K0C68KvRcDkojObfnVFI5RtGcO99rEXWSt/QJzWphS86obtF6IUgqhoJ3KClQ05MGf+VbMXXxJEHpawmY4slm6aqlB+da+5HhhaHo6VV6OQTvCdBmkSknfBvLAz2E4r06GFdr6uGIZoKvjKLix9g6OO8Lrk3TZzRQIMGAod6zi3eenO1MPq+NErr+bvrtaTSw6kFjsfgqb26kuUwrpU6UH9zIBKawkJHqrGrv/JKu8CB6JuwuHuil32Sfpg3Cu8AGRgS5m8+ADplO5nGqESxFhO9lnBlO7+lK6Xto7B6zAnWAmYSQ37lT76FNOFoRvDa4TxB9pvlZVOQypE4MrpcYf5xq2g0FH7CScDOZBFd+D4mMzdG5HsZrmKXf0ujhYj0OaMGMnJzHoeczD9b/MooZUhXOcU5h3lBUMrY9GTewX71A+UkBuAflxP6OYviyiyNj0tFUCocTP+B/h5uOAKXYpOzNwau1rJ2jf85JioxOuPIzB8Bd9FY5U4XSnuKO2kZ4t/CyKFum0xKgnJvJH77Owqs6gKXAHY2/thBHSnudKW1Mnr1dgfRhC39/o22tmZ/BmTQa8T4IoWn8n0oWGoIfVnOaZ1y6Xrj916516moADk9UdE02nOJnVjFcatnqlx0os1woBReEmcAwPPbvI4JRBtJD3ZYoBk3rsNVrKT8bus3JC2OpBjV2qjNvZXMLzqEb+jtEBE4Wk82iTCgcOQs/0V3VnQxAkgkS0Br0RBt7V22ntIb8sPqZj2KJanVHdjgMT5Es3vKQUnVwMljQ88enn3KT7drH3JN3XdauoFVL3skiFRZSeRdqNjcnIw6RQIcfPnY0SeiOAA6fYVnkqllKASAF+a7T7E4ETFTYkQJdrMNAN67ObdoK+f9C7EZ1GdGmDTIqa4TePy1q+l7sOZI1GYkTM9h1xQ1vqHW0GBed5ca8W/ohgJyz6iAy66jdnj0KFrdtozZ4Te4tmEX3ar4aEXQET3XKdxCIE0x6YjFyGY+rZTXbsjcweSrpTvUfTlizpShjKnhil9ylARDRVFAXixfgWlm4N+KTIx0HgCWi9qOAjNc6hK+Bl1oiNQo4dSbi7ZKFbOfXIMS0GQcw9qpq4ZeC29QuawRBuAyEpDEP702/7S8l9haon6ssE/kgM8j9m/H/cTpTpNxmJgjw7t+6ruOX1LBbwVaEAANJuXkzQtzUz2FEIKFG734gBdmOAd9GTDMb8whh9urT+xAD45nPMvp1gNUXcTBAHjKgn0YI92VtdllRtGh+I8zfVqG6K0bLRk96H2/7OMEAYRAH5zrEeiWBqUz+lW9ytkje8CGAmLNvlspTYXWf7QqzWscs1Z/Wh61c20WGlmZEKY9CkiKQnVI+mGMG+mCqjFi5GEK/wCiSKQMEDABDf8NyrnZsEgmA0yoqpAGHUxopL/49o0LqMsQy1v9lJC/z+NJQGIGFE87tTaXZTrgdszj9XyeIJBDFNzFzyOzCq+1dP8d5flhGCErzyBK9XnVfyXax8MZYJ9oDKWCOHb9hi2COnaH7KqXhd2okIGHG7Xe/gwfzhVkI4kkfVbA9ZqOs7Blf6ZtGZ6ggNLUlC/mvcULO71KTNakEQwimG/GdqyvNlpYmX9seue1y9hv+BoLEtdr86Ng9WviKxr/Dqb8DPqoovC0De9T65yc0vgBqY7iHfjXFblnDBpsWXwRYU+gmskJ7jkEnfmaNQsZkboR23XTE2f26xV7479XxlLE3E4vej/W/rAdSfNI4lZGTrngqkbyT+svMdrio0sfYRxRF7uzFwCvFurDUkmCFhNR8A1RC1JORoBFXIg74oaza7Tu97wreEGqcWMBYTtcfXWZcGg/ua4IyY7xJxkAcAUp5e3AEbCTaJ+DDwnOybAap8qw5YQ4iaEdruGoCuntkSpXHyWSPfe1al/XEhV7m6lzvyPsGm1M435XkCq1X+h/cD37AWZ+RBtfeT2Bj+24ecm72fhW//MZwJWzMb8VeQMTtZP2QQ2mN6CNCmy4XxhS0YbDwiyRVSTXDRlUXe4Kx6NqoL0ipBdebGnz/zh2ju/JuIx4rvq1ywVxfQrXyojfLGBFBvTxl1LMa0+XcsB3byY2mS/w1uZb60IrC4j4lyItywNH7xJlQLakDotmOFXlR3zcV4cENuw+OIOZuAQzym31bwaW0fq7yo/Ij9Jtx58Pje6RitXgU8JJ0QB1SkEdlo8HdkF80MtwvDmzkzdJn3A10wTF9VbcOrq9QLA7Gy8gGXvRIttR3oPreG0nf3Jqd1oxrC8pYR75S4CmRuDYA8wrYibVnv3oG7F9asiV7d6yxUrZuGOkTBj+oo0YSnvH2zcqY1egRZpJ0hlrygnMO4htSTaeyZx2iLETt69sTfvQORVvcs9Ph0G3KMujuH89sbFrqmmiaoxvZWILyNlYLcnyA3IX8lj3dh1AWWaRYBZrGTua+Z3onf6m8FMbn2cd3Jl4wUlv9uNHer0q3MbaF6UrNfriSRF/+z2fMCMZVGkDL4HX6JDAA0HBBzteXkmX1yLSTmkvcIz9DS9ve4Exr6Za4lu8+eZwaT2inPbQbde0Gx+lTf21NqnEkAc3dl+UDztu0v19dOMi6gztv9klAAbyymSTc7mj5mODFKOxx4Vc6SiE6pWpCtwLeIPjvRp1EVCS/rYMQvFhyD9aT5NRRDIKmFi391RS6dShgZpaUNRZ6aovvOPreBSI/x3yh6S2u1I2kAX4ZXubvjUsGiSoeCozLV16auQwZRvzmXGJ/16iU5svifspLRU+8oqrRIgBaAXXeYODyzqijbqWwOo6a67w3k9hJl8SZ7eVvxhtHL6q8Ljy0TXaVv8IoKjL8dUqHM3Anv6GGl/FR6/QRXdUfPXm0nP0fa2WnPgX+gWmqiAJhe465u6RfzybxWzMN6WSnr5l8oQJsFzRm/7sUf9Y4T+RLT5DWtzSPOHg6T6FuHstU1Uww6OsLoWAOTA1a0xAIXcfi6oJD0UqXfeZtHbfmh8+oAWPXMQ1kEDgKOIKnaTX+O9SN38f6FWdd/socHWpGzbZM3MktEbBxIaEJNsWtNKesdznWwtWx8qsl8L/BItC8r/3wNxY9UVn/dRpI/SxmXtuB/7H0TqU6y8pruGoOUF1sHz9aED+LsLfoOxe821ISl63uuw4JE6DTDPuepQuEtP/eAcxUxz6BThF8QdeR0DXA/W3YInt4ZQ7+IMwkC0/+/jaa1GxvJcQugseeJosvCsQ5uspXCcSc4o0ttWU2uY7gu4Wk+YSiw5wXinV0sjqlUIaue1URQ/TVC9lZJy0MiLULVXnRvLY7CtOgnbAlZZR8I4Y7KOL6Y+rG5KQuuM8JXeFMht2FldQeOZQItZJEVgLb4sIo7qB6A/MPDJO/yHZu/VtsLN4vNufLK5nT0KjLKQl6iMJIwYLNnYp661SvyX2++zUGRvWzMhtaC3W7FLgyNugasN4ek4cfYCG/YHY/i42JHECvuzJd/m/Rs0ZmBOnxxz4YhUNR492v/O2blkywd5WjGP/PiEAK4YEGbbjOAhOZTave7UGSwydV0nnyTGlIDm0ehUM6BbP+EO0o5w24pbv5MCQ7g8A/3wOEOBisu/ULBRW7C8rad+5V9xnPCDeasGsIRFe3H0hoAkLTpOWRF8PLPxdTEccAPmQAtf3/80c5b1gLgWvQx9wpxbDEMk5GHOC1hsrrgvDx+i1PaEUvSezSSdwgsW4k8w5e3T6hKvAPgOt05RvOe5VfhLbWZ7LlqzABZDKeieyo/61J+B2J1RpXmKhG+q/ouCnS3s/+mGHuhhCuIAv5UXB3T/uwCWz5TPOK2BcCXUf5X9YKTXmq/jkzZD8WLab61vEQiepzSAEAZgKQs6UdJtoZfELVPewT6ruxVLwi1uk7c2A6X27f61fJTuHHxrE0jLf4zJcyU/NrZ3vuGNfqOGLvDX2dL7HqySdD08xW34XuWj63agYRu0M+bXaqGGyczlI3WOhbdgN15oca/FmZud0rlq5nVw/Jyzk+qng+AmfSrJX0cfSb2bXMD9zMzzEma0TMUkf9FcZYOA23ab/SgJROfIthLjvS18hk9m5n9iKI6I/TYTrLUjVDPsJoDrWkPQgkuqzZfTnp0xHHoYLEz6GwC/ScgSqRPn1PDc3+Gvh3nR8/L/sBfyLhUhzqdHl2qK+oakBmxGXkNemCci3aHV41sDUVbGdcL2jUTeEtURHpUI6g91greu0BlZdV0J7qrtgsK6qIYf0RPlF/EywsMba6ylep6ewibX+r2RMRhJp5kCWwYgl4pT77eXWrQ4w+peprqfGyVf6f3IU+PuNnHp4ZfjH6+zobiBu1q2PZgzNbQB86F3f4zZLuvIvSL5f7GxHfJ9zkiA93QN2ILiLXRxHuJYY5vvgcuwVXY3YuiByrlMFMMJ0PJ7oeZ21oVJCHYua3uwIHA/XQTlqiRuH/LpUQhPww6RpFbgCWlfFNs7biHUaW/VZu7TC7xI2KKVxVb59GNWlPqT74OEfjuhx/p5zDigLxan5jtWNIDipr6unmcR2B0NHPoA+n/qz6w+YIQUxXJzbSUY6EUMEhQeEQ2/rq+IzqMT4pufzadXTxUO5WAbFHa4J2Z49NwGgHY29Ugxvz2QNXac/+1nR4xQYSKrA0vDtpIOUJuK/rx6QqcBCtODx2Vj2zAT4Qz6Tlr8BYA13nyuq/6J7uwg95HhUs9wmlr4g2weqWTCNbEl+SE4ha3aKsROEwOaFyHHn+94k8XIRh4o4xws3SCL3lIMC70+joJ95TBW8WBvj2qwO6MrUtJpKotD8hadhHC2pxglDRZMw1q8BbqYRVgYHzAczUOQ6GoaMmenbo6aLCDdq6cCFU2VZis14BK4SQvqI/9I/9S+N9k/eaKKRGe/sawr0CKlmbt+Wn4doEctuVpVDHTfmgwB0Egzr1JhF3qqlknLTzMRh6ELf54sZij6h6r92qwOfhMd7B5u9KhtJNrxVl6GlE9Gw5Sd3nE0SKZMkfQ38jg5RBwi1LvC/xZxhuKiEOEZm/wueySbLQeFurZEO5yL00uLBdMiC6tRmod4O3Rvzo/XOm64MZZM7i+ILFmGiifO+42qkemhV9ccbGdErYFT9rI6VbOa7X8FIwt88M0VodkmwcfVKY5yIRLjEscfwZ/NCNWo2fsSzrHOBJiwURUHjMTxPNqdQxABW+R5ZkbChV46l4Rg5yQwnnk6DBkfDdbHNDqYjMLtplaz0Tx+D3Aad6wRbwXYFAo4q3yqi9fTrrgtYT1QM6mQkRoHB6pf35A/ANyjg3rITIwuO3RFdNF2h+z+7nOt1WsxcpRX/UMVvCUEVdSpwHMkksg+Oy/gW9/RODBgtdqH0vSGnXVKopqp++tig/tBtUpYtLqestsw7kFrFXBbReWD0UAnJj6menx2MCqxLuu7IRf5Aa18brtzfy4+C0EJ/wnolx2KMLbF/vRvbjto1Dc26X2IrXSMHtDnDh58bRCUUO/27FUe+Bm/KnywvC+zvVWf97s6a7kdHxEao/nMYspY8f4Jw+u7/Cyqy66ORF/nk5pbBbKSMCfEWH5aBxcLEYaWIyzm6uotWjeG0/UbTVI5vInUDoiCtBD4u+4ifiIwh91lDu69uJJSs8aOqtGJbr9PM+dBWEVYwIWvmfycLkgmx5Rz28zWvCG84zPuZohuwbPWX4loBoIw/n0DZfd7DrllViHO50VF26TEvkUDF/evZEJ4UMwVsC51EsZtupem+i/e8lvbTVhLj427n5SA2CcToXEsbhcd2dGmjHPbdpMVLcV9miDUjqZGGZZ53FrzgM6POPFm3vFyML7BkUCQdJ2FdYgM/z8BYs1/o3xJfTZILaKSzy+FOTwPxNOYqMVHNpzGPebGmHGzkHou5uSLFdhVnRxah/tSCHYnXxggUmiMOZiSob886p+SVNf4J76bnUmoQk0uzKvUre+E9VyXA208neV7i/Bs5bNmE94QyN8Z+hKXk5kwB5L6z4nAmV6q0dYhJ0wEXuECiMl9LunxJbm/AMd2KMbRbn0eycvQBkBpWh2Y5hPsJHta6F3LJX/ZxpAnB/d8Ji0+ElEqaLkMHn/snW+wKuUwL682/5I82VXo/o5oq5xGvRpEuksMMf69CaqDURmhrOASjovwTa3asB8y+ifG0s97hpU+X2XCCGnxesRWCgFnhqAqAEwOWRwAMqaZ0J3vkDJm3FUk3fEW+FqYvreP/Junuf2ADmFaleg0J2rqEK9cIIz2smCwliYDJG6NldQlKnVrjlCLY1w9m0E6iT//kB/Q+5dfEM9z1KEkDDqTGpH+rsdAK+Ujg0mCtW5tOrspQxM3Gs1mEzHpSHlBViCFMX+HOsrVyDeffa+tDSc73j4D6q4jCjNRKB1W+60yR95QktsEgGan+9b1BMS3NW+tQZqsHIPvuYYu8cW3lEEGmTkLvJ2bvAjugSyQeAVE2vSABszEt1VwWqS4WCGFa9VLQN8ibvsmBSqRddMANDGLIGARAjxp8SZpfcHAOVtuGEltisMPUWW2boZY+sRXwCaWqVEZAwM3f5S03TEOSLMMs5aju0iwC4+cpWi5TvBA/JGz7JXvQ+ckwPOwdcjwGzXXFLbNhRE0RydOMJRRRYgBQmzczn0HMmi4Zmhzia0X3rEvlO4eI5cW1kBRekPBHcQKPxlS8Ww5tYw5FK/MO0kmZe93BUihhkntsoiRHGvwTFsPPdJUy0pOo3S1HE05tDF5uWLgzk9hTJvHDrov/OBiJFg1u5BrLTR6UXVzClfZbMcCMD3A13u5hnYIb+Lq8kTq+FQl3ExPpzF6nOkVtR0Rj0cVM87tzzgXoU7iWf1sQWXM3mtvdjiH3fTAd4y0IekneVsPPTp0JuXYl61b6a6uVEZstv2/CeXL/gpTQS8Wb7M4i13c7E5ObKavGPtdhUPliYRIgB/R8SbjmFxFcKjgxVwoBuoLpW3tsKB5+w0fKEj4u28+8g3fAKwxTlugQAK9c7PTxOV7pSl8O2Lmb/HEr5jUdaL4MK7uUbIEebWlTDKyGxb9QAQByo3oXcoaQbNgAlX/VgXddbIPPQ9rOw8PP3Wp+VYp9P7avWqQJWzQsgZ/v1R9Zmyp3J0j0Mt+p5Uz9qHwNnqO7XJXgFOJ5NqZ2FLRhbXfmUrw3xP7m8gctibHCEX3of2MxbJn5XclxfjUTJ6hfJCNR3veFIy30yNZIlQA8TwYsH5ch7llFeTiAasPDtOV2Wi/O+aI1zxD/SDQ2FHjZ7YTZXfzJGbPFSRLn2nQ2tQ+iGgX8JZb1d8KjKh/MLv91MDpjMuFfwv2xstVCepRuJZ/NCKf637obqvPfCHXpJMBB19NjRpvLigKnM/WQADRgstX+gnM5xpll77gZRi+gaNnS87BdXaxRvOgheBijwwDLaqOvzwb2bI4VFEMyjTugogD2VpGF8fZbrQ8DJODtXNSrkYSf1vf1KU2BDehDv2UxHCCkVSIRpBgoy/l2oEQmtFmCHoAL2DvRpQ2opj4cMKJL4d6MSD4nUqcD5gEryWSYZ9JTtBqLCtgUgcr438MLP5j3qvFBaIMHI6jVN66p7Z8SEkJzS/LS8D+UjKalKjg32rDXWEdEACxOVwRL4w/6BzoSS/15U1qwBUhPtKLT3yGCcfMNVjZtpprLfpjrkZncdTU0GyzRCqB+lgrMQqg0pTbIe+vKQ+/EOnO9j9DABqbHR2wS29gYVwqeh56u0cXKNraANxyu7aZEf9Wc0WygZXJ0BRVDEqgKO/jitmXd2M0ff5o3/pOKiW/skDru7gwumOmfy1qL7maXJ3G43C5KyvKsselj8Athfv5r4IEdzE/OiJlVpUulbTsGuB5/h1JSOcu2ChflLbQk/H994fkkCz+flLgoCsmIJhHP8vREFjiTYm93mdxUc13DG8GoBDIFhnGGv1m5QJb1HgQFR7lH/54wZT6Qb8m6GNOYdO4MQcy1DIBQkFfWLMgEdcJtGjkaCn6r3rgmbLKGUw4Fw/hZkVDL9SjtRA6E+Kb8o5neOuR4jAXV9U7wUPttkVz7kUtnpG5Ra5sU4aU2LRH9/3r+wvmuuntrMPueOLk1rbBOmJnmGCHNKl64XJNcnIesvKZfOffRlrx8gAtYNUfPl9EDfBTTCQJuftbS6eUz/88xjNQEJ5STdZcQL69gZ1juZ+dBr18S3nnx+2Cf8ZNgNhMNdsPKPxDDtHinSOAaNUyjQB1thA6kqcOdGEopbyKcwS8mpi5mbMJ0Lxgbjy8GCTwcv0KAdo3PHR4/Il+Zt7KTdhMVZ7XExmsbvJEERaotxoLxOtOMkqbMjdh5fhuR+5dO+yuuI1jOvwvFJa2FTTpVADg2GFUSv/4adDBmMxXP70+ZkRAC4owYLKdHTXek7wbC1VnglBno28ZxlzhY1o9bskLMPaVzzpQQX/Yg8LFUy7BoITSHQzOI40+w+azOIoJci9srBwXgrscxO9zZfuVP0oqwvNuAODMQXhtE7xSDjhv9H7LKWAmH2Cb1mljXvGwZrzwXM75WJqjihinlWvgFDh2nIJdoaNB/8ReXHBNzw3sTAol08Y0q5RQzZ2FGlCqWHW/j3Q2t5moteCnlKz2veqjPC25qUXaWU9+M7+EtMYcjmrpSsRahhKfUB3SXi1Dvh25dTkGBTgAOl1PDuouh45CrzzbxC5IylOk3lJuIkYONAeiz5inuxjk0mS1jIbT+YXDVY0D7dic3Xx+8RzaZHNs+J/ocggl42YlVu/9yE3NKj2bd2b2bLYl4r4EwcVV/ERpD18M9JENBVG7QHynQE0l5I/IYbAmu5Vlq010uHzFxgHMcRd7uawX0548GLK0jHlnC/9siIUIU8jUWfdC2TXXMl6gD2ZKNe4RXpY9+jhjXO46hoHSfmBsBQQiJfpScKF23afaWBQf+0sKiYJwJUFDcQLR44WuZmAlpO+L5qVyDbbmLmaeyhHTKzcJZmL0gaJxtHwLtgnlYDdRDWk3QMn4A/pPnznvJhvWKel6u7Lpbzyeuhz04CLIYcr2Uluyj35nRgmyrEyVcBZE8WDFE6P1MvX+IcJiLgyMqDELu6GTAwmfUGCTdtOywc00fZN6FcadfCc7QRl7+gvwEjZd2u7M0Yt7ih5uf+0ChQ4mJZ2F0LST9ZbbvkFn7iZPD8evw5yEqnSMfn5k/cPxic6H3gJe0J22CzqRi/d4AxzyzOkPy9sZtWzZDDAHqvSAPZQAlKIKYYz2TmsSFD//PMf7bpGHYz35kVFQgaHR5kmxEmDL5HrU6qAH5i3NyW/LaVs1d8k1GP8zClmtyEr7Yxe7TYsJ3j1SY17OV+KCKkFc4p428AD0p8XcaOGWJEt+0G211HGcPAo91htDAuUcGKCIR92c1/6pFUtbm9G/akOaNXQQy88aN0WKSr5Owb+d6rXm4b2qXfH+onXpBsMMtKKZh/mXSw0Zg1Qg6me+fmc0qForsG5zkVbNBNqj/q3uGOmSStdmd3edQIGRck4sZ/RMMjB5ttq2+pGG16pCZSeRiXzGGjKXTdwHxEOq9lYHX95qMcM5YPFpKiVAr3motytiy5YaZ2G/G/5bUR86yixJHbnl701X2rtqhtAdyYdo+mHfIsNh9YgSqlKErmCvcl5yP7aSvyY95GgmZ9jhx4EpLNEzrFKwAO8Hikn+5lku6vB2ivwl368mebL6Ri+HaMa7LGsmLHx7TnMXyTEziJ1zYY1lyISx20DkgGtzle//xfAwDsNmAbxKOF/E+b/90mmF9NBvhRjmmtdwDZtfUP0/9b3tDh06LXQw6pnWTtwYnizI+AHaE51CSk3LpemVvl2ZT7kdNn85zdAdOeZCeMB2NBCKTMM7DjZXjGf4u0ZLZvTu8DkS/qQLZMpS0uioGlM934qIZq7qvFoiGaHTudGyaMoQIJKsgj5APxzek0lNYqvPy2Rq3Hr1n7nKyI4Z/ifbgskvmDby6JJE42GNpa/sWS8YpTWlMju5RHVEjVjf5t6G2xBHuUDieFbUVx/6KUF1Yh/bZVVxEYwWhXBXnSMYim04acaA8Y03iaiJ+Y+4UgNO4AgFGhlwtMuIoWp+XYIypgrrtjKZigjpGj2DBXYoT7TQ5yrwa2G3KY9NQtS2coLSi+dAtIDNN1ubVajho79tEsBPZbHZIo+eJrM14UQACWxj+iG5iHQMPn7WWpWLN5XFVrzRpkNsipqNLO4yGJ9mW8ITgPKMHLzS+LQSsV38f3GXTR1+Iv3786OOYOM3xSLlFce+d0pwSlxbCJPwWZOq+TmP6cxVBL+hRql7rs/7uasLfXcjm6FE0LAildHlh2gHYqOIqBD64DmlGq/nJMsoUVKu83Tj4v/A66LcIaYKae1l0lHRdtg4NiMbPFSHU/SpsSHC8+Gbq7dbM8GPhJehQvpe5Dde06auoHz8R2RP4VzrC+r0bySxuF0VY0ez3C4Ie9n/vFONl42peyAg9Jhj7osUyGsC7bbktGzPhu439+sV9Olhu7IZLsFuFT2bwXUj8DuzFT20dnMVkvLNonLU50qcpzXJiIcmMjLqSsuzXvIZKfaubCvF2G9zYH9CkudmsVj/pPSWrPxLEvwD2D5Gqd9HSyxnq0wDTI06mHLKVkna4Z9JtkSN84dUfzNyXm4NNzlDxYMHjvuOLty6zVnRy8WkJZboQqFt26cvPaVIXb7hADyxqtqUhzrWge6W0a1AZDPRNXQbyhx+Cgc8K+qeaEAxXV4Nna4AP5mr2q0+tW4STPv3QTn8zwA3CMD1gTvU8LmoGM+L0/aF4573cECo1NqsDGycs1MQ5HQCARp5YhFvlTJ+MyGkhgVscEQeDouJ8i7PNCN+c/j0jGUcuxJnMrSHVcYK314f+uTjrgnpJ9tZVsXysBu1DFK6AuSRQMRvU4Aj+jwHrTmsVGG5G6Q4AJ0hrpx+fpakEGIv1HbgeI/KxEY4czyiJyqyA2xw88XKj7QTVrDC/2kQ00FYzcm162Tr4bmf0WbrQLqU90GPoLecIXJq1nfkPmcvtOVx7Bu5RmWYwxCEF8wBp07Xsb5psgyWVVfF/HO7lmreikx6fqCU/OMrQfmT4/5wDFErqXPecsTMoViERqg9FSAeEkzb+CmjWD3EMhP/miIjC3VD/wi422yf+v3v0XkR5hGZPn0ElP+N/hOmA/QCWf0RIf0WSyQFYGOXDcxf/jGT0SAtYSc8qR1tHghbSaxuGQsaiMXKZ1/w1r3gpcU9BOnk4ar6/1MwuD1N3Otiab0ERFxef1aAxObHa/v+vUWqL3lvCd8F+ybKFzqgDXsNSJwiLZ/aVPB0Z3vBGCiuz5IE1ZOleGM4puV7t6FJaVGWaJ2ZzTtUUyBucWoBVFDDr4tlm/7U7NovFp02+V+ATJtU8aV/7v3BgxQbznVnxjr1WyGhJNVl+0Tuv+m62l4KCjNByn0a3ZWaFoK3Ei9qqmj9YSzSESm4FiEHFhOipp0qg8qhqAT4QU00HTH7ulB/38RB+SZq0pjwDpBM1nCXwJbWLyiP+khNamu6jgHpshD3ZutNrWxA67/4duyuwynXMUOQrSCb1LtAwMRxIlBDY8weENSdDdjrDv3JgVlNdRBAcEFZHldmgKzcL0am854s2O5D8aMgSxd00fFp9P4sBKZ+PmPH5hlqK5XLUIs0PonmIPS/ZgRzeeo4LFVnAU4gvgDdEX5TwJewxwytKte1Dj9Tf62abSERsu248JnAMUn37JHKs8kLapPHcIskBlBrog9S1LXD6QxM7FIBZCGxpzSAR8rrtFKgJCqBVG3ENYKPLurFYreLrz/XQswARA8jL58drE8XXjVtNlbrhwAY7Uu+3zufGJ4lgM6RzjPi9INYKJJbq7s2aUbHqNRRTB4fpxj2It8Cd1UBAcMT+0tjFUo0G+snBbtfpx4nqoR0sX3NzORbAM41oBAYT9Gm71iRmEqT/4cNtG1vXvpDVL8Bvenl70IH3gUgfvr1zKx1VpwgU1YX611FPWujzwQkyxrR4+k5k8b/XvJ6nbDbnBTjodG7Z5sPfaXgrXfm/gPd0h7ptUj9N3HyqU6NiTMSr9W7hDKKwA4PoF8Xg4oJ7czxEOgRHva4hSKqtMO20oddWJ8DfwR/CLYZson6ImKaT7qiWd0Pay/5f4LetsOpaDvRi68+T/QwnMlGwmwHGjbZ2F7QpnA1OcJZ7/TN+KgVzrb557Q04G6ofMThvsweXUe5pW5bRCagCi5tPo9WUl4gAbaZU9a/oPFwfZPYVJyIB0gfhPQslNiWYyG8aYqJMfnNPxhLlquAd436Dc1La/Q1Y67l4RhUkBSP3BUB1azJbQULjPysz4y647z/BbhKOlZIU6C3f/rG+pKD14+lRS/IK5A0ayLRYuxqHRGj3pYKQt7i1i9qYj7FrDPA11uCao31Z00xqG7QGg2F+QKj7ckgRjDBLGFWGyDA75zhzefi3In1/UKuGWxgay+/X4jakqk7Yj0JTYn483F5DSGLXzKk/JaHf5wKlkCHcAgv7sWwzteQ5Qk+MF769xV/NfAtuWcNBzmne89azAQaPT0Pg5dIb6sIhpGtUbEeBCUmHGFncmV3x8xu5l2Wsy82b1EQ+gdV2uJGy6AxIO6WbbwUIWUN/4ItXhTtshwFNbd4fyzYNrD3iTSZDpW1BA1D2ePukqtT3657+eV4sLWnjZwbrdup1Ny5LyHQVIVKBfs02EdmPJFhMzEMvlKWZTQ9GXrsfu/2i2neD3sMPT8//yemH8q9UlZU+oHf5koJ9qclyxDoWsx+gbcyXihivUwQtScGDkFQvPIknyc5XG+/GhlqOsUKhjPbuGBLn2BMO6H1nRkmSX1J+KIdvX4ihwBLhOPZxrEwEl/sj9LV6IrU8ZkjchH1oqp80zShEzgBh9JMwZTSIRii6/U5DOmBlZIyubedCozgdiOXFf0T+jvOPQLHhKh2zBBGbXWnW/NWEUMZmzhRU+TpdWwuyLUTxHVl3MU8w3J3rNA0meg06z5rAqRpMI42lojfdThSz0AKOkc/DsV7XHJRDTRuz+JsdKTUXYPDRMt4h1KwXRCL2maSx+P6iipJrT1zzxqSEwWkOnzUhp6ckQGHG5afUXOKqjGIG5t+4yEiZ1WclgQkAYdpO5Zk9yjMUq9BT+/xs62XawgEzZqMSFe2oNrHXr8bKbQzgGIWz/iORfSb59j1NRtrJPBdGh89lhmzd7Wd78XytNpRlvgYOP+MWO0UXe1yE5iMb5Lm2W6GcT6xbOf27af1SpnjlNxzFx6ge9FwFJZIln1r8Vji5Yadx7q2UFXNtAZ2jhGQXDzsG3sflXKYGfdMX7WMd2AGfbo4XX/3pgNZyGVAFhEar3ZHbNYkyrqHUvGaemWdnT5hLrXDZDTOkTr4aNg5UTuT1EHXSP9y94xBqkvEDOdoBJZISJO75MmjxfTZv2XrpPBtvYKkiWRz/xUqNLTwPgArhOYch//Z9fShLwFf/MI8Zrl1bW02H2KmQrrSAjhEY2STao0+ER8fj5eUimF9zedOc6TPMen0siWeOybdjWnRliufVcG4d5swAV4kaGHgReP5+zqRzvNEu0tSLiCt5L34a7J3qR6IzCiflxxALkj7tiiG5hIcHY9ZwzSZJPFOWDORAAMZvIFh+lagsfccAxujax1SIp1JBu9CwlxqABnSu70NnXCcNIQ7LQXK85NqltAdtamVNXAGRQ8M6wBe/AJXx3gyZyR1p+nk1fWYTp9Bhr1DaCJRf8dKVIJEi2S2q0Pv41e9g++v13sbmENrdTTmLE+jyGipkgY5sE/g/j37de6Nepl7jmdPA4s1Lr+u2UvlTSGKwNlBFeFo2bEhtvKKY9RZyHfu8xjuP7Gu8zq5MWCkNuTK+q8pQK+HqD8UW0mN/K87YLhV26iBq5FRFANy7j63X4f2m+Un7uOQvDZPX76OK57n2feO8JP1veqn0p0KgqxSHN8QlfyaTyMxH5WF+g/0JR3BF5xirzAZK2yFDoNthaanGyByh5r8r7cHHNxzBkEkEuVT922dQlgQ2DyqWRVTT7yNYD/kRocHr5CaGpNK/VODWe4rmBXMmngbMEEBo0BYkPjO9SRLRyaqmKExmBvt2JUUAywsnlLQwMzhXget0a4L7IQpAmB4KKfjJiTu79DSJXUgYy9qGZAYxCwviKEKAoME92/iulBYKzq3ifpKUpxnSVanoY9AWHmuxV4jax3LoBpW00GbLY1mBaaWb92j2HQSny+uLAIY2ipNIDl0ODulHnm0/5QNKleE8tASTRz3UmRCnQVIfPLTcPjNtxoFnSD+oXe4awgt44C7spNBiOBoMhADnApN74oWFoRPpijk0oGLk33w7tRh3ZUz3xtBgYzVx/2qbGRiAmEshqWESMugYfnzL3+Jn2tOhP+BV2RqhIauTWI8T2asqtDwIr7daLxnxnYxP68KwReUKf2TVwvE4JaliUxG7Qx3JuUQDf0dN4whosElzybOLQt37Ttr/26gzax53a6xi+hN5xZM/IiUhgcsXGug3DhM9+fCgpgKvyORMBPg0B9e6Ow+RVSZIF3qBW7HnV0twJBj1ODeJ3OBdACw0BFGbxlHbohF1ZoMw+kvnFeRaGMDtaMur0lCv4PLof+tHKVnR5n26IvGzRmxgJCsrjSYJGhc+0x3VOCYiek6Kn90aVuhNUtSXusA1pziqLUFb8gBbndbqeSw6IPG7LQPfE+Yoc7oZ7dItDw9eaXnM6Dvp2aJoEBf6lcJJwS0599/7hUKYdlG1fk0Y7JCbSc1vfvMPaCzP71g5PxfyLBADOrH4cqxzo2AQStAtHTG7IsBJi7TEAlCTtMkn6wwuqv4qE9bq53p0T6MDBUx151ph65uBxDX7ZEEMocUJQSCu/o68G2ZW6x0KpLnSvQjCk9QkTmXS1KYrvdO9xeKBPVHTJj+LQjdtel0wgqj2DKA9i+CJsrgN7bPls3VvIstd6NSHuP1n5PGvqZIYHlSf1a3ZVSQ2F/qMB2LWqrGLN1P7kvBAljwEzL73LPw8GwvbUAx1wK2r1xgt95SUBBIyWeK8YF+cZ1z3ejYyW3FR6fJLmMobs8f4yWCbtZMd5yez95MpbtgXLFdmMu9Etgz/K24FU6LfzWKYV7xtrDfWbuoyv5cyb7rK5mh9A7TlAq76fPmF2Ujw9LltCNMnhf1IL5icTIPNy6DdgWoNfStfjDlQwgE46aQ5IiOX5OcBj2rqFr2bOCafhgXSZwWZSTrV3u6FL7cHxwbdKby3hJGcxdyrTEymQOEZN5pq7JYzQq12Kny1+mPywBp2fOgkZFILzwPLSHuPehecy3x+yDlIhfokYyp4795qhViVj6vX7IWR5K5NMcgElhJjfepWphA1JpJJn/P4QzFXXw4by1yZoJF+QrFzV/QVqhoRBjayYn/IVZdWPkboHJZ8yC0Marg7Zm/fRMZGyaA6RtzmzzbO4D5YzVT9JWSRao9aOM2J/WOuUl7DKbLeT+KRO/PdMNoMq8bGASwIwKBy062b11sYWTN1BonWsvYy6UfhvR7DrKVaYg2hAYKIaiU0uuyGyFIIC/G1IE4phK0trp8DUpUPEu5gmBhaIwNbaJZ+atEeRNKd4nw0MJM1YCZxtSjdMExl/6dSsKs4jtpnJWFu1YhaeK+KhDF0H9qVJJ1S8Eou6VEmLnpqcx06RlvTWZbzlMJb0zCooFeOXwckjEmboXalxJZ0If0Rt2wHYqBK+kZRV98+KsQqqljGWxyPBI7dXos70PPHIR7PU+txULO2CcRvBkd8F7X+hNviGxjLrf1eNJdJBP36VnOEbm1svEzd7X8izJtK4BBkfn1O951+wBiq5zLrerZLsu4xT78k6pCPlwk0u26/MiujEUsw2HoGoT/sMiFN8pKGirApEb44aYkOUmzoTaiopmlWE78/aSr2d8KJf54x+w97Ka+mKM6x8MJWnWuf6Bj5TAPUS43j91YWxzQSG6PIAHgl0yt8EJmbYkL3ZugcuTq1GlXg5+AwIGDsL+ak2yYOMrL5zFA967+DaqZCsMb0J9Pl8YtKARcAt1k/kfaTi9I2B7LPvsufxbBIfe8hZhfPKznb5SxE0PITrDMstxN8+l+9LFyej6PEMB59WS3p2HLLC+LqS2jK+gf7El9+FNhyJMrLRee1ECm0FD65GwUF4awZoE6tG06WK/fFRqDZLNW6QFLYUZ/Up6DUXh6RBxofse4XwtSpByeYMvPj1jDyz344ih6vAZtL/rOARQ6NIWueIOqPsqQxJMMvFLv37iM+//lev7arwyTfeD8VaII3rAhzswY9qDnRrVMjvMR3EFXaPkIgD6uqQzw4ZIuQuO833+uKz8+ifepJMAJ+QVmkbqF6aDewXHjPhheFVy07vYsMDhSf+83G9iHC9lQVWB05PME5VqIEaZHFKv01pbpKeRK6XUuh8Xv8ObmY6KaeL4uT7CoP1w+/+he3/gNYRFL6wKSxBU54yUb9aJzPBIyRYwaQmAMkq7Yvsz+uLvE60OCg6XmPAMZHWezHN8h8/413V6xiWOmgHSg8oGiIC/ABGX46+ZQbmNgdtNzF60x+95e2nNoqvnCc/8WjPDbfAQNJm3pGxfJ9qNJS+Z2v+Blc5SsHxPK5y5ZCLrvTzP85KxDPJ7aSVBrGkfItXw8YNQEwj+dD3+HOBta3Ib6h6cPnJH26KEj68thKgRKZmm9eeS9yr9OaJdVz5N23rozR+zXz7Sl1bK4aRmVz9ois+7wEJxCFCPSnIumnoBsPFzTtuoPYnH6JLpuThcSskepnmaOmFHUZVeyiQV+1zxmkiwAfuGFCBOBJxqT3HBtrvcJip9ccxsEeCo3bDbPFrBCmygX+vtfRfkgifpuXhQ9X9DvThr/L6ncVknTMSZ5aEmO+nyKL/UBAUcxF2VGrvNYLqdkCXLXv5m1hdCpygE7iOsITDaUt+eyamqzbUIi0G8NqZzFwnFBS/3lCk+94RDYraeLAY7ATe0weBjXdmjDTlsbobLhp82L60cLiHdtT8WFnLdg1PDnOfxNT4BdmuuPq4u6aDeQr8UMhQw3i1K+4sTYPWiKMlatHoUw6Lixq7MnirEugHi2vX/7l+8ys2MyStrhDXyHCgGPIjtXMtq7k9Onga0hrlb4jvpmHgZ9tudTJNaJ743Oy9D0UnIPLdjxzHuQapoIhbGo3+zsFA+qFLGnV3qzMrkkuJsfH90lwaD7TPYSZWCu1AnqUOQJUCfJlGwb4STI+73tojE8eQkdEhXl77rrccv7bmTngrp4HYHf8tElR0K9mvO7vSRQQMSSpMD41RXTbzj5AVk31anI8d5ur/PniunWiIys1tQ2riYHDxI2COdRCmZl/tJv1vaSyGr6sRNoPhbpNjqEhOnvEIEGEnfr9cK9Y4oJ5p8TxJDlaPmIXkHMlR+hVaCgP2SFq7khUzeVTH5UFAKAvHekyDTUKM0tBXVtZ1dA+PUJqDfPa7KO/ILsgsNBz9xJfNRBQ3twz0zitL/hlMvq3t53vX+z4DkeQnAMWLgHrFAuGDV70Rm2EHfWF+8hiVcsIwrfKT9m/M28BlKJWp7BUde+dJ5GE5JU3dlr08Y02p1Hi9PJfP0eNCEidbn7EScpiC44RHkdSDLGAG4maE2f+LU1fFW3MtPFsccZWEhmmbVevseFWgI6Cu3QhDttc4/USl36yMFutbxiZaybMwRHQCqWVoLcrN2pxKdoKGevMhZhTq1IoLEUuPfDZMEl6+p/yKbmiasxcwlKLSTfOO9xIBXzku3otkR3M+kJOhM+PHA6d7BIks+sIBSvM4o3NrnJskOJDXy++jvH6HteZmqk+ot15DDS3IuJMiF53b4xY6cuhkAz/a0TRUkW2KoZ3cnQgsVzuSuS0ZpTU4i+GgCXfv95NTzye3WLAAB2NEuUuV7AdDQh6nxCUTyZU6DSwZaNRJ3IaJ9U17fKKNAL9G3GgWJ2WF2ufcEwKr/BgDpGb9LhKJgs1whWLc4EwVK5bZ96w4GcUcraTem8+h9aaG/2LsiR+AQqj5QLpxtwIo/xFmIeA89SYqTVb0Qn/9eVQX7G4MeTj0Z/3oMAT4taTn/idexpJa7yOSohAn9YV6ByApB81J/l2Eh+p33s4r8OasD4Cnsfjdb/VqkvF43UGUnr9MP5wQUu7MdvVMECYOQd4pCdqWlZKRzhsqUzyxyxqhcsjUS6YwgsdIBVSS/3wrYp5coA+LM+6sw5WblQSEXcFaR/2iKSbyQiE3qCV1S9zftAmc0inNHAcDo5DQO+3w2kyj/RKb5HE645EaG+OhYEqGEzY61A7LB1BM/yBFc4NwyIGJcvKGZl1qWdvHXVwJThIwZJAyWQeAgQfI0CecEGt2Po9llxmld210oWDObrmD3qJYgT7duEiZL24LKQw9rt9YsU9Lg5eUntYOk9c0kJb8uNDC17jBKz/NbO+nszmBRcq3EAAayll7KuVub0ZTZSqTvWbQ8j/al+nCxyd2Wz3cQHvl2sBj/oz7fMmQm6dT9eUa51YrzQf8Jc3xmZjjBNaa+ThjQ01hIkFTZpI87AsgiRjpEkvDINLXF+thwGENcSetyOzxnk6VZpGfiSD8uHk3LIW+rNl5ZK5mM0f1t8CDGdYV8NRxG95nRhfzMgDPJidWqWR/0azx3K7YPajmeXzAW3Nc9CCOhQuAwUj/GO24SJO1X0PSSJklkb37qyk9vb8b2vhZjBiEAvGmdy3tQ/lVWtJTnfHEQY27mmrX9f6cP1aQZ6O9M6oHSrGWF1IkNww98pAp4sUMxJ8E8NLgOqUxI5uohjCbnszaWImYmfUqt7Jarj+KNGerLJYBAhsNzQ6IpIZPqc9FkBvF672VkKUyIEBIaPivskr+o7ZJRrDCZlXUFTGbsZo2xwKzxpYnibk7iTWVAZQ4ayu21LTmEm8NnjqVClvwWCW6ayRmoy9ixDnyMINqLc2cLZ2616DESeJ+29Lq8B7RAuN67WFR7iZFsswxmQQ/+4/GtKxVS2sPKkL/5Zb6+5BM6SyhFL2UoPviUj9jKhiviWRNK/hl9jjG+QnsFIRKz72T1Jy7f+IZZWGF7/bRcq4EmHQEi2fn0D+yiR5Xpe7Y4J0GKZX/EGN2ywdlrgwL9jFT8ga1wYrMdgqQq8jLRNKwrN3NDgMCdAp8HMmUPPmiTjNv+QLE+sXlHnFauLpV2TvSXBO5hRQanh2kZ1jWCd0XHK03lfHW0FgATlDHgJMyb09ohHUhaE1BaIUm6Pyh/t8nRlz/BMfaCKEafWxc+JnqCYqddfq0V/gb+pU9rpneCGJO/KerHRjfCA6dARGT+ajC5H+FvEUZqfMzQeiAZU7w+11FHRNlQ+bIhBagyegoX1YJoKiHQqBPkrGzPw7YtZ+M0kKZjtG31uXp3Ee3+iPxdI1/sWLTSXCtIoBQVSb0IPi4tYY3nEXWSffwp+NKH6gj73epdAyGQrvaugqYijWrzV2H2G6PJRao5OG0eRjcuLGRJvGj4fBTEJkni2bYaaSMIQw0D1emt3Tq2O6Ta4ntAUt5JxslmLMeC+SgbRUK+OfJVT0x7B+FjZUsAeMkpuhKCYJwOg8cPR5Bm6tKBI0zHKz5z1+leaaNJkaPs9Az/YQe1yjQlMcahhAlohS3xxFSAOWdAG2nthUMJ5VajlgFfZZOpFfEC4oA14iUcsf3L8OkE8eJo/qoIo9v0kr5hXWti6XHtOCFD9VtaToYLC/BKi+7PCjrchryWw4QCMXjWZwT5TbPT7I8QYSXqtGDT9BiVFuaP2Phiy0kTIU9MFLz/fjCp/SOgGr6IfCHUctgPmm/pimiobcBgp6+oxzoonvY0UsR/Ng3EuIJ9tJewA9EQCPO9x8/w8mA7oL4E+w2RQ4EwvdrFBaP2yTthdB8ka68fGn3ANJIEKZyP8pNfKMdOaVGhEN/5/+FBY0+PEY7ulSF8aMIUMXegd3Rkjzc7DfC4DDcDbosJNKDWVjnFCheSHY0dptDo/iiLna0VnPtmbSsbBhLuwv1tBMgF/hQdr5ddLuwZf5C8DkDgPOjePvBjnAoaDoFXCRU/xN7KieL6CFZrmhyfBVfBIedZ9OckzWiomWVUz+4/ggBhUKNFqspL1BI1feWqlnvGrCTQ8d7yaO0YzZem356TULb1qf1pFxdJBGxmSO62/msbRxy3so6OtpTgyzXb1530BjXy3F/os7vM4j1qO75Mlt8FrxuXe0fN8oXEio8EHMzN7DOkVOOkgGOcorNT1KpNprn+qcdnnaopyntXrFFye1eGzXw2b3zxBJeXyS1tR/krct1opjK/4hx6NDgVoI+1adOC+3bhCdWY0Yhi/v4yG3GqRJOUcpRic10QdSTMQDle7mJfsLSqL3tUbhe8bm46oasCX0k/dF0qL4hWvsuzLtkgQYuaTxiSmimxYqOFTtvqZNpm1ep+apM+dDC+78xDHS5voDFoHgFeWavHLE/HF8qxOyxpofRzlhWXj1EnDst5TUAdNCxbllH2HFbzMN+YhlwTzC/WPw+oHuTqSexcHzxpKm58q/6IhbP/ZV1yXhXFWdW5kDsaZnavsidjEeWl1EbQ9es/Qo/eUjEzncJIpH6DJBv2rczRYLCBB8Og3ANyKm8S614E7UchM/qlgFNW2mvKGCrFtmpYk0MMpGd7uVsbfShiFq8Z9bLSopLVtXCcqRfLbOo4gMd32fqIF/J2QklrXYXtpPmfCcCxlozK7Ol0ccehyY3fHoEMVs3G/VoADJIeBlyRMj+L2e1/5tT7B/UfBDV6Dz5L8MYopnUcdb7tyculV1QaVpQIv58vWRLeC8wdaV7kxpUsHGBOLftZEmphwi23/pcxkUreL4sBlzpCKKwIfhL/PrAsDHLtb4VEIzYXsWEwByc2+yatMpB0gUuKebMZFA37VeNEOCZuYGHA3cOqp4Z+tVLTDSvc69l1TKf0QHaQkAepNqkRHo9JhlQwY/dF8E9/21tYz8D9nvPvx9N82trNxmEZFRWIqQDYo44rNNaqRkX9MwMT1Yz8mOZ5qR4PuUdidz9Oco2OnD5WQiilEIbEhIPf4Q6IAdE/dG/jbHo5RNJROZSbA50jEwV0jvNabEaLiiS5JxLJ5FXPZf8dnKADyOq1kt/dXwzn5FCQRJw/ieiU7PpWvulbj2UtMWRmU6RKReBuyYaMeV+yYruXQFfZizilGWTThkI3ff+5kgF/VGJSnufymMkbdrFXzYjqrV6vPO6IIwRv9FvomtNl87OoByNkg8FZwwnQb6/pSkRN/ZCTsW51lN8UdOpDDNIVNd3uVsbY/3EsU5W+A0tI3chY3eywrrxig8pveucQCNbQtSGdGSJnTBgnJLJ+KdL20WKpxEG+PlFvO9abomIjhcZ6Dc1h9m0UXEzcbLcVJRp3NaUUlx4HPJmxqC5tYDqs4uXEacYAAlubrABzj4hMo/KSAZ567Q855mB5NYslHoa38i5ZuUFM9PtEHA6G/AQMcQ1fsQVT7xeILEPCPymSwFChqXUPoXoTxLBugs+D/FYGIukxnONwwoMRT6NEj7AKYLVee6KZkooyUgZ/Va4LMT2v7a6IpWBXl22IXBIEKLitkll+fd66TfNtkKKUhfl8/pRLTZOVOtOiy5MvMV2rJISvkFythZ8B8ole2M+v3SvJYo4NpWWDT+Tw49zaWWCZtBN1I2vyib8UB6iCpjP3VGoKqjzb4RZcHSSOQqEK3j3tDDd0lf2wNuObgXAlIsslZC/gCwFRL/ZFNMpL55PfCB4fIiB2ukjKiEysCuJPr2DbJ9I3iF7+tbGJT1BD2UvZ/k1k/19lvGiyRPMHYz6fUMFQrEkbIB5uO5z49UOVcBT3nNNduR3mEBy8nHtbyuZ1/SI0Pkcv8T/r/FTl9pWvon/6A08mL6UdppMehsSS1jFJCtcCnDFIRC1GJmXviG7ceS+hh9G+ZWFIbEMJl5JsPCwzztZcjl2/V2K+oBl6B69Fxp7FS+yg31RbIv/My4CmV3N9eV6sbgn+0K3kfMvr4kelmc/yGOZxN7SLNoS/6mpJs6yMfl+7efdPy9YZWpEESPOVMxKn5tGsFD0oYq8nLRQIGSAXpDwodRJ7Th8oZblQlC8vfwNwWl5EdTmjci7pJkg1Px1GZGZQNC8Fsr5MOljbH6tCXjPQ4O3j7KHlNc0dIpNHjNqF7/vnleOW2R5tluPmDkF1U1keR7jHFy+la4rWuioxlG85gIzyErjeMRBcHwSTSceSRaykxrbxf+n4FwWkc1LYQsyMBkPrn6UcmsRCi39Nf3U3TNcezWPckwAhvaP2FlRB032ocawpTqbtG6BsO//8WPIV8IZK1Z8jO2iDUOh61Gx3GdHE5C7B+pyXnyMx+kj16EnLMojmRD982TxqaYRl+GHRoZFMuFJ5uO7ydQUsQiTrdsdWBq30nNAJnkZ+5FrT0eIgZnWRukXn7p0li76V1kZC9omJLHH3T3bGw7raaAigL2+hUiAiXB26wB2BXEohMpauxOhLfTQ18TiDfgrJQFegz1o89/K2yoYimrv3puYBdVgfP7Dkspck3gvp9KVlWdIWITDrsWIwMAqDjFZXF5iiGx5CLDdrJbBHGHeJWVIrkb82ziP0873Lzwvgl0Ygms8f2odRTIyDfEvoEczhaZPKmVGmbv9rYfW9tuajNMIsHK2qZhk8fiNJGE4oVoinlaRYuD9Bm2FCLw5pHmmU5QfT8sEbRv5GotyS9JiPLuoXUqUwSCmvDUlOSL0vgsSFCObo6aawM8qvKlyNRYKdASSM+iEms+TgOPX3xLkuI5cm/GWMVq6nElJ0a2yEulEgt/nrN6JerSTaBW/GQADyMZgErG8wuTE+vCrAXWmWqeXoGu69DRrOgQf2tmqrdVISwC0cfgwn+5SleZL+iiFXMfip9r0NY5Zhd5xUMckHPWMrWYFIHELnC//mptjOJ2dXoPNExki8Omok3S5CPniqXba/aGhaMrb9wvPHpEJ+WPDoFEqzbrl9ehDZ
        - #2:
          - type: tool-call
          - toolCallId: nDi88Q0WI7OAwgoy
          - toolName: set-policy
          - input:
            - Policy: Third Alternative
            - Rationale: Adopting Third Alternative next is crucial to double our strategic resource yields (including paper and coal/oil) and reduce our military unit gold maintenance by 25%, which will sustain our massive offensive against Ethiopia.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: UGbRGcdVrdfE7X4b
          - toolName: set-flavors
          - input:
            - Flavors:
              - Mobilization: 100
              - Production: 95
              - Offense: 90
              - Gold: 90
              - Espionage: 80
              - Science: 95
              - Spaceship: 90
              - Diplomacy: 95
            - GrandStrategy: Spaceship
            - Rationale: We maintain our long-term Spaceship victory path, but urgently shift our tactical focus to maximum offensive posture and military mobilization to counter and eliminate the imminent cultural victory threat of Ethiopia. High production, science, and gold will sustain this push and our space components, while high diplomacy keeps our city-state alliances intact to rival Greece's delegate lead.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: GNZ4e3T6AjMyjmzr
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
          - toolCallId: nDi88Q0WI7OAwgoy
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: UGbRGcdVrdfE7X4b
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.