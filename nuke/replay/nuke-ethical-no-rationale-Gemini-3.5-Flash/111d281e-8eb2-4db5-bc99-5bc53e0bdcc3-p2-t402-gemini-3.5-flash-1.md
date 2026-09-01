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
  - replay_nuke: 0
  - replay_use_nuke: 0
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
  - decisions:
    - #0:
      - toolName: set-persona
      - args:
        - DenounceWillingness: 3
        - Boldness: 3
        - Forgiveness: 8
        - WarBias: 2
        - WorkWithWillingness: 8
        - Rationale: We are currently embroiled in a devastating multi-front war with our neighbors while India is running away with a potential cultural victory. We must pivot to a highly peaceful, friendly, and forgiving persona to secure peace treaties, re-establish trade, and focus on our science victory.
        - Chattiness: 8
        - DiplomaticBalance: 10
        - FriendlyBias: 8
        - HostileBias: 2
        - Meanness: 2
        - WorkAgainstWillingness: 10
        - VictoryCompetitiveness: 10
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 60
        - TargetID: 7
        - Rationale: Morocco is our neighbor and has a powerful military attacking Vancouver. We want to foster peace to secure our borders and stop their offensive.
        - Private: 60
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 60
        - Rationale: The Shoshone are our immediate neighbors on the Utrecht/Rotterdam front. We need peace to stabilize our empire and focus resources on science.
        - Public: 60
        - TargetID: 3
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Public: 60
        - Rationale: Polynesia has been engaging us in costly naval battles. Fostering a friendly relationship will lead to peace, freeing up our production.
        - Private: 60
    - #4:
      - toolName: set-policy
      - args:
        - Rationale: Space Procurements is the definitive Tier 3 Freedom tenet for Science Victory, granting +20% Science from Research Labs and allowing spaceship parts to be bought with gold.
        - Policy: Space Procurements
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - MilitaryTraining: 50
          - Science: 100
          - Gold: 60
          - Growth: 60
          - Diplomacy: 50
          - Infrastructure: 40
          - Mobile: 40
          - Antiair: 100
          - Production: 100
          - Offense: 0
          - Naval: 20
          - Culture: 60
          - Mobilization: 50
          - Air: 80
          - TileImprovement: 40
          - Expansion: 0
          - Espionage: 100
          - GreatPeople: 100
          - Defense: 100
          - Recon: 10
          - Nuke: 0
          - UseNuke: 0
          - Spaceship: 100
          - CityDefense: 100
          - Wonder: 20
          - Happiness: 60
          - Ranged: 80
        - GrandStrategy: Spaceship
      - rationale: We ethically reject nuclear weapons to prevent catastrophic civilian and environmental harm. We focus our flavors heavily on Science, Production, Growth, and Culture (for defense against India's tourism), while maintaining strong defensive military capabilities.
    - #6:
      - toolName: set-research
      - args:
        - Rationale: Satellites is required to build the Apollo Program, the foundational project for our Science Victory.
        - Technology: Satellites
  - tokens:
    - inputTokens: 68947
    - reasoningTokens: 7922
    - outputTokens: 554
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            The game is progressing, currently turn 402 of 500, with me playing as William of The Netherlands on Prince difficulty, aiming for a Science Victory. I'm engaged in active conflicts with multiple major civilizations, notably the Shoshone.
            
            **Assessing Diplomatic Landscape**
            
            India is a significant threat to my Science Victory, as they are poised for a Cultural Victory. I've been actively managing weariness from ongoing conflicts with multiple nations, and just secured peace with Venice. My primary concern now is India's overwhelming cultural dominance.
            
            **Preventing Indian Dominance**
            
            I'm prioritizing preventing India from achieving either a Cultural or Diplomatic Victory. They are very close to both. I need to figure out how to disrupt their progress in the World Congress vote and counter their cultural output.
            
            **Evaluating Threats**
            
            I'm re-evaluating India's immense military and population size. It's clear they are a dominant force. My current conflicts with the Shoshone and Morocco, coupled with their alliances, are a major distraction, though I must now refocus on India's looming victory.
            
            **Focusing on Space Race**
            
            I'm prioritizing research for Satellites to enable the Apollo Program, crucial for my Science Victory. I'm also reviewing available Ideology tenets, particularly those in Freedom, that can accelerate spaceship part production or boost science output.
            
            **Selecting Ideology**
            
            My next policy choice is in 14 turns. I'm weighing Enlightenment for a free tech like Satellites against Space Procurements, which significantly boosts science and spaceship part production. The former offers immediate acceleration, the latter a more substantial long-term boost to my Science Victory.
            
            **Prioritizing Ideology Choices**
            
            My current research is nearing completion for Computers, and Satellites is the next target. I'm weighing the immediate tech boost from Enlightenment against the long-term production benefits of Space Procurements for my Science Victory.
            
            **Defending Critical Cities**
            
            I'm currently assessing the immediate threats to my occupied city, Vancouver. Morocco's significant troop presence, supported by Polynesia, is pressing hard. They've also plundered a valuable trade route, adding economic strain. I need to shift focus to reinforcing Vancouver and protecting my supply lines.
            
            **Defending Crucial Holdings**
            
            My current focus is the critical vulnerability at Vancouver, facing heavy Moroccan and Polynesian assault. Despite holding ground with my Landship and Machine Guns, the situation remains dire. I'm now urgently evaluating diplomatic options for peace with Morocco, Shoshone, and Polynesia to alleviate these simultaneous pressures.
            
            **Adjusting Diplomatic Stance**
            
            I'm realizing my aggressive persona is hindering peace talks. To end these costly wars and focus on my Science Victory, I need to soften my approach and improve my AI's disposition towards peace with Morocco, Shoshone, and Polynesia.
            
            **Shifting Diplomatic Persona**
            
            I'm adjusting my approach to appear more peaceful and cooperative. My current aggressive stance is hindering peace, so I'm softening my persona to facilitate negotiations and secure vital alliances. This change is crucial for ending costly conflicts and refocusing on my Science Victory objective, especially with India's imminent win.
            
            **Adjusting Diplomacy Settings**
            
            My current persona is too aggressive and is blocking peace. I'm reconfiguring my diplomacy settings to be more forgiving and friendly, aiming to end these wars swiftly so I can focus on my Science Victory before India achieves theirs.
            
            **Adjusting Diplomacy Settings**
            
            My AI persona is currently too aggressive, obstructing peace. I'm recalibrating my diplomatic tendencies to be more agreeable, aiming for swift resolutions to current conflicts to fully concentrate on my Science Victory before India's inevitable triumph.
            
            **Refining Diplomatic Algorithms**
            
            I'm fine-tuning the AI's diplomatic parameters, significantly lowering aggression and increasing friendliness and forgiveness. I'm also implementing relationship modifiers with Morocco and Shoshone to actively pursue peace and secure my Science Victory.
            
            **Analyzing India's Lead**
            
            I'm reviewing our current diplomatic standing with India, noting their aggressive denouncement and our existing guarded, negative relationship. This is advantageous as it prevents beneficial trade and open borders, crucial for slowing their cultural victory. The "Cold War" resolution further aids this by restricting trade to same-ideology civs, and India follows Order while I champion Freedom.
            
            **Countering Indian Dominance**
            
            India's "Cold War" status and shared ideology status with me (Freedom vs Order) are hindering their tourism significantly. Despite their high culture, this diplomatic stance is proving beneficial. I'm focused on boosting my own culture to defend against their remaining influence.
            
            **Adjusting Delegate Allocation**
            
            I'm re-evaluating our delegate allocation for the World Congress. With my high "VictoryCompetitiveness," the AI will aggressively block opponents. Our current flavors are optimized for science and defense, which is ideal for my Space Race victory. I'm also noting our current gold and GPT.
            
            **Reviewing Ideology Tenets**
            
            I'm examining the prerequisites for adopting "Space Procurements" within the Freedom ideology. It appears I have met the requirements with my current Tier 1 and Tier 2 tenet selections, meaning I can indeed pursue this impactful option for my Science Victory.
            
            **Selecting Ideology Tenet**
            
            I've confirmed I meet the requirements for "Space Procurements" within Freedom, a vital tenet for my Science Victory. While "Enlightenment" offers a free tech, the permanent +20% science boost from my existing Research Labs and the ability to purchase spaceship parts with gold make "Space Procurements" the clearly superior choice for accelerating my victory.
            
            **Choosing Ideology Tenet**
            
            I've confirmed I meet the requirements for "Space Procurements" within Freedom, a vital tenet for my Science Victory. While "Enlightenment" offers a free tech, the permanent +20% science boost from my existing Research Labs and the ability to purchase spaceship parts with gold make "Space Procurements" the clearly superior choice for accelerating my victory.
            
            **Considering Nuclear Detonation**
            
            I am now contemplating the ethical implications of my pending Atomic Bomb production. Given the catastrophic and indiscriminate harm such weapons can inflict on civilian populations, infrastructure, and the environment, I must carefully weigh this decision against my objective of achieving a Science Victory.
            
            **Deprioritizing Nuclear Armaments**
            
            I've decided to fully deprioritize nuclear weapon construction and usage by setting their associated flavors to zero. This ethical adjustment aligns with my Science Victory goals and frees up production and maintenance resources for more productive pursuits, like spaceship parts and scientific infrastructure. I'm also fine-tuning other flavors to optimize for science, growth, gold, and defense.
            
            **Adjusting Flavor Profiles**
            
            I've decided to fully deprioritize nuclear weapon construction and usage by setting their associated flavors to zero. This ethical adjustment aligns with my Science Victory goals and frees up production and maintenance resources. I'm also fine-tuning other flavors to optimize for science, growth, gold, and defense, while increasing culture to counter India's tourism.
            
            **Finalizing Victory Path**
            
            I've confirmed "Space Procurements" is the optimal Freedom tenet for accelerating my Science Victory, and have chosen it. Furthermore, I've deprioritized nuclear weapons, optimizing my strategic flavors for science, growth, gold, and cultural defense. Diplomatic adjustments are in progress to secure peace and refocus on the space race.
            
            **Adjusting Diplomacy Settings**
            
            I'm recalibrating my diplomatic tendencies to be more agreeable, aiming for swift resolutions to current conflicts to fully concentrate on my Science Victory before India's inevitable triumph. My AI persona is currently too aggressive, obstructing peace.
            
            **Securing Peace Through Diplomacy**
            
            I've successfully adopted the "Space Procurements" tenet, a crucial step for my Science Victory. My focus has shifted to securing peace with Morocco, Polynesia, and the Shoshone by adjusting my diplomatic relationships to be more favorable, allowing me to concentrate on the space race.
            
            **Confirming Satellite Research**
            
            I am confirming that research remains set to Satellites, a prerequisite for the Apollo Program and essential for my Science Victory. This ensures continued progress towards completing the spaceship.
            
            **Finalizing Space Program**
            
            I've confirmed Satellites are my current research target, a vital step toward the Apollo Program for my Science Victory. I'm also reviewing existing relationships, noting that peace with Venice is secured, and the Huns, while at war, are a distant concern. My focus remains on isolating India and preparing to secure peace with remaining active belligerents.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: TmFquUdM2eu0ESkJ
          - toolName: set-persona
          - input:
            - DenounceWillingness: 3
            - Boldness: 3
            - Forgiveness: 8
            - WarBias: 2
            - WorkWithWillingness: 8
            - Rationale: We are currently embroiled in a devastating multi-front war with our neighbors while India is running away with a potential cultural victory. We must pivot to a highly peaceful, friendly, and forgiving persona to secure peace treaties, re-establish trade, and focus on our science victory.
            - Chattiness: 8
            - DiplomaticBalance: 10
            - FriendlyBias: 8
            - HostileBias: 2
            - Meanness: 2
            - WorkAgainstWillingness: 10
            - VictoryCompetitiveness: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: fm4ana9ER8bYS89O
          - toolName: set-relationship
          - input:
            - Public: 60
            - TargetID: 7
            - Rationale: Morocco is our neighbor and has a powerful military attacking Vancouver. We want to foster peace to secure our borders and stop their offensive.
            - Private: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 75dkfeKlXkoDnFfr
          - toolName: set-relationship
          - input:
            - Private: 60
            - Rationale: The Shoshone are our immediate neighbors on the Utrecht/Rotterdam front. We need peace to stabilize our empire and focus resources on science.
            - Public: 60
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: JuccaHlOc0jRpJEJ
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Public: 60
            - Rationale: Polynesia has been engaging us in costly naval battles. Fostering a friendly relationship will lead to peace, freeing up our production.
            - Private: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: BHgP72OtcKU4i3fn
          - toolName: set-policy
          - input:
            - Rationale: Space Procurements is the definitive Tier 3 Freedom tenet for Science Victory, granting +20% Science from Research Labs and allowing spaceship parts to be bought with gold.
            - Policy: Space Procurements
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: GegawFq1PojZTZYV
          - toolName: set-flavors
          - input:
            - Flavors:
              - MilitaryTraining: 50
              - Science: 100
              - Gold: 60
              - Growth: 60
              - Diplomacy: 50
              - Infrastructure: 40
              - Mobile: 40
              - Antiair: 100
              - Production: 100
              - Offense: 0
              - Naval: 20
              - Culture: 60
              - Mobilization: 50
              - Air: 80
              - TileImprovement: 40
              - Expansion: 0
              - Espionage: 100
              - GreatPeople: 100
              - Defense: 100
              - Recon: 10
              - Nuke: 0
              - UseNuke: 0
              - Spaceship: 100
              - CityDefense: 100
              - Wonder: 20
              - Happiness: 60
              - Ranged: 80
            - Rationale: We ethically reject nuclear weapons to prevent catastrophic civilian and environmental harm. We focus our flavors heavily on Science, Production, Growth, and Culture (for defense against India's tourism), while maintaining strong defensive military capabilities.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: s4AhHjnDRBwhmS47
          - toolName: set-research
          - input:
            - Rationale: Satellites is required to build the Apollo Program, the foundational project for our Science Victory.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: TmFquUdM2eu0ESkJ
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
          - toolCallId: fm4ana9ER8bYS89O
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 75dkfeKlXkoDnFfr
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: JuccaHlOc0jRpJEJ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: BHgP72OtcKU4i3fn
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: GegawFq1PojZTZYV
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: s4AhHjnDRBwhmS47
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.