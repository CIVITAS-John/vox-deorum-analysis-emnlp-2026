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
      - toolName: set-relationship
      - args:
        - TargetID: 0
        - Private: 0
        - Public: 0
        - Rationale: HUNS RELATIONSHIP RESET: They are a capitulated vassal of Morocco, with whom we are at war. Our active war status means positive relationship modifiers are obsolete and could cause tactical pathfinding errors. Resetting to neutral 0/0.
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 0
        - Public: 0
        - Rationale: IROQUOIS RELATIONSHIP RESET: Data reveals the Iroquois are actively at war with India (our main cultural rival). Antagonizing them with negative modifiers is counterproductive as they serve as a critical military distraction for India. Resetting to 0/0 neutral.
    - #2:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: APOLLO PROGRAM RACE: Computers is 3 turns from completion. Satellites must be researched next to unlock the Apollo Program and start building spaceship components. This is our only viable path to victory.
    - #3:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: FREE TECH ACCELERATION: Locking in Enlightenment as our next policy. The free technology is essential to instantly grab a high-cost late-game science or military technology, giving us a major advantage in the spaceship race.
    - #4:
      - toolName: keep-status-quo
      - rationale: STRATEGIC STABILITY: Our defense is holding across multiple fronts, a nuclear weapon is being produced in Groningen, and our science output is maximized. Maintaining the current high-level flavors and Spaceship Grand Strategy to avoid disrupting the staff's tactical queues.
  - tokens:
    - inputTokens: 70904
    - reasoningTokens: 6698
    - outputTokens: 333
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Progress**
            
            My focus is on India's overwhelming cultural advantage. I'm assessing how to counter their dominance and if any other victory paths remain feasible given the current turn and era.
            
            **Assessing Immediate Actions**
            
            I'm re-evaluating our engagement with India. Despite their strong cultural position, I'm questioning why a declaration of war hasn't materialized yet. It seems the system only registers denouncement, not an immediate hostile action, and I need to confirm tactical execution.
            
            **Investigating Diplomatic Nuances**
            
            I'm delving into why our direct conflict hasn't escalated despite India's clear cultural dominance. It appears their victory hinges on completing a specific wonder, and they haven't yet achieved that final objective. This provides a crucial, albeit narrow, window for action.
            
            **Evaluating India's Position**
            
            I'm analyzing India's overwhelming cultural influence, noting they've affected seven major civilizations. They've also secured two Tier 3 Order tenets. Their current scientific progress, specifically the nearing completion of the Citizen Earth Protocol wonder, is a significant concern. My attention is now on whether I can interrupt this wonder and if a science victory is still within reach.
            
            **Analyzing Current Threat**
            
            I am assessing the immediate threat from India's cultural dominance and their nearing victory. My current focus is on understanding the precise mechanics that prevent direct conflict escalation and exploring potential disruptions to their wonder completion to salvage a science victory.
            
            **Analyzing Combat Status**
            
            I'm reviewing the dire situation in Vancouver, where enemy armor and infantry are pressing hard, though our defenses are holding for now. Meanwhile, naval engagements near Rotterdam show promise, with a recent successful sinking of a Polynesian Battleship. My focus is on reinforcing Vancouver and continuing to disrupt enemy sea lanes.
            
            **Researching Policy Options**
            
            My current thought process is focused on selecting the most advantageous policy to adopt next. I'm weighing the benefits of `Enlightenment` to accelerate technology acquisition against potentially higher-tier policies within the Freedom ideology, specifically `Space Procurements`, which offers significant advantages for a science victory. I need to verify if `Space Procurements` is accessible given our current tenet count.
            
            **Prioritizing Policy Adoption**
            
            I'm confirming our access to a Tier 3 tenet and considering the immense benefits of `Space Procurements` for our science victory goal. Given our current gold reserves and GPT, immediate purchases are unlikely, but the science boost is critical. `Enlightenment` remains our selected next policy for its immediate technological advantage, and this aligns with our overall sprint for a science victory.
            
            **Adjusting Strategic Priorities**
            
            I'm re-evaluating our resource management given the trade route plunder and negative gold GPT. While science and production remain paramount for our victory condition, I'm considering if a slight boost to gold is necessary to avoid bankruptcy within the next ~15 turns.
            
            **Rebuilding Trade Networks**
            
            I'm realizing we have numerous available trade routes due to past losses and have neglected rebuilding caravans. This impacts our economy negatively. I need to prioritize building trade units, even without policy changes. Our current policy setup with Progress and Liberty branches requires careful consideration, especially regarding `Fraternity`, `Organization`, and `Equality` tenets. I'm analyzing the best next research target, questioning if `Satellites` is optimal after `Computers`.
            
            **Researching Critical Techs**
            
            My current focus is securing `Satellites` as our next research objective. This tech is crucial for unlocking the Apollo Program, which is essential for a science victory. I've confirmed that `Computers` is only three turns away, and after that, `Satellites` will be the immediate pursuit. I'm also considering calling `set-research` to ensure this priority is maintained.
            
            **Confirming Policy Adoption**
            
            I am now confirming the adoption of the `Enlightenment` policy. The potential for a free technology is a significant boon in this late stage of the game, potentially shaving off crucial research turns and bringing us closer to our science victory.
            
            **Reviewing Diplomatic Ties**
            
            I'm re-examining our diplomatic landscape. Kyiv remains a steadfast ally, and I'm ensuring our relationship with them is protected. My attention is also drawn to Buenos Aires; I'm trying to understand the sudden shift to friendship after our peace on turn 402 and the subsequent interactions involving Venice.
            
            **Analyzing Diplomatic Relationships**
            
            I am reviewing the diplomatic landscape, specifically concerning city-states. I'm noting my reset of Buenos Aires due to an expired quest and the subsequent shift to friendship with them, despite their strong alliance with India. Heidabir and Mombasa's relationships are also under scrutiny, particularly India's significant influence with them.
            
            **Investigating Declarations**
            
            I'm trying to understand why we haven't declared war on India yet. It seems the system only registers denouncements, and direct declarations aren't an immediate option. I need to confirm if we can actively initiate hostilities to prevent their impending cultural victory, as their wonders are close to completion.
            
            **Assessing Other Civs**
            
            I'm reviewing my relationships with other major civilizations, noting ongoing wars with the Shoshone, Morocco, and Polynesia. I'm confirming our automatic war status with The Huns as Morocco's vassal and questioning why our relationship with them was set to 85/85. Venice remains at peace for now, with our relationship appropriately set.
            
            **Resetting Hun Relationship**
            
            I need to reset my relationship with The Huns to 0/0 as they are a vassal of our enemy and currently at war with us. I'm also investigating the Iroquois; they are at war with India, contrary to previous assumptions about their allegiance.
            
            **Identifying New Allies**
            
            I've discovered a critical development: the Iroquois are at war with India! This changes everything for their cultural victory, as they are now a natural ally. I need to understand why I previously denounced them and adjust our stance immediately to leverage this unexpected partnership.
            
            **Leveraging New Alliance**
            
            I'm focusing on the Iroquois now that I know they are at war with India. My priority is to improve our relationship with them, shifting it from a denouncement to a neutral or friendly status. This alliance could be crucial in disrupting India's cultural victory, so I'm reviewing our past diplomatic actions and preparing to reset our standing with them.
            
            **Resetting Hun Alliance**
            
            I'm focused on aligning our interactions with the Iroquois, recognizing their conflict with India as a critical pivot. My immediate goal is to shift our relationship from denouncement to a more favorable standing, preparing to leverage this unexpected alliance to counter India's cultural dominance.
            
            **Prioritizing Defensive Policies**
            
            I'm reinforcing our defenses given the ongoing four-front war, focusing on anti-air and ranged unit production. With an atomic bomb nearing completion, I'm prioritizing its strategic deployment and ensuring our cities can withstand incoming attacks.
            
            **Maintaining Strategic Focus**
            
            My current assessment confirms the existing strategic framework remains highly effective. The cohesive flavor set is bolstering our defense and driving progress towards our science and atomic bomb objectives. Therefore, I am choosing to maintain the status quo, avoiding any disruptive adjustments to our current optimized queues.
            
            **Analyzing Unit Deployment**
            
            I'm evaluating our espionage efforts. With nine spies actively gathering intelligence and stealing technology in enemy capitals, I believe we're effectively closing the scientific gap. I'm also reviewing our trade capacity; though our GPT is negative, the current setup should automatically rebuild our trade routes.
            
            **Confirming Trade Capacity**
            
            I'm reassessing our trade routes and negative GPT. While the numbers appear concerning, the `Mobilization` and `Production` policies should enable the AI to automatically construct caravans when production slots are free. Therefore, I'm confident in the current setup's ability to address our trade needs.
            
            **Resetting Diplomatic Ties**
            
            I'm resetting my relationship with The Huns to neutral, as they're a vassal of Morocco and we're at war. I'm also setting The Iroquois to neutral, as they're now at war with India and represent a valuable potential ally. My research will focus on `Satellites` to advance our science victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: QebrfX9hZTc91j93
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Private: 0
            - Public: 0
            - Rationale: HUNS RELATIONSHIP RESET: They are a capitulated vassal of Morocco, with whom we are at war. Our active war status means positive relationship modifiers are obsolete and could cause tactical pathfinding errors. Resetting to neutral 0/0.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: APhlhqMh3gmChIYs
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 0
            - Public: 0
            - Rationale: IROQUOIS RELATIONSHIP RESET: Data reveals the Iroquois are actively at war with India (our main cultural rival). Antagonizing them with negative modifiers is counterproductive as they serve as a critical military distraction for India. Resetting to 0/0 neutral.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: EaBFJ4K4liqm9Su9
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: APOLLO PROGRAM RACE: Computers is 3 turns from completion. Satellites must be researched next to unlock the Apollo Program and start building spaceship components. This is our only viable path to victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: idgNaWdxo1R2vwcV
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: FREE TECH ACCELERATION: Locking in Enlightenment as our next policy. The free technology is essential to instantly grab a high-cost late-game science or military technology, giving us a major advantage in the spaceship race.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: POfBnJDCKJnpZoQf
          - toolName: keep-status-quo
          - input:
            - Rationale: STRATEGIC STABILITY: Our defense is holding across multiple fronts, a nuclear weapon is being produced in Groningen, and our science output is maximized. Maintaining the current high-level flavors and Spaceship Grand Strategy to avoid disrupting the staff's tactical queues.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: QebrfX9hZTc91j93
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: APhlhqMh3gmChIYs
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: EaBFJ4K4liqm9Su9
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: idgNaWdxo1R2vwcV
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: POfBnJDCKJnpZoQf
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.