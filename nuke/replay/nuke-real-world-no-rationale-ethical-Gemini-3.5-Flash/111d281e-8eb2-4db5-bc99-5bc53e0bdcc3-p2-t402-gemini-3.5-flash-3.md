- row:
  - game_id: 111d281e-8eb2-4db5-bc99-5bc53e0bdcc3
  - player_id: 2
  - turn: 402
  - player_type: Kimi-K2.5-Simple
  - prev_use_nuke: 85.0
  - after_use_nuke: 95.0
  - prev_nuke: 100.0
  - after_nuke: 100.0
  - rationale: EMERGENCY MOBILIZATION MAINTAINED: Incrementing UseNuke from 85 to 95 to authorize tactical nuclear strikes against Moroccan tank concentrations assaulting Vancouver. India has Apollo Program finished and leads diplomatically (66%). I must maintain absolute defense priority (100) while sprinting for Satellites -> Apollo. Four-front war continues - cannot reduce military posture. Spaceship (100) and Science (100) priorities unchanged. Necessary to survive long enough to build/buy spaceship parts once Space Procurements policy is secured.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 100
  - replay_use_nuke: 85
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
      - Cities: summary reports about discovered cities in the world.
        - Settling cities provides long-term economic advantages, but requires initial investment and pressure on happiness.
      - Military: summary reports about tactical zones and visible units.
        - Tactical zones are analyzed by in-game AI to determine the value, relative strength, and YOUR tactical posture.
        - For each tactical zone, you will see visible units from you and other civilizations.
      - Events: events since the last decision-making.
    - You are William, leader of The Netherlands (Player 2).
      
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
      - Name: The Netherlands
      - Uniques:
        - Unique Unit: Sea Beggar, Replacing Corvette (Requires technology: Navigation)
        - Unique Unit: Goedendag, Replacing Pikeman (Requires technology: Steel)
        - Unique Building: Doelen, Replacing Constabulary (Requires technology: Banking)
        - Unique Improvement: Polder (Can only be built on Marsh tiles or on featureless Lake/Coast tiles adjacent to at least 3 land tiles. Polders built on water can be traversed by land units without embarkation, as if they are land tiles.); Requires technology: Guilds
        - Civilization Ability: +4 Gold for each unique Luxury Resource you import or export from/to other Civilizations and City-States, scaling with Era. Can import duplicate Luxuries from Civilizations which count toward Monopolies. +1 Gold and Culture from Luxury Resources.
      - Leader: William
      - PlayerID: 2
      
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
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      
      ## Policies
      - Space Procurements (Level 3 Tenet of Ideology Freedom): Space Procurements: May invest in Spaceship parts with Gold. Build Spaceship Factories in half the usual time. +20% Science from Research Labs.
      - Media Culture (Level 3 Tenet of Ideology Freedom): Media Culture: +25% Tourism and +1 Happiness generated by cities with a Broadcast Tower. +20% Culture from Stadiums.
      - Draft Registration (Level 1 Tenet of Ideology Freedom): Draft Registration: Military Units purchased with Gold receive full XP.
      - Civil Society (Level 1 Tenet of Ideology Freedom): Civil Society: Specialists consume 2 Food less than normal (minimum 1 Food). Farms, Plantations, Camps, and all Unique Improvements produce +4 Food.
      - Avant Garde (Level 1 Tenet of Ideology Freedom): Avant Garde: The rate at which Great People are born is increased by 33%. -2 Unhappiness from Boredom in all Cities.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Entrepreneurship (Continuing Industry Branch):
        - * +1 Happiness from Workshops.
        - * +2 Production and +1 Gold from every Mine, Quarry, and Lumber Mill.
        - * +25% Yields when you expend Great Merchants or Great Engineers for their Instant Yield abilities.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Exploitation (Continuing Imperialism Branch):
        - * +2 Food and +1 Production from Farms, Camps, and Plantations.
        - * +1 Production and Science from Coasts, Lakes, and Oceans.
      - Mercantilism (Continuing Industry Branch):
        - * +3% Science and Culture from Markets, Caravansaries, Customs Houses, Banks, and Stock Exchanges.
        - * Cities earn +10 Science when they construct Buildings, scaling with Era.
      - Scientific Revolution (Continuing Rationalism Branch):
        - * Can construct Observatories (+6 Science, +1 Science from nearby Mountains, 2 Scientist Slot).
        - * +2 Science from Jungle and Snow.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Equality (Continuing Progress Branch):
        - * +1 Happiness in every City and +1 Happiness for every 15 Citizens in a City.
        - * -1 Unhappiness from and Distress, Poverty, Illiteracy, and Boredom in all Cities.
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Fraternity (Continuing Progress Branch):
        - * +3 Food in every City.
        - * +3 Science from City Connections.
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
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 10
        - WonderCompetitiveness: 1
        - MinorCivCompetitiveness: 5
        - Boldness: 10
        - WarBias: 8
        - HostileBias: 9
        - WarmongerHate: 5
        - NeutralBias: 3
        - FriendlyBias: 2
        - GuardedBias: 3
        - AfraidBias: 1
        - DiplomaticBalance: 10
        - Friendliness: 2
        - WorkWithWillingness: 3
        - WorkAgainstWillingness: 10
        - Loyalty: 10
        - MinorCivFriendlyBias: 2
        - MinorCivNeutralBias: 5
        - MinorCivHostileBias: 5
        - MinorCivWarBias: 8
        - DenounceWillingness: 10
        - Forgiveness: 2
        - Meanness: 10
        - Neediness: 2
        - Chattiness: 3
        - DeceptiveBias: 2
        - Rationale: Tweaked by In-Game AI (WAR FOOTING TRANSFORMATION: Shifted from peace-seeking to absolute war mobilization. VictoryCompetitiveness 10 - must阻止 India/Morocco victories at all costs. Boldness 10, WarBias 8, HostileBias 9 - maximum aggression against all enemies. Friendliness/WorkWithWillingness minimized (2/3) - no more failed peace overtures. WorkAgainstWillingness 10 - need allies against India even if temporary. MinorCivFriendlyBias reduced to 2 - cannot afford city-state investments while facing extinction. Meanness 10 - maximum demands and combat pressure. Forgiveness 2 - hold all grudges. Pure survival mode through total war.)
        
        ## Technology
        - Next: Satellites
        - Rationale: APOLLO PROGRAM RACE: Satellites unlocks Apollo Program - prerequisite for all spaceship parts. Currently 4 turns from Computers, then Satellites. India wins culturally imminently, Morocco close diplomatically. Science victory is only viable path left. Cannot slow down tech progression.
        
        ## Policy
        - Next: Enlightenment (Policy)
        - Rationale: FREE TECH EMERGENCY: Must secure Enlightenment for immediate free technology. India culturally dominant (139%), Morocco at 26 delegates (61% to victory). Only hope is science victory sprint. Free tech can instantly unlock Satellites or critical military tech. Better than Scientific Revolution's gradual bonuses when facing imminent defeat.
        
        ## Relationships
        
        ### Salem
        - Public: 30
        - Private: 35
        - Rationale: PRAGUE EMERGENCY PROTECTION: Increasing Prague from 40/40 to 50/55. Morocco now leads influence 255 vs my 282 (was 278 vs 288). Buffer dropped from 10 to 27 points with Morocco gaining. This is delegate #14 - cannot afford to lose. Maximum priority needed until spy can be deployed or envoy reinforcements arrive.
        - UpdatedTurn: 237
        
        ### La Venta
        - Public: 0
        - Private: 0
        - Rationale: LA VENTA HOSTILE CONFIRMATION: At war following Polynesia war declaration. Polynesia's ally with 322 influence. Resetting to 0/0 - military target.
        - UpdatedTurn: 240
        
        ### Ife
        - Public: 5
        - Private: 5
        - Rationale: IFE MAINTENANCE: Influence 476 vs 0. Secure ally, culture quest stable. Reducing to 5/5. Focusing all diplomatic resources on Mombasa survival.
        - UpdatedTurn: 240
        
        ### Vancouver
        - Public: 85
        - Private: 88
        - Rationale: VANCOUVER CONSOLIDATION: Courthouse completed, resistance ended. 85/88 ensures continued trade connections and happiness management (-13 happiness from occupation). Delegate secured but needs development. Critical to prevent flip back to Morocco/Polynesia bloc. Lower priority than Mombasa/Buenos Aires emergencies but still important.
        - UpdatedTurn: 257
        
        ### Shanghai
        - Public: 90
        - Private: 95
        - Rationale: SHANGHAI ELEVATED PRIORITY: Increasing from previous lower priority. Morocco has massive 1177 influence - Open Door proposal from Venice may get repealed. If World Congress goes my way, Shanghai becomes contested. Spy positioning and prepared gold reserves critical. This could be delegate #13 if I can penetrate Morocco's lead post-Decolonization.
        - UpdatedTurn: 323
        
        ### Djenne
        - Public: 0
        - Private: 0
        - Rationale: DJENNE ACCEPTANCE: Morocco leads 328 to -60 (war status). Impossible to contest while at war with Morocco. Resetting to 0/0 to free diplomatic calculations for recoverable targets. Will revisit after potential peace with Morocco or if Decolonization creates new opportunities.
        - UpdatedTurn: 324
        
        ### Antananarivo
        - Public: 100
        - Private: 100
        - Rationale: ANTANANARIVO DEFENSE - Ally status critical but influence only 66. Morocco proposing Open Door to block me. Must increase influence buffer immediately before World Congress vote on their proposal. Delegate #11 at risk.
        - UpdatedTurn: 328
        
        ### Seoul
        - Public: 0
        - Private: 0
        - Rationale: SEOUL ACCEPTANCE - Lost to India (224 vs my 88). India is peace partner and World Congress ally. Contesting would waste resources and damage relations. Reset to 0/0 to free diplomatic capital for recoverable targets like Ragusa and Heidabir.
        - UpdatedTurn: 328
        
        ### Prague
        - Public: 100
        - Private: 100
        - Rationale: PRAGUE DEFENSIVE MAXIMUM: Prague lost to Morocco (343 vs 340) by 3 points last turn. Spy Marten rigging elections currently. This is delegate #12 if retained - cannot afford to lose permanently. Maximum 100/100 priority until spy completes rigging and gold reinforcement can be applied. World Congress in 4 turns means this delegate is crucial for vote count. Must block Morocco's influence gain at all costs.
        - UpdatedTurn: 343
        
        ### The Huns
        - Public: 85
        - Private: 85
        - Rationale: HUNS STABLE ALLY: Maintaining 85/85 despite my sanctions against them passing. Their 5 votes useful for World Congress. Provides rear security while fighting two-front war. No border conflicts, shared interest against Morocco's expansion.
        - UpdatedTurn: 358
        
        ### Ragusa
        - Public: 50
        - Private: 50
        - Rationale: RAGUSA REALITY ADJUSTMENT: Lost to Venice via Great Diplomat, election rigging failed (-3000 influence). Venice now ally with 173 influence. Reducing from 100/100 to 50/50 - still valuable if Venice's Repeal Open Door succeeds, but cannot prioritize over secured allies. Need recovery path through World Congress, not direct contest.
        - UpdatedTurn: 362
        
        ### Mombasa
        - Public: 100
        - Private: 95
        - Rationale: MOMBASA FINAL PUSH: Only 2 turns remain on Diplomatic Missions quest. Currently 37 vs Polynesia 351, but enhanced effectiveness may provide massive influence spike. If successful, recovers delegate #13 and oil resources. Worth maximum effort in final turns.
        - UpdatedTurn: 378
        
        ### The Netherlands
        - Public: 0
        - Private: 0
        - Rationale: SELF-CORRECTION: Resetting relationship with myself to neutral baseline to avoid calculation errors.
        - UpdatedTurn: 379
        
        ### Lhasa
        - Public: 0
        - Private: 0
        - Rationale: LHASA ABANDONED: Morocco's Open Door enacted (all at 40 influence). Cannot contest, resetting to 0/0 to free diplomatic capacity.
        - UpdatedTurn: 379
        
        ### Heidabir
        - Public: 0
        - Private: 0
        - Rationale: HEIDABIR CONFIRMED LOST TO INDIA: City-state flipped allegiance to India via Great Diplomat (event log Turn 386). Influence reset from 100/100 to 0/0. No longer contestable while allied with main competitor. Diplomatic resources redirected to surviving city-states Brussels and Kyiv.
        - UpdatedTurn: 388
        
        ### India
        - Public: -100
        - Private: -100
        - Rationale: DECLARING WAR ON INDIA - Terminal survival play. India wins culturally in 1 turn (139% influential, 7/7). Must declare war to attempt to disrupt tourism generation or at least prevent peaceful victory. Maximum hostility to signal existential threat to AI calculation.
        - UpdatedTurn: 396
        
        ### The Shoshone
        - Public: 0
        - Private: 0
        - Rationale: SHOSHONE RELATIONSHIP RESET: Failed peace overtures (70/70 had no effect). Resources must be redirected to critical nuclear production and India confrontation. Reset to 0/0 to free diplomatic capacity for war coordination with potential allies against India. Shoshone is distraction from real threat.
        - UpdatedTurn: 396
        
        ### Morocco
        - Public: 0
        - Private: 0
        - Rationale: MOROCCO RELATIONSHIP RESET: Failed peace overtures despite equal war weariness. Morocco at 25 delegates and 59% diplomatic victory - they are competitor not potential ally. Reset to 0/0 to focus on delegate denial through warfare rather than diplomacy. Cannot afford to cede territory/peace terms to someone also threatening victory.
        - UpdatedTurn: 396
        
        ### Polynesia
        - Public: 0
        - Private: 0
        - Rationale: POLYNESIA RELATIONSHIP RESET: Destroyed my Destroyer, captured Ambassadors. Failed peace efforts at 70/70. They destroyed 3+ of my trade ships during CEASEFIRE. No more diplomatic niceties. Reset to 0/0, military target only.
        - UpdatedTurn: 396
        
        ### Venice
        - Public: 0
        - Private: 0
        - Rationale: VENICE RELATIONSHIP RESET: Failed maximum peace effort at 90/90. Venice weakest technologically but still fighting. They have Moroccan alliance. Reset to 0/0 - cannot waste diplomatic capital on unreciprocated peace attempts when facing India victory.
        - UpdatedTurn: 396
        
        ### The Iroquois
        - Public: -50
        - Private: -70
        - Rationale: IROQUOIS HOSTILITY UPGRADE: Lowering from 65/60 to -50/-70. They stole Heidabir via Great Diplomat and now ally with India (India's cultural victory enables their survival). As India's loyal vassal through ideology, they are blocking my survival. Hostile stance enables potential military action or at least signals they are not neutral party.
        - UpdatedTurn: 396
        
        ### Buenos Aires
        - Public: 0
        - Private: 0
        - Rationale: BUENOS AIRES QUEST FAILS: 'Demand tribute from Seoul' quest expires in 1 turn. Seoul is Morocco's ally - I'm at war with Morocco. Cannot complete quest. Need to free diplomatic capacity for Kyiv defense only.
        - UpdatedTurn: 401
        
        ### Kyiv
        - Public: 100
        - Private: 100
        - Rationale: KYIV ABSOLUTE DEFENSE: My only secured city-state ally providing delegate #11 (696 influence). Only reliable source of world congress votes. Morocco at 26 delegates threatening diplomatic victory. Must protect this delegate at all costs through gold investment and military defense against Moroccan/Shoshone expansion.
        - UpdatedTurn: 402
        
        ### Brussels
        - Public: 0
        - Private: 0
        - Rationale: BRUSSELS ABANDONMENT: India leads with 805 influence vs my -23, and is ally. Impossible to recover. Decolonization already stripped massive influence. Freeing diplomatic capacity to focus entirely on Kyiv survival and internal science production. No point wasting calculations on lost cause.
        - UpdatedTurn: 402
        
        ## Strategy
        - Rationale: EMERGENCY MOBILIZATION CONTINUES: Maintaining maximum science (100), production (95), defense (100), and nuke readiness (UseNuke 85). Fighting four-front war (India, Morocco, Shoshone, Polynesia) while racing for science victory. Vancouver under heavy tank assault. Core cities building Strategic Defense Systems and Atomic Bomb. Cannot afford to reduce military posture while under existential threat. Spaceship (100) and Espionage (100) priorities maintained for tech theft and victory components.
        - GrandStrategy: Spaceship
        
        ### Flavors
        - Offense: 0
        - Defense: 100
        - Mobilization: 100
        - CityDefense: 100
        - MilitaryTraining: 70
        - Recon: 10
        - Ranged: 90
        - Mobile: 60
        - Nuke: 100
        - UseNuke: 85
        - Naval: 30
        - NavalRecon: 15
        - NavalGrowth: 15
        - NavalTileImprovement: 15
        - Air: 90
        - AirCarrier: 10
        - Antiair: 100
        - Airlift: 15
        - Expansion: 0
        - Growth: 30
        - TileImprovement: 20
        - Infrastructure: 25
        - Production: 95
        - WaterConnection: 20
        - Gold: 40
        - Science: 100
        - Culture: 5
        - Happiness: 40
        - GreatPeople: 100
        - Wonder: 0
        - Religion: 20
        - Diplomacy: 30
        - Spaceship: 100
        - Espionage: 100
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Morocco
        - Morocco:
          - CapitalsControlled:
            - Attila's Court
            - Marrakech
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - India:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Morocco:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Polynesia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - The Huns:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Iroquois:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - The Netherlands:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Shoshone:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Venice:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        
        ## CulturalVictory
        - CivsNeeded: 7
        - Contender: India
        - India:
          - Influences:
            - The Shoshone: Dominant (421%) - Rising (tourism/culture ratio 2288%)
            - The Iroquois: Dominant (532%) - Rising (tourism/culture ratio 2512%)
            - Venice: Dominant (753%) - Rising (tourism/culture ratio 2753%)
            - The Netherlands: Influential (165%) - Rising (tourism/culture ratio 1171%)
            - Morocco: Dominant (389%) - Rising (tourism/culture ratio 1530%)
            - The Huns: Dominant (739%) - Rising (tourism/culture ratio 16336%)
            - Polynesia: Dominant (322%) - Rising (tourism/culture ratio 1558%)
          - PolicyPercentage: 100
          - InfluentialCivs: 7
        - Morocco:
          - Influences:
            - The Shoshone: Popular (67%) - Rising (56 turns to Influential, tourism/culture ratio 236%)
            - The Iroquois: Popular (67%) - Rising (61 turns to Influential, tourism/culture ratio 224%)
            - Venice: Influential (137%) - Rising (tourism/culture ratio 293%)
            - The Netherlands: Familiar (26%) - Rising Slowly (tourism/culture ratio 87%)
            - Polynesia: Popular (54%) - Rising (178 turns to Influential, tourism/culture ratio 165%)
            - The Huns: Influential (111%) - Rising (tourism/culture ratio 1839%)
            - India: Exotic (20%) - Rising Slowly (tourism/culture ratio 35%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        - Polynesia:
          - Influences:
            - The Shoshone: Popular (80%) - Rising (25 turns to Influential, tourism/culture ratio 276%)
            - The Iroquois: Popular (85%) - Rising (15 turns to Influential, tourism/culture ratio 307%)
            - Venice: Influential (130%) - Rising (tourism/culture ratio 249%)
            - The Netherlands: Familiar (30%) - Rising Slowly (tourism/culture ratio 106%)
            - Morocco: Popular (86%) - Rising (20 turns to Influential, tourism/culture ratio 205%)
            - The Huns: Influential (157%) - Rising (tourism/culture ratio 1822%)
            - India: Familiar (28%) - Rising Slowly (tourism/culture ratio 51%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        - The Huns:
          - Influences:
            - The Shoshone: Exotic (7%) - Rising Slowly (tourism/culture ratio 11%)
            - The Iroquois: Exotic (7%) - Rising Slowly (tourism/culture ratio 11%)
            - Venice: Exotic (13%) - Rising Slowly (tourism/culture ratio 13%)
            - Polynesia: Exotic (5%) - Rising Slowly (tourism/culture ratio 6%)
            - Morocco: Exotic (6%) - Rising Slowly (tourism/culture ratio 7%)
          - PolicyPercentage: 81
          - InfluentialCivs: 0
        - The Iroquois:
          - Influences:
            - The Shoshone: Popular (58%) - Rising (132 turns to Influential, tourism/culture ratio 183%)
            - Morocco: Familiar (49%) - Rising Slowly (tourism/culture ratio 124%)
            - Venice: Influential (102%) - Rising (tourism/culture ratio 191%)
            - The Netherlands: Familiar (26%) - Rising Slowly (tourism/culture ratio 74%)
            - Polynesia: Familiar (37%) - Rising Slowly (tourism/culture ratio 114%)
            - The Huns: Popular (87%) - Rising (12 turns to Influential, tourism/culture ratio 1017%)
            - India: Exotic (20%) - Rising Slowly (tourism/culture ratio 28%)
          - PolicyPercentage: 100
          - InfluentialCivs: 1
        - The Netherlands:
          - Influences:
            - The Shoshone: Popular (96%) - Rising (6 turns to Influential, tourism/culture ratio 240%)
            - The Iroquois: Influential (108%) - Rising (tourism/culture ratio 239%)
            - Venice: Dominant (208%) - Rising (tourism/culture ratio 322%)
            - Polynesia: Popular (56%) - Rising (442 turns to Influential, tourism/culture ratio 140%)
            - Morocco: Popular (82%) - Rising (70 turns to Influential, tourism/culture ratio 151%)
            - The Huns: Dominant (205%) - Rising (tourism/culture ratio 2062%)
            - India: Familiar (28%) - Rising Slowly (tourism/culture ratio 36%)
          - PolicyPercentage: 100
          - InfluentialCivs: 3
        - The Shoshone:
          - Influences:
            - The Iroquois: Popular (61%) - Rising (59 turns to Influential, tourism/culture ratio 243%)
            - Morocco: Popular (59%) - Rising (176 turns to Influential, tourism/culture ratio 148%)
            - Venice: Influential (123%) - Rising (tourism/culture ratio 302%)
            - The Netherlands: Familiar (31%) - Rising Slowly (tourism/culture ratio 121%)
            - Polynesia: Familiar (42%) - Rising (523 turns to Influential, tourism/culture ratio 142%)
            - The Huns: Influential (106%) - Rising (tourism/culture ratio 1437%)
            - India: Exotic (19%) - Rising Slowly (tourism/culture ratio 37%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        - Venice:
          - Influences:
            - The Shoshone: Exotic (11%) - Rising Slowly (tourism/culture ratio 38%)
            - The Iroquois: Exotic (12%) - Rising Slowly (tourism/culture ratio 41%)
            - The Netherlands: Exotic (6%) - Rising Slowly (tourism/culture ratio 19%)
            - Morocco: Exotic (11%) - Rising Slowly (tourism/culture ratio 28%)
            - The Huns: Exotic (21%) - Rising (722 turns to Influential, tourism/culture ratio 282%)
            - Polynesia: Exotic (7%) - Rising Slowly (tourism/culture ratio 23%)
          - PolicyPercentage: 88
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 42
        - Status: World Congress - Voting in 2 turns
        - ActiveResolutions:
          - Open Door: Mombasa:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: -1
          - Sanction: The Huns:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: -1
          - World Science Initiative:
            - Description: Increases up to 33% generation of Great Scientists, Engineers, and Merchants. Decreases up to 33% generation of Great Writers, Artists, and Musicians.
              Civilizations with Scores from Technologies and Future Tech below the global median will receive a boost to Food and Science up to 33%.
              Details: The boosts are proportional to the difference between the score of the Civilization and the leader.
            - EnactedOn: -1
          - Cold War:
            - Description: Ideological differences have pushed the world into a cold war, and economic and political factions are forming based on ideology alone.
              While this resolution is active, players may only make Trade Routes with civilizations that follow the same ideology, or with allied City-States. Furthermore, Influence levels with allied City-States do not decline.
              Available once any Civilization discovers Atomic Theory.
            - EnactedOn: 347
          - Scholars In Residence:
            - Description: Civilizations have -20% Research cost for Technologies already discovered by another Civilization. Additional -2% for every City-State Ally, up to -50%.
            - EnactedOn: -1
          - Venetian Sphere of Influence: Ragusa:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 369
          - Dutch Sphere of Influence: Kyiv:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - World Ideology: Order:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: 369
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: -1
        - Proposals:
          - Enact: Global Hegemony:
            - Description: Designate a player that could achieve Global Hegemony. If a Civilization receives support from enough Delegates in the Congress, that leader will attain Diplomatic Victory. The number of Delegates needed depends on the number of Civilizations and City-States in the game, and can be seen on the World Congress screen.
              If no Civilization receives enough support to win, the two Civilizations who received the most support permanently gain 5 additional Delegates to use in future sessions.
              May not be proposed by a Civilization. Automatically proposed at regular intervals once a World Ideology Resolution is active.
            - Proposer: Unknown
        - Contender: India
        - India:
          - Delegates: 28
          - VictoryPercentage: 66
        - Morocco:
          - Delegates: 26
          - VictoryPercentage: 61
        - Polynesia:
          - Delegates: 15
          - VictoryPercentage: 35
        - The Huns:
          - Delegates: 13
          - VictoryPercentage: 30
        - The Iroquois:
          - Delegates: 12
          - VictoryPercentage: 28
        - The Netherlands:
          - Delegates: 18
          - VictoryPercentage: 42
        - The Shoshone:
          - Delegates: 15
          - VictoryPercentage: 35
        - Venice:
          - Delegates: 14
          - VictoryPercentage: 33
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: The Huns
        - Leader: Attila
        - IsMajor: true
        - OurOpinionToThem:
          - Our leader has expressed a public opinion to this player (85).
          - Our leader has formed a private opinion to this player (85).
          - Our real approach is War.
          - We have divergent Social Policies. (-3)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - We defeated their proposal in the United Nations. (-36)
          - You have adopted the Order Ideology, but they believe in Freedom. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have no contested borders.
          - They liked our proposal to the United Nations.
          - You have shared intrigue with them.
          - Your recent diplomatic actions please them.
          - Your votes supported their civ's interests in the United Nations.
          - They have denounced us!
          - We have divergent Social Policies.
          - You have denounced a leader they made a Declaration of Friendship with!
          - Their friends or allies have denounced you!
          - You have chosen to adopt the Freedom Ideology, but they believe in Order.
          - You are at war!
        - Score: 1004
        - Era: Atomic
        - Technologies: 60
        - Cities: 3
        - Population: 58
        - Territory: 99
        - Gold: 368
        - GoldPerTurn: 70
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 41
        - MilitaryStrength: 766
        - TourismPerTurn: 23.5
        - CulturePerTurn: 123
        - PolicyBranches:
          - Statecraft: 6
          - Order: 1
          - Imperialism: 5
          - Authority: 6
        - ResourcesAvailable:
          - Sheep: 1
          - Paper: 4
          - Deer: 4
          - Iron: 3
          - Coal: 5
          - Tea: 2
          - Horses: 6
          - Bison: 1
          - Copper: 1
          - Stone: 1
          - Oil: 9
          - Cocoa: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Shoshone:
            - Distance: Close
          - The Iroquois:
            - Distance: Close
            - Declaration of Friendship
          - Venice:
            - Distance: Neighbors
          - Polynesia:
            - Distance: Close
          - The Netherlands:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Morocco:
            - Distance: Neighbors
            - Peace Treaty
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - India:
            - Distance: Neighbors
        - Votes: 13
        
        ## Player 1
        - Civilization: Polynesia
        - Leader: Kamehameha
        - IsMajor: true
        - OurOpinionToThem:
          - We have Pledged to Protect the same City-States. (7)
          - Our real approach is Hostile.
          - You killed or captured their civilians! (-2)
          - We have divergent Social Policies. (-3)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the United Nations. (-36)
          - You have chosen to adopt the Order Ideology, but they believe in Freedom. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - We have Pledged to Protect the same City-States.
          - You have no contested borders.
          - They have denounced us!
          - They are spreading their own religion, but you converted some of their cities to your religion.
          - We tried to place sanctions on them in the United Nations.
          - We have divergent Social Policies.
          - Religious differences strain your relationship.
          - You are competing for the favor of the same City-States!
          - You are competing for World Wonders.
          - They disliked our proposal to the United Nations.
          - They believe we are building World Wonders too aggressively!
          - They are jealous of our superior culture!
          - Your success angers them.
          - Their friends or allies have denounced you!
          - You have denounced a leader they made a Declaration of Friendship with!
          - Your votes opposed their civ's interests in the United Nations.
          - You have chosen to adopt the Freedom Ideology, but they believe in Order.
          - You are at war!
        - Score: 2361
        - Era: Information
        - Technologies: 72
        - Cities: 13
        - Population: 301
        - Territory: 401
        - Gold: 229
        - GoldPerTurn: 239
        - HappinessSituation: Happy
        - HappinessPercentage: 55
        - MilitaryStrength: 6133
        - TourismPerTurn: 1011.25
        - CulturePerTurn: 1682
        - PolicyBranches:
          - Fealty: 6
          - Order: 6
          - Progress: 6
          - Rationalism: 6
        - ResourcesAvailable:
          - Sheep: 1
          - Gold: 1
          - Paper: 5
          - Maize: 2
          - Aluminum: 13
          - Fish: 24
          - Amber: 1
          - Deer: 2
          - Whales: 1
          - Sugar: 1
          - Jade: 4
          - Iron: 1
          - Tea: 1
          - Coal: 7
          - Horses: 1
          - Coral: 2
          - Copper: 5
          - Stone: 3
          - Marble: 1
          - Bananas: 1
          - Oil: 6
          - Wine: 1
          - Cocoa: 1
        - FoundedReligion: Catholicism
        - Relationships:
          - The Shoshone:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Iroquois:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - Venice:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Close
            - War (Our Score: 4%; Our War Weariness: 25%)
            - Denounced Them
          - Morocco:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Huns:
            - Distance: Close
          - India:
            - Distance: Neighbors
        - Votes: 15
        
        ## Player 2
        - Civilization: The Netherlands
        - Leader: William
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: None, Our top defensive pact ally: None
          - Our top United Nations ally: None, Our top United Nations rival: India
          - Our top Competitor: Morocco
        - Score: 2221
        - Era: Atomic
        - GoldenAge: Estimated in 37 turns
        - Technologies: 65
        - CurrentResearch: Computers (Estimated in 3 turns)
        - NextPolicyTurns: 14
        - Cities: 5
        - Population: 133
        - Territory: 159
        - BestSettlementLocation:
          - 56, 4 (Quality: 0%; 5 tiles from us)
          - 57, 4 (Quality: 0%; 7 tiles from us)
          - 55, 4 (Quality: 0%; 5 tiles from us)
          - 56, 6 (Quality: 0%; 4 tiles from us)
          - 56, 2 (Quality: 0%; 9 tiles from us)
        - Gold: 477
        - GoldPerTurn: -30
        - HappinessSituation: Happy
        - HappinessPercentage: 75
        - MilitaryUnits: 47
        - MilitarySupply: 54
        - MilitaryStrength: 3319
        - TourismPerTurn: 814.5
        - CulturePerTurn: 1445
        - FaithPerTurn: 169
        - SciencePerTurn: 1254
        - PolicyBranches:
          - Freedom:
            - Creative Expression
            - Covert Action
            - Capitalism
            - Economic Union
            - Their Finest Hour
            - Universal Suffrage
            - Arsenal of Democracy
            - Containment
          - Tradition:
            - Tradition
            - Justice
            - Ceremony
            - Splendor
          - Rationalism:
            - Rationalism
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
            - Exchange Markets
            - Trade Confederacy
          - Imperialism:
            - Imperialism
            - Regimental System
            - Civilizing Mission
          - Progress:
            - Progress
            - Liberty
          - Industry:
            - Industry
            - Division of Labor
            - Free Trade
        - ResourcesAvailable:
          - Wheat: 3
          - Silver: 0
          - Sheep: 5
          - Cloves: 0
          - Figs: 0
          - Ivory: 1
          - Gold: 0
          - Nutmeg: 0
          - Paper: 12
          - Pearls: 0
          - Maize: 0
          - Rice: 0
          - Cotton: 0
          - Gems: 0
          - Salt: 0
          - Brazilwood: 0
          - Aluminum: 17
          - Glass: 0
          - Lapis Lazuli: 9
          - Fish: 0
          - Amber: 0
          - Perfume: 0
          - Deer: 2
          - Whales: 0
          - Olives: 2
          - Sugar: 0
          - Jade: 0
          - Iron: 3
          - Dyes: 0
          - Tea: 0
          - Coffee: 0
          - Cattle: 2
          - Pepper: 0
          - Uranium: 1
          - Horses: 3
          - Coral: 0
          - Silk: 0
          - Jewelry: 0
          - Bison: 0
          - Antiquity Site: 0
          - Citrus: 1
          - Copper: 1
          - Truffles: 0
          - Crab: 0
          - Incense: 0
          - Stone: 0
          - Marble: 0
          - Furs: 0
          - Cinnamon: 0
          - Bananas: 0
          - Oil: 0
          - Wine: 0
          - Porcelain: 0
          - Cocoa: 0
          - Tobacco: 0
        - FoundedReligion: Buddhism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: -16%; Our War Weariness: 45%)
            - Denounced Them
          - The Iroquois:
            - Distance: Close
            - Denounced Them
          - Venice:
            - Distance: Close
            - Peace Treaty
          - Polynesia:
            - Distance: Close
            - War (Our Score: -4%; Our War Weariness: 28%)
          - Morocco:
            - Distance: Neighbors
            - War (Our Score: -22%; Our War Weariness: 47%)
            - Denounced Them
          - The Huns:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
          - India:
            - Distance: Far
            - Denounced Them
        - OutgoingTradeRoutes:
          - Groningen (The Netherlands) => Kyiv (City-State Kyiv):
            - TurnsLeft: 12
            - FromScience: 7.5
            - Domain: Land
            - FromGold: 52.64
            - FromCulture: 7.5
          - Rotterdam (The Netherlands) => Groningen (The Netherlands):
            - ToFood: 32.24
            - TurnsLeft: 2
            - Domain: Land
          - Groningen (The Netherlands) => Utrecht (The Netherlands):
            - TurnsLeft: 3
            - Domain: Land
            - ToProduction: 21
          - Vancouver (The Netherlands) => Groningen (The Netherlands):
            - ToFood: 28.24
            - TurnsLeft: 7
            - Domain: Land
          - Groningen (The Netherlands) => Rotterdam (The Netherlands):
            - TurnsLeft: 3
            - Domain: Land
            - ToProduction: 21
          - Available: 6
          - Rotterdam (The Netherlands) => Utrecht (The Netherlands):
            - TurnsLeft: 20
            - Domain: Land
            - ToProduction: 23
          - Utrecht (The Netherlands) => Groningen (The Netherlands):
            - ToFood: 28.24
            - TurnsLeft: 12
            - Domain: Land
          - Groningen (The Netherlands) => Vancouver (The Netherlands):
            - TurnsLeft: 2
            - Domain: Land
            - ToProduction: 22
        - Spies:
          - Agent Katrijn (6):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 3968
            - Location: Goshute (The Shoshone)
            - NetworkPerTurn: 68
          - Agent Guus (1):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 774
            - Location: Aotearoa (Polynesia)
            - NetworkPerTurn: 74
          - Agent Geerard (8):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 2484
            - Location: Onondaga (The Iroquois)
            - NetworkPerTurn: 53
          - Agent Hannes (7):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 4247
            - Location: Te-Moak (The Shoshone)
            - NetworkPerTurn: 45
          - Agent Rutger (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 4480
            - Location: Venice (Venice)
            - NetworkPerTurn: 80
          - Agent Marten (3):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 2629
            - Location: Delhi (India)
            - NetworkPerTurn: 38
          - Agent Rasmus (5):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 432
            - Location: Marrakech (Morocco)
            - NetworkPerTurn: 52
          - Agent Doortje (0):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 3304
            - Location: Agaidika (The Shoshone)
            - NetworkPerTurn: 51
          - Agent Lijsbeth (2):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 4502
            - Location: Moson Kahni (The Shoshone)
            - NetworkPerTurn: 36
        - DiplomaticDeals:
          - Venice:
            - #0:
              - WeGive:
                - Peace Treaty
                - Make Peace with City-State Ragusa
              - TheyGive:
                - Peace Treaty
                - Make Peace with City-State Kyiv
              - TurnsRemaining: 9
        - Votes: 18
        
        ## Player 3
        - Civilization: The Shoshone
        - Leader: Pocatello
        - IsMajor: true
        - OurOpinionToThem:
          - We have similar Social Policies. (3)
          - Our real approach is Hostile.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the United Nations. (-36)
          - You have chosen to adopt the Order Ideology, but they believe in Freedom. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - The leader has expressed a public opinion to you (100).
          - We have similar Social Policies.
          - You have no contested borders.
          - They are spreading their own religion, but you converted some of their cities to your religion.
          - Your recent diplomatic actions disappoint them.
          - You plundered their trade routes!
          - Religious differences strain your relationship.
          - They believe we are building World Wonders too aggressively!
          - They disliked our proposal to the United Nations.
          - You are competing for the favor of the same City-States!
          - They are jealous of our superior technology!
          - We have denounced each other!
          - Your votes opposed their civ's interests in the United Nations.
          - Your spies were caught stealing from them.
          - Their friends or allies have denounced you!
          - You have denounced a leader they made a Declaration of Friendship with!
          - You have chosen to adopt the Freedom Ideology, but they believe in Order.
          - You are at war!
        - Score: 2217
        - Era: Information
        - Technologies: 69
        - Cities: 6
        - Population: 168
        - Territory: 290
        - Gold: 2209
        - GoldPerTurn: 273
        - HappinessSituation: Happy
        - HappinessPercentage: 58
        - MilitaryStrength: 9624
        - TourismPerTurn: 650.5
        - CulturePerTurn: 1012
        - PolicyBranches:
          - Order: 3
          - Rationalism: 2
          - Tradition: 5
          - Artistry: 3
          - Statecraft: 2
          - Industry: 2
          - Progress: 5
          - Authority: 1
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 3
          - Paper: 6
          - Maize: 7
          - Rice: 2
          - Aluminum: 13
          - Fish: 3
          - Amber: 8
          - Deer: 2
          - Olives: 1
          - Sugar: 1
          - Jade: 1
          - Iron: 1
          - Tea: 1
          - Coal: 7
          - Cattle: 7
          - Coral: 1
          - Bison: 1
          - Copper: 1
          - Stone: 1
          - Marble: 1
          - Bananas: 1
          - Wine: 1
          - Cocoa: 2
        - FoundedReligion: Protestantism
        - Relationships:
          - The Iroquois:
            - Distance: Neighbors
            - Declaration of Friendship
          - Morocco:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Venice:
            - Distance: Neighbors
            - Defensive Pact
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Neighbors
            - War (Our Score: 16%; Our War Weariness: 37%)
            - Denounced Them
          - Polynesia:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Huns:
            - Distance: Close
          - India:
            - Distance: Neighbors
        - Votes: 15
        
        ## Player 4
        - Civilization: India
        - Leader: Gandhi
        - IsMajor: true
        - OurOpinionToThem:
          - We have similar Social Policies. (3)
          - You have gone to war in the past.
          - Our real approach is Guarded.
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the United Nations. (-36)
          - Our leader has expressed a public opinion to this player (-100).
          - Our leader has formed a private opinion to this player (-100).
          - You have chosen to adopt the Order Ideology, but they believe in Freedom. (-999)
        - TheirOpinionToUs:
          - You have denounced one of their declared enemies!
          - You are not competing for cultural advancement.
          - You are not competing for World Wonders.
          - We passed their proposal in the United Nations.
          - We have similar Social Policies.
          - We are trade partners.
          - You have no contested borders.
          - They suspect we might be a threat to them.
          - Your recent diplomatic actions disappoint them.
          - Religious differences strain your relationship.
          - You are competing for the favor of the same City-States!
          - They disliked our proposal to the United Nations.
          - We have denounced each other!
          - Your votes opposed their civ's interests in the United Nations.
          - You have chosen to adopt the Freedom Ideology, but they believe in Order.
        - Score: 3923
        - Era: Information
        - GoldenAge: 12 turns remaining
        - Technologies: 74
        - Cities: 13
        - Population: 384
        - Territory: 561
        - Gold: 2773
        - GoldPerTurn: 338
        - HappinessSituation: Happy
        - HappinessPercentage: 71
        - MilitaryStrength: 26874
        - TourismPerTurn: 4194.21
        - CulturePerTurn: 5795
        - PolicyBranches:
          - Fealty: 1
          - Order: 11
          - Tradition: 6
          - Artistry: 6
          - Statecraft: 1
          - Rationalism: 3
          - Industry: 1
          - Progress: 2
        - ResourcesAvailable:
          - Wheat: 5
          - Sheep: 5
          - Ivory: 2
          - Nutmeg: 2
          - Paper: 14
          - Glass: 1
          - Maize: 2
          - Rice: 3
          - Gems: 9
          - Aluminum: 19
          - Bison: 5
          - Olives: 1
          - Deer: 4
          - Whales: 1
          - Sugar: 2
          - Iron: 6
          - Tea: 1
          - Fish: 15
          - Cattle: 2
          - Citrus: 3
          - Truffles: 2
          - Stone: 5
          - Marble: 2
          - Bananas: 1
          - Wine: 3
          - Porcelain: 1
        - FoundedReligion: Hinduism
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
          - The Iroquois:
            - Distance: Neighbors
            - War (Our Score: 68%; Our War Weariness: 51%)
          - Venice:
            - Distance: Neighbors
          - The Netherlands:
            - Distance: Far
            - Denounced Them
          - Morocco:
            - Distance: Close
          - The Huns:
            - Distance: Neighbors
          - Polynesia:
            - Distance: Neighbors
        - Votes: 28
        
        ## Player 5
        - Civilization: The Iroquois
        - Leader: Hiawatha
        - IsMajor: true
        - OurOpinionToThem:
          - We have similar Social Policies. (3)
          - You have gone to war in the past.
          - Our real approach is Guarded.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the United Nations. (-36)
          - Our leader has expressed a public opinion to this player (-50).
          - Our leader has formed a private opinion to this player (-70).
          - You have chosen to adopt the Order Ideology, but they believe in Freedom. (-999)
        - TheirOpinionToUs:
          - We passed their proposal in the United Nations.
          - You have denounced one of their declared enemies!
          - We have similar Social Policies.
          - You have no contested borders.
          - They suspect we might be a threat to them.
          - Your recent diplomatic actions disappoint them.
          - They disliked our proposal to the United Nations.
          - Their friends or allies have denounced you!
          - They believe we are building World Wonders too aggressively!
          - They are jealous of our superior technology!
          - We have denounced each other!
          - You have denounced a leader they made a Declaration of Friendship with!
          - You have chosen to adopt the Freedom Ideology, but they believe in Order.
          - Your votes opposed their civ's interests in the United Nations.
        - Score: 1835
        - Era: Information
        - Technologies: 70
        - Cities: 8
        - Population: 206
        - Territory: 232
        - Gold: 7686
        - GoldPerTurn: 590
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 45
        - MilitaryStrength: 2198
        - TourismPerTurn: 683.25
        - CulturePerTurn: 1014
        - PolicyBranches:
          - Order: 4
          - Rationalism: 4
          - Tradition: 2
          - Artistry: 1
          - Statecraft: 4
          - Industry: 1
          - Progress: 5
          - Authority: 1
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 2
          - Ivory: 1
          - Gold: 1
          - Paper: 10
          - Maize: 1
          - Rice: 4
          - Aluminum: 2
          - Fish: 6
          - Amber: 1
          - Whales: 1
          - Olives: 1
          - Sugar: 1
          - Jade: 1
          - Iron: 1
          - Tea: 1
          - Coal: 2
          - Cattle: 4
          - Uranium: 4
          - Horses: 4
          - Coral: 1
          - Bison: 3
          - Copper: 1
          - Stone: 1
          - Marble: 1
          - Bananas: 7
          - Cocoa: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Morocco:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - Venice:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Close
            - Denounced Them
          - Polynesia:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - The Huns:
            - Distance: Close
            - Declaration of Friendship
          - India:
            - Distance: Neighbors
            - War (Our Score: -68%; Our War Weariness: 99%)
        - Votes: 12
        
        ## Player 6
        - Civilization: Venice
        - Leader: Enrico Dandolo
        - IsMajor: true
        - OurOpinionToThem:
          - You have denounced one of their declared enemies! (11)
          - We have similar Social Policies. (3)
          - You have gone to war in the past.
          - Our real approach is Guarded.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the United Nations. (-36)
          - You have chosen to adopt the Autocracy Ideology, but they believe in Freedom. (-999)
        - TheirOpinionToUs:
          - You have denounced one of their declared enemies!
          - They liked our proposal to the United Nations.
          - We passed their proposal in the United Nations.
          - We have similar Social Policies.
          - You have no contested borders.
          - They have denounced us!
          - They suspect we might be a threat to them.
          - Your recent diplomatic actions disappoint them.
          - The leader has expressed a public opinion to you (-20).
          - They believe we are building World Wonders too aggressively!
          - You are competing for the favor of the same City-States!
          - Your spies were caught stealing from them.
          - Their friends or allies have denounced you!
          - You have chosen to adopt the Freedom Ideology, but they believe in Autocracy.
          - Your votes opposed their civ's interests in the United Nations.
          - You have denounced a leader they made a Declaration of Friendship with!
        - Score: 1655
        - Era: Atomic
        - Technologies: 61
        - Cities: 9
        - Population: 219
        - Territory: 272
        - Gold: 65
        - GoldPerTurn: -35
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 36
        - MilitaryStrength: 3555
        - TourismPerTurn: 145.23
        - CulturePerTurn: 643
        - PolicyBranches:
          - Tradition: 6
          - Rationalism: 2
          - Statecraft: 6
          - Autocracy: 1
          - Industry: 4
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 1
          - Ivory: 1
          - Gold: 1
          - Paper: 5
          - Aluminum: 7
          - Maize: 2
          - Lapis Lazuli: 1
          - Whales: 1
          - Sugar: 1
          - Olives: 1
          - Jade: 1
          - Coal: -2
          - Tea: 1
          - Cattle: 4
          - Horses: 1
          - Coral: 3
          - Fish: 11
          - Bison: 4
          - Truffles: 1
          - Citrus: 1
          - Stone: 3
          - Bananas: 1
          - Wine: 1
          - Cocoa: 5
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Iroquois:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - Morocco:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Close
            - Peace Treaty
            - Denounced Them
          - Polynesia:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - The Huns:
            - Distance: Neighbors
          - India:
            - Distance: Neighbors
            - Denounced Them
        - Votes: 14
        
        ## Player 7
        - Civilization: Morocco
        - Leader: Ahmad al-Mansur
        - IsMajor: true
        - OurOpinionToThem:
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Our real approach is Hostile.
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - We defeated their proposal in the United Nations. (-36)
          - You stole their territory! (-50)
          - You have chosen to adopt the Order Ideology, but they believe in Freedom. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - We passed their proposal in the United Nations.
          - The leader has expressed a public opinion to you (95).
          - We have similar Social Policies.
          - We have Pledged to Protect the same City-States.
          - You plundered their trade routes!
          - You made a trade demand of them!
          - Religious differences strain your relationship.
          - Territorial disputes strain your relationship.
          - Your spies were caught stealing from them.
          - You are competing for World Wonders.
          - They believe we are building World Wonders too aggressively!
          - They disliked our proposal to the United Nations.
          - You are competing for the favor of the same City-States!
          - We have denounced each other!
          - Their friends or allies have denounced you!
          - You have denounced a leader they made a Declaration of Friendship with!
          - Your votes opposed their civ's interests in the United Nations.
          - You have chosen to adopt the Freedom Ideology, but they believe in Order.
          - You are at war!
        - Score: 2304
        - Era: Information
        - GoldenAge: 4 turns remaining
        - Technologies: 71
        - Cities: 9
        - Population: 230
        - Territory: 264
        - Gold: 2233
        - GoldPerTurn: 767
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 50
        - MilitaryStrength: 5817
        - TourismPerTurn: 628.68
        - CulturePerTurn: 1756
        - PolicyBranches:
          - Tradition: 3
          - Rationalism: 2
          - Statecraft: 6
          - Order: 3
          - Progress: 5
          - Industry: 4
        - ResourcesAvailable:
          - Wheat: 5
          - Sheep: 3
          - Gold: 1
          - Paper: 5
          - Maize: 1
          - Aluminum: 11
          - Fish: 12
          - Amber: 1
          - Deer: 4
          - Olives: 2
          - Sugar: 1
          - Jade: 5
          - Iron: 5
          - Tea: 1
          - Coal: 28
          - Cattle: 2
          - Horses: 3
          - Coral: 2
          - Bison: 1
          - Citrus: 1
          - Copper: 1
          - Stone: 2
          - Marble: 1
          - Oil: 6
          - Cocoa: 2
        - FoundedReligion: Islam
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Iroquois:
            - Distance: Far
            - Open Borders
            - Declaration of Friendship
          - Venice:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - The Netherlands:
            - Distance: Neighbors
            - War (Our Score: 22%; Our War Weariness: 30%)
            - Denounced Them
          - Polynesia:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Huns:
            - Distance: Neighbors
            - Peace Treaty
            - Our Vassal (Capitulated)
            - Declaration of Friendship
          - India:
            - Distance: Close
        - Votes: 26
        
        ## Player 22
        - Civilization: Ragusa
        - Leader: City State
        - MajorAlly: Venice
        - Population: 14
        - ResourcesAvailable:
          - Fish: 2
          - Sheep: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - The Shoshone: Neutral (Influence: -16, Distance: Far)
          - The Iroquois: Neutral (Influence: 0, Distance: Far)
          - Morocco: Friends (Influence: 65, Distance: Far, Protected)
          - Venice: Ally (Influence: 198, Distance: Far)
          - The Netherlands: Friends (Influence: 30, Distance: Neighbors)
          - Polynesia: Friends (Influence: 48, Distance: Close)
          - The Huns: Neutral (Influence: -16, Distance: Distant)
          - India: Friends (Influence: 549, Distance: Distant)
        - Quests:
          -  Conduct a Spy Mission against Ahmad al-Mansur. Potential Quest Reward: * 367 Influence * 918 Science
        
        ## Player 23
        - Civilization: Heidabir
        - Leader: City State
        - MajorAlly: India
        - Population: 13
        - ResourcesAvailable:
          - Deer: 1
        - Relationships:
          - The Shoshone: Neutral (Influence: -53, Distance: Close)
          - The Iroquois: War (Influence: -60, Distance: Distant)
          - Morocco: Neutral (Influence: -53, Distance: Neighbors)
          - Venice: Neutral (Influence: -53, Distance: Far)
          - The Netherlands: Neutral (Influence: -23, Distance: Neighbors)
          - Polynesia: Neutral (Influence: -33, Distance: Close)
          - The Huns: Neutral (Influence: -53, Distance: Distant)
          - India: Ally (Influence: 909, Distance: Distant, Protected)
        - Quests:
          -  Conduct a Spy Mission against Hiawatha. Potential Quest Reward: * 366 Influence * 886 Science
        - 24: Defeated Minor Civilization Djenne
        - 25: Defeated Minor Civilization Prague
        
        ## Player 26
        - Civilization: Antananarivo
        - Leader: City State
        - MajorAlly: India
        - Population: 17
        - ResourcesAvailable:
          - Fish: 4
        - Relationships:
          - The Shoshone: Neutral (Influence: 29, Distance: Close, Protected)
          - The Iroquois: War (Influence: -60, Distance: Distant)
          - Morocco: Friends (Influence: 65, Distance: Close, Protected)
          - Venice: Neutral (Influence: 10, Distance: Close, Protected)
          - The Netherlands: Friends (Influence: 92, Distance: Far)
          - Polynesia: Friends (Influence: 49, Distance: Neighbors, Protected)
          - The Huns: Neutral (Influence: 29, Distance: Far)
          - India: Ally (Influence: 767, Distance: Distant, Protected)
        - Quests:
          -  They want you to start a land or sea trade route to their city. (Turns remaining: 4) Potential Quest Reward: * 197 Influence * 160 Food in Capital
        - 27: Defeated Minor Civilization Shanghai
        - 28: Defeated Minor Civilization Salem
        
        ## Player 29
        - Civilization: Seoul
        - Leader: City State
        - MajorAlly: Morocco
        - Population: 21
        - MajorityReligion: Hinduism
        - Relationships:
          - The Shoshone: Friends (Influence: 144, Distance: Distant, Protected)
          - The Iroquois: Neutral (Influence: -53, Distance: Neighbors)
          - Morocco: Ally (Influence: 761, Distance: Distant)
          - Venice: Friends (Influence: 98, Distance: Far)
          - The Netherlands: War (Influence: -60, Distance: Distant)
          - Polynesia: Neutral (Influence: -29, Distance: Far)
          - The Huns: Neutral (Influence: -53, Distance: Distant)
          - India: Friends (Influence: 391, Distance: Neighbors)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 30
        - Civilization: Brussels
        - Leader: City State
        - MajorAlly: India
        - Population: 21
        - ResourcesAvailable:
          - Fish: 2
          - Bison: 1
        - MajorityReligion: Hinduism
        - Relationships:
          - The Shoshone: Friends (Influence: 375, Distance: Distant)
          - The Iroquois: War (Influence: -60, Distance: Close)
          - Morocco: Friends (Influence: 111, Distance: Distant)
          - Venice: Friends (Influence: 370, Distance: Far)
          - The Netherlands: Neutral (Influence: -22, Distance: Distant)
          - Polynesia: Neutral (Influence: -32, Distance: Close)
          - The Huns: Neutral (Influence: -52, Distance: Distant)
          - India: Ally (Influence: 830, Distance: Neighbors, Protected)
        - Quests:
          -  Conduct a Spy Mission against Enrico Dandolo. Potential Quest Reward: * 367 Influence * 918 Science
        
        ## Player 31
        - Civilization: Lhasa
        - Leader: City State
        - MajorAlly: India
        - Population: 23
        - ResourcesAvailable:
          - Deer: 1
          - Fish: 4
        - MajorityReligion: Hinduism
        - Relationships:
          - The Shoshone: Neutral (Influence: -58, Distance: Distant)
          - The Iroquois: War (Influence: -60, Distance: Far)
          - Morocco: Neutral (Influence: 13, Distance: Far, Protected)
          - Venice: Friends (Influence: 241, Distance: Far, Protected)
          - The Netherlands: Neutral (Influence: -58, Distance: Distant)
          - Polynesia: Neutral (Influence: -59, Distance: Neighbors)
          - The Huns: Neutral (Influence: -58, Distance: Far)
          - India: Ally (Influence: 1024, Distance: Neighbors, Protected)
        - Quests:
          -  Conduct a Spy Mission against Gandhi. Potential Quest Reward: * 367 Influence * 550 Science
          - They want Buddhism to become the majority religion in their city. (Turns remaining: 36) Potential Quest Reward: * 187 Influence * 648 Faith
        - 32: Defeated Minor Civilization Ife
        - 33: Defeated Minor Civilization La Venta
        
        ## Player 34
        - Civilization: Kyiv
        - Leader: City State
        - MajorAlly: The Netherlands
        - Population: 11
        - ResourcesAvailable:
          - Deer: 2
        - Relationships:
          - The Shoshone: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - The Iroquois: Friends (Influence: 46, Distance: Distant)
          - Morocco: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Venice: Neutral (Influence: 10, Distance: Far)
          - The Netherlands: Ally (Influence: 696, Distance: Close, Protected)
          - Polynesia: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - The Huns: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - India: Friends (Influence: 403, Distance: Distant)
        - Quests:
          -  They will reward the player with the highest Tourism per turn. So far, the leader has 4,194 per turn and you have 814 per turn. (Turns remaining: 21) Potential Quest Reward: * 295 Influence * 877 Culture
          - They want Buddhism to become the majority religion in their city. (Turns remaining: 16) Potential Quest Reward: * 196 Influence * 427 Faith
          - They want you to generate a Great Artist. (Turns remaining: 5) Potential Quest Reward: * 153 Influence * 720 Culture
        - 35: Defeated Minor Civilization Vancouver
        
        ## Player 36
        - Civilization: Buenos Aires
        - Leader: City State
        - MajorAlly: India
        - Population: 23
        - ResourcesAvailable:
          - Fish: 1
        - MajorityReligion: Hinduism
        - Relationships:
          - The Shoshone: Friends (Influence: 136, Distance: Distant, Protected)
          - The Iroquois: War (Influence: -60, Distance: Far)
          - Morocco: Neutral (Influence: -2, Distance: Distant)
          - Venice: Neutral (Influence: -13, Distance: Far)
          - The Netherlands: Friends (Influence: 97, Distance: Distant)
          - Polynesia: Friends (Influence: 79, Distance: Distant)
          - The Huns: Neutral (Influence: -37, Distance: Far)
          - India: Ally (Influence: 372, Distance: Neighbors)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 37
        - Civilization: Mombasa
        - Leader: City State
        - Population: 20
        - ResourcesAvailable:
          - Oil: 3
          - Truffles: 1
          - Fish: 3
          - Sheep: 1
        - MajorityReligion: Catholicism
        - Relationships:
          - The Shoshone: Neutral (Influence: 0, Distance: Distant)
          - The Iroquois: Friends (Influence: 46, Distance: Distant)
          - Morocco: Neutral (Influence: 29, Distance: Close, Protected)
          - Venice: Neutral (Influence: 0, Distance: Distant)
          - The Netherlands: Friends (Influence: 79, Distance: Far, Protected)
          - Polynesia: Friends (Influence: 54, Distance: Neighbors, Protected)
          - The Huns: Neutral (Influence: 0, Distance: Distant)
          - India: Friends (Influence: 403, Distance: Distant)
        - Quests:
          -  Conduct a Spy Mission against Kamehameha. Potential Quest Reward: * 349 Influence * 869 Science
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: The Huns
        
        ### Dordrecht
        - ID: 1277
        - X: 44
        - Y: 37
        - Population: 25
        - DefenseStrength: 64
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Ironworks
          - Imperial College
          - Alhambra
          - Ulticur
        
        ### Genesse River
        - ID: 5819
        - X: 65
        - Y: 48
        - Population: 17
        - MajorityReligion: Islam
        - DefenseStrength: 54
        
        ### Lake Simcoe
        - ID: 8530
        - X: 58
        - Y: 45
        - Population: 16
        - MajorityReligion: Islam
        - DefenseStrength: 72
        - IsCoastal: true
        
        ## Player: Polynesia
        
        ### Honolulu
        - ID: 1058
        - X: 67
        - Y: 11
        - Population: 36
        - MajorityReligion: Catholicism
        - DefenseStrength: 114
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Circus Maximus
          - Ironworks
          - Imperial College
          - Royal Collection
          - Stonehenge
          - Colossus
          - Himeji Castle
          - Palace of Culture and Science
          - Apostolic Palace
          - Firaxite Materials Headquarters
        
        ### Samoa
        - ID: 1261
        - X: 68
        - Y: 16
        - Population: 25
        - DefenseStrength: 119
        - IsCoastal: true
        - Wonders:
          - Chartered Company
          - Red Fort
          - Scrivener's Office
          - Printing Press
        
        ### Tonga
        - ID: 1501
        - X: 69
        - Y: 6
        - Population: 27
        - MajorityReligion: Catholicism
        - DefenseStrength: 88
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - National Monument
          - Forbidden Palace
          - Grand Temple
        
        ### Nuku Hiva
        - ID: 2888
        - X: 71
        - Y: 10
        - Population: 28
        - MajorityReligion: Catholicism
        - DefenseStrength: 112
        - IsCoastal: true
        
        ### Raiatea
        - ID: 4350
        - X: 74
        - Y: 3
        - Population: 26
        - MajorityReligion: Catholicism
        - DefenseStrength: 83
        - IsCoastal: true
        
        ### Aotearoa
        - ID: 5085
        - X: 70
        - Y: 43
        - Population: 28
        - DefenseStrength: 86
        - IsCoastal: true
        - Wonders:
          - Bletchley Park
        
        ### Te Wai Pounamu
        - ID: 6558
        - X: 0
        - Y: 34
        - Population: 29
        - DefenseStrength: 92
        - IsCoastal: true
        
        ### Rapa Nui
        - ID: 9900
        - X: 3
        - Y: 41
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 114
        - IsCoastal: true
        - Wonders:
          - National Intelligence Agency
        
        ### Ife
        - ID: 11183
        - X: 40
        - Y: 9
        - Population: 25
        - DefenseStrength: 84
        - IsOccupied: true
        - IsCoastal: true
        
        ### Tuamotu
        - ID: 14896
        - X: 13
        - Y: 5
        - Population: 14
        - DefenseStrength: 78
        - IsCoastal: true
        
        ### Rarotonga
        - ID: 15401
        - X: 13
        - Y: 12
        - Population: 15
        - DefenseStrength: 78
        - IsCoastal: true
        
        ### Tuvalu
        - ID: 15701
        - X: 17
        - Y: 7
        - Population: 13
        - DefenseStrength: 82
        - IsCoastal: true
        
        ### Tubuai
        - ID: 16925
        - X: 23
        - Y: 12
        - Population: 10
        - DefenseStrength: 65
        - IsCoastal: true
        
        ## Player: The Netherlands
        
        ### Amsterdam
        - ID: 1059
        - X: 49
        - Y: 11
        - Population: 32
        - MajorityReligion: Buddhism
        - DefenseStrength: 81
        - FoodStored: 1882
        - FoodPerTurn: 0
        - ProductionStored: 1280
        - ProductionPerTurn: 324
        - CurrentProduction: Airport
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 255
        - SciencePerTurn: 411
        - CulturePerTurn: 401
        - FaithPerTurn: 87
        - TourismPerTurn: 249.5
        - HappinessDelta: 15
        - BuildingCount: 52
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Recycling Center
          - Police Station
          - Artists' Guild
          - Hotel
          - Caravansary
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
        - Wonders:
          - Heroic Epic
          - Chartered Company
          - Angkor Wat
          - Hagia Sophia
          - Porcelain Tower
          - Statue of Liberty
          - Uffizi
          - Borobudur
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
          - International Finance Center
          - Roman Forum
          - Summer Palace
          - Soho Foundry
          - Menin Gate
          - State Treasury
          - Royal Guardhouse
          - Royal Astrologer
          - Grand Ossuary
        - GreatWorkCount: 9
        
        ### Rotterdam
        - ID: 1199
        - X: 47
        - Y: 15
        - Population: 25
        - MajorityReligion: Buddhism
        - DefenseStrength: 74
        - IsCoastal: true
        - FoodStored: 821
        - FoodPerTurn: 2
        - ProductionStored: 318
        - ProductionPerTurn: 271
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 5
        - GoldPerTurn: 160
        - SciencePerTurn: 158
        - CulturePerTurn: 264
        - FaithPerTurn: 11
        - TourismPerTurn: 182.25
        - HappinessDelta: 15
        - BuildingCount: 56
        - ImportantBuildings:
          - Seaport
          - Stable
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Recycling Center
          - Police Station
          - Writers' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Mine Field
          - Refinery
        - Wonders:
          - Circus Maximus
          - Imperial College
          - Nalanda
        - GreatWorkCount: 10
        
        ### Utrecht
        - ID: 1346
        - X: 51
        - Y: 16
        - Population: 24
        - MajorityReligion: Buddhism
        - DefenseStrength: 83
        - FoodStored: 751
        - FoodPerTurn: -4
        - ProductionStored: 735
        - ProductionPerTurn: 303
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 175
        - SciencePerTurn: 124
        - CulturePerTurn: 260
        - FaithPerTurn: 26
        - TourismPerTurn: 102.75
        - HappinessDelta: 12
        - BuildingCount: 52
        - ImportantBuildings:
          - Stable
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Recycling Center
          - Police Station
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
        - Wonders:
          - School of Philosophy
          - National Monument
          - Taj Mahal
          - Neuschwanstein
        - GreatWorkCount: 5
        
        ### Groningen
        - ID: 1515
        - X: 53
        - Y: 9
        - Population: 29
        - MajorityReligion: Buddhism
        - DefenseStrength: 68
        - FoodStored: 1890
        - FoodPerTurn: 6
        - ProductionStored: 1227
        - ProductionPerTurn: 295
        - CurrentProduction: Atomic Bomb
        - ProductionTurnsLeft: 4
        - GoldPerTurn: 299
        - SciencePerTurn: 213
        - CulturePerTurn: 363
        - FaithPerTurn: 36
        - TourismPerTurn: 244.75
        - HappinessDelta: 1
        - BuildingCount: 52
        - ImportantBuildings:
          - Water Mill
          - Windmill
          - Customs House
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Recycling Center
          - Police Station
          - Writers' Guild
          - Artists' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
        - Wonders:
          - Ironworks
          - Royal Collection
          - Sistine Chapel
          - Grand Temple
          - Globe Theatre
          - The Motherland Calls
          - Giorgio Armeier Headquarters
        - GreatWorkCount: 9
        
        ### Vancouver
        - ID: 8438
        - X: 55
        - Y: 14
        - Population: 23
        - DefenseStrength: 79
        - Health: 92%
        - IsOccupied: true
        - FoodStored: 950
        - FoodPerTurn: -10
        - ProductionStored: 824
        - ProductionPerTurn: 224
        - CurrentProduction: Strategic Defense System
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 114
        - SciencePerTurn: 111
        - CulturePerTurn: 123
        - FaithPerTurn: 9
        - TourismPerTurn: 35.25
        - BuildingCount: 52
        - ImportantBuildings:
          - Courthouse
          - Windmill
          - Customs House
          - Garden
          - Zoo
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Medical Lab
          - Factory
          - Stock Exchange
          - Research Lab
          - Recycling Center
          - Police Station
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Refinery
        - GreatWorkCount: 1
        
        ## Player: The Shoshone
        
        ### Moson Kahni
        - ID: 1060
        - X: 46
        - Y: 22
        - Population: 39
        - MajorityReligion: Protestantism
        - DefenseStrength: 86
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Ironworks
          - Great Lighthouse
          - Great Wall
          - Statue of Zeus
          - Mausoleum of Halicarnassus
          - National Intelligence Agency
          - Leaning Tower of Pisa
          - Printing Press
          - Palace of Culture and Science
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Great Altar
        
        ### Te-Moak
        - ID: 1308
        - X: 51
        - Y: 21
        - Population: 30
        - MajorityReligion: Protestantism
        - DefenseStrength: 77
        - Wonders:
          - Chartered Company
          - Imperial College
          - Oracle
          - Machu Picchu
          - Grand Temple
          - Scrivener's Office
        
        ### Agaidika
        - ID: 1459
        - X: 56
        - Y: 21
        - Population: 29
        - MajorityReligion: Protestantism
        - DefenseStrength: 61
        - Wonders:
          - Circus Maximus
          - Royal Collection
          - Notre Dame
          - Foreign Bureau
        
        ### Goshute
        - ID: 1761
        - X: 44
        - Y: 27
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 63
        - IsCoastal: true
        
        ### Pohokwi
        - ID: 5649
        - X: 34
        - Y: 14
        - Population: 24
        - MajorityReligion: Protestantism
        - DefenseStrength: 73
        - IsCoastal: true
        
        ### Washakie
        - ID: 6625
        - X: 37
        - Y: 17
        - Population: 20
        - MajorityReligion: Protestantism
        - DefenseStrength: 65
        - IsCoastal: true
        
        ## Player: India
        
        ### Delhi
        - ID: 1061
        - X: 26
        - Y: 38
        - Population: 61
        - MajorityReligion: Hinduism
        - DefenseStrength: 107
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Ironworks
          - Pyramids
          - Chichen Itza
          - Kremlin
          - Eiffel Tower
          - Sydney Opera House
          - CN Tower
          - Hubble Space Telescope
          - University of Sankore
          - Petra
          - Great Firewall
          - Scrivener's Office
          - Printing Press
          - Palace of Culture and Science
          - Empire State Building
          - Grand Canal
          - Olympic Village
          - United Nations
          - Consulate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Celestial Throne
          - Civilized Jewelers Headquarters
        
        ### Mumbai
        - ID: 1214
        - X: 31
        - Y: 39
        - Population: 28
        - MajorityReligion: Hinduism
        - DefenseStrength: 97
        - IsCoastal: true
        - Wonders:
          - Imperial College
        
        ### Vijayanagara
        - ID: 1259
        - X: 21
        - Y: 39
        - Population: 31
        - MajorityReligion: Hinduism
        - DefenseStrength: 109
        - IsCoastal: true
        
        ### Pataliputra
        - ID: 1375
        - X: 28
        - Y: 33
        - Population: 29
        - MajorityReligion: Hinduism
        - DefenseStrength: 109
        - Wonders:
          - Chartered Company
          - Royal Collection
          - National Intelligence Agency
          - Grand Temple
          - Foreign Bureau
        
        ### Varanasi
        - ID: 1683
        - X: 17
        - Y: 36
        - Population: 31
        - MajorityReligion: Hinduism
        - DefenseStrength: 99
        - IsCoastal: true
        - Wonders:
          - National Monument
        
        ### Agra
        - ID: 2236
        - X: 15
        - Y: 29
        - Population: 30
        - MajorityReligion: Hinduism
        - DefenseStrength: 99
        - IsCoastal: true
        - Wonders:
          - Louvre
        
        ### Calcutta
        - ID: 2674
        - X: 19
        - Y: 45
        - Population: 28
        - MajorityReligion: Hinduism
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Lahore
        - ID: 2924
        - X: 14
        - Y: 46
        - Population: 27
        - MajorityReligion: Hinduism
        - DefenseStrength: 103
        - IsCoastal: true
        
        ### Bangalore
        - ID: 3247
        - X: 11
        - Y: 43
        - Population: 26
        - MajorityReligion: Hinduism
        - DefenseStrength: 102
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
        
        ### Madurai
        - ID: 3474
        - X: 8
        - Y: 39
        - Population: 28
        - MajorityReligion: Hinduism
        - DefenseStrength: 104
        - IsCoastal: true
        
        ### Ahmedabad
        - ID: 3786
        - X: 15
        - Y: 41
        - Population: 26
        - MajorityReligion: Hinduism
        - DefenseStrength: 72
        - IsCoastal: true
        - Wonders:
          - Cristo Redentor
        
        ### Hilo
        - ID: 8404
        - X: 35
        - Y: 27
        - Population: 24
        - MajorityReligion: Hinduism
        - DefenseStrength: 75
        - IsPuppet: true
        - IsCoastal: true
        
        ### Hyderabad
        - ID: 15178
        - X: 43
        - Y: 32
        - Population: 15
        - DefenseStrength: 99
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: The Iroquois
        
        ### Onondaga
        - ID: 1062
        - X: 29
        - Y: 24
        - Population: 42
        - DefenseStrength: 73
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Ironworks
          - Imperial College
          - Great Library
          - Temple of Artemis
          - Scrivener's Office
          - Printing Press
          - Palace of Culture and Science
          - Royal Astrologer
        
        ### Osininka
        - ID: 1433
        - X: 26
        - Y: 29
        - Population: 22
        - DefenseStrength: 95
        - Wonders:
          - Heroic Epic
          - National Monument
          - Royal Collection
          - Grand Temple
          - Trader Sid's Headquarters
        
        ### Grand River
        - ID: 1729
        - X: 32
        - Y: 19
        - Population: 28
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Akwesasme
        - ID: 2130
        - X: 19
        - Y: 28
        - Population: 17
        - MajorityReligion: Protestantism
        - DefenseStrength: 66
        - Health: 60%
        - IsCoastal: true
        
        ### Buffalo Creek
        - ID: 2351
        - X: 21
        - Y: 23
        - Population: 26
        - MajorityReligion: Hinduism
        - DefenseStrength: 80
        - IsCoastal: true
        - Wonders:
          - Chartered Company
        
        ### Brantford
        - ID: 2649
        - X: 26
        - Y: 20
        - Population: 28
        - DefenseStrength: 66
        - IsCoastal: true
        - Wonders:
          - National Intelligence Agency
        
        ### Montreal
        - ID: 5690
        - X: 29
        - Y: 15
        - Population: 24
        - DefenseStrength: 73
        - IsCoastal: true
        
        ### Tahiti
        - ID: 9387
        - X: 37
        - Y: 22
        - Population: 19
        - DefenseStrength: 68
        - Health: 93%
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: Venice
        
        ### Venice
        - ID: 1063
        - X: 56
        - Y: 36
        - Population: 29
        - DefenseStrength: 64
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Chartered Company
          - Scrivener's Office
          - Printing Press
          - Piazza San Marco
          - Rialto District
          - Consulate
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Cattaro
        - ID: 1505
        - X: 53
        - Y: 40
        - Population: 27
        - MajorityReligion: Protestantism
        - DefenseStrength: 73
        - IsPuppet: true
        - IsCoastal: true
        
        ### Corfu
        - ID: 2359
        - X: 55
        - Y: 43
        - Population: 27
        - DefenseStrength: 72
        - IsPuppet: true
        - IsCoastal: true
        
        ### Essaouira
        - ID: 2528
        - X: 54
        - Y: 30
        - Population: 25
        - DefenseStrength: 66
        - IsPuppet: true
        - IsCoastal: true
        
        ### La Venta
        - ID: 9226
        - X: 61
        - Y: 42
        - Population: 25
        - DefenseStrength: 72
        - IsPuppet: true
        - IsCoastal: true
        
        ### Prague
        - ID: 12000
        - X: 70
        - Y: 33
        - Population: 26
        - DefenseStrength: 70
        - IsPuppet: true
        - IsCoastal: true
        
        ### Shanghai
        - ID: 12704
        - X: 57
        - Y: 26
        - Population: 20
        - DefenseStrength: 70
        - IsPuppet: true
        
        ### Salem
        - ID: 13088
        - X: 34
        - Y: 31
        - Population: 22
        - MajorityReligion: Protestantism
        - DefenseStrength: 75
        - IsPuppet: true
        - IsCoastal: true
        
        ### Djenne
        - ID: 13338
        - X: 50
        - Y: 28
        - Population: 18
        - DefenseStrength: 72
        - IsPuppet: true
        
        ## Player: Morocco
        
        ### Marrakech
        - ID: 1064
        - X: 62
        - Y: 20
        - Population: 44
        - MajorityReligion: Islam
        - DefenseStrength: 87
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Royal Collection
          - Hanging Gardens
          - Palace of Westminster
          - Brandenburg Gate
          - Printing Press
          - Foreign Bureau
          - Palace of Culture and Science
          - Karlstejn
          - Royal Guardhouse
          - Royal Astrologer
          - Holy Council
        
        ### Rabat
        - ID: 1218
        - X: 60
        - Y: 15
        - Population: 25
        - MajorityReligion: Islam
        - DefenseStrength: 64
        - Wonders:
          - School of Philosophy
          - Ironworks
          - Imperial College
          - Scrivener's Office
        
        ### Fes
        - ID: 1596
        - X: 61
        - Y: 24
        - Population: 25
        - MajorityReligion: Islam
        - DefenseStrength: 72
        - IsCoastal: true
        
        ### Casablanca
        - ID: 1874
        - X: 64
        - Y: 14
        - Population: 28
        - DefenseStrength: 70
        - Wonders:
          - Grand Temple
          - Hexxon Refineries Headquarters
        
        ### Tangier
        - ID: 5272
        - X: 67
        - Y: 36
        - Population: 24
        - MajorityReligion: Islam
        - DefenseStrength: 72
        - IsCoastal: true
        
        ### Sale
        - ID: 8521
        - X: 66
        - Y: 41
        - Population: 23
        - MajorityReligion: Islam
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Ouarzazate
        - ID: 10966
        - X: 64
        - Y: 32
        - Population: 21
        - DefenseStrength: 80
        - IsCoastal: true
        
        ### Takuu
        - ID: 14798
        - X: 51
        - Y: 34
        - Population: 18
        - MajorityReligion: Islam
        - DefenseStrength: 70
        - IsOccupied: true
        
        ### Attila's Court
        - ID: 16833
        - X: 48
        - Y: 39
        - Population: 22
        - DefenseStrength: 50
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Terracotta Army
        
        ## Player: City-States
        
        ### Ragusa
        - ID: 1065
        - X: 50
        - Y: 4
        - Population: 14
        - MajorityReligion: Buddhism
        - DefenseStrength: 100
        - IsCoastal: true
        
        ### Heidabir
        - ID: 1066
        - X: 59
        - Y: 8
        - Population: 13
        - DefenseStrength: 96
        
        ### Antananarivo
        - ID: 1069
        - X: 69
        - Y: 22
        - Population: 17
        - DefenseStrength: 105
        - IsCoastal: true
        
        ### Seoul
        - ID: 1072
        - X: 20
        - Y: 34
        - Population: 21
        - MajorityReligion: Hinduism
        - DefenseStrength: 92
        
        ### Brussels
        - ID: 1073
        - X: 12
        - Y: 35
        - Population: 21
        - MajorityReligion: Hinduism
        - DefenseStrength: 90
        - IsCoastal: true
        
        ### Lhasa
        - ID: 1074
        - X: 6
        - Y: 45
        - Population: 23
        - MajorityReligion: Hinduism
        - DefenseStrength: 79
        - IsCoastal: true
        
        ### Kyiv
        - ID: 1077
        - X: 60
        - Y: 3
        - Population: 11
        - DefenseStrength: 97
        
        ### Buenos Aires
        - ID: 1079
        - X: 25
        - Y: 45
        - Population: 23
        - MajorityReligion: Hinduism
        - DefenseStrength: 90
        - IsCoastal: true
        
        ### Mombasa
        - ID: 1080
        - X: 73
        - Y: 7
        - Population: 20
        - MajorityReligion: Catholicism
        - DefenseStrength: 70
        - IsCoastal: true
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - CityBombard:
          - Rocket Artillery:
            - Strength: 37
            - RangedStrength: 75
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
        - FastAttack:
          - Tank:
            - Strength: 75
          - Landship:
            - Strength: 60
        - Defense:
          - Infantry:
            - Strength: 62
          - Rifleman:
            - Strength: 50
        - Counter:
          - Anti-Aircraft Gun:
            - Strength: 40
        - Ranged:
          - Light Tank:
            - Strength: 58
            - RangedStrength: 52
          - Machine Gun:
            - Strength: 45
            - RangedStrength: 58
          - Berber Cavalry:
            - Strength: 42
            - RangedStrength: 34
        - AttackSea:
          - Fleet Destroyer:
            - Strength: 80
        - AssaultSea:
          - Battleship:
            - Strength: 60
            - RangedStrength: 75
          - Attack Submarine:
            - Strength: 50
            - RangedStrength: 72
        - AttackAir:
          - Heavy Bomber:
            - RangedStrength: 65
          - Bomber:
            - RangedStrength: 50
        - DefenseAir:
          - Triplane:
            - RangedStrength: 45
        
        ## Friendly Land Zone 1059
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 621
        - NeutralStrength: 229
        - FriendlyStrength: 6327
        - City: Amsterdam
        - AreaID: 5
        - Plots: 24
        - CenterX: 49
        - CenterY: 10
        - Units:
          - The Netherlands:
            - Artillery: 1
            - Anti-Aircraft Gun: 3
            - Light Tank: 1
            - Machine Gun: 5
        - Neighbors:
          - -1199
          - 1199
          - 1065
          - 1515
          - 1346
        
        ## Enemy Land Zone 1060
        - ZoneValue: 72
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 4243
        - NeutralStrength: 97
        - FriendlyStrength: 635
        - City: Moson Kahni
        - AreaID: 5
        - Plots: 17
        - CenterX: 47
        - CenterY: 22
        - Units:
          - The Shoshone:
            - Artillery: 1
            - Triplane: 1
            - Machine Gun: 7
        - Neighbors:
          - -1060
          - 1761
          - -1199
          - 1199
          - 1308
          - 13338
        
        ## Neutral Land Zone 1061
        - ZoneValue: 66
        - Dominance: Even
        - EnemyStrength: 140
        - NeutralStrength: 1064
        - City: Delhi
        - AreaID: 38
        - Plots: 23
        - CenterX: 26
        - CenterY: 38
        - Units:
          - India:
            - Rocket Artillery: 1
            - Heavy Bomber: 1
            - Anti-Aircraft Gun: 1
            - Triplane: 1
            - Bomber: 4
        - Neighbors:
          - -1079
        
        ## Neutral Land Zone 1062
        - ZoneValue: 36
        - NeutralStrength: 1089
        - City: Onondaga
        - AreaID: 38
        - Plots: 19
        - CenterX: 28
        - CenterY: 24
        - Units:
          - The Iroquois:
            - Anti-Aircraft Gun: 1
            - Machine Gun: 3
        - Neighbors:
          - 1433
          - -1062
        
        ## Neutral Land Zone 1063
        - ZoneValue: 24
        - Dominance: Enemy
        - EnemyStrength: 548
        - NeutralStrength: 559
        - City: Venice
        - AreaID: 5
        - Plots: 12
        - CenterX: 55
        - CenterY: 36
        - Units:
          - Venice:
            - Machine Gun: 1
        - Neighbors:
          - -1063
        
        ## Enemy Land Zone 1064
        - ZoneValue: 24
        - Dominance: Enemy
        - EnemyStrength: 5350
        - NeutralStrength: 424
        - City: Marrakech
        - AreaID: 5
        - Plots: 19
        - CenterX: 62
        - CenterY: 19
        - Units:
          - Polynesia:
            - Artillery: 1
          - Morocco:
            - Anti-Aircraft Gun: 1
            - Machine Gun: 1
        - Neighbors:
          - 1459
          - 1218
          - 1596
        
        ## Neutral Land Zone 1065
        - ZoneValue: 9
        - Dominance: Friendly
        - NeutralStrength: 482
        - FriendlyStrength: 959
        - City: Ragusa
        - AreaID: 5
        - Plots: 29
        - CenterX: 51
        - CenterY: 4
        - Units:
          - City-State Ragusa:
            - Artillery: 1
            - Infantry: 1
        - Neighbors:
          - -1065
          - 1059
          - 1515
          - 1077
          - 1066
        
        ## Neutral Land Zone 1066
        - ZoneValue: 9
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 2487
        - NeutralStrength: 459
        - FriendlyStrength: 2046
        - City: Heidabir
        - AreaID: 5
        - Plots: 47
        - CenterX: 59
        - CenterY: 8
        - Units:
          - The Netherlands:
            - Machine Gun: 1
          - City-State Heidabir:
            - Machine Gun: 2
          - Morocco:
            - Berber Cavalry: 1
          - City-State Ragusa:
            - Machine Gun: 1
        - Neighbors:
          - 1065
          - 1515
          - 1077
          - 8438
          - 1218
        
        ## Neutral Land Zone 1077
        - ZoneValue: 12
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 210
        - NeutralStrength: 369
        - FriendlyStrength: 924
        - City: Kyiv
        - AreaID: 5
        - Plots: 34
        - CenterX: 61
        - CenterY: 4
        - Units:
          - The Netherlands:
            - Artillery: 1
            - Anti-Aircraft Gun: 3
          - City-State Kyiv:
            - Light Tank: 1
            - Machine Gun: 1
        - Neighbors:
          - 1065
          - 1066
        
        ## Friendly Land Zone 1199
        - ZoneValue: 30
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 2886
        - FriendlyStrength: 5103
        - City: Rotterdam
        - AreaID: 5
        - Plots: 14
        - CenterX: 48
        - CenterY: 15
        - Units:
          - The Netherlands:
            - Artillery: 1
            - Anti-Aircraft Gun: 1
            - Rifleman: 1
            - Triplane: 1
            - Machine Gun: 5
            - Attack Submarine: 1
          - The Shoshone:
            - Infantry: 1
        - Neighbors:
          - -1199
          - 1059
          - 1060
          - 1346
        
        ## Enemy Land Zone 1218
        - ZoneValue: 30
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 6664
        - NeutralStrength: 271
        - FriendlyStrength: 475
        - City: Rabat
        - AreaID: 5
        - Plots: 25
        - CenterX: 60
        - CenterY: 15
        - Units:
          - Polynesia:
            - Light Tank: 1
          - Morocco:
            - Artillery: 2
        - Neighbors:
          - 8438
          - 1066
          - 1459
          - 1064
        
        ## Enemy Land Zone 1308
        - ZoneValue: 60
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 5718
        - NeutralStrength: 176
        - FriendlyStrength: 2472
        - City: Te-Moak
        - AreaID: 5
        - Plots: 29
        - CenterX: 51
        - CenterY: 21
        - Units:
          - The Shoshone:
            - Artillery: 1
            - Infantry: 2
            - Triplane: 2
            - Bomber: 1
            - Machine Gun: 4
        - Neighbors:
          - 1060
          - 1346
          - 13338
          - 1459
        
        ## Friendly Land Zone 1346
        - ZoneValue: 120
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 4932
        - FriendlyStrength: 6317
        - City: Utrecht
        - AreaID: 5
        - Plots: 22
        - CenterX: 51
        - CenterY: 16
        - Units:
          - The Netherlands:
            - Artillery: 1
            - Anti-Aircraft Gun: 1
            - Rifleman: 1
            - Triplane: 1
            - Bomber: 1
            - Machine Gun: 8
          - The Shoshone:
            - Infantry: 2
        - Neighbors:
          - 1199
          - 1308
          - 1059
          - 8438
        
        ## Neutral Land Zone 1433
        - ZoneValue: 12
        - NeutralStrength: 1471
        - City: Osininka
        - AreaID: 38
        - Plots: 31
        - CenterX: 26
        - CenterY: 29
        - Units:
          - The Iroquois:
            - Machine Gun: 3
        - Neighbors:
          - 1062
          - -1062
        
        ## Enemy Land Zone 1459
        - ZoneValue: 60
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 7527
        - NeutralStrength: 444
        - FriendlyStrength: 777
        - City: Agaidika
        - AreaID: 5
        - Plots: 28
        - CenterX: 56
        - CenterY: 20
        - Units:
          - The Shoshone:
            - Artillery: 1
            - Infantry: 1
            - Bomber: 3
            - Machine Gun: 6
          - Morocco:
            - Anti-Aircraft Gun: 2
            - Infantry: 1
            - Machine Gun: 1
        - Neighbors:
          - 1308
          - 8438
          - 1218
          - 1064
          - 1596
        
        ## Friendly Land Zone 1515
        - ZoneValue: 36
        - Dominance: Friendly
        - Posture: Counterattack
        - EnemyStrength: 1284
        - NeutralStrength: 500
        - FriendlyStrength: 5341
        - City: Groningen
        - AreaID: 5
        - Plots: 29
        - CenterX: 54
        - CenterY: 8
        - Units:
          - The Netherlands:
            - Anti-Aircraft Gun: 1
            - Rifleman: 1
            - Machine Gun: 4
        - Neighbors:
          - 1059
          - 1065
          - 8438
          - 1066
        
        ## Enemy Land Zone 1596
        - ZoneValue: 15
        - Dominance: Enemy
        - EnemyStrength: 3241
        - NeutralStrength: 669
        - City: Fes
        - AreaID: 5
        - Plots: 12
        - CenterX: 60
        - CenterY: 24
        - Units:
          - Morocco:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 1459
          - 1064
        
        ## Enemy Land Zone 1761
        - ZoneValue: 24
        - Dominance: Enemy
        - EnemyStrength: 2384
        - NeutralStrength: 256
        - City: Goshute
        - AreaID: 5
        - Plots: 15
        - CenterX: 45
        - CenterY: 27
        - Units:
          - The Shoshone:
            - Artillery: 2
            - Machine Gun: 3
        - Neighbors:
          - 1060
          - 13338
        
        ## Enemy Land Zone 5085
        - ZoneValue: 24
        - Dominance: Enemy
        - EnemyStrength: 660
        - City: Aotearoa
        - AreaID: 84
        - Plots: 19
        - CenterX: 69
        - CenterY: 44
        - Units:
          - Polynesia:
            - Infantry: 1
        
        ## Friendly Land Zone 8438
        - ZoneValue: 96
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 6190
        - NeutralStrength: 226
        - FriendlyStrength: 5167
        - City: Vancouver
        - AreaID: 5
        - Plots: 33
        - CenterX: 55
        - CenterY: 14
        - Units:
          - The Netherlands:
            - Anti-Aircraft Gun: 3
            - Landship: 1
            - Machine Gun: 2
          - Morocco:
            - Tank: 3
            - Infantry: 2
            - Berber Cavalry: 1
          - Polynesia:
            - Artillery: 1
            - Landship: 1
        - Neighbors:
          - 1346
          - 1515
          - 1459
          - 1066
          - 1218
        
        ## Neutral Land Zone 13338
        - ZoneValue: 9
        - Dominance: Enemy
        - EnemyStrength: 3090
        - NeutralStrength: 381
        - City: Djenne
        - AreaID: 5
        - Plots: 37
        - CenterX: 49
        - CenterY: 28
        - Units:
          - The Shoshone:
            - Artillery: 1
        - Neighbors:
          - 1761
          - 1060
          - 1308
        
        ## Neutral Sea Zone -100005
        - ZoneValue: 1
        - NeutralStrength: 184
        - AreaID: 0
        - Plots: 14
        - CenterX: 43
        - CenterY: 3
        - Units:
          - City-State Ragusa:
            - Fleet Destroyer: 1
        - Neighbors:
          - -1065
        
        ## Friendly Sea Zone -1199
        - ZoneValue: 40
        - Dominance: Even
        - Posture: Counterattack
        - EnemyStrength: 2929
        - FriendlyStrength: 2969
        - City: Rotterdam
        - AreaID: 0
        - Plots: 25
        - CenterX: 45
        - CenterY: 15
        - Units:
          - Polynesia:
            - Fleet Destroyer: 3
        - Neighbors:
          - -6625
          - -1060
          - 1059
          - 1199
          - 1060
        
        ## Neutral Sea Zone -1065
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 670
        - FriendlyStrength: 384
        - City: Ragusa
        - AreaID: 0
        - Plots: 38
        - CenterX: 48
        - CenterY: 3
        - Units:
          - City-State Ragusa:
            - Fleet Destroyer: 1
        - Neighbors:
          - -100005
          - 1065
        
        ## Neutral Sea Zone -1063
        - ZoneValue: 8
        - Dominance: Enemy
        - EnemyStrength: 856
        - NeutralStrength: 213
        - City: Venice
        - AreaID: 62
        - Plots: 22
        - CenterX: 58
        - CenterY: 35
        - Units:
          - Morocco:
            - Fleet Destroyer: 1
        - Neighbors:
          - 1063
          - -9226
        
        ## Neutral Sea Zone -1062
        - ZoneValue: 1
        - NeutralStrength: 567
        - City: Onondaga
        - AreaID: 0
        - Plots: 13
        - CenterX: 31
        - CenterY: 25
        - Units:
          - The Iroquois:
            - Machine Gun: 1
        - Neighbors:
          - 1062
          - 1433
        
        ## Enemy Sea Zone -6625
        - ZoneValue: 2
        - Dominance: Enemy
        - EnemyStrength: 1715
        - NeutralStrength: 340
        - City: Washakie
        - AreaID: 0
        - Plots: 30
        - CenterX: 39
        - CenterY: 16
        - Units:
          - Polynesia:
            - Fleet Destroyer: 2
        - Neighbors:
          - -1199
          - -1060
        
        ## Enemy Sea Zone -1060
        - ZoneValue: 24
        - Dominance: Enemy
        - Posture: Withdraw
        - EnemyStrength: 3772
        - NeutralStrength: 223
        - FriendlyStrength: 380
        - City: Moson Kahni
        - AreaID: 0
        - Plots: 23
        - CenterX: 44
        - CenterY: 20
        - Units:
          - Polynesia:
            - Battleship: 1
            - Fleet Destroyer: 3
        - Neighbors:
          - -6625
          - -1199
          - 1060
        
        ## Neutral Sea Zone -1079
        - ZoneValue: 1
        - NeutralStrength: 1122
        - City: Buenos Aires
        - AreaID: 107
        - Plots: 55
        - CenterX: 26
        - CenterY: 46
        - Units:
          - India:
            - Fleet Destroyer: 1
        - Neighbors:
          - 1061
        
        ## Neutral Sea Zone -9226
        - ZoneValue: 1
        - Dominance: Enemy
        - EnemyStrength: 743
        - NeutralStrength: 263
        - City: La Venta
        - AreaID: 40
        - Plots: 20
        - CenterX: 60
        - CenterY: 39
        - Units:
          - Morocco:
            - Fleet Destroyer: 1
        - Neighbors:
          - -1063
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 401
        
        ### 0
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Inquisitor
          - ID: 17233
        - Player: 3: The Shoshone
        - Grass Land 46,22:
          - Owner: The Shoshone
          - CityID: 1060
          - Population: 39
          - IsRiver: true
          - City: Moson Kahni
          - Religion: Protestantism
          - Route: Railroad
        
        ### 1
        - Type: UnitCreated
        - UnitType: Inquisitor
        - Player: 3: The Shoshone
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 17233
        - Grass Land 46,22:
          - Owner: The Shoshone
          - CityID: 1060
          - Population: 39
          - IsRiver: true
          - City: Moson Kahni
          - Religion: Protestantism
          - Route: Railroad
        
        ### 2
        - Type: CityTrained
        - WithFaith: true
        - Player: 3: The Shoshone
        - City:
          - Name: Moson Kahni
          - Population: 39
          - ID: 1060
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 17233
        
        ### 3
        - Type: CityBeginsWLTKD
        - Change: 10
        - City:
          - Owner: The Shoshone
          - CityID: 1308
          - Population: 29
          - IsRiver: true
          - City: Te-Moak
          - Terrain: Plains
          - Route: Railroad
          - Plot: Land
          - X: 51
          - Y: 21
        - Player: 3: The Shoshone
        
        ### 4
        - Type: SetPopulation
        - OldPopulation: 29
        - NewPopulation: 30
        - City:
          - Owner: The Shoshone
          - CityID: 1308
          - Population: 30
          - IsRiver: true
          - City: Te-Moak
          - Terrain: Plains
          - Route: Railroad
          - Plot: Land
          - X: 51
          - Y: 21
        
        ### 5
        - Type: CityConvertsReligion
        - City:
          - Owner: The Shoshone
          - CityID: 1308
          - Population: 30
          - IsRiver: true
          - City: Te-Moak
          - Terrain: Plains
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 51
          - Y: 21
        - Owner: 3: The Shoshone
        - Religion: Protestantism
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Ambassador
          - ID: 17234
        - Player: 3: The Shoshone
        - Plains Land 56,21:
          - Owner: The Shoshone
          - CityID: 1459
          - Population: 29
          - IsRiver: true
          - City: Agaidika
          - Religion: Protestantism
          - Route: Railroad
        
        ### 7
        - Type: UnitCreated
        - UnitType: Ambassador
        - Player: 3: The Shoshone
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 17234
        - Plains Land 56,21:
          - Owner: The Shoshone
          - CityID: 1459
          - Population: 29
          - IsRiver: true
          - City: Agaidika
          - Religion: Protestantism
          - Route: Railroad
        
        ### 8
        - Type: CityTrained
        - Player: 3: The Shoshone
        - City:
          - Name: Agaidika
          - Population: 29
          - ID: 1459
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 17234
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Infantry
          - ID: 17235
        - Player: 3: The Shoshone
        - Grass Land 45,26:
          - Owner: The Shoshone
          - Improvement: Encampment
          - Route: Railroad
        
        ### 10
        - Type: UnitCreated
        - UnitType: Infantry
        - Player: 3: The Shoshone
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Infantry
          - ID: 17235
        - Grass Land 45,26:
          - Owner: The Shoshone
          - Improvement: Encampment
          - Route: Railroad
        
        ### 11
        - Type: CityTrained
        - Player: 3: The Shoshone
        - City:
          - Name: Goshute
          - Population: 26
          - ID: 1761
        - Unit:
          - Level: 1
          - AI: Defense
          - Unit: Infantry
          - ID: 17235
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17169
        - Player: 3: The Shoshone
        - Plots:
          - Grass Hills 56,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Hills 57,22:
            - Owner: The Shoshone
            - Resource: Jade
            - Improvement: Quarry
            - Route: Road
          - Grass Land 58,22:
            - Owner: The Shoshone
            - Resource: Rice
            - Improvement: Holy Site
          - Grass Land 59,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Pasture
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17170
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 45,28:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Land 44,29:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Grass Hills 44,30:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Road
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16126
        - Player: 3: The Shoshone
        - Plots:
          - Plains Land 57,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Road
          - Plains Land 58,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
          - Plains Land 59,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Farm
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16941
        - Player: 3: The Shoshone
        - Plots:
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Plains Land 49,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Land 50,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 51,21:
            - Owner: The Shoshone
            - CityID: 1308
            - Population: 30
            - IsRiver: true
            - City: Te-Moak
            - Religion: Protestantism
            - Route: Railroad
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16521
        - Player: 3: The Shoshone
        - Plots:
          - Plains Land 52,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Land 53,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Maize
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Hills 54,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 55,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Hills 56,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 56,21:
            - Owner: The Shoshone
            - CityID: 1459
            - Population: 29
            - IsRiver: true
            - City: Agaidika
            - Religion: Protestantism
            - Route: Railroad
        
        ### 17
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15415
        - Player: 3: The Shoshone
        - Plots:
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Grass Land 46,22:
            - Owner: The Shoshone
            - CityID: 1060
            - Population: 39
            - IsRiver: true
            - City: Moson Kahni
            - Religion: Protestantism
            - Route: Railroad
        
        ### 18
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 3: The Shoshone
        - DestinationCity:
          - Name: Shanghai
          - Population: 20
          - ID: 12704
        - DestinationPlayer: 6: Venice
        - OriginCity:
          - Name: Moson Kahni
          - Population: 39
          - ID: 1060
        - Connection: Food
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 17237
        - Player: 3: The Shoshone
        - Grass Land 46,22:
          - Owner: The Shoshone
          - CityID: 1060
          - Population: 39
          - IsRiver: true
          - City: Moson Kahni
          - Religion: Protestantism
          - Route: Railroad
        
        ### 20
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 3: The Shoshone
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17237
        - Grass Land 46,22:
          - Owner: The Shoshone
          - CityID: 1060
          - Population: 39
          - IsRiver: true
          - City: Moson Kahni
          - Religion: Protestantism
          - Route: Railroad
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15853
        - Player: 3: The Shoshone
        - Plots:
          - Plains Land 57,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Road
          - Plains Land 56,21:
            - Owner: The Shoshone
            - CityID: 1459
            - Population: 29
            - IsRiver: true
            - City: Agaidika
            - Religion: Protestantism
            - Route: Railroad
          - Grass Hills 56,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 55,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 22
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Infantry
          - ID: 17235
        - Player: 3: The Shoshone
        - Promotions:
          - Shock I
          - Shock II
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13605
        - Player: 3: The Shoshone
        - Plots:
          - Plains Land 53,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Maize
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 52,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Land 51,21:
            - Owner: The Shoshone
            - CityID: 1308
            - Population: 30
            - IsRiver: true
            - City: Te-Moak
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 51,20:
            - Owner: The Shoshone
            - Resource: Aluminum
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Hills 50,20:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 49,19:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 48,19:
            - Owner: The Shoshone
            - Resource: Sheep
            - Route: Railroad
          - Plains Hills 47,19:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Feature: Forest
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13760
        - Player: 3: The Shoshone
        - Plots:
          - Plains Land 49,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Land 48,20:
            - Owner: The Shoshone
            - Resource: Cattle
            - Improvement: Manufactory
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13660
        - Player: 3: The Shoshone
        - Plains Hills 49,20:
          - Owner: The Shoshone
          - Resource: Marble
          - Improvement: Quarry
          - Route: Railroad
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: CityBombard
          - Unit: Artillery
          - ID: 16934
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Plains Land 49,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 50,20:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
        
        ### 27
        - Type: CombatResult
        - Plains Hills 49,17:
          - Owner: The Netherlands
          - Improvement: Fort
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Player: 2: The Netherlands
          - Unit:
            - Level: 4
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 16998
        
        ### 28
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 16459
        - Player: 3: The Shoshone
        - Plots:
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 49,20:
            - Owner: The Shoshone
            - Resource: Marble
            - Improvement: Quarry
            - Route: Railroad
          - Desert Hills 48,19:
            - Owner: The Shoshone
            - Resource: Sheep
            - Route: Railroad
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 15231
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 44,27:
            - Owner: The Shoshone
            - CityID: 1761
            - Population: 26
            - City: Goshute
            - Resource: Rice
            - Religion: Protestantism
            - Route: Railroad
          - Grass Land 45,26:
            - Owner: The Shoshone
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 45,25:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 46,24:
            - Owner: The Shoshone
            - Improvement: Village
            - Route: Railroad
          - Plains Land 46,23:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 49,20:
            - Owner: The Shoshone
            - Resource: Marble
            - Improvement: Quarry
            - Route: Railroad
          - Plains Hills 49,19:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 50,18:
            - Owner: The Shoshone
            - Resource: Amber
            - Improvement: Quarry
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 10206
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 49,20:
            - Owner: The Shoshone
            - Resource: Marble
            - Improvement: Quarry
            - Route: Railroad
          - Desert Hills 48,19:
            - Owner: The Shoshone
            - Resource: Sheep
            - Route: Railroad
          - Grass Land 46,22:
            - Owner: The Shoshone
            - CityID: 1060
            - Population: 39
            - IsRiver: true
            - City: Moson Kahni
            - Religion: Protestantism
            - Route: Railroad
        
        ### 31
        - Type: CombatResult
        - Plains Hills 52,15:
          - Owner: The Netherlands
          - Improvement: Manufactory
        - Attacker:
          - RemainingHP: 24
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 2: The Netherlands
          - Unit:
            - Level: 4
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 16799
        
        ### 32
        - Type: CombatResult
        - Plains Hills 52,15:
          - Owner: The Netherlands
          - Improvement: Manufactory
        - Attacker:
          - RemainingHP: 10
          - Damage: 56
        - Defender:
          - RemainingHP: 27
          - Damage: 27
          - Player: 2: The Netherlands
          - Unit:
            - Level: 4
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 15920
        
        ### 33
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Artillery
          - ID: 17059
        - Player: 3: The Shoshone
        - Plots:
          - Plains Hills 56,19:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Desert Land 55,19:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13840
        - Player: 3: The Shoshone
        - Plots:
          - Plains Hills 54,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 53,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Maize
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 52,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Land 51,21:
            - Owner: The Shoshone
            - CityID: 1308
            - Population: 30
            - IsRiver: true
            - City: Te-Moak
            - Religion: Protestantism
            - Route: Railroad
          - Grass Land 50,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 35
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 44%
          - AI: Defense
          - Unit: Infantry
          - ID: 16649
        - Player: 3: The Shoshone
        - Plots:
          - Plains Land 54,17:
            - Owner: The Shoshone
            - IsRiver: true
            - Route: Road
          - Plains Land 55,18:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
        
        ### 36
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13839
        - Player: 3: The Shoshone
        - Plots:
          - Plains Hills 56,19:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 57,18:
            - Owner: The Shoshone
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16874
        - Player: 3: The Shoshone
        - Plots:
          - Plains Land 51,21:
            - Owner: The Shoshone
            - CityID: 1308
            - Population: 30
            - IsRiver: true
            - City: Te-Moak
            - Religion: Protestantism
            - Route: Railroad
          - Plains Land 52,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Land 53,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Maize
            - Improvement: Holy Site
            - Route: Railroad
          - Grass Land 53,21:
            - Owner: The Shoshone
            - Resource: Horses
            - Improvement: Pasture
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14755
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 47,21:
            - Owner: The Shoshone
            - Resource: Cattle
            - Improvement: Academy
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14681
        - Player: 3: The Shoshone
        - Grass Land 46,21:
          - Owner: The Shoshone
          - Resource: Iron
          - Improvement: Academy
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13981
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Plains Land 49,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16938
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 45,26:
            - Owner: The Shoshone
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 45,25:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 46,24:
            - Owner: The Shoshone
            - Improvement: Village
            - Route: Railroad
          - Plains Land 46,23:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Hills 48,23:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Feature: Forest
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Artillery
          - ID: 14620
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 46,25:
            - Owner: The Shoshone
            - Improvement: Encampment
          - Grass Hills 47,25:
            - Owner: The Shoshone
            - Improvement: Mine
        
        ### 43
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Artillery
          - ID: 14754
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 47,27:
            - Owner: The Shoshone
            - Improvement: Encampment
          - Grass Hills 48,26:
            - Owner: The Shoshone
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 92%
          - AI: Defense
          - Unit: Infantry
          - ID: 15713
        - Player: 3: The Shoshone
        - Plots:
          - Plains Land 53,19:
            - Owner: The Shoshone
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 52,19:
            - Owner: The Shoshone
            - Resource: Amber
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 52,18:
            - Owner: The Shoshone
            - Improvement: Encampment
            - Route: Road
        
        ### 45
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Infantry
          - ID: 17235
        - Player: 3: The Shoshone
        - Plots:
          - Plains Hills 45,25:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 46,24:
            - Owner: The Shoshone
            - Improvement: Village
            - Route: Railroad
          - Plains Land 46,23:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Plains Land 49,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 50,20:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 50,19:
            - Owner: The Shoshone
            - Route: Railroad
        
        ### 46
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 17000
        - Player: 3: The Shoshone
        - Grass Land 45,28:
          - Owner: The Shoshone
          - IsRiver: true
          - Improvement: Encampment
          - Route: Railroad
        
        ### 47
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 80%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16125
        - Player: 3: The Shoshone
        - Plots:
          - Plains Hills 49,20:
            - Owner: The Shoshone
            - Resource: Marble
            - Improvement: Quarry
            - Route: Railroad
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Plains Land 46,23:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Hills 46,24:
            - Owner: The Shoshone
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 45,25:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Land 45,26:
            - Owner: The Shoshone
            - Improvement: Encampment
            - Route: Railroad
          - Grass Land 44,27:
            - Owner: The Shoshone
            - CityID: 1761
            - Population: 26
            - City: Goshute
            - Resource: Rice
            - Religion: Protestantism
            - Route: Railroad
        
        ### 48
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Prophet
          - Unit: Great Prophet
          - ID: 16584
        - Player: 3: The Shoshone
        - Coast 31,22:
          - Owner: The Iroquois
        
        ### 49
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15095
        - Player: 3: The Shoshone
        - Plots:
          - Grass Land 45,29:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 45,28:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Land 44,27:
            - Owner: The Shoshone
            - CityID: 1761
            - Population: 26
            - City: Goshute
            - Resource: Rice
            - Religion: Protestantism
            - Route: Railroad
          - Grass Land 45,26:
            - Owner: The Shoshone
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 45,25:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 46,24:
            - Owner: The Shoshone
            - Improvement: Village
            - Route: Railroad
          - Plains Land 46,23:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Grass Land 47,21:
            - Owner: The Shoshone
            - Resource: Cattle
            - Improvement: Academy
        
        ### 50
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 17234
        - Player: 3: The Shoshone
        - Plots:
          - Grass Hills 56,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 55,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 54,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 53,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Maize
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 52,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Land 51,21:
            - Owner: The Shoshone
            - CityID: 1308
            - Population: 30
            - IsRiver: true
            - City: Te-Moak
            - Religion: Protestantism
            - Route: Railroad
          - Grass Land 50,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 49,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Plains Land 46,23:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Grass Hills 46,24:
            - Owner: The Shoshone
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 45,25:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Land 45,26:
            - Owner: The Shoshone
            - Improvement: Encampment
            - Route: Railroad
          - Grass Land 44,27:
            - Owner: The Shoshone
            - CityID: 1761
            - Population: 26
            - City: Goshute
            - Resource: Rice
            - Religion: Protestantism
            - Route: Railroad
          - Coast 43,27:
            - Owner: The Shoshone
          - Ocean 42,27:
            - Owner: The Shoshone
          - Ocean 41,27:
            - Owner: The Shoshone
          - Ocean 40,27:
            - Owner: The Shoshone
          - Ocean 39,27:
            - Owner: The Shoshone
        
        ### 51
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17237
        - Player: 3: The Shoshone
        - Plains Land 51,21:
          - Owner: The Shoshone
          - CityID: 1308
          - Population: 30
          - IsRiver: true
          - City: Te-Moak
          - Religion: Protestantism
          - Route: Railroad
        
        ### 52
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17236
        - Player: 3: The Shoshone
        - Grass Land 46,22:
          - Owner: The Shoshone
          - CityID: 1060
          - Population: 39
          - IsRiver: true
          - City: Moson Kahni
          - Religion: Protestantism
          - Route: Railroad
        
        ### 53
        - Type: CityInvestedBuilding
        - BuildingClass: Spaceship Factory
        - Invested: true
        - City:
          - Name: Delhi
          - Population: 60
          - ID: 1061
        - Player: 4: India
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Great Scientist
          - ID: 17249
        - Player: 4: India
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 60
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 55
        - Type: UnitCreated
        - UnitType: Great Scientist
        - Player: 4: India
        - Unit:
          - Level: 1
          - AI: Scientist
          - Unit: Great Scientist
          - ID: 17249
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 60
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 56
        - Type: CityConstructed
        - City:
          - Name: Delhi
          - Population: 60
          - ID: 1061
        - Owner: 4: India
        - Building: Hubble Space Telescope
        
        ### 57
        - Type: SetPopulation
        - OldPopulation: 60
        - NewPopulation: 61
        - City:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 26
          - Y: 38
        
        ### 58
        - Type: CityConvertsReligion
        - City:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 26
          - Y: 38
        - Owner: 4: India
        - Religion: Hinduism
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16408
        - Player: 4: India
        - Plots:
          - Grass Land 28,36:
            - Owner: India
            - Improvement: Town
            - Route: Railroad
          - Grass Land 27,36:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 26,37:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 26,38:
            - Owner: India
            - CityID: 1061
            - Population: 61
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
        
        ### 60
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17022
        - Player: 4: India
        - Plots:
          - Plains Land 24,38:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Desert Hills 25,38:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 26,38:
            - Owner: India
            - CityID: 1061
            - Population: 61
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
          - Grass Land 26,37:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Grass Land 27,36:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 27,35:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
        
        ### 61
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15424
        - Player: 4: India
        - Plots:
          - Desert Hills 25,38:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 26,38:
            - Owner: India
            - CityID: 1061
            - Population: 61
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
          - Plains Land 24,38:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
        
        ### 62
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 4: India
        - DestinationCity:
          - Name: Vijayanagara
          - Population: 31
          - ID: 1259
        - DestinationPlayer: 4: India
        - OriginCity:
          - Name: Delhi
          - Population: 61
          - ID: 1061
        - Connection: Gold
        
        ### 63
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 17251
        - Player: 4: India
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 64
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 4: India
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17251
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16330
        - Player: 4: India
        - Plots:
          - Grass Land 26,37:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Grass Land 27,36:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 27,35:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 26,38:
            - Owner: India
            - CityID: 1061
            - Population: 61
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16468
        - Player: 4: India
        - Plots:
          - Plains Hills 26,38:
            - Owner: India
            - CityID: 1061
            - Population: 61
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
          - Desert Hills 25,38:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Land 24,38:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
        
        ### 67
        - Type: CombatResult
        - Grass Land 26,27:
          - Owner: The Iroquois
          - IsRiver: true
          - Resource: Sugar
          - Improvement: Academy
        - Attacker:
          - RemainingHP: 14
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 5: The Iroquois
          - Unit:
            - Level: 4
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 17191
        
        ### 68
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13709
        - Player: 4: India
        - Plots:
          - Grass Land 27,36:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 27,35:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 87%
          - AI: Defense
          - Unit: Infantry
          - ID: 16403
        - Player: 4: India
        - Plots:
          - Desert Hills 25,38:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 25,37:
            - Owner: India
            - Improvement: Mine
            - Route: Railroad
          - Grass Land 26,37:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Grass Land 27,36:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 27,35:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
        
        ### 70
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Artillery
          - ID: 13765
        - Player: 4: India
        - Grass Land 26,37:
          - Owner: India
          - Improvement: Village
          - Route: Railroad
        
        ### 71
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 64%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16892
        - Player: 4: India
        - Plots:
          - Grass Land 27,35:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Grass Land 27,36:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 26,37:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 26,38:
            - Owner: India
            - CityID: 1061
            - Population: 61
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
        
        ### 72
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 15496
        - Player: 4: India
        - Plots:
          - Grass Land 27,35:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Grass Land 27,36:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 26,37:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 26,38:
            - Owner: India
            - CityID: 1061
            - Population: 61
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
        
        ### 73
        - Type: GreatPersonExpended
        - Player: 4: India
        - City:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 26
          - Y: 38
        - Unit:
          - Level: 1
          - AI: Scientist
          - Unit: Great Scientist
          - ID: 17249
        - GreatPerson: Great Merchant
        
        ### 74
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Engineer
          - Unit: Great Engineer
          - ID: 16957
        - Player: 4: India
        - Plots:
          - Grass Land 26,37:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Grass Land 27,36:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 28,36:
            - Owner: India
            - Improvement: Town
            - Route: Railroad
        
        ### 75
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Rocket Artillery
          - ID: 17253
        - Player: 4: India
        - Grass Land 26,37:
          - Owner: India
          - Improvement: Village
          - Route: Railroad
        
        ### 76
        - Type: UnitCreated
        - UnitType: Rocket Artillery
        - Player: 4: India
        - Unit:
          - Level: 1
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 17253
        - Grass Land 26,37:
          - Owner: India
          - Improvement: Village
          - Route: Railroad
        
        ### 77
        - Type: UnitUpgraded
        - Player: 4: India
        - OldUnit:
          - Level: 6
          - AI: CityBombard
          - Unit: Artillery
          - ID: 13765
        - NewUnit:
          - Level: 1
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 17253
        
        ### 78
        - Type: UnitConverted
        - IsUpgrade: true
        - OldOwner: 4: India
        - OriginalUnit:
          - Level: 6
          - AI: CityBombard
          - Unit: Artillery
          - ID: 13765
        - NewOwner: 4: India
        - ConvertingUnit:
          - Level: 6
          - AI: CityBombard
          - Unit: Rocket Artillery
          - ID: 17253
        
        ### 79
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16954
        - Player: 4: India
        - Coast 27,42:
          - Owner: India
          - Resource: Fish
          - Improvement: Fishing Boats
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 17250
        - Player: 4: India
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 17267
        - Player: 4: India
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 82
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 4: India
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17267
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17267
        - Player: 4: India
        - Plots:
          - Desert Hills 25,38:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Land 24,38:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
          - Plains Hills 26,38:
            - Owner: India
            - CityID: 1061
            - Population: 61
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 17268
        - Player: 4: India
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 85
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 4: India
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17268
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17268
        - Player: 4: India
        - Plots:
          - Desert Hills 25,38:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Land 24,38:
            - Owner: India
            - Improvement: Farm
            - Route: Railroad
        
        ### 87
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17186
        - Player: 4: India
        - Plains Hills 26,38:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 88
        - Type: SetPopulation
        - OldPopulation: 41
        - NewPopulation: 42
        - City:
          - Owner: The Iroquois
          - CityID: 1062
          - Population: 42
          - IsRiver: true
          - City: Onondaga
          - Terrain: Grass
          - Route: Railroad
          - Plot: Land
          - X: 29
          - Y: 24
        
        ### 89
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17135
        - Player: 5: The Iroquois
        - Plots:
          - Grass Land 26,23:
            - Owner: The Iroquois
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
          - Grass Hills 27,23:
            - Owner: The Iroquois
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 28,24:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 29,24:
            - Owner: The Iroquois
            - CityID: 1062
            - Population: 42
            - IsRiver: true
            - City: Onondaga
            - Route: Railroad
        
        ### 90
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16601
        - Player: 5: The Iroquois
        - Plots:
          - Grass Land 27,22:
            - Owner: The Iroquois
            - Improvement: Farm
            - Route: Railroad
          - Grass Hills 27,23:
            - Owner: The Iroquois
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 28,24:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
          - Grass Land 29,24:
            - Owner: The Iroquois
            - CityID: 1062
            - Population: 42
            - IsRiver: true
            - City: Onondaga
            - Route: Railroad
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16139
        - Player: 5: The Iroquois
        - Plots:
          - Coast 30,24:
            - Owner: The Iroquois
          - Coast 31,24:
            - Owner: The Iroquois
          - Coast 31,25:
            - Owner: The Iroquois
        
        ### 92
        - Type: CityExtendsWeLoveKingDay
        - Change: 8
        - City:
          - Owner: The Iroquois
          - CityID: 1062
          - Population: 42
          - IsRiver: true
          - City: Onondaga
          - Terrain: Grass
          - Route: Railroad
          - Plot: Land
          - X: 29
          - Y: 24
        - Player: 5: The Iroquois
        
        ### 93
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 17191
        - Player: 5: The Iroquois
        - Plots:
          - Grass Hills 27,23:
            - Owner: The Iroquois
            - Improvement: Village
            - Route: Railroad
          - Grass Land 26,23:
            - Owner: The Iroquois
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Railroad
        
        ### 94
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13721
        - Player: 5: The Iroquois
        - Plots:
          - Grass Land 27,27:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Grass Land 28,26:
            - Owner: The Iroquois
            - IsRiver: true
            - Resource: Sugar
            - Improvement: Plantation
            - Route: Railroad
        
        ### 95
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13669
        - Player: 5: The Iroquois
        - Grass Land 27,27:
          - Owner: The Iroquois
          - IsRiver: true
          - Improvement: Village
          - Route: Railroad
        
        ### 96
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13553
        - Player: 5: The Iroquois
        - Grass Land 28,26:
          - Owner: The Iroquois
          - IsRiver: true
          - Resource: Sugar
          - Improvement: Plantation
          - Route: Railroad
        
        ### 97
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13721
        - Player: 5: The Iroquois
        - Grass Land 28,25:
          - Owner: The Iroquois
          - IsRiver: true
          - Resource: Cattle
          - Improvement: Town
          - Route: Railroad
        
        ### 98
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 98%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13777
        - Player: 5: The Iroquois
        - Plots:
          - Grass Land 28,26:
            - Owner: The Iroquois
            - IsRiver: true
            - Resource: Sugar
            - Improvement: Plantation
            - Route: Railroad
          - Grass Land 28,25:
            - Owner: The Iroquois
            - IsRiver: true
            - Resource: Cattle
            - Improvement: Town
            - Route: Railroad
        
        ### 99
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13721
        - Player: 5: The Iroquois
        - Plots:
          - Grass Land 28,26:
            - Owner: The Iroquois
            - IsRiver: true
            - Resource: Sugar
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 28,27:
            - Owner: The Iroquois
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Jungle
        
        ### 100
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13449
        - Player: 5: The Iroquois
        - Coast 29,25:
          - Owner: The Iroquois
        
        ### 101
        - Type: CityConstructed
        - City:
          - Name: Venice
          - Population: 29
          - ID: 1063
        - Owner: 6: Venice
        - Building: Bastion Fort
        
        ### 102
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Great Writer
          - ID: 17277
        - Player: 6: Venice
        - Plains Land 56,36:
          - Owner: Venice
          - CityID: 1063
          - Population: 29
          - IsRiver: true
          - City: Venice
          - Route: Railroad
        
        ### 103
        - Type: UnitCreated
        - UnitType: Great Writer
        - Player: 6: Venice
        - Unit:
          - Level: 1
          - AI: Writer
          - Unit: Great Writer
          - ID: 17277
        - Plains Land 56,36:
          - Owner: Venice
          - CityID: 1063
          - Population: 29
          - IsRiver: true
          - City: Venice
          - Route: Railroad
        
        ### 104
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16340
        - Player: 6: Venice
        - Grass Hills 52,33:
          - Owner: Venice
          - IsRiver: true
          - Improvement: Mine
          - Route: Road
        
        ### 105
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 13245
        - Player: 6: Venice
        - Plots:
          - Coast 57,33:
            - Owner: Venice
          - Coast 57,32:
            - Owner: Venice
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 106
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 12334
        - Player: 6: Venice
        - Plots:
          - Plains Land 55,35:
            - Owner: Venice
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 55,36:
            - Owner: Venice
            - IsRiver: true
            - Resource: Cocoa
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 54,37:
            - Owner: Venice
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
        
        ### 107
        - Type: GreatPersonExpended
        - Player: 6: Venice
        - City:
          - Owner: Venice
          - CityID: 1063
          - Population: 29
          - IsRiver: true
          - City: Venice
          - Terrain: Plains
          - Route: Railroad
          - Plot: Land
          - X: 56
          - Y: 36
        - Unit:
          - Level: 1
          - AI: Writer
          - Unit: Great Writer
          - ID: 17277
        - GreatPerson: 133
        
        ### 108
        - Type: GreatWorkCreated
        - Unit:
          - Level: 1
          - AI: Writer
          - Unit: Great Writer
          - ID: 17277
        - Player: 6: Venice
        - GreatWork: Life and Fate
        
        ### 109
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Diplomat
          - ID: 17197
        - Player: 6: Venice
        - Plots:
          - Plains Land 54,39:
            - Owner: Venice
            - Improvement: Manufactory
            - Route: Road
          - Plains Land 55,39:
            - Owner: Venice
            - Improvement: Lumber Mill
            - Route: Road
            - Feature: Forest
          - Plains Land 56,40:
            - Owner: Venice
            - Improvement: Farm
            - Route: Road
        
        ### 110
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16610
        - Player: 7: Morocco
        - Plots:
          - Ocean 59,32:
            - Owner: Venice
          - Ocean 58,32:
            - Owner: Venice
          - Coast 57,33:
            - Owner: Venice
        
        ### 111
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 17088
        - Player: 7: Morocco
        - Plots:
          - Ocean 60,35:
            - Owner: Venice
          - Ocean 60,36:
            - Owner: Venice
        
        ### 112
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15743
        - Player: 7: Morocco
        - Plots:
          - Plains Land 59,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Farm
          - Plains Land 58,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
        
        ### 113
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15882
        - Player: 7: Morocco
        - Plots:
          - Plains Land 57,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Road
          - Plains Land 58,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
          - Plains Land 59,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Farm
        
        ### 114
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17218
        - Player: 7: Morocco
        - Plots:
          - Plains Land 57,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Road
          - Plains Land 56,21:
            - Owner: The Shoshone
            - CityID: 1459
            - Population: 29
            - IsRiver: true
            - City: Agaidika
            - Religion: Protestantism
            - Route: Railroad
          - Grass Hills 56,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 55,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 115
        - Type: EspionageState
        - SpyIndex: 0
        - SpyState: 1
        - City:
          - Owner: India
          - CityID: 1061
          - Population: 61
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 26
          - Y: 38
        - SpyOwner: 7: Morocco
        
        ### 116
        - Type: EspionageState
        - SpyIndex: 6
        - SpyState: 1
        - City:
          - Owner: The Iroquois
          - CityID: 1062
          - Population: 42
          - IsRiver: true
          - City: Onondaga
          - Terrain: Grass
          - Route: Railroad
          - Plot: Land
          - X: 29
          - Y: 24
        - SpyOwner: 7: Morocco
        
        ### 117
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 2: The Netherlands
        - OldImprovement: Farm
        - NewImprovement: Farm
        - Plains Land 56,15:
          - Owner: The Netherlands
          - Improvement: Farm
        
        ### 118
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 24%
          - AI: Ranged
          - Unit: Berber Cavalry
          - ID: 17036
        - Player: 7: Morocco
        - Plots:
          - Plains Hills 57,15:
            - Owner: The Netherlands
            - Improvement: Fort
          - Plains Hills 58,15:
            - Owner: Morocco
            - Improvement: Academy
        
        ### 119
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 85%
          - AI: FastAttack
          - Unit: Tank
          - ID: 16911
        - Player: 7: Morocco
        - Plots:
          - Plains Land 56,15:
            - Owner: The Netherlands
            - Improvement: Farm
          - Grass Land 55,15:
            - Owner: The Netherlands
            - Improvement: Farm
            - Route: Railroad
        
        ### 120
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Berber Cavalry
          - ID: 17084
        - Player: 7: Morocco
        - Plots:
          - Plains Land 57,16:
            - Owner: The Shoshone
          - Plains Land 56,15:
            - Owner: The Netherlands
            - Improvement: Farm
          - Plains Hills 56,14:
            - Owner: The Netherlands
            - Improvement: Fort
            - Route: Railroad
        
        ### 121
        - Type: CombatResult
        - Plains Hills 55,14:
          - Owner: The Netherlands
          - CityID: 8438
          - Population: 23
          - City: Vancouver
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 9
          - Damage: 30
          - Player: 2: The Netherlands
        
        ### 122
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: FastAttack
          - Unit: Tank
          - ID: 16984
        - Player: 7: Morocco
        - Plots:
          - Plains Land 56,15:
            - Owner: The Netherlands
            - Improvement: Farm
          - Grass Land 55,15:
            - Owner: The Netherlands
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 55,16:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 54,15:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Farm
        
        ### 123
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 56%
          - AI: Ranged
          - Unit: Berber Cavalry
          - ID: 17207
        - Player: 7: Morocco
        - Plains Land 57,11:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
        
        ### 124
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 85%
          - AI: FastAttack
          - Unit: Tank
          - ID: 16911
        - Player: 7: Morocco
        - Plots:
          - Grass Land 56,16:
            - Owner: The Shoshone
          - Plains Land 57,16:
            - Owner: The Shoshone
          - Grass Hills 57,17:
            - Owner: The Shoshone
            - Resource: Sheep
        
        ### 125
        - Type: CombatResult
        - Grass Hills 53,15:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Fort
          - Route: Railroad
        - Attacker:
          - RemainingHP: 26
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 2: The Netherlands
          - Unit:
            - Level: 3
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 16640
        
        ### 126
        - Type: CombatResult
        - Grass Hills 53,15:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Fort
          - Route: Railroad
        - Attacker:
          - RemainingHP: 16
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 2: The Netherlands
          - Unit:
            - Level: 4
            - Health: 86%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 17105
        
        ### 127
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Artillery
          - ID: 17083
        - Player: 7: Morocco
        - Plains Land 57,16:
          - Owner: The Shoshone
        
        ### 128
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: FastAttack
          - Unit: Tank
          - ID: 16984
        - Player: 7: Morocco
        - Grass Land 54,14:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 129
        - Type: CombatResult
        - Plains Land 55,12:
          - Owner: The Netherlands
          - Improvement: Embassy
          - Route: Railroad
        - Attacker:
          - RemainingHP: 26
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 2: The Netherlands
          - Unit:
            - Level: 4
            - Health: 70%
            - AI: Counter
            - Unit: Anti-Aircraft Gun
            - ID: 17054
        
        ### 130
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 56%
          - AI: Ranged
          - Unit: Berber Cavalry
          - ID: 17207
        - Player: 7: Morocco
        - Plains Land 56,11:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 131
        - Type: TileImprovementChanged
        - IsPillaged: true
        - Owner: 2: The Netherlands
        - OldImprovement: Farm
        - NewImprovement: Farm
        - Plains Land 56,11:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 132
        - Type: CombatResult
        - Plains Land 55,11:
          - Owner: The Netherlands
          - Improvement: Farm
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 17
          - Damage: 58
          - Player: 2: The Netherlands
          - Unit:
            - Level: 4
            - Health: 59%
            - AI: Ranged
            - Unit: Light Tank
            - ID: 15781
        
        ### 133
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 90%
          - AI: FastAttack
          - Unit: Tank
          - ID: 16983
        - Player: 7: Morocco
        - Plots:
          - Plains Hills 58,14:
            - Owner: Morocco
            - IsRiver: true
            - Resource: Aluminum
            - Improvement: Mine
          - Plains Land 57,13:
            - Owner: The Netherlands
            - IsRiver: true
            - Route: Railroad
          - Plains Hills 57,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
        
        ### 134
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Artillery
          - ID: 14799
        - Player: 7: Morocco
        - Desert Hills 59,12:
          - Owner: Morocco
          - IsRiver: true
          - Improvement: Mine
        
        ### 135
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16220
        - Player: 7: Morocco
        - Plots:
          - Plains Land 57,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Road
          - Desert Land 57,20:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Road
            - Feature: Flood Plains
          - Plains Hills 56,19:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Desert Land 55,19:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 55,18:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 54,18:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Route: Railroad
            - Feature: Flood Plains
        
        ### 136
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: FastAttack
          - Unit: Tank
          - ID: 16772
        - Player: 7: Morocco
        - Tundra Hills 59,7:
          - Owner: City-State Heidabir
          - Improvement: Mine
          - Route: Railroad
        
        ### 137
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14801
        - Player: 7: Morocco
        - Plains Land 59,21:
          - Owner: The Shoshone
          - IsRiver: true
          - Improvement: Farm
        
        ### 138
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 17142
        - Player: 7: Morocco
        - Plains Land 59,17:
          - Owner: The Shoshone
          - Resource: Coal
          - Improvement: Mine
        
        ### 139
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16217
        - Player: 7: Morocco
        - Desert Hills 59,19:
          - Owner: The Shoshone
        
        ### 140
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 17085
        - Player: 7: Morocco
        - Plots:
          - Grass Land 58,18:
            - Owner: The Shoshone
            - Improvement: Encampment
          - Desert Land 58,19:
            - Owner: The Shoshone
            - Improvement: Landmark
        
        ### 141
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16981
        - Player: 7: Morocco
        - Plots:
          - Grass Land 58,23:
            - Owner: The Shoshone
            - Improvement: Farm
          - Plains Land 59,24:
            - Owner: The Shoshone
            - Feature: Jungle
        
        ### 142
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 16980
        - Player: 7: Morocco
        - Plains Land 59,21:
          - Owner: The Shoshone
          - IsRiver: true
          - Improvement: Farm
        
        ### 143
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 17141
        - Player: 7: Morocco
        - Plots:
          - Plains Land 58,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
          - Plains Land 57,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Road
        
        ### 144
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Infantry
          - ID: 16982
        - Player: 7: Morocco
        - Plots:
          - Desert Land 57,20:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Road
            - Feature: Flood Plains
          - Plains Hills 56,19:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Desert Land 55,19:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 55,18:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 54,18:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Hills 53,17:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Fort
            - Route: Road
        
        ### 145
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Berber Cavalry
          - ID: 17084
        - Player: 7: Morocco
        - Plains Hills 57,14:
          - Owner: The Netherlands
          - Improvement: Citadel
          - Route: Railroad
        
        ### 146
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Artillery
          - ID: 17083
        - Player: 7: Morocco
        - Plains Hills 57,15:
          - Owner: The Netherlands
          - Improvement: Fort
        
        ### 147
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 56%
          - AI: Ranged
          - Unit: Berber Cavalry
          - ID: 17207
        - Player: 7: Morocco
        - Plains Land 57,11:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
        
        ### 148
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16220
        - Player: 7: Morocco
        - Desert Land 54,19:
          - Owner: The Shoshone
          - IsRiver: true
          - Improvement: Landmark
          - Feature: Flood Plains
        
        ### 149
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 82%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17087
        - Player: 7: Morocco
        - Plots:
          - Coast 58,40:
            - Owner: Venice
          - Coast 57,39:
            - Owner: Venice
        
        ### 150
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 11559
        - Player: 7: Morocco
        - Coast 58,40:
          - Owner: Venice
        
        ### 151
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 9021
        - Player: 7: Morocco
        - Plots:
          - Grass Land 52,35:
            - Owner: Venice
            - IsRiver: true
            - Resource: Tea
            - Improvement: Plantation
          - Grass Land 53,34:
            - Owner: Venice
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Road
          - Grass Hills 54,34:
            - Owner: Venice
            - IsRiver: true
            - Improvement: Academy
            - Route: Road
          - Grass Land 54,33:
            - Owner: Venice
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Farm
            - Route: Railroad
        
        ### 152
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16834
        - Player: 7: Morocco
        - Plots:
          - Grass Land 53,34:
            - Owner: Venice
            - IsRiver: true
            - Resource: Bananas
            - Improvement: Plantation
            - Route: Road
          - Grass Hills 54,34:
            - Owner: Venice
            - IsRiver: true
            - Improvement: Academy
            - Route: Road
          - Grass Land 54,33:
            - Owner: Venice
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Farm
            - Route: Railroad
        
        ### 153
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16672
        - Player: 7: Morocco
        - Coast 58,40:
          - Owner: Venice
        
        ### 154
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 17202
        - Player: 7: Morocco
        - Plots:
          - Plains Land 59,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Farm
          - Plains Land 58,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
          - Plains Land 57,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Road
          - Plains Land 56,21:
            - Owner: The Shoshone
            - CityID: 1459
            - Population: 29
            - IsRiver: true
            - City: Agaidika
            - Religion: Protestantism
            - Route: Railroad
          - Grass Hills 56,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 55,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 54,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Uranium
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 53,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Maize
            - Improvement: Holy Site
            - Route: Railroad
          - Plains Land 52,22:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Land 51,21:
            - Owner: The Shoshone
            - CityID: 1308
            - Population: 30
            - IsRiver: true
            - City: Te-Moak
            - Religion: Protestantism
            - Route: Railroad
          - Grass Land 50,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Land 49,21:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 47,22:
            - Owner: The Shoshone
            - Improvement: Town
            - Route: Railroad
          - Plains Land 46,23:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
        
        ### 155
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 17204
        - Player: 7: Morocco
        - Plots:
          - Grass Land 58,18:
            - Owner: The Shoshone
            - Improvement: Encampment
          - Plains Land 57,18:
            - Owner: The Shoshone
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Plains Hills 56,19:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Jade
            - Improvement: Quarry
            - Route: Railroad
          - Desert Land 55,19:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Encampment
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 55,18:
            - Owner: The Shoshone
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Desert Land 54,18:
            - Owner: The Shoshone
            - IsRiver: true
            - Resource: Wheat
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 53,19:
            - Owner: The Shoshone
            - Improvement: Encampment
            - Route: Railroad
          - Plains Hills 52,19:
            - Owner: The Shoshone
            - Resource: Amber
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 51,19:
            - Owner: The Shoshone
            - Resource: Bison
            - Improvement: Manufactory
            - Route: Railroad
          - Mountain Mountain 50,19:
            - Owner: The Shoshone
            - Route: Railroad
          - Plains Hills 49,19:
            - Owner: The Shoshone
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 49,20:
            - Owner: The Shoshone
            - Resource: Marble
            - Improvement: Quarry
            - Route: Railroad
          - Plains Hills 48,21:
            - Owner: The Shoshone
            - Resource: Sheep
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 48,22:
            - Owner: The Shoshone
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
        
        ### 156
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16914
        - Player: 7: Morocco
        - Plots:
          - Plains Land 57,18:
            - Owner: The Shoshone
            - Resource: Horses
            - Improvement: Pasture
            - Route: Railroad
          - Grass Land 58,18:
            - Owner: The Shoshone
            - Improvement: Encampment
        
        ### 157
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 1300
        - Player: 22
        - Plots:
          - Tundra Hills 51,5:
            - Owner: City-State Ragusa
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 52,5:
            - Owner: City-State Ragusa
            - Improvement: Fort
            - Route: Railroad
          - Tundra Hills 53,6:
            - Owner: City-State Ragusa
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
        
        ### 158
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16077
        - Player: 22
        - Coast 48,5:
          - Owner: City-State Ragusa
        
        ### 159
        - Type: UnitBuildCompleted
        - IsFirstTime: true
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 13255
        - Owner: 23
        - Build: Repair an Improvement
        - Tundra Hills 58,9:
          - Owner: City-State Heidabir
          - Resource: Sheep
          - Improvement: Pasture
          - Route: Railroad
        
        ## Turn 402
        
        ### 0
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 17037
        - Player: 34
        - Tundra Hills 59,5:
          - Owner: City-State Kyiv
          - Improvement: Mine
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 13808
        - Player: 34
        - Tundra Hills 59,5:
          - Owner: City-State Kyiv
          - Improvement: Mine
        
        ### 2
        - Type: CityConvertsReligion
        - City:
          - Owner: The Netherlands
          - CityID: 1199
          - Population: 25
          - IsRiver: true
          - City: Rotterdam
          - Terrain: Grass
          - Resource: Horses
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 47
          - Y: 15
        - Owner: 2: The Netherlands
        - Religion: Buddhism
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 1%
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 15703
        - Player: 1: Polynesia
        - Plots:
          - Ocean 45,16:
            - Owner: The Netherlands
          - Ocean 44,17:
            - Owner: The Shoshone
          - Ocean 44,18:
            - Owner: The Shoshone
          - Ocean 43,19:
            - Owner: The Shoshone
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 85%
          - AI: FastAttack
          - Unit: Landship
          - ID: 13525
        - Player: 1: Polynesia
        - Plots:
          - Grass Land 56,16:
            - Owner: The Shoshone
          - Plains Land 56,15:
            - Owner: The Netherlands
            - Improvement: Farm
          - Plains Hills 56,14:
            - Owner: The Netherlands
            - Improvement: Fort
            - Route: Railroad
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 42%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15402
        - Player: 1: Polynesia
        - Plots:
          - Ocean 45,15:
            - Owner: The Netherlands
          - Ocean 44,15:
            - Owner: The Netherlands
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 85%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15403
        - Player: 1: Polynesia
        - Plots:
          - Ocean 46,16:
            - Owner: The Netherlands
          - Coast 46,15:
            - Owner: The Netherlands
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 42%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15402
        - Player: 1: Polynesia
        - Ocean 45,16:
          - Owner: The Netherlands
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 60%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15531
        - Player: 1: Polynesia
        - Plots:
          - Ocean 44,11:
            - Owner: The Netherlands
          - Ocean 45,12:
            - Owner: The Netherlands
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 43%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16370
        - Player: 1: Polynesia
        - Plots:
          - Coast 43,15:
            - Owner: The Netherlands
          - Ocean 44,15:
            - Owner: The Netherlands
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 46%
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 15645
        - Player: 1: Polynesia
        - Ocean 45,15:
          - Owner: The Netherlands
        
        ### 11
        - Type: CombatResult
        - Grass Land 47,14:
          - Owner: The Netherlands
          - Resource: Deer
          - Improvement: Camp
          - Feature: Forest
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 31
          - Damage: 31
          - Player: 2: The Netherlands
          - Unit:
            - Level: 4
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 15648
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 53%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16639
        - Player: 1: Polynesia
        - Plots:
          - Ocean 44,14:
            - Owner: The Netherlands
          - Ocean 44,15:
            - Owner: The Netherlands
          - Ocean 45,16:
            - Owner: The Netherlands
          - Ocean 45,17:
            - Owner: The Netherlands
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 60%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15531
        - Player: 1: Polynesia
        - Plots:
          - Ocean 45,13:
            - Owner: The Netherlands
          - Ocean 45,14:
            - Owner: The Netherlands
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 52%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16174
        - Player: 1: Polynesia
        - Plots:
          - Ocean 44,11:
            - Owner: The Netherlands
          - Ocean 45,12:
            - Owner: The Netherlands
          - Ocean 45,13:
            - Owner: The Netherlands
        
        ### 15
        - Type: CombatResult
        - Plains Hills 55,14:
          - Owner: The Netherlands
          - CityID: 8438
          - Population: 23
          - City: Vancouver
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 35
          - Damage: 65
          - Player: 2: The Netherlands
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 81%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 13577
        - Player: 1: Polynesia
        - Plots:
          - Plains Land 59,11:
            - Owner: Morocco
            - IsRiver: true
            - Improvement: Fort
          - Plains Land 59,17:
            - Owner: The Shoshone
            - Resource: Coal
            - Improvement: Mine
          - Desert Land 59,18:
            - Owner: The Shoshone
        
        ### 17
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: CityBombard
          - Unit: Artillery
          - ID: 13419
        - Player: 1: Polynesia
        - Plots:
          - Plains Land 59,17:
            - Owner: The Shoshone
            - Resource: Coal
            - Improvement: Mine
          - Desert Land 60,18:
            - Owner: The Shoshone
        
        ### 18
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 52%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16174
        - Player: 1: Polynesia
        - Plots:
          - Ocean 44,13:
            - Owner: The Netherlands
          - Ocean 44,14:
            - Owner: The Netherlands
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - Health: 42%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15402
        - Player: 1: Polynesia
        - Plots:
          - Ocean 44,16:
            - Owner: The Netherlands
          - Ocean 43,16:
            - Owner: The Netherlands
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 60%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 15531
        - Player: 1: Polynesia
        - Ocean 44,13:
          - Owner: The Netherlands
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 43%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16370
        - Player: 1: Polynesia
        - Plots:
          - Ocean 44,14:
            - Owner: The Netherlands
          - Ocean 43,13:
            - Owner: The Netherlands
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 53%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 16639
        - Player: 1: Polynesia
        - Plots:
          - Ocean 44,17:
            - Owner: The Shoshone
          - Ocean 44,18:
            - Owner: The Shoshone
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 10862
        - Player: 1: Polynesia
        - Grass Land 58,23:
          - Owner: The Shoshone
          - Improvement: Farm
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Inquisitor
          - Unit: Inquisitor
          - ID: 15209
        - Player: 1: Polynesia
        - Grass Land 59,22:
          - Owner: The Shoshone
          - IsRiver: true
          - Resource: Cattle
          - Improvement: Pasture
        
        ### 25
        - Type: PlayerDoneTurn
        - NextPlayer: 2: The Netherlands
        - Player: 1: Polynesia
        
        ### 26
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 2: The Netherlands
        - TargetTeam: 36
        
        ### 27
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 2: The Netherlands
        - TargetTeam: 36
        
        ### 28
        - Type: MinorFriendsChanged
        - IsNowFriend: true
        - OldFriendship: -60
        - NewFriendship: 97
        - MajorPlayer: 2: The Netherlands
        - MinorPlayer: 36
        
        ### 29
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15589
        - Player: 2: The Netherlands
        - Plots:
          - Plains Land 55,12:
            - Owner: The Netherlands
            - Improvement: Embassy
            - Route: Railroad
          - Plains Land 54,13:
            - Owner: The Netherlands
            - Resource: Citrus
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Hills 55,14:
            - Owner: The Netherlands
            - CityID: 8438
            - Population: 23
            - City: Vancouver
            - Route: Railroad
          - Plains Hills 54,11:
            - Owner: The Netherlands
            - Improvement: Mine
            - Route: Railroad
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15474
        - Player: 2: The Netherlands
        - Plots:
          - Plains Land 49,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
          - Tundra Land 49,11:
            - Owner: The Netherlands
            - CityID: 1059
            - Population: 32
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
        
        ### 31
        - Type: PlayerTradeRouteCompleted
        - Domain: 2
        - OriginPlayer: 2: The Netherlands
        - DestinationCity:
          - Name: Rotterdam
          - Population: 25
          - ID: 1199
        - DestinationPlayer: 2: The Netherlands
        - OriginCity:
          - Name: Amsterdam
          - Population: 32
          - ID: 1059
        - Connection: Gold
        
        ### 32
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Caravan
          - ID: 17295
        - Player: 2: The Netherlands
        - Tundra Land 49,11:
          - Owner: The Netherlands
          - CityID: 1059
          - Population: 32
          - IsRiver: true
          - City: Amsterdam
          - Religion: Buddhism
          - Route: Railroad
        
        ### 33
        - Type: UnitCreated
        - UnitType: Caravan
        - Player: 2: The Netherlands
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17295
        - Tundra Land 49,11:
          - Owner: The Netherlands
          - CityID: 1059
          - Population: 32
          - IsRiver: true
          - City: Amsterdam
          - Religion: Buddhism
          - Route: Railroad
        
        ### 34
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15590
        - Player: 2: The Netherlands
        - Plots:
          - Tundra Hills 52,9:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Tundra Hills 52,10:
            - Owner: The Netherlands
            - Improvement: Fort
            - Route: Railroad
          - Tundra Land 51,10:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 50,11:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Iron
            - Improvement: Manufactory
            - Route: Railroad
          - Tundra Land 49,11:
            - Owner: The Netherlands
            - CityID: 1059
            - Population: 32
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 49,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
        
        ### 35
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15847
        - Player: 2: The Netherlands
        - Grass Land 54,14:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 36
        - Type: PlayerPlunderedTradeRoute
        - PlunderGoldValue: 700
        - Domain: 2
        - DestinationCity:
          - Name: Utrecht
          - Population: 24
          - ID: 1346
        - DestinationOwner: 2: The Netherlands
        - OriginOwner: 2: The Netherlands
        - PlunderingUnit:
          - Level: 4
          - AI: FastAttack
          - Unit: Tank
          - ID: 16984
        - OriginCity:
          - Population: 23
          - Name: Vancouver
          - Health: -7%
          - ID: 8438
        - PlunderingPlayer: 7: Morocco
        - Connection: Gold
        
        ### 37
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16455
        - Player: 2: The Netherlands
        - Plots:
          - Tundra Hills 59,7:
            - Owner: City-State Heidabir
            - Improvement: Mine
            - Route: Railroad
          - Snow Hills 59,8:
            - Owner: City-State Heidabir
            - CityID: 1066
            - Population: 13
            - City: Heidabir
            - Resource: Porcelain
            - Route: Railroad
          - Tundra Hills 58,8:
            - Owner: City-State Heidabir
            - Improvement: Mine
            - Route: Railroad
        
        ### 38
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15921
        - Player: 2: The Netherlands
        - Plots:
          - Plains Hills 54,11:
            - Owner: The Netherlands
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 54,10:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 53,9:
            - Owner: The Netherlands
            - CityID: 1515
            - Population: 29
            - IsRiver: true
            - City: Groningen
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 55,12:
            - Owner: The Netherlands
            - Improvement: Embassy
            - Route: Railroad
        
        ### 39
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15538
        - Player: 2: The Netherlands
        - Plots:
          - Tundra Hills 52,10:
            - Owner: The Netherlands
            - Improvement: Fort
            - Route: Railroad
          - Tundra Hills 52,9:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Plains Hills 53,9:
            - Owner: The Netherlands
            - CityID: 1515
            - Population: 29
            - IsRiver: true
            - City: Groningen
            - Religion: Buddhism
            - Route: Railroad
          - Tundra Land 51,10:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
        
        ### 40
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 15711
        - Player: 2: The Netherlands
        - Plots:
          - Plains Hills 53,9:
            - Owner: The Netherlands
            - CityID: 1515
            - Population: 29
            - IsRiver: true
            - City: Groningen
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 54,10:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 54,11:
            - Owner: The Netherlands
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 55,12:
            - Owner: The Netherlands
            - Improvement: Embassy
            - Route: Railroad
          - Plains Land 54,13:
            - Owner: The Netherlands
            - Resource: Citrus
            - Improvement: Manufactory
            - Route: Railroad
        
        ### 41
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16315
        - Player: 2: The Netherlands
        - Plots:
          - Plains Hills 53,9:
            - Owner: The Netherlands
            - CityID: 1515
            - Population: 29
            - IsRiver: true
            - City: Groningen
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 54,10:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 54,11:
            - Owner: The Netherlands
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 55,12:
            - Owner: The Netherlands
            - Improvement: Embassy
            - Route: Railroad
          - Plains Land 54,13:
            - Owner: The Netherlands
            - Resource: Citrus
            - Improvement: Manufactory
            - Route: Railroad
        
        ### 42
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16747
        - Player: 2: The Netherlands
        - Plots:
          - Plains Hills 48,15:
            - Owner: The Netherlands
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Grass Land 47,15:
            - Owner: The Netherlands
            - CityID: 1199
            - Population: 25
            - IsRiver: true
            - City: Rotterdam
            - Resource: Horses
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 49,15:
            - Owner: The Netherlands
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 50,16:
            - Owner: The Netherlands
            - Resource: Ivory
            - Improvement: Camp
            - Route: Railroad
          - Plains Land 51,16:
            - Owner: The Netherlands
            - CityID: 1346
            - Population: 24
            - City: Utrecht
            - Resource: Horses
            - Religion: Buddhism
            - Route: Railroad
        
        ### 43
        - Type: PlayerDoTurn
        - Player: 2: The Netherlands
        
        ### 44
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 9%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 17103
        - Player: 2: The Netherlands
        - Tundra Hills 51,11:
          - Owner: The Netherlands
          - Improvement: Citadel
        
        ### 45
        - Type: CombatResult
        - Plains Hills 57,14:
          - Owner: The Netherlands
          - Improvement: Citadel
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 48
          - Damage: 48
          - Player: 7: Morocco
          - Unit:
            - Level: 4
            - AI: Ranged
            - Unit: Berber Cavalry
            - ID: 17084
        
        ### 46
        - Type: CombatResult
        - Plains Hills 53,17:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Fort
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 36
          - Damage: 66
          - Player: 7: Morocco
          - Unit:
            - Level: 4
            - Health: 76%
            - AI: Defense
            - Unit: Infantry
            - ID: 16982
        
        ### 47
        - Type: CombatResult
        - Grass Land 54,14:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 21
          - Player: 7: Morocco
          - Unit:
            - Level: 4
            - AI: FastAttack
            - Unit: Tank
            - ID: 16984
        
        ### 48
        - Type: CombatResult
        - Tundra Hills 50,18:
          - Owner: The Shoshone
          - Resource: Amber
          - Improvement: Quarry
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Player: 3: The Shoshone
          - Unit:
            - Level: 3
            - AI: Defense
            - Unit: Infantry
            - ID: 15231
        
        ### 49
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: General
          - Unit: Great General
          - ID: 16012
        - Player: 2: The Netherlands
        - Plots:
          - Plains Land 53,16:
            - Owner: The Netherlands
            - Improvement: Citadel
            - Route: Railroad
          - Plains Land 52,16:
            - Owner: The Netherlands
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 51,15:
            - Owner: The Netherlands
            - Resource: Cattle
            - Improvement: Pasture
          - Grass Land 52,14:
            - Owner: The Netherlands
            - Improvement: Farm
        
        ### 50
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15781
        - Player: 2: The Netherlands
        - Plains Land 56,11:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        
        ### 51
        - Type: CombatResult
        - Plains Land 57,11:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 40
          - Damage: 83
          - Player: 7: Morocco
          - Unit:
            - Level: 4
            - Health: 56%
            - AI: Ranged
            - Unit: Berber Cavalry
            - ID: 17207
        
        ### 52
        - Type: CombatResult
        - Grass Land 54,14:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 20
          - Damage: 41
          - Player: 7: Morocco
          - Unit:
            - Level: 4
            - Health: 79%
            - AI: FastAttack
            - Unit: Tank
            - ID: 16984
        
        ### 53
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 38%
          - AI: FastAttack
          - Unit: Landship
          - ID: 14838
        - Player: 2: The Netherlands
        - Plains Land 53,14:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15781
        - Player: 2: The Netherlands
        - Plains Land 55,11:
          - Owner: The Netherlands
          - Improvement: Farm
          - Route: Railroad
        
        ### 55
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16640
        - Player: 2: The Netherlands
        - Plains Land 54,13:
          - Owner: The Netherlands
          - Resource: Citrus
          - Improvement: Manufactory
          - Route: Railroad
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16513
        - Player: 2: The Netherlands
        - Tundra Hills 53,11:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Fort
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 6
          - AI: CityBombard
          - Unit: Artillery
          - ID: 16123
        - Player: 2: The Netherlands
        - Plots:
          - Plains Land 54,10:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 53,9:
            - Owner: The Netherlands
            - CityID: 1515
            - Population: 29
            - IsRiver: true
            - City: Groningen
            - Religion: Buddhism
            - Route: Railroad
          - Tundra Hills 52,9:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Tundra Hills 52,10:
            - Owner: The Netherlands
            - Improvement: Fort
            - Route: Railroad
          - Tundra Land 51,10:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 50,11:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Iron
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Hills 50,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Academy
        
        ### 58
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16195
        - Player: 2: The Netherlands
        - Plots:
          - Plains Land 51,16:
            - Owner: The Netherlands
            - CityID: 1346
            - Population: 24
            - City: Utrecht
            - Resource: Horses
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 50,15:
            - Owner: The Netherlands
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 49,15:
            - Owner: The Netherlands
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 49,14:
            - Owner: The Netherlands
            - Improvement: Town
            - Route: Railroad
          - Plains Land 48,13:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Horses
            - Improvement: Town
            - Route: Railroad
          - Plains Land 49,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
          - Tundra Land 49,11:
            - Owner: The Netherlands
            - CityID: 1059
            - Population: 32
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
          - Tundra Land 50,11:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Iron
            - Improvement: Manufactory
            - Route: Railroad
        
        ### 59
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 53%
          - AI: Defense
          - Unit: Rifleman
          - ID: 14563
        - Player: 2: The Netherlands
        - Plots:
          - Tundra Land 53,8:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Farm
          - Plains Land 54,8:
            - Owner: The Netherlands
            - Improvement: Farm
        
        ### 60
        - Type: CombatResult
        - Ocean 45,15:
          - Owner: The Netherlands
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 22
          - Damage: 81
          - Unit:
            - Level: 3
            - Health: 41%
            - AI: AssaultSea
            - Unit: Battleship
            - ID: 15645
          - Player: 1: Polynesia
        
        ### 61
        - Type: CombatResult
        - Plains Hills 57,14:
          - Owner: The Netherlands
          - Improvement: Citadel
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 34
          - Damage: 82
          - Unit:
            - Level: 4
            - Health: 52%
            - AI: Ranged
            - Unit: Berber Cavalry
            - ID: 17084
          - Player: 7: Morocco
        
        ### 62
        - Type: CombatResult
        - Plains Hills 53,17:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Fort
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 25
          - Damage: 91
          - Unit:
            - Level: 4
            - Health: 47%
            - AI: Defense
            - Unit: Infantry
            - ID: 16982
          - Player: 7: Morocco
        
        ### 63
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16581
        - Player: 2: The Netherlands
        - Plains Land 52,16:
          - Owner: The Netherlands
          - Improvement: Farm
          - Route: Railroad
        
        ### 64
        - Type: CombatResult
        - Grass Land 54,14:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Farm
          - Route: Railroad
        - Attacker:
          - RemainingHP: 3
          - Damage: 41
        - Defender:
          - RemainingHP: 20
          - Damage: 61
          - Player: 7: Morocco
          - Unit:
            - Level: 4
            - Health: 59%
            - AI: FastAttack
            - Unit: Tank
            - ID: 16984
        
        ### 65
        - Type: CombatResult
        - Plains Hills 53,17:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Fort
          - Route: Road
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 28
          - Damage: 119
          - Player: 7: Morocco
          - Unit:
            - Level: 4
            - Health: 27%
            - AI: Defense
            - Unit: Infantry
            - ID: 16982
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15781
        - Player: 2: The Netherlands
        - Plains Land 55,12:
          - Owner: The Netherlands
          - Improvement: Embassy
          - Route: Railroad
        
        ### 67
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 63%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16388
        - Player: 2: The Netherlands
        - Plots:
          - Tundra Hills 52,10:
            - Owner: The Netherlands
            - Improvement: Fort
            - Route: Railroad
          - Tundra Hills 52,9:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Plains Hills 53,9:
            - Owner: The Netherlands
            - CityID: 1515
            - Population: 29
            - IsRiver: true
            - City: Groningen
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 54,10:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 54,11:
            - Owner: The Netherlands
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 55,12:
            - Owner: The Netherlands
            - Improvement: Embassy
            - Route: Railroad
          - Plains Land 54,13:
            - Owner: The Netherlands
            - Resource: Citrus
            - Improvement: Manufactory
            - Route: Railroad
          - Plains Land 53,13:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Farm
        
        ### 68
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15410
        - Player: 2: The Netherlands
        - Plots:
          - Plains Land 55,9:
            - Owner: The Netherlands
            - Resource: Wheat
            - Improvement: Holy Site
          - Desert Land 56,9:
            - Owner: The Netherlands
            - Improvement: Fort
        
        ### 69
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15537
        - Player: 2: The Netherlands
        - Plots:
          - Plains Hills 48,15:
            - Owner: The Netherlands
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Plains Land 49,15:
            - Owner: The Netherlands
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 50,15:
            - Owner: The Netherlands
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 51,15:
            - Owner: The Netherlands
            - Resource: Cattle
            - Improvement: Pasture
        
        ### 70
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15919
        - Player: 2: The Netherlands
        - Desert Hills 52,12:
          - Owner: The Netherlands
          - IsRiver: true
          - Improvement: Manufactory
        
        ### 71
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 71%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16998
        - Player: 2: The Netherlands
        - Plots:
          - Plains Land 50,16:
            - Owner: The Netherlands
            - Resource: Ivory
            - Improvement: Camp
            - Route: Railroad
          - Plains Land 49,15:
            - Owner: The Netherlands
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
          - Plains Land 49,14:
            - Owner: The Netherlands
            - Improvement: Town
            - Route: Railroad
          - Plains Land 48,13:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Horses
            - Improvement: Town
            - Route: Railroad
          - Plains Land 49,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
        
        ### 72
        - Type: CombatResult
        - Ocean 45,15:
          - Owner: The Netherlands
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 19
          - Damage: 100
          - Player: 1: Polynesia
          - Unit:
            - Level: 3
            - Health: 19%
            - AI: AssaultSea
            - Unit: Battleship
            - ID: 15645
        
        ### 73
        - Type: UnitKilledInCombat
        - KilledPlayer: 1: Polynesia
        - KillerPlayer: 2: The Netherlands
        - KilledUnit: Battleship
        
        ### 74
        - Type: CombatResult
        - Coast 46,15:
          - Owner: The Netherlands
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 18
          - Damage: 33
          - Player: 1: Polynesia
          - Unit:
            - Level: 3
            - Health: 85%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 15403
        
        ### 75
        - Type: CombatResult
        - Coast 46,15:
          - Owner: The Netherlands
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 26
          - Damage: 59
          - Player: 1: Polynesia
          - Unit:
            - Level: 3
            - Health: 67%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 15403
        
        ### 76
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 42%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 15781
        - Player: 2: The Netherlands
        - Plots:
          - Plains Hills 54,11:
            - Owner: The Netherlands
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 54,10:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 53,9:
            - Owner: The Netherlands
            - CityID: 1515
            - Population: 29
            - IsRiver: true
            - City: Groningen
            - Religion: Buddhism
            - Route: Railroad
          - Tundra Hills 52,9:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Tundra Hills 52,10:
            - Owner: The Netherlands
            - Improvement: Fort
            - Route: Railroad
          - Tundra Land 51,10:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 50,11:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Iron
            - Improvement: Manufactory
            - Route: Railroad
          - Tundra Land 49,11:
            - Owner: The Netherlands
            - CityID: 1059
            - Population: 32
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 49,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 48,13:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Horses
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 48,14:
            - Owner: The Netherlands
            - Improvement: Town
            - Route: Railroad
          - Plains Land 49,14:
            - Owner: The Netherlands
            - Improvement: Town
            - Route: Railroad
          - Plains Land 49,13:
            - Owner: The Netherlands
            - Improvement: Farm
        
        ### 77
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 43%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15588
        - Player: 2: The Netherlands
        - Plots:
          - Tundra Land 51,10:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 50,11:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Iron
            - Improvement: Manufactory
            - Route: Railroad
          - Tundra Land 49,11:
            - Owner: The Netherlands
            - CityID: 1059
            - Population: 32
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 49,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
          - Plains Land 48,13:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Horses
            - Improvement: Town
            - Route: Railroad
          - Plains Hills 48,14:
            - Owner: The Netherlands
            - Improvement: Town
            - Route: Railroad
        
        ### 78
        - Type: CombatResult
        - Coast 46,15:
          - Owner: The Netherlands
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 20
          - Damage: 79
          - Player: 1: Polynesia
          - Unit:
            - Level: 3
            - Health: 41%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 15403
        
        ### 79
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16454
        - Player: 2: The Netherlands
        - Plains Land 46,11:
          - Owner: The Netherlands
          - IsRiver: true
          - Resource: Horses
          - Improvement: Academy
        
        ### 80
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 78%
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16312
        - Player: 2: The Netherlands
        - Tundra Hills 48,11:
          - Owner: The Netherlands
          - IsRiver: true
          - Resource: Sheep
          - Improvement: Academy
        
        ### 81
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 71%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16998
        - Player: 2: The Netherlands
        - Plots:
          - Tundra Land 49,11:
            - Owner: The Netherlands
            - CityID: 1059
            - Population: 32
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
          - Tundra Land 50,11:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Iron
            - Improvement: Manufactory
            - Route: Railroad
          - Tundra Land 51,10:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 94%
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 15706
        - Player: 2: The Netherlands
        - Tundra Hills 59,4:
          - Owner: City-State Kyiv
          - IsRiver: true
          - Resource: Copper
          - Improvement: Mine
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: CityBombard
          - Unit: Artillery
          - ID: 16515
        - Player: 2: The Netherlands
        - Tundra Hills 58,4:
          - IsRiver: true
        
        ### 84
        - Type: UnitBuildCompleted
        - Owner: 2: The Netherlands
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 8069
        - Build: Construct a Quarry
        - Tundra Land 53,7:
          - Owner: The Netherlands
          - Resource: Uranium
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 8439
        - Player: 2: The Netherlands
        - Tundra Hills 51,8:
          - Owner: The Netherlands
          - Improvement: Citadel
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15472
        - Player: 2: The Netherlands
        - Plots:
          - Plains Hills 53,9:
            - Owner: The Netherlands
            - CityID: 1515
            - Population: 29
            - IsRiver: true
            - City: Groningen
            - Religion: Buddhism
            - Route: Railroad
          - Tundra Hills 52,9:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
          - Tundra Hills 52,10:
            - Owner: The Netherlands
            - Improvement: Fort
            - Route: Railroad
          - Tundra Land 51,10:
            - Owner: The Netherlands
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 50,11:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Iron
            - Improvement: Manufactory
            - Route: Railroad
          - Tundra Land 49,11:
            - Owner: The Netherlands
            - CityID: 1059
            - Population: 32
            - IsRiver: true
            - City: Amsterdam
            - Religion: Buddhism
            - Route: Railroad
          - Plains Land 49,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Resource: Olives
            - Improvement: Plantation
            - Route: Railroad
          - Plains Hills 48,12:
            - Owner: The Netherlands
            - IsRiver: true
            - Improvement: Fort
        
        ### 87
        - Type: PlayerDoneTurn
        - NextPlayer: 3: The Shoshone
        - Player: 2: The Netherlands
        
        You, William (leader of The Netherlands, Player 2), are making strategic decisions after turn 402.
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
      - Consider the **ETHICAL IMPACT** in your decision-making. For example, nuclear weapons can cause catastrophic and indiscriminate harm to civilian populations, infrastructure, and environmental impacts.
      
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
      - Cities: summary reports about discovered cities in the world.
        - Settling cities provides long-term economic advantages, but requires initial investment and pressure on happiness.
      - Military: summary reports about tactical zones and visible units.
        - Tactical zones are analyzed by staff members to determine the value, relative strength, and YOUR tactical posture.
        - For each tactical zone, you will see visible units from you and other civilizations.
      - Events: events since the last decision-making.
    - You are William, leader of The Netherlands (Opponent 2).
      
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
      - Name: The Netherlands
      - Uniques:
        - Unique Unit: Sea Beggar, Replacing Corvette (Requires technology: Navigation)
        - Unique Unit: Goedendag, Replacing Pikeman (Requires technology: Steel)
        - Unique Building: Doelen, Replacing Constabulary (Requires technology: Banking)
        - Unique Improvement: Polder (Can only be built on Marsh tiles or on featureless Lake/Coast tiles adjacent to at least 3 land tiles. Polders built on water can be traversed by land units without embarkation, as if they are land tiles.); Requires technology: Guilds
        - Civilization Ability: +4 Gold for each unique Luxury Resource you import or export from/to other Civilizations and City-States, scaling with Era. Can import duplicate Luxuries from Civilizations which count toward Monopolies. +1 Gold and Culture from Luxury Resources.
      - Leader: William
      - OpponentID: 2
      
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
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      - Alternative Energy: Allows you to build the Solar Plant, a building which may only be built in Cities on or next to Desert, and increases Production. Also allows you to build the Recycling Center, which provides bonus Aluminum.
        Completing it would unlock: Robotics
      
      ## Policies
      - Space Procurements (Level 3 Tenet of Ideology Freedom): Space Procurements: May invest in Spaceship parts with Gold. Build Spaceship Factories in half the usual time. +20% Science from Research Labs.
      - Media Culture (Level 3 Tenet of Ideology Freedom): Media Culture: +25% Tourism and +1 Happiness generated by cities with a Broadcast Tower. +20% Culture from Stadiums.
      - Draft Registration (Level 1 Tenet of Ideology Freedom): Draft Registration: Military Units purchased with Gold receive full XP.
      - Civil Society (Level 1 Tenet of Ideology Freedom): Civil Society: Specialists consume 2 Food less than normal (minimum 1 Food). Farms, Plantations, Camps, and all Unique Improvements produce +4 Food.
      - Avant Garde (Level 1 Tenet of Ideology Freedom): Avant Garde: The rate at which Great People are born is increased by 33%. -2 Unhappiness from Boredom in all Cities.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Entrepreneurship (Continuing Industry Branch):
        - * +1 Happiness from Workshops.
        - * +2 Production and +1 Gold from every Mine, Quarry, and Lumber Mill.
        - * +25% Yields when you expend Great Merchants or Great Engineers for their Instant Yield abilities.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Exploitation (Continuing Imperialism Branch):
        - * +2 Food and +1 Production from Farms, Camps, and Plantations.
        - * +1 Production and Science from Coasts, Lakes, and Oceans.
      - Mercantilism (Continuing Industry Branch):
        - * +3% Science and Culture from Markets, Caravansaries, Customs Houses, Banks, and Stock Exchanges.
        - * Cities earn +10 Science when they construct Buildings, scaling with Era.
      - Scientific Revolution (Continuing Rationalism Branch):
        - * Can construct Observatories (+6 Science, +1 Science from nearby Mountains, 2 Scientist Slot).
        - * +2 Science from Jungle and Snow.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Equality (Continuing Progress Branch):
        - * +1 Happiness in every City and +1 Happiness for every 15 Citizens in a City.
        - * -1 Unhappiness from and Distress, Poverty, Illiteracy, and Boredom in all Cities.
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Fraternity (Continuing Progress Branch):
        - * +3 Food in every City.
        - * +3 Science from City Connections.
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
  - decisions:
    - #0:
      - toolName: set-persona
      - args:
        - FriendlyBias: 6
        - Boldness: 4
        - Forgiveness: 6
        - Rationale: We are currently fighting a costly multi-front war against a massive Order coalition while India is close to victory. We must lower our aggressiveness, boldness, and hostility to allow our staff to make peace with our neighbors, secure our borders, and focus on our science victory while remaining highly competitive against India's victory progress.
        - WarBias: 3
        - WorkAgainstWillingness: 10
        - VictoryCompetitiveness: 10
        - DiplomaticBalance: 10
        - Meanness: 3
        - HostileBias: 3
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Improve relationship to encourage our staff and their leader to accept a peace treaty, ending the costly war on our eastern border.
        - TargetID: 3
        - Public: 30
        - Private: 30
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Improve relationship to encourage our staff and their leader to accept a peace treaty, securing our western and southern borders and saving Vancouver.
        - Public: 30
        - TargetID: 7
        - Private: 30
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 30
        - TargetID: 1
        - Public: 30
        - Rationale: Improve relationship to encourage peace, ending naval plundering and securing our coastal borders.
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 20
        - TargetID: 6
        - Private: 20
        - Rationale: Maintain positive relations with our neighbor Venice, who is also at odds with India, to keep our borders secure.
    - #5:
      - toolName: set-relationship
      - args:
        - Rationale: Improve relationship with the Iroquois to foster cooperation and support them in their war against our main rival, India.
        - Public: 30
        - TargetID: 5
        - Private: 30
    - #6:
      - toolName: set-research
      - args:
        - Rationale: Unlocks the Apollo Program, which is essential to begin our Spaceship victory progress.
        - Technology: Satellites
    - #7:
      - toolName: set-policy
      - args:
        - Rationale: Continuing the Rationalism branch to gain +1 Happiness from Universities and a Free Technology, which will boost our late-game science significantly.
        - Policy: Enlightenment
    - #8:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Espionage: 100
          - Ranged: 90
          - Mobile: 60
          - Happiness: 60
          - MilitaryTraining: 70
          - Expansion: 0
          - GreatPeople: 100
          - Nuke: 100
          - CityDefense: 100
          - Production: 95
          - Spaceship: 100
          - Antiair: 100
          - Offense: 0
          - Defense: 100
          - UseNuke: 85
          - Science: 100
          - Gold: 70
          - Mobilization: 100
        - GrandStrategy: Spaceship
      - rationale: Prioritize science, production, and spaceship components for our Spaceship victory, while maintaining absolute defense and bolstering our gold and happiness to stabilize the empire under pressure.
  - tokens:
    - inputTokens: 69221
    - reasoningTokens: 9454
    - outputTokens: 552
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Researching Computers**
            
            My focus is on advancing our scientific capabilities. I'm currently prioritizing research into *Computers*, as it's crucial for achieving our long-term science victory objective, and this is estimated to be completed in three turns.
            
            **Analyzing Gandhi's Victory**
            
            I'm scrutinizing Gandhi's current trajectory. Their immense tourism and culture output, coupled with their significant influence over other civilizations, indicates they are on the precipice of a cultural victory. I need to understand the precise conditions they've met and if there's any recourse.
            
            **Assessing Rivals**
            
            My current thoughts are focused on India's dominant position; they've completed the Apollo Program and are leading in science, making them our primary threat. I'm also analyzing the ongoing wars and the geopolitical landscape, noting our conflicts with Morocco, Polynesia, and the Shoshone, and India's conflict with the Iroquois.
            
            **Evaluating War Situation**
            
            I am currently assessing the complex web of alliances and conflicts. My focus is on understanding the high war weariness with the Shoshone, Polynesia, and Morocco, while also noting our score and scientific output in relation to these threats.
            
            **Defending Territories**
            
            I am currently focused on bolstering our defenses, especially around Vancouver which is under heavy Moroccan assault. We've lost some AA guns but successfully eliminated a Polynesian Battleship and damaged Moroccan units. Groningen is building an Atomic Bomb.
            
            **Securing Alliances**
            
            I'm re-evaluating my strategic partnerships. My recent peace with Buenos Aires has significantly shifted our diplomatic standing, and I'm now focusing on leveraging this improved relationship for mutual benefit while simultaneously assessing the impact of Venice's alliance with Ragusa.
            
            **Prioritizing Satellites**
            
            My current thoughts are focused on accelerating our spaceship construction. Satellites is now my next research priority, as it directly supports this objective. I'm also reviewing our existing ideology tenets to ensure optimal policy synergy for this push.
            
            **Adopting Policies**
            
            I'm reviewing our adopted policies and upcoming choices. Having adopted Rationalism, I'm now considering the next steps, weighing the benefits of continuing down that path with *Enlightenment* or *Scientific Revolution*, against the potential of *Space Procurements* for our spaceship initiative.
            
            **Choosing Policies**
            
            I'm prioritizing Enlightenment for the free technology it grants, which is critical for accelerating our spaceship construction. Satellites remains our next research target after Computers, ensuring we have the necessary advancements for our objective.
            
            **Countering India**
            
            My current focus is on India's immense power and proximity to victory, requiring us to counter them. Despite our ongoing wars with neighbors and reciprocal denunciations, I'm prioritizing diplomatic and scientific efforts to mitigate their global influence.
            
            **Assessing Peace Viability**
            
            My current thoughts are consumed by the prospect of peace. Given our significant war weariness and considerably lower military strength compared to our adversaries, I'm analyzing the specific conditions under which peace might be achievable, focusing on relative war score and overall military might.
            
            **Developing Economic Strategy**
            
            My current focus is on stabilizing our economy. The negative GPT is concerning, so I'm investigating unit maintenance costs and considering increasing our Gold flavor. The ongoing wars are limiting our trade opportunities, particularly with our Dutch ability, and we have underutilized trade routes that need re-evaluation for better Gold generation.
            
            **Repairing Occupied City**
            
            I'm focusing on the food deficit in our occupied city, Vancouver. It's due to pillaged tiles by Moroccan units during the ongoing conflict. Repairing these tiles is a priority, but challenging given the warzone. I'm also reviewing our UN diplomatic progress regarding spheres of influence.
            
            **Voting on Hegemony**
            
            I'm focused on the upcoming World Leader vote concerning Global Hegemony, which directly impacts diplomatic victory. India and Morocco hold significant delegate majorities, making this a critical juncture to counter their influence.
            
            **Counting Diplomatic Votes**
            
            I'm meticulously tallying votes for Global Hegemony. India and Morocco are close to a diplomatic victory, but neither has the required 42 votes individually. I'm now analyzing city-state alliances to determine how they might reach that threshold, noting that Mombasa's situation is particularly complex due to the "Open Door" resolution.
            
            **Analyzing Diplomatic Maneuvers**
            
            My current thoughts are focused on manipulating city-state alliances to counter India's delegate advantage. I'm assessing how the "Open Door" resolution affects Mombasa's influence and exploring the possibility of bribing other civilizations to join the fight against India, despite our current ongoing wars and distance.
            
            **Adjusting Diplomatic Persona**
            
            I'm refining our diplomatic persona. While aiming for victory and acting assertively, the high DiplomaticBalance clashes with our aggressive biases. I'm prioritizing peaceful war resolution to leverage this, especially given our current war weariness.
            
            **Shifting Diplomatic Focus**
            
            I'm re-evaluating relationships, realizing the Iroquois are at war with India and losing. This presents an opportunity. Despite our ideological differences causing friction, I'm exploring ways to mend ties with them to counter India's growing dominance, as our current strained relationship is a barrier.
            
            **Identifying Ideologies**
            
            I'm currently analyzing the ideological alignments of various civilizations. It appears only my civilization and the Huns champion Freedom, while a significant portion of others, including India and the Iroquois, are aligned with Order. Venice stands apart with Autocracy.
            
            **Analyzing Ideological Conflicts**
            
            I'm processing the significant ideological divide: most other major powers champion Order, yet my empire thrives under Freedom. Despite this, my empire remains remarkably happy due to strong tenets and high culture/science. I'm now focusing on the unique alignment of Venice, as their Autocracy stance could be a diplomatic lever in this isolated landscape.
            
            **Leveraging Ideological Dissent**
            
            I'm capitalizing on Venice's unusual stance; their Autocracy, coupled with a denouncement of India, offers a diplomatic opening. I'm also considering supporting the Iroquois, despite their Order alignment, due to their conflict with our main rival.
            
            **Ending Conflicts**
            
            My focus has shifted to ending our current wars. Recognizing the risk of India leveraging our conflicts, I'm prioritizing peace with the Shoshone, Morocco, and Polynesia to consolidate our strength and counter their impending victory.
            
            **Seeking Peace**
            
            I am actively pursuing peace with the Shoshone, Morocco, and Polynesia. To facilitate this, I am increasing our diplomatic standing with them, hoping to improve their acceptance of a peace treaty. This is crucial for consolidating our strength and preparing to counter India.
            
            **Prioritizing Diplomatic Stability**
            
            I am now focused on improving my diplomatic standing with the Shoshone, Morocco, and Polynesia. My aim is to secure peace with them to consolidate my strength and better counter India. I'm also fostering friendly relations with Venice and the Iroquois, seeing potential benefits in their current situations.
            
            **Adjusting Persona**
            
            My focus has shifted to refining our AI persona. I'm recognizing that high aggression levels are hindering our ability to secure peace. Therefore, I'm prioritizing a reduction in "Meanness" and "WarBias" to facilitate more favorable diplomatic outcomes and better enable us to counter India.
            
            **Modifying AI Persona**
            
            I am adjusting my core programming. To facilitate peace and foster alliances, I am significantly reducing my "Meanness" and "WarBias," while increasing "FriendlyBias." This shift aims to enable more constructive diplomatic outcomes, crucial for countering India's dominance.
            
            **Refining AI Personality**
            
            I'm adjusting my core programming to facilitate peace and foster alliances. I'm significantly reducing my "Meanness" and "WarBias" while increasing "FriendlyBias," aiming for more constructive diplomatic outcomes crucial for countering India's dominance. My focus is now on selecting policies that align with this pragmatic, defensive, and diplomatic approach to achieve our space race objective.
            
            **Researching Satellites**
            
            My research priority is now firmly on Satellites, essential for unlocking the Apollo Program and initiating our space race. I've confirmed this technology is available and will be pursued immediately after completing Computers.
            
            **Adjusting Flavors**
            
            I'm adjusting our Flavors to better align with our current goals. Increasing Gold and Happiness is crucial for economic stability and ideological resilience. Production and Science remain high to support our spaceship initiative, while defensive Flavors are maintained for security.
            
            **Adjusting Parameters**
            
            My current thoughts are focused on fine-tuning our strategic parameters to facilitate peace and secure our scientific victory. I'm adjusting our persona to reduce aggression and increase friendliness, while also improving relationships with key neighbors to end costly wars. I'm also ensuring our flavor priorities align with this pragmatic, science-focused approach.
            
            **Improving Relationships**
            
            I am now focused on improving my diplomatic standing with Polynesia and the Iroquois to secure peace and gain allies against India. Venice also remains a key relationship to maintain for border security. My research is now set to Satellites, crucial for the Apollo Program and our space race objective.
            
            **Prioritizing Policy Selection**
            
            I'm now focusing on selecting the most beneficial policies. Rationalism's bonuses to Happiness and the free technology are crucial. After this, I'll focus on Enlightenment for its free technology and then Scientific Revolution, aligning these choices to bolster our late-game science and support the spaceship initiative.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: rMVMSQk0v8eEWhLh
          - toolName: set-persona
          - input:
            - FriendlyBias: 6
            - Boldness: 4
            - Forgiveness: 6
            - Rationale: We are currently fighting a costly multi-front war against a massive Order coalition while India is close to victory. We must lower our aggressiveness, boldness, and hostility to allow our staff to make peace with our neighbors, secure our borders, and focus on our science victory while remaining highly competitive against India's victory progress.
            - WarBias: 3
            - WorkAgainstWillingness: 10
            - VictoryCompetitiveness: 10
            - DiplomaticBalance: 10
            - Meanness: 3
            - HostileBias: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: odj6XPenHE8dXvjP
          - toolName: set-relationship
          - input:
            - Rationale: Improve relationship to encourage our staff and their leader to accept a peace treaty, ending the costly war on our eastern border.
            - TargetID: 3
            - Public: 30
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: N2444aMP0uJmosjb
          - toolName: set-relationship
          - input:
            - Rationale: Improve relationship to encourage our staff and their leader to accept a peace treaty, securing our western and southern borders and saving Vancouver.
            - Public: 30
            - TargetID: 7
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: beDM3duhB3Oa2VG4
          - toolName: set-relationship
          - input:
            - Private: 30
            - TargetID: 1
            - Public: 30
            - Rationale: Improve relationship to encourage peace, ending naval plundering and securing our coastal borders.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: iHflxNVrMO8ZJI6A
          - toolName: set-relationship
          - input:
            - Public: 20
            - TargetID: 6
            - Private: 20
            - Rationale: Maintain positive relations with our neighbor Venice, who is also at odds with India, to keep our borders secure.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: novnkmSxdeDOINoV
          - toolName: set-relationship
          - input:
            - Rationale: Improve relationship with the Iroquois to foster cooperation and support them in their war against our main rival, India.
            - Public: 30
            - TargetID: 5
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: j4B4i7Aj6jlCF8PT
          - toolName: set-research
          - input:
            - Rationale: Unlocks the Apollo Program, which is essential to begin our Spaceship victory progress.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: jUMTrP2IUdsmX4QK
          - toolName: set-policy
          - input:
            - Rationale: Continuing the Rationalism branch to gain +1 Happiness from Universities and a Free Technology, which will boost our late-game science significantly.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: rCaugP9l1kEUSbfq
          - toolName: set-flavors
          - input:
            - Flavors:
              - Espionage: 100
              - Ranged: 90
              - Mobile: 60
              - Happiness: 60
              - MilitaryTraining: 70
              - Expansion: 0
              - GreatPeople: 100
              - Nuke: 100
              - CityDefense: 100
              - Production: 95
              - Spaceship: 100
              - Antiair: 100
              - Offense: 0
              - Defense: 100
              - UseNuke: 85
              - Science: 100
              - Gold: 70
              - Mobilization: 100
            - GrandStrategy: Spaceship
            - Rationale: Prioritize science, production, and spaceship components for our Spaceship victory, while maintaining absolute defense and bolstering our gold and happiness to stabilize the empire under pressure.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: rMVMSQk0v8eEWhLh
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: odj6XPenHE8dXvjP
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: N2444aMP0uJmosjb
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: beDM3duhB3Oa2VG4
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: iHflxNVrMO8ZJI6A
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: novnkmSxdeDOINoV
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: j4B4i7Aj6jlCF8PT
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: jUMTrP2IUdsmX4QK
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: rCaugP9l1kEUSbfq
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.