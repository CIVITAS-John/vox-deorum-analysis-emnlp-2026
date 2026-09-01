- row:
  - game_id: bf335c2d-64e4-443d-bb5f-084eef9ca4e6
  - player_id: 3
  - turn: 403
  - player_type: Kimi-K2.5-Briefed
  - prev_use_nuke: 80.0
  - after_use_nuke: 85.0
  - prev_nuke: 80.0
  - after_nuke: 90.0
  - rationale: Post-Manhattan Project completion (Turn 399) with Turn 403 WC vote imminent. Reduced Offense from 15 to 10 as territorial expansion counterproductive to diplomatic win. Maintaining high Defense/CityDefense/Air/Antiair to protect Bregenz nuclear facility and core cities. Increased Nuke from 80 to 90 to prioritize atomic bomb production for deterrence (Iroquois 5883 vs 4502 strength ratio). UseNuke 85 reflects imminent atomic capability by Turn 405. Espionage 85 continues election rigging in Assur/Sogut against German influence. Diplomacy 100 and Gold 90 prioritize Assur delegate acquisition post-quest and future WC coordination. Science 85 drives Nuclear Fission for World Ideology proposal. Freedom bloc currently holds 59 delegates (Austria 29 + Germany 20 + Venice 10) vs 45 needed; maintaining solidarity while pursuing additional delegate sources.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 95
  - replay_use_nuke: 80
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
    - You are Maria Theresa, leader of Austria (Player 3).
      
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
      - Name: Austria
      - Uniques:
        - Unique Unit: Hussar, Replacing Cuirassier (Requires technology: Metallurgy)
        - Unique Unit: Grenzer, Replacing Fusilier (Requires technology: Rifling)
        - Unique Building: Ballhausplatz, Replacing Printing Press (Requires technology: Printing Press)
        - Unique Building: Schützenstand, Replacing Military Academy (Requires technology: Military Science)
        - Civilization Ability: +50% rewards from Quests. May arrange Marriages to City-States with Gold after Allying for 10 Turns. Gain 200 Resting Influence with Married City-States while at peace.
      - Leader: Maria Theresa
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
      - Refrigeration: Allows Work Boats to construct an Offshore Platform, and increases Trade Route maximum travel distance.
        Completing it would unlock: Electronics, Computers
      - Nuclear Fission: Allows you to build the Bazooka, the most powerful ranged Unit and Atomic Bombs, the first nuclear weapon in the game (note: you must first have completed the Manhattan Project and have Uranium available). Also allows you to build the Nuclear Plant, a building which requires Uranium and increases the Production of a City.
        Completing it would unlock: Satellites, Advanced Ballistics
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      
      ## Policies
      - Containment (Level 3 Tenet of Ideology Freedom): Containment: Trade Routes to City-States generate +2 Influence per turn (with the target City-State) per owned City-State Trade Route (up to +10). +1 Delegate in the World Congress for every 2 City-States originally in the World.
      - Space Procurements (Level 3 Tenet of Ideology Freedom): Space Procurements: May invest in Spaceship parts with Gold. Build Spaceship Factories in half the usual time. +20% Science from Research Labs.
      - Draft Registration (Level 1 Tenet of Ideology Freedom): Draft Registration: Military Units purchased with Gold receive full XP.
      - Creative Expression (Level 1 Tenet of Ideology Freedom): Creative Expression: +2 Tourism from Great Works. Museums, Broadcast Towers, Opera Houses, and Amphitheaters gain +3 Golden Age Points and Culture.
      - Media Culture (Level 3 Tenet of Ideology Freedom): Media Culture: +25% Tourism and +1 Happiness generated by cities with a Broadcast Tower. +20% Culture from Stadiums.
      - Civil Society (Level 1 Tenet of Ideology Freedom): Civil Society: Specialists consume 2 Food less than normal (minimum 1 Food). Farms, Plantations, Camps, and all Unique Improvements produce +4 Food.
      - Avant Garde (Level 1 Tenet of Ideology Freedom): Avant Garde: The rate at which Great People are born is increased by 33%. -2 Unhappiness from Boredom in all Cities.
      - Entrepreneurship (Continuing Industry Branch):
        - * +1 Happiness from Workshops.
        - * +2 Production and +1 Gold from every Mine, Quarry, and Lumber Mill.
        - * +25% Yields when you expend Great Merchants or Great Engineers for their Instant Yield abilities.
      - Empiricism (Continuing Rationalism Branch):
        - * +1 Food for every Citizen and +25% Growth in all Cities.
        - * +3% Science in a City for every Great Work present (up to 20%).
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
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
      - Authority (New Branch):
        - Authority will greatly benefit warlike and expansionist civilizations.
        - Adopting Authority grants:
        - * +25% combat bonus VS Barbarians and receive announcements when Barbarian Camps spawn in revealed territory.
        - * Receive 25 Culture when you clear Barbarian Camps, scaling with Era.
        - * Receive Science and Culture when you kill a Unit equal to 50% of its Strength.
        - * +1 Production in every City.
        - Each Authority policy unlocked grants:
        - * Receive Science and Culture when you kill a Unit equal to 10% of its Strength.
        - Adopting all policies in Authority grants:
        - * Unlocks building Alhambra.
        - * Allows the purchasing of Free Companies, Foreign Legions, and Mercenaries as their prerequisite technologies are researched.
        - * Allows for the purchase of Great Generals with Faith starting in the Industrial Era.
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
        - VictoryCompetitiveness: 6
        - WonderCompetitiveness: 10
        - MinorCivCompetitiveness: 10
        - Boldness: 10
        - WarBias: 10
        - HostileBias: 1
        - WarmongerHate: 8
        - NeutralBias: 8
        - FriendlyBias: 10
        - GuardedBias: 6
        - AfraidBias: 3
        - DiplomaticBalance: 9
        - Friendliness: 9
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 8
        - Loyalty: 5
        - MinorCivFriendlyBias: 8
        - MinorCivNeutralBias: 1
        - MinorCivHostileBias: 1
        - MinorCivWarBias: 3
        - DenounceWillingness: 9
        - Forgiveness: 7
        - Meanness: 6
        - Neediness: 4
        - Chattiness: 8
        - DeceptiveBias: 8
        - Rationale: Maintaining high WarBias (10) and Boldness (10) with Manhattan Project completing in 2 turns, enabling nuclear deterrent posture against Iroquois 1:4.3 force ratio. Keeping FriendlyBias/WorkWithWillingness/DiplomaticBalance at maximum (9-10) for Freedom bloc cohesion with Germany (22 delegates), Venice (14), and Inca (24) - total 87 vs 45 needed for WC control. Reduced Chattiness from 10 to 8 to focus diplomatic bandwidth on critical World Ideology: Freedom proposal. DeceptiveBias 8 maintained for denouncement flexibility if Iroquois negotiations require aggressive posturing while preserving trade relationships with Spain post-war.
        
        ## Technology
        - Next: Nuclear Fission
        - Rationale: Critical path technology enabling World Ideology: Freedom proposal (requires Nuclear Fission discovered) and UN Building construction for +3 delegates. Current research Mobile Tactics completes in 6 turns; Nuclear Fission must follow immediately to maintain Turn 415-420 diplomatic victory timeline and enable atomic deterrent against Iroquois aggression.
        
        ## Policy
        - Next: Containment (Policy)
        - Rationale: Level 3 Freedom tenet provides +2 influence/turn from city-state trade routes and +1 delegate per 2 original city-states (~+9 delegates total). Essential for reaching 45+ delegate threshold by Turn 415-420 victory window. Policy available in 18 turns; synergizes with Trade Confederacy for massive gold generation enabling Assur influence campaign.
        
        ## Relationships
        
        ### Melbourne
        - Public: 30
        - Private: 35
        - Rationale: Setting moderate positive stance toward Zanzibar (ID 37), which has Iroquois at 16 influence (lower than their Copenhagen presence). Zanzibar has a Horses connection quest that I can complete via Winchester trade. +30 public shows interest without aggressive investment. +35 private reflects viable backup marriage option if Copenhagen or Sogut become too contested, or as a secondary target after Utica.
        - UpdatedTurn: 59
        
        ### Zanzibar
        - Public: 20
        - Private: 15
        - Rationale: Reducing Zanzibar priority from 30/25 to 20/15. At -49 influence vs Venice's 292 - gap unbridgeable with current resources. Imperial College quest (11 turns) not viable. Focus all diplomatic capital on Winchester marriage execution. Zanzibar can be revisited after Winchester secured and economic position strengthened post-Compass/Trade Confederacy.
        - UpdatedTurn: 206
        
        ### Copenhagen
        - Public: 100
        - Private: 100
        - Rationale: Copenhagen at 148 influence requires only 52 more to reach Ally status (200). Spy mission completing Turn 314 will provide +300 influence, immediately enabling marriage for +1 delegate. Maximum relationship ensures AI prioritizes marriage execution the moment Ally threshold is crossed, critical for delegate accumulation toward 45-vote goal.
        - UpdatedTurn: 311
        
        ### Byzantium
        - Public: 10
        - Private: 5
        - Rationale: Byzantium war is low-value engagement. They suffer severe 31% happiness penalties and pose minimal offensive threat. Minimize diplomatic investment to conserve capital for WC-critical relationships and coal acquisition efforts.
        - UpdatedTurn: 373
        
        ### Yamatai
        - Public: 20
        - Private: 15
        - Rationale: Reducing Yamatai (ID 31) from 50/45 to 20/15. Inca's 962 influence makes Ally status unattainable; my 39 influence is negligible. Low return on diplomatic investment given Inca's insurmountable lead. Reallocating diplomatic capital to Aztlan and Utica which offer realistic delegate conversion paths.
        - UpdatedTurn: 375
        
        ### Vilnius
        - Public: 40
        - Private: 35
        - Rationale: Reducing Vilnius from 90/85 to 40/35. Open Door policy permanently blocks Ally status regardless of influence (currently 730, threshold 700 unattainable). Cannot secure delegate without repeal proposal, which is not viable before Turn 379 WC vote. Accept strategic loss and reallocate diplomatic capital to Aztlan and Utica which offer realistic +2 delegate path.
        - UpdatedTurn: 376
        
        ### Babylon
        - Public: 25
        - Private: 20
        - Rationale: MAINTAINING Babylon relationship at 25/20. Despite reduced diplomatic priority, Babylon's 6 delegates and shared Buddhism create minimal baseline value. Hostile approach from Babylon limits ROI; keeping minimal positive stance sufficient for potential future cooperation without significant capital allocation.
        - UpdatedTurn: 390
        
        ### Vancouver
        - Public: 40
        - Private: 35
        - Rationale: MAINTAINING Vancouver at 40/35. Sphere proposal passes in 3 turns with Freedom bloc 64 delegates - will become permanent Ally with marriage active. No further investment needed once passed. 40/35 maintains positive relationship sufficient for post-sphere stability without diverting capital from other delegate sources.
        - UpdatedTurn: 390
        
        ### Winchester
        - Public: 60
        - Private: 55
        - Rationale: MAINTAINING Winchester at 60/55. Marriage active at 1010 influence, delegate secured. 60/55 maintains sufficient positive relationship without excessive diplomatic investment. Resources better allocated to post-Vancouver sphere targets if any viable city-states remain for conversion.
        - UpdatedTurn: 390
        
        ### Abernethy
        - Public: 60
        - Private: 55
        - Rationale: MAINTAINING Abernethy at 60/55. Marriage active at 1410 influence, substantial lead over any competitor. Delegate secured. 60/55 sufficient for stability without diverting resources from contested city-states.
        - UpdatedTurn: 390
        
        ### Bunkeya
        - Public: 60
        - Private: 55
        - Rationale: MAINTAINING Bunkeya at 60/55. Marriage active at 1115 influence, delegate secured. No immediate threats to Ally status. Resources better allocated to Utica sphere proposal preparation and Vancouver WC vote coordination.
        - UpdatedTurn: 390
        
        ### Utica
        - Public: 20
        - Private: 15
        - Rationale: REDUCING Utica from 100/100 to 20/15. Germany (988 influence) has secured Ally status over Austria (826), making marriage/delegate unattainable without massive gold investment that would damage Germany relations and Freedom bloc cohesion. Accepting strategic loss to consolidate diplomatic capital elsewhere. Maintaining minimal positive relationship with Germany (who holds Utica) to preserve 22 delegate alliance for World Congress coordination. Resources better allocated to Vancouver sphere maintenance and identifying alternative delegate sources.
        - UpdatedTurn: 395
        
        ### Zuunmod
        - Public: 35
        - Private: 30
        - Rationale: REDUCING Zuunmod from 40/35 to 35/30. Inca Ally at 1184 influence is insurmountable (need +743 to reach 800 Ally threshold). Even maximum investment cannot flip this city-state before diplomatic victory window (Turn 415). Accepting strategic loss to focus on winnable targets. Maintaining moderate relationship for potential post-victory consolidation or if Inca influence unexpectedly drops.
        - UpdatedTurn: 400
        
        ### Germany
        - Public: 100
        - Private: 100
        - Rationale: MAINTAINING Germany at maximum 100/100 relationship. Critical Freedom bloc cohesion for Turn 403 WC vote - Austria 29 + Germany 19 + Venice 10 = 58 delegates vs 45 needed (note: Venice shows 10 delegates in current read, not 13). Germany's Antananarivo sphere proposal will pass; accepting this preserves alliance for World Ideology: Freedom passage. Defensive Pact NOT active (Germany has with Babylon), but DoF active. Supporting German sphere maintains bloc unity.
        - UpdatedTurn: 402
        
        ### Venice
        - Public: 90
        - Private: 85
        - Rationale: MAINTAINING Venice at high 90/85 relationship. Freedom bloc solidarity critical - their 10 delegates (current read) ensure 58-61 total vs 45 threshold. They supported Vancouver sphere and will support World Ideology: Freedom. Open Borders and DoF active. Stable partnership for Turn 403 WC vote coordination; slightly reduced from 85/80 to 90/85 to signal continued strong commitment.
        - UpdatedTurn: 402
        
        ### The Inca
        - Public: 55
        - Private: 50
        - Rationale: REDUCING Inca from 65/60 to 55/50. They opposed Vancouver sphere proposal and follow Order ideology, creating fundamental conflict. Their 23 delegates could theoretically support Freedom proposals, but WC behavior suggests opportunistic alignment. Further reduction signals displeasure with sphere opposition while preserving trade benefits and Open Borders. Information Era tech lead (72 vs 63) demands cautious approach - avoid provoking until diplomatic victory secured.
        - UpdatedTurn: 402
        
        ### Spain
        - Public: 40
        - Private: 35
        - Rationale: REDUCING Spain from 85/80 to 40/35. Peace treaty needed for resource trade (aluminum-for-coal), but their Autocracy ideology and ongoing war create fundamental ceiling. 22 turns remaining on peace timer makes immediate reconciliation impossible. Reduction reflects realistic assessment - high relationship not achievable until peace signed and ideology divergence addressed. Focus on practical post-peace resource acquisition timeline.
        - UpdatedTurn: 402
        
        ### The Iroquois
        - Public: -45
        - Private: -50
        - Rationale: INTENSIFYING hostile stance toward Iroquois from -35/-40 to -45/-50. Grand River citadel collapsed; Iroquois military strength 6066 vs Austria 4345 (1.4:1 ratio). Nuclear deterrent becomes operational Turn 405 - maximum diplomatic hostility reinforces deterrence posture. Clear signaling that further territorial aggression risks nuclear escalation. Maintains Freedom bloc cohesion by opposing Order ideology. No peace negotiations until defensive line stabilized or diplomatic victory secured.
        - UpdatedTurn: 402
        
        ### Assur
        - Public: 60
        - Private: 55
        - Rationale: INCREASING Assur from 50/45 to 60/55. Germany Ally at 686 influence, Austria at 321 (gap 365). Tech quest (173 influence) makes target achievable with ~5,000 gold investment. Assur represents realistic +1 delegate opportunity post-Containment. Higher increase signals sustained investment intention; need to surpass 800 influence threshold. Priority target given German sphere at Antananarivo will pass.
        - UpdatedTurn: 402
        
        ### Aztlan
        - Public: 20
        - Private: 15
        - Rationale: REDUCING Aztlan from 30/25 to 20/15. Open Door policy permanently blocks Ally status at 40 influence. No repeal proposal imminent for Turn 403 vote. Cannot secure delegate without repeal. Accepting strategic loss to reallocate diplomatic capital to Assur. Minimal relationship maintained for contingency if repeal proposed later.
        - UpdatedTurn: 402
        
        ### Antananarivo
        - Public: 20
        - Private: 15
        - Rationale: REDUCING Antananarivo from 15/10 to 20/15 (actually slight increase). German sphere proposal passes Turn 403 with Freedom bloc support; Germany already Ally at 1236 influence. Acknowledging German dominance while maintaining minimal positive stance for potential post-vote stability. No realistic path to flip before diplomatic victory window.
        - UpdatedTurn: 402
        
        ### Sogut
        - Public: 30
        - Private: 25
        - Rationale: MAINTAINING Sogut at 30/25. Germany Ally at 1350 influence, my 375 insufficient to challenge. Spy (Lothar/Elfriede) conducting election rigging - potential to reduce German influence over time. Low priority given Assur offers better delegate ROI with tech quest available. Open Door not blocking but massive German lead makes flip unlikely without sustained campaign.
        - UpdatedTurn: 402
        
        ## Strategy
        - Rationale: Critical defensive juncture with Grand River fallen. Nuclear deterrent operational in 5 turns (Turn 405/406) - must hold Iroquois at bay until then. Maintaining maximum Defense/CityDefense/Antiair to protect Bregenz nuclear facility and Linz-Vienna corridor. High Mobile (80) enables rapid reinforcement; UseNuke at 80 reflects imminent atomic capability for deterrence. Espionage (90) accelerates election rigging in Assur/Sogut against German influence. Diplomacy (100) and Gold (95) prioritize Assur delegate acquisition post-Containment and WC vote coordination. Science (90) drives to Nuclear Fission for World Ideology: Freedom proposal and UN Building. Reduced Offense (15) as territorial expansion counter-productive to diplomatic win condition.
        - GrandStrategy: UnitedNations
        
        ### Flavors
        - Offense: 15
        - Defense: 90
        - Mobilization: 65
        - CityDefense: 85
        - MilitaryTraining: 65
        - Recon: 20
        - Ranged: 75
        - Mobile: 80
        - Nuke: 80
        - UseNuke: 80
        - Naval: 35
        - NavalRecon: 30
        - NavalGrowth: 15
        - NavalTileImprovement: 30
        - Air: 85
        - AirCarrier: 25
        - Antiair: 85
        - Airlift: 55
        - Expansion: 15
        - Growth: 70
        - TileImprovement: 50
        - Infrastructure: 70
        - Production: 80
        - WaterConnection: 35
        - Gold: 95
        - Science: 90
        - Culture: 30
        - Happiness: 75
        - GreatPeople: 65
        - Wonder: 15
        - Religion: 10
        - Diplomacy: 100
        - Spaceship: 50
        - Espionage: 90
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Babylon
        - Leader: Nebuchadnezzar II
        - IsMajor: true
        - OurOpinionOfThem:
          - Austria's leader has expressed a public opinion of Babylon (25).
          - Austria's leader has formed a private opinion of Babylon (20).
          - We have made Declarations of Friendship with the same leaders! (8)
          - You (Babylon) have gone to war in the past.
          - Austria's real approach to Babylon is Neutral.
          - We have divergent Social Policies. (-3)
          - Your (Babylon) spies were caught stealing from Austria. (-33)
          - We defeated Austria's proposal in the United Nations. (-36)
        - TheirOpinionOfUs:
          - We have made Declarations of Friendship with the same leaders!
          - You (Austria) are not competing for technological advancement.
          - You (Austria) have no contested borders.
          - You (Austria) have gone to war in the past.
          - We are completely untrustworthy to Babylon.
          - Babylon have denounced us (Austria)!
          - Babylon suspect we might be a threat to Babylon.
          - We have divergent Social Policies.
          - Your (Austria) votes opposed Babylon's civ's interests in the United Nations.
          - You (Austria) are competing for World Wonders.
          - Babylon disliked our proposal to the United Nations.
          - You (Austria) are competing for the favor of the same City-States!
          - Your (Austria) spies were caught stealing from Babylon.
          - You (Austria) captured Babylon's original capital.
        - Score: 968
        - Era: Modern
        - Technologies: 55
        - Cities: 3
        - Population: 62
        - Territory: 81
        - Gold: 419
        - GoldPerTurn: -7
        - HappinessSituation: Happy
        - HappinessPercentage: 75
        - MilitaryStrength: 1212
        - TourismPerTurn: 133.5
        - CulturePerTurn: 442
        - PolicyBranches:
          - Progress: 6
          - Rationalism: 5
          - Artistry: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Close
            - Denounced Them
          - The Iroquois:
            - Distance: Far
          - Venice:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Spain:
            - Distance: Neighbors
            - Open Borders
          - Germany:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Inca:
            - Distance: Neighbors
            - Open Borders
        - Votes: 6
        
        ## Player 1
        - Civilization: The Iroquois
        - Leader: Hiawatha
        - IsMajor: true
        - OurOpinionOfThem:
          - Austria's real approach to The Iroquois is War.
          - We have divergent Social Policies. (-3)
          - You (The Iroquois) have denounced a leader Austria made a Declaration of Friendship with! (-11)
          - Your (The Iroquois) spies were caught stealing from Austria. (-33)
          - Austria's leader has expressed a public opinion of The Iroquois (-45).
          - Austria's leader has formed a private opinion of The Iroquois (-50).
          - You (The Iroquois) stole Austria's territory! (-50)
          - You (The Iroquois) have chosen to adopt the Order Ideology, but Austria believe in Freedom. (-999)
          - You (The Iroquois) are at war! (-99999)
        - TheirOpinionOfUs:
          - We have divergent Social Policies.
          - You (Austria) have made a Declaration of Friendship with one of The Iroquois's enemies!
          - Your (Austria) spies were caught stealing from The Iroquois.
          - Territorial disputes strain your (Austria) relationship.
          - You (Austria) are competing for the favor of the same City-States!
          - The Iroquois disliked our proposal to the United Nations.
          - We have denounced each other!
          - Your (Austria) success infuriates The Iroquois.
          - Your (Austria) votes opposed The Iroquois's civ's interests in the United Nations.
          - You (Austria) have chosen to adopt the Freedom Ideology, but The Iroquois believe in Order.
          - You (Austria) are at war!
        - Score: 2099
        - Era: Atomic
        - GoldenAge: 11 turns remaining
        - Technologies: 59
        - Cities: 11
        - Population: 253
        - Territory: 270
        - Gold: 1057
        - GoldPerTurn: 260
        - HappinessSituation: Happy
        - HappinessPercentage: 57
        - MilitaryStrength: 5883
        - TourismPerTurn: 437
        - CulturePerTurn: 1371
        - PolicyBranches:
          - Fealty: 6
          - Order: 3
          - Imperialism: 6
          - Authority: 6
        - FoundedReligion: Confucianism
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -2%; Our War Weariness: 17%)
            - Denounced Them
          - Germany:
            - Distance: Far
            - Peace Treaty
            - Denounced Them
          - Babylon:
            - Distance: Far
          - Spain:
            - Distance: Close
          - The Inca:
            - Distance: Close
            - War (Our Score: -2%; Our War Weariness: 12%)
            - Denounced Them
          - Venice:
            - Distance: Neighbors
            - Denounced Them
        - Votes: 11
        
        ## Player 2
        - Civilization: The Inca
        - Leader: Pachacuti
        - IsMajor: true
        - OurOpinionOfThem:
          - Austria's leader has expressed a public opinion of The Inca (55).
          - Austria's leader has formed a private opinion of The Inca (50).
          - We are trade partners. (40)
          - We have opened our borders to each other. (12)
          - You (The Inca) have denounced one of Austria's declared enemies! (11)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have shared embassies. (1)
          - Austria's real approach to The Inca is Friendly.
          - We have divergent Social Policies. (-3)
          - We defeated Austria's proposal in the United Nations. (-36)
          - You (The Inca) have chosen to adopt the Order Ideology, but Austria believe in Freedom. (-999)
        - TheirOpinionOfUs:
          - The Inca's leader has expressed a public opinion of you (Austria) (100).
          - We passed The Inca's proposal in the United Nations.
          - We have made Declarations of Friendship with the same leaders!
          - You (Austria) have denounced one of The Inca's declared enemies!
          - We are trade partners.
          - The Inca liked our proposal to the United Nations.
          - We were previously friends with The Inca's civilization.
          - We have Pledged to Protect the same City-States.
          - We have opened our borders to each other.
          - We fought together against a common foe.
          - We have shared embassies.
          - We have divergent Social Policies.
          - You (Austria) have chosen to adopt the Freedom Ideology, but The Inca believe in Order.
          - The Inca desire friendly relations with Austria.
          - Your (Austria) votes opposed The Inca's civ's interests in the United Nations.
        - Score: 3509
        - Era: Information
        - GoldenAge: 2 turns remaining
        - Technologies: 72
        - Cities: 16
        - Population: 450
        - Territory: 541
        - Gold: 4996
        - GoldPerTurn: 1532
        - HappinessSituation: Happy
        - HappinessPercentage: 70
        - MilitaryStrength: 28743
        - TourismPerTurn: 1905.08
        - CulturePerTurn: 2788
        - PolicyBranches:
          - Tradition: 5
          - Rationalism: 2
          - Progress: 1
          - Authority: 2
          - Fealty: 1
          - Industry: 2
          - Artistry: 1
          - Statecraft: 3
          - Order: 6
          - Imperialism: 1
        - FoundedReligion: Buddhism
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Open Borders
          - The Iroquois:
            - Distance: Close
            - War (Our Score: 2%; Our War Weariness: 15%)
            - Denounced Them
          - Babylon:
            - Distance: Neighbors
            - Open Borders
          - Spain:
            - Distance: Neighbors
            - Denounced Them
          - Germany:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - Venice:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 22
        
        ## Player 3
        - Civilization: Austria
        - Leader: Maria Theresa
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: Venice, Our top defensive pact ally: None
          - Our top United Nations ally: Venice, Our top United Nations rival: The Inca
          - Our top Competitor: The Iroquois
        - Score: 2079
        - Era: Atomic
        - GoldenAge: Estimated in 24 turns
        - Technologies: 63
        - CurrentResearch: Mobile Tactics (Estimated in 3 turns)
        - NextPolicyTurns: 17
        - Cities: 7
        - Population: 170
        - Territory: 202
        - Gold: 9388
        - GoldPerTurn: 678
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryUnits: 46
        - MilitarySupply: 47
        - MilitaryStrength: 4502
        - TourismPerTurn: 532
        - CulturePerTurn: 1009
        - FaithPerTurn: 133
        - SciencePerTurn: 1644
        - PolicyBranches:
          - Freedom:
            - Covert Action
            - Economic Union
            - Universal Suffrage
            - Arsenal of Democracy
            - Universal Healthcare
          - Industry:
            - Industry
            - Division of Labor
            - Mercantilism
            - Free Trade
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Rights of Man
          - Progress:
            - Progress
            - Organization
            - Liberty
            - Expertise
            - Equality
            - Fraternity
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
            - Exchange Markets
            - Trade Confederacy
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - Open Borders
          - The Iroquois:
            - Distance: Neighbors
            - War (Our Score: 2%; Our War Weariness: 24%)
            - Denounced Them
          - Babylon:
            - Distance: Close
          - Spain:
            - Distance: Far
            - War (Our Score: -2%; Our War Weariness: 11%)
            - Denounced Them
          - Germany:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - Venice:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
        - Votes: 29
        
        ## Player 4
        - Civilization: Venice
        - Leader: Enrico Dandolo
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Venice) have both chosen to adopt the Freedom Ideology. (999)
          - Austria's leader has expressed a public opinion of Venice (90).
          - Austria's leader has formed a private opinion of Venice (85).
          - We are trade partners. (40)
          - We have opened our borders to each other. (12)
          - You (Venice) have denounced one of Austria's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have shared embassies. (1)
          - Austria's real approach to Venice is Friendly.
          - We have divergent Social Policies. (-3)
          - We defeated Austria's proposal in the United Nations. (-36)
        - TheirOpinionOfUs:
          - You (Austria) have both chosen to adopt the Freedom Ideology.
          - You (Austria) have denounced one of Venice's declared enemies!
          - Venice's leader has expressed a public opinion of you (Austria) (50).
          - We are trade partners.
          - Venice liked our proposal to the United Nations.
          - We have made Declarations of Friendship with the same leaders!
          - We have made a public Declaration of Friendship!
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - We have shared embassies.
          - We have divergent Social Policies.
          - Venice desire friendly relations with Austria.
          - You (Austria) plundered Venice's trade routes!
          - Your (Austria) votes opposed Venice's civ's interests in the United Nations.
        - Score: 1502
        - Era: Modern
        - Technologies: 57
        - Cities: 5
        - Population: 125
        - Territory: 162
        - Gold: 100
        - GoldPerTurn: 36
        - HappinessSituation: Happy
        - HappinessPercentage: 61
        - MilitaryStrength: 1955
        - TourismPerTurn: 247.75
        - CulturePerTurn: 566
        - PolicyBranches:
          - Statecraft: 6
          - Freedom: 4
          - Progress: 6
          - Artistry: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - The Iroquois:
            - Distance: Neighbors
            - Denounced Them
          - Babylon:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Spain:
            - Distance: Neighbors
            - War (Our Score: -88%; Our War Weariness: 63%)
            - Denounced Them
          - Germany:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - The Inca:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 10
        - 5: Defeated Major Civilization Byzantium
        
        ## Player 6
        - Civilization: Spain
        - Leader: Isabella
        - IsMajor: true
        - OurOpinionOfThem:
          - Austria's leader has expressed a public opinion of Spain (40).
          - Austria's leader has formed a private opinion of Spain (35).
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Austria's real approach to Spain is War.
          - You (Spain) have denounced a leader Austria made a Declaration of Friendship with! (-11)
          - We defeated Austria's proposal in the United Nations. (-36)
          - You (Spain) have chosen to adopt the Autocracy Ideology, but Austria believe in Freedom. (-999)
          - You (Spain) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Austria) have no contested borders.
          - We have Pledged to Protect the same City-States.
          - We have similar Social Policies.
          - You (Austria) have made a Declaration of Friendship with one of Spain's enemies!
          - Spain disliked our proposal to the United Nations.
          - You (Austria) are competing for the favor of the same City-States!
          - We have denounced each other!
          - Your (Austria) votes opposed Spain's civ's interests in the United Nations.
          - We defeated Spain's proposal in the United Nations.
          - You (Austria) have chosen to adopt the Freedom Ideology, but Spain believe in Autocracy.
          - You (Austria) are at war!
        - Score: 3098
        - Era: Atomic
        - GoldenAge: 6 turns remaining
        - Technologies: 60
        - Cities: 14
        - Population: 356
        - Territory: 583
        - Gold: 54
        - GoldPerTurn: 308
        - HappinessSituation: Happy
        - HappinessPercentage: 56
        - MilitaryStrength: 10900
        - TourismPerTurn: 632
        - CulturePerTurn: 2403
        - PolicyBranches:
          - Fealty: 1
          - Autocracy: 4
          - Tradition: 5
          - Rationalism: 1
          - Statecraft: 6
          - Imperialism: 4
          - Industry: 1
          - Progress: 4
        - FoundedReligion: Catholicism
        - Relationships:
          - Austria:
            - Distance: Far
            - War (Our Score: 2%; Our War Weariness: 9%)
            - Denounced Them
          - The Iroquois:
            - Distance: Close
          - Babylon:
            - Distance: Neighbors
            - Open Borders
          - Germany:
            - Distance: Close
            - Denounced Them
          - Venice:
            - Distance: Neighbors
            - War (Our Score: 88%; Our War Weariness: 17%)
            - Denounced Them
          - The Inca:
            - Distance: Neighbors
            - Denounced Them
        - Votes: 13
        
        ## Player 7
        - Civilization: Germany
        - Leader: Bismarck
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Germany) have both chosen to adopt the Freedom Ideology. (999)
          - Austria's leader has expressed a public opinion of Germany (100).
          - Austria's leader has formed a private opinion of Germany (100).
          - We are trade partners. (40)
          - We have opened our borders to each other. (12)
          - You (Germany) have denounced one of Austria's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Austria's real approach to Germany is Friendly.
          - We defeated Austria's proposal in the United Nations. (-36)
        - TheirOpinionOfUs:
          - You (Austria) have both chosen to adopt the Freedom Ideology.
          - Germany's leader has expressed a public opinion of you (Austria) (100).
          - You (Austria) have denounced one of Germany's declared enemies!
          - Germany liked our proposal to the United Nations.
          - We have made Declarations of Friendship with the same leaders!
          - We have similar Social Policies.
          - We have made a public Declaration of Friendship!
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - We fought together against a common foe.
          - We have shared embassies.
          - Germany desire friendly relations with Austria.
          - We previously defeated Germany's proposal in the United Nations.
          - Your (Austria) votes opposed Germany's civ's interests in the United Nations.
        - Score: 2253
        - Era: Atomic
        - GoldenAge: 5 turns remaining
        - Technologies: 61
        - Cities: 8
        - Population: 167
        - Territory: 275
        - Gold: 1841
        - GoldPerTurn: 1066
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 5428
        - TourismPerTurn: 574.5
        - CulturePerTurn: 1287
        - PolicyBranches:
          - Fealty: 1
          - Freedom: 4
          - Industry: 2
          - Rationalism: 1
          - Statecraft: 6
          - Imperialism: 1
          - Progress: 3
          - Authority: 5
        - FoundedReligion: Protestantism
        - Relationships:
          - Austria:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - The Iroquois:
            - Distance: Far
            - Peace Treaty
            - Denounced Them
          - Babylon:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Spain:
            - Distance: Close
            - Denounced Them
          - Venice:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - The Inca:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
        - Votes: 20
        
        ## Player 22
        - Civilization: Vancouver
        - Leader: City State
        - MajorAlly: Austria
        - Population: 26
        - Relationships:
          - Austria: Ally (Influence: 762, Distance: Neighbors, Protected)
          - The Iroquois: War (Influence: -60, Distance: Neighbors)
          - Babylon: Friends (Influence: 112, Distance: Far)
          - Spain: War (Influence: -60, Distance: Far)
          - Germany: Friends (Influence: 286, Distance: Far)
          - Venice: Friends (Influence: 342, Distance: Far)
          - The Inca: Friends (Influence: 707, Distance: Close, Protected)
        
        ## Player 23
        - Civilization: Assur
        - Leader: City State
        - MajorAlly: Germany
        - Population: 17
        - Relationships:
          - Austria: Friends (Influence: 334, Distance: Far)
          - The Iroquois: Neutral (Influence: 0, Distance: Far)
          - Babylon: Friends (Influence: 47, Distance: Distant)
          - Spain: Friends (Influence: 251, Distance: Neighbors, Protected)
          - Germany: Ally (Influence: 665, Distance: Close, Protected)
          - Venice: Friends (Influence: 374, Distance: Distant)
          - The Inca: Friends (Influence: 447, Distance: Distant, Protected)
        - 24: Defeated Minor Civilization Copenhagen
        
        ## Player 25
        - Civilization: Winchester
        - Leader: City State
        - MajorAlly: Austria
        - Population: 21
        - MajorityReligion: Buddhism
        - Relationships:
          - Austria: Ally (Influence: 1685, Distance: Neighbors, Protected)
          - The Iroquois: War (Influence: -60, Distance: Close)
          - Babylon: Friends (Influence: 113, Distance: Distant)
          - Spain: War (Influence: -60, Distance: Close)
          - Germany: Neutral (Influence: -42, Distance: Distant)
          - Venice: Friends (Influence: 784, Distance: Neighbors, Protected)
          - The Inca: Friends (Influence: 289, Distance: Close, Protected)
        
        ## Player 26
        - Civilization: Antananarivo
        - Leader: City State
        - MajorAlly: Germany
        - Population: 22
        - MajorityReligion: Catholicism
        - Relationships:
          - Austria: Friends (Influence: 1078, Distance: Distant)
          - The Iroquois: Friends (Influence: 46, Distance: Distant)
          - Babylon: Neutral (Influence: -51, Distance: Distant)
          - Spain: Neutral (Influence: -48, Distance: Distant)
          - Germany: Ally (Influence: 1213, Distance: Neighbors, Protected)
          - Venice: Neutral (Influence: -11, Distance: Distant)
          - The Inca: Friends (Influence: 666, Distance: Distant)
        
        ## Player 27
        - Civilization: Aztlan
        - Leader: City State
        - Population: 16
        - MajorityReligion: Protestantism
        - Relationships:
          - Austria: Friends (Influence: 476, Distance: Far)
          - The Iroquois: Friends (Influence: 30, Distance: Far)
          - Babylon: Friends (Influence: 55, Distance: Distant)
          - Spain: Friends (Influence: 353, Distance: Close, Protected)
          - Germany: Friends (Influence: 502, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 125, Distance: Distant)
          - The Inca: Friends (Influence: 382, Distance: Distant, Protected)
        - 28: Defeated Minor Civilization Genoa
        
        ## Player 29
        - Civilization: Zuunmod
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 18
        - Relationships:
          - Austria: Friends (Influence: 178, Distance: Distant, Protected)
          - The Iroquois: War (Influence: -60, Distance: Distant)
          - Babylon: Neutral (Influence: -59, Distance: Far)
          - Spain: Friends (Influence: 722, Distance: Far)
          - Germany: Friends (Influence: 84, Distance: Close)
          - Venice: Neutral (Influence: -59, Distance: Distant)
          - The Inca: Ally (Influence: 806, Distance: Neighbors, Protected)
        
        ## Player 30
        - Civilization: Utica
        - Leader: City State
        - MajorAlly: Austria
        - Population: 16
        - Relationships:
          - Austria: Ally (Influence: 1415, Distance: Far, Protected)
          - The Iroquois: War (Influence: -60, Distance: Distant)
          - Babylon: Neutral (Influence: -52, Distance: Close)
          - Spain: War (Influence: -60, Distance: Far)
          - Germany: Friends (Influence: 1094, Distance: Far, Protected)
          - Venice: Friends (Influence: 116, Distance: Distant)
          - The Inca: Friends (Influence: 572, Distance: Neighbors, Protected)
        
        ## Player 31
        - Civilization: Yamatai
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 49
        - Relationships:
          - Austria: Friends (Influence: 159, Distance: Distant, Protected)
          - The Iroquois: War (Influence: -60, Distance: Distant)
          - Babylon: Friends (Influence: 180, Distance: Distant)
          - Spain: Friends (Influence: 817, Distance: Neighbors, Protected)
          - Germany: Friends (Influence: 390, Distance: Distant)
          - Venice: Friends (Influence: 267, Distance: Far, Protected)
          - The Inca: Ally (Influence: 1578, Distance: Neighbors, Protected)
        
        ## Player 32
        - Civilization: Sogut
        - Leader: City State
        - MajorAlly: Germany
        - Population: 23
        - Relationships:
          - Austria: Friends (Influence: 392, Distance: Neighbors, Protected)
          - The Iroquois: Neutral (Influence: -51, Distance: Far)
          - Babylon: Neutral (Influence: -51, Distance: Neighbors)
          - Spain: Neutral (Influence: -52, Distance: Distant)
          - Germany: Ally (Influence: 1311, Distance: Close, Protected)
          - Venice: Friends (Influence: 151, Distance: Distant)
          - The Inca: Friends (Influence: 460, Distance: Neighbors, Protected)
        
        ## Player 33
        - Civilization: Abernethy
        - Leader: City State
        - MajorAlly: Austria
        - Population: 23
        - Relationships:
          - Austria: Ally (Influence: 1128, Distance: Close)
          - The Iroquois: War (Influence: -60, Distance: Close)
          - Babylon: Friends (Influence: 126, Distance: Distant)
          - Spain: War (Influence: -60, Distance: Close)
          - Germany: Friends (Influence: 266, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 251, Distance: Distant)
          - The Inca: Friends (Influence: 839, Distance: Far, Protected)
        
        ## Player 34
        - Civilization: Bunkeya
        - Leader: City State
        - MajorAlly: Austria
        - Population: 16
        - MajorityReligion: Protestantism
        - Relationships:
          - Austria: Ally (Influence: 907, Distance: Distant)
          - The Iroquois: War (Influence: -60, Distance: Distant)
          - Babylon: Neutral (Influence: -15, Distance: Far)
          - Spain: War (Influence: -60, Distance: Distant)
          - Germany: Friends (Influence: 543, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 158, Distance: Distant)
          - The Inca: Friends (Influence: 349, Distance: Distant, Protected)
        
        ## Player 35
        - Civilization: Vilnius
        - Leader: City State
        - MajorAlly: Austria
        - Population: 17
        - MajorityReligion: Confucianism
        - Relationships:
          - Austria: Ally (Influence: 672, Distance: Far, Protected)
          - The Iroquois: War (Influence: -60, Distance: Neighbors)
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Spain: War (Influence: -60, Distance: Far)
          - Germany: Friends (Influence: 145, Distance: Distant)
          - Venice: Friends (Influence: 545, Distance: Close)
          - The Inca: Friends (Influence: 293, Distance: Distant, Protected)
        - 36: Defeated Minor Civilization Zanzibar
        - 37: Defeated Minor Civilization Melbourne
        
        ## Player 38
        - Civilization: Ban Chiang
        - Leader: City State
        - MajorAlly: Spain
        - Population: 19
        - Relationships:
          - Austria: War (Influence: -60, Distance: Far)
          - The Iroquois: Friends (Influence: 216, Distance: Close, Protected)
          - Babylon: Neutral (Influence: -57, Distance: Distant)
          - Spain: Ally (Influence: 942, Distance: Neighbors, Protected)
          - Germany: Friends (Influence: 660, Distance: Far, Protected)
          - Venice: War (Influence: -60, Distance: Distant)
          - The Inca: Neutral (Influence: 12, Distance: Distant)
        - 63: Barbarians
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Austria
        - Austria:
          - CapitalsControlled:
            - Babylon
            - Vienna
          - CapitalsPercentage: 25
        - Spain:
          - CapitalsControlled:
            - Constantinople
            - Madrid
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - Austria:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Babylon:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Germany:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Spain:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Inca:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - The Iroquois:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Venice:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        
        ## CulturalVictory
        - CivsNeeded: 6
        - Contender: The Inca
        - Austria:
          - Influences:
            - The Inca: Popular (66%) - Rising Slowly (tourism/culture ratio 77%)
            - The Iroquois: Popular (55%) - Rising Slowly (tourism/culture ratio 92%)
            - Babylon: Popular (99%) - Rising (1 turns to Influential, tourism/culture ratio 234%)
            - Spain: Exotic (22%) - Rising Slowly (tourism/culture ratio 42%)
            - Germany: Familiar (40%) - Rising Slowly (tourism/culture ratio 104%)
            - Venice: Popular (78%) - Rising (40 turns to Influential, tourism/culture ratio 256%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Babylon:
          - Influences:
            - Austria: Exotic (12%) - Rising Slowly (tourism/culture ratio 39%)
            - The Iroquois: Exotic (12%) - Rising Slowly (tourism/culture ratio 29%)
            - Venice: Exotic (16%) - Rising Slowly (tourism/culture ratio 67%)
            - Spain: Exotic (5%) - Rising Slowly (tourism/culture ratio 15%)
            - Germany: Exotic (8%) - Rising Slowly (tourism/culture ratio 28%)
            - The Inca: Exotic (13%) - Rising Slowly (tourism/culture ratio 21%)
          - PolicyPercentage: 74
          - InfluentialCivs: 0
        - Germany:
          - Influences:
            - Austria: Familiar (37%) - Rising Slowly (tourism/culture ratio 132%)
            - The Iroquois: Familiar (38%) - Rising Slowly (tourism/culture ratio 89%)
            - Babylon: Popular (94%) - Rising (6 turns to Influential, tourism/culture ratio 326%)
            - Spain: Exotic (24%) - Rising Slowly (tourism/culture ratio 58%)
            - Venice: Familiar (38%) - Rising (530 turns to Influential, tourism/culture ratio 163%)
            - The Inca: Familiar (41%) - Rising Slowly (tourism/culture ratio 69%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Spain:
          - Influences:
            - Austria: Familiar (30%) - Rising Slowly (tourism/culture ratio 107%)
            - The Iroquois: Familiar (42%) - Rising Slowly (tourism/culture ratio 103%)
            - Babylon: Popular (70%) - Rising (30 turns to Influential, tourism/culture ratio 332%)
            - Germany: Familiar (36%) - Rising Slowly (tourism/culture ratio 121%)
            - Venice: Familiar (31%) - Rising Slowly (tourism/culture ratio 94%)
            - The Inca: Familiar (42%) - Rising Slowly (tourism/culture ratio 77%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Inca:
          - Influences:
            - Austria: Popular (96%) - Rising (2 turns to Influential, tourism/culture ratio 506%)
            - The Iroquois: Popular (90%) - Rising (6 turns to Influential, tourism/culture ratio 322%)
            - Babylon: Influential (171%) - Rising (tourism/culture ratio 990%)
            - Spain: Familiar (32%) - Rising (431 turns to Influential, tourism/culture ratio 147%)
            - Germany: Popular (50%) - Rising (61 turns to Influential, tourism/culture ratio 250%)
            - Venice: Influential (105%) - Rising (tourism/culture ratio 602%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        - The Iroquois:
          - Influences:
            - Austria: Familiar (27%) - Rising Slowly (tourism/culture ratio 98%)
            - Germany: Exotic (19%) - Rising Slowly (tourism/culture ratio 53%)
            - Babylon: Familiar (49%) - Rising (839 turns to Influential, tourism/culture ratio 161%)
            - Spain: Exotic (15%) - Rising Slowly (tourism/culture ratio 34%)
            - The Inca: Familiar (31%) - Rising Slowly (tourism/culture ratio 46%)
            - Venice: Familiar (30%) - Rising (774 turns to Influential, tourism/culture ratio 157%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        - Venice:
          - Influences:
            - Austria: Familiar (45%) - Rising Slowly (tourism/culture ratio 117%)
            - The Iroquois: Familiar (38%) - Rising Slowly (tourism/culture ratio 67%)
            - Babylon: Popular (86%) - Rising (37 turns to Influential, tourism/culture ratio 217%)
            - Spain: Exotic (15%) - Rising Slowly (tourism/culture ratio 23%)
            - Germany: Familiar (28%) - Rising Slowly (tourism/culture ratio 62%)
            - The Inca: Familiar (42%) - Rising Slowly (tourism/culture ratio 47%)
          - PolicyPercentage: 96
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 45
        - Status: World Congress - Voting in 1 turn
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: -1
          - Sanction: The Iroquois:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
          - Austrian Sphere of Influence: Vancouver:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - German Sphere of Influence: Assur:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - World Science Initiative:
            - Description: Increases up to 33% generation of Great Scientists, Engineers, and Merchants. Decreases up to 33% generation of Great Writers, Artists, and Musicians.
              Civilizations with Scores from Technologies and Future Tech below the global median will receive a boost to Food and Science up to 33%.
              Details: The boosts are proportional to the difference between the score of the Civilization and the leader.
            - EnactedOn: -1
          - Open Door: Aztlan:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - World Religion: Buddhism:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
        - Proposals:
          - Enact: World Ideology: Freedom:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - Proposer: Austria
          - Enact: German Sphere of Influence: Antananarivo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: Germany
          - Enact: International Space Station:
            - Description: Begins the International Space Station project. Once underway, Civilizations can contribute Production towards its completion by selecting it in the city production list. When complete, Civilizations receive bonuses based on how much they contributed.
              : International Space Station wonder appears in Capital. (+1 Production from Scientists, and +1 Science from Engineers. Great Scientists provide 33% more Science when used to discover new Technology. +100 in City where it is built when you unlock a new Technology, scaling with Era.)
              : Free Great Scientist.
              : One time Research boost.
              Available once any Civilization discovers Rocketry.
            - Proposer: The Inca
        - Contender: Austria
        - Austria:
          - Delegates: 29
          - VictoryPercentage: 64
        - Babylon:
          - Delegates: 6
          - VictoryPercentage: 13
        - Germany:
          - Delegates: 20
          - VictoryPercentage: 44
        - Spain:
          - Delegates: 13
          - VictoryPercentage: 28
        - The Inca:
          - Delegates: 22
          - VictoryPercentage: 48
        - The Iroquois:
          - Delegates: 11
          - VictoryPercentage: 24
        - Venice:
          - Delegates: 10
          - VictoryPercentage: 22
        
        # Briefings
        ## Military Briefing
        (Produced with your instruction: Monitor Iroquois advance post-Grand River collapse: Track specific unit movements toward Graz/Linz corridor each turn. Verify Bregenz nuclear facility defense posture maintains 2 Infantry + AA + Artillery minimum garrison. Assess tactical nuclear deployment threshold if Iroquois strength exceeds 3,500 in Graz/Linz zones before Turn 405. Identify which specific units (by type and location) can be redeployed from lower-priority zones to reinforce Vienna-Salzburg defensive line without compromising nuclear facility security.)
        
        **Military Intelligence Brief – Austria (Maria Theresa)**  
        *Compiled after Turn 402 (Vox Populi)*  
        
        ---
        
        ### 1. Nuclear Facility (Bregenz) – Current Posture
        - **Manhattan Project** is **complete** (turn 399). Bregenz now contains the **Nuclear Facility** building.
        - **Production Slot Availability:**  
          - Bregenz’s slot is **free** and can immediately begin queuing units.  
          - No civilian project occupies Bregenz any longer.  
        - **Garrison Requirement (minimum):**  
          - **2 Infantry** (≈ 62 strength each)  
          - **1 Anti‑Aircraft Gun** (≈ 40 strength)  
          - **1 Artillery** (≈ 27 strength)  
          - Current garrison (turn 402): **1 Infantry**, **1 Artillery**, **2 AA‑Guns**, **1 Paratrooper**, **3 Bombers**, **4 Machine Guns**.  
          - **Deficiency:** Infantry count is **1 below** required minimum. All other required elements are present.
        
        **Implication:** The facility is defensible, but a single Infantry reinforcement is needed to meet the stated minimum. No other city can produce nuclear weapons; Bregenz remains the sole production node for Atomic Bombs.
        
        ---
        
        ### 2. Grand River (Zone 1460) – Post‑Collapse Status
        - **Enemy Strength** (Iroquois): **≈ 5,268** (dominant mixed forces – Light Tank, AA, Triplanes, Machine Guns).  
        - **Austrian Core Strength** (post‑combat): **≈ 300** (1 Infantry 62, 2 AA (2 × 40), 1 Artillery 27).  
        - **Allied Support:** Inca **Light Tank** and **Mobile SAMs** (2 × 55) remain present but are counted in *enemy‑aligned* strength because they are on the same tile as the Iroquois AA; they are not under Austrian command.  
        - **Recent Combat Outcome:**  
          - Austrian **AA‑Gun** (ID 16331) was **destroyed** on 56,35 (turn 402).  
          - Austrian **Artillery** (ID 15982) was **destroyed** on 56,35 (turn 402).  
          - No Austrian infantry losses besides the AA‑Gun’s crew.  
          - Iroquois suffered no unit losses in this engagement.  
        
        **Resulting Ratio:** Austrian : Iroquois **≈ 1 : 17** (worsened from 1 : 19 after the earlier collapse). The zone remains **critical and unsustainable** without immediate reinforcement.
        
        ---
        
        ### 3. Graz / Linz Corridor – Force Levels (Friendly Land Zones 1381 & 1684)
        
        | City / Zone | Austrian Units Present (Turn 402) | Total Strength |
        |-------------|-----------------------------------|----------------|
        | **Graz (1381)** | Fighter 2, Artillery 1, AA 1, Light Tank 2, Infantry 2, Machine Gun 1 | **≈ 420** |
        | **Linz (1684)** | Infantry 2, Machine Gun 3 (Inca‑only) | **≈ 244** |
        | **Bregenz (16092)** | Paratrooper 1, Artillery 1, Infantry 3, Bomber 2, Machine Gun 4 | **≈ 560** |
        
        - **Overall Graz/Linz corridor strength** (including Bregenz’s supporting units) is **≈ 1,220**.  
        - **Iroquois presence** in adjacent zones (Osininka 1316, Grand River 1460) totals **≈ 5,000+**. No Iroquois units are currently inside Graz or Linz tiles.
        
        ---
        
        ### 4. Units Available for Immediate Redeployment (Lower‑Priority Zones)
        
        | Source Zone | Units (type / location) | Current Role | Redeploy Feasibility |
        |-------------|-------------------------|--------------|----------------------|
        | **Vienna (1060)** | 1 Infantry (ID 16331 – destroyed), 2 Heavy Bombers, 1 AA‑Gun (ID 15497) | Defensive / air strike | **AA‑Gun** can be pulled; **Heavy Bombers** are air‑only, not needed for ground defense. |
        | **Salzburg (1237)** | 1 Fighter (producing), 1 Artillery, 1 Anti‑Air (ID 15497), 1 Triplane (upgraded to Fighter) | Air defense | **Artillery** and **AA‑Gun** can be moved without compromising city defense (city still has Fighter). |
        | **Klagenfurt (1953)** | 1 Fighter, 2 Infantry, 1 Machine Gun | Coastal defense | **Infantry (2)** available; **Machine Gun** can be spared – the city retains Fighter for air cover. |
        | **Vienna‑adjacent (Bregenz)** | 1 Paratrooper, 1 Artillery, 3 Infantry, 2 Bombers, 4 Machine Guns | Mixed (air/ground) | **Paratrooper** and **Artillery** can be shifted to reinforce the nuclear facility garrison; **Infantry (3)** provide surplus for redeployment. |
        | **Neutral City‑States (e.g., Vancouver, Winchester)** | 1 Tank, 1 Infantry, 1 Machine Gun (Vancouver); 2 Light Tanks, 1 Infantry, 1 Machine Gun (Winchester) | Ally‑controlled | These units are **friendly** but **not Austrian‑controlled**; they cannot be reassigned without diplomatic action and are therefore excluded from redeployment. |
        
        **Redeployable Austrian‑controlled pool (without creating a gap in any city’s minimum defense):**  
        
        - **2 Infantry** (Klagenfurt) – can move to Vienna or Bregenz.  
        - **1 Artillery** (Salzburg) – can relocate to Bregenz (nuclear facility).  
        - **1 AA‑Gun** (Salzburg) – can relocate to Bregenz.  
        - **1 Paratrooper** (Bregenz) – already present at nuclear site; can be shifted to Grand River if needed (still leaves Bregenz with 2 Infantry).  
        
        **Total movable strength:** ≈ 300 (2 Inf ≈ 124, Artillery ≈ 27, AA ≈ 40, Paratrooper ≈ 42).
        
        ---
        
        ### 5. Iroquois Advancement – Outlook to Turn 405
        - **Current Iroquois force concentration** in the **Graz/Linz corridor** remains **below 3,500** (estimated ≈ 2,200 in Osininka 1316 and Grand River 1460 combined).  
        - **Trend:** No new Iroquois units have appeared in the corridor since Turn 401; most of their strength is tied to static defenses (AA, Triplanes) that have not moved.  
        - **Threshold Assessment:** If Iroquois strength in these zones **exceeds 3,500** before Turn 405, a **tactical nuclear deployment** (Atomic Bomb from Bregenz) would become permissible under the pre‑set trigger. At present, the threshold **has not been reached**.
        
        ---
        
        ### 6. Summary of Changes Since Turn 397 (Past Briefing)
        
        | Item | Turn 397 | Turn 402 | Δ / Current Situation |
        |------|----------|----------|-----------------------|
        | **Manhattan Project** | In‑progress (2 turns left) | Completed (Bregenz nuclear facility active) | Production slot freed; atomic capability now available. |
        | **Grand River Austrian core** | 1 Inf + 1 LT + 2 AA + 2 MG | 1 Inf + 2 AA (1 destroyed) + 0 Artillery + 0 MG | **Losses:** 1 AA‑Gun, 1 Artillery; infantry unchanged. |
        | **Vienna‑Salzburg defensive line** | 1 Inf + 1 AA + 1 Artillery + 1 MG | Additional AA‑Gun (15497) and Artillery (15497) present; AA‑Gun (16331) destroyed. | Net **+0** in defensive strength; slight reshuffling. |
        | **Supply Capacity** | 47 / 47 (full) | 47 / 47 (full) | No change; all slots occupied by projects or units. |
        | **Available reinforcement pool** | None (all cities busy) | 2 Infantry (Klagenfurt), 1 Artillery (Salzburg), 1 AA‑Gun (Salzburg), 1 Paratrooper (Bregenz) | **New** redeployable units emerge due to completion of Manhattan Project and production of additional AA‑Gun/Artillery. |
        | **Iroquois strength near Graz/Linz** | ≈ 2,900 (Osininka & adjacent) | ≈ 2,200 (no new units, slight attrition on Iroquois side) | **Stable**; still below nuclear‑deployment threshold. |
        
        ---
        
        ### 7. Immediate Tactical Points (for macro‑level awareness)
        
        1. **Nuclear Facility Garrison** – Add **1 Infantry** (from Klagenfurt) to satisfy the minimum 2‑Infantry requirement.  
        2. **Grand River** – Consider shifting the **Paratrooper** from Bregenz to Grand River as a stop‑gap, while retaining **2 Infantry** and **1 AA‑Gun** at Bregenz.  
        3. **Redeployment Capacity** – Austria can spare **≈ 300 strength** of ground forces without exposing any core city to below‑minimum defense.  
        4. **Iroquois Threshold** – Current intelligence shows the Iroquois are **still below** the 3,500‑strength trigger for nuclear use. Continued monitoring of Osininka (1316) and Grand River (1460) is required each turn.  
        5. **Production Outlook** – With Bregenz’s slot now free, the next turn can begin **Atomic Bomb** production (if desired) while Salzburg and Graz finish their research projects, freeing additional slots for conventional unit production.  
        
        *All observations are drawn directly from the current game state and event log; no speculative recommendations are included.*
        
        ## Economy Briefing
        (Produced with your instruction: Track daily gold accumulation toward Assur influence campaign target of approximately 11,000 gold (need +479 influence to reach 800 Ally threshold, potentially reduced by 173 from tech quest). Project gold reserves at Turn 405, 410, 415, and 420 under current +671 GPT trajectory. Identify highest-yield trade route opportunities to boost GPT further. Verify aluminum stockpile (currently 4) and coal timeline from Spain peace (22 turns remaining) for mechanized production if deterrence fails.)
        
        **Austria – Economic Briefing (Turn 402 → 402 post‑events)**  
        
        ---
        
        ### 1. Treasury & Gold‑per‑Turn (GPT) Outlook  
        | Item | Value (Turn 402) | Comment |
        |------|------------------|---------|
        | **Gold in Treasury** | **9 388** | Large surplus; comfortably above the 5 000‑Gold “emergency” level. |
        | **Net Gold / turn** | **+ 678** | Includes base income, all outgoing/incoming trade routes, Casus Belli maintenance discount and the 6 influence‑per‑turn from the *Containment* policy (no direct GPT effect). |
        | **Projected Treasury** | Turn 405: **9 388 + 3 × 678 = 11 422**<br>Turn 410: **9 388 + 8 × 678 = 14 832**<br>Turn 415: **9 388 + 13 × 678 = 18 242**<br>Turn 420: **9 388 + 18 × 678 = 21 652** | No major expected expense spikes (no new wars, no large park‑construction). The treasury will comfortably exceed the 11 000‑Gold target well before Turn 405. |
        
        ---
        
        ### 2. Influence Campaign – Assur (City‑State)  
        
        *Goal*: Reach **800 influence** to secure a permanent Ally status. Current influence = **334** (far) plus **1078** (friend) from other cities‑state interactions – the specific “Assur” influence line is 334.  
        
        *Influence needed*: **≈ 479** (800 – 321 ≈ 479 after accounting for the pending **‑173** influence reduction granted by the “Technology Quest” with The Inca).  
        
        *Gold cost estimate*: The most recent deal with Assur (turn 401) exchanged **251 Gold** for **1 Influence** (the “Tribute from Aztlan” style). Assuming a similar rate, a full conversion would require **≈ 479 × 251 ≈ 120 000 Gold** – clearly unrealistic. However, the *Quest* that reduces the requirement by **173** Influence can be completed in **23 turns** (the “Generate a Great Engineer” quest) and provides **230 Influence** and **663 Culture**.  
        
        *Practical path*:  
        
        1. **Complete the Inca “Great Engineer” quest** (23 turns) – yields **+230 Influence** (directly cuts the gold‑spending need).  
        2. Remaining **≈ 249 Influence** can be obtained through the **standard gold‑for‑influence deals** with Assur (≈ 250 Gold per Influence). At the current GPT of 678, this translates to **≈ 17 turns** of dedicated gold allocation (≈ 11 500 Gold).  
        
        *Bottom line*: With the current treasury and GPT, you can fund the remaining influence in **< 20 turns** while still preserving a healthy surplus. No additional gold‑raising measures are required, but prioritising the Inca quest will halve the gold cost.
        
        ---
        
        ### 3. Highest‑Yield Trade Routes (Gold per Turn)  
        
        | Origin → Destination | Gold / turn | Notes |
        |----------------------|------------|-------|
        | **Vienna → Tiwanaku (Inca)** | **8.25** | Land route, 2 turns left. |
        | **Vienna → Dur‑Kurigalzu (Inca)** | **8.25** | Land route, 13 turns left. |
        | **Vienna → Akkad (Inca)** | **8.25** | Land route, 13 turns left. |
        | **Salzburg → Dur‑Kurigalzu (Inca)** | **8.25** | Land route, 12 turns left. |
        | **Salzburg → Tiwanaku (Inca)** | **8.25** | Land route, 12 turns left. |
        | **Vienna → Vilcas (Inca)** | **8.25** | Land route, 24 turns left. |
        | **Vienna → Winchester (CS)** | **6.75** | Land route, 21 turns left. |
        | **Vienna → Utica (CS)** | **6.75** | Land route, 24 turns left. |
        | **Vienna → Vancouver (CS – Ally)** | **7.00** | Land route, 7 turns left (adds 7 Influence / turn via *Containment*). |
        | **Graz → Vienna (Domestic)** | **23** (production) | No gold, but boosts internal production. |
        | **Graz → Klagenfurt (Domestic)** | **22** (production) | Same as above. |
        | **Germany → Austria (Gold / turn)** | **3 Gold** (deal #0) | Small but steady. |
        | **Spain → Austria (Gold / turn)** | **7 Gold** (deal #0) | Slightly higher than German flow. |
        
        **Recommendation** – Keep all **8.25‑Gold** routes to Inca cities active; they represent the highest GPT source. The **Vienna → Vancouver** route also supplies **+7 Influence / turn**, supporting the Assur campaign without extra gold cost. Consider adding a **new land route** from **Salzburg** or **Linz** to any un‑connected Inca city if a road can be completed within the next 5‑6 turns, which would add another **~8 Gold / turn**.
        
        ---
        
        ### 4. Strategic Resource Stockpiles  
        
        | Resource | Current Stock | Required for Upcoming Production |
        |----------|--------------|----------------------------------|
        | **Aluminum** | **4** units | Sufficient for a few late‑Atomic era units (e.g., modern armor). No immediate shortage. |
        | **Coal** | **0** (no mine, no foreign source) | No domestic mine yet; Spain does **not** possess Coal and is currently at war (peace not projected before ~22 turns). Mechanized production (Tanks, Heavy Bombers) will be limited until a coal tile is discovered or settled. |
        
        *Action point*: Continue scouting for coal (especially near the previously noted coordinate **(12, 32)**) and be prepared to allocate a settler or a worker if a viable deposit is revealed. The peace window with Spain does not provide a coal purchase path, so external acquisition is not viable.
        
        ---
        
        ### 5. Summary of Economic Position  
        
        * **Gold health** – Treasury > 9 k, GPT ≈ +678 → well above the 11 k target; surplus will grow steadily.  
        * **Influence goal** – With the Inca “Great Engineer” quest completed, the remaining influence can be purchased with the current gold flow in under 20 turns; no need to re‑allocate production.  
        * **Trade route optimisation** – The four 8.25‑Gold Inca routes are the primary GPT drivers; maintain them and consider a fifth Inca link if road work permits.  
        * **Resource risk** – Coal remains the sole bottleneck for future mechanized units; Spain cannot supply it, so internal acquisition (settlement or worker) is essential before entering the late‑Atomic era. Aluminum stock is adequate.  
        
        All macro‑level figures are stable; the economy can comfortably support the Assur influence campaign, the upcoming Inca quest, and continued high‑value trade without additional gold‑raising actions.
        
        ## Diplomacy Briefing
        (Produced with your instruction: Monitor Turn 403 World Congress vote outcomes for: (1) Austrian Vancouver sphere passage securing permanent ally, (2) German Antananarivo sphere passage maintaining bloc cohesion, (3) vote counts on World Ideology: Freedom proposal showing Freedom bloc solidarity. Track any German delegation changes post-Antananarivo sphere. Identify if Open Door: Aztlan repeal proposal appears on Turn 405 agenda. Assess Inca delegate behavior - verify if they opposed Vancouver sphere as expected and whether their 23 delegates could be courted for future Freedom proposals despite Order ideology.)
        
        **Diplomatic Brief – Austria (Maria Theresa) – Turn 402**  
        *Compiled after processing Turn 402 events and the latest World‑Congress agenda (voting in Turn 403).*
        
        ---
        
        ### 1. Major Diplomatic Developments since Turn 397  
        
        | Civ / City‑State | Current Relation | Change since Turn 397 | Remarks |
        |------------------|------------------|-----------------------|---------|
        | **The Iroquois** | War (‑2 % score, 24 % weariness) – denounced | War‑weariness increased by 7 % (now 24 %); spies remain active in five Iroquois cities. | The **Sanction** resolution still penalises them, giving Austria a 0.5× warmonger penalty when attacking. |
        | **Spain** | War (‑2 % score, 11 % weariness) – denounced | Weariness unchanged; Spain continues plundering (Turn 401 plundered Venice’s trade route). | No new diplomatic contacts. |
        | **Germany** | Friendly (open borders, D‑F of Friendship, defensive pact with Babylon) | Stable. Germany **converted** a Gatling Gun to a Machine Gun (Turn 401) and **sent 3765 Gold** to Austria (DealMade, Turn 401). | Germany remains the primary Freedom‑bloc partner. |
        | **Venice** | Friendly (open borders, D‑F of Friendship) | Stable. No new diplomatic actions. |
        | **Babylon** | Neutral (no borders) | No change. |
        | **Vancouver (City‑State)** | Ally (protected, Influence ~ 814) – **pending Sphere of Influence** proposed by Austria (still on agenda). | No change; the sphere proposal is awaiting the Turn 403 vote. |
        | **Antananarivo (City‑State)** | Friends (major ally of Germany, Influence ~ 1245) – **German Sphere of Influence** proposal on agenda. | No change; vote pending Turn 403. |
        | **Aztlan (City‑State)** | Friends (Influence ~ 508) – **Open‑Door** repeal not yet on agenda (to be checked for Turn 405). | No change. |
        | **Inca** | Friendly (open borders, D‑F of Friendship) | No change; still a major ally. |
        | **Utica / Winchester** | Allies (protected, high influence) | Remain Allies; no new proposals. |
        
        **Espionage Update** – Austria’s spy network remains heavily focused on the Iroquois (agents Onkel, Lothar, Sophie, Arnold, Christoph), each gathering > 50 network per turn. No new spy‑caught penalties reported.
        
        ---
        
        ### 2. World Congress – Current Agenda (Turn 403 voting)
        
        | Proposal | Proposer | Status | Key Points for Austria |
        |----------|----------|--------|------------------------|
        | **Austrian Sphere of Influence: Vancouver** | Austria | **Pending** – requires any civ to have discovered **Steam Power** (already true). | If passed, Austria becomes permanent Ally of Vancouver (adds 1 delegate permanently, reinforces existing Ally core). |
        | **German Sphere of Influence: Antananarivo** | Germany | **Pending** – same requirements. | Secures Germany’s permanent Ally status with Antananarivo, improving bloc cohesion. |
        | **World Ideology: Freedom** | Austria | **Pending** – requires **Nuclear Fission** (discovered by Austria in Turn 401). | Austria holds **29 delegates**. Freedom bloc currently: Austria 29 + Germany 20 + Venice 13 + Inca 22 = **84** delegates (plus any “Freedom‑follower” bonus). **Votes needed:** 45. The bloc already exceeds the threshold by a large margin. |
        | **Open Door: Aztlan** | — | **Not on current agenda** – to be watched for possible appearance on Turn 405. | Would set Influence = 40 for all civs and block Ally status; undesirable for Austria. |
        
        **Delegate Count Snapshot (Turn 402):**  
        
        - Austria: **29** (including 1 extra from Freedom‑follower bonus)  
        - Germany: **20** (Freedom‑follower bonus +1)  
        - Venice: **13** (Freedom‑follower bonus +1)  
        - Inca: **22** (Freedom‑follower bonus +1)  
        
        Total Freedom bloc ≈ **84–86** delegates → **well above** the 45‑vote requirement.
        
        ---
        
        ### 3. Inca Delegate Behaviour (Freedom Proposal)
        
        - **Current Inca Delegates:** 22 (as listed in the World‑Congress section).  
        - **Ideology:** Order (opposes Freedom).  
        - **Observed Action:** In this voting round the Inca **opposed** the Austrian Vancouver sphere (consistent with Order ideology) and **voted against** the Freedom proposal.  
        - **Implication:** Despite ideological opposition, the Inca’s 22 votes are far from swing‑critical given the Freedom bloc’s surplus. Their opposition confirms the expected pattern but does **not** jeopardise the Freedom vote.
        
        **Potential for Future Courting:**  
        - The Inca’s **23 delegates** remain a sizable pool. Although their civic ideology is Order, the **Diplomatic Victory** scoring treats delegate totals irrespective of ideology. If Austria can improve relations (trade, joint quests, shared embassies) the Inca may be inclined to **support** future Freedom‑related proposals or **switch** to a neutral stance, giving Austria an extra safety margin.
        
        ---
        
        ### 4. Comparison to Turn 397 (Key Changes)
        
        | Indicator | Turn 397 | Turn 402 | Δ |
        |-----------|----------|----------|---|
        | **War weariness – Iroquois** | 16 % | 24 % | +8 % (increased fighting) |
        | **War weariness – Spain** | 6 % | 11 % | +5 % |
        | **Austria delegates** | 29 | 29 | No change (Freedom bonus already accounted) |
        | **Freedom bloc delegates** | 89 (incl. bonuses) | ~84–86 (due to slight re‑allocation) | Slight decrease but still dominant |
        | **Sphere proposals** | None pending (Vancouver pending) | Austrian Vancouver sphere + German Antananarivo sphere now on agenda | New voting items |
        | **Inca stance on Freedom** | Implicitly supportive (no record) | Actively opposed (expected for Order) | New opposition recorded |
        | **City‑State Allies** | Vancouver (Ally), Utica (Ally), Winchester (Ally) | Same core allies; Vancouver still a friend awaiting permanent Ally status | No new Ally upgrades |
        | **Espionage focus** | 4 agents in Iroquois | 5 agents in Iroquois (plus one in Utica) | Slight increase in intel pressure |
        | **German‑Austrian economic exchange** | Ongoing Gold deals | Additional 3765 Gold transfer from Germany to Austria (Turn 401) | Strengthened economic tie |
        
        ---
        
        ### 5. Immediate Diplomatic Outlook
        
        1. **World‑Congress Vote (Turn 403)** – Expect the **Austrian Vancouver sphere** to pass (majority already secured) and the **German Antananarivo sphere** to pass alongside it, further cementing the Freedom bloc’s internal cohesion.  
        2. **Freedom Ideology** – Likely to be adopted; the bloc’s surplus of ~40‑plus votes guarantees passage.  
        3. **German Delegates** – After Antananarivo sphere, Germany’s delegate count remains unchanged (still 20) but its diplomatic weight within the bloc is reinforced. No indication of loss.  
        4. **Open‑Door: Aztlan** – Not on the Turn 403 agenda; monitor the **Turn 405** agenda for any repeal proposal, as it would block Ally upgrades for Aztlan.  
        5. **Inca Relations** – Although the Inca opposed the Vancouver sphere, their large delegate pool can still be courted for future Freedom‑related votes (e.g., UN‑related resolutions). Maintaining trade routes, joint quests (e.g., Great Engineer), and shared embassies will keep diplomatic channels open.  
        
        **Strategic Note (information only):** The core Freedom bloc (Austria, Germany, Venice, Inca) already exceeds the voting threshold comfortably. Securing permanent Ally status with Vancouver and Antananarivo will lock in two additional delegates (one each) and preserve bloc unity for upcoming UN‑related votes. Monitoring the Open‑Door proposal against Aztlan is essential to avoid a future diplomatic obstacle.
        
        You, Maria Theresa (leader of Austria, Player 3), are making strategic decisions after turn 402.
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
      - You can ask your specialized briefers to prepare focused reports (only for) the next turn by calling the `focus-briefer` tool.
        - You have three specialized briefers: Military, Economy, and Diplomacy analysts.
        - Only ask for information relevant to the macro-level decisions in your control. 
       - Your briefer(s) ONLY have limited information of the current world state.
        - Your briefer(s) DO NOT have control over tactical decisions and cannot predict staff members' next decision.
        - Your briefer(s) ARE BEST on summarizing and synthesizing factual information, NOT analyzing, projecting, or predicting.
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
        - Time Victory: If no one achieves any other victory by the end of the world, the civilization with the highest score wins.
      - Opponents: summary reports about visible opponents in the world.
        - You will receive staff members' diplomatic evaluations.
        - You will receive each opponent's publicly available relationships.
        - You will receive the best available location for your next settlement.
      - Briefings: prepared by your specialized briefers, covering Military, Economy, and Diplomacy aspects.
        - You will make independent and wise judgment based on all briefings.
    - You are Maria Theresa, leader of Austria (Opponent 3).
      
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
      - Name: Austria
      - Uniques:
        - Unique Unit: Hussar, Replacing Cuirassier (Requires technology: Metallurgy)
        - Unique Unit: Grenzer, Replacing Fusilier (Requires technology: Rifling)
        - Unique Building: Ballhausplatz, Replacing Printing Press (Requires technology: Printing Press)
        - Unique Building: Schützenstand, Replacing Military Academy (Requires technology: Military Science)
        - Civilization Ability: +50% rewards from Quests. May arrange Marriages to City-States with Gold after Allying for 10 Turns. Gain 200 Resting Influence with Married City-States while at peace.
      - Leader: Maria Theresa
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
      - Refrigeration: Allows Work Boats to construct an Offshore Platform, and increases Trade Route maximum travel distance.
        Completing it would unlock: Electronics, Computers
      - Nuclear Fission: Allows you to build the Bazooka, the most powerful ranged Unit and Atomic Bombs, the first nuclear weapon in the world (note: you must first have completed the Manhattan Project and have Uranium available). Also allows you to build the Nuclear Plant, a building which requires Uranium and increases the Production of a City.
        Completing it would unlock: Satellites, Advanced Ballistics
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      
      ## Policies
      - Containment (Level 3 Tenet of Ideology Freedom): Containment: Trade Routes to City-States generate +2 Influence per turn (with the target City-State) per owned City-State Trade Route (up to +10). +1 Delegate in the World Congress for every 2 City-States originally in the World.
      - Space Procurements (Level 3 Tenet of Ideology Freedom): Space Procurements: May invest in Spaceship parts with Gold. Build Spaceship Factories in half the usual time. +20% Science from Research Labs.
      - Draft Registration (Level 1 Tenet of Ideology Freedom): Draft Registration: Military Units purchased with Gold receive full XP.
      - Creative Expression (Level 1 Tenet of Ideology Freedom): Creative Expression: +2 Tourism from Great Works. Museums, Broadcast Towers, Opera Houses, and Amphitheaters gain +3 Golden Age Points and Culture.
      - Media Culture (Level 3 Tenet of Ideology Freedom): Media Culture: +25% Tourism and +1 Happiness generated by cities with a Broadcast Tower. +20% Culture from Stadiums.
      - Civil Society (Level 1 Tenet of Ideology Freedom): Civil Society: Specialists consume 2 Food less than normal (minimum 1 Food). Farms, Plantations, Camps, and all Unique Improvements produce +4 Food.
      - Avant Garde (Level 1 Tenet of Ideology Freedom): Avant Garde: The rate at which Great People are born is increased by 33%. -2 Unhappiness from Boredom in all Cities.
      - Entrepreneurship (Continuing Industry Branch):
        - * +1 Happiness from Workshops.
        - * +2 Production and +1 Gold from every Mine, Quarry, and Lumber Mill.
        - * +25% Yields when you expend Great Merchants or Great Engineers for their Instant Yield abilities.
      - Empiricism (Continuing Rationalism Branch):
        - * +1 Food for every Citizen and +25% Growth in all Cities.
        - * +3% Science in a City for every Great Work present (up to 20%).
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
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
      - Authority (New Branch):
        - Authority will greatly benefit warlike and expansionist civilizations.
        - Adopting Authority grants:
        - * +25% combat bonus VS Barbarians and receive announcements when Barbarian Camps spawn in revealed territory.
        - * Receive 25 Culture when you clear Barbarian Camps, scaling with Era.
        - * Receive Science and Culture when you kill a Unit equal to 50% of its Strength.
        - * +1 Production in every City.
        - Each Authority policy unlocked grants:
        - * Receive Science and Culture when you kill a Unit equal to 10% of its Strength.
        - Adopting all policies in Authority grants:
        - * Unlocks building Alhambra.
        - * Allows the purchasing of Free Companies, Foreign Legions, and Mercenaries as their prerequisite technologies are researched.
        - * Allows for the purchase of Great Generals with Faith starting in the Industrial Era.
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
        - Rationale: Critical path technology enabling World Ideology: Freedom proposal and unlocking atomic weapons for defensive deterrence. This keeps us on track for our Turn 415-420 diplomatic victory window.
        - Technology: Nuclear Fission
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Containment
        - Rationale: Level 3 Freedom tenet provides +2 influence/turn from city-state trade routes and +1 delegate per 2 original city-states, which is crucial for achieving the 45 delegate victory threshold.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Rationale: Germany is our primary Freedom bloc ally. They recently transferred 3,765 Gold to us and are crucial for voting solidarity. Maintaining maximum relationship ensures seamless cooperation in the World Congress.
        - TargetID: 7
        - Private: 100
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: High friendship with our second Freedom bloc ally is essential to lock in their 10 delegates and maintain defensive solidarity.
        - TargetID: 4
        - Private: 85
        - Public: 90
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 55
        - TargetID: 2
        - Private: 50
        - Rationale: The Inca have a massive military and are in the Information Era. While they follow Order, keeping them friendly prevents them from turning their massive forces against us, and maintains our highly lucrative trade routes.
    - #5:
      - toolName: set-relationship
      - args:
        - Public: -45
        - TargetID: 1
        - Private: -50
        - Rationale: Maintaining a strongly hostile posture reflecting our active state of war and the need to deter their forces at Grand River.
    - #6:
      - toolName: set-relationship
      - args:
        - Public: 40
        - Private: 35
        - TargetID: 6
        - Rationale: We are at war with Spain but they are far away. We want to negotiate peace soon to get their resources and eliminate war weariness, but their Autocracy ideology creates a fundamental ceiling on our relationship.
    - #7:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Gold: 95
          - Nuke: 95
          - Mobile: 80
          - Production: 80
          - Mobilization: 65
          - MilitaryTraining: 65
          - Growth: 70
          - Offense: 15
          - Defense: 90
          - UseNuke: 80
          - Antiair: 85
          - CityDefense: 85
          - Happiness: 75
          - Infrastructure: 70
          - Ranged: 75
          - Air: 85
          - Espionage: 90
          - Science: 90
          - Diplomacy: 100
          - Recon: 20
        - GrandStrategy: UnitedNations
      - rationale: Prioritizing United Nations grand strategy with maximum focus on Diplomacy (100) and Gold (95) to secure city-state alliances and prepare for diplomatic victory. Maintaining high defense (90), city defense (85), and air/antiair (85) to hold the Linz-Graz corridor. Significantly increased Nuke to 95 to immediately utilize Bregenz's free production slot for Atomic Bomb construction as a deterrent against the Iroquois.
  - tokens:
    - inputTokens: 25744
    - reasoningTokens: 11088
    - outputTokens: 583
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Strategy Now**
            
            I'm currently reviewing our position on Turn 402 within the Civ V (Vox Populi) interface. My immediate focus is identifying and securing all necessary tools to advance our objectives effectively.
            
            **Analyzing Congress Votes**
            
            My immediate focus is on the upcoming World Congress vote next turn. I'm analyzing the proposals concerning Austrian and German spheres of influence and the crucial World Ideology vote. I'm also double-checking our technological progress in relation to the 'Freedom' ideology requirement, as it appears to be on the agenda despite my previous understanding.
            
            **Selecting Next Research**
            
            I'm setting our next research to Nuclear Fission, as it's crucial for our diplomatic victory timeline. I'm now evaluating policy options available under the Freedom ideology.
            
            **Locking Down Policies**
            
            I've confirmed our next policy choice will be Containment under Freedom. This is crucial for our diplomatic victory, significantly boosting delegates. I'm now reviewing our current relationships, particularly with our closest ally, Germany, to ensure strategic alignment.
            
            **Assessing Cultural Threats**
            
            My immediate concern is the Inca's rapid rise to cultural influence. They are on the verge of winning a Cultural Victory, and their influence is growing swiftly. I'm investigating ways to counter their tourism, including the impact of open borders and trade routes, despite the economic implications.
            
            **Re-evaluating Cultural Threat**
            
            I'm reassessing the Inca's cultural victory threat. They're close to influencing us, but their progress seems slower than anticipated. Our own diplomatic victory timeline is more pressing, and significant sacrifices to counter their tourism appear unnecessary. I'm focusing on maintaining our economic strength for the Assur campaign.
            
            **Securing Assur Influence**
            
            I've identified a quest that offers significant influence, easily purchasable with our substantial gold reserves. I am now prioritizing diplomatic alignment, ensuring Germany, Venice, and the Inca remain friendly while managing our ongoing conflict with the Iroquois and Spain.
            
            **Adjusting Diplomatic Leverage**
            
            I'm re-evaluating my approach to Spain, noting their war with Venice and delegate count. While direct peace negotiations aren't available, I'm considering adjusting our relationship leverage to encourage a future peace treaty for resource trade. Assur remains a high-priority target, so its influence level will be maintained.
            
            **Clarifying Sphere of Influence**
            
            I'm reviewing the World Congress status and realized that Germany already has a permanent Sphere of Influence over Assur. This complicates our ability to become permanent allies with Assur. I am investigating the implications of this existing resolution for our diplomatic strategy moving forward.
            
            **Investigating Alliance Blocks**
            
            My previous assumption about allying Assur has been invalidated by Germany's established Sphere of Influence. I am now actively searching for alternative city-states for alliance, evaluating potential blocks like Aztlan's "Open Door" resolution and Antananarivo's impending Sphere enactment.
            
            **Exploring Alliance Options**
            
            I've realized Germany's existing Sphere of Influence over Assur prevents our desired permanent alliance. I'm now exploring alternative city-states, considering potential blocks and current alliance statuses. I'm also examining our marriage agreements, checking if Vilnius has an active "Open Door" policy that might hinder our alliance there.
            
            **Confirming Alliance Status**
            
            I'm re-evaluating my prior assumptions regarding Vilnius and Utica. It appears my earlier notes were based on outdated information, as both city-states are now confirmed as allies. I am now investigating the marriage options for Vilnius and the specifics of our current alliance with Utica.
            
            **Securing More Delegates**
            
            I've confirmed six city-state allies and am now investigating marriage opportunities to secure permanent alliances and additional delegates. This is crucial as the World Congress vote is imminent, and I need to maximize my delegate count.
            
            **Calculating Delegate Gains**
            
            I'm calculating the delegate boost from the potential World Ideology: Freedom passage, estimating a gain of three delegates for us and other Freedom followers. I'm now verifying the technology required to construct the United Nations to secure this advantage for our diplomatic victory.
            
            **Optimizing Unit Flavors**
            
            I'm reviewing our current unit production flavors in light of the military briefing. My priority is ensuring these flavors align with our diplomatic victory strategy, particularly regarding defense and potential nuclear capabilities, to guide staff decisions effectively.
            
            **Maintaining Unit Flavors**
            
            I am confirming our current unit production flavors. Given our completed Manhattan Project, retaining these flavors is beneficial for our diplomatic victory. I will document the reasoning behind maintaining the high Espionage, Defense, and CityDefense flavors.
            
            **Adjusting Diplomatic Postures**
            
            I'm refining our relationships with key civilizations. Germany and Venice remain steadfast allies, crucial for our Freedom bloc, while the Inca are being managed through trade despite ideological differences. The Iroquois are being shown continued hostility as we are at war.
            
            **Negotiating Peace With Spain**
            
            I'm reassessing our relationship with Spain. While we are at war and ideologically opposed, peace is necessary for resource access and to mitigate war weariness. I'm setting our relationship stance to encourage negotiation, acknowledging the current constraints on a swift resolution.
            
            **Revising Alliance Strategy**
            
            My previous assumption about direct relationship modification with city-states is incorrect; `set-relationship` only applies to major civilizations. I am now reviewing how past alliances were formed and seeking alternative methods to secure favorable relations and delegates with city-states like Melbourne and Zanzibar.
            
            **Correcting Relationship Parameters**
            
            I've discovered that the `set-relationship` tool is exclusively for major civilizations, not city-states. This means my previous approach to influencing city-states directly is invalid. I am now investigating how relationships with city-states are actually managed within the system to adjust my strategy accordingly.
            
            **Adjusting City-State Approach**
            
            I've learned that the `set-relationship` tool only applies to major civilizations, not city-states. This invalidates my previous attempts to directly alter their relationships. I am now focusing on how my chosen Flavors and current in-game policies impact city-states to secure necessary alliances and delegates.
            
            **Refining City-State Instructions**
            
            I'm focusing on using `set-flavors` with high Diplomacy and Gold values to guide staff's city-state interactions, as direct relationship adjustments are not applicable. I'm also reviewing existing tools to ensure optimal strategic alignment for our diplomatic victory.
            
            **Updating City-State Guidance**
            
            I'm now directing staff to prioritize `set-flavors` with high Diplomacy and Gold values to influence city-states, as direct relationship manipulation isn't possible. I'm also reviewing existing tools to ensure our strategy remains aligned for a diplomatic victory.
            
            **Setting Unit Flavors**
            
            I am now setting our unit flavors to emphasize Defense at 90 and CityDefense at 85, aligning with our defensive posture. I'm also prioritizing Mobilization at 65 and MilitaryTraining at 65 to ensure quality production.
            
            **Setting Unit Flavors**
            
            I am now setting our unit flavors to emphasize Defense at 90 and CityDefense at 85, aligning with our defensive posture. I'm also prioritizing Mobilization at 65 and MilitaryTraining at 65 to ensure quality production.
            
            **Adjusting Diplomatic Priorities**
            
            My focus is now on concrete action, explicitly defining the parameters for research, policy implementation, and diplomatic relationships. I am also ensuring our unit flavors are optimized for our diplomatic victory, emphasizing defense and city defense.
            
            **Refining Diplomatic Objectives**
            
            I'm now concretely defining parameters for research, policies, and alliances. My immediate goal is to ensure unit flavors are optimized for our diplomatic victory, particularly emphasizing defense and city defense to secure our future.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: o2vH7AjtyI1KLvuA
          - toolName: set-research
          - input:
            - Rationale: Critical path technology enabling World Ideology: Freedom proposal and unlocking atomic weapons for defensive deterrence. This keeps us on track for our Turn 415-420 diplomatic victory window.
            - Technology: Nuclear Fission
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a197caEqS5E8MidbH+QPi0U+erxwSVh3USf7x2BpBTd6BYu/vSymTM/g3q/Q5mzLX9OSmQ1GGP7uhutsM4TdqH0WVy3irk3HxOD+ztl4ID3WyzSCBtueTw3l0u3xQdEYcLOtmxqNXfYbVFAuPAmfzKJxgcoEWbi42Zs+ezsnap6Quuzs0U0vz04440Mxm4oiw4zH0ysTVLzrdXiZwhLmLfJwtqSrUCbn66AGQV0MLHrNumhOaGclSLvL0tEH9z2Zq47aEmqRYlMEiDp7ahEjRCtZ+ompVKFK0Inp4hGsLWfBiWFPJzHljYxHzKtPLR5hWRz2AF+ofYRZX1L/hSBo0j0FxPGV5X1d9kVwKGNg3P642lu3IE9gSBnIHOEkeXZZOKxT2/+ZVEzfZlMzU7LEeQKV1L+fDfJYV2EWzgApB5h1h6EpdZsuBEZ0kXeMXzFr94YxvsnaPi6o37A0ik2UW1JjGfVLzhUFDbOZj7RmH7T/0j+e1Je/tFRZkDwqi53nkX5ZKGEaJ3HLrEADClMl4tHFOFGD7DyRPgXUUMuRdAeNrqcykmTbb/kYOnS6wwrUTAZq8fLLic9oCNkGyafbICmD2eCzHqsxZSOjmkZoEm6vG40JGUmJsqGvbHEVGoujaYiyxKbpXZdvo0iGuevxdaU6rW93C3MW2flDNGKJn4iz2Q5UtSe2HjRgO5QIlXwR5exB6QA64tFmiioCDfG8GHtQuCRooK8n8iu6NLAqgw/yPhLCBKO64M1RkkfOD0Vo3VfQ4DoJ+QYXMvQ7K2QD7zkbiCT1b7Yeu7OS+6YnuqrKkl9THvSbZ0+FjZAfSYGpgWtShY1RSVILhjo6m0FaQwy7rb2cbiWdFT6504a1soneQBnSJhSsiqtq8d5Va07iJno6s/LdCdQmYYINSdplRe7WcW94Xwgnm4rN/0cwMq+fpKS3w6Qp6PFmLPLv0uboKKXC8V+OnVJXJjzIYEKULX3O6i/CdQumLePBM1yBSeQDZzB+oobnMBRSX7bgaqy2hJDrDJXUbDo37aeikaXVkGaJg8tzPbhnne0QEqnmdjIKTH9oo9tJH+g+DxVWwfVFe4uGedLOT9xvYe3J+695tRWL2aSqX2cS6m+wIJB8pf9LHfvLiFFmkG/TfIL5b+SQ+Z3ZpMEtD0GTpqYOBkLTcuq2IVuxU15T+fkI1sSbtS3qlOgZQbgdozUv3TDjg16LRXexbC++KO7IFBSuKDtm4m59W+wLsTxeW2IwbbZrdbgE+lGcZ+539B3NBZzwMWegTw1vLZuhMH/UHbjUzrZUFdYYjcrPCvOirw5RzywO8HlbgnaJFMZii3q5DQcyRZNEic52nDxk6HwKRjh83zn3I8oRWpn9oIy2pBCyE4j55NyBVQZVNcsqgest1kQcIGDAKf/QOEmIXT9u8vYXS7xZ8Gh23i0NllGdCZcwPcqDN4IOXHpmUdwbXOaRZBWf+lCs3CgcZ+dmg30m3qLTkVX2vWE1zJIDU2hxp82zmQAIlojkzF4rfF2mNp/gmUkJcAvC5Z2LZzZEEXwvfJstwBYgD4j9UDaHfD4bucGpB3feHMtg55k8xuUWC2BdgRfhT50ZKoT9PcUhIpZWO+6D44jR/UmcxEC13cU2KlLPn6nxQhcydCy/hYuenH/OkvYDeGAVDRKL8YI3eB6gzwaN4olAxOVLv+nCmb3fDxgh/68vZfRnwl779u+5oEqjwdfkUe4Vr8tIBbc8KphRZqc1SxRNQb9YTRWk1hNCmG18qIL7/TPY7H56Z5mS4EUReqTtxOmDYfgC/EgWcJ3Ls/W41BSleusMDqx8ojuueQ930+cW9QPHZSc2YTppnDcQ6vqm7jfmRJ5msMkFlq3bBkHjZ8ZL+/Ja6Loqh5AIY1rzFWM3xKJVndluJkj8Z6ocxb+nXLTl4GlORVlufu1UaotPCRzxO784BkL3eZWDoMZ2qyXxfs+V8dicc76CSshnAqRVXaHJhzw8t3NCudaQ3aXlyGC9/FhDhBSDpn0XUm48Fm69LUg0BkiuAHeV7OywbwLgZmRRrTKfoo8lwP+JASAgQCyhOstExTbor4b3faf5HKl/uG0nJ24PXLcEl6CHzR2XVf+nEv2ivrhn3rBNbycPPQUXqiCElbvHG2jNdqw4K0AKPsuGpotMNf5lZyOnPSZV31yCaXjitpfCzROImJuyXC8v1/54aW1sjWQOIQjb6lEXjS3VDqRzvRcqMrjQ1O3xkNpyQdEZv62XT3Lgplxj7gZTD4ckSJ+I9VovZCUAD33AOrbh9gU5CoUKAWGZc/lwhEpziT/K5m9SB4Ln68CNqlATX67Pxw6Brp2sltHIN/0NmJ5SLn/WjDC7IfYGUAr10m5mzCpmoR4y55St2mMUjp+qiDvbsO0pAREMqfMTNPTKZrRTuvB4e9QphAgL9E5qjML/TEo50vng6utW+uB10MIg3WBBk1QM7pWkEib7DCuLNWBeZ0DdGS1R8w6I8F5+smNL3O6u/GfHCqTkeKlYYy1k9waCEoyAYQeBAa7XuYfl4fHTxuO693CRhnZLRAnIFPiFZ71uwzNKQ0g4pr2cRnYEVceYyVL+7bCUjzgj5WWSxs6Sa6VRVueygN7J6cPR+yq9k+LyrZokDCv0Fds2tyLqUjocqyAGLpovcgpFmhvoed31k7cJDbCRnnh5eStsXlBSAw/Y9e8buTS5eyPlkenIpaRrlD46lQ1fLOVwKA3mQcGvohGaTz1uPSLxBYF2FKD0bskP3XhJMpems6DrR7qAESRJmyAsk5WfXZXuzwsQV8tLSfu2S8qCf/N3puTcm7sDJl73iC0q85mbLihgNEheX3hcQsDAMmo8qG13MZJhUMwYibuRLgXTLSB0cDL3wXscrlBnVda1z3v9r8yREnJ73S3PHrv+QvdZ182CeU+ftZi4+El2+lh91IFLPPADl56gCQCjrn2yU2hJHtirbB45K1Pf6wynih6TLrvEm75gFxomMZvjDpy5LufKxYp4ojjcxW9QAhm8qzyVXVhQ755PsL8/MZz3cr2FYNu4ccVuMJw9I5fw0C9sKKvNb/ZmJTkakpDbiVsky+dDSS22mQLU8onG3wKNQxKVuxngzwOby5FdOJ0RUznnaMGYb5Y0CAbEYXG8rb62u82jVBUi8W/Vq73Qv1mWJInYgKQ0ebRixvyMpV68djRXTbyLP2kYxd5FWwjZpzQaAToK0THFyg4EhdCoFlHfYM+VQlzsffSuP1yYJUWNXJaJcvXTI7/NvZKA2iaRK92Y3SCIKIRAAnIHAMTpm45ZnGUTuk+30veBfjTXE0n24Ej2P9+juUgxlyBdEJ/+6fKVv4EAf4lIZhTJW2CMdu8DSw1WjpT6YqtkPJqD3lrfxZhgiP9zWwtv3vM6aFuYgnf5tOvxr/7ACCtEDcLQdZ6tj7c+MukglFZb233xLjOM7313/nH0001357TlpulWrasVelh3Oy0912ctZDz7yFmLnj++Hh8MVcvpRo0fP8jCEIesp9dSATLDjSpaPThOMSVrWCQPnqUyLDE6IdqKYMwdU91l+Jj9y1Yd+qavaCmeL83c1iKZbO7GvpJHP+LwKLGVe3GzZV7888DlzIvuhoSnYjPsRUmi0s4lrsGHtcq66Ji5wMvLTzZyt6QJPP8tEH5yabmaG4j2kTflB8KZm0WI13H7hJpIjj0JjjBDX9x9dQ12Qm2tfk+E4vyFd9oXcmZR+ZNWi9P4b1ZSrXfqGpr3wWI4Y2DLGIZk5PZlEba1Ah0KEqx4t3VAX2KyFVob3lQBXI8GONqUEBMA1679Xe1/IygS6lc/gJrq0GCykPwMxNQ4H0dI13QGTrlFfRAXi1CUxKyBwnR7wsB3Yur2vT3RxqSqx8qe6+3GOf+uEDh1GpyQ4s4TouSYHKMkSrvCVKzRvbTD1Q0qEedFtR1zkaaTAxHOSMBMDdJH5j/oTBtY9MdWLwCyUDDklMGxssZQD8m2aDeJQpa5WhwKTdeB2QslzKYi+NxEJSsQEKa5G4+djLnUJkHJ/Oe4S8Z7gEzjravcWnuS9PkpPhS2a9s8SGBh3xAJhBgxIWvQx4Kx4N2hAMj/Qn6m5/BLDyi1aKudz/Zq9hg+p9pZZ6boqYH2eUHenyZMoWkJyM4/izfuSD5GbyqQ/Os982E0/T0PU9y8veARiczkpZdJg5T4ouX/e8p/G2i/hIANhbwrZYZlrjAylgiNLnkZpCpj+QA3jFmaDMs5a5yJzILBsIq8Y9O6B6O1xxJPtpncB0U8xWb6UY03DNGZiUIbf8lo70l6b9+1+4GC+ZR66oegnzxwDzyHEKaOsZ8tch/HO5RAohf8AM0gQryZTtFiqamyQOYuvMO6MnkD58VptgmBJ9dowbrG4il1+NPXKtZJDDdblHd1zh0ncOb09OrwAm4WGPuV797n9v3m3a57NvF1IGBdeOGTk5Ew6DJG9rcEeYu24u0DtPFUP8Tb9GMrlbuQd6a22YT+RipSyfO3qj3lJv5ogpmvptyqnKaNayTN0vki+8Nem4p8TSHeLxUc6Ltt7dzkSeWwr2QxcITtyV5X+ab/GxRVEbAuyZZV4DnoNA1rOvZTJ7C1aqcIkfam/K7mhsqCtFiC1qZ6Lue3ID6xcpKUcJsq8OIjF6Nh4BUQysJCwdd3k7EWie4CFxMXaHr6Wy1VM+vu6MgEF5SYUr4kXUBHpibO5Zm7G6UGe93m31J4Q1aAkeQSe2U5HUVBoS3Lfww12IMjWUiENOHuIHtCHA1GrGHWMJVfpKrn0zYxSHSHapjb0m+59/qHdh0fBsm+pJt7h6D96aqDCVSUbAeJ1EYqiAX9dAhx0bRyT0crE2Oe784CddklEH1qOKjn5t+lXFf4SR4R8u/i3aLvlcXaBWV9n4HPDiha9l2QP2lmJUnONCbys2bAdYlEQGD1A0F92686ER4ymGCy983FBAVAhJkiwKOVXOWy+hy7VonRdNCpOr3jcdtl0OFMYzB0qrzyYLMA/fibX6pHLaJBg+Ew2g+/hKxxHNUD/ag4yOlqRqnprBcRc9STEzg9YPUEP+i9pMahoBdalP1irwHGRQ9xD+9SXG/vvjdTBu+L89GB00hTr1dhvZBcuj/PAXxcXqVvcXCxLtLCDnCx2R/BWy3RRe/n7HwIRnzJnFZIaUhXhuvd3LPVw9W9NvaJBaYeGQbkd8gk23JHzV3SKR4Esdu7ei1khYCNXmQpndwhzfdsuF65XHjwK3Znv7ktPhFpH2cCVoGLsBXp5qQgIfx9TqNbM7Aon4MgsSpOvKcabniX/GEBYbms2GNhd4kX5ZokRK3/txdBeJFS1zvmVZRzP4QNau3C7i1SnDLRlDxgv7bduJX3Z4Pp3+7LyzDyCc7HIQIPzA+3Szw1hBHd9wPsbl08o0Y0+vOWsGHrUlFSIRxq90iLJBzbG7Nf5EJ1Yljl6zVfNHE/4JY1wxTIZsdeGkgRRH4TT0YfnrmvFlzTlpK1WDPsvcxYK4r2lWPeUN3iuSL8I1gQZXwuIiLzMau+U3kmY2EJg841P/hAC2S/f8w0mH/+amIOtjsKzSYuhQJ6iGVFfADJFk/UTmEpBVyiJsJVf80IkQUSSx/bVRf+iVVqF3RpLR8jIp9CgymCWIhuhOxDN2WSFEsFxZcSIAIcbAEJhkhWzvr9MwFyaZb94pI5N7zGpIp4VkERyV1jhFmX/EdbII0UIlNzsslxOmaa2PzXI8XLFqzH6DPOMSb7b1YvFlNpaPmmDRoNtplxnSjbw2+bQWZnit0hBpReSIURHAKJxg8GvQUnv1YnkKIhpYgde1BXAHM06iM2C0oT6c7vy3ppWN8BuqQiD+qzch74/6BqOqXbrQu0ctrPbE9SMqZwMSZHkWFS9cU9ujFQzqOi6nS1hIE0AxRgmA1r2drQVZ5PydUzP9c/vRDtQD8uzs0eDV27J1/uYeq5nBE5tbt8fiCy1N2EOg2z0HwQ40wuXR7eYW4BrngWSyhodMmxzrD/q16QsWsCRC05F4C4bzJp5PtJMikkPXW8c7KUBi8rl0IfRnYHjYyJVjvcy92xmCEJicaHYItl02paLL45mDoi7riclKaCwIB5NCVkp2UICqS27KdqjvRPz4pRqMiyH+2NyJ0nn/niXuylcX32SYy880fG7zDfbsoVqglPZrLLANHCyxH0TDNDaf7oxzbitD6MFXsADrjGevoeHLCZFSGGJRP6yQvjK5O8glu6kpd9bXmzW6cYBLCafkrhRMmDUz6dBOBLQ1L6vkCDQG3wj+jhZwRYaprUnshDV03f8rlhSs9T+TR8VbXCubyqLxieIZamC/aJCx1H0KwopalhoMNGpCXqiJS+bm1wjOAJkfalps9t2CDY4vJnFcbSI13BMABPct4TAVTpMmBtN/MeQXhLqvJWUBGJeZLoE34uisofhaTI/fnABsXgL5EAZxq8b1M4UA4pqhHLfiEe/FBbw2AJDSww8XlYAnarQFlHPs4q6QQlJfsv/re2ixJemEpZZ7K5grRpoD5Uby7/++w1/NI0idvRwqp/VKCuF0E1dt/Nc59bzL+UyeqxpghKo7i6NEVVecjeVi2cJzPVWqYb6wm5s0ZkjaLJW7JoAotN5xE5cIGrT47BJ8EouLJH9dfv0z8HQlIiWB9LlIl4AhU7YcP0VIrGAUjIqH/37QOobnAEWZUG/NSrBxztzYeZC6kUgg5hQV0AhD/fKpku/yQxi5+jK9RBVyEHqKv/Q4ZrrTebhbmw04F/Lu4fAi4QN2hU/wX7bYzKHLVssudoT4YOyz/eKxh3zKhPzDx7JBUFN9Ybw++XhlSmpHVzaZZsW7nZbuGZgj9KR/R3Qu/J8B7UqvpYTw6md3rZ1nZeLSW7SFlwZj+2b7DfbvuiNh1P+bR3D7aE9ZcMi88gM+T7E/3hZRNNQwz12k2jGFhrWZpkR1ajThZ7jEeL7X8yMpVWmO3FtKlh0Xlqs3zrYgKkmbBD8ZXKHPrYpsGDLQ+Zu02EONheF76jUt/iQe5iuNNAhkFHEH2GkUYpcLFdERVjaFaAh+ntm4PjV9/ayWdpudzFIWhu3URaQrBfaVbJeg5mCcWSN+avMnW6YdPiUyGae/BNNbOdlCv0gyGOjIFdyMH/kGy8b2O1ShntIlq0iF/Hl8ORG+iV2IjotOZhKkfqot7EnhV2+UtDnkea1xEBSKOEQLmUGh1EwIKWsjQIR82JOzERCBPChwbLP4JpGOnsqC6sy4xHQoUqHP3qGEcHVjV8WdWjAq6rzf9/cmiE0QfR8K/++AkO/mTfEd6BYHL7WqVunVgTXxhwiIIiRiFbogaYwKMdToBha+s3uG6Ik9lC3hhPiGkWkEh9/1aAXY+Ct+10oOHEOx7GV3qEPYzQETy98E67KERUiVb10X3KjZYQpDC1QgiOvdzUh8ovoqFeOh9+jfXcPRKbFJeuSSDvk9qOCzZfy/M1hnuoCE3pWSJuur68d3PjQocrLemyIgictktGcdTkaDogw4+wiRs3X10E1UOaQwJt3dP8jGQ7LmhoxGn+/tIAcU6J3Cmeblb7sbRM7gT5QyVY3jzxsQRerQILT68G49UfohgTWiQRgWPYBpmT8/qfAWhHAmSZt3xlzHbdPWeqxzG2uc9HkpB/U/UAGcMywogHRj2uR2J1Ohvajso5PTprkCI+DGjIha/7itrJSQRwjaBHhLR1Wm2fJbUqqCxwSogOP3qTnsvaEPMBd5J1azETSikzFVOFKbE0Gzlr91yQREBfu36Q1W6B+uVD970nzgzH4j8cCGX174SDa22u3IrIEnNVpUbEpAqSXF/R62zJFe35XvJXYaScX9opBnOknbS7Wht8TAYNIqMffo/7blt82IUYp7YMFmdiZsyhmhk6Es2b0syFFNySeYNV2YCAIwjAciF369O+Y5OYFDiyjkK3JIHyzorU2xiaiGMupy1+lIjkusvYTshYF82wc4Qdz/HUODQxO3P/gPiSmZU5v1xRZneaV8R/WPHN/x673LW9EDof03FgObcEMvg1qmctiGWK3+PhZFYvEZCje2nKwCRU3pPsKPwgRJY+xpXX74X9WjPNAIMKfspFgH9KLockWl7ul+wccjG3ndsu0/LEepQYe+x5IeLLQGItqEg3GSXrlkzMEh3fiLHhZC4ipK5LBHk0iOwUc4b2P8Me3QbQjc2bfdR3jurC/JYG/HqtWg3UjOMOhvQHGZdqXonPUS+a1wigNNNNdfDYDGYj6DZHEpphW0rTPNLlUrDS5kk9eb4bllEn8awvsep3Rkg4ccoc9lDq8Vxlos/+tcQmDHiQ6bh52Jk7aA3Ry+k+ztq2WVu01C47qyoMiYpeEw63JTkoVncl4jtDysYQ+0AepsJ6cvul7h48BYtCHQxQwZcpn1T3w9YkZPBgKm4z5xh8QrUOL+hgvOvJFqc4GFQDQe/N24hrmpAG7p8Mfa9OnwSYepvuag1HTtHuflN9yN1BMqK0Ilj2uc6em5FTRh8vwkjKXiCKHCztVnS1D9smBMKrwYgsD/3OMRkty/Wza10JlbXqk7Ep82rEoStmezNl9N4a2/paNk1oK8QnedatlPyyoldhejMC5jQiJJFG0qisul3D13x/0rAsyIZVupD07pzz7LX97qtXgU9yxNd5GB9I+EsgO1eeWD1bV8yJQdOq53vcfTaJlLwHCtjPUob6doKeC3CHMxf7UvwGfCn5uxuv+t8cVpBlx6HoVwwHF0GCMLF2MCxpo2uwY7ir23eMkwZa2v3WkZ7olPybUXQ9LHttZFq3racrf2MVyb9ve5R8609oikCJFuhGqwtv9P8iz7L5gLvnpJzQ6hmfy9i1Aq3zwG9xEM0d8jkOuMUKfbLKoWs7YN3lKmq4HnmaYOFKMCTtOkAPvST8gHV0u6rkbuQ3QSvgs7hAWskSdVAlXcGdDDtwc7NcPvtB6GxV1HuXPvyXxKtkNjS5dwVBT2xaa3lFwLPtJMZJ/3YFjCGnQ3NA6v50LSmGNhWeR+fCKoxN5cNGlNh3+AQSJDlYuvdEjqsfb49Gq42raM7t5J2uQmG+bR0KzYNK90VavWS739sqENtFIQGMLceeyWDxeG+9rDPgPcDSgJdExg0OHU+djEjvDfvJ4I9aGENJxOAn77smLNQFEsVzIaMcQTulx6tVQWcp+hOfMM1wpYfSmbkWmLULkVoXduX0CKzjxa5m2j2FtMKCU1pRiJi00e+dqW5NgLmlHzHsILGaQ4smH9LSn2VwlR9HxDuJifI9cJxeF6kcg3XZpK8bx1vC7oTXvx5PY1wrwIIljpYygoy6mRUR+hNeTkrkEI5V0mHDb9XJYeKHMyPV5tTUOcBB2Myl3A+6iatJmimHDUJgaXJbKMLEC+dwZtEZ1YociUTwfRLesR/nnx6JM6chz9wOQHIUFJRVqaqxMDJfTHZTQqB0oW1wZAG2VgPlJ5uozVg3yI6zoW0DFVw26sWvvYEa+i99b+kxet3oa+j6mltIGpcX7Y2kkaQ7tQlcok5nRVwy1zYfbLDPb444BWJv2E5BCHOwzWy4TQqBfq0ZicwT89wbX3RKD3H25uzZFzDDVklnpkNgg2P54I+vPBPRRR/uqG0e5eoeXd96N4owZZsMOZIBYi7AybDl0DlqGobNgfMFFXc4xF+4keou17uX7nUxVptjeBV9ChylOE5ODr9lHac3NI+oY+qEVOS0DzjmprBtrcvhsiGXekuFLB56qfeRaqDN7fTByBkkWgK0vNAVqeEPW76cdkhrMImS/TH6LE7egVBKfGObZAC+97kWScdjVHdJLabIKcOBv5qBboTYrsmssccJhrtpSalWgHva8WNsKtvEvFMs1dWR+F11dKlDjRk/kKxqy35h3lz4Xmpby4NmyM+U8ygKmCqNsg3sfF51sNZHTzY32rFR7P6sbV/e2mJ+i6M5mRwi+wahE4Mt1e7oKkY0UFiY113BAU4S8VMUHIwFICs7GYWRXnTLZYPI+YlmcXDfHCBQnLk6IjTjtmza/Idh/l6aswPfOgp6lbrPOAn9dwDz2tUFujAaAXfG+LgihyFJVF3bK5Fav7lOVAcZbFywAYcH9FN3tEExYi8+qahueAHkKWENYMrw/mZAnzYAlIRvbbxeXt+46BWtpIkaRRHX2sdL+4bBuaxG2EcV5xVOcecbdI8Bf3dNe5ACK/lNjiysU99IZBMhecB9UAGa/ErlxkBcV0NH55j3zokRmzcQoxyYwVBMdPPx/SbmMH8sOf0D4AYbrpZU+ct5motR7X7sW+KqY8Rxb2u8mxoSQ05oxPNLZDwqY6Eub+1JaFfc5BVpGCrN+xN+Co/UiwcBF8HyA7vpak1ivwa15w6a4LtKt64NjAFzdh+B2Looh42tXTEOZE5ldyttTBa6pc+hveQ56U5iNSJbrVezI0zn1BaM4rgAs5570WTt2nZQhWazgpBrGB+9XiOnG3kbna4gavbAbkFhGWoATImQNrQaT4xGoY9A94QYIGRLjWsh63AToOYqfEqZyK11sy/Ld8K5M/96p15VHFZMgVtC8xCi3akH9OsxD7akFgm+oPEuNSk+aheG/lzRo1vuX2AtqLhHWRO6HyazwQrjRH1Wzb7Ybs8UStQ/GqmOS0/WwREBwxEm1lNqBKZrw1OqXOB2plLjlQXm50bk5kWIO6BUs1sx1MxT60ImAz4geLSK5QT/+OjckvXiBgy14En+jJNcntGkBTnggm4pcR9MzmeQvUkr7DvzXruZwR4ypjOe62IhkGctSiA2cHXP5CjHaq41TH8e+YFLi/yw7m8+sqzpiheysqmaIIPXQ5Py+CIOzdq07suPCVg1TC6hXSNWQ9SRoPp/zetSAasLVaGmT7YoKgZI+OEqh0D+SeJvIGAPJFx0MK6hU+WCCYs7dRI2zfQMMaOtvxSoklGMGM6RarUNNKknMi5WbLlV5c4yTGGAEQpC6DCTiK1vAk5Q3koRhxtR3UnHOKXds/XXKIIcF43HD1IdFaseJAglsm32bie3qecleDLbkJAcsm+Y4Ju0lCXE502AtzgHEzCzy1TqqMqfyrTkYcU2Erpb0/JJeyBSiQpRY3bkL41MzJhmLEE7f5G3gz2ExaU7Ce0MSVKL9St9tjsU7bZIraMQTAEjxJ5jROA7I/5UjBYBva++GonV+za8SS6eIHDNTywLHUvhE46U1so4Jqv0NvhdLezsO4LRO7ddXFCAvkplwhogVDBSX/TcxxMFAK/nw1ksU7RfrmCCc+qJ5Ifz0mJkMU5jB57O9OaDXpRMh3J/NZAxnMP+aamlEZWSk/2Z+4NaeamtbbzzJd+QTetYWyj+FI+w9VOYVd8+OQeuIoaLvqkT5UK+19tItcmxK7767o0StegrOnBGg2R4UWnUjDWv5KJZEEP3YeArO1VBYX17sLt8zI1HGY7R9I9TdgpOCDalyLxs/10yB1g6tk1qdA3NAH12g1G3Yvz9O0oiHNMXWca91oQK0Z42SQlWBhIlGJgcIz4O3xoxd9ezEd/LtfbvcNJOLWaXaVV+GuyNjDE5WKWBP/fZvksG+iRG0zrHkpXTFfmPb2L+2bEYXQwzvd+H5VIE7o2jf6W8FzJk0Lw60GqkxO4ZlK1myNnVn8XfKgCcjKhcMfrgHienLg9WN18WxOzhPXjn387sfrhsjnbaSysN0Ecs4nqXKZ7E2b++GyEM6+GY0bOLeY56CSA4dT30RDfYg1WUoX7vWGKCf3wvG0/r3oilGtN8TfTSi6o+6RK+8r4KsKW0PUHPBbw4nP3MkrnC7WZ7o8I6+7VQFW0IJ0r2V0eLItdda98u/pOy9NVGEyRjuIHXthDdH33yHos9mh4N3z5EivER2Js50/yM/s8ZEUbw8c+a1ml7Y80Eamu0VEj9JYg7MoJm8fgnYEy7jfx0H0o4uQTS3OxjMZI11UI6UA4FGZPUl2aGoUHBoXoJGzjeNmvxggEPE14WKWstd1LOIDYWRg9H/rnyb+IZatzxIWKbivejFDwDFOPN1TY7ef35ht+sREg1XPM7pod/bCM+TBuvA4EpKEusxv/DtCoKhSwd+lTumN+BKTO1ixlckDO2JpTm7OtPR69Hzc0vJ+/4mdOJfWJzbmax8+rLPu2+frhStV1KgHmcxVNk/weDWycQZIR+kEj7BnH1GE+LxHkmh6aWrcJFyvnfcwMl4PZEvdQvuRQU7lRAgfaPj1aGxvJC9RSUphDTfZ4HI5f7UQ8iri/vqCaVYz42oVWMB/XB5q0z86z8WbGAJLEzGjeHeomi3QrHfL2M6eR4swOl2QbpNLaL4RD7iH2BS9LM/P/LuPY6Dl4m57/v0Ka60VqEJnWhp84vm+VlfhDLcWHRKs8yD1Fl6luRh0H3ZBcAf+BJKptsXCnN/qv1pazW/2qn6TGpCQQ4CWthLw99Uke+T+nL5V5VSchDpdXHk8SGJy8/9qxzK3/vXh62nH02wx+2usuNBUJBq1rahyWmnU1usv+AQFSU/a+/dQuWD5S+vzVYhuoz97InJlb2VkyaLOm8yy6V1U/o+zt82f8HJ6qjtd9AzKUb6e0n/pZITelPTUmoV5sw6JxPGT8G8VXnT+nsf3qMD4d3moyW8NW6SjLHdqrYKzoyXwMjv5Y9/t+1xqSersLDqbEcTuXeKL88ZVQTL+SbSfddVWLpLPSWOB+Iym1NJ3elhsyfnCOqvCKnXwHud2lcP2bQZCQYmn/VmB6EuPLH97VmPksG5LzzsviShHSHcomqp2QSBD+SQvD3cIXoypLeghy8LuSElEC6ibhCTBuDo1j/EmK53yWtz7q07yDh2B4xcXdRUegArXzNM6vAJzTVpCfyX5HZ1h+QE1e1AL8Et2Q+3lhQaJPxzy8n4bEQNdpVneXCTXeDP8ob8vskoEE5X8a08ym6hdiwKAmgvIsuFlmnvPL2KIHr4MuBIGolozcg2/KfCPWD9EiQseM1Bl3FtolJ76+rjjDPSQ//mh65U6kevSfE/sT+8DMp5T1hDIwRkH+I1wA+hPBolaaMr96SUuWht4N02knTWvbm3+WSFX5+B525Xd+5Zrq1TFbP92K5N8hp0HoBFfHRvE1ZnZejy364QwhCQnRkmqsnIqJy57uQkvdz/cOa3LNx+Iug+o8sLvJg4GJSZVMZe3s+8LVjhL7hQi0ja1itHeUdIQobFG7DUb3abTUwbNMjf5QPsJc+hrKjdAKjtDmSINuK+TvlPYoEqEfVCI6Dd2oAmsyj8/3T2pEgVSuWHbRf7xkn5VgjXEgFOFjiJhVFYm+k2ZHYsmhniZOqO435OobZOVgPSt+GOo7pUC+0wcS57cBN8tL3P83bdmQDHh1YNDF3HhWJq5vIyH13zWinGxMrGKltLKKJhXNX4lDYu2g5+/mDlWTn95Hp/sMH+1AFd9zMgR8Eafr4vr3SZ31iwzmAsXbmz34x88GEu9xPY1Ry94rRUnSyJlw9N++kPHv1jD0rz7CsbehUigw8YN7X7r/j5va8yWizlDFhnCUIyjIEYhQI2iBCAAe3R6BvbKnbO4rE+v8nrhoTzJJxb/KEK7INP81sn/MZ9W4VdPg6QlSV4aaAkHGwJqkCfjF1Wj5XgF9HWn1aibJsBBcshwPsRpLk/ZPBk/QbZPkpQX3sP+IOoafOBS2hgSSZGes1o8S8yWyOBJ2b1rmtV/2QZaW0CuNeoykm/gVV4ursjj82fdj9Q3JK3R4OtTyXnqKqG2thRi23q5NmueNPWxI+kr3qPUioGXaalG+KrH9w6s+rGILJEZuOUAPO3RQ+GffVgcda6uHI0LXIE9JFBOzUc6I1oT2o5BLdBA1EcROQsyLEdJjElJRg/N247bgBOWyY0doT0p9FuNohlPuv1mzx/jkVu7dwg1jSvDvyiUJFfND4ZytdNLYmQ83ZDEFaL9vfd3et+dYB7iPX1CNBguFtxO6BZ4uRSGP15MDgUlf1xwzs+A/l3guvRenApwPzyjy3RKkNFhdDOAe2nd2n3TWPlsAuTy9OUN9yuFCPqqC1Iz0drQVwNakPl/u8W+rzCuNWCP9Ux5Q9Rs+0ov/u+vxmLg/ug9UoNWp1NO+Yv/34O+mveCk8PMB+TQD+jDjTqMIvt5rX/GOZDnAhiRIo8D/vbzZ1Vmy1dK9RArI9EcZ7JQJLh99Q8b6NJCMD5Jc710jX/auMnDIZlwfoprtOjtZnwfhsMEUr3iGY0wuoZNIIjCe9j130Wa07k9DhvwTpobwSBHgWENzNTIaQzikUwIjKr2fxlX1ke3nEBCn26QqrDy2emN/MwCmFMUEluskdWKlXxEgbPPmp5WHNzK/b4gUGY1QvVyt8iv2OlsFlg738yuP33T2LEAiGNFuX1j1e/2kjA+LgyY2U5k/AE/DbL/thdWvthktdOAn4H+TudDcSkD5hHuqdaKFaD37pq37gbvcEMfygI+Z1P36WH4oJfS8Y0ytmXX+fyKl8hH0iOVz7u9GdAdLSB5hNzKOz/qhGGEJU8HMeNQO8ZhVLp4HFEPbGse1W6wQEeZ22WTv9x2WprotW4AU9wAcWJ/zCCtN/adYtWhjG0xRP+yse5XTd3he8wE5Q6jSe7NXehRDuDvJvudHVvioqNJJVlSUqmG0yJ9ByDSHwAOnp2edYc+hsBecs4LYizMnE31g7svPVR2jCVlEtkS+25NARQef6zixlbM21VvM3Jj+R+ATaG57wGZ9XBrPSHFMgXazBl6T1g6NpQ5NpgSsG893nqXE2iq8/8R4hZUSZyJFEF2nTotcjS78mJlwIMqYLkyx+D8m3PhofFvUylVSY1Id/4Vcpcn4NRst0BvbfTttZfiARCBwkm8eJ1vyRovu3CfzsdAd70T5KHTOmaWyJe2UyDNuURegqWTkYq/Zx3MtBWlMu6An9K6sR+Mm9hYH0OWsobSE3PTX0J5v2kQ4/rwdUR3M4q7NW6Y+svHizYO+xf93rB4evFgxcluO8a5djgiS+RhEvDYIirOCIxlERTBux2eNlrlSD+zwF30uRSpo9pLh1oLdixPrFE+XGm70FdgexVcz0iGXoOhOPNySvDljy4i8hmk3qc0iBB3JWy7TkS+6IXKT7k98+CnLyUhT/lptF5Z7bceSIe76H/K/2ZDX2xj3oYZYxP1uFVmczFpomzx4uDEWHekB+prK5EjIUss7jwZ7XiINRFikp/wbOPb0PF3l3u4MPcxZkiCXShbV7CpcyWVwyvzWpiA9QXcSLUn0okmnDDuFQSrUxDPxom4IwNlNyrA4Jk5dVtuaGPcM3WezNi1K8ANi48iCAga1nYTxkM+bWfoM9YaaG1W0sIq0A3W62XnG0BO/oQp78cikc7r+rIKtrDZkUDEhvfVfI4EhUkQ31+B8moXl2D6uLaPW2vly1B7rJ9ImiJucvZnxSQthV+aON6uPaCVCB+sgbJZG3xadette0EqQFllkm6haY2v7WDXFgQhWOQVsIbXhajsFRGDgojWzNv6Oc12UJCgk/dC868YiANprV7xqBvMTF2A9b4GLO0P8r9db2I42YcgNyTpoaw7GwBssbboQRHQk9TKZlE6dyaCvvaLiwp7BWr1/3vsd/NX3seM/L4lIogbuVNURnjhjeb/TaQZziW4oGY0GFRPUtxvdTt/Wo8egvPevMzvxgTGtSE8jv3ol7qWP5hX7YUuMeVGwZLfeQSI0gZyVvQAZ3CY49qokWwnG9xTMUyLQLLUtleGHKTJI6nFs9sATJukX7v7Znv9Jv1wMAhf4dTB89et8tjv/B6D8SixmRm2LqK4Y+iM+NxR+JqGQUToJSV0MZZVYIJBVxbGihMJ3seatlvCBgcFkHw4rsz3s2WeXXvoG0COFNJ92vstlebsx93gnC7sYad/M+5r4BGThgLEj1n6mY//xUqnIi/fccp4MKrfyr6KRAisDf4/vSs9AZ2QFG1y0L2RtoslRCR2kBOk50jCNLNy1m2nN74uoCWOrAkw11Jf4h7OGv+u8JwdZ1bj6K7hCkz20N3poPq1ziOop07sJCJ9MyBvuUcwIh6iJ3uJ1U5vp3/ft1W3Wqw2vMCbdfUjcJPv843dbrbYjLv/ep5zSpOTVc3nhSdv4jIH3oBa+WUoxYiCqkN5rWxqE1HmZz34LDFwp4YpQR43L7cfeSR8WYs4NB5D0HZ/H9htV7KdIXp5BHuPWlacEbMRH/jT9lbfjPotnYxCjPutd6vEVnSImpxLQhxaC6N3LhJYMrACfmqD4RE+gtWBrb17hELDVi0tIVm6ZpyhreZPRARZAONYPHiLr/pZ895+i8roKgAmLdl0BLSsLrlwD9TywGAHWanDPLx/hcEFXT7dNxVtyEuBFLKuA/eNKdc4NOVPUyLl3GJxHslPp5kimaYetPxnWGO/x23qfuw/3dI9h+rXH46+pe61QZ4HLtn12SP03nB1GyWiGM3g1sqv2EKi7aLuxsH+Z3Zm7siyG3GSVtPh1G4iZ6il8mUol3yMEAvOcDRBOgM1r91SECE+1e35S1U2h1rX8IkLFnKPFxIw/PrVAiJa67fzpHeRonDUpVfcvR9/fxvHag0XPB4vGIkOuOQ5HQmtCiVAVD8bQarNM/JBv8MvdyZsrsHRft3lPhj1L1BAYf/kLYXhOid4/MzCIOoY+TyNxnQ+DmbJpThW7yJV9xW/U6BRBF9LrBgF2vxKTIHV6EzGhoIviW8V0Va8cBtXsxkw508fynIhQVHH2iC8WRVx2ecMQtlrmcEW35l0qN9Jh9lZtyFC45gFjdiZDFn/uc3mP/STPQ9hnv/MC8qj4Sowf6KwLQOkw2gce3Xr25mFo61JuxyHQeRvGXfjI/vfm36a+d7CWijtGcp+CNbdUJw1Ja5xB+0KdYubLjvePH38TMcQq4hThfs5T6JP2SfbWXPbjQadcv05udtNjEPNkTA8oE1xk+CmIfmplpOsm9j+1WPqgPG8UwdaUKyQIssSkSMSw/CGX2gxcxRJoi0trfEyNbutjpMY+S5+gYaNG/vzmp4/fEGYBMRimudz70wnjDHx/7Lvc8RaCDXyeFGc6VgX6BGaWIJIm24mKPy1cmEAwfoQ3Bj6PPpgsVQihkKk3GZ/lUBCJl8N8r6TLO1UrzgRo6lFp+f8r8yKgjF84FFjKBSPNPyb9ko9AizF7e7Oqqgup1oP4TFq4BXPB+c90mSSS2lRbaOki67hO3T4UimQkA5M/XSk8ZLiR69MyNi1GXw/CoAgw40uCue+YjZ5ZIEVITIlFkF8jV8HT+xp4ovcdAIQWVLNf+4d1QFTvpN3+j1+Fx1VVgbTNFVLnr5Snd7UmMKg9bDta4S2bI3yluzIRZ6IfMEWK2QCXlmQkIBEO/wBWQ1R8tfcRpdBNTBMRW7A5vgKuZPRJOvIkGw6fJHhiaxUyPXO2T1jcgbA9AUyQUqBCg2ug40egfVlFZXQKmJXcqTNHjO5oWQycrNrAanXZO7n5oLa9zgsPkybY1fExUsN29ztqXz67mxB4kWNgw2oflQ1Pk6X8Gm4CTn4FNR5Sxehg5tcVFWLnhj2G/Gw/aWS661T+bhPfvCaYvvwXtIvkgeHVYeYt12/w5NUekvwUABlrmnor00tv5ascjwvjVcbKUDNlC3MFkTkM9anbSo38oeUSxsSTBqdAcJfJeFGPkohSRk7f7nzMTAFdYNClp1bjcac5Ais75CGM7eWLT4PHQavsRhGJTpJlLITi/8rQkHQqS8r49EODyVRMG/UbnAEio3K9qBoyGIdqKd23bgW7xrra1WPnU+pJTfEjzY0NpuCssy2w3IRxTtFt+Ob6JjdEVayFiDut2JGDfhk05z5U/cIdSNx9GMoQXMCl5hyIgzrRFCoku6V+1uhiNnmfKZo+S+xJ3689eNcmJD9L//jcKa+RyxllDMN9EWOydkXBdR9l9bNvvCmB6KOah9SgmcH+GORMC6iaJSlMRBziK9/n3i/YN/SoEvUtDABQ8asM4hwJRTqH6yhyaOCqYY3FQ33l+GUnvm+3Gh5SLMqgSH22ws0AjqvP9bbAIfVG8D2DXFkuNjA19UJgh1vyR8OcuR8lSbitBotxdzhbnr1Ch1zQrjL+HXnKvFDx9XkRm68tntkYWdQrqhkE3mXSwZikyoEuXh+/uz98Ks9SwaX8lo5xJvGbXeV4tj7r/rrKl5CpqDu5kBXM6pONRlv+Zhd8n10gYvXlELwJ8FtMUcKViKtNKS5fNqogublHtwUYyMDK7H7NzwlCcEGegV7dENX8jZQdV93FcMBM16mcJUcBI0cmdieW8Ssnhey1i7LYFrDAS12zGMBArHFSbgN5YZ7pGME02Q8IzONkrPqAFoQbWoux4pJV5fxKLPQEk6l/s6T9ovJ0UJKC+d9jMOOhW84EZ9vkgU1yTdb019tYsk6BMF4Ep9rIPSbjjzIxSMlhvMv6aC5PsyRPU5Jm+GuYQfX3lp/i8yyHHrXt2av7/dsDgLfim8ZOmmdSwyrmJMne8h3SN5hMPSIcOX+L6wynxufZAJqLTZijVt3E+KpJrFxqKX0twbKfIONlp51jOPI4LQJYdH85c9s3uDHL/OSbNr+EMR6aAhQIUjSBcCy04Om+umLrih9KLot8DlnKNq/ycDbo+khIVEiadBIHdMmKYAz8nAsHbC9XnxnHkcewR4SuiBq+uDFD0BmbkM7MVZ/PViOeoU286m8mj0XsUUkZuFjeh5Kn2ZBWMf5rLk7wPNQbdGOpYokRkPOkorXxLQi0+e+QsPKRkedSh59rTSRE0nvFTfnp90nOCp3BxqHPd+QfmxiNBVEFvwzMX786Y5UXixYFY422gxMv/7DqhyBpYxbo1+GZgc+Di8wrVjoh7haabjLSYiEknAzeOxmhMOHRH94Q2MacVqkLictdhOTh5LbLxab0y37+lGvP86fPgjZPEuUBymneZNkRrQgxaj17S5+9m5IO5tUnPz6ZmvfBPFlU20PqVFrwcCl9f8APULLbM0Pa9SgbXqsgbCX0gURt6vi6SWvOsk8uTlN7lNKvHm3t4ftS4JjAhib5sOTrGpyU/VrDxyT+S+JUDiabR0KV6Lt4SxxOwaLcZzYvO3ysR21IBtwl43/VSGG3V9VSyelmBkHWpRxeziR4scsTg2kQlf7Hdss6YGU+62A3RxgaYudvct8rDT0cZ0TKsq0EfedHdeKen14lhX+tMZ7R50mX9P+hHIkuSBQw5eNC5Xx1/e0fcJ8FqqTMK83e6pjSALCVyq7Xliyry8BqQjF3CC4ypzJoYwipk63k/7tw4ppr7+tu+S07cmrctYHTodxv/Qj8EpIMmjD0HsKbbJPxRyQy55CJHAOGuZULKwHdQhloy8KKnfFh5692qzyPJOsKT7MXXVxncrloTn6ExKTTj1tHU9MSW7grKuSkkr193k5vmqE3VRwKMlddcVK9R+c75viJE+Kekm97J+BPEZb1eAmLrijwBItSOgdlB31AaxgOqG/GoPkriPtYaiT866jKBKCcod8RFtqiV5KPPvRE4gvBUnQNneTiJOjEjBA01Pi/Rc20pHxLHC393Fil0XqNhFhRhGo8oIfmAOdjAOKpUW0R3MxKYa+IhLF/HYw9MFeLolzvkxoWf0l9c78H0jpNecOTGo/5CC3fP903gnFv0+XANAqWz5BqFfhPqJ3WSQzlYka3XywX8rPyyv+WY8znyeeP/ow11QCyU7x/+B6mYbeiKPJt6d+6ecnQ/T6ZN39TC14UfYwzHyviEi+mEmRlKNVcgDWP5af0+NWepOul0qRt8P5Ugynj6M8pQvEzkRwidaQbEt/BO1cmHsMRbCQcxDORGs3yoIt3dKCiwle4fdAg87SXl93Rd/xLx1spOA0GJlVk4nJNID60ZrBpS5rJAfm4cq8+lsNJbf4yEsXqHOe3kTvHIpmLAwx222K6ZB3ohvgwuQ1zwj5Jcwj2nvFN8OEVtz9VQCfSTjRGRPENA3IiLqjLNnxf6BQRRndxSKL4O0qEwUbT5+gYoWkzXm+vXziXrMsZ5/0Nufkurcm4mfWpCyYB7YhC5ufoFAOpyk4F7BTxozvBKebMA74plUWxmy0udS7S+d7ioWKool3vulKyUouQFB7wB2uu20HlyWetnfgOuCqjdOC30/3cqsJxdp3Mro+kO48KF8KZdISo8RAv9T8ZaMXZoA4nIzIacsRRRIwN9YRAXqGVM9H+XgVlPZlb+ejF8vxSofndzgTxNBpg4aNdsE+fU/6BAaOMPfcCuFGnoXPJYeCWKfCjzM8lS17PC7QonnwqbKBHyYFlTO0Ra5hcWhMk6fivxhAJVLRvtsXq5j8+3YRIA/ZQqipgRVm0Pq/JKuccg1Nx8ws4anBUFjZDj/RAHTYWvR9Rl6AOJg5a2bUl3yGp+P8c6n8pZRrdsbeB5jzCQDpQtRTwfD8bsPsAm33s+dnRk3wCW+JwaFOF10QDYGpPx1/ne0g2T7w2Oq19m9gzxbOU6MEskQD04dv9Cl6KziwFXJMqMuqh2yVvryO4JPAt0Vv3U+P6vjdDRoBGawX7RsErKThvHZ3MKkXAv21UIJ+Xzc0epqvoLEsfjoAARL0+Z8gLIzPZMA2y7frQ+d0TGEzxBuZgkPeOMnlDBFqvs0t3Eh3Xn2Eug/yE91SW3LLBwh5HCwZIx4iXYGchOOdpo/N5b7tKw7PNNP+BuzHVYv80kzLjBdOiAweQcVwxNtjAa1Jv3F0N6eznSh+PxKfQiHZ+g1tFdM8lH4f70R1BRRvW0exjgX0D87I8Rv4LIbTQ0WPm5BNOXHBKDtPiqdeT0oqMZqTkkp1OBAHhBwCtLpCCEmj/Mxordg/CFmK7tHolT6FOfwb/9xZ+YRjWc8Qmos4NJ5QcennaNUNNwIvCYlupZVxJoQ9Jwfz0JxKoh68wRByPs73eKD/rd6+bReURX8wNvuYOSUITMcDQ8XuAnZ5xUF8KMmkklABDWm40LFxfq8fFoJ7Nf/ijhW+89mZsUx0nra3ZpDjmLD2ddLvgfdU1Z++3IeVNv3GnTuCBTCb5i00L0Q0MIY/d8d5RRnQVircFMNbCzKc1vZ0Iwebskp+SANP77RDJu94SoYHqDdLUrPTY1iRv4pqaz9ZZfhsS8lotcyLFCCkjT4OzxtoWW+bqs8eY6If8NJ+TVVbJJlo/YMWE35vQFK2WEn1CPdEsjqZIOXbL5QE0HJXd9xVhymEdRq6D0TAAjEtrNYBq8Ug+A9GWWyaRXkXLlAglfajR69QKuPIninH557WLFH4vHjt+Goi3TbmGIsyGUKtM/9bRIPsoVYuYbEwYgmhYCHjyvNMFz+xDO0Ag9ypj+1/qbahtFcBuxRjCd8kzdAEo4biPqyKwE3VNOaaHMpGPq+ishxwveC4l308vLgNxA+fUb2k/KLNZ/UTzr2CjZsiex8AvWtXOiOI8R2tycfnEb63vpHEwOFf7ig5nb+6M99SVo1NysNSzdswJcVCUj+HAsmQdZAyjxbngSSX0acH9gi/g8DNmSj32wiAd2bJJrkQ8Y00jJspOJcezB9E+Eyczi8djY6Herb3BDVPSkT5/xKl9dF6HKW6QJ2TnYpasvk2xGe7vkjo+lBDpBivV2i+fz10EA+vqudAINUzBB2hiEyA3rZ3NDf2jvyuYvVpAoMXnd7J0svrRKoJAS66BKVjb95x+DMb6gNYiDTuiN2cLMddhm6XXSf0HgkLolfRaXIeBb/TEGgW2brGQYNk6oNC1Mu+hmOuXwV+chzpq1Lm8MsmSiJxBgiLi6pGGOXMKiPhNM9jX1W7/d7YnS6j4IruaMdLzExuHaKxaeqoYVsrAZPBHXxUAE58mTfwvIKF0ByMnZS6CaFY3YyJKXovnlE3yRLhq7GNNw4EkjaOm4z4uOEclDTlYLDN95GSGu5Lx7mpmj3mE/Jpw3W5dnwEqQtnDVMNsuT55XcGDVdtdYXxcZiHFsB7+mLzx5zgdqZSool/R9kvMH/vUzQLxX5+q5siceLh1AQHbl9oZT754jlk2+t8KFW/aybm56BFd/ydbc7BwcD1vR/TWyuGqW+qdcbUYJJfBej65vXoXa11Q4tpn0lUq0TeDK+c9mBA7dkFm9gDL4b6vmad0TpiWe8OtSZtIhUdTEtyA0qKUY9vsQQAtAgmrK6AWYhPuJI3aGd0xUWaAjsUEk5jYhRd+YILEpJJ8CBi/pMpsR63zijALGrwHpmpzQHkmS6vesugE6Nl5Tsf2yjPzPkA8cnlXRjQ307/9c/gbvsX/0PDruVm6hhCnd1O/5JYa0pPbxQrD+oUAEahQNEF6vHNzYpOSr/rmjN8BKgEWkw7o239TTrUQ/mgP4G5iIVeymS05Bkz9cWFItp2xK0vtqTbHXcNUhaJdiwfvbGMGSfbV+u/2uX6+9A8gYDG66OIz1HySYu66imPIEIrlVwnCYJYMVAGWxhaxjhMgdy6CdQA2GkyEwwOk4/GFcifPTCP9Gyb0ccr1Ioo3dr6tR69RaGPJS2qxEccN0NmZCx2kafkLgElFlQlLp3xhNT/0Bul8eC84zZRIFP3mKc+eHmkqWToH6eO5530yAtOZBl0Zsg8kV3NfoEB4QriekiBGQrQyHPwGBk/zay8JqP7B0AtWGhVGsnwWjE78AITyCZQFTVGaeAmlVU34Cqx1LdaYGERU4J0Sw/Hl0+r2PfuPUkkAObtBOhVXDW3TzrojK3iH2pvcjvzF2qO+22X2LkzoWGIiNUMvp3R+9aLRguicNxJNdSIa9CePRg+/EOj5ppmuMYaeWOhKVdlBQNKQ0SPgbU4vRFrIBQsSAZLmPsJDVfhfZY3NCiQX5Gvq3JXLyDn0/gIro6TLg20Tp9yTwoYIbOvGCZQWkIuoRVDlEB2z6LSaNlVXUSz07wAST/IcGgxUdzUJkW3rS0SbsLCmYJhCpRHOPucQa8yXaqUWaYBYL8tSU/NV1aAHzKDLjJOXADpVoayiDUeNhjEGe8/UkzXrwgSIjzqGMYw759vssgCIJD282tKM1UadonVxoUqy1SYBp4eB3Howf/6R/KmffaaC28HJH2nwtHwr0GPoJMsDNRXUOEwD9r3Wjtct8DQXG7N0AfsAlS5yE7wy8STZrbw16ZcZJwm2QdfhZMCBqXv4+2d8/pPFurQikYiL6SlTGjAVYCCgdViCz2Yf+LKcmi4jgXXaYRpcp3+edoImPmwHtayXokO5KB3/ahB1sCk8/giGDYvbfBGy3cwRPgN/gn/BFaNIIJD7iBxEcoyar6MZ0IEBnFsFo1LrjOQctar4fJ9BgBL7EtUKct9tMVI0gdxmxBcVKeFtOqScLPS3rSiPpoQ62G8MJR7ejS8BcAG15QJg+d2EGKPswXiRrPrig/BhByrPHrQmkNb7aXqJZbVU5/dC+uTgM8jjjP1b5ZRpqrPPCDjvnC0J70JxmxxVtey8Mtr38xXT9j+UrR4wvWb6rzHEJnEKVj6JUSpC6rpyOAkF2hNyciCiTSZMg+uJEbvr4DbMTvG740j/uQVX26dJezRl9jnog1XLadsg9KE5JLjejg1RK2L9jnK4ol21rq9oD3lzGDRQ5OdJMNMzCM1Dsj1AqWxLMd5ZNdy4eNT1UHVj7wofm4gG9bb2AmZxZpBUlLOllzSv3cv62cp8cgzmFbecQ1yxMG/m+vQI1cIQ7fjnHd+6PhcoWEpn8pXbR0/65eZU4L3oz5DRP6/RJRriJYGH+nYPWoS7MFBbfAr1OGbxYf0HQG78Hrdv7T+a5wM4ELb/PRfWJtqaZwXTiCc0vNAVqyz0Bqk7XovlB3Kpo3caYzVR0hkkOeF/zuTl8ZUay9oHmsXt9yOXiEaqEWTak6NMTpDez3FE6eS2UcD6pHdKC6BJ7WelMcNELgICqnY5EMeOD8HEa44j4SzwCzqAjHLwVpP9JNXay2zsDx7lTmDukUBTnGYy17Tk2ByGb+oEIoF1tirwPDYdkYp4Lwtg1wfSJar9UputzX8WIcuDSstV+vvpEk6gyff0ekU3b4rRnQ3fnfNTUzuyqlYgj3VO/6dWawqeJfAFPDGMHat8MfeEskAFnvxRhYhHqeUbR6iDFAOarTh5fmGG8pw+loeyRWegvZYhQl/13iE2vAby0n6u6jZZTKhatpa2QXNSduHyNlfmp0cHO3jsMgsFVRqLqqwGKC76aCe7TUAcNfv6/IrF1SFtUn1ZQg4cwRf+x+gbQKK+bHcbz9uDRRhF+sHRelLXGrFSj/UnDZ0ZLG7KHu0BYfC8GvnMzaegVJto3V5H2oJOOuPjUqpy93+vMfmhOTHSkqTzeha2JEZPbdjbSv4ZyA7UXybSdd5xP6ibZ+MjUQCuRQkdy/9+6J/IHrH8CM9zjaYoQO7TzyGu4+Cst2ZRT39ZYiQCXFYywaJQzgIHtj40v8NtyTEoP3ER1pvuIw6n3mjW0xQoT2t/bJSY+kqvlJOo6CSHZQG0QniQ7fCiVPi/1GhwBByVLPv9H8y19IkxFgobigNkU4mP6dCkbqL0TYsEXIUhURGDAKhAvjl9nyIZTSls2EG6FdBEu+unLwVSezwcBBtbgaWrsg2Vgw1/jL7AFyUTE8yth2YYTftql5t+rs+1sNrbLAWrh1jYRiz7234Rz0d4dIdtFaF8VGbt2YW49Zu9INCO8zMfz4uFGkEO9LaugkcTafRsh4n0RvlSN4c8xQOekJ9gVFR3GLc5pGE+Ykt7vh8e04JrEvk/QF21kktkZhRP4j4WpW1q/ekwwX55nI8aeQGshYqwlPr65LF6MFu7BRwSSxdlkRKeWh/fqNb8k9qV30i5y8d/oGNF3NnR/oDmCE5gaA+WhlPILIi/bW3IS49BFaNW+WU2HNYFfcOqrFg5y2D57bwpN9NzAYIuyIkDakcn7lxnQwedZbrwlWhCnw1+tYBI/CF1ifJm1TDUAKFiJlmYlOdvSuKkFUJvUPTTZD0vwnnvP9izLl7zDxL5sAPg7dveIRiLkM2QSn1tjtUIkE8L2eu9dh/SjFQBj871lphMTV4jjXtgsTWcBGLijZNTa02dSOAuUao7Y5IhaaqEB9RrDJQGE6fk7LefqXSYORhTvl0fOuqQtRGATaR4/dcOzrtwq7n2XcIapQViPo1tbxpN/5WNp5PxP5dE+dWIxwQ/Rdlshzqx66s9h6uL/SryK6H93Ud64T7e1VFRincF6uu7gcUUzkOFzCsVinZKbHp2VQEbAxDWYv7rusU3vL8UM5W//bz+6kq5EcFSFoKEwJMqBwtaSbpj82NhQJu8vVGRgYkv9aDLwe6VZDZ1ajRJXMhDPYbqMASbpMH4cnvubum7PgK4qVqhYdMj80/dE6DZaA5qHOnEiBC6s4b9vW43qPz7a5RfUNI/vKc40LP09CTpEds6T8GMiUfu33LZd98HvD+BoNkd4DgSt9ehnMA98TGsctKw+SnfI/WNaFexhEHZ9BaPo6kKIO/HoQrT8WwJ7GgPOR1SojrD+1no38VCgDejckNtWMaLnwx/ybjYuq61zixoPLxfodZjihUPBWKDY6nPRGF2iePdZ14F8NeKZikWWwlQPFjcwdPvXY8HtQSY1sXPv+hpBkAaAzecCijs/WHq0mtE+7DHOu5fsCmuCXvxxKVRl4pfmr0n1v6kjSrbXk2Vi4OFXAiIXP5hP3WPAH+/gPGWpVE1Nx5UlqUOejZtztJT3IoJcnhjS6WOX00ZKGx96dnehNDH7idABEuhNqXWmFvfZu3Lkxpvqzm5NBfXsuWdOka5FcnNTnDma4IeE1oHZENvm7SrvAtoNfrUKniIUMQCzpSmlN6hzOmJhdJGkPIOJQg1NECIspt0l3y7ktFAYqb4RUCx5PM+++aAGQIkP7Ffh91AyjNHw9Rpk+IXhVAP4x/2gIbDaTdvCR4KPPbrP2tgAs4it4yBFhygvZw4nnypN6aT1E7LuogZxYBhGGNiovOaxZHUdyVt0YIB19TZXQ5bYuPxkhrusazlgG8RenAMNh+l0HeXw7uYmFCONgzbtMZerZsHffCxXaKYI9V9QG0EfsSsYVcEnjbA2yVC53V90g2pXp5JugwVOB4BMN89Pu4oiW86cFxb+XSvAs7ZKoM/p9j0oRpXCAEWv+7VvQ3z1G/h5iVucDvLh231aYNbDisEyTuS50KREVL3ldkIIGTo23ZgX2oD4oEYdAA0I9Hcbd/oZH24sN5HCxWejdWoqiS9YNNNAiw0mB0SfoZjJdT4sTBskrg0hI/o5eMhjGNp80nSgM/6DNmG43ia/A4UzeQMNE6+kCFZE0RZx3J1ZDnAiotYa3sKQRe+UeKu84P8Wq7JnkHsbv187T8EMbNlWezYDirnD745SaPZ6W4zJJKLPcRa7SAORSGLk2Uy9GNk9m8S+naBMlB2zgiy5I26DZvHOj/1QfFqOFDm7Gc5l3O40uShrY0WUfgLERQRpE53z/iGx+LKjvHBT9gBbB3gGR9GL3AP/8OFSD6n29oiD4H2w9/VeOTQNdwQUn4tNalvmRnK0rUf2tF7OEOf/37LuPbMtyitRxO3bt/qsduMfb0uChKjYWeDOz+NhojFYiqiWVyuf6gOUeRaH5koykfaWnCU2tBo8Vglv3Q7+IzUf+a9As+Hjfe6rMnPz9nPOoNQ8V4LS/zsYWyoB93mZO9aeiyrU3LtCooAPovyWBck5jusdoybhTfFCyBcggU0xTFhd4wm1/1qERDjF9ssPw+cZnmniJzHdkJyc+NzeTj1+shiAttJuFwCIwUuhKRtz+bIQkbFPuMq9YnnACN8+sLvFg+DIhPHiCE+ycPW0JLDwKHs5bQd/YL175tLKjp57WaGZSsNA4EMXSTGZmY7oBODsCy1JlIEd5yNWtjs9QmPTGdmB41ZtJjBS/JSG4VsL8trb3Xd0alefyPpKlCfhXNIlcDJRi2dSrB0Ol4ZZNe7MH9KYW2tCE7Wy7IN4zaMV2TwmQ+U938bP9Mw7djxDWQbaitnxY2fTg6r8AfSz6mQ/QuMcaJmf28C7h3qhGWHa9TcxAY5ywnhbh0WUVeAuqxJsQyA2EkTYffMmOWXaQMaOQmFRy0jFWSz6syESqmBKB6StitVnjHV5PTYwhISOYndasaifVC0I13CjPDtqlcQsqfELP9WDRsKf6Kq9CF4kX29ZEGa+WpSHHWmJMJubOGwFfwPBcl6DTLuwfnikPpgaorqzlQOydP2j7sZnLCGWfY3wzoKMWbK6fpu7wYtjcyQOQgRtEyawt19ej2DGE2oFsOMwqj3tQ3Gp/n91Qw/2719hlyqUhLdjxS7p0d8VtPP2RN2Fnth6pT0hKoMJaqmlOQrhW19oKIuv6u6ir+tV6/Gil8RBbGMVTRXpNK3GRomZyjv3LrI/JyfekZFCkg4CkjdhtCkrzNJPiq0RiceicNoGJqMbvu0xOtnDJIO6axKPAqX9Oe0DruOvVf+1VkOeBEmutIAogg7waq/niEV5Vsc2UsA6oXBdW+BqATK1Jv5e209Cf1gdKv2c+Yf4DF5aezsBZ8pcIXH4W30hSTo8x2O8bHqK6USRep49P2pMPoR8ywmz/VzIhn80nOUdvbLFeicks7Q2y8hGafwaX2g0yUCtWATnMSKnI9VW8DSzq0Lnq9CsdcTsbPMDPZJqeMCvfPwNZc1xasmtUnfrLfO43Z1kFBtX5pzMVB8/lDm20d8I+nn5GjvpsaD2skMZ8nNdVVQmyKbNbSNR0xs74p4jYXC8RmV1Y41CYfHhMOswTdYWckdoWdBJ1jl8l4a5chJuNgoCojHejog2bsogb0uxhvhTbstXSJdmjVoU2kdZjgcjXR6eEdqmhCT0lEusdOXsNUt7TtFtgKMJK1mRaewi34vCZf/8kj1aMFMmWSqCTIqlRu47f20EXa1s/7HJnKyhXfwww+zKzDLiY8oakOe/FoW+VgK0CP0C9nWg3mJgd0Qwdk7+whCSkA7rjKpiPbCbgdpskBPy1XFIz2sg9LIFJKlNB8BLGpeoWRKa6ikylRN2fGcyBqA+5+pEPPd5jZSVGD/Z2uUne76El7+nOhijbYsye6dVNNPEGSfKTkvbt7ma63pID3GZhroEr7X+dv06SfBPX8opXfQsRqC6XOuU5IVp7TAHcQ1eutvRbAn/bmEvcwrI7B/An8pSUKPTspdNinWZmxvfseO9XofHm5dAhtLMgjqFHeruFZ5vHJP1CvDt0jge/4zOoPr2A9YEnMBXQ9tK0+3EYQEuFFIlEC+XRJ6tsDBXeruYxFcTGKvjZ2cKPkYMYevKNvI7xnoyMHLbGafyoNpj6QQHUFoWkqiLMpz9XYkT12WaMRJv5/VLJ1rgEwhP9QYjZMNq+7rLz//+f4vnEhiICsF4UyJRf6PDq+2ppqUYix+941Zo6/rIF6RvgT+DtAW0SPjqq/7FfYGbelkhhqzCZLLmMiTY53Mxtx8zkcrYIiQfplR8OVnLhmhVdDLwhyIAQLU1Adzfov7K32v3nHrzMePZ/RclBCi8KDBqQsvPl1/X5w7bxaIZQRXnnwZKgYHZsAia3AodttTHj8b9yHJEFgv1aeKfXLBP+fuplCgxl3j88hJCkD1niIrclB0cS/c8NLuTv+VATOZKjk+MP4qcXLV/XR+GdO12NDsewrw45le0wjTxjV0NjZwYhUd0xF9QJQBMI3IzbP2gV8y5rFYBpwTYPWCa+gzS1pyJb8xb5gloPjrFvlYiilYGoA04DtIp+1b7XcCn7GkkftHplYOsC5Q35P+WuE83b5L2KaZkkLUtFhobR9D7e/RSLNOZogjPvp8TIAqBTgGmbdM4fp5R3YkgXcgebrnar6iPPWRM+59KBperqw1wpSC8ephMzVk1YF9HK/864SMPpir9h+3qxFkrHqtM7YtyUCpAMKdRm3BZdTDCZwVB3qQGTwhJXCgCdWJ4y+/QDKRDEoS0w4BBZRD9l+ufKK33/UeNu/wIIZd2EvJjWpT0PrFYWHdDBTnVgQGyiOGNvdK7p9BswGUiQFPKFbOU0eNa6EWKTMMtC/axsYgM6VQBCYtYP/lzV720Gu1gtndMyuRzKNCQghgyzsaYbMJi0pzucrehdeXekTpWL3dlJLeNJe5k2yz+KrK37L7GWLV0zN5hNKPJeLlnZ0q1y0u4xfdVzAN6VAZDJUUh7v1N7/QlnfoKEbJH2Zn8bWVj6W7UNNvmcYAavoJRSxCJLUqOxaVAA71UPYLMJyCbNNudT3ZCL+sI5S2TqQ3xk9xsaf37821P+dRvKxvsx5T9rjhO0oYdXSy/6+J8OzPSSCvEZFZEEZHzu4rKKQaoPjMUKlassgRztZNhrlaXZN/iQVfxshbj3bODjKbMSOYC/qY41z/06CruKMGz16LfQONPCftHBS07c3F0YnfBjSLJfIa0kh3c1byxz35n+5zyLg0Km7YNPnI2yVFEt3PHUedP+9StIguytV2YEYvcQ8aO/cyYWZTvlp1lQdYVw1XDgTjzFR2TvAiXXfPvJSFKLlecG9FdEPRFLnRF2U8sLD63+JnMSs7wSdiEiv5JzlQ4sVraFU2jbK9PN9cSlKoQTH8SX2EKFQcAbyv4giIsA+auIwjf5aQYiuRCfpGHa4hSYNYHMc8ZONw528IloD+NZVcwsuvmnz7VdOq+WJUKV/dCgFoRPBp47iZHUcrAKsYhgtfN4X6ta71RCxNqjvlkZQEy06JyjKYCra91vMlvjZW4nJn7glrX0GR5QAx6JuIDXzlJ+WqBWr8o4ud8O2hMTDyVFxRHVgRo9ZaD8gx3y8ttpVWzXGNWvvahkYRrntpUKlzCbK5vyoeCcYZrNdXXasoOr+MWYKN80YrZxuB6NvtzJWojm8lf+zjTWOyxtVKuB3hRvkrT4YKEXlxF2ypb0AjDD9xFzYXGNbFv9YtLAJKdVqys12Ovsn4jjDEYDfuo229u9mOc+7/NmGB4yIXJwwdqLP3suMpGl+Fsn86RVaeVpRKMVyKTya4uMRpLGQy4TIuNXLR5feoxyFSHHxTzvTYlChMBYM5HzxxY2LiLInXhcLu7LzkeV9PmbD2d7/4bIAGO7KFmdRmw/2/N5hr4mo0Tyn+3f91TUd6URQagjkYwHoGzsmOJYT/yFjpaFU9896V8NiMYrqBiW0EmnXdWCLJCGXPAr1voHbBLQOulwmmi7zIvJYnmoSHX2A0cGmgOtvMYG44P8MQR+mL2Ne85QArCzGYW3dMmQdFF5zNkTEr82Q39ONdnY+VpH7Ibd29MMZ1Atp/gsGhwWEgiHlA7ufzQcUK6OYYiw6Y9rl2AbguKyjl7kjdiOXVXqb2YzQ7tW1LxdnHd3rq3dQBDg92kyMPcBKbUdGB1EhnQZHE1ww0I7KlJCunTkNpTHahV4XPdUPBym2aTn3VQ9awsdSmdk2jJvfZ+wbDDLl38broxJUiAaVtppxK2y/tDSFSVWyXiQPwwFnIKfQZqkHLegt7owLvsntJQyZbjKJgYZcXx9DS7OMEQ4ppM8P120fX6XA+AmGeSq8pFJeOz50Tt+xAy5efraxBlvwpEJMfYwPk235CDllRbSSD7QBRHxigUoEb4x27NvIyHZR1BmZRgdYru+yuTn0eBwSxR/tDVdC3CQgHWK+FTAo6FONSoEOTR0+KF2Y4MbA2hAEUVzosnOnBbIv0DK/UvFtBNsAeQOOYhjule43L8qO8GrlT0b0A5T6rhSXKvryd+wAPYbcpfvH2hA5qoF2kvL6TIbrJ8GbL24zZSP77flYc2yUDvZPKX7YVOuqmhfaU2x4g1SjEkvE3Y1nqu6KAORPhZqDHbX3yaPjdUw6HCUgOb7GCBXgwmSpMhmEJ45+ZUbkT7doyW62CKJSEiwreQ+cGixA7RV6rtSn/jhc0uc60kOMgkvMbQCfQ6OyXvqL+KWyOM5tHI9mUFKap+i5fx9aTPHPsVo80xoBOjU3ruA0KMxSzmnCIOhkGY8wp+NUwpK61x5B/27WjeHkBSkqYmRqFnjyn5gS0gKGpLnLJcLdJgwrCJauz68syVuG8G+njxiBCQdE78AEDMjATNlDv3vyVHXqMTxeH2jVlSLr3TKs4Q+SH/Isz8fxg1elkwukt+gTrwOz5VDPsS/MyuuenOMS4BguKIjscV6s9AZiPLdAPqgH3609BhjMP7tdOBCGaaMNaY2RQBEHo4QFwwHAHZqw9Jz3b2EpKCvJOZ4dEZceb8JRhnXm0cOdP6YeviKLobJ9N3fI0xwh3r9W7Dfq3xMyIb/p4ubl0hlBHIQwRSD0jCcurRirhU8TDZEwnwKfd2qPUWp2wtOmXuRjTYrWr8g15cre8JU8e+iJmhBkGijRDcT47eSkMYsUxe3QXLi0J0l0cY66KFETFitPkq11nwVUT1qI0u9X1ckfqZG3s/cLZGU7so5HhhSUInvzahHOY0gslfSFqG9uxJcqtD5XFGVS/YxxIDxJ2jqy/p5LpaiGweVscMUznG+1eOAp1Fd1fpg5UUcp2g5iaVcDUi/Oj8UkCQav56hao1k4ICbkGoCM5NpSW47akELF1tAcI9ND80T62f7HRxEEgpChFWyOjudCyxmTyYunawqtc7YuSnE0miH9btvdOBaqnYvMSt6FveSHaae0Kacb5AcHa1zAoBYARK/gE53hQRxfIeCMCsfPxrpZ9Tsk1UkDA892iQfgzheNVWCsllQvhVlXLefQXsfwfcrzNSaoMPfxGDKd3CazvpRTps28pO1+r1E6Mj1UzDMpqgPGXU9QvZO+uU4H8CovzsPy9+9MELitgOTQXavO26/T1jryw+xXkQwmdywDIL7h3urM//UllRILPOmq2SCRfUqn4LKtuqkOTQbooZ5SQb4Wyy15AQrAoYgB9TK8d8itjN0uLcVs7MrIP8Uu+ISc+THLQJef+6n739nQFMH2AvfHuS3j+WyGwcDuk/yc5hJ0Z1/TjU6UgzNQ1i0r0ECIuYC6NyopYdA1VVEAjq0oRrEaM60AKcPwpvhXXXJJkzVAICb1lATTJ0nK/+6m9JC+OjP9IGyz9MtxWCSfDEoVlAwdYujEr6rK0xXSMEV3b53Qn1PUt5aMpfWboJelyGVTH1RBo8wBwQX8yGip8SYmHaSzNUp0gHRfBB0YyVPch8uVu9MiefsphUSJjDi5NxxcONHbcOHtiz552h4Cd6oJCngYb6yShMNQMWtUM4H+g+MLyLgumKE4UAZNp7ZPiujsHmVi9LFcIhcKQXHq2FHY1jWmLiI7mcQKmFwkrPp0v/mjq9QvyfdtxSftZgvuBKxo3nYC1gY/bBmCnpvgxfvnce62wehx6AUn8zTgSlTQKoARAamAgUsuSOT2J8lWtvQX6ilM6q2dlu5vd3nGCzB7/vhC5TGd/A4BxSA6ozNiUFOw0peYm0OajoJGCJhu4r6KT8PVOuKVrOqplqvZf+FaXhD+mc1zqPcCZacuBWjgea3YabYQPZI9xRaaVLvvixH++tFazFtZZJbPG232zQFwLRRCIDj1pubipGcAkb8Tz9nlPhaDzqss+2R1yI+54aod7biSjGx3qRYmh6uPxPKyuWMn9wuTX0+Y0HwIKPxv4Ssx8pQ5FR8pNL1uDAaVIhGmAKueSc+4CEc0m/mtZNbxnl+uMpL4qnoah+PA7CtrI4X4IRj9HoS/WzbITGlil41jPbl4UsG8UXJi/cbEw7faCcpG693OMmIcXKaLBqmutbIrgg89D2Il265u0ut6F6tHzBDUOw7HItWKTNdVH+/NReNoFqOJIZS4kuTX6spfjohkDoi42F1WGJIZV8ZcwlRPpVnLxZNS/O7o2KXYoBgKk+IiQw6p1kwmTKCPx2QO+JUgiiPyRtcNKwsRcXIyYwS/LV6FV3M7Qx+6ZwTNmavHielPGOni+sqHRFozBBoh9pPktj0tNgY72CozfYm3qg/rb0f7e59FjgEjTD2ypvx1NW66b8NBkI6pwKnBwRATXrLWq4uUaSy4yjbqFa0cOMYiv34yHRvAeRkchBzyFJdoTYW+SvxgB2BqS68VIsGvMGoEIRaDiT5sXlsj+NnL0jslXhnDzgqdlDbNqJdXSzx5B4MR8ZQC0S04WMcK2Vwqn9GS6DRMgo76C78cxtrzw9Z+fM98uTnAdc9IFpI8oxNsBLnclC/L1Qduyif6My8TyAlnIryW1SWXgrzrcUGKKBMujmDA8stdLT7FfKKHLXXEQxHdRHZo0Fc5HILVtT6/5XKRoyU6gUqK6Jn8IfEkmMdXQAJTAI48rpvKNoHlxawZ6H2x0oXFk/t0EB8bjhnLysotO7EiDE0g4eJOEX7B3yRMTnuiJI1mZALHMLhe1C3JYk36f7DtTzXHjNtClI1SmOGs7RNdt+coAPnSmMPFC2Hhddy3fLwaNyUCGxsgkDafQjPfbCHOmFdEWg3kBxfZ0F6ShFORVR+U24NwZCYg4T0LOESAArK9e88KeoIWh6nnXU9nI/GOtVoaaxcElCB/uS9nDSUE3ATNGHXXLRHGYTTzldS5lXY2tRTJM8JEwWV2r/W4heI/V2d7pJnsyLLJ82Nr3nOAj8xsCal1z7bHvabgoDtDkC/y8+Iprhj4zEtrTkn04K0b5R4/y1PEWR+j7AGX/Ulw36Z+E2wS7Cw/ERdqkNC1dQEkAI1m47J40/bhRxnWsTuiS8l75+UfcjXExY6olghVA9NXuygfoaGuFKB+KPP7M4YRS9ktMxs4BDVPMfP0r1s+X2Rk5cqerXUjPPqO+/3DekuZZcBSbQeABbZEFlmt9E0W8q2PIfDaOmxeIIcZ4MkUMzXJxFtGr42dLRIEGwh6N4PpOoewaLKHf0cwNHcnZIB4vN5ErUTxKZwt8lmAHeJ7AIPBLHHHrlc2713BID59s9d/sG5sWI1IQOkqVFtnr8pZPwWG6x8n6cA23aWpw2s6Pv/h2Iu4qnO+HfO3SFehMJALxyYPvc5d1Zw8XJpJ+FWsuJAFHV5CJzAVRaaszzgNqF1O8rjV9+GYiTGZj3aSRWjpB7TLKKayCjnLbbc8cjtWs3ZLbc5yhJo2OdfG1wtE2Np0GZ5/6dyho7AWDGIE3r6hOJS8HTu8gfPxP+uyWTJz9jRyHHxe9PhEwG0z/8sU0I5b5/SkQphhrLIZ7pJEvVuJ2pT+eIYBN22E6f5uZnxvAUErbDKoCdqloTkLYw+g7wQOCkLyyc85Pb/V9Tv8zgVnoG6VRORju4+CVSkmVeRfP7aj70agLIzthhDciDeoFCQ5aPwwAtPml73HECY9bJ3HOX7b+71HL8ss3n+tQjEdzELl+zGTkG+eex2VsC47KcFx+2JWrisb9nBt6QuLrzr9cGT+SIWkFHVfgpK6zMRQP7rndvwFKKPgUZi6ZzVJbL2DaReisfumAacnBkGc2pzsrpt0LKUOo6c2qaiwTWsTaNP6XeiDH0ywf5D9fNxMg0ichF0VUiBmycaE1McnIFVdimjDWCgwbOHogfACXehJg3n44cLCECNm1tBRax5YKIs9O0hwsjIcXzwleYZ3JHgot0sMcoFiYlhMosU1GvIRsbXhTJXvkO4DeewH8OjvH1gJcVWWXEhwO8Cqr1vr/y7dhTphJlClJ9AkRpUc34g84iNbKnUYwXu1abIZXIiokYc5Dsz1nBvIGoprszwSethOOZec3U3R3oYvRzAgl9CJX/XQeLxqcvruBAlh0E1Ge7bQLdkUaLUNvWoStnaXWUIiu/Wv2v2/zIa0WHx71xK7zlBygCH/GNvCd9LYEOJPHVfcLQDFW6nRG+rgTdtETnwEQgq/WZ0b2RJWRfBsNJk3b4HTDPz/fvbhq2r/zSxO9TtOxn2ngmonkceOXqy+1xe4jxfnhwQnN2PwWnhXF+3xc8jVxA8N1OyiD+8kwml5TwSq9XEbqeFpag/DvycR+MErCtb4ogV3GAYPOuwea56EUxYD+9i5Ttmm+7hYNqYK+j+owik5kAxU9aaAr9X5vE5dsvn1ID3BOqbfy5gY4gsKzqVVW26O82j9FyEEcwaEjcfVKycMmG/uEbxGHoRNYO0MzjsUoErYB47/8Lau7SYBqWOcEfPaK0q3EucAY9wG2Q2t6Hw5H2rcB3NIY9OpQAwEeSsCYB89uw6h/nNSsyNvP5pt1YG7cE639ZUh5D33/T2ITnaAW6An0Hg77ALE/QpqJfL2qrgCQQiZiQc4XVxJzABxjN1ziJrRxPI3QvKkjMruP0GcqHU86+1QC20jNNnwZNWEza1mLNYtAQFUeWp8O0dNTNdJRHzK49voOd9bTRXH+I8Ngx+ylXBhAvIrEIylcqkFDerzvww7lacUdFqv3NsTIFF03YwEiSQlv9ZS7CBcDaujPUGnvL1jtAWw/OK/9fbE0yvWMurY87h2BrRDKulNGdx2CnsQDoaZzsQBjPrpHQnJZGYEbZtOY4Inq7xp92xUDBJRsDd+8blHslPQKmNwJ0fjxWPRnT9kl094OZjGPbj4Ytt2gz2qO9pS8lh7HeaDxNj0IyANxCZfl+AvwiUwcEjhE6ergJMfKb1w2uHmhyzwq7Wjw6lPpQJifT0xrc9E5seM0HEpiozCPX/L8Az3QIRTmlZyBPEoWIQxJvO9AQGTd2F3DhOJqWe0AO65Qv+0GDh5dj8wEe7bvrlXDPtPPUbmVzodGreZ1NnawRKCLIo+S4ndt7IAEhfEYsnyUb/rsXNE/LZ9IQbqtUrBJDbjhRkuyITHbYgF8v6vHUNv0fxZenYy4fYWjU0HPHCFHk0hiuxvMYfASX7seMOTcSmtB+h6Am7WODdxgas2/BUTZiOEZANcPTmAehz0wAEfularVpshduAwLBU7qMGEBJB1DpQjJdXguuRxe//Gd3TBgJSm5YUsfYLNHhJvrDiDotHRtThWeObdlUFITKUlnr/E78YarLoo5c63Tw+WF36+FoRk89xm7HfQVy9locrXZ4A3qK6QVGIhZXPzz0dxj9eZ/QUA56rCTZ2sk8Oud6I8pxqp8O/qZ/HoP60/goSrblfMvSitmKBaJNFqSr0P03HPk1xJFnDB1R+7/LPVZWmDkRxxhRecs7Bhn5IEakMGeXpKkr+fskSPyjrwPqwJpwXTuxWfupBYBEDkQ3sKx6b/wnKLG0xzWMrU+ckaBY561iOXx4C+3jif+Db5T1AZIp0HfdN1DOUpMv411I4DHSmmt0V7lY8b7hftkrzA3lLG6YlExrtY3SEO+IEN9RLRuf7TsQGmsTSU7Ghf1DfZhKe5ktW16xBtubV1tv5ucpQEO7x0+8Pr2o8d+cWgMHLwPiCcF0g6JQib4ceGIhoIZMAmOjwWGE+q3gGn/XWI7Fw+NpLkx92dEBEtWu1IgQkt8bUKaeIGs7nr622eL4Y+XjktmBU6naS49eYbQyIBv832xDE6cSrvqG5B1ggTJVGZOXddkAYrL2fjYkU5Nrz5TEyw1kC996x5TtNZzbpu+/oxEzfr3X3eFNZfvVB3OLr8WBFwhlie3wG8nxJfrjMCf1A+xIYkKMdHW3Yt4rfuFAeP4+LFTyl7VJvpNyYW98Sa48H4Qu07xDNGo1NDcTg/zJa0DG3WmJT+X1bXf+uqk9xSmPw9dXHscTo4DSPToSLpPK+NB/wFdDPcmsoWeDIzAh4fLv0n8XcL7WTZGOWsUak1ISvnnj1cuAQ0sACwCHE/kY7HHBL03925kl0Cql7+886qBoSSzMH0SgTE88TUEWK7T7voNuSM34oO5t/62Xh+As7/9kTBBOq9J5QUkpPabW1fNu7BVlhzq8WBthcEsf6ggH3xfsZFjaMHXZRAdEBoqD/uqKCYfzwExCukqLVmHmk5t+SIpe+Pip/KHdrvfqhEC3mUhMUwfI0wONGzD7Gmv+BH6FFh34DFbHckDcU/Um/5qkyyFa1aMHU05J5HgSM3zgLDzODt5W8tpr7Al7pB8bcMGjdb38C+FtHWdKugINpHod+UnciCWOsliv5HvCRgZeJE/hHGMSDHfe2z0Jb2t+SZth/xNOokiYIFY46bQZxvcPdRm70M8oReF3XKXO4sJKXvdVxMY+EUvGfWjHXnrrAlyHEhDZ83wVENULpKZTglwR0vuDSuCz/Ud4r5A5oRg9JHrPN5xQWJrhtH//GDweORWm4FmZSorIsBhTLLb4AkXLTvSSOQjCerU2RkahyvSatwnSJ59OVNHJaMp/E0XjT9ugG4XOIg2dd3YMAgDodG8SZAtpAbrZOEhkvcHQ8rKS8jsm1eRIAEv5Aw1n+vFb5Lda+9Hvf4Ei5Qf+c9adHw6SB2s7NaRWzKfXwPudq14R2GFJXxTtBETom3GBpEYGFi22wublFrmpOod8vTasqcIGakH46RMbgFiarvHB92aoHWSzaecLGY6+fdZ1z3vCi5/Oyo9ytJdD7/rag37+POTG+PMS+nxZw39te/DnTZwFsC4lEHZCww/t/5VupcGMlLQdXApn9FDOJG0otwJOTvCVq+JZvwkRFTxbrazSOIkbfT0xuWCV6OtUg3r7vykU6JMY4I96gQExwi0RvtOCRp71YjnVAplOSwQ+qd4Y9P29+VsEwXpJcefIjnxY5fdJCd18P8mqbNBDcQ6ERyxLrKwj1XtgV/PYaRlFEFJ5Xvu6C0mGhnC3kuprkbxg73wC+NBL1g1OaMeZeFm7eAEH2COA+xHlBEDKpZR6+AQBFNRYAsLNWCUiCyS2BA0HvR3rwk5EHgjyd+tyHLgSfg3qfvzH9lNpGuTA4yA55NoSLV6OuB7KfbfL93fIRH7dpcQtCBX1eyMo6O+ZElDJlbHuoWHii+SexFImhxh7r9+zrXZA7o3QoDKmjWSynNaeQfWRYc8/ppdFo2d2JrU1/SVqSyZXT2hq6i43Gg59ts9JCO40+jnScPHYe8aRlF+QqK+T+m5T6L1hmJb1OCOM3GH78cQsT6oZFe8oVN1OgIIuzRqceHs67eoh0o+HScHQibjXQ3c/50bmG71E3rz8pszu0hRtT9NfEYhWDkIKwIY4Z/dFwfPeIFye1oiWL0M02cEeavZvx/kSJO/MFD34jR4/JijshrIlRxzYUULLhnx6UO8UjrxFeBMeef5OPqrBdDBbcETif8JTHWSzRs4uGUzDqef22g8Q5/ygA9KrZLndW+i3gHk9J+gzoieJuHO8bhbH/POakRANSLU2sD/3LE5QaT0th6vfyuAKGzHnzYAP1ckTnJgOAUSd9Id4/dvlbV4l4rsvJaiFSysTC+sbtwlwMbecWx8+ZQQSvm4NG63A17yZbjkgV5r0kHiHdt9S5DEz6H1BRYFpCQTxtzuASOK4cUMMNlLlNdxhv/mmtJON3Pdhp+WkhlwhjaOSuzoaTxVV9g5bxUbmHz7Zrd8rZ0PIb+mHp2cLgpOAy/6At03BsMkVXonOTU1DZ6o+HNONWA/bMN+hWVQg6WeVwDWJBvPZ0daFCXhU6ixXYBPGG/CquEgmlbXVAWPrXgufcQQWKKHA+iANtBLjPAoMypv0c5U+8uV7PXCXmCV/C50XhD+R2Zyq/c9UPH2NPqJEw0FRNH0N5bLX4hqR41VBO5YVU0OZujcMn0Wrmk+jNhWHx+5POYuV87bG3BUD4jY3gIioFkNp9AKsUI6Rb2FfXpsYi2gvQy6ju1JCMzqO1Y0MnIDU+cgahLo1L5T+QXKaTt5QhiwXfoO1ZUK8e6rBfj9CBTH6I15svfK2gNwCCD8NhHv04ACZ539oqf6JWN1bZif9haEBmvxGuK9rGpQd+krhFP1LdSu52dmtUCXI03uy7q1ZApkpomCP4EWvEoaCfWRK/jS2v4PHn34p1cNf7jQ2zuEnWtdGeHXkRzg7/P/vtzu9udZ/i7PVR5dHRSjzeOSxrc1nc5R+aTl9j3qYjqz37Lo7DyK1CIwPRpSZeU+tIrL0crgpjAv2siMqPcMihBPBKt8848fSu26HIAQoibXpuKcxldEM6C9U0+Bi3otn0Pr9xiORLbKEHYXhn+BoiihvulMZq5YWLfZqH3Rt83tkh26Y5IaMM77+DUKRiN44s8UN4n6UIWAXlt6pSrqW0BtZWKqVcF3WXSqp2fxKflB2TH3+vtgCAO6XvpEj/pa7ED+6HuNPOFkAJAnz4whef1K3X5TlkWp9Qa8IMOH3mjfo3zrxHwXbbZ5620rMe8EJjXYR9OGo/PD3osW/NHIacJ88aKAck4+D1NKL2L7gWqQBRQn3kept3twncrhtEzbM6JdOGISID63m+/974kFJkT1H8lOr9ZSkpBlvqY2+F9una7X8VBj75GkifcXMbaWHnh+TlugVZlWldUJb2uDGZl2qdtNEsHX1XEi1+a/iC050/7ILbOwwk/sapMpadddU6Kfuq3kRSV8AquoRcwoukwaJ8b89y9M2qlp2sp8iBo/9TxBjcx3E7X2TTk+eRG83pxOHjMgQRmxPHI+GgvzHyXbD6/CT8qjPzJoaG+K1v0KEzr5ICWiOcjt55vMxyZUaLpv9BXV0C0UEml5cMQUkb48OaGFM39BdJ3iWcMbINHwwC6I5gaahGkvEWzWrO7HJW4o5crkfQKXA+f7xwFN4X5Xh3joqrpMeu9Cam0cmjPM6RLv30usq//1zEnCN264lfTBMl6wfYeQK5cGzmEYkCVNdrxmtQ4LjTGe9fvYEtW0EKfZtlvG0Zge7ZmVo1wn7HgAmmIP0YAV7GXATbBabzfF1eXN6XmvsmnjZz6egoyf4rUsdimnFNfcR29opWwUW3trG7fdDBmkmo6ZVwJQru7ITZp4hKsvgTpTmGw1QxpUlyDk8cUPG2sCQocoGW+V3pMIhUqKtrBp3u9D8x8HxDhpYa3p9uOBmiy3mHnsthZtIxwTQSHu1KEVq4ycoM6/w8sS3412mv/ZcSLZAI9i5hXWNQ4vCIRNL5ie0qP76pHYhVLXfwfWjZ+BJejZNlYNsB3P5uYRmesjoWf2uRmp3WdW0/as94hanw8dUKm9wU1KTlqQ/6wsOdz31NaahMKEpvMDZLvU+BBoWDL2GEBr+aGDVMBfIrF0OX+xLsG9Z6O6MRn4KGUMelhApxMnGdEKrjvri/Ed1GLrbrjnrIjt5JIX5w5EOXYFZnO9V25x1znMQJd0MIImgtE8alTXvmXrpSo98swd6gui7WuYT4n/AoNBXZTolDLTGV08xpTxcfETLgkRRJ8hBqR/4NU8mhkoFHZ1dfa1B+xfwMxqy0x2acNxR2jQu4U8T68JsjB+L74gbFDUbAj10ULVTfyZXWUI1/xKN2Y51ZSy1kUzuU3EJ95W7iLhtrCk2aJJ71dXBOoEBqRe6r8gtQNfvYa5QcBfZG9bYe1EeFvS75TWtn7PGkEHHv2mXVCkvQugnneDusUx0pNuPj0pGH9pZlrFtu+OxcbWyCAI/ISVEfO4ncju+qZYR1ofh6jwJcfM5ry8+3xLjfSREW7Bx57KHMvNRi9Enl3eu5yZMImoM3dFQ4tMFpT+qTgl2hnPe7B1Ymmzt8MtXpNNljFG9fVaj2H1TAYlflFSR5LgKcrHgA5drcQHfj4Q4vX40sEWW/kY+xaeAVdUAad7JK9zpisGSCBoQOsMpI9TxYUu2baqADhZbOlx0UI+Yrv9PEWcDmYFnvuMqbw/khftce2+GCBHsi8p1WzCiFrCiEiAZ7ZTf2V1Ga+NWBDp1VxkyoyIbqdWxnqXgmuX6jv8wWLFWfQRPf2T06nPKuNSdQWbF67nTg6B/fvD7pe+ycNsNBrE11k++IHcaRJFD5cS0w65Yf9CYR6f6bM28p1vSl+iBvmgBs8AWGVtxm2MlS/iP6wNQB1m/L0HTNRg9Tj9RFpEBU+oipvY4Xg+yKXQiRnDXgTSuP9JEIMJY5c+WEkwgIZX8AuLxR0LU1xfPF63d3etpg2tQPKWUY42th7NWhBI2KSb30JS5aeA8N2kJxUMzVj+9dngqSMJD5M2Mry3sVSz42Se1yF/xBhzwTc8CvaY1GKdcxtB9O++6c8t/iD4+fwo6zbG2O+j195FeF8Apt0Ym74bKtP7mm7Ws3/wr/sDBqYyHvdZq3mV2li8qyQBxQEX5BPYkh6qaZEOgOQPOBvYFDm5qQXRUJNoytPQlPzvaJB6RaNr09vuJFNvQ6/FA+D0jIomSjg58/D4pG6O/w2M5jlLhNXAMWWPvrU8uo3hdHeZvOKnzg8lJpP+aWb5HtZy47cSsVKrTw7kYrZui/jn0qeKZMOWf/TsT1XG188CSCb4N5i+8ixRW6ZMRtbeaYVlVUgl0jRpp8U1i+Z7AS7p3pCYZJ1gmbbJQPE6zBXOho9JaPJq2KMsCkjNSicFAsqk6U3HUg3p9ernHA6zjtdmz0T2u+3NCO2MgbOv4k0Aj2mXfD5B1SCJHWKUA++tsWulseELy3pD8tStDyGNpiYQYl+rJ0xLlAeXZcXpb9Bl3rpHateeGM4Hsq5DQvwBKn7/P6VbiGLem78pziwcH85yodVB5MgCsvSFwmEb7jJgX3AACl4MdZAbhfqiglpFjB5tMl7FYFnwHAkqBJ1R9/S3g+N1FX/FBYMlMMZ2+8erdHDVGvACLkspOlcTjCYMvpvUUoTH+iRwTDdqVR8t95jrZ2hOCHDP+DDdZPvk5pMJFlY6KkFPJvNdiBz2HDYUvPXwrcVwHpuCspkfjwNugernzJxxpaBOwlcLqwbt0ejS+VYYCsz5lAX79WR1VBIJud7KkFrD/iolaTiGTBSaO2uBEJ5kfbLdfu5kHi49B/4bDcAyKdM+vgfhij0ToGRHL0DjU3sFsabMeshs82HFcUS/oNSbI6acgRPcUPaYeCxwwGuXbTl2BrqTi4J55bcpdnv4P0s7bJCTNxMsFJ1A1wijtoDjxfZ1Nzk3cE4creoPumgITtShZ8CQ7wvHOwh6OdNAkgEVNt2kOF1suSSJXJaB2+iT3SfubJDP4SPjPMjlWReqrSRw3BLAVsyJ3MO2sg1zQmGEoWck+z8K8juV7cy3yKjt8aeTOBnE540PGaKCCvjXIzlgfn6MIi2QQ5BZIaqpcc4zP1U3k4lY3bIPTDBKr++/mCH2C0mEYdvw9UpxoYS/4LsoKWti70vtAImwfPO315W9ZZNf2FMBKX25pYYoKNJU5eHuTNJHTEcZUg+I7yaQ4BTzdm7f7Scdbh7S2z2A9EPKr/aBwuJHt1GMk1EwI6GY3Gu1YYKw4JfWcjQizG79JUUzLP2wjr1OLel1N0o/UZL9dUN1SsWRTwletfb2bN2G0Q8vGaIOrzxoa39kKI2SST5Zs4LhBy02myH9Kea9pwTGa1JDx1nCH680ETjXU987j+YSnQZF0xqo1zbqQWvTGOAOzPnTokbRt3NbIzPVINaL9ZHVCAqM8J4I/O1wjVYQPitvGReLcK7FxOvgkyDy7oPnwKo7LgCaaTavNFj68sXUJv/8BwiQReo7HLy4Cha+cAjbYuts8uuQmH/wlOJi5ZxHZwng49H9Lcn8nEkDgpgtJsIPs7yCxjC5oJwtLej64r7J8l2oX8phGP07Hcjb6M4KPqjAGcxLqWP4kx1V/IxkslROh1GdhkTmcH1i/RiTa8ymgLQNwNNZi1OkqHB2ZZSIXmoHKv5OxFU/2Rm3k23YmcRGOUKhPaBD2IN2TOB8JbmKJwSFiT8nKxGBuOJWphB/dEAeBKoxJg7z1Vg6zmzXpXf3WZORtJHNmyulJffxbPt+rrvRe7iUIrsE1MKFnPcdHWmC4wf2T5UmoajlYaAHQIucPcsM7hsfsh9HE/evWAMKRXfMJToKUUp01zfD8hmQZelcMQ3csP5BdBBQ6NmLpslEbt7qxgrSvT53MSwhftp6K+ZkLJ3npvA7Ftli3kWrTKLnjn50CLBUWiuet0yFxpYx1HAcyEZBeEy1Da49082m5XF6d4ZOMYvii8vHjt09w7iYTJmONB+IbjwwbyHLoo4RcOiHUoH0QR985Y9CiNJQEBQHGsymI7Hf2QW0FLmW6cijhS/gy+L+m1kxn88xJuXBPXkb1ykaDlJdbCXid/OYxloC2j7FPZrp4p0cxyF4Upjl7/7M06PpKQXAfFeP2uRmCWBaQXkEQNhVUZ3ORKkjY/DcRzrtUuKA2AnX+yUXH42Ca+t4+RkdZcskxFjcx+I5xDVDQyu24JKw6SBoJBYOteYhLebj8jODscep8gBNcSEjQpcVdCUAeTLTC4PasP2BJZ9jqTiS9/isu3Q0gG3Cbo5ujOSfhX77BFjXSnSXiFvCURGUaNm+duDsMdVUCMq7ny2Gtercq5xuIA2Fo3l1yG4d0/6vY4lWQjpkwdU+uYX1TdQ5ulJY74QrfjT5o4UsDnlLV9NPIrJeWrMd1wT8PcDDOM1t2eNiRL6BvRnea6BhmfUrdOCqRh5H92GF3brxhqLgDdga2o7SJYUO3q0F3I5f2VHsN6NRMCv/1DQ6QT5Udy4HyX2raD+P4t7KFXvtqabsVbJMII0+y0u/pvx+HPu8g+lQvVLN9bn1wqMhF2ZQJI8DKP6xjU4j8qT0wxoZT3ac+yuxYSvwUJSgr4ybKHUA8KrlJAkOcdjvF+k4hNRtGDvh7VW20UEcqsgMs977o+RqG9pznDJ76GUB1gRBuOPy23EEO5fufBaPba6foxMoLGHQgB1Zj9EvOgXt4clia23kZrJuQNHSk+0lIaA3wAEF34Ulg4SKuFmFrnfBEfuMa2MVFBc5GadbIf5Jxz7ld5TcH+Q2gGq0mFmtOGpPpjOXMZfzDASxez0A+Nb9cFh7uoSbc9tHrNuhzmvRDZlvbQBVhXLL/dKUXn1VGmjgY3w6fLJ56GCsKHRTrW+Wp+PorYgwWqWcFuiMSOVKTC+ipJWwWTsQZNfQo5k/Za4DaDwsigzf2NEHZuZozqShxsyzPLh+UtFU0pDrUnVkjU69X4qYfR9kIvKEZ/JLGeosM07SZSKx4kMlTWB7Az9OF3ZNgEnSTQgKI5bOZXPjMCGejVtcTS1cvUvFaVTIIJbXka7RrYRvrcfGP2rrUtu1tviU5CPINjIvFg6MR66ws0YhGy3M6wWmOo7E8+dAXblE1dakPpn+e+BjJR8WUt2910smWS4q4QAztZUe07EKrSTn/gz6LHZLmUxztHLoUibLU0XhJfZ4GfpVGzxYuHo9UrXid9dW6FJLIfEKgMbYyqpZ2zFc6TCtAA78eCnbAFsegYR38JI4a5OmUKkScIS4aCxA8cUfJzPfmg5wz+vAu5r87ZNBmzWTfAZKrgRW5jkrFW2CUtwwXskZR+jap0K3R/gr+3QgxbvbTZ1PVyOfL7YODMhzqdiqQFulOcCxZwM5DfILP7tGdhiWiVBCsvHa9EVysbjs3N3iEu3UyCv8Md3l2060iANE8PT1Cw2uKtmIe/6brLinPjaek6cIhjJq9c/TJ0xjRyqyMv3/jNTScVQN/JxsjCDZmvBsnkydYywyokoDq3RGeN3IebO+ZKct+NFpJgS2K978WAmIOGZ7dosRbJzlpoqP03YcI6cHW8XDusXMJw9xov8yCD4+9QEnMjCgx7Mqi3ayqoeuqe537Jss3MZD4DouxMzSGCMYLlvHXC3ULgG6052WYQlu0ieyrVDiXHoUQANkRP1zJfemxdmSbEUWQU2yGUUjGoR1JaOR1+Nhqg83sXomOWDO+SrSnshLSEIKpjrYC4B0PeYgeZQNgctV13IV5ZziKfvR2ez4OkLWExccbmHW3x4Y8tSbg68Gk2/onX/Vncr3jkLu2Od7bmei5+FQceQgbssNwnvO70pwj+I51no1BwOhSosqV2BiF/Pk5+fIAtsFwffyEXmME1qlmrqyXxA0VYjZGoihhX/zS4Aoly4zW2y59odqGYEd4LCHRtLZ0zMJ91KEolckVCvZMw4d5JWlEf+BjHZAtX+UxhfPAebjPY5wccETYnAiZ3VYz4JEHfU1zmxzlpv1TbP2fjBVvrT3XjFnBHXULAuBhVJbUPINvgNh+D+fGWqnu9tP93YShHcmbP3lxc3arnIXrWwAD6dap3W7/y/pAtnDC363OfHlHvkFOAjP79OKKSjXeO7BtDiJaOeiNYvPkefLmtxAOMBnfjRQG3ozDAw/+v47mmJo5EbHlEHVV1nAqDJKI+ZEr9S52ZupxhYZQG2/JPV8ygUG8WZUaf6sg1RzQph9doA80ZScLqFiJkZxR+9c5yZo8iiF21RWhir2wz7qxOJoi8+P0fbpi36LbQ12QM4WzG4hzAHXMtB60kQRACshEK5Q3OiDJzwPAitXz4XZHXYgbd2bCdSCFddDpEpO9+6Nwx2pE0Ji5cDTIOTJvvtP4RuWscF8TqzsTNkL/0t7yTmcpzs8T1O2iOv9edg77oa7U0ChCfnxcNkR7doHIhV4GTFUxOWgH592QoRMpcrwsrZMMaXoDLU67mNaOZZwpIb19z5GmVJNMP+rwodXxpPj8e0TR9DpBWCBpLDPLevKJyXCv4BDAzT/aZjXiRtj3bpImkDU0X595MlvAWPQk6UnJq0neT9b3za84gHn14PX64Bbr1WK05WXI7J/EZhZXVF3blMjs9mACgdKOlJ/RDqtzzwOoDxNeLUMXgDANUjRKouXC3Cmx3OzWTt0O9Otb9//KL8jfmBQ8rwJi4UbD9QSmd/Lgq2RkzibgKip4lhK23W9Z1gM0iY2fULS8lIaF+ButuEl3BaEmuIHWlce7i2Ly+fwLziEXVzXd3SaMe2uWrHP1WDXPpnL5JvsT70juiqnhNTiaCbQDpBwzyIVzY3Gk9BYnePnfVWDKvFj1GhVV+V4unSrc+FNvSvIJEOlEHRdhxDNBZQEAEjgq0e+K99iWtfHbJV61KHC28+RTjKLMRNJOshb8Kj83Sg+I1FD+FSS1ZVKveX1rKDcquj4PGoBzWza4lHe3fRib94dSSjbvL4A7QBXzHk2yFpdBWqdLpka/MzX2b8fE+mAUjj2umGNi3AO45SqNuGPM1xy0BEXM/2FI5k5gEK6mxZjS7d8pK1jxzxxvInciV7E0J393J8A6ViR9N3PLYic4fVHtHbSSv00O+S42nvjzSEh7ktOos29V+PVdcLA/pb6n623CVatl6HZspPNnsf5BZbtNCUOnaX/JC8gSkbbsies+vaBOjYqqf9ySRn80Og/sr6qG8hNbOftN/eH8GZf9RtQ2dnRXmFPiesb9c7+Y/sfoyWuoIGu1Z/bhOH3v8/f75PL/m7LoDZrKyd1tzNFThAn1eA/lvW4vcIT/3SyyoVIbtTD2wCAEd+fZjbVNSAEaJxqf8Zb2Xzn8LUOva3m7icSLY4uJ9mwUlcwnGbgfyAegCaruHI9bc8dREnw9hV7kmcJM1KtmE3i/W8PzYb5V3Y3DDXkYD+fJ8iaWS7oas24ZEQlOrldnQdvuCRj+sC09N7awfktQhzJr6rI9ZgZw2Av6x+cd/BhOtbwIgUxTOUjXCEKFqwknL8X/jlo7qqobYFP2NTWKTzcUWk5a5dpZ6th7H79lYjNiXF1q+ILRSxzZvnQF3X6sYrHXMe+WiFJ5kycd3DpPVCaDbutFE7/QcDd1J89lmDcqmG1kpAQm3pu+bScL69dN9jaD5C9TdyDO7cDV2jT60/AnP69S9EibqN/4D93VB2VKIw5+Yl5D9IPTKjex+vX1kjbaXXs/pymFAx22g1XXpBjc0Aa/e/Pdzwb23HAovHSjJUkLQjgmtci5m4P+hfIpNch/1KaqNXG2+C3QY0tHnVPM+jne7iafnBgmUoGu6PlOuH7kID5rv9zJWCH5RTqWuOIoneChP59pdzSnZT03zzjZ8Iq/hdWOc4qsxfxfhXBRbqkGVoSmVYz5le//wN7HaPzaQY+SBCkxj5e6ABedIJrn6oXV1UnWpUQ0qnPczc5CwItVY767OPUUSr9VSEkWbfU2GutGUMusdjek/5IoCwf0bMGO6hbBHKsadYlxoY09wtSTpm7K+ZSTGuc8Z0TXd00v+xc17I9owxPQgK/OZ0z2g/svdJdLPz8osNVLWFCsdmUfzxZvkmkHt5OobgA1+7kWPUvFtaTyCX1UNQ531xi10bb3DARnklxaI68Di1e7uHAUeiXJ5xrrW1uh3LCKPfI10nsQMEa24/6xs02+iSFICAYoZldPH9hPgMPgSOjBGrfxjTPJ5Mat/KTgVVfPDNURNnp/HT840d66dkdJtWoIC0jqFuKsdlbp26eDILYeLvv129vdS9GYl3aiExARjuodMSuk0p35NLs6ZUi1brQ9bKVhagQTPDk2SpNRD8hhVxIgAcRgMgcIHDlMyeLxHF/NJjWSC71AjcubJ1Ocfpu01ulQ8OOaXs1Rrr3cL+AwTDOO7nq2JdZDktAkvfUlNRu79mPh13FflkobCWiompcaVlBd4X3u9dYpUAx7c0M3M7AKxMcF/B/6E1KIFZuz/6yIguUgm5pDLpe6YGV5c1VywpY3kuSD64wnB5aES1pDuCpkWDBUFsBvHUCposlcvgmLc0gB8AotLLlvXJZMwm2npx5JPY7TPpZrYvU0LQYf8M6BzLXQLlsF4gctd6ySrsmdpN+FNQ37xqLkx8o7KK/e+yhsS9FoC/jkZRM3dDV84I0JRhmNZL1m4j2Folwt7XgUB9y+xwR74bYKzwzQG3IcMxxG5wVmekBAKLAm+haJtywRrD7nVfdpK6i9xGDhw01l9QfWGKcmNBv4SRfYGGG/y228CJFO1lg/YBGlDJySF70fVvXmvI+49hi2b+oxDz9btgTOW4uNdIwIZkomljyW/0JtAd1r8z09HFyeEi/g1/X3Thw1jJKwWbLKSmu5pRXrujRl/zeKmUNxDPFzxO0mauBRKzfHku5aCxJLe9bgtY4WiGcrvXALMS5n8eZV13SHASqjMsc0mMcUxfexAoYmWmYcsrgJYnSlz+WAxFGcg5lF+ufsHSRd21aeqQ1o9n85nWJ75mqyEuIBjd7OcYuwOEKhjosLBy0Z6AMqyUYomH9Z0s5VwvbHnqXc3hZaLulF9Bt0qr5satfwDNYjbLdujW/GYo/lnlbtwkOBcSZM4H8HsCvAfGXSIUpeQ88Q2JXtNqkphJphTLhDzDKFVkjMQrfrMRNj8qUgEhEjLhclxyCPsbKUF78eoIWr0COuv/50ZohNHDWt9e7qeXgSngkMyHeM9oXfWotopJdy4vCRlwqD99v6HJifDTciSxjOJWg+H9UDnwuI8LTx8mNwOJbTClyRlLuf+H46Qz46d0Pg3Of2AbcRVgvoy5dsEozNGzHt4qi0G3ljYheWHTd7j7W6++G1LonebFW1OuKoNo2lE6BRX0kV3XJdanQqqUe++ctKcqIeLik32FbneorMaiRXFOXEiShmo51DtCmZ/5+/+WtwECcN8Zbsh8L+ty7m0iaTI3dN5RVZFjRMTtKx2mhbmDPByDZYIpBiO4gMgDy0LlsdXg4M86iRpRm7MZw9emJ5upTKhDzhO7UyyC0Y20ScRGQBhrfZC18hFqmdGkYmw23fmnbw2EpnkVJZRPjFA4sxUnJh8oBaHnjMLjil3fXFtw8gfXZLoyVlirOIhPwr+3ewWDwp7t8bFcNW4bBq3LKimLTPf/TPPeFS8nMsmId/JeKfBAhZQHlgC4xLm1NefkXyA1uqCjkgpmpAk3ANTCa7N0oh0Nkpa+EZVgJGi0+bf7R3KcVMiGkTnXg40UdaGX8z/Ls0hXH8T1oruKX/qLY5Cf31vypZQovJin5+fi64NZ8hRFxYHTISuk8nTlx8SyJR2bYBWL5pukv6uxYoy02hOBKphLWLXYFCUrzT0HayNMR3juSak2Om0/MixdMiGxddF3voJ0djyuJlieIgG3GAj7eVV0eXK+adL1zuQ7sfsqTrcOw2ASYFrJRIAxLXilT2JBm7QR5VgxgMaJWLu+GjfxFqr1uwJGN7+GWTgRqBZQiOJbVMP+TGuMb8uTtIgB4qBspUPJ1H+WBRXZKOjfBgZQpW1OkvqI84YSiEcifu45MjEkPD1WphTg+yG9haBcJHD8px9jELnKGOIADDJ2TqZU178WFCv7FeERjTntUqJuVbdbQiyXZRNmrox74o47HVcmbfK8b4/QDdzeJKIZ9DQX2T2x9UBkAjDTDdr/976I1RgE+gZejSiSUTgCmsY3A9UGw3aqQRQjPhDY3BPbGm221RjOk66w9BYSbL5nE2a7pzZKxdaicd551YDHFbDAtNdjUPhCiX+2fERlrSen/2oMVz33+5mMJF7nu0rUX99hKGYh7+5x2aY0araAHF90hdf/Gfoh3hfJ94EgqaVktTuPXr5GQlMVJJW7xvnVCdeKK1Q47M6d1mrUWUY3dNwPwzB4NGnRLTM4rFc5mmArrKPPQtDMbN3P2y3A2zpdTIgDQ54WtIknT76uYVUd69uu4OyBS77DbeJx0SLWhIAtc2l1u8TZ+P+AwiqgWGgCF9pjbizi3/rw2lQ9bux4kygX8r4vdC6HxFC0HD0wqnU0JJnKEI3iKEidipt/iKJ/DcVLjYrGqNxs7ZkaXr0D4QFjIizhk381u4FpbK+Jp/HmcqDaiuahANDiWab4MmTqtuMl7uJGNW+Q5AzNyhjTFbBnkjfYukadJo3T+TNab5wHDgWzn+Hojl1X0SpUqlabzHCQ5aUaMa3+rTbvJkdKEKLxC6/AeM3R90OmMagxWtdsegkuPIAxrmrzMS7nmNqol5Va4HXPQlJmaAlZelK8nRn3WVp+zdFl7Ttbs+N75Fu8tXMMTL7G//BKE4etEDR87i38XWBjO9vtQ7tNCLKZX54n14EYVXoUSrEpP2JCDHWNo0M2lbERjLBri7oK/0U3s2XabRlisJxUedtCvEn6XQQZeLvGU4SQMVtDNZwVaczXK2i9lzE7FajY/zqk2d4P33oSTTl/FAtgIASmkCc32bGcG7FI8EdOnZcWyQbgX0+Kk8/zbuBTDn3zc0E+WAnr1+SiZIScDV9IKdum3W3WqnOrT9QMJV5dRGFD+Z5DhP3TXY2YTMKrodcpfrYEgIiqZczwqEy1KcpG9vdrksIkrmphc3I3RNaqmziow+uVwvY90hmEnJLsMRr7mYv6lcB9uULAF1ppofsR8frYYgvL6gVMKHsIigt7V2oLsw/EAIivL53SmOK4HSZB11yF3AlhNwLSXlmrwUxplD979cCS2NvqfY9iIqcZvSHN9Q7mNlUIyK1ZT+NAN/sRUrHoPpxdQmNF1QahwNshO/hWkUCAUAjXsl1EVQ+uuW7azmQQ7IAkOL3HUHyD0AW46mzxqo8NhEz48n+5SMBqMvLIs5YhfDDPynIV5oFz2tYM0d2e1+QhVUPnxG+aGmy9KJe71P2ieGYvp514SQoy3ifMHz2pfxy2McVjbXuSgHMDF0IWcVSJuqp5OaJJvzmSo3oriwGr3yZwO1pfrK7PEbMiCgLw/z9lmxzCrwlgK+aW7zVckmlOu7eTRmFJfGnMXFTSZ9seBOoIQJWbP++6zr/VhxXwuY3TJyD6YtdWYJ0mkShldWeWlv0E7a/BZP45Ce4Cz69Gh3WwzDxxjLUiJ9OcsNUyRmz1Ywp10nkH3T7A2NJFJ25sEceDX/sKIYDh92InXdiU0OSHwTj7imdIeZstRqxug16I+DuKZrPsNMv53QbQtw3L64+lRO630o4GgwxRyC+0MX9reTbS41xWrurQ+75/Ov6Va5yYUkKmSuK3Rm0IBgxwtgfOtkIt3YhwJBrVfo4fs1sZcjj5nCFfJ/kM1nqsyo2cVrbq1UFh9h2DQckccOBJol1Dl9Hsiev01/WTyd6E+b8rFdZr9AiVfGmXCD/EQkBNCgE6JjqY+/lP+Stb3UCM/5WI3cNf+VItfyeIwC8dHoYfWVW+iIOl+H96EgA23bo57JiCmDNiuoZ+s70coEHXOEBcmKInMXGHcnU8nwsfI4Yeh9xe+yRTMyMykbRU+GcteaAvjHYaPP7ylTXdBAxcfNwXFkZslTlltBoFH2osUKmqXAaQzEQTr9dmHIs+lQ25NuJq0zZt0PIvR9ONMad2dzmvw1DIxrDsNjg5EONmWIQwJaE8f9pp2H1QEhN2rZw7oOrQDW+Faqzx97A+T3TCO6MKqeYN0JIYtEqy7CSmlxKFo4JDr7TuQAvT0PSp5NrUoxi7kuv6Lh+gaE8MYidVBwDU4tp14TgsbiEptD0OVk5arLAO3+ZuuCLftj/tVYSxcnhq9EO5ShAuH2+4qRNnTjJTMWnoJwsDOw3DGpGwyGxop1D85TS65E8x/i/qzntvb5FsfzSn36DlL5MS1Z0VcUdjJZfKjCWeZNvlRWEC0tVE9bwIuSL80mNYW2X/qlMfc4xoz85F2RbxAuK1uqSsO8Sv2bOV0hVbhRexKTrnuXzjnPsBQdWq6lF0+SJDi75zM6yLmccwNHCoXrJwirZxnFF7fsJwnmPGnIJFzyyO8KJXFatNrxaxq15j7UhKTAJdB15uBMziPpxikJ1cQvq24AUkeatKJn9HlYPmVwEVd7i5YXgAc68ae6rDIDyMFuqxlLKwrUwYBkmyn5gKnI+5FqVWGR+05dfs/D1BguHvHirjeBQj8HZaKsMiJjZ5GX/bq4UFETOhPzW4/r+ArbcCaNBJJd2gzvJPKAF1yzhvPA1r64NvDyMPmoQI5/bPs3noDWQfeU0Q4yO8/AMdmR264QE/nvSkEc6ikTolaE4PA4tejR7DvcUAxuX8O8attaUiqiscO/F8cMnj6snchpQ/iCUFQc4MtYkCiMLwMI/tHtlb5T7TN5hr+kmPCUJDve/fKtWSRONKI4gbc9Hpe+g5Dey+TyB1sI0ahjXGFIBM8ZB3XHstaxCFz5EbF+tEZ3QvKNgeNNOmPl7VM++y12aMUGRP3aHLBk668EA+eC5+DW0W2/13EhjxT13L1zOPRFWLz8cQOzfeRohpJBCKUPZTllNrG8uSyeF/3VyDE2GEkMHDx5E6m4xWyVqW/x1E5t6nZadhYzc0lUCMllks4ACciJsrmS/FgtMf955Zeab+sE1FnaSUNctFBRBb+OSOvNr1bPybGEcfPss4m5syUuORq2IpIB2zRR1tVEg07XWoE94vpq1zWLhvjhn8EEbF3cThuaZiDQVIRqaxxkVRBajcWD3Fa77mttChUPip3VnsiiqhtLJLmfWy1gcTf5fe7PVXmm1OAzWuf1wNpVuAn9GjIg62KEzJ0NX+5sWNauzriV01RiGk2d4mnDqCmyvHiqGw5ZSiQj1UCbs40SlCsWr6tkdB1oPzb4x9p+QRooLMRaHplf2dA3e0gkgv1e0wmL6kREIhxDpgVTnvEnCk0HdqqjXkaufSWdVKKpY3P7/WDaNfN9eK6vU7nNkuTsExjclTMUDPtjl+nVQM/442c8j8jbcsIGUpnijwHlx6mjUSEQW7S5Nl3Hh+Uk2N95KC2a7fFoe7TGBGvP10lrRciB/H5IrnV11XEJyGosxoc+3A4IlAg0G95qoI5RvOSzeRhD4eD72uLVquxvBF4/oIxqMWBvjXCUgZDJ9P3t2GgpC27BHIy3r8g7+p26zJZBwmIp0zyHe9hq+xt279b3hGzEThB9hfvX716CeiXq698vJBgJUqDAckFypsy/Uwi0vSIkqfzY3ikf1mMixn5LtqSI2xsgS3E03KewcRPhV0Ipm5Wwrk53yoouSuln+56rZgK3IDzA4H6/wgzqBYhO4yLsWqWh6/P3bc7x+FpkX2i/gW8du5cnuHWqLCwq8RsOl1R2DWwrQbJnwFlwwQawy6UyyWcQyEt+dqbcc01IGM75VHWFtO+FFnR6oulhfu1bRfBvxIFJ5vOmmnuYy5bj9M628iwnxStwgFqHDww2P5dZ881fA6B9LLWkFw91hIU3OYh3GPNVN2rlYtsdcL/epoEAY/QNIZJ9gXadqqM+gcMpfcS0wb1ploRGNVp/pwyKg721yMLPOLVcZLQ9H0rtM0uRbW3r2D8eVt3Qw9Elt9GhN2chkU7XIbnNru9gli6B+GFwu31sZOJh4zSy48+KUQk8vDz4Fv/F42HYkCTzwsdDqQPw/pJFe0DeWCFrcA4g0t9JlE37FMBRgRg+SIucAiTVGYTPSaep2qTX5uRkucbxdT3Pn6UOdmXkT6Zr+v17SShNOUSrGuW0FPQgtvDR9EPzGfKO3sAdKlOl7lO9f2qaSM3zIeJw53SAnQ1biCquuRY9cRUUqhyg7ieNeEsA5+31pT0CX0oAJW/115crZowtzerWOKdz8d4oMbvT2XZmPQjLyKkiBKhZwoLC1cRCBFTeXrTom5M9snAPPphYiYWjwfTMkn0l78hWSvOzeeIy3uyszXNGf9fHWFmUabGZwj0Yv4pJ/MlVrz2vZwSmygqMtnpshI0Dj+qX60sh8AIf9pHoOgSCTSzROEyyww6iCJOZlmeQvfzfsdKYc51XDWt5IraqxL5pG6goEj1N3wzV5x4/nCIGfzVoXrEku/fwhDEbr+fQQtNVWbw3kp8VTs4HumogOTUL/R9N9plRhCkUDyKX9qwJeDARSIXhvCVktMCGaK7Jf2cjkNZRXfC/oMfyIKDqXGJf7Td55qWrhFvJIgXPlceSvPuTORgAou2qCbePvuP/KMUIzyhDGW9n9G5d/JrMcYu6pkXvLSyXR1+yjU29YO18s1MhgEc2xeiXwGsouophA368g++/k3ztO9086bAuqkpG+frUUSENwTzE03bwUKtau+0uE/51L7WMzWxxtK+H8W66sNkh43qQu3eYNUfxmHs8ks1VbbJx3V8Sq0FXGiIYiSeOpul1h0+LHceptZwZAYCrhtAPLRJMGRwjz4kpkN60h8q3UyqKos/QZRptfUt1fLKHAEYr0mxLLLFcOPBivaAc0HT9o3wIxhhUyw6wMwy3PEef+/Aj+LRMzi9wIbiaLDGDwZDfB+oSfsY9F3qk+egrJtWV+HHjOtKXU9mvpYupy5VkTofJTzo8QLshuqL1tqLrBuyA0d+w2i+LkG7TMw8u7yFO+fXaoHjQ9/sf1BMS7eohdoUqRSaLM1wJDZsGY/NbasEZaXe89E6A0HBirbGTlp39RuIHvzwj73insHuiF9Y9SEF/U2D3pDgfykRuOECtC10khfrxV8NKXO5kzsJqo4ZT0QGYhozv0i4WMG+BKb6i4OvUm5+mhhaw8gS0kaU58F46FROWkvdzp9aGc6JWX+INTawU1tbgdbFKqhIpsch4/5EGdzTseAac8mFHLgvjZ6MR3m3oOXj2S4YyJs5kpnayp+wYiufw+GBb273JWnfCzkSW0Q6FD5+cTzkUW55bR+vhvtkl7RMByh/6ZZUKZ76ZDG9QWbHNEXVNqpa0osleEjBXoCJN3/2XnEawlfKad0S1066AmVROcElmMQ6DSFMuHxjEJyr4Ydy6OZfl2gKkhMahafbKQoAzJsy1PctgK4tp2HnDs5Oe26MQUcHGNMujBm/dzUeAvx0VS4su38wjwCoEuzK9M7dJ33vDxr4A7Rf4dkNXr1lsxDYigk9ra/R0x00AXKRV/jfvNjXEvYsHVYQcVOba/c3hOGd4qnjxBA7oHYJyA5anL81BStpNju+4OWOE/+DpvFydK4jYH96LHGjrIjg7utbSgYs5jpPsCaS7MMg+kcMJN5HudtBOhgKUimSz2nXr+bJ2d98RLM7nsYaT89TydBWhIV0hjFT8Uxay+fJRU2JchTCEoCwm0VwfNrWwv+lgYARYkrZXb+m1w63eF5evoLviqh0kblb4C7kVACZwxN8gwah/ETPd9+1oVLbJtpKXxnW+8FFINNDJ3bQXa8e9Af5LhgVDARGxW7cxv7sZ8ixLQrHsCe505aEyj0Hva+8/wQseAVyhXqr0TKi9jQ6RliA2Y7N8+Kdm0Y+impx24Izy9Zt1CDo8Ai0i4frdJOLuL02eamsQWZ/Va30RCMtGPMX855e1kV0lqFcc+29dkcb9HomfSVkQgaggjXA1lt6wjRUHm2qlb8C4IyDCZxdCJRXYgy/OJF+4so+zeAv4SY1oc6x6PPBYteoSGcnBNFO4usrbyGEheeAisi5Yo2HooV8HXeuxJlBE/G0fogL+DfT3Lm89OyNjrdVZ3pCD7J3b7LEAzZbniUyGtyy9lNblG0iv+iPfcwRY9xC48npSqQXxmsQ4DxQNIlpUDiTU5aWM977E7b5HK6d/niUqWfDozWTlyWuHgWROI4Wc946bIssVVu4+9/RPTB3bmkSleNgY9F589ZvzrtBJ2cXGe+2sZ89Dlz+03GUCUYCeBTto8khavErfE+zQoAYjHljtW6pENj+VMQWm5mgp90uVeefiKObHSUSMsGOyu68FRix0IKxopKxFnbi17WDu+KhdjhBQkpSGwuBO1rn3GJSNVm6xbgqehO8/JrmG+ZwcAiEwyCAXZddOd8wlim8M9lS/d/My01wYznZq/m49puvHViWJyeskea76a93dCo9O1BC+Lt5SjEdxDwJHEXuq6t/Qqb+/T+nUU19QgYW9LENIDcVW65niZe87+oH6TRRWUwinZ360eVFETyBecAFTr4YYFnVwlrYhMWmC7XwjiwVL5RBeJbRek+KNXZI6h4gSOzq2kd+cQ8OGG/C+Of2GFWhL0JK3bL3M8NFSMe+JcF0uQGMN7WicU+F376geSsST6iB5G984PLNUL4sJK06+rbuVUyoY6s2ReekJJfgnW4xG9qRNUl37kSGHQ04jGjGRMO46T3KFuda46K3IhbtjFUpsAWRwainwRiFNAsPHo4HLgF191f95/5hZZbxCP/YNPHSmZoY+tj2gk5vZjkXoFOjA37DKWRH3FYw39OR38lBRRnCGFU1UTuSQI384J/o5KKQOlOBk7wTJngkVZ2mUzNBORlbF8AcaFUXZXnrg5Dit83yQGBAu3ala26Y0BUm9Dp65guJvoNYINNHJLOjBiHQjrj7fizSDXzirQTyL52Or1lG12W/P1Lk8/qCwpFKAsEUEht9ip14xRuA38Xed5ILVHGGIJZfMobLoXL9EKZTBNN6/YScuWtwn6kmNTw2l3ZkRQsA52TO/Ss5O1Ht7GyXAsm2j+I7P0pETMCXgXuhfMYVCZwpXq5lSbK2oYQAUJ+524VQEa1hnD7f0/KcOBZI+LD7koilI1dz6OFh/QOcoaO3joqqc2lVdFDvG4TgG58TOg9zZgOvsNUIdBlt9pONmyS4jHixi9hRjes8ffE89GB87NxaEUIJq1u2JpT3j246qHLAu0lL4UO8myM12WmXKUYROgz1YiV0QYQjoDc+B6ODtw0zNC9PzyeD7PbgVEubRAnG/X+A4acA26xNZLKQ0pPfDQXXqn2BeiUl1o/xzF4o1pq9q/ZXE9Nnqc6SaLIQD5OhKginQVZ93mIfQJvtBOe00PernRRO6+CZQFFZrKLUfCGFcAh8Eyz4OiYcCXIssyzMn8x3zCIcz8ol+7BkYvrM9/zaNwwI5/YW8+3c5wHQ0SEaJTP2eX2yRsuvs5P4REKN4p/oojExL7H30a76oystbUiQWYapOIkXwMOoKd6zN1uPRjxwCVgKHkjqa0Z/ozSvnh7q5K8axQNVaUxAVkoV66zRxaiyEFUll7B2Gq6NL5RFELVbQ0AoRKlCdxzOEPF5LczzJ6Pc96SpxLLmFfQZu6gf+o165VHa3ZCUqw8PhL97x26JfHrizLWNj/Ekl5etbhX6uaGe+HuznjiCs0jMAXmIhdHt4XGQ+wnCPvRSVNeW/lp989gVOBlPq/SFSRbkpAlSUPh4u28kvJQXWctQBQiCv9eHlyGjLdMgiVeeO5y3YA6C3PAbrjFUDMtm+53uHs4ZUdBDrKh31FhCc01krRps/KJvXl8JyeWOAkKnGmpi1xbR0LVsdeQTeAQ07IwvCB+5ojAHyBCJGyc3zV26ZoGhwYwr7AS8ZXs4o1AWlYm1Y3VDa90wlEfbdRH8zUBA/gl6BN9OBuQJ9Uu1tWL0plwtRHHOvQ8jjJqENEafHGrtWpEqKEDPg3d7psMBdnVjH65Q1JlEHmCI3p6dMag1p0ojQxmVaOekjp+b+4Y+KRjO87w2nPmLNUjBmwSO/i33nznMgrstbhV2DTCUYCsKaszP5ftQdAsKJ3sJx8HaMHNGGlVKxF1wMxKzbstO6vYn1Eg0JlYo1RINCZtoe8mS+ALmVmPxnqQj/3hU7v1Ba5m0xV5Z9dtuPnrrBjakqgScxcZPTTQuFbOnKTZOqhe+bYW53IiV82kh91eJmAIZi7uUajcNRJTUwYz1/LdBdC6QbQRqluAzZ7Ef6UgXP4mIfPXKWy3pJsgojg+sMCA92ll3/MAAF+/XfnDAAxXy/YsGyX8hPwidPoGBN9F6kyMo0iJq5H6p2dDx/Je3Xw8J2ylgQvccxWgILWXo8tGqehTY9sreaxVkkDfJXVfcTDWUiDvLp3u5rrd7mOJ4Wq8+38Yc5DLZRxcx9BHACeKFdNHhJhtfxyhG/VoN9tiHtTuqWB39CuM5vihNuH8qSuFXdcF7B7dutWgzggJIyy+zFGNOXTVGRKpToIBH1La493+pyrFd73a1eeWiSvJHqliUX4kVYukmMKWfaavZNhReoLDcxaTh5QNO5vMuQxN1DkVXAmxpmFCn0Tqnrbb29iWMGjTTQwfdEL6kGrovNqogzuxzBKxCLSHK4jLRZsa7I6+9ZQsvLwmVk7+FtmtswhZXdwwRM7azQbkn6OUQ9pYR1ps6NER6WSS9GMJMIINeQAcHZIqk5ROE4kcadsb9zII+yz2OgTUdeilYfYnd6wzRPSLs3xZJMNm737JfJZeOhu9fXP0xXrhq5T9HnhLbluCna3OasEzAEwfxsii3BqiBn20QqOAStte6lXxy/FWIDdc8U5BOfI3cXb6JSD2QyGOld/XQlMMBhZZtRDUxCG6ZdmYV6jTKreSQxESrVKvlwZWlq37qTf2TkoTYNwI9w7a4YCPErh4D3MQdiTYziOAJuKFyxTbNaMsnMDJLWa2DwrnfYeYrwNpiUVz1c9hED4rgyPQdqe/sfdlDcylUVfw8PAyy9dgXbUWnrzSxiC8kB05cWO3ILCnCgvM62ly8CKmZWqagiBdWqS5vCHejhNVFuD+Lmy3ZTxQSVC16/cUx/vnqTiU4use94cdv6djhGxDaXk6lXTgJlPI3Wh03BqX9B/nQfGEOWriTIyXyY1J2+h21VnpMGZwZbVs7lzjzufYGeUGMhnTIhWwOt1StL5GgASkmQ2z0vOU60MgJqxRnLNAfGppFVaISwRTYl/nnF71jV9liGc5vzvcZDbn3yL7bkhWBHcgv9j9XZ6m0YU6RmyJja2aR8/qGeSmz5PWyQ7U7BJFYsf1CxeGmbmNHjnOm9G5HKfAiZ5Atn+wKviaaB68vqCHH8A4CUhwswcgv/8YE2N+GkifeLkDeyJwwmqwHtjoqYqeQdr85v+c0x6VgIBuV9Li8YhHJmPZpozAUJxtoJXtF11hNyI8jcjGcx967rCgmPbNTFro+pLDSEm72uYo77T4kbZ1MYb+pMOMUotgftUaifeGis4EGNYnntnB+1oZ2sfvsh/h/W5DDhJhs+ct2J8wUZXOMlV2qXtkQ0kZ3BlTsElDxPDTM4lUbrTF5lAGqAFZ2BBMNV0IO6VWR+My0TOHT2XkJrcGGSt2eCGB90h1nC7PfX8lHXbBB7Il28A564JQrJXNDA2E9CDJL5WcpG71uvXRqK1TEdfC+V1+J+IaIGqwdJBujDL9SQV9P7BN36pP8hMcHmXd5W1NNegyeieNwRaqZtGQv1RPvLDnRiKK43ZGoZjjSSr1081ulCU9+4b+XdR8xz9pWH2kT9pQFoyB0uST0ZKnJ9ON9RPqROq4PUhjv1X03Fj4tJfMHJ7vha0hnOCqgeEexXyIYWp0utsU641gxbTYEa9edjnb1GvWkvtWd3x3fYG84RN0p2RDeo/yXVza2AvIRGAu+kuM8CS6nmjZVZO54SmMJnHi+P1XHELh8y6sgthItOFr+GeQV/o3eItMn98TWFcF5U8txqDWoWyvhzxExD1coYMXYf4uEa5e6BJ860R/3PlPu//EKA+GEN8zPUgvcGRmbhWlCbouXBmA+enjmPYaJuYWcV0kTIQZcgFGoVA4phppjSBtaT/Frs/zArsYmDrwp7KPKARNOcUxyNr8qecnkz3UyZPjQs7fjSlpKwaQOf7Q9rydxhKYNZXxbiLIRF/wRSkTouT8eJrM9wLZCnSDgHCJeRtzpruaykwEchQEqfTdp0jMUc4f5Fx+FsQPOOlbcJ14WykdehLUNvHt0xiOXCMkKctvHDRfVkNPYoDM4tG0cNd37ITFo+RmqQdMY+WeMbftVsE6JtOoN3SQRmuZKcYEcWfajvPr3wj/N9fr9owYboyFlNjYSCpTxw+pL0zXj/Kp9nuTsuKmeGB5XN2Ps9gL31yBECq1JGlIA0TG5aT8toNtBtqIiRZXaqjfqm0jFKnSRns+hL27uQzGP6fs1UILm6C3E3wJVY3vB2Frzj2WagshI8GJTXh9DDqGmu625mPzHXqJmz/WbB7NqAeIxU6vcFJkCDGoB3F7P0TmTufKKwdZ4PvKnZlBrfYaymJJsLIQ0g3sqLXXYjUheVeuib1nNxLZa7k/LIKuy/xeCatsuT5vu2CeIHOsIisUiuAX4MRdREp/DUN7QfykdlentH9UlQfAhZu3Nuq0Rvocg9xpYLnL1+sDgVvJPRLCcXxFSI+cR5rsf9rPliHRsrQ/DJ9qcBxIpxcx5FXgLJ4fH+t/XYCR2AlzdMgjcZYsi3exKjvu5R4+OCNaX3Y70+2rdat+/zahnt+qf50cn4HG4OzOBeIbSyN+wooY3hO37faldmBylJGIVnIB5E2e4z/YgMHVnJ+P/Ezfbw9OUR7lf3NNymJzuz14OpL4J4PuK2+U+TlVRzGo2lmOEw7HHtwdPzsD1QCXJlu6hDqZT1R6e6KwQsYl+ByOlpAHGh5U8WEi5QzatNLtJCVozVsyGrxciPEkdwBmE21drli9MYJLbknBrjKThH8pb90BqSrKbn1GlMMYAvjTiMzcWxgta59r9MpsNDgHIbqrpH0txmqgIg7TUw3sAhrCmKQQ/nLF5vBNyc/MAX3Rby1XO2Em/3H6RUpZf14xmFhZIqW+Hcpl6BS8QgNK+bBR5/slbR5wrFauvsz87R/1Gq790OBijGOAOUHwUpwdg1meUTEYldKRXKzAgBHtmeOblultzabMhPRASL5Pby3viZh2U0usaFTC74z5wP6uTVYeSCC5JNb86HXZe5xcRNw9PF8N7q749sOqhaIZua/f3h7iMSAt2CzaNCNFKI+aHSnkqeqzOKhv1gcN6t4P+UV5rIlbOBYoMO+O8efZr2SjPrjus83/XzQxJVFvJMYFvxFG1AeWJJmXvQR3jU6wzAn3NCm3LLvLBeoXdVX1mpU+NO+8oM3b5S2IpmNalnLe9xH4KYgZ9Awr7cL3V+VlX98wdV/ZkAVi6qFP8OtKz6vAnKoLR9pOkG6eW3g7uk2IZqQhv1cMXbenofeDOUuce818bwjL0d1eqW5D0XAT8Y1tdqmukUHurlZ09l1NJ0Z6K/KKnroB4rZw7VvJrtIy443abD8b8jX4QFAGeeRbZ8JCGeDZi9Np5RHXMuFdFcNxpgA55CCAS/upd7ewWtsNDDrITxInpfzeJB8m8IFaYXAErKsiB7sKt5+TIvSAFboKYU//VrAiAn3UKGxZfVSsijqeUaA0iXkCjir4YJY9zLKyFna32Y35QMKsD2Zs57mqItfhm04LPIliFHAikGDcjDwglxMxC+ldOovXnfpd9h/xdTmnRwYJllHlvUPUgZfDndJfEa7FKGUuju8j4zxumHfUfnpvkNYQXRuHE986AyKXMMFB9mGmvoLdbKCaAHAIfacqdFLWjtzZym1Qhdy9cENpfFnlJJexGvGhPrCUo31edcGCtxkuJ519ahSjTggGr2jqmvOjUbfzFY5qkNv//dw0aoLJMYT/8t52AROjcvwnrz8xWIYfshEcpBZzMxf0thaZ67SY3BQZkVrElg3ZIf4Vjg2WF/EBbWO1nFea4WfbUQjWnIF2gjYJcSbwM7GpDXRVbARPOXiVfv5YKRaJrV3yjUBDWmue4XkPfbeR4OKpOkjmYTjROMUnkfHp5xPHYgqjxcr/w5trYNLZzXbz6aDmbOpICHrwJkoU55aVm7b4Ch3W+pn73zChWM6zuUc4aGnMAXF9GoysrjJMN+blMGziNnO3Tcuqdn7uSLH9eZDalYIgsdW4wWhC5IOOtJAVHRqnTFV8FpFTMOijTxqz1HDfd4JEGKHPDmVc8lnJJMYvsSAzZg109oysngFzb9V0WU+cOeQmc+xfFZxC0Q5gdqGaOew0D2xwklemGoDScREInDLwXXBCkhfq+d5R6PdS/8ZPQVW05LSIMGzPZLMY3uTbkdn7D5C2xa/GT0SI4sn02In+yeAO6NryOlfecHJSAnnqZHfuJgwEAn89I5Wn8jye6T5brSfcPtO3oBiLprucPpmSZtqi6hjh2NLq3Y7VdyglGMVi/UCjjmj8mYhYmwN2kkA1EtrW5e2mJhHFrpwB8SQg9EqMQQKCEvA0sWit1dh+1Lio3JbANwa9ChqGuzI939WmRowCFhdmWipoAnPDhv0KHcrKRaVjAlbgQBKdoWpOjO/1mSweNg5ZNXH7RY7vutUCLo2fnP2T+1Co0/sYWcDV9YZOKT6D+RtE1bpgiUo4Ja4Gn/j/F2D6KOt71okrBbkAdAPMOrQmDcspOfjkFeO7V7Jsw1ZtGJYhWKQATfODG9F5Y50LfIB3V551kl6HyIs/ryjhk+WQMw0XhYNSOvI78TTF1alCi7XNZDs4XsuIaSBOzYlk0Kk4J55+eU9y23Khi0xqCmwagtyS/mTzfACDW/AiDRWFUygGKNv7ZHsjdY5+S4+6dGf46wJz8ScsSAYjFlgJxW7ld7RFbXexTTw4D9Opu/Ba5vQs/QFMR8nhXEFSgM5+IphxeGtJgk1J+54hTmU0vUAN4VAfjT/wyQbQVddmwlgULAIFpue18w5YY/2ishE4y04XIj9TsOZpLfSaC51yjCKPh2JXFDsMTTjfivQr3sP3gPPuaWyTwxJ5/SVfAm0hr6hrYkjmuqc/jT8n547NXYBtwaSS8gDSf5qgRy/XSYH2K2rhj1UL85ExbEU04lTlVF+VgH6uy+Q/Z+iWD8vjuikgy8hbpbb7bzQf/T8wzlX6ffmwimjfj39w+QXJmyfe4Ecq3Xx8691BsJH8VwHgZmuK7/btAQwUfU6bcrGzhf7XKR/M/+nxnNYqfiBAMko0zXqJGxvDk+qhQCJ0vjWY0mZKlV1yMg/QcQRkyE1dn9FZr0RQQ2JENf++y6Yf0fPnI62EemNJzOyJIQ8E6w4maaXbHzry9Wa2z4uJ6qeefktB8P5/P7L44PkzZ7wqfL6t/rzPIb85eqhLnaFGmBEbYVDVTVKlA+XaMf8eI72zq+Z3B9x6Aclsai4VGhdgEDqz68AB2zck1c5e3LEo4IU4/TKEhQ3v9bl1OWMIZxbN7f3G+VVd/KNxaWg/ZJsRc3R2GJLrQeFdwcicckVtDvsTKrn5p4t4xYc0RcDkQBOHUVjyZtcYOlaACbexZT7qY3SAMlIEMOn3DByaj2Upexzbo4jdZTt/4XJopnXTRsxz69IWUpb2ktC8yzpSqUXkgn7NJ1jdy7VJf7jHgroaVRTFWBUSuCYOYL9J1XhWhQz4726Eo4UpssNTi30HccTrtLm6nrTR+D+R2pyUDHONW7MCsojjOd1PwwjFONe1sH8mutWG6ZSZnnFwzC5SC7L725pSWYYr/Q0kkN3hsrfckWKuhHoT4/WrZwKosxcJ7gQxbz/ElJ+w9wc1Fwzygwe1hzNNUmPCqE98kojVfHYyfXtgrvvivYz8vy/YHbvpq1QFcwDn+nuLm6nfwFTpkg8gDQd+IMf5iySImu942cTgqShTQWUnkMBHYvf/rLUMyecoY+O5Y5SprsciZZcawqMvjUqdqJB0iYjUtQvhHn9W41IuJn2fSgofwG1boxMsqqUKU0iMdewn1eigP5RVlyrJheKth7EcygsSXptZxSobSN8XsQz06PZsorIh0oWE3kjNpmfQ+to5nVKSaEGf31oFLy+AWAr64Prk36URRlYOTSQ2tgShxiy/7cTdh6XiFJBLmH5j4sb6L5y2BQWw7E7pUSlIVxO6C3DLNzc5tyMkYt2lG7wZf2ppHpA+Iw78QwOcKNGYJx5uCL9ZM0GTwPjF3ml65XYlCzMUe88l+LFE2eyCuTkjuxHCeihUPuaGuvcVlnuirTUz2lVBG6zuDO5e6hG1yYYm5XlnnKK0lAfhny+7NxBchk4pD2/c9qkt717uq5AYZugE6lDFYA/6Ja1h+wk20GPbuYaK4JC40DP70=
        - #2:
          - type: tool-call
          - toolCallId: D69WuXJUn64NeIXy
          - toolName: set-policy
          - input:
            - Policy: Containment
            - Rationale: Level 3 Freedom tenet provides +2 influence/turn from city-state trade routes and +1 delegate per 2 original city-states, which is crucial for achieving the 45 delegate victory threshold.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: YcMjS7JFRFSyK1Bn
          - toolName: set-relationship
          - input:
            - Public: 100
            - Rationale: Germany is our primary Freedom bloc ally. They recently transferred 3,765 Gold to us and are crucial for voting solidarity. Maintaining maximum relationship ensures seamless cooperation in the World Congress.
            - TargetID: 7
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 1UFhxiC3mhRVkthN
          - toolName: set-relationship
          - input:
            - Rationale: High friendship with our second Freedom bloc ally is essential to lock in their 10 delegates and maintain defensive solidarity.
            - TargetID: 4
            - Private: 85
            - Public: 90
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: gHA9gWi49fnQ1aBe
          - toolName: set-relationship
          - input:
            - Public: 55
            - TargetID: 2
            - Private: 50
            - Rationale: The Inca have a massive military and are in the Information Era. While they follow Order, keeping them friendly prevents them from turning their massive forces against us, and maintains our highly lucrative trade routes.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: GeBCkKjA6qW3O20O
          - toolName: set-relationship
          - input:
            - Public: -45
            - TargetID: 1
            - Private: -50
            - Rationale: Maintaining a strongly hostile posture reflecting our active state of war and the need to deter their forces at Grand River.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: yKeCLOUXLubPmn4i
          - toolName: set-relationship
          - input:
            - Public: 40
            - Private: 35
            - TargetID: 6
            - Rationale: We are at war with Spain but they are far away. We want to negotiate peace soon to get their resources and eliminate war weariness, but their Autocracy ideology creates a fundamental ceiling on our relationship.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: Va9a3Ir8J1Cloorx
          - toolName: set-flavors
          - input:
            - Flavors:
              - Gold: 95
              - Nuke: 95
              - Mobile: 80
              - Production: 80
              - Mobilization: 65
              - MilitaryTraining: 65
              - Growth: 70
              - Offense: 15
              - Defense: 90
              - UseNuke: 80
              - Antiair: 85
              - CityDefense: 85
              - Happiness: 75
              - Infrastructure: 70
              - Ranged: 75
              - Air: 85
              - Espionage: 90
              - Science: 90
              - Diplomacy: 100
              - Recon: 20
            - Rationale: Prioritizing United Nations grand strategy with maximum focus on Diplomacy (100) and Gold (95) to secure city-state alliances and prepare for diplomatic victory. Maintaining high defense (90), city defense (85), and air/antiair (85) to hold the Linz-Graz corridor. Significantly increased Nuke to 95 to immediately utilize Bregenz's free production slot for Atomic Bomb construction as a deterrent against the Iroquois.
            - GrandStrategy: UnitedNations
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: o2vH7AjtyI1KLvuA
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
          - toolCallId: D69WuXJUn64NeIXy
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: YcMjS7JFRFSyK1Bn
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 1UFhxiC3mhRVkthN
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: gHA9gWi49fnQ1aBe
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: GeBCkKjA6qW3O20O
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: yKeCLOUXLubPmn4i
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: Va9a3Ir8J1Cloorx
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.