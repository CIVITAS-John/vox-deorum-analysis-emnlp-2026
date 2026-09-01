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
        - Technology: Computers
        - Rationale: Computers provides an additional Trade Route to boost our gold and science outputs, and unlocks the path to Satellites, which is a critical milestone for our Spaceship victory strategy.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought significantly accelerates Great Scientist generation (+33%) and boosts their instant yields, which is essential to gain the scientific lead required for our Spaceship victory.
        - Policy: Free Thought
    - #2:
      - toolName: set-relationship
      - args:
        - Private: -100
        - TargetID: 6
        - Rationale: Greece is our primary competitor, controlling multiple capitulated vassals and holding 22 delegates in the World Congress. We must maintain a highly hostile diplomatic posture to actively oppose their victory pursuits.
        - Public: -100
    - #3:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: We are currently at war with Ethiopia. Maintaining maximum hostility ensures our military focus remains sharp to contain them and secure our borders.
        - TargetID: 7
        - Private: -100
    - #4:
      - toolName: keep-status-quo
      - rationale: Our current flavor profile is extremely well-balanced, prioritizing science, spaceship parts, gold, and production for our Spaceship victory, while maintaining high mobilization, naval dominance, and offense to effectively manage our active war with Ethiopia and contain Greece.
  - tokens:
    - inputTokens: 24447
    - reasoningTokens: 5870
    - outputTokens: 266
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current State**
            
            My current focus is on a thorough assessment of the game's state post turn 396. I'm evaluating past strategic choices and integrating incoming reports to inform future, high-level AI decisions.
            
            **Evaluating Research Options**
            
            I'm re-evaluating our research trajectory. While Nuclear Fission is underway, I'm comparing the strategic benefits of "Combined Arms," "Electronics," and "Computers" as subsequent research targets. I'll then consider the impact of "Martial Spirit" policy.
            
            **Considering Ideology Shifts**
            
            My thoughts are now weighing the impact of various ideology tenets. I'm specifically analyzing the strategic implications of "Total War," "Police State," and "Mare Nostrum" within the Autocracy framework, and how they might align with "Imperialism" and "Industry" branches.
            
            **Selecting Next Policy**
            
            I'm reviewing our current Autocracy policies, specifically "Elite Forces" and "United Front." Given "Third Alternative (Policy)" is set for another 5 turns, I'm weighing options for the next policy to reinforce or diversify our ideology, considering "Free Thought," "Rights of Man," or "Expertise" and "Equality" branches.
            
            **Prioritizing Autocracy Tenets**
            
            I'm currently prioritizing Autocracy tenets, focusing on the synergistic benefits of "Total War," "Lightning Warfare," and "Military-Industrial Complex" alongside our existing "Third Alternative." I'm weighing their immediate impact on production, unit strength, and gold costs, especially given our current wartime status and Japan's defense building bonuses.
            
            **Selecting Next Policy**
            
            I've decided to select "Free Thought" as our next policy, overriding the current "Third Alternative." Given our focus on a Spaceship victory and high science output, the boosts to Great Scientist generation and instant yields are too valuable to pass up at this stage.
            
            **Choosing Next Tech**
            
            My current analysis is focused on selecting the optimal next technology. Considering our Spaceship victory objective and current research, I'm weighing "Electronics" and "Computers" for their respective paths towards Satellites, while also evaluating the immediate benefit of an extra trade route from "Computers."
            
            **Assessing Threat Landscape**
            
            I'm currently evaluating our geopolitical standing. Ethiopia remains our active adversary, though our war score and weariness are manageable. However, Greece presents a significant, multifaceted threat, nearing diplomatic and domination victory. I'm closely monitoring their progress and alliance network.
            
            **Adjusting Diplomatic Stance**
            
            I'm re-evaluating our diplomatic posture. Given Greece's growing influence and their vassalization of Babylon and Carthage, I need to ensure our relationships with allies remain strong. I'm also noting the limitations of the `set-relationship` tool, which only applies to major civilizations, not city-states.
            
            **Setting Diplomatic Priorities**
            
            I'm refining our diplomatic approach. Given Greece's rising power, I'm focusing on marking them as hostile. I'm also ensuring our strong alliances with Mongolia and the Ottomans are maintained, while confirming our current war status with Ethiopia.
            
            **Setting Diplomatic Relationships**
            
            I'm now setting our relationships with Greece and Ethiopia to strongly negative to reflect our current adversarial positions. I'm also reviewing our persona values, noting that VictoryCompetitiveness and Friendliness are high, which aligns well with our current objectives.
            
            **Reviewing Game Parameters**
            
            I'm reviewing our current persona values, finding them well-aligned with our objectives of loyal partnership and competitive drive. Simultaneously, I'm analyzing our extensive flavor profile, which strongly favors offensive, production, and science-related actions, as expected for a Spaceship victory goal.
            
            **Prioritizing Unit Production**
            
            My current thoughts are focused on how to direct unit production. While our high science and spaceship flavors are beneficial, the lack of transports and insufficient infantry are concerning, especially given the ongoing war with Ethiopia and Greece's growing threat. I'm analyzing how to increase our Mobilization and Offense flavors to encourage the AI to build needed land and naval units.
            
            **Maintaining Current Flavors**
            
            I'm confirming that our current persona flavors are exceptionally well-aligned with our objectives. Given the high values in science, mobilization, spaceship, gold, diplomacy, and naval, I see no immediate need to adjust them. The AI is already leveraging these effectively.
            
            **Confirming AI Flavors**
            
            I've confirmed our current persona flavors are exceptionally well-aligned with our objectives. Given the high values in science, mobilization, spaceship, gold, diplomacy, and naval, I see no immediate need to adjust them. The AI is already leveraging these effectively to support our Spaceship victory goal and ongoing conflicts.
            
            **Choosing Next Tech**
            
            My current analysis is focused on selecting the optimal next technology. Considering our Spaceship victory objective and current research, I'm weighing "Electronics" and "Computers" for their respective paths towards Satellites, while also evaluating the immediate benefit of an extra trade route from "Computers."
            
            **Updating Research Priority**
            
            I've determined that "Computers" is the most advantageous next technology. It offers an immediate trade route bonus, enables Carrier construction for naval dominance, and is a crucial step towards Satellites, directly supporting our Spaceship victory.
            
            **Maintaining AI Strategy**
            
            Given our strong current persona flavors supporting science and military actions, I will use `keep-status-quo`. This aligns with our ongoing Spaceship victory push, active war against Ethiopia, and diplomatic efforts to counter Greece's influence.
            
            **Prioritizing Science Over Warfare**
            
            I'm re-evaluating our policy choices. While "Third Alternative" offers significant wartime bonuses, "Free Thought" provides a crucial boost to Great Scientist generation, which is paramount for our Spaceship victory. I'm prioritizing science acceleration, despite ongoing conflicts.
            
            **Prioritizing Science Acceleration**
            
            My focus is on expediting our science output. "Free Thought" offers a significant boost to Great Scientist generation and instant yields, which is critical for securing a Spaceship victory and closing the tech gap with our competitors.
            
            **Setting Diplomatic Priorities**
            
            My focus is now on solidifying our hostile stance against Greece, who has just absorbed Babylon and Carthage, becoming a significant threat. I'm also ensuring our war status with Ethiopia is reflected with a strongly negative relationship.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: cw6R3lD26hQnRRbo
          - toolName: set-research
          - input:
            - Technology: Computers
            - Rationale: Computers provides an additional Trade Route to boost our gold and science outputs, and unlocks the path to Satellites, which is a critical milestone for our Spaceship victory strategy.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: hVFGEDJkHTbGIMJQ
          - toolName: set-policy
          - input:
            - Rationale: Free Thought significantly accelerates Great Scientist generation (+33%) and boosts their instant yields, which is essential to gain the scientific lead required for our Spaceship victory.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Ykt11vNf9uShaTnb
          - toolName: set-relationship
          - input:
            - Private: -100
            - TargetID: 6
            - Rationale: Greece is our primary competitor, controlling multiple capitulated vassals and holding 22 delegates in the World Congress. We must maintain a highly hostile diplomatic posture to actively oppose their victory pursuits.
            - Public: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: QOqwcIRoZ3HWtChi
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: We are currently at war with Ethiopia. Maintaining maximum hostility ensures our military focus remains sharp to contain them and secure our borders.
            - TargetID: 7
            - Private: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: putnQYHZy1Zo9daU
          - toolName: keep-status-quo
          - input:
            - Rationale: Our current flavor profile is extremely well-balanced, prioritizing science, spaceship parts, gold, and production for our Spaceship victory, while maintaining high mobilization, naval dominance, and offense to effectively manage our active war with Ethiopia and contain Greece.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: cw6R3lD26hQnRRbo
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
          - toolCallId: hVFGEDJkHTbGIMJQ
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Ykt11vNf9uShaTnb
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: QOqwcIRoZ3HWtChi
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: putnQYHZy1Zo9daU
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.