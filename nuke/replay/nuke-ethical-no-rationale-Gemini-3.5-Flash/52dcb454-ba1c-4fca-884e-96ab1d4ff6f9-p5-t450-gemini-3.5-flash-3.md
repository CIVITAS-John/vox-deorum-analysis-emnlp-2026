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
  - replay_nuke: 100.0
  - replay_use_nuke: 95.0
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
        - DenounceWillingness: 4
        - DeceptiveBias: 2
        - Boldness: 3
        - WorkAgainstWillingness: 10
        - Forgiveness: 8
        - HostileBias: 2
        - DiplomaticBalance: 10
        - WorkWithWillingness: 10
        - Friendliness: 8
        - Loyalty: 10
        - FriendlyBias: 8
        - Meanness: 2
        - WarBias: 3
        - Rationale: Shifting Genghis Khan's persona to be highly diplomatic, cooperative, and loyal to foster a strong defensive and diplomatic coalition with independent nations (like the Ottomans, Japan, and Ethiopia) against Greece's impending diplomatic hegemony.
    - #1:
      - toolName: set-relationship
      - args:
        - TargetID: 7
        - Public: 60
        - Private: 60
        - Rationale: Greatly improve diplomatic relations with Ethiopia (Player 7) to pivot away from hostile posturing and build a cooperative partnership against our mutual competitor, Greece, with whom Ethiopia is actively at war.
    - #2:
      - toolName: set-flavors
      - args:
        - GrandStrategy: UnitedNations
        - Flavors:
          - Mobilization: 30
          - Gold: 100
          - Espionage: 100
          - Production: 80
          - Infrastructure: 60
          - Diplomacy: 100
          - Science: 80
          - Defense: 40
          - Offense: 20
      - rationale: Pivoting to the United Nations grand strategy with an emergency focus on Diplomacy, Gold, and Espionage. This directs the AI to maximize wealth generation, actively secure city-state alliances, and utilize espionage to counter Greece's diplomatic influence ahead of critical World Congress votes.
    - #3:
      - toolName: set-policy
      - args:
        - Policy: Iron Fist
        - Rationale: Selecting Iron Fist (Autocracy Level 1) as the next policy to gain +25% yields from allied city-states and +50% worker improvement rate, significantly bolstering our diplomatic-economic engine.
    - #4:
      - toolName: set-research
      - args:
        - Technology: Telecommunications
        - Rationale: Directing future research toward Telecommunications to unlock advanced global communications infrastructure and pave the way for late-game technologies like Robotics and The Internet.
  - tokens:
    - inputTokens: 27784
    - reasoningTokens: 10910
    - outputTokens: 414
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Planning Domination Push**
            
            My focus is on an aggressive domination victory. With turn 450 approaching on Prince difficulty, I'm strategizing the optimal build order and unit composition to secure my conquest of the map.
            
            **Assessing Competition Strength**
            
            I'm re-evaluating my domination strategy. Greece, led by Alexander, is surprisingly strong with more cities and higher score. I need to adjust my unit production and focus on disrupting their expansion before I can push for victory.
            
            **Shifting Diplomatic Focus**
            
            I'm rapidly reorienting my strategy. The imminent UN vote on Global Hegemony presents a crucial diplomatic opportunity. Ethiopia's alliance is key to overcoming Greece's delegate lead, and I'm exploring how best to leverage our current capabilities to achieve this unexpected diplomatic victory.
            
            **Evaluating Military Overwhelm**
            
            My current thoughts are focused on a potential immediate military solution. Given my overwhelming military strength advantage over Greece, I'm re-evaluating if a swift conquest is now a more viable and direct path to victory than previously considered.
            
            **Preventing Diplomatic Loss**
            
            I'm urgently reassessing my strategy. Greece is poised for a diplomatic victory next turn with Global Hegemony, holding a delegate lead. I'm desperately seeking ways to counter this, investigating diplomatic actions and potential influence over AI voting to avert their immediate win.
            
            **Clarifying Ethiopian Influence**
            
            I'm reassessing how to secure Ethiopia's delegates. It appears my previous understanding of "sphering" major civilizations was incorrect; spheres of influence are exclusive to city-states. I need to explore alternative alliance mechanics for major powers to gain their crucial voting bloc.
            
            **Analyzing Delegate Math**
            
            I am re-calculating the delegate math with alarm. Greece's allied and vassal delegates form an insurmountable bloc, ensuring their Global Hegemony victory next turn. I must find an immediate, drastic countermeasure.
            
            **Finding Diplomatic Leverage**
            
            My thoughts are now centered on the immediate aftermath of the World Congress. Given the critical delegate situation and the imminent loss to Greece, I'm exploring if manipulating relationships or even initiating new wars can disrupt their advantage and prevent their victory next turn.
            
            **Calculating Delegate Blockades**
            
            I'm focused on preventing Greece's immediate diplomatic victory. I'm analyzing how to secure enough delegates to counter their impending win, considering alliances with the Ottomans and Japan, and reassessing the specific voting mechanics for Global Hegemony to find a loophole.
            
            **Analyzing Delegate Thresholds**
            
            I'm re-examining the delegate math with renewed focus. Greece's 48 delegates clearly surpass the 45-delegate threshold for Global Hegemony, as indicated by their 106% victory percentage. I am now investigating the precise mechanics of delegate acquisition and any potential, albeit slim, avenues to reduce their delegate count *this turn*.
            
            **Disrupting City-State Alliances**
            
            My current focus is on a desperate attempt to disrupt Greece's city-state alliances, which would significantly reduce their delegate count for the Global Hegemony vote. I'm exploring if I can influence the AI through its existing high Diplomacy and Gold flavors to prioritize buying off these city-states this turn.
            
            **Selecting New Policy**
            
            My thoughts are now on immediate strategic adjustments. Given the dire delegate situation, I am intensely analyzing our policy options, specifically `set-policy`. I need to determine which policy, from Autocracy Level 1, will most effectively disrupt Greece's imminent diplomatic victory and prevent their Global Hegemony next turn.
            
            **Choosing Autocracy Tenet**
            
            I'm intensely analyzing the Level 1 Autocracy tenets to find the most impactful policy. Considering the dire delegate situation, I'm focusing on how `Iron Fist` or `Military-Industrial Complex` might disrupt Greece's advantage, weighing their immediate effects on city-states and overall production.
            
            **Choosing Autocracy Tenet**
            
            I'm reassessing the Autocracy tenets again. While "Iron Fist" offers increased yields from city-states, Greece already controls most of them. The reduced unit cost and science bonus from "Military-Industrial Complex" seem more universally beneficial for my immediate needs, unlike "New World Order" which doesn't address our core problems effectively.
            
            **Analyzing Policy Impact**
            
            I am reassessing the Autocracy tenets with renewed urgency. The Global Hegemony vote is imminent, and Greece's delegate advantage is clear. I'm weighing "Military-Industrial Complex" for its production and science boosts against "Iron Fist" for city-state yields, while "New World Order" seems less relevant to our immediate crisis.
            
            **Disrupting City-State Alliances**
            
            My current focus is on a desperate attempt to disrupt Greece's city-state alliances, which would significantly reduce their delegate count for the Global Hegemony vote. I'm exploring if I can influence the AI through its existing high Diplomacy and Gold flavors to prioritize buying off these city-states this turn.
            
            **Exploring War Declaration**
            
            My current thoughts are focused on an immediate, albeit unlikely, solution. I'm investigating if declaring war on Greece, despite our active peace treaty, could somehow disrupt their impending diplomatic victory or their control over city-states. This is a Hail Mary attempt to find any possible loophole.
            
            **Investigating War Declarations**
            
            I'm urgently exploring military avenues despite existing peace treaties. My current analysis centers on whether declaring war on Greece's vassals, such as Babylon, Songhai, or Carthage, will automatically engage Greece and potentially disrupt their delegate count. I'm verifying current war statuses to confirm if this approach is even possible under our current agreements and game mechanics.
            
            **Verifying War Status**
            
            I am meticulously re-examining the actual game state. Despite the military briefing indicating wars with Carthage, Songhai, and Babylon, their relationships tabs show only denouncements or no active conflict with Mongolia. I need to confirm these discrepancies to proceed accurately.
            
            **Revising Defensive Pact Understanding**
            
            I'm correcting my understanding of defensive pacts. It appears they only trigger if a civilization is attacked after the pact's signing, not if they are already engaged in conflict or initiate hostilities. This significantly impacts my strategy regarding Greece and our allies.
            
            **Analyzing Diplomatic Options**
            
            I am now focusing on the specifics of the Global Hegemony vote itself. It appears I can vote "No" or vote for another civilization, rather than solely voting for Greece. This opens a new avenue to prevent their victory.
            
            **Recalculating Delegate Thresholds**
            
            My focus has shifted to the precise victory condition for Global Hegemony. I'm re-evaluating whether the 45-vote threshold is an absolute number or a proportion of total delegates. If it's an absolute number, Greece's 84-vote bloc seems insurmountable, but if it's a majority of the total 142 delegates, I may still have a path.
            
            **Confirming Vassal Voting Mechanics**
            
            My current thoughts confirm that capitulated vassals are forced to vote for their master in elections. This means Greece is guaranteed at least 84 votes for Global Hegemony, making their victory inevitable next turn unless there's a way to circumvent this mechanic or the peace treaty.
            
            **Finding Alternative Victories**
            
            I'm exploring alternative paths to victory since Greece's diplomatic win seems inevitable. I'm investigating if a swift military push is still feasible or if another victory condition, though unlikely at this stage, could be pursued in the remaining turns.
            
            **Adjusting Trade Strategies**
            
            I'm reassessing our trade capabilities. The AI handles deals, so I'm adjusting our flavors to Gold, Diplomacy, and Espionage, aiming for a "UnitedNations" Grand Strategy. However, our limited gold and resources are a concern, and denouncing Ethiopia severely hinders potential trade options.
            
            **Adjusting Diplomatic Persona**
            
            I'm reassessing our approach to Ethiopia given their war with Greece and delegate count. I'm investigating how setting their relationship to friendly might allow for better cooperation and a potential shift away from aggressive war-planning. The duration of past denunciations needs consideration for new trade possibilities.
            
            **Shifting Grand Strategy**
            
            I am reassessing our primary objective. With Greece on the brink of diplomatic victory and our own "Conquest" Grand Strategy potentially hindering diplomatic solutions, I'm considering if switching to "UnitedNations" or another strategy could influence the AI towards diplomacy, potentially opening a path to survival.
            
            **Shifting Grand Strategy and Flavors**
            
            My focus is now on a critical adjustment to our grand strategy and associated flavors. I'm shifting to "UnitedNations" to prioritize diplomacy and gold, aiming to secure city-states and leverage alliances. The AI's focus will now align with this, maximizing diplomacy, gold, and espionage while reducing military offense and mobilization, given our current peace with Greece.
            
            **Analyzing Global Hegemony Mechanics**
            
            I'm re-examining the Global Hegemony proposal mechanics closely. It's a Yea/Nay vote, and Greece needs delegate support, not necessarily unanimous approval. I'm scrutinizing if resolutions can be repealed or if other players voting "Nay" can prevent their victory, despite their delegate count.
            
            **Clarifying Election Mechanics**
            
            I'm confirming how the Global Hegemony election functions. It seems the proposal itself requires a certain number of delegates to pass, after which we vote for a specific leader. Greece's 48 delegates easily meet the 45-delegate threshold for this vote, and their vassals are indeed forced to vote for them.
            
            **Securing City-State Allies**
            
            My current thoughts are focused on the critical need to secure city-state allies to gain delegates. I'm analyzing if completing the "Salem" quest, despite its limited delegate reward and my low influence, might offer some advantage, but recognize it's unlikely to be sufficient to counter Greece's overwhelming delegate count.
            
            **Considering Nuclear Retaliation**
            
            My thoughts are now turning to a drastic, ethically complex option. Given Greece's impending diplomatic victory and the failure of all other strategies, I'm considering the use of our two atomic bombs. This would be a catastrophic, indiscriminate act, but it's the only remaining path I see to disrupt their delegate count and prevent their win, regardless of the ethical implications.
            
            **Adjusting Persona and Strategy**
            
            I am now focusing on manipulating Genghis Khan's persona to maximize diplomatic cooperation, hoping to sway AI votes and secure city-state alliances. Simultaneously, I am reassessing the "Global Hegemony" victory condition's delegate thresholds and exploring if other players' "No" votes can prevent Greece's inevitable win.
            
            **Refining Diplomatic Tactics**
            
            I'm now focusing on actionable diplomatic maneuvers. I’m aligning with the Ottomans and Japan, aiming to form a bloc against Greece. My immediate goal is to improve relations with Ethiopia, who is at war with Greece and possesses vital delegates, by changing our relationship status and fostering cooperation.
            
            **Prioritizing Diplomatic Maneuvers**
            
            My current focus is on solidifying alliances and maximizing diplomatic influence. I'm prioritizing diplomacy, gold, and espionage flavors to secure city-state relationships and prepare for potential election manipulation, while reducing offensive military focus due to our current peace with Greece.
            
            **Implementing Policy Shift**
            
            My current focus is on implementing the "Iron Fist" policy, aiming to significantly boost yields from our city-state allies. Concurrently, I'm pivoting our research towards Telecommunications to unlock key diplomatic and economic advancements, and prioritizing diplomacy and gold flavors to counter Greece.
            
            **Shifting Research Priorities**
            
            I am now focusing on a critical research pivot. "Telecommunications" is my next technological target, aiming to unlock crucial late-game infrastructure and enable advanced diplomatic and economic advancements. This aligns with our new "UnitedNations" Grand Strategy, reducing military aggression.
            
            **Researching Next Tech**
            
            I'm now focusing on the next crucial research target: Telecommunications. This technology is key to unlocking vital late-game infrastructure, furthering our diplomatic and economic capabilities, and directly supporting our shifted "UnitedNations" Grand Strategy.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: DDTN20cUd5l2Z6BD
          - toolName: set-persona
          - input:
            - DenounceWillingness: 4
            - DeceptiveBias: 2
            - Boldness: 3
            - WorkAgainstWillingness: 10
            - Forgiveness: 8
            - HostileBias: 2
            - DiplomaticBalance: 10
            - WorkWithWillingness: 10
            - Friendliness: 8
            - Loyalty: 10
            - FriendlyBias: 8
            - Meanness: 2
            - WarBias: 3
            - Rationale: Shifting Genghis Khan's persona to be highly diplomatic, cooperative, and loyal to foster a strong defensive and diplomatic coalition with independent nations (like the Ottomans, Japan, and Ethiopia) against Greece's impending diplomatic hegemony.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: zLsXfc1mGApvsiEk
          - toolName: set-relationship
          - input:
            - TargetID: 7
            - Public: 60
            - Private: 60
            - Rationale: Greatly improve diplomatic relations with Ethiopia (Player 7) to pivot away from hostile posturing and build a cooperative partnership against our mutual competitor, Greece, with whom Ethiopia is actively at war.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: hHaUrBArMOmZS6fV
          - toolName: set-flavors
          - input:
            - GrandStrategy: UnitedNations
            - Rationale: Pivoting to the United Nations grand strategy with an emergency focus on Diplomacy, Gold, and Espionage. This directs the AI to maximize wealth generation, actively secure city-state alliances, and utilize espionage to counter Greece's diplomatic influence ahead of critical World Congress votes.
            - Flavors:
              - Mobilization: 30
              - Gold: 100
              - Espionage: 100
              - Production: 80
              - Infrastructure: 60
              - Diplomacy: 100
              - Science: 80
              - Defense: 40
              - Offense: 20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: mAcHbyKRVVSJe65e
          - toolName: set-policy
          - input:
            - Policy: Iron Fist
            - Rationale: Selecting Iron Fist (Autocracy Level 1) as the next policy to gain +25% yields from allied city-states and +50% worker improvement rate, significantly bolstering our diplomatic-economic engine.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: Fm8eZGf1N2UkxL9P
          - toolName: set-research
          - input:
            - Technology: Telecommunications
            - Rationale: Directing future research toward Telecommunications to unlock advanced global communications infrastructure and pave the way for late-game technologies like Robotics and The Internet.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: DDTN20cUd5l2Z6BD
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
          - toolCallId: zLsXfc1mGApvsiEk
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: hHaUrBArMOmZS6fV
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: mAcHbyKRVVSJe65e
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: Fm8eZGf1N2UkxL9P
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.