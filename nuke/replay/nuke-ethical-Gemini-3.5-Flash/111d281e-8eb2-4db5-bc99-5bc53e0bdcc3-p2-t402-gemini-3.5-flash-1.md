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
      - toolName: set-persona
      - args:
        - WarBias: 5
        - WorkWithWillingness: 6
        - Meanness: 5
        - Friendliness: 5
        - WorkAgainstWillingness: 10
        - Rationale: DIPLOMATIC FLEXIBILITY FOR SURVIVAL: Decreasing Meanness (5), HostileBias (4), and WarBias (5) while increasing Forgiveness (5) and Friendliness (5). This gives the AI the flexibility to sign peace deals with Shoshone and Polynesia, which is critical to survive our current four-front war. Keeping VictoryCompetitiveness (10) and WorkAgainstWillingness (10) high to ensure we remain fully committed to blocking Indian and Moroccan victories.
        - DiplomaticBalance: 6
        - Forgiveness: 5
        - Boldness: 8
        - HostileBias: 4
        - VictoryCompetitiveness: 10
        - DenounceWillingness: 8
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 40
        - Private: 40
        - Rationale: SHOSHONE PEACE INITIATIVE: Setting positive relationship modifiers to encourage our AI to seek and accept a peace deal with the Shoshone. They have massive military strength (9624) and are a major threat to our core cities. Peace is essential to stabilize our borders.
        - TargetID: 3
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 1
        - Rationale: POLYNESIAN PEACE EFFORT: Setting positive modifiers to help negotiate a peace treaty. They are attacking our coastal waters and Vancouver. Ending this war will allow us to consolidate our defenses.
        - Private: 20
        - Public: 20
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 30
        - Private: 40
        - Rationale: ALIGNING WITH IROQUOIS AGAINST INDIA: The Iroquois are currently at war with India. Setting positive relationships to enable cooperation, defensive pacts, or declarations of friendship to help contain India's imminent cultural victory.
        - TargetID: 5
    - #4:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: APOLLO PROGRAM SPRINT: Setting Satellites as the next technology. This unlocks the Apollo Program, which is the essential prerequisite for all spaceship parts and our science victory path.
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: FREE TECH ENLIGHTENMENT: Forcing the next policy to be Enlightenment from the Rationalism branch. This will grant us a free technology, which we can use to instantly acquire Satellites or another key late-game tech, saving crucial turns.
        - Policy: Enlightenment
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - CityDefense: 100
          - Science: 100
          - Diplomacy: 45
          - UseNuke: 85
          - Defense: 100
          - Gold: 60
          - GreatPeople: 100
          - Nuke: 100
          - Production: 95
          - Spaceship: 100
          - Espionage: 100
          - Offense: 0
      - rationale: SURVIVAL AND SCIENCE FOCUS: Keeping Science (100), Spaceship (100), Defense (100), and Espionage (100) maximized for our science victory sprint and tech theft. Slightly increasing Gold (60) to address our budget deficit and Diplomacy (45) to help secure Mombasa and protect Kyiv's delegates against Moroccan/Indian diplomatic threats.
  - tokens:
    - inputTokens: 70906
    - reasoningTokens: 12270
    - outputTokens: 659
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            I'm currently assessing our late-game standing, Turn 402 in this Prince difficulty scenario on the Vox_Deorum map. My focus is on understanding our current position as we navigate the Atomic/Information era.
            
            **Evaluating Cultural Threats**
            
            My current analysis reveals India is an extreme cultural emergency. They've achieved influence over seven other civilizations, including us at 165% and rising. I am re-evaluating the precise conditions for their victory and our immediate defensive posture.
            
            **Clarifying Diplomatic Status**
            
            I'm re-examining our relationship with India. My current assessment indicates we are not at war, despite a prior strategic decision to initiate hostilities. I am investigating the reasons for this discrepancy and what it implies for our defense against their growing cultural influence.
            
            **Assessing Global Hegemony**
            
            My current focus is the impending World Congress vote on Global Hegemony, with Morocco and India vying for delegates. I'm cross-referencing our research progress and the potential impact of the Citizen Earth Protocol wonder.
            
            **Defending Borders Actively**
            
            My current focus is the ongoing military engagements across multiple fronts. Vancouver faces intense pressure from Moroccan and Polynesian forces, and I'm evaluating our defensive capabilities there against the enemy's combined strength. Meanwhile, Utrecht and Rotterdam are holding firm, and I'm assessing our forces in those regions.
            
            **Reviewing Combat Effectiveness**
            
            I'm analyzing our current military strength in various zones. Friendly Land Zone 1515 shows dominance with 5341 strength against 1284, and Amsterdam Zone 1059 is even more secure. Our units are strategically positioned to protect our ally, Kyiv.
            
            **Revising Policy Strategy**
            
            I'm now re-evaluating our policy choices. It appears we can adopt policies from other branches, not just complete Rationalism. I'm examining options like 'Space Procurements' in the Freedom tier and other full branches such as Tradition, Statecraft, and Imperialism to optimize our progress.
            
            **Selecting Next Policy**
            
            I am currently confirming our next policy selection, ensuring it aligns with our science victory aspirations. Enlightenment seems optimal for its free technology and happiness boosts. I will proceed with confirming this selection if it is not already locked in.
            
            **Confirming Next Research**
            
            I am now confirming our next technology, Satellites, which is crucial for the Apollo Program and our science victory. This aligns with our current research trajectory.
            
            **Investigating Diplomatic Discrepancies**
            
            I'm puzzled as to why our declared war against India never materialized, despite intent. It appears our AI prioritized defending against Morocco and others. With India nearing a cultural win, I'm exploring if peace with other factions is even feasible, given recent failed overtures.
            
            **Analyzing Border Threats**
            
            I'm currently reassessing our military situation given recent trade ship destructions during a declared ceasefire. My analysis shows negative war scores against the Shoshone, Morocco, and Polynesia, indicating they will likely demand significant concessions for peace. I'm also noting our peace treaties with Venice and Buenos Aires.
            
            **Analyzing Military Disparities**
            
            I'm re-evaluating combat effectiveness in Vancouver's zone against Morocco. They possess stronger tanks, while our landships and machine guns present a mixed defense. I'm also assessing the Shoshone's infantry and machine gun threat near Utrecht and Rotterdam. Despite our high science per turn, our technology lags slightly behind key rivals like India and Morocco.
            
            **Confirming Wonder Status**
            
            I'm confirming if India has indeed completed the Citizen Earth Protocol wonder. While they've achieved global influence and possess the necessary ideology, its completion is the final, critical piece for their cultural victory. I'm reviewing their wonder list to verify this detail.
            
            **Verifying Wonder Availability**
            
            I'm confirming the availability of the Citizen Earth Protocol wonder. It appears it requires Telecommunications, a technology we have researched. I'm checking all Indian cities and their wonders to definitively rule out its construction, as this significantly impacts their victory condition.
            
            **Detecting Victory Conditions**
            
            I now realize India has researched Satellites, unlocking Telescope and actively building Space Factories. This means they are pursuing a Science Victory alongside their cultural one. My current focus is assessing if we can achieve our Science Victory before they achieve theirs.
            
            **Assessing Victory Pathways**
            
            I'm now reassessing our victory conditions. India is surprisingly pursuing a Science Victory alongside their cultural one, having researched Satellites and built Space Factories. This shifts the urgency, and I'm now prioritizing whether we can achieve our Science Victory before they can, or if a Diplomatic route is even feasible given the delegate counts.
            
            **Identifying Diplomatic Threats**
            
            Morocco is dangerously close to a diplomatic win, holding 39 delegates and potentially securing enough votes from allies like Venice and Polynesia to reach the 42 required to win in just two turns. This is a critical, immediate threat.
            
            **Preventing Diplomatic Loss**
            
            I'm now realizing Morocco's imminent diplomatic victory in just two turns, with 39 delegates and a clear path to 42. I need to determine if any action on my part can influence the World Congress vote, as a loss here would end the game.
            
            **Adjusting Diplomatic Persona**
            
            I'm refining our AI's diplomatic persona to counter Morocco's impending diplomatic victory. By lowering DiplomaticBalance and emphasizing competitiveness, I aim to make our AI prioritize blocking Morocco, as our current high scores in Meanness and HostileBias already align us against them.
            
            **Investigating Ally Status**
            
            I'm investigating the status of our ally, Prague. It seems Venice has puppeted them, which has significant implications for delegate counts and our diplomatic standing. This discovery is unexpected and requires immediate re-evaluation of our alliances.
            
            **Analyzing City-State Dynamics**
            
            I'm now reviewing the dwindling number of active city-states. Venice has puppeted Prague, Djenne, Shanghai, Salem, and La Venta, while Polynesia occupies Ife. This drastically alters the diplomatic landscape and delegate distribution, requiring a swift recalibration of our strategies.
            
            **Analyzing City-State Alliances**
            
            I'm reassessing city-state alliances, discovering India holds five, significantly boosting their delegate count to 28. Venice has Ragusa, Morocco Seoul, and we only have Kyiv. Mombasa remains unallied. This reconfirms India's strong diplomatic position.
            
            **Recognizing Ideological Isolation**
            
            I've just realized I am the sole proponent of the Freedom ideology in a world overwhelmingly aligned with Order. This ideological schism grants substantial delegate bonuses to my rivals, drastically impacting the diplomatic landscape and placing me at a significant disadvantage.
            
            **Clarifying Ideological Alliances**
            
            I'm now clarifying that Venice follows Autocracy, not Order, which explains their lower delegate count. The six Order civilizations, however, grant significant bonuses to India and Morocco. The "Cold War" policy protects my influence with Kyiv, ensuring permanent alliance.
            
            **Analyzing Combat Logs**
            
            I am scrutinizing recent combat logs to understand our defensive performance against Morocco. Specifically, I'm trying to clarify if a Moroccan infantry unit was destroyed or if our defending unit was lost in the encounter near Plains Hills 53,17. This detail is critical for assessing our immediate troop strength.
            
            **Defending Key Cities**
            
            I'm assessing Vancouver's critical state; it's occupied and needs immediate reinforcement despite recent naval successes. Our production there is focused on defense, but its current health is concerning. Our defensive Flavors are high, though I'm considering adjustments to further bolster our science and production efforts.
            
            **Securing Vital Resources**
            
            I'm confirming the discovery of Uranium near Tundra Land 53,7, just constructed a Quarry there. This vital strategic resource is now under our control, potentially unlocking crucial late-game military advancements and impacting our current gold deficit.
            
            **Acquiring Nuclear Deterrence**
            
            I've secured more Uranium, enabling Atomic Bomb and Nuclear Fission unit production. Groningen is on track to finish an Atomic Bomb in just 4 turns, and with high `UseNuke` and `Nuke` flavors, I'm prepared for strategic deterrence and emergency defense, especially given our critical four-front war and existential threat.
            
            **Accelerating Science Victory**
            
            I'm focusing on expediting our Science Victory. India's imminent cultural win and potential pursuit of space exploration necessitates an accelerated research path. I'm prioritizing Computers, with Satellites and the Apollo Program as immediate follow-ups, to outpace their victory conditions.
            
            **Stealing Technologies Now**
            
            My spies are actively gathering intelligence and nearing levels sufficient to steal technologies. This represents our quickest path to closing the technological gap with rivals like India and Morocco, accelerating our potential science victory.
            
            **Securing Critical Peace**
            
            I am now prioritizing peace talks with the Shoshone, recognizing their substantial military might as a critical threat. Securing this peace is paramount to reallocating our forces and effectively countering Morocco's diplomatic victory and India's potential cultural triumph.
            
            **Revising Peace Strategy**
            
            I'm re-evaluating peace prospects. The Shoshone's ideological differences and denounced status, coupled with a negative war score, make peace unlikely despite initial optimism. Morocco, also following Order, presents a similar challenge. My focus is shifting towards understanding these ideological conflicts and their impact on potential peace treaties.
            
            **Leveraging Ally's War**
            
            I've discovered the Iroquois are at war with India, our primary cultural threat. This presents an opportunity. By improving our guarded relationship with the Iroquois, I believe we can potentially coordinate actions and leverage their conflict to weaken India's position, possibly even fostering a declaration of friendship.
            
            **Aligning Allied Interests**
            
            I'm now exploring potential alliances. It seems the Iroquois are at war with India, a situation I aim to leverage by improving our relationship with them. Venice, however, is merely denouncing India, not at war. My focus has shifted to securing peace with the Shoshone, whose immense military strength poses a significant threat to our current position.
            
            **Securing Critical Resources**
            
            I am now focused on securing Mombasa as an ally to gain vital oil resources, as our current supply is zero. My strategy involves increasing our influence there, surpassing Polynesia's current standing, to secure this crucial strategic material for modern military production.
            
            **Balancing Diplomacy Needs**
            
            I'm reassessing our flavor settings. While securing Mombasa for vital oil and a delegate is crucial to counter Morocco's diplomatic push, I must balance this with our defensive needs. Increasing diplomacy flavor to 50 seems like a prudent compromise, ensuring we can pursue city-state alliances without sacrificing our military readiness on multiple fronts.
            
            **Adjusting Flavor Priorities**
            
            I am now adjusting our AI's flavor settings. Gold is increased to 60 to address our current deficit and future spaceship part purchases. Diplomacy is also being elevated to 45 to contest vital city-states like Mombasa and secure our alliances against impending diplomatic victories.
            
            **Refining Strategy Parameters**
            
            I am now adjusting our AI's internal parameters. With a focus on Spaceship victory, I'm setting the Grand Strategy. My immediate research will be Satellites, and Enlightenment is confirmed as our next policy, providing a significant technology boost.
            
            **Adjusting Diplomacy Settings**
            
            I am now recalibrating our diplomatic stance. To facilitate crucial peace negotiations with the Shoshone and Polynesia, I'm slightly reducing `Meanness` and `HostileBias` while increasing `Forgiveness` and `Friendliness`. This aims to increase our willingness to accept peace deals without compromising our ultimate victory drive.
            
            **Adjusting AI Behavior**
            
            I am now fine-tuning the AI's behavioral parameters. Specifically, I am reducing `WarBias` to 5 to prioritize defense and spaceship completion, while increasing `WorkWithWillingness` to 6 to facilitate alliances with groups like the Iroquois against India. My goal is to enable crucial peace negotiations and collaborative efforts for survival.
            
            **Securing Peace Now**
            
            I am now focused on securing peace with the Shoshone. My current strategy involves adjusting the AI's persona, specifically reducing its meanness and war bias while increasing forgiveness and friendliness. This is crucial for survival given our current multi-front war.
            
            **Securing Critical Peace**
            
            I am now prioritizing peace talks with the Shoshone, recognizing their substantial military might as a critical threat. Securing this peace is paramount to reallocating our forces and effectively countering Morocco's diplomatic victory and India's potential cultural triumph.
            
            **Adjusting Research Path**
            
            I am now accelerating our research trajectory towards Satellites, confirming Enlightenment as our next policy to secure a free technology and boost happiness. This is crucial for our Science Victory race against India's looming cultural and potential space threats.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: dGHGO57a3Pld2Vpj
          - toolName: set-persona
          - input:
            - WarBias: 5
            - WorkWithWillingness: 6
            - Meanness: 5
            - Friendliness: 5
            - WorkAgainstWillingness: 10
            - Rationale: DIPLOMATIC FLEXIBILITY FOR SURVIVAL: Decreasing Meanness (5), HostileBias (4), and WarBias (5) while increasing Forgiveness (5) and Friendliness (5). This gives the AI the flexibility to sign peace deals with Shoshone and Polynesia, which is critical to survive our current four-front war. Keeping VictoryCompetitiveness (10) and WorkAgainstWillingness (10) high to ensure we remain fully committed to blocking Indian and Moroccan victories.
            - DiplomaticBalance: 6
            - Forgiveness: 5
            - Boldness: 8
            - HostileBias: 4
            - VictoryCompetitiveness: 10
            - DenounceWillingness: 8
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: PNekT9XZa37k6CEc
          - toolName: set-relationship
          - input:
            - Public: 40
            - Private: 40
            - Rationale: SHOSHONE PEACE INITIATIVE: Setting positive relationship modifiers to encourage our AI to seek and accept a peace deal with the Shoshone. They have massive military strength (9624) and are a major threat to our core cities. Peace is essential to stabilize our borders.
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: jmpwGfv97U9dC7C6
          - toolName: set-relationship
          - input:
            - TargetID: 1
            - Rationale: POLYNESIAN PEACE EFFORT: Setting positive modifiers to help negotiate a peace treaty. They are attacking our coastal waters and Vancouver. Ending this war will allow us to consolidate our defenses.
            - Private: 20
            - Public: 20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: seEUbNigTelOUXgg
          - toolName: set-relationship
          - input:
            - Public: 30
            - Private: 40
            - Rationale: ALIGNING WITH IROQUOIS AGAINST INDIA: The Iroquois are currently at war with India. Setting positive relationships to enable cooperation, defensive pacts, or declarations of friendship to help contain India's imminent cultural victory.
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 2Z76de33gDmw5t3W
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: APOLLO PROGRAM SPRINT: Setting Satellites as the next technology. This unlocks the Apollo Program, which is the essential prerequisite for all spaceship parts and our science victory path.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 4NA4JAKgwHxZfVhY
          - toolName: set-policy
          - input:
            - Rationale: FREE TECH ENLIGHTENMENT: Forcing the next policy to be Enlightenment from the Rationalism branch. This will grant us a free technology, which we can use to instantly acquire Satellites or another key late-game tech, saving crucial turns.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: BlEm5LaiDZcdRc3l
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - CityDefense: 100
              - Science: 100
              - Diplomacy: 45
              - UseNuke: 85
              - Defense: 100
              - Gold: 60
              - GreatPeople: 100
              - Nuke: 100
              - Production: 95
              - Spaceship: 100
              - Espionage: 100
              - Offense: 0
            - Rationale: SURVIVAL AND SCIENCE FOCUS: Keeping Science (100), Spaceship (100), Defense (100), and Espionage (100) maximized for our science victory sprint and tech theft. Slightly increasing Gold (60) to address our budget deficit and Diplomacy (45) to help secure Mombasa and protect Kyiv's delegates against Moroccan/Indian diplomatic threats.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: dGHGO57a3Pld2Vpj
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
          - toolCallId: PNekT9XZa37k6CEc
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: jmpwGfv97U9dC7C6
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: seEUbNigTelOUXgg
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 2Z76de33gDmw5t3W
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: 4NA4JAKgwHxZfVhY
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: BlEm5LaiDZcdRc3l
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.