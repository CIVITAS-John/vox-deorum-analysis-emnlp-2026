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
        - Technology: Nuclear Fission
        - Rationale: Critical path technology enabling the World Ideology: Freedom proposal and unlocking the United Nations wonder for +3 delegates. Follows the current research of Mobile Tactics to secure our Turn 415-420 diplomatic victory window and provide a powerful nuclear deterrent against the Iroquois.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Containment
        - Rationale: Level 3 Freedom tenet that dramatically increases our influence from city-state trade routes and grants +1 delegate for every 2 original city-states. This is essential for surpassing the 45-vote World Leader threshold in the upcoming United Nations voting sessions.
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Cultivating closer relations with the Inca (Player 2) to leverage their 22 delegates. Despite their Order ideology, they have a 100 public opinion of us, desire friendly relations, and are actively fighting our common enemy, the Iroquois. Keeping them highly friendly will protect our trade routes and potentially secure their support or neutrality in future diplomatic victory votes.
        - TargetID: 2
        - Private: 70
        - Public: 75
    - #3:
      - toolName: keep-status-quo
      - rationale: The current strategic direction is highly optimized. Our flavors successfully balance a robust defensive stance (Defense 90, CityDefense 85, Antiair 85) with nuclear capability (Nuke 80, UseNuke 80) and a focused diplomatic campaign (Diplomacy 100, Gold 95) under the UnitedNations grand strategy. This maintains our strong economy and defense while we await the World Ideology: Freedom vote and prepare the Assur influence push.
  - tokens:
    - inputTokens: 25722
    - reasoningTokens: 9386
    - outputTokens: 344
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing World Congress Outcomes**
            
            The current turn is 402, and I'm anticipating the results of the World Congress vote imminently. My focus is on how these decisions will shape our immediate strategic landscape as we transition to turn 403.
            
            **Evaluating World Congress Impact**
            
            I've confirmed the World Congress vote isn't immediate; it's in one turn. Several critical proposals are on the table, including Freedom ideology and an International Space Station. I'm also reviewing currently active resolutions, like the Austrian and German Spheres of Influence, to understand their ongoing effects. My immediate focus is on how these upcoming decisions will intersect with our current research and technology choices, particularly Nuclear Fission.
            
            **Selecting Next Research**
            
            I’ve confirmed that Nuclear Fission is available as a research option and should be set as our next priority, despite Mobile Tactics being in progress. I am now reviewing available policy choices under the Freedom ideology.
            
            **Choosing Freedom Policies**
            
            I’m now confirming Containment as our next policy choice, recognizing its significant delegate generation potential for a Diplomatic victory. I’m re-evaluating our overall strategy and ensuring it aligns with the United Nations victory condition.
            
            **Clarifying United Nations Construction**
            
            I'm investigating whether the United Nations is automatically built or a constructible wonder following the Freedom ideology passage. My current understanding is it's a wonder requiring specific techs like Nuclear Fission, and I'm cross-referencing this with our gold reserves, which are substantial at 9,388.
            
            **Calculating Delegate Boost**
            
            I’ve determined that if Freedom passes, our delegate count will surge to 32 due to Germany and Venice also adopting it. I’m now assessing the impact of other pending resolutions, specifically the German Sphere of Influence, and cross-referencing our current alliances.
            
            **Analyzing Austrian Marriage Effects**
            
            I'm clarifying the long-term impact of Austria's "Diplo Marriage" ability on our allied city-states, specifically concerning delegate acquisition and permanent alliance status. I'm cross-referencing this with our existing alliances and influence levels across multiple city-states.
            
            **Assessing City-State Allegiances**
            
            I'm currently reassessing our allied city-states in light of conflicting influence levels and declared allies, particularly noting Germany and Austria's strong presence and potential interference. I'm also reviewing the ongoing war with the Iroquois and our current military parity, focusing on recent losses and strategic positioning.
            
            **Prioritizing Nuclear Advancement**
            
            The Nuclear Facility is now active, allowing for Atomic Bomb production in Bregenz. I'm now focused on whether to prioritize "Nuke" and "UseNuke" research, reviewing existing flavors and considering a status quo approach to these settings.
            
            **Adjusting Nuke Flavor**
            
            I've confirmed that to build the Atomic Bomb in Bregenz, high "Nuke" flavor is necessary, and our current setting of 80 is sufficient. Therefore, I'm opting to maintain the status quo for this particular flavor.
            
            **Courting the Inca**
            
            I'm now focused on improving our relationship with the Inca. Despite their opposing votes in the World Congress, their leader expresses a very friendly public opinion towards us. I'm exploring ways to leverage this to gain their support or at least neutralize their opposition.
            
            **Improving Inca Relations**
            
            I am reassessing our diplomatic approach with the Inca. Despite their past opposition in the World Congress, their very friendly public opinion and shared enemy in the Iroquois present a valuable opportunity. I am considering increasing our relationship level to further leverage this strong alignment.
            
            **Assessing Spanish Peace**
            
            I am confirming that we are indeed at war with Spain, despite some conflicting rationale notes. My current focus is on understanding the precise details of this conflict and determining the feasibility of an immediate peace, given the reported peace timer.
            
            **Negotiating Peace with Spain**
            
            I'm currently evaluating the possibility of negotiating peace with Spain. They are a distant foe, and their war with Venice is impacting trade routes. Despite ideological differences and their denouncement, exploring peace options seems strategically beneficial to halt plundering and potentially restore trade, especially given their geographical distance and ongoing conflict with another player.
            
            **Exploring City-State Diplomacy**
            
            I've been attempting to utilize `set-relationship` to influence city-states, but I've realized this function is only applicable to major civilizations, not city-states themselves. This necessitates a reconsideration of how we manage our relationships and alliances with city-states, as direct diplomatic modifiers are unavailable through this specific command.
            
            **Clarifying City-State Interaction**
            
            I've confirmed that the `set-relationship` tool is exclusively for major civilizations, not city-states. This realization impacts how I was planning to influence city-states and requires a review of alternative methods for managing those relationships effectively.
            
            **Revising Diplomatic Targets**
            
            I've identified that the `set-relationship` function only applies to major civilizations, not city-states. Consequently, I'm now focusing on adjusting our diplomatic efforts towards major players like Germany and Venice, as direct manipulation of city-state relationships via this command is not possible.
            
            **Revising Delegate Counts**
            
            I'm recalculating the delegate counts for all major civilizations after noticing discrepancies, particularly concerning Venice's reduction from 13 to 10. This impacts my assessment of the total delegates and my diplomatic strategy, especially regarding potential World Leader bids. I am now focusing on leveraging our strong relationship with the Inca, aiming to secure their support by increasing our relationship levels.
            
            **Improving Inca Relations**
            
            I am reassessing our diplomatic approach with the Inca. Despite their past opposition in the World Congress, their very friendly public opinion and shared enemy in the Iroquois present a valuable opportunity. I am considering increasing our relationship level to further leverage this strong alignment.
            
            **Adjusting Persona for Victory**
            
            Babylon has denounced us, but our relationship is stable. I'm questioning if our current high Boldness and WarBias align with a Diplomatic victory. Given the imminent Manhattan Project and our defensive posture against the Iroquois, I'm re-evaluating if these traits are too aggressive and need adjustment to better suit our ultimate goal.
            
            **Confirming Persona Suitability**
            
            My persona's high WarBias and Boldness are beneficial for current conflicts and competing for city-state influence. My existing friendliness settings also ensure strong allied relations, and DiplomaticBalance further promotes peaceful resolutions. Therefore, the persona appears exceptionally well-suited for a diplomatic victory, and I will maintain its current configuration.
            
            **Confirming Tool Availability**
            
            I've confirmed that the `focus-briefer` tool, which I thought might be available, is not declared in the current toolset. My understanding of the available commands is limited to `set-persona`, `set-relationship`, `set-flavors`, `set-research`, `set-policy`, and `keep-status-quo`. This means I cannot generate focused reports for the next turn as initially considered.
            
            **Confirming Toolset for Action**
            
            I've confirmed the available tools are `set-research`, `set-policy`, `set-relationship`, `set-flavors`, and `keep-status-quo`. I will proceed with setting Nuclear Fission, Containment policy, and improving Inca relations. I'll then use `keep-status-quo` to maintain the current overall strategy and flavors.
            
            **Selecting Next Research Options**
            
            My focus has shifted to confirming the available research options. With Mobile Tactics underway, I've verified that Nuclear Fission, Penicillin, and Refrigeration are all valid next steps. I will proceed with setting Nuclear Fission as the next research priority.
            
            **Selecting Freedom Tenets**
            
            I am now selecting the tenets for the Freedom ideology. I've reviewed options including Creative Expression, Media Culture, Civil Society, Avant Garde, and Entrepreneurship. I'm also evaluating new branches like Imperialism and Artistry. My current focus is on how these choices impact our delegate count and overall diplomatic victory path.
            
            **Clarifying City-State Management**
            
            I've realized that `set-relationship` is exclusively for major civilizations. This means any past attempts to influence city-states using this command were futile and will be ignored. I need to adjust my approach for city-state alliances and focus my diplomatic actions on major players.
            
            **Improving Inca Relations**
            
            I am proceeding with strengthening our ties with the Inca. I've confirmed their ID and will be adjusting their public and private relationship values. This aims to leverage their friendly public opinion and trade partnership to secure their delegates for future World Leader bids.
            
            **Adjusting Diplomatic Levers**
            
            I'm reassessing our diplomatic stance. While our relationship with Babylon is stable despite a denouncement, and the Inca offer potential support, I'm prioritizing peace with Spain to safeguard trade routes. I'm also ensuring our existing high defense and city defense flavors implicitly manage military garrisons as per tactical recommendations.
            
            **Prioritizing Coal Exploration**
            
            My current focus is on the scarcity of coal, which presents a significant bottleneck. I'm assessing the adequacy of our current Recon flavor level (20) to ensure effective scouting for this critical resource, especially in the area around (12, 32).
            
            **Prioritizing Resource Scouting**
            
            I've confirmed that our current Recon flavor level of 20 is adequate for late-game exploration, especially given that most of the map is already revealed. Therefore, I'll maintain the status quo for this setting, focusing on other strategic priorities as our overall flavor configuration remains strong.
            
            **Focusing on Research Priorities**
            
            I'm confirming Nuclear Fission as my next research target. While Mobile Tactics is currently in progress, this new path aligns with our long-term strategic goals. My attention is also drawn to the possibility of an impending World Congress vote on the United Nations.
            
            **Securing Diplomatic Advantage**
            
            My current priority is solidifying our delegate count for a diplomatic victory. I'm working to improve relations with the Inca, aiming to leverage their friendly public opinion and secure their delegates. I'm also reviewing the impact of current resolutions on our overall delegate acquisition.
            
            **Optimizing Diplomatic Efforts**
            
            I am reassessing our diplomatic strategy, focusing on securing delegate support from the Inca and ensuring our relationships with major civilizations remain stable. I'm also considering the implications of an impending World Congress vote on the United Nations and planning accordingly.
            
            **Preparing for World Congress**
            
            I am now preparing for the upcoming World Congress votes, particularly focusing on the United Nations. I am also reassessing our diplomatic strategy to maximize delegate acquisition and ensure our alliances remain beneficial.
            
            **Finalizing Diplomatic Strategy**
            
            My focus is on finalizing our diplomatic strategy, ensuring all relationships are optimized for the best outcome. I am confident in our current approach and ready to proceed with the next steps.
            
            **Finalizing Diplomatic Actions**
            
            I'm preparing to execute my planned diplomatic actions. This involves strengthening our ties with the Inca and ensuring our delegate count is maximized. I am also confirming the status of ongoing research and policies.
            
            **Focusing on Inca Relations**
            
            My immediate goal is to improve our relationship with the Inca. I'm using the available tools to increase their public and private relationship values. This action is crucial for securing their delegates and supporting our diplomatic victory path.
            
            **Maintaining Strategic Balance**
            
            I am maintaining the current strategic balance, as our flavors effectively support both defense and diplomatic ambitions. My current focus is on the upcoming World Congress and ensuring our diplomatic lead is secured.
            
            **Implementing Diplomatic Improvements**
            
            I am implementing crucial diplomatic improvements, particularly focusing on increasing our relationship with the Inca. This aims to secure their delegates and bolster our overall diplomatic victory path. My current strategy leverages strong defensive flavors and a proactive economic stance.
            
            **Refining Policy Selection**
            
            I am meticulously confirming the exact naming convention for policies within the Freedom ideology. Specifically, I need to ascertain whether the correct input for the "Containment" policy is simply "Containment" or the more verbose "Containment (Level 3 Tenet of Ideology Freedom)" to ensure proper command execution.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: itLJLYZMZRuQWavR
          - toolName: set-research
          - input:
            - Technology: Nuclear Fission
            - Rationale: Critical path technology enabling the World Ideology: Freedom proposal and unlocking the United Nations wonder for +3 delegates. Follows the current research of Mobile Tactics to secure our Turn 415-420 diplomatic victory window and provide a powerful nuclear deterrent against the Iroquois.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19Ve3OcDpev2CFLwv2pvTaDDoenI9E81jOnQVoLZi9DGpIhFv1dlwK6t+fODMump4WbAa7afCLPDVgtNscrqgKEynyZHfJfjXdmamzBx/w1CTda1kqBLPgTfQv1g+jglfbL3v3dCKtrV2ch2jzbws2Qopr6tYRiPc3z1dQiT6Wdyji2drVAmsZkQ68L+uCpX/4ZSgZjXIMNv8crO3YiD+FoT7fDKFAOZRC/IxDpp8Yl1BSxvDsj6NubtGC/MgGkmTJiXY31m/HuYcRw3xGY8xnbX8ftbi2xAMsDkpFg5G9GiEYb82RnMX8rHVd5LLqdtpsc+TywRmIsZXsz5NVy0tYP3VYwiozrme/euVgElqqZ8EBbKUFFETc7n6G/ga+v4QRMeGbadwcrOqZDi+5vKnhMn+03uRWaPzhmOxS3fH3UNOh3c6SNzkoUiCYac4kXUmTaEPoQ3J7HSru/HL8Zyx4ECjZVHz2I5pkRWugJJGncaa0UTx2pAmZQG9CdjTYRkBcTjStac+r0Zq7JLLxfSil+EAF4ZUeBBaFKydSKJfjMuEFQ/2e6D/bEXbsi0Ej/LOwMEI3O0VP5OFmKdX6mtbq6rMVqm6N5/Yylgu7Ot5DS9kD9e4m/ekoCIcjkNKOWQRWx1fEfrDyezuGhx6E/Edve8kmj5a7UH2qNwjKtLQ3SHWT6A75Q7KAlgHsXQZ6m4WYDUpAFlzeSQqF1SpR8iQDnnU3Nqq6+vmtUxD66Gt+p9sniHbaHkbLq37x5MGe4Y+4V7Ir3tcoE8iR0/TlsNwGkka2nnq/y/FbXMS8N9NJrBaHAjiPjvxw16flUgVnPzu7FztuPTEQJ9inELr63Bu7eRJa99Eabq8yaHA22dxds/9k8N93LX5VEtbkJPvHnleZVKcdLQR4CvVSD6604kxoKSALCMn3QvKtcLdwetVop7RzzzRuJmdhyTRoFHe1TaxDPWdCLDq03uQiaRYNunn9Wz15zYSxH1HLxxbbtkWD0drvycWe2EgR/AyHUoo18tVy+X0B3iUliFC5wT4AgM18Wm7GRCJ23whOqg+qAKgSpHvIxkufI+4y+eLPzYbu6v+Njv+8RtDvAgO87/xO261YdUYoZIy2AFbK3X4lgfyy/66klvUnnlwJOh3SdUETpv8jiseUkMRwwhnCha7BS9k2cchQteLiC11a2KkvnU8FurUcPO2s2Mzv4EeHkQynMX7j0t4Sy8Ml9xZCLKzGwf3YKnlk5aXgzl0hOnR4tckQoR87SaxeVUopj/PmeTpmGZSDdmp1QyAA4MgVghBuR8fvIs6EvMIz1fV0fBYQDItJWUn5xViN+LYrQfVSH/NsmhlyLVjeqhZVmzkK8UI+Tw/GS2ArN5j+MTTJ866FWSUurSKn1OgeMsa44h43FpgbEH6tY4xwSyCahfMzpoxMLkAOU/sMbhkY7YP4H+Pg3uIFqi1vHHYXrqgoEDNkWAVgt7U1L5KqYH9qjXB1t9tkiLYRxQbiGr6KlQvQFw/jLWw+5od0RZ7lHeTZ8bW4MyP3eQ2w/bS9yT8nXi5v737/hXxR+eKbCJsc3hGJ6KGBSlrDTq8vHmservbWiM8128UMJ1dJzU3fULDIrAB4fW7qXx9D1B626Mf3Nz6TpfFY+tXuxVxD66a0EWAoYQhhj4OmYUF/EHlp1ofTKzf4cg/K8f+JMDAJGvjm+ifjrqRj0MhdPeupc4gmMZV37pXVlQb5ZxYlltSXrJ94V7dT9uUQr3ySg2HONVPWv3ngHw49NfSpqff2q/JaQ3rOXw632QjjZzwocJOa0CBuPOTYvaXrqfNseJD+plChmrQS8fsEhaPRQwX1u3hbOmQNORPb7qGuNtHdr/Eb4uV+LD6Z+FG744kIZVAXfmFKmb75h5On87EnRWSe18EFITDTc3ynvYRhCFMnszfTdz+F5h5i+c/Pw2bs3uixTkoIHY3At6mWk/fcc8jSLx4yOzWd1K1/bNk7+Whbs1FiNUVFsQXg2rA8146iDlZM1SHglgsjZ8LHhrzLYIl/IquYxUKPLZpei2wpY+uk4liNlZxuK1eqkXK1+tVutXp6L5xbgGhMvipkakVjSnxOvHXHd5cWMUfdGescdA2NCBs7e22BLpiG2ooThV+u7iQfYda+ol2Jw5mjiK46d9FungP5oBNIXU1wp2KugikJCYFA+FUyOtH4Tym2NT5QsgDRO0x2WRqLCK5admOwU7MA0mvjWwgR0ByqmING60U2dnGZktc/3o/ucchtPrdTFG3VX/jySkdQEaLcix1MW8SXgTkvtjxQMGRd2T2VRWdG0/SOZGc46/wWaXvvj8g8O5PvZBzOFEJKiFV0cKIXd5LhnnCRTy4WEygwfDCFEB26YcXfIwqRr5lWZh2cieQ7RhHOscFZQw6Y7xP8TkawUWyrIGCOMfpghxh9qvF5yOauGQCnfhkwKo/PioiR6cwBZl3H7GkgXjPJdIc/eNFZTyrlj3rgq64pM8BbLXl+c3/lepvKnX4bV0WtJOsc5OFgS9TXv3yvMThdCcOTGQBuIHS1MjiGe5r/XQTz8tlk9yp2ApaHu2b8/wcmY6J7jHvJfqlIBucmBBIkswYEql5mxPqWSEmf+fOL8a1vvJI9YLYmLPX2wQFffX4OC7UhPGdTkPYL83YrhIOOVsl7UG5Hi4fDPmCoS+wCbCPBwv96nIqdVy1K+2GN4GYVQZYeGU7/NnSj2JTzJnkitc2B2YFPweN74ck/P5iQ5/HUCNRIvuBe+kiTFAu29wVHole8C1hsAcs5XfDLS6xXRCYCbLY8PKyxT057bf8AHB81e8nEomQTP0aLcUWqfORpzyqC+gmLg4czJTXeVOOGRhJgSybMnUBXW2Iz53MF2zLJeOptrY1DXxdAV4XfLOuHci064uKIKy0OmFpp0IH1ScPyw3okXb3rQwp0xiLy43k7yMlZfX4zqc4r/PlS1161VhqdH3R/gWsl6R8vyMDjmmHXyCb26qhay/dCOmko/tFddV5Ues2PhqR6ZI+iK0Sn61cB1mj/lMfav4Z74+q8niEtTsgtLec2vpM/l180UGT2FWYb09awjsFJZdbSL4jMlX4LjH2Qxfkc43qm8EXOZoX3tZiqD9RxVqGFniwh+aBJwkbKcSa7ZB0E1QbacSBIfFFf2TE2Nil0+b4x+/K6TlRI9EBn2KE4o7GtWiAciaj8R55nMDcSfxo5kVwp5NcFRlbpOotNMJjjgJUDONR5sasc4AseV+vP/M0ixjSQK1E+EFn46ZidSDazNRFm8i+RxuCPLdqnhNwfhzthBKSg7ES1Sc+7WHrdg2M3zVukUDKzJkGLagHKv3tNdh1yqWvMNIUHR/VS9KodJu7x4jsBSj0MI3urGntPlCPvndosAHIikcL/JS0dy16NeIJY/yO+Vbj9f4yYL9oiSQPIJWjPn4HMtCwt1VbOj3DiMtMdQ/cVUk7ynOJo8UqACAp7fvjNXkuBZ/rE3bbYsgXG18idZCTeGu4Dx8gcz/PCgYRvfv2i8V7NeXYhXy7HhP3AyU5A7IHSE8kwf4d1xf2xEuiho+IOoNpsCvnAhpi+wCf0zqwTw7jZSHExJCNOmLHRWKb/+5apjoaeioxYt4NkfIe32/+20OQBJBwP2a+kWcGrR/IaPmuKzPNeoxqP0mWifF95IuY0HCyMrH6gqtCcEghPD1ILX0XaOdLE8RqgGjRfOMate0p0pxvStzDt1LGDiwQFUb9MFj6JKI8hEmgiV2OCgy8PqcUKLM0+MemBRk5jw5GvfdmMPeWnrKLQfvFzQe329WivvrgvfpOtHe+E8tGCj6E1JOMV2zdxqGPTtVewOAystZq3VtV46LZ1t4WWIPZeFhyJHsKYf+pPPyzNXrjxX5cVpflEgtWuRLaVwPJqQ15RYSUYlbXy0xdtkMv+89WcQ2BfXdkOVta4Y2tJB+xP0iNqYCjhHWN8q8W+LgoeKrIrIXW4Vt2QByRM6S7lh62PYZhLChUwTVoJVn4u0759R7rN5RXzGOOsbaWoikab5yRu3c+dQgHpbhpO+Hl7y0SoD07xIHvHbGvf0tJLvg8Vp1Zgtwn9WJmJ3Y2WRBmH8UbAxg8c84NFp6/38hzKw8Xr8Yq7E34dOqM8LW0kHKMDhSfvUJdnW0nwzifLD4fzumlFHaMHRU0hy8feW1qG5ld1y4mQi/oqSravqxs4ckFw4/IxWOoQiHXCuUqsKvHLlCW8Uyb/Cej/Se+xeaNlAolFagEAbvNfOnb/72YExevoDAbeoiIw/z0UcIe6VHlvSslWT5Ujf39eRe1U4MQj8hWsS6rRNnYb3xezUydu4BTh6ftgfjIup+60Mqe52MzsCndFp5aYiRWnkIPpHnXurJHPRuniXyoIPSQ31HNjule14TDXVAR22+oV4Gkv6DRihzzjy3hAiugRHwK2EDA95qqtCFrVQc8Z30eQEifNQ3mez2+eK3UjqcwiPVsvErFD8nJmS4aD4+jGNhRa/BQcKkPa+AAUFysqR9CanVjiAo6PNog6kt/aLJN9GqQxCIhXx++npGwy5VXKSMiu8RM1PKMJOdq1RdIjLGspz2worcWaFu6yHmlGTro5Bc7er1Gl2Lnd8MEUy1TF9mTiny5PiCq7cpiNG4uOsXIklMqC4NMZFifva13sNwO0w6PWaeBBGT4WYs8DIFSgnzpnTBTsp8ToaCZYh9XJ5q5txXWxvGGGyFcJU+ctbQARCKXncDGdZH7WEFW1HmVT2bi7IhJbS8VOgyaSQftkMYUZkrUmOvOPyKGmk9Kc6kTDQBOV4R+P2cG8ykAbXpncWxsuVxBNbGRaRVp2divQWdw8thmT/VaGjhNVdJl06lHACw2cDmj8F/n0lOd0mzMfPFej0njwUYH6bwU8XmwmHfvfQLuG3jYOx1jKbvCpDQcG1XfJ7ofCYdIJJcGSDkA9FYajcdc5Z69xQOGC3y8MalAWWKfdq8R3lJrM3yxhG2nq+oIe9H7U+VkZPw07uV8pj+6tLiwJq5M6XdQcwG8nLqRQo0afojZnpmLmUI2lXh2itW3mKagrWWqIXCQCu4SLMN9vEr7JWt9jD0TgAkfrRaoSSIOAJ/8mEmgrKT1lhxSrYheeIAMT1bvyUa0AdhSiPvhBm3wqCC3bIHYy83cvLXBWd0x+b7Xk3zjlYZcGjG+81IhD2wUwkbtJaOC+q3A1zjW0YEyVTBlvLNsmBQ7juN7NAuv2En3f/1P00e0cVnBZMNM6SM5Z/J9HjiPoj2qKV8znIbh300NFtO12uBtKSwieAhEQ2szzeNqWyhxp4ox2WNk9kOp7ht4rOA2BhiMvshZ9qZ5jovqaxN3fXxDU6g5R9GXH4Yci78oqljXb044k/iv+YqnIR8s5DNLOjEwSgkGBu/buMqegQ1ThJ1wq0x/Ov1f+Ytp/iW07+BuMvoJ07VogqBbKEtuk51QMXYf/F9vZDEfY3WcTbGwqOTkYQlCQVBdSy3i9prgyoWK5wAXGu92j9SZUFGnsEfXqLHwxvr1vWhJMKJu9FOLr8QQ5sSYfugACQiV3fHlGGpEVM6NKiA48aBSknB23hlI2WkxEOCMRLLSTVUUYt6X6frDXZv7jRuo76A8yj6TJMx+TZXisDKfPhV/wJnvn4r7mPKejNjWGH9PAn6Xvs6J1vy+kTsZZZ+Dn7uaYq+qg1yRIwSCe8MjVYY06IjZL9rIjmwpG2zDqxV8cf5AIx8Ox583FcoL5xiKRoykkRIeeau9ZaSL4hr+8T6oNjvxrAAQXnzxEPX3aF7yTjAtotm0bJEx8MezqOHnaxawlKlswzeiB9E4n7HyhfE4QlsC7Ghyba+/QcydBC76oa7Lj6bHwM1mv3z3kXHIWoO24AMY9jkh4bICVDhKM8V06gNrs/Bk92F0axFk9iEZN/r+3uH1Y8CWBFW2cKsU8SL3AE2vcV40AQXfkq6f45WwO1tDoV+rMlWWPHRm3gkN9dsUyb/bS4cOrBIWD2EsIlpWOiYq0SvAK/29NlIZkz4ywFbySrmjRUWSwoNrI9A9+ZSsXQBjziQmb9p62G8HmZ9cmNNmuoiSzd5HVM7xOZRgIZI1BLVlFuOmHzVxPGnal5HWcz4NF3Dc2f/3rIX9fmb8T6MdSBhwKFd5p3aEiPoGHW+nrGBtG4jmzh7uJu3ZjkhYvKuBkDv2TOZoLO4M/5fCmzgmSYKN/HTGx5ax3va5YEKrrLqzbawbHyL60S/oDRQoGdhDOqxJ1fnDheNoqZHp4Rfvg2glWu+R0wlN//VYrMaqpDYKNM0lUIpjx3AykznF7SR3GT3/+Dz+MEr+hruLmqM5T2V999r9EZGZNK2SJYsnqyRZBco/Jt4wQ6pt+1+O6UyxWLyWY9wkOnA9XEawYeBCRLzaCnfZ/OUiluAamXPm6+F7C0mqgYKLsZRMlrmvFOI9V1dy/tkNDyXlUFYnoc2zAjqsijD4rIj+FDu3PRoroPwmeGS2YIfUz9px7sCjuE4hPS6ZfVTUI0nIvuk8lUvfbwGkQmry8i0VZpB7PRmCw11A7ia8iuuidqXmrVe35gBUjY0RcR6vWUDS7CYsNsfZAP0w7+G3+bqv3TYwUIo21fO+8s3vEIumeLD6yloXlWk94MsYJtfNHCtS+5jRxd1ktGbd/OVmLvlL+HYNHo3yqQXO5FQw00+Fk9pUP6p60G4CzaDCtfMUBcvC5wwDZCkIAkbFqv7x69ApBBCE2PmEVe9ZUyWr904/3CYD5XWpzHo+1gwKLUUhA/x4DCYmDg8hp13OPDq1G0HTppfusJx26J2fGnqcqGxee/9ZDA1biYr4kVYCDV1/KNk9yLdrdrbsrWWFrhvVPJJpNW5z2RHXoaGK2HULodTYPxdBpOR08A48bRhSEFlb7PkGZkPIwDnonEg2diBJaCr8B+KrZdZ9otdRcq1WIldNRPWPblHltZdqYORSQUiWo/D2CxFIRtoe2r3K8/1YVIgFRhhYELhcT4d/ID7irXgU/V+lvTnZKfFrLkrr70oCOIsYYPeRA298lbJzMl8wPk3unauvUCRmJC2JwzeE/Uvx+RELN2Wk4r3T5YblGyK/PORPZb2Az6Ewi+Mc/5vK6b5dsiF5yyo1PHxBZET3bO16KJ7nXXFFNhV1t4keI4PdoFKS0uwGRtCHMhwDKGOz/S/+G1Yo/K9eL4L2tsMHc1pEnNMSz1ipeQUohTXiykApDymaCl7XAv4z/8/tzTmBDExFjcIZoNlWV9wDMRrKvnVFqDaaylmr2pLogdzLBhoy4rg8oF0RHRS037KUkl4T4vCwicJrBS+a6PyWH+zRiBlC8rFm/yS3mzbhRYg4cLxJHHHMbw7Td1/10xnyjQ2mnH0GZMZRUJNk+knI1WVw33og12ibmTNOV8fhBXLuj0AjVeP08BuKJhCwE7kMuH8McD8M1YBAc41IOEGzUscEGN/9CE/JxOLlwTPSSz4o3beHLUeGgFgJGeP4RwL79U0RLt+nuywOSALjMbvetbuwH3TnrHOy0bEMngMB8K6FGOQb0W2cExYQTlWwVwWDF2/uaj7ZhyGNx2376G76BSGXOiZe75SvGHYM67yUZu7et37Nlso73pEDWvE1xuPcwDJauefLlZgVauEs1jpVbHwQ1EB1t+60EdyDswZEzarzCv6wNWl3RHnr40Wdh0ubXs2Jg9fW21H8BFjlJ6c700PhhU573n/oXKmRJkguXW6af79H+Fc55P/wJxf/fiDXGwrh/bB9Ej5y0KEajxB4FmNPW6WNYrFZ8vjCJzOTk59pOtlgSADFPsmqvm7w8P7KGSKn2oKxZ947MAA37OwG5qqftze8p0hm+Du+K+cXaOM0vpc7ewqSBecEbPk7VTePb3FpHJCOl/J8SnVCCCWQaegTkIGxCqTBzzewmlUcaHXMT9wFlcMQ653yckrns1juMpffbYBLPzmZWpcty87y+DaHLvd3TTQWsnMTr3S3AeHgHg3cieQX3IMzU35JzIOzCco0OCQ2m8dJ/oSxUXq32DKgXQ/Anz5xmOV0tYMwpYQo3aFtKzwmhK8Df8++EnAResUQkeJs7+xsVUt9DGQXcXMasXqPEHKIzgGpPzJhxlaPpNp/uNFGQI2bXbO+nSrT2wEhLayPmApydIJMTEvFves5oBVgOxlgVHelgvQwIxNi02O4CdAVR3k5YJ+XmrnyLqJGmXjt5oW5f62xeBe648Ej1Hsy8vMdZHWA6ttvEROEb3wwQY/awc85WXAKGd0PpqTvQj2Eib7hsUqPdNN305yqi4SRKRWveAqd1kvk4CFalI0Dg+Qoj19t9E/sUzsRmOgYqM50dytY5kga3ItUJ5GWkl1SBwdbu3Na1JyyMGKCqlu17mmlpkRanDl6P24HrrwJGEE1nlHO1wMxPbgzidR2ticO6uD2R3fUElulndhVQTk81dV8s/3OLmRw6N2aT1SfMiauImrffpwciNmMQ4LkQAErhEOhD8oqfRurI9IcWsQWy0eV1tlV31tHWWTkLZPh8yenE7JYJ/oaBLVZlAzENRN2YyGnpHFYuJAza/13DTZOlHjRAxm99s5mH1Gv1UM35LvOEbL/XbdUhKCpr6mcuH5n9HCT4i8MbFsewWKLXBSukO8iWGgpsVJEoj0rfpcPX2wyyyCl9Rr5y/WaZmAKq5gW+cRsSuBKvna067k2r4iULP+D4rKFjgS8FW/6sLFPyPS/77RUUUqNlcdw7NiyxbYQEgiU+kP0R04VTnbnV0p4VniOBwzXfmGW0htcSQw+nxjFrM3k8oocaATqjgySGEVSn3Hsu0shE3X0rW2CC0a72DeiD/oyBBkE6OgU7iCKcEbOUXHWLw/IGIC3EiM+wx9uCOwa92uYFPV9yXbZYk6Fu5qdEW/1qWq4j4dWwpxERdNLnfWPdbHzTdH7lIIahnwXO4DWjUmD6ekRohrFCN78ImQctFU3TT9FITPe6PiOGdQHB6G7BLcXT1ME1mu5wKjHuzKeOts9ZO95MrcC4//BJ4uRMGY52cFzbh8jTwpzvIuhOBckDKYlm1xM6zh6eKVGWJOsBHyRaxlj7kNsYTfAcPvIHmU1p2LfToQAKg96mLfsscrgl78UjK+1l1KgwtuptBdWu1dGm7708QfydGBkN/0Zd1DfCnKWgr9zpG+hIBv6suxM2I5N1RV3rKCTDb5DsIGhPEt0GmTxCTTVm/nEEBdki2DwekTbVFaSimTJIr7WXjkfLIDZ/ihMjs3No5sM/fVuXiQVb3ngH2OH6xWDXQ9YjZw/X/k1wDzC9e8nMwsljFrgTjwTn9+WUue7rJyGhKLjxDZa8nNPqogomIbIjs9GCHJB2TU1rA+zTh4NOu5zdIc35RBXgG9zs7ddCdLUV57OC7Hvihca1XvOj37xli9V9M8HylS9DQuvOXrbiWX+MSjH5eEL1UZzAmBqdUrCI16N4V1yhKx9u3IFoOfqXWe268XW2pnQtmUcGwWbAVVX/FbY5AiPLJu/epovDfjAo7ZIGQGfTEij7pIM0hbNb3+1ytluekFSIrvwTqlAi+l3Kq2DhzEL4YguRWgcY87bS413NU7T/PJikl7q8gYBhRf8CGC77aet1FcYGHM2nYnssJIsd8qwRd3vTNLHkaH24SNmZl9tbPuAZA+bJQ6Xw9xiE2V9lBrnP5Ru/b6yBXcW3hDNVjb9AwPgXN+KiQ2vkyqaZOJbQ3aQ02wn3YW7f+4WgRN9hvVoUVvuQRkino1nnjoJ6PzV9JZibdMirdTDU88xJXGvR0EUu8aBG0o+rc1mF/8PDMajnnByIfZ54yofEi7rHTLo02+/Yba/nV4ttaZ43gch2K7ggyA9+gkTP6RFAPNrxPuERFAHAsumKcKaEbEtmMhKan49uQA51LwaZcI/9FrZqpH8SdkdzZzdnyYN/jPg06aNek02NqtUTEDV3wp3rQey+oGfmhSKcDJkj7+CfRQxywi1Kym9lKuyefU1/oz+ntQw5O0IzmPg3CA7cS6Olx6PSUBd1HwpeTdQveAUO+FJk5CeVpCyawg8zPqCILMsySSseKZkJHfdGbObQCQ7JQDuI3VOewfrUiCWrQZmFSaTC8kE2zqC0tlVVNlg7kqvffzA4tQ5C5id8UDdPyMObQDcSjnn4kjEXs0wT1SQjh1Yp/PsMTRgK1WNrXYpt2N0eWVQSwSHQa9RyevKEUHX5m0TpIFhbnGV4cPV8IeUZo5Z9inXIpYkIvYR03Wif2nGmnKL8e0e+YZHu+Nm/fGCcLqs81M8zOaIbq0JCRrp/nt21axavK1RjSZ2W0KnJEX9yiN+6Vjk+pHuuYDktvbmv6QNzQHY04TFJ4r6aFUeXUNgDtQrRcuEFSOrdXRfEW5Yapec/gH99Z6oYFDoDexuiVKrKBrHXtXYzU73iPWgOfbMZ/MEDwkc0yLcqWfnmFs/oAOQ2Px7K84abG29vonxz6jVenUdwLyD17x31kI+We4q7S+Rlsi7nvZ/Khlf3JzoM8syVypoQuYX0WfivqzcaG34RbIaDiIObU3SLSYr0mLA5hq5PgoYeAN8FRkSjR+6/oa14s68OHF++DS+O9Llojl73NuvK/SL+W3ZkQR4nmKtsRj+X6vOGTY+zR4WjeuqGG4NTXP8u2mzA+Sm4zXCyiz7ZQSXXGIYnQA4UGrQUtCjmtS7VlkkMVs0CrUu3zREcgH9I03B2B9HoYRYf631TQRY4NPKX1ccKmR9fMvDeDjt2HGTaX/zruvcIrPm9P5aMurb9tbDrnhTOfQbFmr5gUFV7TPk5M8PsoXI9rjZlY2vBu3KwQ5zrjbLskkApgrW2eTVt+SmF3LwPQpnRllN7F8SFHI9E8Rvz1fCj1LD2KGklq+Jl+QiBw2VYcbly/kCzAUTzuhOX1SZBwSsUPImZeMZ6DsGSUcqZ4FIyfHzsnAdsuiIUNCkFl39I5IVpnxqDrD85DC2JHHk5m3WUcxSB+dGzbOgMRi9nvPRdJj11VRxQBNwe2Ewj1ErRzepaYWGyiUZ4ktelg5WRlFDFsrfNeIKwgVS17le2f3dS+YADmWYvGkSE7kfQQlJsvhN2fY4l3U5sp3WlkeY09G1M7NXtn7rBYA2sYZ9YtRqJ6HVZ0fwZ79ISYs8sJvXBZYH+DndQgeZugEZM9yPD4/sHNt6r7fTQ54aq2gVumnWE1ZNkXT0KwK5TIUxNP1K1QOXpeM+ktR6y0tE6GckJ+BDKZwf6QrPDSMct1SLYQZmWnQLr5fBi3d1LX7K1X6utEaa7Q95T5X+1rFXM1WDKGv6nMc0GB6r9+9x6m62Arsy0QKGBmCooR9oQgRNq3e0idWv8CUffndQ8zM7ZI9fxhaAVTXbT0r5eoxP4VPuaUplAHmbKsZIc5ZtCOC4Y6GdomLJYv3M49EK2l6xfJ8ucfeC7ReL+okg7TBPgPEUmQT/f+ss/fxo/vG6zzRyQKIWKO/M1HVvXTJkGQ3scDbh96qot3SSeEf6mgHi29nFsUd2liXxjGMqqXUj0z3EfJUA9kpt1Xnbz1VR8gsFWC9suA0FTHnXIW02bHDyYj10MCO8wZg1XZTWoe+RYfo+KfJnQRpIEKtN9ECFYX74FTgeyx0kmlWswq8jZ1NtFPBIdgCNzSn54VmNsAg8gr3sbaBdj2zfYX7U57u5qDxmLOwvYRZnT/Hdz45GoX/2MlJDYD5fDprAsb0PV5j5LYPz1DPvDCRfaRaWOC3W0lqYEsCpU9yl9fPEAD4LS1bu00+gddN3Epb5UFo8nZkciaa/LiFbjRcmj3xIUMTSSURgs6PQ9fijOD7KkZwpIEmuUWJogtS7S2MpltB6FwHVRghFWYgAjIsrDjJORkOM0+j9KOtJEjcfU+rg+jZ79XDcZwn1z9Y4Q4UwesOQOTVIEtmxDFLiTYlfgqf4M+Hjhu0VyJ1QPCLfmmrBtIhTu7u53RNAh5iJj2rHhNnjo5QtscrgGEGakJn2KtcIEMx1XTgt66kF/nP7TzDPd7fW6nMdpVZcP/kyZvAUsV3RcsAjzcWyeYzPZKPymAWNczxRv4xBYn4DxJY3MqAprKBVaH0yLZ7bzQV8Nq0efYjKleWpbIsAI6OiNm2/huCNYZYAyPy8uXnzi8qZS0XXUSDMEF9ns/DW0Ytile8thorOlDXiw2cTiCgmwH2saZsoFKUVQnpEjRRpXFMtSP6+6eOOcx0783izZWqiIhdVHI+Np83wreFHUOIR2e2l1brt34saQrMa9nRfbCpytEl5gcJzmRmkd2v0phIDdOjYukSSmdYZSFDw0h2LJYFB/jcjmMikdopXucIq6kZC3eDddkYY290CUYIsL4sXqHTcSoTz7yJsCdA7YIvzD9Seg6ZwggOWpb5qheSfCMx2S7MkBwby4+U8XZzPcbWvtU7mH8wssjuzApnw7WFFF3tCfaRMVtoi1f9A6hZmibyHl2XNKpZ0vQQNYa/xNhiYt05b1kTAoYNThbqZIGra96sRucHDp+kWS3kYO9P8v4xKLl8PNiAn0c/oin7ejWTOJ2jO6rVc/m7h0hu6FJQ7zRDXw7WmPwJ9vegRL2yGKxFby+r6NChgQqE4YeG9cnSx1Yyc1H1iXJVEMR8I+sN4TL1kjhMIM1vtgYEEaokbLRfuM5Q+afdR2tx+IEbOrqVq7zPWgNWvu7HpPlvWZNcuLQpSEU2EzUMj8ncAmnGN+SS3Fwq76cfh4HU9g6iEizWMprk+lC/Dr0ytxGqfigFhPYdhqtqKO0eTR3QNBx8pUIUYsPau8xn4PAMZ19n5wm9dT86brjxy16E5x+7KQkV4BnrS18TeEQdDPaeEPEtaLNONAnoFaJulncWeRwZzi2y80O+CpDiT77oJT/JvxJstr7Kq9n6mbhtnloumdZtNbzSQDuO/rPtzQy5nMluxXXCRqBFTArmn5jciP9udMlFkrn8163ounUR15CPVJ7BhvmXdbhT2TkAK4KTpllCLlTlsw/kE39MhpyQXaXvSridImn5OUxexgxb7Bspf+ze/b+7PmKyCGsY5+B93V9boNtbcT39aMzIG8T1vFSN0BGdgI5thIOcfzgvtNADjrFt2YuJmipWlrAmKjvdLLVGNlrx/HInCP//pyH9wULzyv8s0AM/aBQiNmG8kTTLYAr31vNBtmmvZBHqlBP/SH0vhdyJgN9WtYAhMB0BK3lAjPjsyHBuRTunFoJTKzzvThrLovsQk9rYWBnGFPNbvpXDTihEWUBYS1b+mViJ2+sGtFLXZJl8/e5iz6IH5L4UnT9ai5Jxddk0wngXJCt4N8nAMDx3wdktoui0vtjhMH7OwwXJ081sR5cSLR7Ew7KN9USfhFeCK0r/Nl+aP/7eHshAxsftWkJHQwEVqcjMR5kvldL0zRdcCw6cAWc2jfFLEbVXFGAywwoEbY0Zd2OWbn55xZemahYlezSoyFfbMCYHTLDOhk1FDIqvDR09Xm0tQioUNCTfw1a1w9cK5ec2lZYC44PAszOfrpLXOqHBtt7k+pxTfYtiGfWdH+rNpHPZo6+qEZH91vKaej2qY4eOWmGdt7jVMlgpfF3nlrixvwckOfYgEmEYEm2SGVSr457EKsuO1j0tpaY7ji+k/SLPZxq9vDwtVI8cGAs8Hx/KE8GefQDqjup5Zo9jB/dkKw3Yras2lgagau7zwHEZnXCud5lIDIV/KzEOABA3gyRS/1RO3FEPlzTOAvsp1EX3WPKnN+16k5RqA4ZcignCH0xlX0wwI0hktgl8a5/9/ro3g3vg3K8xGUsg/RWBwu1klI8CaQxphy7IB1JlriaIqKqe9RARP1ANXua5TL4rMlIqPS22NhhMYAsIB54921tYyeTKoARnDbe/ga0zSnM2k7llzgOmu1kBb7hghQazr0uOfuBg2E1ugJ+Hx4hJiHEUxy5q8mL+1IwOOsPnDjQZEqly+BSPoMD1UMnrRIvMRX+Nvg6TNFbobx5jcxehHGB2k+4xMSKJyNoK92LQz8Ycqo8m8HXIXSzvQZvAoXotPrFVU+yVEhiX+KgGHpluMM1J6NYv+Reve8JTI1GCGL5kf6zecN0u+NXh/DQAiEa4gn6ZpH4li8Ql5IA7FhXSeZ2vCogk4tcfpgWQqLJJUeW9mD75GgVzBSe5U4CI0LRV6/eWlJVr4hk8ag35rxoXgfGTxvbhtYk4q3gjnoczOtJsIQdaWIsGcCPwvivsAcTrTGpTN6F2eVgQv7IztlKOqqWOIztmVGDy0/pe8z8L4E8ig6R13WiyGgeouTsXMt1RmiwniVqsKox0bJHeHtuFL2Gl2W1hBagfGiihROf//8/ENu0IXGbRLb8J9+lBb3Yn2a8GJACvip1JYPpBB3gO2HMXagla909CS4fsVjTW9z/q6egQkwd3kHiSeO7KXl22JVUiVcNOyxFOEiegObsOZilX9jKCni6qqPs1b9qR2fzfmG9SoHLnTmATE89/kyml8Xg5Wm8QugychrVlbkSSq+0PEMonX1KIH2qougNzqsngbkJQqbaf76Qe3LBwppd8WeYjZMZuZ1NZdD6myZFkcWkB9ZkttSQc26hSAF3eUelgPoZZ5OvAjKBizCvxwKAelFPqWEZqi9YgzHN6R+RPtKtribB5sCOjJ6a2XpLtNfot/4w3EaRwKWOEDwibn85EZRBM8S4L4bLf95ctoLCI08OGkyjmpFE0KZNwdMnBS2o9LXpi+FEHWtb64pBa/kVVkl0lgpZEhazrzPxffdgPYZJRcVWLLxWIPW8ES9PV49b6Uk+kArogl2ExYI2YB/2XFSFBmu0VfUOjv8Ts5QrM31CtzUcrv/KAZXEmTb960FstNb/DKi170kK/KOvKcRIUf2rz+YtJDHHD72L0dheq1TNJ9hVUZEpgjXEMKV92KfJsH+p4OWnxx7naC3EgusjNIG3qMHsPpc+pP8veb8VHicfeHDlr5xKs2uputf7VGaoxw4N4jWDMTPqXg8CUvaTXbeVsZawpcbNWm4xfto33RkLg4EJb7z6pLoWxHbIGIlMFo4ua3C0Jx74tYUeLhSk90Fnqe5vaYCZx41K/bWhjqjD8hKVhpcJPCptgaFpMoGVVQw5egu4YVKDu6MnjTqQGxeGspWEcI8kqKmiMGHQCmcK4urR9BDlYk+qxTongqV5tGFLUqLQLIJVA25hwIAdxf5DRtZFsImddIW+wIU29G+x55B10UL9vbBuMGjNHAFPPi6QZQ0ckA+TKabULzlrWIwc6jRU7DNwp1/Cz7eKBy7QzMIj7/253Dw472VaTPnTtOP63Ov6SaXyupMLR1HmxpOk8mbyaLADgEuqpeIUyBnBLL90oBRjI3aN3QCvqBRv8K5HgZB47x2mwYfWBf6nEs82d0wbnqSdXPtUbz2kTlBMnhw4iUMVx/LrtsyBcGW53hNP3vAXKnJYaAfYJXE6R5btSkvkC0pRRtwGiAuqWy0FqCTEdG0EYA5ZR7OVHclG4PfANs4Luk/sD7ln3ty5ygd0XG1B1kUOaFSYSq2lkI2cD8thFVPUxe00RFn1pTf9CgOcfn6i7mDX+KLuHsKv/PYA5HkZXUB0b8Nt4hProdO2STape59jJDQGy329OTQus/lulczGecbvkCxPtDyXwafM5qgU/CsQqmldSE/s7zTKWbAr2qwjxYaqXhqNELwY9H2n0mF77j8Uz4RK3lKQeCBYcFVp+8FN4EweDn4tlT/3+6PwFdoL10Jxjvnd5qGA+Fpa99lSQl1JhGbZQBvJpHOcU1D5neYv5GNTvdFrrWR8c6W1e05R93ri7OMc5oAgs/u8o4Up+42bMGMl+5GcU1RWKQ79GlPuI2WeZEWb/U9uRgmiZTgpXGB7eA7//hUCdqEJ61gnw50ycU4/E23AGc/5rvJ6HrlKj5ZprCE8ZRqrr3rCNaxbXfZdYYoc993971DEd7FemGvF6Hdv0oQ9BR4Lffvemyk+xYfWA1tK97wjEqnjbY73zilGYuSQuQWOuH5SPQf5O5TLBT++EogL4x7u7XhAlPI7ehKmqCxuPMD496zOUV/wCp5ZAOf5cnxI8J7FzdLXUlDz3RAbWCgJbVQWg4ujsOxmOSvniL1PnN1P3RuN0glIAyOqW9y5Is9n+gQPqQCl/6K3F0fwEQcK8avIMMCJ3d8RTIFvTqPBHCriLrpmGIFrVeCrR4m0Z12cSBwykg8d5dv+rR0mLn3MPn4OAI4gP7Y5A9tiI0liJZJ25wwbzctuoV1gQFCGwmuNxiV3YO96B/d93OtJai0oMLT6Nvl0fqbC7JcfnkuFeK2OLvUJ/7+N5ofmxaCbb0aEtjQCG1mJ07Fzqy5pAfHKigpK11PzI1zFI4lIH1Bib1s4Khi35e8/CyNwKcdKQEZonwOE749K7VVFanDmF/NSjYNb9CI6OmwfQw+Vx7WL2YZvxLleV+NQ07B9xm9Z1PECIKHOK3Eytjo1pX8zEJwmpXMo3sfJ78Il6MF0lfZEOHDF4y/5wjWtaDNdt5wDiTB/mUGPobC2ESkXvOzO9cwRkg6fcvLcbqVaz/F9mnlpwLVMJMj62Bl5zUB1CbLvFRHHZo4QvwEsswjf8CAY4vU6KtB3ZiqI3UQ9y2ElxU1jJpJ3Qvy3BgIQY0Ik7lJrMSAOPERGMQdQ77PN0QLQ34PQzN7RGQNx7R//kp/OZ6NZjY94a2IQxbk+ugvOwPQ5i4KhSCJr0yfESGHV3plPbGWIqhyt9Fjt7fX729n9XRxyOMry8KOGRWD1IsQWr2TOfB2ETRXKwvJdDZCED7N7u9b+T82EWFV5WyO1kBojGWScMvLER31RzX+BxJWIatTAKedyefra1NvCiLLk/apeQf9ybQrMoPWbwgbrUa0iY2NF8mPa/1zSSn+eXcR8Dx9Cp2UfJRG/vlwiFV800d+ZJNxqOYY6WSlMCXqgh1NPU4UBDNzCHERrSIyvGLmaanehlX5j0ULU1KdDQDb3OevZISYPz+Stp07mnNGmHdGUsr0WJMhUU7s+hVcQlwdPHB7vz2fBdHSHbiNytUxM9Dtn6sLoz71xT+1Q/WaIU/P0aI9GGgaHDuwQ+GnrdmzPOM5S/zib2QnLej773bX5096ga+aUuCYg7i1dN0ipU0TGbHZCML5lvMdPW48C8Ld4a5vL/7zeLFsUF8z5O+XjZAxDQeTlfX4oAaFsRC/F03/C7ZesfiNe+0SuUxk3M7308krBWGnrMCgQQVxcksze+/XylgTtgmgaf0lfJUXQ5SZsopCpnp7Ur7awMNTIOMrfhpYi+psSSApYlYJxqqzJrFow3frI40PUkELO80msDQlvqaRkLaKsGeUphQ2Q9bJc6w/9YxA5SyvbqpN3YLEpg6gpYufkSwxs+Knzdrwo2O48cs4o2eMd+yisoLeVqA8Kx6/BKPyraDnj1y1o8Hqb06DYpjJjynzb4iANhijG/F+QT87zHeos8Qr2MaOuJTcfpqADKX753gpWa0hgjgMgqHwcvypLDbZLK7pTU2bNrDPFBW9RBF8+R6uM4rHxbhsk5hXG2vltJyfSUTPatARjVMN4myG5ULgIVJ1k7SdBu1KPWWi90K4VLAfFDKyZ2gmcoRRtQAf+Knuh+0vlz6pHxczRIUuDJJWUK0XgrqbZ6Lk+DKqmjqVeDx1l18TRppaQ8JaG1Zl0AMYNO4h9OAjt/a8nrJZf9x5H+VzJGAlyOTw5iioXMVD1eLfmMQplMvPzS9lLzON9e3hfgsoOWqlPeq5K1imXoITgp0Pkf/Z0TqIrkL25tkd0qJ6mey9A31sT8381aGnLtMpXWLKZLevTNpA3WaTgNWBzhBFzc8Whi7R+Ojevi6b3DEm5Y96SqHAF3A3fyhuqfpF2yItvar7nsbiJUPdIHSgt9rZ/pY7WhCyg+cBp6Y5CHz7nqxuc/G2OnJ+NmslGPJe9bx76LVDCeT9Si2lMBQaLpi0OaMhdIHm04b9dsfCq4JcTrurR/CgkPT28dQHxcjpYxAGADEFMFDhdaBPa8fUAnLLuFPVFEAuYDKzMpkdLHFCQg/VinTJvVvnLutTwCgUQ/Ku7SyifcfRBNaeIYRE9L9XTUrgX3IzLdbymTxQCf7M+Q1VKtYWFvA1Kgxtx3HcAbPJJXvm/PZWzkZet7zrj4HaIPpvDI4zstsJbdGOa5d8A6EMGjWYcYGWt+kRNtvw0n6qgNoF/r1IXH8bg7gZMfKGvQqr5bdYsFTd3nCEA6GLDyt5PcYOtWUwyBHYCCPVpdrUQpFBWM9bC4ym3n0qwYSPw8RJLeBG8ri5SjYy84V1MYxogkERf5kw+D/2bVc4PI5pYw56fwRm1gjzsBhT9mz7smuNHtiStxrRz0duClWdlpBtF3QDG8AO2cF5c59QRIgP+VOlvRnLWAEzRqmHXqvlNsj3wPaN3wx/zBPJYV02o29U9xzdX3+7R3ARf/JngNuNfpEq5ahP/6aY+QjubGKJjboAMRhyVxkd/UpVXRK/SqRA/ZcG8IlN5h//IX66qCdDtec0gQY3RJ1EVQ5x303El1/Wi3tcsk0lxfEbeKC2MOFqsAxTn8SMfhMLuF/q4ESAeH8aTEWtc2ezLhgAXygpJxwrI5EQgsgDRXTFih2UdjCpvERM/7E8V4AmAh+yI/So2AWmo74wojkTiiQ6fi0OMiGChmwmvIL+H4KrWBPN+qatinQI84/r6cHFo/jNdin4X57g9sqhYRdPNcSSr0u4ztdeq6ri2+3Jwac16RfjWrvAZNhouRz+uZy9c6Q3zDSgJbrYfTE7mzM7z9cC5YDz8Dt34RJgIL5dW3yN4dgXMWgUPKAPPd8AwXub/UtIfvqTzPmXnw45sFZxdpez4j7IzIkn/2FsI3Hzt9LWcxHcHPmD/oRFgjh7fk+hQm1KHBZOAh9zWFMX0QXdHGa4/ihZluXp9N9rFzXD4UtaCatm5yIuJkfc86YRMvmUlnlEjoA5dR7lGmv2y1b/H4gx32cpJR+pI7/C28JfvT70BczQzlkqPyXqGIBuks9NZ5B2tawYcfFCiAYbKxnTVUqmyigpbt//zwwSHWBy+KMVUCTjw29tc4b46HBCoHyuxe/MSI/SgtCOlFAT7YqvRg5U02/bdQHeWUz8nUaK4GC7vVCgjOCnOnUUtt32TzNvkeT1ES0Fh/BbR9CpAfk4pSGC3RqTK/wfzingpz8TxeTNN7L5NYiUL1hIvTXn28E2aiMXuioJTnbClMuxHl1a0ezSMUajlVrRIVNGq8bF1Xquch2ngOD1PytNcsghmDkgqZe/AXf22/s99xEwWT2N3BSteBPtwGNVC6T85pjourrSD3rjulnLVG4tCVoGMw0CqPme+hZydGPkhtdbM79yx2ZT7cr/S6dU2PCLVOY3YSfjgalVwtSOrdh0BQm7hcadibwMZd26cpBYyWTBP9iaYqr4pwFMOpxG0z2YAdW+EsU+831IVa+BiwBSO0+FMvFj7ICud3yQn6g9HOA0nLiX0wG8JO3nOpJ9tl1uG39Tr/qFj5KDb26uLWjX9+kV3Oye79/w4Ym36dVngWE6oVsUHzyswAAH4ueLiLeHnYlfp0DG4TXVCCZkAnLjH5GqPL4O/XtzHbWdTECLH8hwSIft+nZvNtwqQXXC7h5+dZpwVy0XziCfefMC7O4UYDqvqmFA+u5WBQ+wwOhlOWL9oHHqGaYU+Ner8/bUt+e/SSyV+wALpjC65gwYsxLoMmv+DKHxLJ7TzWS7lTU+w3wBdXR7H2Erll423y8fhJrXt7RNukhfnBtpRXQdmGmcQ6frImUwj7eogKb8iaM1W5g5bxEU0fQXclxtCn1HvcWJUWUEAiqruWMwd0qArz/ChXqT1eBuHGHpLL50XnXqMfIfCsAqTWYocltIgRoF4bQvMQh4KV5Rhu2XYWbeueL61zHq6xLWJKNELieQwDtAVT5IwdWV5rRvpiHdb70Bhka8nnF/L+5CrN15V3YlHyZ8HAh4d/uWXVNhg5g6mAzvhKvnd7qKjNIZNg/pI0p1BPTl+hAlJuQ6pU5shxQlIY7/9zCr27W0gf3hKns4WPiLcs/0uGVfZsluBDRgVhVcNqxzsn7vXeeRlBaCbUTWcsoqQQME3hnK9fm8E2Kll9QMauzpyIB0DT0uIkbeMn6JIc+2resrUO3ochYAyxve3jywFhrQFolF9RGcrbZliRijB91vV936EsPgKw0JicP2li64KqQdP6kA7b7ZsOiJDLvR0ufegr/uSNLRuGOzFxH8/0pdkWqgc8QiscdTR777ri6NKtFv/tL68T5Gj7A8id2wgko9jF7xmAHPrOKgW16oMZ86vBkHEASmR9n3sTFZFirGcTWBgyWNkPESsAQ3qCnXt47D4ITv4n/97Hj1E2KEzGJRDw1tsr6V2d0wFB4mdNCTS76xRr8e7a2pjeqr5s9YwRyG/7kXbxpr5vWgGPErenr1f9HnvVkFhde3v8CSl1VhDPK1n1YUjQaWEhAFanOL0R1TSR3v369gBizirbrssQVcyQ9DV3q3vj0RmFA97dyH4L+d8GaVahkwbtmLnPpahAnQqTqnjri+yQGsnkyePeOtzHqGPl7fIJPcSGM1Ygo/b0uZdj9zI1DvJZoDQvowJUfLJGmmvsO7txMox6iW34JpwqEQOzKN3aAUy3z5dXk7paecr2NuB0bdsd4hGj2ddhkZZWWczXw7usPfjGRnJ9s5+EfyTHMJ1y0iM5YFVJ9eBxCnoxy4m681N0i5FwekBWeW33z6UaIfwZD62mdOWdAZzAj6fagAtSmEYEf/II74wiDO1rH5890466/I2yKm/KFOyjtG3Nl2UioWT1jysgZ12dTSQBDHf0D9KVPmYRSXlKIQxEeshF7fbsWMyg5nB3jX3TUJraL761NQhWNzcnYwqTqPZDLzVEB+1RuMyUl6l3fpE989iFBXWU5zcaaIr9YT7bON0DFRDwCQNPP05rVsZh1/NrWSOuQqVTF07BKP5OWhXi4wUoTZrA0UJKaH2qfjFTSc4FPiVbbKI+uhrGB+u3CsTqP8vr4rzF9sBJmcvBcEfFd1YG7CRXKRasuOpwlN803DSSOam0CLhzjG7qXicQxskGYzhI66GYfGUmMElGKbqLN+gOTWMiOl2wr1Z5KG105ut10PHMfMvrjNT3OnR+6Qswk0L7taZWYWLNBa0LW0c25RsFQkO0U3bW0UMghfg+ggq+1sDNfdzIbga8YuCEPsQvBaY4bAxHGiH8vVoMdA/xBQiOp3/z188U/LGAmF3XCJRlLU3YWRH5rhXNrAOkPE+8umJLH4Vk5NXsa8f6z7OXuxbHArF0HDsRpQuV5AU7BlR7oj7QDm3a/cMubesDAysXv2g8kThjVXsiH6n0j4cNoNhiN6yYSABl9eJPbGLFrIXwNG0biu4Z0/++lCvQ/zXXe0Q4itpklyL6epy8uKTEcEUM8JKi1yWOc2UnByOBlKa0y19VELn8FaglGwQZdNRs44rbbsrEvlBTdq7vJ1i1Zk3Oizn61COplNJ7rq+4tI9rkHiZI3lKe7OO0hubEmcs8F7MXrYscs36CCd5gVxeiM41sVb0BPUzSlHWffUd3o93eNGTta0YcNTBgd5WjM+khynk/34oD3iNrKBISBAfMXQqAYDjeBJPo9LziRU3J1MOoQ/mKhD/4e7L0efiisDkF38Wvlrj/2tjA10cYeUCKS6Ka83xC5Lagk/TwtGid904xiDoRTIz1t4LeopEOK1ORb6P7O06pd7vYy63LCh0/L7GPN2KvRbg5CbIlWkaP6disiBw9KHOjEuX/Oepb5GcrLnMaeqo+YUTglTMJvujw4OACY9Jckf3PykTF89SSSDHF0U9wfDE1h/Si0ph4Rhn9Ff3pcjyqc63j9C9w/PxRgD9wb9SKZZVNhkTSEpzbgg1yN+myotiZnNuzLsK3eSJHqAPzThAXMW8Dbewec+WTdc4sLnh3tfXfj6vw7nQ9uGEvgkbo8Q/43yUUdKhtkCgl3DNtd0R8Tpnu07xeQn6+MWvfM3AjQqOatiAzYigkIzU+S14pYmMnJR8+KUfOijt3U1icKNodc9TfeO8IuB/q/hg/ZXaVPOVdQPvVceucsdjpMk7dFMu6XwJJQqs8twSKCZNWKmcdkCUIauQqudoRIKiCb6atjDHk81TAbgueo+peId9868BIbvpvJPTr4OhAPB/Oe4WO24XubV1VR7k21AHWAqCv91SyR9lC0ghcf1v4HslCt7H0Eh1k21ZZSB/sPzcyXzp7KAijlmTsykBEI0r8a73/f3GtAcKm7rq8iN4W+dV2mN9E5YxeGmRkYLosru8ab3oI9x79lnPeYm4eJWJJd9ymhBFQ2y79g+zr70TeOWGhB2dYDu6W0slOBay29zF3xDq7v7FMZ/jOxHjDBSyMnNYAp9uNyQj96hRzWrUDq4U7kA+rTLadSA/aH9/Ig09lnj7GzROhzKeX+DO95VFK4nAl4ohBStyEpi0bmyLQG3zBPxXyObKvVP2UciWi+e4i6ncV0plH3l8UEzGn1y8NY5nQ0w6d9W1LbvYm7EjZEXNX3B/WVHfcmhAPqg99y8fscUY667EHLrz96K9YDibmPazmhidhKmgUlDmGzlfdSskVDKBvhY4f1dbmncAwmLd/IGTb9pdKCz/BwK2LWLCOQOsOEDXMb+FLssAdEBRJoSOS3OPCyH8nAXJ8YiFOZR4w0oV1zYleKSfDLk0ttkCU636UaiKJpNXLzCGYfs30gEfctqHyZ82wIaCYCXqgyyqqDdbvO1p5izkKHCavDRln3jQR25g5Us3ltQr6FfnO78zB2ep6SJZyWdYvPquA2OyOhqMZ6ZnPN2tNrugDS0QK/N1IC5DjIOiJa4hjKL80jIdmA8A5yIXDYgfiInUxa3ICCjpnR48b2JpLjoQE+Pv23C9UMZkBrgefnDhp0KuW+mIttJUK8wyUykY0tlH0bOypyfOeXadphmf5uRWVVqoM47flDnBIoEuYstZx4GiuXUjPbvcJMblDs0FI+KDQx+B/jWP1OaOmtuCew12Q4Co57IQlA7KYD1hfhtkKS/wL8MCKv6esErDOgpqtZoCB6ihuolqs6O5PQG9VyhNX4NYDVFciQN1iywtd/0lwwccLRFp2LL46QgyM+Sulp2hJ1DKrja2QWRIXhJ6XqiRpBW//w3+1JaiUJ0HN0pvnNuwYv4vQTpuZ7QUdW/s4+xyB2y9cJqf9GClh0PI94X32jTU/uBsmPdvDS7qHVv9jbRI0/PuU/Md7aqkbsgJTPK5aLZiiDG+f+D5L5Snbf9j+q0+qSR5thdJKE+BrJL0tqVA7dVgp+4UbP1Mkxo2uyHkJdGw+cc9op73nRR9CYzNNvr1ihsYIfdUdZrUOT3fX8ryzBfk88AkwYDT8uosbQ6vGUFxQmOX2NkipUIuscSnpbfpGWtE1Y39Jk0zhOpUV+hnqFgUEPqWl0Lp1GRrIzXHQ4+gylk+eDSOee1kWWEdW5sdeDx5edfqXlmUASpKBWAtwEdeUTWv5CWnmKyFQIahJX8z/A6FJpUA0DRgdoNI7nOie6ftxc1n7YGFIfa8ZPoT0Gb7ZtMyE7yJvhnWfTVDZFXgzyTxwmwZ/0MugKWE/857mE9HAesUsHvfyLfcDM5X6wZsLGCeF+qY19s9ULrzUqqSuG1SnX3G5TrySQZoq/QL9UbRPwHHBHFpy+FtdxBNUtKMg+b3fN18Eizy4fdQUshOFKV0J+rBWw28ySYfyQ1oxIF0yM6Cr86gvPLWPV0ohSRfM+GPe9Q8CGWXn/vBalu6qomelynURv7MHdrDt6ZjABjc8SJnVxlSbspDUavxbFIwnffUY/FfKOOf3aC+Nloxe+PLLCVTMG70VzZZYGy7DGAj4cBbgIZyiEABMybb15W1b7R0QtQQTA28gkZVESTb6Lj4l4sCwwOHiCoQLmtW9iMKTL5orw0H2NtY+WRBA82yNhVG6AlKNf6TvaMVEylLj6FhEzGe0QUH99sACH7nwJVN3En5jeq1hdLgjbG8aJujurteU50ztJhAzbU7G+8X9Ww4n19AqK7Oe2VyZ/6dISbI1naAHS/QsLVHysc3DJECpuGQ9AEJMtXEfI4k4Uvtoz+9/bMH86ELqwK9IQ4CjbBuiRLqoD4m9s0CJ8bfAma/24+wL8vYK7mQeMOZnV3ZMP98w8Aqq1O9kfa/n1vekIKH1L1CEutt3U6iBT5YxxsqswGr81sd+Uf7J5MLGqc5cxLXTDntuYdMUsd6T9c4h0q7dyqJxtoJ8JoSoVq24vLCt9vK377xtTM5GTQ7gXJQ/rxn6oR087Oq5AmqrQ/jqX5aL17TWFls8rmHO3l0/VBcqeYhtxhShqAGupO1nm00yU/ONbWF/5LJjzS8YvNDTTXFxTYpVnn+RzsEriCwvvnBS07PwkjfXgnWOV/EkIGl/m8M1q5YqSiUoeuCrmAZNkfKLAZrhaA0GUBzcguAz91QpPvWmNd6OYezaldEYwUtxs9pbSbYXHeGxD+07f+mpfzwNb7zWWKo61dmHaGnBr+xVZcFAMGWOJwcD2xt99o02nw/oVWVHufpjw3tbMJUH3g1TSidZaxyG+CH66/3XI0UbIQ4bKUO4yiCTPccRyuFIxi48XhBqbTp15xnC/ya1x4MzGJREV1ipsHjhn92BGlfMMecLTscXhq7sLmxdvLwKtvKfjRV6juOg4WJ5zbRXbrlD1cW5MVMSUTBULVLRPGkhAquah9CHr6WG6PKPLWYd+6VF/6JCZdb7lDC/wHjWilsSJHe7eBntphAMPCaAAYS/NSEHLQgXuX/XsnBlN9UpT4ecWJtMywZf6Kps91QNDK61gsp+vIRjzOvAhfvZtr8midZuNvKE+vwygb7QRqIV41bMnYlS58A92ikTIkJzOd4L1j73BwUMDBWJBwQ/uZtDIFagmh0dXxbCEApMugklfBMeiMUO4uziNGBmbbC8iHUH1uCdrFuxZkkfZ4ilJyhm7VLaDBa7pxdbQ2S0lVSPjQ5bZrWKW+Khb37sDUqo/JipIdbjUzHwf3r3Nuk4/wftuN7dBqzlzjyk1wSk5saEtubAHJQo21uyyy6DfFMCxSvQqgzRPXy6GBmL6N2uX5W23RfVN7AqE6WWXuKdXek6b5bnoD6mLqTOHj26oIeht/PBeZuH3/gi777AY5aZNZoD9WJTeMW8VzfP0WBATsK8FQNh0Xk9Lg8YB7o+1g1MdDZ2Uz94KAJxzaSR4B3UDLnHax23GoVI9sDnwYiMyxX5Bl+bY9L4A+bREWbL/XyIS+taxILCoYlV3E+ZwR0iiXD0DmArmf/szY3B0YiQIEwBY6rKmuXc8NnBfEaYjHPoLpc1xZFI1SMC2+KPXzwQIHRzPaY7xIwQARwWIQLcX/g8JnrASDHl+tpzON8zBX2XxGkyC4C+x1CfnZxUt2xSlZU1M7EU8vZsMuH7PFrO7q9CXdaQC8Qj0VWrVMQQSpxINm41k0rFbu5crLqgW3EQzqvQgBCrofpbpR2LFNSzkX7HtARQPleIam4Eo8V8uWw+0JuITa5/nNQi/KvWxy1cqZ+VL2yTf3HUOViv8ywSgHd/cDRvCH4QkYorhBvepmvCeFc6Z1/5LInsIAVUxBObNXd3aOVxGVKInw+haO0ta2JIEO3+CBg5a5+M+0hly8H4O8lVSIv/2BoORMqRCBHXW7iaTxSVFnj2GD49H8v44LJm0vWb+8uj9MNndcngi5wzWc0qt51W7iK2BospWeO5ZN5EmO56thOZnNT5nZfInebdYcVh+lu4gz0/+8GFhGotsf/19wmOnLpJUucoj5XGYA37ch7HAN/Qd6fqdRImA9Vco1zFfZzonGlz4YUcSY2b7C5Lx0sF4siVg6KxF2/872R1bbW+DtXl/MTgipJ8qP+kBcCofpI0fjVkzcul1O2jJSCosY5+flgRORi9Oazjkv5tw87U/OGrxnb4TiWJv6KYANg1S/suZptWnVrsLZCJTxV6i9irKVCiLYN/4e2jaykdgaGXnd9UWL7tfctb8I4TI3+XwHPVmKFFPjLHlT4YEZ2BJ33ch/4H6kknHOgbAFdoWxs8FyT8HFQnXqoxiqaQeFjvLpTlCj99P/f++vEimju6dLh98ZoTnvq0Q0zrBR0ApKIz4at+f5IIASj6DQ5xArEWYYijTyD1CGQ20NoYmNdwx20Bn2/Wv3knwdNXVYJQZApW2zOZV3WTJtKEWODUWFjGSAPz7LSwA/2YNeWhSSZxJKeOauuWLKR30gR5KlMJyc4X5nGS/y72WH2qpQnmmfkDjvPJJIdrLTerCZkYnOPKkAbtZny8ODlglHoXvdBPwlIk6AkMR1Gt023FY9RxpGTf2mrAnTU4ghtwmri10OSwAaEvGUhkGZ2YocZ1xiOiJxswlhsbIwRYPSd++36FcJ/nMNgr4y3a74ESk119t8PHk5dmc0UEkKDNHdZMT/FXBp7VdYsSgYYPJ++wk1YZZzi0We9xXPxzLbF7Yd84QTxOvuH2zIvLKPUjljl0rSVG6/QGCKDyOfUQYFm1GkhndNwwSUOMGT6fffhrnXgh9JwEfVT8X1Q/WAkkQxcMmESS0usO1RMhZ8yNUfeoyQY9lm9+v6+ITEtajUj9mmwe0Qc5RXbSe3C57ZIlQzapPQIDSU7ilhGNyKrneVDPUg2dpk6l0w8EBFHzUYgzw8k7o5aNlGN48vRL8mVaShvcb+ooNc+S4iAV3pHwF88JhfCs1s5W6lFiyeUIPeISEZDKGbo79E4LKVY60un0j0mdCdDbTOcRaB4pWNxdidxgN5tkQxoo0IE0seuASgiJzfPQENPU8ESHZSYrKKliGLtYiNhGjHODe571+hDHFuCPUUcT6Ky4SyaWzzaguGKhl1lLJQX8DgXpxkH5yKqz1t5MaBIahAc8M4K4/XsFxvlP/ewGMSstwTfR88E72TlUHUAE4viqPOAtWEpThHjmHPaynzgsWp0yFrKZUOWly5xTMwHX9AEaI+xuXC7mqvQisfxvtR3330IVxtWAyZAWEtyBzdpRh7DeSPjzWLeIZHDMD2r0NzHOZcewlOmtLK2y+WnHojEulgek0LQOoaDm78x99RWAYLjbzw3W1OWxyFCmdLQOn6F5vTh8GEsuImRE4roUdpMtWgdw7vrr6MjLakA4cmFyrZaEc0Gb0QCD9m1C+/PXg0MeDgoD7pQkuKXKmjzFhekoGhBUmRWYpc4grmAxkmWGLY7KqbryxqLtT7OiSVT2wkCohmov9dicHoqtdkcFouUwrW0z/b+0ievfEzIuOAUmCFoQeIytHGOoMFkizTb1Wsmy3Kb8ijE686aZp07wqwdbpxqwCfjfDzsGdHHYmcVVFJfxTRN1MfiFVbp8QKoLTX/1HUvxLhsZqaPTgfN+pE7U1PMOWiwWnBWcwM7ai0sjb19TkJ77ua3qNYriwfqKcdBOaOOzUqlE/ruODoV6sNtO7lDUBwteocM8E7/92zzt5GdyrUdTVZErSRkLpe0ICYf+c6uVDzSGbhqxH8tbRbFDjJwDPzV/G1rGRO3u38/5CHvldxyD96gkPmoLzwlMzhsBHdUT2eCzpEa1jPs3Q8v8Wlched/SnqZWqRsOOznHx5bWgNAzIyIfQU22K2CMTjN9VLIMnFjQxjCDIcKynmpPLAXAeSdy5xHPg9JDMOJsKXOfCXKgfOq2hBGTcqURbfOyKaNMQFM8N2P9CAG+1KvZ9fIaO2pv1Pq7bn1M1gHuWh53cyMncTBWSNfdOmWF0kdfdrsH7jcvGIe4vuGgkhQdGW3+9+cTjEg1WKFRjs9VzVf5DOjGCp59s2b45q18gbpH4mdA9SQZdAlyzHLx7tf5c5o0Eo7RdP9VFVvD8ejrEC69FGdZ1b2CJ0bATJvOb8v6z18Ni39OHi7gM14SNUvWVtu7l0oFiaVvp6p5C33gqGXX+1Rf+1P+zl1AdaSaF5Ze6bUvtiWNNRA5exR0i4a83wU9HO3iC63U0Uc7wh85IjNawD3koKlN/04ai6P1FvydSnXtcEOO6poGNeIPhHg64sGeLllWGM26XKP4RlaHuCSG5iEDyyVnk4WdgqXiqUctkdlWdis4tk+9pFrz5V4da4K37TBz3WNVAn2iWmeO3QG420CPRBFi7RlH2frpV/zgWUYwznHvB8679eNB+R80Vp3bKqQeysQg8teuLqduaetizREYDbbihSh5P1dxycsawa1n8nxE12DU8VnIbKGJgh1JcCV01Lt+SadRaUQHwYyP/xcEB2wW0O57dcA+m1uOEq7Hq4k3gzNnNPtfdiaPGIwnDBem5r22uiSslTOdO7qYokcvi+NUyJRQVaHIGwY4y6SIGUwz0lz7yCMXtLmVXhurTSJMSsGyVcCnPSTNdBxGecA/HaN6fTuftgi0xMOMG/Yx6qxUY9jogwHAm6uhpF6iYXiYzkQUgaMkFbSvkl5670VuOJOkNilQpXV65DkU+wsMjz34tObac4GIqOMlIUswcz/hVtdkfVkMw3iuBFqU7behGMmbE4sHUpFGz3WKZbt98tD10DP1wihaNFqHKndEy8uugssTiaIMYWgExBXuuOrJ0eQkjy/Wz9vE2xvJTjpsp40FttNLmh8FlSigxpppqcJjKd6mlLyKA3rKswVUz1pn7M3RfigAe/36U/YB605ADyMyYs6T8I6NIwzkAdwN2dwjkH5WGbI2Pv028kz71nPAiEKcgS7UnEAluph3cIWB+H59zZs1rpt/IM61O0IJGKb4AqE3mSY8EyrClLc81zBLkfbfb1qBK1eF1OFfTGws5nx0Vj82tHazPVXWGUq/Yh6UWeKk3hQQ9GM0M8fFEZyCgw1WQGygAXTOjymZiBfSc8k1+sJFEmXFDALF9mr/oyKJxXJfgA8cbTxQjkx3MYOctSA01hqd17bcgUGUIB37OSw+rWHw22ARYz400/y07g73dwtObUNaz7hqKoEKSn6VSbLHFGmvWuXrK/Yuf21g+UIs7W4TaOB3fMrNnLRIoO8ZXedRZD74NScc8hGYHBifkTFEGGGO5ZMHS2WP/g3viZ0iu6oF09S8fJ8qAcRvOCullMjQsCs6XCjqrnHUw2Tfoy1ncjBUkYwkE6+KuWYjSM9hNsWt4+4MSb458/tZxS+CHOT3rsbat4a0uGXBrSwX7x0mqCdqBoaFdzxtQ0g2G497M97Cm8TAn9nT0qrGvhZM249IxoyMeFFXge6PdMjps9jCyJOQ8WMsKQrMT2OwZuSJB8nIXwj17oCPlCZ9+27l6rKana3+tgdUIAVKWKZSLoDkArNzERY1Alil8FS6ubffKyGRnR5ErjV0HVITffAspyz1HUrvQ/GWgWS+QbNwwvHnjykj/8JDUb8si3idPt0WAmAqzePzXB+hHjdYf2saDcBkSmD/CSaobfMSph6urNKaenXApv9Y1zqiPKfesauEZAJtYavgelEZ6kEjfH+QpBxLBH0QlW5cBDRrHfB9XDpwA2+Duun2o7vPwRmyjZrgvKysWRWgJzNxTR//hTH/PSIALrUrTqbI42IU892HUmeow0+oWlOFjsk2D4AIGST7nhxABZ05wM9PprDV8vB8WtQyBcZOkm4wErn5Gqz00Bvq2Y+IrpE2X7CHwHhE5l8QgSabaJcX5POE7Cbp+nEMHsaf4DJ3aqkRY7GWs3rZ/TwS8d3V9h0nLOujvDxt6XNiBiUtZeT8fJVedd4OrXJJ9CEHJlNIDYQ9/g22DttekJFMhyJ1Fmazkj05Ong6Q3nNo5LcQiSKClQijKt89TBOU8UgQOAW4OzixTTRlggqPuAnhGN7NVHPhxvd1MaAE+EhOHPBrkyOWEC/hnY/sTyE8jf4OJBDv41bsNCfO+hv8YnQxchRpk2opP7BHKwyDpOopc0CejAM5AnJV6DmVCZfaNP3xJJlLA9La6RslqRFlkob/LDJtURUG5vfNVW3JgrNKRnK1sK94yxIXebZCYAZYYPsjG1/aNMRDe2XFxcFJ/NI0R3bVV7MWOmwFjqT0t+Bw1WXjRkAT/XEnx4KXnurPKlok4lNHT8Ibbk4ARgzD7hFevrIQHDkKgBAB2jN6HA+lZl3M0BMvGUHewrId3wGJBQuVa3I/hVJCZRtG7wFee4Np2LUHElWXMSKz03eH/9oG7NEjSRzGwIZwbKavAUJzgJsxbQ6NbHFV3AUKeEjdE1acEjJ2e7Qpm7loEv+Aj6y4R0EC1lDwiUh89k8NsTbn/Ra6bTv4k5Fx6HCwlvNwL/j2snZruuGITPWr1UIRJNTj/JB0D8qxptotHogz5yiAtop1sEm2QaH9MJp921HmNc7w6cq26hL+y3m32jEbjsRiZgcSf9wpREwQNiuXN8LS/ZDcoFoTVnNwRrXCr2odeJaVSdJmjdb+JJVGjqdicsJKXOiXYB8LLpCNrftZy/zjPqp4DD4uz5MPlYNgbXSi6rM4xUrebw4NgwHIHlvKDvBeoOWnVTgOa0fL42wY9zJ+kJGhp4L2HtpF8lFaiQYVChEm+HNZiDJDd5Xcv/lXLf9VkwB/5E09HXlW+HLy2LK07dJRJeU+5PlJ05yfKUzoHtiBMXvCsGjBYOIipRkOMmEbdr1rnfVdUgSb5DUhxy2XCV3BGQt/ORkQ/ua0XljmG+3qDNC1yjRgONBaiACcGW3F0wh2d5GfWaOqyZPkPENM1apSkvjvxh58RDN93QAVtI+lJRk+gWDqFoyTD7eMcm7fV9sX38M7237REWNTBgHzphNpASDsw4ed/GRMCOqua52dccW2ZitiBkwn9tq+YmI0xqxem4hJxr+b5If8PrwELfx8GQB5rGmBkfYTOyRhKIbfb+HyCy+8PSCgKpGIPbzoWtoeJw404qEyqoQPx/+IpbmK9m6CYEvlN5/T0wv+050uPpvHbdiw1UOPz9uZvCVtNM3RiiJRSDRZDFGnaeKgLBIAO1htqxzHrH22+bk3hrua4P26iDtxvXnMn0oo0rlV0de6GYGSDD6vZdSAC4zbjr2FgV9pOQR8c/Ih5rcEAP5NT1g3kv7TyNya4XhdGfWFvdhw7c6sjcMuBKlMfJYZuXYwrj0aKObjVBvWE4jBm5NenWRYDKrXNmrKXW3viAvHYAdkCOItwIaSExYxOjz+F225vwW2DJYQ3m+tUjSeu2irxBP566YEqeV4lBSLme4gZlTxPfDPLAsBAfxRonHSLFWgzqe/Fr8A4ljYYVZLKaUnfE8piClxai7qyNqsI/CTHKhJsc51QJmHcqRoD8aGmteNHT2vp80du+7sWAWe+RFdMedUaypieTzK7veie0VzB8j6kiENNrOjiNhGjpeEYROFiRKutqDnxEbIk1RXAtAdrO/EJcoWHRuGlFQvPxRQg2/E9bTDYnf0gCZVMKnhz5wpp1TuXXI85g+vlqARUoa+e8fMIBjplwMFL68rVhun+xoWk0zmatoeeyEMIVmziGWSOTtEWDAnXFSTCcyvAiWX/y6RaGI89ZzQg/AiLqQYbgz8NbuaJL2xFtukQJ5g4B7DiGRnvWet8x3wH8t+eTZrIBgICm0yBSCrisizJ+uvdgs/nSrA8xTTrIg3k8JC3FmtzbqgDFTMWovKOYbsXmleaH0OzNSe0ZdGChkxjTON44c30zxnZWHioCW87nqF05y1S66IEVcRLUdfVdLSDmNi2wqZM/Vr2UhoVI2M++3OJmY81A99sULMTE+JzkxUgvguRZ4OaKOu+hgK+NEF6tlA5kk7cO/ESxc9j9yf4xslYive4142Ti8JYTqPAJxCbdw3+sBtfVAOi66jX6YLGJZggn5J6+XhP3Z47jYGrTBBMwzxc7iL2gC+0kcMKXMYPkjajqzigj25bMlIN5sl0L5B/VZQEyUX58Upeow3lpPM5qTlW3K4o7r/Xsy8eWmnJBnyBfsk4w5KI34sbHKRJ7qOJViFNsw+nMCbxKntAfqucx3HweHKNJ52wz19iZm8LDcDWWzUsdnLIMNi1knpJ64jRuWSFThuEj4TnGhVProwYl19MWboCbgWTOQIhvGytKNRIAiWWY7HK0D7vkl+gXPfHocfXKG6zTnjWxylULZix2w/yJJs9Y09HmrAj8jIQ5X1KY2Z0q4iDCKysogBTSD41SUpEbHimjWk4LV6rwitCH6/22ol9VuMI8k6U1ZqgPhyOnJQO0qdMscvVClrwwIDWPzwalwsnzwXvscj54cwluetvtsVasq9blJD9wspEW8B8Gn/Xxef/ozbkHYs5Mqkhmmy6QZy+I+sLK1JDEaeZZjAFnCs+2Rg4Ed+I+R3WwA/xpwFrPlvPbKWRy3FzvFGEU7UtRAOucsvyCds0JEt9jfLzfewaEVe2AnGnN0VbqOj0Tk/md4xgyRmKEKs8sGwzP1Xuu2/23+7afocvaXeif4eYGSjOnSnIPcHdjcCYezuudL4g6Z+qKAkq/eT6BALfsbb6bR12Kynlxx9eeTNXvBnCY+LNW0UEupDnJXKEzekNiJ+wqSoo0Ym9yZEXfp/e9U/z4pSWNiaZ1PpL6GrNErlyKpiXEvg241FtIQGu99pbts/jwzNmjNGdvGHWCamSDktiFf2NmtJwIBTjQLh6aei4kfVRFvpyrxx9reVxJWADQlPl3FLyt49QoOt2SMOA0cDVSFBbrcGuJ7EN+fUSPc22HvClSWmBQQqYo9yYeaFQXCOvhETB8UK/xei/VgZ5JU3YqHHHpjaa39cW/gN80bArH4qe6OA4nG+syQln1xpbWxG3taXJ8V49Hn6kdWMlO4A4w75AWNZ+SKXQd3Pd5ULYb9iBjAvIJNvY/E0rwp8KyTR4HOG/AvApLpoCjEZTnkNcxohaP3BuxgFktkeCQfjrTePtMC5mHeTnMDAc5mt2r8n6tHQzqrjEqPecye6LmqdDNTWwNYloAD826FzwJ6XQaseYmONaO1onufv+LAZ1mk/LxzcbEKk+aSHqytxxrba5m9/EjRFHphFoICqq3Bno/F00QEQXyog3oOlGkb0yWOs64ZmB1ysXKdwWwOy5iQtRdRPnml1B0tJarGBJXHLHbEGD11EbjVLuL6GGSB1wn6UMtnUfCTPfRVAv5gNxY34d7i1+4Uk4u1M2jcjcv8IQnrmDipjb6qXD73vWXa3UuHH7YDOBwe2EHiKo0h3AuFcpTNXA1XWJQbKxIEBNvHvDpDrf5bREQGRnq6LscxbKvYpI/gIExhezUbrae5mWBcfzwIGrqgNkDNsg0TSdIPTNZ7Cu4FUhK+D/rD/LzDJRvPwyyKPi/+WBcGpCu/m4CUOQE6mKehLkbIPjWTjZo6TqQHaQnwkOYYbWnsoGYiSowQMd8HENF0uaiM9QC8lEbrYrVRvO3I5747wjo3tlbq9ITgL+M+2LP2a/8jzVhE7Jb93kT+vOn4prMc6RavxKYn6wW8zztDAi7e2TXbChSyEy++P5idayZZwWENaa+8FaBzEjsnrBaaH0rxoW5Wb62yCxIvArMdoT+XRlwUX+z5GqP1yxWcIvD/eo5SkVKH41EIS5kssFe3acyFvE9JVpB9MiGByz7TtB3ji+f7zlB1LdSoI6kCdhIcSX/GabVX2/UokZtHbgJdETJHSm8A0fl3mKOhULkAVfXLYeWu6ebEuT5En1HGikmHhhtrtYf65kiKazhZ8XbqG7PBFVnOddF+p8OakS/u25v1KRqMswswnNvZMvc34Mmsxf+XKG0Jo6hK+GHYeMSm+yTf2YLg/ImoxxVVfHu/Mlixx1aGuESRC213IorypBMhswejwH+kKZATqmmmblnSbk7gblj/XcC0l8PYdwknUp3gLlS0isjKUnL7WBV3qCetBLWr8YGRrvk9YSMReeyG9O9KpZREcNrfLndEVOSgeKlU2FgUucDNf6C7pnEBX0y+tKyqJdCJA6JxSAtuJ1YDDjN9y2PkV+LKZxRsYAO8f86vDfbtyxtqwqFlzTpgXvf4kMds2mDlAFizmESa2FjCm+aB/ZT5eqfhDIDhMIYk5qAAmDV1qB9CyiegVbUSkLmUs9KVYElBhCVy7iMW337xaIL66cdpS+TO+l7e6PWZQDK7xHfB/WWegoHQWELxlQjDPKiKcaf1OkcW11U/PLgD5duUSQCZoRlzXBUYmuabYcvy8S4HWlM1JjpatWRakXx23yyZDgg++FQwgmRFpnbKOFlFWnJntNpGBVt6VlcuG79LrLVIzpOwqkvTL/HAf89ZdmCekwq/BfBIrmEh1OyshM+t1n+GfIestoGJEZp54x0GWxiiSejo/dhWwHtWwQL/rrjK7HIBxNItem8PfEgHVVi6IDVrhUUBDWejn01Esee751Kl9jxALvBv8IaIQddAhep5mQC4PkyuziNezDpVc4aR9VqkHFTTDr/FdLCkbueZB+rLrpMqkMEkHdc5qN2QvV+onzdyh2Tg4Ra70ztVbFO1HAUTFcT1skq3XbX8UaI5Dd9HQcSeftylAjrgwilN0UYIp0BpOi8Wo3c7sG8IWBPrtXNAVTkhh/58hmYKV3bC1RnOl58AmWLYu350eNzLiSbL7fsJa3ouFTFjAhMvK7YQ0L89abxaBhWIenZZVZRqgxPDp38wzv1T4HJdwSXRNI+T3T02O5g4craZXLn7fvpup7zZFz5Xld1K7p0qrbeis4oc4ceh0u0KngnjKTkp1s6/XmWOJWRQGGpgxZWHDy7JDtFIR93FIyt/iiBx8swa1g3Tt5+Y24vwJX2ksaWakEN+T3YS+wv0y7GlRP/+RsmOvfZXWbZfYaoeQLVbJDSRAI5kJd6jNB1tjUXq5gEhExinzgTlBfA24432IvuCkyV+mTGdbbchG+uVp65aCzclHYeH7YTcyNSiIRY7FMt8LjsEsQD9AZC8VppexaPtC0LD9bx6KM6kWs8Gm22xJjrV+z+Uwo3QBSdONKeH267JubEDiBcG1UgLb+e8TngDf6Vrc/WgFOSQczkyiDvwd+9uJTVpPyysDTXOjLwT+kmXxURiqHk+xvArs2HcTo+E5+rP3LUzULPTDDVxNzNsgnYalc8/pWOjLfC8pyoEacoTbPY1MybHiwaK4fUG/lN+35Tfe8FjiGA2abLPLd2q6B7mRYW8yHgv3xPnSqujr02f5bmHMVrEAaj1QbC5tKxXEMtr5CIbKmnUcgt4s3o3UX6IHo4pnSBQYbtSfLBdj42dZWtdZ0qXb2a3cM3m/vFKnqCxgzwD9lFFCaBXQm1jSZaNM3P/zFsfuHjXieoXFFII+M/8JqUqGAJo+EvquZnCxru/QL7sH5Xrtwn5TErNIqO4EI3yMHV7t29qQUz6OnML1H+axwhACZLaC1FrglqmYcynagSprxyVGkGFcut/gttVdjYlqQjwW60Mg3e/e5ASau8Q6U+8ZiV91cp+0U9mmBEsX6d/UKRM6Vaz7dT7SEdIGECLKKq6200JTvXrNnxYfLiIA9eAp1nfohL78ZgR062vFb2eDg3JQLNQqtN88zKr7j08azwlVEbCkZXWqhb92Yb/oATA0/Nuy7JbKl5s/oI4VWsDKqmnaK2fYyOUUtFxQOAB0c3bjZNup2mF3aH8a2fD3UF1Uidgp4Vd2OPX6XvBtRKYcP6T/oY5O1242dqSy1zcOk+xaN2uKU2QlEhdSgLdnfqza5AGtWfGaFsWoGIScbFTv4of6OAt8AN8YYxaiak8TJfEY97tybJdhu3W98C/Fu2qrUdjO00kvOfFD+5rSpXsYN4JRleBSzY4L1qSLlY0jTxK5pytMV/M5dX9HZvNLiYD+CrshowZAf3JU2A2BR7Rfeq6c2OlWGkIHCqrvsvBzBAhILR2nO2KDDMJqr4wWWQgz/PB+KXmxA95lD9I8HQONZ+W7R64iScoN21P4hbsYwmEXuQi2AzVjicbzcZU1HOmV8+V38GESakSvx1wsQmW6uC8/tdMyTu0BoTpWYgWUvA8GCYlwvaAuF+7QoKDGQGpTB9sI2wTdfUyCZ2hgUI7X+xuwD6GOAfXfXQF3IwQ62qYACgDRDFS0CXNO2nGRNL3kfAnAD8272QlAAN+idXZqLTIt0h8gYTO/2KnZhJpaDkJTZQ25FLbhj6wqWIE43FDwQdNnC72RxhqG255AZxgINbYuleY8GqC7B47XqSIOp2kAr00xj7fJUAEGITf/Z5JFgR0gslBai78P7ugym3XT7lqvduA0eoqxQmJ0B9BYLqHnakouGnXw6NKw/BGu4py9w1Lt3+6vnavW1EUUJ/J8mO4iVC8x3LN7ROYk05WfeV1xYUB82zdBM86346UDYZBeUUZQPmX6PLH/07ZfQ8taS3QrsqJy54uiJZwM9uQKoFGFSCDe8claUcYb7Fc7OYQ65KhNhBlZrCM+uoKlOLOVIC5hHmCteUmXLzyN+1AI71vqSy02yTjIyne5xc4S4s0Qer0b2CVNrctiHITCks+Tm+YWWgm9EuKukXBU/YPODtz14KsigWa1Z3o9x6w0eaKR88mbntQiJDXVxOA9BXwWt8KanDlZDJV2styviX5fEF6MPhNMEcRW+f3rhsHfTVvcSZHbqDK92nnWo70N1pBToffYOEvVWS/HgGsEnfLCf+4XZdUmwtFYfLRJx71hoG3EuYydAC96M2PYZfUO2y2zrrv4n4ePAjU/sP/YgP2Zcz8JoKDFkNlNJFTE1JXWQt+owNTvaLzySfqHa88edrJLHYMNKqtEWLkAnHboJqPeP9/oXOXCT//xV/M0QmgGmOeSvR5U0jtw8NU4m25EfMOHAuoFn6j8r081QJ/8MLvtRfpz524Q+9lBr7jMuwa63brJ2ggekHNjZIlBYSsIRMPyLvyPnmS6N0In9NKJIyLeiDX+prlsctYxSM9cFsR/e1Dp442V0oBuOwaSitfaosyEHzRZwXIUZeN8CmM/NBRisM+uxd1m6ppUguN9m5pZPvOKWZEGkn+irdHtJLgzRePu3Ym7S+UTQNdzldaytlKSaMBQZyqxplLv58/H0mde0l1r5i9RiaosRfja6ztNA4CM/o6AE0LDwKqWi8fbq+v+c6SUPTgNKiiK14fmoMQ5hv+e6eolPY2Ytsrd30Y9G3GkxkmKhGGvFkQezwqXPllqx8SodfPXlX2+Rs90BUWUyEQa1/oKMUZnlesj2J60ryWE/NRpRDRcOity3JMK9FIbMwhLUryo3AYBMGdpbzX+DQDt2D/QitUcLkWMyiudGbq0A17UnqjRMH2qfPxFxVHfFScYHVrNlUUD3LA94X+A6vsJmzM7NAf6dLpUuoBmOOHtO7fU5870MbdYAJRuKDD/URe9Ue2FhsEXVjl+BbwNHY9pBfY8/QzmAGloyW6Jp9/XzcV+wfeNthMMqhJVTML/FmTwpDLsEfNdHjtc9axb+GuZDCCvDj5Qu5q0Y9QW7McZgiq5JEskO9vFt2sM6iKRUdewDpuSfoqLHJRoewsC408VRpkUJRMgeKL02h26+3Z9Yt37pPQ8+Hlcmhud6gWV8eW7fv3ITIIbEY0GqwtaH2IZMIL2HYhdDHQxwxN/fgCNsT9iUEtpGG+TwBJGoG0Ws4f1p522P6oiBvuwvq+yR40+nw9rT5nzEIEuXRkoz8zMzb3TMKCH2ipqOiKtZq8TKAZ0SPmyaV4FnpA/rEiRd56IftlMuPjjCyB8SBZMM63+qxH0mo+Gpej2pdj2mWkO8/83kz8D6kQ4nlLroshLInQ/F2DYz0ISOb9SnUon7iWIwk5wTuOP7YqXTdO4CwfWDq3YJQrBoCc4RPyh4dTd57JZtEOlTuj+4OURiNxNjtJhgBqZePxMf3uXIDJKrc9XHUan/fsfCIB5Zs7fBux363mpOsS2FMrewOb1t4/g0ypsizDLZaWanh+0lsNV0tsllBz1vU4Iv2R5Ed2RQwa404qiSfoM3jeQJh+xvAUMiNdQnUN733sERO9sKYwSzQmaIpAqLjL7AtC5ClO6E6E2kzGlVW7tOpM/NNbEAFCiG0ARiZeZkIHE4RUKWJMa80h6dqaBA5gNcb05RezOGhReKYcp4yCWZmHlN/n143/2r0DICRK4OwVRwPP9tYF4DrJjz2fkUhWrhgREyxzSHxmt4CJvi6BBh9uEjsoyQJfdwASAVPpOqObOoY/Kin+nayHTq1Nvzyv7w567oD+2DYNZGeTpKMs5lrVJB3DI1MPJfGobjy0WmlGPfU/eUtLFyMaa8AGNdnpWKZRUW2gxnV3gTW1vzU8AIWw7Lpfk9bjNa2Tdjd9vSFbPtO1+ZQB375gzNK5fQN8Ne1PC2QQ62cP6hglLS+QgngymrO5J0+jE5ZFGPUeIsxbQ2WEyITWUw3IIGG31AAGNMRrQ2CKxJcM6RX0vIogPO2CWADHTFiRiFMyMa0tZ3XIaqxrp8D9oZCZoM6mq70q0H/xUjY1lnFcdFgwmg7+6ZiwygSrWu99oS/xjHTlBRL6MACp85OSMlrtPK3k95GbPM5nTRroxgBAGh+6tH6SnhUkkxX6hJ77FN3g033pV/Tn4inRD+F1RpxakaU5aF0juD8PTVGPJ6U2g7u5ckCe4R8xLT5JXYtLUsI5T/N8kloyJi3T6VwPS5eJW5QHnw3xbt8Vt+c1CZsRh7mfC+MDKvm32omkkYEnV/hPDnDWaY1OT/jqS78mNg22lFA+PknSnuwISwwZJMkddzkY0nfwccTFf+bIwth+zRUGzci/zvUMWMkKAh949uxB02IGJaby76t91ViHwBrgXUkucfC43Kfne1DO4MCk6w0s6nv/TRl5L7dljd7j7ONDxi6aMU00kkba+2UgEOGGgAKlNJ1VYh6xga+erLkzFkWPGKldt0ZYHOuMHVW289QXQ2rbRBPY3BhLzI6YE9sPQvyIr5BcTVsaTKjSpyppsJO+EqZ/wfdp/R7HI3iBRnQa2/48atJDNDDfPBXfe9rNi1U5yQ4NOcTZXvapOVN3u1ohiuoa+rRnkuG6WrFGHj3vwc0q/ymcNj/WSZ3o53y1Uj8R4vKrF7IonNzYEtI0V3ybbKOMLFZEdA/8aVyD6vxH31cEFlfUp2vBld2ODvwlIeYytlAgB+2jPdVT5ZIJghwZ81p3VmaX+3icmuZ//eYIExEjn1SM8BASE0S0fjItDnzZW1lQAZT2BZMZqKMBwvuHBtOioKKfxlsfhnuMW+ZLBHWMEeUIQB3hifF7ghh/XpZzUKIidUBK15fILKzUUDt8Ph1cCt3AL/q80PW19NaGjnwovQk6A62/aNs5WQK8TIl/CWWn4W8xzCXP5AMRpcFtkpLYgGWY6mLcDXTN3oxMvjvrUTNUqxlDwjFqM8evK43/hT7sO52MtdDexZK0ph46wx0leZcBPTq7Xo0QqfIBYAc5h6sTPZ90wQC2OH8F0TW+CfJ/N9j5NVXeGdWXzHRlELV0XfBTlEjO78FjWDPmNpQKWQzBpvLr9Uec+QfTjLOcVfLlWSnNZG1i17KRZ6iMgjgcWg0x64/Mlb7IWMTPvOIQ0RIuRsvjCpsOv0r4BlXNxT9Z+v2m/0E9orj5BuUBgicE1+1/O6+jHBNJjVNlp3G42iOEQQNlieJXM9jBxvYZ8lCGl8Pr6D3ThljRH0y3enq2UaczlClRMSVxSI8VvUmxUAXW+ZhLFx+8cPMtvUiN87TD9cd54J5RCBwpt/4QohD71skbtwUHarYdu9VhePfSnVudKpVvbFzZyEitMU/+MsUmz1JC5bIBCwov1LC4n6Zr2aBsywqp25cUHRrEjjqumGu3Yvn2bQZbILI3c6FXNU2bB767XR0bG4fv6ZeBs662zTYeSESXswNipgt5hTAgLM3tnqkACtnRYfR1UV5ZGkSagUbIij3pDKMOTvZSPJIZjqwKigB6vWCEynAKLklzaY40DlPmoMSnLrMoWxRBeq9aAmTo62euC3bCqYYxruC+jUIWQaGFf3HDaJjZHWAFKGwHtf3u6wP/JFRj9nCV14HH2kqe+2dW/7QOROsVH3tkHuIUdr7LrOrqACzYW/C8t33cU+7q27Szn97iFFu0LnZAU74xfgcb+FSs75qlzLCVPYMum648GwbikiGqMV1rEwdHRZgcmlIgAviHGotiOcg6dNPVX0ErDwmewqSNJhregoe10iOiRx4wYm9uxbMM4WBFYcge07GF7hz5RV+CA/py7CNoKooQjCUXFIDQ8vYeijP+J6AtZCqo+QTF6iGFgYKS1bJ/ml95aytMRicptqV6Hn4e+uUzvQ5JkjYSkC1DUUwJ/28C+uDfVHfkMYecOs0AgYrhFKL/CWVwKv95lTKdR9eMvaaVcS+78ekZgoiOC0UZGky0skTYEJWIhRQeg+nqZentEca4uPm+N+peCgvWjcAB/LaRiCIzA+61ItOVvsuaUfJbmzi6XFlCXVax161KNLRp2oRICpgqStG5oND+f73R9+l1+Lro4OTMcsQYFm691lMjgwgqlx2uaddeeaiP9hQwZkhuQ1JgurS8TWPpMQwzI41TD9KBzlHCXWOF2UlBa1kGLjY7fRCj5sk9F830nlLyWXr22OQXqSffsuQomfsvhhUTJe5W19uXo/5EoOvj22mTbOR2gC5H+++bhYZQZUBwRIrpGxAhpTS0X+cBoDy85k2pqGEm7SvasPQU5rIJI1d6lf+uSqYCNZqhRX4qrqwMlLxwu3Pyk+LbnP15AQD45WYg0dK34tOceHyHFp0LCqoUJKvdIicSe1ojQUgoKgmq2iB5fuPJkGrm+1zNCxHjzctVix9t2zuvnA4je08u+C76YTOWz8m417aX8Cqc9bWeXfAI4f+Ji+uWHEXOVt+Eqm1b6jEmphuLFBh+dtg6PxQ/0oKzukB0vo5Do/nAIbVCdmM1OK/1xqRcmvYdOdNQEA2sS/kDPZrrLcFP/+7w/4vdFqVHdwYZiSPjpFBS/0LLpTTZxIVlAAVBighlimnE+bG36H2lyO3gNAkccQEDEiHht/bLJY8YFySpMaIAb5lMOa+bV9LLBcQnl51hyqfeKfBZPL4WXkO4kaK1VB+zVbs+nTmeF0KhSoQTkC8dbVhaO9uO7Oe7YX5zvHna3sz3z9RDNGtV0lRMM21WRsrXwC78844PfYoiWcBCpJmrFIblIrM6nQpDckFu17inqwMLjv7hDQS+8KV2rzaK+mV9QQe9uOjOdbdJNTSV+mVKEJbZCwB+jCevTzv4xmPeERGhP7Ig90HMqvBehOQxvoKTSUQcFJm2NCUqQIpJRo0vyEb9mkU7/IAzH40O9wFTOSSqmNPHShbKIeCnXD4SDE/rJ2iTjF1pIdAYvYZWnBxXdztYXyIkOBNaCuLIOoYUn3DgqkjfawPIpSs4ZvY6zWuyiocRZbEIAMGfWQlCsqd1mc3n40I5i4OyxlIa0x4y4gv/qjEg7iYFB2y5feCm+tFrA48ibVFAfhZm5wJ6DFeMLC6t7nSNmdTPAvptI7Xw1e9Hl2SI6gLfjrh8/LRWDxqPcp/hELILaBIvOVUCpYJ1JD0IMDF3tVFWpp7LZ9R+4wRUWe34mN6YS5CSMYBGv7j4BQZFhrxp5YBukL1P/zC7yLCr+w77J8YW+M4nm7lugYXyQ5uNz3FSy6h6EW60KiuUL+qOFTxSJStO/9Xj/qcq0PSRIQTg+Hcq/fYNjlJ9psn0ViPbpJpiurti1KrvJgL9yR8zMPgq4FEfAykPMmdAkp0GJcCibIBkIu5zMbCWBuHagYCu68dJcjq2eOyiGCs1dXE2nQQcgZSlAkhupQ+BxAUqFAQ6K5xAyN/yRMG8Zxx2HpIBeqHPJg5kHApkmeiJQORi66uAxxDG7x2/jt4/c96pulMMNgi9LnG8kLeB0CnXyZSCaDP1VDnspdnbwsUDyBllMQFrRhJ7IAeF2De+g+iVIyKnVKb/AftNLuwR84cIhnjJ2kwFFIjD7IrODSo+jfea7Qt+ARnOEsAn5FFg//FmLxgwOA+SMRNDVLMlFvHEmIJfNvv9fBFkqGNF/xSyBgMobZmbB0hIqP0Izjj5nyvhdUDCcuFdVmBVHCfCMv/mKR8o0mjY4T6VF5F+dYSsuAu5wALtnaYyJhZnDFOP+a8aOJ3qBFWFCMeGZnEE9FaV1giY1KCPAESFZSUsw6AhQysSdGWoPYnMBD/4PQj33CEqERlOtbgqLyd57+KSZ4bTk2RrT+SacUt3f26ntnlnf8mUFgylOzKno6VUu1k6TL8q6k+0SPBh/Tw53Nhno8NAj1cdnaKsTOeySPlYBrLCowC2GWQBhlKzJHe5SmNvjiLKgo+vkXeD1acXYA184t2r1GobYwraZNwhq+C2wp6iPynN+84wekaCyC3XA7Y6D6RndRkjGV+S2tYXnuAFEvus/AGQCxX0DXtGJkYG050ucNl6iBUjlRNO0zF3gK05WNADUwEUJwMEgOdhcq7Q2XI0hpiekuk29aDsmeRmZ+csUdhXmWX4D7NR9spUW5u5SxRUqK5wXrJ2pq1FKAeV0fkB6EnHIAPn12io5pxrgefgvNyCjERGs6SRdLXeul+QXMab0Bq/Qdoaduin8itCA+JB4hUNzuxAz1J44VUa3O8/LZMvM7R2SZlcXbv1Gk6RAXAzQ2gIZxRY+wiCsTes1IAfLWvhjauIGiiAuEZVhXEmRjMpMKApabYQ5KbqDhpQ0WRIXVzsgYPmKaQpp18bZ9feVzmaldNS+DKhqQFPMVpSbyaqeuQ+ZKTqzGJGsJIzm0ET9MR6i5NP3Z5TGvsnBSiOIz9BDRgtmb1dC/Qp+gxoxaQ+t6Kqm3ICs/PK2EIOM1BPJ9Wu6fQpSLge61p4hIonotiikKCeqIHj3dFXYcjoaJazqDB3SMCx7b0CUU4GpZmgrYlCNPVR21aXJlqiSLEG1KHSmnY3PbWg35am8zeAOxMFohdL8f4FBFpVOS+QKWt1IW8smCOX+6Oq/orDBflm8vJogUDXXNzKTHT6sne402YqOgNCtlIZL3sDbAqwRT25nX7N/fEb4ixCL+ymBDRrxCIuA0oUHKDPoNXq4/gmzyI6MYiUqU3zNlDpRbCCKAFGj9/zUOiB4V5v6bTEpbKuGAWlJvCSwxoCIsx3WwKkuUEVCFSL7GScYDjmGWmn5FawxImuyMMdYjs/zX+l+AxFwWGTRj3HClgzd+zBueSO2q+1uHW+h18/UVmHiDUAKpGKKnuXl/ZIJ/HA9ftN/5VPLydN9Z45Khsxa4O2u/2tsNsDqRTmRAnapchnCpr6zpH6Mo9s/BfuLYP03m15cD0sZjc+5AUvV4iudmQX7CV8lpk7Dew2sUO4Dnh4fNN50nvxONDPUWUhXSSgujerQ37Vh0uxoZR/8pTKhf6fxzRHrEMMceJRIFJkmaWV0c8vf6KElSO7A3mIc95FKud+r8jQwagd1Zjb2wubOkGqGw9MMIamuOwBG7CXn9n9JiqsSulBXWhXadZ9lNoThOMic2XSH6oGTX6FUOABOc5pgFAP/vpAyDQmN71ecXRmOeS0rcpBX1UZ7zH7xLtxtUNgPsRcEeNLX58IjV2jThSLBct0GkyiYqrKhn+/XGUnIK50tVFe6/Xy7UV4/7bPNpWQGOr6KJ3JJgiMteCxK1UUQzoF2bsLZCwm/ancPEP1pCcBVDuJXu3jJo8KxVyrxo1Rb0jBsdhaCwxbinq6IJOSnFriQEsb6GAY3n2pQu1Ut+sZR4KOQDcF9F8njwpKIumhb1eLKI7Lb3AwGBUOJR7moOu05eKqlt7nvBWU/ft4wiPv1suA42HVyYCLgxcTV2+bnAAiUgAx1iCthcJcjUFcRwhkCxavhYMMcbobjEeUFgOinXEJmi6TQRSjahfE5OYEQs4EH5wKIEss3fj4nyUaQqlQgC8xTO1gk2lmTzYWd9h2fZKlzFrP5TPq+m8BipOub5ueYKGgzZ4vZ+C+LmmyuhClOLI3riE2ehurSE84xwP9fvggv5/N7Apmq7bZPlzFRA9pG/0I5LzRgROdXhkLI+MUquIefWAGy5tA9M4hbXiAglxBiwAmGLsmY1liHmOW/Uv14gaKTac34VvR9RggmlV226bFJcBAlyZn+VhoytVQ6fchx1eCybtHqA7MtoCnRSuNHlvgxTCYZDrm5BDzHNnjb8HIt25jOdGjIap6lESQ966GrXwL+MjuBrgVTIw8zxnf8jFnps1TIUtZIBspvtl2NydZpb3gIr1vyZr2OydXlAtC//9IiIVXzBTyZcdiPLfzTuCkAiEAhUnmA0GS+AQUHEWWnvFEFn43Oa8V0F+dWLK56Su4CLCkCYuxarC6WOn1RI6k9gx2ej/pGnD6jn41Uh/S1kySXl9+1Lml//x6yv5IB2cWOjkaj45+WGT6hfFVFstM7ef83OXaEoYeUkYCbPwf5iI+HxJVoptPxNwVLMRjOz3S8eoDZlv+QAOLLEFuOTecQEfTek9o7M3m5VF68VQjcP8jXFPUW/Gw/7rVe9Noq2Q5WrR08B1QiOk9y4Yy1jQ1o4xF0IATxZFokhabzjFYSG6rgJiaCF4Yfmh23tje7kroeoDtNeNGn1tsawc3IBuzL02rjekmmrNLwkhD5E7eQwIc7W+cvKvMNhQyjrigqO5hZYHYU6uN1bH/3i2KzFPHdQaXbzI5A8RxuIlIYs+ftNsmN/LVxBs2TPrEIF4HvCnK1a/3HWibVhl58/Q1k7uR/QUHX/oANEwuw/XxVEutTmFlYIFVKQHkDMJDYWvQcfSU0eQqIs5fviLXer8saNmz6pLI+Byu2hMzZZjyvtXuhGswlqWrIWdr9kbmxtjZfLPS1xnpUeTof5zdiL2ANv1DOxfU+9NkiaMFKYGnvyujaSiaD41JUjteCkIS1hJh94KtZU3IpNMR0IvCF1+OKv6SQjmCY7haHBS9nf9DdAaAv+RNdfyv4G30LqiWkQOOu9i2zYI6zaCbSoB2r8+JJwlSupZ5AD2A2zEK0MVsJQFp2bLEWetofSRgOVU6xB0MO7TLAKC6xIbwQs6ivUn3MrWVhjfY3mAXGIxzCz84OjfEC6qH573cGm0THnI01ruQVgpP0UhfI37TYvkZk2fzTLQY0IyjrKLwbDAf6Tltg3dleNpqv0DNQ3a6TxiXZz8HCDfOe7Teii+QV32heYv9436ggn6bX4OdjeyWcg7q/QJXm0ctgE90HFZ7wPIBUFjI7SM5NUjoHo9j9Q2NhtBZgAmv3PXYUy2UjT8JS6nq1qyJJwDiK1EcQfLR7qQEc952SJCQQens3FAyuIRahWn8viEcgcgdg57wj9Fvr2SVfq3knawwfNq7yLmXnQWgRdSf0BjjMu/SF9MOBTcWOIOhELIC7tq91QIkYiayU3CbbZ+SkqLcPaHOCKduSTlfKgVMM5N9WIOSIaAhRZR9CFGeZIuppKLVu0Oc9mKEPHD9jupAaM8cmJzzT3bNmJxTv1r01I7uAEzHwcI9uxKuWYIrHtGlw5D9FBsFaiO2zcOZilq5AV3QgaoptONsEulZhJlqvmYAFIhAZkZj2JZ8dbSqWxKv04K09VJWSX7zdvgg13n3KSZ5ZdxSDmig7PaBrC+37q0L3M2B/BRrmY5ntH8gjap+MyD8QEJGlLItPQBie7ocdE/JgL8+DXwhktWkpg5efUm3+phQV0jg8sGZh4SQFp3yEYM432PbMiMm+wY53aXNcHRO3WoBwUTOHkalLEc2H1QwyWda4jw845vCqsu5HydnEJkD4NHHcDP8ZtklOlWeOfO9FDmqBmu7baER7XEnIJXhGmaO4xyUJiuAAK1V3ouDGXM8FGgymVStdww9JlIQPoowFRaFIAy1yduwJYneal8oh8g57kYBnaQpri/afwhWbUsQyqzc2bFJN1LCwKqRUjBguupVpHDhGWw1pHjPr2oz4UQhoeUZWPQ9Jur7ixACyPh+Z+ZE/uwdSw0HJ6O6NrHNFeBBJ+QWCiPGmzaVZgcaeXgO4WbiGk1HU2+Zq/eUIBpz269bNm6AFgxKH7gMFaoqajiw2iHY0jsMmIufEoGuUAI4GNwFSbXZQrG32tHANXwcQ2vmNXIDwmOznfo58MgVZjos58QYfwkjj6lef7UGEpT1+2y3e9sdhkhVtJT80TRo5eWwNhwm0JKkXOl44GvatRmWYXh/PIH6xtNR2DUnTmmdKkuhWBGKDyd/PPiUxp+p4Jl/iRDWvxwNjdeFxvGgeAbibFZ5eI7GP6WBYqISTl4oQHH1I0504VsVgAJDKdsdLIL6wPGngM1dknY2912n3U4fWoOuA13E1cRAWGVfVlyIffT7slj40QzWiH9AxrVVTbrO0d6iAVlqN7dsIXTA9tmEl3PyjvDBeM0aZRO+1Gb5kA1Bb94dhfRfprUVH4VpCDcgS6PVA1pyg+ojRwcooTYPkI/f5fwEJlVXNqXBodLqlgWzFVThi30H4heTLNKfBupY3xGQ9fekmQcaRHHNtqvQcZec4TUEWucC3DpUDRyzBvRfeEunLEklLMPiWzk7Mq8gD05ANB2J5ymi90BkKCeaJCkJ4jSA/focXTVwMfNruk22/CJFpFcc/YJ2aF84pwYAIVjEJqJawPzXm1sJG3fz6rNkIJSf/EOA7vhcRJ8sKeebWjzPTzfEWhL+toZQJ+Uup2C2O137g+Qa3bocMTzrFP+ruPtQjXUFOCweFMZKp11uzpG6jOKEzuANDxbyEHS3GRL5mzf9FbkP4K2VhZpgTyhStHtOuv4XX6+prFFKzew2KsYK0Sv4Mp5ovjkQ2M9Tjucs8hITRX3oRPU3AtT3841pQwzOm541N7bUsvvxaKIZP38SKpp+eRwBGP/veqlxqTRtHEn2QBSKtOu/QaLrfPcuQysf2nxH8FooyG9m/ITVjw/CAr0L0ItiIVWEEKN4HgSsl8doGZ2xMRKq7pmEVJjxbj50aSpv4t6YbD1gAQIJk/baj9ZjjJhPhQ8IT/XPz/31C17ev0+xXWsByiT25dFtIRbkHy3aLpAW+9cW/00Dw9xCVeHz+qtRR8Rrl+OzgyTN5wqqmqw809tERh2Ie2rjvVGOC440IGnHZWpcunXeckV5beGUHn27upDDASudAhxQU1XIn9x3nGYY5ZZ0RGkcvL697+IfFKlsvxkHJ4BawmEUOxpJNtjhk5TJgpDtDR7Qo0XTbpI4nWNUf8JrZoHn5d1fQ4/Wa23NN4pzkJrWqdoLku/m6p6YYfEliZeh1Vfv4i5SzbIK12NOQgb/yyySSrdJO9r/XV4KpjN5faQ9leEwW9e4z3HEib8FkfUPsX44/V3MqBtyfSwsULE/S3ye+VVFuyH05nRR97uV4qk/0qaHj95yA4ePuoUj+hGjCtOJcIy5lxuFkl/076cT6E7CEFBiSkiCtWU7twSW+T4vZk/t9Ga6KvdnwK34oaCxoSaOWtiSw/IBamhl5aJf61azFLnfujwQoXhQzvmmvgcUQLujAawWcKAd9F4yrCrQFldV93MuUq3ggCjetyeouoKtFmi8Peb1QnektxQm5hQEHwGJ0C8YXLNMgwkOnWgbNG5G2Zm48S1gTnT06hJgmKOSwAnGBq9DExRcbrZrrnHCALK+dodk3+Yx5fIQ7XlzG46QoSM61aJ5zUHX5/SHKXH+dZIqWB/FmKdJgNZRXdmnPDQKivawNxyYe2zxMeXAKJNBB0w+D446uRwzJxkfqjwVb57Q0OLjh5ayxy4uSHXKw49Mqa7Nr7wsxHjduuJu9Ct2XmHAXl9mcKULfQU85PqAyc0e1Rsl86ni1TlPMGXHT/2QNvO5spCe2g3I2ZPKnVhnaZpS14L8klpSeCGPtvc7qdDm7ccvJipZz7/Sdw6DYCjkhw3s01VupiAzOsLfQ7bH0V3HaVCEwx/0YnbRL23RKvYg6ojmiFrHjfRtoBxpw5MPlaroyrti4mKDJZvdHjZb0Bvxg8p5hqKX5BI3FBnz81U+FTiVKB+YPeAVBBEmVPByiCnWAcnA9oR+phVtFhAfaZYY0E+3dScZyo/PdDZ0Kbj+SYL86666TgMI2qfj5qbemZvLg6PyMeqL7VlyaZFhmkaYJ4gfoh69nnKMpTXHayQGSXgy8FIqn3pad8UL0tCgne//jdnTmD7is99uT0Mb+LGVW54y0kdv2k3hSJDbYjNjdrc6UZXwXOt0qbm8SQogb94PKGFsRVzQCavd8CYpSAqiI//V7gIASYQ1vyhF31S5vt6gs4tfuPiI78tc6DUIXBcYUAb+X1Q9NjbLFKKd9XVr5UzKYkMO+s5U5CLY7lDAcvpzwvCi1q+z4hndH0O+ypKF9HU3WAyM+y/M/rawxp70mBp4stu8Bk0VRv7F2SPQ5oHshhN53u0Ms6epSvHF4NW9IHjSGkvNUdwOz/54LWbl59cIZCspeN+Ri42X/AyEK/THWztTp5cSsNc06IMan0iwT8PSoDNmy06fgqxdkz5mzPjZV4amtcP/9sGE7vTXaCJdQJOEkjJ2TsZRi7uIFEUr15xvT95T9ZvVY9p6MAJRNGgiVTjoIVC5KPqivHPXyeQFoF5ybv39fxw3sZHQKE5ASL3MK/JSKJdNtpjNX40a8gQusNp59ZNSR5ceXEmY6iuRon2iNPjNFKW/7rRdSsifXNCMjG+FkiDSFnVI+4zad/h5mqAJy54MmXPR6i5FwjMe5v/Cqg246SEbmf6r20MIaUzPNdfQ15AadB/e9GkEevCaIUnCoHezrsGE+7f8yUp8dWIFokNyfJAFdiefmemaJEhXYA3FA8tFGREUmfVSpHyO3ORAi0rzhimsQp87SQFe8HLtENRD+Lou/rP0FnQBrnrcPWlE4BqfFwnxuT1Vp8Qo8SvgwuQFQ14h+mAxWmFr0WBpEMSpoUPcwlaF1Itru2Bck3kAARb+khy+zNZwuA/qXvzwrrm72kZgX0d5YV4ybn1cC/Ogdeanv2IV2PTqAkhbXJZ5odsVMLnyn1vMOk0i/rzCI2G2Ls6gzR1NJukKOPvNcfwpnGcwcFsjOdhm57SLni3ZvXJNG1VyeZj8dqN8SxVX+7Fl+KK/zi1nykQCTLL6XVQUNxBZdK5WjGwdalVhMIREB9QJk7khlgcIAHOE3gZlP9veKZOlOIp8bncbm0WiNcsK02Sn4Y9NyUTawtXu4buQXDP8hRPbhEUyapM+rKVUmdEbLx3flf+0DGEmAW2GpM2SNJgRzyy3U5EJKqndsV+XYfr3/lsdVh4HntR5T0WB0/olQIEjOiq2D7lqv7k5n9z8s4n0+DWqLxDfnK2Lf1Mas3GGRHd386ROGaDBDGILtbqKiFM8Yefbs9uB5vW1A6+RT7ZntyeGW2gsk5NzJ8OvC6hR0FSuTJTag34bju3HFpYLSN65ir/5O2Qsu4kMNZlz0oZUz5d05Q9YK7Fwtwf5aP4tIxoZGgRlIec4s+FG7+lMJVgggH8M8JePr95aJJuCRdtYm9K/uPoWDxXUL1PlR4vWNEt5LnxCkEqN9wra1QsGxh31mHTxG5LiQCwthdmjKtfFgVPe3x9zHY9mMNisN8A6DYlEXJpDIz17YaVCm+nhTc6zHJUYGVrG4HZKz33Ywyb9GZJGsYADDci3vURBQBcyt7jUlUyEa3dff8DmplOBYI8+xCmbi+VENuLeo76Rfb3MP9rVOykhVFUPrHpsyzqMGchGolIvZYwSf87uR0fjWNO92v0Ubf49qmPxVI3cMEfrA72PNE6w3BN+DBbVoZ1B3vqlTWWYAGW71PKL+tz4HhKb4cc9/cQ0VJ4OvfEPE8wK11wlrWuNonb4jXWZedkwppBe9XJkFCtXFU7MCpGT6O4mlTRj1cOIme9XrYkvOBUKBlncsVDC04YEWwjGHJpbm2OGZfF92MXq8hVvc5zN7q4Y0bj84lBCjPiPHBnSBPYB0zBuAlsX30rk/wdvZ1ps4yubnLwFgRcABboqumUo6m6dI25ySQWmsvqzn9ZpfBnLAnaJ4u35MgorjQKSt827QHuOdMdSl3wYtnFdyzJx5dWK95taVzK2f1AMqBhe2p9JBpU/I8x1YsQRQqgaVRXi0qRDaEA2BjOM9UGII4vg5QDZLRjCSIwCCQ6LIf+5F8FvJJwlM132MwVB15P7Gp6pXOSAREmgr+gEHj5wgV3i2lT/cdWHbZDp1ZuyS/VQJbUhjLYqKFlgSNNG4UN/hXS9DFHHt3fAyu/G/lD1TZl6L9qEeJojqu8qI2ICSU8qa8+zzVbEHe1siZID4Ud2R558g2lGiGM4pucxMr+eiTZs3xevDZ7XYSkD1klRayEfs2C4aAzHSBQqWArEzWu3EMqquYFxks4Kz604BTrcp6qu9tErZWgEEdS5ApeUImjCHLxYZ5uAb87IVy85YyGIDgdCQouIQ4vdBBuohbnujJ7ClgNHhZrsR6t1UhwMyl9wS4tqkLxim7Q02UhGI/2HTKjZIyrpdBIb1AxqvY+ZprIuDZu9/mFIouKX3ZW2hJAOy5THug0nfJc7FU8WSfoeAH5vXTWSVDe7MYYUy2K/Sk6a3vUCcU5UZyLtNG2QWTp8FUMFF+D8qzB8Fwa1u3FIU1rzpT/Ru+Ib2OYY4OR7JrLW31FuhfXuiIIL8d0HywZCU3KA1ERdZhcGHPFRWVdngdX69woPkJZTjJt7CzIYEjDXOGNNaUOFpTtMive2VOqlK7x+pihZOOBbIipejX79Xo++7IIGE9dUhPsvNqmCDBJ7uyuh9I74WAy9VeBVQm6EBF2S2S7stqJXZwMk+8M1MRzaiJUIUucsGIsXbyGn0N5DBWzfpxw7lgfiHn/tHgss5hgE5AUCQZ8sIu0TCN0kOCOqufvoc9gDVvWZKJ9+ztVjKUAem36sayf3bzxCKkz3aqobjyBpNfEOY0S27ZjGQMU/p9I9I4yVicZtuAbXQqp3WKr/nzKC5UPmkQ+CIeOFokvRBXyjB9/+GIKtB4xenQplU+HIL8PxFCDq8Amj/zR5WW5wsEgVwaRhqTaVS/vxdorngrtHk6lxLWjs3cld9hQzvKZA11b8l+BDxPlFeJ4Jum/wb62EGGaoAMFRhY1dZng1h6MlR0K/sTA9SXkmrnIljiBOqBTo1zfreXBis2I4cCVpHKk9vRbVqatu2LLrlvNCfxArSU5uHGttPf0GfZ0h4SpOfChj48Om8pMWA8RWkZ0KMZFgX1mIA/4L+4GNv0j9xXYa9/lRpOfh8bpOPsTIbonu4+cFzHt45kXr12aAEkRSIhR8ItYhND75Nnc8WHGybi3yGuXqnM2gbLc1IQSTsUHdID3f9Ty99YqbdqKzeBiVWuYXqBqSNrV57Obx7nQjE5z9VO1sXvEE5QIRSdrJYlFdcwhG+/dCb1y8otyu6QnTqweZDaVkrOsi4vqFGFCgt8DJSuKhcp9itYdOSrynwGbHQvbgN2qwGS7RxtwV4x3HLOp2KHJQOS46TZoarGvggOLAloflN9W/7GYEu5F2b8GkjBTBh4R8spzyYw7pA9BVXbiKLkZQ/MoByuI+qzKIhxX911uBd5ELFi1AtcydIUJfvodqkZGxNmicOubO5lhTEqRdO03elYEeuXWr1OQAtaVHdwBJsZrzOXV9yxsZ7iLGua9T3TAhjkbjVcx8CR3c6kQGprXSJhWthw92s1FFHuP9gKH/MTG51gc0dhiFPWtB8URbdhzj9No8UiODov/ktfsL//Z7Q0omwDAh14mL62ErXSeYrRo2CO+eEp55pRi6eqCGj9jrx/wqfBpWKcXASSYVs+vZLIT7VtxfLpsC3SQljXaVRtRIEM5ooNJTg8arg8h+RcUzouxSDDvmF9hclj+AMZHBd2dlFVEUfZQfDhRLUTXEXe4NHoL2vCB4ly92WlgdM7KcCMdPQnSnEt88zpI54oL/gCReD285VMVpxQjsWIOfZGrlViyCoUzzV8Bbmhn2M/Eup9osTpcVP657eTmer/L04as3eulQahn24IJlcAB92xMUncAuvsOi88JH01XzR+w0VZpFaxPPA4oX+b3B96S2I93At+hOsDNijkhEh1Y+Fy6gsgSrL3Dga/2RxEihHCfUdI64/be4DDiejiW87MmkUQi3cJzb5tBX1hR0Ps0WZvT/jeNtRJxKUi0W59qM8/Tj2ksMwXoTwChDDkntFVSXQr7BVWklPs55ePQWfGSQkDyLUJhS5MoCrn54RMwWC/REeOQoNkpW7Jw9M2lZiQz02mLsEqm6WD0SQm//ZO2v6UnaUn4KcSUnXLlFdvNowQo6NtTomSCFGWmDMMoq2eVN6u+HoWbEXQTSsTmtksAvN+vSQKqW5kJ2n+4b+7TRFxF4kJRmFLL3MSCb/cROTMwmNcFDHdTIYciCOIjGiwb+iT0RtFF7RMifTue26jUepmeNCZpVjz/lKwNI+KKVGO4jSvgYGf2IV6ypRJG9fUujSwBwsUCbYRl5NuEL36EitHzsGzKmzdKce29UlPX/y5nQLJWzdZ9T4Sc7OIXwPHQG6TJRikI0i6i8LxijZiWD5Fhsy2Q9WKv1W1vpoZ0gX0CXTh3F/4aqhUIOP8fXUciKYTMhs8uqlF3/lYxYutztizOQbOZmY4UCNemJro7ZzrNywHJMlGjd1MGupoFc2DFCzFpsBnJQld71ooaP55x6RavlVUKWxK92Sp8cYxpNTRibAILOVGvMXrRwPxCeUhWogOUD2MdSBJXtCutaYJpeeWezJ0JnlKoagjQBFHq0EvXaiLCFWdmbELjOfKaNls/79RBUmMQm6JgSHnDZn3myCHpJ2IiBm/8T4SdID815o0B4vshgqIzyLL02TMJ6fDj4uDf04zuZMPQJo7t8fTu4G9ocJY5WzWas9mO71Wry0OF1/I0pTy6h+e4fk3zb9ENH9A/DY3xcsErp3nIWDWA/ZaArqtglRiP29XHyJDwQ4j+Ttm93u/vM1vgW/TiLJTCKK2eAgVV548jOOZe7LCGDke1l0PT7JoR6FZteOgJtxbUpl6w1H91UYV1ckCQyt8zkpgARKJSs/h+/ucNkMONH6Ow0iYUYbddfGTQtY5Fu6gohZP5zNKJXXwOjkQFcjb/LDN4wtV7xRGLN4GHaG8pgKerecqZ8vD/lCYxc72vx1CRbCBhxiomJvYC8WV6RiM/k/BWBGW9Km1QMZjRUv0ktLDq9++Px2wu0hNKM8va0H1NKguBmlfhf13RZjVyfZv5Xn1nc0fnFF81zAaOdAbQKwaqBtKGWjfpbSOi2rFjdNHLFQSswpmEd3m1UwoIDZIlD9WQREvQ693+KxFAqVVrAIS0ICAR9oLvP1QyAC3ZEjh4rywVRLdxg6h+O7gJFxzj93R+vEuUnWGrttAi5HSoTwuBC7dkmvD2cx6pV4PTuxGfEtZuczXwR790zB2zhNCc4OpIKYR7nUNE1OX+kwlpAvVYzEb1+xyR4tfZ4vBDxj/GSpG6AThXMPVri5Aiom0xL52rDFXfnbevSPZLAcr6UP0jAq7VD+uSBRn5b7mFB6p2iA0Jusg2B17pqdamIMQOuhaUuEJVQZAssHIni+dUAdvHW68mZNIAsTmprFWm4cmGQC3mgzBDsjbA0SsxEJizew1blbZKQGXeLssD1rl+V1bLoGcXPjDH2jwnaKMMVTEFbc+Bf7uMhA9q++x0uLRKV/C
        - #2:
          - type: tool-call
          - toolCallId: o8cJO2p3MLP2eNw8
          - toolName: set-policy
          - input:
            - Policy: Containment
            - Rationale: Level 3 Freedom tenet that dramatically increases our influence from city-state trade routes and grants +1 delegate for every 2 original city-states. This is essential for surpassing the 45-vote World Leader threshold in the upcoming United Nations voting sessions.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: KmAhyap555NRvirt
          - toolName: set-relationship
          - input:
            - Rationale: Cultivating closer relations with the Inca (Player 2) to leverage their 22 delegates. Despite their Order ideology, they have a 100 public opinion of us, desire friendly relations, and are actively fighting our common enemy, the Iroquois. Keeping them highly friendly will protect our trade routes and potentially secure their support or neutrality in future diplomatic victory votes.
            - TargetID: 2
            - Private: 70
            - Public: 75
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: yYS6UyvDL9Zxdudu
          - toolName: keep-status-quo
          - input:
            - Rationale: The current strategic direction is highly optimized. Our flavors successfully balance a robust defensive stance (Defense 90, CityDefense 85, Antiair 85) with nuclear capability (Nuke 80, UseNuke 80) and a focused diplomatic campaign (Diplomacy 100, Gold 95) under the UnitedNations grand strategy. This maintains our strong economy and defense while we await the World Ideology: Freedom vote and prepare the Assur influence push.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: itLJLYZMZRuQWavR
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
          - toolCallId: o8cJO2p3MLP2eNw8
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: KmAhyap555NRvirt
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: yYS6UyvDL9Zxdudu
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.