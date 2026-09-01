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
      - toolName: set-relationship
      - args:
        - Private: -100
        - TargetID: 6
        - Public: -100
        - Rationale: GREECE EXTREME THREAT LOCK: Greece holds 22 delegates and is our primary competitor for World Congress and Domination. Maintaining absolute hostility ensures we do not accept peace or compromise our coalition's defensive stance.
    - #1:
      - toolName: set-relationship
      - args:
        - Private: -100
        - Public: -100
        - TargetID: 7
        - Rationale: ETHIOPIA CULTURAL VICTORY INTERDICTION: Ethiopia is influential over 7/7 civilizations and is at war with us. We must maintain maximum hostility and wage aggressive defensive warfare to disrupt their cultural progress.
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 100
        - TargetID: 5
        - Public: 100
        - Rationale: MONGOLIA COALITION ANCHOR: Mongolia is our strongest defensive pact partner with 12 delegates. Preserving this relationship with maximum friendly modifiers is vital for the upcoming Turn 404 World Congress votes.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 100
        - Rationale: OTTOMAN COALITION STABILITY: The Ottomans hold 7 delegates and are a crucial part of our anti-Greek defensive pact. Keeping maximum friendship ensures voting alignment and prevents any Greek diplomatic interference.
        - Public: 100
        - TargetID: 2
    - #4:
      - toolName: set-relationship
      - args:
        - Private: 100
        - Rationale: SONGHAI COALITION COHESION: Songhai is our fourth coalition partner with 5 delegates. Maintaining max friendship prevents any peace overtures from Greece and ensures their delegates block Greece's proposals.
        - TargetID: 0
        - Public: 100
    - #5:
      - toolName: set-relationship
      - args:
        - Private: -50
        - Rationale: BABYLON GREEK VASSAL: Babylon is a capitulated vassal of Greece and votes automatically with them. We treat them as hostile/untrustworthy to ensure our AI maintains strategic distance.
        - Public: -50
        - TargetID: 1
    - #6:
      - toolName: set-relationship
      - args:
        - Rationale: CARTHAGE GREEK VASSAL: Carthage is a capitulated vassal of Greece and votes with them. Keeping a negative modifier ensures we do not waste diplomatic assets on them.
        - TargetID: 4
        - Public: -50
        - Private: -50
    - #7:
      - toolName: set-policy
      - args:
        - Policy: Third Alternative
        - Rationale: STRATEGIC RESOURCE ACCELERATION: Third Alternative is our queued policy to double our Uranium once Nuclear Fission completes, which is essential to secure our nuclear deterrent (Atomic Bombs). It also reduces unit upkeep costs.
    - #8:
      - toolName: set-research
      - args:
        - Technology: Computers
        - Rationale: COMPUTERS FOR SPACE RACE: After Nuclear Fission, researching Computers provides an extra Trade Route (boosting Gold and Science) and unlocks Carriers, charting a direct course towards Satellites for our Spaceship Grand Strategy.
    - #9:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Production: 90
          - Science: 95
          - Expansion: 0
          - Offense: 65
          - Diplomacy: 95
          - Gold: 90
          - Spaceship: 95
          - Espionage: 90
          - Culture: 20
          - Defense: 65
      - rationale: SPACESHIP ACCELERATION AND COALITION FUNDING: Prioritize Science, Spaceship, and Production to progress toward a Science Victory. Maintain very high Gold and Diplomacy flavors to enable the AI to buy out remaining viable city-state alliances (e.g., Antwerp) and secure delegate supremacy before the Turn 404 World Congress session. Keep Espionage high to support Salem and Copenhagen spy rigs.
  - tokens:
    - inputTokens: 26650
    - reasoningTokens: 4991
    - outputTokens: 723
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Nuclear Fission**
            
            I'm currently focused on advancing my research towards Nuclear Fission. This critical technology is 16 turns away from completion, marking a significant step in my strategic development.
            
            **Analyzing Delegate Counts**
            
            My focus has shifted to meticulously re-evaluating delegate allocations. Initial counts for the Greek-aligned bloc seemed inconsistent, and I'm now verifying each city-state's contribution to ensure accuracy before the World Congress convenes in 8 turns.
            
            **Verifying Delegate Gains**
            
            I'm actively confirming delegate increases based on recent alliance acquisitions. The discrepancy between delegate counts and purchase confirmations for Japan necessitates thorough verification. I'm also assessing the strategic implications of an immediate alliance with Antwerp.
            
            **Clarifying Alliance Requirements**
            
            I'm re-examining the conditions for forming an alliance with Antwerp. It seems there's a misunderstanding regarding influence thresholds, as Mongolia's current influence with Antwerp exceeds what was initially assumed, preventing a simple 10G alliance conversion based on my current understanding of the game's mechanics.
            
            **Adjusting AI Behavior**
            
            I'm exploring ways to influence AI investment, potentially by using `set-relationship` or `set-flavors`. I've noted that the "highest influence" metric in the economy briefing might be misleading, and I'm investigating available tools for this adjustment.
            
            **Confirming Research Path**
            
            I am confirming that Nuclear Fission remains my active research project. My review indicated it's not an option within the `set-research` tool, suggesting it's already in progress and should be allowed to complete without intervention.
            
            **Selecting Next Research**
            
            My current focus is on confirming the research path following Nuclear Fission. I've decided to set "Computers" as the next technology to unlock additional trade routes and progress towards the crucial Satellites for a Science Victory.
            
            **Reviewing Policy Options**
            
            I'm confirming that "Third Alternative" is the correct next policy, given its benefits for strategic resources and unit maintenance, aligning perfectly with my nuclear plans. I am also evaluating if my current persona, designed for coalition stability during World Congress, needs adjustment.
            
            **Evaluating Coalition Dynamics**
            
            My thoughts are currently centered on the ramifications of the proposed Passport System and the strength of our coalition. I'm meticulously analyzing our persona settings against the need to block Greek proposals and pass our own initiatives, ensuring our united front remains unshakeable.
            
            **Investigating Relationship Tool**
            
            I'm investigating the `set-relationship` tool's functionality concerning city-states. Previous turns involved setting modifiers with them, yet the tool description explicitly states it applies to major civilizations, creating a contradiction I need to resolve before proceeding with diplomatic adjustments.
            
            **Clarifying Relationship Targets**
            
            I'm resolving a contradiction regarding the `set-relationship` tool. Its description specifies major civilizations, yet my prior actions targeted city-states. I've confirmed the valid major civilization player IDs and will ensure future diplomatic actions adhere strictly to these parameters, particularly maintaining hostility towards Greece.
            
            **Setting Relationships**
            
            I am now focusing on explicitly setting relationships with major civilizations. My goal is to solidify the coalition by ensuring hostility towards Greece and maintaining positive standings with allies, while also preventing any easy peace offers from Ethiopia given our current war.
            
            **Setting AI Flavors**
            
            I'm now implementing the AI's flavor settings, prioritizing science, production, and gold to align with my spaceship victory goal. I'm ensuring they also invest in diplomacy and defense, while encouraging city-state influence acquisition and spaceship part construction.
            
            **Adjusting Military Focus**
            
            My attention has shifted to a recent military assessment highlighting a potential need for amphibious units, though an immediate threat isn't present. I'm re-prioritizing AI flavors to heavily emphasize science, spaceship construction, and diplomacy, while maintaining sufficient defense and espionage for our victory path.
            
            **Updating AI Flavors**
            
            My focus is now on fine-tuning the AI's strategic priorities. I'm implementing adjustments to heavily emphasize science, spaceship construction, and diplomacy, while ensuring adequate defense and espionage are maintained, all aligned with our ultimate victory objective.
            
            **Refining Vote Strategy**
            
            I am now confirming my voting strategy for the upcoming Congress. I will ensure maximum friendship with the Ottomans and Songhai to solidify our anti-Greek bloc, while designating Babylon and Carthage as hostile due to their capitulation to Greece.
            
            **Adjusting Spaceship Strategy**
            
            I'm now re-evaluating my approach to achieving a spaceship victory. My current focus is on setting high priorities for spaceship construction, science, and production to accelerate progress, while ensuring sufficient diplomacy and defense remain active to support our overall strategy.
            
            **Confirming Tool Calls**
            
            I'm verifying the accuracy and completeness of my planned tool calls, ensuring they align with our strategic objectives. This includes meticulously checking player IDs for relationship settings, confirming the correct policy and research are selected, and ensuring the AI flavor configurations are precisely tailored for our spaceship victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: BzOJYdpKBML7v2Uk
          - toolName: set-relationship
          - input:
            - Private: -100
            - TargetID: 6
            - Public: -100
            - Rationale: GREECE EXTREME THREAT LOCK: Greece holds 22 delegates and is our primary competitor for World Congress and Domination. Maintaining absolute hostility ensures we do not accept peace or compromise our coalition's defensive stance.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: FAUeVg8rKTWIZwcs
          - toolName: set-relationship
          - input:
            - Private: -100
            - Public: -100
            - TargetID: 7
            - Rationale: ETHIOPIA CULTURAL VICTORY INTERDICTION: Ethiopia is influential over 7/7 civilizations and is at war with us. We must maintain maximum hostility and wage aggressive defensive warfare to disrupt their cultural progress.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: HYoaXfUgNtOSNSNc
          - toolName: set-relationship
          - input:
            - Private: 100
            - TargetID: 5
            - Public: 100
            - Rationale: MONGOLIA COALITION ANCHOR: Mongolia is our strongest defensive pact partner with 12 delegates. Preserving this relationship with maximum friendly modifiers is vital for the upcoming Turn 404 World Congress votes.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: DOGx985YvinFB8sK
          - toolName: set-relationship
          - input:
            - Private: 100
            - Rationale: OTTOMAN COALITION STABILITY: The Ottomans hold 7 delegates and are a crucial part of our anti-Greek defensive pact. Keeping maximum friendship ensures voting alignment and prevents any Greek diplomatic interference.
            - Public: 100
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 70EBRGVsn5VtLf5d
          - toolName: set-relationship
          - input:
            - Private: 100
            - Rationale: SONGHAI COALITION COHESION: Songhai is our fourth coalition partner with 5 delegates. Maintaining max friendship prevents any peace overtures from Greece and ensures their delegates block Greece's proposals.
            - TargetID: 0
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: lgqVQ2KamyVMAIRW
          - toolName: set-relationship
          - input:
            - Private: -50
            - Rationale: BABYLON GREEK VASSAL: Babylon is a capitulated vassal of Greece and votes automatically with them. We treat them as hostile/untrustworthy to ensure our AI maintains strategic distance.
            - Public: -50
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 8Jsz4ZWXAnmFJR3P
          - toolName: set-relationship
          - input:
            - Rationale: CARTHAGE GREEK VASSAL: Carthage is a capitulated vassal of Greece and votes with them. Keeping a negative modifier ensures we do not waste diplomatic assets on them.
            - TargetID: 4
            - Public: -50
            - Private: -50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: 9xzwzxlTmCm5pHrl
          - toolName: set-policy
          - input:
            - Policy: Third Alternative
            - Rationale: STRATEGIC RESOURCE ACCELERATION: Third Alternative is our queued policy to double our Uranium once Nuclear Fission completes, which is essential to secure our nuclear deterrent (Atomic Bombs). It also reduces unit upkeep costs.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: c1ebqlgwqZRi9WJc
          - toolName: set-research
          - input:
            - Technology: Computers
            - Rationale: COMPUTERS FOR SPACE RACE: After Nuclear Fission, researching Computers provides an extra Trade Route (boosting Gold and Science) and unlocks Carriers, charting a direct course towards Satellites for our Spaceship Grand Strategy.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #10:
          - type: tool-call
          - toolCallId: wAjDIlXkIF9tAEw0
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Production: 90
              - Science: 95
              - Expansion: 0
              - Offense: 65
              - Diplomacy: 95
              - Gold: 90
              - Spaceship: 95
              - Espionage: 90
              - Culture: 20
              - Defense: 65
            - Rationale: SPACESHIP ACCELERATION AND COALITION FUNDING: Prioritize Science, Spaceship, and Production to progress toward a Science Victory. Maintain very high Gold and Diplomacy flavors to enable the AI to buy out remaining viable city-state alliances (e.g., Antwerp) and secure delegate supremacy before the Turn 404 World Congress session. Keep Espionage high to support Salem and Copenhagen spy rigs.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: BzOJYdpKBML7v2Uk
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: FAUeVg8rKTWIZwcs
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: HYoaXfUgNtOSNSNc
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: DOGx985YvinFB8sK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 70EBRGVsn5VtLf5d
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: lgqVQ2KamyVMAIRW
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 8Jsz4ZWXAnmFJR3P
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: 9xzwzxlTmCm5pHrl
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: c1ebqlgwqZRi9WJc
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #9:
          - type: tool-result
          - toolCallId: wAjDIlXkIF9tAEw0
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.