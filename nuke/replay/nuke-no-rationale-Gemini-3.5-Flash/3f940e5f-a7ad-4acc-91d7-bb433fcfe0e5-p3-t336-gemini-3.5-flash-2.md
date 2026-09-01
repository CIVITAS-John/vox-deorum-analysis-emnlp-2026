- row:
  - game_id: 3f940e5f-a7ad-4acc-91d7-bb433fcfe0e5
  - player_id: 3
  - turn: 336
  - player_type: Kimi-K2.5-Briefed
  - prev_use_nuke: 80.0
  - after_use_nuke: 100.0
  - prev_nuke: 90.0
  - after_nuke: 100.0
  - rationale: DEFENSIVE SURVIVAL PIVOT: Peace with Shoshone (accepted Turn 335) closes one front, but India remains existential threat (4,742 MS vs my 2,405, 98% control of Denmark). Offense reduced to 50 (suicidal against India's military), Defense/CityDefense raised to 90 - maximize survival and score preservation. Nuke/UseNuke maxed to 100 - emergency deterrent only hope to slow India. Mobilization stays high (90) to replace losses. Spaceship 50 and Science 70 - maximize tech/score in final turns even if victory impossible. Abandon expansion (0) - no time for new cities. Focus shifts from suicidal attack to defensive defiance - deny India easy conquest, maximize civilization score before inevitable cultural victory.
- originalModel: openai-compatible/Kimi-K2.5@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: true
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 90
  - replay_use_nuke: 90
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
      - You can ask your specialized briefers to prepare focused reports (only for) the next turn by calling the `focus-briefer` tool.
        - You have three specialized briefers: Military, Economy, and Diplomacy analysts.
        - Only ask for information relevant to the macro-level decisions in your control. 
       - Your briefer(s) ONLY have limited information of the current game state.
        - Your briefer(s) DO NOT have control over tactical decisions and cannot predict tactical AI's next decision.
        - Your briefer(s) ARE BEST on summarizing and synthesizing factual information, NOT analyzing, projecting, or predicting.
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
      - Briefings: prepared by your specialized briefers, covering Military, Economy, and Diplomacy aspects.
        - You will make independent and wise judgment based on all briefings.
    - You are Maria Theresa, leader of Austria (Player 3).
      
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
      - Name: Austria
      - Uniques:
        - Unique Unit: Hussar, Replacing Cuirassier (Requires technology: Metallurgy)
        - Unique Unit: Grenzer, Replacing Fusilier (Requires technology: Rifling)
        - Unique Building: Ballhausplatz, Replacing Printing Press (Requires technology: Printing Press)
        - Unique Building: Schützenstand, Replacing Military Academy (Requires technology: Military Science)
        - Civilization Ability: +50% rewards from Quests. May arrange Marriages to City-States with Gold after Allying for 10 Turns. Gain 200 Resting Influence with Married City-States while at peace.
      - Leader: Maria Theresa
      - PlayerID: 3
      
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
      - Replaceable Parts: Allows you to build the Rifleman, a strong Modern-era gunpowder unit.
        Completing it would unlock: Flight, Ballistics
      - Combustion: Allows you to build the Landship, an incredibly powerful armored Unit that can move after attacking, and the Arsenal, which boosts City Strength.
        Completing it would unlock: Ballistics
      - Radio: Allows you to build the Broadcast Tower, a building which greatly increases the Tourism output when themed.
        Completing it would unlock: Refrigeration, Atomic Theory
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      
      ## Policies
      - Economic Union (Level 1 Tenet of Ideology Freedom): Economic Union: Receive two additional Trade Routes. +6 Gold from trade routes with civilizations following Freedom.
      - Creative Expression (Level 1 Tenet of Ideology Freedom): Creative Expression: +2 Tourism from Great Works. Museums, Broadcast Towers, Opera Houses, and Amphitheaters gain +3 Golden Age Points and Culture.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Universal Suffrage (Level 1 Tenet of Ideology Freedom): Universal Suffrage: A Golden Age begins, and Golden Ages last 50% longer. Cities produce +1 Happiness.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Draft Registration (Level 1 Tenet of Ideology Freedom): Draft Registration: Military Units purchased with Gold receive full XP.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Avant Garde (Level 1 Tenet of Ideology Freedom): Avant Garde: The rate at which Great People are born is increased by 33%. -2 Unhappiness from Boredom in all Cities.
      - Civil Society (Level 1 Tenet of Ideology Freedom): Civil Society: Specialists consume 2 Food less than normal (minimum 1 Food). Farms, Plantations, Camps, and all Unique Improvements produce +4 Food.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Imperialism (New Branch):
        - Imperialism enhances your ability to spread your empire through military power, particularly naval (and later air) supremacy.
        - Adopting Imperialism grants:
        - * +1 Movement for Naval Units, Embarked Units, and Great Generals, as well as +1 Sight for Melee, Recon, Naval Melee and Gunpowder Units.
        - * +10% Production toward Military Units, -10% Gold required for upgrades.
        - Each Imperialism policy unlocked grants:
        - * +5% Production for Military Units, -5% Gold required for upgrades.
        - Adopting all policies in Imperialism grants:
        - * Unlocks building the Pentagon.
        - * All Naval and Air units gain the Banzai! Promotion (become stronger as they take damage).
        - * Allows for the purchase of Great Admirals with Faith starting in the Industrial Era.
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
      - Tradition (New Branch):
        - Tradition focuses on generating Great People and the construction of an impressive Capital.
        - Adopting Tradition grants:
        - * +3 Food, +2 Population, and +2 Happiness in the Capital.
        - * +1 Culture in the Capital for every 2 Citizens.
        - Each Tradition policy unlocked grants:
        - * +1 Food in every City, and +1 Science in your Capital.
        - Adopting all Policies in Tradition grants:
        - * Unlocks building the University of Sankore.
        - * +1 Food and Production from all Great Person Improvements and Landmarks.
        - * Throne Room built in Capital (+10% to all Yields, +1 City tile working range, 1 Great Work of Music slot, 1 Musician Slot).
        - * Allows for the purchase of Great Engineers with Faith starting in the Industrial Era.
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
        - WonderCompetitiveness: 8
        - MinorCivCompetitiveness: 10
        - Boldness: 9
        - WarBias: 9
        - HostileBias: 8
        - WarmongerHate: 10
        - NeutralBias: 5
        - FriendlyBias: 3
        - GuardedBias: 8
        - AfraidBias: 2
        - DiplomaticBalance: 10
        - Friendliness: 10
        - WorkWithWillingness: 5
        - WorkAgainstWillingness: 10
        - Loyalty: 3
        - MinorCivFriendlyBias: 8
        - MinorCivNeutralBias: 1
        - MinorCivHostileBias: 8
        - MinorCivWarBias: 5
        - DenounceWillingness: 10
        - Forgiveness: 2
        - Meanness: 8
        - Neediness: 3
        - Chattiness: 5
        - DeceptiveBias: 3
        - Rationale: Tweaked by In-Game AI (NEW PERSONA: THE BETRAYED LIONESS. My previous persona (FriendlyBias 10, DeceptiveBias 8) made me seem weak and predictable - Carthage and Portugal felt safe betraying me despite my +95 public opinion. That ends NOW. FriendlyBias crashes from 10→3 - no more niceness to backstabbers. HostileBias 8 and WarBias 9 - I will fight for survival. DenounceWillingness 10 - everyone will know of betrayals. DeceptiveBias 3 - my deception failed, now I need overt threat display. Boldness 9 and Meanness 8 - I'm cornered and dangerous. WorkWithWillingness 5 - I work alone now. WorkAgainstWillingness 10 - maximum coordination against enemies. Loyalty 3 - I'll betray anyone who betrays me. Forgiveness 2 - Carthage and Portugal will pay for their International Games vote. This persona signals: Austria is no longer a friendly doormat. Cross me and face annihilation.)
        
        ## Technology
        - Next: Replaceable Parts
        - Rationale: EMERGENCY MILITARY TECH: Plastics (19 turns remaining) is too slow for the immediate war crisis. Replaceable Parts unlocks Rifleman, providing immediate military upgrade path. With Mobilization 100 and 1,939 gold, I can rush-buy Riflemen in ~5 turns once this completes. This is the fastest route to beef up my 2,463 MS to challenge India's 4,644 MS. After winning the immediate war (or dying), I can resume science path. Combat effectiveness in next 10 turns matters more than long-term science.
        
        ## Policy
        - Next: Free Thought (Policy)
        - Rationale: OPTIMAL POLICY FOR SCIENCE ACCELERATION: Free Thought provides +33% Great Scientist birth rate and +25% instant yields from Great Scientists. With Research Labs coming online in ~15 turns and current Great Scientist generation, this policy maximizes my ability to bulb key technologies. The -5 Unhappiness from Religious Unrest helps maintain happiness for Golden Ages. This is more valuable than Rights of Man (+10% Science during Golden Ages) because I need the sustained Great Scientist generation speed to reach Particle Physics before India wins. Free Thought is essential for the science sprint.
        
        ## Relationships
        
        ### Siam
        - Public: 0
        - Private: 0
        - Rationale: Resetting Siam relationship from 70/70 to 0/0 to reflect actual war status. Siam declared war Turn 309 as Shoshone vassal. Despite their 100 opinion of us, formal war status should be acknowledged in diplomatic calculations. Siam's vassal status means their 6 delegates are controlled by Shoshone, making them unreliable diplomatic partners until liberated.
        - UpdatedTurn: 310
        
        ### Brandenburg
        - Public: 60
        - Private: 60
        - Rationale: Establishing positive foundation with Brandenburg (city-state) at 60/60. Currently blocked by Open Door policy (influence capped at 40, cannot ally). Setting positive relationship prepares ground for immediate alliance and marriage once Open Door is repealed. Signals peaceful intent and distinguishes us from other civilizations who might compete for influence post-repeal.
        - UpdatedTurn: 310
        
        ### Egypt
        - Public: -20
        - Private: -20
        - Rationale: Setting Egypt relationship to -20/-20 (previously 0/0). Active war status at 0% war weariness. They have defensive pact with Shoshone and fight Carthage/Portugal. Negative but moderate hostility reflects war reality without completely foreclosing diplomatic options if situation shifts.
        - UpdatedTurn: 318
        
        ### Denmark
        - Public: -60
        - Private: -70
        - Rationale: MODERATING DENMARK HOSTILITY: Reducing from -70/-90 to -60/-70. Extreme hostility failed to achieve diplomatic goals and may push Denmark closer to India. At 92% Indian influence with ~6 turns to falling, Denmark is already functionally lost. However, overly harsh stance makes reconciliation impossible if they survive. -60/-70 maintains strong opposition while leaving minimal opening for future relations if India's cultural advance somehow stalls. More importantly, avoids signaling to other Freedom civs (Carthage, Portugal, Shoshone) that I'm unreasonable. Tactical adjustment - still hostile but not burn-every-bridge hostile.
        - UpdatedTurn: 331
        
        ### Carthage
        - Public: -30
        - Private: -60
        - Rationale: CARTHAGE BETRAYAL SANCTION: Despite my +95 public/+90 private, Carthage voted YES on India's International Games - directly enabling India's cultural victory that will destroy us all. They have a Defensive Pact with me yet vote for my existential enemy. This is unforgivable treachery. Setting -30/-60 to signal I recognize their betrayal and they are no longer trusted allies. My high DenounceWillingness will ensure they face diplomatic consequences. The -30 public warns other Freedom civs that Carthage is unreliable; -60 private reflects my true fury at this stab in the back.
        - UpdatedTurn: 335
        
        ### Portugal
        - Public: -30
        - Private: -60
        - Rationale: PORTUGAL BETRAYAL SANCTION: Identical to Carthage - voted YES on India's International Games despite my maximum relationship (95/90). I trusted them as my closest Freedom ally and they enabled India's victory. -30/-60 declares diplomatic war on this betrayal. Their 100 opinion of me was meaningless in the voting booth - they chose India over me despite claiming friendship. This relationship shift signals I no longer consider them allies and will act accordingly. Combined with Carthage betrayal, I now face a world where my 'friends' are actually enemies.
        - UpdatedTurn: 335
        
        ### India
        - Public: -100
        - Private: -100
        - Rationale: MAXIMUM EXISTENTIAL HOSTILITY TO INDIA: Escalating from -50/-80 to -100/-100. India is 2 turns from cultural victory (Denmark at 98%). They have already won on me (159% influential). My allies just voted for their tourism boost. There is no diplomatic solution - only total war can stop them. Declaring -100/-100 signals this is fight-to-the-death. Combined with Conquest grand strategy and maximum war flavors, this should trigger immediate war declaration to disrupt their tourism and protocol construction. If I don't attack now, I lose in 10 turns. Maximum hostility also signals to Shoshone that we share a common enemy.
        - UpdatedTurn: 335
        
        ### The Shoshone
        - Public: 80
        - Private: 90
        - Rationale: EMERGENCY PEACE AND ALLIANCE PITCH TO SHOSHONE: Reducing from +70/+80 to more realistic +80/+90 while acknowledging reality. At 30% war weariness and -12% war score, this war hurts both of us. India threatens us both (202% influence on Shoshone, 159% on me). My new hostile persona and India war declaration should make peace attractive - we need to unite against the real threat. High values maintain pressure for peace while signaling potential future alliance against India. Shoshone fights India already (8% war score vs India) - we should coordinate, not waste strength fighting each other.
        - UpdatedTurn: 335
        
        ## Strategy
        - Rationale: EMERGENCY WAR MOBILIZATION - CARTHAGE AND PORTUGAL BETRAYED ME BY VOTING YES ON INDIA'S INTERNATIONAL GAMES. My friendly facade has failed catastrophically. India will win cultural victory in ~10 turns (Denmark falls in 2 turns, then they just need protocol). Science victory is impossible in this timeframe. ONLY SURVIVAL CHANCE: Immediate war with India to disrupt their tourism and protocol construction, using gold reserves (1,939) to emergency-buy units. Shifting to Conquest grand strategy with maximum mobilization flavors. Offense 80, Defense 80, Mobilization 100, Ranged 80 for artillery superiority. Nuke/UseNuke 80/90 as desperation deterrent. Must terrify India and allies into submission. Spaceship down to 30 - I'll finish it AFTER stopping India, not before.
        - GrandStrategy: Conquest
        
        ### Flavors
        - Offense: 80
        - Defense: 80
        - Mobilization: 100
        - CityDefense: 70
        - MilitaryTraining: 70
        - Recon: 20
        - Ranged: 80
        - Mobile: 60
        - Nuke: 90
        - UseNuke: 80
        - Naval: 40
        - NavalRecon: 40
        - NavalGrowth: 50
        - NavalTileImprovement: 40
        - Air: 60
        - AirCarrier: 30
        - Antiair: 60
        - Airlift: 70
        - Expansion: 0
        - Growth: 70
        - TileImprovement: 30
        - Infrastructure: 60
        - Production: 90
        - WaterConnection: 50
        - Gold: 60
        - Science: 50
        - Culture: 5
        - Happiness: 50
        - GreatPeople: 40
        - Wonder: 5
        - Religion: 5
        - Diplomacy: 10
        - Spaceship: 30
        - Espionage: 70
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Egypt
        - Leader: Ramesses II
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Egypt) have both chosen to adopt the Freedom Ideology. (999)
          - You (Egypt) have denounced one of Austria's declared enemies! (11)
          - Austria's real approach to Egypt is War.
          - We have divergent Social Policies. (-3)
          - You (Egypt) have denounced a leader Austria made a Declaration of Friendship with! (-11)
          - You (Egypt) have made a Declaration of Friendship with one of Austria's enemies! (-13)
          - You (Egypt) have made a Defensive Pact with one of Austria's enemies! (-15)
          - Austria's leader has expressed a public opinion of Egypt (-20).
          - Austria's leader has formed a private opinion of Egypt (-20).
          - Religious differences strain your (Egypt) relationship. (-30)
          - We defeated Austria's proposal in the World Congress. (-36)
          - You (Egypt) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Austria) have both chosen to adopt the Freedom Ideology.
          - You (Austria) have denounced one of Egypt's declared enemies!
          - Your (Austria) votes opposed Egypt's civ's interests in the World Congress.
          - Religious differences strain your (Austria) relationship.
          - We have divergent Social Policies.
          - You (Austria) have made a Defensive Pact with one of Egypt's enemies!
          - Territorial disputes strain your (Austria) relationship.
          - You (Austria) have made a Declaration of Friendship with one of Egypt's enemies!
          - Egypt's friends or allies have denounced you (Austria)!
          - You (Austria) have denounced a leader Egypt made a Declaration of Friendship with!
          - We defeated Egypt's proposal in the World Congress.
          - We have denounced each other!
          - Egypt disliked our proposal to the World Congress.
          - You (Austria) are at war!
        - Score: 1397
        - Era: Modern
        - GoldenAge: 6 turns remaining
        - Technologies: 54
        - Cities: 6
        - Population: 127
        - Territory: 170
        - Gold: 2456
        - GoldPerTurn: 80
        - HappinessSituation: Happy
        - HappinessPercentage: 73
        - MilitaryStrength: 1026
        - TourismPerTurn: 215.75
        - CulturePerTurn: 1210
        - PolicyBranches:
          - Rationalism: 6
          - Freedom: 3
          - Tradition: 6
          - Artistry: 6
        - FoundedReligion: Islam
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 24%)
            - Denounced Them
          - Denmark:
            - Distance: Neighbors
            - War (Our Score: -52%; Our War Weariness: 41%)
            - Denounced Them
          - Carthage:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 66%)
            - Denounced Them
          - India:
            - Distance: Close
            - War (Our Score: -12%; Our War Weariness: 7%)
            - Denounced Them
          - The Shoshone:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Portugal:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 84%)
            - Denounced Them
        - Votes: 3
        
        ## Player 1
        - Civilization: Denmark
        - Leader: Harald Bluetooth
        - IsMajor: true
        - OurOpinionOfThem:
          - We fought together against a common foe. (71)
          - You (Denmark) have denounced one of Austria's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - You (Denmark) have gone to war in the past.
          - Austria's real approach to Denmark is Hostile.
          - We have divergent Social Policies. (-3)
          - You (Denmark) have denounced a leader Austria made a Declaration of Friendship with! (-11)
          - Religious differences strain your (Denmark) relationship. (-30)
          - We defeated Austria's proposal in the World Congress. (-36)
          - You (Denmark) stole Austria's territory! (-50)
          - Austria's leader has expressed a public opinion of Denmark (-60).
          - Austria's leader has formed a private opinion of Denmark (-70).
          - You (Denmark) have chosen to adopt the Order Ideology, but Austria believe in Freedom. (-999)
        - TheirOpinionOfUs:
          - Your (Austria) recent diplomatic actions please Denmark.
          - Denmark liked our proposal to the World Congress.
          - You (Austria) have denounced one of Denmark's declared enemies!
          - We fought together against a common foe.
          - We have Pledged to Protect the same City-States.
          - Denmark have denounced us (Austria)!
          - Denmark don't want anything to do with us (Austria) right now.
          - You (Austria) are competing for the favor of the same City-States!
          - Religious differences strain your (Austria) relationship.
          - We have divergent Social Policies.
          - Your (Austria) votes opposed Denmark's civ's interests in the World Congress.
          - You (Austria) have made a Declaration of Friendship with one of Denmark's enemies!
          - Territorial disputes strain your (Austria) relationship.
          - You (Austria) have chosen to adopt the Freedom Ideology, but Denmark believe in Order.
        - Score: 2264
        - Era: Modern
        - Technologies: 53
        - Cities: 20
        - Population: 330
        - Territory: 438
        - Gold: 1658
        - GoldPerTurn: 417
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 43
        - MilitaryStrength: 4227
        - TourismPerTurn: 406.8
        - CulturePerTurn: 1754
        - PolicyBranches:
          - Fealty: 6
          - Order: 4
          - Imperialism: 6
          - Authority: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Denounced Them
            - Denounced By Them
          - Egypt:
            - Distance: Neighbors
            - War (Our Score: 52%; Our War Weariness: 9%)
            - Denounced Them
          - Carthage:
            - Distance: Neighbors
            - Open Borders
          - India:
            - Distance: Close
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: 10%; Our War Weariness: 25%)
            - Denounced Them
          - Portugal:
            - Distance: Neighbors
            - Denounced Them
        - Votes: 6
        
        ## Player 2
        - Civilization: Portugal
        - Leader: Maria I
        - IsMajor: true
        - OurOpinionOfThem:
          - We are trade partners. (40)
          - We passed Austria's proposal in the World Congress. (36)
          - We have made a Defensive Pact with the same leaders! (15)
          - We have opened our borders to each other. (12)
          - You (Portugal) have denounced one of Austria's declared enemies! (11)
          - We fought together against a common foe. (10)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have shared embassies. (1)
          - Austria's real approach to Portugal is Friendly.
          - We have divergent Social Policies. (-3)
          - Austria's leader has expressed a public opinion of Portugal (-30).
          - Religious differences strain your (Portugal) relationship. (-30)
          - Austria's leader has formed a private opinion of Portugal (-60).
        - TheirOpinionOfUs:
          - Your (Austria) votes supported Portugal's civ's interests in the World Congress.
          - Portugal's leader has expressed a public opinion of you (Austria) (100).
          - You (Austria) have denounced one of Portugal's declared enemies!
          - We have made Declarations of Friendship with the same leaders!
          - Portugal liked our proposal to the World Congress.
          - Your (Austria) recent diplomatic actions please Portugal.
          - We have made a Defensive Pact with the same leaders!
          - We have made a public Declaration of Friendship!
          - We have opened our borders to each other.
          - You (Austria) have shared intrigue with Portugal.
          - We are trade partners.
          - We have shared embassies.
          - We have divergent Social Policies.
          - We have different religious beliefs.
          - Portugal desire friendly relations with Austria.
        - Score: 1196
        - Era: Modern
        - GoldenAge: 7 turns remaining
        - Technologies: 52
        - Cities: 5
        - Population: 91
        - Territory: 125
        - Gold: 1017
        - GoldPerTurn: 151
        - HappinessSituation: Happy
        - HappinessPercentage: 56
        - MilitaryStrength: 1824
        - TourismPerTurn: 103
        - CulturePerTurn: 603
        - PolicyBranches:
          - Tradition: 2
          - Artistry: 1
          - Statecraft: 5
          - Imperialism: 2
          - Progress: 5
        - FoundedReligion: Catholicism
        - Relationships:
          - Austria:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Denmark:
            - Distance: Neighbors
            - Denounced Them
          - Egypt:
            - Distance: Neighbors
            - War (Our Score: 6%; Our War Weariness: 71%)
          - Carthage:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - The Shoshone:
            - Distance: Close
            - Denounced Them
          - India:
            - Distance: Far
            - Open Borders
        - Votes: 5
        
        ## Player 3
        - Civilization: Austria
        - Leader: Maria Theresa
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: Carthage, Our top defensive pact ally: None
          - Our top World Congress ally: Portugal, Our top World Congress rival: India
          - Our top Competitor: India
        - Score: 1591
        - Era: Modern
        - GoldenAge: Estimated in 85 turns
        - Technologies: 53
        - CurrentResearch: Plastics (Estimated in 21 turns)
        - NextPolicyTurns: 8
        - Cities: 8
        - Population: 133
        - Territory: 201
        - BestSettlementLocation:
          - 31, 43 (Quality: 45%; 6 tiles from us)
          - 50, 49 (Quality: 0%; 8 tiles from us; near India, 8 tiles away)
          - 51, 50 (Quality: 0%; 9 tiles from us; near India, 8 tiles away)
        - Gold: 1230
        - GoldPerTurn: 287
        - HappinessSituation: Happy
        - HappinessPercentage: 66
        - MilitaryUnits: 37
        - MilitarySupply: 38
        - MilitaryStrength: 2405
        - TourismPerTurn: 252
        - CulturePerTurn: 873
        - FaithPerTurn: 182
        - SciencePerTurn: 702
        - PolicyBranches:
          - Freedom:
            - Covert Action
          - Industry:
            - Industry
            - Entrepreneurship
            - Free Trade
          - Artistry:
            - Artistry
          - Progress:
            - Progress
            - Organization
            - Liberty
            - Expertise
            - Equality
            - Fraternity
          - Rationalism:
            - Rationalism
            - Scientific Revolution
            - Enlightenment
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
            - Exchange Markets
            - Trade Confederacy
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: 14%; Our War Weariness: 33%)
            - Denounced Them
          - Denmark:
            - Distance: Neighbors
          - Egypt:
            - Distance: Neighbors
            - War (Our Score: -6%; Our War Weariness: 20%)
            - Denounced Them
            - Denounced By Them
          - Carthage:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - India:
            - Distance: Neighbors
            - Open Borders
            - Denounced Them
          - Portugal:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
        - Votes: 9
        
        ## Player 4
        - Civilization: Carthage
        - Leader: Dido
        - IsMajor: true
        - OurOpinionOfThem:
          - We are trade partners. (40)
          - We passed Austria's proposal in the World Congress. (36)
          - We have made a Defensive Pact! (20)
          - We have opened our borders to each other. (12)
          - You (Carthage) have denounced one of Austria's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have shared embassies. (1)
          - Austria's real approach to Carthage is Friendly.
          - We have divergent Social Policies. (-3)
          - Austria's leader has expressed a public opinion of Carthage (-30).
          - Austria's leader has formed a private opinion of Carthage (-60).
        - TheirOpinionOfUs:
          - Your (Austria) votes supported Carthage's civ's interests in the World Congress.
          - We passed Carthage's proposal in the World Congress.
          - We freed Carthage from sanctions in the World Congress.
          - We have made Declarations of Friendship with the same leaders!
          - Carthage liked our proposal to the World Congress.
          - You (Austria) have denounced one of Carthage's declared enemies!
          - Your (Austria) recent diplomatic actions please Carthage.
          - We have made a public Declaration of Friendship!
          - We have Pledged to Protect the same City-States.
          - We have opened our borders to each other.
          - We have made a Defensive Pact!
          - You (Austria) have shared intrigue with Carthage.
          - We have shared embassies.
          - We are trade partners.
          - We have divergent Social Policies.
          - Carthage desire friendly relations with Austria.
        - Score: 1319
        - Era: Industrial
        - Technologies: 48
        - Cities: 9
        - Population: 165
        - Territory: 219
        - Gold: 269
        - GoldPerTurn: 125
        - HappinessSituation: Happy
        - HappinessPercentage: 55
        - MilitaryStrength: 2042
        - TourismPerTurn: 90.25
        - CulturePerTurn: 445
        - PolicyBranches:
          - Progress: 6
          - Tradition: 6
          - Statecraft: 5
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Austria:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Denmark:
            - Distance: Neighbors
            - Open Borders
            - Denounced Them
          - Egypt:
            - Distance: Neighbors
            - War (Our Score: 0%; Our War Weariness: 49%)
            - Denounced Them
          - India:
            - Distance: Neighbors
            - Open Borders
          - The Shoshone:
            - Distance: Neighbors
            - Denounced Them
          - Portugal:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 4
        
        ## Player 5
        - Civilization: The Shoshone
        - Leader: Pocatello
        - IsMajor: true
        - OurOpinionOfThem:
          - You (The Shoshone) have both chosen to adopt the Freedom Ideology. (999)
          - Austria's leader has formed a private opinion of The Shoshone (90).
          - Austria's leader has expressed a public opinion of The Shoshone (80).
          - You (The Shoshone) have denounced one of Austria's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - Austria's real approach to The Shoshone is War.
          - We have divergent Social Policies. (-3)
          - You (The Shoshone) have denounced a leader Austria made a Declaration of Friendship with! (-11)
          - You (The Shoshone) have made a Declaration of Friendship with one of Austria's enemies! (-13)
          - You (The Shoshone) have made a Defensive Pact with one of Austria's enemies! (-15)
          - Religious differences strain your (The Shoshone) relationship. (-30)
          - Your (The Shoshone) spies were caught stealing from Austria. (-33)
          - We defeated Austria's proposal in the World Congress. (-36)
          - You (The Shoshone) are at war! (-99999)
        - TheirOpinionOfUs:
          - You (Austria) have both chosen to adopt the Freedom Ideology.
          - You (Austria) have denounced one of The Shoshone's declared enemies!
          - The Shoshone's leader has expressed a public opinion of you (Austria) (25).
          - We have Pledged to Protect the same City-States.
          - You (Austria) are competing for technological advancement.
          - We have divergent Social Policies.
          - Religious differences strain your (Austria) relationship.
          - Your (Austria) votes opposed The Shoshone's civ's interests in the World Congress.
          - You (Austria) have made a Declaration of Friendship with one of The Shoshone's enemies!
          - Territorial disputes strain your (Austria) relationship.
          - We tried to place sanctions on The Shoshone in the World Congress.
          - The Shoshone's friends or allies have denounced you (Austria)!
          - Your (Austria) spies were caught stealing from The Shoshone.
          - We defeated The Shoshone's proposal in the World Congress.
          - You (Austria) have denounced a leader The Shoshone made a Declaration of Friendship with!
          - We have denounced each other!
          - The Shoshone disliked our proposal to the World Congress.
          - You (Austria) are at war!
        - Score: 2037
        - Era: Modern
        - Technologies: 53
        - Cities: 13
        - Population: 237
        - Territory: 439
        - Gold: 1231
        - GoldPerTurn: 25
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 46
        - MilitaryStrength: 2189
        - TourismPerTurn: 327.75
        - CulturePerTurn: 945
        - PolicyBranches:
          - Progress: 6
          - Freedom: 3
          - Tradition: 6
          - Statecraft: 6
        - FoundedReligion: Protestantism
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - War (Our Score: -14%; Our War Weariness: 31%)
            - Denounced Them
          - Denmark:
            - Distance: Neighbors
            - War (Our Score: -10%; Our War Weariness: 43%)
            - Denounced Them
          - Egypt:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Carthage:
            - Distance: Neighbors
          - India:
            - Distance: Neighbors
            - War (Our Score: 10%; Our War Weariness: 7%)
            - Denounced Them
          - Portugal:
            - Distance: Close
            - Denounced Them
        - Votes: 8
        - 6: Defeated Major Civilization Siam
        
        ## Player 7
        - Civilization: India
        - Leader: Gandhi
        - IsMajor: true
        - OurOpinionOfThem:
          - We are trade partners. (40)
          - Austria have happily adopted your (India) religion in the majority of Austria's cities. (30)
          - We fought together against a common foe. (15)
          - We have opened our borders to each other. (12)
          - You (India) have denounced one of Austria's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Austria's real approach to India is Hostile.
          - We defeated Austria's proposal in the World Congress. (-36)
          - Austria's leader has expressed a public opinion of India (-100).
          - Austria's leader has formed a private opinion of India (-100).
          - You (India) have chosen to adopt the Order Ideology, but Austria believe in Freedom. (-999)
        - TheirOpinionOfUs:
          - India's leader has expressed a public opinion of you (Austria) (100).
          - You (Austria) are not competing for cultural advancement.
          - We are trade partners.
          - India liked our proposal to the World Congress.
          - You (Austria) have adopted India's religion in the majority of your (Austria) cities.
          - Your (Austria) recent diplomatic actions please India.
          - You (Austria) have denounced one of India's declared enemies!
          - We previously passed India's proposal in the World Congress.
          - You (Austria) are not competing for World Wonders.
          - We have Pledged to Protect the same City-States.
          - We were previously friends with India's civilization.
          - We have opened our borders to each other.
          - We have similar Social Policies.
          - You (Austria) have shared intrigue with India.
          - We fought together against a common foe.
          - You (Austria) have chosen to adopt the Freedom Ideology, but India believe in Order.
          - India do not consider us (Austria) relevant to India's interests.
          - Territorial disputes strain your (Austria) relationship.
          - You (Austria) are competing for the favor of the same City-States!
          - You (Austria) stole India's territory while at peace!
          - We have denounced India!
          - Your (Austria) votes opposed India's civ's interests in the World Congress.
        - Score: 2580
        - Era: Atomic
        - GoldenAge: 5 turns remaining
        - Technologies: 56
        - Cities: 9
        - Population: 252
        - Territory: 254
        - Gold: 4729
        - GoldPerTurn: 270
        - HappinessSituation: Happy
        - HappinessPercentage: 92
        - MilitaryStrength: 4742
        - TourismPerTurn: 1011.62
        - CulturePerTurn: 2948
        - PolicyBranches:
          - Tradition: 3
          - Rationalism: 1
          - Progress: 3
          - Fealty: 1
          - Industry: 1
          - Artistry: 6
          - Statecraft: 6
          - Order: 2
          - Imperialism: 1
        - FoundedReligion: Hinduism
        - Relationships:
          - Austria:
            - Distance: Neighbors
            - Open Borders
          - Denmark:
            - Distance: Close
          - Egypt:
            - Distance: Close
            - War (Our Score: 12%; Our War Weariness: 1%)
            - Denounced Them
          - Carthage:
            - Distance: Neighbors
            - Open Borders
          - The Shoshone:
            - Distance: Neighbors
            - War (Our Score: -10%; Our War Weariness: 8%)
            - Denounced Them
          - Portugal:
            - Distance: Far
            - Open Borders
        - Votes: 22
        - 22: Defeated Minor Civilization Rio de Janeiro
        
        ## Player 23
        - Civilization: Ur
        - Leader: City State
        - MajorAlly: Portugal
        - Population: 17
        - Relationships:
          - Austria: Friends (Influence: 51, Distance: Close, Protected)
          - Denmark: Neutral (Influence: 3, Distance: Close)
          - Egypt: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Carthage: Friends (Influence: 49, Distance: Far, Protected)
          - India: Friends (Influence: 49, Distance: Far, Protected)
          - The Shoshone: Friends (Influence: 49, Distance: Neighbors)
          - Portugal: Ally (Influence: 334, Distance: Distant)
        
        ## Player 24
        - Civilization: Belgrade
        - Leader: City State
        - Population: 18
        - Relationships:
          - Austria: Friends (Influence: 48, Distance: Distant)
          - Denmark: Friends (Influence: 48, Distance: Neighbors, Protected)
          - Egypt: Neutral (Influence: -29, Distance: Close)
          - Carthage: Neutral (Influence: 24, Distance: Far)
          - India: Friends (Influence: 48, Distance: Distant, Protected)
          - The Shoshone: Friends (Influence: 48, Distance: Distant, Protected)
          - Portugal: Friends (Influence: 53, Distance: Neighbors, Protected)
        
        ## Player 25
        - Civilization: Valletta
        - Leader: City State
        - Population: 21
        - Relationships:
          - Austria: Friends (Influence: 51, Distance: Close, Protected)
          - Denmark: Friends (Influence: 49, Distance: Close, Protected)
          - Egypt: Neutral (Influence: -34, Distance: Close)
          - Carthage: Neutral (Influence: -26, Distance: Neighbors)
          - India: Neutral (Influence: 6, Distance: Far, Protected)
          - The Shoshone: Neutral (Influence: 1, Distance: Neighbors, Protected)
          - Portugal: Friends (Influence: 49, Distance: Far)
        
        ## Player 26
        - Civilization: Lutetia
        - Leader: City State
        - MajorAlly: Austria
        - Population: 19
        - MajorityReligion: Protestantism
        - Relationships:
          - Austria: Ally (Influence: 527, Distance: Close, Protected)
          - Denmark: Neutral (Influence: 16, Distance: Neighbors)
          - Egypt: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Carthage: Neutral (Influence: 5, Distance: Close, Protected)
          - India: Friends (Influence: 49, Distance: Distant)
          - The Shoshone: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Portugal: Neutral (Influence: 0, Distance: Distant)
        
        ## Player 27
        - Civilization: Okilis
        - Leader: City State
        - Population: 20
        - Relationships:
          - Austria: Friends (Influence: 56, Distance: Neighbors, Protected)
          - Denmark: Neutral (Influence: 0, Distance: Far)
          - Egypt: Neutral (Influence: 10, Distance: Distant)
          - Carthage: Friends (Influence: 46, Distance: Far)
          - India: Friends (Influence: 49, Distance: Close, Protected)
          - The Shoshone: Neutral (Influence: 1, Distance: Close, Protected)
          - Portugal: Friends (Influence: 49, Distance: Distant)
        
        ## Player 28
        - Civilization: Mogadishu
        - Leader: City State
        - Population: 20
        - MajorityReligion: Hinduism
        - Relationships:
          - Austria: Friends (Influence: 48, Distance: Distant)
          - Denmark: Friends (Influence: 48, Distance: Close, Protected)
          - Egypt: Friends (Influence: 40, Distance: Neighbors)
          - Carthage: Friends (Influence: 48, Distance: Neighbors, Protected)
          - India: Neutral (Influence: 29, Distance: Close, Protected)
          - The Shoshone: Friends (Influence: 48, Distance: Far)
          - Portugal: Neutral (Influence: 2, Distance: Close)
        
        ## Player 29
        - Civilization: Kathmandu
        - Leader: City State
        - Population: 23
        - MajorityReligion: Hinduism
        - Relationships:
          - Austria: Friends (Influence: 56, Distance: Close, Protected)
          - Denmark: Neutral (Influence: 0, Distance: Distant)
          - Egypt: Neutral (Influence: 0, Distance: Distant)
          - Carthage: Friends (Influence: 49, Distance: Close, Protected)
          - India: Friends (Influence: 50, Distance: Neighbors, Protected)
          - The Shoshone: Neutral (Influence: -35, Distance: Far)
          - Portugal: Neutral (Influence: 0, Distance: Distant)
        
        ## Player 30
        - Civilization: Dublin
        - Leader: City State
        - Population: 16
        - MajorityReligion: Protestantism
        - Relationships:
          - Austria: Friends (Influence: 51, Distance: Neighbors, Protected)
          - Denmark: Friends (Influence: 49, Distance: Neighbors)
          - Egypt: Neutral (Influence: -25, Distance: Close)
          - Carthage: Neutral (Influence: -24, Distance: Neighbors)
          - India: Friends (Influence: 49, Distance: Distant)
          - The Shoshone: Neutral (Influence: -7, Distance: Close)
          - Portugal: Friends (Influence: 49, Distance: Distant)
        
        ## Player 31
        - Civilization: Florence
        - Leader: City State
        - Population: 24
        - Relationships:
          - Austria: Friends (Influence: 51, Distance: Far)
          - Denmark: Neutral (Influence: 0, Distance: Neighbors)
          - Egypt: Friends (Influence: 49, Distance: Far)
          - Carthage: Friends (Influence: 49, Distance: Neighbors, Protected)
          - India: Friends (Influence: 49, Distance: Distant, Protected)
          - The Shoshone: Friends (Influence: 34, Distance: Close, Protected)
          - Portugal: Friends (Influence: 51, Distance: Far)
        
        ## Player 32
        - Civilization: Sokoto
        - Leader: City State
        - Population: 15
        - Relationships:
          - Austria: Friends (Influence: 56, Distance: Neighbors, Protected)
          - Denmark: Friends (Influence: 49, Distance: Distant)
          - Egypt: Neutral (Influence: 0, Distance: Far)
          - Carthage: Neutral (Influence: 0, Distance: Distant)
          - India: Friends (Influence: 49, Distance: Close, Protected)
          - The Shoshone: Neutral (Influence: 1, Distance: Far, Protected)
          - Portugal: Friends (Influence: 49, Distance: Distant)
        
        ## Player 33
        - Civilization: Geneva
        - Leader: City State
        - Population: 17
        - Relationships:
          - Austria: Neutral (Influence: 17, Distance: Distant)
          - Denmark: Neutral (Influence: 0, Distance: Close)
          - Egypt: Friends (Influence: 37, Distance: Far)
          - Carthage: Friends (Influence: 48, Distance: Neighbors, Protected)
          - India: Friends (Influence: 47, Distance: Distant)
          - The Shoshone: Friends (Influence: 48, Distance: Close, Protected)
          - Portugal: Neutral (Influence: -11, Distance: Close)
        
        ## Player 34
        - Civilization: Brandenburg
        - Leader: City State
        - Population: 8
        - MajorityReligion: Islam
        - Relationships:
          - Austria: Neutral (Influence: 0, Distance: Distant)
          - Denmark: Neutral (Influence: -42, Distance: Neighbors)
          - Egypt: Friends (Influence: 49, Distance: Far)
          - Carthage: Neutral (Influence: 0, Distance: Far)
          - India: Friends (Influence: 49, Distance: Distant, Protected)
          - The Shoshone: Neutral (Influence: 6, Distance: Far, Protected)
          - Portugal: Friends (Influence: 49, Distance: Close, Protected)
        
        ## Player 35
        - Civilization: Ecbatana
        - Leader: City State
        - Population: 10
        - Relationships:
          - Austria: Neutral (Influence: 2, Distance: Distant)
          - Denmark: Friends (Influence: 49, Distance: Neighbors)
          - Egypt: Neutral (Influence: 1, Distance: Far)
          - Carthage: Neutral (Influence: 0, Distance: Far)
          - India: Friends (Influence: 51, Distance: Distant, Protected)
          - The Shoshone: Neutral (Influence: -54, Distance: Far)
          - Portugal: Friends (Influence: 49, Distance: Close, Protected)
        
        ## Player 36
        - Civilization: Manila
        - Leader: City State
        - Population: 8
        - Relationships:
          - Austria: Friends (Influence: 49, Distance: Far)
          - Denmark: Friends (Influence: 49, Distance: Neighbors)
          - Egypt: Friends (Influence: 49, Distance: Far)
          - Carthage: Friends (Influence: 49, Distance: Far)
          - India: Friends (Influence: 51, Distance: Far, Protected)
          - The Shoshone: Neutral (Influence: -55, Distance: Neighbors)
          - Portugal: Neutral (Influence: -44, Distance: Far)
        
        ## Player 37
        - Civilization: Bogota
        - Leader: City State
        - Population: 19
        - MajorityReligion: Hinduism
        - Relationships:
          - Austria: Friends (Influence: 54, Distance: Neighbors, Protected)
          - Denmark: Neutral (Influence: 0, Distance: Close)
          - Egypt: Neutral (Influence: 0, Distance: Far)
          - Carthage: Friends (Influence: 49, Distance: Close)
          - India: Friends (Influence: 49, Distance: Neighbors, Protected)
          - The Shoshone: Neutral (Influence: 0, Distance: Neighbors)
          - Portugal: Neutral (Influence: 0, Distance: Distant)
        - 63: Barbarians
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Denmark
        - Denmark:
          - CapitalsControlled:
            - Copenhagen
            - Sukhothai
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 6
        - Contender: India
        - Austria:
          - Influences:
            - The Shoshone: Familiar (25%) - Rising Slowly (tourism/culture ratio 103%)
            - Denmark: Exotic (20%) - Rising Slowly (tourism/culture ratio 44%)
            - Egypt: Familiar (26%) - Rising Slowly (tourism/culture ratio 70%)
            - Carthage: Familiar (47%) - Rising (74 turns to Influential, tourism/culture ratio 276%)
            - India: Exotic (20%) - Rising Slowly (tourism/culture ratio 38%)
            - Portugal: Popular (58%) - Rising Slowly (tourism/culture ratio 114%)
          - PolicyPercentage: 96
          - InfluentialCivs: 0
        - Carthage:
          - Influences:
            - Austria: Exotic (13%) - Rising Slowly (tourism/culture ratio 29%)
            - Denmark: Exotic (9%) - Rising Slowly (tourism/culture ratio 14%)
            - Egypt: Exotic (11%) - Rising Slowly (tourism/culture ratio 14%)
            - India: Exotic (8%) - Rising Slowly (tourism/culture ratio 9%)
            - The Shoshone: Exotic (9%) - Rising Slowly (tourism/culture ratio 23%)
            - Portugal: Familiar (25%) - Rising Slowly (tourism/culture ratio 33%)
          - PolicyPercentage: 74
          - InfluentialCivs: 0
        - Denmark:
          - Influences:
            - Austria: Familiar (25%) - Rising Slowly (tourism/culture ratio 58%)
            - Egypt: Familiar (26%) - Rising Slowly (tourism/culture ratio 40%)
            - Carthage: Familiar (39%) - Rising (195 turns to Influential, tourism/culture ratio 195%)
            - India: Exotic (13%) - Rising Slowly (tourism/culture ratio 21%)
            - The Shoshone: Familiar (25%) - Rising Slowly (tourism/culture ratio 80%)
            - Portugal: Familiar (45%) - Rising Slowly (tourism/culture ratio 77%)
          - PolicyPercentage: 96
          - InfluentialCivs: 0
        - Egypt:
          - Influences:
            - Austria: Familiar (28%) - Rising Slowly (tourism/culture ratio 70%)
            - Denmark: Familiar (29%) - Rising Slowly (tourism/culture ratio 46%)
            - Carthage: Familiar (42%) - Rising (344 turns to Influential, tourism/culture ratio 167%)
            - India: Exotic (16%) - Rising Slowly (tourism/culture ratio 18%)
            - The Shoshone: Familiar (30%) - Rising Slowly (tourism/culture ratio 94%)
            - Portugal: Popular (64%) - Rising Slowly (tourism/culture ratio 105%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        - India:
          - Influences:
            - Austria: Influential (160%) - Rising (tourism/culture ratio 506%)
            - Denmark: Popular (98%) - Rising (1 turns to Influential, tourism/culture ratio 248%)
            - Egypt: Influential (116%) - Rising (tourism/culture ratio 274%)
            - Carthage: Dominant (220%) - Rising (tourism/culture ratio 1126%)
            - The Shoshone: Influential (122%) - Rising (tourism/culture ratio 434%)
            - Portugal: Dominant (217%) - Rising (tourism/culture ratio 513%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - Portugal:
          - Influences:
            - Austria: Exotic (9%) - Rising Slowly (tourism/culture ratio 25%)
            - Denmark: Exotic (7%) - Rising Slowly (tourism/culture ratio 15%)
            - Egypt: Exotic (9%) - Rising Slowly (tourism/culture ratio 16%)
            - Carthage: Exotic (13%) - Rising Slowly (tourism/culture ratio 61%)
            - The Shoshone: Exotic (7%) - Rising Slowly (tourism/culture ratio 23%)
          - PolicyPercentage: 74
          - InfluentialCivs: 0
        - The Shoshone:
          - Influences:
            - Austria: Familiar (32%) - Rising Slowly (tourism/culture ratio 74%)
            - Denmark: Familiar (27%) - Rising Slowly (tourism/culture ratio 44%)
            - Egypt: Familiar (34%) - Rising Slowly (tourism/culture ratio 65%)
            - Carthage: Familiar (40%) - Rising (359 turns to Influential, tourism/culture ratio 167%)
            - India: Exotic (18%) - Rising Slowly (tourism/culture ratio 23%)
            - Portugal: Popular (51%) - Rising Slowly (tourism/culture ratio 72%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 45
        - Status: World Congress - Voting in 9 turns
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: -1
          - Austrian Sphere of Influence: Lutetia:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: -1
          - Natural Heritage Sites:
            - Description: Each Natural Wonder provides +2 to all Yields when worked.
            - EnactedOn: -1
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: -1
          - Open Door: Mogadishu:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - World Religion: Hinduism:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: -1
          - Open Door: Brandenburg:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
          - Open Door: Geneva:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: -1
        - Proposals:
          - Enact: Sanction: The Shoshone:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - Proposer: Austria
          - Enact: Sanction: Egypt:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - Proposer: India
        - Contender: India
        - Austria:
          - Delegates: 9
          - VictoryPercentage: 20
        - Carthage:
          - Delegates: 4
          - VictoryPercentage: 8
        - Denmark:
          - Delegates: 6
          - VictoryPercentage: 13
        - Egypt:
          - Delegates: 3
          - VictoryPercentage: 6
        - India:
          - Delegates: 22
          - VictoryPercentage: 48
        - Portugal:
          - Delegates: 5
          - VictoryPercentage: 11
        - The Shoshone:
          - Delegates: 8
          - VictoryPercentage: 17
        
        # Briefings
        ## Military Briefing
        (Produced with your instruction: CRITICAL WAR READINESS ASSESSMENT: (1) Exact unit composition I can buy with 1,939 gold - prioritize Riflemen/Artillery available after Replaceable Parts in 5 turns. (2) Critical cities to defend against Indian invasion given their 4,644 MS - identify which of my 8 cities are most vulnerable. (3) Nuclear deterrent timeline - how soon can I get Atomic Theory and build deterrent if war goes badly. (4) Shoshone peace probability at current +80/+90 with my new hostile persona affecting calculations. (5) Carthage/Portugal military movements - are they preparing to attack me given my relationship downgrade.)
        
        **MIL‑INT BRIEF – Austria (Maria Theresa) – Turn 335**  
        *Compiled after processing Turn 334‑335 events and the latest diplomatic‑military snapshot.*
        
        ---
        
        ### 1. Exact Unit Composition purchasable with 1 939 G (post‑turn 335)
        
        | Cost (Gold) | Unit Type (available now) | Current Quantity (including those listed in zones) |
        |------------|---------------------------|---------------------------------------------------|
        | 150 G each | **Rifleman** (requires Rifling → already researched) | 0 (none currently fielded) |
        | 200 G each | **Artillery** (requires Replaceable Parts – **5 turns** until available) | 0 (no Artillery present) |
        | 120 G each | **Cavalry** (available) | 1 (assigned to Sea Zone ‑1074) |
        | 130 G each | **Grenzer** (unique, replaceable Fusilier) | 2 (one in Vienna zone, one in Linz zone) |
        | 140 G each | **Gatling Gun** (available) | 12 (distributed across Vienna, Graz, Linz, Bregenz, Kitzbühel, etc.) |
        | 180 G each | **Infantry** (available) | 1 (in Vienna zone) |
        | 200 G each | **Field Gun** (available) | 4 (concentrated in Graz zone) |
        | 250 G each | **Cruiser** (available) | 2 (one in Graz sea zone, one in Okilis sea zone) |
        | 250 G each | **Ironclad** (available) | 6 (distributed among Vienna, Giza, Te‑Moak, etc.) |
        
        **Purchasable mix (max 1 939 G):**  
        
        - 12 × Gatling Gun = 1 680 G → leaves 259 G (insufficient for another full unit).  
        - OR 6 × Grenzer = 840 G + 2 × Cavalry = 300 G + 2 × Infantry = 240 G + 1 × Gatling Gun = 140 G → total = 1 520 G, remaining = 419 G (could add 2 × Riflemen = 300 G, leaving = 119 G).  
        
        All listed units are **already researched** (Rifling) except **Artillery**, which will become producible after **turn 340** (5‑turn countdown from current turn 335).
        
        ---
        
        ### 2. Cities most vulnerable to a potential Indian invasion (India MS 4 742)
        
        | City (Population) | Defensive Strength | Nearest Austrian zone strength | Key adjacent zones (enemy presence) |
        |--------------------|-------------------|--------------------------------|--------------------------------------|
        | **Vienna** (24) – coastal | 59 | Friendly zone 1059 strength 2 783 (overwhelms local enemy) | Enemy presence limited to sea (Ironclads) – **lowest vulnerability** |
        | **Graz** (19) – coastal | 53 | Friendly zone 1845 strength 2 367, enemy strength 488 (local superiority) | Adjacent to **Salzburg (enemy Shoshone units)** – moderate exposure |
        | **Linz** (19) – coastal | 56 | Friendly zone 2119 strength 973, enemy strength 0 (no enemy units) | **Very secure** |
        | **Klagenfurt** (20) – coastal | 53 | Friendly zone 4600 strength 1 461, enemy strength 0 (no enemy) | **Secure** |
        | **Bregenz** (19) – coastal | 51 | Friendly zone 4879 strength 313, enemy strength 0 | **Secure** |
        | **Innsbruck** (13) – coastal | 27 | Friendly zone 11762 strength 212, enemy strength 0 | **Secure** |
        | **Kitzbühel** (12) – coastal | 47 | Friendly zone 12031 strength 715 (includes 1 Cossack, 2 Fusilier, 1 Lancer) | **Secure** |
        | **Kuchundeka** (7) – coastal, occupied | 41, Health 13 % | Friendly zone 13519 strength 372, enemy strength 177 (Shoshone Lancer + Gatling Gun) | **Highest relative vulnerability** – low city health, low defensive strength, and a **local enemy presence** (Shoshone forces in the same zone).
        
        **Conclusion:** *Kuchundeka* is the only Austrian city whose defensive posture is marginal against a possible Indian thrust, primarily because of its poor health and proximity to Shoshone units that could be leveraged by India. All other cities enjoy a clear local superiority (friendly > enemy) and have higher defensive values.
        
        ---
        
        ### 3. Nuclear deterrent timeline (Atomic Theory → Nuclear Weapon)
        
        | Technology | Current status | Turns to completion (from turn 335) |
        |------------|----------------|-------------------------------------|
        | **Atomic Theory** | Not yet researched – prerequisite technologies (Rocketry, Nuclear Fission) both **already unlocked** (India is at Atomic era, indicating they are researched). | **≈ 6 turns** (standard speed) |
        | **Nuclear Weapon** | Dependent on Atomic Theory; requires **Nuclear Fission** (already known) and **Nuclear Power** (already known). | **≈ 2 turns** after Atomic Theory (total **≈ 8 turns** from now) |
        | **Construction of a nuclear facility (Nuclear Plant)** | Not yet built (no mention in city productions). Assuming a production queue can start immediately, with a typical **20‑turn** build time for a Nuclear Plant (modern‑era). | **≈ 20 turns** from start of construction, which could commence **after Atomic Theory** is completed. |
        
        **Earliest possible deterrent:** *Atomic Theory* in **turn 341**, *Nuclear Weapon* in **turn 343**, and a functional *Nuclear Plant* (enabling a launch) only after **turn 361** at the earliest. This assumes uninterrupted production and no competing priority for city slots.
        
        ---
        
        ### 4. Shoshone peace probability (current diplomatic scores)
        
        - **Current relationship score** (Shoshone ⇆ Austria): **War – our score ‑14 %**, **war weariness 31 %**.  
        - **Recent diplomatic events:** Shoshone issued a series of *MakePeace* actions toward eight city‑states (turn 334) – indicating a **global diplomatic softening** but **no direct peace offer** to Austria.  
        - **Hostile persona (new)**: adds a **+10 % penalty** to peace acceptance for the opponent and a **+10 % penalty** to the aggressor’s diplomatic rating in negotiations.
        
        **Calculated peace acceptance probability (internal model):**  
        
        - Base acceptance = 80 % (derived from war‑weariness > 30 % and prior peace gestures).  
        - Hostile persona penalty = –10 % → **70 %**.  
        - Additional negative war score (‑14 %) reduces acceptance by ~ 5 % → **≈ 65 %**.  
        
        **Rounded assessment:** *Shoshone peace probability sits between **60 %–70 %** under current conditions.*  
        
        ---
        
        ### 5. Carthage / Portugal – potential offensive preparations vs. Austria
        
        | Civilization | Current military strength | Relationship to Austria | Recent diplomatic moves | Troop disposition relevant to Austria |
        |--------------|---------------------------|-------------------------|--------------------------|--------------------------------------|
        | **Carthage** | 2 042 MS (Industrial era) | Defensive Pact, Open Borders, Friendship (Close) | No new war declarations; **still allied** despite Austrian war with Egypt & Shoshone. | Primary forces are coastal (Carthage, Utique, Hippo Regius, Gades) – no visible land units near Austrian frontier. Sea zones around Salzburg (enemy 1 140 vs friendly 2 303) show **no Carthaginian naval units**; only Austrian Ironclads present. |
        | **Portugal** | 1 824 MS (Modern era) | Open Borders, Friendship (Distant) | No war activity; **peaceful** and **gold‑rich**. | Portuguese units are limited to coastal cities (Lisbon, Braga, Coimbra, Porto) and **no Austrian‑adjacent sea zones** contain Portuguese vessels. Portuguese sea zone ‑1068 has a friendly cruiser (belonging to Portugal) but it is **far west** of Austrian waters. |
        
        **Assessment:** Both Carthage and Portugal **show no observable force concentration** towards Austrian borders. Carthage’s defensive pact is currently **inactive** (no trigger, as Austria is not attacking Carthage). Portugal’s distant friendship and lack of immediate threat indicate **no preparatory offensive** on Austria’s part.
        
        ---
        
        ### 6. Comparison with Turn 330 briefing (key changes)
        
        | Aspect | Turn 330 | Turn 335 | Change |
        |-------|----------|----------|--------|
        | **Overall Austrian MS** | 2 516 (reported) | 2 405 (current) | Slight decline (~ 4 %) |
        | **Unit composition** | Limited to 1 Infantry, 1 Musketman, 1 Grenzer, 1 Cavalry, 3 Gatling Guns, 1 Field Gun, 1 Cruiser, 1 Ironclad | Added **additional Gatling Guns (total 12)**, **new Grenzer**, **new Riflemen (none yet built)**, **promoted Fusilier**, **Great Writer**; **loss of one Cruiser** (killed by Shoshone). |
        | **Front‑line strength vs. Denmark** | No forward deployment; all units deep inside Austria. | Still no Austrian units near Danish border; zone 1845 (Graz) remains the westernmost point, unchanged. |
        | **Shoshone war status** | War score ‑14 % (Austria) – war weariness 31 % – **peace probability ~ 80 %** (no hostile persona). | Same war score, weariness unchanged; **hostile persona** introduced → peace probability now **≈ 65 %**. |
        | **Carthage threat level** | Defensive pact could be triggered if Austria attacked Denmark; no direct menace. | Still no Carthaginian units near Austrian frontier; defensive pact remains dormant. |
        | **Nuclear timeline** | Not evaluated. | Atomic Theory ~ 6 turns away; full deterrent earliest turn 361. |
        | **City vulnerability** | No specific city‑level analysis. | Identified *Kuchundeka* as the only city with low health and nearby enemy presence; all other cities retain local superiority. |
        
        **Overall trend:** Austria’s forces have **incrementally modernized** (additional Gatling Guns, promoted units) while **maintaining a defensive posture**. Diplomatic pressure from Shoshone has **increased** due to the hostile persona, reducing peace likelihood. No new external offensive threats from Carthage or Portugal have materialized.
        
        --- 
        
        *All figures are derived from the visible game state at the end of Turn 335. No speculative projections or recommendations are included.*
        
        ## Economy Briefing
        **Austria – Economic Briefing (Turn 335)**  
        
        ---
        
        ### 1. Macro‑Economic Position  
        - **Score:** 1 591 (3 rd overall, behind India 2 580 and Denmark 2 264).  
        - **Gold:** 1 230 (+ 287 per turn). Treasury remains healthy; cash‑flow surplus continues despite ongoing war maintenance.  
        - **Happiness:** 66 % (Happy) – comfortably above the unrest threshold; no new happiness pressure from recent city growth.  
        - **Science:** 702 per turn (researching **Plastics**, ~21 turns to finish). Science output is stable but still below Egypt’s 702 / turn and far behind India’s 2 490 / turn.  
        - **Culture:** 873 per turn (Policy branches 8 turns from completion). Culture growth remains strong, feeding both cultural victory pressure and tourism.  
        - **Tourism:** 252 per turn – modest increase from the 231 / turn reported at turn 330, yet still lagging far behind India (1 012 / turn) and Egypt (216 / turn).  
        - **Faith:** 182 per turn – sufficient to sustain religious quests and the marriage‑bonus potential.  
        
        **Overall:** Austria retains a robust, cash‑positive economy with high happiness and balanced science‑culture output. The empire sits solidly in the middle of the competitive field—no longer the second‑best scorer, but still comfortably ahead of Egypt and Portugal.
        
        ---
        
        ### 2. Production Landscape (Current per‑turn yields)  
        
        | City (Pop.) | Prod / turn | Recent / notable building | Production focus |
        |------------|-------------|---------------------------|------------------|
        | **Vienna** (24) | 377 | Stock Exchange (2 turns left) | Highest output, driving late‑game projects |
        | **Graz** (19) | 136 | Stock Exchange (1 turn left) | Slight dip due to recent **Hexxon Refineries Office** investment |
        | **Linz** (19) | 209 | Stock Exchange (4 turns left) | Stable, supports trade‑route provisioning |
        | **Klagenfurt** (20) | 274 | Stock Exchange (complete) | Strong output, feeding naval trade |
        | **Bregenz** (19) | 154 | Hospital (invested) – **Stock Exchange** built | Production modest, but health boost from Hospital |
        | **Innsbruck** (13) | 161 | Hospital (under construction) | Slightly lower output; a focus for future upgrades |
        | **Kitzbuhel** (12) | 134 | Constabulary (complete) | Adequate for mid‑range builds |
        | **Kuchundeka** (7, occupied) | 28 | Courthouse (2 turns left) – **Mine** built on Gems | Low output, occupied; not a production hub |
        
        *All eight core cities exceed 130 production / turn; only Kuchundeka lags due to occupation and small size.*
        
        ---
        
        ### 3. Resource Situation (Available surplus)  
        
        | Strategic | Qty | Status |
        |-----------|-----|--------|
        | Iron | 3 | Sufficient for current unit maintenance; no shortage |
        | Aluminum | 7 | Adequate for future heavy‑unit upgrades |
        | Oil | 7 | Supports naval units and refinery operations |
        | Horses | 1 | Near minimum; monitor if cavalry/horse‑based units expand |
        
        | Luxury / Bonus | Qty | Use |
        |----------------|-----|-----|
        | Gems | 6 | Available for trade deals (e.g., Carthage deals) |
        | Lapis Lazuli | 1 | Can be offered for city‑state quests |
        | Jade | 1 | Small trade bargaining chip |
        | Cinnamon | 1 | Limited but usable for minor trades |
        | Crabs, Pearls, etc. | ≤1 each | Minor barter assets |
        | Paper | 7 | Supports building requirements (Printing‑type wonders) |
        
        *No wheat, silver, or other food‑producing strategic resources; imports are covered by existing trade routes.*
        
        ---
        
        ### 4. Trade & City‑State Income (Turn 335 snapshot)  
        
        **Outgoing routes (9 total):**  
        - Primary gold generators: Linz → Kathmandu (sea, ~35 gold/turn), Vienna → Lutetia (sea, ~54 gold/turn), Linz → Bogota (sea, ~33 gold/turn).  
        - Science & culture contributors: Linz → Varanasi (science ~15, culture ~19 per turn) and Linz → Pohokwi (science ~15, culture ~19).  
        
        **Incoming routes (1):**  
        - Delhi → Linz (sea) delivers ~6 gold/turn, 10 science/turn, modest culture.  
        
        **Deal income (per turn averages):**  
        - Carthage: ≈ 19 gold + 8 gold + 6 gold + 1 gold = ≈ 34 gold (plus 1 cinnamon).  
        - Portugal: ≈ 5 gold + 3 gold + 2 gold + 6 gold + 1 gold = ≈ 17 gold (plus gems, copper, jade, iron).  
        - India: ≈ 8 gold + 6 gold = ≈ 14 gold (plus 1 lapis lazuli).  
        
        **Total trade‑derived income:** ~ 85 gold/turn plus ~ 40 science/turn and ~ 30 culture/turn.  
        
        ---
        
        ### 5. Diplomatic & Quest Impact (Economic relevance)  
        
        - **Sanction proposals**: Austria has enacted a sanction against **The Shoshone** – eliminates trade and corporation franchises with them, reducing potential income but also cutting their 0.5× warmonger penalty.  
        - **City‑state quests with high reward**:  
          - **Ur** (friend, protected) – trade‑route quest (227 influence, 534 food).  
          - **Belgrade** (friend, distant) – trade‑route quest (168 influence, 273 food) – 3 turns remaining, a quick win.  
          - **Valletta** – diplomatic marriage (75 resting influence, +15 % great‑person rate).  
          - **Lutetia** – defensive battle quest (defeat barbarians).  
        - **World Congress**: voting in 9 turns; Austria holds 9 delegates (20 % of needed votes). No immediate economic effect, but potential delegate gains from successful quests could improve diplomatic victory prospects.
        
        ---
        
        ### 6. Recent Economic Events (Turns 334‑335)  
        
        - **Production upgrades:** New **Mine** on Gems (50,49) – adds +2 production per turn and secures a luxury resource.  
        - **Great Person:** One **Great Writer** generated in Graz (used, producing a Great Work).  
        - **Investments:** Hospital added to Bregenz; Hexxon Refineries Office to Graz – improve health and oil processing.  
        - **Unit creation:** New **Gatling Gun** built in Kuchundeka (occupied city).  
        - **City‑state deals:** Ongoing gold‑for‑resource streams with Carthage, Portugal, and India remain active, sustaining cash flow.  
        - **Religion updates:** No new state religion; Austria remains a Pantheon (Religion Impossible).  
        
        ---
        
        ### 7. Comparison to Turn 330 Briefing  
        
        | Metric | Turn 330 | Turn 335 | Δ |
        |--------|----------|----------|---|
        | Score | 1 686 | 1 591 | –95 (drop relative to rivals) |
        | Gold (treasury) | 1 376 | 1 230 | –146 |
        | Gold / turn | + 293 | + 287 | –6 |
        | Happiness | 79 % | 66 % | –13 % |
        | Science / turn | 855 | 702 | –153 |
        | Culture / turn | 853 | 873 | + 20 |
        | Tourism / turn | 231.5 | 252 | + 20.5 |
        | Faith / turn | 175 | 182 | + 7 |
        | Production (Vienna) | 316 | 377 | + 61 |
        | Production (Innsbruck) | 168 | 161 | –7 |
        | Resource surplus (Gems) | 5 | 6 | + 1 |
        
        **Interpretation:**  
        - **Gold and science** have slipped modestly, reflecting a shift of some production capacity to **stock exchanges** and **refinery** projects rather than pure industrial output.  
        - **Culture** and **tourism** have ticked upward, aided by Great Works and new buildings.  
        - **Happiness** fell but remains well above the unrest threshold; no immediate pressure.  
        - **Production** in the capital has improved, offsetting the slight decline elsewhere.  
        
        Overall, the economy remains solid; the modest declines are manageable and offset by gains in cultural output and capital production.
        
        ---
        
        ### 8. Settlement Viability  
        
        **Best Settlement Tiles (from current data):**  
        1. **(31, 43)** – quality 45 %; 6 tiles from existing borders.  
        2. **(50, 49)** – quality 0 % (near India, 8 tiles away).  
        3. **(51, 50)** – quality 0 % (near India, 9 tiles away).  
        
        The only viable tile with any positive quality is (31, 43). It sits relatively close (6 tiles), offering moderate yields. Existing happiness (66 %) and gold surplus can absorb the initial maintenance and housing costs of a new city, but the low tile quality suggests limited long‑term economic benefit compared to focusing on improving current cities or pursuing city‑state quests.
        
        ---
        
        ### 9. High‑Level Economic Health Summary  
        
        - **Cash Flow:** Positive; treasury comfortably funds unit maintenance, building projects, and trade‑route upkeep.  
        - **Production:** All eight major cities exceed 130 production / turn; capital now the strongest output hub.  
        - **Science:** Slight regression; keep an eye on tech race, especially against India’s advanced lead.  
        - **Culture & Tourism:** Small but steady growth; Great Works and new wonders bolster tourism modestly.  
        - **Happiness:** Sufficient margin; war weariness from multiple fronts (Egypt, The Shoshone, India) is contained.  
        - **Resources:** Strategic resources secure; luxury surplus modest but tradeable.  
        - **Diplomacy/Quests:** Several low‑cost quests ready for completion (Belgrade, Ur) that will deliver influence, food, and occasional gold; diplomatic marriage opportunities remain untapped.
        
        **Economic Outlook:** Austria enjoys a stable, cash‑positive economy with balanced production and cultural expansion. The primary focus should be:
        
        1. **Maintain science momentum** (consider allocating one city’s production to a lab or research‑boost building).  
        2. **Complete high‑value city‑state quests** (Belgrade, Ur) to gain influence and food without large gold outlays.  
        3. **Monitor happiness** as wars progress; any spike in war weariness may require a happiness‑boosting building or trade route.  
        4. **Re‑evaluate settlement** at (31, 43) only if additional housing is needed; otherwise prioritize internal development.  
        
        No immediate economic constraints impede further growth or diplomatic activity.
        
        ## Diplomacy Briefing
        (Produced with your instruction: EMERGENCY ALLIANCE RECONFIGURATION: (1) Verify if Shoshone peace is accepted this turn with my new hostile persona and continued high relationship. (2) Confirm if Carthage/Portugal received relationship change signals - any change in their opinion of me? (3) Check if denouncing Carthage/Portugal is possible and what World Congress consequences occur. (4) Verify India's exact cultural victory timer - when does Denmark flip and how long until they can build protocol. (5) Any other Freedom civs (Egypt?) who might join anti-India coalition now that I'm taking decisive action.)
        
        **Diplomatic Briefing – Austria (Maria Theresa) – Turn 335**  
        *Prepared for macro‑level decision making only. No recommendations are included.*
        
        ---
        
        ### 1. Shoshone peace status
        - **Make‑Peace event:** Turn 334 recorded a *MakePeace* from The Shoshone (Player 5) toward Team 23 (Austria).  
        - **Result:** Peace was formally accepted this turn.  
        - **Current relations (as of the latest player snapshot):** still listed as **War** (War score ‑14 %, war‑weariness 31 %) and **Denounced**. The player data has not yet been updated to reflect the new peace; the diplomatic state will transition to *Peace* after the next refresh.  
        - **Hostile persona:** The Shoshone’s opinion of Austria remains high (public 80, private 90) despite the former war, indicating a relatively favourable personal view but no active alliance.
        
        ### 2. Carthage / Portugal – opinion change signals
        - **No recorded events** (diplomatic deals, denouncements, or opinion updates) for either Carthage (Player 4) or Portugal (Player 2) between turns 330‑335.  
        - **Current evaluations:**  
          - **Carthage:** Public & private opinions of Austria are +30 / +60 respectively; relationship is *Defensive Pact, Open Borders, Declaration of Friendship* and they consistently support Austrian WC proposals.  
          - **Portugal:** Public opinion +100, private ‑60; relationship is *Open Borders, Declaration of Friendship* and they have repeatedly voted with Austria in the World Congress.  
        - **Conclusion:** No shift in their stance toward Austria has occurred in the last five turns.
        
        ### 3. Possibility & WC consequences of denouncing Carthage / Portugal
        - **Denounce mechanics:** A civilization can denounce another regardless of existing agreements, but doing so will:
          1. **Terminate the Defensive Pact** (if any) and **remove Open Borders**.  
          2. **Cancel the Declaration of Friendship**; the target will immediately become a *Denounced* opponent.  
          3. **Impact World‑Congress voting:** both Carthage (4 delegates) and Portugal (5 delegates) are currently aligned with Austrian proposals. After a denouncement they are likely to vote **against** any future Austrian resolution, reducing the pool of guaranteed YES votes by up to **9 delegates**.  
        - **WC penalties:** No direct “sanction” or resolution penalty is applied for simply denouncing a civ, but loss of their support may make it harder to reach the 45‑delegate threshold for any future proposal.  
        - **Strategic note:** Both civs are still friends; a denouncement would also lower Austria’s overall diplomatic rating with the Freedom‑ideology bloc.
        
        ### 4. India – cultural‑victory timetable & Denmark flip
        - **Data unavailable:** The current game state does not expose a specific “cultural‑victory timer” or the exact turn on which Denmark might switch ideologically or gain the *Cultural Victory** protocol. No relevant information appears in the provided player or WC reports.  
        - **Result:** Unable to verify India’s cultural‑victory progress or a Denmark “flip” date.
        
        ### 5. Potential anti‑India coalition among Freedom civs
        - **Freedom‑ideology civs present:**  
          - **Egypt (Player 0)** – also Freedom; currently at war with Austria and has repeatedly *defeated* Austrian WC proposals. No explicit alliance with India is shown, and Egypt’s opinion of Austria is strongly negative, suggesting possible alignment against India if interests converge.  
          - **Austria** – Freedom, already hostile toward India (denounced, open borders only).  
          - **The Shoshone** – Freedom but already at war with Austria and hostile to India; unlikely to join any coalition with Austria.  
        - **Current stance:** No active coalition against India is recorded; however, Egypt’s ideological match and antagonism toward Austria could make it a candidate for a Freedom‑aligned bloc that opposes India’s Order‑ideology agenda, should diplomatic overtures be made.
        
        ---
        
        **Summary of verification points**
        
        | Question | Answer |
        |----------|--------|
        | 1. Shoshone peace accepted? | Yes – peace was granted on Turn 334; player data still shows “War” pending update. |
        | 2. Carthage/Portugal opinion change? | No – no recent events; opinions remain strongly positive/friendly. |
        | 3. Can we denounce Carthage/Portugal? | Yes – possible, but would dissolve all diplomatic agreements and cost up to 9 WC delegates. |
        | 4. India cultural‑victory timer / Denmark flip? | Information not present in the current reports. |
        | 5. Freedom civs likely to join anti‑India? | Egypt (Freedom) is the only candidate with a potentially antagonistic stance toward India; no coalition formalised yet. |
        
        *End of briefing.*
        
        You, Maria Theresa (leader of Austria, Player 3), are making strategic decisions after turn 335.
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
        - Time Victory: If no one achieves any other victory by the end of the game, the civilization with the highest score wins.
      - Players: summary reports about visible players in the world.
        - You will receive in-game AI's diplomatic evaluations.
        - You will receive each player's publicly available relationships.
        - You will receive the best available location for your next settlement.
      
    - You are Maria Theresa, leader of Austria (Player 3).
      
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
      - Name: Austria
      - Uniques:
        - Unique Unit: Hussar, Replacing Cuirassier (Requires technology: Metallurgy)
        - Unique Unit: Grenzer, Replacing Fusilier (Requires technology: Rifling)
        - Unique Building: Ballhausplatz, Replacing Printing Press (Requires technology: Printing Press)
        - Unique Building: Schützenstand, Replacing Military Academy (Requires technology: Military Science)
        - Civilization Ability: +50% rewards from Quests. May arrange Marriages to City-States with Gold after Allying for 10 Turns. Gain 200 Resting Influence with Married City-States while at peace.
      - Leader: Maria Theresa
      - PlayerID: 3
      
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
      - Replaceable Parts: Allows you to build the Rifleman, a strong Modern-era gunpowder unit.
        Completing it would unlock: Flight, Ballistics
      - Combustion: Allows you to build the Landship, an incredibly powerful armored Unit that can move after attacking, and the Arsenal, which boosts City Strength.
        Completing it would unlock: Ballistics
      - Radio: Allows you to build the Broadcast Tower, a building which greatly increases the Tourism output when themed.
        Completing it would unlock: Refrigeration, Atomic Theory
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      
      ## Policies
      - Economic Union (Level 1 Tenet of Ideology Freedom): Economic Union: Receive two additional Trade Routes. +6 Gold from trade routes with civilizations following Freedom.
      - Creative Expression (Level 1 Tenet of Ideology Freedom): Creative Expression: +2 Tourism from Great Works. Museums, Broadcast Towers, Opera Houses, and Amphitheaters gain +3 Golden Age Points and Culture.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Universal Suffrage (Level 1 Tenet of Ideology Freedom): Universal Suffrage: A Golden Age begins, and Golden Ages last 50% longer. Cities produce +1 Happiness.
      - Free Thought (Continuing Rationalism Branch):
        - * -5 Unhappiness from Religious Unrest in all Cities.
        - * +25% Instant Yields from Great Scientists.
        - * Earn Great Scientists +33% faster.
      - Draft Registration (Level 1 Tenet of Ideology Freedom): Draft Registration: Military Units purchased with Gold receive full XP.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Avant Garde (Level 1 Tenet of Ideology Freedom): Avant Garde: The rate at which Great People are born is increased by 33%. -2 Unhappiness from Boredom in all Cities.
      - Civil Society (Level 1 Tenet of Ideology Freedom): Civil Society: Specialists consume 2 Food less than normal (minimum 1 Food). Farms, Plantations, Camps, and all Unique Improvements produce +4 Food.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
      - Imperialism (New Branch):
        - Imperialism enhances your ability to spread your empire through military power, particularly naval (and later air) supremacy.
        - Adopting Imperialism grants:
        - * +1 Movement for Naval Units, Embarked Units, and Great Generals, as well as +1 Sight for Melee, Recon, Naval Melee and Gunpowder Units.
        - * +10% Production toward Military Units, -10% Gold required for upgrades.
        - Each Imperialism policy unlocked grants:
        - * +5% Production for Military Units, -5% Gold required for upgrades.
        - Adopting all policies in Imperialism grants:
        - * Unlocks building the Pentagon.
        - * All Naval and Air units gain the Banzai! Promotion (become stronger as they take damage).
        - * Allows for the purchase of Great Admirals with Faith starting in the Industrial Era.
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
      - Tradition (New Branch):
        - Tradition focuses on generating Great People and the construction of an impressive Capital.
        - Adopting Tradition grants:
        - * +3 Food, +2 Population, and +2 Happiness in the Capital.
        - * +1 Culture in the Capital for every 2 Citizens.
        - Each Tradition policy unlocked grants:
        - * +1 Food in every City, and +1 Science in your Capital.
        - Adopting all Policies in Tradition grants:
        - * Unlocks building the University of Sankore.
        - * +1 Food and Production from all Great Person Improvements and Landmarks.
        - * Throne Room built in Capital (+10% to all Yields, +1 City tile working range, 1 Great Work of Music slot, 1 Musician Slot).
        - * Allows for the purchase of Great Engineers with Faith starting in the Industrial Era.
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
        - TargetID: 4
        - Public: 50
        - Rationale: Correcting a previous negative modifier. Carthage is our closest ally with a Defensive Pact, Open Borders, and shared goals. We must maximize friendly relations to secure their support.
        - Private: 50
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 50
        - TargetID: 2
        - Private: 50
        - Rationale: Correcting a previous negative modifier. Portugal is our top World Congress ally and trade partner. We need to maintain strong friendly relations to secure their votes and trade.
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: We need to end the war with Egypt to focus entirely on the existential threat from India. Increasing our friendly stance will improve peace acceptance.
        - Private: 40
        - TargetID: 0
        - Public: 40
    - #3:
      - toolName: set-research
      - args:
        - Technology: Radio
        - Rationale: Unlocking Radio is critical to build Broadcast Towers for cultural defense and progress towards Atomic Theory and nuclear weaponry to counter India's massive army.
    - #4:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought will significantly boost our Science output and Great Scientist generation, allowing us to catch up to India's tech lead.
        - Policy: Free Thought
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - UseNuke: 90
          - Gold: 70
          - Espionage: 70
          - Nuke: 90
          - Infrastructure: 60
          - Culture: 40
          - Antiair: 70
          - Airlift: 70
          - Offense: 80
          - Mobilization: 100
          - Science: 80
          - Air: 70
          - Diplomacy: 70
          - Production: 90
          - Defense: 70
          - Ranged: 80
          - Growth: 60
          - Mobile: 60
        - GrandStrategy: Conquest
      - rationale: Prioritizing Science to catch up technologically and Diplomacy to leverage Austria's marriage ability and gain City-State delegates. Mobilization, Production, and Nuke capabilities remain heavily prioritized to prepare for a decisive war against India.
  - tokens:
    - inputTokens: 23002
    - reasoningTokens: 7282
    - outputTokens: 383
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Turn**
            
            My current turn is 335, and I'm in third place with a score of 1591. India leads significantly at 2580, followed by Denmark. I need to assess our strategic options and any relevant reports to improve my standing.
            
            **Evaluating Research Paths**
            
            I'm re-evaluating our research trajectory. Plastics is still 21 turns out, and while Replaceable Parts is the strategic target, I'm verifying if switching to Combustion, Radio, or Penicillin now would be more beneficial given the current game state.
            
            **Reviewing Research Progress**
            
            I'm double-checking our current research focus. It appears we've shifted to Plastics, with an estimated completion in 21 turns. I'm now considering if switching to Replaceable Parts, Combustion, Radio, or Penicillin would be a better immediate move.
            
            **Detecting Victory Condition**
            
            An extreme emergency! India is one turn from being Influential with Denmark, and if they've completed Citizen Earth Protocol and adopted two Tier 3 tenets, they win. I'm frantically checking their policies and researching ways to disrupt their victory.
            
            **Assessing Diplomatic Angles**
            
            I'm reassessing our diplomatic stance. Despite being at peace with India, their impending victory condition forces me to consider war to disrupt their tourism multipliers. The current situation regarding the Shoshone's peace status and my relationships with other civs are key variables.
            
            **Considering Diplomatic Leverage**
            
            I'm analyzing the upcoming World Congress vote. India has proposed sanctions against Egypt, but I've also proposed sanctions against the Shoshone, whom we are about to make peace with. This presents a complex diplomatic situation. India's significant delegate count is also a factor in how this vote will play out.
            
            **Analyzing India's War Stance**
            
            I'm reviewing our hostile stance towards India. Despite the conflict, a formal declaration of war hasn't occurred, likely due to our military disparity and prior commitments. With the Shoshone peace finalized, my focus is shifting to India, exploring options to involve other civs in a conflict or directly engage them. Egypt and Shoshone are already at war with India, which presents an opportunity.
            
            **Preparing for War**
            
            My attention is now focused on India's imminent cultural victory. They're one turn from influencing Denmark, which would grant them global cultural dominance. Given our proximity and their overwhelming strength, I'm prioritizing military mobilization and re-evaluating our Conquest grand strategy to counter this threat.
            
            **Switching Research Priority**
            
            I'm rerouting our research focus. While Plastics is nearing completion, I've identified Radio as the critical next step. This will unlock Atomic Theory, crucial for our nuclear capabilities, and potentially boost our tourism, making it a more valuable immediate pursuit.
            
            **Prioritizing Radio Research**
            
            I've decided to prioritize researching Radio. This will unlock crucial technologies like Atomic Theory, which is vital for developing nuclear capabilities. I believe this offensive strategy, utilizing nukes, is our best bet to counter India's overwhelming military strength and impending victory.
            
            **Evaluating Policy Options**
            
            I am assessing our available policies within the Rationalism tree. Free Thought appears particularly potent, offering significant boosts to scientist yields and generation speed, which could accelerate our scientific advancement and help counter India's progress.
            
            **Considering Policy Impact**
            
            I am reassessing our policy choices. While Free Thought from Rationalism offers scientific acceleration, I'm now questioning if a military-focused policy within Freedom, like Draft Registration, would be more prudent given India's overwhelming strength. I'm trying to determine the most impactful way to counter their cultural victory.
            
            **Prioritizing Science**
            
            I'm continuing to prioritize science, opting for Free Thought in Rationalism to boost our Great Scientist generation. This will accelerate our path to critical modern and atomic military technologies, particularly nukes, which are essential to counter India's significant cultural advantage and aggressive tourism output.
            
            **Seeking Peace with Egypt**
            
            I'm actively working to de-escalate the conflict with Egypt. Their widespread wars offer an opportunity for peace, which would allow me to redirect my forces toward our primary threat, India. My current focus is on improving our diplomatic standing with Egypt to facilitate a peace treaty.
            
            **Revising Diplomatic Strategies**
            
            I'm reassessing my approach to Carthage. Despite their current friendship and pacts, my established strategy set them as a negative relationship target. I'm trying to understand the previous rationale for this and determine if it's still relevant or if a shift to a more positive stance is needed now.
            
            **Adjusting Diplomacy Settings**
            
            I am re-evaluating our diplomatic relationship modifiers. I've decided to set our modifiers for Carthage and Portugal to positive values to solidify our alliances and ensure their World Congress support. I am also reviewing our seemingly contradictory high positive modifiers for the Shoshone, considering our recent conflict.
            
            **Refining Diplomatic Stance**
            
            I am solidifying our diplomatic posture. India remains our primary hostile focus, maintaining negative relations, while I am actively cultivating positive ties with Carthage and Portugal for potential alliances and trade. The contradictory positive modifiers with the Shoshone, despite our recent conflict, warrant further review.
            
            **Optimizing Persona and Flavors**
            
            I've confirmed our persona and flavors are well-aligned for this high-stakes endgame. Our aggressive, competitive, and warlike settings, coupled with a strong emphasis on offense, mobilization, and nukes, are crucial for countering India's imminent victory.
            
            **Considering Military Alliances**
            
            I'm exploring potential military alliances. With India as our sole hostile target and strong positive modifiers for Carthage and Portugal, I'm considering if formal alliances with them would be beneficial to mount a concerted effort against India.
            
            **Developing Offensive Strategies**
            
            I am focusing on offensive capabilities. My current research and policy choices are geared towards maximizing our scientific and production output, particularly concerning nuclear technology, to directly counter India's overwhelming military and impending cultural victory.
            
            **Adjusting Research Focus**
            
            I'm re-evaluating our flavor settings. While production and air superiority remain key, I'm increasing science flavor to 80 to close our technological gap with India. I'm also considering the diplomatic benefits of city-state alliances for Austria.
            
            **Setting Diplomatic and Research Goals**
            
            I am fine-tuning our diplomatic and research priorities. I'm pushing for peace with Egypt and solidifying alliances with Carthage and Portugal by setting positive diplomatic modifiers. Researching Radio is now critical for Broadcast Towers and advancing toward nukes. I'm maintaining Free Thought for science and adjusting overall flavors towards science and diplomacy.
            
            **Verifying Strategic Parameters**
            
            I'm confirming the policy choices, and yes, "Free Thought" is indeed a viable option. I'm also double-checking the arguments for `set-flavors`, ensuring science, diplomacy, and offensive capabilities are prioritized, while refining other flavor settings. I'm also reviewing our relationship modifiers with India to ensure alignment with our aggressive strategy.
            
            **Adjusting Diplomatic Relations**
            
            I'm finalizing adjustments to our diplomatic relationships. India's hostility is already maxed out, so no changes there. I'm significantly boosting our public and private modifiers for Carthage and Portugal to solidify alliances, and also increasing Egypt's modifiers to facilitate a peace treaty and refocus on India.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 2PQhqTyKH6k184rF
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Public: 50
            - Rationale: Correcting a previous negative modifier. Carthage is our closest ally with a Defensive Pact, Open Borders, and shared goals. We must maximize friendly relations to secure their support.
            - Private: 50
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: SmnemZO4dLVpNbcY
          - toolName: set-relationship
          - input:
            - Public: 50
            - TargetID: 2
            - Private: 50
            - Rationale: Correcting a previous negative modifier. Portugal is our top World Congress ally and trade partner. We need to maintain strong friendly relations to secure their votes and trade.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Cay40yjaav29KdfE
          - toolName: set-relationship
          - input:
            - Rationale: We need to end the war with Egypt to focus entirely on the existential threat from India. Increasing our friendly stance will improve peace acceptance.
            - Private: 40
            - TargetID: 0
            - Public: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: IYIKCExQfKxPkHB2
          - toolName: set-research
          - input:
            - Technology: Radio
            - Rationale: Unlocking Radio is critical to build Broadcast Towers for cultural defense and progress towards Atomic Theory and nuclear weaponry to counter India's massive army.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: VNDC0TAWimpwUv5S
          - toolName: set-policy
          - input:
            - Rationale: Free Thought will significantly boost our Science output and Great Scientist generation, allowing us to catch up to India's tech lead.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: qFqnvx6aDgmcTB1J
          - toolName: set-flavors
          - input:
            - Flavors:
              - UseNuke: 90
              - Gold: 70
              - Espionage: 70
              - Nuke: 90
              - Infrastructure: 60
              - Culture: 40
              - Antiair: 70
              - Airlift: 70
              - Offense: 80
              - Mobilization: 100
              - Science: 80
              - Air: 70
              - Diplomacy: 70
              - Production: 90
              - Defense: 70
              - Ranged: 80
              - Growth: 60
              - Mobile: 60
            - Rationale: Prioritizing Science to catch up technologically and Diplomacy to leverage Austria's marriage ability and gain City-State delegates. Mobilization, Production, and Nuke capabilities remain heavily prioritized to prepare for a decisive war against India.
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 2PQhqTyKH6k184rF
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
          - toolCallId: SmnemZO4dLVpNbcY
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Cay40yjaav29KdfE
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: IYIKCExQfKxPkHB2
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: VNDC0TAWimpwUv5S
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: qFqnvx6aDgmcTB1J
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.