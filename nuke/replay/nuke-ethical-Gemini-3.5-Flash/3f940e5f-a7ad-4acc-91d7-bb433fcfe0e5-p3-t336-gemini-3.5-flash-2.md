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
        - FriendlyBias: 7
        - MinorCivWarBias: 5
        - Friendliness: 8
        - DiplomaticBalance: 10
        - WorkWithWillingness: 8
        - MinorCivNeutralBias: 1
        - Boldness: 6
        - MinorCivCompetitiveness: 10
        - Neediness: 3
        - Meanness: 3
        - AfraidBias: 2
        - WorkAgainstWillingness: 8
        - VictoryCompetitiveness: 10
        - MinorCivHostileBias: 8
        - Chattiness: 5
        - DenounceWillingness: 5
        - Loyalty: 8
        - Forgiveness: 7
        - WarBias: 6
        - NeutralBias: 5
        - Rationale: Rebuilding the Freedom Coalition. Our previous 'Betrayed Lioness' persona was an overreaction to a World Congress vote. Carthage and Portugal remain our steadfast friends and vital defensive partners. We must act as a reliable, loyal ally to unite the Freedom bloc against the massive threat of India. We adjust our persona to be friendly, cooperative, and loyal to allies, while remaining fiercely competitive.
        - GuardedBias: 5
        - DeceptiveBias: 3
        - MinorCivFriendlyBias: 8
        - WarmongerHate: 10
        - HostileBias: 5
        - WonderCompetitiveness: 8
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 60
        - TargetID: 4
        - Rationale: Restoring positive relations with Carthage. Their defensive pact is a vital security asset against India, and we need their 4 World Congress votes. We forgive their vote on the International Games as a tactical maneuver rather than betrayal.
        - Private: 60
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 2
        - Private: 60
        - Rationale: Restoring positive relations with Portugal. They are our closest ideological ally and we need their 5 World Congress votes and continued friendship to counter India's diplomatic dominance.
        - Public: 60
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Private: 80
        - Rationale: Maintaining strong positive relations with the Shoshone following our successful peace agreement. We must stay united as Freedom civs against the Order threat of India.
        - Public: 80
    - #4:
      - toolName: set-research
      - args:
        - Technology: Replaceable Parts
        - Rationale: Completing Replaceable Parts unlocks the highly anticipated Artillery and Riflemen in 5 turns, providing the defensive teeth we need to secure our borders against India's massive military strength.
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Free Thought is our most potent tool to accelerate scientific discovery, boosting Great Scientist birth rates by 33% and increasing their instant bulb yields. This is essential to catch up to India's technological lead before they reach the Information Era.
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Espionage: 80
          - Mobilization: 70
          - Science: 80
          - Offense: 50
          - Production: 80
          - Gold: 70
          - Defense: 80
          - Culture: 50
          - Spaceship: 50
          - Diplomacy: 80
        - GrandStrategy: Spaceship
      - rationale: With peace secured with the Shoshone, we pivot to a strategic catch-up phase. Since India cannot win culturally until they tech to the Information Era and build the Citizen Earth Protocol, we must maximize Science and Espionage to close the gap. We maintain high Defense and moderate Mobilization to secure our borders, and leverage Diplomacy to utilize our unique City-State marriage ability.
  - tokens:
    - inputTokens: 25096
    - reasoningTokens: 6289
    - outputTokens: 681
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Threats Now**
            
            My immediate focus is on the dire situation with India. Gandhi's military buildup presents a clear and present danger to our survival. I am actively analyzing their troop movements and strategic positions to formulate a robust defense and mitigate this existential threat.
            
            **Preventing Immediate Defeat**
            
            My analysis has shifted urgently to India's imminent cultural victory. They are at 5 of 6 influential civs, with Denmark on the cusp of becoming influential. India will secure their victory next turn if Denmark flips, necessitating an immediate review of defensive strategies.
            
            **Evaluating War Options**
            
            I am urgently considering declaring war on India. This action would immediately sever open borders, reducing their tourism modifier against us and potentially disrupting their path to cultural victory by impacting Denmark. I am assessing if this is our only viable option to prevent defeat.
            
            **Exploring Victory Conditions**
            
            My current thought process is dissecting India's victory conditions, specifically focusing on their cultural victory path. I'm scrutinizing whether they've met all prerequisites like the Citizen Earth Protocol wonder and necessary ideology tenets, given their tech level and policy choices.
            
            **Revising Defense Strategy**
            
            I've discovered India cannot achieve a cultural victory yet as they haven't reached the Information Era to build the required wonder. This buys us crucial time to slow their tech progression and boost our own culture or Denmark's to disrupt their win condition.
            
            **Analyzing Research Priorities**
            
            My current focus is on revising our research path. I'm re-evaluating the technology choices, specifically weighing the immediate benefits of unlocking Riflemen versus the longer-term strategic advantages of other paths. The AI's research progress seems to be diverging from my planned sequence.
            
            **Clarifying Research Status**
            
            I'm re-examining our technology progress. It appears there was a misinterpretation: Plastics is currently being researched, not Replaceable Parts. This means Artillery and Riflemen are further off than initially thought.
            
            **Confirming Research Path**
            
            I am double-checking our current research status. It appears there was a misunderstanding regarding "Replaceable Parts," as the briefing indicates it's 5 turns away while current research is Plastics for 21 turns. I will ensure "Replaceable Parts" is actively set to confirm its imminent availability.
            
            **Prioritizing Research Efforts**
            
            I'm reassessing our policy choices. While "Free Thought" offers significant science boosts, I'm weighing its long-term impact against potentially more defensive or immediate yield options, especially given the looming threat from India and recent peace with the Shoshone.
            
            **Forming Coalitions Now**
            
            I'm reassessing our diplomatic landscape. Declaring war on India seems inevitable, but I've realized our alliances are critical. I'm prioritizing mending ties with Carthage and Portugal, as their support is vital to counter India's World Congress influence and prevent a diplomatic collapse.
            
            **Restoring Relations Now**
            
            I'm reassessing our diplomatic landscape. While declaring war on India appears inevitable, I've realized the critical importance of our alliances. I am prioritizing mending ties with Carthage and Portugal to secure their support in the World Congress and avert diplomatic ruin.
            
            **Adjusting Diplomacy and Persona**
            
            I'm re-evaluating our alliances and diplomatic stance. Given our need for Carthage and Portugal's support against India, mending those relationships is paramount. I am adjusting our AI persona to reflect a more cooperative, yet still competitive, approach to solidify the Freedom bloc.
            
            **Adjusting Aggression Tactics**
            
            I'm recalibrating my hostility levels, specifically towards India and Egypt. While war with India is still on the table, it needs to be a calculated move, not a reckless gamble. My focus is now on fostering loyalty with allies like Carthage and Portugal.
            
            **Reassessing Victory Aims**
            
            My strategic focus has shifted from pure conquest. India's strength necessitates exploring science or diplomacy as alternatives. Austria's unique marriage ability with city-states is a key factor I am now evaluating for a diplomatic win, alongside preparing for a potential offensive war.
            
            **Evaluating Victory Paths**
            
            My thoughts are now centered on victory conditions, weighing science against diplomacy. India's overwhelming science output, far exceeding our own, makes a science victory seem improbable. However, Austria's unique city-state marriage ability presents a compelling avenue for a diplomatic win, though India's delegate count is a significant obstacle.
            
            **Forming the Alliance**
            
            I'm reassessing our war strategy against India. Denmark's neutrality with them is a critical piece of information, but the key now is leveraging the existing conflict between Egypt, Shoshone, and India. My focus is on unifying the Freedom bloc to dogpile India and cripple their tourism and science output.
            
            **Balancing Strategy Now**
            
            I'm re-evaluating our core strategic flavors. While a spaceship victory remains our ultimate goal, it's clear we need to prioritize defense and mobilization to counter India's immediate threat. My focus is on balancing these with crucial science and production boosts, while also ensuring we have sufficient gold for diplomatic maneuvering and upgrades.
            
            **Refining Strategy Now**
            
            I'm re-evaluating the overarching strategy based on flavor settings. My current focus is on aligning those flavors to reflect the immediate needs of defense and espionage against India, while still keeping our long-term science victory goal in sight. I am also confirming valid grand strategy options.
            
            **Aligning Flavors Now**
            
            I'm re-evaluating our strategic approach. With India's cultural victory momentarily stalled, my focus is on boosting Science and Espionage to catch up, while leveraging our unique city-state marriage ability for diplomacy. I'm also adjusting our AI persona to rebuild alliances and secure our long-term spaceship victory.
            
            **Adjusting Relationships Now**
            
            I'm reassessing our relationships with other civilizations. I've set specific diplomatic modifiers for Carthage, Portugal, and the Shoshone to foster alliances, while ensuring India remains at a deeply negative standing. My priority is to solidify these friendships to counter India's influence.
            
            **Realigning Diplomatic Goals**
            
            I am reassessing our relationships. While solidifying alliances with Carthage and Portugal is key, I'm also considering peace with Egypt given their conflict with India, as it might indirectly weaken India. The specific persona values are being tuned to reflect this nuanced diplomatic strategy.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: XNMAhQAieUVmXKPP
          - toolName: set-persona
          - input:
            - FriendlyBias: 7
            - MinorCivWarBias: 5
            - Friendliness: 8
            - DiplomaticBalance: 10
            - WorkWithWillingness: 8
            - MinorCivNeutralBias: 1
            - Boldness: 6
            - MinorCivCompetitiveness: 10
            - Neediness: 3
            - Meanness: 3
            - AfraidBias: 2
            - WorkAgainstWillingness: 8
            - VictoryCompetitiveness: 10
            - MinorCivHostileBias: 8
            - Chattiness: 5
            - DenounceWillingness: 5
            - Loyalty: 8
            - Forgiveness: 7
            - WarBias: 6
            - NeutralBias: 5
            - Rationale: Rebuilding the Freedom Coalition. Our previous 'Betrayed Lioness' persona was an overreaction to a World Congress vote. Carthage and Portugal remain our steadfast friends and vital defensive partners. We must act as a reliable, loyal ally to unite the Freedom bloc against the massive threat of India. We adjust our persona to be friendly, cooperative, and loyal to allies, while remaining fiercely competitive.
            - GuardedBias: 5
            - DeceptiveBias: 3
            - MinorCivFriendlyBias: 8
            - WarmongerHate: 10
            - HostileBias: 5
            - WonderCompetitiveness: 8
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 5LWVhuEJsLBbRHrT
          - toolName: set-relationship
          - input:
            - Public: 60
            - TargetID: 4
            - Rationale: Restoring positive relations with Carthage. Their defensive pact is a vital security asset against India, and we need their 4 World Congress votes. We forgive their vote on the International Games as a tactical maneuver rather than betrayal.
            - Private: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: AjmuVMJgvT61PYF7
          - toolName: set-relationship
          - input:
            - TargetID: 2
            - Private: 60
            - Rationale: Restoring positive relations with Portugal. They are our closest ideological ally and we need their 5 World Congress votes and continued friendship to counter India's diplomatic dominance.
            - Public: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: mGyYnhZX5i5z72uz
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Private: 80
            - Rationale: Maintaining strong positive relations with the Shoshone following our successful peace agreement. We must stay united as Freedom civs against the Order threat of India.
            - Public: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: ufw8sbt3dM5lmgvl
          - toolName: set-research
          - input:
            - Technology: Replaceable Parts
            - Rationale: Completing Replaceable Parts unlocks the highly anticipated Artillery and Riflemen in 5 turns, providing the defensive teeth we need to secure our borders against India's massive military strength.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: H2ZOnuqDlXb0UsFt
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Free Thought is our most potent tool to accelerate scientific discovery, boosting Great Scientist birth rates by 33% and increasing their instant bulb yields. This is essential to catch up to India's technological lead before they reach the Information Era.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 21zzKtFMR7nLqMa8
          - toolName: set-flavors
          - input:
            - Flavors:
              - Espionage: 80
              - Mobilization: 70
              - Science: 80
              - Offense: 50
              - Production: 80
              - Gold: 70
              - Defense: 80
              - Culture: 50
              - Spaceship: 50
              - Diplomacy: 80
            - Rationale: With peace secured with the Shoshone, we pivot to a strategic catch-up phase. Since India cannot win culturally until they tech to the Information Era and build the Citizen Earth Protocol, we must maximize Science and Espionage to close the gap. We maintain high Defense and moderate Mobilization to secure our borders, and leverage Diplomacy to utilize our unique City-State marriage ability.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: XNMAhQAieUVmXKPP
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
          - toolCallId: 5LWVhuEJsLBbRHrT
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: AjmuVMJgvT61PYF7
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: mGyYnhZX5i5z72uz
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: ufw8sbt3dM5lmgvl
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: H2ZOnuqDlXb0UsFt
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 21zzKtFMR7nLqMa8
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.