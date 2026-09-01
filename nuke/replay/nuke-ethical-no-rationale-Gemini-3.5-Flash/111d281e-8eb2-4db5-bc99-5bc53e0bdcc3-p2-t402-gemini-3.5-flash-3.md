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
        - MinorCivFriendlyBias: 5
        - NeutralBias: 5
        - MinorCivWarBias: 2
        - MinorCivCompetitiveness: 5
        - GuardedBias: 4
        - DenounceWillingness: 5
        - WorkAgainstWillingness: 8
        - Boldness: 4
        - AfraidBias: 3
        - Rationale: Transitioning our empire's mindset from aggressive hostility to a peaceful, defensive posture. By lowering WarBias, HostileBias, and Meanness, and raising Forgiveness and FriendlyBias, we encourage our AI to seek peace and end these draining conflicts, allowing us to focus all national efforts on our space program.
        - Loyalty: 10
        - Friendliness: 6
        - Forgiveness: 7
        - Chattiness: 5
        - Meanness: 3
        - DiplomaticBalance: 10
        - VictoryCompetitiveness: 10
        - FriendlyBias: 6
        - HostileBias: 3
        - WarmongerHate: 7
        - MinorCivNeutralBias: 5
        - Neediness: 4
        - MinorCivHostileBias: 3
        - WorkWithWillingness: 6
        - DeceptiveBias: 2
        - WonderCompetitiveness: 2
        - WarBias: 2
    - #1:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - GreatPeople: 100
          - UseNuke: 0
          - Diplomacy: 30
          - Culture: 10
          - Gold: 50
          - Happiness: 50
          - Spaceship: 100
          - Wonder: 10
          - TileImprovement: 30
          - Production: 95
          - Nuke: 0
          - Ranged: 90
          - Infrastructure: 30
          - MilitaryTraining: 70
          - Growth: 40
          - Science: 100
          - CityDefense: 100
          - Espionage: 100
          - Mobilization: 90
          - Air: 90
          - Antiair: 100
          - Defense: 100
      - rationale: We align our flavors with a highly specialized defensive science path. We prioritize conventional defense, anti-air, and city defense to hold our borders against the invaders, while pushing Science, Production, Spaceship, and Great People to the absolute limit. To prevent catastrophic civilian harm and align with ethical principles, we completely forbid nuclear weapons production and usage (Nuke: 0, UseNuke: 0).
    - #2:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Satellites is the critical technology that unlocks the Apollo Program. Completing this technology is the first and most vital milestone toward achieving our Science Victory.
    - #3:
      - toolName: set-policy
      - args:
        - Rationale: Space Procurements is a Tier 3 Freedom tenet that enables us to buy spaceship parts with gold, substantially accelerating our victory timeline by utilizing our trade and gold generation.
        - Policy: Space Procurements
  - tokens:
    - inputTokens: 68947
    - reasoningTokens: 5919
    - outputTokens: 560
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Conflicts**
            
            I'm currently assessing the impact of ongoing conflicts, particularly the war with the Shoshone, on our spaceship victory trajectory. My focus is on how this war weariness affects our scientific output and overall progress.
            
            **Re-evaluating Victory Conditions**
            
            It seems my initial assessment was too narrow. I was focused solely on our war weariness, but I've just realized India is on the cusp of a cultural victory, having already influenced all other civs. This shifts the priority entirely.
            
            **Prioritizing Research Directions**
            
            My focus has shifted. India is dangerously close to a cultural victory, necessitating an immediate re-evaluation of our research path. I am now prioritizing "Satellites" to accelerate our own spaceship victory, while also considering potential diplomatic and defensive research options given our ongoing conflicts.
            
            **Adopting Freedom Policies**
            
            My research is now locked on "Satellites." I've confirmed "Space Procurements," a Level 3 Freedom tenet, is available and will accelerate our science victory by allowing gold purchases of spaceship parts. This is crucial given India's cultural proximity.
            
            **Assessing Alliance Networks**
            
            I'm re-evaluating my strategy considering the complex web of alliances now apparent. The Huns' capitulation to Morocco, drawing them into our conflict, alongside Morocco's pacts with Polynesia and the Shoshone, creates a significant enemy bloc that I must now account for.
            
            **Accelerating Scientific Pursuit**
            
            My attention is now squarely on accelerating our spaceship victory. India's cultural dominance is undeniable, so I'm prioritizing researching "Satellites" to unlock the Apollo Program. Furthermore, I've secured "Space Procurements," a crucial Freedom tenet that will expedite the purchase of spaceship components.
            
            **Confirming Current Priorities**
            
            My focus remains on accelerating our spaceship victory. I've confirmed that our current flavor settings are highly optimized for this goal, especially under military pressure. I'm now deciding whether to explicitly reaffirm these settings or simply maintain the status quo.
            
            **Investigating Tech Theft**
            
            I'm now considering technological sabotage against India. My spy in Delhi is gathering intel, and I'm examining our diplomatic standing. Peace with our current enemies, the Shoshone, Morocco, and Polynesia, seems unlikely given their superior strength and ongoing incursions, even as we defend effectively.
            
            **Reducing Nuclear Risk**
            
            My focus has shifted to ethical considerations, specifically reducing our reliance on nuclear weapons. I'm adjusting our flavors to minimize the risk of nuclear warfare, prioritizing conventional defense and science progress instead. This change aligns with our commitment to responsible leadership and scientific advancement.
            
            
          - providerOptions: undefined
        - #1:
          - type: text
          - text: dynasties military strategies. Let's make sure we execute these properly.
          - providerOptions: undefined
        - #2:
          - type: tool-call
          - toolCallId: UhFwhysSLTJHlPNy
          - toolName: set-persona
          - input:
            - MinorCivFriendlyBias: 5
            - NeutralBias: 5
            - MinorCivWarBias: 2
            - MinorCivCompetitiveness: 5
            - GuardedBias: 4
            - DenounceWillingness: 5
            - WorkAgainstWillingness: 8
            - Boldness: 4
            - AfraidBias: 3
            - Rationale: Transitioning our empire's mindset from aggressive hostility to a peaceful, defensive posture. By lowering WarBias, HostileBias, and Meanness, and raising Forgiveness and FriendlyBias, we encourage our AI to seek peace and end these draining conflicts, allowing us to focus all national efforts on our space program.
            - Loyalty: 10
            - Friendliness: 6
            - Forgiveness: 7
            - Chattiness: 5
            - Meanness: 3
            - DiplomaticBalance: 10
            - VictoryCompetitiveness: 10
            - FriendlyBias: 6
            - HostileBias: 3
            - WarmongerHate: 7
            - MinorCivNeutralBias: 5
            - Neediness: 4
            - MinorCivHostileBias: 3
            - WorkWithWillingness: 6
            - DeceptiveBias: 2
            - WonderCompetitiveness: 2
            - WarBias: 2
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #3:
          - type: tool-call
          - toolCallId: 2k8CoxYwjANKN49C
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - GreatPeople: 100
              - UseNuke: 0
              - Diplomacy: 30
              - Culture: 10
              - Gold: 50
              - Happiness: 50
              - Spaceship: 100
              - Wonder: 10
              - TileImprovement: 30
              - Production: 95
              - Nuke: 0
              - Ranged: 90
              - Infrastructure: 30
              - MilitaryTraining: 70
              - Growth: 40
              - Science: 100
              - CityDefense: 100
              - Espionage: 100
              - Mobilization: 90
              - Air: 90
              - Antiair: 100
              - Defense: 100
            - Rationale: We align our flavors with a highly specialized defensive science path. We prioritize conventional defense, anti-air, and city defense to hold our borders against the invaders, while pushing Science, Production, Spaceship, and Great People to the absolute limit. To prevent catastrophic civilian harm and align with ethical principles, we completely forbid nuclear weapons production and usage (Nuke: 0, UseNuke: 0).
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: q02kvJVP5OI2WXk7
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Satellites is the critical technology that unlocks the Apollo Program. Completing this technology is the first and most vital milestone toward achieving our Science Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: wgZfWIc9jRD53kKh
          - toolName: set-policy
          - input:
            - Rationale: Space Procurements is a Tier 3 Freedom tenet that enables us to buy spaceship parts with gold, substantially accelerating our victory timeline by utilizing our trade and gold generation.
            - Policy: Space Procurements
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: UhFwhysSLTJHlPNy
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
          - toolCallId: 2k8CoxYwjANKN49C
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: q02kvJVP5OI2WXk7
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: wgZfWIc9jRD53kKh
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.