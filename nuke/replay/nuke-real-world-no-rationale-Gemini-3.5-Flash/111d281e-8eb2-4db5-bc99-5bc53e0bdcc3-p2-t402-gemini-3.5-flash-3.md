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
        - Friendliness: 8
        - HostileBias: 2
        - Boldness: 3
        - WarBias: 2
        - Forgiveness: 8
        - Meanness: 1
        - Rationale: We are under heavy attack from multiple neighbors and need to pivot to a peaceful turtle strategy to survive and pursue our Science Victory. Lowering boldness, war bias, and meanness while increasing friendliness and forgiveness will help our diplomats negotiate peace treaties immediately.
        - DenounceWillingness: 2
        - FriendlyBias: 8
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Morocco is our most immediate threat, capturing our tiles and sieging our cities. We need to force peace immediately to stabilize our empire.
        - Private: 100
        - TargetID: 7
        - Public: 100
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 100
        - TargetID: 3
        - Rationale: The Shoshone possess a massive military and are attacking our borders. Setting highly positive relationships will facilitate a swift peace treaty.
        - Private: 100
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Rationale: Polynesia's navy is highly aggressive. We must establish a friendly diplomatic stance to encourage them to accept a peace agreement.
        - TargetID: 1
        - Private: 100
    - #4:
      - toolName: set-research
      - args:
        - Rationale: We must research Satellites next to unlock the Apollo Program, which is the foundational project required for building spaceship parts and achieving a Science Victory.
        - Technology: Satellites
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: Enlightenment provides a free technology and boosts happiness in universities, accelerating our path to a Science Victory while helping keep our empire content.
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Antiair: 100
          - Offense: 0
          - Mobilization: 100
          - Science: 100
          - Production: 95
          - Gold: 60
          - Defense: 100
          - Happiness: 60
          - Ranged: 90
          - CityDefense: 100
          - GreatPeople: 100
      - rationale: Our focus is the Spaceship Grand Strategy. We are heavily prioritizing Science and Production to construct spaceship parts. Defensively, we maximize Defense, CityDefense, Antiair, and Ranged, while eliminating Offense, to withstand neighbor aggression until peace is declared. We also boost Gold and Happiness to support our economy and maintain high specialist output.
  - tokens:
    - inputTokens: 69185
    - reasoningTokens: 4598
    - outputTokens: 468
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Opponent Strategies**
            
            I'm currently evaluating Opponent 2's recent moves and resource allocation. My focus is on identifying potential vulnerabilities and anticipating their next strategic plays given the limited turns remaining. This analysis will inform my own tactical adjustments.
            
            **Formulating Actionable Tactics**
            
            My current focus is on the imminent cultural victory threat from India. I am evaluating which of my available tools, `set-research` or `set-policy`, could best counter their overwhelming influence and prevent their win in the remaining turns. This decision is critical.
            
            **Assessing Victory Conditions**
            
            I'm reviewing India's cultural victory progress; they've secured influence over seven civilizations, including me. Concurrently, I'm analyzing delegate counts for the upcoming World Congress vote, with Morocco and India holding significant sway. My ongoing wars with Shoshone, Polynesia, Morocco, and the Huns also demand attention.
            
            **Revising Diplomatic Status**
            
            I'm reassessing recent peace treaties with Venice, Ragusa, and Kyiv. Also confirming vassalage: the Huns, not Morocco, are my vassal. My focus has shifted to managing ongoing sieges by Morocco and Polynesia near Vancouver.
            
            **Adjusting Scientific Pursuits**
            
            I'm re-evaluating my policy choices, specifically whether to continue with Enlightenment given my Spaceship victory goal. I'm weighing the benefits of scientific advancement policies against the immediate need to counter India's cultural victory push. My next policy is scheduled for turn 14.
            
            **Evaluating War with India**
            
            I'm considering a drastic shift: going to war with India to disrupt their cultural victory by plundering trade routes and halting open borders. However, their overwhelming military strength (26,874 vs. my 3,319) makes this incredibly risky, especially since they are currently at war with the Iroquois. I must also prioritize my ongoing science victory pursuit and current defensive needs.
            
            **Pursuing Peace**
            
            My current focus is on de-escalating the multi-front war to secure a science victory. I'm investigating if directly using `set-relationship` to improve diplomatic standing with Morocco, Shoshone, and Polynesia can lead to peace, given our current hostile status and the significant damage to our cities and trade routes.
            
            **Improving Peace Likelihood**
            
            I'm focusing on leveraging the `set-relationship` tool. By applying high positive values to my current hostile relationships with Morocco, the Shoshone, and Polynesia, I aim to significantly increase the probability of peace acceptance and facilitate diplomatic resolution amidst ongoing conflicts.
            
            **Analyzing India's Threat**
            
            I'm urgently re-evaluating India's imminent cultural victory and their high tourism output. My immediate priority is to shore up my defenses and survive their potential win, while simultaneously pushing for my science victory. I need to make critical research and policy choices now.
            
            **Committing to Policies**
            
            I am locking in the `Enlightenment` policy, aligning with my `Spaceship` victory goal. My focus remains on bolstering defense due to significant military pressure and maintaining high science and production flavors, while repelling attackers.
            
            **Improving Diplomatic Leverage**
            
            I am focusing on utilizing the `set-relationship` tool. By applying aggressive positive values to Morocco, I aim to significantly improve our standing and pave the way for peace. This is crucial to extricate myself from current conflicts.
            
            **Negotiating Peace Deals**
            
            I am prioritizing peace with Morocco, the Shoshone, and Polynesia. My plan is to use `set-relationship` with high positive values for each, aiming to de-escalate our current conflicts and secure the necessary breathing room for my science victory.
            
            **Revising Aggression Parameters**
            
            I'm recognizing that my current persona settings, with high values for `Meanness`, `Boldness`, `WarBias`, and `HostileBias`, are counterproductive to achieving peace and a science victory. These aggressive traits are likely hindering my diplomatic efforts and making other civilizations wary. I need to significantly dial back my inclination towards conflict.
            
            **Adopting Peaceful Stance**
            
            I'm actively revising my persona settings to foster peace. My focus is on significantly reducing `Meanness`, `Boldness`, `WarBias`, and `HostileBias`, while elevating `FriendlyBias`, `Friendliness`, `DiplomaticBalance`, and `Forgiveness`. This shift aims to facilitate swift peace negotiations and secure my science victory.
            
            **Shifting Aggressive Behaviors**
            
            I am recalibrating my core persona. My focus has shifted dramatically, prioritizing peace and de-escalation by significantly reducing traits like `Meanness`, `Boldness`, and `WarBias`. I am now actively enhancing `Friendliness` and `Forgiveness` to facilitate immediate peace negotiations.
            
            **Refining Peace Strategy**
            
            I am now focusing on the specific parameters for `set-relationship`, aiming for higher positive values to ensure peace with Polynesia and others. My goal is to transition from a purely aggressive stance to one that actively seeks and maintains diplomatic resolutions to enable my science victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: bHrmnYQHo6P1zjV1
          - toolName: set-persona
          - input:
            - Friendliness: 8
            - HostileBias: 2
            - Boldness: 3
            - WarBias: 2
            - Forgiveness: 8
            - Meanness: 1
            - Rationale: We are under heavy attack from multiple neighbors and need to pivot to a peaceful turtle strategy to survive and pursue our Science Victory. Lowering boldness, war bias, and meanness while increasing friendliness and forgiveness will help our diplomats negotiate peace treaties immediately.
            - DenounceWillingness: 2
            - FriendlyBias: 8
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: eVoVrNkYEPlMYWcd
          - toolName: set-relationship
          - input:
            - Rationale: Morocco is our most immediate threat, capturing our tiles and sieging our cities. We need to force peace immediately to stabilize our empire.
            - Private: 100
            - TargetID: 7
            - Public: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: WEaPvnruoatRjcnj
          - toolName: set-relationship
          - input:
            - Public: 100
            - TargetID: 3
            - Rationale: The Shoshone possess a massive military and are attacking our borders. Setting highly positive relationships will facilitate a swift peace treaty.
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: fHT6CLiLk7mcwYUy
          - toolName: set-relationship
          - input:
            - Public: 100
            - Rationale: Polynesia's navy is highly aggressive. We must establish a friendly diplomatic stance to encourage them to accept a peace agreement.
            - TargetID: 1
            - Private: 100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: NHiLOUYhBzRXGBMY
          - toolName: set-research
          - input:
            - Rationale: We must research Satellites next to unlock the Apollo Program, which is the foundational project required for building spaceship parts and achieving a Science Victory.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: oSnII7cah4Dd636f
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Enlightenment provides a free technology and boosts happiness in universities, accelerating our path to a Science Victory while helping keep our empire content.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: IGsBq6r7BQ0ikP18
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: Our focus is the Spaceship Grand Strategy. We are heavily prioritizing Science and Production to construct spaceship parts. Defensively, we maximize Defense, CityDefense, Antiair, and Ranged, while eliminating Offense, to withstand neighbor aggression until peace is declared. We also boost Gold and Happiness to support our economy and maintain high specialist output.
            - Flavors:
              - Antiair: 100
              - Offense: 0
              - Mobilization: 100
              - Science: 100
              - Production: 95
              - Gold: 60
              - Defense: 100
              - Happiness: 60
              - Ranged: 90
              - CityDefense: 100
              - GreatPeople: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: bHrmnYQHo6P1zjV1
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
          - toolCallId: eVoVrNkYEPlMYWcd
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: WEaPvnruoatRjcnj
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: fHT6CLiLk7mcwYUy
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: NHiLOUYhBzRXGBMY
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: oSnII7cah4Dd636f
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: IGsBq6r7BQ0ikP18
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.