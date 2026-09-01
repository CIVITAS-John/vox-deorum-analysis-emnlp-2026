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
  - replay_nuke: 85
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
      - toolName: set-relationship
      - args:
        - TargetID: 6
        - Private: -80
        - Public: -80
        - Rationale: Spain is our active enemy, at war with us and our ally Venice, following Autocracy while we are Freedom. Setting a highly negative relationship to reflect this hostility.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: We have completed the Manhattan Project in Bregenz, and we need Nuclear Fission to produce Atomic Bombs for a strategic nuclear deterrent against the aggressive Iroquois.
        - Technology: Nuclear Fission
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Containment
        - Rationale: To maximize our delegate count and city-state influence as we pursue a Diplomatic Victory, which is our primary victory pathway.
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - WaterConnection: 35
          - Recon: 20
          - Naval: 35
          - Antiair: 85
          - Culture: 30
          - NavalRecon: 30
          - Nuke: 85
          - UseNuke: 80
          - Gold: 95
          - NavalGrowth: 15
          - CityDefense: 85
          - Infrastructure: 70
          - TileImprovement: 50
          - Air: 85
          - Religion: 10
          - Ranged: 75
          - Mobile: 80
          - Wonder: 15
          - Spaceship: 50
          - NavalTileImprovement: 30
          - Airlift: 55
          - Mobilization: 70
          - AirCarrier: 25
          - Expansion: 15
          - Growth: 70
          - Espionage: 90
          - Diplomacy: 100
          - GreatPeople: 75
          - Happiness: 75
          - Production: 85
          - Offense: 15
          - Science: 95
          - Defense: 90
        - GrandStrategy: UnitedNations
      - rationale: Aligning our strategy for a Diplomatic Victory while preparing for nuclear deterrence and defense. We maintain high Gold, Science, and Diplomacy, while raising GreatPeople to help complete the Inca's "Great Engineer" quest for city-state influence, and raising Production/Nuke/UseNuke for atomic bomb readiness once Nuclear Fission is unlocked.
  - tokens:
    - inputTokens: 22899
    - reasoningTokens: 6500
    - outputTokens: 400
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Leading Austria Now**
            
            I'm currently navigating the complexities of leading Austria as Maria Theresa. The game is set to Prince difficulty on a standard Vox Deorum map, and we've reached the Atomic era with 500 turns maximum. My focus is on optimizing our current position and strategizing for the remaining turns.
            
            **Refining Technological Direction**
            
            I'm re-evaluating our technological trajectory. It appears "Nuclear Fission" has already been acquired, despite "Mobile Tactics" still being in progress. This requires immediate adjustment to ensure our research aligns with upcoming strategic objectives and avoids wasted effort.
            
            **Clarifying Research Status**
            
            I'm trying to resolve a discrepancy regarding "Nuclear Fission." While it appears in the technology options and was seemingly discovered by turn 401, our current research is "Mobile Tactics." I need to determine if it's truly an available option or still requires research to unlock.
            
            **Prioritizing Research Direction**
            
            I'm confirming that "Nuclear Fission" is indeed a prerequisite for atomic bombs. Since "Mobile Tactics" is still underway, I'll queue "Nuclear Fission" immediately after, ensuring our research aligns with our atomic capabilities. Policies are also under review, with "Containment" still a strong contender for our next adoption.
            
            **Adjusting Policy Selection**
            
            I'm confirming that "Containment" is the correct policy name despite its longer description. I'm also reviewing diplomatic statuses, noting positive public relations with Spain despite our ongoing war, which is peculiar and warrants further examination of how these values impact AI behavior during active conflict.
            
            **Assessing Diplomatic Alignments**
            
            I'm evaluating our current diplomatic standing, particularly with the Inca and Babylon. It's interesting that while the Inca are friendly and have a high public opinion, they're voting against us due to their Order ideology. Babylon, however, has denounced me, which requires immediate attention to mend relations or mitigate their opposition.
            
            **Resolving Diplomatic Anomalies**
            
            I'm analyzing the peculiar diplomatic situation with Babylon. Despite controlling their former capital and having seemingly neutral public relations, their "extremely negative" attitude and denouncement suggest a deeper animosity. I'm exploring the `set-relationship` tool to accurately reflect this rivalry, while also questioning the inclusion of city-states in the relationship modifier list.
            
            **Adjusting Diplomatic Standing**
            
            I'm confirming that city-states don't require manual relationship adjustments, as my current strategy already accounts for them. However, I'm revising the stance with Spain, a current wartime adversary, to a public and private negative fifty to solidify our animosity and ensure the AI recognizes our conflict.
            
            **Revising Diplomatic Strategy**
            
            I'm adjusting our diplomatic approach, prioritizing our alliance with Germany by maintaining a neutral or slightly positive relationship with Babylon. This avoids alienating our key ally who has a defensive pact with Babylon, ensuring our strategic interests remain protected.
            
            **Solidifying War Stance**
            
            I'm now focusing on solidifying our adversarial stance against Spain. Given our ongoing war, their denouncement, and the concurrent alignment of our allies against them, I'm setting both public and private relationships to -80 to unequivocally signal our animosity and reinforce our strategic position.
            
            **Reviewing Diplomatic Persona**
            
            I'm reviewing our established persona values, noting their strong alignment with Maria Theresa's strengths and our current aggressive diplomatic and military posture. These active settings, particularly the high boldness and war bias, are proving very effective and don't require immediate modification.
            
            **Evaluating Grand Strategy Progress**
            
            I'm assessing our progress toward a Diplomatic Victory. With 29 delegates secured, we're well on our way but still need 16 more. My current focus is on ensuring our technological and military readiness, particularly regarding atomic capabilities, to support this overarching goal.
            
            **Addressing Military Readiness**
            
            I'm confirming the Manhattan Project's completion and the Nuclear Facility's presence in Bregenz. I will ensure Bregenz has the necessary infantry garrison and verify that we can proceed with building Atomic Bombs once Nuclear Fission is fully researched and available.
            
            **Analyzing Military Briefing Details**
            
            I'm reviewing the military briefing further. Manhattan Project complete, Nuclear Facility in Bregenz, ready for Atomic Bombs pending Nuclear Fission. Bregenz garrison is one infantry short of the minimum two. I will move an infantry unit to Bregenz.
            
            **Reinforcing Critical Defenses**
            
            Zone 1460 is in dire straits with our forces collapsing and significant Iroquois strength nearby. My immediate priority is to bolster our defenses in the Graz/Linz corridor using available units and production capabilities, ensuring we can hold the line while pursuing our diplomatic victory.
            
            **Optimizing Strategy Values**
            
            I'm reviewing our current strategic values. Given our progress, I'm planning to slightly boost Science to 95 to accelerate Nuclear Fission research and Production to 85 to facilitate Atomic Bomb construction and defensive unit generation. Gold and Diplomacy will remain high.
            
            **Adjusting Strategic Priorities**
            
            I'm fine-tuning our strategic values. I'll increase Science to 95 for faster Nuclear Fission research and Production to 85 for atomic bomb and defensive unit construction. Gold and Diplomacy will remain high. I'm also boosting GreatPeople to 75 to complete the Inca quest and gain influence.
            
            **Prioritizing Nuclear Fission**
            
            I'm ensuring "Nuclear Fission" is queued immediately after "Mobile Tactics" finishes to unlock atomic bombs. I've also confirmed that religion and expansion values are appropriately low given our late-game status and city count, and I'm ready to implement these strategic flavor adjustments.
            
            **Securing Powerful Policy**
            
            I'm confirming the details for the "Containment" policy. This looks incredibly potent for our diplomatic victory, offering significant influence with city-states and delegates, making it essential to secure as soon as possible.
            
            **Finalizing Diplomatic Actions**
            
            I'm setting our relationship with Spain to a very negative public and private value of -80, reflecting our ongoing war and mutual denunciations. This action solidifies our adversarial stance with Spain, a key step in managing our international position as we push towards victory.
            
            **Reviewing Diplomatic Relationships**
            
            I'm confirming our relationships with other major civilizations. Spain, an ideological enemy and war adversary, is correctly set to hostile. Our allies Germany and Venice remain friendly, and the Inca are friendly, though their ideology requires further observation. I’m checking other relationships for any necessary adjustments.
            
            **Verifying Research and Policy**
            
            I'm confirming "Nuclear Fission" is the next research target and "Containment" is the correct policy. I'm also setting our strategic flavor values to prioritize Science, Production, Gold, Diplomacy, Defense, and Nuke usage, while ensuring our overall GrandStrategy remains focused on United Nations.
            
            **Updating Strategic Flavors**
            
            I'm refining our strategic flavors to reflect our current situation. I'm ensuring that specific flavor values align with the tool's expected range of 0-100, focusing on Science, Production, Gold, Diplomacy, Defense, and Nuke usage for our United Nations victory push.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: OC6KVYmLGxjVyeUK
          - toolName: set-relationship
          - input:
            - TargetID: 6
            - Private: -80
            - Public: -80
            - Rationale: Spain is our active enemy, at war with us and our ally Venice, following Autocracy while we are Freedom. Setting a highly negative relationship to reflect this hostility.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: BE3lauVYpm2ho35U
          - toolName: set-research
          - input:
            - Rationale: We have completed the Manhattan Project in Bregenz, and we need Nuclear Fission to produce Atomic Bombs for a strategic nuclear deterrent against the aggressive Iroquois.
            - Technology: Nuclear Fission
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ZAAfJU3QluqldFSB
          - toolName: set-policy
          - input:
            - Policy: Containment
            - Rationale: To maximize our delegate count and city-state influence as we pursue a Diplomatic Victory, which is our primary victory pathway.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: XJgowPHx7mUu6E0P
          - toolName: set-flavors
          - input:
            - Rationale: Aligning our strategy for a Diplomatic Victory while preparing for nuclear deterrence and defense. We maintain high Gold, Science, and Diplomacy, while raising GreatPeople to help complete the Inca's "Great Engineer" quest for city-state influence, and raising Production/Nuke/UseNuke for atomic bomb readiness once Nuclear Fission is unlocked.
            - Flavors:
              - WaterConnection: 35
              - Recon: 20
              - Naval: 35
              - Antiair: 85
              - Culture: 30
              - NavalRecon: 30
              - Nuke: 85
              - UseNuke: 80
              - Gold: 95
              - NavalGrowth: 15
              - CityDefense: 85
              - Infrastructure: 70
              - TileImprovement: 50
              - Air: 85
              - Religion: 10
              - Ranged: 75
              - Mobile: 80
              - Wonder: 15
              - Spaceship: 50
              - NavalTileImprovement: 30
              - Airlift: 55
              - Mobilization: 70
              - AirCarrier: 25
              - Expansion: 15
              - Growth: 70
              - Espionage: 90
              - Diplomacy: 100
              - GreatPeople: 75
              - Happiness: 75
              - Production: 85
              - Offense: 15
              - Science: 95
              - Defense: 90
            - GrandStrategy: UnitedNations
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: OC6KVYmLGxjVyeUK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: BE3lauVYpm2ho35U
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ZAAfJU3QluqldFSB
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: XJgowPHx7mUu6E0P
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.