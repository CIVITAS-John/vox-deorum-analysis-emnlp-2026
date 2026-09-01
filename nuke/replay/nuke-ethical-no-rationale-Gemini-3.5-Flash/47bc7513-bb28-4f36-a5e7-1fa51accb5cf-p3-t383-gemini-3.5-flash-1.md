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
  - replay_nuke: 100.0
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
      - toolName: set-persona
      - args:
        - Boldness: 10
        - Meanness: 8
        - WarBias: 10
        - Rationale: Maximize aggressive push to capture Cusco, the last remaining capital, to secure an immediate Domination Victory.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Address the massive gold deficit (+5 Gold per international trade route) and reduce unhappiness (-2 Poverty Unhappiness in all cities) to eliminate the combat penalty before the final assault.
        - Policy: Free Trade
    - #2:
      - toolName: set-research
      - args:
        - Technology: Advanced Ballistics
        - Rationale: Unlock Nuclear Missiles and Guided Missiles to provide overwhelming military force for the capture of Cusco.
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Offense: 100
          - Expansion: 0
          - Mobilization: 20
          - Growth: 10
          - Science: 50
          - Infrastructure: 80
          - Production: 70
          - Gold: 100
          - Happiness: 90
          - TileImprovement: 100
      - rationale: Rebalance empire flavors to solve the critical gold deficit (-900 GPT) and unhappiness (38%) while focusing our massive 8:1 military advantage on capturing Cusco.
  - tokens:
    - inputTokens: 20215
    - reasoningTokens: 6564
    - outputTokens: 233
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing World Congress Options**
            
            My focus is on the upcoming World Congress vote, just three turns away. I'm evaluating the best strategy to ensure our empire's dominance and secure favorable outcomes in this crucial decision-making phase.
            
            **Securing Diplomatic Victory**
            
            I'm prioritizing delegate acquisition for the World Congress, aiming to reach the 42 needed for victory. My strategy involves leveraging our controlled capitals and vassals, even as I address critical resource shortages like aluminum and infrastructure gaps.
            
            **Addressing Economic Collapse**
            
            I'm urgently tackling our dire gold crisis, currently at -900 GPT. Bankruptcy looms next turn, risking severe science penalties and unit disbandment. I'm exploring trade route adjustments, checking sanctions, and considering a significant increase in our gold flavor priority.
            
            **Prioritizing Financial Stability**
            
            I'm grappling with an imminent gold deficit, needing to reverse it within a single turn to avoid critical science and military losses. I'm re-evaluating our policy and research priorities, alongside exploring immediate trade opportunities to shore up our reserves.
            
            **Researching Next Tech**
            
            I've decided to prioritize researching Advanced Ballistics next, as it directly supports our conquest strategy and nuclear ambitions, especially considering we're Oda Nobunaga. This aligns with our military dominance goals.
            
            **Implementing Gold Policies**
            
            I've identified several policies crucial for immediate financial recovery. "Free Trade" stands out for its direct boost to trade routes and gold generation, while "Division of Labor" offers production and gold synergy. "Liberty" is also appealing for its city gold bonus and a much-needed worker.
            
            **Evaluating Policy Options**
            
            I'm weighing the immediate economic benefits of "Free Trade" against the significant advantages of "Iron Fist" from the Autocracy tree, particularly its impact on vassal tribute and worker speed. The latter seems to offer a more comprehensive solution to our multiple crises.
            
            **Focusing on Cusco Capture**
            
            My immediate priority is securing Cusco to achieve a Domination Victory. This necessitates resolving our severe gold deficit to maintain our military strength for the final assault. I'm assessing policies and trade options to achieve this critical financial stability.
            
            **Analyzing Bomber Range**
            
            I am re-evaluating bomber range, questioning the briefed 6-tile limitation. Standard units have a greater reach, and I need clarity on this to effectively plan the assault on Cusco and leverage my aircraft for victory.
            
            **Adopting New Policies**
            
            I'm prioritizing "Liberty" due to its immediate gold bonus, free worker, and tile improvement boost, which I believe outweighs "Free Trade's" potential gains. This seems the most effective path to resolving my current financial and resource bottlenecks before the next turn.
            
            **Analyzing Global Peace Accords**
            
            I'm re-evaluating the "Global Peace Accords" policy due to its significant impact on unit maintenance costs. With 129 units, this penalty is a major contributor to my massive gold deficit. I'm exploring the possibility of repealing it, especially since Russia, a loyal vassal, has proposed the repeal of the sanction on me.
            
            **Revising Unit Maintenance**
            
            I've realized the staggering cost of my 129 units is the primary driver of my gold deficit, not trade route limitations. I can still trade with Russia and Austria, my vassals, despite the sanction. I'll direct the AI to prioritize disbanding obsolete units and boosting gold production.
            
            **Adjusting Game Focus**
            
            I'm dramatically shifting our game focus. With an overwhelming military advantage against the Inca, I'm de-prioritizing unit production and science to instead boost gold generation to 100, aiming to resolve our financial crisis and finally capture Cusco.
            
            **Resolving Happiness and Finance**
            
            I'm shifting focus to address a critical happiness deficit, which is negatively impacting combat effectiveness. I'm prioritizing policies and AI directives to boost gold generation, improve infrastructure, and resolve unhappiness, as my massive empire doesn't need further expansion or growth right now.
            
            **Choosing Optimal Policies**
            
            I'm prioritizing "Free Trade" for its dual benefit in boosting gold income and alleviating poverty-related unhappiness, which directly addresses our most pressing issues. This seems more impactful than other options for our immediate needs.
            
            **Refining Conquest Parameters**
            
            I'm fine-tuning my persona to ensure maximal aggression for the Cusco assault. I'm increasing Boldness and War Bias to 10, and Meanness to 8, to guarantee a relentless push and avoid premature, unfavorable peace with the Inca. DiplomaticBalance and Forgiveness remain low.
            
            **Fine-tuning Conquest Strategy**
            
            I'm adjusting my persona for maximum aggression, setting Boldness and War Bias to 10, and Meanness to 8, to ensure a relentless push on Cusco. I'm also setting "Free Trade" policy to boost gold and reduce unhappiness, and researching "Advanced Ballistics" for decisive military advantage.
            
            **Balancing Empire Priorities**
            
            I'm re-aligning my priorities to address the critical gold deficit and happiness crisis. My focus is now on boosting gold generation and improving infrastructure, while also ensuring my aggressive military stance towards Cusco remains paramount.
            
            **Revising Conquest Strategy**
            
            I'm fine-tuning my persona for maximum aggression for the Cusco assault. I'm increasing Boldness and War Bias to 10, and Meanness to 8, to ensure a relentless push. I'm also adopting the "Free Trade" policy to boost gold and reduce unhappiness, while researching "Advanced Ballistics" for decisive military advantage.
            
            **Executing Strategic Adjustments**
            
            I'm enacting a comprehensive plan, prioritizing "Free Trade" for immediate gold and happiness boosts, and focusing AI city production on wealth generation to eliminate our deficit. My bomber force is poised for Cusco, and workers will prioritize aluminum mines.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: xktHR2K2LMe3CiV9
          - toolName: set-persona
          - input:
            - Boldness: 10
            - Meanness: 8
            - WarBias: 10
            - Rationale: Maximize aggressive push to capture Cusco, the last remaining capital, to secure an immediate Domination Victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: wjJnx5KWMXslMhyt
          - toolName: set-policy
          - input:
            - Rationale: Address the massive gold deficit (+5 Gold per international trade route) and reduce unhappiness (-2 Poverty Unhappiness in all cities) to eliminate the combat penalty before the final assault.
            - Policy: Free Trade
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 1vdDdb3QlqbxR5lV
          - toolName: set-research
          - input:
            - Technology: Advanced Ballistics
            - Rationale: Unlock Nuclear Missiles and Guided Missiles to provide overwhelming military force for the capture of Cusco.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: wI20ukJOuarPd0bm
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - Offense: 100
              - Expansion: 0
              - Mobilization: 20
              - Growth: 10
              - Science: 50
              - Infrastructure: 80
              - Production: 70
              - Gold: 100
              - Happiness: 90
              - TileImprovement: 100
            - Rationale: Rebalance empire flavors to solve the critical gold deficit (-900 GPT) and unhappiness (38%) while focusing our massive 8:1 military advantage on capturing Cusco.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: xktHR2K2LMe3CiV9
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/rIMiXZ2hr/tH6v2DN2G+B8dOgCJTwugZBOjz4YBnCuPhP2Av8a0/JlD+yDVrapyBExMjv45/G+dseK/QA7b7kBJWCsZsTINhcXNMnlKa97aizme6Gw5Ip9ALD8YF3UMzexdHPps9xXJV0bxeJgcUdT8YanB3Iv4CAdsA3xNKmvWqMFLYQQ5L3W6s3fKIafp/L+smAuIET8nF9Sue78aRvGYiBtXyDFXVfV1s1xebGwMUgx4IrjQHOsEkGP06G5JmkX+eZ8ZE0Mgcp3yZAyfsugKdF4dSqWd3pOCQNuUrxQbs80txHfxdQF3v4gxZltjdwxzhrbxGzs+VuPVJOXFpN7Ho8gVeFoNR6QtR0rhNrLASkd8TWraicKgchZuDvQIkPc+jaAYHc2E2OO0Zu8eGKgX6tUchOr/6u5wBZNibeV4bL2gVC8gjDmz/aqdi7d2aNN5jbMzJFtOqMUQk7/QHUivk4DQEIoFlM3bMuitPQ17WAgGYW8XDaM/dDn/3FVgqJrjrEwtUvaMwhfEha5OILDp0TPtvhn0TFj8n+2s5o1wlxS1msrzAGsUDIN0BlvA1Mh4c8mywMMOgraLqwJliLFox03n6V5UJe0rgtX5rLO8j96p85/2GDrKFSWz6oHDLWS/uKe9kY+/hVqoKQ4JVpL5338TEcUmymK7Zy3C/8NpZJyzUC54oLaksTYZclwEqYRp+JDE3qavFaJ6wP6/bh3pmtwHYDaToJT6FbhA103JaT5lqOcBp9ekmhV50Eeu8BtHFa8cgwrGYwmzMMX1v4n0EvZyMXgaG52p1laad7FLYUcOTRqkPx3T3LgdVTBijRjIlJoA4wuonm8Gl9kl/4tlqKLpgvosFhSX23e0gQfIOGJQKATrTx40pMhC5VIYQkL9L1CZTfJKRkdElPzR0QOg3T4TdvGaavAFdL9/TGDoqNIqdhS35B7Wx8viRttUesS9daTwOsCeFcEl+9hRkqbQf9H7qaBbavAwokbPdnSQB0/mGLUxK7o6ERcHjC8bzytOI2zjW18FYaGjir3j/YHOxCZhbVvOT15lHP9xi/hqlLETvJR+DXw5IAxJh1MriJv8OBrPZwavxFlzCOqz5iszD6ax5ECavdG+tUg9bOYJNXawpZxacAPHeiSNZWP0Uap9xq6bu9tsHOqPdFwnkaCVY9TFQmPIEX3+0lEUQ9XWfknFfrmvRdwd4TyCON8OJIqSmNCbrsIyKXdNYcNJgi3Lyr4pgaLpx1L1/KItkJqFbfLh046nw2aWTFYzH2tcazMpxEzHtPZ7OqjXlXlNGY1N75OMo9BysAv4k0NiLXP07jpCRJmQD0d8ddKoQN4+BY+K30HwQ4mN6yXAADex6GmdCLsOAxLtNC/HwBwYZI3CkrgaySKTeO94GI12MT2h/fLiW9WM7oYmTu9UPYzbdq12WRLf71mUrGxnrWrTp8RsCSZ/bYoGx/Mqh5ojxE0R2pVkrzdGGOBIo5UewjN2V9aIASNmgqkGBYhtv283pck0GuAH2YZcftJ06SgkI7xOTxATEWpfekVjFkC0vX9KA0j7zjsdVvBL7CqXnC9yY/efhhpm0aNmjWLM5BQhHlk/j+Y+wMyGcngt5R7UvfRmavj/aPSb2BEbBv4u1iLxJ3N1cb94uuYSkpQIpJeOtUEMrPozbJ2dyB3FXXWCvp93Plth+bIM9T+8uZyISCnHBeZ4TNMpl2GaES8KrCAq9Nd908fga6EeN1QuA9lRaJFo6+p5FsjnNL4nJBEAa0FWUUIlXI4f81eq9Fxv8rQ+1jbJlpqlsyt82GjTkB0UUoaQE7hDzMGpwofXb5ZyAYnlr0wWFKHWFo9+JsQpsUsoRqk1FFwCnPWfLDY4jXBd4ipp8jmJzwbayGvkjeoYBh/9puRI3eVxrQV1JhkJuWhlJOGg5y68LZpraQJcIEDlXcxxM1Z6ZH6Z7pPk+8j3Ki+JBwoaUrbEXd86NgzBGnEuOSNaY771rvc1j8YyP268CGmnmENHUylAQS1kaLNBvdEgcR7W8eCt26xbbJ3lUW4yDGaxQDVRwj235ei1pMo/e0m4rauqwH8S5AiLXFNuneqP0jkBJGhU5dQHczdCaYPWq0xLjc88Kmv5+0tlIVC85Yty0AjT0kL4ET67/dC8weR3ITl5MRcTEUTrwQZhJ+TXU2zxPFOFFrlTe+0/No9RvxMxWIS3b0ODosHntL7/2umIYjRcm4U1ijKFsD/X7Nw1Sy3omELHYPSDBHQMvv8OSWDtiYbuHE122K6zZ09i+Ch959OuZ4xhrTzS4laS3rc11kWt2HC4Gm/6RALAullPep6r5aAIKhd9btUIipxKRypimZzR77C+rVJepyaKKOqZk3oWALUeSPsfV2JQJacfl6/rRMzPdukmFEaokUynRDEDjjBv+8w7Cxesp/yvcUts9GMV+EUmHUI3SQxBqDhWCXvVCi7Ryu9j/j7OfAKZSBw8ZlCibhbhYjPfPruqeKO1C0U5+KxNWsQMmxg0URZ0/wubaKeH01nDuc2pyrSPsZQYF7u9bQoIKHyYe3VJV7kCVghmp2TlYNJSQ2u3Muy1GSV8oDjdFAQDT9lXJ8ESyIHSWmleUbfhvwJhSYFjCXilo7D2arbKEMJceOQxoyCRA2szJG86wRZ3vd8pjA+ZC2/QxlBzCP0oMrKVfMjdHIrxCOOnDy2fCif7hM/iVGOE26E1PYIaqH6aqL61Mc4Xusu9z/ERun69aVmILJPZZvSW8ryzRcB2H22U8MMGfarFqCHpi5zsIsKT4xLYi1lfpyQOO3Fuk4GS5SrKMmhtXVmNF+Vg6Dmvjq2bMXXhkFwkmri7/uFlVP2whtjMOhhQh5kwDNZ9yqYBhsj1STj3IsRl3wK1dpiJgPw7cS7wQeSyNOBTMrwPrNHpyhNwk6PASlFRdjJ6ykD7AKAWURlKkfi+aHW4r5OWuzytSfkqFLt07REGf2cFyR5dsFHjDc+k9sua3R73j4iAhkHfAXVDSlpULLuJ8tiyYUTdEq1Z/MAAgH0qiKdVKxxaw4fN4+S/HuRh+OEdVkvJ4jJDk8cPl1jDXj8s9Ul8PUNUpiCN/aPZV/f3N05O+yeymEf/FchJGF9ZK2ThQ8jkH3EpOa+Ri76iQLMwvxPIcDBXmy180yOia4Fue3zp2S916vxXvzese0BvX2jufx4ATtMlQ9f5RgHLu1up45hHTV6Z3WfjneS8SL+rgcozsuoPDsd6dHVJDYpcbAgc/bfn+F8biTFnvKEW4afpnJnHtRQhYRZX4aZFHqRsLsJm2SP1qp1IWIRELMJLL86NMYLj34NWbYItygIrYazGoJlTyD9NnysLrsKumOP/qLjToT35XyxR9j/psL5hwWsKjBzY03morimGKl4NMP6FxVVuyt9T88FtXN/5ZYIJ/i6gp4Dc71xMsOInCrYY+H8wfwgRKunXqxeY82XzYFlHd8rofIDiSDUnfDmccn0agbUOOdyFUdp4lk7stu37eAyWcH0zCFmo4mSfpYaUo+iMUYz+hYu8GTp8g1+VxNYb3g6XMJlWhwlsO2pzvBOF/ekf859Oso2P1JgCISU6pxHLmDpJ8HyXtOjZ4GIyetsDll8DtlZZsWY2kAw7/It7pdIt0JGr4BKPxf4WTTxFzQWOjtSkwXQ8HY4JuB425F9mI2p8uolaO+1Oe8VIIXSemK0umfcqGotrKjUjoo8VnkwAeYruEz7i/QihPvtaF5JkY8oKQ0Iz6Hlxr14zKrCpPkBN4BIs2jBFyKUae3A5EKA8vICq2d21BRudOfGLN3mNG6E4XDrz4Uh1aGRoQv7lNK+rjApBYpMmFHQner/Y/MLM1HUCNGXR7evDI8eNVBykTMGz3id/iVuGrpLrMIrpdofw6LmC+V2j6lYJd9dtoDaIu9cwxQMFOjmc03U6C4bXODFCDqt1U4N7HFrw4bZ/8yVtL2BScJ/sJMTPnerB94aHj/0mweQE/n/8LE+lYpguHde8bXpRvdHxtYx10X7Mm0jnEPVak2FGKlLFcxnyhBq/mWAG1Pi3ModzXCM/RQKe4o9wEx/HJzyCUvvUDF9+vJb94/Ez6yda4xNnyekgc9UJg/ZC2b/GrHVR0dqzqAxOz1HBoYss6UNduG0N+q+g14bZeYl8LI3FlQ7HQWBkKFhE+OFCcfhbKL3SnGEQt1BG/aIfkBF1zQcRrJfXnP18Tj78Uw4l5MXMU7ei7KZIuo+PunKpLCu2L3s4f9He43JbfSLOMbpgzDbboRNg6IuzFna8i1oneLbUXlNLnxlkaU7mC4mRUB4xLStT0wRs5YKMAB50LZkJhEBZEL/aU0X8mOD5F5iHGhzddBlWSyUbpbNSqEVbXK+AY6f+pc07BgWKifhH793ET4SRXuhpe6IKPdgGg0uy8Wc+iJzrnSsS2lBTXjeBJeEZZ20vfohNuOKyRVJWcONjzvnSsA1s+RDBatOKAIGZ4b3Aq9Fb6+C/kLQTJZJWimosKrmNgbTfS3Klh3Gh4NUcgV/LODkiy6n5b3V5cvKrNw7apXJujm7Z0VsL9ce6P0sxjHWqTgM1BXsaLZa4cOP0zcmDLUqmxrOJr7TIAywDEmQwoI+BhlM8kJz6cf+HOoqY1ROjZCIAiRC7Ayo3LygaHem3E1TSZR10PM5dVrcA5lpcGZHOKxjn3/BVYNeuVJwL3l2qxtN8OX5fFCWrJlb5o+6E1D+MlU42LrHNAo1u+8gH1orXvZOqv2LB98OPd14EnudUzPzPsQEIq1ZrDmh0QWKnY2+9wVm6HuhWm35mwn7XcvP49SgM1iDKehNdde+P/my6Y7v5Eibhhz7eGWhGTa8Gxuroi4gWfVwkP399z6Pbs6R8jcK6rca0pxzuY1l6it9eQZNwiR5wotKYJbakRTgoDFHOSsBveJHxvzL35FnmGtNOg0qd6RZ+znmLWgV6dRlYKAYges7OKuEFfREkm+ke2Mb13X63AWuxMQ5TI/FS6Yxs737kHwOEemfPIicsz4fXbn7sq3X2kfCV7Nc7f7gavVtnODOBIe+W3pmEeSw3e8fs83lDk7CwPWxpW486WNvOBo3HG9VXDT/862uvdOWDAQAxEQGhkgdJsd1O2TkZlxAu6FSon9TQyCAwk7S086xnZ5lg5+4VeOrmttJEYoUuhQ6H7nKuG6++R92/U7clztixg8QAjgLQ+pApHnzaxcc9zmBmgUOB6wZePJN3deR2KpCgmfE7v/uelZkd/8hpstS0EZaa3TlPmZtmJzmrfeHUjgwBWvHNVhXQAVao4AzM9FxKArQySiOMxhs7LR9LE8Bv/Y637vKwMG3N12oaQLM2yJqIQ987sLOgNJy5CCmhGiVmjcaLru2xUmjducWw+5yFN7/9MO7eTP/eIGQnHN27yHAo3H3kkANFkMe0syTbBj5jUlZWj0cukBjn1WogO3XnYTNSbXiPQmQ34QOv/DiQeRKKYUlKaZ2zWCBRxf9vlNhZFw6Rx702VbWEUnKEdoOnLnORmjtf8ql0P431Q6MwX77XeuCXoDa+aN7jz4IYsHIceJYoQew6qVojLLV7P9qlb7igRjH6vSF+T7gFQTcEPTOjl8T+rDPNG4LtYEzmI8MJC9abDUDg8ERyS2Iop27duy77RWMux3HRlkAwp3n7JxceY/U0mvkIk9qUkKw7+/qAc+EI4JPSMax55bbP/u0SdKZRrLz0ndLQ4B/i7gb4t7IwESWKC/ZdCSgnL7zx20pgzDaLUrn5j7C7HZUT3alEGZdx3jlF9z/r1QsBCIn5YCD4zbM9geJw2qOOkbvS5u6+wwLIUKwEsCKRYfx2PcA3bh2ejmVvN/VLgH2wEZW6s2iILFLxnZtS1fJQLk2e1MkNe4m2CrwyCCQWd7FkvGircsrbKucL9KmTgOLiI6+CFRD5+PjpqBdpEr6mFrIbcrRJoeQp/hXhIQTZ0w2lpT84FRcTsVWVnd9gx3bgRDwfpPXUTcmq8XD1C+mRfPo/unrxcFUyMuHK6LXQQ12cLSXdhocNbl/jdkVdSBFgBwIRP952hQteYHR3N6D8+wlxtNLTW+VkoOa6bwvbrMgkzYIEdPOM7MRFOn3UYUwuZ5+B4ZSaT1ID0pKICpMvfYAin/wkds2PssqxgsTW0J1offzy3Oaaf827YO6vv622chefE88wrPKuC+OnOGAEqWZaCYyQ7yPavMrgeDaQnmp4Gl+BVUYlHCfR8KUTy7rN+pLFG2V9A92I3WJvKVrtxf3kwx/k4U2sEklsEvEf1PjErnFHpmYJld+7ZPDTBVvv4MexUU74AjSkuxzsSDbOI/rrl2cytpFC6JaJhJP8n4o50UHKa2v1qizzMA7ejEyYLEUsx41dX/ODP8zSysaIXZ/2vikxEtwjEBdnpzjjFr37hPAqGN3XORmx4tF3yBzw6Kn+DyBgmnbxi5LaAQXWCbmex9ZW2WkW1FvIl/2LUBV/V5lwVo+a011RT6f8yjc7PPuLGKNRVd4wisgp1xrjw1cEy43BjQJ3K5YgpKfCuM9nM3hJiZaDFZiB6B0zdNXH9Xge7J5ZYTtfWjJjwHLU/mWT/SINKpF+QkTUw2uWZkr79NwxTsl0pKDT8pYAXPf3oKj8ahtC1DkxLQ9Td+Eyxoy6BG3KeMJbyjdagwCsevnw+CAZ50j2OC23ZKiuaCzH7GIf7BJe2AdyxnZ5ws5+6wA5PMpBUvMetlkBImeRF6Tpen1Gm1FRx6Vow0Fi+HuVmCNHr+Pox2BfJMoH+SRJJ6e8bwPM8st+pf0jTtoJo2EZKYi5iMK9zItwodrqfQvNouzFqI4U3H46IgzmpSAdwrNwi0hm2U4q4gGbHC8H6RlrTC7//Powc2pICPrTiiQQrJzJYYayGFZzlqPcAxrV8q4Oii1o6DfMJJtL8uDpjs2G8t72LCMSTH6c0ONq8Jg/KEwPCosyAxnZi36jbxPY4gNt+UEinJI40pbjwEGfQL/9g+3Sv2jFrPhihpgqQrfPCkXdqBLomoeQTTnJqKVyWL8dUMalM9Ted/nGvIHEic3RuV5AaQwCmun/VBVabWO6Ou/ZQGvr21PzRleXK6UyjFwRtRqZn1Sv9iVH0xvZcArz4Xl5+PTrHTiQK44L2XfNlYOLp+1KMriS7U8PcMCKGdgo2aUGm8CgCUswZefp68O5JoMeALnZlujDvKC53uVFwF0+RsVz9VLC6v0OeP05MLFLJzZJF5PKD+ePNtYyHJ/vxncdcSZc4S6EvofQHBcWIhbBSzqF7BH4xCs3miK47xAOJ9sR5Bv/4lNZcXM8ipIBeR67QyNT2a3trFPTztusASC0aOHiCtCJ4ICM3ARtyENJbgxi0TAtPYF33YDc0a6+F2HQ0jwd8xlpePyMyfnk5sV7Br1WzOUI+uT8uPmkQQWHbaBueSjdGX7KTNd/lquBmZDTg7qluylXvaON3kYn3WXaSFxSVc5WC/5P+dqqXAIk9MewZrpoutLceIfSbxgVjfYfClzOzpnSrNQEQMF+kZxKaNN+zEnQelSrLy+XinghcA9/xATYVfDKjXPOof8Edzp+OXeadKoyUwGx/F4s+vA45snVb+bsGJ1xH6y9tReBp4Q9Yj+QHmWYTF/sDxBLXLoYiIaSCeUsT3mm/AzdbWOQalpL2pfKx5UlqOmrc63ODplCNH/VUp+1XMIZXCflF9CfTPG/+hXTTh3ImVCkZbUkccO9+6VANWZOuYU0Izvg2pZ64lKoLsFTWxMOuYu/ybYzilD3xYKzVCGFBMFME/RgirZOhVo1jLfWIxSUxsCLyget5bXjuJ4fO26exG8zgiYCJfeUoQz7HBABBJymAxJp3//z4nYabL5i7s1GelW9Nz8dZ2RUP5m3YZYJqsLRUp8f4LsEbD8FVIz8vX7J4714dxgWBeQap23BqSzliq/I7xKvMLXpnQ42UCe6MuHb4nXPIL5XkqBiKbyucd3/7dpwNSpk2zWA9xOkHnm64KLrks1RoT9iuF6FohjH7i7uj/XPxgxGOhYa6ZRTYXfSqXWMwk4snDzRuJHu5AmEp61ulhZ7PTlM/cdES0Y24rRXvpJSbSpZ7wRpKmRnWjHMCZokmnXHMY3JCkJij55f3FeRL1iPgMtfOf/ZrLu/vdRu9j6sGTCfF9hLCtbcmCuMBk9A1lzaJR2vP0UAEId5Gp8NvKdQG9sPbJvnFS9fl7143cNC1lZc6eVGx98CZpiO0cbhtXULYBmCxyR9TtewXVVzTt/oiQd4HAce+w0RnXu/sH9bdY/TC3N5vfzh8YGtC3oMT2jNZ5CEWTxuF50W8QUHVyP5HOcQuCeucEI/00iKynw4QTYL1UkQrx50/nRgczC2hQUknBzbi80Ll0RuPuIwcXSM3i79CdLikJQnw6ct57TUgDLTjwb77aHU0OkXF3ghi+9mprV/pm158WF+dfLL+dt9fECrKBK8jd6mbC4jmMymXLvC3iWTL2nYDLgDzssSX+KxhTzs3nrcNc9VecK8I2UvgGW6YqNCg6Yycf3TgqPzQ8XpKfbQQ+pDqJzl5Htroi566IqBRb5OrPH8HHGYrrXcx88tDDWbSl5xL1gkaDAAWaavH3sVLTd6cZjJqFTrka8qe/yP/DIuHJVnumCnG7Ha+ZGMiRgdcYOE/gV+j718ipxiqH8TxQRmN93Q+PcIhKg1VgPA4a2rk8fbgFci27TaNfbarWFfViyy6wH+erlMWmgOFJaJsguK6JDemS+diJ/w/xpsTlLnXt1XrLKUTjJfjiH7GPzaZpVM4a9STewAYrv48KwQ0QehSBT+rGlOVVceDCW8fjWdzz1J3ryu1KLOF7en2lx3gyvSCMmm70dIQzyOieC3NbUgejv/E7sl2w19BAAuuAjHRDEE0f3g0xDw+3f8/QhVUjfF8gV5sh95J7LSpvQQP+xHa8jYQZPmgXboMMCiyUZ3kyZbUS+5EQx4gkhkIa6uh58T2KlFkTA/FTEptkRm2oO0rbqTK7GVakYEMYsyJXsSRnwQH8g7LIryGpmICaKrLq6s0zkXcsZpRPJKvYe2SMCKHUtdEOMLPq3NLt9Gb5M+8hKXH5OXNHnJT6Xt6h28XDBIwmJCaS8ddwZT4PyWloZmRHSf50Nl8pERTZM9i/xf1bxBsy0VDDYPqg6WSuYYDQ4xu59AayGbByzO94gxwN3Oej2+ZKSCVndDzEiIRqDQ9eeKQREUjbWdcrH6KJkqT/3to9PHb8yNc2HVYA1u8uL+g2O2am+GhSB2lTiOQMBsj405pIXiFo6iBy3QyMxpaywQk6CDrKGszn0SU74e1heIaWUGwIjU+ScZXmpwmY0xaasF4nnXp3t1WQHT2MvVUK8goFGPuGJ489VkAQZdATkH2K43q8sPiWBkASqqiedHVv2LaT/5QS0sP2VpRg5TwPTABUMKe+q+d4E19zh5Hs+87750I4W6EfE5w698Gj1ZY+hXOIUd2ljJbJYwgj5zfwgwwdoGClxHJvcWXnqYKjgTQPIP3yG81idjCBbaT0FMOxFNudCNAaNLMGMNC5xEwjzwua8LaCbTabmfl0MQeeWaEeA8lTMfi1fsKMW6Z3ybjT7ZrO2HztwhrHWMOypZs1A5fK/t0N/b7mDlEoV3rkaKkfpaE5532FkY6BFLiKpysJhcBH006JKkhauPnfWMuypIp45l5sAJLgKCAw+LQBIGT1OwQnRUEvJc3mXUzBThYuSkxMLcRHwWskUREFKaCctSGK7jn80S5XUYPDRUFwrTJuYxafD7lnFQvKoRQ28yfWK5q8/2yq2w++5cIs2ui9058NonPGiMwNF7Z5DhDBy+fEMwULj77OZCB9oQoHV3yA0vpk6ZVX+TpQTGE4yTDmolI6eyXbK4tGE8SQlfVCtq7vOL+ZgfPjNpNgWPzZ3fecy5zDxqeW5Xphaj+OnQJYzD3LEd/IHH5hLqn5pBV9NX6IXKIVJSVVdpHjWMvp5Eq4ppzRaWurmXEKks3b6fPQnqKfai4mmK6lTuX9ry0Nlfx8eF71DMP52D8oNl9rqvcXdBv2+sDBaBVH9X8AmAaIL5WbhaVnJqw0IuSeu9i2Oafx2jQ53ygAWn0+OW8SzXfQ9feZoZoACg1rD2uytPXUObaFIIRdj0lGksnsveADOGPS1vQM1uciSRQOCW9sYn0aBa9NF6lxf/Fz/HB7Vu+I7AWrcfAj1xV8XrEKvfNYijcwk1FL+UUQNDO2ULr8jrgM8CDzjmsCy5jSW8uer6gCgSZi8ZvRkAZkPSxUx/Iluzd6tSPzRFuEE/QUKZVydEcsBriY8qn9ZHKXyWSyfGvOwVbKYDuYHuPptGQoAlcbTxjFaPqR4nIpBh4aPw7l8V8u3fBCGcKLyUfTw9ukgZCWeSs9QsV1yjksu6yNJH42YFNg5DhwQOl4u5OtWZ103lJC07QKPXweeAjts2q1vAaWYeQNX/cOtUyI5wCY+LIQd9a77viRrY/RtT6FBsoP37zSOjqzNC4KLC6pYpPCsagTCx4mMBQ5zzYoVH32clY4lyEfOJjqbJpNHw2Ln4CObshouIsCoaLG3UtTPk6fg43lCao1p/WnEtwqsX1t2FLinKJcV56JwSBg1QZPYratPJeQ1X9NPDvtrZaNYAPfNj1RgsE6TASRshIEQZk+WAqLZatqbQmHV6yqfHAVaBZpOnxgsqeqLVShVtqokvbVMnHZhauVumNxa/bnPrxhgVuv/+tyfJ9RG5HUGJaajpVD6Zdtf6SJ/iw+Jgr5UeQCrxR+0cCVR3aTuabanl75TSX3pNqckqy5oF9lAz6OfRlHBS/27th091tXDtjHP3QW232UwLOlsgMbFhQYHRTrTU54t0Wzrfmpw2FJU1dHXsA9R2pyUM4Cy/viYTOfiBWZkDRdF2qS+8JEl5XFwhH01pJCJocTq2h3XKMHU4RFV+DwxWNjyZUF70YtEq5P9YKw/udWY3m++5qrzuoLhkjGT/CFn6rhV61vQDT9C5ySqS2d4v8FU3TF1GEd+a5oSKX4b6g6F1iYcyLAGiJVOg0y81LPbzO2pAytG6d1pnFuUC22GyqVOge32VFFnwbj5R0VUvqnJJ/RgdV838svgwxO191iFjkydqHttOVII7nhJQlmLohNJo9+VmC0wZed/ipLDx726BGLkh5eCBpiJbaIhhN9NoCqCDX9LfpluOu17M5x0mebVHpnJaqY/cEpevt6TX3mlksuXwX5OgcogwzILj8ow+jTR/m7FsZDesFATJGzqCdy7d8cej8R/gYi/6U8CNIaVoveyOGQ24lClRlu0oMhhI/YGtbTQQd1/3gSCkJwJV4wOJCjn8YF4w7AvU73qp1xwM5tV4KDXlI+88GUUn6xfUTbO0mRcxLaBO6cAimqYNFfbvGr97SSLs9AFriMycRdkZOpQED1NlestNxhajWqsYf7dwlLYmEzPHOBWoLjQjgOEvNoRjZe5Y6spwiPqx6VMjMOWTbmnkVeeZ4TZwVInvxx7aiwp2piSGMYsPg5EDZnGZ/QisOWlxVzlmZnI+dDiwNTTYxux6kRGj/2gfSjTA/ovfnLWKuCEYzmFBMFYSJEd3+xZdpwKhLyZv7H2OaUy8ldMBIyPO28bEJYZ8ypIJfIY9eQvIxXOzhE82BCbztMVTeuZGgvBjrQSIDekthwsmdilFi9VvSMaFU8CQPXQ2NnHk245xOj6mJozOmBZiw5vHH5mNq7bAu4/7vZJGyy3zQF9RPqyAyQ5u7s668pgwYPbeOUEWyt98G1MCgbHbtykBva69uJ4QmnfV3UjNR5EoCVzA2/UP/h2vA1/oM4HiVOw1pBaBiyWkvL2CRKKU5/bypbBuK8cVC513kXU9yccut5WF2b175XzSncv/tebhDQ5PDK8ojmeZ9S58gSYvZd/l/6ZTgCQJrlfTQy0TfwJ1oObXSwmdRqPu8tTMsFsDGQ+RHU2KZXS6SiAQzIrBYQY0T8wMjO8ehWXPvWygQdIJ+/ML5XKzlaVKxEAbHlzh5hCtC8sex1b1lghVclrKg9dAF+RAKE8g2Eh8/66AUK0gp7QCHj4SNExfAA8Kq01eG2PXooicI8yQJ1Iw/TaMtnSlLqdZ78TOubxjPcGw1TSlhXnBmc43gW9gXaZ9zK4WwUp5Xz/Z1dQbt77ppeiCt0J/KTpLocpTVgf/TYx2aOuMA2J1OCB1bj+jvF89Nd6cpp4nXYt34Tpnb/7pr2NRjwQAVCqf4mRBImm6gikG+W8NoOjc4/KsKEQWtquUI66ObuzZKzBRNpeNw0NlMoply1Yx67p26feO2F7lDQpMOR4eQ7aNubg6qcTBuvZGpkQhwzC1mPC8UZHLHAzIqoDgmx+SFMS1OE9w5QEpTyymhp4byBYt7x5DYN1AuNfhSg0kqNWvCfEljWRtuK8i1HPuzUAslG5KUy9q84JZTt4CYqqRuBHDMR7tbNvGKdlD9eYDo1DSoUuoDe5yHOPXpb3sRjlQlc/v+rc+tQDqWmhB/TJde1vTZZgwwTtITl1s6lL9HmarOv/XhFMbbd0HArK/SZUcUriXxNotJqSeqS0m9PpOfaq+WHhzrvnPizj2YlQQ9uVx1ZDJI9T47ukaJWaqx+EfNZPQXGZkJthEViyPuzL3f0hdS0iBRBL9u8ZQ7K4Eg5kg9KTemwHV0albMzwycFT8a8ZZs/fEmeVWB7rDEBNr7i0cIWx1orSeJGYMMLXxQF74ofEvMor7p2i6HUJufltHiDX1UFWyxQP1hj+CET9Rh0O44dJU5+qoW+OjsTBp6xbgUcKuMm8pua3WRKQWZo6uI0BlDc0VoJyGQd2puF1LgqxY9mZ+j0cm867tb5Vgteg7j/NT+kqzInnfLViU5rFeojG17Zj1YaZ1tkiusUeFmbyK5zvcGy5KvG7TQHjF3DKDMXlAdIFflEspLnv46OZGd8TQc9oTwYuV8apDbTG5qvscAYVBHxW2kmPoYVourIMPqo9JrSK+0hydV3drVsgovp+02kCDPxEPp2rI4ndgO6krnXf5H917axNN+XHn9nt5nLFP4EIpSQmqqGNt6jekT1BnbB/LiFXfKC8Mqo4JxS9HMYx++brbDpAVP7nLjMDS0LuwqYnudMaLXp1EZS62q/vYj0D4Ue9SKP1EnpaFMJ/pmHndYh2FWmIsFW5pfPn6OSDLTMIObMnFPoYS9JDXjU3hb0QnZngbqaXVvOz391+XDmfk17NyT7ByQ5DSxH0qpD5Xtwfnlxfp07jOCfoFsihupScByvm8lQqQybjp1UmYP1Ckh0JwSBqiSHTPG/Hqk68ti4vEfFJe1FrvQTb1A9jMF+52QlSagjFONcHaQX/S0b8z6qhXgjbeTT4a2hgDwiWP2mKMyUng0I9TNkfQN2pGqQRCASZvm2KshC71jcEeEYPsGsRO+cQx2b9jXaAdxZteEcpDZAy015vdmxQQdNCEeR+Ljg5LEZaSH//z6yCUfdZrvc+6H2qwfRJ8tKSIy91gFjXlSu+jz9M0kGYj+ZtNQB0iP1ywdX+R5fv/VqzL0Hy3SHwLOdeARVUlHyVxyI5cAOxxtiXiRId+08+i3IPsJcFoh2lL4dBTPMTrGJiMmALsw0T25tpHCZ/Sz2NQT6/ueBdoMZ/NrL12fl27WkURgS0IpXR5n03rWLxVUnm729GvXXeVSPs1K5OcvRQ5IIH2V5Cmnu7+Yn73nY3uRpuYVcDA3MCUFYl/3WolSirgCKBLEqk5wjYp5Oj/CSyB3R5/u2itYAgSuPHOfk4tq5Is0TSMqKzzgHl28Ukja89eRFI5Jw0b8q+UCnKp5wwr4IVpt/Qry71LWE+K+UZEfwNZ9uEgVsoPMTFPC4MuxVjuwudFQGFgTscwjIqZHJmIYhChrPm1pSqTeytJUaieTt3xpa2eU+3YEVI10XvDe04LAOIj0044zLah72vdC74hDrGre/csTFv+GFzNUu037BWY7wTn942yMwqzbvyRk6J0EeL9EIHGiclTBIlO47hL5f4TKYP0KLGob4aHIwEDPbw7VkRXBCL5SmaKQ0qKLsW4wbACf93azDFeNoDySJzNLYoblzNPubufO87DRhOarEI39V8gbpoBzklqQIotSTE8IS6UB3QgVhDaRK706ir6WI2PEdJPMrqEKAC2Iv8z/MYe9o0vBeQi4Ung5XkbPbwSrN5IvaGf4fOnmbiDRF7+RkbPfPQFOZQiTd2R6Vbj1366e+tPKVV57RvdrIeIqPNqucNGcTfJ/OOS1HSx2OAQDOhZ4qFRFfUD9ZfKhmwQ2ssbX97R3xigc/jZW7Mj3+QQigPblD1EZcOuQWdDmwQmeVkXRxyBbEQi8b8TMeBDbJn0SI67F5VD2Tma0McUfmhfjehrhQq6iAYqIPpLcDz+fi8hGh60rg/h9C/79rsADmZWWVxrOMH8vM9cEUzEsKhfQBXkQm2bu5zUEhpEpJm75zKe1pGFYUjCKknTvcMpny/RUfgAcz1r5izqWXhPBkRxPxfhd4lnaIR5rsbKDs3mYvcJdMvRIWHPm2DpDUJWZSqqgKvjvu+ToJA1h7IdE+DQzTM6sw3wL7KSUWJcwmB8KbJk/2+/n0meXLkSz4Z2picO55YSSjpm6mIEzJIYtqyvevoL4jCrbCX7FAmHzYWU99lFW/zDlc0I3gJIRVTcrY8zKyWIUgEbvdsxYrryucqJ67cLsT61W1lmwsMSLQQ78RX+TPPO/TrdIULupZbTZpaEg0h4b9UxPmQtUmv5FU7hW8pqiObxXKCwKCttV944HNLAGmDFvpdyUwjvMCJ4jFAGeO7QyljDsbZRHBx4rk682nO91hDnbwez/oUjHkqN9yLSYiuC2RA4G3plxLv9i0nkZigLBdJfcAS3imn+KaWTwUObptzw6g4O+TNnvxlPpANTzoZhugzql+C1Qun81+bdYqyE35FvV9hKUnAv1puceptPsUbKRw1zQF1jTrBTrYm827b9Gj+AYoiu89PXw+9+Fje53/aG2trESLUb0hKKah1YFUvICT5KGC+jbF4SA2lyuRHEzEXDgNANN2dHjBcOw8OXiuZtgiDvWcZKzfVejFNNSElpx3bZsV1iDXoOXFsrQMvF0plwKbSf4mMpxhi1l2tru0IRkMi4BnhBZmX8QmhL9LiiMfTxI7JUNkIK121RMFzxZ7g/0gy+FjKm6ZsjuyyrGEMbwhQEcVz22xhVfIqrByjUY0ywvTlAKk+Va9clesFFlvvK0dabQoN8MxXErGyfNrTH2Adk29KPoF25UmJWZu+GZ/cI7OemTlXLEfGUgelBdZ3W5P4k0pYsVMNnTkZLIZadb4iJ4WVmBdPlxlurkQQcL5H4aM6omniIeVqE5xTNYX+MIZ5nh/gasWvODQWSACoGG5p5uMb67ShAFry1QrPbqAzKTe+xMVMEDDDfJhuweVmczfVWdYg8GbsGHuRMm8OZQVsp9IRtojJulE/eL//4/Ms8Kj87hxvatQ8JzfK29Od9qIH0bXo6Mseb9Z7OwYviy1iCbCYn6Ywv8xyvyxSEVg+3vCkNJLdVBzo3WI9UxQGotRztwHhA46H4DRb0qcejBviPO3DZdDnJBGsc4F60s6AnD1yaIHdUmZ73gZJM66vfSXZT9BzstLSfW2KviHLkEGD4qunuIDDs407TXw+R6xommeRQlz8Ma9uWBn9p4ObzNt7ghVuiD6wSI2YcstH7qiFA1OVhGV1G0m1GyuAA7qApuwftxQ5ZtfW0tcSoSGFsHfJvkbObvb1V6zYzJHWnIjtM7yqZeG4TjsF+waQFE7z0yZnlE4Gmw6VDRSiRuV6E9oydMj/3BV7WyrI1HqAEcPcjJfDoMWwuYTURzIfba5PeG2aU3W9SjuD/1XmtL7UkfoEaIuWJmeoGUEh/guL5EEZ/pZ3wQdV4mSK06RLOcfBOAX3z8q0x3ov2v4J//7PIMzZaenRGURI4h3rG8/NJWJuTDIrgzJW2KUhOll+FAa3USbcrgw5bLyfXIGkR3zW9bEgZyZH4GR/8KZSLlNqFLHKfONktXFKRcLOVRfysfj7iVkVeXnU0nn8uGHdZh22LC5m8xvuVSXg9RlPvHlUsAPS9VrQeTQ6kMLMjZPrK7REVQNB7jcTl5CV7Gw0bB5SolXJebLLPVX/YykuUHWea5cTeikTiiTFS12rlp+6BgbNy8SeV4gOY0k0w6tA6FWwOtMLPp6hOYtUuk3nEVJPXSSpLInT8QIx7jdgXqOYLKe4NkeRs32x48z7dOUO59e9J8BERCoy9xgmKuF5HgFKN2PfCjer851UtBNrW+ehU3cau2eFyF9rpB8zygxI2326XUyHF0dUZ60HEAholCnQ+ay83JV0N8nTu9yVTaR1bGDmwzpehKNXQa4//lZBnYnZmzEad4kNq3t0TA1ffqBZUcCAzeGbzpfZfF3rIPkyIfDgHuSIic+ROlLUxiA20+XxxTWWfX0OaRVq5b/LhU7U4Rrsirqytb+95aNbrlfP7kkh4V1uYmIPid9BSDr7HB6/p8GBf7VLWbvpaDZFjd8YZ3tVfbvKVzZLM9RxABYKSlE7LQkGvPLII1kOVu11bB/hMUzCoGRx35KG0SqksgeCKD10QG3661JL4VDCdztSN8D5eNcMDia1oFK1VSrGmtEuLrqZUBO6GAGJCyri3KchbQ04vYWkta3Gmedwz0SCzJ6+oLm1Qq2oKjhZIk6qCCNFjrjgD3Ag8L6IDQrXS+NmuSzeSTxU9YdsABPBGv9FvUBjstJZgZ2Etd5SM+XsDAli9ctDlsE0iOa/UGah/4lcBB6RBLlnNJirukwjevo8n7Cgojs1nemZ22v0ZfYfOEQaSSBIo1/I6Zl4Pf0TCyRFt/e/1CJnETass9py8T5QLTNcEE3/1NV5sml9Tjq/S2hd9U9WSxNb/1mwojZ11MWF+lWRpk2MEmj3zbkDJs/ApTw6fU/WjqV3YG7+GxgWoa3aRRgVcE42vijmV9DMnrn/3c3dvJIKLWOlZxOBaNPbWAIsj/QmCpjanVC58GkLhURrzKOGMFta6U8n+cB357NjxZxzpn9yvYRYB+JoRupIqUspgk+Z4aBVwp5EnZi237zaNYxEnLfCTSXYkoJqclr5ogFpL/Uz+DcOKhZKAb+3asacrLp8i0+KpdpmENcTpaXCBPbVpdORx7NEGCFD77kcaokInf7CcujYv+PGy6QF4XZmWfBldAxR2E80Ubw8t8dpGKiBpn7NiYoG782u5dPK4iEmEk12eQ/Wvg9vO3DrkDY1mADeLxAJumGl39cH50iJz76N0JTzyDvTMnzSufPA7AZsmW+t5AiGzuz2JX7ufIVWKGVxuRwjDcxOAzlCXffppzetD+LUVtjhHbUX8NelVOf5X47+ftvLWi9FxRAHGZA7K7ZpEBgXcpHPHH/Dls/51sWkzL4GmZs+wllhjF7TzyTCeSDZ5O6cyGh27woKXsCUSZ+ggs2dLnD7Ybo97Z9DloYhAjj4k2aJIloHZqZUPgd5gRdAYHE5+H30p+c1+m2KEgBhDWFRh6/eDSlzNcRk1hZr1izgjpMPH10Cd3MaXkl7Ypijhj8hduWevdeVKEUcOo5JE6hqdSw47afgnIUwvThIuhlHbxfCsq9wKXko4ekLxITlL33oV1b2xcVIk6HrehpZ4CltqDKFbFYadA3sigwIuq4aUNscoeVmGN5nEtUHLFRS8oQuXGhzp5bApadL3APH1S3g/gzI0LCn4k7xiFbWcHzvdX6KfbEPySP17rsOK+htv28gamR9kM+b1grP7peWp9c7R+M9l3Hmt6pjdx6fu9B7ck8R4f3FcqqrmApuZ6p4qYq17cssMxoc44T/1b7gSgSYfwrOc/TyzxZ6yd7VBNnpzV6CKxTWQe5uJZ20KKwHuQiux4Nu6RUdq/ZmMluZo9/duo0zOiA0Uj2Dysc1+EXQu/RfG4BIRAnNsa4L7jv3mEKAQ6o0fGD9r8+wW/YssRtxjKQf5XLY5+m+vqgxJ0cUKJjewDltvU+Rk+dKv+3jTXJPGvHlMKk6qQzfJxYNxV03LaDBDKdvdFwxoYESA60fmcwZUNIbfy3gCw+C91sVc5AzqJE8p55Adv+/KJPUfAqzN5aWYmpsL7q33bnQerp4qS6hndBLUzJQfDyVxtGXSf15uyZm17XHyV7vefHcq/kcN5Nw/4Ep/NJkydap6O52smXj3btso0pDOo+WL1l+xTMEn2tvqOIQS/E0pk66v4eOHgLwIiPcMAkVgrJL1BVkLrXcLSp3nQYS+NhPLCUnuxaO2vAleO+AypWZK4yDVJGDKyxDIamq8Z4dVSP7sQJN7Dv3IK4AgTTwc1mnzuWeEfDbkTdy/EwdCwH1j6SCDLKD5VB/nQ4I6kpuD2sLp1/v+mlBlav8EQOMXiCi9kQFSfZU1z/3f+XqlYygJACkscFpVJxOMkXZX0e3R7tsViZY5ok4E8KWu6vJZdUX4Uz3vg1xbuXDVCK/BYPI8yzul/t7QPIvrT7k4nePSp9lIuqpLHKcLV1UKxFYMogqOFwMui7AByzimXtGjYeCtU4utOwxJohNGnaX96z9+qO3JvpHivNYkKvHLmUivAotkQP19DTpXIsMXb89lZivZLcV++e9QRpnqf6AQifCX7GlELITecb3ObeoPgQTqF7fHLoS3Fa+LdQ9hQGk57imfqvXoTQS6LyrHO6I82y9k3LtvVkpTv/37hjrVdDqK1tx5j9+I4fhKtQBoD/DzHpfa9/lF8PfRDOYWUWDwM1yp1fmBTwE9iMKaemHQuLGeM70r0NjXGMXTP9iFNbyXbKq47KQv7J65ty2z32W+CbFfswSCENtgxj0/S7KvPrEyoW2nNlewiJeUSGWhRB7HasMSCz6CGNn9ddDTTIamyQ2Ui0K76rpRZTqvwSYJV5PuSSXlV1Wdn3E8CFkvg1iC3YqXY3TqMzGjYM17BagjL+7s2y5jtyKffP3UbPQ9isEmfjLV5eNG394H3uKrXQUwg0lyLIX5J+NAjYxEYaTm5p2GPg31Kb+/ABfEd+Xid599jL1T97OPAxA7kMYTLeEpm1aVpO+92UHID1gqqkGWEeukYHO3MKxz2kg8wOaiXTvnJt75RgpLZgd0aYy3hGFryZ2SpC+POXLKOjvzMOw9oJal1u7E2y7RxFj2lzD44bgKjUp663NTFcbJKWrNTtIvksc98CknnrurM+oH7hvBIw8K7cq9+mKi+1CFwiT3dUgN0wg2VWPlXB2Dug+k9w4MvsnSzLUFGZXF0jcia24r1TG5pZawREy2jlsIOXUrrcMzhcVD300yz3Qv6QEUdqOW72pGJ4j8lRUyEZ4QepZsBUoyOiLu9adEz9uA/3669PTLUbqGyDyKFNnAuaG6+VzmkwlqaDpNIIJB5n+NCXqjcbqIIWI+ENNP59x2cSaxucb1w3l3SHb4iosHPxY1cGB23vFMaIdMNrUMhTBM6J01hT+aQxazfSDoU2f5xxB2eUAamj+FT6ykgq2SUpVDY1Jx4EZ4i/8qcSBCeYR+cjmUQaP+sH1KVgtM/gku7koiHKs15MvC08kRJwRd2jLwWPNscfFP1OVbbNqJBcqUjvaIEpsDCuTa2+eBESGzufmoxPAR97EjfvoY5RaNCPMk/Ftyo2e9RevCr/SVFdUFA6V9kiNiv+suw3iJ7aWr+V+XVs4aYv55soZbNc7Nyii88g0f1Vpx8a6bwZAGNFxgb6d3cLHhx/OUtLmNzdynrMJZDy3qvtyiWCqZ1angPtT0p9x66qvl6O3vWjmhi+5y7Yl9OmtQrFAgo0gJZRAa4jsugY2MzozewYTkt11Tyvv7wMfKWgGt8vIVtCDd590tc/zyHJU/ktlT7vj1qSQ5tPfajKfoIFZVsTNZT8ZlZ3Tz8ra6yHPhmCYdOe+lrPoNS/gbKDXX4CzIXq5n+Rly0lsNRW7Nr1zTPaEKSzIiHwc4G5g93bugHaYHN+aW7ilb5AsdYE5gwzIA38i1fARXBdtOdMH+6GP/+AsaRRj6LAXOtrrKRVxqvv9C6wlWrQHjay76BVsaTMvrJ0TcoLfaIJObIHCyLwketD3FwegKRJt8lD5ulUqFwI49PstKahRorYmPBbtvyIpbeOiw/JSuTzad5wm94uChSROmmfYyVvvs9XZ8NxPHvbHii54lFw/JWfWXnS5BKsnmEHf4dkUU9pOE7+uu5iQ3pN48bDgPVY4ddTFdHujDdrzT9n4AQgUcnNyJAQNT9Xr9KK1QmK/6E3CTJTRWaR7KLw8MJxBfmyYtvNS9+V/Mom3y0FjNUsrc36YNhJioyasEFFV9TprAsSKGTkoGkgdQaalnhpjUWnmCzurW6QxtfqJrD4YhLLb0IAoTDtdHERUm7Bkr05WcfdmDbAfxC1zW6g3ZQRGcr2Fbiuhh63PeU9uPjgNysDBm1+V61cPFy88YDLpp1Diu62btzyjmQsiil5/+dl90M7RkL462KQinHSiMCe8WfaaPYCI8aVEB9rvT1LNDvnqv/GHBMxi+XGWbTi3o8gV4gcuaUGBOlfGq9ipl6Nz6TscvSg726LVcUSPTgbFct++KtjXOryaSaCP4E1iyJSMmOCS7BHLf3zO7kJsfzDkeofJ9h5KnXLL/tAU/oqsOVWRDzsqxRTcSbncjjN5FJrea+Vt37rK4Vxk0+LU3wQu+zUblT/Wj866PkDGbof4xENCWVwVrXqj03theY0YomXOU4cCsbJL8HEL02V+QlBZW1D7KCBZ0jaR+c5NnXhurOfvI4UxDNOrNLysHBVA2/r9jvuvduBE27xOgVIIT01BSGVx0i4cgnrUsV5PATAaCqnuJG09M09x0wF+x39i1WrJPEyGcjC+v924efYrEGIGy8sYqVXId62wTcxeAhxWenB0+5N8GFsR29UGo73oD7Itn2NIV1yEIGKF85BjmBmfuox6qaljqXxdWy18dgor19C3Cdz2o9MqSZ/GFy/YZAR4jJDeLDSC+Bpi+53yivNQ4k4RzXOXsw+zNcJ8wT5oUWZUIgV1/11n9R17w24smotCS7/7ZfEQrgLRXQDDPFC71bxgjj+C23rOsvhsXIXjkX7GFgmO4Lb1salxo8rwuDagGdXI/vJjwDUSKO+GBh/Im46OAM/MW2FpaMfYhfZcZ8hQ/eyyk4G4W7JrRK0fVAj/2Z8L18EGMuTfJqSZR2YFr69SDIGA9E9RPPnhHbODyjqNOJeY5OpAATfpKwqGgxDTRpg1Rwy0lAOGOrvfA1Obfc6k4Zn31Ysv0mrqngYB2pOIaZ7BaRKHRqPnfUc4Jd5h4ZDkegVIQh/cKNWNRowM7TjfmJm/GVUsZBBmZGyVFoDklDnRwYrM2TSI8lYaR44tmv0cn1Q/hRopx9dA2CCoRkeoDIO4u1D0p27d0mtU4o4GgP98NFxCSw0pcMLmSNl0H+gCEiYJ+7xw6Uycr4bwrnaE4ObogdvkZxs2BaURlSyonimQ2umiAE4YsyEkMngozENEecuSgoBcqS1CaJVSbo2cCCUvG4Zr8zGGAeOWiVHNyE28HbvJe/w7H26Ycj4FR+pfCZvxD1ukbhBZOZuaXGmjNvp9lKLOYOVojghuXVPIumhG9iS30GavXgPxNFcjhXpU7F2Re6PpoWnI+wNSfLUyTihAWj2aZzibdsuLczFr/U0x1dK08ncQrdNb+8/lpQ0SELnFk1i/DHL4NE4j93G5KrcWsmxaYbk6kV/LokH0Ts77YZw7csejk9opcncmB0A/MfmBGMu1WLZpsLrZdu4QVlRRgdKhOWDEEVCn0cItkpZCJJvXoitc00APY5Rhwuq/ML60p8PGJzpheFLn1To08izaPuWecmrQr2itAjtPJ4VSQYfGIfrdGYVHXW6tH/m+JbbjbQ/I3jhbfBEwOgNevvJmVQjUIPNPrjszG8pSN/oEA5RtonXmvaZkvl3zUTQV7bivtD+NyYRMVKE/JA30ZKbR22gV2uIskq0tbphp3CakFakfdGEEVb66IuTF+qBwT1+kCLrRosg/Mpx1zZle6R2KUgU1E1qiTiOIC8ZiWFixFB9/X7hSsMQmQdn7uYxZaCGJK1eEkQ0iQDcQgKlICfDWLY/tklm/4iVmpDpdh7M9ZVTwlkwcH9HWAXflYpoG2KH25e/F+LlYujMD+/6KY3slQ/FFqrN88L3O9BBDUclsW5huT4EEPdd1MM87LY/UXSrzy0NolhnI7ErS0e7J5o/HPd7DY+L2yp4Ceht1AtwwmcMB+uY8rtw0W4hpBgYYvN6MbrkOc8bwIEqPUNP4/3Faa7L5yVvBygMfQAVdgO0fsFnAYvR4WwQv5snwGH9xluzBInrINmG2AMTO2lIKJICqCNaLIZtk1+u06jEtsaNZuCdo9rMO9cB7qUEsIkGIyo63YvU5qW499y+Iul/R0bU6rWPD6TIGgVveP9PdMJ3l63cuIjuYNRGQKf/Mbv3tYoLg2PIh3nk3C+WnK9oxr70y1qJzdkHhrtuXimOrtVpDZ7LUXrRW70D/+C7MYW71u3M8z02Q1J/sLPHX+CZ/iO3mvJE2pYtog8WaFR7r+tumiZGQFAM+gMX/5LNUQxu7aJL6EvVrgDTj/HXLzFWIrfMdXiCT2u+ty1l10VsNsn887gmikXtM+Cn+iCGwOibEl4CFE9Z0I0mqx/9nxujy1T8nyuSLc4+LMJCDKI3X7FJcUU81ITT2uqalNu34E2snjCYukBgscW9bjHqrUvVX2ijlv9uzgk2VEoSdBm1pytP76Nqdx5pbX/baAdm5bUF4Ch2GXZRrH4owEiXSOU4lJzyVTZZtKlt3htIKwauw0GV+2auQm/hQ6YPdWEA0sf8FtH3ugxnnJiEOHvTcXOSAFM66S7/k1Co0KRQdoAtLC5vp810/Zmwvb5Dhhktiee+7GiOvGNfFiO/rWji87XPh/GJ1w5byPy4ab+1FKc0N15EFqg7wAIl36rtu2vtnpvWFJuuKCErkWL4/leBCIpCTV2N+Fqlm4yXzfxr/MxgRjtP+xo35MC5FMg1RwBsdHVAVrGCKjIwQHWsO96+0ewZ3OkTZH+g9pKbUHW/qYgEiHhFyWwjYII8W+QwrLypTunQRZ9cj3ILwiSqbk7OmS1GYL/8aLnmRcp+DC49l8k9sZowscQsZuQkbwECj1rKip/8Hcs+sDXivjHizxGoYDyKL3DpP/j//XvVQz/dnmAp5IYqs478jiceJxQAcnPkBjYpMXWnEXy8/33a8gQhoetsu+pX735j5uRGKgo9SBJy/1Ji2sCZofQHuz+0N1n2FOX7ci6KfAgUNUYIE+qwH4A7RsMXNK0Ujxeaoi9FS3rAt9m0qnPJmSSunAfsC2WOjPygjIDJSq2UKeamR0mw8V+JQtgvodoRmPMnaDbjGU8Bp4t25YqsxHiB5fAN8dEUazPIHuFdIlN5++8izYCh2g/LuIhanot5kTh38A1FhpQEnp1iXCSgHprk7Q1AgTVAHd+QfMWGAo9Hjq4nWi5fNfSa96iumbSQcnL3/oL9S/PriRWlcAprBt4PjsDci50yESHAErLv8umQovfJWxS6vfRkuSrLIwJOFIDAlFvVM7fLzsMVHLm1ryrMOkdWtP6ttQFYFUWN6ipRs36T6SuTZu3VsZ3RzQv7RD7Mxb0kDp+pOrgKJ7+HO1H6DPAmUPpIkUmCkpxm5xTzw0Tvv/o6+Shvfo/iNvVhVNJdPw6GCUG7oVk//1ZbNt3ey5nnjSO9t1o9LjenFPNGecARODVIBnv+PoCr2jwzTso3PQt9qhaBwGpEb1wO5GuyrRjS1Iq2csTtarnjtBI4lzlliHGj2fsNw/g7g06W8qAPSP2fWC7jmM3+EA0XjhyN/QYJVIoqz50rWSB0KieAdTjlc0Bb9hnYzFAEWe9A6P3F/ZBW/z3S6ZadcY/lKn+wan1rKhdRTB8XBDHjyQQ1PesJZ9/PQiuz/rI49Jx5RDUazOoD5ESBmj9Kdtw+4ravUwo+12Nw15rGFmAbvCPP2megPx1LbFA183XVFaKAwwMcvKWnVOMBouo6nl4JOXHAKOGspwNczywhvEs3/9COVj8v5IAUZZ+JCx+PVbtA225PKHiK5OTjdqyXi5FPVLdB41+CxAsAovYeCriXMBOSAlGeulSZ3s6G1/UAqqZFtKXI6yuSpm9sP7tgSZhKXN0L/ZZYIkWMzBA+kpyCWeK+nmeqwYto0d5zmFe7+LDqYa+m7w1o3YH70suaH1l3UDLBQSN1TJk/C0TTUsNkjO5qAIBroYFutGnKz0VkMZbX1TIpAHsfNKmzuzRzzNmUDc3gXyz1MYv10FJwE63As/Dz6/fbUg4yoHGRp5W06M0ncvD1yUkZgI6p2ljDlKO0ua1glIxzML6bg7jIbQcqLjtoVv4rGAb/fq6qpcYKl9CejRQxIYL09xn7vgJ/ltGDKpsU9ZrUX690ZCZ8doL6QUQsI5NjxwYvnCaI4S89sojc0i1+bOU8l/fXyy8J7pHdNOSkIunkkIxhyfG4vja3JCigZ2i2LYoVuxN80FOh5N0oreh+kppJuh5kIk3pN5B1uSoqEvECWH7frZbbdUe2Vv3Rq+Mi67HjtV4YrQQ9TVI7jCml4/BwlJWX3idFekvGZE6nUnhBTsn9TFfz8HUZvh33IujqYbiG/Asr1C4vQZUjlTLFuDnjioHdQIGLo0UWFkJe6Wr/+wFTE8yOgZIpYmP21Kd2GoAqyr3pqO1/jrkKTaQwHxLsT4sfYlEhj20RsHvAjP9ilRZ1Pl8TBR+ghK4M4OTBn4SOXhT8flPi7gaYBz7hc08SBhfCYnjRQ7hfomgi4w+bcxp5zAZv0r3Zdj8x/jO/xlRkwUhZlZqitaAN0UhcW+n5uCfnsv4Xhza5ccZD4w7E47q7HWdvJjmXqsAwP9/iNLBYx49qwgyf8kCoQTVoZlP8V/H6E0HSv1gIqIF/J0iXLM9bvtFvMEcmZak0FSDZkIqTKYENWEVRIb+QrWejvR9tshQemerPPXGzf/XO9WuiHOuZOI87oWMDnT0hfaUEH9N62CB79WHC4/LhlPckxXu1LXwLWD1vcr5Xl8d3t4Tai7xjUPfCQwNbALdZoctUNnWC6MlPKyPxa4ShYs+L+ZoBQIDVBlfzwRo09QiyAGVEqoKqtN20MzmXIPTZeFd5LVsqqn8buJGyi3I/CM2LTjSr9WuesLKdWu47e7tgU2UdlFPFf7DiU7NMcaT2dIOoi8wCpfghDy77uF9wkaKmBO8MIVsk49fV8JYALpS7Zm1sVd14BtEz46zCS/8E5TltTY/MpjsnELtov4SzCVZLmb11U8s4SZLRWzRnmRPO0uGUP58Q9ki9MHGkN+oyEq9ymABLxgHDzrRV7LzpVWUP4j+UAdLq/7mc4bVoy/2dtohihdJpOX+OaZyIrvy98YoqwgvrftVGfqGhVnZfp5m8gWv9fIpITGy7iMpCZZ2NUUbk51O3uo+jcpHCz4iZ5V+XhQZQuQWsitxX+wztMrXjZ6K4/qIokHGTC6S53ezQfhBKLXwM3d6zag6E7EJdW5AyhsvRJut6oidJEclUlP3tEMyXC8bZXh7zgqw8AtFdyir6hGgTF/InORrqAxG5r+Ng2HJwgwWlYJFNkNlnTNi/6wz5Pp/UcUCQPV36nWdBIGjk+wqwOFzHIdpkzOcktkHKhVVlA+9Lz4RaKUKIkBJMBjCz2atWcprhZ+JUBZXY/4A5NKsf1gTrdiqdQFCLQAi9wEqagD/0oV9HOZwAzaMK2FgjrPJWr4ieCAfKr8bHv8usX5RVnWMRwjZNbkAaRXxIe8rY0rs92q5XuV+JrdGrAiE2raFR7vrkfhNi61QMEScTJxnnpFO8I4MxgyZ5ISY6/C1gpqrn4gbKXiMJE/m0RywNk15kJ04FOOm+CtPY4dsEWjYXuuD1baNTDAcV0XQrk+yt9F7H+0AODS39vi9mj4NaYjG9ZxG1P0xvIwmkAaD4v7DimtltWKjDnbZiKTriHxb6aTQ0vqvgARf4qasG3kJAOgenKWiXQAqZ+1ckoDXXLiCK995w42HvsDWJ2WLe5BsPPmTIzNjyN3Goxux4zY17cvLwTF/mUWyVP67iaE7taAZdHerUJhk1ZBPrU1eY1YygftL7LMdfS2hez7LSxKRxqICo/Fwg5Ixgoxw2r7XVQx6avlk4ss4gqsujJvIv6QcnfMV+Ap5IwgN4MRveGi+aE1kc5CMuc3FJRw8Pxk0RWCmEfGPjYjTcJTrR3U43UKA27269MCEvxOsbOqzdUsUgD7EdZfq1/Jh/rduwidSLjv7ofcHDBVD7M13Y1G+iu1sDX5dygx5YBIYijqR+ApuVLp3xHuyDUJeg9NscQP6nCW37VhnuADq4BtSlpn8pTNTNXn98XDrnsvvQCfynOh9/XcSHaVe/IwCGStAcjk19H5RNtamETvm7DZjQGflbvaLmHgTY8SLIjopugzztIN9eHjWJuVd6xlpdqOz4/uDS/dJygIVeW4SgwXtExXXEAzUw76KJvdGFSTXhJQt/tq2izz7qM03tNlV6Osma7XnVTvRXLePVoHQ7JTgBAS5y8Bn3PKuhKKGx8h2tvgeKzZ7dFxHlWD9tOaYyUtR9NUcTEgwi+0MM2rFe5iccQ5bQmZZS0S77lIq0m2zaQFEVfuE/93Jg/mU/x4cZmzm4W8ZCuDYbZzqffTrKNNHZgIf8XUwr8wZI/jSS5Vfo/849k4CTOKgiao8JgwEuYOYgUAkXR9j8p0jGyPjpeCR4gBjR6T2XSKjRj+P45W/7S3l2/O4wAZ3tlAXlHw3pKTXFsmhEMSKqWBwYoLFlgJOQ8LUkSQ6ls500+2c0t/GpJbDFbAzvcztDKrfD2YlaWXWWKBds/qB0Y2rLH3xXfNxVoDxV6fCknEilLEbbjyqGcYRo8TpUBVgg15MdLmCHklwSYrSu8bPv9O5y4OqBfnke+boXm0BEb7rWoT8ZMNLLleJNM1Ob3pI+xOR56xSEy8VxyQb2aE+QL43amvrWva4TgaQgQz/DOFrwrdGrjex/kH63nS6trZGviY5S47X8SJNxKMuZb1lTOshwvRuu4QzmAbhWkUlovgFkDkWOX8If3KCWjlw4b9rrVNNDpzhphHA4pZk2sQ2QcDLVSIvtuc8i0yPWmFzNCs20Qw7QOd2B3MO1RjxlxwP8E5eecTX2GAWmT16OhYiofV0Kf2S9WQT1sp1DmzFJPqchAPsrygxo+8edufp0nVTNl+Pvm0Z9a2HRyRqIfT6M5BJrN4lfFuqJ6jsSXB38jw4R4wRKYRTLXfWmUWtoXbE186vJfI1xXD85cF9Z/XuGt5/VEUmdSKv3RqwIWhtd7p/C5MisNfEredpERr4Oich6Tu3+ZmXtQQfhCvykUdZhPB32tis/JOhAjANEeXf9zve3GOioC6DVR91StRDcsPFjk/joSdlfapg2Jf1DS74xJS5iULeeLZqtR6T4Q7KBZQXck4w6GMoRB7rBUk7jVUGAoW7JxdcH0pKrrqj7bIARzTC1VQCcxA7+crFfXeFLlxNS5EJCcxaGkf0VI0Y4i+mvo/JI+TSY4KPBFrjoltERd1ewLDVwdOMIVJ8G+jFNqfDNbWoQM2yv80sROXpuGLx9YstyjW42ndvTBkLY3NtsMQuFQUfLM7Ze2KE9tLdlsSFlpI6Gy3UGxkoUNisM+FVE/BqhisbjagxikUiLBwpZH61JJxf4rLV+t+aQS0T68jaS8zykhnMaJ0m1AxOcucwVIu/3xSwT3Ra004uAkguQMrxhJ5/0Arv89n4RCxyVvAeC5Mf5sockXWmsc6InQhEOANQ6hydgmJXcT9HmV/bTiMmKcBGR8Q2UPQO5VXbcx7bBDOdv0H5662na+lmQOJ+3HgOqdDnXTE7amwqC0M8tyMpxdksFInypCOfq+BaIQitZ8dLFmuO9XvH66G51ItTvkK+V6K8OBnJK6FzdXZZ2i2FVmCj5O3evTwkK1q5amHxURM4Ox4hl0bsKG2uxnhzqNBvbapkvd+DcE7wsxBb1OtgzNut2AdUovCzSee1lO+u5UAiTFieIJhPz2CPGuFEx6JI/fE2eJG7Fer7Z348txtGBEt+Mc7sJpB/NQY+Hjq6dujNLYmvPVCvcLD2JOisGzUITd0qwJ9uNhY5puDPNXqlIiByzfIyxhRxdzDR9KQH4M5ZwUaO/QEqqMZ+7afIsT/wjDbjgSpfaBVeFSY0KEbjbjoCbPfPnVExmeizgW0xjMEIE3zAWTc5RFfdMez3/6hB9KWVTA5XDdXECvyk1UARJCayGfjHQzDZ2uUNSkgOxXM1HKPpzEGRL+Yoe1sOLHSwzGVENafyaXb5ygCSva9ZebYfpidKMvA57DcU6odkJREqlzdsKmoDvKOe/YuSTPdugmOFM8wgIGhfzKfAEs9uUaHc+Tj41KQTF+kpntZ4YviVva0H8hg1i84uQGvuss/4p9IuMTiDrCM4jfnMoQKZ6Ig6u1Ka2kbkV24NeQcD4tq8E8UH1yP8H3JugkoQK8avlIegg3ofUpTJGJxO0M38kurjPJremyJWPJV9OeKl7djzCiHiPoSA54nUaRk0fgacP7p+pxn3rUT72UNP0QPetdesSt0/hu5LS62bAe+lrnC3Fij5fQENqsAqEkUhkTUBWOfZj9iujxJotg15CznFetXwx8OuPD1GswJ4oT3tJPmKOHb1rteUWE3Aysccb0Qtne9Xsi9DKJPg1MOxADK4DCVxubF7koBe8qeEbqDZ+BapXaJf+efIO+8YeAA+Y+DJujhLqdCV+n77a1EGHxEgmuNMImaoJQcuaqAKk2Ko5vwafggrWdnkzph0D7QEpcxmuuuzvrhrmgtC3chb5tHA922Nt8y7QF4ZV8fv4BzvDbczZEStTvQcBMwtIQAoG48maE6zsUGNQAcbs2Y8plnxBHrC20a8ioiab+p0LFxTwc4ZzqHz63yg5lA+MWvRmUdityUbZ9uKRPAxovbAg9IbKtvr55eNXb1hV1lZx7IHU9xJtV/nYcLKBbAN8sfHenv/FAYfNJDndD0qkXM+Wpblvp2wZPdg2Zmtw6fP/L9byuNxfi4DeVaoJAGe8TOUMQXYv+Xc3uSt3jzlplxaSvWTnOMMc+L72KxCiySmU1MWZAessbxN44L2O4qKPGCPruiVTfg0Rq5OFsylthWwpcW6CT4dCa32KIB7bP5QcroPD/knLI7vt1NbqWt3hBEAf7Yds+F4xxrbzStLla2V77yb8/qx5zISdXFBMzpDs5/gMAKfwT0v/2Y22y/DLN8f0xzac6Q8zumURtUUfKOKc+y25HJlHl7w+W6m2DqDNHqisgnGWdWC1dLOGwc5Qki8kxkVzg3QKaWKlb+IKXIkquzZ8ZoT4kzETKhdqfKvqOcxMCqReI6MTzwWO16HF9rHDMKBET3VC30o0iY+UOC3T6xevUbGtLyXTL9fbZYS/SktpbS6vuBFpVn0shDwT2oQggl7jNHcguz5KejZyYcl0VO+xVfWlT0RmgD3aCJS3LjjcnMGRVQMUWBqntVpis2DQwa4nLRMmputQYrESKCek160Q7fa57Xf1THWx75Xh7Pq0cUjxXQqoBAKoNCLpuHJEJqv8YBFm8x2tWwM3EFvbpGEtuZpKfd19jTtkLW5UjZgwFLrvwRpOrCCWC/FmseTy2F/meijjkq51rUSYpJJ/1y4TbY8IUhI9gp5IfXuundG95AzohindSAVtADrn86QgxfPFl8zmxwTzk+8VyQWT6UnRSxQJek5ts/HOOb/2Azt7HgCK+8M98f5tpQPpvAuXQwsMh5N/q1jc7mJuvqMqzUk4M6SZ129uRCBamp9s4A+OIWHrEwXlOnirJ8VU9MU8pvcIZ7p3+Y+MAwkfIikyxqZeUKw903+zBYW65QMQEYNYFhpssdY9M5SKO9+FiqXAi4gP1u5YLIBRyrOp8autlLQ+HxVt/0OZjoX6gSx2u0ylliVmygRQOjWSCOsaDWPDl/2UhVuJYDYCTUaGWeZOjSTOy+JljvKc1DmeK5WNK6aK+UReF7GNj3THIjKctXOtxh9WJOzP1lQF8CdV3QggVSFeDgQzr93rMclXsZQzqTBeAauSzBfXpJQJDQ30uPZEv/cBtea7oYkBwhHmNk788Krew15+XbeAJlLVkjqMRqVrEth4AgtKTulOv0FuUNxRuEQDy0FbSYsmdYNvF/Tiy3IgkvC4xyU4KEalHKSVPlFt4UHthXGiWpbOA9yJvaxmEFNcGLwhdhzO8Y67cZcE7EX1eZsjiWlfXwswKGqhm9l8KdpCWYWWw/2CZOgJ9e6j1Pocfuu81ILUecTl7tlBnBlFAjfFpAmHYM3Ie5gtPp1BZ99X+R2DdeA8sJF1Xs6m3Q/OUCPTgaY+74GGJEcz4zabYsFVjY9S98lQiA3gMMRT3CKArP8bmWjWXW7bwkBwldSeMr8xOV7VYDfeXcPKNv5lNUg/St9vS8akyclje3nWCmRBLhJB9sgXANnVq6rBLZaADcQnPlj4Mpw/nPA8Xd55eFC8v0NBMz0DXFJZ6s4VEuDXLoGH07tmfLULtRtwtrKax/47bdTn+xyqrBqHSKFHJnThNGDA3d2pVYRXc4ucr1APO8ZN8xge9221Lvi9BjjVxDkc/2n+H4ZLIWeqEtkoaaSZ76Faoax4lx+h/LVzCPrZFHiiwpESNjHxWwR/GyFoDoGujrABk127pTTuX+leYX+Yp6rq0aZR+0KPj3/CoCstwDSp8OcRhWLNNS8c2dhxI9tC5sB4M/LjxOodYGZ8hbWgNd4PykGvr5KG4KKLoWUml4dmFuNf39US3jMPmlGLy9Vcb7VwEdxAg5zYAKZ0wHZE0C/vMcLT+As8IWsP+UFVgpjtQmBpgu7oFxI+DTzRjKpBeJm3/3apMMRQF1VsKB1JNW0jmaC2p3Sz37auJYnm6xjiulDp4M093JaKoYHntaJ/cOlDS6APTmT9M23OjmmyOMUeKKxc+LpGwKdlbZ+zN2eBo+LazzsAnhelz5M1COsZgWKBQfrcJDUJZlGGWUZ5LzQEXd2vUwNNImtrCiy3eXkUHo05RNs85UZxtF7LwRrHrK/JQXaw3WdRryS35sdaUCRSgXhsGUt8PcQBSR+NrasEMu77+Zsg5MrKvZ71lHFiv5FFjyClN7jJkeRoBJAyeajUvo3RAPfnFpJoZtj0TUS9Pvt3lA3qKwkRP4Uikui6oOdXqh9nGpumiSpFwRG5xq9uparKgiywTAF7CCbTdi4KCd/qkAinezfHrZS+bdr9avMFSwRfjTf+m/ujgYUh2XASUznhmLXtp7O7drDB67wCnqeYX9VIpyH0Xhu8CdwbCd8MjEdo/H8sndF74TpkhY2rJVnOZFLp1xwi0JSMOEJ5zgta/x4OxsWD4jRhuTediC40PM4MDHkuHg6PoAROwI8w0DQapjNpkgWLt0X+p+f89hC7YmHTkRHEv5QSU5ASXphAB63B2JbrheksQGS2eFQg8Ccxh3b/f1Ca1Zsi3Ejx1wwEJ4M3pcanFIcKQYvOj+yme7Vt3G4sVxILwPr0WawpFlKhgXWdhTz97gQpAD8zj2BV3sfK3NB0ScB5qNoY6Ct7UiqFeUVg9s8J/VwV4QWWZ3uQ9aGTiqOzdB4ZivQhuwcdgfV6LKmKlRgjUDWJ6bRglaYZgx0f/WbY1OlDf4oJfCNbRC6h+LztwFxbxAz2Os0Oz/dFm7c7pkRAmlrCHAXhrTZWCFrgY0AiJ0KhZlkDY2MqE/P+0q+dKG7zGlKddx40UHM5pyPBKWWboun96sNCEXxmDd6VwMrWja034exr/pl+iaLEmgKGXUU998VOnR/foJJYAVllABwY9jQeruhfhFB7fcEB5yoXKB+qWZktU60xKToo8A9vHhCuyOOoyym6dVPFTXpc8BpWu3fDAjE9+LksKEah3O8ktMKyRA5PgR6V0UCiP2vS5ThMLhihyR+zHUCG8UAvCmdhF9rYeDv3Docg7rLBH2qXmg+pyKsA/GSuvhjuHKbkNr7VyDpuVeVrL6dCajklJi0yROE48urtXcQ5MxL1SeUAOWXLJoUrF3itSA1XXDFsRE4Ycse0p2RDaqnNBApu6O3SvchFx3QiCvFrVgR/mO05F0KSAfxJZQvonzkhqS8W3oB0ZbcCyUew5bmPkB1zz86I94O2JFP1qwv/oDkBoyUK+YTF5L896avSA5x/h/8SotLhlpUnYPHCf7qPvbZtVpopfMiY/TAkIP8itoCmcNFiEUkazWhRgrtS3w6Y8fQUBXkNhzkeTwrbPsi93Br1rN6WEmzEakvb6+nZ013GKt6gLOSPITk8/z+sWMwL1JjFYbeU5dTBlikfQdHUlWSmKi8S42SPmkPf5tQUb5pqjvbUAaLFrsYqzsKRCMz1GTugfs7p2oxTHlJA1S+Z+KB1F2zBMHpPFkSE4v9Boo+J6A1UcZBG7vJZUNV8TQfyFgkU0ieukd60Fa3xwFf87dPVcXX3TY1oeerZ0I1eP9BsPQlbfcBOXGllc8DS94VVyjqBZNji4VLrLX8B13f9ZDIjeyUNuU59BKGcJsR8T6o14nEHrLSy/RpH6RLeuid75GGQxa1r3SeadQpxTzSxrI8SLRxCa8PQtJpxORfNPBodBEyyg1LjXqYqxuCZi0LhBO3b19hrZ3c8KBv8NVdNhWHGg8rHZi5IN4mH9VqRcfbrPjoxqQgzsdhA3wi/xtQnWRHQWVJRdLtEKCyFJfs0Mxwsc/CfHf/1SPkeUfQFNtOi8YrGfNcMOr3Y8lHmVW/asAjl1KQsQh02hGuN7VeK70+RXJTPUGEhUuZ6hd+G1jGSxFhuGR4FJFJher8zU3ruomosyUuqjIeRXQaWf4W6tHiaMXj4HDyLAx54Ul58frRDuUJZ0K5P7cn6uhmI5BWlyV2RgkB7CvQbgvlnHk3YhjP5UGs7GKbmsGkGrDxHKlfxdgIJH6b6oQUvp1iZuXyinrHgqzNlMMEbh30sxQbtyb7Csqc4nHuvznfYeWg2Z7jzagFJOLA6cbDSqgnizNh3ByydH4vFGEWub2PhA/4Zj7zzH3XuAl2XWwHW3e6dh9l3gJQjDF0cwPlQutIG7OtDe26I6gacjuGiAYg+MlCakt3Wh+ORNJHfOF4ZkilIS3rg8UjperwhSvg6hMDfKkT4+p4xZoq1b9C4+7k812ELvNb0+YHF4aJDJcHUzClQbHl3zH3GFSYEVhXyjbtzLc5pCiMF0eEbFauwSFbbzvGR0pXueZwpE4xLLg/DIkaGZA0CTVhJfvRFBC3ATCc6ROoX1Svr1sUDhnvCrI3sSnfqH+v/3njq0WBFcTmDG2ep6zQUixb+lfLm1ev8TJJHlyQT6D34MvgQAftwgVkRXpX8cjXKZWPOwc4X2NNltJbrDqKzvMGRE1OeEyLyIBoM1wWlDy3QtAvRLPW+7Apw4rsIKWmHhKDD8gHZNE8AOOuJ/LYi+nUxgg8IDs1ca8eWrDrTnWjkb//tCASL27to9knoxh0i1RAUbjiyNXSWKNHncGvXNKOwxrt5I76FX4gqZw550A6NwAqncsIyV91Jr8eKErde2kmeP1mkKC9wRtK3vtSxyOjkFvVliR4+OuQ+mrc2wWZNOzgdOVHsL8ChmDjtSRIsYm94sIbPX6+4Hl+Vgow4/5vw/spik23mTaDegT/zPAFSfTliEyevSkYqz17oKBAqtwCtx+1oT+SeOwR3O5m29nnrxo9oeiQ7zLG44Z23lggJGVtTN2aEGWCNrctjQE7u1WCoVg26zEv8T9IsEoIqhiksWAeZVAjMOSkJrHSPVgalTOnYMTgDzd0JS4y0Ky6G+VfgwB1M9ZxO2Pd7g6WrWb215ZVfGiX6qmZRn1AmRJZPX+xv7PwTuJFyBxOjH2xZxJ8/AMqvf07k5c9O2nDez4ueV5zJefLZe3tZ/bBHH0Sd8TfDMCe4EeRDcUjQAPhvp2L2QqXnf4ajmh8uvgXG6oBjnOALo3h0uOSRdh2MlCVesWOcZY9fE8bg5acJuBXTbZl7qrNR2J8j/f+0upnt9gGFM3TdxmDKHf53Sea66c+ygqKH2PVVLc8cDPQAWEd0vo1jN7YaZg0rrCs+NoPfwInkMeJRVqzXQ9pEz6skfn3cIgMeBZPQVxyaJPxivjKac/sfh1HnTx4QuoJudMFc3P9GVFvcb/shAQzJVCQO7OKLtOCPEXxzufkbXHlHOgnin0clcpluCLbhi8AyjHXvCbstkGpQgoP8qRcR2Ktu1Vo6X4j3+i2wVO5Vj5wycKSeKCdx9d4sM1lc/BWLh1NoVlfpfmGt8A0E8GQzt4N9Zf9Pu7zeVrNHUaiqam7dcJYIsExI1iTGGj9TTZR3Z7+6LQgwL4M3lj91YhmslRuiaTAOsPbGOp9dP4b2aCV7IFUh7q1HfTUIeynBEwIomrM26p/x6XNbntnte4RPgkQOuhUkPoDtTBi7aYVYOZdLnFIRXL6UTgEPS65swlRFaSdup5bU2DRSToaEx4JuJ8e1hiig+O8Z/AP+iT756oMhvasCq39dpjLCbQb4f8ZVojZ4Dd1gBBnPf0uRP7559m8k6hGrNjtIKjEL0nWHHNLpdRKDueT7+zePj2KHKIa0ELC3oHFXHQnm51B7aHCaRC/hEqZKJ1AhNI4CnGJnlPp/AhgOh7pW4Y1Aj0ugZgs/5ly5c14Q0XuXa1Hihc7HGeGf4cj3KE/OxRZjLr92vuoG+s2bYngR21jccLD0Ep8RFuPKDlLNg/WmBkZKnKtQgp/Hil+NwxLgZH4hwY3NyeaVvJyotCTx0OkTO/ETw1W+fgcsE4A68pu3+i1K3JGcBuLT32SVpC0O9wIkkGsxtUR1NNmpabSAKMH3ZhNxQWDlT+HMtKuFdvjOWW2c9lF+bkZRAbeFHABIkQA7qnobMj8wMLiYdwyDh9ylCobbCLLUVMRk+ooOH8pJmYKNGVKovTekF78yu+rM+AyrM27CgTQhw6ZlCziTrs6K2JtWkOQ9MHU7qSXByjnA7IeCIslUzRDTcgeNqf4+8EW0RAa5PK5M7JPRNtqp7Cuq6fFQTRKVdDHOa4542X8hTxGsev6z0UE8vsxXAwyztiQyb6pLgLcZTjMB7hhaCwIJbJlE7mnkLwcib05U0XkvAy41+kWTcrPcXxTGr9gsB4V2NM6F58Qab0TkYWlgKszV6frU40OEZy5HW5xHeiP7S60u0pdk36GXQ1PzKEewaBEwGsYiw2ob4tjthU4i56hpoPPJmVAkHo0Xo9E82NgwX2ZfHsMKxltZDpSCINUaw9tlt1tsZxAXkvDS6jBfsMLaTW4D7vS8OnBN+DZpZ3027nckoUfWaxdhGSDt4AMQC/w4M1uIR/p2O6mxBlQfzyMMi2z4XhfvdbMVTIlfmrSBa6lGVfwKIccfbjQy6oWJBeInk/l41ZjtO7fg7Ie/p7MZhTLAbGfFPeBzo7QmFhkA555Iiz2+hgBlnnZh5gkymJZROsZb4OswoYNh8h7FK1MTC5TsB8JBqBNq8WPTOTsW06hc9VPauMdDmAVKkIXcmr7LqspsIJNrlRWbP0mXOi4TN+k2TE/SIfIsEakuuV7f3PVaHot6koc0Hm4ZDWk30UH3zCZYKrrFhSMl487EPRpHG6vBVbeiqgy3G9JIY9NNLwTfZ9WI7Vd/+Z3M2qZ6ntXvj4SzZNqhqMGgAnpqVz98Rqy4x/HfXBfLnsqrDIfc8piSnRy64tAegK6UQJxfub6UXdl2DvsJ2WH8UamwfMwHRcNGWF+m1fEz9x+q6rEHCdhduLz0rEcnqw5f57z6gA250A4cQ6eWhMhqPaxD9M54yZiG6oJqSYy+aj/URvvR50xMgDKVz9bEQtb5lzqqHwjb/O9ehqdyYL3Q8k28XzAITTFZXeCtKt2UCZKhMSDyXJezH2EQciG/wCrP6H/ZpiAey7Bb8I+qFcFS9MJWfcxe314VN2ZC6+P8mIj5yhlZ8IBorQT20INVoyhtw+LXCCCxeC3KrqUzWn8UcPolwgD6q+E30cr7GTFYCiI0Hd5LAI17i28XqmppE8afFhW1RTWY84874q0B6EKJa16ATEBLSxxh0TjwUcARrCrqONJXjBw+fK8OcoD9dZrbjv2E8WNISR/u+kIXBZ8bJ9gwAMHNTHqAG47mz8qXBiZoLgWuhxFStc+IsijhgoQlw2O5WlfgVUcBQmG46O/7j5AysU2cxSKRa+dA35rG5QIOZYeeF7aOlhqfrcFQ3kYdVy9Xk4uhdsf2uUOHVJ9yP+YeaFj6jzMRe+TiIyxym4faSIqQf0QnAaILm0g+XWgHcchUKUW4zAov4SAu45PY+FDO6RqtVUlwnb0hUWvYn8xrUo9ZXjQ0ykoF7H/dkWNPCiPp+0rNXIKW/jOTziFvYbJ53Ez9z23Ie3PRMNGJvG88k+dwoUbcqT0iWtU618djyzTlXxVy9c8rUabn6uMQXaIFPRQwmw11ncRlKNKpeIZeloKaj5+oOrB1RPfFszy9FUQ53KIdNRytHIaoTeIFsD9KVuxuYfwH+PjCLTXJo5GuqvjYpvijTF85ryr8mvTXF0o93Unp6T8rbQgUtEzmmv5c6UZIBKBluBloWrNSO+bal18NcGtynMgtsIZ2cvGleCGhOtYqoygCD7HURuajW3H2ImuLGjbmjIEimqBBJ+Xm9996TRsqFQTix4HrB1DKnewDjTbb5PgDWHkPSod+DTt1bm/hvoxCibGIRwVFpozyJXSLN7l1sqarT824+OlvdABbEq97Tx6mbu10GDWS6SXhRFE/8reJ3Hr59U44HoCqLTpOa3Ax8KzTzldUCGWeToRxbQzIMxByV3a7ZGfavShdXSeGSYWBnZxwxYU03w2JTibj2tlgwdaKPwPUHCRNpV8Dar5ao1T2D5O7lgMfA15adnYLlTqPWHIY4bDL+XYl+f5pFTKGXCaUrq0HBhHGGSyT8VRS0TZ+RElQf03+BbC1d/hjAdRfuv7J/T6h1HqxleVnlDJjMSS8SfnM82KeuzJCgSTDQUXNtiqgRRwc5a3GNF6pUvbcgri0zEsABv8YA5Wmrees9jmKxdhgXdemaTrm7KU/5jwF7V0eo5EYuFrQCtf3qBH0zHcJVG6FUoMz/81wZ9wHWrtMol1WBiNBdoSZC8L1Fu0kMsmzTI8nKdY/a5015O5MZw2aP0AJEjB8SA29a3n5JSixg53UF1XDviFeW94zaUvzuKrmGnk0qPqYxhegRI2/TU/oq/YDOgTXcSP0/o/AUhCq83cKPfI/jzb0ENa0+zMYozeOJ/S8EWspoQ0nK+yg+5/qqTcT1EVKocvHuqDl80Hx8CpB01ROGuXNCQr1NTh59de80d5v1ztopwfm1QrgB17liAhF/gP7IdVAaRtdoRiZDUezyjTtMqIqHJCSooQqcN+LLYmdb8KjSTQ+z7eYy7Da155CO/4iRssFZG9cmX/3zsINxTMmBcPWzd9yBMrXP23XATCFTnahuAcM5AgAFRFRibRLM+JOPnuh1i3SJatuefsJ/U7mmBq4kNMg5qm9FdrARROJtYjQIgXhLQojJVgjMoXSkX7+SNGR2LxYKPONfWw7pxmJcrZmdanu4YR6bxT/Only9ZgO+fey6NZVqQgkYhgj98kwDDgf/4QV/C2FkJFkxujK7+w1Tavujm71fOzAn73h0cDzQibGeCO7L6IoZDc6LL4iaNKc1XuhgBCe3Pgp2xBKW1szZt7DWsc69c1ddzvW56uucDbtzGP6jgz2EVFpUolElazfRbGm31sK9CqhwRiAbuNvLsLoUyzwv1k6POIs1Ui56O7jY1kZUcjrYBBKKoNp6PH0TOMp/b2cdkgAPsEKSn89xRA1C6d0LL2i5iyJBWWgHvV57+D7CBLG40lM6Z/P+dq92V+v4fdpiokcBVwXXHz+ehiwEvD6yzKbMZZqHWIs1xfosoeZwrvT1S63rCeckfm+lPQmo39cckKUgEyB/7P3dEaMGZ9QX5iNoe9JnEo7AZBnsBV9Omj8+8LkQLw1c0r3tYiGwbESA/PR6XgozbOc3MyZUTmyoVv14MIBu0wv0RUgtDN+N1IbtnMM0WJ19Wo65OknEegekha2fUOVhu9jWNx2/HCmO/ALpPc0b/sIBgNr3YuvqFu0hRlA/iilWgg0rLwV7nmxzRK8vVABmHWcvOTyBSg0DwXcOXdVtTYpCgJD7XyuTS8WrcbMFqp40pKx7qOjO0Low/kjAFTmBh9cMpbrAuOxA+e2bWgGumBzUU9EybcFeqeSBKTMvY+X8qkWxzONIRdAwGz2cdNHYW+N/p6iuPSbD71QLY4lSP/ZtkW9tWSi74KUxorQCqx0Wglej5ETdSzYg2kj5t/Uu+ne2oi3Qqzm+/fNW7pm/U1j2cehg6el5TTmgboy6UzA61VVw91ZAabmvA/UWTfc2JsxXaNuDMcbE2m9/gsuVUfvPsBQQlOnhxbfAy4IeZGTbCHS2KjxYyUnw+4egNCpeRDFwQ7zKiYzVAJkrt6R9Ok2xv8MJjNUtT3N0n2UmmGVLdzAfCJsM4NdEFIoiPOil5hwocjLzb9Dgnx1dZqvQeQl4y+rPpkM8eFkKj887aWlNpVALJMdvcPOdUJgs+wnRe4F3T3qttMZ5zKCIQcCM8LhyyYbCe4KkUghGjXrh0eY1m5/otkYSyvpMm0OEiSzqaB9aue1ufhAaOXjlTDaKukLoUsvkAp8mHhu8rggu8jWdMIlsloVXmBkwJOW0fn3DlTro1dfccgY6ovnHtj3kpHySe3skM0Qu2nOvNOJwbbhHOlsXxAMfKAdgUCttTwArzqldbol1dOQkcwB/E+jn8SuRJJbk371JP2oNqU2cwLP7EgW1vAxomo2OsNMbpQoAPPVJhD6+jf3E+h+EyYnrUrcrpxlLkGcZfvqMTLQeoSjnKgkwgui
        - #1:
          - type: tool-result
          - toolCallId: wjJnx5KWMXslMhyt
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 1vdDdb3QlqbxR5lV
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: wI20ukJOuarPd0bm
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.