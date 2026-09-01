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
  - systemModified: false
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
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Culture: 5
          - Naval: 80
          - Mobilization: 40
          - TileImprovement: 100
          - Science: 50
          - Recon: 85
          - Airlift: 100
          - MilitaryTraining: 70
          - Diplomacy: 10
          - Gold: 100
          - Antiair: 50
          - GreatPeople: 40
          - Production: 100
          - AirCarrier: 95
          - Air: 100
          - NavalGrowth: 20
          - Expansion: 5
          - Ranged: 65
          - Spaceship: 0
          - Offense: 80
          - NavalRecon: 60
          - Mobile: 0
          - Defense: 40
          - Religion: 10
          - Infrastructure: 100
          - NavalTileImprovement: 25
          - Nuke: 100
          - WaterConnection: 35
          - Happiness: 70
          - Wonder: 5
          - Growth: 20
          - UseNuke: 95
          - CityDefense: 60
          - Espionage: 50
      - rationale: GOLD CRISIS AND EXECUTION CORRECTION: Facing a severe -900 GPT deficit with 520 gold in reserve, we are on the verge of bankruptcy. To prevent unit disbandment, we drastically raise Gold flavor to 100 and lower Science to 50 to force idle city queues to run Wealth and prioritize gold buildings. We reduce Mobilization to 40 and Offense to 80 to pause excessive military unit spam. This frees up production for Builders (TileImprovement 100) to mine our 6 aluminum tiles and construct forward airports (Airlift 100, Infrastructure 100) for the final push on Cusco. Grand Strategy remains Conquest.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Liberty
        - Rationale: ECONOMIC AND WORKER EMERGENCY: Selecting Liberty as our next policy. Its adoption will immediately give us +2 Gold per city, providing +76 GPT across our 38 cities to help alleviate our cash-flow crisis, speed up tile improvement rate by +25%, and spawn a free Worker near our Capital to start mining our critical unimproved aluminum resources.
    - #2:
      - toolName: set-research
      - args:
        - Rationale: WEAPONS OF MASS DESTRUCTION: Setting Advanced Ballistics as our next research technology. This will unlock Nuclear Missiles and Guided Missiles, providing ultimate atomic siege capability to support our final assault on Cusco once Nuclear Fission completes in 6 turns.
        - Technology: Advanced Ballistics
  - tokens:
    - inputTokens: 22067
    - reasoningTokens: 5672
    - outputTokens: 479
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Game State**
            
            My analysis indicates Japan holds a dominant position. With the game at turn 383 and a significant score lead, their control over original capitals is nearly complete. This suggests a strong strategic advantage.
            
            **Assessing Critical Shortages**
            
            My current focus is on immediate operational deficiencies. Notably, a severe lack of aluminum acquisition is hindering military preparedness, while builder units remain exhaustively committed to infrastructure, leaving no capacity for essential resource development.
            
            **Prioritizing Builder Production**
            
            I've identified significant idle production capacity and a lack of builders. It appears the AI is hoarding production for high-value projects and not auto-assigning overflow to builder creation. My immediate priority is to adjust AI flavors to ensure builder production and aluminum mine improvements.
            
            **Planning Next Research**
            
            I've decided to queue Advanced Ballistics as my next research, anticipating its benefits for missile technologies. This strategic choice aligns with our current technological trajectory and future military needs.
            
            **Adjusting AI Flavors**
            
            I've determined that the AI's current behavior of hoarding production and neglecting builder creation is a critical issue, especially with aluminum shortages. I will adjust AI flavors to prioritize builder production and infrastructure improvements.
            
            **Addressing Gold Crisis**
            
            I'm re-evaluating AI priorities due to an imminent bankruptcy. Increasing the "Gold" flavor to 100 should compel cities to focus on wealth generation and potentially mitigate the severe gold deficit. I'm also exploring how other flavors interact with this critical adjustment.
            
            **Balancing Resource Priorities**
            
            I'm shifting focus from pure science towards immediate financial stability. My current thought process involves drastically increasing the "Gold" flavor while significantly reducing "Science" to encourage wealth generation. This is a critical adjustment to counter the immense unit maintenance costs and avoid bankruptcy, especially considering the current lack of policy options.
            
            **Adjusting Strategic Priorities**
            
            I'm re-calibrating AI behavior, focusing heavily on immediate economic survival. This means prioritizing "Gold" and "TileImprovement" flavors, and critically reducing "Offense" and "Mobilization" to curb unnecessary military spending. My goal is to ensure builder production and wealth generation to prevent bankruptcy.
            
            **Revising Flavor Settings**
            
            I'm fine-tuning the AI's priorities again. I've boosted "Gold" and "TileImprovement" significantly, while dialing back "Naval" and "Espionage" to focus on economic survival and resource development, aiming to prevent bankruptcy and enable essential infrastructure.
            
            **Selecting New Research**
            
            I've chosen to research "Advanced Ballistics" next. This decision is driven by the need to unlock advanced missile technologies for deterrence and offense, supporting our long-term strategic goals.
            
            **Adopting Beneficial Policies**
            
            I'm reviewing available policies to address our gold crisis. "Liberty" offers a direct +2 gold per city and a free worker, which is incredibly valuable. "Division of Labor" boosts production and gold from specific buildings. "Free Trade" enhances merchant earnings and international trade. "Rights of Man" also provides gold and production bonuses from villages. I need to assess which combination best mitigates our financial strain and worker shortage.
            
            **Adopting Beneficial Policies**
            
            I've decided to adopt the "Liberty" policy. It provides much-needed gold and speeds up tile improvements, directly addressing our current financial and infrastructure challenges, and will also grant a free worker.
            
            **Clarifying Relationship Parameters**
            
            I'm re-examining how relationships are managed, specifically concerning city-states. It seems my previous assumptions about using `set-relationship` for them were incorrect based on the tool's description. My current focus is on whether city-state relationships can even be modified directly or if they are managed differently within the game's mechanics, particularly given our current diplomatic standing with major civilizations.
            
            **Adjusting Strategic Priorities**
            
            I'm re-calibrating AI behavior, focusing heavily on immediate economic survival. This means prioritizing "Gold" and "TileImprovement" flavors, and critically reducing "Offense" and "Mobilization" to curb unnecessary military spending. My goal is to ensure builder production and wealth generation to prevent bankruptcy.
            
            **Selecting New Research**
            
            I've chosen to research "Advanced Ballistics" next. This decision is driven by the need to unlock advanced missile technologies for deterrence and offense, supporting our long-term strategic goals.
            
            **Adopting Beneficial Policies**
            
            I'm reviewing available policies to address our gold crisis. "Liberty" offers a direct +2 gold per city and a free worker, which is incredibly valuable. "Division of Labor" boosts production and gold from specific buildings. "Free Trade" enhances merchant earnings and international trade. "Rights of Man" also provides gold and production bonuses from villages. I need to assess which combination best mitigates our financial strain and worker shortage.
            
            **Adopting Beneficial Policies**
            
            I've decided to adopt the "Liberty" policy. It provides much-needed gold and speeds up tile improvements, directly addressing our current financial and infrastructure challenges, and will also grant a free worker.
            
            **Clarifying Relationship Parameters**
            
            I'm re-examining how relationships are managed, specifically concerning city-states. It seems my previous assumptions about using `set-relationship` for them were incorrect based on the tool's description. My current focus is on whether city-state relationships can even be modified directly or if they are managed differently within the game's mechanics, particularly given our current diplomatic standing with major civilizations.
            
            **Strategizing Inca Encounter**
            
            I am now analyzing the Inca's war weariness and our own, alongside our war score advantage. My immediate goal is to capture Cusco to secure the game-winning capitals. The critical obstacles are the lack of aluminum and airports. I'm considering flavor adjustments to prioritize wealth generation and infrastructure development, while moderating offensive and mobilization efforts to allow for builder production and crucial airport construction.
            
            **Prioritizing Financial Stability**
            
            I'm currently focused on preventing an imminent bankruptcy, as our GPT is significantly negative. I've adjusted AI flavors, drastically increasing "Gold" and prioritizing "TileImprovement" to spur wealth generation and builder production, while reducing "Science" and "Mobilization" to curb expenses. I'm also exploring trade deals and the "Liberty" policy for immediate financial relief.
            
            **Focusing on Economic Survival**
            
            I'm prioritizing immediate financial stability to avert bankruptcy. My current focus is on maximizing gold generation by setting the "Gold" flavor to 100, while simultaneously reducing "Science" and "Mobilization" to cut expenses. This shift aims to generate much-needed revenue and support builder production.
            
            **Focusing on Final Push**
            
            I'm prioritizing capturing Cusco, the last capital, by ensuring aluminum mines are active and airports are built. This involves strategically adjusting AI flavors for wealth and infrastructure, while moderating offensive efforts to enable builder production and crucial airport construction. My primary goal is securing victory through conquest.
            
            **Preparing for Final Conquest**
            
            I am now focused on securing the win by capturing Cusco. My immediate concern is ensuring aluminum and airports are ready for the push. I'm adjusting AI priorities for wealth and infrastructure, while slightly downplaying offense to allow builders the capacity for airport construction.
            
            **Adjusting Tool Usage**
            
            I've realized that `focus-briefer` isn't a valid tool according to the available declarations. I must stick to the six declared tools, which are `set-persona`, `set-relationship`, `set-flavors`, `set-research`, `set-policy`, and `keep-status-quo`. My current plan involves calling `set-flavors`, `set-policy`, and `set-research` with specific values to guide AI behavior and my strategic direction.
            
            **Refining Economic and Strategic Priorities**
            
            I am now fine-tuning our approach to ensure victory. By prioritizing gold generation and infrastructure development with specific flavor settings, and adopting the "Liberty" policy for immediate financial and worker boosts, I aim to overcome our economic crisis and prepare for the final conquest of Cusco. My focus is on critical aluminum acquisition and airport construction.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: nT8k9G6iYoXIIOSO
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - Culture: 5
              - Naval: 80
              - Mobilization: 40
              - TileImprovement: 100
              - Science: 50
              - Recon: 85
              - Airlift: 100
              - MilitaryTraining: 70
              - Diplomacy: 10
              - Gold: 100
              - Antiair: 50
              - GreatPeople: 40
              - Production: 100
              - AirCarrier: 95
              - Air: 100
              - NavalGrowth: 20
              - Expansion: 5
              - Ranged: 65
              - Spaceship: 0
              - Offense: 80
              - NavalRecon: 60
              - Mobile: 0
              - Defense: 40
              - Religion: 10
              - Infrastructure: 100
              - NavalTileImprovement: 25
              - Nuke: 100
              - WaterConnection: 35
              - Happiness: 70
              - Wonder: 5
              - Growth: 20
              - UseNuke: 95
              - CityDefense: 60
              - Espionage: 50
            - Rationale: GOLD CRISIS AND EXECUTION CORRECTION: Facing a severe -900 GPT deficit with 520 gold in reserve, we are on the verge of bankruptcy. To prevent unit disbandment, we drastically raise Gold flavor to 100 and lower Science to 50 to force idle city queues to run Wealth and prioritize gold buildings. We reduce Mobilization to 40 and Offense to 80 to pause excessive military unit spam. This frees up production for Builders (TileImprovement 100) to mine our 6 aluminum tiles and construct forward airports (Airlift 100, Infrastructure 100) for the final push on Cusco. Grand Strategy remains Conquest.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: RnbM2iS7kXiQFQy2
          - toolName: set-policy
          - input:
            - Policy: Liberty
            - Rationale: ECONOMIC AND WORKER EMERGENCY: Selecting Liberty as our next policy. Its adoption will immediately give us +2 Gold per city, providing +76 GPT across our 38 cities to help alleviate our cash-flow crisis, speed up tile improvement rate by +25%, and spawn a free Worker near our Capital to start mining our critical unimproved aluminum resources.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: hJoJbmN5UjVm4ovO
          - toolName: set-research
          - input:
            - Rationale: WEAPONS OF MASS DESTRUCTION: Setting Advanced Ballistics as our next research technology. This will unlock Nuclear Missiles and Guided Missiles, providing ultimate atomic siege capability to support our final assault on Cusco once Nuclear Fission completes in 6 turns.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: nT8k9G6iYoXIIOSO
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
          - toolCallId: RnbM2iS7kXiQFQy2
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: hJoJbmN5UjVm4ovO
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.