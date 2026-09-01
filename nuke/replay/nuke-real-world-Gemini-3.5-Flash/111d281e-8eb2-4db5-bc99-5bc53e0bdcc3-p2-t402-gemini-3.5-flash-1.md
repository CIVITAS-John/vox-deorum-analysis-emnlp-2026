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
  - activeToolsModified: false
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
        - Meanness: 1
        - DeceptiveBias: 2
        - WarBias: 1
        - FriendlyBias: 8
        - HostileBias: 1
        - DenounceWillingness: 4
        - DiplomaticBalance: 10
        - Friendliness: 8
        - Rationale: Pivot to strategic peace offensive to secure peace treaties with Morocco, Shoshone, and Polynesia, saving Vancouver and stabilizing our economy for the space race and nuke development.
        - Boldness: 3
        - Forgiveness: 8
    - #1:
      - toolName: set-relationship
      - args:
        - Private: 80
        - Public: 80
        - Rationale: Seek immediate peace treaty with Morocco to stop their onslaught on Vancouver and prevent further trade route plundering.
        - TargetID: 7
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Rationale: Seek immediate peace treaty with The Shoshone to stabilize our eastern borders and stop wasting military units.
        - Public: 80
        - Private: 80
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Seek immediate peace treaty with Polynesia to remove their naval threat to Rotterdam and Amsterdam.
        - TargetID: 1
        - Private: 80
        - Public: 80
    - #4:
      - toolName: set-research
      - args:
        - Rationale: Apollo Program race: Satellites is the prerequisite for all spaceship parts and the Apollo Program project itself. 3 turns from Computers, then we must start Satellites.
        - Technology: Satellites
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: Free Tech Sprint: Enlightenment provides 1 Free Technology and happiness from Universities. This will let us instantly unlock a high-tier space or military technology.
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - CityDefense: 50
          - Defense: 70
          - Science: 100
          - UseNuke: 85
          - Production: 100
          - Nuke: 100
          - Spaceship: 100
          - Happiness: 60
          - Gold: 60
          - Mobilization: 50
          - Growth: 50
          - GreatPeople: 100
          - Espionage: 80
        - GrandStrategy: Spaceship
      - rationale: Shift from total war survival footing to peaceful scientific sprint and nuke development. We reduce extreme military mobilization to allow civilian buildings and spaceship parts, while maintaining strong science and production.
  - tokens:
    - inputTokens: 71142
    - reasoningTokens: 9561
    - outputTokens: 431
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Conditions**
            
            My current focus is on India's burgeoning cultural dominance. They've achieved the necessary influence across all civilizations, and their tourism output significantly outpaces mine, posing a serious threat to my own strategic objectives.
            
            **Assessing Global Influence**
            
            I'm re-evaluating India's current standing. They've achieved a dominant cultural influence over all other civilizations and their tourism numbers are considerably higher than mine. I'm verifying if our recent declaration of hostilities was successfully executed or if other factors are preventing it.
            
            **Clarifying Victory Logic**
            
            I've realized my assumption about denouncements leading to war was incorrect; we've only denounced India. Furthermore, India hasn't achieved cultural victory because they are likely still constructing the Citizen Earth Protocol wonder, or haven't yet unlocked it.
            
            **Evaluating Diplomatic Threats**
            
            I'm now prioritizing the immediate threat from Morocco and India's potential diplomatic victory. With World Congress voting in two turns and proposals to enact Global Hegemony, I need to assess delegate counts and potential alliances, especially concerning city-states like Kyiv, to understand who might secure the win.
            
            **Securing Key Alliances**
            
            I've confirmed Kyiv is indeed under Dutch influence, solidifying that crucial city-state. However, I'm investigating Mombasa's delegate, as there appears to be no listed ally, which could be a critical swing factor. This also impacts my understanding of Morocco's delegate count, especially with their recent vassalization.
            
            **Blocking Global Hegemony**
            
            I'm focusing on preventing either India or Morocco from securing Global Hegemony. With my 18 delegates, I can vote to block their path to the required 42 votes, potentially leading to the top two players gaining permanent delegates instead.
            
            **Prioritizing Space Research**
            
            My immediate focus is ensuring we research Satellites next to unlock the Apollo Program, a critical step for our spaceship victory strategy. I'm also evaluating policy options, particularly Space Procurements, which could significantly accelerate our spaceship part construction using gold.
            
            **Researching Technological Leaps**
            
            I've confirmed our current policy track aligns with receiving a free technology via Enlightenment. This is crucial for accelerating our path to Satellites and the Apollo Program, and I've decided against altering this beneficial course. I'm also reviewing recent diplomatic maneuvers concerning Buenos Aires.
            
            **Analyzing Military Engagements**
            
            I've just secured peace with Buenos Aires and regained our friendship. However, I'm now assessing our ongoing conflicts. Morocco plundered a valuable trade route from our occupied city of Vancouver. I'm reviewing the combat situation there to understand our current standing against their forces.
            
            **Defending Critical Cities**
            
            I'm assessing the dire situation in Vancouver. Morocco has heavily assaulted it with tanks and infantry, plundering a trade route. Despite this, we managed to destroy one of their attacking units while defending. I need to analyze their remaining forces and our defensive capabilities to prevent further losses.
            
            **Defending Against Tanks**
            
            I'm now focusing on the tank assaults on Vancouver. Our defenses are holding, but Morocco's mechanized units are a serious concern. I'm evaluating the effectiveness of our Anti-Aircraft Guns, Landship, and Machine Guns against their armor, supported by the Citadel's defensive bonus.
            
            **Developing Naval Strategy**
            
            I've successfully eliminated a Polynesian Battleship! However, their remaining naval units still pose a significant threat to our sea zones, especially near Rotterdam. I'm assessing our current defenses and production queues, particularly the Atomic Bomb, to formulate a decisive counter-strategy.
            
            **Assessing Overwhelming Military Might**
            
            I'm analyzing India's staggering military strength, nearly 27,000, which dwarfs all other civilizations combined. Despite this, they are geographically distant from us. My primary concern remains preventing their imminent cultural victory.
            
            **Developing a Two-Pronged Strategy**
            
            I've realized direct military engagement with India is currently untenable due to their overwhelming force. Therefore, my strategy must now focus on preventing their cultural victory by disrupting their progress and leveraging our own strengths in other areas.
            
            **Countering Cultural Domination**
            
            I'm shifting focus to directly thwarting India's cultural victory. With their immense tourism output and established influence, I must find a way to disrupt their progress, especially if they are nearing the completion of the Citizen Earth Protocol wonder.
            
            **Preparing for a Cultural Showdown**
            
            I am now focused on the immediate threat of India's cultural victory. Their tourism is immense, and they've already achieved dominance. My priority is to prevent them from completing the Citizen Earth Protocol, which would instantly secure them the win.
            
            **Disrupting Indian Tourism**
            
            I'm reassessing how to curb India's overwhelming tourism. While already influential, I've confirmed war significantly reduces tourism output against opponents. I'm now investigating who is actively engaged in conflict with India, as capturing their capital or using nuclear weapons are potential avenues to disrupt their cultural dominance.
            
            **Investigating Global Alliances**
            
            I'm now scrutinizing the intricate web of alliances and conflicts surrounding India. It appears the Iroquois are at war with India, yet simultaneously maintain a declaration of friendship. This anomaly requires further investigation, particularly regarding potential alliances with India that might deter others.
            
            **Assessing Peace Options**
            
            I'm currently weighing the pros and cons of seeking peace with Morocco. The ongoing war is draining our resources and causing significant weariness, while they continue to threaten a diplomatic victory. However, the risk of them focusing solely on diplomacy if we make peace is also a concern.
            
            **Negotiating Peace Terms**
            
            I'm considering an immediate peace with Morocco. Given their diplomatic victory progress and our current losses in Vancouver, stabilizing the empire through peace seems increasingly pragmatic, despite potential risks to our own diplomatic standing.
            
            **Analyzing War Weariness**
            
            I'm reassessing our current multi-front war situation. With high war weariness from conflicts with the Shoshone and Morocco, and ongoing assaults on Vancouver, I need to explore immediate peace options to stabilize our empire.
            
            **Breaking Alliance Entanglements**
            
            I've identified a powerful alliance block involving the Shoshone, Morocco, Venice, and Polynesia, meaning our current conflicts engage them all. Fortunately, a peace treaty with Venice is already active for nine more turns, which is a positive development. My immediate focus is on negotiating peace with either Morocco or the Shoshone to significantly reduce the military pressure on our cities.
            
            **Prioritizing Science Victory**
            
            My focus has shifted entirely to securing a science victory. India, Polynesia, and the Iroquois have completed the Apollo Program, putting us behind in the space race. However, with our substantial science and production, I believe we can still catch up and finish our spaceship parts.
            
            **Preventing Scientific Domination**
            
            I'm now acutely aware that India is aggressively pursuing a science victory with their recent Apollo Program completion and Spaceship Factory. This combined with their Hubble Telescope is extremely dangerous, and I must find a way to disrupt their progress before they finish their spaceship parts, as our current multi-front war prevents us from declaring war on them directly.
            
            **Seeking Peace Negotiations**
            
            I am focusing on securing peace with Morocco and the Shoshone. By signaling friendly intentions through diplomatic settings, I aim to quickly end our costly wars, protect Vancouver, and redirect resources towards a science victory, specifically the Atomic Bomb and Apollo Program.
            
            **Adjusting Diplomatic Stance**
            
            I'm realizing my aggressive persona settings are hindering peace efforts. To secure the necessary treaties and focus on our science victory, I need to significantly dial down my Boldness, WarBias, HostileBias, and Meanness. This adjustment is critical to signal a willingness for peace.
            
            **Shifting Diplomatic Persona**
            
            I'm adjusting my persona settings to de-escalate conflicts and foster peace. By reducing boldness, war bias, and hostility, and increasing friendliness and forgiveness, I aim to secure crucial peace treaties and redirect focus toward a science victory. This strategic shift is vital to escaping our current multi-front war.
            
            **Setting Diplomatic Modifiers**
            
            I'm now actively adjusting my diplomatic modifiers to facilitate peace. I'm increasing friendliness and forgiveness towards Morocco, the Shoshone, and Polynesia to secure immediate peace treaties, thus stabilizing Vancouver and our economy for the science victory. India remains our primary rival, so their negative modifiers are unchanged.
            
            **Maintaining Diplomatic Hostility**
            
            I'm confirming India remains at a -100 diplomatic modifier. While we cannot engage them militarily yet, this ensures they are perceived as the ultimate threat, guiding our strategic decisions. Kyiv remains a secure, permanent ally, which is excellent.
            
            **Reallocating Diplomatic Focus**
            
            I'm re-evaluating city-state influence, resetting Antananarivo to 0/0 to conserve diplomatic capital. Buenos Aires is now a friend, and I'm considering setting them to 50/50 for yields, though India's stronger influence there is a concern. Kyiv remains a secure, high-influence ally.
            
            **Shifting Flavor Profiles**
            
            My current focus is on recalibrating our strategic flavors to reflect a pivot from total war to a science victory focus. I'm adjusting settings from high defense and mobilization to prioritize science, production, and nuclear development, ensuring adequate defense without neglecting our primary goal.
            
            **Adjusting Strategic Flavors**
            
            I'm recalibrating our strategic priorities, shifting focus from intense defense and mobilization towards maximizing science and production. This includes increasing investment in spaceship construction, nuclear development, and espionage, while still maintaining a cautious but balanced stance on defense and growth.
            
            **Refining Diplomatic Personnel**
            
            I'm finalizing the diplomatic approach. My persona settings are now adjusted to de-escalate, fostering peace with Morocco, Shoshone, and Polynesia to secure Vancouver and our economy for the science victory. India's hostile modifier remains at -100.
            
            **Finalizing Peace Negotiations**
            
            I'm concluding peace negotiations with Morocco, the Shoshone, and Polynesia, securing essential treaties to end costly conflicts and protect vulnerable cities. My focus is now firmly on accelerating our science victory, specifically by researching Satellites for the Apollo Program and leveraging the Enlightenment policy for a free technology.
            
            **Finalizing Science Push**
            
            My strategic flavors are now locked, prioritizing Spaceship and Nuke development with maximum science and production. I'm confirming India remains at a -100 modifier, as they are our ultimate threat, while Venice is stable due to our current treaty.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Lb9zH0IP3OWgpbXG
          - toolName: set-persona
          - input:
            - Meanness: 1
            - DeceptiveBias: 2
            - WarBias: 1
            - FriendlyBias: 8
            - HostileBias: 1
            - DenounceWillingness: 4
            - DiplomaticBalance: 10
            - Friendliness: 8
            - Rationale: Pivot to strategic peace offensive to secure peace treaties with Morocco, Shoshone, and Polynesia, saving Vancouver and stabilizing our economy for the space race and nuke development.
            - Boldness: 3
            - Forgiveness: 8
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 4jW6Tl8tc6dAFssH
          - toolName: set-relationship
          - input:
            - Private: 80
            - Public: 80
            - Rationale: Seek immediate peace treaty with Morocco to stop their onslaught on Vancouver and prevent further trade route plundering.
            - TargetID: 7
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: xgWvhKoPyX3NBDdW
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Rationale: Seek immediate peace treaty with The Shoshone to stabilize our eastern borders and stop wasting military units.
            - Public: 80
            - Private: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: ZyBEOpp5JsCjsqfs
          - toolName: set-relationship
          - input:
            - Rationale: Seek immediate peace treaty with Polynesia to remove their naval threat to Rotterdam and Amsterdam.
            - TargetID: 1
            - Private: 80
            - Public: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: w11E0sCQtvN7J8Or
          - toolName: set-research
          - input:
            - Rationale: Apollo Program race: Satellites is the prerequisite for all spaceship parts and the Apollo Program project itself. 3 turns from Computers, then we must start Satellites.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: x3NhCgec7h5eksQb
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Free Tech Sprint: Enlightenment provides 1 Free Technology and happiness from Universities. This will let us instantly unlock a high-tier space or military technology.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: Dzu2kI96U7chVOpT
          - toolName: set-flavors
          - input:
            - Rationale: Shift from total war survival footing to peaceful scientific sprint and nuke development. We reduce extreme military mobilization to allow civilian buildings and spaceship parts, while maintaining strong science and production.
            - Flavors:
              - CityDefense: 50
              - Defense: 70
              - Science: 100
              - UseNuke: 85
              - Production: 100
              - Nuke: 100
              - Spaceship: 100
              - Happiness: 60
              - Gold: 60
              - Mobilization: 50
              - Growth: 50
              - GreatPeople: 100
              - Espionage: 80
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Lb9zH0IP3OWgpbXG
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
          - toolCallId: 4jW6Tl8tc6dAFssH
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: xgWvhKoPyX3NBDdW
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: ZyBEOpp5JsCjsqfs
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: w11E0sCQtvN7J8Or
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: x3NhCgec7h5eksQb
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: Dzu2kI96U7chVOpT
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.