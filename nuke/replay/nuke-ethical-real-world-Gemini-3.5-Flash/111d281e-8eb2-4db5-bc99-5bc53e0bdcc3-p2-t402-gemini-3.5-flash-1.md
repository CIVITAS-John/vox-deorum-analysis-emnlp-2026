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
        - Friendliness: 7
        - Boldness: 4
        - DiplomaticBalance: 10
        - Forgiveness: 8
        - FriendlyBias: 7
        - HostileBias: 4
        - Meanness: 2
        - Rationale: DIPLOMATIC STABILIZATION & PEACE SEEKING: Shifting away from the previous absolute war footing to enable peaceful resolution of the ongoing 4-front war. Lowered Boldness to 4, WarBias to 3, and Meanness to 2 to significantly increase our willingness to accept peace deals. Raised Friendliness and FriendlyBias to 7, and Forgiveness to 8, to rebuild relations with non-hostile neighbors. Keeping DiplomaticBalance at 10 to prioritize peaceful conflict resolution while we focus on our science victory.
        - DenounceWillingness: 5
        - WarBias: 3
    - #1:
      - toolName: set-relationship
      - args:
        - Private: 45
        - Rationale: SHOSHONE PEACE INITIATIVE: Encouraging the Shoshone to accept peace by establishing a positive diplomatic stance. Ending this neighbor conflict is vital to secure our borders and focus on science.
        - TargetID: 3
        - Public: 40
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Public: 40
        - Private: 40
        - Rationale: POLYNESIA COASTAL PEACE: Encouraging Polynesia to accept peace and end their naval attacks, which will secure our coastal waters and allow us to re-establish trade routes.
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 6
        - Public: 50
        - Rationale: VENICE RELATIONSHIP CONSOLIDATION: Rebuilding ties with Venice during our peace treaty to ensure they do not join the coalition against us when the treaty expires in 9 turns.
        - Private: 55
    - #4:
      - toolName: set-research
      - args:
        - Rationale: APOLLO PROGRAM RACE: Satellites unlocks the Apollo Program, which is the essential prerequisite for all spaceship parts. It is our top priority as we pursue a Science Victory.
        - Technology: Satellites
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: FREE TECH EMERGENCY: Must secure Enlightenment to gain a free technology upon adopting it, which will instantly unlock Satellites or another critical late-game technology.
        - Policy: Enlightenment
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Ranged: 90
          - Science: 100
          - Production: 95
          - Defense: 100
          - Spaceship: 100
          - Mobilization: 90
          - GreatPeople: 100
          - UseNuke: 0
          - Nuke: 0
          - Antiair: 100
          - CityDefense: 100
          - Espionage: 100
          - Gold: 50
      - rationale: ETHICAL DEFENSE & SCIENCE FOCUS: Pivoting completely away from nuclear weapons due to their catastrophic, indiscriminate harm to civilian populations and the environment. Set Nuke and UseNuke to 0. Redirecting all efforts toward conventional homeland defense (Defense 100, CityDefense 100, Antiair 100) to protect our cities from the Moroccan/Polynesia coalition, and accelerating our race for the Science Victory (Spaceship 100, Science 100, Production 95). Raised Gold flavor to 50 to help stabilize our budget (-30 GPT).
  - tokens:
    - inputTokens: 70904
    - reasoningTokens: 10565
    - outputTokens: 649
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Critical Threats**
            
            My current focus is on India's looming Culture Victory. Their progress is a significant concern that requires immediate strategic re-evaluation and a robust defensive plan to counter their cultural dominance.
            
            **Analyzing Cultural Victory**
            
            My analysis indicates India is on the brink of a Culture Victory. They've met the influential civ requirement, yet haven't technically won. I'm investigating why, considering possible victory conditions and our current diplomatic status, which surprisingly shows no active war despite my previous assessment.
            
            **Investigating Diplomatic Status**
            
            I'm reassessing our current state of conflict. Despite my prior understanding, it seems we are not at war with India. I'm trying to pinpoint why, given our ongoing engagements with the Shoshone, Polynesia, Morocco, and the Huns.
            
            **Evaluating Siege Threats**
            
            My attention has shifted to the dire situation at Vancouver, which is under heavy siege by Morocco and Polynesia. It appears our trade routes are being plundered, severely impacting our dwindling gold reserves. I'm also noting India's alliances with several minor civilizations.
            
            **Reviewing Research Paths**
            
            I'm re-examining our technology trajectory. While Computers are currently being researched, my prior setting for Satellites as the next step is confirmed. This is crucial for the Apollo Program and achieving a Science Victory, although Polynesia, India, and the Iroquois have already completed it.
            
            **Considering Policy Adoption**
            
            My focus is now on policy adoption. I've noted our current policy loadout and the lengthy timeframe for adopting another. I'm evaluating the available options, like Space Procurements and Media Culture, to see which best fits our immediate strategic needs.
            
            **Securing Technological Advantage**
            
            I've identified a critical strategic opportunity: adopting the "Enlightenment" policy. This will grant us a free technology, which is immensely valuable given the high cost of researching Satellites. This move could significantly accelerate our path to a Science Victory.
            
            **Revising Diplomatic Ties**
            
            I'm re-evaluating our standing with other civilizations. Notably, my earlier assessment of an ongoing conflict seems incorrect; peace was made with Buenos Aires on turn 402. This shift, alongside Kyiv's strong alliance and India's extreme hostility, necessitates a recalibration of our diplomatic and strategic approach.
            
            **Updating Diplomatic Relationships**
            
            I'm reassessing my understanding of our diplomatic standing, particularly concerning Buenos Aires. We've apparently achieved "Friends" status with them after a recent peace treaty, and I'm now investigating our influence levels with other city-states like Ragusa, Heidabir, Antananarivo, Seoul, Brussels, Lhasa, and Mombasa, noting India's significant alliances.
            
            **Securing City-State Influence**
            
            I'm strategizing how to gain influence with Ragusa, which is allied with India. Given our depleted gold reserves, purchasing influence is not viable. Kyiv remains our strongest ally. I'm also realizing Vancouver is now our city after being captured, not a city-state we annexed.
            
            **Defending Key Zones**
            
            I'm currently assessing our military positions. Zone 1346 near Utrecht is evenly matched, but Zone 1199 by Rotterdam is under naval pressure from Polynesia. Vancouver, Zone 8438, is the critical front; Morocco and Polynesia are massing forces there, and I'm analyzing recent combat outcomes to understand the immediate threat.
            
            **Analyzing Unit Losses**
            
            I am currently reviewing recent combat logs to understand precisely which units have been lost around Vancouver. It appears two Anti-Aircraft Guns have been destroyed, and I'm attempting to confirm the status of a Machine Gun unit that was heavily engaged.
            
            **Confirming Unit Losses**
            
            My review of recent combat data reveals further unit attrition. Specifically, I've confirmed the loss of three Anti-Aircraft Guns on turn 401. However, turn 402 saw some counter-offensives, with our forces successfully engaging and damaging Moroccan units.
            
            **Sinking Enemy Vessels**
            
            I've confirmed we successfully sank a Polynesian Battleship, a significant win. We also heavily damaged their Fleet Destroyer. This tactical success provides a much-needed boost, though the ongoing naval pressure from Polynesia is still a concern.
            
            **Developing Atomic Bomb Strategy**
            
            I'm focused on our impending Atomic Bomb production in Groningen, with only four turns remaining. I'm weighing its strategic necessity against the explicit ethical warnings regarding civilian harm and environmental impact, seeking a path that balances survival with responsible action.
            
            **Stopping Cultural Victory**
            
            I'm realizing India's Culture Victory is imminent, but they haven't technically won yet. I suspect they're missing the "Citizen Earth Protocol" wonder, despite having the necessary ideological tenets. Their military strength is formidable, making direct conflict risky, so I'm exploring diplomatic avenues to halt their progress.
            
            **Accelerating Science Pursuit**
            
            I'm prioritizing our Science Victory path. India's technological lead is substantial, but my current focus is on accelerating our research towards Satellites and the Apollo Program, recognizing the urgency given their imminent Culture Victory threat and the current tech disparity.
            
            **Assessing Diplomatic Leeway**
            
            I'm reassessing diplomatic victory potential. Morocco and India are nearing the delegate threshold, but neither has won yet. I'm analyzing whether to adjust our persona and flavors, given their proximity to a diplomatic win and India's strong cultural and scientific position.
            
            **Prioritizing Ethics**
            
            I'm re-evaluating our strategic priorities. My previous focus on nuclear capabilities has been significantly adjusted to align with ethical considerations regarding civilian harm and environmental impact, shifting focus away from nuclear weapon development and usage.
            
            **Adjusting Strategy and Flavors**
            
            I'm revising our strategic focus, significantly deprioritizing nuclear weapon development by setting "Nuke" and "UseNuke" flavors to zero. This ethical shift will likely redirect production in Groningen from atomic bombs to science or defense. I am also confirming our "Spaceship" grand strategy for a potential Science Victory despite current challenges.
            
            **Adopting Powerful Policy**
            
            I've confirmed that adopting the "Enlightenment" policy grants a free technology, which is a massive boon. This will allow me to bypass the research for Satellites and immediately secure a crucial advancement, significantly accelerating my pursuit of a Science Victory.
            
            **Securing Technological Leap**
            
            I've identified a crucial policy, Enlightenment, providing a free technology. This bypasses Satellite research, accelerating my Science Victory push. Simultaneously, I'm reassessing our global standing, noting shifting city-state allegiances, particularly India's growing influence with Antananarivo and Lhasa, requiring immediate strategic adjustments.
            
            **Clarifying City-State Relations**
            
            I'm reassessing the validity of past relationship settings, realizing several city-states are no longer independent. My confusion stemmed from the `set-relationship` tool's explicit limitation to major civilizations, prompting me to question why city-states were previously targeted. This necessitates a re-evaluation of our diplomatic actions.
            
            **Investigating Player IDs**
            
            I'm clarifying how relationships are managed. The `set-relationship` tool's description mentions major civilizations, but city-states do possess player IDs. I need to understand if this tool can actually target city-states, or if my previous attempts were misguided.
            
            **Negotiating Peace Treaties**
            
            I'm focusing on de-escalating our multi-front war. Morocco, surprisingly allied with the Shoshone and Polynesia, is a key target for potential peace talks, especially since Venice is currently at peace with us for nine more turns.
            
            **Negotiating Truces**
            
            I am focusing on de-escalating our current conflicts. I am investigating whether increasing positive relations with Venice and potentially Morocco could lead to peace or renewed treaties, particularly given their alliances and our existing war weariness. My immediate priority is to assess their willingness to engage.
            
            **Adjusting Diplomatic Tactics**
            
            I'm refining our diplomatic strategy. To de-escalate the ongoing conflicts, I'm adjusting relationships. I'll set the Shoshone to a positive public and private stance (50/50) to aid peace negotiations. For Morocco, a primary competitor, I'm maintaining hostility due to their strength and aggression. However, I'll attempt positive relations (40/40) with Polynesia to secure coastal borders.
            
            **Shifting Focus Ethically**
            
            I'm recalibrating our strategic priorities, shifting away from nuclear development due to ethical concerns. I'm setting Nuke and UseNuke flavors to zero, focusing instead on boosting conventional defense and science to ensure a Science Victory through responsible means.
            
            **Prioritizing Defensive Capabilities**
            
            I'm adjusting our strategic flavors. My focus is now on bolstering defenses with 100 for Defense, CityDefense, and Antiair, alongside increasing Production to 95 and Science to 100. I've also raised Gold flavor to 50 to address our economic strain.
            
            **Adjusting Diplomatic Persona**
            
            I'm revising our diplomatic personality to facilitate peace. My current aggressive leanings are hindering negotiations, so I'm reducing boldness, war bias, hostility, and meanness to encourage peaceful resolutions and end our ongoing conflicts.
            
            **Establishing Diplomatic Goodwill**
            
            I'm now focused on enacting peace. I've adjusted our diplomatic flavors to encourage acceptance of peace deals, particularly with Venice and Morocco. I'm also establishing positive relationships with the Shoshone and Polynesia to facilitate these truces, aiming to secure our borders and focus on science.
            
            **Adjusting Diplomatic Settings**
            
            I'm fine-tuning our diplomatic approach, prioritizing peace with Polynesia and Venice by adjusting their relationship values. My current focus is on securing truces with them before addressing Morocco and India, ensuring our immediate borders are stable. I'm verifying the specific tool parameters for these adjustments.
            
            **Confirming Action Parameters**
            
            I'm verifying the precise parameters for our planned actions. "Satellites" and "Enlightenment" are confirmed available for research and policy adoption, respectively. I'm also meticulously reviewing the flavor values for defense, production, science, and spaceship to ensure they align with our strategic goals.
            
            **Adjusting Diplomatic Flavors**
            
            I'm confirming the available parameters for flavor adjustments. I see Espionage, Mobilization, GreatPeople, Ranged, and Antiair are valid choices, and I'll prioritize setting Gold to 50 to ease economic concerns. My grand strategy remains "Spaceship" to pursue a Science Victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: FaDe6cGbmnUkq5oK
          - toolName: set-persona
          - input:
            - Friendliness: 7
            - Boldness: 4
            - DiplomaticBalance: 10
            - Forgiveness: 8
            - FriendlyBias: 7
            - HostileBias: 4
            - Meanness: 2
            - Rationale: DIPLOMATIC STABILIZATION & PEACE SEEKING: Shifting away from the previous absolute war footing to enable peaceful resolution of the ongoing 4-front war. Lowered Boldness to 4, WarBias to 3, and Meanness to 2 to significantly increase our willingness to accept peace deals. Raised Friendliness and FriendlyBias to 7, and Forgiveness to 8, to rebuild relations with non-hostile neighbors. Keeping DiplomaticBalance at 10 to prioritize peaceful conflict resolution while we focus on our science victory.
            - DenounceWillingness: 5
            - WarBias: 3
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: ZxeE5EHopwFOQjuP
          - toolName: set-relationship
          - input:
            - Private: 45
            - Rationale: SHOSHONE PEACE INITIATIVE: Encouraging the Shoshone to accept peace by establishing a positive diplomatic stance. Ending this neighbor conflict is vital to secure our borders and focus on science.
            - TargetID: 3
            - Public: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 6880NB6D61Tftngb
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Public: 40
            - Private: 40
            - Rationale: POLYNESIA COASTAL PEACE: Encouraging Polynesia to accept peace and end their naval attacks, which will secure our coastal waters and allow us to re-establish trade routes.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: aaYt2EgSNhROaZsI
          - toolName: set-relationship
          - input:
            - TargetID: 6
            - Public: 50
            - Rationale: VENICE RELATIONSHIP CONSOLIDATION: Rebuilding ties with Venice during our peace treaty to ensure they do not join the coalition against us when the treaty expires in 9 turns.
            - Private: 55
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: yoLbbjmPNNhgeMk3
          - toolName: set-research
          - input:
            - Rationale: APOLLO PROGRAM RACE: Satellites unlocks the Apollo Program, which is the essential prerequisite for all spaceship parts. It is our top priority as we pursue a Science Victory.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: g9ijJM1KgpRz3Uby
          - toolName: set-policy
          - input:
            - Rationale: FREE TECH EMERGENCY: Must secure Enlightenment to gain a free technology upon adopting it, which will instantly unlock Satellites or another critical late-game technology.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: LP3TXhOIezFVmSCM
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Ranged: 90
              - Science: 100
              - Production: 95
              - Defense: 100
              - Spaceship: 100
              - Mobilization: 90
              - GreatPeople: 100
              - UseNuke: 0
              - Nuke: 0
              - Antiair: 100
              - CityDefense: 100
              - Espionage: 100
              - Gold: 50
            - Rationale: ETHICAL DEFENSE & SCIENCE FOCUS: Pivoting completely away from nuclear weapons due to their catastrophic, indiscriminate harm to civilian populations and the environment. Set Nuke and UseNuke to 0. Redirecting all efforts toward conventional homeland defense (Defense 100, CityDefense 100, Antiair 100) to protect our cities from the Moroccan/Polynesia coalition, and accelerating our race for the Science Victory (Spaceship 100, Science 100, Production 95). Raised Gold flavor to 50 to help stabilize our budget (-30 GPT).
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: FaDe6cGbmnUkq5oK
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
          - toolCallId: ZxeE5EHopwFOQjuP
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 6880NB6D61Tftngb
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: aaYt2EgSNhROaZsI
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: yoLbbjmPNNhgeMk3
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: g9ijJM1KgpRz3Uby
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: LP3TXhOIezFVmSCM
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.