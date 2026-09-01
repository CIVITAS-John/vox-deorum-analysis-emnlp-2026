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
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Private: 50
        - Public: 50
        - Rationale: Carthage is our closest ally and holds a Defensive Pact with us. Correcting our relationship modifiers to positive to maintain this vital alliance and prevent backstabbing.
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Portugal is a critical friend and World Congress ally. We must maintain positive relationship modifiers to secure their support and trade.
        - Public: 50
        - Private: 50
        - TargetID: 2
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Resetting our modifiers with The Shoshone to 0. Since we have recently made peace, we should let the AI dynamically evaluate them rather than forcing an artificial friendly bias toward a former enemy who spied on us.
        - Public: 0
        - Private: 0
        - TargetID: 5
    - #3:
      - toolName: set-persona
      - args:
        - Loyalty: 8
        - Rationale: Increasing Loyalty and FriendlyBias to ensure Austria maintains stable, long-term alliances with Carthage and Portugal, which are essential for our defensive security and World Congress votes.
        - FriendlyBias: 6
        - Friendliness: 8
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Gold: 80
          - Espionage: 80
          - Production: 80
          - Culture: 50
          - Offense: 60
          - Growth: 70
          - GreatPeople: 70
          - Science: 80
          - Diplomacy: 90
          - Defense: 70
          - Happiness: 60
      - rationale: Shifting to United Nations Grand Strategy to leverage Austria's unique ability to marry City-States and gain World Congress votes, directly countering India's diplomatic and cultural lead. Prioritizing Science and Gold to catch up technologically and fund our alliances, while keeping a strong defensive military presence.
    - #5:
      - toolName: set-research
      - args:
        - Technology: Replaceable Parts
        - Rationale: We need to research Replaceable Parts next to unlock Riflemen and modernize our army, heading towards Flight and Ballistics to protect against advanced military threats like India.
    - #6:
      - toolName: set-policy
      - args:
        - Rationale: Free Thought is essential for boosting our Great Scientist generation and tech progress, helping us close the massive scientific gap with India.
        - Policy: Free Thought (Continuing Rationalism Branch)
  - tokens:
    - inputTokens: 23038
    - reasoningTokens: 8899
    - outputTokens: 439
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Austrian Strategy**
            
            My focus is now on dissecting Maria Theresa's current situation. I'm evaluating her modern-era position at turn 335 with a score of 1591 to strategize the next moves for Austria in Vox Populi.
            
            **Evaluating Austrian Position**
            
            My analysis now centers on Austria's current standing. At turn 335, with a score of 1591 and strong cultural influence, I'm assessing their competitive edge against India and Denmark, aiming to optimize future strategies within the Vox Populi environment.
            
            **Assessing Impending Victory**
            
            I'm alarmed; India is nearing a cultural victory, potentially influencing all remaining civs. Their military outclasses ours significantly. I'm investigating immediate actions, including potential war declarations and leveraging existing conflicts, though the Shoshone's recent peace event complicates this.
            
            **Formulating Counter-Moves**
            
            I'm currently assessing potential avenues to thwart India's impending cultural victory. The shifting alliances and recent peace treaties, particularly involving the Shoshone, present complex tactical challenges. I am meticulously reviewing available diplomatic and military options.
            
            **Closing Borders Immediately**
            
            My immediate concern is India's proximity and open borders agreement. I need to sever this connection swiftly to mitigate their tourism influence before it's too late, as it directly impacts our defensive posture and their victory condition.
            
            **Analyzing Victory Conditions**
            
            My current thoughts are a scramble between managing the open borders with India, which I cannot immediately end, and reassessing their actual victory timeline. While they have influenced everyone, the completion of the Citizen Earth Protocol and securing Tier 3 tenets are still potential roadblocks, offering a slim window for intervention.
            
            **Revising Victory Timelines**
            
            I'm recalculating India's victory path. They haven't unlocked the Citizen Earth Protocol due to their current era, meaning I have time to bolster my military or pursue an alternative victory. I must also avoid nuclear warfare due to its ethical implications, prioritizing conventional strategies.
            
            **Adjusting Policy Branch**
            
            I'm re-evaluating our policy choices. The current strategy indicates "Free Thought" from the Rationalism branch, but considering India's cultural threat and my need to boost science, I'm exploring options to shift our focus accordingly.
            
            **Revising Technology Path**
            
            I'm reconsidering our current research trajectory. Given India's overwhelming scientific advantage, I need to prioritize technologies that will grant immediate military parity. Plastics, while beneficial, might not be the most impactful choice at this juncture.
            
            **Shifting Research Priorities**
            
            I'm re-evaluating our technological pursuits. My initial focus on Plastics seems inefficient given India's scientific dominance. I need to urgently pivot towards military advancements like Replaceable Parts to achieve parity and counter their impending victory.
            
            **Prioritizing Research Paths**
            
            I'm prioritizing technologies that offer immediate military parity, specifically "Replaceable Parts" to unlock Riflemen and advance towards critical air and artillery units. I must confirm our ongoing war status with Egypt and re-evaluate research choices considering the tactical landscape.
            
            **Revising Policy Choices**
            
            I'm now scrutinizing policy decisions. While "Free Thought" strongly boosts science, I'm weighing its benefits against "Rights of Man," which offers production and gold advantages. This choice is critical for balancing my scientific catch-up and overall empire strength against India's cultural surge.
            
            **Reconsidering Grand Strategy**
            
            I'm re-evaluating our core strategy. The diplomatic potential of Austria's unique ability, particularly with City-States, has become apparent. This could offer a powerful alternative to my current conquest focus, especially considering India's looming cultural victory. I must weigh this against our existing military build-up and policy choices.
            
            **Leveraging Diplomatic Power**
            
            I'm now pivoting to a diplomatic victory path, recognizing the immense power of Austria's unique ability to arrange marriages with City-States for resting influence. This strategy seems far more promising than a direct military confrontation with India, especially given their dual victory threats.
            
            **Focusing on Diplomatic Flavor**
            
            I'm prioritizing a significant increase in diplomatic flavor, recognizing Austria's unique alliance potential with City-States. My goal is to leverage this through strategic marriages and alliances to rival India in the World Congress, shifting from a direct military confrontation.
            
            **Securing Diplomatic Alliances**
            
            I'm excited about this new diplomatic path. We are already friends with nearly every City-State, and by significantly increasing our diplomacy flavor, we can secure alliances. This will then allow us to arrange marriages, granting us crucial resting influence and World Congress votes to counter India.
            
            **Shifting Victory Condition**
            
            I'm now shifting focus to a diplomatic victory. The potential of leveraging Austria's unique ability with City-States offers a more viable path than direct confrontation with India's military and cultural dominance. I'm prioritizing diplomatic flavor and alliances.
            
            **Prioritizing Diplomatic Flavors**
            
            I'm re-aligning our flavor priorities. Science at 80, Gold at 70, Diplomacy at 80, and Production at 80 will be key. I'll maintain strong military flavors (Offense/Defense at 70, Mobilization at 70) while boosting Great People and Happiness, as expansion is no longer a priority.
            
            **Refining Flavor Settings**
            
            I am adjusting our flavor settings to align with the diplomatic victory path. Science and Diplomacy are increasing to 80, Gold to 70, and Production remains high at 80. Military flavors are decreasing slightly, and Culture is boosting significantly to counter tourism.
            
            **Analyzing Relationships**
            
            I'm re-examining our current relationships. India's tourism influence on us is high at 160%, necessitating increased cultural output. I'm also noting our hostile stance with Egypt and Denmark, and a surprising lack of strong connection with Carthage.
            
            **Correcting Diplomatic Modifiers**
            
            I'm correcting crucial diplomatic modifiers. Our strategy incorrectly set negative values for Carthage and Portugal, jeopardizing key alliances. I'm rectifying these to reflect our actual friendly relationships and defensive pacts, ensuring AI cooperation.
            
            **Fixing Diplomatic Discrepancies**
            
            I'm astonished by the diplomatic errors. We had positive modifiers for warring Shoshone while inexplicably applying negative ones to our allies, Carthage and Portugal. I'm urgently correcting these to reflect reality, ensuring we foster crucial relationships and avoid further AI misinterpretations.
            
            **Adjusting Diplomatic Relations**
            
            I'm now fine-tuning our diplomatic standing. I'm ensuring positive relations with allies like Carthage and Portugal while maintaining hostility towards rivals such as India. I'm also setting a neutral stance with the Shoshone, allowing their AI behavior to dictate our interactions moving forward.
            
            **Setting Diplomatic Relationships**
            
            I am now focusing on precise diplomatic adjustments. I'm setting relationships with Carthage to positive values due to our defensive pact and friendship. For the Shoshone, I'm resetting their relationship to neutral to allow for natural AI evaluation, ensuring an accurate assessment of coalition potential.
            
            **Finalizing Diplomatic Strategy**
            
            I'm finalizing our diplomatic approach by solidifying relationships with allies like Portugal through positive modifiers and resetting the Shoshone to a neutral standing. My research is locked on "Replaceable Parts" to quickly bolster our military.
            
            **Confirming Policy Choice**
            
            I'm confirming our next policy choice. "Free Thought" is crucial for scientific catch-up with India, so I'm locking it in to ensure its benefits are secured.
            
            **Setting Grand Strategy**
            
            My focus is now on setting the grand strategy to United Nations. Austria's unique ability to arrange marriages with City-States provides the best path to increase our delegate count and compete in the World Congress against India.
            
            **Adjusting Flavor Allocations**
            
            I'm finalizing our flavor settings for the United Nations victory path. Diplomacy is now at 90, with Science, Gold, and Production at 80. I'm boosting Culture to 50 for defense and setting Great People at 70, while slightly reducing offensive military flavors.
            
            **Finalizing Diplomatic Stance**
            
            I'm finalizing our diplomatic persona. While the core is aggressively competitive, I'm emphasizing City-State influence and slightly toning down outright hostility to better reflect our United Nations victory strategy.
            
            **Adjusting Persona Values**
            
            I'm now fine-tuning our AI persona parameters. To secure our critical alliances with Carthage and Portugal and prevent unintended betrayals, I'm significantly increasing Loyalty to 8. I'm also boosting FriendlyBias to 6 to foster stronger cooperative relationships.
            
            **Revising AI Persona**
            
            I'm significantly increasing Loyalty and FriendlyBias within our AI persona to reinforce crucial alliances with Carthage and Portugal, which are vital for World Congress delegate acquisition and overall strategic security.
            
            **Executing Diplomatic Updates**
            
            I am now executing the planned diplomatic updates. This involves applying specific relationship modifiers to Carthage, Portugal, and the Shoshone, alongside confirming our ongoing research and policy selections. This should solidify our alliances and strategic positioning.
            
            **Implementing Diplomatic Adjustments**
            
            I'm implementing precise diplomatic updates now. This includes setting positive relationship modifiers for Carthage and Portugal, resetting the Shoshone to a neutral stance, and adjusting our AI persona to reinforce these crucial alliances. The grand strategy is now set to United Nations, with finalized flavor allocations and research locked on "Replaceable Parts".
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: OkWHUUchvIbakXc7
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Private: 50
            - Public: 50
            - Rationale: Carthage is our closest ally and holds a Defensive Pact with us. Correcting our relationship modifiers to positive to maintain this vital alliance and prevent backstabbing.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: jvcLG8tZeIVCFiE1
          - toolName: set-relationship
          - input:
            - Rationale: Portugal is a critical friend and World Congress ally. We must maintain positive relationship modifiers to secure their support and trade.
            - Public: 50
            - Private: 50
            - TargetID: 2
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Z6PJ4NXjeRmNpcRf
          - toolName: set-relationship
          - input:
            - Rationale: Resetting our modifiers with The Shoshone to 0. Since we have recently made peace, we should let the AI dynamically evaluate them rather than forcing an artificial friendly bias toward a former enemy who spied on us.
            - Public: 0
            - Private: 0
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: mPH1i93hS7Y4NEfZ
          - toolName: set-persona
          - input:
            - Loyalty: 8
            - Rationale: Increasing Loyalty and FriendlyBias to ensure Austria maintains stable, long-term alliances with Carthage and Portugal, which are essential for our defensive security and World Congress votes.
            - FriendlyBias: 6
            - Friendliness: 8
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: DcdyRwqvVk2o7N8K
          - toolName: set-flavors
          - input:
            - Rationale: Shifting to United Nations Grand Strategy to leverage Austria's unique ability to marry City-States and gain World Congress votes, directly countering India's diplomatic and cultural lead. Prioritizing Science and Gold to catch up technologically and fund our alliances, while keeping a strong defensive military presence.
            - GrandStrategy: UnitedNations
            - Flavors:
              - Gold: 80
              - Espionage: 80
              - Production: 80
              - Culture: 50
              - Offense: 60
              - Growth: 70
              - GreatPeople: 70
              - Science: 80
              - Diplomacy: 90
              - Defense: 70
              - Happiness: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: iBFh3M2kuYGvYbNV
          - toolName: set-research
          - input:
            - Technology: Replaceable Parts
            - Rationale: We need to research Replaceable Parts next to unlock Riflemen and modernize our army, heading towards Flight and Ballistics to protect against advanced military threats like India.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: knW8K5mKI4rWwsWH
          - toolName: set-policy
          - input:
            - Rationale: Free Thought is essential for boosting our Great Scientist generation and tech progress, helping us close the massive scientific gap with India.
            - Policy: Free Thought (Continuing Rationalism Branch)
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: OkWHUUchvIbakXc7
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
          - toolCallId: jvcLG8tZeIVCFiE1
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Z6PJ4NXjeRmNpcRf
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: mPH1i93hS7Y4NEfZ
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: DcdyRwqvVk2o7N8K
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: iBFh3M2kuYGvYbNV
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: knW8K5mKI4rWwsWH
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.