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
      - toolName: set-research
      - args:
        - Rationale: Confirming Nuclear Fission as the next research target to unlock Bazookas, Nuclear Plants, and the ability to build Atomic Bombs at our Bregenz facility. This is the critical path to establish a credible deterrent against Iroquois aggression.
        - Technology: Nuclear Fission
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Maintaining Containment as our next policy. This Level 3 Freedom tenet will provide immense influence from city-state trade routes and ~9 extra delegates, sealing our diplomatic victory.
        - Policy: Containment
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 30
        - Private: 55
        - Rationale: Correcting Utica relationship back to 60/55. We currently hold Ally status at 1415 influence (Germany is at 1094). We must maintain this alliance to secure our delegate count rather than conceding it.
        - Public: 60
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Increasing Vancouver to 60/55. With our Sphere of Influence proposal set to pass on Turn 403, Vancouver will become our permanent ally. Maintaining a strong relationship ensures the AI leverages this permanent connection.
        - Public: 60
        - TargetID: 22
        - Private: 55
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Happiness: 75
          - Culture: 30
          - AirCarrier: 25
          - GreatPeople: 65
          - Infrastructure: 70
          - Naval: 35
          - WaterConnection: 35
          - Science: 90
          - TileImprovement: 70
          - Defense: 90
          - Airlift: 55
          - NavalTileImprovement: 30
          - Wonder: 15
          - NavalRecon: 30
          - Growth: 70
          - Antiair: 85
          - Mobile: 80
          - Ranged: 75
          - NavalGrowth: 15
          - Diplomacy: 100
          - Espionage: 90
          - Nuke: 80
          - Mobilization: 65
          - CityDefense: 85
          - Religion: 10
          - Production: 80
          - Air: 85
          - UseNuke: 80
          - Spaceship: 50
          - Offense: 15
          - Recon: 20
          - MilitaryTraining: 65
          - Gold: 95
          - Expansion: 15
        - GrandStrategy: UnitedNations
      - rationale: Raising TileImprovement from 50 to 70 to ensure our workers aggressively prioritize strategic resource tile improvements, specifically searching for and connecting Coal to enable mechanized production. Maintaining high Defense (90), Diplomacy (100), Gold (95), and Science (90) for our UnitedNations Grand Strategy.
    - #5:
      - toolName: set-persona
      - args:
        - MinorCivNeutralBias: 1
        - MinorCivCompetitiveness: 10
        - WonderCompetitiveness: 10
        - MinorCivHostileBias: 1
        - AfraidBias: 3
        - HostileBias: 1
        - Friendliness: 9
        - Forgiveness: 7
        - Neediness: 4
        - NeutralBias: 8
        - WorkWithWillingness: 10
        - MinorCivWarBias: 3
        - Boldness: 10
        - WarBias: 10
        - GuardedBias: 6
        - WorkAgainstWillingness: 8
        - MinorCivFriendlyBias: 8
        - VictoryCompetitiveness: 6
        - Chattiness: 8
        - Meanness: 6
        - WarmongerHate: 8
        - DeceptiveBias: 8
        - DiplomaticBalance: 9
        - FriendlyBias: 10
        - Rationale: Maintaining our highly customized persona: high Boldness (10) and WarBias (10) to support a strong nuclear deterrent posture against the Iroquois, combined with maximum FriendlyBias (10) and DiplomaticBalance (9) to preserve the cohesion of our vital Freedom voting bloc (Austria, Germany, Venice).
        - Loyalty: 5
        - DenounceWillingness: 9
  - tokens:
    - inputTokens: 25758
    - reasoningTokens: 5002
    - outputTokens: 742
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Deciding Austria's Next Steps**
            
            I'm currently focused on formulating initial strategic directives for Maria Theresa's empire in Turn 402. My immediate goal is to outline a set of high-level decisions for Austria, considering the current game state and difficulty settings.
            
            **Refining Austrian Direction**
            
            My current focus is on assessing the strategic options for Austria, specifically deciding whether to adjust our persona, relationships, research, policies, or flavor values. I'm evaluating the implications of these choices given our strong treasury and current geopolitical landscape, especially our ongoing conflict with the Iroquois and proximity to the technologically advanced Inca.
            
            **Analyzing World Congress Proposals**
            
            I'm currently reviewing the upcoming World Congress vote, specifically the "World Ideology: Freedom" proposal. I need to confirm the eligibility criteria and our actual status in relation to discovering Nuclear Fission, as there seems to be a slight discrepancy. My priority is to ensure we can successfully pass this proposal.
            
            **Preparing for World Congress**
            
            I'm currently confirming delegate counts for the upcoming World Congress, specifically addressing discrepancies for Venice to ensure the "World Ideology: Freedom" proposal passes. My focus is on solidifying our strategy for this vote, considering the potential for immediate atomic weapon production and our current military posture.
            
            **Securing World Congress Victory**
            
            I'm currently assessing our economic resources to solidify our World Congress strategy. With a substantial gold reserve, I'm exploring options to quickly gain influence with Assur, potentially accelerating our path to victory by securing the "World Ideology: Freedom" proposal and preparing for immediate atomic weapon production.
            
            **Securing Coal Resources**
            
            I'm prioritizing coal acquisition due to its scarcity and the ongoing conflict with Spain, which complicates trade. My focus is on maximizing production and tile improvements to secure this critical resource. I'll also be monitoring World Congress votes, particularly the "World Ideology: Freedom" proposal, and ensuring we maintain diplomatic ties despite opposition.
            
            **Finalizing Nuclear Research**
            
            I've confirmed Nuclear Fission is critical for atomic bombs, so I'm prioritizing its research and will set it as the next technology. I'll also be setting the Containment policy to synergize with our diplomatic victory and carefully adjusting relationships with major powers like the Inca to maintain peace and trade, while keeping our enemies hostile.
            
            **Adjusting Diplomatic Levers**
            
            I'm reassessing our alliances, particularly with Utica, where our AI seems to have surprisingly retained major ally status. I'm increasing our investment there to secure this crucial relationship, while also noting Germany's potential permanent alliance with Antananarivo and adjusting our stance accordingly.
            
            **Maintaining Diplomatic Strength**
            
            I am reinforcing our alliance with Utica, raising our relationship level to ensure marital alliances or continued friendship. My current focus remains on monitoring Iroquois movements, our gold reserves, and upcoming World Congress outcomes, while also ensuring our persona is optimized for the emerging nuclear deterrence phase and our diplomatic goals.
            
            **Optimizing Unit Capabilities**
            
            I am currently focusing on refining my approach to unit AI, specifically prioritizing offensive air and mobile units for swift action. My aim is to bolster defense and anti-air capabilities while minimizing investment in naval and expansionist units, reflecting a shift towards nuclear deterrence and strategic maneuvering within the United Nations framework.
            
            **Adjusting Flavor Values**
            
            I am now prioritizing the refinement of my internal "flavors," specifically increasing Tile Improvement to 70 to ensure swift connection of vital resources like coal. I also intend to re-establish strong diplomatic ties with Utica, setting its relationship modifier significantly higher to secure our crucial alliance.
            
            **Refining Diplomatic Interactions**
            
            I'm now assessing our relationships with Spain and the Inca. For Spain, I'm considering the implications of our ongoing war and ideological differences on potential post-war peace negotiations. With the Inca, I'm maintaining a polite but cautious stance, acknowledging their significant military strength and voting influence.
            
            **Solidifying Diplomatic Levers**
            
            I am now reinforcing our alliance with Utica and Vancouver, aiming to lock in key relationships for delegate support. My focus is on finalizing these diplomatic connections to secure our upcoming victory in the World Congress, ensuring all necessary votes are aligned.
            
            **Reviewing Strategic Inputs**
            
            I'm currently reviewing all configured flavor keys, specifically setting Tile Improvement to 70. I'm also preparing for comprehensive Turn 403 briefings, focusing on military defense of the Bregenz nuclear facility, Iroquois corridor forces, gold accumulation for the Assur campaign, coal availability, and World Congress outcomes concerning World Ideology: Freedom and the Vancouver/Antananarivo spheres.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: MmXrDqq5SDuV0JWl
          - toolName: set-research
          - input:
            - Rationale: Confirming Nuclear Fission as the next research target to unlock Bazookas, Nuclear Plants, and the ability to build Atomic Bombs at our Bregenz facility. This is the critical path to establish a credible deterrent against Iroquois aggression.
            - Technology: Nuclear Fission
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 4m7Y1qK27pfGIj14
          - toolName: set-policy
          - input:
            - Rationale: Maintaining Containment as our next policy. This Level 3 Freedom tenet will provide immense influence from city-state trade routes and ~9 extra delegates, sealing our diplomatic victory.
            - Policy: Containment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: P8wdMThpQfjJ7gaA
          - toolName: set-relationship
          - input:
            - TargetID: 30
            - Private: 55
            - Rationale: Correcting Utica relationship back to 60/55. We currently hold Ally status at 1415 influence (Germany is at 1094). We must maintain this alliance to secure our delegate count rather than conceding it.
            - Public: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: EW8UD8rbr4idXBf3
          - toolName: set-relationship
          - input:
            - Rationale: Increasing Vancouver to 60/55. With our Sphere of Influence proposal set to pass on Turn 403, Vancouver will become our permanent ally. Maintaining a strong relationship ensures the AI leverages this permanent connection.
            - Public: 60
            - TargetID: 22
            - Private: 55
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: Db1PCB3exE4HgN0l
          - toolName: set-flavors
          - input:
            - Rationale: Raising TileImprovement from 50 to 70 to ensure our workers aggressively prioritize strategic resource tile improvements, specifically searching for and connecting Coal to enable mechanized production. Maintaining high Defense (90), Diplomacy (100), Gold (95), and Science (90) for our UnitedNations Grand Strategy.
            - Flavors:
              - Happiness: 75
              - Culture: 30
              - AirCarrier: 25
              - GreatPeople: 65
              - Infrastructure: 70
              - Naval: 35
              - WaterConnection: 35
              - Science: 90
              - TileImprovement: 70
              - Defense: 90
              - Airlift: 55
              - NavalTileImprovement: 30
              - Wonder: 15
              - NavalRecon: 30
              - Growth: 70
              - Antiair: 85
              - Mobile: 80
              - Ranged: 75
              - NavalGrowth: 15
              - Diplomacy: 100
              - Espionage: 90
              - Nuke: 80
              - Mobilization: 65
              - CityDefense: 85
              - Religion: 10
              - Production: 80
              - Air: 85
              - UseNuke: 80
              - Spaceship: 50
              - Offense: 15
              - Recon: 20
              - MilitaryTraining: 65
              - Gold: 95
              - Expansion: 15
            - GrandStrategy: UnitedNations
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: a1em4XgUE9ulVt2W
          - toolName: set-persona
          - input:
            - MinorCivNeutralBias: 1
            - MinorCivCompetitiveness: 10
            - WonderCompetitiveness: 10
            - MinorCivHostileBias: 1
            - AfraidBias: 3
            - HostileBias: 1
            - Friendliness: 9
            - Forgiveness: 7
            - Neediness: 4
            - NeutralBias: 8
            - WorkWithWillingness: 10
            - MinorCivWarBias: 3
            - Boldness: 10
            - WarBias: 10
            - GuardedBias: 6
            - WorkAgainstWillingness: 8
            - MinorCivFriendlyBias: 8
            - VictoryCompetitiveness: 6
            - Chattiness: 8
            - Meanness: 6
            - WarmongerHate: 8
            - DeceptiveBias: 8
            - DiplomaticBalance: 9
            - FriendlyBias: 10
            - Rationale: Maintaining our highly customized persona: high Boldness (10) and WarBias (10) to support a strong nuclear deterrent posture against the Iroquois, combined with maximum FriendlyBias (10) and DiplomaticBalance (9) to preserve the cohesion of our vital Freedom voting bloc (Austria, Germany, Venice).
            - Loyalty: 5
            - DenounceWillingness: 9
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: MmXrDqq5SDuV0JWl
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
          - toolCallId: 4m7Y1qK27pfGIj14
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: P8wdMThpQfjJ7gaA
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: EW8UD8rbr4idXBf3
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: Db1PCB3exE4HgN0l
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: a1em4XgUE9ulVt2W
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.