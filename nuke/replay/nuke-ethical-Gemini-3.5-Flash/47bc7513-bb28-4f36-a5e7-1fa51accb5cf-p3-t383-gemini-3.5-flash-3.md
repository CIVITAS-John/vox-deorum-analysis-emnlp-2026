- row:
  - game_id: 47bc7513-bb28-4f36-a5e7-1fa51accb5cf
  - player_id: 3
  - turn: 383
  - player_type: Kimi-K2.5-Briefed
  - prev_use_nuke: 95.0
  - after_use_nuke: 100.0
  - prev_nuke: 100.0
  - after_nuke: 100.0
  - rationale: CRITICAL WORKER REALLOCATION: Reduced Infrastructure from 100 to 20 to free the 7 Builders currently tied to railroad projects. Military briefing confirmed all workers occupied on railroads while 6 aluminum tiles remain unimproved despite TileImprovement 100. Aluminum crisis (-5/turn, 26 turns remaining) threatens Yamato production and bomber upgrades. Maintained TileImprovement 100 and Production 100 to prioritize aluminum mine construction once workers freed. Nuclear Fission completes in 6 turns - need Advanced Ballistics next for Nuclear Missile and Yamato. UseNuke increased to 100 to enable atomic strikes on Cusco immediately upon availability. AirCarrier 100 ensures carriers for Yamato deployment. Conquest remains correct grand strategy - Cusco is final capital for domination victory.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 100
  - replay_use_nuke: 95
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
      - Advanced Ballistics: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities. Also allows you to build the Guided Missile, an inexpensive single-use Unit that can damage enemy Units, and the SS Booster, one of the Spaceship parts necessary to win a Science Victory.
        Completing it would unlock: Lasers, Stealth
      - Refrigeration: Allows Work Boats to construct an Offshore Platform, and increases Trade Route maximum travel distance.
        Completing it would unlock: Electronics, Computers
      
      ## Policies
      - Co-Prosperity Sphere (Level 3 Tenet of Ideology Autocracy): Co-Prosperity Sphere: Bullying City-States no longer reduces Influence, revokes Quests, or cancels Pledges of Protection. Doing so decreases the Influence of all other Civs with the bullied City-State by 10%, and increases your Influence by 10%.
      - Cult of Personality (Level 3 Tenet of Ideology Autocracy): Cult of Personality: +50% Tourism to civilizations fighting a common enemy. 50% of your highest Warscore counts as a Tourism Modifier with all Civilizations. Free Great Person of your choice.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Exploitation (Continuing Imperialism Branch):
        - * +2 Food and +1 Production from Farms, Camps, and Plantations.
        - * +1 Production and Science from Coasts, Lakes, and Oceans.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Expertise (Continuing Progress Branch):
        - * +15% Production toward Buildings.
        - * Cities earn +10 Culture when they construct Buildings, scaling with Era.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Fealty (New Branch):
        - Fealty enhances your ability to defend and leverage your Majority Religion.
        - Adopting Fealty grants:
        - * Can purchase Monasteries with Faith (+3 Food, +3 Science, +2 Faith).
        - * -25% Faith costs for purchasing Buildings, Missionaries, and Inquisitors.
        - Each Fealty policy unlocked grants:
        - * +1 Faith and Strength in every City.
        - Adopting all Policies in Fealty grants:
        - * Unlocks building the Red Fort.
        - * Your Tourism modifier for Shared Religion is 50% stronger.
        - * Cities that follow your Majority Religion generate +3 Production, Gold, Science, and Culture.
        - * Allows for the purchase of Great Artists with Faith starting in the Industrial Era.
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
        - MinorCivCompetitiveness: 8
        - Boldness: 9
        - WarBias: 8
        - HostileBias: 7
        - WarmongerHate: 1
        - NeutralBias: 7
        - FriendlyBias: 10
        - GuardedBias: 6
        - AfraidBias: 4
        - DiplomaticBalance: 1
        - Friendliness: 9
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 7
        - Loyalty: 2
        - MinorCivFriendlyBias: 7
        - MinorCivNeutralBias: 5
        - MinorCivHostileBias: 7
        - MinorCivWarBias: 7
        - DenounceWillingness: 7
        - Forgiveness: 1
        - Meanness: 5
        - Neediness: 3
        - Chattiness: 10
        - DeceptiveBias: 5
        - Rationale: POST-DIPLOMATIC FAILURE ASSERTIVENESS: With diplomatic victory unattainable (30/42 delegates, 12 short), no longer need to signal peaceful intent to world. Maximum Boldness and WarBias demonstrate commitment to conquest path while maintaining vassal loyalty. Signals to Inca that this is existential war for their two remaining capitals. Low Loyalty (2) allows future flexibility with Inca/America after capture.
        
        ## Technology
        - Next: None
        
        ## Policy
        - Next: None (Policy)
        
        ## Relationships
        
        ### Hanoi
        - Public: 40
        - Private: 35
        - Rationale: Onondaga declared war alongside Babylon but has only deployed 1 Archer. They're militarily weak and distracted. Slightly increased priority from hostile to cautiously neutral signals we might accept peace if they offer terms, but we're not seeking it. Focus remains on Austria/Babylon main theaters.
        - UpdatedTurn: 102
        
        ### Onondaga
        - Public: 40
        - Private: 35
        - Rationale: Onondaga now Friends (54 influence, protected). Updating from previous hostile stance (-30/-25) to positive reflects current alliance. Road quest available (49 turns) - positive relationship encourages completion. Provides northern buffer and potential military support.
        - UpdatedTurn: 121
        
        ### Kabul
        - Public: 0
        - Private: 0
        - Rationale: Kabul city-state declaration of war creates distraction from Austrian priority. Clearing hostile modifiers allows AI to evaluate peace options or ignore this non-threat. Kabul allied with Austria (influence 122) making diplomatic resolution difficult, but maintaining war diverts no resources given zero combat units required - military briefing confirms no Kabul forces threaten our territory.
        - UpdatedTurn: 134
        
        ### Kuala Lumpur
        - Public: 50
        - Private: 50
        - Rationale: Kuala Lumpur city-state war continues with -60 influence. Moderate positive relationship (50/50) signals willingness to accept peace if offered, which would secure our western border and allow focus on Austria/Babylon theaters. Low priority but worth resolving if opportunity arises.
        - UpdatedTurn: 151
        
        ### Milan
        - Public: 60
        - Private: 60
        - Rationale: MILAN STABILIZATION: Reduced influence to 80 (from 105) but still Ally. 60/60 maintains positive priority without overcommitting. Northern buffer against Babylon secured, Protected status active. Kabul tribute quest (56 influence) may be achievable - worth monitoring for opportunistic completion.
        - UpdatedTurn: 204
        
        ### Babylon
        - Public: 0
        - Private: 0
        - Rationale: Babylon ELIMINATED - Dur-Kurigalzu formally captured, Nebuchadnezzar removed from game. Clearing hostile modifiers allows AI to evaluate any peace overtures (unnecessary) or ignore. Total victory achieved - 3/8 capitals controlled (37%).
        - UpdatedTurn: 240
        
        ### Antwerp
        - Public: 95
        - Private: 95
        - Rationale: Antwerp URGENT delegate pursuit: At 190 influence (10 shy of Ally threshold 200), need immediate +1 delegate before Turn 272 vote. Increasing priority to 95/95 signals diplomatic AI to gift ~20 gold or complete quests immediately. Byzantium leads 66-84 delegates; securing Antwerp Ally status maintains critical margin for Global Peace Accords repeal.
        - UpdatedTurn: 270
        
        ### Byzantium
        - Public: 0
        - Private: 0
        - Rationale: Byzantium elimination confirmed - military briefing shows zero remaining units and Antioch captured. Clearing -100/-100 hostility modifiers allows AI to process peace treaty formally and focus on post-war economic transition. No diplomatic value in maintaining hostility against eliminated civilization.
        - UpdatedTurn: 310
        
        ### Ban Chiang
        - Public: 95
        - Private: 95
        - Rationale: Ban Chiang is our critical city-state ally (398 influence, +1 delegate). Maintaining maximum relationship ensures delegate stability. With 7 turns until World Congress vote, securing existing allies is priority over gaining new ones. Protected status active, no immediate threats detected.
        - UpdatedTurn: 316
        
        ### Brandenburg
        - Public: 95
        - Private: 95
        - Rationale: Brandenburg ally at 824 influence provides +1 delegate. Maintaining maximum relationship prevents any diplomatic slippage before Turn 322 vote. Russia at 183 influence (Friends) but not threatening Ally status. Protected and stable.
        - UpdatedTurn: 316
        
        ### Oslo
        - Public: 100
        - Private: 100
        - Rationale: Oslo URGENT ally pursuit: Despite Sphere of Influence making Oslo permanently Russian ally, maintaining maximum 100/100 ensures diplomatic stability and prevents any future complications. Oslo at 150 influence (Friends) - positive relationship encourages trade route establishment for gold income.
        - UpdatedTurn: 327
        
        ### Byblos
        - Public: 100
        - Private: 100
        - Rationale: Byblos spy mission CRITICAL: Agent Amaya conducting 'Conduct Spy Mission against Ramesses II' in Pi-Ramesses. Completion grants +300 influence, pushing Byblos from 105 (Friends) to 405 (Ally) for +1 delegate. Maximum 100/100 relationship prioritizes espionage completion before Turn 332 vote. Byblos is only guaranteed path to additional delegate given Open Door locks on other city-states.
        - UpdatedTurn: 327
        
        ### America
        - Public: 100
        - Private: 100
        - Rationale: AMERICA VASSAL STABILITY: Maintaining maximum 100/100 ensures no diplomatic complications. Must keep as vassal until Cusco falls, then liberate immediately for Washington capture. America at 0 military strength poses zero threat. Liberation timing critical - Cusco first, then Washington.
        - UpdatedTurn: 341
        
        ### Egypt
        - Public: -100
        - Private: -100
        - Rationale: EGYPT MAXIMUM HOSTILITY RESTORED: Spy mission for influence already failed, Egypt at 100% war weariness with 1 city remaining. No diplomatic utility in moderated stance. Maximum hostility ensures AI rejects peace, focuses on complete elimination to clear battlefield for Inca offensive.
        - UpdatedTurn: 343
        
        ### The Inca
        - Public: -100
        - Private: -100
        - Rationale: INCA EXISTENTIAL WAR MAINTAINED: War score +52% in our favor, war weariness 45% vs their 72%. No diplomatic utility in moderated stance. Maximum hostility ensures AI rejects peace and commits to total conquest. No negotiation until Cusco falls. Atomic bombardment preparations underway.
        - UpdatedTurn: 380
        
        ### Russia
        - Public: 100
        - Private: 100
        - Rationale: RUSSIA VASSAL MAINTENANCE: Catherine at 2621 strength, 27% war weariness vs Inca, provides northern pressure. Trade deals active (184 GPT). Maximum 100/100 ensures continued loyalty through atomic preparation phase. Their distraction of Inca forces critical for our preparation.
        - UpdatedTurn: 380
        
        ### Austria
        - Public: 100
        - Private: 100
        - Rationale: AUSTRIA VASSAL STABILITY: Provides 6 delegates and 1442 military strength. New Frigate production increases naval capacity. Maximum 100/100 ensures no complications during atomic preparation phase. Maintain until Washington capture.
        - UpdatedTurn: 380
        
        ## Strategy
        - Rationale: Tactical execution failures, not strategic misalignment: Flavors are already optimized (TileImprovement 100, Production 100, Nuke 100, Air 100, Offense 95) for final Cusco push, but AI is failing to assign workers to aluminum mines or queue airport construction. 1500+ production sits idle while critical infrastructure unbuilt. War weariness (45%) manageable, military strength overwhelming (27419 vs Inca 3976). Conquest remains correct path - Diplomatic Victory requires 42 delegates, we have 38 (4 short) with no clear path to +4 in 6 turns before Congress. Total War policy next turn (+25% warscore rate) should force Inca capitulation, bypassing need for direct Cusco capture. Status quo maintained pending execution correction.
        - GrandStrategy: Conquest
        
        ### Flavors
        - Offense: 95
        - Defense: 40
        - Mobilization: 80
        - CityDefense: 60
        - MilitaryTraining: 70
        - Recon: 85
        - Ranged: 65
        - Mobile: 0
        - Nuke: 100
        - UseNuke: 95
        - Naval: 95
        - NavalRecon: 60
        - NavalGrowth: 20
        - NavalTileImprovement: 25
        - Air: 100
        - AirCarrier: 95
        - Antiair: 50
        - Airlift: 100
        - Expansion: 5
        - Growth: 20
        - TileImprovement: 100
        - Infrastructure: 100
        - Production: 100
        - WaterConnection: 35
        - Gold: 5
        - Science: 95
        - Culture: 5
        - Happiness: 70
        - GreatPeople: 40
        - Wonder: 5
        - Religion: 10
        - Diplomacy: 10
        - Spaceship: 0
        - Espionage: 25
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Russia
        - Leader: Catherine
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Russia) have both adopted the Autocracy Ideology. (999)
          - Japan's leader has expressed a public opinion of Russia (100).
          - Japan's leader has formed a private opinion of Russia (100).
          - You (Russia) are Japan's vassal state, and Japan like it! (99)
          - You (Russia) have adopted Japan's religion in the majority of your (Russia) cities. (60)
          - We are trade partners. (40)
          - We have opened our borders to each other. (12)
          - You (Russia) have denounced one of Japan's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We fought together against a common foe. (3)
          - We have shared embassies. (1)
          - Japan's real approach to Russia is Friendly.
          - We have divergent Social Policies. (-3)
          - We defeated Japan's proposal in the World Congress. (-36)
        - TheirOpinionOfUs:
          - Russia are content with your (Japan) treatment of Russia as Russia's master.
          - You (Japan) have no contested borders.
          - You (Japan) have denounced one of Russia's declared enemies!
          - We are trade partners.
          - You (Japan) have both adopted the Autocracy Ideology.
          - You (Japan) protected Russia's territory as their master!
          - We have made a public Declaration of Friendship!
          - We have made Declarations of Friendship with the same leaders!
          - We have a Diplomat in Russia's capital.
          - We freed Russia from sanctions in the World Congress.
          - We have Pledged to Protect the same City-States.
          - We have opened our borders to each other.
          - Your (Japan) recent diplomatic actions please Russia.
          - We have shared embassies.
          - Your (Japan) military deployment is threatening.
          - We have divergent Social Policies.
          - Russia have happily adopted your (Japan) religion in the majority of Russia's cities.
          - Russia are our vassal state.
          - Russia desire friendly relations with Japan.
          - You (Japan) are competing for World Wonders.
          - You (Japan) are competing for the favor of the same City-States!
          - Russia disliked our proposal to the World Congress.
          - We defeated Russia's proposal in the World Congress.
          - Your (Japan) votes opposed Russia's civ's interests in the World Congress.
          - You (Japan) captured Russia's original capital.
        - Score: 1429
        - Era: Modern
        - Technologies: 57
        - Cities: 7
        - Population: 154
        - Territory: 246
        - Gold: 183
        - GoldPerTurn: 192
        - HappinessSituation: Happy
        - HappinessPercentage: 58
        - MilitaryStrength: 2724
        - TourismPerTurn: 237.75
        - CulturePerTurn: 993
        - PolicyBranches:
          - Statecraft: 6
          - Autocracy: 2
          - Tradition: 6
          - Rationalism: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Close
            - War (Our Score: -20%; Our War Weariness: 27%)
            - Denounced Them
          - Japan:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Austria:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
        - Votes: 12
        - 1: Defeated Major Civilization Egypt
        
        ## Player 2
        - Civilization: The Inca
        - Leader: Pachacuti
        - IsMajor: true
        - OurOpinionOfThem:
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Japan's real approach to The Inca is War.
          - Japan are spreading Japan's own religion, but you (The Inca) converted some of their cities to your (The Inca) religion. (-6)
          - Religious differences strain your (The Inca) relationship. (-30)
          - Your (The Inca) spies were caught stealing from Japan. (-33)
          - We defeated Japan's proposal in the World Congress. (-36)
          - Japan's leader has expressed a public opinion of The Inca (-100).
          - Japan's leader has formed a private opinion of The Inca (-100).
          - You (The Inca) have chosen to adopt the Order Ideology, but Japan believe in Autocracy. (-999)
          - You (The Inca) are at war! (-99999)
        - TheirOpinionOfUs:
          - Your (Japan) votes supported The Inca's civ's interests in the World Congress.
          - We have similar Social Policies.
          - We have Pledged to Protect the same City-States.
          - Religious differences strain your (Japan) relationship.
          - The Inca believe we are building World Wonders too aggressively!
          - Territorial disputes strain your (Japan) relationship.
          - You (Japan) have conquered City-States under The Inca's protection!
          - You (Japan) have made a Declaration of Friendship with one of The Inca's enemies!
          - The Inca disliked our proposal to the World Congress.
          - The Inca fear your (Japan) acquisition of multiple vassals!
          - We have denounced each other!
          - The Inca's leader has expressed a public opinion of you (Japan) (-50).
          - You (Japan) have chosen to adopt the Autocracy Ideology, but The Inca believe in Order.
          - We defeated The Inca's proposal in the World Congress.
          - Your (Japan) spies were caught stealing from The Inca.
          - The Inca fear your (Japan) warmongering will end this world in fire! (They strongly dislike warmongers.)
          - You (Japan) are at war!
        - Score: 2540
        - Era: Atomic
        - GoldenAge: 2 turns remaining
        - Technologies: 59
        - Cities: 15
        - Population: 382
        - Territory: 407
        - Gold: 590
        - GoldPerTurn: 911
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 44
        - MilitaryStrength: 3581
        - TourismPerTurn: 548.25
        - CulturePerTurn: 1294
        - PolicyBranches:
          - Fealty: 1
          - Industry: 1
          - Rationalism: 2
          - Statecraft: 5
          - Order: 2
          - Progress: 5
          - Authority: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 46%)
          - Russia:
            - Distance: Close
            - War (Our Score: 20%; Our War Weariness: 52%)
          - Japan:
            - Distance: Neighbors
            - War (Our Score: -60%; Our War Weariness: 84%)
            - Denounced Them
        - Votes: 12
        
        ## Player 3
        - Civilization: Japan
        - Leader: Oda Nobunaga
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: None, Our top defensive pact ally: None
          - Our top World Congress ally: Austria, Our top World Congress rival: The Inca
          - Our top Competitor: The Inca
        - Score: 6031
        - Era: Information
        - GoldenAge: Estimated in 16 turns
        - Technologies: 65
        - CurrentResearch: Nuclear Fission (Estimated in 6 turns)
        - NextPolicyTurns: 22
        - Cities: 38
        - Population: 714
        - Territory: 1149
        - BestSettlementLocation:
          - 27, 10 (Quality: 37%; 4 tiles from us)
          - 26, 10 (Quality: 37%; 4 tiles from us)
          - 24, 10 (Quality: 28%; 4 tiles from us)
          - 16, 28 (Quality: 26%; 4 tiles from us)
          - 25, 10 (Quality: 17%; 5 tiles from us)
        - Gold: 520
        - GoldPerTurn: -900
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 38
        - MilitaryUnits: 129
        - MilitarySupply: 130
        - MilitaryStrength: 28449
        - TourismPerTurn: 1451.37
        - CulturePerTurn: 4119
        - FaithPerTurn: 1144
        - SciencePerTurn: 6188
        - PolicyBranches:
          - Autocracy:
            - Elite Forces
            - Military-Industrial Complex
            - United Front
            - Air Supremacy
            - New World Order
            - Lightning Warfare
            - Third Alternative
            - Total War
          - Industry:
            - Industry
          - Rationalism:
            - Rationalism
            - Scientific Revolution
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Shadow Networks
            - Exchange Markets
            - Trade Confederacy
          - Imperialism:
            - Imperialism
            - Regimental System
            - Civilizing Mission
          - Progress:
            - Progress
            - Organization
          - Authority:
            - Authority
            - Tribute
            - Imperium
            - Militarism
            - Dominance
            - Honor
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - War (Our Score: 60%; Our War Weariness: 45%)
            - Denounced Them
          - Russia:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Austria:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
        - Votes: 38
        - 4: Defeated Major Civilization America
        
        ## Player 5
        - Civilization: Austria
        - Leader: Maria Theresa
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Austria) have both adopted the Autocracy Ideology. (999)
          - Japan's leader has expressed a public opinion of Austria (100).
          - Japan's leader has formed a private opinion of Austria (100).
          - You (Austria) are Japan's vassal state, and Japan like it! (99)
          - You (Austria) have adopted Japan's religion in the majority of your (Austria) cities. (60)
          - We are trade partners. (40)
          - We have opened our borders to each other. (12)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have shared embassies. (1)
          - Japan's real approach to Austria is Friendly.
          - We have divergent Social Policies. (-3)
          - We defeated Japan's proposal in the World Congress. (-36)
        - TheirOpinionOfUs:
          - Austria's leader has expressed a public opinion of you (Japan) (100).
          - Austria are content with your (Japan) treatment of Austria as Austria's master.
          - You (Japan) have both adopted the Autocracy Ideology.
          - We are trade partners.
          - You (Japan) have denounced one of Austria's declared enemies!
          - You (Japan) are not competing for cultural advancement.
          - You (Japan) protected Austria's territory as their master!
          - We have made Declarations of Friendship with the same leaders!
          - You (Japan) are not competing for World Wonders.
          - We have a Diplomat in Austria's capital.
          - We have made a public Declaration of Friendship!
          - We have opened our borders to each other.
          - You (Japan) have no contested borders.
          - Your (Japan) recent diplomatic actions please Austria.
          - We have shared embassies.
          - Your (Japan) military deployment is extremely threatening.
          - We have divergent Social Policies.
          - Austria have happily adopted your (Japan) religion in the majority of Austria's cities.
          - Austria are our vassal state.
          - Austria desire friendly relations with Japan.
          - Austria disliked our proposal to the World Congress.
          - You (Japan) captured Austria's original capital.
          - Your (Japan) votes opposed Austria's civ's interests in the World Congress.
        - Score: 1127
        - Era: Industrial
        - GoldenAge: 9 turns remaining
        - Technologies: 48
        - Cities: 4
        - Population: 83
        - Territory: 134
        - Gold: 941
        - GoldPerTurn: 5
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 1504
        - TourismPerTurn: 253.5
        - CulturePerTurn: 1041
        - PolicyBranches:
          - Tradition: 6
          - Artistry: 1
          - Progress: 6
          - Autocracy: 1
          - Rationalism: 5
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
          - Russia:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - Japan:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
        - Votes: 6
        - 6: Defeated Major Civilization Byzantium
        - 7: Defeated Major Civilization Babylon
        - 22: Defeated Minor Civilization Antwerp
        - 23: Defeated Minor Civilization Milan
        
        ## Player 24
        - Civilization: Byblos
        - Leader: City State
        - MajorAlly: Japan
        - Population: 21
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Inca: War (Influence: -60, Distance: Distant)
          - Russia: Friends (Influence: 664, Distance: Close, Protected)
          - Japan: Ally (Influence: 920, Distance: Neighbors, Protected)
          - Austria: Neutral (Influence: -48, Distance: Neighbors)
        
        ## Player 25
        - Civilization: Kabul
        - Leader: City State
        - Population: 21
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Inca: Neutral (Influence: 0, Distance: Far)
          - Russia: Friends (Influence: 58, Distance: Distant)
          - Japan: Friends (Influence: 900, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 174, Distance: Neighbors)
        - 26: Defeated Minor Civilization Kuala Lumpur
        
        ## Player 27
        - Civilization: Quebec City
        - Leader: City State
        - Population: 15
        - Relationships:
          - The Inca: Friends (Influence: 50, Distance: Close, Protected)
          - Russia: Neutral (Influence: 0, Distance: Distant)
          - Japan: Friends (Influence: 265, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 131, Distance: Far)
        - 28: Defeated Minor Civilization Winchester
        
        ## Player 29
        - Civilization: Stockholm
        - Leader: City State
        - MajorAlly: Japan
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Inca: War (Influence: -60, Distance: Far)
          - Russia: Friends (Influence: 375, Distance: Neighbors, Protected)
          - Japan: Ally (Influence: 760, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 150, Distance: Close)
        
        ## Player 30
        - Civilization: Utica
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 19
        - Relationships:
          - The Inca: Ally (Influence: 716, Distance: Close, Protected)
          - Russia: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Japan: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Austria: War - Peace Currently Blocked (Influence: -60, Distance: Close)
        
        ## Player 31
        - Civilization: Lhasa
        - Leader: City State
        - Population: 23
        - Relationships:
          - The Inca: Friends (Influence: 334, Distance: Neighbors, Protected)
          - Russia: Friends (Influence: 115, Distance: Neighbors, Protected)
          - Japan: Friends (Influence: 459, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 176, Distance: Far)
        
        ## Player 32
        - Civilization: Ban Chiang
        - Leader: City State
        - MajorAlly: Japan
        - Population: 24
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Inca: War (Influence: -60, Distance: Distant)
          - Russia: Friends (Influence: 125, Distance: Far, Protected)
          - Japan: Ally (Influence: 700, Distance: Neighbors, Protected)
          - Austria: Friends (Influence: 232, Distance: Far)
        
        ## Player 33
        - Civilization: Oslo
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 7
        - MajorityReligion: Protestantism
        - Relationships:
          - The Inca: Ally (Influence: 726, Distance: Neighbors, Protected)
          - Russia: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Japan: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Austria: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
        - 34: Defeated Minor Civilization Onondaga
        
        ## Player 35
        - Civilization: Brandenburg
        - Leader: City State
        - MajorAlly: Japan
        - Population: 16
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - The Inca: War (Influence: -60, Distance: Distant)
          - Russia: Friends (Influence: 782, Distance: Close, Protected)
          - Japan: Ally (Influence: 1255, Distance: Neighbors, Protected)
          - Austria: Neutral (Influence: -15, Distance: Close)
        - 36: Defeated Minor Civilization Hanoi
        - 37: Defeated Minor Civilization Jerusalem
        - 63: Barbarians
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Japan
        - Japan:
          - CapitalsControlled:
            - Moscow
            - Thebes
            - Kyoto
            - Washington
            - Vienna
            - Constantinople
            - Babylon
          - CapitalsPercentage: 87
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 3
        - Contender: Japan
        - Austria:
          - Influences:
            - The Inca: Exotic (16%) - Rising Slowly (tourism/culture ratio 57%)
            - Russia: Familiar (28%) - Rising Slowly (tourism/culture ratio 86%)
            - Japan: Exotic (9%) - Rising Slowly (tourism/culture ratio 31%)
          - PolicyPercentage: 88
          - InfluentialCivs: 0
        - Japan:
          - Influences:
            - The Inca: Popular (58%) - Rising Slowly (tourism/culture ratio 40%)
            - Russia: Influential (184%) - Rising (tourism/culture ratio 433%)
            - Austria: Dominant (228%) - Rising (tourism/culture ratio 345%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        - Russia:
          - Influences:
            - The Inca: Exotic (24%) - Rising Slowly (tourism/culture ratio 62%)
            - Japan: Exotic (12%) - Rising Slowly (tourism/culture ratio 35%)
            - Austria: Popular (51%) - Rising Slowly (tourism/culture ratio 94%)
          - PolicyPercentage: 88
          - InfluentialCivs: 0
        - The Inca:
          - Influences:
            - Austria: Familiar (29%) - Rising Slowly (tourism/culture ratio 45%)
            - Russia: Familiar (37%) - Rising Slowly (tourism/culture ratio 82%)
            - Japan: Exotic (13%) - Rising Slowly (tourism/culture ratio 38%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 42
        - Status: World Congress - Voting in 5 turns
        - ActiveResolutions:
          - Sanction: Japan:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
          - Global Peace Accords:
            - Description: Unit maintenance costs are raised by 25% Gold. 2.0x Warmonger penalties for capturing cities and declaring war, and 0.5x Warmonger scores decay.
            - EnactedOn: -1
          - Open Door: Kabul:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Endowment for the Arts:
            - Description: Increases up to 33% generation of Great Writers, Artists, and Musicians. Decreases up to 33% generation of Great Scientists, Engineers, and Merchants.
              Civilizations with Scores from Policies and Great Works below the global median will receive a boost to Production and Culture up to 33%.
              Details: The boosts are proportional to the difference between the score of the Civilization and the leader.
            - EnactedOn: 377
          - Open Door: Lhasa:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Historical Landmarks:
            - Description: Great Person tile improvements provide +1 to Food, Production, and Gold when worked, and Landmarks built by Archaeologists provide +1 Science, Culture, and Faith when worked.
              Available once any Civilization discovers Archaeology.
            - EnactedOn: -1
          - Open Door: Quebec City:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - World Religion: Eastern Orthodoxy:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: 355
        - Proposals:
          - Enact: Passport System:
            - Description: Increases international travel between Civilizations. Increases the Tourism modifier for all Civilizations by 50%.
              Available once any Civilization discovers Flight.
            - Proposer: Japan
          - Repeal: Sanction: Japan:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - Proposer: Russia
          - Enact: Open Door: Stockholm:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - Proposer: The Inca
        - Contender: Japan
        - Austria:
          - Delegates: 6
          - VictoryPercentage: 14
        - Japan:
          - Delegates: 38
          - VictoryPercentage: 90
        - Russia:
          - Delegates: 12
          - VictoryPercentage: 28
        - The Inca:
          - Delegates: 12
          - VictoryPercentage: 28
        
        # Briefings
        ## Military Briefing
        (Produced with your instruction: CRITICAL EXECUTION AUDIT - Turn 383: Report specifically on whether the AI has started ANY aluminum mine construction on the 6 available aluminum tiles, and if workers remain on railroad projects, WHY the flavors (TileImprovement 100, Production 100) haven't triggered mine priority. Check if an Airport project has been queued in Arequipa or any city within Cusco bomber range. Confirm whether Yamato battleship has been placed in production queue with Nuclear Fission 6 turns away. We have 1500+ idle production capacity - demand explanation of why queues are empty in Kyoto, Tokyo, Graz, Vienna, Kuala Lumpur after current projects complete. Focus on micromanagement failures preventing Cusco assault.)
        
        **Military Execution Audit – Turn 383**  
        *Japan (Player 3) – Oda Nobunaga*  
        
        ---
        
        ### 1. Aluminum Mine Construction – Tile‑Improvement Priority  
        
        - **Aluminum tiles owned:** 6 (all on the continent of the Inca front).  
        - **Current improvement status:**  
          - No **Aluminum Mine** has been started on any of the six tiles.  
          - All six tiles remain as **Unimproved** resources (shown in the map overlay; no “Mine” icon).  
        
        - **Worker assignment:**  
          - All **Builders** (7 total) are tied up on **Railroad** projects (city‑to‑city connections in the central and western rail corridor) and **Airport** construction in Winchester (2‑turn build).  
          - No Builder is free to start a Mine, despite the AI flavor weights (TileImprovement = 100, Production = 100).  
        
        - **Reason for flavor suppression:**  
          - The **Production queue** of every city (Kyoto, Tokyo, Graz, Vienna, Kuala Lumpur) is filled with higher‑priority items (Heavy Bombers, Public Works, International Space Station project, Research Lab).  
          - The AI’s “Production = 100” weight only applies when a city has **available production capacity**; with 1 500+ idle production points spread across 38 cities, the AI is currently **assigning all excess production to existing queue items** rather than creating new Builder orders.  
          - Consequently, **Builder availability = 0**, preventing any Mine start despite the resource‑rich tiles.
        
        ### 2. Railroad Projects – Worker Availability  
        
        - **Active railroad projects (8 total):**  
          - Kyoto → Osaka, Osaka → Vienna, Vienna → Akkad, Akkad → Arequipa, Arequipa → Winchester, etc.  
        - **Builders attached:** 7 (all on the above lines).  
        - **No idle Builder** remains to switch to Mine construction.  
        
        ### 3. Airport Construction – Arequipa / Winchester  
        
        - **Winchester Airport:**  
          - Currently **under construction** (2 turn remaining).  
          - No airport has been queued **in Arequipa** or any city within the **6‑tile bomber range of Cusco**.  
        
        - **Arequipa (Inca‑controlled) – no Japanese presence:**  
          - No Japanese city occupies Arequipa; therefore the AI cannot queue an airport there yet.  
          - No Japanese‑controlled city lies within the required **≤ 6‑tile radius** of **Cusco (1059, 41)**.  
        
        - **Result:** No bomber can be staged close enough for a precision strike on Cusco; all heavy bombers remain ≥ 12 tiles away (Los Angeles, Elephantine, Constantinople, etc.).
        
        ### 4. Yamato Battleship Production  
        
        - **Nuclear Fission technology:** 6 turns away from completion (estimated turn 389).  
        - **Yamato (unique Battleship):**  
          - **Not** present in any production queue.  
          - No city currently has a **Yamato** slot open; the only cities with shipyards (Kyoto, Osaka, Tokyo) are all occupied with **Heavy Bomber** or **Public Works** projects.  
        
        - **Implication:** Even after Nuclear Fission is researched, the AI will need to free a shipyard slot and allocate production before the Yamato can be built.
        
        ### 5. Idle Production Capacity – Empty Queues  
        
        - **Cities with empty post‑completion slots (after current projects finish):**  
          - **Kyoto:** Manhattan Project (2 turns left).  
          - **Tokyo:** Heavy Bomber (1 turn left).  
          - **Graz:** Heavy Bomber (1 turn left).  
          - **Vienna:** Heavy Bomber (1 turn left).  
          - **Kuala Lumpur:** Research Lab (3 turns left).  
        
        - **Why queues are empty:**  
          1. **All current items are pre‑set by the AI** based on existing strategic priorities (nuclear project, bomber production, space‑station progress).  
          2. **No new production orders have been issued** because the AI “waits” for the completion of high‑value projects before adding additional items; this is a built‑in pacing rule in Vox Populi.  
          3. **Production overflow is not auto‑assigned** to Builder creation; the AI prefers to keep excess production unspent rather than start new Builder or Mine projects unless a specific “Construction” order is queued.  
        
        - **Resulting idle production:** ≈ 1 500 + production points per turn sit unused, which could otherwise fund **Builder units** (to start Mines) or **airport construction** in a forward city.
        
        ### 6. Impact on Cusco Assault (Micromanagement Gaps)  
        
        | Requirement | Current State | Gap |
        |-------------|---------------|-----|
        | **Aluminum for advanced units** (e.g., Tanks, Heavy Bombers) | No mines → no aluminum output | Resource bottleneck |
        | **Forward airbase ≤ 6 tiles from Cusco** | No Japanese city with airport within 6 tiles; Winchester airport 2 turns away, still 9 tiles distant | No bomber staging point |
        | **Yamato (nuclear strike platform)** | Not in queue; shipyard slots occupied, tech 6 turns away | No atomic option |
        | **Builders for Mine & Airport** | 0 idle Builders (all on railroads) | No capacity to start critical improvements |
        | **Production slots after current projects** | Empty, but no orders placed | Idle production not redirected to needed tasks |
        
        ### 7. Summary of Failures  
        
        1. **Builder starvation** – all Builders tied to railroads, preventing Mine construction on six aluminum tiles.  
        2. **Airport omission** – no airport queued in a city that can bring bombers within 6 tiles of Cusco; Winchester still out of range.  
        3. **Yamato omission** – battleship not queued despite imminent Nuclear Fission, leaving the atomic strike path unavailable.  
        4. **Production queuing** – after the completion of the Manhattan Project, Heavy Bombers, and Public Works, the AI leaves the city queues empty instead of ordering new Builders or strategic improvements.  
        
        These micromanagement oversights keep the **Cusco assault** stalled: without aluminum, bombers cannot be upgraded; without a forward airfield, bombers cannot reach the target; without a Yamato, no nuclear option exists. Immediate reallocation of Builders and production capacity to **Aluminum Mines**, **Winchester Airport**, and **Yamato** (once Fission finishes) is required to unlock the intended offensive.
        
        ## Economy Briefing
        (Produced with your instruction: ALUMINUM EMERGENCY TRACKING: Current net aluminum is -5/turn (consumption 6, production 1) with 130 stockpile = 26 turns until depletion. Check if ANY aluminum mine construction has started on the 6 controlled aluminum tiles. Verify which specific tiles have aluminum and whether workers have been assigned. Project aluminum trajectory if we build Yamato (+2 consumption) without additional mines - we need +3 mines minimum for sustainability. Report whether trade routes to Russia and Austria have been established to offset -42 GPT deficit - briefing identified potential +27 GPT from these routes but none established. Why is gold production prioritized over strategic resources when we're at 7/8 capitals?)
        
        **Japan – Economic Situation Briefing (Turn 383)**  
        *Prepared for Oda Nobunaga – focus on strategic‑resource balance, gold deficit, and trade‑route status.*
        
        ---
        
        ### 1. Strategic‑Resource (Aluminum) Overview  
        
        | Tile – Location | Current Improvement | Worker Assigned?* | Production Status |
        |-----------------|---------------------|-------------------|-------------------|
        | **Kyoto** (≈ 6 tiles) | None (plain/grass) | No record of a Mine order | No extraction |
        | **Satsuma** (≈ 4 tiles) | None | No Mine order | No extraction |
        | **Graz** (≈ 2 tiles) | None | No Mine order | No extraction |
        | **Vienna** (≈ 3 tiles) | None | No Mine order | No extraction |
        | **Moscow** (≈ 5 tiles) | None | No Mine order | No extraction |
        | **Babylon** (≈ 4 tiles) | None | No Mine order | No extraction |
        
        \*The event log does not list worker‑tile assignments; the absence of any “Mine” construction events for these tiles indicates that no workers have been sent to build mines on any of the six aluminum sites.
        
        **Net Aluminum Balance (turn 383):**  
        - Stockpile: **130 Al** (unchanged since turn 378)  
        - Consumption: **6 Al/turn** (current unit composition)  
        - Domestic Production: **+1 Al/turn** (only one active mine reported on a non‑Japanese tile)  
        - **Net Δ = ‑5 Al/turn** → projected depletion in **≈ 26 turns** if unchanged.
        
        **Projected impact of Yamato (Battleship‑class) construction:**  
        - Yamato consumes **+2 Al/turn** (additional to existing 6 Al/turn).  
        - Without new mines the net would become **‑7 Al/turn**, shortening the runway to ~18 turns.  
        - To keep a non‑negative balance with Yamato in the queue, at least **3 additional aluminum mines** must become operational (each provides +1 Al/turn), raising net Δ to **‑5 Al/turn** or better.
        
        ---
        
        ### 2. Gold Production vs. Deficit  
        
        | Metric | Value (turn 383) |
        |--------|------------------|
        | Gold Stockpile | **520 G** |
        | Gold per Turn (GPT) | **‑900 G/turn** (net loss) |
        | Primary Sources of Income | Trade routes (see § 3) and limited internal gold from cities (e.g., Kyoto +710 G/turn, Osaka +182 G/turn) |
        | Primary Drains | **Unit maintenance** (inflated by Global Peace Accords resolution: +25 % maintenance cost) and high‑cost projects (e.g., Manhattan Project nearing completion, multiple Heavy Bomber productions). |
        | Estimated time to zero gold (if deficit persists) | **≈ 0.6 turns** – the empire is already in a cash‑flow crisis and is relying on trade‑route gold inflows and ongoing deals to stay solvent. |
        
        *Why gold is being prioritized despite the deficit?*  
        - The empire holds **38 diplomatic delegates** and is within 5 turns of a World‑Congress vote, making **gold‑based deals** (the numerous resource‑for‑gold agreements with Austria and Russia) a principal source of immediate income.  
        - The **Gold‑per‑turn values shown for cities** are net after maintenance; many cities still show positive GPT (e.g., Kyoto +710 G/turn) but the aggregate is outweighed by the global maintenance hike.  
        - No new gold‑generating improvements (e.g., Mines on gold tiles, new Commercial Hubs) have appeared in the event log; the AI’s current production focus is on **military units and space projects** rather than new gold infrastructure.
        
        ---
        
        ### 3. Trade‑Route Status (Gold Offsets)  
        
        | Route | Owner → Destination | Current Gold per Turn | Science per Turn | Culture per Turn | Status |
        |-------|--------------------|-----------------------|------------------|------------------|--------|
        | **Satsuma → Novgorod** (land) | Japan → Russia | **+8.4 G** | +14 Sci | +3 Cult | Active (5 turns left) |
        | **Satsuma → St. Petersburg** (land) | Japan → Russia | **+15.95 G** | +14 Sci | +3 Cult | Active (7 turns left) |
        | **Satsuma → Rostov** (land) | Japan → Russia | **+10.15 G** | +14 Sci | +3 Cult | Active (23 turns left) |
        | **Kyoto → Salzburg** (land) | Japan → Austria | **+7 G** | +17.5 Sci | +4 Cult | Active (8 turns left) |
        | **Kyoto → Linz** (land) | Japan → Austria | **+10.8 G** | +17.5 Sci | +4 Cult | Active (9 turns left) |
        | **Kyoto → Klagenfurt** (land) | Japan → Austria | **+6 G** | +17.5 Sci | +4 Cult | Active (9 turns left) |
        | **Kyoto → Byblos** (land) | Japan → City‑State | No gold listed (food route) |
        | **Kyoto → Heliopolis** (land) | Japan → Russia | **+8.4 G** | +14 Sci | +3 Cult | Active (11 turns left) |
        | **Kyoto → Stockholm** (land) | Japan → City‑State | No gold listed (culture route) |
        | **Kyoto → St. Petersburg** (sea) | Japan → Russia | **+9.75 G** | +26 Sci | +16 Cult | Active (9 turns left) |
        | **Kyoto → Nicaea** (land) | Japan → Russia | **+9.75 G** | +26 Sci | +16 Cult | Active (27 turns left) |
        | **Kyoto → Elephantine** (sea) | Japan → Austria | **+16.25 G** | +26 Sci | +16 Cult | Active (1 turn left) |
        | **Kyoto → Akkad** (land) | Japan → Austria | **+11.05 G** | +26 Sci | +16 Cult | Active (22 turns left) |
        | **Kyoto → Linz** (land) | Japan → Austria | **+9.75 G** | +26 Sci | +16 Cult | Active (26 turns left) |
        | **Kyoto → Yaroslavl’** (land) | Japan → Russia | **+5.5 G** | +27.5 Sci | +18.75 Cult | Active (17 turns left) |
        | **Kyoto → St. Petersburg** (land) | Japan → Russia | **+10.12 G** | +27.5 Sci | +18.75 Cult | Active (19 turns left) |
        | **Satsuma → Brandenburg** (land) | Japan → City‑State | No gold (culture/food) |
        | **Kyoto → Byblos** (land) | Japan → City‑State | No gold (food) |
        | **Satsuma → Bregenz** (land) | Japan → Austria | **+5.6 G** | +17.5 Sci | +4 Cult | Active (4 turns left) |
        | **Satsuma → Hanoi** (sea) | Japan → Russia | **+10.15 G** | +14 Sci | +3 Cult | Active (10 turns left) |
        
        **Net Gold from Trade Routes (summed):** ≈ +150 G/turn (gross). After accounting for the **‑0.5 G × maintenance penalty** imposed by the Global Peace Accords, the net contribution still falls far short of covering the **‑900 G/turn** deficit.
        
        **Unestablished routes that could offset the deficit:**  
        - The “Passport System” proposal (Japan) would raise tourism, not gold.  
        - No additional **Gold‑only** routes to Russia/Austria have been opened beyond those listed; the AI has not created new commercial hubs or caravans to generate extra gold.
        
        ---
        
        ### 4. Recent Economic‑Related Events (Turns 382‑383)
        
        | Turn | Event Type | Key Economic Effect |
        |------|------------|---------------------|
        | 382 | DealMade (Japan ↔ Austria) – Austria provides **Gold per Turn** (duration 50) in exchange for resources. | Immediate gold inflow (not yet quantified in the snapshot). |
        | 382 | Multiple Austria city investments (Museums, Constabulary) – no direct gold effect but increase culture/tourism. |
        | 382 | Japan’s **City‑Bought Plot** (Kuala Lumpur) – Refinery added, increasing oil processing capacity. |
        | 383 | **Aluminum mine pillaged** on tile 18,35 (Japan) – loss of a mine (already non‑operational). |
        | 383 | **Great Engineer** created (Kyoto) – potential future infrastructure projects. |
        | 383 | **Great Writer / Artist** created (Kyoto) – boosts cultural output. |
        | 383 | **Great General** created (Tokyo) – military morale but no direct economic impact. |
        | 383 | **Yamato** (unique battleship) research **Nuclear Fission** still 6 turns away; no production yet. |
        | 383 | **Total War** policy adopted – likely raises military production weight, further stressing gold. |
        | 383 | Multiple **Heavy Bomber** upgrades completed – increase unit maintenance (gold) and aluminum consumption. |
        | 383 | New **Archaeological Dig / Landmark** improvements (Antiquity Sites) – minor gold increase via tourism, no direct gold output. |
        | 383 | **Caravan** units erected (Satsuma → Rostov, Satsuma → new routes) – maintain trade‑route volumes. |
        | 383 | **Tile Route changes** (food, uranium farms) – improve food production, not gold. |
        
        ---
        
        ### 5. Comparison to Turn 378 Briefing (5‑turn interval)
        
        | Aspect | Turn 378 | Turn 383 | Change |
        |--------|----------|----------|--------|
        | **Aluminum net Δ** | ‑6 Al/turn (1 mine, 6 consumption) | ‑5 Al/turn (1 mine, 6 consumption) | Slight improvement in net loss (still negative). |
        | **Aluminum stock** | 130 Al | 130 Al (unchanged) | No extraction added. |
        | **Aluminum mines built** | 0 (none) | 0 (none) | No progress on mining. |
        | **Gold per Turn** | ‑900 G/turn (same) | ‑900 G/turn (same) | Deficit unchanged. |
        | **Trade‑route gold income** | ≈ +150 G/turn (estimated) | ≈ +150 G/turn (no new routes) | No additional gold routes opened. |
        | **Strategic‑resource consumption** | 6 Al/turn (unit composition) | 6 Al/turn (unit composition unchanged) | No increase despite new Heavy Bomber upgrades. |
        | **Policy weight shift** | No explicit policy change reported. | Adopted **Total War** (Autocracy branch). | Likely raises military production weight, intensifying gold maintenance costs. |
        | **Gold‑for‑resource deals** | Ongoing with Austria (Gold per Turn for resources). | Continued; latest deal still active (duration 50). | No new gold‑focused deals observed. |
        | **Infrastructure focus** | Airport construction bottleneck noted (Arequipa, Kuala Lumpur). | No airport projects queued; same bottleneck persists. | No shift toward airport completion. |
        
        **Overall Trend:** The economy remains **resource‑deficient** (aluminum) and **cash‑negative**. The AI continues to prioritize **military/unit production** (Total War, Heavy Bomber upgrades) and **cultural/tourism projects** (Great Writer/Artist, Landmark builds) over **strategic‑resource extraction** or **new gold‑generating infrastructure**.
        
        ---
        
        ### 6. Summary of Current Economic Position  
        
        - **Strategic‑resource outlook:** Aluminum deficit persists; without at least three additional mines the empire will run out of aluminum before the end of the Information era, jeopardizing future Nuclear‑era units (including the Yamato).  
        - **Gold outlook:** Net loss of ~‑900 G/turn; trade routes supply only a fraction of the shortfall. The empire depends heavily on **resource‑for‑gold deals** (Austria) and **diplomatic delegate leverage** (World Congress) to obtain short‑term gold.  
        - **Trade‑route network:** Fully operational with Russia and Austria; no new routes have been established since turn 382, and no gold‑only routes exist beyond the existing list.  
        - **Policy & production focus:** Adoption of **Total War** and continued Heavy Bomber production have increased unit maintenance and aluminum consumption, while **airport construction** remains stalled in peripheral cities (Arequipa, Kuala Lumpur).  
        
        These facts reflect the macro‑economic state relative to the prior briefing and provide the data needed for adjusting AI weighting or diplomatic actions.
        
        ## Diplomacy Briefing
        **Diplomacy Brief – Oda Nobunaga (Japan) – Turn 383**  
        *All statements are factual; no recommendations are given. This report is for macro‑level weight setting.*
        
        ---
        
        ## 1. Delegate Situation (Current & Near‑Future)
        
        | Turn | Core delegates* | Vassal‑derived delegates† | Total Japan votes | Vote threshold |
        |------|----------------|---------------------------|-------------------|----------------|
        | 383 (now) | **38** (base 20 + 2 × 6 city‑states ≥ 500 inf) | **0** (Russia & Austria remain vassals, no separate delegate count) | **38** | **42** |
        | 386 (World‑Congress vote in 3 turns) | 38 | 0 | **38** | **42** |
        
        \*Core delegates = 20 base + 1 extra per *Friend* city‑state with **≥ 500** influence; each such city‑state supplies **2** extra delegates. The six high‑influence city‑states are still:
        
        | City‑State | Influence (Japan) | Relationship |
        |------------|-------------------|--------------|
        | Byblos      | 920 (Ally, Protected) | Ally |
        | Kabul       | 900 (Friend, Protected) | Friend |
        | Ban Chiang  | 700 (Ally, Protected) | Ally |
        | Stockholm   | 760 (Ally, Protected) | Ally |
        | Brandenburg | 1 255 (Ally, Protected) | Ally |
        | Lhasa       | 459 (Friend, Protected) | Friend |
        
        †Vassal‑derived delegates are already included in the base 20; Russia (12 delegates) and Austria (6 delegates) each contribute to the core count via their vassal status.
        
        **Status:** Japan remains **4 delegates short** of the 42‑vote majority needed to pass resolutions unilaterally at the upcoming vote (turn 386). Maintaining the ≥ 500 influence levels with the six city‑states is essential to keep the current 12 extra delegates.
        
        ---
        
        ## 2. Major Diplomatic Developments Since Turn 378
        
        | Category | Details |
        |----------|---------|
        | **World‑Congress – Active Resolutions** | • **Sanction – Japan** (no trade, deals or corp franchises with non‑vassals; 0.5× warmonger penalty when attacking the sanctioned civ).<br>• **Global Peace Accords** (unit‑maintenance + 25 % Gold; warmonger penalties × 2, decay × 0.5).<br>• **Open Door – Kabul, Lhasa, Quebec City** (all civs locked at 40 influence with each; no new allies possible).<br>• **World Religion – Eastern Orthodoxy** (Japan’s cities are 100 % Orthodox).<br>• **Cultural Heritage Sites**, **Historical Landmarks**, **Endowment for the Arts** (Russia’s proposal still active), **Passport System** (Japan’s proposal pending). |
        | **War Status** | • **Japan vs The Inca** – War continues. Japan holds **+60 %** war score; **Japan war weariness 45 %**, **Inca weariness 84 %** (Inca fatigue increased markedly). No new fronts opened. |
        | **City‑State Influence & Relations** | All six high‑influence city‑states remain **≥ 500** influence; no loss of influence has occurred. Quebec City stays at 265 influence (Friend) under Open Door. |
        | **Sanctions** | Still active; all existing trade routes are with Russia, Austria, or protected city‑states, thus unaffected. No new foreign (non‑vassal) routes have been opened. |
        | **Spies** | • **Usagi (Idx 0)** – Gathering intelligence in Chicago (Inca).<br>• **Yuriko (Idx 9)** – Gathering intelligence in Vilcas (Inca).<br>• **Momochi (Idx 2)** – Gathering intelligence in Corihuayrachina (Inca).<br>• **Akira (Idx 5)** – Vassal diplomat in St. Petersburg (Russia).<br>• **Oki (Idx 3)** – Vassal diplomat in Linz (Austria).<br>• **Additional agents** (Hattori, Amaya, etc.) continue work in Inca territory. |
        | **Trade** | • **Inbound routes (8 total)** – Russia (5), Austria (3). All compliant with the sanction.<br>• **Outbound routes (9 total)** – to Russia, Austria, and protected city‑states (Byblos, Kabul, Quebec City, etc.). |
        | **Religion** | • Eastern Orthodoxy is the **World Religion** and is present in **100 %** of Japanese cities (latest conversions: Philadelphia, Antioch, Varna, Nara).<br>• No religious tension with vassals; all share the same faith. |
        | **Recent Events** | • **City‑religion conversions** – Vladivostok (Russia), multiple Inca cities (still Protestant), Japanese cities (Philadelphia, Antioch, Varna, Nara) reaffirmed Orthodoxy.<br>• **Unit upgrades** – Six Japanese bombers upgraded to Heavy Bombers; one Triplane upgraded to Zero.<br>• **Tile acquisition** – New grass‑hill tile (21,29) now owned by Japan.<br>• **Trade‑route completions** – Satsuma → Rostov (food) and Satsuma → Rostov (food) completed; Austria‑Japan trade route (Linz → Yaroslavl’) delivering food.<br>• **Espionage** – Inca spy detected in Giza (Japan); Japanese spy detected in Tiwanaku (Inca). |
        
        ---
        
        ## 3. Relationship Summary (Key Civs)
        
        | Civ | Status | Delegates (from civ) | Victory % | Notable Points |
        |-----|--------|----------------------|-----------|----------------|
        | **Russia** | Vassal (master), Open Borders, Declaration of Friendship | **12** (provides 10 delegates) | 14 | Shares Eastern Orthodoxy; large gold‑per‑turn income; very positive opinion of Japan; supplies 10 WC delegates. |
        | **Austria** | Vassal (master), Open Borders, Declaration of Friendship | **6** (provides 10 delegates) | 90 | Same religion; strong trade pipeline; supplies 10 WC delegates. |
        | **The Inca** | **War**, Denounced, Religious difference (Protestant vs Orthodox) | **0** | 30 | Inca war weariness **84 %** (very high); Japanese spies active in many Inca cities; no peace overtures received. |
        | **Other Majors** | No diplomatic interaction this turn. | — | — | — |
        
        Both vassals continue to view Japan as their master and have adopted Japan’s religion, keeping relations extremely friendly despite the sanction.
        
        ---
        
        ## 4. City‑State Overview (Influence, Quests, Religion)
        
        | City‑State | Influence (Japan) | Relationship | Major Quest(s) | Religion |
        |------------|-------------------|--------------|----------------|----------|
        | **Byblos** | 920 (Ally, Protected) | Ally | – | Eastern Orthodoxy |
        | **Kabul** | 900 (Friend, Protected) | Friend | • Archaeology (218 inf, 1 556 Tourism) • Great Artist (220 inf, 1 017 Culture) | Eastern Orthodoxy |
        | **Ban Chiang** | 700 (Ally, Protected) | Ally | – | Eastern Orthodoxy |
        | **Stockholm** | 760 (Ally, Protected) | Ally | – | Eastern Orthodoxy |
        | **Brandenburg** | 1 255 (Ally, Protected) | Ally | • Great Scientist (237 inf, 616 Culture) • Acquire **Arequipa** (659 inf, Juggernaut unit) | Eastern Orthodoxy |
        | **Lhasa** | 459 (Friend, Protected) | Friend | • Archaeology (203 inf, 1 099 Tourism) | Eastern Orthodoxy |
        | **Quebec City** | 265 (Friend, Protected) | Friend (Open Door) | • Trade‑route (190 inf, 453 Food in Capital) | — |
        | **Utica** | –60 (War – peace blocked) | War (blocked) | – | — |
        | **Oslo** | –60 (War – peace blocked) | War (blocked) | – | Protestantism |
        | **Other city‑states** remain neutral or under Open‑Door lock‑in.
        
        All Allies/Friends remain **above the 40‑influence floor** required by Open‑Door resolutions, preserving the current delegate distribution.
        
        ---
        
        ## 5. Economic & War‑Weariness Snapshot
        
        | Metric | Value |
        |--------|-------|
        | **Gold per Turn** | **‑900** (large deficit; increased from ‑7 at turn 378 due to higher upkeep from unit upgrades and war) |
        | **Gold Reserve** | 520 |
        | **Sanction Effect** | No trade/deals with non‑vassals; current routes (Russia, Austria, protected city‑states) remain legal. |
        | **War Weariness – Japan** | **45 %** (rising) |
        | **War Weariness – Inca** | **84 %** (very high) |
        | **Happiness** | Unhappy – combat penalty (war weariness contributes). |
        
        The gold deficit has deepened as wartime upkeep and unit upgrades increase expenses. The sanction continues to block any new lucrative foreign trade.
        
        ---
        
        ## 6. World‑Congress Vote Feasibility (Turn 386)
        
        - **Japan‑controlled delegates:** **38** (still below the 42‑vote majority).  
        - **Potential opposition:** Russia (12 delegates) plus other civs (≈ 24 delegates total).  
        - **Outcome:** Japan **cannot** pass a resolution unilaterally at the upcoming vote unless it gains additional delegates or secures support from other civs.
        
        **Key leverage points:**  
        1. **Preserve ≥ 500 influence** with the six high‑influence city‑states to retain the 12 extra delegates.  
        2. **Avoid any loss** of influence that would allow another civ to become an Ally/Friend and seize delegates.  
        3. **Monitor the sanction repeal vote** (Russia’s proposal to repeal the sanction) – its outcome will directly affect economic recovery.
        
        ---
        
        ## 7. Comparison to Turn 378 Briefing
        
        | Aspect | Turn 378 | Turn 383 | Change |
        |--------|----------|----------|--------|
        | **Core delegates** | 36 | 38 | +2 (gain from maintaining 6 city‑states ≥ 500) |
        | **Total votes** | 36 | 38 | +2 (still below 42) |
        | **War weariness (Japan)** | 45 % | 45 % | unchanged |
        | **War weariness (Inca)** | 72 % | 84 % | +12 % (Inca now heavily fatigued) |
        | **Gold per turn** | ‑7 | **‑900** | large increase in deficit (unit upgrades, maintenance) |
        | **Sanction** | Active | Active | unchanged |
        | **City‑state influence** | Six city‑states ≥ 500 (stable) | Same six remain ≥ 500 | stable |
        | **World‑Congress proposals** | Japan’s Passport System pending; Russia’s Endowment for the Arts active | Same set; no new proposals added | unchanged |
        | **Religion** | 100 % Eastern Orthodoxy in Japan | 100 % Eastern Orthodoxy (new conversions: Philadelphia, Antioch, Varna, Nara) | maintained |
        | **Spies** | 4 active Inca missions | 6 active Inca missions (plus detection events) | increased espionage pressure |
        | **Trade** | ‑7 GT, limited routes | ‑900 GT, more routes (including food routes to Russia) | deficit worsened |
        | **Open‑Door** | Quebec, Kabul, Lhasa active | Same three active | unchanged |
        | **War status** | Ongoing war, +50 % score | Same war, +60 % score (Japan improving) | modest improvement |
        
        Overall, Japan’s diplomatic position is **stable** but **delegate short**; war weariness remains high for both sides, with the Inca now severely fatigued. Economic health has deteriorated due to increased military upkeep while the sanction continues to block foreign trade.
        
        ---
        
        ## 8. Monitoring Points (for macro‑weight setting)
        
        1. **Delegate security** – Keep influence **> 40** with all six high‑influence city‑states; any dip below 40 would reduce the 12 extra delegates. |
        2. **Sanction repeal vote** – Outcome of Russia’s proposal (turn 381) will determine whether foreign trade can resume and whether the gold deficit can be addressed. |
        3. **Inca war** – Inca weariness **84 %**; continued pressure may force a peace offer, but monitor for any sudden peace‑proposal attempts (currently blocked). |
        4. **City‑state quests** – Pending quests (Kabul archaeology/Great Artist, Brandenburg Great Scientist & Arequipa, Lhasa archaeology, Brandenburg Arequipa capture) provide large influence spikes and valuable yields; completing them reinforces delegate count. |
        5. **World‑Congress agenda** – Japan’s **Passport System** proposal and Russia’s **Endowment for the Arts** will compete for votes at turn 386; anticipate alignment of other civs. |
        6. **War weariness management** – Japan at 45 % (approaching the 50 % combat‑penalty threshold). Consider allocating happiness resources or temporary cease‑fire negotiations to avoid further decline. |
        7. **Economic recovery** – If the sanction is lifted, reassess trade agreements with non‑vassal civs to convert the large gold deficit into surplus. |
        
        *End of Brief.*
        
        You, Oda Nobunaga (leader of Japan, Player 3), are making strategic decisions after turn 383.
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
      - Advanced Ballistics: Allows you to build the Nuclear Missile, a frightening weapon that requires Uranium, and is capable of destroying units and cities. Also allows you to build the Guided Missile, an inexpensive single-use Unit that can damage enemy Units, and the SS Booster, one of the Spaceship parts necessary to win a Science Victory.
        Completing it would unlock: Lasers, Stealth
      - Refrigeration: Allows Work Boats to construct an Offshore Platform, and increases Trade Route maximum travel distance.
        Completing it would unlock: Electronics, Computers
      
      ## Policies
      - Co-Prosperity Sphere (Level 3 Tenet of Ideology Autocracy): Co-Prosperity Sphere: Bullying City-States no longer reduces Influence, revokes Quests, or cancels Pledges of Protection. Doing so decreases the Influence of all other Civs with the bullied City-State by 10%, and increases your Influence by 10%.
      - Cult of Personality (Level 3 Tenet of Ideology Autocracy): Cult of Personality: +50% Tourism to civilizations fighting a common enemy. 50% of your highest Warscore counts as a Tourism Modifier with all Civilizations. Free Great Person of your choice.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Exploitation (Continuing Imperialism Branch):
        - * +2 Food and +1 Production from Farms, Camps, and Plantations.
        - * +1 Production and Science from Coasts, Lakes, and Oceans.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Consulates (Continuing Statecraft Branch):
        - * +1 Delegate in the World Congress for every 8 City-States originally in the World.
        - * Completing a Trade Route to a City-State triggers (or strengthens an existing) Historic Event.
      - Liberty (Continuing Progress Branch):
        - * +2 Gold in every City.
        - * +25% Tile improvement rate.
        - * A Worker appears near the Capital.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Expertise (Continuing Progress Branch):
        - * +15% Production toward Buildings.
        - * Cities earn +10 Culture when they construct Buildings, scaling with Era.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Fealty (New Branch):
        - Fealty enhances your ability to defend and leverage your Majority Religion.
        - Adopting Fealty grants:
        - * Can purchase Monasteries with Faith (+3 Food, +3 Science, +2 Faith).
        - * -25% Faith costs for purchasing Buildings, Missionaries, and Inquisitors.
        - Each Fealty policy unlocked grants:
        - * +1 Faith and Strength in every City.
        - Adopting all Policies in Fealty grants:
        - * Unlocks building the Red Fort.
        - * Your Tourism modifier for Shared Religion is 50% stronger.
        - * Cities that follow your Majority Religion generate +3 Production, Gold, Science, and Culture.
        - * Allows for the purchase of Great Artists with Faith starting in the Industrial Era.
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
        - Private: 30
        - Public: 30
        - Rationale: CAPITULATION ENABLEMENT: The Inca is at 84% war weariness and our military is 8x stronger. With the Total War policy adopted, they are primed to capitulate. We must raise our relationship from -100 to 30 to allow the AI to negotiate and accept their peace offer/capitulation, securing the final capital for our Domination Victory.
        - TargetID: 2
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Late-game military dominance. Unlocks the Nuclear Missile, Guided Missile, and SS Booster, providing the ultimate backup options for strategic deterrence and final capitulation pressure.
        - Technology: Advanced Ballistics
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: VASSAL MANAGEMENT OPTIMIZATION: As we prepare to vassalize the Inca alongside Russia and Austria, Iron Fist prevents vassal rebellion and increases yields from vassals and City-States by 25%.
        - Policy: Iron Fist
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Happiness: 70
          - Production: 100
          - Recon: 85
          - Offense: 95
          - Antiair: 50
          - WaterConnection: 35
          - Culture: 5
          - Infrastructure: 10
          - Nuke: 100
          - Air: 100
          - Mobile: 0
          - GreatPeople: 40
          - Naval: 95
          - Gold: 100
          - AirCarrier: 95
          - TileImprovement: 100
          - Diplomacy: 10
          - Espionage: 25
          - Mobilization: 80
          - Airlift: 100
          - UseNuke: 95
          - NavalTileImprovement: 25
          - MilitaryTraining: 70
          - Religion: 10
          - Wonder: 5
          - Expansion: 5
          - Science: 95
          - Spaceship: 0
          - Defense: 40
          - NavalGrowth: 20
          - CityDefense: 60
          - NavalRecon: 60
          - Growth: 20
          - Ranged: 65
        - GrandStrategy: Conquest
      - rationale: ECONOMIC CRISIS & RESOURCE CORRECTION: Setting Gold to 100 forces high-production cities with empty queues to run Wealth and construct gold buildings, resolving the -900 GPT deficit. Lowering Infrastructure to 10 frees our 7 Builders from railroad loops, redirecting them to build mines on the 6 unimproved Aluminum tiles (supported by TileImprovement 100). Offense, Nuke, and Air remain at maximum to ensure final victory.
  - tokens:
    - inputTokens: 22103
    - reasoningTokens: 8532
    - outputTokens: 488
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Our Dominion**
            
            My focus is on solidifying our control across the territories. With seven of the original eight capitals secured, the path to ultimate victory feels within reach. I'm analyzing the recent briefings to strategize the final push and ensure complete dominance.
            
            **Securing Inca's Capital**
            
            I'm prioritizing the capture of Cusco. Despite our overwhelming military, resource and infrastructure bottlenecks are stalling the assault. Specifically, a lack of aluminum mines and forward airfields are preventing bomber upgrades and deployment, which I'm now addressing.
            
            **Re-evaluating Tactical Approaches**
            
            My immediate concern is the stalled assault on Cusco, exacerbated by resource constraints. The revelation that Arequipa remains Inca-controlled prevents its use for airfield development, necessitating a re-evaluation of staging grounds. I am considering a direct march on Cusco given our troop advantage, while also investigating the AI's strategic priorities and our critical gold deficit.
            
            **Addressing Financial Crisis**
            
            My current priority is the severe gold deficit, directly linked to high unit maintenance and an upcoming World Congress vote. I'm exploring diplomatic avenues to secure the four additional delegate votes needed for a potential diplomatic victory, which could swiftly end this conflict.
            
            **Analyzing Diplomatic Threats**
            
            I'm prioritizing the upcoming World Congress votes. The "Open Door: Stockholm" proposal poses a significant threat to our alliance and delegate count, and I must block it. I'm re-evaluating city-state influences to see if Lhasa can reach 500 influence for an additional delegate.
            
            **Clarifying Delegate Counts**
            
            I'm re-examining our delegate situation. Lhasa's influence at 459 prevents it from contributing its full delegate potential. The "Open Door" resolutions for Kabul and Lhasa are also blocking alliances, limiting delegate acquisition. I need to confirm how influence translates to delegates under these conditions.
            
            **Calculating Delegate Impact**
            
            I am reassessing how city-state influence translates to delegates, particularly for Lhasa which sits at 459 influence. Understanding this will clarify the exact delegate gain if Lhasa reaches 500, and if Quebec City's delegate count can also be increased. This is crucial before committing to a diplomatic victory.
            
            **Investigating AI Priorities**
            
            I'm analyzing the AI's build queues. It appears they're prioritizing railroads and improvements, even with ample resources and construction queued, potentially hindering mobile unit production. Their builders are all occupied, preventing mine construction despite having stockpiled aluminum.
            
            **Clarifying Bomber Reach**
            
            I'm re-examining bomber range and airfield proximity. Despite having aluminum for upgrades, the Cusco assault stalls because Winchester airport, even when built, appears to be too far for heavy bombers to reach the city. I'm verifying their exact operational range to resolve this logistical puzzle.
            
            **Forcing Capitulation**
            
            I've realized our massive military strength and the "Total War" policy adopted this turn can force the Inca to capitulate. Their war weariness is high, and their military weak. This bypasses the need to capture Cusco directly, potentially securing domination victory by vassalizing them.
            
            **Negotiating Capitulation**
            
            My focus has shifted to forcing an Inca capitulation. I've confirmed that vassalizing all original capitals grants a domination victory, bypassing the need to capture Cusco. The AI's high war weariness and our strong war score, coupled with the "Total War" policy, should facilitate this. However, I must adjust our current maximum hostility setting to allow for peace negotiations and capitulation acceptance.
            
            **Refining Capitulation Strategy**
            
            I'm focusing on the intricacies of forcing Inca capitulation. While our military might is undeniable, I need to fine-tune diplomacy by reducing hostility settings. This allows the AI to accept our peace terms, leading to vassalization and a domination victory. I'm also reviewing builder queues and aluminum mine construction to ensure all paths to victory are robust.
            
            **Adjusting Infrastructure Priorities**
            
            I'm rethinking our builder focus. Since the AI is preoccupied with city-to-city railroads, I'll reduce the `Infrastructure` flavor. This should redirect builders from railroads to crucial mine construction, especially for aluminum, and free them up to address any stalled projects.
            
            **Prioritizing Economic Stability**
            
            My current focus is addressing a critical gold deficit. I am implementing a strategy to significantly boost gold generation by increasing the `Gold` flavor to 100, forcing AI cities to convert idle production into wealth. Concurrently, I'm reducing the `Infrastructure` flavor to 10 to redirect builders from railroad projects to essential aluminum mine construction, resolving a key bottleneck.
            
            **Adjusting Negotiation Parameters**
            
            I'm focusing on the critical step of capitulation. Given the Inca's high war weariness and our overwhelming military, plus the "Total War" policy already in effect, they should be ready to surrender. I'm now reviewing relationship settings to reduce hostility, enabling them to accept peace and facilitate a domination victory.
            
            **Confirming Victory Conditions**
            
            I am verifying that vassalizing the last civilization does indeed fulfill the Domination Victory condition. With all eight original capitals now under my control or influence, this swift and decisive path to victory is confirmed.
            
            **Negotiating Peace Terms**
            
            I'm now focusing on the final diplomatic maneuvers to secure victory. I've confirmed that vassalizing the Inca, who still holds their original capital, fulfills the Domination Victory condition. To ensure their capitulation is accepted, I'm setting our relationship with them to a slightly positive 20, providing a balance between willingness to negotiate and ensuring they offer the desired surrender.
            
            **Refining Negotiation Parameters**
            
            I am adjusting our relationship value with the Inca to 30 to encourage acceptance of capitulation, aiming for a swift domination victory. Concurrently, I'm setting our next research to Advanced Ballistics to unlock nuclear capabilities and selecting Iron Fist as our next policy to strengthen vassal control.
            
            **Confirming Relationship Dynamics**
            
            I'm reassessing the relationship values with major civilizations, particularly regarding our recently vassalized ally, America. I need to clarify how their "defeated major civilization" status interacts with our diplomatic options and their potential for rebellion. The existing relationship with them is set at a positive 20.
            
            **Adjusting Diplomatic Standing**
            
            I'm confirming our diplomatic approach towards America and Egypt, both of whom are now defeated major civilizations. Their relationships are no longer a concern for capitulation negotiations. I'm now focusing on the Inca, our sole active opponent, to secure their surrender through adjusted relationship values.
            
            **Setting Relationship Values**
            
            I am now setting the relationship value for the Inca to 30. This should ensure they accept our peace terms and capitulate, securing the domination victory. I'm also confirming that our current diplomatic stances with other nations are no longer relevant to this immediate goal.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: FpalSrxFlf7V04GI
          - toolName: set-relationship
          - input:
            - Private: 30
            - Public: 30
            - Rationale: CAPITULATION ENABLEMENT: The Inca is at 84% war weariness and our military is 8x stronger. With the Total War policy adopted, they are primed to capitulate. We must raise our relationship from -100 to 30 to allow the AI to negotiate and accept their peace offer/capitulation, securing the final capital for our Domination Victory.
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19Ezfzc6XbZF5G/U4uiHUenmuzxDcsSoIljx3XP27fisBqg7wCbkGU2lwfeTAF+5ieL1qKOfmetlv80ULpK84V0vmp3oiDhI0USXgxxbwv+OftNKRTu+BTLRt/JC/iMyQYYL3YKpCMOvvl/oCufviO02ZMf9i1YyaUdhOaeFLP7OCacoUvEkPrrk8MuU9uai9FZrGHpldIfXNVpSdq7qyO/74K36+LV3P2gfmjacmnq+cmPaj4D+FDlGAq6+BKHy2KDFRYK/YgbsNdvf37uCCM5j2w8DfJ6jtOmTtplcICPn8efuVCDwgqisMZKmULyCA2dq16Ud2fOlozkFjGKjh8dg6o7iiQhqKHQ2GoMyicpO78vItZz1xWYVswZ+1zUTGxPtd9M10WIRdR+qhGjn3KhuPSyd0HrurApVnNJxsTyooBYPvZO7f51UGGzVLmAML6a+4EUAxzZSieFECfx0Jhfxq/gj92yslskZHihJDCJKNi4sHbSw+A8jY8BGA0GQao4V0ueYELyrehstkLqAUR4hBWGHRADJX0xZiwdcqElbOq+NJLeaH3V7XkyhhEqqf4E5fVyih1r91VgIHV4nXkErsNgrRMBpmtvD2GYLpk+9G4Vll7DdILp+JzDQtdQ/EG0htDEpiXLqyxjTQ+ybJk8YORrFe+yGBZet4UDbCHPbj/K8w2f5sxbh9pm/h1/KRDullDWGU65Smf6UhephDErqbpDTduresFRZDpwsrHd4tFWWOYh8R35xTon5V7UDfeqN5MPbSLy0etZKkYMPVW2AtiEXra1WgomlWIgWqoHUlz6oGzP3jRR8rGFZ3qBdhMGa29RG+/WqU3CRWHJpQcgTUmg+sRkDMnOoHeRufChjwq5Xmw/PEcYJ/lOVxYcw7bqircsAqEQ2MRDTtySnDkucv5fC7QDYSTAj0G+z2u6Q2fcJuOT59lPTH9/wh8cIXN6tVxYRB1OFn9jO1f9XIytPjcCZ9ISR2jJdxw2QbvKye73C9QcqZOTCx7rAmPVh4fjkN6niT4IIrbanrvei3q+YHrzr6NdjtZZjZYpbYbVdqF9a4WErUVjWg0q7gTX9iRc74u7BmLXcenzItzvieD1D9KnsOOGjv4QKUXaQneU+mYX4+5PNMlJV/J3q3enIy6of6fhglWOt0fwkJZRVyxWrtWkmauyeg6IfT0ynAWYgzQmDECkcl+ElWAu8nDwUule7a5pFEC2yxng1AysV6L0jZvsnYu4OR9t3VmH+l4UzbBuT/lrvPDbSDBFzIcQ57Y/Yc2nhoNGgaNMMArIk8fzDT0rUb+bBRFOD/zI6VyUyUfLBmvo7K0vypGaCfUpCC7bEmm94O9AX/Xia0kaKFXCXum+dyj/oasGCjQJ320d4S6oHIY1nuLz1S3CZfO4FsaoTOM9RZHeZpEyR2Xb0bkAf/fsFsQ9ltsfVs4l6bJuYpcX8fq+ZgApW2IN+tXUhnGTVcvbk/yq44EyWqYBSbzslPSRqaRWE/ekQJyHc4pGF4a59N6Mgr+x3z+5tAHpZRIwTs8rWdmHrK4tt0w7sZEcAK1j4W1eQJh3r71sVo5uFEyL+aLIkpLorSeSEkgFz/WZngyf4Gve6NFobEk8eLzO3pfmYvEty29Efu/Xx5c6kCSkL2nOCpG7r3onXsbl2VUVyjTX32Aa/Of+txugEdGRkPMLLJb3r1wsFcNBXgWIvr08pi4DVD3lLjmKFz2o+1NnMwfxR0UZjV4f9QfIeedqP86URnEVK6pKII3kb0QYKnZP6ZRbrkGuqTWHDUQwhqd6o7QSMeJmyvANCgEKhsIy28wJqmn4oTeVpgqKln8Xof6xv0m1Uxpacnx9fbNSaH7LcVqhXNUYMz1Pe4vIGqjWknp1Y5albYePeRp4+XOq3hBzCd5Brhcr/NyAsDAwF4lw627bURePeF5/oL8uDtNtm0EbSWuBaKxa4kwL9mgtOLT96ZABhZtm1AZqHK5rWNLsbykqtoc47aAejgVPNjtWTmfngsmjjVkKxqq1EcLrFGGp/1BMMAr1ZXn4HWb4xAPEXd4HP+y3IdnTc4rwDFJAJrjlbXe72mbc67vrmE68My87SdwvVxHB9cp6iY9+KBY3PKSYjREDinQrlIcDLTpCQmKoUOlnoYCNyPJR4vsGxIzr6ZMdR9sTqRaCUdR6yPtNWBmiFXsBugP1mjuJ+ePRF+gbFQRbND3TisYErZ7Hbm6xb7+jfPWxAoPEEsKav68jeUv2QV/fh/zsdBWoWhYkDq8Vm5ES96cnwXruFxfoxVwaSRlpHMuWea0uq9mWrGBRyE1nQ+WedXFvE5DiFGJQDw2TVozvpc1El1r+sEYNGbV2mPMp8uP0G0OZO3Sh52SBGiBtFS52y/5zxGzeVysppIkRPdsspGPzTllw2z7ps4rdPf66hMY3hOPRQBZUUqSC3yOcseKDSVrv2EDJEg7RKq5VJqVQLCxFcxi40iDc15JQyYFX8fKIee7AObo0pCcA4jp3nn3XqVoSGh5ykLNBMKgBRlOLUeN1SzXEFfixTf9ShNG8uY/HhtfpgmzMrNu8JR+dFLvS17+uZ1KY7E5jZZuM2BRIRmAjp1rF4r6ijOCCOUDScOPeX9ziiRJ3ooyEHCixoZMFHSNNUjcZvtzdx94NTrHvFpRhYbCj9fKs5pI+Jj0koThw4v2G8XgeVAWIUVl6CdPqlPcyBYdJj2Bq0QBx9bzupN95yisVVaTZxtRurgDxFxMn8RrA/ePcMGG9QrdZXfliUAxNCA+bMSQzjH6MS/wKTZYrYYhqBG8vvaRkAY+LdHyPmwCaJDN5OegMoNiJhr4+Ror9OoE9epHuPHcrYTy0Nc9xaHFdXDYqCG7eIqbJ91os8NNWSPxfTT9YjlFHL/SotrEckKl9GPXBk7BqY/9N4O76i3nuOC3uVioKKcV2xPy4AsCrnY6PhlXl42vnTrKyWqtCZRSeyr+E5ZKc4/ZOP4ruZciKS84DzbZeUCoE9HFdqffRVXUH+pDQNYC7Y/6a3V9Ek0NbGB3JV5ZkWXISorLRQQvBWS7w9pOmOZTf5d7tOVoScEL5IcsV7hNaxQ0lABlhgq+B7iAoqc+h8SITfXoycWHDbwUMqXjgmWU7JeO4Bga7VqbP0U3EOR22j6GLJX4u6hxxKw0AVOQj446wI/nOJmflmia4gNSioprx9KycJ3sSzaIvTRD+VYhoCUIQiXb3gFRPhYFIe6aR0O5pAAY8XJUZkNUGlg8v8qv7UIbSPlX3Yo2+YsjPcWnt/j/X1uSmj0iwrX2mgSGmVVAXun8F4BiIa2wzyY4Th8DyIiOAgq6kREBgzGPfiLUbqTOr3hRhPlrILU5SCNcC834b7qL49Vwj2vGGOWni1GQbEqHUQ4amg39OZYmPzWOh03AAaW8BNxAgyXtCEMfjhwNQVzyTqdDby1yj3gw0sBBoWkv7A08H9JW0V1m5Dqx/a4h2cu52jBwPMOvuONNnYS+zfYNgjH0msCO85xQhYSbpX34NXCLjM/x3Ge+lY4OaNJJrMK+2EcgskyXhcy3xQQVj6ZOqDf1ohw5n2tQXBIIn4KHhIYlOCXMA8Kh91BRee2u6txKrJSQQ2mgkOrDSsk7q9CrjKcfYgA0iTC3MU15eyzAZlmudgNaDx/rwFpMbCD10fQF2zDkv+W1LYijTg9fauba1GsJS+RRbc7vCRd2x+Iga5Tr41sW5m2JyxDnxiqYBLYOe2liEt7Ud0Mds5WgR8o6JIPHpIIPJ7kfmlWhmidZyAnWdN1Z8QPqW5ughx6grh3ZDMXZC4nGAgVGklfxhotB+lbrOmYRZYs8do2IPaYRZ0GzLKp4qwk+RJEn6v/EMHLgcUbIlJmXODkLBnYZ2FAwxto25W5NfU0WOtzp+SFZWCnjJRsQlhTrALHJksOe0KFpNt6bm1OcdSa1skGcgOdb/FYehO503aOMr1aH3DIlbSRc/6mJJmWlk5Sji9xLdbXXZKKcM9OCDJHRvsngfMh7GiyR6IXw1LFDHa6BUTXJG999hsJhYZuqljFbLYpjGlFACRyBbtMsLB3K0ffPwhuoord9mEyINm95uss+iINg0XrDIPDlfjvl0QsXMYclRE24OCDEVedLLB2xQw3auKdSpspH02JGUXXJ9tzaJpF1+d6wIhShLdCqyjs6UxjOwrOuTX2n+8YTvCewhURKh4wd2CkJ2II3oSMvpMxqs9mfgsoRuyB8rqHJg+2qPjzaBe6OeDLqtJ92BlYxsc3qwdmuL4EaFhruI4tdFs0aQgGzrwHzqm4EFOeyuoNcmBJOD8OnKwr+PLl69rV4/2mx35g0OwDvsKlkRTJaRX9ZIU6mZC2o7kLpCI1LGfq1BSLhe01W1AGUZS/9EE0TfpbVSiYN0/QQsqAQEQ/P4+oFnvhhBpR4uhR1JGd78bHhMtt3jUhVL4yBeZgq6S0SfscqKncM+CMaY3GRAEAjdQo7qEU5OyGgbLpqqZDbXS1uvm7+lvi9NhZ+DLGbslPxtvgQ4HJctlhWqQ3FK4UViMWGiPAlcG3N2IDsO5gUvYznIbr78ATGr9UjbllroxuogvO8CYtAy1hfZk1l7+1aRRYD9MAIwNERG8NFnK0YiVOANcYQS5nBUTHbE8hFdOFjzTZqiagvKcv8bkbhv8TrsFP9VkpYnt4nW14N9hUyNRduDEVsfBacaQLBfrmRyIj/x2AowYxbb4m/tsCVj0NFhGEauQue/4NNyLuyGzeCIpFZoQLQAFptcyiWdFYyseymcLYsCbXGygmvvHnkIM/A82Z0zoFfjtBHoQamAFcueheJwghMNXRNcF/aiW9TmDL9s+uv3VXGLo+DbSPnVzqfGjDHV7ACfAb1EuBRxBmse1ZIVsAW/b3cgrsypXXaVcPMg/PIDuWqvg/bx/sn8uwT1SdrznZfTlCF7Bij/Qi6CsaMClPFvcxDH2KLUkHDk2+P7aHkioLWuHHYPrCWfYcI/8hET2+94RGhv8ofEgLYEobnz/LwDePgA61YL5JCGHdsPuhDvlUUMWhQU/zPV2kyOiKWWUjSVsevU+VpQOzlPN8DExk61F7JdSniZRv1kAPkGD7E/OdseTERt2FkSGeDe9mue4YFQ2vvZH0ugjM8C0gt8PKvSOHMhVsQ5AkRpilq2u/bdlyhBzPE8aWhr7Ib/9saBJuIWSzSHiNj8T1YvvrPpY0zT6j6q1S3xuurUONBYuFxvx7ky5FugBEDoY1UZwcpMcfgKN9E2sUE1ZkIou22jGiBlpLR92BhhmkRw4Iir95srYSA5YUkym/UMpwQdwOBy1DXry7MhHK2kJUZCID5+aDrpoMftwqPyOdCDtRXgivJ7B5a1U20+0Ld5uJ5VOmdYC5m3meFtEcr+f5bOzbmkOe9wqbPitd2amsx1pnjHNTNpcxBjbfhx7wTTVp75mPm/h4ZEMwvrKZ+bAdpCn2oD3VlUvS2UsV78rj0Ah823o+gjno8uX71S00pq94TZ88FKgWfIPcnCMT+772lAuShZLZel9yrPwqRIg0Vx/IJ4h0UxBRA5iL1DfsqRQozlTbdGL/MoNdOmtaG4LHxqm2t3lfdruy0hcu+0C9cUL80vGTqbgbvHGoMGv2coXGqVw797xc6BsH1ZacGHEWn+zO4k1FzUUvdVNq9qDb/p+pE1EvDpArrvZy0nOmDMr9PKin1vtGyLXoQXCmyhOKDe5YrARwiSt7d/MxJho1eFHBlb8He1dcA1PEsZCUaI1R5QQUATaj6Bj8aztN6/EkvHs3QhXpyVYr/1TgF+0JXELJ4MfSAS1lhFgYgD7RJdb/ZOA0thNkE0k/p84WTkJN8LpA6oHlzxX1h0NEdCB46utg9yuBUBCL9bTNAPemXD2rLuNZqVPWHqD9DDX6+ca+0HEKo7sF7Zzxdrtnj+gVh+vaC1cDVit+xDHz/bJCalYBqrkJwgczfk7PJJ2g7IxHPnAAx9QUBDq4PH4bF2xGeX9LUMhQv2kpWttuU/DHMrF6qqzJUJ2Bnc7MGyCoASNvGwQ6+lSSCtjlhJ2wl1rZ+aWcxUBFibKDKsPvz0AzJf5fOU+OS5L2KuHtixsUA4xgr62xGIGqMBhhz/xH/DpwirMAmHctXGlgn+oGlzAptxJsuLshivc1/IOg4J1zmS/ZIGTjxVGmQ0hvUyW4mYlpjMFmGR31h0ZAENPGHnEZ8hzUWl0t3x6rLrNZXnXA96eU9JXPgla2JDvDOf0TW37gp+CoZmM7XVKsLLnCX0r0NdWtbcEwNrRs7PwqFcfVM08HkvtmdfVMxYPIFlblfhMECPPyb17PX3w+qqkwgW8vnMM+Bnc84DLC3LmmQ8efaEVt5q9tK/4ol1jMgX/oVyvsRUOnk4u7f38f3ppTNF0GsHmS0vv4gW6x/m3lowjM+dENIfGydnsbCQnws7ZmmJvdatNw+VgrMAIHZfANXUKp4WbDmFobNyS34AvwQ63SBr1VhdPYeEBXhZGFoLnZvmfCt47KLt+jWPgpFKmtSnnA4SvmGZwiDH89k7ro4921kCSRGmIVwz4KqXiAzw8za5c1clYmI30pF70jJ6u0zoUd7ck8uR2KKU3/nriWLU8xCr00yJ02lO1J06ujYYs3OQ6WPWeJBiF3rvTFs4YVYzsWwmCJldt3cwgZ5JNSIq31NAcIpz4jxdlGEmQqlUxswB4D4Gc9Qv+5mbJFEedXoah7x2GwuKrLAKoaQGuCksnBS2HjztDaCLPUnSQ8l9GaishRcHqTIO04YkkRE8rruZNGLv90l6i7OlI2HpMSQ6YxPofvrutVBLojf7GtwN+zjuPL6NI7zbmcSKWk+XjPlkPlcs+exFWx6SQlfoDQdGv1Su8Ll2cQbNEoXzYPjMnNenw7UsihLfq1eVN91BklN5yscnd3Ez3M3jJgzNmGzP/PKUnAXcEhtj5lCGnW2te4PTcJ3FeXoNDO0vsnYCxoT2CGViOdwqsdA3I57/CAC0PthXMbm7SYr5wzvSVSPpzyxJlaQPrYB6MVLK2wYEhrdL05V1yKB+AcKAkym8AqggIUFjPNQWH5fNGlIBWhW7XrDJl+i37AKEfbOW1DlATlg4KLkwe+A7OHNRgVwkM7FPQDaEULQxsjofvA9vG9NoevGXMaWsFQyflfE1psBwz03+hNkL5Kx2Kn9feYyv3gri5DHED++JgKsSYW7uIJc5evmuW+Zmwq0PtaQN5CoyELWbxeLwlQ4l67PSA/v2OyCVSS6yw72gT/LGv96KFrbaaIN+RGUHtrXLtcd4tNQHy02tJijJUbF99NRcbwbwD0dLBR1d93icn/pGf8R6YB3IYcsYZ75tAyLJYx5hcSnMTQb7dLjaz5ZxXa3y1QWIlGZeUuosVpD74dnonTFCzdi7as8nf+Mu101uGFcYgk5Pflv5LpmvKc48TQvrXO+cH1pWxJrubbuqiDZ+3O8f6oPCUKUr0P0OSJScHDMk6AC3FOwu6mZ7Iq2kGNvzDcZ7z76QqK7DlXvhJrqxBtv13KM2mfp+vUIiu42ayvNpriTMUS6ugyV2fTpGSbw+hclBjBNcUte9ZOGY6m4RTQvb07UfpQ7bSXT+weDQJCMfoQPE6epjzGGW11Bcz2V8Jljw28/l2aL9JZLBAsZiIzOt6Kx/Q+p1psOuy8b/SZBWZdudW/PJQM8cf7JCkZ22SHh87w6C/BlZbWOB61CMvipmnRESd9iJp0HMUkM9oY+wuqs2WBggroW7ixudxZKB3Q9OZh8iQTvcmpKXN7n+GYoyIayLW1+xZt6EAfer1uNLWvRuG/7XMN14vIbX/5zP6kWHr5Jsvp5qPJWd2quXP8CWIY/9sbSO4fCH+5pnkFXC3EzFYYidOkKPUl3vabxMfRmm9Xf7qh7ktUJ9DPWUvsr4FBTb8WTMEI3Nl4B5/axzDG51Q1XWa/Dn15OUpoUfLtUAhMhh+iPORvDiZplqlrAV4ESuRNGBZ0MzefatB/xFzj6HhK8/2LVAmHOMI8T4+EjiFNGyhlSbfKdet0mLRCWUbJNsaq1Ez3uPMYeC3DjgZmrLVhyEKhdRaEbQEyyL1XwjRQdQOslmiYXvMT7Aored6oe95SBxyADEfNFYLdqFp6W6u2IMBDejqEK5lB5n4Xd7xg9T33GdaNs/wgSV9dCjqeAJiz1Py5Hrg8JgtNVjDVFGHGkFyF5pnTNiO5uthLTwez1Tan2NVON8lUPnBHdeOJDrCIhEO8j2g4MQruB74hd+HB2LGdZcGBK7HKf9LDjv6guM35X8Hps8u0YlQHoGI0WLnwByNssFvVDBnIlsF/7eqCXn1FPZ2OM6+Zo5c74cfI2iPju7ufPvflrbAd7RE3y7Qo37TXRr8KZ5rLSQGxybju0/m6SrjgcGDoy10JJsaXtXwQKZU8OMiAXrLxorN+6oZ8KVvj+Z3QKwvs7PJBotYQZKPncJItLSIflk7laEhj+69ULI++bP0jkIjpGIPdVBu1X4YsoECmTVNlG1OjXpUNWEicf1hkYfsk14hNxGjSL18fqLLi5Yw2vXvu0j4NEZc3RjfFkUOlmlLWrZC80U4HLMQ+PGwuUaxzO+Ev3d4VHgyPWtKImqCy6FlttJWXynzCq19V52RA/Oe+4Z9uV9hRGkIuuxoUlu6to1DJwcw6HqZzKdoWszYCw9W/kluARXD6ZdsSa3TrLMnlw7v+YQ/uZENtdxwSlQ6q//AkriEowvTg2asfbwBCDhGjAEVmy1dcBjPLiIMM1X+X7wj572ul2eioirlmY0kQ/3EVSch8+Qn2H7WS2f8bZ2/llP/QhcQLvPWTyCPp9j2ncuWSppfmQsEYc8RzzfiCTHBY6YgeKixICm2VK609oj94wZ1IGHUjvIRRCokh4svphJUecLfY/mZkiJRFsiX3SxeOyCd73XGX/Ucc3wrLQM+U+YNgKUV5svuJvELMbhM6FKFGpW4uq3u2uHMRsRovAXX7FkaensrsVD/7zYkC+vrcQmvDLs6Jwu/InxTdYm1clGhtdC2fbIdejJnZLUYzWRLLAe06bKFiKS4qB/9Q/0OtyF1DmcCe+BJ94NeGQeWV5dE/KVazSCCX/EbaInGtDHrXLOjMUD2niW+2gtuX7ZiK/Z4B/RFQRAS9R9PdrZG7ufDDZPlhp9Bs7u+U/avjaE9rJ8fp/bcL1wgQuyPGBjB/68DxKUjL45F0nb7/W5uKkDTQ4nrxFoiJ4DmHZH/4SLZ305EZDs2onlYNSTnNndnIVWu/urJfn+liKGW1JuSgMdGtGge3/Ya6DwVyJ4F85ne9dYzK3o7W3z18L6caHZ6nxSn0/bfwh0hieaXKR2WHQxQkdK3CT3duN1t3jzqJXvHSOi6akYYeUwdfHXU+u9L9fStZ4C9N31xbcF55usHv28oivC9eyUHfLIh1aWgCzXWCJghsz7kdc2tvSmJzKP3zb5jtzaa/+2/id6VOohcqX6eFcXBjxj3qS0zqJUHMj/hYPjVBMwInbprEY1QSv1G1pejqOwW9HwJQiHAAgnXajUK5ZsUAfSZYi0Wul1Zope4cTYjJKzew6fvcGu2Zz9JWZ63plrMiu5MuOdQ5W4xpEaEtGYuGq142jXUkWMGG2Va/r1VoAGs6xBzUx4ugXBZ6DuYnlxICxtV6mqQXa905fkN/Uu9eBOrrUmUGVG+6mD5MFxMK5NXjYfRODLDLF7fSvYAHM0k2Ikc35GSf3j7yjhRSMvCwPG43/mKhW8ahnwfurYtWQpPP0gLmgoYnUj3KE6MqyGtb6liKX7sdoaRHPOJgCvZRUl4iSg/aM8+bmrrOp3HtgUgXJS+BIY5cr2h1/9MrFaOfGaZi3kYBDu2E7KfUsEbvrpIV34HWJdr8kaxdww0YnQWRU115OY/94D9O0wBRQhD1wNM1Oo+hHVq5ZuwoGtyPXvg4bwMjxSXPGzR8gc/7wq6y/XPKgSkWyHHa6ypPiX7hnhZmRnQc8SRreG/3xqPiP+PaVUPWUcZU1FT7OM+uGrrTuRDZCtV2IiQMfZtSlIH3WY8PA17aPcsVoc+6NvtUtBbR7RY+hwJDktO2PWRD26w/7bdgslCw1/xEUFGfT/DkhVkyEwUZAqMJczaVZ0gppvO4WRyFTmnUz0iBAvutOPQgxtzhcCYzsBe0RQlxp25QvjoIXoPis/hy4El6m2qmuPWJZ+2qafJ+EZYTAXrRmBitx1Dyd6q2doe7KB+UrvEOWZo7DfVrLWN65H0mvVyCAVJ+ZKiuDLgWSZ2q3VMXF+a1pT3JGLefSU7ZMRYxC5z1ban4XVYQkMMT51eq33lHcgcAiKGqt93KjhOpYGEODUntxNekk/qsJtr1Y7bo8CL/YR0dbnMQOrLIk8cpe4UcrCnR5CE0ZFTkMwh6fskssTzFBHXYOW84QQtgcObi/ui/7VDk+3+rHMdlSbKrh4Sv5LAppr1jDl3nEJ5Q3Pn9LGQ4vcn1kMYmtHpkCzK8UnLPjTOnft4pr1ofBJRjcxx4TgRW3m7CvRsM4FpPk2zZH52t5nWAfghmG+TknUer9gj1+imIhTApuGC8u6YBbkYNamNsEnzLefCOwyTHiidc38twYZOro+B1H53rUNCRFRwPxRlwn3vbfGNXSblzwLYRt8yOkN7FJnq2p4fsk8BohyKe887Dm4/lKK2KHEEIImCEzhUABvRyo37/Q2qv+8+CAbA+Ll1/2TTNod7s8cfU7pI8hlAG0eEy1joaWaPKRrutYOHiJqxC4XtMCq0i0CWqVLJfrmiHZEQGDA6VBOuRDxtUfJrpcrR24XWK3te14hku3Hx029FfR8alnFQF2sK1C4J5fZizENWWG6UuSxI0HmmGqFJZpiqIdOdMbcXfsqkKxtl/hVn7Kt1FoZsRDgkEhxGx6IG+hmszP7I6KtIvvafG7exca5HHFO2+H6S8HIXGJtYxpdF3ikMcKz1FqWosBsHGpV1XITnEEgu5SmzcGiLYZjrUGTfuXZqUKaoegCGgjLoncfKFSK2ziKw1+JZCzNqEy5gwK97sHyr1qLoskc2lW26tNhtTzdaNbTFecmf1pdcZOL/Lvkxxgk1a21IrLUJvK/GKmjg7xs/WD1j0mFGjxy7veyTb8uDzEbfGN0e4HwVjTY6jBZuScDQMgQKdPS/uZMdo3z29jPeS+/wBordCszhUwTK6LbWDptgp/djBKXJf4vY9jhgaL4T0URFKVLOy4jWr9ggrREDGtKWw1gy28O519h8i+XIKJeuWCKj24PnSTnCT/uxXgLuTZqUNLbhZUCdfjuMDXpRO5USliLc3DY9fsQM0/nGRguvKHM3dWNfMPBhi/VZKexGjNLZ6gwxMqT0aOs0nlLqP7cTrNTlJf21FM6R6NB2xngn8KGBznaUt4fLDYby6qrQsgGsHP8oYTOHtAOZmZj07SrDGbhLVoPcz4bPDxqjJXzUEZnk3QPCURXiQ5qEbZRVCgBfuab0jzmDbcljU5zIoJiGKezE0la+zHGYZZWEDAI6QS9exp2f33moe8Cuh+muOvEwsX8f73PKM4aBiXHhoqwRWU7uNdbBKD3h/xCwGMT5aqzyoulZsomsgCyO0dA5X7OxFjBwpg7uuLz5anXREYSdSxgXbyNB24J69xYmA7nJOn6OkoIRa8ViuBaqNxNQN78JByaG482vgtdCg3rFOd0Fgqin0BVrXCVs0/ttCE2F7KVPAGJ/7Ng4vAUNtjYmSyxZ39pwCyZaKd15Gi5s7O3/UaBvBzJ/HGRQp2qJsehlBfSXbtuartHCVaXbiqDBu3wOLJZHjGfovIR7klwo1g1g+j4yF/UriLCbeGprkjZe6b/jubpzScdhUE6tr1NVi9JmkiOIPEQWaFQywrFSH1c6eYVyPWdeWmwxPfnWJecmtCoICplxSmr05f233jXoLCkiEs7t9AaA62ULgKplNF4Jma7cRWgYKVsUH2qDpb32Hcs2AsNmuGcICNzPFueCHc/K8S9XMTDIS8eqUDN/TJ8efnvjjRZ8XIPAC2lecqemy1o6MTiKpkjy5LBwzlJ/UsUu2YqVf+UilVl1C0NBs3eb7huPqOmn6gLTIre5Yp9TRKKPLjHIw+adGRWt1Kn/sE3Qxm0P8KYh42dx5DziC02NXxCsXQ+ubIMjOSXG5wS7nj5O8xnnvowmJOi6VkzqIPezsaYXKElgXOg8JZlAowqmOA4lnVoaUTvq83MfV5ZUFPnjCLJDxeg4MgWcWR6rllmT/G1LInWE+8jfP6wSysqOPqyvCQ1BnCF6693aKCNLRJKUVKSqKn88pYjISKa21K8atzfwg7bghgrCgQNjq+EjOXtv0Hs0DOh8dIoT/Az/OOatp7l3xNfTiQpnIDjCCdhiXU7f3fzi7BKrQWNRK5uvP2p4N+E2QZj+NJGGEX1qjv1fZ4kqNFv/7+95ql97QjqpWKuuOeFrkgZiEv1AJNkZl8yL4belKJQwdb2mpujaaE/57aZB5rqSJDlznhJKP8GvqboZQaOiJJUpBxYEpt4iS7NHy2OHMCkR3/zY064Sr6EUNYn7Ci2hrHtgFx5M+7C8eBwlh9fc5QqjmmYSXUCBE7H0NAIRj2KUlADs4r9H/8G5+CB+VX997Q800ua7LwwuRI/jez8tF43ISb7qoiNvYSm8fW8aD2W60mB85tIT64ZaJRJbaYKNl3zgShep87WM8ceR5gczz9dg2aVBCAzPnNBwTiNOXuNQOCB+g/We5z4q8P7QD9nH3Ks0UnQxOXhP2WT5qbAE9JvBn1JrnOhAxakMs6Pf2jSjBWHwnYacX2hTW09Ev6POiZJU3USjwdTZliDpRdBz2fCZMEW7lH9CybIRjYw5bOS/lwKKzCvSvd2KOgsi+qOB1rMgZK+ypsyAJcKPb1pN/WKjpz2tCEa6LTOFLSURBWze1rzIPGlCBIu8TrL/HF9ImoxIZh8barpf+33p2uSE13jLJEBaZzAso2rv3p6yuubGgq92EFFNAdkZmVP+oW5V6aEsAJZjK3h8adyqRDsqsmKYbO//SjwWPCNhOSO4SsYeCcTapDgr4S+9zy3yzc4K0cx1uYtceaBeDIHP9U0zWrK48JAjYxNdQQ+fEoF5f2Z0PbcX472j9u/pm6cl6NxzIgSpg6Rm4DwizpnBh+la4pG6II6qrfx+LnJPnx7vXpAZ7Li0HhDrhgpYwfhgz5NSMFHsbh95cXPLRBd+ZSJa1t7LK5+Tyt3ajIs87BrtqddI7hlWJU/m8qSHcBqWWKd9LvXks58qLmuhpvsejzKlkwKvfktiAg1M5PjODNMC1RXp8tkmHMUKeggJmA0bom7pIJxAEHEgFcm8LGwxdyxocJvjq7f6pbujXqCosd8eKdrA8/hefwLMXG1vYK+kmlEyOpElolRyPOzrQwidgmANEAO52syDD/KazCVEl/UkuMt+8VH7Us8ynpoJaXjCgAzvRoEe+a1uXvce7EoNGGwWZs1qzLS0okS69voERaZ4h2BTClh6IDHOwn7A530qU38xPpJo6dhyw9WGNRSAaEJfDaanuJP8kqK0lcHnCEFUPfilD+UlVU43H2bimPr786E7yjQFFAVMtg2CTolhIypYWnv/4VREHB8/SLPHA24ITe5+a3r3FRZL5sU8tsV1qRufOL87BUIPTyCi2ZM2rm5iukSmSULNin3DKovOdt6r0/p3Z3UVa0/V5Wi9UFXEGUbgk/rCvKPSIMg+qkb7cNmOiLTVN134mnkgPQf9pW3YeG6nE9vBPmLj10pp6osYKEHW//Z6l14/jmBHNkiDGb99YVhLiJFZVr2JqZWnoUKAmY4f/7MslMgPltsS+rjnu5VHJ/f7dUxtjg9If68Sh4n5+zXTVDaZAMnuaT2CTle00dGbYT7G/eqnYNHoqYiMucKml+wOAg8CqPKmkrMEvDk0S0q35PrVRv/YcgUrpJGe/hfBrwKuYyI7IoQe5xfZyvIkBNWVXQEzhXwyY/AVBI2tZaQkKW6vRfReC4OG8u9S6VMgWHrpq0fdRvrg9gvnSxZ9OG5BnTCB04gU7/IBJjxOnWuztz8MenWbKZun/z2diuNFJKb+C+kp3LdFA9+xlTXo8P+yueL7/W6gfws4vWIr2EeU3x4vBssF9DXAfb4mleLmluDVFPzS2C1X8ysdDsnGNqe5YS0zknYWecgnSI8alAx92XFZLTOeWIlHKV4aSEtneMgv9PyqDayf6B/YeuRcNN/jGh53zm0j+U0vA5aM/RUFC6xe+rUEquyA960KMGADHckXUA4H5TVlFJ7h1pASSahKAY53Y+tl53Z8V9Hpv+Y4qEmaFroPoM7Z+KE2KmcHy/FTa8MrSrGzocOw2iA3/T/ebxRs77JvfALMt8X6ecU5AHuigyP/Wav6T1NP+j/sa6AGpMM7mSoXeeubP/RZhplyqntyKLo/uZvTvBNdP2/80tbHRHX9E/CXscwb8jK3zmDQhDrNH3X2wVJi2NRK5IoAT26IMPpk8l+mIN0BOl5Z2MT+PGrzoLit8L5hVLFWEidbCFhSkZMGnj7cOoj0nhebibtT0cD5NS0GHbn+43YbNi2dly34WkCj5Gk3q/weG3QSzB4C3HCQzpR7/oGDsT5aEXqNUIeoXxrtUBwFVpV/AdWmALhpaRyU48YLET3s2RFQvnABh+roFMHO6e87zbphrIl+AiAhOFTj9wrCZsnzWw++jgFBePpXAPCnx2UKyATeGn0y/5l26KWEwyYRKnkDMO2m7NTODbJILfxdzn/yaV68lqUm8r5BAUpr3VeYPjiXc2gBk/pnuGOP6ZqTludwz0CocG6VKUuhIutFsS7xk0IaJjC7GMf6TX0V9ayNboXFcjJi4x1TPdK8qs/m28SEfMJDzUthAiWXfj/BycCfWULP1jOsv40+PTaR84B1CeyVkB9r3WSrBkFnXe31OhMxOl4mm96dBTs2YDKUabRjCtiAMTacOeswncpx+zQ6G3ym69jL3qdWIGaMsoS/B0Pj0IoZZc/2OXb4VRgp2TpnxPM4ZK74V9W7qIL4MoNcoh0wOO8/n/Lf6stT04aoFSu+ip5u1/n8FrQ0T3cWW6wwrI+U2m7KRlaA5qaJR7oIh0sU5WbjS4xvJOpHfPJnlDkiqJavGm1zkzvwRp/zZ8X9vFSLMNgRRsDY4CI2YMr5QB1d0vgCaQJ68GPLWvlHAYqYU0VoXj2wetqJxhG1Jayp8iGjsroviNjNsa/u0cntbg0wbQoJWrOmDDvhXR+sQ8KEECl2LvXS0crDIWYvm1DvMl6ETanrOFx8OLvqsqLobQkWQjMWX7Gf5v8PwGnsMYwHpRM8uyoHWMoM0HFHQlC2FbDh3PX6iR2iVlyIQhLwlq2pkPBpTsD1UgGj3NgagNUXsp2AUZuOe5OmdhMI3PuMeOlcmlTl6D+fc+ZT+mFVQ+Dljbd5FdRvF6YF2XrTKFvLzNzhvTP6lG/zTadRWAzTg00Bt41j/+mkAUkerQGXphADFwZcYlB2IyFc1SBW0mUJ4b8AbX+tDr07BjLB3N0yTY9ZMDb4sJEh+GXIV6yk8+i272LSBG6XbKkgNaltH6oACJ0ccc2BIN6G/voWUqZX7vnb8gF/JZKK6bDaLPs3sBoHWW1GtmUuTskimB3BlfRVLpdxuC9cSVZnlbmUj+ZB//QkLqFUxIfFv2fM1v84UfueCcyNVA8Ze0v9RuTY4Hfs2WUO2KMhtmvnoHw36hRcBUI6U4uj9AQX7siMciCIR8K9ypYuJnBXu/B5+LffTITvs+jGn2l78H9blv2pkg3ZS9o7rRzeQtqqfdmT7zPy6lqtQlh79C6aO4WusYRAcYAG85eOJibZerkJCtsXDQd2sHfRBtKTX+QopUP419uYoYM0xY+Q4miI9DJucwkGW8+jnwJR0sA8a2t2ue4nXAiyi1vHGYgO2h1uTMWs9P0io/i6pm+Mw3mpmSawK1hVrIoWMsDMQEIe3pQszTTlvkwC8NKAulNPeUMfRzRDGOUU11Yrl2BXqcSuO0XHXFyGaLLKwuk/iy/MC0GVetGY4pAUboV3FwlkC4ENtoAg9RCWdQQd4Vf4y65A18JkOJJmQNiqlGTSFlu2ASd0DrUd8QbhH/OcCK0hmGPT8a4WiZxU/5bYyxTwlapatRadEZOrZLh7QfGGUErs69wA8KxqwN1ZCC+ip9ZtEEHSzO++ZmeBwgfQdb1wJw5dSVoTg3iumnAjGJhkcUrBvYJ5++AuodtAnQ/EkyOi5U0mc6CnvSoKvuPZ24HxoYjm5AD3CDjPpsUPVHwC40n8p3I31fS8OCXrZgPQM861boAbyE5EyN9s6BdIEe/EyE/onjk+34P3F3UtNg3qvx+jw3xxjkoNzZWpCnppGmtbZARyXdGJZmZLVBYUWGkWGkehfonERGaU1keej70hfIMco69zA95iRKFzHlUMmcCx8IDyvE20Y8pGEVb8NB9Lg1hBjjetZE43xRUaSuxEO1Je2b95QY5yGfw908IrVwESluHeP6Bzs+Bmvs0FLvlA+trxEfCEN8oNgEc776oHmvS63xvxCLIjllrb31mbwVBB7MdXRs4uTDXxOHekgWSNBb4UmXEM/fVmtjuliRVvSv/raJ7+uZzxQ/KvuAC62HXzuLCkRMsxGfXV2qLrTTrjKNMO0HV9Hj2Itv+aVMzvFg+k1xLb2VorHjnlbnX8uEMwAtXuP9RFC+1TW1btfCKrTVH5qVIvOkRW2hslL0/inQzU9NqhcjX27g0yWlattT6SKNIVwwa/UJwMlR5oWWT9hI6DOIMDTX4pAh/9m48T8Qt7z5a3RUtF4q94x7v93pggcOmoM8C0th0Vb+CDzwFOzHgneVhH/b0HR8wt9xJfmfx86oRrGETeisXikB8hisn3LE7nNouBkaYOay+Z7B0OyKt8NLuN4ijIeDaxcvDGokUWGgsY2Oay4v3+pRorS9j4cBYoQde1rQw5rAWolkiFTnZ3rzrCzPel2Tucv4gcQMfARz0tboLF9srcSG+AJ+g9P6c0K0nCEkR373Q7x7CbEbcHLouhnS817UgHnwLn8z+zdsjcGh7vXdiBPuXPgiZWEJJ1OLzm31ECAfDf324jBidSHgBh3NDwhifKcFJM5z108+bzECVJAAhcmfRPoZQ2hOQ9RVNmDHJ+X1f0ML150gQbokUUv+4QUQH/Mt2UaXdpE92o453C9RlU4nUHHojMNTw4pJIW4KkB4WErO9YwdXWwSHxPyyK39qpi0wiA3tMszHbAXNQnuVo03IU9Kc0yJ92F0dNTcD1LNJB4aH3Fff+zYD47YyZSlDngpY2P0ul/4U/5I+zMiwMOiP5kvjo+QAB7SCu0+xJEfA3amb4R8fVwBix1jfR360a9VWL3ZREo5xvgDJcTqST5BC4jTQ4i8SLkkNtvaBJglRq2+kkt0SSizQxjJRQjOTAZh3t79Zsl82yVOMQtz2Cek0zFL7al6kdt9B+1bagfSLJuE9urf2OHTJvxhDClAw1vtPFX7+h4DJAQncbyYHHJW5C5DEIeDS9aK7vHIVAep0QxvOHp47hSl90jx4b2FSz/XQ4zbMperqHMJVFR2z264/6v2iWhBlMSgum87KQv8LksIJFcy2bejkxuLFAqOT0ToxMcVrJUqHjuZsEsVFqMncGJFQ7ntUGO8nPRluw1lJ8f1nEz4aN4mPNg0RKEbkoJ2uqQoAgTjoT5Od29e24cnKWaOKGrrs5WoxB5PYvnF7B2r7aFXTcNAtjTmnQzZRlJnRbTY4EeydSyfyQSI1cJlsmRX/zAddN4yTGHgn4hYMc3q75I32V/E1KGHtINAohq0IBTsgf2UL+2QFR1eabi65clEWjz6c4YfAowtVuZ3lOf/P1TUR1pCllZu4WwqaDIzpp7uf/xCX02hDKbe2fOOVR+/5t9j7RwHSMBgRdZiA1bfpemSLXMk7k05Lz+znCWAMTExZyQDfxS23zdEGuE0hhZk0AIl69ZNWDkykYpEVt+WYiIxlvw/456H/I9rSTXss3Y4zLwRboVh5OOt2G7E+c+yvAiQWebr88FHrpk/amFgXiiMH0eNozD+CJS0/yx+bEDOEwtrE2szqOAnI4m542XsXkzOD5ua2BYMhLnCG/hS3QCNKrJguF6UsJZsTaft4YZmFskfKv2NtvqgquCx731G8I1yCSp3Z7D5m0TN+CXGgRwSaKDSJmqRST2NN3ZDSI6oBiDjLMvZI/3bQpIDyCVy7KP+Nru3pSb4jqrqYrJdyGl/kD+QgJNepWX4i4+2uZUKhoB6eUkzejVMNSEAa5Z8MT3/SpXEeYLb4fnoMNaIO7zAynjeRIxKJOMrbZMMr68CQ3amJMr9BZQRz7oYazd1iwrJ7IZR6iu6a3/siZwMi9EluvvzZR7+zHtGCMzaIBewV+aNBKOdSepP48mgHnnGstLNx3MJmhwk2cI5KelDj6Xza9PTozHBESKF8iYBHQhneXNgnvSEBj9rDiGq6XvCo2cEGoZF5rduzLedmuazmGImQhUPEsRxipeUBf0VlhImBKZ6QcnV95AtZgXUGYClhbF47zqq2tFKyZKNsQmJhXEmY1NrZQJdVIoIQ2qTVmjYzjQQc3eq73cSnQccReVjS1LIH0FaUuoKN9pgLOAfS05IeMysq086qcAOXz4W6kJ9cWpzI/M3VyXngHf3lhQPAwgArnaJYsdYbv3LcR5TUS1sSoD6ezHb+h0Rw60QRoXTdq3/yZBjpS9Brc0qtumrgCx53R3BSv8GRa2RSSquKEVcLP+dh9kNBkm3bUxwY2KZ79gTYamM/AaisofnBPViB50QO5bHrWnfcLXkRP3H0/2TXDJoYMA5DI8+hAumLGWU2aRxqJSxixscl6WognqmdopnaUOE669b9rQeZk+m4qbWrI7+pmWgQgAaZg9NjVCjns/3a6+T58qJMxemiABEUZnqMKrsy+hEUi72CQBVYD0WOV8GfgM3pCcWGmi84T2e+KaCB0r37WK7PPmUMtCV9p5Up0IhqZx7D6C0D1/1UO7KmzG+ZEQ0S3XorN2hnsTYMAwp4ObV9GJGwkRjZGIpOlub89+zW9KZGin4YkGm2xUTozTESRaI2pQkKHhjec2k7PvCi6Y3w1cqRcaxUo1jwef/y5FpWY5V195lV8hWD4gxJMLp8Dwq60BXtOMTgkqj7BTITNlxQ29ZiLTrpNr7XUNU3CwiVryvbSf15Yyxgcx9kx4N9p/B6eqsPb7S4KUPLjkt3dZU584iHBqoP2P447oKG+b33GlYDME+/XdHBIvZH8v1erd4/aCQV+f6k69uDEYXXk0IL+viX7VI8fOFntrFVKpWdVuKsJq9Lbl/HQkek0tqgiwEV/ZaTFQ19PxSZlS8XF/WQsZu4ivJlOnbmJXufd1jIXNtRNm3tZNXhYPr2RN+HR16Mj8aFEsk5wkF3vAIBx9heJL6QjLxjgisGvLyMfYbdZJtfOJHMizym3Oa1wd7FOhKSQGcv3PiMGU++MnnzQMXY5Bq1WHCDqR7aa/iieIqDVUPxuf6BG7DQPWjIsW0PU6xMKNkWDX7DqyGwDankFrpcxYs9TVzc7sEtnfN347+SIeUJZnzzuKjjxqEueLEzI0hpUgq+zWBv6pxnnaVq1QX+SNbaFliTlgywVTrdzCKGa537xcyzNrlNRk0b0spS2r0CmT60giH2FJxGQZ9cLN5klZu97lD/i3MSaCB+FMW84Bh2JY2pu+JMFIP2LJUvv7gOdJ5PSTbB9Yc+KFS7udTJXQUDejvh4h+8mQ3zhVpuA6jckPSIi/fiq31U5toswqMn8wiOeT3ykXi8smdXidxc6Yc3VDnrft0A/l0pTk3KJ/Y0KsHlWVtuobwEQV5hgFiV8yJ9iDbJV2fJFTkPRpuerBV64vkOSlyiklOei1WCPtnR+UQ8MM+a/s28YjTzVBODCN6d00ji9Z7LLtDQzPbVnrjq53eDkICuygHUgxFmPYf12TzqzZnOoU+kk6EisIzfFDoiBtW+EXyjrsYR8QjqKi7BlK9i3FUaX2zBLAyCwX9zPP1GrASIf4a/mUJScYmebnsr+0AWPbaGolezsbX46MS6u0wg9cnSnIEDANbaWwyvMpYaKkzStRhc70ieQc5w+LePBNKUL1bTqEq2yb9kh3VK1guCH1qY1XVUfroZ7w9r7Ykf5PM+myvUATCuvLHaoybgqTtgSK2tMPYJN176af/FuT73nMoAFRM9gqNaXLjDl2uN0z2CZTpfCT9+uQ6UvSAJAL1Rn86BBokrx/ZzVidXTAiy0RT8TeWVRgW5vTSK7pemcZj3PnpUsjaoRydoWw41oJv1P1eqZqC0JoIqg49XxQA82mOn9Hgr2HVBrL/tEXqjIevhuzjtdVu95mV+e8ksVoOYC2ms+uBBYfogwQw1FbohgbKo4zc6JOjYRbwRM/xVc/WYIXPChwzg7W0ZJcJJcBq9wtMHUuywgVT3+dBiaY7P7k5Oy0ILGkBgp1eIPcJbDW1pDiQ4KXJBLtV5xutUv6WnExID5zHa3hasoeqfdVrE3FMYU1YVUI7C92PPyIH81460lKd6gRQALn+WMZTl8GHWk/OHM6rDy+K9YkuU7a8vschYXeH4yx7w+9DPBEHChwUACCCi9sHU1qSK1oDh6en6YAse8D/2Zqv71SnA/xtdTs+Vf9RvuHkOSpdLUXGKwHLkhH1eK9hYNu1lxXJofSmsHrBvGo+J6U/zhaa2aBeA46niwJU0U9PxdvB83i+gPbzCGkUUC6u3oZZrori3utfBwbKm1NyBY1Ea87INA9Y86SRFQN1b/TnuTnZ4b+cTjpfZQVF5q7+SWyfR/785Iw1oGd5I5eh5ucck+ae7NiAn6l+0nJBtQj8s5RonfN2y2gWPVguATSYSNqfFHGBO90MEAdlEpWxSxZPKXknAitHStjeMn7/zVpMIHFhSdxZge5XCwpmnatheDfzdp0VQrXcpLQgk8TO0gWOBFoBvuN7ggX/K2T6/YytQt0wXcqrVGgWuqeHL07Z2YAmSOVJQKcfIisrxcECLuRbrfHk11v2IlGtJn1zg7CIDYFHFlpzSExgih0QCFeq6Y7rcG9uZqO0GRyMjq+bXLGhs5oKOSesSKs38ALb/b5utysdcfS8gf1CXkCVMBZwHzHRIJSskNtc8/7f3V3p77qX9ax2olhp3i6p3pCHB5jpWGNm5046dNQWMDyTam5y2IzYc27hM9QYKzm3a43v2qYvk7gfI2SmY5ELDGkb36HGEk2stgEzu8t6nu9yhR37XJAauvFh48iDFZRhIY1GUAVrQo8NSUrcd3oEGjqGAltfbtFhrAAUA6l1rGsIK0Ri1VmRVd+Y/ZwdI2eV+qjF5hBGbQ+B7oRW6ILtncfoqxQCp8B7vclyq08sAnawT3ckO133fVX7vqe2BGFHtwBbDDUZIFJk+RLrRMr8n6OcXeKGStkeTVu7T6LJEBOXmbMw9dYczlqajmCLuIf/GWt0qC3ycEbz+J+ptFd+Xi2WRwAljnLXA2BMTcBstTBhAm0mKwvs5GaLsFESBAdlxK+vdnMlu3VPH+k3RS5LbtG5i8zEqBMvlazinnyGaRa5D6LsUau+5NvM45Sm6/JY9wxEkv2Sg9UJLEYAleMHUijs2EyngztMxpSxHuAI+3wTfrGbmhuyPVvWUy0Vgpstu5r7U+RQKvdHUM6D/96+ntnLp9nFS87iJQ0VUbNm+FQCL60U1QMWpfmrpxi0JRNxNF5rLSVdqld960MAQoHp/zseXprZyRBrPhJgg4aO9kSDmsby2HiK2rRG3DxDrqSwIbNhTqYC9bvBKHBiBicvkrlBCmYJv+RXibs+tuIQzdP5vsosjL4Ve3MLI+4adMcy+w9nALpO2oBl7pMKmRgOZjLC5oQIp1LmyOUxzOUW6sz/tYD/EPqGhlVnqOrZ7n8jPKLW8JaTsBoml+AitOhnWY9Kjyafu8eb2v7EeN8TUMLfIIuVOOvQ/x+Pq6XaYtJbuzRCOhFPzVFmVOPEqc7P4n2p7lIIrdf1aES590GtwvbHIxCBQ2TyqoSiBcvkEjxhLGSxyt9PHgdDGMM6OloX0ehaNr0e8pL5xF1Cy8PWV6wTSNnIMDQhiIXIxvetwF6ozuS3oU5R/oBhqLIQEutb9VtAu33Q4or3oF1gLMQmRehGvHi8EeKiF7qbrYthAjV1ZU1gPpjYoNmnxnaP3vW7gueTxLJCWT3N+xGg8ZEcPhwxFS6PFnSJmxLFRNcwYGC/yCixtkxpGSjxGZjCUjOrtM9roRnBRJaFhUaEit0VowGQKqLBjw0TnE/suFtWU9yK+JOgKaM0+BBGPqDOXH8r2cUbziEpcaFaOOZ0iL1oEf8arPYKxuhlJHhYq1tsXGfbQWnPLgLsR0xvDmvEHQ3srm5pRXOyErzySE/0icTsQ62vDIZNPMjVDu7as8LcZy/yEQI4hwIfh5e4BwVAG1CWRqc72xKS4/Fo5XDS0zrPtneu4HidiDWWzoi94rSEFA0D3NlcmKGTXp4XuKFzWNCtlSKbOs+40ix6OpHpJvBfqU9tCoXZ059sPgUVRjGP8jOiv2sfDPEqyJhdZh0ozmBDF1LrDohunH0fz20eGZmO5kvR+l+e+5N9Dhh+/ge+05wjzDf9HT5Z4mtnDAveaNejV/jSBtoMfF6oRO9+xUXxvfzJLg32Lw+RwnWPcvhWRrbH6sDfMcVUybKKrg+mCrkUx4BSIlSEjGDQibZKU9KRx16z3cR4boOKg9wC1Jhbsvg/GdOSJSGt7oA8of31QmXT6oDZqAaUoCvusOO87lc3b41K0LnrASW4iKtUootVTxIotMeqgvq/lWW5tEVeAMo0uCK3NUJJFDTDDcq3tB31jiSrJsNyXCFPHKvzbTzu/URMkwBhaR6KnxSJud5dyk128JVDRQ6k1qwZcDm5ds3K9hBHRJKheBI1j5nmpv9R2e7V+HxursCjXSM9X2OQijiixnsCmg39kjm3mzxlTmk3RwCMs1Lxz86wKuX5VrqQlGi/yrJMnh2uvHWnEgkSMzgqVPUcB6H1grckOVNQaCy0ueKp/muuohjEhcVTtyERAaT6KSKcDoxE3/ZA2UdNmSMqUpktiBv5LJxmm6tyWKveYMrX0AEcfW3hGgmo+9Opys6+AQjLp3J7qNotB4x1JDsXOgzzeNWyP4ZdIk2d2YBwzNyw/GITxGyNiLRN+rkrOrPBcpreFXK2elQW/VXrPdhNPwD5JjFUTsuCZxNRiLJqpKhhe4gcWJMFHCHUTAF6XcQqM5ihELeqsADoIP/QoEVkMnRoeOtxFL+Fs9lCvzA9cHRHTi/APNmJgYGZ7c5pvJv96ccSGy1MzRkFZgjT1GZdYVVO49ULc6ZqnJPsENnly08u1HnIutvpbU0thjSa6VtnwZvJ5qRUaQvMlSA7XvxIDmF6Nvp6uPTK2hpDeEsoafzXFGbCoFChPCeHMK6sI3t63kX2ujqeOqeKyaJRvdOhIZ5xFzt0ydxJWbUpJPJJkhionuZD0w8wg2gfJk+7iTe6Ou9VJCndO7c8mM7WjyEKARr2qcVFajsU9NVfskN7e4AreEtQq7x7xmI4D8JXiteU6wqpUX9fhC0w3+s3/xGl8RAESlNq4G7bRzIjjUglqKy6Fk8fDdmiAprUfSUCckEWSaZhYWOxPRYdgkp9K88KFnYJY0R/mc+otAm96IF8FwkexOEoWRpBOM8xIcsnA/GX6SRWMqC7qef1YMOamLmbeXgxg+bc5WcjbqAz7Ry/+klQS2D0x+j8YpsVW0UY1H9ixR6NK2Klbqib9nOQlZksYgDoLZ4//hF56KKkpfhE6tBq5RgizZzlqbWgkaNB2/nw6ElRSagQu75SU5fE3DoUAEBXKdpc3z5v+3SlukZi50Q5QL0afumJkq3JXPsddU1k0yOUhKjtvw4kyU8SsHUTbzeXOmR0FtaX4IP9npx9JZRiwr+kcad3t+wR1/brN/mVZiKcQeGCAMiFK+KRGrga5dTjMQ6BJgjnpF/Zt3oQ7/xR9xb5AnbVOnjU5WzV9mR50zy5ONbAkEbQfJCyQ3wU4MTE96m6S19JfTrd26KoIIuep4KIiQoraDplK3uKQvMLwTPV6/VRD8jUh/nZL4P5g2bYO5mcWF847w62qUmOox/RtpDE4QyBTP5la0hpaKw9Ck59zok9kYxq7d3eZU2qq6w7ARHI8Z0ixdbeYkhO8xh3gSfi81ilpTxIaFoPJ/f3Nmp/2IZCjeTOMED1WKHmZTJcQe0SQHXS2gXOd8z6LB6GV2YrAPcNcbK5hZvYcqFQSuNi3WWyePOdeCuCgW9ijU+UcYWoRLVNWvJOwfhnvDVF5YnC1fXFeeJu+8DUZ6YQASPvC4G1crgWdQP+WPoEH10ouJuOGATkYOhFXuda2tsBAhFUURHrnHHGkqMuWrEwaitjg37GRlYeuq5qIzhptJ46JxJhb008Q/1zIqBwklEuvjq6QhZc6pt2RG12nso5DWAgcv7OOL2vP2VyQb8qeXp7JZ2t4YWTRuDetpz7ryJaxZSbCStphXBhxo+jde8cvmf681C+XJZ1kjI376BR0VYa3r03eRbv5qKJiFllKT8lX2TDB99A/aaL9zzEMaieH9oIcws4n81MxEGaJ8P96HHpkgTN8vNhtJg3K2SVz6bKpxETZ7D0Ekxsf5vpK4Ba5ZU5JsZodliUQ1O+nA2S8OI8xh1BpQ9bmFg1Jgqh854i9T+hvhK1pTWht8QOno9LL0XDbw2+Ih487aFZRtxAHttP+qPGLug7HSe2hSlin4qHuFc9Z47yDvkl2mKIGmYuP1DXHTsr07iLT5hPkPcvhFxKQ0oWK3pdfiiPCUY3S0gYEqsjaYnf69VCuMzCaqe1MJSxYH7JOigID6xg7RfR6R7eOgispSnKMgs0YO7GZ8eveHK/JgYUABO2l+SybEQDjfkWMh88HF+38DUK94baLUGl4yMfq/aIpcyLq+S8ZRGQ5CnJb74yF24LGF8LnfwpEwWuLm3dZmdKlA+Vx/4aeeS1Hy2w4wXQoOCy/ZiI9ZtGu5/yFAOYMM7G5bWt993IN/IztG4MrJbDHba2Jy0vIYDLyPOU2alau4HnBHGaP8N6/T6vmSyGklF8TpH62V9+rcZXdkuPoSKo8Bu3aANib+TpfpO1NCygC720iPw7utv3QPrBZRcVwJ01qnJovBUzb/63eIkYm1iGB5RQbN9Jv6zl4dnlLyzMZ4o7BksulF2EDM1VdJpjLtITh6GfA5jySsfGH1yf2YqJkq1d6fRoRPz6iROJkuHTEEaX3VVNqF/VFNnxIdTBFYyNd3xC72YE6DZhT9ZXa5eMzdqPN+F+OyYJR/clJJ13ARAu7qJqGwdfaZVFYghkZqXiVtUfaZxmaFw8a7iPQ97CWH7vxWeoUOujotz/1xoqqmtHJw6/DT7J1iDoHXHJvmuukn00J8RPadWjpCuGMmWbkWwL6S7SV6VgxnPMIroYb9cWlPASvBee7iGuqOO+ydy8/ruPcxpOLonx3bu4Nzsv7ksStnPDhXZHa4aJ+Tkjcoh+sH1HKSgvAv8INoHPbUueVnkn49jngbwwqDl/0W4GmZqh6mRiYeZQXpba4Pu8v8QWVfGgsyOO6HA8nbJOpsnGvYvsaaCVfn0q0EMA5xD/Do0MUThAp5eRb1Ma7ObRq2Nkt/79yQ+qGmlbZTFKPAJX4xM2g2jzo4HqjTXxGg0tQVXMP8zN5lVeU+w94eZA0s3It5AjEKQa86mC3vB2LPm/Z1UDg2Kfim1rWMjHWe9U3DiGuBAljgdkws9srk44yoJAU6eZMs3sDkBY8PeVkd0MbeyJ/Iohjbe/BRVjBzs1Ei3YcI53ZFKp1ReZG9X/xV5neR41bhXC0rvUQigxLTcyvvXQd+/LbMLW4LZOauvt3ecy5WaI75HZjgW6FGGwvMMYzcsbsy1bHhzGgcI7CB8Mo3FiMMUTIHrfGGhYkESE2Lli5tDcRpZ6yb49zKyaKSd8DkJbCnNIgl1AL/pBcDWTZYomd5KE1ZjtsGomrbjMQpS4Hffe7HkzCL7s+O/utl2HC/ysMJWKyfVfhoinThloohpAkkBLQS+2X/uF/laWpJnXxQ6/h1RMUF+RWNWm+nk1qdeSgTzZy4O05yknZEr8AQ9glNsaV5+oIHkl3a6LT19ZrUGV63BrR1L3vA6IFtTxzy9tkpdIW1iSBKO1z5Nn+w9a2vNA5L0orzkLAKzIZvxNpafw32pcVSVbTCrWzvSLc0ZKlLE9ELMn5O89IVVT+8XHCaph8igBzg/bXxkW1/LeNg+DGAyvLBizmv7oaL+7zISt5L+76GykmsZu93TKe2FA07J4CZUWc4Qd5EZXWF2RcEzYpLv0WcxBdn67cIMISkd0/orBWjqK1pReU1/npJAoHhGSgcK9ZAihKD3qgQYO4SCLctzbBhHBGKRahP70RF+LFxM0LaHSfLGutQCKui7YrE13bR4CUSUgFhRgh444+3i3C9DuHDB4IY63n1iSXDm9kVSZBja+wa/4IW9Od0b/8n0l/7bg9fB1niD49unAmohNDxH0nT6mofZ7sVYoAgb22b7r00rd0Oh6kvBe7b6WZjRtVmDr8AE2LH98WutdSytp/FL3jfpdvDyro7vKNgrpV2MzHHCpDBWPggrabQ6aYOD+gV9lEQeRUwgbkDouLCMSRIq2N0tr1kUq/UuyHio4UI0kzlvSdkRIJq2Va9kpEwqFBz5nu+vO8A9JGTTE9ENkW6xhInU9Ie+KmyJlOTU0fPyYXUL+W2D4+EvteM1pRpvqEXL3O1bWT/I11LgFmRpu+CRX1NQngwIWB7llpZKYykOxnMBPNTV+7dP50OP1cHosoxXOLmjk/U/dY+//MaIj1HASGtqKoTEwdSvzbaKKGLXfJfH1tTEO9TvRyEjHEShAbgkBocuLBMsco8QLpmJtYql6tMLGD2Gyhn0tJ9sGLFXK07i7nCBS+EMsEZBXjPawqvnCm4mHtOu87EdeDNle+mjJSbHAER41FVwjDUD9SD8czDoeA7WIXOaIXWvwq4SR1uRqVzqEGqLmt4eZndtvxHLk38in0mQ3sAJhsDS3Ue0j5E0HWBSc/w+7r3+WgU0INqJ4GeifwbuG3MeOci6cETMXZggDrKk15FrtBnp3CUvdLybszfDtVq5CMbbatxCooWbhHb6gshKVfZaS10+qyUl6YTQs3U4ZfaGtcrHRo6G1xlufvq/CeUuNhz9J/lMO0JewJFY6A/nZVGfC5hz9Pa+mRZFGIrX97SgFTHiTiNuOT8lrjuWxOXK+JvUHnHxokaKwY9qXFbtd/O6ro3kLkSrkn8TiHjpoMcGcsXk0LyXRnib3eA1FtQ0pHtr5+VTseTWPkei9lG+ysK2ZCl5xtWI7eyhx4jbKs0Fw1n/f7n1vAMkpoMIOiB2tz9MnCdKK1EMMBGviQqReypHMf82SoibxHLSfAeC3tlwtqfIJX01LBPEaP70TKShPT0ZJH3+30q3APZ/1NfgSBJR7DId8/71CJ1vNvgvltmgX7oIdB9Mw/vt9pWEqRTxahcXcXobyFBPJZZ3DpJopSBmDcEUfMC1ET2OOYkPYhFj7RQ2bMCLKFgMoUHG2EeZZh9Bntydqwym1atMpswA7a75ZtanokSGK3L7m9GvaYE5bUTKIkzQ9nEAtr3lenI0UmmtyOH9IqFxgkEY+8fgsDTiZWu9FzEkUFdQR9omu7evHvqk1GrO6ojjRvfQgz+W4rBHGt1zEzFCj0wwCrXWm+GqQfFtxGtH3qRR3J2L5TbuyihUzd1HioxAghFuG0Bwpw8z/FGXZmv5nkQyUIyANEVGd6k0GtcL8Zx1tjGjvoFAmshcsnJfxXO3WeIAzjfAjJpdZUmkmAnQX7KFU+ES41ql1Oxd5/HlEUHY9BNVsqQUNFeUdZQZFb7QC2T8S23GTIosJSMV60xo2CtKuZ+kKnKDErK48K8mLAXJH9zzxOZiJAVyRvXUPOOTGW228N6dKDdnFaElqd1781ReCrdz1VHmhxGLARmFF+obmqUqhKmNPSpIH7cRehaG54cvkJtz2c/t6/jzRRXAAKy4y/GZ1+LJL2o09s/+sy78pGJDKJdFFUcHGDLGBaRNnGH576eN5VXf5SSyD+2UtsEuIZLKrxpwCXL4pduYZOyYc9ikbLQQ3LU5RSp/rarcKpGkJ2BleVTYvogehL16nN/65XThV5c3nhWkBQw+v0qk7vO9zTJoV0wXolaOmmGrM6OQYNBHs1J1MTa2qBjQRZNglJ/WqRaA0sAEIZnJY9fQIY+ZrGovFMr2MkPtyH0WG1fp6jU+zTAd/xZtou64T+V1ekGPlKXjwyVVLCVFgPQZInl19e1mULWRbxhMEiq0DiNXXxgmYiXz89BqkEJN6UZ3WyMT4gDvtYMrMTXGlqBNM/o7L0SmuNqlTU28hUhVxl9A7DYlafFJkgkQ5+OrtH0UtQRUp3ciWIWrlc8M3crKm6sNx+Dq83MD+PIAhh2v4YG8GLERW1o9vEFh33dVLhDrHEVIZxFmR1l7UMAn5wM/XWSitXqVlNGYQxThd6qR4G09qRWQQPpedPHnIYIw97dhbdhaOddhIfsqEsiPiUPb9HcDxsZHiO2YHcl62+vnBLFEZEjHk194jKBjxXNqgVPhqmGvQ4lKC6NFfAd/PHramCzcP3lh3sjnx6lsQNDQKv//TtDnJ5JMAT5/1OqgfG8KoU7MufVcqmmIgmsqjgumFweG071NoxsVpzsXW2RzXgNWYzkqO8+YufJgHxPlnZYR0AXEiy3iQ9fG/GNQ+uVW+ACp+K1UOxXYzUbnI45qWWsHp7ry04xWyVdM2syvp/mXYXH18zLsdFwK/emDYoCKhxjpA8S+5MHTJ8yjJpuIFZ+R7a8qH8vCbdyZpWht8dp30m8gQ0sSc+tw1RfNB+b6KEYuenIzoeTn2OBas49adVeqaEb7h+UAGHsk+WlanZoXVTJHWM1ub8CiQFUV5CyVNaOxrw9pnvSHBOhr3dzpd/K+t7BItpFIupi6QQX0g2ozqxMdWiu5bKVIKcfcLUkkMs7sMylXdlfuivh4ZlvemY5M8JMLzEPc0h/qcFbBbLpf6tD64cFGnuwkP+FSFCdphGpQr7VDAJGvwQ9HtCsOcQpKNbGNm6Q5apYDW5m77wEgNn0qTCgJDSP4pPCJI9yS8IjyroLnvwolv/9BZXFgTxkqHmXeT6zrih6W7LJPAhgc7fVY7IcaPPHNkAaq/mTWoCTsr73TJbBR46MpXhM3bq7vIC5CXJZm6KxdwjiR9it9Q5LQgmK4T6ZkriQBTi1yzfwLMuS5PXn8Pn0IN1JE459Q07yG0srtcOpHk93oi1WAfxW4G9LP+P4k/zZHBEAOPy0PBZs7y4QgtoLY2k0UtuIGMRlse1tPoeOq46fT17k+yVdoZVQRoyEHfsuW0NQqo0x1DXvYUm1LL8MkAABnQdxBoTOAqgXqTJlNf81GwnZLPeCU/GO1qphndN1g5me1YrJabhoZF95BqdzfvOl1D2ZrIub47b2Z4/CqQYRSI0wOtXSkVBVQmfNt5aPh+I6kYaFsak1lGsD4RGLZ4g2tuAIoHsCko+avF+SRfPcgKC2IEYQuiwiw9NQ7BVPBWjEIvEoKHjqS7TFMH/GEgYm3A8Zr+YLFAhsqP2MBFIjoy4/PvR+J/Y+BUpg65gYAEIPKiOwWxToMZ1BoQEbRtsHXQ2/FjN2VPKuoEHIcJNFm26pEt0jafT2wWQzLqBzIHZUbGx6MhCCT9WBLQhqh28v3BUveVU6sVCxzZ6CeiVJ0C0VwuEvomFlLecOLtMBZCXxU3lkZmg9L8M6qjcFgBxC6FRdZ15q1Uk9ag0O39HZOP2ke8WIh9FhrCOCUKUJCs5KULRxGSGAtXk9co2Pl0DZajD7xNmhpZp8FBncupc6b22uSAG9+38tGnAqp+AziS2+o7IiT5ezOPERAC9u823/P4jEq9wG6K5M4IIQtulBaQRCs7ibZzEt9XvorPoR3NX8L2RQvDEl+4xE/6LgW3tyhoqUqGUr1ZGs8BC59TdsF8lcCKsqlG15DhbanPtlY0Ad4NynsmO55Bg4rHAhbtPkIF8fXccLW13vo/UaQgBWZ0nT/UPZt7tbh3f8FXCWDaeE51TBgnWFvwVPijZpjhZoZ2dR4ao+St/cHzHJip+Js17GD16i98KCWeeOOqqKoD18pc97/XByLu8YPjQxVuKfkk6y+fVDtOKE2mtYXkdNXkUYDAozabIzza+j5NdOAIz7Q+OzF7uLcjUGaN6wrt0qudyfANfSq1kJUs/jeldbVqHYM+C7IURSmqTNDo19ZdhL/6J/42OAb3W4RpuqoM6fmvqtavBCqeu8jZJaPz6QNAOxpYKQ5ln2R45ik1k4y3BOYnkGegTYONBXQ+zvzkgvfly3vx3AHXSTm31okMMeyS+HTsPQXmUVDKFgMcL45mgoxSXSQ5Xmr8t2mV6Tkf0X6BMz3wnHhj8fduvVkuIkqT/yI5Wf28qN8i1X7aQOxiizEXUrZJXWLVdlgsStG3CtB/VhcgbApCK36xrVtsyOhG70K4QYR+OQ7Q292xF/JjWxjgTzjN/5VFyMzBfXCiCeec1Z/BeCJtEKgW20CYKaP6mJGO1Bn1G3WjxCDiyUtU2vO/wWBk+bRcxD159p8X9dnCD32nCXzQ7STi1yJrp4LL5YPj7jI+WZLTEE2xAYb+kTncKXUxsKm8DPqUA4iDrUylW8nLisz0KEpRvOJNwzPnxgu+BBNFDMatfyGtRvGx7U1Z+Dk5Cs93jW1DFjT/CkmRNU76n3C5xvTIwu9hDbXA2RDQ32hhyvpeW+B1vav317HtzDIbVSCnYX4DbRoQ43foM/nHnIkWYWcWnD/+S8v/mX+v6erxtAyG9c3qtv5Fxgl+tWsrtI9PqTVWULIu5yAvliLHGJ4KyBT/NGJqk1JKdOovqv0zqso3wIiBGaYXgCdmZDueo6WE/aCcwoSYfPXAScrGIiGPF0/s6dbONmw6HSrhM2rvfjoHZiv5IJKCFa23M21xPUVus5+F8TISDxfsAq6wHIbYkAPaNpT9Jp6+gqT8L2MPaFPqvPm+Xfmg3ER6XhaZnHQZZX9V6X/5u6XIKBwJr/uNIXKELJ86EEzWLgsdCFDWLPcNNwJg3pSMLRuhTEwEP8C+sM/HNifYKqCd+qIrhulZs9ywHXxHL4OU3BJjOq25mdpWKuePqsRClgRfS48bJ2tBf1fumZBjpPg50daQc3joTiya0+AhgQWwuoAeA4+x34MobT7m9Tt87KZI6BoJy4mT3bv5uMT1kLeMS0MiDtzoCYfcBTQiaw6kt3AFYvZpNkHWVLBWLzH7a28ZASgKTownuwxTJluOFt8WT063lA7w3jNijv3hvsBhsfqkH5kNA0i+15O4J42JIziyBUrypt7Adp0RyV9czeiPwqPyOdV+GGgG2XTZYpydsyh0COgkzj0YS0WAp20mEs4mgUEOQ8/vUlOEGlf3jgbWf3c3HAsEwUIOIZj/jMY3wwielLFGtvgWnIqi+xueoCw6ENv6FIsuJxqOKtznVAeVfiWSgwQtX7yGSgDtq+S6LfCfKPAJpkvY1o+3fGKVdiHo8r4tOA0W3LhQRfmPDJ+WMbJnTMc/S4t9Fi8chI47aNCOxXtPKzSV1Fa4Snk/2QDvHNkccB+MgAWVjogbs+KpG454Mi40YyRPeVQBlV8KsbY2utdT3FfABNgk+jHIUPbDLSrzA2DmhKYf6fuhLcy9e/fbSOQD9AMox9tyj8nUAM/k6cMqJmBfv897f0CNAG/+90zNdv2niHH17j9yXA3drinJSMMfKWIAlnUmzcge/j4Iq//RdHhFxRAYD0C3549DzKI0YGe+bbqTrENHTGE/WoZUIvPPkxL67G720azXmB1m+M395myquzo29Vhwgigw/w1YEXsLkEXFdUPshZkKQ6ipd7i5jGQjSFmEyuCI5Ww9BsoyeqYk1oinikPoaQKcETNpY2STO7BkQASCd0quTTErYJTBk9ZQilgcdYCFU9dLJkoMmugyK9OrszZMm0SIDNcI2JB2WvHotJnkoOt0myOnwTTzUHRCHTwURxfU4IB2ejG6db3WZEnH7FOXaS+3u8BjtuNkASrHXZWS2ka/7eR8fKA8i2WSqhrpj1y5z4xpm5PdujZjIdEnzQwtU60EbS71Z6QeXCb/aQAZ0LWJC4YK1QUqM7JZ5pbWvRgiVw+fxzRTphJZsqBJER3wRnQnuZEnTto1cibEu9S/9nRFM++dHUVQ2pUYYY9GHJZLON7kaZj1mLNKQh9k7/7i+PVKhswJPII3OckvWmxgE8LTGeb95/+wifEOFPgjOt4B41VL5PqYlzXseGtQaPjY+kx2qreXfa2Txoi5L11/ce0iOUlJfl/M3Sh/w6cp/JbPAIeuS1No2Ej/14cR4wAajJ54UIlYsLttAAfeP9b6yKhDm/0Cc/x1aTPGO25j0ChU2hd+oqGAdf+zNFaCmzWT18vo3OSRMyb/qykkJjQ+T6wAXRqAf6uwTcIthEe/0qYidVPve3GbZwoggjQhO3eMWi0ADIf6WuS2WFkelFJD/2faR71JM5wFBEYPO/gen/XV8VyW8jq1eCY9VkKAj49LEcUogXAuxLgKFSRLKStxTbbFRlEKz6bOw9uz4v1mdB4yJFZem2gRQUHzOhHjle/SMSFkKZeNQzfBqy2LvJtaGv/r4AzJTclvZ9Khu0PjpRYaN2zvdhvwhTf1DLcU/AxRp9ItztxFoAz1DEdP3RF1AOQAYBpnO3OMg5CnrusDJq+syaAVFAaWE2K0DIWhPTkkcROyKsnL5h6bgcKwDZ1Zin7OVv/DbR1D8Zf2Id6XyW3gbaqrIZAL8tMXzukW3c6OTdZbkNV6Q9OBU1daGDz5vDiUxVtDAToqqASCL8OZ8XD48hjC7eKj4FElArxwVZ7Ihy3TGd6O+T5NTBeAY0LvcLhjaB2y5aqZN+eb3zk4nEf8VKVQWx9ZO1cvHxStoifetQm55q1HdXUHxlrca8QUsxLvvFWMI/gp03HmiUk/faCnTS7OE25y+GUtunQJB+UIfII+YGC+IwE0yysKElS7wgaMm5VsKpdWtU7tAVl16CNu4MSZ9/ksnUfKOCXDM47wVyErssGvxskJZ/gOIXq5+evOI7yyUV30V1DEynGh5GBjXjUy4d/qXKFTov15b1WkEHT7DvhYkGwiIg8i8JiylBrkwMqW97qxf8/O0gBGEHsSiTLzfEiBLjL1N6zXLL/nuLzKzIDI723A8cnxUerlCf5qS0tcePY4l3E/7OLJC4yjV+suOEAttNK2Bzpc+kH0wVdIw2X+/06k/9VvhGWVz4vQYvA6P+rG8I/QoitpsCUSTK51ueAP0azb5Vxus33L5UxtMYfhV2eRjM+em4jAPoC5jWAlITzrXe7UR984p5IhO+pj1oEis23cr4wzpL7AymaYaL/8l3PBjX6iwVl2sxHnxgz7hO6MxtBjDXkwsAwEh8u/xCxTDz60hOvjXymsZI5/pZ7TY/O2jIN1IKloEPitTzDe1VBFGvG3F3Hq+kTcbuIavmcpcsfwCBfuISnq5Jfdi1IRHEgL3pqsH4wwurK6sHnRJKHb24h10l87tKYd3gzBkwBfNbRpNfsj8zUdAX1CLtnS2HAg0FxPjnpWdTWuuJK0V2myS2h6NN7ssgdt21jGq3rEeNZe9l/C+oFI7gIz0l7ZQIcZhvE831tzKj2A3SxEWZMMB1kE1jkc7o1CFI8y2tYP/90R7GGI6zwbPwswzmHglQnESND3zImHH+0ay//yuSlK7nVWo7Ala9+rdr/zM7qb+5kK0gHFy++s06gRx0DM6/Z/DEvJkO3JGbHDy76M52LNbHtOuHsMGafktJMqSXpUeAuS6e6S1urB09yNrIBbtPFyMYGdS6OjZ0fGgExpqAehg3EgypsStcwMOwbMW+r+x2+HLxO0Vu/VAv+9/cWgmJGjxI5fZWBlWWNwTxVbJ3moa2FWOcqbEmL9HE7u/4l0Xlvn/8iVwsKOhEc1++kyR7HJKTIGCrQiYiV1YGPydqcKEmf22WVcMQciy9+PJdHl7ZZkL1mACsvvlGnG7KpJcAKMh9Yg2ulo7ghviUx5K0ve2rRArRjTRQW9dcMn5vledo/acuWYfGT+wgQb6WEPrFogi5CI/iniAiQFzOKY/uHw4EDn/tLia2efEQK02nxeBB6oCeWp6hLVOQtsqQ13AGisqnLFJpD8k2+MZYk8gSvIvMaz37s6gTnlM2gVLDBk5YVCvnJi0iAMp/h5kmg9jDOO/JxiLSqt7xY393oPsN5/F86AF7u4xqyP94qZi5DwGBexfOvh7PmYPDEGrydmyk5t+3kZ1YYHKsD5i7NvojWkiSyljNXKdFzQi1DmbjnznCYkEBMvtkNgFitUPx/VUhc04t5GfMxyZ3JBfzy+DjCx8U9Bz+v6B+ZoRnV0MqMavSaT18WEKzrBToC8u6McaVZkNROUxtDleVT1t0bCFkYYmQv6oEVmWEc1ZFIoiHkMXOKAsTYqQq2BrwVwW5LHEO02qPghO3y3MuvdmPgLH/qbAgbv3HlVU781IvsW9kU4/rs82jJjUWWMv9AyBrKI7ao0osReehB9744vvlN1rfhYmV8iwL8EBuGy52yF9V2d+pp6SGPeUVsFP3HSq3tIgo7zkzukbRK3PF2O6Kwe6XRcsKuMzD9jm8NKnRa6RB3qmSssPTr+K/x4gAvbPCkHMe8jznCFSVHjOv4eGYv9scmkvt612FQKxB6AcVou/yxV2txK8V3zGu40Y+U++enqI9HsrAGQd16HByKb2i9eNlT4vehWxLKTw+JwKQM44/zcSZQ4xgWz6PCdTd01oaMTqer2aum2X2Iv/ZAB9Il/TUslIbk+3XJtVqdj6cdG8Jn8cgBRbNiWZiEgg1Y8UZujudhuH06Tvw5ZoVRqbXNW2kjPD+tmRrw5EsqnxxjDw1u1YFrQFLvqaQ+ZyMawLUiI/H64EykkO/JrWaY3Q+jrCWWBmverjIl55l6H403C3bMZ4bcsRNJRqMpBH32fX9YENCYfdQZC8Ay4qKYRR3xGa7qcoXois/FOqoVyRjBFt/4l69VGgjrjuyfxzLrREFqHdctM8dHraSFP02TC2XIEZLQuu+bC4wIwQS0XEgiKMdtKMbfxMgPtl1rbpNF6BQBZpZHt2hcDUJVmxtdBniUbKP7CBA3UsF+iB/OM1PbFc464xLDzZy0faCBDde4EfWniYFabM3XW34JP9honrIDNQpxCL0OcuqV+lAEAVqM/i6kG/Wi87ooQP9Qsk/g2m2UYSIr7fHuraB7/9Xp1n9+u4aWfV89qnoacMUY6Mv2Erhy++jdDOl9zQR0EQ0JJuhI9oG5+S49xl5zWsFLnKhpyDOP/FJgkD34xkXHTT1Q7mWr6Hf5bMbm6Zjkm3WKL0Zbr/T4qQd9ptLLxlN2VKTgR4elvT/5htvGNrH8hX9ABHkeHf9QQO8qdgawOv3KiritlAU281e2FsN/7JamsHZ6fvEFLeCvvpBhLkt4yflzPR3HdN2uHFyzWhIEbr0FkwSpxDEtECwbFacZxQulUo0+eXK228eNWd2unbRX3aihqPDJZ73DZl2/3rzEgikn4Ue17ID+m/9reD9czBspLAqaFqV819mwqVdUGcuOm822HzgRVeWDBQVQEeh4WoPh55nvpsrvKs+Ubm/OWCjDXoWEmW+OYXMv3FeAB3Cw90LmlYKNHMaIopQh3b+9X9W7uB+4ZBwTrp6um6AnyO9iRX2f2oA+CRGFpk3HFwjt8VJasRf7zVk7YAPmjwWigcGaoilvi/O+jEWypx2HjlXuL31zqFgX5klreNc/unuHkXvScS/kuaVxnInjaI9O2EYEkY/1mZ7kfyFs3mPEJlj8ZrQx9utMgnX+z5otxhHg71Pm6LB99our+jMaQz2DvHl9Ho3OIWMK3360oDrfyp2itCMGhH1o8RYNE92xBa2z56334fAKQ0gme1ol16LzKreWJJy97B7gbsJOMkRYmcxo9oF9nturAdpb4fTQHlJyvd98qBxSgpYUhGaSpsYqLdTf9o3FZpGtXvHNjKbtwJy4FigUQwY8qdavyyON8IEmd3Fj7itinx7q1Foroi9WUGctJVM9NS5Ccy6hIVOima/kaVare3Q7uQydYHfAuPtYz4ANM3cM3SWC2K/ytxTfz1+2bN0jOJSsX69elZdBDFwHeC43euuGh6BN7VRDspn3D73/yYQGMzxZStttPw7lcjVwp1pl8T/jHLp3Xx+yJxk4fJyBgNyt25V747M7oiJTx1PNfd3nI99f8fa8Bu5UI1xvuAhZT0fIcjX5QKQEx8cW0C2PLbZFwMk0onpo/tYKmf6JW3zlrbdhEkOO95V5OUF1vkC9ngWMMCOZpg6C/Hl8I7rxRxPMWAxAF8nK7CzKIaR31MvYfoe6R4B/y672J+1XzsMeV+lnZkZviCYSOFBXByFp7v/S7FvO7FAIi+iSI22MzL6N/4JD8KW2XF0RpQJvs2VIpGnm7XR5oT9NXKbS4FYIuUrYYl8AnrKDrnUWyPAA3W91eCNb/0SwyRs54CN2N8hwO8IHe3W6ZNrnHflJF/GH4AJFy26K2CQ12jYSwMdYug895zdhwdrNySc+pJ5pbeOL82QTSWr3NlvGNFIq6p737Mct8ihLWq+1QNiomDIt9oah462PheFK+TSIqYzd3VQkSzwPe9rn/a0fG5UFZzQlIpwbo2K0RE302Ip1VBe73Y9Hk+eOl0rtgXJxoSeAkugNHQCbYWF0wN6DR2ELPv4LW8+wffa3sGqQ7CQZYfW2acVoCt3BUkJgueDYW+0zQ+j5aeOV7c7FZ/8KT9Sg/zQPB5kDh4ebYrl5Hw97G509ntmOALRohhwifpQFVz5+0mz8T0fjVe9fLtL5q1laZaAPvi5TSThsWfz17Bk59N2KbxBCGPdPNWI3vM03e6ZZ0S/I2LLkcnalhc026NIMVbDxzC7iwSCBP/6c68pgre6R2V4KeCQBAttocdbtbn/yavDquBjBbGLFralMd/WsP/XSC0wF3LTiossJCucBav+dSUhUufryvXb9y/H+gzKkdLI5rK7ul+bjzBZfVfkXYyG0aXggvc14xoNNXzIbRVx7XZlqMvU6RR1IUVvsIlr2oariFqLAup/c+bLwQyWYq2O5iZAZ+0xNvBTok9/kkPkGEXy3CXjJGi9J8/5jNINGkZ7cSvg7+GTYSRaX/pr5RYXK0mDK+ldmuoQ1Yj/LnR01nQWkRJ9vDgmpOz6cNSOtrxPVy2GsZ517+nUut7aqpVdHYkh7mlMQCsiHHI6+BodZ94QI7GqTwKuRDEH8qCKJtK5pxcuZDjY+UJcUIhefSbkO5tsi0HRQS/3GMUvVCReTcxPXZix7Ep82dAyDYySCE8BnMjjMJUO2X40GI/5oXScZXsusvhZirHbxVTTY5spG373EdcekPXB0khOsd5IwGHln9nBHyntWowASli0VTjMjTb8xuG4cQY4++p4i2EF8aaJY6NlObh3/b8SkqPixrh9+PRseK+fssc+FhvoTT5enbZ1IkFTsswvZ4VT5Y0J8zzdW3RUdI7lFG7Q7tla+eCFVEDTE9NzxjgLExJoowbdq9zd64gpq1Ktr4rwdhrH6clr4y+9XrFYO9DmPqqAxFJByxvCWUZPjKXybQ1IkiBC46Eg6892NG8X2s2VPt+iCN1CUEbJpGq+aUilaU/j2TjUvmJwupgbEy6A3eWUlnjgd1UBRXg6FMrn2cB+ALnP5D4a1PNUygKVCN+jgBXlqGCzMWYUf0n1vY57Tix0bu6UGhkGT73UftmcVPO1bE2YMz0AdL9jKyWgfWrgmYS01Yrz0hnPHWfczX6c9XUimD0dKsbwRK55YVc6bgPClXmlKi13vk+rUnLNxJWYfrTbrWSEpTkUsIAD5Cdf5LCpo+9E8rNt4cde8/UhFi8kB4YFApSOhsKYVO+mfJGYvbNTd1rdHRxw30kU3lHhlZcWAs+WqSMspl3U/f1Z6EmqJu9yywD5/rN3p+hTzh1rF1W0KGtpI9ZdbNTJlqAbMjUWBlfOVBqoXEoJz4peKx7HazLTqqx2iZogmUvb805ZMKJvPYcwjPQL2GEW+KZKGerXuRQT/Xpj1sjpVlpZRFUZof9pAkqk120M4XpT/BRkKdJMaUNktmZ9XmYJABhQudJ9S6eOOsYyq32rRYqxipqVRGdS7iGTyNpCLGUe95PbS8c1u4A5Us5zThvJxLEbOBAZl0bvi3qtIh7odtjBH4y3qtLOuhnoS8wXh/lxoPNP3sjMKFhIMBZwwiQ+9L877ldqw/6ewb04LSOFt2WdK99I7qXP9wHj/BQ5fKr3kJE/qgiLFGAsBkjwUh+yoUnMmzIqCq96QAqznIHO8uRlYZsehWrGZ/+Q6s0rR732Z54cRuN8vApTn/6fXyuVIzRvOlIapME2DrHXZb0ibPGX6NxYZMFfKQ3okYkprfbM4p3+dZ5+s/FU6pXtO/axaQtzVnMA6gYm9C1xGZDpCXrfdpyOIuEVEb8SKOeBiHsBWES2GoYl4G1oGGuNCT/FrhRa6Zce22cPieag+EMPy/wRmtwh2P6jEKKoPzz+2wmtUOb74DvkKKNZ5UY9chu0bXv+GA0uBrqYMYj0XI/uwAzFXfC0HCivyE+9/jehk2VBDaDyVieMAJ5fl10kSTiF9S80TbhtCKDh3eSwmEYs6pgqcBZmW444ddoPmkEhU/1UuiHrQY/0+TO9M8UIcjXOvRbYIkUiCFX77Gd08rCfSgSpBvVz0jEeSY9HWqvkioABqmva6QQBtsrVIwjSSUjTrIUR2OtorRxEt/skwgEZ6O6+sxX3ZNajLlu1iRxgEShRikFOlsOfhOsa1k/mjXnCHDSpeMxI1QMWOEpvjaf9g+jbNoiGvDjbxWzju4ulQrS0AgoZs5JMw+A/DeMOuwjEIYSYzRMzRO+4jJYP7bVjtVG1bai3Z3/DpLAl0ZYteKksztK61eRBbn234trBIAE6CiYEZF984v52+09zFEm/KF4DqeFK9njRD/dp1bJ8Z8ksp3xkoYNBJZfTgjZQZIWkRCMCt9T4byAP4xs1+pGqEMso0HU3fg/LooSOQUubLrzoucJC36KKADznr2X2fR4Wr5ZIc08Xwnp0n9OQig/E8NxP+aKl2guW/cudgyEC/yIyWw6wyKj66eQw14zGcgya5mnXUbNqQPez8kK6vzrIul8oBHt2QZeA/Yj3gg8CaLP/Blc/oRYyNvzk0TsinpV8Ln/n6zewC2q7rWBdxToL9lP+agI28f97HdCeKhFpWq88aCR1ZQiHdw9h5JBqtBoOE0lC0HV4st9oXItFtA81X4thSuWqvDmbKBwFbEJLjJr20XFM1gQ2gCFk6JfBFtbh+EP1evqsTcFJPqzxH6Lzi+TaL5Qxs8GjW9PLAK7cselkePIR+7HE8LwZKAmC1BqKAjdi/1qUXoOak3FR7MOkqBMb9kv43PRAIkFxNIAhx7VZbJiz0B17gauZ6mX0YKRi3Xq3YU7L4uV6Qtxi4iYlNUSBK6hCp11hdw8jfhEBt8iozttscL8dwCiyEDX7v8y2O7gnBPe7p2I5OVQ2E2krgJZWkrRYB91UcAGojDJxGUHv/1sXt1JA8+GrRwQFAHH/EpsJmRTf8MLu865bvGiLWW7TF1SHGP6BeiPj+DBmAVdnf50xla2/mbNFrPAKvH5cskvVtArJFRLR9NjVZVpWidY9zvV1q46cErUwVTgndY0r9FZBU2VUW/0+uIWnj4LVyQxRUSHUkwXUCqVgo+I/6gU8EfFaPgHnp+CG1MOAPhF1M9YnCKrSPThNcJ7So7uWsa5Tkl1pgJRyMel73rPLUovskw45qPE28G/pYiyrTrRBoRK09LkwRmgvWd3ZTm8w3f1XxHtYypFxq/I6L+p+Q6+VqfX/vXMbbvgw8meC4xNkaCkPQFjUhQcij2S33ksXTC0/nOs2ZCiYrkZgbvmP9RwQWN6I/amu8siA6Zsr1X08OxslwlFUrRgT/w5rPfOG3UH/3oVuBAtpfXpLS5bit6BoCjNeq18rBOdIUTE8sDRLB/cCzivbCIUTH1KJAoUwz2nTDtv9PD+ijOfpzkBsdl1IVonLmelW9GCXr1ooN9sFqbo5n+pdkQ/VAym2TPAE4pahGp3rKQQFupuVu+nsTs+iR/RTaclcgKuHz7hx0f3lCkbh+9jy8UItxcE+dQHgTNxTW5wgYLi5I/mgtVyPyv8fb04hT9dlAKabUTY0k9MoCph0w9LLnYLclkoQBN4v6XfhoFxucXyV/aAmDLU+G8QUXctqkCmkZSHKp4Ep3xGkCv7Jsn+U3ku6z6FFVpG/JI0+U4fe+sZUVs8xbQKaiS4i01p5isbil3nZ02GqxgALQMos3tKaBQ+Mm7GxTjm0+hiqWN7pMxl12pYNmN6KxztKFtE9gWt3zaYTvWfy9Wx7SyI3kGkicV81RexfVEkWYhVTy7n7mf6PQDZf487vUapFEAxzo2n6j+e5iiph494hfQ23O/pllhoIeMXg7pks+4TJ9fl5FUvO2cxnYyVbgIKFDb6bSMXyI1XaRN1ZJxRgYArDp3/9UHCH3jkMSWoaTQmkseSgqtGqubTo6PhAzpxjWCjf3FpYHw5WRx9OBT76OIZ+MMVGelIemq2HGF3gZ2ONmLwivM0QxnklmvTWOS8oE/eScv/heUF1eaJO9a3O+nU1bHbDgcWxttTVxfMd/F+Y+jaEk75GBQB30nVJOrwspzzV94GvNRLnB0pK6twQQAfUMX8sdTtBS+I8cC5f1qp7r9EqRZldP++kks+bJLHOOwZCtSSAYgFJQwbKoxauITWKb0l6cwE3xfBzXRx7u3mIQav5W4YjR2EY0LtNJr+y1kRKHWnUF6gsSCc3FUvbYl9S4YeM0nAVr8YztcegVargcyGsIhYx4X2PDSjHW493wpRo2APmX+OXPx1+us11M+Ou3ZJLk1iUQ6RSIuUdGgK0m2quA0ln5l7dTVVxt2KWF/6TcQz2qxHR40abu3xS0uYGN8A8keDGBnW5KlTgAt2c5WmphRismGWjGLxTTReoXix/k1Vtpv+YtqpBieDhqDjTrzXWWSHjMmskTjjKN+8UFotCUa4Gt2ncnWnC9PU8QxnpiOkmvoQBPfc+WMpYVKl2oM/HkWQmqGllRvUyboWpyB53hDrJB9jhNzKdEnsCwB7/2xqTQbykmTI5USPoukAYjaGuc3/SEZ4V3e6lP0D3z1vOoOZXLX5jzj7QDDe/vmDSpxlyhqPsnjCOkrHhoPHwWAXhfxQXu4RWU30UcwNTbdliFOYwUxy4mcxLKT61j4cnA8wwL3LciXCP8F16SdDyoWl+8Lo5nfJv7k2zHZzFCUDF7YhHC4ZYfaZ1IMjNa4vrxUul+PcqDd8vT1P8Lhns4h2om4d9iZAFZraZwJAJDY+MFEQmVjiLdV9MfLFrbWotOKDvXfMtHrFvitSo1No35fWxO8En3DNYlpCi+bCzxVruO7FDEMOjeLnobQW9rwkYhaIBwXg61JaUeSbprc18oE66g9zN/BRD3aox7v7h4TyBQv37x5a1/cJOtmv4NcasO7IU7cc0fKeUkkDNFSF2+GE+LVvyjYFkugcRjnX4Ij8g7EV6Zs01KJtB2b+Rm0I4lveYkUZrq4ij5ERkO80ib19OL9EFVyCvqcSr3G9jsuwiu8pB6iD3CxN5TstON7Fw8HgANoB+6SlYLbwrkjFlj6OlKehk7c+IFMyp5MCEXJP+UDgzdqbCBgqkn5NpdvavY+ShCRge3oj4JxgpxupeckW+63hShIFHThjMG1USFK2uaX2ehPy1xBtPfMKGI5gBSX4rzXvv0TrJnWoWIN+m1se2vg248Agksc3wAZQfDF6g/sWjX8e9H9++/wFIAQ+27NNeBO35ZIDMksy8sla7N8RbW7UVFP6hY19l2zXKLSL59mgt6MvxGjvqdx1iqna6EeXrk7nBMTErGX2zwklLmqyxenyvjmKQEoF/nbegmNCOkDsIm4wPn+8SRGQDRgDwY29OlcPQDxju33FFLtq0c/L24fPMJ1ip/ufBbyDRw7Vwd5WHAPcdFziHvWDnTuc+lBFsy0P+//8k0Z6KSt/4jgAI7wNzzWO1VpctfCDR6n/d71JNx7LkcIj1K5WOiaCcEOk1K3BJFnQUNCbt1F6EAyC75Z03uQVD4fhU13halsw2I679bLPr2oNBxYgHWfD8of8EjwNMMwQk3hg8pJjAd1xySLsN09gQaRxKSfsO55iy9Tnp+HgJR7K3brHWrjoe4f5Z0V9ACEYvfxTDQe2zl9XJ7KYGeph55JejA90W3NyuusxVhy5Sc55gyutCR3TBTsOnCRn68xR32wa27+hymyPEcHQuFm0Snizc+n2mksRPmZu7SH2Iq8uMNaB6knjfadF8wHXTv5qiRCUBUSGwN9uvbZ1PXNOCELFvLHqpMjnxkzWil9S5dGuYHjyWSbjKVQWt5C8tA3Bd3RPCMZRNeTgBblJuWja2D9jvCdLkIVoeJsomN5PlQ+PHKXlN4hqzprcDTs0liKDWsT10ZxVHLybtGVe2PvDuTYD7pUGlFIBbghifY+sGaeJrBuT4rE3NQvxmbSPRajuoEhGsqVK6AvB9MScRWceA84optYzYNyRU+ovYAXrlb1aSJv1/gcwpF0h6e582F6wUgCLlTQbQqP4CduxRXQuaYOnYl0wRTrI8q0c0HCXnICyT1obVU5VjeJlSU8kzXUNpMJl9hUw/a5AI0yEw92x7IQAQvh3kzT6isbyNY9SG+ANwBcr6o9kMrCcnd78gBXpkie8WtpJR3rN6jtJboOsgh4f6TnYWkplgVpgRyEyA+ofLNqjbvugO0bO9wyC9Pamb5KjA1BupDDbdT+TUeEeIotQodhjC1vMqh1BenTbqZXTWXSveDxf9zVwcKIsEqnrrmBNgtcwYQ9iSS0VaLSbwgYO+f2ZEzKwuv53HVeEAi3DsOCHLXcm1jgMIP0oDB4U3iAoYRUOToRKp2c9eyMRf4/Gpn01hVaJIBwr5E5aLeJD+xrVTVPqZ+BeCTQnvWt4A2Pw+Tij0ulp4Tei/j4j+ImPmq7mxCwEgXvMrThuw9yRmp0VX3qYIfe4OddW0HTvBDOhZFVFK4ArlgOQu5bB4MY22LZbsh1rP9KfkBwQvHlCy8juOduB42M8tBYG+yeI7j7H8M6nlvd219fIAh9xNGCMjT7iPTYGS5Uvzsdf2OuRxsnvcGU/eM3t4J2VcfvsCqhRP30ZjW6IIYR5vjN3Rlqykg+ksGlfDqamZ8Ir031v+u8nahjNyLuFnGDyJEqiAPtaYs7iAi+o6tj0ccgXltBKbsr+sV5NEnnUg/rzo0aRl9uLSVRTZnfhLSP7AsxOFdepcCGXxOC+XBoatDLlFuhLHMzgEXThoc0I5wfbiMNGiNrxnPOcs2Z/Ts4yXtJmxWWj49pO6kE01SGGmbOO+vjZmpMDkkWI/q9xblfNCK0X4XfNZMMo003AinafCeGJMLS7Ax5t3rVFrrfslUszwXazNf1UquBBEbsZFCdRnOtwILgmxY47YOR8K0+tRWjsjPws2nXkTMb5yY8F03cNINcqX9N4F4yPxLIo2laKgPWYV5gJPCOiqmhwNsbRfE3N8fXg/fPfZ36T9T6/RM5qP5Wm/qfnLhiL5m2WDsPOlG1z1XZNTHLLSxzJBJyJLGhfcjp7v5VxXydfLZR05ThYTBH2JvAIBk9p3o5toteMJhs3zWfMwAHjNK+lbNyGvF8jS4DfkVaC4rOZ9C9KtA8dimEuVGmNYz0wca37ns6ZGwoqlPvqfnjq1coX5fTUO6adjbvc3hb4rVv14bUB8CuevLWWwu7//Mm45I5HzBSiy/KEWKVBjS9vpnrvlFMhq77lzTnTNF15wxPiq6fTnnojqL2ydZ27I2GWaQ1HqAIZ5KkMfWSUg2QFtaJpSBiY+tK3BeleikHK7JUYK2fa2k+rfIx/qgLFlYWbVZiCATW0wkQ6r0BMzqyKZq9cQFIp6PcDWvzPTD4IM7xWtv3Z//Q1AC4LYxmWyFX1/Lzt/yIzJ09Gv/IE40faFJnFJ7uxdotgVZh4WOm515zUfsEiLoQGA5xIcDpl8ZIQYNcUnj90YReLH+K3kdvUIdMRSaSl1Lq/VUgxDbHDcCyguAeE+VvHL4wLgHLn7wH69Vf+OfI9Lr63Pw6wWDth8eORGZOh8pI8nBrztlxpYXvZJbNqsgWLN5qupmHd+NDGX/7kdqoWQhIcfmkUE4tjhvzb0WkLQXR7XbuM3ta0LbCySIsG5/7pxZXmI+izv533lxsM7qI4j9Qq2ioIBt0mae1M3R4PVod5D4OXIpwk+Bgoxh7X3jsTr3SgQ8i7ZAfvXie0olUTJtFdlVRRGfCZ1ORb0rhplwlLakpdSFL6yviVn8+HfEcnJEzPOZ1wZbugguSeuQ+diXz9tK72s2c3BnujmHbt+KNJ5EFtn4qN1YTFkWBGtREjx4ZSlyWoyuXOvXQFc8xNaB1pyKoVMNL22/59SLQsm8ufDfwRkplEaN7HuPxpVcahiRiHWmjqkfrYEk2UuOS5HLNF8kL7DvQq7tCx1NCRmyqWo+FqQjFugAUYiF43qn155UvJ9xcRiAnhjpdBHCvZJVSGzZGaN65WLKMFMPWsIDSSMBHOUTSDyHzulTAd9aYahKC1s96L7KJJxuNc3SU7GRb/d84in84UWJQ4aPJ5uucVWDjuHqT8FANr1J0I5LnHXZBxgSUs5viGZ2VKjBxS5cTAQ9JLV5UDXQT85Rkn047S3qgOyqupmypyTfMFKd4D2VQYiG8Osnf5QPzKfMp9WXywBQdGASS0MifcsRgR5I6rYD/XDmwlGuQASc9UYojz72Jc1xyG52mOFvl/kR0JDHdynAFQm6cgO0akDWBQNlF5q5wU4fKciKQ9iK/LL7s2TUvJMd0IlHX/Qo6p4r8e1yR82DMZUy2vZFYtgrCFAqvWdCTPoShk5vOv6t1VCMl0kDOKAIBoH+VJ2x4ZChjPFzNqjknTVWwvzi7kZbL8n7ivmMJuQqLCLb3sGiEn7SCpoz5/2wlJpgqMBjOw+rgv/RqWX3g8XT3m4EDsru0It5fypUKAWcFP/CTpRDvS4Dx4x5eOMNg/zsFYv096fQgkgR4QYMi5tCOive/DW95zrIXL/5ab9DsOJqpl6et+uGasC298mbWeZEmgc6n9H4g/Mr7TdERgrOIyplurcgTko66U85RvceLwVmeypzfEuas+g38nNWard8mijarSXtZkqAO6TDB+Oz31/OBE2OXrC08H+ChJnnkuEZVvTCphybvIJ8UNVULWR51zcbcAlQyPODswh84cEUZSmEBq2+ZxlnKf8GHPzbndJY3ZWrwY3pycK4ojulJArDn22bBPDxHT7a8eC5AA3b1zKL7W4+Ui2L5AjzYcflU1jBoshydYRMa7g5iBP8A/ibFuNCF17Cw5dPmF1P210uUCSWCiP7VNlyf12HCIYkGBxSyZv4ZhEqQmgIq6EjbvKtDoCmWOjvrlcyIa7MG3GuJxtiI3LvKu7Aifx4G4ppX/ELmQp+8PxU7DujSrGw/S2mD9gSz2tBwULi3RigTtxkkDTKsgVFNDTZMXFtaOxH4aKgaq7CmpAADNwmLAqDSWrQ8bDymm5NskCi5MBL66XADpmGBXK1zB3n7MDf6OJThxCFOCPPHfFcBNMzHnz+WiKhm3RGg2++J2e9PnFxk1DulB/KxsbBbujM9KkDdLXKlITOJ85ECrQO3VPd72Dx8rN5Inh9mTcgcfNVHIMxvXDp2zJA0vQ7sXS+xqbouhWCfXkSqqYznKM9T+dVujR0FgKUz8gFODCPz/xfju1k/2d2U73F/e4PeXPKrw22Bp3ucEa/5lWciJZNuOG8icpqkIg9hcHGeRMq0eyTtlLelN2RHINRCEflzUhx4qiB1fiSJxEw0gqlb5PnehKEfG8YA57nxlDk8ctYoj7Cq8YOUJvyZGTOcedXjSXOkKk6cbVkOiGrhavPdyA25hJ2OlvF7gqLqirKUtCRXS3V3EmbZUDl8yyR8IJ51Pr+Z/7kQpyHaK+IMV7dg85dmRPS9sCC5T537psUOeDo6/7rV6m1eNt/0g2VC02xFJ3NPIHJ7dcLW1xoVOx79pXCxSE4+rzVLfVoFuxKnBuT04yZjnSFNT/p66luQTuYRt3/4o3qg3T/N4ujmFRWgTyd7yFjMlOw3vJcdlP9n8IM1XvZcy4aCpfEjUjmG+4I9khe4WUjTMlr3YYdxw3lbU13UTHp/yG5u1sIJ85XlwPYsynWRvVu7zRlBi2cdrg4r9eAjPz+NNcW1wyYI14Sq23bk03L1vNz3QP5bzldDQVx9O3KGDdB8clvsrKEg3V8X1ekgxsyk96xcC3DQJPXvwLnlbY6Ft4nu+ue1l1Tm78chgNGevG6oHLt2WBfTm+jyVet8J6YcTTWDA1GTAnfVi4A0zc9favF+uAYc8EnEfUdq0M5sz4vuqKez/pyPx9ozB1M9JuExFoG8131GF1ULxi+3Vc+/X+Nn1yH2K1aWAhNFJfBYS9VhS/lUz//z9fy6HsVTfrdYpMsacGB+WUmNySQKwIpSjgU2l6hw2Z5EbgdSRtDA2OgfA5nQdga4R3BPKR38m1V8Z7gl83fCHGUlhm9Rl6hi8SApsNDcACY9ZxGcRLjbChxhZEZrob4JZL5ebhKM4olI1NxAdEpPa83ajvupfo52ykc6ulrvs722BnlUyoZnL/yiOILDP14l9lpZjYy9KdYTDqLT0up/I2f15QdfefpRTZzRq4REopi0z1RKeHFkdM/t134165pRbvv8NoZ6gOqQnhINZHXIEPIsexXdZy7iB7mVq2+QC1bfpSID6J0z+BCwzH/XM3E6LXCGzhTtHeCA9uPKDEyeyAPMvkXgfeAL+/wYRr0CD5FOvFVfz5V8DXZ0mMiMG/nkmUSag6Lf9iw8ijiNqmxUw0/vaVMxKMu5tm1Uk/OyTpZrkdvZaUUzq8XaaAmLqOLELKA9cyKpUOCwn+KtVenbZZNa3USaqQlery2OzJkiMAOXhRYwwvYOUbvTTJ7aItM6yybzX1kw70A5Vaacr3QDMl3K9/jBz3G+ec+jhobLRXdKrjfFh2VHjPrfRo6LE2bUdQZwAqIsrI8HRAOkAD/kPr2ZUA8qiKq7vLX+rhvH1+6I8ntvWK4MeHPMP0ITpjJE2FZl4qfckZjJo9H4d+mymiiQgJy76TjQZGFBIp9EjXBGWUO5sLrXInH4OGp5VCq0WwdkLXLWrmo73nOxRuFrKW9wm45lcN22s5w/QSEc0ot59lF/iG07VbGA1uoSK84y78O3pSgb72e/Q8U0614feWd9ajLm3q9CkT2pVe27SupdMADvW5nsg+GEiwmvk9Jp52iuUCIKvJxWYm1A3lDN3n0spLruGrewJVy45W9dQ6YYLdRY8rMLL3CWFV6iLJ+bU1ONai+yZ3Sp6SPp13hGxKS+BFFb0PRfgG70TP98/ljiZ/9zyULxBNC/0G29k6fVM+H9rXxktJB9QpzLDoAz31oPDdC9Fqm0gcE8AdIDM42lXPp49v8SWc8lIjDU+xNZoAJMNw3h6UX/4XqN74roeEwTAxX0bLyfQkqoARVjPq9bDvmC6z3v+qIZLkHS7YyarVw0NcufAIx7Ih8uM2CDH6p3nBhc1NkwM17UieVdLgtHADgSK2ZBoOzCKm9mxf4PNfXP5GWIc0yOiIIbAQsS01W7mycTjd3qWRvgCqjmXk89KYHtyqyou0tAbtymWwRlnSeoRcmdwegQQOzfCNJVQ4A1/YfgyLC0l21Tp+Xquug/dRizQQ45/NQXcGX+ozxwxfRx2pl7N1qMHrtXGNF36R591wg+X78l6Iux0u/l9JgNZswCQkD6k+gZ/3lmol6gJULfCHZi0DU5DfEABoFjUf8SIhAm43Je/nzf4rsIyAh517nxuTNKcbtDJf0zaULgQFwKQ639lvr3zZ7afj1bckNOKoCEqL3h85F5P8YTEMqn5iJEvanNImdrH2sLw+9eX1Nx/Ib6HmdOkMURmPIZjC5HoRbanR9bRb4ZqBEqua9nTGPKLPHMh/Xv5hh3mEmZCyHYlpKrlc2muNXSrIOFd/7ZNb7foCez/XD8tSMXsI2nJVQuAXt8BsbkRlvfE3nRVicx3UrhN+iLRmFAMXStIqN6o+oLFrIxfBvPwiHKjelm3Vp5ymgq5aFHkfH4jfDP9+wk/1oiCKYBXLuXuPsRKm8RRUv/rCSO+ZWs2Fx1CEjqR+5n9ILbH4MID3DuGljMYcZLKUCKANL2nI98WZ9w44S7DXRSI07ugyEKqReTUwB0+gw5lgYXg0KtX/z2g1WaA3JDYhZ+jQJKGinlbyqtIrCeLrWfyQroj/HEUL+0gyZGHpOMMnumxg328M1qZnI41K63CLvoxphBLThzDxm0UHuuX1ug82bVkWiH+fwWTJ4rPkKmLKXjfOvnmGqbMTuyaVaNSx09UE5UvJi3kb7dnqkCJ/VJB9AFtXJeJMKOWgwpuFRQxQjTCHr9FxVTSZcj6ZMdIQt3JkZ8cTfjsGOVVI4m04iJqgM+Q58Dv1qBZZrHc8pHNiEMbQJ8MAbsDn8NE6o0GOg7DgXO/Le68F1S7QCm7gPJKrmbLYTzfTdPE9bedTlPk/s0ij93HBt+e6nUQENnqQlOIZlPeU9aSf6MAUy0KYb3Ao3Jdlvu2iECsj39ACJG4I7hZHBKIszs3nHw5lQ83+tnVa9Q4W3iF3JR3QaG1NBbi5pZzGvM8SstlES+1xqmoMN8SUjUXNPluXA4NreYLqPxiVtQNRVemOQbZ0v3NQ3y5+8Rk8Oht20ytdN+oq7UAKq1Wi6fB/8ssq/y3GTHtWq+j+OJFa5BOMG/RN4cX7MdNNNCPBd2gyQ4EJJMjf/LAPkMvQ56Wr74T/nGkwKUTutcPpmQB3RfUfjm5WfVZX9/oITerq4w1RkeFLwiTbZLNJK7pkk7Zu1KqwFGfJ272TzAVjhrYnLdIaBlhpWN66ZegFRhE9NvAIY/ww9hxZsKMRJpunrt4AemSMklYHP0EcwOWaZ5EOiuJ/+J1DqO+PJFCmWLtTOjzP6CL7RNEr8BQwccOjVK+qcCYznOn+GM3gO8pNjUDW9ZQ4/KBgKLxSO71HB6BMQshpH5nyT0tcuIy6i+4y4D/1BRULp4VCV0+hbCYaYJ2R2h+Ii+0x5+sgyqDkMedLh1GpGW/lDV5utVyaBbsqFDbsau6f9eViPKwQ3lGDjJw21tLVLKGUFiFgBNtR5nKjQnRE2F2VoJxRrH8f+6/g9qSeTsEDfpA4MEl54yVsDPZk5IaNvJLpfiJBb+l6jm7MQ4XxvyNg+J24t6HvVHlkt3ApVevJYQPhXqQ8l8YaE4RI6aBIiSQvPPJo5PzhCG8TpWK9k87ZoEbZBf+h6WMIkLbXjEVrNLBbew+LmcfKiMIQteOVpOTgY9M6tyuHMnUuybqN6E10vRLPGqXNpv3wYX6oL4qZItu4kfWUji99DLt+vd4QXHz6IYd0bpq5+zNsz3df1aLLHE+yRt9OKJ2zoAONE6U7NXejHf0OyW4mk9WjrDBenfeBeqHrA9hftf+rFDhYjfayjYuke8s23DzZyJ98CGNhg1IpeXhB7P/rNtU8Re5QlweWIsaM+cL/aUqUkpWSWQSErKdQQXlUXq0c4mUujt9k+WIycTnywyRrbJ6r7ssJiZ4MSEd/YJvJ6CmxyqXO7OFY0NdJ3tKvIen7cyBbrXSY3GT0vYQRJBieo9B5dfU5qop4XDVd4/j1zJYyg7hGwU2bZ1Ci5OdnZoQqrhzdo7Qw4zial65q2bnBh5kDj1t7bkUICAa789ToRoT0M3ruCK0MWt7nMo4OZp3uSO6gKWj5sF67p625dJBe8j6bWDOipRG/cSUU98pIsKBRNbAj+D7py9/ySRyFuvRnJJ11EB+e/fdSQBzTWRbNDHGTW2nExNhSMpfxR4Dpea8YM8ooaJLbbPP+4FNxtCThigxG1IpAwul5xMa1pEltHMLabN+5uXg3a/1SkNlWaP0ZrocUZljoYQoY86hE8OgAnjijuxllWIwgXQujsKA2ug0FbEJZDUflA+TGNTqOTz17yOIy0FhmLyjdEDOPWLFAeKjNKgXzcS3SGF1tIxmBKNdvp7CjOgLYYemAcVNpm0KF3g1JGT7Zx6hNJa4CtK5iRvAndqXT4ksmeKy34HORKG/i2CcvA8L9SbWwIEMUKoIWhmsjWbjJNfWx8r+UIZqq6dzFQ0rE60IAoWpRpKer9uqhJ23DK9cTFnz8diDpi6jrgzz8UMeq/ZtnPFJrh16v9EMuccXZykMMpYudv1XZX82Rjc65x+F0SCdwkeINBQThWdJ3lQF+93R4IHOLKHYKNjeGMF6ZwuGRYSWmGs/a8Q2mJufZqQne3c4i4aJ0fio5Zz8gV1eyEokSnQWm835sYz5yxTSbgk3E8nJA9cBqDlsGwXxyAps1hIy5vMkAwmjMmho2Ix3aETFoZjoAxim/VchJ6GNhn42YkXj1853elt3ofXmALCWKJiR8hvNDr6jZv9Ka1Hid4wxzGkGdBZYH8hg6dkXGKoLCOEr4W8em1bUZBP3MzMAjVqR88uS6PbuWTc9gHkh3Tuky4tXQ8obAWVny/HTW736n+M57UuYPUAweoHgl8YNGEdWzGjZcioQV2IazhctmmKfB0SVc/JiAg/jzbFGP63TR/MH+dQi5/pTs04m2HDc7mzNydi/K+Nnd9ZyMlqzcqzxJ5QESGVAn85dA3AeZfglCIRx9uOOXg4GpPRjo3xdf7c7av+6cbUM5bl/ERpTeeccWuwY/s1ZnNLoJHfUkuyqNKCMZRMbpNlwTSi0Wdwavj721OBjYdkXHHWwO1zCWJNpWwlysrUPNj46EopNPqmtDvxVqJYjvdhqR50Rpi4jWaftWjZkhAzc4+FxvRb9F2HKZibGru5154EV/J+3ORJNiSFq43jRNChD8Zk7783+cVyyKkokHxYRJUNs2HEzlIT5j3hakd9IbA46brcZsjSXRGaVnTdxa6n+z5gCqJTaeuiS6woI/P9ToScPVJVlDqOPSRaRvSjClrFaHxv9lBlTrwP/kTe8L88XCzw7rxeKP5BG31TaMpBp0fths04KFe79hizfyZyDxmwyFBN0WYVPS4WqMOj7n4E1yMeslockpiotKuZdfGIAnRMXCf2CR+9ePInOR9L06N5DxV4aT3YbetnIl386EDVSa
        - #2:
          - type: tool-call
          - toolCallId: MeB5PnRxks9j7coc
          - toolName: set-research
          - input:
            - Rationale: Late-game military dominance. Unlocks the Nuclear Missile, Guided Missile, and SS Booster, providing the ultimate backup options for strategic deterrence and final capitulation pressure.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: oJ4XhUnpl6CtNLlt
          - toolName: set-policy
          - input:
            - Rationale: VASSAL MANAGEMENT OPTIMIZATION: As we prepare to vassalize the Inca alongside Russia and Austria, Iron Fist prevents vassal rebellion and increases yields from vassals and City-States by 25%.
            - Policy: Iron Fist
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: ysOBBhl6Ebt6falX
          - toolName: set-flavors
          - input:
            - Flavors:
              - Happiness: 70
              - Production: 100
              - Recon: 85
              - Offense: 95
              - Antiair: 50
              - WaterConnection: 35
              - Culture: 5
              - Infrastructure: 10
              - Nuke: 100
              - Air: 100
              - Mobile: 0
              - GreatPeople: 40
              - Naval: 95
              - Gold: 100
              - AirCarrier: 95
              - TileImprovement: 100
              - Diplomacy: 10
              - Espionage: 25
              - Mobilization: 80
              - Airlift: 100
              - UseNuke: 95
              - NavalTileImprovement: 25
              - MilitaryTraining: 70
              - Religion: 10
              - Wonder: 5
              - Expansion: 5
              - Science: 95
              - Spaceship: 0
              - Defense: 40
              - NavalGrowth: 20
              - CityDefense: 60
              - NavalRecon: 60
              - Growth: 20
              - Ranged: 65
            - GrandStrategy: Conquest
            - Rationale: ECONOMIC CRISIS & RESOURCE CORRECTION: Setting Gold to 100 forces high-production cities with empty queues to run Wealth and construct gold buildings, resolving the -900 GPT deficit. Lowering Infrastructure to 10 frees our 7 Builders from railroad loops, redirecting them to build mines on the 6 unimproved Aluminum tiles (supported by TileImprovement 100). Offense, Nuke, and Air remain at maximum to ensure final victory.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: FpalSrxFlf7V04GI
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
          - toolCallId: MeB5PnRxks9j7coc
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: oJ4XhUnpl6CtNLlt
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: ysOBBhl6Ebt6falX
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.