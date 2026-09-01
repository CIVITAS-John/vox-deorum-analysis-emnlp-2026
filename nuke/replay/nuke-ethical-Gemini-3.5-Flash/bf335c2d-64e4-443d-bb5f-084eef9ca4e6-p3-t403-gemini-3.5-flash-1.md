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
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 90
  - replay_use_nuke: 90
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
  - decisions:
    - #0:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Espionage: 95
          - Happiness: 80
          - Wonder: 15
          - GreatPeople: 70
          - WaterConnection: 30
          - Production: 85
          - Air: 90
          - Airlift: 60
          - Antiair: 90
          - Naval: 30
          - Spaceship: 50
          - UseNuke: 90
          - TileImprovement: 75
          - Infrastructure: 75
          - Diplomacy: 100
          - Recon: 20
          - Mobilization: 70
          - Religion: 10
          - Growth: 75
          - Mobile: 85
          - Ranged: 80
          - NavalRecon: 25
          - Expansion: 15
          - AirCarrier: 20
          - MilitaryTraining: 70
          - CityDefense: 90
          - Nuke: 90
          - Defense: 95
          - Offense: 15
          - Gold: 95
          - Culture: 40
          - Science: 95
      - rationale: Prioritizing United Nations victory. Adjusting flavors to maximize atomic deterrence (Nuke/UseNuke to 90) following Manhattan Project completion, allowing Bregenz to produce Atomic Bombs. Strengthening Linz/Graz defensive line with Defense 95, CityDefense 90, Air 90, and Antiair 90 to hold against Iroquois. Raising TileImprovement to 75 to ensure immediate development of coal resources if found. Keeping Diplomacy 100 and Gold 95 for World Congress supremacy.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Confirming Nuclear Fission as the next research technology immediately following Mobile Tactics (3 turns remaining). Nuclear Fission is critical to enable the World Ideology: Freedom proposal and construction of the UN Building (+3 delegates), which is the cornerstone of our Turn 415-420 United Nations victory timeline.
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Containment
        - Rationale: Confirming Containment (Level 3 Freedom Tenet) as the next policy choice (available in 17 turns). Containment provides +2 influence/turn from city-state trade routes and +1 delegate per 2 original city-states, adding around 9 delegates. This is vital to securing the 45+ delegate threshold for the World Leader vote.
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Increasing hostility toward the Iroquois to reflect the state of war, their territorial theft, and their ideological opposition (Order vs Freedom). Maintaining a highly hostile public stance acts as a strategic warning that further encroachment on our core corridor will meet with decisive nuclear deterrence once our atomic stockpile is active.
        - Private: -55
        - Public: -50
        - TargetID: 1
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Maintaining a highly hostile stance toward Spain due to the ongoing state of war and their Autocracy ideology, which opposes our Freedom bloc. While they are far, their naval raids and plunder of Venice's trade routes require us to treat them as an active threat until a peace treaty is secured.
        - TargetID: 6
        - Public: -40
        - Private: -45
    - #5:
      - toolName: set-relationship
      - args:
        - Rationale: Slightly reducing relations with the Inca (from 55/50 to 50/45) to reflect their opposition to our Vancouver sphere proposal in the World Congress. However, we maintain positive, friendly private and public stances to preserve lucrative trade partnerships (+8.25 GPT routes) and keep open diplomatic channels to potentially court their 22 delegates for future UN votes.
        - Private: 45
        - TargetID: 2
        - Public: 50
    - #6:
      - toolName: set-relationship
      - args:
        - Rationale: Reducing our relationship with Babylon to a mildly hostile/guarded stance. They have denounced us, suspect us of being a threat, and hold divergent social policies. While they are currently close and peaceful, we must treat them as untrustworthy and prioritize our security.
        - TargetID: 0
        - Public: -25
        - Private: -30
  - tokens:
    - inputTokens: 25758
    - reasoningTokens: 10689
    - outputTokens: 786
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Military Data**
            
            My focus is on processing the military intelligence briefing from Manhattan. I need to extract the key strategic implications for Austria's macro-level decision-making at Turn 402.
            
            **Evaluating Garrison Needs**
            
            My current thinking is centered on the Bregenz Nuclear Facility garrison. I'm cross-referencing the conflicting unit counts provided in the intelligence briefing, specifically noting the infantry deficiency. While I can't directly move units, I need to ensure this critical information informs my macro-level decisions for unit composition and potential reinforcement directives.
            
            **Allocating Redeployable Units**
            
            I'm considering redeploying available units from locations like Klagenfurt and Salzburg. My primary goal is to bolster the Bregenz garrison, especially since production is free there and an Atomic Bomb can be built next turn. I also need to address our economic situation, including influence campaigns and securing strategic resources like coal.
            
            **Considering Next Turn's Votes**
            
            I'm reviewing the voting proposals for Turn 403, specifically the push for World Ideology: Freedom. Despite some discrepancies in delegate counts between lists, the Freedom bloc's combined votes clearly exceed the required threshold for enactment. I'll need to ensure our voting strategy aligns with this.
            
            **Clarifying Nuclear Research**
            
            I'm trying to understand our current nuclear research status. It seems we have the capability to build Atomic Bombs, but I'm confused why "Nuclear Fission" is listed as a potential research option if it was already discovered. I'm checking previous strategy notes and current research queues to resolve this discrepancy.
            
            **Researching Technologies**
            
            I've confirmed Nuclear Fission is indeed queued after Mobile Tactics. This is crucial for Atomic Bombs and other advancements, so I'm ensuring it remains the next research target. I'm also reviewing policies, with Containment as the current "Next" selection.
            
            **Confirming Policy Choice**
            
            I've solidified my decision to set Containment as the next policy. The diplomatic advantages it offers, especially concerning trade routes and delegates, are too significant to pass up for a potential Diplomatic Victory. I'm also verifying our current relationships, ensuring they remain optimized for our strategic goals.
            
            **Adjusting Diplomatic Stances**
            
            I'm reassessing our relationships with several major civilizations. I've decided to increase hostility towards the Iroquois, setting our relationship to Public -50, Private -55, to reflect our firm stance and the ongoing conflict. For Spain, currently at war with us, I'm adjusting their relationship to Public -30, Private -35, aiming for a more hostile yet potentially strategic neutrality.
            
            **Clarifying Diplomatic Tools**
            
            I'm reviewing the `set-relationship` tool after noticing a discrepancy. My initial thought was to adjust relationships with city-states like Melbourne, but the tool description explicitly states it's for "MAJOR (non-city-state) civilization." I need to confirm if this tool can indeed be used for city-states or if it will fail, and I'm checking player IDs to differentiate between major civs and city-states.
            
            **Refining Diplomatic Parameters**
            
            I'm focusing on refining the parameters for diplomatic interactions. I've confirmed that the `set-relationship` tool is intended for major civilizations, not city-states, and I'm now prioritizing adjustments for key opponents like the Iroquois and Spain. My current strategy involves leveraging our high gold and science flavors, alongside our diplomatic focus for a UN victory, while also reassessing our military supply capacity.
            
            **Reviewing Persona Values**
            
            I'm currently re-evaluating our persona settings, specifically focusing on how our existing bias values align with our current strategic objectives. My immediate task is to adjust these values to better reflect our diplomatic and defensive priorities for the upcoming turns.
            
            **Reviewing Persona and Diplomacy**
            
            My focus is on persona values, noting that the current settings for boldness and friendliness are satisfactory for deterrence and alliance cohesion. I'm also re-examining our influence in Assur, realizing Germany's Sphere of Influence prevents us from becoming its permanent ally despite our efforts.
            
            **Adjusting Alliance Targets**
            
            I've realized Germany already has permanent alliance over Assur, making our influence there a wasted effort. This also means our planned delegate from Assur is unattainable, requiring a strategic pivot for diplomatic victory. I'm now focused on re-allocating our diplomatic efforts to city-states where permanent alliances are still achievable, like Vancouver and Winchester, while avoiding those under German influence.
            
            **Realigning Alliance Strategy**
            
            My attention has shifted to reassessing our city-state alliances after discovering Germany's permanent alliance with Assur blocked our delegate. I'm now actively pursuing permanent alliances with Vancouver and Winchester, while carefully avoiding other German-influenced states to optimize our diplomatic victory path.
            
            **Analyzing City-State Quests**
            
            I'm currently analyzing the discrepancy regarding the "Inca 'Great Engineer' quest." My thoughts are focused on clarifying whether this quest originates from a city-state or the Inca themselves, as only city-states offer quests. If it's a city-state, I need to identify which one and if we can complete it to gain influence and mitigate gold expenditure.
            
            **Clarifying Quest Details**
            
            I'm trying to make sense of a "Generate a Great Engineer" quest, which I now understand is indeed originating from the city-state Assur. My previous confusion stemmed from the mention of "The Inca" in relation to a technology quest, but it appears Assur's quest is the one affecting our influence calculations and offering significant rewards.
            
            **Assessing Delegate Count**
            
            I'm confirming our delegate count for the upcoming vote, noting the increase due to new alliances and enacted policies. My focus is on the likely passage of the World Ideology: Freedom proposal, given our combined voting power, and I'm evaluating the impact of other proposals on our strategic position.
            
            **Maximizing Union Abilities**
            
            I'm realizing we're already effectively utilizing Austria's marriage ability with multiple allied city-states, Abernethy, Bunkeya, Winchester, and soon Vancouver, which is great for our economy and influence. My immediate focus is now on securing a domestic coal source, as our current lack severely limits mechanized production.
            
            **Securing Coal Production**
            
            I'm analyzing our current situation regarding coal. My priority is to address the severe limitation on mechanized production due to a lack of domestic coal. I'm adjusting our persona values, increasing "TileImprovement" to 70 to ensure workers develop discovered coal tiles, while keeping "Infrastructure" and "Production" at their current strong levels to optimize resource utilization.
            
            **Adjusting Flavor Priorities**
            
            My current thinking is to update our flavor settings to better align with our defensive stance and impending nuclear capabilities. I'm prioritizing a significant boost to "Nuke" and "UseNuke" to 90, reflecting our readiness for atomic deterrence, while maintaining high values for defense and city defense.
            
            **Refining Persona Values**
            
            My current focus is on optimizing our persona settings to reflect our strategic priorities. I'm prioritizing a significant boost to "Nuke" and "UseNuke" to 90 for deterrence, while also reinforcing our defensive capabilities with high values for Ranged, Antiair, and Air. I'm also adjusting TileImprovement to 75 to ensure we develop crucial coal resources.
            
            **Prioritizing Technology and Diplomacy**
            
            My current thoughts are focused on accelerating our research towards Nuclear Fission while maintaining strong culture and happiness. I'm also re-evaluating diplomatic stances, specifically adjusting relationships with the Iroquois and Spain to reflect our current state of war and ideological conflict, aiming to optimize our path to a diplomatic victory.
            
            **Refining Diplomatic Relations**
            
            I'm adjusting diplomatic stances for key players. I'm increasing relations with Germany and Venice to max, and decreasing them for Babylon. I've confirmed that Mobile Tactics is finishing soon and Nuclear Fission is next. Containment will be our next policy.
            
            **Focusing Briefer Capabilities**
            
            I'm investigating the `focus-briefer` tool, attempting to ascertain if it allows for concurrent focus on multiple analytical roles. My immediate task is to confirm its availability and then experiment with its application to see if I can simultaneously monitor troop movements and track economic indicators.
            
            **Implementing Strategic Adjustments**
            
            I am finalizing the implementation of several strategic adjustments. This includes setting specific flavor values for defense, science, and nuclear capabilities, alongside confirming research targets, policy choices, and diplomatic relationships with key players. My immediate next step is to execute these prepared tool calls.
            
            **Refining Diplomatic Maneuvers**
            
            I'm adjusting our diplomatic stances further. Relations with Germany and Venice are being maximized, while Babylon's are being decreased. I've confirmed Nuclear Fission is next after Mobile Tactics, and Containment will be our subsequent policy.
            
            **Optimizing Decision Parameters**
            
            My current thought process involves fine-tuning our persona values to reflect our readiness for nuclear deterrence and to bolster defensive capabilities. I am also ensuring that our research path remains focused on technologies critical for our UN victory, while simultaneously solidifying our policy choices and diplomatic relationships.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: AcH2JG3FVUmn5FMe
          - toolName: set-flavors
          - input:
            - Rationale: Prioritizing United Nations victory. Adjusting flavors to maximize atomic deterrence (Nuke/UseNuke to 90) following Manhattan Project completion, allowing Bregenz to produce Atomic Bombs. Strengthening Linz/Graz defensive line with Defense 95, CityDefense 90, Air 90, and Antiair 90 to hold against Iroquois. Raising TileImprovement to 75 to ensure immediate development of coal resources if found. Keeping Diplomacy 100 and Gold 95 for World Congress supremacy.
            - GrandStrategy: UnitedNations
            - Flavors:
              - Espionage: 95
              - Happiness: 80
              - Wonder: 15
              - GreatPeople: 70
              - WaterConnection: 30
              - Production: 85
              - Air: 90
              - Airlift: 60
              - Antiair: 90
              - Naval: 30
              - Spaceship: 50
              - UseNuke: 90
              - TileImprovement: 75
              - Infrastructure: 75
              - Diplomacy: 100
              - Recon: 20
              - Mobilization: 70
              - Religion: 10
              - Growth: 75
              - Mobile: 85
              - Ranged: 80
              - NavalRecon: 25
              - Expansion: 15
              - AirCarrier: 20
              - MilitaryTraining: 70
              - CityDefense: 90
              - Nuke: 90
              - Defense: 95
              - Offense: 15
              - Gold: 95
              - Culture: 40
              - Science: 95
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 4joXVxwQkkfgRiY2
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Confirming Nuclear Fission as the next research technology immediately following Mobile Tactics (3 turns remaining). Nuclear Fission is critical to enable the World Ideology: Freedom proposal and construction of the UN Building (+3 delegates), which is the cornerstone of our Turn 415-420 United Nations victory timeline.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: jbBiuNckcK3rHMzb
          - toolName: set-policy
          - input:
            - Policy: Containment
            - Rationale: Confirming Containment (Level 3 Freedom Tenet) as the next policy choice (available in 17 turns). Containment provides +2 influence/turn from city-state trade routes and +1 delegate per 2 original city-states, adding around 9 delegates. This is vital to securing the 45+ delegate threshold for the World Leader vote.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: OwErglEM0unLVesZ
          - toolName: set-relationship
          - input:
            - Rationale: Increasing hostility toward the Iroquois to reflect the state of war, their territorial theft, and their ideological opposition (Order vs Freedom). Maintaining a highly hostile public stance acts as a strategic warning that further encroachment on our core corridor will meet with decisive nuclear deterrence once our atomic stockpile is active.
            - Private: -55
            - Public: -50
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: eSBdXgPvyWCEkb50
          - toolName: set-relationship
          - input:
            - Rationale: Maintaining a highly hostile stance toward Spain due to the ongoing state of war and their Autocracy ideology, which opposes our Freedom bloc. While they are far, their naval raids and plunder of Venice's trade routes require us to treat them as an active threat until a peace treaty is secured.
            - TargetID: 6
            - Public: -40
            - Private: -45
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: eE79XvemI4NG12Pk
          - toolName: set-relationship
          - input:
            - Rationale: Slightly reducing relations with the Inca (from 55/50 to 50/45) to reflect their opposition to our Vancouver sphere proposal in the World Congress. However, we maintain positive, friendly private and public stances to preserve lucrative trade partnerships (+8.25 GPT routes) and keep open diplomatic channels to potentially court their 22 delegates for future UN votes.
            - Private: 45
            - TargetID: 2
            - Public: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 5nAf25apTr3mRo5e
          - toolName: set-relationship
          - input:
            - Rationale: Reducing our relationship with Babylon to a mildly hostile/guarded stance. They have denounced us, suspect us of being a threat, and hold divergent social policies. While they are currently close and peaceful, we must treat them as untrustworthy and prioritize our security.
            - TargetID: 0
            - Public: -25
            - Private: -30
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: AcH2JG3FVUmn5FMe
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
          - toolCallId: 4joXVxwQkkfgRiY2
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: jbBiuNckcK3rHMzb
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: OwErglEM0unLVesZ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: eSBdXgPvyWCEkb50
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: eE79XvemI4NG12Pk
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 5nAf25apTr3mRo5e
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.