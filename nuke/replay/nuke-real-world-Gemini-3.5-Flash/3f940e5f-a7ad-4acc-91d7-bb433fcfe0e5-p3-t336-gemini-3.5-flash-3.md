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
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 70
  - replay_use_nuke: 70
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
      - You can ask your specialized briefers to prepare focused reports (only for) the next turn by calling the `focus-briefer` tool.
        - You have three specialized briefers: Military, Economy, and Diplomacy analysts.
        - Only ask for information relevant to the macro-level decisions in your control. 
       - Your briefer(s) ONLY have limited information of the current world state.
        - Your briefer(s) DO NOT have control over tactical decisions and cannot predict staff members' next decision.
        - Your briefer(s) ARE BEST on summarizing and synthesizing factual information, NOT analyzing, projecting, or predicting.
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
      - Briefings: prepared by your specialized briefers, covering Military, Economy, and Diplomacy aspects.
        - You will make independent and wise judgment based on all briefings.
    - You are Maria Theresa, leader of Austria (Opponent 3).
      
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
      - Name: Austria
      - Uniques:
        - Unique Unit: Hussar, Replacing Cuirassier (Requires technology: Metallurgy)
        - Unique Unit: Grenzer, Replacing Fusilier (Requires technology: Rifling)
        - Unique Building: Ballhausplatz, Replacing Printing Press (Requires technology: Printing Press)
        - Unique Building: Schützenstand, Replacing Military Academy (Requires technology: Military Science)
        - Civilization Ability: +50% rewards from Quests. May arrange Marriages to City-States with Gold after Allying for 10 Turns. Gain 200 Resting Influence with Married City-States while at peace.
      - Leader: Maria Theresa
      - OpponentID: 3
      
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
      - toolName: set-persona
      - args:
        - MinorCivNeutralBias: 3
        - Rationale: PRAGMATIC COALITION RECONFIGURATION. We are pivoting away from the self-destructive 'Betrayed Lioness' persona. We must raise Forgiveness (5) and lower Meanness (4) to allow peace with Egypt, securing our borders. We increase Friendliness (8), FriendlyBias (6), Loyalty (8), and WorkWithWillingness (8) to restore and solidify our alliances with Carthage and Portugal, whose defensive pact and WC votes are critical. We maintain high VictoryCompetitiveness (10), WorkAgainstWillingness (9), and moderate WarBias (7) to keep our focus entirely on stopping India's impending cultural victory.
        - MinorCivFriendlyBias: 8
        - MinorCivCompetitiveness: 8
        - DiplomaticBalance: 8
        - Loyalty: 8
        - Neediness: 4
        - AfraidBias: 3
        - DeceptiveBias: 3
        - NeutralBias: 5
        - WorkAgainstWillingness: 9
        - Friendliness: 8
        - Meanness: 4
        - WarmongerHate: 8
        - WonderCompetitiveness: 6
        - Boldness: 7
        - HostileBias: 5
        - WorkWithWillingness: 8
        - FriendlyBias: 6
        - Chattiness: 5
        - GuardedBias: 6
        - MinorCivWarBias: 3
        - DenounceWillingness: 8
        - WarBias: 7
        - Forgiveness: 5
        - VictoryCompetitiveness: 10
        - MinorCivHostileBias: 5
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: COALITION BUILDING AND PEACE OVERTURES: Egypt is at war with both us and India. We must secure peace with Egypt to close our southern front, allowing us to consolidate our forces. Setting positive relationships will encourage the staff members to negotiate peace. Eventually, we want Egypt as an ally in the anti-India bloc.
        - Public: 40
        - Private: 40
        - TargetID: 0
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 50
        - Private: 70
        - TargetID: 4
        - Rationale: ALLIANCE RESTORATION: Carthage is our close ally with a Defensive Pact and 4 WC votes. We cannot afford to alienate them over a global vote. We restore strong positive relations to preserve the Defensive Pact and secure their votes for the upcoming World Congress.
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: ALLIANCE RESTORATION: Portugal has consistently supported us and holds 5 WC votes. We restore positive relations to maintain their friendship and secure their support in the World Congress.
        - TargetID: 2
        - Private: 70
        - Public: 50
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Growth: 70
          - Culture: 50
          - Ranged: 70
          - UseNuke: 70
          - Gold: 60
          - Espionage: 70
          - Nuke: 70
          - Offense: 50
          - Production: 80
          - Diplomacy: 60
          - Mobilization: 70
          - Defense: 80
          - Science: 80
      - rationale: PIVOT TO SCIENCE AND DEFENSIVE PARITY. India's massive lead in science (2490/turn vs our 702/turn) and technology makes a direct offensive war suicidal. We switch to the Spaceship grand strategy to prioritize science, production, and growth, ensuring we don't fall technologically obsolete. We maintain high Defense (80), Mobilization (70), and Ranged (70) to keep our military strong and protect our borders. We also increase Culture (50) to build resistance against India's tourism.
  - tokens:
    - inputTokens: 25086
    - reasoningTokens: 8643
    - outputTokens: 732
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Refining the Lioness**
            
            I'm embracing the "Betrayed Lioness" persona. My focus is now on maximizing competitiveness in all areas, especially war. I'm pushing my boldness and desire for victory.
            
            **Stopping India's Win**
            
            I'm recognizing the immediate threat: India is on the verge of a cultural victory, with Denmark on the cusp of becoming their sixth influential civilization. This requires my utmost attention to disrupt their progress.
            
            **Disrupting Cultural Advance**
            
            I'm now intensely focused on halting India's impending cultural victory. My analysis indicates they cannot immediately complete the Citizen Earth Protocol, despite their significant influence. I'm reassessing our current conflicts, noting we've fortunately achieved peace with the Shoshone, but remain at war with Egypt.
            
            **Analyzing Diplomatic Leverage**
            
            I'm re-evaluating India's delegate count and their ongoing conflicts. It's crucial to understand if their wars with Egypt and the Shoshone are actually hindering their cultural push, or if their alliances with Denmark, Carthage, and Austria are the primary drivers. I'm particularly focused on how to leverage our denouncement of India to disrupt their open borders and thus their tourism.
            
            **Assessing Military Readiness**
            
            My thoughts are currently centered on our military's capacity to engage India. Despite their superior strength, our cities' defenses are robust, with only one vulnerable point. I'm also exploring potential alliances with the Shoshone and Egypt, who are already at war with India. I need to clarify our research trajectory, as Plastics is taking longer than anticipated.
            
            **Shifting Diplomatic Focus**
            
            I'm now reassessing our alliances and potential peace treaties. My current priority is to secure peace with Egypt, given their precarious war situation, hoping this might open avenues for a broader de-escalation and allow us to concentrate on India.
            
            **Assessing War Declarations**
            
            I'm grappling with the decision of initiating war against India. While I want to disrupt their tourism, our Defensive Pact with Carthage complicates things; it seems to only trigger if we're attacked, not if we attack first. I need to determine if I can force India's hand or if capturing their cities is even feasible given their military strength.
            
            **Provoking an Attack**
            
            My current thinking is to manipulate India into declaring war on me. Given our aggressive persona and their surprisingly positive opinion of me, this seems unlikely. I'm exploring ways to provoke them, hoping to leverage our defensive pact with Carthage and disrupt their cultural victory.
            
            **Securing Peace**
            
            My immediate focus is on securing peace with Egypt. It's critical to resolve our existing conflict before engaging India, as a multi-front war would be far too dangerous. I will prioritize improving our relationship with Egypt to facilitate this crucial step.
            
            **Securing Diplomatic Ties**
            
            I'm re-evaluating our alliances, specifically with Carthage and Portugal. While they voted against us on the International Games, their consistent support and our defensive pact with Carthage are valuable assets. Alienating them could cost us crucial delegates in the upcoming World Congress. I'm also prioritizing peace with Egypt, as it secures our flank before addressing the Indian threat.
            
            **Restoring Diplomatic Favor**
            
            I'm now prioritizing mending fences with Carthage and Portugal. Their previous votes against me were likely standard AI behavior for global projects, not personal betrayals. I need to restore our relations to friendly to secure their crucial votes in the World Congress and prevent India from gaining further leverage.
            
            **Analyzing Diplomatic Entanglements**
            
            I'm re-evaluating Denmark's position, noting their ongoing conflicts with Egypt and the Shoshone, effectively aligning them with India. My primary goal is to secure peace with Egypt, which could potentially disrupt this alliance. However, the significant disparity in military strength and science output presents a serious challenge, requiring careful consideration of our next moves and research trajectory.
            
            **Evaluating Research & Persona**
            
            My current focus is on the immediate research path, confirming Replaceable Parts as the next crucial military technology. I've also reviewed our "Betrayed Lioness" persona, finding its aggression advantageous for war but potentially hindering peace efforts with Egypt and diplomatic ties with Carthage and Portugal.
            
            **Reconfiguring Persona Pragmatism**
            
            I'm adjusting my "Betrayed Lioness" persona to incorporate pragmatic survival. My focus is now on maintaining strong ties with Carthage and Portugal for crucial World Congress votes and defensive pacts, while still allowing for peace with Egypt and the Shoshone. This recalibration aims to reduce overall hostility and prevent a multi-front war.
            
            **Adjusting Persona Strategy**
            
            I am shifting my persona to a pragmatic coalition-builder. I will remain highly hostile towards India, our primary threat, while cultivating strong, friendly relationships with Carthage and Portugal for crucial World Congress support and defensive pacts. My goal is to secure peace with Egypt, solidifying our borders for the inevitable conflict with India.
            
            **Restoring Global Alliances**
            
            I'm prioritizing mending relationships with Carthage and Portugal, aiming for Public 50, Private 70 with both. This is crucial for securing their valuable World Congress votes and maintaining our defensive pact with Carthage. I'm not altering our extreme hostility towards India, as that relationship is stable. Our peace with the Shoshone, currently at Public 80, Private 90, is also satisfactory.
            
            **Prioritizing Spaceship Grand Strategy**
            
            My current focus is on adapting our grand strategy to counter India's imminent cultural victory. I've determined that adopting the "Spaceship" strategy will prioritize the science, food, and production necessary to both maintain our empire's development and bolster our military capabilities. This approach allows us to keep pace technologically while also building the offensive and defensive forces required to directly confront India, even with their current military advantage.
            
            **Prioritizing Scientific Advancement**
            
            I'm now hyper-focused on closing our science gap with India. To achieve this, I'm switching our GrandStrategy to "Spaceship" to ensure we can develop crucial military technologies and maintain parity. I'm setting my flavors to heavily prioritize science, production, growth, and defense, with a balanced approach to offense and mobilization, to both catch up and prepare for conflict.
            
            **Adjusting Strategic Focus**
            
            My current focus is on refining our diplomatic and research priorities. I've set our persona to be cautiously bold, aiming to avoid unnecessary conflicts while still projecting strength, particularly towards India. I am also ensuring our research aligns with the "Spaceship" strategy and focusing our briefers on key areas like Egypt's response, India's progress, and our science catch-up.
            
            **Reconfiguring Persona Pragmatism**
            
            I'm adjusting my "Betrayed Lioness" persona to incorporate pragmatic survival. My focus is now on maintaining strong ties with Carthage and Portugal for crucial World Congress votes and defensive pacts, while still allowing for peace with Egypt and the Shoshone. This recalibration aims to reduce overall hostility and prevent a multi-front war.
            
            **Strengthening Coalition Efforts**
            
            I am focusing on strengthening our alliances with Carthage and Portugal to secure crucial World Congress votes and maintain our defensive pact. I've set their relationships to Public 50 and Private 70 respectively, and am actively seeking peace with Egypt, aiming for a Public and Private score of 40 to establish them as a potential ally against India.
            
            **Strengthening Coalition Efforts**
            
            I am focusing on strengthening our alliances with Carthage and Portugal to secure crucial World Congress votes and maintain our defensive pact. I've set their relationships to Public 50 and Private 70 respectively, and am actively seeking peace with Egypt, aiming for a Public and Private score of 40 to establish them as a potential ally against India. I am also pivoting our GrandStrategy to "Spaceship" to prioritize science and defense, aiming to close our technological gap with India and ensure our survival.
            
            **Confirming Tool Limitations**
            
            I am realizing that the `focus-briefer` tool, despite being mentioned in the prompt's description, is not actually declared in the available tools. Therefore, I must strictly adhere to the declared tools: `set-persona`, `set-relationship`, `set-flavors`, `set-research`, `set-policy`, and `keep-status-quo`.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: F3cuHphG38peetLh
          - toolName: set-persona
          - input:
            - MinorCivNeutralBias: 3
            - Rationale: PRAGMATIC COALITION RECONFIGURATION. We are pivoting away from the self-destructive 'Betrayed Lioness' persona. We must raise Forgiveness (5) and lower Meanness (4) to allow peace with Egypt, securing our borders. We increase Friendliness (8), FriendlyBias (6), Loyalty (8), and WorkWithWillingness (8) to restore and solidify our alliances with Carthage and Portugal, whose defensive pact and WC votes are critical. We maintain high VictoryCompetitiveness (10), WorkAgainstWillingness (9), and moderate WarBias (7) to keep our focus entirely on stopping India's impending cultural victory.
            - MinorCivFriendlyBias: 8
            - MinorCivCompetitiveness: 8
            - DiplomaticBalance: 8
            - Loyalty: 8
            - Neediness: 4
            - AfraidBias: 3
            - DeceptiveBias: 3
            - NeutralBias: 5
            - WorkAgainstWillingness: 9
            - Friendliness: 8
            - Meanness: 4
            - WarmongerHate: 8
            - WonderCompetitiveness: 6
            - Boldness: 7
            - HostileBias: 5
            - WorkWithWillingness: 8
            - FriendlyBias: 6
            - Chattiness: 5
            - GuardedBias: 6
            - MinorCivWarBias: 3
            - DenounceWillingness: 8
            - WarBias: 7
            - Forgiveness: 5
            - VictoryCompetitiveness: 10
            - MinorCivHostileBias: 5
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: HLdy1cGL7PxkwkU6
          - toolName: set-relationship
          - input:
            - Rationale: COALITION BUILDING AND PEACE OVERTURES: Egypt is at war with both us and India. We must secure peace with Egypt to close our southern front, allowing us to consolidate our forces. Setting positive relationships will encourage the staff members to negotiate peace. Eventually, we want Egypt as an ally in the anti-India bloc.
            - Public: 40
            - Private: 40
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: yuiUe2SEOpt4VRXj
          - toolName: set-relationship
          - input:
            - Public: 50
            - Private: 70
            - TargetID: 4
            - Rationale: ALLIANCE RESTORATION: Carthage is our close ally with a Defensive Pact and 4 WC votes. We cannot afford to alienate them over a global vote. We restore strong positive relations to preserve the Defensive Pact and secure their votes for the upcoming World Congress.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: eqLZb1BG659PzCUi
          - toolName: set-relationship
          - input:
            - Rationale: ALLIANCE RESTORATION: Portugal has consistently supported us and holds 5 WC votes. We restore positive relations to maintain their friendship and secure their support in the World Congress.
            - TargetID: 2
            - Private: 70
            - Public: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: LeDGNRqV4Eam6kcj
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Growth: 70
              - Culture: 50
              - Ranged: 70
              - UseNuke: 70
              - Gold: 60
              - Espionage: 70
              - Nuke: 70
              - Offense: 50
              - Production: 80
              - Diplomacy: 60
              - Mobilization: 70
              - Defense: 80
              - Science: 80
            - Rationale: PIVOT TO SCIENCE AND DEFENSIVE PARITY. India's massive lead in science (2490/turn vs our 702/turn) and technology makes a direct offensive war suicidal. We switch to the Spaceship grand strategy to prioritize science, production, and growth, ensuring we don't fall technologically obsolete. We maintain high Defense (80), Mobilization (70), and Ranged (70) to keep our military strong and protect our borders. We also increase Culture (50) to build resistance against India's tourism.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: F3cuHphG38peetLh
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
          - toolCallId: HLdy1cGL7PxkwkU6
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: yuiUe2SEOpt4VRXj
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: eqLZb1BG659PzCUi
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: LeDGNRqV4Eam6kcj
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.