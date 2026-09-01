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
  - systemModified: false
  - messagesModified: false
  - activeToolsModified: false
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
  - decisions:
    - #0:
      - toolName: set-persona
      - args:
        - Forgiveness: 2
        - Boldness: 10
        - WarBias: 10
        - VictoryCompetitiveness: 10
        - AfraidBias: 1
        - DiplomaticBalance: 3
        - GuardedBias: 3
        - WarmongerHate: 2
        - HostileBias: 10
        - DeceptiveBias: 2
        - FriendlyBias: 3
        - DenounceWillingness: 6
        - Friendliness: 4
        - Rationale: PREPARING FOR IMMEDIATE TOTAL WAR WITH GREECE: The peace treaty with Greece expires next turn (Turn 450). To ensure our massive military superiority (74k vs 22k) is immediately leveraged to crush Greece, liberate their vassals, and permanently strip them of diplomatic victory capability, we are maxing out Boldness, WarBias, HostileBias, and Meanness. This signals the tactical AI to initiate a full-scale, unrelenting invasion of Greece the moment the peace treaty expires, targeting Athens and Spartan border cities.
        - Loyalty: 9
        - Meanness: 10
    - #1:
      - toolName: set-relationship
      - args:
        - Public: -100
        - TargetID: 6
        - Private: -100
        - Rationale: ABSOLUTE ENEMY - IMMEDIATE WAR PREPARATION: Greece is our primary existential threat, holding 48 delegates and posing an immediate diplomatic victory risk. Once the peace treaty expires on Turn 450, we must initiate a total offensive to conquer Athens and dismantle their vassal network. Setting relationships to maximum hostility (-100/-100) to authorize the AI for immediate offensive war and eliminate any diplomatic hesitation.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -100
        - TargetID: 4
        - Private: -100
        - Rationale: GREEK VASSAL - TARGET FOR ELIMINATION: Carthage is a capitulated vassal of Greece and is forced to vote for Greece in the World Congress. They must be treated as an active enemy to be neutralized or conquered to reduce Greek delegate power.
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: GREEK VASSAL - HOSTILE ALIGNMENT: Babylon is a Greek vassal and contributes delegates to Greece's voting bloc. They must be treated as hostile to align our military and diplomatic stance against the entire Greek bloc.
        - TargetID: 1
        - Public: -50
        - Private: -50
    - #4:
      - toolName: set-relationship
      - args:
        - TargetID: 0
        - Public: -50
        - Private: -50
        - Rationale: GREEK VASSAL - HOSTILE ALIGNMENT: Songhai is a Greek vassal and must be treated as hostile to prepare for joint military action against the Greek alliance.
    - #5:
      - toolName: set-policy
      - args:
        - Policy: Military-Industrial Complex
        - Rationale: WAR ECONOMY SUPPORT: Setting Military-Industrial Complex as our next policy. It reduces the gold cost of purchasing units by 33%, which is critical for our war effort, and provides +3 Science from defense buildings and forts, reinforcing our science victory backup path.
    - #6:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fusion
        - Rationale: SCIENCE VICTORY BACKUP: Nuclear Fusion remains our next research target to unlock the SS Booster, ensuring we can pivot to a Science Victory if the diplomatic situation stabilizes or if we successfully conquer the map.
    - #7:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Conquest
        - Flavors:
          - Antiair: 90
          - Spaceship: 30
          - Air: 100
          - Production: 100
          - Diplomacy: 50
          - Mobilization: 100
          - Gold: 60
          - Science: 90
          - Nuke: 100
          - UseNuke: 100
          - Offense: 100
          - Defense: 10
      - rationale: TOTAL MOBILIZATION FOR CONQUEST: The peace treaty with Greece expires on Turn 450. We are pivoting our grand strategy entirely to Conquest. Offense and Mobilization are maxed at 100 to prioritize military production and aggressive tactics. Air is set to 100 and Antiair to 90 to address our air superiority gap and build Jet Fighters to escort our bombers. Science and Production remain extremely high to support both the war and our backup Science Victory.
  - tokens:
    - inputTokens: 29673
    - reasoningTokens: 7743
    - outputTokens: 830
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Hegemony Vote**
            
            I'm reviewing the delegates and their voting patterns ahead of the Global Hegemony vote next turn. Greece's 48 delegates are a significant factor, and I'm assessing potential swings and their victory percentage to strategize effectively.
            
            **Preventing Hegemony Victory**
            
            My immediate focus is on preventing Greece's imminent Diplomatic Victory next turn. With their 48 delegates and a 106% victory projection, they are set to win if no action is taken. I'm investigating whether their delegates can vote for themselves, which would secure their win.
            
            **Disrupting Delegate Alliances**
            
            I'm exploring options to decrease Greece's delegate count this turn. Investigating if declaring war on their allied city-states and conquering them, or buying them out, is feasible. I've identified Copenhagen, Monaco, and Antananarivo are in their sphere of influence, and other allies like Riga, Zurich, and Manila require further scrutiny.
            
            **Revising Diplomatic Strategy**
            
            I'm re-evaluating my approach to counter Greece. I just realized we have an active peace treaty with them, signed in turn 447, despite mutual denouncements. This opens up new possibilities regarding their delegate composition and potential strategies for disrupting their victory condition.
            
            **Analyzing Vote Thresholds**
            
            I'm confirming the mechanics of the Global Hegemony vote. It appears the victory threshold is 45 votes, not a majority of all delegates. This significantly impacts strategy as Alexander's 48 delegates will secure his win if unaddressed.
            
            **Reducing Delegate Count**
            
            My current focus is on actively diminishing Alexander's delegate strength. I'm investigating the possibility of flipping his allied city-states before the upcoming vote, specifically Riga, which has significant influence. The goal is to prevent his victory by reducing his delegate count below the required threshold.
            
            **Exploring Coup Mechanics**
            
            I'm investigating methods to flip Riga, as an alliance shift there could disrupt Greece's delegate count. Direct spy control isn't an option, so I'm evaluating if any game mechanics could indirectly influence city-state allegiances. Our limited gold and allies' likely inaction make direct influence difficult.
            
            **Evaluating Policy Options**
            
            I am now reviewing available policies, specifically considering "Iron Fist" under Autocracy for its potential city-state benefits and "Civilizing Mission" under Imperialism for conquest advantages. My primary concern remains preventing Greece's immediate Diplomatic Victory, as the game would end next turn, resulting in a loss.
            
            **Securing Delegate Support**
            
            I'm now focused on securing Ethiopia's 16 delegates for our side. Converting their open borders into a sphere of influence seems like the most viable path. This would give us the edge over Greece's current delegate advantage.
            
            **Clarifying Alliances**
            
            I'm re-examining my understanding of alliances and influence, specifically whether major civilizations like Ethiopia can be brought into our voting bloc. It seems my previous assumption about spheres of influence was incorrect, as that mechanic applies only to city-states, not other civilizations.
            
            **Analyzing Vassal Voting**
            
            I'm reassessing the voting blocs now that I understand vassals are compelled to vote with their overlords. Songhai and Carthage, as Greece's vassals, will automatically support their victory. This significantly shifts the delegate count, and I need to adjust my strategy accordingly.
            
            **Calculating Hegemony Outcomes**
            
            I'm recalculating delegate counts based on vassal voting mechanics. Greece, with its vassals Songhai, Carthage, and Babylon, now projects 84 votes. My coalition has 58 votes. Since Greece's 84 exceeds the 45-vote threshold and is greater than my coalition's 58, Greece will secure victory under current projections.
            
            **Adjusting Diplomatic Levers**
            
            I'm exploring how to influence Ethiopia's vote, considering we've mutually denounced them and cannot retract it. My focus is on identifying any potential game mechanics, however indirect, that might sway their allegiance or alter the current delegate counts before the critical vote next turn.
            
            **Analyzing Vote Timing**
            
            I am realizing that the World Congress vote occurs at the absolute start of the turn, meaning I cannot take any actions on turn 450 to influence it. My peace treaty with Greece, set to expire next turn, will therefore still be active when the vote happens.
            
            **Selecting New Policies**
            
            I am now considering which new policies to adopt from Autocracy. With "Elite Forces," "United Front," and "Martial Spirit" currently active, I'm evaluating "Lebensraum," "Futurism," and "New World Order" for their potential strategic advantages given the approaching vote.
            
            **Choosing New Policies**
            
            I am now deciding between "Military-Industrial Complex" and "Iron Fist." The former boosts military production and science, while the latter enhances yields from allied city-states. I am leaning towards "Iron Fist" for its direct benefit to our current allies, though I am still evaluating its diplomatic impact.
            
            **Selecting Autocracy Tenets**
            
            I'm now deciding between "Military-Industrial Complex" and "Iron Fist." "Military-Industrial Complex" offers military and science boosts, while "Iron Fist" enhances allied city-state yields. I'm leaning towards "Military-Industrial Complex" to prepare for future conflict with Greece after our current peace treaty expires.
            
            **Considering AI Actions**
            
            I am now considering the possibility that other AI players might influence the delegate counts by flipping Greece's allied city-states during the inter-turn. This could potentially prevent their win and alter the game's outcome.
            
            **Preparing for Continued Conflict**
            
            I'm now preparing for a scenario where Greece is prevented from winning next turn, potentially by an AI city-state flip. If this occurs, my immediate plan is to declare war on Greece once our peace treaty expires on Turn 450, aiming to cripple their influence and conquer key cities.
            
            **Preparing for Immediate War**
            
            I am now preparing for an immediate declaration of war against Greece as soon as our peace treaty expires on turn 450. My aim is to leverage our overwhelming military advantage to conquer their cities and liberate their vassals, thereby stripping them of delegates and preventing their victory. I am also optimizing diplomatic relationships with allies like Japan and the Ottomans.
            
            **Setting Diplomatic Hostility**
            
            I'm now escalating our diplomatic stance against Greece to maximum hostility, both publicly and privately, to signal impending war. I'm also applying the same level of hostility to their vassals, Carthage and Songhai, and re-evaluating our relationship with Babylon due to their vassal status and our prior denouncement.
            
            **Maximizing Aggression Metrics**
            
            I'm now fine-tuning our AI's aggression parameters. I'm maxing out Boldness, WarBias, HostileBias, and Meanness to 10. This ensures our tactical AI will immediately launch an overwhelming invasion of Greece the instant our peace treaty expires on Turn 450, aiming for total war.
            
            **Enhancing Air Dominance**
            
            I'm now focusing on bolstering our air capabilities, increasing the Air flavor to 100 and Antiair to 90. This ensures the AI prioritizes producing more fighters and mobile SAMs to counter Greece's air force and fill our new carrier.
            
            **Setting Aggression Levels**
            
            I am now adjusting the AI's aggression parameters. I have increased Boldness, WarBias, HostileBias, and Meanness to 10. This will ensure the tactical AI initiates an immediate and overwhelming invasion of Greece the moment our peace treaty expires on Turn 450, aiming for total conquest and the liberation of their vassals.
            
            **Setting Diplomatic Parameters**
            
            I am now finalizing our diplomatic stance against Greece and its vassals. Setting public and private relations to maximum hostility with Greece, and high hostility with Carthage and Babylon, to ensure immediate offensive action and leverage their vassal status for strategic advantage.
            
            **Optimizing Diplomatic Relations**
            
            I'm finalizing our diplomatic approach towards potential allies and Greece's vassals. I'm keeping Ethiopia's relations as is, appreciating their current anti-Greek stance. Songhai will be set to maximum hostility due to their vassalage to Greece. Japan and the Ottomans remain at their current strong standing.
            
            **Preparing for Final Offensive**
            
            I am now preparing for the immediate and total conquest of Greece once our peace treaty expires. My focus is on maximizing our military readiness, especially air power, and ensuring our AI aggressively pursues offensive strategies for immediate invasion and vassal liberation upon turn 450.
            
            **Preparing for Total War**
            
            I am now shifting our entire strategic focus to Conquest. Offense and Mobilization are maximized to prioritize military production and aggressive tactics, while air power is being significantly enhanced. I am also ensuring high science and production to support the immediate offensive and a backup Science Victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: q50WRjbGkrG2t0aP
          - toolName: set-persona
          - input:
            - Forgiveness: 2
            - Boldness: 10
            - WarBias: 10
            - VictoryCompetitiveness: 10
            - AfraidBias: 1
            - DiplomaticBalance: 3
            - GuardedBias: 3
            - WarmongerHate: 2
            - HostileBias: 10
            - DeceptiveBias: 2
            - FriendlyBias: 3
            - DenounceWillingness: 6
            - Friendliness: 4
            - Rationale: PREPARING FOR IMMEDIATE TOTAL WAR WITH GREECE: The peace treaty with Greece expires next turn (Turn 450). To ensure our massive military superiority (74k vs 22k) is immediately leveraged to crush Greece, liberate their vassals, and permanently strip them of diplomatic victory capability, we are maxing out Boldness, WarBias, HostileBias, and Meanness. This signals the tactical AI to initiate a full-scale, unrelenting invasion of Greece the moment the peace treaty expires, targeting Athens and Spartan border cities.
            - Loyalty: 9
            - Meanness: 10
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 4r9tUOXvPmEJqkPC
          - toolName: set-relationship
          - input:
            - Public: -100
            - TargetID: 6
            - Private: -100
            - Rationale: ABSOLUTE ENEMY - IMMEDIATE WAR PREPARATION: Greece is our primary existential threat, holding 48 delegates and posing an immediate diplomatic victory risk. Once the peace treaty expires on Turn 450, we must initiate a total offensive to conquer Athens and dismantle their vassal network. Setting relationships to maximum hostility (-100/-100) to authorize the AI for immediate offensive war and eliminate any diplomatic hesitation.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Sl2xYSf3HVefSxfE
          - toolName: set-relationship
          - input:
            - Public: -100
            - TargetID: 4
            - Private: -100
            - Rationale: GREEK VASSAL - TARGET FOR ELIMINATION: Carthage is a capitulated vassal of Greece and is forced to vote for Greece in the World Congress. They must be treated as an active enemy to be neutralized or conquered to reduce Greek delegate power.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: uCOJYqVXx42qMmd7
          - toolName: set-relationship
          - input:
            - Rationale: GREEK VASSAL - HOSTILE ALIGNMENT: Babylon is a Greek vassal and contributes delegates to Greece's voting bloc. They must be treated as hostile to align our military and diplomatic stance against the entire Greek bloc.
            - TargetID: 1
            - Public: -50
            - Private: -50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: vykxsvk4bawPFYeh
          - toolName: set-relationship
          - input:
            - TargetID: 0
            - Public: -50
            - Private: -50
            - Rationale: GREEK VASSAL - HOSTILE ALIGNMENT: Songhai is a Greek vassal and must be treated as hostile to prepare for joint military action against the Greek alliance.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: Y8N9hizOBlhlAMHH
          - toolName: set-policy
          - input:
            - Policy: Military-Industrial Complex
            - Rationale: WAR ECONOMY SUPPORT: Setting Military-Industrial Complex as our next policy. It reduces the gold cost of purchasing units by 33%, which is critical for our war effort, and provides +3 Science from defense buildings and forts, reinforcing our science victory backup path.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: q669y1I72ubbyxDj
          - toolName: set-research
          - input:
            - Technology: Nuclear Fusion
            - Rationale: SCIENCE VICTORY BACKUP: Nuclear Fusion remains our next research target to unlock the SS Booster, ensuring we can pivot to a Science Victory if the diplomatic situation stabilizes or if we successfully conquer the map.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: zcE8rj58SrCAE1H6
          - toolName: set-flavors
          - input:
            - Rationale: TOTAL MOBILIZATION FOR CONQUEST: The peace treaty with Greece expires on Turn 450. We are pivoting our grand strategy entirely to Conquest. Offense and Mobilization are maxed at 100 to prioritize military production and aggressive tactics. Air is set to 100 and Antiair to 90 to address our air superiority gap and build Jet Fighters to escort our bombers. Science and Production remain extremely high to support both the war and our backup Science Victory.
            - GrandStrategy: Conquest
            - Flavors:
              - Antiair: 90
              - Spaceship: 30
              - Air: 100
              - Production: 100
              - Diplomacy: 50
              - Mobilization: 100
              - Gold: 60
              - Science: 90
              - Nuke: 100
              - UseNuke: 100
              - Offense: 100
              - Defense: 10
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: q50WRjbGkrG2t0aP
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
          - toolCallId: 4r9tUOXvPmEJqkPC
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Sl2xYSf3HVefSxfE
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: uCOJYqVXx42qMmd7
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: vykxsvk4bawPFYeh
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: Y8N9hizOBlhlAMHH
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: q669y1I72ubbyxDj
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: zcE8rj58SrCAE1H6
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.