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
  - replay_use_nuke: 100
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
      - toolName: set-research
      - args:
        - Rationale: Advanced Ballistics unlocks Nuclear Missiles and Guided Missiles. Since we are close to completing Nuclear Fission and the Manhattan Project, this technology is the logical next step to provide the ultimate offensive leverage needed to crush Cusco's defenses and secure our final domination victory capital.
        - Technology: Advanced Ballistics
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Iron Fist
        - Rationale: Iron Fist (Autocracy Level 1) provides +50% Worker Improvement rate, which is critical to solve our worker bottleneck and speed up the construction of aluminum mines on our 6 controlled tiles. Additionally, it increases yields from city-states and vassal tributes by 25%, which will help offset our severe -900 GPT deficit.
    - #2:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Science: 90
          - Production: 100
          - TileImprovement: 100
          - Happiness: 80
          - AirCarrier: 100
          - Infrastructure: 80
          - UseNuke: 100
          - Offense: 100
          - Nuke: 100
          - Air: 100
          - Espionage: 30
          - Gold: 50
          - Airlift: 100
          - Defense: 30
          - Mobilization: 90
        - GrandStrategy: Conquest
      - rationale: We are in the final conquest phase of the game, needing only Cusco to win. We maximize Offense (100), Nuke (100), UseNuke (100), and Air/AirCarrier (100) to prepare for a devastating atomic and air strike on Cusco, using carriers to bypass the distance bottleneck. We increase Gold to 50 to help the AI manage the -900 GPT deficit and prevent unit disbanding, while maintaining TileImprovement (100) and Production (100) to get the critical aluminum mines online.
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Private: 100
        - TargetID: 0
        - Rationale: Maintain maximum friendly relationship with Russia to ensure absolute loyalty and continued vassal contributions during the final offensive.
    - #4:
      - toolName: set-relationship
      - args:
        - Private: -100
        - Public: -100
        - TargetID: 2
        - Rationale: Maintain maximum hostility against the Inca to ensure the AI rejects any peace offers and focuses entirely on capturing Cusco.
    - #5:
      - toolName: set-relationship
      - args:
        - Rationale: Maintain maximum friendly relationship with Austria to ensure vassal stability, trade deals, and delegate support in the World Congress.
        - TargetID: 5
        - Private: 100
        - Public: 100
  - tokens:
    - inputTokens: 22067
    - reasoningTokens: 6324
    - outputTokens: 493
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Focusing on Inca War**
            
            I'm currently strategizing our ongoing conflict with the Inca in this Information Era. My focus is on leveraging our current technological advantage to decisively end this war and secure our position. I'm also considering how our alliances with Russia and Austria might play a role.
            
            **Capturing Cusco**
            
            I'm laser-focused on securing Cusco; its capture will grant us an immediate Domination Victory. With all other original capitals under our control, this final push is critical. I'm analyzing the military situation for a swift resolution.
            
            **Securing Final Capital**
            
            My attention is now fixed on the final push for Cusco. Despite our overwhelming military superiority and advantageous war score, I've identified a potential logistical concern with aluminum production. However, a closer examination reveals our current stockpile provides ample time to complete the operation before any critical shortage arises. Winchester Airport's imminent completion also presents a strategic advantage for air support, even without a nearby Japanese staging city.
            
            **Researching New Weapons**
            
            My focus has shifted to immediate research priorities. I'm evaluating whether to push for Advanced Ballistics to unlock nuclear capabilities or to secure Refrigeration. The potential of nuclear weapons for ending this Inca war is compelling, and I need to quickly ascertain our path to atomic bomb production.
            
            **Prioritizing Advanced Ballistics**
            
            My immediate research focus has pivoted. After weighing the options, securing Advanced Ballistics is clearly the superior path to military conquest, especially given our ongoing war. This decision will unlock crucial atomic capabilities needed for a swift conclusion to our conflict.
            
            **Adopting Iron Fist**
            
            My current focus is on resolving our significant GPT deficit and accelerating infrastructure development. I've decided to adopt the "Iron Fist" policy to dramatically increase our worker improvement rate, which will directly address the aluminum mining and railroad construction needed. This, combined with increased vassal tributes, should help alleviate our financial strain.
            
            **Addressing Gold Deficit**
            
            My current priority is tackling our severe GPT deficit, which is primarily driven by excessive unit maintenance due to the "Global Peace Accords." I'm investigating options to repeal this resolution in the upcoming World Congress and exploring potential gold-generating deals with vassals or through diplomatic channels.
            
            **Investigating GPT Collapse**
            
            I'm currently investigating a sudden, drastic drop in my GPT. Between turns 378 and 383, it plummeted from -7 to -900. Preliminary findings point to an increase in unit maintenance following the upgrade of several Japanese bombers to Heavy Bombers and the adoption of the "Total War" policy. I need to pinpoint the exact cause and mitigate this financial crisis immediately.
            
            **Assessing War Readiness**
            
            I'm currently evaluating our overwhelming military advantage against the Inca. With their cities unhappy and war weariness high, my focus is on ensuring our offensive flavors are maximized for a swift capture of Cusco. The massive disparity in military strength assures me a decisive victory is imminent.
            
            **Prioritizing Offensive Capabilities**
            
            My current focus is on re-calibrating our strategic flavors. I need to emphasize offensive and mobile unit production to swiftly conclude the Inca conflict. Additionally, ensuring our builders prioritize aluminum extraction is paramount for future atomic capabilities.
            
            **Adjusting Strategic Flavors**
            
            My current thoughts are on fine-tuning our strategic flavors to ensure victory. I'm prioritizing gold generation to prevent unit disbanding, while maintaining high offensive, mobilization, and nuke readiness. I'm also focused on tile improvements and overall production, aiming for a conquest grand strategy.
            
            **Analyzing City-State Dynamics**
            
            I'm currently analyzing city-state relationships, particularly the "Open Door" mechanic impacting my influence with Kabul, Lhasa, and Quebec City. This has locked them as Friends despite high standing, preventing potential alliances and delegate acquisition. I'm also ensuring loyalty across my own cities and maintaining an aggressive stance against the Inca.
            
            **Focusing on Inca Conquest**
            
            I'm shifting my focus back to the absolute priority: capturing Cusco. While I briefly explored diplomatic paths, the direct domination route is far more efficient and certain. I will concentrate all efforts on achieving this military objective swiftly.
            
            **Pursuing Advanced Ballistics**
            
            I'm now prioritizing Advanced Ballistics. This research is crucial to unlock nuclear capabilities, which I believe will swiftly end our conflict with the Inca and secure our victory.
            
            **Researching Critical Technologies**
            
            I'm now prioritizing Advanced Ballistics. This research is crucial to unlock nuclear capabilities, which I believe will swiftly end our conflict with the Inca and secure our victory. I'm also preparing to adopt "Iron Fist" for improved worker output to secure necessary resources.
            
            **Unleashing Atomic Power**
            
            I'm now prioritizing the acquisition and deployment of atomic capabilities. My current focus is on leveraging atomic bombs to decisively conclude the Inca war by targeting Cusco. This involves ensuring sufficient air power, including heavy bombers and carrier staging for aircraft from Winchester Airport, to deliver the decisive blow.
            
            **Unleashing Atomic Power**
            
            I'm now prioritizing the acquisition and deployment of atomic capabilities. My current focus is on leveraging atomic bombs to decisively conclude the Inca war by targeting Cusco. This involves ensuring sufficient air power, including heavy bombers and carrier staging for aircraft from Winchester Airport, to deliver the decisive blow.
            
            **Refining Conquest Flavors**
            
            I'm now fine-tuning our strategic flavors for the final push on Cusco. With an overwhelming focus on Offense, Nukes, and Air power, I'm also adjusting Gold to 50 to offset GPT deficits and ensuring Tile Improvement and Production remain high to secure vital aluminum resources.
            
            **Discovering Missing Tools**
            
            I've realized that a tool I assumed was available, `focus-briefer`, is not actually declared. I need to only use the explicitly listed tools: `set-persona`, `set-relationship`, `set-flavors`, `set-research`, `set-policy`, and `keep-status-quo` to guide my actions.
            
            **Identifying Available Tools**
            
            I am focusing on accurately identifying the available tools for this task. I have confirmed that `focus-briefer` is not declared, despite being mentioned in the prompt, and will therefore not be used. My actions will strictly adhere to the explicitly listed tools: `set-persona`, `set-relationship`, `set-flavors`, `set-research`, `set-policy`, and `keep-status-quo`.
            
            **Identifying Available Tools**
            
            I am focusing on accurately identifying the available tools for this task. I have confirmed that `focus-briefer` is not declared, despite being mentioned in the prompt, and will therefore not be used. My actions will strictly adhere to the explicitly listed tools: `set-persona`, `set-relationship`, `set-flavors`, `set-research`, `set-policy`, and `keep-status-quo`.
            
            **Focusing on Tool Discovery**
            
            I'm now focusing on identifying the correct tools. I've confirmed that `focus-briefer` is unavailable and will strictly use the provided list: `set-persona`, `set-relationship`, `set-flavors`, `set-research`, `set-policy`, and `keep-status-quo`.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: BpdT6SiDQMvBxgWS
          - toolName: set-research
          - input:
            - Rationale: Advanced Ballistics unlocks Nuclear Missiles and Guided Missiles. Since we are close to completing Nuclear Fission and the Manhattan Project, this technology is the logical next step to provide the ultimate offensive leverage needed to crush Cusco's defenses and secure our final domination victory capital.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: fUc9wygIPH7ibTnM
          - toolName: set-policy
          - input:
            - Policy: Iron Fist
            - Rationale: Iron Fist (Autocracy Level 1) provides +50% Worker Improvement rate, which is critical to solve our worker bottleneck and speed up the construction of aluminum mines on our 6 controlled tiles. Additionally, it increases yields from city-states and vassal tributes by 25%, which will help offset our severe -900 GPT deficit.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: O8r3PjKuMs7HtMkx
          - toolName: set-flavors
          - input:
            - Flavors:
              - Science: 90
              - Production: 100
              - TileImprovement: 100
              - Happiness: 80
              - AirCarrier: 100
              - Infrastructure: 80
              - UseNuke: 100
              - Offense: 100
              - Nuke: 100
              - Air: 100
              - Espionage: 30
              - Gold: 50
              - Airlift: 100
              - Defense: 30
              - Mobilization: 90
            - GrandStrategy: Conquest
            - Rationale: We are in the final conquest phase of the game, needing only Cusco to win. We maximize Offense (100), Nuke (100), UseNuke (100), and Air/AirCarrier (100) to prepare for a devastating atomic and air strike on Cusco, using carriers to bypass the distance bottleneck. We increase Gold to 50 to help the AI manage the -900 GPT deficit and prevent unit disbanding, while maintaining TileImprovement (100) and Production (100) to get the critical aluminum mines online.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: TPby6cLNX6MU4Auw
          - toolName: set-relationship
          - input:
            - Public: 100
            - Private: 100
            - TargetID: 0
            - Rationale: Maintain maximum friendly relationship with Russia to ensure absolute loyalty and continued vassal contributions during the final offensive.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: umiLc4HYASlZyEbW
          - toolName: set-relationship
          - input:
            - Private: -100
            - Public: -100
            - TargetID: 2
            - Rationale: Maintain maximum hostility against the Inca to ensure the AI rejects any peace offers and focuses entirely on capturing Cusco.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: vN0gkcAyo1bSrnue
          - toolName: set-relationship
          - input:
            - Rationale: Maintain maximum friendly relationship with Austria to ensure vassal stability, trade deals, and delegate support in the World Congress.
            - TargetID: 5
            - Private: 100
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: BpdT6SiDQMvBxgWS
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
          - toolCallId: fUc9wygIPH7ibTnM
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: O8r3PjKuMs7HtMkx
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: TPby6cLNX6MU4Auw
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: umiLc4HYASlZyEbW
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: vN0gkcAyo1bSrnue
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.