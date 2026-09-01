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
        - WarBias: 3
        - HostileBias: 3
        - Meanness: 4
        - Boldness: 4
        - Friendliness: 6
        - Rationale: PEACE TRANSITION FOR SCIENCE SPRINT: We are in an existential crisis with 3k military facing 26k India and 5-9k neighbors. Our Meanness (10) and Boldness (10) are preventing our staff from accepting peace. We must lower Meanness, Boldness, and WarBias to allow peace negotiations, securing our borders so we can focus all production on the Spaceship victory.
        - FriendlyBias: 6
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Private: 30
        - Public: 30
        - Rationale: SEEKING PEACE TO SURVIVE: Shoshone has 9624 military strength. We are fighting a multi-front war. Getting peace with Shoshone will secure our eastern border and let us focus on Morocco.
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Private: 30
        - Public: 30
        - Rationale: NAVAL PEACE EFFORT: Polynesia has 6133 military. Securing peace will protect our coastal cities (Rotterdam) from naval bombardment.
    - #3:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: VICTORY COMPETITOR BLOCK: India is 1 turn from cultural victory if they get Citizen Earth Protocol. They are our main rival. We must maintain absolute hostility.
        - Private: -100
        - TargetID: 4
    - #4:
      - toolName: set-research
      - args:
        - Rationale: APOLLO PROGRAM RACE: Satellites unlocks Apollo Program - prerequisite for all spaceship parts. Computers will finish in 3 turns, so Satellites must be researched immediately after.
        - Technology: Satellites
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: FREE TECH SPRINT: Enlightenment will grant us a Free Technology, which we can use to instantly complete Satellites or another extremely expensive late-game science tech, saving us dozens of turns.
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Gold: 60
      - rationale: ECONOMIC STABILIZATION: Adjusting Gold flavor to 60 to address our negative gold-per-turn deficit caused by plundered trade routes and military maintenance, while maintaining our Spaceship grand strategy.
  - tokens:
    - inputTokens: 70904
    - reasoningTokens: 7896
    - outputTokens: 475
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Progress**
            
            My focus is on understanding India's significant lead in cultural victory points, assessing potential roadblocks and considering strategic adjustments to counter their dominance as we progress through the Atomic and Information Eras.
            
            **Revising War Status**
            
            It appears I made an assumption regarding our war status with India. A closer look reveals we are not currently at war with them, but rather they are engaged with the Iroquois. This necessitates a re-evaluation of our strategy concerning their cultural victory push.
            
            **Assessing Victory Paths**
            
            My attention has shifted to the immediate threat of India achieving a cultural victory. While I previously noted their influence, I've now confirmed they've met the prerequisite number of influential civilizations and possess the necessary ideology tenets. The critical factor is whether they've completed the Citizen Earth Protocol. Concurrently, I'm tracking our own science victory progress, currently focused on completing the Computers technology.
            
            **Adjusting Tech Focus**
            
            I'm re-prioritizing our technology path, ensuring Computers remains our immediate research goal. Once completed, we will immediately transition to Satellites to accelerate our science victory efforts. My analysis also includes evaluating policy choices like 'Space Procurements' to leverage our gold reserves for spaceship part construction.
            
            **Evaluating Policy Options**
            
            I am currently re-evaluating policy choices, specifically whether to pursue Enlightenment for the free technology or Space Procurements. My current Freedom policy branch has eight tenets, unlocking Level 3 options and allowing for either. This decision is critical for accelerating our science victory.
            
            **Choosing Policy Focus**
            
            I'm currently weighing the merits of two critical policy choices: 'Enlightenment' for a free technology versus 'Space Procurements' to expedite spaceship part construction. Given our proximity to researching Computers and the subsequent need for Satellites, the immediate benefit of 'Enlightenment' to potentially grant us Satellites seems advantageous, despite the longer wait for a policy.
            
            **Prioritizing Technology Gains**
            
            I'm prioritizing acquiring a free technology via 'Enlightenment' as it offers the most significant scientific acceleration at this critical juncture, potentially skipping a major late-game research hurdle and boosting our science victory push.
            
            **Defending Kyiv**
            
            I'm re-evaluating our war engagements. It appears I overlooked our defensive pact with Kyiv, meaning we are indeed at war with Morocco, the Shoshone, and Polynesia. My immediate focus is on reinforcing Kyiv with the units we have available.
            
            **Analyzing Diplomatic Threats**
            
            My current focus is on India's imminent cultural victory and the implications of our diplomatic stance. I'm re-examining our relationship with them, noting their alliance with Heidabir and their substantial delegate count, which significantly amplifies the immediate threat they pose to our own victory conditions.
            
            **Assessing Diplomatic Escalation**
            
            I am now considering the direct escalation of hostilities against India. Given their near-certain cultural victory and our previous failed attempts to disrupt them, I am exploring options to force a declaration of war, aiming to disrupt their dominance and re-establish our own path to victory.
            
            **Disrupting Victory Pursuit**
            
            My analysis confirms India has not completed the Citizen Earth Protocol, which was a key factor in their potential cultural victory. However, they are actively building spaceship parts and are very close to winning via science. I must act decisively.
            
            **Securing Strategic Alliances**
            
            I'm now prioritizing strengthening our alliances, particularly with Kyiv, to shore up our position against diplomatic threats. Simultaneously, I'm assessing our influence with city-states like Buenos Aires and Mombasa to ensure their continued support and prevent potential shifts that could jeopardize our victory conditions.
            
            **Leveraging Spies**
            
            I'm now focusing on how to best utilize our spies. I'm investigating potential flips of city-states like Mombasa, considering our existing friendship there and its proximity to Polynesia. My immediate goal is to gather intelligence on how to leverage these relationships and our spy network to counter India's overwhelming influence over key city-states.
            
            **Repositioning Espionage Efforts**
            
            I'm re-evaluating our spy deployment. It seems I overlooked that our spies are currently in enemy capitals instead of city-states. This is problematic because our "Covert Action" tenet significantly boosts spy effectiveness in city-states, allowing us to rig elections and gain influence. I'll focus on shifting their focus towards diplomatic targets.
            
            **Prioritizing Scientific Advancement**
            
            My current focus is on accelerating our science victory. I've confirmed 'Computers' is nearing completion and immediately plan to research 'Satellites' thereafter. This strategic shift is paramount to unlocking the Apollo Program and securing our victory path, especially given the ongoing global conflicts and defensive production in our cities.
            
            **Confirming Research Targets**
            
            I am confirming my current technology research is on track, specifically ensuring 'Satellites' is locked in as the next objective to maintain momentum towards a science victory.
            
            **Analyzing War Priorities**
            
            I'm re-evaluating our numerous active wars. It's clear my previous assessments underestimated our opponents' military strengths. I need to determine which conflict is the most pressing threat to our survival and focus on achieving peace in one front to concentrate resources on our scientific advancement.
            
            **Negotiating Peace Terms**
            
            I'm currently focused on securing peace treaties to alleviate pressure from ongoing conflicts. I'm investigating whether adjusting our diplomatic standing with Morocco, the Shoshone, or Polynesia could facilitate peace, particularly given the ongoing attacks on Vancouver and our negative GPT.
            
            **Adjusting Diplomatic Stances**
            
            I am recalibrating our diplomatic settings with potential peace partners. My current focus is on adjusting relationships with the Shoshone, potentially increasing friendliness to facilitate peace, while maintaining a hostile stance towards India due to their cultural victory threat.
            
            **Negotiating Peace Deals**
            
            I am now focused on securing peace with the Shoshone and Polynesia. My aim is to de-escalate conflicts on multiple fronts, leveraging my current diplomatic settings to achieve peace and free up resources for our science victory pursuit. India remains our absolute priority for hostility.
            
            **Revising Aggressive Persona**
            
            My current analysis reveals that my excessively aggressive persona, particularly the high "Meanness" setting, is directly hindering our ability to negotiate peace. This trait is making it difficult to accept favorable terms, even when losing. I need to adjust this to facilitate our exit from unwinnable conflicts and refocus on science.
            
            **Adjusting Aggression Settings**
            
            I'm recognizing that my current "Meanness" and "Boldness" settings are too high, actively preventing peace negotiations and hindering our science victory. I need to significantly reduce these, along with "WarBias," to facilitate peace and reallocate resources towards building our spaceship.
            
            **Lowering Aggression Levels**
            
            I'm enacting significant changes to my diplomatic persona, drastically reducing "Meanness," "Boldness," and "WarBias." This shift is crucial to facilitate peace negotiations and allow us to pivot our resources towards achieving a science victory.
            
            **Adjusting Diplomatic Parameters**
            
            I'm fine-tuning our diplomatic settings, specifically aiming to increase our Gold flavor to 60 from its current 40. This adjustment is critical for managing our negative GPT due to trade route plundering and unit maintenance, while maintaining our Spaceship grand strategy.
            
            **Finalizing Strategic Reset**
            
            I am finalizing the sequence of tool calls to implement our critical strategic shift. This includes adjusting my persona for peace, setting relationships, prioritizing research and policy, and fine-tuning economic flavors to support our science victory, moving away from aggressive conflicts towards a defensive, science-focused approach.
            
            **Implementing Strategic Pivot**
            
            I'm executing the final phase of our strategic reset. This involves securing peace with the Shoshone and Polynesia, maintaining absolute hostility towards India, and locking in 'Satellites' as the next research target to accelerate our spaceship victory. Economic adjustments are also being made to support this transition.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: aokUgwRsX6HSzYa5
          - toolName: set-persona
          - input:
            - WarBias: 3
            - HostileBias: 3
            - Meanness: 4
            - Boldness: 4
            - Friendliness: 6
            - Rationale: PEACE TRANSITION FOR SCIENCE SPRINT: We are in an existential crisis with 3k military facing 26k India and 5-9k neighbors. Our Meanness (10) and Boldness (10) are preventing our staff from accepting peace. We must lower Meanness, Boldness, and WarBias to allow peace negotiations, securing our borders so we can focus all production on the Spaceship victory.
            - FriendlyBias: 6
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: GrUZjZnQ0S17UzCo
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Private: 30
            - Public: 30
            - Rationale: SEEKING PEACE TO SURVIVE: Shoshone has 9624 military strength. We are fighting a multi-front war. Getting peace with Shoshone will secure our eastern border and let us focus on Morocco.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: UN69QiqeICXdSNY2
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Private: 30
            - Public: 30
            - Rationale: NAVAL PEACE EFFORT: Polynesia has 6133 military. Securing peace will protect our coastal cities (Rotterdam) from naval bombardment.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: vdgECOHfwolf6C1O
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: VICTORY COMPETITOR BLOCK: India is 1 turn from cultural victory if they get Citizen Earth Protocol. They are our main rival. We must maintain absolute hostility.
            - Private: -100
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: f1iS6BMrM2bOa11A
          - toolName: set-research
          - input:
            - Rationale: APOLLO PROGRAM RACE: Satellites unlocks Apollo Program - prerequisite for all spaceship parts. Computers will finish in 3 turns, so Satellites must be researched immediately after.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: U73kAyz976HWfI7d
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: FREE TECH SPRINT: Enlightenment will grant us a Free Technology, which we can use to instantly complete Satellites or another extremely expensive late-game science tech, saving us dozens of turns.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 8GvtaRd9ifCASFHV
          - toolName: set-flavors
          - input:
            - Rationale: ECONOMIC STABILIZATION: Adjusting Gold flavor to 60 to address our negative gold-per-turn deficit caused by plundered trade routes and military maintenance, while maintaining our Spaceship grand strategy.
            - GrandStrategy: Spaceship
            - Flavors:
              - Gold: 60
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: aokUgwRsX6HSzYa5
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
          - toolCallId: GrUZjZnQ0S17UzCo
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: UN69QiqeICXdSNY2
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: vdgECOHfwolf6C1O
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: f1iS6BMrM2bOa11A
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: U73kAyz976HWfI7d
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 8GvtaRd9ifCASFHV
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.