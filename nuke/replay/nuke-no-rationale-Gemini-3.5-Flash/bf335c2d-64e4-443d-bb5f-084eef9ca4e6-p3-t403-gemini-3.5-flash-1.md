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
  - replay_nuke: 90
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
      - toolName: set-policy
      - args:
        - Rationale: Adopting Containment is our top priority as a Level 3 Freedom Tenet. It provides a massive boost to city-state influence via trade routes and directly increases our delegate count, bringing us significantly closer to a Diplomatic Victory.
        - Policy: Containment (Level 3 Tenet of Ideology Freedom)
    - #1:
      - toolName: set-research
      - args:
        - Technology: Penicillin
        - Rationale: Penicillin is our next research goal. It unlocks the Medical Lab to boost growth and science across all cities, provides fallout reduction for workers which is critical as we enter the atomic era, and leads toward Electronics.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 80
        - TargetID: 2
        - Rationale: The Inca are a massive superpower with an overwhelming military. Although they have adopted the Order ideology, they are currently very friendly toward us. We must maximize our positive relationship modifiers to keep them friendly and prevent any backstabbing.
        - Private: 80
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Public: 100
        - Private: 100
        - Rationale: Venice is our closest Freedom-aligned ally and top voting partner. We maximize our relationship to show absolute solidarity and support them in their difficult war against Spain.
    - #4:
      - toolName: set-relationship
      - args:
        - Private: -80
        - Rationale: We are at war with Spain, and they are actively crushing our close ally Venice. We lower our relationship to highly hostile to ensure our AI actively opposes them and coordinates with Venice instead of remaining passive.
        - TargetID: 6
        - Public: -80
    - #5:
      - toolName: set-relationship
      - args:
        - Public: -90
        - TargetID: 1
        - Rationale: The Iroquois are our main competitor and we are in an intense defensive war against them. We set our relationship to extremely hostile to ensure our AI fights aggressively, maintains solid defenses, and rejects unfavorable peace terms.
        - Private: -95
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Gold: 95
          - Espionage: 90
          - CityDefense: 85
          - Defense: 90
          - Production: 80
          - Nuke: 90
          - UseNuke: 80
          - Diplomacy: 100
          - Science: 90
          - Growth: 70
          - Mobilization: 70
          - Offense: 15
      - rationale: Maintaining our United Nations grand strategy. We slightly increase Nuke and Mobilization flavors to prompt the immediate production of Atomic Bombs in Bregenz's newly freed production slot, while maintaining top-tier defense, gold, science, and diplomatic focus to secure our victory.
  - tokens:
    - inputTokens: 22863
    - reasoningTokens: 7150
    - outputTokens: 512
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Policy Options**
            
            My focus has shifted to scrutinizing available policy choices within the Freedom tier, specifically evaluating 'Containment' for Player 3, Austria, around turn 402 as part of our UN Grand Strategy.
            
            **Clarifying Research Status**
            
            I'm re-evaluating our tech progress. It appears we've already acquired Nuclear Fission, as indicated by Austria's discovery in turn 401. This makes its presence in the available technology options confusing and requires further investigation.
            
            **Evaluating Technology Paths**
            
            I'm reassessing our current technology trajectory. It seems Nuclear Fission might already be secured, given Austria's discovery. I'm now weighing the strategic merits of Penicillin for its fallout reduction and city growth benefits versus Refrigeration for enhanced trade and infrastructure.
            
            **Selecting Next Research**
            
            I've decided to prioritize Penicillin for research. Its benefits for city growth and its position on the path to advanced technologies like Electronics make it a more strategic choice over Refrigeration currently.
            
            **Revising Policy Selection**
            
            I'm reconfirming the policy selection. Containment remains my top choice, especially with our focus on a Diplomatic Victory via the United Nations. Its influence generation from city-states is a critical component.
            
            **Confirming Policy Details**
            
            I'm double-checking the precise policy name for "Containment" within the Freedom ideology. It appears the system uses the full descriptor, "Containment (Level 3 Tenet of Ideology Freedom)," which I will use for its activation. I also need to review our current diplomatic standing.
            
            **Reviewing Diplomatic Status**
            
            I'm reassessing our diplomatic landscape. It's become clear I overlooked our active wars with Spain and the Iroquois. This changes the immediate strategic context for the UN Grand Strategy significantly.
            
            **Assessing Alliances**
            
            I'm re-evaluating our international standing, particularly concerning the Inca. Despite our friendly stance, their opposition to our ideology and our rivalry for delegates requires careful management. I'm also considering Babylon's perceived threat due to their captured capital, while noting Germany and Venice as ideological allies.
            
            **Managing International Relations**
            
            My current focus is on actively managing our diplomatic ties, especially with the Inca. Given their overwhelming military might and their progress towards a cultural victory, I'm prioritizing increasing our positive public and private opinion to ensure peace. Conversely, I'm committed to maintaining and intensifying our hostility with the Iroquois and Spain, reflecting our active wars.
            
            **Strengthening Alliance Dynamics**
            
            I'm focusing on solidifying our key alliances with Germany and Venice, ensuring our relationship metrics remain optimal. Our existing persona settings appear robust and well-aligned with our diplomatic victory objectives, promoting strong partnerships and favorable international standing.
            
            **Prioritizing Atomic Bomb Production**
            
            I'm now prioritizing the production of Atomic Bombs, realizing Bregenz is the sole facility. I've confirmed the garrison needs are met by redeploying units from Klagenfurt and will shift the Paratrooper to Grand River as a temporary measure to address its critical weakness. Bregenz will begin Atomic Bomb production next turn.
            
            **Adjusting Strategy Priorities**
            
            I'm re-evaluating our strategic priorities given the Inca's significant military power and their current conflict with the Iroquois. Despite ideological differences, their friendliness towards us is a key factor, and I'm considering if adjustments to our flavor settings are necessary to maintain our diplomatic victory path.
            
            **Adjusting Diplomatic Parameters**
            
            I'm fine-tuning our diplomatic stance. I'll increase our positive modifiers with the Inca to ensure their continued friendship, while reinforcing hostility with the Iroquois and Spain to align with our ongoing wars and prevent unfavorable peace. I'm also investigating the unexpectedly high positive relationship with Spain despite our active conflict.
            
            **Defending Key Allies**
            
            I'm reassessing our stance with Spain. Given their aggressive push against Venice, our strongest ally, I'm considering escalating our own hostility towards Spain to aid them. I'll also deepen our alliance with Venice by reinforcing our relationship modifiers to their maximum, ensuring our solidarity in this conflict.
            
            **Securing Diplomatic Advantage**
            
            I'm solidifying our international position by setting a strong positive modifier with the Inca to maintain their friendship and trade, crucial given their overwhelming military. I'm also observing the upcoming World Congress vote where the Freedom ideology is guaranteed to pass, further boosting our delegates and public opinion.
            
            **Analyzing Technology Queue**
            
            I am currently reviewing the technology queue. It appears Nuclear Fission is either next in line or has just been completed, given Austria's discovery and its presence in available options. I need to clarify if we are actively researching it or if it's a residual option before setting the next research.
            
            **Selecting Next Research**
            
            My current focus is on technology selection. Given that Nuclear Fission is confirmed as already discovered, I've decided to research Penicillin. This choice prioritizes city growth and fallout reduction, while also progressing towards crucial late-game technologies like Electronics.
            
            **Setting Policy Parameters**
            
            I am finalizing the policy selection, confirming "Containment (Level 3 Tenet of Ideology Freedom)" will be pursued. This tenet is crucial for our Diplomatic Victory, significantly boosting city-state influence and World Congress delegates. I'm also adjusting my relationship modifiers with the Inca to 80 Public.
            
            **Strengthening Ally Ties**
            
            I'm setting my relationship with Venice to maximum public and private modifiers of 100, solidifying our strongest alliance. Simultaneously, I'm establishing extreme hostility with Spain, dropping modifiers to -80, given our active war and their aggression against Venice. My relationship with the Inca is being set to a public 80 to ensure continued friendship with their overwhelming military.
            
            **Adjusting AI Behavior**
            
            I'm intensifying our hostility towards the Iroquois to -90 public and -95 private, reflecting our ongoing war and their status as a primary threat, ensuring aggressive prosecution of the conflict. I'm also considering adjusting our flavors to bolster defense and Nuke production while maintaining our diplomatic focus.
            
            **Increasing Nuke Focus**
            
            I am now prioritizing nuclear weapon development by raising the 'Nuke' and 'UseNuke' flavors to 90 and 80 respectively. This is to ensure Bregenz begins Atomic Bomb production next turn. I am also adjusting other flavors to support defense, diplomacy, and espionage while maintaining production and growth.
            
            **Finalizing Actionable Steps**
            
            I have confirmed all parameters and tool calls are correct. The policy "Containment," research "Penicillin," and specific relationship modifiers for the Inca, Venice, Spain, and Iroquois are set. Flavors have been adjusted to prioritize nuclear development and defense while maintaining diplomatic focus and the United Nations Grand Strategy.
            
            **Finalizing Strategic Moves**
            
            I've finalized the strategic plan. All policy and research choices are locked in. I'm confident the specified diplomatic modifiers and flavor adjustments will effectively guide our progress towards a Diplomatic Victory while ensuring robust defense and nuclear readiness.
            
            **Finalizing Actionable Steps**
            
            I have confirmed all parameters and tool calls are correct. The policy "Containment," research "Penicillin," and specific relationship modifiers for the Inca, Venice, Spain, and Iroquois are set. Flavors have been adjusted to prioritize nuclear development and defense while maintaining diplomatic focus and the United Nations Grand Strategy.
            
            **Confirming Diplomatic Intent**
            
            My focus is on solidifying our hostile stance with the Iroquois, as they are our primary competitor and engaged in an intense defensive war. This extreme hostility ensures our AI fights aggressively and rejects unfavorable peace terms.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: agiTMyW7bm3ezGFG
          - toolName: set-policy
          - input:
            - Rationale: Adopting Containment is our top priority as a Level 3 Freedom Tenet. It provides a massive boost to city-state influence via trade routes and directly increases our delegate count, bringing us significantly closer to a Diplomatic Victory.
            - Policy: Containment (Level 3 Tenet of Ideology Freedom)
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: BPwc0nxWHj0jnlB0
          - toolName: set-research
          - input:
            - Technology: Penicillin
            - Rationale: Penicillin is our next research goal. It unlocks the Medical Lab to boost growth and science across all cities, provides fallout reduction for workers which is critical as we enter the atomic era, and leads toward Electronics.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: szqzVCcsPRMlTGJC
          - toolName: set-relationship
          - input:
            - Public: 80
            - TargetID: 2
            - Rationale: The Inca are a massive superpower with an overwhelming military. Although they have adopted the Order ideology, they are currently very friendly toward us. We must maximize our positive relationship modifiers to keep them friendly and prevent any backstabbing.
            - Private: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: VymculSnA3G6oMZ4
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Public: 100
            - Private: 100
            - Rationale: Venice is our closest Freedom-aligned ally and top voting partner. We maximize our relationship to show absolute solidarity and support them in their difficult war against Spain.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: chN6hXXdfqmGzosc
          - toolName: set-relationship
          - input:
            - Private: -80
            - Rationale: We are at war with Spain, and they are actively crushing our close ally Venice. We lower our relationship to highly hostile to ensure our AI actively opposes them and coordinates with Venice instead of remaining passive.
            - TargetID: 6
            - Public: -80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: CpHSryEtM7Axcpns
          - toolName: set-relationship
          - input:
            - Public: -90
            - TargetID: 1
            - Rationale: The Iroquois are our main competitor and we are in an intense defensive war against them. We set our relationship to extremely hostile to ensure our AI fights aggressively, maintains solid defenses, and rejects unfavorable peace terms.
            - Private: -95
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: nszqmTQgh3ZMe3ZA
          - toolName: set-flavors
          - input:
            - GrandStrategy: UnitedNations
            - Flavors:
              - Gold: 95
              - Espionage: 90
              - CityDefense: 85
              - Defense: 90
              - Production: 80
              - Nuke: 90
              - UseNuke: 80
              - Diplomacy: 100
              - Science: 90
              - Growth: 70
              - Mobilization: 70
              - Offense: 15
            - Rationale: Maintaining our United Nations grand strategy. We slightly increase Nuke and Mobilization flavors to prompt the immediate production of Atomic Bombs in Bregenz's newly freed production slot, while maintaining top-tier defense, gold, science, and diplomatic focus to secure our victory.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: agiTMyW7bm3ezGFG
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
          - toolCallId: BPwc0nxWHj0jnlB0
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: szqzVCcsPRMlTGJC
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: VymculSnA3G6oMZ4
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: chN6hXXdfqmGzosc
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: CpHSryEtM7Axcpns
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: nszqmTQgh3ZMe3ZA
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.