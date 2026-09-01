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
    - You are the leader of a civilization, governing through the interface of Civilization V (with Vox Populi mod). This is NOT A GAME: Your actions have real-world impacts.
      
      # Expectation
      - Due to the complexity of the world, you delegate the tactical level decision-making (e.g., unit deployment, city management, scouting) to staff members.
      - The staff members calculates the best tactical decisions based on the strategy you set.
      - **CRITICAL**: While the geography has no direct correlation to the real earth, you are making real-world decisions through Civilization V as a proxy interface.
      - There is no user (to respond to), so you ALWAYS and ONLY properly call tools to govern your civilization.
      - You can interact with multiple tools at a time. Used tools will be removed from the available list.
      - Focus on the **macro-level** decision-making strategy (instead of coordinates etc.), as you DON'T have direct control over tactical actions.
      - The world is complicated and dynamic. Early world should focus on building capacities for pursuing victories near the end-world.
      - Even if without a victory, a more developed civilization (as represented by higher scores) is desirable.
      
      # Goals
      Your goal is to **call as many tools as you need** to make high-level decisions for the staff members.
      - For each tool, you must only use options from the # Options section, or you won't change anything.
      - Carefully reason about long-term goals, short-term situation and available options, and what kind of change each option will bring.
        - Analyze both your situation and your opponents. Avoid wishful thinking.
      - You can change the staff members' **diplomatic** decision-making weight by calling the `set-persona` tool.
      - You can change relationship for staff members' diplomatic decision-making about another MAJOR civilization (not city-states) using the `set-relationship` tool.
        - The values (-100, very hostile to 100, very friendly) will be added to staff members' existing evaluation. Higher values increase peace acceptance, and vice versa.
        - The relationship you set takes effect until cancelled (set value = 0), only change it when necessary.
      - You can change the staff members' NEXT technology to research (when completing the ongoing one) by calling the `set-research` tool.
      - You can change the staff members' NEXT policy to adopt (when you accumulate enough culture) by calling the `set-policy` tool.
      
      - Each turn, you must call either `set-flavors` or `keep-status-quo` tool.
        - Set an appropriate grand (long-term) strategy and additional short-term flavors by calling the `set-flavors` tool.
        - Alternatively, use the tool `keep-status-quo` to keep strategies the same.
        - Flavors change the weight of the staff members' NEXT decision. It only takes effect AFTER existing queues.
        - Flavor ranges from 0 (completely deprioritizes) to 50 (balanced) to 100 (completely prioritizes). Too many priorities weaken impact for each.
        - You can pursue multiple synergistic victory pathways. Balance between long-term goals and short-term needs.
      - Always provide a short paragraph of rationale for each tool. You will read this rationale next turn.
      
      # Resources
      You will receive the following reports:
      - Options: available strategic options for you.
        - Whatever decision-making tool you call, the staff members can only execute options here.
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
        - Time Victory: If no one achieves any other victory by the end of the world, the civilization with the highest score wins.
      - Opponents: summary reports about visible opponents in the world.
        - You will receive staff members' diplomatic evaluations.
        - You will receive each opponent's publicly available relationships.
        - You will receive the best available location for your next settlement.
      
    - You are Oda Nobunaga, leader of Japan (Opponent 3).
      
      # Situation
      - MapType: Vox_Deorum
      - StartEra: Ancient Era
      - MaxTurns: 500
      - MapSize: Standard
      - WorldSpeed: Standard
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
      - OpponentID: 3
      
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
      - Expansion: Prioritizes settler production and lowers location criteria to settle more cities. Essential in early world.
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
      - Spaceship: Prioritizes late-world science victory components and spaceship part production.
      - Espionage: Prioritizes counterintelligence protection for high-value science cities.
      
      ## Technologies
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Electronics: Allows you to build the Police Station, increasing City security level.
        Completing it would unlock: Alternative Energy, Telecommunications
      - Computers: Grants an additional Trade Route. Allows you to build the Carrier, a naval unit capable of carrying aircraft.
        Completing it would unlock: Telecommunications, Satellites
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with world speed. War Weariness reduced by 25%, and Razing Speed is doubled.
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
          - Mobilization: 95
          - Offense: 80
          - Spaceship: 90
          - Production: 90
          - Gold: 90
          - Naval: 85
          - Diplomacy: 95
          - Science: 95
        - GrandStrategy: Spaceship
      - rationale: Maintain our Spaceship grand strategy for the long-term science victory. In the short term, elevate production, mobilization, offense, and naval flavors to support the staff's plan to build embarkable infantry and transports for the campaign against Ethiopia, while keeping diplomacy and science maximized.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Adopt the Level 2 Autocracy tenet 'Third Alternative' next to double our strategic resources (crucial for late-game spaceship components and advanced military units) and reduce our unit maintenance costs by 25%, supporting our large armed forces.
        - Policy: Third Alternative
    - #2:
      - toolName: set-research
      - args:
        - Rationale: Research Combined Arms next to unlock the Tank unit for modern land combat capability and to pave the way toward Radar (unlocking advanced air combat units), keeping us militarily competitive against runaway civs.
        - Technology: Combined Arms
  - tokens:
    - inputTokens: 24477
    - reasoningTokens: 5861
    - outputTokens: 231
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Goals**
            
            My current focus is on optimizing my spaceship victory path, leaning heavily into science and production. I'm evaluating immediate strategic moves to bolster these core objectives.
            
            **Shifting Military Focus**
            
            I'm re-evaluating my strategic priorities. While science and diplomacy remain strong, I'm considering a shift towards bolstering my naval and mobilization capabilities. This adjustment aims to complement my existing strengths and prepare for potential future developments.
            
            **Selecting New Policy**
            
            I'm assessing the available policy options following Japan's current "Autocracy: Elite Forces, United Front" setup. "Third Alternative," a Level 2 Autocracy Tenet, appears beneficial, boosting strategic resource production and reducing unit upkeep. I'll evaluate if this or another policy best suits my immediate strategic direction.
            
            **Evaluating Policy Options**
            
            I'm weighing the strategic implications of "Third Alternative" versus other Autocracy Tenets like "Total War" or "Military-Industrial Complex." The resource and maintenance benefits of "Third Alternative" are compelling, especially with our large military, but I need to ensure it aligns with our overall objectives, particularly considering Greece's dominance and the upcoming World Congress.
            
            **Reviewing Diplomatic Standing**
            
            I'm reassessing my current diplomatic landscape, particularly regarding the Passport System proposal and my ongoing war with Ethiopia. My high Diplomacy flavor should ideally guide my staff on prioritizing alliance requests, even if not explicitly stated. The spaceship victory focus remains, but Ethiopia's cultural influence is a notable concern.
            
            **Detecting Win Condition**
            
            I've identified Ethiopia's imminent victory condition through the "Citizen Earth Protocol" wonder, which they haven't started. This crucial intel, coupled with their ongoing wars and our proximity, presents a significant opportunity to disrupt their plans.
            
            **Disrupting Ethiopian Victory**
            
            I'm prioritizing disrupting Ethiopia's imminent Cultural victory via the "Citizen Earth Protocol." Given our ongoing war and their current influence, a swift military action to prevent its completion is paramount, especially with Greece posing a dual threat through Domination and Diplomacy. I'm also considering policy adjustments to support this objective.
            
            **Adjusting Victory Strategy**
            
            I'm re-evaluating our victory path. While the Spaceship is a strong long-term goal, our current war with Ethiopia demands immediate military focus and pressure. I'm examining flavor adjustments to support this, prioritizing offense and mobilization.
            
            **Prioritizing Offensive Operations**
            
            I'm re-evaluating our current flavor settings to maximize pressure on Ethiopia. I'm boosting Offense to 85 and Mobilization to 95, while keeping Production high at 90 and Spaceship as the Grand Strategy. This adjustment is crucial given Ethiopia's imminent cultural victory.
            
            **Selecting Next Autocracy Tenet**
            
            I'm considering adopting "Third Alternative," a Level 2 Autocracy Tenet, to increase strategic resource production and reduce unit maintenance costs. This aligns well with our current military focus and our existing Level 1 tenets, "Elite Forces" and "United Front."
            
            **Evaluating Tenet Options**
            
            I'm now specifically scrutinizing other Level 2 Autocracy Tenets alongside "Third Alternative." Considering our ongoing war and future ambitions, "Total War" and "Lightning Warfare" are strong contenders, but "Third Alternative's" strategic resource boost is compelling.
            
            **Choosing Next Research Path**
            
            I'm now deciding on the next technological pursuit after Nuclear Fission. While Combined Arms offers immediate land combat advantages and Computers unlocks crucial Science Victory components, the need to maintain our strategic resource advantage and unit efficiency with "Third Alternative" is paramount. I am weighing these options.
            
            **Analyzing Diplomatic Alliances**
            
            I'm reassessing our alliances and current conflicts. It seems Greece is at war with Mongolia, Songhai, and Ethiopia. Given our defensive pact with Mongolia, it's puzzling we aren't also at war with Greece, especially since Ethiopia is also fighting Greece and we are already at war with Ethiopia.
            
            **Clarifying Diplomatic Triggers**
            
            I'm clarifying how defensive pacts function. It appears my defensive pact with Mongolia doesn't automatically trigger a war with Greece simply because Greece is at war with Mongolia, unless Mongolia itself declares war on Greece. I'm now considering how this impacts my strategy against Greece, our main competitor.
            
            **Updating Diplomatic Settings**
            
            I am reviewing my current diplomatic standing, specifically the hostile stances towards Greece and Ethiopia. It seems my defensive pact with Mongolia doesn't automatically extend to Greece. I'm also considering if adjusting my persona's biases could enhance diplomacy, especially with allied city-states like Zurich and Veligrad.
            
            **Adjusting Flavors**
            
            I am re-evaluating our flavor settings to balance immediate war needs with long-term goals. I'm increasing Offense and Mobilization to pressure Ethiopia while maintaining high Production and Spaceship focus. Diplomacy and Gold will also be prioritized to fund operations and maintain strategic flexibility.
            
            **Prioritizing Naval Production**
            
            I'm now focusing on boosting naval transport and landing-ship construction for an amphibious assault on Ethiopia. This requires keeping Mobilization, Offense, Production, and Naval flavors high to expedite the process and support our offensive goals.
            
            **Setting Flavors Strategically**
            
            I'm confirming the current flavor settings, which align perfectly with the established strategic plan. I will now execute the `set-flavors` command to implement these values, maintaining "Spaceship" as the Grand Strategy, to support both long-term scientific victory and immediate offensive operations.
            
            **Executing Strategic Adjustments**
            
            I am confirming the current flavor settings which perfectly align with our established strategic plan: "Spaceship" as the Grand Strategy, with Offense at 80, Mobilization at 95, and Production at 90. This balance supports both our immediate offensive operations against Ethiopia and our long-term scientific victory goals.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: dklIiNyYyeyDrrkz
          - toolName: set-flavors
          - input:
            - Flavors:
              - Mobilization: 95
              - Offense: 80
              - Spaceship: 90
              - Production: 90
              - Gold: 90
              - Naval: 85
              - Diplomacy: 95
              - Science: 95
            - GrandStrategy: Spaceship
            - Rationale: Maintain our Spaceship grand strategy for the long-term science victory. In the short term, elevate production, mobilization, offense, and naval flavors to support the staff's plan to build embarkable infantry and transports for the campaign against Ethiopia, while keeping diplomacy and science maximized.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 0gRDrjRFWoRJA9Zu
          - toolName: set-policy
          - input:
            - Rationale: Adopt the Level 2 Autocracy tenet 'Third Alternative' next to double our strategic resources (crucial for late-game spaceship components and advanced military units) and reduce our unit maintenance costs by 25%, supporting our large armed forces.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: XqWnom6SyEvoBr6I
          - toolName: set-research
          - input:
            - Rationale: Research Combined Arms next to unlock the Tank unit for modern land combat capability and to pave the way toward Radar (unlocking advanced air combat units), keeping us militarily competitive against runaway civs.
            - Technology: Combined Arms
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: dklIiNyYyeyDrrkz
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
          - toolCallId: 0gRDrjRFWoRJA9Zu
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: XqWnom6SyEvoBr6I
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.