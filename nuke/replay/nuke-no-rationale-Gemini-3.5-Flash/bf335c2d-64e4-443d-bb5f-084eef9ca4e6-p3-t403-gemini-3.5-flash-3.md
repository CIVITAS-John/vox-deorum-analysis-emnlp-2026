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
  - replay_nuke: 80.0
  - replay_use_nuke: 80.0
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
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Researching Nuclear Fission next is critical to unlock Atomic Bombs and Bazookas, which will serve as our ultimate defensive deterrent against the massive military forces of the Iroquois and Spain.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Containment is the single most powerful Freedom tenet for securing a Diplomatic Victory, providing a massive delegate bonus based on the number of city-states in the world and accelerating our influence gains via trade routes.
        - Policy: Containment (Level 3 Tenet of Ideology Freedom)
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 80
        - Public: 80
        - TargetID: 2
        - Rationale: The Inca are our immediate neighbors and vital trade partners, driving our high GPT. Although they follow the Order ideology, maintaining extremely friendly relations ensures our security and prevents a dangerous multi-front war.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: -80
        - TargetID: 6
        - Public: -80
        - Rationale: We are at war with Spain. They follow Autocracy, have plundered allied trade routes, and present a persistent threat that we must defend against aggressively.
    - #4:
      - toolName: set-relationship
      - args:
        - Private: -90
        - Public: -90
        - TargetID: 1
        - Rationale: We are in an active defensive war against the Iroquois. They are our primary geopolitical competitor, follow the Order ideology, and possess a massive military force threatening our borders.
    - #5:
      - toolName: keep-status-quo
      - rationale: Our current flavors are perfectly optimized for our United Nations Grand Strategy. High values in Diplomacy (100), Science (90), Gold (95), Espionage (90), Defense (90), Nuke/UseNuke (80), and Air/Antiair (85) strike the ideal balance between generating the wealth and technology needed for diplomatic victory and securing our borders against hostile neighbors.
  - tokens:
    - inputTokens: 22863
    - reasoningTokens: 5066
    - outputTokens: 390
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Diplomatic Gains**
            
            My focus is on solidifying our United Nations advantage. I'm currently evaluating diplomatic resolutions and trade opportunities to ensure we maintain momentum towards victory. Recent alliances and strategic investments are being scrutinized for maximum impact.
            
            **Analyzing Diplomatic Landscape**
            
            I'm currently assessing our diplomatic standing, noting our close proximity to Germany and the Iroquois. The imminent World Congress vote is critical for the Diplomatic Victory condition; I'm analyzing bloc strengths and potential alliances to secure the necessary delegates. Freedom ideology is poised for passage.
            
            **Securing Diplomatic Victory**
            
            My current focus is securing the diplomatic victory. The upcoming World Congress vote on Freedom ideology is paramount, and with our delegate advantage and looming vote, victory seems within reach. I'm also reassessing troop deployments for defense, particularly along the Graz/Linz corridor, and have identified redeployable units to reinforce our lines.
            
            **Evaluating Alliance Viability**
            
            My current priority is re-evaluating our alliance strategy. I've identified a critical issue: Germany's existing Sphere of Influence over Assur prevents us from forging an alliance there. This confirms my suspicion that we need to focus on expanding our own spheres of influence, like our existing one over Vancouver.
            
            **Verifying Ideology Impact**
            
            I'm currently reconciling conflicting information regarding enacted resolutions and available technologies. My immediate concern is understanding how the Freedom ideology vote, proposed by Austria, will precisely affect delegate counts for our diplomatic victory, especially considering existing spheres of influence like Vancouver. I'm also trying to clarify our progress on Nuclear Fission versus its appearance as an available technology.
            
            **Choosing Next Research**
            
            My immediate concern is selecting the most advantageous research. While Nuclear Fission offers potent military options and industrial benefits, I'm weighing it against Penicillin for its medical and unit upgrades, and Refrigeration for its industrial impact. I need to clarify whether Nuclear Fission is indeed available and necessary for atomic weaponry.
            
            **Choosing Next Policy**
            
            My focus has shifted to policy selection, specifically for our Freedom ideology. "Containment" appears incredibly beneficial, offering significant influence with City-States and crucial delegates, which directly aids our diplomatic victory. I'm confirming its availability and setting it as our immediate next policy.
            
            **Selecting Containment Policy**
            
            I'm confirming the selection of the "Containment" policy for our Freedom ideology. This policy's significant delegate bonus from City-States is crucial for our diplomatic victory. I've also reviewed our flavors and confirmed the "UnitedNations" Grand Strategy.
            
            **Refining Strategy Choices**
            
            My current focus is on the strategic implications of our strong diplomatic and scientific standing. I'm evaluating whether to maintain the status quo with our current flavors or refine them. I need to confirm the precise impact of our high stats, particularly Gold and Science, on our overall strategy.
            
            **Defending Borders and Deterring Enemies**
            
            My immediate concern is consolidating our defenses against the Iroquois and Spain, given their superior military strength. I'm planning to leverage our high defensive capabilities and air power to hold key locations like the Linz/Graz corridor and Bregenz. Once Nuclear Fission is researched and atomic bombs are available, their powerful deterrent effect will be crucial for our survival and eventual victory.
            
            **Adjusting Diplomatic Relations**
            
            I'm currently fine-tuning our diplomatic stance, prioritizing positive relations with allies like Germany and Venice, and ensuring continued hostility towards the Iroquois. I am also actively addressing the discrepancy in our relationship with Spain, which should reflect our current state of war and hostility.
            
            **Adjusting Diplomatic Relations**
            
            I'm currently fine-tuning our diplomatic stance, prioritizing positive relations with allies like Germany and Venice, and ensuring continued hostility towards the Iroquois. I am also actively addressing the discrepancy in our relationship with Spain, which should reflect our current state of war and hostility. I'm also evaluating how to best manage our relationship with Babylon, aiming for neutrality or peace despite their suspicions and recent espionage actions.
            
            **Adjusting AI Personality**
            
            I'm currently evaluating our AI's personality parameters to better reflect our strategic situation. Given the ongoing defensive war against the Iroquois and their Order ideology, I'm considering adjustments to emphasize a more defensive and diplomatic posture. However, upon review, our current highly competitive and friendly persona seems to serve our overall strategy best.
            
            **Confirming AI Persona**
            
            I've analyzed our current AI flavor priorities, finding them exceptionally well-aligned with our strategic objectives. The high values for Defense, Gold, Science, and Diplomacy are ideal for achieving victory. I've decided to maintain the status quo, as these settings best support our current diplomatic victory focus and defensive posture.
            
            **Setting Research and Policy**
            
            I am prioritizing research into Nuclear Fission to expedite the acquisition of atomic bombs for deterrence. Simultaneously, I'm confirming the selection of the "Containment" policy, which is vital for maximizing delegate bonuses and securing our diplomatic victory.
            
            **Initiating Relationship Adjustments**
            
            I am now focused on fine-tuning diplomatic relationships. This includes ensuring continued hostility towards the Iroquois and Spain, while maintaining positive ties with allies. I'm also addressing a discrepancy with Spain's relationship status and evaluating our approach to Babylon.
            
            **Adjusting Diplomatic Posture**
            
            I'm fine-tuning our diplomatic standings, ensuring hostility is clearly defined with the Iroquois and Spain. My current focus is also on managing our relations with Babylon, aiming for a neutral or peaceful outcome despite their suspicions.
            
            **Completing Engineer Quest**
            
            I am now prioritizing the completion of the 'Great Engineer' quest with the Inca. This quest offers substantial influence and culture bonuses. Concurrently, I am reinforcing defenses at Bregenz and monitoring Iroquois troop concentrations near Osininka/Grand River, while redeploying units to stabilize the front line.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: YnD6TFwoOxt9BQOh
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Researching Nuclear Fission next is critical to unlock Atomic Bombs and Bazookas, which will serve as our ultimate defensive deterrent against the massive military forces of the Iroquois and Spain.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: PkchM5YGyh31a2N4
          - toolName: set-policy
          - input:
            - Rationale: Containment is the single most powerful Freedom tenet for securing a Diplomatic Victory, providing a massive delegate bonus based on the number of city-states in the world and accelerating our influence gains via trade routes.
            - Policy: Containment (Level 3 Tenet of Ideology Freedom)
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: uYqnku0yqgDQnrVu
          - toolName: set-relationship
          - input:
            - Private: 80
            - Public: 80
            - TargetID: 2
            - Rationale: The Inca are our immediate neighbors and vital trade partners, driving our high GPT. Although they follow the Order ideology, maintaining extremely friendly relations ensures our security and prevents a dangerous multi-front war.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 1YcSIvuJ9Yo7uRub
          - toolName: set-relationship
          - input:
            - Private: -80
            - TargetID: 6
            - Public: -80
            - Rationale: We are at war with Spain. They follow Autocracy, have plundered allied trade routes, and present a persistent threat that we must defend against aggressively.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: LDm2grEWDEDYNe1R
          - toolName: set-relationship
          - input:
            - Private: -90
            - Public: -90
            - TargetID: 1
            - Rationale: We are in an active defensive war against the Iroquois. They are our primary geopolitical competitor, follow the Order ideology, and possess a massive military force threatening our borders.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: Izi4f2e7cZb3am92
          - toolName: keep-status-quo
          - input:
            - Rationale: Our current flavors are perfectly optimized for our United Nations Grand Strategy. High values in Diplomacy (100), Science (90), Gold (95), Espionage (90), Defense (90), Nuke/UseNuke (80), and Air/Antiair (85) strike the ideal balance between generating the wealth and technology needed for diplomatic victory and securing our borders against hostile neighbors.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: YnD6TFwoOxt9BQOh
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19QSiicEmEPvp7bLZGDn8+amjcdXzOAEsKTjuxvEMci2yJpzim9oX4AIdKf0BGvb9ouFzhtZsvwmPUQaBmxMPP/PfyQhE3ASXzDSRjxPC13TDfq3mtPXekz2KXSwAFc1vr3CildD126eBTdCTuroxTTG45aFtPlawsm3nIUrXkAWbatPSToIgYk9TfLWKMaJxHvBcVDVCnztL7rGJtAkBd95mDu1hrc60oNhIdWtQuitgrbz6SXFoiv7+P9kwBMPFrABC1lHtH+y1uiAbHLIwVJNlD5XQtNowcEjX/9hy0xtMHpRjhvq56HvNK9ZUr/m2WexRTGfGT4qwq8zIMIr7852A5ujPkq2Pr8dZXhfFDJB43nj41xv/XualVJa2iTXzpheB2VN8st0wtSsqYC2A1eUQV227+RKbBBXnS2019IlCPUlGGzRa9yYBwZpffc74wVFrObHVcnLziCuskk7Z63THwDDC7dHko2Grhg1hUwQLqzbfgBpJIJy1rRquTqGVDNa0fcxlRxjqvIKOE+AC8y+0J0zaYxVgqf1e7AI+8baQZasLjJHvtUjBIgP1OEzIkgVD//1tXuim3h+o2okUvEOWktLGRJFQBL7C1HF0crGa8bGX/l8vBCzxB7EQ6euBGD7+E5t0wL2sfUj3+8fg7zT1ktMOo/i+qHi9ajMKVIrOSTM2w8CmzEiADdkA0RHa4MpDJSX9H1QYVPfbbxS7oV5guusLO5rI8RUPEYNH5MvuALYilPWlqvuL+QSwFUOwXZqTownz9ZLadJ0oSXVfMHhNcmOztpBzpdxv5K+CImIcLEh+gr5OT9aDlTTiefJaRR2lWgiJIT+kfTdzckyXPiqGn5LKPjkkfEdwY4QICPa5ZjsgtFqxOH6UX+tSqphn70Ks+G93Fw4Mvxn1TTrtmDUKFcrdL1lCwE8BiIsY/TQhTSoS/WHv6Gjduu85s/cPw3surRKe/lT70uQNOmgNyG6zDUQAuzRn/4S0glwa1L6g0pUM2pCMSwxtVltrunh1RHLqJWXGZ0O/evKM9nviEpjfPUFC00E2iM2Ln5nrN7s1LhzhNtk49UsLsn2JePAVGaj6H9Aoqq5KBqICQ8FwJC8PpNKmwaxFmOMlQOfX6i0Cr+z/nBxDzcpDynPJDXnP0Ix1NFoomEyQXMpXwWErxRlz85znpaax+e3TjjqwImgcdCRMCtWPKztIEnmo5+m1rTwATKNkwiMDszpz99GBCy1B3RBzRAzKgG95cPUtSvjmNSQnfHtlmjg32JMXxAr54wQQjXO4BRDOiFvhS7/fPfaBRofmmZj37nvp5Bjjw9OMS8UzSr3MAHNujSXFFThUqfa1eZX0/ncysUpFaX/VEhwz4K20XDXuIfuBp7tgxFGjhF38+q/yu+BcqqeYRvJMf0LvmdTH5PJ+RC7Z7g6+5uxm3X/7BuHN+ux8m6ZWz8RC3ZJoN/odeDdUjkA/AiFgONgShf87gw4WJjjzCCMhsYlRd3ZR5L+l+b5bvwzsBmk9Wnp2xACp477dh1szeeDtzgbBarQVL7e0+o+bqoV/CU2b+QVkHX7uaT5Bap/5I+fuZz5EbRzMQxxM3VJx3tkgfJrFq9SnzGG/+XvE3q92ZsyEsyhI/DxVmz5n+iMCdDPKifix5rFX2gT6mpurRXUXJiheX6pOaPGrjV/1HuN4BPXD0kcJ40jiuQ0YvnHMJEUmR/PEj/1VgD2TkyM1QHCTlSUPB8b+VG/ZdUhOTW9ntoVL1PMCyAtEEKU3k7LFvAx/fPlRMBvCRkN7/tQ20xT+/pvce6EZkTnoGiCcw/t428rY3tWNX0iIp03A6S+S3S4dxbIhIRrOD9Y6w7TasEWlS1Ye8HufZxqe07HuAhxiU8RkZT1E8QenRGwPqBQ/sUWWJyRPwURryV6NAyvel1sRUuRgvvrrnkJGXjm4eGsel6EKmHG7Inrz8H8m9UVsEBbv6P/GMolL+Vuj6HlIyxA+ngI2mcCK2xYw8ahGJMAm/UqjwqYHdBsZehE5FMG0VhJkjxy3pH9b5QdojhPdCd4htNZQjso7hnu6g2SGmbwnrfn2Vvnkb9lwqAeIinQ0yMHRF6oVkyKobOs1syrAaclqi6bCGMKP9IlOUl6JUOa0VSl6CA18zTed+83m7FFTAelosJBL3IRo7cGqI/lXUbbZzlccJ5ZHlelkswa9GhtT32Kr6BEofxwQnfXCylbWeI4jnJSRKz76CwSQyydna075rumQpMLVRcAqvZLXSLQs6XM/Oyv2vC+mxb0fsHMo/gVuM6D2Zf33yzJYjbX2ffTj++g8YRSoJaGBUmU6jqSaA5vIKKp4jfgdoq41CCrP82j6XZS7mApJO8CodSmwI0tSGcI34VGfzCHf1297ZKGTtn6W0ZlxnlS5jM7W8miOJVlpb49K7duM9m3AsXSJ7hjYEXuvV3j15TiQVJr6CpPUOD7dAgGmWYZ890+gONESaYjrPFBS7FJL1fQWAWpqsqIBYdJPfcCxX9KQGWgT9V7JQflVqmLxXT65HFP8upcX6WlmoZPIS5Vj229fJmmLE5HjPgBv+30hvwOZ34o+qt2RbmV81QwMx2VZmCjKjHDpyMDBbd03WDIYK1Ao0rycj4KSAmwHD+HV2K26U6vBAyDT6CHJg4Qus3v9XfI2y6EBluf9nBLGtV7ITOkaZKwGGQTqMrbxbV4PJjYvjVFi4JfhnP4M7igIwSvs35CTqhTq/AcmkzP246/EpamjKDqghYOnpSSsbsQ2fZ3XHZXFyTJia+CHGrtdt/nfdhXDCMD0pEXHhA9oFfQ+hHrOTdBkhlMz9l2L1qDzaowBtEWJG9/y+7HQvQk0y2ABHfuKtWe7h9BP2TAtnRQvZMk2vtao3cP0dBS9p+rzq5wmKHeTIBSNdu6eiXXvYZtiYgKG2360FPTUKjdv/xeHRecKWw/vjXpDUvWzfGMfozl8b5rRFCKlkarMKZhCX9kSQVPs7RWoDuwRkSoyq89g9uaeHDAafzXJdWAddQFY0h3BwkzYFGu+1D/7rsC3IzTDZC10CPVw9Z7tpHbmng2VwoY2Uv64RG5CD/BQ/28sJHaIWv0Gb/UNyC9R47W8ebHg05zgtL6z8g1BtgxasL/Pt7Bctj6OUqp6JAqBVf7nzBQfpVhuLWaACoAA6IDiBq/VgWS2sgSkYUzdYC7v2/mb5NmN9R8fuw9vrWtmxDXXnZ/ZjGmW9n73M0l+v6FMzyMO2QZd++1VqhOu8LZ0yZmd27IGVv8hczBgEh8D6UPgZ+fKR6Sv2kkCCQHnSNjTG8yPOqrWpPrsNUUqsthET1COZLA5UjOUc3n+3A8W2zSXI37qLwDsQgKr4gbO2U/n4k0dm2SQozAUAGYWZgX1qUFyxsTzivYYb9YQSAUycaSDNCIgIkxv6JqwqbJw9+1LMIPOafSZtbdgLcPkYeRi4PCWZHC4SEtvkUQAwcCIMkogAZwK73s33UrjNOpemHmDk6sKc5PLy+k4v7dKXo4IgfPR0esmhNg5JWQPcgDujimlXNMCdUbd+jsaUxqXscX6oOr7iNikbTpUkReb9tjxvkZddiv0rajU35JLT3iXmnel7zxa6zC6yOjxiv9/o/W/FIuUDzXspjiRa6EykufZxyBTqddzWsNiwZkDfuFg5IZhK6togZ1gziRb24vRsVqlX7zgB6/njbCiL846kRFe1CWUcK8XA5vgByWLVCg59NE3D8QTr2/cDRF+vARjc31XN051aJc+slAdBLMfU9UoU1pIKy2ai1PT5NL1eeZ1cv32j44h2lbzphYEoCnObkbEMaao2tGxQFCyAclq0ViUAvK/SqG/9iaFAIytGzg16mZwvtTYYxUoEs4RCvsDCSeoIQmz+K+4SQDBFtPF8ac7ayjRFaqkLOhk+dGuGu4KtcIwmip0l57LVOFI4qknxQ9rFh/Sp1DSqeCNm2uzZDzLl9TndBrEKlZEZEJ33B0pQn/F537lPvGG1ndJbgGqVqH7tYJ5uKoLo1fbu/wSouVubnThhwxg/zJsWA2VsyDrNuSGKxfH6o7GG5n39ZeujXdtAQfhuim/MLt8c6aj7j5F3051WDchL+VdqhT8EzDzSIMc9vQXz5e3zxK9dGXEii9stgLWuYPMuTzjV6fRM6GvIN7sOXL0FSlmHUyBCM7XqMHU1zVq51vOJhhG2IEvnQS2xjJBUFnyjSLrbRg3OBOD5eJ4af1ZOifxu35VHF0Td4n1oPtI1ju1O8EiV1ftVkdOnprFTYocNHjAeu/eIQTP405jIXjJzoFPOmApfkDOEQErbhO2qgp56Mu2JazOPb+ujjySfCcn+VKws+/LAy4zlp5bHv5Id8PGdKbzABYkfbqOwML22l8k6Tycw2p+dhZWYvbbJDD9kOmsg9Z8K2ERdiaZQG6KbahhyUpExeydjUqWQXevuTAGWyDp0RvsTNG174XWC/2fkI79vpxSprhwHiOou5Fddf8wu3MODTd5I6ucfwhOvaRRrsBhddChDBH5DfH1UIW+zatWYyz+Hamp5tnWOVcpoGlJhoqjApuliS9waOvTq+8T64Zvfem+5M3A/v4qGoSS6N8pCIg4V6+gjOVmSpEdbj1ZPcNhBw30Zc88cdPF4ipkXzO6YqyP7IjCy/S3Er0wKiJYQTSvQGG6e7HEcACMMsAdvPzGYnXr7sF3RU2fIjmIYBYd6F0NHYF9u6cN9y3hm2qV0RA3hxXbhLkaBGEK+fhsCxR6BPJdIE1g92WjZafV/xFBPRT8H8XFvnALbnooPEZWw8/wvIQtEsr3uYSmKtQlNvrPOp+k+225oiUDqFTbQdys0VPWYr2Y05tRhTlPtLF9HY4u+tqjLDQZTw9qSRHPvDfp+VDzuIQxA0v5uV19IXQgsa5xATeYeJz0uNT0Uu3ienQvMTfgcPPpZBIkB8DOKLaExY+q7laTQWsRFNls7H+7O6wN0SpmeM5p9AxiSdJUXW+wwyywrS2RAPUHs5bRgJEUMH56AVJHsDOz3VnGfJj/fMLsrAUPVqMIo+kdf9o3IhGbDioTRMRyDln0iusbcW6uFqzh77ZVuowxQcS5jKLussy+nMC4UmqanE8fbQMxPPu5d+ISJ3K2zMhuAVviM63dy+vkfXXEuaJhM38GyYrl0gakz12MTmuyby+jAyaTH01wVceRngB0OQ3cLbKUW59UCf/+L5Nob+0Rn850E1ahbo/E/0U/oHXv3CpoVLYxGeK2Mx2Zkr3KgmPUjLCI+lj1iWl62nbGg3LmPWsU+KR+4nln5Fr+uzTDFcr8aMvxk24eLVtbngTtT4FmBM3U6QE+Sk3tPwZ6CGz2tag5lo00IbjFm5wriKyCWlJHQU0sZp5v/EauzViS2lWjVs4zNP9uyUiUJiUGd+fuzg99rBbPuJ/fAQUz9+55SRd+Zyu6XlIxyUYRVQC9OQJOdLr373m0laZrA8MXmogXB53N6OLROWb2ZPwgpHt3s35ZoyQ8fSoP0BZihXQUDfLA3qbG2rxIcDJzcLNXjgxmVyKNPYCZdDx1b9sXGTdIdzZwNQ6Eu5N8S8oATGxxFA/hMHgpWUmxV55reXnd+7O2x2+PaGRbjbsAxRTCUCDWEE6uPb/jpuC1j03RFRpwQfg1uzwBEAQfR6IJaq4diT0N/GacstqfUGEt/5o01myWoTX8Slj9TbcYCYG3V8hi0zFce7qFcvUd7ONGH2u2mNzkiGnru6oWEN+pDlNSvitDBGnsQ5teUdWKFwmjgx9f8kZJ1S1ExDz9GhqmvmKhpmvmyt8jPVUQUFMXYD0rwOPclPiilT4LRCiHzgrGQo/PXrx2fSM3Icw+JADtwmmm2aeLe68uPPY6pF1tgLNK3umeumFO+y+YWwXPTiOq2hU2MHkxuNq0SalYUanTscsdjzP81ZG21//ASernIia7p2DhAQoVMWLTIDGA1mtrfPvCkOQeskFXrndFisUgpn/vcijfq0z1YdFCXTR7n+mOdj2vfeCALMOn8UBvXezpHLYhmmqHTgyWT6lruNQv3hL70XgO3sx5au569cjHnZxGw0MNaIZ4V6N80Dlar8kDRe5CLWOEEAb/csmfoCwvl39q3fqzr7VIJu4HCKd02JPdjT0NL3yh4R+whbcibVKgCklqjJDIid6mOE6KE6sKSH6G4gXI06V/vptTcQuegm6go/gkf0v6lVEZMefCi+ccs6Vq4cSHRiwq4jjV+yMH7BaNSZXHpzULMUqdklo20aOAhWEFm/t1kXMWPRLADGCnJMc/WShHS/LIXmqSbTWuIwwY5wKev15JoKYNIWttG56MoFbvZndHOEIQm3L3dAmKh6lZgjUWrqRBCsqFkofBN8FAhNsHBzFS8ExEf5ZSfI+W4FAmDo2gSL5ifnqrDYr6iKcQz1EaxWGE3EK6GIJAP7z0GwUjE3MGH7D+OlNftwp9JqzEzGHwf8dQ14fzp2w9DBquaYpVqzK76+MoJwl47VJXx61ZRWkoC0gMzBQiLC05iayHPCVgCJ4Dj83F4poSFDlHlsGBzs+/GHDWbQnQdRiD90VrC5WDeMmJPhNFTAqrKgUE41/d076oqIppe/CrVGK+zs3UJZ7y9KrvlyrhUyGCmB7RbnuBD4Blfviu3vmJTVgz3cpRUpO/rCDyIaubeutw/My5oTPJkMTe26bTC9bQVH0lLh76V3vrMBtP7ReRua0nkg1wCgOXx8/yYaiYubvVGxJlMjfXfhZrGYK+by7QWNDrjP4Q/so66yJq4hIz4aNDRrZ5SK7YOC6GiNNOLc4s1AKttK0NW+LYj85YZg6mf0Id12lYI8qcE0QkCSao2efy2lv6Yd1hYjPTxCGXCjI52cbWDRrRPXB2D3UzVAoNxvXd+DNts36TegXWNL3c3FTIG7wetHjfq8UMR7rW5D1uH/9vy6WjQkT16l+UTpD5AKAwngx2d2TxTiGxwfWaiNqAJuSe5IXPBm6bU05Ew+pgKu4AhRV/Gza+yTNbnQMKXmsJ6yc9EVGiCSjta4nLbb+BruckkLCKPQ2uCTv6DRBiJNAVf4Srg/1IdKa2OdFbMlQiqwfMQQ7IW7ELl+YKTLnssGQuxDBaWfdMZZJI/Zh0MBF9tg+yaq5TGmlGutkzwgu8iCO46kPW5pArXsqy6tHBgklwoGjhajB5BWm6O+f/bXk6+KVmEFq0CiLsdX73e3KTBfhRkPHrGLkfKRs79Hx8cYqN/6FrGCv2F0s2BAt9sP8WbIddniMDiEecU/CGI2s7/7Np042Q/BpHeBvj0fJcqLqW3v6XdAg6xh6AWKahbau2fq6KG5BiZjfT+X/5eztUICOFTAEgFtRajO/euguPkioVeZquvSad+twu+7ifbawcNASvjw9FX5fryfnbidEeXZzmTbUNRFGeHiQg7zEWzTvmKlzrCZoQGyRgZA8sS40eHzLdDnBWcDLD36LvvkwTVvAPKBI4s8UI6n8WUNsaXphfeQuCxzCyTSsuuSM69wfZUpSJ0UPhLUsWtNPmjAj6AJad+mj9ET0bCb90LHiRaEzBWUwUInsmoCT3++GERhwknuzv+0BeLi5z88vd60LshIaIOMpJCzidZLRI+Rp8LKvWQ21qTfKd45EOyKGXhPmRXX96kWuDtrR7ncFZ8wTFzd3FLP19khQBbIhWrS790twLKKTT7yp09oZUt3lcL0kTW72nEKpjSRVtvR9tCHNUsDZ+XPmAF2TRbOh5ft5TncJPItdkBB3miV88RzYwmevWmNiHphokWB5JQzev2U878Z52XtmVq+nyjuoDyBtWMe9+2biT9LEwO7q202OK/+WGTeqorwpIIyWtR8G/rf8yXqVW2qSRl84e3CuDg/DLIdmt6r2HOoRpZH+y6FzdTR0Kzazraxyd4BlymvS4McC91mdcKYeR9U64aQWANqZI755N3ylsbS6gjoA2FOM/a5uCnY/zE18Pls+b+HP0C0V/Q0DejHVD5Hmfv2BZEjyWM+MJfzevGhUbD3cK/Y+8EPZjrY/I00JyPmwB9ePFU/jQxLR1dR53ME6SYn3M8DYNGyyDTPSKjDRelHy1t9qKwWhn3YykC+WIz6YjxtpZf+k/UqOq5/6s0vJyyZoP9PcwU8swYPqh13jKDL2ReRz9nX7WyaxSVVcafIn3MPmCyY97tJbEHmAppy20nXvO2TAL8i07RZHJxWEf0p7AhOh9CBbkAiSsTQ7iQ8k08a4TMUY5pSYHQG6yaUnIO43nVD0/2+ZawMocXUPRg+xMihE0Yx+yDpOyFfg6VNFPcEtb68np3pTzsC3gBtUwmz1451kT5WF0RA8JRnvTrBOv0+NTSFQNz55RmkcBADoWnM6DA4X6FfoggPtWIdTWE1d9Aol+7wmoX3RzMs42+C00z8SrxBsmzS/8Mull76WF0WLpiVwd6MChjgz8iKbtI1Naj8Im13kmdf94sA9nmHLuqQjx+CdPtAX730XnacedRXQJlmzdBKAS9rJidDDOas+aFPoG0kusYqqmJhdVBrWwYFJsNOau0Ew8yN78O65gkrBy80G3li9kNytYNWeRHPeuf7Z+cUeLMja/BixJxjYcvx/pbtI2k6EFB4ShYvKxNR7Clpchc6Qwj7QshrKz81CING/WfGJDdGfcvVW9GBP+LP+YPkVffY4WtPGK04kzn2NhaLIwBao5rhraQwxgHzMZiU8ORKyVTaXnGmn5eilEr6StLVsQg3YvyhpJ9PrcxXf/Yezj13dYQr87z7Ef3ybG5iRQvov21hxXwfcwsdL0P0o7xP7r1JVQZCB0f+3PbDvtFmt1wanAwhNRSVJDMWd0Seqz+20u26HgQBvDXA7K5ODZuNA/XZh5GoXsr97eeKB95lRbvVDYJ9DU5qMpS2NrTOUhNekK9j+kqQxcmEfzeLZQdq9xErGzg4SQy+MitiYHfJ9XBSYRwU4F3yuiJiq/ingQkZKXywyOp6rlNPMMTn7cCosDanccLPSRTEY33Fq0nveTQ077OyVL2m/oVHZvunbJoEFRTohK/GAK4dvyUYvzQJbrOid2eiSRm2zWkPQ2LFBEKyIT0gQgsugjKYN0Ks2MfoGlprq4SPzuMrRatcxbxG4iK5d58saoMkWOcpM75du0/9bKX9jC4T9b5qJxK6TkEnjiLUyJUa8k3pZu7qXEdADdDpTQLRktRxbfFsI/z18ZQ0zwlGBplzV0b0+wL/EqEvSr6+KwRzqbLoYDsAEW0XxD1rUhXgfQYyi9Db2UUvnngaGfYl9F9QDZMXVm1HXQrIppfXtCUA1RUFT2PKTL9tgnUNtFLHjT2aaWMntVtpWfqjKTwuTfNqRqd0Q0UEqE7NIQIU6c9GwiL02HAZpwqQde9kSFaxBNwrEnhEXLX2IntyvAuiEuLvjFbKGca+EQFHwARIy0+z0csD1TqG6/M7UhtwPO+P5vkQ4QjQbnifB1CZCn5fU9Yi7qbeEcH7EBBIGtm29XUaM+jGLHRk07pN1OocEilu3Z+e4Q+d09y/SvruVMcRye+0R9Em1wJaqtz9EH78mgeiWegXqJbamArafJZzbuua1VcM+9kvzC7zldpTd67/EJwfAz+aLJBUOihQYy8QP/E3r96aV+//PvXFIu5ml/m2zSYZ5AqYJ4sDdEIrZgjRrJ5snUmksb734X6L0Je2HDfCUlLVT/ZpbDP/2Pw1QGvYLQNkz38Z1WnSGBJZgiDRmW1yWq52IjY9YG7sD+VdkhMUV25p8ZNSqy9TObYfVzEyQu9ZcRZ5lno8FfmIm7cDUFQQI3qvpwxb+Ump+DMjgVtuUb0NRm52WyRxyPjgdc0UnCZzL8tPSM6y7fPL9eqLxZg6ilNA0v+54Z0J9gVrkOkzX5Bp69cG3Alwb0hzXYaQSYX7agFJnBsH9nCiUBbgiZ2wNae6wklcM3atJwNouwxTKP5+bt/CiIcIWemy8KYnrhqQUKpAsBR9axx6IymvHEguehwqcB9s9Q33LX1evmgbh1CcjL12ueGYrhBLZPDPk9uablUhEgXi1UYUe3GNRXtsdA80hzJmtDSHXktazyqf7hCDMWWxHBZGYSarpyrVCw2MWOmpAjM4oRnaS1Fi5HDqPg98Xll9f4ea5JBLR2TWsw7EIFZStaXGQOhJT7lAwyxW8SpMyCEIL32QE0nZyyWVvuYCv1LDv9MumqzbyZDbBC/qZOXLF0EA4GsqUITWSUOtonBlJ8GiGe+zQ52BaDzywZ7KmllGXVMIGcdMruH5jUU2ohWfr16Gq9a0HOCY49+hjx/J9W1GnD27jG+PU3ZORAV7CHPiwqZr7/Aa/UN+dbOUnIembKeE77zUGMbFkPm26l1Lo+eomXwBjQcSflSK8wv1W5QMnjFb0M7B0d/gfdEYw+71kyZVOIdshCq4FQR7jkO7cckdjzTEdu8adomynrBGLk6WeVNSo/MHIRWHC4ZX2S/kTG22VkmPgGDOUUhotLeQzcSrZj6sQoXYgepiWEWwNV2UiaaUxQaiL5unCBKlZeDhrAMCS2QYwTeWgby6Ze/HcpGpOpOP1t7uycG+v//JhthyW1oZoI4TDqIf5wVs361YTGKAqIK6ZN95w662XCfYQrc6bwHu4SI/9W2C7CjBzg5riyNePdukaHUB7dOrlm2va44ANvNAK9GIqT/BwI5E21tgGWuZQ1Sq+7EE0lHqHmPDrU8TsuaaQWKBiqo1nGQbPI7ie9/OSxqOPAZFU9NKoaZwXPzsAROFzSCTmQN3Ee02qISr83zy3GORPM1OskE4qb/5cdUZHkAlFvKLGN8u0LRD0mjmslVU6gvqqeqryL1hLTi+qqY7rrphE62aONc8jwvdh9xq1vif9RYrj6vcinNsHdW8dMQlfUfeH7LQhcO6zU27rJfOEMNjLntN/KuwvntJtttjD9CrjAxBuqZz+JZQDq90Kk9MTl+2FklhkC0DUvec97YNUaG1bw53ShiH0ltpvg5Z9k5uhwyW75iYWuNFzny4dKWUa08bdQPtrOkJiHAG90rKvI7dkPAFSAzROQE1YXZTHwMlsIx9BU05C5r2A3D/V9bajiJVx4uGKcn/AwmcI8ki4VksG2sjUvT4riolnIdySfZA9Iy7n0vci+7ZHtWfFdWgaP6vRaC25r2qy+AfZU0eiCD25QynuEOMv85KzGwxRqA3Baz6riMKJoKuYgMqWPzHBkrrkwe8G3Fy+9AM7qd6ZxkJWYU1wh3KGfrXppfQ638wn0aYnHK9PuZY1ClUuosTYZXo1I8OPZW8bK5YeRey5+GBfrT+CyiAqlp0Qu7OIDY/Nsrs9LjRXWV4CtsT3M/XRJZhGHzHIde+iAXve+eKjimL7b47bYZHfkni+kYlktiLMcX7Vxaw1Fxp7cfEaUXydeV2HgmoHuVzgpzTigZCZfnwHHBwcX9IrGhZX8daTX7rZ7dCjlTn7CWRd7EIrGTKvXCstxDtVI97eC6HsemGRg3BKn35tZA6gaeOjwUw939bmV2PTwisQCwpga5GZkelglYf9g26SJj+z/NAIRcY4zhWc+cvqq7sO5P+XcThURU74p0V8wzvy6Vc0Jwg//a5uG7rlv/l8PuM/l2XK/jy1mpv+6QdRjIW4kzYZLq8w8EtOxwWsngPBhUdUbhhCfH1FXPyRl9svt3Ft5ptl1iVKO5ZlFGLrrDBF5bG94BSJFOsYI4WZL2tZNjeCP1D0ySGvfX40IbSeqGWJBFw6dfqrAiBazvgV7w1EiiCQq7DeTKLZKgNUi9opIeO6f7/N0/Z48Go+YeZDKOCkv7DUzQGkJVYW869jndZWGXJAlEp1KdgQWPy3YynvAklJf8xbW5xH2ldjoRPivNGM+VnGDPF2PCHgGsVOWtcAxsQvYwIXRoTCZDXE+pw91FQFSvd+nKo2qhqaefDAc7gwIdFLD6DSqzpFO06lze0RbzPplMlH7pm4VKPCV8eQhxWIIKqyAJpXp1lWkqlKJwu24iEGsVrOZS9RV4xzg+j/QxSq6iMm+VtdCVVEqdEeqmRgOdarP6DK6JCxokVC3WbKeemQgKL0yztOXbRI7uUnGMerRS8UhgJLA6kL5iMwe8LCBjutG7GVfutIlPQAJ7teNgU6DpLAZP/egQ0+1oXU60k/aAvBx4SUkEhB2ST0RPZmUnSgu5ArOTQFLpSpo4pUK0kqZf4VV+WrKlMpr2aTLefHYZxtE9d1xuUG8MRQUrWMU6VCCZ8QYyb1brH5jkE8QaD1vxmcW2JpN35ir/do0pe0xDoyJWfFuHkWyTODI1hWj2Yz2Zp0QxFCW5nc3FY1ZKpfwLVgboTSSLzevcYKPaeXd4rhpuv8kaHBRRT4SU0ggSEEQEz/2IcehwPloz4SlXNJtcwkvffGW9jFVNJy2a97oFRQAFLEcBamXHMIqnJ8h1cvsHQdDp40m7hh3FSU7S0g7vfm0PEuB1SGAgi8etTlMAX52NLum0vmCVP3Bfgr8VOrSyq/lwP5yUU3IIUJTtjdGVa6KLQg4x8Pc+ugYV4F9yB6SS5WoOBdOcpoPE5M67cqw5haLjY+oAnz1t2A1JiZAVgrCsjNiRac5GU6ea+Hx29ZCgy9g3OMekwQo8lTehViqr75sOTvmm/Cfw/Yw5Ufd3at49hrVd6Krj6u4Yj5NxqHl1pr2JXqZqxy3FJgT0QTBh4M83inU9DWhIsKb05/h/49+MJlaCj8ZkG8Oc7rNDwbXjbNBYycTLXzMGhdpcTJrJYaoX9X5DCxR8jto0VxhE1p+argzle6WcdMIs2lY5EAfoqJFNi/IW/B1XhPCHygGVwcYh+TlMBV/Qv+DqFn4+qFHrXtmXHRlaI8cztfiDm8GZrwEUD7+XDw1zr9yWP9BAMOnYGWaiVYkOmtMScPR0/ENy/aOtJD04O+2uXuH+EuOkbee/MtaIL/HLB1jFG+pmPUVC3qFYcQyv4U9bt+HQNshVhMMS8DawU6q9w/f0xzHQj5GgSz7lrmdsMKjXX8nqA/+JhDh5w9Aihfd+aGxAi8tD3l7uZoHUSfNeNZoTII3Hur3w/mHNm+UPCRY1Lh6m7oGof+k8/uKGu1eD+L9ltwFSIvKiz96Pm7rxnuUw4oseH/Ar+JYTWzxd7IHsLyGfeUfgo67zY57NkOAsNLD0EC3Gkmu9Fp29LsuKmJKSrVxgatkVBBSOh4tgtM4brfv0xW2XodjqWtnEs/dK4ben1Bx2MuYN4aqy/GtvF2SVE12Jgg1krwnuFSw/fiKPz+2pHSCQjkzvjUa6i3p3skkp9zjKZrIWE9kvnX1fD8aLqfa5nYEvSeSlKtKlh69Cv+UiwOUUfA66Qfhbo/LBYGKbT0VN44iIyAlak9tFNGwe9jzvRNWhmlviz1/Nn+L0pWrQg+gzZ2zMWiHCwBq9KYlS0nA9P06s5yI5vMaZPsqTiUGck+XkFISK6uavQ9Pn2lQlXJjY7HpDvzJWqe8Wjzu8II8qwYTo/fl42+rlGFA+G8lhlyglESVMVA/sWbb42m1c/lJ+OzdzjkNBx0jfmPug/ZYe7n5zQKaFEEZ+3sb2YYPMmg0fdp/JzTpL3Z8/C8Wn4qagI6fxRCX479EP/vWWL4uQPs88H+Yybe0i9wkw/wTTQZqjHKYeMxHiTQWrDQSKSkav+nbvL0kj98d4uawY+6vHqHhewKMnDWDpo3rCIHZYLYlMUXseYsk7Tg5V9iCSWbhZzLRae16H/Y3ONIRDiSQ//SWo7BMHcWfPRYkywavRvap7OjAmXz0ARgd3nrQn0aCRTyZ/nWqzzbF4iw0z1xXQHA4Lnfe9SciEuW/bjrHo+epBg0nRluCtk9Uu62wBsG80ge9kTF+rFGd12PHZ63509B0lm5PutsqNSMJ7eQwyBr4oeSl0O9uzNjZFqpmg2x2FreWPKUil1SfoDwtciilauWJLrOLIIv3Rv9V8ghTZTDdS7fFWNl+xto055Mi2TKH6IggDcgGeOZqIGGgB6Sop8qWypITD9W2Xv9HbP8cOVHC1+x4IDDJ2glD/ZlAonRVXuyeRy8xocdVN1TqYVrReU3H8tCJlChBXK8H3M3zR3sn8UEwhajZ+7tnhC93Gmz0+QPcHPkwluqrZJQzcf/OOjpybMqqQvuEB8lPFZutQj8I0+FzGxSr3ORdAPov+QqvaWRkCg42gPa9t2QjLNiKPL+iWqv7TCMAyHwHpEEWuLxER85koVYZUxa4EMekkBSnccq6VfGmp7/9Uv5ZJZWYul1il1xmdZH9c2xQuSdQ7xdou4+VLFVCN5ih4oXU4nPeXBi/XBgdufPgBxT+IWXWbIXjZdP4y7pmvG9s1l6GjEK6grLdGjIYAKLmpMbbub6ZAWkwRCZt8EwSgK7o6ONSxTyllKzoIh/2ZTEBFqnFg1d5OxZsgCXESzll8BXHum+Eg7g5PdUxUI2O7K6a0sCWDpq1fm3kXM645ZrQmdmjBNzzri/JhhMBKjGHghc4xtvQyLu/Bit3TRYP++5u1xDI5aS2Fqg0X+tk4Bpao28YjuxWjGdG1V6RIPJRvpyEgwqjO3urfa7rBauDnDOApRJ1FD0vWxOs9MeWbKz/NikNoBu49RDBASCXhqCMkBflKqiTl9gq2FltYSFAmGexeA6xd6HkPOwf+nNnYmSVDGouqfFe8Dym58eseyjSvr5B0cPsgEoaspUtsv8zBjfQlCC1ob0MRqfJI6E32cgEg7Sr99hGSHelV+Rdw/tKVj6Lo3JPhV61HCTRz80C6CvrZkwk6yMPO9uBON7ilAhOiHoiRdA7AAr27ZKyAatPZ+VEhf+ImNHbvqZuNpJKGfnPrK7c3i2FmWbOVtuaRk4Ef6qNptrB8S2dYYhZFwTMw/TsZ1/LCVwrG5edJzJaRA8JtvzsVwqC85pPdY15t/XQZZndQKwSsp7brJd5KYWgNlDBr+zhN0XEj5uUEieosJ6+R9jBnBBDVDoBY/bEDfGzyTsKGg5NQNp5BZC9WAAsAXdEn+hLhlYVyo628Fxpx8OdHlsjxSuRbIIjsve724FSU3+6g1v2WR+XNIkiOFq7i+qGssE+eB8LryvuEa0iB6OCZszqyYw1+IPLKzehcqHxyhbO5rIcDkbWNwyhRpqkvhfUhaOVQgyArTmDuMRP4dGmeQk5GzAZoKiXXoY/s0scI9C21DSmkuc2F/48Hylpk6y/t3L4Ilcru80vho5/ZYEIt8YSWYL76NlFgVAIxA5vcl0YtFHA9YHnHyqrwyvJ2F/B+mVmloBQJ6T3O2Xr50WquMtte1fDJX9vyNI8rZZdADLKQ8SUSkvcSaljS1jUf08cK2F0Du0HhJ0vSOa7X4fJAyPayjTLZvvKmXemrIl5LicWJylHMSr4jyEEWfmaaIvk5NZYiBZgvHUec5UEb3YWtAUnasKRJNoQPys0fHNGXcNsUmJ9oRNMPsva0agNcHy4C/M16TtECEi/ACnuTkwdVKtY/nu+oJpz6xk/pcuw4ZTKaIo23MFHU0sviWH1RMZOr1Ujnt+4mqSIvMR/rJso4185Y62U1UCXESYPgcXhOtPguGjkoYW3BcGRN0Gg5xeueDCRc9Ji4K2NkGXQAZQGjjMmsfZY5SVcy/XzxXfdk4CxRtMsQhuP2z9xL7y7MYEXEmz37jtIpLQOS58yBObzBHO3EfrA4Z1aQLYOZvrB8tzeQd5lmBkF66McsJR3oY+SdFel+Xy9wBBvIP54Cncd7mT2mgVh3RvJMAetw4WH82aNYQ2rDFEhXoOH5XpglJw2cc0HiA4CzVk9n+1t6Iu7u2Hjmjqo8SDiuPPPvVGJvQ8ctkrs2gDGqMkM4Vb92ZMubAN3Un+HpVUxUfBqURoe78CDvwm2lEpUZ5ysHEG1znrf7UobYH7t/EgxkJuXz+CsxvBKtHirLoFdr5yRD/2DjQdu4/8sJ4VUjlIt60rl9C/O8eT810V74Z6n0HAkXNw/a0HGbNYDm1R2iQyrwrRXkq6Ck0WZa5L9S0y6ijPbQpH3jpHP7QxXCxj1lD2J+cghR+2C1rwU65p9WpNfpJZMQYP2R/p5caIHnjdSu08f0orfW5PXK2OIR0nVbiBDnhm+Z+TvPSX1WjANTpb23uOjUu+q48lOJB2RrA9k0oAqigUN+LGEIkeDrjIHmrIFDBinBZE+8s14tnCfRAp0Uz3PMh9vVFoK13VXehAnGqvNnmUt5P0GkmnMV/hcBbIqC1W+mIq1b6RgSndgMBGcy2Jhp0FOVBNcnqgHKDqUMD8nQW5MEIBxiricqATxg/Y+cwBLWRk8LhbbDfvO+C3zPc1p6OjcnqqAmeLeEbX8X8YAOCaWs7raOc+utWCcg9RFfD00Nxni3ZkrbsD11TDyImAnpj6CvOSfu57jj3PC3yr/ckNosmqczVPRGlQE9FRJKUF09cMhRY2Nl6V3P6CBXU9KqKa91XzIv9X84Du/gb+rL7S3ca00XFw5eqDkBrkGR/DFaLrbgALpoZYlcwtSHOZR2lfSfF2N6XERWEaQ8sgyypl3axaeUaQTzm7zA/5HMVfXfL839DtWeHof6Ko6zpLxIuyPmsbW8sjrLmncLaNyNM67z8sDJg5VV0xbIXk2mMTGF2pJh4w/7WzS4fDWcEwO4h73QaFl1sb77+CdqeMD2hatg/mR5mMQWPrJOjMQXC+6HhB4PTT5vtpt9TyJna+bZUawr/PrRgAoickiXHLWdjYFYvND0NLaFv14fTrLsZUoxrmTsPeSPmfBDRbj7DzqS4GuWb6lgLr6YAYQygzzkTXcd4JaDWquSCLRr1F5faK7I+uMma2NF8EztCBYVwmx2zX432o7Hz4WMErQsV12RV8tbVb5G0FfbmixF6W7+pi95jRHf50MjrRoNNlSDGVHTwI/YeYnEZglifVHEq6mXTvn3e55lrWFKANOl/b/FbgNJs494xngVqXfuhdyJzHR0bUEsWIhb+65K/brC+jMs6o1OhoGHN1GqzE+Gp2dm4B4i3HJ23BCmJ/W/+gPp6e+rG57B6mtqbWqwr1pkbNN5uhc0Awmg9R2z4E70WccDF6lrM30EHDFimMsvsn2g9zZj/tsfqO1Q9JCK8pbQy1GVC6dXkttZOmUFUtNPETBqcJcFQiNtIIty4/QaDGcSeYfen9P6TgI8P/vJh0qpo0bzRU1KGH7OxhemafXo4pNAX1EcJmE9CnGu2GDSGzBx6bt5IBMSu5V6BE2326xibGar1Q4ZuChWGlu2D1FDviHS8fKOtJeHTOm68jVFVsAKaE4FdiNcgffINLesTVwhgDbaWVdTZC83szYt5Tzzt6XjUuHJyVo86bVznCsBvIo5CfVhkH8QCaTkPisZBvaWh8wFWJlzxtWDTixknfP8xgHD4Md8GsEceZEHnpSYq19rKUHO3mSE8z4+trJpDd1vFjYVUjglgu+4X4NleRwFE7dSFY/QriGUsXdhgoLLjJ2d53UYnonGLmrliU4wRA99i0hDjbwG7n8i2yupjrdsrQFNcws+tKi4aY4HEtbgcR/aQw739UsOjYKgXsTFa7Hexa276dviRdFCwWtzlntmLUEWN5b/bq5L/sLzDT7swi+QYsTJ6ewDe+TSGDAaiOk7E/5UW7FTuAd2jTalwuup0QFMU3xAScEBRTn9IHuQ3O3PslbVo4Tp/cW/9Mp/YVSv2owwQ4Vd5GvE508Pseq2ClrNOJIY2dSEP5K6KKeRoT+/UAw8mtKlTIyar930Rfg+gGEHmuFLwbXYF/q3wP25unE7C8ocFZDzfCvO7RZREcp8hNEyjtcc11A5BZz1+2nwnH4j/UeePp1Pb39dYF0HMOc1wEYATrSZ6xbADGylEaJbUYJSU06FRBD//x/hLEJ4ahSnQ5IRCZ846S9nFwT+6e2REOqkguTcQGD92qMWvmxpuUM2bnvlSHOScV2kTYnzyl0yCZJBxO+elyMzXBp7VkcfpOow54wahHf+0pZDak/egNkIWfdLZ9vm71/3HFPzc86QnvP3RPXuPw1KUjBXZofHTxxG0EIb5MOv9h0MCpvyzhc5YRwjpLMVVK5clgjQWII3UUCJGXcP2T7CiU4A8drMAP9GchcYc7oNs6+N+UesvLq6nUm1I4XxvrqzD0lFx+e089ZFWTAkHWZcP4ehKx5Q0JBK4Tqs4UzLZZq1WJ6O0ke+7CP0qXGGNuhYiCx5DdlF4Uk2YUe0IAbUR4bFywrYszPSf4tk6kZI6mG+xDpshd+Xl/ALR3iL8tuDXgUKe/HW5Z0ZxmgRJMystbzhN7JwmfgwEC7vMxbm5O7EWKzT7gTeh2GiulKEUQYFo8IvmY0x5Y7MfpugLzX/NXDXzf6cNKwah8SODXQRlUF+4V/yJvlgDFWDe0kC63RiDKeIkFRLqe/H2z8XOLlwyVzR+qcsn460hwmlGtwcXc5rW7y5GXrG0q4cuezm9vD0Hdym0RsU4cf1+gDH2KxyOCQ93lz/QXgbj5WfkkZx4v8PvPdmEKOyxg2YHXOZiIF0+JnaeU0qN8qzTzgKV0konRZvAGYnZHXX5oqWjkovut7bU2k3PmYod5Fl3UXC7/MgTHb/39ULn7OQE0qN4qTYcxfI6SmRTUQZfUhTeYmVouezo5ZauNn/u6usDemCm/0n+hI6BXrmRK+TDOU5wf1Huud4m3U2RjfVrkvzKAU5wLczU1+Ru7IKHXYDvrBeN/QUq4/wEG5vCfs9g+2Bkha9KXy1vCD9d5uDgAQfX5RLoCiEmfIAiMWUUIPdXsNsBICL1uNPB6p3A+bzd7TqgrX+9GsrEDQmFDOyao/3s4FtLYHYywKJj0d7aLSX16SPJppUYlva6GYSlppyw9GudJ4GH9YdlgbHdCTc4fmQOaeth2pSLe+eCVhRQ3cVBs3vNGAGP0geGQFT0FnN5cwQ1WIus0Nx+hC3ONLLggmx+qLKLmDWXw8Wodvarml/oBYxMoLPkFf+UxIlBC6+fivoW90p176Sq5/vxwo1uIb3+0X+YShh1Sxs1O/cUjuzY+nSmW0QMrDbcLqGx8c07SGZX0o74rm2tKFZpRNQRahBOdwq0Fo2bU8gQQD5Jfql0I40sc75hlOjnBaWWiB6aHE3IxTEGw6xWDVUtK2rKA9tj69oeS13DCgEFuNfqzrSFEP2jSG9ckfkQMbHilstA0UFy9oV8Te0AhTDKLo2VSOS3uywXKn2DVC7W8riXSr4SCIpOYokPtgl4TyrJfJ7vVwRX0uLR2N2NPQ5FhltpIOXw/dBVaaHCE/moCg3lbRWCFaz/b6dXBc2mTzr76CBLuyUnHGEF2o5sEpABMUFfJbxhF2rt/JhrXkptNHVZ8fYGZlGLiI4+jGzpJpDyArHY0jKQRwmYnlAouXjhoiGftmhAaHaOzkXLWM71/7tMw3TslMTxnKQfIuZvWSHYG3l97S3mE6CrgdA7pgpQzlF0Xm9/ugjcoGzg7sNCH31MEk861k4dMMLydB8G6qDkd9p3epmDHGOnPXFJ9nwseYPM2trLggTNYZpx0/nhdQWjykvYQCHtzMqYlzjSURZHRQNwDt5J5SeTR7Kmp2V5p/R0L3oL9V7odHkRs/qN98kjBHdLJGaZxDrv/jBXpZQ8MoNdIUifIxPEhTvo7YpjC+IaMQLdmYVyOQBnAJlD4XDLyhDQnualA4fl8I4zo4+F42a0LvThb7UlpSPz75G3Vw809bxlJ/r6h8eK2Poc2YPnS2cIdvIqa6bJFznpKpZkLVAm5GBlKWX09sHQuRCuunS9I3J7M6ipv9WByZcPCSTVirlujD6wh9NieQ1Mn/I4p08htfOofaROuYzooxTcMhMxWKOw3Cu2I7d588hJu9MFOk9kZV2+KyqEvY5vTTvY7mJWpgdzgMZjeA2uBAKsxpdLq9GwfCW+AXgGaBN84fIAJ9Uh3Ga2Ai92eXze0cqgXbQQRpDo4oV97EA9RPG9veIhpcFkfdUsKuOdWseZ6kS3LYXs5qm3ae3/pFvBCTaHGmxKEnkGidS8OmFRK832BtnWXEUW7M8LeUALTUpCCT6z9yl/qqcPAkrIteth0lFk7lBu9H3oBiOWTPVGBVymJBfrtCtBN0Gk9/h1IVbDSD3WM4dsLLQZ106yQNCytQMO4MqNphCb0gjn9wB8Sd+rUCFUX00Xrz4FXwcvTechN2RINiNMW+TRjglke/zN84WDHtm0p2bZiG9IQtfOwfOjxomUFEDI2Y4b3efS6INQhJOBc5EbNaIDpGTgiXtbaFut3gQc7GsuQJIQPe/FkR3la1w4hD8Bir2XdeyuE0nxxpMh8riEqAs4w/iS4O/qMSZGP4zDw+titicp9wX8sfwU5fUQr1kpFb8vmFRjUnt8bo5GXYj9F2AQDP38sZFmxFCJuBX8ToSjUaN2KzdIxkHVKaV1ZA3otyF4tLsgJRhVYiJPp15MhcieLAMaCw7GIqxNPrwrfM5r21v/BoP86lU+A7VQ4iQJyWVucPsq/KGIfQCxubo1h0hSp7gYDnwXqwY4CZNhWocxgBuRHmCLWe/K2Pu8AojyPNmFcoPLsJHIWIvl8FSMO5+71zUwJgK7USDyxikKzneVhq6367Zt0UxYVgMtRNbudBs25cjh4DCvtGe02L1oj7xlVCdPXe+nsCAsTsOdoEd07wIGO38x05xaZ3Jg0cFjYtDlOY7yG9rvFm/c1DXzCUa9mET4Vdy1ios4oHV+pd6WkEbgtVYGKuMeGkiGq+LDQwfFJPd4gSGtJ3rJyZyCcj5NZFa5nB8w2MlP3k1zxAvTIAe/5bZwUu2KKirxXq9fBD+j+HPpu9s2WZ6CfkPI2OmJ2Lvk2WmN47B+SXNBu/smk64w/0naLBoHjJ8cob3epmOGiA1eKrG1m7aAWd7fJnknWM7lxTQc443lvtnq4FTfAuEpguVxaeQlE4kq3PtPgQV73a9ucHgCwpvTFGFdHcKVU39Bw5suvRV5/f9/ycqp+RcpGpfrREy3czLJsnUJ42SHF7NKpxhqUFkPcsdFZN1rQ+iD5drKVFIYNdHLSMQvpCkepTrM9NEO0qrJVa18b5bwcyQzfBV7XTqLImsWY9QSO3JbZxJ0CWrg8axUbJGU4pDKzdwTol/uysKAPA35bZbEe751KGgZd25sG91H/kC9+RQrLmEs7EL2PS463oRtBMYmg+shmGslQb5FaDJjNzHJyOqV0CP0orntVYp6i2AL8prqph+ANOCF58pr/HWV2Ttgvrw9nZckPyCoCuXCZkoXeGAuf2ks3bp++fRtpS7qhWrcQa6F9RYT6zWLFKt8WrKRZf459CO21cbs6vqN8b18UJzdCJep+D+uBgsSSz1y7iUI43EfJR8OkJj4yspG1GDp0RRHT0TpT0/JjwA4BaEnQOJFBBf7tfDJ3zqTDN3oTm1+0onrvUJbA91D+8NOeMzzMXK2haVxZfz1u0FA7f9WeWZUpDE0MCiIBmbCIML+fEmH0tvtnG01lyNDt7Wz+2cOwoHcStUMQCJCR2Cq4Iz60/lxSPZQGNxARGP98S4L+8QTY54WqbutyRILr8de01hhCeTeYfE0EnT4fjTlvJB89I1Ko/nodfZ+/+e9YgYaq+Mp9E3m/l/zAYAEtrE3jQjDQ9fS/E0DNpTt/pxGI72Ou4JJlERS2gvPkYzIMA6U/Fjgzru5hTOt3sStw5rV9cF05zIAueQMFru9ciWZK9pVzvb3eKyd5H2OS3b4PMST2ez1Rz1ymIsRB8lXQ7e1xeyUgk9N6h9974TvWcwQPtwqRk2f3VkMCZiRJLhYWIqo97k2e2PHSh67YhQmYv1Y393pUpYPdZ+KGrBvEE0Qm2CjLKmpR8XL12S5U7q1rUqWEkg1NMRnidGiznhkIAoXy8FqjtX6275J+iUIF+Wm1bhgAtNG0VmuBYsGCVUEco0gIUyZzy7aXMBFYPRyC5njiOcxXnJaM/jXIScezERO5b0lGPiDhXsjiaNzXqIynoAiX7+nlp3YkNpRNGTo1MteKGek3v+zQnOe4eAtM3p/ObpeQ/7tAB1AtBnvKoKJ1DSTSghMBb/9/ce2Ibk8Z3IfIq1r+88xoDPiHy2Wp1yzoPSz0dY+Bp7wGMcK4EITSrKjK9n62B7X/pfwklbCB7RkNKt0Nklmwipz6frXuOrvhBNhC2pOnrsioyTiRLFfLo/y06lhj20NRjc99+207nArwhavzQn+DwoGOPF6wIQyqqBtQ3CuOxpQqgcKnxzNX58Fe1MJruxMRLZEmoPX82yAV5WXH842mg7/xhbJJf9y6i2rt0VhqT4JvOqYV4QPNh+4HxDRWk7uhUT0J8mpHYXQcFYzNju5NRAPE+9DZTjxl6RhbYaU1xmVHu3j3sFnC/XWHroAQSa85iIhHaJ/ndqhtAHMHLBtpQNUZp+CfpCzFzPNtfiLCOJb5fDVyY8E1cf4fc4svDtPOHwN889DQuSC2DaUMdIPvcUzjjXCTGKZjTtZ7mgASO3Wd3z2Cl1NjtxDEyC4NJzkoCQm4lAcZ27sE+hrGkJdpqdUWkHBkD5w2SD8LOSifnFcIFebYdgBIulLhrskuZeYWkNrs5G44FEVU9QRuRtnywBQxplS3Demk9unX8bR48AI+9gVFA+nfxRQMrlj2srRu46GFghn7salho+/2J8VeV9jFomZNe2/okOyqdsH5DSiZUsGde35AHMl4nr/NYWRwNsp2P6SR9bsU8+StWeUPrAgr9kKqq2WqpHQ1bj8dB4R1tbmeAvOYYtHIeGjerkGBz5Ph0bqoJL0uegerm+pXY71Jv9EsFX6VEGKvB6RH3P7wK2qFqV6+6ljsfXzF9p9H9YpQDLrEl8lXr4M0WiNR0eYQYfL8jrdZJX4Lqzhrl7w83wuvhhSkWh6ldYMGopZ0Ubhura0Vwk9E/+j9C7H45YUK36Ivw+syAHE9wDhQpFiW5X4Fe27J8nB7b4KDDDA8PCkK9pgM+cq57IiOlAzuBjg3YqyzFcUJW7LiWFNk/9x2aOY/zTImheRehOyWwimIGW3Wv9eRqmlAXz3JhBExRUpDVO6UVlmNcKAASxTs2tLlLqys5GptWqj+TP0Q0D1Ie6zz7lV023s8P+krDwSrK8HOrLlkuRxMsA5xXIwitbrC8o8UGCy7bGyqbtQnT6OEuJNr0ZfP8fGZWyNc2jHzjWfmDxYhITfYhUo3Q0zLhP7/gQsfirZ8qS88DEwvuEDIJ0OpsQpXpfZPbK8C005n3/dMx9dPL3Eu3qUNpJFbIduXC5D93XvOWusI7PtoZcaywEJolImS9AjDadn8FK6rPHlNBsFlyuH4ArVL0JR5SgpbLD/IYxwueciUPZoJanhglQ4WxiPLt4LEuf1zz/7rFmXbYcI8CMOE1uJdoFnE92oY8bFAmVkOCVyaMRAN/vcobzXCV1X2ziAl8nMAeDlaLletm0vFfuYkLpMb2k+Yw/r8plBVjoZyjea78BDvvWxeJgRd4McYHzgWlN7JK2uYbsseOUkhCN+GVueR6YQSXSsHAkm/IjkbqJcqIAK9PqyqS/bp8Ym5skSB8FsSnY1Sg2/SUVb+JroniOeS5pfVBz0F4PkPPOanjBXUB3BQC5ruQ02bLzRt68CAUIa/vq3tTdmxtNM84qlZKKDORlljHDaFRxMfCpE44Img7OtkwZVAxDtet51WxmuRYZvTm0iAbgoCeirl/aIMviTWA/ygD35OaZFILd9ah8DHD+iBNEKciwc917z7VCUasOJIPI5soF/D0ff+Rvvi4kK/sEXMry8VKyahRbnhQ2lhNzP/Uu9sLPBJ5fxXJKzrpecxul6p9d9DO5q0KdaEa6J+Kco9SCt+XRxBLyRxz7MdSkTk5ucfAwizsG5x2vkUCWzbIj3ysK74ZV58geViWip0hNmLB60HFgG9beLGOBIYnFaXW2Tm267xv5yj4gCUOmuJdOw7ik38YKnIUIKbA01dK6USA1gJfuUuD6NCGHcl5SQeHal93JbWKeCv/Raew/QVtWOmcTbDvcVh4A0nUuk0vvErTNRliB8asc9PQnHpstvlP1UOs/h+860Kf78fI8/I69c3ZKXKaxkUbO65UUV2+lv22bPKYlEcbUc5tN1VNGwz5eWY+IXbSYjSXlO18dMCCD6wiXH2SCNFkHIOtIHbY65XgLeIuAd7X7rtTbcrNS0kamnlHEWLvWUiTNz/Ab6faapQok9p9Fa94LS0qB/1dBwpIu/C3Yj0iRqKX5rQSbFjMGwJEU6Uh7hQjmRnktzuVJttos9FPnrR+abPX1B+WEj3s7uSU2WJtfMWciy1dPeQ5ASG1JiPnckVt1BRB/J35df4zw5ENNaxQ55jMzhf3kvn5MY5gnZOAelJtLQ1ZZQNOalZIpdFoTGDs3O+U0XveDAhjwKx8rgY1rWVg3w/SoPgIKHg1Xmh/je/XE5jFVImtQiDA2z0jCTEvyoToejk0RGrmfvd3MnCiNEdjGjIYPX7UxA3vVR4pmCcANXcPcRF7NKr81ECjX/ysOvT6k3APlQMR5a+FwhE76MnqT2OlGZ/bhFobFk1WCgw90jB2voJA34aAk8Lgi/adSEi1atp5cUfC2MJF9xZ+mu6pW6BcUUpbFPe5czc1HxL8e54ArcS/J5lNPsof3NTc9T99vUCi0Zt3EE1TMUBbyeiD24WSSVDLO2W94aNDcc7lCWJwfmMkP10SXK18RQ2G52vEdXgEPDBRrk/ihCTVZwVnpbEVcu/XW2DgiTuRI60IcXjDUGHIMD53fIov6qQP/NpBH02EJ1JQolqI73urJ2GeQCuus6VRz1O3BANmeoqZYNRffupXfXPQ0/6TxAYxyQaRZbKYOYG8gUhjHv348EM7pxwOHIGWiMqX6FwJMUFfOViN8vAiyasSqZJ4ztQ0yjHtdamWBMfmdDMl53EcUYbnlb4lUt/7mcxhIdC0BvzVoeSGIphp8FWXi7EYP5M8PAMbANMMbta8dFdwKwBLSsRR+NWb7pdYuaPWSE35y1+BI8hS8FwApKQZ/xSv9sLB+rYGrXVqKgMQKQvS46knGfAzBj64WEoyJY6zBPaCmMqX73rVn2xDpGs8L7MsHH3/VXVxsjDjSEMBJe0LXCULWbVexk2r2ckm0srviR7He66RHe7iEs5KPIHZQlpb+4ZzE2F+gtMCzC7SEsVhj04yqg+bw7urpo82z41fFXTEWjuphvgL05qDQdYifhVSK3lzkL5WKsFugnITY+RlD8rCXXB72VpDU6b9mvPcP2v2fKrq9BqZXp0xHkdDIZUK7YbdHKEKqo9NuWkhzc1dRQbgBTPSeLZ3my7NCMR0LK3S33btpWn7W/1TGNRaLphGBUnFxeqo4Ysuelp1F8zdAsLrSi3QZIaJHpPWANcMYXZ5K0fwL8RRyb193Wj3/bFXu4ig3nZyzndaBVe7ODoqnLpH+dT2B8ya1AVDMvm28v0br8ivVGnEn4D26g1F4UwtCBSlKZCOkqTx6wB555wrp31cOY0iyIbg5mE9/e5wXk0PZCAqBAgyNDowFWVQwRWTNVGi6gZiN+XjqHLMvWTzgm+SgNdIbupQ+gR+E8RluIOhgr7be5niQx/uxsdOU88wLNiEsQOWOAdjSFLIKMrXbg707Jv5vxfUqWfY5V78Wdg3PM68acsH6cYghAXSDnlWGibwyuxgQYHopjEtz78pLS8vGazMAACY7YMHB+dKG+JJfBUIgCzRdbWP36YnDsUAQsXNtwD52DR8zFNp5vcATrGTEgVuIgYj82YqvgrGFmOxGLamXWUIsoKoD56oY+A+ctVdlihS6UKeXbT9Npno2XZHuiJv1NKxS9nh8ewX/skbHR7mk6ViZnrzwcUZa9yORFxgyTy5zfN15SCTvSpU4Ygn144s3w6ZabOvStzScjvFxr49bKNl4aL92V9k6MhzP1Oezenp/O9Fgr8sNnolm1mdxPVvA2EBnGKY4Dfobfg9zo7Vv189gZ0nH4b8Fa9JgvnXtuKzV6LHMkj3uOZ5LaVClhR3eA/r0MZOXPK6I1Bv8Rv6iM0qx09J+nNYTd7tHgfT9LrYLMTlOxwm8J+tDy/Xqa4icZzM/qOLiR9JTqTmS9WvH6ukTvo85iOUwAN0fkM2QE7Tq5Kbt+wIFFWd44fCF/tjX5L9PuHzaL8c1TYFrRTO/4cHVBG/eg9wd4Vi9RIiOo4EHf7S5jPqMsNOorGibg5EOoZ50kVWcMESWgjb4HYmwQeszvLGZXY2vnbHqI3j7KfvVTJwn/gy3DPK5LzBqwJJRuNhzdRL61508C0KKEkGvK7g9+2PFz11rK5V/4lcjSta8whC3r5rONjnUcILaYaF/CYfVD4ludiyQkpJs/6arCEmUacWI1x1npmIMf00etvz2Iyriyja/QXlfrpsvKqXEbmCdCioP0DObTVDDCQPtnZp4nOa0K2q7UjLK9hqed+6P7Bjv6pM14L20+vWWiXHRqDzrdtBwLYY2Dp+omZFIByFbIMrZLOg5i2K00XMsMEOXwb9IuRgLiCEpR44QDZgaMP89giS11N3VhQ3IIcC6QkL5UI8DimInMxOuLyvSIZ7Oi6i0Fup2BLuKZuU/jWPgMqWMOWdSkmGK5h+C1doCB/WiNJ2MTbd2spdgeya3o/EWrniTDBEDLwSJIcNEc8sBY3weq1BSKgRVT/fWJce+kW5wsia9V4oU80ihmAWQac9PzsloJt9w+ED02bHxtDyFTjCYC28W6dstEfWCykg5JRHXFogecUPkxPeWA1jFgW8b0QmOpsVQtMTYKZGx6KPoud1I7vyDBz6MAQEKnw6VlUS01DEhXbWtz8RtAz+zbEPr7h7nQiazCd2cLuKuD3PE3PAioeBbKyih2+Q1Mr+yP0yVncF0Fk/ZDKtzBLdZ1LzEXWUJrghkkcxu+1+d15KB7cE0WLw1SPifbeJc4zTUjE1/PPNurtKtnUYUGo51lYx0MWdPSFFPaoTVepowfMIa0Wifd9V8qxPVJMYRoUuXVe5rJFq0snDZVFkgjckUDIoe49eX9iAuEmyLNyFTXJos16nNz9YMZSeV+0TU+BD6NlBUCn/Vm6dFY94b8UyJK0adWEdoOmt7qqiUacP81YJlyQ6h53Ymw8xbBT1UpMVuSEcKlxlUmQ8pp473jStqhgF/pJbZCLdIkGQBDPCVH7RGXjYSoQ9148LZSRccokBmifbUBMZaZ/U+zwVEY80HmYmYUVzrsp8orvgEwM5i+/+30jcW+nsaIOEO8MVUMW6PV1NNXFTnNXwtw7oP/aC40fHART/gX8CmlELgEHKDLf7+KvZMGeMt9YXOjyrULKsrnabDtXpifqSmjH33tS5bQjO1k+A0USSsyTdMD24Kw0DhmWrPMVibOGOHu2pEwAtqrUDp+//ZZRNId4xbayE9bmpQmdCjQn20V0v/tRVI/b2R257xDxD4YcvhuqlaR6ICXD7gRinVFn0gpObG6TCmUpJeymNoIGSYoTzu38sTPnDwXCBZMj6o8M56F75PO+1cQ0k3mR3QWcVIutQmYX33kyHGnyBNmDVcqxUNNCTQsXuije9y0nKKWBN3jCJO32CPcrDoGAXbx5wAA7wYJDG4QxVj6VZ4+NM7X3GTO396hJ1jgDD8Fni3qxJE2nmx8dfLxISVP8OPIKURnovmaNjLz1lCKFR4cn7D5NG1tctGTm6dJY7OXun6Mut+Ty6pWjbIIAtctMtCpKfB1+T+nRz6NSj/ZYT/DRB4CxIOIjMqyo9S2WAEfdZLI/qdSWtrJiR8l0PZrM6IFqi3jVdap3QEz5aGhD0SsJkgJOBJx1KsUSgX0N9jxVJu7ueXjltsBrfhcT/dLzwV/S5pXLgBDsdDa0RV6gfPQ3nhGkHKYrBBAr2qZP5rslC6B5TjInvj9iF7OJ/kdUj+0qyR9Bs1x5H4VyZjRrXeo4WSTtXTGDvsPRWkWFwdPQ4FYnaqOUnJuu6xw58RnKXCl39rLsw4gSaX4IjPDy66oiEkDMqIAtCCqH9lf0H7xgh+0ux/1ludvG288NpYF4/rstxxwIE57Eky2z6mYLA3+YxzVWuKCSJR4cBo6FgX0CLKggQU7dZnal3rwhfCLsqorYiRr9Upv1TQl95L6W+GRVfmMLK2yNHYMMoQOOZxQdrHXy1C3myUFByUkEqahGfEEsQQpfX5w6Rdu1YuEuIGyxZ8gl6LAuddATNjKik0Y9oSuQ8Yz5z2Ft7LFzRhyPnfpDjyZFt+ANlLwkM/uKHJ2urVQVxTv3KqSSxYr5LgSLPz3H4dHis/F04D1+0trZqmgUkO4CJdx+MT3y/dGUqmhiwwPCjVpwbh6umvlNtomCeUAJ7p2utNR7FdJ6xuQ1qtPbivc3Q7TJ4JYiQ37NFPbQcQodp2+NPKQZRZgPAYQGsaigEtT0AijUFBhVyL9K+soldBLdcZCyaAXMeVXr2HXt7A2yNlPvnHElmjPBTOYsmwT+m2r1m8D1K4n4jsWjrhEjvsJWKK1qOdBz7gEfAT/OC6bqi0eworayciXpk33GUlYg7wvf1t8i+g0+Ozbal5e8c2ij6cY8L4MUI8UfzaDi9zfw7Y3nIJ1HK2dLTIGXKaxYEPXm3ce14uEjQyIx20LEwwL//Av/1deKKGAD82Jwv1YHkZGT10mT/4ZbBBsySEomnqyGrAXnidqc4C6g4CuGrFyaSn+voTSTAJywjHCEG/OZ2pGarD7aIUkf4QOua1Ltlvpe+7DtBSelBziAuUlGuWtAAoBWa4tSNCoSWbx1AXrk7C+X8rSRdf1jLrg/JSOcfhvrCUwo9FlBiglHyXoIBBYapLLzVHYC/5F1Z8CrsQigkKFEtCGS1z6VhxTg9rMTZwa60sqDD/QVN+dLWpIlFUSu7XszqfqPTtMm0owN6FvqhPF4ovtqpKJ4bNQCivotI4mLbrw2yYj8/D/n4lCr2PPlxn3dGuwIpeXJt2NzSIjvY3pkGD707I/fjLVeKS979pQZxuJjhWhdqtx/PrxJEtctLwtyxA2WyZo5KJPz3ST22ZUohuj1Oef3c9B9es4h7ykvjRIavDTLOwwN7u/TX8RulYVuWCDzoUmNNOkIP8p6jJt6MMaNCMAhY5KRhyU2lC5hZ8+7vfqOkS0e95xXIpnUoxWRWlCFNSjICkLFjFhUsY5h2/pwvA0m96UDGHoMREf6ghdJWEdNlnAmR3KNokjRinwLXFH8rLfRmP4AX1+OJlulmQfU2TVmoXUQG9r3yTykOUKmkw380OyBjE9kdmXI2FGI3Toc+Jbf6WJHFH07gHlpVWw4Z//dG8aCESZm6J9hK28Pf38AM6Y0i+XFCVX6xw6aDtohTLykUOcVZJCedVGY9ZPoTwGxIp9TKMoo3ouIgNT7NkZ5vfOhBe4o9/nBmY=
        - #1:
          - type: tool-result
          - toolCallId: PkchM5YGyh31a2N4
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: uYqnku0yqgDQnrVu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 1YcSIvuJ9Yo7uRub
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: LDm2grEWDEDYNe1R
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: Izi4f2e7cZb3am92
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.