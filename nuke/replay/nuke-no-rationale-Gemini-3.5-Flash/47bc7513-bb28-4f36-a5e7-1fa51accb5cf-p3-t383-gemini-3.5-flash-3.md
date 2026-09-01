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
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 80
  - replay_use_nuke: 95.0
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
      - toolName: set-research
      - args:
        - Technology: Advanced Ballistics
        - Rationale: Advanced Ballistics is selected as our next technology to unlock Nuclear Missiles and Guided Missiles, providing the ultimate military options to break Cusco's defenses and secure our Domination victory.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Iron Fist
        - Rationale: Iron Fist (Autocracy Level 1) is chosen to grant a +50% Worker improvement rate to quickly build Aluminum mines and finish vital infrastructure. It also increases yields from City-States by 25% and vassal tributes by 25%, helping to solve our gold deficit and unhappiness.
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - TileImprovement: 100
          - Religion: 5
          - AirCarrier: 50
          - Air: 80
          - Production: 90
          - Airlift: 80
          - Naval: 80
          - Nuke: 80
          - Growth: 35
          - Expansion: 0
          - Happiness: 85
          - Infrastructure: 50
          - Defense: 30
          - Diplomacy: 30
          - Science: 70
          - Mobilization: 40
          - Gold: 90
          - Offense: 95
          - Culture: 15
        - GrandStrategy: Conquest
      - rationale: To resolve the acute gold deficit (-900 GPT) and builder bottleneck, we dramatically increase Gold flavor to 90 to force cities to run Wealth or build commercial infrastructure. We lower Mobilization to 40 since our massive military (28k strength vs Inca's 3.5k) is near the supply limit. We lower Infrastructure to 50 to free Builders from railroads so they can mine our 6 unimproved Aluminum tiles. Happiness is raised to 85 to combat the combat penalties from unhappiness.
  - tokens:
    - inputTokens: 20179
    - reasoningTokens: 5564
    - outputTokens: 343
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Securing Japanese Hegemony**
            
            I'm focusing on consolidating my control over the remaining capitals to achieve a Domination victory. With seven out of eight already under my banner, the path to total dominance is clear.
            
            **Analyzing Global Power**
            
            I'm assessing the current geopolitical landscape to identify any emerging threats or opportunities that might impact my pursuit of a Domination victory. My current strategic advantage is significant.
            
            **Commanding Final Conquests**
            
            I am driving towards the final capture of all remaining capitals. Victory is within reach; I just need to execute the remaining maneuvers.
            
            **Domination Victory Imminent**
            
            With all capitals now under my sway, I am one step away from achieving total domination and securing my legacy. The final push is underway.
            
            **Consolidating Control**
            
            I am actively working to solidify my grip on all territories and ensure no resistance can arise. The path to victory is clear and being secured.
            
            **Achieving Total Domination**
            
            My focus is on the final push to secure the last remaining capital. Victory is within my grasp.
            
            **Enforcing Global Order**
            
            I am currently strategizing the final maneuvers to secure the last capital, ensuring a swift and decisive Domination victory.
            
            **Commanding Final Triumphs**
            
            I am in the final stages of my conquest, preparing to seize the last capital and secure my path to victory.
            
            **Securing the Final Capital**
            
            My immediate goal is to secure the last remaining capital to complete my conquest and achieve a Domination victory.
            
            **Executing Final Domination**
            
            I am focusing on the swift acquisition of the final capital to finalize my conquest and secure a Domination victory.
            
            **Achieving Hegemony**
            
            My primary objective is the immediate capture of the last capital to achieve a complete Domination victory.
            
            **Finalizing Conquest**
            
            I am actively working to secure the final capital. Victory is within my sight.
            
            **Addressing Economic Collapse**
            
            I'm currently wrestling with a severe economic deficit, a critical issue threatening to derail my progress. My immediate focus is on navigating the upcoming World Congress votes to repeal sanctions, which could significantly alleviate our financial strain and allow me to focus on securing the final capital.
            
            **Navigating Economic Challenges**
            
            My immediate concern is the pressing economic deficit; I'm prioritizing the upcoming World Congress votes to repeal sanctions. Successfully doing so should alleviate our financial woes and allow me to return my full attention to securing the final capital for a Domination victory. I'm also preparing to research Advanced Ballistics next.
            
            **Choosing Next Policies**
            
            My focus has shifted to strategic policy choices to bolster both my economy and military. I'm evaluating "Colonialism," "Division of Labor," "Rights of Man," and "Free Trade," weighing their potential to boost production, gold, and science as I push for the final capital.
            
            **Evaluating Policy Options**
            
            My current thought process is centered on selecting the optimal policy to address our significant gold deficit and happiness concerns. I'm weighing "Free Trade" for its economic and happiness benefits, "Enlightenment" for a potentially game-changing free technology to boost our military, and "Division of Labor" or "Rights of Man" for their production and happiness gains. The choice is critical for securing the final capital.
            
            **Selecting Autocracy Tenet**
            
            I'm prioritizing "Iron Fist" from the Autocracy tenets. The enhanced worker speed and increased vassal tribute offer significant benefits for both infrastructure development and revenue generation, directly addressing my current gold deficit and speeding up the final conquest.
            
            **Addressing Production Bottlenecks**
            
            My immediate concern is averting bankruptcy due to a severe gold deficit. I've identified that excess production is being squandered because the AI isn't prioritizing Builder orders or strategic improvements. My focus is now on reallocating this idle production to generate new Builders and improve tile yields, directly addressing the financial crisis.
            
            **Adjusting Economic Priorities**
            
            I'm re-evaluating global strategy by adjusting economic flavors. By significantly increasing the Gold flavor, I aim to compel AI city-states and my own empire to prioritize wealth generation, directly addressing the ongoing gold deficit and paving the way for the final conquest.
            
            **Refining Economic Strategy**
            
            My focus is now on fine-tuning the economic aspects to support the final push. I'm re-allocating production towards builders to address aluminum needs, reducing military spending to curb costs, and increasing diplomatic focus to secure crucial World Congress votes, all while maintaining high offensive capabilities.
            
            **Prioritizing Global Relationships**
            
            I'm confirming that my relationships with key allies, especially my vassals Russia and Austria, are maximized and secure. With them at the highest friendliness and already capitulated, their support in global votes is assured. This ensures I can focus on the final conquest without worrying about external diplomatic interference.
            
            **Optimizing AI Behavior**
            
            I'm reviewing the AI's decision-making weights, particularly concerning diplomatic interactions and competitive drives. While current values appear strong for my aggressive, allied-focused strategy, I'm confirming no further adjustments are needed before proceeding.
            
            **Choosing Next Research**
            
            My immediate research focus is on "Advanced Ballistics" to unlock crucial missile technologies. This will ensure I have the necessary firepower to swiftly overcome Cusco's defenses and secure my Domination victory.
            
            **Selecting Autocracy Tenet**
            
            I'm implementing "Iron Fist" to boost worker speed for essential infrastructure and increase vassal tributes, directly addressing my gold deficit and happiness concerns. This should accelerate the final conquest.
            
            **Adjusting AI Weights**
            
            I'm fine-tuning AI behavior by significantly boosting the Gold flavor to 90 to prioritize wealth generation, and reducing Mobilization to 40 due to my current ample army size and high maintenance costs. Infrastructure is also being lowered to 50, freeing up Builders for critical aluminum mine construction.
            
            **Confirming Strategic Decisions**
            
            I'm reviewing all recently implemented choices. Technologies like "Advanced Ballistics," policies such as "Iron Fist," and the "Conquest" grand strategy align perfectly with our current objectives. I've also confirmed that our key alliances are at their maximum, ensuring a smooth path to victory.
            
            **Securing Final Capital**
            
            I'm focused on securing the last remaining capital, Cusco, for a Domination victory. My key challenges are a significant gold deficit and an aluminum shortage. I'm implementing "Iron Fist" for increased worker speed and tribute, and adjusting AI weights to prioritize gold generation and resource acquisition.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 18e8RwEePKQReTux
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Advanced Ballistics is selected as our next technology to unlock Nuclear Missiles and Guided Missiles, providing the ultimate military options to break Cusco's defenses and secure our Domination victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 4MS9Y0x3QsQOiDRU
          - toolName: set-policy
          - input:
            - Policy: Iron Fist
            - Rationale: Iron Fist (Autocracy Level 1) is chosen to grant a +50% Worker improvement rate to quickly build Aluminum mines and finish vital infrastructure. It also increases yields from City-States by 25% and vassal tributes by 25%, helping to solve our gold deficit and unhappiness.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: QIVm5XEgwQHjBuXy
          - toolName: set-flavors
          - input:
            - Rationale: To resolve the acute gold deficit (-900 GPT) and builder bottleneck, we dramatically increase Gold flavor to 90 to force cities to run Wealth or build commercial infrastructure. We lower Mobilization to 40 since our massive military (28k strength vs Inca's 3.5k) is near the supply limit. We lower Infrastructure to 50 to free Builders from railroads so they can mine our 6 unimproved Aluminum tiles. Happiness is raised to 85 to combat the combat penalties from unhappiness.
            - Flavors:
              - TileImprovement: 100
              - Religion: 5
              - AirCarrier: 50
              - Air: 80
              - Production: 90
              - Airlift: 80
              - Naval: 80
              - Nuke: 80
              - Growth: 35
              - Expansion: 0
              - Happiness: 85
              - Infrastructure: 50
              - Defense: 30
              - Diplomacy: 30
              - Science: 70
              - Mobilization: 40
              - Gold: 90
              - Offense: 95
              - Culture: 15
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 18e8RwEePKQReTux
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
          - toolCallId: 4MS9Y0x3QsQOiDRU
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: QIVm5XEgwQHjBuXy
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.