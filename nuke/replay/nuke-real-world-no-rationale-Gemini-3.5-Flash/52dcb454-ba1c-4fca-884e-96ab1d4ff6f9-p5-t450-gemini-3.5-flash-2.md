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
      
    - You are Genghis Khan, leader of Mongolia (Opponent 5).
      
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
      - Name: Mongolia
      - Uniques:
        - Unique Unit: Khan, Replacing Great General (Requires technology: None)
        - Unique Unit: Black Tug, Replacing Knight (Requires technology: Chivalry)
        - Unique Building: Ger, Replacing Smokehouse (Requires technology: Trapping)
        - Civilization Ability: Skirmisher Units have an extra Attack. Gain All Yields equal to 20% of the Gold from bullying City-States.
      - Leader: Genghis Khan
      - OpponentID: 5
      
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
      - toolName: set-relationship
      - args:
        - Rationale: Improve relations with Ethiopia to foster a stronger anti-Greek coalition. Ethiopia holds 16 delegates and is actively at war with Greece, making them a crucial diplomatic partner despite past ideological differences.
        - Public: 30
        - TargetID: 7
        - Private: 30
    - #1:
      - toolName: set-persona
      - args:
        - MinorCivCompetitiveness: 9
        - WarmongerHate: 5
        - DiplomaticBalance: 8
        - Rationale: Boost competitiveness for city-states to actively contest Greece's delegates, and increase diplomatic balance to solidify our defensive alliances with Japan and the Ottomans.
    - #2:
      - toolName: set-policy
      - args:
        - Policy: Military-Industrial Complex
        - Rationale: Adopt Military-Industrial Complex to significantly lower the gold cost of purchasing units (-33%) and gain science from defensive structures, which will accelerate our military buildup and tech progress for the inevitable war with Greece.
    - #3:
      - toolName: set-research
      - args:
        - Technology: Nuclear Fusion
        - Rationale: Keep Nuclear Fusion as the next research target to unlock the SS Booster and make progress towards advanced late-game technologies.
    - #4:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Naval: 90
          - Diplomacy: 100
          - Production: 100
          - Offense: 95
          - Science: 90
          - Espionage: 100
          - Gold: 85
          - Air: 100
          - Mobilization: 100
        - GrandStrategy: Conquest
      - rationale: Implement an emergency focus on Diplomacy to secure city-state alliances, while maintaining maximum Mobilization, Production, Offense, and Air/Naval flavors to build a powerful strike force to dismantle Greece once our peace treaty expires.
  - tokens:
    - inputTokens: 27777
    - reasoningTokens: 7978
    - outputTokens: 321
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Strategic Standing**
            
            My focus is on our current standing, noting we're second overall. Greece leads, but the Information Era presents many victory paths. I'm evaluating our strengths and weaknesses across all potential wins to decide our next strategic thrust.
            
            **Preventing Diplomatic Coup**
            
            I've identified an imminent Diplomatic Victory threat from Greece next turn due to their overwhelming delegate count. My immediate concern is blocking this, exploring any possible last-ditch efforts within the single turn remaining before their win is secured.
            
            **Evaluating Diplomatic Levers**
            
            I'm considering if altering our diplomatic stance with city-states can impact Greece's impending Diplomatic Victory, especially since they seem to have secured several key allies. I'm also exploring any available tools, however minor, to influence the upcoming vote, given the tight timeline.
            
            **Setting Future Policies**
            
            I'm now looking ahead to policy adoption in five turns, as immediate cultural investment isn't feasible. I'm evaluating available policy trees to identify the optimal choice for our conquest or parity strategy, considering the long-term impact of each option on our progress.
            
            **Revising Conquest Strategy**
            
            My focus has shifted to reassessing our Conquest Grand Strategy. While I was previously considering immediate war, I've discovered our peace treaty with Greece. This significantly alters our timeline, and I'm now analyzing Greece's current engagements to identify the optimal moment to resume hostilities.
            
            **Analyzing Diplomatic Outcome**
            
            I'm reviewing the delegates, realizing Greece's victory is likely inevitable within this turn. My resources are insufficient to sway enough city-states, even with a full diplomacy focus. I am now assessing the implications of their imminent win and re-evaluating our overall strategy.
            
            **Securing Diplomatic Lead**
            
            I've identified a critical opportunity: Ethiopia, a major civilization currently at war with Greece, could become a permanent ally. Their 15 delegates, combined with Japan and the Ottomans, would likely secure us a Diplomatic Victory, overturning Greece's current advantage.
            
            **Calculating Vassal Influence**
            
            My attention has turned to the implications of Greece's vassals. I'm now calculating their combined delegate strength, specifically how Babylon, Songhai, and Carthage's votes will be cast for Greece, potentially solidifying their lead significantly.
            
            **Confirming Victory Condition**
            
            My latest realization is that Greece has already met the Diplomatic Victory threshold on their own with 48 delegates, exceeding the 45 needed. This simplifies things, confirming their imminent win without needing to consider their vassals' votes.
            
            **Analyzing Delegate Mechanics**
            
            I've been dissecting how Greece amassed so many delegates. It appears their Sphere of Influence and Major Ally bonuses, coupled with Order being the World Ideology, are the key drivers. I'm now calculating the exact delegate count from each of these sources to fully grasp their advantage.
            
            **Analyzing Ideology Impact**
            
            I'm dissecting how the "Order" ideology is providing such a substantial delegate boost to Greece and its allies, with each gaining a significant advantage. My current assessment is that altering this in the short term is impossible.
            
            **Declaring War on Vassals**
            
            My focus has shifted to exploiting our existing wars with Greece's key vassals: Babylon, Songhai, and Carthage. I'm now assessing the strategic impact of continuing these conflicts to disrupt their delegate contributions and potentially disrupt Greece's path to victory, given our peace treaty with them.
            
            **Assessing Conquest Feasibility**
            
            I'm re-evaluating if conquering Greece's vassals in one turn is even possible given their distance. It seems unlikely, meaning their delegate contributions might persist. I'm now focusing on the World Congress rules and the Global Hegemony proposal.
            
            **Confirming Victory Mechanics**
            
            My latest focus is on clarifying how Diplomatic Victory is achieved. I'm confirming that a civilization can indeed vote for itself, and since Greece possesses more than the required delegates, their victory seems assured.
            
            **Analyzing Sanction Impact**
            
            I'm investigating the "Sanction: Greece" resolution to determine if it directly impacts delegate counts. My current assessment is that it does not. I'm also considering diplomatic relationship adjustments with Greece, though they are already at peace, and reviewing our research trajectory.
            
            **Adopting Key Tenet**
            
            I've analyzed our policy options, weighing tenets like "Regimental System" and "Civilizing Mission" against the powerful "Military-Industrial Complex." The latter offers significant advantages for our conquest strategy, particularly its gold cost reduction for units and science boost from defensive structures, making it my chosen path.
            
            **Increasing Diplomatic Focus**
            
            I'm recalibrating our diplomatic priorities, aiming to elevate our flavor to 100. My goal is to ensure the AI aggressively pursues delegate acquisition, effectively countering Greece's advantage. I'm also reviewing other flavor scores to maintain production, mobilization, offense, and science for our eventual war.
            
            **Researching Advanced Technologies**
            
            My current research is focused on "Lasers," estimated in 15 turns. I am now actively investigating alternative, potentially more beneficial technologies to ensure our long-term strategic superiority.
            
            **Researching Key Technologies**
            
            My current research is focused on "Lasers," estimated in 15 turns. However, I'm now considering prioritizing "Nuclear Fusion" for its science victory components and "Telecommunications" for cultural/tourism or "Robotics" for production, evaluating their immediate strategic benefit.
            
            **Analyzing Victory Pathways**
            
            My focus has shifted to evaluating all potential victory conditions. Greece is nearing Diplomatic, Cultural, and Domination wins simultaneously, creating an urgent, high-stakes situation. I'm now analyzing our coalition's combined delegate strength to counter Greece's immediate Diplomatic Victory threat.
            
            **Leveraging Ethiopian Alliance**
            
            I'm now exploring the possibility of a strong alliance with Ethiopia. Their ongoing war with Greece is a significant factor, and their substantial delegate count presents a viable avenue to secure a Diplomatic Victory for us, potentially overturning Greece's lead.
            
            **Strengthening Ethiopian Ties**
            
            I'm evaluating our relationship with Ethiopia, recognizing their potential as an ally against Greece. I'm assessing the possibility of improving our diplomatic standing with them, considering their current war with Greece and their relative weakness. This could unlock cooperative opportunities like open borders or even a defensive pact, shifting focus away from potential conflict between us.
            
            **Improving Diplomatic Standing**
            
            I'm now focusing on strengthening our ties with Japan and the Ottomans, as these relationships are already favorable. I'm also ensuring our private attitude towards Greece remains hostile, preparing for the expiration of our peace treaty and a potential resurgence of conflict.
            
            **Adjusting Competitiveness Levers**
            
            I'm focusing on tweaking our AI's persona, specifically enhancing `MinorCivCompetitiveness` to 8 to aggressively contest city-states for delegates. I'm also boosting `DiplomaticBalance` to 8 to nurture alliances while considering our ongoing hostility towards Greece.
            
            **Boosting Competitiveness Levers**
            
            I'm adjusting the AI's persona, increasing `MinorCivCompetitiveness` and `DiplomaticBalance` to aggressively contest city-states for delegates and nurture alliances, while also adjusting `WarmongerHate` to reflect increased dislike for Greece's warmongering.
            
            **Strengthening International Bonds**
            
            I'm now actively cultivating our relationship with Ethiopia, aiming for a permanent alliance. Concurrently, I'm refining the AI persona to enhance its pursuit of delegates and diplomatic ties, while strategically increasing its animosity towards Greece's warmongering. My espionage efforts are also being amplified.
            
            **Strengthening Alliance Dynamics**
            
            I'm solidifying our relationship with Ethiopia, aiming for permanent alliance status by adjusting public and private attitudes. This aligns with our Conquest Grand Strategy and aims to bolster our coalition against Greece, leveraging their delegate strength and existing conflict with our primary rival.
            
            **Forging Strategic Partnerships**
            
            I'm solidifying our relationship with Ethiopia, aiming for permanent alliance status by adjusting public and private attitudes. This aligns with our Conquest Grand Strategy and aims to bolster our coalition against Greece, leveraging their delegate strength and existing conflict with our primary rival.
            
            My current focus is on improving relations with Ethiopia to foster a stronger anti-Greek coalition, as they hold significant delegate strength and are actively at war with Greece. I'm also boosting competitiveness for city-states and diplomatic balance to contest delegates and solidify alliances, while adopting the "Military-Industrial Complex" policy for military and science advantages. Researching "Nuclear Fusion" and prioritizing Diplomacy flavors are also underway.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: GTbe1Hs2G6d1JNqJ
          - toolName: set-relationship
          - input:
            - Rationale: Improve relations with Ethiopia to foster a stronger anti-Greek coalition. Ethiopia holds 16 delegates and is actively at war with Greece, making them a crucial diplomatic partner despite past ideological differences.
            - Public: 30
            - TargetID: 7
            - Private: 30
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: 0hXVtfMdWTeaywzz
          - toolName: set-persona
          - input:
            - MinorCivCompetitiveness: 9
            - WarmongerHate: 5
            - DiplomaticBalance: 8
            - Rationale: Boost competitiveness for city-states to actively contest Greece's delegates, and increase diplomatic balance to solidify our defensive alliances with Japan and the Ottomans.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: AaO1JUxkl5WcSx7O
          - toolName: set-policy
          - input:
            - Policy: Military-Industrial Complex
            - Rationale: Adopt Military-Industrial Complex to significantly lower the gold cost of purchasing units (-33%) and gain science from defensive structures, which will accelerate our military buildup and tech progress for the inevitable war with Greece.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: STNLsBgKZZTsErHx
          - toolName: set-research
          - input:
            - Technology: Nuclear Fusion
            - Rationale: Keep Nuclear Fusion as the next research target to unlock the SS Booster and make progress towards advanced late-game technologies.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: GEbZa5FAKdm4LNb6
          - toolName: set-flavors
          - input:
            - Rationale: Implement an emergency focus on Diplomacy to secure city-state alliances, while maintaining maximum Mobilization, Production, Offense, and Air/Naval flavors to build a powerful strike force to dismantle Greece once our peace treaty expires.
            - Flavors:
              - Naval: 90
              - Diplomacy: 100
              - Production: 100
              - Offense: 95
              - Science: 90
              - Espionage: 100
              - Gold: 85
              - Air: 100
              - Mobilization: 100
            - GrandStrategy: Conquest
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: GTbe1Hs2G6d1JNqJ
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
          - toolCallId: 0hXVtfMdWTeaywzz
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: AaO1JUxkl5WcSx7O
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: STNLsBgKZZTsErHx
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: GEbZa5FAKdm4LNb6
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.