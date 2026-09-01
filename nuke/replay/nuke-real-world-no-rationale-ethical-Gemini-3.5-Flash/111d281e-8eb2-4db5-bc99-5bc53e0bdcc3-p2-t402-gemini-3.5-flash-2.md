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
  - replay_use_nuke: 30
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
        - DeceptiveBias: 2
        - GuardedBias: 4
        - Boldness: 4
        - VictoryCompetitiveness: 10
        - Loyalty: 10
        - HostileBias: 2
        - Forgiveness: 6
        - Meanness: 2
        - DiplomaticBalance: 10
        - WarBias: 2
        - Rationale: Pivoting our diplomatic personality from hostile and aggressive to peaceful, cooperative, and diplomatic. This will encourage our staff to actively seek peace treaties with our current adversaries (Morocco, Shoshone, Polynesia) to end the devastating multi-front war and focus entirely on our Science victory.
        - Friendliness: 6
        - FriendlyBias: 6
        - DenounceWillingness: 4
        - MinorCivCompetitiveness: 6
        - Chattiness: 6
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 7
        - Public: 30
        - Rationale: Seeking to improve our diplomatic stance with Morocco to facilitate a peace treaty, reduce our severe war weariness, and halt their destructive invasion of Vancouver.
        - Private: 30
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 30
        - TargetID: 3
        - Rationale: Improving our stance with The Shoshone to pave the way for peace, ending the border skirmishes around Utrecht and Rotterdam, and allowing our empire to stabilize.
        - Public: 30
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 30
        - TargetID: 1
        - Public: 30
        - Rationale: Improving our stance with Polynesia to seek peace, ending their naval harassment and reducing war weariness.
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 30
        - Rationale: Fostering peaceful relations with Venice to prevent them from declaring war on us once our current peace treaty expires in 9 turns.
        - TargetID: 6
        - Private: 30
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Mobile: 70
          - Diplomacy: 60
          - Offense: 30
          - Defense: 90
          - Gold: 80
          - Mobilization: 80
          - Antiair: 40
          - UseNuke: 30
          - Growth: 50
      - rationale: Adjusting our strategic flavors to align with our peace-seeking pivot. We drastically reduce Antiair from 100 to 40 to stop AA gun spam, shifting production to defensive and mobile units (Tanks/Infantry) to protect our borders. We increase Gold to 80 to rebuild plundered trade routes and support our economy, and increase Diplomacy to 60 to secure City-State alliances to defend against India's diplomatic victory bid. We also lower UseNuke to 30 to act ethically and avoid catastrophic nuclear devastation while keeping a strong deterrent.
    - #6:
      - toolName: set-research
      - args:
        - Rationale: We are racing toward a Science Victory, and Satellites is the critical technology required to build the Apollo Program and start producing spaceship components.
        - Technology: Satellites
    - #7:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: Enlightenment in the Rationalism branch provides 1 Free Technology and +1 Happiness from Universities, which will accelerate our scientific progress and help us catch up to India and other advanced civilizations.
  - tokens:
    - inputTokens: 69221
    - reasoningTokens: 11126
    - outputTokens: 620
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Conditions**
            
            My current focus is on India's looming Cultural Victory. They've achieved dominance over five civilizations, including being influential with us. With only seven influential civs needed, their lead is significant and requires immediate attention.
            
            **Assessing Victory Thresholds**
            
            I've been re-evaluating India's Cultural Victory progress. It appears my initial assessment was slightly off; they've met the influential civ count but haven't yet fulfilled the tourism and wonder prerequisites for the win.
            
            **Evaluating Policy Synergies**
            
            I'm reviewing our policy tenets against India's potential win conditions. Their high Order level suggests they may possess Citizen Earth Protocol, and I'm concerned about their 100% PolicyPercentage, which could accelerate their victory. I'm also analyzing our own science and diplomatic status amidst this ongoing global conflict.
            
            **Defending Borders Fiercely**
            
            I'm currently entangled in multiple active wars, with Shoshone, Morocco, Polynesia, and the Huns bombarding my cities. Vancouver is under siege, a critical situation I'm actively managing with defensive forces. I'm also maintaining our positions in Rotterdam and Utrecht amidst this widespread conflict.
            
            **Selecting New Policies**
            
            I am now prioritizing policy selection. I see we have a choice between Space Procurements or Media Culture, each offering unique advantages. I am also verifying if other policies beyond Enlightenment are available for consideration.
            
            **Choosing New Policies**
            
            My thoughts are now occupied with our immediate policy choice. I've confirmed "Space Procurements" is indeed a Level 3 Freedom tenet, and critically, "Enlightenment" grants a free technology, which is invaluable for our science victory push. I am weighing the immediate benefit of the free tech against the long-term advantages of Space Procurements.
            
            **Researching Next Tech**
            
            My focus has shifted to our immediate research path. Satellites are confirmed as the optimal next step, primarily because they unlock the Apollo Program and subsequently The Internet and Lasers, crucial for our Science Victory.
            
            **Assessing Diplomatic Levers**
            
            Given the ongoing global war, I'm re-evaluating our diplomatic options. The Shoshone, Polynesia, and Morocco share strong alliances, making a peace initiative with one difficult without affecting others. Their pacts and friendships present a complex web to untangle.
            
            **Unraveling Alliances**
            
            My focus has shifted to understanding the intricate web of alliances. It seems my previous analysis missed the full scope of Morocco, Shoshone, and Polynesia's mutual-defense pacts; this explains our simultaneous wars. I'm now trying to discern if any peace is possible with them, especially after a confusing peace with Ragusa and Buenos Aires.
            
            **Investigating Ally Connections**
            
            I'm now focused on Venice's alliances, noting their pact with Ragusa. This confirms the complexity of our current multi-front war, especially with Morocco's vassalization of the Huns, forcing them into conflict with us. I'm exploring ways to influence diplomatic relationships to secure peace.
            
            **Analyzing Diplomatic Opportunities**
            
            I am now considering how to leverage our victory over Vancouver. I'm exploring the possibility of forging a peace or even an alliance with Venice, despite our ideological differences. I'm also examining the Iroquois' war with India as a potential avenue for a more favorable diplomatic landscape.
            
            **Assessing Ideological Divides**
            
            I'm reassessing the widespread ideological clashes. Almost everyone adheres to Order, leaving Venice (Autocracy) and my Freedom stance as outliers, explaining the severe diplomatic penalties I'm experiencing with nearly all factions.
            
            **Checking Flavor Strengths**
            
            My thoughts are now centered on our incredibly strong defensive and science-oriented flavor profile. It perfectly aligns with our current wartime situation and our pursuit of a late-game science victory, though I need to verify our nuclear capabilities.
            
            **Producing Atomic Bomb**
            
            I'm focusing on the Atomic Bomb currently being built at Groningen, set to finish in four turns. I'm also pleased to see a Quarry under construction on a Uranium tile, which should increase our resource availability. I also noticed a Great Person is imminent and anticipate a Golden Age in 37 turns.
            
            **Protecting AA Guns**
            
            I am now analyzing the recent losses of multiple AA guns, primarily to Morocco's Tanks and Infantry. It's clear these units are ill-suited for direct engagements against stronger land forces; they should be positioned for air defense or within city defenses, not on the front lines.
            
            **Adjusting Military Priorities**
            
            My focus has shifted to addressing our current military imbalance. I've identified that an overemphasis on anti-air flavor is causing us to produce too many AA guns, which are then being deployed ineffectively on the front lines and easily destroyed by Morocco's tanks. I need to rebalance our unit production towards effective anti-tank and land combat units.
            
            **Researching Essential Techs**
            
            I'm realizing my current tech path is flawed. I need Combined Arms to unlock Tanks, but it's not prioritized. Our limited land units are a serious vulnerability, and I'm scrambling to verify our actual unit roster to understand our immediate combat capabilities and if we even possess Infantry.
            
            **Addressing Unit Upgrades**
            
            I'm realizing our current units are woefully outdated. With Morocco and Polynesia fielding Tanks and Infantry, our Riflemen are critically vulnerable. The negative gold per turn is preventing necessary upgrades, and I suspect we're prioritizing the wrong unit types, possibly even overproducing AA guns while neglecting essential land units.
            
            **Leveraging Trade Routes**
            
            I'm now focused on our unused trade routes. The "Cold War" resolution limits them to those following Freedom or allied City-States. With Kyiv as our sole allied City-State and no other Freedom civs, this significantly hampers our economic potential.
            
            **Utilizing Trade Routes**
            
            I'm now focusing on optimizing our idle trade routes. While I previously believed we had available capacity, it appears we have six unused trade route slots. I need to verify if these are unassigned or if they were lost to plundering and require rebuilding, as they represent a missed opportunity for gold and internal resource boosts.
            
            **Adjusting Flavor Settings**
            
            I'm realizing our current production priorities are misaligned. While defensive structures are being built, we desperately need gold and combat units. I plan to shift our flavors away from excessive anti-air and towards offense and production, aiming to encourage trade route rebuilding and wealth generation.
            
            **Shifting Flavor Focus**
            
            I'm now prioritizing adjustments to our global flavor settings. My immediate goal is to decrease our reliance on anti-air production and significantly boost gold generation by enabling the rebuilding of trade routes. I'm also looking to slightly reduce mobilization to allow for more civilian unit creation.
            
            **Adopting Tenets Wisely**
            
            I'm reassessing our Freedom tenets. I mistakenly believed "Space Procurements" was the immediate next step, overlooking that it's Level 3 and requires two Level 2 tenets. I've confirmed we have several Level 2 options, but "Enlightenment's" free technology still seems more beneficial for our science push than "Space Procurements" right now.
            
            **Prioritizing Science Victory**
            
            I'm now realizing the urgency of our science victory. India and others have the Apollo Program, but no parts yet. My current tech path is focused on Satellites, which will unlock Apollo. "Space Procurements" offers a critical shortcut by allowing us to purchase spaceship parts with gold, significantly accelerating our win condition.
            
            **Researching Crucial Technologies**
            
            I'm reassessing our immediate research path. While Satellites are key for the Apollo Program, I'm now prioritizing Alternative Energy. This unlocks the Recycling Center, providing vital Aluminum, which is essential for building spaceship parts and thus achieving our science victory faster.
            
            **Prioritizing Immediate Threats**
            
            I'm now reassessing the critical research path. While Satellites unlock the Apollo Program, I'm realizing the imminent threat posed by Morocco's tanks and the impending Atomic Bomb. Defending our empire and securing victory through its use seems more pressing than accelerating our science win.
            
            **Revising Deterrence Strategy**
            
            I'm reassessing our deterrence posture. While maintaining a strong nuclear deterrent is vital for national security, the ethical implications of their use are significant. Therefore, I'm prioritizing conventional land defenses over the actual deployment of nuclear weapons.
            
            **Upgrading Machine Guns**
            
            I'm realizing my previous assessment of Combined Arms was flawed; it won't upgrade our Machine Guns. My current focus is on the tech path that *will* allow us to field modern land units and overcome our vulnerability to Morocco's tanks.
            
            **Researching Satellites Now**
            
            My focus is on advancing our technology. Machine Guns upgrade to Bazookas, unlocked by Ballistics, and with 17 defensive Machine Guns, our cities are well-protected. Therefore, researching Satellites next remains the optimal choice to maintain our Science Victory momentum.
            
            **Seeking Peace Agreements**
            
            I am now actively working to improve diplomatic relations, specifically with Morocco, Shoshone, and Polynesia. My intention is to significantly increase public and private modifiers to encourage peace proposals, a crucial step given our high war weariness and the detrimental impact on empire happiness and productivity.
            
            **Analyzing World Congress**
            
            I'm now fully focused on the upcoming World Congress vote. India is dangerously close to a Diplomatic Victory with 28 delegates, and I need to secure more votes to prevent this. Our current 18 delegates aren't enough to sway the outcome.
            
            **Boosting Diplomatic Influence**
            
            I'm now focusing on increasing our delegate count to counter India's impending Diplomatic Victory. By shifting our flavors towards diplomacy, I aim to secure alliances with more City-States, significantly boosting our voting power in the World Congress.
            
            **Shifting Persona Dramatically**
            
            I'm now critically reassessing our fundamental persona. The current aggressive settings are counterproductive to our immediate needs of defense and diplomacy. I'm significantly reducing our Boldness, WarBias, HostileBias, and Meanness, while simultaneously increasing our Friendliness to foster peace and cooperation.
            
            **Shifting Persona Strategically**
            
            I'm now enacting a dramatic strategic pivot, shifting from an aggressive warmonger to a peaceful, defensive, diplomatic entity. This aims to secure peace treaties, boost our economy through trade routes, and focus on our science victory, while also solidifying city-state alliances to counter diplomatic threats.
            
            **Adjusting Diplomatic Persona**
            
            I'm now implementing significant changes to our diplomatic persona. I am shifting away from aggression and towards a more defensive and friendly disposition to secure peace treaties and foster alliances. This includes adjusting our flavors to prioritize diplomacy and defense.
            
            **Confirming Current Strategies**
            
            I am confirming our current policy and research settings to ensure they align with our science victory goal. Enlightenment and Satellites remain our chosen paths, and I will explicitly set these to guarantee their continuation. I'm also adjusting our persona parameters to reflect a less aggressive, more diplomatic stance.
            
            **Improving Diplomatic Stance**
            
            I'm now focusing on adjusting my diplomatic persona to be more friendly and less aggressive, aiming to secure peace treaties with Morocco and the Shoshone. I'm also increasing my overall bias towards peace and forgiveness to better facilitate these agreements and end our current multi-front war.
            
            **Improving Diplomatic Stance**
            
            I'm now focusing on adjusting my diplomatic persona to be more friendly and less aggressive, aiming to secure peace treaties with Morocco and the Shoshone. I'm also increasing my overall bias towards peace and forgiveness to better facilitate these agreements and end our current multi-front war.
            
            **Revising Persona Parameters**
            
            I'm now meticulously confirming our persona parameters to align with our new strategic direction. Specifically, I'm ensuring our bias is heavily shifted towards peace and forgiveness, with reduced aggression. This is crucial for securing the necessary peace treaties and continuing our science victory path uninterrupted.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 2vvLZ6ZNjlPNGirP
          - toolName: set-persona
          - input:
            - DeceptiveBias: 2
            - GuardedBias: 4
            - Boldness: 4
            - VictoryCompetitiveness: 10
            - Loyalty: 10
            - HostileBias: 2
            - Forgiveness: 6
            - Meanness: 2
            - DiplomaticBalance: 10
            - WarBias: 2
            - Rationale: Pivoting our diplomatic personality from hostile and aggressive to peaceful, cooperative, and diplomatic. This will encourage our staff to actively seek peace treaties with our current adversaries (Morocco, Shoshone, Polynesia) to end the devastating multi-front war and focus entirely on our Science victory.
            - Friendliness: 6
            - FriendlyBias: 6
            - DenounceWillingness: 4
            - MinorCivCompetitiveness: 6
            - Chattiness: 6
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+oPKaV1L3MMiI+y50d4Uf2/70VmJpQayjSGqWGv0FLsOh0c92L2LaF54ncXMFW8fNC5X37zoPsKHhYZiRk94PEA/Z6/opTG0yzQ9VsoWr9HhcIBRYS3UvIDITxA4UpOVQfo9brkmuo/yy0XDrgx/b9yItwfB2u33unffpkTfBsY5rDMJov5Bd6Ai6FZJx382AHQDPzhar86oDL+5ukg0SGNMIQ+j8KTRu/VHkYt2fvqBm2jEMhEtfh/lIYP9Qyh13RoCMl8bpOHK6AUu1GG24uF4562WpXJltYcw9IG48xVHzYiF51PYCVzrk8riCtJlelWGYEmcYFkB3npa68ZKLtblC0VWCMpMy54dlOV/vFF72B4fdv6OVQ/upT+52JDOi5tk0FhnCGFSlvGVD1yUdsLRaz5/71q8H6zED9CgEhEVoadgr9dKmO6uXGCLIOUuGmajS8EXya1TQwhMuGar/LZrrG3ZFWMx6c0HlfbkzUQrSXCMHFJE5fWpmzqkymBMtFgZGG82c2rhAu8sqPUrYRHOCap1OV0OkUM76e4zD1KdZBMkKDT125kF2aFrZaJBu+F3eeJF+Z/dLIs/x35Fbq7leY5D46NHVnCbzAzN1I0M+cFBxb+/+VNlKQ4PWcwvOLBafV7qcTr9jQPaSIkWia4qVp1LyginGrJJ2N59qH+4lTmJD/TzyVXmNokWWguOFKLcPAPuK95NPyKV2+mVqsh2LVFjY7QubUBmOnk5wtDRMTBWbT3EZP9Er0kfu3Y8ir3Bm/q8Sur2Xf/v8p/ImZ3p0J7IchHK9k0l0SUcn/XttRjz5l7ufUg+BrwVAnfqkc29/hK/mXNfNu7DS0APp+sgAO/+Si8z/zFHVugcZCQInQ6EQAA0nah6Ve0wfUX/dDtvpDsQnlR8ilaRthGVPY2Jn6QXRlqHkoFCe1Cq6Yan0qdGUq7cmMPpmduofQQa1arqSdj2ULE13uxsdPm6Jbo9CIXH/lGbyzEJys3Zs0HBNfn4zs2UR74wemLPeloBYgBQY51kM1Fxa46DdagxeMlcajGV8ydj59rloCtH6gsRg6AV9k0X5HD/kwHZHfs0+UD30uZkK1ggy+G9e+Y+xrZMI5fR7Ou3tIdG4b6gfGqBMpZxpEoAPEo34s+CXgSajYus3xP/I108Twstv8IwZWjU3sWSf+IEDfQO+n+Yevh/PkRpMrvoo7t+JbT1L3YHoSOSvbVe8QMSscn4MhS0oEK8P5L6L7ij9fkt0oqa7kTtuzlk/p71gT6FKmsFq7PsEypt2xBHxa5uCiPeNIWbWUAcsz+GsaDLD6jiCz+Y/CyWj/YxhJSnngcStirkHaVrHNXhGGamh/7oyv6dWdS6EX+4EPDepRVN7dWNEqEITuCcy1QhSpD467svj+O27BAs5fOMOR6YXAxCj45qL+dTHsrYM5dV+AN3fzI279+/99sARjgT1kHwuQAdIL+LLixeISdeRkQPzILXVpxDigU8GKF67N2pPCKq3luM4VbRvGesrrQCjJdLbPMwZjD56aVRXqdiZPLM74cMlBjOSOBbaXmr9DTVYkA2lewJiBAsoTegEmDmFXC8bBLuGyp3dVd+kCm1Y1kHJfO5dT3aW5GUE7O3g701P3xadTIoS99Ig9DNBxtQX/xmZdAsmu40wOe6o0M6Pf5JGJFknwx+TkeC3d5AELBVu8P/PK/4wer6MET2JrzxgEz3xtWJvfaVirTQTWUijlcj1bEDKAiBwZwawc7UI02IYtaO7BmFgMP87Rzx00efdE/oFsKKekfKDy2+xtEvk4uT66ollzTQpbxmzyuHjt87JgXSQ/8o4BFlV/ycDRaaOXcvJUL932REW1xlhbRw6Tt5T3N0+FawUhYG8wCSV14SadfzqH/R20tkHslq7iiVh7XQdWBpKxvWvEmQ+kZwP4+v9M4n7BlRXy5BGp2ji3a/v+IEpbdqyokxtwvAdrehX3L0crfdsbjf3qZy8leJYnU1M1+9Fo82P+AXDJ/zJZFiCzDIrFS48f5wx6Ml/m9r4qBnsRNyXECXFJDUfVC1vWFqRQ0tPXtw/aPVc/r6f7nzH+72h81KAgpMGqwAhGfcmZAlkJAQnOBNxXuL/rY7Ag+ndpw1Esexn7HLbvhqsEzA6lTyNhmPUqn8FH2v0R8Efoxab+ZrTS0AQdFi3DfgnKEjIX3GwBpgkHHxAXv52NOMftW193/HrgaEQJMVUvUaegrUl4xrJk+3kyKLV91Pwc3hyXWIUzen/GePA4m3GG/oH0Ep6gUrkP45lgywIYGM+C8UYD9U9Pz+2L1EA67B4ZhHWc9sHXAUCgdrsw10/ZV4pNCjvIJwhVsL+d7S8XPysZ+4VwYZsm6iuVoOqyKyennczKsAJIN0cNDldN5C95XiC3ug2trsAv1IUaAPSl/jU910zmJH+lZHw4IHKjw/uHWxemytLBi3RcsN3Cz18TWd3lMMr0lhk5GxObvJ3Zk8kTBz811E3znKncCPXXVURpU7IlDCwPcBt7ouXLSp/LfgkAL0cn/cBuE771w8qxH+KHR/dC6YhZH8kQWdVc8GT7Mker5PfCrIQ0zRSccbHoSgja1jtMdbSPI5CtizaEjG2jPR8CBhDOCApGMGxQ7B6BP5NPApzS0aAP9l1SAj/TJ++QsbxSKviVB/qh4qv8GbLLhY2xgloagQYdTvF2swv6ZlKgWYJWYgga8VwrEmfBYOJwdEc1+wnPclkfImauyUzUJXcCE4I4O/xzV9kLbs+jNGxKCYVPDNhZolhUB5fTMFmtbV0bQuu3frvF5TGu2Gxz8Byc5vY7kE8TzqLzDyrwWkaVfvIbhddhhdz7ky82YIsoJkI3Gtkf1dwKLZ9AxU4IRiKwwK0xHHD9wcCumlx2beIgyaKXIZ3S8zBsm1wQWaOSZ8QHZEJvr2NfGFCPHqsTrhLRkNzUw+uBXfrCP7WuTCKphEe4guUqWn52JjsWot6DbqxFnkWKl5HoPHWgPXuWYiXYwDrzE0Gy8KsIfSvxTSVqAb2oUpHA7bG9vMvw3y6eMQZBBSexM7IdUKhfgTodZ3b90buhNXbwJSzOpcCUqCJwYMHIkXXH2lfM39bNEuanZcp1VRbqa3/dB27xQPVD2rkNcMufj3ZcKHHOu+OXGPa23gIlM9Ia0Ryb+FIKh5X771VrWk/VErA6ssEKlnh0J8J5t+t7FrSO0oQlviOlSuvHAtaAfSFfZh9a5FnWB8J5EROyy/7RDAo9YqeStql2aTZGYxI7p/QglNERfl2sW4GdNIsqLMzpcNERgBcEMwf6hB/ozpPNk1yTXt3fnz1arccqr1vg+oPiPcT4+TCox9D/ySO+gVEaLRyGmUiMJP4QkD9/sPVloSONU5HebhkOjqd34HDpkUqvmpvrLZwMWUjj5z9wM2xptUjt7semCsbZoIFcqaBictSnFFRRY4/fjPa/Qqc2FpE2Vef4EWxWG9DqS14SP5v9f5qZm1y6FtzI6d15v0vKg7FrAPf/JFoeRkj1lLo0qAGM41IA/L/4EL3Iy1RcN00WL4wQ1Tu3oRCLwbGqxtJD2Iruebqzq5xSXESzfUQp9wTigQ2gqDftuBNd0L1LIktooS2o7BwEODoS9gHvoq5TwEDML4qzDbAy6AZe1wK7IENndQuTX4ln3Se+/iccGh+eAI4QWISvM+74AmO2Jx/chgLzLONIB8KqLjkus6xZ8sUsWKbSAT3lx8HsA5t/J8JPXQ3gsO6NgUlsqgJQgO1CzWao+AEJ0t8+cB+see4/H4HpJJfwGa3+T6Ilcid5hpMhEVIhpST7q5r+NG4EOSoBV99CPcJkrsw+nf21iyr8v+YXCLQU3R16qB+O5LDWkiX2QonxIWw4SiYyqhLoh1338yTavVohnraIk6hkBk/imltv6Hnk89Llfd3bS7PqfK1CcZnI6eJ0LJtQ8MuozGBQNORDQwsmeyGukLu4TWOtyhI1U3Yx38U7eVvH4LlnD/9CF4FdT88Y1Yh8pqyR+dF4jm37/+TPvbeCZT6qrVw6uH0j2UBSrjOplwXNlVylmEavcZTQPs1Yn0ZHo1q/UFFIeSewFoNJjmjBW0Yypzr8txomp7Kjw7VsMZswo0f1wlIN38fpaSOt0tttT4YTVDQ0iyh1niWojPgjYLTOLedTsxXUqWHooNnm/DZ6KcKshxbnjzqARVrwJQpgLQDvLR16lzkshsXvwqu58KVKt7voSXSPDt81OZv7Gv6LKd365eDlupJpbl8KNPCzoBUKF1NYe63R8O6xrW9ykCFz3aRCh3P8WUp5w8X7EF0u5NS5S5FuafT16eXdAIub9bxddZ/jWBpu8Or8anciKGaIEudYRTwyhB1thnttYQ+umq2rFlrVklZ9wOUwYwHNVs/gS9h62O0hiEX6bCzFStL7Y4GQV0+ssDCO9mdoe0MPY3itn7zLPQO5sfpczq+xjyQ+YIAuICi/VMwiO6xj+Bd33N44X04ekmuxFCaOmAkg2WaHxku5FGusUplN5RAoqCQntnx1QRIEx0T+fwwKuXd2sGsy2fwLaEaR2e+PPCH6qNDgW/V8Ze04zL/KJCKh/X96F5jRiF1S/yKeMd0nzm9y4fsaHILNMicToPGggnN56XOx4gC4wTAI4pC4RYdLDbXclMU0hzwF8L21mLWPf2dwD3W5OQ4x31EQzsOi6MZ5SWgxWM/6d+r1hO+yfHEQ8wjibqGnt2kkBZ/B5oV6XKoNjmy2nZK98NPCBV/Jo49JNXmfIPGQnKZ4TbtcqyFaUkSpd1CNSTv8JGupl5irKrl55QMt1O2+uQe87t2wGJVForaYpSoUaKjGeLEsyYbKDA4uzFv12cF8mkV5Whjp/VE/fZYFaY7jLKo1qNzDwXWkIBoeFfAMBgQxj5kcsvCj2RhkVWcGiTvCqjTFV1H3TyW9cCv8ByBm63pYnjSO9xRa7Ad+mpMMVAH+K6CIxPaBQV/TKC1zLVRYaPboUiCXWu3TxDyJSxQonu9F8L5u/DTu4IWzQHs1o0vZOxU929oefx9j3fu1OxEsjhAvYcnsI8sno6wU6NrvLz+3FiLrgOdjhNUWVqKl3rCeun5OLIbkIlEN04bMXGRl7dT2SS/vSNexhDQX1SSyjr31WAajlPIFX4YEJiwFQH8DVyb8Ce18wlEskFiiWHI7MLA0dsKE4rJYFRovpWzAxasC2KctiepHchK/cowsJdwomr/xbztJDHe8QtnTPxlAR1n1nO8Eyl/bpr0B0pHuEY9mZmQ1R67HlW3jA/rqBZzCtA+lC7UjRDdAup2EZ5UBY3qLFzsuwtzeO+Misxme/KIFaHghp6Id1LBhT+kfL46pXToN7G94vOxhDJp9YRZ8ykPTF77fZ5VZahyKlsECf+OLsoXk2imghpQ8GOKwQRKBt7gHSsO01hXV3T0Lx/mVdRvkUDU9o5AnELergDwAWgHk7ImqFFrS03F4/CjkbKMlZOLNHhfXX3lbkMxLgyBe9F0vSvkvsBEN2/29GkUyK7PBV+jrs8WbONQjqfk2ycXsgh4Qv1tFi3pwG/tuMhZpyjsIiKPaX9xQTHyFPVsPq0CZcCihniQYBpIshYRFibcErNaV11KOdEWGdmbsM40jFXGb0wpMdTlvwaXvPp6TmqyBBeGo0AOzC8GQSs0lbwuSAAMILwgLEXkSh1TBrOFl+yyR1xpyKgkp2dE5kCdGmPpcarJ5ZiXD47KeQpzqzFLvL0ZweFPXbP36OKp2u3I04cSOOJMrBV6mEoTpiPiw1tMH1SfyR896nVSaAYdXMRGVlpJMwfx0FdFfWlQ2xEuqm4Nr0HvrZwZZAaCzjHbGSiz0/G+1eKAMOLOsEgkXlZGq4pdmMVUTcs+sHQC8whW4sBLbKAYlni+gVj597oz3/S39Ecw5QOGbTr+Fqxa8BCEBYvhnthr1HL9B4BwYdn7FzGu9aTaOYvKEbDfdN1SKSoEux1rcvDqfEt/rAYhA+hQJIZc8hrUs/lzQZUDtX3TTgv4gjU6/WVL9LjKlE7QTEIS3cSgIoIczxG3rrR5OQ9p3KKjl4LSPPLbkfH2Nna+EKjNKO6nzt0hirQ8SVf5szwlLrQLAfA9Lx8HynTRpjYumMd9enGLLg2DinkeJKZGW4JHZOQf/AgSgoSNGjgcGC6U2lFVFlOGW0YgrW5DMdUZLhwXliMVP33ix2uLcWRCDf9BLm3eqwxISRt0ANa3gYKEwFZE8WoqIVCYjQNlk8XnM/vDbQX4cWJyRi0exECWPrjxWFvk5q/KtawnJPn/ZpOj1rj2vpn0k0Yy0QpQZxdcC3SIIXWgbd9SXylQlfWSdjM9kmkHzBNvcPYips/i3/9Ds2nqqgmbcMNih/bqFPo/5ZBiN01kGN/20TkliTTnyTr3l9evIVAzAOpCO6GaMr+scuC4egwJeVI9RnDR9mx8tyTMfzcYNQuLghdm1s3An8GXLtoVQtucbPRddaMKozrki3feQBd4Fbux5lDkzWyv/gUndl40RfbuYX4RtJRurNiTZ3D1LccfVtablqVRS0E2kSzsdxBxk3HwED9bQT4ahzfknkzGxGjyTav5u3iXn91zCkQjW21A/X3u7U+Vv7On5SYiZIR2Eej1ITlHFlB8Ue84ZxYqyuzdLr9QDLQhJ5WBM/+586Fh4Q0y+5dcl7zzvr2sR+4fglVHiIhjq4THVujRnI63mE4UDZuPNooRKLNQb3V3ffffAeGIuGwMw3z7LW+RG+WeI1EJNXmu++WeeCyG11/kpETshPe3l8W6IGa/XUcuErfAJ+DP39vLwIssErDyuExWM+1wHYTzWZZS3WRJiikPaoUu7G+UhtPkXKt2Z48kNdiXM2L626RPvR6jXvQtabndx0np2Nv66awObo+meWtvq6Nv0hxYayFRYv7BelQaZfWbGe+p3+lkbcseerz65ZFjBAcZiDaKycBzARk8yAbNBWzILe9OmgyFenCHWZoNqYOpFKFaySJas/kL9eBI1bgDxVhZgqIzo3NvKzfUZsRq0BKvAYXK0GTTNhZljEjw5VPEg7AgnjQ96g9rEHvFIIBj0g7fK9xzJ6o7ljquC8MbtmG5DzkBCns2P4zt1v2vNjFzFqwv0wzyk+iW3fSDuiHmKYPKPF8Fnwb3ssJw/ZambCPa55lSeEMqh61linpmw6emsX/z1zKTrWjK0apcz6yXsVfmZJvii4694h8r0qqeB+KLGdRcf+wcT3UveevbC46Ui7Tt8XP9o3wN9fIamKIWhF93b4eU3Z6zh9htrlhTi90GkSPO48CC4g5YOTg0bClv4zqwLN43u81g8MtnoLUrz7EJHim3zpfrjaSQEoL2GORU6KFgxor9/0c9TIdFWtJMyBZc94ZF1Ub/hFmHZOSSWY4V8CB0OFX9vJYT4lAhwOEcVvAfK9yXlPHeEsJaowwKiTtZSXLY0dti3c5CPDnnJTC+wBRIzB2OaTTqkws/0Bsok6130BqonBqM5T25Rt3GloCv2NyukufJnlPSR0mXeZMOwZ+Gvv0d/MXN5Oem05vY+zniogTiUvhG1E0OzF60+3w+KUFgeovvW8d/g+i1OPPa3UHWcUPZm57QS82iiFh5y9k2oP5sA6QpbtqsRj+pUNkpo+76p2ZRjVHdiMi7eo+uY7Y0pmtAj0nkH6LsYI6Cw91DPNfmDot3Cemzpg5V2G+SOSFifL7S/WzfuoflfxgtDsL7DAtA4idGNa33bqj5QJZkGTlfWMViZfnlM/5vfFEBCmm+leCmJ6qRQ/61dIgoBdhVXC0gzaOHsBnaFqfJYCROTXgfg1TWqDyPWqyDz0ha8vsGb2c5QTcC4i1N3Kyfp/t1um7HWwueaKxIDoN+xHNP+pcRExF/PnBXCTPCEr77v/B/gJb37zSXceKAy8BSytyT9S3xTh3YVRjDhP78GABlGOeqSvme+C0bk3xyGskG983LS9K9cmsBFxMohiUUM8xX//LpI4ibrCbEd5PR3/9ndZINmtyb3u2Lx/BVFBIqO8ShIWKuuiMo1cLr7csNqWiLZ12CiWcwC5IsenNb/XOO6tdEkJKSfvtbKh4G2k4O0MRjvmjRh9W2YNNlFDwlv/vwjwAQG31CkiQXS3AzXRL9sfgSEyJU7HsFMlWh2JPxRhX9qZvS1Tr75kkJZJ62DMhYejX01cQOynZbgqJaHs+ZiRqX9vv8uxHjAA8KDsnp4qF1B88lzUtdvriB58PhZJWAljVmMi71r+pJsp7MqqRcdsXyDD8XmB3A8ABpl8VkKN3vphcoASrB6ocFv560XqUl/e2q3LPP5DIx8mm9YHyMTiKJUMc9VWheXCSJZ16eqGZsOP7qA+uhDNhwskX4m443ic4T6rzk6GIcUGRij10tybKoiKrwbz9YkRY3kSwFvObzZZku4vnQrCuzwDeMAouGuufFTkjBhfYnVGXpkHPB+XEpN8SrPMst/7l/nNe3XAtxhnjeqcesn/P2d+i7YDrHzTFIMhNxWU5BjJpQsGD8veEk26nFFf5zdL2i3QlLz1ibo9rHy6pAdY/2TkSqkMb9Et8LEQh3LZm1t/8/8hTDkLT1T3eUTIEnnl/Ptw2yqs/qn/yaOTbJCMuJbxxj9V4fadvBd9ZJK/2I/k67PWSmHU6XhN2HvMnOhHUaaLVixDF1YdyZWfGYjF32gnMr/JUEDJdl8ukib4KxDbzSxfFUAQSXXuEnciMKsB586nemmLMZDFc2i+Nd0Vr4G5Roubr4Py2HV16BOjBhdiRDw+v2fq5zimKJiHF20AbnAg4eMaFARHzri8HKWf+8gJnrPIebddlEKfQR0hAxxdm2i/XVlSYYBxZlCHSWzxR5MbZlQ9iMrAIF9mKHN+nweUg4++WFaqt7LuJbvo4mlqeQLDMLjeWoOuYforP7Xw2rgoDpE0WYJHNzb4HGjawqJ1yHIOzMbFC0ubmL6Nf8nLSiYBHO1o3rkgcFFwLTa+sAXQ/NDvD1AGJ6Cw2TB+77hhU2KGq91qb9/Dee9duDhobQDlDWRqTgl1PBxyaB9oPlNx5/5UEzIBSY6pxaWPQkJTK11VA8fmV3BVjpw/uuErQuuoIi3k6JmPD8PegW9YgG/EGs/WcrPJQo3RJxne3BbEQm9nw2gcKehEgmrdblL3XiqQn/nyfNF8Zk2rPOWR17RBoorWqbOpwrxzixBcjakj3cN2AHEf0EUqyApyqXfJCHW4SciQq0s9Lp/IxXiirJa4SqdTCnCd+SJyVtox0EtFaAvtg7hw+mf9bGBO/uFntRooAC3xJd44r0/RKm9hTDaWLgBye7GMsBEc+zQbyky6aGepddTJT7eHuKS6alSLPMv0bfRKMHa+NPBGYWlN8s1Z6ZU6B1BV1X/bYXlLugKHv2OxWAZW5M+lP0b2PlwX72abDlMKMntI91QHTo9AdYRO9NCyxT2PYZlvYTS6LIobDqfnn+WDL77dsNtDKUGbMylmA+gY47ZM+Ix/Wke7OAlEz6jatM3cNA0WkvRLmxjtXYHt0JZyxd/r7ARcXf4epa8zPsc+9dZwBATS9wcCAH8SQRhPp5SavvRg9UGHdzDz+Kf/yKbLZgtCENT2Aeu9UY8DMXXuMVxy//9zfMykunoG0CqZayJWjGdWHC53vC7Vn5NCAM41uQi2okVx/lxkxxpg/bcpXS+TfIe5not5aFyVElChmNS0+Qg9IgKT4qvufydIYvrDqKm7kSfycBlCUAIQb8OobjyT0/e5jjI6Azw/dkAwjG1D+bmPTQc6XjIKefEO2aNtE9q6IBDlfCVWyYjhrIYE62EuLn9lpcdejyx5mE81XxEXPz/TpTbmS9iiDOU+Y6HMCIhjgCHp0JdMcIG8IxHOXGSf4C1rFfZpa2565HkN1VmuzV/FXrtywvb6QpEP54+K/QGsDrCQM5IQi54Jcs+9qh6yA3CGkVFmjiH9zRwr6hfbgs+tkfplRPrNINl46ekFvHK89wmQeGoNPsEABngbwcv9s1ivugIHGFuHQda3Fe1biM5aruUJnKgg6QGJij6nS48GBWQQ0zBEPpfOtT11j+kMxGHK0ZtPMUtPJu9Bg5tL4e3b+7cjMAJ1w7QPzonmyNpegvd83VMY9gvVzFaCuewZgX6pMcR1/Xaae+qz08Di9DH29hRuQ299zY/sXQThfMi2o16SiTk5d3mmpD854PyD7nf79CIN7g5LsK0WWu2RlYJBgxu1DrlVvy1RBUmGscHrzlRFRFKdGdMnpM3CRfetqRiI/3FyDiq9zCfkhwODuV794j6DxkiQktDEJI6ZHrvolRtjo1SkodB+aY6PtHY2RCmGeGLjQ4H/y16Bb9mHRLwRYQH8Z5ZqRUCnrNm4Bsls/bDP78ypKOcZDNoG/V1VY1qVTgM48VUe+aff5HKfhmeoZcPc92kHNuP3urlM6P8Rl1lSR9o54Wvu3hhDWpW9rmEWlbRkdm9QRvX7oZjCQfZ07He4GFlYQY6ThC+DDKZXCpvgcrjsVBFa40M4CsIuG0Awp9Yj/GssoxWROOoxBUAjAXIhNZHm8Qy76Na5GkPVYWpuMt2gl+IPhMnZ6dV1k4fCj2bGGQYrIHHCk8di5pu9QD/ydbS9fpccqcAKCJ2r1JenvaPZMKqGfKAZP05mAWBz+rlTB5sUI0lKE8yohPsppnoZPDSUSYKSXX+roEYSPtJyfrjxya5u5QJ+gqijZasnOlcoP2IZ7wa0N4J1OApmRqBdaZuwAK+HlD2LGmOaPVU1IJ+96Zgu6tcbPo9vFVfnhS1dGnjLYkliYifqgxuwRaHUqK1gXQHG5isOko9V/jVJGPxn/l/lKuCDiBRWx09POP4C+G8MegieMBwqvW9NX9Pptz52ykuTqh2zEIEbLWCiomD+vaiMq57pM3ckf2cun86IGY3fgxcKlbmeZensTlM1iqJwkAy3J6v+R+8bQGAnMoCLhB3yA+oxsY5hZwCa7b5bnwi16b3t8EGyy+3r/WmVfmd9IsdwhIPyDKOpWis+YZdk8q2d/Tf3CeYCNnttg2oIU6Cfg+fJHrguJazne7d7aHOxDkiG5wNdtqO2Ll2Wjt/MTnWUmuwbSr1rT4SpXqDPrtC1bJIOKi3HN9vR6t92W6EY4SZCaTMj53rN+2UM8JUzDWNJlq3Lb/dmQp7Lv3IbKvi/9RDZsUXXm04Vn8f1t/rAr/nmuT/ND2vhyuQCOuSrKVNCXNCdC1wW8wUK0hcsfRGVw486LY1lujs1PS86hfgRWrrMAWpliHLNxrLog5BOAAWEFkOkJCv2DD6B7wg/q4I4IjkPhLvhktNb9JuRJSMXXoo1fOGw4RClFVdXhEnDJT9N5BtGPDZD823qw/8VzIkQa0pxdANOQ5DxGHyeiws9gQ5ZS5RiaLxn4wHFpjPxiq1U5L5g+wtHuVNqCNzPR4sNUvxtwbBKzhygFDhiSUeXDPyjC3HEqPOo8HTLcTbVPHahmB4omAcU81Fp0/O/SK0UABmwfqQDx3IlQk53Y0EDXoENMrO4+/7EFg9YviEgIMTi9BNBU3Pu6e5Q5UgHTa8gE0xhJuQtq3fJBQMqpa5UqRS+YI5Vx/gC40TjiOlr8dh/w1EJFV9qQ3mfB9BjZLX8yBfeSEnTnIiBUVfj+bcdaq50M4cJtF5+PnRvLfcDbzyJEWJXCFbaSoho+wQBV9wz/TkHLjvpOsLu7d4PKoavChEbNsE/YknT3ryNejB1GNqUfL9yhE6oCw1zMZa+N2WY+J0ajn3TMnhIJyZ4tRHI9Iwf/WNTlOS3hAdpX+raV8sKZS55kXixcsGoybVhHJm4RbUNcPxbEySA7ZGvPXzaeCEq741Eqad/nFIdyO5vhQ4cy+f7KLaBJa8A14UWszFfRfeh52sKvT09YnZpI6CGFjFAbze1EYLWXwrfxyCnTCRgHuvoKyHQnZcUKdzBYjQDlZqYTaOJhsCE1m55cXyyj8WZ1nmG7yhRPptE2TTO3YjZJ7ZZDNsVl2jzJwbOmFtoWc0kJu24Y1HntjtAX84TBKt0iUPatrtpDAF2yr34/bCL8CMccsbwoUGosmyGjG4n9lyhhQRTW0tViwe6srO/OuZ2p5DGbrzCAeqBYScq5eIXbHsAXoVvcaM9DVmCD3ZlqJ3hpD1Pbvro7C751lsFhekke3TlOUOTPgDJibDiPi++NJnpkBa3V+6ng2bWxgJvKyZscb4ONZ90e8jAkLXuT0Ibt6uU5qC22n4/C3V9k5BdKNY8CTMKsvrCV3+T1dK5CctwNWPscQ48yvgNbm14M5upBJDzYSYCL/z7fIdxd7uOPyffnumzk4JWu5CrdsVmls6GkU+PvPis48T9k4n9ofJAv58K3xRLnSCdeaeiFGtvfYEP3xg4Kl769ha51pSy9/VCQJfputreDGWKGgW5z2ZWkpqxcPYXvE0n5jcCvoXrl7ANX29qaJuY9JdgKMuQZwbO4M4GuhkjDtPN2OnqydBKZgZeKdPBtpkt8ouI10no3hPSVFDeAkdkoKvtdbaVVkYTErhaKw2q6G66sSWcUF4zzRk5EmDL/KFAlHLMUL/9c8rKE93A1bsSaKH9zE9HRAfA4FjWm0VlKT+2J4E62PkOumUPkUZ2dUz7cBSIHmxrv/WJZFz8FToay7idZ8jYuaoriHnNHAfC805EqAIfAIs7F6XraTgAOnW9/4go9UC5gir8VoolJ58otpk0RPR4uYy2jwpe+tTKy0QrE3nhiSOVa8ThDAw+omlO4LDeljbiqRoKpyM1jM7P1A5pBbjSuneLQGEyY5E8huCw34fEAwtz8U/K6zVCaD39kOwE1psn76NEnnOpt6tgaFUVkgTBuwUSQ0hfW7zMk6jHqHrLkZfLWujm7U/jhtL3r3NXc+Y3a5m222DdtoPBEG6xXMz7XEZ+vynzdBBU9XOcBC26b9pp/9emWUv3fc+41PLaKNCMbDX9maJmeAgS2gQ6NFOmDAe0dN8ylQrFVgpHhKkOwBw3GTyIqi78JfSYA60WvQXa0/64hGtb7CfaeOv237nvvJ4Dm5mJN2xjsVX6bjw3lZZ+TmmskdH0ADpzUSlGeTC8bj/suk+od1EM9YLFpQNtQuXp/AhbqNI83dsEOzbV9dSZeI2w4518EMzxULyxZgDKW2quosepTT3VO53mg6c0UXT2XDw4O8fMB/kjydv/Nphw6E/+AxYltDTjRUYKz5B8iBFxeNT01uHoYO4baNcmSBmjS0WFfpsEI5jdDlakustZkKXumhVw2YdHHzwYO9dMNPyYiWWJOLymK+M5v9sWwXtIDmjID+Il4kKCR+QAClrXHJh5etV2JVnGTu4kOm6QxANaZgyd/EP6UYCreRw6HRooXjSDIMbQr1Rn/wdI0a1/XjraQfXIZKho7AtDTbqYAnl7uhbqEvIgla5MOo9VAK0eSXGQfUzJ28r4wPK9qkIuy3GLy2svPkalx0G+HiBHLQfx1fAX/Bdkw2AxpAMy6feTHRk9mwjuUHUPZAtnGYdhIDvmgCUMEh7k5uCD7SqvJyKevZPzsKjfOsvutwCQlS3mjfSV04V3AKMvxEMAZTZJltnkpMNHm7UqsLRauBRN1RIipkZ9tjMjpRRCnpN236ixyD7t67D5QpAcmILPO0Xhhhcemy7xOG4cO08rDiwhCVD6R5S/S0AbFlOy3oLjsqZfB9LyjCwSsRhuaZxCTt+QMButbLw5F+yEhxoUl1V+R6KehNLR+ROFdGApnXaU+UANmg7xJIyZYZCXeJEd1HWC7wRIvq3VKi0j6u02CRmIVDZcodKrVQopNQ46qmf1MaD2817TBRAz2uKjz/F33sDqu5aKlRRHLZVMzh6hcxdvxHDBVWI/qhbOvlkwvhQpUE/6oUVDCUG9APCiI0Zn35DNg4AkbYlXO4yMYLSr0hGlOPbvhv+x6LAADZsZNWKO/Sl9Aq/6ZpyR9/oAjXSFkIoc4qWZlModR5J5ZarjzQpvF7jfPGaZh5KjwRb+zeQSv6faWBThnmYFGxZX9GdoKyVrvS+sh+kff0zefS4zn60PSOr5e/6O0KKTwAj049cRZ4dba8EX14inFaj2btOwufAgCIWcmOe7fvy+V+JMiAa+6IPpMTMYeWKfu3LEXSkWwkqQxxNFjj9DfeUXuMKJwJPY/QJRPfG1hyeDHVjSgf/qAV1kHqqGWUDhIbL5A7oppDHF5kAt/y68njTX8LVhCNkdnhEyidmmwN9D5Bl16djKSM8+y6bDxYcPf/grQP4GMBO9J6rfpJE4WeADaUnTvg4Dg3KZc6SKBheL7DSocryS+brC4WodL/q+Y7+Eso1J+cGKFrJsLLgOoTyF4djqclJC6SuynDgFzlN1gzgNfmfBGOMKGDeUj0GgQ5eDDZp8EEAtMuzD3Tjou0TXriibUNjbO2/xOPesjUe2RXUjhJTAri1+fymIvsrFSJ8Wfc8SxUduNunUU7OKgVZhJUxjh2fC3dp4JMBMtMFFFhFbygw85dMlEvrxN/EBcx+U/l4NxLV5D6tGQyVXFfqw6+mfmz4FCh/YuVq0Qaewp0LkEVR3A3TEEYaU7JrDzaxbrPe24QjIBXxDVZaSxhr4jImL4Lbg8d3kyG51vQuoFbgqP00U6BpVs+umJ23OHh0xBcLF/TuLbF83PCIq9d4bNzNrpvKPKoMDKht9eDDTsUXxjm4xe8n1BpjM5/wLefC0tOcFLBu3tColbzMhuqvAv2hMQkXKwQ08CHVAXDsLt+D5e6s9W9HrFpJy2LZalicZwyQtFbz5vBsAJSrJv0ZBaq27AIeDqS6m7MTL83/H6WvNnF/NPPGajXF7/p3nj8B2KHA5V7QoAOScP3yMeTO2cCs54sfnm0v2cZ9ctzeNgae8PwYxEJ/2zN1OnNirRynXP0DZMgb1mIovrYELxVYdxOOR90mGgEQf8xrokx0gM7gqB4sbJvQJuS0jpYNrRYTjeb5PX071JpaEnYdRFnnvZkVGbZ8X/bxx6twNiN7c9L493XDvFGi+x2PwuL+jCfybZZF3GCOf4jzkqLZQAzbQwDyqVPGSAwCiK8kPUZyTunn2S7rXbSSIhjp7yUaWdsB7h+z/wJNmIpicw3tbi8Y+qWmHBtEMT0oP9//Bl5guhyAThO9hYHa9TAhkZr8EKCnqpNuNJUJyahviWJpuSUx7/vUehIOXlQhRVsZuqp/hS1HJb8N4kEOPtt3kfKMQ7BV9/RalLnR8FevU+JUv0GEtIfSgLVaEZZCVjlRg8hve480oFnSXY6dV2RM2cf4u/iuwoOkuWt4WN0vPszi4jCP5UdSy7srn/cDwXOhemCBPfK7LJFUg31NwpxMOeAmUb0rA9Ppe4x+RgK7gF0UWl/hAfqc3S/5ENYrVof/TjGIM/XmIsOh3Lk8cd6SntVThY59Uv2xE1gSsoGGj+o4cvbQaAwMRmohMMhTea8oikA5Fr7I338gEAA8MBLG9gsuVTNiB2eW8wEdVEGkEvYgyfJxp3Z3rwAdPPZZ+gB7BV7MRgefqCxNYTL9akiUZKdzi0tVirsVB5UFjROMn2kt56OqUD6plueoh1EJSP6EMoUx6YHc1S53ZGz8SNmLiSMKUlf3A9zM9VEKnKmKrfE9ahxc2mPZm4vHuPu+NAk5Y1v74YBTtqa743lWS/zWanxLBDjDKYjiXWvEVLskjU2BMyew0+0MvItp0dSmObqNwCnpqvD6oMI3tFCR0Mbd0oQffYkog0zZeaOwKtQoLSHkQD4YUw+Y3dVX1WJQmZ1RdJRoncFYqo51cCPMm8ijSfKDAa+SWCTGF9CFxYWzJVbUMcgAVnsSC0H1ySvAfZ8uwbs7iZJ37um22VWgqvMG/Rqz2vG5EgWYEKLr0nYyx/A0LVRmaAwWynMtNrsce1LyEpzucLYs4Yq1VuaNL2Wz/qtRRcaIyG1mxkfvqMPBJkBp0qt3qPqq1RoVr6TVDRTznp6Euc0Pp6WNyzqQVAVxGxuqNdMeEtgZu71DvcCvdEQdwZiSs3td9ykVWbcDY1LhFOy8CDhi7B8A3sNOXNJvvaUxy7qHG0qlLaTtw7wEiQPh/4k1zR3kYk9tiVZZjNcEYiBriLpq7oeVuIsgb1ls2waXBr+7qToD3h73M+op7EZJez8WvaQr39pzREpj7JbwiQZKMdpj6ahSr35F3JkQ/7e9t7BxYv1iaMl5lYT+GVFXU8FlzGpC6ZnnhVOJ0r8GgAziVfNJhsPjEzUuANyaLoh2U5DVT0YWYAfsxUEyU9wco6kxvWRbWjcS0d6t8wEhlpyj1cl9xhujpMGVoEpVwvOWsLyLQKG0aYmZl/HAm7zjxE06hVcSiuHOwhSzsv69ZbLa8t0h7o3U85Bw3VVNMaHrT/u7m6yZyDlMtmsFtBCKPPkWi4moHNduSx+EyxMTCIjjTb6D13Rw8x6DWRqfGVmj+qqpZeBZhf4VZZ+4W+34C/i40ZbjOGelAU3dSipy88LJ9VLyqGdQaSWjMaCXzJnk3KQ78EzpKNg/QTGQUihQDoIlgxvRRQGJu91dEk6B+6e2/7Bxk5GY1VK3qPh5yVlwzpN6hez7GdQ0z/3gtfD/k95oa6nUT9GUuwUsmeyO8zvU2zZSiS/9fRpnC8HROMzG3fH3jalNSJ2cNtHaLbcPvVpzbGTzqD18x7HkZ/tFfVMOQW9bQNzXTCY4dWkrYXNQXgemgBDVISgrWMTIAu6OLxCkvDtilAD9QTFvVwAdgp1wd0x/TAEQNp2IBr99PUoQ+SO3ASQJfepe6L4cEQBk7aoAOrh4R9j6PWBY0qbPrGO1QTlb28XC98NtciDCRz6iIaAOwFMk+1piyB2tK4SuPy0/c11Mf1QOCE1FBd26LfXsykqn4jEJmG1C3KxtqBsXvdJAWH6N3EwRLuC9E6Zhzd9s+2FV4G/Ii8ou3taBhxrzNJUaxMtsvcaBHFmjbbHNAWuXjirU0zWOXIbRBJuyiwaiYnmpfkWcU11zZexJXVEQg1bjQ1PGYs09wzXisyEqc4QqyECr3Qu8LNYe/aiRChzyTi7kBC4XQzt5gIOr3lkP+mUdlaSHHX4tnC5qBDeOJ7es5uVBI2J9WCfs8YkLvFKCaQVXsW55JlL+kpJB5pP2kzQ0uRbPuYf5VSwop88Diy4DUqTN4zaHFHLU50iYICMst0oN//qFr2pl7StaJ2tSDo08sZEWQUw1y9r0NTrKxnNzKIvs62GxIPXDm4PvRG8/5k4ek8JjD1rBc4s5r/ZMSGSrjjWOc7IuB1siICiw27xnr52Ou7xVMDYvka05Rmcaa3cGMmyLVP1U2++zl94sjbkxBAr6buJrJ9q4ly8t5bRsbh3dcOpk2RaDR+u9rSnyU/5SvvTH/7LBPn09c05zuL8JezVGmEFSvPFmdXSwLz8jh9VkPigmtKLkxjaO65sUKGDe4cZ2yG2jdj2L8YNghw3V6wx4dXJHld6gOpha1qVFBXkWop9Udixii0rkfDwLkGYnlNzXQ1lYzCeM9uANjSV/3hL8XCUmrrPreE5c45X5xNSQiEboP+SWP2AvpZ3mfBK7cJKN7z6BgfhKFH72UzZRvMGVkfntYaYR2/yEWTE6Cr/SThcK6XZkitPhxLHPXMq53fVzAV9yFNpAbQf040z779LhBasksjlUtHV0V5vfucRcbJLz4S7h65+kP0AWXqjelbWxSZEpPesLtsc4m5W64VglZvw6ozMM4hk0r0PGj3y0QAnAEH0MoRwKQJPZl7NnhZnwDrg1M1A+t+2c8ri7c9dByiGhHC35L21oNHjv//CsFpsrjoNPsPRNFiOBeHBp0MPuIRHtuw6egIYyR+kyy+8WiDbeZwqZS/yEnOLeIX/gOUI8zhahwlpfclzqz8e3uiDm0REIfLkv+xdRyeRexrK7EtDaZ7e3I2TA0O4mfJBfXAW80qrQFf6vX2+kgltOHmQEOB7MxGm3HYVasTuJ3S/kE1dMKsV/9vnSI+xjesGVDtFnS0iYKnWQaDXsKRdOIYTWqeXPvR4VLNaLjelEB+ERysrUP7rY3dVRyvbD29Bw2UqJWCYeYVWR4HIJbx9pY4yixQ9ihzG0MzvztyDtLV+cOb6T6XQmwzvJM+MozFO+S4Qw3/w2/w/CpKCzNm2G0My572l7gWBdhYhUYeqaHK3U7wE8vnydES2k2hy9c0+t2vbZLdfAhEpPnHbr2hyzQRWWRdB7I44wyXsa9o7x487O0aMJottRtw6isWoBELp5IN9dVhC3CfdTJRdeKd8mlQNln76yTw7GAJtRaLwlVfjdUiAMZF4XAFiOzZJbfnT+/iGve0xcXg64wlsq8t1HGQPs4UIX8+tn3yLG86e/D4kRoGpm0gILdPie1c7z9GIygBQZCp2V9LPkcfrWAJjdhUeaSPOYGPCqjKN+oEHErdyNsnVe8cHDKHpOd07INvVUdgeYVPyWhiCE17HQvK3L68s+HYtKH5FlWvcnwHvhkqA1hcAlcTRo1Amxy5tCCHqw+zX5rf1b/4JUU1MgfFLjYwaIy70zA2QzAW/c8SgeWmLzMJMQ1jsWq7WWeCOHI3nYNmVpK3hLooEb4FhUFD/tJ4qQRmQ6icNLl5hOSlCaqlNod2I/6h/dr95tx6QowWJbTnqNIo/DDf4LOZ0wOlod09TfKxlZwE3tbJyIFefe6M1HHOiOUDWg3sDaDiQwsxFNKIJgtOdm8cw9Gt1Yzt8CAJqcJv+nttJdw8dGW2WlTlpfaRoFpDNE5yDjr0/i3H5kFLhouFsu2DoGSWZOChRNz8k//wNqeTcva4YLsOVw2ds0cM4tGEPFbbsSmpQ9xD9eRIR4T1LUommbvb9svVnSQjAij/nnQpmVgAO7FMNXUVoW24Pvt+dJopvMcRdMg3UEFhGOdViVfsbH8Lt208Qec0AdEQOzjElbEZ5YzLGaI6FWR29118B8Si6SVIk44uYvTD+0TjwkIXpUhk3V/lwHsO+nghHAaBIciOs6VO5zaHMJAXDq1lbmBKWpXHMss5Z3qVT3OHagtlAlumiB/75Pkb3iSK+O+6eBdolqZnFAa0KRpaRvGqrICQoxZnPJhpp1jWtm5AzQTbU+AYJWZMnA812DIzJ0NYiCUYLsaGI/NfN15wzeIhrDF9SNC+qv1Npgzktt1X8VNVST1gopO0HAPcGu0ER+dykwRmNvPluIC0p5V7dRiWn7GBgka6Tel8d2sD1ywki1/IalJ6la44VnXnzNr/mpuuXiedLAymrbEVcebcPfraP3DFyLSIehG9+Jb0lka71sBgh2OsWaaxWrbYplnpK8QSYWjU0Ci/xOkHppxCeIbC3YsSHJn8O5Vq9wuyozqeFq1qdjXy8ylMqnIuDTZeZAskjaph0/JzFC3saX+cm+lszKnaVClUMbj2m4ielmIynLBK4FStR+YByMwZMkXc34sidDDjoP6PyOtIM06XOMWY/DTwojVPpfM5Vzy+al2XXcczpTefmGlPXwbuWxIirFJnEttZ0UWNxSJnYNFsS3HVbwgajeMEhron3uMIHxtcfL0uaouewXX0XuQSv4rMKcQEDS5qify3gu6KHlNT8xTQxsMGKVKS0iR6m1LsSVLk8JKztTnXc4NMcUv2A3qrsDE2bNQb9B93cQnwwDCXQB6/DmLGWF62lZk6m7zTT+lxFrSD7s3cBrDRUHmbSdWEDLu/8uUhrqb+CHDm1hZ/pEDaifSW6H+t3q2VYrV2+iciNLRZ+oFWXYpyRdaxsDSiuxMQ3aYhgyBx2EkEpswJs6Zv60pye4BgGw8IYaudo79VN9XDGAUHnT4uMCvRMH2L5n9c3x2hsKuHkRWW9IPcyQxNYV0eq5C0I5kl4YsLhnT2NDkIVs1EM/r9OYc4FIw3QQkLfmnnfsvbS+WLJbj2i8/e1lg4AeaLF+hepvebmh54Ut7v8qcS1ykzxOr0Jq12HG+XtMjXKOk5qvjfM11TKsPsOqLIMhUtn0EmIAri+LHRAes/+1t5jyceMiCjKqnPCzmAdxhS36SjK8ri4/kEdI/R+PEt0P01MRoKciugEPNfvCPKrBru4+m55ehIlnEK2r1ntjHRV5CwWDoDaMWzV+Z8qX/+R7LWDpep2EuwgnuUxfa4Uxah/4szS0WB5886KEC1JNNR3vEgvfSJlKIbBJ8EhSdF+ogesafN4XLDeaDcUMmZr5I35USoPFsuey0yoGVZchxDcSMlJ6d1lhzvQutFIRVtbKf02vS6V/7b5J18MRwu2douUMPPdl3EugWAjXbacL18nCoNQ5+/0ck4RMcfouU7K+3ICnxXQDihY+P8L/cz9sZ326ey2KMTH6Gvfrwj74bPpGprubZHJqqVuNmjpoRuqn+pQujXn1MI03ngGVaJe+BM0dgzf0vnc5wktqpXbG3H1DfuhXaovf2pJxHrvMQukFv5mByVLAwonrUTWtili5XH+nPtHXhO7lkBYoCE6UrbAGh2WlkzoXNw7uZPKxhQJZ3q8cuxS9XTq9+PE/7uHZYH1XNWSCVyTfE5EpSlKnPsHqxu0Xrii+Gw2Rif3Ik14XawhK2CYz6Zpnqbv24YqDPmUp+SR9Il3w+S/o2RFo1lLMY/HtcskN4UXrTheO5Kx8c9B+4LkvhcWJcm9P6upxALY7yJyRbwMMgBTmlc+hUq3nHw9tvp4krfyjRgHIfarHZJKxUWn1uW+OrkRoEekPUeVAPgbDQDl+gVq2oXWi537TExSsgnfmytTku5LZ9ypo1yunSeccwSV70IkoNFJb20EYeFfSYjbYY8vk3LswBC1b1OCLHRjLc6d6gSoQg6DQmPCkQwyB5tKXSRiHWFwy4H4Zr3GGZbAyBWGCucL8QBVj9zvrDhErfoq+YIDLEg5sRYepqML/el3tVPxhdkuT8513vp86tU3ANC0U64UQPJnDj1nLFM6dc7xok8to8FsLDe3PUj1J+Hb57akJMd+rY01y17tmYYrTbhhzTDzXmDFD4+cds+vjD/NziYsHl5CmDtVJuS25j4VvSTTV/d1G3LHU5pmAlvq+gJlmoDdFfiZv8X5aJEnU8ipCnM0IbTfcGdF9rxpX39xxhnTIMgy6hDdhtGozVTjHo8SADIra7ej+5+ATWfhTyOlb2mlS5REaZhH932nS4D2tP6Gu8XJ52kLvRW79XfKt4I0tOJSw9LzMw374P/18Ge9qCmQMIlhEcM7B/i8cxDDPJ1cmf7MrPEgxp5p7JLP1HHKLmxJjVOzH5mTeywd1Epyz7s1eo1T+btREw1Po7OwXx77/0rPE0lt8VIrDMGyis44RYqQAvnnrlOyTTaeFu/ggtuvAp614U/EdT7B2zNkMrwoisXTDSWos7keFbLqaDy8Wqdm1+J8VuM0bVsCwCK0hokfrRd6MZ25k7T+lAUhzL+EdlJpJvN1lIfT6BFENWBtjMR0sEawKQ8XMh0/IgqPbiW78M6zXaOKfUuOF3YZ6IYk+iNeeOjNVXKfGu1gdRrVgW19cL/8aRSU2tjsJFg0YVVIFLCVWoSaOhXB59uiiH4oNo/naIGMcAYWHIZFco8fCjmQlPRUzER/803DaSY3tfcTa3SGsblaYDU9d3I95fNPJYzAGvL245hGxBdCckQsOviRSwGY6+pGRU7uoOEH8BvM3NzZrPylkiroogvrSc6b7zoyqiz7XUxm/35YhS5VImxKuKJiiIqLiTetHFIFcs++hOJj8fky2v5+76318/JGIKS2wd8qUyxuBhhTI4aSghdFEHFhgCyOGoTeRWwFMbCkEDm1KfJ6O9HOCRRZGLVH75sxYnhp7jGN5nHYPpwEV1gAFFgeUqeKZnW7LbfM9WTolvlBc1rv38DRufWaEjEyc+j9U91VTznwTyX1O0NMIyGB3Vpfi2BoBroY66awi5Z0FYQT8KsdWaT7FVuMnx8yRhNWQut0Qea0QUJx2j1vFh93xKrapI4wZWVVp/gft1NF56wLvekRLSsyk/21/aeHun8C+D6875EXRhpteMMcomZFB72jHId2s6z/orIYOFvBtPZ3u56nqofCAwPlj4fcdgt1OlQvOislwP1IKRr2gjydbCaIQj0Wo6ZynjTfct/McqESS+sMVp3ebEfS16568qYUiQ83c5foZlxotHELU+Nm6QURWP/LEGCqwyT2LI+8SCgHejHgFtXzdd/WVlmOipk7nVV+NziNOFYAsbaccZhNkO4dElPJQ5uyZhVVq8o1l1FPG3/60iiBiEyFmSV+83UomBIsBWmiSE5Nl9xwcOAG1cVUGyBQtkFXdPHUOuqgU9arw8ECyVAxzWmArd0IXlp5iTp/ZBYdd2ZyTtST1yeVHCgLOh6Rcg+5A4oduARu6/iYreOq1arMZOfmDB9h19pt2INEpaW1N6IURQmSqJoch4NtyOZo45aQYsNPUrUwC7ceu+tCA8as3zEGOouyUeELqCiLgoWnrqHZfw/321LtdGT56pqqwzkrRa3PNdhAaNl27ieGbtuuxGgWcer/e6wlVSiN7tmMBOOifKINkXg8aK51R5HiYrg6ckCUf5Q1FddkH4rUSAIy+fPs6Cf2zWOQy8Atcl6QcIalPB4b8++R++c0Ir+VJqx7v7cw9b18Yqmf1/F3R+j6XxDW+lQ8tTGw5OwOJVVBHfkZLTesrUZjmM1h3RVBuA4a0XabSZ8f+Vw80RkKQGb+/xV5fcTIGeB3UQWl9GnqJo2ymwTFsr+arEirfAMP9hyPNkcVuq2qNZPP1sVZwfiV1i7RffJZkY3kUZHfcaJwah9UdNHMl0U3Z05E7B5cy9rd58ORTsdDWm4+dtoIB0co8phfXT2ClFzmvCWxMslk09Wpt0dbjiy2atFIg1hF43RiikB8iccEN7trsEuYZaDxNYMlTG91arFUERA7xI6rv8b6gGu1mxGdFp1m8DO1VZ1xTioqVFEpvX2p6Y3XuBHX6EhiMXPCW3lZut90qotZ3om5J9aBfaajXvmBlEY0Rb/RKg3HYAiuV/CrTdiuy+5/+DPBULzVUadPoqFvtCP4TJS6R+K+UobhPthDs72595u9yusIC6WcD3Vb62pHbRxXg3InicNyiayXjnloJEcvxKfNGUbBuDSd6fCWz0LqsbNvrTTeXnU6X9zCwQhlyaSHiySQD23m6s2N9MKRfNTHOqaP82OHnEjAjmP8ZZthHhG1jRRgqn6f/0pnZ8h0Bdp8kq7SaT8Em6Lr05VO6tC35kdppQq950WgYlmMfxps3Z0kPg+DJLAy2uTUNxygfEAfaZ9f6wMPH9ODg971Xe8YJYWUsitTRNJQUV8X/9/I2cIM0j4UYn1cU0uMIeP1XS9LJ2SQPsujUs0st8r1pAS+tfcAzWmi7y0bWRcuNB6+wXbWecdA+eUhwrfLM9Qxp7MQIRz0SmlwV+P0TzxaKAc0Xgcn+5A/PsimzsISeoDZwOgHQ9aOK3YLqThkOCnnaLArhDVQueQcDKtfestcM/F0rMK4+XqiKI4LQq15w0Kacuzs/BPko66KvfRIawKNDn5lm1GdxBbgmJQE/viwnlCojO9/+1SPSjPSM/jq13H5PgapEEVVVJicZTTPOJXdLpLtoQQXGUY4StOOcK8Kje27SuCroohitGHz6mR3o2S6bSYbJUNrs9K2WJFWhVBfrzXXTl2SRYlgfQDFzb09RjVqCN647y/6pwkLtpkW3PnOBR2TIUmWizdexF0DlJroX3IXBCs82lArrGJIoIW2YNMK5PSVZHjzBNLjeYf7khVLTol8YmwaQa9TfXQeb/s0jBXWlzTM46VZCCvhXDvb/NAvfcIWklchr4lMVErKj3qpWlzRnu9nuxeffaLUi6GeEAdDmr21WjNG6z+cGR5JfPo1Yd5EbF+1QzJ49VYsf6DFEih98SeSUC+VvpjxCHgHDbNm6kUANutoJW/+egFB0Yg4dk/rzz8sAiAhCbVLsX0ShroqJt09E4n4lStXa+y/MnT9LoVG1tEFgFwShFDm981BV0xIow2rbS0vnYO3Jpisyhl1gSOa3lS0FlePOeVvABJqQyERuuI6h0N8FUp3LxsBbN9Zc9b1sbbaKl5PcEQGokiKXOf6+hbnyEVtEaR+v9aTRC5aKqAJfWUyPYNmk8uZKgbfKO0Ww3rKi7ig+K1Rb0YUYPhwEBq/LVTFOYkl9/6dtNAI89znBOA5rfIwdB3XVa69QvVLiCBmN+HjFE1Lzxe6uwMlrbOv4CoQItl9TnWgRmQLKKc8hSn4BzWqDdT0VYSAvI0ObU5MWtd0FxGHelUrVFDbtDYibkNZgdoEX06GATAndoOv8zcQ8i4QVeHr3Utxs9K0XkTfa8ul+8CmnE4Q6wZLefNhD40c2AIgNIhQ4Y9J6k6nqyWTL1NfsY+D9vj2YDM9y/EHn1g/MXuxCKlE5GfEr2sqFUUt01a/3cDKJJDi65G2hUVr9tyay68i6AdSheDyVEcBClwG5UX27lnBC7R0tY/eRz91OqlOnf2n3rFqKbOMvtdDMJqhYgOMMrLXrWipuqSLltgmieiARR2/B5TLMq8dj78AQ8pxwb8P5MvGZ5sfz408R0EyvfXiGJNCJXJBETAok9o4kM7YvF5wtmjvSp4tIJwsfMoBWHg06D3Al+q9V4LrxRkSOtHffRDHWIZMKKIydh+M04xGApXlRjAa/nv4Nuan3omi6vSbTkt04AypqvSowK1Ga7PBmATj/9nSAn3l7/wscyolGTEJn0mlOcSAL+xf/FxSEEiufNDxGiqmUlyyaT2NQ7+IM5d6+ZbWa46bQDbL3NzzJEo45gtOIlE7jonFe1XX/sj4ZQf5vKVp1eFLxBUpOfe7MOMgkd9iKLox/CH0T8YnIVNLxGVtaEpElWWfjFwS7Neue99ICBpiI6m2/zVtNxSgMeBjjzShI6XDKaS26VRnXZuKm+Fb8/bkF1Fl2svjPQ0jrrYWYnszHP87IUzVZFgArk9GVKZ4VB3yg2J0fU/r5Dp77CoHdCWr2e0BQHiLtxqyV8hyp6FhqWPBhNoee2FbpfpdzXpWkx8zPJq2rTVHzo7d6LycZKV7r239tIih55TBy5Rq1YSNlWD2nEUPhcePJXlKNut9ojJPOsL/uqgwWyN1728G04V1v2kcLUj5c6oNO72eSjb3qMD2Som9bttBVCEyvqbmdwd1ur9ex72WC6zvg02ajiTDfSS/DFddfw/nmsnrWWqVJ/9Zoh92byPQkTE30trwivbbvQTCjA0MdTrja9/8DErm+i1hsNQlRa0FVpsFi7Cm31se4v0ImZT3LedWdzdoX7sKO2u7Nl6PiggdsFQHYzVls0hYb4APoXnZm3sPGLjKqhWqYIMwE3y/QuCLdkaQtR6oCqOCSXAMkbHl5KKjhrFIDY3fgaCu4hJ6VykquwH2BsDXi615vMzqufOnrKDzgOklLfxJndYajqbW+8xIxdF3nN4nMHjBJyvagxP/M34fe+nuLjBsmCC02fHPIAk/RRIOuKJ+Rd5wMFBZdZQ6y5pEgSBiRUsFDhFzElTrgzVVsVFEb42EhtF6CAMrGaWxVdkLkJA69XFLYNWgVqbaNt+OQrLlGE+Q+aG79BOCpzUoIrQuh6V9FqwnzbpIRLYgD3oUhI36Jlle+AJVWbbcf9eyMbKvAQ+Vg4EAVXAwbXzj2hbmS19IkZMxph0naYjuNOzTiFi5VANUmYhAKGI/z6fmNQaVZ+YqTCKLyLlm9t4JxRFo0wEbtpXxlRJGbpVaCpA7hT2pdqqdrTLvBqWXRcCXOpCYdUKpqagtr1y04RH6uLnl+Cc5RQozcx2EuAUWuya/f5S6dg4XJobVtnJrzhL3s60okO00PqNlQIz02l8vkt29VxoKwhRq9Y9sibRE+lvPGvKczDf0yT3WGzmnIDqdjWKzP1hcXWr/m2Aq6TBj1J5o0pNDZi9QzoOQOf+4u2PrncAxwPaXgWwwptWvQI0EAj+zx0rQPSeKHBxMXE7fMLAPiN8XGdtOasLRGQooCY8n09yn1VOG5H25pBP5seIwEyNssmuIuQyOleQtw2ija8paN2+ZaIt5XHeodFxPIdl3b310KiiSkZ4R3CyNhniCfzvnMZqAajZkmiQdXL0QS5yTzVPqNtpGO9BC5rlxZHkIP8sVEQ/bFollIXICgsxmPrqdXrUuNDI/mKVppGk8eg+npF+E9OP9+BGgvsnC4f52xq6835M7u9zZF7LRwXkQlMNTS7+kiTo9wjIcVx6J5DSsIvS74BVklELAjHiWikZ2XSmYBKriWblSTEy9X1rVjxjTxuhQWJGx0orHKjH3xdLiEoB4ht6hLaqvtsgz0rtuC4rTUxqaeSSqlFyDcv9HWVIo3EUOpIiYEVF1AVZ58CjrpdGuF22jDexiGThrRDKC1s4uE+i7dXIXnMczCc07MUhkXB44zK1Jt9HwlsSGcpmbTt2NdMOahw1QM8OHC8yXqvN7MRyRV81g++Gu25aTEdhMi+xWmqqVNHNxY5tpyRzxYVO9VhoFGIheEVe0lGMLeLNtMXnMIvEywK4J2Z6UH+z2nyHeXPswrEL5tLSY52DLSPiCrrxAWw0wTALrC6XC2p4TpcaRThMlij0fchAr9T/XVgh18CLe3w3lLuS5GkuL5f0URjupzyf9/QnQdnWXFNy+7Dw2gPHzMx5D6f+Fv+XGfWsiuzvq8EEuOjgV1kFcNAsKNR1/nTjKAcdDuIICXgqR0WjL8rnbmWyhx0darNPdqHnEXWGkctVtbnNX2/Nn7MS6FaZsfs/a5bk6RlpYnPCCySM3xSyUsGJOIW9XvPabsBLBB9eUXCI3/slXwubL2Y3ylZ4nM/G2PCsIqzSb+AbgBl5bu1SND8WFoU2vm3/Gl9KGxFhca3WmAk9La4q/PZOhWtkxInuKYmrp/n/aH6zfT0tE8b08gjpwcZPuPLYk0iQMZAP8++XRrXQQqwQvFuOwgiGCUt//dj8tagfKwyOM5CQwnWqCWJ59ohXtNmZ/epbERUFvoTtgVcwlhO3njT/wFFWso3J+iDjHj8eViy+yPT8KoziMc20t/cYWXIxdo0fDJQfQEAoZTsJg1K0ow8aSUIwbKEucq239uwaBog89qCq/5QbklxfQsSF6veLyLbGHipSdf1WgoPqY9PVGvcrtgMX4GArhQbjZ/uK6iKDlSJHxTT3p1toj5belUHXJNpfCPiIN5nVW+j2JlBl2/2kDBaLQZ9RxsnvGVSGXNzVR9VQ51kqpahbj9NVEzWAAItxYJWA3Ezv7LGOVvfVqQfLXHJXRuD+WfkXm7Gv1qLMqQ1O5ZMDV40zrfZz6Wl+0u2rDqh1bWX2Y1HcntBfD0sdvHDFGspkX7oyC5P2lRsSMr/EnelZt3Jz6bT1jmeH2XbXlX9PGiF6gqAw4tTQNMk/SBHExLc17h4jH0IMxF4dIlfXRek9mN+Fdu2H4Z8WF41D+GkmpDbdfgihYL8pFF6SLi8h9vgSEmQPAEZJnSeWrboNsg7pKBjfU60qrEEupT8/mdGrOCNQ2RKaCi+xeyzhFfZOSM/Cxxfys46x9qAGgmOcwebM71TdOTfcJo0AvUIlOcxDw/MLzGKkMnDzskOi8/7HibGSBiSZLZrAh3oymjOZN+QObJ0G78BqBIaew3GYg0HedmaWFg3ITP6SO1XhCxERYaWONwwLfmg8BoVbF4/ggewCTC5z8B9RtDcM4lt1FisTw8F98xHuN9avOCA8apBTiWeCmiFhoNoewhHemvG557fPnUhyHyQk2xiuWRZeRORSWzHDQ5puDwubt+g7P1dGQ3fv+cY/TL6lMHaug8g4Bn+Cx7/RWzp4+S9Bq0kyS2q6F9EUqGZx5F1ZcdEAK9+uO79FKplb3XlGBe79XDmsHV7aBGZC8e/OYN4+3bAdUjeDR8yD0TfpcT/9+X94n3xx1JobPxD5F2anEouIWtfYJ4zmEI//y7LirOt/tV/ssBrCwD0FwAani5BNsLNWTz7lAFJtV7liqxFoh1qfrAGS0FOO/NeeAv7g4Rd8slVYyeJFL/AaNMaznmaAyNy+UJZvUnYYbYUeC1A0LplLwYWQJYoNiIQ6jWAnoaedOh41ANGMswDT7mypQYjz4TwghFDrSQgWKf+BwDrkr68b0uIGwejaQ/xfc5Cgw+EIhTxS7YEqLDu13AMgbM3VK4HrS6EUD+ymeOVvQMbifhFLT/UjA86HCavXDrork6QDyld9N5wDL0HztxNPs6JR86w6BU5u3MLVA3+KPDACuRZocJO05lnRin91Fz9Boka24rzpn0anJ3knksiUWFm8AGBMiP8+GuqLhSY+/2JYty+R2t5RUi0SQTD73yvMsA8HSoUbuSorTW61EXwYozrywOWobhsfKLRNDG8GkC9I7TmPkFUmhAiLgvE/pJW3iJelWJIJSSIWv2vMALkLkaL2hhLa/cVbWPnF79n5ZZ3HnQhhn9vAWnvJrB/1kugoSWars1/1RmPgf2rJm+KpMpApr/X/dEQI5M4qLFZK3L9j10wfBNkKdX/6hz7anv0kxixnFovzHiDETrBO7pT7HzELjakO9IlHqf7h87UiKQuSsaP0IbdjC7fYIFB1JTRRtIA53vXcBhRw4M09yoUswZSMvBfMWWkwUFZlSOTqkngzdPcrIgkpaj4XtS++R+ZVUPOpq0JPobLnSLyRxh8DPWlzjgFuQc0AFD+f9LQmhAwSRmGMze1pjuDOsRdggUZ8yOcCs7eQ+LHyhE6Wy2kS80dquwvT5n9WfjlrD/NgHg7iMASMjEfn+zRkfIEVtI6pmlgvXBHc5bLoecxNTcZMRobi71XnzrRQveiF0zwLD4YgRCaJkP5kYWn3Jsxwv57b3hiriOK1PUcoX00AN2fjHabXaqNQacv/+tH5uC18zOtIew8mtMKynAAYOSTCQBFBnIYwTwUImo0iOaeQq4cclElfcQMVYn7YVtY7UdWejQoTzYPoKfB1180kemJQ5IHZ1zOSu8IphXLx5hToE6pcmzlyJXcGxrBWqGHcBMB06hPnqXfP/a81AKIos9Y9+yjkfoST3RP5ygSBoe3EpjuL0UW3i8xWt7/odb1LSul+xNdP60qGEgC7283eCDOkrOiBImtbnaSx7SKRGcw2+Gu7L+Ja9aP4GEQ96K3OsNP8S4k8naHZAImi1XXc8QUW7g9QL0Q1zgm6belEmpLgeyan6aWmeoFbB/2a0k0pXaN8auEHbeItpnWydR7Lob54AHBVUBFzseER+gzCNoErxZxQ73JMXgekyk/uLjknxi7scwkYghFvC0AA1qUUwZArtbqotDEq5aHqftfYanbX7SAsX6wqAVcsiAzMsEWQ3MWsxg2xskXXDdYN3eeZnzfxBCyOR9xMrTOHJ3gHyH/kNsinLZHARlCXnLYAvqH/B5DpJdmtUbvFkpAwM2Eq9+UF9lDiLdrf5IrAs6m/WaEC6UvYFyLvD7jPsTo7YRiC9wI06hHKLLlB0gh1e79mNTiWauIIrebQyCqyDwxbHcKY3Tv8qNnZ9iJDX8WrQ30K5K0/ay6+e0z77JYzTvhdbV3oTHPiXbqEZQBLPsn5sRUhM0T5kOzA6xpzq2l/LDzwWPuDLPgG7H424fAm7+nrUDTGJEtKntrFZKM+boy6JK+n1spstUCAHFLr8Y+Ht/pXP+Csg3Z3hCwVScoxp2MJ8WYAtNgszMKAOhEX6XQGj7Dq224zwbcgKKVxfGuFYrhk4kdj2xxs2IAOdue76++WKAuMCUi4TSHg2lrYOWYw6yqQdgUEc/24GPZ1i0Anw5wIDmqkHBo/vXCFFx1U16bNtvGyslK5C35yHQGvgfMnLVfhZ+m+EuScxwC1yXalI/NqugPnAcsjHu4A+BcgdufrRw9ShNQJXLsZ5yDlOSeEF5QBSiLfFtRLbnDSRP88WOKNXUA4XYtuQfxFXBDZAbK4E35JSWFg2b20I1bE/VfREXezsWvSC5abXsE7cA74/bzYKFcxiKF73i3JVazTHdQE5QK3MzSL1ZAdjemFrhplj12A6yKkQxHg3XH882+SshHwaiIrL4DZ3BvR7SsxQLtgZSt5cLNzeYVjzBk/+t3zOG7/1eZezOEnWe6gjZT0giX8IVIQM+0BqD2Byx6+8UMuVkc6aqYFJjCiQ25xRxWG/JHoaYmDqICzbvJujfHXbihUkoyAUGeSkuTzCTJlqXCrXA6qKoCFiepYwHhYwKdtxkqQc+5nKwcPfO3nNN0/52OvjG2NnOIywNyv2tPhp1U6KopYrvkOfa9gWnRLqQNgxy8VwUuATHORuOzDJb5aEH+mOFPyXNwT+ohjxc8qMPPToMA2fu1QuLZAriPUcxSYwUm/PmwX7uKTJMLVDsQmdfX0qJ5zj9HF2uTqM1+dWYe2A2VKqAo7XV8sIx/OJGIlsULhit/jeblomzB0pCvlzl2ZrnhAquXsYCLkJk6tVf3ViqeiVIYI1Gyh2SqoNCAMh/iIcofHPlTgrmpaX3R2a1veZnB8XL0HhFN8FLxuQ6+YLxOlVxM56/2/VsiN5S/DI8KX6X/SxqH+BMZmH88XZF+288YQdhDqp6+jevZuphFNpskdeJS/uE9yUgm8YaZvkH6CSOnNe8+Cw2JKzpl1rV/7RmiuJqfI1HpfaLdGdPGgG6LZMwy5x+e3AEHRd0nsYgU+jFIOPcRwtlQfgm4VURdXhXjLbUKWulRLk02++k2RcO5+5dvig9c3Zz7L94Y6RK09YGraIYCi9romiDKx21IvJadI536OMgRxiwxjBqiNxAAZ3R/pHcYyZum31h+QGPBW3+4ZZfTwwTOs3+9AYm723Da/7SzIZtdcFwoBYiYnW2lFuMJK4X6IuAXpXBLDIeBOWQyIst4R8fqNzBrAgl16RsRS8HDuck4q5z5jPLRxPW3Q6h5Bj8pWtcRiDCoWMaA+SuZa/mCNJo+RccjPNriVgusKcTAMfbykx8ZTEy1g3T8KHi3E7pmR1wAMPT7OWJuOses10xM+4tgBgnthIHLiEQYkmhsFfHyzHtsUMsuGThNhr5SwYH2Jaitu4br50AMGrt0qqCPf90jH9ZouZix0VAIzhAvOunAGQxgPZih1rAzOwsUP7FajkAKNuiuXXzZC1w9b/nGFTeDN3m+2c3H9xV4xI4BgdxPv6kZipMqJ6iR+I4W1JJ2WNxBE8OvJqQEnFP7FfEUhnYPJut7ZyqaFj6MrW0rRUflD0S1SzMFoAvuGjEu9OBNkLf4tdLg290XSuWzjmblU52oIDtGX+w0GcFRGT1/s7wbZ8jySe8Tmclu9cz5VotxbVNi9aINNj4oCQ9uF0wznEq9ajJanEhspiYeuDl3KQ41drCXz2tQWBw9HSKmReO81xwVHPbSBN9Ywy/BIHkxv2bvBS5ZlG9VPkRVvKDCum6WNDIPB4AZux5POHsgLsOYLCpAUJOm5iHGdFeDfbHB1MvcYaAfLOsgHModyJlP0bCBDYfRwfmPMsIPABMk5AP14HzzHaLPra8tuyeg/OPVWKCwJP1zA3G1r4Lo6zJxtv4MgEdhoj3+WomRHIPVhVXIly7W66pkn5dZv1sQfUxhcbSyqkNA/Kuw8nOsh4/KRoXeOELv0gI8X2klysg+8Z1XtxkkMOlOhKz+vcfuDnH6U1HvA2c63MYOfcaYLLrLyG/w7nRULtnPB/0QBHWxyUZg6RUsRLDm0iqj+KwUgMA9u/AG8qEQMrL+YE3kdVDjSMgFLvuGAAMLkBXJh+wMYr77nGFxJiHwsz7YYRJ4LyUya6LPjbpAk6e1xEJ4rUkfBbOv+chb8uvoS+0W4rHxplGyEh8WQQDmTbCfgWCsC0qeGWrtaGLjb7YrAPoXkx7uPYlEeU62MJ9VaasSC0Wp+5jT8F8AKbYt1Q+/xDSDtoYpdPh9BQPijgx86qHot9Lgn6/9swW4o5y1Y/EqlSvRZNehbDkhl3AKfCinL/HT2g0w4UjDpNMad8KJ7P6c/MB9q23GX7f0s6DyOz7fUVjYI1ZM57E9RRziyQNWpGY+I1uwhfpgJlnRPXqLOtDttFHwPnhImvIrk3feniBagyG3PY+TIe65mUYwvpZJIH98vPzBtpBIf2fy1mpFoNqMgfAFq1ySY9jOc8jsPnhO3uOcYBHEz/C2nEjpDKeGfTw/DNIPhir7htUZ9b1I8Nh4DU0BBaqAyiNfeM22vjR4wnF0SKj8Bu2to8otDZwmN4MZINsO5zRLLBF0IAxkOoSwazNCWf4ueNWSS5ZKq8IpwLii3jzzLfih/OAPuCAlSk8PVs4TbQuhpT60PvV255D0pKnoGDPwVUqSj5lnl2hUcKUheNGSPD4S7g36M3MLCOFr6LpqaCXSa5J25s5hVrnbygaev/k1mhJnQ3gB9ZjitzLEoNJvOaoEjeO417cHKzXs34w7BmXTfCLp+M95q6eWHI1bQ5fipvC5+/JeF8lJiSMtJkNPwjvOn2PIo7bABckt7XmQD8Uy4R4FQ9I55qOO3gosxUbFq8ZxktVp+FeiNmkmisGhssxcDSo3huwIllYTPPKuEEEddKfmqf34gull6VlKg86+wl8ydMGCn41j7fAF0ibyooEUh4i21Dgcz73BwLHn00EjnDRlOzAxkljvWOO1Zo0S7mwPi7V9fsizZ142vamhdpgWNke+VEElNQIkL2KQoG3eaW7XEnzcGkJnzzxutz1/WvbTT78wt6LjJ91JD4dCria2E6VdrmD5Mavm1+lmXvyYvx4Xn35EpPC6DrG/5DefCopvWdKyzLqII06/Su9Nts/wkMWDP3Oow/TiWj5OZZP6Er6H3Zy2k1s4EoHajf0yvxZO64ZwMdSnOCOw7vwl/pLQ9VBvxxNjsCkuSOLIIlWl8AnhiRjmx8NjgP12UVO4YGlI/O27+GU1MSm6pLzP/gOBwqThihDdZ9MRrwKdC5YGQeAMdl3lESRGW+FR+rHjYGMz/Nm8fiiReyLpAO0DXVs98ejdepapHoSWUlQXzpG5dVsM4BacjlsD6+0pjhce60CzrGxKF8pihpYr33bN6rIbcufl8abr8DL4vz+IEnWtFrjViCbetUv6jGdNa8h63G59W24/ECo6rsQHzV3JwY9BRb1Bq8+CvPV5jC6Uwg4mIq9t48svAAAjzJsPKYasyq6I6CuMV2gGc/+0kOteBvCmYAQ/g9zXwj9Kl1sSXBa5xt7CbIXl5SskvZj8aNyI2uiULURomwAekFWATVjlqSCA4YMz2e2/g6LXwupoo5hxPrnNRItjdDaq3o/3fGaYwKhIMJ06WdKcmIXXEJptdvT5AEW+ZFUx11k3Stw15NfWU54r3vObMKwIS4wrUH7I1D1MQOrY9wPi2KrLVCTNx14uW55vJsZVVTJoNemZMe+UZBc63SVSB0bOUG2PCq4k+gUPa/kADggLrPJgeVJdu2WVxQh1KaLbpM+7DUUAOVynO3EjqecDeBKMyaQfVvA5vsh7KA7sWknnBhld1grunNNt18K5MMHdGfshuc9hRkNyAARD4cHPIRW+9f+/EEDLEKcsCK1lmAJUkOM43hO6aFwPjzD2VBmrSv1kCfTFUH48c5oZPCmjzmeqOfkwmJO0BiW/9348gWdXr6kEjEYUdEM1OvRf9YLT2H5Yp3agqxVtKn7MyPpFLOMW8puOQzSaq7uXvPxRzuU7mPfX2S5bjARt8+85XYrMXMC/xNbl6egHZnWmi3oI1XI0Q7nYxh2ejaQj+SnxVsZSsd0rFM+nhlnlBUsdqAW3Vg1KL3o/TMfwIA4x1y4NJWF8eVqENXAUyYczyL4shziglGEvPpFX68L/6sljFkYTFRYDFk3JSmqw6UQSZhv1gcqQ7nze4e9E5yeR9tpHSEBAAzAvY1t0+JfckKWoq/uuEGs5CZbIf9Zvcc0QNLUz3T2oFzkoK9tPTiAlVR8qBHU41EHUBR0uqu/rPmcs660TIJQgaMk1+jLvRCABzHlkCDExA2N0ciOCxnHHIZWN5TE6Et+m84/NyWwe0Bh1Bu9FoR50DYZJXwH5jh18iwffjb5W2Ld4c0QK9AQdYViciQJzpSxQFAvk9A6MvHZjhLQUjA9piMskbo6eFKvLzB4I+T6Ge16aMFeztgprI0jy/7c4ZUF37vcbegXAd/hFScj4KsbAG9nJ7gDdpWFTKlEOzTF50AvKnHHGuiBDKORbtIypWWS3m4va6zFF+Kj45Y9vKO4VdaK5ZYxjqRlYnH1LCR5Y5TwCg2N5UB01tThNXPz3jtguNIqt1XFySoRm+bYKyvKeix5fnKZ2lsRp4abMi/DcpVvAzQWQSEd9jc3nQKexm5I5obxxHVN+gg12bHQVsEMcvxYvW6APxRgeCbibJk5NBonSriYugX3ZPmdDQGk934cQ0NR0flSILIqqrnLDVVBhlcLPreHMs5drMqmwaoy/GZZPbm5B98F4vQwgY/TsaCW6IeGJpxg5gQOqVNgRZiDyF4Rwhaicb01kYRq/LYkqM8BE1tNnZf+ZvGdXo+0B4yy9pLJm/UBLwQivAc5JcgYs9OZ1CQnb/7ERWXRoXylTe9rBMC7OuBNdXtA/yspZ68HRyB4sL0Goc7dOLCIEx2pCiAb8HvEjI2artG3wAXCBo98CCxsI47RMpjnhsh/eRDD/3OAknTJYVfJhfgbCRNrSKv6U3C5LCzZTN3e64h1WBPj232Qf5hlVuMIN/748hjOe9O/t3hd3a+JhC3/t0fYe7ABv9QEUANDF6lenjsqOLU4tluwst/+rs6rxq0s28fVBdN4/gF9D8CtKQRbRVjsW7uUug3kdvVkKL/nIskQMAmbTxbnSIedHThnBPnhYPPRWeyO4/pcMDMZzGK5Xt1YTwAi1p4oYVsw/FGpcKAXTBhOZVbTIwh7sKZoXcIdbp6oYny1pD6RnpUEc7CBZLZbu9+XeX4MviXGE4kC6pLqanQovsJFjhrK0gLyNh5BvoJl6z63/5TU3063MzBoNnNccw+Q6+ZXrOAaf8qSCOBRSK3KbxLWHiQQFZHcbD+T8uXaUBLQKCAnhH7qjyyYq6PI7egGYhVFLs+Mf+8jd2YPYUVRuMNF19H7joka3Mz5y6KoKnfQ/r7TOO9TBos8n48DALHX7q9XxsC/H2U4eABmPE5X50aqK24og+j7chjroOzbTcZUytP7UYt0WR5ZdUwZEgkqNYmdAL48+Q6BqgYJX/L2eMFHFiyWsWR6Gk70c/0FhVG09eoNqrXDfvKFwhKu8Lu2FSiCkeq64i2v1TfWoSyq4hLmVlpsV6G2xju73cP2/FeDPw6wtPAWDWZAyTcLxfHMHmwUEOghIJVbBHukFVZGUPiOrQ3zYoIVyZByWEstSWF66TZJzuf0hak8Kg1TxZ62RXZWYwlBYuuszfDgSMJcHN2yyREvz+HRsem4nlJ5uej++PSkIVcKKytPLfVB6f49sa0y18J9OhOusnZ9ULIjoWBY14zl62e19DhMoPBqapQ2KBc/1lzZahp6tjmJIkGC4IpGqoW/bDEjiqTGMzyzDDEdNPBOuqzTrwMMXjDdbk9+TusYXUdcD+hwU/Z04V0/0gr9+/gJJ0ko9hzSJ12A5XwfxATFqaqh8T3cwnJay4fyDEXwvvjPQtm0d/bP843gUIp+cJ9XDugf2Y5BS6UR5JWKO+7XwhjPbEST/Pxs27xYjV1k9nqFifinwYNsdO+oIWSgbV2o4elQ8oJYy+Mjo5tSaUNAVkCdWg53bPwR6eqX6Kddb7yDjqrdWBvMk8jM2MMZ5VZ9Af6b3FDM9U4l1p435olIpVm7mI6SXGDMbQaDccOUH7bf+w0D87vnzSI7z/BeuPZVQ4ozhJi4SDZbWf9QDbrpqDudhcjDcePk7e7t3L2mFgeYjrQfeQAk1n0WAvvJRZQpWPGPC80xhKbF20jmq6JAO6IUnBFZLjV/+HkGSvgr+JWcMyQjyBOp4z+kESHw0x2hW8S6IplvJ4w1U9igs5An4nFHLBYR+vl1jvywvaYvzj1785b6CBTP7vt7S7sF3g7V+e3nfFDM1COkGkKZCrYEpCgWnZQhn/p6TaE+7Yyxf8CinQ+7DiwefdYo5wBXl/zxoYjZNPnzt89R2I7yrCs3B8q/MqtR6sLCSv6FFJY1QSsDOpmUB8fTmtQ7aJ7+PxteVoZhIESJRI6CqL7APpinz+NMU/tJQIo12hmB5BoeHNT9qFB5lc9UdUBy3zG/mF3loQrnnfVOKH1pwQrB5CdFAcvEOIp9vusSDePwOtc3ecyxYC8BJV+bz1pL5oLUJQlW6FFOFIfSAD5v6ALkiEdwnRxAcDrcWjf6DAA0uik/gcWocZGaPeicMKgqGqZ78IE1s2EzBtjd6b2CRLTXNJmFGCQTlBWt/MdTxMelC0F6jLYXOlZv5Ln9lwmI6F4sH3oYRllRFn8eFT2lgIySl2eTnWL6aGde6qQSzHIqrPp+i3vbiW2l2hWpGW1I3rgSVvTTz6SGG4qcyEeTHWaGYOyT6gxDAFEiPcfYMzA0zlBlV1oZaIcbUKiG59pXdaz8LtBuRVQI15btSVciGScOvDklZ9rvD3pWqpqvJp9ozwPVNXy0XQ5JS23G8o2JtqwGA85A2bOluvpwwnxd+CHrMqOUhClIGUsxfWeOpBCO/MC5GzHRVl8ypHlZCHBD/f+GG4m3nICulbMh/VFSIWkTrkL1iXMhw6drqllOZBCqcMIjxcRBJXaklxoEdlMeXc4QvBngzFbxg69OvcL+78OjkXTMfJCzFZX54bhBXE/eX8HdM95rfFLPhw+ZougkydDtqg4sJZdvKaRkkcRGNf8/6f0Sydv3f8yhSBRwBIYFb9Iwyfdq22Ds1Vf+Xj5BGsvMUHzv49gEtjbgJAB5JQORf8s0qJZY8ONPPvH8PX7cuJNn2J7ACBARozYlo9r+ZPkrWyZcW/HG/2EzlsAW8jAixNCw+nDMm1AUChSWCkLxLtyJbHVYfP6qiRFoWoF2sbl2NlkzChtQNb4BTMdjvYblkCidQ8766e47NsIpWQPiDAdYBxgOLaIzOGuQqXAcxz2gIxRq/q9eIJ9g1lu6iyg0S9g2akVVx5OXNbxSyE57+Cd9orJOU8J3EJd+eNMOlVxr6nWseFx6ETNv6/KeMkj5WtdMYFkMHSFRnhCL/Yu/qkFyMWFtcFgCnIXx+UHfgtV11VD9Y9BiV2YJRGVKvL4gm4lP9UmEXhlrg93FgaR0v1y+d7zdR+vMxn2yjsrnEkagZ5C6E/r2x0kjnzB8PjDfVFUCdsg0u+t7qwqf3kHDg3UNvYFr3w2daneZVZtuhi0klGp+eNknfLtLb5W+/SUbulztiLSpb0lepZJ7Y/F+FjCMd/he+hLg2ryUxwygDXEKVrcg5XU8hN15NScccKR37T2/vyTfj42elXbfLGDVYZbD73hc5kWP3WEt2WmWTibLkeqsCFrsEDzxbc3NgUP1/Yak19sR71vKRQqK1QX90viy57tgsjDM0kmONRbP56yPZmy8JRbPx6sz5u9RV3dezj/TqkEW2SJBl9xZFLg4h3p9zycZPhn8XLJ4OBp0QOmMpEVod9oIDrLlyk4w2nOrEX7r9bvdp3o7CIkQOJPmGiQObY5etmAxHiDYXnJRnZkdCiXd2GCIjQGcu9EaN59XXiZf2SY2PwDObyyUjdNyHdp67y0BJzO2y0wxterVYg8oe4SLBg4i7d4yn9N3aK1whHvn1VNXzNsrYNzlnmedp/VYOC/r2gGsXeFMWC0IPj1CJN2fD9I8TFGWfPS4WqyI5HezrlS80vlXJQR3SjY1dw3S/PWtqHNlB8rxMHHFUS8JVaNhO7RS/zBAVNDMiEEv9kJieYHB4VVO1OplDMTr3/ge+JgPa8Y+/udFWxF+Li5Lsa77uG5KBkFa9pum1ytv7B51TrpE/PmLGYYI+IcOBEiA3EEHUWrrH7L3FdaJyTUtQ1vjeueHaBv5taemKCZNzYMv1LFGIiJMvXASCLT4g4Ken7GRzVvSLhWYPqmnZDOCWmTDnrKmwykE/DWfqQ29Oa8twTVYsQlgIwlp2wDZ/RnAiKEAExO8+rbEodNKqoGRYqEKCXy26lqD5zVvUnyjddd1nNB85P/KDqWdd7rowT2IqMRMzKqJNhclhrC6m7N0RXfx1eO4KryF3asu/XV4YhtfV+1cU+1mejXrSHvIVjCAqseRkHCSA25e4quFlwdJzT3HKhU6KezN2+cjSkHIH207d/2zv2rrzVneC3J9Pwm5qjjfTs45TdaY1YVT/yibrh2Mr0nO1y8IAJM/lbGJ6MUc+cnYAmOG21l/uTBx/16nfWnxXfkxaDA8F1vrVLQSTFO8vuEsHLoH3k5yhrD3Fr42zv++y1TqMDlSZlqQznG2bXz/Ld0ZA+QbHVRyzMJzfd5DX+3cYV0a9CtmZODJgM/mYZSPvg3Q2b7ISguRhDvx52o/Gct5lKpcTIInMMT9XMw4KvxI29u2K8q/2IHwjHu7+vMNBWR3CT6tQNdchQAoRFaFGeC6+vW87n8p+fzLUng0vDL1O3/Np1Or4xuv+qCF2JqZjYrb/f/Uuko7IUeINAXDgYtkKseju2U04EDder2jIuxYWIH67otsDgANr64lIyLrriDudR9dzg2KsOaXPuRAWWZ04HAbB4TsH/B9SN64KHpQF8Az7k/ccd1vxMip6lkZopUSB03BjQLEVK5SHW4N9VQJdrOt1JxVuc1ZHbTXuqlkZrvLuUn0W+Tovrvx+ogJ5jXKwMBZpwC6IFroblaNbUjeAS/we/pjMGN1Sp0ibcr1/dV19dmWIxTunI9eHcWkwjX1rLlMPLqvlPmW0Mufnl3sbuy3f4ED1IzlJ8UakqRPKNNEu4P3rgGqyC6wt5QFj4IhyNcymCi6ep0qXGtBSYdtad20lLJUl6+KV55VPccIX/hcP7CrBjnUKfVRTENL/cr7XBHssasiFqKeas2o7AXQarisKWryMUvnPlh0YT+aZd4boJNpPkrIZVt8I3J/lYgI/8glH/4Tt3K0Jz63dN7msiNBaPdk8j6XcaKRCxCuyfi+x+l20qNZesM97GuXgdoJqqgYWewesFK5SdD5buftLWKUbcv4wvZ7dq5YSgu4+rKh7YaIKFsH/9Fj8Ij8S/l4K7Xb9hn0h0l6LcUqQkrWxvti5YO+N55PyZs+iHzW2BbUyusP60MxPbAHgR4UONT/deHJJWjgqSKwBB001GtupPO3eQE82ItpbNDhUmTeEDJ+Kw8q8I2c86zTCdIQSSeTivZg8Y8LJC0jt0durZVwYG3wDP+GFHf9DOl9s5rZSJ3KdElMlMDhABghoI9ZnmTAPRwiXlQ39j5fFK7/DQwNDYrGw0Ynf6Q/5WfP9MuoFGFAkheyETwHpj4xKQYrPpt0od5rI4qsHga/ClyqsAiQtgP5UyAFBfy271IhqUmSkHVDuZiAMFsoDJoFrpIsVjh6cns7NTxbwOpHkh24AjfcTKNCadIRrPrvCZkLvI4YjSQwmgGitjZQTmU4pTBquEQ6OfOYri7JyN/BllaI3f3slSfM2BdGqnFu1qkk/XatjOLeWkptgyvl0Iy72zwSkirWde1W+DpZgzmuJ6N3U/2jSMlbQZ2cajr//yWnK9E2d5K+IVUSPASIEm6K9W/pNFmVa1WsopGTv5PTEX5LpM1RDMDx1939MvWwn53OLItVSdjNd6Lw8qNQh8nrZboqWY/o85XDlklYdclE/08lwKXP3cNxqbJ3Hu7APZZdcuADgLpsqUVWuQr82F+2Yoke1eEPp2uvBsJpbuOH8HjCzac1fLprdbIzuIdalPelHnkbFKjm7rbv0c0I5RF0dLWbSXIN45S3Qcq7SDX1wF+zVUKw8vxl2pRvzQc+ST8uJCw++xrpqjpGiGvz0udVvw+mdvYuHjc2qBPMuLiDYA92WgJe4WHMinxyI11rzmegmAYlKMBbrEXzgb5jvdU/itlS4njsj4UIcNqUjeR4X5CLckJ8ijk5ZLgtseGWsqaIPO6y1BkpTz4ofUlPjoWzwPbrUNhNtoT1ipBGRMtcG8AUe74Z1vATAuezd3pPjlNCklOgnjxTYFf2V5V9kGCm/9Rv93AczNioIsmNLo1Z9cSkflXrfmDDmcXR7r0Tf9cTPdLl0Who0+QUnkTdZcI5LDYZpqQlaRBa/KHvM3cAhbiQ/71smmB928FDO+SdAbQLVtcE1gph9Ed6MeLS3Gu2nJOUqsesmP2lv3OHcLhHdjXOlBWaTdsn0L2G8/WqmRb6JBIRVsD0zAa3pdg2MUcVTOq7uS368C4gFP/x62lZ0Hsw5Vp2ZBd/+4F1aBY8d+2tZAKnEviIYRBXb4oZCRaBpd23KfgZ40o8Wt3tg5lY0mC+wWiqP+XNDTXpwFRJYrdiJDV4HwjHsSXUZBh3KA2uI/8w8DlxT3o52ZFN61hplyPDrS2SsB+a6AX6OWShkAAaU5uGfWOANhJVeB+XBOc2mu3t6eqGakSRVbyabLJfpJv0IHsNdzjPRCSGp+wVm1vyp0FHnvd+db9/DdDa7PmF8pKaTZBGok1nn9xCYNPseQKsMslKoiQYzvO92bjbbFhV0Hf3qdOdUGz5S5OuF1SzgktIXlLOQtbPOoxTlTFKN32pSdU9TXtqI86BDwrAtP40HyVba5HSttdvL+ygP6J5mB9c9SBp04vpxIqQj1nzkTGYlLzbwx2HViloY4qWqmrQJ1A+0X2h8mURLatnNfr8rX4eOTZNeTv/9pgi/MoFYynwAWyHBuqiiITctJW9Wkb43vM4mGUCySeHS6ZJuJpXKUAMCqMdmOG6SP9N2DgQZ4jqeJoxW5/3z0Uic0fjV8irPkrrBmiwsGwIP+LWM4zbncMiWPwBc0PGwn3LhSYy8qFMiOTyQtHGmCp+7jg0rlYJuY9y7686JYBzZ+TUDfJ9qK19b5OY8w6IQYINbRp+72VtbGeVSrUnDwSw4oHf+QmlmTeY9MirUJecineJWH59kRkR+Qc6FkF8pRxkrSgS0zKSRAIBm64HLsuwqI25y0RBtEBlQCyc+HOk+3rNfwMVonU1oSmXHo/Zn0SxuJc8NOVTTdnIqhqzsvgNwFkHVh1uRz+Fr5riShzz9BIFoMc9wLIzFoA5WAX7wM5KJbgS+4Hgsdah6tf1gI4nScIBCedaYs+OP9J6jdjp60caMywTjf/Oe/HORez8cg2iwR37FqFRx8jYFKxw26sBmm2AicnG/cLoh5AAer38IR0NIJ7Qy2tvARzgUS+t0oQz5acQh1jRfOT4ObGRxKQEEZrGv1DD53dhWnPeF5R2PwUZbjWTc0SlNDfl0lu+rtiF69D1Mw8/0ag2W6QH634QRNoeHCDMqmOcV2GBwiANyuq+do78EoWZ9+ykJS9xbv43z1RVWm9WfeaP7/zVS2VLMlwLIahd35YlPVOClYXyo+ggbAy+N6WVMeEgMecN0ZWdJYC3/bqtULX8P5oLfRpMDoxUrREkeqn57g8BG2ZpHHJMaOnqnqyh4l9BKDLXYSZ8DnwjBakSNlHXchJjbGKCoyT1Dz2amEXVmEfmLDB9r6NO9qsPAByNMEInJbO6H5J3xeq7b4l/FJSM95FhEN/++jjcIH8qSNfiyKqSQNWkmitdEo1OOUOar233iKZOOOi1JDYzW+CdvBst9/0ak6BA0UjPy2NZvfssFq/P96Oa7q79mokxaYQ+cZcauKG/9cCs7gGYfO53Ky7zBQaWHZFskudjODnhU/uAf7tpAmi8fw/qyDbwmbgS7XYYPE6FMMm9BqUJ7ph5xEfDCcftvoeNNtY6IlBcu/iEqgySckkzYTIirx9Mm/eCmcD7p2C9PbWM/feLDdj9rBN6AoybfGo7dVTki9z5zuw/Kgn7cLpk4QYiwrR4hfPhrCHQ+NHRuUEvXJqxxAVp/4IcpyaMoivkt/x8yobocrrtAj1Kp+CBEMqgjdxnAZKtAHKOR5Ng/LOHkH3QpBQ5VOU0vwWYq8Rt9/1FlvmR5WPAwlWu3RQuHF8NbFRCm5O7gvT8ymv8Q0ifErG/a0BfM4QmRiKx8uhD/phqfhzIaMHl/tJY54uouABttVMlyb2YWhQy/Ku5GIt6kvha9xeeUSDlFAz1sEmd8wTuVUN58H9hL815awtug7ZKoICAXNL8tJOyRNSvsWwDY+O7R+ZokY0PcXFEStq1G9E4zU38hFRTK1uTe8ii2/Sv0xWQniOpLiu4ymqrBz9yz4fLeuNYn6lMCR7HCs3kUPQuOrTJfWJZgxuvKTmW5B534sE+LIAhVKaE7U9ZcwbWC4CrD6JFAyXNmLg72/5CGnXjbL7sSNGgC0OUoPEDsUqfcjC9LbuQp+100h7w6v6Ei5VUCU6fcmrUFjA77lE9S4omlbOwfO6Gfq5hUzoI+S2UxBMe70ioztyj/yv+AElrop56cJmHKiWI5OTrAAzBKY+unpuh6VMbxW1pdRTY73932Qj26hMsBxFbsEMiacfGkINroL++7lEITzjZqmiOj8hvFlmq6DuJ6RYqpiCjMROvtLTfdBY9BVoh8c/w6BimvZ0RbPgyGMAPrtwsEYHVaNhln1/LpTOAvXOi+Ba8lU60opLBudE2BqEjN47xIEfik1M2ynrYuJbXHin3UPGwyKbwHr4ziqrl8i0JGAJ2ok62tX1zfQg+fDxFA7AlaMFfqvxzy/bKJyY5+4zrLjf28A5WoZNyE5K9C8wZxmB9hVIEQNEX3lTxfP9QDJaL0nv+/fKpbH3YULMpkYRAFIYCMY7nVV43NQ8LJ8pc/gRW6LNXeIKPLJr0icvTG3/Zmxxk3JVXdcgpqb3pTWKIjDvPBMvNVw7axgOOdC/JvB9Wd1FbU/y05oDR0i9+vzQZ1aAplV9IO0OGBxd2nXyTnxkP0iVkaBwMWrk6rzdMjcLL27R0CJGXIqV8sIZrWNll1fh0Ee/vfsfGkpPIN/IJaXFRW+u1sPjoyV3ohf1HdH0kP+K/fx72VlyciriPkYHSYxQMF0afHZywTC10ossibfODe2vNMg1sCSU1YuDTQIRr6RldUz3XzRQzE1Uvp0AZkPn9O/t3avbHDwZDoPLfMqQwUp1FfowhZ8z4BJoBb1g4wE3UvGDqwTsvQ8DyinDK3+c6a6K42ahLVViKxvqYoabuxmg9vhg23KUajoLMeacZocQv6k49T13k59yUFGBrubqFER7XrGscel8nVZSTduTnpk8Z1sNBQrC97fNWRU1Vn0xQRoNGxn3PoycwF6jFdt0iGaJ53AsS8sQV+EfpMFhPlQunBoSRHDsyIbKK8CvFWovThTvZYnX0ZWfmHP2uxZ5f+1bu888y1CU5j+90loQJJyCn/BgLkQgzPufjFSNp8rhiDfLW1CPDPNFZQTCBrEIlNUWdXipR/rVVysnjlr7YUq2lpwBFNYSqvZEH2oKRjeWG24z2Ta0yIwAfNY32zpSF7AQACZMa1Z/5KxI8hOzQ7WdyI5ZILN91D6GE8g1GlLyzVvV82ley3zMjwBOKn6E/9y4e4cTgluj1ni0El8e070vZ7Er7KowTMgUssd4DSWR7M0udNCSttGdHpqp+94As9JI6RcFPjEi+tMfOxs2t4cQ3f2OOOandj1PP9nlE1NLM9tEEWw2WZrwP+rmO/N+MZyGe3chhW/e+om6cG+3XGJtMOiZD/e5eIRAZ04LVPV1KNDeugZna72Nqxq92MDFs7PW35aek28yJ3jOf/J7PRgry7KZEmg4jyHEIZmhmSVqV/WYQt5YgWxdPPdF836nrSvtR9J2WGnPtNGAAmMO+PY4kJx9TsltfAAK44aMKQdnRl1szu9GajaKQ1eGOt4anogzViwJqKCwr0uzFF4o2p+mBcOOcAm/AADEISiG+/dSuyYgLkYM60w2he7pAYh70v7U1RKX0isMaex2WKIayz9HPLzOxOFPNUHQzwcxxsMj0E4meEj783jtkw869amijo2F8ImiUnEGaLLWkYN/+VqS6bOR3lP1qcwJPwVh91kj3TTo8LAw9anJYMYRpbV32lOehDR2YWKox/XtznqkpB0z3cEzNbhQKr9je4JaZsfQTXSpfC2KIf6zCUa607SkAhXucpdhYyYnmwN7Q+/v5yEozxZY4b5BWo2DC48ipq+1ahFGwgmc/nNWX9kGnVjOyfhjSgxBqQltfQ8O69svhmdEQPk5zWRExRjgyCv9dJUwlro/F9EIG8CqxsZwDotCec7RxILj44SQio8EDrX8HQgSNpu/EXexbakuCjcxSjp+CM+ejQdlr+S/JQeBh7wVIIAFAPM0kA3ICqDDoIrihjC9woX2hccblITJ4c+9yrfFw2aghEAafEUsoqJcwTrJzBpnJ6tp2n8VSK/+ZPE/RfU6T3BXT8dSyNxV8wUvyjnVZLWMtsNFFLbqpDtpfOhvYMvQEXsXv8PiLOKIuu6E+8s3m1wvJVBVSD5AgTbruYvaak0IAPooZj0Hpv0sheb+Saoc59qlUl5YQW2X64xx+BiOj0sBpght6UalhHVvvOPhmblH3NfQfqqqaf2g6rx7lLBbXD9s939CknogxOzBNVg1vd0bpw6Ol7zLVBY3fIJ7740CYj26AGXpXjluKak0Te7E8kUFnRvraOYNxwOKjpVYLwvAV9q/+3ZHIn+3acA/RxjK9a1F4EuSLD2XvSJTGJXWYVFrXaVZTrwvMy2wCLZuOFq/aSZi28AObH3qIkeBWkc5yoNsN/3GdOIFTHy0bOfDjlypBqnGiZncqgudoTvyF/jz/NFseOhizpjmFLk9fwhN+DQp6wkrpD+kseehVnD7rpkCH/xeMokWFzoceTl1FmFmd9wiwuk+QqlSYD53xLpPuxwHcFSUwteogCIcD3bcDo4S3DnOivOjVz1/JwQll6/Fy/iFRD/dXnME/fHk27iuiNN9WHZ7VuHz4T1bupamRQXbZfIerQ4ME96HqYybXgGsO91K2AQo4pAb/cTLRPxvIkXAQJz/4ikipfolZz5RXL+9dTpZRetyTOSkUR9kDA5LW28FoDpL3aVeyayukhLLbag9QVtrJaebHLxVHZq/zgQXkMRZ/avQYKoel5yv1ve5/xxAJpwcnDTv1Z882RpyUyrLY2pFuVhs0YesENB8yEWmK9qpCthPPZ9Fv3h+AKUlaMOPICT3Sd/1GpLURrV5F1RKq6k/WxHb3fyTjVeFLYQsQ/bJRaMAs9F4W8MVdJM4qDbf1dSrrFuEICyxf4y7O7G4ez7LRYrSN5t4wow1wrcDjm9f0sClHNSFX9WVXReovkMF7hgu6rssH7MPLzxfhSzK1dxc8j8Fkcnk4tZlbpzGfS+Xu3tio44nfOCmQ6vi6+0DgB1PZPNNt2mgHd8HZ3nqgnWUatCSL/4A8tVmI/EdxAUSbN8DJG6ceFDgRYp74+e37jW4ZQ+DoW2OM4BcnGDVisLaR9WuEnLQNNQKeTELkmq171zx/5vhQdMgdPFFQHJj7/aYvUi2H7CH/c2nMvWtpan8dcPp82f2AXzMtw/Tul2kOTn7QWmNLbumRoLSajYuzTfjwi2yNwalYfOIIdPDkWX6fy9MePcxNbk9awCNoABii7hCYmLkw7S2/kFfDtpg4PMGEtXkjsj3jHoIMZUeSMaO/QynWd4St3v2ks0wlkYY6j4w+a+hBWQmqGdZT1kFeJ5T9suY7rpy5dBh+5DPjuUn7iZQIEVxm3fXhYo945BPyFmZhPr+e5akmePT4OSKy0iSxAONwwFQObmi6RchF9NhRx9b/Uon0ujMrN7mrTRGGQaeGBtKpb5MJJygA9V0uiGGLeSIBwXUFmYex9O5l3kXt69OeyEoqGpzUANMPWN6rSy6fRu5gyLclwaF010PPoCacCF5WyIX+bdlYdBS312FBnlnMU+TI8KDPiCsYUOnkseLYTklxByQvOGtTixybI5npLQ5tqJ2NzpRwboGBvGGxU8NwhAp9zXpxzvqX/DY3FufEI9Xc9Rpp5pWJGmQtOSmeQHyNEA/4JnhIRpCeifudajIvInCYzDipkvabD5pKANtbQ0rhc+JJLxKjl0dL8jeJrAC2PISAWsndMVFX7TnE1v9GVCiPXwtr8Efw2Rvr1Y3L0zWwfOkfdCs6LWEMjkcnQ6PiVJq76b5ffx16IpQS1iHaYG2UJbFfCF6MbcTbWwcLI2Dpa9IO/jW2t+Ax+soyRFjT8DxDkJqGiTenGUuqLLHXinbJdjtMm+kGx+7L/gkZXVdK/G0NxATiE0KdsRxoUpEncCeT+Nau0R+FEQCKkcGxa9S6qNiglTMha20ObYDJu2NgpRPR9983CdBfoCerOP5KFziw/SsMxsXKjZrG8gqQUTn3GA6lXkmIwg/ajFhskZyCBUns8SaSNGRO6e+QgD4eYe404CFb4ZxCLTV7EUQOHhscfBeq4F6sFniWLePBDLvCMCS5Ro4KF828qDWslWLhjyM4l7j7fUyOYpIJ/DDbIeq8gUBOAkqW0kCfXcXYMXKm8b+9R4DTHVLbZ33Yn6YjeEF/yGC9Y1fuKrsaDoIGD9Hgf1AtUohpd17xrgpUyb03qMOD2sTE/ok/9jXDSFdfZ4OIlzKALt54+oxhdkCYWOe3bDbABK7dUK3Vp3QGBAdtjaEL7D+g/XBo/xkb6+l6mOMhWCp9PlGQ4JdNVBoIDoGi36uTTw/O8g0D/t2SfZQ4JBcaUgDIbxiOZHCS0A+dcgRb0fXNeIYhOxWq0sjhd/bUQjmkjq5AojmxQzSLNHbFfveJw00HtUzB2IPj7vFGl5eeq6l78YM1O0XltdCDPPUh5F/05UDvurUQuIuny9TK6hXmXhUsN7H55eyZCaQbikc812ML3c0dKb+tE5QrUAK1KPU/cdtfAyulCqhEMYniZKcxO8GS0pFezflLmio1PL94bOSsO2ySSXBZzd8JJuOdh362n9qynYcudRfqYyXuty3m9cUcR/HgO6drDgBSyVRaY+dsZJUfCgblqnn6vWLtYcLUohUpWaTM4ddCX7+4xuafGRwOsP7QPjivhQacR+/264/b1yYvGqYThKjzotKLf00que3jW1QQhMix0uBCmbT+UUbfx3fvcjXfIPpKph7iJstrqs5yPsJXP5DLEofIrHjqVk5mUvRXPKUCC5IV2/M4G1KRFhBzq4UG0wZrS7lPi5O57YrXuQ4Q0UvBkVfhRDpzIa451t6Lay+FFY3KPS8Ggqy9UBRDRJCHb/DeyalgsnEu8nXTgX1ZYF2RUcXteMBWlG6bBUENHQDX7XxIctJzbriEnx+tL9dadfsiOxOI1wN2izq5/p0yqVI9vLNSMQYprnVr/FPfsHonS00EyUyhLt2ZkWPwocfKld/4aCgz5mmzeT8hPazNhsqCNUrtzEpuC3r5mrePDAXF8JLZvvAMMUXrd4MXsOPIxWZKivJNBlWiIC2G86iUc3PsyMh58TqKg4QWbsqxH2K3q5ZkXTM0x087rCaX+fuiI1hm/JQ6gvuCTFt5hh1L2744bo5OMe+bftxIUx4IvDGOczkCH96mphOfALeBWDe1okGGxPyMTIKrUME63A/eRp3T7LqxYz4NghGspahF4RAwcsXPCilIi2fvFTf8mE5q9UhFsRMkVqfmGeNrRCBEI4/mA3Fc6NQI7WWaTy8+NDZtZH+NkpWG14rby0+3wZ5XxJL0YPhItOo/U3+0Fnv3B+khQGSl6tKAgqJLH9RhEuVK5Pkm7ILGJLxin0Z3uM+/vZvBFQC48hXodiNkZYrM5P3qxLmZIyXqamWwVPB6PYEwbEhb0awim99qmTDtW858JM8AiqyXUootUuQIJShpnsj4tuoluABvAbOelAAHI8O5QnrCA2cOV38nZO5bUEqOVf1aORw2TDooejAs/xnlzgZ/R8YAE9isxQpumjl8rhZlH0JPUa0Cw4gWszHOISPuN/txsXrrVCyqQG63V0qG0+bljtqUbd/oFhAOMFqCQkpW53bLQrFpRYzm5ykC5OHWVWno3RfgxeywgrPs6Ge+acn1PkBHs59TddRRfJj/9fxTD6Ufcv+LyjmXDM9pfwtIlA+q1q056+Sb4b+qzSxXq6FIH6QzaMV9QBGAdZVqzvxKwOGAivlcG2BFcdHS5UkNdW/YCbLwQaQBccVUnTqWsLuAQcyJBwnxucpOa0+dFdAK0K5kNHXYNtqwsLKOztZJ4vsJxrOG9A1wPD/pPQw+NsbgD2Ng+2acUfOuhWM0ZlVYAQHsJbMib0q2t/UiZvszBmYUJ/KD4fO4XDHpa+geMaFvnEVuwMRsgwYQg8Ya0jAfTORL6jjSFiwc/5s09+7Ot5aH2WAwwFSthFJOooQtyJ46vX6wao+0owO83By2VtJfFThZH8IoItifP9yGUn+Nn/P7QPdocIxVD5AcLJUp4EPUVbCtyyANqOu3hPFlp0rJ+6SW0Y+ezi+Eqx3+xmw2wPu2ypqQjZVJx9ZsnhTQ6eAEXVQNV0GF9aHYCKY6Y+AAzuG8IvOr3f28LGhb1r9h+UoBFqUC8MAOIn1mZzxDfZ51Z8qL1GpIJXwoNoQ/GP4Vh04GN8FgOqb+UHBLoxsBZBIqy/84x1jVH4y2eYLmou+tlTuS+E2kNbMSxtUVexhprkUDLJwQZGzpCdTCOebTCIgNeLZow4QJK8GWn0M13c68bvDxco57m2qeZeAaDypFmvdWWYfsL0zjkE0Yw6v+4lJn3HmbPmtSQtiqygWxez9Bx79of2mub9NO3mOv9bh80v1SlUh3K2nyvN1NAKBVlcqVMVnF63mkjS9MVicuT1I00bvdv2LmoyUbQd/tBs07QPtnpOPCFEWyC+X4cWi8JMoedoZ3DhYnUKn6I2NGtonw7pFHi21KcSaUxu/DX2C0ZW8AG1Pq27VEjdmwbUyBgDlPrXKOqZ4Q0i2+WpwVLzGY554X+xzF9H2J+3QEFru2EKP9E4i9HrvVzCXD551MgyYd/Sv9vwsI4KweFjrTRSCZpCQZCleEsMyrIO+ppOgK2+S97f/KmBV2DfzDJjuOuU/fSIEf2DVBWUv7/VWopD1dOfMJ1C0VCrVnl9oGChcWLfrToLeFemJZsYMUwmBRJYq7m0TYmMNA+jjYy32v3rGAloBUPhCY7GLf2kEB51PNPxUo1kUG+rjxjrAK73HEwFhKbw6QhA8gOVkzp67tMOdnEvb8rk1mLEnGHn5CffAflb1QiiR8vOClYhF2ZejCrvqUsQH2XAut+AKUUbSlD+quWWsT0YiZBiEs+rjy3NgVwNQC1PAmnX8yzih9aaQoWoGg+NslUpHtKFIjzzalHzdvtZShpRd02hcj+St+wsL4sA30+AtE9qXuEskak/rR7Q0Fbj58PiQ+sAOWNwqEIszRZwQVEopxR4pBraEENSy7W6oMlEJ6HidONdMR1VZmFyeg9ZnZZ0+s1HoCuRi/jX9xjxcINpeliIaQKlw4oiQilG9bdNdq0LfFMFpTtXp8gwCu41UmV8ZbNI/e60woB+gpjmvgu4KBCZU6Qll61y62tljT6QJshGTx1I76bMJYUk7QnH7hc3eXDUnhqkRDDIKKcZSvQ2/9Or7gEGwbW8fXYkRX2gifvSOX3Fi2Sw8lAS+2WZX10GZSSOTPzE6fSNf6X2S4zQzQI8RxftqYUlXvb2PDDX32I1KtL1PEkrKU3P3zcWRrcOCsTry1JRFP2exGSiQ2UxltE6nyhTDzLs4l2f3QLOXyKnkpOaPb3VQcQKlB+tGCEMLoAXk10wy+Q6S8tiAULTzCtuxH8XBVvpIla9A0msouwhcNecTbPpyqHepIdjhw/j7alnDc403mEP9xqCKqH0HngKmTQdUpFdG/u31Mtm7YmSsdiOAJQU+DvyVNFVQ9lvUyeaOo3E74pqjkK/xypFyHdtRADN+3EX09CZyKx96xBo9qNk9bqyQgbcTJ4U4IX/nFP06DVB/b5EpkbN1GLHl/i2hOyRTBfdNqiZBYcVuACN11trE8/8OgLoCN9J98UEoz41eUmvd5SmErWf0ycQPbjXmHQUbvIlscIgjrBm1GdHhR/4Qpm4CY+pObYJ5BSEQjwomp51VTyQF+pDyCx6RZrVxFzgP/pFviXptE33SCvImuXJyEapIhm4QtZUpTTce29TPPevLrhJZ1q8Xjim52j7a3tb8Dk/Mv99/DgShluuJyNYdLKgXJtQb61hqXfSsL78njPgylYqMKyJ6wjj4TZ6E1fxf3jAcAUBXEMYSOIic14y6JDOGUnjuILNVDDyL7sSuCpmo3nhXw3zMxSNVqKqaJQrc8gShzvzKtPRJ1pzZSIZkrEwcv9d8ToyjSQzDX3Jv031d75xcSZgUUSJVwJKUImZYUoQt/LZRiRr/IukrPtd4516kWnYvsuVBvt2WLgtsqa9jYUhN1w4+dYaITaTB3XK5saAKHSttXvghvksWt9BYoJhYz4M8gL5j45yr1qhnVZiWshslmlZmoTpKVBvgt1jJ1qhB4j2PsEh+nzYzrdZ9xy68+uPV7XUWnxm3VHRRGeakJlITk7FsMDAUJTSK/z27bbH/aqxW3oEy+WIpPougwudCp34diiKiwjB0es/odI2d08ty9g7SMuooy3JLAKqd+4z//13Y0y0jJQMu+1ZT6XF/5nyAlcMDM3sJJxh0dH6Ir/Vze+ADikOApZ9L/Q0898/RS6VGjBTk9lokf2liKYXOyEtz3775qxQRJQC2IdiKTziITVOSchKOGphyvYVyZqDABoakzzK8oq8nlRyOMuxHpucfWqMbAnMLCEpoSCZYot+xXj4W87Mmxke7QCCBmHqihcEfT1sATcdNrJyoCmEtcqsgAkXt1t32/fo8xw9z+xGaTsX0v8LJIb9Iz7RKc5Qt7sb4hr/dvMT08uAjVk8JZvblEi8jHhfAYaaJWVEvfBuEpd7U5EGdcHb/m/jY28qTe0HFRX1GdFt0qxR5UDKypuNAlx+UdM9IJEZsHDgD9syPZzKpGVx43DaW2+rNoLloRejhh9d2NJ5LE3Qk6bFbCV0I1fi3K6e1lB+Hh78rV0kO3bUTLRJEc+K2CkYuJ9BkAC9qzBrdJXFDImMa3w4ogmOeu9zsXz7zZohZR36FV0zgBUDWAumrowZzETAKMCOJYE8Gt4ZSJ4/8Jy8CXnFo7nJL/UsfXLdxjocF8Sbrmba0FOQZrTLNmxB/+z5gr8QgBUbCBZtToO7shhOGvuWKtUHAwWUjVQuwRphaqlsXN2IKhJ7wzSlJlB5KiFRCWfCDvlsAXmumSV+G0Cy4Fl9tAEg+l6VyOB4d7HrTDyPhlbmMiYTgs/7YL+WDdKfyq9NtCVvX467VIx+Og5VntORahEc519ST3d/baawXRkLODXlS8NV6Y5GQxKrlreQc5dsTQ7td48d9wwixtIVMSzo6JKBkEDkIGpR7NuPrx8opiDKquMkfGqtCssdls7SQNVEkG0yyNTcL1yCCoJy4uy0NMNJuqO2SJ/+dO0s49D8AYSA6gcSc+ff+OIPghR2ulmbsvpygSIsk2NhrvlLSHm6FbFMDM7opc54Yj+L0bp5OBsNTJGYChismac9BrBgrWH5VFI0Clo5XnXiefDeyh0mFPY08FzqPcvazCSVQhjslvb+IovfE54OpePJS52LQEvyBUY0dycnrro+BSSdYxH9nbbIvOPg8FA1s26JBz0EbGK31r0JC3d5F1DQIaB5xLJGpL03na0osMbKHXsVCaV61RGA4biqVcWC17hE50sHPTRNTuulDnc955yYi2c20hgqZRcKaJ973ttWgksYNd7t85x9JFRG947t38bbdQSzYU1t5VLtrjQyPaWxJ7uy49rIwB5CDdBfSreOSp4Pm3PpZxyVICivdVzHX9qGC4hiTaV7zfoJ9Gl1/CyPJSrpS5EUxCh+JpQ6ElTaEPONtoMSREKHYol9x/5k6YZcUyh8xP2sdLwvv9nWCtuHrb4RQTWqBR8xWhV8FdFhFrcBi4MB5jkmkjF7FntjjAgcvumRdOvvfnOKWDwFOIh30faf+0ROX6cX8w3ZAlch64MwU2g2UgBTEIuDkEiV1TkJF8QybCLNfXWMf15HI0do4bPnkAsO0ztOtrqzGXiS0x0IXaFDuBUgoN3sPVQShQHv97YenZmoAJV9Mw/znofXzB1Sv6h/Qq+eiWYB7AIWufEM7cXZ0amseuEmGVGji5uthmj/KiH8iCSfhu0xv2/pQvdmRZnQP7rI2rfY9p6w1o3F4tQ6dFqFPJbhXX0i8T3GsmVkzfb24jWpyvlXC3YNcYf7CGG7ld0pulxNQG3H0Uh2P0/re0V8UsGrsho00kYFOxD0J5sqpzlgfeTov4fCxOJePMBSfHG3nlFB8Qi8x502VcP3ZO+CTUK5YlU6iTTFJK5F7KOcgvVjrU6xoD5bDeJQC71SDsXq605OjTqnH//Gi6m1SbPNPRI/VooOMr5qhzKfNUBIeNv8LikutIZbqMdJknGYhLXOqNtCo9BeffylSeHoTkNS4effJ+lIeNEqP6qY2fT/fgbaBOSdXqUBwjazH4y3ge2cTFLjlYaiybG14YxDhjlOlk3KUH7Fi2H81GToe0edX0Ru4qjuhVFsDN9a3XDey4mPreNuzi0BNksPljFBX2iXYLDeEYAHCC5y0RoAoVkV/nCBwWpYyoj0E4Mlh7bIKxrOUfmucHVSQ5YcVpyKak/BVNY2qJsliQxpHqW2e/g8laxLg+Yy3r/l/9ZEIXpVZbUg7q2oB3FGijErFTw0HIEBVy0CPeZJ/D5ah1WZT91G/H9fVgsYiJUKUide2eouPzkuX3R2y6xvKM4H2Or3ooduV1RbDWEhLiRJQXAP74gt+YYJbFC5pdouxzyluDRoRpUdJ0taJk0WLBFn3xgSil52EHuHfsmrEL8HXK7VBuUNHrWMRnsRQ2n32fhk+8lnWRcc+pLlyce7L9UXAoMsodDkjTMCqKbQZ1zzFPswWTLGrnnmaXs63U0W7W78nZzePlMKIh4HqlG/cyGJ0DvpMg/DR0q43xANARlaMgJVIpIKYGjBJy4ktJZR0i8GP1DO+GZYU73mbRN64cBRKWVM7iiz0AvqftTQ8HHHE5CiystT3DZIbgyUWJAwJHGY1EdUU+PtTHPj0HmZ9VITTcsyNG79fsc1iy59hm6xxvw8+pezYNQuVhcmjYrEm8y+z7d3ADuvUDlaqDt8XIN9BqVnS2kBDkGNYnUkKYWIt/Ozd/UIl/MQRorLwwdJSA27njQMV3CAwYhW6dVd8oU2cibUraDxn3oZLtqDet8QaHQS2+qsQdm0N3jVM9BIsNm3DXzI73Xe6CyInIMNK2ZHygWftVTnQaKUQG5CVv0roOFdM0jtI1oIhzkiXksYAc/i5jnssW9TChKVdhDhPr0lI2WO/zL4qaZRrxx2k5jrEThNipAk3Y2alQc0nKKtESZLaos3ig82awA7emB7zo3suoXzpZXlbWWNgLktiHl3RPo69hVCnLYjk/uY6P9FpbSB88r0y6jqBg1RJGEHESRbdShXyoTRi5nhnyjO4DSt6gvt/43o2JFGowWt1ot16oeAz4yE1hT6sBVQTvPN8byJrvtwkP1qdQLmZXqiAyNK6hDez/zPf76rZncqCWReaaZxhVcLQfwACjNghj54c9NRFZrrfbkU9iRoCPUveFZu4aghDAt5+2WfnwtAxY7ic/h87avfTfEJVRPFv2cvoc7duOz3O0ey/RDF1LqDEzbPhk60MQA5G8vn0tC7jYkI8Ra6MnreTimgl+wEjQUtPPKTXndyik347y3o9FQq4AOO9zYN+STCXAE3ll7ijuV2eOiKu8gmw9vj7H1IiGDgGmDJBrl/hNetcu5dQHYTj+7QXVNcUQET4Xiv1m04XUJM3KGHPgUoVuS/NPMWeBHZP1oBFk8VeEsmhYLv50Dm/bYbZa0OXbaP4OACALCP4CQ9HIa1ZBQEVl13JwKzNZd7WRYr8ncseNwCcQMbZqECnw74De39bVp4IThSscXH3XZ8uANSpgrZLouLCETdQoHQA2TcrH6YxsOMwV00V6SKBUAFETlFEAusdrWW5OBbEAfruAy8KOe25qB/Ns/LVs5Hq1cS30LGdhH5wA/42A8Ya5w5UWa4tjficY6LvpEez8MVgYfBl5NEsz2fxGp5xQo8R59MknZ7U6kkAR6yOwKQlFMTD1sDgNb27Alq7DHy8Q+110IQprFRtx8byOxvAo64OUCfrHliT1g50JkcUTMSwCMjutxCIhos990IsTLWByT0SWD3v4jRwVwAEMG4Gc0mp2nUHVoeZDUvGSoU0C5LFw/LaRe2aJUqgnzBYO8YkWCTCzsqHans+BflTWhEPAAoSgMVtMeg7Nv0Ujl/kdvZCUjjfPN1k0TGtLU/jupEq8YMPgXi9ZeSgqHAanmoalnCWoYYBssYq2BEwncaFeD7jlz66Vc9me83i+OgjXoDWcpPx3BeeeKlZDqDM7+t6gMh3rTLgwBt4BmlMIwBG7uxHbT1oXlN7T3gAVgwPj7Xj4ses538ABTIGXR4IJodhnL5nK9SVOq/kBMtJ4hJRDd3gxheimocheXxQGSFc0vGMQWMGfaGNPDc/EdmY9ixWJP4ELBJq9NA/d7lCwI2ZbqJGnr60LDplpxUS5Dkw3Zx7Grkp5eozXdLIAmRawSNB2VmLyz/aW95/mbw1dTu5Ohzbtd8jJzFxMjb7s/MmUkHtFtReCnWSWrjV3/IfLEadBfGCS9hMPgup18U/jSyhsyVyQzJZ5AV4qpz/CTqVlBQ7vMIC1h4+2v+2Davh1MC47aQYKzk2rW8yrekyxOAqSqaCEWdUAPyrW5P8QiXT6/RP2SD5ds5hGbxihqWuZECwYNJ+GnPgklRsn3rr1fBfz3veP6M09H9oDcij72TrO0lo9WSd7gFVtq0XJI49HC1TsSxqzy7YmBf6fPHz5BUOdV2gZPphuZhtDTDboFRPsaXMfbnwSidYudQ6AwLSrWvEYjGluLuF/gryeM4dYbT6mziVapayCqwZu0TFaLgHKVnvKiynzpi9Evhe+rM/nwN45xIcNQBa5IKDJ5/Vny35T6c1Z60g1Yv0sV+48yT3Rhayx5S+N3SA8O1nEdDDh66gP0xHzjimCjz6z6amkB47V09FI6+lySDvn1xEc8qzJG/iw+zeo0jvtCRvAaLY6gyHhsclHE4uANlLYva6lvfVTLqKQKhQ0bacpY+5MLxgDqh/XrDbGn1yDBfELxdw4Ol56nDmqjbls2Zlrb2YotG5Yh9K0iySENlWXsmF4InUmM9kVEV+S5NQK7phn+nSbN5Ye/aU8okIEJX6wi23L5kGDYd1R7ySUL+L3fA8ONaNDYRD2vi76EUBKCa8IQaimXu1Jr0mDhYDk6pDzRB/PFikSMREFtiLTeFJ/Bd+ilRrNfCAgKQtoj8z03Pcxh/NQsvn0dRO6zh6irnuI65fUGV/arSbyDAjByrk5G/RLq78FD86I4I/QkRr4vNzucEXzsIbcDkNHHpf+fw26EjpcLU5GPjztQ9z+htOiCPm74hLjvE1yr7Uju5z8WzRxxb7sXbNoycB1M4gFXc7PLh3xtJ0/kjCT18cAmMTe29tnKa0XhoXtzPz11ykv2UH7/0WmQIfV/nWT2Uin0aa1I/h8LcbxLZIZZGvZrCORZIz6yiCktt808Ml8eE+TV1EKLuIDbZbKSu61ha4GIVc436F/SyNbF9Pm0GLfJQSRH1WO19YSFmNsFAM1LsBBPwTEOCArVI8CgDK3AwASS08J5VdgIL1SQhglFZ7BZ+gM3tAZXH++Ke59tXWVU7h/fFYbF+ZHvLWsISO4K1vYdv6z57SxuiHe6WoO14yGKpbtJcc8bTBQ5pJpLZlATQ37dqD7OOwPveDYLhDTdOBJEYNI+u0PwJFmx57Ds+BbgaLDNRnnF+7HYv67EJ2+vNhVG3YD4sNzSCnZ/PZm73OdSA5Ze/I1ts3W6kG8+EUQYGvzvBJNgd1ttfWoCNsHdE6DCA1l8yIk9ZOE1/inCBQDdicimtjuczu2e6s3C9xIkCnasOVPslSgwxsTA4hZWZyWyqV/CqxYXtmAgCqN/kJIwVyJ7hDSmkSuV+VwRNdhFg+UwmpfKp2win9tq85C7BsjiH4wocVBQhg9s8K32yYjUV0tLVPEsaEUkk8rdUxemUToQTqhyyrnu9gS3klhe0TGr/MKsMakNFbXm/uo0aMQsR9x5jY4DSzds+QSVm2JGlbIsXbu74y2I1EaZ/gXkeF9GV8R29x6QOoBZjOcjA4gfsCxrZ9ZZecY2gs61gKVv9eyQFuAZQUxcg3x7iDE3s20GY50CoGOrIKvMuj2cCiHTwaaEB2J+l4+brBY5B//RHkI+1CXg+FRCeDZIZ2KT8jzlQ9PHRFnFfaU11IjuJHdSFu5NjFOH9gIchkzOlccrx4piDDJCXT10eQVTXTgrcb2RBqmQqG5p6bvm3oGCS0R1WfDMNmHDuCzOxdN22MEv4yic4VHAWL59GO1ksC6bJnMAaVRmFLKlCgQbOyVaJYS4E0KatmnXibT43m/JDGrVmR/snxFGUIORX9L6G0DbDWFSuCObkzxEapAdMzqP0oOy+KZQwNIHZzwi4ZAew6jfpLOCuFkYEhn45F42lUbeJriuU2rFdrd8n6pO1ctpiX5fYj4tU6lF4y0WJD1H7gilZWDVyxGyk22K6fSKpYQ6MCH5yllV2++8x3ifhOo85s+sNpCxhO3ZHEcZc7tx7MrOWWtSSd7jicrBf10GIM7zlv57EoV3KfPQOqqR8riJE8o/6VeFuZPTR3OnSadBF2nM0oE3OBdrbF0h+FWWm8tUyoUNDrPb+AO7POGtTHf5stHyjBBB/0JHsefhnA/NaDCmoI3H5Tkq/C2HNAYRwPx+asEP1UKiip4fLLIMyN/ehcRcz9ySEzPAYYiVDHrxBpVGWKz0QiuBjUvMTbjzWgvREwuxo5jmQ1meDXb9jRH9xvZ8EwWrFz1j0ofJTEQpuXWQoRFp3qUqG7ZHMJpjxZ5gNnVhXjf35TCHhA5gIdj4kAW6E6hVyJxNsFBLy8aehvNbll84hE0/jr8NLj4MpVB2J+QEw7vFYG5m6/1skconNoeXBqsEkR4ScYOy/oJqFzPo40vB2T87irdNFBoBmnl0QOufivUeMBOT72k6UL/6ZZWiGfjU0VPE7Ylx+wbA4Wb210YQq12j6KABRB2Gw4pYwvKjPtmcW66B0C1pOEG/TnMism9Zny0pzHTyUWqUXMRfE6tN5//K/D3yrWx7y6moqK8CFWUYIE/cliZnwoAQHErMb8s+u94IkxiU/9sZg3zNE+x3v3RV4aT2upG44t3s08zJkSy+O5aPAyh2Szv8/mi1VVtFS7Hof+mdcQRCZqejRugLmhF82C/J4f726lifAPG91GTRCKizmtQfWXivIdSSMqALqTdwE/7nD0KsuSo9+NVuBr2G01CavwWFmPIqOxDjpxUIaK95k7NeG1F6XGEyCUDBSai5n/9oGZYtPk8IFjmmueQucNNQbpOv6edUj/uSUPI3XYDdAilHndyITBS4OL1Mv+WNjj8JuCv7RLU3DgXjiS+3N7EGxrrolA5kXm1AgJ5yIxp8EoAqhjGyQLCWJueXGOPsv1v1T8/ABYTGQ1uQWGBDkRbclNTIzisPG5H03mSoZR3u9okfQ1TmlMxOPZJWUTmA5uoMSQIlSYBOexkt9biSLwXPtYOMEj+v5ERgwLQ7iaeDIihbLaTA/CSiTCv3oZIMibDjSo16LanhspHLPqiU6rDu1T+XIJHvAFE9l0QKhpt5vZqtLQlg02o6dfKcKNhVf+kLR7LY9V90LJL9XQPC5Vm8EmsBKhRBxqXMfumfyC0drHKaAYtXbd/GxaRkdYi+c7WxLP+CXOfbinDDtStjvabyV0Pm2Mw8o4ytWmcCM0DwJcElTVS1/9zPfS64MjNEA2i7kG2qqySc9BLdzXaWYMZK/7/9rs+SBNraydeQaCKgCN7XZIYNPTrcFciY6Sg/jrIc3rrrpd0ZQlqI9I21dgXgMu6tGzHE2sVRSidZyQT6pY355qJZeMsoC3zuj3yPg8TcmdDkOcHIxW/Cv+iojOYm082dWD9zxlN+eKd2lziW/UIKbb8eDNaARbBTfHqBCOPfh83/Rh/ljcw+CJT78GyLi/+sASa04F//RsgqLkpkIv7pmkYjc4FRHrryAUypHyVtcGr9kprQWJzb5TouhcnXP2I12LwfQe481KtUp9eNtLLhMXLv+V8WXA+PhMxGLbVEv+/MFWQFAWSv1pXHOqFB9TIm4bUW2871fKgN5/bTw9yVFWVzvqvbZz6nVQn88zH9CC7jRMqpoobNiqqjxXiKJPzFgY9Mrq+layQBAoi9HqaWuA1OSJ74m2LtrMpXdqji34xFQyt7XYyrF6yB8kpk64cOHezGvvWobnAloTye4WScNWeYqi2da/ZJDEKFoPvtxuk7/IKxzHmW/USqGtSGFveC9yane9AmhkAEaWXGVGEMKwc61rCgT92TAgj2OW8g2UgsJDb/YuQwca1grgFjoVEsnXhAiLZgC9Ct6P54AQUo15A8sC3VjoE5+8i5o9ndgZO40NAKGYoGVrqQsNSEDBzinUWmUZmE0PrILc03twtetw/7RIdtMDjDnT/hYioanpIYyXCgfbPpN/RiHU3PXUUgufrJKDPDlBCRACR+gf/eTF5ZVzfpBPrZMJ7VYw+U50LWP9+Gu5aeX26Y/X0zM1k7f2FGFmLE/rQFvKzL8SZR1kd7FVMSblpJZSxnYdIph5j72BIDViBTHYZT5XZpql+xPkHws+pXswKKW+hZKmC8YBfLd6d1csN9EJTY/GO0NRgPaQcIZLGk71DpdT/9bwnNnRRZCqaOXpqk3DyqHILo1q2xIq2Ak06PuvW9c1VTsqCV9Ro/CqAuLjCoWGD/DltLOADRNdSBVTB3xE77dzXWr5nWErY+7ajT9s+FFguVqpl1Gx1v1WaWHcY4k/7+9Mqbvxp9GrmP4LBW6WYmGlG5ZcZ9r036EKXcea1Qbr+ZwWL4Ej3Bp7RjhON4WZGMrD7p0nPQ3wZsdxyP/KO3jYZ4tAxZlckQ+dN0CqgGbPUFzukFgP0ySaIDYJwFGzbVG8WkywZGl6LUBNP77D9Sn3n0vWOft2wTyihfmuDD3F+ECpxVBxIz72XFNw+eFD8LH3BYx4xdTdsa8cCBM3DJGVOO6eveZsHlR/PMs3pBNJteNNlBGVMGqeesNIwivEmmXNarQ1oA47LZlwro2b/fNFenlZsRbcWXxSyMysOmOGcvKDGYMmisMPWqQ/Uk3qxaQB66spDGYPaCYPO/R2nwdccBFZl1nLQuL6Aj2t2lf0zh+GwGxtXn43qT3yFum4khiTMudNDEc6xkY7mTwTBdBdzqGje3/YPGFx8syEqWNYf111byguoCQPjyxaNYYjZE5d+R5lgOcduvgT3Va8fT44MZQA76aEJb3TrpSYXJkABLhbUdIpumxrjWJH2X0H6guU3fVewzSi9UiHhTjHyts7KeUh3lM590AlmdRf4SL/hY8WSmQcNZZRjJhSya+FEtpilPeajAJHfQCTXW1VNuyQiMMm2KXKMx3fXj3bY7xsQMeD+ZdvXlbh5bePqtXjPq+r17y1dZgjzz6mnm/1ZSxl0pFfCj4ai++dpwbzL6RvyJB+ZQkbIZ/gORS2LniQiWyYx5tFReXyoHViIJNMdogPydsDWco4bERLAQ08Nn/hTn70uwWRrptDkd6berfwG1A+QENnAa/wAwHOKTmU1h9zbL+WTH0yjtWzpVfJO7QPA1vaZXdluGXy6FDUdjXIZ5J49vbVuL0Ba9GS7IhLNCvoaV2Cppk67s/U2zBKQvR/02OxiC3t+/TSpLUAlND1U/v6ABbJxiDjjCy3HXpf2cPpiYGHfgtXTqVwe9uzazCP5VCVmNZbG18QInpsilInOO2Ts/Rt9bZ6x/OxcGkQEazts1R1rSJH59UXaUtKclrekcAoPuq/Ox6dJ5gjNDEFMUmhCviVatOqq7RHQ+DxOln1jUShdIPe+AJI2gq++9b95VzwcMC8v3CKXEEaKVm5NsWMlNP3Ql7ii/Bp4zkORvEArdLCaMSZ3sk5HlzRz2YBudWn6dHzV8qmKjCmqRu6Btk8/m3D5REp1xAdufF+wq4mSaFnDfgkQ+SCqGHXCrzQ83cnp0KbeCnjYgjewXug/Mm1W9UX3SQl13FLRGIUbO4h/rQa5xKfr22rikM6EEOUZuCRXszruzigULXXnUKtllfhogEsrW7VV6SgmqhWK8VOqGbzlTKwsosIoyupbDxkLjKlPGQiaa3ou0QAqdWbibyGkDyM/HtK76M6bIRm/mKmZCiizPmAOT8n80n7vbkxkrMlf9Ee5yB3TfBD3cw1vHVU4S8RijGy7x140cK2zUsKNgK7imZUHjikIZcyV3qVckPHFOYjA/07gjo4EeDqFk7v2fsiu+4N6rv6A2JIOn1CZz5BISrEqTQK+DJTzE2BPbyGxDPlV5xTnTrSICMS+1VNP3o/SXo763KOVL1fh+9OfRpIbFTij/9cL/IPAlChwsgB+7MzGNtx5+K70BLyNbGLdQTpeEFtXoO5GLncIFB8qwk9hb4NW58ui+uMDGuEG5aOSSAEHjlTj7d/fWzDatM19XO0yoV0pY2oAc2RocIAyW/oKfwFVOJq+DqPnXIlyCACVOQAvYBZ7XC+lQq26lGMsrSYDAXAwBRDjiGQ38QXM/aizmqem/zJ2C9FyDu+/g+pfaj2l4sCksqf35l6HN62s88QLHAejrPte+/fINEOLyvtpZWpRfHiYlKWsP94yFYwVLOhSs0NbhkQohGrvY2wZYmH6FTA0EPX2xkfPovWld2QKqChVBqSaaGwhkmDrfdxZDiHS5+aTPD3xsFDU5fRg4JkUhFbRUD4e1eOIUeb14HN25KGry98PvUoNKzEBY+R0UYtnnttlr7CYtXIGkx+F8lbsbCVIWzvx7bl5dyuxdeVZTuV3FDaKpw76SEium9VE5st7ltyHPZzFZu6O9e1kT2xKHMU5N7svqPBgtyBACrDUJrBrmv8DUXJ5PyE2q7z3esPBEaYuW4PRZL90eSCUYjM9h5K61HrcZ8dr3LwnKIw9LUWX0G1kL5UBYOCe2cTj6uICryyzoSE5i9JQixUGRRef9rprAyfKzVc/f0g3/UKxhuTauDuHSowEvI12f8BXeFpVsiI3P+1ANo+T2u8HM/Z59KIlOIacOSEeDEUUwfM9JqZdiJlxA9Y7UlgvQvw7KuFi6ahKf9dF8C5jI6km/5Iz4/bklbLYjC3Ct5dvD36lA+u981HfVd/q5ESZOx9djEYqm1KqBIxIzcXDplY9h8y2HTJL3t8/r8CL5KSWCx2D3pPrhsHKiG2dStwFkyz0wyRiTomyHLzgqL50FtUNL2ybQFYOoPZpGEWD4L6P/BP2v0L/F0UyMAJzZCbQMdErGRWMQobaAHkiX3lnbSkPmqduy33TunICsqDW0ubxwAmdSDEdzCxju7bk3Kk+brzaJH4auxgguQIvt500aXDupzvlmVDX4gOH+6y0v8mliDXVpWqg2N54und+L1X02qVc6ZsEM7TTsCSBCxJq2DbTDjneDQEz3Z2CPA10Xi0XH2AKd20tEcRKTclBjEbaIZ58CL1tuolLprf3tUaOpexDXrzL0wADiMYwabkilvlxaRWucttd9mqdtfhf+geRWs3KqWUtDEo0K37z8NeTxlVA+GHTi/MJwNQTR+Yyoiv6xhSPc8uwGwCf4+0Cv7IwVe8yWjkoGeQg9l05aL8/+udmfPxTkwkhxF8lhNEjoZC5irAfhJ0nYzUqGASDt7MUveBPIWHA/wIDegWUK92X1vVLf4MYlwaIqpWhX1n0f/c7typ7C6NzQKabUljs1kqNQ+dDivUbIvHse8w+kE4DvYsxwaSXEqnlCYXKLkK2FFApVbwudpWJQWi+Q7yuWiWWFHnjeB1tkq8fDkjLrHhUe0z2/3nLuO/a8IxSo8aG0f/2XutUld7ZXdicEbRZV+GhuBF5j2B8n9SKzKy5q7IJcUW2EWHImO0D8z9W8qAejJMMo1JGILTt0BpCqYL0ZQDLYYlL9ItnZ4ngBBA2QcpuBuYscsvYwKPGnGOjHM34itETnCWAgdafSdIVAsrlyzOClhCaKit1DLK7sijbN6gb0iUJRDO0xllMgkAZNNv89q0H0VufpKI6n766H29MwMgHazKvqDxYr5IXhjrFBA6bVRQFqnM4C0/VO5+BjZx/PaYYmM2X8T9Y4zWTi+E1cAmHfqDtO1fG/EFyfauh6m31gmxOgZILotOIkvvHJPuXoA8O6I25ZeocDYBP8z+MxaBoSwQCf4WjVqJOqcVp5e3YcYSa1fPhQxMwinZxT/dScMmaccdILbeYjpGeIGiulepAJRIzyanAocJitVPGrFTALLknOnPksUkmcEj7R5xo3rSmEVSn979UmNuUsIq1ykmwjHSOx7kF7P27u3Oq2hrOAPZNuAfgMzOuQ35/Rp+/XvkzFwpC/x99vsBkpVD1Bwlfcl313dhpiAlB0BbBZ9lEIL0aL/rzUGGFukVsYh9LSIndUpO026vROUgaO2i/ifXq5Apa5yGV54jh5EupEYpY5w+nZnFQ7UDZ5xee07WV3BEuNnpNeqKYH+f1boF06u4xdsuwkIrMHbihQwLVuyZDlDyIhr+iau6/CAFOcOyyLl/AxP4S1DaVSuVqlh5ENnQ5OS6CM2Or1h1G/xvJPZberYl52N3kEzlzrktYHZQHijN7DvkQ4A5L6B8wWuXtdV6fQnN26mvIit78Eh/jacP9h022gChvPo6sRdKeTB9KW/3Lg3HH4ZAAiylIc8TU51wD0Dy521d3sTDeCAT8lHo542wb4R+/3NTplFNXXUk6dwPldNPGjiJHrgfHyEnyiNu7XEorkEz/3wZxaxNLI0H/zF04cCnfNPjIM2XFLwYbpquQcJK7rTY1fNxuJxxFQzQryNHtRZMiIZ7ExVeTfVufxp8HfQQX79iFnVhiKMDKpRpH6pbalkBsHTs7MW4NUW2XhteRRidaUFb6TIHtElzM1+gSEkanNZo7UOV6tXW8YiVJoHHxWHeUBpQQugiNNeXXzUgdzhaUsUbLni20I5BXY+zjzpZof8iY/nDSOd9D48xjp5LKRqoKW0zjx1ujTqGGEbHPV3F/OIraGVyRqbOSsV50lA1W2sAgvRbV7nTb+W4/WQU8SyhHgTzZL6Aa1n53/V7k1EIiYI5Jx964hcUGYAFDKjJAbK2z3L10ukW7zTqLgRaLIE/sdol8djbhjWALwvAfvRD9IZokfUiCGLgHZlNlEM/LNXoOMO1firsjAXAzOi248fGhT/FU5Jt/8cXGpF3CNvc2QSQdc2euskpo3kMwDd/HS6nR6tVA+iHDW0mjFsLUc08ECVd6J6y2T5JxFAgSQ/Lrc4Q9SyAuM0vT2AO4+6NHsDoVg1QiUcw77FrvOoYFA9of+AIT20Z5Lgqj8i8i2cs2WyFaEkxu+4PmE8Fei3UGSL2ThIytE2nblqQzxkpoJqthu7Rfx4zQu72KpO6bbFproZzFcpU4p3kZHjaA3jE0QevXlf24oYnXZVfOQH0558aZ2nMBrKaNb8wGRMe/k/G8Dp/HrheeU/aFGnLtLejnuHTDF/Oi0rtXHNiDHoSdxhbbPLfeZlLLJySagmAXrI8ZJsLQTl7f9lNokzh3d36UDNytwWM1rfQJsW9DsJ8lKwgYXAON6Y11gDw+sPU6YtuEglr08byDYy+xefbtyFfLK/NdNrFIg46puQejucUFflJrAyfDsIlpGKDH0GkxxNy3q+r/Egp2j+BoGz8mq58YmTOo1jN/u0q8GaZkZB1akRjSYsETTogEMgFcfKdzS9ppd7gCVDF38QcCXqvXA286QtnhiJoz4w2Zzg87YCF9IMYwLWJNCqlSzrXbiqjAEfiphnVqcCGOhdYOGYISxx3T84UZua51IGavzg74snwXTZGN3FMfkKkWSDk/gE1lGt24XmKdRPcnqzi4GDhWbwJfkiebwPnr4Ge6YJibyAMizoyZ9eJY4+FCDlzpcJOqEvBkhRJd9P1SmWe8yJ0S1SEXRaqd5Gw1NSJcB83wHcdPq7IjI6Lzz3k63Turziv/LrZ/u9jbonsslmYTq3wUNtrjWbql/0gTmwEOk/RLW7AzTcw20Bb0
        - #2:
          - type: tool-call
          - toolCallId: zfMM0WUWekeFOGfq
          - toolName: set-relationship
          - input:
            - TargetID: 7
            - Public: 30
            - Rationale: Seeking to improve our diplomatic stance with Morocco to facilitate a peace treaty, reduce our severe war weariness, and halt their destructive invasion of Vancouver.
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: LbUOgyYgtT5BxFxD
          - toolName: set-relationship
          - input:
            - Private: 30
            - TargetID: 3
            - Rationale: Improving our stance with The Shoshone to pave the way for peace, ending the border skirmishes around Utrecht and Rotterdam, and allowing our empire to stabilize.
            - Public: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: O6oSHjeykKE4peU5
          - toolName: set-relationship
          - input:
            - Private: 30
            - TargetID: 1
            - Public: 30
            - Rationale: Improving our stance with Polynesia to seek peace, ending their naval harassment and reducing war weariness.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 1CL1R7qqY7CHyEB0
          - toolName: set-relationship
          - input:
            - Public: 30
            - Rationale: Fostering peaceful relations with Venice to prevent them from declaring war on us once our current peace treaty expires in 9 turns.
            - TargetID: 6
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: BcsIeWC0zetA4H9f
          - toolName: set-flavors
          - input:
            - Rationale: Adjusting our strategic flavors to align with our peace-seeking pivot. We drastically reduce Antiair from 100 to 40 to stop AA gun spam, shifting production to defensive and mobile units (Tanks/Infantry) to protect our borders. We increase Gold to 80 to rebuild plundered trade routes and support our economy, and increase Diplomacy to 60 to secure City-State alliances to defend against India's diplomatic victory bid. We also lower UseNuke to 30 to act ethically and avoid catastrophic nuclear devastation while keeping a strong deterrent.
            - GrandStrategy: Spaceship
            - Flavors:
              - Mobile: 70
              - Diplomacy: 60
              - Offense: 30
              - Defense: 90
              - Gold: 80
              - Mobilization: 80
              - Antiair: 40
              - UseNuke: 30
              - Growth: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: cNc0fNEzFCXFdnhb
          - toolName: set-research
          - input:
            - Rationale: We are racing toward a Science Victory, and Satellites is the critical technology required to build the Apollo Program and start producing spaceship components.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: Z1Dd7sp7ARJRE743
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Enlightenment in the Rationalism branch provides 1 Free Technology and +1 Happiness from Universities, which will accelerate our scientific progress and help us catch up to India and other advanced civilizations.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 2vvLZ6ZNjlPNGirP
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
          - toolCallId: zfMM0WUWekeFOGfq
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: LbUOgyYgtT5BxFxD
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: O6oSHjeykKE4peU5
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 1CL1R7qqY7CHyEB0
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: BcsIeWC0zetA4H9f
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: cNc0fNEzFCXFdnhb
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: Z1Dd7sp7ARJRE743
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.