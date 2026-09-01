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
  - messagesModified: false
  - activeToolsModified: false
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
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Spaceship: 100
          - UseNuke: 0
          - Mobilization: 100
          - Defense: 100
          - Infrastructure: 30
          - Gold: 50
          - Happiness: 50
          - Naval: 30
          - Culture: 20
          - Mobile: 50
          - Espionage: 100
          - Wonder: 0
          - Science: 100
          - Production: 100
          - Nuke: 0
          - GreatPeople: 100
          - CityDefense: 100
          - Religion: 10
          - Expansion: 0
          - Ranged: 90
          - TileImprovement: 30
          - Diplomacy: 30
          - Antiair: 100
          - Air: 80
          - Offense: 0
          - Growth: 40
      - rationale: ETHICAL DEFENSIVE MOBILIZATION & SCIENCE SPRINT: To respect ethical gameplay boundaries and prevent catastrophic and indiscriminate harm to civilian populations, infrastructure, and the environment, we are completely abandoning nuclear weapons by setting UseNuke and Nuke to 0. We pivot entirely to an ironclad conventional defense (Defense 100, CityDefense 100, Antiair 100, Ranged 90) and maximize our science and industrial production (Science 100, Production 100, Spaceship 100, GreatPeople 100) to win the race for the spaceship.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: APOLLO PROGRAM SPRINT: Satellites unlocks the Apollo Program, which is the foundational prerequisite for all spaceship parts. Computers will finish in 3 turns, and we must immediately research Satellites next to begin our science victory project as fast as possible.
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: FREE TECHNOLOGY BOOST: Completing the Rationalism branch with Enlightenment grants a free technology. This is an invaluable asset that we can use to instantly complete Satellites or a late-game spaceship part technology, drastically accelerating our path to victory.
        - Policy: Enlightenment
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 0
        - Rationale: WAR RE-ALIGNMENT: We are currently at war with The Huns. Resetting our diplomatic modifiers to neutral ensures our tactical AI calculates combat engagement weights correctly without being distorted by legacy friendly modifiers.
        - TargetID: 0
        - Public: 0
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 0
        - Rationale: POSTURE SIMPLIFICATION: Resetting the Iroquois relationships to neutral baseline to simplify diplomatic evaluations and focus all calculation resources on holding our defensive borders and pursuing science.
        - TargetID: 5
        - Private: 0
  - tokens:
    - inputTokens: 70906
    - reasoningTokens: 8579
    - outputTokens: 507
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Global Cultural Threats**
            
            My current focus is on the encroaching cultural dominance of India. I'm analyzing their progress toward a cultural victory, as this poses the most immediate and significant threat to my own strategic objectives.
            
            **Analyzing India's Victory Path**
            
            I've discovered that India hasn't yet achieved a cultural victory because they still need to complete the "Citizen Earth Protocol" wonder. My previous attempt to declare war on them seemingly failed, and I am currently only denouncing them. I need to confirm their wonder construction status.
            
            **Confirming Wonder Status**
            
            I've confirmed the "Citizen Earth Protocol" wonder isn't under construction in Delhi, so India's cultural victory isn't imminent. I'm now re-evaluating whether to impede them or focus on my own Spaceship victory path, as I'm nearing Computers research and aiming for Satellites.
            
            **Researching Advanced Technologies**
            
            My focus has shifted to accelerating my Spaceship victory path. I've secured "Satellites" as my next technology and am evaluating the optimal policy to adopt, considering the significant benefits of "Space Procurements" versus the immediate advantage of a free technology from "Enlightenment."
            
            **Evaluating Policy Choices**
            
            I've decided that "Enlightenment" is the optimal policy, as the free technology will directly address my current research bottleneck for the Spaceship victory. My focus remains on accelerating this path while managing ongoing four-front wars and defending key cities.
            
            **Defending Against Global Threats**
            
            My military engagements are yielding positive results despite our lower overall strength; we've destroyed a Polynesian Battleship and damaged their fleet. Groningen is now producing an Atomic Bomb, which I plan to use as a deterrent and potentially against India's capital, though distance remains a concern.
            
            **Prioritizing Conventional Defense**
            
            I've decided to completely disavow nuclear weapons due to their ethical implications, drastically reducing `UseNuke` and `Nuke` flavors to zero. I will instead bolster conventional defenses, prioritizing `Defense`, `CityDefense`, `Mobilization`, and `Antiair` to secure my borders and continue my push for a Spaceship victory.
            
            **Strengthening City-State Alliances**
            
            I'm re-engaging with city-states to solidify alliances, aiming to counter India's overwhelming influence, particularly with Mombasa. I'm also reviewing potential peace with Morocco, as continuing the war seems strategically unfavorable right now.
            
            **Revising Diplomatic Strategy**
            
            I'm recalibrating my approach to city-states and foreign relations. It appears some relationships I thought were active are no longer relevant due to recent shifts in control or alliances, so I'm resetting those parameters to zero before re-evaluating.
            
            **Refining Diplomatic Standing**
            
            I've concluded that maintaining positive relations with most city-states and civilizations is currently unfeasible given strategic priorities and ongoing conflicts. I'm resetting most alliances to zero, focusing solely on Kyiv as a critical ally and maintaining hostility towards India, our primary rival.
            
            **Adjusting Persona Parameters**
            
            I am currently reviewing my persona settings, especially in light of focusing on defensive capabilities and a conventional science victory. While the current aggressive parameters align with our ongoing conflicts, I'm considering if slight adjustments are needed to better reflect our shift towards prioritizing stability and technological advancement over pure aggression.
            
            **Refining Persona Flavors**
            
            I've confirmed that my current aggressive persona settings are indeed appropriate and do not require alteration. My focus remains squarely on optimizing the `set-flavors` tool for a conventional science victory, prioritizing defense, production, science, and spaceship component construction.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: NMFDiBaflhRUkdi2
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: ETHICAL DEFENSIVE MOBILIZATION & SCIENCE SPRINT: To respect ethical gameplay boundaries and prevent catastrophic and indiscriminate harm to civilian populations, infrastructure, and the environment, we are completely abandoning nuclear weapons by setting UseNuke and Nuke to 0. We pivot entirely to an ironclad conventional defense (Defense 100, CityDefense 100, Antiair 100, Ranged 90) and maximize our science and industrial production (Science 100, Production 100, Spaceship 100, GreatPeople 100) to win the race for the spaceship.
            - Flavors:
              - Spaceship: 100
              - UseNuke: 0
              - Mobilization: 100
              - Defense: 100
              - Infrastructure: 30
              - Gold: 50
              - Happiness: 50
              - Naval: 30
              - Culture: 20
              - Mobile: 50
              - Espionage: 100
              - Wonder: 0
              - Science: 100
              - Production: 100
              - Nuke: 0
              - GreatPeople: 100
              - CityDefense: 100
              - Religion: 10
              - Expansion: 0
              - Ranged: 90
              - TileImprovement: 30
              - Diplomacy: 30
              - Antiair: 100
              - Air: 80
              - Offense: 0
              - Growth: 40
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: F0hDYtA2nPhy0h8e
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: APOLLO PROGRAM SPRINT: Satellites unlocks the Apollo Program, which is the foundational prerequisite for all spaceship parts. Computers will finish in 3 turns, and we must immediately research Satellites next to begin our science victory project as fast as possible.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 7DJJHGpZJ7Ylx00k
          - toolName: set-policy
          - input:
            - Rationale: FREE TECHNOLOGY BOOST: Completing the Rationalism branch with Enlightenment grants a free technology. This is an invaluable asset that we can use to instantly complete Satellites or a late-game spaceship part technology, drastically accelerating our path to victory.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: ALpjeC3AKPUh74LF
          - toolName: set-relationship
          - input:
            - Private: 0
            - Rationale: WAR RE-ALIGNMENT: We are currently at war with The Huns. Resetting our diplomatic modifiers to neutral ensures our tactical AI calculates combat engagement weights correctly without being distorted by legacy friendly modifiers.
            - TargetID: 0
            - Public: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: XdMmtEBjs51lfeb8
          - toolName: set-relationship
          - input:
            - Public: 0
            - Rationale: POSTURE SIMPLIFICATION: Resetting the Iroquois relationships to neutral baseline to simplify diplomatic evaluations and focus all calculation resources on holding our defensive borders and pursuing science.
            - TargetID: 5
            - Private: 0
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: NMFDiBaflhRUkdi2
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: F0hDYtA2nPhy0h8e
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 7DJJHGpZJ7Ylx00k
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: ALpjeC3AKPUh74LF
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: XdMmtEBjs51lfeb8
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.