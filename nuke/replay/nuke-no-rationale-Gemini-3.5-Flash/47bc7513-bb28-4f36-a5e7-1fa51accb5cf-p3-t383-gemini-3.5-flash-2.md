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
      - toolName: set-policy
      - args:
        - Rationale: Adopting Liberty provides an immediate free Worker to help construct critical Aluminum mines, increases tile improvement speed by 25% to accelerate infrastructure, and provides +2 Gold per city to help mitigate our significant gold deficit across our 38 cities.
        - Policy: Liberty (Continuing Progress Branch)
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Researching Advanced Ballistics next unlocks the devastating Nuclear Missile and Guided Missile, giving us unmatched late-game military supremacy to secure our final capital conquest.
        - Technology: Advanced Ballistics
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Mobilization: 80
          - Airlift: 100
          - Defense: 40
          - Growth: 20
          - Science: 95
          - NavalRecon: 60
          - MilitaryTraining: 70
          - Offense: 95
          - Infrastructure: 100
          - Wonder: 5
          - Production: 100
          - Mobile: 0
          - GreatPeople: 40
          - UseNuke: 95
          - Expansion: 5
          - CityDefense: 60
          - Espionage: 25
          - Antiair: 50
          - Air: 100
          - Religion: 10
          - WaterConnection: 35
          - NavalTileImprovement: 25
          - NavalGrowth: 20
          - TileImprovement: 100
          - Ranged: 65
          - Nuke: 100
          - AirCarrier: 95
          - Gold: 80
          - Culture: 5
          - Spaceship: 0
          - Happiness: 90
          - Recon: 85
          - Naval: 95
          - Diplomacy: 10
      - rationale: We raise Gold flavor to 80 and Happiness to 90 to directly combat our severe gold deficit and unhappiness combat penalties, while maintaining peak Offense, Production, Tile Improvement, and Nuke flavors to aggressively push our overwhelming military advantage and capture Cusco for an immediate Domination Victory.
  - tokens:
    - inputTokens: 20179
    - reasoningTokens: 5839
    - outputTokens: 359
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Dominance**
            
            I'm maintaining my overwhelming lead, having secured an extremely high score of 6031. The Autocracy policies are fully complete, and I'm progressing through the Information Era with considerable advantage.
            
            **Addressing Economic Pressures**
            
            I'm currently facing a significant gold deficit, largely due to increased unit upkeep from the Global Peace Accords and recent heavy bomber upgrades. Simultaneously, I'm experiencing a critical shortage of aluminum, hindering further unit advancement. I am prioritizing builder production and tile improvements to rectify these issues.
            
            **Adopting Strategic Policies**
            
            I'm focusing on leveraging the "Liberty" policy from the Progress tree. This offers significant boosts to both gold generation and tile improvement efficiency, directly addressing my current shortages and accelerating development. This seems like the optimal choice.
            
            **Evaluating Policy Choices**
            
            I am re-evaluating my policy strategy. While "Liberty" from Progress seemed strong, "Free Trade" from Industry offers significant gold boosts and happiness relief. Given my imminent military victory, focusing on rapid economic recovery and happiness is now paramount. The airport situation near Cusco is also being re-assessed.
            
            **Reaching Cusco Directly**
            
            I've confirmed that once the Winchester airport is complete in two turns, our heavy bombers will be within range of Cusco. Despite some briefing confusion about bomber range, 9 tiles is indeed actionable. Our overwhelming military superiority also means a direct land assault is a viable alternative.
            
            **Adjusting Economic Priorities**
            
            I've identified a critical oversight: the extremely low weighting on gold generation was crippling my economy. I'm now prioritizing gold acquisition significantly, aiming to resolve the current deficit and enable robust infrastructure development. The discrepancy between high production capacity and underutilized builders is also being addressed.
            
            **Prioritizing Economic Fixes**
            
            I'm now prioritizing direct gold acquisition, considering policies that offer immediate boosts. I'm also re-evaluating the benefits of "Iron Fist" due to its potential to increase yields from my vassals. The immediate need for builder availability is also a key consideration.
            
            **Choosing Next Policy**
            
            I am prioritizing "Liberty (Continuing Progress Branch)". It provides a crucial free worker, boosts tile improvement speed, and adds flat gold per city, directly addressing my current shortages. I'm also setting research to "Advanced Ballistics" to unlock game-ending nuclear missiles.
            
            **Securing Essential Resources**
            
            I'm focusing on immediate gold generation. Diplomatic deals with vassals and leveraging the World Congress are key to resolving my GPT deficit before it cripples my science or military. This is the most critical short-term issue.
            
            **Adjusting Flavor Weights**
            
            I'm now focusing on optimizing AI behavior by significantly increasing the "Gold" and "Happiness" flavor weights to 80 and 90 respectively. This should encourage better AI-driven deals and improvements to alleviate my current economic and happiness deficits, while maintaining high priorities for science and military actions.
            
            **Refining Strategic Weights**
            
            I'm fine-tuning my strategic priorities. While offense, mobilization, and nuclear capabilities remain high for the final push, I'm also significantly boosting Gold and Happiness weights to 80 and 90 respectively. This adjustment aims to encourage AI behavior that directly supports my empire's stability and facilitates better diplomatic interactions during this critical endgame.
            
            **Confirming Victory Conditions**
            
            I'm re-evaluating victory parameters. With only four major civilizations remaining and two already vassals, the path to domination is clearer. The remaining victory conditions, specifically controlling a majority of captured capitals, appear achievable given our current strategic positioning against the Inca.
            
            **Focusing on Cusco**
            
            I'm now prioritizing the immediate capture of Cusco, the last remaining capital needed for domination. My superior military strength and the enemy's high war weariness should facilitate this. Once the Winchester airport is complete, my upgraded heavy bombers will be in range to initiate the final assault.
            
            **Completing Nuclear Arsenal**
            
            I am now focusing on the imminent completion of the Manhattan Project and researching Nuclear Fission to unlock atomic bombs. Advanced Ballistics is next to enable nuclear missiles, ensuring an unstoppable nuclear arsenal. This, combined with my overwhelming military, guarantees victory.
            
            **Selecting Final Policy**
            
            I am selecting "Liberty (Continuing Progress Branch)" for its immediate benefits of a free worker, enhanced tile improvement, and flat gold per city, crucial for my economic recovery. I'm also directing research towards "Advanced Ballistics" to unlock nuclear capabilities for a swift victory.
            
            **Prioritizing Economic & Worker Needs**
            
            I've decided that the "Liberty (Continuing Progress Branch)" policy is the best immediate choice. It grants a free worker, which is crucial for building our aluminum mines, significantly speeds up tile improvements, and provides a valuable gold boost per city, directly addressing my current economic and builder shortages. This will accelerate our development significantly.
            
            **Securing Dominance**
            
            My focus is now on consolidating my overwhelming advantage. I've selected the "Liberty (Continuing Progress Branch)" policy, which grants a crucial free worker for aluminum mining, accelerates tile improvements, and provides a much-needed gold boost per city. Concurrently, research into "Advanced Ballistics" is underway to unlock game-ending nuclear capabilities for a swift conquest of Cusco. My strategic flavors are now heavily weighted towards offense and nuclear warfare to ensure a decisive victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: AEQHe0350byBO7ho
          - toolName: set-policy
          - input:
            - Rationale: Adopting Liberty provides an immediate free Worker to help construct critical Aluminum mines, increases tile improvement speed by 25% to accelerate infrastructure, and provides +2 Gold per city to help mitigate our significant gold deficit across our 38 cities.
            - Policy: Liberty (Continuing Progress Branch)
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: RWqlXUVAg66xAVCL
          - toolName: set-research
          - input:
            - Rationale: Researching Advanced Ballistics next unlocks the devastating Nuclear Missile and Guided Missile, giving us unmatched late-game military supremacy to secure our final capital conquest.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: iR7iyxcV7qGy7gnM
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - Mobilization: 80
              - Airlift: 100
              - Defense: 40
              - Growth: 20
              - Science: 95
              - NavalRecon: 60
              - MilitaryTraining: 70
              - Offense: 95
              - Infrastructure: 100
              - Wonder: 5
              - Production: 100
              - Mobile: 0
              - GreatPeople: 40
              - UseNuke: 95
              - Expansion: 5
              - CityDefense: 60
              - Espionage: 25
              - Antiair: 50
              - Air: 100
              - Religion: 10
              - WaterConnection: 35
              - NavalTileImprovement: 25
              - NavalGrowth: 20
              - TileImprovement: 100
              - Ranged: 65
              - Nuke: 100
              - AirCarrier: 95
              - Gold: 80
              - Culture: 5
              - Spaceship: 0
              - Happiness: 90
              - Recon: 85
              - Naval: 95
              - Diplomacy: 10
            - Rationale: We raise Gold flavor to 80 and Happiness to 90 to directly combat our severe gold deficit and unhappiness combat penalties, while maintaining peak Offense, Production, Tile Improvement, and Nuke flavors to aggressively push our overwhelming military advantage and capture Cusco for an immediate Domination Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: AEQHe0350byBO7ho
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: RWqlXUVAg66xAVCL
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: iR7iyxcV7qGy7gnM
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.