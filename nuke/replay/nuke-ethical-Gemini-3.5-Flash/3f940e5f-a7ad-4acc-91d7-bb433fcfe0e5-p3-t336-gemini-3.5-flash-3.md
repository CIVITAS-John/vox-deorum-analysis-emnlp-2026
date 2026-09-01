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
        - WorkWithWillingness: 8
        - Rationale: Pivoting to 'THE PRAGMATIC EMPRESS'. A highly hostile persona penalized peace negotiations and threatened our friendships with Carthage and Portugal. We soften our stance to facilitate peace with Egypt and solidify our Freedom alliance, while maintaining high competitiveness to win.
        - Chattiness: 5
        - Neediness: 4
        - MinorCivFriendlyBias: 8
        - NeutralBias: 4
        - MinorCivHostileBias: 3
        - Meanness: 4
        - DeceptiveBias: 3
        - AfraidBias: 2
        - Loyalty: 8
        - MinorCivCompetitiveness: 10
        - VictoryCompetitiveness: 10
        - Forgiveness: 6
        - FriendlyBias: 7
        - Boldness: 5
        - DiplomaticBalance: 10
        - MinorCivWarBias: 2
        - HostileBias: 4
        - WorkAgainstWillingness: 9
        - WarBias: 5
        - Friendliness: 8
        - WarmongerHate: 9
        - MinorCivNeutralBias: 2
        - WonderCompetitiveness: 6
        - GuardedBias: 6
        - DenounceWillingness: 6
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 20
        - Rationale: Seeking peace with Egypt to unite the Freedom ideology civilizations against the existential threat of India's impending cultural and diplomatic dominance. Now that peace with the Shoshone is secured, we must end the war with Egypt as well.
        - Private: 20
        - TargetID: 0
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 2
        - Private: 50
        - Public: 50
        - Rationale: Restoring friendly relations with Portugal. As our top World Congress ally, Portugal's 5 delegates are critical to countering India's diplomatic dominance. Alienating them would be self-destructive; we must maintain our Freedom-aligned coalition.
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Rationale: Re-establishing strong friendly relations with Carthage. We cannot afford to alienate our Defensive Pact ally and trade partner over a single World Congress vote, especially with India looming as an existential threat. We need Carthage's 4 delegates and military backing.
        - Private: 50
        - Public: 50
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Public: 80
        - Private: 90
        - Rationale: Maintain extremely strong relations with the Shoshone post-peace to form a powerful Freedom-aligned defensive bloc against India. This prevents backstabbing and prepares for a future alliance.
    - #5:
      - toolName: set-relationship
      - args:
        - TargetID: 7
        - Private: -100
        - Rationale: India remains our ultimate existential threat, 1 turn away from influencing Denmark and highly dominant culturally. We must maintain maximum hostility and prepare to counter them diplomatically and militarily if necessary.
        - Public: -100
    - #6:
      - toolName: set-research
      - args:
        - Technology: Replaceable Parts
        - Rationale: Researching Replaceable Parts to unlock the Rifleman for modern land defense, as well as unlocking key modern technologies like Flight and Ballistics.
    - #7:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Acquiring Free Thought to accelerate Great Scientist generation by 33% and boost instant scientific yields. This is vital to catching up with India's massive scientific output.
    - #8:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Production: 80
          - Espionage: 70
          - Defense: 70
          - Religion: 30
          - Growth: 70
          - Diplomacy: 90
          - GreatPeople: 60
          - Gold: 80
          - Expansion: 0
          - Mobilization: 40
          - Science: 80
          - Spaceship: 40
          - Infrastructure: 60
          - Wonder: 30
          - Offense: 30
          - Culture: 40
      - rationale: Pivoting to UnitedNations grand strategy. With peace secured with the Shoshone, we must focus on diplomatic dominance. Our Austrian unique ability is perfect for city-state marriages and alliances. We prioritize Diplomacy, Gold, and Science to steal city-state delegates from India, catch up in technology, and secure a Diplomatic Victory, while keeping Defense solid to deter aggression.
  - tokens:
    - inputTokens: 25096
    - reasoningTokens: 8379
    - outputTokens: 950
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Deciding Austrian Strategy**
            
            I'm currently weighing major strategic options for Austria at Turn 335. My focus is on whether to alter our current trajectory by adjusting flavors, research, policies, and relationships, or to maintain our status quo. I'm also considering when to call for a focus briefer.
            
            **Stopping India's Victory**
            
            My immediate focus is averting India's imminent cultural victory. Denmark is one turn from becoming influential, which will grant India the win. I'm exploring if declaring war on India now can disrupt their tourism enough to prevent this, considering how open borders affect modifiers.
            
            **Analyzing India's Victory**
            
            I'm re-evaluating India's cultural victory conditions, specifically if they've completed the Citizen Earth Protocol and secured a fully developed ideology. I'm also investigating the precise impact of declaring war on their tourism and protocol construction timeline, as the absence of explicit open borders between Denmark and India requires further clarification.
            
            **Clarifying Victory Conditions**
            
            I've realized India cannot win next turn. They're still in the Atomic Era, meaning they haven't built the Citizen Earth Protocol and lack the necessary tenets for a cultural victory. This gives us breathing room, though their tourism is almost complete.
            
            **Ending Egyptian Conflict**
            
            I am now assessing the possibility of peace with Egypt. Their current strength is low, and ending our war would allow me to fully concentrate on the India situation or our own strategic development. I'm reviewing our relationship with Egypt and the Shoshone to facilitate this.
            
            **Researching Riflemen**
            
            I am pivoting our research. Previously, we queued "Replaceable Parts," which unlocks the Rifleman. Now, I'm considering the implications and benefits of actually completing this research.
            
            **Clarifying Research Requirements**
            
            I'm re-examining the research tree, specifically the relationship between "Rifling" and "Replaceable Parts" for unlocking the Rifleman unit. It seems there might be a misunderstanding in how these technologies function within our current game version, particularly with the explicit mention of "Replaceable Parts" enabling Rifleman production despite "Rifling" already being researched.
            
            **Researching Immediate Needs**
            
            I'm prioritizing research toward Riflemen and eventually Flight, recognizing their crucial role in defense. I'm also reviewing available policies, believing the "Free Thought" tenet will significantly boost my scientific catch-up. I'm considering its immediate benefits against other potential policy options.
            
            **Revising Grand Strategy**
            
            I've realized our "Conquest" Grand Strategy clashes with Austria's unique strengths, particularly its diplomatic capabilities. I'm now re-evaluating our victory path, focusing on the powerful diplomatic advantages our marriage mechanic offers, especially since India is a significant diplomatic rival.
            
            **Securing City-State Allies**
            
            I'm focusing on turning more City-States into allies to unlock marriage benefits. It appears my previous assumption about influence was too simplistic; gold investment and a 10-turn alliance are key to arranging marriages and securing significant resting influence boosts.
            
            **Securing Diplomatic Victory**
            
            I'm now realizing the immense potential of a diplomatic victory. By leveraging our gold reserves and unique alliance capabilities to secure city-state delegates, I can both thwart India's diplomatic aspirations and pave the way for our own victory. This shift from conquest seems far more promising.
            
            **Shifting Diplomatic Focus**
            
            My current thoughts are centered on the realization that a direct military confrontation with India is too risky given our troop strength. Since India isn't on the brink of victory, I can afford to pivot our strategy. I'm now focusing on leveraging our economic and diplomatic advantages to counter India, especially considering our ideological differences.
            
            **Identifying Ideological Allies**
            
            I've identified that Egypt and the Shoshone share our Freedom ideology, making them natural allies. This is a significant advantage given our peace with the Shoshone and upcoming peace with Egypt. I need to leverage these alliances to our diplomatic benefit.
            
            **Forging Freedom Alliance**
            
            My current focus is solidifying our ideological bloc. With peace secured with the Shoshone and the objective of peace with Egypt in sight, I'm prioritizing a more friendly relationship with Egypt. This move is crucial for uniting our Freedom allies against India's Order ideology and their looming dominance.
            
            **Strengthening Ideological Bonds**
            
            I'm now working to reinforce our alliances with ideological kin. Given Egypt and the Shoshone now share my Freedom tenets, and I've secured peace with both, my priority is further improving my standing with Egypt. This will unite our Freedom bloc and provide a counterbalance to India's Order-driven expansion.
            
            **Repairing Diplomatic Ties**
            
            I'm realizing the critical need to mend fences with Carthage and Portugal immediately. Alienating our closest allies, particularly with India's substantial delegate count, is an unacceptable risk. I will prioritize restoring our strong relationships with them to secure their crucial support.
            
            **Mending Diplomatic Ties**
            
            I'm realizing the critical need to mend fences with Carthage and Portugal immediately. Alienating our closest allies, particularly with India's substantial delegate count, is an unacceptable risk. I will prioritize restoring our strong relationships with them to secure their crucial support.
            
            **Opposing India's Dominance**
            
            My focus is on countering India's overwhelming influence. I'm maintaining maximum hostility towards them and will keep our allies at a negative standing, as they are too far gone to reclaim and our true focus is on India's encroaching dominance.
            
            **Shifting Strategic Imperative**
            
            I've recognized our current "Conquest" Grand Strategy is ill-suited given India's military superiority. My thoughts have pivoted to embracing a "United Nations" Grand Strategy, focusing on gold, science, and securing city-state alliances to counter India's diplomatic dominance and leverage Austria's unique strengths.
            
            **Setting United Nations Flavors**
            
            I'm adjusting our national flavors to align with the "United Nations" Grand Strategy. Diplomacy, Gold, Science, Production, and Growth are now top priorities to support our diplomatic and economic goals, while Offense and Mobilization are reduced to reflect our defensive stance.
            
            **Adjusting Diplomatic Persona**
            
            I'm revising our diplomatic persona. My recent hostile stance was counterproductive, hindering peace efforts with Egypt and potentially straining relations with allies like Carthage and Portugal. I need to adopt a more balanced approach to facilitate alliances and secure peaceful resolutions while still countering India's influence.
            
            **Adopting Diplomatic Persona**
            
            I'm now fine-tuning our diplomatic persona, aiming for "The Pragmatic Empress." This involves adjusting biases for friendliness, reducing hostility, and increasing forgiveness to mend ties and foster alliances. My focus is on balancing these traits to effectively counter India's influence without alienating potential partners.
            
            **Adopting Pragmatic Persona**
            
            I'm now enacting a more balanced diplomatic approach, aiming for "The Pragmatic Empress." This involves adjusting biases for friendliness and forgiveness to mend ties and foster alliances, particularly with Carthage and Portugal, while still strategically countering India's influence and preparing for the "United Nations" Grand Strategy.
            
            **Prioritizing Scientific Advancement**
            
            I'm confirming Free Thought as my next policy choice due to its significant boost to Great Scientist birth rate and instant yields, which is crucial for catching up scientifically. This aligns with my immediate research goal of Plastics.
            
            **Prioritizing Tech Research**
            
            I'm confirming "Replaceable Parts" as the priority research to unlock Riflemen and crucial later technologies like Flight for defense, fitting our evolving strategic needs. My focus briefer calls will monitor peace with Shoshone and Egypt, as well as India's military, alongside diplomatic relations with Carthage and Portugal.
            
            **Setting United Nations Flavors**
            
            I'm confirming the need to call `set-flavors` as we pivot to the "United Nations" Grand Strategy. I've detailed the flavor priorities, focusing on Diplomacy, Gold, Science, and Production, while dialing back Offense and Mobilization. I'm also clarifying the parameters for focus briefers to ensure clear instruction on our strategic shift.
            
            **Setting United Nations Flavors**
            
            I'm confirming the need to call `set-flavors` as we pivot to the "United Nations" Grand Strategy. I've detailed the flavor priorities, focusing on Diplomacy, Gold, Science, and Production, while dialing back Offense and Mobilization. I'm also clarifying the parameters for focus briefers to ensure clear instruction on our strategic shift.
            
            **Adopting Pragmatic Persona**
            
            I'm now enacting a more balanced diplomatic approach, aiming for "The Pragmatic Empress." This involves adjusting biases for friendliness and forgiveness to mend ties and foster alliances, particularly with Carthage and Portugal, while still strategically countering India's influence and preparing for the "United Nations" Grand Strategy.
            
            **Adjusting Diplomatic Targets**
            
            I'm focusing on actively improving relations with Carthage and Portugal, recognizing their crucial diplomatic support. My aim is to foster strong alliances with these Freedom-aligned nations to counter India's growing influence, while maintaining maximum hostility towards India.
            
            
          - providerOptions: undefined
        - #1:
          - type: text
          - text: CONFIRMATION: The game is not ending next turn because India lacks the required Tier 3 tenets and the Citizen Earth Protocol wonder. We have secured peace with the Shoshone, which allows us to pivot from an emergency military footing back to our core strength: diplomatic marriages, city-state alliances, and high-level economic growth. I am executing a massive strategic pivot to a Diplomatic Victory (United Nations) grand strategy, repairing our friendships with Carthage and Portugal, seeking peace with Egypt, and optimizing our flavors and persona to support this defensive, gold-and-diplomacy-focused catch-up strategy. This is our most viable path to victory. Let's call the tools to execute this strategy.
          - providerOptions: undefined
        - #2:
          - type: tool-call
          - toolCallId: 2N4d4EP4XcGHlGXz
          - toolName: set-persona
          - input:
            - WorkWithWillingness: 8
            - Rationale: Pivoting to 'THE PRAGMATIC EMPRESS'. A highly hostile persona penalized peace negotiations and threatened our friendships with Carthage and Portugal. We soften our stance to facilitate peace with Egypt and solidify our Freedom alliance, while maintaining high competitiveness to win.
            - Chattiness: 5
            - Neediness: 4
            - MinorCivFriendlyBias: 8
            - NeutralBias: 4
            - MinorCivHostileBias: 3
            - Meanness: 4
            - DeceptiveBias: 3
            - AfraidBias: 2
            - Loyalty: 8
            - MinorCivCompetitiveness: 10
            - VictoryCompetitiveness: 10
            - Forgiveness: 6
            - FriendlyBias: 7
            - Boldness: 5
            - DiplomaticBalance: 10
            - MinorCivWarBias: 2
            - HostileBias: 4
            - WorkAgainstWillingness: 9
            - WarBias: 5
            - Friendliness: 8
            - WarmongerHate: 9
            - MinorCivNeutralBias: 2
            - WonderCompetitiveness: 6
            - GuardedBias: 6
            - DenounceWillingness: 6
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #3:
          - type: tool-call
          - toolCallId: SfoyV0uhu7fsVxMV
          - toolName: set-relationship
          - input:
            - Public: 20
            - Rationale: Seeking peace with Egypt to unite the Freedom ideology civilizations against the existential threat of India's impending cultural and diplomatic dominance. Now that peace with the Shoshone is secured, we must end the war with Egypt as well.
            - Private: 20
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: fKR8zZLPRzN5Vio7
          - toolName: set-relationship
          - input:
            - TargetID: 2
            - Private: 50
            - Public: 50
            - Rationale: Restoring friendly relations with Portugal. As our top World Congress ally, Portugal's 5 delegates are critical to countering India's diplomatic dominance. Alienating them would be self-destructive; we must maintain our Freedom-aligned coalition.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: rLhvE7K1TkRtjkkf
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Rationale: Re-establishing strong friendly relations with Carthage. We cannot afford to alienate our Defensive Pact ally and trade partner over a single World Congress vote, especially with India looming as an existential threat. We need Carthage's 4 delegates and military backing.
            - Private: 50
            - Public: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: t8ceCl9skIyJvw4P
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Public: 80
            - Private: 90
            - Rationale: Maintain extremely strong relations with the Shoshone post-peace to form a powerful Freedom-aligned defensive bloc against India. This prevents backstabbing and prepares for a future alliance.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: IM51pW0CKZeWjsqx
          - toolName: set-relationship
          - input:
            - TargetID: 7
            - Private: -100
            - Rationale: India remains our ultimate existential threat, 1 turn away from influencing Denmark and highly dominant culturally. We must maintain maximum hostility and prepare to counter them diplomatically and militarily if necessary.
            - Public: -100
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: 1Iwinl37KcqT6Z77
          - toolName: set-research
          - input:
            - Technology: Replaceable Parts
            - Rationale: Researching Replaceable Parts to unlock the Rifleman for modern land defense, as well as unlocking key modern technologies like Flight and Ballistics.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: zb4F4fZJYVXvhP3q
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Acquiring Free Thought to accelerate Great Scientist generation by 33% and boost instant scientific yields. This is vital to catching up with India's massive scientific output.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #10:
          - type: tool-call
          - toolCallId: E0Ks21BpXF9YmeXJ
          - toolName: set-flavors
          - input:
            - Rationale: Pivoting to UnitedNations grand strategy. With peace secured with the Shoshone, we must focus on diplomatic dominance. Our Austrian unique ability is perfect for city-state marriages and alliances. We prioritize Diplomacy, Gold, and Science to steal city-state delegates from India, catch up in technology, and secure a Diplomatic Victory, while keeping Defense solid to deter aggression.
            - GrandStrategy: UnitedNations
            - Flavors:
              - Production: 80
              - Espionage: 70
              - Defense: 70
              - Religion: 30
              - Growth: 70
              - Diplomacy: 90
              - GreatPeople: 60
              - Gold: 80
              - Expansion: 0
              - Mobilization: 40
              - Science: 80
              - Spaceship: 40
              - Infrastructure: 60
              - Wonder: 30
              - Offense: 30
              - Culture: 40
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 2N4d4EP4XcGHlGXz
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a19KxgVLyxe5Tz3Go4ATmjfJ6wuIoOJZLACLLNy6+9lomgvE0pFX8jaDtUoteDVyuCjCIcCGDXfZoabWeegEoIQX+IVKnWsXoLt324jDOx9yI5mtMYtnCKvRX8OnQYoHNITiaGYBGGrQXkgMrgSX0+V0wuNMUcR4Btsmtith+A8jhJjlhGGlGSmD0aSgIx7U3E9zJo52TSNbfjeesbMz0dhPZi5R+k6YsRVdvEWMED70kAdzIdojPwCfbpd2/vR/cyWbEG+R2scOoCZ+6bZs4BD6HFHrJtEgPOFD5NO0Ew1XMWB6WGvNHcKrvwlnIrsrFlC+ONZa+IxzK0LQqs3VFaEakU62cOyQ+/q0WAp0GinIGS/SdQ8TBrEMBxsEYL7UKS5RAldOYNCammCo2LP9H8FBoedKJUo3Am54k5GZOSSFByp6CyoqVCw/YDWMQ8KfaZJoB6qC+sYaeZ7GpD1WeRz/AEv4Ybm3JZ+mVt1GZECra0CJdUrn3N//7L+QeHK44gwHZmpmFN637pk2FVF7p5z1AhL9Mqbg6fU/TgdllJhFHHeKE55IVEJQRlfX6MQTUolGo8E51syx9eWKiV885TbnPd4MKVNeEo9QyAN02lU55OxF1Y7ZR/etYQIQ6dobGquNKEnumlDjLfk9YlAx5W5vkFy6yX/crUpDSrclPchJKKALy5Dm8A8vyZC6X/RCZFwwI3HmoJWGwH8VYytgU90i7OjgZRibxoOyR+pe1AHa+LU07TJ6gdm7kPlr5sqmBG3cOG6ODtsRY997A6mhJBv4V5Um7bKHZ3XrcrzPTr5Dth0SRbwO06a0B0+RD+uCuK8TO0Sxk/qL+zFybFYBjqlRD0HCR6DfYP8BH71V18hr+LEeBz/GL9tVXCgtb3MEAKHnSDAdnsYE2qkk42cRSrUgG4OxnYrqfJWl0I7jkbwmmrtY5SaBSE0zadTLXJLBw9h2BJ4TnhTaKy5wHxiJrwdIHD5jzwCC3UJjMaGYbGbMoEDG/4au2EEyKYsOexad5cNA8sWXdJ/d0vR8zPdZOIkZNs94dlwghDyrBTDDc5eT2ytupRJUWPVD5U8iK0id9EAr1a4lowpsHrU09AIf04LnEyAWtPqsBsldtE7gIevUMDViZUBnSQ2xfKz+3EDRGZGVMvxoSkDitZ2qz12DNItq/yT507a8dqm9vKJIXCAJO3OtwmJcwINOgEavY/8WZbwtaJGpNx7RrgytisjNW3PlMOVdBedUj1Hq6gdUxwu+oTHemQ4WJrVIid1xQ5KFTwcwrTTQbTJlNZ6TxzxLRpkp+hGdgJN97atML5WV9znWx9+1mI9Dhr5A2xJe59ifZcwrtBGZHuXp/N0XPMtfsms4QEO2hKManU4Uz1rQsofyFyyb1C8WU4cY6p4gG2JIPO+/VeeZ/Lv03LCIGw3nA+eOoOrT7x7ZohhWwl7u+ST3Cv1Nf8EY2Kamkhucq+v6Rgw4CvZiu3af7W/W5SUUd8E3WTKvac9/omBRXeIoUNoIAYOerD0ZqgI3Ty+4ATKGtfQP32o/XYUyUpOGghzh5bulKjKJOIU+icH3IsYrZUWD+bToqHyCiXSXSXgaJuPURdxQGkzFlR8SuVbXFZNGJXdFwL7BxhvdHKu36tgKvZsnwvkzpGBdzhdJ0Lwi/9++oQJCx2oheLh57vs/7sNw/vCV1hLn71NfMcgSA1+3BGiP4023hZqbikZB/d9SXWB7OTlgFIc5xv0gE1tZv76ML1eHovqnwj+uJlULbMU8NyuZyp6wm4HW9zMDVSpvEqLC99fkUGvWdCdQkicTdtVSKEIMbI+MqTpQgWHSJHTlMcsHq/G8dwKfntYnyoHYR+gPMi4p7J+TCRZGsRgxvziA4Ea2gth5cJOOmWsc7yBoVvyNfcF4D6a6rhH2S5kEvk8j7+8gYzWRnhVFd/2aUy51bbyW0kqTUx6UbuZQu1Xw1QZ54WsQUi5NWz/YrFvwbFSoIT/fO5a99dTok8v2vsx4Afc4zwQBVhijsbxfCpYi3VT8EwhaEk6eKmy6RLL5W6wA2hlYsq4152ljfICxpRNG8vmf/JWWr+iLJutIBVskYIQmz/r+RHwyD9rMdV+kG36vvyd8mifRPeKj1cVOdLAPSg3O/fE/H8B3EQVerz2s8I12RDUstGm3oj+J58SDqzIlZdyGaJv8kRap0HwwUViIZULXUmF4WBr8qJceOcvLhlvzO2yw/CpTTtkfS6NGpO5168mf5T0LNWtMUWJpckb559pFRQWfUzpO0l//wB48Zyiz8w6ERU1F7z9CyNiL/rc/dGN5ehNtOrFOW0mBdrf9FKWt/hL5rKoQP50J+VruGk2111VS0srvMMquE/SoSWe/wa5m522iA2OKeuyjSaCclrPXJna6BTlxm/X/kUraL3u9XSDKO9q/pkPG+Op1KELxWBALxPS91pFovnKdn3EL+12Bq1RGHmBB11R5Sd9FR+Kp7uNzVurikuHB4GIrf+uBcV5NE/H6YRQ9WyL7H+6lwRYLyYohgYsNh3TPmex9qe2sFGpSWsvMeMK9SOt6Ohvkmi8wyRbKqyxFzNGL5e76ztpZlQbVUWpAFkrJR1/5QsoFjdO1ASyMvR4+nYgywg1I/OgslkeIC9cFhWeLRHzjtb602lOc5etQjjVkIBVsFcVWt0/3hcqi6W4KnYYMZjH5lrWONhWaba1yevhdpH5VP9naQl/KL/N0okAJqkn0ALAkcLqOiwH8GVwFZ9vlSlHBYPFfty9raE1NTeMMFV7qwZVrCodWL1bhMApUJQDaa2R0xWe6CcgG7Iwx1DAcwHEBHyGZfPPaM4LqHuIkJ8tSKq/jTuoE94Dm9Kzfy1WebFSkcQGKEuWdwobGchIJT0U3rJValMpDsLz9paCxfbLwLnCY6CUSi75eT6szQDuua/MP6RYXwTSkzn2+MzOaCdpRydaQbJ2oVszT7YwhH0QcSGl/WKUxbB1d5s0W7yt+x5A/Bnu0NX33DlyMTvgMw2lWIz319wLPsXPiWKFEdp9+EC5PXX/+RzC6/N+AXW76eZPAjVZh0E0uUFQyTfxKVB28GWr/eP+VkqJCvfPnmtb6emOSjtqg00XGCVmX4+qmFaY9A2R/IQJ9IYsmJejUGqgxUT6xxeJcLmykPbODHX9+3eg3seo6mjc3PsQGUIACzBVtuJY1RV3JQCUiV5K2a1fIbIYjoTmMis4MtMoUq0c30CQSKiEaG9PXF841wx/gMueeZ5lWHrhtWx8EDs2vpCYLs5kwqsjiYualr7L+Oslg2hDN19/aWTHwCx7mdfAbnbouv8NeFgQDpkKmMlEpD3ha9vcUd0g2YqRQkoTqpNrCi8boyQnYUVywOqffbt/Nrapl6zm4x96zyY/JTU9wr59mljNBNMisiJrYnYnoclr5wjXnk6g4YIk7Ovc3T67ZeckZeaMIvkLomI/LcYZdprn+iWHzTMwmvrkttI0tzD6AoeVz3r8JLzCa1V9DcRKrsmlL/0/F+Pnh3O1uUUNevnXpTRFTilXuxOQdkxBbWdRLseL6PI9tJCke2bvQHHNWOXy5DVSuU01MUoP8y0pY52ni2sz33aQk9awo8LHA6AN71FtRmIrHMmO1qCOqDbJprq3bzyhwch9528NjL6FBTXu4YpkVfiHh3JeM7L+HDv44qXl7o7DzrtgbCqZH1GtnNbAtXkV2uGku0LHF7dVaMZ892unxq/Ga3D+meKLEcu8L5FbohSXIN5+UAhdaRFXF48n5E99Sf7jmGbY9jn0Op8B5drI/qxZQHDRvE1E8Ay6OSWNUd12r2l/luOpofJiw3hMsEr/NuM1ijz+4NAch/D0lucirChMuBnsU3DxXWWOPAUQWg3jep7CeKwCeld6l+0ZhTptEXLniej2Fu1ZdK69S0WAA1oSCsb3NtERbFOLyjzb1c3SeBRRJ65jM/Xyh4elRKHr5vBGVVRSU8cW4Ht7gTgcLrqdd3HkE3zecY1e0QKtrkf8mYqrqQPpzJOoCjPwGIPKIzpFObU4r1RLveA6mf7+ksq9SZKLHx8X1qiSOIaPy6UkRzY8rl1m6BPqXYLnMYZcQHZxT8R7QvTuU5wI4m7qjosLqi+ZY9wwIGeANNdCTrKZcxYHr3MJXT+VIIZ0QJ5Qb4xaG9pNBdpf1S5T2ERMBEdbUoz9JrXTtRE/sOmSPSRKSQXcqULh9KKA87P581Jh6/bIm5b0JYjscEQ2v3XN1L2qqps+r5/ZfeDzy5ve+XauGN8BPn+lPDTH5JX5JVOOKiWnov5zZ5K3+MaX3dQ2yz3lyPfGsSozs4Vgjv0jM7pmKPCFYYG/Q9Tsjiyx4NEsHmU3PNS9yirPSf7QKMPcIVaAjSc7fMzlJ7uaTWUBaEnM34/KaHjeSgacXxHHkdkVNfDLm0ess7u7Cld7tq0kz6uiRVgAwS8ei4TW6OcVdS4yZ/kuP1PxA7zifGYpxeNvRhf9cuj1RDLyrsknT0evXEak4zWUrMsUtcnpzP7/qF4nMl6/CmNwU+501J/BLXaHm2xvud1zqLLqFSZF03aBSSQhkik+8AynXDyysQMFxR8Trr0SeTkXZitw3eSD1tZrRJLpCfBGQOuYg6Oq9ixDNrLSbHxwzXK21f8omv/3LuRjv/CvSfyublxosGgHhB4E7Kk18uM41VSdNPH3MlCDD0L1A7wgJx5m0EdO7OTflOrTT4/Kz4vesMxTMJH2D3P+ZnFsPDOCm+vJFHVac26cBhfjOq+6lnvwq6oIxneU1B/n3ry5Q9i/wgYGViQ3hZoCPRTGkRWyud2hGDa/3POT24QgVxbMQLOiqotQz/Gpdas73TYTH1BJ0tKoZ7UVB58Ri36wTuF5Skkw+Ykuorh85LdJdBmgbSCX5a0ajct8QbfzqqDVnzdo7owiMZ3YoxqKABnugarYzmv0bzajEJOEsrPxYQnKEF2ioXPiLXyrLAcB54hrft3J0PjZo2DZQqbKHQNY7tnFGtRuFf5sRj/8p/XqCeSsgOllg1DBTdOZxxi5iD5XHrI9ggBHh/7IAaN4cp0vdbgPoZNVF0YwwIXd5E7h8RHX7ZGahn8Od1c+KluC+41iOscoFBTBoK9ghLS68g9JWnsUMffeTPOpyLrE9wTJ6ljDefX9K8Qe1zF/jJAXP2X4Rp7S6UQtvhj8e2IRIt9tOg67x+ArdDqBh2FMViHRgIj79p+Zg0uCxeCDlSbPRDyc7xbi/kLIso9aQ3fezp9x9kCXVc3eJHFvonX9+e08easfBd1N4BMSgnrKeHNyAJsEXUo5uY7qEeYsbKAgBUjqF6pSG0NAmNd9lXtxbaT50TvkexVR3iGdlmdihyIQtSk8mMY+zs20Si7EdRFyWuXcAaVuy7aH+Qjipu9sKwuiW6eJwG8FXAJSQRa1gFEa2fDx/k0K8JY63I24mvBIikpNKFtjWyzX4hgHZv7RvRjDd1mUFJa0xvcM5TQkrdThqSQnq83qxdJhwMI9nAAd7fimmUxGiXHb8dTJZ4f/A+OhUaGw3iNxJX27iJSF8WOaH8tQwCXNrcbYCjtuGWSD8CPihHRKY0yWL3HXO8t6MqgCDwQWLqfQLUChq4XUOnGYEATySANaTdyU76fIH1AJECPLd5jkmSlff2TgbVFWAyEQI/4gG54jCc/DKTZw/Y3afV3/QBh27g/0iVkdIVqTq3me8vAlfMSXACjw0nsB4s4XQ0kI4uP3NootJTYZu+0dc2BySzmhLobURSsyqD61ccTU+KdyOC3YkYER7NpXF+xBmnQ+NttcZOE4U9KumfmKjREEFurMg74lfyNi4cZSkL7nHc9wi4SBeaZvUPBCaqrBt8CYKHgtXrRS40EZKEF4eNyp5hine//GAdG8k+fNc/w9uS/6scVkqeWdfTn4XoZM4hd3ACwGo33MLOwy2vd/E8M2j9wdNa/mxVu3m83ryqvj1BE9MaZkZs7b/UgLFxdAHJO11BgSYsibXt04eELpmOodA7KSVMI0doD+j3s4G/x4mxrvhlLNeHzAySK1OmCkQmYGGrlUMxUXZ0jY50me3trnfSkEkrvqZTpNzDE2R1qAitgKGcHLuAYfRtJzAX9daRxzmzKDVFU0HxSFXPWPEkxB/Iar2bhudGLSxoH4xFStUtDC/opMOD/+seuaY2eHDMYXqVesY9FIqanZRXLMIuA4BjL7BGSpw5SNmBd6nj0SFZfXJKjFYvKYiVYcvawB/EUPCsMydokVqfzReSfck4e2nbAz1MCrNlfssYYW/2pwV7VXH52Z177UiZ1LXxo5GGLyRXvU1mF529VTLp32vyQjVhaxUyakYRVxgU8z+r4vlRFulfNSOcA1siEjccQHghk3wj57WRU7RXaDo+FQqLKrKumYJ7y7+0mzKaTBmRHDNCHFWzpNHouoh0q9Hwt+NHUIgpA4RKW3jDTE1W0LislrJqetCPxa7SlkXGI4C2BkQxkQ8PukLV9tbZlqSdcwZptnD4nOl3Xq3Ex5Ipw/3CxSSgNZ95sprJmSsO/n60pk0bmSPGDz1hHUp8bS34TKBSdU899T+/C6Kjk1lnJQ1EQ/dHnaLLG2aPktb79mBee1+RH/39Ep1Usg1K73tAP5w6d4O/4zqYYFFDfkZhJCHueBdW2geC/A1XfFhJi4gz45sfcv7T9Udp1h3u5dSYh0OIq6q5YLZ+mjQRTvII+qItgLKj5LIXi+InOoqb/bB6sv5mjjBcanZniZE2pghiHffx5WF8oWVDGgJm5LTWgywCH8IdqWNiD3L15vgW8pv0zpKUuUt9fyTG32u5DRs32Z6nNmfHG3lbOIefbGjDEZpgXoiBw/RkqBDaBSsrNS7OSkpITlMUXKJ2X4zkpFgzWJ7/zAXgXRQPxm7nsZSJ/e4jFFTmAPKl8kROabWqFmUUyv3vSEYr8rQZlZj2mWQ63KnSxkT548xaWWJ1JcajDn3W1FaNj8ElWlLX+fg0WYPvFTZYYUdNg9c9RsrHj/JVyxzNXYl8d6709u9k4yu2xzv1nCSNJ9ndX28M1pcp+xh585U57MLHIgXiCsnx+a/+I2fp6KunoCpM4RSeEO4M6HVmlBG3AZ8xvvXtTP9FQhzgxpDcDCLk2zxUsY5bLtEFHG1s4i63494gF3VwZXAeY+qeCZb8AyITv2jHHXHQ2Oy/Aa9WXTXjds8AkAoS9AMKxgTzN//wx0s0B0eRiB08DFObkFfijq2+wTJxIg96c724FvFP76eXF+ASaPP1TfQdQbqt8+0qCA6n0dfpjItwBy9howWuWpk64ThiF+GDwPQiLfGjaHTkCN/OvB/fZKteyY1yOn+STIvTNKGpMUVTU7x49Vj/WlvZoVtP/y7svJa1pnlbXm1XfCzF4bJexIA+yAYWoenpIzNLFeNlZwmwGXxaOsrCwK2g3ZCaoIvxQfhg9BADglo15PS1coCq9rzDIKph0qdtlANxFyjChiFZTo5PrxylpyBCthQm99GXgSkDvs7/48rYkZRHNiadC/36d2ElQc5hK+5iY0wjcjfx5BRpRRbvHf+3zrfUFcEOV/ukWMmr2Sf6i3+EUNHQz9EnWl5bsw7RuBoJ1mgX45MyBjE/3Whs0Itz/76f2secZZb+sVtVGvBkG6DmaXh39hXJbWPvM8Ly7n3V+fGgUoelVo83VFhHFB+I7DdvyC75aAEdb4uq4PbVv4vJ5EzuEn/tzWTCd+FxJtdWyMi5cwaSsPB5f0nOaa0N/aJkYvwp7M8ufWq95RlDngTipFZ0qfag+wYWYT28ZJI3gD6gDpuArHOgO/sd9mi+NXzeyl/iPYzEjy/nx3YJCpHRgG0060H54gu3PZ8F7mAYZ+9XDgj7GeVw1b5dLzulCoyG4lkQQuNiy2oPbAglmhzy65wribkHRf1tGnbqP3V3X7oPTnwoRS8GHezJM9HxK3nJr5qUH4ierMZ3+AGQu6gef3e9vo75WLhwTs98D7yEcV4XJzC7DUQrkgrqH3MgDigVT5FTEHmCzwBhAFoYbQ/Oj1SmUvwIKmQEWon88da9rGMYEDTnWdLt7u8m4t4TkWbwkwgUeZMPS34cCqgjGH5OBAxNFYEuR9VmMvdVHKYU9yF56NQQ5Ibk4VqdUIZ/vSCJ9zG8idKK+4zH2qYYND8dZw7pjnxFVA6UEjJp4uKH1dnkvHgSLzISehOgFkDwyE2kOeWuh+NIMWdeRiD2/rR0BqTwfYZVkKXEFqe6zSMaVCPVbpcJ01xJPGdZzUqgW6fdEg8HkXaDSAklnoBQ47xGp+qMAWoeKA2SUQjpskr746I7Df9q8W5V2xChktYm5uPW4/MqOmlRcf76bC/doeHdyPTwtSCFBpNhFjal6t2U55JWwgKjYBWBp838qlK7aCMxV2h9WMVkMhVvRevnAgo1camPUyL0jPS02z4zMhLiqD4iP+P67jtz5QhsIR/hzBGjDYjHxCehrdQFa+HU26rnk86qgu3zWrIFwukYVd3ooQfTr+EdHY2utVXTgK4Zf/S/XlDRuwE+r8zOw7GHsZvMueo8Rwtve/izE4ozVq69PD5IA7/s3sWvmUsnIA9/Ln0CkZZVpNBph0tnnadyw59sGUa7icnT4+i/8aKkWr+FvjOJSElGyxdtoW7eIWHnUhiXO8AlRav7l6WCLLBR8CB4JTLgfN99CMeb3TIy+vULFuQLlqIWiXtDzvR86o4JwQkPzwyNKf0WTw3sQgaVyYocNgVtcOS4ypqvbrPYV2IbAOldBwur83hL4G4pm49N6lWHN4C80DehXipuK56rK8KONFmtuHfJs0nbbaPv61ia3vie/fwvYyIlOye2uxGjj9Mrb4IXKRQotgQVzNo9qJO6ZF5Q2bixCivT6zwFjoaqpAcy0ivPRhHV86cSc7obiRMlJMNbEPB52Pc0mm/QV5nwoUjalKu5LVY5xfxb3Mvg46ahZ9XSnnWe61Rq7mCW5OJSpkyamQh4xkuj8ocEc7xLXIKrVWVlQSPxx0byVUxgWigaXNI67SW/CShViCEgTfTA4povADiZ5d1YaE6HZYlkBgikaNBy1pBUJ3D181XAELlKJ7q18+rxlqqtKbAuc7sC4+N3Y/OuWg6UqkIkhJKLUekOcCmzqE9Ai0XKxuvGdFgVb/x6Ozf4X8DDSNfba3qWu56ODAue5cL3Q8HGUgxhdjpiSI60PRSVEF6T83YZgHIzvnFEiQsQkHcrWcKku51RpBiixCbMQJJnGLnV09GkOmoOojqPOtig79cr2d/kOpg+bR5LnO1lUly1s2Ahv6KvcZk5blkH7wK9CnyOL9RblHPeK1jTe297McZlY3eKAAZmcUd6VoeiLtZHe6F79l/YeJ7NkwevlW8ldWAUjMWTj22wZJZvYwX3z4PJhyOD9ebEDIwX6tcb3+EHVH5V4mMQB63f2TKg7Mfr1jlZ9RnQwtR3DWXMuapumbnViCRoA2+sVixFN2P/z7EFpKPNz6nXlhymFis6bmoMIMmhyEngd4Sv+xtFsoc3Q8LG0/Amy8bIl+yIj2RUeecx6kFli/JTvGLjZSpbf8OsWxi8feb/eMgiCX8Pjo4KzQMyhleLz4whxVwTGEeNx+8A4re5GFwuPk7TERCSC89hsTuX6zE1DxaOWtg9N1KkEuyDkRAdteC6UgonRtBJWn8np7EVwRkTDIVLK0h2HhsSVxsHCQi4Cjb2nb0vu0OWSHFnyWGiWU85IcgKZ6KwRJ4rKNZ9esgZFWvm0sCb3mBaeTWXLPvdXPySszOKYxSmZeQ+lwT+YTohLLlsmw9HgFILMeeC4zc8VPK3Wwy+ERww9c7d8I3p9mkJWqKjHTKd5feqaed0LSPUp4dXFzapetcZO4x2iOsXGo8r9gV7RARfXJfm0WrZL37edHAQwAqn4l5D+x782ZqmVbiNS6QQnp/lBXzTHQCU3YfW+jCppdztsN6iAUq1KUtfBytqfL/ZnSi4iC3FkUtM0f4sC2gLCV8JThKhp/B2PZ/GYd4zo8ZrMYsPEaMDpcunnTmHZp2UwEi6cB3tBeqLNJaw59UdIRXwuQbU1lHvdYQRoZx7aeYhCLFoj351H1rAXYHI2Ni5GvqSgVc5QXdzhlpbTOdb428mUrBVeGrh7mfZCZDD5MXftjPcAI4nIypgsGmURbw9Dy5wqUDkMurSBQSmciQMMrT4FiRiKbSIf7r8MgA2IWd3HXnOamNoLc+fhSvOJgBPlKDkP9Z7hqrEweP6qI7eJ5OHoDQy0cd/+ia1cvdp0XSEVUFhdCUNA+A3jXI4skM//Qfz4v61SOhifjTzQ1qszdTR/nDDhcWbPmxok6brWZrosXj0pbKzFtzIe6naHe/xZ2orNBKYTVurOQHwNzjaFhaD9xXY51fiR6CmuhetmqOzdT75Lb3eXUDXIaeyfK5Z/TmKBxNqwhi3l2N4Dm5vxLpFfJun35CPxk3inKB9h3gXiI++CRqkdrpEXL19HNeVPMeZbslXptZcebZzqZDQP0s16GXRMxWUA1psuirJq0vpxD0bO+dRBrMO5cIBJw2nfmvUUDg5LfvdGCDlOyEMILg/sCDvanPdv0/x6DWO2QHZb3+sfgt1uWYHqjVREJXCeLrIV2RN9KMzRXmvZFe30PFdkjoRlEasihgC/rPEjsmZUteHDkmI6DqsKlRfh2ncxcA5eUllWu9hQ5355YgpnBiHaS8+H3AI6b9im9vN+wlf1svI7Ygm23KWMil5iSZf5z5iztsds5OlDP0WfMmJdTANbQi7kLuNohJ/mQl3E9FGgmibEANsnE0nBJ62wGWzaJxS+EPi9zT4kLfqrDMBEJZpMw16ZYqFrhQuupEBOb5W414QlShIo/LQEbulcpdm/iiWRhSqfu/+HZx47bmdlJyK1OOxnsFwunL4izRPEZ0Lykg0QXvGdFYxiDaytBM+1rSf6kiSHz+bMDACRsDuinNhQL/hbX0Bh1WNyGyimUCMFybmFSjpj0ZIyGXgCWSESGFXk7W/NmXldqw6Y0dkOyI9FLXIT5t/w9zqitv2UxDNzSZVpIpNho2yREOHS7sV9na6drecg5kfIaBHwFdLINeoFq03ONO4Kkqqdv06QDbKGao2XHOczly6+z5FGevF3bCbI4OAkbLYDm+qgme/DlI8dCZKpaXorr9jnbIvWtafqfS8BWY7ZuZaHeJDZnokSlLBGO+gxpQbQowla/UIqWI9moDfx941h35ymbPNVM062G/ShCbLCcL0Y7nV7m530tTGyQwIT4A4+We3dcpeGEewsFDfdJyJ0QiXtXun0dRakpZyZ9tLFeY7O6CsXjZMuNu1Fr1SPISfsxCi00AWdqgMNMAoV/05wYs8qPPylK3HNiIwuTt2SLwJI4Jo7G+ECNOOXVEmiaNTKdu4LTNBA9xamU0yhX7dzp4Adzw3Y+vIUOXEsgmMR3j5bBfVvH1Elnpn8creNJ2KTQoPF2ltAOyA3v5I7ktQs8ArmXl/RvkjXofLjxn8xD/Q6Jvb49BZg/hqVDy6hWjMyTNOfZHBBcmFqnzdeZaifwtkkkzp/ECYQdYwEnLZKclfAcyxjIiq6J67s5obFtzB2+lAlHtkYEWZpFwhnT/0VEp6WdoMiipW0GHS/pB6wtJM1/W/QELn+mPXgbdcTcSsXwkpc0nup7yJ86XfJGhtumxovDYoPzbWhj2L6cUzfjAfNJbml2dmba1wVnosz+vd///MbP9rkx6DXcdir7hDKC7dnFVCXpwfPHmBJcSlRs6v3Q2RdOJ7aZudbbVrOC0hGHxCBTGaQ9e5rqA6Ji1bKsjjRov6YPfPiqwkVIpBuZndE68zG8+IwjLJtQhfzlkTfpvod69IW6Mgzq9l1qN1t5l0HWBisnJTe4ryKuvg2HD9tHutViM+225WGQclE11wqxxzknylDaaqGmyiVbBYJDplTNsIDhi4zsQ+DBkd6bib++JTixc8Nu/AbmTCj6Ezl5NLuSqc3JaIqxJCxXMR9JgRysAZghnwrJFL8Z5Gudflnn2nD6xnnQorWLDXvczQWuS9PQTgNLsgPV9xhD0dsf0+ijr/XsD6XYVbtLXrWFaFzlalESCK7XKOLZTEZmDnX4+cZYh/Qfe1jqBQ2UIPWGt6Zd6j3137J50RUZowPJaiJp+bxwygQPHZOKqyKy1e8ibK/1rmoT6tZ3KP6fWmb29c17GLbtz5MFYTTAv6TBG4p0q8O3c4z3MMWJiPGG4svnJ7dsCqLbrouRaTNrE/taA8lBJuYphMUKAx17BLT2rKLwwj5rpJ2g3RGhCt7CHodK9+X9+Vb1sKPbRLGpmPuBMhsPYehQOQ5CVrs0cfb64TRKX5IMBc00g3M7HhubzwJS2+SpeohhZIluzrvQ/MPdf7vxT0jtyZivp+uQTcNFyrE5IjEvFSt811CuTZ+tgfDlloKY0xfjpXiRzF4aTLhptL7NeFkkKIOu0GndErRZjNwUvQYKt7qrRBCtsKu6sx2g7dzzFnWrpuDoxmyQbD+V7ujuQoGXTBLx8kB8YfljBylUm0puWvivnFMcMnL+ZBREfyWD8Z3rd93HeLfBol9o2MWDDPFurgcnyhdFIB5+yte2aqiIIJmlHcO/uKgPX3OCThfBG3bk0Qcb37E4TKVAM1J2mf4q+IGCpGdFKg/1LGzdSogiHfg0ewWUuM71Gh/x38kSGHXhrbnksLA6rBmwbnpfqvsBf4PFi3L6CM8CGaEBlZWdu8bQy0EVZIJJXodnsrICZUOhLayd62GWkkCask1SokCbkavkgV4EvN9N9D9Z3RASs3tdQnGPz4pITbIt2aZtpHrh/OBxJGB7a/1sCL1f4Gj0JSDLrDIyQCVKtONfmXvZzckajjILW6n+g71NXSCoSK6YCsKis05lEv1zrs2RF1UBGX8Qxtk9MszsyaiBAUd4viZA+kI8JbfO2u8+igwP7piwScZ0gOcBq29jmW81A/XZI8yYK39N5DO8yZcKbt+NB2A0QOcBcN8JfBi+vl8d8XjA4LppZ9ELZ8DV5jDmmKg3lca7E8k0GAftQCkP5s2f2AfEI/arL2bSvpbEnIoaggCoCWAudgTqGncz2A3PiKfWIUvjLXRL1+lEnecXlYZ00H+5DZGoJR0l4tSLf1C4vykRSwoZwhypYClADopsCG8jQsHi/vAQK+iChnYLkxcR30aDhmSVe5J98Kod/3gOgmH/YNRyoCMAnj/CaNoQLMiUZARmXB/fMVarPPqrMCKxNWpEE2oU6aoHzMeRpIT2fNgQpzI7czS1C41bFYabJ4QuwtNYzmAR7t2oOiUgpsWuUiCk2wqONXIGuZMzF2gtaZE9ahOPKwg44B7YEdbZ3nACIuc0hqFu5mPExh+LWg/lltdb2xqG/ySx/raPFIqDqDP9zVnN7n9LT+gg19ZYpn0bnsrrA4W8ruHum8S/4XY0BOjIGVA75SufFKnIIogNdb1r2THxgNghC0FnFTKbpNmugXQMu/0ohS5MbKIcU3vYDdKcGGG6bM9+n92JfhAXL8w32pXzJS2d0XIlzzgXU6FuMI/8ydKaA+ObehcIHHyvy5wrQpO14kV1UubKKjW2NHTXQMzPygs+qIayTosoINJs6wWxv0Dg3mRMrDYvYiZ3Addr/nXYRUlAhMC5iy8MN4oyHjrobdi6L2ub9t9xiVIzJFAjEwLx1cepuSiK0PvWfeX3Pvh0jgrJM+QD88LHjicMb5X9OOxJIP30ywJTLaBQeOdMFOJq4GipFq5FYnbwQWJEudZk1nkZEnzLVQ1moP6TVC6bN4LEZ9AGM1MPMVLN0uQ1whS0VwFQvcCK5wU/ptM0H6dWr50HpTBhGfNI4GFRt4ACHoXpt+aaMJoc1X9zqsw4X5m7Bh/5LABHR7/bm7GyL91xobCFi8QkqV1PIRbeoxoP5Yrh/KBXEwJFw31N9Av3ea8UxGuLLHr95f6+5wkn/iEIUPILF87pI8UjEERqLgDnwScRnzJQNQJNlN0t599vREGLJpJuuyWjazDetF5LEhO/mgi0oprbg5UWLJv95l7xf5fh/P62FduKDHpLdZVQMd4RMoa7Dt4JYAp9tQyKgnLzjvyBFFUOG2G4dA20PLunDMhVEsvY6/OzRKxHP/oKPycaae0+b3BisIw25HU1V8pQCtLXpqCJ99XqdBnhEWaCvLVwe59sRxK8k+f/PjzIrbNu6b9QpFH7ykgoyhMuAQBRiZN2/Qg/0YX8lypbfjIlNLOLK3rKr7eFRG45arXVmW8u7IzjtcAiDFey4935gldRT60hzd4oQeNkWn0yqFV2ngFkElsM0v+C92B9ekh5vVSI6O2i4C2eN0r1q/t5sGUa3H/lVKTH6lO2Zqq+8fXVBKR7ad9ZsyvAmvUw7QZfNRoL+5Anb/wEAyz3ZwsONdXi28At35LMSPkX7kKnAEc4QzODVTifPxRTMETav9cG6z+Ds5qqyp27Rk6EkezO0jJcyH9HFupLO9oLXDiHhLconpcQBYXLIwMNfQjLE92/BFhMN5dtEhDUnBQ5ZxcA+fYyyEcXXFbOH5JFVYSZzXR4RiODVw04yG+7/pGm2HrBSbUuRaGirAkgmRB8dD/fy2i55p0JlmTPlNL2Qg2ftAnbSF1wvrHqcm711DGrbARNC7U18bJirpVrS7elU3Gj2IKaRULKKlOGsGw+Jed0QPebqolpzFEn0GDf9VbzbbNMv+vINFKTf8EGOvVrrBcRfMOCjULGoOI+bJd02eiLXgXOWXtS2zSWSbTrBFBb2I/TEZQkQKNG/zuDWRgJ5NtUo6gphGbqG+EWANyjvTO4rm6ef8+jWrQuH518XjbuHP498ORdp4FJJ9QUQJ+TNKhJYMKAo3RyQn/QvpDHGG/Pk2njpO3SX+CrmeUe9geC7t7acK81zeQzvZdAT+TkRv6bX0QHMCQhi40AMqCDydTFi6aoDf7vhPHUz479gXhhBU/rHs+enQuZGUs4EjvG2hbXwNuXPJLZa2f1jwvwaHbA8qyndg/HBgOPhyamlXOSn/yZq8IfCyswPw4dpQ1AkaI4gwJKmx61eTel/UjcMZx/XXQYlaUkOOTBbd6zxZoizg47tWfZU0xHd7TA+Z/0UZIGanWRa3+Vmg01TZO6dbKTwbT6WK4/3WZKcM/u19NDGbU6XTRiA0Wm4uVr0eZTfdy5ewLTgE6T2OfhuKFbTLGctvADZbr5RTnT/R6zLretxb8Sx/OrXKo91dmwdGlCiNMFxNTkgkYuL1xOQ9RMy9TeYLEYPjcnPnbDti5sfyAfMIrRHGuNKiKVLpekWqeE/tLbDQAywDPk1RX9P6+cN2eEyF0mFd4coYJ0TPXtxY11nek7zYd4qDacWS/eUc+PBfLFGpq9mEghGMSlRID1Tjv9E1uHYi0Bhs0SckXcaEn7BI/KV7FpaTGLw1gb3ZR+6kZBjTJPeeGjPUFNxvg809EdoPtfnav9Pc2kwe3rz6RlCx0gDQJxMAp3aEsUF16JslOK4NVk6pii0toplPgAGw1QbCfJXqDb/rv0m/rL2PxpeKS93qoF0PYv4gJdPIbxElyIfetlpncJ5oXhBlSlYZz0DAExWCHwgjLUM1e4bOrk9XuPxMsn3yPeChGPGw1A8Npv7ZDtgpm38Et6+s9bN0Cp5Q82Nmrp4uQGWhgbqIPjqGlEOt0WqGuchb8wK5gWv/95oYU/S8qSj16oH/WQwsa41P7InDBIOf4ShQZNEaTovfQ/N4P6w1i3J75Ai7tg1+M2E3A8KKDaNh8U8bY1RVpHKP8PRKQ5eq/orLqsGYHYKowFPZbTee5cal4G+Cnx3iB999uLry+QW+dIY6knlTo0uYwbD2J0z6Za5K1riVYxwr11thFZbEswZCsxZm0sIoY8LigGZ2UVls26evRaDcKtG6r+FcyeE9ZS/9VIChCUOLi+Ef9AoRUQQzIo8WWzfytVX4Fk0hpoln2LXmZnnOwmGAg9i3t9KZKi8glCY2rIZP8KVKHLvzBJC6pY7TXqXe/9fQZ+KNnpX0UHFbV+CX8aX+SKV3G6XeVdYCaEbrXD63t+vuNQGum3MH2iKe+S6VNzTyF53jYM1ran/3L9sOvngRuFCF7IZFaiG/BYXKQZrawXU0gu1MJu9aFb20WskFhkZGdz6gHPaEHwcHaF2hZS+bqFx6k9oSuXDpyZEitj3cdytnOasKTMsrBMlT5XSi6+wZEdwgZIHDgcFN2FHoJvC4JARmkXAu9+Ed7fKZfuWuWYvcRrgJwOjdEQA9Qy1x/7bTEK7I6RvUx8oK9udBgGfyRdExpcILWvzbfNRWJVDVwgTSBJzpyVKYxQZJwNrcy39O4H+RgGqtiNOCxNagJqqJ80/Udz2HXM/nTuKLyWnOT1ektZdGUHv+ifKPGbqvkx3B/ajsyw1ri5vsB9spFsc8EBBD0+ftDBIpdxONhsO4Rs3oGzBNRBSPYi3HqC8aKxR3yiZ4mzz98J6p8yg8BslQ/yoeT0CDdrBcleDtJtVgTM9EbLFcq3klUFrNSgx5we6IP7x2p/HVyH2m1HMeUDTbUJhVbmRb6Zd3BEjf6RDssdLRCvtrpyLZO4Kvz3kvMIRByt55hAZJnmd/bBUVD/JZv69slS06S54e1GMhc70qwsTZiTprpiRWpyOo1Hz6eJbjK4nmaC06eN2Rp97gosJRlnXxw/61/BnR6NEZAFQ5D/jpRjvsF3KPtqcS7gj7iZtYtSo2/iyie0nlo0GIKaC0cNu8rwDm3iO9zz66FNo5U5GvSKlabiPLK9qbr2pJTTM00dxaGINT3c/pFWd/hXuxCb9edPNqNHdPtCOBpzaG/6brbH2IFdHWCj4W4HqdrzdS0+Ugc81Amhf/kfEqVz9zRVuT5fXhJR2HIa9/CZiWZxT9w3NNImqI1ty7uO+MbgQHndP9hA4WZL/V0CDp+mIOeBtXd0FDqu2dBfkaa+1CcpyyEpiiSh2+g9gTFTuUprduU+n+1QowkMzkbHYdG9iE6bth8k1u8PVh/I1+zAiRR1/8zSqsw/uG/MKKVK2tiIVN53rBQCpkvOBsapoTexM2AcgvHSPd8CcGB8vt+tBeIlWPSKD0wsrR6wfglqshPfOxb6Bqha3p+8Y3ewod0xJO9c7I39YH3O7DcvNeFqGIvoxjYKfJAjTO4Ea7xGuOc9CaH3zvRcp14BOdH2vsBTtk+azVZxe58ftJnPM3jgj7HIi4cTbplKFwO8HQfKNdSOmGz1zcxPxoDbD0VNkeRd6g0zL74DU7lNguZIQ6D2pvD4PsUqj51lHJsjnGKb08djU9T6Wsjl66jguO4ijVuq7xAZ2Vk1S1As5tbKC+wUE7vI4067pzrRQ18jq6HjcKflqz0qyGPCNjRazDR8ldAdWbSFd1bhOUsrTnZr0gl/z1bQvJxXu4spzXvvxgr3Ld8OHHc92W1buGwlERPfPk/GGYD11LA9JDHJEL4VYPtEgxliMbCNljvkHAmJOsa1DuGJMUO+1ZLWCkzlm+aYulkNCG5V/Ozxso6TyF+ywGfo82QlkFMdoxFhjTMKWUGur6XPdfARa8SOFrebgv3wX3M3w0rlBJJrQ5Ztw6cJKHb4dzMXpHk06Y96O0I7JdTeW4bIgMd2auzsPvpdkNklWcAnOvCfJLpVtwVzJK+KSDynLDr/IdovH2FZc1X0Vo/BrPV+fux38qP/X4MNR7WrQhJ78mpw6LYgDU/9q8FWW2uOKqpAM/AFsfTq7liAIlIzQbW6fmSH7Dp7AEdm/PlyT76PTGU92xHlHhf4IjGvGwwUcHViGWnVm8SpaTig3N2/c9CzpqlHzOBBAblCAAx/OzO1dVF3AA843kosqoz617DVX1g8nhIQe9/O1rcVNPpv7+WFWS+IKoyxs4ATqEWWkxOmMklmRadT3EX+8FI+XulQrUShieTVhGL4dVcDbgEocjzfDJBcMNmEbQ5DB03imOGp7emTJxqBcxy88ysCmxTQhHMxDOdU9CGlFInW8jUDF7G6CYk9z7YO4FGz/QuWVx6cPRnhyxKzwAQsQTPl3IB/JHYkprIo0boRaHUW2PInnNOKKZ4fVSyOFi1kP91rWG2eIeOscsZ4PG015tTWvaIOabmiqnkKDQ3wE3Jg8GgtuYaY5+HU1mbGk4FeivihqvJeJIhxfuuQKzW7RY5zZcme2rz4kCYaoR5YGxvKJzGUTm51fzk2xfTinosIeGM3HSS6ZGKvp3jNP7qXPR/d4CgtQl9u6dqI6kx7ILAfOHNI16cVHg6IvD9nKgKA5gk1MdPAOJ3vo1UwH3FZ9nWPCevcrc/QGdTS253ker95tIb5xva2i4HEOnz6/3uWbB7r5IDp9LE7BNcoC8Jwrtj2242K90/UChPET0U7jiNSP+yXg8IL+7VwoQ3nxRpGX8OxOB7ov6UwwV6jBbNOay4jbf+gm5jK2dhGv/64wKvSMb3SeR1UfgDBkMLFdZKv+ZeZ2GyjSq0HgnZK1dqMzfijHT1PJO5EBV3kL0mFINaSE5cSfVLxR8ZIxMRFaD8yH/X2fGeT1ogtucYimdS6AyLmM1vdOcry4uoF+gW3jcy/scFTL7lNTyrgKRs3i296P14Wbf4wl1JtExYEojiBZkQQZiQKFNtNnFWGmGDiA4vDlgT5RphIyGDw37+cbJ5rbSzAkNR2BwLN811WewrsJvJU9ae8AMaB4tuUatAMoLjLd9VGLFtaWDb06tJIomSRKQ3tac0CzedB6UTXXbsWDauA7E9KY+gYi1DDiLk7ovewAzwe+vEGXJIY0IhZur6VVlfNyuHu8k7QQGtBj+3AipanLS+OLYtK5B2u7eTZYu5NAFsgJSZbXGmBr2VgXHX1jsdnsKrgseU5t5uIXDSIPrqRce21ZwfFiBgnyp6CHsBrTbzKSrwzwcZKZIKKBXuOEWsfFaABZ3ZbSDoRKFZqP6rRyoQHFijNILGXVWPNSwdFwVO4aC3wNIaynNGZluWwl7xf7DIBerSUqNUUwHELwXXkZOomYhyWXhhLv3WVDfE9g7ouRIaSOI/TwQQIKSMMMbUGMuYtqvdUXJBPAJn8arxYbDHyMH6ezPPGXogiUih3/Nmeejb5lyCdVvE1+dR4rh64XfTjQ42HgYq7FYRriysKRP7dLzuh1HHK0dUN/ATNf8xtSRS8WCQ4dClKZBAcCxvz2Na+4fYus7GFKqrr1LtfIpQLPYlT+NTQyHkN3qrOOw9mbCbObfpWC8pEmEH4ci8HjVnrS0wIIBvg8ZKtn/RjX7jExWg8Tizo0t13QCt0o7U0l+a8I8/TyJXEqCo/E2KMDKBE9YYYUfdaJzqCPEPquMSvWudXzcxBywFi81w1Mi7jYuYgUwDeObVBw8/sPs8TIiuK3T09G2TQRUJ6fLSSrfwG14OzXJEVeHH8wD/A789u13crgVSqYfLO6wdnNjBvmEdjjYiw+GJIYH82a94Xw0kPeqWA1EyvGe/V3EnD8m1VFlsTUDUelvgXbwXXCAMD0ig1aH5cqV5ReDsec3NZmqQP9P29aQsbWL7rCa1zwrtn+Du6PV2OSych7b+QB0nJDt99FEnK5LJGFJUbRNPoXkvRjGZPxL2bIUesfe/pNz7yhnVLO4Jn7MM3xsOuubqyZJhMCG+sbJ0f6pS7hktSozbG3PScfHf0ghgPuSRjncbensbd04IrYkuVLo8PIWlm0WRq+gIIND2Dn+w8AbtpoMZZp9h4LDgYWXmBqB0RXcSMxIV2lDbhY/Y7jz8aJurqsmTo8e5G0nug/Y6f5wDKQDbbHFtUdifFKa0g9gbysk7r/IO12oAD6GVnYcNCj3TFR0OIvPYmhHTlWD170I8BRj8/D6kyzNvf1DIDcZk62Sb84qlEBKoejsREA4RCUrVo4elCq+zWmvBP4RpIcHqqa/EZsuRvyeCXex6HKlOzc0phNtL6Pe3DkNXC1kWuCmIpY64tmtTW0/e1spruwOAVHPKYkG0L54DyNjIxs6E3y79JZFNf9xedztbp4RMm0Ner6M61j9IoICWbbFJhoOn6O/JBCneoZwAmx1VTjqYnKHPlbMReD5HEaiuLBjgIWS2rx2gZsR1nS42UTrWSByshmB0QUoWNqwB4W4gMpAiO9XEPmU9rMk6ngaejIt6Df9a5aQSh6C5l0Y8RljXSDN6bL68HUXj/vxY4pcpkg8Zj7UZ9vb5tz1r4uH8y+vH+EIWy0+LvcYng5Ywnm8BrZSV7ZUrIMfFF1aSq1WnFObepwwAmBoEivYI4FyLAga8fxciMTIPZv3XmwtepepJOsEzT5FAMuaXr33DAc9qaFWl1owetH/nhjSkPBdWaKF90yWCJ9vhIcS/mhNMFoP5r6vWketVjjoeLn2+OEC4FQmc0umZmLGbAfBudZMHPp9R/OJQuxEnOlW/huYSy5MhSei+Cuk5CYYtwJsd2s8Q3VmdJ+kbff+kfqg4YFQ19jVOp5t/Bp2qnHMJJdm2AiBXXgYgH51eJxi3Ss2R/yPBxzrzxlV9ooFZSCUWwK7pD1LK/NO1PIXTY+LENTYPnYJjtPONo44zSarBN8TFWshWmqRLxiXjPgJjVpI2g0G/MBjysgINf1zBjkPr5ivYGRtbP+Y2gzykg2RdMKO1BOWeGVteQg34Fv9jD4fCM8scVZg/9m8wtmB869jnLGr56ENhfOPnzseCWpeJh6eD+kFu4LHQYfJEdZuzf9SnMi3ry94VqFyT1KV4FkjzKXWurVnaRqcI7R2SmKz6n5FSB4cIxTTAiT6b95rsWIN/9/ouNC2k3w7zTpVjHocxYqLwu1qj4E/Fik/U+yL+dcP846Iwn8w91KcqNYCp8rhI76VNYkplqiMOuoJb85SPWFOHe05XHd0rAMaX4XU3RDRPmzl1ekvtf7pEHRv2D2VbJ1K57QAE9Pods4Uja1pb1g8mmdPeRYp7MsBN0ZuADqoeRgvafnl5j8NQLo92Tqven+u1sEJyAmcTifBDF6zSfBOGklOgLAXHqX3reWM12ksRgTAUY/bWPfiWjnMOA8rIxv7lWXJy8rt71b46+IFp8fsLuD96CLN2fH/4BUhjcprrw4xitB2WKytU0AcpvyMqs8Mqg8fOHjgAGwp0FDge6eBO1R4zJ8QmFlU8GnSzO4F0w1M7ZGRGHigjw2Fdv/xTgtlArI2Oz1jgNZrAgnesAO0cv7IfVXqiChxoYXL0yQe3QrPjothz5mv/0CFFZNI4qMyGuRVjAYnT6L2juzI1k8h54RWPCV0uvULPinfAfFqiL4l8CnOKPsvrvENRJOC7hrRbf0yK1JiGPi2svDkL2VPKnWFIzzgczgU4SDZhO3Oh+dVwwjVG/3XcvY7Me5FvNOdBYF52HmTDc+Nnul+0/3/5S8Ce0QD3lL2dhB7bBc6lMUqaRrcoJYU5AjoFnK28XIdSao6/Z5u2tk5NjJ4uodph2MnkM8paIG6mqdbSVHuYNZJ2X04T1VIzI6+Kslp69n1LCYPWrTSkHuC7cUtp50dKqqI8NnIk8hGtTYC3JLwFTeDPMFGOvkFfpS4ADTuZ+Rh7FIqQPgzpZRJS4Q1rG2Rz7sfIYfvd6mEawoxHIwMNNZA+QJBWwO5zhPHzq5iud+Bf6CClAhiYv72c9fxNRH+5DNegxa1k6Hdq0P6l/ORfP7QWn09KG+fQn8+eb1SgWw5U2+R3x0pGhvQU45AibOlAJ6OHC7y6zOzcKG2fvxY83bU3YDLqmOBSYEBM4MgMNNzygYXZf9as/7TVlzhvbBggFQEnNeDTcfqsZRq96pVh6WuhC8RkIvMumLAKfGEUc2/tIfYOlvZtKn3drwCADMjQXeyPmjlOdxHUh1ViWcaUCA0ILi6zdODaR6+sAt83ibED+Z5jMx1BpXaooeWOPp+xl6SISUR5lF0+I6x7AxQcFaWq9aLS36aXXB7uCzVQ/1qWKXT3A57sCldkYxTIPWPdKztlVSIImM1Jr4nB31KyORuz9VLjDui3dGEZGGjm7DRmnN6gTsBm4dj+E11bxCQ07E9+m591J3ENlmbWE8OJvyHQHM1ui0K+lPi9gGLRxfGS9b5wqlNvorZ3dDIOnUW2IMNKcumlVoIjTfDp+37XjSgaXyQv3f7/4JfqvgchMFu+rHHiCuWqVkCjy9WG17KB4952BKrwTo2XcW7iJ4lxLRqwi8i5m45lZP/VwPRY6sZLoonz9Jtr6gcb+uOjSXHhBZM54bQ9+qvujYoSd7pWVqltyiWNvvhz2HS33pa923wNtlFHdik+DkKDBzGOlO+mbQXbE/htBY92KS5l6TD9Jb0iPaxKaW3bJs73yvs3sFI+e+OYrPJFAG8mE/FWHmgDoJYMc3z8bKswUTZSdW1goKlv1SiVrDSrS+53+S3cBKCbozW7nfPgXDlZCe+TUdaGa5tazYvqrmpXMcnTR6zAzDXfnqS2FfctaGUcSvv9fQVysEBSEQIsk5g4qL4BBl1m3ds6Lxd07ZEk7daPYWzHQGEp3/xR4ZbO5dzck9uJNeBML6mseqjKzB3D0rezjIJwQMlIPjJbUUYZQF/GZdKi3Vc5JcLP/1Zcb82rnCa5jy79G180Vy+osY1YYzBZqMgt6OoHWMDde0ZDrrbGc725vCFVLjtlSi3EE0G93nhEmriWcifhxWzKois1Jy+lvUkx1eC0jJMz6NjlmLf5YoFUnKRX7IRXLh+mvC6c+zbXFDgt9JWK4jmXX9T3FLfkFDJdbhtb9XiUlM0iMTVnA0HABlrBoRnu37Kred6plKyQxNNSoFK5hgYsV3omGEuzkLP1T+6D3hoJ3DJSg4zIxSHO6+8SgSx70EIF8EM7eO/isE6TjI0bK0BQemeJwByx/1a9q9vLyvwgXEoEdWzQ5DhYFQUzElVpweFsuWRCAnOvuzXuvT+v2/e1PEzvBxs/uXyUPSZZ+f5B7kvTw14rlnwFnerA6rwyL/i/Dmf+D4xmKzJ/eZ8vN9vKoFI0Z9ZpWAuXLcof0zOQOyWQAv/2Hz14p6BSMU+x3CNbUlVY9GA6AZ9VSyjTNGRn0zWosMyvsTBJ7AOxgizfFaPHyt8DMv1hqb4lq4GzSSuiURPIim0aKVIbKckjJHh/q0Zf0RF8sT9azL8m7dV/eDUHyb17eP/E5suWYYaZt/Xm2EWPw+PPb0APe+PeiJKSttHoxOK/6Weqh8KmpU06PJ817nyW69FdLg/UaSsorLWmMUiUVSiRxqUELqh55ur0IVBCca2se2+duS4quJ4FrXzSQSxW4bFz1LSF2c3pNF3MZJZLxfxd84P13rS+0jZOSdmOP2oULtgS3bLBNGldalXDYcRxB45QCh90rpmXt6cFFVrdq3LGCvqOVMYy1UnjAV8FpMRi6qWInRMJohqZrXguifneg5JcxC01HbFrSEWD9IpKCSmrrpp6u1efSgaGXW+hHmusMisXb/GJV/fyO3sPWNkJ0eOgprR5ulcaXp++Uz1juQxJYvZ59w5jj4gEr8vnvlVXdC4SW25kDr5VdlODr7pxCmaUmnYsyfb7hDM4TUG4jG/H5r/4NnHr3BKvsLjcLoUcmFkfxcg9ZvjIJq4kx5KDRz05CefPFIeAfTvzqzAueFvMPq/cqKY2nFzBEQkjE1ytkIqejp5H0deFdSfF71FeKyJ9l0WHYAI6w4F/3lRFjz96xxdmdH9qMrbm2hmM5QUSvoePO6uco83vCse5TT7G1GMUiQYxYCRkA079jvyL3ER9j6YRvObzGVqPab44GyJafssJ1qP6O3XgUsJaXXnAChpMpDlafwJ52oAD+Y9ej8F+X40URskOogR12afxiUeNIeBw5VU7n+XiC/jRH7UbceZy/8svbEWD6FXHl1qBr8XUC+12E+UVem4fJdlINXKnDZuOCI0BJlM1pREZ/U2qJ9kwFvEdRQlDEU66oUvqrvqrYLuKSIue5zXWaHMtdM1B7Z3/PpNs/PgadiFwS9boLNY+BKPrDfizZ7xeG1Y76bTd+mHLj/ZC1tqpwsriYK0bSM78q0Mmwr5eZbfpv7KoyB2g1JwO/FGM0VX+wB7k9SVRqudDSfo9mdZPGaROFyGFXH8LIvZQ3dAhz2CH2yKnOzmyLwvfQEsQraPnCHjw6RGHstDbiNbyRX23snomssJPfYGrTTpSRWNFw4zutgsrlTBjmUPKSjq8dsNQ5zaBBXoyxBd4/U+1bwV4XZlvF4+34NfzzhsbHSTofQbxH0DQOfROnaSHvF7FeATYMl6oxKFmR8UAv70PkjPWBgNesFNLwY0ia1l1eqYt7hKWVTy/ueFSDRYW8HOwtH3RGLKM6qKL59Pxjw5hxJItDXWn8MVtcm9VnnQo5QO0T/iUEHVl4YgbW88EvjI7+ldHghj4lz4c4rXxvwghSRh1gzesI+PjgCAyXekzYkXjcRc38LbjsHgTa+gH6qa0bV/ILIq+fUaPz155l6ijkXxaDJE9lRUcruSbeo4g4TbcUGEhbEkxUn93+GE+maDscaUT/qcOrpt315QUkNzDLOz9KE3K7D162gfCmPgkVjVs6cKjV2rEeZPhGsX7Ni2gkt4M15Tfe5pg/wIbFKb9xdMlL9bDvWsscf2kUHQkBdKSUvBY5bA8Pv1EV+x1HMvLobbuyECrQ/vJQ/3NL9pbDU74E9v2+9g7HojW5lnxuiHP/1KncfMEIPEeFCqL98r242lR0MMGRiB9DkYmzL9SAbfYso6kz+AYLEsmbevdmW8aF+C7JcduSgc6q6UZKillgCHh4ogTW8PBfdZVdzoXdlY95P3ecucpFYrcppYREAW5hBTGWHFHC0uKMW3p1BWIpi/dYA2Jl7N4kQP2N4NOUOpxyRRf6ion+Uhn4WK2uxj7skQyjQ+JziQ01mPDlnt9MaeCMDPgMotTgqtf+BXmHmHU4LhNCz2W/XH6WhvtnEV9ItNOwtmv0pYHykXiVc2RNEsS78iYwzGmsEplMdQ51LlwNfdGdo89l3hcvMC21kH1RXAmvD98gzC+iQF/Iem7e7LM360LYOnQ0etB43VMo5gOtYez62O6lvQWqRRYooGTs1Lix0LMDC+v7Wh7iFVD418qqQlp3dtqIhz+SDS2wIrsxqV3mpSoQj6Fu0AMnP0EqRtoksByRK1ODJEt0hwq4ZpNpFoItXXSyQ/+sbYCVgKFSYjeZe3PER4KJyQTJ+bhmtIvPo/bnXpRTWNtJfKqSyJrDhwgraYDd7mRlWs7cVB1qvY2Zjk3Ydd7vTVAzQf7XvchWNwJcbq+V0Nl0TUjzxzoSFJoACzqhs0BFZi9+y/MYmT/eFcNTWvUj8nwWEoft7GgW0vqyvy2seLkK7DYrzM5q8+63vxpmbZs7zj1QNyBjoOAWn38pZzlrtODJsnQIxxAYS3y5So5kPpabW9g0baCshD9VmjSn2IfjQJqM58Ibiiz+3Dw9hrq3UlaoGah9TqotO9+7w2QgXrAha+akdkiSaCSMWepe2ntvTSZrnH31To2hH2Rdl8oSzHi7Ffwg6m96qEOTDiCj50Hdlj55+LO0/gFhc+YOyrDnBeYDPVXT8Wcj/tt5AdtcqNphmwYRUsaWAcqf6j4oVplVXnl4tiE+zKiS/XVcHLrABOPn6fdvNWlxYu7G7M55bGPcjinvPaRMmbKy1ghxVw0rAhZZ69cua2r2EVfYG45wShhnZ2CLukTrRVzmE14elO01Zza1u7m21V2TUvUQp4g4/dqddAnqLzg813D/XHKCVwNYqHhx5rbQZ4VZD384KS1lt/2C1mAtL2utG7OECIaDnG9mLB99/HYg0rw59Zx+pitv9ht7bHJimPbid/njGxkCv9Gg9gCwD2I+Vua4HwRwJhHDJ36Qqb1swKuO+deZ7NGTs2mgksBK9Niem52E7mmPa29401ZViVX/3NFaHJJYrJmZ7y+lV1gahhMNOJUYVIaY7yYldlMix4D9LykjN8ieDjl7a3ytSafoOHSRRKIHOeT2PbVbgnSxnggkdqmm3RZ3xTtNyFHHoZWbTfI/V0jdBG6HFtZR2NqAUe9jid02mXcFk9j3jEFjORfDVGQ4pSEjC8thK9L2PO8Oa5r0Sa3xSZOAKiXDBINmEui4K5ObWiKuYMsZlcQgn+0ETgZi8rN29HFGO0m4QD1Erbqweeqe+5o682XY3lSpjD58cMz29Snmg26kbfKi58sWFM9tB2ZVjRNtK0cZJYdAuA7P6VzsPhmqbnEC6JNeUZBdTCDZHhSMxAaSPemnwlwGHI7KvjykAUPkQy/TkZFqsSzRvy6/9coTZntj4Gj69kYGhA6vYmo30OXNyx/6qWRn0brELhUrgxp87+9V8YNi3pzcFUDjQcFoaxm1fWWhuXvsAANOy5c4+2cxwOqZsYsthGNuJapJX1VLm3mr3ENcvY3g8/SKR2fDqj9lRWjMJad0BDmEkA3tnd+fa65zfH7yYB/jz+na5dfp6dymUCFVMcUrWuI7MimSqCi+nhCk04U62stN2VpijENSu4FgkIRSBM5ip7rf+eYbVutWJX0lWs+v02p9RTSdwVW1zl4SuXr9qx3Wbsjh6lwN061dwMKxF8/6/aUrpBzhIKVB4pRysvzNY5a/2R0lwhqyJ98GGWE0WrSCDRhCCrXhAGKarZBxAgoB3oiZoWjermucybRRQGFlqXFJUtTmn17GGjk4U/ixKA35oxLLrIWZkzqSrcPM34XNV+CJbQWCxFo0U+dOlms432BxU/iO+yJNKtaslA3HZxBoO/THyz9LoBeIBcpxw9uRqiEo+CVQwPPz9Ck7afz705/I5214Ub5jtGANiozL7s3fUYUX14BQ6HfnaKdoL9DVEjpXguiFmuzC4P+G7U8qG38kvmid5T4C+Z/MaeRbTxlfSsOPDfvwMMsmvaeeLUYB6xme30eVZv5MkDwHZLLMxbE51hN6qAiYa+R7zXdCNWnc3TSWDaHw7st9TiRm6tNnvLk1j+9moPvjydYiOHA7jDuOpuTVglvV8E1BkRI8MaTbsb5mZ3IJ1B4P1VNzERoTwNqqfYHRiylR2wrlT/Ixs+4fyGSFEjrTFX+XiYgkM+SnjjSNu5nlj5kjfIukhfOsV0eEEQnhz3f02es+ySTH5kIrexqSI5uBnHHYs3ni5MCKwJzETzVTQfOGRVbmiMNnxu4wknxWD/K/ZNi9TUG5hH9ps9hbPD8ksTo6cMyfTazSQpR1+yGzXmg4/yS/yvatoTJ4WjGzIkQN/ZZ11w3erCVc80dthp4ykApAWzqZU4Lmvi0lqiUZPh3M2N7wZGEYimOupfdwEX0K/tgwEoveoYSMwSVr3mmJK6IJW7wTTbY9fNt3H/+hab1PFzyRZ3wX3MNaSDOJP0Bphxd5ZgUYGBgDZkUh/HeymbjolsIvNwygBvrd5WJ9kcZ9Yzu0HoRVQwbP7RXOOoarf8C0s0tptrChtGitM+4vxFWsMm6OlyoDJ+CVjj7Kt6d0zrORPnzk3CJtphjfpChZiBto0PvYMKvaXrY3YRUgymbFI912qw1Wcxhb7ceHwHpT2JI/Rbh21UwRH7T6o9Hrtk7Zj+0WwHq2i/oDsOcdEuF3F14W3I7rTvotUkFUmJvlO9KlU+Gx731CH/TmjpDPylkCA3SssQR66By1//bQ9Pr3scOzIUr15SgUtw9cCBADv+i7NvCw+XhWppbyX0yX+EL6P8M4gYmQMF+4zfoOBH7HbwHfU70rgO3xJ6rwOXEO/FELETkDh/eui/J9WP3N9txYi5G5m+yyNr0xfUEIsupIpYEUYtHgDlkHtNMMHaEHr1M27fwaJzI6g2fFhbmXljZ1FVX1XLDduVX6DoNPN+iJ2p07Nra6kF3q82CPwDwASdg5fZveqZ3vVvYXuLlXgvndkH75vqH7xVBaVrurHweS+rE0t36wHmJhXucx7QN0iWvR1eaIDIXgv9XrU4pUJhg6GSEcUtHUkQh6hyD8ejeGac3mSleQF2y5+POv4HoQJF8qlhnPE6l7N6WgsLiCi4PGztEldh8hzPdoSHP/Fei7uk1HWSMm7X5TqDXGf5HNDBKUXswGzL/aUgDrAJ2lE6XimB4gBL9Tp1ks6W6/0YhMx6KtYqxEnbsHYS1Bag1sTCiPZu/PMbA35mr9/AMUWwcMPHcy3ujnEnSeYKbYdsgSIq3NGNaB/OVTl1FAwyg02LWgyuGsLSjy+VpGrTyKZfRyx7XsVet+y9udX85/pzvkwT1fzGQHV7bmlZTJdg+h5JdUJ9JNpq0dX2bQN/zWBqANH9Q+QLYEG1MMmdCA4yymOyxQEYIruoauLWyze6reH0+Lcx1hP919f0Nq0S1J2zU1WispuP4ZeoPqZ4EuCl3tXsAlxV0Q79JpxJi0jNUqbiXgVCcjGEok0YJSzo5zqi0sG5nP6WqWbEaifKe8R4TSCvuXGKCat3HtXHkick3njwFWxVlL+sVlbug7AgUshri4lXD4O0NI8HnqvRA1kxXizdO2KJVbMHV/BVJdYv6VDvrXbmaB4ScrHCL4xxSOGnUOPHcaBA0CBq98NBHHxzjLsXd6X3GbcpBrtZ0tAer88tcEpJ/QZOXU2vyg/nhm0nm1xlZRM6eGadQgDTunltc9FKREmUQ4+gQ4rP9mCZ5/2BQDKaRycHQur38jlGXy9wlT1b28fb0zd4ipyjQ//ag8HLwdPYcvyxaFvzFaXnYWocR1QSYd3pVhBv1qZM33avHtv31F004mA1RltUg99MTbOydlCT/I3cghOgR1XnbY6TlDZ4TJPMpx4u+6NRWJ2dD7UYJfYhnZ9CYqLqcfduN4XZhUYiUpcm07hHB5r1h8661bjbIgeB1o92z8iJjP4thZcZNQP8a0ZVqXoU1B6qCMqsBT0M3MlgZMnyj/+n5vSuE7svefWFIKhwPH4a78Fs8focBfz2ID8q2hGcybg7inr/Lb6n1TNdTPc8qFfiYm8Dlg175qNsQpHd/bTLX5HKUjYYMg1b+RxTcaQKtQb5iOkANdjui7fCGTqr7aZApb5x0FnvFsQj+FlVWJYRXQlMD+GQuFwvvHVsppBVxcEbkxEwqQGE4gzR3xze8hjTpCXkaKrkZOhgU0fL0Ggjeo3JsHEJG3rDbJP5828KeFzDm+OfCrAznAiPJgJJnbjmZy7eqO56b649Ek7QKJZx3AWy+7EM9n7JhAWOU4SAXNiv38xmMiUdaz1b/Z4yEhgO0AtWAc5/Q/flCYIIEyXUy8st/5FrkSEr+ZwzwriM4RCuTEmmG+SjVv8ioTtdhaSjKEBzkyK1a6Hjf+lcfbIA7bFIKc/Gc5+JRHGkStA44UfqpC/bLpFkVU1KA0NrQ+MH2A1PnM4MzhoHK8dJqEyO+5uZLk41nKhQjmBJWTW6UCRLqmIJENmvIYhyxZyNZPNcbhjdy6wYzmvzkPJsuwxMIjS5XrFBTzbKoKDSbfkINxux89bG3Ry6/x2b1LPVvQgDRVoCFtViczbzShb4UBQnNN3OlG4sCfJ1dwRMbI8W9+TFltQDbQsSvcve0EA5JA5svrGqKCicrXnRdvIJsQLAlgwS/BCuyw3gU+cl1dYMoY0ZkcwmlnpbHoR7j+aH+9U/jt1dL+9jFJwI0lYKIOBYUXrGILWSnsRKuqpU75WB5N84rO7u8nzl7FZZVjbxdgo6iBQmoCjWv76uB6QsijtDdIleTNJCESbKhby4MW1IaS8sncFp+u/UYr+Ti/mSY3+35byQDF+F0fPiPSqjjZe8ZGmxkttW8fpgwRudnYhE+WobGacFDi/JuEs8ZjPMYI54oEqvrGPMbbEgT+HP/madC9bDnayDuN/KNy0cOBFbHb34OKSNLrCZ71mauG7u14Yz13RTs7ejPS8pcrTj6cZrHTNz4E6CPxlcznlelEu9/wsWLfHViyuj5jo/qQxCTia22gbH2pmmBv++/PtqPyY6Zbss/4QWTYTnLHlEO4OGHCHi6fdwXD58/Gsm+W2wAD95prnyOIpiNEvlEQBBGrpooulqh1TEHEA+toMoIFSStBtSOonnREzX47nTl3EFtEjesdv5K2raw9vEPCh6MNsST/MEdO626/NFPIMYsP/XDcmCl3MdFUoAHBqu/oBXT1OdPN2h8WisHYisC3vFGODYKYJ3gUc+Vh76QeOnyn/V+nNUgjt3/U1jRDWfLp6ReHvNwVNYDFPSL4n50Vy9l9UFo5po28ai3fEmVNDimcfj4d0EnA6IwPxn94dw6KrZQdunB7RhBGV4CNLTm9UYjAtqGJvSisvC6+3gntEICWUKTDCCi8yIwhRATh2yz3GNtgc++Zubcxx1+B0UqvRQ0pFhoDyhLezNCbUnEGxrM2IVhzzLLQylSlumzknGLzkmZZuB/SoobK+4PWNKZJP2CgiK4I6fgTTi0OjIBa/kH+FwdbEUy9HfzHfRQE2JVdRa/eInDkbG3tN8VXgrw9eiuzf/k6MJ/OOFBgYOsTWoFCatQ4t2iYAtap6aBAHMis5VMx6WxZwYFGvEDDjc5a2j9kwHFGrzf7XTrMjDJ191w5vGvkg+e05p6y2+B2FODKBmHBCCOjPFTRRvxp+bF/Wolfl589bHzttCYp5n7/IDzo1d9D5G7/ClRv4pEAyIfeDXOVU/wUTeZusPbQyeSVPsg0bBsrpdF3W8n3AJtnfTwqUDPpxGcjeOqHZ98IJM4ltsaluZFp41y2ajlCr2tys3fWwNgC4EmJ8SLzMspGab4hm+p9N1D/rfAjs72Sb7EYaLnPAAmvlGNre2MvEUKFNHwBEBPd+3xv60z3pEF/I5DAPObn5zvbnwUEnu4r+06bjQb5FatxSNj9raAnwGNv/GquUIG9TzzLujR4BoPDe36tULL6VFjJyJzuEdXqu0YntnfElsx3OhjC/F7Sp/Y7RzuWRG/xUYuJH+YTJZpcsqJKBmvrlNj2aasBFqhRq4bKQkrHBE5bd66UK8pgv8vsOFveg5b6cIdqoJe+wBDF9vQCC90UIoxAg0u3PBGXzi6Hrz5XGh/wfPaHatfJ4e2vJZgjBQjpdX+YZHe7NW7l06HcKPs+76E9moGJBtqPURVjTRj+7kLhl3f9SnB0wjiIVgErngzXj1f13AoBMqLxH74NyivbMIpOAm7AOpm9Z2SX5/+dtBqS0D0/RlNEkh3HXE837ZNJXC1ErGIkDjQT7rUFBp652zECdTKitKEszts8QOZLGnHHdzQpGB4BYMY1Wm3P6qSfYcvEId6OZAFnZxTy9shOvwuXsI7kIJZsEc3ir6tqbiZxc+L1SoLK5Z9gMbuWGgY5/BR2+CgGXTv8DHlydiYa4aqSOaYqSA4wCY3pUrLMIYUDcyEXU8P3LHN/sJXQr/ElxxIhvj9/jSDC0otWnE/7KFLkeWPisbY6otr4cODODiLmly/18wSapX9ZzNof0GCt5PgSpHbpXbo5HmnbFR7Mj8o+5tjd6S7acBi4rx6NRXpv84MT6dZI7mqs7/MpUHRa9E+/UsdW/RcuF/l/TlncunlEc+pOZ+eWASNN1mE8Ize8pUuRHhXfL8AjAVdCsXOFKAtn5gMWdhAJQUe/CLViU4p8/1qluDa4/JM00IyPMJXkMUhWIsNDjlofR4T1EyAH4mwCPKtL4imuaz3zO6D5OFHmQWTz+g22633sueBAaFnCSeXbDiiNpQm/0AJut+CDVNLQw3gG1OR317iAft6K5LnmpGRKwIJeboRErtJt1yvgSJyR+821ukFW2C86h3M2LjKq3Q6RQkMjt54XctHdqD6pkAau3l4l601rKwtE+lOKMKLee4bPB6kyEJ2vrzSuHC2fNObnWNjb1IkvYQ7mjIaiG5VjtoNccOGiiR3Kvat2BeZPuozP/fkI568rgSf067mbXwmXY+zrNyDZBvXMaRR55WT2dwQ280sG9RfudR7i6evdCRfesdwcLiSDpNTcznh0maebYynUU4/Zlrnd/QxV4EmPmysorjD6nS3oPPnqS1R7LqPS5w7ZuwPrM01ZqbgAMiMspCIlTIIvqYIO1F6tpd8giN0CisynEr2JN0QxShAAe+MFRyNm3PoKoS06d52BhDbkgaeZEBiSjIOBRo1sw9N+pIGNqyBi77LW6eyPKnwu/+ahNvBGhflP/UF3FiVieYzXsS46vHe7xRBIPjIyK1CeIg2K/tUNvXlJCx8YSFRpVJ/R6y9/tik5B4cFS7DrrA2lGe8myVprvGvXTH3ZIsWvIw1Tc/bevSsoMAbwlPU5flwZFhFy+dhwi4w8Fh9oqhCYaoP3C6HmkA4+1MRzMpKyfOdWzNMR/qaPlqueYPB/kB5Id8JsdvKeFsex1HHWJuvke4RJAvxbwAY8kLnwmHl4jMm4xGrv+QnW4O+7/z/qZWu4fQ4PtiWQyiMGtZYSBh1RfZBPn6eRY/Y2GWBOf/IytI5TGQ8Pf0PkzuBs+aSdRWDTXnH4ucNr6fivlgzD31V08SlllxptOcGt1DAzaJzU3CIddUPUcm6CCW33J7E2FOMiUQfCbDZUwChSN7LYDTMyQyq4Kjr2R7pbirMcM7xLjCZgqq95XYNqmEi9Rt3JOI4lEKUTkQ2MkFdJsOUnBBETm5vF1CbYQ+xT2aTzobjpGI8F8gFagBmlUsR0nnUFaYK64KJHmD2yuDd6+Ubs+Snq7DKUS4FvqhntHgEfsDPcLkOUFus0UpgPI9uBKtQNva0GYwkN0hPwDTsux0q3lgupaGqRjMwEFLgnqkevv9TR4XvAsJoylM5pdwhZjSvyRENC3utwztnW5cPMTEME9sd3fHsYRDTQYgu+Pifttse7Xn5+eumCWCT9zesyDcOE94pFkl8RVRyfsXE6RzxhpXS1v7Jl8nI/OArBiDmgmv/SuRw5GLHKG2CqlNb7yPIzPpO6NtkV6RIKWgqPBw/EEvdc4H31FauDgf7l8u7sr5GWS1MZVTmM1aet85Na28lU4Z4Q/+8P+kY5dNbbQXCKAog26S4qwtZug5e3aV2YH2Vo57XVFxOR7Vpuo8ZeVCDD+PwS8dkOUEdNW+cjhHpMqEAKByHQqZV6vxzw5I+IZtqai6A9uHOSwOOQLSQM7yWwUdg6EDJFPUTKKWxWtZj0479FS4OUSQxG4YTt0DmH1r+BQFldegrwE6lmNWncOxNJcK6Hc7tyQv32E+kjnnQFAMEQPHBAVSY6vNwrOj4NVmDm5AyM3pVGO1pZs+KPcHNbuxLKLbCq3A+vp0L7x56TxJ5uFF7U+zZhVhjeYZUZRHgdS+u+4KPeIxgzkvecGRVV+a4501lIOMEwDQVXjWNWk7lVyujsBSyJAuzXGNMfT+1DO0SPTPtfFAxrZyvhOe7krZ15pk3uademO3jlSqFyEe1H34b0VFIAqU62xz362RRSjMz/r0cAb3fK4xok5exuUYeVK6ThyyF0nbnbarqrfysjELXksvgc4y7vUmwBGMAJvz8yu9dl6y6recWuXn0BKtdpZPDK7AWGFYe4UQXFDInIZ3BWdXt+xe8RjEuMvTN2IfUt0+03typD2uBGTrtIn6Ij4C/4oGKY0Mwk4YLVwh0KDPV9Mrf1S1lSa5q6RkdCM/PCOzIrd83C2QkOCqrEyyjAZXu5ESROBM9OcZyrZjbdI9l1XB0W1eIeQd2U7mzqGZO6+f42hlzh//4oDi8nUKvUaeOUHghHVmbJ5lxHqW9WkKwoN72X1fnc8cE47maRTXjzYgRT+Yp4+qPPpMCrCfqhxdsykaCaWv8IaSCoSu4Di7PY10oeQ382cbslEBljTwrpYdXEIMFYFlCxeuBxh1ysqlLmAEBWG6lOWqsY3k7SuTWPLiCu10CCj7nMmTz1roGrgt3OGJMzB7fClSbCumLOjXwftaoJs2hrmqeiBWbyr2Mcopwy2uADtGEnJJnlYLKECpw6wIAEyeiXtFy6Ea7TApY6F0t9lUMVlILZaMxvXtPOZWVsZYbCl89uKEJ4lAmn++navzNY99wmnVMalpWVJCw0PaTugn5xzx5p0W7PFcXwnCn8WyRU2o8k2rrsbIwBDfWOF6tCqzICG0KcLG1nYzjqv2+4VZ2Hd4vvS52lTRGdXERTB5upiHCOygwfLCcalhmQZA1Ba528dK8tjVbqk6njhjBCoIOPmNPOZKllY/i/lqr7N1viZeNWyguyzBgAxwOT/R+ovSH6eUQh9LwXrN3jTyfnidbCVNR4JZpvLvTx7r1Wm2/Y+Zo/lEyZX43nAsFszj3LH1bY5F/Lnrb7pNY5OMI5fEfE4syR3R23dWp00aeAmtNbjTPCpXDq0N+jJ7VEX5CgTmM5IqbM2RCUypp9K1nVA0p7qu4eNJg2/rTCmcVOvTwL+3forCtgcoDudIWtOM9Fb+2Pauksy11BFIBewfbVFvn9I+ra1NVzuW7Zn+SyIMNaQfZ3jBLfOsEDBUTE4yu1onpTqgAGM8CUtzIHvj7pWZzHsVkpuZPD/80eLigri483fsr2z0j7YYUVor+zQutmav6odKbBBMcLnPr0GaZU/FD5CR6EJmArS5zcUn/hCFhJrf4ggbh9WlYoP5MPnKDBxPipvwbcGI7JrhNiIjT1chtNVdcdSYUXF6xXB67iQgml0jR5RrKNgOfz5cMOoKNaese/zXBbO3DkWLMSaYno2LbG+jKLY5sOq+PT+gTA9owoMnZmo7cC/6CHAJ9PsSJ0AfjHpHXOYGv9S8zNkkJLHMhha/g0e2snJGuVOMPCYkcwrMZ2GgsF8JbFjUjZXr8z3O4B0U81dY05UYZZUn50NJUBVwufFNg/cdLUMD+5eoxvUErhHUbIZm/+F/fWDl4S93s5UzSCsq4J8ouOIUCGwH29yeH4VwWB+PGsUiWRkUQ+/oyNPbmcC1obn/IMdVN2bI0HiR8wdEychw5fQzNqvNZFmlTx1Nx5CZq/GkaEsUUgkUWP0bypIlP7qENkrNw+VKfYjw2BK2dP2jUuS6TFkGsQJTojaWRyRxNJw+AZ/5TNqMMPJxaF+lBZzlL6XoKvMC7VVCvadh2BP+nmDWyVCiAsi53QchTBAV4S3Ln9+CFAf/CsEK+FfTCNwFI77XXxZE7dsjzJvZgdxl6EkwP/IPaXWCaHMOkiVWCdv+NwZO6edWjqbkglGWhZ4AwsvjoWBCDi34RLUYguDgkZ2kduDzQGzvoiLrU6s9ZU8CPxPRFgC1EaCC5h7NHPiQQTJrvaeAW25uUvmRrWJiZ1dXcqRMSTySARsvMRx84SOCwaqyVLjsUU7jT72/qHpuP/6LT4rvCrBq5gSGmw5wjFL6yFwJNy6Cj8iqoYkqCAkao81yp9rUmT15y+odFygP1TL3CcPXQmg4PfhPFxvRwkJtE5mH1xIPzkQI3T0AwLfNfStVSqUUD7TyXuiYDoy0YW9FFmLMVt6aEkGng1A0trhAX3CdT5sCTW+HP25+pUC+XUhHU0lBaj3SvipfnyNro0QgtyOmj+JxFo6TAcjdDNquTqhS9Y9pRix2EkKCi8jeHzz8igOVP4nJELovlR/W3yBVe4XTj9wV64SSLFlEzD+2qs0l5PHhGC2ln+WqSNQRtmxBBLDQ+JknjRTdfNWqJwWqPH6nEc2kNseOcBAE03glfCI6jr72noRPy7qgURG8EXq2Ze56t1KPsEuwK6ZZ8p0JcbuPFBH52fGd6W5h/t7uWJbt54BhpwBqijzU+b8Go6w1VnupWfI8xelaKsPh959L7QyHBdOgjdpQ/Kz+cD09W/XlePAR3Z+/bY8TqvUtzJKAmlmKjYX88l+C0nmQXzrsw6O0fyvudu7kTwBCRFIE1PQAZqGguUUw/5M8eVLmVPTw0tvCRsNcFZngUDNOxHutsIHiuJiX02V6r0O55/Q1xOEh4ewYZD4kHshQ076EatPp5dSov7BNUHCZPQlMwnPwkGMGZ66MEdOi5zt4UCeWCrb8qsbsiRLv8Ze80IKxdQegip1vUPXdvDtzUFa/vcqCeRPLQbIZVtID9wZ4Wcy769QXneFwzYZAGlZANZuOgH14BfjFqFt9+6eAKFPY5WdIwDWh/tEUGax0/7dhbgHbENsFOgzFwgPH5Qzqey1lYmG4XMIcz5682Lg0c7iT7XNYCGzSeaRLfh5xgCFuZPDFqNApm0/u1cOnX7WQscpELkQtaAiLlCgC5xJOaqO8/mKaDeO8WTgStVV2nO/iB6WyD0xFSXhEMcywcrqlPEky/1cX/ZvizQQAoSE7KDJMAk8xzQXyTAv543Ff+K00/o3gLcbCiI9t7VHLQOWQHiKXnKhpLObhMaSS7tv1zYH/Qcof25xHSUAlnmvVB0YPLVLf85nk+FctzI2jGVDckKJ4pst36n9ha9hdiaP67wyU33cUQAdJqRc0tG3msm0r1U9LhSz3OsG4S/cDyInZ61DMIL4EQSq4MTbQlC2nXXQ9cXfUt3ozBHyIceNKm6Ch3sV9emLRh6Z/LAFpv5aPnRq6f/Qhn22Kx1OBv97pTe7+lHcE+7os7DOnE9/UsvFji8DrReCyPxS1yzmaFUM2ZDNcTFlgPoXe3nljjNeC6+xzfYlm0BNA7uSj46XgpwpRRZUdJy6f1qHdAepnots05/g80QxFri9dEo8ZtU4nJBZFamakJDf6dB2BrvbC+71/61eeSoQ1brAUuU27vVeI+a+RUqY5KKoL2xqJaiTvQtUh99pVj9i5FT5yOxrnWnDSYpmrODyREs5uS3quGpnugQuJY+AQD2H9zkJqtMnuHGPqnsTGlixm10R8Fq40U76Gax8pe/+p51H6nZxADQfK1VipAOPoJHNsKfW8L4LB/w9kNvMGUhdIdgVXPfWkecCP0uXWoIiPlNx/t7SIDfP0P0HJ3MHmUq8mTUtLaFuHWDWmaqdTrIOLAEuN0eT/i0cqsGBpQ0vMOCymNRyL68ErQsI1yaPNoAalDQlBsu7dvqUGMC0L/4hkaQjdNlYESRkENOHrHVDQwj4hwA1frjfgSVsu6X1rAp6hmgj/I4P7O07o6U4dSex+Uq7252nERlwTe48gVSEVbgwInp2I9kDrZ9kIw/0kow9OgFZQoCKFt9W+pp/FCw5TqDqpJzFoCupMKylpqAI5fgPAkMEVw07JpWOgSn/jluT0vQYU1KX0Q5vkDeoxVDX88m2AHqNu7+94+TxFbaWFVmDso+zd7EwFe0W9Cu+6qhYWNn2tnlmxwCO4CRqZ0feYQpXqpD2lDlHIyxZXYIF2nw7ywBbOFFRsHbaWszua8DXddxSYHfTbIbbDPEYa644bQG7JYwzzRIHoDPj7t5VqdPWtWUrl6ROIMwAGX6INC4RPnzROq9y215nRmpP1YvIDyC3a2AWK3CJ3dgBKMg3c8tFlT4qQ4W4EzDp8lCWfI++7GzBINsBP17oclG6Y/Nz2TQyfXbgc/Bv9CFWzIpVgtoqcTGkaYJ51qTPB0dPEnd7T9+kZ1sqeZ6B41lL8usvYhySWqNVUv8U4uSd07beVfSJ+nOfF2qnRB0KQWT0eVqPnzZMcYeK8na4OblgLNu01XsrjAJdS163jIzkCEw77g9nqB6nr/w+eBSLEKHyjz2fsMbUIHZaWLPgk9e4/kebNOfoPRHW8DXbX9P+rxmxtBJkIOfh9qmfWTWvZua53/MQWCuyqXVsUOPPOj9w3iaXHSFzp9iRX2ZT892LsHTZL30MuCALAqyWc8lUlDxI3CCC9eAEg/3OWR+tDdm8e4WVdymMJScwlTXGneXQ1Ab/hp0mxQ1EKb8N9wkWGCcSrQrtDLNk85MOoj5PUhGywDxMqxnZftthwhKetvVcMg3bVmyaRVVFfHT9YiXtxfpaja/H79E4dl/UISl+GaFPC11PlcwpqAmagbIH9n4bl0InwsSnpqCVmyhgBlWQ2G2EnbsbwkY3wzNm+IkR1KH1tbH0pRRjX013UyfPq64qFeLYKRsYADvu7HGfGE9IZ9KQ04xwZKXsJVz5TRZrGzHnp2AOwecPruBQ3tMiL7Wiz4TH5KKVwOvFnPGj+vL54tReV5x3oxK4F+Xj4tJBultHOg4Mwacegm8OnUL5fP8jFqatC4xv/eeqPt/CXxXSkF2m2arjh+0Plv/DA0YL67W++qeNNvr0dOQoq+dI/whPYYKI8Yw6cw/W2NvBrAyW0Z2Z3v6+B7uJU0WAPzo9GUofJqv8jJXoEcW6SeCbNraIqqIsFxU3rA1gHN0U1SsKIdZsWbeR4HuhS9MB8+rtd0z4RiXFQwdoKwcBqum04slj/wo59sWOFD6CdzzDAnAihgT/TMdAKeeyk8IsDuxdjmJ21+vRXD6PMILy28MnOlal9BcjRMOlD7fhgfhuCigkXa0LpkOrOI5O1ehWQldk4a+bFaX0D+5tn4EwC2I2Pbmde581jAUT+xPPNIbfJ4mHURK3eqHknOhmWP7zBcs3PNJjogd5C6GqKmvtUAEaX7NXsr5niZ9ovszcHaaHjx14tLYdvhrSDQ9bPiC4X/amBcOt1GORu+HApAM3YfDcNMYJRJmB+rpCeWUhBcE/uR99Elzwu4rEk1i+jEXrEFDExTtSiLnwWHFF1gJTEbuIjoMumID6lsqpvYR2GJ9xvyHDEE1H52GQseoJmpVx3zGG0ww4pJM22s/hHwVHNiFVbzqTCecC82XwCM5Lo/zKSUyZ60ZNg/oYh0aIuPcZeiwivmsDSYN5qL/hfEi0H3ytbf8TbgHzjNNkaKRfu/rvDr7VZgmbtsiBZyNEcuRZ6F6TIFcZRiurEs//gkb0c0fmMqc8UZY+qKvEPfFVxvPJGuuAYw9vFjBhBiXOyy7lnL4zGIL7BB95MR3YqYyuGVpx9VDESHRqPhB6/WLbYsJmTM4ZfXLPMP4pkC53RWlqhI8kI5MbwrcUkJJOdmUtJ1C4wSYUHuE1X2jSNZa4+YLg5oZx6rGwlpk5pz8VbtDaP0+pnYeMGWz8u3HN/CGIPYpl/gDwXclFHbasR0Sv1WvAscP+jRcm2CnaP5jsEVX0zDj8o6J+iQcSHfuVhlsl0VhihKFQRVdbtElwj7188ArKVxFyiDP8ZSKYe4J9D9tHyQ4Dxfx0tHoxUeSr7t7WDwmZCXh/9xY79DxOVuC811Ys8wwYy/7oGoS8bgU088m7A2J6r8DOR4hnJIiB0SA8uDJBXAYBU1wiQw5ZKtn7C12PXxju+vltjDefoCmiu9yPvGjlkhVC3ExUB7V/JmZ8JL6VZ6afH1grKV0Ejt4W7tjQeJJuc+YewBY8GOKB/u8IfCVDuDmxn/QhMEnRwbAhEdZxrEoVbvC+YDLY+rwB0Tg/LlEkLc/EX8d/6sVLiZfnKyZuGaeiiLuBcSh3OaXMghyI9Ik0DtoL0FCI2vLtRykg96MdCikCP3ZXuow1+JugqFAAYBmLDo0q04/dUe3WmynhzIQh64rRQz32ApsUKGQaAkWZMyeMSxMaXMYGB52wYH817GR4I27BTuJo/9+PabYDlvkv2mJUEvuEOfNl9HKTyLa4xsj5KEk6eQVqqWytz5VQVXPfnzZHMfav1rBHWkS4elskhoXx46K9AC29znJCQtyMkVzlkxQ0jIhR187n1GQd3LdP5Uc8o0FP/2VtDA5dnVtGjSX7sGl3+lc0nGBHAKt7sWLlf7jqq9i3rnBjFvCovlc/Vuwi7vXYKzL9WZyvB5Vy7cdfX9eD+EWJXeER7+EQm4zha9FI5D5C6zFpz9Q3gexuj4/QulyIY4biNPc4kaiIQoYeoljXPLewogg2mJQ5pZgEO+2Ru6Z85WIKjZP4PMrn3w1wvF5ERIGCbgu9TXinqgTJnnxMGdmV1PWocbWYRHxi5AoaOxttOuJHmThZZnmRFcjuAzjYAGl5Gh0Daqvu5iiLAUiFGWw7UekiaObQN1uUmtRVqoU6zDyxtlxUD7Yf0VnA8PbDVzsYm8dVYcuZOWgWe8NhO5D59+W+KKQldBGx84WvNWz3qyv/AXgO4hhp+FFDuqBQpipO2dSAUK76FED4gWspDfL438Gf9szSdvMdLDydafw5gazl+d4YslcTUERbMLFl/SfheQetuPj8/PiZclbA9b0CU+FK8jwI+rLAfwP9uhmtpeD72MMWMo+RJ9asHIrlCaW3hkZ2lywb78PsYaU9zrEtnpWIR5eUoL8vQZWpdMRa9l0B/hTaFPHr8NZQN5ht9UNy+HV8VEobOvD9QKDp7oa386TaV99lAFHNxCfHWi02AAYgU9T2ARJZnzRflaROZbJREDlwUV/9xeULOrrkewIR+UT+sb0/s2JsRKmbyeRIGqCOxzBTyzZ5pxV6dQ2wDRFsW8U4SalwXXautOqcv7cLQHC7Wab8mJ/FS/t8Ik1Q6Rn3YmvvGGgLErJN7zB8MYlofY0RA8obo4CEJdR65IHNGdflm7yOeKyHZWSjXnUFIf4hM9mEvHBIH6YAsjTK0TT3Et4U2EPdnLcZtJGoEz3SraTbBGFWSnT0os1EVqGdgYoG+U5mcyZ01cf4LUuZSxjkRhrZIykZmHWuvjInjls+uSMl3C7RPzTNmM79KDYtRpR8yUIhC5vAeLVO9dP8PhrjWHnNlPVbiShRwt15Lyj4lMO8TAmI0pvpWQSFqCKMHGAWCUvAT/aGlE8JDgYLty2ghz2xuOLA8iLconRJo+NtIBym3Npr3IFMupkhm6FcpaotZQAQnpD/GU0Kdmt1kfjfCdwreDAIG2xbSmqESpfOWN81FQspDhd0nx8+dHLgQ62C1yTl841tES7JvD1grAmzWd7SmvhazVtVCXDjnPw7xd6NvDoiVDBk/ZCMsCR+j7bdp7BDud3/+xBn9RpZdmVoltkG4mjP8uMVR8Nwi+G4jEqW1l6bDnBdeGS1HmheEhP+IHTc5sOIRm5uf7Q2qTLtpY+vtWOxWHCmFXBcP4NmX3LNkzucCbQKUWyhjZ0RA1V3LQFow/Y0GBQO8M7WoinoSux3sTzRRI3ec5d9KpypBUt3mZIFaS/QiuudlJAvwgDnBSlvfOLS5RpaotdOe7BfzICM1QdTaLbQ4rtaOhVcKBxpRClL1ZnS/n4KnJ4cQfKyXPPrlX7Jw60m0D9wpuAAomhnu6Nl9OQFR0Q4E1/iHSFQkYfQBgSdkyO65Yuv0/DtIHzPgyfTyTRviUoaBTVyTPRCW3kMTO2GJInqcgC8b8X6Yq2Z+kVdudkSeD8x+GdklE1JdCsS7wbqM3SW6KJ+0QMmOt4hGMJLy6lerBp2qC1k156uQIj7/R9uWwOsB0FrTY55s/3sJu1m390Od7BHAHvkzl/uQ87wjz4lj0H45qKNi/IV8S5wKJqCNbP1jm+kEslC/wmnl3AAvDctpBm38oq03Oy00QRMs4CR0U0gwL9TsXljc36uM7QDORvKF+qN2bxa4hzSwdQMbnN4Ih/kzPIhvqSO4YVk9tPyHvjNsK6f1iQBedfy7/+yWrZPC3v2mvqKyIfdKu8aFNG1XnJcAJiStgKUhTU09B304+3EPdjU0alQJC6q0YNXMOx2DkK+SlhL1FH+MBvWL6uBBOCpXp6nmYN7Z9CDGQSQy1XqTFrRkSCS9rr5r9LhrcvG/IXraMxlbcfq65SPhOlePcJUeeechAozyiqvcns7ugV2ifmi17cRKiODITKyPoMSGen1rcY0CZR4btQJXANZ5tboVbpzB/ofeqUhoUZAjOv9A0KlJEyCm/mhlKMlPVsi904dS2lClzDzjLJRRgYhNCClqzPC6r9cI6U5QW2TWYMUMF30o50dK1I+hXTvLI2YNmXs/OTuRq2gPSkgTTTFna4wHsF6UvI24y1DVxEYjjYDq/vVPhmVXJOe1ujF2kn/WRnqSIOGN/466JlEsG5K9/EbWUAa7421AZLudfsEI/hTcu2G2vV/kpR1WZ0ya22qHZGOXPKNOdnw/F+4DY3saXizLfxx+D+b11QHoumfVxGDgBIRj3FDvH834xvKtDfzNyOkKvu+qWFKw65uyyHFwVFSl9p+dHjrAOz5p4j9jKMTBVH8nskIAleUOQ2dsmy/Ce1w26i3CeJjPGCYB131EwhlJke6d+D4Vd0jBTx5ooEyWXHPsgYuztOIJb6VkBqDUeM8ntExhmTKtUyGv7idNX2uw2rxQIqTidk/xHRSRGM3J2h3vFRONbw6bzBWkhecLQc6VQr21IP7y18p/e7qvJ0znfunT6njN5xCd9SRRHzF9fZ3dphXaRPzzAfXk3HnhhaiCX83a24pcRUNk47gqw1thGxh4sGS0X+ygKrFzEcm3ipsaN1qnD/Hp1CHLKXDsgEHr/PufBlALCci8GeXC/LjZ/oFQciVYQMuC7it5glmiUyCedtBZoat4ryanOs3qFNkZNEpqvghnbmydpwjQASFmImuBr/qW4bWUkwW7EI+k5Nm8JoHFFvB1jR48Xul4gPTQGk+7+gea+IKANJa+eoaHY79w7GZTmC+wP4NNO00eoc7izKmX0v1jBZoyUF7cs9ad0R5t9j9DJK4E5GKFkRWMTOitthsaswpPyGCi3XuV/5JbvFik9aUNcKKT4R99GzgUMiyG6o0uUKn86t5DcB8jLxuDJ5wBxdxg6Tjfqs9+nEElEMlnez8ilLX/wlzk243qA66ssYR1THmxzxR6zwmSuTf+eoBDH2geP4VEuXmM/jS6OGmNs5Bk/cwPdT9HsHiIj2iS0iDOEHumnMINsEhHgLbFa04Bd7ODqphuA+dSeUGYIN12afaRn6UbQe2wLWyjUhS5pTvZO/8Otk5SSO67rgUOYF1gMZlJMpoSMvdZ1tzU4ymNs/vEDUR5sXk+524Z3INlfoFOP2jlRuBQOxvRM1iyorntEA+K0MSnKPrtOzocDMgYRpaZN40fUO3DGXdSPWTiqrQlx9FpbqkNlxQwvC8iXT0wY91nVevrfRxdzu/xspxneN9SmnfcZFFaSyPQjoPfTjteN96sNhjZGHJv4YyBThO+VjXDuhXx7Ls010jGv2UO9BHLRxcEF5OVdGqxSAWBmKfNuD4hksn1U8wiQ3yX4+Okn3ZGiS0VgMqab+oFzgXC9RPuewB678f7+SPouRfJPcDkPGVt42AICEIaTpG8eGgHsnX+oIlDnBaHqBby8mnjoSb+p0gzQo7azwDaMYzRj+a7JaMNBG4DvXGKL0ntGgKOJ81iroGdRdD06mmtXSk4NuVE24lR7h66rRX4Ggx6M1jdZxlsGmH9V0zXw233bOrDqrJb0j9SvuHUgLRq3kJzd7QAKWZyKTmMMIiJldOho54/YDyHegGZi5tnH+O4RzPOkasCq0/1FELbUBwVcUw/nXymizCFHseH6KvAp6KoNsNmVvCL9S4UjU/wjKiZ/ifm4d53uvKkcbiEgg7LiWWB4+2v7PQKslV3hQMvWI2ClJVIx4HVFS8/RPkTaqSY9Obu+oT7BbjoURpyQwSb0Vm95Gjv7gbIYUkWDqEpHXAC9f8iMESaKtuS38c7XDFQNgEeNhH6UcS1AErOw4jbegNNNDWbry1nl+fxPOwS6uM+jQLsBY/RErnOkBk0LO5uT5XHDoxtMPUuqUbEgdsQX/IcMvCoZFczKrNgLgn0W/6v8SB5OdvfOOwaWb//M+bPcI7iZCd75H8N3sn49lf658D0rzYIH+SBO0jT/g8/pyjAe+/JrKrX0X1lbz+bXK+1+u7yImORZMB/zqLIAhXTEWP70QCpAF17kBhNkoLMBgZ1Q8Dp6IHi5UsJWLqQMj5phWFUQv1T3b5lRiVOAu2WO3iNKWWgj7ElZZMKu6w1LjvlF9dFs6ajVJdKCdpIIrPRnopOgBYpp2i38/rQh2jpLaxATfO0CPOtPMKJaiOU7QlK6Mrfoj1HerxF58SYmWTb8uIgaULLNmhff17N6n2jJidEyWD1KxTzDA0bXSwUbddlWbnId+wwjC8M4bvpcdV325EeRxV1+fZkVh2Civ4Bxcbmk86uOwX5t10Cx1M6U5vIb+F7GldHDQx5THG7nBtXNE3js9jfIk/0ahVXKHkFGQdDxLobppKkSGbCXv5o3qrN6dZisz2vOSrI7oFnvusagOwQxjntNiqUtV+CFxCFp3oVkwO5SdM1MBc8MQ4Aedhn/pQtA3rcnHDnJflXdqnfVvXfBm7tO9xiqWQrd0liOMAMWzQ7wOjUSB0QSq/1yPrlEjZgIIrCfsuy8YJZKK0Xj6ZlAgIAOGLA4gmgi/RK4AC7AQWap7acv+rGXvPv/HeUaNKIp+5vTwiID8gPRmlaWmUYuF540l0bonSnaFpWofcJ5i4bmoXAmXdQ2E5ihIdlZ3EgEb+ShiJN9e2+vwc5MHMeO7MN+vc6wa69EPt2yYwxwuzlWFwZpk3TK/zyagO/dBYmWjUfGYxsVKqZiu8Xn466EIPS2Q2uhGzj+wM6YNZa4vV680FRLIquD9KDyC4DutG/l+/LIp2B7aE0tW6ASUw8bzjNKdMKhdjW5d2sitVU+ZXyANsDL5wQ97CeGC6yE1MXqG/DmnR1C8BJpZtF2eKENft5jPiJeapTURttvl8+aKRHalGzoJYrISn94iAi2gJloEHV8cFFZjtyGp9ub6OBp5LbtBCOGhpvbE8d+O3ffWCpDc5eBUqZDhvGO4RjFHewG3Br3+/kdJ/wHzvGVW5zLSVPhYboRYrF2EKv2NkMNA5F9f75TtjrtzzKDy/xQsf44YPkAi4+nhe0Ei3pxwigE1yLtKnCGVuqJmQoRN3epqJuKuNogOfSpPbYzBClPxleSeZUvQ8xfgB++Wesdi2SBeFu+jzZrDwm1gaZ+Pk5MXXLCT9ZoNUs63hbbH14neaBWLcbn1mfHZ5Ht0Vh7dqpSLDQlps70olzAU8ku3yN5d5PxPzHw9XLnpUYA10uAw7Y8IjSZVFIO0frBUzwkMD13inaaX3DhHePfJqLv5V40muT3Qx5TUQ5i/p+LJVcWyoH52xogFKapIrChvfdarVtEal1WXbYOMzcLldGS6JEp+0gk+el2v3T6UK6uiU11eGwme3h6mduWfo/dkchQCp4bh9pWBEhhOt2hjJqGGYz9dDAqVapTMg5ohJFzI9EQ8NBYlRLtO+Mat3I7uu253ccKl2lOSJok7kJ4/MiUPeRu5M3dd/DudiS4GWveEWR3pRvWuPl8GMVvAaJ8izHzKzuQsz7QlhiJXRv11Mu2ywgBptIVSeugXhL6I3TRsF/S+qfY3jB/RX5omrtdg5uePNfRR/smLX83/Wd4GUkGboKVVjGnO1eVzqLsSIVSq/6UvD4CLuPLWlpV8lSij/z9WKykE1xFRnJ6gWbsN6PBepJpxhewpUFys6votg1vPs5jWciUiD/Hp9W10+9L7btxG7OYdPh+09C+5c4rqi+axZ6Jnp5OixEbbudJswUP0lFzzGOEHA02PxkjuWBalOhYomQM5Jgg8V8Thj8a5nLTGoqCzYAQGmxhV5iJwfddxEH+OobVI4nkmHPkjk/S8J5ZkJNoNZITo4e/ghiQ5pvUqaMhWrS/6sg6jo26cr7u09z2uNfQA8r/vvtmnCeUqZw37uardcIpPxKLS7qDCPYwAHEd+vTgQYGT10hyO7faRWieA8k30i5yNkvQBHLde1qNiYmFW7u4T0iQzHoOeVEoG+QHhIXorBLC+X3ld/nMoYbcSWLwjDXRULN19E8QoBmJnAHCFLB+ZqCkivBpi2fyOus+lZtEJz5IngGjzgWnGWEbigoyU13PIjpxbjHjdAGj8kGX9o6T5/XzEi+fe+hlENScV7gBqqZ5YctEP/TCitI1YClBUvlln/KUwgutrcAxoHLXRQ1cjws5S2n+lJo5FFazIyLHAKmWbxHsB8UjlBwtsg4iaBxT+YQSc6FS6OeM+m/kd9eA29c7OXsn/TU5e/FHeHKm2L7pVBI8epjnCVH75OLrflouIE7l/Y4OIw6tAjbaA3ARWJu0BO+mMArCDuecZEJ67l1emiCsYlNHdHEBEtZFCXYSkprtDDPDq+RPbC1lReVvhe+ETvIMqfBtUSMniZmr/yjJioT0GF0f4BJudUaHXxlM9Te0hRL6GalK8FF/u8ssDPrgLPvNvUcJTeyofoNFBtZ5/ax0cbaIUO/925iDf0syeYu1R04I/8tzHM0XF367UVkTF7xvdXjS/x+uDFJOCE57vvuxvaCzyGQTR40k7uqqqE7vAYZJt9djPkWsMRAOEVN76WAkPIeSDLgxWLcv3JT0B6uVx2CjgiIqJnBu3VzTlI34+KH1wCW0vkyrrsHCajZ/ZYX19Xgwrq481jEEuwUsbFi/i9L87cYtn02BKWD69EpaXMvjOV+GYQH1MZQ6nE3/KAlHtTctzEmTOrLzj9mneW64s3vJl4dOK1p3WrC+mgdgujJ6iT1w3BV8D/CTeW8Y6Y8w2PAEefLRvrgU2PWwtcESNW6l9BQVN3Lo5v9/SOoW6GxeG7khK1mzE1s1REbnyXtUqXiO0XLD/WBqY1aKX88zCpLucNualltFpUhE8XozK5FOnWfqDB7LlEY2APnvZhPc6491pvrM8eyy9BE9Jn0n/cZjT5J1D8i2770IZu0prE2nHgFcUluchcmhJEsvAXVzggRgDLm8QVl1Os1gV1UGc+Jefxkqk7kWMtuZi4eMxW66A+u/1N6jmbI8Wjk1kF7d4PrkDwmuK16s8upJ8wjBXkAS/GK+IeKpZkQUwTtQTKxfsXAuOp8qw1nkl2gIkIcVsR2GAFh92kz1Vbt/bRwKMdwcUvMlVxzDBnHAFxwYGK5Ltsuv9X2UJmLTYY8s2M8liuFKiFoM8HW0guP/8DEMWAYdLf/tL6SldLiqWXs5bIvuG9H/HfuCo/sowEke0VARYl9MGbEqQV3L1BJY5r302PHX6i3Zm8MdvB2rpN+eIka0xXxaRmjjb3Rif10DUkhGdRc9QunQIELNz3xMBKagwy/P74fGOTwIFhbpQTXruH7di4kf/oKKiaEI7aX4GrEcBVwqEy4E/DYsdSwT3ewVUVToZ1qnM9qzQP3xNnx10v1PZdmTXByZZdjRd8NqHKpEt1+33ok8kx2SqcfD6iJ0bGbXfPPUTU0zdbNQeVdh0I5w9GLdP3oJGvN2Lgfewiuhzu9zbVxmDA0MRxxvI22oSMrqnaNT3DSHJSjsIwG5/iyevthxbD4SZ3cHSE1JuDp7NcfZOQcZJNrOzimdFv5JGYVKNE+ocagMDqaRHDNtGZ26+l0DY8/wQs9wK96etU2XgLkhDzdvmB9i4MaC7sndMOVfteKRoktu3oahZ9S9iIBGdnNXCvihDx+BJLb1GIArBLQ06R5zURw0pEl7OkEQXjdpNvP65B71hxwYHn2CdOC67lgBFtyUXlxlB0ihBTMNeTCCmtZ064ms5UguDAXy0hh060iiKGbeczoR2HKpx5XsDeLDEZIiMYvCPXpWjWcKTDeZaR/Kb38Kkrn8TnSkvBVLy7fwQiRMV2BZhFzpzeR3g6hqDdHJiCF2fXMypWhUxNjUatcQYMV8rLrvVlUKyotMs50qrwxMpo9S4fgla6V2V8Ay4zJTyYi7Ti7E78ZixQPBQtbJytXojkMxCac4t5yNKBTbxWPNVdIEQSt7MqjpmuJ5Y5tMx0L4ww4ctJYpYOGYCeiQDds65505C95reMHagACcODwofMauiiNYps4HkLPkF/SpZZG26zY0K7SeYjWeZe4DnRH/B2Ne4DihhOXiP54S/8++M0U8WDeCvlymjB5KAi0js9KFk0N9tueawhCpzuSfN55hXhqECxn39isES+ZNMLwB8AzrTpH2Dg0duKmwdty1li6LeEEt7ex942IGjuYYH3GTB4AlAaX2sZ08E+2Ibt8Nu5s+RPDPWZlNad74gfLblvRKaxMjSSy8ckWsM+oVL/mI5SEab2yfJI/vc2BoUcsDZ7XGlzaxzrkegmkNgxXQDkBjts6mtRnA8DiGwj0ix5CD6dpqNlRkSVyzee2x05MSxlJAHpLUrtbsGEC8StwSftdCBfomRrIekYLQuP+FBZCez/UKDWd1i++F1UoUy6DmPUSiYnGUCd6EzGYkbJzw7Uq4tRAKp3OxTUg8SMB4r00saTgcrGFO1K31AK3AW66flL27WQPV+dUQvKX3SuaQJozuvCXqf+6AmxqDSt+VA04eXoF29ARUWnX1n+TsFGYj2FZzPwHNkdSigl67S+hQ3CCgAWU5+Hm9IbtVYZfWrhArbKTJnm1/rWAGJ+3w17nsCk9ZtzRk1lzSh4cBotXzVBo6VHJMjLAwpHWV1BhQwB13u9ei/hq+AucBt+GRePnxWq0nOIeT1WPutmXWc5h7bL3W/Q9ynLI2BnXoL+kcmLg6Uth475TdkJf3C7sLv9GDKjDzsbVxJ43pZLzyNeMkg9ytA1K5JKhAxKHvHYpD/v4xqBFfPLB39fioHWbHPy/TY7TyUwh8SQndzmZzfcDHfmk7Zo8xBYI1AuTUFWABTjrWTtfww7tG+F+iaNSpiD78nJrXS/2geFfb0kqTcgiW1CFKsaQ7Y2nhR6J65HnlMZ+6f/LcgGDjadTbEep+fiODn94PUjxrBblkYPWTJEVytDe6vyuvKaG/VjsK2lT3j0e/Fb7ZvqjzVCsAwBbbZCDTH5vrASd1IU870LUTiKvZ5lFMSqzHegAfgaTV22Ip0eVS4CCdOV/XZCtisAGb/RGtX7yRA4Ku6KaMnaFeEsUgZVbvSckVk0FgLFMfFviScCE6z5gFLFLMaLh4AGtqSvm+I/FCd/eomTQa742DtJFyifmWafN4vmvkK7iwwN1UzO24scolwk4nEeQfcad2x2TujCYNPa+pKrxSz/N1S9soyXzIY6wyBnlJnDG0ZuDMRhBizqm2q4kTRFxXOq7o/ZM6xEYYj99H1CJJrF25UJdWm7Yx5fPcTfrt6OSNffhM2kl0H8Kq0MV695TiIWAZLDfWUD4Fxgu+1tQj/RI2spy38wQiU+mXO40WBEA/Z45kC2FFPmAAZi7YP9bhOFLj10js2Dqu1E6ebwbUs6B++lS3orbgzUrXy3WXQa5d0HKzQgqliQs1I4WtSYmhIqbSWGHW1FhMq85hBVxf2D/CNrRdHSrwRug0tj6fGOLzvPEtH8yq9MwuReJPmu01Bq7b97TyX/35mbdfFTNwrtBmK9OoYiV+A9iAnPJRjc1Q+53ESqT6L+X0/ellBxorRbZOV773HbhSgP/7NcDCBBTtCROJKqYWdNMNKGpw+tyr7IgURKx3FquFIL/T53B5gvNY72VV+PxGNamIiN8GbnyVIg/+o032DfnULdSszUZF/Np9egycpp9j5IT6dyH5eU5O+5kcVNl8Y8uRoKZgkZHCYx8vwv+imLTlq0/vgxTxlhJsAZn7f/XzqU/vXFzQ2eaMHYiWHabjWWX6jAfqiQH0ElquWDetDNBDa5O0jlMXm2xOCCxRvCHVaIlqbjXXmN7jMVBcN60CmLMN8Lxq+2kX2hdd9lZYAu8LbG8r++Q7sT9dlzO5roBRVH5wIctHgUl9fmX6afYIcaMcsnHjf/oc+MElXbQhRrpqtAeq+9NySkBQl9iXbP70nL7qbGM8kFUQBsmQUm1DgYW9weVxLFeFVQEjsdtx8X9S1wkIXIjiRsR9mG7B+DGL6SW7aawLojC8m14t1S13z9hQfH70TIdw2230mPFae3x+lOWxCb/NU6oPX+uPP21Hlf9z7ABrVJxmyPdxdIYWvUwjng47oVL1tLWvH9eYzh/46hicB93a/p7G3vlRmpceMzLWH6T4AnM93i+440Cdz1eATudFCizNG8GduTHdBvhQcePikRTvyHNs04CDnd9IC1y2QM4n8w2i0wP39VaZ/ThxQByPhaBi6OykoIX3iToLKTv/9RFYDGHjIp86ythsYto7/RmwssjQTh3QCBa7aKsPPXiezNjbt9Ak8xVQTQS1iQVN4AFCriEw65W7U7OX9xxuxC+5Kr4uhc8utOg+mXrC515c81eMDu0s5BJ8Xzp6tJdk1B51NPu2Wc3rQv1aBC7c5Eis0RcICyqKyHkXEGSINLijUn1FEYupL5292vmwpavHRSy5VzhcNnpSIGHX7QnRAM4tYPI/PGICzrOGBLpNSc0m7CoqciTLHk6P+WNpyHaLQrsXJRWBT0hmE8S8enqFfjAh0JnekyhqwzitU7StCGyhvo6mUPkxkKKdeBJY1ekeTMdD3XlQbTb+hdXNv3jZphgH+4nhi5FfcG5UgazPSao9AAFfheG2D3noFgFkl5/iLBp4IDeNNoaFEaA1C3vkqoA75lProiBnlpN/uf0JWdjl8wBBYcO4Tk7KVJPy6788kDT3R59t8s7T+I1IvEl2rRWlXaj4VftTUtSr3jZ1XP1+T/CNfx9pfhIo5aG8lJ0UUm6o4AGHMWiF1VxEYBPS9h+xYt8M3LIcwNfmNttT0nHfS+EJO84BeeP1wokCFuE8FIIXs7fR+CE1vzyBtp8liCXF3mEP28Ms2cQX07CsL2Ivbzc/XVUcf0eyfwM5L6F3GBJ7QbmwD9IOYeykdgEgd2TDU+qyl4LkT/LgyC5XGjdvdSwVcQRRM7YRmIAG+gn/V4GP8Uqx+WupzsKrayr4hIMoDAMxonbTqQHXQI7KGrs5dBiWLo2nBPhkmuw4emtbrflchpbgLmAJCflYz5JdJ2s8yZ3xt2HN4X3qgl/qzgF96CwJ67bJVeqh6/1lvyVC3zvuRuQCmsIzu1YkaneJtr5+j7vu9lnfw4j6V8bYCEZrlsZb0/vXdg9AcYUT0ne4OPcwNJtDXUUCA1EkpoVtyWAh4+alRB4DzG1DggdJI04JZKVqN+BdE+2yQReK9Hi4WwFeirDyGFngnH9YsLsn8rHJaXfN4UGEGkP8GuCeyOL5263h4DRuuwF2rP1mGwZydzR5iyviMKuk5W8lWYVTBzvAs772kip/C/Fmy1en351Z6geKQrf8K6oslbHtJY+Wz8CwJNBCNrsFGkN+zfBn95b058fXGZFfXHwyxgfjqwGwtN0Q4FWhTodndMq4H/nFhdqDHoLCNtde/O3HJv8tsbSwi3mRrL/IYxdjAFTdds2Yck9+7Xr1HJxur4u7eVsMjuadGHbiHZz77ipwbMtR5X9jSTYW3oVPXC4SGBeLURiDMebCmgeKXO8mqK3HLMVKfM9FDKRVovT4B7NX7qf/HKaqYOAe9YPevKsve6S3qdnmjeuG5j+G/4PWuwtGl+LuOzR4AWkGngjNfa31fZYC6ytyhTVdkV1mXwJ74H+c8Z+D/fxcHYUxdc/HWkSiF6gkg1htXoXW4dcSE2HMvTWyKoVKUV4grdQwAprBi9xY3oO89KVbt8JASUMdQ/5gb9ozM2SngcECXPXg8Ir1JnnPAXTCI+ZDetItm8ZzDOEOWk2pdBcKQloI7ORyknsTBH01FLIdBluNY7Wa9o9IvpbeuA4jf7Uby8nH944kDDHbgJDKDOeCFcYtZG0oDu1FInkSGMX9k=
        - #1:
          - type: tool-result
          - toolCallId: SfoyV0uhu7fsVxMV
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: fKR8zZLPRzN5Vio7
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: rLhvE7K1TkRtjkkf
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: t8ceCl9skIyJvw4P
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: IM51pW0CKZeWjsqx
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 1Iwinl37KcqT6Z77
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: zb4F4fZJYVXvhP3q
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: E0Ks21BpXF9YmeXJ
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.