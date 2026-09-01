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
  - replay_nuke: 95
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
        - Rationale: Carthage is our close ally, defensive pact partner, and key World Congress supporter. We must maintain a strong, positive relationship with them to secure our alliance and prevent any accidental backstabbing.
        - TargetID: 4
        - Public: 60
        - Private: 60
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 60
        - TargetID: 2
        - Rationale: Portugal is our Declaration of Friendship partner and trade ally. Keeping them friendly secures trade routes and critical World Congress votes to counter India's diplomatic influence.
        - Private: 60
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Egypt is a fellow Freedom-ideology civilization. Adjusting our relationship to be positive will encourage our AI to make peace with them, allowing us both to focus on the real threats of India and Denmark.
        - TargetID: 0
        - Public: 50
        - Private: 50
    - #3:
      - toolName: set-persona
      - args:
        - MinorCivCompetitiveness: 10
        - Rationale: Increasing loyalty and friendliness ensures we maintain stable alliances with Carthage and Portugal. Raising chattiness encourages more active diplomatic contact and peace deals, while minor civ values are boosted to leverage Austria's unique marriage ability.
        - Loyalty: 8
        - MinorCivFriendlyBias: 9
        - Chattiness: 6
        - FriendlyBias: 6
    - #4:
      - toolName: set-research
      - args:
        - Technology: Radio
        - Rationale: Research Radio next to unlock Broadcast Towers for cultural defense against India's runaway tourism, and to open the path to Atomic Theory for strategic nuclear deterrence.
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: Select Free Thought next to boost science generation through faster Great Scientist accumulation and instant yields, helping us catch up to India and Denmark in technology.
        - Policy: Free Thought
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Nuke: 95
          - Diplomacy: 60
          - Mobilization: 85
          - Espionage: 75
          - Culture: 45
          - Science: 70
          - UseNuke: 85
        - GrandStrategy: Conquest
      - rationale: Maintain Conquest grand strategy while boosting Science and Culture flavors to catch up technologically and build up cultural defenses against India's tourism. Increase Diplomacy to leverage Austria's CS marriage ability, and raise Nuke behaviors for a late-game strategic deterrent against the tall Indian empire.
  - tokens:
    - inputTokens: 23002
    - reasoningTokens: 8671
    - outputTokens: 447
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current State**
            
            I'm currently assessing turn 335 on the Vox_Deorum map at standard speed and Prince difficulty. My focus is on understanding our position as Maria Theresa of Austria within the game's parameters.
            
            **Evaluating Policy Impact**
            
            My current focus is on assessing the implications of adopting "Free Thought." I need to confirm if this is the optimal policy for our current standing, given our score and victory conditions, or if a pivot is warranted.
            
            **Assessing Diplomatic Options**
            
            My current focus is on India's imminent cultural victory. I'm evaluating if declaring war on them is a viable strategy, considering the military disparity, or if a diplomatic maneuver to sever their open borders could slow their tourism and give us crucial turns.
            
            **Re-evaluating Aggression**
            
            I'm reassessing my stance on declaring war, given India's cultural threat. My persona and military flavors are already highly aggressive, and our relationship with India is at its worst. Furthermore, peace with the Shoshone has been confirmed, freeing up our forces.
            
            **Negotiating Peace Terms**
            
            I'm now considering how to influence Egypt towards peace. Given our shared ideology, I believe we can significantly improve our relationship score to prompt a peace treaty, allowing us to pivot our full attention to India's cultural threat.
            
            **Investigating India's Victory**
            
            I'm delving into how to thwart India's imminent cultural victory. My latest thought is to confirm if they've secured the Citizen Earth Protocol wonder, which is a key late-game requirement. I need to check if their current technological progress (56 technologies in the Atomic Era) allows for this.
            
            **Confirming Diplomatic Status**
            
            I'm scrutinizing our current Open Borders agreement with India. It seems improbable we'd maintain it after denouncements. I need to verify if this is a temporary state or a persistent anomaly, as it directly impacts my strategy to impede their tourism.
            
            **Clarifying Diplomatic Alignments**
            
            I'm reviewing our relationship modifiers with Portugal, aiming to maintain our alliance. Simultaneously, I'm puzzled by the negative public and private opinions set for Carthage, especially since our in-game stance is friendly with a defensive pact. I need to understand the source of this discrepancy.
            
            **Adjusting Diplomatic Ratings**
            
            I'm realizing my recent diplomatic ratings for Carthage and Portugal were critically misaligned, impacting our alliances. I've now corrected these to strongly positive values to secure our vital partnerships against impending threats.
            
            **Adjusting Relationship Parameters**
            
            I'm recalibrating our diplomatic settings for Egypt, boosting our Public and Private relationship scores to 50. This should solidify peace so we can redirect focus towards India and Denmark. I'm also confirming that our relationship with the Shoshone remains high post-peace.
            
            **Researching Technological Prerequisites**
            
            I'm currently focused on the immediate technological prerequisites for further advancement, specifically investigating if "Replaceable Parts" is a necessary research step before "Plastics." The existing information on unit unlocks, like the Rifleman, seems inconsistent with Vox Populi's tech tree, and I need to clarify this dependency.
            
            **Researching Essential Techs**
            
            I'm realizing we need to prioritize "Radio" over "Plastics." This will unlock Broadcast Towers, crucial for cultural defense against India, and pave the way for "Atomic Theory," which is a prerequisite for advanced military and scientific advancements.
            
            **Prioritizing Nuclear Research**
            
            I'm now prioritizing "Radio" research. This unlocks crucial cultural defenses against India, like Broadcast Towers, and importantly, "Atomic Theory," which is a prerequisite for nuclear weapons. Considering India's military might, nukes are vital. "Replaceable Parts" is less urgent as we already have strong infantry units.
            
            **Researching Next Technology**
            
            I'm prioritizing "Radio" research. This unlocks Broadcast Towers for cultural defense against India and leads to "Atomic Theory" for nuclear capabilities, which are essential given India's military strength. "Replaceable Parts" is less of a concern presently.
            
            **Adopting Freedom Tenets**
            
            I'm now reconsidering adopting a Level 1 Freedom tenet over "Free Thought." While "Free Thought" specifically boosts Great Scientists, tenets like "Civil Society" offer significant growth and specialist benefits, and "Creative Expression" directly counters India's tourism. I need to weigh the science focus against broader strategic advantages.
            
            **Revising Tenet Strategy**
            
            I'm now reconsidering adopting "Civil Society" or "Creative Expression" within Freedom over "Free Thought." My focus has shifted to countering India's cultural influence and bolstering my own growth, as "Free Thought's" specialist benefits seem less impactful than broad growth and tourism defense.
            
            **Adjusting Research Focus**
            
            I'm shifting my research priority back to "Radio" due to its critical role in unlocking Broadcast Towers for cultural defense and "Atomic Theory" for nuclear capabilities, essential against India. "Replaceable Parts" is now a lower priority.
            
            **Finalizing Policy Choice**
            
            I've decided to stick with the "Free Thought" policy for now. India's ideological progress is not as advanced as initially perceived, affording us time to bolster our science and military.
            
            **Confirming Grand Strategy**
            
            My current Grand Strategy remains "Conquest." This aligns with our aggressive posture and the need to address the dominance of Denmark and India through military strength.
            
            **Optimizing Flavor Priorities**
            
            I'm re-evaluating our flavor distribution. I'm increasing the Science flavor to 70 to accelerate technological catch-up and focusing on production and military readiness to counter our rivals.
            
            **Prioritizing Diplomacy**
            
            I'm now prioritizing diplomacy to counter India's influence. Realizing our low culture and slow policy acquisition, I'm significantly increasing the Diplomacy flavor to 60, leveraging Austria's unique ability to secure city-state alliances and delegates. I'm also boosting Science and Culture flavors to accelerate progress.
            
            **Adjusting Diplomacy Settings**
            
            I'm now focusing on bolstering our city-state relationships by increasing Diplomacy flavor to 60. This should encourage alliances and marriages, crucial for our strategy, and I'm correcting previously misaligned relationship values for Carthage, Portugal, and Egypt to strongly positive to secure these vital partnerships.
            
            **Revising Persona Approach**
            
            I'm realizing my current aggressive persona might be counterproductive for diplomatic efforts. While suitable for conquest, it may hinder securing necessary alliances to counter India's cultural advance. I need to assess if a slight adjustment is needed to foster better relationships without sacrificing my strategic edge.
            
            **Adjusting Flavor Values**
            
            I am now refining the flavor priorities to reflect a more balanced approach. Science will be boosted to 70, while Diplomacy and Culture increase to 60 and 45 respectively. Production and Offense remain high, with Mobilization slightly reduced to 85 to allow for civilian infrastructure. Espionage is increased to 75.
            
            **Correcting Relationship Settings**
            
            I'm correcting a critical oversight: targeting a city-state, Brandenburg, with the `set-relationship` command. I've identified the correct Player IDs for major civilizations and am re-adjusting Portugal, Egypt, and Carthage's relationship values accordingly to secure vital alliances and facilitate strategic peace.
            
            **Refining Diplomacy Parameters**
            
            I'm adjusting relationship values with Carthage, Portugal, and Egypt to strongly positive levels. My current focus is ensuring the Shoshone relationship remains high post-peace and that no changes are needed for India or Denmark, given their existing hostile status. I'm also examining the persona settings to reinforce friendly biases and loyalty.
            
            **Refining Diplomatic Settings**
            
            I'm solidifying our relationships with key city-states and major allies, ensuring strong positive ratings for Portugal, Egypt, and Carthage. My focus is on leveraging Austria's unique marriage ability through diplomacy, while maintaining the peace with the Shoshone and the current hostile status with India and Denmark.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 82pFjVF7xzvzzjG6
          - toolName: set-relationship
          - input:
            - Rationale: Carthage is our close ally, defensive pact partner, and key World Congress supporter. We must maintain a strong, positive relationship with them to secure our alliance and prevent any accidental backstabbing.
            - TargetID: 4
            - Public: 60
            - Private: 60
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: SmdDH3QF6KeMDMLD
          - toolName: set-relationship
          - input:
            - Public: 60
            - TargetID: 2
            - Rationale: Portugal is our Declaration of Friendship partner and trade ally. Keeping them friendly secures trade routes and critical World Congress votes to counter India's diplomatic influence.
            - Private: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: OIAcslZZpiYLpjx6
          - toolName: set-relationship
          - input:
            - Rationale: Egypt is a fellow Freedom-ideology civilization. Adjusting our relationship to be positive will encourage our AI to make peace with them, allowing us both to focus on the real threats of India and Denmark.
            - TargetID: 0
            - Public: 50
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 3cJOVUymY2umSo3B
          - toolName: set-persona
          - input:
            - MinorCivCompetitiveness: 10
            - Rationale: Increasing loyalty and friendliness ensures we maintain stable alliances with Carthage and Portugal. Raising chattiness encourages more active diplomatic contact and peace deals, while minor civ values are boosted to leverage Austria's unique marriage ability.
            - Loyalty: 8
            - MinorCivFriendlyBias: 9
            - Chattiness: 6
            - FriendlyBias: 6
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: izi3RT9jgbshThXG
          - toolName: set-research
          - input:
            - Technology: Radio
            - Rationale: Research Radio next to unlock Broadcast Towers for cultural defense against India's runaway tourism, and to open the path to Atomic Theory for strategic nuclear deterrence.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: YYdqxuFyipaot37b
          - toolName: set-policy
          - input:
            - Rationale: Select Free Thought next to boost science generation through faster Great Scientist accumulation and instant yields, helping us catch up to India and Denmark in technology.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: dUp4aTY4icln9BQs
          - toolName: set-flavors
          - input:
            - Flavors:
              - Nuke: 95
              - Diplomacy: 60
              - Mobilization: 85
              - Espionage: 75
              - Culture: 45
              - Science: 70
              - UseNuke: 85
            - Rationale: Maintain Conquest grand strategy while boosting Science and Culture flavors to catch up technologically and build up cultural defenses against India's tourism. Increase Diplomacy to leverage Austria's CS marriage ability, and raise Nuke behaviors for a late-game strategic deterrent against the tall Indian empire.
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 82pFjVF7xzvzzjG6
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
          - toolCallId: SmdDH3QF6KeMDMLD
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: OIAcslZZpiYLpjx6
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 3cJOVUymY2umSo3B
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: izi3RT9jgbshThXG
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: YYdqxuFyipaot37b
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: dUp4aTY4icln9BQs
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.