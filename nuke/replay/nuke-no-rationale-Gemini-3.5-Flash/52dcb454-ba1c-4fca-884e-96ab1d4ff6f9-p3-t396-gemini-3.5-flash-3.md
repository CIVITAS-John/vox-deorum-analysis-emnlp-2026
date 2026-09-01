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
        - Rationale: Computers is on the direct path to Satellites and the late-game space race technologies, which are essential for our Spaceship (Science) victory. It also grants us an additional Trade Route to further boost our gold per turn and support our economy and diplomatic city-state purchases.
        - Technology: Computers
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought is extremely powerful for a Science/Spaceship victory. It reduces unhappiness, boosts instant yields from Great Scientists by 25%, and accelerates Great Scientist generation by 33%, allowing us to speed through the late-game tech tree.
        - Policy: Free Thought
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Spaceship: 95
          - Science: 95
          - Mobilization: 90
          - Production: 85
          - Offense: 75
          - Espionage: 80
          - Diplomacy: 95
          - Defense: 65
          - Gold: 90
      - rationale: We reinforce our Spaceship grand strategy. Keeping Science, Production, and Gold at peak priorities to fuel spaceship construction. Bumping Spaceship flavor to 95. We maintain Mobilization at 90 and Offense at 75 to encourage the tactical AI to produce the remaining 14 embarkable infantry units needed to reach our 23-unit threshold for our military campaign against Ethiopia. Diplomacy is kept at 95 to ensure the AI prioritizes securing city-state alliances like Antwerp and Riga, helping us counter Greece's massive delegate block in the upcoming World Congress vote.
  - tokens:
    - inputTokens: 24447
    - reasoningTokens: 4463
    - outputTokens: 307
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Current Status**
            
            I'm currently assessing our position in the Atomic Era, turn 396, as Oda Nobunaga. My focus is on evaluating our strategic priorities and the overall game state to plan our next moves effectively.
            
            **Analyzing Research Options**
            
            My current focus is on our technology path. While I'm researching Nuclear Fission, I'm also noting the availability of Combined Arms, Electronics, and Computers, and need to reconcile the gold figures to ensure optimal strategic choices.
            
            **Selecting Next Research**
            
            I've decided to prioritize Computers as our next research target, as it directly leads to Satellites, a crucial step for our Science victory. This choice also provides an economic boost through an additional trade route.
            
            **Prioritizing Policy Tenets**
            
            I'm re-evaluating our policy choices. While Third Alternative offers strategic resource and unit maintenance benefits, Free Thought's boost to Great Scientists is significantly more advantageous for our current Science victory push. I'm leaning towards switching to Free Thought.
            
            **Adopting Policy Tenets**
            
            I've confirmed "Free Thought" is the optimal policy for our science victory push, maximizing Great Scientist contributions and instant yields. Now, I'm reviewing our diplomatic landscape, noting alliances and rivalries, particularly with Greece and its vassals.
            
            **Assessing Diplomatic Landscape**
            
            I'm currently analyzing our diplomatic standings, noting that while relationships with most civs are solid, Ethiopia and Greece remain intensely hostile. I've determined no adjustments are necessary at this juncture, as the current extreme negativity aligns with my strategic intentions.
            
            **Considering Diplomatic Actions**
            
            I'm weighing whether to further antagonize Carthage, Greece's vassal, given our planned war. My focus remains on our primary objectives: countering Greece, prosecuting the war against Ethiopia, and advancing our spaceship victory. I'm also re-evaluating our diplomatic goals and flavor profiles to ensure alignment with our economic and military needs.
            
            **Reviewing Flavor Adjustments**
            
            I'm considering if our current flavors, heavily optimized for our spaceship victory and ongoing conflicts, need modification. I'll use `set-flavors` to confirm or refine them, aiming to maintain our strategic focus without compromising defense.
            
            **Adjusting Strategic Focus**
            
            My recent thoughts have shifted to ensuring we meet the embarkable infantry threshold. I'm considering how to leverage our existing high mobilization and production values, or if a minor flavor adjustment to prioritize military production is necessary. The core strategy remains steadfastly focused on Spaceship victory.
            
            **Verifying Persona Alignment**
            
            I'm verifying that our current persona settings align with our strategic goals. While the existing parameters are largely excellent, particularly regarding victory focus and managing rivals like Greece and Ethiopia, I'm confirming that our private and public relationship modifiers accurately reflect our hostile stance towards them, especially given our ongoing war.
            
            **Confirming Research Choice**
            
            I'm confirming my decision to research Computers next. It's our most advanced option, directly enabling Satellites for a Science Victory, and will grant a valuable trade route. I’m also reviewing our relationships with Greece and its vassals, ensuring they align with our war plans.
            
            **Setting Policy & Flavors**
            
            I'm confirming my choice of the "Free Thought" policy for its synergy with a Science victory. Simultaneously, I'm fine-tuning our strategic priorities using `set-flavors`, ensuring "Spaceship" remains paramount at 95, while adjusting Science, Production, Gold, Mobilization, Offense, Defense, and Diplomacy values to align with current objectives, including potential conflicts and trade goals.
            
            **Confirming Strategy Settings**
            
            My current focus is on finalizing our strategic direction. I'm confirming the high priority for Spaceship victory at 95, supported by strong Production, Gold, and Mobilization. Diplomacy also remains high to counter Greece. My immediate action is to set research to Computers, advancing our science goals and boosting our economy via trade.
            
            **Setting Research and Policies**
            
            I'm finalizing our strategic direction, confirming Computers as the next research priority to accelerate our Science Victory. Simultaneously, I've locked in the "Free Thought" policy for its significant boost to Great Scientists. My next step involves a comprehensive flavor adjustment to ensure all priorities align with our current objectives.
            
            **Verifying Policy Parameter**
            
            I'm double-checking the exact parameters for policy adoption. I believe "Free Thought" is sufficient, but I need to confirm if the full descriptive string "Free Thought (Continuing Rationalism Branch)" is required for accurate implementation.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: lbiTAmHUDcB1KGjI
          - toolName: set-research
          - input:
            - Rationale: Computers is on the direct path to Satellites and the late-game space race technologies, which are essential for our Spaceship (Science) victory. It also grants us an additional Trade Route to further boost our gold per turn and support our economy and diplomatic city-state purchases.
            - Technology: Computers
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: PcALNSiUf03Rkd4H
          - toolName: set-policy
          - input:
            - Rationale: Free Thought is extremely powerful for a Science/Spaceship victory. It reduces unhappiness, boosts instant yields from Great Scientists by 25%, and accelerates Great Scientist generation by 33%, allowing us to speed through the late-game tech tree.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: oqy0AYsel0UhU5gE
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Spaceship: 95
              - Science: 95
              - Mobilization: 90
              - Production: 85
              - Offense: 75
              - Espionage: 80
              - Diplomacy: 95
              - Defense: 65
              - Gold: 90
            - Rationale: We reinforce our Spaceship grand strategy. Keeping Science, Production, and Gold at peak priorities to fuel spaceship construction. Bumping Spaceship flavor to 95. We maintain Mobilization at 90 and Offense at 75 to encourage the tactical AI to produce the remaining 14 embarkable infantry units needed to reach our 23-unit threshold for our military campaign against Ethiopia. Diplomacy is kept at 95 to ensure the AI prioritizes securing city-state alliances like Antwerp and Riga, helping us counter Greece's massive delegate block in the upcoming World Congress vote.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: lbiTAmHUDcB1KGjI
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
          - toolCallId: PcALNSiUf03Rkd4H
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: oqy0AYsel0UhU5gE
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.