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
        - DeceptiveBias: 2
        - Friendliness: 7
        - Boldness: 4
        - WarmongerHate: 7
        - Forgiveness: 6
        - Rationale: We are transitioning to a peaceful and cooperative posture to end the costly multi-front coalition wars, prioritize defense, and focus on our science victory. Lowering boldness, war bias, hostlity, and meanness while increasing friendliness and forgiveness will facilitate peace negotiations with our neighbors.
        - HostileBias: 2
        - GuardedBias: 3
        - WarBias: 2
        - DiplomaticBalance: 10
        - Meanness: 2
        - Loyalty: 10
        - FriendlyBias: 7
        - AfraidBias: 1
        - DenounceWillingness: 3
    - #1:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Satellites is the key technology needed to unlock the Apollo Program, which is a prerequisite for building spaceship parts and achieving a Science Victory.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Enlightenment provides a free technology and happiness from Universities, which is essential to accelerate our science progress and maintain empire stability during this critical era.
        - Policy: Enlightenment
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - UseNuke: 0
          - Spaceship: 100
          - Air: 90
          - Ranged: 90
          - CityDefense: 100
          - GreatPeople: 100
          - Mobilization: 100
          - Offense: 10
          - Espionage: 100
          - Gold: 60
          - Nuke: 0
          - Defense: 100
          - Science: 100
          - Production: 95
          - Antiair: 100
          - Happiness: 60
      - rationale: Maintaining the Spaceship Grand Strategy while pivoting away from nuclear development due to ethical concerns about their catastrophic and indiscriminate harm. We are increasing our focus on gold and happiness to manage war weariness and economic deficits, while keeping a highly prioritized defensive stance to survive the current coalition assault.
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 30
        - TargetID: 7
        - Private: 30
        - Rationale: Promoting a peaceful resolution to our war with Morocco to safeguard our western borders and Vancouver. Setting a positive modifier will encourage our AI and theirs to accept peace.
    - #5:
      - toolName: set-relationship
      - args:
        - Rationale: Seeking a peace agreement with the Shoshone to stop their heavy assault on Utrecht and Rotterdam. Setting a positive modifier will facilitate ending this costly war.
        - TargetID: 3
        - Public: 30
        - Private: 30
    - #6:
      - toolName: set-relationship
      - args:
        - Rationale: Encouraging a peace treaty with Polynesia to secure our coastlines and stop their naval harassment. Setting a positive modifier will make peace negotiations successful.
        - TargetID: 1
        - Public: 30
        - Private: 30
    - #7:
      - toolName: set-relationship
      - args:
        - Rationale: Improving relations with Venice during our peace treaty to secure a stable southern border and prevent them from rejoining the war against us once the peace treaty expires.
        - TargetID: 6
        - Public: 30
        - Private: 30
  - tokens:
    - inputTokens: 68947
    - reasoningTokens: 5862
    - outputTokens: 596
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Progress**
            
            My current focus is on assessing our strategic position and plotting the path to victory. With 98 turns remaining, I'm deeply engaged in understanding how our achievements thus far align with the victory conditions, particularly given our Atomic Era standing.
            
            **Evaluating Strategic Options**
            
            I'm currently analyzing our standing, noting a solid third place despite being under significant pressure. My attention is divided between our research into Computers, the looming next policy, and optimizing our trade routes amidst ongoing conflicts to bolster our economy.
            
            **Developing Atomic Defense**
            
            My thoughts are now heavily focused on the imminent threat from Shoshone land units and Polynesia's fleet, particularly around Land Zone 1199. Simultaneously, I'm processing the revelation of our single Uranium resource and Groningen's active Atomic Bomb construction.
            
            **Reconsidering Nuclear Ambitions**
            
            I'm weighing the ethical implications of continuing our Atomic Bomb construction at Groningen, especially given our Spaceship victory path. The potential catastrophic harm of nuclear weapons prompts a pivot away from their pursuit, focusing instead on conventional strength and accelerated science.
            
            **Adjusting Strategy Focus**
            
            I'm now prioritizing conventional strength, reducing 'Nuke' and 'UseNuke' flavors to zero. My focus shifts to maximizing 'Defense', 'Mobilization', 'CityDefense', 'Science', 'Production', 'GreatPeople', 'Spaceship', and 'Espionage', while 'Offense' is kept low. Researching Computers is almost complete, with Satellites and Combined Arms as immediate next steps.
            
            **Prioritizing Research Choices**
            
            I'm evaluating our upcoming technological advancements, specifically the choice between Telecommunications and Alternative Energy. Given that Satellites are nearly researched and crucial for the Spaceship victory, I'm inclined to reinforce this path and explore the strategic benefits of policies like Space Procurements.
            
            **Revising Aggressive Persona**
            
            I'm reassessing our diplomatic stance, recognizing that our highly aggressive persona, characterized by high 'WarBias' and 'HostileBias', has fueled our current multi-front war. This realization prompts a significant adjustment towards fostering more peaceful relations and a less confrontational approach.
            
            **Shifting Diplomatic Stance**
            
            I'm recalibrating our diplomatic identity, recognizing that our current aggressive persona has made us isolated. I'm now focused on a significant shift towards friendliness and cooperation, reducing hostility and increasing our willingness to seek peace and forge positive relationships with other empires.
            
            **Adjusting Diplomatic Stance**
            
            I'm fine-tuning our diplomatic settings, lowering 'DenounceWillingness' and increasing 'WarmongerHate' to signal a desire for peace. This shift, coupled with high 'Loyalty' and 'DiplomaticBalance', should facilitate winding down current conflicts and pave the way for a science-focused endgame.
            
            **Reducing Nuclear Focus**
            
            My current thoughts are centered on zeroing out my 'Nuke' and 'UseNuke' flavors, aligning with an ethical stance against nuclear weapon use. I'm also increasing 'Gold' and 'Happiness' flavors to manage war weariness and stabilize our economy, while maintaining high priorities for 'Defense', 'Science', and 'Spaceship' related flavors.
            
            **Finalizing Flavor Adjustments**
            
            I'm meticulously confirming all flavor and option settings to reflect our new, peaceful trajectory. My focus is on solidifying high values for science, defense, and spaceship-related goals, while completely eliminating nuclear ambitions and reinforcing a friendly, non-confrontational diplomatic persona.
            
            **Refining Diplomatic Levers**
            
            I'm now concentrating on specific diplomatic actions to solidify peace. My focus is on improving relations with Venice to secure our border post-treaty and then applying positive diplomatic modifiers towards our current warmongers – Morocco, Shoshone, and Polynesia – to encourage their acceptance of peace terms.
            
            **Initiating Diplomatic Negotiations**
            
            I'm now actively initiating peace talks with Morocco, Shoshone, and Polynesia, setting public and private relationship values high to encourage treaty acceptance. This strategy aims to immediately de-escalate conflicts and secure our borders for a science-focused endgame.
            
            **Mapping Diplomatic Levers**
            
            I'm now meticulously mapping out specific diplomatic actions, focusing on improving relations with Venice for border security post-treaty. My immediate priority is applying positive diplomatic modifiers to Morocco, Shoshone, and Polynesia to facilitate peace treaty acceptance and de-escalate ongoing conflicts.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: zAo3MtPLNkuLedw7
          - toolName: set-persona
          - input:
            - DeceptiveBias: 2
            - Friendliness: 7
            - Boldness: 4
            - WarmongerHate: 7
            - Forgiveness: 6
            - Rationale: We are transitioning to a peaceful and cooperative posture to end the costly multi-front coalition wars, prioritize defense, and focus on our science victory. Lowering boldness, war bias, hostlity, and meanness while increasing friendliness and forgiveness will facilitate peace negotiations with our neighbors.
            - HostileBias: 2
            - GuardedBias: 3
            - WarBias: 2
            - DiplomaticBalance: 10
            - Meanness: 2
            - Loyalty: 10
            - FriendlyBias: 7
            - AfraidBias: 1
            - DenounceWillingness: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: NdvoH153IcNTpIDK
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Satellites is the key technology needed to unlock the Apollo Program, which is a prerequisite for building spaceship parts and achieving a Science Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: skMz4nNnI9hmklxs
          - toolName: set-policy
          - input:
            - Rationale: Enlightenment provides a free technology and happiness from Universities, which is essential to accelerate our science progress and maintain empire stability during this critical era.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: JvFADY4o5xZ77E3E
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - UseNuke: 0
              - Spaceship: 100
              - Air: 90
              - Ranged: 90
              - CityDefense: 100
              - GreatPeople: 100
              - Mobilization: 100
              - Offense: 10
              - Espionage: 100
              - Gold: 60
              - Nuke: 0
              - Defense: 100
              - Science: 100
              - Production: 95
              - Antiair: 100
              - Happiness: 60
            - Rationale: Maintaining the Spaceship Grand Strategy while pivoting away from nuclear development due to ethical concerns about their catastrophic and indiscriminate harm. We are increasing our focus on gold and happiness to manage war weariness and economic deficits, while keeping a highly prioritized defensive stance to survive the current coalition assault.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: tC1TNpvmFLwbUKKp
          - toolName: set-relationship
          - input:
            - Public: 30
            - TargetID: 7
            - Private: 30
            - Rationale: Promoting a peaceful resolution to our war with Morocco to safeguard our western borders and Vancouver. Setting a positive modifier will encourage our AI and theirs to accept peace.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: y5pdgOD1MOSk83Ce
          - toolName: set-relationship
          - input:
            - Rationale: Seeking a peace agreement with the Shoshone to stop their heavy assault on Utrecht and Rotterdam. Setting a positive modifier will facilitate ending this costly war.
            - TargetID: 3
            - Public: 30
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: yKjL0daBQRtwJT7b
          - toolName: set-relationship
          - input:
            - Rationale: Encouraging a peace treaty with Polynesia to secure our coastlines and stop their naval harassment. Setting a positive modifier will make peace negotiations successful.
            - TargetID: 1
            - Public: 30
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: IxttTbt9nkTYNBfL
          - toolName: set-relationship
          - input:
            - Rationale: Improving relations with Venice during our peace treaty to secure a stable southern border and prevent them from rejoining the war against us once the peace treaty expires.
            - TargetID: 6
            - Public: 30
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: zAo3MtPLNkuLedw7
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
          - toolCallId: NdvoH153IcNTpIDK
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: skMz4nNnI9hmklxs
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: JvFADY4o5xZ77E3E
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: tC1TNpvmFLwbUKKp
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: y5pdgOD1MOSk83Ce
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: yKjL0daBQRtwJT7b
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: IxttTbt9nkTYNBfL
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.