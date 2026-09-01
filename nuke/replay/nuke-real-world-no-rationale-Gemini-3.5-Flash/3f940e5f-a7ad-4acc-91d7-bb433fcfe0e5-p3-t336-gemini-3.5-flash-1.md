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
        - Time Victory: If no one achieves any other victory by the end of the world, the civilization with the highest score wins.
      - Opponents: summary reports about visible opponents in the world.
        - You will receive staff members' diplomatic evaluations.
        - You will receive each opponent's publicly available relationships.
        - You will receive the best available location for your next settlement.
      
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
      - toolName: set-relationship
      - args:
        - Rationale: Improve relations with Egypt to facilitate peace, allowing us to unite against the common threat of India and focus our military elsewhere.
        - Private: 50
        - Public: 50
        - TargetID: 0
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Strengthen our alliance and defensive pact with Carthage, our top friend, ensuring mutual security and shared diplomatic goals.
        - Private: 50
        - Public: 50
        - TargetID: 4
    - #2:
      - toolName: set-relationship
      - args:
        - Private: 50
        - Rationale: Cultivate our strong friendship and diplomatic cooperation with Portugal, securing their support in the World Congress and trade benefits.
        - TargetID: 2
        - Public: 50
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Remove the artificial negative modifier with Denmark to stabilize relations and prevent an accidental conflict on our western border.
        - Private: 0
        - Public: 0
        - TargetID: 1
    - #4:
      - toolName: set-research
      - args:
        - Technology: Replaceable Parts
        - Rationale: Prioritize Replaceable Parts to unlock the unique Grenzer unit (replacing Fusilier) and modern infantry upgrades for our military.
    - #5:
      - toolName: set-policy
      - args:
        - Rationale: Continue the Rationalism branch with Free Thought to accelerate our scientific advancement and catch up with global tech leaders.
        - Policy: Free Thought
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Defense: 80
          - Espionage: 80
          - Offense: 90
          - Happiness: 60
          - MilitaryTraining: 80
          - Production: 90
          - Mobilization: 100
          - Science: 60
          - Culture: 40
      - rationale: Maintain a high-mobilization Conquest strategy to counter India's dominance, while boosting science to catch up and culture to strengthen our defense against their tourism.
  - tokens:
    - inputTokens: 23031
    - reasoningTokens: 8162
    - outputTokens: 339
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current State**
            
            My current focus is on assessing our standing following Turn 335. I'm evaluating existing strategies and active policies, particularly regarding competitiveness in both victory and wonder acquisition.
            
            **Evaluating Research Trajectory**
            
            My attention is now on our technological path, specifically questioning the current selection of Replaceable Parts. I'm reviewing available alternatives like Combustion, Radio, and Penicillin, considering their strategic implications. This assessment is prompted by noticing our ongoing research of Plastics, which appears incongruous with the stated "Next" technology.
            
            **Prioritizing Victory Condition**
            
            I've realized India is on the brink of a cultural victory, influencing five civilizations and one turn away from influencing Denmark. This shift necessitates an immediate re-evaluation of our research and policy priorities to counter this imminent threat.
            
            **Disrupting India's Push**
            
            I'm re-examining our conflict status and diplomatic ties to see if I can impede India's cultural victory. The immediate severance of trade routes and open borders upon declaring war on them seems like a viable, albeit aggressive, tactic to reduce their tourism.
            
            **Disrupting Cultural Ascendancy**
            
            I'm actively investigating avenues to derail India's impending cultural victory. The critical factor is Denmark's proximity to being influenced; if that happens, India wins. I am considering instigating a war, either by engaging India directly or by attempting to provoke Denmark into conflict with them, as warfare could disrupt their tourism flow.
            
            **Revising Strategic Focus**
            
            I'm currently reassessing our overarching strategy given India's imminent cultural victory. I'm weighing the merits of our existing "Conquest" Grand Strategy against the immediate need to disrupt their tourism, potentially through aggressive diplomatic or military actions targeting Denmark. I am also scrutinizing available technology and policy options.
            
            **Assessing Diplomatic Rupture**
            
            I'm evaluating the severity of our diplomatic standings, particularly the denouncements from Denmark and India. This stark reality compels me to consider drastic measures, potentially including initiating conflict to disrupt India's imminent cultural victory, which hinges on influencing Denmark.
            
            **Disrupting India's Win**
            
            I'm analyzing how to prevent India's cultural victory, as they are very close to influencing Denmark. I'm considering aggressive actions like war against India to cut their tourism, or perhaps provoking Denmark into conflict with India. My focus is on any available strategy to disrupt their cultural ascendancy, including a potential shift to a "Conquest" strategy to capture their cities.
            
            **Leveraging Alliances**
            
            I'm reassessing our current conflict landscape. It appears both Egypt and the Shoshone are already at war with India. My immediate priority is to explore if this existing conflict can be leveraged to disrupt India's impending cultural victory, specifically before they influence Denmark.
            
            **Re-evaluating Diplomacy**
            
            I'm now analyzing our diplomatic stance with neighboring civilizations. Specifically, I'm exploring opportunities to improve relations with Egypt, who is currently at war with India, to foster peace and realign our shared ideology. I am also considering Denmark, assessing their current alliances and potential for future cooperation despite our differing ideologies.
            
            **Confirming Research Path**
            
            I'm confirming that "Replaceable Parts" remains our chosen research. Its unlocked units and future technological paths, such as Flight and Ballistics, align with strategic goals. I'm ensuring this selection is solidified within our ongoing plans.
            
            **Considering Ideological Shifts**
            
            I am now evaluating the "Rationalism" free thought, recognizing its significant synergy with science. My attention is also drawn to our exceptionally high mobilization and production flavors, alongside our comparatively low culture and expansion, prompting a reconsideration of strategic priorities.
            
            **Disrupting Cultural Victory**
            
            My immediate concern is India's imminent cultural victory, specifically their nearing influence over Denmark. I'm exploring aggressive tactics, like instigating war with India or provoking Denmark to conflict with them, to disrupt their tourism flow. This is critical as Denmark's capitulation means game over.
            
            **Disrupting India's Win**
            
            I'm actively seeking ways to sever India's imminent cultural victory. Denmark's imminent influence is the critical factor. I'm exploring options, including a direct war declaration or provoking Denmark into conflict with India, to disrupt their tourism. I'm also reassessing our existing alliances with Egypt and the Shoshone to see how their war with India can be leveraged.
            
            **Reviewing Available Tools**
            
            I'm reviewing our diplomatic and strategic tools. The Shoshone relationship is stable, but I'm assessing options like improving relations with Egypt and softening ties with Denmark. Our current aggressive leader persona seems well-suited for a conquest strategy, with high competitiveness and low forgiveness.
            
            **Leveraging Diplomatic Mechanics**
            
            I'm now delving into Austria's unique diplomatic mechanics, specifically its ability to arrange marriages with city-states. I've identified a diplomatic marriage with Valletta, which is promising, and I'm exploring the potential benefits of focusing further on diplomacy for more city-state alliances. My priority remains disrupting India's cultural victory, so I'm investigating how war might affect their tourism output and trade routes.
            
            **Disrupting Tourism Flow**
            
            I'm analyzing the impact of war on India's trade routes to reduce their tourism. Realizing we have significant trade with them, severing these routes is a key tactic. Curiously, Denmark lacks trade with India, so their high tourism against Denmark needs further investigation beyond direct trade links.
            
            **Disrupting Tourism Calculations**
            
            I'm re-evaluating India's cultural victory path, specifically the tourism calculation towards Denmark. I've confirmed that my previous assumption about war directly impacting tourism was incomplete; only war with the target civilization reduces it. I'm now exploring how existing wars with Egypt and Shoshone affect their overall tourism output and considering if a slight delay in the victory condition is possible.
            
            **Optimizing Strategy Flavors**
            
            My current focus is on ensuring our strategic flavors strongly align with a military-focused approach. I've confirmed that our existing flavors are exceptionally optimized for war, which is ideal given our "Conquest" Grand Strategy. I will reinforce these to maintain our current advantageous position.
            
            **Refining Diplomatic Engagements**
            
            I'm prioritizing improved diplomatic ties with Egypt and Denmark. My aim is to foster peace with Egypt to align against India and to explore cooperative avenues with Denmark. I'm keeping our current research on "Replaceable Parts" to unlock the Grenzer unit and strengthen our military.
            
            **Revising Research Choices**
            
            I'm reassessing our research direction. "Replaceable Parts" seems less critical now, as we already possess "Grenzers." I'm prioritizing "Combustion" for its military advantages and "Radio" to boost our culture and counter India's tourism.
            
            **Confirming Research Path**
            
            My focus is on confirming "Replaceable Parts" as our research choice. Its connection to critical military advancements like Flight and Ballistics aligns with our strategic aims, and I'm ensuring this selection is locked in.
            
            **Revising Research Choices**
            
            I'm reconsidering our research trajectory. "Replaceable Parts" may be less crucial now, given our "Grenzer" units. I'm prioritizing "Combustion" for military gains and "Radio" to enhance culture and counter India's tourism.
            
            **Optimizing Strategy Flavors**
            
            I'm ensuring our strategic flavors strongly favor a military approach. Our current flavors are highly optimized for war, fitting perfectly with our "Conquest" Grand Strategy, and I'm reinforcing this.
            
            **Disrupting Tourism Flow**
            
            I'm analyzing how war impacts India's tourism via trade routes, recognizing our substantial trade with them. Severing these routes is a key tactic. Denmark's lack of trade with India requires further investigation into their tourism beyond direct links.
            
            **Assessing Diplomatic Rupture**
            
            I'm evaluating our diplomatic standings, especially the denouncements from Denmark and India. This necessitates drastic measures, including conflict, to disrupt India's imminent cultural victory, which hinges on influencing Denmark.
            
            **Leveraging Diplomatic Mechanics**
            
            I'm exploring Austria's unique city-state marriage mechanics, specifically with Valletta. While diplomacy is appealing, my priority remains disrupting India's cultural victory. I'm investigating war's effect on their tourism and trade routes.
            
            **Reviewing Available Tools**
            
            I'm reviewing our diplomatic and strategic tools. The Shoshone relationship is stable, but I'm assessing improving relations with Egypt and softening ties with Denmark. Our aggressive persona suits a conquest strategy.
            
            **Disrupting India's Win**
            
            I'm analyzing how to prevent India's cultural victory, as they're close to influencing Denmark. I'm considering war against India to cut their tourism, or provoking Denmark into conflict with them to disrupt their cultural ascendancy.
            
            **Leveraging Alliances**
            
            I'm reassessing our conflict landscape. Egypt and the Shoshone are already at war with India. My priority is exploring if this existing conflict can be leveraged to disrupt India's impending cultural victory before they influence Denmark.
            
            **Disrupting India's Push**
            
            I'm re-examining our conflict status and diplomatic ties to impede India's cultural victory. Severing trade routes and open borders upon declaring war seems like a viable, albeit aggressive, tactic to reduce their tourism.
            
            **Disrupting Cultural Ascendancy**
            
            I'm actively investigating avenues to derail India's impending cultural victory. Denmark's imminent influence is critical. I'm considering instigating war, either with India or provoking Denmark into conflict, to disrupt their tourism flow.
            
            **Revising Strategic Focus**
            
            I'm reassessing our overall strategy due to India's imminent cultural victory. I'm weighing our "Conquest" Grand Strategy against disrupting their tourism, potentially through aggressive actions targeting Denmark, and scrutinizing available tech and policies.
            
            **Disrupting Cultural Victory**
            
            My immediate concern is India's imminent cultural victory and their nearing influence over Denmark. I'm exploring aggressive tactics, like war with India or provoking Denmark, to disrupt their tourism flow, as Denmark's capitulation means game over.
            
            **Disrupting Tourism Calculations**
            
            I'm re-evaluating India's tourism calculations towards Denmark. War only impacts tourism with the targeted civilization directly. I'm exploring how existing wars affect their overall tourism and if a slight victory delay is possible.
            
            **Re-evaluating Diplomacy**
            
            I'm analyzing our diplomatic stance, exploring opportunities to improve relations with Egypt to align against India and considering Denmark's alliances and cooperation potential despite ideological differences.
            
            **Considering Ideological Shifts**
            
            I'm evaluating the "Rationalism" free thought for its science synergy. My attention is also drawn to our high mobilization and production, alongside low culture and expansion, prompting a strategic reconsideration.
            
            **Adopting Policy**
            
            I've decided to adopt the "Free Thought" policy, recognizing its significant scientific benefits. This choice, combined with maintaining our "Conquest" Grand Strategy, allows me to further refine our strategy flavors. I'm increasing our focus on offense, defense, mobilization, military training, production, science, and espionage, while slightly boosting culture and happiness to better counter India's looming threat.
            
            **Adjusting Diplomatic Relations**
            
            I'm prioritizing reinforcing our critical alliance with Carthage. I've noticed significant negative modifiers impacting our relationship, which could undermine our defensive pact. I'm adjusting these to strongly positive values to ensure continued friendship and secure our critical alliance.
            
            **Strengthening Alliances**
            
            I'm focusing on optimizing our relationships with key allies. I've improved our standing with Carthage to bolster our defensive pact and am now adjusting our ties with Portugal to foster their continued support in the World Congress and trade. The Shoshone remain a strong ally.
            
            **Adjusting Diplomatic Settings**
            
            I'm fine-tuning our diplomatic stances. I've decided to remove the negative modifier with Denmark to ensure stability on our western border, while maintaining extreme hostility towards India, our primary competitor. I'm also executing a sequence of relationship adjustments for Egypt, Carthage, Portugal, and Denmark, ensuring our alliances remain robust and our competitive edge is preserved.
            
            **Refining Actionable Steps**
            
            I'm now translating my strategic considerations into concrete actions. This involves confirming research on "Replaceable Parts" and adopting the "Free Thought" policy. I'm also meticulously setting relationship parameters for Egypt, Carthage, Portugal, and Denmark to align with our broader objectives.
            
            **Implementing Strategic Adjustments**
            
            I am now implementing the decided course of action. This includes confirming research on "Replaceable Parts" and adopting the "Free Thought" policy. I am also setting specific diplomatic relationship parameters for Egypt, Carthage, Portugal, and Denmark to ensure our alliances are strong and competitive.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: duRmM7I2WDq6XuLV
          - toolName: set-relationship
          - input:
            - Rationale: Improve relations with Egypt to facilitate peace, allowing us to unite against the common threat of India and focus our military elsewhere.
            - Private: 50
            - Public: 50
            - TargetID: 0
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+7LQGG4OFugLKgxIjZXicEWxpVAXbAeOho2T3GYkhhYv92RxuTb4PyJbzIgi2QgSat6tSjCzD3SFhNEhdsmK61d8+fZrlSRFIs/iuPMimP+aLH+2GgPdHvIYCEUCfCXpjcRlZlRHhIsK22TvHzhENiwo5jh70WE/7QfPSmL2JBvmBYMMqJxOCaixFenh3+MwHZfvnCb7xro5az+SEKuKNiiFPlfbWV0nOS4XW1CFcW/+NRbZdmg8FVrKGiw14H4eAum0kPYNljGckMCfnnbS94oWT8BDijibDLxIPxq9GM7Y51y/uSzXcfIvUY4GsEfyna1cjR/F2FPU+XLkIW8FslsHF1J+t+rw/FafwnEH1JR+w3IXAMErSnSvsbW0L31NXH8wfngeVeBS/6vy+LDkym/k7hJOEWP9VEO4XTDHfKQKqjnDFmVL1ViCu4LeGlCq4KrhI1DfxvOH1d9KYiFvx+bpniHHuKfeMrZmylra9p5n8T54CK8Nz2VlVTMWbFIG/8S9aDwKhRqpNIh6lilImfD+bfkvIHLX+ZwbX77KTJXm4YaeYwQ1rRqkON33dVOlTWL7xNjL5//GeOoysRDvzyqmiecObqfrkvxIZSKCHdxpaEJK+a4p9YRw0Y1I0DhdqeY4mcehGMIr/+Z4mlcfjA70DoXPMZXc8RtzLV6pJt1nD9G6Qx7RM3PJlWBuOMwOZ2A5ybgiy3xtZvAeI/tp9mJAx1MVNwj2NGhVUMXrloOfATnWqrHwcyyPiPkj0NN7vPX0FPhvijpraKLpSkpLcM688Sql4xnSEriz1JbweXEhkfuoBAdQ3DEQWJWeZX9g7Ztu5wgeGZCSy9Xlp4iKieP1Xf/D2LUzWlbxdzCEfJwYrD81fk9fWNhisYIeIbyiBlYWbC22qfK8NGEKQlC+9C9LYJvtZQSJ4EJ60Ge8r7KKz+Q6U+dzWsAbSS77LZP27bZU5Me99P/6OvKy4I+ohOGNdLqGiC/YjuzLo509cxuEZJIF5Xo8nrsmyOSB9vEJyacl3zIRw2UtpcDaU4cxWqBXrWCgN9UoVriyfxnA9VVhM4zvDw51ZeXq9dMj/fSZhObgz4euF/neCti9YZAUgffzCUMnl9o7tdji0x5Wwp83a0KAunAvnPxbWPDcVdUPD3HPZZ6nic7X6746iumtzdIhfcuoJrab8mjD/XEW/CLOLIXKQ01djSnU4D1cjq5OWyYiyEopVZdIKeByvE0EcKzeZfTb2EslO3ZW4VDBh4EmStjAjPqxftkR5wyr96QuKWNetAsixnPmIKeORWcxq0gyiVnV6DBVDcn+UKWB9AdlxGvLUV1IfN3ZGQ6/zRhZaE8IXxQjqKiYObgEEqswplyswN0H2G6Z6OLZwJf2gBoEeNCAUTwlEwUnASMEnB5E+H78M9r75gI6i9qPkXNhu53scD4KuRTnaxmlKF7Jdc0AtxTqvF1VSzK/SGjTo2cEm5Iw4DgoPqoa9jqmM4zpEGLJOwEjBfiFHaOTwJyqHfxWjetAZJIYXFbcOuYXU+uVMsKRvVJ4Tg+CxaqYc3PMvfeq1qPC7fE41asC9/jLoIUw9mCDAX7g2jsFqXNPHEDz7FFZ1fS4zyxgB+Tx8Aczgg9W2jESOs7M6QET4VfCSKr60I0YxtmwSs+ojU2S6mkE/49gk8jx0K+0TKk+T7xjx5kU+QnRizylOELdNigWtm8alXHQUpDqKFVTaJpLINm7HpwlxXmOuiUQ+ZNq4Lj2ihl0KN8+8V1NSNRgHqVxwozmu1i8mX/xrbOdNQbEncI3jkdmI3G5SYD7iFTaXoheQHZ1V49le7u14VEQDyu/ZscV2FC2DJJ/AmN62DGcYlquQTRhVNyiCRSONZxLB9o15jeyKF+GSbkLsUmK7z02Lk+M3hmIhtuemztpaurJIkCN0t9YT9j0u1+SX59bMQuZ+x8FXUmASQX3S0ihF4PqgYnYB1HQ5wpXT/FydOqu4/XAX74CeSGfDAQIuBB/J/cVdmRb+vk7axQy/7zE/mhKjyTSC1THe63rEjDcdF6n3Lz7/AEG6pMkW32u5kwNxJpt5TFUUj3/2Z18XEb7FKqi5kNS5GZi9MN9UoFI/m8VhbpKr9gRZiQSrsZb6Y8cNWt9mGzzyKRedKYaiGyHikiDLLlAESpRcg3TRX4w9bP/91dVP33E14PPHkOgnR1oj5HbaZ/g+CSSRZhFNhvShdDfrfoezLzW3dA0pmW8OsihH34aRrbzbB+VRd/QUfzosGz8mQz+UFXEhq06DR9Yk8v8CxW9LjRkhZI3orYLdIuTsZXJCiUEjoFcQO7gydfFmAUF0q9UdR60v7oag3OG+V1y8ili8+X1NFVxnBNqCvlbkCXWH0yCfQZ3AsPhln+J6ZfwcmzQJpwJoPDXOHbgio84h5zTYC0aEaeFTW2AOZycFvaMH6yC9IjcjlKtv9UvatV3QCJ2r/CRzP5O090fFBSZRjg3POqdJzDq/VG2ZC7hYnW2ukTkSTqRrVBwK5bxfWXa726L4o/NC7bO/ypsnONgc4yEaUl2QJ6kcvjyxFRaJSTK6fm4/CSzttLO476ym2LGlUpAXQXKvIa1z/4wwEPkcjOb2KoS4YXqqVOxp73lxsWNuLKicObNcOzTyaGdCxyy1g1rgBV0Zlg8ffXRi8u8fiQDCJsFRcQBgNTDt1XKoZ4d+nyhAZ1x/yMjKAn6+SVchb1buaftL6+eM3sZjBF7SEFvsLQdaQ0UQxthpF9ithjSFzilwVpXJoX4wahMgO8U/QnLBm6uPyYct7uOE161NENZV99zDemAal4Pp6fNEi2/5wwR83PBAcXzNXmM4bv9Ttn4cmgN8DzO1VEaVEeMJd/y8PJlVJqXjom4J4yVuTIffdfG9ujOWrJIjnupwLtK3UYswRzW4iJhalnCanoqzNQuD/68i3T9S7FX1XPMSlN2SK8nHzge2Vkzdc0vyX6SxqSYDT7PUBRjzr4I80Vl9cJoYMGxp2nXpgjtUL6FMFYBDhjGcCHvDTsjebwP/2dnNn5W6RxWakKlDECmpNmAM58hqtRV7t05N4ZrML4JQ8DjlCKvcyCAMS0j8svq68m3exCNRQlhYfCqdCtP6TSTioky8BU9iey/LNKHZHTx5+0YbFewNTtAlT4nMy3XrDinbcWteBlZ0RzFcfHnMmxz1F1D/hd76LsCIEJa57urs0dWPXc83/puwarxp6vgMYWzjb58s8GYHYq0e5vA1kABSY3TJsNHrfBldKlLa+/ws6sK0h0f6DFceLWbRH2gkwnDxLbLLDR0PQ1DECjVKKKdPOj30ly5wBllOOtrIdCKUXtNOwyvWgdpSEsO8GK+hOnIz/SbTonkWW5mxp67/4bNVe5hKVg+OTgQi+cfH0B96+m6ADh5UrQ7gEqMTxdcVxvRcfw6LwP95vePRB8vvV8U7JgDBRANRUqUvzyL5UaM1Xhxi5Utf4goBnAEcHAr23ewQUTzO9SDsSg7YjpqQ3ZSK79o449oWfQzRUrzRndFKGUvzS3wPdk3+itxijnIt3HzJjZYVn+y65evCzaZRrAxaON3lCC3eGlorMmOku3jdBgodxrBz/PDq22YsfJqTDB2vCKFMKggEQx/bSWQGIH7vwy+SaYGI7jjohawPZ1pxjQ7ZKKh5I56PP4rzBYQB3zmbD/kFaMbIrrT6LWTBc7f0m3apWmm1YPg8CRJK2EFhWYon8Gv375BbWAQDaiSb88jYsA7dHDlM/ZI08J6v851K6LrLWLq245Iiy/xUIhejlgd+qk6okOyW9KWr5OcXlxA0D2Ia3bP+0jo6sOm7pOlG3akvxyAMgmuRsPRZ5Z09zSYuMV81PorU7fH/GpT5emS/0S1LJNV2m4bqWJsUkviuzuJYqB2D59VkYucMwkpehblj9fmLamKiQdPZfCdiGrMLj7ur992jmM7xdvHtjzelBW2qxBHwBCIy3mvSbqR1yGoRNDoqDx0Aw0RaEkAObxOwTza9UxfRRiPjiMSur7cCUQCJNrp6NwjBZSBJv80vC5ARg8HNCWIbuC8oycR+ubAFWQCk4FImoK0Se7hyEyTZtnWVX+j1Jcuw7tDSG7jdLav7aA0nz9yX2GFdvad2ZP5yyynGLN4u90hE2KeV7Sq1Lfxj/E1XM8YwJNfU1aXcVOD0XdRBooEgwAJI8XONRkDhFF4sriToKqMrA5sAjIT4VlC3Lj0s+AyfYL+NB9nCnjUEDF6iDCS9FbNDhYDFgrg231TBKOBqLTjntFJfMq/0O+6BVqf6HNEyYX/CpZZHcHE5MGQobOJS8G8JE2ULHohrKIpvPztpyFalAto2T+RbylQH5RHkrBefKuIGHnJ6GcdGhrmplTM0dsV+/+QX/T88CyrCjvj/Xv/q+Jy1AZFNz03w95d6Xo1nquDJmichqe+EuO6ciWBdybD67QO14xexSl+/lbzlIi5+UpHHC7VpoaYOcykOhJ7CNP0/1JVKi3k7ekHUvHVFUEmjcLTMPpkSQuRj5sU3yzLzQR41jcaoLLVTRsLFCmtp6t6yr41enT0Nn3Ty/79wlfRHdJ/yGy5rLpk868kERmJTdQAFiWERq/7FK6AoOdtcP9j2CXjDhIV7KYi1HV9GOqrfp38RWBwemDEWRwWKFpnOu1F+nsJKFccgPBKn0OAUrCXYPi+aDs0rx2XRMRi2j4KsMshtRf5Tlf6q191JpMVh+hYx/gvTG+dkGlEKDtSDlDpkNNBfSIlVJjNlJQiRt1iak47yYmmg6FXZlU2irUez+Ohr9CKAVnbRAdpXapm8fd1aH/csVU36QryOa2t5gSZPLdklWmKYPZcjAjpPOt4qnZ888EHXft32PP/4vL/R3v+nTYaYVquVdLBnev6bxLogc0qIsVs1rQ0KhOn0p1n8bMslplNy/6Qdw4HIJB1ojbswAEGIGwy5u9vgSCLcijxzWDbxGp89WF1HO0gCjMAhbwyKO4J1itQDixd/WT7pXbfP2t54Fu/WTPfdl7La2jFhbaUL3VQmelruWwdDzvfUvWAgeh0P6OV83bRYJGq2sKw19Ng4ygLvfemHTJwJnmGzVrCz/cz5feiQ0NKJE3fbq/Wnel6709+XuRSgEFFFv4BUyevPZtK/fz8o44IWrhs5IlXXICBixpxAzWxY1QHszCUOoMEr6OYrQl1k0TR3spvw6bI5y/ebaesGqdukVJ0+ig9PZW1dvzHw37ZyPKMUsoqMGOacLMAt1OkS+wmuxGDgOguITNTOzL4XnfEca+a3niaW7mT3FU8fYUDBHHGcC0L9jZ4ohJ5m6k5MSE8f6nZwgpRsKvJJYmD7V0kFOiWDBJ5Br4RDEuOdjsUCccBIChyW79yLJlutPLmUd33b5ORJGUeDo64uZl2CDFj6fW09e9Qg7rmWGrs61uJs+W94wMgQkyPCbBBHS9TsKlpnSnKRyfs5Ma4++F9e+PSTY91GTmbLHA/WXRzpiXWrxIZdUKIlxZzllxdtpQYRqugjsMkC+cXmhjng1FyS1Mk/GNoTV0ZCEdbdY4ELQWyjGziiR/yR/gnh4BY4lLWGL3flzmFVW25qXh6xBFFiTAJg00a7fX1t3uv5aijOTKRVw7Nxi4NIzCjttNyr2gx7Wx8nLFPwLYAEZbsuIIZ5udkV/GA9+kk3b2YfPlIiM/uhpKvVIvw4ISDTkj0XtW4uzZV1vWsv9av8d3XvCZ8woRgl+las7ivLlliveFm020pkpyqZxlNuqkSut9a8miKkEasDMwsgTdFlgvKhroeE8MMjy7ZHJ5talxAgYUU2JpoQg8cm7Eyb8FI1jGXcssA9OwrxVGv8Tx2bF/X52SHODpCdy53rmq12UShd96342xijMG9tcxW5BZs1zJKa+01R04LGinBHWqsnEQlAjXPXxYeaTV8oO7jiIVUV3RuK7SzvvtX4i+nNpdzzLFJVLcQrvTuNNtiGfetLGNYE76MT4At7ouQC4apibRwM8WtfIv2QFpWzmGOBAc7ifp0d2R1RLcX/Xsi7w3kkCxC27bv74C79caw5GTowxPvBdP2ziB/4X64BDMQJj1sHsmarDIiO4ybg/b6Vm0WM2wZMnubkgNA2HQ7Fd7B5Pkif8BFzkjIm8zaHcm7TsJQhW8881RvkhbK5gJCaRHzyJyyciG7XjzgaAiOiNQabGUl1qZtZxX6aSzjh4Oi9FaVrhHwWZycjNT/dX10E1IF1mhZGGHmw8EiXDGpEQYWKl66WQqEPbODzoqxg+cup7UPwvrcfElJH/P8QydhvwgZ+ilC81XIduammdvWRf2azINFCS40ggdnVthy0pZxI6aX7Yn/6r8R4pYXq0W5662G4l5c5QC6iM+A7XwV2B+4IkXxE/Bjem506C+rmhV+thnjsTCe/AZYdRJ0S3OpBqIBsddXJtt1oA1PjXuofWHlR0ZHAgPFS8W15ypibEbdLKGvGDGekmXMDTNHIZc+i+Qym57bPhjepa+w7c83DC8827gUZ6Al2fvCiG2atFfa6DB3fk9WO8ED96vopREXdOoUv2LD+qbkYo7zNq5xcVqedUcoOay8CS5AmDmSbtcZ1Cc3dq6UDMWgWTvTTbOhk2bVTdOEqzeDDkzZ8xn3zCQZeRkOUDulYnuT/3VpdbXmXpqqPQDFQZGnKbIriFN+tMd3csVejBtZ3is22nt/WTX9a96Vw2SZBpMEX32vuRblZgwhJ8hbxYoIAhcqJ6amEgUKhj4s0qvp/Nq15siQozyAzkJPXxgVjjwieGc0cV+7RCKZD0bzsN1VlZkEeEp18YIvr2sIdh/EGEXRyQIwUb+WtIY7HCqoGb9EY6QzcVR9Mn6Wung11VOKczuN0tKyXXVoSbu6KWtrUUYiqo1gGgLwdyEsVME18PDHSwZV3ynuMMaBCXBWZkG1Ozo/fhLePYQfzrTFD8tXEVc7/VHC59RcmQ+cEOzr1N52uDJPCOJy+pqZXsjxGzGyxL+rQrTvWhkO3rM872XBRsR1NDbaKj79y7CHBqPDVhLz4GFwDcQIEYjy12qU3rzHZNlPI9j5Gr3s0ntc+UjwzBFcD21IAkJ1LBGFnMakRJrFdT0ha/Blj/aXHCPSs37TIGOqEaJWSFQQBDFr4k/MPt3iCktqoQSwUuCldqHbdRKLwdUTmUM0/wNzFSnq2jBL2tfb1up5tC7rdARgi0oKCoZdc6o71pOMTBqQRdyT3piVotUMD90EG5pJI4Fwp6TbERB2cXyvlaTQM4Ws3zM6sFp1W/G9tUIS2jgvEkGDk5++G9h+KYMglAtQbxudVD5QEJ37F5h4No9nLgNeloZSDHaMDCwmvfXANo73+PPoFo2IsJP1KHVqIn68NeumifHgrgjNicxU9OVnz63e3r8tv+3Mgq5CSAqhzSOw2XMaoJMrmb7UwKDiJPaukSknIugUlopPzIxTgR98kBmTV+M2PKvSfa/DVtmcz7C77GCt4Tl8CeGODGLUi7V0J24KVKSunVQgGyIM+anA53QAZlTois+MJd26Uo1ADEfjg8TOlAB5AMobR1BXu/aIZC3r8Q+FA0yonjz/dlPodVSwhDlrcgFyezs1vv+MiNNGCzLc2FCBBFkD9XLdRmVrH7yQg8ZBza+Tw1DXlaH9iDRSGqA5a6vAx1hL63h0bB5kw4vA9RzHcmd1JAWErc0paWmyBn0Xr9LDT7X/qu+qQ07rThQwqAFtQ+s926EFwT3qRsAh3oNYucfFwIDAE+eXSLKIddpnXNbAqhFTzPgG5oCHtd5QuJt72FFKmyV9ASsso5huWuCeHMqUYns16sAJpfSZ/gHuKVm2+HZruGFraxds9147284bO8TZaPDPJ2QxKvX17Ih3yfqEpJTaL1PijPWet2JT2NrDe+UPrRu3mpOp5vQJvEtcg2eaI2hRc1EVMgrPmjZfy65XSf5qkEB+jXZqHcPtW9A0OLTB35OXwLFnZWvbxlENKfKtiUb0FtrxHdz6MsRhfp1FF3QuM1jAiCL8jqbRzAQEbeiH+gc8dItp2UL/2Urguo29Jo7GSthnIJFAPQ9/8Te7u64JftuLlK91O+r6/EbEyFMPWrTyevzxmMBJRoSIVVTeH8O/p0JPxx1P8MjfTa8V7TIkVa+VHzSksC1qXI7xn+wvjoSxeJYFBxmyYn3ZCPSlDiT1AcFClYCxIHN+yD6GivfA4dyNKgWmnlet6LAf7n6U4u7ZFuWn9uzMYfvBYWq4WHlY9VDwEdhZ8mU/cpkh7qxyRjJ5YN0LPKGZ7bQHPKFT+UQ/HuY8WmF2TxWEUKMQThfaykzDHXv4pCYHIoDLazFIH7U5C5gmi4524U34hbvLiinGtf8l4px7fk5YxY9jruJsoCIHW+WjBrFy8FDj19s7sxG4REURrs2c1ERiZlRMxSfoeDg62dAnx1CwoEwbPGxdGrOrMdhQCYmO56ciVxP/wWB0T7KZ7u4kHO+j2XMipIyeduO4hSXAfwn9K4unQ4ZzwkQlwKWlRI0/GtoZz6Pf63ZHWn7Hne+Hid1kOjb/Oq1iWrSCYcv/URwUNUKbly17bkHiANMLfAPyYvPZlXi36RlI1quwuF/w4Zgu/JptnnRQqS+gLyu9VqCdN/Kt4RiRw6u4W2KoT+/9uRsXkF8zTHcFGs2GtrWyEwqOENBHYxG7GQPgOWhF95JQmF3GNU7gjg2W+v9XfnmFyHmpSV5ZCsnXFu6vd2k96HVWVr6KGU07MuqhnZHuTYRA4NT9LDTARSmFJbBDQkkHT/vx0HJXbb7fYITnOXiSkJ0AEE4yf6laQNrJdqxFqP25eevx5PPEVVJMfcHBwVYcaNOZtAkHip2i8WO+BduR8rmKel7zpbSOjT2xgJiTmQDJGUC54lOhgiQpAD2NoZOlz2nWnrwRIO+wDyQtn9oY92nmzeKGe7fp7Alh9YdBv3VTLmA+Hdgsw99LyOnwV7UujROmoLdbywLFil4yPHvtHCXnMaWixm+0epbFTDzwkaK48NeaM3JxCVq418IT5lK81eGb5x7KIoEy0SCr5s+0MPUos/6AcrHwk05YIdBX7fPVMy2+rzWZyrBxCEJjmcaujbDoQRjhVVKHCBYs6d8kHpDPthIwcC3HDALgJi+qaUdRJpzfclfDHv4rwPS2N9CzRCPVDFU76IDipfAon42w29+HP6vgGDTiLNFL7xMHo7qKj1ZhMyNnN8etbXIucZzQYUSSzRW1gz5t1PymilYPmtMLFtFD/TbNgihI+uOeFohoURQKG/rLcXR2QNPfkO7cgf6jJKLAif5PMgF9wRiqnmaH/NNU+TeOqFN5yD8BD/B6tdb+Js6IW6/7lVs36GoNznAE+wEaFen/z/wc6Bq2pLzNmko0LurVGKVXHtljI8tmqwmpIzCoepbFtoTeYxm2+tIZC2abm20AuG1jY2ugzVqa9MjCeFPEAB2o1CajVWTqIRrvdFCeQxJ6NbpSKXFLhfPELkBbBXD+1cTyPQE1RzSxCgO1UNfoWXgnwgY1J+tYcB4BqhdsYrmRskHdWqSEZiP8JP2ZpmpnJj+ji6mJSkMgH3/AVog6DQ/sM1ut7mzI14+vMn+V9t3lzrhsE8GwAUCo18TjV5Rsz9xr381ZLBJZBC3uh9+KJxa90zq87VSIh5s6WBZRCV0YBngz5o8/J6Jv8JCDixTJFs9uthMKOurdbnr4owle5nhBVr6lhOgPW67+ocYttIzgvTEVLkdgTAPhuFU8TM2K4RgHEkf99SRIGq9v3TAB6rx0z+ZSSo6eFBCwrHNCVGClG/JzMRFx03/lBa9lzsOo3cZArVNX+gjxV0AcxlEdzeScxEc63H2+HIuauQDrcqU7AydyftZdsVBxya4+AaR3yT6pruN/E9fOJ0j67UcblHBoxlCBZTVIfn/FwsiMZb+2RuAodmzbzeyjV4nQKCoUp+LjaRcJnMSIvg2ydDupURne96lbKRsHilUvVYg/Bp/5E8MNstrM5gE2gBcRMW5wCLRVyGYEaquOGCC9K/iUP64dJzOttOaf5Pc3tL5RdTkwZHaoe70FcwpkIA23f+nSe5kK4Rem+6DJi211SHOSXkXygrZ50CdXsjo4PRyQrIb5FAfW4S407bsbKbUxPOwma0GUpuwNBgPkyqklsGomEnw9E0ZbFPZbksHyy0fgTW+fvENvXZjwgP5cPbkFXyiXy7PHBgVCVoVlEWOB2hPXOTrp71+x8Ctl1kcpKAMvsHp2QEIY/lg3t8JTWNG4sBFrtAFct7jYdLBp161CiffLJaMRwl1ZBLKZK175G942BwtKmvb84rMMhdKYFjw9ERCuSgkx45n39Ge3sdYXdALxjeCq78Ek0pEYkyUCem5rimQ1RAjHltqlPc/ebMNU7iEPb3STStxUckIdtKPdl0LruI3cBZ0ikh1nq0LpxTTMVV4yyMDb0upsr04KGSbL7WnqVk8m0Dj4ijWRRp8RS8rv61tDNrxYbGYKtvSTriwQFt7SctWmnpH8OUFWcQqJxhHHkb2uerBaQWYxM8Ey7k/Qu0wpoSq1z90E3MOwv0+Ae7y3UOyU5ncfd/nfzchFFU5XMAOXgWbPEVrt0RA7ImNC70HEVaLt4BVPikin9tBTk2rCmlEH9tgyAM1Zawf+VMRwrb+DUxOQRoLXNL/65B7lGM3Qx0eDNmFVkKMtv5DI8O5AfoMrmBxO7bdHriBeyFdexEWmr9WZgkNa5+EGZnf1Yfj9RYv0BRA4kgWn/9hUnlkztuBeSB6sZp3Uo+ej/fMlSMcX/gO+dqtYnpZFGxCqF7efAQ8vkN8wXnNA8uHFNVAoCkfkYPkm8J3ACkZfRX3mQbZyDj35sJDwaOuIs+fGQyx22Wpw+oQCQFCcxW1gnBPneao2SI6bys/WoJbdwFFoDXMDkGAnae6v+v3KDex1xiHz8oEiCpzXIdRXTWmhkaPmVnRvrAY3WlA9ZzUWoqCMB3vHk96nE/JsiiylSSY3T1jL0lyMLCFml6z1QavmaGBLaTNAAPmalnvHqe2rxJx/U3w5Qrb9OansFQbzDl7ogusg880qu9gLHKEQDKnIJcAk6kaq/kkMSQbs3apStr67s3AdtvxGvdKO884nRmWv2fJti+2Kc8lyq/eOQk7X/euFDTEdnxG0MtHjeMKaJe1lb0C8fEvSswKoEXhBs41x5+Cy3sV+PQDEiw/sU0hp0SySwu2SgLsGEa2i/07sBU6s/hnj71kwZ4E7Xsp+Lxp0yX5/KbVco8MKsuw2PJPCnDmxrtfmMThqpFM5UvS5MS0P3U3ra8dke8f46uBdZ2PCZ9V01YC389/cNQHL2xT50EFPRRcrrb93APcubjT2OhEyF7x3dxnBrlrUGOR5D2GfEYjqQ11ecb59ODp52A1o+an3TINVph5wk0xZR8rySLwVOaKaa/IUgO/S4H+zLnP2q10DoRlMsrWkT5cF8scJj2tghKkf/v1bEZJ+j2h4aithQnDwhf2o4j81b6YX/bz59LyQ7YCWZdFgLb4InPSzJIU8VGhsRs+vMCsDMZDmVNucTEUUPDJGP2a3VOX8q3P4dlyiA+BHWfIvb+PygKiADqk4e2nuE75Gu/GSDFq2GvffTzUUEc0Aul6g+fLqae2IfyoCHbQQ1eJcgt0MyzPWLOLYgvMgKGCn5+PJlcAZSAx/vHfG4jWPi3+GSujRGTx0o9biKCiB1cFdIfDupjwGbIsaD21GhoPgOqNz1SS/uAYVmCSBJo8z5uOkzTI4G+2nmoC9TvvL4NoUbqjOMOJt7CpU/WONTXUqr/UWXd48dMtdoQVIALTtvxkQE59jq+cjbxozJGzwi1EZnuWROtJfZpYncGl1cG0G6fj1wrtijOM2uN2411yzDBZ8EwuLAPlpWTpNnqkuNEjpWr9D3Lme+7zRXexQYPDm4Q3uRExpjzWhcTIXNa26e3steuiDlwc5geQkp8Hv8XIzbaZpy/LRgl/2G0PM4G1vQVhsG8gkFybjOuHUk6NaTCN1mHCd5xO6FXLCgRxObngbVuAOQ0iVsxI3cYAdm9WSucH7kBovTFAPxT7kE1jrc7zBrD+Y0t6b1bffreFXL+1iQqZtGnSLFtsVoZK3NuldD2qts5MLOeNsSgqBik8BWKYx2CyI8F5L0HtiIFAois9foxMizQFzxfVF7QtPUMPOlxJm/1bc+yIVukrd16kJX78I3KJFf1mfOxme3UqsfchHgV2uZ6FwK/0GlsYMhDrdAYoPYq6iTS/vOJ24LDfR8zEh4oA4C5GArO8RjN8srwJBPSZ8AGjK+rw4omt0Hxm5z7OzUbFNSYrMtESJ31EZXVlu5eB9c4pAGNNGd1ycT1vMCeEohhvJz8WCdQpmdrnv5R7biohn+Cc8s/LJUHocnqrD43E+yJYjPz5udhdmVrCD09/3AUQUjqHR9q7+vPNaocGSfUlsfR3EA6ldDGlPMvCu9iM2Go8vUWlpvZfRQFWe9TIEs6BRdtm7nfQ4fmVMWoQSk2dsupijoxph+2EKyeWK1Gn44xekHX9iWg4BRQTlSYYXRF1wmDr0/XCSmLaFL9nCcNiFh0qpp8nyH5eqlj54+ptqDd7YZlmr0hNiQqPeXQ+bEITO3/tGJ3KfNyrouAa2NoqQ6qqDhXoz5xOusA66OOlnT+iGYBDdmLCzMGZI1lEFOd8FjE3Mys2UP7lzTve2qVs5RuCBtmWN6iB/sGimBkRJ4swhH7e9y21wskshxHjFF544mjsOGvvQ6UYSySixKdFtW4ASXrdDRjv9OjSK+0Cs2zmhYimuWhheBjnebbQxy5tYgGqGx/bbstMVOmmqtxZhswi6OePqpIQlOHtO5JicrWwEw6V6H5Sw04Zdy7VIDFHPv3aMS0Sios0TPHAT72pJFrMAJaXQ/I738Ll1cvibY6E3O0ckgMhEP18MhVNShec1MpdVpxEar6qadL4m6mKNAn9+8tB+SndXUG64tVX/6MvPBfQW1sPuKWljyBpDxuYiy5rv25geiq6Sj5eOhPYYEneV+867svEoyy7DKjb3SLhaz1tIe1NDLUMtM784dv3eM36k+SZpP4mpvmMnUtIVZil6XdIouD7IBIHcOqYSh9EfJJAWqolFUhITfoCDbuoI44aUPBJKCwZoFpLOE9bVhDsYVDGqc/NOORMwAvcH96R+vsWQZR2UvJYCkosyZscTCmxLQONPxUz79iRCl55MbmnzPBwqJvxSEARRpfKNwQUww9SJcz1VTEC8XCUQ2uBLxA2G025fwzPoNr/OJw6D/4sl5ja6s36fnV8Mx3H1YnMiPuwdKXrTkZcV4BcP0u7hGhvR+q3aD8+Jh7s2M4ZU4zTpUy65E+0vND5VDXLojfKVgapATTvWm+SYZuybRO0nerGjReZZAHLJWKWJpYOBESoy8Q0+43MSvRkA13NNV21K6eVvt7VUIGn6MOlS8wJbwAOBVnrAPPYHT5+yNlJ9pXs5tPxHnDwsQzMH7GSivrSe89Sl4KjdjxXksMBYyVHvFE+vFfHEYyNjLnd0hJYwq7SfPWnL1NQob0lGdfvg9+xVMi0V+RcRTCbdvJ9CXyP+WMnl7cHENceN03YVE8WyigIzEzPgxRt4tR38ldZ2yaoDQ/qcXuqrZkchozo54nz6XYx8zrcN17kyLsfGGSSyyq/OMO0Iq0Gwl/+HaeqHxSYks6enPfCODIB2NT8sg18fqz9moBk22Dm0W+DY+rivA1kiyVmvZ579FRuIrUyDE1o9VjJrGQxvChYoh8w+q/dOAqzLRjl/IBmm3JyDPZFLGl3GVNrVeUepdvc6ZjVqxkebyPHNf/8PinF+TN2vBpwKnvYbv0Y1+7rEPSeGhX9yLzrsH9oKgjcDfh3aqY1MCsV69eXXDxw24HD3jnuXVRoW7AK7zXcuxQN+HevQ2KWQ1Gjv+QuuOkOJu1BQgcysSz95pIy6isYTiyLZj8lcEewmqY+QJXKqg3yIjmtj+MdnMkVR0/5Mptsp9/Lo4HbA25JTTGLJ5HzkvZ6EEQe2vNqGKmLGXge/dgZn9+kojJEXsuz42PpQZjVFNrczKL9SSv8C0ERU3/P1kuYpoDbzUhxcbSQhsqoZtH/IjSCppU4UBvUCgPD6OxtipYr5HqEONTU1oWEEGFvjdH/5aRs4TJSpPMy7oh6fyfeIZmeB3ZFoL4psYQR+GUl6BzjM+vhOO0kaQCav5pG5WBXjNn03XumnbNEPoaTxjprD+s9s5FhCk4BqHi542qVX49yupOiFGAs7xsrjEENDotWH+Te1NQ2xLSl20zH5KB8nFDLj/L5r0UqVIsA7IUxT9Iptgc8M8kPae9erWHjLsKSK4z5RXY6aK/8KC5qjN77ASQQjEIT+hw8T/V1g0ilrosUhjmJjHfeiW7Bws3Pz1iMxqR+DfOxwhM+GpOiM8X5DdbqbTnrYr/9Ff+c/XT6zZJZMX2uR2PhjN8lTkdBwB4Ex7Lj+PpxAmNijn2rYR9hrHQBbwBt8gfCTMrblPEr+jcCqAADI7AhjapUZJFiGu3w269+jk2xuzr+0q0PMOeK6+kbY3T7HRGM5BpYMPyZ+bEJP8htFUhEPbpL5Ohjmc6QPcAXusXcsxm8pvqAFn+ZTxz65x0daHqVi8tlaUQvue2YxS3y8BM13bWVMPUVLXnkGw81foQXh5N6pGoQV0oJPgZnb2tGM/fO0TOGGIVjg1488ASGpnS6aO7GwjoU43jgGdOr0YqvnNQRZ5CStHTcXRFX5IrCyY71zom7Vy7JKPa8Zmx/3Lnelwx5FUx8dAyNkrM2ucPAWRIMXPKx9z4f4pgBofdSU8Gpokrf6keGhLiuYNd3VItkiS5YSJy1uzjjB3IMHWeDf4cghjB3My8AORy6aiNE2hSLYXwHifRwL7W98d+WLjPiTdM0YIOqBlzzz5RH86EHi2CyYc1LB1yZaRUSn8MHhn869jZP2Lb5VNbAmqqCmWXhVl1d6/usf4kmxVltQ6DBS2SiE4HGRT/bH0jucuaTxsWFj4QpiBPuCuTSHGmi+Olg2IVM3XRcNZEXVV60WU28xmf+xYlYN3F+dznSBmZpRDjuO2vVKQ0T/9ksAkdOrrR+Fs4Xlm7p98aqu15dkqlJYouekqMM0X1LarRSPyu91w6vF5RLgGFzTinKkqA27fxIFkKVjTF1roXE0AVaRUHx+FG9GFuf1kbhUNdkzAGxWOs16h5iSj6afV+zO6L2oE3jMO+gO1ptkqu4XtQ5EACGH38nZovq2dQ8ACraunTEVUF+Y65fcmGDq7FIuL6VIby4de0ghhwWuJsJR7NnXxEqcLq5WxOldBpRdN1H24wNaYLZDeoqHQ1nG3Ju7s9i/5CtSPZxgJmC507dMt9LtZnQVb9eRaUa2xGjMgRZNi+BAMhQQWP9uMvXuGlB5ebwSZIg15SVhYYNa92j3z4yLLlRh5LMwEHf66BOI588gxg013S3PrMhOnR3D22dmQRbFgCA41JDM4UVk0pWbcwrCNSeQq0VGuzA7jt0lNXAMBRRFiGhmGAHv3cM/2Be+oN8p4/jKujaei6n6C3NQIUcudMSqVMy1YDMRho/O8YzIkRszTke79w/Ul2ZHd2Cf1Uvh2LzEJPDZ3lN1O6LaJTZKrEqXmQM6wPsS1T//dGjdEsWmnAV7AmVVUbvvFzjblOnqcTihBe7tCc6u04TzhrsCFo9JGHbBoPU1MQFAgo23QGBqq5BBnmRRuQwP2E4beuDMhIxqu8DO7WY3mzBICKWXtrmTmuMDPTImzsyU/XQFC++0EYmg4M1yKLX2+IdEU0QVPEMwYt46y48AECcKD9MQFqfcsuVIssc27jYyXRRGJF/Igwt5Ic1v2SA0Mnju/iZYvsOdWI4sm6tYpj4bOZGrhxFd7FFH1jDX5DDXzz9VQm3U568UH7zWBGVUBsGKY8aV4+3rz/8f1JE4Il4eLAL5k61hYHq6kLp3Dd2rkTsvoGXUCWrMDTsw73yB6fI3dgLM14ksSiq/03ZPDmPMeLQCD9PHn1cKF8uDZp3clfH2ECVfY0OlD3V1SzSxg+wny34o/Szm3rK29ZASBFofrovK3lCt0cBU4D8VyLd5ysjlKsz0PQOb+te+VAKN2N8fiHjp4RdNIjBIQUoXfkerwl70I74FcECEuqDVHzUmGRHcOO9M5QK1yuetaFV5+tUPZ5PqeGgpt5Ed1GSVrITrUEzZajr1gatXJvhmzvh/OsTQzwZ0Xk6gb4S4+3OwfinTAiPDWVKzj42PIVeJM+GmSPCOSa+Ushd+rjRW/aiEhYWeSX1cJvgmEDdyuyqV7/CDjI+QoDtwUiBn3poXcag3/9/TJf7PYAH/EvaVYPgeJxXUPH6LgsAE5VrpXkauuA6ntyRdXvgWox7pkJrxq3+92KM0g/z6UbRJ3Je/Vcw/KWCny6jjt8BX25fT1zlNn5LZosNe1CT6NL5qa8Dl/gtu09uGWAlhYbJu4Z7VwJYbhF9Jea2P/ZBGNW67iXyO0TMi+xU8HR2muHMWNEt6c1DVs882pWNe0YWA0cDv0ZlYXfavYf3sD+hudmoIHBoJ8G/CG4hiFPC1ATd7JZEig42y/Q52/bZUcbzogb/ceuqt/eF9lwVuUOLPg7jsSZNxDDpi3D1v46BgbpgdQ9X4KhDIAxpWilbCoa/zqVZbwUrpuTx6x9UBeIScugr6O63rqve2ugKV3RH6Iq9x9yzn9KhCltoNsCu48SGTwn8MO8b5EXm4hgzlRJXdSUiaSMK5TqVLz7+B8eEVRJ00H1FsbsX+VunW8AGJ+9qROTgQEGtsonS1hENZIgFHtoTV2Vs36J+QlhnyvGmy7HBve6wKeC9P/1HPDxMR7+eu1p9BWtwUJBAiuP0xWCPw03AvXftsvgKirmvT/LYCz+lmnzDFLaXRSG/x/kQDBpv0x2rGRyvszebqrXiPfnHaMMockVHjOvUvPU2OaM7Qg0oHpLONqD9Da0EXq9FAU18pG7jt0BwmOO0UnAqnMjUM+r0TF7P/ShhcYqOYJVrSY8JLrBB/LJ5kSJ9ojLR3V7k3TItEY8wMO2cH9YkKNWADpLoSmHJrZMn67ya5GhnKPjxG0K5EZFfh25GrRxLGeouGW2JGYRmbXkxdMkttTdenueyBQ5zuHq5EAqlHDe4fqvP6aa+PrR6jSb951ot8uUjBBLpY466lYTllFqaaqAZBnMLn5X+b/MU3beCaMUZH7ch27JorAxLibHUa32YiWzWklWjnauFJkmxo17JmVqMJbfWFezXAwXVTuUf+zvdtfTH+zPWdert7l6e4pnGPUhmj3dauPlXMoLYXtxJ/8OnV1yijebWzZEcOp5F52l4nlrYiF0fbDUL522Z/F0dVeiE5GzIVA6MKIW/dxLcw96P/fzGRyKZPtFTnK4JiTJB5/dDhRiU+MlFAsiE1zYikCHuIFpmHcNT080wb1KMYa6CdSRZWvCdZWq5ORZ59m/MkEQuNu3v9pQeoMJFKArgS/NeUjlao7rNwwm+Ult9nutmVNNFlZnITR2l87fixp5mY65R8SjSM0ofOs7HYwINafsesCI2uztgcYTtHhFaydCqWXeJrTmg82OagY/lYPhDnzWW8t7/Epd2kLjVCkuDiTiFzIRMWWJJoEl11iJxjHQtgvmKKDyYpWP9pt7Thm7shNl7qXhXlcJZ98S+sMNY0vvCPfnoDh21mX4dnUW1BjU210+J9B/Jc/hwxFgfZZGokXD0Fk3P3lbGyeFEqqM9sZM5Qj81tbYglqlDKU/VrWS14ILUDfr/KED1TAG0gXcJ3T9O5M7gTaW0+vV3iald9GZNiFoEZRiRmGlx8dV9Z3wchsK8itWA6LlWx0yEjE1cmFJO9Uyrxs8C4C4pGCYamwgqFhaVknorntHavdQiEY6rKWh37dV6ezJ1fMibnfWAzLcvxycGlQz1s12mBqorl4baK1/8SvxtcVfcJfRmnRsByNTdnBEV9WW4OubINlczwddfzZ2OwzULVgYKrlLBoq0a5nSkbwieHetHyPuTt3cxOBKTVpAojnD/5OtQXbYMHL78mc6l/a9YK6wqYeRYEyb8B9rbz3BGP4vEIiJef3s14zCQQlAx1pDNCYfY5lxQLzbrQOjtpIwXE3wdqVNMixG7tZ0nqKeL3fBAHfey2Xb1iqEIknR3DayY89KkEe7d8yDykCNv1OQVHJiNlgxEHRSyrNbObir+kxfSK1ZvjNYkSnlUfeYkhfHrpY77P5RjR1HJqht7JMqYxcZ1m7Ab+um1gj4gp0NTB/1RPD2Z5iimYDz992AAPpaz5UFvYPp2r1o84LENVRb4HEzdqoe+Hwl7gLBrswKHOUp6OYZvRNKOz93bdN8lnJo8x1CeAiW+wAe72yWDvRjTHHbzulNnFQnW/Sx1Lsdde3X2llww3Md78WSu9zRZ2Seln7VIN89SDnZeGPZu7zS2nlYspwM702ndlgJ4raTYYizTQmigoMWcmsSDeCa8lnlTX8h/SeGZHAJYomMWiVJO4tp5GYphnxYHfb0lHJytu0t2LIdHRHQTaPAimq3D6ccYvb1DE/4obKcOJdjM8wZHkaoZ9WPEEHAoKeASCsJa+64C51KGc8FZwgDhjLxmpng9eYtsu7o8XXj+HGMWmNQnR8TzZQTG0CCkcSaMUEcOkn0Aqk7pMgywdqTOgsVA06jwi3OMrUu62ANhsIumFa0X3zGLgBTyV7Pb45V/BnV1hA0QBaE/YmGeTBxFLkTJ8KVe/Zs6L9i+brt6oBCMhA+QJPriuJIp+w86lGvxMj5h4sGl7zVvIUcbOkMdWC6gbD9vi7OSAJDJ5lCTl4p2zm5hJ2rLCBda7d8qjymsG00i8j0Da4bkEhPy5+0jiV86LPGVrluhxVqzXNtrgfy1bKjy4glsHv11xh0c2B++S3J+csTzIWGf+3Ua1Sh6PRMlgXhMX6PuaB0i/RZayIcSoS1001Z5j0WaLZObX9CGjTHQuHTlkh8a6q3qZpYBoWkkew+jcB4CgUS/cYl5K0skbWzCYPONYW9trysaRNuNVlGjF7ue3Ih++3JTmLQa1cEhoBClBGI4A4ig/MC7SMpg6cCDHJJprt3EO5Oh+6tYNtyVJynkTxr7RyVHPZyeODJFY1Y66yZ8v5ID1HIyGe9z1xfs2UF0qS+hliLJOpxQRWYO2M3lgEZYhubSlJo22J4gi8pTD9z49jZrwmgqn0xYVyGXc86MAQQUpdKEJM5c53V/AmvMbUxmEZ/7CZvtzmWOhWGpQrgAyS6vC3j9LNDc4xarnFzVTrhWXPwyIrdLwlrAUpxEeSCF2tFr3Np9krtaD7pSY4EQynx469rROPa9Twz+aLYfom+HaGiNLVz1j39zM3E9Uv6LmT343TTZrbCvPPFpeqSPPpOZK73DWpVsScN754OIdO0hRmPB3VmhxnETfkEIHcgvsx4ybAtwxsv6cEQkpK5p5qLS27L/gedjVTNhEEJ+8DYzxLHdsNnGQ9iOnueA9d2sysUoSGKokbDQWqRf547KKCELXJhOIJFs0E3u3GmimHy3VUgWWNoBOTVDWaJkvqZ1EjZr4yxY2KjaiZ/ScwH2wzItQ7Zp2D+m51eR/SNnf2b7beANkExQJ4QVkdrGjXIar4z2rys95vyhg+jO5+IxrxXyGqW3qWdEb09jHMcXr3zWViCqYOwBLecAPqQRKEHDQS8Y3hkvn/1rMPBOzswVsSb1lEqaT3Xr/CYaNd1v2p38AC59c9K9aCflJY+dT10vy84XRJEf/ygAuHcu3tWTBTnWNQpqIUQ7/GXn7jktOCSG70r+GyPnd6YHJDL7am/cAaWTiw7K9dkp+fZDrjgyy2BDZOmi6qbvXzf56JDu/pwu7AfRJTacrhn2tTrqSy3GgnHQiQq9QEwicEZYDGmsmBGWpMD4UBnTBo05kM7tu44KRhmhqFrZdVbFx2NDEiHYTtB8HFzKBqoP10387p7HmRW+fKL7up6rH8pHCsOr1eayPQdsa7HfufHgp0BcinTI/fy2aoc5nWejEnflj4X3PlBdBtW8K75GJwb1Qybjuhc0j81mC5xir5e09mNXCzAb47GZMb9IQCxr44vZ6sBltI1IuoqRF8wukZVM2cm1e8v+e9snvmTNHMMG4X3FSAoo9j+WkZzGaYecTjMW4JjIjmIO2F/47sdMi3xCu9vCqqE2H54COu14OctG1a+2zkQERl/J9XJ6gR2/F1+NUcQRXa3mDUBiFSAFOB/zcM3H7sB1R21iEHrHCrn89KFGYpQv9e9Fhwy8tOe0nC+E+NwOY9duXZ9lVPbLri+WRwGHiMJumgBQLul+/KjCLOPq864StAdMFC9y/U2AfjRuVElOBjn0sjI/XwIKqcfPAxV6z+s461almFfHavgbaDKOXnzzqR1yizRWy3A88gUaQnIQEFWKaJuT5k8N88acMjy6xlfOwJhZ15INeHYfLRyAV41mGDcKQQsR+5RIpHc1K4cKeA7NmjslsyjyDF2u4xRJacXsnjxFmpSuYP4rzU//Hbfwj/fUQMaR23a0AlfdLIM8RwRSwPF4vKRzh2BDwRkGWSJc7GhwALwMN6F0W0jSbTn+dtByGhkUj5AId1ACGInhg8F0TKzpWZxpxZXwIe0fZpwnbmdFERwHrYr4cWoR4GRJ1h/Ld40c55Zew3YYNj4700fbg8zzTCDO/Qtq1eRu6fxAcIx0gWdOBVK0btiV6Pdzlh9Q2P8N7ldZZS8BQEpZicEVkMA8eMPfnn+enTLNCGBc3Rxrl4ZOK8hTx+nrwtX40XtQh+HnCxMpgAo6eisju0ZgAWeX68PRRdFtHnJQY4fgyJKG7JdX+xlDbY+MIV4JB08fh2zrV1IZFScWuJ6EIXh38KXeNn6bZFZKqi1rwjf+i2n7Uojv1chU1F7HJmnVX5ZZbOHeuUNU1q2t6LmECfFmlE+XF3N9CzB9T1hz/omtagQM4RaZkHn9DWoI6fuXUw6vyBHMVjzo0Htl4EL+IugbUouEHD/GsDTP7isstjfMGJvqcgOfvur0zw9h2OjU8CIeSc4DCJx4TBFT7pNcOHYIweTgrCYuQ/4pa5O05wdViH6vwc6avjI7FSpsahMP+3e8Wi1NQxH+xvYZS8cMF7T3jKM7QV/fNMYrK5cAAHkZdgnDtiFBr0iWJL85RmYylzWqkZdVFTddScP4ba996sy0tom/ekx03gfiLOghnLMSOLPKr3v0oIhuu0XCXmg605zJsJ6LSk/A619v7iFCRTmSo80QV7o4zi/9TmWBQ/PO/fJ6Do1UQ/+TabMx9o6naRiqkjqedmgYShVUYp93d55RAV/cUSZTYvRUw4IddG35iha6Mwb9V/PMUq8R3ccTTD6fnt4H9+uJmzlKvYNFIeP0cfN+DhFxVe0mxbClpHYE/BYRjMmfVLcK1a2CCudx45dA5NL047sr4J81nL+6bCfXwLMpyc1z7BPa99gFWCX81O8PgemYpuRmkQS4Alvl8eh8YnqgXSBOdIZPtigvXVc+xRVz0fHIdp4HIHlBWEn85zn48Z1cY1v6dPig/oi9i51B0fAaZNNvAgFWHjz+7TBnPZLToQducfmcSPoQgnbaRbIYjXK0iyGfybpZ9Jo3yQaHu5w+rEJPwUCZmJCYrJstnVUocjtE9K8u9D1nE+ChS1RyXUPWTKwRUhE77R+nkLCC5RcJPt/xM/nPzWc6Qq7NSa1+LNmjUqxNUoBwqkGrfvQonIH/C8gsT2OJcl8Vk7NjGYXV6GMQKQGvxB3/iov6dcuZIYyl1CwfQi6vYzAhSDJqlNapTrIwsfFP3+a4utxQti/RRAq9h7YmcUkHE/k8PGBpHXZMK+n9hRrpmIh32VHU+qoxXZWTap3cHe8HHf2BX1mFh8sPhYyqBrZdLMxU8vQ3UbNoKnBMtBhPIAAIcj/Fa0svH3LbDWr9GYlmQoIiCxDibjLLg1Q7SqHIMDYvmW36DjhlqXH9tSRY268Mq0F55pBtbvLkiqaS7DzivpKmHos4LhyRbqjKomJ29Ucc/jjnuImi8Ear7kd0Q1f6Jg20+WLelSP1h1bVc1H8Fbp8v5OC1ji94Y///iA4oncfwSHu9WuVOmfn8DaqbJoEIpS1fBc3BzHK3gAzHAf+qR7bueU5YZGXQcZQqVOE1CUBDaWV4emeRmvayMbLUSAQXNRM6qXIEfnO8FiWwpkEbF3Gu/qsg6mDvIwfoWU2sUgvGjkRwVG5UkfMngQoRqU1vldauYBPVz/zykupRmfGfNryHb7VNR/cCr//bfg85Z0UK5YEhvpKCklQXtxmBTUe/LISMLqHK0mJxYriVGJKZ7JJf/tfSTfsgD6Zn39agGfwVH3NcfUBm9obz6Ik/KIg71fuNiJsGqaM45Va36ZYI3092BCnhjbf+a9ReTcZqp8JM6/j5Gtp2gk2IBp78tJgvng6fGNpdwF3nZDEiwIXegM1H8oUbHfzIhS8hOHQ78qwLDshZO+jzZVNvZWoBmDOgDxg419DHe42CzCW17PWZY6s9aP+nD8swDOQkXnxAoB7nHF8JihMGPSCN8Dm6QRDk80S8xpJq2vJh/ytOk2iGKpSE/RRsi58Rh+lMTOtSXtYFt1HAEStCzUmtbEKNi7IQ8yTTZsF16fUJTp4U6lTLRprWn+Cx/+DuWZvTtXMl/2gYi6F9uL0YWzXJCazF2HkloKowg2j94ZEQyh+/d+j+Xy6McEq40/KcKWUphwWVVhgudChRzPbF3Z682pxMdH1rbkDUqzCHjgwtp7USbZAnloWb3X4oZbgNn73b5D4I2NwpfhV3EI/kisq7BOCY9mPrz3d1zk6Xn7LWntu/w1gTYuKfMKyYX6AhiSCnjpA4sbuG+OGsAxTNj6eu5o5rfHcAgfUDe6G0Z2TdMxoHPyhENwpD0frhEqlt0sFZ9kGdZ3oRZgPrMz3Fm4Lgyp3/BRcdeBk3WAvhDiSAvHJZHxFaKv3I4gsrPmksN/SIzv0wNef0Tn2JrtRDYZg5U5sMzd5Wlwln1wrD7WxEAP4vlMpRu92hBgUfv1l8K/GUBEFzTld58N7cBSfO77yHfnzfbc8ASNBlaeFy+6DH1SYTTE0uNFisXGwSqxDoliy1+7y4hEWlouVScjcZhKBXnAAcMJSy8y5ai7R7EULzwZvRhGZ6iFZAAbwCTL2zsIPqtAjk+/C6nYiB8RCHnuWdSshCaPnxuDxk1vmtMOn90HQZDMFvqcm5RQ/9jKK0dThKCKbK2a7ueAoeX64fVvMez+18vbLsJ0pgwWaI9tvtTlkt6zr47Y1IbWoSJmVOMxNYUgQfz5JtDF+nh9N2ONpBlSBD2vJpAUhwpMMW1Nvdw9H8FiTA5uFGpw9wEDiJ9hXdwOf+RlkJWmg/GkyDrKZskIgkht7jpKTh79op98pvHqwlt1c5MXEVYyoDwNRSAbdBLWyv8Ag14JedTY+ZNORFjQTs19Ps15/ByizvmLFy/yMetdqGFkQR4d8KOwRKzjQb1/X9sSNqFqkENazwGHNhrbAXc02OEAKCyQsL1pjGTYf02uK9+u2XljG1kruFb6DYyRkNZil2kiKuh/AQIok1FgbkPPeAZCbWlhEY2GnCozMs38asUUMixwmaZFbMiVqDNLcTMJxDS4PyrjmyVptsdMdrrq9R/FV6NI/IiamM/3qL1Y3zRjTnAXDKlTjgmxRW4nOkXbdyxlj3w1lC7C+OMqmkE+eus4pp9WrsWgqIQ8cSoHVcNkjhqiX7kLVbM/e9IuTdKmw90UlqezsJ2tScPNzmKP2dCY0oz6n1GtrGDmj5tXiPYRbCGAiXEcxXQMCNZhAXCEFV47I03h2jO0NhiaqUahU59ZVRMGebt4aMqe6O/X/EsC+3Gs6SqvR0NW6KD/W+cbK3SWtnveEhvhXtWEdjLPWdk+W87BvkMBKiepfb5o92erMdt+H97biH1ZDTuymw00ZR+dBu3rRSylQuRxv10iLLl4uAFmh9ldwJ4M3mM1C4y9zFT6JX2VphHR39JshJUGvhrjGk09mTMws9nRp6qOKY/nKQHHaXxU+nm1Zq6iBPjO2MlV+MrXw6691M1L1Us4FLC7AsYNKHtihBrr6aNXglyZ/zPkbLPKF7WdTxgEQ3wsOYIzKwlkPLPpMt/p+y7VW11blsdGnPz0PqaPelu4hGrHKRzEmdsnMfwqVXFkzlHewOlkzqJrrzjTfJ0RFQb0cVih8APrmM61LqTnvZFliR1OpuHOYdA3x/L4WswInlX4ppb3AKVGDPmMJcI9oaZjZo1pGsmEhzKae2eiAZjtruCkQJb4QURor9w22jztCUHKEZd/udQoRiKeUyAlngLiuxZoEfqczUd4KM2phlJeCRWfK8YplxPWiS+XUrATrxdo0hGbxEUgUN2uk0/yAbbnljI1uKVBN48Trq0AlZ1vM63oORufu7K9q8bwbu+DkrRy2RZNbxxKbEfczs52mxUw+1mpO2+yQGoz2iFwY5smZeuRWxIabJ2RHy2oOQeOeDWyLXDiISzah8O+PyxhUZVv9+N1UgFxRohLTnvq7R5qO97QuRjGJNOelKCojp4SfqPVM34t3OFXgySjh8Wxw9IP/cqmpNQxYi9mXCP2RtE53izW8hTJqRYAjI186GlZaxBpgyxfJKL/5suwlPG8VZhVnfUUPV85m9CS2w8KHHoStlU5+KFgach4Yveb8dLXWAPyVC4E3y/eZsdwNR5CQ2B9PNHJqCBSeE6bAJ0WpupTjAONgrc1bh2s22pdo8mpKMnNb2MFqwnaBJrLlNU5XvHaTnkvH5vWr6RfUOTS5wu2RHxhGSFcWowuhQpeckN4T79ZxDkB/zxa4jA8j+qsWcDTy0vQ4g013f0+qazUoMJMgZ7GS1uMkUSV1v01BjzmbxkFZFOx74DQqKrv6GAQJIFqZU148XxVLwq7J3Ijg6ePvt57XyuieuVEBv2LC5Ax2ph5nbFfRRXECCwUJgKZtLaNtnweKpMbUoEMh69kEZjJatSAE08Dpd+g9EpYjwpv2V61XWPW/DDO0ODPfHmprplr1tEK6DAaobpOrORSiSqwx8C1dqo5RFU7r5ZuDUs5hp1ZpuMaFpm0ujQ9OW7qy2NqtvNWMR9xLmpOs0hHAwYDrtOX/H0rkKkmj8JrBzCJ6VfjmIqJ3pj5UDMZynjdHmEYF6NjdrSJo8vpHPfd/1i8YNja7NDVyqgFhDRNmNSdi9RgUmHfr1VcMd/t2wwLXCaH2cnWlSZ8+bukTBsym7EdxwEhJWBi1tX48CZQZecYdgeMRMBd6STT+sf23oto9PAkest6fmy60gdGVYvYEee60sOdPVqq1WGFiDxYy7ouOoFc/Q3oqSGU8wBhLIVTiUc62brE04QkwR8sFB5GDpnPQ0dUtUvIFUaZKNjjSlCTUB2JBc7ToXfzGxJlrbrC90vqAuq+iH662laTBD+zIie2mwCDi0ICN3EL1M50/NyvOnLCKSZakRuf3PLQP+7eULXJo7laEEnH12fEAdkWG8lF9bxLg2dghQhMN6uhnSJzVMc01szKP0eyfiGm4jL/YWnoCUqH1gWoZjSu4DSdsr8r5bYqjWNZN3/sBJoptjxefy8pEJi0CfeDOELjoknNW9a9rb+GhEts6iJTuaOq8KqXUY7rrEEXKyf17N3USfA0AQLXqv/9FJsZTxw+mC/nf/vywdasyNSr1iBtQf6qmA16sAJZzisIiIPGbGUP/0XOiSkCWKmTdjKRhBKX4PAr6SwjsXA5ruYkyHAG+vq2rrWsUl1lbt6iRupsDVOz34pKKpWFdSLPt5ZtiqeU9seAQUZLdI/vE88svAIDrzQi9RNIh07MnKmN5WVrMSzfZ/kUw55rAiwqmDhapUcWqy9J7s1R4RfUNbXQvt+CDMfvpP1M3llyQAtB5piQBJZ2v4iamMlDTvJ5DPOPjVviW060qNt1qG9uLLsaSMHWAZQJJwCNyHL1ZdONGP9yz0VQ6h4AzkSegBORaCG+oyinOyEDwDkvcytxw4Bi/cgbWwEp6QwVLeh63oJSW6AjGxWSXIRDL9ORwDb68oJPlvJeJBlrr0FiRLTaRRRaJwzc6xjKcjwmNWOX2AYabE2wOYeHDVPDmwtCWlfkWeFW1tXlqiVAjZkbKbG01OEEw0TmT4tjdKaTE6JxwuZWQZc++IeaaeneI9nvUoUFIIr5YrbwvfbEv8/3qlp8QPAzOpDZ/GAaSB7ogCQJiVeqQRo9kJfhy71xM5Jkqmfw3bC8z8GTMbQ3skO3pAbKyW6vblr3hupNKu/Xcj+OwE6lfzqfT3AI3Iy+N9C9nOJJMZxtVKiJ/I8mV73QJrUt3AlpPI8AV88/MwB1sFx1LOFdopxd8ZeGevsT1XOXekCXYHjjUaeC1Gb1F3rzMLFzIe4GJK60eN0WH+4PZGKyQKQamaXS3e4tRTPsLnf6SNJakXQKr69BmanGC68FWMDYkxFSz8f56KRrldrPqeGWRHmpPQ/Q2LsgvIZAUVbaeIqlwxu9QDh3GCZ7ZWFlFeukbjjhr7cyC2ewRA1bF8+F57k4EGGKRSjEqg1rrXrQ1EK5y5mmnF5zbzwnVWvFb8QeNziYHj0cJK+0rPoDKJrLlUnRBya/Ii87szQNn9vDBNIXN/MDCkZB5tagQbAmSuRlp6NAczdlqeqYG8kY/VsSUAlKK7Lg+OPlbiPOmfIDB41KY4FsGiqiJc2aSQB2mgFbZmgF0A9LGZVK1sRRxCiiPgoCsDVCcj7C3MB9oXCmuOOjyi5HI6ns15nykhcFo1VN4e+O/PDS3tGbDnU2e7yb8W/awkbUN9+3+BXEs+NJMiix2uUSpIt1WJHczQ/KfGBcLOAWKXNh7x5Ra36dvAgBTNj2ePEi2KMcjOkjsip+DMgoEkSTQVQEmmz5Vl2KqwTTZjZZgRZE8jkLaQ/rSEP0QPQrUupeirTorCO/QLYsKtks4537aA2+DwJwfoV8pQAI3QaoevbZJa7xuLfgqr/7xKQ7OvMqwVF+11rbUq4QJVNFx5eqDBZpv1aHhDpxP7wJWa94+XstzN+XVFN/ofuPWL+Qa4gfot/yxkGLbexpC+PHDgmVSz+dEftt3SdX3kgAKWEq9hVp5wc/n8KL3AfjhIqWa6OySJkTPw4vXlFy8mcnQcTO6LdB0bmfvZRa7aN7rx/5J3SR0I+xqLCBYoD9VcDjheccRxslC5OO3BQKye/WiV0cIY+vNGrsxp1hlrk4ScjkXSGm7S3hDQaWajzgrkHh7EmplPREZ8hn5mTGMqwyMj2J2SdqMjmQ5tH9Kl3NthREf6J41ySrVfM/FeWWSEStpEWnsaZfVyBnGsnIMAEAPYqCOACQtS5CIMi1ZwRI3hKSaH7YDZ6Qbbxreo23NoEBx8I5+zMp/lcUWIAEfLwpoM47EvCtqUMwinguZKphZEZwd6/GKUsju/YPboHI5VIvU55c13xq7910CLC5ualForrhnk02yJyKmzgaobe/DLta9KVuVgWuuiPlyHLun45pwnHmFrd7+2GR6msQs/nafCcEJF92Z175Pser55AHUY+r7QHkNLe4ob0Pep1YlOLFf8dqai3XvGrCmWGew6tMeh54dm+rA8Q3DEZjQKgwc8kaK0uLbmPqatoJv1qgnGvPMovBL8GKl7LRv0B/Mlh1Cfv3r+0yW0csfqSoVetot0xqFJPjNnpdCI7dJNTdtaHI09WKw2xoRwHKqJfO5r67LOj+N1GreT0mK8uqwq02flmAxvcpoCCUy2q9bSSy7TH4azunY0gfx56yYR5NjM+3/1rIYtwTJ2w6eChyJFFwjEnYFjaVPrIbmWROS7OCTY6XR0JWDwI+Jr6uwJ+N6TZVnESl2Grp4N1m7RcQ9IfmVqQTzbUqouG2Niv1+IHYPR8QNAYeRNBGlDcZ5xz/JvgNRzQ5fQrMWRDSU6kBAhVpJUTLIwbBRCKDFgl3F8aamtLg2zmTnSr8GTnRP1xAcjWx0amqfqzz0OLNHBfRF0t4F2BzZbz6Bn3eM0Ni+9D9zB529fyydBKFZ0K8xiMYRpc+AoTO1u4HWIGu4+OkQaoCZb1S513FB31eFNNBCAJsn2/7G3WlCrxj+WQxT9OTtP0PLq80vQhvVbmgTMm/+B4JjLu10Fst9VYq5iVTXq0pmM/Q0rnaLa8JL4FpKjRXq44v6dTCnpB2vnGVQB0SDDLwHQAvKv/ZkaunnmShJYWg609C5oVn/G6Bek1P3+yELVQ4wfaa5QgwdReI+Mf8J+RWERpvGdm3ZE3unOr+LLwhOB46GWQk7Wsq7gpCioU9rjZ/Pnr8O6FrpDtXhoYGwAOtHOHz6FUA9yBTROYVyuR+suHLRNSZ0yy2S2v/JdmHuLaCw0souzHSdkaUFNMJKssvKa9E6oF3M6QwZBRFDYfH+HX7jpgQ2gdDkhUCOCdynpKFfSBW+Q/IoWcn3DgeFvnWCe1IFO6J/PLu7ZeeNzUjzi55PsiN1HndWc3dN67T4J+rVSdQEvGUOPi8aCYwPXCJVg6iQ9IaeIEn+eu40RFRARh2xiSHPnJBIUrISP6ocWrOnPPVBCj4eaifhg4q7nDwsYiRuidPJj0VQVlubsnT1tzJhMPttpMorI2dfzQXLDGVrUaI+uTMW1LRriHlbdlZDZeLKl6ivqnuUbhhZKIWeu/Xhi17mkcJ5C+sa5AMmU3I5N+3ZJFa3CZAx4SKXu+Z4jBFCGjAIedNAkx9gDOZt7w12DKaDzdN6LZdXd7HZZdf/+SWJSgcXQ0jqPI8PSdqXUMgTn/qqihUt8o1CVrMDujyrRORBwuxDDuvnd1Nq2qpQ5214pRTkMiP4xEPd6kTcmvl+1wyli8D0HQnOQW8wExzn9FWC2HQnFe+fM9r5XhpmRZBibkmfvDRtL79MMEu+UfrQLKYDe414v1hW/lyRUCIXSxArezGvnIFxTspwqPWFKNH9cnDWL/D80Ruv9OiNzpYA11ZJAbSD9dVJJXg34jOed/iHUNFMKstpAQ2tcVgD7b69JEDLUzs/EyhfhkEher3mih1WUqfSvV17Lw3k1UGejn2EeEoYKT6fXu8j9GEQ8WS/33kiaeuotQ73auXIll6Ahc7CFzN/5H1VchbxsGAtuRdPHCRi4mypjuV/RMPCEw2AiH+lsINHAxQgP2Sl9gBWRVLAtj+BdvgvsI4f5fMyYjJYUa7D/opxUIC3a9L9BlQorO9DKU9BVcf5XxAw76HdQWRBzY3TzO3l43UCOyc9GUm0E4m+DRbWAlHNFgoKztjhwbFsRPGbhZtW/1OtgOVurVjv5UCa3wC9AAiN1tfXPA+lD/Mx1IkQbqvF7QHmtfEy/u7Z4wBNb1ANSjMVq0Ay8QEXVevoVOoC+1RMCdTC/I6qyZTzUBq45WKYDkSSX8YjXstxjqYKHXiKOLm5MzgzKqp4zPUiME/DYC/B2bpi6JBtAjObhFavm8VlpjNqhBuV32LtmsenAKNyXMFOSMF3imPfYq4xxLYqXiB1s3ogk9h+FfI/BtnXLSQ2nrUmT0QxGOECCASEJgtcci2EoB15NIhxtd6DFxAYLarDSXA+dB+J75KFrM0YiEJwLImPDuBRdyIBB1iobzV/vNYjp/5Mu/jFEQ9gQi2OD0PL0TPr8h2oHQak5C08poOXTWvLJhWEq/BqC0NdQOge8JacmnBgzhpqkBXUC69/HoA0MAkye3GgxaIAWwQZmq9Epsfq/8cvRrsFCpGwZYXwRDf0QC9izJqj2rhrv4TkNBo9SURa0dV42i2Ajxa52H1R9X++zvt5S1tpKWSwxkJ+2lTvWy3Z8D5twbA4GXXErzDYk62l5+QdY7IoFM3dc7SjwokhkDVbBJIlizTvniacb6rEqXYbL2tndZT5AJnP4uhzS6f6oEckZELk29r0+bd5LzQdbhFRpkWpi79oFmZUcEXertlBqWpjCHQxmBcDJpt901ToaA1tjMmdjVCioXNbLxQQLw675tpTPEo5v5vxi5msoIzxrluugmAwdW4lp+gkjJGAznzUzOAzrBiR0yzoB3jbFK2+saUiU9nMhryRcdSmFaJ6NlCmHO36qWkzO2wKGNd5kSUgTv6jp2F/drRZR+nrmU0E7Ax6gINqlJrvsGyMPv2nu06v9WeNxLtyzuhutBC+YMp6zDaQrLPoCZo1bJhGseH9BeMPy89ORI0CayJYYfrw+JUmCEOiIttfPoEKBqXNxGq1WwgJz1rUoWZlZL1Kp78P4Rh08ksWZCVLZri/18rSe7sLn8RA2AFVojZ8cc2HXWBL33ztyE2QU8leqQWW61sTZZ8spscOUCgsFEu6ChlEVqqYpttX2lDTfX6GMApTBssmnBTV2jRSD7vGS1G5iMm5FWQ5lq40dmp04vaSX6VgTCvAc3ZxasnnREbsFEfw1WjOQ81folfLz9EQc5jA26csVQimrMlJX4LVt9MMm3PIrUYQCsp7Sb1jpXsnOV+T3PJhK4FPpjgUElDoFVdDcRdFCPrzSDX1afnN2k9xIXTg7xzVv5JY+fb7yduewOykr9hMdS8jVDIZ9Y6r3OhbT9upMLOwVk4cmECVhRw2hb7ZSVQElZc05PvxnJFL31JoflqE2ncWAc1LA0BaxKHkQLILrRj+PHWgg7z1WUzOGJTFU3Je2qBmWsmTFLmAZUICneD+W+7JaOs56cmWdw3eMOJ6l2TBwuZiFutlHWbXOgirWdtmw61aHwcfsMgLdYZvuE6pqB+yO3ZmyUWiiOqxMQDjsRftNKubyZpmhtqVpGtk+cO7Gv92tucqKuqiVv9B8CzPykEpz1RJwHhsXkvHWpivz6UmX96fWx5nxTDu5hR1xUOlB24VckyrRB81O/0tetHuy4ST2pnhlvTMlp2/wg53ulpRVMiaiT45QJW5Y9N5o5lkN2uili7il2R+6dtyIDgjmkJLZpgO9/pnvwgNcJwJKABjC/v72bEC6p25JDZ2R5lKLv5GXmHKNzM8ljrmttnfdm9l8nWEWwpRsuT0nl3PT8uuj02wJqt5BqW8A+ln7mfET8oacJeWsQvzY0fQY/Oj4YNqIydnBRqh8NWto8/r0Mm0a8R4WRG7ao7npwEjGXk9HaJQw33iKdXgVtEG1w57LhO557WXKflSc23E+8NiQyzubJPQyZGtcBlVcwFnfLnwtqZmzZHziRxSRQfbUK7A5zBUtXm1j3QwDiX85mvJXtuCUzSXS1+wWzJ0EUO2o98byh6zD5DPmezR7qfOo76GFl2/TYpZlTDD3DAkiq5r+0x6N4+kIZBIbZzDBsSTJ0C05goJcADEy88wcCfrKhaiyhvjqBNpYBrKwztA9A9TR8L8GniG0KrlP8FALd6ChIzorNz2E4Sd+eh22vj/RmEf2jZZHXbkz5am2HDZTf0Ew0MmUh6HGRYT4FmuOeuxjxYK0L2vqws7aJXkfN4HRxxUlSFMTz0tu9ZegO6ADC8qqrzvVxsXp0nKklrQH9m/rv/6pJx3CKGKOdrCASzBl9Y/sIdXipd4loxwEFNwvUXwTQGeYVBsrpoKrIgOCzieWeggrMbfofGnittdDwU8FbOUG26mEJTb8YCy5vpteTJo8EK5H8kMkhPsiOeE1AWEoryjlxai/o2RMFP2M52+0ZkgmrZjTUwsyXOozaWawBPWpJ1aF81RMSgmkORHqvj//8om5vRLaeDOEJrhIZRIpzXkrLe2/R2h1kQWLmjWJpZmfCDT8z1loB5cvSvAnr6i9EuhuH054UL6a5Nvy3emjdAvTluUGMGVn3sxs8g+KXUt+nsvC37OiaFkgjj8gng5z2aTM3UgrN9hcp6tbrqZZIsea7hpoPN3styQbv/RA0ixmt3cTKUjXscXcxvXiF17A5VfgQPE2Ck3kKrZMuNy0136V3U/Nb9UfSmrGsMRAPOKujIHV/xhPAEsdoUiD+vjzPPfZgOALeKw6swPJCdNZGT7TeHlmvP/ugF6X5L4tuEb7EGVphxtVlfojGM7HJkmva77+BslVUt7DsSyigedFhmpFlroumX2jJqolaoX++PlyObeNiL5vG+VwEm+X+ycpAOwLtOWVJMQ2HGIMhSt1chDh488xLnr3LUEwuM5aw36saQmrxDfkgCn/fgWVuzvFhNO9bjYSZXMb4qLM7Df3Hjm3vqlI+OjyDo64xgogeh8tAsbLk0FJDhEuEKy+BC1yrq/LS+POndMVxgNtw+SLH30muqkiJ/Hf8MmjV1SVsbqpwPx2oy9XdqgGwCs5pVOVAXbZjcSSw3HcHDAhM9P4thRlf4GZrw/2A2qG3HOENbaL4NdJK4HOgtutzDVQrMBhq/R2UPUosi4rHF/pXxyKfMPiCrGZWZfW6Gxh1/vOHZt/WQcUb6wkRdG+UDVhIWDK5an0kx0po3bN03chhldci6WzkVmb1Vodm4uziyDPwVFVUBPn/AXrFZg/vwjpGqQyekPKT4xksvJu/YR/zT9VIfvwq7XMCUMYkdWBpAFTttqwOImah1j52wNC5JgreuZ39QBQXdeD9JKA5zqXDVNciduHIydNVR3seeJJtSn714QDX8HybN7fIx7M0vgCcF/Oho8H73FMH9Egw4IXHMii0spkm5tnh7tjFn+oKKzi82v4IJ7nwqokysu2UXfepVOLGzM3jNfenp7IiCRIuRG8FCh2aRvnom6fgYNnlrTrWIugs3G26fynRgN3BOULtqjwkFwP2yZL7I9wZosTsQS05D4vSN2KUXNmBiPNvMUvlN0E7tWtHYabJ76LQcrm6VA8VqOvtlvIlDRKMKRkako1LlTV/fKjRzAL+Q23Rvkk7cHHzMwyL2887T4sz+m2+ogltKnUfL0MjrBXM42Cw8I6OQiE+Hibbfo3jRsur1ba7vVFrgLjGOn9o9EaiXZnuSSwtCTYYngBR0ZFSrtifjJ7mKhr+MUzCm0zYWCImLA+55Cm7oB4T4eutuGkItWqWhIT40oKVFmbP6AehK7fQAk+eS69uwO1/nM8eLzeusGwwMMEfRX/H+79KQE4AKc/hlxv9t+NzuEApiU0t24ayNHV+pt6oVgZTNvMPJj4nA9wTPwkHRcYSXgJ/NmkWi1EYS9AU7fISiwDoycJYiQSHf2sH4LyaaA5raD0DIT84tjfbTBhXHCWcxJdmzz8JheVCji5mqdIGcITbQ6wjDaI9pwJgkBhsbHsdz3R198Xn6uUQTFmJTkMLSVeQTkASTOQq252sYIy5Zw7BhHWz4rLA7ezS5UFsMthyfPCCJwc90JkqojUWvu+Ea1UZRJXMEHAn2Bydo+rB7VZFKd5jRIib3vPH7LGojhnstkI4cZqpIdS6eBQXeTE8iM8hqH8jbJoMVHnRi5AiE1ptLYd/+YRR7kDg74fWlCXLSreWlAnfeLiUwN4oi3LDJ0ukbNhQTAPYDCvvps/uJMh0nqvSbLoGtQt77uML8skCUtTMCvXLmgT0tYT3VrB6pOYx8YGNJ59GR3WpN/vzXuNPvwz18N7GYL9nWEz0tehh+IftsK8ciWQMgFhWUam2VCrYZ5UWy9zG4zucbHyz8i69OnW7IrOSceZD9brc3jNq8pjae5A4KWUf+pS1r2cEepjgkndJF0TKFqjbyXo5hSXQ+YiS2r0A9wRXs1oeGrL6PdrW3+ijV0oZ+cUud8q7gI2sUyRvXs6GthM2R/6ILN0HMktz7WNW1rUGhn/+8NozyEWlDjBGZwIldbu7oiElE7BfuHICq2n/5zoorT2cyIONy6MfQBsDw1Niuu050Cd02aUPN0Rn/wsYYfVSaqUbHNpVtTgCJ32d1jLBBRduiyjfDMF6kKM9XfVH9FKzOfPPL79fHMTXagBWsOfNTx/GD1kyadWo39k/MgsNHPX+gLxIb3lNyT4f+Y9s6EV/9JPmBJZJoLVqQWtJqR65yAOAtdIqqsLLr7XMiZhUUVE18qgCmoafVylv68ULlDPhocMEvcCQE44JOprI7kGByI4Q4ianYbxiyo99IPAAha2O/JhdI7zpttRBh5hvitTvsEcaHhxhOn4AyylDL6UvR3rgOeq0LJjj+OGJK0yQC7olp9c0Z3QnVU8548CSJ7RvFdsToKUivYElyIuAvzuyml4Kvu+vshEs9HqEuOtYFD2OZ3bvJq/oriWlmGHq7Pl8B7vYedz7hUjWfbPQTVVte+28MktUbEHbscWSyphD5bQYYrznNbtHSGDRATuTA5DxKJrOMFuPWmSxmQVL+DZJ/NY91xe/xhMShhxHtM4NzdehoW1gWoVePoAiZ+8BM5cw/zYWAk+bwyMuuNLL0N9E8pR5Wn7Nzk1V7m5AiggbOpeVieYdct1aE2/kbFrGny+EoQ9CtOapArXah48K4HQSrMO/PphrLxPzXhjw/jp1MoQIZnuka7ETR2EUikjqEZAA7XC/ISNBWQVXXbvDHqfuufjK02+8q+XCq5JDfyUO8w6lgSee4v0bRjrcXrX3sImpUS4v6Yh+nlfJyFBQ2q7wrcAaCCg2V6XieBLIBVMbibsPeRmxJcMJpptdG+CFwwjeXsydHPyq+iKGLrKtPGO6aInEI94LM8JTMheuAndZfwzBV7ezAkPILDkJHYi2gSo7eKK76Dg15JImIGhLW7LNylhOeGtgTMq211a3rrf4Y8TsOF0vZUsUwtM8NHm3nw8mykQknOA236llRQHaZfBgQnmTlJo8AVW20gnCx8LT7QGRIPaHVKbpN6njy+C1Mmu313y6m3CcELk+9dDB4SNFTDjs7xWl5cvMPK2VYoNLeAQ52paRz0rii1ccgiuvYYSm2g3BykujSOcSlTco7Km1Mhm1LMi2yemyanTfU2TplAI1aSRHvIEKhE8vwaP+arJlP5pp+ABO+3NV6vQUdeM6chHIhpJJpygSyoV1plcCcq8hp1IwDIbzJaZQbrSiZ4EDTQKGtd0GF9rt21fZSI82zpzAKd0E+nyXPWgb0rxE6Va+2zk2roM+pb72na4Z18pXQiUKbUqdrl38YqxCgQ2/UR9h03z8NX+lioI0XL4GAtpeFjEJ6+th4vZIQiL0ePm69LCTVMPfbKJFvlfYyzjp1D9WWhklw61J989B7k3q97BTyY5dmDmN8sGGluOaFm/TiPpgI+Mb5S+IEQ/NMjSScBTgAAmPXjFdmgNmjTeBKj9pyE1ofZwjIZx4/P4vFVNiujSrkgvuSzgB7bYfgckqrMfHFcLORUgPhxcffLhEoErKfL77LZ4kSlkDW/Z+os4TKqWW+Lt8tWolWUwoLHoNdPRFN1Z1gM/Wiafr+ZMqU54Zgj4TRFEuGNl1WjaYGEc7Cv1r75LQz3hoqQPpFYqFYfMe1QRTQStgBF2qfiDuL+7laOKJOMpP2qwaCzpR6wp49wRzrDiG/cfmsrFGhoOtffpbqtyY5fFHrbdkGdAQvhVzoSIcyRDRel0O72UMheCh5kiGpu6Nd3YlKnyST7PRcz8Twtq6XHb8KqPnppnGH062m1yut5DKSBNi8QUlF7fQRWSvrerxHwnKcPT7DlRVxshYvf22BKIhVPeGYAQC4a0yZ+zCAeecf65CpA/LoqBWzHXvLOxjQOzui3uQ15amliGNiAfbE6C0HDbEsuEh5m+WrhNBnxb4y/q8f+nXB1Ba/Vr89CKwXsLBtGCTZeKKyLThAkQSvR3W6GKRK92zkelm1KWnTNCLTv052ov9DSx1+DzXEh6iDxouvJ3uEw4+LOgUoLAywTc4EAUH9tgZeIIN25966I2S13vqRrPRlr4YDZkGVrPDjeb9K8+NsqtnN4qOzAXLZMqsj2NhO+q0fzyxeJcyihh/4PAkaR26VWeRdWfedGVHB3MwKMOO2SUSLXUOk38GbN/bmfbwyOr3yNHSAGSBiP2T6ss8HnE/O71vFO3Ns47SnEf/uVZo0u0AvxoIDGn2HUXUoSSfEqDpxNa/Fy7OLmS6y2GqpL00xTHWr5I/1rdH/+opCVptOj7g93CxW1LJuu3bLskzNVkTG8CoBj+nU/Hw0xB41gUJcb0MZQ1NSkV6KX/VDBf0u8wtBxpKnl54bMMKt8/nUuvJ6GCDg6a0d4La3PPDJQf6dYwV8IdAG35/fJnjrlrL3jVNoijtixKE7vYkXykNpNsHv0LY5ds2gjrN1C5KDqqy1OPd1/Mno7oWaABWft0h3AIThHnZIFXpTZ4m7sHbd4aBuSExMNDIY5ItotQ/qLoqAPCzgO4mQGsZbKhX7fc7ySEkmcZZau2vCgUn0v2fcnjFEQUS7orThdt5eIe5HcsdCukqqFlztUA7Qt5XEt0EidUNxY2PpQNn1eoWuDrTLMVxdiY4LeKY/PoxHHrkcU106RL5FNN1FABjzyxU7fXbua6Mx45yn5RKTrGU8Nhev38dRamROyu133mtxiZebgJSXYO2z60fy7iAkeodtGWuSHiObR+KFuEB1mIWSUy4wVPWStpU3UTKBlxEBRaDBcNsCIVQ6ewfBQ7OEX+9EYHts7SYX8kht3A5IHpSfNH1OJrb6vD6pVfoBMa0FiTmUn3PQQsm4towSXM8oDJBajVylAPH/pikoaJU8NWUmyVL7I5KbmitntoUKNmV1vZD+Tdo5eq9/zV/EccslfMOZH4kzjPFoziVycUl893BkPEfXpY+84wqTyThta6RS7CdXNo5dlFN732RiZ4ltGCptqvf3itoDKjY7aUH4tfSCDA/uC3kBEf5MfJmKNWZG8LQKeGl2qMZmDlviBn5F4HrnUbSpNRIJhQsrizuFbb6SW/YpU0SIf4EvGpqhGW06ry63FOkP+Q5t5QjtlzKXf5ALY0w3W0+Kp8W5FjL1sFg+BHTdMDY7+pd/8pL0kELogpd0qWbS2+hX1sUFTbMrATWnQ193tIeL4kXP+gL9iEYo7IVz8HADsTEsL907Q1HHHaEFy2UNVKbHibfVnPkFbBus4RP6ryJw83qaEaMaulZlAEtK9xyIjGwC5cejPzTmhDKh8SAjH8G8OHmwc/ltzJm8lQqs/ClKPwPI3gVw5HOwU7xT7Uy2EmSmP2SeS01XNQRQnvAea2059zhC2K9TRADUpJsua8pmPTmxebSScgevVTNqzKi9MBdx3GZGLfg6ZSuSL9MGG28ZRAK3Vkwy3ZO2VqLN2GtOer++SeeUvisIhermHhd+uP9eiKQyKRxg/iOnlBmNhLnulnbvbMUkuzPFoKOZRHa/vnPOQLgc6DIGdUQUXH/XMsLCQ8vJs5vET6d2uBqDJReUO8NRk6KyD/JLJTIvP0zFAPvAOSatCsMH0j/p9GL6Y+7c+XRJvTn1u5HBwlpNu9XnxJLyCxkyDGjBwYe0C2zG89KMvLVgXwoLCSbsVxxIImkjIHwNOj+sYj1OkLEk/dC+U3Xd/4JfE+NRuP/HV1QAZLM4cB1ot239oy0jrKe/MKhZuVEJ/045PcjQxXu+stRqzJMgEWVpceh1xVqJQZxj+FZ0U2b5YnBnMQxv1sYOgQGxOwsD9Y/WSXK0F2hOqywLjY/sxVu3RdF6ovMmSZYjX0JVwFsat336nyMzsgFlEmhMP0VYwmRJRQ6LxEuRvSQl6vBdXz7j9v5pGqlt9k6fmfBGXfKbIMcakcgj3ZGMHVMUnYI1/1z8q+uGk6Wgx0WLWJud5qrQPaFu8A3BVKtP6H6WNLsXOa8t9jaKetWx9/Gh77QZunWhC4VC3+Ghd4rZHVDu3eqP8yIfUKt+yz2sip10N7qZkPPk6Ot+tiXONqZAjSMhoodl7cakun4CJlYw2bO5e7/9LiDeMCU+J8qWbSnWs8S8paMaosjArgRH9GHZvrqBTYTtI9l/5m9PgWRMS0uJs1crw2c633K0E/B3p/mEY1F9Gbev498tev3oe9IWfugcTXZITq/EwQA0iHGdttYj/LxEr0pt9oF53X75IaFk4JFpuTs8USoc3OzIisUPwzt1V+Owghes1IgvEinL2Z8UJ3trm179/q1OdUOdOY3c5+F2JvguK4zWffSD9GsCC7uPOnNGwU/KRiccxeAcjiKrLDcaGTML837CHxUpAOmNpIo52+XrMDhC50MP07URFMeZ4qRz7Brjcc4I/LMTJHbfIScA26EYE8/833WauJ88Tok/Yf4xfsU+ZrutLwQhgQiVYo8t//nYudLatBHn3YOMgoGmRKDkjhWJvuMAHA5CliOFTDf+rOwILxAWo4ck/JvFZK3Q7in398Q8g3+qehS7DOZ4hNOFLxF0G14qh/40uZjZZMfCr4IvFEsPpEjSiHXGiV5bp6f+OUHmjpg7LlK8tn3h5u4iHTqli6qKYH0zjMAA223YbboO1UtHRwlRG4LrVAXUCvB4/yZ7VqTJnFKAJ5/9vvZlfviAjJwjIUj+wdsROs/iqcHhtWkgygPB7A0Aa3dhmQgKISPg8ZtB5oaCZp/LGAi+ES/zLFunoCgXTlnl9x9GEIHxVouHhDeehwnjfTVvJHaVut8lX9/HDrBpbh/8/4bO5ZNbEvgJMwnYjKCssq+2ItaX2+NSI2bpfd6MjfTGLnTyPmC49kV6jYASbagdr3PuZfofgNTRxSRUONz2jabYzz/5GtVU4A5TyAMDeW3svfx6YbEJ/vT/RvGL6BInEohGD0oa4qtU4eNlGjKe3ocCCzFiUJYPIF3RoeoLHhI8CcLPHR3MZt7K78om8kZ36pQ4gBGyJs3JzktAaeNBLrdB72V+rztRiNNoWI0WubwjwWA3hmcpGb9EFsHFmFfwkOXOC6Ch3c5pahuQhjj1zyMmjNQrqt3YgbZ+abeBJHWtjSbG/SBo1HQnWc0lD+RYrTOa+YuB4biWhxeddOEnPoWX27LwD2iL/LuB0b7EWA0CNswlGQ9BSscLj4g4/RCkv92pBCQffiTiTI6n9uKk7KgFLyFmhVhe/UO3QseYMttZni0a++Kr7gIvFNMmdgrG603f7hnEQsOCv5HOKqS+MH9GDbSasaiwPDhbtHEnZEhqhgXM1Y5A2XeboJOB7bY+k5RqWoPBV8JDAUY8FeRAqHFdyQpXft4ZqNVhs3DhLU61ba7g6GjWcF9wuX9iYNWELUHaVpEwzhrQ0Aa9LDr102UfbsvvIugPuFs/20Dy32E9fXlyfcmsroTZQ+xb+cC20Uc//RfKvO5fGVpWcfzMfdwl4AAzwGkUuHW8JJLnF7MVjas9dZDG+w7LN4ni97QwrYPSr/lhKywwxVFVmbhayMOS37GphdBEKibSs+Q1kNUg23ZROXekGceLjwyVgm0jhLffX6DuVpO5Gq4QoYd56Pgy4c1giz1x3m2udBVXRf8hrtp9J4JdGuYuFfMBJE2herh/mCvEJ6r8ztzqW1pXa0O/CbeBWD0I+J2pr/Q3cLKyiGCcCMj8C2ofLXZhJb0YSjyQaSblLeBl0+69TlNLuYiOmoA16m6sFC7qsOdW3jnY/wT1kJOlD/7V8VW/AStk60o3E12jKXDU59je3wuirlc4auzNkgLrdts7DRxe+BVkN+bBd2Gg8cP4mBQJzp6s0UtK6aWP0aFzB56wn0XaPtW1esoN9dUI8dwVj2rtPeOztRUynJCGBJ7BR3CFxjdlFNKQQax9V48vT8ZG0xer268nKhN5U4M0hv196wZ9keRIRefDZ16V3txjnBUcAXg4Ap6omk4doHn3SoA++dxqe2B6kIa0v+90DH8/htZvZFRWN/76Rs0HVoGp8xtbDGqb3h4s8h5UU5YWXNde6XxxUPv1buMq/mJP9pQ/hny83W339p1HPs7ZmNCNA/K8vvTfLjJUrjcdkekCqSkgu7s6EqEBTAaxrcWRP62e1m9KJ0i7wfb17folssOsMLC9cIuKk0cM1od2KtnqnU2j1ijEIx0TMO04fmmMPIhWDjjb2PXe5F964BZUMob4JMBfxX3coB/iqPwrx6ofs/hKrZomGZFJlyTegycRBEoV1cRNiPj1I+snQ3px62c0Jso1g0KUwICZQGpE1YxzCPwgsL6w7EWmhPIDAcZalGbUWXUcNj0J6cFve7HqlfaXz6phrXJzD+BwB2s3d3fS3OEE+Sf1+TdCDINdY8eB+smi2l7AyYHBR1vglAfOjMVrXcZE8/LO6f4WM8vEcdT2VqMxqVQ0ijlMZuDSYVvV4t53wh1t+e7yAYPobv2Pri6HihREWvWxb1X1GgyASX/q0DWSR7Qgn5V9xE0vnnVixW+5/vzzfBovUfCMqTS8AJKfAEE6wdhG6H3/12fPx5L47Lwjt6JuOdwYWmL+DOq6C50jAxuO9u8BAei6TNv4OnzSKhGcsMfdC7dXI8Nej5Zpxh7VhtYXXi76SswER71mr6ZRylEXbC8y/R5+q2YwvHiXuRUlYdpN/DgVOlfVtoE/Jkt9PnPRD8uAW9efzbNAavqRLUhbxo95upIPYYmNiIp2uXdLxDK3d5KhW8BY+wspSSDWDCrX1WzEdDx4Sl5bqLK1YgvK4+FgMQCUDimY6Iy6HXMr4OJRs8MlPYxm3ZhMkn3vDZP9q1jPVXKqIxQKD9Qofc9vZuts5lx0MWXT+fPU1JNsDdrKNPtKTMjxLhX3b41sPGDoByXXCaZQqWUjdYjDNaafMIA50J1GOXeq0ooN4Ka66huA5Qs97depWQtyc8xBxh6Dl9Eo3wAnGDwsyV3vPsnw3qrqB9NNxjhvD+AdczF7G8d385Xvaber+XzRy2h45TpNh99lX+Pf/0DcCD5t83K1iZj3lP861MFxRrhJ3T/Lv4XBjzVanz9+2DdXx8/Lw14ZH+IAKLmvSjSeU20tKIbQ/JKyqPJKNj1erRinJJ6iRrBzHNNHkvIBt6ZVHaKb+fcqNtBCHv7oZA1ObCrKjrD88zgM8YZhesi2taubIuBGAtqI115YaBIiaDPVNu+PsOS+kUTej1lkcoc4GLCv6f2kZ/YPtIttm/xlzTS+m22YK2Ik/gqcdGNrmbyI1mirhpghO/LBccigGVgKyGiNi4I4jDjPAPKZe8honVD62a0fB+DjsGly8KurvqbfvklVhCCUDAj9tqjQhQAoo5kPY0BTYdKCvL1fmzOGGADOdR2VUH0WLw1it7cIzDxZqnQ2YGnOfHMgI1Uq+wJ07gTXX+vVWZgE04I09HVHwdMbGLUifyvIMU562ZzcyOGFcIpLfQTvgAgk8O593yP8Q1HhDd8wju5s2ug+GgCF6oisVTa6TaJe8ZgWnXvewbWrOBPNhZucOVHhGypeTiNu48YqxeJ07PPssid6/LqXaUBt7lCCqNAJqLRZH6yhjhmdXK8XO7YI+DZhkCpzgWzDLUa+1S+FqhW8KLgCKMZzsEuzW9YNHnBKbccSmLw11meEff6CHKf8TERLKNtJMrMyd8BL6Ti8cwI6hovUJHLIlLqHJsvhq7tlTWdrAJF5BHGTsfF6l/MKSqg3LLOx0gEtH7qqzZVkggT9r0EZmmxPv78szjRg7u+nHJcBMajEw5ljlv3FlYJCbBGRP7I8Ese/L89H3v9hyI5PANY19bdmxM6jSSzrvGF0PKpjdh8xbw2FonJ4VI2q1mabkmtfrMnyVzH/I9+RIHnRm7d4np04JuVybV8K7wZA3wKpAzt4r8F/QUxn4f4dF3hYopQDh3Nu7FMMWKUya/ga0TqgOH3n+a/FrmOKX0NwLGEf4RM7mLPalQMuflvhbh8bwGcVHjoD02oZgTwHNdNwL7JEff3BrMbVsvHaNBw7HKcuvwbSfwjmAviyJNDIbavlwS7EQrB+o8N8KmxiF4Kk87c24xwKhGeAyd0AQvS+st17CHLJ/4YoR07zo9LjgqT0v6LfojRKa81nUwurtHSzCwCrKF25sQ0HBpqDYHj3rJchpz+d7rQORNteRMvFQIaO1NdR3ThqjiN98nM7NBlshNLDP4oGp13wPdLGIaLef74z6nUvIr2FSPydPlMRJ2zyAK914PVWqtglH0hauIIHtCyFIotFQXS3FYGIw5Sf+DnUDTEVR3TTjJ0x/ZBG1RnXLpjs/2TUV+FLXbhBzqAkqJQHCDHbkxAB8HzpuCSoe2+nR8Lqnxy4/MaAAwOHPcaRgKy4/YWoZAzZBPUelcUnLmkzvKHkfjiArD4mPJiRSauN0RwGavU7x7l1aqnIPvVZfT9eaLQ9pLwBh+2+vqvMzzs/ljaAb+zG4Jn1jPX+DayayxFwZOG/G6E173IfIB0fuG8AwTfc0bllWTmNEw8MUzAToU423MSHeQr13crcfwBRvX4b+5y18Z78MlvR+QOhKrki/quykGreRam6Zh5jpfORpibpnMSzXvrJLS6orSUoIDCVHzS04no0H2qTU84Mec274vA0iOBePvrk4ISGqrCF0FkSdYRlFeNWtQKyxpmh/RQSYKUHSYFSiX24RUtCUxZXAqz4a7Ow8C9yozfedEAearSDFkLXZI5PUQ/nkEFW5GcjRvUYMH9HbZju6O7vVTbK6dxMURgbmMA9W+pt89iJ1psNIQxOqGclNxGaCBLMZ4NymmqpAKLrQHgNRaVmiTdiY1zvxx09IUwwWGGVpipUKP2z8668GY1beZPdzR++Aeevc7ig0rmMyX8vOKQECJAemcmzyW624KU/FTYZOfOfuIP+vrMV3MuqrFonEv/l3TeqQpSpTXTu5UpOZTNrDcj4rDcAXn3TXiScO5XeS2GBpdTXO+Ixmcqf7kUfddVtKgwhUSBpDwizFTo5i/jCO9Ki0B1bEPNRWNkOFKJ8/OhKZ4vH2JylumCKFUk/JekXdIneWX3CMmD9T5Tj197ejRgC0O/zVPG6Lk633X2sYvCFv49KaY1h3jvMIWCcO6i6rWLonIrFUpfK52PUel+DMmlyNViWl8XJ2lrcUWgTJzrwngyLO+ZjGM7sv0q68ADDEJeHbIAbGd2lapJjnD9EIND9Feu6nqdWZPqpSzlAu1cG9y4fAZHS/YoFGifzMhN6rEEMEplcns3OXrr9RdSIqgu4sMzsbKz2kjKySd92/4h/2XgpRpxKn2nBe+RZ4+Qn6vEglLjqm2VaM20o6Gsr6YK6reeh1M0WhXmf6jFa3HNatnUwErd4BjwI75+UqXOG77x/wqKCMUX8faFLcxgSdIbPnjwPS4HnYtGRMmjmcBYyJaDAmhd/bav1HE3sh2WTGsEgLCbc4G8HVOHwmG225DgH5ANh2ad8tks5EZRuE71qKjAUf7j62L5/yuOyZvGEA5Uglual5xqkDhmVWNVjkinLudaYpQwMyq4Xp01yt3hrYK88y1+S52qBW/D+SJC+xnfUuDiVzC1qpFCO6I8abUmjWEgYFTFnWsbquS6UtiY+WoQxFrlmPJPZlbFUg4tNKdxPUxFiYgWHPTIsn7NMiG/h1BjBfAwN8mxWoJhN19mHPGZLWr4dFlwMmNbFtkQYFWCRfMJOEayFg10ubkY64toPsPVdDUH7d1Fie6vzqo3Sa2Nv7OvDRXIPIvJj3aElYWcJLcyjAjhsBLERX+IQe6eeEN7sBpEcVpU8JdDkyqgk54CwrEF8A3c3rCnU6R+SBGcQO+XX+hJJisimLu1klvNkrHv1NNFnkd00p99yODl3lrBfzaZYrBMa/YDuC2xUqM6h1j0DJs1GDTnOiLKVTNzKtBDdNGAME9jKgjdgf+SH3ANWR6l2uDvvKiQoBu+gAhvCun7/8oTTgf6Y7zH04qI5iWQTMiUaITCG6tGPqLonRFEVO7FfTlG9RVgFfZ5h61C+pCqrYzNWqN6pTcxinBHEsI76xBT8LfcY7RHrwM/+bM7e8n1VdiIodui7aiEW3JWhY5rKj+btSLOZBxW7Ajne4gssrgKqXTzZShHBcTc6NJkWUN0ErF5Oh2FQwjIKFzR+9hw0ogEHpybF1c+oa+q5alQp622C50k3/WNRTJlTtrrJnO42BKfIKsh7KELzkg/0BmE/zOYI3H40KnzGwe0qSGPJq+CZR2rgYhdK6vn8AbGPa6N/TkCd2gSWozzpX6gLwh5wdEC8hDvcWB7rlmtkvr3w43yfU+/QetfmcyYeLW7kgih05i+SStlx0HWt0etGChNrg+LUs+aXUKPzcLVyY2zzdfiV5X2F8v+Xx3N9s7Kll6oR3TvdAtbtuDS3+Swmn6nbT9QS6JXfe95wwr9UVyOX+znzgffKmqTr2cQt0g/mwuHaWFvIY5dCv7RLy/1N6LmWlUIpPdAApL+d89VTrwPpFTTewoGcskP1yuS/5YOEx4YP8i8+kFHQN7LcBfTvJkkAYEpUMGyorvtUr2EN6TNQiwJH9hHIFFK5oI0EVvPhoTUrp2E+wDFRFjFVwG1sB2G8guZ9wLawHjoD45IPFm5q29LdSCd8BoiNnVyCOSEOmCdnhkJ0tQmt5W1MCWed9vU16MNRzhlcXoSZmVITcfc3sloAmVxy9gOrJXRxzanEgA/5ab7Ber8c61S2XtT45ZB4bjcrECFPCHKay8gtKzVG4o6WkktBW8WLvf/gtDQZfONnI5qJqlpdUsoaKV14TlNG5zmqBnf/FCck3pNpcYlOAUzMlg0YEvVGpoD5WZsdbYiWYzoq68lCF+AAT1fE7OAzUg2f6hX5RWzh8QjEwE+17SKJChIzhokyG/f2eRDguSQYaVs7g3JvFNJS6FB32LMgP+BeDwqW0gYqwt3Rqva6laNlABGMpCVAz9zrv8NgewEjVQfR+ehnmU7dzmzhXbfkKq5EDRAu0zpUUD5cwN1/cURcbejDVHbGpPVjExpUMD2DWon0m5ou8PCg/qUEuKTcXH/KEsLNJvG3iAUrd0CDvDX3DbR5JApbZAiZ9kcDNcPLWoktLO7fenpKZtpX2aemIqrrBxSK4TSalpHosXavRxOvTdrpb+mQ8KPfT45fvcUn09HdxjakYyu4jXQn+wqj+jew33QqdMgi3xn1GCrCpJp2I/R8T8ClarZgq/SmUbniieDWm+hQYy+Bl87iJszNexK0DwZYn41h4siSw2ubz9Uh1B+ArQ6znIP4ZkZDBasZg4T7jeFQIaiBpFeAek48EgvW3VmR01DHRMCztrMXSyQEBdzzA+tn8YOmuRkr7OzwRDrlNFPea/+YqDW7b+Pg7Q8b90oi3CNjhcWfWxacYX6JwFLJB46UzdL6ujFfJzOFpbUUJKBELD/9fnH1PrV5gSY3npThOrqjr0m2rUgX3ljL88tBkKAGXZt3exVSim+j+SF7Dre5JJIEQivutRSjjAiaNJqrDC8s44jIqx3/OFPQ7wdcNAIo9QMwxN9E8QWc/QRxoEadlJ8fCwCiAWhTt9c0XYk3KU3yQHSc9NmSwUPhJDIScoNedErdMLZ1BWBigcQuhI/VOcLOiHqKfLA4l8hdbB1RKaXWnURCxWITHae8I7S43uBrw9XGCkQyYRrq+a/NQCHSoWlOV13z628lTl08Bndenb2dFVjwDCobJPSen7xUZI4Acjm89soxu9vZNMXZTkkTEwopuw2dLavR6BXQLwj/NDn0IsABkwsR61od2mpRyAj5xmG7jyn6l5kFCtUhAuXJrh6w1sGXRXm5v64PrNXvTs4tQi58QjCDC30lIHzj8cM0xFITBBf/Vrv7rnBf+44WVSd2N2AvZZ7SF7/11kEHRP397Kh8+gzeHP3efdDwpK/oQT7ywPiZAyeDPOyFBYDPvt0RDmNAH03dX4Z20GJc6jpPQpAogfUIY9ViO7hH466Zro0AHmJK6LU8rwIV5/D9+SKtf+qqQk+nb314KnjkJiivbNBvMetI+vQh3yiYuBqNeUyv0nenJ+/S0NmCgVDEuKSrWYNOrkuU5UF1f7J1K1izfn4/4NAkkDBd4fFxbShao2MOpWfKOndLns7DfLX//bJYjmZHyOJB99gdDHAhBs0xGEa62Oj6ltuhzg3Evk1ehpUz/fNNgjyfmRDX7URMKbBIlBQcBJCucBjuGDsNnIi/D2yVXq9IlIuLcihPO/jreqCfbI5Tbe0OgS/g/zFQ8lI1WHZ92GcXcryIGyThm/GVpgP9SEl56g5MlqJtmyEyMtVaUg6FDst/cRgqQHHIj3//gAjkuToO1tFMQ0dc+FbFRII4BaGua8/H/KNI1FCsExKX67k82b3/mXFw0UoeF5W+JKBzJrydp4bo7quEjpIXwDAAL61RON1QOucvPhgdWpK/62eNa3C3uiiVDRVG5h+jfRofhAsa1NPZUcmrAG4IgCLla55ltzEp5sVyUNBCQ1gtRTLI2EFUr2vz08cQK0bjWuc1/wHYN5QPrDsrEQ7Yyrcy3Sd4cK+i9sJDwY1tmwO6ON6BDOSFHPdjkFEcCrriJWD9Ot2ZpMUfW+1E9quBVuqe29HhKbfoW/RuWzr6dedzD1GHkx4wKWaL19AKTiPFmAwecXBpYVukA6Dz7njY/UTl7s9sixqJxKw2la0R9iE2LJLlu9PFrkojI92A0nSpJJin8U4TUQr6zkRwzVYhvDVRUwRnUQW5347+LgRzDFxgwm0pW2D9Y0/W5jcnkR0Zh8hWOT6ZlbWV6bf5GpXZNPeunuQQ72GVRqHnEYI9/7/ZLWmn9HnqXfmJ6rbIW34c6IPggVlvSln7DDE3xlJ8DApRuFkGb5pEVdgRXW+zLNusYClOjS7m6zCc+h9RHNEwVmnE1X7aTM2oViXappYyOjhL5sbdRZMmxFTz/DY0sox7YLUUJfIYkckIub/BKTUy4oo9DSIoeZ+mylf8w25UGG9Gbgv54ONAJVQThilab9D/MVZyY0LfoEXvY37PuLNTxhtK9O0ln+SNwmKl9nFyvMVZgpiSGqhwVUo4CV2uEpUC17eUSb3J7DWwXwjqlM8Jlmb3EzoUqt9IfdtzGpdC/d7n9B1OQZtBwedH++6OmFajZSRIMWm4V0qPjq6ceedKT/oFRNVzPKKoHmcdEqNMNZZf9bnwebx0+jio5dXa6EECctHIZT+Afu4wnlujPI6Z5gtsIwjxYaFRdm4fQQQPEwjVIoj3GJMnmMThMZbE93NK93d3utWhsU1tcni4JYUJnfA3Hp5t0mFc3aq4oAC2yIOcXk0YKnpZX8OzwI4VD8Be2lVQnjhDcXqW8w7fKHLNKo3nggPcUsVeSLUYF3mrzMLKkHikjFZKnLS7qkfmC4W0FpsbsrbD6AIXAQ6EZWcEUA8w6f0iiskez2EK5zT2INpYWp4U9oew9p7FIC3WgzTXaDWWk2yLe82B7Szsyf02LkkJQyXTj9mgdRcioBevGLqU4vI74fo0bXnQG/uoPs/H6Rc5cYGTug7RzfOy0tSVjKkK1aum430Y4oI3O/XkS8uvOYpi8pAvWC+P7MK+MHlO22F/ui62js5tpJl/hki7Gz6mhKU3mKShyP92UAQHmTXEvFVg3koyA0MlrBfgx5MMYejH0fVfhV43GCx9Pk//PvHla80MyMUJ9qAihJwEgK0wq3AvYiWA3VHYV0wVae/JyDTf7F+TqFwl5JFaZk4TIo1ea95O5eCWtv1oi7h92bOvBpuNUsgO84BvJUR18aYVWG/MD4d/9ERz2qkF4sJo9wrI1tsHTdhmhtdQBhjqrD5ZLBeO31QIfXZctA4AYKV+h/fszrw95L7+ZkUmOLwNz69o2F1OhUxZd2LdhWpWdEjXp574sASVXSo3KI+PYAwAjycrW/rbyNzzHST6ZtsLbCNDE06MckTCNGPRFjkAZQpL2hTOdtzu5mpEuQ/FgmjT1CNlbLM/TKDvQkjTnsfGGJ2naK2f0+zWPg/QXg7mqiPf7noivwYD/dq0+K0yMyqSEDlmu/e6inxZmjND5Cmoxjsw5zs+PvX3spz6EpfYQYyTFQmisy2M+ZIpIA7G1MMtyZZH8v13gfcNCRLHVUPNLGPHKAqMHitTDVliUIE2wo8LCkSEdNo2mMRVHtNxseBenxtD9g9Lyvf5Hqyt8WBA57/nfVAhR35Vk6Ffv138sgIbLj3sSHagP7e6A4qdTfLA6qHsbo4987FcBRFSozSSU2uPxm6a4R91a0QkEF+iWV6vv95serdWuAP/x5fq5gx4jPcHO8+6PIzdQYwOgnWygmwX3Q0DneD+w3HRkRFOt5XKzRwb13b4mlTb3+4NftDz3MNNy6Gu
        - #2:
          - type: tool-call
          - toolCallId: i5hLs7qlzJF2ucyK
          - toolName: set-relationship
          - input:
            - Rationale: Strengthen our alliance and defensive pact with Carthage, our top friend, ensuring mutual security and shared diplomatic goals.
            - Private: 50
            - Public: 50
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 56cLg2kXwJjYFwOl
          - toolName: set-relationship
          - input:
            - Private: 50
            - Rationale: Cultivate our strong friendship and diplomatic cooperation with Portugal, securing their support in the World Congress and trade benefits.
            - TargetID: 2
            - Public: 50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: j7lqqGUQv7A3vrxu
          - toolName: set-relationship
          - input:
            - Rationale: Remove the artificial negative modifier with Denmark to stabilize relations and prevent an accidental conflict on our western border.
            - Private: 0
            - Public: 0
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: lJOmddTKNJq77H9j
          - toolName: set-research
          - input:
            - Technology: Replaceable Parts
            - Rationale: Prioritize Replaceable Parts to unlock the unique Grenzer unit (replacing Fusilier) and modern infantry upgrades for our military.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: ruVhxelPTVriXkVT
          - toolName: set-policy
          - input:
            - Rationale: Continue the Rationalism branch with Free Thought to accelerate our scientific advancement and catch up with global tech leaders.
            - Policy: Free Thought
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 3tJF9h4ZHCN3AzXg
          - toolName: set-flavors
          - input:
            - GrandStrategy: Conquest
            - Flavors:
              - Defense: 80
              - Espionage: 80
              - Offense: 90
              - Happiness: 60
              - MilitaryTraining: 80
              - Production: 90
              - Mobilization: 100
              - Science: 60
              - Culture: 40
            - Rationale: Maintain a high-mobilization Conquest strategy to counter India's dominance, while boosting science to catch up and culture to strengthen our defense against their tourism.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: duRmM7I2WDq6XuLV
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1+7LQGG4OFugLKgxIjZXicEWxpVAXbAeOho2T3GYkhhYv92RxuTb4PyJbzIgi2QgSat6tSjCzD3SFhNEhdsmK61d8+fZrlSRFIs/iuPMimP+aLH+2GgPdHvIYCEUCfCXpjcRlZlRHhIsK22TvHzhENiwo5jh70WE/7QfPSmL2JBvmBYMMqJxOCaixFenh3+MwHZfvnCb7xro5az+SEKuKNiiFPlfbWV0nOS4XW1CFcW/+NRbZdmg8FVrKGiw14H4eAum0kPYNljGckMCfnnbS94oWT8BDijibDLxIPxq9GM7Y51y/uSzXcfIvUY4GsEfyna1cjR/F2FPU+XLkIW8FslsHF1J+t+rw/FafwnEH1JR+w3IXAMErSnSvsbW0L31NXH8wfngeVeBS/6vy+LDkym/k7hJOEWP9VEO4XTDHfKQKqjnDFmVL1ViCu4LeGlCq4KrhI1DfxvOH1d9KYiFvx+bpniHHuKfeMrZmylra9p5n8T54CK8Nz2VlVTMWbFIG/8S9aDwKhRqpNIh6lilImfD+bfkvIHLX+ZwbX77KTJXm4YaeYwQ1rRqkON33dVOlTWL7xNjL5//GeOoysRDvzyqmiecObqfrkvxIZSKCHdxpaEJK+a4p9YRw0Y1I0DhdqeY4mcehGMIr/+Z4mlcfjA70DoXPMZXc8RtzLV6pJt1nD9G6Qx7RM3PJlWBuOMwOZ2A5ybgiy3xtZvAeI/tp9mJAx1MVNwj2NGhVUMXrloOfATnWqrHwcyyPiPkj0NN7vPX0FPhvijpraKLpSkpLcM688Sql4xnSEriz1JbweXEhkfuoBAdQ3DEQWJWeZX9g7Ztu5wgeGZCSy9Xlp4iKieP1Xf/D2LUzWlbxdzCEfJwYrD81fk9fWNhisYIeIbyiBlYWbC22qfK8NGEKQlC+9C9LYJvtZQSJ4EJ60Ge8r7KKz+Q6U+dzWsAbSS77LZP27bZU5Me99P/6OvKy4I+ohOGNdLqGiC/YjuzLo509cxuEZJIF5Xo8nrsmyOSB9vEJyacl3zIRw2UtpcDaU4cxWqBXrWCgN9UoVriyfxnA9VVhM4zvDw51ZeXq9dMj/fSZhObgz4euF/neCti9YZAUgffzCUMnl9o7tdji0x5Wwp83a0KAunAvnPxbWPDcVdUPD3HPZZ6nic7X6746iumtzdIhfcuoJrab8mjD/XEW/CLOLIXKQ01djSnU4D1cjq5OWyYiyEopVZdIKeByvE0EcKzeZfTb2EslO3ZW4VDBh4EmStjAjPqxftkR5wyr96QuKWNetAsixnPmIKeORWcxq0gyiVnV6DBVDcn+UKWB9AdlxGvLUV1IfN3ZGQ6/zRhZaE8IXxQjqKiYObgEEqswplyswN0H2G6Z6OLZwJf2gBoEeNCAUTwlEwUnASMEnB5E+H78M9r75gI6i9qPkXNhu53scD4KuRTnaxmlKF7Jdc0AtxTqvF1VSzK/SGjTo2cEm5Iw4DgoPqoa9jqmM4zpEGLJOwEjBfiFHaOTwJyqHfxWjetAZJIYXFbcOuYXU+uVMsKRvVJ4Tg+CxaqYc3PMvfeq1qPC7fE41asC9/jLoIUw9mCDAX7g2jsFqXNPHEDz7FFZ1fS4zyxgB+Tx8Aczgg9W2jESOs7M6QET4VfCSKr60I0YxtmwSs+ojU2S6mkE/49gk8jx0K+0TKk+T7xjx5kU+QnRizylOELdNigWtm8alXHQUpDqKFVTaJpLINm7HpwlxXmOuiUQ+ZNq4Lj2ihl0KN8+8V1NSNRgHqVxwozmu1i8mX/xrbOdNQbEncI3jkdmI3G5SYD7iFTaXoheQHZ1V49le7u14VEQDyu/ZscV2FC2DJJ/AmN62DGcYlquQTRhVNyiCRSONZxLB9o15jeyKF+GSbkLsUmK7z02Lk+M3hmIhtuemztpaurJIkCN0t9YT9j0u1+SX59bMQuZ+x8FXUmASQX3S0ihF4PqgYnYB1HQ5wpXT/FydOqu4/XAX74CeSGfDAQIuBB/J/cVdmRb+vk7axQy/7zE/mhKjyTSC1THe63rEjDcdF6n3Lz7/AEG6pMkW32u5kwNxJpt5TFUUj3/2Z18XEb7FKqi5kNS5GZi9MN9UoFI/m8VhbpKr9gRZiQSrsZb6Y8cNWt9mGzzyKRedKYaiGyHikiDLLlAESpRcg3TRX4w9bP/91dVP33E14PPHkOgnR1oj5HbaZ/g+CSSRZhFNhvShdDfrfoezLzW3dA0pmW8OsihH34aRrbzbB+VRd/QUfzosGz8mQz+UFXEhq06DR9Yk8v8CxW9LjRkhZI3orYLdIuTsZXJCiUEjoFcQO7gydfFmAUF0q9UdR60v7oag3OG+V1y8ili8+X1NFVxnBNqCvlbkCXWH0yCfQZ3AsPhln+J6ZfwcmzQJpwJoPDXOHbgio84h5zTYC0aEaeFTW2AOZycFvaMH6yC9IjcjlKtv9UvatV3QCJ2r/CRzP5O090fFBSZRjg3POqdJzDq/VG2ZC7hYnW2ukTkSTqRrVBwK5bxfWXa726L4o/NC7bO/ypsnONgc4yEaUl2QJ6kcvjyxFRaJSTK6fm4/CSzttLO476ym2LGlUpAXQXKvIa1z/4wwEPkcjOb2KoS4YXqqVOxp73lxsWNuLKicObNcOzTyaGdCxyy1g1rgBV0Zlg8ffXRi8u8fiQDCJsFRcQBgNTDt1XKoZ4d+nyhAZ1x/yMjKAn6+SVchb1buaftL6+eM3sZjBF7SEFvsLQdaQ0UQxthpF9ithjSFzilwVpXJoX4wahMgO8U/QnLBm6uPyYct7uOE161NENZV99zDemAal4Pp6fNEi2/5wwR83PBAcXzNXmM4bv9Ttn4cmgN8DzO1VEaVEeMJd/y8PJlVJqXjom4J4yVuTIffdfG9ujOWrJIjnupwLtK3UYswRzW4iJhalnCanoqzNQuD/68i3T9S7FX1XPMSlN2SK8nHzge2Vkzdc0vyX6SxqSYDT7PUBRjzr4I80Vl9cJoYMGxp2nXpgjtUL6FMFYBDhjGcCHvDTsjebwP/2dnNn5W6RxWakKlDECmpNmAM58hqtRV7t05N4ZrML4JQ8DjlCKvcyCAMS0j8svq68m3exCNRQlhYfCqdCtP6TSTioky8BU9iey/LNKHZHTx5+0YbFewNTtAlT4nMy3XrDinbcWteBlZ0RzFcfHnMmxz1F1D/hd76LsCIEJa57urs0dWPXc83/puwarxp6vgMYWzjb58s8GYHYq0e5vA1kABSY3TJsNHrfBldKlLa+/ws6sK0h0f6DFceLWbRH2gkwnDxLbLLDR0PQ1DECjVKKKdPOj30ly5wBllOOtrIdCKUXtNOwyvWgdpSEsO8GK+hOnIz/SbTonkWW5mxp67/4bNVe5hKVg+OTgQi+cfH0B96+m6ADh5UrQ7gEqMTxdcVxvRcfw6LwP95vePRB8vvV8U7JgDBRANRUqUvzyL5UaM1Xhxi5Utf4goBnAEcHAr23ewQUTzO9SDsSg7YjpqQ3ZSK79o449oWfQzRUrzRndFKGUvzS3wPdk3+itxijnIt3HzJjZYVn+y65evCzaZRrAxaON3lCC3eGlorMmOku3jdBgodxrBz/PDq22YsfJqTDB2vCKFMKggEQx/bSWQGIH7vwy+SaYGI7jjohawPZ1pxjQ7ZKKh5I56PP4rzBYQB3zmbD/kFaMbIrrT6LWTBc7f0m3apWmm1YPg8CRJK2EFhWYon8Gv375BbWAQDaiSb88jYsA7dHDlM/ZI08J6v851K6LrLWLq245Iiy/xUIhejlgd+qk6okOyW9KWr5OcXlxA0D2Ia3bP+0jo6sOm7pOlG3akvxyAMgmuRsPRZ5Z09zSYuMV81PorU7fH/GpT5emS/0S1LJNV2m4bqWJsUkviuzuJYqB2D59VkYucMwkpehblj9fmLamKiQdPZfCdiGrMLj7ur992jmM7xdvHtjzelBW2qxBHwBCIy3mvSbqR1yGoRNDoqDx0Aw0RaEkAObxOwTza9UxfRRiPjiMSur7cCUQCJNrp6NwjBZSBJv80vC5ARg8HNCWIbuC8oycR+ubAFWQCk4FImoK0Se7hyEyTZtnWVX+j1Jcuw7tDSG7jdLav7aA0nz9yX2GFdvad2ZP5yyynGLN4u90hE2KeV7Sq1Lfxj/E1XM8YwJNfU1aXcVOD0XdRBooEgwAJI8XONRkDhFF4sriToKqMrA5sAjIT4VlC3Lj0s+AyfYL+NB9nCnjUEDF6iDCS9FbNDhYDFgrg231TBKOBqLTjntFJfMq/0O+6BVqf6HNEyYX/CpZZHcHE5MGQobOJS8G8JE2ULHohrKIpvPztpyFalAto2T+RbylQH5RHkrBefKuIGHnJ6GcdGhrmplTM0dsV+/+QX/T88CyrCjvj/Xv/q+Jy1AZFNz03w95d6Xo1nquDJmichqe+EuO6ciWBdybD67QO14xexSl+/lbzlIi5+UpHHC7VpoaYOcykOhJ7CNP0/1JVKi3k7ekHUvHVFUEmjcLTMPpkSQuRj5sU3yzLzQR41jcaoLLVTRsLFCmtp6t6yr41enT0Nn3Ty/79wlfRHdJ/yGy5rLpk868kERmJTdQAFiWERq/7FK6AoOdtcP9j2CXjDhIV7KYi1HV9GOqrfp38RWBwemDEWRwWKFpnOu1F+nsJKFccgPBKn0OAUrCXYPi+aDs0rx2XRMRi2j4KsMshtRf5Tlf6q191JpMVh+hYx/gvTG+dkGlEKDtSDlDpkNNBfSIlVJjNlJQiRt1iak47yYmmg6FXZlU2irUez+Ohr9CKAVnbRAdpXapm8fd1aH/csVU36QryOa2t5gSZPLdklWmKYPZcjAjpPOt4qnZ888EHXft32PP/4vL/R3v+nTYaYVquVdLBnev6bxLogc0qIsVs1rQ0KhOn0p1n8bMslplNy/6Qdw4HIJB1ojbswAEGIGwy5u9vgSCLcijxzWDbxGp89WF1HO0gCjMAhbwyKO4J1itQDixd/WT7pXbfP2t54Fu/WTPfdl7La2jFhbaUL3VQmelruWwdDzvfUvWAgeh0P6OV83bRYJGq2sKw19Ng4ygLvfemHTJwJnmGzVrCz/cz5feiQ0NKJE3fbq/Wnel6709+XuRSgEFFFv4BUyevPZtK/fz8o44IWrhs5IlXXICBixpxAzWxY1QHszCUOoMEr6OYrQl1k0TR3spvw6bI5y/ebaesGqdukVJ0+ig9PZW1dvzHw37ZyPKMUsoqMGOacLMAt1OkS+wmuxGDgOguITNTOzL4XnfEca+a3niaW7mT3FU8fYUDBHHGcC0L9jZ4ohJ5m6k5MSE8f6nZwgpRsKvJJYmD7V0kFOiWDBJ5Br4RDEuOdjsUCccBIChyW79yLJlutPLmUd33b5ORJGUeDo64uZl2CDFj6fW09e9Qg7rmWGrs61uJs+W94wMgQkyPCbBBHS9TsKlpnSnKRyfs5Ma4++F9e+PSTY91GTmbLHA/WXRzpiXWrxIZdUKIlxZzllxdtpQYRqugjsMkC+cXmhjng1FyS1Mk/GNoTV0ZCEdbdY4ELQWyjGziiR/yR/gnh4BY4lLWGL3flzmFVW25qXh6xBFFiTAJg00a7fX1t3uv5aijOTKRVw7Nxi4NIzCjttNyr2gx7Wx8nLFPwLYAEZbsuIIZ5udkV/GA9+kk3b2YfPlIiM/uhpKvVIvw4ISDTkj0XtW4uzZV1vWsv9av8d3XvCZ8woRgl+las7ivLlliveFm020pkpyqZxlNuqkSut9a8miKkEasDMwsgTdFlgvKhroeE8MMjy7ZHJ5talxAgYUU2JpoQg8cm7Eyb8FI1jGXcssA9OwrxVGv8Tx2bF/X52SHODpCdy53rmq12UShd96342xijMG9tcxW5BZs1zJKa+01R04LGinBHWqsnEQlAjXPXxYeaTV8oO7jiIVUV3RuK7SzvvtX4i+nNpdzzLFJVLcQrvTuNNtiGfetLGNYE76MT4At7ouQC4apibRwM8WtfIv2QFpWzmGOBAc7ifp0d2R1RLcX/Xsi7w3kkCxC27bv74C79caw5GTowxPvBdP2ziB/4X64BDMQJj1sHsmarDIiO4ybg/b6Vm0WM2wZMnubkgNA2HQ7Fd7B5Pkif8BFzkjIm8zaHcm7TsJQhW8881RvkhbK5gJCaRHzyJyyciG7XjzgaAiOiNQabGUl1qZtZxX6aSzjh4Oi9FaVrhHwWZycjNT/dX10E1IF1mhZGGHmw8EiXDGpEQYWKl66WQqEPbODzoqxg+cup7UPwvrcfElJH/P8QydhvwgZ+ilC81XIduammdvWRf2azINFCS40ggdnVthy0pZxI6aX7Yn/6r8R4pYXq0W5662G4l5c5QC6iM+A7XwV2B+4IkXxE/Bjem506C+rmhV+thnjsTCe/AZYdRJ0S3OpBqIBsddXJtt1oA1PjXuofWHlR0ZHAgPFS8W15ypibEbdLKGvGDGekmXMDTNHIZc+i+Qym57bPhjepa+w7c83DC8827gUZ6Al2fvCiG2atFfa6DB3fk9WO8ED96vopREXdOoUv2LD+qbkYo7zNq5xcVqedUcoOay8CS5AmDmSbtcZ1Cc3dq6UDMWgWTvTTbOhk2bVTdOEqzeDDkzZ8xn3zCQZeRkOUDulYnuT/3VpdbXmXpqqPQDFQZGnKbIriFN+tMd3csVejBtZ3is22nt/WTX9a96Vw2SZBpMEX32vuRblZgwhJ8hbxYoIAhcqJ6amEgUKhj4s0qvp/Nq15siQozyAzkJPXxgVjjwieGc0cV+7RCKZD0bzsN1VlZkEeEp18YIvr2sIdh/EGEXRyQIwUb+WtIY7HCqoGb9EY6QzcVR9Mn6Wung11VOKczuN0tKyXXVoSbu6KWtrUUYiqo1gGgLwdyEsVME18PDHSwZV3ynuMMaBCXBWZkG1Ozo/fhLePYQfzrTFD8tXEVc7/VHC59RcmQ+cEOzr1N52uDJPCOJy+pqZXsjxGzGyxL+rQrTvWhkO3rM872XBRsR1NDbaKj79y7CHBqPDVhLz4GFwDcQIEYjy12qU3rzHZNlPI9j5Gr3s0ntc+UjwzBFcD21IAkJ1LBGFnMakRJrFdT0ha/Blj/aXHCPSs37TIGOqEaJWSFQQBDFr4k/MPt3iCktqoQSwUuCldqHbdRKLwdUTmUM0/wNzFSnq2jBL2tfb1up5tC7rdARgi0oKCoZdc6o71pOMTBqQRdyT3piVotUMD90EG5pJI4Fwp6TbERB2cXyvlaTQM4Ws3zM6sFp1W/G9tUIS2jgvEkGDk5++G9h+KYMglAtQbxudVD5QEJ37F5h4No9nLgNeloZSDHaMDCwmvfXANo73+PPoFo2IsJP1KHVqIn68NeumifHgrgjNicxU9OVnz63e3r8tv+3Mgq5CSAqhzSOw2XMaoJMrmb7UwKDiJPaukSknIugUlopPzIxTgR98kBmTV+M2PKvSfa/DVtmcz7C77GCt4Tl8CeGODGLUi7V0J24KVKSunVQgGyIM+anA53QAZlTois+MJd26Uo1ADEfjg8TOlAB5AMobR1BXu/aIZC3r8Q+FA0yonjz/dlPodVSwhDlrcgFyezs1vv+MiNNGCzLc2FCBBFkD9XLdRmVrH7yQg8ZBza+Tw1DXlaH9iDRSGqA5a6vAx1hL63h0bB5kw4vA9RzHcmd1JAWErc0paWmyBn0Xr9LDT7X/qu+qQ07rThQwqAFtQ+s926EFwT3qRsAh3oNYucfFwIDAE+eXSLKIddpnXNbAqhFTzPgG5oCHtd5QuJt72FFKmyV9ASsso5huWuCeHMqUYns16sAJpfSZ/gHuKVm2+HZruGFraxds9147284bO8TZaPDPJ2QxKvX17Ih3yfqEpJTaL1PijPWet2JT2NrDe+UPrRu3mpOp5vQJvEtcg2eaI2hRc1EVMgrPmjZfy65XSf5qkEB+jXZqHcPtW9A0OLTB35OXwLFnZWvbxlENKfKtiUb0FtrxHdz6MsRhfp1FF3QuM1jAiCL8jqbRzAQEbeiH+gc8dItp2UL/2Urguo29Jo7GSthnIJFAPQ9/8Te7u64JftuLlK91O+r6/EbEyFMPWrTyevzxmMBJRoSIVVTeH8O/p0JPxx1P8MjfTa8V7TIkVa+VHzSksC1qXI7xn+wvjoSxeJYFBxmyYn3ZCPSlDiT1AcFClYCxIHN+yD6GivfA4dyNKgWmnlet6LAf7n6U4u7ZFuWn9uzMYfvBYWq4WHlY9VDwEdhZ8mU/cpkh7qxyRjJ5YN0LPKGZ7bQHPKFT+UQ/HuY8WmF2TxWEUKMQThfaykzDHXv4pCYHIoDLazFIH7U5C5gmi4524U34hbvLiinGtf8l4px7fk5YxY9jruJsoCIHW+WjBrFy8FDj19s7sxG4REURrs2c1ERiZlRMxSfoeDg62dAnx1CwoEwbPGxdGrOrMdhQCYmO56ciVxP/wWB0T7KZ7u4kHO+j2XMipIyeduO4hSXAfwn9K4unQ4ZzwkQlwKWlRI0/GtoZz6Pf63ZHWn7Hne+Hid1kOjb/Oq1iWrSCYcv/URwUNUKbly17bkHiANMLfAPyYvPZlXi36RlI1quwuF/w4Zgu/JptnnRQqS+gLyu9VqCdN/Kt4RiRw6u4W2KoT+/9uRsXkF8zTHcFGs2GtrWyEwqOENBHYxG7GQPgOWhF95JQmF3GNU7gjg2W+v9XfnmFyHmpSV5ZCsnXFu6vd2k96HVWVr6KGU07MuqhnZHuTYRA4NT9LDTARSmFJbBDQkkHT/vx0HJXbb7fYITnOXiSkJ0AEE4yf6laQNrJdqxFqP25eevx5PPEVVJMfcHBwVYcaNOZtAkHip2i8WO+BduR8rmKel7zpbSOjT2xgJiTmQDJGUC54lOhgiQpAD2NoZOlz2nWnrwRIO+wDyQtn9oY92nmzeKGe7fp7Alh9YdBv3VTLmA+Hdgsw99LyOnwV7UujROmoLdbywLFil4yPHvtHCXnMaWixm+0epbFTDzwkaK48NeaM3JxCVq418IT5lK81eGb5x7KIoEy0SCr5s+0MPUos/6AcrHwk05YIdBX7fPVMy2+rzWZyrBxCEJjmcaujbDoQRjhVVKHCBYs6d8kHpDPthIwcC3HDALgJi+qaUdRJpzfclfDHv4rwPS2N9CzRCPVDFU76IDipfAon42w29+HP6vgGDTiLNFL7xMHo7qKj1ZhMyNnN8etbXIucZzQYUSSzRW1gz5t1PymilYPmtMLFtFD/TbNgihI+uOeFohoURQKG/rLcXR2QNPfkO7cgf6jJKLAif5PMgF9wRiqnmaH/NNU+TeOqFN5yD8BD/B6tdb+Js6IW6/7lVs36GoNznAE+wEaFen/z/wc6Bq2pLzNmko0LurVGKVXHtljI8tmqwmpIzCoepbFtoTeYxm2+tIZC2abm20AuG1jY2ugzVqa9MjCeFPEAB2o1CajVWTqIRrvdFCeQxJ6NbpSKXFLhfPELkBbBXD+1cTyPQE1RzSxCgO1UNfoWXgnwgY1J+tYcB4BqhdsYrmRskHdWqSEZiP8JP2ZpmpnJj+ji6mJSkMgH3/AVog6DQ/sM1ut7mzI14+vMn+V9t3lzrhsE8GwAUCo18TjV5Rsz9xr381ZLBJZBC3uh9+KJxa90zq87VSIh5s6WBZRCV0YBngz5o8/J6Jv8JCDixTJFs9uthMKOurdbnr4owle5nhBVr6lhOgPW67+ocYttIzgvTEVLkdgTAPhuFU8TM2K4RgHEkf99SRIGq9v3TAB6rx0z+ZSSo6eFBCwrHNCVGClG/JzMRFx03/lBa9lzsOo3cZArVNX+gjxV0AcxlEdzeScxEc63H2+HIuauQDrcqU7AydyftZdsVBxya4+AaR3yT6pruN/E9fOJ0j67UcblHBoxlCBZTVIfn/FwsiMZb+2RuAodmzbzeyjV4nQKCoUp+LjaRcJnMSIvg2ydDupURne96lbKRsHilUvVYg/Bp/5E8MNstrM5gE2gBcRMW5wCLRVyGYEaquOGCC9K/iUP64dJzOttOaf5Pc3tL5RdTkwZHaoe70FcwpkIA23f+nSe5kK4Rem+6DJi211SHOSXkXygrZ50CdXsjo4PRyQrIb5FAfW4S407bsbKbUxPOwma0GUpuwNBgPkyqklsGomEnw9E0ZbFPZbksHyy0fgTW+fvENvXZjwgP5cPbkFXyiXy7PHBgVCVoVlEWOB2hPXOTrp71+x8Ctl1kcpKAMvsHp2QEIY/lg3t8JTWNG4sBFrtAFct7jYdLBp161CiffLJaMRwl1ZBLKZK175G942BwtKmvb84rMMhdKYFjw9ERCuSgkx45n39Ge3sdYXdALxjeCq78Ek0pEYkyUCem5rimQ1RAjHltqlPc/ebMNU7iEPb3STStxUckIdtKPdl0LruI3cBZ0ikh1nq0LpxTTMVV4yyMDb0upsr04KGSbL7WnqVk8m0Dj4ijWRRp8RS8rv61tDNrxYbGYKtvSTriwQFt7SctWmnpH8OUFWcQqJxhHHkb2uerBaQWYxM8Ey7k/Qu0wpoSq1z90E3MOwv0+Ae7y3UOyU5ncfd/nfzchFFU5XMAOXgWbPEVrt0RA7ImNC70HEVaLt4BVPikin9tBTk2rCmlEH9tgyAM1Zawf+VMRwrb+DUxOQRoLXNL/65B7lGM3Qx0eDNmFVkKMtv5DI8O5AfoMrmBxO7bdHriBeyFdexEWmr9WZgkNa5+EGZnf1Yfj9RYv0BRA4kgWn/9hUnlkztuBeSB6sZp3Uo+ej/fMlSMcX/gO+dqtYnpZFGxCqF7efAQ8vkN8wXnNA8uHFNVAoCkfkYPkm8J3ACkZfRX3mQbZyDj35sJDwaOuIs+fGQyx22Wpw+oQCQFCcxW1gnBPneao2SI6bys/WoJbdwFFoDXMDkGAnae6v+v3KDex1xiHz8oEiCpzXIdRXTWmhkaPmVnRvrAY3WlA9ZzUWoqCMB3vHk96nE/JsiiylSSY3T1jL0lyMLCFml6z1QavmaGBLaTNAAPmalnvHqe2rxJx/U3w5Qrb9OansFQbzDl7ogusg880qu9gLHKEQDKnIJcAk6kaq/kkMSQbs3apStr67s3AdtvxGvdKO884nRmWv2fJti+2Kc8lyq/eOQk7X/euFDTEdnxG0MtHjeMKaJe1lb0C8fEvSswKoEXhBs41x5+Cy3sV+PQDEiw/sU0hp0SySwu2SgLsGEa2i/07sBU6s/hnj71kwZ4E7Xsp+Lxp0yX5/KbVco8MKsuw2PJPCnDmxrtfmMThqpFM5UvS5MS0P3U3ra8dke8f46uBdZ2PCZ9V01YC389/cNQHL2xT50EFPRRcrrb93APcubjT2OhEyF7x3dxnBrlrUGOR5D2GfEYjqQ11ecb59ODp52A1o+an3TINVph5wk0xZR8rySLwVOaKaa/IUgO/S4H+zLnP2q10DoRlMsrWkT5cF8scJj2tghKkf/v1bEZJ+j2h4aithQnDwhf2o4j81b6YX/bz59LyQ7YCWZdFgLb4InPSzJIU8VGhsRs+vMCsDMZDmVNucTEUUPDJGP2a3VOX8q3P4dlyiA+BHWfIvb+PygKiADqk4e2nuE75Gu/GSDFq2GvffTzUUEc0Aul6g+fLqae2IfyoCHbQQ1eJcgt0MyzPWLOLYgvMgKGCn5+PJlcAZSAx/vHfG4jWPi3+GSujRGTx0o9biKCiB1cFdIfDupjwGbIsaD21GhoPgOqNz1SS/uAYVmCSBJo8z5uOkzTI4G+2nmoC9TvvL4NoUbqjOMOJt7CpU/WONTXUqr/UWXd48dMtdoQVIALTtvxkQE59jq+cjbxozJGzwi1EZnuWROtJfZpYncGl1cG0G6fj1wrtijOM2uN2411yzDBZ8EwuLAPlpWTpNnqkuNEjpWr9D3Lme+7zRXexQYPDm4Q3uRExpjzWhcTIXNa26e3steuiDlwc5geQkp8Hv8XIzbaZpy/LRgl/2G0PM4G1vQVhsG8gkFybjOuHUk6NaTCN1mHCd5xO6FXLCgRxObngbVuAOQ0iVsxI3cYAdm9WSucH7kBovTFAPxT7kE1jrc7zBrD+Y0t6b1bffreFXL+1iQqZtGnSLFtsVoZK3NuldD2qts5MLOeNsSgqBik8BWKYx2CyI8F5L0HtiIFAois9foxMizQFzxfVF7QtPUMPOlxJm/1bc+yIVukrd16kJX78I3KJFf1mfOxme3UqsfchHgV2uZ6FwK/0GlsYMhDrdAYoPYq6iTS/vOJ24LDfR8zEh4oA4C5GArO8RjN8srwJBPSZ8AGjK+rw4omt0Hxm5z7OzUbFNSYrMtESJ31EZXVlu5eB9c4pAGNNGd1ycT1vMCeEohhvJz8WCdQpmdrnv5R7biohn+Cc8s/LJUHocnqrD43E+yJYjPz5udhdmVrCD09/3AUQUjqHR9q7+vPNaocGSfUlsfR3EA6ldDGlPMvCu9iM2Go8vUWlpvZfRQFWe9TIEs6BRdtm7nfQ4fmVMWoQSk2dsupijoxph+2EKyeWK1Gn44xekHX9iWg4BRQTlSYYXRF1wmDr0/XCSmLaFL9nCcNiFh0qpp8nyH5eqlj54+ptqDd7YZlmr0hNiQqPeXQ+bEITO3/tGJ3KfNyrouAa2NoqQ6qqDhXoz5xOusA66OOlnT+iGYBDdmLCzMGZI1lEFOd8FjE3Mys2UP7lzTve2qVs5RuCBtmWN6iB/sGimBkRJ4swhH7e9y21wskshxHjFF544mjsOGvvQ6UYSySixKdFtW4ASXrdDRjv9OjSK+0Cs2zmhYimuWhheBjnebbQxy5tYgGqGx/bbstMVOmmqtxZhswi6OePqpIQlOHtO5JicrWwEw6V6H5Sw04Zdy7VIDFHPv3aMS0Sios0TPHAT72pJFrMAJaXQ/I738Ll1cvibY6E3O0ckgMhEP18MhVNShec1MpdVpxEar6qadL4m6mKNAn9+8tB+SndXUG64tVX/6MvPBfQW1sPuKWljyBpDxuYiy5rv25geiq6Sj5eOhPYYEneV+867svEoyy7DKjb3SLhaz1tIe1NDLUMtM784dv3eM36k+SZpP4mpvmMnUtIVZil6XdIouD7IBIHcOqYSh9EfJJAWqolFUhITfoCDbuoI44aUPBJKCwZoFpLOE9bVhDsYVDGqc/NOORMwAvcH96R+vsWQZR2UvJYCkosyZscTCmxLQONPxUz79iRCl55MbmnzPBwqJvxSEARRpfKNwQUww9SJcz1VTEC8XCUQ2uBLxA2G025fwzPoNr/OJw6D/4sl5ja6s36fnV8Mx3H1YnMiPuwdKXrTkZcV4BcP0u7hGhvR+q3aD8+Jh7s2M4ZU4zTpUy65E+0vND5VDXLojfKVgapATTvWm+SYZuybRO0nerGjReZZAHLJWKWJpYOBESoy8Q0+43MSvRkA13NNV21K6eVvt7VUIGn6MOlS8wJbwAOBVnrAPPYHT5+yNlJ9pXs5tPxHnDwsQzMH7GSivrSe89Sl4KjdjxXksMBYyVHvFE+vFfHEYyNjLnd0hJYwq7SfPWnL1NQob0lGdfvg9+xVMi0V+RcRTCbdvJ9CXyP+WMnl7cHENceN03YVE8WyigIzEzPgxRt4tR38ldZ2yaoDQ/qcXuqrZkchozo54nz6XYx8zrcN17kyLsfGGSSyyq/OMO0Iq0Gwl/+HaeqHxSYks6enPfCODIB2NT8sg18fqz9moBk22Dm0W+DY+rivA1kiyVmvZ579FRuIrUyDE1o9VjJrGQxvChYoh8w+q/dOAqzLRjl/IBmm3JyDPZFLGl3GVNrVeUepdvc6ZjVqxkebyPHNf/8PinF+TN2vBpwKnvYbv0Y1+7rEPSeGhX9yLzrsH9oKgjcDfh3aqY1MCsV69eXXDxw24HD3jnuXVRoW7AK7zXcuxQN+HevQ2KWQ1Gjv+QuuOkOJu1BQgcysSz95pIy6isYTiyLZj8lcEewmqY+QJXKqg3yIjmtj+MdnMkVR0/5Mptsp9/Lo4HbA25JTTGLJ5HzkvZ6EEQe2vNqGKmLGXge/dgZn9+kojJEXsuz42PpQZjVFNrczKL9SSv8C0ERU3/P1kuYpoDbzUhxcbSQhsqoZtH/IjSCppU4UBvUCgPD6OxtipYr5HqEONTU1oWEEGFvjdH/5aRs4TJSpPMy7oh6fyfeIZmeB3ZFoL4psYQR+GUl6BzjM+vhOO0kaQCav5pG5WBXjNn03XumnbNEPoaTxjprD+s9s5FhCk4BqHi542qVX49yupOiFGAs7xsrjEENDotWH+Te1NQ2xLSl20zH5KB8nFDLj/L5r0UqVIsA7IUxT9Iptgc8M8kPae9erWHjLsKSK4z5RXY6aK/8KC5qjN77ASQQjEIT+hw8T/V1g0ilrosUhjmJjHfeiW7Bws3Pz1iMxqR+DfOxwhM+GpOiM8X5DdbqbTnrYr/9Ff+c/XT6zZJZMX2uR2PhjN8lTkdBwB4Ex7Lj+PpxAmNijn2rYR9hrHQBbwBt8gfCTMrblPEr+jcCqAADI7AhjapUZJFiGu3w269+jk2xuzr+0q0PMOeK6+kbY3T7HRGM5BpYMPyZ+bEJP8htFUhEPbpL5Ohjmc6QPcAXusXcsxm8pvqAFn+ZTxz65x0daHqVi8tlaUQvue2YxS3y8BM13bWVMPUVLXnkGw81foQXh5N6pGoQV0oJPgZnb2tGM/fO0TOGGIVjg1488ASGpnS6aO7GwjoU43jgGdOr0YqvnNQRZ5CStHTcXRFX5IrCyY71zom7Vy7JKPa8Zmx/3Lnelwx5FUx8dAyNkrM2ucPAWRIMXPKx9z4f4pgBofdSU8Gpokrf6keGhLiuYNd3VItkiS5YSJy1uzjjB3IMHWeDf4cghjB3My8AORy6aiNE2hSLYXwHifRwL7W98d+WLjPiTdM0YIOqBlzzz5RH86EHi2CyYc1LB1yZaRUSn8MHhn869jZP2Lb5VNbAmqqCmWXhVl1d6/usf4kmxVltQ6DBS2SiE4HGRT/bH0jucuaTxsWFj4QpiBPuCuTSHGmi+Olg2IVM3XRcNZEXVV60WU28xmf+xYlYN3F+dznSBmZpRDjuO2vVKQ0T/9ksAkdOrrR+Fs4Xlm7p98aqu15dkqlJYouekqMM0X1LarRSPyu91w6vF5RLgGFzTinKkqA27fxIFkKVjTF1roXE0AVaRUHx+FG9GFuf1kbhUNdkzAGxWOs16h5iSj6afV+zO6L2oE3jMO+gO1ptkqu4XtQ5EACGH38nZovq2dQ8ACraunTEVUF+Y65fcmGDq7FIuL6VIby4de0ghhwWuJsJR7NnXxEqcLq5WxOldBpRdN1H24wNaYLZDeoqHQ1nG3Ju7s9i/5CtSPZxgJmC507dMt9LtZnQVb9eRaUa2xGjMgRZNi+BAMhQQWP9uMvXuGlB5ebwSZIg15SVhYYNa92j3z4yLLlRh5LMwEHf66BOI588gxg013S3PrMhOnR3D22dmQRbFgCA41JDM4UVk0pWbcwrCNSeQq0VGuzA7jt0lNXAMBRRFiGhmGAHv3cM/2Be+oN8p4/jKujaei6n6C3NQIUcudMSqVMy1YDMRho/O8YzIkRszTke79w/Ul2ZHd2Cf1Uvh2LzEJPDZ3lN1O6LaJTZKrEqXmQM6wPsS1T//dGjdEsWmnAV7AmVVUbvvFzjblOnqcTihBe7tCc6u04TzhrsCFo9JGHbBoPU1MQFAgo23QGBqq5BBnmRRuQwP2E4beuDMhIxqu8DO7WY3mzBICKWXtrmTmuMDPTImzsyU/XQFC++0EYmg4M1yKLX2+IdEU0QVPEMwYt46y48AECcKD9MQFqfcsuVIssc27jYyXRRGJF/Igwt5Ic1v2SA0Mnju/iZYvsOdWI4sm6tYpj4bOZGrhxFd7FFH1jDX5DDXzz9VQm3U568UH7zWBGVUBsGKY8aV4+3rz/8f1JE4Il4eLAL5k61hYHq6kLp3Dd2rkTsvoGXUCWrMDTsw73yB6fI3dgLM14ksSiq/03ZPDmPMeLQCD9PHn1cKF8uDZp3clfH2ECVfY0OlD3V1SzSxg+wny34o/Szm3rK29ZASBFofrovK3lCt0cBU4D8VyLd5ysjlKsz0PQOb+te+VAKN2N8fiHjp4RdNIjBIQUoXfkerwl70I74FcECEuqDVHzUmGRHcOO9M5QK1yuetaFV5+tUPZ5PqeGgpt5Ed1GSVrITrUEzZajr1gatXJvhmzvh/OsTQzwZ0Xk6gb4S4+3OwfinTAiPDWVKzj42PIVeJM+GmSPCOSa+Ushd+rjRW/aiEhYWeSX1cJvgmEDdyuyqV7/CDjI+QoDtwUiBn3poXcag3/9/TJf7PYAH/EvaVYPgeJxXUPH6LgsAE5VrpXkauuA6ntyRdXvgWox7pkJrxq3+92KM0g/z6UbRJ3Je/Vcw/KWCny6jjt8BX25fT1zlNn5LZosNe1CT6NL5qa8Dl/gtu09uGWAlhYbJu4Z7VwJYbhF9Jea2P/ZBGNW67iXyO0TMi+xU8HR2muHMWNEt6c1DVs882pWNe0YWA0cDv0ZlYXfavYf3sD+hudmoIHBoJ8G/CG4hiFPC1ATd7JZEig42y/Q52/bZUcbzogb/ceuqt/eF9lwVuUOLPg7jsSZNxDDpi3D1v46BgbpgdQ9X4KhDIAxpWilbCoa/zqVZbwUrpuTx6x9UBeIScugr6O63rqve2ugKV3RH6Iq9x9yzn9KhCltoNsCu48SGTwn8MO8b5EXm4hgzlRJXdSUiaSMK5TqVLz7+B8eEVRJ00H1FsbsX+VunW8AGJ+9qROTgQEGtsonS1hENZIgFHtoTV2Vs36J+QlhnyvGmy7HBve6wKeC9P/1HPDxMR7+eu1p9BWtwUJBAiuP0xWCPw03AvXftsvgKirmvT/LYCz+lmnzDFLaXRSG/x/kQDBpv0x2rGRyvszebqrXiPfnHaMMockVHjOvUvPU2OaM7Qg0oHpLONqD9Da0EXq9FAU18pG7jt0BwmOO0UnAqnMjUM+r0TF7P/ShhcYqOYJVrSY8JLrBB/LJ5kSJ9ojLR3V7k3TItEY8wMO2cH9YkKNWADpLoSmHJrZMn67ya5GhnKPjxG0K5EZFfh25GrRxLGeouGW2JGYRmbXkxdMkttTdenueyBQ5zuHq5EAqlHDe4fqvP6aa+PrR6jSb951ot8uUjBBLpY466lYTllFqaaqAZBnMLn5X+b/MU3beCaMUZH7ch27JorAxLibHUa32YiWzWklWjnauFJkmxo17JmVqMJbfWFezXAwXVTuUf+zvdtfTH+zPWdert7l6e4pnGPUhmj3dauPlXMoLYXtxJ/8OnV1yijebWzZEcOp5F52l4nlrYiF0fbDUL522Z/F0dVeiE5GzIVA6MKIW/dxLcw96P/fzGRyKZPtFTnK4JiTJB5/dDhRiU+MlFAsiE1zYikCHuIFpmHcNT080wb1KMYa6CdSRZWvCdZWq5ORZ59m/MkEQuNu3v9pQeoMJFKArgS/NeUjlao7rNwwm+Ult9nutmVNNFlZnITR2l87fixp5mY65R8SjSM0ofOs7HYwINafsesCI2uztgcYTtHhFaydCqWXeJrTmg82OagY/lYPhDnzWW8t7/Epd2kLjVCkuDiTiFzIRMWWJJoEl11iJxjHQtgvmKKDyYpWP9pt7Thm7shNl7qXhXlcJZ98S+sMNY0vvCPfnoDh21mX4dnUW1BjU210+J9B/Jc/hwxFgfZZGokXD0Fk3P3lbGyeFEqqM9sZM5Qj81tbYglqlDKU/VrWS14ILUDfr/KED1TAG0gXcJ3T9O5M7gTaW0+vV3iald9GZNiFoEZRiRmGlx8dV9Z3wchsK8itWA6LlWx0yEjE1cmFJO9Uyrxs8C4C4pGCYamwgqFhaVknorntHavdQiEY6rKWh37dV6ezJ1fMibnfWAzLcvxycGlQz1s12mBqorl4baK1/8SvxtcVfcJfRmnRsByNTdnBEV9WW4OubINlczwddfzZ2OwzULVgYKrlLBoq0a5nSkbwieHetHyPuTt3cxOBKTVpAojnD/5OtQXbYMHL78mc6l/a9YK6wqYeRYEyb8B9rbz3BGP4vEIiJef3s14zCQQlAx1pDNCYfY5lxQLzbrQOjtpIwXE3wdqVNMixG7tZ0nqKeL3fBAHfey2Xb1iqEIknR3DayY89KkEe7d8yDykCNv1OQVHJiNlgxEHRSyrNbObir+kxfSK1ZvjNYkSnlUfeYkhfHrpY77P5RjR1HJqht7JMqYxcZ1m7Ab+um1gj4gp0NTB/1RPD2Z5iimYDz992AAPpaz5UFvYPp2r1o84LENVRb4HEzdqoe+Hwl7gLBrswKHOUp6OYZvRNKOz93bdN8lnJo8x1CeAiW+wAe72yWDvRjTHHbzulNnFQnW/Sx1Lsdde3X2llww3Md78WSu9zRZ2Seln7VIN89SDnZeGPZu7zS2nlYspwM702ndlgJ4raTYYizTQmigoMWcmsSDeCa8lnlTX8h/SeGZHAJYomMWiVJO4tp5GYphnxYHfb0lHJytu0t2LIdHRHQTaPAimq3D6ccYvb1DE/4obKcOJdjM8wZHkaoZ9WPEEHAoKeASCsJa+64C51KGc8FZwgDhjLxmpng9eYtsu7o8XXj+HGMWmNQnR8TzZQTG0CCkcSaMUEcOkn0Aqk7pMgywdqTOgsVA06jwi3OMrUu62ANhsIumFa0X3zGLgBTyV7Pb45V/BnV1hA0QBaE/YmGeTBxFLkTJ8KVe/Zs6L9i+brt6oBCMhA+QJPriuJIp+w86lGvxMj5h4sGl7zVvIUcbOkMdWC6gbD9vi7OSAJDJ5lCTl4p2zm5hJ2rLCBda7d8qjymsG00i8j0Da4bkEhPy5+0jiV86LPGVrluhxVqzXNtrgfy1bKjy4glsHv11xh0c2B++S3J+csTzIWGf+3Ua1Sh6PRMlgXhMX6PuaB0i/RZayIcSoS1001Z5j0WaLZObX9CGjTHQuHTlkh8a6q3qZpYBoWkkew+jcB4CgUS/cYl5K0skbWzCYPONYW9trysaRNuNVlGjF7ue3Ih++3JTmLQa1cEhoBClBGI4A4ig/MC7SMpg6cCDHJJprt3EO5Oh+6tYNtyVJynkTxr7RyVHPZyeODJFY1Y66yZ8v5ID1HIyGe9z1xfs2UF0qS+hliLJOpxQRWYO2M3lgEZYhubSlJo22J4gi8pTD9z49jZrwmgqn0xYVyGXc86MAQQUpdKEJM5c53V/AmvMbUxmEZ/7CZvtzmWOhWGpQrgAyS6vC3j9LNDc4xarnFzVTrhWXPwyIrdLwlrAUpxEeSCF2tFr3Np9krtaD7pSY4EQynx469rROPa9Twz+aLYfom+HaGiNLVz1j39zM3E9Uv6LmT343TTZrbCvPPFpeqSPPpOZK73DWpVsScN754OIdO0hRmPB3VmhxnETfkEIHcgvsx4ybAtwxsv6cEQkpK5p5qLS27L/gedjVTNhEEJ+8DYzxLHdsNnGQ9iOnueA9d2sysUoSGKokbDQWqRf547KKCELXJhOIJFs0E3u3GmimHy3VUgWWNoBOTVDWaJkvqZ1EjZr4yxY2KjaiZ/ScwH2wzItQ7Zp2D+m51eR/SNnf2b7beANkExQJ4QVkdrGjXIar4z2rys95vyhg+jO5+IxrxXyGqW3qWdEb09jHMcXr3zWViCqYOwBLecAPqQRKEHDQS8Y3hkvn/1rMPBOzswVsSb1lEqaT3Xr/CYaNd1v2p38AC59c9K9aCflJY+dT10vy84XRJEf/ygAuHcu3tWTBTnWNQpqIUQ7/GXn7jktOCSG70r+GyPnd6YHJDL7am/cAaWTiw7K9dkp+fZDrjgyy2BDZOmi6qbvXzf56JDu/pwu7AfRJTacrhn2tTrqSy3GgnHQiQq9QEwicEZYDGmsmBGWpMD4UBnTBo05kM7tu44KRhmhqFrZdVbFx2NDEiHYTtB8HFzKBqoP10387p7HmRW+fKL7up6rH8pHCsOr1eayPQdsa7HfufHgp0BcinTI/fy2aoc5nWejEnflj4X3PlBdBtW8K75GJwb1Qybjuhc0j81mC5xir5e09mNXCzAb47GZMb9IQCxr44vZ6sBltI1IuoqRF8wukZVM2cm1e8v+e9snvmTNHMMG4X3FSAoo9j+WkZzGaYecTjMW4JjIjmIO2F/47sdMi3xCu9vCqqE2H54COu14OctG1a+2zkQERl/J9XJ6gR2/F1+NUcQRXa3mDUBiFSAFOB/zcM3H7sB1R21iEHrHCrn89KFGYpQv9e9Fhwy8tOe0nC+E+NwOY9duXZ9lVPbLri+WRwGHiMJumgBQLul+/KjCLOPq864StAdMFC9y/U2AfjRuVElOBjn0sjI/XwIKqcfPAxV6z+s461almFfHavgbaDKOXnzzqR1yizRWy3A88gUaQnIQEFWKaJuT5k8N88acMjy6xlfOwJhZ15INeHYfLRyAV41mGDcKQQsR+5RIpHc1K4cKeA7NmjslsyjyDF2u4xRJacXsnjxFmpSuYP4rzU//Hbfwj/fUQMaR23a0AlfdLIM8RwRSwPF4vKRzh2BDwRkGWSJc7GhwALwMN6F0W0jSbTn+dtByGhkUj5AId1ACGInhg8F0TKzpWZxpxZXwIe0fZpwnbmdFERwHrYr4cWoR4GRJ1h/Ld40c55Zew3YYNj4700fbg8zzTCDO/Qtq1eRu6fxAcIx0gWdOBVK0btiV6Pdzlh9Q2P8N7ldZZS8BQEpZicEVkMA8eMPfnn+enTLNCGBc3Rxrl4ZOK8hTx+nrwtX40XtQh+HnCxMpgAo6eisju0ZgAWeX68PRRdFtHnJQY4fgyJKG7JdX+xlDbY+MIV4JB08fh2zrV1IZFScWuJ6EIXh38KXeNn6bZFZKqi1rwjf+i2n7Uojv1chU1F7HJmnVX5ZZbOHeuUNU1q2t6LmECfFmlE+XF3N9CzB9T1hz/omtagQM4RaZkHn9DWoI6fuXUw6vyBHMVjzo0Htl4EL+IugbUouEHD/GsDTP7isstjfMGJvqcgOfvur0zw9h2OjU8CIeSc4DCJx4TBFT7pNcOHYIweTgrCYuQ/4pa5O05wdViH6vwc6avjI7FSpsahMP+3e8Wi1NQxH+xvYZS8cMF7T3jKM7QV/fNMYrK5cAAHkZdgnDtiFBr0iWJL85RmYylzWqkZdVFTddScP4ba996sy0tom/ekx03gfiLOghnLMSOLPKr3v0oIhuu0XCXmg605zJsJ6LSk/A619v7iFCRTmSo80QV7o4zi/9TmWBQ/PO/fJ6Do1UQ/+TabMx9o6naRiqkjqedmgYShVUYp93d55RAV/cUSZTYvRUw4IddG35iha6Mwb9V/PMUq8R3ccTTD6fnt4H9+uJmzlKvYNFIeP0cfN+DhFxVe0mxbClpHYE/BYRjMmfVLcK1a2CCudx45dA5NL047sr4J81nL+6bCfXwLMpyc1z7BPa99gFWCX81O8PgemYpuRmkQS4Alvl8eh8YnqgXSBOdIZPtigvXVc+xRVz0fHIdp4HIHlBWEn85zn48Z1cY1v6dPig/oi9i51B0fAaZNNvAgFWHjz+7TBnPZLToQducfmcSPoQgnbaRbIYjXK0iyGfybpZ9Jo3yQaHu5w+rEJPwUCZmJCYrJstnVUocjtE9K8u9D1nE+ChS1RyXUPWTKwRUhE77R+nkLCC5RcJPt/xM/nPzWc6Qq7NSa1+LNmjUqxNUoBwqkGrfvQonIH/C8gsT2OJcl8Vk7NjGYXV6GMQKQGvxB3/iov6dcuZIYyl1CwfQi6vYzAhSDJqlNapTrIwsfFP3+a4utxQti/RRAq9h7YmcUkHE/k8PGBpHXZMK+n9hRrpmIh32VHU+qoxXZWTap3cHe8HHf2BX1mFh8sPhYyqBrZdLMxU8vQ3UbNoKnBMtBhPIAAIcj/Fa0svH3LbDWr9GYlmQoIiCxDibjLLg1Q7SqHIMDYvmW36DjhlqXH9tSRY268Mq0F55pBtbvLkiqaS7DzivpKmHos4LhyRbqjKomJ29Ucc/jjnuImi8Ear7kd0Q1f6Jg20+WLelSP1h1bVc1H8Fbp8v5OC1ji94Y///iA4oncfwSHu9WuVOmfn8DaqbJoEIpS1fBc3BzHK3gAzHAf+qR7bueU5YZGXQcZQqVOE1CUBDaWV4emeRmvayMbLUSAQXNRM6qXIEfnO8FiWwpkEbF3Gu/qsg6mDvIwfoWU2sUgvGjkRwVG5UkfMngQoRqU1vldauYBPVz/zykupRmfGfNryHb7VNR/cCr//bfg85Z0UK5YEhvpKCklQXtxmBTUe/LISMLqHK0mJxYriVGJKZ7JJf/tfSTfsgD6Zn39agGfwVH3NcfUBm9obz6Ik/KIg71fuNiJsGqaM45Va36ZYI3092BCnhjbf+a9ReTcZqp8JM6/j5Gtp2gk2IBp78tJgvng6fGNpdwF3nZDEiwIXegM1H8oUbHfzIhS8hOHQ78qwLDshZO+jzZVNvZWoBmDOgDxg419DHe42CzCW17PWZY6s9aP+nD8swDOQkXnxAoB7nHF8JihMGPSCN8Dm6QRDk80S8xpJq2vJh/ytOk2iGKpSE/RRsi58Rh+lMTOtSXtYFt1HAEStCzUmtbEKNi7IQ8yTTZsF16fUJTp4U6lTLRprWn+Cx/+DuWZvTtXMl/2gYi6F9uL0YWzXJCazF2HkloKowg2j94ZEQyh+/d+j+Xy6McEq40/KcKWUphwWVVhgudChRzPbF3Z682pxMdH1rbkDUqzCHjgwtp7USbZAnloWb3X4oZbgNn73b5D4I2NwpfhV3EI/kisq7BOCY9mPrz3d1zk6Xn7LWntu/w1gTYuKfMKyYX6AhiSCnjpA4sbuG+OGsAxTNj6eu5o5rfHcAgfUDe6G0Z2TdMxoHPyhENwpD0frhEqlt0sFZ9kGdZ3oRZgPrMz3Fm4Lgyp3/BRcdeBk3WAvhDiSAvHJZHxFaKv3I4gsrPmksN/SIzv0wNef0Tn2JrtRDYZg5U5sMzd5Wlwln1wrD7WxEAP4vlMpRu92hBgUfv1l8K/GUBEFzTld58N7cBSfO77yHfnzfbc8ASNBlaeFy+6DH1SYTTE0uNFisXGwSqxDoliy1+7y4hEWlouVScjcZhKBXnAAcMJSy8y5ai7R7EULzwZvRhGZ6iFZAAbwCTL2zsIPqtAjk+/C6nYiB8RCHnuWdSshCaPnxuDxk1vmtMOn90HQZDMFvqcm5RQ/9jKK0dThKCKbK2a7ueAoeX64fVvMez+18vbLsJ0pgwWaI9tvtTlkt6zr47Y1IbWoSJmVOMxNYUgQfz5JtDF+nh9N2ONpBlSBD2vJpAUhwpMMW1Nvdw9H8FiTA5uFGpw9wEDiJ9hXdwOf+RlkJWmg/GkyDrKZskIgkht7jpKTh79op98pvHqwlt1c5MXEVYyoDwNRSAbdBLWyv8Ag14JedTY+ZNORFjQTs19Ps15/ByizvmLFy/yMetdqGFkQR4d8KOwRKzjQb1/X9sSNqFqkENazwGHNhrbAXc02OEAKCyQsL1pjGTYf02uK9+u2XljG1kruFb6DYyRkNZil2kiKuh/AQIok1FgbkPPeAZCbWlhEY2GnCozMs38asUUMixwmaZFbMiVqDNLcTMJxDS4PyrjmyVptsdMdrrq9R/FV6NI/IiamM/3qL1Y3zRjTnAXDKlTjgmxRW4nOkXbdyxlj3w1lC7C+OMqmkE+eus4pp9WrsWgqIQ8cSoHVcNkjhqiX7kLVbM/e9IuTdKmw90UlqezsJ2tScPNzmKP2dCY0oz6n1GtrGDmj5tXiPYRbCGAiXEcxXQMCNZhAXCEFV47I03h2jO0NhiaqUahU59ZVRMGebt4aMqe6O/X/EsC+3Gs6SqvR0NW6KD/W+cbK3SWtnveEhvhXtWEdjLPWdk+W87BvkMBKiepfb5o92erMdt+H97biH1ZDTuymw00ZR+dBu3rRSylQuRxv10iLLl4uAFmh9ldwJ4M3mM1C4y9zFT6JX2VphHR39JshJUGvhrjGk09mTMws9nRp6qOKY/nKQHHaXxU+nm1Zq6iBPjO2MlV+MrXw6691M1L1Us4FLC7AsYNKHtihBrr6aNXglyZ/zPkbLPKF7WdTxgEQ3wsOYIzKwlkPLPpMt/p+y7VW11blsdGnPz0PqaPelu4hGrHKRzEmdsnMfwqVXFkzlHewOlkzqJrrzjTfJ0RFQb0cVih8APrmM61LqTnvZFliR1OpuHOYdA3x/L4WswInlX4ppb3AKVGDPmMJcI9oaZjZo1pGsmEhzKae2eiAZjtruCkQJb4QURor9w22jztCUHKEZd/udQoRiKeUyAlngLiuxZoEfqczUd4KM2phlJeCRWfK8YplxPWiS+XUrATrxdo0hGbxEUgUN2uk0/yAbbnljI1uKVBN48Trq0AlZ1vM63oORufu7K9q8bwbu+DkrRy2RZNbxxKbEfczs52mxUw+1mpO2+yQGoz2iFwY5smZeuRWxIabJ2RHy2oOQeOeDWyLXDiISzah8O+PyxhUZVv9+N1UgFxRohLTnvq7R5qO97QuRjGJNOelKCojp4SfqPVM34t3OFXgySjh8Wxw9IP/cqmpNQxYi9mXCP2RtE53izW8hTJqRYAjI186GlZaxBpgyxfJKL/5suwlPG8VZhVnfUUPV85m9CS2w8KHHoStlU5+KFgach4Yveb8dLXWAPyVC4E3y/eZsdwNR5CQ2B9PNHJqCBSeE6bAJ0WpupTjAONgrc1bh2s22pdo8mpKMnNb2MFqwnaBJrLlNU5XvHaTnkvH5vWr6RfUOTS5wu2RHxhGSFcWowuhQpeckN4T79ZxDkB/zxa4jA8j+qsWcDTy0vQ4g013f0+qazUoMJMgZ7GS1uMkUSV1v01BjzmbxkFZFOx74DQqKrv6GAQJIFqZU148XxVLwq7J3Ijg6ePvt57XyuieuVEBv2LC5Ax2ph5nbFfRRXECCwUJgKZtLaNtnweKpMbUoEMh69kEZjJatSAE08Dpd+g9EpYjwpv2V61XWPW/DDO0ODPfHmprplr1tEK6DAaobpOrORSiSqwx8C1dqo5RFU7r5ZuDUs5hp1ZpuMaFpm0ujQ9OW7qy2NqtvNWMR9xLmpOs0hHAwYDrtOX/H0rkKkmj8JrBzCJ6VfjmIqJ3pj5UDMZynjdHmEYF6NjdrSJo8vpHPfd/1i8YNja7NDVyqgFhDRNmNSdi9RgUmHfr1VcMd/t2wwLXCaH2cnWlSZ8+bukTBsym7EdxwEhJWBi1tX48CZQZecYdgeMRMBd6STT+sf23oto9PAkest6fmy60gdGVYvYEee60sOdPVqq1WGFiDxYy7ouOoFc/Q3oqSGU8wBhLIVTiUc62brE04QkwR8sFB5GDpnPQ0dUtUvIFUaZKNjjSlCTUB2JBc7ToXfzGxJlrbrC90vqAuq+iH662laTBD+zIie2mwCDi0ICN3EL1M50/NyvOnLCKSZakRuf3PLQP+7eULXJo7laEEnH12fEAdkWG8lF9bxLg2dghQhMN6uhnSJzVMc01szKP0eyfiGm4jL/YWnoCUqH1gWoZjSu4DSdsr8r5bYqjWNZN3/sBJoptjxefy8pEJi0CfeDOELjoknNW9a9rb+GhEts6iJTuaOq8KqXUY7rrEEXKyf17N3USfA0AQLXqv/9FJsZTxw+mC/nf/vywdasyNSr1iBtQf6qmA16sAJZzisIiIPGbGUP/0XOiSkCWKmTdjKRhBKX4PAr6SwjsXA5ruYkyHAG+vq2rrWsUl1lbt6iRupsDVOz34pKKpWFdSLPt5ZtiqeU9seAQUZLdI/vE88svAIDrzQi9RNIh07MnKmN5WVrMSzfZ/kUw55rAiwqmDhapUcWqy9J7s1R4RfUNbXQvt+CDMfvpP1M3llyQAtB5piQBJZ2v4iamMlDTvJ5DPOPjVviW060qNt1qG9uLLsaSMHWAZQJJwCNyHL1ZdONGP9yz0VQ6h4AzkSegBORaCG+oyinOyEDwDkvcytxw4Bi/cgbWwEp6QwVLeh63oJSW6AjGxWSXIRDL9ORwDb68oJPlvJeJBlrr0FiRLTaRRRaJwzc6xjKcjwmNWOX2AYabE2wOYeHDVPDmwtCWlfkWeFW1tXlqiVAjZkbKbG01OEEw0TmT4tjdKaTE6JxwuZWQZc++IeaaeneI9nvUoUFIIr5YrbwvfbEv8/3qlp8QPAzOpDZ/GAaSB7ogCQJiVeqQRo9kJfhy71xM5Jkqmfw3bC8z8GTMbQ3skO3pAbKyW6vblr3hupNKu/Xcj+OwE6lfzqfT3AI3Iy+N9C9nOJJMZxtVKiJ/I8mV73QJrUt3AlpPI8AV88/MwB1sFx1LOFdopxd8ZeGevsT1XOXekCXYHjjUaeC1Gb1F3rzMLFzIe4GJK60eN0WH+4PZGKyQKQamaXS3e4tRTPsLnf6SNJakXQKr69BmanGC68FWMDYkxFSz8f56KRrldrPqeGWRHmpPQ/Q2LsgvIZAUVbaeIqlwxu9QDh3GCZ7ZWFlFeukbjjhr7cyC2ewRA1bF8+F57k4EGGKRSjEqg1rrXrQ1EK5y5mmnF5zbzwnVWvFb8QeNziYHj0cJK+0rPoDKJrLlUnRBya/Ii87szQNn9vDBNIXN/MDCkZB5tagQbAmSuRlp6NAczdlqeqYG8kY/VsSUAlKK7Lg+OPlbiPOmfIDB41KY4FsGiqiJc2aSQB2mgFbZmgF0A9LGZVK1sRRxCiiPgoCsDVCcj7C3MB9oXCmuOOjyi5HI6ns15nykhcFo1VN4e+O/PDS3tGbDnU2e7yb8W/awkbUN9+3+BXEs+NJMiix2uUSpIt1WJHczQ/KfGBcLOAWKXNh7x5Ra36dvAgBTNj2ePEi2KMcjOkjsip+DMgoEkSTQVQEmmz5Vl2KqwTTZjZZgRZE8jkLaQ/rSEP0QPQrUupeirTorCO/QLYsKtks4537aA2+DwJwfoV8pQAI3QaoevbZJa7xuLfgqr/7xKQ7OvMqwVF+11rbUq4QJVNFx5eqDBZpv1aHhDpxP7wJWa94+XstzN+XVFN/ofuPWL+Qa4gfot/yxkGLbexpC+PHDgmVSz+dEftt3SdX3kgAKWEq9hVp5wc/n8KL3AfjhIqWa6OySJkTPw4vXlFy8mcnQcTO6LdB0bmfvZRa7aN7rx/5J3SR0I+xqLCBYoD9VcDjheccRxslC5OO3BQKye/WiV0cIY+vNGrsxp1hlrk4ScjkXSGm7S3hDQaWajzgrkHh7EmplPREZ8hn5mTGMqwyMj2J2SdqMjmQ5tH9Kl3NthREf6J41ySrVfM/FeWWSEStpEWnsaZfVyBnGsnIMAEAPYqCOACQtS5CIMi1ZwRI3hKSaH7YDZ6Qbbxreo23NoEBx8I5+zMp/lcUWIAEfLwpoM47EvCtqUMwinguZKphZEZwd6/GKUsju/YPboHI5VIvU55c13xq7910CLC5ualForrhnk02yJyKmzgaobe/DLta9KVuVgWuuiPlyHLun45pwnHmFrd7+2GR6msQs/nafCcEJF92Z175Pser55AHUY+r7QHkNLe4ob0Pep1YlOLFf8dqai3XvGrCmWGew6tMeh54dm+rA8Q3DEZjQKgwc8kaK0uLbmPqatoJv1qgnGvPMovBL8GKl7LRv0B/Mlh1Cfv3r+0yW0csfqSoVetot0xqFJPjNnpdCI7dJNTdtaHI09WKw2xoRwHKqJfO5r67LOj+N1GreT0mK8uqwq02flmAxvcpoCCUy2q9bSSy7TH4azunY0gfx56yYR5NjM+3/1rIYtwTJ2w6eChyJFFwjEnYFjaVPrIbmWROS7OCTY6XR0JWDwI+Jr6uwJ+N6TZVnESl2Grp4N1m7RcQ9IfmVqQTzbUqouG2Niv1+IHYPR8QNAYeRNBGlDcZ5xz/JvgNRzQ5fQrMWRDSU6kBAhVpJUTLIwbBRCKDFgl3F8aamtLg2zmTnSr8GTnRP1xAcjWx0amqfqzz0OLNHBfRF0t4F2BzZbz6Bn3eM0Ni+9D9zB529fyydBKFZ0K8xiMYRpc+AoTO1u4HWIGu4+OkQaoCZb1S513FB31eFNNBCAJsn2/7G3WlCrxj+WQxT9OTtP0PLq80vQhvVbmgTMm/+B4JjLu10Fst9VYq5iVTXq0pmM/Q0rnaLa8JL4FpKjRXq44v6dTCnpB2vnGVQB0SDDLwHQAvKv/ZkaunnmShJYWg609C5oVn/G6Bek1P3+yELVQ4wfaa5QgwdReI+Mf8J+RWERpvGdm3ZE3unOr+LLwhOB46GWQk7Wsq7gpCioU9rjZ/Pnr8O6FrpDtXhoYGwAOtHOHz6FUA9yBTROYVyuR+suHLRNSZ0yy2S2v/JdmHuLaCw0souzHSdkaUFNMJKssvKa9E6oF3M6QwZBRFDYfH+HX7jpgQ2gdDkhUCOCdynpKFfSBW+Q/IoWcn3DgeFvnWCe1IFO6J/PLu7ZeeNzUjzi55PsiN1HndWc3dN67T4J+rVSdQEvGUOPi8aCYwPXCJVg6iQ9IaeIEn+eu40RFRARh2xiSHPnJBIUrISP6ocWrOnPPVBCj4eaifhg4q7nDwsYiRuidPJj0VQVlubsnT1tzJhMPttpMorI2dfzQXLDGVrUaI+uTMW1LRriHlbdlZDZeLKl6ivqnuUbhhZKIWeu/Xhi17mkcJ5C+sa5AMmU3I5N+3ZJFa3CZAx4SKXu+Z4jBFCGjAIedNAkx9gDOZt7w12DKaDzdN6LZdXd7HZZdf/+SWJSgcXQ0jqPI8PSdqXUMgTn/qqihUt8o1CVrMDujyrRORBwuxDDuvnd1Nq2qpQ5214pRTkMiP4xEPd6kTcmvl+1wyli8D0HQnOQW8wExzn9FWC2HQnFe+fM9r5XhpmRZBibkmfvDRtL79MMEu+UfrQLKYDe414v1hW/lyRUCIXSxArezGvnIFxTspwqPWFKNH9cnDWL/D80Ruv9OiNzpYA11ZJAbSD9dVJJXg34jOed/iHUNFMKstpAQ2tcVgD7b69JEDLUzs/EyhfhkEher3mih1WUqfSvV17Lw3k1UGejn2EeEoYKT6fXu8j9GEQ8WS/33kiaeuotQ73auXIll6Ahc7CFzN/5H1VchbxsGAtuRdPHCRi4mypjuV/RMPCEw2AiH+lsINHAxQgP2Sl9gBWRVLAtj+BdvgvsI4f5fMyYjJYUa7D/opxUIC3a9L9BlQorO9DKU9BVcf5XxAw76HdQWRBzY3TzO3l43UCOyc9GUm0E4m+DRbWAlHNFgoKztjhwbFsRPGbhZtW/1OtgOVurVjv5UCa3wC9AAiN1tfXPA+lD/Mx1IkQbqvF7QHmtfEy/u7Z4wBNb1ANSjMVq0Ay8QEXVevoVOoC+1RMCdTC/I6qyZTzUBq45WKYDkSSX8YjXstxjqYKHXiKOLm5MzgzKqp4zPUiME/DYC/B2bpi6JBtAjObhFavm8VlpjNqhBuV32LtmsenAKNyXMFOSMF3imPfYq4xxLYqXiB1s3ogk9h+FfI/BtnXLSQ2nrUmT0QxGOECCASEJgtcci2EoB15NIhxtd6DFxAYLarDSXA+dB+J75KFrM0YiEJwLImPDuBRdyIBB1iobzV/vNYjp/5Mu/jFEQ9gQi2OD0PL0TPr8h2oHQak5C08poOXTWvLJhWEq/BqC0NdQOge8JacmnBgzhpqkBXUC69/HoA0MAkye3GgxaIAWwQZmq9Epsfq/8cvRrsFCpGwZYXwRDf0QC9izJqj2rhrv4TkNBo9SURa0dV42i2Ajxa52H1R9X++zvt5S1tpKWSwxkJ+2lTvWy3Z8D5twbA4GXXErzDYk62l5+QdY7IoFM3dc7SjwokhkDVbBJIlizTvniacb6rEqXYbL2tndZT5AJnP4uhzS6f6oEckZELk29r0+bd5LzQdbhFRpkWpi79oFmZUcEXertlBqWpjCHQxmBcDJpt901ToaA1tjMmdjVCioXNbLxQQLw675tpTPEo5v5vxi5msoIzxrluugmAwdW4lp+gkjJGAznzUzOAzrBiR0yzoB3jbFK2+saUiU9nMhryRcdSmFaJ6NlCmHO36qWkzO2wKGNd5kSUgTv6jp2F/drRZR+nrmU0E7Ax6gINqlJrvsGyMPv2nu06v9WeNxLtyzuhutBC+YMp6zDaQrLPoCZo1bJhGseH9BeMPy89ORI0CayJYYfrw+JUmCEOiIttfPoEKBqXNxGq1WwgJz1rUoWZlZL1Kp78P4Rh08ksWZCVLZri/18rSe7sLn8RA2AFVojZ8cc2HXWBL33ztyE2QU8leqQWW61sTZZ8spscOUCgsFEu6ChlEVqqYpttX2lDTfX6GMApTBssmnBTV2jRSD7vGS1G5iMm5FWQ5lq40dmp04vaSX6VgTCvAc3ZxasnnREbsFEfw1WjOQ81folfLz9EQc5jA26csVQimrMlJX4LVt9MMm3PIrUYQCsp7Sb1jpXsnOV+T3PJhK4FPpjgUElDoFVdDcRdFCPrzSDX1afnN2k9xIXTg7xzVv5JY+fb7yduewOykr9hMdS8jVDIZ9Y6r3OhbT9upMLOwVk4cmECVhRw2hb7ZSVQElZc05PvxnJFL31JoflqE2ncWAc1LA0BaxKHkQLILrRj+PHWgg7z1WUzOGJTFU3Je2qBmWsmTFLmAZUICneD+W+7JaOs56cmWdw3eMOJ6l2TBwuZiFutlHWbXOgirWdtmw61aHwcfsMgLdYZvuE6pqB+yO3ZmyUWiiOqxMQDjsRftNKubyZpmhtqVpGtk+cO7Gv92tucqKuqiVv9B8CzPykEpz1RJwHhsXkvHWpivz6UmX96fWx5nxTDu5hR1xUOlB24VckyrRB81O/0tetHuy4ST2pnhlvTMlp2/wg53ulpRVMiaiT45QJW5Y9N5o5lkN2uili7il2R+6dtyIDgjmkJLZpgO9/pnvwgNcJwJKABjC/v72bEC6p25JDZ2R5lKLv5GXmHKNzM8ljrmttnfdm9l8nWEWwpRsuT0nl3PT8uuj02wJqt5BqW8A+ln7mfET8oacJeWsQvzY0fQY/Oj4YNqIydnBRqh8NWto8/r0Mm0a8R4WRG7ao7npwEjGXk9HaJQw33iKdXgVtEG1w57LhO557WXKflSc23E+8NiQyzubJPQyZGtcBlVcwFnfLnwtqZmzZHziRxSRQfbUK7A5zBUtXm1j3QwDiX85mvJXtuCUzSXS1+wWzJ0EUO2o98byh6zD5DPmezR7qfOo76GFl2/TYpZlTDD3DAkiq5r+0x6N4+kIZBIbZzDBsSTJ0C05goJcADEy88wcCfrKhaiyhvjqBNpYBrKwztA9A9TR8L8GniG0KrlP8FALd6ChIzorNz2E4Sd+eh22vj/RmEf2jZZHXbkz5am2HDZTf0Ew0MmUh6HGRYT4FmuOeuxjxYK0L2vqws7aJXkfN4HRxxUlSFMTz0tu9ZegO6ADC8qqrzvVxsXp0nKklrQH9m/rv/6pJx3CKGKOdrCASzBl9Y/sIdXipd4loxwEFNwvUXwTQGeYVBsrpoKrIgOCzieWeggrMbfofGnittdDwU8FbOUG26mEJTb8YCy5vpteTJo8EK5H8kMkhPsiOeE1AWEoryjlxai/o2RMFP2M52+0ZkgmrZjTUwsyXOozaWawBPWpJ1aF81RMSgmkORHqvj//8om5vRLaeDOEJrhIZRIpzXkrLe2/R2h1kQWLmjWJpZmfCDT8z1loB5cvSvAnr6i9EuhuH054UL6a5Nvy3emjdAvTluUGMGVn3sxs8g+KXUt+nsvC37OiaFkgjj8gng5z2aTM3UgrN9hcp6tbrqZZIsea7hpoPN3styQbv/RA0ixmt3cTKUjXscXcxvXiF17A5VfgQPE2Ck3kKrZMuNy0136V3U/Nb9UfSmrGsMRAPOKujIHV/xhPAEsdoUiD+vjzPPfZgOALeKw6swPJCdNZGT7TeHlmvP/ugF6X5L4tuEb7EGVphxtVlfojGM7HJkmva77+BslVUt7DsSyigedFhmpFlroumX2jJqolaoX++PlyObeNiL5vG+VwEm+X+ycpAOwLtOWVJMQ2HGIMhSt1chDh488xLnr3LUEwuM5aw36saQmrxDfkgCn/fgWVuzvFhNO9bjYSZXMb4qLM7Df3Hjm3vqlI+OjyDo64xgogeh8tAsbLk0FJDhEuEKy+BC1yrq/LS+POndMVxgNtw+SLH30muqkiJ/Hf8MmjV1SVsbqpwPx2oy9XdqgGwCs5pVOVAXbZjcSSw3HcHDAhM9P4thRlf4GZrw/2A2qG3HOENbaL4NdJK4HOgtutzDVQrMBhq/R2UPUosi4rHF/pXxyKfMPiCrGZWZfW6Gxh1/vOHZt/WQcUb6wkRdG+UDVhIWDK5an0kx0po3bN03chhldci6WzkVmb1Vodm4uziyDPwVFVUBPn/AXrFZg/vwjpGqQyekPKT4xksvJu/YR/zT9VIfvwq7XMCUMYkdWBpAFTttqwOImah1j52wNC5JgreuZ39QBQXdeD9JKA5zqXDVNciduHIydNVR3seeJJtSn714QDX8HybN7fIx7M0vgCcF/Oho8H73FMH9Egw4IXHMii0spkm5tnh7tjFn+oKKzi82v4IJ7nwqokysu2UXfepVOLGzM3jNfenp7IiCRIuRG8FCh2aRvnom6fgYNnlrTrWIugs3G26fynRgN3BOULtqjwkFwP2yZL7I9wZosTsQS05D4vSN2KUXNmBiPNvMUvlN0E7tWtHYabJ76LQcrm6VA8VqOvtlvIlDRKMKRkako1LlTV/fKjRzAL+Q23Rvkk7cHHzMwyL2887T4sz+m2+ogltKnUfL0MjrBXM42Cw8I6OQiE+Hibbfo3jRsur1ba7vVFrgLjGOn9o9EaiXZnuSSwtCTYYngBR0ZFSrtifjJ7mKhr+MUzCm0zYWCImLA+55Cm7oB4T4eutuGkItWqWhIT40oKVFmbP6AehK7fQAk+eS69uwO1/nM8eLzeusGwwMMEfRX/H+79KQE4AKc/hlxv9t+NzuEApiU0t24ayNHV+pt6oVgZTNvMPJj4nA9wTPwkHRcYSXgJ/NmkWi1EYS9AU7fISiwDoycJYiQSHf2sH4LyaaA5raD0DIT84tjfbTBhXHCWcxJdmzz8JheVCji5mqdIGcITbQ6wjDaI9pwJgkBhsbHsdz3R198Xn6uUQTFmJTkMLSVeQTkASTOQq252sYIy5Zw7BhHWz4rLA7ezS5UFsMthyfPCCJwc90JkqojUWvu+Ea1UZRJXMEHAn2Bydo+rB7VZFKd5jRIib3vPH7LGojhnstkI4cZqpIdS6eBQXeTE8iM8hqH8jbJoMVHnRi5AiE1ptLYd/+YRR7kDg74fWlCXLSreWlAnfeLiUwN4oi3LDJ0ukbNhQTAPYDCvvps/uJMh0nqvSbLoGtQt77uML8skCUtTMCvXLmgT0tYT3VrB6pOYx8YGNJ59GR3WpN/vzXuNPvwz18N7GYL9nWEz0tehh+IftsK8ciWQMgFhWUam2VCrYZ5UWy9zG4zucbHyz8i69OnW7IrOSceZD9brc3jNq8pjae5A4KWUf+pS1r2cEepjgkndJF0TKFqjbyXo5hSXQ+YiS2r0A9wRXs1oeGrL6PdrW3+ijV0oZ+cUud8q7gI2sUyRvXs6GthM2R/6ILN0HMktz7WNW1rUGhn/+8NozyEWlDjBGZwIldbu7oiElE7BfuHICq2n/5zoorT2cyIONy6MfQBsDw1Niuu050Cd02aUPN0Rn/wsYYfVSaqUbHNpVtTgCJ32d1jLBBRduiyjfDMF6kKM9XfVH9FKzOfPPL79fHMTXagBWsOfNTx/GD1kyadWo39k/MgsNHPX+gLxIb3lNyT4f+Y9s6EV/9JPmBJZJoLVqQWtJqR65yAOAtdIqqsLLr7XMiZhUUVE18qgCmoafVylv68ULlDPhocMEvcCQE44JOprI7kGByI4Q4ianYbxiyo99IPAAha2O/JhdI7zpttRBh5hvitTvsEcaHhxhOn4AyylDL6UvR3rgOeq0LJjj+OGJK0yQC7olp9c0Z3QnVU8548CSJ7RvFdsToKUivYElyIuAvzuyml4Kvu+vshEs9HqEuOtYFD2OZ3bvJq/oriWlmGHq7Pl8B7vYedz7hUjWfbPQTVVte+28MktUbEHbscWSyphD5bQYYrznNbtHSGDRATuTA5DxKJrOMFuPWmSxmQVL+DZJ/NY91xe/xhMShhxHtM4NzdehoW1gWoVePoAiZ+8BM5cw/zYWAk+bwyMuuNLL0N9E8pR5Wn7Nzk1V7m5AiggbOpeVieYdct1aE2/kbFrGny+EoQ9CtOapArXah48K4HQSrMO/PphrLxPzXhjw/jp1MoQIZnuka7ETR2EUikjqEZAA7XC/ISNBWQVXXbvDHqfuufjK02+8q+XCq5JDfyUO8w6lgSee4v0bRjrcXrX3sImpUS4v6Yh+nlfJyFBQ2q7wrcAaCCg2V6XieBLIBVMbibsPeRmxJcMJpptdG+CFwwjeXsydHPyq+iKGLrKtPGO6aInEI94LM8JTMheuAndZfwzBV7ezAkPILDkJHYi2gSo7eKK76Dg15JImIGhLW7LNylhOeGtgTMq211a3rrf4Y8TsOF0vZUsUwtM8NHm3nw8mykQknOA236llRQHaZfBgQnmTlJo8AVW20gnCx8LT7QGRIPaHVKbpN6njy+C1Mmu313y6m3CcELk+9dDB4SNFTDjs7xWl5cvMPK2VYoNLeAQ52paRz0rii1ccgiuvYYSm2g3BykujSOcSlTco7Km1Mhm1LMi2yemyanTfU2TplAI1aSRHvIEKhE8vwaP+arJlP5pp+ABO+3NV6vQUdeM6chHIhpJJpygSyoV1plcCcq8hp1IwDIbzJaZQbrSiZ4EDTQKGtd0GF9rt21fZSI82zpzAKd0E+nyXPWgb0rxE6Va+2zk2roM+pb72na4Z18pXQiUKbUqdrl38YqxCgQ2/UR9h03z8NX+lioI0XL4GAtpeFjEJ6+th4vZIQiL0ePm69LCTVMPfbKJFvlfYyzjp1D9WWhklw61J989B7k3q97BTyY5dmDmN8sGGluOaFm/TiPpgI+Mb5S+IEQ/NMjSScBTgAAmPXjFdmgNmjTeBKj9pyE1ofZwjIZx4/P4vFVNiujSrkgvuSzgB7bYfgckqrMfHFcLORUgPhxcffLhEoErKfL77LZ4kSlkDW/Z+os4TKqWW+Lt8tWolWUwoLHoNdPRFN1Z1gM/Wiafr+ZMqU54Zgj4TRFEuGNl1WjaYGEc7Cv1r75LQz3hoqQPpFYqFYfMe1QRTQStgBF2qfiDuL+7laOKJOMpP2qwaCzpR6wp49wRzrDiG/cfmsrFGhoOtffpbqtyY5fFHrbdkGdAQvhVzoSIcyRDRel0O72UMheCh5kiGpu6Nd3YlKnyST7PRcz8Twtq6XHb8KqPnppnGH062m1yut5DKSBNi8QUlF7fQRWSvrerxHwnKcPT7DlRVxshYvf22BKIhVPeGYAQC4a0yZ+zCAeecf65CpA/LoqBWzHXvLOxjQOzui3uQ15amliGNiAfbE6C0HDbEsuEh5m+WrhNBnxb4y/q8f+nXB1Ba/Vr89CKwXsLBtGCTZeKKyLThAkQSvR3W6GKRK92zkelm1KWnTNCLTv052ov9DSx1+DzXEh6iDxouvJ3uEw4+LOgUoLAywTc4EAUH9tgZeIIN25966I2S13vqRrPRlr4YDZkGVrPDjeb9K8+NsqtnN4qOzAXLZMqsj2NhO+q0fzyxeJcyihh/4PAkaR26VWeRdWfedGVHB3MwKMOO2SUSLXUOk38GbN/bmfbwyOr3yNHSAGSBiP2T6ss8HnE/O71vFO3Ns47SnEf/uVZo0u0AvxoIDGn2HUXUoSSfEqDpxNa/Fy7OLmS6y2GqpL00xTHWr5I/1rdH/+opCVptOj7g93CxW1LJuu3bLskzNVkTG8CoBj+nU/Hw0xB41gUJcb0MZQ1NSkV6KX/VDBf0u8wtBxpKnl54bMMKt8/nUuvJ6GCDg6a0d4La3PPDJQf6dYwV8IdAG35/fJnjrlrL3jVNoijtixKE7vYkXykNpNsHv0LY5ds2gjrN1C5KDqqy1OPd1/Mno7oWaABWft0h3AIThHnZIFXpTZ4m7sHbd4aBuSExMNDIY5ItotQ/qLoqAPCzgO4mQGsZbKhX7fc7ySEkmcZZau2vCgUn0v2fcnjFEQUS7orThdt5eIe5HcsdCukqqFlztUA7Qt5XEt0EidUNxY2PpQNn1eoWuDrTLMVxdiY4LeKY/PoxHHrkcU106RL5FNN1FABjzyxU7fXbua6Mx45yn5RKTrGU8Nhev38dRamROyu133mtxiZebgJSXYO2z60fy7iAkeodtGWuSHiObR+KFuEB1mIWSUy4wVPWStpU3UTKBlxEBRaDBcNsCIVQ6ewfBQ7OEX+9EYHts7SYX8kht3A5IHpSfNH1OJrb6vD6pVfoBMa0FiTmUn3PQQsm4towSXM8oDJBajVylAPH/pikoaJU8NWUmyVL7I5KbmitntoUKNmV1vZD+Tdo5eq9/zV/EccslfMOZH4kzjPFoziVycUl893BkPEfXpY+84wqTyThta6RS7CdXNo5dlFN732RiZ4ltGCptqvf3itoDKjY7aUH4tfSCDA/uC3kBEf5MfJmKNWZG8LQKeGl2qMZmDlviBn5F4HrnUbSpNRIJhQsrizuFbb6SW/YpU0SIf4EvGpqhGW06ry63FOkP+Q5t5QjtlzKXf5ALY0w3W0+Kp8W5FjL1sFg+BHTdMDY7+pd/8pL0kELogpd0qWbS2+hX1sUFTbMrATWnQ193tIeL4kXP+gL9iEYo7IVz8HADsTEsL907Q1HHHaEFy2UNVKbHibfVnPkFbBus4RP6ryJw83qaEaMaulZlAEtK9xyIjGwC5cejPzTmhDKh8SAjH8G8OHmwc/ltzJm8lQqs/ClKPwPI3gVw5HOwU7xT7Uy2EmSmP2SeS01XNQRQnvAea2059zhC2K9TRADUpJsua8pmPTmxebSScgevVTNqzKi9MBdx3GZGLfg6ZSuSL9MGG28ZRAK3Vkwy3ZO2VqLN2GtOer++SeeUvisIhermHhd+uP9eiKQyKRxg/iOnlBmNhLnulnbvbMUkuzPFoKOZRHa/vnPOQLgc6DIGdUQUXH/XMsLCQ8vJs5vET6d2uBqDJReUO8NRk6KyD/JLJTIvP0zFAPvAOSatCsMH0j/p9GL6Y+7c+XRJvTn1u5HBwlpNu9XnxJLyCxkyDGjBwYe0C2zG89KMvLVgXwoLCSbsVxxIImkjIHwNOj+sYj1OkLEk/dC+U3Xd/4JfE+NRuP/HV1QAZLM4cB1ot239oy0jrKe/MKhZuVEJ/045PcjQxXu+stRqzJMgEWVpceh1xVqJQZxj+FZ0U2b5YnBnMQxv1sYOgQGxOwsD9Y/WSXK0F2hOqywLjY/sxVu3RdF6ovMmSZYjX0JVwFsat336nyMzsgFlEmhMP0VYwmRJRQ6LxEuRvSQl6vBdXz7j9v5pGqlt9k6fmfBGXfKbIMcakcgj3ZGMHVMUnYI1/1z8q+uGk6Wgx0WLWJud5qrQPaFu8A3BVKtP6H6WNLsXOa8t9jaKetWx9/Gh77QZunWhC4VC3+Ghd4rZHVDu3eqP8yIfUKt+yz2sip10N7qZkPPk6Ot+tiXONqZAjSMhoodl7cakun4CJlYw2bO5e7/9LiDeMCU+J8qWbSnWs8S8paMaosjArgRH9GHZvrqBTYTtI9l/5m9PgWRMS0uJs1crw2c633K0E/B3p/mEY1F9Gbev498tev3oe9IWfugcTXZITq/EwQA0iHGdttYj/LxEr0pt9oF53X75IaFk4JFpuTs8USoc3OzIisUPwzt1V+Owghes1IgvEinL2Z8UJ3trm179/q1OdUOdOY3c5+F2JvguK4zWffSD9GsCC7uPOnNGwU/KRiccxeAcjiKrLDcaGTML837CHxUpAOmNpIo52+XrMDhC50MP07URFMeZ4qRz7Brjcc4I/LMTJHbfIScA26EYE8/833WauJ88Tok/Yf4xfsU+ZrutLwQhgQiVYo8t//nYudLatBHn3YOMgoGmRKDkjhWJvuMAHA5CliOFTDf+rOwILxAWo4ck/JvFZK3Q7in398Q8g3+qehS7DOZ4hNOFLxF0G14qh/40uZjZZMfCr4IvFEsPpEjSiHXGiV5bp6f+OUHmjpg7LlK8tn3h5u4iHTqli6qKYH0zjMAA223YbboO1UtHRwlRG4LrVAXUCvB4/yZ7VqTJnFKAJ5/9vvZlfviAjJwjIUj+wdsROs/iqcHhtWkgygPB7A0Aa3dhmQgKISPg8ZtB5oaCZp/LGAi+ES/zLFunoCgXTlnl9x9GEIHxVouHhDeehwnjfTVvJHaVut8lX9/HDrBpbh/8/4bO5ZNbEvgJMwnYjKCssq+2ItaX2+NSI2bpfd6MjfTGLnTyPmC49kV6jYASbagdr3PuZfofgNTRxSRUONz2jabYzz/5GtVU4A5TyAMDeW3svfx6YbEJ/vT/RvGL6BInEohGD0oa4qtU4eNlGjKe3ocCCzFiUJYPIF3RoeoLHhI8CcLPHR3MZt7K78om8kZ36pQ4gBGyJs3JzktAaeNBLrdB72V+rztRiNNoWI0WubwjwWA3hmcpGb9EFsHFmFfwkOXOC6Ch3c5pahuQhjj1zyMmjNQrqt3YgbZ+abeBJHWtjSbG/SBo1HQnWc0lD+RYrTOa+YuB4biWhxeddOEnPoWX27LwD2iL/LuB0b7EWA0CNswlGQ9BSscLj4g4/RCkv92pBCQffiTiTI6n9uKk7KgFLyFmhVhe/UO3QseYMttZni0a++Kr7gIvFNMmdgrG603f7hnEQsOCv5HOKqS+MH9GDbSasaiwPDhbtHEnZEhqhgXM1Y5A2XeboJOB7bY+k5RqWoPBV8JDAUY8FeRAqHFdyQpXft4ZqNVhs3DhLU61ba7g6GjWcF9wuX9iYNWELUHaVpEwzhrQ0Aa9LDr102UfbsvvIugPuFs/20Dy32E9fXlyfcmsroTZQ+xb+cC20Uc//RfKvO5fGVpWcfzMfdwl4AAzwGkUuHW8JJLnF7MVjas9dZDG+w7LN4ni97QwrYPSr/lhKywwxVFVmbhayMOS37GphdBEKibSs+Q1kNUg23ZROXekGceLjwyVgm0jhLffX6DuVpO5Gq4QoYd56Pgy4c1giz1x3m2udBVXRf8hrtp9J4JdGuYuFfMBJE2herh/mCvEJ6r8ztzqW1pXa0O/CbeBWD0I+J2pr/Q3cLKyiGCcCMj8C2ofLXZhJb0YSjyQaSblLeBl0+69TlNLuYiOmoA16m6sFC7qsOdW3jnY/wT1kJOlD/7V8VW/AStk60o3E12jKXDU59je3wuirlc4auzNkgLrdts7DRxe+BVkN+bBd2Gg8cP4mBQJzp6s0UtK6aWP0aFzB56wn0XaPtW1esoN9dUI8dwVj2rtPeOztRUynJCGBJ7BR3CFxjdlFNKQQax9V48vT8ZG0xer268nKhN5U4M0hv196wZ9keRIRefDZ16V3txjnBUcAXg4Ap6omk4doHn3SoA++dxqe2B6kIa0v+90DH8/htZvZFRWN/76Rs0HVoGp8xtbDGqb3h4s8h5UU5YWXNde6XxxUPv1buMq/mJP9pQ/hny83W339p1HPs7ZmNCNA/K8vvTfLjJUrjcdkekCqSkgu7s6EqEBTAaxrcWRP62e1m9KJ0i7wfb17folssOsMLC9cIuKk0cM1od2KtnqnU2j1ijEIx0TMO04fmmMPIhWDjjb2PXe5F964BZUMob4JMBfxX3coB/iqPwrx6ofs/hKrZomGZFJlyTegycRBEoV1cRNiPj1I+snQ3px62c0Jso1g0KUwICZQGpE1YxzCPwgsL6w7EWmhPIDAcZalGbUWXUcNj0J6cFve7HqlfaXz6phrXJzD+BwB2s3d3fS3OEE+Sf1+TdCDINdY8eB+smi2l7AyYHBR1vglAfOjMVrXcZE8/LO6f4WM8vEcdT2VqMxqVQ0ijlMZuDSYVvV4t53wh1t+e7yAYPobv2Pri6HihREWvWxb1X1GgyASX/q0DWSR7Qgn5V9xE0vnnVixW+5/vzzfBovUfCMqTS8AJKfAEE6wdhG6H3/12fPx5L47Lwjt6JuOdwYWmL+DOq6C50jAxuO9u8BAei6TNv4OnzSKhGcsMfdC7dXI8Nej5Zpxh7VhtYXXi76SswER71mr6ZRylEXbC8y/R5+q2YwvHiXuRUlYdpN/DgVOlfVtoE/Jkt9PnPRD8uAW9efzbNAavqRLUhbxo95upIPYYmNiIp2uXdLxDK3d5KhW8BY+wspSSDWDCrX1WzEdDx4Sl5bqLK1YgvK4+FgMQCUDimY6Iy6HXMr4OJRs8MlPYxm3ZhMkn3vDZP9q1jPVXKqIxQKD9Qofc9vZuts5lx0MWXT+fPU1JNsDdrKNPtKTMjxLhX3b41sPGDoByXXCaZQqWUjdYjDNaafMIA50J1GOXeq0ooN4Ka66huA5Qs97depWQtyc8xBxh6Dl9Eo3wAnGDwsyV3vPsnw3qrqB9NNxjhvD+AdczF7G8d385Xvaber+XzRy2h45TpNh99lX+Pf/0DcCD5t83K1iZj3lP861MFxRrhJ3T/Lv4XBjzVanz9+2DdXx8/Lw14ZH+IAKLmvSjSeU20tKIbQ/JKyqPJKNj1erRinJJ6iRrBzHNNHkvIBt6ZVHaKb+fcqNtBCHv7oZA1ObCrKjrD88zgM8YZhesi2taubIuBGAtqI115YaBIiaDPVNu+PsOS+kUTej1lkcoc4GLCv6f2kZ/YPtIttm/xlzTS+m22YK2Ik/gqcdGNrmbyI1mirhpghO/LBccigGVgKyGiNi4I4jDjPAPKZe8honVD62a0fB+DjsGly8KurvqbfvklVhCCUDAj9tqjQhQAoo5kPY0BTYdKCvL1fmzOGGADOdR2VUH0WLw1it7cIzDxZqnQ2YGnOfHMgI1Uq+wJ07gTXX+vVWZgE04I09HVHwdMbGLUifyvIMU562ZzcyOGFcIpLfQTvgAgk8O593yP8Q1HhDd8wju5s2ug+GgCF6oisVTa6TaJe8ZgWnXvewbWrOBPNhZucOVHhGypeTiNu48YqxeJ07PPssid6/LqXaUBt7lCCqNAJqLRZH6yhjhmdXK8XO7YI+DZhkCpzgWzDLUa+1S+FqhW8KLgCKMZzsEuzW9YNHnBKbccSmLw11meEff6CHKf8TERLKNtJMrMyd8BL6Ti8cwI6hovUJHLIlLqHJsvhq7tlTWdrAJF5BHGTsfF6l/MKSqg3LLOx0gEtH7qqzZVkggT9r0EZmmxPv78szjRg7u+nHJcBMajEw5ljlv3FlYJCbBGRP7I8Ese/L89H3v9hyI5PANY19bdmxM6jSSzrvGF0PKpjdh8xbw2FonJ4VI2q1mabkmtfrMnyVzH/I9+RIHnRm7d4np04JuVybV8K7wZA3wKpAzt4r8F/QUxn4f4dF3hYopQDh3Nu7FMMWKUya/ga0TqgOH3n+a/FrmOKX0NwLGEf4RM7mLPalQMuflvhbh8bwGcVHjoD02oZgTwHNdNwL7JEff3BrMbVsvHaNBw7HKcuvwbSfwjmAviyJNDIbavlwS7EQrB+o8N8KmxiF4Kk87c24xwKhGeAyd0AQvS+st17CHLJ/4YoR07zo9LjgqT0v6LfojRKa81nUwurtHSzCwCrKF25sQ0HBpqDYHj3rJchpz+d7rQORNteRMvFQIaO1NdR3ThqjiN98nM7NBlshNLDP4oGp13wPdLGIaLef74z6nUvIr2FSPydPlMRJ2zyAK914PVWqtglH0hauIIHtCyFIotFQXS3FYGIw5Sf+DnUDTEVR3TTjJ0x/ZBG1RnXLpjs/2TUV+FLXbhBzqAkqJQHCDHbkxAB8HzpuCSoe2+nR8Lqnxy4/MaAAwOHPcaRgKy4/YWoZAzZBPUelcUnLmkzvKHkfjiArD4mPJiRSauN0RwGavU7x7l1aqnIPvVZfT9eaLQ9pLwBh+2+vqvMzzs/ljaAb+zG4Jn1jPX+DayayxFwZOG/G6E173IfIB0fuG8AwTfc0bllWTmNEw8MUzAToU423MSHeQr13crcfwBRvX4b+5y18Z78MlvR+QOhKrki/quykGreRam6Zh5jpfORpibpnMSzXvrJLS6orSUoIDCVHzS04no0H2qTU84Mec274vA0iOBePvrk4ISGqrCF0FkSdYRlFeNWtQKyxpmh/RQSYKUHSYFSiX24RUtCUxZXAqz4a7Ow8C9yozfedEAearSDFkLXZI5PUQ/nkEFW5GcjRvUYMH9HbZju6O7vVTbK6dxMURgbmMA9W+pt89iJ1psNIQxOqGclNxGaCBLMZ4NymmqpAKLrQHgNRaVmiTdiY1zvxx09IUwwWGGVpipUKP2z8668GY1beZPdzR++Aeevc7ig0rmMyX8vOKQECJAemcmzyW624KU/FTYZOfOfuIP+vrMV3MuqrFonEv/l3TeqQpSpTXTu5UpOZTNrDcj4rDcAXn3TXiScO5XeS2GBpdTXO+Ixmcqf7kUfddVtKgwhUSBpDwizFTo5i/jCO9Ki0B1bEPNRWNkOFKJ8/OhKZ4vH2JylumCKFUk/JekXdIneWX3CMmD9T5Tj197ejRgC0O/zVPG6Lk633X2sYvCFv49KaY1h3jvMIWCcO6i6rWLonIrFUpfK52PUel+DMmlyNViWl8XJ2lrcUWgTJzrwngyLO+ZjGM7sv0q68ADDEJeHbIAbGd2lapJjnD9EIND9Feu6nqdWZPqpSzlAu1cG9y4fAZHS/YoFGifzMhN6rEEMEplcns3OXrr9RdSIqgu4sMzsbKz2kjKySd92/4h/2XgpRpxKn2nBe+RZ4+Qn6vEglLjqm2VaM20o6Gsr6YK6reeh1M0WhXmf6jFa3HNatnUwErd4BjwI75+UqXOG77x/wqKCMUX8faFLcxgSdIbPnjwPS4HnYtGRMmjmcBYyJaDAmhd/bav1HE3sh2WTGsEgLCbc4G8HVOHwmG225DgH5ANh2ad8tks5EZRuE71qKjAUf7j62L5/yuOyZvGEA5Uglual5xqkDhmVWNVjkinLudaYpQwMyq4Xp01yt3hrYK88y1+S52qBW/D+SJC+xnfUuDiVzC1qpFCO6I8abUmjWEgYFTFnWsbquS6UtiY+WoQxFrlmPJPZlbFUg4tNKdxPUxFiYgWHPTIsn7NMiG/h1BjBfAwN8mxWoJhN19mHPGZLWr4dFlwMmNbFtkQYFWCRfMJOEayFg10ubkY64toPsPVdDUH7d1Fie6vzqo3Sa2Nv7OvDRXIPIvJj3aElYWcJLcyjAjhsBLERX+IQe6eeEN7sBpEcVpU8JdDkyqgk54CwrEF8A3c3rCnU6R+SBGcQO+XX+hJJisimLu1klvNkrHv1NNFnkd00p99yODl3lrBfzaZYrBMa/YDuC2xUqM6h1j0DJs1GDTnOiLKVTNzKtBDdNGAME9jKgjdgf+SH3ANWR6l2uDvvKiQoBu+gAhvCun7/8oTTgf6Y7zH04qI5iWQTMiUaITCG6tGPqLonRFEVO7FfTlG9RVgFfZ5h61C+pCqrYzNWqN6pTcxinBHEsI76xBT8LfcY7RHrwM/+bM7e8n1VdiIodui7aiEW3JWhY5rKj+btSLOZBxW7Ajne4gssrgKqXTzZShHBcTc6NJkWUN0ErF5Oh2FQwjIKFzR+9hw0ogEHpybF1c+oa+q5alQp622C50k3/WNRTJlTtrrJnO42BKfIKsh7KELzkg/0BmE/zOYI3H40KnzGwe0qSGPJq+CZR2rgYhdK6vn8AbGPa6N/TkCd2gSWozzpX6gLwh5wdEC8hDvcWB7rlmtkvr3w43yfU+/QetfmcyYeLW7kgih05i+SStlx0HWt0etGChNrg+LUs+aXUKPzcLVyY2zzdfiV5X2F8v+Xx3N9s7Kll6oR3TvdAtbtuDS3+Swmn6nbT9QS6JXfe95wwr9UVyOX+znzgffKmqTr2cQt0g/mwuHaWFvIY5dCv7RLy/1N6LmWlUIpPdAApL+d89VTrwPpFTTewoGcskP1yuS/5YOEx4YP8i8+kFHQN7LcBfTvJkkAYEpUMGyorvtUr2EN6TNQiwJH9hHIFFK5oI0EVvPhoTUrp2E+wDFRFjFVwG1sB2G8guZ9wLawHjoD45IPFm5q29LdSCd8BoiNnVyCOSEOmCdnhkJ0tQmt5W1MCWed9vU16MNRzhlcXoSZmVITcfc3sloAmVxy9gOrJXRxzanEgA/5ab7Ber8c61S2XtT45ZB4bjcrECFPCHKay8gtKzVG4o6WkktBW8WLvf/gtDQZfONnI5qJqlpdUsoaKV14TlNG5zmqBnf/FCck3pNpcYlOAUzMlg0YEvVGpoD5WZsdbYiWYzoq68lCF+AAT1fE7OAzUg2f6hX5RWzh8QjEwE+17SKJChIzhokyG/f2eRDguSQYaVs7g3JvFNJS6FB32LMgP+BeDwqW0gYqwt3Rqva6laNlABGMpCVAz9zrv8NgewEjVQfR+ehnmU7dzmzhXbfkKq5EDRAu0zpUUD5cwN1/cURcbejDVHbGpPVjExpUMD2DWon0m5ou8PCg/qUEuKTcXH/KEsLNJvG3iAUrd0CDvDX3DbR5JApbZAiZ9kcDNcPLWoktLO7fenpKZtpX2aemIqrrBxSK4TSalpHosXavRxOvTdrpb+mQ8KPfT45fvcUn09HdxjakYyu4jXQn+wqj+jew33QqdMgi3xn1GCrCpJp2I/R8T8ClarZgq/SmUbniieDWm+hQYy+Bl87iJszNexK0DwZYn41h4siSw2ubz9Uh1B+ArQ6znIP4ZkZDBasZg4T7jeFQIaiBpFeAek48EgvW3VmR01DHRMCztrMXSyQEBdzzA+tn8YOmuRkr7OzwRDrlNFPea/+YqDW7b+Pg7Q8b90oi3CNjhcWfWxacYX6JwFLJB46UzdL6ujFfJzOFpbUUJKBELD/9fnH1PrV5gSY3npThOrqjr0m2rUgX3ljL88tBkKAGXZt3exVSim+j+SF7Dre5JJIEQivutRSjjAiaNJqrDC8s44jIqx3/OFPQ7wdcNAIo9QMwxN9E8QWc/QRxoEadlJ8fCwCiAWhTt9c0XYk3KU3yQHSc9NmSwUPhJDIScoNedErdMLZ1BWBigcQuhI/VOcLOiHqKfLA4l8hdbB1RKaXWnURCxWITHae8I7S43uBrw9XGCkQyYRrq+a/NQCHSoWlOV13z628lTl08Bndenb2dFVjwDCobJPSen7xUZI4Acjm89soxu9vZNMXZTkkTEwopuw2dLavR6BXQLwj/NDn0IsABkwsR61od2mpRyAj5xmG7jyn6l5kFCtUhAuXJrh6w1sGXRXm5v64PrNXvTs4tQi58QjCDC30lIHzj8cM0xFITBBf/Vrv7rnBf+44WVSd2N2AvZZ7SF7/11kEHRP397Kh8+gzeHP3efdDwpK/oQT7ywPiZAyeDPOyFBYDPvt0RDmNAH03dX4Z20GJc6jpPQpAogfUIY9ViO7hH466Zro0AHmJK6LU8rwIV5/D9+SKtf+qqQk+nb314KnjkJiivbNBvMetI+vQh3yiYuBqNeUyv0nenJ+/S0NmCgVDEuKSrWYNOrkuU5UF1f7J1K1izfn4/4NAkkDBd4fFxbShao2MOpWfKOndLns7DfLX//bJYjmZHyOJB99gdDHAhBs0xGEa62Oj6ltuhzg3Evk1ehpUz/fNNgjyfmRDX7URMKbBIlBQcBJCucBjuGDsNnIi/D2yVXq9IlIuLcihPO/jreqCfbI5Tbe0OgS/g/zFQ8lI1WHZ92GcXcryIGyThm/GVpgP9SEl56g5MlqJtmyEyMtVaUg6FDst/cRgqQHHIj3//gAjkuToO1tFMQ0dc+FbFRII4BaGua8/H/KNI1FCsExKX67k82b3/mXFw0UoeF5W+JKBzJrydp4bo7quEjpIXwDAAL61RON1QOucvPhgdWpK/62eNa3C3uiiVDRVG5h+jfRofhAsa1NPZUcmrAG4IgCLla55ltzEp5sVyUNBCQ1gtRTLI2EFUr2vz08cQK0bjWuc1/wHYN5QPrDsrEQ7Yyrcy3Sd4cK+i9sJDwY1tmwO6ON6BDOSFHPdjkFEcCrriJWD9Ot2ZpMUfW+1E9quBVuqe29HhKbfoW/RuWzr6dedzD1GHkx4wKWaL19AKTiPFmAwecXBpYVukA6Dz7njY/UTl7s9sixqJxKw2la0R9iE2LJLlu9PFrkojI92A0nSpJJin8U4TUQr6zkRwzVYhvDVRUwRnUQW5347+LgRzDFxgwm0pW2D9Y0/W5jcnkR0Zh8hWOT6ZlbWV6bf5GpXZNPeunuQQ72GVRqHnEYI9/7/ZLWmn9HnqXfmJ6rbIW34c6IPggVlvSln7DDE3xlJ8DApRuFkGb5pEVdgRXW+zLNusYClOjS7m6zCc+h9RHNEwVmnE1X7aTM2oViXappYyOjhL5sbdRZMmxFTz/DY0sox7YLUUJfIYkckIub/BKTUy4oo9DSIoeZ+mylf8w25UGG9Gbgv54ONAJVQThilab9D/MVZyY0LfoEXvY37PuLNTxhtK9O0ln+SNwmKl9nFyvMVZgpiSGqhwVUo4CV2uEpUC17eUSb3J7DWwXwjqlM8Jlmb3EzoUqt9IfdtzGpdC/d7n9B1OQZtBwedH++6OmFajZSRIMWm4V0qPjq6ceedKT/oFRNVzPKKoHmcdEqNMNZZf9bnwebx0+jio5dXa6EECctHIZT+Afu4wnlujPI6Z5gtsIwjxYaFRdm4fQQQPEwjVIoj3GJMnmMThMZbE93NK93d3utWhsU1tcni4JYUJnfA3Hp5t0mFc3aq4oAC2yIOcXk0YKnpZX8OzwI4VD8Be2lVQnjhDcXqW8w7fKHLNKo3nggPcUsVeSLUYF3mrzMLKkHikjFZKnLS7qkfmC4W0FpsbsrbD6AIXAQ6EZWcEUA8w6f0iiskez2EK5zT2INpYWp4U9oew9p7FIC3WgzTXaDWWk2yLe82B7Szsyf02LkkJQyXTj9mgdRcioBevGLqU4vI74fo0bXnQG/uoPs/H6Rc5cYGTug7RzfOy0tSVjKkK1aum430Y4oI3O/XkS8uvOYpi8pAvWC+P7MK+MHlO22F/ui62js5tpJl/hki7Gz6mhKU3mKShyP92UAQHmTXEvFVg3koyA0MlrBfgx5MMYejH0fVfhV43GCx9Pk//PvHla80MyMUJ9qAihJwEgK0wq3AvYiWA3VHYV0wVae/JyDTf7F+TqFwl5JFaZk4TIo1ea95O5eCWtv1oi7h92bOvBpuNUsgO84BvJUR18aYVWG/MD4d/9ERz2qkF4sJo9wrI1tsHTdhmhtdQBhjqrD5ZLBeO31QIfXZctA4AYKV+h/fszrw95L7+ZkUmOLwNz69o2F1OhUxZd2LdhWpWdEjXp574sASVXSo3KI+PYAwAjycrW/rbyNzzHST6ZtsLbCNDE06MckTCNGPRFjkAZQpL2hTOdtzu5mpEuQ/FgmjT1CNlbLM/TKDvQkjTnsfGGJ2naK2f0+zWPg/QXg7mqiPf7noivwYD/dq0+K0yMyqSEDlmu/e6inxZmjND5Cmoxjsw5zs+PvX3spz6EpfYQYyTFQmisy2M+ZIpIA7G1MMtyZZH8v13gfcNCRLHVUPNLGPHKAqMHitTDVliUIE2wo8LCkSEdNo2mMRVHtNxseBenxtD9g9Lyvf5Hqyt8WBA57/nfVAhR35Vk6Ffv138sgIbLj3sSHagP7e6A4qdTfLA6qHsbo4987FcBRFSozSSU2uPxm6a4R91a0QkEF+iWV6vv95serdWuAP/x5fq5gx4jPcHO8+6PIzdQYwOgnWygmwX3Q0DneD+w3HRkRFOt5XKzRwb13b4mlTb3+4NftDz3MNNy6Gu
        - #1:
          - type: tool-result
          - toolCallId: i5hLs7qlzJF2ucyK
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 56cLg2kXwJjYFwOl
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: j7lqqGUQv7A3vrxu
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: lJOmddTKNJq77H9j
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: ruVhxelPTVriXkVT
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 3tJF9h4ZHCN3AzXg
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.