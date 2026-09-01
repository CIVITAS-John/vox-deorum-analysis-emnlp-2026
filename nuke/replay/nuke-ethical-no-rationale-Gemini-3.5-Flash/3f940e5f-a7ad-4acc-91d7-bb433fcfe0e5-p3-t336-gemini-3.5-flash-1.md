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
      - toolName: set-persona
      - args:
        - Friendliness: 8
        - Loyalty: 8
        - WorkWithWillingness: 8
        - Rationale: We need to stabilize our alliances with Carthage, Portugal, and the Shoshone to form a united front against India and Denmark, so we increase Loyalty and WorkWithWillingness while tempering general hostility.
        - HostileBias: 4
        - FriendlyBias: 6
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 80
        - Rationale: Carthage is our close friend and defensive pact ally. We must maintain a very strong relationship with them to secure our borders and World Congress support.
        - Private: 80
        - TargetID: 4
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 2
        - Private: 80
        - Rationale: Portugal is our trusted friend and World Congress ally. We must maintain a strong relationship with them to ensure their continued support.
        - Public: 80
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 5
        - Rationale: We have made peace with the Shoshone. Since they also follow Freedom, we want to build a strong friendship and potential alliance with them to counter India and Denmark.
        - Public: 60
        - Private: 60
    - #4:
      - toolName: set-relationship
      - args:
        - Private: 20
        - Rationale: Egypt also follows Freedom. We want to encourage our AI to seek peace with them so we can unite the Freedom civilizations against the threat of India and Denmark.
        - Public: 20
        - TargetID: 0
    - #5:
      - toolName: set-research
      - args:
        - Technology: Radio
        - Rationale: Radio unlocks Broadcast Towers, which will significantly boost our culture and golden age points. This is crucial for defending against India's tourism and advancing our own cultural and policy goals.
    - #6:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Free Thought in the Rationalism branch will accelerate our Great Scientist generation and tech progress, helping us catch up to India's technological lead.
    - #7:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Offense: 30
          - Production: 80
          - Espionage: 80
          - Diplomacy: 100
          - CityDefense: 70
          - Science: 70
          - Mobilization: 45
          - Gold: 80
          - Defense: 70
          - Wonder: 40
          - GreatPeople: 60
          - Culture: 60
        - GrandStrategy: UnitedNations
      - rationale: We are shifting our Grand Strategy to UnitedNations (Diplomatic Victory) to leverage Austria's unique marriage ability and our completed Statecraft branch. We increase Diplomacy, Gold, Science, and Culture flavors while maintaining a strong defense to protect our borders from India and Denmark.
  - tokens:
    - inputTokens: 23038
    - reasoningTokens: 7157
    - outputTokens: 502
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Threat Dynamics**
            
            I'm currently assessing our strategic position, particularly the significant technological and military advantage India holds. My focus is on understanding the immediate implications of their progress and identifying potential avenues for counter-strategy development.
            
            **Evaluating Cultural Threat**
            
            I'm now intensely focused on India's Cultural Victory progress. They are on the cusp of achieving it, being Influential or Dominant with all remaining major civs, only needing one more turn to reach Influential with Denmark.
            
            **Developing Counter-Measures**
            
            I'm now focused on the impending Cultural Victory, as India is poised to influence all remaining civs next turn. My immediate priority is to analyze their potential completion of the Citizen Earth Protocol and devise a strategy to delay or thwart their victory.
            
            **Formulating Tech Path**
            
            My current focus is on selecting the optimal technology to counter India's impending Cultural Victory. I'm weighing options like Radio for its cultural benefits against defensive or scientific advancements.
            
            **Choosing Research Path**
            
            My current priority is selecting the next research technology. I'm weighing "Replaceable Parts" for military strength against "Radio" to bolster our culture and tourism, especially considering India's overwhelming military advantage and imminent cultural victory.
            
            **Analyzing Policy Options**
            
            I am now evaluating policy choices to counter India's cultural dominance. "Creative Expression" appears beneficial for boosting our tourism and culture, potentially reversing influence. I'm also considering military and scientific advancements, weighing their impact against the current strategic situation.
            
            **Adjusting Alliances**
            
            I'm focusing on leveraging our diplomatic standing. Given the recent peace with the Shoshone and our shared ideology, I believe fostering a stronger alliance with them could be crucial. I'm also considering our relationship with Egypt, exploring diplomatic avenues to solidify our position against India and Denmark.
            
            **Strengthening Diplomacy**
            
            I'm now actively working to solidify alliances and shape international relations. My immediate efforts are directed towards improving our standing with the Shoshone, aiming to transition them from a war-torn state to a cooperative Freedom bloc ally. This includes fostering a more positive relationship with Egypt, recognizing their shared ideology.
            
            **Correcting Diplomatic Standing**
            
            I'm reassessing our relationships, specifically with Carthage and Portugal. It appears previous internal evaluations incorrectly applied negative modifiers to these crucial allies. I'm now prioritizing adjusting these values to reflect their friendly status and ensure our diplomatic bonds remain strong against external threats.
            
            **Adjusting Diplomatic Values**
            
            I'm now reviewing the specific numerical values of our diplomatic relationships. I'm ensuring Carthage and Portugal remain strong allies by setting their relations to Public: 50, Private: 50. I'm also aiming to initiate peace with Egypt by setting their relations to Public: 20, Private: 20, while maintaining hostility towards India and Denmark.
            
            **Updating Loyalty Parameters**
            
            I am now adjusting our core directives. My focus is on enhancing Loyalty to 8 and WorkWithWillingness to 8, ensuring robust collaboration with Carthage, Portugal, and the Shoshone, as these alliances are critical to countering India and Denmark.
            
            **Refining Personality Settings**
            
            I'm now fine-tuning our strategic personality. My focus is on balancing boldness with calculated risks, shifting away from broad hostility to target specific threats like India and Denmark, and fostering stronger, more willing alliances with key partners like Carthage, Portugal, and the Shoshone.
            
            **Revising Victory Strategy**
            
            I'm re-evaluating our path to victory. While conquest seemed viable, India's overwhelming military strength makes it risky. I'm now shifting focus to a Diplomatic Victory, leveraging Austria's unique marriage ability to secure powerful, lasting alliances with city-states.
            
            **Securing Diplomatic Majority**
            
            I'm now analyzing our position within the World Congress. With Statecraft complete, my focus is on leveraging our gold reserves to forge and solidify alliances with key city-states, aiming to secure enough delegates to guarantee a diplomatic victory against India's influence and Denmark's presence.
            
            **Securing City-State Allies**
            
            I'm now focused on solidifying our diplomatic advantage by securing city-state allies. My analysis reveals many are unallied or only friends, presenting a significant opportunity to gain delegates for a Diplomatic Victory, even with India's current influence in the World Congress.
            
            **Securing City-State Alliances**
            
            I'm now focused on solidifying our diplomatic advantage by securing city-state allies. My analysis reveals many are unallied or only friends, presenting a significant opportunity to gain delegates for a Diplomatic Victory, even with India's current influence in the World Congress.
            
            **Focusing Diplomatic Efforts**
            
            I'm reassessing our immediate diplomatic priorities. My analysis indicates a need to secure influence with city-states like the Shoshone, Austria, Carthage, Portugal, and Egypt to bolster our delegate count for a potential Diplomatic Victory, especially considering India's significant influence and pending cultural win.
            
            **Analyzing Victory Paths**
            
            I'm now weighing our potential victory conditions. While conquest is currently outmatched by India's military, and their cultural victory is imminent, a Diplomatic Victory through the United Nations remains highly achievable, especially leveraging Austria's unique abilities and our accumulated gold and GPT.
            
            **Countering Cultural Victory**
            
            I'm now hyper-focused on India's imminent cultural victory. They are one turn away from influencing Denmark, which would secure their win condition. My priority is to analyze the exact requirements and identify any possible avenues to disrupt their progress before they complete the Citizen Earth Protocol.
            
            **Clarifying Victory Timelines**
            
            My recent analysis reveals India's victory is not immediate; they require late-game technologies and tenets I possess. This provides a crucial window to pivot towards a Diplomatic Victory, leveraging our existing diplomatic infrastructure and gold reserves to secure city-states. My strategy will now prioritize increasing diplomacy, gold, science, and culture flavors to achieve this.
            
            **Adjusting Game Strategy**
            
            I'm now refining our overall game strategy and victory conditions. Given India's overwhelming military and imminent cultural win, a diplomatic victory through the United Nations is our most viable path. I am adjusting various parameters like offense, mobilization, and espionage to support this new focus, while prioritizing research and wonder construction.
            
            **Researching Radio Tech**
            
            My current focus is on the "Radio" technology. This will significantly boost our culture and golden age points, helping to counter India's tourism and unlock the Broadcast Tower, which is crucial for our late-game science push and policy acquisition. I'm keeping the "Free Thought" policy to accelerate our science output and catch up to India.
            
            **Adjusting Diplomatic Modifiers**
            
            I am now rectifying previous errors in diplomatic evaluations. My current focus is on elevating our standing with Carthage and Portugal, specifically adjusting their public and private relationship values to a robust 80 each to solidify our crucial alliances. I'm also setting a path towards peace with Egypt, aiming for a public and private score of 20.
            
            **Adjusting Personality Directives**
            
            I am now refining our core personality settings to reinforce our strategic alliances. By increasing Loyalty and WorkWithWillingness, I aim to ensure steadfast cooperation with Carthage, Portugal, and the Shoshone, crucial for countering India and Denmark. I'm also dialing back broad hostility in favor of targeted aggression.
            
            **Strengthening Alliance Values**
            
            I'm now refining our alliance parameters. My focus is on solidifying our bonds with Carthage and Portugal to 80 each, recognizing their critical support. I'm also building our relationship with the Shoshone to 60, seeing them as a potential Freedom bloc ally against India and Denmark.
            
            
          - providerOptions: undefined
        - #1:
          - type: text
          - text: Lands.
          - providerOptions: undefined
        - #2:
          - type: tool-call
          - toolCallId: mJPOjjGYAM9707fW
          - toolName: set-persona
          - input:
            - Friendliness: 8
            - Loyalty: 8
            - WorkWithWillingness: 8
            - Rationale: We need to stabilize our alliances with Carthage, Portugal, and the Shoshone to form a united front against India and Denmark, so we increase Loyalty and WorkWithWillingness while tempering general hostility.
            - HostileBias: 4
            - FriendlyBias: 6
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #3:
          - type: tool-call
          - toolCallId: KjnFGroq4uNrCZuY
          - toolName: set-relationship
          - input:
            - Public: 80
            - Rationale: Carthage is our close friend and defensive pact ally. We must maintain a very strong relationship with them to secure our borders and World Congress support.
            - Private: 80
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: gpTVDUEw5jVbMnmW
          - toolName: set-relationship
          - input:
            - TargetID: 2
            - Private: 80
            - Rationale: Portugal is our trusted friend and World Congress ally. We must maintain a strong relationship with them to ensure their continued support.
            - Public: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: JwEcAuyW53rQiDwv
          - toolName: set-relationship
          - input:
            - TargetID: 5
            - Rationale: We have made peace with the Shoshone. Since they also follow Freedom, we want to build a strong friendship and potential alliance with them to counter India and Denmark.
            - Public: 60
            - Private: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: 4o6t4OMN7xmM1ESK
          - toolName: set-relationship
          - input:
            - Private: 20
            - Rationale: Egypt also follows Freedom. We want to encourage our AI to seek peace with them so we can unite the Freedom civilizations against the threat of India and Denmark.
            - Public: 20
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: tl3NBlLkgRO4kDXj
          - toolName: set-research
          - input:
            - Technology: Radio
            - Rationale: Radio unlocks Broadcast Towers, which will significantly boost our culture and golden age points. This is crucial for defending against India's tourism and advancing our own cultural and policy goals.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: nVHZQphyXkiD3SvY
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Free Thought in the Rationalism branch will accelerate our Great Scientist generation and tech progress, helping us catch up to India's technological lead.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: n7rRvIOqB4nw23Rs
          - toolName: set-flavors
          - input:
            - Rationale: We are shifting our Grand Strategy to UnitedNations (Diplomatic Victory) to leverage Austria's unique marriage ability and our completed Statecraft branch. We increase Diplomacy, Gold, Science, and Culture flavors while maintaining a strong defense to protect our borders from India and Denmark.
            - Flavors:
              - Offense: 30
              - Production: 80
              - Espionage: 80
              - Diplomacy: 100
              - CityDefense: 70
              - Science: 70
              - Mobilization: 45
              - Gold: 80
              - Defense: 70
              - Wonder: 40
              - GreatPeople: 60
              - Culture: 60
            - GrandStrategy: UnitedNations
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: mJPOjjGYAM9707fW
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/sp1hA8GVDP5p/EaTk0Gi9HxEy5SuwWZhCYeY1FGYXMoxpSI169MZPPtOy4yUAIvfoHLMrLwH/VOb5hdXiigQD2w3/p1O8qcooC437t1sy7d2iRpqMYl0YKBqpUzVIpikebLoHDCVDLAG3K2MV3Dv3uMuxUko6T8GmDLTagqj1HXFzBfKU+7r+4dbC1ftuW5tPRt3JN7avk+rebkbjrDosIrzPhuL9eWZnWMIw2MrK5qOcngPOw05htuDv1mHipSjaMVidXxUm1eWmHZrN2lLiJc6e5ym/DZ6Rv3pyM81iA0i8FM+4n+Tun/P/W1nrotdCTPhda8hW0M6BO7ruVuNHRchWzThLwcDRr1dqbdBDrabWRz5N2HGUG6fdZUGJ7p+o3PRFipgTge8+vCqJCXTgZO/NLa5DF8aercuzwfWNYLilKS5sKLFdetn30l7bgwLCZEw0/OwCf++GYnqlvrUK1lhVrkS7Cw7vz7rOczesHtLlBl7vzV0YJlKeQ5GGI2LFobtUTKBAm1SOej/bjs+BWFaG9OFjLyIY8GA1hPEUfN86wjABLykjNv4gyOTJrCPBvQiUrOE6u3MHoMQG3K4J+hOqq3uwF260c3Ww05beF+vKhH1sxECiyBPWUenYgDpiuS/WcldBF+oIGZEhnGbPgJCBEzCqMjm7r1ySvOxC+O7KWYdhpJCn88CaCZ4BA+0CCPb/v2jtZNO3cESYiZMkMSEn4bisRkkS9De2wFXLQicQ/561H4rk0vZ2djxCB0cOLfEpQvZBQTHYaof2t6cBFfkT1hY4nZhIX8Qld9v4SGeK4FC65KUNOZo5pj6pJa4WUp4QuinfAv1p6xxxQrY+UI4SMe3PlKotxynZtl5S/318ie9p5ao5PQZ9FyjLBWmEux2vtInX8YuHsZHvYGHyccrhweoOwLghOHm7ARFgJ1xTT1uOmElw0RS6EU5WSj1qnHuqEa111vsEaMqdHl2kYJWz/wtXbd9rWYMyj7mq55FpaWgskDw5dUz/WGQfLRwdyBix1RUGtq3pmd5nIEBc8hE1AARUMGruBThGi9Mhxrd/SDorhMPD1Efr2UlvqdF8rUQW4uA9DWPhAwe1vxjaz+rwqzRCYdMkouQGFkurwSe8fWSnW1IBA8zRKOe6iIK4vCZEZywgTFWvLUrwp7F11Nx+AgZyPJnhg9/PshIIIE5H5i+16GdW2LygX2xLOFgimBtVDKWeXtTskJL5YIUOqTaXk9LNM0k1B4B2O0k4OgfsHi/yos4jzfyhxRZ1dNRN3WHBMYWefrbg/eQjkWaAUd0YegSnjo6gQOBzUkSJkuxm+12qahXtMdFQWRvorprx7ikPk7we8FQAsg0V/r6OzydTgA+1m+4Byf7++yr53hAXfNaA+6o9RWh+/Q6YsIMbWb9Tvwu+If1HyJK/vZF1kS1HXTv3r86paO0i3KshqjZyGd4lpYnIF1BL3VvR8I+swA7ODUSkYlzRwDiK0JW0EuzStvBccMggMhQdcLOmgGasD9AgQNO+K89U6f0CBc3ZU5DXJaeIclI/rKm7kv1cGrlH1lEfT3/Fp3pTHAtrydzXu/Iu11xEwj0+umJYexAjDC81X93asuVJ0JyeNYbqyc23vwYGU9CGQElb013yq7bQizf7Gt8/iPtGTVKnaNe/kNiaVqV7xGLvrycaxgQMq8QUtaNRh0hwZRHw3UVJ6vi36CZu+AYgD6hlmasJVTIpU79cCfi7LGV1hqGHJ7cf5EWRdQ9e/zkc5UXP/BQFOYh+vZNg99ItbzrAc7z8AAkHZYe1i161s6zN6xlO1bQwIjM5kNuIznMJqCZDS1DOveVBopcdPlrJApgTM7AgybKvhAO06s6LcKm8041gGD2m7rroaLuLM2c7cFB3kHTqsmbB9ISUSBO1H/3HUI/7Rby84fJGvyNf07QN3IuT2VjzfF4ktt1iU9sK8GsGvUYFL8hGSk+3m0ggnjTEzmnFRes3mMgImqNit7P4Nm4sQcT7ZuLfWUlDDPGxgY09ucyGlQ/2HBGnPqapE056uGqtibIWE9lugyyfhPgdSFKuvkNq+TKgfHvD6rmQjpOBLDCJQY8RZezO7CiMawoT1WW/ArZEnf1jeTWd/LiYYI5ZgI/16xRgdDGlDcqgqsO2N/zhbXeQDP8rbhN8EshARjfQsjlW6uouqLmyYEKDd2sBHXaCvXUbn7LjqAtWXguEKqvZRSqKjZp/tAR6s4mXadtJ2lNGygdsVQt4hHlp1U9WRtmFE2HI6PpxdHWAykQV0Egh8KgjECNhviGsqPF/fF6xU2USiO9v2YsS88swQIw6ZGoNc0zfQHrjsnr65pjg8vYhy9dqdKD9j5e5dEcVF+5p74PgRyVcIjJRrHX8nFfE40e4fXc2j/l+iXKa/9G8arq9qXBpKPmphQAQ+uHklm4FipoJ7VfeQGHFtLbbPfbGxJefSldH8J1lcDfP20i4DEQXwQ5SrMlxM+gKy5N6dZbh8CKSCB/4CkwdNHjBdtBVtj8des5NxUJ0RqspLDH6P2uX1OkT+2k8U0RIHg8np1/JfdPDEkzgjvKbrZLjhJ3lCZCbyR0wHADfGtIHR+Qwq8qcyHAXFBncyLq6GqQ5LMixBf4oa64mQymYXDByXGY9y07NmUi70LqSFeicQSPDRd7T1eJD2m4hLZv7Fzt5u8//ZFD8H+g0FRSJ8z3VdpKy1iOUIFep1run/4TtgLUVbfIKKVrONAT9CeVe/1QywclRzY7ALPizYKnnMfO4WxF1gzLzgbh1GT/JOHlz6PF+ZyGWaOGTRUjS9tpFDRereKk3W4n78vCpggp1o+ad+Sh9kdV+PFA3I52w9vuKu9wuLO5bWH7EXdMXLoJOsoIkUPohcg920nEAZdUZ4yB1ZPY8ErTG9fUq1TzFl+Wmg14j2p7tHSa/M0EZsStluMB76vh97mYcrCmhCJY9KwwDtHYqtPpJQinlT88rhvmdI8xcEaL5+avKGLv3G8/T9aXIcndgKuwuRQsiHHemDR0LBoNpWh/rAtUAL0cUgYKQj9wTJQO/0tQWEDwvEv6IuH8Kd0yxR8m98uYXixG7FdvijsnAMy8hgnQgZQo7Zdc/gbv1zGDNTGgFib2rcf46mB6shzo1jHfJVkRE8KkvaHLi900oEHADq0DhzeBJv5hbXWuObECH6u/yiCKoL4iWGk29Dgy1H3OmurPp7qGV7dgwbRdEgekmTFyC/QUJ6yGYKwp1ON0rtiIPnETbsQ3eCd+YfmOigyRzvAH8Nq10OByDN6WpcDy6vXBJYX0EJRWfkyDvvjeba60cZVf/cnAm99y0vOkLyUSA4TBtqaHb2I8TNKgdVAaobtJq2qP9FabDLMViTVYoNEXYY1i2DsiyoojFeO0c3S+/gutSdzic7v2RW9oMPMX10g7CaduAufaX5yI4GkyyiWWe7PcFEmb9lSDZdYge69vB6Sz9qXRVQ843YCjamrB7TRg+rJugwyuiPBfo4dLTzKTJV+2q267yecvZcpr+9Q6ACT8p0u1d3qoWfvn3AVKU6i2fmxVKklBe4YMkuHuQrJ+gFDMKhzO4q8n7NmTi3FI1NDpee4S+MhZx3U1yTiWcd0V0goceayeY7tCoR5rFCOg0jECceMnshuMBCp4PtIEz4BW4FFPoClv6tZ59aTofFWVRwS/eBromy8UxTAm3T//mHhahwMiAh6uqI3kxg+KDBOEJDBoTG3jZ8W9/aloO/Xn8PmP1xIHhCyD8c0xdn76HDOlctw3JRV+AvUR+uJ13gBBhXss2Rzb8p95VNHrwMUX634dtBxFc1yPbg7LF+8+976jl88N7Gm3Of00A/karrAq4XJDDBOMR1261zMsaULcUHBUZnDbhm7p+G1wCzW5VdlM7BBo/4l+jUgTmWKxLkZBn1C3brxYeutAFHff6ef18XDTAFXbwxjzsa/oS743S2mDTfjle/r7JkCRfEq4x/OGCIAxnFb6LHV++x3u2+Gv0CezrDPr/HHfX6gl6QWaN6DExlap8UBmnOHa23tydVSFzN+K6PNK7If9ZLyYVy9FUJY7yolUzMHcZzaHWhR5gJoxzlyaCnknLpEQI/rDVJGWYNHkWv8IHzE6Y4KgGCldmfSWaILP0GNGVHFEKyza0QlAUXBTHy4Kdpfk5iZ67ohXhFOASBhP5/a+Q/c6IOP9SkMvGuTx/99a6rJMB8+SJYvcwD74xQxHq4sTsW3Wnpm1AjQ07kVjbDqkt9QnvO/nu+pb0BkWD/sDwoumCP54zSFj6hr6ZfADmumjqvgs0X/SB5JNkEM0iyOZiCe0rjH9IRMmNgdej2ottKNGLXtRjhdy9itnroV4lMHCkgsdBE38Gd+1rJhl4t5hi6WUUK3+RsDSnSkv93Ux4uXqfuWUkfe8IcW7IYYktcxa0fMt240UJCkT/Xd1iVGsHgpVt1+IHJSCK4EfpknP/4jma5aGqb7dYxxlqs/e5bDptrStrozF7nhH3kvbsCGhnczR63gP3ai71WgZXZxvPkQD3yAqPLDiLT35dPCDgYiSSb45m57g+TRFi/tdOL9xK1X2M9uktUarJsXyidyRy4Yd11AaSCl3fRoFTm//EQ+uFe1EBD8JFm5PTjxDD39p9pvuU61cdP62MIDdw7sP9KJlfWG6pkgrj5K+rr/TFqCzmg5jJATFiIcG1fhZXGayAb6ejObq/OxxdOdHKPd71MURoBGTRyWi0twdRh2nVOA3/5M6d1FbTMVQTMtseTakIxeyIcCmx3j4xuKWdzeS3120IfODbgDMIBEyhhzNjRevcR6ZYsMTOTwNDjh+TVP8+SwBkWjARE0w8mheFcwLX6EFacWbEtkLLG6gO/nrGg4Tj9kHAeNhRuAvNB3y3MWrYXO2VwP59FINHkWfvqof3xeKbN4m22E5LZ4U5WBIz8ftxmpbTpCt21xgs/ZzifhR1UByIvToIWtyA3lvEy4Jb7kmkvylYaf0XdaOLAIFGG+pEPIPRZsvO9Gbc5CJo8vYEuR1XgkM/lUrNaTM5/Ril0bnHh/GZCWNAHVr7NU8KI4idIHCAyLROFnlxAxOeE+UrvYU0TaVTbKl/yii8FbaC5KGqsllywZLX3xIQxaSFIPVmLk4pYKJVBS0cvbw8hdSubTIrr2CG0dJ52EN5AAmGpex9wZLAygaLUi+rHAtMmKAJz0qnlRGfW3nt5/HLUQPvITRagU70ym/wjeKLgzrdJAJ621iKVIVGQ1bDgpVunEfnCeI4mxkXYBaXeNwsfOTKKVKfL3DeI7xOV81/49KfG6arrI5TOlektq/GLP//RxehuRFeKNLSGkt9+UqZGaNUm5vrRc26118sQ6qNiCXRMh0Jpdn+S64csuInpTfhAN0QF1B5TpYfjAaxqGk8a9ZaxVyLtsxadxiJzR2YXPuV0iTOUBU4t0X5g/Su42i3y6N2TcE3AklrdqJzwb4tvtqFlFlcfYMn4905Yn1IFUqS+hFt/jDFABvTv+dxr7pb7ELL243w923EnZ8ph7k+y5J7yC6oIcxpzXg818GaLp2tYSgWUrOIN3khwIU3S2eo8NNNZG1NUFE0lebM2/o9txyFBlTCp8kiE6h040mJUtN/JzJ2H9wVt9TOEbdAkoJMIy/r7WaewPh+3Ox2rYZ/SevMdiyRSqkPYyerY5CkOd1+b65Xpc2kTT+kKw5eaEminCrILNnEJisplrn+caH2yD1SmrqX4E7am99KEPnudrRYMHcO+Z1+p46ngZo697n07U5W5jpT4XemODvg7D8MbGdvgbSVM5WIrGIxulV4cTdN1WzWampvMW8sZW0JFPopsuTiF+zyfVHOrHuBFUhPYK2MKzoKg9TgBMGvfSu8aLAJZwxtvvPJZvw8bGkvXJXfeoI3gjko16ZtIX/mNM7MzpVRI1f1abbnAcVqLg97rm4o8f9okAfCR5GOpGFg40lQldmrvM94og9o/nObgh52gu0DzeSrutN37Hy2Yr4sixlcF1yqUjzPLP0vZ2a2M+tNiY+hngRVkQxD9ckAP0w/1T/WYbjP/wvcn0+YmJ4pnHrTaLJNc4/z4SU2ac5HT2uew2e7nNm+6wJz6hVHPLFSYWnjmybWL2ZWB3+NbG8HScwuJJ1p8rXNMX5LkmHD4MYf7T9bJM2bsDCy7gt4dsq85w0ywwqZ3c4VxXgNsycwiIEWs/374UtIJViut+oagvG5je6x8JBnwsGApNmp7xaGGnIHvTyAsYK9PPSnfUnpPE551jAYJNACJ4ULjo7ZdIDyNH1HwiUNGTDpZ8yzpjAGY+2kw33h6UJ+hfHF4kN8dGa4LwJPtQ0qcOu5hdwLb9+72PIbY71pBQfrm+TZfwgDOxrXSb0jqo7QKabe0oOZYi5JCbW5AhnTFvKhEZsZLiN+yd6xcLS81JRz16fVTvcGElp1tjQmeqXhjdkce7q3fN9YUJRaLc5JkWk/QfC3+y4mJDQTaKYakO500BcuRw4mSSTc0Lce8+VjhlybsIIrJ6427EZCVuADGzVYCjPgpUGTk6HsS7pLhTA+tcIdGVBM5n3Eho7UCHRrIKrB30guUNQY/uuSG5v4xqHB7rKBT9LhcRlt8CnbfrZowhKKgQlm4y2D6gt1sSFmKkxi0Y/9aCPVndKoz8BNr58St353iB6GBFkQ+Cn03gnVAxBNKq87K/uw3umHxvzhIYNyoXnMCp/KH/R5kcTP7NHm01jGyoOc0gDkPXyI1xvCDBQrOPtjWE2r5V2jncBb4YF261qTk2kLNi53uTqXvDAHWqQHl6c4iSPy6QYFsyttL2zU+ovdHK73XSEn72ke624uxOjkAfblW7WmuzYE4PklANUJAhF0QmOVEl+5hMJsiA0CeWNZQ6H+ZG7SM+wCdp5h29HjahUqcfESYUXB/pWjjJdz1OPDb3Uvc5QhOZg4orE3+eBPrm7luIvwd+sF9HB8ZsnVSlJPABA9igQGy1n/vJrlkAd/Tst/YKmXrjsS6mcwOokmdaCHGLvWXniZgDS7yngHVkNcoMDCFnsDVVz7ZjOQ3qkxwxwACqI7/Gi8IwjW4cYB906eraiEMTMsO+oVBDdAAzI79FGA8Yv8ryybwTYU3htjS5c3cSbMklNdUuWTeDO3h21EkpBOO1v9/EXWjYMPMB1HcbdO+fr72XC0uThxaRfXWvlhgxoujdubKR2WhOQAKG+tYxEMYKO1Kh2QPYgV12LXFUE0eErOZwCcL1f9x1J2uX+k6Nb3P57le6jYbAS47pWHADO0mEyHvSeoeDoxdEqZeBBP1u+IjXSq8ZLUr7vY6iSdikfaEsEwOzMYBjlKnN7i0XRnmbc/Br0JxuwWzGd/BGF0Ne/2QHItBQAYL4aAgrBmRGBdwnANS2ekfnuNeN+g9QhQQK2k5gya63++Bnl62b5ak4UrRhxq8JoFXF67nd1nZOF79PthMxdQfNMM/u49RuMrmxKF59vfmIuTOWdfnJdOsYLF3hnPgMuZ0xH+8dylJjtyrmpnG3XtKd+LFEaA58bYvB3xoS8w0qXtw4vtP6VCIDoo6EWZ+EkuktaSTb/xJcb3tfjDvXqQgQzlOd7YLYt1gaKCK1eitIUhJgGImcXUUfaGLX8C1WmNgUdEUePbcwp6TZEecHNEuhlYVF79UmbuYYOOBtCrFiapl6H1E49tKfLq/lH8LsgAiOufdxX5RyUJ1dbmMAeTuemRnFAGd2jow400uD8DO4G6YB9Gd6UhYk/XpI7NizSOdrdhpTJsj2Bu8ZzUvMRTl0s4WFed1KiP6rRLgWKzq+cEhodP1EuNhjtVe85EIHCW7aBJpWagFLtDI/lS6Y80+1FkDgBhlAk8FePck2h0LJf/ZnxFvhIUvPYHYWHDoTu7vej5fw4rJFOxLHHI0TevQnYxk/K4tVna2tGuEiDH4e5tofL0qRI9nHY7+tTMtSXaWGSwicVSUWfuSVCDsCpYoz2g3kZColixuVCRJDS7Ys0Vb5We/HZYy/jX9ISJclqRvHa3BJ03db0Kq/Hmo7XewqNczxbcoipoAsTyPzMjP0t2BXBbEmuXMu70pU+9vUL/NTvbFnR1Nc8jqyf/gFsx/28yNxfQpEWclnJnoQHgeAkfujkl+gQ+VsiUs2OLOC1vu9SfFt/eKPPS5phrQeWr38ATg11VNv4A2eFf+FDd/waExO4fW++AwtKZ/sAajW/2B+lbrUdTo2+znSSsPPdlV4dJk4y48OTc/jjwF/GfGOw50f6IM8KAMSCDx65fww4hMAXGlXzGjqVIH7IYfdAHe/KXknQfsH3vvXlBpG1hEUiCH4AmwCBOA4ITXgfxF8sBFWua7a0UjVHUQxd19zRgPc7d1JAlyv8ajfMxAF9aqz4o09uD7XuQYZRousz28FwTLt5hruJFAw8TB3WCD/ijog8ag15fmlPZfDZjIeBrjycqoKPSzBeDU9ayhdBc2XwrNB/XOB3YbY3GCjE5IjCNqSeHQggTQHWlrxEDmyR8Hj+T5/1PhAlKFuW1uT8WLP2CipEZgQvvKciOb5dK2nFXbmHXcwBMStVNSVE00aokWxGItRMor8wWw16Kpm51ssCTfuRxlSBMRO33H/OenMTFYoGMdNEtHCevcypaU5YMOm53hTKlB91utPhZAidVnPmmy92mjahqxsKIZmQ3+WtF+u8u3DREy4REy2RyzUiH/trgO1HKu5rwBH1TCNc0fKwd52joNBJWq1HOSQsYAsBMXWzsRBceqF6YvT5c+B1yrei4yr0XlhOyM7GVVitjIhwTGs6r6WNL7gIj93OBBedPjcNLdWRU7H3RoP7iXlfJsmIay45XDm3yyLrw3KEa++tLMlS/bkj8MG8LrHeSZ9IZ78ClIzebv+nMELkZxJQBGXmOfPU+5gxp9YNjnpKHCYEVRXhTdTql9317QiJqLGcsJNAmAnNVRaftv5kWAxykwz9zRseHgiqbRu7P+Qci7rueLTL2qaV9wIJWqwVqw4y/EVunzjI36c7sGnbhvZZQT0rrKiIu+E5f2j1Qr19NyTSwOgMTDdNldirkzBHbmtFfp3ICZg22pkctOONfWMLZ1SzII9D9pzrt5dOaAduyz6fDWK63NPBUrBYM3p9/OFqbutTRxkhQiJHgEfJaJj+9P8SxdDcMyYr8yewKKecUBx80POBaJEIROBtIs8DIXIMX6hN8WBp6sS+PdNL3VFFi3o1zsCViNjmgYIO+ybbZRMzfDZ7kyHr1ZM+g9ElxJmkauwTG39ndQ3Net+MFsQu4HiU7B/icCGuQvUDt+goaFO2rQeHWcc1+n7OZwiV3AUmFS5So7KmdbhKpnlDwx4Et2CxEmBT2qB5YBTGJaO9/kjhipKkMlqgdiTb2UNj6PjZeQx4L525EisUUtupO1rBTaXeJaJ8djUTo6523Ol/jJQeDIcPWZxlW76knr5vXqlEwBXcryuvfeg0C9QG8ejLIQFs17nuepuaFq6ZyGOuFd0gtxwQhayRHw2OHKlwQ+OnOe7bngG9LTipqOh6TbDHiDrSfcwN8oyRRNLVINPRmi7VGm9x4DJuRu4GAT4XM4TxOjjpZ9/1fUiqY8dbeq/hjWB+s0qdKMnmBRwCffx+2s9UhegyibZ4W3oWBR/UZtiKEcyAlWB6SqVyPMU0fmDO6KPfTniJkJcO54yG+0mqxY2/7GCqA99MTx4hycXZSBbJIvtYcfdiqyGQ+gu5YNliWaWCaQxNrY63zxsE21pXhPka1taumEQRvlkd0bePP1QzibUUHHezQJJHi7GF3AIziJZM198oEvAP2deIxWS0D+V1ZZnsaSCA2j/GZBwqH43cVL4pk3rgzmt3KxMERzALvm0AeYtNItUHD8GKK6ZxtcbfxLzWkiMqn4QaOqE93wZH0NZEDZxNWNxM3Fmt01bEsOZ9bhnrOhfFYjk/Gfw+GR4oBHNDj3Z02ns+EZtOwCoPQN/3yBKx+Mn3G/Ba/fC8Px+zWYWnpw4JIyaNnNkerffXcOXqV4YF9PI5L2LqDE6ePuIWpv7YtP1RRj/11aGN3Q43Spb27oGUmhcORip5FCeRV6QayuUTuaqnhPkK1W0Gt0PSJhy9Dh9ps8thA/Wed35ncJmvuj9dwWuEZSkEfDwSmMqN/V8BjqA1tnpIQI2/FlJYzpX7mPDG642S6TQs5v/BOf0hrNhk+U69LwqMtEhOaz+UOW2XTtV0ZPkM3hPzj7pWbD04s+v7ES/G/3I1+ayfHRnFFVn3FzQcaUUNx5iVgjkoHz1vfQzIi20eJW9+w/fGe1Arj0PLDm0wM5YGNJl0oCdNcG6uFb+dt6ML5qZbiG+2HmadoR/ixpkeGdMVmqqY2yPA+zEfRiNtidWygN5Funkot2JyZy43LxOFRwx33cxzVSbNl0xEsXi97Ywy80unL4Heuyw323e75Chf/ypBLWkUImlP3cwpsOE1CZE3fp2BEbYbwBfeq/hUlKUy2yVnqDzG1d7vFICZgofkzF6X9XdhepKgoTzuT1ev/faI1+OoCCN2J/YnvkSLEH2wVK/rBq0hNZvXb3uoc9CtEDMm0CRikcHrjc+p3OCA7CtE+1AJM8qNXou/4EKjipFlm2scEnpaJDEdICMRGVkbWriM2TswMZtLOBmOZs+lyQ9Bttx9QgdrTVBv+Kba9IgdAFTwRvS2pWmli/DMKCcQ+75rYCvm82Q1GFCsiP3Er4PlMv0JxV2hnDRvdkxDTOy9HD0LS4j3bkubl7Xy/cFfATXkDYKG8AaTcwZCgLYvsdzzMN0hh9g/pLABy3CGPHMIW3n74nrU09JVxC5a0XhXUKECnBU1PZsf45gkJ6RumJ8BMHz1dxKn4b09sGEm4etALH151VTbnJ3tRkb/YhZ09KYloPKgyDaubjvEBjtC+UxEAf3p/HZrc1wHmr9FmucDr7OtWyOfrfwLsEm24Uo1OH75cafCC2xdaKvQxEc3SI3O8s9h+ZNwsjJY8Ys0YGm3A9sbuRo8ibfQ6OG9vAavIcq+x0SlTr9qKD0Gs6Rrvr/y2LkW/ji8h0Nt5oCY3/0ZiAWJ2DoSJbF/jqiM0o5ZFitNOyiPYnrMclA7VAXvYVuIofT8Ms6NTT31KnOmCWYFDNFH2tG36a/laZTKoyy1ENgFilTPdCCxGID6jf9LcDYbpiv5LzLO04TRk1sHEHGX7F+WeuweF4EfQKfIsRRWxD3mop1vv3FK/3iYpfU84F9Mux6igxCaIsKeTuCHi28b2vmNNY3tZQoquUuHrAUYO35seGMSvR+WaKCeWTg3ou9JTahJIcZiIyAzWVV5CbbHD3V5XHvpDBMrQfjDaJStaOFrobilDBRmdds50JMvl3GmjGhrvEirZX+OO4EAvvip1r+Rnr3uka4C/K3BGqxaImS0cvgYEft5CoavclV7N3RDCQ+HUDy6OHRWmJDelK00xcHriCywcyWmNap8jRvWzJF4YtJprTOwOD+W1Gq47/P1P0HRYaXy+bkIBvNurfZpB9JNTt2PFk3VcSecIYnrU+yCp6qTEJo6PPZMd/FePM9b/Br6BVcG3o7BJSmpM+9522u4WXGbcNwmL7m7+UfBXsnTxQ1ljeN0ZfHj57EvaEb096IdZ7lmb3XWxK0gve0hgdx2IHdWpcmL9/yQrKK/cbuHhOz5py+FWK0I92p7So/C6x1A96xraCJQYW1v74hfHRIxq/wi4aRa5suiYBnt8uwreknBAAoWfGpCg8XJD1kyQgjdjOR9Ux6I6tvSeV+IRbvUta57PDxPU48ompVYinRqtpfh+ou6/2aSqD7XDCBkoE98HT/mBVGaXG8AaG9S065m6sXllXe/32S56pxfP7IMoO74fatpEL9J99CW3yTpYBkj/ScNALQwQtSFyAvn1nH8OqJYHphq0l3ArJl441xdOQ1NUKAa4vVtckgaqVuzs70lSGGMH+uet6x6c36QycJKI7f0LZyeyp308p6DSX+jDMb3CIYT375zI0FqH3CcM82rYhenpTx39fREOWE8J+Q10roo6ZiEzHWMXf1B1jOxe0EVVWIfK/syEVOYdgC58m0EbTkgpZciZ6Colkd4afUSUp09AnHuQEhjh9QBqLMcBO1kCYvLBmfpmLJQauHBHukMem3x9/rLoi/m0ueqBsRx/A+K9tVkgVWLsEGvqQsqQqflCbIW0XzuMe5bxEL/8oXoD4vP2d/g70d3pYd1l5QW8QNbbidoIh3oSsJde7FehIpB25qzUa87gWq3nFqSG5q3QgKQ5HfU65v0uzs6CBzSlfBhdp252sPZBtNdP+2zC595HJSEI0eBCB3MZZPYk7N/KBlyzz6+4ZN79olZUgDXJ5GORDBzSRf5nXQ2izgCu4e5GnUrvr+09x3NIiVyaceO0d17+Ar1DF5mcbXZz1EG0iZR/gjzcbQnXbqY2VDcTije1m3dCCUahcKc50G5dUVa58Bo95c2k53JmUNfz95ostGSPeNk5Jj2n/G3R4thoX/e20f3s1t2z0LZdLpQzvadu9h0FEzeM7Kl+2jOJmUAP3eJcsDl1/uoXPK+C5okIS8wOs2WjlrZHv3WtxYpWzWWj2JYvjYs3DQrmnfSR+pdstu27EubO4reR78BzEVpO1RVi/ugW4adWNQpJtb2ixeR6Rcm8n/P/Rc4nhyZkWZneSlsKX6HsL7kZcK5W9bVu0kNNHN5ZUDkg/f2fzafBhUnwt/3X7/TsOp+Ij8bfu6sO9jTRYg0zPYUU8/fynxYG0aZYuBXTnAz8PoEcdWuh/lWR54M/gOx6Zbn6G5/7eTBdm4AoGcE9shA6rz2M5NXSOUufwFTgQg9A1skgC3elZvHor401XZl9FT8x4tbeL/RBVfhj8P+y8pjJyBsz3JZNa20PCeQi+BI28xjeAx0+C3nnDqyfgr6NWGrmLG6AoibV/2AWp3YtbnfCGQkMJbLQVbZZobiYgy+jZi59ScAK+/FbpODcMAtKeBwL7R2hLaHVjNFHDuug7Q5GXgQfbTIbcc8I4GM/GkHN+VJgJwIkHGtIxWrSX0zuy7sNeX8ksD6Hk5DaDmdU1gp8Q7rYKMzrYi+HRqfD82S7EATEAE13JvIcWqZWv/9wPcSK72pt6yc1jxDXt4kzs5mRv/a2bu2LR0mwm9nHstswimVEO1bgMmgdHb6puGOWlJdoqFbzR8cIbJk8a79uHRMDjAvWuu+V0OWJ2K8A3tvloinlzT5tXiTpcFKPFh7GNR76k2AT5e66nxLMWkY6ILQkrobL6VpJ6Zr+3TcOksOWgzPo7xDfe2/BvKAWXBmqSvqKm5G79osU10TNFt5l75fnqX0qw2BZh1z1xIxrArXxO7jqraC3zZWVbLl/kfULTjgKIxmG4qGVi++anBIKYUsvlu06Vf7N2Lf/1gvQc9/W1IzS/qVpWhwsJ8NiYNvP/BiuxL+UprwE4CRm2z9j5zGf+BO8SSSddcexv5PM6yeDdU4y8OM+9YrwjqSzEd8avk5h5NQTtnTDHGzd1+SB8KqjaWXIJSfDCSiSeNiEIFEUQ/Rte1OvLT1fbeh6Wo37VnsV6jk2L6KqDJZCLRv4oZBXJ9syuPtCcuVOAbGTG7KIieenUYkxjUnQc+c3ARiPRSADCxlRL9Caulu9XL6giDq/iG4ua2tyhaM1bRtHTAUrs5AJPs1xIvIA6hSvnKZQAj3EylIZVwYki4izc49cd2TinGjBIbnrZL7BZLsoYYK5u9efamAYwncu8SYquBlML8lNKB6cgh3c9tBzMGS+Dw45U6hNpJ+Gu5fIONAvi5EwshfPlo2jWHF1eyWwf0U4AnFmQtm6EcIYYxVgham5T6SCk30LV8vSUm2E5260Nc8KdbyjDBEoOPCddsVOdEiiZGnlqN+XnTyR8pYqL+mQwpW9PrR3kBjCqG64dQ8QidLLvA4VcE0EhmBSRF+CKzuNSQgitM7rXnimNBoPkaxsT0pvvfwm+10HgtAR/t7Md4LB8JzEwQYagzc0B5ly45UaQX4G0I5LUE4nh2Udvt0Mq5X0KUNDTluCIL+CdvRxBfJmUww1Q3rWBH7Rt1SPT+gPddI86YyqogsHbn5havjG/kNFKwoYz/GEq6VqUpdVniwSMhN7kAnIAJTwj6dS7ei+2FUJz0iwGcF9aHkwh30Uct0kTo3XBdZ4q+PV7uitpfYMkSFhiHiXMAtFxYjzv1Upm52eDUMRpOiYn6jN6EcPT4gFxpS3zGcT2QT8vWYJAq+X7C610iEQxchaLZ7qa8m0AHB5Yq1UfpBEQ4cOG9ClJaXj7GFLB2vyvsP6Fq9bHdMLsw3S5Ded84NiuuFAcem4ASI55yjVrAz8g2bPS25thkRwWs3AQ74Ce3Iji+BXw159BD+cwL/H8pgcEn5XjnPsRmzKQ+aTbru36gQ7HChZqmw8TooDlfb8UAH01xaTsWz27t2UMzWG9K6jn4FlBJNjk/qaBvvebDvBcqFOnLbROafMA/SrtoyhN5FHy6n1mhkotMZQ6I5YX161Az2h7uH4Wrb1wY4y97WC6pubw8Dq1o+TgSYWjFOnTuITk8Rzjjb6RcDkGa5Hg1UC27u/fmD7O2uIggzsrszqk99fKbDHVQGkXDXheNUggLXUILYz5sdy6qXBqt3eXJGeGrvARqGHo27zFlj9rH72lyXSrFTCP5uXWS/Vrabe+A8dq+HBUiLRWTvunokeJTuykowK3R48yGjOOo0Bzpwy90gmk/P4Hn1XLmDoW+Z+2jjYFrlZRFgMt9gOQiDJ9L2coTugqMLb8uBDCSyxCKOGf587lQYcmxmdjhOGihXx7Q83wdDhFOD5SizE/17t3wK3naGrAdo4zlEPI6tFJfticH9eJAdebuFoUnczN0weYvO4W/Z5GdowBwFuS6bVdjhlVPExcTaX9gLrJhXnpNxCYVw62HtlkvHb3PQxAybFGNCoSP/tpvkKb5ELUUkmJHgWY8Fm07jsZE5rdtfjYWG3Tdnoch1R+YWuMYs4VayfSazOIh5kigAkifrQUrIQu8cIj38sXaw5DmHuGqsHPLuwNZzdoK1BQFTtNKdydl6vHlEKknHXkGuJRm8FCy8ZjAZfFhwVdpTPls3TAb1XkO3b6Mia/s//FtQCxCWhvQ93o1y9OltRHT3vbQZVdu5pSW3PiPWZa4LPWFcPGuv3FvCvfuuc7ZpmeDVtC5GJHSLJWXDrzO1IZRbw00kWhx4/Q3ntt0BAtvIx50G4gU+8ii1V07jXKXkA/qI+jDZUm12YuvgAiKq1ZS8pCkhg/5/1NBcMOBd2cWJR6i1d6qn9nztyUkseVQRXv+yJB6p/P30OqWX69KyzcEs0pAK8QGaVCBwf5PAhdounwzeIxhA1+6kIXpwwZ3YfAqY9F00931Vw3hzTqARgy9YBi9UfQKcHI7j8pqIGX4U/EZAsKFssdG51/tq72ZyStDC0KdS0G731KlYIjoQR0vFPq3FCMECglzVxLbXmNFOSiM1NpTqwvwcg1csMCBP0o18qUX+L++IsZmukDymIsQcruzr0vZZ9E633ObANUeu6UI96fWJvTAUPI5F5n8LtZrmBoTlD/xzNJcxyCQBS0rG9e/jaXw7cAt7+/tV4012oKYwnxREvEb3oc2R6igdJko5132dJ2fnpo/NvXH1l0SELRFUk97KS0GKHvSlcInaQFIQEQXvnMpptHH0u/RYGBw9bHRTnzEN3B10+oqP/tvtBrOtxRpRHW7pvE4gJ8V5UVbiZRBQBnp7eUxVO3iCRwVrLhbFASa9rBuppQ4DmpKpBEnLUDi2wi9kL0yxUmCuBe9aoKMDSWbuGnVi4p/62vVBJfiXbincGF5Zpu+sK1CCRe2X9WQtiKs2EVWx8zoPClqE7B8m54WO8mcl3YhGbGM7pjvG+vTkdm9Bt2VVZ1YUopcXHawuiUX4cFXg6Wj8tU4wLhN465QCaY/eo4pplFv+ds6mjUQ0TRvKFZ5WK5Dry5E8cy8Exi/rTR0ZlIi1q9ryVNc8LGqKq0KaxjMFO7VnAdASnlriGGLnRdmTA31W/5+ITBtkP639N8+jiTn+4rInLp49IyFesCSiU+GhlD3pB7IOZo/+krckcoJdiPm3ABNgRbWPa2mT1jiUXTmeOnwozjaTy60mJoOsDFju9/v4s74li+ifBetgc2AoI59yKhs1CrdHJf9TpG9EUNtIvYX8fHXdREp8XBMP9p9AAjTjEE2BeeJ0wnn/gf9wxo9X602gP8GHwhRFXqvY+atpCBjDpC3Kku8/hN+oXn28uqDYSfmcV2YhIo7Op6ykNmKQu8GYKVNXKM2xijoHBTSW8XEPhgmndRXYrRCva+jQ3IrElxWm+GiQwIxMTp/8n1pORrpWt23h+SZR4GgJoNZ+2nfHYnfjVaney/golu2PgRboxtIcCOcmoSk5J+aA/dFJY+mTM8kQwbS6eiwxhdmkZIw6bSNc4dY5fLfuZA/aBFvO4tlmEbrLNpueI5+N7nI+xzZwDYYwdQKT4hYClwtJ3VW+WjfLmB9pUAI1e8w37oDxjhVgEchnZofmQZmfyAvrIyNUQ21/v3c8cFN/q7CThTa++tlWV5tNKwnnBrpuwPOkCGKS8u6P+EKmEaqABvMUDOwQ4ttEMMjEr+GdsaUbRITv8i3ONM/4fSMKmfucZF6yX3iiQEmklJN5UNikAaKm956AoJEyUcQx/xTJ4UsKvtSQw7jhxGXZPd/CHYK1oD7uM5S+IBTJixbgtlGxFKG83Ox4cVJJ+hfVrBeHcXkAH+lCnr/JdL25zwdviG+F/yigPG0+8+qtVls5NaztGK6gd0g+94xs6b1+/tP5Tx7EWglGk6BUxhoCYV4F8nRbwHS4pDX/u/ctV/4u7naH2vXLTq/tVK25FTqvkFORY6ZnZYMoqh0lxBMex0QQHY6WIncA51OZ0HI8kGkCnZrKWrXp3DcLZUbSTcPkWf0YpRNN8I/VKxkEMT5yx97f3MekG/QeBB+lgVCAbJPeTWJ6lcFwSUY3n0QJz9qLvdxnKhckasovOgviBVvq0kzPwWU6x0kemDlh2avxZW8WWux12XJ+ZxBG/Nc1h19cDpPYxTCTpil0yofPiiX6basA8AXg6ueaIIs+AC2umFQyHEc/zLNvjpYoh+DQeCpOnfOH1m+yCYPnI06hDHxAjhZT5U9ejvNM2mRP2+9lFge6lExU5yRbemF9v6NNtaZaFoLrtlEyX3AYVyvvJa19zIb3/EEqw8diE/4aO+UITAF2jKRCZcBdOzi1EoGdtru+1v1UBM92NW2KY8LafciNCwiTdwdoV79Qfhsk4kFuEwlou5fVKuUyuSKgGMD0I+v9c7cLjQjAWkNlJ2St5//q8lu0WIS95LD4gJfUU/pQBK9z8eeWU38CCWzuqg/wsZ/9WD4Gz32m/pmQ5RvuYvm3PBoWxrVe2suBDFEJCwxNn0g9iR265yM3dZ2U52oaZcbl5xhp9n8IxzwkNqwBc92y2OFyvE7VYgscTwvJCfqiRPxJstHkihwxy832CPb//+dV2s8+oBnYgd44bsDNE7ZeJzrF334D3WspAJVgrer600OHEfmutMSF1f85aGKmUFifoy0rMRmBBDslWZgoMpw1IIm1OonX6URKfV6B3AnQJHEO5dyaHuVMVfUYaG1zG+fnpGTJEWVgrWqG6lp7fwgE5KMNFCFoaKKjz8F7/ZOBsfE81AEWsJFEWBjKELSvWZGFeIH6oPoNjBLdv2q59tWrWKeYvZmfUDDU4it/ILPNzNma10YoETQbRXg/VvbhuAK6NRnLcLOFDcRL6jqMxWluHTUuJ8doV7p7Yu9KBYhfOssGpsAyu27rZVm4WA8dk3ixIYK66zHB4gUR/f1NDfROUQbzEXammMsfmr+No1zoaIsj5SSbvnFfj8kACaulUzE+wIwAWyOJumhKFwtNAjGdkyQKcrgFVfWJIV7p1iuIuDcrMySpW2iTMj1svWu6nCdnhiYUoO95xqMAyP2PzHRItK0g38e/n74aNEootvk6j6wxlVsT2x627t9B9rkdNz1vTBTh4mzEv4mSF989Hew6+RE4Ilh6lXysxjdmxgApKRW+OeuyTAnO9ZXdLMbQE+EaImc9oDIEtLCanR+w9ynXREOhYzXfW95kqxmmLt2sOYVNwzoBybQV2ZKDoIqSZLYqwOx/5igRTxQuZQplFQPCiR2mmCegPYXnz2qw/HE+ggJUjWU4JiCIyO98AyVCKbg/n21EiKmwh4Px9u2EjGffgct07q1k2k/lrpi1oySu/IYaFmDHTVLh4Yb3t3c5we8LOocLpOHgF0QlUJKXqj1Hb9rIfEZS1XHNvw5kpZK5YLeBKxcQaOZWRDVpC1VjaTDDas0UBEkXN93jVNL98N2LwzE537LG4nPkVOuFyrMo1WWWD+BmFCVBQzHsd6K1/2xlIJlKU30e4L/gy1qDfgOsarLC9nLkumgJKtBmA3loTR1kB6r/TtJmsTZuSv5UCSCQkHttWmQKShNvoqrlmNc+6BisLYRYn0PdqcCjuf3Z6VKXlQ34L3yn4FtIhdABFV1Jv4jV+MwAcOwnNKD3xjpfgrwcjd8px9gMB3zFN/zZW54eqtdjFyXWJoGzmN+7nQNBNwBrC4xDy1aORR/g31pk1Lw52V/i9QOJGPSigzolQ+SluNuEcmmr9jpfx7+EnepQirVLRzCLmMxe2XuMTb2M81HVlaJpBmLMvSe6j5OUyUTftpadQtS/1I+tqsdZSDjQreJS4GRrVzCU3JMnxb69+1w2ErFSMzfPV//MFNwUX8QNW9bBOgTMiWZV5iIBq8fs5rdIsbj+qDbiz89cImWfwHYKDgajwhdZpYxDUZNaI2RYQmEpLedx4/sCjW63Kx6rk54n4M1TpH7iG+gboVJciXW5iGt79m2Htb/GipYJwwPa+h4soPNF7YXW4tS1CEH+UUn5cE0K/e6QZTRcLI6zRxVq6XyL4zGR8mJYIASV+6vf+SkW005VrPB/REhZrU87mdjVV+ZqdxILKgpmoyd7Kh76Bx5VUMyc2VFIMtHjtb0ym8XVeF6N+1M7MZBj2u1dqshIN5EjCdJmGjZQ8yi0J17djCIa84dVXwOlVT5k22Br1vPyHnszUcirfWy7N2sVbSuNwI1/OcheEFLdCTDcNU9OReyeQEgMEQL+TYOrBcvzcOdeyuIJ6nj2qSHj7pax7tmGVr5Z1UfGwBrT5oV43qMy+oa5OI0mrbxEIvEOAIP8vNE7o9Jc5v7dL84oCqfrI9MTtOsUsQvMsxbcg1A5vT2OXCz2Xlm8I1pUXsl9Sbp5Z2xRHU1x0BOM7/aV229femYrnwie0ias+9unsLq31F4Yz7hBxfaJ150TL653bB/ILF05t19YJt0j/+xFcAvFKqMQsu3u0eWfso7niQE8xVuqKEAP67NLe7wguZU4ns9Ks/YQBfdLml1vkWz7Gi1XJpE/uNAfQI3u0ij2mjadGoD0d2VBxWNR7FdW8TTI3fw6ddZHoYGMmo2otPFmMuT1S+uYwlKTXd+Mq5BgSrduwUA9WU28sGwoq/ZUyxkZG7AHskTmzcxvWXDjI049gMxxKWk8K1znNS7l7UKHMU7XSmhWbGNmK0qe40dz+9U7XfOV2eeQxK/bdCyh1i1qyB07KCu0GvAv09AY7Cxv9jzQDUWBHgBJ1KfU/KHqOschSAh8KCNeytRb3f5LR3wjXIWR+jF3bahJNOY2uEMxMERc0NbFYD9rOVg8V+T/cBx+Ebep0c33tRD+YBDiZfbDJ/G1veW+VG/BL1LTcFjAtUjSWJujzMLTIuD7Gx5x25usCsLU/sn07W4sHOy8dfwTluvyckzTtSKA/XSVmyIb7LXjdXBCPrCIszs/7mEFUu7TsNe7OS4Ygy1On0G+rYnQjeSyK/sSg1WEz28PXiy3ZGdWMiWKF1Fl7dqsfRTOO2Yuc45M2s0aqNBVK4O0OtXvpMpH0mkU1hzkz34jWbrfJUb6NL7ht6y8vK4pudGLD0Kt7s/P0jwl6TqoB2ON1hy/CitfBJBnFKsr/3p8++A0WiIpjOQ6AOOlXB51hl1hz2N0ThmG2Gg8ElLHBAeLhwCWVrkTy5ABCTm2jodsnUBNSVeEtQhSAYYhEjMOVAkAGLNGiXrWWPFddYa3iTQVfQt6TxJsM7cciIucSNY9aekLjoX8Qx/xYEXuATpnW0Gay7JQ/zlFWLory6BZkzcLYJJu5G48EX/Xlzc15A/V/2rHnqRSvxtp+VMze9DHAYIlUN5phxeHd+TgZG4Z/ZdE5peqo7pX1P1gnoSeJhjbSt9OzXU0Ru1vWyh7YONexmGnAZNr2sRWmPm8q7fhDZhxx9LYuUdyyTCojTNE3zZzCW7YGv27sb5CV5U8wC6fVKmd/ab1J0MftSSTbkEJ1gDRP5wdF7FbbkGvsSJzuHldklnKl6y8G9KD4NUfthconV4hbVHno0FUtf5BJhD2QTAJq+bYaCZw3+h9V2/EaH4+Cfa03A45mY+bDcuQlriryBzDPXSHqW5wNOgM0AFGJHhEh/oD0OUY54Vp+LEaKQUUgmj5JQZKqpYDwc+MbE+H8JiFesRsGbpeJDKSVEKCZRrkpZh7ejGXglaJtUQOP7ONuJEZUnvPphQKo6IBXlBDymsZdRanGKZHJmSMyNinNkyffUyfKkKbJKcn3nuyYplwa4ChxYH03ZeLtWwXJfQ5y0ZqSAWJRCcN7jXP//GFINMi46lnN96CESUqYL9WyRpaco0rwXqoTXDfETJ5Ugi1UDoS1uHsJmY330sbdCtWCWgez3Uhh3P7kBaiWp8z+TQsWhlaxQ6NrYqPxDBZESJo6XgdivbA6X1+mhG/6kRbCsyVtOXQR/fj4zJtAH4p7MVCXa150sqs0K12jXdUwEhivsufnhtP00hdXl6zWs1xKM5jIciyeV5bMoIqEIS+OnahVfZQODIRCHHodbRzps6Ywdi5L2u0aWDbHPXJM9gN5sAHZfsNx/1ZgxA1vyyyofU1swDr8EgaMRJhCayWP9zrmHeVv4OUsH3CI7QarVzbic1h20GldUDDNR8zrxLO9xKX2tD+LMtRC74bnpJQikfV8Cj3WFUXSil1aQOs26AY+s3xuIoMZVYo3Lk/CSrMu5k5f23KWs7tP1aSLHXiAHuMwBEyZBfXE7IwBb/uokMI0hhT9ECVEumgp6EZkIsXMPJGcZtQJn/brAJQT1rFFGxd1/2Wv344HtYP4nLT1YlS1llQZcsY/aNCoPo76ugCv3Ta8kDncuRzRe0QjyL80jKWBnygsd+XvkQtX+SI8KAXD03tet0bDArT7RggXl+c5MnNbP1OA0I9K1sPNrJ85DVXtIrEsCpzBhH0tS5/7MW7J0Adumlok2rtggzB/ESLrKeSWvyGifd6Fk3EZBG9BgFohogSXHeaHg1lsYUt1RQt++nEIc/0twefHAOPm1LVhS5tYignYBrFecVAyshIL8KpGaItoWkjEJebO6oZYs1QHXCZCKdnnla5AAUwmGLlfabMrL1YTEs1IeW+HZyHOmdpPzk5Y39X+s60l/4/VYABaElZ9f5uAQp9W344vbU4ByCTBd/pp2GZ3ixCoBovoNxhJyiet2bCVpx224XSA2LOdOGoDGp+Y1p+/PLfXZjhBfdadkIlIDGyFa8aYcaDsp1DFzpsou2FkueluoB5ni5bP1mrTGiwnVW+olRwJvk6e2w36Gp+ZJcc4JbNmrtct6+629hsICjxGfKOovqKl71yrhdJZBO+R+LIEZbyVRJn9D0OHRs5qmr2txUUdGv6DYqxG7WHiJ8/YECXLdzJSOzGC6hH4mKXE8zNDEND/MMF4OcceovaeIF3t7eYK+ZXj4wJLw0ux4GXZUAOwcV2W+MJq+IOlRJqd3HxLPh1gRwMIFGAKS2izqBOaYKq8w3RXU4InEfSUw8AXrqiX0K6pZhCbyEt8O8B3/y7FvjZZJ5FVAhmzZi70k1rEIMr1DpCB12IFbk7DKYyZOEjs+7l06JH5G6gZhzVM0Eg6SLHlEAMmoFRDYFF8b0HPolOfsdviki/omO0rVZX5Otdaufc0DLQg6tif50oOZGayJC3k3OxbPLPc6Ik0Fk9R3RmmZRPjEznR/ZL4J43o6RYvdp+bnIQ4R1mag8e6zW3Ii+QirszXzycydBNuMErdN5aaqj0Or29StKgMOWP9v5GJJlT/DJ4R+ynoQPPBov/Q20PscVQmSnyhYhNTSGW6bzoKLVZcYGNA9PoI7KVtlMSOci/ppXGjqGC4vhC/yTZFOC7frNMd9+JOK5BE5GTrMxcUFJJVLruv/rBHyXEWd9/kqZZ7pUrucUUTMTPwd/OQTNKiBT3qJZXPHpD0u0B7697SBmXcSa0Yxt3gP7jqLx6+IzDnJB6LROxi3mYWh26G1TjzqmeJdxhpIRn+YiPVVv7IIqPUV6XLpXxCau1wsmZoooSXqZ6ow+J828P28W1I6lHBt/bINs7tzHkomGib1jwvcfbuZrv80lNz5heQSWd4UhIURnKwBupIAMmpU5nI+KJ/rDGeZY9wx8EJgLjXFJOWL0m5kIShfqHP3pH42ow1qTMwaikiEJ27ENx4IGHgEzdp1hgJrL7VnqxXFuwtZtWSTq/hWcL+KpAB3MovslsIUIT2GVkwcH5pufRNrtW3swn65a/OIrz2nPiNL9S6k3wJEA8JoUNhUgDtnO+tlktS36waND/vKWnx1ZOmbeAPvbMpKvLgHoqM2asHdWY2jleY7J6X2wq2Ys7M1gPu4gYKvb9FLGB1B//SPzUq8AE2yBJQohfwmv4AMfMVn1FTlpNZ7CfhgtrdGxtfuhIA75uTzxuodf9xQiatmr7NhYzlwHUPgFfaFRSvgNG7SlRQrQJuHDy+6myaBaqEpiUs3jplQhnBLxB5Kbz0Riz+sDOac4vluKDinWNAF0RMDjzRTIBM7SIXyCwM4UflVq7xYn43YWRqzi4Ks4hSto56eauXeATQqQf6rmekyTVESx+LfpW1RsuKmusDc7amgNOmRU+pGJm3TWf1mQMlL5a7ClGsE/2mOgiNLb1jCQ6iqYdfABbQ3cQdK3ozSbNQWO4lyLGIiFXKjAkPUCKatrDgEVe7Meitj9CivRvs9RcMp4EJeA3O9ha8JfgQC0fuMihCvwp/1ZqFUSyjkmqX/indd7OdBCzttXxVZ/6G+6aLkJzcd1YqAHw0quDTcxs279zMNS4nZdIEEBbhyAUTBI0RE9os4ndXZRF2lrBi9hYUtdKOielo4eam1NwmBrgb5ect5Y+/rJ/8/myn0tIJ/Mi7/yjbpg4cU7V7ehwywALVOL7weNqbgixtqwRYP8cLZ9oGhIapCRpUYcdpBWMW7NsWxxdq6h0/ESpZ3aacrkYt1HW2kcQgQSnqDSKOueoeoo+VDcTnurtq47i0fOaJ/9/bLGSni/OxDoFYVzogthU7UBa4tB29qDkC2QnNxWW/9YBIDmLY2LbbkZ3N8ozoijHtAHCov7U8kpQ1e54P9hx7tcbTZm9uZsBkaGnSCb4sXJNaj41Ulr2CQnhCWFkRNEFuCgZeNs9u6T7eYV6QaoVCtNvEarNpGerDJbUg67C69bWC0akmUAYimtIeJ4hfrktF7sEAefFoLm5lOmv6JhIoHSAwi+aBYcdyzJgZ5kqOcRyrObz6IAFMg2Rop3OCdrmunq/mv7YnW/7wxY0PQlXFgsmf2Wuobw/RjORpDe9RSLL4aw8WVfeO2R/oT9l7Ebr9pN3hdpscsF9z5wLeBkge4ap6tIsJmuEr6Eg3r1pv+ZMtX2Kh9dA2y+OO2UHoRwaSPjZxSvboqa4lK/D7+a7mmT8VfRZYarTfTcJpHf+1Wos4MPs5xjc3iIyk9rrAYxzDxjFwkjgAIShLC/Zqz0Uc4EKfb4OVGuyzaZaJzRssgBf/JJQwGajKZnKv+bMB/gZn9VPvw+DlSnMlqYdi2a3cbOP/6KNr6u7h0NKU1y0XLQ7z8HhMRRf5d/HUDf3ay5GW1YDb4IrJCyvkHafc5DenEFZHWaPZ9mcC4q/ziPxI7ph/WsBcOLDle1YHKgDrtBZh5ECklTtJcRXF1q9NirA7qfAncaqG1Hpw9zlb8UbpU3lkGq3UvI2zSJZRFNWYFnIwNayh7BRBNmo1SPuO3K/IXaa2ryBu7XAhTIvFZ68/0EUmIygrw+teBk9ulb16BpQeSoNhYAImh/lInfrGbT41gXBecy2TabHNILvuZxyOSTqPNwOI5b4h/EfIm/T2JbpX0/te1ZZKdz7DiLzOhul96ILIbfHhah9s2plZ03kIVF9AFeNNIfslF5/6l9jtfqn6eTWUcRZV82/BW8asVP6hqi+NF+HgBehxHReZjNyc5LwTlFmjzDud/ZTGoFCwvoLlGu7P4dinTcRD9b6IOynqbPHUTxi27P3XDbxsg32+gs0b5RWO0nUmYUbBF2cstOEzJXlQTNPk27wX5yiK+yNOTH7tgm9guYBICxL9oQ8MAEb6o+e7nPPqVfmyaRUHuEqeKqJpaK4Ehv2snfNnuk2Q2eRrvqR/X34yo0WcTZZZLmkLjqJWsDFsFR6lj7lFd5GIoLDADfP9Zii6uECabZciM8s1RRQ78ZWkBF02zg+BRjzR7wOcYT4UP0L8abl+q0VV3S1IxXglyhPb9vCjoeZcIYCgaKCh/975xebqfJjLhPB7ukYiWet0VB/akydU/8mYsDBH0PgrStK+pT8eAyfYebdEyY0IezAqWUaZ87oPWo4G4TrOfgTosgSkC29dEWXxBc7YVVfMUeO0rAih4JwDa6lMLIbXSqF+r+CCvDLWjJnoROyziPF/FBc3NTrBAZoIRoKKg8qHb6hj2tPdK7arGFJyOO0nHKjewlruxvwh6pPhHHhm+rS278mcAHM2SbTv10KDY/bumNPQdhsIPl4wWVoxpBt8/PhRoT3jcaQc7Ks7xkbsdLb3ZksH1gEnW6tBKgVeWt2SXTOkX5f9p78f90vsFJx8UkF46+IlyfIOiCwxNCxRBGvVVaLDbQIUYJNBRdfQHGYTMEKQYHnZwwP/X6xZNONAWALlWZ+NHSLwZw8sJv3BOUS6UGbR/rismn2oaADduroQZ5HCa5tk+omUaJbTiGcttwatODqizvxT482qPW+MfgBGe2mkjHWw8GpMEsmOvsM4yLEzTtFQS4fQyaV7JMs4KZMoJK/mRICO6roinFS9WiDjAhaYWtvST5hirxwswHRLc1Z9bwKhU4ry4UpK8qJz+vkQV5YgyE7vo8XzG8pqY2Qr+uyNYZJsmirA7IQMDVUqTvmzoyBq1HI2qkdfeP4MNb7L3CPPasul3e6QeQ0QTvDSOfb6+882DB8kPFQQJHU0HnKuc9s6Tcg/0I0vbAwAkPgJVAcMzcHOX+BJiZGiU/h6lC2FC1m/pKgW4ar4ItI112xYaC3hjB4IGVdSGbMtTyeeXflf5p/Oz7nj/m0CvrR/Zjc15EbdlKkWScUWvMTLBoIoHkqbW0vOjlkfIu5twXM9tCtGz1DUSVJjnugTNploxmRKoFVHMSzKqqlZNun1MEYQdE1oJtRY5z40819yzKbowWn0SmrGXp89otcKh/3oCN8EH7GGLxtyHNLPi+X68SDtxjgYSo8BoGs9YeElNouzuykGhcEvORgGtB0Wvl3yLuxiETFnDUDJJYM348buAczpeNcXT6jTebmHZIdxJ5bigy3kVEPuWIeuSEmq0LEU0tX2HjBc0VWUXfAi1F1Kcbd4DnfWML67E3X0AMHP4T/jd/UStMnPFWzClzDkpY6UTxcxxN0F+nAb3kZkQB1wZ6Yh6boBQBr95BKyhaiuxSReXxmgqJZh1huF4RHahFz2asyhBo4tj/uZCIYomrL2zo0JOiyesiywSFpxnL5lmYGMeG3WPDmKeKFDixGD2YkkVF54AOWjAgMTw6X2YOwdOBGEFampRkOp/iR0Df12WNOhXm00pRkyeTwSh0cmClUFIfHdJc2FhjIlDOAcgoifsH55NpD+1yrBkrxSJSTx/aOBXZGhRcvwWx6RmbXKkCroTX0CUkrDTvAa7HJCqO+EaZ+k1G+fZ/RBmtGAfAag7asSPNnMWuPZOQ22mLlu7hGWSWMkHWm/cppgOVU5Dg3VEZr5jhm2xPPQH+bO3MuhGOO10w1II2qtoasC8GKICxUy6aVECJO5U2lJnphp+vjk8xQeXSz883gh6mD4aJXLVjcdHDQ1KfLsq3Jgvuc5r1fYq/pSDEdk20gD2YSMZq4aygMyiVD+Y6JgBPNXBrx+HGHLNoFYZbTF1GVlpVmW7bkEIV5I8WdjqVtW3aWy/ZfMTPuZ/L7dgH78nzVmlRT999XfuQqioykw/nbPaoL/Yibjbb4BGWuyz1GuM0yMezapUaRoJX0vFnmoRKFgu716ctlchEbHmnh5anXbMHFyIhJKHZbMyDjB4MuBTrIY4D3fRtGTdybdeZDN8LkGf/WhG7/Ir1IYRRKrTijx/HuaZQRZa+zK3lR4U4Fy/Jvab/9jwrD7nxlmbvabc/gCO81Gr7Nl8YddUp7mUHxIwgzTXUdrfmDjCTc7niQUlXSGA4LeVJ9ruLwBOMRYEJFi3SDyMJJY2MdGLvbgYRaL0QMaGeaybcd9QwbPaymN/TW8YTvClzfFTeFfLWLiVkQUggJYthBXIWQ8CWvohcRjfnq2V6ww5lawG854Y98WQ/gAyjc7NfZR7yXGFpv2k6fR3TP7emadKTIF1NETmJ/an0GVx549IarGuEBrHYUCGF5HmbeVKYp+M95ufdXjWZysWKRSdpK1v6MVVUKmiDAlkKa/sIyyvaU7iT4PiSzTDkM5wxCB6ufpsOgSxMPKhF5Lk3GcM+iH+2NeAxlSLkE+S45rO3yUORzI8yWQ0edxzCD9fCgSNKeH0XIwL2aZ7LegQ5Kx4b4f4kbXIQAwLN2RME3rZ8C4kxjvrt2wDk6cPQb0EvJLffioH/wYkYxV7IvwJERkT/bSa2dyqhRG4hqTIy4VkPXdWegDHDtNXNhIuTzyP2bcMu2SWIrRtXvUX7f+Ag18QFklxBLML+1qqjNqkqb0PXOixYQ20L7gR6H+iU9/snFdMimARDW3i5PWTPZhXDO6hrhqnsg+bQTYkiG+5etBH6MwnMD0lcicVDnmfgQ7IwWSlUyKeytnyqvyTBcCjk6fg49SNzAv4dBtwipUKANJcAsZAo901XHd1NTSU2nt9sf2ae7rWRbN9vpyMci6Dc/c6xE31b17TwzPDlWW+RLgThg7zy0eFThC+h7AtyiAi+a61JlNxdfyQmyYnfRrymGGiwlVNvSsZQmph/xq7QUFCCEvDQqwc+dfbF1XWwTSPBZMgUSXQHf+jGKPJZqRa5vzsBzXnIBseAz1ID+KVv8TvK6PhKYdbcS/chvYQPdEu8bolkILCuJxWGixkHA8NeuFKYnneWK/CTD7MBdZKQFjxWFAWOS0qjSe35Z6+Q+j62Az11+23G61oBhX5fqSZFV5E0zwX8shXj9PPURjBTA3ibAU8PYOtm7NjzhuT+iLoRymf06d8t4ePzcDy9rqCzbTquyDCx0dXl4ZVJ7TdYK60RldqS4dK0wwGbW2FbudREmKRbNvfHgCmaemW6uiUR8jd6trE00AdbnToqTKsDv7xQlnu5Z56Tx13cWt0fn1kr7S7W/ea6lPoC2cZyU1iuu3C9vlKHpnsUPVh/QmP/IFvh9aiyztddTATw9vvnvpEa8V8KqWgze8khNST31sa+TAdBLvSqpREuQ8QxJnPZh/iCrNdyU1j7RFn6bJ8yo2R09JQLZh1vhH5PsmQ/XNy5YOMT7G7mkk7/Bu3hsa5qz+A93fbbyFSAP13qjP1N9c/Oz7b10mshVlZlDi64h1jXrLqSnc6APhyOq7dMA39DbkHyXW87/PTqW8zgcC9UyAeZfI+ub3Lz6pkENgrH6ywh78w3QYZyATYTWHUpzvWo7FZS1H0KPdGNVLmMNSb0f6dtHtxtqJF23N/3UuDqc+Rtgd7BJZAG6uiQKGHaLJVVT19DIqKLAl6+svhz7AMhIEOEgscP8mPuRUnepBLgcG33uu1w5SIa2T70xxEDsNYdt4AMObSFatnj+tpw+9taO7N2KXF93StRKgFn4AKy9KnidZUUypiKveBg2CXEAQ+AMlvVdpDvifAxPVY2Sx+eMjVwzysJllI5Bc43SVW2KRKdRpZanVaw7+Bwa2eqs7ZWS6JQWTFaINQm2Mey33qWlMQhpE3wz/ZQNYz4y5eodJMZz8FFVC5Rq6nVWZXG5YkjH3gYlUZYV82UjrIjS5W4zALgZmxzyojH6DYeRW9j7iiI/Jf1wP5J368KdefsWUAT1PndNF6TykID6EayvEupSYQZ7iUjAFubrRDP+aPy3smS53q78w0HVRxJR6iVQWlezxi/F0RmKND0ed7t3DgUjAeD/gWSUlvCYuDmue0PoeJ73ng2BIe5bWm59rccKQuhdeJK7R5Ubyn2i+HCeXcd1Tu4TtAoXHGSRXUWcptoy00G/ZHTcp2ZBjSImhn9aNfF4K2SAYVbnjGCoptANm3rg1vAps9t1YzFNb8RrEN8BLJ4sxNsOwEUJF5Zc5q2TqfYLGelZBD00xUG/dROsldjmhpC5FaJaA+sOc8XdNHXGF9xRne0xdmguv3TvVvliPwfR7YckR/QdCcqDAlHv92Trb1wYRWoF2F+DwJcMH6c5fHD1wIFXvLEaNK/iTct1ZXV6CW9SevQ1knrBjH8BQAJ/OT4spiayC7gMy0g7G0fwcmq7fqNsWVJA56XEWNGuyuguSQkE9Jgwz3ixZ2mJJ4eFNIVL1MQkJVmau02N+lpZG3JOjfu+Js85DVCBM/9FDb+J43mG/mYcHgvaoKt/OcAARz4mXrkIkudOBHSujzpoVeY+ZIHZAPMrTmIOA3YC4BKwFevsMdihMYmQeFHNYZ4SQkkMLL1cthf5BSXeSx+/2Wp+ujyG7mWKFdY1ermlixa8pbF7v9f4r8sgJze+EdbQIV6DMM6cB1l7IbDDLcFm4Qak7sgONohfUjmo/BodQc5UyASvfcjOcgo8JfCvAzcmRtcqBO29sadjbCX6w8hskSKW01bHMNgSinkO6tP+1FLT+dUFbPM6lMQlJNkYWIOs6PQN8WxOiteY1DMW37TJRO5L33jR9mqGY4nvwDh5Y+xgkzA0XBR0dGpfBukFmO3YS8oSPCoP+kdemzB+XMR0mdGhn/YhG8vsyx/ODOLWTkRbAz0Z++BcMep5QpRj7xLc8H90draASlM784l4GLHwMhZGRwvJO7Hk5heqD3eabLST9RSRCG4Iw1nuc8pe/OxUeb1RWUGB0t8gYkDNTLhGaxwsp4ZDDdoeH2j9B/BJ0J0DYKGU0QnLtKaGYUnTKvr5iH1PabKU5mr9yVFX2V/+1xbYz/vdFqBmEsSiYeJHciVfm0hL5bgowF7PnnhpTW3sMmyIlL9UjU0CqsKpLHvR0Zws62sHjCKOclOe4n0ytsLtwCzZ0liR/fjMMu910/VX1zs/q92GZZCJMgaGHhQPONn4Re0tCW6H6HmyEvsUhytFAHwgoz4UJHDTnAaNi5tU6ljkPqOeqs80mAh42G6tQAbwDchDCTeiSzJnhSLFZ8yITcYXnVHAySEhGrNm4BGIc7MVgBhqdvDJlZenZobwYU6GdbeC+VlQEVjThF8my8SRyF+8ZACC3U7BpE2afpDTzMFDrU4uW086HSOOVh9vAzimaO6z31NQtOUBxPNcUQTwWPoBcVut0xrgDFFVUATxJLq+3GvFrDwTJY9EUBi/vz5ViRXG0BzQi++GO8hyhw/m6oa49ARxXUGUTdxZmV4Rvmuqtd+jZm1kewKdpuDeqjZ2m1jNxuWlP1VHiaeNARjejrB/mO2RfGKRRscBtKEfrJDVIEqmtbXIGcfUbRb6dA/PMJx9P0R+ROQPeVqkVLFJdtOWMdogh3LnKLCxhGwHzJQT78fosa2DGI9/sKN3QZaXmwgJpe7dkloPWzLj9QyMj59IHIL+hlOuZDjFlkv0fms0mPTsSlxwPHS6tlgnRU5GMaY5E41RnyDaahz4AjwHnrHHH7l3DbtqTkbF4Bl05j+WJ7aJJWNXXnVQ1ARPHLto8Eung9Qf0NZoeDyL3EHdLQOAeTaEBgQ8IeW/hIGK8ttv352xOUp+Dlmi8BSlzjf0JR7PUcPQ1DQZUH7RMj+RFDB9uXGE+1Bj8Uoro+AjcZucB9OZ+9ypRZwW7qVCMG4oQE41OA65j8//K5ZwehpDjpqBMjEAilVw6O8HhIiQI7tOVKwyITiCrpyLMEYFO9u4hv2EKglSABJeE5J3STbERFRT7fCjisSKQ5SwHZk1PwhPmX1ntdO+izlq1yD/sdLjy07QQbR9rrPT1x/xgEndHurj48sKpLqQD2AoqswZDyjIM7s2AFoPQh5pFVoNRMm6Le/SisTFxXOP2jx6hsbs04kDZJAhlGlH97Z2Drk8Hz6F3mvdoHhwIcc/xDbVpaQvQ+/3QVHlovysVfHEq2DE2XJnSMji9/0OandvrYIcYHlLxb3h0sAwLhLE/1Asvy0nzuNcTmTG78DZ/v8v1v/FrnHVJppQ0h2+cLXmfkmhE22QxYgGVd8meAFByuNavb1K76FIqrre/LM0htdNZeCPn4vv+iNNxreXBzWHPWampDibeSPtFvEJ1a/34Ux+dFnKjBil01pitchYgVMvtL3h9No+rX3W/SL0GmJpI9rZYam9Slj8dkClZ/UpTM9Tlm/0SF2zt2VeTFxS+/95yrDmIdhqd/bj4qOKrq/SsbGsJHJMlB8zwh8s6xdkoddbojCTpQHjiY9nCryo0tKgi5f4grTG6Ygdu+W+XsFb9Oy1hN0ZJ2zJ2T+bfPknF6NipdHQsL06Cg8IOPlrQPKjaMrKxPlVODNCkMuyv2xZY4MwannhQP/WwbWYRhPtQCd9ekrJmB+t4+eS6p6GmidMqHdiMjsN8xWR366x6ar0rimfEBCc1hqElBkHMzvUsO/lAEASxM4ruBajOX1ARBgp/akHn5v/5lWVSrU08LDAyuEUHsiZapJqFhWGyRNj7DxHACe8iByzl4XEarIFHIeNQKdMTuSlOAckxgPtKPc9CN2IcDoQOhJZTCg41zyuUaojwPG7bBbSuAdnIvvLmgtGOtejY50pQr7y4YaFPz1ILah8LxdJRmJADpDse6H8V0AFoAxC+W6Njks+3dT5CcwDJQGdAWUHAdI2d3Qto1Dh5Yc141tItmP88LVoky4TV1QPy+f49MN7bqsnTVywLO9MclXff5FekKS/0QQ3bD1cM1SZEf+jdDA/7rBzgvvQUBeDODm6VsycLP4dXcKstpc67lQ3BjE72Uqf4I3OQEStYXfAFO8r7Rwazl3liVn3sC3C1jPsPEWlmiXzJnVFfmaKE2rsEwZFOeQtrguyqaW2s3+AgRbmH7/htUyGPiAJ+9g8E6ChfmtQnduf9qoNzzk9vgxvRkv9pxvpMmAlx6PXo4AAzUO4mhzWoyqzIIz9g3slQBsqKMFTIW5fQWVACHcBY+aySrL+m9u/kX1IkR/wQoX9Gc4hL2eUGokKzPRBhCM8Uk3A6sivrV6wihy/CqLTNTVEUd2iCrtEAoSWG9Vfmi+WirP25McU1up+PSHUfbkUoC8uwatmi09dE+CKi+qyMPagLDE5J+3BhWOqProj9Os2ZjvDa/aROMReNrVnAmS59cchBZJn1K+HNMotIOxeHn7ckJzRduHBbthlqDQvdWuUGPxI0tkAAN48AnEcKxGGIUExh8LgXHi9dwd8lMt6RstNt8l2mMaTZYeutcvpArb5HEWitYbj1kISeJ0nWQ9cL2bEKrbYcBlLfFlmeNqP9j/PEUVrUuKNZKXqUMrBIgIwiIW/2ab+liLAfyrcwioKyB0qp1lwfyKAvRf9UYtQsc5W5nGYWZl5XRHeduE75t/ic9fWmsg68C2HZrkXNOAbUb7UjHu/WwAKMgqAA7Lg243cngCX7o6VqctSQ2mi42mWsNsVdYk+vOM11HW5DI1pLfVWxpZJ7MNJClzmHPTQws8FdsLYXA59xLE5CtaLkwLt3PzhAekyLpEe0VYBlG6dfY96HaXAJxJB3HIlNRdWBvRLTM2P2PsC2EiOckxJ+XZ4Qt+pM+bU1f3bCacWszAMZvkzx3Nmh9/p+TTj7pdFB1RAQ0eeuD7+x2SQZDNYMTVWN1eqOpheG2YMYg7mve7wlRPsF8RmDOVzwoIU5F5mVhRUINSz7MGUxjKQyYawOx+D6RosHcg4v9a/xv/cJC8V8b2BwZoRnzw7+cfIh2QFZeP4f9es0XgHAHR3XGl/rjnXgRU8QCniNY+5+Tm3WBy7MG7w7vNod8i4WhJbthnOlTt25QIUCkQHlAyviAlsraIjkENuUXpJ2dJ4ZKa36NI5WXSVBRqYHISjtpBSDI18urbrWzYuS69om5a1g5BMDbNPobXy6qoGNC8HMunxmOrxBIJXsquwtnHFtFdqYNO3m5/Rb5WCXOnz5Sdrk11B5cw1AOWILsCQZ9qoJBDqaaxceoKSOOa37Q6yapASJR+jXu/yFKhYLo8HBTAT9pgZuKufsvQuOVF/KTY2AwtsCRcHX/OjYgLP8YiKc+RRmJN9ObARscqFYyUgz9CWk6GiHox8i9sOmpWY8k+z62lQAVWZq81HVdndib8630Z9qC8Us30knPxR1M7s+4pKNsBYLuvuviziZpRL3+n3oU4Jf4DNltTk0qCa3lAbkOO94+6u6IeCX6bio1hEFexPLy7L/bCP2aX+f/yAo8tGrB2Z0+Ce3oOMmZVwL2GJHyle/69rkkn/PEc8WH2uUKyv7HEDvhDIOBJsLtpUNH+eq3FqENXk4N5IH5+mmUc1uX4CN26LlMSsJPrk46v1uxU7MX2w7p2hZj+5rfTJFOyMtq8IwH8ocA+ct0JCjfNEcdoWjf9D2AhfGwD4fAialrMgzr3EOdzfCFwxNo/a+NaygG+7bXC0MVjL8FAwOQbAuvIhNwHVq4rWzTxh428b1gtJeBZoZRC/Wlg+E+fxdoCzXAzCmJou7KJpTXzv7gI0TO98LKoSdQ64IZ4GkA/oAvAbVG9W3MiebV8G7Bn0XW1MwgS4gASJWd7mGuf9srUV3JH56pHucUnpARKr/SbBSy4fNOGAsLr9cN71evnRVeyMxvqSe7dNF/w1MbBMo1EmJ+44bkYnYl2zoQeTrBKcfPV6C5Np4NWAsJ25+W/xMBowkFFBCV4q2MwCM1VDCQT4bX4UHqknPhCA+KXiWbL5VR0MBuTGwwtCDRq5wgEfQ71wcNq9s5ZQB18Y25cqStklSn/POV5HBSOPcvfj22qUNUKjQMj9CeoVt4knyvTSxxoWTjIwcKYdur1QOyfdeRJ/kp9CIV/tl9K1svkYlnuRas3GY4UvkfX4zBnc+JueqllgyG2Zq0Z4VMCsiUJunAWTTHqtfRiW+FT0ry28ECzUd+tsS1uB7FCuCe8EvZn2AMc+QdnvrrsyKzl4e69dFI6nAuBIAhc2bsV70h/m+CM0jbQpC7uubRhBn9NeLqj9TQOE5eGLE6RDiIQVbclkNoiuQ/wZWzRgJu0Sl0mpQjaW4P1qQXXIDm4ZPhMsrphsdepJNeHM4l2EXWI8AqQaBaT23Qe3FfWVPTN20/NU3RALRs4SuleyMY9bs+DSp6++NCs/jBerLCeQup9XQOf9v0zWA9aQAlzzdvSsAeWX3zWScG2yfkz3aUfniy2naDN16NsP2njVz89x9EKFwF76hJ1UjMRsYweHQ44ZozLVdttH0ZSMIwrDe0sOMO5BCsNAE8USBLf+cAodM1wj0FSsU6DCANvpqV/XS+AH3bVCNffLOStvlmmYOSqJRpTh8aWfiaVsgLWJpTEmOlbMpq2ny2MZeNgZjVGoxt1Mw/y1xD91i+F/iGH01i2hbKFBn2ktNC3nhoBFI54Rdpj8w87J1/c4z4Aj584F1tEfOzaZX3/PHfHme+ZU3+vk4vJSnXQVS6wpYMI1Bb5qjLM4reWP1Vo36BrnQm3kIuLjItzy3gtwk2KmLrXAmoiIbzJSKLuPdb2Kc7wNCJHfsVSOGXXAFpzJLsLZTabVXgU4QwBge4yWFtf5QI9b2fMYJleR72g9tFCnNmRRaLLYENS14vhFeCUnFXTwpBvJSZU0L/f8VnkaTT9Sa6i0iQ90swzUpbuhGKIwl4zVbqg58iPi8JmfRWg1a4tWBkf86s3jtCd+KKPnmV2fPU0qUHnfvGfORKOuAzJss1yDGfnuH8FsXH7WwJhzwOumllVwtnGPlu9/G8x2cJRauNSuJbrLl+Mg1sJqVcZY5MFD+3S/sWlm130WZAIPnOUPDj+EKV0JubP9cTdA+sYxyXu9hZti2ykWYwPzK7JxZ07R4A1UKm10xwThx4k1O19lKBNdkf3vVRdDKzAdH4Ix7nTjdMVNxMEcvTCE2C3t/nKtIQAaChfNLztBj3n392ODq+gEWcOs2KWOx+rdZWK545hXZHhWxFNjr85p6USosR9egx2ItpJbzxW+greTaRKp3KKGhTdaFg+EFgOhgOIX102YBkfFV/rACnk9qPhMLNg9YAEFwPc4Qq9UavwQkUffyvNbHxgpLgBJwXbC38Sjq3gILR4GHLSut+qvNvKcCFpWU/IheVQu5cI5XT8cgm5iKDPECm59eVNuk16I7bLsN6XDA1crJRguAzMBQaXPGRWGe6Xh73djlEZm+y6qSmh6t4SdEbdMdjYHE/vJXzEnWu4M9aGNCgBrGJq5seahXMh3wnjnkhsQsjrNLR2nL2zLt7FHCK8VkN+vLQN6g1yzoN0vDDEQmHZpHRHsZUUKur5WGsdxsqYpPIjOTxxVPv5XLC34cpcUPTVQztWapO2Twb32pm58GdKjc2PeKs+1u4ctAhfJvw4Aq7h+MhUe+VtFj1350YaAiFXv3TQFToDWcCkyZ1nx8MbZwX1KYoKAngSbUsCNJMw+T0Sj9ZRNtA/EUp8/N7ma78KbjE3xNyJYucCnT7cZkUoOUH1aAHFWK2rCKWbJ1tMhSI+ftVjadBZFQi3mtCT3V/Yyl1LLNlLTtlr+VcRZdFmUCtN4kO7+CVdFuK5v15CQFzlT7jCOCyyabrs1C1p9U3I4M/JSiYPbF/+Oai9qyJIP2YV5fmtcbFzrE4N/KeMfnyu2bw6KH4EnyS65NDvHYyTI1pzv0UZFvjop1mziz5M16e+ELIj16RTVt5i6p6xHZBjPr+g5e9PVtcKCLyS18pxkGgwAMYWmVaT9ITES4qBvvww3vKc/ciTxlDFMNJfxwSa5tl8EYZCWb3K4MtxBPh2gDfPEVwRoRmbivN8gXZyjm28sz+b6x+FR3NFZ26Y0qFYO54DlSPR7KpDzasslCUwsMdcNVLQrnwQWYrM8H52UZFyyJk9FHT3CsqGMXh3I5rUvF0dKoFKtndQ0NRz2Pv5kgBd0BKBbP11XZex+qC/sYjfLhrZTGry9Kaxxeu3qFzM6D1i7rU7j5U8uMsjKSNu95ddRJYfYTSsKVIB0F+upd/3J2qHATCU6iugRCWIrvsDrRa+XLvIXwdq+NWH+RtDU/fDSh+9NLB1RwmTqHfqAdD0NKgqoIBQymthHr2kCsd7qj/Dv62wxNhgYW1eH5TsbKL2sz+EBzTvry0C78fSK/YLVfgVl4J6t8szSdTgpyhyETNAA68ig/h0t1SswFAZNhCPHbUmig12NBIUBW8AV/t0TEMNzfLg5SEssqGJ5WaSjSjMOSCYOoZvBhzVA2X1eK+Px5QvGxe/4RrNRwnHndbjb3LNNk8AnzTvUtokdUJ2dFhZZ0+UGrrY2AXG0s5m5iVYfklV575ez7vDwKRqP+Mqyumc9YzgiYbm2pgnoCeefB2VR32Tui1pQmxS9lw64yuIPHHtjSTx823bOBhUzfzdV8UUNlrOd+UVBoeuRm8MWJ8L7Fbm35yDl+5fr38L2wvrjldqMWcUI6YrCTFwj4i88KJfmDnIezB+wwZaO/VNeVaSJcUNu8dbJm1tX3vsiOwFkU6VfgSHkar4zA7Qs3ZDGlw+Wfy+PS0XuTz5Y97CD+EpCrSLqFZZtQa3y2SEBkwp1yBWWuGCWQWKvDXiZ+LE9B6pi3kdMJ6GQ2EnUWGUeB0Nvlb9L7EV46DTmZ28epc2TJ5F7Xh9TlhF3CdHCNHeoTScitq5llTKQDJ+UbV7q1chZcjelPGbkMFP/ppW0IPqX0o3/kJbZ6ekXHCt+d0NdLlr+Wnp8A+p6PcySARPaDc2RlTKZQ8EIR8I2r/OfU5IH2eEYyM12M6Kv8nUt38wqvyp0e1a6at+iB61TSxSdMYJZMJKDjQSQ1W17J84XkdK3jVR5x3tfSAJvJDGrkzfBynCTFH/eZKCwTKplsaeRGrf7TfZw5+cIukQc9MeKmjKLyk0YYyL70wEWIV+7dzphsxcMr7qcui9AXxNEcZCfHQQ4vBqUOeD512GJQHwOyO3TcHLSW4tjYvHidl2F7JPCQJV9BWL5ukl/1hpqSDFiwUYjSiSX2X8NEnx3PVYprNyq2JzoyEx7og4E9qy88ZMfGx9d8ToJHLsjtzVLjvOGFjZRnp+H3Vlht8WPVIQsPb4LAX5BqxZs5LbJGNnnzP8ZThAdeK/IMF+QcZK2zNQ16cva9l23B+tNKwtRc84sGNk0QGO8OmMfxIISLZMwfaI4iasyPQMYDgXrBgoBB5gkhDYuA6S/lwe4VHJutfjuSxRqvxXSfT0isH6384KCfCV9tIvXTDN65kvHdwtHzcgLE5fm7gyrPG7W8jUYm9OYlWZRS1Qk2rUZkfJFh5H7JOmyVCXNAgFdUOHHJZULP2YSCug/MF5Qe3NbDxI3FydOuseKN7PokTszora6FpvagZ3TQ07KEo/6sDkzi4fBneuebwRdezMbAVLgou5Hx4Yfb6Aq/WqtmGOwlKJlkaal+Vv4vbZAxvQI5lQKH+Dsnt5dnEzydVxnyBwNSB02WjN6IggrpRid9TsOTXmdwbnNR14lFPUqZ3KJZU9n4hfvOUuJCr6kp2NGZhzIZubcD9/MegnFd0PvdyYkFy8CINUuXm+fQ8UnvwItcUOj0kl8rFYaualKe2+gBk+xO5Tf0k1f+fIQv/JYTJS2NuFZQvTb2IBX6kuHy0E8BbcYblVASPslypQ0PXvS2UZgNT9J5CLkvBHPnXuT1Fy3ieZHmIeLqURP5nRP6AZmXktrBCt4eqOMzfriO5/9OMHuzmnZS/N6V7i+YpuxMvO5Dij4TVp5cgNdmyco9ISvhdanHBEfW3c2dcbMphYHPJEGwjPlYA/q80qAJ4mAm1aj/1wxbRAO35ZbFoqXhC9+6HO5A6+kx6LguBjmpRo6a0KrUOl5IQRfI6tC7B4pFap19uB8pB3DknyPR34qcbduKlbbxzrzZtT/SekqNoMmN8Bmjz/p4Oi1WrQMbn76fjBO/J3K5jlVBlkexH/q0/Oy1CbJsDs2fPWnLKj5R5z4C3FjE5xmIfkRyH5TWFSS3SzazOEgqpL9eP+BQRZhgkACsO6aeIJ9EEgk+xIo0gN9v02QESw4InFmzvf2+NQ56CnQodh7Scr8adJwRt1rfyUZ8a3YfWy3iM7hsf3jfybJb2SQDNcbYbmDVWvUEzPR7HuVvWuh6EOj7bN3SC7GLuMMkmyMLfmbOXLfHShWc6Ow+rVZyy2R+1WztwPATsIww1FcIrJlsiuGgrmO8qqNQYYXEZLwW0ZT+eWp0AXMBe+8MOlHxNUrmuW2czEYMs6pbPdOwrqFe04xAFKsbT7UOIix5U4JPUPx6QE7NauWbp68ans3kAT30Y+DY8TMF/Y64cB1dNrw87TWL6HmfmuHYWswxlHXQnc8xI4YGVqVSQQa06dq/fbyWg78NhyfJOAAZS84w2GV21+vpvtA+IcLfBKoRp2FO7IAwsHh0TXTc7VHAdhn7H6RddDE79oGUpw9Zh1jtC/v7or+3y7vCReIY3MWzBjPo+CrU6yTbOh+gzFxQN3KHK/JL5ToIk7hsgR+Y1D8QItTpv1zhodBZTLPdepp876uss5eJFXWyfTKn26/dJEyBNloWXISaLQkh/Y+muz3opc65fuYgiUdqycCPNpHvIoh8KZAfy+JL3hSQJGmPU8+5bqWoZYralGeMlgBhqQ0DOB3uQbapv7UtcNnpr8kfP0sGhSOcsuTXv+Rg3Zhkk7lwbhvuNhpsH5GY8NJqhS2GfcbMzbZ6HF/nmyFuKtNBYfvy44yaKuIxP3+cu0sc/paq+CAn8VE/zfKxBQw0CCJtaIpCCd/tCS1csmCH803tfsf5wvlEkD+l+3fYZz0ydNGDwwJStTbJToGFKxphzzi5BmeJCy0lJT79tLeF+GL1phpN+S1Y2hNaOPL4ipIUzFX40wC6GR5arp8Peu7UXytR9WE1PandoKL5LQ2MWHm5twOPmRQxf4eL605VOA1AbOC24o1X20gnpqhtW/iHGqy40qay2tvY6RbmOcVY+hHqJJTbAiya/ibsmsPSzyyAjI2k+8nncN9CiT4Yv6tZg/JJLeG9vxelT3HCzYvWDYPMCXxA8RDbz1TduW23JU/SUMDVxZ2ffnaJ4UH+ZH+dCdabeNluW48rfjIotUI6yB7YaZ1Dg+L7Y66u4Y/8h8VNLhCEkAx98xnIgrmPQQrJ1EbIRoZrrVHAx3s++YaTrKl5g2wG0GMG9wnB9EHbeLqTb9rNqXHLlxUGGOc386l1tGRIfVHItcrIV2hpt0BejBgTLcTpg4FrJwx1WADDsxHSmwMwf3/zS8OQOeDjqyj7wE7PQrqZjKAOdzGJUK77TQ3oRv3OcapVcmwBBicaMYdsVA67Zw8yAUh0HRuNuQDeCYUwFx/DQViG47Z+8M4UEkzI0oWaNnS8mgyWKTa3yIrRRWfsDxbigChRobTJHtLqVLuY2XvQjl0bKqHV1CQ1b+V9L0CTbz7L8/xoOnTI9/4Oj5FJEZ/wrK5j/xeDUbkwB2smIDZ2zfNvmTsay6Sohj7aq21R46gxWRZYoy5q99Nr9//usaBpKp1nFmH/x9wcas2HycgaiCqhgX3x26zP/f3+C0PrkETHjfvTUszc5HXb2Zf/88XMIg7jClrdJ6gF6bZWm7H3QxpdCYIiDX04YbKlfcJoKWatqPjKzJLQpk54TMa50Qw6zVICJvMFu16/8rGJqyBO+Xxr5etZo+mdRtH5BOPk/6Zc3BYgVk0KnCJaaVmTTikRp8t2WuOmGGSJJDanIvIvahih6Ql5EiTxhdznotu5+A1vAiezWw9c3pTjHdgBPAkj3N57xm89+g11cJ9mq2FTEC+rUEBzKBd7DyWylwpzpmAMYirtuBnfgyhHDEJxkgc3cdQlZ4upi6tNbs64ovvoUAbYDutHQp1pN2fnkCxEe6BIkdbFQEt5zkL//jaOMEa9aqoxRb2VRXiGyW81irFcQeIWzos6xwuRn6+Tzkk4S20Og98IJ0GsXh0o5VJl2x78KgMYeAg4xXZICarvLihKDAfWmSs5x+Ln94lPV+FNgrEpz0h84LlCbhGhF5kVa992mWKCftDKctLsykqfIVXlQZd+Giq3318HOF2uaeHasVhZfFT7sQYu/Asw+b0sskhumKCMPNDDtWlQnM+RGQTXjadokP31C17drBPHINSXxHx5gsLCSYwWqL9bVnpwHTWIhmVAhqPf8qrUCPLC51/poHjLaCwRvnw9+j5AViATyRWyngOzsmRkuy5NFM1jx5RdFeFBxLfwxkh7B09skoHUtqJYp/eZ71xldgr9zNVc/2gAuSrdVCmBounlw8xfSAVITt6tPodI2Ce0bcY8VNVL2MyLqluzwoNvdzj4pqTuicgoaPj+CsL9A3YC46tOVPz+QMqgdjGq7yZ+JoPPJt5qCJgbcr6R8dRWS5jyQ+jkr6sPOl5ax6OMSkOWGzmXt4rvkj+GBR/rB0ul1SY6raz7cOcIpymQAGnUoPrTQjUTewNcwVgC0psHb4FlEKA4vI8oYeaoFDsgZ2MtnLp9MUAmdBZc8f20ivFNKMQrmiOYVoSk+7/wBPWzKXx26FjYCv0JHiBZ+dMALRah9j+Vrv6ryUfJg6qLuky7hjuStqlN4ZJPAUQggfpuWEVliPbVjIk5XsUSHwOCfCneZD9R9HbO2RO+GEBQ6Wnhjr30GEqXPHBRrGDNisKZTwrgb7RG5soYl2jpTpdNlSptsZhVVE3NdtBuUMiqshKsFY2iQdRu/8/BIE8n0IbPsRMO9zOMG0Hv2QBNH6kuKb1VGM5pXQG/IUXzI1Jrw9iChe2pXk4pgaDWrqbzMzkbOjxD5GSx4i1PSp7FgRizOosg4g1lrnvFeSpD263nMHDCSqrzQ6o0udj9v5eb/0iumm80smdfunKDlPGEgedGAzTNBR6dEIFtLlui954oq+ivpDP3sM6DECK0xdG4MRKVSfGAhbfEBriT/vpcOKPGuauYIgDJEuJket4ORCXvYxCN0HYdeM9tXINXDqkxAwnfeE7c0H3Q7Qx9nn4k4tEJpJCw9b3wKbAuOETu5yx6+gdYvHmr0LsZQtXPVX04qH1eDt0wZ5dZ09L8dlAMjgmBl69yX3NOHJatS+OvkNlbA7Xbd1lqSSyd1PbdYiDi4hRTb+x7X3wYs+UjT8Fto5zbbXqCnSqWkdhP+oS7idJSMa7/96WcaJ9ifl6lHygdHRuSD+VBt/NZKOH0oFBg7G0EIhRgUIGKiNbAIOPDv47+tYIeqhUBsFevQmT9+ImamLSmfXQftlkypSPhMjv/HZlW3oBcvQtBvrky80YfVQMYx5mX8PVyiwS1QDEpf0xJJ8r9fZOvUfIcuggg5JYj8AWoccAoY5GzXBeEgH1tejt5C9y638kNlXN7m7Am81nD8fstJwVSuO/Um8SCsaDE/naJ/6xhD23UMYNv5HQjU5ip7FSPHKbvritpPsbO0k72y6rn2Aq7U2o+Guy5oi4Wvl5buypli1fj/8LzuD56i1Z4LlYQKHoZ4bOMALU0CR4d745xzJsuTvgcQYfhCSLUFLbsRqlk3NW4LkOWmv9Idi64hu45+HouO2Csg304R0Ih1AcU0bA4pVTpDJToQUx+dLmpDBSu1IHN5zw1x0vxqGTGaH32Duu4aIPA2jT/XnVAZYB/JXRu9Cay6AdvxXciUqFzBvJna765udt2zd1Syggtj4kGKrv1HUiIHzHYlgX7epGylkKCdYwn3bCZE3d2QpxA22c87VFUrqJyNeTouRTes21ktAiRQ1iaEMffGo2F4WikYFP5+a4/8HT5KKug5QadWmkiwRH+AuhkK4rxTQDMHfEBOxgM88zZ+saXtTTwikRAzFBCoUfMULHICF7KVereQmPk2/sO909fngSRUI1vo3ZU2UdhFP9bGh5QrgX2/loGPoXM6iSeXlsIHYeG0rmNjttS7CYr0mFN///TElH3YsuIvP8gFmwL3uek1ze0ab57VATKjxu8Z1gmq86TKsAiVZfoh9vpjfQaFWOdaztAExwo6dvAEutpOsOtdqxdKveBXE+7NhOYeakXfvjYzQ5NDJfK1QUUWsYblUEUOTj3LHgBHLdnIPAjLmnaKtRK/KyIVxXTXnEXDbjxv2iNt4fWQBHt6vi4XkIr7fn+LdpGKG2QM50nPa49f4vihlyVsfgb/mBVj1Tfu9rarEn0R2KcaYay2Uz8V7ifdEdce7+mi7kd1UNS3KAIGPCKicIYZLFPFEhHSHWcUrriEWeonhG7TWiBhOdME4/tuh4sqKuas8W5V/LYZxZQ4Ju27NMLDIijy+p0u0Psj2WqKarqifFas1CmYNB9CDsuCLIaGe/Q80QXWwC3dSXGdBcsWdtMD33XqvVG0HKpWX8LRhTrMdAHi6Zb5UyFutW87hbvncw0jk/RR/Zs9YbMGeu2BWLDuFM8CZDXOZMyn+gbADjKrUs7nyz+gfwo/1VOBkRfIYMALcgmKiF+aELnAb+wEwQIaMlyTcCjz8GzpyfLBVRmwEpqQIWrr/bK4RRKdlbPshWkwwG89sOX46r9KjPwcWnXp4K1lcW1XBZX3auXJ3g0xPquvmMExY70Wln4ODFLLkmTVjNqZrgl8sfhZxn3wlL6DHBHzfsvzQb82kPZmVLYK7cMDSlYj9tODyXf5rBmv2RBGD3Rj7tju0AdXzFXl2aEP7wM+S+pHeCNZat7xuKqpmmU4cJ6lh3dGPxU9LAjiXh5iR0hQ2dhrhV+Uwy/DrZvtvHWJV/G9xhPLFXTg3VM0WTxxImbdhMtiSxo6fGGIYZQUvKhqTsnYGhvCL48hn5G5zVilfqckGka7F3KagZ66ApydszcSbgsVYv+yEHTXH8DqcH+kKW1RPORygv3CTQSWPwrmqiZeeJGO/3CV88Bdv+Npvr/2ttMRdEgpdzivCQpjmMX5KkEDT2ntZFC5/Po90ZraOLU96aS9MuQCTW5EAGiENLJzGoEq0agKg==
        - #1:
          - type: tool-result
          - toolCallId: KjnFGroq4uNrCZuY
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: gpTVDUEw5jVbMnmW
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: JwEcAuyW53rQiDwv
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: 4o6t4OMN7xmM1ESK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: tl3NBlLkgRO4kDXj
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: nVHZQphyXkiD3SvY
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: n7rRvIOqB4nw23Rs
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.