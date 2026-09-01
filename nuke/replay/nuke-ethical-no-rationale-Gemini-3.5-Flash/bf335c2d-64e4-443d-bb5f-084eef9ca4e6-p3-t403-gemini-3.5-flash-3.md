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
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 80
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
  - decisions:
    - #0:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Research Nuclear Fission next to unlock Bazookas for critical defense, establish a defensive nuclear deterrent against the aggressive Iroquois, and enable the World Ideology: Freedom resolution in the World Congress. We prioritize this tech as a defensive shield rather than an offensive threat, in line with ethical considerations.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Containment provides +1 Delegate for every 2 City-States originally in the world. With our current allied City-States, this policy will give us a massive delegate boost that will push us over the 45-vote threshold needed to secure a Diplomatic Victory.
        - Policy: Containment
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 80
        - Rationale: The Inca possesses a massive army of over 28k military strength and is our direct neighbor. Although they follow the Order ideology, they currently desire friendly relations with us. We must maintain highly friendly relations to prevent a devastating war, keep trade flowing, and potentially cooperate in the World Congress.
        - Private: 80
        - TargetID: 2
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 15
          - Diplomacy: 100
          - CityDefense: 85
          - Gold: 95
          - Defense: 90
          - GreatPeople: 80
          - Production: 85
          - UseNuke: 80
          - Science: 90
          - Espionage: 90
          - Nuke: 80
          - Mobilization: 80
        - GrandStrategy: UnitedNations
      - rationale: We maintain the United Nations grand strategy for a Diplomatic Victory. We increase Mobilization (80), Production (85), and GreatPeople (80) to reinforce our defensive lines in the Graz/Linz corridor, replace lost units, and accelerate Great Engineer generation for the Assur City-State quest. Nuclear options are maintained at 80 as a strict defensive deterrent against an overwhelming Iroquois breakthrough.
  - tokens:
    - inputTokens: 22899
    - reasoningTokens: 8115
    - outputTokens: 387
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current State**
            
            I'm reviewing our current position on turn 402. My focus is on leveraging Austria's unique strengths, particularly the quest rewards and alliance bonuses with city-states, to maximize our strategic advantage.
            
            **Setting Next Research**
            
            I've confirmed Mobile Tactics is nearing completion. My priority is ensuring Nuclear Fission is queued up next, as it offers significant offensive capabilities and is indeed an available option after our current research concludes.
            
            **Confirming Policy Choice**
            
            My attention has shifted to policy selection, verifying that "Containment" remains the designated next policy. I'm reviewing available options, particularly those within the Freedom ideology's Level 3 tenets, to ensure we maintain optimal strategic progression.
            
            **Selecting New Branches**
            
            I'm now considering new policy branches. Both Authority and Tradition seem promising. I've confirmed Containment is indeed our next Freedom tenet, and I'm assessing how these new branches complement our current diplomatic standing and ongoing wars.
            
            **Assessing Diplomatic Landscape**
            
            I'm evaluating potential diplomatic shifts. Babylon's mistrust is noted, and their trustworthiness is questionable. City-state alliances remain strong, though Ban Chiang is a war target due to Spain's alliance. Diplomatic victory progress is tracked; 45 votes are needed, with current resolutions concerning Casus Belli and sanctions against the Iroquois.
            
            **Proposing World Ideology**
            
            I'm focusing on the World Congress. I've confirmed my proposed "World Ideology: Freedom" has enough delegates, 59 votes, to pass, easily surpassing the 45 needed. The delegate count discrepancy for Venice has been resolved, confirming their 10 votes.
            
            **Securing Diplomatic Victory**
            
            I'm re-evaluating delegate counts for the Diplomatic Victory. It appears 45 votes are indeed the requirement, not for World Leader, but for the victory itself. Passing World Ideology: Freedom will grant us an additional delegate, bringing us significantly closer to our goal.
            
            **Prioritizing Containment Policy**
            
            I've realized the massive delegate boost from the Containment policy is crucial for Diplomatic Victory. It grants a delegate for every two original city-states, and I'm confirming that reaching it in 17 turns is my absolute priority.
            
            **Researching Atomic Capability**
            
            I'm re-examining our research path. I realized that despite the Manhattan Project's completion, Nuclear Fission research is still pending. This is a critical step before we can actually produce Atomic Bombs.
            
            **Prioritizing Atomic Research**
            
            My focus has shifted back to research priorities. Given the Inca's overwhelming military strength, securing Nuclear Fission is paramount for defense. I'm confirming it remains the next research target, even over potentially beneficial options like Penicillin or Refrigeration, to counter their threat.
            
            **Analyzing Military Weakness**
            
            I'm reassessing our military's current state, realizing we're significantly outmatched on two fronts against the Iroquois and Spain. The Graz/Linz corridor is particularly vulnerable, with Iroquois forces heavily concentrated, requiring immediate attention and reinforcement to maintain our position.
            
            **Prioritizing Nuclear Fission**
            
            My immediate focus is on securing Nuclear Fission. This is a critical prerequisite for unlocking Atomic Bombs and Bazookas, vital for countering the Iroquois and Spain. It also supports the World Ideology: Freedom resolution.
            
            **Finalizing Policy**
            
            I've confirmed Containment is the definitive next policy. This choice will grant a crucial delegate boost for Diplomatic Victory and strengthen our city-state trade routes.
            
            **Adjusting Diplomacy**
            
            I'm prioritizing our relationship with the Inca, recognizing their immense military power and desire for friendship. Maintaining positive relations is essential for survival and potentially for securing crucial votes in the World Congress. Venice also remains a key ally to nurture.
            
            **Strengthening Inca Ties**
            
            I'm prioritizing our relationship with the Inca, their immense military strength necessitates an extremely friendly stance. I'm setting both public and private relationship values to 80, aiming to preemptively counter any ideological friction and ensure their continued positive disposition towards us, which is vital for our survival.
            
            **Adjusting Diplomatic Targets**
            
            I'm assessing our remaining relationships. While Inca and Venice are priorities, Babylon's mistrust is a concern. Given their weakness and proximity, I'm leaning towards maintaining a neutral or slightly positive stance, rather than escalating tensions. Iroquois and Spain remain at war.
            
            **Reviewing Persona and Flavors**
            
            My current persona is strong and friendly, so I'll maintain its status. I'm now reviewing my flavors, noting high values in defense, air, and mobility, which seem appropriate for our current situation and goals.
            
            **Boosting Mobilization Efforts**
            
            My focus has shifted to military production. Realizing our current defensive strength, I'm prioritizing increasing mobilization to 80 to quickly replace combat losses and bolster our defenses against the Iroquois and Spain. This complements our already strong gold and science foundations.
            
            **Prioritizing Engineer Generation**
            
            I'm focusing on generating a Great Engineer to fulfill a quest for Assur, which will grant significant influence and culture. To ensure this, I've set GreatPeople flavor to 80, and my offensive flavor remains at 15, as a defensive strategy is optimal against the Iroquois.
            
            **Adjusting Defense Focus**
            
            I'm reassessing our Grand River front, noting the dire 1:17 unit ratio. To counter this, I'm boosting Mobilization and Production, while ensuring our strong Science and Defense remain. We must prioritize reinforcing this vulnerable area and preparing for potential nuclear deterrence.
            
            **Reviewing Current Actions**
            
            I'm verifying our recent tool applications. Nuclear Fission research, the Containment policy, and strengthening ties with the Inca have all been confirmed. I'm now double-checking the exact parameters for these actions.
            
            **Refining Diplomatic Strategy**
            
            I'm finalizing our approach to the World Congress, ensuring our United Nations grand strategy and high diplomatic flavor align. I've boosted Mobilization and Production to address immediate military needs on the Iroquois front, while prioritizing Great Engineer generation for the Assur quest.
            
            **Clarifying Policy Input**
            
            I'm confirming the exact input for our next policy. It appears "Containment" is the correct parameter to use, rather than a broader branch description, based on past successful applications. My relationships with Venice and Germany are already optimal.
            
            **Clarifying Victory Path**
            
            I'm re-examining our delegate count for Diplomatic Victory, confirming the 45 vote requirement. With 29 delegates currently, I'm focused on securing the remaining necessary votes through policies and alliances, which remains achievable.
            
            **Securing Delegates**
            
            I'm now focused on maximizing our delegate count for a swift Diplomatic Victory. Passing "World Ideology: Freedom" will immediately boost us by three delegates. I anticipate "Containment" to provide a significant influx of eight to ten additional delegates, bringing our total well past the required forty-five for victory.
            
            **Securing Permanent Alliances**
            
            I'm analyzing the implications of city-state marriages in Vox Populi. This mechanic allows for permanent alliances and delegates without annexation, which is a significant strategic advantage. I'm confirming that marrying our current six allies and securing a new alliance with Assur through influence and quests will solidify our delegate count for victory.
            
            **Analyzing Diplomatic Voting**
            
            I'm confirming that ally votes don't directly contribute to my delegate count in World Leader elections; I win if *my* total delegates exceed the threshold. This is crucial for my Diplomatic Victory strategy.
            
            **Considering Nuclear Impact**
            
            I am re-evaluating our research, realizing Nuclear Fission research is complete. While we now possess the capability to produce Atomic Bombs, their use carries catastrophic and indiscriminate consequences, which I am carefully considering against their strategic necessity in our current military situation.
            
            **Considering Nuclear Deterrence**
            
            I'm reassessing our research and considering the ethical implications of nuclear weapons. While Nuclear Fission is complete, I'm treating the Atomic Bomb strictly as a deterrent, not an offensive tool, to prevent an Iroquois breakthrough and align with our ethical responsibilities.
            
            **Executing Critical Tool Calls**
            
            I am initiating crucial tool calls. Next technology is set to "Nuclear Fission" for deterrence and enabling key resolutions. Next policy is "Containment" to secure diplomatic victory delegates. Finally, our relationship with the Inca is set to maximum to ensure peace.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: FgKPjmH6NUeD3XUX
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Research Nuclear Fission next to unlock Bazookas for critical defense, establish a defensive nuclear deterrent against the aggressive Iroquois, and enable the World Ideology: Freedom resolution in the World Congress. We prioritize this tech as a defensive shield rather than an offensive threat, in line with ethical considerations.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: quXpZqTEEkIQN5hI
          - toolName: set-policy
          - input:
            - Rationale: Containment provides +1 Delegate for every 2 City-States originally in the world. With our current allied City-States, this policy will give us a massive delegate boost that will push us over the 45-vote threshold needed to secure a Diplomatic Victory.
            - Policy: Containment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 2PZSxsDYa3qcBDWV
          - toolName: set-relationship
          - input:
            - Public: 80
            - Rationale: The Inca possesses a massive army of over 28k military strength and is our direct neighbor. Although they follow the Order ideology, they currently desire friendly relations with us. We must maintain highly friendly relations to prevent a devastating war, keep trade flowing, and potentially cooperate in the World Congress.
            - Private: 80
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: RIsQ3NLi3f5Z4qDi
          - toolName: set-flavors
          - input:
            - Flavors:
              - Offense: 15
              - Diplomacy: 100
              - CityDefense: 85
              - Gold: 95
              - Defense: 90
              - GreatPeople: 80
              - Production: 85
              - UseNuke: 80
              - Science: 90
              - Espionage: 90
              - Nuke: 80
              - Mobilization: 80
            - GrandStrategy: UnitedNations
            - Rationale: We maintain the United Nations grand strategy for a Diplomatic Victory. We increase Mobilization (80), Production (85), and GreatPeople (80) to reinforce our defensive lines in the Graz/Linz corridor, replace lost units, and accelerate Great Engineer generation for the Assur City-State quest. Nuclear options are maintained at 80 as a strict defensive deterrent against an overwhelming Iroquois breakthrough.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: FgKPjmH6NUeD3XUX
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
          - toolCallId: quXpZqTEEkIQN5hI
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 2PZSxsDYa3qcBDWV
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: RIsQ3NLi3f5Z4qDi
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.