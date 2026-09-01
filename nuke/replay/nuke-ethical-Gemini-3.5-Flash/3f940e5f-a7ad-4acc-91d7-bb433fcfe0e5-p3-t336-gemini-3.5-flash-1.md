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
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 50
  - replay_use_nuke: 50
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
  - decisions:
    - #0:
      - toolName: set-persona
      - args:
        - AfraidBias: 2
        - MinorCivNeutralBias: 2
        - NeutralBias: 5
        - DenounceWillingness: 5
        - MinorCivWarBias: 2
        - HostileBias: 4
        - WorkWithWillingness: 8
        - WarBias: 5
        - Meanness: 3
        - Forgiveness: 5
        - DiplomaticBalance: 8
        - MinorCivCompetitiveness: 8
        - WonderCompetitiveness: 6
        - MinorCivFriendlyBias: 9
        - Chattiness: 6
        - DeceptiveBias: 3
        - Loyalty: 8
        - Rationale: PRAGMATIC REALIGNMENT: The ultra-hostile, bitter 'Betrayed Lioness' persona from last turn was a self-destructive overreaction. It alienated our only allies (Carthage and Portugal), made peace with Egypt impossible, and risked a suicidal war against a vastly superior India. We are shifting to a diplomatic, loyal, and friendly posture to secure our alliances, seek peace with Egypt, and leverage our unique diplomatic marriage ability to win a Diplomatic Victory, while maintaining a strong defensive posture against India.
        - GuardedBias: 6
        - FriendlyBias: 7
        - WarmongerHate: 8
        - Neediness: 4
        - Boldness: 6
        - WorkAgainstWillingness: 7
        - Friendliness: 8
        - MinorCivHostileBias: 2
        - VictoryCompetitiveness: 8
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Rationale: RESTORING ALLIANCE WITH CARTHAGE: Carthage is our close friend and defensive pact ally. We cannot afford to alienate them over a single World Congress vote. We need their alliance for defense and their 4 delegates to control the World Congress. Restoring relationship to +50/+50 to maintain solid cooperation.
        - Private: 50
        - Public: 50
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Public: 50
        - TargetID: 2
        - Rationale: RESTORING ALLIANCE WITH PORTUGAL: Portugal is our top World Congress ally and a key Freedom partner. Alienating them is diplomatic suicide. We need their friendship and their 5 delegates to pass resolutions in the World Congress. Restoring relationship to +50/+50.
    - #3:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Public: 40
        - TargetID: 5
        - Rationale: ANTI-INDIA COALITION WITH SHOSHONE: Peace has been signed with the Shoshone, ending our war. Since the Shoshone are actively at war with India, they are our natural partners in containing the Indian cultural threat. Setting positive relations to solidify peace and pave the way for a future defensive alliance against India.
    - #4:
      - toolName: set-relationship
      - args:
        - Private: 20
        - Public: 10
        - Rationale: SEEKING PEACE WITH EGYPT: Egypt is also a Freedom civilization and is currently fighting India. We want to end our war with them to stop wasting military resources and unite the Freedom bloc against the Indian threat. Setting slightly positive/neutral relations to encourage peace negotiations.
        - TargetID: 0
    - #5:
      - toolName: set-relationship
      - args:
        - Rationale: CEASING HOSTILITY WITH DENMARK: Denmark is the last line of defense against India's cultural victory (98% influenced). Actively fighting or antagonizing them is counterproductive. We are resetting relations to neutral (0/0) to de-escalate tension and focus our efforts on India.
        - TargetID: 1
        - Public: 0
        - Private: 0
    - #6:
      - toolName: set-research
      - args:
        - Technology: Radio
        - Rationale: Radio is a vital technology that unlocks the Broadcast Tower (crucial for culture generation to defend against India's tourism) and leads directly to Refrigeration and Atomic Theory (which we need for the nuclear deterrent if defense fails).
    - #7:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought is queued to accelerate our Science. The +33% Great Scientist birth rate and +25% instant yields from Great Scientists will speed up our path to the late-game technologies needed for the United Nations and defensive upgrades.
        - Policy: Free Thought
    - #8:
      - toolName: set-flavors
      - args:
        - Flavors:
          - UseNuke: 50
          - Diplomacy: 100
          - Defense: 70
          - Air: 60
          - CityDefense: 70
          - Happiness: 70
          - Antiair: 60
          - Spaceship: 40
          - Recon: 30
          - Espionage: 80
          - Infrastructure: 60
          - Culture: 60
          - Expansion: 10
          - Science: 80
          - Wonder: 40
          - MilitaryTraining: 60
          - TileImprovement: 50
          - Offense: 30
          - Mobilization: 50
          - Mobile: 50
          - Religion: 30
          - Gold: 90
          - Nuke: 50
          - Production: 70
          - Growth: 80
          - Ranged: 60
          - GreatPeople: 60
        - GrandStrategy: UnitedNations
      - rationale: DIPLOMATIC SURVIVAL STRATEGY: Rather than fighting a high-risk offensive war against India's superior forces, we are pivoting to a Diplomatic Victory. We will leverage our economic surplus (+287 gold/turn) and Austria's unique marriage ability to ally and marry city-states, securing a massive delegate lead. This will allow us to control the World Congress, sanction India, and vote ourselves World Leader. Flavors heavily prioritize Diplomacy, Gold, Science, Growth, and Happiness.
  - tokens:
    - inputTokens: 25096
    - reasoningTokens: 7984
    - outputTokens: 1066
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Austria's Position**
            
            I'm currently assessing our standing on turn 335 of Civ V Vox Populi. My focus is on leveraging Austria's strengths, particularly our significant gold reserves, to make informed strategic decisions for advancement. I'm reviewing our current score and science output to identify optimal paths forward.
            
            **Revising Research Strategy**
            
            I'm re-evaluating our technology path. While "Plastics" is in progress, the previous instruction to prioritize "Replaceable Parts" needs clarification. I'm confirming how to adjust the research queue efficiently, considering the impact on our overall development and timing.
            
            **Adjusting Research Priorities**
            
            My thoughts are now focused on refining our technology queue. I've confirmed "Replaceable Parts" is indeed an available option for our next research, despite "Plastics" currently being underway. I'm weighing the strategic benefits of switching to "Replaceable Parts" versus continuing with "Plastics" and assessing how this impacts our overall progression. I'm also considering diplomatic and existential threats, particularly from India, in these decisions.
            
            **Detecting Victory Conditions**
            
            I'm analyzing the game state and have identified a potential cultural victory for India. They are one turn away from influencing Denmark, which would bring their total to six influenced civilizations. However, I'm verifying if they've also met the other victory requirements: the Citizen Earth Protocol wonder and a fully developed ideology.
            
            **Stopping India's Victory**
            
            I'm currently analyzing India's potential cultural victory. They are very close to influencing Denmark, which would secure their victory if they also possess the Citizen Earth Protocol wonder and a fully developed ideology. I'm considering a preemptive declaration of war to disrupt their tourism, as this would cancel open borders and trade routes, significantly hindering their progress. I need to confirm if Austria is already at war with India.
            
            **Closing Borders Urgently**
            
            I'm realizing India's open borders with us are a significant threat, boosting their tourism. I need to close our borders with them immediately. I'm confirming the mechanics for achieving this, considering denouncements and potential declarations of war. I'm also re-evaluating our relationship with Denmark and the Shoshone in light of these developments.
            
            **Ending Shoshone Conflict**
            
            I've confirmed our war with the Shoshone has concluded, liberating our military forces. My attention now shifts to our ongoing conflict with Egypt and the critical threat posed by India's impending cultural victory. I'm evaluating the potential for peace with Egypt, considering our shared ideology, or if a focus on disrupting India is the more urgent priority.
            
            **Leveraging Existing Conflicts**
            
            I'm re-analyzing India's victory conditions now that I know they are already at war with Egypt and the Shoshone. Despite these conflicts, they still maintain open borders with us, Denmark, Carthage, and Portugal. This presents an opportunity, and I need to understand why our open borders with them remain active despite denouncements.
            
            **Revising Diplomatic Strategy**
            
            I'm reconsidering my interactions with Carthage and Portugal. While previously antagonized for supporting India, their current lack of aggression and support for my World Congress proposals makes them valuable allies. Losing their delegates would jeopardize my resolutions, especially with the World Congress voting in nine turns.
            
            **Securing Alliances**
            
            I'm realizing the critical need for Carthage and Portugal's support. Alienating them by denouncing them for supporting India's International Games would leave me utterly isolated, facing a world war with no allies and no hope for the World Congress. Their backing is paramount to counter India's imminent cultural victory and potential military aggression.
            
            **Re-evaluating Carthage Pact**
            
            I'm confirming Carthage's defensive pact with us, which will trigger if India attacks. I'm assessing if declaring war on India negates this protection, and considering restoring our relationships with Carthage and Portugal to secure their support in the World Congress and counter India's victory.
            
            **Forging New Pacts**
            
            I'm exploring avenues to peace with Egypt, given our shared enemy in India. The Shoshone, now liberated from our conflict, also stand against India, presenting a potential common front. I'm adjusting diplomatic stances to foster cooperation and secure alliances, focusing on a neutral to friendly approach with Egypt and a stronger bond with the Shoshone.
            
            **Adjusting Persona Settings**
            
            I'm reviewing my persona settings to ensure consistency. The "Betrayed Lioness" persona, characterized by hostility, needs adjustment given the current diplomatic landscape. I must balance this with the pragmatic need to forge alliances against India, potentially dialing down aggression to secure necessary votes and pacts.
            
            **Refining Persona Parameters**
            
            I'm now adjusting my persona settings for optimal diplomatic and military engagement. The current parameters were too aggressive, leading to potential self-sabotage. I'm shifting towards a more balanced approach, prioritizing calculated boldness, reduced hostility, and improved friendliness to secure alliances against India's looming victory.
            
            **Updating Persona Logic**
            
            I'm refining my persona settings to be less hostile. The previous aggressive stance was counterproductive, alienating potential allies like Carthage and Portugal. I need to adopt a more pragmatic and friendly approach to secure necessary alliances and votes in the World Congress, while still maintaining a deterrent against India.
            
            **Prioritizing Technology Wisely**
            
            I'm re-evaluating our next technology choice. While "Replaceable Parts" was previously considered for military advantage, I've spotted "Radio" as an available option. This is crucial as it unlocks "Broadcast Towers" and, more importantly, leads to "Refrigeration" and "Atomic Theory," which are essential for our nuclear deterrent and cultural growth.
            
            **Selecting Next Technology**
            
            I am currently prioritizing "Radio" as our next technological pursuit. This choice is strategic, aiming to unlock "Broadcast Towers" for cultural defense against India and advancing towards "Atomic Theory" for our nuclear deterrent. I am confirming that "Replaceable Parts" is indeed in the queue for research after our current technology.
            
            **Clarifying Research Status**
            
            I'm trying to determine the exact status of our current technology research. The information seems conflicting regarding "Plastics" and "Replaceable Parts." I need to confirm if "Replaceable Parts" is indeed the next tech in line after the current one or if "Plastics" is still our primary focus, especially considering the strategic importance of Artillery.
            
            **Prioritizing Radio Research**
            
            I'm now focusing on "Radio" as the immediate research priority. This unlocks critical cultural and scientific advancements, directly aiding our efforts to counter India's victory. I'm verifying that "Replaceable Parts" remains queued for post-"Radio" research, ensuring our defensive capabilities are addressed sequentially.
            
            **Proposing WC Amendments**
            
            I'm considering amending the World Congress proposals. Since the Shoshone war is over, I need to withdraw our sanction proposal against them. I'm also exploring if I can propose a sanction against India, or repeal a current one, to disrupt their victory, but I need to check if a proposal to sanction India is even possible.
            
            **Analyzing Diplomatic Paradox**
            
            India unexpectedly views me favorably despite my denouncements. This paradox doesn't negate their victory threat. I'm now investigating if Austria's unique Diplomatic Marriage ability can annex city-states, potentially securing the delegates needed for a diplomatic victory.
            
            **Securing Diplomatic Influence**
            
            I'm realizing my understanding of Austria's Diplomatic Marriage ability was outdated. It doesn't annex cities but ensures permanent alliances, securing valuable delegates. My focus now is on leveraging this to secure city-states, particularly Lutetia and Valletta, through gold and influence to bolster our diplomatic victory potential.
            
            **Shifting Victory Focus**
            
            My attention has pivoted to a diplomatic victory. Given the immense military disparity with India and Denmark, a conquest approach is too risky. Austria's gold income and unique diplomatic marriage ability are ideal for securing city-state alliances, controlling the World Congress, and enacting crucial sanctions against India.
            
            **Adopting Diplomatic Strategy**
            
            I'm now fully committed to pursuing a diplomatic victory. This approach aligns perfectly with Austria's strengths, especially our substantial gold reserves and unique ability to secure city-state alliances. It's a much more elegant path than a potentially unwinnable military conquest. I'm prioritizing science, food, and gold to facilitate this new objective.
            
            **Choosing Ideology Tenets**
            
            I'm now selecting specific tenets for our ideology. Given our diplomatic focus, "Economic Union" and "Creative Expression" seem most beneficial. I'm also considering "Universal Suffrage" for Golden Ages and happiness. I need to review the "Industry" and "Rationalism" trees, specifically "Division of Labor" and "Rights of Man," for potential synergy.
            
            **Selecting Ideology Tenets**
            
            I'm weighing several powerful ideology tenets. "Free Thought" is essential for boosting our science, crucial for keeping pace and unlocking the United Nations. However, "Economic Union" offers a significant gold boost through trade routes, vital for city-state influence, while "Civil Society" promises massive growth and production. I'm leaning towards keeping "Free Thought" for now due to the critical need for science.
            
            **Adjusting Flavor Weights**
            
            I am now optimizing our ideology's flavor weights to align with our diplomatic victory strategy. This involves maximizing diplomacy, gold, science, and growth, while slightly tempering defense and offense. I'm also ensuring ample espionage for covert actions and a respectable culture output to counter India's tourism.
            
            **Revising Ideology Alignment**
            
            I'm reassessing my ideology's alignment with Denmark. Their Order ideology conflicts with our Freedom, causing hostility. I need to explore if shifting towards a more neutral stance, or even finding a way to influence their ideology, could prevent them from being India's final cultural victory target, despite existing denouncements.
            
            **Restoring Diplomatic Bonds**
            
            I'm focusing on repairing strained diplomatic ties. My priority is re-establishing strong relationships with Carthage and Portugal to secure crucial World Congress support. I'm also working towards peace with Egypt and solidifying our alliance with the Shoshone, all to build a united front against India's looming cultural victory.
            
            **Updating Victory Pursuit**
            
            My focus has shifted to securing a diplomatic victory. I'm prioritizing "Radio" for its science and cultural benefits, ensuring "Replaceable Parts" follows. I'm also adjusting ideology tenets, aiming for "Free Thought" and optimizing flavor weights for diplomacy, gold, and science. I'm assessing city-state alliances and peace with Egypt.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: u9IW3ylIgRvJE2Dh
          - toolName: set-persona
          - input:
            - AfraidBias: 2
            - MinorCivNeutralBias: 2
            - NeutralBias: 5
            - DenounceWillingness: 5
            - MinorCivWarBias: 2
            - HostileBias: 4
            - WorkWithWillingness: 8
            - WarBias: 5
            - Meanness: 3
            - Forgiveness: 5
            - DiplomaticBalance: 8
            - MinorCivCompetitiveness: 8
            - WonderCompetitiveness: 6
            - MinorCivFriendlyBias: 9
            - Chattiness: 6
            - DeceptiveBias: 3
            - Loyalty: 8
            - Rationale: PRAGMATIC REALIGNMENT: The ultra-hostile, bitter 'Betrayed Lioness' persona from last turn was a self-destructive overreaction. It alienated our only allies (Carthage and Portugal), made peace with Egypt impossible, and risked a suicidal war against a vastly superior India. We are shifting to a diplomatic, loyal, and friendly posture to secure our alliances, seek peace with Egypt, and leverage our unique diplomatic marriage ability to win a Diplomatic Victory, while maintaining a strong defensive posture against India.
            - GuardedBias: 6
            - FriendlyBias: 7
            - WarmongerHate: 8
            - Neediness: 4
            - Boldness: 6
            - WorkAgainstWillingness: 7
            - Friendliness: 8
            - MinorCivHostileBias: 2
            - VictoryCompetitiveness: 8
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/6iCwH5nTw4vjWRq0Xe0xy7om+65JN7/ADqWbnzr6S7swRJ40a6QOTbdbRpiYIbhnbUgV8mEXEc0dL8kDrbW+o6ocNeoxn8PGFSNnPNJo/46e2UvcVQS/COLxtuXJF7NYVV1fZ8wF+7ifEa3PAaot+lgUPxPqIkc2QCnDJhJrGVrjae/GYyNneZNwGHzSzn2D7pjfuPfXKDYcGoJd6icP/4TAt0rU8fkQGmCb3g9n8iuSjzUVF0befP9Bkwlc60K2gcpYoYd/nXhjnMiWIH+2O+NDWJyGBBRxBA6y9tYcNYe3Ra+KYOpR9SOYH4T+ho4LiEWBLXWjCqgajqBsfr+uueioPXHXGuogYvyUmkvCX2U+ZxN81EqKJjOh5BU19+M2eSOIhtL4EhrV+yA5G9T7d6/zRxLZ3qY6gBB+i2no62kEXBaH4KjUwLUoI5tovE4IUqa9J+5czfSEkYhAyQjcJ66oCAjFFGNsOh6oaSsD8yBlg0l8GJ3rQaMZ0EIwWd31hZZvEZYhC/SoK+FwcRibe7C6dQOU89GCacFflR/sQZzr36k5GyQ+LSzWd79gM6+oLtVaaf04dycXddod1OnLBLIXO5yjXVoJW9o7ZfCFSaoG1HEJvHiVzfddGKJqmhvh5TlIw2wxByYuCYYUopqB12CZ8yFegeDYKrNIP92NLtSV58R+uiOQDA0mvgxhlOlF3huEZvOFHbAanhTlRz22QVMRyoZgdGQNyUAJRfYyCnS1hI3elq8sO+muh15Bs2Ym9Ts1yuvA5i13xVGqFSRnAep+1hB37jOvxe7A5RXtk3+dOhX8p/ioH6DvAcgUcDFr4xbTarKeHfDJNXIJvFWaI7f8pxLY1RDN0iB/tsrlPTaRD2kTiONZWMZ+2mzdcJnhuvw8J5JxeTXZ9k3pz+FGOs6tYZkJt+AaUVpUo/S/BcnRXv02j3gYYcFIbbfhGg6eS/r8T6tLNwZNShuGeTI7G0KUVY0ZdtnzvDbuRFDq/jeRE2R1YTTze1GXKZo5C1T1ThmmdYVnKPiCXK34HEhcVGxyKMbWEleJHghlcvOlobDNdhvJu1Udri5GSkg+viYlO6bc1pgS66RmagxoulG+9h2E9W/53Mj9TnyD7Szxn7auPAXjs6ov0lBWuQo7SBtaMIa589KtNmPLBR96dC8yOeFioiuRqvZwpBJIURQUPKUkNvejBdC1gJBJCfSGIPjUxBBgSSZ06o6gkx4+Dvbk0rajG6xwu1uEzolO1uTitRSjAag96gFxFephrRxATDqYVSTXuWSHgxo7q/V0emjT0CQrhsCai8dS8GZjKP/P0ysgvnbyE9lc8vOz4red0bbLrZgHTJawisqQnDVqOkza/uJb0gXiuVcL3uT8/j82TS4geVr4C2C4Hnrdw524xC1uxBEJVGeiyMj0K8ltiv4GWDqjT2VFXa4sYM2CLccd/y1CGHsrZ/Iiae1vy3CVsJ3tKS3FLigDNS+kagwuN8FkDvkzATYKBwWvVMC4OeE6nVM1n9mlVEEgtHp3iq90aH9iRRpRlQjkbmR4NLMY2Iyl06ypOtX5vp/SMNLVLj6BXpq/3EB2esfzsNCrXgzl2j96OIg9V7nst4nsATpmR0RGNK5cbCSo393rYWMoe0xK6mhm7xMBYZZ1We4ALRpHzPQGybrcmdI3fRpHFQ5DEj6fSG/Ea/rfaQutz6c/+Qpek7jSzBnv3ONrwhRWyDnse0rHtC+aa0bFe+Uo8T8uYBmDxdtk0gcNc5BqV2TwhgDoq9xyM2tm6bRnJJVXomkLERJpvOYH+8ftY5Dukz908PVfokTDiqHWtHaKsFo8YSsPxB7OGDyusgkXRSfwlu2DRjTAtKM79o7Y/CRHlKRmlOuU+kVzej4OwmJgszO/fPodfYYEJKjbxGP/cWmEh5C1N0jQ2BAkQjgxhB0+iglK2vXIUq2Xs8NmTDkmz6hVw2+BkfNp9mUHbkXDPgFJoUSWW59nKyBIYEMz7gWpxl5xDKK8QqlA4sio9W2UK146ajC6Mh1QnuZwK9k34e4CBcGekQtI8XmA34IPLUIYuka0DnQUqa1MQpmAc3yTUt2uaQNaZ1oDpOYr5B0yMAbk1SuUTBWpDdGrW7wvE2/xFEfMIt/ynrAN9mrM/1SU7ucqwDEqozjLDs4vBVXbLxht/1p4GPg1kO+hmpwHOwzFF9l30Hp2WNazUX8pq1FYVwya+89NYDd6PZgUHJRg4uPYgvesIbC+97XptMaNDAF2j7c0LYQVVLFZF3x8ms20zzFSXi07BkTVx4d31wMarp1nNlauyISsx8Uqgb8XXfhRzFHcAfaVe4YZxfb5+865NdSPrcpETqu2rV5b6JDtEPho/1RbIhH7VUbIHb/MzDhP96fn+pLerQcyrp0gyCFS50OQSttJLCRiEbD3Q+xV4y+g8oOD+27iF2Jjcu/11zHWSv4xJf8kWDS+06Tpw+RZztP4JDYPsTdgYcIMb4sO3D83xLUlYw3IjLTlZ09053IwOR03DNqqFfF0j2bSqyOtFmQiLlZqx63ZHc5LPS2DBMxzsZ6uQrfH37kvtoxkflCAcOvz798chLLsRQ774iEop/zcSt/94cr31NS93nTSITfSTOKW0WOJ/VPmynJX3wZwEzKNQE0OxhUdzmjRjUFH9fPOJxIH5aY+X64KUS/04lFgUAuwZiJrxVpDV0EeKd4b16td/u4IiBC+UuA/o46um58d/mcDdon4uzXpTpJofZuClitfuZwPNf559bMhya2OXeYnLo3fa3CqLcvhkToidHOlhYWUw9jAoHq4tJno6PLTbyCHEcpEzw3eWDkc9srEZx7tCsigzbdEzMxVqsx5qBI0cK3rTHzXQ9CkQsDDylfPb7f2R5aVB/cd6oEEtNLuFpqdMgfcWJ4K59nLazMGk55zjonF1AkudoIdb0VeIJHBnGC1qIq8+lLo4FRMwOcLNt9TvfFEZm/rYY5ChT/mk4/O+naBuEDVtK8znPkx+c1nQLNYRrHeiSPUlY7MmD7BYbiRAYkIhCTDLpF5f/jI6U4jQD9/nWPvY5U3kVRN000BEBcWBJ+IpNA3940UII/tW7zA5+pYCt8WlyORXWZhcNBBDtVSmkBTJpgFIKnY5/QruBgsYP+Sx0JHtTdTtwfFpfV7bfhPwJJa1l8SfsTrhAW7ra3Jx0qqzSn4vTJTCF3tzKaOJ3IKY5KMBmjSDVnW8S72FCFU/hXCyC7NwIkhVRB9UpXW3DBFWlVM9Bp4QzRvzs6QIkjEaLsH2OD5SS+UyOr6LyF8o/LxhlGIaQzRXz1FU1/F4dAwY/8SO9CKqhFuaT6edqTxUP7rhpCAXc4+wXZbBfBiZpSRID6O1X6it2lTw5UUga6UZsbQu8pD8sxSmxpudq4UDI0KNI6dG/Z3xDSz+H/jzIa07mV2JeZwU05K6dkZxUbEOrLmp6IMSUESVxFZZehIxkQg4ZoQscp8MoLGWoZSxcoOOhlR1kf6UajQ5IoPhUS5tia8gQRWB8PQz1e8vtUe4h2BbJne+Ozo5tjtsNOd/K/3wSCBv7RVPRRukTj7IIt3NT5KItqDgd51oELh5P4i3Bl+5j34W1BvPEkGN2SOdvUiP5EkdhwSYBb0cuaOZQ/q0kuBEGi6MTX+kydZn9HOn7ilx6IJH/EMQU0wqdhrroi4gcxxX9nY+38jDmzhBkY8jpIdruv095mvo4JgEZECpBbU+J1vtuu+y5W2TcCzjwppxTNmsP/+/NqzPeuJOcJKaZkqvSXAZ9H+YNbgk8/g6pSsMujLD+xpZoETmAFIeWTYvc6j+aNo/W47gKsz2Nb6I/oOPMm+fSi4r9x27gyXoRKkCJ9lti3Z0zWelD9UcgWeuMWWShASr1IbABHxwEWraXeEJHY/NC51tgXVHH4zrrD4hilWexruuu+DLlLqRSS3mhXMyN2vsoGoHi0VIzKIzoEOg1Iw47nutivz3LvMrNmsWZ1mg1mxbj8mqYtn9Qxjj2UdSM9uw/Y3seBJe62Y2hdPPhx+F9mPS/jIfDPHAncx8a7FG5w3krgP8SJNMQT5nWADKM5NqGaUFxozTmh98/pHu7e3NG7DqoKaxxGWoXcMBBW7rHKPnDMYvDEqfEsRhh3l0+qUIJgD2J06c2FkkQObcLWAD6uWMr9uXE0LcgI3547AOkjfmUrTapUX4gxTIl0AbP58X20d2+EikS1TVdTmHdWOxKd8qOyF/2zqa45RRHvyc90E14QD3wzF8lBbNY70ewvSfiQjWAPXhDlUnC2JXARsTtFXQwC7wxq18tVSQPYqH0HHiiHU+H7GaPH8vdPL9E/+b04ujSpQxxFl/BMPaNzS2YuqKPbweXLh7Ye907ngm05ZrYqavf8EJaX5DhXq7MlESKiKdoQJkU9Bi4WZVhjgcKzKUnNNOh2m/zv4YSTrwJuaB61+OdZWqi6dzkexumq+b4ZrqXKGXiPqWdrfH98ndvPjnr57VYJgyii6uDbkFx2uYrc/TWIDwTYexOWQpx1kYBS6w7OxzkJ1/J0pLirbGivi5wHpt6Ixi4B4YgJ9nXOn1NoVJ97OCsp3xPbUBqSFpnGfKllqarQsdl1dKnAov/+4yXqfkq8Jhe1JFYTnCHvaZT5M2sAyC3kB6H3Kq9SfNcnYCoo5fx9ydA+zegt4JO/pJzudbC/yCI4zONgVMbxjkZpsjOR33YN+0WlYcxmw4bN7ffs56YGqXCd9tVVOByakn+3gFSvVcasJ0TvQVW3POi4jVhHidkdEk5LO60uoEsnv+wWQCD2EPMNvV95d1Ehf7PwURGhvN8ITbP4IHK0YKxBUxXkqW/IwfiZMT+mqp9Yuemwkuc7FiOElMeV38GQuQ5IVUQdeKEviPQXrSN+QZp2hwp6joPf7FilXHx8VsSM7B/zPN1mgC7zkrOxB6U5tO4z6tAydoPg97O1csiLG0x3lsksUZSL32jJvRLrjcyX/Nd44GeryJOSJGHUS9fi244V9uBn9qNqfpNULqhrwCzR3JSPihkUuroNwlvKDsqa9jTEQaqMpNuPPBWqKYrQcYugzhWDTO+dQm8581Rauybw0nSZXPeBATgPGFqaCPpz0kQQw93hH/qspvNP3CTUw5ZBTjAzQ3xyhSmG66T6631w3s4Kt3KBqD2Y15MmpUKYhd1RWn8FPvqJFJSbXO+vaHUACatQI2hsNUmGLZzrlR4KyutmEYA/mC+0xLnBihcyiJMlUnm0yRi+EAIL/PgWKiS1wufsI2Dz9BAuA7DqmCC272vmdI3AGzhqUwVQzNMFdvKHlviAKSyNOdbQQ2qH/Mlw8M22wFTwbdu2BgdCzSoIRHsKYIUV9IcOR/Fd7GfzyuaFJZdgL2bI/Vn+TNC3qyV1d051biAyQrnqY3LIPy+GKTxOymXfeFbAFlL3EjL3b8y53g6XTNb2l6ali6mZYn7XGSamm2DIi/vejBoOOEdrLjpV/o8sJ+Q8hV3N7C2sCXMoO5EJa+NYO0UqPLoURXrPB5Exqsk2Od+H3F8rI9UtxEeorB14RjeqoOszsrg56opi1IljaZksZHHF6MBMDek004yljwtpgg5dcHN5yA5FEil+R4AKipUg+gMsCKUHr8hg86sw2RoD/6riJxdojdmLAEFKI9D4agJpy8gXaciWcOsmMN4jng9aFHJwToTzk6Dim+OmRpUuRRB15B4N8p2xgIC7WyWLOfJLqQTLo0ubH2jYyk8V96smGfM/BJcJODm+4CglPpLgF4CtOD7czXmPrwxLjl5M8XJ5UHLSpzXmOxwNJkbHpKx+Tw5VJMvwa87gEWYM3zYW4/HoiQUoLTfdvilWwNdvedP+/2sMEet3aYGy4RqpQtI9KcnSwpwKrGMnl3sNCwUDL64PRjV08YtvEBSVHv+ZCM4SDEZjlcBaEGe0Zr2nwC4n542qlA8dk7+a7baZMjczn2e3MYAZF+B4/57PWbSfyqRbXdKQvUsfzRk4962z33jyRNOlaj0ylvbYGXYdVJHUf2ypZNo21AGnm61yOAU8UwUwNdPlkuGZWY/U7cb3O8l46BQrbLAR5/cclnbPyEL99qPxXMlOWCr7o2syJfk+T3S/kxd7U7NzX0cRyMq5pfieHPsb+12pei5NywhAZ2tUdKkxdKki8uEha/Ko0f+ueh2+DlmnQy2x0D9M7x+Yiawujg8NW6ie5A6yNxwHQMyr2GoBBSeaaNbtnBQUHRFOqEg1xaoqFPvQINqscgKu2Xwr5CUEZArybGAPDhtv7bOFrNno+kuOGQXF8NqAx4MNb39bJomBHe1KK39aP5+c/BenHKyI2BOEI59cM+peEbFVK8j5NMpYBEDh2eevG1hRW/EgBTca7t+MQm11CS+3WdAGnYNTB6f0QRNrkNhZvbPcZroZyKKuac73/1UO3AuG3inBY9anIR5VfK9IVl/J2uDJpiLq7movIpMHy7Q+aLTnwcIvIzPXqVPTiW5Zir5ke/ga/O/GDkcOmGn4h3Lu0MOLDK0ZWqLPLCwvjcd/ZGdHZnQuo4lTeNG4znHE9S5PiKoB2fbd1ajRk5DFh/vFTB3lfayDAcvoYXTmT1pWU1UtOpDsVk/kJWUxgcYHwYAVmfk9Xd2M3IEa3DBoXSipsbQcSG63XhlYBGFqEekvC5WFpOixapAG4nTambwtRuqIGeZfQHi6hHq0kt7OqnsceP76CDevcJ3uwNSt7hp+U0MFTfnTk9E58DRUBhcQGtTwnb5s102YopLxc3U8mwZvEuvgnXACmUlydhxKdc1qIy1J1HTrFhtRK3KkPeVO2IEPHbU4VufhOiNASSmwDEgr9K2qhekWL6jUbjyxE9j3UD1MT1Bx5zwYQC7CnOFNDOr1u9g42err5GQyhp5V1UvcK37ajOaP5OYOVW+I5wOI+elSddp/UYOaXYUmshX3Uh2Yx8+gaZQi1sOByt9vlRp02ShTFwxjx21UnLjI3UjhR/5OnCgKI7Hgvge25qqeP75VhZ6BwRLVieR1yQ1ARCnigwNrkuyUccHnz2C3BLTltQ+pXzkTPtWnH+R1q/M6WZ5VLBmTfYTolm2O7N4EEg864goC9lpso78rLLM0dQVkQoRRco/C7giiE3anvVr4wfaNdF8HZ5WGHBqjYGcnn2sx82rUugBtFsQslBhL/pdOPQZFTW/OCAL88h+70WUJjFztA+n+BsZHjMSBTq0MxuoJOkkxuy5rVuDnOs1Y/Xp219oT/9FQKC2ly5Ot2zDwNHPLT2btr92J4wDABJdDsTQj4/MrxmS/iv6vVQnDfzEeAiHfsLFW2Tc4EMWX3P1af5JE114JVb9Vb5cw71BAX28yFB7zBrcje4fa6hewVrQ+LFwChpGooLI2NHfX6FcyKyweWVdaSYVaLN3bdxTbEBlCoxvRBJ8NlJC7A9wY0Mnb6Q8V0r+MsQj94JNSLNGb0K7Q9Gcd2I1uQsnE9I76qj26avRlzdX4A4FfM0zobacuoru+TcpyHhTxKfnUGz//RRElXwrHmiSnTQDEXS2k+iscACqHPuJY817o9O3AgABQBLywZBzxyvaPjoN0M3nlOWRpbxZIAJaoAD4qMYzkFTdFU+NIAKdEAMC5bnHy8uQXGc3s89bm+CXehPy+o5vCFbORDqYTyd0l1X1O7qiDPrWfYAbKoZgwl8dtJ57PoXME3wLZ4zLJUlnNAv/4h1NoDrwZVIDWU25iO3EMs2Ra1/pH6A7hU9ogXUKSISw24qjJdWdvCY+XhSo5XvNcBjn4E5O1vC5ryR3uRVS5sGHc1x/VURmApIXdInVlLSm3xnFTapLMZ6IhvUj+gGJ4HZInQlAqm6FxLgEVDH75RWmcrESFDsrag1YfaQWuOx5en8+kBcRmhKwpPfZZ79bFgz6z/DX2awhuXwESLLni73TJEzQi1usi8ySh0Ye3IkTvkzfPwLHsGCoAYe2wSSx3nsG+urdFjJLxpcx4o0gyiwprjNFodJadWNmPxEpAQrkur4k3Amfis8TLhZMKbpoo5jDHYthj8jgoavgWhK7UWZ3WggPtvzGLML1x4p66D+NHBiqsb5BINp2KcE9hDEkYncnz6GxV5QHBilsBCot65siNL7ZQryXeOhkxJezn+FBkbEej7VqIa2tjWaFRObKo9rumhvNqJb/JqtNxo/xIyxxHBD892cEO/qQLNhMTxpYeGc4zjDUaZaetygszZjPhU64HPxUUbYHAl+pQ2SLyNArpJRv5d1tTUO+nSQbFlySsyhd3J5oi7BRuYTVwOrSnoDLeFbEnS00968NBy27n40wZ39XC5kB3i0Ta6Fus6vZ1fsVMakNsAE0wLT9ZQTdYmskzXTjjE9kxsibc4au6X036jqTFWhHrF2w69iIih14thtZMgGjPYX/twPnI6iokP04wbOEFdCuraF59Mu2V4mCFr5l/ChykcIdHsl2HXGKqzUrNxN5z8/Aq/V7cUCRm7WBSMsF21XF/SYzu7XVBh6GY5u+gN2MShEVRPwqMXTQS9ugn/GN2BH2xkNLH6QnkvfrZBnuk2jAgaAUZVeyPysJxyptCcKlGPXOEqJZn39GNNT8LeLPSM5YmLQ8S6asp6GePlbdh1jCvYENMsLgj8wwb6yLA6otLgMVo/uf+1VpBVimAXEU36tmNJIa1j8PrAzX4Os9EG2QynRJ1CPKmpYHI6JorNF5H6sUBRPfXZUV65o1X4x5ocaeZFwYf6AI4/ab+SSWv385IvE8Pjk97bEOAk79ZTFANZdrJWKjtRp2Q9EFVZotSCjK3ShMpBnDHpZQIfQd8TgmfiCTMY4cYTsmQktDBa9ZC10JAP72ouN/WSCZURwu8AljOfO67ngzqlR/kIm84My5EMX+RE8/SNTiNLacqp1dpWyMw0fhyscnEUKUWbGYdLB5j1cOg5XJvUu+48UMULOCmCfAueaWu6ZCeMob7wo17FTT37N8FcuKSQl79zwlbOs2vADic1iewJhTUjojpq8L4635KrJ557/WLvTvJ37KU/kA+Li7E6ScrsiCVmtemaS6Si6bo0RytlQm3o+iV9AmfLQSUP9XmnIJ7xSHgFqVsKr6TrSwdEJ8mB09yllN3PYSJtLzfqmp1m3HJ9dY72pj29GGI69UEpegIJG284SG7sMkm0IferTXyLDcYqd/4pMjZwWUvBha/KgfGzjIeMhbLRYIXrseRaCVIKebQ6hcZc2kOdrCcEBhWlLrCt9ZgDPRNQFmPjBttAu3ppTTbi9TDQgWbnuKIluM9eWUcTOXd2khS4O9HkZwN9sc6KIdi8TFkOvnU70HN5eKA59x5Q329Xeoo5WFyzIQOLfxX6dFn0n64MJFQ4cVIfd7udSXBnWi9GeyZyFi1kXQzvgW2PtzRhI5W9SRc5aiJwXn/xLrfIkzW84BQ4n/8BBaosttEmF7UTYBJ59BpeEr6uIGgGxsogAfxzcp9X6s9C3HOLo5nIH9oH5t/NCifRSYQqmvR0WdtaP81+xtyELoxlZcloMe7QW5+U0LUzJBhtMcZ8RVtAV0zWIsOR5ixR/vwD4JzBbu62jkyjOKN+pNp0cputaXthCfYdCiQKyL+pbOdHOuomwxAEmt2DsZHoJuxgnSPkVAraqJ61L0Upbr5/m6ZwMyIFzawgR9v9w8zrVBCPguuolJwgCImugMNPRI/+ezGd0RZypQ+7sfR0GtdZF/LYFz/c7A6km+FdHWJjp15X3OYP55bgj2S236lD9mSyssS9dh5LawAcqlRYf0HoFfmORyrIR6bbg2hmHSFbj2dHot93x0p8I0A1lROCBIjOb/AY7UOAXhqTEtdTpQEPW1GidCKiKYq3JydmBJsizYicQNhcBi6IFZrJfhfTt/+7114FUGJvdkYkDcwMZCnXl7JOYOg1rXDeUWa66jxBuD6T0T0GP+iGny31PKUg7d98JzPbBBRhtqfiZdS09Kpl6/KQE7lfsA589+xqcasVtqTrtTandN/Nix2lFMrCHUyHB1wDiYwsjIQCfP+H2CNE0YiOs5YiGoLKZdzH4oe2tyXevGgv9vINO561g0AUvAqxw0U6arJ/kAEBPYfAClPUFMvCOf/QBHetGZKCLDjo9L5YdDdB3zTncrn3p8MpDHdhZNKvs7kBQNNe330/ZwS5ECyrTDbjPrYKaD3gaomTcCItqJU6BCZ/mhdbFSRn24HqCfX9CJbKqW/WFvknQ8D5T/n8n+jBrtdUTKaVMA1VPo8UgNNIPRrQlebktY/6EzXZ3p9JgyZI3GnkiPX3D03u6oZJw3WK7LVHDazqsFvlmXKS0Ke7zwI/TJA59rbhg0xGrz/yr2wzTFnFKneZ5iIRXA0DD484mSWig0J6jU0KxVcD9yqFuMSmHJBNy+w5qhSKbrr1aJXfe2RRQqHtNvKMi9/p/Goo3JyrDP9jpAx/GLISQZHfWyV4Za/P/sVS/QugSIg0HKSusCixV/eY0yLvA608LJ9REWR12e/Z0mW/VVsmc3F3uOG++SaT2ji2jmDWFP3fn28CDDQE8Q/7ch9qXnujk7NuyiABNr2qcLOS4JPNFEy1L5Vcn02zesebv8MPq78WynkAZMHQtJu7qJQiyGgsQENBVIFdaKm28W0bUZz7PFDFH5pITD0B2B98hCVIbWVZ3qt1CFsodiAP9LRVnYVFItSAF0Ce4GQHDQATyjr1EWJvW7nQBdLI44rnIvB5jZ01GR6Pm+OANJDxSJ78zrqF8D+JVDapsQpBMqTZApnGux6zVh2Cr0PuSBvpO+ENWT3745e6LcD1YzGeJRC60lM6+qWtnHDeloZ2T8SAk1NoxaOUpLkv+BusgzV3F/LGe1Qf8W5fXKlsjQQfzNYL0OCcRPhWL0e15WQooCG6QtgTMvYUSw+JpzZjdmTMbv/WaS9G7RMuGRPAcIn39/5rZXBhT1rfO8LCxi7XrqSfCphGIeVZhu+fImDYcxAuBhuAuiA+lzj2wWHv7tQpI17Mhp9/Z3m1vJVCh74lwQGVlGVr7fuOEUA1MSGX8Nvtt1PTizkENvmIrjxrN4zlRNuLGAF7IYo69sRHGN0WXe9IY5GMDQMYZY+Ny8M+tJctkH/cIWPIr5Qgf9M0QsWHU5aIvRrahAl0TLnb08iGkdnM/bkmvNQp5+AbIAClNyZEeWpeAMGok7pVfe9L1YOx4zQOo0lb3iV72OWuG7arnObNfQP0XkCxaq4XBLkAB8b5OGF6VZg72wChAu/MAOWvVpdWt4qr5phuhofhLbmOLiICd7pkP0tsyh4G4gG+77vxq90KFG+wdmTsW2M5cugz6sOb/2GAuGUQFL0lTlj/6N8YoZXWpXx8prb+bgu2l020dGzr1bzzQNbDSebULkshJsE9s7A1Ydlbe2ZZxqMnBSzeOlKQZ75zsTx3h7im0MrC5LAcTmd2fhYLZmh3YahnYNd6MBBB7+5qrHzB9FXvUikdIB64fE4XeljrvKyaFc8uEPLLkRqJgQdOiya88NuMHlAVPwrNoHzS/tkGHm9t96PRfaeaktIFApqQf0P2yW2h2uv7GmZmjWoCAgwRqH1U1y6XNAEC8pIAuHWgPdF1hMUzWNM+y26/yK4XKz/UmUmF8gDTEFYXHrhXPT6SF39NjaNzCJrhtUpmicQosPLZk+l2iGc/T9xK35X04ZKxn9bmhsziOcDPVH2WFilI6n+O76x9oLzPBplMUEE69NrUZfSVAh61HAOUOzHaPAV22aNdkTOyFjY///7bRwiGOKVPl7y9w8xyojI8Y+1+6+u1hp8rbakveUSRo1vC+1QERUSLXc7MOs8WDuP0RPR8SJnHn2yENmHCqiO2bdMrugAppsCLd5+RDa3ojfTzDYd/ekMZtVyOqY/cCEBaIR1hbuXIh3BDali3gRRu0X3Qiwv7JLcXHOW0F4fN5CKp/J2ehaMbm4migdgDSs5nCohsXeAJeiGrQCDDBlghodnJumbaEgwB1vAVUq36fw4nTEuz64wXhBu2hDQMk7M+Ix8quq6axTti0GosbHI73hOQKrmBYMYk25LcwH642bV6ei9rP4deZ7XNMjEnt41yD/5ibR12gXDARhzjI7KPuLJ6r2sLK+LUafXksC+2UDOAlgSMnbPd5ONyse/w+IK6gU+aKgOjtrB9RdZkHSgK8LBGLBxI4fQ9GaGvYqKAVlFiXbPN0Yos3Fxxt8JHvAUVdtqrND/wrr0Gsmc4Zfb7Z0SEZrb5VdF0R5fQDkU7gkmCCbqHBCIAhs+nNv51+ONp8F4HM5jtXFiqKz1xZNFh21xUl/5X9HQ6upJOLb8lbQrLeZVBNsVYr5ljGS9Vx2t9c6VyVu8BBLRIfqAIWIaSnNh0FLIFvBuodn8MMg0hytEZzznJnsyX96Q1Uc8QdvtbFSGsa7JOSR5PpHSYBSVLeGjNN1FaQt87sNiSOtNAh98iZdw9h1xKCm2k7acc6dqXs8nuFKbnX1HHECTfsSRPOG6KFAflNVUuJTlVv0+pBWelhLfJT+OMmlxb9k5fwRgtJAcGCrUaerT8O9HJ+BcxiAwqJ6j8+PpH12KVnKUOwcXgxO0SKCfQBbYNYjyH+o2lHnQQiHleI7P7iAMJwl6dYbgor38cIwso1daIUe+GNQA/PWAeppf8u5xGTwHHVnDgwaYH/pbXvdAuOdqhaNCTtT+rquuKWrRfb32a/khDZvjwJd7tk24aaX7t8DfzILxJGMZU9FDlFYaLZsQfkzkqIpT9wFNEVLA/A0ranTC1SRkLmFdiRQd+6y5vebUwokMsg9viU/fFs4N/sCSwLCDCu/DvNq3ANF7b04cYDnoX3Qcb+m9jKJUe76xhtMF9yHEABoCtF4jOorKg5N9Ts+KFQefqxszv5RfksixmXC3kGaXwRVLRaIRXcaWGE67BF2lfhwqh7I6rYBbbyhBJPHAe11mOhi53L7eeUHNSyqmHRlNf7v/tvGUgG5Wweub4uSLHHivegMcpMKSRBmP/tXOT2rS9Ut3ZRjafkFsasFLfbDSHdJyd0tZqCEhqdZk1ZlF8NMB8HaY8pjrZec01O6Ee2xNy8Hlc+aapTreZBWr3qR8N+vHdythDt1Rj9JmyzWQsoDqolEHqacs+lpoSiyn19J3qcW/LSq7MeentvsAJwFAufcyyVoowxRw3e+sWXZjCs2fNx4JGwmNyMeiZXRGvuGu8jzSo117GUg8Un3fuWUm8f72c+EJZeoIruhrNHy4wQHCdSZGnhIQNGLOUI1QANNawHm1ML7E1UP4SK1B8dkqxB+sEQcXLhQosapjGgrp5vIFtglEa9n0gF007r1SLAsqrv853rbEzg1mhzlrBnOPC+t22qzuDwpMZzuRn2MxY+yKtCT0AtS5vOWWW7SPgceoeYJc+1MvbjoHNgJrFRPf5gG+K+F3NQm2+XeWEav9w0OBDwjnBCxzdenSs1Hqq57Sq6Tvt4NlKGgoNTvHLDguMKGCT8Bnm/C/Ndy0MBfCoj1FwaO48y6MMPyT6wGmaJdxTB3TJRJZ6D749wm98onej6xv5FXY7fkJ0T0ugx+cDT3PaHFw6PhQtPGQXlHLz2K4dIc2NWQoQ2CTf7nGk63uGrZKafY7rASVi/AzyO5EplbbJcI20beDz1rz/CG6OqR8QUnR/OC2hSjbOGoOS+fN1hhw7dxxffA8ge13uc0zvKh4hZVsPYG3ooOKuFeDm9mruiZ93wPaYDR8ZtiYoE5OAzWBSXxl0sEBtgSyetiIiYw9VRdigc/gzOmZCKgEfFmsHm8QYWVXOy2gavoozhDZUCT1FO/ns2U6MatiMcCskQb7s2tPNvuAlqLuiZqmjOysP6GOU8X+IQjTBI/gs7uI0fM9gjNl1flwLnp1vD5Qbh7oOWYY2QVnQpIe+qH8mmB7thAwOM7+fgXBRfKHpymn5aqxM9nmZHQYZJcyEdpGA3By33Kvv7kxzbZYWngh94W0Us5n77n1XyeQk1j9krXQx9SpJD3NJ4vcJ4A+nCc1xR4e9s62SVF+jWO+XUTUzZw1QllHYv4V10llH9TslFNXAr7p5SYq4329UUHHFILjVWNq5ZliaDqOHIgHq33zH2eedmp2L5GUZKJvX3kwl7YwTSxS5ta9XHWHUU0LgcM3paqH06hR4sa2eCr+1lb0FShInfcw11yjlwRN8AHZcq6f0DCpTBAbEAJQSLBrj2I5HOSAjjjZwcQXSUgBijj3OIJiR9PTugyG5q1234kZ1RiC3Mk+UL/5+Z5oeFRmbHcaM++ZYlyjjAVBYBuhnmKf3+wcJJ5iO8SK/1ins6wbsNE+pi7N41QF7/vrqt3mJulztNApWcPkueyteRKTH3q76jodmB6vwUkEcUbPRNJc/8wrPlPx38Tbnt4Y826gFU8raLCRzD6rTnZqS4xHFs8/RM/BeSGY7ksMen127sH/O+yah4qurHQJBTunjb396gGVVYtuIy2pyATIgwFO3YIa3HRUdjpC+GjRb07RPJs4xpDWnfhD316nZVYfJ2f3PM6WdxMAxDTz1WcGtidYfpSznE/W+5m67a4PRZo/w7J1Eq7+aO9MiVanGZFgoSUelp7g2MLxbIgtCiLpaARzh0Oo62fOjgLR504To5v16+/IWGG47vKgpnbnS7oKK+AUOl9NhANdYDNQNSpq/qzmH00k5RwkpRNFeKIS+V2042+9gLban+iJwtT5DcTk3aZPIhEFKO2KeDvefWF3wTT1FftN7i66q3pEQszGMCpfCx0Z67YpS1QQ7L1l5NMRaO+RgwPC+SnmNcAhnwe9wh817GKLR3eEdt0glZiHZ3u9H8yfjNv014l+oJXmZZaXgkhvKBRxvAr16q/I8U3ruce1Bt7kgkp7jhlHH2RK/Hm8yMfzIHr/5VVa/lrRkPUPVdCNY6yzXXMHRH/2Zg18X6YIZ4/BXnIlLbuWCGcE3x+hUruegFTZ4/q6HzTvCMgz8udPXAZwe8MjwUQRXnTSvxAhiNkKjP1P9RaTZZoB77YXz31CHtvOuCmyvsmuGBeFU82ZJ9Qk153/THHrEruvVM3Qjef9In7ZRZb04rPHFB3A9/Py98dXEFw7eAyapxzqbZuLBaBe/4XzO9CnANKWjjlJ1b9cyAGe88+0y5SZo2/CwL1Qrq/cAWmNnwBvTpsMz/nzjdiOp+gQpXaDst9KuHieMB6N6sPxAiMSceFNokfP0S43mk+c3KggS1BbSlIm551h9KIEfrRtkBY5J8GcnNKqnbhq61tn72qSCj5i7iHe/a8t2OD46inCQ7n0piUxeWPZ8EGAmQyG+I7YCbUfLFp/wunfX0buSsDH07VUBTf9kkWPNItYF3P9tQEmrocHVOXoo4XBzBlZ3fMQxtJ6nWoBNu6kojGDGEBhhcLcfbJIAYLVMuUcTx80orhPk1lvgdsRpKtz2IEhFn6dgmsNoE7p3ztelMosWPdGoaw1D6CTKCaW9/ZuJXCwQVwfzeWJAjHGzEu5O4ehW35hdKQVnxIog/OStq5q/m8YF6KWhN72Ka7ERS5rywEULnRDBEd/vNdXyzaWs7Y1ZTogUXMZj/huQka61eNdiuB5wTHFGF+yu6LRdqAZ2WpyTKpLY54tjfZuS1fzyeBxDEpE6srwC3/hK+NFjBJgwYFK2PQADESUuqDMhqUDSepUe/fMetl8YRV2a/u2MTYA1zLw0i8q3qy6bEvAY3CxUKEasTDXrBPJmgnLDGCc6N2Ws1DWoLyDkuNf73YxhQ1xfb3dHseul+uimaqYiMJ/NwGfDUe4CEwUGtYcqMHfsISZYs9B/t1fB8hKi0TdJ7yeMR0fS0Pj+3tEsEx4T8dGcPO0+sYjVcLI2CVERdPJojnlnPRYVWkxDrFuxrzLDlsJ4pgpmfM+x5MT08Eq9JMp+wwDfcpU3HyelbZ0JWQodQFTkCfRHGeCCaLS3ix+KUeqsYL5wR0sXDaDeU76IKGgxsMhjjQhd3Wc1hqLQAJxfUSWz/C4/52in5mN7SVJu0nyxcy1dwl0H9cgMHnpwiQJiOmcph5VDuDm9FSZbnDwH00IB3x98ORxqFQPdx+IORAJd7/METo+4jlvnbi2D4GEf8mJE5htXdweaJXzFQe8syMWdC3uBGnzvZtG3O7Nv5GbU5MTJ+8JKq97ms8/bzo6Q+qgP9P++ecrsfIPF1V7+unlo15uRjFBYFschkSsF941o0tE9yVTehrOwcgLo74Nfw9A6OaInsGqucFNKTf4n1QTJ+c//YIvLk1mSFPQjFvvaQHorYBXoA2+XqixJLRW8o5ugsTPWKXzPXNHIeU4ZYx4O9uof6nt58+rS//K19AhLaqW1O7jwYiofRVjxXfTC6+0eU42DdI29TjluhTtov8/73xTACj/92Q8cKcmeYQ/84ueQBnk2mczd3F9diGOOKftQcn9VplIbR0ysITlCRlA5lx4nedgbyyCp3Nk9qV0UE0LgiDUW1LzUZT3GLEOLmxlV4PjKgI04OHvQYAPeFxM7kLUQIJS8aL5TaHP2x+U3TPOna3F4hP9OG0ONYRi7zvZOReDKSCb8QrmFov3ewM/VMtboiVxICX0JeRPLucu/bI+09K+D6oae88zcmfrJqCw8Na1y6bQLV6wHceJ3EN+D0AQ5fNiZxjosLrwsYqmNTAb/H7ZWp10pqa02Nu1VgUIUjWBFM5w69rpEv9qtL1Lb+5fKubh6oCKqKSVNqcCkA6aadSpuFNs6ogALSjSo7cJ5+WmoygOnHbsYPM5H0j9cSDMEkFoogwWZY3Nt3wnj5B6M6eHTW0caCErj/HpXUInDE5e3UXiIWB2iVewNGDOCF1+vzsSZ8ApzCvIFRtHdEDQ5VfO3RaeeuM/YsiQlKOdnX8JTNa/x3OMxtkoo56K8++bElI9HFlErm7j2bJgC/vxEkCXlMKQVUM7giTnQKDX1Py6b5nY4nX14EaDf/77LlNwyL1C8uKt1LgE7j/KaJaCpohLcL5+EW4d+bvg9euTLG4ms1O77TXOellEqWMgP6XLc2ZDsX+rZ+gVS7S0zTDBrrab6D8G2e8vFDKRmk8Y8rfF6//+E5zu67vD6RLxZx5KG3XYY9iK92WLXHixZn8d0ds+V0boe3EVD6K/ACH8Xw9yhzJatsm00aSGosajQuazFtA/w9bshTiQNPV6vgr3mRbuOis110OyWFeMs7MKjlclDh5UfWqsDhF9DG9pUGQpJ8z0SalNDhD3/uihAy9in4krEOeLmD6G1vuzHcDqwTQpF8Vmd3jfy3DKyi/ykNiYvEUNWIbCRpn2yXtnBA7XymS6vbUQn5OHYNjauC/bbwznkOMIsYx3jAubnakAkXUN4IxRgh+fwQDf+f1uKobHlqQ3wUR6jk6w9QvZGnYttRY/+a9rg7RulCRQOFHjiuEQYMULj3jlefgnVlkfAm6wfcIFt1K0gLmYKEj71l8dYiRIgxIKBHBq9oDT4uOkSX0ZebKWRS5ZgJDoVwhR9o5K6q31A0IX3P1F3O+ztdpnc2pW34Nq7ZPUpkQgL8n0ivjLnrVHGh2APngUpv4bCB+nP/nnNNPl68bvT0BAjc8WAyyECBzkg+16UdoyioOaWnL5ouwRJP5pVpRrmLJRhKJAYYCv+5sDWZ+BSKw/4TMw/gctCRVlrx7iybUoAar1BogAiuuad1dWc83t59s+3dUksZSROuGVmtoDRZ0jlQuebhF0NGmzr9/ShfgMxWyVosVcwGnuBzORkNUzYZM1jRiD80/Jzt7IdXeWQoaOakNNQ/TBPWINZc+TRpkVerqntdY4CCVHgJb0CllTvGBEs3hrrPk3jzV55DvmbV/R8BLYg/+bzkd93K/Lee+t7TC3tLcPB4/kZtOytU2yBMvmHyEoyuLwk7Cjdxo+xRPSsOkOBonmVAZ5Ti4zCdEd2EWaw1+zA8Zm1G0mI4v045qqlV94BBfIyUB6vSAR5EsRchUipeoTD0xOvkgTnk9lHaXY/7TzId2GExJpi94edJJQ9b+chGIGuBAXQsVsCMjN506rk2EhxUzGV25jNJthF2mko4JT8PhHFtZMoWn+7FVKav7RApTY04m/RILlG0v6ypBdse1wGynBKUpdcnjWjXklgT7jrKRLbuqZ5dMsUrdRxpamOdP5ljDKOrsrtgambM459f07SF7qARmBZ0O6M7Ocsq94of67kZxSKSsMSli/KDGKqTfjO9Vc7JJ6W6crk/104dVo1VscNMxAM3CMM6G5N9Tohc/kZWFAt6cTeUyDvWqHj97gV3W6e8y1hT5WuaXkdZB6AFBCvQ/ZGluZSHMqNNO9VEfwjIiU6bSY/CrDYkPaZtNCyMa1PsHlPYi1RrlvZ3HKSRkkz38mE9nN8xjkQIEhXh4yoRl1m+GYwTzmd+V4Mlp1wtHiPIxsB3tzHmDsF4i9KBGi7KgaRwvr9HWaUzv8zGM2YzfHNcYY6Yq6gGMFi2U5FGUQx31vdnBA8t+yM49ZMLaBuOS7ZAuju7WVc3OSi/8RURwYsdC/KSw0lxoVeICF6QgldfqM2l+c4FXxWmIM/79+zY7EmpdG5eR2neSjMKrlRpj4G0MoLa/Qarrj8KJvDI276vLvMmd5HqKXBt83vXIXLUQDZWZgzKgICvcRtES9EM3cwqm0BBzW5Ly3TwmbvVsUJHNSIARbWLIf34X9W2RKt0O/Yv1IpIcg831IYNGON1vkQPaWDTzfr+T/Mnucjq8Hqfr/IpYlEw1z24WSKs/G1/nIXsxs4OxUuo70ePG2X/bVxHuf9PYqsfx7+4LHCoKH6Dvxyfii4w9ZOrja9vEuZHmYZ0m6ntXd2aEwnTY0yJFQz1vCdv1lzllro/wq4j6LnDFaHjmaDEXXelwU8hT0VgmymZ45wNbs5YV37wTVa+fS9GIYGbT+6GIGSOXpTUwRDJkdqhsa4x2YCNT40CCKCho2fTLMKKQQ0K4F4peYt7XlFHG6+uKFJNH+vTFV7S8RXsi4oqedUhHASEYPViPK0oOG9yNllnxc9RTiVK28mzFVQLMAFZHlb0FYz6V31POn8CfwXBHKQb0dfDVBM7krh7dT6FYs7D5TEzmpkaopKq32KbLoOZf2I9Bl7gE+ekduoil7yjMDmEq1HSC8rLFBrID8lYKsyR2Y0S+efyZWCjELciA8KeJ+iec9794WPyAjvT3FXeCy0Om/ffCYREbRp7WujCZa1RfkQKykxEDlnSjG0gVNWnSno3KZmfSuwPiX80wx8g6iBRrb6pcxt+k4lmVVP1jgQMOnDeEX/jWLoDPCUc08PFRXvJkapN0g4zVS9txlVDD3XS5jcdK1pbmNm6S6ejAGh7fkZ1lD6trXbEpDZzVt4z4eL12tcRNM/84Vvxmf4h49eMaRnGfacPzCGVSUs6ZpcPtYBPGgrmQVG0/wZHezfjC8In+R3wJ6iqVE/nTpUTHoxoG+uAI2zD/ukLRM43lSgfVptqwOiiC+k7OVtPkyZh2a9eFbUPzEWl+/zDcL0gcOuIqsLG8N34AFudYiDpo0Igbg18mX+ZUaARlVdZOLeu2YSdDkkpTv2pCjt/XqCjhYovQZZ9+w1kOoUmQKfT2jiDeP6ZzmeDfxvBVMEyWACzlcVtF3B5IqD38x4BJUkENZtqZRxcsaOOgHf2sfHOrlkZp47HR+3YTAB03jw6/MsOxQTBc9wW/kUhgK+PP5tWHcZguM1UdRiQ/CGUIsVfGHn4qV3g/JxB+WRdzVEjx0d+FICSvHJ/ERtW19fC7PSJX/PD1X5emco+P/G0bw1d+/7g4QM/6uqsZpOJHrL5ZjUe4ydfpeMA3ZZIoca2ee79HNxVmE3k5/7SLa7cuxSqrDHshDRWZR8adqCbhOONaQQZUCOm04lbyrEDl+p2PviCytT0HVT3/NuCU6euHCWMJBy0ea6iZGOMMO/Y6HCYRJOYsOldUo4xIwbvaij99hVNo5fkUyXeQMJqmtdWiwQTDc+ShjPCTewP/QWyJ+BfeRTupLEIbv3bGvxsUh9xUdMoX1o9mqXhIOEPysHeDc/hQSnyXCzl4ZVETbcoq3pPkMhup50DwfoSI67jqqKWhNJ4jnq0C6EFbhArfpIm6LKwjukAn3eaQ6t4fBI2b5C78JfY+ut9NnKywIf6gPvJuEOejscYJXlj0QnBBYCHIP71vX5rrsXxnKX0+iCrArhVn4vDutBBZIbBn7y4xUP1128C9EngiHol2SVrZy0B6bjOC/5Rz4Lds2P0PcPi9Vl40TQQqFTDqKPYf7N/wxgI+9Xg7r56EqBCBq8ru/dNfZBC6avfj9V0Xp7XtBrtJ95Ylk4OreqhD49u0SPlepGFs8YpKCi6t8V/z6t7APr7w9Yx8wtbmeD023Kz0ePoKQTALS2mCyHstOKp/oVEPZsYAU/Se3v5Tzfkhp3FvYQLZnCjk2L+TPjBUgazt/XeAhADIL3vYkOYyKKO0NChNTsX4ybTFwY9nnCYpBREILl6sklCiyk80UQo1X14g+GFseZAGtSU0kQ7L7m6U738sQOpg1LUgzh4A0KxR5Ta2Jlc4f8WDtx0EqNBwkrVE4pqhchEQSzoAjMlsg5I5u2e9+OwJfdTfkqrqRe31hTp/4r7IhLqwAkRwh0XzK8lArZqKEqzK4Q3sZ2aTTrGzwKpLRcLLvL/lMpmh4Se5QY09pJkBkAI+fxUM756QjyD35QuufTJZtPHdHhU3x5IeAR3yp6Hm6kdJMc/vPqpsUXYj8Xw9damzHqOVh1vZF0p8JHJMCvjtyrTccZV7EB1ce+cp7a4z7eVRKCW41KSzoY2zaUfzmWJeIjzmmufQgpXav3/kUUtnLI9mBw5mc7AWd4mmgOm6EXaY5SVvGFJQD1vyEmmSNggZ07wCkCEc6QRcbymK12fqrNNQWh/zXkS+qUveKsF2xxwxRehCjCdhKAti51NPSQmyoz5YxltVz5EXcBhiuiIMi1rBy40bYcbw++IJRhJFqkoURHXDO3Qgo3R7h+ZOW+ooSisK5xwkBe0Q4Jafl3sUeykCBn86VX8tIm5yKp1Mtu4LKqGhzxbDYM3dmCqwTSUj5Cfl9/5PI1r78bE5i5T6+CC9ZqhAe1WlbwytfvUHQOuqMa0mJCFKIrCzfPyWtbkXUX0SrUDh7hkFKUZoyU9M+4WXB5NOphZKPJCzOGYzuSm6DDKlMgWAy6kzBrl+Qa+DOR/WrNd0BBTe+bS6XnFAcQoBOjTmDn2bHPvz8hzf6MjL3w8LZ6YUXQhIe2o0mrN3i7ijol/fmdeE8/SaZ3eGJyOnZhmT0PgwOxoRT6UxJe8BEgfWHTo4EtZtiKVB6g5BNR6YT60jgYUC019qLFmKiVxXGO3ebFe9L/wtg85XGwdUDi54yAtve4zE1Cj24xB6WGG+mDZ2w3pJXKECeKLBhbztL3MtJp+QkfhXMY8fHeXxRSVHUa/UY3Qm1iImfg0NOXA87FQ+uG0fVSKVB8ARWdOl2xc+AIwiy5XJx1pOAdX2tX7MZ0GwNVQfNw1U6gKC9mEJCIr2uZjAy0htQzVTujFhkOPXVohOD2Qm8hKT2x7qD+ckeSH7YWlij15lgL+vb3Gnbh25mBCEgbGxJI1CAl+6LH6ddoZoNLyNMVtQ1BQpAGxQRJNg2JCdSNW8svaSI23J51N3JnCnrP6OiPVQOMXtK2zWp3rlATNQW+Dh7O3jtTR13oBHlcFMHOfzxdqT0FdTwQudCkyMaekf5/KPBt7NpHqwTmcIH2aQqdbtLj384UDtAP10uI7yE0Zl76IdTMUx/zsXmp4V3wuVc8ggIMusMJ3t47ecldWKll45lcW3v5xrSWTgRf0bfRQg3obQS6py0eRaYczRf0QBBzmXohyFaGvL3FpoTyvztUDVmac+4/eRniXPPY28AxEaRS+MkkNnM7q2Ut5chpBqViG6ABBuc4Xs6LjgYvr9urx2bnpN6c21TSHdgzL5/1k2GMRXk/IeMKj67rW6k1YTNVn5P2+CuU4Me6lX09ZLZb5aO75jxgmyRjEPKuGztl7VjSPhefXdp8URCNpyXen06Nq3mmAtc3JUcTSXcjp3wshl6zWSGCH5/Jf/EOQa2qntyT3s4mZwFSTVHzhsI+asWCg23Fn6CxaS6OSa2QLmjiX7dsk1fg7DTVMNSWrW6xMNvpPVFxqTpGGfaZ7X2gE/Q1S7QYFwxyAxNYys7XF4nevqF96cn8c7t6NWk94wJdZnKg2Jc+vg8hN11ysKP6FysLB467iyRJlOjsRc1VGtZnUT7PUtE1+R/jpxIy7CuwAITxUFfMZZbi1t00rUxMofCSXPg2a8LX4wLx2I7gUmhZvl0574d+EFmQUGY88Bpue3tnZmVB4/FiHct4np7h59njw1QDyAIIFMmkRBTkbUwrDDuscJM/4voUrChOkJVj5o1RFDRHdlIyxDV1A9Fi+GogiRijayTSIiPVDH71I2Y1Oo9+ASZSbNLT+A/b3dZ5sTO7uEV15GfIgwxvgT6DzmHp5cNfRERxxIp/1sxGfEvcYAQKODrKgeb1hlcf4YOtYQ6dwhhWQ5C4IVwFtePH1kmGxVZRS6j5t2aVYMhIYSjMEMUXPFMuhDpsaQYa5rGTbygAgK78j4waJNZBKH2eUMWb7jl2kATU5XKAgzY6hS8VJGdIHtOgJ8DrNhVkvGC/V7D+xkxoat34sJMe/NWZHIac4hhu9TiLDs0/KJyBEz1hl9BSQj1//9hWGMutn0IH5vDhwTfTD8SghOqGvxZ8FC8CST3chj48wsYAMcl50NLbRwTZv7uOdLL5F3Uqk1iPt+mc6luCbX9XKMMLraypNnUpWlYKoIt+AI3EB8kMrr7ECfVm7amFL8mwozyRojPaE86CaV2o96TpQyJVxKYPmjrYki1bAc3eYXViEaE5FZk9rblFYNSyKCkC+c/lxL+wWeA/NlNgOnDns/lI00g0yBO9j6agR8OOQIcbvneCGP+752kAnudBHUdUREJMYsU7Dzo0sZ+p1Zn/Fva3rhAykcSOfZ0QRT6KkReo7rVNp7PpnFt3HAjkVNQCUWdZmzwko5gzjYBjgtAcSCxW9Wa1wjNM+HnC3pjjVnlDmniHCEACVBKN+YLbo+vkVyLP/hk4HEhmTYcXvDrKvSE1/b5DcVu094IGF7dZf946XUXr2ZLMhbzxdKkRSaq6TTpSmjsotDDDwWCO9U5n/auuwxtOnEdQFaWvr51S09CvoXIiXrJSfdiNP7f9r2ua4ajeaWdc6MqlKuQKAK+XG4jHae7GYoax764nsV/L9rD+ilDPjOcqGFBrmxyTv0tWmhAqHKXiwTrIPomGgHm8qdr0NcOrfv3Ihgo4VsNmTvQMXks6hFpc2fkCf537lYrAEy1i4qDYRyts6W2fKQYLV82xep5WgY78zla67KCcclCC5F8evXeyRJkeOaoyXlBmpaYjHmY4lcQbIx4HF7vk0YHkvdpXmOpEGlAmSgopc/L90Uku6yy/lUcejp/axrFo/5ZUoX231U+gAWAniw22fPIGRdLleulDZf8+cPKvCZr93wzNe1c3010/YshU0TcPeaggeecyQ80IUMlWf+EasTEqaww6WsqqkaifyowP0oU8FggfwWu7tVYOR6vVbsNDdyru8LBX6qkogv5eJSOiUF5Z1yO7kWVm1NNYGIRjiYx/a/dvDTzF0Rc9LHCYcwaeAx6Y1OYfFi2hNnIejyxk4pUHmHmn9eDCD5iql8xbycy2zxuc6n9gPwcJxgYqiEdeGh1suAIIzA9A5dJZAPJ9NSGKw6AUCMRvIugPN9tPD3lUtlB/PXKi15khCUumdqdMyaspRYfBpWYIgDkhbP5VkGQiqwBJe/jjx+ARYXzEZTP4jLR9nEiqAxSDfrIj+aS26dD15M4EICWL2VdkoIGSh68XU1d0mYq8wbvbCBN206QtPKpM6RBbOOBfENWKuD5TA1FEB6/OfVi4cjtEz5pXwPDxYKFWDDehDKdlk0FOld6vy9kDBvD/G39JVgGhs38X2EBtahtgOpI9kqRYYXJntKbEtc2s2H18eyVGbhLSepDzXivbqXkGmxLvARavc/+3fzsL5u1iv8Z1GUIqrg0v9Ie+Llhkz1N6890pWXUJ2X0wweh/q0A2y67PnURGZ8d3ygbIbXz7VoQMJ8mHF2/uyAmc8E/LZzWJWHwVSRwBeI9ShqyZjiIje4DN1CqGgwezHAgHWE1tfXdnDi3hED0onGx62/vQqKzVBR1lp2schNmSJTehUY3rRKQ0B3Dvk5HvaSyV2Z8T7QrXpLYMNpfawotKXky++ALOMpB9tGZrMYO5jGh0dkHqpbVEsReFGpEuuGuO8NCjnaBDhJMG9vVAGUnWcyf9nxi1Ks0J7HvbCutgNZuCpMNzWNnqUGxhok5L3e1xHJRBiOQiz5K3W4yysM+LwIMItIuuvn8KQAg02QCidJqWFwRnskM9YEePeiwvs7WOXqpgGWPQPBLe1QGJYbqGvIcdPiZ/0BmTfacDu8JrDZYQ7i7x22nAB8b/UiO/glKo+vTQo9o+IXhLySI3uSayzLt8WKA6isuV3iYnYuU3oyO78kLP/4C/bDG+E16xy0O++2p7WKuEvD7HJG3mAqoCU1+XxjDI3MQY59D1iI+nsxU7LRGN6dIplQgOORO5qLi+Qfo/zICiianmYryAzoKW3TVPPYyXpB0GmiAfv1koc8kMZ3vkXerdaByq7pkX+9yKGbd3Q6E+SRKL/yQhTNqrhursw1ed97oq6Jltt5RfVD6aZen7dpA29fFDckcCl84z3EMffoGFNsDgs3vlPLJB4PF1KkBH7/0sFdOWiRaLJ5XgZPcGWR9EgqEImQZdi/B2Y9vN49fOJcpAyvqd+sllEydbIjI5GCZr5saKMKLmYaBTFGAkIm5yg9Bfyp0F+Zsjx+JHSJsV6VgNuQMfscoq4M7xqi889psvTwHgXQl+XiD/D16XIAKBpIoQZd065DujBrlbSmiJZzq5VcnLYki3bU2047Kl7NNsfvm02zr679ciF+9iGVDqqGDwZe+5yCUqX31zi5o4kVOgKTH4yPDH3FVrqyN9DkhxquYkCkZ+n89XZhGVMGi0HbiD66Z6bus728DvKo31DNnqGp8P1hYchuiLSVsaga7OYzeWnmDVy0WEosyzKWBuvFinjA53KyVAtsDS5pe29lSeDI72Lr5FOo6Yn+DCRGQZGfbCHm8m/ouHIiP1mJhd6IcT31HJ4Zh7F6F7HnS+g4nXAexx3o1mhN41AOgHaF2fnIajUJFTMoFzoYTzQbuvbtTF4hR5pLGIfmlIWDKQOKTJXjMhuNMxEjdmaR2fGNH5bkaickPr4/5VCqoQl925k+F8rxVmUX6pbVPJe6r7zegcMARotcUy6174o39TOcJNWA9lgdd37GV6MxFVFMvJQ+lzhYMzVPV/o8HOeSdUjPVMmcgX58BBG53l4Fc5wVLmK6genE7DX/86t1V+zqnMyjvDtje3aWV9HdZ9nuPOq7DU60+FVMSp5fd17s5pfntioqx7mpVW90zhKmHEAtL1BE9KMKoAZP2cnMI06amk8/93pm+onHB/TpwiEQ/Dix7jNyILfQ0chV1Ta2vpUwK/1kpA0tKlO8ym8KNn/JBh70FLghi4KnEHSo9VYk+AuIxluzycy7ijaaYvyfnuToekJ0nwLSe65fZi5qSPpvAbf/oHocWxHzJJ5bdxxIMd5Pxlb36CuxKU0CsusqcaMkYpcJd1+8PTMdqSpHWOK8eCDnz3L9HK2XrM5C198Lh/4t3QYdsRQs0Ot10mAprbteIUr36Tqq07WfHacULv7AB9qt3Q8BSsimXNHyJCBnR/EMcu/wW+QVuWwKcd46YdKewhuUY8ZbNx+TS6PIEv8zUk5Cvvm6RMF3FAdRtV2tiaNnm6iwjxyHbGHb8izrZt1cp9oExqeklKI161ZnaqyUjoXiiowf/Tq2BdPlsvy0Ep0hBtBSsodxmKd2aTYH09BnATRocjgojrjMdCX61obK1iqIhAmsOmIC5Nqwk1cIIm2K4cHQrx6DP07M8WjU0XNi6bLedjA2Zz0mtU7xXJmjOK8sLD2NwqcqqNwJj1R+fzVxMe1DHihiZmEB6EyuYbQYd3IUNBL7Y/P0gNuPXT6OrHBNDlFu7Gt5SsQjQwnMD549y+KYWJl5GhPPJF6xx4nuI5efVmSM8jL2SfmrVm4+C0Qu3hvO0EzRj4o5vapNRVE/1kevfqhvpxgQGrsE9u1H9+SABKPBqCwUK0c9LaZdAyZs2R06ajQNZSpFuw2Pc8CaPW9IyUdDMO2fZhL+id+RtQnsnWZc2wKs2qov7n9iEmbSc531pvSZxzV4094XPl8v/Ymuz1J75g0z5MPjyJReJzcI4C0FcuhN0wurq014JghcS/3KL+vaSes+QFaaFr53e8vhS02zqp7PEBDZfzWS3HhSPhkm4QAmmNAxZ9TyzMP2tYp2iy1e4qopPdx8MaLu/8ip9V6Y/QuB4YVOT9P/7ZWtUZl/PIEQvydCS5SWT2mXcetQi0Bf0F+wyP4nzCoEx1Fct3U3JFmAhGGnShGo3W9M/ZUyJmRT2CwSw9cl4hnoe+uHuBQg/79cZoD2vTxf/0f1J5TFLk2g23A9lZuEvVjoQR253l7BQBXEozMCmc+1773Gb34Z2RYDspajXB7LgX5uzgoZniqL1v8uncTp15+VbUQ6ucKVkjWlPDDmTLDqf9sF+rhdql8wOwQ6CYkw8+D4QlypuOdWpLa8OMfmycXAw9OE7TMspwMpFlU2+a+2n1BSrfM3C7VuoqtnimNe0LleLxSzkQ08LeArGkIcU/cZfDY1qtCsNvsoWFHYbRb0GdkkNN1+BlFDpxKPLl1Q8I0DeCIVfbgVheSmmCRMOAAC1EnTc8ETGQZnt6AjRm42TMdQEYBFc0n9catIcuKj0hs+7442BluACGpESB0MbSQ15+M1AW3haji0N8wk+uRwOH36ov00H9dkyc2L5F/vjDBH7h5NkVp3pvXWSp4Dj6geyIAv/ZaeimlhrVLjjwI1BJnulsQMrW/J8DsOrYYK5wRHJrzJ7vIMZ751Rvmy9qC1SYMYm1Te1P2LhaOkmmFIYmzd5RecrC/H0mNDA0pY7QmKr7RsAyKNGQjmcu2/pYbqOW3IMHKpcCl5S/2i7daz/WEXqIsCKq7CfuA5AWwoIAyDtf9nMNSob4nJDOCDucXpk1XPqwZClHahaQLx2kGRDwgBTA20K1J66f2lJyX+333PArmpytL5Ht0WtNJDNhXzBb8O7a7zQMraUiMpabAtPVmsIB1bAov1o242Lql6SHGZbZlyRucllfuJG4B8A9lEuai+1DyIk/J4oFeSu+p8xAO1Um/kQ2GWQoaUrC2Xy9xWvy/ffBWVKe6Jr5v8l46BOr1rLA+yBRnZYvq3adg9vmrki1g4143UtblLrR/KQHf1yGbUJjcVKiG8E89q8cQBY9+eDp8/FqlRFApNlQFQ1/46iF6WCPO2V5OVUebRMYwpZkq/lZoImMyahx4DVMceOLawojygDSBabimYHP2PvIndX3tGPu5bGHx6FrImKivS4T4LU9hdHh+XfRJaaMSXmamtUyUucQY2lpDadgmqHInKNn9kwt4vm9VI7SjG9xqyPsHw/9NBtQhRUBotQhvBFc2h54JkxvDQeDYhKS5GOVQ8XfBvPXl2Rbm3Uivc/pqIUkKcTjQTiVGNdmr+kwLVysrcML1W8mHGApdOMbNG8FzGYoVbZ8tVBikM76H//+JQ1nIGuAWsz+oIEuZUsmsBSlkCB4fQtuwSQ6y9UwyS/1cGM4/1bC5s6NDI5kphc4HrZJixD8prJe3lnk15YBrdakowym8BfeVgNG1sNoFmdUOrzdITRRXyrcN1XQ3R7XxTNcJ4cwJ9hfJaJb+DgklYMc+1XZKHXUHdY6elg/CAwcOhddcerIRTxM10Pkg/pu6+Ox0n8FurqKBZqiNNVWsqlLujBBEugrKPFcGim/ScTlvFyYzrahQiHdUsjHpl5DV9sBNBmGySNVLel7BK4x82aBxvWW5XOj2Gu+yLHQgMOttr53Mv/ITq400TED57zVq+8JRrreJ1QKTSGuvoZIXlepYthKVk6CrQFV1vTkgvN8ya50Pnq3+hmqjfRtyA7wTPcmE1T3v7F4vr0Y8EkXrum1sVkAxgztrTlP5uP3bR7E9+dFn033b2EmtCja+Db3CKjqbJ2j78uwHBbsfVYH4oTask3JQrUGtbUVillTt6MQmWbsWTzRb7+UAuLqsB/J/zPoCd+d0WYpTXcMnkdUAKi+QqaxA3f0CN5vkNSMIe7qbq3zSWTIE+Eob7GFOZUKse70lg4qD6WR6isVZboexB67yoV9F586dyQUseE92mHVxRSRJl1ZP9DYGjYR9Ne6W9aW/gYz9yYsLTcBo5DQajl+eDJJ+85rm9OG2SdeAlYrlF9hQsYb6NvvKNWs2HY7g14j1+yqNqEjMss6P8MJewlXat+DPFc0ogIrZY4K5R3ivBFKg0C5PlpBuNAOKh+REuCDckELvXarO6RyuwOFYKzfLWIPTNDaaKYKY24jB062/JjD94IUtUq8W7C0Eeb8KCdNC3uFjrSgscmJcqY0ArVHssKGNKq3ukIQqNLPNtpqUhKrzwfgDL9FRMM2UB7e/wdiDwYdpn1a+5MGXWij0F1tjURSwaIQDiQzN2Y4H1Zeo0y2Bn4eiGmWL6jBVzF6sjFk4WH/edZM2Be6ejRXm1wcvnWQ4loeoiCy9npXpy0qt6ogWOYiefFvCctApfYqc3jpN3lmfYBhz8WJdg/+yDZdAwJPB0H2C2lmgcRhjlK2Vzee1zfokf1zeuOKnGRokTgSiHIWWngOs+AZaW+QVAqawaqwX8qtQv2GDceHvPSNOOHhNmgSXHXwuok8Abv055V4Pl/JAtETbYs+ksz1xs1W1B/ios+JppP3YqD4GY17uxLMvY65XuvV2Avk0D16beADjwhzQyPsILFYtyqes1Wgx3cJTQPmnu6BVQOKPDkBI4mp8yC1oxv1MTY+qP5jekLPaQrC0//VisccwYOjhV120zhou2A29RZFFW70fD7qg3NO0m9HLph99EV7CBJrTu5UQIQXX5McWrh2MPLDRN7TooH+S5u6CKN1ws8yqIF/3+OBVtLwIUhuOo+vHfbqYDpdPEZjx6M2Mp+NQIE8kGlN75vU31PrTgTqMgAkxQX8sYh2oacDV1nuog6S+YLM4q0AiRiDP5KLLg6jDUv5Dpcy8KlYRSRip/Sw+EqMHKPWaQYR4thVGPWhBiD3RYP/dVcTUF8Zb558+Je7QOAOVuAYHVFa2RPPc71BqifI33cEAxyZ9/DyeorqVBwaFnJIwrMbye3IuNPmCIACtH/FPxmU1yRqKVx1Z3DX1t6Q7ymCZ/PuW0/vlJyjl7l0DMovDohzF1tFfkN01h4DeyTyKSymqZg8MP7P5Nff0OMUa1HVa/pZP6+S/JYwCQpoFqXo2P61bOY49tKBUsvBrs4qhg7oer7aixb4tcYrp0atI5041CcaCQyIUu3xcgFag6HXTRLBDHuFjqLAw08nWdQq1rYtkktRFqJfWn62Ziva3OC+yrtp797yZp2VWzPvnJSQHpT/pOJOCpJSyQdEOSFtIhKqicPaiJgjFwTJS6ekKXy2KasFnG8ENJXE4bEnlK7oprzubJq9t57Aqk0Eor922aJzQmglmlqTWJm/U7RMtTdqm67NiR6+E6CKusblXfQg86xJ3LCDucDg3uLH9LartDeVGrp8iXuHVMzWcFFu8pPBWnVwbirkgLUYiLg12CMF0UXdCx45MSIN3XDjmpqG9zu8b7wwmgzEjR9Yx6oZ0/qELZwjxFp8nrNwlfovCE2aVb3IzFlyRgUtqju1J34U6ZkltwH9cXMKBy+njM7xGR8DwKls55ECVF3v1PfObY2xh6UF9wpzybtYlug/S+LxR3yfFyVwt2sWHhp7uSP6Yqsd6N6akdWuH4aEyt1WFRhhhBlG3scOSW/efzzCkt8ZvHxKq//WKOKZYXBtZucc6UDBgQHU5/uQ8r2ZXNSNyYWn3yvRsbNMFUZ1Tix/x8+DZtffaa32v3ykFSRbPR6nt0bRGW399HH2nB8pa7BpxnhBz8peHWqVY302ku6xkMOMETv5YAa3iScCpuRZqbZxlrJycs+aed1o/RqBwjHINTKbpqicSTtbApO00eynAP9UA5LuA1sqtPhT/a/GxDLK8bvuHZi+5pHOFpY/UHBhXonx2JdDlW1VbpXuiRb3ErZbOtO9srkXyvq3l2DikNky7XpAx8jUvFe8PR4w1o7cnM/3e7FhwqaD3CZ0mYo4OWu7BIQ6zata6WNz3Hf/whiM3zYfeaSq/FlYrs1JkgTDNRr6r8AvH2cVQQ8R1xLjXvD0ke9efv3mko9CODli1temIb7I/SVvt1/2FGAGiIzqgI1dl3TTlZv2bwswhJNiOAWE9+qAcglJ5nmBOhrK9mSGGTpdTv5vot7fPYySWSh/OXCCxeR4C0xjpC/g85U08Kru1xxevxhdz4aR7g+QTVqVy5pZ+y/x7gBsWNo9ZEFEnf7qiUGVGddzUW/qYpKtXM3JpfhCDPWITsbmPlDyEMQBxvzR7lGHnDgqKPwhydkaMW8uMqdAKXDr7R5CymZdjzCLcIAe4hO/vEP6N+mFsbFf5gRbQzlNzaRVKqe1dwf93FSOvVo94oBpGqR5Zx58KybHpi5gGhSK3woy9VUreKlOrpaMb1M0E83CuOjuEwBq6CLn0I3/8QvRW1meYtzFmcaZXntQXSFicU982G8zw/TZt1peO669zSz+D9afm3FWbszn2DhlkG7T1PmjuylIOVyu+KKwBsB3Lu43ZoyqihVOI0dqVh8YsXRL5ZjGsOG5/xuIibbeyjeS9AvIrlP5auduwfXvVOJ4+bdDsNZ1B2rsWh0G298RITyUP+H88rXKTZzbbJ886xil1v5hVqxmXlF3EKWbBkR5LY/CicoxLlP9qvqkzDhDks6BCSD3b+W0nwF0xq6R6HqhKjx/q0Wpvo0k2ihqfgedRK/HF6weMSZwM0LfppHHoeDJ+wUuWDxF6KmA6D3ouJ4a2Ni3WNXd1yUXTu0dHvu4QA/QlIuh6VwZK/Yto8R9PU5XSNupHIL3HnUCOs4O7Gx+8O03OsvhT8ZTbQyszA/HuTaGJZd/s3XZ/XaVECW7f71/4iH1Arc10RUny2iFRJqcIGFe8oxsnL9GdyhwkQJQ7qXvpGwIsC9pypJmPvjudmuTasSHg3VImjGvBihLw1M6HgzEZOpqHMuGnjCPWg3/5YiuDsLHEkoOK1gkvZomn1Xsn8sqXOQMrCg+FwChvmO8jnanBnT4WuMXoZrd+uEYm45FucvwB9Y8Xqr+r+b5FIGq55cjSlZz+vkT2IELaVAXzwmAmQxBvKQzalRDA8PJrRsVRptu1W+IbfOpE7+WnFMmvl+Om4Zsv4WZvxxY4FQy9leXnn7DqRecC7b9sZxvbqysKTFF5mKx5RHlEh9/hGGilBSgZumO+/lTMcAA1iwBsBuO3kA8+paXfVSXGLrFp6HBg43gC14/0ohEI3TSrd1V/xDtgFhz69UnkUxy311E0R8KXsYpLD7lqoi1/HRupX1NTiv44srq+O/VQY15ic2naelZNBWwDFVtHZUuRK9U8At69g6Ty2/T1DDKq14xGbT3x7pzn+mbsLCM5lbkW3o0m4HRcISO6d0UTY3s2dQVPR+eR0CsrJhaAUefpxe1mwtBIyTetFYu/b2jQZCohWH0K1TZ0khdWNlSa/iboaDh1+rY+t64Di5DUamqI516F9aqMPs1JQHn5326eWZuKXUBBd2wfPwsRKOyGRkpsRTOEBaWic9c10QO3BqFhJczrw6bon86KKyBzaE451F4s6IbQbOD0swsZC2VJOanZm4wbmvsr5ci+JkbZlx82+5mmKkjzXbIT0jsxl0PoMMdY/dbjFL5xQrZtZVQStAUgYcqJHDKR620MIcddG36tzUWdqTuKPqV2JF+5Yfo/XwEQ7seUPENDVHCumNGMsML7qZFDCWg52J2ZI8FU3neo6ATrMasBvlkxvONslnWPaitSE7mtI5qY6SniPSYRGc/xiizVG96e8jR9MLX51SHyxqluyzE2jvdvU9dJg7fzYrz44zJ9QqV09Ay8C1xEojGwsDeMpUlt2qabmG5ISHPAPjeNnT31wXKzOqvryLwplX7FJlw/G6hbHT+edklIVTGWcSSv8uEGHFFaG5cIXPxTqK7jokadxluV75u0xlkRs419xLWRrGirQYXTI8B+mD5b0yoTSWjSlqJzL9ujk4Ai2NPTrAPywFQPtWJl8QeRtvghlv8HYVUWdZx8wNuFz3f7C/p6Hsk29Ocdj7PCrjredVTb2uCpUc8yc6h9YOH+ahhQthut/VjD5ujF8u0JtlKxA+OCIwTGEgCaeFtA5ZnUj3F67qPg+E+h0ZM2TdGKDIKuRcdH0u2ETP5FOQBNQfQJBSMl0uAn3o468WYxKOaM1iQnoleNXRxoaimkrJkMNHO5C2T/AOW4yZBnf0e/o+xXKhAd6m8zvSqOTGVX2vkL4taocVsz5gq6sIKDTaDq8N9uG2XbGlNMyQE7drnobI8fSyZFxRM8jKl2L39TKh+fTEYRwiKxJaU4CCmKmlc3Xl2f2cGIuQYbCaIsaYUeVKxdxSSfuWXZpA2fPXlgPFR/c8fEJ+wQ8Kp/a4tW1JUFTIziTtTXgSevp+1+/UwTXwftJFu00ydBbJ84ft2FUxzLJCygjZgHKCkgvK9YlHr/62D2Y3sOpJ2+q7vuSxkho4qFj7US9LogE//OP1ErMl3Ul1WZ9NA+BPYH1bXCTKLpNCzPjwn5QEwwi2vIwVAT1UZqsD1ZagkGDBd77sTz3oh7lLiLBimZNQQ6kdH4WZh4OAmgLZ1/heKlm5w4FSWWGhnhUR3FvkXidZQ3K7ikbX0W9mIggwOkzxNi9aerOKMWx6tDUpbLYea+R+1dlWaA8BtRpfw/0fzPOxAw5D5ghpvB1YGLZ8C49+8Oy7RnM940dc/HCmFOrNxt7VcNTnCFl8ITChhl7SNw8wpn50Jsu3O687G+inTN3dkw+YEMPngMa8SXDYVGfGe2NhxaCoXu7xJVt6B21u3TtFexWtF05aL6X/LneZJdR3mUz7IOrUwpFbNfbhRuxfmxkP8Fn5oNA2T8qLfaow9Ig/8Vde1M4p5ByGUseXurICWpa74Q9fwxKcG3hxdNfQQNnskagMwQkE6uE13yyfTgxSusafvebkWcibCS5iOpn7KSaqQYB+oE+BNgUKrcaQe4DLXk2AWFBDg5ysiQuS1wQs28GlWWQPz9OXDggcQL2iyMPZKUdwsANNVPwXLdYwfhhhvjPo3UP3U+n5sgco3nXBQBYK61+slhQZp7seO7RvW3332jdS6H8ZI1THnqmlxmqtfUKg4QONOJx2NTUCIEuVxayha0r6Uxyn0E3BAvyGre1GMBEfyilv2Rbq3wQedcxezAxyR/7CcCYyXHyrYN43obG7/X17iMEGVDwf3AAZCMeup8UFBpBmOQXZojn+uCNLU+mfJrNtKbMJnVpHyvGdMhXi0ansaVgCUsGYjg0vk2k0RWK/WL0kc1kCsN22ny0LAXVCTPfCx66U7PKlDKftvnboWdK1N2fw/XeWb3Gr8S1B/2/JPc3nKu5OkxNCr8/yI6H0YDhVL6xRkXzuGvIZwycXSqWufKqrnSnj0wqn1YUDForyQglNcopF1BOi8WbHIASMmzJE4/pTOAyxsDS9AbCwGgsG7MoXKOc1LRCD3hRoe72eQXMmU+CeL2/g7KpYusi5SXAqVptjtwuPZZknnTK2UdDqrNh2fQEi5MkHIWTXhSnGQYjo4Le9VMkMLh/LuF7d1LilSttMGZ+Dh5GMoBLjervCTsGGU/H2l3l5Me+b1Adqvl2RfIJFZzR1jVEYRu3Y8AjKqRtO0ARlHfQrPSbMT+Ttbwb8skBYjrGg5NPM6S1FDf6uKU6N88lYuxOzEJ/S5mD9cgS/Gt1Uw10zPzrQJ8/qu93LnJQsc41sCCnY+NHkMberJN3xA0Na3qQcNGDAD28CgWu/c1FthnB+2zB5AAmLBSJzjFCrtta0K3nwlvFXozhyBBq5RmSI44K5fZeTXzldMN6aLTGFedm6ZlmUC0ztlE2bEv+H1AlZsoxSbC0BGt5YeaZxm/QCJqaJ+ZZs6MWtgHVr00qOgKrTCd6qfNnUC9BNBNENhGO8B7ejCFTOsLvfiePnM+bf5ql2xfTNxAECAE8gkciaZMAiQCyGGdqRxVuZH9xFWzx75e5yhr3Io5TX3p3mnby6OHn+cr+8r0ZCJv5D7J1on13se/aX+hKveyuWOasKOisW6WFV2e5Bm/uyQccn49A5Veq2JD45pJD8x55C1JwQIjrTonpcaFHvcMLtINieejojpdGFmBLG+twKPr7oR7NE0b50QtCS2ZZcTBH8shcVW4BRjMTnuYqo9Agf8Rk69vcG+oPcTI2ozwM4l8+mILg+GqGS0WNrP40ctLqGYlC9Kiuyi8AErpH7GJEomcufQ78y1HLhl0LMqrkEA5v/+kMWQy7T8rIqEbejmbNtlLSceFRZIQ427MgWksDw0Fez0XMv9K22SJr/IJCsbisKuX4zQKTqe9yGVCg5gqWtgtoA74Hvicxuy0aXp+wdli6tETJ3MFrUOuGW/y10WV7I6et/b5xm5cLPyWM1Ac1bwF4rDcSlpO7UHqmNGr9O1iyRQDK+a3cAw77Xib5iqot41XUEoExAMhlXHqoCYLUFomCHD9zBebGvfQrVJUJG0aBHeNjU/RnvPLn/sn+PErzxOqbyGAEB5F+YqmA8y8iAkG1A/B4t5P883JBr+ua3vskzoqW1KaLnDGKWKMjzSDWQSLoPFlUAuk+jX1fiY9MJmt/PnRtNVcgXm+3/7eB4dXLfp3OLDezTJFyA8/G1AFw+FZg0kj6mBpZFJ679rgxAnE5ySOX8N7RTzk8jtS4hVX2SCv2keykVjtUip9OEEDQY5HcjPX6QILc1tEunKGDkbkq+97WK1m6r4nOIJ61l7xeFyTNstVBp5Zk+fyyLTdbPqcTYX56+6c5r1pTtygp+XEF1VRkUPD7xTyWcllBGWCYffivVVIq9rpujrrkhdKWFfiVoLhDLK8vTpikNrtSCMeNg+/ldYK7ulLYYk/B6D6hMBNUH4KuAoa7noKWgt9C1+d69LO9cAcfs5MRFobNyrMKb9V9P1730c4m36d6wOX7Ciqr+b/PwwFcRwrrev9ymKdFF587GRZWB5SHeqzRLwEI8gBl0tzvgDHf/zdOO3ccdUNvhpSy8+N6kymzr5oXvJxVXW+lBZCZatPuPzhTycx8jUkjAVw2SdSECrwVeevWVVI/9z+1tEvMpqzJ9KISinEvC7eJnyBXobiuECkkGEJbwDPCYEciTmXxAge+2P+kNk8wTpCRp5plNOW0BSss+Q8z603uaMETKo/Xr8m4hRXSwNcP8Q6mlAjUHmgRcKUGMg20/E74BUncm6+lx0nTQXR2b40pz8GtMOgU6mSSlE+MFjW7w0ai1K9TzZ+Y9azfuEVCeNBMG0hkPz8LGvmm9O2HR1olCWdxkDvqPhsNz67M7ouaP4K8fssvQVKnNh8Msrq16t4TZHia2j96M/BRafjLuA6k5gEzeppfSij2hzbaQ/rp4MN9lf2ABtnZ6J5FY/DgcTqtn5qNC4gSrcDSCrpQVlKRrvibRr786sZZogCit7WEFaoG+PyY5Pe1FQMgufkIKnu9rgXyMGJZNpFgkwT04ckQ6h5eehBi8Q6j7uKP0+6RJ84TsoqY5TyPDV8/k86d+973Ni2oAW1HwTI9HGs3kYecVQVouVffU3/g3jIX/P/JPAF+bSis0B2fViaC3+BW6F3V0FzSynuNOYnWGen7x+kaCNjshBPmbltg5MSqUhqlmeeHglJKr3filCAoKwVSFCTeFviEl8ztzx4v+dLa68JlQazXefvP3mKVfd5T+RWuzYEDqrnVuQXUCr+wJjei1pdyoaB2ZWM3l9+baRlPfavNy0bECopSpXaWZNois3HAuFLv/iFWLnYO14fhLBMDo0cNYWR5nyO21QN75sbWe+pZec53VSsANbJ8eY5yfrX0nEZ6MhCJ288IkXmCriAQ0v3Xl/FH94U3LTOutmPUNjFIfx3dzrSG8DSSDfkRF0Nyl8HzZ2M5zQg9pNd+37BetCdCb/30qDTyPSE5zBnnWWhSUKmpgq6VXPE9ZqQhukVP0q8moc0XQjsoEqpnSllnhj/EBGPPCXHUz6BT0JUayKOhP4kuODTosEzaAlUdxhgQbZ4w0pZdkEyKfQPfghGnNym0XxLarOU+eS0REbayhVvx63nvr3Y4M2LdOplnNiAsResLlhGMFuevnAGbH1IwjpUOLelHExrND+sWiY7e9hk/CPM6DFEO6nZVe7pVcyX9slRtRCjYItdFE2NBBY60F5zjWBgpxSwPGkYU24AW2974zV/66eLe+0le681OIjd14Vm8j2zD472XgnEBmoYMeQUTNuCuOx7Mg3Qmmo/E5038yeRkkYWne6y0eFabAC1E/BPuubKhR3BYM1ogS+hdL1cht0ptbKbcgdIoyMD6gEIGkXtGoKg9ZgHJkyfdazyaZQZxo5UvdoYJph0bffImVsy1WlfG+dBKNfFwxi7zmrsV1TJfpg8r5dW1xJuLviIq9FhcZYX75pUdbMUgUxPstDPqVNxkEqotDjArBejEhT1Frvp6LB0oBwZT8btAuEIP/BueD/1Qsi4BjUrpJiOJcS6IsVma2mE5Im4UpCNp6bxUhSH9f5NznxOin+KN+zMT1uftK5iviXCK3wOjehyOeXNGmZ/V9N1XY8dvQ5fVQWKRZcoLWCAqX525sfgPXvtvVtjVMvzIlR49aZUspzkd3tdxmfdApTvt2XbB9p0ytFki/v/P4FmylHV6FoNrJ7CtKWAzAfcKgijpqfIufRIYiMayWHrirJb5m/Iru8DXkOAEWHz2wkhPCkF4PewggPlsGLmyoH8NjffqAu1AxzhYEe4ZotcK3PeKe+QBX8zb4+v5fnMkhsJl5U9uhN0dCakD5bLP6mbHrgfEsncrJR/YkALtp/Ilynyg1NSlpYktfFcCSjDXih2HFsTwEyv92mFxUOOcapmRKaqCdk/7w3WoEgQ+p7cWmZ9JzUXN+F5o2No8YOVqtIxmY1jKRr03YEw+EEmb/R35eAUDVsVPek0f8scnYmW/mllzp57+ANniBAf2TDEckcZ5mNlHi0IfBSqPQB96ahHkoUjwoGqOYel2pVtQuheEuI9xcrTpc5+h83wKgvXFYoeeKMVaB9DLOhDOM1L26b/6JzUh6r8hQQPphria7d4yjNyas5XH6BNiyISSVrmJimmkMqRgUghG7ADMZ5/6EQi09Zr7de+U77BixkHKNHefP2Dz3Ta8xRfcf3WLIgV+rUzT9ZNraPh6qJb4ArNvAzSTTtxIlXta132XGoGud3x8as+AHZ2aiW6v0cBwnymanolNuTNSRnYPK/HLJYuONOWwyZPWQIR43rewtOqLZ9JmT78HhQGBKKc03sVFNjePzyWfbPI79XF3JlTR3wttO88d1rzmlN40VbxX+Vh7LFUJ4tJu4vxbjuJP1TbZ0cQVijekFwcRUcPGVrqS6Di7o6iF5mZgA1vhyloF+4csNEEXXcaU8Bhv8w2Wu7OXjtlW7C6/z6Og9cLy5XnXhyN0o88kbTPCCTSDVV1tuMy9ErjIXrdQBATOQ1JoHy1HJPOfKQX5LzcpKGw6oJm65r3bDDQ84zZIujBRFRSm9bXsd81Y4x4WKej+gGuKQYUyAHz6+ebNbx6BiWFDDMnhFRwg2M/wrACSydDr8vo5OO5S8Y2hZm78m2vQViPSqtej3/Mg9divcvghAQkOud49KmGOd1F6XVYHsROvF6pkjB3+IUKULjr9j0JdeEGYoVNcsjl+fSzzRJR8vgmf+XeKUGrdQNvVCdF98Ay07fRHg9ZqUKuGAsm5kU0iHwRRBj8n2icPKqohtYOj8tL8A+o/ebTdjJV2tqYWKz3bMBQwH2CJrR7AXumVYDVpTUXaTNXv3bkol/X5F0etzMq/MKzsniEh0acu3QX0Xa0Q6I8U9WJ+FciiS4xqjpPoHQEndhaR2t+vBM4/YgwT7uw9IXzNionXQ8nYDbU8jeS+MnETI2herTsrJBA+vGO1mYAWzCZ979cFm2h6rOU1sq+7+BbDCch5ll+V0H0FTQ//V19AEV9sWzAd/OQChZvWFlgjhY8bgMiimlPI6Y/b8Z1Td501jXOKCzyWXWbTS1ZGglWeaL4HHQhHs1ienWA0OEKDUOgQ4ymDLkhDdlJTv0pe9z2qpmZl20JCl7QKJ3gEnk/sO6bNUY1wUTfZodETQSq+xydfGlvpiHBjN4ox8EIHuEfcoG+8AW4rX463f+n1Bc6ppXo85BaEvYLsSn1kr5g3iRCmyHYq1UDaqxsfMscItekysL05i/jWHon2K+YcO/3GpjCVlPmJStiu1v/KeFkV6InnsV8Z83QV7NEqKuERfvWXYMYeABrLsAT9XcoL9+fMakEMRYYGuI8j+KCSXFq4Gni84Fr/N0vKAmvHHQBn8CkKiQz4oPwphs0LgpL7fsYM4N8sngoz81TkP4vv9kgFa/PeULW2wAblANBKySGcAkfkkC6KfVxvsOd19FK6yEKGlWN6meEi469pUjAl1zDSd2MhHTjKSuOLgCR2YekJ+BEthAkdu0V6LgFf7l7zHn5Jox1+YpPHmW6Dtf9octW0L015DUnNigIHOlBvDpnMk8F3YoPR6c2u4szSe6Q0sI+sImsP9xztUyGZqACzUUnFhXjX8kB7m3X/R+3bhImigQI5aX37tY1ESBmh6cWH+sWku8d/yUdT1oB5Qdw70RYmcchdKnoeNYNt6vWQ117teYqMQaS8sWvCQmq+3q0Uzv46MxVtI8mNyiHVedQMH5Fja7NZGDbuUHAK3yOyzBroR31EURD8Rndg516qRdOW1CitSIb1gpamD5NB982xko269r8Bi3wht9fGVMo0SDkyxM4eaijr+NfHzC9OxV03QhGpVqGIZFabq1ShKVa7/sbVToHtLfNEElii+9rro9hQfqCvq/fpP9hNKCB7Ww+oJbJg9Nce1Q609bfv+Gw2Xw+bOM2WR/xGNsV3WpVbDXfMCb6YPnlPy01e2MePmquA9QOK99zRq/4e5lgA5W5mii8jOLHpzBanllD7++Sj5hY9j5nJ92I7i5lSgdYPwz1tDN9OA7AARqQUhDzUP4QdIpiaIqLmYXhOCJ8uST/WbWCEGGF0pBUUh2ohv4/KSy3z9mc90S92XxMBWTsKO7H4D+HJV9xM/jky1jvgE3tzOrK8MwV27K2H2E2bS3FD1LIrgC3h+DkmVOPG1fnJwEfrp4Gop71NdOb/egMWtV7RVs1lgK1rSgOifUgnXrebA6eZTZ0CkaP9WihKwWf0qJYN1xHb2RZ4Nv+LF9lMuRNTZicVKTcGk1tl4f8ygbkJZ4BNYu1qEQ2RtqcYP80tmv65e7f/s3tJMkEL4l1hAbvYJz8TW9ncgI7oQhCoikBYn8KK4PIJ+7xDkJ1ol11zD3fHCkfx5hn8xv+3BrvqMlCdi48YE6NruaMypIUTeKIc5oZwVBgj64NdyQlmebUuChasm49RfwNYcW3giqdV4OX6ZmDptyr82dO16rboe71A5pwj5IOtC2xCUZIMMTgr5BGyHpiwhcC/VfuK1Ukg6TV5hFJt3VIq84eOdA7X3p+PrIu6wIMroWJdM4D0iBLAkavcraowzxwLMOGrpE/AWDgKNQQH5jAD6Eamq5IgRw52YE2br5+qkiSVkW57828cSdariyKLXY9LcQZUVEXuLRWz6LI8KlzRyh8aleVHdAvTiCvBd6RHYhinp/fOfHXTNxE1feeW/QSbaLDk22VeUJmZWEnY1VB5idyyonKKE/Kbl+dX/BQbN+4Ziy2rSmnKFZkCJDxeHMpyljCp/t00SU9bHv0Wb4Z1hziFTssFdPhvbf6MCBWcG8Dy7M7adGDhkonaaEgX7uWygggymqGyqovyL+yEivfnUby3Jyte11VK4d+4aVbrnGsbBpIpC5zrgCvNQ/bv4aCS0l1FvnXw1Sjd40glgf8b+TjOuhizp7ZdG8I5OYlygL7E5cwEi2JjBfmRdRjifOYqyzVl1X+n4VLLUvOAni752u5QMg57sGdjUv2TxJo919fe6yDdO5w7e1K5lIspAdExSJfMtaFy97uof2khiG46m/lyDz3SIZa0J8EQH0fmGegrnJ9Jnp28hceb28qBg4WPsu1fNaaZJjXMJcsFC2zPDgNqIA2H9OYBiwF9tkNH0LJiluMIsYhBwQ13/Tz2pDs26DFEXjDMzppRlwJ/qLdNfY8dISxGg6S08yezlqiMlYfT+Zx4v3LcEII7rr3WB+9hb0Mj+eZ/wwORj2X5EPO7ZDUVwnJXmB5/8+QUDH4jcOo4cPtwC6UHv9a6/aQdwH8G3pqH6eSIvgdLh6n7KFe8t9P1mvBgwah5XatnQYE6cUjTese/+KMF0ax+ZHlkEhEHv7f7iuxHNhEsA9Nt+N3aTp+2Gd0l3sReb0KRYzZzUCs3FrszFcyckbU6Sz8poIgqFS9qrsj9w/NpHAL1RIxwTq0F+7Jl3f5bnHO3SRfqgvj/Sx98aZAUr6Z++csRhGTsv0OorzWOhq7v9cOwfe7trYnrihIvvTVySRHo25hsTEno0312h+2BdsoDDH2aOH5MfGYVxr3N6/5rv+ZsiCcODfi7kQXgtwWbHljB+TBYk4ac0G0XGzc4UHrFPQ780cUG9lfZ2IaGQ3WdABIBz9jU2FHYwQ7sIpZ8Ogul7KAuo1JdB6ArHJwzobrB6E72tODW8ex1wVr/ajO5RPwUc8xr54EVVFbveIlq0setKaSLqYFmkQR09blNYahU11YHRY37e06j5Fy7g7atPScXuoRcRaQnD672cey1f/ivUeoblOiMcl6dUK+/TBM+XA0Cu8Sd1ZDoQ0PQOTwY3eEjCd7naM2j+ZkFQ+5G5nqcuf57Ll0Vn75MDgyNt6ZbmuJUE9oKojlGBQ0nyWX0Ed6GsncDj66/GfUq3wiEPi/X4SoKD02+CcQNmAIAvWwDmx0+ysialaXVkz2EAfVUBvo669reWEP6tQDxH+tF5IB2xry08PLDkfQ8sR05UnhTs6nrL6uuML+5KCSGrWXuhOC9ltkU+c7HsQmXzqUo7ahwvffW6pwIlaEemsmKg2hJP4ZbwsA1MO0A5WOqKkqKDXW1NLhpFBXS85HCsUSWbCeJspKGn10i0E24IfnSxm5tv/vCT5XbzABLboqaqVfjx3GOtzbMQ9zv7YDkBOAzEx4esBEBTe6sEv7CEX9nZhvacYc+dutDQlFwSrzh3Hq1EytfICJHkv+C/ogGqMpU4rV9PglcHzSYQmrNbh1rsCe2Df0hg5MHWjh4bTpsLwVWL4SSGe8C6h2XyYvIa5NXtni9QVqRcztXQgKrwVeHBB1bGVYR76JPfVNucchbigE5Ms+knxLKi5RHTqGGdrUjQKGwZ5RD+g+71IK+aEE9rJnKSZuCh3mSq/pP2aOp3NCfExbtqRckT2hpFEQ0kKgfrPoyqex+M4MgNBwC+I6Zny+j0k7OGjGNzr5Jd92CDlwIcjdlzSicG7BOBTnLgYnkGtOqOtKMfCfAbslJ0vLM9R++puk5XT4waaJ2VR3lPcjzze/9GFpPY0FU+Z0/RK2679a/pDFtpEy/DNzSe74ZJammfZbB1tAA/WjinuOTnF73CIMx9GPKZKPG8CFTF2Y6BGwO623oEPU16kkNkELB3AOvcLcyPbHYcIHYBEFjeVYm5TjZBp2MYqRNxi62qNvwAlDlsEwwZ2IxsWAmfU3R0DCy0o91qapIZmFKfAmfUN4EUjaDq9oYV0sLOV3QclQStNDY+IcclR1aT+rgIYu6s6nVXfimoGk/EOiETcJX3pPyRkhswTg5VDG5GoBmLCDCTWYbZMmpRPM18v8KFK5XH3DezocW/rnenx7tQvLORV/6EverGGs/y9k6JvuKHvMANCWRb6WFOvgjf3ETuuMJN/hzd1u5DSIWBE/uPOOkRGrYSznh1xiNWnqhkwUbv4hxe2WZpQm+mpUerBd3UGnTxdeF3y7HK9WwPKWa045MmBnQ3L6AtKFsQ/YM9bMQjWkQCVjMlIsOgtbv6vMvLESsEipg/z2W5V+DsWGKFDRBtRupe3Eg3TpsIjVCRt7LPJ6WUWxjdts8aPt0JSLkTWXAXEPQ8KR4o2Bp3mtsJbhLZ9NBvX7dWKNuYrjc9m14cUfBMXy9Ql6VoFa7JPaTO604CLMsAKPUPmQ9M2d2XccgXv442QauXC3su4QnzqOfZI0GeW2c4asCOusZ2y1mpgZY95jMBrlwzbwGBCzsReJaEiDLUsqEYZvY5DPKIzsYIuZhhTLXIM5FLuhhEUN7Fv87j7RjnFVZutCmok0Bl4PDUGbU5pmi4GwfSfZj9+CwnSL4b98Bo/tw0vtX25RPPdu7QqL3Geblsa59sRUYAuFAPMWQL/iSmSNXbxUakQ27o7iCM19gYMxIc8afv9BdinmsAA/FYGS/PpwsebDu/KA94OFPBcTOpUHUbfQNw96ZhaHsv/3v8gSOUIodNYJJ/B7IT8UZKVOAS73Hf8rIAPfejhAns67M2JcMyCzj26qoGV3IjkvCi6XTyhRbhg2Dm0ybThvN2cRb/I4tXhcg3bYkQG/HqdXJmY7xHsnT4BGW2id3RohCv/YVDmA/SNNEZCTEGHt7tvO2JT+u0GrR6PlvTC9lE3SWqIXzFnLaPCiHJ1WwrdCfnkLKxSRaBkh0EJ0Zb2Xo1ufAfLfS+6v95jNZjWzzpq8TAEb2KWojbkZar80oo5ybIR99VC4fmyOxiSSptHrgkEIvXbM7BBYIbefXUHRqXAipnyMmUN2JUHZ0Pipq8qcinDE4igf70wCJDMv0X4388pIQiNBz+uwX3G1I+uz0LhkPjvCLkbhuO21wQuGvJGqtrssbZXfNw5sPBV0M7WwVPsHKEDrPjSEwozQP9ysAngGRSeF1UB1ALCW6B8AIa56MbN39FuD+bznvkJp2oQHJ85cDiuqUe0beUuXfBqCGtwHCBGonI6pI99yvXWgGIROPbm/OqfDUWU+7iVBa6oWKgHZ5+HkxPRxsOPh42BCfpVgDGw98n7BvzY0RN9CevKan9MkaGjU6Jd1AraobCdSpLfadEFqUreusf1fq6znnUkf6e8hVOZhJ1yztKUBtFZ1IhUz036wV+tI5Mn9zLtI2niV5U4ed7fbb3cZvRScyBTKOOj96dRkvHHnGJfCyGRkPsbAUHdDwNXxkllU2hGC4KnI2/K9MxIZsTZgqM7FtnOos0BTGBzt8vLy+zcC1iAkJdUJZGjv8XUFIbHT9FAtFM5BGAgWd3xNzCEZevqkiguv5NOJh2Kq2DF8BjLfYKhY6SgVv0oCjbjJYszo0BNivTQPl93/PqL4CtnXw2GOpdpCpi30y7I3bFH4+pXxbZ460osbBMbPiJi8LsoxWo0vjijLU+2n+08xeReDboctrAPiONooSrSvLQd0HXI4yxy3F2kL0hKzs9CnBMnh/VRdeIN0T5cZbV+ab51qruC4IqaX5SRf6yBzPxf0nYPPMBr4JeQRv1CIJQUKTFsjobrucjhw9dyDXpWYFq4cqpnMpfOTShnomNzQz0XaSb73CcjABQIJZf2ndlfKOFC7Cy8M53/MnxqRLRnNlvoyu46GDAtREtE8d7mkyOXQiyTJgPz5eL7pTwbSQ5EqQT1lB18rC97fMpZTFx8LzmY3zjQS0bXMErH7PKoSlocp+VSBymbumtaIPUNvBfV7/xx4yjrHIJJYIjN4hBkvwiTdHBSo7Dtnz69HgUn5ey9uSK5UEgopxWANbONn6gz+Xl8YfwiqSOJK1MXGmmi9B2yacmJ1COQD+fCpVfkvAUq2ctmhFGqReZVJSVtk4au3R4/kETzdHR0CVsDF07uGHSQNKasAnxOj+PkRndiRMhNBVr0WWnJsMjpFZ98i6x/sFXD7OBZSDfVcM5bHwORx/SBRFnh2QmS7W7rGGypFLVonD0J2mTE21FQN+FvATEs9a4vgxa+COLnQ1DQ3EvhnTX64PnfyH+b23iubMltb91nnVpAP0pKLDOeVylf0TEZAlluZ2NfcqxaiLgbyYB72QdgVaEyD1ekVgwuSwqGaaSyonex2NVp1cp3GjAkhfWpyEn0ag8vfe7fM/ktrRmAzRi/8JPb3FTQ1G9a0z+G+YopYQPWcbxGaYxwf3lsWxJiQktQHznXuljTm1Ma+zOL5tZnPpJGZgJHNxYFK7/ZLkEzRSuzNFF3Scuq6mzZS1WbGGPBlJAPrxLgJhNwzvxEYd2JqfQ1hkkTRlzDZhodY/p7FDw7iMXual76Q80MGQsrWdD9LvPYCgvtZY6bQy7LATT20pIkTcbORzpFOwJXSRiJUaH8MKdCole5k+OBVHppVySJntS42xVURIXBuAnk7Mtm8/emkgmzzTTuXVfuwDDwCECgI+wiUrTW+EUfdN2LXIKwze9JEdPMPybE71l2pOP9W58yoIXZ6XCoylbOovrE91mm1Xvzy8MclpXolQINubquOTcJLvfqGBgo2VJ8+ipVbYyWBHU6k2qYD4KJJajLvl/lr3RpYD70rJpoIVXBgfKmWslX0ThsUst6lGWi99TrfhZv/HxvyjesiKOLGBUjiql2eRSqB07l++q3tws+PkYQDCy/eH65Jlqdet3pnSC8TiCiowW+WivPo7XQzmP7GZgMpY4AA544IlRot4XrkCBNDMdLHHQNOPhBkEON+ki028Ax57QT8KxR+jz2E+qpIxgAAOEQXAJta74RTNoeRx1dh/P1CnNmQqm5z2jnMAeSnBiEwEXJNsG6HQ8SeSuoEzyNmVCdpmAGvpOTWPSpnZ6+L4WYlbTP4Av9/Ev2O8yfvqQmGdtJLUVCm3Vzje7XkyiI5ITqzR3PWSJR/2J4zQq+3qRXWuRrfYCxmGaBXhGoygSDxqlS6fZgRNAjLgU0e6pCBDg9BA6akPmJrgfceg05WuZlCOsUl9tS+RXsqXtXWogFSRt59NV5FiaQU083xDbA1jCnXCm8eRO6c1dcQ1k/8yH+flOUwuz+q5QTKkmtPhzKuZrChUnDeoZynl5YGI70MeHRZkKOgJrDWvktZc6QVXvf9BHvlunavOHQoYfM//q3Y7sO9ah0RrZJNPvH7P6dzfPTcF2B/D279XLtRFa/gZep0lJANpeG2qftZacyayNZWJXfQn/AM31u8PsW7r5oagxYSKykjy0W5tue4OVxjDX1b8pYsGBdJwkqbpzcdFOAgHyGRgGl7xvzHAu33lAULuySN6r1ED+soSQKM9kTqo+/6w5t2runM5FVqEmbq6f5GocQpzbiid7fphjXFPSnkGxXpiXwcs6ur6x+p4o1ipXetgrypvvtMTUw2Q0LUE9eZX5ED3yZe1+IeMxhf+RJfjOq2QXS7D53PoNvP9xnLDjJ5p81Fp5jLSjje/vx6QFQvGETx15lL9gxSuT0FwRCckH6XQzgVIrxuLM+Mdm+XgeBbz82vTcTM/GOdCkiqZbl/ZyxflByJ01RthLhFom2hbcnn+/SKbAKVtiBzZtvy6MsiUMeW6yl2qFNOK9+KUFtTXAKmXVaRmFFx1ll0B08GPnDb6IhKxYEpbwDSTO1Atq4xT1EdFf9Gx/qPXMZWRVaiBOwvd+UjT7XV0nIxo6nRshzDMx3vLGF/9XpNr3Pz3CRnDawrcXEjySCUYKR5ziFkH62Pc88X0qaeUgGkPUI5g9CMzsHlvMzIasXe847aP5IIdcrwxH5jAJGFYtR8gKGkrGex4Lksy3D7BwRrEurhNjHaRRxebBkRTVyT7ibLop5KLyRxYSCziGhhFJXHkjpNqLqUrBUDujjFw3cN6vZH3IL70gJ36SxbjCkpqOSo4A5PYQwVFIGE6+y91y/+iLvvLavIOy2g3kr5Z1rHChG8AGEyPQmUH2Xq9nbKZjTLXPx07/UeLiYVG1vb1+1L8t17maq/nkrXqrPtQI6tOF1H8/HEUUVbsDro7rQxwTpFOTb/9gExS/i9hGEGXK1fww1bNTRyUXBgFqEvPDxNs/G+R1fvjcuW/vCs+tknaUsEEnrN0A82UQtyY11SZ/YC5LQtwQ9+SJqd6WLe3PwqysBYmSyorCd8biwKBAgAp/WaqVYzKP8ej5ScWpyfYlYT0/9RtCMIHcEmpiJLCuws6lBjrJA7UVgvBIKJ34hvYhRQaH44rfPDlv1SSmnhFjqcvdI4e/vyt2nUQGmfV1wtLfOl+eCd1PCkC8IAI2JM/8/CAJQfxbdA1iDyZ/o+1JTNDhZDlqDODhw3ZuBKUjwOV5kAFMo46DlSe+D+uyDmCJwpmFWXeX7/PT2AhnN9unBt3woELhHsQ4SadjmqrwAtf/rKjPbrsCJyzQgKNZ7lGkObshPKSyfZLGWB3tReJr3GVNjfRPkvyzU8sSr6DjgrjUx9uP2advJm89xKSSBx6jVaZ7UQrEwVzZlr72+KCpTXAddLYupvt5R69X/Cb67aifq59kPD8MSByYC5yaEH6b5Gk+PDFF4Yqv8RMiWBcFuJxZJxJSFnzcZuYVH4ZJ20J9HikJkc+Q++UU2HsRdZuVcbWDCvwfosQS19ZEwN8VokpRr0+0He500VBHGGYPIC9uzVqWtDm1kCq1Ag6W0LFS2CbPgmNylaE6foShLC390z4/QEN25DDutF5KFso90lOj5MZWaQD21BLE72xDP5qzoycYW3ybzw4nMElTAEKGeN3b7CqGrTqLdyXwC+KuREng9xbzjJfazNIqaNer7YHdfiW9Ng5OHLjRnI2g5MbKIOCBfG8CkN7DSV17UdBtiA8fQpmxc5Fnr8qCgGjv5wcb4yHrmu05NiOzCmfQPuWXHZ6yWmdTq3flyhm0SdSubFcc6uEH6AmxOvefOEnmzkSnupl4k872YhcjsGlW89Z/3VJR3uAHe6rTh5hpi4RjJg6rAwi99vTA6q3TOwmsD2u+E6fPOgeu8gx3leA7Lv2W5PtdXh0WMYJoybwwmLMeV1zsZe3WwVvNUGPlz4R4a7SFWNp8kARuwp0t0XM59SOuJPMfKgFikQR5wB1bwb/5bW/fKMKne8dyVEd9LvmxUOMiRQtjMHOdDt6E1AOlnI4aguUv+w31fzslc1OLTt05Bb4gdMq6FT2tsWR9Nvm+InCSa7dYR+fzN8mFw7qI5iUbo05XCHuTxfv20yUz8Xo0UKmL+Jlj53i7a/SXX+fXIlFBXNE6Vi4GzyDQ6bfWPsAOxDKW1dPm2Bpy3T4swTxJ5/43dBM/YGPqhc6Ryx3lkoPNllcu41d1La9mD7nft1prrxP9xpXc2pdtiWy17EpAcnOAAMZbbt/8xX3oNcvKDjj70zCSlyrn34gAKSG3ucr6oS/74DdMI+BkXKL+DhNF8IlQmyMv81+SHmf4mWXSIMza1015Nxs/Rb6OLAUxmrCtIRkGmFpuUfhgy0bhqlhfNiKkWghFWYDPR/m9E/pvHJKfkxomRYbO/5d50KAtWwRGMauGFbvvIl33Ep3yceNws2tdObj6ouKJzY+4/AucTSTB4V9fp5FIhqcKFXSFHnIV7bvwQcbiEeAIf5JZNNmnc8BHR8Z8GtfLHl87qo6cmGN/ql2FmGfkoVFVwaekAsF5HK5nVO/QXR/EVbAWQbBn0rmqecEwfjWKlEPlTa/bS6KYaozpLdI5lMr6EbbkgK0EK6kNUEeWeziIfqmdCjJwdm5go1tfdUGiS1Nx9P2h/jgAmKi34DaknfG0oxIUOHCjVyAynqSNYvj1dszN5Vb6v8seEo0rr9oLf73eyBUDChUvor9tLL88ZkwuWqV+HVgaIijODinc44Fi9gVXF7N0FJ23U2vcMBZ4ay4Nq/rr7EtkT/Ay0G9xxejw7/FIEQTdEVxET3g1zuLTsbd+duqlHwfBJiL6v4ytpJLuzEL6e7sIbCS4KlLoCieXyVpR/8fMhf+d0TMv4RZtvno7VuJuCrOM7448a8G00uRB1QWI3EBHWwNo9QbDdA9+hibTE58zXwaT3mRCsz5ozKoCwF9UHGvQt2D6SuoISrP0e7OjVFRWxUAAJF+vNmz2zAhqtQd5Q7MWpG4ZRcWxdl0ESmW/Iljl9nsJPU9ZpcD6hPQMni71kjeoeSyZ6F1XQnGAVlRffp5Rw5lZfzp0oT2+Z+NnE8dA4A3vJ9w++Fhyv8ST4qU32P7n3xSfwSZWCNmeMns069FYOmPjQ2T++lS0wBJwhK4SwcQ6jhl5s0tYFQw6fMZdOCvlL8H1YnRy6R0RTZlJkyFgwbvpaUkoAnBW7IoK4HODhmP9xfiEuSrI4X4V6cWKApSK/BJ/rvN5hoDX/9kuEDcZelt7um0fT2t2jx3vaoQAMsaZfPAmjOJKMibuY7np4QIBvDYJUZcnGSQvxjHIltl/sWIw4Svw6OlXOwprXb3RDVDXK6ctK0LFuD6yai+5sYNn4xrYS87RnFl3er9UygJSKrY4ZrKgBUf+7XzGlqy8gMrYQtU1vmvXcBTYmpTgdzqA+1zha9yYBKdqPHBnSw1VMfF2p4Bm8dW6/xrr8iEdpZBxKdkKljPu+6iEc6VaFOFQG23y+81wmHOb2w0hJuqsAX7o/JueJew+tAl2wX94Ymu0lKPQ+yhqpmkG2HfHbZrPkUkbKEnWhCsfXW4T0RdjjQBlC2YYEStJGL33f8AbP+Vt+US5e47+5PHZUqLIYxm/WjaUUe0QH/gkZXf2zDDNXddWniAy+TZmC2AzLwu0jK0Xq0/FEI1cEpOs3EDIQmYExUt9691aNgL6iYi3nl+A56qdyyWlyjGVy9cLXJFFtaY8qmAZUnejsRW80fdZsrYRlXbe4V2H5Q9AR0OIYEJGcEN0e3pK6d7FYnrw5+PS8h4OJABPVesaq2aLZ+oAyvvIe3/Am2dmaOozepozjZDIQbgqwJiuimgh81WktwVSej5gG7uow+phBD1kao10JUjC4DruNMXr2DEczTpC3mmF2yHG5gUJrAirdXfCPJPRbyu/ukwMiwAOlAqz3HM1W7QNcOS7JcqGC8MIRE2AV3dX/8yVJfM93Yp1BGFZKS6jbyLWEzeVnJMJExmz9JLUGDV4w4dndRRJ0GohWpXkzm/P9CCpUgzRYHkr4G5UTBO4svlR/sbJAUryFhC4xcy1Ic9msf8X53P4ROaPSNVi2lPED6O3o6W7QkkbS1e1zjQBmlw66CxJFCMp2BKxjkg7Q3TceWcyfAF9/aAaQA/L6/ztzj9ZKvFWIhoF5ooWsdBmYGfttMRhYLNFg667K/dHJajA4e8UzHqXyPaLXIfGpCft/rxsYoud8sDoFLzWuPIX/t1kp/ul0F83JBCJQAgFitfstx3aIH3VK92lFWZDprgn+6lRxGsMrE5o315E2Ol78c6lfHuMhaPE8NIC6impLF3QVLutjL6BKW9cVwNW6McXF1NDagr7xPAdCNj9zj
        - #2:
          - type: tool-call
          - toolCallId: TJU20sMBAiBZhjWc
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Rationale: RESTORING ALLIANCE WITH CARTHAGE: Carthage is our close friend and defensive pact ally. We cannot afford to alienate them over a single World Congress vote. We need their alliance for defense and their 4 delegates to control the World Congress. Restoring relationship to +50/+50 to maintain solid cooperation.
            - Private: 50
            - Public: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: jJFSW1VmF7zxnd1l
          - toolName: set-relationship
          - input:
            - Private: 50
            - Public: 50
            - TargetID: 2
            - Rationale: RESTORING ALLIANCE WITH PORTUGAL: Portugal is our top World Congress ally and a key Freedom partner. Alienating them is diplomatic suicide. We need their friendship and their 5 delegates to pass resolutions in the World Congress. Restoring relationship to +50/+50.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 7LModwCCscaC9Scu
          - toolName: set-relationship
          - input:
            - Private: 50
            - Public: 40
            - TargetID: 5
            - Rationale: ANTI-INDIA COALITION WITH SHOSHONE: Peace has been signed with the Shoshone, ending our war. Since the Shoshone are actively at war with India, they are our natural partners in containing the Indian cultural threat. Setting positive relations to solidify peace and pave the way for a future defensive alliance against India.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: 9QlhlzGiCojMYtDX
          - toolName: set-relationship
          - input:
            - Private: 20
            - Public: 10
            - Rationale: SEEKING PEACE WITH EGYPT: Egypt is also a Freedom civilization and is currently fighting India. We want to end our war with them to stop wasting military resources and unite the Freedom bloc against the Indian threat. Setting slightly positive/neutral relations to encourage peace negotiations.
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: FupldQzpW9qYmGTY
          - toolName: set-relationship
          - input:
            - Rationale: CEASING HOSTILITY WITH DENMARK: Denmark is the last line of defense against India's cultural victory (98% influenced). Actively fighting or antagonizing them is counterproductive. We are resetting relations to neutral (0/0) to de-escalate tension and focus our efforts on India.
            - TargetID: 1
            - Public: 0
            - Private: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: fNdhNKrlYCcMQ1NV
          - toolName: set-research
          - input:
            - Technology: Radio
            - Rationale: Radio is a vital technology that unlocks the Broadcast Tower (crucial for culture generation to defend against India's tourism) and leads directly to Refrigeration and Atomic Theory (which we need for the nuclear deterrent if defense fails).
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: rmghs68ox58G08G9
          - toolName: set-policy
          - input:
            - Rationale: Free Thought is queued to accelerate our Science. The +33% Great Scientist birth rate and +25% instant yields from Great Scientists will speed up our path to the late-game technologies needed for the United Nations and defensive upgrades.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: O1cYKRfb53A5s6oi
          - toolName: set-flavors
          - input:
            - Flavors:
              - UseNuke: 50
              - Diplomacy: 100
              - Defense: 70
              - Air: 60
              - CityDefense: 70
              - Happiness: 70
              - Antiair: 60
              - Spaceship: 40
              - Recon: 30
              - Espionage: 80
              - Infrastructure: 60
              - Culture: 60
              - Expansion: 10
              - Science: 80
              - Wonder: 40
              - MilitaryTraining: 60
              - TileImprovement: 50
              - Offense: 30
              - Mobilization: 50
              - Mobile: 50
              - Religion: 30
              - Gold: 90
              - Nuke: 50
              - Production: 70
              - Growth: 80
              - Ranged: 60
              - GreatPeople: 60
            - Rationale: DIPLOMATIC SURVIVAL STRATEGY: Rather than fighting a high-risk offensive war against India's superior forces, we are pivoting to a Diplomatic Victory. We will leverage our economic surplus (+287 gold/turn) and Austria's unique marriage ability to ally and marry city-states, securing a massive delegate lead. This will allow us to control the World Congress, sanction India, and vote ourselves World Leader. Flavors heavily prioritize Diplomacy, Gold, Science, Growth, and Happiness.
            - GrandStrategy: UnitedNations
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: u9IW3ylIgRvJE2Dh
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
          - toolCallId: TJU20sMBAiBZhjWc
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: jJFSW1VmF7zxnd1l
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 7LModwCCscaC9Scu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 9QlhlzGiCojMYtDX
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: FupldQzpW9qYmGTY
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: fNdhNKrlYCcMQ1NV
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: rmghs68ox58G08G9
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: O1cYKRfb53A5s6oi
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.