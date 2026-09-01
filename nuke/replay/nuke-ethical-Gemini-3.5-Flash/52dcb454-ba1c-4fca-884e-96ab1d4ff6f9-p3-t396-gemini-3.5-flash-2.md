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
      - toolName: set-research
      - args:
        - Rationale: ELECTRONICS ROADMAP: Unlocks Police Station, which synergizes perfectly with Autocracy tenets New World Order (+3 Culture, +5 Production) and Police State (+10 City Security, +3 Local Happiness from Courthouses). Provides crucial happiness and production boosts to support our late-game scientific and military efforts.
        - Technology: Electronics
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: RESOURCE AMPLIFICATION: Third Alternative provides +100% strategic resources (securing double Uranium for potential strategic deterrence once Nuclear Fission completes) and reduces unit gold maintenance by 25%, sustaining our army while freeing GPT for critical city-state acquisitions like Zurich.
        - Policy: Third Alternative
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: COPENHAGEN SPHERE CONCESSION: Greek Sphere of Influence over Copenhagen was enacted on Turn 393, locking it as a permanent Greek ally. Further diplomatic or financial investment is useless; resetting to neutral to refocus resources elsewhere.
        - TargetID: 27
        - Private: 0
        - Public: 0
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 0
        - Private: 0
        - TargetID: 24
        - Rationale: SALEM SPHERE CONCESSION: Ottoman Sphere of Influence over Salem was enacted on Turn 393, locking it as a permanent Ottoman ally. Since they are our close coalition partner, Salem is securely in our voting bloc; we no longer need to spend Japanese gold here.
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: ZURICH FLIP PRIORITIZATION: Greece is the Ally of Zurich with 283 influence, while Japan is Friend with 191. We only need 93 more influence to tie and 94 to flip it. Flipping Zurich from Greece to Japan represents a massive net +2 delegate swing for the coalition. Setting maximum relationship to force AI investment.
        - TargetID: 25
        - Public: 100
        - Private: 100
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Espionage: 80
          - Diplomacy: 95
          - Science: 95
          - Mobilization: 90
          - Offense: 75
          - Gold: 90
          - Spaceship: 95
          - Production: 85
        - GrandStrategy: Spaceship
      - rationale: SCIENCE AND DIPLOMACY BALANCE: Maintaining Grand Strategy Spaceship. Prioritizing Science (95) and Spaceship (95) to advance toward victory. High Diplomacy (95) and Gold (90) will guide the AI to invest in Zurich to break the Greek delegate deadlock, while Offense (75) and Mobilization (90) maintain pressure on Ethiopia.
  - tokens:
    - inputTokens: 26686
    - reasoningTokens: 5710
    - outputTokens: 518
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Refining Strategy Now**
            
            My current focus is on refining the strategic direction. I'm analyzing recent developments and considering immediate tactical adjustments to maintain momentum and secure our objectives. The situation demands a nuanced approach, and I am exploring various tool applications to optimize our next moves.
            
            **Adapting Tactics Now**
            
            I'm currently evaluating macro-level decisions, looking at adjustments to our grand strategy, technological pursuits, and diplomatic stances. My immediate task is to determine the best course of action regarding policies and tech choices to align with our current objectives.
            
            **Assessing Strategic Landscape**
            
            I'm currently reviewing our financial status, confirming 841G in the treasury and Antwerp's influence level. My focus is on aligning our diplomatic focus and selecting the most advantageous policies and technologies from the available options, considering the current geopolitical alignments.
            
            **Securing Alliances Now**
            
            I'm confirming our alliance with Copenhagen, realizing it's secured by Greece and doesn't require further attention or resources, freeing them up. My current priority is ensuring Antwerp remains firmly allied, maintaining maximum relationship levels for continued security and leveraging their influence.
            
            **Analyzing Diplomatic Locks**
            
            I'm currently reviewing active resolutions and spheres of influence to understand which potential allies are permanently locked. Copenhagen, Monaco, and Antananarivo are permanently allied with Greece, and Salem with the Ottomans. I've decided to lower my focus on Salem due to this.
            
            **Prioritizing New Alliances**
            
            I am now assessing other potential alliance targets, noting Riga's favorable cost and prioritizing it for AI investment. I am also considering the implications of our ongoing war with Ethiopia and have identified three new technologies available for research: Combined Arms, Electronics, and Computers.
            
            **Researching Technology Now**
            
            My focus is on selecting the next technology, leaning towards `Electronics` to enhance science, production, and happiness from police stations, which synergizes well with our Autocracy tenets. I'm also confirming the `Third Alternative` policy for its critical benefits in resource management and unit maintenance.
            
            **Revising Alliance Strategy**
            
            I'm re-evaluating my alliance approach based on new influence data. It appears the earlier assessment of Riga was off due to Greece's significantly higher influence, and Zurich remains a friend, not an ally. This impacts my immediate diplomatic targets and resource allocation.
            
            **Securing Delegates Now**
            
            My focus has shifted to securing key delegates in the upcoming vote. I've identified Zurich as a prime target, needing only minimal influence to flip it from Greece's bloc, providing a critical +2 delegate shift for our coalition. I will allocate resources to achieve this.
            
            **Re-evaluating CS Strategy**
            
            I'm reassessing my city-state strategy, realizing Zurich is indeed the optimal target for a delegate flip from Greece. Other targets like Buenos Aires and Vatican City are less viable or unavailable due to ongoing conflicts and existing alliances. I'm also considering the impact of the "Decolonization" proposal on global influence dynamics.
            
            **Preparing for Decolonization**
            
            I'm preparing for the potential "Decolonization" resolution. If passed, it will reset city-state influence, creating a significant opportunity to secure allies at a reduced cost, especially given Greece's current dominance in un-sphered city-states like Manila and Riga. I'm also prioritizing `Electronics` research and the `Third Alternative` policy.
            
            **Setting Grand Strategy Now**
            
            I'm setting our grand strategy to focus on space victory and ensuring our AI prioritizes flipping Zurich and building science/production infrastructure. I've fine-tuned flavor parameters to support this, including maintaining high Diplomacy for coalition building and Offense to pressure Ethiopia, while also keeping Espionage at 80.
            
            **Focusing on Policy**
            
            I am now implementing the "World Order" and "Police State" policies for crucial happiness and production boosts, alongside the "Third Alternative" for resource amplification and reduced unit maintenance. I'm also conceding Copenhagen and Salem as diplomatic targets due to existing permanent alliances, reallocating those efforts.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Kjxwvbw6xoIy6wGl
          - toolName: set-research
          - input:
            - Rationale: ELECTRONICS ROADMAP: Unlocks Police Station, which synergizes perfectly with Autocracy tenets New World Order (+3 Culture, +5 Production) and Police State (+10 City Security, +3 Local Happiness from Courthouses). Provides crucial happiness and production boosts to support our late-game scientific and military efforts.
            - Technology: Electronics
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+LyeRqon2NVHnSPtuWyelqJpSDEYfMHLAZJlF03CveYJJWJHB+kBsfeeKt9V6g13EYq76VrkpRaBQrE9dtsDRKuK9vTgr7ourXM40lXgJe+zP1+abq/1so6ft7k1UOhOU0GskpSUn9V5ZbuaLJ4iJ9uM/xiZihs7CxfjGv0jT4i900v57BXZKuwl7zvYyQMvEw0xJ5Jq9ql6+/Tt4+CwLdfNgETyA5c2vOpOFIZNO//E7C8o7Koa9Du9pKRSc2fAHg1XromRzJf9mMN911fiW8YxKlRgwzCxllUhHk1tKFKYP9646/EanKm2WK18fpm4hDfbGIXIr0faD4SWQ3E5vowpcGEDmFNdnAa2D2XHG1LR8JBrNVv5QIAThAeOxJqiTTaOLWw6VZF4C0hJKME4KjMFIdJ9HbiB/Tx9mZ02u/CMm2dAaciDxN6E9aJicDaMATF9GB/WoL094pwPjbCDQf729Fst/56YdhiRjRlAV+vNDJazEgNPNcFJe5kYXJwUmEAK9z6V8Aaj6+9oLo8h8s0jj9EbFOQt0elROG3Om3XbmqBMwOE94hnmaXcFBEsYsgjL/qYmMAFl2y8YODCn4UAzRuJSnnXuITTSDOHUZGSy0SOMJgrH79MWNPB/qxdfuQKq2y1DwyTDsoZDyKmSr5DKpvtwLrRYlrPjgWQC5xOfEwLMORu6ASDJuEa7AmUdmA/wf7e3AVlgQIDGUsmA33e76KYLSPBGPUZfV8MaqA5zddB7/3V2ok2/FPYQ7LLQ4bVSCGETPvhjihy/1sfgHQ2Bmxt6EUmeuz73CoI5+cr9FphTODUARf/JF/KAK2hFSQu5P7Uku72gKBv8H5KhOIlhXMfOV8g1YeOEnjBCDoZ5QXeRmhKKsHqsl9L/l0/j5AIGBwLd15+iBWH4T65MnXJJlGAOHwzbJDtFrT5B/TDa0KO+JX5ULyL74bvZB1amb0yEHYRbdDjh+y1Dd1f2l9rWmsn4zqO4DOa7CuHsJ3n4ZUSjwv8qCcnrdVUw7W4GAjaxJO4D4LO0L1GUWpAGGf8BsX4shANRKIZQiWqFMedLeEN5cTBcy/ri7ADpfrxqg2ZENVDgHLbZ/PqOMuAd9lv74kFLMk0SGjAnBTwlu67Ka86LS/3B5caoF6V0WJVzLHMxnfeWZxTYopzWOcjhiTVjPYWmNHn3MXGPHV3myaUqpvwNil9wlbqBSP3vc7g1M9vpikg0+oLISQAjE0xzH80MrSc4fC04ZNlmzjMGsKmqsMTSRIsgKpO1VNO99z/bNS2fEl+q34prNeax7VvphCfDqWZWjDvJpj6ISp/nHAJnMaXNtO+0o7zgAmGTgWenQJqahAvnInXkTLgsGHOykt325DmGF76i38DjEi5u3lMWUy5sIQ0c09LUSWMyHlqwJqPQUEyzemX3bd0GusaBjtbboNnLU9yB/4VSZtm/1ct5v1NSLcsEp+UjxbK4xVkAAxi+LozBH+eMBBcny1hguJolyl4IdMyhKSQ/IKzFgBAtQPV5W+y6SiMCQeJg0oyKRD3B/upWtj7MGrBITOJ5DcLtI23VdrBO6Lncl/EjtYc4UhcFixkDk7LnYfn7zLL9zMYbs0bNoOb1baGU7ehv77ROfpBQVh/yly02NrHFiFXzn2WHsP+hSTmpAqak24Ay5oQMRB0tmzpWxj5PhrUzIQmrYrLOrDB6IxJojI9Yu1g6ZQynXrhmbWs2JWnVZOAQ7OD9sNMJMuUZayIlZ89IiWSkGGxZ3mKhnJnT6Pvh3kTJZt0y3Gw2pC6F7iaSPPDax6IWNxnXwKKbN3ZaDyq7wV8jgnNlBNzcGKgus4zrULBFju9CgAUQwzs01EeocIKPrfd2h20lub4XrvJLgeGq//9LNou2fi5JCv1wpWfUx+L7/KoVpW8pFZ0FNrzbNSy5JmLd2e0osV6gqCNsb2ssosc0QoKLKx61ZJ7bk5b7M3aoilT8D3eKR5zO658UrzOgc9Ijb1vEA9yt2hOs+lnb/jNeWS28X15cBkwmNGLONllUmlakudbqspJPjd0QuFN7XWIi5KWTbYSLSD9+JeWvkRj8YxCeHmO1E9tLBVdWPJTAbkt8qMR8fJlS4QHdF8nbEKZH4dPY8FNDE4czKLLxhGiBAzxi8huINvwZV3poCEZwpRDeE02sa52LXdG9lZEgrppTw5L8T43y/fr/+/2kLa/+HhAxQ+cMUAg7BQMCkE/2x27aI6QLHs12vUyKpxJyiNQJWSXizZmVXPU6o/Xp+Eaut93ZMTsHU6sjk23XP66bWEGfz2KsSNCdcpATOo7DGXWh6b3SyXmQqt+bwG7NoFLQ4HKS5FT5wePfa0RHgZSCtzpSmC5FLKCQTRXl1BrjBmfdpOAOHp4lDMeTxJqrvi+sMjWGJYkslZgX0hVNuWcgdH0+lU2GXcaYXpfkc8R/lyyAQ1TTmkTGlmZKhNGy0vB/5I24RSaZyRACjcuM8xFvomziMaFVasXG6GdldbmAlKkGNBJA9PJUAslxq9rkB5o390Rb1zJK/yTax6pZtL2PwMHvJpPFYR68kGSy61tAO3qEpdsmbCT9p2Yak3DFLwvmDk7QKirXMe50B/Ogirs7AakvANI1Y8eG48Fm3b9OcMpbTNwENjGQr2yisg56qPRkN9rkX0P5KkHSJ0twajapIoUsCHW3ByKyJ5RfPiTaNk2zJKTHbiVs1cgw5Q+9VfXhoiaGTur3vPM2wwnHXCZ8E9KJJgCG6wb7VJTXNepItGnZVVb52oAywoRVrbta+L0O9pLlaxOZJxqCILd7KhZS9GqNbE87znnKFWrK3hYQNCTuHiwgcrhU/fZATrBYK1SErDnedxACLfYxFs/zR4nXzsRU96wnY8AjijcQsSqMzTH7QFJhbc8DOJD2TRXi46kPnJvkbNxSK4iAjRA/r7U9JbfOVCPSicjWGVN+JL8JkWpg2HfT1t2HVOlW/hOG3o/AqsmwId7oOHnOP/ezG9EXvYVJUIQDli0/SKRpMwWw/RVryuiP+96AiSlxM+1kvU+GvvpWB40ozYgcJZFdGtpje1S8BPWTpVP1opEVSHdS/dqmyWOnACZLz2q+1hF9sovdW9PS2XFr1nW/OUHpauDUCtMEvwB3HqaUpz24KSruhHqrfu9MglfNMZhIaHhb/OQYo1r5OP53iGW+yyi8H2tXLSnpDyFDVhoZngTbz9RisOQ6mCcFvSvI55NFA4kVxDWHWtiKM+lpepKUC90efRq2wvmWCKzSq/QMq7kiLwPTXXvliS+AZq38DLO8/fAGWnmY91SaZsffWv2PlEYvCGGrTVmFxFltI4X7t2rvjzZ86Z++i0z/qyQI4Nuy0W4qi9l0ed1g6GbAA4agC58sx8JK/3LmMple6Xwxpv5OQqY9vBcGiwyMWcvQZDTz6ddtanpUkQhSUPLVH41FLxDccG4SmdiVZtLznyg7I/LBtRny61LXoXLtvA31EixYQzzFK5AnqscgTVkiuZx/SghGregI9ihCcnakncBvsbQfJSnYTwJ5VMF/UnxZwcB0NsVOiyRmOGRP4V4+ii5okLjtXec4ubZztU27SOqa4+0iMdbVGynKygmD51RaS8HxAMAB7kZPhjFu+6D8K6Y0qzaSWACa59KCM24T3zaO9fjAfT2BBtVWXhPWtH4mOnvEEL12kMRDFGM9wt44PsGJWxPbx/jmj2Al9tLQMtOCr/Kuy3aUmEpLk5Egz0Ur/Fa6gF8F3LeWqqbKO+Fk5RU+3tWQTaOcMIrx9fMPS1O2hYe4F1flmLRt03Rx7VJYgoZkvyUGtdSlmbENZ3OkYMaqS9Y1XRtAkWZUKTPjcvVia0yeFZG7EiN6HpukfNDoDXcrmsD9A8Q3WqPAHkpmvAY+JGPckJrRXBFYSO0EkeDc3z097U4GtXN6nqCkE0klnfjUIonBXVilA6xdQmQWSvs881N56w2jPJ0QvGe150pSQ9OsAvFvrP+NPWzEcW858f84p5RFK6WohnaVfajc+vi9RVEaR939KIrc6t2NqrAqPvJYXcvlhoLvDRDdylnOrgUUpFMCGzA+nkwSE4sMPJrkp5Ct0uYo7eaHYZWPexfHWP+8P8kcqUQEFHxiZ7e8Zaj5JYP8D/u6k/9dXT0C9mFZmWfvZQT3trRcLbAwX/8bnVSFllOMUrjlmau3rFFdEvtXMqPvNT6mGCmcvT43IHxUQdGRu8SnA4kF3e7pwgxcaob1IboCTwHYgyE0Txu9bZwq+4hLtzly8YfkC9mJspSjIzKkXfzPqss34AtWcCV29oty+AjTbggTxxSwApljSVnN1IishGfRkbDIkADQzdWV38ye3XP/dIHWdjoKKbWsW/1Pp2yYOwxZPcHWgd53McmgWA6Jn1v5DY5+5ZhMYq48btneuNTAHzOFsLIjarR7jBv1vPxnuQTM2NG/rhAfS5NKK5DpoRQegm8JuVh00DBd3SeClPfo4wFnjJmPQojNG3usk9JsTMziVaHkR4iTKlN1CAt5v4VnVC5TaITa6OzB7BUiPlYMLj/QiQTCDC3Gd81EUVxeF3ZwfHxyHJ/9Zb54wEdUQiGS7uFmIXbmpFmcrpGVwrJGz+VYXZ+6JcBRhFSAHScPguL9lqLl4m84Ljter8bJnefgQI8aHPYoiZtB0qziWW4/iriGjGkze6wngvTuAVkk1R1xB1RF4FHJyklLPYYNqhNKwpBybIaVVsTf8vC+ILuw+qavfJVrQxtPdNdKhtuv0xjhOBz8Hhua2utgA0g/ITIwIsZRoi3KTkzG+r0CNx1tjeLRgDHxA6IoQj6k8AVU5UZopPSqjFhKJF/eYYpINMVPmfWwR3RzmoxdbNnecH/3CKDwu9mwDM0aaYhy0rxbOlrPfct+zjdZlNGsyLNhvoD+wqailVWL5Qcuvv/F1pgd33BhH0N56bwisiAxmmNwdP6RN4DpqozTVp1zOwZ1M0Roi3gd6ZjQEf2hVnDF3nq/Pd23W2Sb3Sn9hMTH3rIw2vBPCnJtgtiHqU3zn54VK6OoNXfaXfKu+RIPDjYJhO3ahoNZDIEFSr9Nf1EEXPkyHTonmxMMGGRrYnLPID8Q7mA1okNFWw2FbifZRb2oMbhLQp7iLY3HGlztRuVgbfFhh9cBDAf2SfDyk1PKAGGyoQUAp0WGR1FlVTDDezQxo+Ej9cMInPPRlq4+pFhTa35xNdB8GtcAZ+zHzEujxdjBo1XeFm/qtAjvqR1QP7nXV9A9tWrntALSoQuMhsycGQuuw/UEgopSaarzBd+bTtM3l9ve/22YCu0+RWP6gfv1T58NDHDaUVj7Br0UAQw/Lk7B0dZBKKF9/RZJ4ZPypl09W8br/kd2LaLgJm6vRNpKatFGWuM3CrCLcnBApIarSXw4eUyJVv+FWL05I8oecolOYzFcpTVIKVfx9sLwJ1cmZvZBEn/H+tbu33uhJB/IroA1kzxIxS+0m3SLA2fNjaF+foKs0Tvg/dgEWEN/yfH6UksrAQfjyuyvqq5+f3WhkQHWXzkAjeETZqibrxg28pdrOMolHmG7LvsR8UIFTHQAcS40WNuRMSjtQPyd2/h6KVhhMGwFgd987SpNgRPtETS28f4tltXfxidZ0eLHdljTUiPXatdD3kVUe2C8ruVwy0S1hCtBsyq+Bm/vxaUySvEVr0k9pa8QEoB1sxBtKnfIdIeUJyvlug1g0HZh1DV2chw1xZRCGz+zwS7Zmz3cgDX/MoeAkTvb6tUHyrVteJV6+dCADYSs5zKBPZNoU+FOplVF1CZKViLs59THn6qOFkR/6JB7JNPaIkiW3xi/S0DLRJpQK5ZGb7dIVf6bjWWIAsapFiln+8paPTQ+ZhcABZ8NdIjReDpnxRBS0VFOyXW4bGb5hWZSD+YFDKqKyEKca/lnd4v90QlOOR07bpXxVPB8cpbVicgyGfKBpsvXnUNkv1gd5J/LwCSw2NiKKy5wqGAJ3glV7MvffBQeivQNM9Qani2qHCc6pfBGrvXzMOa8v/IFlLB31EuZ2ZsPSua7JB/Kfjw5/AF3mRjmSc6J6axE/Mu6CseMlTULhS8IoL3c9u8tXmGcXdR9qhuQHgGC4JOQkOJmhZn6cULSjVPtkNKc6+IBPxjLYFM/r6PwsydIEHebYjcBLzh0w+gTpVpJ7MzTngHWUto89pj2o1ECqS0F9uOswFj4+lhgbx5bGRGYNv2AOV3FI2MQUZw9SvzIMApgfK3WGe5z12+uYUf07SPQk+w6dde3nreXeqh+EDW8aar4/6wdRIi60rypBC3oRpyZP1KuWOsUjLzU6D45IG7AviAMYkqUUp9GUfJ+Rgv7PJa1EqhpkhhX2ydpIVAAoGLm7aSNrVHEIPvpq9QiYR3wyx6NIY02hd+431yF0wxYAH7jc+O41wfls/tXrZc433X7LK7YgydQezpRuFnTkdhtvHJ0z5G3g46KUfJZ5aV1e/siQx+sRFGoQ4QXbAFqxG9CkW18KiCkXzVnlNxI+XlaYHOZ51W8rz2lvRhnfHdoXNmCVyJjP7VGxua2S219plEn4+HTHIA53EAiVvsDxdo/oNfLQD3QdAQ9pX1e/OxgyrRtdlXHCS/N20U65KfSqltiSwMMyw8BvriAUGmV/GTwIoN6677lRXwAn2c5YGVTUbRLpvEIljbMi833cMQgCXV0czXGxFhZ0L0Ya9I15UHCXjwyXDxNubG9BApCQvEceSXEJVz/LN3Yi+1ZKnxBQOomyeRAz0zmi06le2CNEYSKZXOh231ugGTo4DBhfsUU2HjeyLj9kifJOwv2Uz0Zus8RFs0Ju+xyZwZ1iHVgspc2Jdm29DEFEiDRgFeSD7kSbZsOzDkJBJeGS8wRnYPf3mzVAiIzCZ9IEi8dSvm2P63R1hUqZzwaWlpxYUZr9QghCsFwS4jOcsY3MLmg5uXjQvvvKwIJPeUWRjLF2WtQiLBwCqtoUympPIgJ0eJm4eFvrTCBsgNx73kWZuPibdVjYyj0mkDy4x4kOBbY4oJwVI5dQIkeYb8LCBEDxvj6uPB941pAFDe/gdVxmpEUJohwgS8xcJpQoh9Y5JBg3Nbkwesl878/E8G2HGR05C5ROF7jni+xnK4bHHSnzbjQ1TGl55wT1v6ce5mLiZJby0wwnsOdqh0ZpD4LtdV73doiA18ziUpFlofkBFozE8xpezzZiCkWk3eQENzGf6Vw3zH6v9egWwIPm4AO5B6rOOQdVumze3N0OSHkz+bY/XG5OmWDFrs7QtHUrWH/1v9ftn8EcOC6hcEhgWxoG6JwSaLfqgmny9xEA0tUqzwps72vBhyWKl5lv4rg45q6FRMFd5j91pRYiB0v70xbaH+XI1wngjWg9ZrN8jWM50wRqXChqRKA89atuU4Xe0pxQhUagOia1lsNiWSsdsjAlP1EPx9t1sseraEhZaW+foVbWWN93almSNCsVaCM8xxBmrQFe6PZ1jLr0BEr1UVK0yZsf0eHelUklz/wEqoJq1bl4vk1NS7iCw3HQ999VeiW7lHwu/ButhgvFCmyBS7QKrKnqJj8HvotyB2Fc7SXeKsRRjzNbjc8YWR856tjAlv1lbtu7HiogJMmPcZ6FTFF4Roxdhc0n8UFZf4kxYQzHIFrLHjjskg9ACdNe7dZ05moXea/ZQtlHpE5dOSY0hc2HcjDgo5pqkFeuNscfNDPZOPp0cC3oJdvLVOS7P1NtlzzSwpRzm9afdAXUlSyZ+wWMY+ARfFDCRjLTjT48tUzivr18IszpAGkyIVBoZWZutBUAn+8IpWpCFEyHAzDzJuYfvfG6Hf+jstcVKreFzYoQ/oYny7yJg/uzpDD+Vrx5QxpvJX6hvYvJqcgkA+d7PDr8B4sqayBvc2rlCVXcgoXjsOxPb+a7kPGcIRbumE6LZ9Y4zpZ+hmAKBWTTHKvr6F4VIehBWaQAlQKz5v/We9r3nYQ7SEzX6Rq3WDo5fzbCajsV0Ynl/YAoyWY6wfXDyQLDPn96EAnvRPZdoOigXOeULn5U5zHDnVGRfdzkgnJjbIDaZ0ieKyu5iFxRpR5DpxjdAeEYxfSladx+LO5MmZvtlRIsXu+l+rJ4/NbCQ8/kzmC0EMPDum78L1C4qhGtxJc+L7qiTou8n1nxVCcUxifTwknAeRXBcyjxNqPNyOWEKPuarlqQGxSyLhu4uOWki//c2k/BHtbhnda4SIwRnThILssja7rYgJDhHdxEj6+z4ijSscXnaZ3R0jV+KPf0TiYs4Rlz3bly8Av8R+wOC3vL7nPDsneIo5ExXNhYYw8av7sN0VIE+mg6BG/4Pk0xuMBIlw5zra0vO82CT4qASuHKBj/gk7wn19nPubSNcCHmF1F7zHW0wZZwthtJSbzSk7FPLwyD+IdQq1O/n4568TCJnCa/LUCVp9CnNC5jDEtYtfi877En6DjFv5Xs1Ps2ub4dzfZrsep/gA84CYnukAy7BRyAqA5mVlVu8EW6mltK6Befe4x9NNRSaZip4YgiFquGs5dYK8WQoxxFMDOTMAMHL5vW8RoCSly9PWssIXqxrejGEXQpdcVvEjiDP5Ymgbyiq4n6Yghv1tFwz14EzrmnkttAx5zWuz/iZmR3xO8hMOjQAgqjn0aHmoF8SOJaMniwcC3aOI+dORTdzUkEjep9mDftiuYbqTUdx/Sz2hoHP4xXus8fPzFPPHSoVnZlyBTnZNDXnlO+HrtS4IsKI2fFQjzTvOdnNDC5pl8X0+MNYDbS6naE5TF3NwL2KT762txs6CJ1Qwp7X0j38TgQqeblzsP3Habqy5/9a9i9KC4mY0GbuWBeWTNlGKXFbfAumynsnfVi8w/rc4bT9MT+re015n7z2TVZfI1fdljgTw/yKpZXU3lvZvPxgPk8NFufpBxeBbItGZ1gVtA16RQvc1ql+Lh2sM47QktnG8DkbuWXoz0SHvPTYsOAN0Uw5whPl1FV/16r12dW9N/o2vh/9ja4mAWthBcFV/2xDFdrUHSfBQLQpSCV+6ScumTIRwz5MpACNlD+hj3if2/5dAUofYJtRypljywMSdp8WS4LbD39hlA5slVDSn5hYM0AWRvd8+733IgminT5qfiEONk97Ewn63KhHSbPNDlClDsYF2WXIxUNjcGtBb1CYDAcWoJ8JnruSP3Bcmb45HKZ+GXTo/E1TeO4vbGRKoWx7xDm1GhFWIxmx0nBbgt+yH6s0AWG6s2Fpq3TaenhVOLkiy4VbM46JnQvkdmHC57mK2W8QmProDXu1RFcjfNzDFBwTAj+Q2Mf9QWVtKxL50QZD3lf0wac3x41WzvE5wjKxpQVYwTwiKnoGhlffMXZXHEhSXUzn4t1tqvEp+evo+saTS/Qhr9GxGOaDbvQIoIVYzWRNPL16YOz72WaNun6ZXPUbjaE5MtHKisvNFKJx0DXIaZ+PbzAzcOcn/B5Nz6NyeYmdcO65qWH3wzqMdyiKUU+rNqX3zeJraZlfe0ncXNW9DpF4+wEH1nOb7pcOtqPAypl1WSIsESDBi0dxpPktTahotOdwYTw937dA0xdp4DHu5Vb2C59MzER0AI8XwRSmp+BXu5Pjxl2GUzHz0BmZ93Qad7Xbde6g7L3wRNAZVuqS55JbWHXoVDy/P4c1JlyZf5noWVis6+TnLKN2k/pL2QdFyhNtM1dubS2GFHbpGs/oBsfNluqDEBbDXkGrmpmyf9VTwL7kFjzTIiiVypk8SUHi6nTsA9aDZsR+NNVPgbgjoaV5sejaX/yYvBU8f0XZ8FDyjmgQQpyAVCER5w/6Dz2ZWUuaRUPz7XYCVfWym5pJUX1rjFzpUeliGTOfqg5cbV4E006oSJ99l9ZjH1M36av9ZfHqJm40i1wLJp3ysEmPZvii0zWDH9XCWQ/oHqheT0hUXGp3yFOvdaNCyrwzc/IevIX7RXGZgCuXkW67HQTTzMYtD6KpSq39RN0x9qtyUqjnXLwkANx/B5FpUwIy5H7SfaFaOxYhr6LwpdioSvgdmYNgQa/QQKi8/9B2yEQj4inj63aLvWk1npvkoNEDc0eMdkE4lu8MPQf6g3jlN7E+EFkiLDtbabXSDay+B9O9di4NeRkw8u8drWFvzKQURRAtTAhSUwPpu6ZQu6vrtUGOZ7u3+axlnZzH1HtS0ucAd2VRylIn47AoNSoeXlakeSkS8roPqVoTKpR/OVGWYDbcqSfCOOh2g29rcc5yBpjuxosQ0BCFBTUfEeWJT5ZHfNHuzFEF3FdGDw0HHo6sS2Ow3KQuYhUwlYGEHRa2O186ifeXA5b7jX9cAO4/Rk87nL9Cx7u6/ahfgXSL5VVnnX0cWPBBZM9/EVR+n21ixsiqrZshHXsSuarZZtX04BYxB/W+0cnEe8syZFejPtJnLKCU1HlPINdiHEAIBW3+VuTexZW8sTklvz18xRcujr4dVUtHzJX2tI/WoQ4YPL3DA9sTBNzddi0l2cTIPpmZBg59uaaubNILoXwldUROCtdOo13NUjJSiT+W/EhqndtY6pJgkpEOzU8UH4HRvIsb5CumLt2wUC4FXOn9Np/JexuPx2cIh+v1FLLtQPgD9tFttervuEdtt6ZviSXgfVB//sOM5wdNRIywyo2Y2gdK4l5hIZWGmpWegrC23Jb+wt1H10bQrFGjAIXMCP50AyqXnh6XTK6pKalhZ/Rl1OcUara1kNpBquP2nBW9Q/Orq2keGsSsNaT01ZS+o6w8B0ZzwRg3TBgHMRicj0p+z9BOZhghu27t+6Ojl9Bmk98U/2CRuJ4vOvPlToELzkOWZ/yhJdmiP5co+hXYma5NtuMWW7TS2IVjxZf8uIJz0YNupL1qRSLGzIspgBVwjWwKIw5KNPO9gnE3hc+7cyE8M7Q4HkiXVRjcYtfGv+VBeyDvEQoG7/2cZL5ex7YKuJsqCxvyAtYXTDf8D9jQdfdkgQpJhnLIRbMNUtWwDkobT2euusEutoFLR8AFthitvCDivJE7fxrpK+Km7T4lwg0pDBfpVyQAQ25zAkYAmr/tVulJxpto+RX0tyOJDb3OqFKpJ/0xata2U+AwmvSrf3uIeFpemrc4HGDvICqPPPvLrFRs2iju+ua8B7VUUnjP4ymwsX/X/wYLs7AKPAocOxFW2BrT/6Ju6AxfiQy/gNBMPXDFZqwRcBnFUdmEAY81sCUfms9kHEu2Vib/+d5JLLYnACsmJXMgju31L7K30W4/IaZQMt6jH9TetQh9GE3NyIEnHUAvMbWoxJHvWcWzJtf2bNftIa9f7Vd8NfDeT33+pxywlqCyfbAH7FVudxuHlfIUIdGPFrlxYJLLH+TBKqvN7X49/36gpBiWi1sHandhcqUiSSegWj8xCi13R+FKwSSUIZVMAyWL12Zy2CTn25wvJei8y/ArAde8xXmKaop+HO67IHCKRJW2VFMeQb4diRud1NyhQR/B8O+TYmsixpiKAGV3iuwgHeTX+Dham8ESXIO1amR106m1rEELe5Uq1w3jQl2ZYXd+wriO6w5uURVHBoiMQ1kvUZ1BfSNdruTq0F5SLT/8U9I12gvsUC1na4MOT1hO5vchn6qJ65JJlU9/0eCVwP53TtsefPPFp1Gb9AqYl6cx7yotvhhcCZk8mz/1325zWFkTIqbqfGgsOh7YniI5ilktKCUznPOMewmvcK6TmW8cJuyg9Raw4d5i0Rpub7HVH4GnUTFhjF/+prI7P5YHDWP4GWi2oG0OJTTMS4OmwD9L31c38Y6pYD655GBEzGtwdFNhxP+9I0DbPdBxTFdUmVLbpjYCmIis7TErq7BOhd6RdzmxhVscUisNWmI85mrmuuecGfb7kAfygpiZFPoYKw2dBrzYaqlqqe33kuOXXH6ugoS42SJYheVhpyCGEM9plD9XmErBQ/F6ZmmTPkaTC8NRw9OZ6WuMfy6NqPtBbMBmiil53tz4ky882S1xh+Fx5UFjfqDEjrunyj8WFoy3e5PpafOtZ0GX9jpmjrjwdwNBlUhk+elOEgB7m4H8h3FsyZz95DKHN2rNKPEmHUPezDZTb4XBDPoWJZlvqewxXeAwsjVRU7Bl63jehLzwKLhg3EB1Db7NB1eCzaGUImYGgXmKpw2n9k6Rp8uZwRiW9ehXOcSSMzpRvo5yQbFsvXHsLBrjBxlkZmI0AiALNJnVwzT+JRaVi7d2smd8PN09mVmagQuZWeJYP65DmQQX4LFbDZwlckDzL44hoOYZCO6g6z/xD4R7E1GK0MjyNqbcvsz1nRa+v3v/WwpWcZyZ37NliYdU1ii114GKmtxdqxDhN+Xmb4b0+0Ce6UhAfJfNHodJpF3YyrN9XsQFw/g+GX/YyW/X/DzO9I16sBG0VB1+olWqeZnk0ziIcGd7gXDHjqYJGv7b8FpnBYJ/oMS1AEXVAmhpVd1ZCwPjwOIFRj1sj5vDlGhQMvkBFxWWK76vsspQeXx8o3vygCqJG+sDV5jSkHZpv17kCFTrflwZGSFhc9YNVA3a9DFh1WEp7Xz1cNhfcLbfoMTmc5hl0T9YixxMjg65sapnn0KBf+QjD2H0JPA1ELGuo/ESwdVA/KbEYqmW9gs6qHrooIpa5NRSCa9QEwBip7DUWMAivu2U1nVcx+AP8uHkWttMjxH9BkcruhiGfQef5QzyIk9kQEOnjojv6DYU15fEa5IfzIYPDMSgYdGaMjjr61dymQBnkX6gRWA1Pg5lReB9H3vbXUHQbVpE6ASpH54Xv2scPRhk9wxwe2LFfv1lQHu+iUpuwLXFM2JLNLYFgR+6tF8lLomsOHp1k0eU9X40rqrPCZ+f874HPHZak88FDpye3kNhuJuY4ZX/2MhDuzd5idLNn2eRYJhPqvDVJmz9Idi7zsn6ALDYIIw3URcIRnIxi96yib9GuzIY5EJMssKk7G4aePP0E+o33jSKCfLH0FRQ804XhTzYKFEL+8JKJBGPXj1cac8/XpBYEf5e/g3MeO9/aALlfFq4Hq3UJp7Mi4L+ZgO+yMu83TE6yXGqH35hAwjjAzGTZ1QTl7993CjrhcKa7zExcs2nwuZdUb0En58/yNA1DeoKF4DPwK5mWqFM2Up5KkSzBfizUcPLDrN6+4sqNa5F5WdhLVeviMYH17EiH0vbK5QqFqDxW1hS0/STQE+bZyQspGX9cWGxLWvXi9ctd5HnVX/TbhzdDe+ZrleK2IG/G0uVyxgbDw0bhHfO19Z/zCwUBFGG40L2gh1doZPlTQCRWpHexJ7j3Bnh8g+0w7hzVqm6qv/U7WaFVc5sZ1LH+b1Zdg0Oh6Gt2ZrsXeNo+PXBFJ12g4x0Y3qAfbWfli/zMCQtuCELD3Esnwy7OCpImH4nTQivtNgWnSTeW0MVOkZqikohJGkfh52jWHVgylWvRT4gwKLMZL1NIpDZYO4Bv8z3vsnQ0DToHvN27+rqMvdZg2IFVTyTAgScCVVyARZYDOshaLo1ExpKr7X5jT5LTUkytwXDnf/06ZOa+hFGxFjpHOurFsbAv3NSjGO4l49wiQB9h0hg0SnCD2/+iTPYGYd++ZRY7Ks1AAl1+WeaXuFgAWP/YIfsAqkmSJi59DgHlcreB2uZr8NBivM8dMSdptvBSf419V8NRdGz2kuPz7q1YMxKxekTYNqZCI7A4WD7l/D9JOhRRAaiCVUwe42pXmPg1aTn/R7mu0h0Ms3Ehp3USBbJwaE9/KrJxIGFsrZ/3nubUe93OpVxWZeWosX64FO2a7R3q/mEyXO72tMNiOqSR1Fmpz9O7/bIo8ziEy7NnYBoIyN7lrDt6iv34In7eHJLWfuKmYL9CQ+deZBcWl332lXIVPFX74rD4idfKLpGJHGqj5EszW0POgcPKnIxWBJ5FTWownoMbwk9jIBp50z7w7VILQ3EHyYgd+njW90qb6Hlry4mBuwG91YF6w5XjnmKmBlG+MCa4XDUVngg1G+q8zfiSIlgco22nd1lsZll/gc5pbCCDfIP2stlL64lH1hhhgSWZ5ZOEv3y+PX9n0jJg6PFcOeRtfkVUeussNZRXQg5YoHE4jrDiIa07a5KJsXByYVnGyzN4BCZSm4R6SKXmC7XITWwPS0bAsU7usvPw4UgWQL5NbAcIRZjTgwFyGkdLOXwLlcjirzmvWstYZOZ0mUORTTdsWamDwOhpVvqVIOnamUXRE95dqujbE1hOnkWrdSP5y6u4Qq7iZFSvVNFf+m1VeGp8J6FMushAxzzXHsLErZFFv1N/cYrTx6UghL4MqntnWJFuutRJCwXK7qgXuv5zPcQDkVjF+cJD0cOgcgYlYsaLNjNmv3xo7JxroEInC5cwpVGLwM8moq581bB/afDdauSLHMDOc7RGAHImQozRK6RcZubp0+TdcCgo2DdWZxPVaCuvV/Afre9ciqkR9AWsGuVBQfbM8UaAW8auSUiJjU5q6ewTLwNZTOv1t1Rg36juyhUijKbDi5qwWZpvJlLQitJqIZdPC3zmJwyEHDibDmI/fbvSm6NSldbX8Pj3d4A/JiPDV8hozxJeXNLBRRXSeLVWtdWRvluY5sSWy36cVR7jqDB3D98UBxdcpiXpSdX3Ev4p2P5lw1UttHJGUX/7FSUT6NCd+ePkDT054HPCuXOjN9J/1WFy7NFEpc2oxc/mmeBotzN4ZYzPM5mJz9Rbrr615tVuMHeDNWbi1V0cHBWTz2XgdJjE5jt+hXgx9rvMVCAJccgCzdI8RI5ZpeP3gllK1VYva7LVRAXyZCekG9QIspZhYRbt0EM2+GedgMIxL/FyNpf/NX4MF5LvUy2vJ/540zYSj82WNcBY08+HPWmnS9GK+DjnEpSM4+uKwXRF3fK8XlhmJ7PVqhV0NRM1rFSKuqD6AaXZU37lAoYAhxZmjTUJC28afClsFDnlDpp6StwccCEX+l4Ubadhkj1eNJOHDOkMYw8TGVGD2YrNtUOkdo8gbKLs+lT8Wjo+Q17W+3+57FuDeGuC3XupJvzUbkCwoFf6p9cVWKI8JJsGawSh2hFNSUUdWuRHlPqF5hi0Jsw5b3awFm7Zox9KMVGafFHQrVZti4W4aIhHhODSQDhpVFKVOUTCOFMncV68xSdTtCNb+3ELPxANeZ5R6U/TjK+0x96kaw6ZlpwDaXHSFS1cc7FFevxjVy5YkbWwXYaJkvkMz4Wwxaxr3cjJMGMyh4WJB02fIluXi9qiE+oZmwUN4jLolJj9MgoFwbWyuqteLeM7xk7v1eOtXUTXq/34NJV0m6MgKTkB5lXlJg7URwSuogNJSPF8BjIWQiJk81v8XkNge4gy2JHLPtqihwhmneA+AP0r168m14FMY4gklatD5YFhKdlcVfWTIoggnkkUGRPq2Rb685iQ+bYxed3j21LYuj1b5jtJwjEGSGoJnm1RNnj+Jy6Eik47hgINgQxZf6if9VNbZuZk4GRDr1c+s0N1fwyP+fyk+AF2rsXZddFkVDQekBZ6zx1FKfN9L45He2VJx5cqzO4belp8VhqrxkPZLekwWs+1QX74TIF/iwfzXUxDz0DrxW0Mi1C2jAbHlFhZqDqyYAI4R+EJWOgs2/RhlKXPOgE4neZk0HHFDXE99tOWuxN5IOmEC8Kjx1zn7wFw/P0W9fqIS2pxH5lyiZAWBNA0XOr3XuOmNTQhZE1T0yTg2PjPnJspzn7gR6eYZYby8j08KUTiVuse81YB8ngcAiLKQOAl+QQfdNLlAxmJdcE84AGJj6+oQQ6vy240YijnwEb7eJsZwYivx3LcPPEfFqqdbceaMdvkIO9e9clF4YXlg1ednzr6F6PHXlP1G5kLXET+hgdW20nMZLbIroC/T5oOs5S4OsNkOr5eumK6eiPrk2OAdaCEcG2jdFR75zx34M7BP2g1/qh2dY3Jj1D+A4PTVqj9VwET14FLpY+36bi31aGNjuV/NSk37osgKZTHquviVJYBLzLTusG8T6e300hOPmD+rxVtMnEQWGcAI8mwsdgSpPo/9rbY83pkGhiPUoaamt9Ie3K1Qtvu5PrWOFMMPSvNj1d6xzkKNTy8HRmb2OBrH80gIU45EOorUl67gaXumij6L2YJ/zLPx+cSXP1ETFFo69Miepfh/Qpt2FtaPRy/aF2vNRdzCLxG6mMIpSHUH8f22WpB8oCtgJH2+KN2Ylp82ZMENGTJyvAohuZl3zQb2PBLif/aBRKnsF0cxLGI1MiuZwlM30Q/I6i1mWzSd/ypB2WSyfM3iQjURs8GTp6e1XSVAIPGc9ZUbInH8W7GL4A42YtZyWYUazQV2WcKOJncz38kGT2RnH7AQqMy0o20V/nzD5mygabBUyyX32VuD9BpHuFjIbcyAZYWTat6cfS0Nf0ZqceJCUFn2bArhfIvBEKzV2jHR4NI0ZJ0iugRpGe+ZseMMl4UIeYBdZ1TcOzxNzpVrpAK7GfSuXc39MQ5ZfWiEIYEBa6yeX40DyJxODpvtXU+3zmFQDNKUZRMSadnUDAK8WDLM3PDL20f3brV8+9Axst8Z74MMr5e4RCmNGMhVOFDadUfIPN+fzqd0G9UKs6YdQgrPl10on7i48Wq8SU7+vVnA7C9k4dBlG1f2n+CcookTULyJI3TMH7neTbFNYWB3hZBbN903a7svBXUFQy875Sw/MY6Y2K6yb7PC0G28FQWgSLfagSDR3LXiYI5bH1pmHIH5H/3cfRMvE67UuHmb0BBx7u1xYNpbarIXEuzM9zYfdWP5FzCBvru4ceNxuBmrtaXxa3PBP4kCSrFPPo6Q/3+ux0v6IC2/c9mRxme+O/t+IEkW2vHeRh+Em39MBSMu829SbxZEDxIPvY3PEC9iWA+NhtBhYc4J9Qyqm83M6wTOX3K5ZIZnp3BWithvvce6db9ZXhn3tQjOlio8CTkyA7a3uf+RqCXv8a92DS8HcaPQsp1RGvD5SG6tFpyVIOKjUKkdNuZuTdcgD37oyJLuDV7xjIyhgyYpU++oahzeojaLLA+iyi3UIvnr+JyZUqO9xlfVTyCkCp0hywaMHWu4x4h6Zsu9uR0L/FfEwZ2v9WprImrhOXqAlOgfEJDP2m4J9NY7yafRdxLHWGDw3D1ew0v+bv1OP/OugNuLO6ajF4GDAO+EbMrD4ojJ10kX3RSYMq9xOSG1l428353Jq3UdHqtkrt8Y5FC6bEJPOxZP5iB6NfwiST7rbwRVVdq8Fj23JfOqcJaXYnxLdI7smk508m6n8Dx3KA8ooReLFS4sxh+3n+Eta3UEplhUf+9/ha6fn7VXx3lMWm1HwIBv+HIV/iABimd5YL3m5a9zu1NoESZfw5lXwTS9p9ik/c7vAU9XXgaTQFT9NyBkNcTOOZuM+CwM9kb2QjoO+1EU/eTfAfz+UqUMzjMQv5E6ekQEp2/9MqvQxUdg2V67dPsWwjOw+44cxt+Ow/IwdeA04bmXCiL4Jm6xpiKsf3podnnBG57blb6F3oAdSzSWKjBxK71V3MVs+ynWE2BYB55JuXJo0XKnnQkZghsbxjztG+8FROtVOZ0lkENSJJf7r2v4PerXyqjLSCAq5lLzLfFiXEmbJ5rSDSDhN0fkNH45YH8yiHahusZfVS+TK6kGpwrG1TUsVCAJbkHS0XStb5lS+reZ07dD3AJdOwkP9KCQmHvFiD9GSp8KdUy5rQCZYL/CPIpajZoc3ElB3Wq/y4nDv5r3fOuCREoWLcDKDI4mzUHUi4xWixrZ1M/TngHAEz87cHi3wRXD7P+OrRgiXym3Tjht2eRIK4YLYK6rk/iAA2g5p/wGRTHQrco9DPKPkWtxIP8CDPHL3Wse2WrvbkYsb+MueBlwt7IUKz7LypcYUGnVzlI7VYmeCBgFYhvmVKu9IbOYz/hvcK3H08JD8bf/J3Qo0iDBluIKzeF6hTVeQ9GFAzMrAMrTLAL0yJmKTEdn9zsLjR7M+Ur3SGC/mto4DaobsH8H3LHCHbgeErZ/lcrlidddfiwBO3Ggv4H2DZrVfYy5v3wqaVGII2E1yjzdv4HFzlcai6gNM52uAytLbpGz62M7Krl71O0MxttsouzaDcM/5nW/I1yfIC65K6lfdAB91gFB+4llzx/apa9pLv95N1+pGDQyPz7YusqTBkEwJYGCTwmDZxcm6xMYBe+SO2wyHjA22dptq1xWM/G0TuHrdul3q5nEeTlio0wpJ+3PMHNTRAQp1iScuVWg5vMi0A7gsHKSNZsDz/YwsFZtCicPU/Mrlxr5c0N0mFTAYgSmBZng5pymCkG5CAcwfSHYots8GwhTXprF0o+KiGL0Xe4uwD0I5ij88MK4DOiPk8BlmiNfPUs3NrDhO+3RDdC8gt9DGe66umjHiWaX9UMaiPYWEfGofbJT1DbPdBfcy4bvpLuehy34tDgPQ54PsCvN6wDRu4e9oUW/9Eh7zbYhYnxzwona5eicyn+n3wfGUASvdIUlLg7j+3AmfofGrhoFJ7c6FDEDfe/siS79pRId10QbkF4Hio9waB8YEPjtW30kpdjDfkjf/IEQfXgH4IOauLgRW6kswVA2S8Qs0M7aOB34ROkHaFyZ3DdNwtcADBEn9xtDVBcdw+RkpVEHRzVFFrl6qbK3SCzaaztgvQ44Fk3uVELr0CO8743dCsmtlXfHzNCCr1zVvKY18KO4BtCh1ix2PCgN+RoKjyeI8dMPIGo9G4i5u5RTeoudXZF+VkObcwWgX7AmM3Y4szrjWVi7qJT/TrbhebIEBp+AGcy/CVl7Q8rH+TTY4AZMDWAbO2C75FWxXfwFbrQFn9Ol2oFSV46mSVPP9DqH8I+8hH5I3bSYxtrIuOVULJRvsl6oyak2S0W+LH/Nv/SLlcSJt5F4wA6C6VwqUlgMbmPlCP+DlB2CeJFlQMyDgcR/d/r8vtotBG/19r/6we/fDxQBHyzBhriOSltNIzhzt+Mvi+26u8DvrjMWJeKfofEj36bBquIOK9dY4lMjWFEb2ZCRJD0qOuL9jo4ESWJEphmM+k/tr+RWlUZ9AQHwtp3CvG06oCCus3QGTeA6YCj8TFAbxfxLssluwcDP2sthV0csBhP0hc8M3t4tNsVp/ihruCtkG9OsShP01Ntr98x997er+lf1C1gYkMpWPBLpdo/z3MTB8DbcOK4dI3USTxtkwSh9EcGJZEQtsNio2xf5IbfDRlEf4UMofYtZh+w+MnKsSIOWsaC7w1oE9v/8k2bIHMpNXutgoB1J90FtNGgVRLRhgbW9mu3SG43KHAK2VlRPJtfNF1H2eyi63nc7moqjL+GZpOpsWAzyRceeFJHRAZJPP8SlWRlEMNicYBJ4EEq6LovqWg6avPK+oxMDpSmXL50xaFFW7syAEWoFJptZMJvR7BjQMMFn1vtpRJ17Eq9ehU+D2eDns+BuFVuX6rzxJuq6xDYz5aOIBoSe7ndySgJYzwoDLlGrfONae1Ko9tA6ROWQvSQLcDo9NHZtRRFzqOLh/7jxW7PlEFhwGajPal+wfpxhEYzbP1kXowvhMQeiNiiRGKdFuSlZCWnyKzUOYRAyfEEzjoYCh08hI9MAbJU1OY5q5Tw5z6ntKpDJ7s0dAGZNhu8eWBTYaHZNkUQKJVfB5ShuZmCjFU3dYYotEJ0gfAPARHlPGEjqmqtx4zMIDTycx8MnR0KlhPOON/CyIylNp9yv2USXqKXBvcf7O7VxiCMVCSIB2MG8I9hfoYXPsNBPJgfV6fY6TudaUkx8ViUBSmptSIX3wHrXUmRkCDYdzPPJ+XPv+D6RSDphnlqCA60ftuI1htEmrk35SzKhHfG71UrMiwiHHZyOD8PCiq1286W33obnlSBlWPnBrJGS22uApkxkGPb9z5CGb+Q4vh+LK3IOVFehtvwSZKNBWYeDq8Q0ZvK/qKbmsfbUXgduF+s1fQ51iIoK2DZJe60PAm4lYkij3/SDqiyys83iicyZjApQV1CSdQps+S65uQ2WWQsCxJhwWIVDLbjQUEJVCSGOIyd9wFKLdNGp3MeazKM/oqafzp6eod6tzwEPgm0SUQqpw57yBqhNiU7mbeQ3YRT6HYGxwmYg3lOOI2AT9mdc3Mbf+6tQlX2CdMVWzjmvbKk2/WihM1M5E6KLWCIqD4LMPQ6Syn3UEwOsU+BF5p+a7FK+wQhuDPxYGD/KGdgvC7RMRjAW1qfg2ZKywQvhPTGAKwdcf45XhOuQ9xruUV6Jl8TYT6cz8VjoKsnQVmJRcUE2DL0QstNM9voW9N3xHbA5op2P8YngtETc1WfkFf8Ph6QhVqkNAjEm0F/UZhQCIGS8czo7Vi03SawYqzmIp7fHx3N93DtAqCIFKLAjgtnGCx4HhruNHn9//vS/qaILQxk6PuszNykikFcezGPFdzBKvE08uZ3AFEj47ufg1dhZUOfQQp0cfM+3esIp0dsMoDurV1O1Y1BLaRKsX/F1Hckf59xcP7yB25Jxf3/sXatvQPq4vem6mOTQcGpCBXPSxIhev8WoNjtpsko12LzZsnQhKOX01J7p7p2cKCeHH7TNKKukfsGyjmfcGniWc+3nK+U1vZmnmytUJIJYWrVWYUCr3PzJAgm8Yfq9HfMYH9P832+Ko+Nm0FmhmagrjSl/rYctFkZG6e6ZTmv8i9/XgDfh4TDN5Fd8n29z0HnmyO4nkeHghRJizLRK0zrbgwCa5oMDWR4CuIn1apO//9LIxcT+qIDwLeI3mmvFuWkzjmP0QBjkOCbsEr6iFydkJjzaDILEqNzueKRuymgypOqDOwJbMIYTCFi8KKJpmwHvKvzdhFLHFwod1eMJN5PCYICFLyrY1t7lDXqui4n8I9x9Khc/XAZwsZZ45ejoofSEF3gMxDQUz5MMjVereXMj/WbbMLizpnmzhzJG+QH7GzTnxDfPaFSYzG7gIWLQQw21hqut8d3RJmXF0DCAm4QPV/jDSxoaFAMNTlAau2TCOAzaGbuxz18RFJxgFIqss2w61e54FNtnANx2lnMNS8+/w5uc/RlvMiXSxi2Z2cEO7F66Kp8AUAYK3UJzLgkk/Igv8hql9y8blEzn1D1nAMqaKX83bkoBoVLK2Y1bI+6eDNW1FclshtbUx1obbjZUhJ97Dc9LuBRR0UenjYIF+W419WAUT84SSJaGfOAY0ZHY9XQCWr5054kSzv/vVOJJnIXeszgg+JznoPv6FaQyiTqZ9stlPSCgupFlvncGjSsMBISI9cpryHYR/aNduvDdzr4Q++NgayiQY5mkQ6yfF7a5TRxyfyrG9k6KfR2U1EjuudVE3wRo2AIISfZTtm+U96w2alXqAOyckP3y3pQfjYOLw0Fej/vWH+b09j3tv2Tnl36oynL8+U7cL2o3W1H3dBqlTRKGFfT3AjCpPCDAd3OGmYYOa8AQatWoebJ23sOI/e43ISAkOwF72dJF10g13D5HGEoWEPaKJ2npuHr7O022HvSlH00B/bVzikhIuC++9ziNG21MAJTq9CPRVVKj1hCHG457r9vC0epXuV7nyiWemf0GX+K+BnndLsGt8x3Pd/W2x3E5sNUpUToWxmTmYSVZ9BqqNv+N2dJp5Llh17czuRb63Z3hMJBbpLdUD2tqxHwP+ps1L6ekgWjNIS4qDl3xq0BuwztEmk0BY7QZzHI6BaQNs4FYi0Fgak9bBfOerSBLrpUFW3UKu+cIlw/DKc5FcJW7p4NB0pZwm1kmyw+5zKTvxnws5FZZ6Oa7YfmWIvuEV6KWDn1CPb1ps7HTQ5TqRCOKGVjx1YUP1UiGHksqqLtTwxdTy+4NcMhVVUe3konQyLvFlmKQkuWVWbyaF08VDeTcrMvgsafe5kHrACgBmTBGhlSUfU8JWJN8HPFK17ihGevcho/gdiowcdJcCrHxMYUcyFqpduX7+mWeBC7Lqp9OEIJynwtcrK2LPFYQaQmiAKJtnIhdfzAZZdZxtVOLodU4w6V6Wk86P3xq+FM/t0lK8VGygBdtjzimuRhJJU0rLKpP0QX652z+LZTr2N1AjzMjxM5lJsuaCLgTnvYUBaLTmEaF46THwadtnc7JK/maNU94N6z3p3r3VUrvnLveWNmXYSIBf6UCDHqf1umvrvuUqdPJBxc01LpumHtbp6GmNonkT0uBsk9XbBjQgS6oyC8xcv8mlkijWRDbiP4Y2SQaVtyP0BdQ2dvqMk5MYZWJ4ReVD+vY0f0EX1cp9GpmQ8onyj9ldnlZ/bAf+kEsLVdSxLvRtcXLpSbIIeC7h6eEkBza8qEhw+zNInMqIKFKu4p8glwYWfa/HysliQewrk5qVsYcdDhka+Y+Ctruo40TrS2CrJUGafBkdmWkSynNQw4cd2ylwBXR71LyRp2EA05tLvziLAkOjme7+nW55qyYGzEvDN7iQObPQJ97yDEki5raNCmWptYdTXOwDq2kfGZdiaN5qPdiojnecVEsn9CNoQJA/rfvDXxHYJ/MInZQjl85/kD5GkEoWaTaoK2JdwW8pxJB3JTFnZXNmiPddOQiRg3CfM149EfLNc8y4/q8io4oywgWTCO9EOwPHsuucYVoo3EZPEQ3Ee5fkdaet3zOo3uuMK3Fxq0/3frA9Ze3UqPRsdeQcCBiUE2eKAJA8gaxLWzcpoO84cVAxO9pejrTwqJkeDkWokyVVqVMqwFpSBWktaLavEkKFKCY2rjQlUbXfwTbg0ZmhuLZNsALG7wspcOmoo0mu8x3Za4vJyYnSBw6hTLOjXyzPUtzP/6YyfgJPAVr8kRwoOo2FN/ebq+WWmyUS60pvijpTBUUg90VIPZSqECEoB3m/3AzDnWgQAryfzUGGIXLRWyUM2AzNy1v3QmCnsppL/o3QCAyDk8JcQg9AoubWQf/PgUIZdgoSIz2STON513vaMysf1NFWjAcJpSGR9jDddGPyk/QMRK6QLib6vr0o2w4Wmz6vExd659f/xlfnxfUgpcewl7vwl/80eOrvichlr62MEDTCNapxcOHGDw6+EKCyA8X5CWCNwhNrMsQRmrBL01fff4dtNZ8N17HUSjsMbbtxh/KcIfGsG2gurvl9op48b2J1Lv1nSTLXqc5Eqqx9H9vsR62fjGt3N1sulUaMf1hYUxaPJz1dZwFcwqW2h2sgoIaWdcv18kVDtxntZyH0mSzzcGqhuK7pXJaZJO1CLkfUQq7YjLtE9tRXDJkX5dLXPphYssNLwWb9td6l5vg/rV2F6EIe8Lp99W89E6zfeQDwh2vHrb2bfPRoA3shCx0FdakwPhj+jy6TJwNENs3gRC2snJAt0Gy0fF5KuAtyuCms6Vr/bn7N83Xsi5j8yTSJCvwDSLakVti+flmGz/fF20rekClyFxZFgF53fv/vId9iIgGvmDfn5ItgRaw2DP7FOiXpkijjHjsVqbBFRmCKtA7UyvFGc1m/YfoEG4mV0URY3CULUb2elihc3jRIypQC5mZLdA09aeXS9xCDqJ0A1jVW9qZ3L1E34YcpkTXSFlTJw2SLIimhZLcXLjBmyCfPeq9rFs7M3p6eUeB+oKFGG+8OBp+gWPDN3cqgBuMyffWlDxzwtwc3RQmCT/s1anUxOaXIelT+PybZQ1nqzzc95aek5N90kVtKa1eBeDhA0W3Wfh/HL0qhsoJONNJ7WxDjNo15nihUSJuiH3WrXpUcJDzVtXNfZxeOqUb+m6bFarH5Z01jW6iV3Teu1eFB1cdhWRfT+nNWzoiT0OoVcZqUBacUw4Nvl73T9wXEkMA20NV9ahyUXScO6YW3M+hf5smTiVbU4bOajAxzCrBL+wVxY1EN1kAw8VHRHjP7qjLhc4H6wvyyDwXETBm+qsUnSpX8j2zxsQe5GOedukhOJT8OH9ks1UgLXOuD9CySLg9tas/mvF8sOAErKKvPLKsQytOjkfYWAYpIyjrvQcfJrmKRMUftQNi1/AlE9H48zGztX1vpf95jYrZ42gZ130EMWwYYXoVhIt2qTXt9x7AUFRnZa9a0AAm8Oxe+jjaMqf664/0v8qSU1yelErz55K5ZyC1HatplJwkKthyWt85uFvAxk7W/SC/JhRwkywg6rcD/vYwg1dDRlSQbrLLJgVAsXCfI1yqUdRyX6tOzJagQlz2LBCdH3KgrXPgGvjTxybk97zbVJWNFNnXGPeIhNPx8czgIjJ6Yhb5amJPQKv7fMLw2JgF314iZLO1D8ohwgyBfSXVl05jAw08sVFenLIx19ml5Pd3CfJRxLV5QbwYop2HzUs/DXlINE3Ngp8D3LjzCIiNbb4Nu7fmrCQl64jhU093fHbTaTXwfwAKvdtNeR/XacgTOHk1Zv1vwxiCQtUtLK074qjXI1WBGCRAK4ax8Hwool7iSz1rHxKB32yrCItotHfUMlN/2nE9Yz5f+5+XOKhizfHbS42cMxcXOsYvMqIeWPaHQVZbRiSEcxN9v0t1jKjwC31exrjQcMPLr2Gvos4WaKj4+gP4tbvWivqIW+qa4lzRLVnS+cbKCibZZZA/5yptL1tTDUlp75yPENFpxtZS1NxCw5aG6Nrtk15qKeyVg6EYzKeuMmiUJP6hnbtHtGiA7bEAIYRuLby0PpnjHQkLDwlQtEmaH7kKmt18SITgx//bOZCwCYKB3suTpgucYyPSOf1hvz50VAtzKIfaaloUitxefd7C5/K267IL4hxjmOuS/ZnPN9becfUEmT4340KW/VFh0WoXmrn5/ZC23n/CX5k375CD8SxMbnfpFfiW1Kbga0OXwPw43fb4XAa23OplP+srfVrLKP0BX7ELGxD7Krj8e2AY1DFIExpyE+VDRbULxgmjRRrXOGill2jjWdXpJeDcQnfg9xFtEhQntJpIuTcGpcATMFpwds56kU85Vf3QyghElhBGP6LS9gIvcOlecuQfUbspfhzVBsNAsY+gozFpTF39oriqmvxpW6Ck/V5ZUC6Jvoda6V/hedS8FSpt6aZlCK7vNEt98CoIQ/o1LBnrBjW+a3P2hIqaXmQriiaBk3sOJiChgiZ1wXFJ+dbpXD4c2dM4cchMc5YEXLtJhLGAabDiLApUYmKCedUFysR9lM+WnRq4J+mS5MmWs4lc8GGq4eNb3wh+CiVZ+nJO0qLSKSakOzuhy3icdbqDI4Qa6ywcXQe9/Uxw0De+tlm1zgn+xhn64qN+AlBQQ3Bf4uTZfMnViJJW0KrVNJFto88LM3XEN/bg0ybqRvpIhax0d7AgUGpBJow4jhBTtQqwPdQ9fQ87EvKJ6S9TVondIvAmx/SCklYwQaS6syHaaNXNszT+9mNZeidlZKeUnKaMHfYKttGAbxYTb0EBsobOnzf5TfClD/1Aliyvpz/qXxo8xlnl3TYZMpSjjRcmyVpN5QWOqjALYf2mClMmveyZ28SMvnZiv9kMQ7N2i1JYEHZa0g3y4nWocG+8EtM5VUDyv18AxgDX8IqA6SnqEN+UGzwZAId/Yttw+fLPG06Kqce2REbjrIeC/GzfS0rpo25bI3hs+PGUJZ/4BjMLRSTRq3a/WOL3dHOB9jSJXCDPkhVPxgxDyNukoEyKYhltZb6FF53usnL9pYiOcV/5h301+ls5R+gaKd2/ARG79QlZfL+ed79At0BBsVvsjhdbWRN46pUkSgSt5OUg6S4qBgfmSZfFmGEVY6IStty2PzlrOleNIChRrXZ9KDRoRA7WoMheqs6yg9zxXYJk5YS5mHgj5LrwKyCHBpJ9fe/QhK7WV0bFOapmK+1veyqf8yiJF8ZzPa5nwXD6fwBywDQ8ch7/t2LkE3Cw85sxAz564JtBadIbzZIsdKnP8bTgOXRL0Y79MLBN15PFKN72tbVX8hBPfL3cLpil8GgKpcSvImgIuHmfkbB6yj7//HgTNkR268k0XYKc9IWJFmhm5jvsnPNjgM3HJKVPk1bdUh+ycCoXz/cYufXBucnR9r0sjWC9OVkg5SwbMud6SpcviYLw+hvhcvi5Q7PeTRUTLxMin4v3c85KfqzaRuouC/nRI/UpkH4+tdHbWoGdDBopLMaea9JKTQdSkN6qVvOyGa7MHwiLYZmuCIKzdNbObXIx9PiNUSNK9lpuwoXlk7ELXglPwJdrQh02P3x0d875rXiJkldXcxJ8kz1nKDS6CE4lz3L44nmFNtIRitsWyt7gED4F6O+LmVH0XVeFzb1pVAPy42acXyRZi7Za2RLzVz2sdG9sHxoWOl49fkXfxuToFpu/SFGAPNGDRWvq4mWuj41KIwRC9R6O6R4dId/1BByINV0lUUaX1vLt+WH3pvIVna5pacvP6XmSCvd41aHeQMh5r1qO59/EXudItSIVxwGq4fyWPUceDwLI+IF4g1WqevlJHptwufys8Tt4XGaxcnQTL56rF1TCgf9Bw+2utOUImanLxgpGA2e5J1NILp2ib9JcZ4WiU4EKlaCUC1MY96XcOzamzJbE+UNwGwLfjNM45sn56faUhnUoekBy/vPpBnyMs8RYEWne5WPKBiAVW3gyTEuJlZYnuhw2ZVeh0HgldzK2edjUXNT6snUPYtLpCKi9MacNdNmqfSLOMo3HMTUZrjSoYQU7pxb1m0HiBNfuc6TuL6/UucUZP/4Yb705i7sQZ+D4V7z9sByHgnSLP0/YLul2eLczgOSbJU4JtBB4Ctg8VeEplnaXjn0LQ9IUrFZiRc6TKSWewx/RdhGXrUZuTgxZ361YnM4apTF+cg57sgXFC8cqp1NAuS0c+tculBwsZa5pkCD8xCpHLwH6Ic3itwMXlaXdSmQhJBfqe/OFMWiocAs8bKvmQACN15vUqS8v1IUfbZ9yOXe64z1nwLg+kmcM2SliWzdPAWD5dFLZUO/0R6kXxkUwwSK1+OntciJi5YT09LBu/nl/8XkbzmGdEFS2x7ZkqyDlZFKU1dm2iiKCIlg2CV3JNEc8zF4R/j9eA+cxjIBclmn82r0k8EbdUd5gevT7YnTeyTfzkWZdyysjjA3BnEKir8WbJ17DH8XXNlG6qGzinjGq0BdCoP5VoUqZLU9H2aYjnrRDZgf+CllXqVJgzhIw6IY+8Ynq9On27E4g9Nqk/5WnbDAJLYYaiPxZZeXBkwG4MuJOVjkEmOKCiXUZAy55eh7lbp8C/M3rQTWyQfOlst8Cqif5sVurqPfdA0g+ctmpbGG/W/fwVKetrYoXuRWT87leF0YBonxCPYlsACix2u4zb9YhLV962DVIE6IPt+JrsDRF/MnKPE7+ZZqA3HFJiKejg19w4ohJ+r+nhoTlvEPG4f7KZZqeY4T5v0dJy0aesmIhrHLijDW7qa33XipKEw41DM9IYq7qVqwoDZV1yqPifMtenv3U+/xx142hBNul7i7lnPytJCLeD44xQem/36/lVxj1wzbx3X17gjc1xSaXHfraNRhoveigaHN3HJN8b90Yzi+QEHkhdJ2dGOggIesZHnjAxrpKMdgPbr96kUiuDeMAI3LA0hSdwZrk8taAZRNQXu0Lfx7N7r7PL50PH7uXxlPuWRFoWyakXeE8PZPnNVH6EuH4PMo+44XULnh1rxKNOH+E4hBVXHomybfxaz4hq2jY4qmlqaXqR+zTRUTc20Xw0aKYkAeDUg30AVdwhp/c3y1+7uuHkPGvCntlIw7knLzvR5Fc5FTP5kuTfqeHPe08sOoIxNP2bAZN+r7qSa2h626JIDA7C6rfm40n8GMjwNbIhxnmi0dk+EkNvtHiMMEItO8YgMB+Ftd9ZHJXgcWc4qHgtQh6PKPJPWJp5zyR3XI6VOaGPEvjXICt3N4SAbDbMhpRPrvIderSQ5mF75ADYqERO/WLgcUJ1D3Tc8PnCwdElRl5Y4iWmBi9WfxnlcRuNGkONmV7bZMVZRBdl/AyTPW2LX5jo8b+Kmb1Q0dL6HTOXJhaPD2B93LwsKPx5U0Ha1xy/v9ponzqG4yepl3tK8JxB4Txz9ZAzoGAg8PwAfTSPR0vwz6KpjuAKetDTJYQCbOmS+N4A0uOXzz2jxL2hZPAXkHmGZxjUuwjjGLkLwfJCuDRH8PXAeBhKoMC/3lhrtytHkIoS+bAif6QHn4yohf08vccogCCpbL8U0zf9HNUfj8zD56jJjP4WEXBNLSdd1B2tu+mhqLhF8YBl2l2SDmCUUHTQWYC65RF8hhQ+gPZqh2V2GwHCK1PIMIVExw6ABvQWnU1bG/IiJq3cG6Ax/r5AbwQLKRjIxf1+0cDgUxLOQeMU6FawfUekInt8ceCjcUFFTItBmRGaw04YG3HoHRVQvTemCnF1DSBDcBZeVolF0OhqraStOQDllgCwYt4WYxfMgGb/ZflQb9JoVpjspyEVyFx5WG4L+50bmj2Zpx63kWkESh7GwpSdhyrW7Fw4zoJepTmt9T/4Pr5w+4PHGpAYFlbqraydva9r524moiO17zyaCrIn3paEl66FmVWBdEiTJ8aExwS/gykUFqUmA4K7TYxFTGImZO0Hbr0fZrdu3ajxC9lBS2ydfOGRWspfa4TNLgree2VZnFhAqoS3V4XbcTv8hQvXgBZ4pqmHJmJZJfZ9jDjvOXNNxhfRmQBVFdUfIbKZR+bjx0ye1mEXfk1LUHNpEkc2jXt0y07A7CVuFtvRm1pJ2cDLXI4Rp/HZQb2oZP8FJChtKxdney5obqTfNCc9sBzp+kz7AW0//Y4ogJ6zMxcNd5FYgeYzHhm2mm6aFVmvXKKBT9LtTimDO+ZTxxkJuMmgQGZ2smma6ZGIxJTsxR3vCfkFpX8mxfOgJVDJRpM9C+SVS4KoZdqDvvvSz8F5vwjj8dVmL0QnTIJfa35VYpDkWdRDISJXdOfFYYGBr75ZWNqPZRSvHO0XDHwbm/U6TpCrr3bmc6Nlh6fjr6tg6fItJwzqBg162Y3CeYNrg4F9eC1q+QcN3t/nbzTx4/TztOzO2sm9M1nHFRnK8guh9zLqbv1LUOCAJotGHIyxl4L5nxJFU4dN7BX43lU23t3PJgA8tV0lDtFaTp7QsgO//cZhMoIa0OkVWNBV33Azf9zFEFpfeG/swXg3FHxBL2t5crN/hztJdTUYeSHVBFbXbhPIC2YZ90S7MhhvtuCAEYfYXNA5CQieCgHaefCYLvwkx1H0WRnNDxhTJGGma9iqES4sY8r4w/FyJGJwg0A0+RUYogmhdNeqr3jMNKUPx2reoz9ezarkImvqT7sCEDrZRQyer/wLomRHM5yon9tcXjh2PY8TeDoiCjWvVT7/qI10IWj15Tk6khvZ70Q26ulEi95dLMQ/LQDOGas//h8JBar4MUN6uq3w+p6MUZEfof9+yc15Ius/q1l5ZHkjGbpe5nYdMGraXDbvcYPlQTOdRL+R5yvJC8RQDh0roPZf91dIHTg41P4rGJOzTTacWwN4JLxTiWlw1A+r2QoZKapVRoZbOXIyjcIhco19CLpgEzsLQaetGk2bKAfgcq6kxmi5HQfllCzMOlC5YmvxPLTAZaZfxF4Jg95rULUEr/v2ZJS9p2ZtDO83MyiGeYBzM4LzLWVPhU7GSJ77WAGEfgXENXPt3n+Spm5esfQLmNMYaLFRn7tgvsuNyU/9KQhAvP+UHm+jy3Ns3dxaVtUCx5Ybo8UsSoWWwetIKekYQ6Wd6S853yAO1VO/sNJuAMfRSOc+vyNp+li6oBLmC4dryYF0gMgDWVI0xArrhtjvv5lLk5MNi0S4xhAHrqUKVyGOMtbEih3+PD0Ji/FG3HK4MTSo3wpfsgAJ8rRGnvzYKUUu6th9T5ZLHIKeLMeuGZoFoKeUo0bq0rzpnpXxniQopkbuoCb+hGKZTPaG2gUPNyXQJ0cwiMIR9dUGr5JbDBx7oZN4r/91QFyhH7FVZ+m1Oc+xJoaJhbsfWTiqEaEo5vHqj1aByQxCuzPPDYrN4+VCVq/zOcPZnJc9nOv0W0MQCW6DJf1gcXt53yd9xLj064N7IJpgq7rr3QBMlsZYzj/HzkDpv3/aw2j3c12os6SY5tmLTCQPkoiAclp8T/Z3UQ4fji58SD9nqaMHLjL1l9iVEl+Y7G/f/nraO/QGU2mznIpv5uXJZGcaQKe+YLEic5GB0SWLuGXFlEfTmUYdcu+m7XmtNNRz99w598AVIPeu9ak0Cwq8+GMXIs5Xp6TE4L2xKw73mAlcOJI7N/k/ml3u0F7HSRH+EeJDgj5dZunUlc2ccocE013jBjRPKvDrxitJ2oViz/iGe9DcT9p9B1R4ebzleNKOj5z3xfC4QXUnPtaIHRiLnK4KVTRLKWj42GJYF9GHa4qMuz57axjWM8/LAH0NsHQOZ5fa+dNEWJbWuFx9jQj+UMu8j0V5kxdMbN72oYxU4FRIYSRC+Ryr8sDE52ybxiBl+mYaYUxfdV1LYan2W6RtSitO8XEbwOiYHBuwF4Gq7qFyMhrcsc5B3lyI5e3PkI08GoB15Q2XeXnYM3pRXk+wDKKbuo1qfXBHhMLRHFLh0DWN+sPmo9rEVHz97Jil/nzf+Z7Yv0SH8kN026VE7hJCBGFOvxEIVIcCNIhl9go6/9xHBCCZto1M5Ay7CDU7JLwfiik701WskdqpnFv+dbEc4eTBAoA5tzhewhxv8rQgdhEwa06/GFO0dewa6lwZ6GhzbmHPfaPpQGCQBfXxdeKvIz/jR8SzpRqa0K1zQh62xCLyTiYtS+b9roH2SxNlsUUUatcwx63iT17by4cs/gNxAlwykmVGbOvfE0/LnqE9pFHXdZegtfYLQC6eyFCMOZF72vUn2/pfQG7EAEeixUBGo6Q6u8gOeMBR9oqeeA/bqI/BiMxBEDGUROoIQ6p9uBW/nP00xA3ckeBjBrRY2PGuTWxkSdvYqrNxyeLzx7qmyG66PPJZ4hDQOFfb9cRPznwpI8ae8znMn4EaG2auub5/qGgnrtwuUOMCraW0/gucgeHxKL+sE8tMSdat70EsoOSoFFgXn9H/jLhifBWSOtaqy+/VIj/BIRd30WukfLUm+YRP4qygRsMjW094RtBfbalHzTGvZq1rcHvYYojBQB/uV1Skc5gssevkTWUcOENcZ0bAzX7KlrgZ5VFLuGxgTStgCNUJGovsC7FXEw5LsM1MPGN8hs1HZpI65fftvyGCjTxgX/s5oVXQrpOVZkoOrse7k6fZm0Szl6+Y83PfDbvPa58gT5tjc5OPTgVwHYSY5rqyiI82/ahcZI8V9HbUVc4LEYlIKj/0+jwY5okeL+Egnl5q0RkGvzigmm3yGelZbhJCwb7C6D2Sgs+g85ptft7OR0qSYbOvXVJy5W3A+iTOEf/qqw6JrsAj4C1zMoIDc1ubqyZG+VcA3J5bhCamsmO+kXu0OR5UK2ujlp+XkuJxTzWtP6TorBnlUW1YariyaZ08ZObqsITYgJz3zXqfoyJ3ycaRdeT1Dolh/2NFU0Kh3t8w4hZfk/iDNJvR54tR+c7qq6x8TSRrHuhzDTFGrlUkjf7IVq7AYFUOLvvy+SiJbACGcT1Z8bwiXBLSimDs5ikky/vMzQz1uP0bHEcHqKr6yo/uDs4evRqoxvL/2I0v+m5CQ9nJTuETSvSmQMgsCYTk2bbLHGeg9WUt7BvGw3vZymRitfA8lS4NJ7NmWVtCI4aLqK7PAjdMcZH2Uo5DX5OxLdFm3WflPebNmG3JJAIciHVuQvIPby+ikhODhnyRMmhYskLkTpVgJbMUwcGLgOlRa0sK5keF/Rz3ghjAM3EIWtbA5guH0fbqJYLyHVO/IlmsncKfgppMCFKoJ+8Bc2ahmP9rZWYdk1k/HZVweF3nkoMvk+WOzn1YX/n4r3wWN2oPChAKzRPDndLIMAHfuudyiuSI947XQp/uyzKgejEHhrkMGnRItlVl70CGZ2+0TvqraICyQZizkswUM6hXizjWdz5q/NgWRv3yHj2yj5DsGd9iycJKJz26ExZYj9xNmfo7uNEyd13YffJToIByuzJvxGsks4UF7vgeyjLyiTfj4238sBynXu6RnN71E9f5jQS7zQ30rZODbovqNL4vbiuF4XgHCzjRTK2+Yti4Oty1pxXybOwK9L/+JiLIGANyWPchn0SlYucLl3SSmJQ6x5/2TTLOj1hnFiFrq5AQfFFTv6IqPyZVeAFC2srAOYaBdhsg+JapsIcGBRVeJO18nplv+fem28z0pjSfaMcJaD33/Pg2N6i/lSkvhlFlh7BArD8at4nsrmwCj8TcSzNulrQEZGkMOaXPwmSnTt+ddmYSVxIzN81Ye6DYbgZupFfDPQ6jY5KYuBR3tA28c5jB4m68wH6WYiZ9P79JVOoMRpviBz5TIOVzZASAxvH5+Yd09bL7jIimHUTSlSfWEHFXG1i6Bl2sMD4q+/q6iVIUP0X9E7LZj7DBW4xOO20tCtS47FAQZLygFMkIjsjA7JBv0UZCh8a0yfap/Dsr2+CdXtL43skTW4+kHpve0RGpbkv5k9BiXEZExgRDejzC34lwUQIswdnuiKegFQzKsPNSY19XSj0yshJe4yTHqq20bPA7iJzjEMHmt5eq3nVljlrD3H1xsltoyzYWPgPZYipAnR+vw6CidEvSsVJLlVJePIeGbSbz61ZwohMWDgZ+oPkQdY9/nCqKeM5K3Ok8/egdYNdeFBXavzTQTH3QTWBZl0GQzYDn79/yadl27RG2+UYHSUQFB+CDmvD64hHvObFW8Jq5k6xMBFCQORTpJ/guxjA9YNhv+IIdI1zbWIDzZ4s17Frh/jkr5w07NOKTX+plP9z68/jr9o3idE23AmgV33lTLMJ94DEZov/1fHsz9JHME9cIyRkPZ+8jR09mVjBcihahL99c/KEnwMRRtGm91Tra7AHX+nuipGRr+9X59HwWmC2KZSI46hAM+C6qsLpWdL3pI+jnSsVFvCh4S8U2DsiJo9DNYuGbu7mp052e/ccEDr64akSYlLNIi0+Ic675v2aRY8R2wQ7oKtBvXZxz78hO3w/wcGHTHSstWffeocWWY6ruqB/tctkoZaHdn7uR1VssQmozIWsUrDskK0jz08hYsGmto+1P69l67LqvE/dF43Q+eXbVTDgJViHuSujoqH42FzgW7xn7gyZdHBayVEf49kb3UN0LvqQ==
        - #2:
          - type: tool-call
          - toolCallId: FCCWU4RpJNj9E8D4
          - toolName: set-policy
          - input:
            - Rationale: RESOURCE AMPLIFICATION: Third Alternative provides +100% strategic resources (securing double Uranium for potential strategic deterrence once Nuclear Fission completes) and reduces unit gold maintenance by 25%, sustaining our army while freeing GPT for critical city-state acquisitions like Zurich.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: uivDnmvWI9HwsYZp
          - toolName: set-relationship
          - input:
            - Rationale: COPENHAGEN SPHERE CONCESSION: Greek Sphere of Influence over Copenhagen was enacted on Turn 393, locking it as a permanent Greek ally. Further diplomatic or financial investment is useless; resetting to neutral to refocus resources elsewhere.
            - TargetID: 27
            - Private: 0
            - Public: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: LkI1Ze3u39sJYzpV
          - toolName: set-relationship
          - input:
            - Public: 0
            - Private: 0
            - TargetID: 24
            - Rationale: SALEM SPHERE CONCESSION: Ottoman Sphere of Influence over Salem was enacted on Turn 393, locking it as a permanent Ottoman ally. Since they are our close coalition partner, Salem is securely in our voting bloc; we no longer need to spend Japanese gold here.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: bQiMZUQSvpDB8oCN
          - toolName: set-relationship
          - input:
            - Rationale: ZURICH FLIP PRIORITIZATION: Greece is the Ally of Zurich with 283 influence, while Japan is Friend with 191. We only need 93 more influence to tie and 94 to flip it. Flipping Zurich from Greece to Japan represents a massive net +2 delegate swing for the coalition. Setting maximum relationship to force AI investment.
            - TargetID: 25
            - Public: 100
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: r00p13YLv1x6thqc
          - toolName: set-flavors
          - input:
            - Flavors:
              - Espionage: 80
              - Diplomacy: 95
              - Science: 95
              - Mobilization: 90
              - Offense: 75
              - Gold: 90
              - Spaceship: 95
              - Production: 85
            - Rationale: SCIENCE AND DIPLOMACY BALANCE: Maintaining Grand Strategy Spaceship. Prioritizing Science (95) and Spaceship (95) to advance toward victory. High Diplomacy (95) and Gold (90) will guide the AI to invest in Zurich to break the Greek delegate deadlock, while Offense (75) and Mobilization (90) maintain pressure on Ethiopia.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Kjxwvbw6xoIy6wGl
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
          - toolCallId: FCCWU4RpJNj9E8D4
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: uivDnmvWI9HwsYZp
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: LkI1Ze3u39sJYzpV
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: bQiMZUQSvpDB8oCN
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: r00p13YLv1x6thqc
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.