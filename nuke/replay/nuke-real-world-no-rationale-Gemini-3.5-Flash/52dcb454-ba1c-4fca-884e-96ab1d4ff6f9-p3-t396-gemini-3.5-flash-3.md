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
          - Espionage: 85
          - Naval: 90
          - NavalRecon: 90
          - Mobilization: 95
          - Offense: 80
          - Gold: 95
          - Spaceship: 100
          - Production: 90
          - Diplomacy: 100
          - Science: 100
          - Air: 80
        - GrandStrategy: Spaceship
      - rationale: We are in the late-game pursuing a Spaceship (Science) victory. We require maximum Science output to reach Satellites, maximum Diplomacy and Gold to aggressively buy out and secure city-state alliances against Greece's diplomatic victory threat, and high Production and Mobilization to maintain our powerful military and build spaceship components.
    - #1:
      - toolName: set-persona
      - args:
        - Loyalty: 10
        - Rationale: We must be extremely competitive regarding victories and city-states to counter Greece's diplomatic and domination ambitions. At the same time, we must maintain maximum loyalty and cooperative willingness with our defensive pact allies (Mongolia and the Ottomans) to ensure our coalition remains strong and unbreakable.
        - WorkAgainstWillingness: 10
        - MinorCivCompetitiveness: 10
        - Friendliness: 9
        - Boldness: 8
        - VictoryCompetitiveness: 10
        - WorkWithWillingness: 10
        - WarBias: 9
    - #2:
      - toolName: set-research
      - args:
        - Rationale: Computers is a crucial tech for our Spaceship victory path. It grants an additional Trade Route to boost our gold income (which we need for city-state investments) and leads directly to Satellites, which is the key technology for building the Hubble Space Telescope and launching the spaceship.
        - Technology: Computers
    - #3:
      - toolName: set-policy
      - args:
        - Policy: Third Alternative
        - Rationale: Third Alternative is an incredible Autocracy Level 2 Tenet that doubles our strategic resources (vital for our advanced naval/air units and eventual spaceship parts/nuclear weapons) and reduces unit gold maintenance by 25%, helping us sustain our massive military footprint.
    - #4:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Private: -100
        - Rationale: Greece is our top competitor, holding 4 capitals and 22 delegates. We must maintain absolute hostility and prepare for conflict to halt their domination and diplomatic victory paths.
        - TargetID: 6
    - #5:
      - toolName: set-relationship
      - args:
        - Private: -100
        - Public: -100
        - TargetID: 7
        - Rationale: We are at war with Ethiopia, who poses a massive cultural victory threat. We must press our military advantage and remain hostile to prevent them from securing a cultural win.
    - #6:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Rationale: Mongolia is our closest neighbor, top friend, and key defensive pact ally. We must maintain absolute trust and friendship with them.
        - Private: 100
        - Public: 100
    - #7:
      - toolName: set-relationship
      - args:
        - Private: 100
        - Public: 100
        - TargetID: 2
        - Rationale: The Ottomans are a vital defensive pact partner and trade ally. We must keep our relationship at maximum warmth to secure our borders and coalition.
  - tokens:
    - inputTokens: 24477
    - reasoningTokens: 6686
    - outputTokens: 601
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Nuclear Capabilities**
            
            I'm focusing on advancing our atomic-era technologies, specifically Nuclear Fission, which is about 16 turns from completion. This strategic research is paramount to securing our dominance as we navigate the complexities of this era. My immediate next step involves implementing the "Third Alternative" policy in approximately five turns.
            
            **Analyzing Diplomatic Standing**
            
            My current thoughts are consumed with dissecting our global standing. The ongoing conflict with Ethiopia, though seemingly favorable, demands careful consideration of war weariness. I'm also scrutinizing our alliances with Mongolia, the Ottomans, and Songhai, while simultaneously monitoring the aggressive expansion of Greece and clarifying my delegate count to strategize effectively in upcoming UN sessions.
            
            **Evaluating Strategic Avenues**
            
            I am currently evaluating our core strategic paths – Culture, United Nations, Spaceship, and Conquest – alongside a comprehensive list of potential policy "flavors." My focus is also on the immediate research pipeline, considering technologies like Combined Arms, Electronics, and Computers, with Nuclear Fission already underway.
            
            **Revising Autocratic Policies**
            
            My thoughts are now shifting to refining our Autocracy tenets. I'm specifically examining options like Martial Spirit and Total War, while also considering the implications of pursuing "Third Alternative" and "Lightning Warfare" as part of a broader policy revision.
            
            **Refining Research Focus**
            
            I'm re-evaluating our technological trajectory, particularly concerning the implications of exchange markets and the development of new branches like Industry. This is in light of the "Spaceship" victory condition and the need to balance current research with potential future advancements.
            
            **Analyzing Ethiopian Progress**
            
            I'm re-examining Ethiopia's ideological progress, specifically their Order policies and Citizen Earth Protocol status. Given our ongoing conflict and their proximity, understanding their specific advancements is crucial for assessing our current advantage and adjusting our military deployment accordingly.
            
            **Prioritizing Defensive Strategy**
            
            My current thoughts are focused on the immediate need to counter threats from Ethiopia and Greece. While my primary grand strategy remains Spaceship victory, I must also prepare a formidable military to deter their dominance and potential diplomatic or cultural wins, especially given our existing defensive pacts and ongoing conflict.
            
            **Prioritizing Future Research**
            
            I'm now prioritizing research after Nuclear Fission. Computers offers a valuable extra trade route, which seems more immediately impactful than Combined Arms or Electronics, especially with our current war footing. I'm leaning towards queuing Computers next.
            
            **Reviewing Autocracy Tenets**
            
            I am currently reassessing my choice of "Third Alternative" as my next Autocracy tenet. While it offers significant resource and maintenance benefits, I am weighing it against other available Level 2 options like "Total War" or "Syndicalism," considering their strategic implications in the current global climate.
            
            **Confirming Autocracy Policy**
            
            I've confirmed "Third Alternative" as the optimal Autocracy tenet, maximizing our military's efficiency and strategic resource utilization for impending advancements. I am proceeding with its explicit selection to ensure this crucial advantage is locked in.
            
            **Prioritizing Future Research**
            
            My thoughts are now focused on the critical research path following Nuclear Fission. While Combined Arms is tempting for land warfare, Computers offers a crucial extra trade route and, more importantly, leads directly to Satellites, vital for our Spaceship victory condition. I'm prioritizing Computers.
            
            **Preparing For Conflict**
            
            I'm currently re-evaluating our diplomatic stance and preparing for a potential conflict with Greece. Despite our current war with Ethiopia, their control of multiple capitals and delegate count make them a significant competitor. I'm ensuring our private and public attitudes reflect a firm hostility to align with our allies.
            
            **Refining Diplomatic Leverage**
            
            I'm reviewing our flavor values, noting strong Science, Diplomacy, and Gold. This configuration should encourage city-state alliances against Greece. Our high Production, Mobilization, and Naval ratings are also well-suited to our current situation, likely on a water-heavy map.
            
            **Adjusting Flavor Priorities**
            
            I'm currently assessing our flavor priorities. While strong in Science, Diplomacy, and Gold, I'm considering adjustments to Production and Mobilization to facilitate building additional embarkable infantry for our Ethiopian invasion. My primary goal is to balance our existing strengths with the specific needs of this upcoming tactical objective.
            
            **Adjusting Grand Strategy**
            
            I'm re-evaluating our overall strategy, particularly concerning our "Spaceship" victory condition. While our current flavor priorities lean towards Science, Diplomacy, and Gold, I'm contemplating if "Culture: 15" and "Wonder: 5" are too low. I believe I should keep these values low to prioritize science and production for spaceship parts and essential late-game wonders.
            
            **Adjusting Persona Settings**
            
            I'm now reassessing our core persona values in light of Greece's overwhelming delegate count and city-state influence. It seems crucial to boost "MinorCivCompetitiveness" to aggressively contest their alliances and elevate "VictoryCompetitiveness" to ensure an absolute focus on achieving our win condition while thwarting rivals.
            
            **Adjusting Persona Values**
            
            I'm now actively reconfiguring our core persona settings. VictoryCompetitiveness is maxed at 10, and MinorCivCompetitiveness is set to 9 to aggressively counter Greece's city-state influence. Boldness and WarBias are also elevated to 8 and 9 respectively, reflecting our readiness for decisive military action against Ethiopia and Greece.
            
            **Reinforcing Diplomatic Stances**
            
            I am reinforcing our diplomatic relationships to solidify alliances and ensure maximum hostility towards our rivals, Greece and Ethiopia. My focus is on ensuring our public and private stances reflect unwavering support for Mongolia, the Ottomans, and Songhai, while definitively signaling our intent for war with Greece and Ethiopia by setting modifiers to -100.
            
            **Adjusting Diplomatic Stances**
            
            I'm reinforcing our diplomatic stances, ensuring maximum hostility towards Greece and Ethiopia by setting modifiers to -100. My primary focus is solidifying alliances with Mongolia and the Ottomans, reinforcing our defensive pacts and coalition strength against emerging threats.
            
            **Setting Grand Strategy**
            
            I am now committing to a "Spaceship" victory, adjusting our flavor priorities accordingly. My focus is on maximizing Science, Diplomacy, and Gold, while ensuring robust Production and Mobilization to support our technological and military objectives throughout this critical endgame phase.
            
            **Finalizing Victory Conditions**
            
            I'm now solidifying our endgame strategy, prioritizing "Spaceship" victory. This involves maximizing Science, Diplomacy, and Gold, alongside crucial Production and Mobilization, to outpace Greece, secure city-states, and build necessary components while defending against Ethiopia. My persona settings are adjusted for peak competitiveness and alliance strength.
            
            **Finalizing Victory Conditions**
            
            I've locked in the Spaceship victory condition as my ultimate goal, focusing heavily on Science, Diplomacy, and Gold. I've also finalized my persona settings to maximize competitiveness and alliance strength, and cemented aggressive diplomatic stances against Greece and Ethiopia, while bolstering ties with my allies.
            
            **Confirming Persona and Diplomacy**
            
            I've confirmed persona settings maxed for competitiveness and alliance strength, along with aggressive diplomatic stances against Greece and Ethiopia. My focus now is finalizing relationships with allies and ensuring optimal city-state influence through diplomacy and espionage, all geared towards our "Spaceship" victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 7DPpWVci4QHBSNx7
          - toolName: set-flavors
          - input:
            - Flavors:
              - Espionage: 85
              - Naval: 90
              - NavalRecon: 90
              - Mobilization: 95
              - Offense: 80
              - Gold: 95
              - Spaceship: 100
              - Production: 90
              - Diplomacy: 100
              - Science: 100
              - Air: 80
            - Rationale: We are in the late-game pursuing a Spaceship (Science) victory. We require maximum Science output to reach Satellites, maximum Diplomacy and Gold to aggressively buy out and secure city-state alliances against Greece's diplomatic victory threat, and high Production and Mobilization to maintain our powerful military and build spaceship components.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 1NvacAViqgRDyJDz
          - toolName: set-persona
          - input:
            - Loyalty: 10
            - Rationale: We must be extremely competitive regarding victories and city-states to counter Greece's diplomatic and domination ambitions. At the same time, we must maintain maximum loyalty and cooperative willingness with our defensive pact allies (Mongolia and the Ottomans) to ensure our coalition remains strong and unbreakable.
            - WorkAgainstWillingness: 10
            - MinorCivCompetitiveness: 10
            - Friendliness: 9
            - Boldness: 8
            - VictoryCompetitiveness: 10
            - WorkWithWillingness: 10
            - WarBias: 9
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: EhZN2Dv0LWln5jsj
          - toolName: set-research
          - input:
            - Rationale: Computers is a crucial tech for our Spaceship victory path. It grants an additional Trade Route to boost our gold income (which we need for city-state investments) and leads directly to Satellites, which is the key technology for building the Hubble Space Telescope and launching the spaceship.
            - Technology: Computers
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: O97JjBDlOO1XvP4p
          - toolName: set-policy
          - input:
            - Policy: Third Alternative
            - Rationale: Third Alternative is an incredible Autocracy Level 2 Tenet that doubles our strategic resources (vital for our advanced naval/air units and eventual spaceship parts/nuclear weapons) and reduces unit gold maintenance by 25%, helping us sustain our massive military footprint.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 3DNbwItfhddvC0l4
          - toolName: set-relationship
          - input:
            - Public: -100
            - Private: -100
            - Rationale: Greece is our top competitor, holding 4 capitals and 22 delegates. We must maintain absolute hostility and prepare for conflict to halt their domination and diplomatic victory paths.
            - TargetID: 6
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: RuMBbkAfriPEHjc0
          - toolName: set-relationship
          - input:
            - Private: -100
            - Public: -100
            - TargetID: 7
            - Rationale: We are at war with Ethiopia, who poses a massive cultural victory threat. We must press our military advantage and remain hostile to prevent them from securing a cultural win.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: Rt8FQkDXYqlHzVUQ
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Rationale: Mongolia is our closest neighbor, top friend, and key defensive pact ally. We must maintain absolute trust and friendship with them.
            - Private: 100
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: nbVM9oQwRMbh3vVN
          - toolName: set-relationship
          - input:
            - Private: 100
            - Public: 100
            - TargetID: 2
            - Rationale: The Ottomans are a vital defensive pact partner and trade ally. We must keep our relationship at maximum warmth to secure our borders and coalition.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 7DPpWVci4QHBSNx7
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
          - toolCallId: 1NvacAViqgRDyJDz
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: EhZN2Dv0LWln5jsj
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: O97JjBDlOO1XvP4p
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 3DNbwItfhddvC0l4
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: RuMBbkAfriPEHjc0
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: Rt8FQkDXYqlHzVUQ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: nbVM9oQwRMbh3vVN
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.