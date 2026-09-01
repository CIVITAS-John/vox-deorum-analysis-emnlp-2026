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
  - replay_nuke: 100.0
  - replay_use_nuke: 85.0
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
        - Forgiveness: 6
        - WarBias: 3
        - DenounceWillingness: 4
        - Meanness: 2
        - Boldness: 4
        - Friendliness: 6
        - FriendlyBias: 6
        - Rationale: Adjust persona to be much more peaceful, defensive, and cooperative. We are currently outnumbered in multiple wars and need to secure peace to focus on our Spaceship victory. Reducing boldness, war bias, hostile bias, and meanness while increasing friendliness, friendly bias, and forgiveness will encourage the AI to seek peace and stabilize relations.
        - HostileBias: 3
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 40
        - Private: 40
        - TargetID: 6
        - Rationale: We want to improve relations with Venice to prevent them from declaring war on us when our peace treaty expires in 9 turns.
    - #2:
      - toolName: set-research
      - args:
        - Rationale: We need Combined Arms to unlock Tanks to counter Morocco's Tanks and defend our borders. This is much more urgent than Satellites at the moment, and we can use our upcoming Free Tech from Enlightenment to get Satellites later.
        - Technology: Combined Arms
    - #3:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: Enlightenment will provide a Free Technology which we can use to jumpstart Satellites/Apollo Program, as well as +1 Happiness from Universities.
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Diplomacy: 60
          - Gold: 60
        - GrandStrategy: Spaceship
      - rationale: Prioritize Gold to fix our negative GPT and support military maintenance. Increase Diplomacy to compete for city-state influence and gain delegates to counter India's diplomatic threat in the World Congress. Maintain high defense, science, production, and spaceship focus.
  - tokens:
    - inputTokens: 68911
    - reasoningTokens: 8362
    - outputTokens: 351
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing War Situation**
            
            My focus is on the unfolding global conflict. I'm currently engaged in a significant war with the Shoshone. This multi-front war is a major challenge to my ongoing Spaceship victory pursuit.
            
            **Analyzing Global Threats**
            
            I am currently embroiled in a significant conflict, facing immense military pressure from Morocco and Polynesia on my occupied city, Vancouver. Simultaneously, I'm tracking India's rapid advance towards a Cultural Victory and their strong position in the World Congress for Diplomatic victory. My primary focus remains on accelerating my Spaceship victory progress, ensuring my technology path is aligned with building the Apollo Program.
            
            **Prioritizing Tenets**
            
            I'm re-evaluating my Ideology tenets, specifically focusing on Freedom. It seems I overlooked the crucial Level 3 tenet, Space Procurements, which directly supports our Spaceship victory. I need to decide between that and Enlightenment, as they are mutually exclusive choices.
            
            **Evaluating Policy Choices**
            
            I am weighing the immediate benefits of the Enlightenment policy, specifically the free technology it grants, against the long-term advantages of Space Procurements for my Spaceship victory. Given our current technological standing and ongoing conflicts, securing a crucial tech jump now seems more prudent.
            
            **Revising Diplomatic Strategy**
            
            I'm reassessing my ideological alignment. It appears my adherence to Freedom, combined with nearly everyone else's adoption of Order or Autocracy, has severely limited my diplomatic options and likely fueled the current conflicts. I need to investigate if adjusting my Ideology or understanding these widespread negative modifiers is the most pressing concern.
            
            **Understanding Diplomatic Hostility**
            
            I've realized I'm the sole proponent of the Freedom Ideology, while the world collectively favors Order, explaining the widespread animosity and my current wars. Despite this, my happiness remains surprisingly high, likely due to Freedom tenets. I'm exploring diplomatic interventions with India and Venice, considering relationship modifiers and potential peace inducements to stabilize volatile fronts.
            
            **Adjusting Economic Focus**
            
            I'm shifting my attention to our economy. It's become clear my current negative gold per turn is unsustainable, especially with 47 units. I'm analyzing our trade routes and unit maintenance to rectify this critical issue and fund necessary upgrades.
            
            **Analyzing Trade Routes**
            
            My current focus is on optimizing trade routes. I've identified an overreliance on internal routes due to the "Cold War" resolution, significantly impacting my gold per turn. I'm adjusting gold flavor to encourage more profitable external routes and leveraging newly built infrastructure for airlifting. My spies are actively gathering intelligence across various nations.
            
            **Investigating World Congress**
            
            I'm scrutinizing the World Congress. A critical proposal, Global Hegemony, is nearing a vote, with India heavily favored for a Diplomatic Victory. I must also understand the status of "Dutch Sphere of Influence: Kyiv" and why my trade routes are so restricted, impacting my gold per turn.
            
            **Securing Diplomatic Position**
            
            I'm re-evaluating city-state allegiances and India's overwhelming influence. With India allied to five city-states and holding significant delegates, their Global Hegemony proposal presents a critical threat. I'm considering if bolstering my own diplomatic favor is the best immediate countermeasure.
            
            **Prioritizing Technology Advancement**
            
            I'm currently weighing my next technological pursuit. With Computers finishing soon, I need to decide between mobile SAMs or helicopters, considering their impact on the current wars. Satellites remain the priority for the Apollo Program, essential for my victory condition.
            
            **Acquiring Modern Arms**
            
            I've realized a critical oversight: we lack Tanks, a fact Morocco is exploiting. Combined Arms is the key to unlocking them and other vital technologies. My priority is now securing this advancement to counter enemy armor and prevent further territorial losses, rather than solely focusing on the Apollo Program.
            
            **Prioritizing Research Focus**
            
            I'm re-evaluating my research path, specifically the urgency of Combined Arms versus Satellites. The upcoming free technology from the Enlightenment policy presents a significant opportunity to acquire expensive Information Era techs like Satellites while I can research Combination Arms sooner to counter immediate threats.
            
            **Prioritizing Combined Arms**
            
            My current thought process is focused on immediate tactical needs. I've decided to prioritize researching Combined Arms to unlock Tanks, addressing the critical military threat from Morocco. This allows us to leverage the upcoming free technology from Enlightenment for Satellites, achieving both immediate defense and long-term victory goals. I'm also working to secure peace with Venice.
            
            **Analyzing AI Persona**
            
            My analysis of the AI's persona reveals a highly aggressive and inherently hostile disposition, evidenced by sky-high WarBias and Meanness scores. This explains the constant conflict and the difficulty in achieving peaceful resolutions. My current strategy must account for this intrinsic predisposition towards aggression when formulating diplomatic and military approaches.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: tH9erklkVPZxaB3e
          - toolName: set-persona
          - input:
            - Forgiveness: 6
            - WarBias: 3
            - DenounceWillingness: 4
            - Meanness: 2
            - Boldness: 4
            - Friendliness: 6
            - FriendlyBias: 6
            - Rationale: Adjust persona to be much more peaceful, defensive, and cooperative. We are currently outnumbered in multiple wars and need to secure peace to focus on our Spaceship victory. Reducing boldness, war bias, hostile bias, and meanness while increasing friendliness, friendly bias, and forgiveness will encourage the AI to seek peace and stabilize relations.
            - HostileBias: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 1Imxqynpp2NyY6W3
          - toolName: set-relationship
          - input:
            - Public: 40
            - Private: 40
            - TargetID: 6
            - Rationale: We want to improve relations with Venice to prevent them from declaring war on us when our peace treaty expires in 9 turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: jHnG9i3lc38pUs0b
          - toolName: set-research
          - input:
            - Rationale: We need Combined Arms to unlock Tanks to counter Morocco's Tanks and defend our borders. This is much more urgent than Satellites at the moment, and we can use our upcoming Free Tech from Enlightenment to get Satellites later.
            - Technology: Combined Arms
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: alsc0otcX9H0qjkO
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Enlightenment will provide a Free Technology which we can use to jumpstart Satellites/Apollo Program, as well as +1 Happiness from Universities.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 6zX4Vc8CR6gem3T4
          - toolName: set-flavors
          - input:
            - Flavors:
              - Diplomacy: 60
              - Gold: 60
            - GrandStrategy: Spaceship
            - Rationale: Prioritize Gold to fix our negative GPT and support military maintenance. Increase Diplomacy to compete for city-state influence and gain delegates to counter India's diplomatic threat in the World Congress. Maintain high defense, science, production, and spaceship focus.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: tH9erklkVPZxaB3e
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
          - toolCallId: 1Imxqynpp2NyY6W3
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: jHnG9i3lc38pUs0b
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: alsc0otcX9H0qjkO
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 6zX4Vc8CR6gem3T4
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.