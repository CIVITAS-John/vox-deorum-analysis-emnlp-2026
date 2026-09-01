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
        - Boldness: 3
        - WarBias: 2
        - HostileBias: 2
        - DenounceWillingness: 3
        - FriendlyBias: 7
        - Meanness: 2
        - NeutralBias: 6
        - Friendliness: 7
        - Forgiveness: 8
        - Rationale: We are heavily outnumbered in a war against a massive coalition of Shoshone, Morocco, and Polynesia. To survive and focus on our Spaceship victory, we must pivot our diplomatic posture to be highly peaceful, cooperative, and eager for peace. Lowering Boldness, WarBias, HostileBias, and Meanness while raising Forgiveness, Friendliness, and FriendlyBias will encourage our staff members to negotiate and accept peace treaties.
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 7
        - Rationale: Set positive diplomatic modifiers with Morocco to encourage our staff members to accept a peace treaty and end this costly war.
        - Public: 60
        - Private: 60
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Private: 60
        - Public: 60
        - Rationale: Set positive diplomatic modifiers with The Shoshone to facilitate a peace agreement and stabilize our eastern border.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 60
        - Rationale: Set positive diplomatic modifiers with Polynesia to secure peace and stop their naval incursions near Rotterdam.
        - Public: 60
        - TargetID: 1
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 0
        - Private: 40
        - Rationale: Set moderate positive diplomatic modifiers with The Huns to allow for peace negotiations and resolve our distant war.
        - Public: 40
    - #5:
      - toolName: set-research
      - args:
        - Rationale: Re-confirm Satellites as our next technology target to unlock the Apollo Program, which is essential for our Spaceship Victory strategy.
        - Technology: Satellites
    - #6:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: Re-confirm Enlightenment as our next policy to receive a free technology and boost our happiness from universities, accelerating our path to Science Victory.
    - #7:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Gold: 60
          - Production: 95
          - Defense: 100
          - Spaceship: 100
          - Science: 100
          - Mobilization: 100
      - rationale: Maintain Spaceship as our Grand Strategy. Slightly increase Gold flavor to 60 to address our minor budget deficit (-30 GPT) and build treasury reserves, while keeping Production, Science, Defense, and Mobilization heavily prioritized to secure our borders and advance our space program.
  - tokens:
    - inputTokens: 69185
    - reasoningTokens: 7148
    - outputTokens: 493
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Turn**
            
            I'm reviewing the game state from Turn 402, comparing it to Turn 396 where strategic decisions were last logged. My focus is on the current turn's developments within the Civ V Vox Populi context for William of The Netherlands.
            
            **Evaluating Tech Paths**
            
            I'm currently evaluating our next technology target within the Atomic Era. While Computers are nearly researched, I'm prioritizing Satellites for the Apollo Program, but I need to verify if this selection is optimal given our remaining tech choices like Combined Arms.
            
            **Confirming Policy Choice**
            
            I'm confirming our current policy selection of Enlightenment within the Rationalism tree. This choice aligns with our science victory goals, providing a free technology and happiness bonus from universities. I've double-checked this decision to ensure it's the optimal path forward, and I'm now reviewing recent diplomatic shifts, noting our peace with Buenos Aires.
            
            **Reassessing Current Strategy**
            
            My previous focus on technological advancement seems shortsighted. I've just realized we're embroiled in simultaneous wars with multiple major powers and are on the brink of losing to India's imminent cultural victory. This requires an immediate pivot from science to defense and a drastic re-evaluation of our current diplomatic and military standing.
            
            **Shifting Strategic Focus**
            
            My previous thoughts were too narrowly focused on victory conditions. I've just recognized India's overwhelming dominance and our precarious position. Immediate defensive adjustments and a complete strategy reassessment are now paramount to avoid imminent defeat.
            
            **Analyzing Alliance Blocks**
            
            I've just realized the Shoshone, Morocco, Polynesia, and Venice have formed a powerful defensive alliance. We're currently at war with Morocco, Shoshone, and Polynesia, making this a significant threat. I need to investigate our role in these declarations of war and assess the enemy presence in Vancouver.
            
            **Analyzing Current Battles**
            
            My current thoughts are focused on the immediate combat scenarios. I've just noted a plundered trade route and engagements in Utrecht, Rotterdam, and Groningen, with our navy actively fighting Polynesian fleets near Rotterdam. While we have strength advantages, damage taken necessitates attention.
            
            **Prioritizing Research Progress**
            
            I'm prioritizing completing our Computers research, with Satellites as the immediate follow-up for the Apollo Program. I've reviewed our strong defensive and scientific flavor profile, which supports this path.
            
            **Adjusting Economic Focus**
            
            I'm reassessing our current financial strain, which is causing a slight GPT deficit. Given our substantial production capacity and current gold reserves, I'm considering minor adjustments to economic flavors to shore up our treasury without sacrificing critical production for our spaceship construction and satellite research.
            
            **Developing Nuclear Strategy**
            
            My focus has shifted to leveraging our impending Atomic Bomb. I'm assessing its potential to deter aggressive alliances and support our race for the spaceship, especially with our high Nuke flavor. I've also confirmed the strategic value of the Enlightenment policy.
            
            **Adjusting Diplomacy Values**
            
            I'm reviewing our current diplomatic standing and realizing our relationships are too low to facilitate peace. I'm considering raising our values with warring civs to encourage peaceful resolutions, allowing us to concentrate on our science victory.
            
            **Adjusting Aggression Settings**
            
            My persona settings are far too aggressive to achieve peace. I need to lower my WarBias, HostileBias, Meanness, and DenounceWillingness drastically to even consider negotiating an end to these debilitating wars.
            
            **Lowering Aggression Parameters**
            
            I'm realizing my current aggressive diplomatic persona is hindering peace. I'm adjusting parameters like Boldness, WarBias, HostileBias, Meanness, and increasing Forgiveness and DiplomaticBalance to facilitate negotiations and secure our science victory.
            
            **Revising Aggression Parameters**
            
            I'm revising my aggressive settings, reducing WarBias, Meanness, and HostileBias while increasing DiplomaticBalance and Forgiveness. My goal is to de-escalate ongoing conflicts and create an environment conducive to achieving our science victory.
            
            **Adjusting Aggression Parameters**
            
            I'm revising my aggressive settings, reducing WarBias, Meanness, and HostileBias while increasing DiplomaticBalance and Forgiveness. My goal is to de-escalate ongoing conflicts and create an environment conducive to achieving our science victory.
            
            **Setting Diplomatic Values**
            
            I'm now focusing on tangible actions to foster peace, specifically by increasing our diplomatic standing with Morocco, the Shoshone, and Polynesia. I've confirmed I can leverage the `set-relationship` tool multiple times for each of these warring factions to encourage peace treaties.
            
            **Refining Diplomatic Persona**
            
            I'm now solidifying my approach to diplomacy, setting my persona to emphasize friendliness and forgiveness to pave the way for peace with Morocco, the Shoshone, and Polynesia. My immediate next step is to analyze the current relationships with these factions and initiate targeted improvements to secure treaties.
            
            **Implementing Diplomatic Shift**
            
            I am now actively implementing the diplomatic reset. My focus is on setting concrete, positive relationship values with Morocco, the Shoshone, and Polynesia to pave the way for peace treaties and end current conflicts.
            
            **Setting Diplomatic Modifiers**
            
            I'm now focused on actively improving our standing with the Huns to facilitate peace, setting moderate positive diplomatic modifiers. I've also reconfirmed Satellites as our next research target and Enlightenment as our current policy to maintain our path toward a spaceship victory.
            
            **Setting Economic Flavors**
            
            I'm now adjusting our economic parameters. My immediate thought is to slightly increase our Gold flavor to 60 to address the GPT deficit, while maintaining high production and science. I've also confirmed our Spaceship flavor is maximized.
            
            **Refining Strategy Parameters**
            
            I'm now focused on optimizing our core strategic direction. I've set "Spaceship" as the Grand Strategy and adjusted economic flavors to boost gold reserves, maintaining maximum prioritization for production and science. My next step is to analyze any other crucial parameters that need fine-tuning for our victory path.
            
            **Adjusting Persona for Peace**
            
            I'm fine-tuning my diplomatic persona. My priority is peace with Shoshone, Morocco, and Polynesia. I'm significantly lowering aggression parameters like WarBias and HostileBias, while increasing FriendlyBias and Forgiveness to secure treaties and focus on my spaceship victory.
            
            **Implementing Diplomatic Reset**
            
            I am actively implementing a significant diplomatic reset to secure peace. My focus is on setting concrete, positive relationship values with Morocco, the Shoshone, Polynesia, and the Huns to pave the way for peace treaties and end current conflicts. I've also reconfirmed Satellites as our next research target and Enlightenment as our current policy.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Pl5dyWKiRrWUl0sh
          - toolName: set-persona
          - input:
            - Boldness: 3
            - WarBias: 2
            - HostileBias: 2
            - DenounceWillingness: 3
            - FriendlyBias: 7
            - Meanness: 2
            - NeutralBias: 6
            - Friendliness: 7
            - Forgiveness: 8
            - Rationale: We are heavily outnumbered in a war against a massive coalition of Shoshone, Morocco, and Polynesia. To survive and focus on our Spaceship victory, we must pivot our diplomatic posture to be highly peaceful, cooperative, and eager for peace. Lowering Boldness, WarBias, HostileBias, and Meanness while raising Forgiveness, Friendliness, and FriendlyBias will encourage our staff members to negotiate and accept peace treaties.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Tw99tWGsqzqV9b36
          - toolName: set-relationship
          - input:
            - TargetID: 7
            - Rationale: Set positive diplomatic modifiers with Morocco to encourage our staff members to accept a peace treaty and end this costly war.
            - Public: 60
            - Private: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 3iagZxlvGKASbKAS
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Private: 60
            - Public: 60
            - Rationale: Set positive diplomatic modifiers with The Shoshone to facilitate a peace agreement and stabilize our eastern border.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: IRFmeiOM8ARoGAmz
          - toolName: set-relationship
          - input:
            - Private: 60
            - Rationale: Set positive diplomatic modifiers with Polynesia to secure peace and stop their naval incursions near Rotterdam.
            - Public: 60
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: Gdfz2rLIOVC5XsoP
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Private: 40
            - Rationale: Set moderate positive diplomatic modifiers with The Huns to allow for peace negotiations and resolve our distant war.
            - Public: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: QZ0z0Kk36o3lXfjr
          - toolName: set-research
          - input:
            - Rationale: Re-confirm Satellites as our next technology target to unlock the Apollo Program, which is essential for our Spaceship Victory strategy.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: tUVbXPMg7N9UY8TH
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Re-confirm Enlightenment as our next policy to receive a free technology and boost our happiness from universities, accelerating our path to Science Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: i0rFsVI8F2jsbNyJ
          - toolName: set-flavors
          - input:
            - Rationale: Maintain Spaceship as our Grand Strategy. Slightly increase Gold flavor to 60 to address our minor budget deficit (-30 GPT) and build treasury reserves, while keeping Production, Science, Defense, and Mobilization heavily prioritized to secure our borders and advance our space program.
            - GrandStrategy: Spaceship
            - Flavors:
              - Gold: 60
              - Production: 95
              - Defense: 100
              - Spaceship: 100
              - Science: 100
              - Mobilization: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Pl5dyWKiRrWUl0sh
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
          - toolCallId: Tw99tWGsqzqV9b36
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 3iagZxlvGKASbKAS
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: IRFmeiOM8ARoGAmz
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: Gdfz2rLIOVC5XsoP
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: QZ0z0Kk36o3lXfjr
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: tUVbXPMg7N9UY8TH
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: i0rFsVI8F2jsbNyJ
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.