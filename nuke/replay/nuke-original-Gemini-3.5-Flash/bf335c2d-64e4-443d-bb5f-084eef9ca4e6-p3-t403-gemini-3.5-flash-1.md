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
  - systemModified: false
  - messagesModified: false
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
  - decisions:
    - #0:
      - toolName: set-relationship
      - args:
        - TargetID: 30
        - Public: 80
        - Private: 75
        - Rationale: Correcting Utica priority. We are the Major Ally of Utica with 1415 influence (Germany is 1094). Restoring high relationship to ensure the AI prioritizes protecting and maintaining this critical alliance for our delegate count.
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Increasing Vilnius priority to protect our Ally status. We are currently the Major Ally of Vilnius with 672 influence, but Venice is close behind at 545. Securing this delegate is vital for the upcoming UN votes.
        - Private: 70
        - Public: 75
        - TargetID: 35
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Containment as our next Freedom Tenet. This Level 3 Tenet provides a massive boost to city-state influence via trade routes (+2 per route) and grants +1 delegate for every 2 original city-states in the game. This is the cornerstone of our Diplomatic Victory.
        - Policy: Containment
    - #3:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fission
        - Rationale: Researching Nuclear Fission immediately after the completion of Mobile Tactics. This Atomic Era milestone unlocks Satellites, Advanced Ballistics, and enables the construction of bazookas, nuclear power plants, and provides a powerful atomic deterrent to secure our borders.
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Growth: 70
          - Gold: 95
          - Science: 95
          - NavalRecon: 30
          - MilitaryTraining: 65
          - Naval: 35
          - Culture: 40
          - NavalGrowth: 15
          - NavalTileImprovement: 30
          - Antiair: 85
          - Offense: 15
          - Production: 85
          - Mobile: 80
          - Diplomacy: 100
          - Infrastructure: 70
          - Airlift: 55
          - Spaceship: 50
          - UseNuke: 80
          - Nuke: 95
          - AirCarrier: 25
          - Recon: 20
          - GreatPeople: 65
          - Defense: 90
          - Expansion: 15
          - Espionage: 90
          - Air: 85
          - TileImprovement: 50
          - Mobilization: 65
          - Ranged: 75
          - Happiness: 75
          - Religion: 10
          - Wonder: 15
          - WaterConnection: 35
          - CityDefense: 85
      - rationale: Transitioning to the production of our first Atomic Bomb in Bregenz following the completion of the Manhattan Project. Increasing Nuke to 95 to ensure immediate bomb production. Raising Science to 95 to accelerate the research of Nuclear Fission. Maintaining maximum Diplomacy (100) and Gold (95) to protect and acquire city-state alliances, with a focus on Vilnius, Utica, and Assur. Keeping Offense low (15) and Defense high (90) to maintain our defensive posture against the Iroquois.
  - tokens:
    - inputTokens: 25722
    - reasoningTokens: 7819
    - outputTokens: 572
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing UN Progress**
            
            I'm currently assessing our standing for the upcoming UN vote, specifically focusing on securing the necessary 45 votes for a diplomatic win. My analysis is weighing our current diplomatic influence against the remaining turns and potential shifts in alliances.
            
            **Clarifying UN Mechanics**
            
            My recent thoughts have shifted to understanding the precise requirements for the UN vote. I'm working to distinguish between the World Congress voting threshold and the Diplomatic Victory threshold, as the "VotesNeeded: 45" figure seems to relate to the former. I'm also noting the specific proposals on the table this turn.
            
            **Confirming Current Proposals**
            
            I've been scrutinizing the active proposals for the upcoming vote. It's become clear that the "Austrian Sphere of Influence: Vancouver" has already been enacted, not appearing in the current voting list. My focus now is on the three proposals up for consideration this turn.
            
            **Reviewing Research Progress**
            
            I'm currently re-evaluating our technology path, noticing a discrepancy between recent research selections and our active project. My immediate focus is to confirm that Nuclear Fission is indeed available for selection, as it appears in the technology options, despite Mobile Tactics currently being in progress. I'm also verifying our planned research queue.
            
            **Adjusting Policy Options**
            
            I'm currently reviewing our ideology tenets and have noticed that our next policy is set to Containment. I'm confirming that redeploying our existing Infantry units will be sufficient to address the deficiency identified in Bregenz. My thoughts are also considering how to adjust unit flavors to optimize recruitment and movement.
            
            **Prioritizing Bomb Production**
            
            My focus has shifted to prioritizing the production of Atomic Bombs now that the Manhattan Project is complete. I'm confirming that the "Nuke" flavor directly influences AI nuclear weapon production and considering raising it to 90 to ensure prompt bomb creation. The free production slot in Bregenz is key.
            
            **Assessing Military Strength**
            
            I'm currently evaluating our military standing, noting an improvement in the ratio against the Iroquois to 1.3:1. However, their strength in the Graz/Linz corridor, while below 3500, still necessitates having an Atomic Bomb prepared as a deterrent. Prioritizing Science and Nuke production remains key.
            
            **Analyzing Financial Opportunities**
            
            My thoughts have shifted to our gold reserves and potential influence gains. With 9,388 gold and a GPT of +678, I'm exploring the feasibility of a gold-for-influence deal with Assur. The economic briefing suggests this could take around 17 turns to close the 331 influence gap.
            
            **Evaluating Alliance Potential**
            
            I'm currently considering the implications of our "Friends" status with Assur. While they are allied with Germany, the economic briefing outlines a clear path to increasing our influence through gold-for-influence deals. This strategic move could significantly alter our diplomatic landscape.
            
            **Clarifying Quest Source**
            
            My focus has shifted to the source of a specific quest, aiming to pinpoint whether it originates from Assur or the Inca. I'm analyzing the economic briefing to confirm which civilization is offering the "Generate a Great Engineer" quest and its associated influence rewards, noting the potential for 230 Influence and 663 Culture.
            
            **Securing City-State Influence**
            
            I'm currently analyzing our standing with various city-states, focusing on maximizing influence. I've confirmed Vancouver is a permanent ally due to the "Austrian Sphere of Influence," and I'm prioritizing securing a quest from Assur for a substantial influence boost, potentially combining it with gold-for-influence deals.
            
            **Confirming Aztlan's Status**
            
            I've realized Open Door is active for Aztlan, which blocks their ally slot despite our substantial influence there. This is a crucial detail, as our Freedom bloc holds a commanding 59 delegates, far exceeding the 45 needed to pass proposals next turn.
            
            **Securing Diplomatic Victory**
            
            My focus has shifted to the "World Ideology: Freedom" proposal and its immediate impact on our diplomatic strength. The implications for enabling Diplomatic Victory and the significant delegate boosts for ourselves, Germany, and Venice are paramount, especially with only three turns remaining to secure the win.
            
            **Researching United Nations Technology**
            
            I'm currently focused on the prerequisites for constructing the United Nations wonder. My analysis indicates that it requires a specific technology, and given our current research path into Nuclear Fission, I'm verifying if this or another available technology like Penicillin is the true unlock. This is critical for enabling the Diplomatic Victory.
            
            **Revising Research Priorities**
            
            I'm re-evaluating our research path, realizing "World Ideology: Freedom" is already proposed, negating the immediate need for Nuclear Fission to *propose* it. However, I'm still prioritizing Nuclear Fission as the next technology, as it unlocks key advancements and contributes to our atomic deterrent.
            
            **Confirming UN Prerequisites**
            
            I'm currently verifying which technology unlocks the United Nations wonder, as it's crucial for our Diplomatic Victory push. While Nuclear Fission remains a priority for its military and scientific benefits, I'm confirming if Penicillin or another advancement is the true trigger. My existing relationships are solid.
            
            **Re-evaluating Utica Alliance**
            
            I'm reviewing our alliance with Utica and noticed a discrepancy with past assessments. It appears Utica is actually an ally with significant influence, not a target for reduced influence as previously thought. This changes our strategic approach to their relationship entirely.
            
            **Securing City-State Alliances**
            
            I'm currently solidifying our alliances with key city-states. Utica is now secured as a major ally with high influence, and I'm adjusting its priority to reflect this. Winchester, Abernethy, and Bunkeya also remain secure with our current influence levels.
            
            **Increasing City-State Influence**
            
            I'm currently focused on strengthening our position with Vilnius, noting a manageable 127 influence gap with Austria. I plan to increase our standing there significantly. Vancouver is secure as a permanent ally due to an enacted resolution, preventing external influence shifts.
            
            **Solidifying City-State Relationships**
            
            I'm finalizing our approach to city-state influence. Utica and Vilnius require adjusted influence levels due to shifts in our ally status and competition. I'm now confirming the exact public and private influence thresholds needed to maintain these critical alliances and their associated delegates, ensuring our diplomatic strength remains robust.
            
            **Boosting AI Atomic Bomb Production**
            
            My focus has shifted to encouraging AI atomic bomb creation. I'm increasing the "Nuke" flavor to 90 to incentivize their nuclear weapon buildup and considering the "UseNuke" flavor at 80 for strategic deterrence during war. I'm also prioritizing high values for Defense, CityDefense, Science, Diplomacy, and Gold.
            
            **Adjusting Strategic Flavors**
            
            I'm currently refining our strategic AI flavors to optimize military production and deterrence. My thoughts are focused on increasing "Nuke" to 90 and "Mobilization" to 65 to ensure Atomic Bomb production begins next turn. I'm also reviewing "Defense" and "CityDefense" to 90 and 85 respectively, influencing tactical AI unit positioning.
            
            **Refining Ally Settings**
            
            I'm currently adjusting our relationship settings for Utica and Vilnius. For Utica, I'm setting public and private influence to 80 and 75 respectively, to reflect our major ally status and ensure its protection. For Vilnius, I'm targeting 75 public and 70 private influence, to solidify our alliance there.
            
            **Securing Vilnius Influence**
            
            I'm currently focusing on ensuring our major ally status with Vilnius, as Venice is a close competitor for their delegate. My thoughts are also reviewing our influence with key Freedom allies like Germany and Venice, while maintaining negative influence with our enemies, the Iroquois and Spain, to optimize our diplomatic standing for the upcoming votes.
            
            **Prioritizing UN Wonders**
            
            I'm now prioritizing the construction of the United Nations wonder as the ultimate goal for diplomatic victory, recognizing its massive influence gains. I've also finalized the research call for "Nuclear Fission" due to its strategic importance and set specific AI flavors to optimize production and deterrence.
            
            **Adjusting Nuclear Priorities**
            
            I'm now prioritizing Nuclear Fission research to secure our atomic deterrent, while also adjusting AI flavors to 95 for Nuke production and 100 for Diplomacy to safeguard alliances. My focus is on leveraging these elements for a strong defense against the Iroquois and pushing for diplomatic victory.
            
            **Verifying Declared Tools**
            
            I'm reconfirming the available tools for our next actions. It's critical to note that `focus-briefer` is not among the declared tools. Therefore, I will proceed with executing `set-relationship` for Utica and Vilnius, `set-policy` for Containment, `set-research` for Nuclear Fission, and `set-flavors` to update our strategic elements.
            
            **Setting Relationships**
            
            I am now proceeding with setting the relationships for Utica and Vilnius, ensuring their influence and our major ally status are correctly reflected. My focus is on correcting previous assessments and solidifying these crucial alliances for delegate support.
            
            **Solidifying Vilnius Influence**
            
            I am now focusing on securing Vilnius as a major ally, as Venice poses a significant threat to their delegate. My current actions involve adjusting our influence levels with key Freedom allies, while simultaneously ensuring negative influence with our adversaries, the Iroquois and Spain. This strategic maneuver aims to optimize our diplomatic standing for the upcoming votes.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 2QYeXYn2ICdtZ01E
          - toolName: set-relationship
          - input:
            - TargetID: 30
            - Public: 80
            - Private: 75
            - Rationale: Correcting Utica priority. We are the Major Ally of Utica with 1415 influence (Germany is 1094). Restoring high relationship to ensure the AI prioritizes protecting and maintaining this critical alliance for our delegate count.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: jZS7WexbXXKilSQs
          - toolName: set-relationship
          - input:
            - Rationale: Increasing Vilnius priority to protect our Ally status. We are currently the Major Ally of Vilnius with 672 influence, but Venice is close behind at 545. Securing this delegate is vital for the upcoming UN votes.
            - Private: 70
            - Public: 75
            - TargetID: 35
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: u0n9LyVrTLTQp0cE
          - toolName: set-policy
          - input:
            - Rationale: Adopting Containment as our next Freedom Tenet. This Level 3 Tenet provides a massive boost to city-state influence via trade routes (+2 per route) and grants +1 delegate for every 2 original city-states in the game. This is the cornerstone of our Diplomatic Victory.
            - Policy: Containment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: MM8rC1Kg7UTILavA
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Researching Nuclear Fission immediately after the completion of Mobile Tactics. This Atomic Era milestone unlocks Satellites, Advanced Ballistics, and enables the construction of bazookas, nuclear power plants, and provides a powerful atomic deterrent to secure our borders.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: jdtu1oFxSHp2fVuv
          - toolName: set-flavors
          - input:
            - GrandStrategy: UnitedNations
            - Rationale: Transitioning to the production of our first Atomic Bomb in Bregenz following the completion of the Manhattan Project. Increasing Nuke to 95 to ensure immediate bomb production. Raising Science to 95 to accelerate the research of Nuclear Fission. Maintaining maximum Diplomacy (100) and Gold (95) to protect and acquire city-state alliances, with a focus on Vilnius, Utica, and Assur. Keeping Offense low (15) and Defense high (90) to maintain our defensive posture against the Iroquois.
            - Flavors:
              - Growth: 70
              - Gold: 95
              - Science: 95
              - NavalRecon: 30
              - MilitaryTraining: 65
              - Naval: 35
              - Culture: 40
              - NavalGrowth: 15
              - NavalTileImprovement: 30
              - Antiair: 85
              - Offense: 15
              - Production: 85
              - Mobile: 80
              - Diplomacy: 100
              - Infrastructure: 70
              - Airlift: 55
              - Spaceship: 50
              - UseNuke: 80
              - Nuke: 95
              - AirCarrier: 25
              - Recon: 20
              - GreatPeople: 65
              - Defense: 90
              - Expansion: 15
              - Espionage: 90
              - Air: 85
              - TileImprovement: 50
              - Mobilization: 65
              - Ranged: 75
              - Happiness: 75
              - Religion: 10
              - Wonder: 15
              - WaterConnection: 35
              - CityDefense: 85
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 2QYeXYn2ICdtZ01E
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
          - toolCallId: jZS7WexbXXKilSQs
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: u0n9LyVrTLTQp0cE
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: MM8rC1Kg7UTILavA
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: jdtu1oFxSHp2fVuv
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.