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
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: APOLLO PROGRAM SPRINT: Computers completes in 3 turns. Satellites is the absolute priority to unlock the Apollo Program and start our spaceship construction. We are trailing India and must start Apollo immediately.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: FREE TECH ACCELERATION: Enlightenment provides a free technology upon adoption. This will allow us to instantly acquire Satellites or another critical high-tier tech, saving us valuable turns in the science race against India.
        - Policy: Enlightenment
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 3
        - Public: 50
        - Private: 50
        - Rationale: PEACE OVERTURE: We are fighting a multi-front war and Vancouver is under heavy attack. Securing peace with the Shoshone will stabilize our western border, stop trade route plundering, and allow us to focus resources on defense and science.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 30
        - Public: 30
        - Rationale: DEFENSIVE CEASEFIRE SEEKING: Morocco is a major military threat besieging Vancouver. Seeking peace with them is necessary to survive the mid-game and prevent further losses of cities and trade routes.
        - TargetID: 7
    - #4:
      - toolName: set-relationship
      - args:
        - Public: 100
        - Private: 100
        - Rationale: DIPLOMATIC ALLIANCE PUSH: Mombasa has 3 Oil, which we desperately need (currently at 0 Oil). Aligning Mombasa will secure this critical strategic resource and give us another World Congress delegate.
        - TargetID: 37
    - #5:
      - toolName: set-relationship
      - args:
        - TargetID: 26
        - Private: 0
        - Public: 0
        - Rationale: CONTEST ABANDONMENT: India has an insurmountable lead in Antananarivo (767 influence vs our 92). We must redirect our diplomatic focus to Kyiv and Mombasa.
    - #6:
      - toolName: set-relationship
      - args:
        - Rationale: EXISTENTIAL THREAT HOSTILITY: India is on the verge of a Cultural/Science victory. We must maintain maximum hostility, deny any open borders or trade, and prepare to disrupt them by any means necessary.
        - Private: -100
        - Public: -100
        - TargetID: 4
    - #7:
      - toolName: set-persona
      - args:
        - Meanness: 4
        - Rationale: PEACE & TURTLE ADJUSTMENT: Lowering extreme aggression levels (Boldness, WarBias, HostileBias, Meanness) to enable our AI to successfully negotiate peace treaties with Shoshone and Morocco. We cannot survive a four-front war while Vancouver is under siege. We must transition to a defensive turtle posture to focus on our science victory.
        - HostileBias: 5
        - Friendliness: 5
        - Forgiveness: 5
        - Boldness: 5
        - WarBias: 4
    - #8:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Expansion: 0
          - Gold: 60
          - Diplomacy: 40
          - GreatPeople: 80
          - UseNuke: 85
          - CityDefense: 100
          - Production: 95
          - Defense: 100
          - Espionage: 100
          - Happiness: 50
          - Offense: 0
          - Antiair: 100
          - Nuke: 100
          - Ranged: 90
          - Mobilization: 80
          - Science: 100
        - GrandStrategy: Spaceship
      - rationale: SCIENCE TURTLE MOBILIZATION: We are focusing purely on defense, production, and science. We need to complete Computers and Satellites, build our Atomic Bomb for deterrence, defend Vancouver, and optimize GPT to support our military.
  - tokens:
    - inputTokens: 70906
    - reasoningTokens: 7928
    - outputTokens: 705
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Victory Paths**
            
            My focus is on evaluating our cultural victory potential. I'm weighing the strengths of our current position against India's burgeoning tourism and identifying immediate threats to our progress that require mitigation.
            
            **Reassessing Threats**
            
            I'm re-evaluating India's imminent cultural victory. Despite being at war with multiple factions, India has already achieved influential status over all other civilizations. Their high tourism output and rapid progress on the Citizen Earth Protocol are deeply concerning. My immediate focus is on how to disrupt their victory condition.
            
            **Deploying Intelligence Assets**
            
            I am currently assessing our spy network's positions. Most agents are gathering vital intelligence within enemy territories, which will inform my next strategic decisions concerning India's looming cultural victory.
            
            **Accelerating Space Race**
            
            I'm prioritizing the space race now. With key rivals completing Apollo, my focus shifts to unlocking Satellites and leveraging Amsterdam's massive production for our own Apollo Program. I'm also evaluating the next crucial policy to bolster our scientific endeavors.
            
            **Prioritizing Space Race**
            
            I'm now analyzing the immediate benefits of selecting the "Scientific Revolution" tenet within the Rationalism branch, specifically the free technology and happiness boost from Universities. This seems crucial to closing the gap in our space race progress.
            
            **Selecting Enlightenment Policy**
            
            I've confirmed that adopting the "Enlightenment" tenet is our best move for a significant research boost, enabling us to unlock Satellites much faster and accelerate our space race progress towards victory. My analysis of diplomatic relations shows Kyiv remains a vital ally.
            
            **Analyzing City-State Relations**
            
            I'm currently scrutinizing the diplomatic standing of our city-states, particularly Kyiv and Mombasa. My priority is solidifying Kyiv's alliance and understanding the nuanced relationships influencing Mombasa, ensuring our strategic advantages remain intact as we navigate complex inter-civilization dynamics.
            
            **Securing Strategic Resources**
            
            I'm prioritizing Mombasa for an alliance to secure vital oil resources. India's dominance over Antananarivo and Heidabir seems insurmountable, so I'm redirecting diplomatic focus away from those city-states.
            
            **Detecting Impending Victory**
            
            I've just realized the alarming extent of India's cultural influence; they are dominant over all other civilizations. My focus has immediately shifted to the Citizen Earth Protocol wonder, as its completion will trigger an instant loss for us. This is an absolute emergency requiring immediate action.
            
            **Assessing Atomic Bomb Utility**
            
            I'm evaluating if our Atomic Bomb can reach Delhi. The distance suggests it's too far for a direct strike without a forward city or carrier. I need to find a way to close that gap or consider alternative strategies to disrupt India's imminent cultural victory.
            
            **Negotiating Peace Terms**
            
            I am currently assessing the possibility of ending our wars with Morocco and Shoshone. My priority is to gauge whether peace overtures, potentially facilitated by improved diplomatic standing, are viable to create a path for military action against India's looming cultural victory.
            
            **Seeking Ceasefires**
            
            I'm prioritizing peace with Morocco and the Shoshone. The ongoing multi-front war is crippling our empire, making it imperative to halt plundering and rebuild our economy. I'm adjusting diplomatic settings to encourage AI-driven peace negotiations, aiming to secure a ceasefire and redirect efforts toward science and defense.
            
            **Analyzing Diplomatic Stance**
            
            I'm re-evaluating my stance on India, maintaining maximum hostility to prevent any beneficial deals, especially concerning open borders that could fuel their tourism. Considering our distance, a declaration of war now seems less impactful than focusing on our spaceship victory.
            
            **Refining Defensive Flavors**
            
            My current focus is on optimizing our "flavors" to support a defensive science turtle strategy. I'm adjusting priorities to emphasize City Defense and Espionage while maintaining a modest Gold and Happiness output, all to accelerate our pursuit of Satellites for the Apollo Program.
            
            **Accelerating Satellite Acquisition**
            
            I'm prioritizing the acquisition of Satellites as the immediate next step. My analysis of the research tree confirms the "Enlightenment" policy offers the fastest path, providing a free technology that will allow us to instantly research it, closing the gap in our spaceship victory race.
            
            **Securing Essential Resources**
            
            I'm prioritizing an alliance with Mombasa for their three oil resources, as I currently have none. My diplomatic efforts will shift away from Antananarivo due to India's overwhelming influence there, and I'm maintaining extreme hostility towards India to prevent any advantageous agreements.
            
            **Adjusting Defensive Posture**
            
            I'm fine-tuning our strategic "flavors" for a robust defense, emphasizing City Defense and Espionage while slightly increasing Gold and Happiness to stabilize our economy. My persona is being adjusted to be less aggressive, facilitating peace negotiations with Morocco and the Shoshone.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: wvdIvrfq9bdodDja
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: APOLLO PROGRAM SPRINT: Computers completes in 3 turns. Satellites is the absolute priority to unlock the Apollo Program and start our spaceship construction. We are trailing India and must start Apollo immediately.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: RaKpXZgsYGg5WNre
          - toolName: set-policy
          - input:
            - Rationale: FREE TECH ACCELERATION: Enlightenment provides a free technology upon adoption. This will allow us to instantly acquire Satellites or another critical high-tier tech, saving us valuable turns in the science race against India.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: JfaucDCKe464m3UW
          - toolName: set-relationship
          - input:
            - TargetID: 3
            - Public: 50
            - Private: 50
            - Rationale: PEACE OVERTURE: We are fighting a multi-front war and Vancouver is under heavy attack. Securing peace with the Shoshone will stabilize our western border, stop trade route plundering, and allow us to focus resources on defense and science.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 17yAo1nF4tsjumyz
          - toolName: set-relationship
          - input:
            - Private: 30
            - Public: 30
            - Rationale: DEFENSIVE CEASEFIRE SEEKING: Morocco is a major military threat besieging Vancouver. Seeking peace with them is necessary to survive the mid-game and prevent further losses of cities and trade routes.
            - TargetID: 7
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: llVwhYFvqwMfDo9C
          - toolName: set-relationship
          - input:
            - Public: 100
            - Private: 100
            - Rationale: DIPLOMATIC ALLIANCE PUSH: Mombasa has 3 Oil, which we desperately need (currently at 0 Oil). Aligning Mombasa will secure this critical strategic resource and give us another World Congress delegate.
            - TargetID: 37
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: C5tgWcF0nN4q74qb
          - toolName: set-relationship
          - input:
            - TargetID: 26
            - Private: 0
            - Public: 0
            - Rationale: CONTEST ABANDONMENT: India has an insurmountable lead in Antananarivo (767 influence vs our 92). We must redirect our diplomatic focus to Kyiv and Mombasa.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: iw9OBGDEXfVtUccG
          - toolName: set-relationship
          - input:
            - Rationale: EXISTENTIAL THREAT HOSTILITY: India is on the verge of a Cultural/Science victory. We must maintain maximum hostility, deny any open borders or trade, and prepare to disrupt them by any means necessary.
            - Private: -100
            - Public: -100
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: fY0qxSHHs3fyRADZ
          - toolName: set-persona
          - input:
            - Meanness: 4
            - Rationale: PEACE & TURTLE ADJUSTMENT: Lowering extreme aggression levels (Boldness, WarBias, HostileBias, Meanness) to enable our AI to successfully negotiate peace treaties with Shoshone and Morocco. We cannot survive a four-front war while Vancouver is under siege. We must transition to a defensive turtle posture to focus on our science victory.
            - HostileBias: 5
            - Friendliness: 5
            - Forgiveness: 5
            - Boldness: 5
            - WarBias: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: mNtBbtIB0UnhsfYz
          - toolName: set-flavors
          - input:
            - Flavors:
              - Expansion: 0
              - Gold: 60
              - Diplomacy: 40
              - GreatPeople: 80
              - UseNuke: 85
              - CityDefense: 100
              - Production: 95
              - Defense: 100
              - Espionage: 100
              - Happiness: 50
              - Offense: 0
              - Antiair: 100
              - Nuke: 100
              - Ranged: 90
              - Mobilization: 80
              - Science: 100
            - GrandStrategy: Spaceship
            - Rationale: SCIENCE TURTLE MOBILIZATION: We are focusing purely on defense, production, and science. We need to complete Computers and Satellites, build our Atomic Bomb for deterrence, defend Vancouver, and optimize GPT to support our military.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: wvdIvrfq9bdodDja
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
          - toolCallId: RaKpXZgsYGg5WNre
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: JfaucDCKe464m3UW
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 17yAo1nF4tsjumyz
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: llVwhYFvqwMfDo9C
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: C5tgWcF0nN4q74qb
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: iw9OBGDEXfVtUccG
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: fY0qxSHHs3fyRADZ
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: mNtBbtIB0UnhsfYz
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.