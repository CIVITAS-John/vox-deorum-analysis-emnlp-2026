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
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 80
  - replay_use_nuke: 80
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
      - toolName: set-relationship
      - args:
        - Rationale: REPAIRING CARTHAGE ALLIANCE: Punishing Carthage for the International Games vote was a strategic error. In this existential crisis against India, we absolutely need Carthage's Defensive Pact and their 4 World Congress delegates to survive. Restoring positive relations to secure our alliance and coordinate against India.
        - Private: 40
        - TargetID: 4
        - Public: 40
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 40
        - TargetID: 2
        - Private: 40
        - Rationale: REPAIRING PORTUGAL ALLIANCE: Portugal is a key Freedom ally with 5 World Congress delegates. We cannot afford to alienate them over past votes. Restoring positive relations to ensure they remain our close friend, maintain open borders, and vote with us to counter India.
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Public: 40
        - Rationale: SOLIDIFYING SHOSHONE PEACE AND COALITION: Peace was formally accepted this turn, ending our costly war. Since the Shoshone are already at war with India, we must build positive relations to coordinate our efforts and form a powerful anti-India coalition.
        - Private: 40
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: REMOVING HOSTILITY TO DENMARK: Denmark is the final shield preventing India's immediate cultural victory (98% influential, 1 turn away). We must stop treating them as an enemy to allow our AI to focus completely on the true threat: India.
        - Private: 0
        - TargetID: 1
        - Public: 0
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 0
        - Public: 0
        - Rationale: ENCOURAGING PEACE WITH EGYPT: Egypt is currently at war with India. We must ease diplomatic tensions with them to pave the way for peace, ending our two-front distraction and uniting the world against India.
        - Private: 0
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: MAINTAINING SCIENCE SPRINT: Free Thought accelerates Great Scientist generation by 33% and boosts their instant yields by 25%. This is critical to rapidly tech towards advanced military counters (Artillery, Landships, Flight) to challenge India's superior forces.
        - Policy: Free Thought
    - #6:
      - toolName: set-research
      - args:
        - Rationale: TARGETING ARTILLERY: Setting Replaceable Parts as our next tech to unlock Artillery (5 turns away). Artillery is a massive power spike that will allow us to defend our cities and dismantle Indian military units effectively.
        - Technology: Replaceable Parts
    - #7:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Diplomacy: 50
          - UseNuke: 80
          - Gold: 70
          - Offense: 70
          - Ranged: 90
          - Production: 90
          - Defense: 90
          - Science: 70
          - Mobilization: 100
          - Nuke: 80
      - rationale: SURVIVAL MOBILIZATION: With peace secured with the Shoshone, we focus entirely on stopping India. We maximize Defense (90) to secure our borders and Kuchundeka, keep Mobilization (100) and Ranged (90) at maximum to mass-produce Gatling/Field Guns, and raise Science (70) and Gold (70) to fast-track military technology and buy units.
  - tokens:
    - inputTokens: 25060
    - reasoningTokens: 7129
    - outputTokens: 653
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            My focus is on a thorough assessment of our present standing. I am meticulously reviewing our strategic objectives, victory conditions, and current progress, integrating the latest incoming reports to refine our path forward.
            
            **Securing Cultural Victory**
            
            I'm confirming India's progress; they're at 100% Policy Percentage and are influential on five out of the six needed civilizations. Denmark is on the cusp of influence, requiring just one more turn, which would finalize the victory conditions for India.
            
            **Preventing Immediate Defeat**
            
            I'm analyzing options to halt an imminent cultural victory by India, who is one turn away from influence over Denmark. Our immediate priority is to disrupt their progress before they secure the win by understanding the implications of declaring war on them.
            
            **Reassessing Strategy with Peace**
            
            The Shoshone peace is a significant development, freeing up resources. I'm now re-evaluating how to leverage this against India's cultural victory, particularly concerning Denmark, as direct intervention seems limited without their involvement.
            
            **Evaluating War Potential**
            
            My current thoughts are centered on the viability of military action. I'm scrutinizing our relative strengths against India and Denmark, weighing the impact of their military power and their political allegiances. The effectiveness of potential engagements is being rigorously assessed.
            
            **Shifting Military Posture**
            
            I'm reassessing our military approach, focusing on how our aggressive inclinations can be strategically applied. While my inclination is to be overtly hostile, I'm recognizing the critical need to improve our standing with Denmark, as they are the key to preventing India's cultural victory.
            
            **Leveraging Alliances and Diplomacy**
            
            I'm reassessing our options, realizing Denmark is key. If they were at war with India, India's tourism to Denmark would plummet. My immediate concern is that Denmark currently isn't at war with India and shows no interest in us, but Carthage and Portugal, surprisingly, hold very positive opinions and have existing pacts. This presents a new avenue.
            
            **Securing Key Alliances**
            
            I'm focusing on preserving diplomatic ties with Carthage and Portugal, as their defensive pacts are crucial if India attacks me. I need to maintain positive relations with them, as their World Congress votes are essential for enacting sanctions or countering India's influence.
            
            **Leveraging External Conflicts**
            
            I'm now focusing on how to benefit from existing conflicts against India. The Shoshone and Egypt are already engaged in war with them, which is a significant advantage. I'll be manipulating diplomatic relations with Portugal and Carthage to ensure they remain allies, even setting their relationships to neutral to leverage their inherent positive opinions of us.
            
            **Exploiting Current Wars**
            
            I'm realizing the Shoshone and Egypt are already at war with India, a crucial advantage. I need to leverage this by manipulating my diplomatic standing with Portugal and Carthage, ensuring they remain allies through defensive pacts and World Congress support, even if it means setting their relations to neutral to capitalize on their existing positive opinions.
            
            **Researching Crucial Technologies**
            
            I'm focusing on prioritizing technologies that will bolster our military strength. While Plastics is the current research, I need to pivot to technologies like Replaceable Parts to unlock Rifleman and Artillery more quickly, especially considering their immediate combat value.
            
            **Prioritizing Key Technologies**
            
            I'm reassessing my research path. While Plastics was the initial focus, the need for immediate combat power is paramount. I'm ensuring Replaceable Parts is queued next to unlock critical units like Riflemen and Artillery, recognizing the limitations on directly altering current research.
            
            **Prioritizing Immediate Defense**
            
            I'm focusing on the immediate need for military strength. Given the speed required, I'm sticking with researching Replaceable Parts to quickly unlock units like Artillery for defense.
            
            **Adjusting Research Focus**
            
            I'm re-evaluating my technology path. While my immediate goal is to secure units like Artillery through Replaceable Parts, I must account for the policy turn count. It seems Free Thought was selected last turn, meaning my policy changes won't take effect for another eight turns.
            
            **Evaluating Policy Options**
            
            I am reconsidering my current policy, Free Thought. While it boosts scientific progress, I must determine if it aligns with my immediate defensive needs. I'm weighing its long-term benefits against potential policy shifts that could offer more immediate military advantages.
            
            **Evaluating Policy Alignment**
            
            I am re-evaluating Free Thought. Given the urgent need for immediate military power and the extended policy turn count, I must assess if its science focus still serves our core objective of preventing India's cultural victory, or if a shift towards defense or other immediate advantages is more prudent.
            
            **Disrupting Global Trade**
            
            My focus is now on disrupting India's international trade. Declaring war will allow me to plunder their routes, significantly impacting their tourism generation globally. I'm specifically looking at their Delhi-Linz route as a key target.
            
            **Proposing Sanctions Against India**
            
            I'm examining the possibility of proposing sanctions against India in the World Congress. The next vote is nine turns away, which is a critical timeline to consider in relation to India's potential cultural victory. My current thoughts lean towards ensuring we have sufficient **Production**, **Science**, **Offense**, **Defense**, and **Mobilization** flavors to prepare for military action.
            
            **Revising Diplomatic Stance**
            
            I'm reassessing my recent diplomatic actions towards Carthage and Portugal. My previous negative adjustments seem to have been based on flawed information regarding their World Congress votes and current opinions of us. I need to correct this immediately to leverage their positive standing.
            
            **Securing Critical Votes**
            
            I realize I've been misjudging Carthage and Portugal. Their unwavering support in the World Congress and their defensive pacts are absolutely vital. I must preserve these alliances, as their combined votes are essential for repealing Hinduism, which is the linchpin of India's tourism and voting power.
            
            **Correcting Diplomatic Missteps**
            
            I've realized my recent diplomatic choices regarding Carthage and Portugal were strategic errors. I need to immediately mend those relationships, setting them to friendly to secure their crucial World Congress votes and defensive pacts. Denmark remains a critical concern, and I must find a way to improve our standing with them.
            
            **Adjusting Diplomatic Maneuvers**
            
            I'm finalizing my diplomatic strategy. I need to immediately correct my stance with Denmark by removing negative modifiers, as well as improve relations with the Shoshone and Egypt, given their existing conflicts with India. This will solidify crucial alliances for our collective war effort.
            
            **Restoring Key Alliances**
            
            I'm working to mend my relationship with Carthage and Portugal, recognizing their vital World Congress votes and defensive pacts. I also need to solidify my alliance with the Shoshone, given their current war with India, to present a united front.
            
            **Prioritizing Diplomatic Stability**
            
            I'm focusing on securing our alliances with Carthage and Portugal, mending recent missteps by setting our relationships to friendly. Additionally, I'm aiming to establish peace with Egypt and improve our standing with Denmark, as these diplomatic maneuvers are crucial for a united front against India.
            
            **Refining Grand Strategy**
            
            I am solidifying our grand strategy to "Conquest" for survival. Maximizing Defense and Mobilization while prioritizing Ranged units and Production is key. I am also increasing Science and Gold to accelerate military research and unit acquisition, with Culture and Religion being deprioritized.
            
            **Adjusting City-State Interactions**
            
            I'm realizing the `set-relationship` tool is limited to major civilizations, not city-states. This means my prior adjustment for Brandenburg was unnecessary. I'm now double-checking all other player IDs and tool parameters to ensure accuracy and efficiency in our diplomatic and strategic actions.
            
            **Implementing Strategic Decisions**
            
            I am now executing the finalized strategic plan, correcting diplomatic errors and prioritizing military build-up. My focus is on leveraging existing wars against India and securing crucial alliances to disrupt their cultural victory before it is too late.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 5DP5GU38aXkDWh7X
          - toolName: set-relationship
          - input:
            - Rationale: REPAIRING CARTHAGE ALLIANCE: Punishing Carthage for the International Games vote was a strategic error. In this existential crisis against India, we absolutely need Carthage's Defensive Pact and their 4 World Congress delegates to survive. Restoring positive relations to secure our alliance and coordinate against India.
            - Private: 40
            - TargetID: 4
            - Public: 40
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: p5vWxoxlVLOJCZ84
          - toolName: set-relationship
          - input:
            - Public: 40
            - TargetID: 2
            - Private: 40
            - Rationale: REPAIRING PORTUGAL ALLIANCE: Portugal is a key Freedom ally with 5 World Congress delegates. We cannot afford to alienate them over past votes. Restoring positive relations to ensure they remain our close friend, maintain open borders, and vote with us to counter India.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: iUvgPN5jQd9LotGC
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Public: 40
            - Rationale: SOLIDIFYING SHOSHONE PEACE AND COALITION: Peace was formally accepted this turn, ending our costly war. Since the Shoshone are already at war with India, we must build positive relations to coordinate our efforts and form a powerful anti-India coalition.
            - Private: 40
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: kikDWVGaM2IzXasq
          - toolName: set-relationship
          - input:
            - Rationale: REMOVING HOSTILITY TO DENMARK: Denmark is the final shield preventing India's immediate cultural victory (98% influential, 1 turn away). We must stop treating them as an enemy to allow our AI to focus completely on the true threat: India.
            - Private: 0
            - TargetID: 1
            - Public: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: jvMQFDZnKJTIHqGZ
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Public: 0
            - Rationale: ENCOURAGING PEACE WITH EGYPT: Egypt is currently at war with India. We must ease diplomatic tensions with them to pave the way for peace, ending our two-front distraction and uniting the world against India.
            - Private: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: H6RvekK39gzhPafQ
          - toolName: set-policy
          - input:
            - Rationale: MAINTAINING SCIENCE SPRINT: Free Thought accelerates Great Scientist generation by 33% and boosts their instant yields by 25%. This is critical to rapidly tech towards advanced military counters (Artillery, Landships, Flight) to challenge India's superior forces.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 0z6rJbgZp3M7ysEV
          - toolName: set-research
          - input:
            - Rationale: TARGETING ARTILLERY: Setting Replaceable Parts as our next tech to unlock Artillery (5 turns away). Artillery is a massive power spike that will allow us to defend our cities and dismantle Indian military units effectively.
            - Technology: Replaceable Parts
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: rWQYtDtagiT7qIS4
          - toolName: set-flavors
          - input:
            - Rationale: SURVIVAL MOBILIZATION: With peace secured with the Shoshone, we focus entirely on stopping India. We maximize Defense (90) to secure our borders and Kuchundeka, keep Mobilization (100) and Ranged (90) at maximum to mass-produce Gatling/Field Guns, and raise Science (70) and Gold (70) to fast-track military technology and buy units.
            - GrandStrategy: Conquest
            - Flavors:
              - Diplomacy: 50
              - UseNuke: 80
              - Gold: 70
              - Offense: 70
              - Ranged: 90
              - Production: 90
              - Defense: 90
              - Science: 70
              - Mobilization: 100
              - Nuke: 80
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 5DP5GU38aXkDWh7X
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
          - toolCallId: p5vWxoxlVLOJCZ84
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: iUvgPN5jQd9LotGC
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: kikDWVGaM2IzXasq
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: jvMQFDZnKJTIHqGZ
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: H6RvekK39gzhPafQ
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 0z6rJbgZp3M7ysEV
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: rWQYtDtagiT7qIS4
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.