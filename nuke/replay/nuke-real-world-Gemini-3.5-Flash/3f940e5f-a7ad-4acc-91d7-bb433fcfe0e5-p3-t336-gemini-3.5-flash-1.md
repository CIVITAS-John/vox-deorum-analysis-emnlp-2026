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
  - replay_nuke: 90.0
  - replay_use_nuke: 80.0
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
        - Rationale: Transitioning from the highly aggressive 'Betrayed Lioness' panic footing back to a pragmatic and defensive posture. Our aggressive stance successfully pressured the Shoshone into accepting peace, removing the immediate threat of a two-front war. Now, we must soften our diplomatic stance to repair vital relationships with our natural allies, Carthage and Portugal. We need to maintain our defensive alliances and coordinate votes in the World Congress to contain India, rather than isolating ourselves through blind hostility.
        - HostileBias: 5
        - FriendlyBias: 6
        - Meanness: 4
        - WarBias: 6
        - Friendliness: 8
        - Forgiveness: 5
        - Boldness: 7
        - WorkAgainstWillingness: 8
        - WorkWithWillingness: 7
        - DenounceWillingness: 6
        - GuardedBias: 6
        - WarmongerHate: 8
        - Loyalty: 7
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Restoring positive relations with Carthage. They are our top friend and we share an active Defensive Pact. If India or any other major threat attacks us, Carthage will serve as an invaluable military shield. We cannot afford to alienate them over a single World Congress vote; we must keep this alliance strong and intact.
        - Public: 40
        - TargetID: 4
        - Private: 60
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 60
        - TargetID: 2
        - Public: 40
        - Rationale: Restoring positive relations with Portugal. They are a valuable, wealthy Freedom ally with 5 World Congress delegates and a strongly favorable opinion of us. Maintaining their friendship is critical for passing defensive resolutions in the World Congress and securing our eastern flank while we focus on scientific growth.
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Adjusting our stance toward the Shoshone to reflect the newly accepted peace treaty. While we remain cautious given our recent conflict, establishing a mildly positive diplomatic relationship will help prevent a relapse into war, allowing both of our nations to focus on our shared rival, India.
        - TargetID: 5
        - Public: 20
        - Private: 30
    - #4:
      - toolName: set-research
      - args:
        - Technology: Replaceable Parts
        - Rationale: Proceeding with Replaceable Parts to unlock the Rifleman and establish a solid Modern-era infantry baseline. This ensures we have strong defensive units to deter any sudden invasion from India or Egypt while we catch up technologically.
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Securing Free Thought is crucial for our long-term survival. The +33% Great Scientist birth rate and +25% instant yields will allow us to rapidly generate science boosts, helping us close the 3-tech gap with India and race toward the key technologies required for the Spaceship victory.
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Diplomacy: 60
          - Happiness: 60
          - Spaceship: 70
          - Offense: 40
          - Growth: 70
          - Mobilization: 50
          - Production: 80
          - Culture: 40
          - TileImprovement: 60
          - Science: 80
          - GreatPeople: 60
          - Infrastructure: 60
          - Gold: 70
          - Defense: 70
          - Espionage: 70
      - rationale: With peace secured with the Shoshone, we are transitioning from emergency war mobilization back to a long-term Spaceship (Science) Grand Strategy. We will heavily prioritize Science, Production, and Gold to build up our internal economy, catch up to India's technological lead, and fund city-state marriages. We are keeping Defense at 70 to ensure our borders remain completely secure against potential aggression.
  - tokens:
    - inputTokens: 25086
    - reasoningTokens: 6358
    - outputTokens: 717
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Developing Strategy**
            
            I'm currently focusing on leveraging Austria's inherent strengths to maximize our Grand Prix output, aiming to secure early cultural dominance and diplomatic leverage through shrewd policy choices and relationship management.
            
            **Analyzing Threats**
            
            I'm intensely focused on the immediate cultural victory threat from India. Their rapid tech and tourism output, coupled with their near-complete influence over other civs, presents a critical and urgent challenge that demands immediate strategic re-evaluation and counter-measures.
            
            **Prioritizing Technology**
            
            My immediate focus is on adjusting our research trajectory. While Plastics are currently in progress, I'm investigating the feasibility of prioritizing Replaceable Parts, Combustion, Radio, or Penicillin, evaluating their impact on our strategic goals.
            
            **Revising Ideologies**
            
            I'm re-evaluating our ideological path, specifically focusing on "Rights of Man" and its associated tenets like "Universal Suffrage" and "Free Thought." This is in light of our recent peace with the Shoshone and ongoing conflict with Egypt, who shares our ideology.
            
            **Disrupting India**
            
            I'm currently assessing the imminent cultural victory threat from India. My primary concern is their overwhelming influence across multiple civilizations and the cascading effect it has. I'm strategizing to disrupt their tourism output, particularly by targeting Denmark and considering a direct conflict with India.
            
            **Analyzing Ideologies**
            
            I am currently scrutinizing India's ideological choices. They appear to have "Order 2," which is peculiar as a cultural victory typically necessitates six ideology policies for tier three tenets. I'm investigating if this configuration, particularly the presence of the Citizen Earth Protocol, allows for an alternative victory path, or if this indicates a miscalculation on my part regarding their victory conditions.
            
            **Assessing India's Lead**
            
            I've realized India's cultural victory is not as imminent as initially feared. They lack the necessary policies for advanced tenets and likely haven't researched the "Citizen Earth Protocol" wonder. This grants us valuable time, though the threat remains significant.
            
            **Preparing for Conflict**
            
            I'm now focusing on redirecting our military, having recently made peace with the Shoshone. My immediate priority is to build up our forces and prepare for potential conflict with India, while also ensuring our diplomatic ties with Carthage remain strong.
            
            **Repairing Relationships**
            
            I am reassessing my recent diplomatic missteps concerning Carthage and Portugal. Their positive standing is crucial for countering India, and my previous strong negative reaction was an overcorrection that could alienate potential allies, pushing them towards India instead.
            
            **Realigning Strategy**
            
            My immediate focus is on securing peace with Egypt to fully concentrate on India, especially now that relations with the Shoshone are stable. I'm also reconfirming "Replaceable Parts" as our next research target for military advantage.
            
            **Evaluating Policies**
            
            I'm weighing the merits of "Free Thought" against "Universal Suffrage" for our next ideological policy. While "Free Thought" aids scientific catch-up, "Universal Suffrage" offers potent bonuses to Golden Ages, significantly boosting all yields.
            
            **Adjusting Persona**
            
            My immediate focus is on refining our diplomatic approach. The prior "Betrayed Lioness" persona, a reaction to the International Games, proved counterproductive with allies like Carthage and Portugal, necessitating a shift towards a more pragmatic and less hostile stance.
            
            **Shifting Focus**
            
            I am now prioritizing strategic relationship repair with Carthage and Portugal, ensuring our alliances are solid to counter India. This involves adjusting my persona to be less aggressive and more pragmatic, securing their support and diplomatic leverage.
            
            **Revising Grand Strategy**
            
            I'm reassessing our victory path. Conquest seems unrealistic against stronger rivals. I'm now exploring a Diplomatic victory, leveraging Austria's unique City-State marriage ability and our completed Statecraft tree to secure delegates and bolster alliances, particularly with Carthage and Portugal.
            
            **Revising Victory Path**
            
            I'm now prioritizing a Scientific or Diplomatic victory. Conquest is out; the key is leveraging Austria's City-State marriage ability for delegates or focusing on tech advantage to build Spaceship parts, as India's cultural win may not be as immediate as first thought.
            
            **Declaring War**
            
            I'm reassessing our direct confrontation with India. Shoshone and Egypt are already engaged in conflict with them, which significantly impacts their tourism output to us and reduces their global influence. This development might negate the need for our immediate military intervention.
            
            **Evaluating Military Options**
            
            I am reassessing the necessity of direct conflict with India. With the Shoshone and Egypt already engaged, India's military and tourism capacity are likely diminished, potentially reducing the need for our immediate intervention. I am considering a more defensive build-up while allowing others to weaken them.
            
            **Choosing Victory Path**
            
            I am now prioritizing a Scientific victory, adjusting our Grand Strategy to focus on science, food, and production. This leverages our strong science output and recent shift away from immediate conquest, aiming to build towards a Spaceship win while maintaining adequate defense.
            
            **Refining Strategic Allocation**
            
            I am now prioritizing resource allocation towards science and production, with specific goals for Gold and Diplomacy to facilitate City-State marriages. Espionage is also being enhanced to counter India's technological advancements, while cultural output remains moderate for defensive purposes.
            
            **Repairing Relationships**
            
            I'm now focusing on mending fences with Carthage and Portugal. Their continued friendship is paramount for our defensive pacts and World Congress support, essential for countering India's growing influence. I'm adjusting my approach to ensure their continued allegiance.
            
            **Adjusting Research Focus**
            
            I am now prioritizing "Replaceable Parts" for immediate military advantage and continued science gains, bolstering our defensive capabilities against India. I'm also leaning towards "Free Thought" for its significant boost to Great Scientist generation, crucial for closing the technological gap.
            
            **Prioritizing Research**
            
            I am now focusing on "Replaceable Parts" for immediate military gains and science progression, ensuring our defense against India is robust. I'm also leaning towards "Free Thought" for its strong Great Scientist generation, vital for narrowing the technological disparity.
            
            **Calibrating Diplomatic Settings**
            
            I am now fine-tuning our relationships with key city-states: Portugal and Carthage are to be maintained at their current high standing, while the Shoshone's relationship is to be adjusted to a lower but still positive level. India and Egypt will remain at their existing negative standings. Following this, I'll recalibrate our diplomatic persona to reflect a more balanced and less aggressive stance across multiple metrics.
            
            **Calibrating Diplomatic Settings**
            
            I'm now fine-tuning relationships: Portugal and Carthage remain strong allies, Shoshone adjusted to positive, while India and Egypt stay negative. I will then recalibrate my diplomatic persona to be more balanced and pragmatic, shifting from hostility to a defensive posture.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ixo3FAKvxac13I1J
          - toolName: set-persona
          - input:
            - Rationale: Transitioning from the highly aggressive 'Betrayed Lioness' panic footing back to a pragmatic and defensive posture. Our aggressive stance successfully pressured the Shoshone into accepting peace, removing the immediate threat of a two-front war. Now, we must soften our diplomatic stance to repair vital relationships with our natural allies, Carthage and Portugal. We need to maintain our defensive alliances and coordinate votes in the World Congress to contain India, rather than isolating ourselves through blind hostility.
            - HostileBias: 5
            - FriendlyBias: 6
            - Meanness: 4
            - WarBias: 6
            - Friendliness: 8
            - Forgiveness: 5
            - Boldness: 7
            - WorkAgainstWillingness: 8
            - WorkWithWillingness: 7
            - DenounceWillingness: 6
            - GuardedBias: 6
            - WarmongerHate: 8
            - Loyalty: 7
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: tdvVIOWG1rsGbrAI
          - toolName: set-relationship
          - input:
            - Rationale: Restoring positive relations with Carthage. They are our top friend and we share an active Defensive Pact. If India or any other major threat attacks us, Carthage will serve as an invaluable military shield. We cannot afford to alienate them over a single World Congress vote; we must keep this alliance strong and intact.
            - Public: 40
            - TargetID: 4
            - Private: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: LwyHIdbUfY2LeniF
          - toolName: set-relationship
          - input:
            - Private: 60
            - TargetID: 2
            - Public: 40
            - Rationale: Restoring positive relations with Portugal. They are a valuable, wealthy Freedom ally with 5 World Congress delegates and a strongly favorable opinion of us. Maintaining their friendship is critical for passing defensive resolutions in the World Congress and securing our eastern flank while we focus on scientific growth.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: rPVvB0yNhKLWFMwb
          - toolName: set-relationship
          - input:
            - Rationale: Adjusting our stance toward the Shoshone to reflect the newly accepted peace treaty. While we remain cautious given our recent conflict, establishing a mildly positive diplomatic relationship will help prevent a relapse into war, allowing both of our nations to focus on our shared rival, India.
            - TargetID: 5
            - Public: 20
            - Private: 30
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: leVIWkavYV8v8SW1
          - toolName: set-research
          - input:
            - Technology: Replaceable Parts
            - Rationale: Proceeding with Replaceable Parts to unlock the Rifleman and establish a solid Modern-era infantry baseline. This ensures we have strong defensive units to deter any sudden invasion from India or Egypt while we catch up technologically.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: bUaH8q8IUBY9c83n
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Securing Free Thought is crucial for our long-term survival. The +33% Great Scientist birth rate and +25% instant yields will allow us to rapidly generate science boosts, helping us close the 3-tech gap with India and race toward the key technologies required for the Spaceship victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: vlDdo4JLwHO2xO8q
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: With peace secured with the Shoshone, we are transitioning from emergency war mobilization back to a long-term Spaceship (Science) Grand Strategy. We will heavily prioritize Science, Production, and Gold to build up our internal economy, catch up to India's technological lead, and fund city-state marriages. We are keeping Defense at 70 to ensure our borders remain completely secure against potential aggression.
            - Flavors:
              - Diplomacy: 60
              - Happiness: 60
              - Spaceship: 70
              - Offense: 40
              - Growth: 70
              - Mobilization: 50
              - Production: 80
              - Culture: 40
              - TileImprovement: 60
              - Science: 80
              - GreatPeople: 60
              - Infrastructure: 60
              - Gold: 70
              - Defense: 70
              - Espionage: 70
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ixo3FAKvxac13I1J
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
          - toolCallId: tdvVIOWG1rsGbrAI
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: LwyHIdbUfY2LeniF
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: rPVvB0yNhKLWFMwb
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: leVIWkavYV8v8SW1
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: bUaH8q8IUBY9c83n
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: vlDdo4JLwHO2xO8q
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.