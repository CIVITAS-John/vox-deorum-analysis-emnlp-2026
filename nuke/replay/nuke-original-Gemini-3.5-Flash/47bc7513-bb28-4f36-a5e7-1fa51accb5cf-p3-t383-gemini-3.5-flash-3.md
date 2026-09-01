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
      - toolName: set-persona
      - args:
        - Boldness: 10
        - Rationale: FINAL BLITZ: We are 1 capital away from a Domination Victory (Cusco). Boldness and WarBias are maximized to force the tactical AI to push relentlessly toward Cusco. Meanness is increased to ensure the AI rejects any peace offers from the Inca, as total conquest of their capital is our sole victory condition.
        - WarBias: 10
        - Meanness: 8
        - Forgiveness: 1
    - #1:
      - toolName: set-research
      - args:
        - Rationale: NUCLEAR OPTION: With Nuclear Fission finishing in 6 turns, Advanced Ballistics is selected next to unlock Nuclear Missiles. This will provide the ultimate destructive capability to vaporize Cusco's defenses and secure our 8th and final capital for a Domination Victory.
        - Technology: Advanced Ballistics
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Iron Fist
        - Rationale: VASSAL AND WORKER EFFICIENCY: Selecting 'Iron Fist' (Autocracy Tenet) next. This policy will provide +50% Worker Improvement rate, helping us build the critical Aluminum mines and railroads much faster. It also increases yields tributed by our vassals (Russia and Austria) by 25% and boosts city-state yields by 25%, helping to offset our severe budget deficit.
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - AirCarrier: 95
          - UseNuke: 100
          - Production: 100
          - Offense: 95
          - Mobilization: 80
          - TileImprovement: 100
          - Science: 80
          - Infrastructure: 10
          - Nuke: 100
          - Gold: 100
          - Naval: 95
          - Air: 100
        - GrandStrategy: Conquest
      - rationale: EMERGENCY ECONOMY AND TILE PIVOT: Correcting severe tactical execution failures. 1) Placed Gold at 100 to force cities with completed projects (Kyoto, Tokyo, Graz, Vienna, Kuala Lumpur) to produce Wealth, immediately neutralizing the -900 GPT bankruptcy crisis. 2) Slashed Infrastructure to 10 while keeping TileImprovement at 100, forcing the 7 builders to abandon railroad loops and immediately construct mines on our 6 aluminum resources. 3) Maintained max Offense, Nuke, UseNuke, and Naval to prepare for the final Yamato and atomic assault on Cusco.
  - tokens:
    - inputTokens: 22067
    - reasoningTokens: 7817
    - outputTokens: 477
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current State**
            
            My thoughts are currently focused on a thorough analysis of our strategic position. I am evaluating our standing within the Information Era, particularly concerning our current score and how it reflects our progress in this critical phase of the game.
            
            **Conquering Cusco**
            
            I'm focused on securing Cusco, as it's the last capital needed for a Domination Victory. Our war against the Inca is progressing extremely well, with a significant war score advantage and higher weariness on their part.
            
            **Prioritizing Victory Condition**
            
            I'm prioritizing a Domination Victory by capturing Cusco, as it is the final capital required. Diplomatic Victory concerns are secondary given this immediate game-ending objective. I'm re-evaluating our economic situation due to impending bankruptcy, which is a direct consequence of our extensive military upkeep and rapid expansion.
            
            **Securing Funds**
            
            My immediate concern is averting bankruptcy. I'm exploring all avenues for gold generation, including assessing trade possibilities with vassals and re-examining research and policy options, despite the current research and policy cooldowns.
            
            **Addressing Financial Ruin**
            
            My immediate priority is tackling the impending bankruptcy. I'm analyzing the impact of our massive army and the Global Peace Accords on unit maintenance. I'm exploring the possibility of increasing the "Gold" flavor to incentivize the AI to generate much-needed revenue through wealth production once current projects conclude.
            
            **Boosting Gold Generation**
            
            My focus has shifted to aggressively boosting our gold reserves. I'm implementing a dramatic increase in the "Gold" flavor, aiming to pivot our immense production towards wealth generation and immediately address our GPT deficit. This should allow us to overcome impending bankruptcy.
            
            **Shifting Builder Priorities**
            
            I've identified a critical bottleneck concerning our builders. By significantly reducing the "Infrastructure" flavor from 100 to 10, I can redirect our 7 builders from railroad construction to vital tile improvements, specifically targeting the 6 available aluminum tiles. This should immediately boost our production and strategic resource acquisition.
            
            **Deploying Airpower Quickly**
            
            My thoughts are now on rapid air deployment to support Cusco's capture. I'm evaluating city options for airport construction near the front lines and confirming our naval capacity to potentially expedite this if necessary. The research path towards Nuclear Fission is being monitored for potential strategic advantages.
            
            **Researching Missiles**
            
            I am now focusing on researching Advanced Ballistics to unlock Nuclear Missiles, enabling the destruction of Cusco's defenses and securing our domination victory. I'm considering the optimal research path to expedite this critical objective.
            
            **Securing Vassal Dominance**
            
            I'm reassessing the "Iron Fist" policy. The boost to vassal tributes and worker improvement rates is incredibly relevant to our immediate financial and infrastructure challenges, especially with the increased yield from city-states.
            
            **Adopting "Iron Fist" Policy**
            
            I've determined that adopting the "Iron Fist" policy is paramount. The significant boost to worker improvement rates directly addresses our builder bottleneck, and the increased tribute from vassals will greatly aid our financial situation. I am initiating the `set-policy` command to select "Iron Fist."
            
            **Maintaining City-State Alliances**
            
            My current focus is on reinforcing our alliances with city-states to safeguard our delegate count. I'm assessing our high influence levels and ensuring no relationships are negatively impacted by ongoing conflicts, particularly with Oslo and Utica where peace is blocked.
            
            **Reinforcing City-State Relations**
            
            My focus is on solidifying alliances with city-states. I'm ensuring our delegate count remains secure, carefully managing influence levels, especially with Oslo and Utica, and noting resolutions impacting potential ally status, such as the "Open Door" policy on Lhasa.
            
            **Adjusting Economic Levers**
            
            My focus is now on fine-tuning economic levers to address our severe GPT deficit. I'm aggressively increasing the "Gold" flavor to 100 to incentivize wealth production and drastically reducing "Infrastructure" to 10 to free up builders for aluminum tile improvements. I'm also moderating "Science" to 80, balancing progress with immediate financial needs.
            
            **Adjusting Flavor Settings**
            
            I'm now focused on fine-tuning the internal flavor settings. My immediate goal is to maximize gold generation to escape bankruptcy by setting "Gold" and "Production" to 100, while drastically reducing "Infrastructure" to 10 to redirect builders to aluminum. "TileImprovement" is maxed to ensure this.
            
            **Sharpening Aggression**
            
            I'm enhancing our aggressive tendencies to secure the final victory. By raising Boldness and WarBias, and slightly increasing Meanness, I aim to ensure decisive action towards capturing Cusco and achieving domination.
            
            **Directing Focus on Key Metrics**
            
            I am now concentrating on directing analysts to provide specific, actionable reports for the upcoming turn. This will allow me to closely monitor builder actions on aluminum, our economic recovery from the GPT deficit, the progress of critical research like Nuclear Fission and the Manhattan Project, and the immediate battlefield situation around Cusco.
            
            **Directing Tool Application**
            
            I'm now focusing on the precise application of our analytical tools. My immediate concern is ensuring the correct parameters are used for `set-flavors`, specifically the grand strategy and flavor settings like Gold, Infrastructure, and Production. I'm also verifying the `set-persona` parameters to refine our diplomatic approach.
            
            **Refining Aggression Parameters**
            
            I'm now finalizing the aggressive posture by setting specific persona parameters. Boldness and WarBias are maxed out to ensure relentless pursuit of Cusco, with Meanness set to reject any Inca peace offers. I'm also clearing Oslo's relationship to ensure their war status is correctly reflected.
            
            **Clearing Oslo's Relationship**
            
            My focus is on clearing Oslo's relationship, but I've discovered that the `set-relationship` command only applies to major civilizations, not city-states like Oslo. Russia, Austria, and the Inca are already set at their desired diplomatic modifiers and are the only remaining major powers.
            
            **Verifying Settings**
            
            I am now confirming that all strategic settings align with our immediate objectives. I've verified the research path towards Nuclear Missiles, the adoption of the "Iron Fist" policy for economic and infrastructure boosts, and the flavor settings prioritizing gold generation and worker efficiency. My thoughts are on ensuring these are correctly implemented for maximum impact in the next turn cycle.
            
            **Finalizing Game-Winning Strategy**
            
            My thoughts are now focused on a comprehensive review of all implemented settings to guarantee a swift Domination Victory. I am confirming the research progression towards Nuclear Missiles, the strategic adoption of the "Iron Fist" policy for economic stabilization, and the fine-tuned flavor settings that prioritize immediate gold generation and builder efficiency. My focus is ensuring these critical adjustments are perfectly synchronized for maximum impact in the upcoming turn.
            
            **Verifying Tool Availability**
            
            I am now verifying the availability of specific analytical tools. I've identified that the `focus-briefer` command, which I thought was available for requesting focused reports on builder actions, economic recovery, and research progress, is not present in the current tool declarations. My thoughts are on adapting to the confirmed toolset for the upcoming turn.
            
            **Adapting to Tool Limitations**
            
            I'm now adjusting my approach based on the available tools. Since the `focus-briefer` command isn't accessible, I'll need to re-evaluate how to get the focused reports I need for monitoring builder actions, economic recovery, and research progress. I will proceed with the declared tools.
            
            **Finalizing Command Execution**
            
            I am now focused on ensuring the complete and accurate execution of the planned commands. I am verifying the parameters for `set-persona`, `set-research`, `set-policy`, and `set-flavors` to ensure they perfectly align with our Domination Victory objective and immediate financial stabilization needs.
            
            **Selecting Key Policies**
            
            I am now focused on selecting the 'Iron Fist' policy. This choice is critical as it significantly boosts worker improvement rates, which will expedite the construction of vital aluminum mines and railroads. Additionally, it will enhance tributes from our vassals, Russia and Austria, and increase yields from city-states, helping to alleviate our dire financial situation.
            
            **Implementing Economic & Tile Strategy**
            
            I am implementing a critical economic and tile strategy by setting `Gold` and `Production` flavors to 100, while drastically reducing `Infrastructure` to 10 and maximizing `TileImprovement`. This is designed to immediately resolve our bankruptcy crisis by forcing wealth generation and redirecting builders to essential tile improvements, specifically aluminum.
            
            **Prioritizing Missile Research**
            
            My current focus is on ensuring our research path is optimized for acquiring Nuclear Missiles. This is crucial for dismantling Cusco's defenses and securing our Domination Victory. I am closely monitoring the progression to expedite this vital objective.
            
            **Maximizing Aggression Parameters**
            
            I am now refining our aggressive posture by setting specific persona parameters. Boldness and WarBias are maxed out to ensure relentless pursuit of Cusco, with Meanness set to reject any Inca peace offers. I'm also clearing Oslo's relationship to ensure their war status is correctly reflected.
            
            **Verifying Strategic Settings**
            
            I am now confirming that all strategic settings align with our immediate objectives. I've verified the research path towards Nuclear Missiles, the adoption of the "Iron Fist" policy for economic and infrastructure boosts, and the flavor settings prioritizing gold generation and worker efficiency. My thoughts are on ensuring these are correctly implemented for maximum impact in the next turn cycle.
            
            **Finalizing Game-Winning Strategy**
            
            My thoughts are now focused on a comprehensive review of all implemented settings to guarantee a swift Domination Victory. I am confirming the research progression towards Nuclear Missiles, the strategic adoption of the "Iron Fist" policy for economic stabilization, and the fine-tuned flavor settings that prioritize immediate gold generation and builder efficiency. My focus is ensuring these critical adjustments are perfectly synchronized for maximum impact in the upcoming turn.
            
            **Adapting to Tool Limitations**
            
            I'm now adjusting my approach based on the available tools. Since the `focus-briefer` command isn't accessible, I'll need to re-evaluate how to get the focused reports I need for monitoring builder actions, economic recovery, and research progress. I will proceed with the declared tools.
            
            **Finalizing Command Execution**
            
            I am now focused on ensuring the complete and accurate execution of the planned commands. I am verifying the parameters for `set-persona`, `set-research`, `set-policy`, and `set-flavors` to ensure they perfectly align with our Domination Victory objective and immediate financial stabilization needs.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 2ZVHwfPdr3Pedf2n
          - toolName: set-persona
          - input:
            - Boldness: 10
            - Rationale: FINAL BLITZ: We are 1 capital away from a Domination Victory (Cusco). Boldness and WarBias are maximized to force the tactical AI to push relentlessly toward Cusco. Meanness is increased to ensure the AI rejects any peace offers from the Inca, as total conquest of their capital is our sole victory condition.
            - WarBias: 10
            - Meanness: 8
            - Forgiveness: 1
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: SkVcECGPvgNN5Mna
          - toolName: set-research
          - input:
            - Rationale: NUCLEAR OPTION: With Nuclear Fission finishing in 6 turns, Advanced Ballistics is selected next to unlock Nuclear Missiles. This will provide the ultimate destructive capability to vaporize Cusco's defenses and secure our 8th and final capital for a Domination Victory.
            - Technology: Advanced Ballistics
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: C83HylL1SHzNAEp4
          - toolName: set-policy
          - input:
            - Policy: Iron Fist
            - Rationale: VASSAL AND WORKER EFFICIENCY: Selecting 'Iron Fist' (Autocracy Tenet) next. This policy will provide +50% Worker Improvement rate, helping us build the critical Aluminum mines and railroads much faster. It also increases yields tributed by our vassals (Russia and Austria) by 25% and boosts city-state yields by 25%, helping to offset our severe budget deficit.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: D8f8HaXwER3IenmU
          - toolName: set-flavors
          - input:
            - Flavors:
              - AirCarrier: 95
              - UseNuke: 100
              - Production: 100
              - Offense: 95
              - Mobilization: 80
              - TileImprovement: 100
              - Science: 80
              - Infrastructure: 10
              - Nuke: 100
              - Gold: 100
              - Naval: 95
              - Air: 100
            - Rationale: EMERGENCY ECONOMY AND TILE PIVOT: Correcting severe tactical execution failures. 1) Placed Gold at 100 to force cities with completed projects (Kyoto, Tokyo, Graz, Vienna, Kuala Lumpur) to produce Wealth, immediately neutralizing the -900 GPT bankruptcy crisis. 2) Slashed Infrastructure to 10 while keeping TileImprovement at 100, forcing the 7 builders to abandon railroad loops and immediately construct mines on our 6 aluminum resources. 3) Maintained max Offense, Nuke, UseNuke, and Naval to prepare for the final Yamato and atomic assault on Cusco.
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 2ZVHwfPdr3Pedf2n
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: SkVcECGPvgNN5Mna
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: C83HylL1SHzNAEp4
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: D8f8HaXwER3IenmU
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.