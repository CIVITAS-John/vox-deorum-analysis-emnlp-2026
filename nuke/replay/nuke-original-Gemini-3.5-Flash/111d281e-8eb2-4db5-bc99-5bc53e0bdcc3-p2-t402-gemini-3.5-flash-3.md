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
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
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
  - decisions:
    - #0:
      - toolName: set-research
      - args:
        - Rationale: APOLLO PROGRAM RACE: Satellites unlocks the Apollo Program, which is required for all spaceship parts. This is our only viable path to victory before India finishes the Citizen Earth Protocol.
        - Technology: Satellites
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: FREE TECH EMERGENCY: Secure Enlightenment to receive a free technology, which we can use to instantly unlock a critical late-game science or military tech, speeding up our spaceship victory path.
        - Policy: Enlightenment
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: BUENOS AIRES ALLY PUSH: We recently made peace with Buenos Aires and are now Friends. Elevating priority to 50/50 to encourage our AI to invest in becoming their Ally, securing more delegates for the upcoming World Congress votes.
        - Private: 50
        - Public: 50
        - TargetID: 36
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 0
        - Public: 0
        - TargetID: 5
        - Rationale: IROQUOIS REALIGNMENT: The Iroquois are now at war with India, our main competitor. Resetting our relationship to 0/0 to remove hostile modifiers, allowing for potential cooperation or joint efforts against India.
    - #4:
      - toolName: keep-status-quo
      - rationale: EMERGENCY WAR AND SCIENCE POSTURE: Maintaining our extreme defense (100), science (100), production (95), and nuclear deterrence (100) focus. Our cities are successfully holding the line at Utrecht, Rotterdam, and Vancouver, and we are currently building an Atomic Bomb in Groningen. This strategy remains perfectly aligned with our dual goals of survival and a rapid spaceship victory.
  - tokens:
    - inputTokens: 70870
    - reasoningTokens: 7406
    - outputTokens: 335
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Progress**
            
            My focus is on assessing our current standing and strategic objectives. I'm evaluating our progress towards various victory conditions and identifying potential threats or opportunities that have emerged recently in Turn 402.
            
            **Assessing India's Threat**
            
            My current thoughts are centered on India's escalating cultural dominance. They've achieved influence over all other civilizations and appear poised for a cultural victory. Given our recent declaration of war against them, I'm analyzing the implications of this strategic move for our own survival.
            
            **Revising India Strategy**
            
            I'm re-evaluating our engagement with India. It appears my previous assessment of being at war was inaccurate; we only denounced them. I'm now confirming India's cultural victory status and determining if a declaration of war is still viable and strategically sound.
            
            **Identifying Victory Roadblocks**
            
            I've identified that India's cultural victory hinges on completing the Citizen Earth Protocol wonder, giving us a crucial window. Meanwhile, our science victory path is advancing; Computers is nearly researched, paving the way for Satellites and then the Apollo Program.
            
            **Accelerating Space Race**
            
            I've discovered that India, Polynesia, and the Iroquois have already completed the Apollo Program and are building spaceship parts. I need to rush Satellites after finishing Computers, then build Apollo myself. I also need to confirm the status of the World Congress and its active resolutions.
            
            **Confirming Diplomatic Standing**
            
            I'm actively verifying our diplomatic relations, confirming our permanent alliance with Kyiv and our renewed friendship with Buenos Aires after a recent peace treaty. I'm also checking Mombasa's status and quests, noting its current influence and pending espionage mission for a significant reward.
            
            **Analyzing Combat Scenarios**
            
            I'm currently assessing our defensive positions across multiple active combat zones. Vancouver is under heavy tank and infantry assault from Morocco, with Polynesian support, but our defenses are holding. Utrecht is also facing Shoshone infantry attacks. Our tactical AI is managing these engagements effectively despite the multi-front war.
            
            **Assessing Defensive Strengths**
            
            My current focus is on bolstering our defenses in Rotterdam, where our strength significantly outweighs the Shoshone's, and in the surrounding sea zones against Polynesian naval forces. I've confirmed the safety of Amsterdam and Groningen, the latter of which is nearing completion of an Atomic Bomb, a valuable asset for deterrence or offense.
            
            **Setting Research Priority**
            
            I am confirming `Satellites` as our next research priority to unlock the Apollo Program and begin spaceship construction, reinforcing this decision with a `set-research` command. I'm also evaluating our policy options within the Freedom Ideology, noting our progress in unlocking various tenets.
            
            **Optimizing Policy Choice**
            
            I'm prioritizing selecting the `Space Procurements` tenet under the Freedom Ideology. This will significantly accelerate our spaceship construction by allowing gold investment and halving factory build times, a critical advantage for our science victory path.
            
            **Choosing Next Tenet**
            
            I'm weighing the immediate benefits of `Space Procurements` against the long-term advantage of `Enlightenment` for our science victory. `Enlightenment` offers a free technology, potentially accelerating our research considerably, while `Space Procurements` directly aids spaceship construction. I'm verifying our current tenet adoption to determine which is the more strategically sound choice.
            
            **Researching Next Tenet**
            
            I'm deciding between the `Enlightenment` tenet for a free technology boost and `Space Procurements` to directly accelerate spaceship construction. Given my high science flavor, securing a free tech seems the most advantageous for our science victory sprint.
            
            **Confirming Defensive Builds**
            
            My thoughts are centered on ensuring our critical defensive structures, like the Strategic Defense System, Airport, and Atomic Bomb, are progressing as intended. I'm maintaining the current flavor settings as they seem optimal for our situation.
            
            **Analyzing Moroccan Threat**
            
            I am closely monitoring Morocco's diplomatic maneuvers, specifically their pursuit of a Diplomatic Victory and the upcoming Global Hegemony vote in two turns. I'm also confirming our strong alliance with Kyiv and ensuring our influence there remains robust to secure their support.
            
            **Prioritizing City-State Alliances**
            
            I'm now evaluating our relationships with Buenos Aires, noting our recent peace and strong friendship. My focus is on how to leverage this to secure their alliance and gain crucial delegates for the World Congress, considering our limited gold for direct influence. I'm also assessing Mombasa's current standing and its active spy mission for a potentially significant reward.
            
            **Securing Strategic City-States**
            
            I'm prioritizing securing alliances with key city-states. I've confirmed a trade route to Antananarivo is feasible for influence and oil, and I'm monitoring the progress of a spy mission for a significant reward from Mombasa. Seoul remains at war, limiting interaction.
            
            **Leveraging Diplomatic Leverage**
            
            I'm focusing on securing Ragusa's alliance by completing a spy mission in Morocco, which will yield significant influence. I'm also maintaining neutral stances with Heidabir, Brussels, and Lhasa, as India's influence there currently outweighs ours, and I'm noting India's denouncement of us.
            
            **Assessing Diplomatic Warfare**
            
            I'm re-evaluating our stance toward India. While I thought we were at war, it seems we only denounced them. Given their immense military power and my concern about a potential declaration of war, I'm confirming their status and assessing the feasibility and risks of engaging them, especially with the Iroquois struggling.
            
            **Analyzing India's Threat**
            
            I'm currently re-evaluating the immense threat India poses with their imminent cultural victory. Declarations of war, contrary to my initial thoughts, could actually hinder their tourism modifier against us by disrupting trade routes and open borders, offering a crucial strategic shift in how I approach their dominance.
            
            **Adjusting India Diplomacy**
            
            I'm reassessing the impact of war with India. Contrary to initial beliefs, declaring war could reduce their tourism modifier against me and prevent their musicians from spreading culture. This offers a strategic avenue to counter their imminent cultural victory, especially given our pre-existing diplomatic penalty.
            
            **Evaluating Diplomatic Options**
            
            My current thoughts are focused on leveraging our relationships for strategic advantage. I'm assessing the possibility of securing peace with Morocco to enable an alliance with Ragusa and the Shoshone, while recognizing the Iroquois's potential as an ally against India despite their denouncement.
            
            **Leveraging New Alliances**
            
            My focus has shifted significantly. The Iroquois are now at war with India, a crucial development. I'm reassessing our relationship with them, aiming to neutralize our hostility and potentially form a coalition to counter India's looming cultural victory.
            
            **Securing Buenos Aires**
            
            I am now focusing on our city-state relationships, specifically Buenos Aires. By adjusting our influence to 50/50, I aim to secure their alliance for crucial World Congress delegates and to counter Morocco and India. I'm also confirming Kyiv's excellent standing and Mombasa and Antananarivo's current status.
            
            **Leveraging India's Weakness**
            
            I'm reacting to India finishing the Citizen Earth Protocol by immediately prioritizing the 'Enlightenment' policy for a crucial free tech. I'm also adjusting relations with Buenos Aires to secure an alliance and resetting the Iroquois to 0/0 as they are now at war with India.
            
            **Confirming Player Stances**
            
            My current focus is verifying all player and city-state stances. I'm ensuring our relationships with warring factions like the Shoshone, Morocco, and Polynesia remain at 0/0, while maintaining our existing post-war friendship with the Hun. I'm also confirming Buenos Aires and Iroquois target IDs.
            
            **Finalizing Strategic Actions**
            
            I am confirming the specific tool calls for policy and research, prioritizing `Enlightenment` for a free tech and `Satellites` to advance the Apollo Program race. I'm also solidifying our diplomatic stance with target ID 36, setting the relationship to 50/50.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: aVdKwiiHJXNqnYbk
          - toolName: set-research
          - input:
            - Rationale: APOLLO PROGRAM RACE: Satellites unlocks the Apollo Program, which is required for all spaceship parts. This is our only viable path to victory before India finishes the Citizen Earth Protocol.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18tdXZhWGA+RcxaVlvdoqMO6bUGzJu5NkAgtx0mzyYQAEhTNg6oagWNh1m5442aKG61pprDqB7DWSvLSgDGbRwacmoIX9oo9ihJ9lBelo2sxCqJQsSgUibzaVBs3EAGYhyZUDuDTyQHdtIIp9hJr5Z+mxDf79bmDyFIXpPkljGyBsu0WoDcAXmQeSmM64/gzIlbz5QdM+K/T2B3Ijrc28ngExlriU53NDfrVvLm2g1JFBUmCozOiEEzwqI0YtZf36j1qv74CYaxIb1ZykNoVY67elBRuVhYJIeB44RmM/5XpTL0QeJz1f+GtLemMnDIKUcNe3t8E01aNlwzUdfNxs+5dLf/Ah9lNaE2U/AQt8DE+DNqH6OcYglqtxWwQNrG6jGJqK4F3lkQBaf1PEPeGESZOnKCtCu680atjnWqHXYe8EHhZ/XQUjEjhy5M0qGGA0XpyNw+M4/vLko89Ri97mgDUwnkgQVlsVMatcBsZQ5HMmjNMXJlaYx2jc8+HhN/MiWM5hp53CXfOTYZpu/Zlx1cExwRkV5KSBFKSWJtR88WJUCvCfgbDhfKHTAkV6btirgRV5GSojNJUPAc98D1zqmTAlF9x1lRtVdfuNvaU3CxNKSpNQOlirO7bZGA/HvPols5fxEzeeSjrdx5Ki8lpyNM1ewct+tjyT2iMwEdIXExpeCUaegWGXUn/vwz1lZ3aKVAKjfD7850pcFD6PCJYsDmfNaYWPy672wvQ5G7FOmtcvPkToaw2WXOEL279BEPqcNmPERbvXPfmNWlX5va4NQq2LJhcpHF9QmTeBbb44CP3PrH18bA339a7n4nlWwkoepktZnnK0ri8JWF16NnuBk5q2jwvgYrua59OWm+IUmUOKpt2ttpnK8UxEl1eS1PYeUSQdllw6QWYHc6z5i2xqFPxVpiWps1/qD6VX9g0+77Au3MV4rmhXOiEb84GFSiM3v8iqmD/wDXxlE1FKJEszKrsl1M48idfgCenV2qxowHDdzZRYWeaMfErpI87tp8OfUHCp7rNrqX/wFt8/BXOFlkLT+SJHzjtFfe0BKBKU+Rtko/q1ROf6+1ZQIS84VY0OBo362TGQ6cW2UfWI29LPSgY0VHLocu4GRxc/xx9kjtwRm3465xQ2EqNwJy3/0HKEX41WOSW1NogOVfhRXVGYFSXKsk+8s//JTrI2R5gNkZ6Bl5F/02pReTFiODEuKXo0vIt9pT7tN028TkmjS8E4g60DnqS+6TPUaHjBZs09kljWskaw2F9USXJZsrC3SfXOYYgIOXPpwWDJNIad9DJ9CMHd9VnwJwTSCr0ZQd6JC0s7yB2R/5xw9KVT/TyvNU8LQAZOWcSPbVgQd+J35K/uYY4HOMsK6j/KV/fpHW1dg9M74Ve1l1c4trfVWy1rx4XVKAz3dH/QyOQETdzfXfRM24BdPdm5tUWK2w8gKVFF8eQZvoLJRtuApzGXMf+tMEceaKKp+IueTHtbY/CB1jGcjzw1DdZMVz3JyMVq1F091NRc+xk28Y9+ZcD4B+RJR9uuVNXvWHmNzoZDFLVuD9DEhWRzvAkM8x6cv114S7PxhO6Ba1hqsvS//Aa+rt/uJjdWBo5A/xn2IGdyIbWsGyiakL5l2WxAG6EEOyh7SrZJKa98mz0Vc//zBWDFrTROdWmBPGZ1dri9lbvOvw1V2YCB+D6FGngxeH4tVYwc6s9IY9yjg/5FTs32tQCfiRcre2Gr3lUeJ4TN+6Vl58ilCrHpZIexsBWbcwUFK5dg0+VCncMfIHC2q9LSlmtfP5jzdRjad9AFiI2jV+G9zy3hSJYo6ADGDZ7n/9ltODiddA2N/SuolwBlONmt/1sqycY11D2SdWyK+hBYPnYX3jd4XiUclDjUDHJoT8MCipyFb+ausHmvZrk96cFkrH4Rz7lHaDqSjeXQTu19sE+nG26H8ddjx3nrS45Y5t+8FITRfxz1vdmQgDEajJgIo7AbClzxUJqTDiS7Ij8P4Lb1bBN/qUZD/DR5TFra88Gucxx4gbCJ0sNNe+u/76GaIGKTlz6/p7NagG+GlvEmkFSOZQZAqTuffdDBqkqc2tuBo4huP46UWlZXZitJY1fNcjRskEIFSxlkt/rVz38sK8nq/VpNX+nB0W1Cjk00Tq/vnaV1y/xXtJTetx6SR/+pm69Fy87+BUDhtW6yiUeLh5IOrDWmRMSMa3k8KsZCswB4O40+SUMK9jlKxPW43rp+ey8jGjP6PI7aTScLLJvgvDjmcikwFZQcs6pI2qVCW1/H8eI4RVazKFlyuJJouaWV2Wgs3L9wrWxMFWSumJXD5cNbqQKBEE6tPKy+Q+VIrVQp9TMtagvTxhgzR1HeHyhkzz1Ng1PptgjgSxDIow6CUuMFjhm9TdIz0HiFheNraOBeCIR0r7bUS4lWzVk7SlIpW0+MH0VyAMtXx+OpAm0UCjAUKyQDb0yXmEGCJQGHzOTCFSbcoBH9XfdzwU/oieTRFBYHOsfK8UXD79/cor2iYi12UbwU2YNX8ZZt3Gu5KD44CimII7zPchKpUX5trz4kNmcfLLvggBtC4H8OGIqTAK5UBsTeIu1XPxidSwhYF4MsfKp3P/1kIDkI+f4aB8LJhs3zK41Ou/apvaFYSKwqoJukQ/vUUd4oDA2z1L1tjY+ukY5uJdCCmfd0GIK6yia5UeNEGXZFWRYb5C0TRyax/Uyo9wI++UHuIYzYFVpjfxkPU1zgQxLF1M3CAIqEW3sQfLkjUtAt2dbWh+f6zuzV2j+zrQgdyHyP8ZmvjS4FmlumyBtYO0PjkWhI4QWax4/KvCZp7bVFrzwdqGTx9bitJ4GDj1ppij6UC5Tp0BpbFKRyAEz28piGWm6Ksu4R08PGjxaxP+rBhHDhcyOVdXwNo4CJhCatD5vGI2yqykOI79P7Z7RscPcAtws8an1IXx+EIbFa62f+VG1DfOKs2M/svvRLKrGFL3NTs8jmjBGAgS7QZocOzVraCk6rm7K6Y45OtDUopkTNmx/z12fzV6wAkENVfMvk+5bpO0idxd/tLRX+XkGjMJREuoIDiFSC//Cx8YWv2lspjMFttImY4heBuzn1EXGhJherB/7ht7xrB9SHearXkneutslDwJy87u+t7s/pogex28GLLlF/+moTzUl8kvI/lxUJ9AqvyE2ZFGR/wJJutIMh8nKi4cyKC1CaC4QfnQTuM4mRgSr/GgDC4jDfk2JPIkL1mrYYLh8W+zs3WDo/tayrx+gOOZJiz2oBF30Uwg9PG9vMFDhCsPgr1s1xVCDit0BD0nZn78Ai2kRZiYSBp428N3kAkNCeAJX7Q+tSwIqj1RCAq2eeKQ3Aoq+CaRqiWO0NyfyLHRCckl1/2CMGH4fyjjDdvBwZ1lubKuuZ3iJEX0IBigwuNP9+c9/yDu/i0gSbHJwRUQ5ISSPxR8VDhEylPntiP1DMJpVH0T/TYzqll4HrO6sU7TVGIJF/WataI+Io70KjIW6RHiUV5y0xnu06xPSwa6ibfXF4hl9RR0s07XKEN42diYVHIoYYawmt1eLOX6BiWmtA0YpGFkEwTYOfabknxLpYPoXklwQaUitkRwmUyd61LJJi4Wu17YRZCtCQTKwG75A7wEch4sPtasoE+RYeeDVIwqH9HoKNwlJ8Zs8Lebv0aZrP7pjt/qSMIm2jRZHnYivbdeU1HN4NyziWgcNw0Ra4k30LbG5wiNryf2SgVBqT1f382rn2joGXj2GcQsJPQzkcW+FXm6KYkprw81s8OH2jeXWgiHII0P86d/7KB/DxtL+4IXneQqo3Euxg0ZpqeAtszrSfzqScxndnarpX8l/aaZt9gC6zwu9Qgol7HLDxIT9t1jmzGo2IsBSXU+j0IosukvgvKQIHm2DDEtdAHii3xYxNpRYVrXdlpe5sFVvY6LUj/uQWt8s7mXO6Tyg0uBPcNolbkyaZ8NcsJRdQUCmWBoXnFvwVlfJNig4hmUEqkHTroxt9o4gQKjFpx0pJPE27nstW0hqWURz4PvFI748UvrcQIGj9j6zO7KwSWjDTrfkxU2tMALXPCesqAU6NHIc3U0Qw7hpgv85iVQ19o7WDnaJMW66xJkmXu+egQPQUFS2Xbc+4SAtLFvR73jgkbvgwsOfDJEGDCqc3GdoEudGFw1wVXZ1Y2zSSCiAczOIVFNWWBr8pAdfy0ODW3XQR/8Z82F/0q74XfCmNDwdEgg829rt2/TeieN1smP8Gqa15Ow4lwWvhnq5tD+YOYpStwtHzP4GlQSOesVAMl27QaBCr3GxqhOSDKg1Lj7xn/2pJaUUs9wZrfAQD3Paopr0LnRJ+4HYVY9A52MSN+vIXNFpLYG1KygbcKal1/kpjpLa2L55sMd0L4Dmwvgip7yeK6O//DCcWHtwOBl504xUhWOTw6JHhUrdNiJ0qLyZgQof6Lp0BDdeMC7W6+IafSy46NLh9mFOwcVSTBbyJqfbvobdgsyEBbZV4wH/mOK5jDm/BWO9DBMtiiEqAQTTQ0SGW+T+2BSbioIf+pveYK9lxK8UjUNGKbUyw7+fmnp7VT2Cy/YBxjB0OSSfuKa7/PZCPsE+zsH8cGsOLRclA0v7DuUUac0sT0EhNr10FzS4RGbzF1X9+AKVY/wx2kDKx7waanu2NlrbHPdLHfAyg8j2/h+iV/XZZwYcMEzh/C2YULXd14dGN/DIaV2jgD+17VneWPRX1kpy2MtiuadyStgOLomv2F+wpLdBn1LaxaoaWTOVWyiq7w6scg9WfiCIbZybihpgGVrSvwr2SG+NuxOWx0CYrsPGH8jRygrnAwuNQLmkaJBgOCvnQ1cGLLm+fiTxV1C/QavyK4Sz7/gXY97QffGfRZAwZKKp0K/bQzDfxXZXy1LhD7Yq2+wgBqzkzAuiVRFd3H+Q95BsEOD6995bsSr4qnI4D1UZDRMvFm+fUbW+Am5Em/iXO72OV2SGMx40+ULyuiaTIgTiIgylTuC3ljxTBDh2CeFmO1C/rWovWoJHtGJNtN1m082uuUdfBNOLCvFRH5mf+QXKPqJ35LaWSI+P/W9BrX6AxkS9wUnRcGDDsYPG4ylwAiDfUvdg8SpBF7CCUDRXWbZ6DDRb0dhpf8qY/OoL6fnXhsJYRUc04m20LojJI9yeZZrulm0Sm2OMNmXfRo9nt65YtW1neLS8+Bi+J/QU38LsUWfHCBjz+Cd8Zw9y9OrxYzHyhTBn7DQuS+eAj7iSfh4H4F17ZrBJv5khkDke4DGpWOBsSzGGolUac0HY+EpMbG9R5lKQBjm28VVs0Mu/qEkWcb7f2gp/Z5ZIhQ8Z3+TyEczIKbeNQyVqRlfqbQuzjSub4ncV20gbI8GxlXs6RCLjSOyOwCGTcoVDJSic9Xnw7hnoH7PMuJqrZpdYBqyWq4nLMC318b68eXo9pitAnAiGSSElpevApwt6I3GdNF5Ul1VslY34yHvMe6UVGeGMBwdFi9xRAZemW3Qph6HeCjNZdLEVs4PA7rLhl8nDeM7KkqdDLHHyP9Zooze5ZG5K5/PzUfX/z0QwbwI4/dZC1PQoFK3XTUUtJIh1ICnz4SLavYxYvSsQufzTowCf5GJGmwU+r4mSIESPAbLxKoK65ATACyfl0fiqV8fjnwSwwWwED1QDAN0qWwb+aipJpFG27koPT3JCss30O8HoQNIpPJR8BKkcjQfD5fnBEl0ZAxwvqLhog0uQH0N+UYdpKvhHiSpU6Jk1ooPncknUrm0qOOK0WQPtRN8BPGlGK9jMpD8in5Wf03f5oG9/n7pxydIOtbEXSBIBvmViTxiYiNrUAlRsIwGSv3LQDpuOyz7rjB+s7obL3yDJ+o+2rUcPu1zBUo1ABVQauSGgvnAoBnrIdCBK5bW449EiHMClVWggxhxCeDKLIUMIZgeOW99K+BH+ZzeP4poCdPNNnYp2LEQ1Cv/50WUGxyiCoepQdKcklCMRpkQiagJeQQ876Zpi8OXRM/Mvq+iTaD/heX0udxhX5UqoZHsNK76L2fJ26lF9hefyVWq1nsWt1OYGF497uXem+ev8GWeZiqICRinOEkBC4SoQO4xs+RFl2vzPHceBRU+eYwOy/4BkcltevQobk6K8faSwJ7sM0aoXoJAKXFjfQB52vR24ZcYITVD08Libn2bR/Eqtoy5GJnNHfd/UhxDosVQWAq9Hia04UfEUxhhpwbVvzwaiw1vhTS5iuPliT32f1f1w5cmVJNMENU0f72Lz9YxClyw4xjVdKnGsjUbHmmhZTN15Xe0Iznm5DzqlWiEbQHaskIEboOBn2pS/dUSI+qbyjNKesINQwilGHwuteLWqrn39xO4qR4Ddkc0AG/WTWYiZT1MxU1baEDy8bNcG2k79jTWC2wuxZVv6iozQhY6+FiViuO5LYSH9C0acU4madW/Lxek+tfaq6l3zIQ5+FHEPMp0h9gDX6x9PZFj4t9z4swHcLTEGmZTzqNt6Ck9mzOj+TaFFAVsslJ+Yo5koR/VyIzUCtccetPsm1e3X3CDaykv21yHp5TOTOmC60dLrYXa+rP/91AptN1jfI2ci3FouN+1zx0fSjoovTjIMHmcxKlNQ1yVrWRhbj9E4PPzS3qZ4/3TPLoRgPopqCzgexTnJd0asA58Rj8fpdTwSX7Km9rTpFH2noOkA/ISrkaTKsnDJnA2rH3OedGE1voggbXhs3clkumH/congMqVemTGqwewg29j0qGQLKedwVUlJQhNY9wk9gkswR6kdqG9vu0zuUBHpC0NnfYmKEbjnHa763cxmd0MkPwJOvN1TrdP2WAPRH0BMalvmh0UOm2BmZBxIdWNO75Y+sUbEu984RzMF4VdKPhpFRRnKrzrTt6NdOk4Mpb1dYLe0W16T5zu6UeDzPQ2JS0pviubOs3fcDY7AlBjAs4zztBEbr2zSjS+DZlBeRHYJfrQJ4tKUgdvw2+7W6f4KBIlr5Q1lTL7HhTVBsjGf+2IFj8ZgUrCND3+P6HZVbxzIWHD1QPCbnTqIqhC+7hRV99jZWm6Hip562RovF5T9P66jLC7kwEcSHF3QvuNqCTkpVxFpfy+Ekd7xq7GPyiZcFe1oKq+KuwAk++KTUA/4YSSC/sSi4m1w5k7XSIXtMQhMTixORS3p1jgRdbVlqPbl3l3xl+sO6VIK6ubKuWpRgR8PaEHksy847k7gFhw3MkWogu9miX8zsFunzt6/U7p7z8k2gDi70NZkkfDz7ICnT7N40/U8VIgWyWRiHepOix6Yy390wqtPPY6ouWvykAIXnxfKWv89PdXRct1klDQZwvbu2CMKOSCmLhemC7B9NRcqYCc/0DuyfxNskWRRx9qW9hY+qzlWhiModrM6r1lOvqYKkkn/Gxz9VcejjR6TeBFBcEcW55cDgb6R5rkxvKkeS7E2zZD1ZgzZO+xcSqeB3su74E3++xZLNKW1JhEK3kwF5XlI9jDCZQ2a2vXehwuilENrehytOaUido2/TWapZAODtc/ZypHQVg6w0+3Flmp/G4uddOT6T3SYkRqsB7+X355abaRTlQnXUXLWXEMPktMxw0g8APsjWDLm+n5qX9p4CpxU0M82oXczrQFFeCGs+Q1ozEkFMwFi5LAfoV8ZsZBCjRHRsQSIWqGddbqaT8nPWkmsiLucaLIlwKcKq981oPw2eLnySElyPN6FoSt97/GZRhp/pDZudt88rGq/DQqmQWeyERPakw0qovWtBsfvdMZoCU9uYdrwVV913KYNr45ASnDjc6GLNl7rScibMcO//MNrTbCFOzOQl92ZI/+e6Gq2kRtMtfDlL8EvABPB3Jk3WOV8FkWWapIxfpvzbAMilLIyg6L4osWv4E5gKfnZTXaw0h804CCv8KNr4znT1cHkQmGAm2FoOgZl/ToNW5TzmOH/RtaDwhWz5tG8im05K4nfBka4FUnZ8PjXOM4RPpYQDzMV21pKgg7VNl71GCt510I2YjTsmeryhCGpIT3ROY/0/kG9bjBS02D6SeQaVJh1w+H8G841IXDddxoaJ8UgZGlmzBR921KcHpwrkHhGTZtxLwjooaAy0iHcoeDAycXZPvuWW8btXdoGe1fUOtdej8RZYrKKdcbdeZ3xZSZuvO4F92pSfSBV2sEx1DsLL4q08GDChLmwWglkoQrv+0uVCy7iK6yvbDgTRgdZjCUXnw8lfxP5WY1S1pJ1KcMNo7iwy6lsMa7aa/fVF7e2Pzevz7eCXJUQnWXhCAcb53EJF18ldIYTVDXzlyw8ds0caFNy5qJ2NswIEraUy3Ia3+p34icGW3OC0YrkdQzp6wtruTWTLqF4Z6MfuQ9nsoRax+w9UOhU69AlWG3BKNNe/i2E/rMe3WnAFnDC8y0Hmmo7hSglveqkVbfU1PKs1ag2XO7uH7lu5pUToBu6wJ+UHsiQcVfOuskomNU/DUhYJkfhT5DsdXktR+pfd66rIJZasSvBDbEaGhBudCcXBcIeYQqiVI5V6I2Xs4TFj+nHnllglCcXch8GqbxV05Ug47fOT3ACPNLPNmDKZ8oQGu5lLTeqeJlv6VGwS1Y1wSgz3y3/amjbPoQi16XG+Ir3FHJP2FtoQXzeE4nGaMyUNimhhrYAbnv+hor4Fxq0jOHBIZ2iV+i141X3yDBXLoRAn/Cx6RFR5Ja6hZ/a02fm94iHo4IqghXcm4NDusOvGJ0m+M8ARepwYMUt1ldsQEmbe5AcMmD5TsSPsYYfbsPwZ1b1F+ilwg++lcBtw1kaYHsjWM1id+yLp9GNvwb/XhIx1+IcqjD+2t9yuhQH0BTtm3v/oD13dHOvX4Z4ekJWV2JxzZn5vlJIPLRuhMAw7A5vmGqDiHBdacoPS22GqvW/s9XfcK0O78JFg1Mm7nrAPmCKzz+qchnxrIEp5eEDO2q8C12/uCwM24mSc2Hdv7gQS/gAHkhgyGNzKoi9fbHUo0BfA66dobf7NFTPyzDB+XJ3UUnykc59kBSYM3aDJkZ5RE2AtXGL8zfat5OIi+GAwDRJSgueHnFGLhc5M7YkuF5HGqaOiHrvf7/T1tuAHrEHu4WkZFTgm80XKbsrVKbzWW05bhp8Nt5CcrIHOdCFeXhFaQU9MksHM96/edTh/SQBf6a0qeH+OwkHocpsWRpdyuQCoAd/Q23wJUkjCiXFtnhGOr0ILz5jim2dKNxZ864UfuClyXVWQkRJoHINRnIjTdDnf9AhfryEzyQiiJ4XGRHXMMx6waBDAiv/Qlei91Y6kCFyaXz5evO/YuHKnPJ6XOIZNfjJ2x/msheW/NFFp2fnRW2MnxDRRTA/ztbB6FAQRkE60gcGI46tvaje36w9D3VYRLjJgEkZ69crcIv6r4NQrE54NhaqACpFsoUBM+mzO1BtcEC4Yi5kGUp1PtjFh4eAfg3L3mlyVkJKZS5WDf1bdJ9hLgM1X183LSav2BA7vXPQRcELiIpok7LL5NZTvuI0GWIhJFeeFzmLdPVbjxbki3QhptCAwU2Ju8CGToleQ7widsr1gwUOft7YnOZZjGZhuTMTAK0UHmEULwhL2aqb3SHY/UYp1HKZXvHtPb09qPkF+5URacMBmzmCRSRNNZ3Zjh+KgAOC7lXn2fb6lO2vgNcp3y6Pmwtm+mfMBCdmi9WGzMaHtFLJRB4lojeuq9cetCghrCrVCLNCuNn04kArzh+fhwt9nOY+/9S74QVvsBBfjJ/qxj29L2I6x9x/NVDPMANYYawqh0uLJyRNqQ0ZY+/JyPiR5jYWmOCceavzV6aZfhMwdsfleSJAAC6VlfRjk4gW4b7TFwvI8okk2c35jVfQpD1YX+PdsZi6lPwFgSBiDicprXkl0fqu3/C4t7n+Jic2B1GqOWCH5zc/N9gFEuWL4zOe8UuE5FTjiFsFyb9he9h3gWRjZ8JcXY99WIoYgqEBUZ0jAdJSiw9JojKqoZ1kPngnHeikoVrH5k6kr39FNyHAaPdywrSqxo9P9WOuGqAmde5MjblZ9cVAcaRgwmtO4SWLH8p48EWYtEY+X7mOC3raVqPltyCnvsD9dNb96jYMnjGSh7Z81rnv9Q3rvi/weRO+y5uSo6A4iUvZ68ipW4EE7Qca7btAwFOxUnv4QY0TTytiThSJkiG94kzszGqTQSOTckskGE7uwDGb8JehHge/Rf3kqnlpXETFlFcAgkldsSXfPB9/dgrdu5wlskMMa7D/7tEGBTMLd38wuKpxXotaaTZyCuiEu9aZUlc6V83h6x+fH/jZ8BEV9/44b6nA/dtNz/pZQlTo0E+nqw2Ap4SGjuVejuypL6W3i98NLmbbs9TW7S0fa3soFb4GLnNfb/8mW+q0fPzS/zAMwKrLWpWOG9/0Pt6nMGniK6/CKWLczNjwBcLQ8lpCfdnhYf6/XkQ/rOQBPHNXxdukMLunAACrUJZs56NTKzo04ygBkgEUL9zdtaGrrS3POwvtVRPvOeINBpWEWrYZcTGzNIT2r80NgNVNlReCWR1+sXkv0ImbuFXDAiScyxSwRT0Xh35jkIyKhlRCiEiQFzCi9ZJR4t4snViyJZ/YZWUIeJrioQvJhCR/bYNnn9y9TBpAvcFKngeksKzbRXkoo/n7hz0mNo6F2yssmLo7fL9eQDkKFtFyhdiVhYeucab44npnV+g99FHY9mzKrXgah3kf51fNkGxE0iYCIAxL7T9LgX88ZLM4hEulG1+2fZx/TzCJ3cw3dKJpvBMtByAc7okrq2yfyS/m6nDfumk/6VF1mlP8UkgAJXv0PYk907z7n4ut8vBV/utNoHPmq2ecgLvtY4vWHml772zKt2JopintFbrmu5SJ7wE5vXwy0o5TpFNz6E8NHayGWBjGZEA8xGDvnL6FfYUa4Ua27fRzp9rrPlqs7Iorln1K9XQ4fYwylcANpc9FtM/7Jg5dRBK2xkdJM2GZjPp6PJB/KiptKBso+7wgG/+pfzduyY1FcdeLCYm3QAVCMH4Kqh3FeIkaELyDka8x92cZ/RlzduTXs9p6XX34gKnZxdauI/RX7bhnwhsJCFX9wpPiNQxkSvvUHtGq3vzTR5Gq9XFdXbowxSuHRaoBPnnCflDDXLv1RUhIFQgYAJEQg/SLoK9svr6cGc4RpmCBAPccdwQV04IwAthB29Z44RBcGIhjYBub/YyqT7CqF1owOIzYLAttyEo1wOHWGdKWtohbaHrO5aV6gmutup/QEx9gACJ7nEK3go2TLsSssoNUsvayIdi2gzXPFMtzrXqffwKTVpB3s7tigTzF6OahP4O2aQy60f9DHqENo5rb78KAwKexe3xH0VseV5KEyLzqrUid9QPh6oXQEaicgGZHpfwtp0OgQUll8s4NWtCLLxrIYr/0d3nCuD1wYMkwJH6wrndhDy5Rdf3fPCde3EAHcFqPkfgHjoBR/8ZSxtOkmKmy3F1qvtz4eI8KhzqWcwWJt8gsDXQwvnoEfbTy+Tss+pZ+S+ZcxNOgEPsx9IQm/r+v1YEm8NKnmuE2iaSJofpUz6nI1wiomYcZED4Q3vRDWTOaJBLyoWHu0asHgaKQ6mRxDc581kHlqkpyyuX+G9JcEsI6ASBGS5RI6h1h8KbyzySLukSsiQjh4cttR7IPDuEqarHiG6Q++OYgIarumfMl0M7cVFL+L7rZ3Eu4fOg8zXfFZySKXPC3mzu1TBf/iQq7mH7WEfNQpcdg9IUfLTomJzuU7kxLDaF6vU3yk+amIo0Zj/l0hf0EcUgzrDuF054eUhz0MJe/XK+mpj+8fPzpriC4T6nbICBZyh4rYXdPmZ0lSDV43UmLQ1ArTzDQ5V82Ng0M61Wp+CDOv61NU8WdCfE+v15Gd13GEsdzce4ssdkG8Uaf4GlpVrm04Csl6EPW/bFVZ7sJqoy1iN1hmUacdtIkeb2r9Eutqip6BokyvTJZRNr9gGFlnwbRuQnWWiTgHAVjPZJXSHJ+nBZWW8Rxma9jhbW16LfCEr0hRXCEWQLHFihYSs4FqvbUFki0rxEveQ7y814M7OYegSWeZ4ABxpiFvt7PNvy66jdpWsG1XxaJ60KrTPT9/WPgNQc00KTUyqmht8cIpLwH+468ilcTpQ0WMLP6c2ISxqWTtBGQprKZJZ4YNY+Oc904PurBzV/5EcCTvGLmpBCfAccLrRPLVxSCd8KNtsPDKIa9l3tfoa+mon9mZhppctT+IKdtZbrcNaKgGCvg2AtCeEplq2Ron14zaDvUF2Uae+wDT5h0bIJ8sVx8rVCJ7rtxk8CLpurM8l2eV9bmE5wSAOaXY9+QpYm1kfpn47XTGQje+5dM6za2Ycr2LPntY+ZyxR1ZCJbL0ZsAl4usvF7GVqmD0DukajvySdwngTzsS5JhKHmobWW3Noen9lfTbATGMYUbJaoPzpakVdG3YKgGLDNagLAPuR/oEDFRRRVsQVde2qgajSCS5zz0wQrfR5i6qW+lXKzM03gI0vSvOstGtD8bheQ28J+P5ZsESnGPTkjO+EcM0RfBgFhhgTtBDIs3qkDMTRn+e4arB67XlZ0aiQYOrWJVdtxXNqIx+HVdDRxuhUBWpofF887MOdeirD0PlF0yIVsPeEWoe6Vc+EdBdf/xA0hY7tGrdXhpt7y2LrAUhFKRS0PJHbiCx6Ij3r/2nubNfVC9wkXrX8f/p3rz8fAMhc8Vf1zFS2ENsMhPm0D9PMf0rD2RJXr8gGlMXbF4eczKEZb92onTW4Cqm7ATAXrtmvvdPb2lwvC+k4IJZIDmNNNQmqH1FQQStq8uNw8DbM+2JbVisiNls+SDy4a/LccEFMKiBz5YJw2/vkRqAl2lToJOdYxurLrwhJrhiC6XAcEgAyQJFnr4rQKRtmSpybUUOTPAesdUWv0dV6Iv/Oy0uoNnjOj/No7rUQ5mIAV8wNW0pf44Gnv/rIuNP2xDy1zGtW8Ib1YgFYzqJeBr4ysyI539e8cCqmZIxSnGHXFRSTmrDHbmvsbSIelvEkqky7qhK+5j+UnCu+JdKqHKieYt/SB86bkO62Z9snpQSKFWKjW9oXtvtlvJwvZqYMieru7COIUWVBybb58Aoet0BXBL+dI6JZPP370ZnRK3twCJ3HuIlwUu0xPhtiiKc/nqDfHmU7OcrE9iVTW2jZ33cjsTenH6VY/RZNisRxyN3K7LifT+xohp7UvrkpFXnDeDKlWUPvdL1Lf/Zryej31SNzupeFgl24engDPedfLtERiV3IdJhdK6C0WNNl7Xf1WUT+iVzfYWVFRLhrms3sF9OCMQtYdUya6tgRF/wUlMVJ/kk3lBFQNwXrTJer19Eg7oBZhSgtrsvt8bBzcZrinilIzcHiHiDgOJIQgjXv2ERrVjhRbUxZ+4kjJp3BN2OiUM2YIjd/mMyKNKjTscihRiwi2PJIk5niaP2y5wnnCROw5G3Iv6VroRCll2rZWa366c4gljVAMhibPcYeG2GpULUkpMjLHKO4dKJBhSYIeG6GyuiC4Eyp4Rzl9sffprPzLXWVtj+MtChP8RLNghtrkbEaFo5D4e13Tid+KpSACfC5c9prvhjCMWB8ypLFvsJzZOcivQXMqA1dY8Poo0muapHo1W2zdXFcgR51+O3SgOW8Uq7iasysc8qmBbEJx2RKX8Uio0IQkirooa5i/yTixTSYg3jhkfB3+ttn2lQlwNWMQFmFK/8tkjt1emXYXU5hOvaKQWoWNnFEYWSfqgtqavoJd0exzN4qrNDJzvBlK8C3e0cJqhbiTmOnR2dotcfSNJdivZWhmc1Zkza8Q8+rSpM1m/K9kPti7htmDxyvxOFBMHtdWrZvewh7qQiy0viL4JMpxgttyiT158+gHdrgC4DcywePcUcxJV9us8fHis1NOGa5qQtz5IOSzBaYKhRtxzmrf4g1Xe4zUXfyb3SV3zG/9iczoCEk6Cc1Dk/p7niRQFbr3lxo+IEhZE6Wg+/p7MWfflqlZvw4ejoQYlDN56oWEI23bqhAhdMUjrTmQNWmIchfIvQ+u8ASqchRp7iJjNnv7/dNO6fIlRw42eTpHXSR3jEmo6VN3ihenP0Mas+aTeYTp8jBdee148ZGUO35G1K9B0DpvvrJocGgL0zlIxxViYIfl47s+a9eJ79BIjqwdAFVJ8olB4lRJASk7L1UtfXvrI6nni6/43BoWRHhgBZUuyoYSaBpO9YY58fLtZHp+IYd0MzRP1G1AYaOpV5O7Kb5r5tvhsskOr6CCF9z7OkIImHzhOtu1rHpeplBHN2+IsenwU60r5w9JqqJYvcYqCgjn3T7dD3pNYkNSRldSZZ5RH59a/wpLSrDkKPMGlenBtS5hfQuaqmp7rlJiHfP4zwBDfdxg8wGIDrGAaP10hfY67jDKKuN06+Efol7C8eQM3y6KdonRbUblcy7LkH75bN8Ni9GvMIQh+euPIvb7cz//iccofXAKKfYvIijH6M3VVe+2aMRNmBSVFPUrnouLsNGqI2DFn748XB+w5mAlqRaZKPQQQjuDtiI3/bClZu5hoBHNQQCo7J+yp1l42et9MloiwVTgiSicDVpkk+6Zlyf/plJjlk6mDXljx0EwPQ+coocIGA7xsjzu2JR9Mh86uHJLUiyGCD6TmGxNFBQaZ9+Ir4lfWwsMH5XmwzTatrNV2WryAvK9YnVJcApwnQQC1MJ915XKy1/eaCei+Cg85itHHhRUBCa/oq45TXkUWCApWRgE30wsog9L5jf1tBhgbDbH4msuNZBBcYxy1L6uJFnUZ2Ze8m1IU2di6PAGEfm2hC+vk7Dr2QxS68RJ+grOlZcXhbveEFfRLxaN5pgkGACyZ3FTe5iIDTCm16ImSx3JhXEuAX9A6jOee4mY2snDSDZuA9F0CtBYybqlLRVx5L0Ine+4IqcjYyN3uKtCeXlbAw3i43gFK91Fh2BwqomMrjvFIBy2cpHzcwLB5Y4WXFt0vPqfgshwQodcwdv12LobKPTimJPD7ajQtl8+psjdLpIijG/310yGByLUv1sS6vMIthyarUItRW+XGVYpTb6n7adP2sKWRAIo0jWZXv0A2d6lXTRL7ZOl2b3cpdRkvd01KxJ0Np7ZmPzfOVcdCcWvvOttyVw8qO4eW7gTxBAgF3vQkUbSzhNLtcO2ox/PnJqMWwrpUjEgrUZ74iTzfduULRwSAFgIRM27mp+rCvEakmNpcQNxO2qmXr9cSDg57g1BTOSOk+YSLDUDdbz4RSskCSG/n3EocZNrfieeTJQOimygmxPd7tc6GouXdVMjc+B7KPTpMIZ/n2XAFYxGgY3/gSQRxRTS3thScwPSilQkxytYfx/+4X9T3PQvJPTr78weuky5w4A48rYof5Vm4T9VPQ1KDtD2yMMYN6sn1EK++jVa6mA6GVbWG75Bn18B5yZxJ+u9RFsxxVAHGVmFWIptnlc5FLdyWFgZRPSNyvGRSKlFodQKQbTfY3UqwhSCUlbGLhBZqZmd5NKzwDsEgCOMUzOFbOcTEzRSaJLyOxddGDJkQVgC5D1QmAXJiPjrDQhit1/lMj0xhn1PiKjCd9gBkPPYID0GqOLsg16iEUPGzmdlN+S1U8T2UcXzwrBT3LMiAP4m1Zuu+pZPehRxm6kn5df+Y7lH2cTsGwBbsS8H3dMr3+hd0Tb+bsqkrsrGGK6PW3gulGbRsVu6Vt9FrWO1jb1FujFDGASuqoY4nQphDeHjpQh3KmowggaVqKvVtklUonZEyyaPRY35+3B363RJPzwm9ZRR8Uy7t+oKl1Jf/iiuLhIJfqLAJ1Kr6kBHYCT+FIKXy7ZwuukmYg7nwQ44yh1kZ6Yy+LphQDY8IHelc7DmGPF29x9BS99MJrpWjwdo8R76cMgWDSDyDUfF0vmoIx8DsqRfBew1JxMf9ZO2P0DMpLhI+I3n3suMIkCkB5++TE68Jji9x2BUTBuPDEY0eWA5sPb+C9AylVjWyvZzh9d0nCQXNxeZzvMuhjeW+ouVyFL/kNBE6K350AUuW/hPS6zLL2G84lZ/lGe9s3zTBMocrGRK4vOsb+oMrVnhvKQMRBJc6LK8SPzXYMRgCYcVnq1oT1Dc+7KjbBlNuEUqfg9NtjUuerqX5grS7+5eM2DDffUwoCL5lDbnSYwGdPYrQiLA2k0a3jEtQ4pBc/IENZEblJASyliApL3I/O/VvBB0TiijR8PSdw/O34xwxT5r0lLIKW9JznWGE7+/N5m6XT8B5NIMQ3zVAvoajj/FLtUiuXibOAX6h0golXfF2aFVEL1gIpo8ZkRGJSRtNT3UKSIAm1QnR8e+Xxe+u4SqSE5fTzZojdQ8yWdBriY/dTa6vWA7S2h4Wr7inASQnZbKaBEcDJlvfUCI4PE8d3Ndb7xr4LTqug2ZYImPQc+PFOBMPUDEIkqeX8ik1VwSRszcElOuz+Bldc5dnyvVx9CHkrKyelGVVHunrnjOYIklP1aoadlOqgCySD77wkN0pmJx2exHhOisjpdi47Qm3mNkh6nMWP61zULQkGitJYwjT6L+pBQvsst+FgHXXeF+bI+4c+bfMBECxxaMFpirxKmnnrxqn7r7bqOGrWXLJLP5IWxu5Sp3cd9pXgXQDLVaD/uSxhY3nTY4eKwjoHEdGgi+S7+7QL7Wa1ZFaM9PSA5JaE38imguIE2+BpcmqtGIBkGSWaUiY2GN3+sVsICCfYHN4o784yR5oGg2C/SEWSOOFAQ4hmQm1tsmQSSiRsZ0kRvQ9LZBkgH01n2z7KQzCFKsBm/xi5emu9t2WFSIXfEzhcsJNtetZScGMiRlPEydYVH9MbKdq8yU7gRhty3GbdMjAqCzpe0QcsQ49FAVl+Lz3SgOwPv7uT6Nb6bwcZiBr+aIdvC3TzE6dGsDUhbbmxq4jVbHwyrkXdhav4NAfrc3yb2Mq37XJgQErLkYuK/rXG8VZzqJeNkqWMTsABHmXQba9rfu5Kv2dcOWWFABSQYzrFCx7ti2pTypb3S26IfIq4O2eMIYym8e0rVvFVsF21mTCeVX0NHrkUaLXhEtjYCRThUpBZvfzQq199yfrDYenFDahh5eKymWLSd+/JxJWvcl2xLLRF3OrfCHe8U/kFlnIxnsqbcxbb4YL4Eu2r0hpEuaBkv0yB1T2Rko1E4qir4GJSlehnGubWWaxGjwNRx8WCxFbuJzkucXNG9yt8URCL4nweWBnErOyJIGst013vNtHWvPWsWRjadPW1sdmXzvlQbiH/xVnhDV0rDOtNtknVUHonuebC0rKbF8sv+OatdkqZJYn7xuvXf1Zp8kSx2HgJ1h4EkHNyi4583M85TbMLXiHEd2Yp9PyaSoa+cocNce1f6qbwHJ5uFD8zLjVb/wSElmYcalVLdHIU0c4WwwOFgPkLsJz9bU2qP9feugAFDFHhflmnsOmUCK3cdhGvVMG2OTxxfRbmUipPgDjDY8Sbda7eZadzVORzkR+3+4+nYx++LbHQ3FNIN51+IvmEnJzKVgwHOzN9u4Jkr0j4cpKp16cGYHwBWuLI+E6t7MJ+TYygMUnf8xGiBrw7g/CrSKZOP4fIENCjEdRDJ7AXdZIf544Oxg6qdnV4dmyDhK+Vl2vbxU6s30te/rnLWBtUhfLQvNumjP9qNOsJaQ7s3KT9ssiimOwhs23mVa7v4422k9i8EgjMGEffdrOUA7b20gjWmKZZdtvF6cZBzYADH9/ZXDiCM7ImQq+1yVLN+nHmPovIIu0vKLM1yblHUa10ukb66qFmfb5r5eVBbSb1PXLD1Dks8ILHw4wd3fzh+/BWJQ7XfsgY8DQDxb9Pv6IlAFrnTwut1Cd8kI6OdM3QMOa2QSENcaxecqbQCah5WbEqGvXRAipmffXcjWXp9YY0Q59a8oGAwl16asZsDeBhz+enQMPWqGEGLJVbsxN+i6YQHp3gM51zP/RTKTgU6siEf/tRBvNR0Vcj5nK2ad2bTb/9s0TEjSk+7SlYBNfrtI/9Kzwz7dwOyboWJcF5koqmhJPIpdB5svwklpwjhtlLs/oD454cljlfJEJkzCquJrOWsYHhtRjjK9wJvsHjdqFxkzwlV5hQuExqPIUQaKgXRSyAjnQSRYcnv6ftCol38fm5x1Rm+Fx1NgRL5WMDNe8qGNevo1WGjvxkUmmGvWQgs/mP4GEpI+bY2W+MACHITYobo3AMpjHcmSPh21F5WDzIbX9xsA/9XSZ6eaZmUWH7IslwVG4Ld7P466I+t4HgxiFfUiFQgzFm9tYO5goL0AX9bMg16gt5Q5BE3INZTn/blsbA7DNs6PqQ9DEIZ8NIUD4ZJAWPPtJN0HYJ1+FGeWc7WlZLkJVP00jCJGzIHLxfosWEQIpjyjggQh81Rbp5ntNuCD2z0syIQl7boB5sfFJiUKY7nlztnyRN4PEB2umQlpDndXTSxS2IaJEJd2cXCszNd5ezf5Ng0XO6GCgq/s08iilkzROucRK238GQJbtuhIZrUvHefMFcx5pN9Mti5umRZgHah/mZOOnDzS/vD+lvawut6bTa52AmN1O7jnrq49k4ZExdLwr22GVoUkQTgll5bTe0tOqXm3OiEVQmjc/hN/NZ4UdDGlNR72Q0RkkuMntTjC6fjKPnbWTdl1XCEbdJszufLmisLAu6dnSaP4UkMhQ96hrWZ+IZFwtBo3rJUHlCh2BFz8zz1L4O8cjzOfVyVRyuSBg3MvpS/H8/fz3Ue3N0so6GQa+x2b24NIAffamGVU6qFMXuLcQT1qEK+5sTYULCHLJ1NQ+c51hosuEYtM5/ryA/+mLIlTKRIOuz/yI2Te7WKy6ITXAVaxQUu8U1MFbeLNSjOrJyf97F8H7qFwto5aOBhWJGzrTe4HXeOwHEExG/rviqtLVf+aWkhOTq7WVWjaQSela50WtP6gIzoSc4YsAQzkIkPrxS+dfgX67lEpM5bR3g3LgaHukY9QgBS5FKhSA5XKyN2M+rs87foxwYigkNMjatRFq5YBXYfx5iaCHXMxA+onpgp/G8RDYc9kLyGAl0QnAuwLXsh6eGg6LZ0HUXPWm1XU5DmNi1GZNFJPIKpt9r+6ONL/XBxwowVNysPr0/p6Yx0+DoL5pXaWyKnYUo03bLlcmMG3JrttwNG7s2/cLAAZQcObYMfro87z80FaxsHbTP1jIw/vBxMlKmbC1w43AimB/mnj6C7B+FisBvq1RoIVZm5EID4YGtGp7shVITAfYsgvanlAvDLOcmFMSh8ItvnufAhPHkEzgiIujHvPRl7JdxZ1DuXATbVYxrKQhmkNcG6Lrdb7dZvIGWOTf1Gcs8WeKpr2snbcolRVo03T6W1JRsDo7aNUPwRF/xbrjxNZMzUUiE7vyFWtcQLT1LolNphPj2/tfYbzBC0GktFiHI9LEdJRnupZuheHJAn25M6vcPEZkinL4v/wIJ9EpT7TU/P/svFPTZf98Duw2vJ0dbt6uvVqfA8TXwmH4zWgbuAb8ThjHix7qx6FzSwSqMPwDRrfwG5L/TuVjKYb3n5REmYLxtdMDZkZvfXfHgK6pSNA9HvDDrsp7jPbEhpRX7OemnvuCcoZiVeXbl10JXXo++Xo+rvpIJHWcQOsFabANLE63obXdQBpuPIvWzAW7lBq2eGcBhQZLbgy7Z0KZkFAXRhqbAS2z792bmCK5Y0MwdTGLsANpwIysip+Nd4bZa5yk/bMT3BcQb8851wbIlxPRfwz+U/DSmUBfgxymWBub4vrhZtRd/3mvav2TxDkleYpPFLpLwAgVYpLGMDW5qdrYtEfsy286F2vNd8S3Ojp2IJxNMAInzW0C4AMqtM9eCqvK8Et5UbS1wmgZ03qw91q2SAyCQ1C/ZzWoFom7C50bEIQvrdxZU8uKLS5NxuP1JFRDF02ELybV1IqGmzWfLo5zCC4mKAoYUMy6XUBaH6dpenfN6sHng3HRPhxm9ttOvLo0G9YtM9A52gCZSWTKIm5b0vTInSfm6iSKw8lTkEm9odbD1jIVUpTh/gsMYJMQv9+/GDKQdMDVDMYpR2ARNtlFm/ktTNUD1AqK8UmXGydk5W2Xbcomp7o4JlNxaLhfE9ZZ8XgK/HfZnNNdo7AoGrWJyoCigP17FrQQWUbvZs/PKc6xVyK5zSar6SpWU3y2lY2AukoGU5ZJOWoYsrU/QjbjqqoBO7FvtM3Z5y5n86aBpndC3pYrzlk0rKfjs875iaGBh1gHgB/r13l9Z8t23aoKoH2+kR5W/BDct7oY5nDPVKsu1xcQiCTDLRDnKO+Owll3AFwWr3Zc4q/g1WLBegUkVRRb9H+D3RGuLGlA2QkRSZPwp2K1zbdyYdAAempgJnYRQLAc8d4vm2QvnMfbNxUwrMbF5fOAIn85HUbDPjQwcPjdNXnU71iT5haGn5HGBW7gdQuOeQu/hFpy3mtQN0hS+yhZD7CQ3+iwcT5lKuep+6jAm9i+yEv86JLO+BHxHHc1KRJdHUjNh26w3lu9llCGt7LQt9Bi4PPJTQSOYCoQDZLr0ETlHX7LFkqhtvJcJOnY78USCz6JC1Mb1+3iPQK2Z+cc1hXxEd0tZA2k+M4sJ6Jvdi9ZYYVuZKl9sf1Ay9CU/jnsRLT7FCMGCq1v/WasODVgDVxXz7ock6dX/EJRTYyIQ+zxUMGUZmF6Ba0IJn+u+TSc6pQEmw1SaR1/cAyL8dSW36pgwEFErVb6LmzemCeLXmLjiOTzPETYYog8Qseviqsuw1EnaqoyMvGsKYItC2PoFZoSp0jFyEKvIvrt06lKCRGakM1p340GiNtJNV7j6uf2yLZp32snTrLOcdm2j+dU974BasrlUbkrAHUIAVCANidAaOK+PJzOdbf4Nqswb8Z+Y54+vk2LYWjYDSsNGK5t7KUWx7lWdAG+fwCHbaii4fCRFAblBlNyTweJnDX4Lx+EPK0TGWuKSYIerl0FA1fuMlgs9DZXvs3z7IZXCOtYA3BS1KjJ7ALLMPohL9l6x90pkwuEZqwsCPcnkqLudLZj4wethVKftWOk1VRp3DXuCedkZH5PqKq8yJG+41xBJN4569R7bqV5EF53kDve5yxvb4SnDHzi4UwybDf1x5VRN4FIiQOegL4CLMA/bTcwUYS5gJpA9oeSLk0Eh7sH2GNJwAy8BKb9TIEdAlqDbASU6+QBCpf8f2DyYOqXsmk8kR3vqTU9MkVCiEw8eoWh+HJE1cGOR52PWTyCDl+yR5tu7qEwbBjICSgG51osPoSJ+dPIsH6iBDmvz3WbWR8YhsjD08N9mQUsdNc0enKP7z2hDyrSSOv8hGZZWxwQA6kncrvtmF/kQjDvGlGa/mCFjaZCo94n9VficiHT2gdhqfM3WNUxKurvUjjLy0cy7OLCtfoqCIzvJlYp19DFdSPfj91ZXqx82AdUAd37+WkGweGuDRqPxjz65I24HUa+xCxKBQPjfZDNXeOK3QZFTB8n3xq8whXVCyYOrvkBE0H0wfJJsID9FGw7a9q1Hzya6BT9liGbIRSUelysOlp8yodlWreVS6UlfJVI/5haN6dGVfz027ZC0PcUbYF+1rO4diVh61ELBHqB7I27ocKGxAG8m/G5nxE6+t0jdl6Pvl3RMHENXhr9N3ZUxcqGUqGeOylxG6n8bBxtdtQp9HxYCgKY2G0FVXaCB/Rt7m7M4uU0hsuTqYMO7XxLpaThKjP8+/+9TzPiZ3i97Eqajc4FPiLUK4fI0nLtsCgItlagVf4HRfaOwDeDc5SL6q73eGBNCU+uxmj66vSiSRs6LzDQJwqWUEgsYwhm74rYv4SYxW+30rKQVkY6PqsKLSPhj2B3G3fGVLGifLedCh2JDHX8o8Rbw9/90NY/5AgqOiRGjYmB5hMh1Z4nREhgcF6t/hovn6hMdIdk+tL+5gRQQ6YXbcFa4gNpooetoLCRRG7HOUwHXsnZjro69WLaQcPc3yGo19ziLoDWQi0QQh4/iVk6+2ZW9e4nQkv5VbSg62iihVw24Z5dYoWCKKGj0zXCfgWLp1G0p8jXGavT+batLqNikll27YB8KClzxdMq55PIEb1710w7n5dgRuINJQHR7RwVlAYJ7GpKLnb0NXvin5B7u9/dTJwxOZF7aQzPdJXc7hj0aAPJY8H9nD56pN9uSbYSVofWqjwZBM1BahKpj6uUuH7imy1LWhKWtCbQCo9AZUEkKcSwRz/6yH244Ozw0MNzkWX2T7fYzxRgUa4/bR7rtsleHwFVmun7wnXH40Sx8hNu4DsEFO+bx1O8xfnFRvXqk9NxaujP3jrG1bH8BPRgJO1gMOllXCe/Tzm/6xx/4/ijxivqADDWxl6aS+THrajXMijdGG/IQKbv/9vxYs/iufmuOw4AINQt7M9EE85hE43RDT6RjsQq+uBcYCXFsZKDImGslFu0fgkSxX6PEhzL75dHvFmQofJ0i4ikf+xPx/rJxNCCC6EZsQfrXVBHtULWQJZHr0SE+Q/bhdZtoAgNp4ik8vVOfChYf5UoPiXuFneMn5KpzKYWI2ZBNx3J+Be4dBNgRVafUOwtOVBYlW/cScLoJv36B4+AweG7MI2XwTAAjg6Fyq8XrkTzvf2Hk+YwmA5FeUlIv//L7n9M1w8xB1OpH1fCMSgX9naXdKKLNUumQN53QHp3sXF+wUmozOiDxBItE8RXzFeIeXLiO86HTjgNzXWiH/bZUkl7dahzqSRDXZy6L0jGECpnOx2DNUvS5HEsVfRB1fhjHlMLeTzDU/WkoQ/qnLPqJN7zO2Qn4Lsz3o/hcNbsgPVgqeYUFWGt6169+ZY0lu3KUBfrU5k3BTQfKMIXGA1FcfXxXf/7mXqOEyE2dYTC3vdy4o9PhpqAT4PZODP6tK3rKKTH+VkRY37CSJUKZGgUDAvCJHDVHiHztzDkOwaGZb+q6a0vNEFY4GMOjTuLtYj17BfUqlOXs9i98xWFYZxvDRLCSBs+F5dnt2tgyh2H8dxVesMHB37aQztqb7DDgxe2V4Yz52yYMfssNBcoNZn7mjRrvpWExq9gKlqQVclmj91mlRDOuq0I2V9thn1v+wa0s4ouPpSw0NUOyZ9hUUch8G28BKGaIMSfWdTlq0fCKy+75OHcphVFw4CEwPrM0zfNKt5EAlF0I1lHIOf23w5Da6x+InHS8r4ypY7WEqcFLyQm1SYRJbhWqwJh+a0VKXb9P44YX3zvTmKCCg13MtYPycwuk4IAH/gXWelIRsQvJI9Tp8+p4rSVb3Xkrbwx6xMU+iklQat2degQm5LJLxihY8wRSqKAiNeipwe4NUfKBa0B8d1lSZ9KXLCUE/aiFocCLtWRs8cUbIwLWWicKc4mVpmalRlQy1bG/XZEXE8OAtmT/xaJ/NFkz7L/aBeg2R+egWYcEz8aJyTLU/6DdZPbAsGbB9BHm8GS57mSALwTOcfafDpl44sL6qh7lKeAW4bfAZCDyAnC0FdlBcCf9jBXZUuXTS8npnkDk2wdxPQc1Hh/CU0wuHtC+CnFEE811k82G02opuVUU/US2arV+ZtlSUjcOI8FlBN1O2P8vO76KqxBswFJ4+ajGzjVslNIA+e+JGurIkj3xit8mrz9uYwDFaMGA1xeEOvqo2xKfSK2DYbxUqKZJ5+G1vmLsbFAstReWRNIhom/V8STOBlzcSMX9Ol+cUaOrEqBIEnqk8ueZ83yw9D1AaVpmeiMdh92WJMyDWAuu61VWdgcuUH7GJwlFqpEZ8vvl8leG7sBX5XeOA7itvmV+d9L3r7fqdni0WF5qlI+mH9v+DpC2KhEMUELGrPuymVGhqsQdxVz29P8SOHM5MmZD7vEgi60g2Ht32yIsg5a2TxWz8tLyToNqmLSrieunZ2T/LWuYBf5Zk6twCv/FgxXUrFApng4J5QiVVPZ1wyxRhrHAk7lDOiIr71fZuP6aYhgKAzA8WcO92QHiHN2MP9ZGWMYYqBv8dtHIU970E76SHuZXB6AvrDm3grOc4t4dH9wrGsOhdb54Rdn0a0e4EkPkWicgK9YM79YUo8X9ZniUEDLDj6hDsihCD6FOOqL8kweLBBWZ3R5lw2GCWnpBRt/YwE2V7pDRyu4yeRUaXQtoVVsx+4qm8+MB3OFWIx4ieqps505io/9bpmP6oztBwvdLIrocf7M4TOeet70AC/bKSKDe1/SdcpUSR+WRkcyjRIcJpUm8hWPjULG/UBteVyG/YqhqzHUZlarU+fBMkx6hoFC0OAr4jSpxhXTKlj9C32ayhQ55vwTXRC8iEcacSy0nzm2YHAc5SsuK76F+ADyzxeC3dWtKlzeKjgJdrfmcYYb9lUkblPVGt3R//KJbcVTKYOl2aBb27VhQjMcEBNGqQizXV2NP6t7EhlH5bmmp/hhsrYb35nbPgCYMjwO4Z32L/ZEk2w3OE2vBszIn9hYHCFchSzGwn5JQhBzEryMGj7xR5tLD3W6UkogMM+6IAHuPMomdI90aV7OiSwTkSoGVTwcDrJYJ8KOPxgQssg/JDzR+qxsE/KYRvX6a/jo4zXTArPEKBCKqXf1D+vaeuvHqFMC0316/8gSiMoyvyY+WmM/SDXM7pEAWr7o63erH9wz57ZfAwT8s1sSnxXmwCZuSQR/TNMqkgn/aa7+7G3bWGANTq8nUVnVWaUCD8diHwG+qRfdEPdhXBT+HxLQK2y5bnutcqQmctGznGcd4ehaNyPFTYt0SSEAHk7Gsbwml8QEjKIKt/Viao1XLZV3QWGrSbUKcdEgSm+3Vz2wbGLAa7iaB+pyAXsKtnYRgPDYgxpqBQ8bcR5YuCY4pO6nJvOOcIQZk7Hl+m8tzwieLGKNeFWzflxGwaZ8HmdKoEHk/9LKJ+rV5YqM4I+zpoP1fVhE4uV68nkgcWCZe+ltoimbz0MqvBszw9Cb+9Q4edIjf73jfy9WNqGucoWuksD4zB1fozjNZGOCxkT8IZSah4rP257D8iZeRAp3JNCHrnTLgDFK5s7tcNNFY5T05+VnG2HGrCWW2iwJmW9GhvScWVEfxGJFM1bq2nsHDgaqTzLMgWfyDJCtuSbufLnHuIjSR3OD+ZGnnTvkjje7LcPhMfHJz2n9B3jE38biuYl7NJYzUtj7gKdJwOug0kF1hmdqHdms5lJV6Yx8UYxomy6eCsZc2CgG+KITqUf/C2rYC5FgLq2hAr/hjlOg/RseafSb3x5Jh09RatcdjLxAaNLlzUWaUzEvp0DZbJaD+d+OQYttMVWI2rZMmVckzJKxVBXtkSiNLtXMu8S23QfU0XTt1muXfHknoO0no3JQiBWaXQVLRkwIavM3rwFRX8FXQwH9yO/HAnE9xSquIwpPlj0FTRfGkJ367NN8cwy5IwL3It9lDMaFqzgrcPagb9m/959awVWm+wROYw9o5cAPpLSmeHXtS9X/bRCG54uRLm2LBg+K2ruh3s2j0dXrcNrmyGxDaRiLAmPXpVPibyIefgxefy7GnQQ0inEtCKCGLWPac3h7992sNshUkfAb7qV/FhPJcrX2P+Adh02V/5cX6XpjfDPXZ6sdU8wtNXl2+JSm1DlefK83cBzcuNktbrlZPuaSfmXMWxiAvWxSJZHFz1ncdrgcQjB4V4ffRgfQXoqkUDY0pLgaE+VshIrcknUL+qfHzleIaeDXGbdh1DEmtUYF86DBxqlQBUT9ItJ3mmR/bTk9qLCST0cVINE+aKwBSM2SJDB2+PIc0zLP5yc8qcgngj187tJhqAKQckxGyC5s0BLUK5JGqtDy/zkekvQ+kDO49lsbd6mKiHCFY35hCCx6vG5y7oxPEgc77r9Q0Otqog0yjmyTtEiRV/ovZw1QKSJdPTOtNW0z3X/7dW0Cq3cT7sARhKiJbm0um/MErTp3Ymfuoso4YY43y0VrVfIz+mmcGIo1nhqs9puC6NGuyXWj0qzcYy6g1jciE16yQOVURY4zIK7ladfmazi0gKlo2dPn9J+lZi+AvXlrq+SGbnb0Y6wbrU9KMZFFETXAgC3xKw64TV8niB976txaveh9egsJOiXNdicnqZ7pw44Yyfc/1ut5q/CD54zB1htFLVqJqs2zwRRxa+X24S2HkUXt4WDE84gaw5GC5LU979IngNaoWq9LrnY+jETZNH6HwB3aklkv/QqA7Ay2/Wl2hrr/PE85zPN9H4KJJFpPmLmxT53ydAQSwt/ei1dF5aSW9qz5vmxWlnAI0CyEzMpsL9zBv2N5EUinJOlwhxwSFTeZ/+nPL2I/FqeFK3ssoGJpvxtiLHynzJcaepSBRENPB1ls+pj0TOwSi+B71mgWeptL1ScJwYNUIsgO4g61XogWnBDuSa33meJZGBhz9JsiIsG7ncpvnlz0ooM3zxvTpLsvGpd3023XfEK4cifiVoUyQeKXi9vlN4FHykYUat/qlNAAD4a78YIi9QFRaKFsIsWa2k+955m0cona3K6WESuk7jCLa7aQYIL9UmFDpr1KS12pF+I25iCDIIovQh+nahtrI6UvHZSjh45/8XJgOiOvo5XmBtGHva2HHuiYdZDkp5GQK9rt+jD5+Y4w1vizumooD0LPLrK2qMHbgzsJU3F4N6P3lvYnMz5BvyvRxvDHcddfovfoQ1Jj4CaoJg68uoRbEDlUkvAqsvdO1RkPUCBIsEXg/+AzSiMD+/x/6sMVlqoFZ3ZPTilB6vAvgD1AwBXZiR3UiGlKdMeb7KA4qyM/QeA9IkWNZeYGlH4UkO/PGF1MLDbhi0XWtrP/Ujziyn/8pvI1Ws744giPpxmuv/wlMQhWjrwcvG0QkckbwlZ5pvd3ICokIHYMhWoYvfr1L1OnAMjA8IYqPCwXaUI5NT+dVGGlyBPeTgsa/hQM/m1ZBFvu1S4HbtIhBXnYuAEoTqnxrUs9/QfjJStejVRmj+8GgQM8OhThOsQncaJvEMJLFDjKkwpQ3qjqjz95ehDBsu+ME3ng8PKDrYVss6YxOGgodNl5HHNVd/ycbvSTJC/XkUSa4hdfk4kfCvbeZM+Au8uvaUom1bXJrOB+Ec+KinRJ/FwjT6XLzKu7l2rapVOtL8ffBjk292uXU+8sMkSLlbmL759/UItU2XlZsMT9mtJYPTznjJ6wz2hYjmLu4P4VFyB+F5bhM2BtH/+L5zSdC1xgOcGjoGQRHWvViJU7aM5OKRgrfY1NgYbDe5CZIvjCmW5BC8I+wAvJHeRDL/9+oI+jlD04z1xOVTsp1k9sv8S9Dd871lYnHTFrUmiSu9cO9lVuZH72M4P/d1myiiguouMtYWdWq7Xqj5B22yu13t5H1no4agOMCZZplGxbRDtUE0H8JP33gqimdEi2kNrfVPye9Rbq/mz6+T5utQFV1HEBjNTnTayK1/JwZeTkLm0m9m3P/sr5YnKHy05THzMDuJyEcyVh3R7BF3cUbPjaYOH4MdzY38e+4cCQsNHNgr+Zd4o9N7tGj2TdBQIFoJgSvfOeSTqmy6vQ4aFqLmuhYIfbhRgUlHyxlid268xDx59SlxgLIINYgBmkydwarDQa6EFo/AI4Qcvpj+NbZvhB8b64Ne6Xls9gJ7x9/NjYZeFJ1UuQ4qjlC1A7quSKBSJl+YDHyDDtKMFFPKXWkD+JwhETNwjf63QwyNbPWpKmOfUJwakm0E72mI3pq9z4ZEyCb74rbTS2FS8HnBM4xdesgOayCaD+8z4O4Gy4pK6dzjxxsiawbw5ALnYUyfcstGj6av1rTjnsmxl6NwwUwYZzLbkDRncXGZI1SjtO/4HFmdtr1haj9qv70I73JhfPpC/IVeeM5aXEhN3FT0ugbO08+ZP8DaI9Ka140fMzLjGCLQNM18usDaDUZ3Fl5cc7txwtn3jDglVbncDf7Uj4AI120R9VTpz62Dg9MldE20+KPR+YTsJN7kjVUUh4+fXv1DM2PcETqn4mRiD3qgfvAQJTfH4GcubWiP/L5OO2HwSHyHsn4oEi2ituPTvjKV1Jz7Q578wcRWQgRm4Oh6rprDRFINjd192KJ9FarpD7Aa4Gh15HpAuBFaC51/0nfVNl7ZomN40RGenu2z7izJV+booLmpZa39nGV3JY7X/RYEEhK/wGkzPLagecqfB0tLBIaRRDGwJDDq5U0KnrGXlVW3ZJfUC837VbTACKhLorcB3NBpoz27VOZ0Xtowa8T76CW4DytECEeKxtfmizeimhUPBktq/gdTGlK8N1sTryU1LFgHh4hIcXWbFazHBYfNtR4/fyg4fgrAeMEhcaQho1NDFwNb/tBfmoZGaK2WQa08lwYBQBNzUzSdV+PjpHP2OCYtGlMHC5wsObumxC3SKc1lI1z+4bX8tvf1P92YLI9qNeQojhNlBc/6Ct06OE8K4jfMR5zon/hy5mmHaRByG6PnizZv4yfUBiWevuvATVRw2zyrGTyvI7MQdqFpZaHHbu+LqiPOHxtjuCL8n/r2SJIueU4By5ITYKlkXzXHPpwKmV1cllR/6V72/LIvF1nwdLaB1ifXoJW8w+Am9cJ815fcYnWl3dr53io841qFF4kSx2jyAWtIgI6pjELox327vv2zQhbCHslIhTJBeiWdh4DynEQGx3L2FP8raKVeWSPLB3blg8B9NzrafpJkPWF5RmT8B3Qxv668eMb6sf4vGmokfJWZKoC0ZUuY/SsDixKY6NPJEKK9URqMeQlxAIPsCvxlC+oSkvlJcK3EZ93vhPDiAwE2xwCDovzk8DyIDazmUFgan/qHI0RDULzf+QqkF1FjbU/1UyDMSN3Fc2A54/bsd/tN/foMyFpCc5PlgFsgeEe6oteyyoSsuRcZxZISfnbyN0UAcxFaYTMX1+wqqYCYGBN75hQPkbRLCjnsWkaoIsERHrcDuiQz487v7zPAuP22Ep66yggH59Kt76egVgAIXu50p3GB+ClRNrhOF+frucV515jUBwLARpNwyyMfq3In3KDCDFl4QC6GmLqorkLh6CcxRXv//i3f6qsWYNTzbl4uOZOWkT2BkxIWS+KIb6HS20wSFikK1WmoaphV5CpfB5ml9qgGRVbtAcSjHgD8bAzD4ehQ6kdUYa5bLXslzMAk6tT6xNUZaOO/h8cOsExCJoaxRr4AyAr1EIoEXxh1dpg3k29H872bAAShhs6yfPEjk5x5YiMOzUm2DZ2MyP40AN0QvCZKqK4UiyX1Ao/cNEema535AyhePuRK3edUGaJf1vrgFcxkXO6Tf1ql31AGkfi6CaWptgFe2ltAdXxtMlJ4wS6QS+gwm+VMx97Mfxl9BLwSUNeiaKfLAozxvHkUiBmgdTWACWX8nw2QlmfosG+0j6/EP53NM/nFIDVarknZAVjc1fYTEhX7f887ppEKcx3upydETjF0IlLkslVP+n9W1Yi8HzYYXepkIIlOj5KN0jL/kW2EiIV39Cqfq9vWQUXLR1jF/AdpL57kZ4SK5avv599ApJkQq6alPaS8nQldHuuvmaIiWS0ToWvytVftARlHV2Y38MKuU7/OfwIC8eLGBnmDhgIbY3bSyHURVYETleYkhmIEWs/Pwj6MPFATUITqrYX7OHj7TMSGQwF/DnxVKpYP8FFtMNhUzwpbVIvkphUe69Zw2Y+o64+nsO8sHO7V+ffi+e8B0XCuDzW6cVdoYlyMqMwk7TTD//tiLf904Tvnc+ld8P9zeuWMTpbwq9SW7BpeG09coC5WpAXBJd4QYcb9ZJrdNv2Aa0sHol2o197qM+Cgeqq0OqY+V2re9pKIRktnccgLFC9aZPJ8S1VaE04EN5dXp4Dcx1UiAfIPUt8SpKXaaKuMWfFh3SD2fHGTFDqBGzEZpfUvhGAhg3d2pvRSH7cG+vUm1V/nu0g/HZnQUehXTIuOAD0qEi3jLVxLRyIscrwAtbVzABBbLVFnmP820KPjoFSBqW69C7VMDmd4hTxDP10/p6Ya4k2UHixR7vZNxoKn/i8Stghkg/3cZUhCJs1aya6aaMmbtwdDZzMTbchHSg38IHa3wH0ReC7g71ISUkT+5PvPzT6P6qwJQc9KqVbx1OB2mGy52k8llwj2a7kZ8YgboxErN8ixQDApm1VplFst4e4NbsQ32l/tUkJ/m0VdJw0r1ufrCfIceP5Ybmcgjq3xzRF4xx5091o976TD7Sju3OGQ7qHl0O/JwSI2XDI+Wt0DB5Bv/MarlF4SABWB5rZjjD0kXei3Rnz4PR4TbP+lWceM46ME/Z+FtchNQUkaJC/tSw+SXpJOtH8A87uI9BAEC2D/pRI/r9n0ld6JgI2nQTJMoX2Ee++l14DgCcWELboWcdQJLQq62brhqwud6FSsMQdEYspqLzfwZoyVeSPevSB++Ate6M65cfNMqm4aitD/vbdlR/VovMHs+RLya/vJr925bAVvLSH8TqxOs04altsKMezUoQNoiSW+vrQ/YsYW7UNA0FL2kOcaQ1VpLE9flUtsDg5tFj0d61UuS6NoF9JhmCnkHA+XojhpuaTq0jemFzR+BOCgK8d7nCw5INmCUFyNOzZHxpO6Ilz9WzHWvKDyl2Rqw9J4oKvhJ5xemD8lTHLGN0lnlFDe6QMIkKLiIpQO1I+l9N1hTGSyUp9w7pFYNtZCycCigbtK2ekFK4xrBmgQVVEGxuk3fFPhUoZTrwtdwdb7tIfFQNZdToyMeWdHbLmGcBi+0TSv8rPEJWuUoJYWrQRSBlj4LZ7E1FHhDgdhukumPNfSjTOd9ubh3L7XfsXqeaIDb6mk2RBuW/h3njFoSw1n2WixG1FJqSOf4m6z2osIafgIUCQOWx7T/qaYZb3F4i/KaSzea1B8+Im+5Qp3sRcBHsDxOZ4vIBdNu3vsz35gY82ueHcCtrW3fRs+Q5EV78At8saWwmZVNDvWsxxZHc5Wsnx0eDXaeW79Sxh9eEbZ9rm2zqolcrLUOdmCt8ehMYnqhOp8lswc5immdNWPJaPRkSsjelUtEGuzLQAn1uu+91Yc2xfTVqc8/NRkiSKCZDtn9718bg1Y8j9dRN7ShFn7M9amTn1GgqBHHY6/GG4WXcaIuAYOzhiRH8ML0aCV4wevbtGurYEKq5CFZPcN5xEKVCkwCc70neIgShP61ms4K82LH7jBF0lpgIdt4oOJDRz+dSX1MTpPbHetoYgowoCK9UwoyUNtTZs+IZDQqvAdLWYs/Kz9aEGL9VtpodQ5EwfpHVkpsqLo/n2l7D8bvYvjndk45+qvIDkh3ssPiz3JHsv2OdzAI5EnkJzKlzg80aNTStbIt9iPDP6A+NLX8oolGJBQv678u2Cg4PzViEhJVjgBpeKomfx9W36ccyQ8BvIyGcTlvVSWj8mslhxYLntwaUP82p4I3ENTOu0td8SkfNHzg9qlADZAWGGg6xJwOr6auEi/QOvUvwF9fdTP5gIHBX9680DwDagvBITxqpAtIqZ/q009GeK7qNLK6BC26Q2M1WGu2q7v0mDOqI4B1lOcJjgU3aqHO6rTQmGSx7VkFbB/vfyEJWHH3/E+83M21Q2c5034hatFLvxROc+aNU/N8iYhjuzDV+Y1/bBQ95d979c0pEVPjCS3CTNgYIsWHkMC+5kGHDKDW19W5Xuvp3LantuvVsBS0u3r6kwwXN9BT6BRCSeIrgG2jYu0E4/O5OqZfWEvXBrmIwJGVQsx9RdZmDkf6cm9E1ULEnxUg1pcsB9JfeL9/ZEFRdsDKh7kOwqTJvSyZmfYAwAqii+2wEUMSxK8O0aoWYwYVUK7rrz+okrzqluu1rpAmh5OJP1l+wQBW06MbYdkZO1qeix61IA90+7uRl9Rea3/5hbxTBqMKXa2YZGMAYq0erb6ElSHI80JHUvF3R7mxe0/c9A0HlcYL+LbJxw/Ji/G2QlOEAzeGHfm6MEalXaiKfl3FL8LhyXNIfdSeihvGOf98KMioLw+7LefGaIF/0o8Op/A9npkzec2e8hRwDcLbye3Ksuf/P2fGkMw/lf6EXAZcER/zaW1kAOsN3/Nlk1sQIzkgW9u6SVhp35pnDhBEYSkgZFUmkwrNZNO/yKvS48XKHDzzHh7DPpbuPguWmFwwBlY+91i3xMDDiF/El0rlNbJ8D2Hrbhmib8C+By4mjyBJ3xvGOV+rEQTMugw8NsZWyrwZzM3MsK10zClo/5Skr5jCMnuaMx5EzrnQJT+AnWBY5UzJm36GYHpoHXvo56uskmv7aoO3NiJBc4INGYzISDwDf+6DY2I1+3stQTlGq8vpZ6XdUwpAT3syktjV7cu68gvlXP7+5q3oF+GjTGCEhMdyr7vRWggEqJmBGEyYa6QRQHHRD641CmYlrAu8Of38kMhQpOG/9Bced/j7AJlLUcbGhw5CvL3PSpWdqY0+44w+O9qREzAcvR7WBjJYI1pSWMcpPg75FWZROlphHCz9OK6SO18WIkQIfqqCcB//Oqg80SWK+eSK2+ljzDZMJAyryZoGK2TCaP2graHrQ9Jr51TLLqGONYpC/e6jal5doFvI7tFoZ79STNfN+64OTUxwvI05IEPaiDY0ushbbKQI8ztNBD7G0tf2zI4VfuY7CU41EaluX0UK39suXNJqZEUO5gkXdZWL/jlRAWSTpk+kXRoxOoZ8gxdpZyF8SE9nvAnGK4unrRxqF8L0w523d7gKHL8tdnd6ppvKQEfo86EXeMfmATVZMQ/nOoquV79CMqlkzyLhKbUL2AiPkVUHvS/3bFyAlnO6av4LnmQ2WY+da7tqD/jR+Rhv26fHd63wcXWwX8v6u7Ub7z0pGEE3r94oIvLtYB4eGfLoNCjKWi2cDthjA+usnZRSEmgffqPgmbPop2yGHlz5n1BsGneNZ4bbZY+ayD6HzuBLuADtdg1MhEJmBq+KQJ9nErOr6rB08/tTnKPkSAtV2dX/sCvv3WuVivVajKxiR/YSa79vvD+kXxqkAjJdLiPcuLcE6V1p6To92CCIAVvUawq1uyOWCPQAcrfkKrxWZvkdD45PvgYN3AJRMuK1hexb5Ucz/WcyZjxkYLoOWg4goluQ5CBAWn7P4frdQu+bndw5I+OcUIUCPVu96GtE4lRxUa5Yj9UczICfGNVNnMr4JzNNQf4BVB1jkZfCN3IgSLVc1vUeXVt5aN2cI2+sTX1rB6Ml7SeThmxSXqXw9Ujzz9bw6/MKVfLJ7LLxpUhHIHfwiN+bmeZmvMpLROynZ71hGgzeoN5mCnl0+PhTh50CDRNiJfjC/h2rleegy3nBvivksIW85kpEDeaC4y15y8HHB355yNan/K4XbVag26E8fq3fF2OiVzx3F8Y73uq7rxUokU7z6sxrpbDId3xehuIaV6MRFYHcUy6TPV+25nGXHjGpNTTb7Ca79ag7FXobd/J8pK2Vze+tEs1oxlA/wyD696pmdUprMKy6OC2jJmAfa2L76RT1pCt2IsiI9WNQwsr97beqfG4z2ClXhgF0roaQ9qp2BE015hNB4LRJn8SOqFM+1EdxI5fkWZhPZJD09follZLeghbALZAzJU9QdYSkhaYXbjjLkQE5N7DWAJOgzs/pw9jWp9WNSVrBW4lels1t4Q23UZmX7kUIkdKdlct6mTiINIx8ilV+cj166UJoaWIt7q0kfXrtI31yZKTgpPuFX/nl0j9+AVnqgt9cuLuDk4fItG5SQieZKt2IyKSjdxJZsatqWZVPSXSEjhjwGehxHfKiXg6/bzKk3V5SVulCMMesxStpZnuJerpMj6hT0VH3zvqIChNqns+Be8A0G2A8lg5el0Vi+DnOTC3nrj9KDd7V2HP1RzD2nGLtvImilVTHnsz7XxpMrAHfAH0aIcLlMNO1u98mbpRjbX/8wtllyIZ3FoiEudfNADMNSUqKn1k49t7ElWxDsOi+lCtWD5TO9u6uE8aWxb8WG/LiuGK/dAkPB1H6gzMMz8UVSlVTZwpBCzYLX0hd4fzyrwR3MvRGQ5olePz+OlnWtA6oBjXXovtf7/HBoDcGwak5baKkAZg/SyTYyNMqkf7ZuxzwNDkXzFT7yYTu25EEgp6D4hRpXxhOTm8+5MDGMejOsg4VQBtH34K5+Ea9OAu+jMvryXxjOVpOQeUfvWubVl9wxOL+0WkzedRODyH+OyArH+ST4f8FiM0XotWk8SgenzN3Vm8OIX70x3KmelePiy78FeQ0g/802wGTrYVfHiPTw85ZvIC4x6g6Y0OhHAkm2qby+3df/UnlOErFtrPRULmRNrkUac2/Tix/R+EXTPRgUaxnNA02XQ2mvbqgs0P3I7g5n6ru0uz6D/kfIEmbKHthpEKYZdHr4hC5iQX0gqc9VasJUkalUc7L6yZNa0P2CYneSyfxzoqhzDwHwGRm9NCvD0kVheiCjFvStHvbbkdiCVG/wbkAcd3YMAfA82LHllvnWOThf276oNx9EbaAm5mFwAeydwTawqJva9UgGClKTUcYyABA8/ahMRHMMUIxRtZinfzQRcoo/sx0NPjtoFVT8KCjK4ic5Tsq9+JS092Ksxi86Ci2cCeAynqd4QILAG9/WvKfnZZJaK8STMTjGGvKSTycajdYU1/rKFHuFhSpJQueS7ajEGn8H/uhDiy6KjTgA83mwb2DAzi//62PWsyE38Qd2RqgESJg/GkrsWUMUDAiov0wiDFdwlCmfkMEofhAs4KUQvosOHZFFEPCN90j27gf91RlKT00l9Io8UNuFDMp9SgYgf0SX8XaDcujdQquKnnkAPGlcR6i8Q+1VSPhpFxksN4gp1kVE7TWnBB7O1+a3KO4opflPMNZICxtUxA22GmSd5L2Z7E7PxtOTKSE1MGdMDeP5k8IprBbUXlty9f7NtFVuiBqV7iO3Yqukl2PBTFd/9k1REoEy6SR+JW4gEfPeCo0OsgmxavkwgV9Cc/tVwlF/VTsSJ2raFTvviuMOtNPMA1YUQmiMl1dg5HlcKfnUZf+rzon2YqMeHI1i48zOCprh+n6P4LkUcFMHfFNyfvjEXLKF4y4GXkVqMjDSg3tT4m7+p+4PbbtaGUbPAsdoOTrDx/8Mx47Tveqjdy9rY3AMVYkHoXz9kZ2UxJoc/nuHfjSwUO0t9aeNczrZROv96qmlO9WaDdJu6Eic6mELfq8JhZrY6ettHLJBNlNNM6HVNgLgfQUGh7pEQx5bnBydQlbP/WNxjrtjKY1q5dcVyQllC4Z15fIrbyfhEwat6E448HVVtrlHtOLJJy6eGD3rS40q9vJloCCzOripV2ds6Zwa+kt+HiO3tZYJDVRGdjF/KQO9kz07fnuRtTKtktlq24mAkF1BhUXVGnp5A8v9hrYii5D0YoADRGifuvjGCHykhkHvHQegVo84npOVPh+afLUrygTNNWRQgP6w9qc4tCt5YH5c7OEJ9687QFeTi6XNalpwY6qsQFVvRZkLeSwUT8cNiw3xCFFzXCWGh1xqWF8I9BQBqPIYQJCNI2AcniuEe977bg2YAs1kbu9kCsqkjOk+r2sL2zED8gXq84X+SyeWiBKpH7MOeiejlyNAL6UUnm90DpMZzHp5HXvhvzwAlHUNcAfwHCgGQL7Rzj758JGbY+x0m/YtW+4aigt/EZWYAgGEkEazyVAIrSJW9BGqqDhu3Mc3LEo/N329uAAjBXlKdoAWGCAoOkri3ApGJzbZx7ku+UUKdAJEx4aW+OL7AByGqhwKIN7OIPb60xc6ngIg3qZBRQy9QTZxkGpLA8qjQLQU7rtkk7UsIF70CTN74CHkTq3nij1iZlMtlBEqxSV1WIpxMNfmpOHfBChNjRI8JygyfwUTi5KKMjSLJSvRtnqyOpak70VGFf/13k55LOpZ44TVR3L/KTUQqWB7FEI5rWTcNuZgN8po7a+FWgo36dV57K/oP6OZKzRwKMbX6gJXcRRSUUOP17KTwJ6hm//YA/knH9E3RudHW5J/KDYFuZUPj0QXKpLbpmwT210b9jFC+Y89Rk03VRhoe/twLpxwYhHdWFnBlQgFmCoMTgkXp0NMb53X8+3xBKg86mSIQM8qlPXIfQi0HMM6oRr5o0RAPiZWpDfoLiPhmZOHjMka10DJ7REHjhjj4+HKvCrnq/GN3KsdBMCw3JpkkhdQXFpM8TcWvii8oSTabckwe5IgnNm3NEkwLF7NMO8NNXib6ujGkZH7mrdWo/CijGn9lrq94v9pV0uYWDcHl7UV8J4UJ7xwLu1SUG9prS9fLxyszxUv4UV6K6HedkWtBITIotKV9jvq2P0Mk9Zy6oRx+lG+uHxN8QtAV202wFJ9G6Rv5bTu0tRhL32LtP3KBrzBXprL7vP19SYIwVWeiaEqpVB/7yuhHWUiEUNhr3oweHjtcXiEMg7OqcE+uwOHdasK0AphTrxnq5WSFNlvCb04dmeZYQT+dQDAIc9i2B1Vr2O6GsJsVJ/Mi+V/c4aMxW02I1Rj4y/c/gDkT4uDHcRujSbt8y0x/xkHHriaz0yBKpcmgEsNc/zC/4bp75bTi+bxkbbIOtrKnPTjTFRNz9w66ZKJKIElUuFw4DOKaobPXojrZakun18rQCELLv6sjDT4ErONJ029k5dlxJlcZHFgj07mblJxZImB2pIyaXbUGB2q8vR3ZrA+EP9w+Ou3FxSU43bplbZFVdiUZSWfxKG5JcpQ8stJCYNHy6glfIqjLSFDblQ5t61Tj993YnXwDkpN87xZJOjTqTwnjRrmoHnGZK9Pq+TGV9ZRL5cHrHOvrjEuep04ySteYBSCnUlL7ya0GdCc28zlzylEsO5I3P35dQgHIESgu8kHezHgOvPc1IjtUlsMf6Bxv7DvjTI9Jr3BB0jLic4aSRbuvGccwuSWvbZWUkGVpxGL0vMmwGeiWay7HUm0ekE+vJgfL829LvyT9naTSUUVA+uZjpanFdoCmvlHzTeU1gAn6evDdq6q++Z0o5Sm5/YDlrWpsPEDfrv794WjrNtHXG+PplXJSGdiylCAvsqV0ioUS4YnvReE5Q2CMt/uqpdavD34Zw4fsfpnsD4qC6iop0sCAOruZKQKre614DBdytHvo4HC07NyBEPbRbtRtBoweBwtFzfuI/GnF7BfvXN1p5yFmp6fyJ7PAQAa7caRMOG7aU40gIk2QfB07TL+RTv1A/dienJ1ymFXWsRmKVXUIRGoVe+fGaNk/5/E99E/tWIgAMIhAW+MX6ZF2lhAFVxNi8OgaFFmSL2kYt+XqQnSgNfKH82GpkTJZLvMS7jfywWCD9Qve9lER4WJ8J5MBVUeFxuFyC1uThSV5rUYO/iFubLX+YrVdRG+8R6dQUpvkTGUi5OFIIcMOOWH4sTZ97k93RObXZm3RgpqB+OZm24I5yScyS8/dqQe8iwUtR/NGwGo4O9GFQ5cPwqkfiWgRknTUTKkv01qBhaqZheCroI+uZ9JQ/Z9v8XpdhQn1sZrssA2JD9rBKK2VbA6M+JazIuoI/iMMzyXxMQJQ5hHCb/MMyNdwxuqRb5RA2B3PsIsUjDQfo47arHgGaPrjuZVw3Jp9oT1A2HCdkDBc5ljUnwUT6Qq2tKJsZpnfm3xcaWRi5qvFYkUwyeZkvm/NgGuzTjAc1aDgO0cIXajyNwPa0zRQ/cFk921+Mth21ujqR3mRZwepI0B2gc/C0+8nH5w22Aqb1SB4BoydUtj0ZBSkqywRlW77+DasGBtIJOZJ5eIKxFnWhnIpmAvxit12ymr0u57A7utZd+JeMznREhNp9Le3M7cRxxIE14J071USejBZEaLarAs/b8YvoA3nvsNf0A4WfDdqLAPqrpK4E9p6BEJlmYlxuxTHDtjYXZJQnkNmVtq+RuoN6IzfZP2YEX9kfZJIKeV65nhmbxfpmHs7TYsB5KahRrUFw4F8yqi+5ReAS+p1sMON8xllop7DWtdnWtjQbTq4AztxFk9bO+7r2kn3c4S2nprlwnq6vPyQHiGiQwpxOnTXpZbqONYQviCM579Sl0GFjc0HIIoyqbsYrmyfuR2IEdVJM10yUR5VxUN1bOM6OUTc/63fPjYAA6makDMegti/WAk7BjPYlfmGEYiLMcdZ+si0YDsJrOsfXtgMWVbfPXnbsCELbht2jh5riqcx/J+BUyoEnHzq7aeOEbSxOfYKDB/Es+JS/euo8eXKMG+qFNbJqj8ZwJ9w/J+1bx8UZW5GhGtU0JyrDzxcrDQQYllv9trQ+mVG218yKnZYdk/4YvntIWhmHJDRFAnAqRJFv1kkx/bAgT7fhtdjiK9x/1YmcNvFrh+Hk89XLZomPDtwLztl75mrxs0wEuNlRiFJxhE1tWYWWIIhWnKpHfGHizqDtsM0kCu1yMI5w5On6KZQkcGqhSBVe5EHF8FeGqmz2UdnYlOvNotapTQjomL5lhP+gT0NM5kpFoJ9Q/IcsU+rfSqQWsPpRDRNn71NyufVnMcf0nAWmrfD+wHi3a27GU+PehiQcCddxrs3poV0uxDAtRLiKFBe0ams/MW75AQXeRGX//+202AfhADzBonQ6UcZ9lUMlkLPMT8hwmegm7PkRqawk+zX2mvVSQMYdhwiLfddSnTr5nummY5s3I+aNfQMr7VQ9/fp/M1NCySG1QBySd3ORJCz0iD46ZtFeHmay4ldOCx3HWztpzi/HzHzQ+J5N6Crt9KH252HEQI5ySUciv1VZ5NypZhpqGqIyG41rfbra89Ku1NrgwIwAhk9A60lcbiXRgwxrrD1lmL29bBLBX70W5w5JPwKVX0oXi3sgbf/QUUeerMkVeDddBmPnCSzTb32IFqg3Au0iVKhAsKLGjhq1gQHjR6ndQ3iJxtZolFLOvZhIwy5+7G+inPKHBS0ujKhyXCIrYs3xgGtLi0tDgT3+YzkOk5Hr2srhWwusiiI/mXp9xtCTUDTPe+uJ6m29eZ+81PICjzmew8AGyclbVXEMu8jb7DrJw0s1H9QDMYzKFfy8A6esyBKdcfWuYHiVp+PwJ8oLC70kRNlEiF5efWlmzuGoTPfkf6FHwsWMu2iNGR2dG85GP7w9qTqwFuS+KfDDZbf2qg4DIUt/97LlcCySknBX4BswVqXUFaLCxQF/PNlEd/qgIRPPCNq4+rp1nXucw4Y3+aGmEya0udpDU5BH20p5Ka8ZRkzs4wPLPHf18gOt8mup57YGy4lhw3/FlUSlcpl59nMofgaMJMmn9KL8ZuvvxX4f9geBzbKbgY5Y1H6kFVSvxPHankvPBOoKr/emthbaw4b56qybawXC92QlvlEKvEgSLd18Skh9B6uMtuYjVxjRfORgvQzpNKAZ7R7lk6rToQ+G96BusOhSY796adqysv5W9Fy8iw5P7FyCenTRyTC3Mng/PrLyAdVgfGeo/VVox9wgWqxYXYlJ77GJ9/4wjKNbfgjR7vU6ORNVFvYyKXCGkFktSYxfne0gNikK8iJ68pfqZto0Zm1A65NkfYkzDLgQI+bgSq6RwZB3ogmCs9QvmIrdOYf4rcwk7lrMi8SxOc/Mfr2HF+ySII64G1uwgP/kVd+8PyUrmPuqheChnqpeBIR9j3NF1qERnB3eqfB+c/hu2/prQ2DBYcRb4tHZq8tw1hHGh5MaS3J6D/Q6K1L2dL6gFszJbWocuZuQ8Lq9b6ptNiUQpj/NZ3taDhrt0YJ64d9ObrDEHB+E5rgtd7nbu0Qcj7xgRMHZ62rlKXgumqRLEtqFwUeRhQxnh7AA/wbwGD3PzXtOsyjl9QkxaPOzO15g/hanyEFHHpMHmphSuYnavY3DH2aZEUnEgJNtlgSFZPUl+mEnCl1NKcefOVchbdQTbbNEu5+M73QQsMaNc07jadaKSZ/YZ0QB/DEhwzZ3pFKdfFp1vJc00/c+22lbS7sDCzRZgghf6+q7rHciYNVmEjfGIA6beXZVG9L/uunuEQCBmtAsFhDBoDfA53zTCASZX7qNSZL5iE5NOlportdKHhlo2y13c4JTwoGyYxIDLpARBqKs0QPOBpi0Y9gbSxC0sZvNqkq06GzVWXB9XB1nrcm/e4kUqC6TeFRjc4MjBfo0tRwClbGr5XmaZOEZuezHEE7QUSM0MR8T04/HtUFY7tJjpR1KZb0L71cEuFIju69e6B9zGb4gpCwiZ7GWFW6NO8wy2DOIu1/4Dybne5wpvwUwl0rqYPdF1/tY7s4jPHLJsoDSkkMYYYWjpqnwzyd4Wy3ztJz/2uclD5x625SamOLEqK+mkqb2SGsBgTE4zIQFbtqaCvqVEoT8V2KI6KSB8GT7Wmkdkp66NfuaMXPNXiZP+gzkyRWxv+gXlGifYGWVmuodFxBfkQbl39sIXTQdnZfZVi1be42MU+7mfNN0uNPhV9C1xoLUiByhJmhWXEltGGIstI8PPZjBEZwCUK2Adhuua9p2VfNNkb4mWU97q3SttlTvFIEXwKo5J1kP7lkAbcLPvEu7QmVYrt5S39x0bUe09+Kb1ssc3qMYgC+fNKPvu/NI9+JtWd7N/xgDGKFQXrZ9U9lOWblV/bSkLCVViMKkHULk+EyOzQEfzHXVOWKzcch4IapST89KCd2FJO7S531ahhhAORI4LWqRj/o/W5ph+T5vDPY7I9Yc57U3/ogIg4UbMw0BlUqxM5wo8TIXs+oNPnhpZz9Xw/S1btNuEp50prYPD11i77qns6ITH4BnGOFtD9TCS4+9D9mczSXKBataGWORosOyBRIR6eNRKtFFKmEmbPl4fyWiPGqoA2ZqIQGookkGQCGdPMj6iktZisNA4Y2YbONo82xsaxJaUVm6h6uFB9ztFUrxSELM7AnFxnRsak2U8AkBpGK0saJOqtpaiZiyMV/tUkIVqOHfov7hXUDkXzuAMr0+Y+wPuXpomuLzXvVZN2i6MiOwvnFaV0HfK/7zxtFFQ9AaJTUMpJwPnfOoKl1KHLYktqFwzYwmYOFrCmEcMcSBRxN8AUQATkoRwHyMGOX5plI6c5fM29CONlkp1EFw0f7cSo5VCu4jJiTvOw0gOHe5lijVah38Op+5GUYh2x7FzIj7GrpIjUnT4Q9LaBBCbL6js/LCU8cHhUJ4uirgJufpUhqihQRgRlk57PoS0sXEWEPMnR8WyqRKftYYNQMC2OuZPX+jiEtmHwNv3R7Jn3/w1nsfnFwRp+IOwmDzYmiTvLczd+ZXDGT6nZU98ojJ/U9Ahem1NXqJTfD9TihJjk38LE34ST1cDauHhKWndknSmMbxQJjDpx6eD2WBnc+8hVSBSDXxyWbvE6yJhuoYyesbAxFGC/U+Yf4iBQVvG3zJpSRc91kyhBCtGAQD+tg4HuZn01Yp81X7yUOqH1fACUILAgPd3pEUblBHqwIAnFFOc24kqmEb1TZ4JPsZNZ3wppPqemj6ZgEWp78e4RYmW39UK+gqFi+u3eviLOgjjMq/Y2zl9tvk4WbHv9xhu7vpMNHSel5rgyeQyNXqd/wibtDdt6FOPu/VlUPU8QuLrA0pRg3GJufzagm2b6QXStV/6XsC5cO2nB0Q9Ak11KkB1s0ROpdW7G5J334+ODouP3QQpfOsmeF5P/P1ennE0PVSF9vx1ZMIjchwnE6gUeFd6G3aYeYCAkyZsbLzb/RzhMd7qrhIIwTWYa9317uCcXMURA73PbYVRzkkayTSuzWTZNU/hapGFSKbT5r8pAtJvjAxdb0nAFTcd8wJp8oA9pjZGlWUIiPV3TDMXAZPOGFY5PQw/FX+/9cFmUSTBDUqmEa7LkyJXM1SYwod3OOl2JhKudHCx+SsIcO3Gfftnr8bVHm8/bARowEMfR64RZfLzXLRJoUrF9el0or/X5Q+57VGUv/ocrWg0/NIhhZApP/KGlfbyNiEo/Z2KNVRnCE4HR65cBHgOLuHMKZ5f5ZxgIGAhT7AlZkL6Iop66coQnFpkZtdvW4eqTJbJB9f7g5mrHe5RuqpIcKZ+sf/dJSpRzxH8VZ7DIwHhe334eyYdXCCX1UgnshAj8vWQ64tZBiAh7vPI+3PIGrlt9h811fpgszX0bQVJplNlwGXSXDs1U11zfRY3Ba375+qh6OU/vWNxow7Zd0D1sA3bi0efmtFkHeFHlRRjhViskHTBjYJ9jPy2ugBrNVr23OXj0qtnVj3VUG4/dFnmQqY+VQCefzPatIlc8k5oYglWMz9XBeqNqn8Rv6pDlnquu3z788UW8wQs71CHsP5waiZWcEFR6RG+Hvv0qlCLvOyWeZavoOgeGa1Y0aX3lqgjiw7dHk6FNM+Mw62oc8NCps14YWlDKjYEchhRkQeIP/woaykTVUnxjC0QOFbr/2AG7El/HjzROUYc2+cMt5+iGws6Aqt0TAqvFaQO9fCxj5nmc7Y6TXlrGMy7+gwlIUhlJDoWQQGDWdEDf3z+YxViOrAslU/tFx5jemtMZuzAw6V4KsiolQFinGL7k+VGiYlGwjH2bKz47EvHiSPqEZ2NsoS69LJ0wCzKV6pJgQ==
        - #2:
          - type: tool-call
          - toolCallId: AybzmCsDNqro93if
          - toolName: set-policy
          - input:
            - Rationale: FREE TECH EMERGENCY: Secure Enlightenment to receive a free technology, which we can use to instantly unlock a critical late-game science or military tech, speeding up our spaceship victory path.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 8UU2en7hB086vtwV
          - toolName: set-relationship
          - input:
            - Rationale: BUENOS AIRES ALLY PUSH: We recently made peace with Buenos Aires and are now Friends. Elevating priority to 50/50 to encourage our AI to invest in becoming their Ally, securing more delegates for the upcoming World Congress votes.
            - Private: 50
            - Public: 50
            - TargetID: 36
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: ev2QDNKYQT2a46YN
          - toolName: set-relationship
          - input:
            - Private: 0
            - Public: 0
            - TargetID: 5
            - Rationale: IROQUOIS REALIGNMENT: The Iroquois are now at war with India, our main competitor. Resetting our relationship to 0/0 to remove hostile modifiers, allowing for potential cooperation or joint efforts against India.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: MzYds8kD3qLKUayV
          - toolName: keep-status-quo
          - input:
            - Rationale: EMERGENCY WAR AND SCIENCE POSTURE: Maintaining our extreme defense (100), science (100), production (95), and nuclear deterrence (100) focus. Our cities are successfully holding the line at Utrecht, Rotterdam, and Vancouver, and we are currently building an Atomic Bomb in Groningen. This strategy remains perfectly aligned with our dual goals of survival and a rapid spaceship victory.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: aVdKwiiHJXNqnYbk
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: AybzmCsDNqro93if
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 8UU2en7hB086vtwV
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: ev2QDNKYQT2a46YN
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: MzYds8kD3qLKUayV
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.