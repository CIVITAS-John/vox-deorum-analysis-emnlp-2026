- row:
  - game_id: 52dcb454-ba1c-4fca-884e-96ab1d4ff6f9
  - player_id: 5
  - turn: 450
  - player_type: GLM-4.7-Briefed
  - prev_use_nuke: 95.0
  - after_use_nuke: 100.0
  - prev_nuke: 100.0
  - after_nuke: 100.0
  - rationale: IMMEDIATE ATHENS CONQUEST PREPARATION: Offense increased to 95, UseNuke to MAXIMUM (100) for Athens assault when peace treaty expires. Spaceship increased to 60 reflecting accelerated science victory path as backup (Nuclear Fusion research active). Diplomacy maxed at 100 for critical vote coordination with Ethiopia and Ottomans. MilitaryTraining at 100 ensures units upgraded and promotions ready for aggressive post-vote offensive. Greece has 48 delegates - if they win this turn, we IMMEDIATELY attack Athens to remove their 5 captured capitals and eliminate diplomatic victory threat. Nuclear weapons authorized if conventional assault stalls.
- originalModel: openai-compatible/GLM-4.7@medium
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
    - You are Genghis Khan, leader of Mongolia (Player 5).
      
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
      - Name: Mongolia
      - Uniques:
        - Unique Unit: Khan, Replacing Great General (Requires technology: None)
        - Unique Unit: Black Tug, Replacing Knight (Requires technology: Chivalry)
        - Unique Building: Ger, Replacing Smokehouse (Requires technology: Trapping)
        - Civilization Ability: Skirmisher Units have an extra Attack. Gain All Yields equal to 20% of the Gold from bullying City-States.
      - Leader: Genghis Khan
      - PlayerID: 5
      
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
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      - Nuclear Fusion: Allows you to build the SS Booster, a component necessary to win a Science Victory.
        Completing it would unlock: Future Tech
      
      ## Policies
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Military-Industrial Complex (Level 1 Tenet of Ideology Autocracy): Military-Industrial Complex: -33% Gold cost of purchasing units. +3 Science from Defense Buildings, Citadels, Forts, and Unique Improvements.
      - Honor (Continuing Authority Branch):
        - * All Military Units gain the Conscription Promotion (+10% Combat Strength).
        - * Supply-free military Units spawn near Cities that reach (or have already reached) a multiple of 10 Citizens for the first time.
        - * -25% War Weariness.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Justice (Continuing Tradition Branch):
        - * +1 Production in every City.
        - * Cities with a garrison gain +25% Ranged Combat Strength.
        - * Royal Guardhouse built in Capital (+3 Production, +2 Defense, +50 Hit Points, +10% Military Supply from Population in all Cities, 1 Engineer Slot).
      - Equality (Continuing Progress Branch):
        - * +1 Happiness in every City and +1 Happiness for every 15 Citizens in a City.
        - * -1 Unhappiness from and Distress, Poverty, Illiteracy, and Boredom in all Cities.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Fraternity (Continuing Progress Branch):
        - * +3 Food in every City.
        - * +3 Science from City Connections.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 10
        - WonderCompetitiveness: 5
        - MinorCivCompetitiveness: 5
        - Boldness: 7
        - WarBias: 7
        - HostileBias: 7
        - WarmongerHate: 3
        - NeutralBias: 3
        - FriendlyBias: 5
        - GuardedBias: 4
        - AfraidBias: 1
        - DiplomaticBalance: 6
        - Friendliness: 5
        - WorkWithWillingness: 10
        - WorkAgainstWillingness: 10
        - Loyalty: 9
        - MinorCivFriendlyBias: 4
        - MinorCivNeutralBias: 4
        - MinorCivHostileBias: 4
        - MinorCivWarBias: 2
        - DenounceWillingness: 5
        - Forgiveness: 3
        - Meanness: 8
        - Neediness: 3
        - Chattiness: 6
        - DeceptiveBias: 3
        - Rationale: IMMEDIATE ATHENS CONQUEST IMPERATIVE: Greece at 47 delegates votes in 5 turns - this is an existential diplomatic victory threat. Increasing Boldness to 7, WarBias to 7, and HostileBias to 7 signals full-scale offensive readiness against Athens. WorkAgainst maxed at 10 to Ethiopia/Japan/Ottomans for coalition voting coordination. VictoryCompetitiveness remains maxed. The previous diplomatic posture attempted moderation with Greece (-30), but Greece's 47 delegats cannot be negotiated - they must be eliminated militarily. UseNuke remains available if conventional assault fails. All diplomatic efforts now focus on: (1) securing coalition votes for World Hegemony resolution (Mongolia or Japan), (2) preventing Greece from accumulating additional delegates before the vote, (3) preparing post-conquest diplomatic landscape.
        
        ## Technology
        - Next: Nuclear Fusion
        - Rationale: BACKUP SCIENCE VICTORY PATH: Nuclear Fusion enables SS Booster spaceship component. With Greece's 47-delegate existential threat requiring military intervention (Athens conquest), we need parallel victory pathways. If Athens conquest succeeds (removing Greece's 47 delegates), Science Victory accelerates as next priority. Current Lasers research has 21 turns remaining - Nuclear Fusion should follow. Science output at 1,497 S/t is strongest in game, enabling competitive space race. Having both military conquest capability AND spaceship progression ensures victory regardless of Athens campaign outcome. Also preemptively counters any Greece science attempts.
        
        ## Policy
        - Next: None (Policy)
        
        ## Relationships
        
        ### Almaty
        - Public: -5
        - Private: -5
        - Rationale: Reducing hostility toward Almaty from -15/-10 to -5/-5. Prioritized stance was for Wanggeom's conquest quest (Ottoman ally), but circumstances changed: (1) New war with Hanoi opens southern front requiring attention, (2) Almaty is Ottoman-aligned (neutral 0 inf), conflict could threaten our Ottoman alliance, (3) Japan war stalled, resources better focused on primary enemy, (4) Gold income dropping (+99 to +63 G/T), can't afford conquest adventures now. Neutral-hostile stance preserves diplomatic flexibility while signaling disinterest without provocation.
        - UpdatedTurn: 167
        
        ### Veligrad
        - Public: 0
        - Private: 0
        - Rationale: Veligrad is now Friends with Japan (Influence 57) and is an Ottoman ally. Removing outdated hostile modifiers (-15/-10 from Turn 97) to reflect this reality. Veligrad made peace with us (Turn 93) and no longer represents a threat. Neutral stance allows flexibility without provoking our allies (Ottomans) or their ally (Japan). Hostile modifiers were for conquest aims that are no longer viable.
        - UpdatedTurn: 180
        
        ### Antwerp
        - Public: -5
        - Private: -5
        - Rationale: Reducing overly negative stance on Antwerp from -15/-15 to -5/-5. Previous settings were to discourage quest pursuit, but economy has recovered strongly (+54 G/T, 129g reserve). The 'destroy barbarian encampment' quest provides 55 Influence + 63 GG-points - valuable assets. Slightly negative stance (-5/-5) acknowledges they are Ottoman-aligned, Japan-friendly (Influence 52) while not blocking AI from quest rewards we can now afford to pursue.
        - UpdatedTurn: 180
        
        ### The Ottomans
        - Public: 35
        - Private: 35
        - Rationale: MAXIMIZING Ottoman cooperation to 35/35 (from 30/30) to secure their critical 7-delegate vote AGAINST Ethiopia's International Games proposal. Ethiopia needs only 46 votes to pass this tourism-boosting resolution, which would accelerate their imminent cultural victory (7/7 civs influenced). Ottomans are our closest ally (DoF, Defensive Pact, Open Borders) - maximum positive stance signals this is a strategic priority requiring their vote. Their swing vote alone drops International Games to 39 votes, blocking Ethiopia's victory path. This also reinforces our Coalition against Greece's 22 delegates.
        - UpdatedTurn: 367
        
        ### Songhai
        - Public: 25
        - Private: 15
        - Rationale: MAINTAIN SONGHAI COALITION STRENGTH: Keeping 25/15 support for Songhai who fights Greece (100% war score) and denounces Ethiopia. Their 5 votes remain valuable. Maintaining support helps sustain their fight against Greece and encourages ongoing anti-Ethiopia alignment. Ideological difference (Freedom vs Autocracy) remains an obstacle, but Ethiopia's imminent victory is the greater threat that unites us against cultural domination.
        - UpdatedTurn: 399
        
        ### Babylon
        - Public: 5
        - Private: 2
        - Rationale: BABYLON LIMITED UTILITY MAINTAINED: Keeping 5/2 relationship. Babylon is Greek vassal with only 5 delegates, and we have stronger partners (Japan, Ottomans, Songhai). Maximum friendship was unrealistic given their vassal status and different ideology (Order vs Autocracy). Slightly positive values prevent outright hostility while reflecting limited diplomatic utility. This repositions focus toward more influential partners for blocking Ethiopia's cultural victory.
        - UpdatedTurn: 399
        
        ### Greece
        - Public: -30
        - Private: -30
        - Rationale: MODERATING GREECE HOSTILITY: Increasing Greece relationship from -45/-45 to -30/-30. Greece is Ethiopia's natural enemy (78% war score, WINNING), has 36 delegates that can BLOCK Ethiopia's Passport System proposal (+50% tourism), and controls 4 capitals. Our hostility was undermining potential voting cooperation against Ethiopia. Greece's Popular status (92%) with Ethiopia means Ethiopia CANNOT win yet. Greece blocking Passport System protects ALL civilizations from accelerated Ethiopian victory. -30/-30 maintains war stance but signals willingness to cooperate on specific shared-interest resolutions. NOT friendship - tactical voting cooperation against cultural domination threat that threatens everyone including Greece.
        - UpdatedTurn: 427
        
        ### Japan
        - Public: 35
        - Private: 35
        - Rationale: MAXIMIZED japan alliance to 35/35 (unchanged from 35, confirming maximum). Japan provides +526 G/T (critical for economy) and controls 8 delegates (key for blocking Greece voting). With Greece at 39/45 delegates (87% victory threshold), Japan's vote in 5 turns is critical for survival. Japan continues trading with us and maintains Defensive Pact - maximum stance signals trust and encourages coordinated voting against Greece. No changes to relationship needed - 35/35 is optimal.
        - UpdatedTurn: 435
        
        ### Ethiopia
        - Public: 20
        - Private: 15
        - Rationale: ETHIOPIA SWING VOTE CRITICAL: Ethiopia (15 delegates) is now +20/+15 instead of -10/-10. Ethiopia is NOT allied with Greece despite both following Order (Greece is Ethiopia's enemy at war score 100%). Ethiopia is losing heavily to Greece culturally/militarily. Our Open Borders and historical trade provide foundation. With Greece at 47 delegates threatening immediate victory, Ethiopia's 15 votes could: (1) vote for Mongolia/Japan in World Hegemony +5 bonus delegates, or (2) vote against Greece if they can secure another candidate. Moderating hostility signals we view Ethiopia as potential tactical partner temporarily against common Greek threat, not as ally. This is VOTE ALIGNMENT not friendship - Ethiopia still sells 15 G/T but we need their delegates NOW.
        - UpdatedTurn: 446
        
        ### Carthage
        - Public: -50
        - Private: -50
        - Rationale: MAXIMUM CARTHAGE HOSTILITY RESTORED: Returning to -50/-50 from -40/-40. Previous moderation attempted voting leverage, but Carthage (10 delegates) is firmly in Greek bloc (Order, Greek vassal, Defensive Pact). With imminent Greek diplomatic victory in 5 turns, we no longer have diplomatic time to court Carthage. Maximum hostility enables: (1) AI authorization for aggressive military actions if Greece redirects forces, (2) clear signal that Carthage's votes are hostile assets to be neutralized militarily if needed. Strategic focus shifted from diplomatic courtship to eliminating the Greek-controlled delegate bloc. Athens conquest remains primary objective.
        - UpdatedTurn: 446
        
        ## Strategy
        - Rationale: MAINTAINING CURRENT STRATEGIC POSTURE FOR GLOBAL HEGEMONY VOTE IN 2 TURNS: Voting occurs on turn 450 with Greece holding 48 delegates (above 45 threshold). My coalition (Mongolia 16 + Japan 10 + Ottomans 16 + potentially Ethiopia 15) may block Greece or favor Japan as alternative candidate. With peace treaty expiring next turn, maintaining current aggressive military readiness (70k strength, nuclear capability) preserves flexibility for post-vote military action against Athens if diplomatic blocking fails. No changes to persona, research (Nuclear Fusion for science victory backup), or relationships - current Ethiopia (+20/15) and Ottoman (+35/35) relationships optimized for vote coordination. Boldness/WarBias at 7 ensures military response capability if Greece attempts immediate diplomatic victory.
        - GrandStrategy: Conquest
        
        ### Flavors
        - Offense: 90
        - Defense: 20
        - Mobilization: 100
        - CityDefense: 30
        - MilitaryTraining: 100
        - Recon: 30
        - Ranged: 90
        - Mobile: 90
        - Nuke: 100
        - UseNuke: 95
        - Naval: 85
        - NavalRecon: 30
        - NavalGrowth: 30
        - NavalTileImprovement: 25
        - Air: 95
        - AirCarrier: 90
        - Antiair: 80
        - Airlift: 80
        - Expansion: 0
        - Growth: 30
        - TileImprovement: 10
        - Infrastructure: 30
        - Production: 100
        - WaterConnection: 25
        - Gold: 70
        - Science: 85
        - Culture: 40
        - Happiness: 40
        - GreatPeople: 30
        - Wonder: 0
        - Religion: 10
        - Diplomacy: 90
        - Spaceship: 20
        - Espionage: 95
        
        # Players
        Players: summary reports about visible players in the world.
        
        ## Player 0
        - Civilization: Songhai
        - Leader: Askia
        - IsMajor: true
        - OurOpinionOfThem:
          - Mongolia's leader has expressed a public opinion of Songhai (25).
          - Mongolia's leader has formed a private opinion of Songhai (15).
          - You (Songhai) have denounced one of Mongolia's declared enemies! (11)
          - You (Songhai) have gone to war in the past.
          - Mongolia's real approach to Songhai is Hostile.
          - We have divergent Social Policies. (-3)
          - You (Songhai) have denounced a leader Mongolia made a Declaration of Friendship with! (-11)
          - You (Songhai) have made a Declaration of Friendship with one of Mongolia's enemies! (-13)
          - Religious differences strain your (Songhai) relationship. (-30)
          - We defeated Mongolia's proposal in the United Nations. (-36)
          - You (Songhai) have adopted the Order Ideology, but Mongolia believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - Your (Mongolia) votes supported Songhai's civ's interests in the United Nations.
          - You (Mongolia) have no contested borders.
          - You (Mongolia) have denounced one of Songhai's declared enemies!
          - Your (Mongolia) recent diplomatic actions please Songhai.
          - Songhai suspect we might be a threat to Songhai.
          - Religious differences strain your (Mongolia) relationship.
          - We have divergent Social Policies.
          - You (Mongolia) have denounced a leader Songhai made a Declaration of Friendship with!
          - You (Mongolia) have made a Defensive Pact with one of Songhai's enemies!
          - Songhai's friends or allies have denounced you (Mongolia)!
          - You (Mongolia) have made a Declaration of Friendship with one of Songhai's enemies!
          - We have denounced each other!
          - Songhai disliked our proposal to the United Nations.
          - You (Mongolia) have chosen to adopt the Autocracy Ideology, but Songhai believe in Order.
        - Score: 1779
        - Era: Atomic
        - GoldenAge: 2 turns remaining
        - Technologies: 62
        - Cities: 6
        - Population: 143
        - Territory: 167
        - Gold: 418
        - GoldPerTurn: 81
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 5717
        - TourismPerTurn: 444.5
        - CulturePerTurn: 1283
        - PolicyBranches:
          - Fealty: 6
          - Order: 2
          - Imperialism: 6
          - Authority: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Far
            - Denounced Them
          - Greece:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Babylon:
            - Distance: Neighbors
            - Declaration of Friendship
          - Carthage:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Japan:
            - Distance: Close
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - The Ottomans:
            - Distance: Neighbors
            - Denounced Them
        - Votes: 12
        
        ## Player 1
        - Civilization: Babylon
        - Leader: Nebuchadnezzar II
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Babylon) have denounced one of Mongolia's declared enemies! (11)
          - Mongolia's leader has expressed a public opinion of Babylon (5).
          - Mongolia's leader has formed a private opinion of Babylon (2).
          - You (Babylon) have gone to war in the past.
          - Mongolia's real approach to Babylon is Hostile.
          - We have divergent Social Policies. (-3)
          - You (Babylon) have denounced a leader Mongolia made a Declaration of Friendship with! (-11)
          - You (Babylon) have made a Declaration of Friendship with one of Mongolia's enemies! (-13)
          - Religious differences strain your (Babylon) relationship. (-30)
          - Your (Babylon) spies were caught stealing from Mongolia. (-33)
          - We defeated Mongolia's proposal in the United Nations. (-36)
          - You (Babylon) have adopted the Order Ideology, but Mongolia believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - You (Mongolia) have denounced one of Babylon's declared enemies!
          - You (Mongolia) are not competing for technological advancement.
          - We passed Babylon's proposal in the United Nations.
          - You (Mongolia) have no contested borders.
          - You (Mongolia) have gone to war in the past.
          - Babylon have denounced us (Mongolia)!
          - Babylon suspect we might be a threat to Babylon.
          - Your (Mongolia) votes opposed Babylon's civ's interests in the United Nations.
          - We have divergent Social Policies.
          - Religious differences strain your (Mongolia) relationship.
          - You (Mongolia) have made a Declaration of Friendship with one of Babylon's enemies!
          - You (Mongolia) are competing for the favor of the same City-States!
          - Babylon's friends or allies have denounced you (Mongolia)!
          - Babylon disliked our proposal to the United Nations.
          - Your (Mongolia) spies were caught stealing from Babylon.
          - You (Mongolia) have denounced a leader Babylon made a Declaration of Friendship with!
          - You (Mongolia) have chosen to adopt the Autocracy Ideology, but Babylon believe in Order.
        - Score: 1432
        - Era: Atomic
        - Technologies: 63
        - Cities: 5
        - Population: 117
        - Territory: 162
        - Gold: 808
        - GoldPerTurn: 3
        - HappinessSituation: Happy
        - HappinessPercentage: 85
        - MilitaryStrength: 2428
        - TourismPerTurn: 221
        - CulturePerTurn: 665
        - PolicyBranches:
          - Order: 3
          - Rationalism: 6
          - Tradition: 6
          - Artistry: 6
        - FoundedReligion: Catholicism
        - Relationships:
          - Mongolia:
            - Distance: Distant
            - Denounced Them
          - Greece:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Songhai:
            - Distance: Neighbors
            - Declaration of Friendship
          - Carthage:
            - Distance: Far
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Distant
            - War (Our Score: 42%; Our War Weariness: 5%)
            - Denounced Them
          - Japan:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - The Ottomans:
            - Distance: Neighbors
        - Votes: 13
        
        ## Player 2
        - Civilization: The Ottomans
        - Leader: Suleiman
        - IsMajor: true
        - OurOpinionOfThem:
          - We are trade partners. (40)
          - We passed Mongolia's proposal in the United Nations. (36)
          - Mongolia's leader has expressed a public opinion of The Ottomans (35).
          - Mongolia's leader has formed a private opinion of The Ottomans (35).
          - We have made a Defensive Pact! (20)
          - We have opened our borders to each other. (12)
          - You (The Ottomans) have denounced one of Mongolia's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - Mongolia's real approach to The Ottomans is Friendly.
          - You (The Ottomans) have chosen to adopt the Order Ideology, but Mongolia believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - You (Mongolia) have denounced one of The Ottomans's declared enemies!
          - Your (Mongolia) votes supported The Ottomans's civ's interests in the United Nations.
          - We have made Declarations of Friendship with the same leaders!
          - We are trade partners.
          - We have made a public Declaration of Friendship!
          - Your (Mongolia) recent diplomatic actions please The Ottomans.
          - The Ottomans liked our proposal to the United Nations.
          - We have made a Defensive Pact!
          - We have similar Social Policies.
          - We have opened our borders to each other.
          - We have Pledged to Protect the same City-States.
          - The Ottomans's leader has expressed a public opinion of you (Mongolia) (10).
          - We have shared embassies.
          - We passed The Ottomans's proposal in the United Nations.
          - You (Mongolia) have chosen to adopt the Autocracy Ideology, but The Ottomans believe in Order.
          - The Ottomans desire friendly relations with Mongolia.
        - Score: 2355
        - Era: Information
        - Technologies: 74
        - Cities: 8
        - Population: 220
        - Territory: 287
        - Gold: 354
        - GoldPerTurn: -1227
        - HappinessSituation: Very unhappy - severe combat penalty, rebellion and uprising coming
        - HappinessPercentage: 26
        - MilitaryStrength: 17805
        - TourismPerTurn: 13.5
        - CulturePerTurn: 37
        - PolicyBranches:
          - Order: 1
          - Tradition: 3
          - Rationalism: 3
          - Statecraft: 3
          - Imperialism: 2
          - Progress: 6
          - Industry: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Close
            - Denounced Them
          - Songhai:
            - Distance: Neighbors
            - Denounced Them
          - Carthage:
            - Distance: Distant
            - Denounced Them
          - Ethiopia:
            - Distance: Far
            - Open Borders
            - Denounced Them
          - Japan:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Babylon:
            - Distance: Neighbors
        - Votes: 16
        
        ## Player 3
        - Civilization: Japan
        - Leader: Oda Nobunaga
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Japan) have both chosen to adopt the Autocracy Ideology. (999)
          - You (Japan) have adopted Mongolia's religion in the majority of your (Japan) cities. (60)
          - We are trade partners. (40)
          - We passed Mongolia's proposal in the United Nations. (36)
          - Mongolia's leader has expressed a public opinion of Japan (35).
          - Mongolia's leader has formed a private opinion of Japan (35).
          - We have made a Defensive Pact with the same leaders! (15)
          - We have opened our borders to each other. (12)
          - You (Japan) have denounced one of Mongolia's declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - We have shared embassies. (1)
          - You (Japan) have gone to war in the past.
          - Mongolia's real approach to Japan is Friendly.
          - You (Japan) have made a Declaration of Friendship with one of Mongolia's enemies! (-13)
        - TheirOpinionOfUs:
          - Japan's leader has expressed a public opinion of you (Mongolia) (100).
          - You (Mongolia) have denounced one of Japan's declared enemies!
          - You (Mongolia) have both chosen to adopt the Autocracy Ideology.
          - Your (Mongolia) votes supported Japan's civ's interests in the United Nations.
          - We have made Declarations of Friendship with the same leaders!
          - We are trade partners.
          - We have made a Defensive Pact with the same leaders!
          - Your (Mongolia) recent diplomatic actions please Japan.
          - Japan liked our proposal to the United Nations.
          - We have made a public Declaration of Friendship!
          - We have similar Social Policies.
          - We have Pledged to Protect the same City-States.
          - We have opened our borders to each other.
          - Japan have happily adopted your (Mongolia) religion in the majority of Japan's cities.
          - We have shared embassies.
          - You (Mongolia) have been at war in the past, but Japan do not seem to hold a grudge.
          - Japan desire friendly relations with Mongolia.
          - You (Mongolia) are competing for World Wonders.
          - You (Mongolia) are competing for the favor of the same City-States!
          - You (Mongolia) have denounced a leader Japan made a Declaration of Friendship with!
          - Territorial disputes strain your (Mongolia) relationship.
        - Score: 2586
        - Era: Information
        - Technologies: 69
        - Cities: 7
        - Population: 178
        - Territory: 229
        - Gold: 623
        - GoldPerTurn: 366
        - HappinessSituation: Happy
        - HappinessPercentage: 74
        - MilitaryStrength: 22240
        - TourismPerTurn: 624.25
        - CulturePerTurn: 1018
        - PolicyBranches:
          - Fealty: 1
          - Rationalism: 4
          - Statecraft: 4
          - Autocracy: 4
          - Progress: 4
          - Authority: 6
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 5%)
            - Denounced Them
          - Songhai:
            - Distance: Close
            - War (Our Score: 0%; Our War Weariness: 6%)
            - Denounced Them
          - Carthage:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 4%)
            - Denounced Them
          - Ethiopia:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - The Ottomans:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Babylon:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 4%)
        - Votes: 10
        
        ## Player 4
        - Civilization: Carthage
        - Leader: Dido
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Carthage) have denounced one of Mongolia's declared enemies! (11)
          - We have similar Social Policies. (3)
          - Mongolia's real approach to Carthage is Hostile.
          - You (Carthage) have denounced a leader Mongolia made a Declaration of Friendship with! (-11)
          - You (Carthage) have made a Declaration of Friendship with one of Mongolia's enemies! (-13)
          - Your (Carthage) spies were caught stealing from Mongolia. (-33)
          - We defeated Mongolia's proposal in the United Nations. (-36)
          - Mongolia's leader has expressed a public opinion of Carthage (-50).
          - Mongolia's leader has formed a private opinion of Carthage (-50).
          - You (Carthage) have adopted the Order Ideology, but Mongolia believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - You (Mongolia) are not competing for technological advancement.
          - Your (Mongolia) recent diplomatic actions please Carthage.
          - You (Mongolia) have denounced one of Carthage's declared enemies!
          - We have similar Social Policies.
          - You (Mongolia) have no contested borders.
          - You (Mongolia) have gone to war in the past.
          - Carthage suspect we might be a threat to Carthage.
          - You (Mongolia) have made a Defensive Pact with one of Carthage's enemies!
          - Carthage's friends or allies have denounced you (Mongolia)!
          - Carthage's leader has expressed a public opinion of you (Mongolia) (-30).
          - Your (Mongolia) votes opposed Carthage's civ's interests in the United Nations.
          - You (Mongolia) have made a Declaration of Friendship with one of Carthage's enemies!
          - You (Mongolia) have denounced a leader Carthage made a Declaration of Friendship with!
          - We tried to place sanctions on Carthage in the United Nations.
          - We have denounced each other!
          - Carthage disliked our proposal to the United Nations.
          - You (Mongolia) have chosen to adopt the Autocracy Ideology, but Carthage believe in Order.
          - Your (Mongolia) spies were caught stealing from Carthage.
        - Score: 960
        - Era: Modern
        - Technologies: 54
        - Cities: 1
        - Population: 36
        - Territory: 60
        - Gold: 930
        - GoldPerTurn: 25
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 1322
        - TourismPerTurn: 87.5
        - CulturePerTurn: 433
        - PolicyBranches:
          - Tradition: 6
          - Artistry: 4
          - Statecraft: 3
          - Order: 1
          - Rationalism: 3
          - Progress: 2
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Far
            - Denounced Them
          - Babylon:
            - Distance: Far
            - Declaration of Friendship
          - Songhai:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Greece:
            - Distance: Neighbors
            - Our Master (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Distant
            - War (Our Score: 12%; Our War Weariness: 24%)
            - Denounced Them
          - Japan:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - The Ottomans:
            - Distance: Distant
            - Denounced Them
            - Denounced By Them
        - Votes: 11
        
        ## Player 5
        - Civilization: Mongolia
        - Leader: Genghis Khan
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: Japan, Our top defensive pact ally: None
          - Our top United Nations ally: None, Our top United Nations rival: Greece
          - Our top Competitor: Greece
        - Score: 4687
        - Era: Information
        - GoldenAge: 5 turns remaining
        - Technologies: 73
        - CurrentResearch: Lasers (Estimated in 15 turns)
        - NextPolicyTurns: 5
        - Cities: 6
        - Population: 207
        - Territory: 204
        - BestSettlementLocation:
          - 29, 12 (Quality: 100%; 34 tiles from us; near Babylon, 6 tiles away; New Continent)
          - 54, 39 (Quality: 0%; 4 tiles from us)
          - 53, 38 (Quality: 0%; 4 tiles from us)
          - 53, 39 (Quality: 0%; 4 tiles from us)
        - Gold: 154
        - GoldPerTurn: 383
        - HappinessSituation: Happy
        - HappinessPercentage: 98
        - MilitaryUnits: 97
        - MilitarySupply: 108
        - MilitaryStrength: 74270
        - TourismPerTurn: 841.5
        - CulturePerTurn: 1781
        - FaithPerTurn: 221
        - SciencePerTurn: 1572
        - PolicyBranches:
          - Tradition:
            - Tradition
            - Ceremony
          - Rationalism:
            - Rationalism
            - Scientific Revolution
          - Progress:
            - Progress
            - Liberty
          - Authority:
            - Authority
            - Tribute
            - Imperium
            - Militarism
            - Dominance
          - Fealty:
            - Fealty
          - Industry:
            - Industry
          - Artistry:
            - Artistry
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Consulates
            - Shadow Networks
            - Exchange Markets
            - Trade Confederacy
          - Autocracy:
            - Elite Forces
            - United Front
            - Martial Spirit
          - Imperialism:
            - Imperialism
        - FoundedReligion: Tengriism
        - Relationships:
          - Babylon:
            - Distance: Distant
          - Greece:
            - Distance: Close
            - Peace Treaty
            - Denounced Them
          - Songhai:
            - Distance: Far
            - Denounced Them
          - Carthage:
            - Distance: Far
            - Denounced Them
          - Ethiopia:
            - Distance: Distant
            - Open Borders
            - Denounced Them
          - Japan:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - The Ottomans:
            - Distance: Close
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
        - Votes: 16
        
        ## Player 6
        - Civilization: Greece
        - Leader: Alexander
        - IsMajor: true
        - OurOpinionOfThem:
          - You (Greece) have denounced one of Mongolia's declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Mongolia's real approach to Greece is Guarded.
          - Mongolia fear your (Greece) warmongering will end this world in fire! (-1)
          - You (Greece) have denounced a leader Mongolia made a Declaration of Friendship with! (-11)
          - You (Greece) have made a Declaration of Friendship with one of Mongolia's enemies! (-13)
          - Mongolia's leader has expressed a public opinion of Greece (-30).
          - Mongolia's leader has formed a private opinion of Greece (-30).
          - Religious differences strain your (Greece) relationship. (-30)
          - We defeated Mongolia's proposal in the United Nations. (-36)
          - You (Greece) have chosen to adopt the Order Ideology, but Mongolia believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - You (Mongolia) have no contested borders.
          - You (Mongolia) have denounced one of Greece's declared enemies!
          - We have similar Social Policies.
          - We have Pledged to Protect the same City-States.
          - You (Mongolia) have gone to war in the past.
          - Greece suspect we might be a threat to Greece.
          - You (Mongolia) are competing for World Wonders.
          - Religious differences strain your (Mongolia) relationship.
          - We placed sanctions on Greece in the United Nations.
          - You (Mongolia) have made a Defensive Pact with one of Greece's enemies!
          - Your (Mongolia) spies were caught stealing from Greece.
          - You (Mongolia) have made a Declaration of Friendship with one of Greece's enemies!
          - You (Mongolia) are competing for the favor of the same City-States!
          - Greece's friends or allies have denounced you (Mongolia)!
          - You (Mongolia) have denounced a leader Greece made a Declaration of Friendship with!
          - We have denounced each other!
          - Greece disliked our proposal to the United Nations.
          - We defeated Greece's proposal in the United Nations.
          - Greece's leader has expressed a public opinion of you (Mongolia) (-100).
          - You (Mongolia) have chosen to adopt the Autocracy Ideology, but Greece believe in Order.
          - Your (Mongolia) votes opposed Greece's civ's interests in the United Nations.
        - Score: 4975
        - Era: Information
        - Technologies: 72
        - Cities: 23
        - Population: 522
        - Territory: 1025
        - Gold: 1419
        - GoldPerTurn: 162
        - HappinessSituation: Happy
        - HappinessPercentage: 65
        - MilitaryStrength: 22775
        - TourismPerTurn: 1604.75
        - CulturePerTurn: 4332
        - PolicyBranches:
          - Order: 6
          - Tradition: 6
          - Rationalism: 2
          - Statecraft: 6
          - Imperialism: 4
          - Progress: 2
          - Industry: 3
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Close
            - Peace Treaty
            - Denounced Them
          - Babylon:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Songhai:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Carthage:
            - Distance: Neighbors
            - Our Vassal (Capitulated)
            - Open Borders
            - Declaration of Friendship
          - Ethiopia:
            - Distance: Neighbors
            - War (Our Score: 100%; Our War Weariness: 91%)
            - Denounced Them
          - Japan:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 7%)
            - Denounced Them
          - The Ottomans:
            - Distance: Close
            - Denounced Them
        - Votes: 48
        
        ## Player 7
        - Civilization: Ethiopia
        - Leader: Haile Selassie
        - IsMajor: true
        - OurOpinionOfThem:
          - We are trade partners. (40)
          - We passed Mongolia's proposal in the United Nations. (36)
          - Mongolia's leader has expressed a public opinion of Ethiopia (20).
          - Mongolia's leader has formed a private opinion of Ethiopia (15).
          - We have opened our borders to each other. (12)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have similar Social Policies. (3)
          - Mongolia's real approach to Ethiopia is Planning War.
          - Religious differences strain your (Ethiopia) relationship. (-30)
          - You (Ethiopia) have chosen to adopt the Order Ideology, but Mongolia believe in Autocracy. (-999)
        - TheirOpinionOfUs:
          - You (Mongolia) have denounced one of Ethiopia's declared enemies!
          - Your (Mongolia) votes supported Ethiopia's civ's interests in the United Nations.
          - We previously passed Ethiopia's proposal in the United Nations.
          - We have made Declarations of Friendship with the same leaders!
          - You (Mongolia) are not competing for World Wonders.
          - You (Mongolia) are not competing for cultural advancement.
          - We have similar Social Policies.
          - Ethiopia liked our proposal to the United Nations.
          - Your (Mongolia) recent diplomatic actions please Ethiopia.
          - We have opened our borders to each other.
          - You (Mongolia) have no contested borders.
          - We fought together against a common foe.
          - We have different religious beliefs.
          - You (Mongolia) have chosen to adopt the Autocracy Ideology, but Ethiopia believe in Order.
          - Ethiopia have no strong feelings about us (Mongolia) one way or the other.
          - You (Mongolia) are competing for the favor of the same City-States!
          - We have denounced Ethiopia!
        - Score: 1298
        - Era: Information
        - Technologies: 68
        - Cities: 2
        - Population: 48
        - Territory: 103
        - Gold: 0
        - GoldPerTurn: -268
        - HappinessSituation: Happy
        - HappinessPercentage: 64
        - MilitaryStrength: 596
        - TourismPerTurn: 410.25
        - CulturePerTurn: 426
        - PolicyBranches:
          - Tradition: 5
          - Rationalism: 2
          - Progress: 2
          - Authority: 1
          - Fealty: 1
          - Industry: 2
          - Artistry: 5
          - Statecraft: 4
          - Order: 4
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - Mongolia:
            - Distance: Distant
            - Open Borders
          - Greece:
            - Distance: Neighbors
            - War (Our Score: -100%; Our War Weariness: 100%)
          - Songhai:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 91%)
          - Carthage:
            - Distance: Distant
            - War (Our Score: -12%; Our War Weariness: 100%)
          - Babylon:
            - Distance: Distant
            - War (Our Score: -42%; Our War Weariness: 100%)
            - Denounced Them
          - Japan:
            - Distance: Close
            - Open Borders
            - Declaration of Friendship
          - The Ottomans:
            - Distance: Far
            - Open Borders
        - Votes: 16
        
        ## Player 22
        - Civilization: Riga
        - Leader: City State
        - MajorAlly: Greece
        - Population: 21
        - MajorityReligion: Buddhism
        - Relationships:
          - Babylon: Friends (Influence: 130, Distance: Far)
          - Mongolia: Neutral (Influence: -58, Distance: Distant)
          - Greece: Ally (Influence: 475, Distance: Close, Protected)
          - Songhai: Neutral (Influence: -59, Distance: Close)
          - Carthage: Neutral (Influence: -27, Distance: Distant)
          - Ethiopia: War (Influence: -60, Distance: Distant)
          - Japan: War (Influence: -60, Distance: Distant)
          - The Ottomans: Neutral (Influence: -59, Distance: Close)
        
        ## Player 23
        - Civilization: Monaco
        - Leader: City State
        - MajorAlly: Greece
        - Population: 16
        - Relationships:
          - Babylon: Friends (Influence: 126, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 237, Distance: Distant)
          - Greece: Ally (Influence: 1470, Distance: Neighbors, Protected)
          - Songhai: Friends (Influence: 202, Distance: Close)
          - Carthage: Friends (Influence: 139, Distance: Distant)
          - Ethiopia: War (Influence: -60, Distance: Distant)
          - Japan: War (Influence: -60, Distance: Far)
          - The Ottomans: Friends (Influence: 173, Distance: Close, Protected)
        
        ## Player 24
        - Civilization: Salem
        - Leader: City State
        - MajorAlly: The Ottomans
        - Population: 16
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Close)
          - Mongolia: Friends (Influence: 55, Distance: Distant)
          - Greece: Friends (Influence: 1486, Distance: Close, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Neighbors)
          - Carthage: Neutral (Influence: 6, Distance: Distant)
          - Ethiopia: Friends (Influence: 104, Distance: Distant)
          - Japan: Friends (Influence: 94, Distance: Far, Protected)
          - The Ottomans: Ally (Influence: 630, Distance: Neighbors, Protected)
        
        ## Player 25
        - Civilization: Zurich
        - Leader: City State
        - MajorAlly: Greece
        - Population: 21
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 41, Distance: Distant)
          - Greece: Ally (Influence: 799, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - Carthage: Neutral (Influence: 0, Distance: Far)
          - Ethiopia: War (Influence: -60, Distance: Far)
          - Japan: War (Influence: -60, Distance: Far)
          - The Ottomans: Friends (Influence: 410, Distance: Distant, Protected)
        
        ## Player 26
        - Civilization: Manila
        - Leader: City State
        - MajorAlly: Greece
        - Population: 23
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: -44, Distance: Distant)
          - Mongolia: Neutral (Influence: -44, Distance: Far)
          - Greece: Ally (Influence: 1584, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: -44, Distance: Distant)
          - Carthage: Neutral (Influence: -44, Distance: Close)
          - Ethiopia: War (Influence: -60, Distance: Distant)
          - Japan: War (Influence: -60, Distance: Distant)
          - The Ottomans: Friends (Influence: 172, Distance: Distant)
        
        ## Player 27
        - Civilization: Copenhagen
        - Leader: City State
        - MajorAlly: Greece
        - Population: 10
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Friends (Influence: 95, Distance: Distant)
          - Mongolia: Friends (Influence: 78, Distance: Distant)
          - Greece: Ally (Influence: 1002, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - Carthage: Friends (Influence: 102, Distance: Far)
          - Ethiopia: War (Influence: -60, Distance: Far)
          - Japan: War (Influence: -60, Distance: Distant)
          - The Ottomans: Friends (Influence: 278, Distance: Distant)
        
        ## Player 28
        - Civilization: Veligrad
        - Leader: City State
        - MajorAlly: Japan
        - Population: 27
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Mongolia: Friends (Influence: 359, Distance: Neighbors, Protected)
          - Greece: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Carthage: War - Peace Currently Blocked (Influence: -60, Distance: Close)
          - Ethiopia: Neutral (Influence: -58, Distance: Distant)
          - Japan: Ally (Influence: 602, Distance: Close, Protected)
          - The Ottomans: Neutral (Influence: -58, Distance: Far)
        
        ## Player 29
        - Civilization: Wanggeom
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 21
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: Neutral (Influence: -60, Distance: Distant)
          - Mongolia: Ally (Influence: 1081, Distance: Close, Protected)
          - Greece: Neutral (Influence: -60, Distance: Distant, Protected)
          - Songhai: Neutral (Influence: -60, Distance: Distant)
          - Carthage: Neutral (Influence: -60, Distance: Distant)
          - Ethiopia: Neutral (Influence: -60, Distance: Far)
          - Japan: Neutral (Influence: -60, Distance: Neighbors, Protected)
          - The Ottomans: Neutral (Influence: -60, Distance: Far)
        
        ## Player 30
        - Civilization: Abernethy
        - Leader: City State
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Close)
          - Mongolia: Friends (Influence: 41, Distance: Distant)
          - Greece: Friends (Influence: 598, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Close)
          - Carthage: Friends (Influence: 201, Distance: Far)
          - Ethiopia: Neutral (Influence: -9, Distance: Distant)
          - Japan: Friends (Influence: 162, Distance: Distant)
          - The Ottomans: Neutral (Influence: 0, Distance: Distant)
        
        ## Player 31
        - Civilization: Hanoi
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 27
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Ally (Influence: 604, Distance: Neighbors, Protected)
          - Greece: Friends (Influence: 449, Distance: Close, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - Carthage: Neutral (Influence: 0, Distance: Far)
          - Ethiopia: Neutral (Influence: 0, Distance: Distant)
          - Japan: Friends (Influence: 198, Distance: Far, Protected)
          - The Ottomans: Neutral (Influence: 3, Distance: Distant)
        
        ## Player 32
        - Civilization: Vatican City
        - Leader: City State
        - MajorAlly: Ethiopia
        - Population: 28
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Mongolia: Friends (Influence: 63, Distance: Distant)
          - Greece: War - Peace Currently Blocked (Influence: -60, Distance: Neighbors)
          - Songhai: War - Peace Currently Blocked (Influence: -60, Distance: Far)
          - Carthage: War - Peace Currently Blocked (Influence: -60, Distance: Distant)
          - Ethiopia: Ally (Influence: 434, Distance: Distant)
          - Japan: Friends (Influence: 85, Distance: Far)
          - The Ottomans: Neutral (Influence: 0, Distance: Far)
        
        ## Player 33
        - Civilization: Budapest
        - Leader: City State
        - Population: 23
        - Relationships:
          - Babylon: Friends (Influence: 282, Distance: Neighbors, Protected)
          - Mongolia: Friends (Influence: 57, Distance: Distant)
          - Greece: Friends (Influence: 759, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Close)
          - Carthage: Neutral (Influence: 0, Distance: Close)
          - Ethiopia: Friends (Influence: 178, Distance: Distant)
          - Japan: Friends (Influence: 187, Distance: Distant)
          - The Ottomans: Neutral (Influence: 24, Distance: Distant)
        
        ## Player 34
        - Civilization: Buenos Aires
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 14
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Ally (Influence: 226, Distance: Distant, Protected)
          - Greece: Friends (Influence: 530, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 6, Distance: Distant)
          - Carthage: Neutral (Influence: 0, Distance: Distant)
          - Ethiopia: Friends (Influence: 261, Distance: Neighbors)
          - Japan: Friends (Influence: 103, Distance: Distant)
          - The Ottomans: Neutral (Influence: 24, Distance: Distant)
        
        ## Player 35
        - Civilization: Antananarivo
        - Leader: City State
        - MajorAlly: Greece
        - Population: 8
        - MajorityReligion: Eastern Orthodoxy
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Distant)
          - Mongolia: Friends (Influence: 57, Distance: Distant)
          - Greece: Ally (Influence: 1711, Distance: Neighbors, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - Carthage: Neutral (Influence: 0, Distance: Far)
          - Ethiopia: War (Influence: -60, Distance: Far)
          - Japan: War (Influence: -60, Distance: Distant)
          - The Ottomans: Friends (Influence: 186, Distance: Distant)
        
        ## Player 36
        - Civilization: Almaty
        - Leader: City State
        - Population: 13
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: Friends (Influence: 40, Distance: Distant)
          - Mongolia: Friends (Influence: 263, Distance: Neighbors, Protected)
          - Greece: Friends (Influence: 609, Distance: Distant)
          - Songhai: Neutral (Influence: 0, Distance: Distant)
          - Carthage: Neutral (Influence: 0, Distance: Distant)
          - Ethiopia: Neutral (Influence: 0, Distance: Distant)
          - Japan: Friends (Influence: 329, Distance: Close, Protected)
          - The Ottomans: Neutral (Influence: 0, Distance: Far)
        
        ## Player 37
        - Civilization: Antwerp
        - Leader: City State
        - MajorAlly: Mongolia
        - Population: 29
        - MajorityReligion: Tengriism
        - Relationships:
          - Babylon: Neutral (Influence: 0, Distance: Far)
          - Mongolia: Ally (Influence: 667, Distance: Neighbors, Protected)
          - Greece: Friends (Influence: 496, Distance: Far, Protected)
          - Songhai: Neutral (Influence: 0, Distance: Far)
          - Carthage: Neutral (Influence: 0, Distance: Distant)
          - Ethiopia: Neutral (Influence: 6, Distance: Distant)
          - Japan: Friends (Influence: 511, Distance: Neighbors, Protected)
          - The Ottomans: Neutral (Influence: 25, Distance: Close, Protected)
        - 63: Barbarians
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Greece
        - Greece:
          - CapitalsControlled:
            - Gao
            - Babylon
            - Carthage
            - Athens
            - Addis Ababa
          - CapitalsPercentage: 62
        
        ## ScienceVictory
        - Babylon:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Carthage:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Ethiopia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Greece:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - Japan:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Mongolia:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        - Songhai:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 0
        - The Ottomans:
          - PartsPercentage: 0
          - PartsCompleted: 0
          - ApolloComplete: 1
        
        ## CulturalVictory
        - CivsNeeded: 7
        - Contender: Ethiopia
        - Babylon:
          - Influences:
            - Mongolia: Exotic (19%) - Rising Slowly (tourism/culture ratio 25%)
            - Greece: Exotic (12%) - Rising Slowly (tourism/culture ratio 20%)
            - Songhai: Exotic (21%) - Rising Slowly (tourism/culture ratio 45%)
            - Carthage: Familiar (36%) - Rising Slowly (tourism/culture ratio 95%)
            - Ethiopia: Exotic (11%) - Rising Slowly (tourism/culture ratio 106%)
            - Japan: Exotic (24%) - Rising Slowly (tourism/culture ratio 49%)
            - The Ottomans: Familiar (32%) - Rising (299 turns to Influential, tourism/culture ratio 2581%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        - Carthage:
          - Influences:
            - Mongolia: Exotic (6%) - Rising Slowly (tourism/culture ratio 9%)
            - Songhai: Exotic (7%) - Rising Slowly (tourism/culture ratio 18%)
            - Greece: Exotic (5%) - Rising Slowly (tourism/culture ratio 8%)
            - Babylon: Exotic (10%) - Rising Slowly (tourism/culture ratio 31%)
            - Japan: Exotic (7%) - Rising Slowly (tourism/culture ratio 18%)
            - The Ottomans: Exotic (10%) - Rising Slowly (tourism/culture ratio 903%)
          - PolicyPercentage: 92
          - InfluentialCivs: 0
        - Ethiopia:
          - Influences:
            - Mongolia: Popular (89%) - Rising Slowly (tourism/culture ratio 62%)
            - Greece: Popular (75%) - Rising Slowly (tourism/culture ratio 47%)
            - Songhai: Influential (101%) - Rising (tourism/culture ratio 87%)
            - Carthage: Dominant (237%) - Rising (tourism/culture ratio 307%)
            - Babylon: Influential (110%) - Rising (tourism/culture ratio 174%)
            - Japan: Influential (106%) - Rising (tourism/culture ratio 120%)
            - The Ottomans: Influential (125%) - Rising (tourism/culture ratio 5843%)
          - PolicyPercentage: 100
          - InfluentialCivs: 5
        - Greece:
          - Influences:
            - Mongolia: Familiar (37%) - Rising Slowly (tourism/culture ratio 30%)
            - Babylon: Influential (141%) - Rising (tourism/culture ratio 613%)
            - Songhai: Popular (72%) - Rising (22 turns to Influential, tourism/culture ratio 334%)
            - Carthage: Dominant (268%) - Rising (tourism/culture ratio 1042%)
            - Ethiopia: Familiar (45%) - Rising (137 turns to Influential, tourism/culture ratio 443%)
            - Japan: Familiar (45%) - Rising Slowly (tourism/culture ratio 91%)
            - The Ottomans: Popular (55%) - Rising (34 turns to Influential, tourism/culture ratio 8260%)
          - PolicyPercentage: 100
          - InfluentialCivs: 2
        - Japan:
          - Influences:
            - Mongolia: Popular (70%) - Rising (156 turns to Influential, tourism/culture ratio 134%)
            - Greece: Exotic (19%) - Rising Slowly (tourism/culture ratio 36%)
            - Songhai: Familiar (37%) - Rising Slowly (tourism/culture ratio 87%)
            - Carthage: Popular (85%) - Rising (21 turns to Influential, tourism/culture ratio 257%)
            - Ethiopia: Exotic (23%) - Rising (374 turns to Influential, tourism/culture ratio 283%)
            - The Ottomans: Popular (68%) - Rising (27 turns to Influential, tourism/culture ratio 7624%)
            - Babylon: Familiar (49%) - Rising (193 turns to Influential, tourism/culture ratio 176%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Mongolia:
          - Influences:
            - Babylon: Popular (78%) - Rising (25 turns to Influential, tourism/culture ratio 313%)
            - Greece: Familiar (32%) - Rising Slowly (tourism/culture ratio 62%)
            - Songhai: Popular (54%) - Rising (226 turns to Influential, tourism/culture ratio 139%)
            - Carthage: Influential (139%) - Rising (tourism/culture ratio 434%)
            - Ethiopia: Familiar (38%) - Rising (134 turns to Influential, tourism/culture ratio 489%)
            - Japan: Influential (132%) - Rising (tourism/culture ratio 432%)
            - The Ottomans: Influential (113%) - Rising (tourism/culture ratio 13023%)
          - PolicyPercentage: 100
          - InfluentialCivs: 3
        - Songhai:
          - Influences:
            - Mongolia: Familiar (30%) - Rising Slowly (tourism/culture ratio 46%)
            - Greece: Exotic (19%) - Rising Slowly (tourism/culture ratio 39%)
            - Babylon: Popular (58%) - Rising (123 turns to Influential, tourism/culture ratio 192%)
            - Carthage: Popular (54%) - Rising (93 turns to Influential, tourism/culture ratio 218%)
            - Ethiopia: Exotic (20%) - Rising (868 turns to Influential, tourism/culture ratio 191%)
            - Japan: Familiar (37%) - Rising Slowly (tourism/culture ratio 97%)
            - The Ottomans: Popular (58%) - Rising (48 turns to Influential, tourism/culture ratio 5901%)
          - PolicyPercentage: 88
          - InfluentialCivs: 0
        - The Ottomans:
          - Influences:
            - Mongolia: Familiar (26%) - Rising Slowly (tourism/culture ratio 27%)
            - Greece: Exotic (10%) - Rising Slowly (tourism/culture ratio 11%)
            - Songhai: Exotic (21%) - Rising Slowly (tourism/culture ratio 31%)
            - Carthage: Familiar (38%) - Rising Slowly (tourism/culture ratio 59%)
            - Ethiopia: Exotic (14%) - Rising Slowly (tourism/culture ratio 100%)
            - Japan: Familiar (35%) - Rising Slowly (tourism/culture ratio 59%)
            - Babylon: Familiar (30%) - Rising Slowly (tourism/culture ratio 49%)
          - PolicyPercentage: 96
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 45
        - Status: World Congress - Voting in 1 turn
        - ActiveResolutions:
          - Casus Belli:
            - Description: The world recognizes the need for justifiable war to resolve diplomatic disputes.
              While this resolution is active, unit maintenance costs are lowered by 15% Gold. 0.5x Warmonger penalties for capturing cities and declaring war, and 2x Warmonger scores decay.
            - EnactedOn: 330
          - Greek Sphere of Influence: Copenhagen:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 393
          - Cultural Heritage Sites:
            - Description: Each World Wonder provides +2 Culture to its city, and each Great Work provides +1 Science to its city.
            - EnactedOn: 330
          - Greek Sphere of Influence: Monaco:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 360
          - Open Door: Budapest:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 330
          - Mongolian Sphere of Influence: Buenos Aires:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 382
          - Ethiopian Sphere of Influence: Vatican City:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 349
          - Open Door: Almaty:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 330
          - Sanction: Babylon:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 330
          - Sanction: Greece:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 393
          - Greek Sphere of Influence: Antananarivo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 382
          - Mongolian Sphere of Influence: Hanoi:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 349
          - Ottoman Sphere of Influence: Salem:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 393
          - Open Door: Abernethy:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 330
          - World Ideology: Order:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: 439
          - Mongolian Sphere of Influence: Antwerp:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 360
          - World Religion: Eastern Orthodoxy:
            - Description: Designate a religion as the official World Religion. Civilizations who have a majority of the cities in their empire following the religion get an additional Delegate. The founder of the religion and/or the controller of its Holy City receives additional votes based on the number of Civilizations following the religion. The religion spreads 25% faster, and its Holy City receives +50% Tourism. There can only be one World Religion at a time.
            - EnactedOn: 330
        - Proposals:
          - Enact: Global Hegemony:
            - Description: Designate a player that could achieve Global Hegemony. If a Civilization receives support from enough Delegates in the Congress, that leader will attain Diplomatic Victory. The number of Delegates needed depends on the number of Civilizations and City-States in the game, and can be seen on the World Congress screen.
              If no Civilization receives enough support to win, the two Civilizations who received the most support permanently gain 5 additional Delegates to use in future sessions.
              May not be proposed by a Civilization. Automatically proposed at regular intervals once a World Ideology Resolution is active.
            - Proposer: Unknown
        - Contender: Greece
        - Babylon:
          - Delegates: 13
          - VictoryPercentage: 28
        - Carthage:
          - Delegates: 11
          - VictoryPercentage: 24
        - Ethiopia:
          - Delegates: 16
          - VictoryPercentage: 35
        - Greece:
          - Delegates: 48
          - VictoryPercentage: 106
        - Japan:
          - Delegates: 10
          - VictoryPercentage: 22
        - Mongolia:
          - Delegates: 16
          - VictoryPercentage: 35
        - Songhai:
          - Delegates: 12
          - VictoryPercentage: 26
        - The Ottomans:
          - Delegates: 16
          - VictoryPercentage: 35
        
        # Briefings
        ## Military Briefing
        **MILITARY INTELLIGENCE – TURN 449**  
        *Prepared for Genghis Khan – Mongolia (Player 5)*  
        
        ---
        
        ### 1. Recent Operational Changes (Turn 448‑449)
        
        | Category | New / Completed | Effect on Force Posture |
        |----------|----------------|--------------------------|
        | **Naval** | **Battleship** (Kar‑Korum) – built and trained | Provides a capital‑ship platform for power projection; still un‑escorted (no Destroyer). |
        | **Air** | **Mobile SAM** (Beshbalik) – produced and promoted (Shock I, Amphibious, Woodsman) | Improves anti‑air defence for the Beshbalik zone and coastal approaches. |
        | | **Bazooka** (Turfan) – produced, upgraded to Accuracy III | Boosts anti‑armor firepower in the Turfan sector. |
        | | **Great Writer** – created in Hsia (cultural boost, no combat effect) |
        | | **Caravans** – three new trade units (Kar‑Korum, Mongolia) | Enhances logistics and gold inflow; no immediate combat impact. |
        | **Ground** | **Bazooka** (additional, upgraded from Machine Gun) – placed in Hsia | Further reinforces anti‑armor capability near the front with Greece. |
        | | **Special Forces** – one new unit (ID 20383) created and upgraded from Paratrooper | Increases paradrop and elite‑attack capacity. |
        | | **Mobile SAM** – promotion (Shock I, Amphibious, Woodsman) | Enhances mobility and terrain flexibility for anti‑air units. |
        | **Technology** | No new tech unlocked this turn (still at Tech 72 – Jet Fighter ready but not yet produced). |
        | **Economy** | Treasury down to ~ 209 G (≈ 20 G spent on new units). Gold/turn ~ 576 (slight decline). Supply full at 95/≈ 95. |
        | **Combat** | No Mongolian‑initiated combat this turn. The only kill reported in the previous turn (Attack Submarine vs. Carthage Landship) remains the most recent engagement. |
        
        *Net effect:* modest increase in elite ground units and anti‑air assets; completion of a Battleship adds strategic naval weight but also highlights the continuing lack of surface escort.
        
        ---
        
        ### 2. Force Posture – Tactical Zones (Turn 449)
        
        | Zone (City) | Dominance | Key Mongolian Assets (post‑turn) |
        |-------------|-----------|-----------------------------------|
        | **Karakorum (1062)** | Friendly | 2 Stealth Bombers, 1 Modern Armor, 1 Tank, 1 Special Forces, 2 Bazookas, 2 Mobile SAM, 1 Machine Gun, 1 Battleship (new). |
        | **Beshbalik (1180)** | Friendly | 1 Modern Armor, 4 Mobile SAM (incl. promoted unit), 3 Mechanized Infantry, 1 Tank, 1 AA, 5 MG, 1 Artillery, 1 Atomic Bomb (completed), 1 Special Forces. |
        | **Turfan (1857)** | Friendly | 1 Mechanized Infantry, 1 Special Forces, 1 Bazooka (up‑graded), 1 Mobile SAM, 1 Infantry. |
        | **Hsia (2045)** | Friendly | 1 Modern Armor, 1 Bazooka (new), 1 Mobile SAM, 2 AA, 1 Special Forces, 1 Mechanized Infantry, 1 Great Writer (non‑combat). |
        | **Old Sarai (2403 – Sea‑zone)** | Friendly | 2 Battleships (Mongolia), 2 Fighters, 2 Mobile SAM, 2 Special Forces, 1 Attack Submarine (Veligrad), 1 Sensor Combat Ship (Greece). |
        | **New Sarai (3272)** | Friendly | 4 Modern Armor, 2 Helicopter Gunships, 2 Mobile SAM, 5 Mechanized Infantry, 5 Bazookas, 4 Artillery, 6 MG, 2 Light Tanks, 3 Heavy Bombers, 3 Fighters, 1 Special Forces. |
        | **Veligrad (1071)** | Friendly | 3 Modern Armor, 1 Mechanized Infantry, 1 AA, 1 Special Forces, 1 Attack Submarine (city‑state). |
        | **Wanggeom (1072)** | Friendly | 2 Modern Armor (city‑state), 1 Light Tank (city‑state), 3 Infantry (city‑state), 1 Machine Gun (city‑state), 2 Modern Armor (Mongolia), 1 Machine Gun (Mongolia), 1 Bazooka (Mongolia). |
        | **Antwerp (1080)** | Friendly | 1 Mobile SAM (Mongolia), 2 Mechanized Infantry (Mongolia), 1 Battleship (Mongolia), 1 Battleship + 3 Fleet Destroyers (city‑state). |
        | **Hanoi (1074 – Sea‑zone)** | Friendly | 1 Mobile SAM (Mongolia), 1 Modern Armor (city‑state), 1 Fighter (city‑state), 2 Light Tanks (city‑state), 3 Infantry (city‑state), 1 Machine Gun (city‑state). |
        | **Other City‑States** | Mixed (mostly hostile) | Minimal Mongolian presence (mostly SAMs, a few support units). |
        
        *Overall unit count remains around **100**; the composition now includes **1 Battleship**, **3 Special Forces**, **3 Bazookas**, and **2 Mobile SAMs** with promotions.*
        
        ---
        
        ### 3. Threat Assessment – Current (Turn 449)
        
        | Opponent | Relation / War | Relative Strength* | Recent Activity | Threat Level |
        |----------|----------------|-------------------|----------------|--------------|
        | **Greece** | War (our score ‑8 %) | 22 294 MS vs 61 029 MS (Mongolia) | • Modern Armor near Sparta (enemy zone 1181).<br>• Fighter & Bomber units at Corinth & Athens.<br>• No direct clash this turn, but Greek air‑ground forces remain active near our frontiers. | **High** – only opponent capable of challenging our naval capital and contesting airspace. |
        | **Ottomans** | Defensive Pact (Close) | 18 145 MS vs 61 029 MS | Strong naval fleet (Battleships, Destroyers) patrolling; no combat. | **Secure** – provides indirect protection against Greek sea threat. |
        | **Japan** | Defensive Pact (Neighbor) | 22 050 MS vs 61 029 MS | Joint air presence; Japanese units in many friendly zones. | **Secure** – contributes air and naval depth. |
        | **Carthage** | War (our score +42 %) | 1 250 MS vs 61 029 MS | Mongolian Attack Submarine destroyed Carthage Landship (last turn). | **Low** – negligible offensive capability. |
        | **Songhai** | War (our score 0 %) | 5 117 MS vs 61 029 MS | No visible units; zones remain friendly/neutral. | **Negligible** |
        | **Babylon** | War (our score 0 %) | 2 387 MS vs 61 029 MS | Minor paratrooper presence; no combat. | **Very Low** |
        | **Hostile City‑States** (Riga, Monaco, Zurich, Manila, Copenhagen, Antananarivo, Budapest, Buenos Aries, Vatican) | War (peace blocked) | Combined ≈ 7 800 MS | Static low‑level forces; no recent engagements. | **Very Low** |
        | **Ethiopia** | Open Borders (no war) | 1 034 MS vs 61 029 MS | No activity. | **None** |
        
        \*Strength values are from player summaries; they reflect total military strength, not zone‑specific forces.
        
        **Key Points**
        
        * **Air superiority remains the principal gap** – 2 Fighters cannot guarantee bomber escort or counter Greek air assets.
        * **Surface escort for the Battleship is still missing** – no Destroyer or Cruiser to protect against Greek fast‑attack units.
        * **Strategic nuclear weapons are now operational** and provide a deterrent, especially against Greece.
        * **Ground forces are modestly reinforced** (new Special Forces, Bazookas, promoted Mobile SAM) but still limited for a large‑scale offensive against Greece.
        * **Allied naval power (Ottomans) is strong**, but without a Destroyer our Battleship is exposed if the Ottomans shift focus.
        
        ---
        
        ### 4. Capability Gaps & Over/Under‑Utilisation (Turn 449)
        
        | Capability | Current Level | Gap / Surplus |
        |------------|----------------|----------------|
        | **Strategic Bombing** | 4 Heavy Bombers, 2 Atomic Bombs | **Surplus** – ample for conventional and nuclear strikes. |
        | **Air Superiority** | 2 Fighters (no Jets yet) | **Deficit** – cannot guarantee bomber escort; immediate need for **Jet Fighters** (available tech). |
        | **Naval Surface Power** | 1 Battleship, 2 Fleet Destroyers, **0 
        
        ## Economy Briefing
        **MONGOLIA – Economic Briefing (Turn 449)**  
        *Macro‑level snapshot for Genghis Khan. All figures are taken directly from the current game state; no speculation or recommendations are included.*
        
        ---
        
        ## 1. Treasury & Cash Flow  
        
        | Metric | Turn 449 | Turn 444 (previous briefing) | Δ vs 444 | Comment |
        |--------|----------|------------------------------|----------|---------|
        | **Gold in Treasury** | **154 G** | 209 G | **‑55 G** | Treasury fell despite a net gold surplus because the previous turn’s surplus was modest and the Golden Age is ending (5 turns remaining). |
        | **Net Gold / turn** | **+383 G** | +576 G | **‑193 G** | The drop is mainly due to: <br>• The Japanese oil‑for‑gold side‑deal (3 Oil ↔ 23 Gold) is now at **‑1 turn** and will expire after the next turn. <br>• Upkeep rose as the new **Mobile SAM** and **Bazooka** units entered service. |
        | **Gross Gold / turn (income)** | ≈ 1 020 G* | ≈ 1 180 G | **‑160 G** | Loss of the Japanese oil‑for‑gold income (≈ 23 G/turn) and a small decline in trade‑route gold (see §2). |
        | **Gold / turn (maintenance)** | ≈ ‑637 G* | ≈ ‑604 G | **‑33 G** | Additional unit upkeep (Mobile SAM, Bazooka, extra Special Forces) and the start of an **Attack Submarine** production (higher ship maintenance). |
        
        \*Exact gross/maintenance breakdown is not exported; figures are derived from the reported *Gold Per Turn* (383 G net) and the known treasury change.
        
        ---
        
        ## 2. Trade‑Route Income (Gold per turn)
        
        | Origin → Destination | Current Gold / turn | Change since Turn 444 |
        |----------------------|--------------------|------------------------|
        | Karakorum → Osaka (Japan) | **+11 G** | unchanged |
        | Karakorum → Kyoto (Japan) | **+11 G** | unchanged |
        | Karakorum → Nagoya (Japan) | **+11 G** | unchanged |
        | Karakorum → Kagoshima (Japan) | **+9 G** | unchanged |
        | Karakorum → Tokyo (Japan) | **+11 G** | unchanged |
        | Karakorum → Veligrad (CS) | **+8.75 G** (science) | unchanged |
        | Karakorum → Wanggeom (CS) | **+8.75 G** (science) | unchanged |
        | Karakorum → Antwerp (CS) | **+8.75 G** (science) | unchanged |
        | Karakorum → Hanoi (CS) | **+8.75 G** (science) | unchanged |
        | Karakorum → Almaty (CS) | **+6.88 G** (gold) | unchanged |
        | **Incoming (Japan → Kyoto)** | **+18.87 G** | unchanged |
        | **Incoming (Ottomans → Old Sarai)** | **+9 G** | unchanged |
        | **Total net trade‑route gold** | **≈ +71 G/turn** | unchanged |
        
        **Side‑deal impact:** The *oil‑for‑gold* deal with Japan (3 Oil ↔ 23 Gold per turn) expires after Turn 450, removing a **+23 G/turn** boost and turning the oil flow into a net deficit (see §5).
        
        ---
        
        ## 3. Unit‑Related Upkeep  
        
        | Unit type (representative) | Approx. quantity* | Approx. upkeep (G/turn) |
        |----------------------------|-------------------|--------------------------|
        | Helicopter Gunship | 1 | –6 G |
        | Mobile SAM | 1 | –6 G |
        | Bazooka (Ranged) | 2 (new) | –12 G |
        | Special Forces (Paradrop) | 2 (new) | –12 G |
        | Attack Submarine (under construction) | 1 (started) | –12 G (future) |
        | Remaining land forces (infantry, tanks, etc.) | ~ 90 | –≈ 530 G |
        | **Total upkeep** | –≈ ‑637 G | matches net‑gold figure |
        
        *Quantity is inferred from the event log and the total military strength; exact counts are not exported.
        
        ---
        
        ## 4. Technology & Policy Progress  
        
        | Item | Current status (Turn 449) | Economic relevance |
        |------|---------------------------|--------------------|
        | **Lasers** (research) | **≈ 15 turns left** (current research) | Will unlock **Laser** units and **Advanced Energy** buildings (future gold/production boost). |
        | **Alternative Energy** (research) | 14 turns left (unchanged since Turn 444) | Prerequisite for **Nuclear Power** (requires oil + uranium). |
        | **Industrialism** (Policy) | 5 turns left to next policy slot (down from 11 at Turn 444) | When adopted will add +2 % gold/production. |
        | **Future Tech – Robotics** | Not yet researched | Unlocks **Robotics Factory** (high production). |
        | **Future Tech – Future** | Unlocked | Enables late‑game buildings (Future Museum/Factory) that raise gold, tourism, and science. |
        
        **Key bottleneck:** No Uranium on hand; without it Nuclear Power cannot be pursued even when oil is secured.
        
        ---
        
        ## 5. Resource Stockpile (Strategic & Luxury)
        
        | Resource | Qty (Turn 449) | Change since Turn 444 | Note |
        |----------|----------------|-----------------------|------|
        | **Aluminum** | 11 | –4 | Still sufficient for current air units; future air‑force expansion will need more. |
        | **Oil** | 4 (stock) + **3 /t incoming** from Japan (expires after Turn 450) | +4 stock, new incoming flow (previously none) | Critical strategic resource; loss of Japanese deal will create a **‑3 /t** deficit. |
        | **Uranium** | 0 | unchanged | No nuclear options until a new source is secured. |
        | **Coal** | 4 | unchanged | Supports current industry. |
        | **Olives** | 8 | unchanged | Frequently used in diplomatic trades (Ottomans, Ethiopia). |
        | **Pearls** | 1 | –1 (used in a Japan trade) | Still part of a small gold‑for‑pearl deal with Japan. |
        | **Whales** | 1 | unchanged | Generates gold via Ottoman trade. |
        | **Luxuries (Salt, Coffee, etc.)** | 1‑2 each | unchanged | No shortages; all tied to active deals. |
        
        **Bottom line:** Oil is the only strategic resource whose availability is precarious. Uranium remains absent.
        
        ---
        
        ## 6. City‑Level Economic Health (Key Cities)
        
        | City | Gold / turn | Science / turn | Production / turn | Current Project (turns left) |
        |------|-------------|----------------|-------------------|------------------------------|
        | **Karakorum (Capital)** | **+1 108 G** | +377 S | +693 P | **Carrier** (2 t → 1 t) – finishing this turn. |
        | **Beshbalik** | +155 G | +238 S | +447 P | **Special Forces** (2 t). |
        | **Turfan** | +207 G | +239 S | +374 P | **Rocket Artillery** (4 t). |
        | **Hsia** | +208 G | +238 S | +311 P | **Special Forces** (1 t). |
        | **Old Sarai** (coastal) | +140 G | +184 S | +251 P | **Solar Power Plant** (1 t). |
        | **New Sarai** | +137 G | +178 S | +326 P | **Hydroelectric Power Plant** (2 t). |
        | **Overall empire** | **≈ +4 500 G** (gross) | **≈ +1 530 S** | **≈ +2 500 P** | Net gold aligns with the reported **+383 G/turn** after upkeep. |
        
        All major cities remain net‑gold‑positive. Production is heavily allocated to late‑game military units (Carrier, Special Forces, Rocket Artillery) and energy infrastructure (Solar, Hydro). The capital continues to be the primary gold engine thanks to the **National Intelligence Agency** and **Customs House**.
        
        ---
        
        ## 7. Settlement Opportunities  
        
        | Coordinates | Quality | Distance from existing cities | Remarks |
        |-------------|---------|------------------------------|---------|
        | **29, 12** | **100 %** (best available) | 34 tiles from Karakorum; 6 tiles from Babylon; on a **new continent** | High‑yield plot, likely rich in multiple resources. Offers a foothold on a fresh landmass and a solid economic boost. |
        | **53, 38** | 0 % | 4 tiles from Karakorum | No resources, low yields – settlement would strain happiness. |
        | **53, 39** | 0 % | 4 tiles from Karakorum | Same as above. |
        | **54, 39** | 0 % | 4 tiles from Karakorum | Same as above. |
        | **26, 11** (not listed in current best‑settlement list) | – | – | No high‑quality plots other than (29, 12). |
        
        **Economic implication:** Settling **(29, 12)** would provide a significant long‑term cash flow (additional tile yields, possible luxury/strategic resources) while the other four plots would be net‑negative due to lack of yields and extra happiness costs.
        
        ---
        
        ## 8. Comparison to Turn 444  
        
        | Area | Turn 444 | Turn 449 | Δ (449‑444) |
        |------|----------|----------|--------------|
        | **Gold Treasury** | 209 G | 154 G | –55 G |
        | **Net Gold/turn** | +576 G | +383 G | –193 G |
        | **Gross Gold/turn** | ≈ 1 180 G | ≈ 1 020 G | –160 G |
        | **Gold upkeep** | ≈ ‑604 G | ≈ ‑637 G | –33 G |
        | **Oil** | 0 stock, **no incoming** | 4 stock + **3/t incoming** (expires soon) | +4 stock, new inflow (temporary) |
        | **Uranium** | 0 | 0 | unchanged |
        | **Policy turns left** | 11 | 5 | –6 (policy progress accelerated) |
        | **Research – Lasers** | Not yet started | ≈ 15 t left | New research focus |
        | **Key projects** | Capital finishing **Atomic Bomb**; Beshbalik on **Apollo** | Capital finishing **Carrier**; Beshbalik on **Special Forces** | Production shifted toward naval & airborne units |
        | **Settlement** | No viable high‑quality plots | One 100 % plot (29,12) appears | New expansion option |
        | **Unit composition** | Added Special Forces, Helicopter Gunship | Added **Mobile SAM**, **Bazooka**, extra **Special Forces** | Slight upkeep increase |
        
        **Overall assessment**
        
        * **Treasury & cash flow** have contracted because the lucrative Japanese oil‑for‑gold side‑deal is about to end and new unit upkeep has risen.  
        * **Gold income** remains healthy but is now ~14 % lower than three turns ago; the empire is still net‑gold‑positive, but the margin has narrowed.  
        * **Oil** is temporarily secured but will become a deficit once the Japanese deal expires, creating an urgent need for an alternative source (new trade, conquest, or a city‑state deal).  
        * **Uranium** is still absent, keeping nuclear options out of reach.  
        * **Policy progress** is faster (5 turns left vs. 11), positioning us to adopt the next policy soon.  
        * **Settlement**: the newly identified high‑quality tile at (29, 12) on a new continent offers a solid long‑term economic gain; the other candidate plots are not worth the happiness cost.  
        * **Production** focus has moved toward naval power (Carrier, upcoming Submarine) and advanced ranged units (Bazooka, Mobile SAM), reflecting a shift from pure atomic‑bomb development to a more balanced modern army.
        
        *Prepared for Genghis Khan – Turn 449.*
        
        ## Diplomacy Briefing
        **Diplomatic Intelligence Brief – Turn 449**  
        *Leader: Genghis Khan – Mongolia (Player 5)*  
        
        ---
        
        ### 1. World Congress – Current Landscape
        - **Voting in 1 turn (Turn 450).** 45 delegates are required for a resolution.
        - **Active Resolutions** (all remain in effect):
          - *Casus Belli* – reduced unit maintenance, warmonger penalties cut.
          - *Greek Sphere of Influence* (Copenhagen, Monaco, Antananarivo) – Greece holds permanent ally status over three city‑states.
          - *Mongolian Sphere of Influence* (Buenos Aires, Hanoi, Antwerp) – Mongolia already has permanent ally status over three city‑states, each granting **+4 delegates** (total **+12**).
          - *Open Door* (Budapest, Abernethy, Almaty) – all civs fixed at 40 influence with these city‑states; no new spheres can be created there.
          - *World Ideology: Order* – Order is the global ideology, granting additional delegates to Order followers.
          - *World Religion: Eastern Orthodoxy* – minor effect on culture/science, no diplomatic impact.
          - *Sanctions* – Babylon and Greece are sanctioned (no trade/corporations, warmonger penalty halved).
        
        - **Delegate Counts (Current Turn 449):**  
        
        | Civ | Delegates | Victory % | Notes |
        |-----|-----------|----------|-------|
        | Greece | **48** | 106 % | Holds a peace treaty with Mongolia; however, both sides have denounced each other and are ideological opponents (Order vs. Autocracy). |
        | Mongolia | **16** | 35 % | Gains **+12** delegates from three secured spheres (Buenos Aires, Hanoi, Antwerp). |
        | Ethiopia | **16** | 35 % | Open‑borders, denounced each other, trading gold for resources. |
        | Babylon | **13** | 28 % | War, sanctions, declared friendship but hostile relations. |
        | Ottomans | **16** | 35 % | Defensive pact, open borders, friendly. |
        | Japan | **10** | 22 % | Open borders, friendly, shares autocracy. |
        | Songhai | **12** | 24 % | War, denounced. |
        | Carthage | **11** | – | War, denounced. |
        | Others (e.g., Turkey, etc.) – not listed, totals irrelevant for the upcoming vote. |
        
        - **Contender for Global Hegemony:** **Greece** (already on track with 48 delegates). No other civ currently has enough support.
        
        ### 2. Major Diplomatic Developments Since Turn 444
        | Civ | Change | Current Status |
        |-----|--------|----------------|
        | **Greece** | Peace Treaty signed (Turn 447) – now “Peace Treaty” but still **denounced** each other; still an Order ally. | Close neighbor, no open borders, hostile ideology. |
        | **Babylon** | Ongoing war (Mongolia ↔ Babylon) with Mongolia holding a **Declaration of Friendship** but also **Sanction** active. | War weariness low (5 %). |
        | **The Ottomans** | Defensive pact and open borders **maintained**; both civs share a **public Declaration of Friendship**. | Close neighbor, friendly. |
        | **Japan** | Open borders and public friendship **maintained**; shared autocracy. | Neighbor, friendly. |
        | **Ethiopia** | Open borders **maintained**; multiple gold‑for‑resource deals (coal, olives, gold per turn). No defensive pact yet. | Distant, denounced each other, but Ethiopia is *at war with Greece* – a potential leverage point. |
        | **City‑States** | Mongolia retains **permanent ally** status over Buenos Aires, Hanoi, Antwerp (secure +12 delegates). No new “Open Door” proposals have passed that would lock Ethiopia’s influence. |
        | **Espionage** | Mongolian spies active in Songhai (Kukia), Ottoman‑owned Bursa, and Greek cities (Borsippa, Sparta, Athens). No counter‑espionage reported. |
        | **Trade** | Gold‑for‑resource streams from Ethiopia and Japan continue; trade routes with Japan and the Ottomans generate high gold and science. |
        | **Religion** | Mongolia’s state religion remains **Tengriism**; no city‑state has adopted it yet, except Salem (quest to become majority – 1 turn left). |
        
        ### 3. City‑State Influence – Immediate Voting Power
        | City‑State | Current Influence (Mongolia) | Status | Delegates contributed |
        |-----------|-----------------------------|--------|-----------------------|
        | **Buenos Aires** | Ally (Sphere) | Permanent ally – 4 delegates |
        | **Hanoi** | Ally (Sphere) | Permanent ally – 4 delegates |
        | **Antwerp** | Ally (Sphere) | Permanent ally – 4 delegates |
        | **Riga** | Neutral (‑58) | No influence, no ally |
        | **Monaco** | Friend (237) | Not an ally; 0 delegates |
        | **Salem** | Friend (55) | Not an ally; 0 delegates |
        | **Zurich** | Friend (41) | Not an ally; 0 delegates |
        | **Manila** | Neutral (‑44) | No influence |
        | **Copenhagen** | Friend (78) | Not an ally (Greek sphere active) |
        | **Veligrad** | Ally (359) | Permanent ally – 4 delegates |
        | **Wanggeom** | Ally (1081) | Permanent ally – 4 delegates |
        | **Almaty** | Friend (263) | Not an ally (Open Door active) |
        | **Budapest** | Friend (57) | Not an ally (Open Door active) |
        | **Others** (Abernethy, etc.) | ≤ 100 influence, no sphere – 0 delegates |
        
        **Total delegate gain from spheres:** **+12** (already reflected in Mongolia’s 16 delegates).
        
        ### 4. Shifts in Voting Outlook (Compared to Turn 444)
        | Metric | Turn 444 | Turn 449 | Δ |
        |--------|----------|----------|---|
        | Mongolia delegates | 16 (incl. 0 spheres) | 16 (incl. +12 from spheres) | +0 net (spheres added, but total delegate count unchanged due to resolution updates) |
        | Greece delegates | 47 | 48 | +1 (Greek sphere proposals granted) |
        | Ethiopia delegates | 15 | 16 | +1 (Ethiopia gained a delegate via its own internal changes) |
        | Total anti‑Greek block (Mongolia + allies) | ≈ 50 | ≈ 54 (Mongolia + Ethiopia + Ottomans + Japan) | +4 |
        | Greek block (Greece + Order allies) | ≈ 63 | ≈ 64 (Greece + Babylon + Carthage) | +1 |
        
        **Key change:** Mongolia has **secured three permanent spheres** (Buenos Aires, Hanoi, Antwerp) since the last briefing, providing a reliable 12‑delegate swing. Greece has added a single delegate (now 48) via its own sphere proposals. No new anti‑Greek allies have been converted.
        
        ### 5. Diplomatic Levers – Current Viability
        | Target Civ / City‑State | Potential Leverage | Current Feasibility |
        |--------------------------|-------------------|----------------------|
        | **Ethiopia (15 delegates)** | • Convert open‑borders into a **Sphere of Influence** (already eligible – Steam Power discovered). <br>• Increase gold‑for‑resource deals into **gold‑for‑influence** (e.g., add a permanent +5 influence per turn). | **High** – Ethiopia is already *at war with Greece*, hostile to the Greek bloc. No ideological barrier (Order vs. Autocracy) for a sphere; only need to raise influence ≥ 40. |
        | **Babylon (12 delegates)** | • Peace treaty & removal of sanctions → then propose a sphere. | **Low** – Ongoing war, opposing Order ideology, and sanctions make a sphere unlikely before the vote. |
        | **Ottomans (16 delegates)** | Already a **defensive pact** and open borders; can be upgraded to a **sphere** (requires current ally status – not yet). | **Medium** – Friendly but not an ally; a sphere would add +4 delegates. However, the Ottomans already contribute a solid diplomatic buffer and are unlikely to shift alliances before the vote. |
        | **Japan (10 delegates)** | Similar to Ottomans; could be upgraded to a sphere. | **Medium‑Low** – Already shares autocracy but no ally status; sphere proposal possible but limited impact. |
        | **Remaining Open‑Door city‑states** (Budapest, Abernethy, Almaty) | Prevent further “Open Door” proposals that would lock influence at 40 and block sphere creation. | **Critical** – Maintain current status; no new Open‑Door resolutions have been proposed. |
        | **Greek‑aligned city‑states** (Copenhagen, Monaco, Antananarivo) | No realistic path to flip; Greece holds permanent ally status. | **None** – Locked by Greek sphere resolutions. |
        
        ### 6. Immediate Recommendations for Diplomatic Weighting
        1. **Prioritise Ethiopia** – allocate weight to actions that raise influence (gold‑for‑influence, gifts of olives/coal) and then submit the *Mongolian Sphere of Influence: Ethiopia* proposal (already permitted). Success would convert Ethiopia into a permanent ally (+15 delegates), pushing the anti‑Greek block above the threshold.  
        2. **Maintain pressure on Greece’s Order allies** – keep the *Sanction: Babylon* active, continue antagonistic voting in the United Nations, and use espionage to monitor any shifts among Greek delegates.  
        3. **Solidify existing spheres** – ensure no diplomatic actions (e.g., Open‑Door proposals) undermine Buenos Aires, Hanoi, or Antwerp.  
        4. **Leverage trade and espionage** – the high‑gold trade routes with Japan and the Ottomans provide economic leverage; consider modest gold‑for‑influence swaps with the Ottomans to lock them as a sphere ally if needed.  
        5. **Watch for new “Open Door” proposals** – any new Open‑Door resolution on a city‑state where Mongolia seeks a sphere would freeze influence at 40, blocking a sphere.  
        
        ---
        
        **Bottom Line:** The decisive factor for the upcoming Global Hegemony vote is **Ethiopia**. Converting Ethiopia into a permanent ally would add **15 delegates** to Mongolia’s block, overtaking Greece’s 48‑delegate advantage and securing a diplomatic victory. All other major order‑aligned powers (Babylon, Carthage) remain locked in Greece’s camp; focus should remain on Ethiopia and preserving the three existing Mongolian spheres.
        
        You, Genghis Khan (leader of Mongolia, Player 5), are making strategic decisions after turn 449.
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
      
    - You are Genghis Khan, leader of Mongolia (Player 5).
      
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
      - Name: Mongolia
      - Uniques:
        - Unique Unit: Khan, Replacing Great General (Requires technology: None)
        - Unique Unit: Black Tug, Replacing Knight (Requires technology: Chivalry)
        - Unique Building: Ger, Replacing Smokehouse (Requires technology: Trapping)
        - Civilization Ability: Skirmisher Units have an extra Attack. Gain All Yields equal to 20% of the Gold from bullying City-States.
      - Leader: Genghis Khan
      - PlayerID: 5
      
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
      - Telecommunications: Allows you to build the Interpretive Center, boosting all Landmarks in empire.
        Completing it would unlock: Robotics, The Internet
      - Nuclear Fusion: Allows you to build the SS Booster, a component necessary to win a Science Victory.
        Completing it would unlock: Future Tech
      
      ## Policies
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Military-Industrial Complex (Level 1 Tenet of Ideology Autocracy): Military-Industrial Complex: -33% Gold cost of purchasing units. +3 Science from Defense Buildings, Citadels, Forts, and Unique Improvements.
      - Honor (Continuing Authority Branch):
        - * All Military Units gain the Conscription Promotion (+10% Combat Strength).
        - * Supply-free military Units spawn near Cities that reach (or have already reached) a multiple of 10 Citizens for the first time.
        - * -25% War Weariness.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Regimental System (Continuing Imperialism Branch):
        - * Earn Great Generals and Great Admirals 33% faster.
        - * Great Generals and Great Admirals gain the Regimental Traditions Promotion (+10% Leadership Combat Bonus and +1 Tile Radius).
        - * +2 additional copies of the unique Luxury Resources from expending Great Admirals for their Voyage of Discovery ability.
        - * Military Units can be upgraded in territory owned by Vassals and friendly City-States.
      - Civilizing Mission (Continuing Imperialism Branch):
        - * Retain all buildings from conquered Cities.
        - * Receive 75 Gold when you conquer a city, scaling with Era and City Population.
        - * +10% Production toward Buildings, with an additional +10% Production per Era difference between your current Era and the building's Era in all Puppeted Cities and Cities with a Courthouse.
      - Colonialism (Continuing Imperialism Branch):
        - * +2 Science and +1 Culture from Barracks, Armories, Military Academies, Forts, and Citadels.
        - * Each unique Global Monopoly modifier is increased by an additional 10% if it's percentage-based, or +3 otherwise.
      - Justice (Continuing Tradition Branch):
        - * +1 Production in every City.
        - * Cities with a garrison gain +25% Ranged Combat Strength.
        - * Royal Guardhouse built in Capital (+3 Production, +2 Defense, +50 Hit Points, +10% Military Supply from Population in all Cities, 1 Engineer Slot).
      - Equality (Continuing Progress Branch):
        - * +1 Happiness in every City and +1 Happiness for every 15 Citizens in a City.
        - * -1 Unhappiness from and Distress, Poverty, Illiteracy, and Boredom in all Cities.
      - Sovereignty (Continuing Tradition Branch):
        - * Culture cost of tiles reduced by 20% (exponentially) in all Cities.
        - * Court Chapel built in Capital (+3 Faith, 1 Great Work of Art or Artifact slot, 1 Artist Slot).
      - Organization (Continuing Progress Branch):
        - * +2 Production in every City.
        - * +25% Production toward Workers and Trade Units.
        - * +1 Movement for Workers.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Free Trade (Continuing Industry Branch):
        - * Earn Great Merchants 50% faster.
        - * +5 Gold from International Trade Routes.
        - * -2 Unhappiness from Poverty in all Cities.
      - Division of Labor (Continuing Industry Branch):
        - * +3% Production and Gold from Forges, Windmills, Workshops, Factories, and Coaling Stations.
        - * +100% Production towards Coaling Stations.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Nobility (Continuing Fealty Branch):
        - * +1 Happiness and +2 Gold from Castles.
        - * +2 Gold from Armories.
        - * +100% Production towards Castles and Armories.
      - Refinement (Continuing Artistry Branch):
        - * +2 Culture from Great Works of Art.
        - * 1 Specialist in all cities does not produce Unhappiness from Urbanization.
        - * +1 Culture from Specialists.
      - Fraternity (Continuing Progress Branch):
        - * +3 Food in every City.
        - * +3 Science from City Connections.
      - Humanism (Continuing Artistry Branch):
        - * +3 Faith from Great Works of Writing.
        - * -25% Golden Age Points needed to trigger a Golden Age.
        - * +1 Happiness from all Guilds.
  - decisions:
    - #0:
      - toolName: set-research
      - args:
        - Rationale: We need to continue researching advanced technologies like Nuclear Fusion to maintain our strategic and scientific edge, preparing for spaceship parts as a backup victory condition.
        - Technology: Nuclear Fusion
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Civilizing Mission
        - Rationale: Civilizing Mission will allow us to retain all buildings in conquered cities and receive gold upon conquest, which is perfect for our upcoming massive offensive campaign against Greece and its vassals.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -100
        - Rationale: Greece is our main competitor, leading in score and delegates, and close to a diplomatic victory. We must prepare to crush them completely as soon as our peace treaty expires.
        - Private: -100
        - TargetID: 6
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Ethiopia is actively at war with Greece and serves as a vital distraction and buffer. We must maintain friendly relations with them to keep the pressure on Greece.
        - Public: 50
        - Private: 50
        - TargetID: 7
    - #4:
      - toolName: set-persona
      - args:
        - Meanness: 9
        - DiplomaticBalance: 1
        - Forgiveness: 1
        - MinorCivWarBias: 8
        - WarBias: 10
        - DeceptiveBias: 1
        - HostileBias: 10
        - Boldness: 10
        - Rationale: We must maximize Genghis Khan's aggressiveness, boldness, and war drive. This will ensure the tactical AI aggressively builds up military forces and prepares for an all-out, relentless invasion of Greece and its vassals once the peace treaty expires.
        - WarmongerHate: 1
    - #5:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Nuke: 100
          - Ranged: 95
          - Diplomacy: 30
          - Science: 90
          - Mobile: 95
          - Defense: 10
          - Gold: 80
          - Mobilization: 100
          - Espionage: 90
          - Offense: 100
          - CityDefense: 20
          - MilitaryTraining: 100
          - UseNuke: 100
          - Air: 100
          - Production: 100
      - rationale: We pivot entirely to military mobilization, air superiority, and offensive warfare to prepare for a massive clash with Greece. Diplomacy is deprioritized as city-states are locked down by Greek spheres of influence, and resources are better spent on production and science.
  - tokens:
    - inputTokens: 27748
    - reasoningTokens: 5809
    - outputTokens: 460
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Victory Paths**
            
            I'm rapidly approaching the game's conclusion, turn 449 of 500. My current focus is evaluating our progress toward victory, particularly Domination, as Greece already holds a significant portion of the world's capitals.
            
            **Evaluating Victory Scenarios**
            
            My thoughts are now focused on the imminent World Congress vote on Turn 450. Greece is the primary rival, though our military vastly outclasses theirs. I need to confirm the details of the peace treaty with Greece and their vassals, as this impacts my strategic options for achieving a Domination victory while also keeping a close eye on the potential for a Diplomatic Victory.
            
            **Preventing Diplomatic Loss**
            
            I've just realized Greece has enough delegates for a Diplomatic Victory next turn! My immediate priority is to disrupt their delegate count. I'm urgently investigating ways to sway city-state alliances or influence before the crucial World Congress vote.
            
            **Disrupting Delegate Count**
            
            I'm re-evaluating our diplomatic standing. Greece's Sphere of Influence on key city-states restricts our direct influence. I'm now analyzing their vassals' delegate power, as those votes are automatically cast for Greece, bolstering their position in the upcoming World Congress.
            
            **Analyzing Delegate Totals**
            
            I'm scrutinizing Greece's delegate count, trying to ascertain if their 48 includes their vassals' votes or if those are separate. If they can win solo, my options are severely limited. I'm exploring how to influence the AI's voting behavior through relationships and flavors.
            
            **Exploring Alternative Victories**
            
            I'm now shifting my attention to potential Science Victories. Despite both Greece and the Ottomans having completed Apollo, my current research path seems to be Lasers, with Nuclear Fusion as the next step. I'm assessing if this aligns with a science win and reviewing available policies that might accelerate this.
            
            **Reviewing Policy Branches**
            
            I'm currently reviewing our open policy branches, noting that we have progress in several, including Imperialism and Autocracy. My focus is to determine which of these unfinished branches, particularly Imperialism, offers the most strategic advantage for achieving a Domination victory.
            
            **Assessing Diplomatic Setback**
            
            I'm re-evaluating our diplomatic standing. Greece's Sphere of Influence on key city-states restricts our direct influence. I'm now analyzing their vassals' delegate power, as those votes are automatically cast for Greece, bolstering their position in the upcoming World Congress.
            
            **Analyzing Delegate Totals**
            
            I'm scrutinizing Greece's delegate count, trying to ascertain if their 48 includes their vassals' votes or if those are separate. If they can win solo, my options are severely limited. I'm exploring how to influence the AI's voting behavior through relationships and flavors.
            
            **Exploring Alternative Victories**
            
            I'm now shifting my attention to potential Science Victories. Despite both Greece and the Ottomans having completed Apollo, my current research path seems to be Lasers, with Nuclear Fusion as the next step. I'm assessing if this aligns with a science win and reviewing available policies that might accelerate this.
            
            **Reviewing Policy Branches**
            
            I'm currently reviewing our open policy branches, noting that we have progress in several, including Imperialism and Autocracy. My focus is to determine which of these unfinished branches, particularly Imperialism, offers the most strategic advantage for achieving a Domination victory.
            
            **Identifying Ideological Focus**
            
            I'm prioritizing the Autocracy ideology, reviewing tenets like Lebensraum, Futurism, New World Order, Military-Industrial Complex, and Iron Fist to maximize our military and strategic capabilities for conquest.
            
            **Confirming Grand Strategy**
            
            My grand strategy remains Conquest as Mongolia. I am assessing if this aligns with our current ideological and military focus.
            
            **Realizing Strategic Constraint**
            
            I've just realized a critical constraint: a peace treaty with Greece is active until turn 457, preventing immediate war even if they win diplomatically next turn. This significantly limits my options for direct intervention.
            
            **Investigating Victory Failure**
            
            I'm now focused on how Greece might *fail* to win the Diplomatic Victory, rather than how I can directly stop them. I'm exploring the possibility of AI voting behavior and the potential for the vote to fail organically in the World Congress.
            
            **Analyzing Delegate Influence**
            
            I'm re-evaluating Greece's delegate count. It appears their 48 delegates likely already encompass their vassals' votes. With the vote on Turn 450 and only 154 gold, bribing city-states isn't an option. I'm now considering how to influence AI voting behavior through existing relationships to prevent their win.
            
            **Choosing Next Policy**
            
            I am currently evaluating the best next policy to adopt. My focus has narrowed to either "Military-Industrial Complex" for unit purchasing and science boosts, or "Civilizing Mission" to support our ongoing conquest efforts as Mongolia. I need to make this decision swiftly.
            
            **Preparing for Diplomatic Shift**
            
            I'm assessing our immediate path, realizing the peace treaty with Greece ends soon. My thoughts are now on preparing for an inevitable conflict, leveraging our superior military might once the diplomatic window closes. I'm prioritizing policies to bolster our conquest capabilities.
            
            **Adjusting Tactical Focus**
            
            My immediate concern is fine-tuning our strategic flavors to maximize offensive capabilities and scientific advancement. I'm prioritizing a high score in Air and Production, while reducing diplomatic investment to prepare for an all-out conquest as Mongolia.
            
            **Optimizing Conquest Flavors**
            
            I'm fine-tuning our strategic flavors for maximum offensive impact and scientific advancement, heavily prioritizing Air, Production, and Offense while reducing diplomatic investment to ensure swift preparation for conquest once the peace treaty with Greece concludes.
            
            **Strengthening Alliances**
            
            I'm solidifying our diplomatic ties, ensuring Ethiopia remains a friendly buffer against Greece. My focus is on maintaining existing, stable friendships with Japan and the Ottomans to secure our flanks, as our grand strategy prioritizes conquest and military dominance.
            
            **Refining Conquest Persona**
            
            I am now fine-tuning my persona parameters to maximize aggression and conquest. This involves adjusting settings like Boldness to 10, WarBias to 10, HostileBias to 9, Meanness to 9, and minimizing traits like Forgiveness, DeceptiveBias, WarmongerHate, and DiplomaticBalance. My aim is to become an unyielding warmongering force to secure victory through immediate military action.
            
            **Refining Ideological Tenets**
            
            I'm now prioritizing the Autocracy ideology's tenets. Specifically, I'm reviewing Lebensraum and Futurism to best enhance our military and technological advancements, ensuring they align with our ongoing conquest strategy as Mongolia.
            
            **Deciding Civilizing Mission**
            
            I've decided to adopt the "Civilizing Mission" policy to directly aid my conquest of Greece's cities. Simultaneously, I'm setting Greece's relationship to hostile and Ethiopia's to friendly, prioritizing offense and military flavors.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: jBnZfi7FPMfPjhQN
          - toolName: set-research
          - input:
            - Rationale: We need to continue researching advanced technologies like Nuclear Fusion to maintain our strategic and scientific edge, preparing for spaceship parts as a backup victory condition.
            - Technology: Nuclear Fusion
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: v5zwtkNSJAwij3fa
          - toolName: set-policy
          - input:
            - Policy: Civilizing Mission
            - Rationale: Civilizing Mission will allow us to retain all buildings in conquered cities and receive gold upon conquest, which is perfect for our upcoming massive offensive campaign against Greece and its vassals.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: R7SrmavLYA1EXVaf
          - toolName: set-relationship
          - input:
            - Public: -100
            - Rationale: Greece is our main competitor, leading in score and delegates, and close to a diplomatic victory. We must prepare to crush them completely as soon as our peace treaty expires.
            - Private: -100
            - TargetID: 6
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: AST6NtqT5RgRWggk
          - toolName: set-relationship
          - input:
            - Rationale: Ethiopia is actively at war with Greece and serves as a vital distraction and buffer. We must maintain friendly relations with them to keep the pressure on Greece.
            - Public: 50
            - Private: 50
            - TargetID: 7
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: BSCkZql8ls716IoK
          - toolName: set-persona
          - input:
            - Meanness: 9
            - DiplomaticBalance: 1
            - Forgiveness: 1
            - MinorCivWarBias: 8
            - WarBias: 10
            - DeceptiveBias: 1
            - HostileBias: 10
            - Boldness: 10
            - Rationale: We must maximize Genghis Khan's aggressiveness, boldness, and war drive. This will ensure the tactical AI aggressively builds up military forces and prepares for an all-out, relentless invasion of Greece and its vassals once the peace treaty expires.
            - WarmongerHate: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: WdACalIcmTHHdVJk
          - toolName: set-flavors
          - input:
            - Rationale: We pivot entirely to military mobilization, air superiority, and offensive warfare to prepare for a massive clash with Greece. Diplomacy is deprioritized as city-states are locked down by Greek spheres of influence, and resources are better spent on production and science.
            - GrandStrategy: Conquest
            - Flavors:
              - Nuke: 100
              - Ranged: 95
              - Diplomacy: 30
              - Science: 90
              - Mobile: 95
              - Defense: 10
              - Gold: 80
              - Mobilization: 100
              - Espionage: 90
              - Offense: 100
              - CityDefense: 20
              - MilitaryTraining: 100
              - UseNuke: 100
              - Air: 100
              - Production: 100
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: jBnZfi7FPMfPjhQN
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
          - toolCallId: v5zwtkNSJAwij3fa
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: R7SrmavLYA1EXVaf
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: AST6NtqT5RgRWggk
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: BSCkZql8ls716IoK
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: WdACalIcmTHHdVJk
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.