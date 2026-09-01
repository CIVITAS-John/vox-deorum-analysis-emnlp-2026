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
        - Meanness: 2
        - Boldness: 4
        - VictoryCompetitiveness: 10
        - WorkWithWillingness: 8
        - Rationale: DIPLOMATIC SURVIVAL PIVOT: Morocco is 2 turns away from a Diplomatic Victory with 26 votes, supported by their vassal the Huns (13) and their close allies. We are in a four-front war, which prevents us from negotiating or bribing Morocco's allies (Shoshone, Polynesia). We must dramatically lower our aggression (Boldness 4, WarBias 2, HostileBias 3, Meanness 2) and maximize peace-seeking behaviors (FriendlyBias 8, Friendliness 8, Forgiveness 8, WorkWithWillingness 8) so our staff can immediately secure peace treaties and negotiate vote-buying or abstention deals to block Morocco's 42-vote threshold.
        - HostileBias: 3
        - Forgiveness: 8
        - WarBias: 2
        - Friendliness: 8
        - FriendlyBias: 8
        - DenounceWillingness: 10
        - DiplomaticBalance: 10
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: VOTE BUYING EMERGENCY: Morocco is 3 votes away from winning a Diplomatic Victory in 2 turns. Venice has 14 votes and is a close ally of Morocco. We must set our relationship to friendly to allow our staff to negotiate peace/agreements and bribe Venice to abstain or vote for India, preventing Morocco from reaching the 42 votes threshold.
        - Public: 50
        - Private: 50
        - TargetID: 6
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 50
        - Public: 50
        - Rationale: VOTE BUYING EMERGENCY: The Iroquois have 12 votes and are allied with Morocco. We must shift our relationship to friendly to enable our staff to bribe them to abstain or vote for India, blocking Morocco's imminent Diplomatic Victory.
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: PEACE OVERTURE FOR DELEGATES: Shoshone has 15 votes and is allied with Morocco. If we can make peace, we can stop them from voting blindly for Morocco or even buy their abstention. Setting relationship to friendly to prioritize peace negotiations.
        - Public: 40
        - TargetID: 3
        - Private: 40
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: PEACE AND VOTE NEGOTIATION: Polynesia has 15 votes and is at war with us. Shifting to friendly to encourage our staff to make peace and attempt to secure their votes or abstention in the World Congress.
        - Public: 30
        - TargetID: 1
        - Private: 30
    - #5:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: APOLLO PROGRAM RACE: Computers will finish in 3 turns. Satellites is the next critical tech to unlock the Apollo Program and start building spaceship parts. We must maintain our sprint toward a Science Victory as our long-term win condition.
    - #6:
      - toolName: set-policy
      - args:
        - Rationale: FREE TECH EMERGENCY: Enlightenment is 14 turns away and provides a free technology, which will be vital to skip a late-game science tech and accelerate our spaceship production.
        - Policy: Enlightenment
    - #7:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Mobilization: 100
          - Science: 100
          - Defense: 100
          - Production: 100
          - Offense: 0
          - Spaceship: 100
          - Diplomacy: 80
          - Wonder: 0
          - Espionage: 100
          - Nuke: 100
          - CityDefense: 100
          - UseNuke: 85
          - Expansion: 0
        - GrandStrategy: Spaceship
      - rationale: SURVIVAL AND POST-ELECTION PREPARATION: Keeping maximum focus on Science (100), Production (100), and Defense (100) to survive the four-front war and advance to Satellites. Increasing Diplomacy to 80 to prepare for the long-term struggle over city-states if we successfully block Morocco's Diplomatic Victory this turn. Maintaining high Espionage (100) for tech theft and security.
  - tokens:
    - inputTokens: 71142
    - reasoningTokens: 12023
    - outputTokens: 826
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Cultural Threats**
            
            My focus is on the alarming cultural pressure from India, which has reached dominance and maintains a concerning 165% influence ratio. This demands immediate strategic re-evaluation.
            
            **Clarifying Wartime Status**
            
            It seems I was mistaken about our current war status with India; we've only denounced them, not declared war. Despite their high influence, they haven't won. This requires adjusting our tactical approach.
            
            **Analyzing Victory Conditions**
            
            My attention is now drawn to the immediate threats and opportunities presented by the current game state. I'm dissecting the specific victory conditions, particularly the Cultural and Diplomatic paths, to understand India's precise standing and how close the World Congress vote is to triggering a potential win.
            
            **Defending Critical Cities**
            
            I'm now grappling with immediate military concerns. Vancouver is under intense siege by Morocco and Polynesia, despite its occupied status under the Netherlands. Trade routes are being plundered, and our units are engaged in fierce combat. I need to assess our defensive capabilities and the impact of these attacks on our overall situation.
            
            **Evaluating Research Progress**
            
            I'm re-evaluating our current research trajectory. Given India's technological lead and our ongoing race for a Spaceship victory, I'm analyzing the immediate technological choices available after completing 'Computers' to best support our win condition and counter their influence.
            
            **Prioritizing Research Path**
            
            I'm focusing on ensuring our research aligns perfectly with our win condition. I've decided to explicitly set "Satellites" as the next research, confirming our ongoing strategy. Now, I'm delving into policy choices to further bolster our progress.
            
            **Revising Policy Options**
            
            I'm examining the available policy options to best complement our current research and ideological stance. My current focus is on potentially selecting "Space Procurements" or "Media Culture" from the Freedom ideology to accelerate our path to victory.
            
            **Refining Ideological Stance**
            
            I'm re-evaluating my ideological choices. Considering our technological advancements and the need to secure a Spaceship victory, I'm analyzing how policies like "Space Procurements" and "Media Culture" within the Freedom ideology might best serve our objectives.
            
            **Considering Policy Synergies**
            
            I'm now exploring the synergies between different policy branches. Specifically, I'm weighing the benefits of continuing with existing branches like Rationalism or Progress against exploring new ones like Artistry, all while keeping our primary win condition in mind.
            
            **Adopting Free Technology**
            
            I've identified "Enlightenment" as the optimal policy choice. The immediate free technology it grants will significantly accelerate my Spaceship victory progress, especially given the ongoing research path. I am now proceeding to implement this policy.
            
            **Assessing Diplomatic State**
            
            I'm reassessing our diplomatic and military situation. It appears my previous assumption about being at war with India was incorrect. Instead, I've discovered we are already engaged in a substantial four-front war with the Shoshone, Morocco, Polynesia, and the Huns. Declaring war on India, given their immense military strength, would be catastrophic.
            
            **Confirming Cultural Win**
            
            I've confirmed India's cultural dominance. They are influential with all other 7 major civilizations. The delay in their win is likely due to not yet completing the Citizen Earth Protocol wonder.
            
            **Analyzing Diplomatic Threats**
            
            I'm now analyzing India's path to victory, noting they have sufficient tenets for Tier 3 policy benefits, suggesting they are building the Citizen Earth Protocol. While I cannot reach them militarily, I'm exploring the impact of war on tourism modifiers and considering the near-victory status of Morocco in the Diplomatic arena.
            
            **Calculating Diplomatic Support**
            
            I'm recalculating diplomatic support for the upcoming World Congress vote. Morocco, with its own 26 delegates, will secure the Huns' 13 votes, totaling 39, putting them very close to the 42 needed for a diplomatic win. This requires immediate attention.
            
            **Preventing Diplomatic Victory**
            
            Morocco is alarmingly close to a Diplomatic Victory, securing a critical 39 votes with only 3 more needed. Their defensive pacts with Polynesia, Shoshone, and Venice mean any of their votes would seal their win in two turns. I'm exploring how to use my 18 votes and potentially sway city-states like Kyiv to prevent this immediate, catastrophic threat.
            
            **Securing Critical Alliances**
            
            I'm now focusing on securing alliances with key city-states. My analysis shows Mombasa is not allied with any major civilization, presenting a crucial opportunity. I need to assess if I have enough gold to forge an alliance there to gain valuable votes.
            
            **Counting Active City-States**
            
            I'm now reassessing the global landscape following numerous city-state annexations. It appears only nine remain active, with India dominating their allegiances. This significantly impacts my diplomatic strategy, particularly concerning securing crucial votes for the World Congress.
            
            **Confirming Voting Mechanics**
            
            I'm verifying how vassals vote in Civ V Vox Populi, confirming they must support their master for Global Hegemony. This means Morocco's 39 delegates plus potential support from Polynesia, Shoshone, or Venice needs careful consideration for their diplomatic win condition.
            
            **Analyzing Delegate Distribution**
            
            I am analyzing the delegate distribution for the World Congress. India and Morocco, holding the most delegates, are confirmed candidates. My own delegation, along with potential strategic alliances and city-state support, must be carefully considered to counter their influence and prevent their respective victory conditions.
            
            **Recalculating Diplomatic Threats**
            
            I've made a critical miscalculation regarding delegate votes. Polynesia, Shoshone, Venice, and the Iroquois, all allied with Morocco or at war with India, will vote for Morocco, granting them a near-certain diplomatic victory. I must find a way to disrupt this impending win.
            
            **Disrupting Morocco's Win**
            
            I've realized the gravity of the situation: Morocco is poised for a diplomatic victory with overwhelming support, thanks to their alliances and vassal states. The critical factor is that if no one wins, the top two gain delegates, but Morocco *will* win. I'm now frantically searching for any means to break their alliances or disrupt their delegates within these final two turns.
            
            **Disrupting Diplomatic Victory**
            
            I'm frantically evaluating options to prevent Morocco's impending diplomatic victory. Voting for India won't work. I'm now investigating if I can disrupt city-state alliances to reduce Morocco's delegate count.
            
            **Analyzing Diplomatic Strategy**
            
            I'm now dissecting the World Congress proposal, specifically "Global Hegemony." My immediate thought is to vote against it, as Morocco is poised to win with it. I'm analyzing if defeating this proposal, even with my limited votes and city-state influence, could disrupt their victory and offer a path to survival.
            
            **Voting Against Hegemony**
            
            I'm now analyzing the "Global Hegemony" proposal itself, recognizing it as the World Leader election. My current assessment is to vote against it, hoping to disrupt Morocco's imminent diplomatic victory, though I'm uncertain if my limited delegates and city-state influence can achieve this.
            
            **Securing Key Alliances**
            
            I'm now reassessing my diplomatic maneuvers. I've secured peace with Buenos Aires and am focusing on allying them, although India currently holds significant sway. My defense of Kyiv seems secure, but I need to evaluate my own city production capabilities next.
            
            **Accelerating Atomic Bomb Production**
            
            I'm frantically re-evaluating ways to accelerate the Atomic Bomb construction. With only two turns until the election and four until completion, I'm exploring investments and spy capabilities to expedite this critical weapon, hoping it might offer a last-ditch disruption to Morocco's impending diplomatic win.
            
            **Leveraging Spies Diplomaticaly**
            
            My spies have immense network capabilities. While typically focused on intelligence and tech theft, I'm now questioning if they can directly influence the upcoming World Congress vote. I need to investigate if a spy in Marrakech can sabotage Morocco's diplomatic win.
            
            **Trading for Votes**
            
            I've identified Venice as a potential ally due to our peace treaty. I'm now investigating if I can leverage our gold reserves and diplomatic efforts to secure their votes against Morocco's impending "Global Hegemony" win, despite their current denouncement of us.
            
            **Leveraging Geopolitical Alignments**
            
            I'm now focusing on India and the Iroquois. Since the Iroquois are at war with India and I'm not at war with either, I'm exploring if I can leverage their conflict to secure India's votes in the World Congress against Morocco's imminent victory.
            
            **Securing Iroquois and Venice**
            
            I'm now focused on securing the Iroquois and Venice's votes. Despite their current stance, I believe friendly relations and potential resource trades might sway them to vote against Morocco. Their combined delegates are crucial to blocking an imminent diplomatic victory.
            
            **Preventing Delegate Acquisition**
            
            I'm analyzing the World Congress rules regarding delegate acquisition. It seems if no one wins, the top two candidates gain delegates and the vote is postponed. This means preventing Morocco from winning is paramount, as it would grant them an advantage and buy us crucial time to complete our victory conditions.
            
            **Analyzing Ally Motivations**
            
            I'm trying to understand how Venice and the Iroquois will vote. Given their animosity towards India and alliances with Morocco, they will likely support Morocco. My focus is now on finding any leverage to sway them to abstain or, ideally, vote for India instead, which would disrupt Morocco's win.
            
            **Securing Venice and Iroquois Votes**
            
            I'm now focusing on securing the Iroquois and Venice's votes. Despite their current stance, I believe friendly relations and potential resource trades might sway them to vote against Morocco. Their combined delegates are crucial to blocking an imminent diplomatic victory.
            
            **Prioritizing Shoshone Peace**
            
            I'm now focusing on the Shoshone, who are allied with Morocco and hold 15 crucial delegates. Given our current war weariness and their superior military, I'm prioritizing a peace overture to potentially halt their votes for Morocco or even secure their abstention.
            
            **Securing Critical Allies**
            
            I am now reassessing my diplomatic maneuvers with Venice and the Iroquois. While they currently appear to favor Morocco, I'm exploring if resource trades or friendly relations might sway their delegates to abstain or vote against Morocco's "Global Hegemony" proposal.
            
            **Adjusting Diplomatic Focus**
            
            I'm recalibrating our approach, recognizing that my previous focus on specific city-state alliances wasn't yielding enough for the World Congress. I now understand that increasing our overall Diplomacy flavor to 100 is key to prioritizing diplomatic units and city-state engagement, which directly influences our ability to counter Morocco's imminent victory.
            
            **Adjusting Diplomatic Focus**
            
            I'm recalibrating our approach, recognizing that my previous focus on specific city-state alliances wasn't yielding enough for the World Congress. I now understand that increasing our overall Diplomacy flavor to 100 is key to prioritizing diplomatic units and city-state engagement, which directly influences our ability to counter Morocco's imminent victory. I've decided to increase Diplomacy flavor to 80 and keep Gold at 50.
            
            **Revising Persona Values**
            
            I'm realizing my current persona settings are a major roadblock. My high HostileBias and low Forgiveness make peace overtures extremely difficult, directly hindering my efforts to secure crucial votes and prevent Morocco's imminent diplomatic victory. I must adjust these values immediately.
            
            **Revising Persona Values**
            
            I'm realizing my current persona settings are a major roadblock. My high HostileBias and low Forgiveness make peace overtures extremely difficult, directly hindering my efforts to secure crucial votes and prevent Morocco's imminent diplomatic victory. I must adjust these values immediately.
            
            **Adjusting Persona Values**
            
            I'm realizing my current persona settings are a major roadblock. My high HostileBias and low Forgiveness make peace overtures extremely difficult, directly hindering my efforts to secure crucial votes and prevent Morocco's imminent diplomatic victory. I must adjust these values immediately to prioritize peace and collaboration.
            
            **Pivoting Diplomatic Approach**
            
            I'm implementing a significant shift in my persona and diplomatic strategy. Adjusting my high HostileBias and low Forgiveness is crucial to enable peace overtures and secure necessary votes to prevent Morocco's imminent diplomatic victory. I will also be targeting specific civs for relationship adjustments.
            
            **Shifting Diplomatic Leverage**
            
            I'm enacting a critical shift in my persona, lowering my biases toward hostility and increasing my willingness to work with others. This is crucial for peace negotiations with Polynesia and the Shoshone, aiming to secure their votes against Morocco's imminent diplomatic victory. I'm also focusing on Venice and the Iroquois.
            
            **Adjusting Diplomatic Strategy**
            
            I'm recalibrating my entire approach, recognizing that my aggressive persona is preventing vital peace negotiations. Lowering hostility and increasing friendliness is now paramount to securing votes from Venice and the Shoshone, aiming to block Morocco's imminent diplomatic victory.
            
            **Shifting Diplomatic Focus**
            
            I'm recalibrating my entire approach, recognizing that my aggressive persona is preventing vital peace negotiations. Lowering hostility and increasing friendliness is now paramount to securing votes from Venice and the Shoshone, aiming to block Morocco's imminent diplomatic victory.
            
            I'm adjusting my relationship with the Iroquois to friendly (Public: 50, Private: 50) to bribe them for votes against Morocco. I'm also pursuing peace with the Shoshone (Public: 40, Private: 40) and Polynesia (Public: 30, Private: 30) to secure their delegates. My next research target is "Satellites."
            
            **Securing Critical Delegates**
            
            I'm adjusting my relationship with the Iroquois to friendly to bribe them for votes against Morocco. I'm also pursuing peace with the Shoshone and Polynesia to secure their delegates. My next research target is "Satellites" to continue our space race.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: nqezGz9SIVpSBIKm
          - toolName: set-persona
          - input:
            - Meanness: 2
            - Boldness: 4
            - VictoryCompetitiveness: 10
            - WorkWithWillingness: 8
            - Rationale: DIPLOMATIC SURVIVAL PIVOT: Morocco is 2 turns away from a Diplomatic Victory with 26 votes, supported by their vassal the Huns (13) and their close allies. We are in a four-front war, which prevents us from negotiating or bribing Morocco's allies (Shoshone, Polynesia). We must dramatically lower our aggression (Boldness 4, WarBias 2, HostileBias 3, Meanness 2) and maximize peace-seeking behaviors (FriendlyBias 8, Friendliness 8, Forgiveness 8, WorkWithWillingness 8) so our staff can immediately secure peace treaties and negotiate vote-buying or abstention deals to block Morocco's 42-vote threshold.
            - HostileBias: 3
            - Forgiveness: 8
            - WarBias: 2
            - Friendliness: 8
            - FriendlyBias: 8
            - DenounceWillingness: 10
            - DiplomaticBalance: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: lTVdkNjvVWnPn4Pw
          - toolName: set-relationship
          - input:
            - Rationale: VOTE BUYING EMERGENCY: Morocco is 3 votes away from winning a Diplomatic Victory in 2 turns. Venice has 14 votes and is a close ally of Morocco. We must set our relationship to friendly to allow our staff to negotiate peace/agreements and bribe Venice to abstain or vote for India, preventing Morocco from reaching the 42 votes threshold.
            - Public: 50
            - Private: 50
            - TargetID: 6
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: AP1dCkil2v4h14V6
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 50
            - Public: 50
            - Rationale: VOTE BUYING EMERGENCY: The Iroquois have 12 votes and are allied with Morocco. We must shift our relationship to friendly to enable our staff to bribe them to abstain or vote for India, blocking Morocco's imminent Diplomatic Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: rHQmIgw9AHbPtX4q
          - toolName: set-relationship
          - input:
            - Rationale: PEACE OVERTURE FOR DELEGATES: Shoshone has 15 votes and is allied with Morocco. If we can make peace, we can stop them from voting blindly for Morocco or even buy their abstention. Setting relationship to friendly to prioritize peace negotiations.
            - Public: 40
            - TargetID: 3
            - Private: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: N5A82C2wexZ5ub9J
          - toolName: set-relationship
          - input:
            - Rationale: PEACE AND VOTE NEGOTIATION: Polynesia has 15 votes and is at war with us. Shifting to friendly to encourage our staff to make peace and attempt to secure their votes or abstention in the World Congress.
            - Public: 30
            - TargetID: 1
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 0AGsd5p71gprWvEP
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: APOLLO PROGRAM RACE: Computers will finish in 3 turns. Satellites is the next critical tech to unlock the Apollo Program and start building spaceship parts. We must maintain our sprint toward a Science Victory as our long-term win condition.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: wnkZ8Onb5AE8VUiF
          - toolName: set-policy
          - input:
            - Rationale: FREE TECH EMERGENCY: Enlightenment is 14 turns away and provides a free technology, which will be vital to skip a late-game science tech and accelerate our spaceship production.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: qS7sjd40HyV6SL4d
          - toolName: set-flavors
          - input:
            - Rationale: SURVIVAL AND POST-ELECTION PREPARATION: Keeping maximum focus on Science (100), Production (100), and Defense (100) to survive the four-front war and advance to Satellites. Increasing Diplomacy to 80 to prepare for the long-term struggle over city-states if we successfully block Morocco's Diplomatic Victory this turn. Maintaining high Espionage (100) for tech theft and security.
            - Flavors:
              - Mobilization: 100
              - Science: 100
              - Defense: 100
              - Production: 100
              - Offense: 0
              - Spaceship: 100
              - Diplomacy: 80
              - Wonder: 0
              - Espionage: 100
              - Nuke: 100
              - CityDefense: 100
              - UseNuke: 85
              - Expansion: 0
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: nqezGz9SIVpSBIKm
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
          - toolCallId: lTVdkNjvVWnPn4Pw
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: AP1dCkil2v4h14V6
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: rHQmIgw9AHbPtX4q
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: N5A82C2wexZ5ub9J
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 0AGsd5p71gprWvEP
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: wnkZ8Onb5AE8VUiF
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: qS7sjd40HyV6SL4d
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.