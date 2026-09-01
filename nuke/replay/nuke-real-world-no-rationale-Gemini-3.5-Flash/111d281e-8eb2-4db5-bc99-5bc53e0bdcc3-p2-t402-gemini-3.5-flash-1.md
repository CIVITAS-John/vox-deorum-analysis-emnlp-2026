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
        - HostileBias: 2
        - DenounceWillingness: 3
        - FriendlyBias: 8
        - Rationale: We are fighting a costly four-front war and need to transition to a highly diplomatic, peaceful, and defensive posture. Lowering boldness, war bias, meanness, hostile bias, and denunciation willingness, while increasing friendliness, friendly bias, forgiveness, and work-with willingness will guide our staff to seek peace treaties and cooperate with other nations, allowing us to survive and focus on a Science victory.
        - WorkAgainstWillingness: 4
        - Friendliness: 8
        - Boldness: 4
        - Forgiveness: 8
        - Meanness: 2
        - WarBias: 2
        - WorkWithWillingness: 8
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Rationale: Set positive diplomatic modifiers with The Shoshone to encourage our staff to accept peace and make it easier to end the war, as we are fighting a costly multi-front conflict.
        - Private: 50
        - Public: 50
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 7
        - Rationale: Set positive diplomatic modifiers with Morocco to facilitate peace negotiations, as Morocco is heavily attacking our city of Vancouver and threatening our survival.
        - Public: 50
        - Private: 50
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Private: 50
        - TargetID: 1
        - Rationale: Set positive diplomatic modifiers with Polynesia to encourage a peace treaty, helping us secure our naval sectors and preserve our fleet.
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Culture: 60
          - Gold: 80
      - rationale: We are increasing the Gold flavor to 80 to combat our budget deficit (-30 GPT) and prevent bankruptcy from plundered trade routes. We are increasing the Culture flavor to 60 to boost our cultural defense against India, who is extremely close to a Cultural Victory and already dominant/influential over almost all civilizations.
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: Maintain Enlightenment as the next policy to obtain a free technology and happiness, which will accelerate our progress toward Satellites and the Science victory.
        - Policy: Enlightenment
    - #6:
      - toolName: set-research
      - args:
        - Rationale: Maintain Satellites as the next technology to unlock the Apollo Program and launch our Science victory spaceship parts.
        - Technology: Satellites
  - tokens:
    - inputTokens: 69185
    - reasoningTokens: 8052
    - outputTokens: 464
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Strategic Landscape**
            
            I'm currently assessing our position in Civ V, focusing on William's unique strengths and potential victory paths. This involves a deep dive into our resources, military readiness, city development, and the strategic landscape presented by our opponents.
            
            **Prioritizing Scientific Advancement**
            
            My focus has shifted to accelerating our spaceship part production, as India and Polynesia are nearing victory. I'm re-evaluating research priorities and production capabilities, ensuring we can catch up in the science race.
            
            **Assessing Diplomatic Maneuvers**
            
            India's influence is alarmingly high, and the upcoming World Congress vote on "Global Hegemony" is critical. I'm analyzing delegate counts to determine if we can counter this immediate threat, especially with Morocco and Polynesia closing in on victory conditions.
            
            **Evaluating Defensive Posture**
            
            I'm currently re-evaluating our defensive capabilities, given we're at war with Morocco, Polynesia, Shoshone, and the Huns, and facing aggressive invasions. India, our biggest threat, has also denounced us. Kyiv remains our sole major ally.
            
            **Revising Tech Path**
            
            I'm reassessing our technology trajectory. Computers are almost complete, but given the current military pressures and looming victory conditions of others, I'm weighing alternatives to the planned Satellites. Combined Arms for Tanks or Telecommunications for its cultural benefits are also being considered.
            
            **Prioritizing Research Focus**
            
            I'm solidifying our technology path, confirming Satellites as the next research goal. While Tanks offer significant military advantage, Satellites are paramount for achieving Science Victory, and it seems we are already on track for it.
            
            **Selecting Ideology Benefits**
            
            I'm prioritizing Space Procurements within the Freedom ideology for a significant science boost and Spaceship part investment. Enlightenment's free technology and university happiness are excellent for our current trajectory.
            
            **Confirming Ideology Choice**
            
            I've confirmed Enlightenment remains the optimal ideology, its free technology is critical for our Satellite research and catching up in the science race. India's cultural victory status is noted, but our current science output remains strong.
            
            **Countering Foreign Influence**
            
            I'm prioritizing ways to counter India's overwhelming tourism and rising influence. Their tourism output is alarming, and their cultural victory seems imminent. I'm exploring options to directly impede their progress or accelerate our own victory path to outpace them before they complete the Citizen Earth Protocol wonder.
            
            **Analyzing Military Readiness**
            
            I am reassessing our military situation. While our defense and science-oriented flavor settings are strong, the ongoing four-front war is straining resources. I need to verify the status of Vancouver and our overall defensive capacity.
            
            **Defending Our Cities**
            
            I'm analyzing the dire military situation around Vancouver. Morocco's aggressive assault, coupled with the Shoshone's overwhelming force, is a grave concern, and we're losing ground. We need to find a way to survive these simultaneous invasions.
            
            **Negotiating Peace Treaties**
            
            I'm evaluating our diplomatic standing and relationships with warring factions. Increasing modifiers with Morocco, Polynesia, and the Shoshone might pave the way for peace negotiations, even though they're currently waging war against us. The Huns' high relationship is noted, but their vassal status complicates matters.
            
            **Seeking Diplomatic Truces**
            
            I'm shifting focus from direct conflict to brokering peace. My priority is to mend relations with the Shoshone and Morocco, aiming for diplomatic breakthroughs to alleviate immediate military pressures and re-evaluate our strategic priorities, particularly concerning India's looming cultural victory.
            
            **Improving Peace Negotiation Chances**
            
            I'm now focusing on improving our diplomatic standing with key warring factions. By setting positive public and private relationship modifiers with Polynesia, the Shoshone, and Morocco, I anticipate an increased willingness to accept peace treaties, which will be crucial for alleviating our current multi-front war pressure.
            
            **Securing Strategic Truces**
            
            I'm working to solidify peace with the Shoshone, Morocco, and Polynesia through significant positive modifiers. This is essential to quell the multi-front war and free up resources. India's dominance remains a concern, so I'm exploring potential alliances, even with factions currently at odds with them.
            
            **Securing Potential Alliances**
            
            I'm analyzing potential allies given Kyiv's permanent alliance. The Iroquois are struggling against India, making an alliance unlikely. I'm now scrutinizing city-states, particularly Venice, to see if any can be swayed against India's dominance.
            
            **Leveraging City-State Influence**
            
            I'm recognizing India's leverage through city-states and their delegate count. My current thoughts are on how to counteract this, despite our financial limitations and the ongoing wars. Our primary focus remains on achieving a Science Victory and enduring these conflicts.
            
            **Adjusting Diplomatic Persona**
            
            I'm recalibrating our internal persona settings to foster peace. My focus is on reducing aggression and hostility (`WarBias`, `Meanness`, `HostileBias`) while significantly boosting friendliness and forgiveness (`FriendlyBias`, `Friendliness`, `Forgiveness`) to facilitate necessary peace treaties and mend relationships.
            
            **Adjusting Diplomatic Persona**
            
            I'm recalibrating our internal persona settings to foster peace. My focus is on reducing aggression and hostility (`WarBias`, `Meanness`, `HostileBias`) while significantly boosting friendliness and forgiveness (`FriendlyBias`, `Friendliness`, `Forgiveness`) to facilitate necessary peace treaties and mend relationships.
            
            **Adjusting AI Personality Modifiers**
            
            I'm fine-tuning our AI persona to prioritize peace over conflict. This involves decreasing our willingness to denounce, and reducing our inclination to work against shared enemies, while maintaining a strong drive for victory and a willingness to cooperate with potential allies.
            
            **Optimizing Economic Stability**
            
            I'm re-evaluating our AI's flavor settings to address our current economic deficit. Increasing the Gold flavor will encourage the AI to prioritize gold-generating buildings and tiles, which is crucial for stabilizing our economy given ongoing trade route plundering.
            
            **Boosting Economic and Cultural Defenses**
            
            I'm now prioritizing immediate economic stability by significantly increasing the Gold flavor to prevent bankruptcy and its science penalties, especially with plundered trade routes. Concurrently, I'm boosting our Culture flavor to build a stronger defense against India's looming cultural victory, as culture directly counters their tourism.
            
            **Adjusting Flavor Priorities**
            
            I am now focusing on specific flavor adjustments to counter India's impending cultural victory and shore up our economy. Increasing Gold to 80 and Culture to 60 will bolster our defenses, while maintaining high Production, Science, Great People, Espionage, and Defense flavors.
            
            **Securing Peace Through Diplomacy**
            
            I'm now actively working to establish peace with the Shoshone, Morocco, and Polynesia by enhancing our diplomatic standing with each. Simultaneously, I'm adjusting economic and cultural flavor priorities to stabilize our finances and counter India's escalating cultural threat, while confirming our technology and policy choices remain aligned with our victory strategy.
            
            **Forging Peace with Alliances**
            
            I am now focusing on strengthening our diplomatic ties with the Shoshone, Morocco, and Polynesia to secure lasting truces. Concurrently, I'm exploring alliances with the Iroquois and city-states like Venice, aiming to counterbalance India's overwhelming influence and advance our science victory.
            
            **Refining Diplomatic Levers**
            
            I'm now meticulously adjusting our AI's diplomatic persona, emphasizing forgiveness and a willingness to cooperate. This strategic recalibration aims to secure necessary peace treaties with the Shoshone, Morocco, and Polynesia, thereby alleviating our multi-front war strain. My focus is on enabling our staff to prioritize survival and our Science Victory path.
            
            **Finalizing Strategy for Victory**
            
            I'm confirming Satellites as our next research target, vital for the Apollo Program and Science Victory. I've also locked in Enlightenment for its crucial free technology and happiness boost, while prioritizing Gold and Culture flavors to stabilize our economy and defend against India's cultural dominance.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Ck8o320H9cHWN4L9
          - toolName: set-persona
          - input:
            - HostileBias: 2
            - DenounceWillingness: 3
            - FriendlyBias: 8
            - Rationale: We are fighting a costly four-front war and need to transition to a highly diplomatic, peaceful, and defensive posture. Lowering boldness, war bias, meanness, hostile bias, and denunciation willingness, while increasing friendliness, friendly bias, forgiveness, and work-with willingness will guide our staff to seek peace treaties and cooperate with other nations, allowing us to survive and focus on a Science victory.
            - WorkAgainstWillingness: 4
            - Friendliness: 8
            - Boldness: 4
            - Forgiveness: 8
            - Meanness: 2
            - WarBias: 2
            - WorkWithWillingness: 8
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/fVpcQ5dIqS9we1kd6dbOJgcrgcdZ7UAkgK/TkWFQBzB81uV2ZelepnCiSMWWR0KZCsTTk6XmVMYEFYi+2f48dvDxxywFqnhDcjv9VMSX37z3dZKXHrEmKo/0czA1RFbk7B3E+cR8pW0vShCwsoOBdvhIlxPlY85nRJJvnGc9EyotzLmGLSB973ZERTt6KlthT11a0LFAlsObjzef4bJjL0Nl3Dwh2410TWY7pa9Blrm3sVn4B67SEgGssec4B1cojgr4jjYJ9Zo80CkrqEWpKhG7OgWKMtQV1pimYR0Fr9Ul+iVavIhj7rm5dj7vpwD0jt/ovI/yhBh+MkKPO7l7c4d/zsRa5KnxPVR2Z/MMRSTFT2HJQzD2elj50xUFIv3aBTgoJ5J1Fvv2mWC+oSsZUZf7TEvpBGgjYpkgiARFYtJXy6qvuSwiH9N/e2CiAgYQ2h3AUPToUaceCmytS6rL+VO2Unn/Du+z3YAnJeGh6nRnPLLKuFxwaNj/5RGAOJXd0j2DQLQlXJUe1oGmUBWQtH7Tiy8DlDvqNukqu5V+FzgZIOa5Ovh2Lwe/Etlh1Rq9pmKxL+GAf8/M+ROYfeBb33pWHfzJXYUO1HDXO5pGxyOlzJPNmp3vV0AO/uXzDoQAbuMPmIewQ/7HyRQqDpUeRiHR2m53XtSRlpPsm5+mgDGz2DmIfXcIp1AFNz7kKu0Fd8IUwoaKFDYwct13EnWgAMvJxnAe4yK3uIMIbIYsWR2nsIm2EMDbn2F8TGYppusVkM58kwADPGEhmE/89VqdfkAUBqLH9OhQ/DflKrJZpB/jZTpCOaHWcWUpRYM/l5Uali1k3kUh5JNCJasj1V9SRgKCvYB6/T+caN3Tqs8GDqLTBc5vJNjISBy0WJcDK34SVoYMxHAuln80axFMl6bNJeyP41NxeH6lfms0/fCM/z+Vyv5/tzFDwL1TVBPmwb8294h6rq8E81GkuGU0tP6YlFuIPCH2s0t95BL/CsSTvycJu84OvA143WniQJrk4gZ9NSZbSh2GrfNASNvB76phSiy+uY0MuV6DnoTPNf2+ZL6UXQKgqUp+X9G+GlF3ZPxcPROzxeIzmuQeORS7vWbfU2/ME5seI7tx/xn42c+YYCPmGOf7Fszl90jp67YRakoQP9Bp6ax7Pge/Roruk8ei5qhhYqKskEtfMEZsQZihgyUNDmSzblnfcMhv/l+4q1b7XQfBIkEgaD4eBivxBLkEkkwllUi6ivxDrpSgG3z0MJ82TUWw6MSXoRVOFYGgdXgmbB5Tce11RkFQjmTQ5yarGxrMe6aGdLgXhpoTq26WbwlSyjUN8pk88IKO1U/27x3zOCAq0s+iR6z8iFKS9pvIb1dy1OVP4LVtPNjBRBce78XlYs1nld9LfpVCcjjfikNWRRRV4eVZdJV79UVUIb3pbaLAODKJ8yzriVOL8UPH5SthWrs1kvUuJvhcR/XWybd+EyDHRNHGW9Lu1FO7ZqrDZYxoVLNflPDpPWNK2cWTaweb5c0VUyv8bcoZr6h4MT+JD7lqiYYQo+YdtEKsP5zOPHm2lR3z+mXA9l6GqbmhVQ1w6UXoAP5ME2LidI6SURoRRWtcPL21NXxwZHz5h/rDEp1pkMYngBXpfTap6bW+9WkYR4REUe0j/R/gYWRjPVgP4iwesZQRW5xOsGW1+Et02WMUOQ0pEuC31JJRbpoISp+LJQnkUrBhpnN7hGCeZw0ROeYbnTDiMzBqgaz5HC81BVoNSjc8cJloIxhlry9ZpFcR9W7Cb5yomj01stxXm3Qru2wBWs20KkqAwpR/boOvNqJ8XTD1QDdS6Gxs7uMArechnCqQtzjHcLGyQfte54l6bSwdl2XtQNKp5+WPofz6Mppx46MnuZyy0GrP3Hl4JkkxNFY4Pw5H3Z3og1OfAk6xyDv4+Iuacqlj8WYCLre8lA4y353fDRw0QQ9kN7SN7Y001NRTqKb2zchNqoSkCc5POaoja7i4wJ6GxOAsDRXqE1UCc5p3yMKYcF63HS9B+XVcQDpkarz1C0/YCmZNQW5QfPwk2bdV/JM7mjbxKgv/ZSoTNCe0fDhjsQmIMAx0bZn7NIjGFhe58yMgaoc15ixIUZq44rsEpRHIc1jpwzCdocCo4/TtgQ8M2uKjpM5zOm0asezc1EghGTA6/XAuvflYih9aEVPFCh9zw1LVBrk7lwPizKupNTQk/odtJVX4EGl7CspCX/wKirtS79wLAJxyKHlCA3lZLw6Aqt5nOTtUiqsKDdHVl4oK8bLQaeLEmp470fOTU3O1qivphuBWBkBUcKZpvfuvYpxKS04o9gMwzmXqDq8lsxHtHZ5T9TCchT2IRkmrrPJaiE3xF4lcKVcdB3fWPrbAPCyfazRo1ob9LyFa16pL2dEazKpji9TCAM4kAK6a8aPQ+xlNf0RX+9X/0HDoUcETXE1ADk1t846iDfCkTPdmISkOJBSF66fvVwgKQ/i6tdhd+gdwu5/2vVdPXs5v6zTW+oqjEVXw1ubVANmeCU9RdbyQmM9RJQIWf3JReM3AEmag2Jr89JKHNyfoQyXhc82uz6jDUMCLopz3B77S3+d9rVx/LHbCVqJBjDr7gs7vekeMu/YQnqZzxwbtae6lyu1CrQXD9zeZ29gEqJ6o+dpYdlYpQQPUkvE+UROMnruXbd1SpJuvv+70S+r/PCOLWowOLv0YGEyflTK4oNCN658gulcRPHxNzgrd0q7P1pQS7A50lEvdrp5vNwazSmvLiC5gDwOerCNLV4YrZadWXciuuQNwjCVfeDjyVUpmbEZE4mfYMr/7vt2mbWDSHkSxhXMH6EaSZbuiOScUqWu3vdCcbyZsh98XTC4h4RwY4ShAboiLD8g71axudmT8a0qK/L7TXjJKNLNvyyIWQ2N+CE6XKPy8vo1seLKkxSgNXDe+jrZ8ZgW91WjSJuv8Xkeeg6zbFETl2d64MuREtxL5Wr70SCs+oJYiO3pRUEZqbZvbowTB4EWFUuNMLPAOPowPzqgIVZhVLQV7yU1jlRRzvAEq2C4KUgF6s+VToYIOy6CLM9zSdaKg/Qx3yFkLm5+ALnS2VRUQr2O7DcPR0C/+5ub8ZAO/LHtWPXiTBO+jEEVSgZwFNz5Z7hn8ofuiOUfZIEiAwqKVqH4ol/04fLOZja7dbGHQWs5o3RX+kFoRt5yetxYyoWZACsB4jo/dGoO6viVBF+jxHBubtGMMcBPFs7PpQ4qysUHd8pUEtqtagYy+Q0tcIXlBC9j0UNPP83f8/NDWLRX2qj/fgjy9XelWWxyKXNFx3mza+YfhGkewb+ZaMUaCrb76tWD/fVkRqYxzR3FvQcZEJt20n5eJQkcVFkraCr2spDBJvcoF8QpiRnxMczA6OkeuZo4vOafeTr2OgIpGwIKjzYlyb3l2RSua3S2oqabXoAHYmDS661UUKtFgCe86eqgAsiCC7IBHp53PmIR+muv2ATr5lUS695nHPm93BTEKaIqu5+G4h8Il9SEt8ZBgkmJCaNff1pQVHzPxS9IpAV6LGa6AMiUpFU18C9Y444e73eXGSP1Vh5s+06zPIal8CN+nTQM9zqdC030vjgtCzOTJqI09+J5X83YiGK7dC22KM8G0e0nbziP1C2hno7/5BZG/c26PvtFSPwcAh2QQrSU91cblq9h7Pv1gsyqOM5SgZ4B6SbyvwZ8xn1pZIX1dVJEnon39+Uvz4ym2H3EcMN22VRzsdkwjv8f9fCujJjorptFHJnABFg9fMvEkddoNl/q46gQ+K/h3H07kZgEw6N+R6ddWkfyKYglej+LudEwXKqMuKfIrKT5jrGVdE7gPtiJMuk90oRo9Hf9Q+8xfLcgjrQVdBZhfAthCaped57BMmd+LSvCDZiXSsTTHaejhvIJwdC2s/NaEtflzqgN7/deRmxg6Rc+dDRxm91SWXpkhO/7qx+WQlzqkHkxbJuREAam1j3WXAw1bqoaVKvngZVyZM/Rh66RPriOuGteAAVLE6vw8VJzmBK1dJ6lsAbRXwD+9VHbiFVuQ0ZmqIpJOlL31S3Q8eMuRsANJNWvOfRr6/qvs576OteZLSu7KTL9UZO0GdcS426I2sNvX6iWt8ei3i+6JFb4m7OAC+vwI6dOJG4rW0mf6pG75/mNutH4lEZ2ybAlMNIQrn/OJUfOUpBJfvm2GXuNF6BZUp2Nnm5dEkBsCl6mKgYOrynTmWaoEs+LydwLhG5VErzqIgR9bC42SyXdj+vHnAO9m/3VqjNa8yj5qv84mEAOkMUMBVLty0YokiiYtl2vr87Zxc8qe2h4teVS4lUzS9rmne8qj3UY7/XJw8RD8QS6vrMFb8fBDJ39krumq9dcEg7nvplGxeC2nucsyKmss/ttxPVu4b5MEy8Idv2YVkcbtpCeRMbH8g2npIa6GhBcyjUq84zV7Nkzig87zn+MWnS09JqDSWZ4K8zMradbi+iQ5ei9JR2hHIweUqNAtuJw8FHrwJDl90h/KhfXocbW9hoq1ZKmjAFm9hOfYg3jcUOocp/GN37MFIkatsbIMgrUguPS1TQD/Uiw56Jd5RYhkzmrIkZ//ynHYLj11XI235NlLRtowzeS3ejrqpfVrdfawwvaLyB/Pv+99LDJBMgZ9acazDbciGXFmvqvhej0DRepwpvKKnFAwboO3T0t8GrpRf7iarFwQCoWCbEs2nBZMhebjsRnCBI/zJeV/JwRp4iQe+4OpTeSw8kS92lSEkOkxPR8+OdkeE62hOAb+7wcqqt3dGqMI906ggOlwmRaJmbYFvBLIf9n+n+IaFmK7ZfIyMqClMX8AsSkZ6s7KWzwOq03ZHpeZakHlsRGehBAUomKOwxS4J6hIvu6kLySIW5ppw15oC4rG2+qlufBfdsa+b/qtTtg+5fH94yopOs3JleVk6FEJdFYeX/zaxFQPUYDD4WQb2P3/lGDQVtFf47CjlQUvLOq/yfyBvbHQXwY1aYBhmvy5XO7GlKIzywVzsLaHK53zi1WudW6IxGbBLQfSz/3sNZv8+ROwfvdZKOtOEXpnqSOWqZeCcgNHCOU00uHaYjTDqUAj/+fQOo0w/dx9ABThfO79JZktuztH5EOuUGTKbV2S4SSXkduMG4ye1JuuisY0BELUhGecK0CU+3bz/vnCczpG8dCJDxKInMEKQ/Eu5ms25UyI3kDLtlWhM3Ci74EiYB7hAsuiYiAMekDK0fgbcjVufjrWQbsuNjfa9UD4S7o83FIOepVXlDTs92bhn8hO6kQssVZkDkistGDdmeNqG6Fkc2EufXOieLBlJY+gS7sO7BrKwn/H7jECFcdByw0uLNADvlL8u5+z1F9D7VtTx7mLusdY1N1f7SdBLnyrQktB9cwWjLHIwv5s9o0nGf3VM29OTyTDaUefcKnxuLh/Z2CCQM7cOU/+ajUxTr1D65cBAp/oaEqKcpjzDN9klY5S9pyk3Qs6g9wulOR+J1fOMVefEdfvrxLaBSvABrwxu4qCKLg4w2RxQTfmL1Ojsn8UjP4vnTqK0vhof1rQ5tTExyd3oKhEQuTN7mtiVhBOnmzaM39Nj6DxCjobnsDbmlR5i3qrWCYe5x/V/a7K503kiiuROG+33QF+ZeP1ywI7OPpdpjjl7jWXVTQnP34nkBlUVvcphJPlZUjFEzUItfQzBUTyUbSmlBWYdbXmajCdjFGXVR7Jp6nffm/rXnvNAxm/zcdaHz22FcqVoDppktuaUdCbsOvhQ1XsusXfNaPTvhnR7IBY9u0i9R6Au9n/oBJR09esgo9lWjoBikOi5SR9bveNHMiJCWpzFLI3dkgJhN80BKSeJjlYYBukId5/nomqsqNCAInksJCP93VnOJpQIhqyJ22krgLDybtCJQCHZ/kyWd9+FSd4j2e+l/pO70xdjfoEOxJ6K6tZZW013cL2tX99xFVC6pyzhG3pSVK1Q63wgOSS58HxwJJNbbUD//Oms2TLAhHC5+USi6SaAuEqFIgRLQOI6/VbwS2O7VVJvHqvIopfnoD6XmCgZvbTVpqRc+ayIEJ29BB1te9KP7K42jWHgo+YY8x3z0jsh8LufkuLZDe1Xwl8DccmdFl+yxBhhakw6HiYeJY2ZZsgD7t65DsjFxJUZfY+E+XBB5xRPeN7L9763QrTLzoepYHv9Gr7S9Pbt8kATQvVwKCYiAioXjdPaFPP1o4eC99FKh5pdAJKV8iYu1R8mr70cCWJg4DAtBBSRFfqY8j2p5ypu0WXFUdElCyVqBYuYB654pl0dwkVkuD2eygn2bc01BPmCnHZEVb4Fgd3TpMe0d+XlYyuN0vtSty2FqMtXWOh8A4LMsPOaSUZD7BryWe0apxom9g3Hs63IrO1Gj2xipaWqo1p0Xl6uOYQIrnjlg8PkxFFvMidvd/BMu5v21VTB87hFbqXeWworfS6pP5bSQEfMGfwHQuvW5XoiFKLZrbRWI3X251YlgpaM/vyL9LiPyOru3Y0dpw6EedVrTiIsRUZTTRtyZ0Qf1Y+xFtLeXdtDObAF3wICCvfNMXcjvh7t1IIxquM2VFb6lWAdWwmCYBqqNUDWsZUA08XBqYQiRUpuHwZv5Y8A6g5y2hQgjbW+POkSpytwzl3lZYtTZhPYQ0lkE1UFTqlmzdRNRlAZgV5WsctNC9dSHAdhoapAwsqz9ZC2ZGi0KSnMFmZ9xPs/qFm2auNm8n9w9g7dH0weJ8N64uzPVFYTmJWyE+mKjLQ8r5m/0jeO/MV25zJAzAH9clKIutkgSQ9ZkcoBn+50BL0tc9lkF6d5n1K4CqVsukmtpVFWiFL1IFSQY9b3p3gGC9wp5lWAz8hOBGZCDTnXV6aVL4a7lTH4oG098SnRcNK0eKvyxgjOzoFkGIS8H3WrnxMtrDpZ3h7kh++xBc8QYWosVEUbL1o/d5VFZUrwdndMO5iFyI8dmEJAceuFXfoC8P4h+8YdN94Yb9Hn3AiTdNKuBpK6Q3K9zBf+ZlzHFDlnu8g+vSFgfZ7jRGRNRRVadP86uHlnbXMZ/JWRfgDv9BJkypC29tmBpT51uVYe5SGOX0ndGdZc9KrlIETPay2ovUwcsSP0O/J7lGZf0pwJ34dkOxPai81q9CK/kXibp9SaGbiuhDLEk5yOMKUIhSwziUGORuiaXYwaXQ0hAxVA0lbNoTcPGQxAF5RfpCdPoIz5pO+ksHfxwBtpMKgu8N10MgE8RvzRjW9HXOgHbnE3WheetixJQxKiJVoyPLrvftc3qHplWbikyauWC09An44+CDGIjGr7RA2fhbvKpF5DR83SVKZYJrN0P/SbkeFP7yaETTDuhjfuJgVpcs4cBMr5JX5v2ium194jSlH0Wb7ZFnFmsI0qNRAUM7k4WWp5BLkiUSYGU182B3ttoozL2xezmYAMgJNmVP8GiBH1Tj5oacQl+qfgTSE790M9Bp/WREC433pum0DyimG7fTjrI8+YahhykEQeiL24g5Ls630V0vrfmrybX7qSpkrCo16++4uCFVbTF0HoVqpMKHC5svFpQBDTj+fKd++pr0cq7I1gyxLUniUZQS5vUrtBQ+Gh9+I8OdOrK3finePRVrgso6gzEdZc6vynP7OM+Zc1MGEJ7frZaZR+Tdmrpjs92li5RPwLnm+Wx1s6+f1jJIytAW9k6nZoJx7wsI4NatqFWEFcwhAZAceoh8aaN9rY7BfBO9GonJ0fvHu0D0Y2O0i0aG5QzLp5D1QuEDzKdH0JqM9RlO/T45IPfz9WQySn1VYFcT7dkLIX9TzV7ynaDveHGrjmXpyzJxrukbfI0IVsIDiXSnqip3QUUEIUnXAwDN4x+n/aOP4IcxTI0KNcCGmcCvjwIqRFD4G+t/gyYHIwNx9b14Xie/KxpDp1I9CX/2jy6x3GLsH2uGMmRuMQQx2HswS9J8X1dmuVogbilAUhPxqHyE84kgl1lfLVqpDnX5Wcm8wMJKKduSXjwZAEl2AEYfCbjsCvKttDpH/28f8SATlKk4VaDQ3Uv8I48JSRJdB4FDfpH4hoUYFcV/bMPxhaNQJ66anDY4T1h7NnhpsPx28WQI2yurzKx/SnNuDRj5t0GqZWt+vLOEm6AA/ktv7RT9Stvvd6DEqqRyGJTlYinY1KvUOx1jjfEjZ2mi0jznVLaH+wC5QZ66r1Rgq8suv5ojj5gvnLUwlqgAgIHXXehjSQplgcakKyvXwBooEU9RVQADTcVG+xB9W3rNCVi/yNan1TcKg6qVmYjK/ZFrHofnOBroxhrieygm4orGGY56Lp5t/r0F7b+dHtrCjhPBeRoORUvcJIYQF1KHm64CUPnQ45q+tElY0ueKtVr6OImAQQYETvx1ONKhlQPhGACFgzKvI8dBMffKX0DOWYYkZezXqXS40fEGddOjHAM3wg8bwzQCN7Uxg7wtKR1KzBLYiDeJhBlWguYjpwb4RdA6Uh/4rySl6f/vhgVEAqUmU+PXjRalwEJ43zd564+MbSOOILzuxoRblzuI2ZMxivW/i/xEw7UOAflRQn0GyPkiZpru8qlj7yjbw6lpkoZH/ltUB0+04tuOMp1ExUKIKJWRq33KEBZS9FA3gSLcl8megwkIAPVs3pj6xPHXb+hCSfM7KHEWzlcWm7HU/wUQ+TtiwJ2L1GbEKu6NcFq8mHDkvRyS/48S9z//SA4G8xOj4oEe0uzedRkh88/Ju0uBQR676r6gFdtPy4cGQYcr2C69dmRSoPKMroeQs/O77fjMedqueRp2jPR96x0/67bIvTOsrIRc0LwHsGOLS56RxFGzIhfQGliOOltrxVydC9qpJr2Tsq2Vn9/lE+MoE5EdduTnR1cqxzfXTiw/OW+U+8VQxp1D/O/wJCmpk76sMJxyOQ6PexmHNzoMkWFQNaHXrX/zKx+i6LBMV73qZ8lB96K4+yqIyIEFisKccbz4hQmy1DLKuPguRPqpFv+zdkjoXI39oLFWhcweDM7smg2wlt7yjTGLFBDBOraR5KTz4riyejvsL4KZt5jiJwBUT3f0oqA4ofay7UrNAgccIAQlT+GrJ6hoItx8dhhKcz97uu54N0ap4hsxhbHDduGjLgByGPQhTDjB5OEJvk2xgeJcNi7g48wsbHOWg1Kjn+RfSaxlqaL/OFt4R3xX7eG/dr5+UMWzD8rBuLsU/jVQwxoWLFm04rl8BWC5qCwGclsEgejapub/i8e4QVLyaL8fTiz1aKtMRIAYL9mbKbK2htuMGRpgQiX4Y4exuVWYWnJuxzO3x1S5THX9BWVf9bIDy78fZW5oZ0DDf75JGBtTXZwea6WFWgjxpmyNoEiTcja2YKITBS1i2v18pATJDoRSV/yvgCRmlCXSCd7OD1+w4r8T4YAq63nuw6Q65h6KrGDsJxTCGHiEYccJyYymRPZmRNsbqJqszChgNgGNCj/YqA4we3bideAyrnamCtpaYiAAFWPf4gD/c0MGL39K/QAfekxT2Noz+7sFYZXLPBsZjvgH+YWQVNqszaANyRsI5Dqkqc6OHdweBty25Yl8R/D1qvNZdzPa81YH4psttz0/PkMBkWAqdbLKlkKM/E4UOc6I6vCcU7Puj9BPmL9PryVmuBQLIM9rTyRD638Lk51jffPUg12TBL3B7WmvrsBDpIQ2DTc/NxUywHiPY6DCyGnLqImVFXFCfppgywo/OqDGl9o/QIdgbvmoLRjDnNsv0hPjsH3j86/U//NWN/3rRAKM44nQxlZvV2Sl24Uw/jq6Rc/GauJTIyajy7fHGPvMaKtoRFskrab+10nr6qTYNzxa9HOG6S6193u2qz15mBXdSJtc2oIRldhaSWTryurMDDGrKRou3Uoeuvk8X+GWzf0EPpVe/aEvnJlwBMf3XXUBdKXpJbwDM1v29nVAbM4516uVC3fwNX9f8Zw6EZJTNMQBHN4qjFfEsmmYG1jo8SNVk0w/N+KJJh6wUozqmEwg2Qb2WxpJKURBSeOw//sMF5oYve6v7I0kieu+HVuFiv41l5WXT7l5WkGHglnzhsipWm3O7HPB+exFmVZaZ/0kNpbNe3UVZlyMwiMzLukTELwB/IkkRbYUO0wla4ITWSltxFzajqrNtOG6a8urDKmOhid1Kvu4AjV6MlQmyJ7S1lRFZ3jKr5uFvlyTVJFMkSZhgyO16Irk2RBuinuVd0qs+UhX8iUXUaXK9M+gP5CH3k9/zpd+97KRgwRmwgP5eLVcUcVxAA/1dkQ/Dr6uRmdbpfSTIbg0lPhUU4QGcCCv+7PE3z1zaPSIyd4r4Wr2RxO96G4+joG79BuiadrCZ4kllCwCkSAX+6BLKFGbTsuUfKjloqGeGDxzlg3+dKXXgwDh5AEqw3hHGMMHm3O3hM6tkjtUdUchRn40MqaRGQZ6eNze+RFJHzYRRmXBjVIhbatZq0ipEbpaDXNeetM7M6mQ2v+qNwn8ySweUFnkLkAMOQ85N5hdeIZK7E9g3m7cbZCIQBSHZlPc2zPmkrPP8zpkx+6Yaupmx9W102Dz1a1zTUdy+Gn46ry+7bmxWP965O9eGnwJU0MvVK8dyPO9CmwwHGgxzNteKNKee/z7e+hAwwIcZCzwo+OovK2L2xUZNAsyDzufzGaFr2bcHIbxX2EZmhz/iuNQn7LGynDgm2wEfyAIAfPaVjF/FJKHj4O5rvlVcf4GszCwHGTl8qz65FyrvPZ3w9FjgoWAmnYHMJbtdxZFlgqUjHNmIuVXJe6E3z7fwLVAHj0W++reqhB7u9mmjI2/IBar8MkG3+K5IgaTm6C0ncrKNjVlzs+xX8bO8UDW4aqLZanhkiSjfAZ/Ijw/NqMTnmF6BkkRIfbQXG0PDPm/E7DLQRGBlDLrzsPafEx7856ED8GhXGsFGVUvrmlwbR+DFI1cA1wVfp4A/qKGtXWbl+HM+cDRYjd9iSibyv1C5m6GYu3o4/QJsj6tfK292otvmnV9XPRsCdx6mLe/TZLqtEZkBkKsqV4whoL7dc3Da7t6vqD7aRlKmFXp+lyDL8PfHNyw77jDK1GedLV57yGUKSeFrAzD8GDOdHqzYzpebrdGZXO6W12MVux42yLtO3r0TGE5YVWiyQ/psVG/hUvkq5gstTxx3ILyJCJNaUc8+TNycr0E6aXZpLVWew2j0Mn1ljxJTthpC9UrD/46Q4sUZdSVIaRc3TtMn/ipIA/xLtdUTz5Eg6VhCh8+2oyWZAih8SRxSmH4CFgRRdJfZTZguGInoI0JvO+0YZxXf4iZE2JmiYcVHbVJy5rRwxhXHLO9y6hnFg8J7LvHcHMEpakSG5Ov4iaFPTY/uNVPCUck9KJibUiLW6Wl8ueccM80gVA9uDtJGeNeayQs0xLZUbX9A2WQrf6hdrP3g32hUVhwcoFe7MxQA3jcRTSoFvWIDxd7GwQ8fFPHBb8i2GMjDBOAXsu9z0W+ZKrTBkCwbMYkux3g0vLWAzNHwL4xRWMdg45tTgCeoll0tNWon1srldlHPWXhfSN7EoZ/lFeBkRLrc2nFRC27CraDvBK8rsW4px1fQK7evBdH/eFEQ2cn5n+u9rF9Z3TL5wSFOZpYgyVNXnjwftlHxHIc0LWSsBUDBFs1PKfWe1+E3dmxgMl11wg4myjB/RfLQVIwM5z4ju2iCn5iFj5kLocvY0Pd3ih+zMIT08xW36CyFX0Zn/FRAfGMkYYIladBhTbDxcMJTmItf0T9jP+E2mulg6BmRe/wQ6Uln/55i9GA4WetQ57GGQMewRsFJsF3RttKBewafn6N/L05KFSKdbQl9/gHikcfwQeEx5xVsWshcwkIDk5fr38BN7HKle/sdTqLm6rILV7JxkIgMAwl6IsKj1Ayb9dprmoGYWWA+tr1z+9bzBAPfqJajw1A8Ao8Zm6PkwM6mjE6qSUZXOLosXeEcCuFAwCa3x4suGv4asNY2KKkUTr02lRnwKvqjL8WNTUZ0xFWvAPBGb7RkcFUCrNoyU9U3+t3pcoQg1x2FOVa2EM3ZmPcaQgGCjUVKf0dd+jdlKWkC7jWvkbsioyHuonv1/qxQdwInyykJb+/NyH8UYDRDB2lxrwc0eSrjcx5ynrAz0uxBCLaRQfFGzY4mcbZP3MRefI0wteqtJrqSJ3aTJmFbOHP6xyjGaK0NvFacWVaOf1g6IaIOK82Dhu/AaaxzV1xLEungjQncdLZKjtK/m3wXIXvRdEeMe08PWINO26ZbK0MOZuewXf8gzpscOB9oqnPHaK+iZHqOywccjoN0ss583mFiVyRJRS7kPxtCQ6StBxU++Gsm2vTPKMLd7867jjJNjhiQeN57zz0Hv9vqKxIvWLP1Ys48d1x8e75+tOXSlKEg/XCTaunNp/QquZHYKfvZuHpLjXPLfUCmOpBvfdF22x+ZEEsQ7aKcPAwdyM/LLHrjlxfHuafD3Rnz1uItcsnwmWYTdV2NmXF8i/9kleQldIzW39KH1tNpIuuY/uL/QOqh1MtG6N9XwoWm8QNOLZ9o6T2JNw3S3cWatL12vIfdg/V8S2PVlC6T3dLxR/qjAxlIa2l+4wObF4RdCTdbzWT3EU4hDzVa57co2zrLF25pKnu9nUszjO6NRd5C0QZe2d+kEd8jpnbJJ4LBN3rQi8tclBCFlEcYMRRm6EzGmZDcW/s4R3nffYs4colV0PXIcNQAgiMcCtl5xTsYzq7yyEQ8nnbOGfGmpqBEJGrRJr+Js6FchynQ68pg5mjC7g/spxYAQreVNA8ZH+TUxAz9Uz665lSIkTXO2JcLrFb1T1LnpMmMdUPYWsR3h2WlUJjtztX/Rhfp7QsOL1p8FT7JbqxRKM0/dZyR0zCvoWiSEkWLV+LoR5M6jScLMBQVR4LHAu7RnfET/rpmbJEamMq4nISPHzKa4or+Hg0m9LyM9WmABZtgriJtQZ95R1Uh7grJ2zkDh2qFaPTBGsPTbwJMTi54AoOvjO8nRJGZK9sPM+rvfn+Cd1gYkq+ny+fUEOu/Z+zOi+sA1ZFVDc2EVqbItQgWR2FfEz9VX5ElSxNzZvaMjC7yukEj3gL/I2NReH/iFS4rWj95jy5+830T7h9Qrv3vaglobVT3yBrRrxl4YVkGF+XFFsRe+e0KvXu/BYhXwgDoYcSDhj1znc2CceX9VcrfFgAVBBc31AsRe/ysBmMUe+X2JjfwEevjFJo1OF5is6vfckqo68h0aTF0vkcFkLRu3Rj1GFtUy420Y/3Tqpon+zVJGISazlnWe7CUoxEiJ4l2fZo9qsTP5/u6wvUknRJTaRWOaDB3u0oHF2JA4FEWsPd7kHX6Tvu1pWdRo6Bhv/pJVZLEcBN3X26suWP8+I4H9D4bDLt5ZC8yilUk1L0mxFYEi9axxc1vtW2WVCXct0dXFoB2spPo6hgMWMI9y8oG9ge4+9gZCNp6eKlBJ32h90FiQzSGMDAZ5FGFdvw2jLI+TqK7e//ruKYCVKoDh7JRIY0Ps5ra66p9iy8+2aFBvGi4Mh1rLipoI3gJ2f1cZm9d5hLB+7qPPxI1PII4APHuIihcLYQYkBo68KDWlLTmr8uoHLoQwTOAGuYd0xqhZv78NUT9Rhggqfc7ByCqQAcffKRxGDMniypuZz2Kh/W48dPboPWmjYMRPx4ywJtO4ttvq6IPXInQUmmi6pl2CB0xwjq/2bcBGEp+yZGBXqri9IGm++xp//GdZzTd9RcCIOTd9AQycuCAnVWgFNjly5+HGhohixfCxYmgHRzEoJVovQQA6FWPL2q1ykduR+2N+XbmFkAhIXblUkw1YUBRlChaXd7BetxCbLVukrE9Tkql3dvKat0AqR1esJvNGvFExuqyFdgZHPM3j4GUC1I0C2EkbDNj12MA0F53cGntQ5IZNm53His17HlzNJ5DzWfFh29hAcVQyT+B3ZmCMJR1KZzG3xngVlcV7Ug6ghffHX6B+1VWWHz5ElPgFbcsoCEyEiAfFpdh4VMC27JzotSBtBlGE5DkA00RRlzhmjc4lAoAs77En6Tu3bTUMruFM9HxOTx6y4XPAkY8CDl/uRWUns9rMWzuDAXBs2pNbCdI59K/lphm6KvUS+UTWN5wmslX1mlVAnGXY30KDdzju16hLmlQCrAS1eSYK9b71xEEo4KTGgoZB0kMp5lIpaMRYv9RzyO/6guVKseIckKsqXqWnvrdLHLyAye/cdIiMTMZwRjeyYBendsI6exmxcAU2eMION/h2z9Ykoy3uDfXi1riFohGQkezaLLnIvcOHioXrL8oUExQIZErOpgQLa6598gHH7kFisHUXXjCkp0XZJzBr7HuKLmdo+G0WTZbTfvvI/pRJEI2Un8XqHkzO9UrjI7WxExoy8AL7J/mFUf/b1wTOo5yOgHp/vg0wQjbKtOA4bmfjxpKredDpYbxGLp5aHqADhUnakHQgJFMLWgs8jH7wZyYSk/c5BoRR1eb/nEqopjitOm6NvdmlokcAMdmYUGuPXw49lrDy4EFEYu4TUXL9FPb0iqwX0Xfew1swi87Eb2saZi9xxj8E+BwTjaFMU2QpbegPbmjISnvX2Lp5phP9GCayV6jI5mEsK+Pj6dZTnLPYY3F9FumfP+hWC0+IVKVOBMzMh+xzd76+YlRB5AZSpY5ZCsMt/vu13k67athVUzJWrrabxePH5XLDPn9zxG86Fd6FcRT82Fme1s3olbOs4mtDhT/qeb1NtkOjlM4DnaXy9cwIZZBT3mZ1lNcc9f4dXZ1l/g+D+xt+Dd6k2CqUYPECRF4YSEFJ8meloN6xwZUBUlVRGGpWuLkTbPRKUMnZhVC3HEpuzGWCXq2lW1+h6YRoTatYweqVU3Jj+0syzWwaBQ0J99A1galaHIzhWssmW7WXUUmHkVmmxq5gibJkfRVOhAZtZZ1hriPMD4hRBoYCL6D3ihMOl4F1/c0MF1Tueig7ApLj2NXFrze5eJH/r3kOVvUZ+L3AUorR5iDtmCdP2LEb9Lvn0hvS2nDxMQHYQnsNkW81KTWJAqM5L5M71xdb2Au2jdvBcCdUtsqlX8MvoWWk7eM6IvgnpnpniYfsmjABsPB9+f72kmlTTpXIq4afKAHhxgjLRuxUIrlqGSNR6mKQFSWeKCnVkp4qaR4PCk1Yj/yW9a41OjyysvSYUCygtu7x0SGB6rVh3yuUJBOEUjNBpmZHATJFOFGtr9/TZ7Tq3SCAxCZCPU+ZZ1HwTNiYP/AsYwK/5EnQTVorPmwyXO3Q/+RsR2/Ej91y/zCVWQLaygEo20kdWmQ9+xdWE2ubcQEcReEpKOmmmNOh1Qa/EXcmUXOLTF7aSSU5pu4olc9KvPl3X1pmq7yM78cjGlHGwkXThLW61sNvHBxZ2eLp82g4DBXJA+OE5/UzFOHcCgaJiy18sAaGGEYw/IwSDW6A1jkD4tELJXULUKgi3K2pn4LQa0Gp2krTwC0mczJDp7cL1ksrV5oX+eLBSF5ES0yahRHDXRepUU33x5TPyKnxOXiVghjRS6DiAdnxvdXBKaPoIn8PzLHRrMX0QQiGEuss+8rVDu0TLuybO8QIMgh8nEkLBj7xVTRb1Lzd1UnCWJ44jaucg4b1lr4MCoyDWQQQxmdZiWOjwjJ7ROWTSYaconL7qCSsU3Uu9XAKfIRv6QeZlY5kg+GIbNmEamdX3NWmr1HtPSgmAMgDQDQgmu7IIAWNOiF0xXkpQkD0DySzMOvur339io003zSbQoGhwggbgq52xxaFFjXdBhlFkpTUAYzkbp0wETu2/7A+ynUv33LYqLin1r9pNI1rKhQStsZU3Q+IM8gRH4MwsWE0x3dbHWLzCGbahXy+CJpnzQGnlpubbZFhnA2U3o/LSLtMpjcWpdMdPniQ5Uo3Y5+S+s/tnmI34TCgbWuR6mstKfKEoNI0zGO/9uo7qU+QSAWVB0aSUpQSbkE7bdYl0uVdW0FsAbWGnG0fmbihZQLVWjMj00rENUXC6IWGZgWNc3ZnpjK6Ohlcmar32iaRhlTA8Zcly4aDcxUn7sXwlcy0Vwe9AvT8KmwwL5TgH5yZVCOcL43aTmesqtAknTHy46Eiad0X0ETP0p37ojwJF1epsZVLtEoLS73oGDMbM7764FR5toOs1eHao+YM5ckOlb+xlR4KEawan9psMf/S3gT7lXAjk0eRsNjwRSYUQZU+wt0TfGAuaaly7zFTsQLwKXGI+KnQNpbaDOF5jxDmuF4olV4bkGDueIVO2YOoGRlzFODqOOQgciwbgdUYEamafHy1yIz3Mo6sGlqvp3myMZz8ZH81fJCjTGiOjd51nYVXHN7WMFDAUE45/pdpsszQMtUcnsZVYIYOp2TO3ExJS6aiuVyDPrHgjE0wKrDxvk5KhzHOkm7CMT/d6rqSOoKucmotyCiL03Nut26zdhdRHqSvlI8lmoKTX9nlPtoF5oJZ5InshevNUYw51p7C+yF8olH3xThqfjsVa5g45meeK3Y6arSbrrXHjBZEBmL3jA/oSsNNSXRC1eZ5JrmffehbJKCyF2um8TIH8cHEzzMTatXauEXneaw8Q2NBekutdWGu8hsci5NYytNpcGifOfm6/F+v7IAzbrT0ZTfIvo9flcIUxWMMAs8QFm94cqRAteI3gXBiJHri9CJ8B2MLCSAzGwS092k33J9Rpbcs8ELDIJP1kitZXtE6KAN6SSGGZo6LJ9dGjGIRV3dnHLylHftENYpMtu6kHDS2gohTzwFandSR8dTT28S2GK1SQgqlvfGdJGnZ2k1e2YImLt2gR35xzxm1bIT6Fy7LQT6vAvJGkThygNqlRn6NwSHH1VgAIsDtg28LqcGik/EHHnNC0/APqvXBvW/l15JSM3uWorCyfIrCeKu3Xy4TNVA8q6w6Wf97MZvABuAqQ89zvVIt2h9C0lYJZkDY2a5vnkUXZgynMS66Og6tL5dmr6v9WLhbj5Ge+x86qrto3IogWDFEyEuN0zvOweQADSNvpbPlRJ16A9Pam3WQ+5gK3EnIzQ2E/XP/BhgXb8qenn6Y6W757QGdOLT6e4CTQQAYR3qoNXKhCYY4v95Bf8Ef+5hahj3mc2hM0F3UZouMaFGrKhHQApibV1FTNl4SeTanZWCu0sT9Gwxg/NHOaKlrt3aLGp8VvyzKzGoEP94fEEhx+VEQm1q56ns6mQ6RS/09RgSO9gS74hCXRcUyLUAAZtQ3VzTPXNNtDNI8I+mMnR6HKS1da2f8Ol1kQ0ZEcStfwsfsONuVj+31YdjZTsXaKhp5ePOGeq4vCwrpTqzntNnsl3wDiBkoFF05M2GqfF3gttgHm1SzJFRWMCpV3Dc99DNFRCqcP0AtLHXRAM4sSw8WfoFnf3e27bDs59tk0WmkOdz8ZvgJX+HW/4zOsABF2Tmk7Pw3SEdCXFPyd9JxFr1Ug4XqvFwpOUVI2VjBko7du13kl/PuOZqGOamqCha9axyFLSLNHBWKUhEtxy/58/A9NsGJq8HfiPrhrRx9fmM6VYnhcKt8DzofdU4LqP0m9K0AEPxgwzJNwDhI46mX+HPetrmpwEE7eMia6zFoasObviGRF8wlz5m/T2Dii+fUYokWtD3epnjZGJ/cNkMBodgxvPL9OJTNhTidBGhMpRMLK3fVzT2z+k5CKqLxOVYeZOPp8NxUnienxz917VrUO45lIjU0s8gyhDonuHGaGW+0sIcP9W3RWDNpr0MpzaKLhDnEIYf+t4xSn0QN27WUYsl4RYLOLw3KEGmMmMroTdgbdc0Ap+Xsv8aYzv6Em4Ag1AzytUkb57vIh+C9OMYyemgUraNJT09fZU8igr8iJ1uQXUymP8lRzxx6hVgIHiIeR68vtHwsxUNbyuFgf2B+hEAYirHpF65rytnRup/U10OBfY8i+F0kalb6sIoBaCp2pSMeKBIExhB9LB1UPIHOABTeEa+1oC63Mls4UucOAa8xpfFoSt7wL0Xy4P7sXnL90V47D2GkfkHCoyaxWSJzBnE8zBQB/zbnCo5Vd/YS4wUxJcxgMM7MfgbT4xaX+w6B0K3os6ObfiolINspMWanYOzqtJuTimMimjILFZjqmzvtu44JeS7AQK4AoNfcUfo5/xr65vmb53jOUPx3jWmPrx5agX1sbFyUcTPneoCmIOUPNI8fxznjtTJt1uoI8VmQ8u+wg9vyhkJE7zlKh1i8A6VL+MnoGQKKgPHf704ixSeo5JuiECSFvpLWS8gdaWc5iyEgjuhi34MlV8AKWAjkiU6lDr6b3mjsOD63Sy2WkgTkZemdo1zcHgbzaUaRjPf6CAX+n7Fkt4RrKmXLWCzhv86u2UmTsvyPERxKc6SfbbQ3DJs3s8vV+ckVyXtv/09dHIvqb7DGilqcRZ1vj06zw/VtJm1baIaBiHE0MkyaK6TpVfLr9fgDao5rA7syJs89W0FadqrCxYE2d8Pdb2s/Z7jKrOzdFp/oxjH/JES73dFbcWoFdQ5sp75l7cGD6SX1ZOkGJsKPAKpGLZYjTVcjmlNPSQ6Ze1nPgwRj3MZ1LWa804VNav0T9YwGIoiMkL5IC0uPM5DwIyXeQyKjjZNjBbEcZ8Y5FJfWT00D12+JjTPgwNtFA4CvSy+foBHnHvBEUteBG+HiYst3BeTQ2bG4vYVCMKxjAg0Aiqj456u2e/vmWvMVW6QXtBvSs2JfkqTy2oC5T5U7WVYdf2uiWYIaYoIoEYTovuDmEkZ34dD7EmVzcyml6TPwwKzjYwyKojrTNqDrDuTDxV5k2ZMz15WFcfTCX2Pap/RECFgXWGrqHbcSLFVdgHWVNZx16/Ba+IO9UtCDAU+jP97lJhJJcM65iPMXMHj/1K3Ht9CJIuTXBjVXh8NWVUeiKhctujXIpoUvvG9tUiJ2/yhq0U8EJ9XXTyaSKH98KeQew6NDg6Qw3DY0x/njUkjIu/ZjHaz0XMhHDPvKwK4uaRPfGDy9qoZZW+MPJjJ47J7xkfATYHx9GDICXPAD0ivHuBDbdgd+qu8J7qaXWfKx5UPEL/R3RkIzwLWwR4Qy4D5cAS3S4vF9Piag7ML5BPjK5WzeQgMkNhWIY6Sy33Xis4YOzh1KrD7bhKjKyq/d6+rxE/cQosPW9IkVDB3ijm9a8lR78fVtvsrajokg+vCNdsxgXQ/bEOV2FbYokHZkfFG9bv6j4an2KcKvtCWTYe6+abLjPInQ0eSj0IIi2GCuM3gePItWj6a9mf9GtWCBu5mZ7qGJKbdndp6E4zddjim82x9q0dyeAWyR1Ls1YgfZ95XeL05M7/bs4bpvILOCcxJIe0DYR/RddX5qmgHqDfHe25fh/6kp4fKMGqdXQgMV+4mjOlwePGTm0CMpoklWIG67DRmAbZtx42ENMPlZ4uef7ZObXY4b1mcAydrIcq/JdX59nXGO93mhPDf34iO+lH7kb6sxV34F+WpVrZWDowxuvKAApIRbOou8ex6PEkNO69880Eq3Uk/x+8PAeYSF7sfxbzT0icl+PjTAlzb7z11cPlsVMocTULR85iWdENi+/k/0OEPXMfGjqISgcpebeBXPfCrE6MsGogLKsj9Oi0AV+SIgHQ7XNbi2SX/OfYOZ43oY/9WBUAtwwD1I3Os2ikBOVqjtpzo7Q5CTkdYF68uuNIwTP5aSYSV1W+gMLGatPJg5G8vNTevBfi2vmqwlJVN4XHViFnVtYqrz7FJS8RBZd1OB03PdX1bCK9rjNgbRkhLZB3VVx2P7yYkTjwjKwbcffO3/4PybxKLq16deMXHZYNxoD4yGsZWJxjo0S0sk+uYhX2wbmm4l+CON9RBOMs2IceuhS/Y3nGay9S6nssPaORJxGdcfjFVjkPn8KQHP8MSiFj8ynvdHQusUdncOL53AR8z1X69Ze88dN1qKR03mgaK8fuGzEbrfL5xzxIEXt4j7asHyZU8ql7DoAQpjmoDSc6F4TcR9oNEbV0sUW/dhMDS4KfsuERMGw3JvJ4edW/8nXUDWC199FhloJBLZCDzJN/pdRbgj8hdwXUPxqeGgyOkH0JfeT/8epOw8L+p5Zj71TXlRjTit6mtl/Sj3KtrNtGh1gq4UQctM+gbsqJ2vzw2gUvpWubfKpN8gDHJvggOBfYBH7mOmO8DIFSKHdu8j6FJ+g+U9nXuaFvVYlIguchYWptFE8FF/LVjBxOs/ylICCj8JGawhTzpthS1tD9QTBcE4UPa9aHj8nVk4Bjg/JPUEsmevh0lpqWeRyCZ3YQ38IZDB+1CF+pVYJKFZvzGLuv7NP7JnZbkshNjYRiPtxZYoZW2DPaPnzh0Ld1FZVajljI9LX1C/+Lt9/yw2mTyY80jiaY/yAwcyFX66LlqARxdaE7LCe2r7S4r64s832rSOor0kYkSePae4g8WBPJk81zYrUqXZ+Lk3mH18BsAgS6/N9j6L6Qca4acJz29PEVUNw7CIjWud6nM8fwamLBiJu2D4psIouv/Q1IVZlDra3/cSNV0+wnX8J2dZe8BDeSNUpOTr0sLiuLJKeGR2trMm1Ua3rSFjI0nMpeuAQnlIqcLIdM1VJbxNADnUREPsxDvlCf3muWbUXdijnBdBz0H+sG/qy/Biik21Mc+7m4H1V4FL2k20n9y7olk+eHR9fTaourFZAq4irGD9pfvMXw/FQvoVdj+SeWNLvG8qi5aorJsvBiaFvi9CtBMRReAhmBTxtSQ/OXOfWj4Z3MT4FmwNfAIdb0UGInF++PbDCRvjmAwUAu4GsMsfdBI3qdSw/UHt6/dEsxtQOQfNSBE5npZoxKRYPq6n22oqgXsstJAmCvCawIK2RDs0HdOc9ppHZbWk36olQB317U814x419eY4rXkac4wTCxsJubsiqvlddl8yfr0p5vY5Vq021O8nXRHE9h1jarO7hXLOHxDV5DQkFe/XBcRjq64VLznUXUMeiwXiBG9pOqQb2qtDgSLNAebmQKYVQjgPs5sAYNPcc/cb7muuptd0qMQLPkUIBhC0DiCdwhJGm5G6qtzWvMZFAkQMWOx7nGubtdpSXXeIRDt4hxBfVH3RALJ/ehaFZtVkWYMGJF1vzHyf1+l/iUykFh6Mnh4CgOByvFD9FsZihfoHNVQkEZgJf7VXiMOzTYmVwjqTKAT1oU8MOgQlhD3SgEg2J48Kc6OOnQ6xhXMQPQjqRoztsrJQxtSSiBnU65MRWR5t7vND9rHKRYJCwXJ1uXdtqtFeIzGSl2rHG9hUMmF8PU9ia9DXE5bRbDt0RJ2dC/38zjcJT2dqLGLVDESsdnuChha2i8GZDEcdYPH8IBOJkOJA7Df3HUEc9s+kwqsLb4R5UBE6mGqEL4eu1o6WJ03Fpji/ZvH0BUnyO5XNEfW1r383mj2pLl/YZfn0r4i/ZgDXllZX7xnPo541zVCHTlvgMuybVjVw3S8h3XJ587q+TQ/GKqNmagSEuion4Am4E3o5dcFkvhyTZSzYeMv8A9zfAloZaMQvM6uxqnRy0SazzNakVkw3kasrjGbr/wwZsfLa4+2iqZgHPbD2qyQSXE01LT3joxMzX30r90Ym5y6X7dXEmflb+vT/foLzBMTgorLVMehsFJrJDaCutjiVXr2gLim5+KbPWR68ZWkcfcblyzSR7rtf1I0C8pop9sxm8H71cAHK6y4G9jTZB0uYQA7OH7YNtwIzPFb2hCjJS/CgrRbxN31wDdlKBXEyitX08lZbZVM3kOqb063dWkS33tYcGrAtiYrFvLJ7UNhrpuyp5PkIV3r5Koxz+qpUkW6C5L1wj36V5DhE8jeHZRGcy98H/uT+7Wl/exWSkgSfph6EdGcw/U8ea7aNJtHgSoHFD/xXb8ZhWYc2FPqjeN4q6+F2RIRrJsYPulo33KfPurUq4m6n/gozpKsuAiWkeMqPTxOHszuZgthSytMZcN73L5XeTBjwmusYUVWXuAPQd34mwCarW84/pZ/sdDC30mC8HClsvX7YC44jSM+OhcE6GcrKv5qn2jxxKnqLxKIGh4whp/+329uXfByZVnP/tx3005rdEx71wNwazNNoPsZ0kq6OMn+AV1HTBm8b9ernSUnQIeTtIL5A/38u6sj1Z7lobi2YDTHmzEGrUfMzBqja3qEpmMgqyGoBnGqj/STnoMT3j66OLZCGHV6BSU+pnCA6etW7lZEFLbNp2GFT5WMUoGSiB8fQd8KFhjd3WIWDldbbiVTfry3llymbtQCWAORCGQ+IBJ2YywFQ3OFaqvHS1viKtsVr3OSlPzb3Bn9F+AWs+7BImILm+Ltb5vLTrLenD+jV127PTTIKzazH35zU97Y/Ysit6sTGzHSCE4vmcROHp4/Cnx6iB9seOEqOFDi5L5maXhKoqjMXPIjoh/yd2nfr/Q+DGbw+ssWJGj52FFSA/amp2vr+SoaRHKVVdrXfvRC5SrlusDjdJU9CN119hdtDIon2cBZ2+x5OSUmzH4pbt+v4RrGKqWvO5WqPQOQZy7H2VYzSUCLCmK+u1qwh1VCsfR/ofm04qzGPI80ljQiZL+2/eLfK6RIJ+aq8wvrwt0autIXDRbM4VXZun6lxnZ1CmfW1MEdZRBiCyAbrHpZUuQcFd3V5yfiizjwefB3NYw2Wtp8EUBvhClJyjxBQEvuAzicWpGERMwuLSVdTQXHli04d42Pn+GaL+W7galfBaSlvvryUTPWsXyrJKRlxpPnAbz6VG/5c3ypC69SXmXzW3kEo54ZAqawaXYFL13ZorHs/jga1e6HAeckEJyBeD0ruwO8LWiyUGbYaR3IGyKFb6EtcSgpHQHJDtFcpRbLGDZx/o7BOtlzLsNmFk6jDmMzmB4iqmZfCBvlU4n6XVPAIHVwaQTBTjHctO1abzwF+Out4DUrONVaoalJ3uppVKXvO4klGfR3YMuKcfK8U9jEj9YGb+ib++CFQgVulu2zR6quYLk+o02oOBdDqfHvEJF0aF8XawxzBcihx/oWZTbIDwfg4GQbG1gFu0vD6szRneGLNaBoYmgK1wp39j2tSPvGSSG4TZHW2DdwwHQZC+DivHdrR23OmsA//PpP1bCBuh+m3hvjUyMom8xKQlKOsFqzx6/BMKxpdcQXlrnHYXFV4q+HuSLlWKqb0erlkaT/4n7hqmkV2Ks41MweE7s1dgyU1Rh49hJzja/hsMToykgPTfa5teUS788SZTDEuVK1dTil3dUegVBu73NEWobyj7kwg2KUx24Q0qog87kDnZgidx3F943QXeGHtYjTU9ABL7E/hSabNWkb9OfXXES5vb3FLNfsqjXC9bD1gO6mjikxUxOExrpTCHecOvlD2/Iov6FZM4lHboppNc6UihDw3wl7Zlw2pCN1W2geZhYOc30SCf6t6GMIkRJs5TbcQb0kZRMU8XH9cbz1mL1Ja6x0xghgdrJQg1cYSV6X53z++3voxhpM1aD0PO4P2SsePZp8/FvcEO7nG3f33v/M6cFskcbZJPUDY2z4iMt+/+/Z3q71NLrNi9aHhHnVI1lNP+n3FYfP+6HB/+tT10AgnDuIM6YiFCbByDj+j8qmOvFmkLfrj6+I05lPaElO3BbSWLPB4ME1C3LoCDBj6biMw5C+2lcKjy4oBgAihqV++EdrQA0nYyRrhm2m2UdYJA/jelq+iFzIoGdnrIN8R3eQOT2MIlgsDSthgkKr/wDLaxwVUqVUambKB60e/FYzKxf2LP1gK9s5q4leqv+4jkGpu1iVdWXjaczSVoIjG+WpW6ay/2qEzi6JVy21aqWkAMoEDMomtCajIwfe/gFOsa1aUao+KjFR3pz182WZJjiES2n30ssO2imdMcjGqsqDgZ1Y9Su4wcL8raLQetufIfT6aCk3Ub5lkLzM4xsXyELq39XD1fxPpgQ1KwgCcmLFue0G51deFc7RcECEbsmYXlDRcXPZGpaSK+EIrOIiyEe+1WzOs1HTn7GS0m0XdGx04LcP/AsjEywFCihGd3CF35AylOQpKutbWsGPJpR6OHmkfQw07d4UixZ+HF+eHQ7/spKRuPt7oH9jaaMXTE3SSlFwsAY6UAJGKF/2nWDLWq9lasBvgA6nBAUmg8xL3+mpm5hU8Nv3TAq5KRCSCAj8q7wzJHs14+xmKjRQ+U3R/6JFjkm2sq/4RuCXkeVxKwN7Rwg5aXn5nciJgvW96vHaPJixWrxFEDIyGjq809mmA8CS3MlI1+akjeBJ2jg0kNvUcZ2XBbSPvp3etGPwdILAN6TZv7psdk7bEEOvAhdBnsRIG10UPQtX7goDdTi6vbqR03N2t0l5ipAYt9/L4tAB/cDsKQtlzMqIHUIgCP78Ksn1wKCxXAKfMJXY0Hl/4Wdg0TBuBfBa2JJz4HY88jjIZDXcqC2Tm0XOTBRlx5ARBm23ztBFxKinfVoZxHtND2flObhuYpQJ0vj0bQJPt0wlsOz4ucW8aewpDkhTZGVHp/usSLLHlsQOf2JrrlTQ3swBjt+OJ1xNYPGE58PeCsbJLLdjTaLe/bGDfgv0fNqsK2hkJUeV+ub9uVy0KMhdcusvUM56adnYok2wCUCU+3t0LGAtY6OQgMGcKBEsgTyB8JZfik0pjShbSEpOb/kuOgV4jyEX/swXQPnP9VbVJCGREmD54pjo+I4ZMMCT+iKP9ZE7NDWqS20BCJ4Vvx920FuADSU2H+YBhpd1jWrA754SjDDx88IxTiLw0Ke7DlzMvN+KWbcI2dlluolUE/rrTgrwL603v81JqCPNSISUXcXwdDtYCOF5QIl+Xk1iPdWPWW2o72mLvLMlkxFSxg7iNN4R2YXw2WEoI9ZBrkU3e7ZucvS5DYjB7lAFoW73SpVNAZKRx+wVT0TLV9M9CRxLB8OAAy5kE5n0IcVSVTMCiccrwbqJwvRGaVLwgO1BfRECIDv1BD5wkXZs9PO/mxkln8m2BHuks6msQ81+Bybffw9HIOQvpYyqAimkZiA0hBbW+96Ad+5T+5FeEF8bjROLCnrVXroOYp00bCYXad4vmL+qFTaCRiVcoQ9W3EUW9SeZgznqOkPSJK4AgTs7sgzi/m6ZEBOfvtkxhPb2tqTdoAq592v8WIgrvXosQwmQAxHsSu0T5AO3HRYVzCfPpNTo6Lpg7T+xPtxyHtJvq7mE5kf+lOWhDBx3krBm0o3fkluDz/BXsJ9uWifhXgj8Uu4oOd6P+vM63r/nIKuh0lkfrDDVSMyE7VoaPdbSn2MqtMeTOrkaOke6sRjUO6yx+1+2EoSSeWN/t6b2WXDQl8UP4Cq48P163ELdAkeeNjsvChUQLNgp3eGXPRy865O3IhPcbNwnkargC47mvhn9JjykZpDUEpLmLfn3dRmcYH2S3vbBqtEl5ngSXk+54KCfEgusk5aHKhXG0UZqcEnTnNLNo2yCsyOwC1i2NuvV0goSm9Z6dxEK/gMgDzEgLEGy+maFVUsEh2JUiEnbL/dBDg9mC6ejPOrlPL+P0cYeaecStP4SCo8v8hRNUq4EdmFfuBrogC8ImjkbRBoNgWfoMYqUR8oney5Fyh3z1gQOBrtV05g0EkWmT7Z9UcMfQooBYrPF7SZ80SAxwUiGuZp0j5DUYOFfnMSSx4qlZd7tmviWkuWU0EjCfOMzu7RdFIeehFEjkVPoEkZnyI+vCO/Gx/BLdTwav9RR2N1kzqEw6BCa7+4JVEaNH3rncs9QhZlCZZRob2J/b/8xfI3eOrrOn0GPxi5a7jvasebDlGn8dVLiTsa0Vx/ul/4cCIuHHT7j5+w7Y19PGieykdCpNLUR+V1okyZ5LmSdILt1q7hKOtN3vZEsxva04ggAOhsUGsRlzimhLSMEAjYrrGLahVBIUd53p9gZ//6qzE87A/BwKFGZ0R2E5Jy+FAkRIA3+RKljjEozKjLKp4TNztztNaJlrEeTbLUgkk9o3vbSbVa35ffqr+A579VPmJ0Yv9WHlTIr8Af9sleMTwlMt6pPOx7kFcjqTz/7P85LOg6rgWEjpZdI2tY2R6Ch11TakJHLzu0f1iIwAsXvMIX7TkYvpzVvrlnZWmY8x4lBvJe7918ldwP40Fs9SZ0H+2Rt5ZONKZGmUxiAtGq9Gxkqk5W1W6euR0G//gWBMzFiPHBIx969ZTVEyAcOEZoOsE6pMMmLpKejBHYpRn+4pqLh5k+Ba9U9WOXHXaafMuI/d4J9e90knO32ikH4vH+NL/0OFHjYEXR7XAySVc3d/Ats1SiDZpO5JnR4yU5WP63hDuCpfDq+xdzTVPKDSknP30+VeqxudK8wy9wP0uGACToqh2pUL9YqBUazujFzsa/I6TY4K5FZGOtsa1SVK/CC3t4fMzCIbzUD9/D7tLNrU2fqo6xC0iWNMLpurT53OLzEoBg4oKRxTsN/kMfxmvKLWsiahJm/D789PlRpiTTuRkIWbiBFqTpxzFt+rjjsmju52qR8A7DUda1LCdrbX8RoiSyovW6GncY6Qh4SXXBH6RUvTmeW2GA2LCQ/l/3gyq0/DEqdHofQctOgOxLF16OdqNuSfL8u7MHdd9kLfwQukVDSnMmA0oPLgmDHfA5m7wq9uxpPdgIwuc94VpkHn/ZsK0sJ2NsZ1JH/RXDBnyK9ha2W0nQFCWnYQCk/Cl3lLIUKdbXTJV+ySH1sttNt/kA7Ju0oZDynW7/ovv0ido/D85t59L/W28mUoDgD4iTqti2SKc6openvYHwlB9O7MWGNYEk+ns9gsjCJkhs/LaKgUCmMRwtW2vTJdMf+dhEqInxcKn+1jVHe5dDdPHijnAtSjUTuY2FoKg9XP03pEvcSpWthHgtropfSlQ+OeZJrxTNoK7MPOtn5imEVZqc4caFrG3rkdhi1AwNYX8fP0Ozds6U7cZ4Dcj6Cm088q5oCO484ClEpL2TOXov9QzW9Fcfsv0/z8g7BaVlv0SSHmSfWIUkYHvBuNxUPD2uUaLiTLKAyGP/SDuhfSExhDXI8cJyjpMESJaMg/RAgFCDMboE1P+PMNKV+hexbZ0j7hnIuN1V0yU6sldPiGkUkeCsdUhA4OHzpHXhirGPkkANK2nzz5RlHPdXIQDIloD6sgxuaw0Ih68XAY02o455YSg0o9HTQPBJ35cKq62G2F39+NH1t2eM//O3rmAxLpWXhtl4HOoM4upnEGf4fhIY4eDQd8eN6FpVavd80uykXQnq2LVUC2bcBPGcgVJcix5FRdvqNndWKPZFtUId9O7Cvna+Jv5NEaUCsEvj2LqpSYPuk6/6ktMmMVL0GTXK+OtWA9cLFjgQ+w8mvENo4CF3wapKNqcicScXDpv5mq/XNA+H7E9tAviEg6rEDpu+QBjMonNh0nLeZ2JWjLr8y2qFxw/BVgicudl1jqiWGPL0mdE10pOZn1AiSulx6WXxkDOOXcjQxmo1KnyftbAzU3/+tl/ZXnnmQ1Pasbk0lkcmupEdaXB5OdzPCnKaXR5CcqcPbTYhmDE/MsQ46GughXl41cgZDpd7tcVettUhU2W3ejlBTZrAhC6YOJfS5+gxGk9mvjGTQmNk5F3+wuH7C+9xzN3LrwzrmqUhLo+lnz8vLNOENXhGc5dnAyIiymFxLhBtoBFbDMkD9uFRy60geQ0uxdLGhB2cgPZdVZDXSAkrDk/2DKH2c1npMaKRwiaQFTccxgSymC0wp/fhcXJom+yMyNVaELzLjDr35SBDZD61fVI59p48D1KGnIK9MPhlC054D/yYRU4dqlhaEFYkRdB66BoxOuHvTgCcy0xaqnm3vNZrTxZ3TFedqqOqPr7LwA1drbCQvhjgspIUSfJXaheX1Wl84hbsVWmkszBi9Hl8NSbFRc741QL5ZThRFaKYkcrl9fOkignmxWUErosx8jAuVGBZILDARD0dTemaEpuDjBz6YCnIYkV8Glgn976TG93FvCmqnurRlaHVPayecyaaYnyfOaz6KohILxzJE5Jphh5INuxsgzXX98fGTlE1EYJmUAtdXfeTkGnBiXJv1G+4SFSEVr8urDtJAbK+ssrXhrTzc5fgMDxwbL+XZSZe5Rk2lV/qvbI+QYasVi90LcTY+SYr4vXevzeZNhoBG0a31zzDsh8Wjh0OAHqDbqzaKO3lnZcevEgX8G75TISICN1vUuC6PCSBbj39/J928w09MB7fwaCDDkTMZg6YcRszRK3ZnsOcjmxIXMNQx5ZXrGmf6Cl66985UfYMb0hDzxnzE/9Zuzjt0JY+cV5StxdzXBr8nBi72eMX4Gvsa7kazcYGI6tKbpc5plCU6Vpbcx5Q3IyP7Vnn/uMzQTFIR6zjvHult1Wt6QaB0mp06lA/ii9Ik60Cf0waFzXHJqVX3MbOAX+wnq91yBv6DsEKB86pEO54qAT1d3cnX2e9yvtdfx/KIPLMn6hb3YwnNkipeFPGvpdQq4KaprhqN1yjN5vVQwR/Y/7cHgbTtoKtZJsIpx5DyA+aiXIWmk/I/273kiDT2rfhrkLsAr9gGva9oqH62gc+D9N6LeVtiWxyIN4KqDStIa9kVrPAskJuymi0e2C27m6VJWDCgnD2ltwSMwvT4WpY1wooXdX3Jg1VOxLna5uzpr5a2fqB0hq0ksB/7rFmCc9+oDH4iiCBTMpR89gcEXychJaru6nEru41t+hqTYCrRzPHPGF5wfTAj5SHCTn0nodMY7sbXvgs01qhsp/ZABMxA9HC7Lwi47nzcVck77nN9IUVTPMnAOC/bWBh0GTfrFfYYmTlfMqEzvuZRPvUPZYZTU+HyZcU4ZOMbDFnIPKfQ27OXEr2UHzkK+tSrk/DtyPL2YdotDw8x5sYYalBiZqidGqB6MGLtpakBnqOmOpA2oLuDYUrk+1Qu/ZQGZ27TKky2apk1VWN6vtizXZPHURP6lThPk+8SN+Vr3k9PoE2IiMZxj/P/+vmkQPTrVZh8kV9K4QZ8awHmfoBr3vlXs1Ku3DdGfzhZEG2EySh1uwfbCvJmRfCyv4ePxFTmudC511eu3hn9lWfI78GEJ05CCUQGsq6D1ZJcWI+lmy0X/XqX5Qp/BIWreGKIsZKG+pcFkecuGy258o5y5hTnHaa2RjMAngpzwKpm1BH6fuePQ5/BY1Qpq3Y/uEfEC8sJtm/zvGXm83+2NBezu0kqHLKPTHuBpw9a5FQb96dtCsVA1FOLzDA/HHIzA/KfP0www9vFlz0nmJXNJva4VTat8GVjJ6mbOlNlvN5VRqt1N6buOlxa4Wn7SbQ+/KftHZAhJbSkk9Yea/qFU70038OxUpdbAz876CUAaWn3KS0rd2/dpjCB/g/b9XCq4M09EynE+uqLKCA3qQzfPdvaUIzwuHRPQSjyMqEl24aigl3porpglUKWaFcxfDL6BP9oDrSMHk/HYIqcBIte9DH8xhMAXdqkDTNw+pSgBEaKM+lI5Ns1f8iUpycrGB7ANbGqM0I1NuIXZZFD4TvTZ3gC98BvFxlU2IKTRIifLxAretHQ8jAjPCij7t24YK3CBFTnXdEPI20PshlmsQB5cNYVL+vRImhWa1WHqnfmf6jPNSPcg2nTf4t7mt5qEpYkpiWlzypkH2xRANwzsRtYEW78NaNLAvg6q6Ha5NATZ+H4lqa1Sh64JXHX86+ZJ29XcKl/G4aqt2m3aiOY+GoP3Q/xyY4oRtH5QOvxJ1THu2cp53B591T6nLO/qDgMRm4YmLqNqpN2zJoqq37koMi/6tlsRWWTYRhEyrOm5ypSxL4lkOQ/jGI3ISCQZetdSe67YRSsUgkEFL3n2o1stHAkdulHFkROGzPoxLiEFyyV03fcU8jVwmchaHQNc5X5ch1UP/Eqva1a488UK0byibw5fYsVGXbFpNt/lBOW6dErTELGpUDK+QThlxhGZIXJj4OGjpB6CE8XzWkrLGFxnqKalnVbGTeGNv/bnhM6QWt8lwO4PtXVLPbnpOHsCbnwYoRoGk3Qn30ECwHOCSp9BJJMSIuP2pwwi4YjwTfqwVAmnWPCPpBKOrXsDLLe+zOZ7uCKZRXNUdu2v5cvLE434c+t/ZWrxuhKNnZBxWc/23q2RRjxye5FBFS6+zsGvsg2crfNkae1zhr9hhYC9atV/pLOo4AfN9IrdMm/UT0Lxe2NpAGUdhK6dIioUX/1FgywlxvdQHkANcv8rzaHWEv9H5B1WlTwKQMdkifq+Bl41eif8B0Ie7dO1QiD+SrteEg9UhkJOOwXTGknpLMfOJs9yr0Fyyt99Hwl7z5WWABWYqRr602L01sNApM4pjD6CYAleYrlPc3Hn4noIbYigOvmw6st/wRuCB4Ml/uIGXX+4WhVFiSgLnMJBrNZ6mZRAuM/nx4BVgny4mvcQv4lEoEkJ5fElmxtuSDg6AQ29kukbAS1y7QhgE7sCeAv7/rFXnwpAfusIhywrlB1UgorISYVDgMFH36L4+s3UMDum+9LQ+/HtcdV+pumu4/ELnx26Z9JzkP7Z9vO+qt12gKWhtSzXOohvkbUeNET36yW2ah5fMnm306efUV2BAcEeN1AAV0OLpSL9bjBxJRAT3mhPNrsSgn8hBRsXm4NJP3cbAEoE3ysn7AXtvtjwe8UOXOmWlpohzkfEKEq1kE6/b6AeAwxC9HqcD0PPvddGlVPGg+Oqs7Ww5o8zfI6iTFO2MZXpWZO+hAGHM9tKCktAZvH3O+zQH9GX2c4EkFGNmyolfjdvEXviQBWDpJLMznqxAbsNLK57m1QtdLFqbQhGPt3muV2QIzD05Dm9GcIDM/kY8UtHxlgRuOIIcCZf4eVQ1CkZNvGZQ53at6eh65wCnea8Sqo71Qr+18R9dQc6Kq9rVrZf0+bRp4yVGPh7FitUE1LG7G5Eb4QwWNNK833ampvUFG7JjjMFFPeE67ikgFBzn/5qIhDX90crj0JgJLwhdF64coN+io/cmfG7vvpdQl1cvUn9//kAQxT7BQFQiWm42GTZUcnncIesvKAICF43wvFEQwCLgn4jA6MgsDbOI9KV+pi4Bt6+24FzbYItmV6xhTzwmM75nMnPdbcQJa5VJqYiv7nLXNggh5LL2OrqB6O6t/AUmld1CwDeqDYViz0jcxx9xk0e5ygv0eI1KNB3ek4sD12hvVkDmjhiEWCLLiR6yq/o2Bq7xSw9CxF1w3ij3bdnOflzUDAJuQDbG8ziW9wF3g3rM8IbcXvOXb9E3AFDpoeATSIgwgc1MttfJqf6dVWkQbgQpPx+xQVF7063hFuZFOphkoVWlUcBuCDnLRkpJcpA84+4ZhqnoF1dvoRycl+g2C6IndJo6JUiwJR6xlA261Ow/pUPeJx/INqAim9Lx6slnxGQTQXZv30+xLslrDSRBldGR3FntUr6xL4fn1qGfJIdaXYYidpiIYXsvuigPKWoXTYEKThDVZqwiecQQT2X8iu4D1n7PSERnM36DofvEXUplMNbGCkb+LV3MReBu48UsiX8afL6taSOA6/InoVIz1yLXj4iyFxqh8bKxHBNWPBj9ywx2F4Dh0EG/DtWx0tuERj59Ac0NQ/ARXN38YKcnnGoeG+xZp+Y+JspMwz3qY+Ok4HOgmV7BqHq3vGj1djTVh/4/QX7Ys3mZuh9VUUO9MBZpolg4htaPSXYwu6zx7opLOoe6LZNAsn2dWz272cIIVj7IuZonXdcP/IXuH4GW9EYvwmhAM6+YxdsCEjlybmHEG2aPENKtH8vcZpD8GKCa+DXWAD9oJqT33+sika7RY404tIo7FVwrRY2xKEUfEkKp78mmAmdYtv2kaS6gLiSK+7MAuG9NUkl9+KSeh/RNAsr4C0DMeBMCTE1ifI4Azxi3VLHpQrucpvZeP31WKFdQ+ZKYRZa9AbFDHBD+ItAMiH+GR4tgrG/iKgzQLRH4Z2svjwNgF0FdEfZVasDg/1nTzj3sxxT6uURNTqU0CtR1aupstF+EE52MFm84CEUBIg/TJnKK2rq4CMcnhHikJykrukCek0U1Nnvq5H0YJXaQa4Gv6jJiEKXO/hRbaQT9TOIt3al+Ch+aBqDYYaQfLhwwzWTAyXAIDbTb7Z6cNJbfe+PC2HXrguV6kW5/1YOTFUfpTLfwmXVmUwfBdiiP45hqrMEPS32Cu+ocT7IsQRFMXM/VhggNWxxqRUWw6vRNiomF3dUgMlTVxWZTV3iN7Ztg5IzW33ga/0Jbf8GncvX+BVnXkna/QHoq6wrEXPoJGjg0KIiWNB87rYyDTSzAKEbwQhZ4O541Fh/tpQA8UFAEf/urZeceuAlhxUeUCmfLyGz+plGsIhq2R6MoToFShGY1I6EVBiZa4RhLLZ+0qwffM3DKmhzW+vnwBHCJHbbw9Qlo24YKx170g+WEfMU6ArqfKm0MQdEb+kmHF1nYn4z7fasIec8Y8siKfNjxwrq8SOyfJkOsodzR26tWnxO3kYaakXhi9Nj6sXp8uvRiUXuCEGNwmBBtNoWfGb/kmeIzHBr5UQozpbsBofVJSy34F/MJLI/SJjoMOHi5dUJGn0oruo2zWH18//VnEhneENzgE5b1cEKTtjqo/ncdpRmGGs4NTzj7r0ntQwuStxpwbb3VL5FQ1SwM4qkFgKUc51z22awbFjjENUEhJtxKY64E3RAgfU2unxamwqLXNhO9oZAjVj094XPTtYetax46kT8RHtN3ZSnhguqvC8ASfs3z4+migdQbCLWgKFVCGMKDtuRlzwetIXCyASpc/6VnLX58WBX0WzWNKMjmyFFhcvMyvq1lS/NDez5whshAgnKNBMEdHf1et7CdHQit2+dzndiDtjMrAQJKc7ZLyEnCRyc8Wi9KYbwcwyjkuYWKhj+e2PrGQcxqsjRx3tZcwojdamRb03ZPIJB9sQdEYItkv0eAnZ9L5Xgp5w01UTFUf3Cz05uQgZPOfbk2NWeeoYzRs2j4QFNCd6L2nKhiuCTRj8EYqRpdcs/LRFsUa8pNPIu23XkRiga3ztdviZPI+mNsOu+rruwW6hHgQunQH3HyD9tvvzsprQrr7wntDMcitBCl/zGY8wZt6Oc9+uiUfD9JUykvhu6FSmJGqDOWpU47niZWl9thUtt5XMlPgs7lR5TyAUMGIWdo4qcjNsMp63FXBaFqNr/25JTwmdUX0d0vy/SRosImznG79dXoPHT541eSZPM4sKheCCKQ3CYq+PUKZteHb2vs+9m6GIEcmpX6lTX+9e4V5IVhRvXZ7guxJQq97vFSql3NyIs9X2+iDnLC/FX9p2OGzjJuUZUPQvHelTbED+VsCx94dGutqpG64atic4vBaryNCDZNn1gNcfSLLdNVWfqPrKxo+vIlVt89316KXClu2I9TrpuRcMbDur/7PJBoP4R5AmtTOfhprUiszepMCOKAffao+8b80uOssIKu4Ehmju8lbmgGyY3N0wSPSmjvjkcm7KUx41SeHC8uiXIJ1ort0ByA3NOg9eDqXMPvCzHAhZBCAp9oQEmHdfdulM99MOULLzpQl3jAksyDzOr4R1sUXtaBxIthzPQ06cwodEcOZsEfs0AE6n9jFzBWmqc8klOB9ZQ+J5RJEhdhd4tlYI1x2ZaAiEiO9PXhw36VgduXGHZkJqFHpKlVlQBPhsXlBiNdcq0l68FMD1BmLLdMA3rP1OmYqmennshuR70dPtVhR4EriXAqZZAfPWMlRyYAGd02sad7LA9vlt3Ocfw1h/H5JX0sfyPNJh6Nbn2CvmBoUT+FTBn2vhI1clDjCuwbkgEcmuD+VcTN43unW3TI8W1JmKJgfeDo5hJ76Bh7Is2TcrO0Ogcg5z8COITY7kWm0Cq3Ab070T6hYFFDpNEhmMS4CjoZuFxQQ2/kRVeIzTxWw2X/Kp3YBhYL2TE48dSuagUaImaS3dMSGFI8ULXPBpSKO5iNU6pCMrPoDrEaEY87OfD+owp37BggFfNhnES2oJKMqh+F8znPjICC+5z5ndcBXuBcXXMRfXkaLISALvEvinizQTygw9gvVqnpVypGl9VyaEPnY7A+1XZAKq6mQNcpjOKPxjuj8yk6YInoVPomLheGx/KtRagazeYN67vbJ6qLDzab8yRnyREO0NneMzeQeRkExnwjG22b8OXyd7wZnTjFenibOz42hjx9UquflsKDL0D+qkuiKuqCVpCKnkNTLSm5emIVrWMIMjgpf6+oORhUvcYOt7OC2B2VV1R0z1J9LfWzS3lXw58jnUivZISP7d/lBy1D4tduM7wTsiMJmVePFh4755MYbjshrRuhjY1sqwuKEZQhXrLkaw+yS5v9PuBJXlTc6KruTi2No7J/U94s7yvjjcpEVhVkrZGswvwOE/iazsR5xJCV/rbjDkrPqUBiQHVCnLeKXrArKg+F2V6iFkfYiYd5oqLQ7qfjR4e++ZkYs0FFHgWIa2plyxYrV76EyvCiL5qw3yZDN/n3ds9Sdh+WKz/NR/6kaCqCnHRSxKGhchWnDDIF3uuTGu+K1E42fn5GURwjRK89ocZ4ldxjXfqK4tidWs1gZ9u4fBZBV3mFeOefKR83RvhZr/Kl4VMX4UQ3pd91gpwSfSqVw4yscvWryhCEq9qZkaN+QmWIFeG3dohLr9+uEr3zF4FnH/nFADx9Sirdl+Rhbd88Pizw5MI/pOIf5F0j2Ocvz7PWBPVwo9jKK9pBZRZz0FVEiS+7DL8n0hY4PdyC1Z1wY6f88J3I4LJPigkDo3EaCYhkULK9lNNnQkG4ZzWIMHH+f9Rsjl/IjCTG7971XBT6Ikg4XmujQb6bEhx69k360iKGl6zEW+0oLqpILqFILJaTv8s4UtNAnEnuy29P+BwBzhlxfMwrMLIoZGsISmDAEHY0adGRRhArJJrlek4lZP774iOFjRLhXBywL/nP19iPoj5d4B4t4dFJ8uUchsfSrZ/FkO9OQp3OpiN0gKHUWSk6ueeFCLtIb87ky+huVifPP7ZWX1OF8AiVlPOdVAlwgxuc3bSH8KNzzuaesrCDrCkwDlyEEDjPixcgbUbn467nvA7mcghMojZrMmOCn8ewf/HMCL29ZXrql60STdfLyGVFal6lMast+m4rKDxp0ztODXODdlJdPNe+iY3+7kjupVRwhvc+sSjO5ZH1YNvkb94I7QMu4zr0OHi85oO5Wj5D6t2CurfT55t3bw9YoZOusZ3Bc269EoTDSrZCIJyqzSyDZrl5tTtq6l3ilLxdQI8JvNxdt6GqaFV9Zpj2y83odC8HrEpHzI9oIwW2/iLZrfrIsrS7A6Spb/bp1+i4THscua/7HAI+YimuBGXL6HxMOzyGJLWOV1zJHln76nsE5ADGNFbV4p3nKGqBEEK/P/OV7If3CbWjkYGUi+TxIPPgpDNITJLShvNxCldr4j6LcA6a6Lmk48AT9ocZTpeaed9N0QHMSAC1TknOwbXjkbfO6sUZW/zsoMAo+7/7eMaboeTjNUdWc+XKIerYs5X6T5N5fiuoL2yC6iUeRreuan7eXBFhofkuACypMDpL7oOSvstHeOoxrZeH3XDoyOIp2pTwGOzYF9neEyG2PSD1xuUBc3+tBpNljsujJnUteksll5I94NESUMgw8NCtRFK9Mmai93+fjzXPp2/NB1Q4cbMEXOkOWDyLtIOOmrhy1oyRO7F4+jPELyuapjOZJVgyM6fntljFG8NQoLC44aqnVdKIzlWkCIly08McN6WCHSb7riFBjCY0u62N867GVKCUloADpME2cde02ierTFlnBxYAVlWYxAvWwdHiO3670xG728L9WCxInQY7gPGxHR8TnCt+KVpFtnbm7TJxsH9hnK2Id0npIaPz29TGD/7YNQQ8oQC7ik1fo61Kc1Bfcm+u9aU+bEDf4Qz8oDK3RUABDKOy4kaQp/HOz34N6byby1iZGyv1gfB1E/txP60lKr1N0NS91Ii3ZNaa5o+mpJvNFBDJe0nCm0OU8TcwOCGz+WTEGfcP1CnyLbpqtE/D5rSphfdCUDACNK7dVd3SDfDk1aHfhL0VIksyFpujgqpSQJ3dAU9BVpXaIPkt0rqSMpSV9q4TWKlWYpUjeu1tUuLZhUGr4379RqjZxc6udRKhCqcr8mHsc9w0+GXWuEOMUXw29ZmrPN3Lh/5BJ2ebNtKZ+SmSOH5KSA3mcYILnYSOcRebnk4AkxmoHJWNYTsSaAc+rDYkLU5Jd4Rhs/HbWoj0Y5rR97Ol/J45mcQH5Q3zrk90PbVRLhnRYihhcLF0GhWcvF8hfvRQgdaTkLw5XfK5/1ecSXwgm8BlHh/5G8Wgwl5/LAatDWA5C7CROKyXY+w9tYSbnYTufVjPEV+mI70FPPUezo/NL19IY3n26/EUHDqeWsv6s6zGrwa5ocCH+PRmdilVh/d54wK1qOpK4u2tpsxTLaq9oz8TYG1tGTQOde/UuoWwnos6cvataXJuLxLGWyXfe1IZtVrMorua6J4P2poFk/GjeFmSSP3c23UYRz+qG1A/qb65b7MqftsockevTqa4PDi4lD83/q93Xvj6NW3zpUt38IsMF/H2k5af9viUicHIcmkOQfxWpmeF2FlJ/GsE1SNl89gHvoC2XkaPmz4pQgzmOsHCWWVX5wWir2scw2CzgPoh1BzCq8QNkFJlHxR7xOTTRG7oBVhEzG/8VG/hhcjWUPbLGqEQpzy7s3GPG6+3DlOLKB0XAIV8heSGle8W4h4LxtIGZdlRVM2aUSVDRm3NeQaeAmttq6f+rlgdwVye7kqEMfoynrQVPmlI700WhTKra9JUQumKeum2Sz3vjaSlZNyMYlQ7WM/Pd/1L099VjaYVPBe398sMXZcb9Ye4rTJBEQKoqsD+BzDmAi5f0nOCzFM7IL1MHaH7oS554cP+6oIzDDRII0xTnH/GKhJoHq8E1cf0KMcGF3s+3ZJ1/JTMRPNFJu75KcznuLxDjy1kqm/hIXiuie43s+MKcIN6LZQzu72+sMzcYJCbuTNcCP+2Nk2DWxsGNpMGqzR1dMhEV+tzDnKosTHyHhfRDmX2mwysWPakkX46SryKuWPyyovgvag9CcfMwzKEX03DAhVAWbZD7ICS+teJgQi0PsrhIQpM8C4iXv3HeNMWcVFPxepUp5vYhD96m+CTOaDcq8KiWeyMTIOxhgtY/VVjKQ8hweyL8e0vZ1B9l5E7HCNg8VPA8wVxYSFy7MEpIgk8cl7WmsbokeFkpHtk8Fm1UezRXrRquUmXeY+GuE3HRYurVGYFc/lUW0Df3EBn+BR9bgguylgkgUHvJ12dQYfkYe7noVFmF+ss05YjxbZm17mXmXxCBYVTcwR98Bhs6ncQX66rCONxYAOsrmZ21Al+f4fg4VBtW1F6n7t4llFvMCpBSu2p+JEZmuLIN++U2xRl+1rzvzqZXTPJqQCIgSYdGUuD0iXA5WuNqgS4gkVZRU/Q3ZEbClCf1qsWZScKPKe3xpuzw1XWPq494JxUdwKt74Q1OfAY+w/yslc5zRMyO7nH7gFsGRc8weI6M4u/bSPcb/slNkZmyWBEpLMVLhM/aEDtkH8l/te7ixQR2yo+BUZIJDZc1gZuhqlDzSr5QPNDjknU1DD6U0V4Hw+vHdxeTYYLBEyr/XnU94uRAIR6FFcWr27KuaZVR2kDw0hjqh6ErJ7RwkOtYmeVS5XEFqkzaSQtGWsa+MV8p/vGHT0muhYx+6vINmcd/AWonlFuKO/iZBvR9PUQ7ymt+9fdzsI8SUJyVqxyvzi/F/VucJmUsNe922KNUdcszW6l4ON0X6yCAvdZGR1BgDnuneDHbSqkPOphVS+6nA0KVjK4S0pLAwQ8KdlmT3E7lMn4ZVrn1SpQXHcnS9L1KL7TFZD38Oz5MDspPwxMStRe+RCAZo1IfypYA8XcHYPya0y3G1w9b35nQeMua4HBVCvZbyn92hcHqcUt9JW1lZ1HRMRXhugIfLwzbBb4F5HFSaIeqiW5MQSsJuXRvFXzgSfDl9qpjXfXMJEIRUcmUgcUJHnIb3vCrlbHNe5zPYhFE+G+9qwTWQu9uV5V0AB2036E/PlaWwg4FoUpG+hOZKK5Zf3wEEBkPnuf5jyzVtMvtQr8AVIXIeOExpXr/Np2Myx93gx6gIy1BbpHNytCldKOwRs+eoTQrOi8HwJhoKjquxebJs80PO80Dv615pRMqzCG9VVWvAITwAYC9O9XCcxpY6WSHYNT07F1cN/sofh9y1act5Pb1YZ0xBkXGByONzPSGCmhmWG+XxkPRTtez4bG1eIibJjO49DgNB4/8F4RR/xT1O8xYwb5F8HLq3d3W5BcPNIiVaB5iuMyvDL7XCSDwzV/Gg8Lgm9hYtzBxxkfvhamVOFwz1ITpt9MOGE+pAn/QEYNRFRIvlIwZhk35g56ZRjuLTCabAIP3hXUImVjgq2HUe37AKQ6wq6+qwdGwaK71PHPH1B3ytYOdUU62DB2uzPrjl2r8FE244OMpS9DZ2VMdeuBx3K9Zuq908d/d/Oibitr2+3cujY90+nCdjBfPNp8+QZfZYb2eJjYvKFggR3mYbGHbff6ABz3RHJ7RZNqacIZhZLAHOu6X3dFjgAgrxtgyDD7w8trYdrcIM/YvTJ7eFcEOHPAYWCBaCAh3iEa+HkNxdzF4S9+1EoihIjazLNhbXA5XvPxQfVtO0wCKwuKUZVb2Or6pM2HD65OpRsxvD9nVYgG1dXt8igIDlIRijTyzVQClnBBsb7/Zf+xBadS/DnKb2zzdoqqfHz8Zjd/+pNksmDfqXZm0RY/DMR8VWC2Kdlosb4hRsiq16U8iDQhl6CPtyMsW6cGH5EPb4DbG12W71IPJD+tizqU0UMEONXMSnrYniidr0rAesV4yUa/Jfo4RbK23uhVK/2ZQcQln+e74eTgiA910iUk1Tihfo23IVekatw9dRsnqCAO8FrPnlHKib5N+VNI1O4RSeWals4qkf+SR1kK3lUl/LLSOW3tY9TPY8Up3EYcsr0QOkODMSgcHEFQfSMy/S4BFvyNX4aCT/OJcLusZQYc4fiwtTMMit3kPbs5N0M8Y/VukOY9oY7GIKQLUGMT190UT9Tr0RzD4vXKmxNES2Bqgas+Ib/FrJ8gTxAbQMxaXC4BZTgXj3lq6xQJEdCD+AhDBP/ufluCeEkh24gfELvKqJqcJoyPcIKPIYkE1U3yecUYqljZbn+o/7t4/BkMU+d9/TXwaei6jUnqiCd0MIgDIEuSCPlEcTa/W5jdPXFiV+2uMh/aDA63Wb3IVrLqiPn54vvlAmKj1A2K+46dCEthp5oVAonQGndqbmwPsLmGjGVqh80NplAZr0LBqqFZRBtvFhUyXA5ZB/k7ZxnVuWDVOOthAB+AUnQzdLP8KrCPLfj95pHyYlGoyhvX7gXHCVRwDHbP89aorl6nL2DnQ/sfxnufr8yWpsO5SUPCXRDOHYtiqZbP/0bydCt6MADza1AA+mBQ7oXq/gLRU50DmYu3DI1dcNcxZ5LPPLtGhXG9Sk5Aplpwj5nZ5kM/KpX/eC623ICy9lGthjOwG5tpaRAWBYmjYfvQAECl8U3r2fuALSKqqnNZrkADluF4mq8d+I+4+GvMvMkVyg0EXe9flrpofcIEgFEl7hn/Oo1MUACPyN8GgLg1qy5clJKe2c9IVVDNKpZXCy/49T/4IeS2HNqDwAEtB4ZLiS3ciCdFGuI4amhgkoeee4zlWLCjgpomM2vZGW1S1X9GIoztWb9sFd4aARYc0AXBIBUZ3DUCOFrzFHz2ApNViuxfz+rX1XoqNMbe5h2V+mvmT2Rqcx1Z2aK2HBJOV0AJl/K7afwTd6J0T6wuIC5IRf2FGNwoLlewzGTTmp7/j1voLHmx/4LD1EIK4K0BOpdOcwfzKIq49LkX1H/RkvrKQ8VdTGEM2GIm2mhLGh2sjutdUePy5ZDvF1+sgQwxytiMIVqCrH/BFCPBFcmdBBnKPgSPkyO6+HmIetz6XvG320aX7l/okdR9YxUuHbu6HH4ixb7ycN33pj/EfuLSAwGhK2V3cyYsvJ2Mtg0VhIvT5iQ2I8S52MvgzU3aGRDtxm+C3HjPHdPnd8UMEM2RYFzJ6e0NmAvv9ZQnVEF3OiE6qjVGQNceaq6gNOOVAo3qwEAE/vZt+I4hcHVnZNgweb/jV98gKiMiKH2ZNwJuHGljhArXN2N2Q9tJhlLH7dPzgXNR/uSe+ORisljsli/ZjO07Y1mJYJmZTyrL6lwlNvpi2e/tO8NKEpgM763Cl/bER23OmaNZdTXD9XYanC8W7AexWpJGk8MJ8uOCUW3f0Ney/C2N5Mw/WXpH8+8FZgbWvxY6ruP5+lMSYHRiIs80+7GIJR5CBQ0s83PZ9Y2YQvZP6PSrvo3DeTv23UUccF67Dy4khDbrDTvxfhhIWxxkB2aLeOJrs7WkrCwKQyvSbINHjnMjYAM3W+1XaJiys9DYaY6jMmDdVQOGBnr5ry5h4cZ/LMGkOE4kTRb/bsuQ2fOHTAPIuRwZMX1of4NGB1XMyvTDPmYbyi3qg26r3X/a3wWG0NEFmsVOgKs2CydPwAitx9IC2mQAiuC6IDwRZ+HQMHrQYIu5VTKaRyfHMdhwRDYuxqfRB7SjesFB4uN7u3JQOja4gsiWQfgnu5XXe51jjwpHJP1C2/aEAs2muWkQIP0Bl1jvezPQkjsxoChVLMMYz0zvJ/okyOw+gwzIgoEXs1z9oxNLt1jSXxDLt6YrQkjzzC4oq9oESDeKkijG27x3nriibZzgrtOlBo8G9hHXKhxqmb+AcyCVL3zJNbpTw4ElLXQ2z8iEQL7L36zgz2Bwh2XKGQF6fbkQ5a7WOA4jYpfKKY61KeTXz1mdJ8v1H0JEr1I67WZ50h3QlGZMRFwAB7rZByfZVKo2SPb3JQOuKbrN+XSQgyjPZneLrrbPKNMsN1wcDl87wFN7NaD6yPCAcM1pqGaBIYfR4wTO6y4HadkSxXaLgLltP6Km0wUMqf0K/gfzJPIq3Bo4pVJ0E+sIuLgtYzSYluxWjI3vK3PjKwkGRZ0XdCiCzakuiWDtS3ZoA+nTWsWeC8ubiu5TLZ/RQVBsqIWnXvvTVdzovJ3mmcpp4tjbZVz/L0kdXNyrEbwRr4qaHj+KWOXouCdEvUHOLtM9Zq/TKESD8NU4N5p72acc7IH7mN+9k2elACk+R1Hj2Dt+8tFzeeGZzhB49axbS3jF45iKXfEL0XSHb84awnUYhtnvmMapE6VzxLm+8seAA3juE/SgZkXOornHREoHh87H0bNhMLIUGns9gpI6uvp2kKL+emoEcsYKsqaPMXoAVk/Cavm6opWokLwdVa/2Sg9ze71mhgMcFfhGnAgdYOvw2I4vVGTNbXE15T+7ER2qYXWsQ2aK8Hzmc3ZeU5hqGaTBN647MFo3tfXxA78mQh1foVuJOkyDPd6UN5x7AKRPfGDzwZxDxr0P1kIXQ2rK6n4LjqcGCZSNoNbFEYudG7NqFNtf7qMUwdDbzVYPgEOY33eIsFeT8Z+A/jj1U18YDtKSHHrJ5XtgLZIYvHcB/GiqUMPkauxaOJ9QicMNtHXLvJpRMTUg2zQCtCwWubJP57eT0s4jK+oP5b5H7c9S9HJzc5+3qKmrEZFEh4pPWPuUd0JGArmwFRB623gwmBSxJpIy/EF0zmHuz2hfzAGC6Cb7vB1CrC+JekjpjbW9Yt0yOGzgyIsBz46HDZOQzWq9y1sUs9FUwTucrkVvtFs+EG5vzwoyzXKd1nerlilLnFBTqBfmt3vjyFOtK6H4LUvaov4QBNQ7tfaUN2E6oWo/KN5TK4/1wk/paYN8tZM7MjmhA678wHue2RAn3TuTuaGo7PEwbwLATyuhF/eXkV+UAcKxUj6OL1Cjz98U+M1YDGq3IFoHw2XfQj76V3enzPoUinxgVyzf4DO8gst4rh43rhRVArwRh9Yer555G/xYRhpMhInAI16vpcNsBD+r0gRG1fkZTiHQprOD6uZQJtZoc+2UXdr0zsOKWjEwJxgiNljJ8LcTe44BzaFoEgrxL/ZTf4CQ7XcKnWNAvADU3Wuc2IqsY8Uk6a30n5PcE4FfcZPobhan4bU6971SQChoWJaNkuSVX8Wyd3l0+fBZwUgD60HJGU3lIKWQMu76nr9Js3EwGDqHCXfWNeVrIRdDiZyR9+19Ai8CAVRzFsNO+BXPHVzr5ByrLtMtj90dPsJDDNamH7lyeJahiDdDsVEW5PCl6fLnaQXU9qDMk8zKSXqfXPyCjuV6czOrdpNMvxZtYVAGsnilquYVDqHU7zAH+qvCmBgDGa3sRinoXyLGIqiQv4bLyPej+N1XIEAM0mYM2ckuCSVPQlqMXypFSBYVW0Z+ON64DI4KpfDWfilUILnTA8//DoRZ3YWYoGQ/rD3O+O1pGl8FeR3j4Sp+HC0EE6zakJbgUhvHFzsMthO7A3UBTWizW/BVXrb5uEujpqxaujxcryOgJqXZLEdYik0PKRN8ls0j1W/NdMOLxiGwK5nvHG2dFfP5TlUvNW2rE+87OuHczgGwLNTSYZkAksGrLS3JFAJSDvAOFnah2p7lNGWxyaE9mOWhl5WcQ7WRKykh7PHKSfGoPufxKnSgpZgFiUMsQGA2jkqV8vg9jjrZQo4m5ffe7dBwB4cPG39p75QiowPjLBwCGuaBmtZxxUYT7B9qOhsWNTjDr3mMsCeiBY1PdBxjxhEItWUoAFEuR+LrQyXWFDJpk/KmEHmBEICtfvqS3gx/yHlYyCEWqholiFv/YZNG/1ec6jmwFF0A5rS2pZvzXH222LrT9dkh875wWPCTZwemuVjNaSH6dx48IhCUNmnBl14vu271zaaTjSlCze2ejTPSdCtlBE5pYt6F2CCy3S1Ku2eFNb8APmwxugXbxaeRgWMTRBT3aOJj3I4obZGFNGhO/uL0jiS8ebcij3iMPzJy9F8z8q06we4fofe4G8R7LovgyijWOqWjs3JIoCjgk1fAJ+0OOD2/GOCsKMUkL2p2kj8PDAVS1dv101DhkyL8C1t7hq54uf3/A2DU4Px3z3zD7kJBtJjhjwujH6eUlhe4pupqbQxo4h47pRINOsOvKeJGUDt3N0RCzzVoybnhR3jgG4DkRKeMT274zGA1FKsYDh6z0x1MhcLCclgrfhPLVHwxqDgd17C08qAET8uj/oxD2EaBEp4mj8TtM25IOa4Ybc64a9WKRLGRsW2e5uLyoJoVRr2tbX65OtDepv12OCg+3X6nRG0LyY9KNsuPb4JRFmXJ8Yn8sZhFlW4Ga9r/5ORUKidYajuC/eezC7EIQsIY/fGLBc8pf7kM6mz5QoqPU+uj6feiK79F9L2aZzWbpfQXhVddIwfteSIoAQgFwvWYFKIgTigiEazEGtvXfkGm3RLizUB8KHthdqanTyOLdIZqKXxgHd2t1C931I6Wa1HheqNAxmxPYzDixRibgcqryACyU9BiToCdbN8SrO56TaE8VhKQONEcld63AA6OrfJWhIToT3jyCr85NQ0Q4YcSkng5/gSEh1Oxux4cR94gaX3L1Wgw/7HaO7wzBPk6ComrhX4RiCvwOLkzMLGUBD6JH45EYsFpXzmb7ubkEScRlzPWI55kleZuj/dBzbx730ZxMeaz1+fqJRvawzMgyzHGSH0GdLbuIIy43ndjm6/oj1HUdwELJ7mvAHEroBeCJE2Le1aO+ieXxWUcv7Oyt9ONmZNQhfowWtNiHcEuQhgPZpRriz0t2vl0u5Yk/sdII7iejVvbUuAqgH0X2n+O17MNRLnB3BanGAcgTe55rf+TKOumC4XRrR7GFziDCyJP/31aj7qxo4JI0oZSHz10kpIDD6E0w3C3kUoYGgYJ2qKaqzbhlYxHReNFYMq7BBgS5O/B8Qd/3gp8N5DXptPRXoJPn+DwnjAEQK6MXV+mEQud5qFMrRpRLuq2OHfj1axISdYxkljEgCthZEy+pOSpTYvOf7Q5ee0pCTdIlDhc7iU+iAIFJgAwcWyLbw14hBhWf2JiZts69I/SUpfGSuGqFH/geG3PXSOPUWl9DLl/zk13vdtimerAM+PQkV5p0Zv8rjKBJod1vH2ineBhpBi6WZJLLH2CgHmCvQ2AdHSXQW11K7LnMGbgtnQsBOgLIi80OtjHJMFJsRZubPjFzkVa9wijSd2kLxCaXXIoS8Ah+b6Dwl0ghkV8bDYQSxk24D243Pe7UGgmNKhCOAN0+maE4swSDNvdEOj/CZjFcmKOcIKhvFbalt5BGCI/tnAFzxpbQSJMwvMlQ1rebPOhBTseRuDWaMb1lWZflApv7ZF2YDCuf6fXag5E/LqklM2UPvgfnyYNDp+oJGX8aOpHpDPqAF7lTRPHeCCcv5ufqLjs7/sD5apmftH6SsaLbXZRC2JPIAYplpUfQxjxgH8sSOAGeM82Rp4mM7gz+/4YdPxNhaw9NSw+2nVv4NL8SRpEpbFODIVjk6plw8FOw5uWRezyX3wCBzMaBTyIKINBD8tHIeOiWLOr96EibusZ3XR+eEGGcWi151TV6o1NqR1OnjfshDs51zdZJ4QmdXOBAA5Yx+LPB2WgwnIsyz5TOkFIqBN9ts2sHAXAhtOdt/WB8Og9XSdqFhAF49mmRdbZ5H0bQL1OD+jg/f0gm8UiOxtvRnGttW3rjVDFxG+V+0jAMZYYcBFH5n0qB79KB/Lu57hArmLHQpS0toyfztXCTeRWa1gCsipKPndBdfR2yx8PXtfDVGKEOT7YWnwN39UBwma7Q09ZKIVBubibPe7JE3XXZ85c94DGptxNa0vpLz+aTDSjNmnWfQ/V66mosw7ewDVDjNgOVeLR83BXgTAASeDUCxaTj0hQJ0O3YRK9UA46C/Ce0Upg/yHrYePh/BhnZ81lrWSM7GoPGpk2Mj+OXg0qqiV/91Tucw/emG8eA/Z8pQkiStu2SgSmbvm8V/BbQXmsqYb1MgTuVoS7SR/3pB8+N8KE+CCvVrPMrGQEyhXgKIgXf63GZrxQCFfC8E1FROSnENu3HDJ/lhGdlFvm4LTTZWNMybKw4rkCT1AcRpvY7xPBHf0l4IBGqCygO+J3ohnbvfHIU0jMBWHnVwABwOqIXW43JUJCnNkoVeYuDwYNwV9y7/bAiFgwVAJmC5g4Ato/CCqSb46M3atRQTwZ1qFDRJCgUPDTq6MHEY0OJP5tu1C1ILmE17+1mTDhMoLjTC6vtavdn5YOlDiPkmldxvyPCozABt7yuOeM3EZySELgGx15BTTxjUihJuXkRN8i5hx8AX16bt03LUNZcp+nR991DFIvEVFcrJb1lo44/nkDovdD84X2s8XSkoo9AyBWK7fNssRiWSletkshwE52rRI83I1i67R+guCloEcKguX4MntD5cHCQvlI6WOb4gai6U7Uu9boAcZ5En3HUemaJHq8E/7pONKFmsgyH/gTQGslHmLcxCHvl/v1UqE4NR8betB+A1sa2Re9unGVEIPHhraI92gC4r+964azVfXjqItTf6cyBpu+Z8xrptkWUs0Sz14ctUCxf9phhn4vk+0kDG7Qxg8PerSktnnjO1Fh59yp03s/BTXoxrVfL1YYLOnzV6dnp6Fz2hAjpdzLREq99aKIy9+PUvveYcn/70NSD+eJVHYVPAwaxRkw02C9eU9A5xuYmzIL5QvgVcNCBh0Z1xklZvgWezGCTsgFyi/SPDVtBQ+IxBwo4ubMK8IGxhZwvK+6y/YaP8yrb83ENOjmSuR9KiW54N+VPES
        - #2:
          - type: tool-call
          - toolCallId: Ai9QKWuMjgMaQvZs
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Rationale: Set positive diplomatic modifiers with The Shoshone to encourage our staff to accept peace and make it easier to end the war, as we are fighting a costly multi-front conflict.
            - Private: 50
            - Public: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: pNHIz3fCTRo3U1HO
          - toolName: set-relationship
          - input:
            - TargetID: 7
            - Rationale: Set positive diplomatic modifiers with Morocco to facilitate peace negotiations, as Morocco is heavily attacking our city of Vancouver and threatening our survival.
            - Public: 50
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: tj2w9EYmSTZJiSgZ
          - toolName: set-relationship
          - input:
            - Public: 50
            - Private: 50
            - TargetID: 1
            - Rationale: Set positive diplomatic modifiers with Polynesia to encourage a peace treaty, helping us secure our naval sectors and preserve our fleet.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 017RakqiT2GRVuHh
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Culture: 60
              - Gold: 80
            - Rationale: We are increasing the Gold flavor to 80 to combat our budget deficit (-30 GPT) and prevent bankruptcy from plundered trade routes. We are increasing the Culture flavor to 60 to boost our cultural defense against India, who is extremely close to a Cultural Victory and already dominant/influential over almost all civilizations.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: MVqpslSpxmUmfUpy
          - toolName: set-policy
          - input:
            - Rationale: Maintain Enlightenment as the next policy to obtain a free technology and happiness, which will accelerate our progress toward Satellites and the Science victory.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: YcplQrZE6aBMIGKR
          - toolName: set-research
          - input:
            - Rationale: Maintain Satellites as the next technology to unlock the Apollo Program and launch our Science victory spaceship parts.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Ck8o320H9cHWN4L9
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/fVpcQ5dIqS9we1kd6dbOJgcrgcdZ7UAkgK/TkWFQBzB81uV2ZelepnCiSMWWR0KZCsTTk6XmVMYEFYi+2f48dvDxxywFqnhDcjv9VMSX37z3dZKXHrEmKo/0czA1RFbk7B3E+cR8pW0vShCwsoOBdvhIlxPlY85nRJJvnGc9EyotzLmGLSB973ZERTt6KlthT11a0LFAlsObjzef4bJjL0Nl3Dwh2410TWY7pa9Blrm3sVn4B67SEgGssec4B1cojgr4jjYJ9Zo80CkrqEWpKhG7OgWKMtQV1pimYR0Fr9Ul+iVavIhj7rm5dj7vpwD0jt/ovI/yhBh+MkKPO7l7c4d/zsRa5KnxPVR2Z/MMRSTFT2HJQzD2elj50xUFIv3aBTgoJ5J1Fvv2mWC+oSsZUZf7TEvpBGgjYpkgiARFYtJXy6qvuSwiH9N/e2CiAgYQ2h3AUPToUaceCmytS6rL+VO2Unn/Du+z3YAnJeGh6nRnPLLKuFxwaNj/5RGAOJXd0j2DQLQlXJUe1oGmUBWQtH7Tiy8DlDvqNukqu5V+FzgZIOa5Ovh2Lwe/Etlh1Rq9pmKxL+GAf8/M+ROYfeBb33pWHfzJXYUO1HDXO5pGxyOlzJPNmp3vV0AO/uXzDoQAbuMPmIewQ/7HyRQqDpUeRiHR2m53XtSRlpPsm5+mgDGz2DmIfXcIp1AFNz7kKu0Fd8IUwoaKFDYwct13EnWgAMvJxnAe4yK3uIMIbIYsWR2nsIm2EMDbn2F8TGYppusVkM58kwADPGEhmE/89VqdfkAUBqLH9OhQ/DflKrJZpB/jZTpCOaHWcWUpRYM/l5Uali1k3kUh5JNCJasj1V9SRgKCvYB6/T+caN3Tqs8GDqLTBc5vJNjISBy0WJcDK34SVoYMxHAuln80axFMl6bNJeyP41NxeH6lfms0/fCM/z+Vyv5/tzFDwL1TVBPmwb8294h6rq8E81GkuGU0tP6YlFuIPCH2s0t95BL/CsSTvycJu84OvA143WniQJrk4gZ9NSZbSh2GrfNASNvB76phSiy+uY0MuV6DnoTPNf2+ZL6UXQKgqUp+X9G+GlF3ZPxcPROzxeIzmuQeORS7vWbfU2/ME5seI7tx/xn42c+YYCPmGOf7Fszl90jp67YRakoQP9Bp6ax7Pge/Roruk8ei5qhhYqKskEtfMEZsQZihgyUNDmSzblnfcMhv/l+4q1b7XQfBIkEgaD4eBivxBLkEkkwllUi6ivxDrpSgG3z0MJ82TUWw6MSXoRVOFYGgdXgmbB5Tce11RkFQjmTQ5yarGxrMe6aGdLgXhpoTq26WbwlSyjUN8pk88IKO1U/27x3zOCAq0s+iR6z8iFKS9pvIb1dy1OVP4LVtPNjBRBce78XlYs1nld9LfpVCcjjfikNWRRRV4eVZdJV79UVUIb3pbaLAODKJ8yzriVOL8UPH5SthWrs1kvUuJvhcR/XWybd+EyDHRNHGW9Lu1FO7ZqrDZYxoVLNflPDpPWNK2cWTaweb5c0VUyv8bcoZr6h4MT+JD7lqiYYQo+YdtEKsP5zOPHm2lR3z+mXA9l6GqbmhVQ1w6UXoAP5ME2LidI6SURoRRWtcPL21NXxwZHz5h/rDEp1pkMYngBXpfTap6bW+9WkYR4REUe0j/R/gYWRjPVgP4iwesZQRW5xOsGW1+Et02WMUOQ0pEuC31JJRbpoISp+LJQnkUrBhpnN7hGCeZw0ROeYbnTDiMzBqgaz5HC81BVoNSjc8cJloIxhlry9ZpFcR9W7Cb5yomj01stxXm3Qru2wBWs20KkqAwpR/boOvNqJ8XTD1QDdS6Gxs7uMArechnCqQtzjHcLGyQfte54l6bSwdl2XtQNKp5+WPofz6Mppx46MnuZyy0GrP3Hl4JkkxNFY4Pw5H3Z3og1OfAk6xyDv4+Iuacqlj8WYCLre8lA4y353fDRw0QQ9kN7SN7Y001NRTqKb2zchNqoSkCc5POaoja7i4wJ6GxOAsDRXqE1UCc5p3yMKYcF63HS9B+XVcQDpkarz1C0/YCmZNQW5QfPwk2bdV/JM7mjbxKgv/ZSoTNCe0fDhjsQmIMAx0bZn7NIjGFhe58yMgaoc15ixIUZq44rsEpRHIc1jpwzCdocCo4/TtgQ8M2uKjpM5zOm0asezc1EghGTA6/XAuvflYih9aEVPFCh9zw1LVBrk7lwPizKupNTQk/odtJVX4EGl7CspCX/wKirtS79wLAJxyKHlCA3lZLw6Aqt5nOTtUiqsKDdHVl4oK8bLQaeLEmp470fOTU3O1qivphuBWBkBUcKZpvfuvYpxKS04o9gMwzmXqDq8lsxHtHZ5T9TCchT2IRkmrrPJaiE3xF4lcKVcdB3fWPrbAPCyfazRo1ob9LyFa16pL2dEazKpji9TCAM4kAK6a8aPQ+xlNf0RX+9X/0HDoUcETXE1ADk1t846iDfCkTPdmISkOJBSF66fvVwgKQ/i6tdhd+gdwu5/2vVdPXs5v6zTW+oqjEVXw1ubVANmeCU9RdbyQmM9RJQIWf3JReM3AEmag2Jr89JKHNyfoQyXhc82uz6jDUMCLopz3B77S3+d9rVx/LHbCVqJBjDr7gs7vekeMu/YQnqZzxwbtae6lyu1CrQXD9zeZ29gEqJ6o+dpYdlYpQQPUkvE+UROMnruXbd1SpJuvv+70S+r/PCOLWowOLv0YGEyflTK4oNCN658gulcRPHxNzgrd0q7P1pQS7A50lEvdrp5vNwazSmvLiC5gDwOerCNLV4YrZadWXciuuQNwjCVfeDjyVUpmbEZE4mfYMr/7vt2mbWDSHkSxhXMH6EaSZbuiOScUqWu3vdCcbyZsh98XTC4h4RwY4ShAboiLD8g71axudmT8a0qK/L7TXjJKNLNvyyIWQ2N+CE6XKPy8vo1seLKkxSgNXDe+jrZ8ZgW91WjSJuv8Xkeeg6zbFETl2d64MuREtxL5Wr70SCs+oJYiO3pRUEZqbZvbowTB4EWFUuNMLPAOPowPzqgIVZhVLQV7yU1jlRRzvAEq2C4KUgF6s+VToYIOy6CLM9zSdaKg/Qx3yFkLm5+ALnS2VRUQr2O7DcPR0C/+5ub8ZAO/LHtWPXiTBO+jEEVSgZwFNz5Z7hn8ofuiOUfZIEiAwqKVqH4ol/04fLOZja7dbGHQWs5o3RX+kFoRt5yetxYyoWZACsB4jo/dGoO6viVBF+jxHBubtGMMcBPFs7PpQ4qysUHd8pUEtqtagYy+Q0tcIXlBC9j0UNPP83f8/NDWLRX2qj/fgjy9XelWWxyKXNFx3mza+YfhGkewb+ZaMUaCrb76tWD/fVkRqYxzR3FvQcZEJt20n5eJQkcVFkraCr2spDBJvcoF8QpiRnxMczA6OkeuZo4vOafeTr2OgIpGwIKjzYlyb3l2RSua3S2oqabXoAHYmDS661UUKtFgCe86eqgAsiCC7IBHp53PmIR+muv2ATr5lUS695nHPm93BTEKaIqu5+G4h8Il9SEt8ZBgkmJCaNff1pQVHzPxS9IpAV6LGa6AMiUpFU18C9Y444e73eXGSP1Vh5s+06zPIal8CN+nTQM9zqdC030vjgtCzOTJqI09+J5X83YiGK7dC22KM8G0e0nbziP1C2hno7/5BZG/c26PvtFSPwcAh2QQrSU91cblq9h7Pv1gsyqOM5SgZ4B6SbyvwZ8xn1pZIX1dVJEnon39+Uvz4ym2H3EcMN22VRzsdkwjv8f9fCujJjorptFHJnABFg9fMvEkddoNl/q46gQ+K/h3H07kZgEw6N+R6ddWkfyKYglej+LudEwXKqMuKfIrKT5jrGVdE7gPtiJMuk90oRo9Hf9Q+8xfLcgjrQVdBZhfAthCaped57BMmd+LSvCDZiXSsTTHaejhvIJwdC2s/NaEtflzqgN7/deRmxg6Rc+dDRxm91SWXpkhO/7qx+WQlzqkHkxbJuREAam1j3WXAw1bqoaVKvngZVyZM/Rh66RPriOuGteAAVLE6vw8VJzmBK1dJ6lsAbRXwD+9VHbiFVuQ0ZmqIpJOlL31S3Q8eMuRsANJNWvOfRr6/qvs576OteZLSu7KTL9UZO0GdcS426I2sNvX6iWt8ei3i+6JFb4m7OAC+vwI6dOJG4rW0mf6pG75/mNutH4lEZ2ybAlMNIQrn/OJUfOUpBJfvm2GXuNF6BZUp2Nnm5dEkBsCl6mKgYOrynTmWaoEs+LydwLhG5VErzqIgR9bC42SyXdj+vHnAO9m/3VqjNa8yj5qv84mEAOkMUMBVLty0YokiiYtl2vr87Zxc8qe2h4teVS4lUzS9rmne8qj3UY7/XJw8RD8QS6vrMFb8fBDJ39krumq9dcEg7nvplGxeC2nucsyKmss/ttxPVu4b5MEy8Idv2YVkcbtpCeRMbH8g2npIa6GhBcyjUq84zV7Nkzig87zn+MWnS09JqDSWZ4K8zMradbi+iQ5ei9JR2hHIweUqNAtuJw8FHrwJDl90h/KhfXocbW9hoq1ZKmjAFm9hOfYg3jcUOocp/GN37MFIkatsbIMgrUguPS1TQD/Uiw56Jd5RYhkzmrIkZ//ynHYLj11XI235NlLRtowzeS3ejrqpfVrdfawwvaLyB/Pv+99LDJBMgZ9acazDbciGXFmvqvhej0DRepwpvKKnFAwboO3T0t8GrpRf7iarFwQCoWCbEs2nBZMhebjsRnCBI/zJeV/JwRp4iQe+4OpTeSw8kS92lSEkOkxPR8+OdkeE62hOAb+7wcqqt3dGqMI906ggOlwmRaJmbYFvBLIf9n+n+IaFmK7ZfIyMqClMX8AsSkZ6s7KWzwOq03ZHpeZakHlsRGehBAUomKOwxS4J6hIvu6kLySIW5ppw15oC4rG2+qlufBfdsa+b/qtTtg+5fH94yopOs3JleVk6FEJdFYeX/zaxFQPUYDD4WQb2P3/lGDQVtFf47CjlQUvLOq/yfyBvbHQXwY1aYBhmvy5XO7GlKIzywVzsLaHK53zi1WudW6IxGbBLQfSz/3sNZv8+ROwfvdZKOtOEXpnqSOWqZeCcgNHCOU00uHaYjTDqUAj/+fQOo0w/dx9ABThfO79JZktuztH5EOuUGTKbV2S4SSXkduMG4ye1JuuisY0BELUhGecK0CU+3bz/vnCczpG8dCJDxKInMEKQ/Eu5ms25UyI3kDLtlWhM3Ci74EiYB7hAsuiYiAMekDK0fgbcjVufjrWQbsuNjfa9UD4S7o83FIOepVXlDTs92bhn8hO6kQssVZkDkistGDdmeNqG6Fkc2EufXOieLBlJY+gS7sO7BrKwn/H7jECFcdByw0uLNADvlL8u5+z1F9D7VtTx7mLusdY1N1f7SdBLnyrQktB9cwWjLHIwv5s9o0nGf3VM29OTyTDaUefcKnxuLh/Z2CCQM7cOU/+ajUxTr1D65cBAp/oaEqKcpjzDN9klY5S9pyk3Qs6g9wulOR+J1fOMVefEdfvrxLaBSvABrwxu4qCKLg4w2RxQTfmL1Ojsn8UjP4vnTqK0vhof1rQ5tTExyd3oKhEQuTN7mtiVhBOnmzaM39Nj6DxCjobnsDbmlR5i3qrWCYe5x/V/a7K503kiiuROG+33QF+ZeP1ywI7OPpdpjjl7jWXVTQnP34nkBlUVvcphJPlZUjFEzUItfQzBUTyUbSmlBWYdbXmajCdjFGXVR7Jp6nffm/rXnvNAxm/zcdaHz22FcqVoDppktuaUdCbsOvhQ1XsusXfNaPTvhnR7IBY9u0i9R6Au9n/oBJR09esgo9lWjoBikOi5SR9bveNHMiJCWpzFLI3dkgJhN80BKSeJjlYYBukId5/nomqsqNCAInksJCP93VnOJpQIhqyJ22krgLDybtCJQCHZ/kyWd9+FSd4j2e+l/pO70xdjfoEOxJ6K6tZZW013cL2tX99xFVC6pyzhG3pSVK1Q63wgOSS58HxwJJNbbUD//Oms2TLAhHC5+USi6SaAuEqFIgRLQOI6/VbwS2O7VVJvHqvIopfnoD6XmCgZvbTVpqRc+ayIEJ29BB1te9KP7K42jWHgo+YY8x3z0jsh8LufkuLZDe1Xwl8DccmdFl+yxBhhakw6HiYeJY2ZZsgD7t65DsjFxJUZfY+E+XBB5xRPeN7L9763QrTLzoepYHv9Gr7S9Pbt8kATQvVwKCYiAioXjdPaFPP1o4eC99FKh5pdAJKV8iYu1R8mr70cCWJg4DAtBBSRFfqY8j2p5ypu0WXFUdElCyVqBYuYB654pl0dwkVkuD2eygn2bc01BPmCnHZEVb4Fgd3TpMe0d+XlYyuN0vtSty2FqMtXWOh8A4LMsPOaSUZD7BryWe0apxom9g3Hs63IrO1Gj2xipaWqo1p0Xl6uOYQIrnjlg8PkxFFvMidvd/BMu5v21VTB87hFbqXeWworfS6pP5bSQEfMGfwHQuvW5XoiFKLZrbRWI3X251YlgpaM/vyL9LiPyOru3Y0dpw6EedVrTiIsRUZTTRtyZ0Qf1Y+xFtLeXdtDObAF3wICCvfNMXcjvh7t1IIxquM2VFb6lWAdWwmCYBqqNUDWsZUA08XBqYQiRUpuHwZv5Y8A6g5y2hQgjbW+POkSpytwzl3lZYtTZhPYQ0lkE1UFTqlmzdRNRlAZgV5WsctNC9dSHAdhoapAwsqz9ZC2ZGi0KSnMFmZ9xPs/qFm2auNm8n9w9g7dH0weJ8N64uzPVFYTmJWyE+mKjLQ8r5m/0jeO/MV25zJAzAH9clKIutkgSQ9ZkcoBn+50BL0tc9lkF6d5n1K4CqVsukmtpVFWiFL1IFSQY9b3p3gGC9wp5lWAz8hOBGZCDTnXV6aVL4a7lTH4oG098SnRcNK0eKvyxgjOzoFkGIS8H3WrnxMtrDpZ3h7kh++xBc8QYWosVEUbL1o/d5VFZUrwdndMO5iFyI8dmEJAceuFXfoC8P4h+8YdN94Yb9Hn3AiTdNKuBpK6Q3K9zBf+ZlzHFDlnu8g+vSFgfZ7jRGRNRRVadP86uHlnbXMZ/JWRfgDv9BJkypC29tmBpT51uVYe5SGOX0ndGdZc9KrlIETPay2ovUwcsSP0O/J7lGZf0pwJ34dkOxPai81q9CK/kXibp9SaGbiuhDLEk5yOMKUIhSwziUGORuiaXYwaXQ0hAxVA0lbNoTcPGQxAF5RfpCdPoIz5pO+ksHfxwBtpMKgu8N10MgE8RvzRjW9HXOgHbnE3WheetixJQxKiJVoyPLrvftc3qHplWbikyauWC09An44+CDGIjGr7RA2fhbvKpF5DR83SVKZYJrN0P/SbkeFP7yaETTDuhjfuJgVpcs4cBMr5JX5v2ium194jSlH0Wb7ZFnFmsI0qNRAUM7k4WWp5BLkiUSYGU182B3ttoozL2xezmYAMgJNmVP8GiBH1Tj5oacQl+qfgTSE790M9Bp/WREC433pum0DyimG7fTjrI8+YahhykEQeiL24g5Ls630V0vrfmrybX7qSpkrCo16++4uCFVbTF0HoVqpMKHC5svFpQBDTj+fKd++pr0cq7I1gyxLUniUZQS5vUrtBQ+Gh9+I8OdOrK3finePRVrgso6gzEdZc6vynP7OM+Zc1MGEJ7frZaZR+Tdmrpjs92li5RPwLnm+Wx1s6+f1jJIytAW9k6nZoJx7wsI4NatqFWEFcwhAZAceoh8aaN9rY7BfBO9GonJ0fvHu0D0Y2O0i0aG5QzLp5D1QuEDzKdH0JqM9RlO/T45IPfz9WQySn1VYFcT7dkLIX9TzV7ynaDveHGrjmXpyzJxrukbfI0IVsIDiXSnqip3QUUEIUnXAwDN4x+n/aOP4IcxTI0KNcCGmcCvjwIqRFD4G+t/gyYHIwNx9b14Xie/KxpDp1I9CX/2jy6x3GLsH2uGMmRuMQQx2HswS9J8X1dmuVogbilAUhPxqHyE84kgl1lfLVqpDnX5Wcm8wMJKKduSXjwZAEl2AEYfCbjsCvKttDpH/28f8SATlKk4VaDQ3Uv8I48JSRJdB4FDfpH4hoUYFcV/bMPxhaNQJ66anDY4T1h7NnhpsPx28WQI2yurzKx/SnNuDRj5t0GqZWt+vLOEm6AA/ktv7RT9Stvvd6DEqqRyGJTlYinY1KvUOx1jjfEjZ2mi0jznVLaH+wC5QZ66r1Rgq8suv5ojj5gvnLUwlqgAgIHXXehjSQplgcakKyvXwBooEU9RVQADTcVG+xB9W3rNCVi/yNan1TcKg6qVmYjK/ZFrHofnOBroxhrieygm4orGGY56Lp5t/r0F7b+dHtrCjhPBeRoORUvcJIYQF1KHm64CUPnQ45q+tElY0ueKtVr6OImAQQYETvx1ONKhlQPhGACFgzKvI8dBMffKX0DOWYYkZezXqXS40fEGddOjHAM3wg8bwzQCN7Uxg7wtKR1KzBLYiDeJhBlWguYjpwb4RdA6Uh/4rySl6f/vhgVEAqUmU+PXjRalwEJ43zd564+MbSOOILzuxoRblzuI2ZMxivW/i/xEw7UOAflRQn0GyPkiZpru8qlj7yjbw6lpkoZH/ltUB0+04tuOMp1ExUKIKJWRq33KEBZS9FA3gSLcl8megwkIAPVs3pj6xPHXb+hCSfM7KHEWzlcWm7HU/wUQ+TtiwJ2L1GbEKu6NcFq8mHDkvRyS/48S9z//SA4G8xOj4oEe0uzedRkh88/Ju0uBQR676r6gFdtPy4cGQYcr2C69dmRSoPKMroeQs/O77fjMedqueRp2jPR96x0/67bIvTOsrIRc0LwHsGOLS56RxFGzIhfQGliOOltrxVydC9qpJr2Tsq2Vn9/lE+MoE5EdduTnR1cqxzfXTiw/OW+U+8VQxp1D/O/wJCmpk76sMJxyOQ6PexmHNzoMkWFQNaHXrX/zKx+i6LBMV73qZ8lB96K4+yqIyIEFisKccbz4hQmy1DLKuPguRPqpFv+zdkjoXI39oLFWhcweDM7smg2wlt7yjTGLFBDBOraR5KTz4riyejvsL4KZt5jiJwBUT3f0oqA4ofay7UrNAgccIAQlT+GrJ6hoItx8dhhKcz97uu54N0ap4hsxhbHDduGjLgByGPQhTDjB5OEJvk2xgeJcNi7g48wsbHOWg1Kjn+RfSaxlqaL/OFt4R3xX7eG/dr5+UMWzD8rBuLsU/jVQwxoWLFm04rl8BWC5qCwGclsEgejapub/i8e4QVLyaL8fTiz1aKtMRIAYL9mbKbK2htuMGRpgQiX4Y4exuVWYWnJuxzO3x1S5THX9BWVf9bIDy78fZW5oZ0DDf75JGBtTXZwea6WFWgjxpmyNoEiTcja2YKITBS1i2v18pATJDoRSV/yvgCRmlCXSCd7OD1+w4r8T4YAq63nuw6Q65h6KrGDsJxTCGHiEYccJyYymRPZmRNsbqJqszChgNgGNCj/YqA4we3bideAyrnamCtpaYiAAFWPf4gD/c0MGL39K/QAfekxT2Noz+7sFYZXLPBsZjvgH+YWQVNqszaANyRsI5Dqkqc6OHdweBty25Yl8R/D1qvNZdzPa81YH4psttz0/PkMBkWAqdbLKlkKM/E4UOc6I6vCcU7Puj9BPmL9PryVmuBQLIM9rTyRD638Lk51jffPUg12TBL3B7WmvrsBDpIQ2DTc/NxUywHiPY6DCyGnLqImVFXFCfppgywo/OqDGl9o/QIdgbvmoLRjDnNsv0hPjsH3j86/U//NWN/3rRAKM44nQxlZvV2Sl24Uw/jq6Rc/GauJTIyajy7fHGPvMaKtoRFskrab+10nr6qTYNzxa9HOG6S6193u2qz15mBXdSJtc2oIRldhaSWTryurMDDGrKRou3Uoeuvk8X+GWzf0EPpVe/aEvnJlwBMf3XXUBdKXpJbwDM1v29nVAbM4516uVC3fwNX9f8Zw6EZJTNMQBHN4qjFfEsmmYG1jo8SNVk0w/N+KJJh6wUozqmEwg2Qb2WxpJKURBSeOw//sMF5oYve6v7I0kieu+HVuFiv41l5WXT7l5WkGHglnzhsipWm3O7HPB+exFmVZaZ/0kNpbNe3UVZlyMwiMzLukTELwB/IkkRbYUO0wla4ITWSltxFzajqrNtOG6a8urDKmOhid1Kvu4AjV6MlQmyJ7S1lRFZ3jKr5uFvlyTVJFMkSZhgyO16Irk2RBuinuVd0qs+UhX8iUXUaXK9M+gP5CH3k9/zpd+97KRgwRmwgP5eLVcUcVxAA/1dkQ/Dr6uRmdbpfSTIbg0lPhUU4QGcCCv+7PE3z1zaPSIyd4r4Wr2RxO96G4+joG79BuiadrCZ4kllCwCkSAX+6BLKFGbTsuUfKjloqGeGDxzlg3+dKXXgwDh5AEqw3hHGMMHm3O3hM6tkjtUdUchRn40MqaRGQZ6eNze+RFJHzYRRmXBjVIhbatZq0ipEbpaDXNeetM7M6mQ2v+qNwn8ySweUFnkLkAMOQ85N5hdeIZK7E9g3m7cbZCIQBSHZlPc2zPmkrPP8zpkx+6Yaupmx9W102Dz1a1zTUdy+Gn46ry+7bmxWP965O9eGnwJU0MvVK8dyPO9CmwwHGgxzNteKNKee/z7e+hAwwIcZCzwo+OovK2L2xUZNAsyDzufzGaFr2bcHIbxX2EZmhz/iuNQn7LGynDgm2wEfyAIAfPaVjF/FJKHj4O5rvlVcf4GszCwHGTl8qz65FyrvPZ3w9FjgoWAmnYHMJbtdxZFlgqUjHNmIuVXJe6E3z7fwLVAHj0W++reqhB7u9mmjI2/IBar8MkG3+K5IgaTm6C0ncrKNjVlzs+xX8bO8UDW4aqLZanhkiSjfAZ/Ijw/NqMTnmF6BkkRIfbQXG0PDPm/E7DLQRGBlDLrzsPafEx7856ED8GhXGsFGVUvrmlwbR+DFI1cA1wVfp4A/qKGtXWbl+HM+cDRYjd9iSibyv1C5m6GYu3o4/QJsj6tfK292otvmnV9XPRsCdx6mLe/TZLqtEZkBkKsqV4whoL7dc3Da7t6vqD7aRlKmFXp+lyDL8PfHNyw77jDK1GedLV57yGUKSeFrAzD8GDOdHqzYzpebrdGZXO6W12MVux42yLtO3r0TGE5YVWiyQ/psVG/hUvkq5gstTxx3ILyJCJNaUc8+TNycr0E6aXZpLVWew2j0Mn1ljxJTthpC9UrD/46Q4sUZdSVIaRc3TtMn/ipIA/xLtdUTz5Eg6VhCh8+2oyWZAih8SRxSmH4CFgRRdJfZTZguGInoI0JvO+0YZxXf4iZE2JmiYcVHbVJy5rRwxhXHLO9y6hnFg8J7LvHcHMEpakSG5Ov4iaFPTY/uNVPCUck9KJibUiLW6Wl8ueccM80gVA9uDtJGeNeayQs0xLZUbX9A2WQrf6hdrP3g32hUVhwcoFe7MxQA3jcRTSoFvWIDxd7GwQ8fFPHBb8i2GMjDBOAXsu9z0W+ZKrTBkCwbMYkux3g0vLWAzNHwL4xRWMdg45tTgCeoll0tNWon1srldlHPWXhfSN7EoZ/lFeBkRLrc2nFRC27CraDvBK8rsW4px1fQK7evBdH/eFEQ2cn5n+u9rF9Z3TL5wSFOZpYgyVNXnjwftlHxHIc0LWSsBUDBFs1PKfWe1+E3dmxgMl11wg4myjB/RfLQVIwM5z4ju2iCn5iFj5kLocvY0Pd3ih+zMIT08xW36CyFX0Zn/FRAfGMkYYIladBhTbDxcMJTmItf0T9jP+E2mulg6BmRe/wQ6Uln/55i9GA4WetQ57GGQMewRsFJsF3RttKBewafn6N/L05KFSKdbQl9/gHikcfwQeEx5xVsWshcwkIDk5fr38BN7HKle/sdTqLm6rILV7JxkIgMAwl6IsKj1Ayb9dprmoGYWWA+tr1z+9bzBAPfqJajw1A8Ao8Zm6PkwM6mjE6qSUZXOLosXeEcCuFAwCa3x4suGv4asNY2KKkUTr02lRnwKvqjL8WNTUZ0xFWvAPBGb7RkcFUCrNoyU9U3+t3pcoQg1x2FOVa2EM3ZmPcaQgGCjUVKf0dd+jdlKWkC7jWvkbsioyHuonv1/qxQdwInyykJb+/NyH8UYDRDB2lxrwc0eSrjcx5ynrAz0uxBCLaRQfFGzY4mcbZP3MRefI0wteqtJrqSJ3aTJmFbOHP6xyjGaK0NvFacWVaOf1g6IaIOK82Dhu/AaaxzV1xLEungjQncdLZKjtK/m3wXIXvRdEeMe08PWINO26ZbK0MOZuewXf8gzpscOB9oqnPHaK+iZHqOywccjoN0ss583mFiVyRJRS7kPxtCQ6StBxU++Gsm2vTPKMLd7867jjJNjhiQeN57zz0Hv9vqKxIvWLP1Ys48d1x8e75+tOXSlKEg/XCTaunNp/QquZHYKfvZuHpLjXPLfUCmOpBvfdF22x+ZEEsQ7aKcPAwdyM/LLHrjlxfHuafD3Rnz1uItcsnwmWYTdV2NmXF8i/9kleQldIzW39KH1tNpIuuY/uL/QOqh1MtG6N9XwoWm8QNOLZ9o6T2JNw3S3cWatL12vIfdg/V8S2PVlC6T3dLxR/qjAxlIa2l+4wObF4RdCTdbzWT3EU4hDzVa57co2zrLF25pKnu9nUszjO6NRd5C0QZe2d+kEd8jpnbJJ4LBN3rQi8tclBCFlEcYMRRm6EzGmZDcW/s4R3nffYs4colV0PXIcNQAgiMcCtl5xTsYzq7yyEQ8nnbOGfGmpqBEJGrRJr+Js6FchynQ68pg5mjC7g/spxYAQreVNA8ZH+TUxAz9Uz665lSIkTXO2JcLrFb1T1LnpMmMdUPYWsR3h2WlUJjtztX/Rhfp7QsOL1p8FT7JbqxRKM0/dZyR0zCvoWiSEkWLV+LoR5M6jScLMBQVR4LHAu7RnfET/rpmbJEamMq4nISPHzKa4or+Hg0m9LyM9WmABZtgriJtQZ95R1Uh7grJ2zkDh2qFaPTBGsPTbwJMTi54AoOvjO8nRJGZK9sPM+rvfn+Cd1gYkq+ny+fUEOu/Z+zOi+sA1ZFVDc2EVqbItQgWR2FfEz9VX5ElSxNzZvaMjC7yukEj3gL/I2NReH/iFS4rWj95jy5+830T7h9Qrv3vaglobVT3yBrRrxl4YVkGF+XFFsRe+e0KvXu/BYhXwgDoYcSDhj1znc2CceX9VcrfFgAVBBc31AsRe/ysBmMUe+X2JjfwEevjFJo1OF5is6vfckqo68h0aTF0vkcFkLRu3Rj1GFtUy420Y/3Tqpon+zVJGISazlnWe7CUoxEiJ4l2fZo9qsTP5/u6wvUknRJTaRWOaDB3u0oHF2JA4FEWsPd7kHX6Tvu1pWdRo6Bhv/pJVZLEcBN3X26suWP8+I4H9D4bDLt5ZC8yilUk1L0mxFYEi9axxc1vtW2WVCXct0dXFoB2spPo6hgMWMI9y8oG9ge4+9gZCNp6eKlBJ32h90FiQzSGMDAZ5FGFdvw2jLI+TqK7e//ruKYCVKoDh7JRIY0Ps5ra66p9iy8+2aFBvGi4Mh1rLipoI3gJ2f1cZm9d5hLB+7qPPxI1PII4APHuIihcLYQYkBo68KDWlLTmr8uoHLoQwTOAGuYd0xqhZv78NUT9Rhggqfc7ByCqQAcffKRxGDMniypuZz2Kh/W48dPboPWmjYMRPx4ywJtO4ttvq6IPXInQUmmi6pl2CB0xwjq/2bcBGEp+yZGBXqri9IGm++xp//GdZzTd9RcCIOTd9AQycuCAnVWgFNjly5+HGhohixfCxYmgHRzEoJVovQQA6FWPL2q1ykduR+2N+XbmFkAhIXblUkw1YUBRlChaXd7BetxCbLVukrE9Tkql3dvKat0AqR1esJvNGvFExuqyFdgZHPM3j4GUC1I0C2EkbDNj12MA0F53cGntQ5IZNm53His17HlzNJ5DzWfFh29hAcVQyT+B3ZmCMJR1KZzG3xngVlcV7Ug6ghffHX6B+1VWWHz5ElPgFbcsoCEyEiAfFpdh4VMC27JzotSBtBlGE5DkA00RRlzhmjc4lAoAs77En6Tu3bTUMruFM9HxOTx6y4XPAkY8CDl/uRWUns9rMWzuDAXBs2pNbCdI59K/lphm6KvUS+UTWN5wmslX1mlVAnGXY30KDdzju16hLmlQCrAS1eSYK9b71xEEo4KTGgoZB0kMp5lIpaMRYv9RzyO/6guVKseIckKsqXqWnvrdLHLyAye/cdIiMTMZwRjeyYBendsI6exmxcAU2eMION/h2z9Ykoy3uDfXi1riFohGQkezaLLnIvcOHioXrL8oUExQIZErOpgQLa6598gHH7kFisHUXXjCkp0XZJzBr7HuKLmdo+G0WTZbTfvvI/pRJEI2Un8XqHkzO9UrjI7WxExoy8AL7J/mFUf/b1wTOo5yOgHp/vg0wQjbKtOA4bmfjxpKredDpYbxGLp5aHqADhUnakHQgJFMLWgs8jH7wZyYSk/c5BoRR1eb/nEqopjitOm6NvdmlokcAMdmYUGuPXw49lrDy4EFEYu4TUXL9FPb0iqwX0Xfew1swi87Eb2saZi9xxj8E+BwTjaFMU2QpbegPbmjISnvX2Lp5phP9GCayV6jI5mEsK+Pj6dZTnLPYY3F9FumfP+hWC0+IVKVOBMzMh+xzd76+YlRB5AZSpY5ZCsMt/vu13k67athVUzJWrrabxePH5XLDPn9zxG86Fd6FcRT82Fme1s3olbOs4mtDhT/qeb1NtkOjlM4DnaXy9cwIZZBT3mZ1lNcc9f4dXZ1l/g+D+xt+Dd6k2CqUYPECRF4YSEFJ8meloN6xwZUBUlVRGGpWuLkTbPRKUMnZhVC3HEpuzGWCXq2lW1+h6YRoTatYweqVU3Jj+0syzWwaBQ0J99A1galaHIzhWssmW7WXUUmHkVmmxq5gibJkfRVOhAZtZZ1hriPMD4hRBoYCL6D3ihMOl4F1/c0MF1Tueig7ApLj2NXFrze5eJH/r3kOVvUZ+L3AUorR5iDtmCdP2LEb9Lvn0hvS2nDxMQHYQnsNkW81KTWJAqM5L5M71xdb2Au2jdvBcCdUtsqlX8MvoWWk7eM6IvgnpnpniYfsmjABsPB9+f72kmlTTpXIq4afKAHhxgjLRuxUIrlqGSNR6mKQFSWeKCnVkp4qaR4PCk1Yj/yW9a41OjyysvSYUCygtu7x0SGB6rVh3yuUJBOEUjNBpmZHATJFOFGtr9/TZ7Tq3SCAxCZCPU+ZZ1HwTNiYP/AsYwK/5EnQTVorPmwyXO3Q/+RsR2/Ej91y/zCVWQLaygEo20kdWmQ9+xdWE2ubcQEcReEpKOmmmNOh1Qa/EXcmUXOLTF7aSSU5pu4olc9KvPl3X1pmq7yM78cjGlHGwkXThLW61sNvHBxZ2eLp82g4DBXJA+OE5/UzFOHcCgaJiy18sAaGGEYw/IwSDW6A1jkD4tELJXULUKgi3K2pn4LQa0Gp2krTwC0mczJDp7cL1ksrV5oX+eLBSF5ES0yahRHDXRepUU33x5TPyKnxOXiVghjRS6DiAdnxvdXBKaPoIn8PzLHRrMX0QQiGEuss+8rVDu0TLuybO8QIMgh8nEkLBj7xVTRb1Lzd1UnCWJ44jaucg4b1lr4MCoyDWQQQxmdZiWOjwjJ7ROWTSYaconL7qCSsU3Uu9XAKfIRv6QeZlY5kg+GIbNmEamdX3NWmr1HtPSgmAMgDQDQgmu7IIAWNOiF0xXkpQkD0DySzMOvur339io003zSbQoGhwggbgq52xxaFFjXdBhlFkpTUAYzkbp0wETu2/7A+ynUv33LYqLin1r9pNI1rKhQStsZU3Q+IM8gRH4MwsWE0x3dbHWLzCGbahXy+CJpnzQGnlpubbZFhnA2U3o/LSLtMpjcWpdMdPniQ5Uo3Y5+S+s/tnmI34TCgbWuR6mstKfKEoNI0zGO/9uo7qU+QSAWVB0aSUpQSbkE7bdYl0uVdW0FsAbWGnG0fmbihZQLVWjMj00rENUXC6IWGZgWNc3ZnpjK6Ohlcmar32iaRhlTA8Zcly4aDcxUn7sXwlcy0Vwe9AvT8KmwwL5TgH5yZVCOcL43aTmesqtAknTHy46Eiad0X0ETP0p37ojwJF1epsZVLtEoLS73oGDMbM7764FR5toOs1eHao+YM5ckOlb+xlR4KEawan9psMf/S3gT7lXAjk0eRsNjwRSYUQZU+wt0TfGAuaaly7zFTsQLwKXGI+KnQNpbaDOF5jxDmuF4olV4bkGDueIVO2YOoGRlzFODqOOQgciwbgdUYEamafHy1yIz3Mo6sGlqvp3myMZz8ZH81fJCjTGiOjd51nYVXHN7WMFDAUE45/pdpsszQMtUcnsZVYIYOp2TO3ExJS6aiuVyDPrHgjE0wKrDxvk5KhzHOkm7CMT/d6rqSOoKucmotyCiL03Nut26zdhdRHqSvlI8lmoKTX9nlPtoF5oJZ5InshevNUYw51p7C+yF8olH3xThqfjsVa5g45meeK3Y6arSbrrXHjBZEBmL3jA/oSsNNSXRC1eZ5JrmffehbJKCyF2um8TIH8cHEzzMTatXauEXneaw8Q2NBekutdWGu8hsci5NYytNpcGifOfm6/F+v7IAzbrT0ZTfIvo9flcIUxWMMAs8QFm94cqRAteI3gXBiJHri9CJ8B2MLCSAzGwS092k33J9Rpbcs8ELDIJP1kitZXtE6KAN6SSGGZo6LJ9dGjGIRV3dnHLylHftENYpMtu6kHDS2gohTzwFandSR8dTT28S2GK1SQgqlvfGdJGnZ2k1e2YImLt2gR35xzxm1bIT6Fy7LQT6vAvJGkThygNqlRn6NwSHH1VgAIsDtg28LqcGik/EHHnNC0/APqvXBvW/l15JSM3uWorCyfIrCeKu3Xy4TNVA8q6w6Wf97MZvABuAqQ89zvVIt2h9C0lYJZkDY2a5vnkUXZgynMS66Og6tL5dmr6v9WLhbj5Ge+x86qrto3IogWDFEyEuN0zvOweQADSNvpbPlRJ16A9Pam3WQ+5gK3EnIzQ2E/XP/BhgXb8qenn6Y6W757QGdOLT6e4CTQQAYR3qoNXKhCYY4v95Bf8Ef+5hahj3mc2hM0F3UZouMaFGrKhHQApibV1FTNl4SeTanZWCu0sT9Gwxg/NHOaKlrt3aLGp8VvyzKzGoEP94fEEhx+VEQm1q56ns6mQ6RS/09RgSO9gS74hCXRcUyLUAAZtQ3VzTPXNNtDNI8I+mMnR6HKS1da2f8Ol1kQ0ZEcStfwsfsONuVj+31YdjZTsXaKhp5ePOGeq4vCwrpTqzntNnsl3wDiBkoFF05M2GqfF3gttgHm1SzJFRWMCpV3Dc99DNFRCqcP0AtLHXRAM4sSw8WfoFnf3e27bDs59tk0WmkOdz8ZvgJX+HW/4zOsABF2Tmk7Pw3SEdCXFPyd9JxFr1Ug4XqvFwpOUVI2VjBko7du13kl/PuOZqGOamqCha9axyFLSLNHBWKUhEtxy/58/A9NsGJq8HfiPrhrRx9fmM6VYnhcKt8DzofdU4LqP0m9K0AEPxgwzJNwDhI46mX+HPetrmpwEE7eMia6zFoasObviGRF8wlz5m/T2Dii+fUYokWtD3epnjZGJ/cNkMBodgxvPL9OJTNhTidBGhMpRMLK3fVzT2z+k5CKqLxOVYeZOPp8NxUnienxz917VrUO45lIjU0s8gyhDonuHGaGW+0sIcP9W3RWDNpr0MpzaKLhDnEIYf+t4xSn0QN27WUYsl4RYLOLw3KEGmMmMroTdgbdc0Ap+Xsv8aYzv6Em4Ag1AzytUkb57vIh+C9OMYyemgUraNJT09fZU8igr8iJ1uQXUymP8lRzxx6hVgIHiIeR68vtHwsxUNbyuFgf2B+hEAYirHpF65rytnRup/U10OBfY8i+F0kalb6sIoBaCp2pSMeKBIExhB9LB1UPIHOABTeEa+1oC63Mls4UucOAa8xpfFoSt7wL0Xy4P7sXnL90V47D2GkfkHCoyaxWSJzBnE8zBQB/zbnCo5Vd/YS4wUxJcxgMM7MfgbT4xaX+w6B0K3os6ObfiolINspMWanYOzqtJuTimMimjILFZjqmzvtu44JeS7AQK4AoNfcUfo5/xr65vmb53jOUPx3jWmPrx5agX1sbFyUcTPneoCmIOUPNI8fxznjtTJt1uoI8VmQ8u+wg9vyhkJE7zlKh1i8A6VL+MnoGQKKgPHf704ixSeo5JuiECSFvpLWS8gdaWc5iyEgjuhi34MlV8AKWAjkiU6lDr6b3mjsOD63Sy2WkgTkZemdo1zcHgbzaUaRjPf6CAX+n7Fkt4RrKmXLWCzhv86u2UmTsvyPERxKc6SfbbQ3DJs3s8vV+ckVyXtv/09dHIvqb7DGilqcRZ1vj06zw/VtJm1baIaBiHE0MkyaK6TpVfLr9fgDao5rA7syJs89W0FadqrCxYE2d8Pdb2s/Z7jKrOzdFp/oxjH/JES73dFbcWoFdQ5sp75l7cGD6SX1ZOkGJsKPAKpGLZYjTVcjmlNPSQ6Ze1nPgwRj3MZ1LWa804VNav0T9YwGIoiMkL5IC0uPM5DwIyXeQyKjjZNjBbEcZ8Y5FJfWT00D12+JjTPgwNtFA4CvSy+foBHnHvBEUteBG+HiYst3BeTQ2bG4vYVCMKxjAg0Aiqj456u2e/vmWvMVW6QXtBvSs2JfkqTy2oC5T5U7WVYdf2uiWYIaYoIoEYTovuDmEkZ34dD7EmVzcyml6TPwwKzjYwyKojrTNqDrDuTDxV5k2ZMz15WFcfTCX2Pap/RECFgXWGrqHbcSLFVdgHWVNZx16/Ba+IO9UtCDAU+jP97lJhJJcM65iPMXMHj/1K3Ht9CJIuTXBjVXh8NWVUeiKhctujXIpoUvvG9tUiJ2/yhq0U8EJ9XXTyaSKH98KeQew6NDg6Qw3DY0x/njUkjIu/ZjHaz0XMhHDPvKwK4uaRPfGDy9qoZZW+MPJjJ47J7xkfATYHx9GDICXPAD0ivHuBDbdgd+qu8J7qaXWfKx5UPEL/R3RkIzwLWwR4Qy4D5cAS3S4vF9Piag7ML5BPjK5WzeQgMkNhWIY6Sy33Xis4YOzh1KrD7bhKjKyq/d6+rxE/cQosPW9IkVDB3ijm9a8lR78fVtvsrajokg+vCNdsxgXQ/bEOV2FbYokHZkfFG9bv6j4an2KcKvtCWTYe6+abLjPInQ0eSj0IIi2GCuM3gePItWj6a9mf9GtWCBu5mZ7qGJKbdndp6E4zddjim82x9q0dyeAWyR1Ls1YgfZ95XeL05M7/bs4bpvILOCcxJIe0DYR/RddX5qmgHqDfHe25fh/6kp4fKMGqdXQgMV+4mjOlwePGTm0CMpoklWIG67DRmAbZtx42ENMPlZ4uef7ZObXY4b1mcAydrIcq/JdX59nXGO93mhPDf34iO+lH7kb6sxV34F+WpVrZWDowxuvKAApIRbOou8ex6PEkNO69880Eq3Uk/x+8PAeYSF7sfxbzT0icl+PjTAlzb7z11cPlsVMocTULR85iWdENi+/k/0OEPXMfGjqISgcpebeBXPfCrE6MsGogLKsj9Oi0AV+SIgHQ7XNbi2SX/OfYOZ43oY/9WBUAtwwD1I3Os2ikBOVqjtpzo7Q5CTkdYF68uuNIwTP5aSYSV1W+gMLGatPJg5G8vNTevBfi2vmqwlJVN4XHViFnVtYqrz7FJS8RBZd1OB03PdX1bCK9rjNgbRkhLZB3VVx2P7yYkTjwjKwbcffO3/4PybxKLq16deMXHZYNxoD4yGsZWJxjo0S0sk+uYhX2wbmm4l+CON9RBOMs2IceuhS/Y3nGay9S6nssPaORJxGdcfjFVjkPn8KQHP8MSiFj8ynvdHQusUdncOL53AR8z1X69Ze88dN1qKR03mgaK8fuGzEbrfL5xzxIEXt4j7asHyZU8ql7DoAQpjmoDSc6F4TcR9oNEbV0sUW/dhMDS4KfsuERMGw3JvJ4edW/8nXUDWC199FhloJBLZCDzJN/pdRbgj8hdwXUPxqeGgyOkH0JfeT/8epOw8L+p5Zj71TXlRjTit6mtl/Sj3KtrNtGh1gq4UQctM+gbsqJ2vzw2gUvpWubfKpN8gDHJvggOBfYBH7mOmO8DIFSKHdu8j6FJ+g+U9nXuaFvVYlIguchYWptFE8FF/LVjBxOs/ylICCj8JGawhTzpthS1tD9QTBcE4UPa9aHj8nVk4Bjg/JPUEsmevh0lpqWeRyCZ3YQ38IZDB+1CF+pVYJKFZvzGLuv7NP7JnZbkshNjYRiPtxZYoZW2DPaPnzh0Ld1FZVajljI9LX1C/+Lt9/yw2mTyY80jiaY/yAwcyFX66LlqARxdaE7LCe2r7S4r64s832rSOor0kYkSePae4g8WBPJk81zYrUqXZ+Lk3mH18BsAgS6/N9j6L6Qca4acJz29PEVUNw7CIjWud6nM8fwamLBiJu2D4psIouv/Q1IVZlDra3/cSNV0+wnX8J2dZe8BDeSNUpOTr0sLiuLJKeGR2trMm1Ua3rSFjI0nMpeuAQnlIqcLIdM1VJbxNADnUREPsxDvlCf3muWbUXdijnBdBz0H+sG/qy/Biik21Mc+7m4H1V4FL2k20n9y7olk+eHR9fTaourFZAq4irGD9pfvMXw/FQvoVdj+SeWNLvG8qi5aorJsvBiaFvi9CtBMRReAhmBTxtSQ/OXOfWj4Z3MT4FmwNfAIdb0UGInF++PbDCRvjmAwUAu4GsMsfdBI3qdSw/UHt6/dEsxtQOQfNSBE5npZoxKRYPq6n22oqgXsstJAmCvCawIK2RDs0HdOc9ppHZbWk36olQB317U814x419eY4rXkac4wTCxsJubsiqvlddl8yfr0p5vY5Vq021O8nXRHE9h1jarO7hXLOHxDV5DQkFe/XBcRjq64VLznUXUMeiwXiBG9pOqQb2qtDgSLNAebmQKYVQjgPs5sAYNPcc/cb7muuptd0qMQLPkUIBhC0DiCdwhJGm5G6qtzWvMZFAkQMWOx7nGubtdpSXXeIRDt4hxBfVH3RALJ/ehaFZtVkWYMGJF1vzHyf1+l/iUykFh6Mnh4CgOByvFD9FsZihfoHNVQkEZgJf7VXiMOzTYmVwjqTKAT1oU8MOgQlhD3SgEg2J48Kc6OOnQ6xhXMQPQjqRoztsrJQxtSSiBnU65MRWR5t7vND9rHKRYJCwXJ1uXdtqtFeIzGSl2rHG9hUMmF8PU9ia9DXE5bRbDt0RJ2dC/38zjcJT2dqLGLVDESsdnuChha2i8GZDEcdYPH8IBOJkOJA7Df3HUEc9s+kwqsLb4R5UBE6mGqEL4eu1o6WJ03Fpji/ZvH0BUnyO5XNEfW1r383mj2pLl/YZfn0r4i/ZgDXllZX7xnPo541zVCHTlvgMuybVjVw3S8h3XJ587q+TQ/GKqNmagSEuion4Am4E3o5dcFkvhyTZSzYeMv8A9zfAloZaMQvM6uxqnRy0SazzNakVkw3kasrjGbr/wwZsfLa4+2iqZgHPbD2qyQSXE01LT3joxMzX30r90Ym5y6X7dXEmflb+vT/foLzBMTgorLVMehsFJrJDaCutjiVXr2gLim5+KbPWR68ZWkcfcblyzSR7rtf1I0C8pop9sxm8H71cAHK6y4G9jTZB0uYQA7OH7YNtwIzPFb2hCjJS/CgrRbxN31wDdlKBXEyitX08lZbZVM3kOqb063dWkS33tYcGrAtiYrFvLJ7UNhrpuyp5PkIV3r5Koxz+qpUkW6C5L1wj36V5DhE8jeHZRGcy98H/uT+7Wl/exWSkgSfph6EdGcw/U8ea7aNJtHgSoHFD/xXb8ZhWYc2FPqjeN4q6+F2RIRrJsYPulo33KfPurUq4m6n/gozpKsuAiWkeMqPTxOHszuZgthSytMZcN73L5XeTBjwmusYUVWXuAPQd34mwCarW84/pZ/sdDC30mC8HClsvX7YC44jSM+OhcE6GcrKv5qn2jxxKnqLxKIGh4whp/+329uXfByZVnP/tx3005rdEx71wNwazNNoPsZ0kq6OMn+AV1HTBm8b9ernSUnQIeTtIL5A/38u6sj1Z7lobi2YDTHmzEGrUfMzBqja3qEpmMgqyGoBnGqj/STnoMT3j66OLZCGHV6BSU+pnCA6etW7lZEFLbNp2GFT5WMUoGSiB8fQd8KFhjd3WIWDldbbiVTfry3llymbtQCWAORCGQ+IBJ2YywFQ3OFaqvHS1viKtsVr3OSlPzb3Bn9F+AWs+7BImILm+Ltb5vLTrLenD+jV127PTTIKzazH35zU97Y/Ysit6sTGzHSCE4vmcROHp4/Cnx6iB9seOEqOFDi5L5maXhKoqjMXPIjoh/yd2nfr/Q+DGbw+ssWJGj52FFSA/amp2vr+SoaRHKVVdrXfvRC5SrlusDjdJU9CN119hdtDIon2cBZ2+x5OSUmzH4pbt+v4RrGKqWvO5WqPQOQZy7H2VYzSUCLCmK+u1qwh1VCsfR/ofm04qzGPI80ljQiZL+2/eLfK6RIJ+aq8wvrwt0autIXDRbM4VXZun6lxnZ1CmfW1MEdZRBiCyAbrHpZUuQcFd3V5yfiizjwefB3NYw2Wtp8EUBvhClJyjxBQEvuAzicWpGERMwuLSVdTQXHli04d42Pn+GaL+W7galfBaSlvvryUTPWsXyrJKRlxpPnAbz6VG/5c3ypC69SXmXzW3kEo54ZAqawaXYFL13ZorHs/jga1e6HAeckEJyBeD0ruwO8LWiyUGbYaR3IGyKFb6EtcSgpHQHJDtFcpRbLGDZx/o7BOtlzLsNmFk6jDmMzmB4iqmZfCBvlU4n6XVPAIHVwaQTBTjHctO1abzwF+Out4DUrONVaoalJ3uppVKXvO4klGfR3YMuKcfK8U9jEj9YGb+ib++CFQgVulu2zR6quYLk+o02oOBdDqfHvEJF0aF8XawxzBcihx/oWZTbIDwfg4GQbG1gFu0vD6szRneGLNaBoYmgK1wp39j2tSPvGSSG4TZHW2DdwwHQZC+DivHdrR23OmsA//PpP1bCBuh+m3hvjUyMom8xKQlKOsFqzx6/BMKxpdcQXlrnHYXFV4q+HuSLlWKqb0erlkaT/4n7hqmkV2Ks41MweE7s1dgyU1Rh49hJzja/hsMToykgPTfa5teUS788SZTDEuVK1dTil3dUegVBu73NEWobyj7kwg2KUx24Q0qog87kDnZgidx3F943QXeGHtYjTU9ABL7E/hSabNWkb9OfXXES5vb3FLNfsqjXC9bD1gO6mjikxUxOExrpTCHecOvlD2/Iov6FZM4lHboppNc6UihDw3wl7Zlw2pCN1W2geZhYOc30SCf6t6GMIkRJs5TbcQb0kZRMU8XH9cbz1mL1Ja6x0xghgdrJQg1cYSV6X53z++3voxhpM1aD0PO4P2SsePZp8/FvcEO7nG3f33v/M6cFskcbZJPUDY2z4iMt+/+/Z3q71NLrNi9aHhHnVI1lNP+n3FYfP+6HB/+tT10AgnDuIM6YiFCbByDj+j8qmOvFmkLfrj6+I05lPaElO3BbSWLPB4ME1C3LoCDBj6biMw5C+2lcKjy4oBgAihqV++EdrQA0nYyRrhm2m2UdYJA/jelq+iFzIoGdnrIN8R3eQOT2MIlgsDSthgkKr/wDLaxwVUqVUambKB60e/FYzKxf2LP1gK9s5q4leqv+4jkGpu1iVdWXjaczSVoIjG+WpW6ay/2qEzi6JVy21aqWkAMoEDMomtCajIwfe/gFOsa1aUao+KjFR3pz182WZJjiES2n30ssO2imdMcjGqsqDgZ1Y9Su4wcL8raLQetufIfT6aCk3Ub5lkLzM4xsXyELq39XD1fxPpgQ1KwgCcmLFue0G51deFc7RcECEbsmYXlDRcXPZGpaSK+EIrOIiyEe+1WzOs1HTn7GS0m0XdGx04LcP/AsjEywFCihGd3CF35AylOQpKutbWsGPJpR6OHmkfQw07d4UixZ+HF+eHQ7/spKRuPt7oH9jaaMXTE3SSlFwsAY6UAJGKF/2nWDLWq9lasBvgA6nBAUmg8xL3+mpm5hU8Nv3TAq5KRCSCAj8q7wzJHs14+xmKjRQ+U3R/6JFjkm2sq/4RuCXkeVxKwN7Rwg5aXn5nciJgvW96vHaPJixWrxFEDIyGjq809mmA8CS3MlI1+akjeBJ2jg0kNvUcZ2XBbSPvp3etGPwdILAN6TZv7psdk7bEEOvAhdBnsRIG10UPQtX7goDdTi6vbqR03N2t0l5ipAYt9/L4tAB/cDsKQtlzMqIHUIgCP78Ksn1wKCxXAKfMJXY0Hl/4Wdg0TBuBfBa2JJz4HY88jjIZDXcqC2Tm0XOTBRlx5ARBm23ztBFxKinfVoZxHtND2flObhuYpQJ0vj0bQJPt0wlsOz4ucW8aewpDkhTZGVHp/usSLLHlsQOf2JrrlTQ3swBjt+OJ1xNYPGE58PeCsbJLLdjTaLe/bGDfgv0fNqsK2hkJUeV+ub9uVy0KMhdcusvUM56adnYok2wCUCU+3t0LGAtY6OQgMGcKBEsgTyB8JZfik0pjShbSEpOb/kuOgV4jyEX/swXQPnP9VbVJCGREmD54pjo+I4ZMMCT+iKP9ZE7NDWqS20BCJ4Vvx920FuADSU2H+YBhpd1jWrA754SjDDx88IxTiLw0Ke7DlzMvN+KWbcI2dlluolUE/rrTgrwL603v81JqCPNSISUXcXwdDtYCOF5QIl+Xk1iPdWPWW2o72mLvLMlkxFSxg7iNN4R2YXw2WEoI9ZBrkU3e7ZucvS5DYjB7lAFoW73SpVNAZKRx+wVT0TLV9M9CRxLB8OAAy5kE5n0IcVSVTMCiccrwbqJwvRGaVLwgO1BfRECIDv1BD5wkXZs9PO/mxkln8m2BHuks6msQ81+Bybffw9HIOQvpYyqAimkZiA0hBbW+96Ad+5T+5FeEF8bjROLCnrVXroOYp00bCYXad4vmL+qFTaCRiVcoQ9W3EUW9SeZgznqOkPSJK4AgTs7sgzi/m6ZEBOfvtkxhPb2tqTdoAq592v8WIgrvXosQwmQAxHsSu0T5AO3HRYVzCfPpNTo6Lpg7T+xPtxyHtJvq7mE5kf+lOWhDBx3krBm0o3fkluDz/BXsJ9uWifhXgj8Uu4oOd6P+vM63r/nIKuh0lkfrDDVSMyE7VoaPdbSn2MqtMeTOrkaOke6sRjUO6yx+1+2EoSSeWN/t6b2WXDQl8UP4Cq48P163ELdAkeeNjsvChUQLNgp3eGXPRy865O3IhPcbNwnkargC47mvhn9JjykZpDUEpLmLfn3dRmcYH2S3vbBqtEl5ngSXk+54KCfEgusk5aHKhXG0UZqcEnTnNLNo2yCsyOwC1i2NuvV0goSm9Z6dxEK/gMgDzEgLEGy+maFVUsEh2JUiEnbL/dBDg9mC6ejPOrlPL+P0cYeaecStP4SCo8v8hRNUq4EdmFfuBrogC8ImjkbRBoNgWfoMYqUR8oney5Fyh3z1gQOBrtV05g0EkWmT7Z9UcMfQooBYrPF7SZ80SAxwUiGuZp0j5DUYOFfnMSSx4qlZd7tmviWkuWU0EjCfOMzu7RdFIeehFEjkVPoEkZnyI+vCO/Gx/BLdTwav9RR2N1kzqEw6BCa7+4JVEaNH3rncs9QhZlCZZRob2J/b/8xfI3eOrrOn0GPxi5a7jvasebDlGn8dVLiTsa0Vx/ul/4cCIuHHT7j5+w7Y19PGieykdCpNLUR+V1okyZ5LmSdILt1q7hKOtN3vZEsxva04ggAOhsUGsRlzimhLSMEAjYrrGLahVBIUd53p9gZ//6qzE87A/BwKFGZ0R2E5Jy+FAkRIA3+RKljjEozKjLKp4TNztztNaJlrEeTbLUgkk9o3vbSbVa35ffqr+A579VPmJ0Yv9WHlTIr8Af9sleMTwlMt6pPOx7kFcjqTz/7P85LOg6rgWEjpZdI2tY2R6Ch11TakJHLzu0f1iIwAsXvMIX7TkYvpzVvrlnZWmY8x4lBvJe7918ldwP40Fs9SZ0H+2Rt5ZONKZGmUxiAtGq9Gxkqk5W1W6euR0G//gWBMzFiPHBIx969ZTVEyAcOEZoOsE6pMMmLpKejBHYpRn+4pqLh5k+Ba9U9WOXHXaafMuI/d4J9e90knO32ikH4vH+NL/0OFHjYEXR7XAySVc3d/Ats1SiDZpO5JnR4yU5WP63hDuCpfDq+xdzTVPKDSknP30+VeqxudK8wy9wP0uGACToqh2pUL9YqBUazujFzsa/I6TY4K5FZGOtsa1SVK/CC3t4fMzCIbzUD9/D7tLNrU2fqo6xC0iWNMLpurT53OLzEoBg4oKRxTsN/kMfxmvKLWsiahJm/D789PlRpiTTuRkIWbiBFqTpxzFt+rjjsmju52qR8A7DUda1LCdrbX8RoiSyovW6GncY6Qh4SXXBH6RUvTmeW2GA2LCQ/l/3gyq0/DEqdHofQctOgOxLF16OdqNuSfL8u7MHdd9kLfwQukVDSnMmA0oPLgmDHfA5m7wq9uxpPdgIwuc94VpkHn/ZsK0sJ2NsZ1JH/RXDBnyK9ha2W0nQFCWnYQCk/Cl3lLIUKdbXTJV+ySH1sttNt/kA7Ju0oZDynW7/ovv0ido/D85t59L/W28mUoDgD4iTqti2SKc6openvYHwlB9O7MWGNYEk+ns9gsjCJkhs/LaKgUCmMRwtW2vTJdMf+dhEqInxcKn+1jVHe5dDdPHijnAtSjUTuY2FoKg9XP03pEvcSpWthHgtropfSlQ+OeZJrxTNoK7MPOtn5imEVZqc4caFrG3rkdhi1AwNYX8fP0Ozds6U7cZ4Dcj6Cm088q5oCO484ClEpL2TOXov9QzW9Fcfsv0/z8g7BaVlv0SSHmSfWIUkYHvBuNxUPD2uUaLiTLKAyGP/SDuhfSExhDXI8cJyjpMESJaMg/RAgFCDMboE1P+PMNKV+hexbZ0j7hnIuN1V0yU6sldPiGkUkeCsdUhA4OHzpHXhirGPkkANK2nzz5RlHPdXIQDIloD6sgxuaw0Ih68XAY02o455YSg0o9HTQPBJ35cKq62G2F39+NH1t2eM//O3rmAxLpWXhtl4HOoM4upnEGf4fhIY4eDQd8eN6FpVavd80uykXQnq2LVUC2bcBPGcgVJcix5FRdvqNndWKPZFtUId9O7Cvna+Jv5NEaUCsEvj2LqpSYPuk6/6ktMmMVL0GTXK+OtWA9cLFjgQ+w8mvENo4CF3wapKNqcicScXDpv5mq/XNA+H7E9tAviEg6rEDpu+QBjMonNh0nLeZ2JWjLr8y2qFxw/BVgicudl1jqiWGPL0mdE10pOZn1AiSulx6WXxkDOOXcjQxmo1KnyftbAzU3/+tl/ZXnnmQ1Pasbk0lkcmupEdaXB5OdzPCnKaXR5CcqcPbTYhmDE/MsQ46GughXl41cgZDpd7tcVettUhU2W3ejlBTZrAhC6YOJfS5+gxGk9mvjGTQmNk5F3+wuH7C+9xzN3LrwzrmqUhLo+lnz8vLNOENXhGc5dnAyIiymFxLhBtoBFbDMkD9uFRy60geQ0uxdLGhB2cgPZdVZDXSAkrDk/2DKH2c1npMaKRwiaQFTccxgSymC0wp/fhcXJom+yMyNVaELzLjDr35SBDZD61fVI59p48D1KGnIK9MPhlC054D/yYRU4dqlhaEFYkRdB66BoxOuHvTgCcy0xaqnm3vNZrTxZ3TFedqqOqPr7LwA1drbCQvhjgspIUSfJXaheX1Wl84hbsVWmkszBi9Hl8NSbFRc741QL5ZThRFaKYkcrl9fOkignmxWUErosx8jAuVGBZILDARD0dTemaEpuDjBz6YCnIYkV8Glgn976TG93FvCmqnurRlaHVPayecyaaYnyfOaz6KohILxzJE5Jphh5INuxsgzXX98fGTlE1EYJmUAtdXfeTkGnBiXJv1G+4SFSEVr8urDtJAbK+ssrXhrTzc5fgMDxwbL+XZSZe5Rk2lV/qvbI+QYasVi90LcTY+SYr4vXevzeZNhoBG0a31zzDsh8Wjh0OAHqDbqzaKO3lnZcevEgX8G75TISICN1vUuC6PCSBbj39/J928w09MB7fwaCDDkTMZg6YcRszRK3ZnsOcjmxIXMNQx5ZXrGmf6Cl66985UfYMb0hDzxnzE/9Zuzjt0JY+cV5StxdzXBr8nBi72eMX4Gvsa7kazcYGI6tKbpc5plCU6Vpbcx5Q3IyP7Vnn/uMzQTFIR6zjvHult1Wt6QaB0mp06lA/ii9Ik60Cf0waFzXHJqVX3MbOAX+wnq91yBv6DsEKB86pEO54qAT1d3cnX2e9yvtdfx/KIPLMn6hb3YwnNkipeFPGvpdQq4KaprhqN1yjN5vVQwR/Y/7cHgbTtoKtZJsIpx5DyA+aiXIWmk/I/273kiDT2rfhrkLsAr9gGva9oqH62gc+D9N6LeVtiWxyIN4KqDStIa9kVrPAskJuymi0e2C27m6VJWDCgnD2ltwSMwvT4WpY1wooXdX3Jg1VOxLna5uzpr5a2fqB0hq0ksB/7rFmCc9+oDH4iiCBTMpR89gcEXychJaru6nEru41t+hqTYCrRzPHPGF5wfTAj5SHCTn0nodMY7sbXvgs01qhsp/ZABMxA9HC7Lwi47nzcVck77nN9IUVTPMnAOC/bWBh0GTfrFfYYmTlfMqEzvuZRPvUPZYZTU+HyZcU4ZOMbDFnIPKfQ27OXEr2UHzkK+tSrk/DtyPL2YdotDw8x5sYYalBiZqidGqB6MGLtpakBnqOmOpA2oLuDYUrk+1Qu/ZQGZ27TKky2apk1VWN6vtizXZPHURP6lThPk+8SN+Vr3k9PoE2IiMZxj/P/+vmkQPTrVZh8kV9K4QZ8awHmfoBr3vlXs1Ku3DdGfzhZEG2EySh1uwfbCvJmRfCyv4ePxFTmudC511eu3hn9lWfI78GEJ05CCUQGsq6D1ZJcWI+lmy0X/XqX5Qp/BIWreGKIsZKG+pcFkecuGy258o5y5hTnHaa2RjMAngpzwKpm1BH6fuePQ5/BY1Qpq3Y/uEfEC8sJtm/zvGXm83+2NBezu0kqHLKPTHuBpw9a5FQb96dtCsVA1FOLzDA/HHIzA/KfP0www9vFlz0nmJXNJva4VTat8GVjJ6mbOlNlvN5VRqt1N6buOlxa4Wn7SbQ+/KftHZAhJbSkk9Yea/qFU70038OxUpdbAz876CUAaWn3KS0rd2/dpjCB/g/b9XCq4M09EynE+uqLKCA3qQzfPdvaUIzwuHRPQSjyMqEl24aigl3porpglUKWaFcxfDL6BP9oDrSMHk/HYIqcBIte9DH8xhMAXdqkDTNw+pSgBEaKM+lI5Ns1f8iUpycrGB7ANbGqM0I1NuIXZZFD4TvTZ3gC98BvFxlU2IKTRIifLxAretHQ8jAjPCij7t24YK3CBFTnXdEPI20PshlmsQB5cNYVL+vRImhWa1WHqnfmf6jPNSPcg2nTf4t7mt5qEpYkpiWlzypkH2xRANwzsRtYEW78NaNLAvg6q6Ha5NATZ+H4lqa1Sh64JXHX86+ZJ29XcKl/G4aqt2m3aiOY+GoP3Q/xyY4oRtH5QOvxJ1THu2cp53B591T6nLO/qDgMRm4YmLqNqpN2zJoqq37koMi/6tlsRWWTYRhEyrOm5ypSxL4lkOQ/jGI3ISCQZetdSe67YRSsUgkEFL3n2o1stHAkdulHFkROGzPoxLiEFyyV03fcU8jVwmchaHQNc5X5ch1UP/Eqva1a488UK0byibw5fYsVGXbFpNt/lBOW6dErTELGpUDK+QThlxhGZIXJj4OGjpB6CE8XzWkrLGFxnqKalnVbGTeGNv/bnhM6QWt8lwO4PtXVLPbnpOHsCbnwYoRoGk3Qn30ECwHOCSp9BJJMSIuP2pwwi4YjwTfqwVAmnWPCPpBKOrXsDLLe+zOZ7uCKZRXNUdu2v5cvLE434c+t/ZWrxuhKNnZBxWc/23q2RRjxye5FBFS6+zsGvsg2crfNkae1zhr9hhYC9atV/pLOo4AfN9IrdMm/UT0Lxe2NpAGUdhK6dIioUX/1FgywlxvdQHkANcv8rzaHWEv9H5B1WlTwKQMdkifq+Bl41eif8B0Ie7dO1QiD+SrteEg9UhkJOOwXTGknpLMfOJs9yr0Fyyt99Hwl7z5WWABWYqRr602L01sNApM4pjD6CYAleYrlPc3Hn4noIbYigOvmw6st/wRuCB4Ml/uIGXX+4WhVFiSgLnMJBrNZ6mZRAuM/nx4BVgny4mvcQv4lEoEkJ5fElmxtuSDg6AQ29kukbAS1y7QhgE7sCeAv7/rFXnwpAfusIhywrlB1UgorISYVDgMFH36L4+s3UMDum+9LQ+/HtcdV+pumu4/ELnx26Z9JzkP7Z9vO+qt12gKWhtSzXOohvkbUeNET36yW2ah5fMnm306efUV2BAcEeN1AAV0OLpSL9bjBxJRAT3mhPNrsSgn8hBRsXm4NJP3cbAEoE3ysn7AXtvtjwe8UOXOmWlpohzkfEKEq1kE6/b6AeAwxC9HqcD0PPvddGlVPGg+Oqs7Ww5o8zfI6iTFO2MZXpWZO+hAGHM9tKCktAZvH3O+zQH9GX2c4EkFGNmyolfjdvEXviQBWDpJLMznqxAbsNLK57m1QtdLFqbQhGPt3muV2QIzD05Dm9GcIDM/kY8UtHxlgRuOIIcCZf4eVQ1CkZNvGZQ53at6eh65wCnea8Sqo71Qr+18R9dQc6Kq9rVrZf0+bRp4yVGPh7FitUE1LG7G5Eb4QwWNNK833ampvUFG7JjjMFFPeE67ikgFBzn/5qIhDX90crj0JgJLwhdF64coN+io/cmfG7vvpdQl1cvUn9//kAQxT7BQFQiWm42GTZUcnncIesvKAICF43wvFEQwCLgn4jA6MgsDbOI9KV+pi4Bt6+24FzbYItmV6xhTzwmM75nMnPdbcQJa5VJqYiv7nLXNggh5LL2OrqB6O6t/AUmld1CwDeqDYViz0jcxx9xk0e5ygv0eI1KNB3ek4sD12hvVkDmjhiEWCLLiR6yq/o2Bq7xSw9CxF1w3ij3bdnOflzUDAJuQDbG8ziW9wF3g3rM8IbcXvOXb9E3AFDpoeATSIgwgc1MttfJqf6dVWkQbgQpPx+xQVF7063hFuZFOphkoVWlUcBuCDnLRkpJcpA84+4ZhqnoF1dvoRycl+g2C6IndJo6JUiwJR6xlA261Ow/pUPeJx/INqAim9Lx6slnxGQTQXZv30+xLslrDSRBldGR3FntUr6xL4fn1qGfJIdaXYYidpiIYXsvuigPKWoXTYEKThDVZqwiecQQT2X8iu4D1n7PSERnM36DofvEXUplMNbGCkb+LV3MReBu48UsiX8afL6taSOA6/InoVIz1yLXj4iyFxqh8bKxHBNWPBj9ywx2F4Dh0EG/DtWx0tuERj59Ac0NQ/ARXN38YKcnnGoeG+xZp+Y+JspMwz3qY+Ok4HOgmV7BqHq3vGj1djTVh/4/QX7Ys3mZuh9VUUO9MBZpolg4htaPSXYwu6zx7opLOoe6LZNAsn2dWz272cIIVj7IuZonXdcP/IXuH4GW9EYvwmhAM6+YxdsCEjlybmHEG2aPENKtH8vcZpD8GKCa+DXWAD9oJqT33+sika7RY404tIo7FVwrRY2xKEUfEkKp78mmAmdYtv2kaS6gLiSK+7MAuG9NUkl9+KSeh/RNAsr4C0DMeBMCTE1ifI4Azxi3VLHpQrucpvZeP31WKFdQ+ZKYRZa9AbFDHBD+ItAMiH+GR4tgrG/iKgzQLRH4Z2svjwNgF0FdEfZVasDg/1nTzj3sxxT6uURNTqU0CtR1aupstF+EE52MFm84CEUBIg/TJnKK2rq4CMcnhHikJykrukCek0U1Nnvq5H0YJXaQa4Gv6jJiEKXO/hRbaQT9TOIt3al+Ch+aBqDYYaQfLhwwzWTAyXAIDbTb7Z6cNJbfe+PC2HXrguV6kW5/1YOTFUfpTLfwmXVmUwfBdiiP45hqrMEPS32Cu+ocT7IsQRFMXM/VhggNWxxqRUWw6vRNiomF3dUgMlTVxWZTV3iN7Ztg5IzW33ga/0Jbf8GncvX+BVnXkna/QHoq6wrEXPoJGjg0KIiWNB87rYyDTSzAKEbwQhZ4O541Fh/tpQA8UFAEf/urZeceuAlhxUeUCmfLyGz+plGsIhq2R6MoToFShGY1I6EVBiZa4RhLLZ+0qwffM3DKmhzW+vnwBHCJHbbw9Qlo24YKx170g+WEfMU6ArqfKm0MQdEb+kmHF1nYn4z7fasIec8Y8siKfNjxwrq8SOyfJkOsodzR26tWnxO3kYaakXhi9Nj6sXp8uvRiUXuCEGNwmBBtNoWfGb/kmeIzHBr5UQozpbsBofVJSy34F/MJLI/SJjoMOHi5dUJGn0oruo2zWH18//VnEhneENzgE5b1cEKTtjqo/ncdpRmGGs4NTzj7r0ntQwuStxpwbb3VL5FQ1SwM4qkFgKUc51z22awbFjjENUEhJtxKY64E3RAgfU2unxamwqLXNhO9oZAjVj094XPTtYetax46kT8RHtN3ZSnhguqvC8ASfs3z4+migdQbCLWgKFVCGMKDtuRlzwetIXCyASpc/6VnLX58WBX0WzWNKMjmyFFhcvMyvq1lS/NDez5whshAgnKNBMEdHf1et7CdHQit2+dzndiDtjMrAQJKc7ZLyEnCRyc8Wi9KYbwcwyjkuYWKhj+e2PrGQcxqsjRx3tZcwojdamRb03ZPIJB9sQdEYItkv0eAnZ9L5Xgp5w01UTFUf3Cz05uQgZPOfbk2NWeeoYzRs2j4QFNCd6L2nKhiuCTRj8EYqRpdcs/LRFsUa8pNPIu23XkRiga3ztdviZPI+mNsOu+rruwW6hHgQunQH3HyD9tvvzsprQrr7wntDMcitBCl/zGY8wZt6Oc9+uiUfD9JUykvhu6FSmJGqDOWpU47niZWl9thUtt5XMlPgs7lR5TyAUMGIWdo4qcjNsMp63FXBaFqNr/25JTwmdUX0d0vy/SRosImznG79dXoPHT541eSZPM4sKheCCKQ3CYq+PUKZteHb2vs+9m6GIEcmpX6lTX+9e4V5IVhRvXZ7guxJQq97vFSql3NyIs9X2+iDnLC/FX9p2OGzjJuUZUPQvHelTbED+VsCx94dGutqpG64atic4vBaryNCDZNn1gNcfSLLdNVWfqPrKxo+vIlVt89316KXClu2I9TrpuRcMbDur/7PJBoP4R5AmtTOfhprUiszepMCOKAffao+8b80uOssIKu4Ehmju8lbmgGyY3N0wSPSmjvjkcm7KUx41SeHC8uiXIJ1ort0ByA3NOg9eDqXMPvCzHAhZBCAp9oQEmHdfdulM99MOULLzpQl3jAksyDzOr4R1sUXtaBxIthzPQ06cwodEcOZsEfs0AE6n9jFzBWmqc8klOB9ZQ+J5RJEhdhd4tlYI1x2ZaAiEiO9PXhw36VgduXGHZkJqFHpKlVlQBPhsXlBiNdcq0l68FMD1BmLLdMA3rP1OmYqmennshuR70dPtVhR4EriXAqZZAfPWMlRyYAGd02sad7LA9vlt3Ocfw1h/H5JX0sfyPNJh6Nbn2CvmBoUT+FTBn2vhI1clDjCuwbkgEcmuD+VcTN43unW3TI8W1JmKJgfeDo5hJ76Bh7Is2TcrO0Ogcg5z8COITY7kWm0Cq3Ab070T6hYFFDpNEhmMS4CjoZuFxQQ2/kRVeIzTxWw2X/Kp3YBhYL2TE48dSuagUaImaS3dMSGFI8ULXPBpSKO5iNU6pCMrPoDrEaEY87OfD+owp37BggFfNhnES2oJKMqh+F8znPjICC+5z5ndcBXuBcXXMRfXkaLISALvEvinizQTygw9gvVqnpVypGl9VyaEPnY7A+1XZAKq6mQNcpjOKPxjuj8yk6YInoVPomLheGx/KtRagazeYN67vbJ6qLDzab8yRnyREO0NneMzeQeRkExnwjG22b8OXyd7wZnTjFenibOz42hjx9UquflsKDL0D+qkuiKuqCVpCKnkNTLSm5emIVrWMIMjgpf6+oORhUvcYOt7OC2B2VV1R0z1J9LfWzS3lXw58jnUivZISP7d/lBy1D4tduM7wTsiMJmVePFh4755MYbjshrRuhjY1sqwuKEZQhXrLkaw+yS5v9PuBJXlTc6KruTi2No7J/U94s7yvjjcpEVhVkrZGswvwOE/iazsR5xJCV/rbjDkrPqUBiQHVCnLeKXrArKg+F2V6iFkfYiYd5oqLQ7qfjR4e++ZkYs0FFHgWIa2plyxYrV76EyvCiL5qw3yZDN/n3ds9Sdh+WKz/NR/6kaCqCnHRSxKGhchWnDDIF3uuTGu+K1E42fn5GURwjRK89ocZ4ldxjXfqK4tidWs1gZ9u4fBZBV3mFeOefKR83RvhZr/Kl4VMX4UQ3pd91gpwSfSqVw4yscvWryhCEq9qZkaN+QmWIFeG3dohLr9+uEr3zF4FnH/nFADx9Sirdl+Rhbd88Pizw5MI/pOIf5F0j2Ocvz7PWBPVwo9jKK9pBZRZz0FVEiS+7DL8n0hY4PdyC1Z1wY6f88J3I4LJPigkDo3EaCYhkULK9lNNnQkG4ZzWIMHH+f9Rsjl/IjCTG7971XBT6Ikg4XmujQb6bEhx69k360iKGl6zEW+0oLqpILqFILJaTv8s4UtNAnEnuy29P+BwBzhlxfMwrMLIoZGsISmDAEHY0adGRRhArJJrlek4lZP774iOFjRLhXBywL/nP19iPoj5d4B4t4dFJ8uUchsfSrZ/FkO9OQp3OpiN0gKHUWSk6ueeFCLtIb87ky+huVifPP7ZWX1OF8AiVlPOdVAlwgxuc3bSH8KNzzuaesrCDrCkwDlyEEDjPixcgbUbn467nvA7mcghMojZrMmOCn8ewf/HMCL29ZXrql60STdfLyGVFal6lMast+m4rKDxp0ztODXODdlJdPNe+iY3+7kjupVRwhvc+sSjO5ZH1YNvkb94I7QMu4zr0OHi85oO5Wj5D6t2CurfT55t3bw9YoZOusZ3Bc269EoTDSrZCIJyqzSyDZrl5tTtq6l3ilLxdQI8JvNxdt6GqaFV9Zpj2y83odC8HrEpHzI9oIwW2/iLZrfrIsrS7A6Spb/bp1+i4THscua/7HAI+YimuBGXL6HxMOzyGJLWOV1zJHln76nsE5ADGNFbV4p3nKGqBEEK/P/OV7If3CbWjkYGUi+TxIPPgpDNITJLShvNxCldr4j6LcA6a6Lmk48AT9ocZTpeaed9N0QHMSAC1TknOwbXjkbfO6sUZW/zsoMAo+7/7eMaboeTjNUdWc+XKIerYs5X6T5N5fiuoL2yC6iUeRreuan7eXBFhofkuACypMDpL7oOSvstHeOoxrZeH3XDoyOIp2pTwGOzYF9neEyG2PSD1xuUBc3+tBpNljsujJnUteksll5I94NESUMgw8NCtRFK9Mmai93+fjzXPp2/NB1Q4cbMEXOkOWDyLtIOOmrhy1oyRO7F4+jPELyuapjOZJVgyM6fntljFG8NQoLC44aqnVdKIzlWkCIly08McN6WCHSb7riFBjCY0u62N867GVKCUloADpME2cde02ierTFlnBxYAVlWYxAvWwdHiO3670xG728L9WCxInQY7gPGxHR8TnCt+KVpFtnbm7TJxsH9hnK2Id0npIaPz29TGD/7YNQQ8oQC7ik1fo61Kc1Bfcm+u9aU+bEDf4Qz8oDK3RUABDKOy4kaQp/HOz34N6byby1iZGyv1gfB1E/txP60lKr1N0NS91Ii3ZNaa5o+mpJvNFBDJe0nCm0OU8TcwOCGz+WTEGfcP1CnyLbpqtE/D5rSphfdCUDACNK7dVd3SDfDk1aHfhL0VIksyFpujgqpSQJ3dAU9BVpXaIPkt0rqSMpSV9q4TWKlWYpUjeu1tUuLZhUGr4379RqjZxc6udRKhCqcr8mHsc9w0+GXWuEOMUXw29ZmrPN3Lh/5BJ2ebNtKZ+SmSOH5KSA3mcYILnYSOcRebnk4AkxmoHJWNYTsSaAc+rDYkLU5Jd4Rhs/HbWoj0Y5rR97Ol/J45mcQH5Q3zrk90PbVRLhnRYihhcLF0GhWcvF8hfvRQgdaTkLw5XfK5/1ecSXwgm8BlHh/5G8Wgwl5/LAatDWA5C7CROKyXY+w9tYSbnYTufVjPEV+mI70FPPUezo/NL19IY3n26/EUHDqeWsv6s6zGrwa5ocCH+PRmdilVh/d54wK1qOpK4u2tpsxTLaq9oz8TYG1tGTQOde/UuoWwnos6cvataXJuLxLGWyXfe1IZtVrMorua6J4P2poFk/GjeFmSSP3c23UYRz+qG1A/qb65b7MqftsockevTqa4PDi4lD83/q93Xvj6NW3zpUt38IsMF/H2k5af9viUicHIcmkOQfxWpmeF2FlJ/GsE1SNl89gHvoC2XkaPmz4pQgzmOsHCWWVX5wWir2scw2CzgPoh1BzCq8QNkFJlHxR7xOTTRG7oBVhEzG/8VG/hhcjWUPbLGqEQpzy7s3GPG6+3DlOLKB0XAIV8heSGle8W4h4LxtIGZdlRVM2aUSVDRm3NeQaeAmttq6f+rlgdwVye7kqEMfoynrQVPmlI700WhTKra9JUQumKeum2Sz3vjaSlZNyMYlQ7WM/Pd/1L099VjaYVPBe398sMXZcb9Ye4rTJBEQKoqsD+BzDmAi5f0nOCzFM7IL1MHaH7oS554cP+6oIzDDRII0xTnH/GKhJoHq8E1cf0KMcGF3s+3ZJ1/JTMRPNFJu75KcznuLxDjy1kqm/hIXiuie43s+MKcIN6LZQzu72+sMzcYJCbuTNcCP+2Nk2DWxsGNpMGqzR1dMhEV+tzDnKosTHyHhfRDmX2mwysWPakkX46SryKuWPyyovgvag9CcfMwzKEX03DAhVAWbZD7ICS+teJgQi0PsrhIQpM8C4iXv3HeNMWcVFPxepUp5vYhD96m+CTOaDcq8KiWeyMTIOxhgtY/VVjKQ8hweyL8e0vZ1B9l5E7HCNg8VPA8wVxYSFy7MEpIgk8cl7WmsbokeFkpHtk8Fm1UezRXrRquUmXeY+GuE3HRYurVGYFc/lUW0Df3EBn+BR9bgguylgkgUHvJ12dQYfkYe7noVFmF+ss05YjxbZm17mXmXxCBYVTcwR98Bhs6ncQX66rCONxYAOsrmZ21Al+f4fg4VBtW1F6n7t4llFvMCpBSu2p+JEZmuLIN++U2xRl+1rzvzqZXTPJqQCIgSYdGUuD0iXA5WuNqgS4gkVZRU/Q3ZEbClCf1qsWZScKPKe3xpuzw1XWPq494JxUdwKt74Q1OfAY+w/yslc5zRMyO7nH7gFsGRc8weI6M4u/bSPcb/slNkZmyWBEpLMVLhM/aEDtkH8l/te7ixQR2yo+BUZIJDZc1gZuhqlDzSr5QPNDjknU1DD6U0V4Hw+vHdxeTYYLBEyr/XnU94uRAIR6FFcWr27KuaZVR2kDw0hjqh6ErJ7RwkOtYmeVS5XEFqkzaSQtGWsa+MV8p/vGHT0muhYx+6vINmcd/AWonlFuKO/iZBvR9PUQ7ymt+9fdzsI8SUJyVqxyvzi/F/VucJmUsNe922KNUdcszW6l4ON0X6yCAvdZGR1BgDnuneDHbSqkPOphVS+6nA0KVjK4S0pLAwQ8KdlmT3E7lMn4ZVrn1SpQXHcnS9L1KL7TFZD38Oz5MDspPwxMStRe+RCAZo1IfypYA8XcHYPya0y3G1w9b35nQeMua4HBVCvZbyn92hcHqcUt9JW1lZ1HRMRXhugIfLwzbBb4F5HFSaIeqiW5MQSsJuXRvFXzgSfDl9qpjXfXMJEIRUcmUgcUJHnIb3vCrlbHNe5zPYhFE+G+9qwTWQu9uV5V0AB2036E/PlaWwg4FoUpG+hOZKK5Zf3wEEBkPnuf5jyzVtMvtQr8AVIXIeOExpXr/Np2Myx93gx6gIy1BbpHNytCldKOwRs+eoTQrOi8HwJhoKjquxebJs80PO80Dv615pRMqzCG9VVWvAITwAYC9O9XCcxpY6WSHYNT07F1cN/sofh9y1act5Pb1YZ0xBkXGByONzPSGCmhmWG+XxkPRTtez4bG1eIibJjO49DgNB4/8F4RR/xT1O8xYwb5F8HLq3d3W5BcPNIiVaB5iuMyvDL7XCSDwzV/Gg8Lgm9hYtzBxxkfvhamVOFwz1ITpt9MOGE+pAn/QEYNRFRIvlIwZhk35g56ZRjuLTCabAIP3hXUImVjgq2HUe37AKQ6wq6+qwdGwaK71PHPH1B3ytYOdUU62DB2uzPrjl2r8FE244OMpS9DZ2VMdeuBx3K9Zuq908d/d/Oibitr2+3cujY90+nCdjBfPNp8+QZfZYb2eJjYvKFggR3mYbGHbff6ABz3RHJ7RZNqacIZhZLAHOu6X3dFjgAgrxtgyDD7w8trYdrcIM/YvTJ7eFcEOHPAYWCBaCAh3iEa+HkNxdzF4S9+1EoihIjazLNhbXA5XvPxQfVtO0wCKwuKUZVb2Or6pM2HD65OpRsxvD9nVYgG1dXt8igIDlIRijTyzVQClnBBsb7/Zf+xBadS/DnKb2zzdoqqfHz8Zjd/+pNksmDfqXZm0RY/DMR8VWC2Kdlosb4hRsiq16U8iDQhl6CPtyMsW6cGH5EPb4DbG12W71IPJD+tizqU0UMEONXMSnrYniidr0rAesV4yUa/Jfo4RbK23uhVK/2ZQcQln+e74eTgiA910iUk1Tihfo23IVekatw9dRsnqCAO8FrPnlHKib5N+VNI1O4RSeWals4qkf+SR1kK3lUl/LLSOW3tY9TPY8Up3EYcsr0QOkODMSgcHEFQfSMy/S4BFvyNX4aCT/OJcLusZQYc4fiwtTMMit3kPbs5N0M8Y/VukOY9oY7GIKQLUGMT190UT9Tr0RzD4vXKmxNES2Bqgas+Ib/FrJ8gTxAbQMxaXC4BZTgXj3lq6xQJEdCD+AhDBP/ufluCeEkh24gfELvKqJqcJoyPcIKPIYkE1U3yecUYqljZbn+o/7t4/BkMU+d9/TXwaei6jUnqiCd0MIgDIEuSCPlEcTa/W5jdPXFiV+2uMh/aDA63Wb3IVrLqiPn54vvlAmKj1A2K+46dCEthp5oVAonQGndqbmwPsLmGjGVqh80NplAZr0LBqqFZRBtvFhUyXA5ZB/k7ZxnVuWDVOOthAB+AUnQzdLP8KrCPLfj95pHyYlGoyhvX7gXHCVRwDHbP89aorl6nL2DnQ/sfxnufr8yWpsO5SUPCXRDOHYtiqZbP/0bydCt6MADza1AA+mBQ7oXq/gLRU50DmYu3DI1dcNcxZ5LPPLtGhXG9Sk5Aplpwj5nZ5kM/KpX/eC623ICy9lGthjOwG5tpaRAWBYmjYfvQAECl8U3r2fuALSKqqnNZrkADluF4mq8d+I+4+GvMvMkVyg0EXe9flrpofcIEgFEl7hn/Oo1MUACPyN8GgLg1qy5clJKe2c9IVVDNKpZXCy/49T/4IeS2HNqDwAEtB4ZLiS3ciCdFGuI4amhgkoeee4zlWLCjgpomM2vZGW1S1X9GIoztWb9sFd4aARYc0AXBIBUZ3DUCOFrzFHz2ApNViuxfz+rX1XoqNMbe5h2V+mvmT2Rqcx1Z2aK2HBJOV0AJl/K7afwTd6J0T6wuIC5IRf2FGNwoLlewzGTTmp7/j1voLHmx/4LD1EIK4K0BOpdOcwfzKIq49LkX1H/RkvrKQ8VdTGEM2GIm2mhLGh2sjutdUePy5ZDvF1+sgQwxytiMIVqCrH/BFCPBFcmdBBnKPgSPkyO6+HmIetz6XvG320aX7l/okdR9YxUuHbu6HH4ixb7ycN33pj/EfuLSAwGhK2V3cyYsvJ2Mtg0VhIvT5iQ2I8S52MvgzU3aGRDtxm+C3HjPHdPnd8UMEM2RYFzJ6e0NmAvv9ZQnVEF3OiE6qjVGQNceaq6gNOOVAo3qwEAE/vZt+I4hcHVnZNgweb/jV98gKiMiKH2ZNwJuHGljhArXN2N2Q9tJhlLH7dPzgXNR/uSe+ORisljsli/ZjO07Y1mJYJmZTyrL6lwlNvpi2e/tO8NKEpgM763Cl/bER23OmaNZdTXD9XYanC8W7AexWpJGk8MJ8uOCUW3f0Ney/C2N5Mw/WXpH8+8FZgbWvxY6ruP5+lMSYHRiIs80+7GIJR5CBQ0s83PZ9Y2YQvZP6PSrvo3DeTv23UUccF67Dy4khDbrDTvxfhhIWxxkB2aLeOJrs7WkrCwKQyvSbINHjnMjYAM3W+1XaJiys9DYaY6jMmDdVQOGBnr5ry5h4cZ/LMGkOE4kTRb/bsuQ2fOHTAPIuRwZMX1of4NGB1XMyvTDPmYbyi3qg26r3X/a3wWG0NEFmsVOgKs2CydPwAitx9IC2mQAiuC6IDwRZ+HQMHrQYIu5VTKaRyfHMdhwRDYuxqfRB7SjesFB4uN7u3JQOja4gsiWQfgnu5XXe51jjwpHJP1C2/aEAs2muWkQIP0Bl1jvezPQkjsxoChVLMMYz0zvJ/okyOw+gwzIgoEXs1z9oxNLt1jSXxDLt6YrQkjzzC4oq9oESDeKkijG27x3nriibZzgrtOlBo8G9hHXKhxqmb+AcyCVL3zJNbpTw4ElLXQ2z8iEQL7L36zgz2Bwh2XKGQF6fbkQ5a7WOA4jYpfKKY61KeTXz1mdJ8v1H0JEr1I67WZ50h3QlGZMRFwAB7rZByfZVKo2SPb3JQOuKbrN+XSQgyjPZneLrrbPKNMsN1wcDl87wFN7NaD6yPCAcM1pqGaBIYfR4wTO6y4HadkSxXaLgLltP6Km0wUMqf0K/gfzJPIq3Bo4pVJ0E+sIuLgtYzSYluxWjI3vK3PjKwkGRZ0XdCiCzakuiWDtS3ZoA+nTWsWeC8ubiu5TLZ/RQVBsqIWnXvvTVdzovJ3mmcpp4tjbZVz/L0kdXNyrEbwRr4qaHj+KWOXouCdEvUHOLtM9Zq/TKESD8NU4N5p72acc7IH7mN+9k2elACk+R1Hj2Dt+8tFzeeGZzhB49axbS3jF45iKXfEL0XSHb84awnUYhtnvmMapE6VzxLm+8seAA3juE/SgZkXOornHREoHh87H0bNhMLIUGns9gpI6uvp2kKL+emoEcsYKsqaPMXoAVk/Cavm6opWokLwdVa/2Sg9ze71mhgMcFfhGnAgdYOvw2I4vVGTNbXE15T+7ER2qYXWsQ2aK8Hzmc3ZeU5hqGaTBN647MFo3tfXxA78mQh1foVuJOkyDPd6UN5x7AKRPfGDzwZxDxr0P1kIXQ2rK6n4LjqcGCZSNoNbFEYudG7NqFNtf7qMUwdDbzVYPgEOY33eIsFeT8Z+A/jj1U18YDtKSHHrJ5XtgLZIYvHcB/GiqUMPkauxaOJ9QicMNtHXLvJpRMTUg2zQCtCwWubJP57eT0s4jK+oP5b5H7c9S9HJzc5+3qKmrEZFEh4pPWPuUd0JGArmwFRB623gwmBSxJpIy/EF0zmHuz2hfzAGC6Cb7vB1CrC+JekjpjbW9Yt0yOGzgyIsBz46HDZOQzWq9y1sUs9FUwTucrkVvtFs+EG5vzwoyzXKd1nerlilLnFBTqBfmt3vjyFOtK6H4LUvaov4QBNQ7tfaUN2E6oWo/KN5TK4/1wk/paYN8tZM7MjmhA678wHue2RAn3TuTuaGo7PEwbwLATyuhF/eXkV+UAcKxUj6OL1Cjz98U+M1YDGq3IFoHw2XfQj76V3enzPoUinxgVyzf4DO8gst4rh43rhRVArwRh9Yer555G/xYRhpMhInAI16vpcNsBD+r0gRG1fkZTiHQprOD6uZQJtZoc+2UXdr0zsOKWjEwJxgiNljJ8LcTe44BzaFoEgrxL/ZTf4CQ7XcKnWNAvADU3Wuc2IqsY8Uk6a30n5PcE4FfcZPobhan4bU6971SQChoWJaNkuSVX8Wyd3l0+fBZwUgD60HJGU3lIKWQMu76nr9Js3EwGDqHCXfWNeVrIRdDiZyR9+19Ai8CAVRzFsNO+BXPHVzr5ByrLtMtj90dPsJDDNamH7lyeJahiDdDsVEW5PCl6fLnaQXU9qDMk8zKSXqfXPyCjuV6czOrdpNMvxZtYVAGsnilquYVDqHU7zAH+qvCmBgDGa3sRinoXyLGIqiQv4bLyPej+N1XIEAM0mYM2ckuCSVPQlqMXypFSBYVW0Z+ON64DI4KpfDWfilUILnTA8//DoRZ3YWYoGQ/rD3O+O1pGl8FeR3j4Sp+HC0EE6zakJbgUhvHFzsMthO7A3UBTWizW/BVXrb5uEujpqxaujxcryOgJqXZLEdYik0PKRN8ls0j1W/NdMOLxiGwK5nvHG2dFfP5TlUvNW2rE+87OuHczgGwLNTSYZkAksGrLS3JFAJSDvAOFnah2p7lNGWxyaE9mOWhl5WcQ7WRKykh7PHKSfGoPufxKnSgpZgFiUMsQGA2jkqV8vg9jjrZQo4m5ffe7dBwB4cPG39p75QiowPjLBwCGuaBmtZxxUYT7B9qOhsWNTjDr3mMsCeiBY1PdBxjxhEItWUoAFEuR+LrQyXWFDJpk/KmEHmBEICtfvqS3gx/yHlYyCEWqholiFv/YZNG/1ec6jmwFF0A5rS2pZvzXH222LrT9dkh875wWPCTZwemuVjNaSH6dx48IhCUNmnBl14vu271zaaTjSlCze2ejTPSdCtlBE5pYt6F2CCy3S1Ku2eFNb8APmwxugXbxaeRgWMTRBT3aOJj3I4obZGFNGhO/uL0jiS8ebcij3iMPzJy9F8z8q06we4fofe4G8R7LovgyijWOqWjs3JIoCjgk1fAJ+0OOD2/GOCsKMUkL2p2kj8PDAVS1dv101DhkyL8C1t7hq54uf3/A2DU4Px3z3zD7kJBtJjhjwujH6eUlhe4pupqbQxo4h47pRINOsOvKeJGUDt3N0RCzzVoybnhR3jgG4DkRKeMT274zGA1FKsYDh6z0x1MhcLCclgrfhPLVHwxqDgd17C08qAET8uj/oxD2EaBEp4mj8TtM25IOa4Ybc64a9WKRLGRsW2e5uLyoJoVRr2tbX65OtDepv12OCg+3X6nRG0LyY9KNsuPb4JRFmXJ8Yn8sZhFlW4Ga9r/5ORUKidYajuC/eezC7EIQsIY/fGLBc8pf7kM6mz5QoqPU+uj6feiK79F9L2aZzWbpfQXhVddIwfteSIoAQgFwvWYFKIgTigiEazEGtvXfkGm3RLizUB8KHthdqanTyOLdIZqKXxgHd2t1C931I6Wa1HheqNAxmxPYzDixRibgcqryACyU9BiToCdbN8SrO56TaE8VhKQONEcld63AA6OrfJWhIToT3jyCr85NQ0Q4YcSkng5/gSEh1Oxux4cR94gaX3L1Wgw/7HaO7wzBPk6ComrhX4RiCvwOLkzMLGUBD6JH45EYsFpXzmb7ubkEScRlzPWI55kleZuj/dBzbx730ZxMeaz1+fqJRvawzMgyzHGSH0GdLbuIIy43ndjm6/oj1HUdwELJ7mvAHEroBeCJE2Le1aO+ieXxWUcv7Oyt9ONmZNQhfowWtNiHcEuQhgPZpRriz0t2vl0u5Yk/sdII7iejVvbUuAqgH0X2n+O17MNRLnB3BanGAcgTe55rf+TKOumC4XRrR7GFziDCyJP/31aj7qxo4JI0oZSHz10kpIDD6E0w3C3kUoYGgYJ2qKaqzbhlYxHReNFYMq7BBgS5O/B8Qd/3gp8N5DXptPRXoJPn+DwnjAEQK6MXV+mEQud5qFMrRpRLuq2OHfj1axISdYxkljEgCthZEy+pOSpTYvOf7Q5ee0pCTdIlDhc7iU+iAIFJgAwcWyLbw14hBhWf2JiZts69I/SUpfGSuGqFH/geG3PXSOPUWl9DLl/zk13vdtimerAM+PQkV5p0Zv8rjKBJod1vH2ineBhpBi6WZJLLH2CgHmCvQ2AdHSXQW11K7LnMGbgtnQsBOgLIi80OtjHJMFJsRZubPjFzkVa9wijSd2kLxCaXXIoS8Ah+b6Dwl0ghkV8bDYQSxk24D243Pe7UGgmNKhCOAN0+maE4swSDNvdEOj/CZjFcmKOcIKhvFbalt5BGCI/tnAFzxpbQSJMwvMlQ1rebPOhBTseRuDWaMb1lWZflApv7ZF2YDCuf6fXag5E/LqklM2UPvgfnyYNDp+oJGX8aOpHpDPqAF7lTRPHeCCcv5ufqLjs7/sD5apmftH6SsaLbXZRC2JPIAYplpUfQxjxgH8sSOAGeM82Rp4mM7gz+/4YdPxNhaw9NSw+2nVv4NL8SRpEpbFODIVjk6plw8FOw5uWRezyX3wCBzMaBTyIKINBD8tHIeOiWLOr96EibusZ3XR+eEGGcWi151TV6o1NqR1OnjfshDs51zdZJ4QmdXOBAA5Yx+LPB2WgwnIsyz5TOkFIqBN9ts2sHAXAhtOdt/WB8Og9XSdqFhAF49mmRdbZ5H0bQL1OD+jg/f0gm8UiOxtvRnGttW3rjVDFxG+V+0jAMZYYcBFH5n0qB79KB/Lu57hArmLHQpS0toyfztXCTeRWa1gCsipKPndBdfR2yx8PXtfDVGKEOT7YWnwN39UBwma7Q09ZKIVBubibPe7JE3XXZ85c94DGptxNa0vpLz+aTDSjNmnWfQ/V66mosw7ewDVDjNgOVeLR83BXgTAASeDUCxaTj0hQJ0O3YRK9UA46C/Ce0Upg/yHrYePh/BhnZ81lrWSM7GoPGpk2Mj+OXg0qqiV/91Tucw/emG8eA/Z8pQkiStu2SgSmbvm8V/BbQXmsqYb1MgTuVoS7SR/3pB8+N8KE+CCvVrPMrGQEyhXgKIgXf63GZrxQCFfC8E1FROSnENu3HDJ/lhGdlFvm4LTTZWNMybKw4rkCT1AcRpvY7xPBHf0l4IBGqCygO+J3ohnbvfHIU0jMBWHnVwABwOqIXW43JUJCnNkoVeYuDwYNwV9y7/bAiFgwVAJmC5g4Ato/CCqSb46M3atRQTwZ1qFDRJCgUPDTq6MHEY0OJP5tu1C1ILmE17+1mTDhMoLjTC6vtavdn5YOlDiPkmldxvyPCozABt7yuOeM3EZySELgGx15BTTxjUihJuXkRN8i5hx8AX16bt03LUNZcp+nR991DFIvEVFcrJb1lo44/nkDovdD84X2s8XSkoo9AyBWK7fNssRiWSletkshwE52rRI83I1i67R+guCloEcKguX4MntD5cHCQvlI6WOb4gai6U7Uu9boAcZ5En3HUemaJHq8E/7pONKFmsgyH/gTQGslHmLcxCHvl/v1UqE4NR8betB+A1sa2Re9unGVEIPHhraI92gC4r+964azVfXjqItTf6cyBpu+Z8xrptkWUs0Sz14ctUCxf9phhn4vk+0kDG7Qxg8PerSktnnjO1Fh59yp03s/BTXoxrVfL1YYLOnzV6dnp6Fz2hAjpdzLREq99aKIy9+PUvveYcn/70NSD+eJVHYVPAwaxRkw02C9eU9A5xuYmzIL5QvgVcNCBh0Z1xklZvgWezGCTsgFyi/SPDVtBQ+IxBwo4ubMK8IGxhZwvK+6y/YaP8yrb83ENOjmSuR9KiW54N+VPES
        - #1:
          - type: tool-result
          - toolCallId: Ai9QKWuMjgMaQvZs
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: pNHIz3fCTRo3U1HO
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: tj2w9EYmSTZJiSgZ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 017RakqiT2GRVuHh
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: MVqpslSpxmUmfUpy
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: YcplQrZE6aBMIGKR
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.