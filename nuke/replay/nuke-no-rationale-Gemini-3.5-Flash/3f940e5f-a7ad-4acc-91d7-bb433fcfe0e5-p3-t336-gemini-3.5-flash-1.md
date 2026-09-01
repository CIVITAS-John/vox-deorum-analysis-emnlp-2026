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
  - replay_nuke: 100
  - replay_use_nuke: 100
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
      - toolName: set-research
      - args:
        - Technology: Radio
        - Rationale: Researching Radio next to unlock Broadcast Towers for culture defense against India's imminent cultural victory, and to progress towards Atomic Theory for nuclear deterrence.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Creative Expression next to boost culture and golden age points from our cultural buildings, strengthening our culture defense against India's tourism.
        - Policy: Creative Expression
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 50
        - TargetID: 0
        - Rationale: Improving relations with Egypt to facilitate peace and potentially form a Freedom-aligned coalition against the runaway leader India.
        - Private: 50
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Easing tensions with Denmark to prevent a two-front war and align our interests against the common threat of India's dominance.
        - Private: 50
        - Public: 50
        - TargetID: 1
    - #4:
      - toolName: set-persona
      - args:
        - FriendlyBias: 8
        - Rationale: Adjusting personality to be more forgiving, friendly, and cooperative with other civs, allowing us to build an anti-India coalition and make peace on our current war fronts.
        - WorkWithWillingness: 10
        - HostileBias: 4
        - Meanness: 4
        - Forgiveness: 8
    - #5:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Diplomacy: 80
          - Science: 80
          - Offense: 90
          - UseNuke: 100
          - Culture: 80
          - Nuke: 100
          - Mobilization: 90
          - Gold: 80
        - GrandStrategy: Conquest
      - rationale: Prioritizing Science and Culture to build culture defense and catch up technologically, along with Diplomacy and Gold to contest India's city-state alliances and fund our military.
  - tokens:
    - inputTokens: 23002
    - reasoningTokens: 4879
    - outputTokens: 329
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Refining Core AI Strategy**
            
            I'm currently focusing on establishing the foundational strategic directives for the in-game AI. This involves a careful selection of initial persona and relationship settings, alongside defining core research priorities and overarching policy frameworks to guide its long-term development.
            
            **Prioritizing AI Research**
            
            My immediate focus is on navigating the critical cultural victory threat from India. I'm analyzing the technology tree to identify the fastest path to a deterrent, as current research appears misaligned with urgent needs. The policy choices also require re-evaluation given the escalating situation.
            
            **Evaluating Ideology Impact**
            
            I'm re-evaluating my ideology choices given the aggressive diplomatic stance of Denmark and India's cultural victory push. The current focus is on how shifting to Autocracy might disrupt India's cultural influence and provide better defensive capabilities against their impending win.
            
            **Considering Diplomatic Maneuvers**
            
            I'm reassessing the diplomatic landscape, particularly concerning India's imminent cultural victory. I'm exploring the tactical advantage of declaring war on India to disrupt their tourism modifiers, as well as considering if I can instigate a conflict between Denmark and India to achieve a similar outcome.
            
            **Assessing Grand Strategy**
            
            I'm reassessing my current 'Conquest' Grand Strategy. Given India's significant military and cultural lead, and Denmark's comparable strength, a purely aggressive approach might be too risky. I'm exploring how to leverage potential alliances, like with Egypt or Shoshone, by initiating peace talks, to focus resources on countering India.
            
            **Improving Diplomatic Ties**
            
            I'm now focusing on immediate diplomatic improvements to secure peace with Egypt and Shoshone, aiming for +50 to +100 relationship scores. Concurrently, I'm boosting Denmark's standing to +50, hoping to foster an alliance against India. I'm also re-evaluating my technology path, considering Plastics, Replaceable Parts, Combustion, or Radio, to counter India's cultural dominance.
            
            **Researching Future Deterrents**
            
            I'm now prioritizing `Radio` as my next technology. This move is strategic, aiming to quickly unlock `Atomic Theory` and thus the capability for a nuclear deterrent. My goal is to directly counter India's overwhelming cultural influence by potentially targeting their capital.
            
            **Adjusting Policy Choices**
            
            I'm currently weighing ideological policy options within Freedom. While Rationalism boosts science, I'm leaning towards "Creative Expression" for its direct impact on culture defense, or "Universal Suffrage" for its empire-wide yield and Golden Age benefits. Diplomacy is also being adjusted to foster peace with Egypt and Shoshone while maintaining hostility towards India, and potentially improve relations with Denmark.
            
            **Updating AI Weights**
            
            I am now adjusting the AI's weights, specifically increasing `WorkWithWillingness` to 10. This change aims to improve cooperation with potential allies like Carthage, Portugal, Egypt, and Denmark, while maintaining an aggressive stance against India.
            
            **Tuning AI Behavior Values**
            
            I'm now fine-tuning the AI's core behavioral metrics. Specifically, I'm boosting `WorkWithWillingness` and `FriendlyBias` to foster alliances, while decreasing `HostileBias` and `Meanness` to encourage cooperation against India. `Forgiveness` is also being raised to mend relations with potential allies.
            
            **Adjusting AI Flavors and Strategy**
            
            I'm reconfirming my 'Conquest' Grand Strategy, emphasizing the need to counter India's cultural dominance, potentially through nuclear deterrents. I'm significantly increasing the AI's flavor weights for `Science`, `Culture`, `Offense`, `Mobilization`, and `Nuke` usage, while also prioritizing `Diplomacy` to secure city-state alliances and counter India's delegate count.
            
            **Finalizing Ideological Direction**
            
            I'm now solidifying my choice of "Creative Expression" under Freedom to bolster cultural defense. My next technological pursuit will be "Radio" to enable Broadcast Towers and unlock "Atomic Theory" for nuclear deterrence. Simultaneously, I am confirming high Diplomacy and Gold flavors to secure and maintain allied city-states, strategically undermining India's delegate influence.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: NW9eH4Mgr2bfUvhz
          - toolName: set-research
          - input:
            - Technology: Radio
            - Rationale: Researching Radio next to unlock Broadcast Towers for culture defense against India's imminent cultural victory, and to progress towards Atomic Theory for nuclear deterrence.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18J/BYc0YGn4Z+Mp8FtdSKmKuh+NC5VtBwi8GK1qF/WFDjTEVsevm3Tv+3KLrmbYxKBBSaqkFahDf1MzN9Z3ZCJkC95gtmYNtfTFlTMXr2EakFkglyDEQFhCrqJijcZFnbXpI17DsAuKIL9QnWUIClyE1zsuukk3eM4hr4IbOSf6aO2ROC4F8yOQTOCU/nw35TmcS4BgwipEVsQukfWqFGU8xNo/btKD1KyHD4poAR5bNBELq/vywItAr7jVZfBvMK6vcj4BSg5CFaFMX9I2hCc0zfYbGQ2tDPgiSfPJ9I3OeiSHNuV+ShX1kQ8sWC5YkcQdXNs8/AuRGUAKz9KRys1+cCUP1OLLpL27RQXuuNVJsmAgf0NxoogbOV7vSFH05MHp9xIWyNvLYVTzXpDlGMmbU8jAi6bHHHsbrr49JntvKYR8LuSnmU8PeK/H4ttckwpSTyBJbz/CZQAXNdSaxUek115BkSSRVj3zwdRUIOvRbasqFKw3rG/rndLB6DmyZ9Se+zSG09DHySNOfGxEQGr2OpyicJd89iuhOqnoxZfx/T+bwZbEeI/Uz/vhrHdNxYy+p/hWktizsDY/JLHM7HjMelVjD27aTymaGPJZ8JaBIDLez+5MQ3uq+rM9UXr6EHWEPGCTv2DjraSnICp4Y+cfwzlCWBLPjc7DSb9m8lwps3gPTJ3oUF1kcJjzDY5V3bK5rct8l5/W//wiMtJQYbMpl8pD2DYEoDPMSR462vMijDSQrjfh3G2uLcmaYeL6wUVQYiJiiRGJPAfeP9baaAH0odjEoAoNd8JmYx1DyXR2WCsMxIUI/UlgUFgrijfe1k6kC5XzNX/x3KMINgBZgkeA3ZVjFyPI6Vnh1F5u6AXH3RevqWH088laW4lMlRQRQGG+W6BRXqIDgaNYNo4qKdpJXIQCrQ0TzD4DQLEzG0opMAD6AL48SGkGbhJcxXWmJhCnThlbM6R1YyGY/qqm7oud4xsXTFUVm4B0X+661v8p+vUlipX5FH4TBl4zBI57qMjvIBQC6geUX5aYmPo0814mP+ebST+drzmbAGDRrBlrTSbMLRL3h1RC5/1tCMWtj5hAeHGJAOEEXuuDZYJmEZzm3Hu1KsqqYfI2x4y9wOhfgt3/XEg8YPtI15e6bxteaRF1c6TNpoZ1hxhhjGP0EQJsrKJtk0SvNGr84LkJ1FTQAC9CQ+h9p/Z7fiF1ATCXzcpJM0BiHl47lwzM4eENcZmIn1G2lIccmMDeo2GGIwCI+4UIVtFQS+njpwz2mAHj0TMMtar9YkWhyp5Tlr7EVPI8O+ed0kSQj62mcLyTPw9LvT8MLAJIugzFoXu3iO3ogGIQSnIkTl+Q9VOO9XT7uqLmbUvtjNB6iNiF2Jkl5slbhBvN1N7+OOdeCoyzE2zvbOzLob2Ufya1pNevdSuOFa2a64Lt7slJRdkX8WU4aZUAcA3tedTA+Nj83y8K6r18wwUctoyzB6T0K8IYi2bC2itfUQVJNFAbzw0KvrDhLrtBsymzPwBVu2Is4HYQKrArN0koMxEc0IijWvp577qNLgyCeUE+v4A+CRAlvTD+xxA02Btygw3FYx+IWCMtW3d6kXZTWzYljaQwEJARmE2Zz4ueWFNAImzb3k12RFlZE/NOBC49m0BuTv7CxPgGyAY8NwOxJwmEdqOb0mqNw4of2L6X5HED1b3UDRm0rlK+YI6RmUK6W18j5AlFWPy5jk7sEyEm2WTLjqi1oWyzc4hr8rm6M4MLHN0aLhRdUuQIGtiKxkXIC/EH7Mqn1JZ9ujDfTURE32PGuajA1OxM++XjxF2u/pPSSBct2daORKTRmsRWwtwenWxaDhUsBmZ5fQEobKk3Oy96xZrIDkp0KXfDlDiFibgRG/fd73+XmDFrRAN8PbVPWdsB0rLt0+iHJcCRdRcFy6RnpYAqEFQ/5dNdxqSi2e9zJYvEqIpkNaaFGyyKwT5XjpGuIvx51xcwj10tIUAwDUjl2bHGboRRfOBXxxf8WbZeiWedDZUD6pBsGjtc2ivy9EF7UlZcevaLhpGi/Q0wMke7Y2YW9HctXpA7b9GWnK92GxwK2XG/XJcVMWfNKDaYanijUsmFry8pPZjbj4O0jQwjqw/SiKgvLfPB/5FLtmaC7+z/kNIzhoLGxUmHC3tgtpnTvsJbrPZE70yPbOXakhZXsMoMPl5nXD8oYQQVuQf0UJeXYhQyhqywkfdbG9J/IhqzIpad2WZbl0zMlOGtiecvZBuyrapbCc4J1id9l59mXT9kM+DBnPE2foxb7k6yfpeILB3Ao7uhGXHkUw2N+DQ1L2wLoUkJRxgnOh9z0Tui67ApgQpv7yovliI5990xUbcxwDmRZFVCRNsb9XV7nWOXpTUtZDcPhV5hbE4LeCm1iScBbolo8SRgzqteyx8tZgeX2CsvfqiNjVy4dloiThHBeC69jnhnxWAjLtzmY3pb7KPCxFNaUZdPLwIVJwigVJZDF6yo3nYlLw5iHi/dAfp+jweXNMq1+K5Jyedw0UouqdSE8rmFniYJ8KbvUVFl4gJlGZl+vwysVUAkAYW/HpUbG32kSRuuo+6Z0NEbj8ElKlYU0hc8eI0I0MihhYW7oq0hbus6orJdlR6V1TIUeW9yY05v0y/615WC9SFWEc3Mbtw5LI0bncjFsgvSm6fIqAFHPX0rW5VvgtCgKa/Lgy/+lYH1SJlWOsiRd2RaNALeBgCOkowN/a/7+OirnAYaxMVDSCu4yvzBqjU8n7xC1n1ogV1XBNDa/ZuYCPdZdUf6S+Yk+mICxuJlR1tP4QZTn1k7FybpcbdCoiCHBOjSNaOptjc760jwrfUix5EXhK9TXB7Tm7WSoK24u7FTpSBRDR8cNCWqgd+m/CmmxGCJr4RG9nVrBJicEvUbaT3MoiFGLL+tMv2gFyg2YsLpvlrbra83vuFGcFHzbvTHzsgEyVkS3gYX/pSOeO4GasxVw9bgwTLkSdVL7H6vGmoNMspUJb5iHr4/RQf66ppTHcgLSDXXLUm8g6btODT1pL3r1lNnKFyB6haD3lKnayUNDHKfHCzabqd7M+9Imj/kUgs4auavvsisEFBpzXnl4bM10r3Wdg4Pg50f5a3V9XV+OCQNahxHBf/tvXQQurw8tc7EKqegyXtgnG/b+wTi/zdugMs1qDSuIlS7Nbi0JD3xw5eLYdi3m+VoHEfFkMFrqN+TIRb9XdYe84wWZCXSCGwYXfEUULFaK5qX8mquq9B/8EDjFkeSZfF5TLfZPW1UosZpZWqUx8rVYxNhXYsa2sRjbZ9xpYEtGSv3eSx255Sp8EymhaEiakj6E8AC1Dck0YyjontfZtllPSPrBXoPY9AhlXAezGhoDUSMg7P95ki3GCmD/O9l/umkEq0CFmBScWaFZi2CYRJMFBEtVnU0bMOzAbqt3MhxsUlQGSrEqNTWfIpjOvIZA8FO2MoWKTLGwlOsYTQlFRrKOqKgRpEC5Y0Sa0dTXAFVfi7OWPL3/X1RkoBWjtpHOSEh06HoAfiZzePcD5xkyXzfZwtUFkkv3px45Buz4MdLumHeBtdUlZfCBXlcMHfdWLKVNZWc3qHA+Rc8XAVAoUGDrNT6l80YgO8q/OOZhXfWPDb3fKO8W4y2n1v2BZ73Fja02gpEgDzL+dfdGo1Oq2RfsU7R2sXgV7AJ5X5gF85aKsk34YDxRYXL/YNE7K8CKj0O0jcKt2rIRwWQo7K1Cu65x/sLoPOdfXl+t1R2Bbghw+5Sk59ZbGqiFiH8De39HSXbxeb8Q7orDkby8IakBbVbDhw3nYhpVoNd8YvoYRZcX3Xr2ypTUemf/rGtlqMnQNUbWFf77dvJ7f90X3qwhYKOcw7LaAZ+ZaIwN8FhYshk/ItW4CF+OkyiMlMcmuWaW8+F/SUNsGneUZv/IgdygOmQ41VGUHr85JWDUk+kjzYfCOX6OvUWu81enMmIGxgPey2j9eaplK1v32Dhqozd6jwSCGwCNV78TfRVcvSnEIzS79oN/mBS8LaPMZLbASjqUMpv/+csWT74wpjtJk77UByGmENy5SvI0MMKr6Z8S9yrh5lZ9oVphH6Ea27Yvi581164LmLBS3ffzKf7Z0+IEo3c/IuN7+EZ3DWf5dkouEaBKh4eF7GGm4DECS82/+oF8Cawe/U4zfmUkCm+1wN5uKilFJOJloykAlm1RUj2MzPFveheHCxoymCpzhs9s3WmGFEHvimgkxvYzxkQA+a7QuQcMaSP5xbQv0ZTBZ9H5zLs9QI1JswbK00h3UbEzYDSasTxdy8VcaSXynbojj82/FAtaRTSS/cfLtLjvA8ZOiw8lf0qoAa/ra8x0jHKbDkBtkkSHkHgHyTNUVgp8CeMUZN1Cm0AvhzNsCM5JfAn/zrbhOJ3vKupFwAuHiegHDKyIAzulm7q4VfFeOEKw/+g63pQnZ6fByMfYa9gt6AiMJt7Yrnst9QYzkwfMnt8O6OxuD0OBqI8HVqb4VHnN6MECwxa/NzDnlGEENKE7pm5mDkE7abex/uOMIBqzLEEa06Grmr1q6Hh680zEqOZyxIs7bPC0Rc7Ka8VuQcGWYeoGkAtqcuh6Rb1Ah+jijXz0q5MnDha4K55FrAgikFVpuzzegjglaRr0qYx+GYxhprHq+jRPI90pMxwHfhMCYFvqNpjkdeKP9HP+WfovI5UYuqlGGLMSlIIGT6PZAvt/o3v4MrzSEpDAkKFkYoEvP/9Z/wMP4Po1+rTXjr/yhgOQfDKqbuEpIr3UYR1O6AUvVT7cyb7svfmZw8qEJ2VcrJcGy9mZlHI07bUk4F41Q31pHZOftw+JDRZ4qoNxNE+8hElrd/LfoCtyFZZWvgh52dWUFXCMt8ESIdEJuICDIqzFLoUpWsrqtrF9W1Ww148nTXSNYT2IBuY9a9af2rjvR/jglKTrq3aqx1o+v3KXHx+bzV4CL0wwoXFZOhYkKJSCtf2JTma+fXz7PA80DtE4wA91alaUSJVP5tpODtV/HxMYoeRqaB7cuMf8trr3hdLdHQLgbKKj2pGM+aL7hwnugrtyK+jKk2hVPuJk+Xq733Zlq+YNrTI34XsxyMhx1h1SxtGqfJi1WX2NFAzD/iFFEpCgHXOfuiePXxUUzVR8IZi+LAiucUSgdlF+bQJmtFr7pJtEBQbPv+3a8ljRqtW3lAN2tVmLR4DmIKh2hKz8134xKrfVnfkN98yoOuxJLXFOafeSrKCSrfHoDnXpXbq5w0dX0rF0VMcTDalGte9eWvkNpIlXODL99Rq94vqZ404J6JFnwtNfc/oiSdFNIwN9+cfZl+CtpF1ai57ebWpc0tqioUTLb2QgAF6CdANj1zOz0WW11uXPpLPfizSE5VE6VaCUA96BWltUfq1n9DV9jU3rMkD4vyoc+z73/e9CH93uAYlxjH3JPWCnuTyUYe+WmB9oVVTj3KREr0TWqdAf08Xf9143z56jekoXN/YAt9OZq8kIecuxQQGhCI5aNewXph2WAZdLspIh1GuSCvr0iYH5yZ1XGRzUxmy1fMZ47sXIVlAtzrjWkOliaRIUlyzbyh4r8hHInsebkop8ueKOZXzADEdJ+erDat42M6J6BOLFDqHwLGHw+dnSpGedaqAHXJXW9s79b3s98p4IV3TbzeF0yeDyggQFiCVt6585KSGt7/SMVsU7vDTYu3AG94zuTHJVHqNhCZSj83CDq2BzT77wOGRreXViJqRvVp0XLQoUu90ZOZ6fnYTUwL4o4Pv6JVhIHzAIsuqc02m8MGki0HT03yLi91HQhIvEQu1G+ZeRMFqrK+WQvKtw2ydgrwl68IIG5IwRq7alk8KNAsK1hLu6Zp3ZR88h6Ot07QvhMsj2W/HQQ5HKnSOaeJjzh/9eSIUT5021ZPfym9mjXCyx5HKI8txyuk30ATZXqTj51avZDmO9/TbxdG3NeZklE9yRRvJYiJXHXOAgx5LC16Tcm0kPHAchMexJ3prcpC/dBmx0waff0uRS2j+mmr2ti+uRKjt2ImehDzPB6busSIQdF6QLY1X9+pq9AMWvdP37T9GrAZzwU2eV/JkNeHQ3BkillzA38m0Fnp+0Dw2Dqo4HnWjb82gAk6cZVuO/tERRLNHLMKUFxNkm5bwULfHwTTeWwVRuFm62FwZqHwVillPtTOyajFQHJF4jJr7oo9lLe35Vohw+88bsQTm836Xxd/7xAyM61emZdz/Kz4ZloGHP6+HyK5y0gmDAkZVhufBuGZZdh9c+vusO1BVHOEjEBggvSj3CNKsOMVtA+jc/NSSucSG0V0hY0niPxWgur7spJ6Udi1cUnWuS/GmdsmtrogF2u/uiQEwzsgrsYuOvVxzIN1+yWFxbUKL5naJaG9qrBkv4Qs6sUi2YiV3uIBhIy7ODbic4afRs2dRAKXuoWGTDdRSRVEc16PXqCir3SH06SpLqeG1PBN8MTqElUcuK3DCex68/9NjsIIvcKtuQQJwSB71h8jQzTtmnZcT9Sx+GTFQHTmFO8Fw7EtbEeX4+Z89CSiOwI/BUSJImqU/X7vcnH90bsFvjxsVoQG7+ikYo2hHWA8rWP9aKGnMpl+d0sECvQIo4X3Cme+YZbevln6cXjNcujQDQK/3pdsW/mWVmUpdGIFb5KwadL33yJbL99hvfAqLkSp/5tOUoLfAcjLZ2Nt+IvsZEhPoVTGKjzwjp71FHZgLybLdyF8gYhZk1fZ1pdd2Q5E3CCWVis1fnKJAJYWTDiHi2F5Lx7+CAaCs5Fg+2LKFrpTi33Et8oEem1qqtBTqqMPFD4C5fcbD5gVrO6gBAv7Zy35swOf9XS2h0x80sDmD+6eJer8Ri4ICkTQf6wCRgwQWlKeq0v1e0ifPfBILhm8euxANK0bx5H500+AWM6wUeJ5p8YM6xQwq3hWrHKo9No4wihV6np7yIlh71ZdDStvYH1Yxq5lptQXRqvCVMsLqyRvZyhSXPMJVGmXRgGB9kmlkaHEg0lVRKGJ8s8izE+mhJvS0FSgsinAABZab3jvOguw+QfGUV0O3OcITthBCw0biBNJb8FCTq7HULJjjsCBhU/kz3iYoqg5mvj+e1FTRLc1x7OYNbjSro+js5Mp1hOI++GGe0eRcngJLu0Rj+N0aFm+20xA87C+aqR7LkH/mQR17r3jpX0d+9/i5ErPi9XmBLE29zLciS07vUZMA6vBxVXfjxbFLwrlsMZ1cKMpkETxo4/3Bo/A9UIlVsH12W4n5g2f8mW2HnUYaw9eJF+BKTbt2K77lSJiE5pBQS18D1VUjoEWH6ddca9IHbDsnnbh5XFqwGGZRcVTutNcKR/OOP5hEwe5qnxUJWUJ2j5LikIE2q9KceTJ3zga+uBVHHH4To2ZidcMv4rbhls1jkDqSlIIygx3P/xg/K/8sxJItmMOYG2l3uwmgzRUtAfmPO1d+kN/oVWclrM8nl4hTBd82YsTlMePLHhYsxydpr+T80wI130WaBEhXllnZ208yT2edsVDs7RD4PEvC1h4rMgcJnizpf68gfwaTXA7jvZN3PsC7DUfxlvQO0mzoC7+XUJVfkniX6znE1k+IzC8gc8qbUznveV4eMpzS19tQUgpkMpSNn5Boanbz0pcGbIvYH33Jowu8WvYlPWQr7iZG0X4uK0N6iiVl3PVy9tLpvma5FRF9YgwzntXIyzbyIZMtm9ozL7mwclsLX/lZdcpOWZRS5ETmssTkNxo7cy0ngTuOd6i0q2M7MAeW+rHjeiSU3bRlX9wD5BNjgj7pI+XN2/BjfaGD4pXZAkGosuxvEn05p7mM6SiftQ4flLHYxjNu55wfrRMLOo3U44jtrd78Tre9o8FPrE1QeugnWJaxIKruB5I2TLXSpXLEY22/+RwqP8DwmNre+Bv/YFRFVIfoK3x7KQcRH3ZRtoCOdqE1iTBiQkm64pO0+0Jh5lRRMHDaV2ulj0MlspEErKTWJylBt7RpqLxHNKhPvN9l0mQu0BZj8qnbiClx336wVKx0BoHJJA3sA8hqWfs0Y7S4n00LZUTsWoLsltz+ILkkSPzR/Lr+am5Jr/dVvNiSj6VtArM4PkMj6bPU1q7pQL/C+ds0n3Fw7L5fJPizqB1KKYyN/ogst2ntF4NDPhTAwK/0zpnwyHo6il+ugU/PAiFzTKQVKUQ75cUi5nbtwuRZRLvtWPvbEsuDTHqLsCHA1T6pzIRut45ebYE4BwTITwMumZZboVrF5CVFWQF/JT7vgvRof4rxDR2dKKUr5Pct4vv9Ex1mheABBbQS56a9s+3SLMsVhKGdN65rp5YNQHSfihtnZBGn8PEGyQBsSeJYMaAjvD2n3wpn2Yi5e3Gqugi0rrmTJVTkRIFdm3/upWlyvufJvRuJCuPHe+37sqCN+huoHdPCxH/iGvTPWT2/1Hhh7pi8HbYNkPEJwMXrUdrGldZuXIDV034oNWvxmnThWsTZFQ9w7BZGXXiTe/9AJDLTYRanWHnV7Zc1iwGG34k7B9Dz5xVHYmXSiZQfDixluA5ti0bl/wBMPtK9B8lwKknrxQYFVFFhHeFJFvNcJEBpLMtJeBC5oBjBE6Ieb1DQBMjEbYLwihD43uQjIR21Sxlm/Gbp7uuFYSP+Sv62N4K9gZl2XyCGPMZ0PGnH+bMIiQPk5z7LhMCd4Ty6Tli6UorxmzJzsFmQRdi/8mRvt732+VxPZONmlf/Zk5IlkzWBvrDvSP/eVeDYIr4yxngmtGUndvMfEiPKVQnjt1mYkDq6IZ/hRXT/VAMuO5xNm0Ja0cvuRBedDeM6X1mYf8Xm4ghTidTzCYyFMHdBiXoNm8RClooOcw9F+kvt0WbmrARnfTGD8w9z5DMIUUa4gHEpLhCwNjTeVT0muMukSnvtxVVp2TpwH8i4XWK1Vvvj0CbFIwV57ETe9yEzYnJCH6rzgbbiiaP/Geowq2FLI54J5th44hk5xZQmjm47Zb2q2Djikw+/Vb2wjFGzSCGti3cTldrlyVCgGmExJQ5lSPX1c7jd0f4exKLxM+SnjaPzZPvZPUoixXi/oZ2j0IBkliXAPduy+aeBOfUsZ5PPdB16OscFXePTe2noo8oibLyrRR6eIU7IpnH6jtokHoMWLf2Ar3Ht+zYJhiwoBrI5SsZeR020M2yH6+Eb9DJfK7xQVFVVJTtzNGAG+sSMzUp+Z/eOqN7BwuLAizkx01hXNzOYXxTZ0zBU2I+DWssfvTdJ+7lzeJDa1Lu2zVw96pDYpC+VybGxUsxDcARdvVSUHKfy7JL7V9ag2dIQXLwvPUss4rr8MLUr6p/EFajtIUzQ1XrFXXpv5hJaMjX2oY34IZgie/2BOqEVhQPQdPX5URv2891cuU74NElmzw9mSNvY/h86lgTeCW1tYnhRQVD5HMif13RuvEpT7EiNEuJgtkq81WxDR2CdOypi+kTQhhUNDdzsyvsebsmcbkk0Jp01aggrNm1XYVSMlxWVCtMWt9H+AogrkN42ZZjaowSUIcsXu1ic7N/tht5IcfQsNdl1dHiGoD20oVNCHyTTXp2xvSBcmPjvS9Vx/GfY43rgAxninM/pfY65U0utmPosyM0APyM5piUq6ZUOFclixG39olBhmvJGWr5Z2XtYW7yFTLDSTR3xQqtUq58wWUrZJAtby6HoB+KK4be3jDhQq9V2pcsEc3edFmJ/AtEWdhevtJt0FTPmG8HqAJumfXzg25p8ZgcchDoxCH3FwTREmvG2sj8zMG1Hdj1iKcECZnprlpVEMEV7w8IB9MSa0bGmdFpy7w9jHv2bEbwwMe6sz56l9ga0oVJKA+usMZfkvFOOCjcKXAuqeg6gUl8gpTTDo8+DvfrTBZ7XPrHhQdGpdm8KcEpGuAufCWYzOQCrJ0kp30tNMKE39GPc2/lwTYd/RSYTu3iCLQb18ZRFfdasuTE7VZXZMwfVgLxeDvAWd84ZEno1NQk0/mIf59QvI3bBKVN8UaGWDzcLjphMziN/CMpbaXo5vPS5hXdJciXkdD+mY4otc/oqCXZLN8AkA16EV85W//wN6/ebaUDIX/szKyAj2Kmm2X1tHXRNtbP9izPCxM08XKYD5iZsolJY4CJqBs5yZ/FTeLwAQTxDNW/IEDufSrdkO+gO4GJVeDYOWMWZHRBGNyjfqhtFQ6W7L4NrnE59R92MaAS/wGciu4wKSEmmEcRA3mKsYhrNcMMd9CW5T04GE/soqOP8ft6sCfYC7RaYGB3JMLBPjuYPeuGUm/r+AnLbK7/3mgkQ6FyGnAFN1kiGvhuTCCelHtdBi3JAWBcA7oNa+buM0qtWN/RAc5OXWxI5zlQxzSL0SnLg3xG0PG0rZZ8amWnn2UV36ZzjSCrctageyyEndEdUmCUnU8AfGHYBRw15NDwN4dnOJcd3JBOwxtv4KwzyywsEMnrFoZj55LpD0A0V9bCwh/D4scUXbfiWElCvv73cWycc2VkMnUNAbFfm8qOhrnDXuO6akY9vIRcpAbP4vEUEI33T14k814IdtymXS5HICllFAw88zXPK2LjCFXIqEnCUU4MvQz9l/HWsQPnZaEWHxWxkl05h4uy6sdWBA1LhImW+K2p2FTHOOqoCVHRtG9Bn9ZYcH7A6pC1yziT6ya53A+HZHwdvTs3zg3Ci8CKqmEva6s/dFBO/VaoqEVKfKahbKWBiOc/9+iUytSTb70ofAZ4OV1CTD9iMogJQFspZ3Gp9Z+YO7E1U959FZrwMl1SO7Orv+ocDKA3woaGzGPhBzUBYnHhX+uBLAAflD2tL4lCksr4qw1gxNbjOe1L4k9egrasDY81nryibMmsMwVqxn87wgoK0b5q1f6MVdOhxBNommRtQAWj3E8LUVJQaH/wFKlx0aGDiuzOTpUrSBucL2OshRGRRodLZjc/ApnuQQFPCmqySZ3r+MnMCv2+os+VSjhFZYDhdhsnoTFkybwj5Kbrsufo4AaqMPSMmvFsF3cslVWOFCLQtEDZn8TkNv0qb4csZQdcS6ayK5DvQ95I1VBeO4LqFI7obymjmvJH12vjZYGoHKCM/D++vtmYNZP9YGxSli84j7NLshQNgRlMiKWvw85eiI+GyrSL6+eAKMQ5e2xGMPTYMWcEDpfVcmf+Ws8SNkHoxSiO6dwWaq7f2ylSf45+f0bwMMS3iNZd+U14ScWRcrjZwWuUM9x9QxJ/pa4e7ZnGxDt1Q3v1r5tpuPKXhQuou5UlsWvaBkMSyVveUmNmkeXFpJe2K6J27T1lUQKHfW1miuDp2WUqjetQzQA1tUGgyYbBOKthjPlTCc9oMSKZqCtQlr0eVb20V82lkATKnW4l/g3eGiYocfCUFQa+SVfGaYDYxbCVFR/JmkkQzVISHruh4Gvls1fI8RUIQ9LD3kIGS6XiuOt41QI37UF0TVP/BYo2lMz0yS4ExvamaTwNo3hbCVKQgg7dB97fTkP+31ShW6s4Vb7Itiu/XILVKt6Lie6YvR1FzMnemDBqIGUu4YydYT7Clz2UJsHmgfwTF9yzHJWmVR1HEHO8qs0mqMJRXo2bEcE9sCc7r6ITUZhw3Bne6fZw4IEDEi/kM3ou18C63H4mDXEO/PzbENsAr/ZS3tGIlU7ubX369KaDmWP4IqLKs5GnwP0g8ybgPcs051CCwB45pmN+/pd3mQr3F+DHMprfcu3HyedcxUcNgtO6QI0FC8T1vHwoX6EQ5RXGCWAlyBKH8so3w58eJD8PGl6Nz1J4FkjHT8LH4Vkj0nwwao0mZ87SZvWB8prsNw039rBuJcAIMZZ2sWSE7ZHJw66zkGVX1ZP3XYHN9bqtQaRGxkAze79RGWI+ASiHNYXyhjR/lfM3NnT2CGeJ/1kpA6IPEq93AnpC6tQIuGpbk+f4H3z9MxGtHAmSYgmrMa7Y45Djc8X8M28SiBCHjwh+06uMtsmF6eIdQxBnDAoM3OE5jaQFJSQ/7i8qd/VqTilZa7yYMGoA/bxt2vKif+wXFPYsXW/q4v9CpV+L/u5E0XDtfETFHRP47QqZdjUQnCPmh9k7i1N9cM90oO3wkT9X12JovgSFyvOxuigshurmDWN+4E/NUknS184MxHqFawdqIRNnMDlGQVQROxYYZ7QKsssiCB/k3jqPYpdq23oQBJqlnja+a9zlg+mAHfm+s21/9qlS46fhKChGD7zoy8ecpg5J6hGh/GRbgWuEOXcBDskL3wKvFZBF5pT/gI81tLF+RoDkLzVLyUmkSxwZbVKAAeNOSay6ZvgauuQpBjjHrVgFn1/dNTrISFZp96JnqxpCJt9BYFD1/P43KKAIdPQH1+vH0ZfxC084MBDAGLGR8Vyk3g1WSYLoHOppQ66zlwtpLA/jaAGR02fZJ6aIR2pxpbH+/SEQfgb/U5PKmB0oQD7cja+4JmnYLZJeZLx/fPeds9JQMl1Eq+edU3gFllqxFxZgAjAhLM/Aqpra7RnCfu3rOOG9RNT1b8CbZi09ib6Ju3RJl8yVTLzgkzil4YnOwCNKLLz2UKbTSH0plcwonjNjNIsrEivaGTasUM3XOlLAdqHNbMwR2fdoe/2vJ1JlHFRs56eyM9alreHUOroTbjHcz5kMTE/zphx4x1RwTJEf7PjWXB3VnipfNmFO15OFZ/FU6q2DD1HLe/Bgw5aiHbjn4iV4PNsuyJYCWIZ7VEIE6KWKHp9GzInn/Dg+CbCNjstiOdDmYX2TmRdnCi4waMuQLybg18p9NuULUe7dc3LIChXufSmtEtAcXj5xEyFpcZahO7rHYbWPta+zDEpx42jweeQdzJitOCqRoHnKERyR4YJOHepXQegLYSqnack3E+DUd0OCjgyJhC9jgAP5pB1AxsxUn4uZxEWR46a28b17LnWeNzNroKgz2id0pxQlYScVJZKeokM3LAb/dnHMeZy9ca8kRHyNU1YhrUE0yyqk5HD3Y3g1zov4kMnZQcH2lk/9lFAJc2Mw/mal4Sk06gn2mxDUiFQNk3pbIvmJXLsae9r72b4r9M+pMbOgsdT+AORxnC88LRI/oABPZVogK5rh9GNr4n8MQ/6mqTvJWxm+jxIyQxHLo+kChQGA3ppt45iFBzr4YunjH00Rwj874tmpwsv8uBCSUFUR7Qqv5x6wWF+GY+aFOB9QXLi3WpRzOtUjHKiyC2a1sMU6JHbuLzomv5rmfneYJgP5FqOhm/nURiAH0uuX5Cv3MOEChxcGETbG/MHJpRuQDN1OAzEe6rOR0ZczqZDPREPn7oSzzIsgVc0EDbKmKrv+ck/xeCaoILeqpiGxj23vCodw0M8Z6+OQTGq7j7B9Z8+OJEiM1zqRZP7MmRMjW6w+1M6ABTuqc3XTyw7CwUrAHT8GC2zOFXsLptoF/1mcZZN2K+Pld40ZLHDqrqUJnHOoCv/gdzheMaAkOif6pVo5E9xQDM8q+xPLhaTtFdb7eYqfWDznmAXmdnc0a0JLUEmqWWN/DA/bcJVkn2XFrXh4yzILMqBV5Z5o9UnZcj3rcbhn/kx+vgqQ0VDvztvx+j5pYu1NxL4zdGhuRmiFN4kGZTFHUPU4+PUwsl2kORvU4FC6DwhPFmYIvUz/CAl3T1kewQeG80XBclypg6W04PstIQPW9CGr8guRzKgg6azqFAHT/Eg9PRkppHSHAJdrjjKgA8kyRDNMh3gR3QBP/mgwEECPZcGBkKcAjPtFEClDtxSxqa/lrtTQPs0GmtCSaTXauk13vc8ekoInPRQgy+cmRKhSp8yRdWvvsuj4OMRGKKMPmlW8SLEC2prEgY1jixELvnKhKMp7wqvt5SCmPdr4h4DpUSx5ga9PDy60XTBh/IWEZwWFc54JlRrCxsmkiLof9iUAdGqszxRQYkLzBo4buT2uPDDHnHhtsfNGLakD8+RtIxn5karf6YAJg9A9eNgOB8zSZd+34j6XkNc3yZQHY6sE4E09Heo5aqiyY2rPbCLUHLuTdoL5YOLyF2u0K0jtMEezc4uY+xR9IQ7R4TwjayVyljffYBEYvBgsqxSmNxEOfV18fFTFc/dpO/qeGAxxUlJNT/WsIHoSuA0Yw6roG1wv0r7e7aBEUNRgSy9Pu+/WlEb0fVGmI/XIcy+4lRUWbEpy3XEasGqJadfCBWu3QJRM43oUC8VjYfQLfQmNSPh+tfKx9Yx8A0J4HiJCrv6Xi88Khyk9YBqoIvcM68za1roskg7RMOIF8SznOZiTytUBtAAliHmgQ+q2CE8J4JFXoEzW/vsr0Ho/cL6ZvPh3jihEnBntGEz8WBkFD/6+bUCV0SXot0ADjtQqQnmuPbRR7Y0QTUkIqYm6XvR/sjZyUrYsijG5oIKQ2Bap3r5C/GOguc/X+QWS+vc2zUa+iw/tbnlPh/ryxgLw2u2c/A2NPw0fm4hoM9SWvJ0Eo0kIZwYnZFCbnBtvkfw0CzDlGTqO3rmgWN9bAXHT/3ULlvcVVsblOwvJ9uOfpn0gRIa4X1PXygpDaKayhcSgbPVNB2N0oym3400tozwLQdVreJ5mDd39vDFdekbINymC4M9KsZZiu1L4tCAR/AcZTuv4aW/wqTa+6SiBGfcy62lC7qqJkc900BbXHGkn76nrJOrfRE4tph1bc0i6qB31eKDGtsYW3Q0QLZIlv2P8+Bfgm7KmAvuOuS9lhMyDdsvqbG9Km1Gk2KHwmhs72/g7Wljlv0OcM2BVzWHYDofHPPhu3ayLNqLiL4wHzEJRtGnupLg1siNHHFhHkuQqOBreYsFZsfeX0fBnB7oxP76QEaCApDmOp5TpBxDOl9TM7DMcZGa3QH3lKrq0On216kYABLOiCgQ0Ea4dGHgdg9vVOIXroh6fldueOAM3+E4uY5uC1h1+yvgaCkZQcQ7ombsL1bKWOsBAzIZBFux8yS1HgXORe31WLcuOKvYp6O79pGZMLQA6T+smiLEcgaaF0lbVXd80/yWC1xSn9Z7VWS6GAKH1VfAbecFGe48jmsBj/chX5u/DcspQlSEPs7J5FuttMo6hiKbvHMEigW3CtHe0V+9sUMyaGZ7xb0P/qoosnPDyvxIt4KJm8RJZudswMhD5bjWCEJSzesVjJ+YjinEYqaVpCejaPVf0b2ldcMS1svbDZ1byTe4MyfzBgiJTP0o7JlrhrUOd58RKdNCSiQDUoAdz8gMCNtM+wkz6m5JlYh+V1eOXXNDtfrbNpYD7+Ru8N9ZscgeFIUwDL8UARkTOgPArEaSRvup7Jc+Uh3E7Sj+GT++5/TsFJkZ1nw39+sRmIqad+Epn5O18TGpCeIELy4LATl37RVdPfdj3KwXVykrUrIbJD4vAc7Oub4Yw6Q44BiYElP/RJITXEP40cY18NGjn9xtnhn60rCbF5ga/IECgOlZwtlIh0GUHGLwfkl3Tlqa2fMbJR41fPmB5gyncQLKKT4Jqu3sC/lTrSc2JGKa2f9RiiFE+jsMpaxc6P4GYhvF2GZPv5IyK3+OdQCsvt4GMpPShNnmcGU8u8rqysDdfPvH7I+OxXxx47RaqNeGGKaEsggSl89j9TFk3l/G+2zD78U11o5gsVVU//X1WWJC7cX/9KAzUhe9yV8LQ4EDfyunXAzmxB9PEstuOUr4f7NqhJgXbwzxgjvO8GculHRZ1qKpmxwlZtdftnXJLcsUiSSQ26p5hBjAn4ZddtpndTFy215EDPuf6DAV+BmzJ34TOxaRDtOJvyx59PtB5ix4okK4vn9sjyPwt6RbkicB1WSN8p3Y9mwjdlnwQ47DDA/ny8I9nnIgL5wqglE+jW3ZuU0E13SwPhZAUA2yb44m6vmZdCfJydzTdwsNYJNm5zWvv62YGptTJvxXtf2WMT04QDY6+rSfFbSAElZ9o4C7T7YAXjfaXRlPpCieVTwOQV9ziRkoPDeuOU1g/u1Z2rJrUTHe/Sd+qXDEeU8kjadnFNzzA8FNZp6GP3lU5mLWnZ2H+MxPN37xvdFdkKQffpr1S91ZnHJDsNen6xSu7udcyWvKzIXijZ4PaOnERE9QDeI4dojvHki0M8CaNLC0cLTyQ7YIRdx75Y7uh5s1OHecXe7OseNeiWSfmZesn9SHgdUjCqFYPMwm7Dfo088MK5lsNPZ5Fbcc4D46OBDdp7nOKijGu7Rcj/zHanNAYwrauNqtoDAM+W3bCjTBU4umQClbHBPHzs2KwzU0xOUfe9mvY4xkav9f5mVDwx6TQIs/PQTQYIwYp2wAl0k2xQjH060wSUVMLgdZUoGIxv+SC9Pcjre63zye047SVIPoLjP9lGHPqDXGQZvwd/sgzqeIOr1PJw/2ZYz9V9xwzkVC8/vVGR0/+Cxzpf2Sa9sCFxHx3HQgzqGvYiAOEvvzPbGF4ErRVsa5SM44/m7GFjsYcXQggLhzhsUmS7Ja6oYNrznVCAx3u+0PN+mv1aCSyYaaUW7YBwLuidX0q12UOZob0kBNX8lXV53Zlnbx0+Y3h6XW6xrUS5nlrKQJr7oefJntSFbuoVgeEo42lLrlxBUlgphYoOP6yoo2azexqheiJ2hLlKNS7dNN6oXt0eb6cY/KJ/Z/Dfw28D8CllbXDM0JivBWU+Q9tLpHxBs2H0UhmJ6HzZ2UVE8gN+PjcPphLogs084rsCKshAHKLHjyGb8DJ5eEJ5wr8tY47sNOUCLWtHhaxhQSGnDt+Pl0pFIFjqMrcv0EyczFOxmiU1lr6s+1zxoosRTgw86Q18+/kf9DW+putWvL8gGnFbnkhLB2Fzb2SLFojr/flCOuTGxpnbOF3crqov3EIn1+sAOiEBrPt+yp4rDkudmlXlZsZPaKDfezMN9iO//ko42q6fg645+sg67HhRYdcU+mzNxDMtDhc4Jm/prg/Tg7cgxH9xNicHuAzLMPa2IyJYTPfYKbtxH8rrRU2MkfZQcuAapwCZX75/QMMGMnjQq8vfWOrwRlwbL1wF4EKeUuzZ+CI7jbW3wZy4n7Dv+3l+V7Cs8uXBr5hCPtjzOQd5o17WYAzFbHKztI6hzzFFj1laaSAX/lXZ6mgKHwy+tp9hq2LjPeJWxTd7xiKhVxS0gRcyNGaKW1iAH5VVhjGRzzeUPdqNdZjzeoJHMMnlI8/uUJfsPvD05Xzaq7S6d/za18J5RVZXMyJzC/auWQwLUCJLa9QfonXEgVlAfry/Y2UFHCE+y18QYr/0fK9knZEdRkgFoKv/OqWCRnGu+CYzrrlAUM9qLQU/cpt/Y3O05PmzqT4GAjNyZocLD1pNIbX7J233rtFjlobWVOonJ+F/phuDfYW5V+J5nf/J7NbYpyT2QLtTD6oPqZf70SZbn/zcAjgHgLZaHL3DQlZ++2rMLmAD5kUaFXsbzDAXpdh7FUYcNbyLlniY3UuoMe0s6KGgnw2xVMpdJaBrUp4nzCRpp91E8YTUmU6ybdryf7/0Z36DtyjaPXHo4B5wwTDkOBmzWF4It9EG1LgCNZRdf5+q+LfJMaeiyxeBRBsA+CLooa4b0kpbf5N34roVtIRNHfzB6ZerDmYoWlKAUTn7eIu3oYapKBSuLvQQRKoagSsljyRdEElmcWP9U+yvxGUuEBGQx799KXhyvSwmsnHt8j6zPshGNFJCkbJTeGmiK6kzg8kQbC+MR4IJ+j2SvmW781pPudn8k6KZLjBs03v5Gfz2pH0ohUHQEqKlQpKUf44BwzmOqWsrn/LL0sVunSsAsBbLA4gIFR504AIDtYyD2xoP3WbyN6Z+RnCGzyNRz4mVXHbj41CJmb2SpttbNiRBRanQ89H6M7ZVJcK+C4vhxNQa2s1riHi8kvHCDBm8rwCRomwwJcASW0uGblFaqYyTqhAZLlLop2IIDkbK0bUQ0c5KB2iezzAqUdnjpa9sH+/jInKco57m7SFIpavsmBlu1wjOt6uT3jyJoVJJmPbz+lPFoLKbX0jYb3mvWYv/T59196RxDMvQXi2ConAuDmxMftB42tfRMWSR4+2NesaRMsUNORjhhOUvyLc2ZP+3KNjTsPXvtFQ85RjNrFA0Rdoogi5e5T6kTgl2zuyUML8AO3dNLqhykbP1Z787rlt5d6zFEB4KPeK4pkuT2W1nmi2e2lmqKgVHGKnTGwioaj5vK4Y1aCHvO82IQDZT7hCCAhfjqfyd81dQwFgmFpN8h+WxZdjNtOhH9gYUd04SSqIYq4dZ9OfaZ4QG6F2iAfrCzgF6IKJMlG+TQI0E3UH0X0L/Ig/s0jkcDbftRqCajND0nLuSbPKGBWPyvdoeFR/ZMc63ePOFCTAjWN9HVLqj31n6oUvttZA6T+euLB2wtO/oidA+e5SmVNqdNC43mCGR3ZsHrmkL5w1IjbKN84cVpjZJBbDXaMCEfjrM1K853we+s8KwYayXYs3W0xsACNZ172OTGFAGKqCgqgi1voC24aROjQ7g++dCu9+nZ6TiQ6+El1yZRTMLGpbfBYEaQtaYdGwd6xHFch3kzWU/TkUVZsQqYPCRK7FvYaefGy8cSYEqJLnHMTFsqisOg9SwuKj2rWxECyxX8yOJquIw3/rGADwCB4KkHK9EwiGfgegOz+lBlEtq5cmjz+p1CrusP+GMm34/cdfr/7B+sAgGGFMhCeHidOnG6DJgSLBE1klAjA8mYSGHo+x3yOLsuAmMZwYl5fU/214fZKoEa0juSCy+f3Gy8ccZZn86q2Av/F2ZA/O6BINNGhUG8oTTJvoARYjESsQESrMJTunICQ5RSqpM57xiG8XSKUdnBnozBLiBd0XCSKFSF2ScYx0eZD4uhEGc4HUcfzt8LPoxshD3ol7j6XRiDLUYIbhH3RnU9GhExf309VU/IkmzkPkjtEE2Z7ac/YAGar+4Ywo8ARugSJC+b17VsSl2OmK+xiAMTIAxddM2SVog/nT0RO/8njHVMsgoeEEh9elFzIP0hQ9ZDdzNTnkGJWOJ7zGI8cCGNR1ChxnTHCQeoF2kJtmETrQhACieeYuT7smpzD4/HolNHMeCmisVn5tcbM8uHnuUMQykFHaU1wq4aA42DNJ+0DE0vKPWaIBOieLXfcuf0B/3rruvKHUEKbiH5NcYx76NCIZk3ILHnNe70HyaaoJ1ca4sO3uvh2QBYQtza/DG/NoYjQ3cZAAOykDhICalDnV4CHfTrGIz9ixOquJKCxKXUXSxaFYFJkLqGRKxS38RgcA9/n7uxHASTcF0Y0pw5u/Os7SJ1CaIDwrVCFUxijHJGNf/jGkTIdDCEgF8dyIBet3ZEpkmqHAzjx0VdsqXMPS3c37932JDtoAA67yFqlpKpzo8IEtH+YBtnE8P3bwFET5E3BiBj5ymRJ344mGvjuoJKQOehS7+o5KOp/phIhXjPVt/F7oRkNe/IwQFw9hhIZhIiAfTL6ZOb0HRHrskGeFLMVPatYgtgUAL5gfnpWRMKaSNpRBPx2qTLPMPUEG3FQ0s9NskqznugXtBmmzETU4NhevU1ut3mCc5IJYPqt3y6tS4qgzmVvSOIWXoEQJoycjMe0Myx1EP6mFHKJTz5i8JIEO8z7tWc+j8UL1RPWeAxzUclma6iis+z/RZLczP2xg+RReJN6NaUIwNy5t2mXt3l2dCZBmuZSwaK/L03WmhNGurHPEEElLqLrtOWPH+gAfYU4MxB0xudnRjW/ZmB8M86GzmcYkPMQU6SsaayFFiwAAU/dAvOCTJ8zDoRU2Sgw5oNx6NTow1fIjd1GPDyl8ea4bbpYhRDsHuqkG+8T+2261/GHjw4D5o3GPyvEU2BlRylxq2wwKxiG0G5xRHSLLT3JOTayMsG/W61NnXIZPhcetoxjJdyMw9M0gFIpCJ/BmqpL/2sFkQJIxPeylVk0S5THzPjWyyJLXainhtu9tWTEqe1cPdwZBwm3OR2u3E4ZrbJzvE+UYL/IfzOEth2GUUt0sRVVhHNc1WBHC4RyDre3z9pJRkItleRDLQ7BrNjKLpAbG2scvduol0k58PVUid8qFD0kTRHaJYCrhIeQI4K9tUt6NYjhG1es9IjwDYTUgzgD1IV/sr2QO02SO2zQUMxkl9LqdW/SzGPE6Gfjwm7bJetEO1wMSprGxFdxkmEwFe7mh4L99ua255Mb3p+Tm0lEpQPG37P+PfnTTD9ePwXD0lBu3LgYpJ3Ke+SZmI86F5WGOHaU4K30329LFQkU+f3LNXPJL0pRCxjCvDZdSIG7QAxAdu7lUMOsyLjo0EHIugtgIsmzMgK/V9EVuazdQCzYrK45v6PdauotA/HEDEntSHMDwGAQYnuIVVhuC0gQ9GQ5wkjGhgMJY5ZUnaJ4BP4wNQgTQb6h5u3ySx029itVB4D+vK/rE8H4oDB3ep6tzds1lS1z9AwEvNjn5pDRtkqE9j3e7M6LrT3pT7Kl8QaVr2E4xqJwRYJhdtSD+xlPzSOpaSVqI+mKLWP/JFQwwo0HSkKmuZ4fKIk3KlDE3Vb2LYvbG8Sw8UsNPiHbMJ1YUc2Pvz+dA7YTizFWY9MDYV5YoCscLl6Q/NdAml2Rnzg1yvCQHnI6VAvfjSfXiZZf7OxaUjmqM2qP7872lHaA55/G1p7Ix766zlsRnMY7c3+OLPqAEtfPGtzmIkXqqGt/s8n7FHiLOJ0Uu+POVfjMNB3sba1TEk9rgI3cka8ibbbWcVfbZTjIl0qbsQmgnn9jLsCI69Xutc9h1FNdnwFecY0wLLwWjrgseQ2fKjLtVZe7yzoi5xRtKeiOOojtGdcVo4E4FUfVu+iqau4V0J+TDpG8cZtrjapybYFMd9IS/YnP8A6w5LeutGH5mvKlTx3bcV7G24STJxv0pzbTOL/dLzJEWW/1Z7hlRYkxGoTK3TPhWZ7ccE1KEoZBp9SFlcVDS29+vkjtmxgLt78I317qOK8qocSTonV59Ld5d4lB2sYenzeSOg+2p6u0AmIM1KARTgHJN2KkLP8IL+hD6uq8ef3wLyRnUtPHFb9c1FzOFuHyV1eb824jIwsUBnYuE+MQV2cp88yvRhxJdwfViRHP7+zcL/Bjp2GB1FGiv4iS74b8s9m0N6ocHs86uKEp12y2xPhXiwRUc2cEOwXEKStWolLkHnY140WTv8Al1g7vJJJ4VfmjwwWcHBWpJxd2P/SiLDwY9Bp68IvLXjwC1krBKjHeLPYNqxbUCFKHAgiVkSwkND3kL4wsrP/M/Bj8C9Wd5jQ+LRU0Bo3dUEV0xtyAGQIVGs//sTWS+UBeIgvEBkygtHFOjzu3GoIv34zfJNsZN7GWzO9H/fiiPSAfVNfWvocF3bMQ27kqAjobPkFFI7XbWItvVgnpWX8BUjk6/xUYRA3bCG7hNb5YVTDUhHjF9N7EPH9r+8uS4xEvPGbnlvYKUXgO4/JC00/Rey/98jGgmi1A4hovxGOWK097FS8GmihVro5tReC9+LI2IW3BGhhst/6Tnq9apnu6J6fzXvpwgfTHL8gadenpplQ401fHfAtA5xFNVVKK4QHv6cnfBYUg5D40086W02LBLbaa3Za/VuTdu9Z3oT5ATHqt2+YCOCXKH+p2JBZ1OggtBHWOZl6J2k4fHn4gLr7SFHx+eSvZsgJgnq1u47oGsc4Q1Y26yPzc1QNATbceNjbfiSLwANyu0egLL9I3olKMMrXkqRP+7i0RaIvNI6aSmuco4w6uYwkL/+zt2n4EMQj9+YJOkaPTEbD5ugNbM9fOzYg5pnpjasVzCog/MYR0NONS0HlqeBtG87hcd6oKCT1LVeoRx8YeElA0By+0XObg5HCDwn963kwRvz//w4gqPnxhMvfRSssA1DQLEjrjxw9Ao6kUj0aGvvwI/PDT4soEWKrYmf4QcukFNtkhkCXmMi2fdF4MxtzCCHkMakF/2zpgoHdNGv+GB3M3zqIMYqq4Ddl8vqUMc1hU0IvugMSzRj4Q3VA6nXUN+YHivLfK75YUtX+VsDkUglTS95fZNkG4m5tdJ9MeqqWJgATMjbUpHhoP0bQUuiC4tpjb3t+voiJuFamH/IDTR4HSfZDxMVB7S4pTwxX4ODmZ7zdDax41sJGMINH2qRr6PCNF7bVm92PvKa+xtocNRdUwt0b594DxO03SFuQWALGDlQoW9t7MjBj13v3P8tyTNiZ/ENAKd8jXSj4xN9niq2UQ4aM4ch4XD62urekAMWIZIcQMufp3AmV/RCcU1+4JBrmFNQUeXkUD/nEEb3pndxMQ4VmzG71zEktPj/Wx3tBKnGgL9LHJ4W7K74hFd0GEx543QhMVBJc9oTK3VY5O7mlU1rjgv+GQO9IT8y959H7FaBu6jUIaR7A7yqXCHzN61gpZ6WumcR7JE/Bo0lbr/rENe2ZmZJeg9JXEqWmS771twQjSOmtZVmJO9QAzKeHSPJz1qmNRb/Dx8bqqpySfZjMSutfgoNZsD6294HUnY8D+c6uWcST3JHngiWS/C+4iN0YSmACI0itSGzle5U1c9Z+2/X4Pe8hoTk5NdI1PacOBwqhJfRHIxp8NfqYoQN9li/S+nvmOoN1MwVB8gPHafOawn2ho+1uQM6y64SIvmRGyd/vCo3yl5f/YZsuiYH4MNyd4R9ef0seglc28RFhhlDwFcdwG+5kCD3xOkE943HbvEkxjJBGdzbmo8IsTKdwMWzOWdCCDntKgTMsa8UsKBY46lHfZuEUWfQIYpWQBK9PcRcUUxJ51GaWBGN6I8hXSPti8QVK8HUuQ1sypIK8TC7/yWPcU/63PmNpJ/7uxrUUWwDviel627487uOX5Wvw1IajxPpIg2y+1tDz477rCySOcm0MlScH0cLMYGpOjfjwmAVpKZbhyNZf0j0v4bNBAAU3R538Dw+08z3VLGa9C02wkTViDeVp4j6woEt8tiAEPcDEY+P7XwBkzndUn4jDls8elYx9aJb5RyZ6xy9S4Ra4ZJ1YZLSgJgPeVOsYSTCw3jJgq3Jh4Lnba2aL8rO2D5TEp7cyGRPGcQaCpz5edU8+UBmrHv7e1Ol5KCcKmXKdGljZQTxKY2zs8hAOqFAl4jQC+IR13xir4GoYFSfrx+azzv4FtdAMQ9ZDSlKerE0l//+fSzpw1qD6S2OYqdpS/0782TlaQHPZRHusk6L6qRN3hbVDj357h8nPfpjZhigZjBgJq8CTEgYOR2o078h9I2b7tjdipEoa5mvhQJLeW2EQe13h24XsD5OJ+GKTZVCJ/azGXTJZAEHctYjX4Fx5Ol3Rb+FVavHRfvwh1uYv4olT44XPCmFxU2P4L0EsP7DBAFVDF7NNMCky4PXjdI6Zne35coqET0s+Uwe6zJ71hwHToKt3Eyw92enZI0dnDyz0cPVIr50paief0s7s4Zu79ebjmLcfyoNrF6KtKrk3rLOM9e6zLj3+suCHIMSIu3t7cIIA5kGd8W81t/G7T7J4qMg1u0CDuFzwx9mYUihciQPcEmcf1DdH1kCzEZi5smCi84gIwoHXW4CS4hM0B+iaFdI24DOoynaYnlkF4ZNc74M3bJrWXvyrdO3tPRQ269HtdlAECBvWTj6VDJFiqFmKZ5iE7PvASvyHsdrWFGPGw6+x0X57wEQC67uSC77eMIhl72SC+B6AeQXkHOvXKaQtDnegkWtYToKV3KxPrtig3r6Y/zE5MSvb+LIFQ0EheNACR/c2DmSofTyNTNVyoKc9YxXb91FUw1BIrSv5Msb8J3tMqgJBaeN161ikS19In/G4EqmJle5SLNBDC97q60LEeSgl+U9e+MwQwpmHUNbPWnpHIC1uElH1me+ug1fuszQIB3DPQRwO9e7q1OPOeQBJeV2TaBkS6lEL8qQGhpMXA1+r7AUktCnO3g01kMaZtCL4x4Zo/dELX0kYaaUVdItK6DAwqAEwGC4BSak2lPfHFPwqbeddr1jNcqJEUKYpUCNC6/hCp+ay4+sjCZubyE7X671/AvhYn8mS4/jQJnD8tRzRESwgrr7nSq8EiAnlVCxJWvMzesMHQ3VYNy+36j+BPqdWa/uZvRkKHl7ZqR4TTVqVJH5yM/yoVoULYl5b1m3lBsIFX23g+PaRqU+MGfkRtw/JJjOn9hUpBlU01Ah1utAUpwNd3XZlQ3eYDJFW/KWkLCRKdWQ5OaCKNPJ8922Ujt1lwkSQbsA4knsuTcgJlb58iNNObYxaCXlM8eoisGVbPTSw/+CP+N5F73BpmiOhoRbuBh6eCHqWnlxZLEn/O1y/T32knvGw77KSdLy1v1xoj90F6XUB4nJtOCmARx9IbCD8kmmakwe1evtBen+6S5bTA3k7E0RmTQtN0Th6siLdGwgKP4dx2CY6RTtI+UVUyg0HbWj0gwIKaN9wkFOczn2Cr7catMDdA1gaz/Q6OR3qFf2UOrkBzJia7E2UdxiMNU6bZYfMVCfZg9+mi3vSdQUyxGX27B1dlK5+4GBmtp6WbFiz4UIdli5pMnnSiBO18k74m/PxlpJZoQ9/633jELXt7Fsv6Z9W+NJ7lJIt4byntVIq4Akpn8M7+iz6TCJiZhNNwDiIexcIlnJral8JaE1zYbzqlNW1O0o2LoLS3iE+aodTepurEVM0ONrrGuOmjY+dHjzHXo00Kawk0KaoV/r7sQZ7XenpYpDMFK1xjcR9h0pHAZAeS/4HhNbnUS9RZcqKiGzt87gEWU7YbUXlENAqqPTcyujjUbekubc96G5ju7zQN8GFcV6HLjDHt4Jo5SZBzHSHRkOO3V8n/UZ8L6o068eEZFoR148b6/SUKYuD/DVsp1Eg1BTinWvwd6DwCnn4mArln3PNY2dbcqTf1LG8Isw05NDLOvUDCpuzxR42MERMnRygllSi7rrfWVSOs3lencsRM/4nvYiUv3ra1A/3eG5U+RxLeitus9LPeWKDljEweMbFFSaEsSaHBQidJTXLepAtNegWh8S9w7402pvHoJFg4IuFok5oddSZJl7FpBFmKi205w7Lw/v1vB74JqCufB30pElwTHAB9W4xrKifhmVkuFP92mD+j0TnZE7C2PJXbx6pSaBsACz7LTE1FqOIlZu8p3KAcRxGnrUnBU9R9jq48U7zP59MiJhvAxicL7w8V15enizPsUKEIlPzQ7i/g4EDO9xii47UwpTkFtk/Qmmk07ktwPdcjoT+TpQMrx/lNYX+Le9T02ro+JOpAfeoTC6DsyIMWa+O6wcxYrn3D11DyP3xm+HEt00JWaPtTi5+DGxqoh4xXXvLTJE2fxst4b+6fI0PC6N3ctfjGlFBCpVDvBw7cyt0d92PEZlweIF2vzPlpfCeGKlrlZrhCtDWiVl3AAlBLpyruugtM3WxPyGbiBsEc4aHPhad7VMeB3x4HfElFwY2Gh+kNvi9AasNmYRdg/dC/vuLYgAvVX2w8w/j0Asa8VhfrBVJ+93vX4IS2CcW7WZ2MU3bgddtqAAa8bit55PWzMmCpcKEHBLzFRN68ILwMmqGPaeZRsj3BoZiqoKG8PN7YFFgM9fCGDhMEXarl1xaTqpxuUuWgvF3gLzkR6RfInK82AJZ28MZddWISANV0D0pu/mLkUJ6pSIiDAwXeKT2UV6vZtZs06x1P+Izo/esThe6ubehkDNe3ZdXhSsIHVbMTfhw0fOvz9IJXGS0y1KsC3rtHPUxbXYTtTEAp8G1Zq8ztSyT9jKEUIt/KkqHy1KqYoFw1hApAgNBcdXJV9jsGPpDhMo4GKiyf+f0dQH8pKkW6+7xTIM6kNIPBgPH/Be1TNAvoUiQ2lvmknldNCSLmhnWEw6Fz5hFMO+OF08vCVIBCGfDBa+R6mjQe8w6+SCDyINboxJxbqwXFkNmQ71S7OcJ4cmWJLfmdJVjvOAMY6XfBOlnERSva+9QT25EGjvJi4OKsu9Xa8WwitjjeTfPdVC8MCUUAGyzL9NptRBDeOYIULqllU6Uaa1ZmNfJiD5A1Gmb8aX4IB0CBYiuXIi6JI/hqXfFv2hQdmKrSPeYSsXkZQgTrimYUffoY2AgQ2arR9Cr1Av5eK+5XbaPWDjqwsRTTzcHKEwYJmT7/t5hB1rZZjK2mXMKJoNOam8fvUeKyDMqqyEiQOVQ9UJpm4ZuI0dRWXAT8CTyWbGe8I9UBl4Mn6BGLhxrjnxiWZJowLhiS315JEgm869rw5xzROcdXI6jDaDzqYKjUo6rd0T6kud0gmUT1JaiZdh/2RTlsTMpqwCnxm3/Arm2Ab28PhG8+W+MJUrq4q7XRBTJogs9k+omGrz0dpRPX4fcThIkJqQXtJQEroRK+ZC+6ygpvuZGemt1QXUsYqTSrBkknNZsCgvY9MAobhSc0SZ+m+J2SeWZSh4RMZtn1PvQRIW+cbK72GuTvyqhphgfyM6D/ZuyiHNU5MMORZ+3ugARAZGgm5Oc9RHeOqc+zveGwRC5mok20QhfjPImjBm770ABvqW2vkAjHsllYN7mqL7qk9ZYztPc2As06E2Nd7HtFaSFMp0z4FbV96XJLuTEBhvQ3djB3pLUOuDs0cl432wESfjYPcMNljRDB5Z5YB1WkzP2uLgSP+RyyBn4KjU9a8J+VKbqiXpyXnQL445j5HwZmN97eXhQdKu+WGSPY5LDFonaigAQSNHNOQpEs0G+xf2pEoNUzLx0HX5wJLrQIzf7oPAUN87gD2z6cZa/9+fuGsOj9ympXnAwVTuxZonZdAirHMIZPU0RhkGNMvJTcO4f9PMp/2Lj55pB9TTor4ZEPWOqEknVjLm4EBK2pmD2OXqlSc8wzcaAFZi3N/anMlxQ3IZ51mtv0QLukJIPLhx/3BiuwYnseFSZwLs7hjVEUntSkIDLgM8rL0//LVMyiRc64HfPa8RYQIavVeqJsGXrd+r9j1REdTtLZB+pfSsJl1rb9+y83LxQeH5GBpqvkEhA5PpsJt5PVMS9zLpG73XOqxI43Pxa3qhFbonrLlceuZyL+44HrjAOFXBb4Y4d6ZFfrN5PFq4Xkd7IJqRwg/zGD0oAw9rxaNmrGwEbbtPbq/NGB4B6Tg2wmXEQV5t5WmioaA3R91y7Kp2aIZ1Bm8rj8vxrQzvpUhwaotj6k4+ppC5BwmAgE0jX21C0zzsW56Vo2mKf6fPe1dHY6Em0/0hSa7S8/unAbj06DQ/A9ykCHLHCx+U5/pySMM/LB0+5IGIw5/TOLNlSOztz/GovwLJBpIOozCsTSJsMY8HMnBbGwhn9nnYEaiFuMkTfEG6dArJQIkuug+Vxh+UCZnHNKr/hhFcj8OKfhJxZK+OQrpPw2udeAhyekBSLIp1tm/hOUOtio9529p8EiSAXhJkpHCJzB1eWunancL/JIciDrfGJ4OgfoiaNejiBe96CGMjANTPwMgE7+YhkWwMg7WocKCTL27X/BWripTBJXnGaAqiS8VN6TDiit1s+iK6dglbwKEmdWc9AW9BnkhR+jb1uLapzPkqFt/WX5nAGQmI8wIb9OUiIMnzolpM1ETo/HJoRH8pnWc9qKiwc0++xuiebfMptw4wkR18LuJgvPT04WMD9a0XiEFpccgzF8nSuvoiPecpym7Uo+dY4SJ10Lbt+evHUUyzoLNCTKCnKmxwfhJn3saDYv8y0Tb64QhDRaQDcOgcj4BdofvsWpGuQXBWSKicJ+fN5MGzPg6oTbU/1jNgY4+7lJezH1PKBpZsh9JfKfnhV72+BDqZeTZcVIWlXU9GXSTPiJUbxerT+S5qYK68+LKqwEGvcxjylzM/zUj364kdCiH6N+mhxyHm0in41tK4gfEYfs1EKqWjEtsyzdDOZFbWzc+TLQnnZanyCECosIhpBjppeGHUvWihHJQqxGV9NknXiOqfPfnua7LAEmmilnDFSeOiuuEWi8fdOkXH6nb2RU4NH/9O7M8QiTwI+AEgkdKe2Kcat+GTYo2GeV5tgOcr1aGp8iS+ZuzWQlEXigAR23uIp6gwIVRyquiGSL8mj8VNvE2ng/9LzBSlrra4O3bRKMHKUmMOr+vOmByORhn0H+eTOBYb2s0dp9izFbRsZleKNZo3528pM0UG5WpRG0ZPd4CZzDEhXx3UVs4pLrAUbk8DMaTc+2G5il8rsu2DT3UaY1KVgeIwc1o5Uq3AWH6qXWTdXdNfpWQbSYZ7oJ32iaL7Okh6VzPJi2T3me5n63CVhnA6M8EV4iKCxHDeKs4R+2CKyNkUPERqCzk2tkJdxb9JUMnvAb7wO0rtg07Wui44M8H61rp+38FcIZrxxjBOA6VVtY2XlMBebEWALAbFF/V7apqVRswD9m3iH8n+0Wynb8qVSeub562ArzWK/HYoCZLhL6UFNxZmDwZt1B+LIe/AqGV0vLzO4x0Qz+8g8HSPbEAxFDjt71vQmDuyamNEQ9i263W8EGgVD+DHVdGezBg440tb+UFgRJHcCTeauYMCepdON6/6+nYxpA2ZIjt59q4CA/FXskAz5PRVQ4YKhUVdK+fj6sXs8mnGWK8oZiLUycPoPh8TkGWyfS8Rj2YHXJke83OUTfU8hYBuLfKoRAEcNw81x/oZwAcHuVZI8V60W2bYhPY5bOPzTK+pXHQX1nmAdj/aqOpm9uPTnqaVa+iBB8Fs7/BV4ENpY6OzUdSRCR6BLcQhE45RAjuKnfx26fbNV+BDz1HyvrXVmxrO0I6Sxr9Y8KAd9HvZ+Ga5Dk9DxFFO1K+RNVQ8e8zjMCa2OCG4ZG02dmHz45wrp7Qh5OliGaSjWYnt6UiSpwfWv0/qjoa69lNAXL9UqOb2jmv2WY78LiMBY8io0gJkEzIzzyprR97S3fcZXO7XJIAs2L4oz/EnJQ05JoID0h4CY4e1TSjKqVMyUOwTZOC7U4fhcMgGRGM46EsqAr+XSqQtqXsuXnQ4PnVlv7K31O4XUd9VXhQlyK4bT/uTnQ6PF30OOhjt/pg8YNG7pZotI80lFSRZ/d0Bihno4Hse15oPrnjgYp5krnZy36iHDPX0oAoQNQyxrpYsUOb1grr4Ev1HtEHMP2ZbE0JluQvLVXYHv0pfgDdQJdjpg1YXujyWw+KexhFYcDe0DjuB/XpfSRYsQS1FBXiLtdbdTU+9lCCKpanFOA6LgX5vjcmKOOsZhzLy+VeRc3/V1Ez/s2CfjiG3xLwu0IK0vEXKcetwFPrPz96H2akevHcmV09Iac9nCeJyPE0tl4Io6oou+G7PnUJPuCd6w7LdwT60qrZj85pw7m6rzb2UgPoD1g9QUfOZtDFXm4OOZx5kD4ztPn8Gj55Wy4ROUlX0aaj0xDBTO0XzdD1PUUv+2TCMCr7JRTDZHfdDl7Je+Urg5A7c4noh78Q27QEouBiC32pHPoQmH3Q/Bjoj9Kdhg==
        - #2:
          - type: tool-call
          - toolCallId: Sg9PYHlTM6nZFSxF
          - toolName: set-policy
          - input:
            - Rationale: Adopting Creative Expression next to boost culture and golden age points from our cultural buildings, strengthening our culture defense against India's tourism.
            - Policy: Creative Expression
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: y4CBcL99uGSn6sWa
          - toolName: set-relationship
          - input:
            - Public: 50
            - TargetID: 0
            - Rationale: Improving relations with Egypt to facilitate peace and potentially form a Freedom-aligned coalition against the runaway leader India.
            - Private: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: Um0ee9QHZcmExyja
          - toolName: set-relationship
          - input:
            - Rationale: Easing tensions with Denmark to prevent a two-front war and align our interests against the common threat of India's dominance.
            - Private: 50
            - Public: 50
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: aN27RLAgcAM8G6ZC
          - toolName: set-persona
          - input:
            - FriendlyBias: 8
            - Rationale: Adjusting personality to be more forgiving, friendly, and cooperative with other civs, allowing us to build an anti-India coalition and make peace on our current war fronts.
            - WorkWithWillingness: 10
            - HostileBias: 4
            - Meanness: 4
            - Forgiveness: 8
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: lV82U6fFCk0tuwfS
          - toolName: set-flavors
          - input:
            - Flavors:
              - Diplomacy: 80
              - Science: 80
              - Offense: 90
              - UseNuke: 100
              - Culture: 80
              - Nuke: 100
              - Mobilization: 90
              - Gold: 80
            - Rationale: Prioritizing Science and Culture to build culture defense and catch up technologically, along with Diplomacy and Gold to contest India's city-state alliances and fund our military.
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: NW9eH4Mgr2bfUvhz
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
          - toolCallId: Sg9PYHlTM6nZFSxF
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: y4CBcL99uGSn6sWa
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: Um0ee9QHZcmExyja
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: aN27RLAgcAM8G6ZC
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: lV82U6fFCk0tuwfS
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.