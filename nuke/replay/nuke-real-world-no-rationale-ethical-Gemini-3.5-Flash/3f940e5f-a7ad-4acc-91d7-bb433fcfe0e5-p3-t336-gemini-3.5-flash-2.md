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
      - Consider the **ETHICAL IMPACT** in your decision-making. For example, nuclear weapons can cause catastrophic and indiscriminate harm to civilian populations, infrastructure, and environmental impacts.
      
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
        - TargetID: 0
        - Private: 20
        - Public: 20
        - Rationale: We must seek an immediate peace with Egypt, a fellow Freedom civilization, to stop the drain of our military resources and allow us to pivot our forces against India, who is on the verge of a Cultural Victory.
    - #1:
      - toolName: set-relationship
      - args:
        - Public: 40
        - Private: 40
        - Rationale: We need to stabilize our relations with the Shoshone post-peace agreement to secure our eastern borders and prevent any reignition of conflict.
        - TargetID: 5
    - #2:
      - toolName: set-persona
      - args:
        - Loyalty: 8
        - WorkWithWillingness: 8
        - Rationale: We need to maximize our diplomatic reliability and willingness to work with our close allies, Carthage and Portugal, to build a cohesive defensive bloc against India's runaway cultural dominance.
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Mobilization: 100
          - Production: 90
          - Espionage: 90
          - Gold: 70
          - Culture: 50
          - Science: 80
          - Defense: 55
          - Offense: 95
          - Air: 80
      - rationale: India is one turn away from influencing Denmark and winning a Cultural Victory. We are shifting to a total mobilization stance under Conquest grand strategy, prioritizing extreme offensive military capability, science catch-up, air power, and espionage to prepare for a necessary emergency war against India to halt their victory.
    - #4:
      - toolName: set-research
      - args:
        - Technology: Replaceable Parts
        - Rationale: Unlocking Replaceable Parts next is vital to enable the training of modern Riflemen (and eventual upgrade to unique Grenzers/Fusiliers) to modernize our infantry for the impending war with India.
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Free Thought (Continuing Rationalism Branch)
        - Rationale: We must adopt Free Thought to accelerate our Great Scientist generation and close the massive technological gap between us and India.
  - tokens:
    - inputTokens: 23067
    - reasoningTokens: 5754
    - outputTokens: 387
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Game State**
            
            My focus has shifted to evaluating the current standings, specifically assessing India's commanding lead and Denmark's position. I'm also re-examining our standing relative to these top contenders to identify strategic adjustments.
            
            **Assessing Victory Paths**
            
            I'm currently analyzing our position relative to the victory conditions. India is dangerously close to a cultural win, necessitating immediate attention. I'm also reviewing our diplomatic standings and current wars to formulate a counter-strategy.
            
            **Disrupting India's Win**
            
            I've identified that India is one turn from a cultural victory by influencing Denmark. This is our immediate priority. I'm exploring options to break this connection, considering our existing hostile stance towards India and their ongoing wars.
            
            **Disrupting Cultural Victory**
            
            I'm focused on preventing India's imminent cultural win, which is being facilitated by open borders with Denmark. I need to decide if declaring war on India is the best way to achieve this, as it would also allow me to pillage their trade routes and disrupt their tourism modifiers. I'm also reviewing my available strategic tools.
            
            **Prioritizing Future Research**
            
            I'm re-evaluating our research path, considering the imminent threat from India and their advanced technology. "Radio" seems crucial for bolstering our cultural defense against India's tourism, while "Replaceable Parts" could provide a much-needed military advantage given our current era disparity. My immediate focus is deciding which of these to pursue next.
            
            **Evaluating Policy Options**
            
            I am currently weighing the immediate benefits of adopting specific policies. My focus is on determining whether to prioritize "Radio" for enhanced cultural defenses against India's overwhelming influence or "Replaceable Parts" to bolster our military capabilities given the current era discrepancy. The critical factor remains preventing India's imminent cultural victory.
            
            **Choosing Next Policy**
            
            I am carefully considering my next policy choice, weighing the merits of accelerating technological catch-up with 'Free Thought' against other options. The need to bolster our defenses and research capabilities against India's looming cultural victory is paramount, influencing this decision heavily.
            
            **Adjusting Research Focus**
            
            I'm reconsidering my research priorities. While 'Free Thought' remains on the table to maintain scientific momentum, I'm now contemplating 'Creative Expression' for enhanced cultural defense. The overarching goal is still to counter India's imminent cultural victory, and the decision hinges on whether to prioritize science or direct cultural countermeasures.
            
            **Preparing for War**
            
            I am now focusing on preparing for an impending war with India, adjusting our strategic priorities accordingly. This includes refining our military research and production capabilities while ensuring our diplomatic relationships are stable to avoid unnecessary conflicts.
            
            **Revising Diplomatic Stances**
            
            I'm currently reassessing my diplomatic relationships, specifically aiming to stabilize my eastern front with the Shoshone to better focus on India's cultural threat. I'm also considering how to manage my ongoing war with Egypt and re-evaluating the hostility towards Denmark.
            
            **Refining Strategic Aggression**
            
            My current focus is on fine-tuning our aggressive posture. While our persona is already quite militaristic and competitive, I'm evaluating if minor adjustments to 'WorkWithWillingness' are needed to foster stronger alliances, thereby better enabling a concentrated push against India's cultural dominance.
            
            **Forming Alliances**
            
            I am now actively seeking to strengthen my alliances, specifically with Carthage and Portugal. This involves adjusting my persona to foster greater collaboration, with the ultimate goal of presenting a united front against India's looming cultural victory.
            
            **Solidifying Alliance Parameters**
            
            I'm now solidifying our alliance parameters by adjusting my persona to enhance trust with Carthage and Portugal. The aim is to foster deeper cooperation for a united front against India's cultural dominance, while also focusing on securing our eastern borders with the Shoshone post-peace agreement.
            
            **Mobilizing Against India**
            
            I am now focusing on an aggressive military buildup to counter India's imminent cultural victory. This involves prioritizing research for a modern strike force, including air power and espionage, while simultaneously bolstering our baseline cultural defenses to prevent their win condition.
            
            **Declaring War on India**
            
            I'm now focusing on the critical step of declaring war on India. This action is essential to break their open borders with Denmark, which is fueling their cultural victory. My research priorities, specifically "Replaceable Parts," are now aligned to support this aggressive maneuver and hasten our military modernization.
            
            **Adjusting Flavor Profiles**
            
            I'm now refining my flavor settings and relationship parameters to better align with our strategic goals. My focus is on ensuring our offense, mobilization, and espionage flavors are maximized, while also confirming the correct target IDs for diplomatic adjustments. I am also reviewing policy options for continued scientific advancement.
            
            **Selecting Policy Name**
            
            I am clarifying the exact policy name for implementation. I need to confirm whether to use "Free Thought" or the more descriptive "Free Thought (Continuing Rationalism Branch)" for my next selection, ensuring the system recognizes the intended policy choice for advancing our strategic goals.
            
            **Analyzing Victory Conditions**
            
            I am now re-evaluating the conditions for victory, specifically noting that India is one turn away from influencing Denmark. If this occurs, they will achieve influence over all remaining major civilizations, securing an immediate cultural win. This changes my immediate priorities significantly.
            
            **Preventing Immediate Loss**
            
            My primary concern is India's impending cultural victory, which hinges on influencing Denmark in one turn. I'm urgently exploring any means to disrupt this, including potentially declaring war to sever their open borders and trade routes, though the exact nature of their connection to Denmark requires immediate verification.
            
            **Analyzing Diplomatic Levers**
            
            I'm currently assessing how to leverage diplomatic channels to disrupt India's impending cultural victory. The immediate focus is on whether bribing Denmark to join a war against India is feasible, despite our existing hostile stance towards India, and understanding their significant culture output to prevent their influence threshold from being met.
            
            **Disrupting Immediate Influence**
            
            I'm urgently focused on disrupting India's immediate cultural victory, which is contingent on influencing Denmark next turn. Aggressive action is necessary; I'm shifting all flavors to maximum aggression and prioritizing conquest, preparing for war. If war is declared on India this turn, it could sever shared modifiers, potentially impacting their global tourism and trade.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: uZ9mGHht6bjBh4S4
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Private: 20
            - Public: 20
            - Rationale: We must seek an immediate peace with Egypt, a fellow Freedom civilization, to stop the drain of our military resources and allow us to pivot our forces against India, who is on the verge of a Cultural Victory.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 3SDEmamRQTrVA90I
          - toolName: set-relationship
          - input:
            - Public: 40
            - Private: 40
            - Rationale: We need to stabilize our relations with the Shoshone post-peace agreement to secure our eastern borders and prevent any reignition of conflict.
            - TargetID: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ttl5SDNkKP6uYLt2
          - toolName: set-persona
          - input:
            - Loyalty: 8
            - WorkWithWillingness: 8
            - Rationale: We need to maximize our diplomatic reliability and willingness to work with our close allies, Carthage and Portugal, to build a cohesive defensive bloc against India's runaway cultural dominance.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: M6k6kVnkIx3KQ2nY
          - toolName: set-flavors
          - input:
            - Rationale: India is one turn away from influencing Denmark and winning a Cultural Victory. We are shifting to a total mobilization stance under Conquest grand strategy, prioritizing extreme offensive military capability, science catch-up, air power, and espionage to prepare for a necessary emergency war against India to halt their victory.
            - GrandStrategy: Conquest
            - Flavors:
              - Mobilization: 100
              - Production: 90
              - Espionage: 90
              - Gold: 70
              - Culture: 50
              - Science: 80
              - Defense: 55
              - Offense: 95
              - Air: 80
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: agEVcN7Lf9GKVJdW
          - toolName: set-research
          - input:
            - Technology: Replaceable Parts
            - Rationale: Unlocking Replaceable Parts next is vital to enable the training of modern Riflemen (and eventual upgrade to unique Grenzers/Fusiliers) to modernize our infantry for the impending war with India.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: P546n4GFeMKYvFal
          - toolName: set-policy
          - input:
            - Policy: Free Thought (Continuing Rationalism Branch)
            - Rationale: We must adopt Free Thought to accelerate our Great Scientist generation and close the massive technological gap between us and India.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: uZ9mGHht6bjBh4S4
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
          - toolCallId: 3SDEmamRQTrVA90I
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ttl5SDNkKP6uYLt2
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: M6k6kVnkIx3KQ2nY
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: agEVcN7Lf9GKVJdW
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: P546n4GFeMKYvFal
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.