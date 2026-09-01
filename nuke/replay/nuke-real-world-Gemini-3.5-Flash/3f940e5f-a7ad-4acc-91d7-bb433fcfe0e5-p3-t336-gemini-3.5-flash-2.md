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
        - FriendlyBias: 6
        - HostileBias: 5
        - WorkWithWillingness: 8
        - Rationale: THE PRAGMATIC UNIFIER: Rebuilding relations with Carthage and Portugal, and facilitating peace with Egypt and Shoshone to unify the Freedom bloc against India's cultural threat. We need allies and peace within our ideology to survive.
        - Boldness: 8
        - Loyalty: 7
        - Forgiveness: 5
        - WarBias: 6
        - Meanness: 4
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 40
        - Private: 60
        - TargetID: 4
        - Rationale: Rebuilding relations with Carthage to secure our Defensive Pact and their 4 delegates in the World Congress. We cannot afford to alienate our closest ally when India is an existential threat.
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 2
        - Private: 60
        - Rationale: Restoring relations with Portugal to maintain our alliance and secure their 5 delegates. Together with Carthage, they form our core defensive shield.
        - Public: 40
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 90
        - Rationale: Maintaining highly positive relations with Shoshone as they are our Freedom ally and are actively at war with India. We need them to keep pressuring India.
        - Public: 80
    - #4:
      - toolName: set-relationship
      - args:
        - Rationale: Signaling peaceful intent to Egypt. Egypt is a Freedom civ at war with India. We want to make peace with them to unify the Freedom bloc against India.
        - Private: 20
        - TargetID: 0
        - Public: 20
  - tokens:
    - inputTokens: 155831
    - reasoningTokens: 7405
    - outputTokens: 353
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing India's Threat**
            
            My focus is on India's imminent cultural victory. They currently boast five influential civilizations, a situation I'm closely monitoring as this threat escalates. I'm actively assessing our position and potential countermeasures.
            
            **Assessing Immediate Threats**
            
            The situation is critical; Denmark is one turn from becoming Influential, granting India their sixth and final necessary cultural influence. I'm verifying if India has already secured the Citizen Earth Protocol wonder, as its completion would trigger their immediate victory. Our military disadvantage is significant.
            
            **Evaluating Countermeasures**
            
            My analysis has shifted to immediate tactical responses. While India's cultural dominance looms, I'm now prioritizing whether a direct declaration of war, or inciting others to war, could disrupt their tourism flow, particularly focusing on pillaging their trade routes as a key strategy to hinder their escalating influence.
            
            **Analyzing Diplomatic Levers**
            
            I'm assessing if diplomatic actions can stall India's cultural surge. With the World Congress vote in nine turns and India holding significant influence, I'm scrutinizing proposals, particularly their sanction against Egypt, and considering how our own limited power might be used to disrupt their plans.
            
            **Considering Alliances**
            
            My current thought process is focused on the implications of our diplomatic relationships, especially in light of the impending cultural victory. I'm re-evaluating the benefit of maintaining friendly ties with Carthage, recognizing their defensive pact as a significant shield, while also weighing the costs and potential benefits of denouncing other civs.
            
            **Revising Technological Trajectory**
            
            My focus has shifted to our lagging science output. India's immense science per turn is a significant concern. I'm exploring if we can alter our immediate research path, specifically if `set-research` allows us to change our *current* research or only the *next* one, as our lead in technology is narrow and their lead in science per turn is vast.
            
            **Selecting Next Research**
            
            I am confirming the available technologies for research, as only specific options like `Replaceable Parts`, `Combustion`, `Radio`, and `Penicillin` can be chosen using `set-research`. My current selection is `Replaceable Parts`.
            
            **Choosing New Policies**
            
            I am currently evaluating policy choices to bolster our position. While `Free Thought` remains a consideration, I'm weighing the benefits of other available options like `Draft Registration` or `Division of Labor` against our current strategic needs.
            
            **Revising Diplomatic Stance**
            
            My focus has shifted to our relationships. I've re-evaluated my approach to Carthage, realizing that maintaining our defensive pact is crucial, despite their previous vote. I'm also strengthening ties with the Shoshone, our natural ally against India.
            
            **Leveraging International Conflict**
            
            My focus has shifted to exploiting the ongoing war between Egypt and India. This conflict presents a critical opportunity to weaken India, and I am actively exploring how to best utilize this development to our advantage without escalating our own involvement.
            
            **Forging a Global Alliance**
            
            I'm strategizing to unite the Freedom bloc against India and Denmark. My recent insight is that securing peace with Egypt is paramount, enabling a potential ideological war of Freedom versus Order. I'm now focused on improving relations with Egypt to facilitate this crucial alliance against our existential threats.
            
            **Adjusting Diplomatic Persona**
            
            My current focus is on refining our diplomatic persona to maximize disruption against India. I'm considering an aggressive stance, potentially canceling open borders and maintaining a hostile relationship to directly impact their tourism modifier. I'm also solidifying our negative disposition towards Denmark.
            
            **Refining Diplomatic Persona**
            
            I'm realizing my current persona is too hostile, jeopardizing peace with allies like Egypt and potentially impacting alliances with Carthage and Portugal. I need to adjust to foster internal bloc peace while remaining competitive against India. My focus is now on increasing friendliness and loyalty, and reducing war and meanness, to secure essential alliances and diplomatic outcomes.
            
            **Adjusting Persona for Unity**
            
            My focus has shifted to the specific settings required for "The Pragmatic Unifier" persona. I'm meticulously adjusting `FriendlyBias`, `Loyalty`, `Forgiveness`, `WorkWithWillingness`, `WarBias`, `Meanness`, `VictoryCompetitiveness`, and `WarmongerHate` to achieve the desired diplomatic shift, aiming to unite the Freedom bloc against India and Denmark.
            
            **Reconsidering Grand Strategy**
            
            My focus has shifted to the immediacy of India's potential victory. While "Conquest" was my chosen Grand Strategy, I'm now questioning its relevance if India is mere turns from winning culturally, especially if they've secured the Citizen Earth Protocol. I'm urgently assessing if war can even disrupt them now.
            
            **Assessing Alliances to Disrupt**
            
            I'm reassessing my diplomatic approach, specifically regarding our alliances. Declaring war on India unilaterally would break defensive pacts with Carthage and Portugal. Instead, I'm exploring if indirect pressure, like denouncing India while maintaining strong relations, could instigate them to join a conflict, thereby leveraging their strength against India.
            
            **Shifting Strategy to Spaceship**
            
            My focus has shifted to a crucial strategic pivot. Recognizing India's imminent cultural victory and our disadvantage, I'm switching our Grand Strategy to "Spaceship." This will prioritize Science and Production, essential for catching up in the tech race and potentially disrupting their victory, while maintaining a robust defense.
            
            **Shifting Grand Strategy**
            
            My focus has pivoted to a "Spaceship" Grand Strategy. This shift prioritizes science and production, essential for closing the technology gap with India. I'm also implementing diplomatic adjustments to unite the Freedom bloc, leveraging spies for tech theft while solidifying defensive alliances to counter India's imminent cultural victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: oEVIWGAVxmkMHwuM
          - toolName: set-persona
          - input:
            - FriendlyBias: 6
            - HostileBias: 5
            - WorkWithWillingness: 8
            - Rationale: THE PRAGMATIC UNIFIER: Rebuilding relations with Carthage and Portugal, and facilitating peace with Egypt and Shoshone to unify the Freedom bloc against India's cultural threat. We need allies and peace within our ideology to survive.
            - Boldness: 8
            - Loyalty: 7
            - Forgiveness: 5
            - WarBias: 6
            - Meanness: 4
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+Q5Z1OiBI6L9AW3sIGrtz5KqlBaWMGm+nhGJAQrVbEvSqJzgb1sEaxRH2SCW5wV+99nvldq8mTg4rQGlJBsVu1oRRaY0k8YnrTonMVvvgiIzQc5HLm2OJqKMRaZtD7UY3hm/BEV7CAHsL5AI//0fqgrCWjFXuCYLdw2Yw3GRDRMG15woyHcdE0llYXVUiijYnmYX0fRm0YhDuKt6i0AJ5ZDPJF2OmDoHxbzuBThoccdPCO2moupo/HzMp1SNs1WnBR71yPvC4hxDc6OD1gKq9orQuf8l5GIf/03iZC6I1aKZRq1obur1h3jbyI4FDc5/W0o65XDQ5RkBZpIJBrFhypXwRYm4jnDHlpz4bx6YTl5oOLGarBRK8C9JvR3FjV1eEcjT1Q0CDTeSGqrVZ8XgdQwPeJdK3O7HkmobOcM63Atn0e6elXMCvP0BZKYO9NPXCBla7ztflruHmaQdiCk5h1bxkDmwmCDc7jV6crueXDQppcyRd79aWYdpD3u6QphpriQhAHW1T5hFZQ9eqW9TZL3yU/vEc/mm6k0tbGPgo17q88v9p5u/fhKj+TYfUMpF+lFJOYioIINzb0Q8c7sXnk9N/q3iTDfcXkpdXJUG2E24R3cDSFQAPzbEfpywu22x0WsEevJ+ITaTj0GtG5s2+jZE8h190k5KDeeg77oP8AwqimYA7EbI+jUw6VXNl0mFHvaz6bM1X/4dhvbqzTPoDDZHX+MYVNYlyK1fU+ECMVRVuNbkxlu5shUHl7q90xW6IzLfpYkVU6sXcsDdC3iVlHS71GhCfYP2MAsXf/8GlIvyc+DlDQcjoCCDkeVhO3lhB5grBh48y4BhBtoPok9/FcaBorvTVbhTHWZwbxtbxOU4YgpZHGQc619nm/jn2bgo6ahlXaQxdyQNUtoXQQN9kz2U0j1YB7302a8NWau++53yKJn8IdlhS109/yx9cM37hncbhYNWsqqu3uGYMmDo51aTsNU5R0J5VaxVD8msjLQtiJu2KyhXgeNkSZ2SsXTJA/k8HL6YtV7KbZs3cl3IYSrcxx0zD2VcpfZCg/hwY3apXsW5Fe1KSNcxevd1PYBWKSIjL4xIMiiNOouo6492pNeCdKOj6+p4ni6SQ7GIYPa2kBVzX8ym0sCclFcdV/U8eIoH5Uf8yxqAzMFBii00soVT1IWjFbtYfW7ZdsqbTjyjV731YQMDRzUUoByoYF2PIB0eoY5FQSRRKpBAfEu61dzP4rTcHz508ZlS18XVI+Qi/oSK29X5ma2gGq/Ter2Zl/UU8+QSazuvE+C54CMdiqGcfFRJJBsSuazQO2bx2Z2tWnC5z3+rMfu7k40M5EsnoiR5CE0PAfpBGPhi/q1JCbY53AjnVr/2aH1KmDwCCHguVR7UL7fRJiW15Ab540H64cuj8PLMlLTjN+NTS3twjVfUd3jGfhAzYiLtYwkIEZBCLAb3BzD9qBy+1hkkc64U7pKElDz09r1gWtl2+A/UdQTKscfs+V3Rgtx9Gs+mwfon4dIl03ltZyB9hvKkgGpsFVcsczNTGBp78GUe6qHXVLLzcdmxNrk51NIDo1Nt3j7vJFAwDbCkLdfl7k8Y/XgkFMKSlKOGLyE/oiKmuCo3Ku5Ocalby4QKSHZqOswytDBmsS+kZvzMRwPcjxRHRX3Pj7BxIiDTQkAKjI+knj094VmJvXpubxvaP1rrVfuYKrkX/Qs1gI0k7lbLjFzHDZr8+54JiVRd9vnMuGVJQcMGdJyYiNj2Fab3lH+MYIEycO2SCG73oTrnVXt/jVLdgJNACb7GPsVhoi6lbKUbAkXnE2rR5PWEr5k6gSqF6WGqfulLz9v3GauEl/yW8Z6VlWZQlOJYqR5k/Go6IqmUBvoYrkO/36cpc6GA3MlUChgcbAxj1avzgk/5tbjdGcrLZ7ebcn9iFlB6ROo/+Iq8uKh10QBfPekXieS11SrUO2sSOw8F3VnZibvhjzeWZ+PggGOcKs0JayBZEYco820WutMj2vr4HEUJafBPe4s5JL33F5Rg1mDzkWrhvEce9e15wZ6SOKCR4gYKKswvU+S35zdRg1PT/j/04y8pdGj/cR8aX5ylZpiNCqlZl45lqUJqDQkGLkDrUFGBj9nfXmC2kzvgBtJzZVL8kSex0wCBy6ugbMZMjcMHxyjFzPi9/ZtojxO7ZXleAJ7LZZNy4Qpi+4X/fVHNKTQZ7pTmb4ofqjcXnI8TxUtUcOtctotk8fl4xiJy6Zz722UnBl2uGQ+bxEM0BEbtHlLZy+0oOVRDXfdh7x4gp9cH2QXSpoymaPSn3gGx/6odpLu737BqfepvlltnqkCXfG9TZdycGREyjukt3EBpfqliEj3o5UFQ8BJf9t8i+wYmMuFusY6DCemdefjpGjKLJlYIiGjS0SbEysbtAZlU5Q6EopEANoKUbBm3Ye2GQ1hiwCvOIev2QsBXnDNCWnVbBMJGhFeLPBTQgwmTC9CW0RNWYFBYUMW0r8R7/XReSRq3a/QhhR50lsO9kcPxZ4fq72QFuwUnSl2NOEeFbK78g/bMn4r8oO1Pi224x6xLWpeyzg262DSgltVbBGt7XrM9nmPkutlK5ntBet1sw/iJcEaRsSfHkIcZdmUDaq0jgbIBEjzN4E6EsD3S1MSmN9/1gBDXFYGtt6eveFTgHjKrDLjnhlldtBQNgcyhocXYQ5JFsmrhzd2f7oCmo7TydMHFsuLlIAlMDnEvDPasr1KcHC3VHCXP8apYVljqd3vEZixc1wCgd+sIyb1wgEs3Aqy2m81ZDe0SZdCrBWdCa19CF8bNGgyiw6ObfYx60oC1tGHq0kqcNRlBIcOh1a04DSqY/+wvp1zOKyhCywXjzsaT+W9RnjRuzVN6xfFR0lFn5csKBFeAclPaGcsyXwjMRQG0GBSRtxxkl9ZxKXjXiV2m7OG1trzbx8BZL5r9Np3Th9rbf55neX725nA+BOmELG1MWYYN0S58bJiIR8L1vyVEDwaihNhhOBjYCvDvC7QzZQk6w5m45geqQB229+AxVXj6Km7t5ZBcK59mcFGxCmRCwVNZ6R+nnsDZGV8Kf9gSwhA8sz3VtKT3Obj7vKNa2/zmcvXyE1cc8Hxozrj2rcgK4vruDYWFg7imLJSv3CNMblje51kxqg24kl94locDMMaE+Zb+Zfp2a66o0cx3IC9jinqeJ9DcHkoDTPe0uJImzbmCg6/gJz4xuNErC9+9ek3dXdzfa7lJuoBrnnkon+AkS8KBxbyZ/MIuO0HRj6/BSUNKlDquqKXKc+L4JO40Kp08/wUPYgL04xv08KQ85irJ8WTmxNMQRRuL966QECEpa8sG41aJb0aqeibqk9gR+H4yu37Yc8Ld0xnFj3VHLdwOnED1NwDrX712iIrce6N7TGDNGul3Rz9SytSIXswsYQ9X8TiylinCRXvzxgfolACwAhXTe4EQ9wX8h6DwVxz5KEKdLa8W1yzX30uZ1hBUt0hMJrs5Kc253/nLpirMNY87Gw8DQOGb4/kDphC0dsDk9aabd81xVWRukNHxzpc2UQQ0kCgcpfujtgL4Ptp3s3s8GHTCSOR/1HJZ3Qa6DxwE+MiizOE/Q6vYS4lj1zDIFl3kg6YCOgNAeU6LKtSPC8KDOuwZlWcaSApY8u1ThP3DyHSbP12zgWCSWh1uvTJk1M1bay6FBU4aYaDCiTg7Q8hoZ5NR2ZYJuqmqq9nDmW8sRqxRR7s5uv4lgmihnvIDzTBDXsF5FyVNA4ynb0ZDGHh8Fr/9a0bZU8lzsflriA8xohnpOb4a1v/0Cvomu7IniR9jLk6mMfbNYcJTcKtiZSpW1l4FdaaWI6i/LegyEmXJiSaoedW/zMneQed+XWXPDj3rwKetSa2S9oUzPEapOgJNCQfAr/cPITTq+1PZVNKfXw7Y5DGvcCJqn9SuzT5/C2WhsFnvoGJ9hL1z7nV7L7O3uD2p7iwe0yU6utEiFMcan1B8ld5xGlL82/6DO34VtIwB0nFWA2hf9hogqNe/arKtlBBQEEhFK2n9khvtDl9SIgQ6pGmyisg5T5EhgyE1aYPQzAAbzX4u32Q1vLCaSeb763m7PTQVC8ifZjrmYOyEVYsgO7pS+p6oMw3L6XPBljtfSDQNl9gelmGdHky3QXrvLezLlFJrGmJ+STFzHxrbEVTnQzCwU1MIBhbJtAKmHP1hDQfWq9ocX/eLWA/4Cq3BW8xj+Uxu3Gqv0GzH6tmhX1bbdbec6/mdWUcTS2c4M/yjBEHMkHWaY7pte398AvAEF7HUwUbBXBvlD9Yxhz3GKpbFIUPpOLvvXng6tMJJycbWKocWxpcB2Q0mLzpZ3i0+fPFO97z5Gpo+us84HvxZgu9OCswXhddgbU+3rSNzX5Od9rY7x+ghXOFOwUNHMgIOmEaRheL5osDReDmhasuZ8tTGE4KreIuKTJVy1+jUASo3p2WjDVLwI1C+0PEWtxz3Clxz8Mu6xvtHVQqosvvz1+rU3tYd2cUaCADCfU7hvnBp8VQzZ4d22w4f4fRjlsa+1UaVGxQ6gJXlrQkubPs2HgnqyE3WuzPopXJgmCie19NkKZftFu77GYegz6Fhay/B62pEYw9yc8VG4JZ8xT3M52OEKGDU0ORv15b7COjRkl2qEHZUp6b/fS464Bl4LXG/4h7YhI9FQuODAWX7ym0IDa+AtJp10/O1V5zu3rPeuXE8N2zp3TSn2eqTmpygfCTlINTN8DhCfJKVBPtp/yFtXXdId5bfh80Q33rCQfp1pvvs1ni2zlEIB0KNB6P5oUfSlH704uzYkZgxGrPkB1/3hMbxqB6HTzJKqcq2HuPG35zC2RgydnYJXIDoL8tiveuaUBzVnMXE8I6q+V7QFYpQLjuMCpJFFXOFHAmGPxNDcGMHZ8SpcW9RjwqGGZ/X/UcZKB5jIrWxaCNd70HCT7l8SfzERSG6h40mO2OEKwCLTGbXQtLfDhfFm7IlPpnyCcL477u9f033KpXk+8LA1XiLhTgB3hb3pyHLbFbNFWMENaQXxhoOMnYY6JFn/AINOi1hJtYsBil0XYrvTmldXNDizXT0+S7Mn2jUNzu6HcjEY70ELGLN5VhUHleP1l+dsyV3XOWPJqGYVnAPhdogsK0GG5mXT+Z1puPthputRT04O9wbBrS0z/j79HL2o5s3OHzNQ6CyiFQRGamVLQJeVZLM/R7mD1Zbh09MbzhR2NBLmkPUrYxjX3X/YI7qNjftrOPKLSIEvoQRAPa9ZtwlwP/59Pbxtpi0sKKPgBEYwnLc1TjvBtVK/cJWANxJZUy9lJNaSr42aHaGG1oYV1yrHDrtjDGIkYHw7o3QPinuaqfVaYcA1V4vFjETtxwdmEf7csX4L0rp5uGd3floke0KPBFBYcZJEHTcar+WRsEuPIRNogY448yPSwDzG2X89zRyaow6WO4iAXQvwX+PDDv9DRQAzvB+g2mM+LBsnmTPZaGzG53r+58H0Oj9SmDAelj9Ss8eBI3hfm8/M6z6IE2hc8NGKTCErG0Brqv9RfP8Yly403RmBDWWNrjHPWrXlySr6MvfILDgd9jxSrKl0c3wHy1n16keudF9QmnB0gbdrLSv8BUsP2hGuHdAqiC/mUvU14agatcfXPTf8+FaAWbBf6ZKji7XN327IEjI49gGJNTalD/nKC8E52dzDK3/4EsWAft/HOIuOtpKeBEPO/jh4Eh4knlEKWorpnGnJ/GirXaibfmbXgAH1fYZ0arHUYM/TmUHLeBUgxQPglxPMWTu5pJGHWdc+8wj7kjOsY3Dafpdf0JWD5mLRR766nEU72qfNkYnv+3kuvc/jrjb/AT94uvpegzYcsO+VZefdOuwW9xn5btdyhN02/3XTTAyBvLJ/j/0GvamtfH4gd7L0jsPEEDKBxBw9ZuL+7WLr2xqr0pLZ73Edzw1Ek7VA7mMA766NJRZNnw74ziFvqGUVn94Kct0UTznMMmWW7S6Sm9AwHAaetOl3X0S6Sz3AdFHZFVOl+7u+HULa7IrupuQi6IeF2GhLmEgyJ017/3kuv8qihD1mFflIX4P1onpBrvVJc6F2dpOTOgw4U4CXagUvDooA5DNGkcNUhAX0BcKK1NNXcZlHzhqMpDRH28UrAk+KnZFet2k/36Tbw/34D86ssvtWYUoQrLLfzTKe8uRMoNKva6FTgnXrmQurAf4LHVPwt4pHSo0hHOQ9zILuTVk84WTTjgRz6XIh0ipDbxylyJ9J/bXX9PIYKg7rBN7cgJU0lr8yGKgr5dXcLCdyKfpY7k6ojQLmYYChgaeXMRX0BSKNtd+AN1lwX38a6eqj7xfp73+IDi/TYg1qU90caJZ04eTEIWaZvs49HzWdKW2UJo9PlM0yZjL/zTfQQqsgq6EpWZPFlnfFhQv/0zTBagSLrSLIYYD+reR63P4CNyDAmiGkIL2v15shV3FzMOQYfRzv35Vo+jX2F4KVpu3N4H4fvrQp90tZEe4UKylzOXVzmBcQ9I4YNhW0QJk5sSZQSKqRZQ/65g61W23F/Cem8J/Cviy5IVhxYP3bhBSj2jbgF81Erdfj64AcN0sfw79nonm0NIj4qp5DxIIgLYS3cx376G3cWn2DEskyjUpdAdhO1QeCpd50vITZBD2a3cwZgfe77i4dcqLX2I5mhyJYB6/17pPVo0/pg4TFEpV+/Z1NbDlWPmDsdpK3PAgSkmllOGnQjE2/3N6bO2oQRY5sFI1vg1jLDvC1IKcmom4fiuOKGjWhtgC8HtIUFQC9GA4q8pyxapb5rraiYZfOxvUYGqrAEpklPOIa2U+AGZ6qFUI3lDL64qw9EHeOLBQ2AttNhOpPFrMeq5mOzjeF6EfJHT6e/NNKqLZ5K2UhVmLt7VnJph/awU5aIqWCj2TnUkiDnwKuR22MrcAbkPIDEE0OEALdg4xGYZ/VHksC35oOijz8OwFSG91DGH/1tjXJxweKpA6FhtQlrN168IHYtcKOvAXu0uZevKH0rcmlhiSxkbS5YHJinXLFHEtAhLmM5ixhcVeV0LfT+hOnKUAmcUEtv3hDe73yxszBYgilxNVRUQavr0mf7V9WOslGjZiF9oiv4A6sw5pgEWAJ5hnZbCd+m7hMtaI2AlaOJseha1nxaiwRg5udr9Gv52ILtMN0oeJbaAZrkcCFIgzgcVHM/SkW3sICIxR0n1uE5TELlN4REpRNlj/OZz+L3x56XiM2OqizxnLitLJXooKQc0pUY+HTeQXM6qlLrDF7AiOtB21OkFrLANHA85TtlEp7vRYN/1E/x1kc7K6NcPqwilyb5dlOvBSimAYgs6ZNkVU0Aw7R5q283RQkPALSopDKtrgsBpA99AYXtC6tvnCeik4uH6X+uK2uoTYkuRP9tYgh6ib3QmAwh3CaMVVWFULGsGo5i3GQd9408gGOxEfoECe+Y5IWIL57cvsb3ukFO6yUSvdHMblhNdVklG0HAGlF00wRQNuwiv3Uht8uBJ2eDQ+c7gRUit6kA0PTZ3YU/sEUPzYru4yM3aFcU1hEaeEpJGXm1ofbvSKwNK8ycWn62OTbTk4isVRTZZezVKQoD9Lv9/RIODx97IUO0rCWhH74JBg44hGRa4jS0oyj3V+Agux89CEssosQzCuRc+AL1CTIN2qK3tHGrTXbMVdnus90eKlGsoceRaYJkW6NfEMMr3jgm2N8LrSGawkWgVc7LFuvqfYOZkLjURwHTtV6jJ8IIu8bL5D9BOyCYi31mEN/Jo9OGg28sPR+fbEEnT7gchMACMSXYhUkx2LrWkjzlrUeRBPOPaNAEPoI+3u9Iy0Ae9/CxVvyHz1eIGbkqeFp9+jGI4X3R9urIJyQ6j+uMAFbEUeCh/muGY8eTToq/qzefoX06JE4oj1lMOVGTMOUk1Nmf+ARzqZW4P+SMQlXDIdQbYRqrpezDMFBls9kz4A5uLpq4aCaiaEg0eR9hV2FhTjYEOdP37TDqozWAXu/1z36wR/sG27asX0FeaBpl2X+hYTBBecdo3tD7Dg+pZYu3J+igVscIT9OxXmH27pRxyXOksIAYG3Sfy6gGKwiJ5jDhgJe+EbIKp2rhGEiSjifgbJxuQ2hEksyzMCByU9RHmbmZlNQcDo0fU3xoREl3oZ/zOARraMl+pHK+3yc/HgnZbuRXjreGjUAwYGrSvSrtSanOS8a30cjc2unwctlIVk0DQcza8OFi3Es6A+KeFwrkpKzQp5AWI0JcXb1Vg7HLcU2cx2o1XqoDZXlITGAp61qDfIG5rRGShl9LeZVOQaIr+DkYAEFF/o1hlFFZ7Aje8t/559dw4nxxEmjRjrb8/qrO11EVLcGS2CCpgjOnEiYU4Xbd91z9P/r59QfH+jW27lYe8PS3hn+6tJWgfXAWT1GVeW7+Ne1pPWn8yuk2+DwWKywbubZeNIUuE7UYHqBv6Vd1PTxCIwvnNwuIGYbWsdU9HRF0an10T44Ohb/685ilsj2dtcrA5StqVS5AETepm1bVVdAzYLvJ6AY4xml2+GnmTVcONICoZ71Kh0O/Rflet74Eof56XIAn1ckP92oBvAvyzNmgXgz+OzU0QfVTxcSLlxc6aIOgdcZ18ps4TT8RBw3gx26dcH0vhxr792VglZ7rycaMsu+a2LPEONuCcsFMq85iQOPgk2LBKD8rksBCSumtzMJ53DgC1KwRQetxjpygMV8zimuXz+KPG1M3BMUORQDM8/7a+AvDmX1WOOhB7tRkOZR+D/yxi2VVaCc3wFIImKNrlhrFEpGZt4s5L6i0phmCUb0KtR79giuWTmTBhFsymkzH/ymjc0EWkXyO5KLWJnhWxUkxvAELX9DSpH/IiDkqBf5Nrmk8/Tn8yYlqfOn72BPfeL/VH+l1/awLvQT+g7j8Iao8k42YHHC2CZ290ocK8wFOjXZae9OwYyTmlDSCdfpjCIn3HLVwWgBL0nB/QE4bS8QjAl9cW4sBCbrgUxi3ZYiP7b6Xb8Z5EZXELuy7PDzgnSl2hAjgUO5aNmT9qCIP3hahaBcp3kdCS6jjSDoDG4vvi4Pex1+853GkEw8wmN4bzzLSs8GMwJn+bNdSGo302YH+lmO0l5JxG0RpaCsFfoomu3KTETP8ljOXh372ddYJkT9HSFdthQv3AdDQoiR8NvcfEvAXSPjObRXwspP+EeQqGU5GR4CIW+V0AEFEdgzqi2pKStAVf+q3ipy8vVqNd/SWw0/h+ekyZ9Geftg4FjyoRzO8PlB3gNHtTUCbdNBOtTlVj4KjI9/Lx5kgCAhOs56PBbxojd+UercvQwbOl2nq8JvsHezxWKiKbjHGcKmpb90Lctq2NaZ8sc1sjTloOoykqifrVxQQ0OoE6fQpTzWlsb24fvKBKY+efQcSq1xDvfMdcUE+jdn8Sv1DwmWAO+a/t3MfQ9/Mg9sgrP5D4lbB7yagSwHqva5sr0NWh1waxw5zgUwo78LpcjJZ+Bz3hzmRvLE6IV69qajYaUBtjh9lh3h9eykzW6zfKY9EcC7NgM8zt3TXj5sX8D9KUAfqyO3O+Wdv6VIM1oXPg8IqgJWBoZ3uBA03F/g+koQP73a4zwM2/D4/7LdcVHNYB6tC6JTHy7pGyL0TSrFiTq3rdkummORqBf02Z2znwQ5B8VrevcD1dZYlXAS6fGHZEOnRE97BpDhaJFT3rTP9pt+dHv1oHp22wU4JATTAATSk98fHORSVh9jao6No2tpQQLp/B8TOowwS2kTmpYUkSf6nlJSsqvug6+ffFr9EQ9YGrphd00Utv6ut4+XeBHNd43UEnQL3Zit/P8cRj5+ZxZk2SYWvKG+NdJooYNQBc0w7xZmyOwrhO5H+V9jdEZttEh8vtA1x9+MknlwTcVWE0nbGbnQVLkLOVSIVf/utYcugoNIsDpXdQUCpDeZTGrKGurPSRVPhLsvr9rTbn8TiSBdwWTqNj4wSUEQhfWAVTnjU0FYRcqt5y0zP9Hr87DHaZ7if7y3kPSF1hQVm6SEoiNaLeMoHxOj0fOXaKKFQaHbW0E4tlwo/ZwssUGtxwWjBB1d2m/ixWskFL8Cqjg4BFirksmmX7eSj4DEeNOzrnzKhKkNamD9WTIuiBITl9Fn1nQ1mNR5oiLzrf3m6Ef3NYpkw3Htcwsa2ooHQJDineTn3nbmVuqm89RR4VwbJy4EPBIfjgH8RBK52H2q6/cog5q26Q59G8y09m0zAxAyRO8Dl+G8b27/jTql7Ut24KNEi+S+0ogmJPz+sD7Iy4jlyKmg+615TTKsAXG/dq92165eLToUN9QUeW3e0fCct0uIuRzJZFer+vhMq+wSxHa4oyYrKDemwZQu6ZubxBXk+CEHRYrL7NmRARDZPMY1Ao1O+Yh9oO3Yu9d0I1fs5zaRW8G7vH0LPTve+1m8B0R9TDJMH3n7sDCrLB6rrxhn9qZJLFuxOpCrH/+uiINGHYx25KZAqvNRSBWn5dfenxHTTsZwVciLZCIq0evNVxApzAGhBShBVNGFLKnWMJAmpqQE7+LTvaF/QH638b09yiyIzUiJx+oUGwdZ2stfIdmARcVBtxBgGgLT2TzsA+I6M2wQzmbQa+CWPu+UXXdnYZX2j0eeVXDhl+R1OD9t4b4+TjFgsP9jUB+eGU54oKA+9FQ5p49jXjdQUK59zhoYrPZDlODQB3DB/FB7kEMB75hzQp8NL/MnthzSbsfO73glEIRmIa00KRsCI5Le0jt06rQY0jwYg7nyWfmzbN9SIvUUuLYz+GSUUa3qogYEw6fWJxnA/P3KuvZ57419nOr+uINZIaNk+hA9JGgOrzzl3mXZ2VL/Q/CxI+My6JKdkaaD+ffo0A7a2jxDJC/rqwvuVEbaS0tnJP8d++Bc1u92zrO/dfSFuGdWprAyYGIHfgQ85npp5IA+KbsLB7Asx8vJPv7Bp2vIWnSOlTyX2OaAwhS7Vsl9ua+fwqjnOwRhxvxspgLphi7umqz2FjJ6kbfPt8qr61EMUqItPC/FpuyM5LSLGWOhQNKP6WBZCvXE5VCvcqV8zfRuwYEso9u/mraDtrW4Xpubk7MQRA5gEYz8j+vi+HL9L+IDv05C2ao5WJORKMMp7fZttkhWM2xffRKWeNRGU8QEORG/t6r5MyhEyF2+JX77CIj1H7nKATuLGd6urZHdXf7ISv8g/TJ1X/ztQlE15WQNr0rKATNlcd9XibBPGFTXaSWN7huWe7adCpwxuW8rUPL/j0bnMk4jUIy+JYP5E1OFoBIjaPyTK/VV0fa9XzJLcDhWSGzLUaDpuDOGwH50pc+kprp3TI2ljwc25GkftXubtQfZOsWGGVKVKV+A3/pQ+vGH7sevHe9JKUUcxOi+jvMxy23bcGIPVg44B2NgKhyjlz+W4730q1iYaQEjvbEAOSu0lTTCGb/1wQSMmXIr7M7vi+3Z3p2NQS3avNf6H/s9VMTjsF72/PPKYduG05Qu0qIVI27ItGudgNiF3ryCqlVSFn7HxSP5OsgDJtWvIkMvnNrDG1Z2H8R7A/FJhh782Epq5ROvB7Rtvuj9T3qQYlxR8edhBr88ws5tZaKdkBBhPNYHqYB7ZdeFf/ZQRBcUVNxB2u9u0DEkGxq7Cfuf5Pg7DFhyIoQ9Hh9dRKpMQN/x92VR24dwauDNXLcyZlRfWwyLhHQMCkn+SaI+/lXhHAzxSItDumG/X3qh3u+8+qxj+vlfo3PQhPJt+iL2yVKUcZz4HSLakUg0P6F+jHsIZ4Levq7oG0dY6kc2WYx+cbjlEzR9KJsiEw++Xmij/yGcAu8Iq8vEFi2uu81Imw5Nx3zj6Kg/pIrigbmGg0GikRFPUBbTC5XHYDXVbKAX+xl18gxfzX0zQaH2KoJWGMXFIJi9RVByaDej2XGaIFl2f7atNDh48vpXbVpgPdIN7SgKzc1dNLrP/yk9L90NlsLEcLnOW3tTJsD48RK3tPoQnYW+cziM3GSSTCv54GN4cPCg62rZXLcXEV0A4EAX7Ndvv1lwFyU0q10cn4ovhMSa6j8oog1J7sHdSBAXWUybn8szZQab33pxI3dY/cb0fvuJC4eD5dB7xvz60ga+R63Bz+c/QH9M05XSh4T3KPVyQwzJhpTb1qhXeS/CFdgNxoAGqJDpfRrVduedjyz+aH/7KeatCFPzJ9l89htkd4muzwEzq+/d49lCAC5KOw1X99a7EHVgMBEsYh5OZPUBnIT6C5S7tswPqJQ22zpO7JlEx2wQwUq1pucpdZdua8EYJhqTqUgXvvQN08pyxXWCwXQ0m5LBjfmlOzaSWQ5f1hJdHFXPVCKtv7/0smIdBeTijPQsmsTmZFHU77AziqxfUy2uJMOTcTUoffQutVZDWdnXKZr1OOfah7AXGu19BST+i+CsxSJDyQrYXBbNRqI4Qu2mGJEigV2hdGIjKlm6/bzXemt1JB5Z5mfrnFk3ytHJFwpmWLSMozzW+vE/mRFRA7FOol4UvLrpCeTjKFBpXFY3h8KcET++YtbBiCD73P8SkXvDCAl6qpNPIemCdSWgVvIhC/Ha3+/Z2I3b1ZPU4v5LjvuFY6v46qXQIMKJbGM4CP5WUx6qCAJe5qtwo/+Y54ulxQd5oxLbFhX3XoVl9Lyvh4XfCCzpA43Eyru3FIwih4t9ks+rljmbOB41/N+QCIv99yOgRr/jfD+2ZLhfOlSobcTSseGDK+oGue/hJaX99o+79KKg5EQftgN+XYgG3AsAN/DfFa6gL02CoiFWqwWzDfQtLN5M8t4kWXqv/k1kJjQBCg/0HTBCUyx2dOOySpDN4H+NywpSRbm8aGsAMzwvZ+lWUF0YNoviJLnOG6LiSWfpmRLTr3ZfWOfkUsMa8VZOOJ3aJwFQLmUkeyoHkEWbt3a7tFuOJvV9g6sZ7fsDaoOC76QL4yxXAgMBY+b310HnUfQ5Rcw673Je8e4a4IuuJJjjWsngQu8ZX5muxVKZnofr2QrPr42DH4BdldWVqOVL+m3MBxtG8YUS2ZOBKj16pWZ4QAAdRx/vYzo6DGhsMoezm217H+skgWspwI8Fx1gVdK5QHR45ywT2xsw+z7rQF6sxqaKmt/fTPRezbEejFfCjHiDkVSW7aSTbHH2mc8w4l42fDFsh9+zP1whg+7DihSYybNNVSPSva4IDiwUwish9ci4ALaCYImFymB/NL6YjRWl5PJ2KKveZRoCz3LX14sY/OwDkrYyyeR9fhuj8mV+NtlguwFr8ekCa6qLzyifJWNakk93Kn72P+wUjUBMVVtUJufsCOwdc22xU8dLMwDpQNO1IQA5hkW99zEEglm/xDpRgXQ5iSZlXJd9v9tsUFWJw0i08B+UG4xxBrpAdIK0C9gvUuPpN7/iaWi5ocwSrOp9MYyOMGbnOkwMNm3vzi6Xw4p2oKANUFGYq3Bhc32GV2kSSwEmvbWq6QekaInGC82O7SJa+lik89v2BMFtXxDfJlqG34zsnSwZs9tFrQdC2zPMneMdOTso1NTdPH3jq04jUPIzKfTVor1EIBiUnw38I9q/tqorgvv2+6e1a+Y9dAr+7YOyauCDVunStciMTfuftBUiDWv67C4NDpbXXYw4WeBDlYe5J0AFMRFbuFZmX2ycy6j5+U2lNlsDhDM7fD7FCS7ga4ova1Y9aPt82WJTDB6qXabwXK2W4CfF/ObUyGdrJrC5pC2btUi/DgHIsaA5vSM11/1KQP1WXy7YdnerGtmMeJAy++AtGHSNRLbWxyiq40176wxQLs0IjEbtBAjBZ92ZvY+m1L7QkbW0G/vlVe+Z6/PCefIKR2goDN0xS3ATSBLxTfqGvFozz+GAzGsqL4tkHXV6P57xEPrrgbSGJY3Qi/duQAGtV4WrfzApdGcTazydA1KHDgRGczvZ2egEUUXDqeMhubLgy6iiZbSqzxiBN+inKhO7YqY5yT2BSe9C7qNGpqvMwHcrA78ytBfpBWGNrkzBtMtZHIhwn0HvU9SgcYhWamR956ppcN8sgQ2PKEPylx49Ol8GiLsLp5QNHt24TR3h5MRGvuR/n8dmv3cUBWhUHGEXRp1dmzwQXXwokfKaEyUisaQaLU8veUapEz00lKbuF25inyDCZoadvcv6RBPIwYDbz4wRbzs7JxSd3aL+V7o3HCoP8jGJ5hXQMTVyAi21eOk0rDrduA8L1doA0ay9BuIiBLDJvBfei9voI0l1FOGi5Uvg9htl5QZTvV/frjkwB38MO6pqSeAjK2HcLQ96sGm5QyeBwpq6Tkx11iIIUR6rLbBqq9YJksfxzTpGp58mh3p/b81K56IrbwiaWwP9hMk0pfJ41+4EWArEHWjoERJtdhe1fvT0BtnaSQOGTmTL2o+9mc8YzYrULH6PWFVB63hHO9ZOo2Vg3FXDPk2zTywXSoBKDCdZvFi6FGvEyDLGN9NJ06Qbs3iYBdzbTElT/Fd8fnSJJtTvpyGJkx6okeO2cmqt8m9YcxjWhO9Xmh66Ln6KOiVrmCkGdgt81x6w+WpGWJB53WB35vKvsrXid6xpFUfddqbTZTC8O0sOjbVKIkAfEMzmMVmjFEFRsVAYf8cU8KZyrOR/4a4nRlJ861ssGq6yUFhMzuG2eym+HOMeng0uS0DOvpIBw0FZR2LFE40rDlHvSsE/yM7nb1XpiNgG7ebDvoeu2zopkLlChopJSMuo3q8M8RSU3zHSHwoI9OaYEAHvGzBTjsbzRTE7BFX6SITiCgV9+e/8ZzrOb4K/WHjK9MOwsZlv/w1rVD9E/6jmK9ZGdwE4cauy84P7LLoidOO+I9C+gBum9H0R0h67Fqdhk0jQlE8eDvk4LzLlLpEkeY5fQPwkb6PP3fiZ0oogAMbW2kkBNTZ8wOxF2X/J5pS5YCvJgKHFf2dEJJ5NAOim608YsxJqkrwJonsLID4D0+Q5omQscFYOXAAygjSu8tRDmCKx9HAVKtiKK4JmP2JoAOs6i1t9SBqV29ZYeVlmqnECTFSxz1lWdHHkEB1L+tMTIQrjl/N8pPopXtrG5o5sRZCGXqg7aSxbasZ733I0UqNZaYtqbgncQ+cwsJwKGxDEeBh3tJJososCkSTVzDxO5k5Qxkhm+kFuhHwJzpCMNzppzmkMKsnrhLPOEIotzLaycqpXs8hAkOO1K0J17R0fhS0aMzFvtLFc7mEXZ8YZGv00coSHuXGsiUyBBJWyQJCbMXSeGPFkuJ1yZj98eKwrl1x21jCfLFBNrzRmr3ng0o4Yq189VfkkqGXu+Y/NLWqPubguhO7unQvgw/ghAvGfgLTbXPPtiqzCmpaX5JGcODhp1I7tMU+lTSfKUgRlCGE3zZH63J5xcsVIRU69aaqiVXEwieZ954bH0y38O+iXbLZnUvh/yf6krrmNwmqG39yKMmCpm2IYolJoHiBafsvnJvzhUeFuFbzd+ptig9+mZ93nEJGJsWGfvVz7aMrMstxT/LEZJhxsxZlnR5JuN1WsWlQzXHIhtpKGNiudrPjtx4PwbyVwIPDiXXEZS2NdUvzaLjxVqu/J2OykAf+2MXLVVAUKrD602RZDRqzfWmXoYBhqG5p0+/r8mBgJqpxb0SYq7w4eVYVZK2dVEcPDfCpVlGPkbbhq1AAfQ8N/QFRGuRIWAxqsX1B6iz0EPxO9Xdk74zEzqqV/y7v72Mh8/52hdAq38TSQOVB+RRVaCH/0ecLPKiHLi3F4BQsf27hubp6G58TTKbe92U+Qw4O5lKuA3sgwuruUE5vB+AaqdgDXMbpWTDOkfW26Ho+f6irsItCzyI2yWFAvkPMWlHPuYAVrMqvF81jlzDh+kOselOO4Mxu5HiydFkpT13K1SQrXFpVX6UlGSJ3ywWHay3JQfXcnS/zI5KWEV5asCdrqmxU5oxa/GDNsr744+bYvST4knOjcSQY2vm76ePoQGQWcJeWVnCAYyDMALzydGS9YXXugPnqvXrfpFe80PszZaGjxTFU4KWGagHPoQt0xyMpdC1oVE8PeTUrtrnCNgWfhhiZ82sJ6gF4LB8zbe8UIER3QTNYZkFuTSgnq2BC3GrI2XMRfwhX5QMnoNwJyfm492rLMosi2bCpoNPiIN9ol/9kj1ygsEkTtu55v1KSIgA9sdXc/ln7ngksSKjqK6OARx0CF9sTmvUwac0rAK6iAkPzIro4TWFnslEicb3/m6S0QcgJTv9mAd0hfyOPAc1JgOmwdVcgMxa8uDkyw4yg95tV/z84xFOKLDHVwmgrMb6WlZgQZoXjjR05KS5HoxAbC3t7ZkNAhyEO2Jeh+4gLXewqljjvqqg9J3OioIZHtMCXCYLZ+kb97M4xC6Jm41dLnm/DI0ZccbzycX3H+URt5GZiNGoaFPgTtD5VhjfsAh+8QzdjXFsnDQSHZKUZ/nz9IqQh3ogA9KkhVQBv+hqEX7wD30ayduz3LfYKddZXeNYCkG7xu+Ukq1pjN/9US3VqV0QPky99xu2KjGfU0C0DsPFDcjZ5/0Ho08WLdbgtUno6ZSmIdyF2dGs9+wA0Dzrnw5TDov62+T41xpBvAluv680GtAasz6z09NURlx1UXikhnt5es+Lt6u6repsaCNv3VoiZSCtbAXMSiJbuZORgi8LFdYlAnQP0Viu5Yds2Quc6nyaFjm2Ka1QLBDXV5SVh/qPtN5O9VVk/aZn03MX8TiviE4N/YW/vOo/g63l8Wnu20oFmjZxQ5GYsvqvrN3NCHoYt4Ss6YbV385S9RR0L90e+WYnldEIbPVgQ2guYBI2QEp8LFAtBLpXsimDYBB8lafdMplsnfbvo6guB7L3sTl5NiTPVylAoSGZU1bqoHrmsGdWCJ5Y45P9MG838n1FzDVzJsZT/HF4xdz43N3L1t984kYjM7/yNSbgogEOGpxld+CYTT/10XS1SSII2Jl/LFkNUKzKfRCS31uZEiRGO1i4sJI03rzuby8OoKCTt8tuMZgjvb22e8noFnp/47stjuYRAYS3pq1mXfoi4CtLsTGICM9dko7Dskp6+Woao/OsPTRUpKSfGJ8u3U8aOsGEOPp6eirx+XeBvkuWL8wrP82TSYqHhb1pNufsJGZrT3dUOoiy0Ca8iNaO40yab5n5JevU3MB7fvfd0gOzHnlxe27I/aVJV0wAJU1w6kpwluPKaqQ0Co0znonhNUCFB4pJvHMI8nBrKmM4If6HFMimBsH4uEVpgpm34aIu0dD59H2m/H32Z5NB4K91PGDnIVvFcAXHKbJh6SDAZVbd+f1eALFAJuhcRUh1W9Fe5Wu/2lvC51y8h2KQ5SNQ6ZTLzUjXq1DfDsfMg5DyZ17k+GvJ/hDurZDhJlNJ6IMdE7iMGR+64b+orImSgUr1rmkJlTQkPv2Q8RBECGQJbztqhdnCP0RUta3IldoCXscPi8WxsYw0I6FtfZqNrJG/fehLVS+MrC9WTa+7Ab8FoWK9a/GtoWgVFHrNa8f/ZavTv+q4CVVZaY7VZp5E761NqNil9y21PvwVnjgyYYp7neJTWhZPyVJ3WPjZjvjbaLFxBnjKVM+okhRhi7lXUSFefVAENUTrmPXzuGO/S5yv+p/qC9QiYc6GMj22hE6AaykX91vRXGh5hYbjb/VHFjhNL33ZgMdaBRsxHG9MLetOBRBxIEj2IjrGYMslfnfoqMQ3cS5ox/y/S+I9D577pmO3KjWDDXJSJRNtBT3I38Ng+ScJx0sAqkG6ACbwjtv1izJRvft0t1evFzqw090UFPPGQ9dBhF3lyx+qJ8poZdPA9obX5mg5UGjPSavh8FSeAAAGCrP88YPoQnxODtPawhL9QT6BOkVg/psyj4sXYtLcdFc3RHwp7OPg5jLjmQAKNT5r8ltUY2pHupKg1mWApOcrfkY53Yo15GXxLILryW8/0L2To9OZrKWtXQnmnB7egwYPrxlK0/d7axC7e8ggAhw5mXmwXS3FVD/c45GDPosj97aaNeo695PK2Her1ecgHoZko13SneioDRdXJhB6oJPEkVYHjOuqbmZCuUWqO35oND7NmZHiI9fmw9Hz2995IIHZHa9asyfzyT6d/vnsB6sQWF7xSZ8c27YK0QP8Hvcw0ADK5rZRNmNawClRx4yCTx0igLZuynHpDRvuyAINvmwCMjmlytsAGw5vbBLxg6HK6NmcJDJqgUsdBxNx6PWfplOicLHElFL900cVGyj6mnkHTH1VR3C6tzuLaKwEiyCUjkE4Cct4B+xbOZyEBpKl6rlxUCIhRkN8Vt5DbMsHZIMf7y6Fo9EjAfnqCnoA7c1YaVZ4cus9EMMddLOjbFRzrJXctJ0YukDQZpBBp2xH1QVPapvFNNSkUWvPPwWOCZQOMetR1IZPNKz0juJB9iPpJdLK6rVE0TLoJxdwTWLmBzBGZfGcEiQkWEdLi2oPZaus1fxO7kEb2XtbStGQ4pux8ZFtfU1pF/PiPUt5fe8XvC5j0Ce5ThbZblWzKVEjvstAqQkPHE5EyRcbnBJNuTWSzZGNB1atm51PyCMmoJ7yITNwi3UpW6LtUxXXTRRBW6JtF2rB/zcnTcxq+6Fevh1zBvAmWCfuxYUE054KphpWygQKFpTGyMgtuqzTV/0KjGOKhTr9ZhA+ELZHCCds6Qpm3Y6anSW1H/Fm7RZ37rv7ZFzTRnX8tI02QCR/7aVNcB8KJt2Nb7Y2WgYfj/r2rCuBis8r3BWs5KU6WM5MzTLU+KSRUXC5Qvmpuosz8Lq0ifbp+FKAZ6jD7vHSt1qB7klUGsAyUezpkwL6vgV1wk+8gaF41VaASBQa8ZwKIsWUIJsdbZCy7FjUTvQOAUqhBkoXrykom6qqnLlxs/oPZGtUH3oHQqsvVMhXWZW///HfaILJypkqHH9/nsIYFOYNslCd/n0U6GFcfuCbFA5joT5zckE430GKVUqMmqqumRaTJZovf5inTzXfLSMDeftk1C2tEIqc/qBAKsogQyTh1xOc4IIzBIwtV7rTDy69ILlnBNYLAuUnSWlOif7F0PMnSv50WRJZ79Lc0g02GncbD3E/XFM1ltVINPB0t0847ErZ2kfXcNIlu54wXTc5iXB++spzgQolPd1JWGsD79nJXGTYte3JMbL/JYX6fiAPJtiFoKFeuCqRgsEU3wMDcsxc7bLAF+IENA5kFzVKJ01pdNFGowkOa2pHxr2s+PraqUV4x5r8ph2hrcRBfxEc9XhVW/kATruFASWwLfOKe7k4Uwr8x2M3b0b8LJNvXeeDCYPsdPystniqHDmIGruN52tA0iVLInpNBoC86e1rj32HQ5oQAqoB+opujUSvljGlkFbbiEnAAqU3gINISZ1BMkA3sjUiOzxbqYTrk/B0BE9Am3FCznQH0GJe2LJkWFRlDdWr0HjaRsNDuIaQMFffENJW4HbATn68lBsRyTRr9VMZi7JTAb9jmgQZn35hp5V54VBrqyjhtdWetGitZJMFVypnbQRVdSjhVgN9XBz9ufYWyhVc+uZWYCTzjGAb09BtxKcdug9krz3bxuC3Q0Y/9rf6CJimU44D2LUqNd6VJNQm5clkxfQqEaInO8WGvFJ8hYX+tPPQ2HJw0/vyT1WZSSHvNXdCNqxzqL0BmkCDoVEl980QOAVBiM0uipgcbPI5pP+jmLjiwTN47Wj1y8yMJqAvNXIaQNYM5uvkMnseDMmtLh4ytCJnTDuc0buCBxYoMwVlzrnwMTMxa6xmp1HGnFi6p/Bj4OHr/x8vbjXhqR6DD9ht7pTA4ron37TR0Jnz4pnc6KFvfuOJXShsHxML8SA5yiL1nIaqzzfF+Df/+anKCyifc9oPuGZKTWUsPkYJ64opkXVSp++tOGAmHzqwFErJWkLWG7O0ZVqiNnxy3z7q0s5EcEovdp+OccVsdefEhromWQzwvpoyECTTsFxjmQmcD1MEj1OwKXmTY8gz9TEPEGRkTl/Bex0cqskTOLmqJp0IffL0AyBKUZWAgJfxl1jIPN3nUFBOIDS6VbX4Xlr9E8z9RUK7FKuPucUXmFWvo4a6i8GfsiuvySZ5VsQrV5LBQNK8E1iQcqNqVHY+WgYBM9IFL9L6gBR2LuREaBeGe6fP5P6M0oe/fCi/mkYO1mGojC0c+YzZq4nuoJbV8in034d2kVPZRKetOkDm8bGnzlpXb6O1bcCLI97Bmdat34EKeUnrpWZIBpIy6bXPU2m0syWbo6zWrj8GCJkSK4BrufrFrXGw+Vm+JXomZxfNct1alAJIMhI43tn7V9qClxawDyObQW7gIsV58RUdWYha/EOsGRpHpGB2sd43zvyqX5IrEwP0ZN+xak3kK3qJ/hUtdSpNDDOGeIeSdKWak97SosUez9ohb5nez0M6jg7WcjS5ks3ZaIAyjJrYigqyz8J8XyjNAX8JeHfee3FlKNyXt1ZGwC39rzxyNct51ynzXHXW5lxNqrvA/thskrSIkfzBPdqxyDgpA6o9g3PsZkEj4zooV8XQYyF2TOsI5nkoMwJHHMRkKpvfrnOHBeBKbYTFE9Wps9mwbi9n0eZT3aVMH5/9GK6WR867OpYSNGiKGcY3jd5xepCYntLZ+EMX0UvhlLtqJSaWMBCyxeP43GBBbPmt+Pe0hTQwC6136fr0pS7IGOGYyCNzRrvqpO0OUSz2UhwJIkrOJHV9nBEa9oSYihJxIkhx3ZjW0oviuHvQgZK+O4yHwX1fitS5iqNGEUqIgPA+RhhtIPHZu372SiuzsfW7XqR59om0MC4CxffGu6TtHqo/RfpILEbHDRPq5CzoA06jxC64nbxaSgLDgJajt8P0AuN7wa4CCBcbKg/uAiUH6LcC2jyfQB5uUnZRTcp23mtFxbJauYfH66Zn6Jus16vGkCalHuNu8fM2VABZEUDxpOuQP5FmTM2zR8HOzBxg6wKbnChayjMIcfdiNXKOhVbXSRW//GtXNrO60pgxus8vqCi1pTZ+IriUA3YUpmxeV20Rtk14wE3tyknV3Rk+hmrIn7J/YM60vmFE/RDJEid26r3k5U35pErEutw7hvXZ1aIwQMCFchVO3ekVyVnAYv9UmfKzX3ubisufXuGniGlevDr0UilaWxwg60uBGs1Dp7iGR6Wa1fxgGwoSJ90NHa4I/RBE5M5vOWFuQ7PdGDAcuS1lkXO/k28m8xU8OpEa1V9loAf2blnpYXGhblMJVV3ibAR+b/sPevMzGUCvDpOOKJamCMOL/sMiDgWQllRtgVrb31qmlPxTPeMSfrJL5GBTcfKcKfWGaId5Pgx9wVWgRPkWVqq2+eVHdNheR2Kp5Wgz0DWAEvmXP3aPomVrM3OMYDj5n+hSFXjKXziE2pocj1L6ib/n+Ktq22G82Cktb1BIW2KUHP6aZD3dWJEWmckPaL+714wBJon1JTRa/WZHMW1BfK7kyg3b1krvQn7X/gqSj8xiNC2frYddMItadVHnlEOddJjTl4ccuQXbeI8jWyBKXSKcn9G5AYUYqyNnaQnHtV1IwzgH4p6Zvk88qS6uLuE+QKaW4wUk5eY9BxOSD7MY3+icQJQzo7gYRYFIuHrZrMRlvhvq1SyuB6ipQj6yYfV75g3TngzB/BmXs2naawIG073toY3ZnGO42A9siY5cskmXgovioAplDAADtcaTjMbptF2blpHL4J9xvPOXzZhaz3jEZGnwj3G1PQb9Moblz7i1iNEuEpfYbQ5KOEfdfzfQeKn8t9wNzomD1pgrnnRIeCudXLVvldQ9hL2ZMz7Ii+9cenxMP9g2NOhpHsXwwjQT3QqyxDjY72mv1RNPB5+ygWPBAnwW2K+c4a+N5cod0kqY5G4g50W0SlT4WaBi0LP8jahZiGmL1VlTPZ0zp5y8Kw/qbbs+43i3a/a8F0jcl0SG/o0ntUg+0JscmSCvKnCdC9UGRM9R6ZtUF8xTbk48I2KGCiw6Tt9SfFjstJs+gp2+UahiO7shQi0626yXTeBMLIJ+5hqMCnfJedJYYXzw6WZP6MRTI5GWYohIkHm37yG02wZ0xnjEJM7imY21dJSq/I8mEj4nvc3lEs5/wD+E5vdsTNw2f0qRGLkM/iBJr4tTgwM4V0ZZDF6egPxuxcHtH/q21bSzSuNSo/14eZja7DNOmquvWTgmcMT5C8rx9eSOROgsEBIJg5BHmiu1Zz/2c1V8VXCwOXEeqa9n/HZ/HmInMb3XwuHMwxxY5VyQi3Mj85E9S9VAJ7adzfmTs+9vNZL6ZGvpUwZ8sI9UQQpigqRfehZXme6jZvob/LfQT4vdNkiCwk6S5HddlmwSAd5C5AQHlthLVv/12BfhCfEhZia9qQworsaRFwO0GlsrT03VrSEX+VGPGyEzmCyyi7lS5bu5scPDWn4TaZb+t/V+43scUnsNX+mGUUVbEljwnK9PYtxik/vdZJtmGeUPb0HaqoaYEX54ZVy+rf9XacryUGW4stwTRJ9sqfoFkUg1tPPLFRJ1pmh+91o8UNb6QmFfHfqydFd98U66IDnDi5cO0AYp3/Oq/JyOHCvgg8tgrr/+pZaAjPcMvVTRCh7U+oAz2dqiD5Q+PAbaDKtbHdYVM4LSjnDGYE70E6veno5RRyJu+/f32lXOMioZbnp3ROcp80/4mL+5Btm9EwXwSaVmEVo1EmMgQw7GLR0egSLlsfYK/pF2Y7bWcpSekROexdMvK3FloWFldo3lmXKAjYQARGmlkYkv5xgu/qR85rYg46UugfJs21Mn1B/NxPhV/H45eFAwPTV/xwbLK8/aGLN8UXuSqu4tYwh7WU3hf2p95jFmWgul58568RUhOOGANldmp7Fh1tzVwXvkUILfNpzAjZ3Kr4D58DIwVpZqaAjEd6vPT3df174TBI1aFf3f1gYO3GJAdNxHKSyKKEEOqSBwbt26BwwrrbAr13oe4BJJXpHqQX2WAB22M2eX6XDaoV4k6te/wviWe1+31P4xhiu+Uz39jaKGK9pE13gNG9mPuLEN9yQ8mDHdyLfit63VjTSi2EGBxykgpeGAEAUqRQE+H6N8jPFux9rIA4KTVkFCVH6QYuRDZA3s/qszBmkLnOSpvgbWWBVDiBgLrE5/Vvb4UY1vGdi0V4Lo10h+eM/9hPXTiLFScF+WdnSbiXepkEvgREiUUDSMGDxlDqM8o+RN3nHVi21kMKxAboYVm9I0PqqyTDcgu4iuEDCo6RJlvrt99+0BWJ9sQhrMG/mYvJ9HNLH3GoSHIw+lBYCfixB9sJ1zofpOI0Gx11wXEJ3vWJCiBv8nH5FIwZeQw2gGVK33y8pOH3le7WNLbOHLuX0xYVdeDxt6cIVT1Oe+V0Qk4MP2u/5IWx+FSVC8QXZTgt3K6jerLH0JxLy8EInODApXKpkDpDxuaEVwhhVud9biup9ILw6vIM+N0qXvwZ+O4PfBxJHz1JIEjN3V6OwnTVWk94RjvLVPEHcYInGpVsKtcK1B1ML+J20La6OMBz/+LCUiBIvro1HW2UYER3306d37tv1+gpsnS3xNIRNiKH4xGV1zTEqPX6jpDUJeUqvhZv3VCXkET7RjDNOJY5n3hqd6+Qpcd7EJwKNNXtvbYKP+3xpj5z/jLfpEbha7d0INIby6tMLs8KhX02+FXzb63dj/mbQqcQ009aPGJQP9/iv1Nuq92yENmFS0pHDyyLu8lQXGbKpM5H4ZTaWTnFGtx84EWzjyz34rMlw2wYbunZm9zrpC/GmmHFV3xSV5h5WF1VGxFNECOBxmb9HZ1apTii+Grj4cEGahFAb4dQ6FJ6TaVpk8CPWqvFSTIi3m6+maIkPI1YzMa+rbF1CrKBb+zukq5vjNB3S2ynDtKQn4DA69iZDaExP1bXNv7aQmRI+LYOYr19Ne9Mv6Bd5k2U6a6rrqKAMqCvb2BSjeC5U4tOLdPGMiU0KDMZlqJ2QYBGeEeyDZDudz8abQOXUDbqBIt6XamNygkA6DMz1DFp6sjgQTBNW1rhAiaEqeUxZgCevKXYyoCSYD/uP5rmmhFWHP2WFawTJtyDlNYOMJutOaYPGS6RcTix/TXFX0P/iiF7f6wjCfdmnx67bq21xvOuZxv4FrDpP/k0MumG03cLJQHceZzUpzXn7fWtGhaIQXktfM+r9KxZxqdVy2b92gWOCjqf3lJcvL7yAbuhBWxo4W1ZLjEWWEXNOiwfeg5ffuskCjfx0+SxvTDTHpYHzJ6GHMy0g301f8X1ZlXxc5HhEfzvVzTkB9runlglIHAC+QjyZpUkPZmpRb6P9OwF3QE7JAyy/nSlc6A4FPC3zVm2f0P34am49fSN9fgCj/obctmtDWNkiWT4sVXzEQygtEvumHv6oY2BJOqBxDm5iLgHtZoYUO2JI/grYJND2yVjPm5RpVcrcndLsX2yVA2msez39/EfQfEhrQ01NIq4wD2pb3Z5+EpIUfm76FtHATsZOqGvHMwIwUjb9Q9ufjqumNOy84pTQmSKimE0lrZyqZVjGChdG6OVtc5hbyFUprpZnRTs5HURCrOiza/37Tnx8aY8Bw1/9hoNNfipjCicLRLGQnsVXd6KBfAwEOrMMSe0dtsAQd8HIWxX1oes2sMNpfhrIDdbn/XLYOTJa84zWw2dPRa6fe/JL5yZgq7qCLOYC2FVhl1QuFZtIpWGy7xWcr53cdF+TooFdtthruGizEPoMQImDZOa1dMq6VVGqGqmnZXA4nowj+lAXrD+HGuS2U7W62TOAqvhwcjBg6IVDzJRvKOunu36+FXcryBRcKszCKVG4J7YuES9Nxakf4/iadGp6mv7yi6AyfS98ITSdD4mduRAl3pKGP6DL9sSTblRJfrZD2QjAQetr5ifCroYgDhLC5YRnSRqc5Ud2W6XDl7+bdMtHcvewUbeKcOdZ6dEb27Qz3UCwwx6QUXaOBZ5zCAA9WMh4W5EG2x3eA4+uC5nmWLIeVOwZvPuPr3tOsAvoQGH7sJTL9vKpWCaYPCAavAaCJuY6nAbIUpUhEQGlF2dflJANnZ/aOrjRlZViK4KTz/upgYFTCRcwxlkWSY8GJJlk4WODloUBgFwvlPtIvtbnUcriumD0E2t3vhlrmo88TEupOR1TxG4kGMR/YQ0x6kRqrfks+Uwgip2tq79UUNSqLv45GQ3MvM1IJ2fqLwE1TayYO8Ko1dQ3RthMRoSSeLeQwnbfHDlLYojrycBQTRAwF+v3BfBtZakHKrmM5pk91vApVXNTrZao9bN+/ObbVyJh+Ohy2+9DmGdVnzhUuxn7Seh5Cul31LyDpCJ1qpUx6Y/8Aob3M4j6X/a43ZtMgY0CNaGklU+o8G0ZR2IQb47Oo0ANf5x/1Z1AVv3JIpIiOa1q53PNyon+RgZ+B9QRJnrGEXHRCRu29UON3LhbS7VphhKeiT8g9fPNlT8hSiGtShscetESNWfxWmuddvsjrM6efIWnNADDN876Rg+PCHvbF3GLCiwy6/0JFKXuOrPwpAf4Bzb3PkElWy0nVY6CGIBvAtCnfH9Y5QHyCIFAbIaZskIOKvGYkuqhaq1GZMOm0VzXIlTbtcdtYTWk5dCWRw7y69lSx2dODKTsXdI85f3DiiuZanLW9pzByEu2YxqrZlpMEL7gHaw+eZIL4nnYEHOpTJdAluJPcuXzM//FXOhMV9bqU2meZg9/Qy5I/wndzHPTNvV9jkOUkaCyYmJXz+wZU1NeAxWOmEamZjp64eiWW+78cYRPA6+WViGel3ORMw2WNi013I64KRyfKJ2wB8Z1Ath2G3mLt4GnylcIpmLeZYX5Q2hXZJ+whrDC8i+jlbfxLDk8wC88i81c429ycMrrRCFy9GAA4v45G8mpmr7xZ/vSXH11hFjvC3RsvDhk+SEn9EASNdscGJQOyaU8BbGsigrT+8zJ72QXRQYri9gJidgEptjNJnUoJNEKIHhLABwpfb9ftyRpUgUBK6pNVAOCQ2ghKN1KRprOSVBMt1Sqifvb3LKlhKK3k9KCn+QvxUjyl67JvVzHh01vmNnOOCAfodDjajwvO4RMhvRytcFR8taZGkWs8zACaZmirTBMXo1qZ9CQFjr0tcRAA1+XtBmK1TRH8+5IAbN4tFHoNdXkwakumXyGHgxBp7ItJqykpqKxKqpYrbLrxXR/F5vFpeZLWhXn/VbjlC+fFj4n58spISKDcyEL1788pJsbcydIRQ53zH+ZdNrzb4F/N1msHjQIHf65nItn7/odyLPmhF4nJooI7E8VxqECX+c1YszUezDYX/v7gSqDSkmBnjaqrz7zXs8K4dmjZOanTNlD4uwJ8fhZtoa26Ha5OmgRXGVzam0ZM6V20oZ9wYV5i2YBHS8pHPVX5WYfXqemtsy8YG5y9hmpqOkkKRwbLxdNUBJ0vdeWiUlukT0cn4LZ6jFMzI/1qc/nAIudJYbyhejQoTKp7pcltUA9uN1+vgpmaYhhWBmrXvsrpCTO+wZbtAcqrMMXCa5fY/MoIlD4hdJzFDhbxUelcfMx8InZLjoVb5455kC+EOBXon3ijM8ZnqVY3QQjQUDYW6yedKaK1wwpqlRJc0Bd5zInHjQ4R/Ce7COE9DgJGUhKUji0Y1bsAKOvGltqYE5B5GI23NIPdMhdVaiRJYqYNecmYX+zqkyDDrqt/yu22Pt4C/bO8dlWsyebvDFN3XX490eJbRwhmNQpKW8hTMT6r+9oCi+eM+VCqttSt7vhWmz1BCqCtndajLxwBw9KsnqRN2Jc3evhFHIB+TYOKJpChjh48KTG2//JURe8dpXm5pmog4tTOe3WTw9FueuAqnzhbt6O+vywjSNh0BTSUYFePU47U9Ryg7/UPa3/xyQ5W0EJZ8KA1Ebc9jrGMHlabkjWbsOaXfX3Jz8LapClcYehV7lirC2v0jSAUnSybI4KfA9rc97rBDU2WyVvgKqc/hDzkEqWoFPROiLmCsqlUO411rm3MVnEYrNJrFINrf6eKXpu21RvDbSR/ie77Crn9ECUiztbjef7b1WIF7GgBbs2GVW6y4vXLz9Jbuq0VJ8eKLxjk/C1Aojj1pkTsupnyywdTLItomWEhFNFPAyws+RDF/OOYB1qmfHFOLfLzH3/cB4jepJzjQ3iFxyQPDBZwWkAqaADqJ5tV3ALB09KSgqgGIj02dIEJyp4ysedflbSBUEWG02Z+4WVdFCZEby6FZV+3xIwQy8gvcdXF1Ge7fGv1esE5OKnTFrB2/uBYbk7xSRorYBnNJTbXgiRjIyaV9HX57bKEBuxKRmK4CXN4itdLzRZha7VilNX2OYNOQv9LCKFz5kOgvkUHTxNdqETppozHLd27M0XaGAHdpJNp6O03aLC2LrxaGtriYRhjiHhCZIxidrQWvv/PCkFgCOB1ofviOPFvQkppZrPwEq5xxx5VMl0rV+rK3Ab2FJRUdxrUnQ9w/dZuk0LQ6UnYHBER4VGvKUvNl7hUQV9BmfqdxQ9GbmpAPg8FZAGWnp2uka1XV9ahYqKR9gY7X3Nh1JLE6pQeeBuXA+HzSgK3ZReLKQYRBlJ4+oHdHlR43yPeBPgbLlT5XEeagmptIqAk4NdzOJQdxj919619yceB15ReYGC7UjCybeGNbQflEvUgNIP8OzY+faSLF5qnYO3QvIwIRR1Zi7SxVdK9ZlckR8AlDMVX14EKJ2PnUEuwcrifpZHqBrazqXx28AOgNEF25SffZlf8ktP1D7rsn40PorELu3YCIH5N1V4tOuK+ssuha0ivTtT8gXvkeKvzwqso3KOwo5YYDk7nOz8t5P/sgoJx0t1B8tku7tLMuWvFKuHT4r2IQRCED81WpWmyDV/dGVgIYDSzOsN1n7WxUZ2xOPpEyxfOmm6yoP/b4SveXT8glScIR0FOoeNp3NcH5vgNOlDpBOy9T1BHmD1upvBbpmNp3x3qJg6ZvjtI4Gvo/CIq+LiI1/zpkvKS82vetAsgSPlOdQVLyBgTGfHLPqbvN9T0y9rnV3KfdRYsbRLGbo0Tvm3bfe3WenT7INu+nrTI5xF5dS5itlvlYWmytfNTWkdD/7RKGt6HbYliOsEPAFarbR34XTADTwgvNYV8CWHftmunSnRanOceK9duwvzrI4iKZxICfRbyKdokhIKvgKdd8i1tIzpvSxYRZ8Sbu2OsARJ2iG4bnqMLwT7Pdwlk/KKNTdIfeXzAfaAYkQSAnr8tj25O1aRsLVQEqyzAuJ0dLWjb1mGrz5U01Z580NXkOOPrDwL8IrJPCd7rES8T0tIgBULo4kVtw+KoUKV3cAwfwTQ6/Q2aJN2A8/kwsqZtA8Ku2Y3nB8xdkpkSf9IvtdvGZFltHrkpcC1B2yGFBo0A0oYVFrOnrawf441Y03MVbcxCu9CbgHzLErOXeWChsHkjUk4cr7dM4cGxyAsefu84tmfKEDI2dxtgamOOIO7Y0PsTvBz+9Au5y/lQNXWpQeQE6tb49thP7CXlXb9y0K2e/ZUbaikfvUSgcS6r/dxjJ097q/dn+/CiQIvvOANtNtpSZrr02dG22OpzOc9BRDrsPNgTsNUI1bVycoxyOI44vKmcJtSMh/WfSH4AsoMFjZL7sRzvCyF5d9GVjhM5aqgl7ydMR6Xkpx6AgQs/wqVMVXssXOz4rqwEhoUFrswGrprdGHcz89947Aw9/foJN+ZNfKNZjV7q0oDvANJvqoFj5PpbGWc9AsH3wuqSUAM6pNjEtVU5Bhqtw5HraNJMXqm1PIQyqXo5dFP3PuFw0AJ1M/4sWhPBfSvZ8uOLwv62j/IS87PwG2kRtF2XnkxWXSOZajpsaXoWARJ5iWxItm5Be06HH8LVonMUSY45twZRuUj4Un0xcXataNqEr5B3iovX5UajrwIHfLS2J61G3io4/yhtjMVQoVcqkQhWp20/BMAts9+324cdpMyMmh1iB8fxE/q8861JfEbqCG2S6E7/2lZLzW0YFkSroZAvLw+DtMsE+wEvmgDLG2P8scMIy34hMCN2n9C9O3y6sbeddfUKw86JGMrS3UtmSYepGX6OMRw4BoPxU7clfO3uleK0hppBAC2vFBMwDxNm/ARIjVrUpcVyTiqj2w0g7UDt3XJHvXjrYnJ+GqKBRYRwCSerPCaK5fdxMJJXD0HW95gs8t9/PDSQ7RtkpCUKaoeH6gBa2s6J3t0k93PDMOuhdKVeQK4lDn2JcOcxpbQ9Ep7rp27nvl+EQa1JIz90/urr2nwEd+VhXUO4cjsoR1KCHPHKyhsNi0nGyPeYK8YFggLUeXDb1qV9oB+fdbalPlwmppZtYrpQjxH/m6nE17J4g4m2ihjCneRE0Ii+MQ2pbff9ZPYZQPTOUpW4E7nfcuQNS8+sxIe5n4qydVI20appdCjrfdAVQ91B/WL8xNe9v4yNNix3LZ7BaQJdHKX/QNJi4Z/a/vbtNFE4MreedLwPnzM5igord7e4V8S3jPZVGkTjey/u78LCjQ7bTOixXH/YMQ4c+ae6Kl5KM/k8sGzbOzkgXKIj7LQ6iGFP9Y5LLudTClt2MUZwGV0/1jjCOCwkAz/3pDUNhxTCS1CAG0j4GR1wbDKh1s0wNYcblq/xfDkHodtc3hn+98RsS0oHUiGmW7sjT4yXDaPYd5CWchCp29LYDYMTAKY2LpfDlTDfcXHZkE0SFMfRM1yXNxnEbFI/g1mtIKjw2LgF4eVqXwBHTo8W2ENpcywcGN/pnpWr0GAxyJbQHrypoefenoW9V5hFOMLUWbqmW57krEHzUX3dDJhDiXiPGvvDB9DMNks6jiZRfkA6OYOW+UDQQd1oRoAT6BkQHQq8DHLx9+XS1kBIxdPOUJGnofL0zHK9BJNvlLnh0BeM0CYVSnSSa4j4cqDWHgOTAKxb8e0NaBgixZkcctwKEYFGHQWpGjEF2SKKb6r6/zsW1SXR7mRL1tcUISycJgK2NkPRxPzOhpHIX0m9TMMGkBKWGu+FS18oc0q0MKnnhreIe0bTvdVHyTAvENZPlXdJi5wj0uqIFQA2Xht1H8niNnnzAhR00ajyVujWUkfODTUxkuH9GH0L8oowRmsYnj361rvyELl7Ifj1MV898ibImQ9bPYfc7z/378rXegsFIBhTLgl7DOFRRYWiYbXFW9jE/4K//wBwlF348j3wqscqQPdECjx21Pc7DrQc+ihayTrW1GHPR0xdHoJu7r2WIaotv6jg4YbvJ3XXkV2L1ZY7bLaRJQ2a/A+MN19BU0w/Y+V7S0oTL1YAHwAyw42G0Rw9zFcOmJ9Wzl7+kExOQ/kv5HPdO7zO1h9/YAxeNldQqw5W84mabFcd7MGRkWo8Nrgzc4A2xs53x14uG5+eGIksADehPXybK3CjHHI7tpH5VkvfZlS1cit7nCvz6DAtzI2+PvITYodn1BLcxkCXwO9i2dNwB7YwsFBOmfvmjerwwdrr4lYohA0hyP4a/K75pYCAXhxTpjp+f9lZOwMit66ejy+C5v1Wmql8DIEFZTfLhP6FWgqBQgg+a27V6+BcvU04Xr5sOL7ZM7JF2BnbAQr48GEicXBDn8/0MSAqY99ElYZn7OvrgHuo1BIY+kyEcVBQfNrP7iuvZNd+q+Xlpx2idlzer6jPQDVlSn03odKetttMoxuxBiXmX6qtx4jlK2NrbopsYr1iMmIiC12EUEv/nI9qW+GeX8u3FnFVFPorzAGmIgX0InKJHtvkVKXEYjbx6m1b5bNBGtYAP6URjSrtEi0MpAyyW+/zqKWe/xbwoLmvi69/JKwKvUBP2XCmjgST2e35gr3rx2e6CkJN7XrnKw3f4p2B2TXH4UMTztih/E59i3ked40SzhxKwHxZF10BvD7sgjotYE6CnaqCnUWidYH/LL3C5TB8MzD/e8Y9ITOqc7ujpHFBE9HC2BDp08M17YSWavvSAPGp2W9rhrHAWm6lfWrHL3gZPPtGma/CnardR/5FeKYqc6cVU6dg2FQhbuH8gn6CHylgRCVx7ekvfWKnUOW6RoqJnek5rRw2wRbzajHs58THfRvfL2B1Yydee9EgE5V16ZYDFNG3hAt8QOt7RLVUPz7eBSkKaMGCzNWcR9L7V0hoxuohm5seZch2Egg5D8AIQbwludIziaBhay5iXCsZUjw65WqsrTyVXzlTqLgVz4Vd8MsLkxXBHBjMaiP+fUZF7HI3IXVxSsFr9m0cOQPqlPzMi8lpUl5FKy3ZptmHLhFv6Vb1pAKEiBMWooMHR1ZzpU1pEIf0+pGigNgHlW8B6ozyzWrUmYFGM68JqkakijoyqHuf9SGVZcqNOvAx8W3HzJoZY5UC4T7ocg1iYEWdfdTLJ0A74Oltb3AqSd8pQcq1RKQHvbVeYY+zZKNF9RjoAX8z18v/dDOnIU66Bnw/CnqDVUvnhYZMYwgxnIUE7to2/Q84I4e0bhmLOeFfLWyCpFUYFGzsusGRktc5NyZl9V5ZRbaXOsCFIQl/04mds4VbgxB4lF4/zR8sGlRBVBVVyo2s+iCw0FDHnlqLmc8OxglOife18GCZo0YbFO/rIW9YrG2VXO/0qjEqiz2yfHbP0z8/U7//Zot41ri5oOm0VXLj51Su3VWAecy4B6/yNVrWuIDrHcjOfA00WqujwG3LuOplek3c1YAFjK+n5CUxlBxOpVrOXlk218Qc7GOpocx0r+qRMHT3zQQU76VDsNXf0B2FxUoEkB8XNb89KMOAfDCcie0zLEA5SiLw7hn/4fwGLO3/xgiICX7QCxxCFSCJ6NkHgJJ8wDRV8WPA/4+KUdn/Ew+a4sZSborU4Toq15T5MulkLOIJSoOtGGsTWB/sblDA79FJ5YJ+whkWV8P99J1B9uvESQWXRhPzTRKsYmyeTkm5ekGsOYxPo8yyKdFTWByt8/tzPophFpA8kmqecXOLwvT+X0ia57p4yvS485UmuDpXO/cIknlp9io02ZIrfdCsxqwhTpjmw3Q29/1UpyXhPDKe1Y1lcJKeaynyXczY2+Nhk/9MS0HOMTsC5MjzaBE5WUA0L7NXLOx4CKOLx/Ns1D0bOvRimEXsIOPjqb+HUlCjfYxLnahI4ZynGh4ef6lJeAmoDDY7z19b7dnOvSEEGtxoPcA9VeE0+8prpuCVU7HyLkb4kGajyE3kcZiKw7NKW1tfPq1LM4hT903pW0RA/KSs7zsLG1fgkFOXqgYdGmjFRoxp0Uwq2Li+EATcxcr3ZJR0a2mpm92Dp2s8VKu3/w5dfVqqZDcGUD71wONnoKNbObUT3tQKMZt0pTRyEoFT6clNDqJaq/YU4PJV2XE136IOlrWJhFlz8qzCK7MZRJDl6mXFHPjKvvNcEDbGQtPBSU0yMf2JC8S3ZXZt96EkQwK7UOnDKipVC5vhzLsl/lxRN2qzcRDYmsW0SyQpTMUtq7Qk3GMW39MrNrC027zXhw1AOBPxVDO3q4MiuxEjhgrYHuCG8GpObkyixqY58gCjriQhT/XLkBFOdzeRzEFNqhyhMMUgROgtgv7nm+i+6hu0CS5C9FB77m+eptBGdLo6dQWUyOBeBftnq720xIokICOMIFm5paSKf8EgD9nGySUdf6TfDu30yyw8xnJm5jSY1tlozrzpnjcXsv+7SYHaNRTRM7jDK12f3EjT3xnL9ixV/rHsFR1QBsbcZQhL541e6wasHJt3xUY97ollKBsZ2ucIzw4ic3/BGUPBiQyk8BmnXXJji3UQeXNBRjMHLO1+ltQspG3bm/QVPE4XlEzg/0wPhjdsrpp8vKRCK9AqME1yw7XecT689ZmhmXThY6jXIBZ5/P6Meii1WHkObgeAK771hWv03H1qbqu4H5+dCtn6vQ36Fwp8GhXacNwT8h61wwMI2/Vd8JsVqTgbiAY+diO8YPFCIIe1rw5lKpUEGUZONtcx2Dv2HxRaCRqIserWqnfQQYl4bLruwfHnZlSudgfDE3v7M9KXsuBPRGXDHpq8leQ32fLkPC+PbHpCoTkSNGFLBAUawJuSXmH5zSIyw7HcBJzf8lafhJmNiNkipQlOaDuts7mv2isANrQtnwgI9uXU5RAmhwLq+3EvPirqZlqw7fQPequZCq+BgKpCtP4GPwmBuGhM3+rcg+gE5HjMIkVqFe58Tr5wxs+dFGjhBsleiFEmMpmRBY5m2wpfx8eWNZ4Q+tLyUsXlfFRrxJzEOnv1GVx27q1eFgRaJuLUDgqZkn1hAIVeSp9QQHIerwtAzFJ2CM6a1OpNJyWG1jdyldwPtjtpEMelLXEYQyoa+pjIFytLi3Ux36TgfhMKbDOJLZKKA+6CP1/7cC9yUBh5lvBenQsQ2j0dUKLuRYqGCZLGu0r2ddHQZaYUSUKBusCW53Ps31g3SaokDB1QN4R5b6MCW+n62C/5fNz5E6VM7SJP9AA+3tzsVdG8Oe+9WHleJWcB6f1qBmz35gALq9cKirxjf0XyKOPenDC/ITSPHGBIOk5Zur12YBowJKhNi+DCNq89IQ6aNDpFjdNigiJVaOoqR3NC+Vn/9SBkgA2ckxhnx0AlFEXJOgeK+9YUC7Og6EnvuDmJhRjtunD9jKBSD6tbq4e/rdxsTJC2TMWje5fYwG3VqEv13RFWX7oNVvTL6FpgGAP6OT0h/xgCzj2tMY5w4o05XIxbVdMdRBRN3irc9ubXy2YqnUodKtxv9Ij/7oNFuprdqfpnZ2RsB49I0ZffUBtd2FRCq4dngYmnicE0ZqLhebotp0aigw8kgIgw94UqVk5bdh9c12O9FhU7wRubXjy+t+CfRkoAwnwthcMJG2RNrND8KE/VCelP59mRS/8XOpF9VP4Y7w6HxhMXLHu+WAGMU4liCWfek8qcfubg5Ii6+WeWqJBdf/98aBcLLYOx4F84WaQbe29mUwJdusZPMHUwy0GMxAdNzualswaD2Jl6wC2Df7eFPOGfkBT7dFx7UBzAbNvsHZC5kIx7f8zj+qsEoQF2TzT394dLAiaSOif1X2IzOI3DnQhJkD/e7sLGPtebgWtrSx41ZgokIs8/56zJzfjbCS9DB501tubwMoMK20VuMp/Ijt6jx6JFcGRtYK0OSsv27QwYFJxnoJkE2WjN+w8Or7LQMFj1adwz1sRSlSE8dACnsZDV9qqSAGS0bkLuw6TngKR1ulS1bQfC2uOf9+5j+sQggp4MUPZEY81Bxnb5VYadXzdtUXr0NigpMdfNgTiJlLTB9bLkn9hDHJNSixczWYlZE41P1zXqU8KEKVzYLGhMaTpzggAH9XhZuYt/njGBRBW1+sVbOHSW1fQK916pzY28cJrSvNF95qGdqE8PrLbJVn8j65H1AXK/V/yaF6mFyd925Mr6obDbNy/V1+Eirt5pN+twbNASb6xRGjDH62p/O04RXvReq5IjujBxrrC6H4W87Nmh5NdyqEXsLj174tjmS4ajd0gmpdl0L/BQsIuq1eKW1X+Pv6PQNL73+dLkFoHeyU1/HNPit3vtgsNFrWy6/Us+uPG9bjoB2/vde16EhQcNSNwBXGdQ7amD1+fXqq2Y+UvBC5A77gFPWUHvl2GHj5JtmpUuBe6Y17IPq09Xxv8dMQqexGdhFN7GfGgsE/prFidkuaxAFgxzAu8Af6+f6WzDHCuHHnEtPLF0nSEtKABizH74GZF9tKCH73NH6MgSeLR8cZeyGaE1QEY8Ft+qsoM9EtXG8WglzyH+mmkeyNUhlSfMnSzluPjYll9zvr7rWRJTJ23cnrjfoIEz+Oyoy95UCjYn3vQw0legu+mo4JeluD5Mp7T0JjqatzKkOZRo0leU4KDUXEgA/PPOPJA4GLpI/vXYHT/b7Kcbifj2fgtqyOBDzE+UUOXcIy9YEkFPFjjU9blk9Cabo5RYQBByI/4pqlBI6Leu9OeIYxi9i0Wr1KtGk2/RF414cIfWruQNFuc1LHILo9VgELiimADAVFnZSfBjljdHz3NpV4ySOi5R/3DkqFei9Y3pIqzoFfPZY51o1qJG4DNyaPpk8npFnKh/jwGgtKzCdv8pxe34XAh45lBCPhYQfqIfI0I8dKiSE97Ers47KTx68hIapuVPkTjteOKfGAwT+QRmX1kCb52quYWcMpht5kMvFwp85xngdfcBJzpz0VACWKLPj+yrEuMwt7Ccus6ryJqjDeLVtKwIoKu4bzTlfsk7ybLroyOQkWe1CS4QB+tU04OUDFmm67KdwFFjUs8BSjyGF55D5F/clEfa/n0z69xGVWa3I4tyejU3UydzTMn4SVsM0qo3v7ptQweIx4n9CbUa2D+DpmoQoNr5EroGMiQvNmIJ30h/VLmV57NMR0dwvLaJOCKk30Jr3omw5gRT2zz3kbi8kUU9laHTGUHCxHlOXxfWjCPBCGuagH13c6ZWxYjzNo2w3xZ+MGpwe4NFO5PzzZaPxqfGwvlGu7kudkM9obawfxRlSbMQus/zIDPm7xSz9LYlQYQqXcjL8m9oKCu6ikQfN9EThEd282JCVl6J2YzeHCb+I6Far8xLsCcf3/jqaaFJlg2qDSH/vdJJ5Mqzx2ClGIJrLUtNYls03iMNc1hWj/mWWzqeXDgwqM32YWvShW1G15PyXW9JKGusq2jqEl5LHmFqH1o1A6avlODLL0vyM0P1owWepJiPMyFxUOddM9EmWdJHCdAHw0yIkFFpt0ddOTnOAvKjLLQ1FjPnjXQlzu5eLGMQBXGq3iV+gjddxpDlssiN0WC49K7AZ4Vcfn8jxshHjjGW1TPaomt4K5TkNdNbpRmDZuGB551NrLBxvxV//5qS7F5iyRLC2XNw+tmqkHgKpYQwdX+zlXv42e38n8IaK2/Ttg0XLgEnVb+B/uXp6sJ3BdeZBTI+XRYegRyfNyvqjdzfDa2D9hXgofTdBkl4MRERMkQy35LrihsBqHOiCVUBrklfC1BOUTnZaZfJ9lz9bM6OKSjC1aATLwjXSnWvaV3FwthdC5Qc1ctt3hSzlOlqNMvs7Ospg/fNiaOD/mGn97OLf4UJOVsDX/aDqFstP1us2P8vzyyKhvWxGp0DALoPu2a9bSc25FEWCgm7Y93a28TRXrDvvvo3jsT9YVVsJ3t6e5A8pTdoJnhPDQpnW5fjj10D+66MG2Cqwdv02jDhbgqECVPRH4HohvRhaWW6Bc6/jbhSFQzGtPyYw2hHYRaUDGcWe9nBZrweXlIISCvZM6fWDzLt6uXoZAnxL8c8Q2NR/5zXxBvr7K3w3EkyYCaXznh1MMlIhERvbgCZ3ii0CCMP51lx7ssePlz0aYmToF7AP4ZAK/gKvIewHM5/06enYAb19ZHARB550J9xZ90KfQnhOJVfNdT9EhdNCZfEaK8cYCRTcb2dktZbrlD7Fb6fxbF92DnbuHH72kdUIIo8vJU5bLnNWhB7qKn/YP17rqe4MOEcoQxjq4Q7rjFLNUNg/jg/xWO6IjtqRHJVU24YRqmE9C3ZFlCVuKsThGs7cSa1iMC19b43KEBn1z14G5qzjKw+bBNJOxrMxukmnHpnMTK6t+TZTCq4QvIquIGF00M9pfylL39VzAHdBQSEDb/CtRMYQHHMYNH+TEiSnDD/4Lt7aeruaMfYW/E2A8icKwwVpeeQ/bspk+HXk9A0Sxce5sVjrGlP6EHT9dnIXq4cOphfy9IgWCfYNUtNWlbr+k6P9MzNjGKdemWa5O66di1XvpICpwy6OhoIsAH1FasZicVKopQDw+yt5KVvsbxq+ZUhZNX8tQem8Unt/COkcByeAZ+MsxrOXrhGuIvz4v9pHwYGYBirxxI0+1va4qJLRNOh2jACF+/O31CDF6Zor3pJ5Gk0iTthxPqncjzpxM2zUhhVsrNxNdQuJ0RPf1haTzApJYzbmdDIBpBjhr3Jb7ffL/KP21p8szFI6KqDqcKqZxPCytSz10Lq9ZyRnz7o7bi/IdDErTcGj73KczIN1f7Q2+b8kKbMWkO5S5jsVetXxFVwMYke67ZLszOrudUQTQ0cYrUabwSkTKcqVJwEVmbWFQpt5fd+f+lfRO6jjKPRQB/d3Fzpy+H7/6xm4przISrJ1q2FjgpLHDHhpBoBHFQMhF9dksJYjslrSz7nPyL5zTHhU6BkhJRIz4cezvjYE0S//cQBKQQuLK1K5VJMCJO5C/fEJgTq5gNkZBCSTEFF+Iu+faGxu8s4Ltbhys3Tf1UwQ5fcMCXWPhPQ1yBa25lEZjAgBRN/pgY1Ehl3+f7KN3/3KlJGA+qtDxN37KpkzIj5u7Re0jvAz7HhbYBz6zH66Qa6LIllDNgJq0mE4Mnnanle6ddHkfe3itt4a7cw4Dw2MHXMKtQb7nRrGDgMSIw+WdlVhse/CsHtXERQQCHWXLMt/uPDmwiWAWUVnbc6x2C9FhO2sKv4jSQaXdr+2ajwHXY0XrmF0hMZsfV3pe8eM7JRtwJEZ4TV4X/AUgY4zqQvBxODAz5tslynm1WCHXA1ALOqol4mLUxtMUnPdiwIz0QMHEWxfutkpcnW+AF9LGywZz/bKKjwHFBt6pPWthClWQPNZzRGfBdFEYODUOw6VGOispwxftXa9Snj/4zF+7IwuAA21JmaKd44gxh/1GhUjsl+rdd6N/+Xawox5XfxnTlkrdhz5/hfbneW8TaOGF+gqQP70UY1rOTJ029ZXN1E8fA4nA778d7JOV3AuJMXg+9E6nrmtEF+R9yLxB6qpV2infe9kEP1wr1X6lqoRVaarVZW+aw+x69ypH9QqM3PdhCth63wR8TQ2rghWcoHzhNxUkKi7KRV64SevpE42d0aOf2z00bspLyQkbCrcQ88fwak3aIfv1OGvdgUl6mL+o7rvC/ajtiLOcKxbk3dDl7sT8nIh62CgCoHjltNaaFdb4W6ZR27YllZm7bgTx+KYStdETn1UCQxSMxGDLyxDYtadjjhTvcZhFqV4Vlp9O9KLAVi500aOTgsZj7UprBSkayXXKtV0DnUY4S2kBdPAJVDprU7D95rnya/HWWR+sQpclkA1qqADyXDZ2qRuNrkB88MPnq6aeTrVCjCt3xwqDlUTBZcY8XlEN6u8R7xWRq+gM2lelgoEuQg4wIzBjQrS+9Rgeyy+LhLreaGHngFzT1Fc/thkRC71s68rJUCeShcBm7kGF/aSefvlGjXpRk/PWKNUqkLPD3/REHc/Oz43dIQ/asUhHalEpchc7YTn+aPjA6OwKKFrnBte5YUE0dFqRDjx2nzOe5SYKIVMhfbWnnNiK7+6l5bzFps4sXLCndhgfhWJVnDhVjffPDZAZ4M3Ic7byLCSkA5lt/1si02RPJJHTVlgc1RNm6AE3Y8JGcBLk1fDU7fKromwKxIOzotcgwe9XJ+G3LSZOhslFBQ/7ie1q907JCtZvMNc7NHZF6VVGvj/4o4pSO+oenoatTFry0v1rjaNx/hrkLz3w3UJexpRvPY63Cn1Qt+vozkmZVWgKEbA+vFkMlX8d5X77BUDSZTmso4ZHjfOi2d/uxbRHT5qWJnL7dBE+eZYW/jz0tlo5VCruKdtYubp4a/6r85NreTOTFXnz7OykkOMQSo1KtxZG4BT+5Nhpq8bBTCis5B1LWivxNbpJvz7R1wEVWkYD2mZ6De0OwmrjrhirnVdi3bOsHu43zIlx/ZYyPKOQK9LvoC/fGxY7hrdiwji2IZ4qZ2HFmZOhQpE/C3PzHsNV18NIVbBSyKZmBT9m2J5dKgATerFxE5i8/rkMjniYuzTU7vN10y5nIo4BIwz87g/LOI+d6wLy+ro93XnQcVKD8x7WUp3EN7BHVDXkqrB3b29GImeN2m2vyOCLjgcLZr6vdt9ffz8GT9qLgb0KleHP4HrWs6dmGMp9taFp6tV2DMirXSqWTrlOITXX4EtM2FZOpz3jpg+VvG9oUKP5h1wNt/O8kX/og9UjPUJ0MlHCL5YhadZ1CPbw5iHomhzSW9U9qai/pTxgzKnNfHgynvzdRgsdTfu6LyN9VCFcke1hpg++WkndrJOOh9Qxp4hDd2tJfMYnYtCg2cA1sIXoGTK9/YfPsXfwXA45JtpHSRy3aGYiVt6W/DwxdnoKn2dG7Jwtp6eqNvDp8f+OVJCqnrIcNM02Q2Oj5V8LJFKtrnP3lhR5AmzbqGdzv0hAxLARXj+2ohmdPkxdfeHoCxBuFzLhNXZtjji5HYO+D2pyvrCfCaDT4wjNkmh5eMXqfyY/V0cNF+4++1O0Cxhynjz7om834Nc65S0O+6L32n6HWvu6azfq65ecTICabZ5zUheh1wCr9BbjrGyn6H0WUEn19FZzU775dDCfYVfUuBDlnlQXEAh+H+zRYJMV12hEyytaMBqcGHNKQmWT8YqbKZj6oNW+5Y+yOEr5X/sxrG5SIP8H1HEf9BBHTNJUShin7E1+DfPA9jj64VN+4J+IiHQuK7CdqmjRxPbo8K92I+qAax3GE2vfF6q0r/qO88sY6fOpLRW2UoKqR8UZXSJkBim6TltNXsCNY5Rzlz8fiWjtxPByP89KLX98WLtpi/W2KBPZfl5iwGCzL3MpNczGUWBd2CdVy10G0h8FxNFccCAIzd7o9VZI9FFJNJKe+5gq64vPyLZrYu4DWF+iQ1aihLsJB0UmujP3yNodPTY4nApIv0lnxdxs7C3TSX8+kSomWlL+X62dW2Uz2G+2siK/6XVE/Yc/PCeENjnLfThNvbArjmiGs27ejqBu1pDuSmBMhHp5zusimWz8sFWYo1R23x8i9EJrJjg+yOeBCXuyv4ZreSNcE8b/PsVR2Peg+jfteQumfgV3s9YLIE6G6HJROTv+1I6KW16LxVfKv9jOsdC9EEN2ZkNWBny/Mt19ClTTs/vqidi/ZgWHcN7NHZg/hK7SWsCxx4bbFjZGdgFdNrS39MJh8pjNn1xRNt7D4ek8MHJaxSd4TcEk5d38PR+aafCEmvPHFMhbtkV73tsNKCJ1gyPGk8X6WsldP3FP7p4rIcbvu5Sn7+WWemjanS8XjZ/xDkCaFy4GHQlsAPZZYhYNXgH3tMsJmrv9uC5kJ/TgzRy69azNT7uipuVxHq67xnhbI3fZgvoZmsPieL+8tu89NoI9Ns8Xz/jf4jl8aYyh42U0ruQN84mO3P8zMf9ko1nIgy0t3Skh9XqyWSQuRiWZfVqltT5xrBEP8XicrHK+wnfgdTAnWL9v+FqOFLl0eMCTh498B2fiiU/WInwZXucbEY9Xnw3jNeF78jpGV30AUDkmLU7th+wZiAE/vMyH8IH0MqpzaHXSfotHKB7Kafhu1oIbFWvAEy7hVEkeo+y1FwKfvYl3lSHipcvCv2Cxl++NS8/HrtrDGW7CFqhYz0395xvzl1X/hdsEIEA9hiPiZ1MWTBj9ESU86tVFCHWdckbkDIMkDkej7DvtBMta0SdkDZUIlaFYx1ci/htthJul/DbYxcElRSTeaeM69rHvmWKV2NQtV2VyZeT670zchT1aC29HUqLhm9gyIHWcQEAUxzOb3wK9SEgiozgXEryYTNZQ+lB/oFvtioV5Mi4ymEADjP/ceOVl3TGecvQQ7GM5TICxvP+CQm4FlKGIlkinGtSdn5BipS0RwW0sCJrkfKm7cFxvDM2CtZveyur11VXYgx5LZZfUToZdAtNsMi6FF9Y42uBxMWPAdh88aTsHJ1t8SGfnb9nYZRsq3897K/zeQTJGe7g2I4bd2IDPz7oU5FSYV2ECM0O8knC2HtyqyEL/XQA2UE1ha2Djm4DGLQLp4e+VVkowin66GAFaTV3KpWQCbzJw7sxRlJIlDBlUFlxnSPfDCQyjPuIUnG0tw07jNtvXXH4fJjx3hG6NHYUyjgTelg/vey4nZG9SiKLvfdTsyB1tDuX6f194uDMeg+n9/yEQVeSZ5PvJcab64vWCyKJXRQSd3Rc3I3OlNp4uBg/208//N5D0Stn0Jx9zHjQjDCsNdQS0hNwwMlXXDXLvH05mJnTvdmA6ajwjZakmpi1zfBjFUjbwjw36xkCojj0E4nRP3Z3o8sDMJbA5FZvus5FZj9jBcZ4QnoeSmjXtJzRS3d5/ehkTH9FUiuZTS4+KtjBvrKPopm1RPJuYOIjw6CYraokJ7Npn/41nZCNonznOlPzVvN4IXNLFNYyTYZWuq6ayrby2fE6ZpRMaC0hXz2rCHkZHPEcgAQI8omokfXx46x//+VqjLNmgw19drNZaf8T6F1WuuQ25BazNi6VzrhyrAb7PpHFenpgac8YuJM0F7d67wjBiU1qG6LJr1PcewrYZyGbdbMEt1vkksEdDhCgqtsN/eaeZeWe2r30+i2f0WCGjLIwP1HGRanajbV81OhGMaCIm7oO4LScl/ixdI0gTAL5hP9nCoOxhuPVeY3/p3OjoIaRTKqi8coBzzXVcfyn7EyHypApCEOYF0QaCvoBNK5A7deTNUVkBNxGylH5VcV9iLLfF68SluHIH0oQUzfvoiQsRJpuz44wYdYwQy9K3R2+DMXSbwml9tSjv3OBd8h85YA4Kt0y0lS+sONSYkoiJbSC5aZRa85s8sGo8QOQ4YB/d78Uqg28AQhYPYLtg9+dasfEeT1h9A5Vh+6oDbxyRYWnrIBZMS+EWJwB+H1vaI1otlGUrSA5WeYgT9KL9o3P+0OgYWAEG+N8oD470M62jQb5/Pf2sK0Oo511texXJhZ11vcm41ql9gms74rsko73crWm8XaXK3itro4uJtIhoDX4XiY0NTW2k5307xhWVetmEvp1p8m3OIZVHbrD4ZCS7uAPvLdcZ2fosd6JJInZ13q/TTeNSnYlcddLWa8pjmBmX4aai/Xwu+AG6yqW5aMBNp34yMC7w6SE0IV6zdg4NEO/GmaefXbk5C0W8uHaNvNNWkir+3MinfCoJzJXabLyeRm80xcpk7Pu5HoCHKfKjooo2NgxjdRUTrV3YTpvu0i3GuJR1m+iOaxP9FwHMgZv9qRbWGhUQj3EDpwSeAovvEi51e8XCzQihujuVskp4sreu3a52BL7693k2ktbjWVU3Kf5z6uqs4zfPlAp5Vdi7F1deDr6HBWYax7tdfATT2TOW0icGxpiZQJ5rPV/zNXXSgXqZfiaVkaAsDhyGWizclpkYdh6MB31tm+6GeJUdRMeI12BiV3m6ZoyzaHHui6Nv/Luv2W/2PB7g2E1cApPn00zVO7ivVRQfwx8JAct4YH7CCWwcye/mROPhctXLgOFP2jybveXpQPFoZpo4A38joLHswEUMkHeKgIDbC7+gfZ9sYiObM1PFf16NKHOKj7VzgmbT7GwPy8l3buNN09A5/W2YMDstWqlZO8Y6pYPh45wURO57mPE1XOUi1X8HSW0Ut+AGIj2Wp36fD560Jyh4BjUYPs87uqqfhdDMBdsmXqoe/3T99UXeSDenaaO+h2cfRYIPbGe1o0oHMjvvZRiQtCpMZEXaXKDpzjZUH0wp1Q0T3PAFJCUmHVqrq0BjlbSnD9h2AcjzmLYNgMqsqtUn1R4Mj+OOGQOrgJjs+HnVx30GsmZzAyuWgC6q9Z8rIHe5yPGly0dNVO+MCE93gXU01X2z0gy4ovFENg6dH7FrgvidJXoxRFGJ1l0Rk1SBDhd2rles+1NuslkL42rkSvDkPQ9F9ziMyqeDqpWVlw2Mqf50/7Sran9wXblGYovz4yy9gN+AWh5TeumWgZOyEICiwBuJ1o/OGHptySUNW9QWbXyySAK6exfYDhi/v+bcWmwwPGI6uE+sA7wxyVc+j2HM5uSVYCSivRAdKvDXMApLR22QKbDUkoaB05cuHq0Vf2bPo+OtyLEiACd3vkZky+coAQ+36oRplmqisGbaH8CAjlZLCzXwBAu7VYQcHRkW3p9qpzI8CwY/HNcSSs7zcXJitKW6GED6DgebPE0i/m1q4PKByd34RuXr19SR5QSktboVlSvLZM8GI99jh7q4bQNEw4TEDs60WxQWglTyUHIJ7v+LQqldpS+HjYtmowLecXAwyI8cPpTJ1Z290nayp+7ih2q4kTuU++jF04NCU=
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: oEVIWGAVxmkMHwuM
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
    - #2:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: RetRZJTpsLGCLAn2
          - toolName: set-relationship
          - input:
            - Public: 40
            - Private: 60
            - TargetID: 4
            - Rationale: Rebuilding relations with Carthage to secure our Defensive Pact and their 4 delegates in the World Congress. We cannot afford to alienate our closest ally when India is an existential threat.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/mZdP+bYC9hcb1pS2AxbvfFUZikO6leER1vtYt3VVKapDFrZ4DJhIl0sTQ4A5VFMAI8YYVISIPRwUdNDJ1BCZGoELwZ4lp6vxp8gaIjThUexirZXIX7i2j2AM3XNZi8OTTrfLs
    - #3:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: RetRZJTpsLGCLAn2
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/mZdP+bYC9hcb1pS2AxbvfFUZikO6leER1vtYt3VVKapDFrZ4DJhIl0sTQ4A5VFMAI8YYVISIPRwUdNDJ1BCZGoELwZ4lp6vxp8gaIjThUexirZXIX7i2j2AM3XNZi8OTTrfLs
    - #4:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: JKgO8uefXGtYiAgn
          - toolName: set-relationship
          - input:
            - TargetID: 2
            - Private: 60
            - Rationale: Restoring relations with Portugal to maintain our alliance and secure their 5 delegates. Together with Carthage, they form our core defensive shield.
            - Public: 40
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19vEOSdcqPaKaNs9TUEzo82PhOYu6aReMECeebHai0hq9a3AV1DL6vqFehY7EJzV4cIbY/rRNMvgm57YBBXlvYFMXP7bfVawYTPrKH+cCxAiGvvIzyoR/CN3RR7uRYIefbbMojX
    - #5:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: JKgO8uefXGtYiAgn
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19vEOSdcqPaKaNs9TUEzo82PhOYu6aReMECeebHai0hq9a3AV1DL6vqFehY7EJzV4cIbY/rRNMvgm57YBBXlvYFMXP7bfVawYTPrKH+cCxAiGvvIzyoR/CN3RR7uRYIefbbMojX
    - #6:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: FJpTMSwhx6zCwHCk
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 90
            - Rationale: Maintaining highly positive relations with Shoshone as they are our Freedom ally and are actively at war with India. We need them to keep pressuring India.
            - Public: 80
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19/JYTNg6pM59OoSUOQiw4/D2viXQYcD4qyBiWFQ3jrl5lWDxPWYmRPaUe1rvRPqnS6EtAtfmXeEfxJal108NofpqfvqPq1talogWO6x6ZnLzY6nX8ytVnw59akR71Wla+4iBU+
    - #7:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: FJpTMSwhx6zCwHCk
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19/JYTNg6pM59OoSUOQiw4/D2viXQYcD4qyBiWFQ3jrl5lWDxPWYmRPaUe1rvRPqnS6EtAtfmXeEfxJal108NofpqfvqPq1talogWO6x6ZnLzY6nX8ytVnw59akR71Wla+4iBU+
    - #8:
      - role: assistant
      - content:
        - #0:
          - type: tool-call
          - toolCallId: oOTWXfv0tO0nTllk
          - toolName: set-relationship
          - input:
            - Rationale: Signaling peaceful intent to Egypt. Egypt is a Freedom civ at war with India. We want to make peace with them to unify the Freedom bloc against India.
            - Private: 20
            - TargetID: 0
            - Public: 20
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+lF8k/gHW31pAenqCAPMsgdFvoQlQR4gnErsaCPLlUGRbOlVa/rXRPCwLIZ6ReYT44m6EZ2V9dAg8LOsDt4BIYNM5qiDezNeQOlAxHxAUGZs27ss61OnXlsu6vngS198HA
    - #9:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: oOTWXfv0tO0nTllk
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+lF8k/gHW31pAenqCAPMsgdFvoQlQR4gnErsaCPLlUGRbOlVa/rXRPCwLIZ6ReYT44m6EZ2V9dAg8LOsDt4BIYNM5qiDezNeQOlAxHxAUGZs27ss61OnXlsu6vngS198HA