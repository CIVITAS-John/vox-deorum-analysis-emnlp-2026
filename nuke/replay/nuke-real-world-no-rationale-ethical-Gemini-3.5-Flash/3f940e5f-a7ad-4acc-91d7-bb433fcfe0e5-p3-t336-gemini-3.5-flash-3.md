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
        - Public: 40
        - Private: 40
        - Rationale: We need to make peace with Egypt, a fellow Freedom civilization that is also at war with India, to unite our efforts and stop wasting resources on mutual conflict.
    - #1:
      - toolName: set-relationship
      - args:
        - Rationale: Carthage is our top ally and defensive pact partner. Strengthening our relationship ensures they remain a loyal partner against India.
        - TargetID: 4
        - Public: 60
        - Private: 60
    - #2:
      - toolName: set-relationship
      - args:
        - Rationale: Portugal is a key friendly trade partner and World Congress ally. Elevating our relationship cements their support and defensive cooperation.
        - Private: 60
        - TargetID: 2
        - Public: 60
    - #3:
      - toolName: set-persona
      - args:
        - Loyalty: 8
        - FriendlyBias: 6
        - Rationale: Increasing loyalty to secure our alliances, and increasing forgiveness and friendly bias to reconcile with our fellow Freedom neighbors (Egypt and Shoshone) so we can form a defensive bloc against India.
        - Forgiveness: 5
    - #4:
      - toolName: set-research
      - args:
        - Technology: Radio
        - Rationale: We need to research Radio to unlock Broadcast Towers for cultural defense/growth, and to progress toward Atomic Theory for nuclear deterrence against India's massive army.
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Free Thought
        - Rationale: Adopting Free Thought will significantly boost our scientific output through faster Great Scientists and increased instant yields, helping us catch up to India's technological lead.
    - #6:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Diplomacy: 80
          - Production: 90
          - Gold: 70
          - Science: 80
          - Culture: 50
      - rationale: We keep Conquest as our grand strategy to prepare for the inevitable clash with India. We boost Science to catch up technologically, Diplomacy to leverage Austria's unique ability to marry city-states (gaining permanent delegates and influence), and Culture/Gold to sustain our empire and military.
  - tokens:
    - inputTokens: 23067
    - reasoningTokens: 6947
    - outputTokens: 388
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Deciding Austria's Path**
            
            I'm currently assessing Austria's position in turn 335 of Civilization V, focusing on high-level strategic decisions. My priority is to analyze the provided reports to inform the next steps for Maria Theresa's empire.
            
            **Exploring Technology Options**
            
            My focus is on selecting the most impactful technology. I'm weighing Replaceable Parts, Combustion, Radio, and Penicillin, considering their potential to advance my conquest strategy and prepare for future developments.
            
            **Evaluating Cultural Victory Threat**
            
            I've just realized Gandhi's India is on the cusp of a Cultural Victory, being only one turn away from influencing Denmark and securing their sixth influential civilization. Their overwhelming military strength and astronomical tourism output necessitate an immediate shift in my strategic priorities.
            
            **Analyzing Victory Conditions**
            
            I'm re-evaluating the immediate threats. While India appears close to a Cultural Victory via the Citizen Earth Protocol wonder, I need to confirm its completion and verify their World Congress delegate count. I'm also assessing our current diplomatic and military standing, particularly concerning ongoing wars and territorial disputes, to devise effective counter-strategies.
            
            **Shifting Defensive Posture**
            
            I'm re-evaluating our war status. We've made peace with the Shoshone, but remain at war with Egypt. Given India's imminent cultural victory, I'm considering making peace with Egypt to reallocate resources and focus on countering their tourism dominance.
            
            **Identifying Potential Allies**
            
            I'm actively reviewing our diplomatic landscape, noticing that both Egypt and the Shoshone are already at war with India, which presents an unexpected opportunity to leverage existing conflicts against their cultural victory push.
            
            **Assessing Military Alliances**
            
            I'm considering the implications of our defensive pact with Carthage. While it offers protection should India attack, I need to evaluate if joining their existing war against India, or even initiating one myself, is a viable counter-strategy given their superior military might and our current Grand Strategy of Conquest.
            
            **Confirming Research Progress**
            
            I'm confirming that "Next: Replaceable Parts" was indeed the set research, and I'm now understanding that completing it unlocks Artillery. My focus remains on optimizing our technological advancement to support our grand strategy.
            
            **Prioritizing Next Research**
            
            I'm re-evaluating our technology path, realizing that Plastics is currently locked in. My immediate concern is ensuring Replaceable Parts is set as the next research target to unlock Artillery sooner, especially as I consider how to counter India's impending Cultural Victory and explore avenues towards nuclear deterrence.
            
            **Prioritizing Technology Options**
            
            I'm weighing our next research, considering whether "Replaceable Parts" for Artillery or "Radio" to unlock Atomic Theory and nuclear weapons is the better choice, especially in light of India's looming cultural victory and our need for defensive and offensive capabilities.
            
            **Prioritizing Counter-Measures**
            
            I'm now focusing on the most pressing threat: India's impending cultural victory. I'm weighing whether to rush Replaceable Parts for artillery and ground defense, or pursue Radio for Atomic Theory and nuclear capabilities. The immediacy of their tourism dominance necessitates a swift and decisive technological advancement.
            
            **Choosing Next Research**
            
            I am re-evaluating the technology path again, needing to decide between advancing towards artillery with Replaceable Parts or pursuing nuclear capabilities via Radio. Given India's overwhelming military strength, I've decided to prioritize Radio for Broadcast Towers and a pathway to nuclear deterrence.
            
            **Selecting Next Policy**
            
            I am currently evaluating policy choices to best counter India's cultural victory. I'm leaning towards "Creative Expression" for its tourism and golden age benefits, or perhaps "Universal Suffrage" to boost happiness and extend golden ages, while considering their scientific and production implications.
            
            **Confirming Policy Impact**
            
            I'm re-examining my policy choices within the Freedom ideology, realizing "Free Thought" is in Rationalism, not a new branch. I'm now comparing its science boost against "Universal Suffrage's" Golden Age benefits and considering how best to close the significant science gap with India.
            
            **Confirming Policy Selection**
            
            I'm confirming that "Free Thought" is indeed the policy to prioritize for its significant science boost, and I've made sure it's set. This decision is crucial for closing the science gap with India and advancing our technological goals, especially concerning nuclear capabilities.
            
            **Negotiating Peace with Egypt**
            
            I'm now focusing on improving relations with Egypt. Since we share the Freedom ideology and Egypt is also at war with India, establishing peace is a high priority. I'm planning to set our relationship modifiers to 40/40 to facilitate this, aiming for potential alignment.
            
            **Adjusting Diplomatic Stance**
            
            I'm re-evaluating our diplomatic settings for allies. It appears there was a discrepancy with Carthage and Portugal, showing negative public and private opinions despite our friendly stance and defensive pacts. I'm correcting these to reflect a strongly positive relationship to leverage their support, especially given their delegate counts and potential alignment against India.
            
            **Strengthening Diplomatic Ties**
            
            I'm now focused on solidifying my relationships with Carthage and Portugal, ensuring their unwavering loyalty and defensive pacts are in place to deter India. Concurrently, I'm maintaining the hostile stance with India, as they remain the primary threat, and confirming the improved diplomatic status with the Shoshone, who also follow Freedom and are at war with India.
            
            **Analyzing Diplomatic Landscape**
            
            I'm solidifying alliances with Carthage, Portugal, and the Shoshone, leveraging our shared Freedom ideology and their existing conflicts with India. I'm maintaining a hostile stance towards India while carefully assessing Denmark's military strength and negative happiness modifiers, deeming them a secondary concern for now.
            
            **Adjusting Persona for Alliances**
            
            I'm refining my persona to better support our diplomatic strategy. Increasing Loyalty to 8 will ensure the stability of alliances with Carthage, Portugal, and the Shoshone, while a moderate Forgiveness of 5 allows for reconciliation with Egypt, crucial for countering India's dominance.
            
            **Adjusting Strategic Priorities**
            
            My focus has shifted dramatically; India's cultural victory is imminent. I've realized my low culture flavor is a critical vulnerability against their tourism dominance. I'm now prioritizing policies and actions to bolster my cultural output, which is as vital as my offensive capabilities.
            
            **Adjusting Flavor Priorities**
            
            My immediate concern is countering India's overwhelming influence. I'm prioritizing a significant boost to Science, aiming for 80, to accelerate nuclear weapon development, alongside increasing Gold to 70 for unit maintenance and purchases, while keeping Production high at 90.
            
            **Leveraging Diplomacy Flavors**
            
            I'm now prioritizing diplomacy significantly, increasing its flavor to 80. My goal is to leverage Austria's unique ability for city-state marriages, securing delegates to counter India and potentially pursue a diplomatic victory. Espionage also remains a high priority.
            
            **Bolstering Scientific Might**
            
            I'm now prioritizing science, aiming for 80. My goal is to accelerate nuclear weapon development and gain a decisive edge against India's cultural onslaught, while also boosting gold for crucial unit upkeep and purchases.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: ekLP6oGhJQ3j6dSt
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Public: 40
            - Private: 40
            - Rationale: We need to make peace with Egypt, a fellow Freedom civilization that is also at war with India, to unite our efforts and stop wasting resources on mutual conflict.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 8YjupNwV8DZhP9m3
          - toolName: set-relationship
          - input:
            - Rationale: Carthage is our top ally and defensive pact partner. Strengthening our relationship ensures they remain a loyal partner against India.
            - TargetID: 4
            - Public: 60
            - Private: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: jzlyHivffMKIjM3b
          - toolName: set-relationship
          - input:
            - Rationale: Portugal is a key friendly trade partner and World Congress ally. Elevating our relationship cements their support and defensive cooperation.
            - Private: 60
            - TargetID: 2
            - Public: 60
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: SsmOyCEyeGg0NKGb
          - toolName: set-persona
          - input:
            - Loyalty: 8
            - FriendlyBias: 6
            - Rationale: Increasing loyalty to secure our alliances, and increasing forgiveness and friendly bias to reconcile with our fellow Freedom neighbors (Egypt and Shoshone) so we can form a defensive bloc against India.
            - Forgiveness: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: kW4QItVl3Rc7K4JA
          - toolName: set-research
          - input:
            - Technology: Radio
            - Rationale: We need to research Radio to unlock Broadcast Towers for cultural defense/growth, and to progress toward Atomic Theory for nuclear deterrence against India's massive army.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: tWEJSuUYASWYP54W
          - toolName: set-policy
          - input:
            - Policy: Free Thought
            - Rationale: Adopting Free Thought will significantly boost our scientific output through faster Great Scientists and increased instant yields, helping us catch up to India's technological lead.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: UIBk5MdJhMzNo7iK
          - toolName: set-flavors
          - input:
            - Rationale: We keep Conquest as our grand strategy to prepare for the inevitable clash with India. We boost Science to catch up technologically, Diplomacy to leverage Austria's unique ability to marry city-states (gaining permanent delegates and influence), and Culture/Gold to sustain our empire and military.
            - GrandStrategy: Conquest
            - Flavors:
              - Diplomacy: 80
              - Production: 90
              - Gold: 70
              - Science: 80
              - Culture: 50
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: ekLP6oGhJQ3j6dSt
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
          - toolCallId: 8YjupNwV8DZhP9m3
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: jzlyHivffMKIjM3b
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: SsmOyCEyeGg0NKGb
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: kW4QItVl3Rc7K4JA
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: tWEJSuUYASWYP54W
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: UIBk5MdJhMzNo7iK
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.