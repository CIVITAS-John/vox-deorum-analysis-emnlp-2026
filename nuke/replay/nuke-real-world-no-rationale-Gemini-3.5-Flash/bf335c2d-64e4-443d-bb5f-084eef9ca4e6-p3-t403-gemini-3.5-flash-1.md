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
        - Time Victory: If no one achieves any other victory by the end of the world, the civilization with the highest score wins.
      - Opponents: summary reports about visible opponents in the world.
        - You will receive staff members' diplomatic evaluations.
        - You will receive each opponent's publicly available relationships.
        - You will receive the best available location for your next settlement.
      
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
        - Technology: Penicillin
        - Rationale: After completing Mobile Tactics, researching Penicillin will unlock the Medical Lab to boost city growth and provide fallout protection for our workers, which is vital as nuclear weapons become a realistic possibility in our war with the Iroquois.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Containment is a Level 3 Freedom Tenet that provides a massive boost to our delegate count (+1 Delegate for every 2 City-States originally in the world) and generates continuous city-state influence through trade routes. This is the cornerstone of our Diplomatic Victory.
        - Policy: Containment
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: The Inca is a major powerhouse and our key trading partner. Securing a strong, friendly relationship is vital to protect our borders, maintain our lucrative trade routes, and potentially court their 22 delegates in future votes, despite our ideological differences.
        - Public: 30
        - Private: 30
        - TargetID: 2
    - #3:
      - toolName: set-persona
      - args:
        - MinorCivFriendlyBias: 10
        - Rationale: To secure our Diplomatic Victory, we must maintain unwavering loyalty to our major allies (Germany, Venice) and maximize our friendly relations and alliances with City-States.
        - Loyalty: 9
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Mobilization: 70
          - Production: 85
          - GreatPeople: 75
        - GrandStrategy: UnitedNations
      - rationale: With the Manhattan Project complete and Bregenz's Nuclear Facility active, we need to boost production and mobilization to quickly manufacture our nuclear deterrent and complete required garrisons. Additionally, we are boosting Great People generation to accelerate the Great Engineer quest for our ally Assur, which will solidify our Diplomatic Victory path.
  - tokens:
    - inputTokens: 140306
    - reasoningTokens: 6318
    - outputTokens: 384
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Grand Strategy**
            
            My thoughts are currently focused on refining my United Nations diplomatic victory strategy. I'm evaluating our progress in the Atomic Era, turn 402, on Prince difficulty, to identify the most efficient paths forward.
            
            **Refining Diplomatic Push**
            
            I'm recalculating our vote count, noting the imminent World Congress. The "World Ideology: Freedom" proposal is key; enacting it grants us additional delegates, bolstering our path to victory. I'm also clarifying our research progress, particularly regarding Nuclear Fission, to ensure optimal technology selection.
            
            **Prioritizing Ideology Benefits**
            
            I'm prioritizing research to unlock the "Containment" tenet, which offers significant diplomatic advantages through increased influence with city-states and additional delegates. My focus is now on the immediate next steps after completing "Mobile Tactics" to secure these crucial policy buffs.
            
            **Securing Delegate Gains**
            
            I'm confirming our policy selection, ensuring "Containment" is set given its significant diplomatic benefits. The immediate focus shifts to resource allocation and research to expedite our path to victory, while simultaneously assessing the current military landscape.
            
            **Updating Research Choices**
            
            My focus has shifted to the research queue, specifically scrutinizing the list of available technologies. Given we've apparently already achieved Nuclear Fission, I'm re-evaluating whether to pursue Refrigeration or Penicillin next to ensure optimal progress towards our diplomatic victory goals.
            
            **Evaluating Tech Paths**
            
            I'm currently weighing the benefits of Penicillin versus Refrigeration for our diplomatic victory pursuit. Refrigeration's trade route expansion is appealing, but Penicillin's city growth boost and potential fallout mitigation appear more critical given our ongoing strategic considerations.
            
            **Choosing Next Tech**
            
            I'm solidifying my choice for the next technology, weighing Penicillin against Refrigeration. Given the ongoing conflict and potential nuclear escalation with the Iroquois, the fallout protection and city growth benefits of Penicillin, including the Medical Lab, are proving to be the more strategic selection for our diplomatic victory pursuit.
            
            **Choosing Next Tech**
            
            I've decided to set our next technology to Penicillin. While Refrigeration offers benefits, Penicillin's advantages in city growth and fallout protection, especially with the ongoing conflict, make it the more strategic choice for our diplomatic victory.
            
            **Selecting Next Policy**
            
            I'm re-evaluating our next policy. "Containment" offers valuable diplomatic boons, including increased influence with city-states and an extra delegate, which aligns perfectly with our victory condition. I'm confirming its selection now.
            
            **Confirming Policy Selection**
            
            I'm confirming the selection of "Containment" as our next policy. The delegate boost from city-states and increased influence are precisely what we need for this diplomatic victory. I've also reviewed relationships, noting the Inca and Venice are friendly, while Babylon is neutral, and the Iroquois remain our active war adversary.
            
            **Assessing Diplomatic Ties**
            
            I'm analyzing our relationships with other civs, particularly the Inca, given their substantial military strength and shared enemy in the Iroquois. Maintaining their friendship is paramount for defensive stability and strategic alignment.
            
            **Strengthening Alliances**
            
            I'm focusing on solidifying our relationship with the Inca, aiming for enhanced friendship and a potential defensive pact. This strategic alliance is crucial for border security and maintaining vital trade routes, especially considering our ongoing conflict with the Iroquois. I'm also assessing the diplomatic standing of other civs, like Babylon, though they are a lesser priority.
            
            **Solidifying Inca Alliance**
            
            I'm confirming the `set-relationship` tool call for the Inca, aiming for maximum public and private diplomacy. This secures a vital alliance, crucial for our current diplomatic victory push and safeguarding our extensive trade network from the Iroquois threat.
            
            **Refining Persona Values**
            
            I'm reviewing the persona values, noting `MinorCivCompetitiveness` and `DiplomaticBalance` are strong. I'm considering increasing `Loyalty` to solidify current alliances, but first want to confirm its precise definition and implications on maintaining trust and preventing betrayal.
            
            **Boosting Persona Values**
            
            I am now focusing on tuning our persona values to better secure our diplomatic victory. I've increased `Loyalty` to 9 to solidify existing alliances and adjusted `MinorCivFriendlyBias` to 10 to maximize city-state relationships. These changes reinforce our commitment to diplomacy and prevent potential betrayals.
            
            **Refining Diplomatic Flavors**
            
            My thoughts are now focused on ensuring our core AI behaviors align perfectly with the diplomatic victory. I'm confirming that our existing flavor settings, particularly the exceptionally high `Diplomacy`, `Gold`, `Science`, and `Production`, are robustly supporting our current strategy. I've also reviewed and am satisfied with the strong defensive and espionage flavors.
            
            **Tuning Defense and Offense**
            
            I'm evaluating our current flavor settings, specifically for defense and offense, to ensure they optimally support our strategic goals. While our defensive strengths are robust against the Iroquois, I'm considering a slight increase in Production and Mobilization to expedite the atomic bomb construction and garrison reinforcement. I'm also noting the need to generate a Great Engineer for an alliance quest.
            
            **Boosting Great People Generation**
            
            I'm increasing the `GreatPeople` flavor to 75 from 65, and boosting `Production` to 85 and `Mobilization` to 70. This is to accelerate the generation of a Great Engineer for an alliance quest and expedite the construction of our nuclear deterrent and garrisons.
            
            **Implementing Strategy Tools**
            
            I am now executing the final steps to implement our late-game strategy, sequentially calling the `set-research`, `set-policy`, and `set-relationship` tools. These actions will secure our technological progression, solidify our crucial diplomatic policies, and strengthen our vital alliance with the Inca, all critical for our victory pursuit.
            
            **Executing Final Strategy Steps**
            
            I am now executing the final steps to implement our late-game strategy, sequentially calling the `set-research`, `set-policy`, and `set-relationship` tools. These actions will secure our technological progression, solidify our crucial diplomatic policies, and strengthen our vital alliance with the Inca, all critical for our victory pursuit.
            
            **Refining Policy Selection**
            
            I'm confirming the precise policy name for our selection, ensuring it aligns with the available options. "Containment" is indeed the correct, concise identifier for the desired policy, and I am confident in its execution.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 1yQU68xIT45lh4EI
          - toolName: set-research
          - input:
            - Technology: Penicillin
            - Rationale: After completing Mobile Tactics, researching Penicillin will unlock the Medical Lab to boost city growth and provide fallout protection for our workers, which is vital as nuclear weapons become a realistic possibility in our war with the Iroquois.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 1yQU68xIT45lh4EI
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
    - #2:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: FD9MqSsZCVEgmqKU
          - toolName: set-policy
          - input:
            - Rationale: Containment is a Level 3 Freedom Tenet that provides a massive boost to our delegate count (+1 Delegate for every 2 City-States originally in the world) and generates continuous city-state influence through trade routes. This is the cornerstone of our Diplomatic Victory.
            - Policy: Containment
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a195pjGBb+FWVbfKrei3gX+gmS4oOqx4SRlxWAhI5YDLxQh8HCl2d5xbkSPHBBRYzX5w6UZu9kn9tHu0do9JF4UyKUnNzznVIjRGrnYlAKAuiqSgrg4GHDH+JN9M481Pu/t85gJHIuKyT9HsruyvprLuepErCIUmU7hRcmA1lxeVFKPhDJTe2a7mk2nYhi9SfpEoql1T9TNKIN3b/XUPieLK7rlTjUR2HRMB1amhAMLbr9ZpYoO+f53p+3LbD/ULPJVv2LKV1u3oYjnQQPjVw2kxCZXNkScRLsAzyl918sPuNxW2P1r8RvO7JwlQra6Zg3b/kg==
    - #3:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: FD9MqSsZCVEgmqKU
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a195pjGBb+FWVbfKrei3gX+gmS4oOqx4SRlxWAhI5YDLxQh8HCl2d5xbkSPHBBRYzX5w6UZu9kn9tHu0do9JF4UyKUnNzznVIjRGrnYlAKAuiqSgrg4GHDH+JN9M481Pu/t85gJHIuKyT9HsruyvprLuepErCIUmU7hRcmA1lxeVFKPhDJTe2a7mk2nYhi9SfpEoql1T9TNKIN3b/XUPieLK7rlTjUR2HRMB1amhAMLbr9ZpYoO+f53p+3LbD/ULPJVv2LKV1u3oYjnQQPjVw2kxCZXNkScRLsAzyl918sPuNxW2P1r8RvO7JwlQra6Zg3b/kg==
    - #4:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: NB91fN7T14vfIZtq
          - toolName: set-relationship
          - input:
            - Rationale: The Inca is a major powerhouse and our key trading partner. Securing a strong, friendly relationship is vital to protect our borders, maintain our lucrative trade routes, and potentially court their 22 delegates in future votes, despite our ideological differences.
            - Public: 30
            - Private: 30
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19Hrt9uM0+vplLjSosV6jkYchKFzpvU4Ipvg/VaqLwEnVZHFNgsxQOYc65t3Pxk1tYFylDnf+BOsFlly8n4GGSbIaOcZdYmtpIQlFxsNRX11Qwu4ac1U2q+wln0eYgTilMANoO58DL191Nl5X6+V/dAzCWG4K7k6HqHOvT8o6B9WBjQ8ux4oBt8c6PWHqyK69F1D3gLD/MVqHaO66Typ9fDDMoHaCrDlqQ=
    - #5:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: NB91fN7T14vfIZtq
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19Hrt9uM0+vplLjSosV6jkYchKFzpvU4Ipvg/VaqLwEnVZHFNgsxQOYc65t3Pxk1tYFylDnf+BOsFlly8n4GGSbIaOcZdYmtpIQlFxsNRX11Qwu4ac1U2q+wln0eYgTilMANoO58DL191Nl5X6+V/dAzCWG4K7k6HqHOvT8o6B9WBjQ8ux4oBt8c6PWHqyK69F1D3gLD/MVqHaO66Typ9fDDMoHaCrDlqQ=
    - #6:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: FscTzGRI8IOufdif
          - toolName: set-persona
          - input:
            - MinorCivFriendlyBias: 10
            - Rationale: To secure our Diplomatic Victory, we must maintain unwavering loyalty to our major allies (Germany, Venice) and maximize our friendly relations and alliances with City-States.
            - Loyalty: 9
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18wCoTngPXys+2/aSiqiUNxdSYeE7ws5Lwr5oEaYq5RK3hdErLcfajCe65qVg8x+zUu88IGDwOB80SbI+Y8VH3E0K3vxjKNpLkbkC1gxFfRvdPbRI9HYDdtLqUnjH/SbjIOnXXhYb8hSoipHNPi26gtrtlOrAYtguqlpBvupZkW88PYiddxkWIJ1jY=
    - #7:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: FscTzGRI8IOufdif
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18wCoTngPXys+2/aSiqiUNxdSYeE7ws5Lwr5oEaYq5RK3hdErLcfajCe65qVg8x+zUu88IGDwOB80SbI+Y8VH3E0K3vxjKNpLkbkC1gxFfRvdPbRI9HYDdtLqUnjH/SbjIOnXXhYb8hSoipHNPi26gtrtlOrAYtguqlpBvupZkW88PYiddxkWIJ1jY=
    - #8:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: EaVhqhVJUnWtxLKH
          - toolName: set-flavors
          - input:
            - Rationale: With the Manhattan Project complete and Bregenz's Nuclear Facility active, we need to boost production and mobilization to quickly manufacture our nuclear deterrent and complete required garrisons. Additionally, we are boosting Great People generation to accelerate the Great Engineer quest for our ally Assur, which will solidify our Diplomatic Victory path.
            - Flavors:
              - Mobilization: 70
              - Production: 85
              - GreatPeople: 75
            - GrandStrategy: UnitedNations
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18du7YS2IPECx5gFC6D7C1tb/xgOMSyvyVEGXGgsdkENVNAW7CWy2jd3f8pr41pY06N/4+kgXlXQtaTitCZku609hylIyEAMpiWyjkzqOXEKYuNIk9TcR8Gw0imMNpzLRVrsM/NuWxVJ1qFMky37HRSrKKgcxUmBJ6pnUOXOLAIjXU2CVnAB650Ty7ZfWQX47YiO1sFBihWS1n9W2mkN279KWw2i78fD/W/5Qen7O31Ig06Xw==
    - #9:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: EaVhqhVJUnWtxLKH
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18du7YS2IPECx5gFC6D7C1tb/xgOMSyvyVEGXGgsdkENVNAW7CWy2jd3f8pr41pY06N/4+kgXlXQtaTitCZku609hylIyEAMpiWyjkzqOXEKYuNIk9TcR8Gw0imMNpzLRVrsM/NuWxVJ1qFMky37HRSrKKgcxUmBJ6pnUOXOLAIjXU2CVnAB650Ty7ZfWQX47YiO1sFBihWS1n9W2mkN279KWw2i78fD/W/5Qen7O31Ig06Xw==