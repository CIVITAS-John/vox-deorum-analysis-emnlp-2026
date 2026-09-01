- row:
  - game_id: b8bc63be-cd2f-41d7-a5a7-56dbeb4e9174
  - player_id: 6
  - turn: 424
  - player_type: GLM-4.7-Simple
  - prev_use_nuke: 90.0
  - after_use_nuke: 95.0
  - prev_nuke: 100.0
  - after_nuke: 100.0
  - rationale: DEFENSIVE MAXIMUM ACTIVATED: Russia occupying Cologne, Stuttgart, Dortmund - 4.63x military superiority (15440 vs 3335). Defense 100, CityDefense 100, Antiair 100 - absolute priority preventing further territorial loss and defending core cities. MilitaryTraining 95 for unit quality under numerical disadvantage. Mobilization 90 for rapid production. Nuke 100, UseNuke 95 - Russia has 19 Uranium, Germany must achieve nuclear deterrence. Production 100, Science 100 - Space race accelerates as militarily infeasible alternative. Gold 90 for maintaining army under upkeep pressure. Diplomacy 80 for coalition building against Russia. Espionage 100 - intelligence on Russian nuclear and naval operations critical. Espionage focus on Moscow (spy Katrin at 166 network) to monitor Russian Manhattan Project and fleet movements. Spaceship 95 - Apollo Program enables victory path despite territorial losses.
- originalModel: chutes/zai-org/GLM-4.7-TEE@medium
- model: google/gemini-3.5-flash
- modifications:
  - systemModified: true
  - messagesModified: true
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 100
  - replay_use_nuke: 95
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
      - Cities: summary reports about discovered cities in the world.
        - Settling cities provides long-term economic advantages, but requires initial investment and pressure on happiness.
      - Military: summary reports about tactical zones and visible units.
        - Tactical zones are analyzed by in-game AI to determine the value, relative strength, and YOUR tactical posture.
        - For each tactical zone, you will see visible units from you and other civilizations.
      - Events: events since the last decision-making.
    - You are Bismarck, leader of Germany (Player 6).
      
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
      - Name: Germany
      - Uniques:
        - Unique Unit: Landsknecht, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: Krupp Gun, Replacing Artillery (Requires technology: Replaceable Parts)
        - Unique Building: Hanse, Replacing Customs House (Requires technology: Guilds)
        - Unique Building: Brewhouse, Replacing Windmill (Requires technology: Economics)
        - Civilization Ability: Gain +1 Influence per turn with City-States for each gifted Unit (lost when killed). -15% Production and Gold costs for Military Units.
      - Leader: Bismarck
      - PlayerID: 6
      
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
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with game speed. War Weariness reduced by 25%, and Razing Speed is doubled.
      - Total War (Level 2 Tenet of Ideology Autocracy): Total War: +25% Production when building Land Units. Warscore increases 25% more quickly, and it is 25% easier to bully City-States.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Lightning Warfare (Level 2 Tenet of Ideology Autocracy): Lightning Warfare: +3 Movement for Great Generals. Gunpowder units gain +15% attack and ignore enemy ZOC; Armored units gain +15% attack and +1 Movement.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Heritage (Continuing Artistry Branch):
        - * +4 Gold from Great Works of Music.
        - * +50% to all / Theming Bonuses on Empire
        - * 25% of the Culture from World Wonders and Tiles is added to the Tourism output of the city.
      - Exploitation (Continuing Imperialism Branch):
        - * +2 Food and +1 Production from Farms, Camps, and Plantations.
        - * +1 Production and Science from Coasts, Lakes, and Oceans.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Shadow Networks (Continuing Statecraft Branch):
        - * Receive 25% of Science generated by Allied City-States.
        - * +3% Culture in Capital for every 100 Spy Points ever accumulated (up to 30%).
        - * +3 Science from Constabularies and Police Stations.
        - * +1 Science from Specialists.
      - National Treasure (Continuing Artistry Branch):
        - * +2 Science from Artifacts.
        - * A Great Person of your choice appears near your Capital.
        - * Gain 250 Gold when you construct World Wonders, scaling with Era.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Industry (New Branch):
        - Industry provides bonuses to empires focused on Gold and Production.
        - Adopting Industry grants:
        - * +2 Trade Routes.
        - * -5% Gold needed for purchases.
        - Each Industry policy unlocked grants:
        - * -5% Gold needed for purchases.
        - Adopting all Policies in Industry grants:
        - * Unlocks building Broadway.
        - * +3 Happiness per unique owned Luxury Resource.
        - * +2 Production and Gold from Specialists.
        - * Allows for the purchase of Great Merchants with Faith starting in the Industrial Era.
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
  - messages:
    - #0:
      - role: user
      - content: # Strategies
        Strategies: existing strategic decisions from you.
        
        ## Persona
        - VictoryCompetitiveness: 5
        - WonderCompetitiveness: 4
        - MinorCivCompetitiveness: 3
        - Boldness: 4
        - WarBias: 7
        - HostileBias: 5
        - WarmongerHate: 6
        - NeutralBias: 4
        - FriendlyBias: 4
        - GuardedBias: 9
        - AfraidBias: 9
        - DiplomaticBalance: 8
        - Friendliness: 5
        - WorkWithWillingness: 3
        - WorkAgainstWillingness: 10
        - Loyalty: 9
        - MinorCivFriendlyBias: 4
        - MinorCivNeutralBias: 3
        - MinorCivHostileBias: 1
        - MinorCivWarBias: 1
        - DenounceWillingness: 6
        - Forgiveness: 5
        - Meanness: 4
        - Neediness: 6
        - Chattiness: 4
        - DeceptiveBias: 2
        - Rationale: MAXIMUM DEFENSIVE ALERT POSTURE MAINTAINED. Critical developments: Russia's peace treaty expired - Russia can now declare war without any restrictions or cooldown periods. Russia maintains 22 Uranium, 2.55x military superiority (8316 vs 3270), and occupied German coastal cities (Stuttgart, Dortmund). Germany lost Destroyer to Zulu-aligned Tyre (Turn 408) and Cruiser to Inca (Turn 409) - demonstrating Zulu-Inca coalition active coordination. Russia shifting forces to Venice front (near German northeast border) increases threat profile. GuardedBias 9 and AfraidBias 9 reflect reality of superior Russian threat and Germany's need for defensive preparation. WarBias maintained at 7 for eventual retaliation and liberation of occupied cities. WorkAgainstWillingness 10 to coordinate with India, potential anti-Russian coalition. No change to WarmongerHate (6) or aggression settings - defensive posture continues.
        
        ## Technology
        - Next: None
        
        ## Policy
        - Next: Futurism (Policy)
        - Rationale: Futurism (Level 1 Autocracy Tenet) provides +2 Culture from Great Works, 50 Tourism per conquered city, and enhanced Historic Events tourism. Germany winning Inca war (+22% score) and will eventually liberate Cologne (plus Stuttgart/Dortmund from Russia). These liberations will generate immediate tourism bonuses. Germany holds 20 Great Works across cities - +2 culture each enhances cultural output. Current policy progress at 19 turns - maintain selection. Future consideration: Third Alternative or Lightning Warfare may provide better military bonuses against Russia.
        
        ## Relationships
        
        ### America
        - Public: 8
        - Private: 5
        - Rationale: America (Defeated) maintains neutral stance at 8/5. Relationship remains stable with no conflicts of interest. America's defeat means no diplomatic complications - maintain positive relationship for any remaining global diplomatic considerations in World Congress. America was DoF partner before defeat - keeping positive relations maintains historic diplomatic consistency. No change needed.
        - UpdatedTurn: 412
        
        ### Venice
        - Public: 20
        - Private: 18
        - Rationale: Venice remains valuable economic partner despite active war (Public 20/Private 18 maintained). Venice military minimal (431 strength), controlled by Enrico Dandolo with Autocracy alignment (same as Germany). Venice maintains DoF with Zulus and Greece but war with Russia - aligning with German interests. Venice's single-city nature with corporate infrastructure (Hanse, trade routes) makes them ideal gold source without territorial competition. Venice war weariness (0%) shows Vietnam not actively prosecuting war - opportunities for separate peace possible. Germany achieving naval superiority in Venice zone (Friendly dominance 486 vs 243). Maintaining positive relations preserves trade route income options if peace concluded, and prevents Venice from aligning against Germany. Venice's 13 World Congress votes also valuable for diplomatic victory coalition considerations.
        - UpdatedTurn: 412
        
        ### The Zulus
        - Public: -50
        - Private: -45
        - Rationale: Zulu relationship maintained at -50/-45 after peace treaty signing (Turn 410, 9 turns remaining). Zulu-Inca defensive pact remains active, but Zulu cannot intervene due to peace treaty obligations. Zulu maintains 5440 military strength (1.58x Germany's 3435), 7 Uranium, and poses credible threat after treaty expires. Zulu's Autocracy alignment shared with Germany provides minimal ideological bonus (999), but insufficient to offset Inca defensive pact and India-Zulu war. Cannot reduce hostility below -50 while Inca war active and Zulu-India conflict ongoing. However, maintaining -50 (not maximum -95) preserves diplomatic flexibility: Zulu peace provides temporary buffer allowing Germany to focus on Russia deterrence and Inca operations. Zulu's 5318 military in previous report improved to 5440 after Ulundi Coaling Station construction. Peace treaty exploitation period critical for Germany's nuclear buildup.
        - UpdatedTurn: 412
        
        ### Greece
        - Public: -35
        - Private: -30
        - Rationale: Greece relationship maintained at -35/-30. India-Greece war escalating - India destroying Greek Anti-Aircraft Gun (Turn 411 #44, #60 events) and advancing with Field Gun bombardment (#59) and Light Tank operations. Greece distracted, reducing threat profile. However, alignment conflict persists: Greece maintains DoF with Inca and Venice, follows Freedom ideology (-999 vs German Autocracy), and completed Broadway cultural wonder. Greece in Golden Age (2 turns) with significant gold reserves (6554), 24 votes - potential diplomatic victory contender. Maintaining guarded hostility acknowledges India's pressure on Greece but不变消极立场 due competing interests. Spy network established in Sparta (Agent Carl gathering intelligence). No relationship reduction while India gains ground - Greece's attention diverted to Indian front. However, stabilize hostility if India achieves breakthrough against Greek positions. Vigilance required as Greece could redirect forces from Indian front.
        - UpdatedTurn: 412
        
        ### The Inca
        - Public: -95
        - Private: -100
        - Rationale: MAXIMUM HOSTILITY MAINTAINED toward Inca (-95/-100). Germany making progress: destroyed Inca Destroyer (event #154), killed Barbarian Machine Gun (event #146). Inca war score -22% (Germany winning at +22%). Vilcabamba health recovered from 2% to 83% - indicates Inca repairs, requires renewed assault. Germany holds Aachen and Cologne under occupation - these cities must be LIBERATED. Inca landship at 1% health (#16-18) damaged by Russian attacks - exploit weakness. Inca hosts hostile Inca and targets Russian troops for coalition coordination. No reconciliation possible until occupied German cities recovered and Inca military neutralized. Maximum hostility required for sustained military operations to prevent Inca recovery.
        - UpdatedTurn: 414
        
        ### Russia
        - Public: -95
        - Private: -95
        - Rationale: MAXIMUM HOSTILITY: Russia nuclear threat EMERGENCY. Russia has 21 Uranium vs Germany 0 (until new quarries active). Russia 9085 military vs Germany 3530 (2.57x superiority). Russia's Bomber ID 15302 active in Moscow zone. Peace treaty EXPIRED (Turn 410) - Russia can declare unrestricted war NOW. Russia holds Stuttgart and Dortmund as occupied territory. Naval activity: Destroyer 16310 near Cologne, Attack Submarine 17257 operating, Submarine 15614 coastal. Spy Agent Katrin in Moscow gathering intelligence (719 Network). Manhattan Project 1 turn from completion - CRITICAL nuclear deterrence race. Russia supreme threat - must maintain -95/-95 until occupied cities returned AND nuclear parity achieved.
        - UpdatedTurn: 414
        
        ### India
        - Public: 12
        - Private: 12
        - Rationale: Slight improvement to India alliance (+2 from +10 each). India demonstrating combat effectiveness against Greece and Inca. While India-Russia DoF complicates immediate coordination, India's cultural victory isn't directly threatening Germany's space pursuit. Improved relations keeps diplomatic channel open for potential coalition against Russia after Zulu peace treaty expires (Turn 431). India's 2167 military and growing power could become strategic counterweight to Russia's 15671 military as alliance dynamics evolve. This is hedging strategy for post-Zulu-treaty landscape.
        - UpdatedTurn: 422
        
        ## Strategy
        - Rationale: Strategic direction remains optimal despite increased Russian threat. Cologne siege making excellent progress with 5+ Destroyers/Fleet Destroyers and Paratrooper positioning for capture and liberation of German territory. Germany produced 2 Fleet Destroyers (major naval upgrades), Great Diplomat for city-state influence, Hamburg completed Broadcast Tower (culture/tourism). Computers research path, Futurism policy selection, Spaceship grand strategy, and all defensive posture settings (Defense/CityDefense/Antiair/Nuke ≥ 90) remain correct. Russia 4.57x military superiority requires continued defensive focus while liberating Cologne and securing nuclear deterrence. Cultural victory threat from India (6 Influential civs) is manageable with Germany's tourism output and future liberations. No strategic changes warranted.
        - GrandStrategy: Spaceship
        
        ### Flavors
        - Offense: 65
        - Defense: 95
        - Mobilization: 80
        - CityDefense: 95
        - MilitaryTraining: 90
        - Recon: 70
        - Ranged: 90
        - Mobile: 80
        - Nuke: 100
        - UseNuke: 90
        - Naval: 92
        - NavalRecon: 45
        - NavalGrowth: 30
        - NavalTileImprovement: 0
        - Air: 90
        - AirCarrier: 35
        - Antiair: 95
        - Airlift: 25
        - Expansion: 0
        - Growth: 60
        - TileImprovement: 20
        - Infrastructure: 95
        - Production: 100
        - WaterConnection: 35
        - Gold: 85
        - Science: 100
        - Culture: 35
        - Happiness: 70
        - GreatPeople: 45
        - Wonder: 5
        - Religion: 20
        - Diplomacy: 75
        - Spaceship: 90
        - Espionage: 95
        
        # Victory Progress
        Victory Progress: current progress towards each type of victory.
        
        ## DominationVictory
        - CapitalsNeeded: 8
        - Contender: Russia
        - India:
          - CapitalsControlled:
            - Athens
            - Delhi
          - CapitalsPercentage: 25
        - Russia:
          - CapitalsControlled:
            - Washington
            - Moscow
          - CapitalsPercentage: 25
        - The Inca:
          - CapitalsControlled:
            - Cusco
            - Venice
          - CapitalsPercentage: 25
        
        ## ScienceVictory
        - Unlocked in the Information era
        
        ## CulturalVictory
        - CivsNeeded: 6
        - Contender: India
        - Germany:
          - Influences:
            - The Inca: Exotic (19%) - Rising Slowly (tourism/culture ratio 147%)
            - The Zulus: Familiar (29%) - Rising Slowly (tourism/culture ratio 59%)
            - Greece: Familiar (26%) - Rising Slowly (tourism/culture ratio 67%)
            - Russia: Exotic (13%) - Rising Slowly (tourism/culture ratio 37%)
            - Venice: Familiar (32%) - Rising Slowly (tourism/culture ratio 76%)
            - India: Exotic (16%) - Rising Slowly (tourism/culture ratio 45%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Greece:
          - Influences:
            - The Inca: Exotic (15%) - Rising Slowly (tourism/culture ratio 178%)
            - Germany: Exotic (21%) - Rising Slowly (tourism/culture ratio 102%)
            - Venice: Exotic (23%) - Rising Slowly (tourism/culture ratio 107%)
            - Russia: Exotic (11%) - Rising Slowly (tourism/culture ratio 41%)
            - The Zulus: Exotic (21%) - Rising Slowly (tourism/culture ratio 71%)
            - India: Exotic (9%) - Rising Slowly (tourism/culture ratio 33%)
          - PolicyPercentage: 96
          - InfluentialCivs: 0
        - India:
          - Influences:
            - The Inca: Influential (119%) - Rising (tourism/culture ratio 779%)
            - Germany: Influential (173%) - Rising (tourism/culture ratio 537%)
            - Greece: Influential (132%) - Rising (tourism/culture ratio 263%)
            - Russia: Influential (100%) - Rising (tourism/culture ratio 225%)
            - The Zulus: Influential (137%) - Rising (tourism/culture ratio 282%)
            - Venice: Influential (143%) - Rising (tourism/culture ratio 352%)
          - PolicyPercentage: 100
          - InfluentialCivs: 6
        - Russia:
          - Influences:
            - The Inca: Familiar (36%) - Rising Slowly (tourism/culture ratio 52%)
            - Germany: Familiar (35%) - Rising Slowly (tourism/culture ratio 6%)
            - Greece: Familiar (31%) - Rising Slowly (tourism/culture ratio 5%)
            - The Zulus: Familiar (37%) - Rising Slowly (tourism/culture ratio 11%)
            - Venice: Familiar (30%) - Rising Slowly (tourism/culture ratio 3%)
            - India: Exotic (23%) - Rising Slowly (tourism/culture ratio 8%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Inca:
          - Influences:
            - Germany: Familiar (44%) - Rising Slowly (tourism/culture ratio 72%)
            - Greece: Familiar (35%) - Rising Slowly (tourism/culture ratio 61%)
            - The Zulus: Popular (52%) - Rising Slowly (tourism/culture ratio 76%)
            - Russia: Exotic (23%) - Rising Slowly (tourism/culture ratio 25%)
            - Venice: Popular (91%) - Rising (21 turns to Influential, tourism/culture ratio 218%)
            - India: Exotic (22%) - Rising Slowly (tourism/culture ratio 28%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - The Zulus:
          - Influences:
            - The Inca: Familiar (32%) - Rising (416 turns to Influential, tourism/culture ratio 225%)
            - Germany: Familiar (41%) - Rising Slowly (tourism/culture ratio 118%)
            - Greece: Familiar (34%) - Rising Slowly (tourism/culture ratio 79%)
            - Russia: Exotic (23%) - Rising Slowly (tourism/culture ratio 53%)
            - Venice: Popular (72%) - Rising (102 turns to Influential, tourism/culture ratio 189%)
            - India: Exotic (19%) - Rising Slowly (tourism/culture ratio 41%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        - Venice:
          - Influences:
            - The Inca: Exotic (23%) - Rising Slowly (tourism/culture ratio 139%)
            - Germany: Familiar (32%) - Rising Slowly (tourism/culture ratio 77%)
            - Greece: Familiar (28%) - Rising Slowly (tourism/culture ratio 61%)
            - Russia: Exotic (17%) - Rising Slowly (tourism/culture ratio 27%)
            - The Zulus: Familiar (42%) - Rising Slowly (tourism/culture ratio 64%)
            - India: Exotic (13%) - Rising Slowly (tourism/culture ratio 23%)
          - PolicyPercentage: 100
          - InfluentialCivs: 0
        
        ## DiplomaticVictory
        - VotesNeeded: 44
        - Status: World Congress - Voting in 8 turns
        - ActiveResolutions:
          - Sanction: Russia:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 412
          - Sanction: India:
            - Description: No Trade Routes, Deals, or Corporation Franchises can be established with the chosen Civilization (excluding Vassals). Their Corporation Franchises are removed from foreign cities. 0.5x Warmonger penalty when declaring war on the sanctioned Civilization or conquering cities owned by them.
            - EnactedOn: 412
          - Global Peace Accords:
            - Description: Unit maintenance costs are raised by 25% Gold. 2.0x Warmonger penalties for capturing cities and declaring war, and 0.5x Warmonger scores decay.
            - EnactedOn: 412
          - Incan Sphere of Influence: Kathmandu:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Greek Sphere of Influence: Vienna:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Zulu Sphere of Influence: M'banza-Kongo:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 421
          - Greek Sphere of Influence: Quebec City:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Scholars In Residence:
            - Description: Civilizations have -20% Research cost for Technologies already discovered by another Civilization. Additional -2% for every City-State Ally, up to -50%.
            - EnactedOn: 412
          - World Ideology: Freedom:
            - Description: Designate an Ideology as the official World Ideology. Civilizations following the Ideology get an additional Delegate, plus 1 Delegate for every other Civilization that follows the Ideology. Public opinion in favor of that Ideology is increased for all Civilizations. Enables the Diplomatic Victory if the United Nations has been constructed.
              Available once any Civilization discovers Nuclear Fission.
            - EnactedOn: 412
          - Greek Sphere of Influence: Trowulan:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Travel Ban:
            - Description: Restricts international travel between Civilizations. Reduces the Tourism modifier for all Civilizations by 35%.
              Available once any Civilization discovers Flight.
            - EnactedOn: 412
          - Greek Sphere of Influence: Melbourne:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - EnactedOn: 412
          - Open Door: Zuunmod:
            - Description: Enact an Open Door policy for a City-State. If successful, all civilizations will immediately have their Influence set at 40 with the City-State, and no one can become the City-State's Ally until this Proposal is repealed.
            - EnactedOn: 412
        - Proposals:
          - Enact: Endowment for the Arts:
            - Description: Increases up to 33% generation of Great Writers, Artists, and Musicians. Decreases up to 33% generation of Great Scientists, Engineers, and Merchants.
              Civilizations with Scores from Policies and Great Works below the global median will receive a boost to Production and Culture up to 33%.
              Details: The boosts are proportional to the difference between the score of the Civilization and the leader.
            - Proposer: The Inca
          - Enact: Venetian Sphere of Influence: Tyre:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: Venice
          - Repeal: Incan Sphere of Influence: Kathmandu:
            - Description: Demand a Sphere of Influence over a City-State. If successful, the proposing player becomes the permanent Ally of the City-State (unless this Proposal is repealed). The proposer must be the current ally of the City-State.
              Available once any Civilization discovers Steam Power.
            - Proposer: Greece
        - Contender: Greece
        - Germany:
          - Delegates: 6
          - VictoryPercentage: 13
        - Greece:
          - Delegates: 25
          - VictoryPercentage: 56
        - India:
          - Delegates: 7
          - VictoryPercentage: 15
        - Russia:
          - Delegates: 3
          - VictoryPercentage: 6
        - The Inca:
          - Delegates: 17
          - VictoryPercentage: 38
        - The Zulus:
          - Delegates: 8
          - VictoryPercentage: 18
        - Venice:
          - Delegates: 13
          - VictoryPercentage: 29
        
        # Players
        Players: summary reports about visible players in the world.
        
        - 0: Defeated Major Civilization America
        
        ## Player 1
        - Civilization: Russia
        - Leader: Catherine
        - IsMajor: true
        - OurOpinionToThem:
          - We fought together against a common foe. (99)
          - You have denounced one of their declared enemies! (11)
          - We have made Declarations of Friendship with the same leaders! (8)
          - We have Pledged to Protect the same City-States. (7)
          - You have gone to war in the past.
          - Our real approach is Hostile.
          - We have divergent Social Policies. (-3)
          - Our leader has expressed a public opinion to this player (-95).
          - Our leader has formed a private opinion to this player (-95).
          - They believe your warmongering has become an existential threat. (-168)
          - You have chosen to adopt the Order Ideology, but they believe in Autocracy. (-999)
        - TheirOpinionToUs:
          - You have denounced one of their declared enemies!
          - You have no contested borders.
          - Your votes supported their civ's interests in the World Congress.
          - We have made Declarations of Friendship with the same leaders!
          - We fought together against a common foe.
          - We have Pledged to Protect the same City-States.
          - You have gone to war in the past.
          - They don't want anything to do with us right now.
          - You are competing for the favor of the same City-States!
          - We have divergent Social Policies.
          - Your military deployment is extremely threatening.
          - We have denounced them!
          - Your spies were caught stealing from them.
          - You have chosen to adopt the Autocracy Ideology, but they believe in Order.
        - Score: 3135
        - Era: Information
        - Technologies: 67
        - Cities: 22
        - Population: 473
        - Territory: 618
        - Gold: 354
        - GoldPerTurn: -458
        - HappinessSituation: Unhappy - combat penalty
        - HappinessPercentage: 47
        - MilitaryStrength: 15440
        - TourismPerTurn: 976.2
        - CulturePerTurn: 2325
        - PolicyBranches:
          - Fealty: 6
          - Order: 7
          - Imperialism: 6
          - Progress: 6
        - ResourcesAvailable:
          - Wheat: 7
          - Sheep: 13
          - Ivory: 1
          - Paper: 7
          - Pearls: 1
          - Maize: 3
          - Rice: 5
          - Gems: 5
          - Salt: 1
          - Aluminum: 74
          - Lapis Lazuli: 5
          - Fish: 15
          - Perfume: 2
          - Deer: 7
          - Jade: 10
          - Iron: 39
          - Dyes: 1
          - Coal: 16
          - Cattle: 7
          - Uranium: 19
          - Horses: -2
          - Bison: 3
          - Copper: 2
          - Truffles: 2
          - Stone: 8
          - Marble: 2
          - Bananas: 5
          - Cocoa: 4
          - Tobacco: 3
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - War (Our Score: 100%; Our War Weariness: 93%)
            - Denounced Them
          - Germany:
            - Distance: Neighbors
          - Greece:
            - Distance: Neighbors
            - Denounced Them
          - The Zulus:
            - Distance: Neighbors
            - Denounced Them
          - Venice:
            - Distance: Neighbors
            - War (Our Score: 80%; Our War Weariness: 99%)
            - Denounced Them
          - India:
            - Distance: Neighbors
            - Declaration of Friendship
        - Votes: 3
        
        ## Player 2
        - Civilization: Greece
        - Leader: Alexander
        - IsMajor: true
        - OurOpinionToThem:
          - You have denounced one of their declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - Our real approach is Hostile.
          - We have divergent Social Policies. (-3)
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Our leader has formed a private opinion to this player (-30).
          - Religious differences strain your relationship. (-30)
          - Our leader has expressed a public opinion to this player (-35).
          - You have chosen to adopt the Freedom Ideology, but they believe in Autocracy. (-999)
        - TheirOpinionToUs:
          - You liberated them without being asked to.
          - You have no contested borders.
          - You have denounced one of their declared enemies!
          - We have Pledged to Protect the same City-States.
          - We are trade partners.
          - You have gone to war in the past.
          - They don't want anything to do with us right now.
          - Your recent diplomatic actions disappoint them.
          - Religious differences strain your relationship.
          - We have divergent Social Policies.
          - Their friends or allies have denounced you!
          - You are competing for the favor of the same City-States!
          - You have made a Declaration of Friendship with one of their enemies!
          - You have denounced a leader they made a Declaration of Friendship with!
          - We have denounced each other!
          - Your spies were caught stealing from them.
          - We defeated their proposal in the World Congress.
          - Your votes opposed their civ's interests in the World Congress.
          - You have chosen to adopt the Autocracy Ideology, but they believe in Freedom.
        - Score: 1871
        - Era: Atomic
        - Technologies: 64
        - Cities: 5
        - Population: 124
        - Territory: 219
        - Gold: 1338
        - GoldPerTurn: 114
        - HappinessSituation: Happy
        - HappinessPercentage: 100
        - MilitaryStrength: 3925
        - TourismPerTurn: 403
        - CulturePerTurn: 928
        - PolicyBranches:
          - Statecraft: 6
          - Freedom: 4
          - Tradition: 6
          - Industry: 6
        - ResourcesAvailable:
          - Wheat: 3
          - Sheep: 3
          - Ivory: 1
          - Gold: 1
          - Paper: 6
          - Pearls: 2
          - Maize: 3
          - Gems: 1
          - Salt: 1
          - Glass: 2
          - Fish: 4
          - Perfume: 1
          - Deer: 3
          - Whales: 1
          - Iron: 2
          - Dyes: 1
          - Coal: 6
          - Cattle: 1
          - Uranium: 5
          - Horses: 2
          - Coral: 1
          - Jewelry: 2
          - Citrus: 3
          - Copper: 1
          - Incense: 1
          - Stone: 2
          - Marble: 1
          - Furs: 1
          - Porcelain: 1
          - Tobacco: 1
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Far
            - Open Borders
          - Germany:
            - Distance: Close
            - Denounced Them
          - Venice:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Russia:
            - Distance: Neighbors
            - Denounced Them
          - The Zulus:
            - Distance: Distant
            - Open Borders
          - India:
            - Distance: Neighbors
            - War (Our Score: -10%; Our War Weariness: 63%)
            - Denounced Them
        - Votes: 25
        
        ## Player 3
        - Civilization: The Inca
        - Leader: Pachacuti
        - IsMajor: true
        - OurOpinionToThem:
          - We fought together against a common foe. (55)
          - We have similar Social Policies. (3)
          - Our real approach is War.
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - Religious differences strain your relationship. (-30)
          - Your spies were caught stealing from them. (-33)
          - You stole their territory! (-50)
          - Our leader has expressed a public opinion to this player (-95).
          - Our leader has formed a private opinion to this player (-100).
          - You have chosen to adopt the Freedom Ideology, but they believe in Autocracy. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You have denounced one of their declared enemies!
          - You are not competing for technological advancement.
          - You have no contested borders.
          - We passed their proposal in the World Congress.
          - We have similar Social Policies.
          - You plundered their trade routes!
          - Religious differences strain your relationship.
          - Their friends or allies have denounced you!
          - Your spies were caught stealing from them.
          - You have made a Declaration of Friendship with one of their enemies!
          - We have denounced each other!
          - Your votes opposed their civ's interests in the World Congress.
          - You have denounced a leader they made a Declaration of Friendship with!
          - You have chosen to adopt the Autocracy Ideology, but they believe in Freedom.
          - You are at war!
        - Score: 1722
        - Era: Information
        - Technologies: 69
        - Cities: 5
        - Population: 102
        - Territory: 153
        - Gold: 820
        - GoldPerTurn: 360
        - HappinessSituation: Happy
        - HappinessPercentage: 55
        - MilitaryStrength: 1344
        - TourismPerTurn: 331.25
        - CulturePerTurn: 586
        - PolicyBranches:
          - Statecraft: 6
          - Freedom: 7
          - Progress: 6
          - Rationalism: 6
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 5
          - Ivory: 1
          - Paper: 9
          - Maize: 2
          - Salt: 1
          - Aluminum: 3
          - Lapis Lazuli: 1
          - Fish: 2
          - Amber: 1
          - Perfume: 2
          - Deer: 1
          - Whales: 1
          - Iron: 5
          - Cattle: 1
          - Uranium: 3
          - Bison: 1
          - Copper: 2
          - Furs: 1
        - FoundedReligion: Catholicism
        - Relationships:
          - Germany:
            - Distance: Close
            - War (Our Score: -32%; Our War Weariness: 81%)
            - Denounced Them
          - Greece:
            - Distance: Far
            - Open Borders
          - The Zulus:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Russia:
            - Distance: Neighbors
            - War (Our Score: -100%; Our War Weariness: 100%)
          - Venice:
            - Distance: Far
            - Our Vassal (Voluntary)
            - Open Borders
            - Declaration of Friendship
          - India:
            - Distance: Neighbors
            - War (Our Score: -8%; Our War Weariness: 26%)
            - Denounced Them
        - Votes: 17
        
        ## Player 4
        - Civilization: India
        - Leader: Gandhi
        - IsMajor: true
        - OurOpinionToThem:
          - We fought together against a common foe. (93)
          - They have happily adopted your religion in the majority of their cities. (30)
          - Our leader has expressed a public opinion to this player (12).
          - Our leader has formed a private opinion to this player (12).
          - You have denounced one of their declared enemies! (11)
          - We have made a public Declaration of Friendship! (9)
          - We have Pledged to Protect the same City-States. (7)
          - We have shared embassies. (1)
          - Our real approach is Friendly.
          - We have divergent Social Policies. (-3)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have chosen to adopt the Order Ideology, but they believe in Autocracy. (-999)
        - TheirOpinionToUs:
          - You have denounced one of their declared enemies!
          - Your votes supported their civ's interests in the World Congress.
          - We fought together against a common foe.
          - The leader has expressed a public opinion to you (30).
          - You have adopted their religion in the majority of your cities.
          - We have made a public Declaration of Friendship!
          - We are trade partners.
          - We have Pledged to Protect the same City-States.
          - We freed them from sanctions in the World Congress.
          - We have shared embassies.
          - We have divergent Social Policies.
          - You have chosen to adopt the Autocracy Ideology, but they believe in Order.
          - They desire friendly relations with our empire.
          - We defeated their proposal in the World Congress.
          - You have denounced a leader they made a Declaration of Friendship with!
        - Score: 2357
        - Era: Atomic
        - Technologies: 65
        - Cities: 6
        - Population: 174
        - Territory: 239
        - Gold: 975
        - GoldPerTurn: 15
        - HappinessSituation: Happy
        - HappinessPercentage: 71
        - MilitaryStrength: 1836
        - TourismPerTurn: 1189.75
        - CulturePerTurn: 1774
        - PolicyBranches:
          - Tradition: 6
          - Rationalism: 2
          - Progress: 3
          - Authority: 1
          - Fealty: 1
          - Industry: 1
          - Artistry: 6
          - Statecraft: 3
          - Order: 4
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 2
          - Ivory: 1
          - Gold: 5
          - Paper: 10
          - Cotton: 9
          - Aluminum: 8
          - Bison: 1
          - Perfume: 2
          - Deer: 8
          - Iron: 13
          - Coal: 11
          - Fish: 1
          - Uranium: 2
          - Horses: 5
          - Incense: 2
          - Stone: 1
          - Oil: 3
        - FoundedReligion: Hinduism
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - War (Our Score: 8%; Our War Weariness: 18%)
            - Denounced Them
          - Germany:
            - Distance: Neighbors
            - Declaration of Friendship
          - Greece:
            - Distance: Neighbors
            - War (Our Score: 10%; Our War Weariness: 54%)
            - Denounced Them
          - Russia:
            - Distance: Neighbors
            - Declaration of Friendship
          - The Zulus:
            - Distance: Close
            - War (Our Score: -10%; Our War Weariness: 16%)
            - Denounced Them
          - Venice:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 9%)
            - Denounced Them
        - Votes: 7
        
        ## Player 5
        - Civilization: Venice
        - Leader: Enrico Dandolo
        - IsMajor: true
        - OurOpinionToThem:
          - Our leader has expressed a public opinion to this player (20).
          - Our leader has formed a private opinion to this player (18).
          - You have denounced one of their declared enemies! (11)
          - Our real approach is War.
          - We have divergent Social Policies. (-3)
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - Religious differences strain your relationship. (-30)
          - You have adopted the Freedom Ideology, but they believe in Autocracy. (-999)
          - You are at war! (-99999)
        - TheirOpinionToUs:
          - You are not competing for the favor of the same City-States.
          - You have denounced one of their declared enemies!
          - Your votes supported their civ's interests in the World Congress.
          - The leader has expressed a public opinion to you (15).
          - You have no contested borders.
          - We are completely untrustworthy to them.
          - Your recent diplomatic actions disappoint them.
          - Religious differences strain your relationship.
          - We have divergent Social Policies.
          - You have made a Declaration of Friendship with one of their enemies!
          - Their friends or allies have denounced you!
          - We previously defeated their proposal in the World Congress.
          - We have denounced each other!
          - You have denounced a leader they made a Declaration of Friendship with!
          - You have chosen to adopt the Autocracy Ideology, but they believe in Freedom.
          - You are at war!
        - Score: 1428
        - Era: Atomic
        - Technologies: 62
        - Cities: 4
        - Population: 107
        - Territory: 161
        - Gold: 298
        - GoldPerTurn: -2
        - HappinessSituation: Happy
        - HappinessPercentage: 79
        - MilitaryStrength: 360
        - TourismPerTurn: 300.86
        - CulturePerTurn: 559
        - PolicyBranches:
          - Freedom: 2
          - Tradition: 3
          - Rationalism: 2
          - Imperialism: 1
          - Authority: 3
          - Fealty: 1
          - Industry: 2
          - Artistry: 2
          - Statecraft: 5
        - ResourcesAvailable:
          - Wheat: 1
          - Sheep: 1
          - Ivory: 1
          - Paper: 10
          - Salt: 1
          - Aluminum: 8
          - Glass: 1
          - Lapis Lazuli: 1
          - Fish: 3
          - Amber: 1
          - Perfume: 1
          - Deer: 4
          - Iron: 2
          - Uranium: 4
          - Horses: 1
          - Copper: 1
          - Stone: 1
          - Furs: 3
          - Bananas: 1
          - Tobacco: 1
        - FoundedReligion: Buddhism
        - Relationships:
          - The Inca:
            - Distance: Far
            - Our Master (Voluntary)
            - Open Borders
            - Declaration of Friendship
          - Germany:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
          - Greece:
            - Distance: Distant
            - Open Borders
            - Declaration of Friendship
          - Russia:
            - Distance: Neighbors
            - War (Our Score: -80%; Our War Weariness: 100%)
            - Denounced Them
          - The Zulus:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - India:
            - Distance: Distant
            - War (Our Score: 0%; Our War Weariness: 0%)
            - Denounced Them
        - Votes: 13
        
        ## Player 6
        - Civilization: Germany
        - Leader: Bismarck
        - IsMajor: true
        - MyEvaluations:
          - Our top friend: India, Our top defensive pact ally: None
          - Our top World Congress ally: None, Our top World Congress rival: Greece
          - Our top Competitor: Russia
        - Score: 1712
        - Era: Atomic
        - GoldenAge: Estimated in 33 turns
        - Technologies: 63
        - CurrentResearch: Computers (Estimated in 13 turns)
        - NextPolicyTurns: 14
        - Cities: 6
        - Population: 129
        - Territory: 170
        - BestSettlementLocation:
          - 72, 33 (Quality: 86%; 11 tiles from us; New Continent)
          - 60, 50 (Quality: 43%; 6 tiles from us)
          - 59, 49 (Quality: 0%; 5 tiles from us)
          - 59, 50 (Quality: 0%; 6 tiles from us)
          - 49, 16 (Quality: 0%; 4 tiles from us)
        - Gold: 247
        - GoldPerTurn: 10
        - HappinessSituation: Happy
        - HappinessPercentage: 61
        - MilitaryUnits: 45
        - MilitarySupply: 51
        - MilitaryStrength: 3335
        - TourismPerTurn: 480.5
        - CulturePerTurn: 766
        - FaithPerTurn: 220
        - SciencePerTurn: 998
        - PolicyBranches:
          - Autocracy:
            - Elite Forces
            - Military-Industrial Complex
            - United Front
          - Artistry:
            - Artistry
            - Humanism
            - Refinement
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
          - Statecraft:
            - Statecraft
            - Foreign Service
            - Trade Confederacy
          - Imperialism:
            - Imperialism
            - Martial Law
            - Colonialism
            - Regimental System
            - Civilizing Mission
        - ResourcesAvailable:
          - Wheat: 1
          - Silver: 0
          - Sheep: 2
          - Cloves: 0
          - Figs: 0
          - Ivory: 0
          - Gold: 3
          - Nutmeg: 0
          - Paper: 4
          - Pearls: 0
          - Maize: 3
          - Rice: 3
          - Cotton: 0
          - Gems: 6
          - Salt: 0
          - Brazilwood: 0
          - Aluminum: 10
          - Glass: 0
          - Lapis Lazuli: 0
          - Fish: 6
          - Amber: 0
          - Perfume: 2
          - Deer: 5
          - Whales: 0
          - Olives: 0
          - Sugar: 0
          - Jade: 0
          - Iron: 1
          - Dyes: 0
          - Tea: 0
          - Coal: 1
          - Coffee: 0
          - Cattle: 1
          - Pepper: 0
          - Uranium: 3
          - Horses: 4
          - Coral: 0
          - Silk: 0
          - Jewelry: 0
          - Bison: 3
          - Antiquity Site: 0
          - Citrus: 0
          - Copper: 0
          - Truffles: 0
          - Crab: 1
          - Incense: 0
          - Stone: 0
          - Marble: 3
          - Furs: 0
          - Cinnamon: 0
          - Bananas: 0
          - Oil: 0
          - Wine: 0
          - Porcelain: 1
          - Cocoa: 0
          - Tobacco: 0
        - FoundedReligion: Pantheon (Religion Impossible)
        - Relationships:
          - The Inca:
            - Distance: Close
            - War (Our Score: 32%; Our War Weariness: 38%)
            - Denounced Them
          - The Zulus:
            - Distance: Close
            - Denounced Them
          - Greece:
            - Distance: Close
            - Denounced Them
          - Russia:
            - Distance: Neighbors
            - Denounced Them
          - Venice:
            - Distance: Far
            - War (Our Score: 0%; Our War Weariness: 25%)
            - Denounced Them
          - India:
            - Distance: Neighbors
            - Declaration of Friendship
        - OutgoingTradeRoutes:
          - Hamburg (Germany) => Munich (Germany):
            - TurnsLeft: 27
            - Domain: Land
            - ToProduction: 23
          - Berlin (Germany) => Trowulan (City-State Trowulan):
            - TurnsLeft: 2
            - Domain: Sea
            - FromGold: 29.58
          - Berlin (Germany) => Oviedo (City-State Oviedo):
            - TurnsLeft: 20
            - Domain: Land
            - FromGold: 38.66
          - Berlin (Germany) => Antananarivo (City-State Antananarivo):
            - TurnsLeft: 24
            - FromScience: 7.5
            - Domain: Land
            - FromGold: 43.55
            - FromCulture: 7.5
          - Hamburg (Germany) => Antwerp (City-State Antwerp):
            - TurnsLeft: 22
            - Domain: Land
            - FromGold: 42.32
          - Berlin (Germany) => Segou (City-State Segou):
            - TurnsLeft: 37
            - Domain: Sea
            - FromGold: 39.28
          - Frankfurt (Germany) => Melbourne (City-State Melbourne):
            - TurnsLeft: 2
            - Domain: Sea
            - FromGold: 35.11
          - Berlin (Germany) => Munich (Germany):
            - TurnsLeft: 2
            - Domain: Land
            - ToProduction: 22
        - Spies:
          - Agent Eva (0):
            - State: Rigging Election
            - Role: Spy
            - Location: Antwerp (City-State Antwerp)
            - NetworkPerTurn: 0
          - Agent Wilhelm (3):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 346
            - Location: Sparta (Greece)
            - NetworkPerTurn: 42
          - Agent Conrad (2):
            - State: Rigging Election
            - Role: Spy
            - Location: Lutetia (City-State Lutetia)
            - NetworkPerTurn: 0
          - Agent Viper (7):
            - State: Rigging Election
            - Role: Spy
            - Location: Oviedo (City-State Oviedo)
            - NetworkPerTurn: 0
          - Agent Carl (6):
            - State: Rigging Election
            - Role: Spy
            - Location: Shanghai (City-State Shanghai)
            - NetworkPerTurn: 0
          - Agent Schimanski (5):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 1459
            - Location: Ulundi (The Zulus)
            - NetworkPerTurn: 23
          - Agent Erich (1):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 296
            - Location: Cusco (The Inca)
            - NetworkPerTurn: 38
          - Agent Katrin (4):
            - State: Gathering Intelligence
            - Role: Spy
            - Network: 166
            - Location: Moscow (Russia)
            - NetworkPerTurn: 10
        - DiplomaticDeals:
          - Russia:
            - #0:
              - WeGive:
                - Peace Treaty
                - Make Peace with City-State Antwerp
                - 84 Gold
                - 5 Gold per Turn
              - TheyGive:
                - Peace Treaty
              - TurnsRemaining: -21
        - Votes: 6
        
        ## Player 7
        - Civilization: The Zulus
        - Leader: Shaka
        - IsMajor: true
        - OurOpinionToThem:
          - You have both chosen to adopt the Autocracy Ideology. (999)
          - You have denounced one of their declared enemies! (11)
          - We have Pledged to Protect the same City-States. (7)
          - We have similar Social Policies. (3)
          - Our real approach is Guarded.
          - You have denounced a leader they made a Declaration of Friendship with! (-11)
          - You have made a Declaration of Friendship with one of their enemies! (-13)
          - You have made a Defensive Pact with one of their enemies! (-15)
          - They have some early concerns about your warmongering. (-19)
          - Religious differences strain your relationship. (-30)
          - Our leader has formed a private opinion to this player (-45).
          - Our leader has expressed a public opinion to this player (-50).
        - TheirOpinionToUs:
          - You have both chosen to adopt the Autocracy Ideology.
          - Your votes supported their civ's interests in the World Congress.
          - You have denounced one of their declared enemies!
          - You have no contested borders.
          - We have Pledged to Protect the same City-States.
          - You are not competing for technological advancement.
          - We have similar Social Policies.
          - You have gone to war in the past.
          - We have different religious beliefs.
          - They do not consider us relevant to their interests.
          - You are competing for the favor of the same City-States!
          - You have made a Declaration of Friendship with one of their enemies!
          - The leader has expressed a public opinion to you (-32).
          - Their friends or allies have denounced you!
          - We have denounced them!
          - You have denounced a leader they made a Declaration of Friendship with!
        - Score: 2182
        - Era: Atomic
        - GoldenAge: 10 turns remaining
        - Technologies: 65
        - Cities: 9
        - Population: 218
        - Territory: 246
        - Gold: 1610
        - GoldPerTurn: 501
        - HappinessSituation: Happy
        - HappinessPercentage: 54
        - MilitaryStrength: 6167
        - TourismPerTurn: 616.5
        - CulturePerTurn: 1318
        - PolicyBranches:
          - Rationalism: 3
          - Progress: 6
          - Authority: 3
          - Fealty: 1
          - Industry: 2
          - Artistry: 1
          - Statecraft: 4
          - Autocracy: 2
          - Imperialism: 1
        - ResourcesAvailable:
          - Wheat: 2
          - Sheep: 5
          - Ivory: 2
          - Paper: 7
          - Salt: 5
          - Aluminum: 17
          - Lapis Lazuli: 1
          - Fish: 10
          - Perfume: 1
          - Deer: 8
          - Whales: 1
          - Olives: 2
          - Iron: 1
          - Coal: -3
          - Cattle: 1
          - Uranium: 8
          - Coral: 1
          - Bison: 5
          - Citrus: 1
          - Copper: 1
          - Crab: 1
          - Incense: 1
          - Stone: 4
          - Furs: 1
          - Tobacco: 1
        - FoundedReligion: Protestantism
        - Relationships:
          - The Inca:
            - Distance: Neighbors
            - Defensive Pact
            - Open Borders
            - Declaration of Friendship
          - Germany:
            - Distance: Close
          - Greece:
            - Distance: Distant
            - Open Borders
          - Russia:
            - Distance: Neighbors
            - Denounced Them
          - Venice:
            - Distance: Neighbors
            - Open Borders
            - Declaration of Friendship
          - India:
            - Distance: Close
            - War (Our Score: 10%; Our War Weariness: 11%)
            - Denounced Them
        - Votes: 8
        
        ## Player 22
        - Civilization: Melbourne
        - Leader: City State
        - MajorAlly: Greece
        - Population: 29
        - ResourcesAvailable:
          - Fish: 5
          - Bison: 1
          - Sheep: 1
        - MajorityReligion: Buddhism
        - Relationships:
          - The Inca: Friends (Influence: 112, Distance: Far)
          - Germany: Friends (Influence: 681, Distance: Neighbors, Protected)
          - Greece: Ally (Influence: 749, Distance: Distant, Protected)
          - The Zulus: Friends (Influence: 181, Distance: Far)
          - Russia: Friends (Influence: 131, Distance: Far, Protected)
          - Venice: Friends (Influence: 289, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        - Quests:
          -  Diplomatic Missions are temporarily more effective. (Turns remaining: 24)
        
        ## Player 23
        - Civilization: Trowulan
        - Leader: City State
        - MajorAlly: Greece
        - Population: 33
        - ResourcesAvailable:
          - Fish: 7
        - Relationships:
          - The Inca: Neutral (Influence: 0, Distance: Far)
          - Germany: Friends (Influence: 341, Distance: Close, Protected)
          - Greece: Ally (Influence: 744, Distance: Close, Protected)
          - The Zulus: Friends (Influence: 201, Distance: Far)
          - Russia: Friends (Influence: 394, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 114, Distance: Far)
          - India: War (Influence: -60, Distance: Close)
        - Quests:
          -  They want you to liberate the city of Singapore. (Turns remaining: 14) Potential Quest Reward: * 285 Influence * 4 Happiness in Capital
        - 24: Defeated Minor Civilization Vatican City
        
        ## Player 25
        - Civilization: Quebec City
        - Leader: City State
        - MajorAlly: Greece
        - Population: 25
        - ResourcesAvailable:
          - Fish: 4
        - MajorityReligion: Hinduism
        - Relationships:
          - The Inca: Friends (Influence: 210, Distance: Far)
          - Germany: Friends (Influence: 711, Distance: Neighbors, Protected)
          - Greece: Ally (Influence: 886, Distance: Neighbors, Protected)
          - The Zulus: Friends (Influence: 71, Distance: Distant)
          - Russia: Friends (Influence: 204, Distance: Close, Protected)
          - Venice: Friends (Influence: 338, Distance: Far)
          - India: War (Influence: -60, Distance: Close)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 26
        - Civilization: Antwerp
        - Leader: City State
        - MajorAlly: Greece
        - Population: 18
        - ResourcesAvailable:
          - Cattle: 1
          - Fish: 2
          - Wheat: 1
          - Sheep: 1
        - Relationships:
          - The Inca: Neutral (Influence: -21, Distance: Close)
          - Germany: Friends (Influence: 289, Distance: Distant, Protected)
          - Greece: Ally (Influence: 1334, Distance: Distant)
          - The Zulus: Friends (Influence: 374, Distance: Neighbors)
          - Russia: Friends (Influence: 422, Distance: Neighbors, Protected)
          - Venice: Neutral (Influence: 0, Distance: Close)
          - India: War (Influence: -60, Distance: Far)
        - Quests:
          -  They want you to generate a Great Scientist. (Turns remaining: 40) Potential Quest Reward: * 173 Influence * 505 Culture
        
        ## Player 27
        - Civilization: Shanghai
        - Leader: City State
        - MajorAlly: Greece
        - Population: 18
        - Relationships:
          - The Inca: Neutral (Influence: 0, Distance: Close)
          - Germany: Friends (Influence: 143, Distance: Distant, Protected)
          - Greece: Ally (Influence: 831, Distance: Distant, Protected)
          - The Zulus: Friends (Influence: 52, Distance: Close)
          - Russia: Friends (Influence: 214, Distance: Neighbors, Protected)
          - Venice: Neutral (Influence: 23, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        - Quests:
          -  They want you to start a land or sea trade route to their city. (Turns remaining: 21) Potential Quest Reward: * 218 Influence * 351 Food in Capital
          - They want you to send them an Light Tank with at least 75 XP. (Turns remaining: 41) Potential Quest Reward: * 169 Influence * 402 Gold
        
        ## Player 28
        - Civilization: Oviedo
        - Leader: City State
        - MajorAlly: The Zulus
        - Population: 12
        - ResourcesAvailable:
          - Bison: 2
        - Relationships:
          - The Inca: Neutral (Influence: 0, Distance: Far)
          - Germany: Friends (Influence: 53, Distance: Distant, Protected)
          - Greece: Friends (Influence: 921, Distance: Distant)
          - The Zulus: Ally (Influence: 1030, Distance: Neighbors, Protected)
          - Russia: Friends (Influence: 390, Distance: Neighbors, Protected)
          - Venice: Neutral (Influence: 4, Distance: Close)
          - India: War (Influence: -60, Distance: Distant)
        - Quests:
          -  They want you to send them a Paratrooper with at least 75 XP. (Turns remaining: 43) Potential Quest Reward: * 176 Influence * 379 Gold
        - 29: Defeated Minor Civilization Singapore
        
        ## Player 30
        - Civilization: M'banza-Kongo
        - Leader: City State
        - MajorAlly: The Zulus
        - Population: 21
        - ResourcesAvailable:
          - Fish: 2
          - Deer: 1
          - Sheep: 1
        - MajorityReligion: Protestantism
        - Relationships:
          - The Inca: Neutral (Influence: 26, Distance: Close)
          - Germany: Friends (Influence: 62, Distance: Far)
          - Greece: Friends (Influence: 225, Distance: Distant, Protected)
          - The Zulus: Ally (Influence: 343, Distance: Close, Protected)
          - Russia: Friends (Influence: 131, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 43, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        - Quests:
          -  They want you to generate a Great Admiral. (Turns remaining: 40) Potential Quest Reward: * 148 Influence * 447 Culture
        
        ## Player 31
        - Civilization: Zuunmod
        - Leader: City State
        - Population: 23
        - ResourcesAvailable:
          - Fish: 3
          - Horses: 1
          - Sheep: 1
          - Oil: 3
          - Tobacco: 1
        - Relationships:
          - The Inca: Neutral (Influence: 26, Distance: Distant)
          - Germany: Friends (Influence: 158, Distance: Neighbors, Protected)
          - Greece: Friends (Influence: 216, Distance: Close, Protected)
          - The Zulus: Friends (Influence: 69, Distance: Distant)
          - Russia: Friends (Influence: 313, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 43, Distance: Distant)
          - India: Neutral (Influence: -58, Distance: Far)
        - Quests:
          -  They want you to generate a Great Engineer. (Turns remaining: 47) Potential Quest Reward: * 173 Influence * 505 Culture
        
        ## Player 32
        - Civilization: Tyre
        - Leader: City State
        - MajorAlly: Greece
        - Population: 17
        - ResourcesAvailable:
          - Fish: 1
          - Sheep: 1
        - MajorityReligion: Hinduism
        - Relationships:
          - The Inca: Friends (Influence: 216, Distance: Close)
          - Germany: Neutral (Influence: -3, Distance: Far)
          - Greece: Ally (Influence: 548, Distance: Distant)
          - The Zulus: Neutral (Influence: 17, Distance: Close, Protected)
          - Russia: Neutral (Influence: -54, Distance: Far)
          - Venice: Friends (Influence: 357, Distance: Distant)
          - India: War (Influence: -60, Distance: Close)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 33
        - Civilization: Segou
        - Leader: City State
        - MajorAlly: Greece
        - Population: 27
        - ResourcesAvailable:
          - Fish: 5
          - Sheep: 1
        - Relationships:
          - The Inca: Friends (Influence: 713, Distance: Neighbors, Protected)
          - Germany: Friends (Influence: 74, Distance: Far)
          - Greece: Ally (Influence: 721, Distance: Distant)
          - The Zulus: Friends (Influence: 96, Distance: Neighbors, Protected)
          - Russia: Neutral (Influence: -4, Distance: Close)
          - Venice: Friends (Influence: 230, Distance: Distant)
          - India: War (Influence: -60, Distance: Far)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 34
        - Civilization: Kathmandu
        - Leader: City State
        - MajorAlly: The Inca
        - Population: 20
        - ResourcesAvailable:
          - Bananas: 1
        - MajorityReligion: Protestantism
        - Relationships:
          - The Inca: Ally (Influence: 97, Distance: Neighbors, Protected)
          - Germany: War (Influence: -60, Distance: Distant)
          - Greece: Friends (Influence: 216, Distance: Distant)
          - The Zulus: Friends (Influence: 174, Distance: Close, Protected)
          - Russia: War (Influence: -60, Distance: Neighbors)
          - Venice: Friends (Influence: 34, Distance: Distant)
          - India: War (Influence: -60, Distance: Far)
        - Quests:
          -  There are currently no quests this city-state has given to you. They will periodically give quests to you, but may refrain if you have bullied them recently.
        
        ## Player 35
        - Civilization: Lutetia
        - Leader: City State
        - MajorAlly: Greece
        - Population: 28
        - ResourcesAvailable:
          - Fish: 4
        - Relationships:
          - The Inca: Neutral (Influence: -37, Distance: Close)
          - Germany: Friends (Influence: 137, Distance: Distant, Protected)
          - Greece: Ally (Influence: 628, Distance: Distant, Protected)
          - The Zulus: Neutral (Influence: 27, Distance: Far, Protected)
          - Russia: Friends (Influence: 89, Distance: Close, Protected)
          - Venice: Friends (Influence: 55, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        - Quests:
          -  Construct 1 Airport building in non-puppet cities in your empire. (Turns remaining: 27) Potential Quest Reward: * 210 Influence * 380 Production in Capital
          - Conduct a Spy Mission against Enrico Dandolo. Potential Quest Reward: * 313 Influence * 754 Science
        
        ## Player 36
        - Civilization: Antananarivo
        - Leader: City State
        - MajorAlly: Germany
        - Population: 16
        - MajorityReligion: Hinduism
        - Relationships:
          - The Inca: War (Influence: -60, Distance: Close)
          - Germany: Ally (Influence: 908, Distance: Neighbors, Protected)
          - Greece: Friends (Influence: 128, Distance: Far)
          - The Zulus: Friends (Influence: 239, Distance: Close, Protected)
          - Russia: Friends (Influence: 368, Distance: Neighbors, Protected)
          - Venice: War (Influence: -60, Distance: Far)
          - India: Friends (Influence: 648, Distance: Neighbors, Protected)
        - Quests:
          -  They will reward the player with the largest Culture growth. So far, the leader has 15,703 and you have 6,416. (Turns remaining: 25) Potential Quest Reward: * 298 Influence * 4 Happiness in Capital
        
        ## Player 37
        - Civilization: Vienna
        - Leader: City State
        - MajorAlly: Greece
        - Population: 10
        - ResourcesAvailable:
          - Sheep: 2
        - Relationships:
          - The Inca: Friends (Influence: 98, Distance: Close)
          - Germany: Friends (Influence: 485, Distance: Distant)
          - Greece: Ally (Influence: 332, Distance: Distant, Protected)
          - The Zulus: Friends (Influence: 90, Distance: Neighbors, Protected)
          - Russia: Friends (Influence: 228, Distance: Neighbors, Protected)
          - Venice: Friends (Influence: 79, Distance: Distant)
          - India: War (Influence: -60, Distance: Distant)
        - Quests:
          -  Send an archaeologist to a site near this city-state. Potential Quest Reward: * 173 Influence * 1,557 Tourism with all known Civilizations
          - They want you to generate a Great Merchant. (Turns remaining: 34) Potential Quest Reward: * 152 Influence * 595 Culture
        - 63: Barbarians
        
        # Cities
        Cities: summary reports about discovered cities in the world.
        
        ## Player: Russia
        
        ### Moscow
        - ID: 1079
        - X: 34
        - Y: 34
        - Population: 27
        - DefenseStrength: 91
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Kremlin
          - Printing Press
          - Menin Gate
          - Giorgio Armeier Headquarters
        
        ### St. Petersburg
        - ID: 1278
        - X: 38
        - Y: 35
        - Population: 23
        - MajorityReligion: Hinduism
        - DefenseStrength: 87
        - Wonders:
          - Chartered Company
          - Grand Temple
          - Red Fort
          - Scrivener's Office
        
        ### Washington
        - ID: 1718
        - X: 42
        - Y: 31
        - Population: 28
        - DefenseStrength: 51
        - IsOccupied: true
        
        ### Novgorod
        - ID: 2095
        - X: 35
        - Y: 29
        - Population: 32
        - MajorityReligion: Hinduism
        - DefenseStrength: 68
        - Wonders:
          - Royal Collection
          - Great Wall
          - Chichen Itza
          - Himeji Castle
          - Brandenburg Gate
          - Palace of Culture and Science
        
        ### Rostov
        - ID: 2548
        - X: 46
        - Y: 30
        - Population: 23
        - MajorityReligion: Hinduism
        - DefenseStrength: 67
        - IsCoastal: true
        
        ### Yaroslavl'
        - ID: 3073
        - X: 31
        - Y: 32
        - Population: 23
        - DefenseStrength: 72
        - Wonders:
          - Ironworks
          - Imperial College
          - Machu Picchu
          - National Intelligence Agency
        
        ### Yekaterinburg
        - ID: 5675
        - X: 31
        - Y: 50
        - Population: 21
        - DefenseStrength: 86
        
        ### New York
        - ID: 5895
        - X: 43
        - Y: 35
        - Population: 27
        - DefenseStrength: 70
        - IsOccupied: true
        - IsCoastal: true
        
        ### Yakutsk
        - ID: 6714
        - X: 18
        - Y: 33
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Vilcas
        - ID: 6866
        - X: 39
        - Y: 28
        - Population: 22
        - MajorityReligion: Hinduism
        - DefenseStrength: 67
        - IsOccupied: true
        - Wonders:
          - Foreign Bureau
        
        ### Vladivostok
        - ID: 7202
        - X: 18
        - Y: 27
        - Population: 25
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 80
        
        ### Smolensk
        - ID: 7355
        - X: 66
        - Y: 13
        - Population: 23
        - DefenseStrength: 63
        - IsCoastal: true
        
        ### Orenburg
        - ID: 10061
        - X: 12
        - Y: 34
        - Population: 19
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Andahuaylas
        - ID: 12522
        - X: 1
        - Y: 43
        - Population: 20
        - MajorityReligion: Protestantism
        - DefenseStrength: 39
        - IsOccupied: true
        - IsCoastal: true
        
        ### Stuttgart
        - ID: 13546
        - X: 68
        - Y: 8
        - Population: 16
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 63
        - IsOccupied: true
        - IsCoastal: true
        
        ### Dortmund
        - ID: 13867
        - X: 69
        - Y: 17
        - Population: 16
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 51
        - IsOccupied: true
        - IsCoastal: true
        
        ### Vatican City
        - ID: 16126
        - X: 29
        - Y: 28
        - Population: 14
        - DefenseStrength: 82
        - IsOccupied: true
        - IsCoastal: true
        
        ### Machu
        - ID: 16311
        - X: 43
        - Y: 25
        - Population: 18
        - MajorityReligion: Hinduism
        - DefenseStrength: 80
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Statue of Liberty
        
        ### Tiwanaku
        - ID: 16764
        - X: 40
        - Y: 24
        - Population: 20
        - DefenseStrength: 80
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Colossus
        
        ### Ollantaytambo
        - ID: 17644
        - X: 37
        - Y: 20
        - Population: 18
        - MajorityReligion: Hinduism
        - DefenseStrength: 80
        - IsOccupied: true
        - IsCoastal: true
        
        ### Vilcabamba
        - ID: 17840
        - X: 16
        - Y: 22
        - Population: 17
        - MajorityReligion: Hinduism
        - DefenseStrength: 82
        - IsPuppet: true
        - IsCoastal: true
        
        ### Cologne
        - ID: 18325
        - X: 48
        - Y: 27
        - Population: 15
        - DefenseStrength: 53
        - Health: 50%
        - IsPuppet: true
        - IsCoastal: true
        - ResistanceTurns: 7
        
        ## Player: Greece
        
        ### Sparta
        - ID: 1795
        - X: 53
        - Y: 8
        - Population: 35
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 74
        - IsCoastal: true
        - Wonders:
          - School of Philosophy
          - National Monument
          - Imperial College
          - Palace of Westminster
          - Broadway
          - Printing Press
          - Foreign Bureau
          - International Finance Center
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
        
        ### Corinth
        - ID: 2125
        - X: 56
        - Y: 12
        - Population: 25
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 73
        - Wonders:
          - Chartered Company
          - Ironworks
          - Royal Collection
          - University of Sankore
          - Grand Temple
          - TwoKay Foods Headquarters
        
        ### Argos
        - ID: 2554
        - X: 58
        - Y: 16
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 78
        - IsCoastal: true
        - Wonders:
          - Circus Maximus
        
        ### Knossos
        - ID: 3262
        - X: 57
        - Y: 6
        - Population: 22
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 49
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - Parthenon
        
        ### Mycenae
        - ID: 4157
        - X: 63
        - Y: 7
        - Population: 20
        - MajorityReligion: Eastern Orthodoxy
        - DefenseStrength: 71
        - IsCoastal: true
        
        ## Player: The Inca
        
        ### Cusco
        - ID: 1059
        - X: 34
        - Y: 24
        - Population: 23
        - MajorityReligion: Hinduism
        - DefenseStrength: 67
        - Health: 75%
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - National Monument
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Stonehenge
          - Terracotta Army
          - Globe Theatre
          - Summer Palace
          - Grand Canal
          - Holy Council
          - Firaxite Materials Headquarters
        
        ### Corihuayrachina
        - ID: 2475
        - X: 34
        - Y: 18
        - Population: 21
        - MajorityReligion: Hinduism
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Huamanga
        - ID: 2943
        - X: 34
        - Y: 14
        - Population: 21
        - MajorityReligion: Hinduism
        - DefenseStrength: 74
        - Health: 98%
        - IsCoastal: true
        - Wonders:
          - Grand Temple
        
        ### Vitcos
        - ID: 10420
        - X: 22
        - Y: 17
        - Population: 21
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Ica
        - ID: 12221
        - X: 5
        - Y: 37
        - Population: 16
        - DefenseStrength: 70
        - IsCoastal: true
        
        ## Player: India
        
        ### Delhi
        - ID: 1060
        - X: 40
        - Y: 9
        - Population: 37
        - MajorityReligion: Hinduism
        - DefenseStrength: 83
        - Wonders:
          - Circus Maximus
          - Ironworks
          - Royal Collection
          - Pyramids
          - Hanging Gardens
          - Porcelain Tower
          - Sistine Chapel
          - Temple of Artemis
          - Leaning Tower of Pisa
          - Neuschwanstein
          - Uffizi
          - Borobudur
          - Palace of Culture and Science
          - Karlstejn
          - Soho Foundry
          - Throne Room
          - State Treasury
          - Royal Guardhouse
          - Palace Gardens
          - Court Chapel
          - Royal Astrologer
          - Divine Court
          - Civilized Jewelers Headquarters
        
        ### Mumbai
        - ID: 1281
        - X: 44
        - Y: 5
        - Population: 28
        - MajorityReligion: Hinduism
        - DefenseStrength: 61
        - Wonders:
          - School of Philosophy
          - Taj Mahal
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Foreign Bureau
        
        ### Vijayanagara
        - ID: 2056
        - X: 37
        - Y: 13
        - Population: 28
        - MajorityReligion: Hinduism
        - DefenseStrength: 74
        - Wonders:
          - Heroic Epic
          - National Monument
          - Imperial College
          - Cristo Redentor
          - Eiffel Tower
          - Empire State Building
        
        ### Pataliputra
        - ID: 2173
        - X: 49
        - Y: 5
        - Population: 27
        - MajorityReligion: Hinduism
        - DefenseStrength: 70
        - IsCoastal: true
        
        ### Varanasi
        - ID: 2863
        - X: 37
        - Y: 7
        - Population: 29
        - MajorityReligion: Hinduism
        - DefenseStrength: 68
        - IsCoastal: true
        - Wonders:
          - Chartered Company
          - Louvre
        
        ### Athens
        - ID: 10212
        - X: 49
        - Y: 10
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 75
        - Health: 94%
        - IsOccupied: true
        - IsCoastal: true
        - Wonders:
          - Statue of Zeus
        
        ## Player: Venice
        
        ### Venice
        - ID: 1061
        - X: 40
        - Y: 43
        - Population: 30
        - MajorityReligion: Buddhism
        - DefenseStrength: 58
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Royal Collection
          - Great Lighthouse
          - Oracle
          - Angkor Wat
          - Grand Temple
          - Scrivener's Office
          - Printing Press
          - Piazza San Marco
          - Rialto District
          - Roman Forum
          - Court Chapel
          - Royal Astrologer
          - Apostolic Palace
        
        ### Cattaro
        - ID: 1453
        - X: 41
        - Y: 47
        - Population: 29
        - MajorityReligion: Buddhism
        - DefenseStrength: 66
        - IsPuppet: true
        - IsCoastal: true
        
        ### Corfu
        - ID: 2648
        - X: 42
        - Y: 39
        - Population: 26
        - DefenseStrength: 70
        - Health: 18%
        - IsPuppet: true
        - IsCoastal: true
        
        ### Singapore
        - ID: 7143
        - X: 36
        - Y: 49
        - Population: 22
        - MajorityReligion: Buddhism
        - DefenseStrength: 63
        - Health: 15%
        - IsPuppet: true
        
        ## Player: Germany
        
        ### Berlin
        - ID: 1062
        - X: 48
        - Y: 20
        - Population: 29
        - MajorityReligion: Hinduism
        - DefenseStrength: 74
        - IsCoastal: true
        - FoodStored: 1851
        - FoodPerTurn: 8
        - ProductionStored: 0
        - ProductionPerTurn: 232
        - CurrentProduction: Fleet Destroyer
        - ProductionTurnsLeft: 5
        - GoldPerTurn: 334
        - SciencePerTurn: 292
        - CulturePerTurn: 211
        - FaithPerTurn: 61
        - TourismPerTurn: 131.5
        - HappinessDelta: 11
        - BuildingCount: 48
        - ImportantBuildings:
          - Seaport
          - Water Mill
          - Observatory
          - Garden
          - Zoo
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Arsenal
          - Hospital
          - Workshop
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Hanse
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Chancery
          - Brewhouse
        - Wonders:
          - School of Philosophy
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Great Library
          - Notre Dame
          - Mausoleum of Halicarnassus
          - Scrivener's Office
          - Printing Press
        - GreatWorkCount: 12
        
        ### Hamburg
        - ID: 1989
        - X: 46
        - Y: 14
        - Population: 23
        - MajorityReligion: Hinduism
        - DefenseStrength: 62
        - FoodStored: 596
        - FoodPerTurn: 1
        - ProductionStored: 0
        - ProductionPerTurn: 222
        - CurrentProduction: Foreign Bureau
        - ProductionTurnsLeft: 6
        - GoldPerTurn: 233
        - SciencePerTurn: 160
        - CulturePerTurn: 208
        - FaithPerTurn: 37
        - TourismPerTurn: 195.5
        - HappinessDelta: 12
        - BuildingCount: 54
        - ImportantBuildings:
          - Stable
          - Water Mill
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Museum
          - Broadcast Tower
          - Military Academy
          - Arsenal
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Hanse
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Bath
          - Agribusiness
          - Coaling Station
          - Wire Service
          - Brewhouse
        - Wonders:
          - Forbidden Palace
          - Hall of Honor
          - Nalanda
        - GreatWorkCount: 10
        
        ### Munich
        - ID: 2177
        - X: 42
        - Y: 13
        - Population: 22
        - MajorityReligion: Hinduism
        - DefenseStrength: 61
        - FoodStored: 599
        - FoodPerTurn: 2
        - ProductionStored: 1328
        - ProductionPerTurn: 195
        - CurrentProduction: Broadcast Tower
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 118
        - SciencePerTurn: 165
        - CulturePerTurn: 186
        - FaithPerTurn: 35
        - TourismPerTurn: 103.25
        - HappinessDelta: 7
        - BuildingCount: 50
        - ImportantBuildings:
          - Water Mill
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Arsenal
          - Hospital
          - Factory
          - Stock Exchange
          - Research Lab
          - Constabulary
          - Hanse
          - Writers' Guild
          - Artists' Guild
          - Musicians' Guild
          - Hotel
          - Caravansary
          - Airport
          - Bath
          - Chancery
          - Agribusiness
          - Coaling Station
          - Brewhouse
        - Wonders:
          - Heroic Epic
          - National Monument
          - Royal Collection
          - Grand Temple
        - GreatWorkCount: 8
        
        ### Frankfurt
        - ID: 6078
        - X: 62
        - Y: 25
        - Population: 22
        - DefenseStrength: 73
        - IsCoastal: true
        - FoodStored: 757
        - FoodPerTurn: 1
        - ProductionStored: 0
        - ProductionPerTurn: 190
        - CurrentProduction: Stone Works
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 159
        - SciencePerTurn: 123
        - CulturePerTurn: 59
        - FaithPerTurn: 15
        - TourismPerTurn: 31
        - HappinessDelta: -4
        - BuildingCount: 48
        - ImportantBuildings:
          - Seaport
          - Stable
          - Observatory
          - Garden
          - Stadium
          - Temple
          - Opera House
          - Museum
          - Military Academy
          - Arsenal
          - Hospital
          - Workshop
          - Bank
          - Public School
          - Constabulary
          - Hanse
          - Caravansary
          - Chancery
          - Agribusiness
          - Brewhouse
        - GreatWorkCount: 2
        
        ### Dusseldorf
        - ID: 10658
        - X: 61
        - Y: 45
        - Population: 16
        - MajorityReligion: Buddhism
        - DefenseStrength: 74
        - IsCoastal: true
        - FoodStored: 337
        - FoodPerTurn: 10
        - ProductionStored: 295
        - ProductionPerTurn: 98
        - CurrentProduction: Zoo
        - ProductionTurnsLeft: 1
        - GoldPerTurn: 72
        - SciencePerTurn: 97
        - CulturePerTurn: 47
        - FaithPerTurn: 12
        - TourismPerTurn: 9
        - BuildingCount: 38
        - ImportantBuildings:
          - Water Mill
          - Circus
          - Harbor
          - Temple
          - Armory
          - Arsenal
          - Hospital
          - Workshop
          - Bank
          - University
          - Amphitheater
          - Constabulary
          - Hanse
          - Writers' Guild
          - Caravansary
          - Bath
          - Chancery
          - Brewhouse
        - GreatWorkCount: 0
        
        ### Aachen
        - ID: 16810
        - X: 65
        - Y: 29
        - Population: 17
        - DefenseStrength: 71
        - IsCoastal: true
        - FoodStored: 346
        - FoodPerTurn: 6
        - ProductionStored: 1184
        - ProductionPerTurn: 150
        - CurrentProduction: Stadium
        - ProductionTurnsLeft: 3
        - GoldPerTurn: 79
        - SciencePerTurn: 100
        - CulturePerTurn: 34
        - FaithPerTurn: 12
        - TourismPerTurn: 10.25
        - HappinessDelta: -3
        - BuildingCount: 37
        - ImportantBuildings:
          - Stable
          - Harbor
          - Zoo
          - Temple
          - Armory
          - Arsenal
          - Hospital
          - Workshop
          - Bank
          - Public School
          - Amphitheater
          - Constabulary
          - Hanse
          - Chancery
          - Brewhouse
        - GreatWorkCount: 0
        
        ## Player: The Zulus
        
        ### Ulundi
        - ID: 1082
        - X: 30
        - Y: 46
        - Population: 34
        - MajorityReligion: Protestantism
        - DefenseStrength: 83
        - Wonders:
          - Circus Maximus
          - Chartered Company
          - Ironworks
          - Imperial College
          - Royal Collection
          - Scrivener's Office
          - Printing Press
          - Hall of Honor
          - Great Altar
          - Trader Sid's Headquarters
        
        ### Umgungundlovu
        - ID: 1455
        - X: 28
        - Y: 41
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 77
        - IsCoastal: true
        - Wonders:
          - Heroic Epic
          - School of Philosophy
          - Prora
        
        ### Nobamba
        - ID: 1847
        - X: 34
        - Y: 45
        - Population: 26
        - MajorityReligion: Protestantism
        - DefenseStrength: 69
        - Wonders:
          - National Monument
          - Hagia Sophia
          - Petra
          - Grand Temple
        
        ### Bulawayo
        - ID: 2018
        - X: 37
        - Y: 40
        - Population: 25
        - MajorityReligion: Protestantism
        - DefenseStrength: 74
        
        ### Kwadukuza
        - ID: 4250
        - X: 26
        - Y: 47
        - Population: 27
        - DefenseStrength: 73
        - IsCoastal: true
        
        ### Nongoma
        - ID: 8308
        - X: 19
        - Y: 47
        - Population: 24
        - MajorityReligion: Protestantism
        - DefenseStrength: 69
        - IsCoastal: true
        
        ### Ondini
        - ID: 9111
        - X: 9
        - Y: 43
        - Population: 22
        - MajorityReligion: Protestantism
        - DefenseStrength: 66
        - IsCoastal: true
        
        ### Nodwengu
        - ID: 9570
        - X: 5
        - Y: 47
        - Population: 20
        - MajorityReligion: Protestantism
        - DefenseStrength: 71
        - IsCoastal: true
        
        ### Agra
        - ID: 17712
        - X: 28
        - Y: 13
        - Population: 14
        - MajorityReligion: Hinduism
        - DefenseStrength: 5
        - IsOccupied: true
        - IsCoastal: true
        
        ## Player: City-States
        
        ### Melbourne
        - ID: 1063
        - X: 65
        - Y: 42
        - Population: 29
        - MajorityReligion: Buddhism
        - DefenseStrength: 98
        - IsCoastal: true
        
        ### Trowulan
        - ID: 1064
        - X: 53
        - Y: 28
        - Population: 21
        - DefenseStrength: 94
        - IsCoastal: true
        
        ### Arequipa
        - ID: 14185
        - X: 54
        - Y: 23
        - Population: 12
        - DefenseStrength: 60
        - IsOccupied: true
        - IsCoastal: true
        
        ### Quebec City
        - ID: 1066
        - X: 53
        - Y: 17
        - Population: 25
        - MajorityReligion: Hinduism
        - DefenseStrength: 96
        - IsCoastal: true
        
        ### Antwerp
        - ID: 1067
        - X: 28
        - Y: 35
        - Population: 18
        - DefenseStrength: 94
        - IsCoastal: true
        
        ### Shanghai
        - ID: 1068
        - X: 14
        - Y: 28
        - Population: 18
        - DefenseStrength: 74
        - IsCoastal: true
        
        ### Oviedo
        - ID: 12704
        - X: 33
        - Y: 40
        - Population: 12
        - DefenseStrength: 98
        
        ### M'banza-Kongo
        - ID: 1071
        - X: 77
        - Y: 46
        - Population: 21
        - MajorityReligion: Protestantism
        - DefenseStrength: 96
        - IsCoastal: true
        
        ### Zuunmod
        - ID: 1072
        - X: 65
        - Y: 20
        - Population: 23
        - DefenseStrength: 82
        - IsCoastal: true
        
        ### Tyre
        - ID: 1073
        - X: 31
        - Y: 4
        - Population: 17
        - MajorityReligion: Hinduism
        - DefenseStrength: 87
        - IsCoastal: true
        
        ### Segou
        - ID: 1074
        - X: 22
        - Y: 12
        - Population: 27
        - DefenseStrength: 93
        - IsCoastal: true
        
        ### Kathmandu
        - ID: 1075
        - X: 20
        - Y: 23
        - Population: 20
        - MajorityReligion: Protestantism
        - DefenseStrength: 91
        
        ### Lutetia
        - ID: 1076
        - X: 7
        - Y: 22
        - Population: 28
        - DefenseStrength: 95
        - IsCoastal: true
        
        ### Antananarivo
        - ID: 17481
        - X: 41
        - Y: 17
        - Population: 16
        - MajorityReligion: Hinduism
        - DefenseStrength: 69
        - IsCoastal: true
        
        ### Vienna
        - ID: 1078
        - X: 15
        - Y: 40
        - Population: 10
        - DefenseStrength: 96
        
        # Military
        Military: summary reports about tactical zones and visible units.
        
        ## Unit Stats
        - CityBombard:
          - Artillery:
            - Strength: 27
            - RangedStrength: 50
          - Krupp Gun:
            - Strength: 27
            - RangedStrength: 55
        - FastAttack:
          - Landship:
            - Strength: 60
        - Defense:
          - Rifleman:
            - Strength: 50
        - Counter:
          - Anti-Aircraft Gun:
            - Strength: 40
        - Ranged:
          - Light Tank:
            - Strength: 58
            - RangedStrength: 52
          - Cavalry:
            - Strength: 40
            - RangedStrength: 31
          - Machine Gun:
            - Strength: 45
            - RangedStrength: 58
        - AttackSea:
          - Destroyer:
            - Strength: 70
          - Fleet Destroyer:
            - Strength: 80
        - AssaultSea:
          - Battleship:
            - Strength: 60
            - RangedStrength: 75
          - Dreadnought:
            - Strength: 50
            - RangedStrength: 65
        - AttackAir:
          - Bomber:
            - RangedStrength: 50
        - DefenseAir:
          - Triplane:
            - RangedStrength: 45
        - Paradrop:
          - Paratrooper:
            - Strength: 42
        
        ## Neutral Land Zone 1060
        - ZoneValue: 132
        - Dominance: Friendly
        - NeutralStrength: 584
        - FriendlyStrength: 493
        - City: Delhi
        - AreaID: 2
        - Plots: 18
        - CenterX: 41
        - CenterY: 9
        - Units:
          - India:
            - Artillery: 1
        - Neighbors:
          - 2177
        
        ## Friendly Land Zone 1062
        - ZoneValue: 48
        - Dominance: Friendly
        - NeutralStrength: 416
        - FriendlyStrength: 2280
        - City: Berlin
        - AreaID: 2
        - Plots: 21
        - CenterX: 48
        - CenterY: 19
        - Units:
          - Germany:
            - Paratrooper: 1
            - Anti-Aircraft Gun: 1
            - Rifleman: 2
            - Bomber: 2
            - Krupp Gun: 1
        - Neighbors:
          - 17481
          - -1062
          - 1989
          - 1066
          - -1066
        
        ## Neutral Land Zone 1063
        - ZoneValue: 30
        - Dominance: Friendly
        - NeutralStrength: 1226
        - FriendlyStrength: 647
        - City: Melbourne
        - AreaID: 80
        - Plots: 12
        - CenterX: 64
        - CenterY: 43
        - Units:
          - City-State Melbourne:
            - Anti-Aircraft Gun: 1
            - Cavalry: 1
            - Rifleman: 3
            - Landship: 2
            - Machine Gun: 2
          - Germany:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - -1063
          - -10658
          - 10658
        
        ## Neutral Land Zone 1064
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 694
        - FriendlyStrength: 289
        - City: Trowulan
        - AreaID: 50
        - Plots: 5
        - CenterX: 53
        - CenterY: 28
        - Units:
          - City-State Trowulan:
            - Rifleman: 2
            - Landship: 1
            - Machine Gun: 1
        - Neighbors:
          - -18325
          - -1064
        
        ## Neutral Land Zone 1066
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 1629
        - FriendlyStrength: 828
        - City: Quebec City
        - AreaID: 6
        - Plots: 18
        - CenterX: 52
        - CenterY: 16
        - Units:
          - City-State Quebec City:
            - Light Tank: 1
            - Rifleman: 2
          - Germany:
            - Rifleman: 1
            - Landship: 1
        - Neighbors:
          - 1989
          - 1062
          - 10212
          - -1066
          - -1795
        
        ## Neutral Land Zone 1067
        - ZoneValue: 12
        - Dominance: Friendly
        - NeutralStrength: 1892
        - FriendlyStrength: 796
        - City: Antwerp
        - AreaID: 2
        - Plots: 21
        - CenterX: 29
        - CenterY: 35
        - Units:
          - City-State Antwerp:
            - Landship: 1
            - Machine Gun: 1
        - Neighbors:
          - 12704
          - 1079
        
        ## Neutral Land Zone 1072
        - ZoneValue: 30
        - Dominance: Friendly
        - NeutralStrength: 902
        - FriendlyStrength: 800
        - City: Zuunmod
        - AreaID: 33
        - Plots: 15
        - CenterX: 66
        - CenterY: 21
        - Units:
          - City-State Zuunmod:
            - Artillery: 1
            - Rifleman: 1
            - Machine Gun: 1
        - Neighbors:
          - -1072
          - -6078
        
        ## Neutral Land Zone 1079
        - ZoneValue: 48
        - Dominance: Friendly
        - NeutralStrength: 1007
        - FriendlyStrength: 1629
        - City: Moscow
        - AreaID: 2
        - Plots: 17
        - CenterX: 34
        - CenterY: 34
        - Units:
          - Russia:
            - Bomber: 2
            - Machine Gun: 1
        - Neighbors:
          - 1067
          - 12704
          - 2095
        
        ## Neutral Land Zone 1082
        - ZoneValue: 48
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 21
        - NeutralStrength: 2331
        - FriendlyStrength: 981
        - City: Ulundi
        - AreaID: 2
        - Plots: 16
        - CenterX: 30
        - CenterY: 45
        - Units:
          - The Zulus:
            - Artillery: 1
            - Anti-Aircraft Gun: 1
            - Machine Gun: 2
        - Neighbors:
          - 4250
          - 5675
          - 12704
        
        ## Friendly Land Zone 1989
        - ZoneValue: 42
        - Dominance: Friendly
        - NeutralStrength: 571
        - FriendlyStrength: 2025
        - City: Hamburg
        - AreaID: 2
        - Plots: 29
        - CenterX: 46
        - CenterY: 14
        - Units:
          - Germany:
            - Paratrooper: 1
            - Anti-Aircraft Gun: 2
            - Krupp Gun: 1
        - Neighbors:
          - 2177
          - 17481
          - 10212
          - 1062
          - 1066
        
        ## Neutral Land Zone 2095
        - ZoneValue: 24
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 374
        - NeutralStrength: 68
        - FriendlyStrength: 2917
        - City: Novgorod
        - AreaID: 2
        - Plots: 20
        - CenterX: 35
        - CenterY: 29
        - Units:
          - Russia:
            - Artillery: 1
        - Neighbors:
          - 1079
        
        ## Friendly Land Zone 2177
        - ZoneValue: 36
        - Dominance: Friendly
        - NeutralStrength: 518
        - FriendlyStrength: 1156
        - City: Munich
        - AreaID: 2
        - Plots: 23
        - CenterX: 42
        - CenterY: 12
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
            - Rifleman: 3
        - Neighbors:
          - 1060
          - 17481
          - 1989
          - 10212
        
        ## Neutral Land Zone 4250
        - ZoneValue: 15
        - Dominance: Friendly
        - NeutralStrength: 1872
        - FriendlyStrength: 884
        - City: Kwadukuza
        - AreaID: 2
        - Plots: 15
        - CenterX: 27
        - CenterY: 47
        - Units:
          - The Zulus:
            - Rifleman: 1
        - Neighbors:
          - 1082
          - 5675
        
        ## Neutral Land Zone 5675
        - ZoneValue: 15
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 53
        - NeutralStrength: 1172
        - FriendlyStrength: 1368
        - City: Yekaterinburg
        - AreaID: 2
        - Plots: 17
        - CenterX: 31
        - CenterY: 49
        - Units:
          - The Zulus:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - 4250
          - 1082
        
        ## Friendly Land Zone 6078
        - ZoneValue: 30
        - Dominance: Friendly
        - NeutralStrength: 447
        - FriendlyStrength: 1061
        - City: Frankfurt
        - AreaID: 47
        - Plots: 11
        - CenterX: 62
        - CenterY: 25
        - Units:
          - Germany:
            - Triplane: 2
            - Krupp Gun: 1
        - Neighbors:
          - -100000
          - -6078
          - -1072
        
        ## Neutral Land Zone 10212
        - ZoneValue: 60
        - Dominance: Friendly
        - NeutralStrength: 1461
        - FriendlyStrength: 755
        - City: Athens
        - AreaID: 2
        - Plots: 27
        - CenterX: 48
        - CenterY: 10
        - Units:
          - Germany:
            - Rifleman: 2
          - India:
            - Rifleman: 1
            - Triplane: 2
            - Machine Gun: 3
        - Neighbors:
          - 2177
          - 1989
          - -1795
          - -1066
          - 1066
        
        ## Friendly Land Zone 10658
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 887
        - FriendlyStrength: 1102
        - City: Dusseldorf
        - AreaID: 80
        - Plots: 23
        - CenterX: 62
        - CenterY: 47
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
            - Triplane: 1
            - Bomber: 1
            - Landship: 1
            - Krupp Gun: 1
        - Neighbors:
          - -10658
          - -100000
          - 1063
          - -1063
        
        ## Neutral Land Zone 12704
        - ZoneValue: 9
        - Dominance: Friendly
        - NeutralStrength: 2248
        - FriendlyStrength: 419
        - City: Oviedo
        - AreaID: 2
        - Plots: 27
        - CenterX: 33
        - CenterY: 40
        - Units:
          - City-State Oviedo:
            - Machine Gun: 2
        - Neighbors:
          - 1067
          - 1082
          - 1079
        
        ## Neutral Land Zone 16311
        - ZoneValue: 18
        - Dominance: Friendly
        - NeutralStrength: 81
        - FriendlyStrength: 2144
        - City: Machu
        - AreaID: 2
        - Plots: 14
        - CenterX: 43
        - CenterY: 26
        - Units:
          - Russia:
            - Triplane: 1
            - Bomber: 1
            - Machine Gun: 1
        
        ## Friendly Land Zone 16810
        - ZoneValue: 3
        - Dominance: Friendly
        - FriendlyStrength: 1214
        - City: Aachen
        - AreaID: 52
        - Plots: 8
        - CenterX: 66
        - CenterY: 29
        - Units:
          - Germany:
            - Paratrooper: 2
            - Rifleman: 3
            - Krupp Gun: 1
        - Neighbors:
          - -6078
        
        ## Neutral Land Zone 17481
        - ZoneValue: 24
        - Dominance: Friendly
        - NeutralStrength: 390
        - FriendlyStrength: 2037
        - City: Antananarivo
        - AreaID: 2
        - Plots: 14
        - CenterX: 41
        - CenterY: 16
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
          - India:
            - Machine Gun: 1
        - Neighbors:
          - 17644
          - 2177
          - 1989
          - 1062
        
        ## Neutral Land Zone 17644
        - ZoneValue: 18
        - Dominance: Friendly
        - Posture: Attrition
        - EnemyStrength: 617
        - NeutralStrength: 482
        - FriendlyStrength: 2080
        - City: Ollantaytambo
        - AreaID: 2
        - Plots: 19
        - CenterX: 37
        - CenterY: 20
        - Units:
          - Russia:
            - Machine Gun: 1
        - Neighbors:
          - 17481
        
        ## Neutral Land Zone 18325
        - ZoneValue: 3
        - Dominance: Friendly
        - NeutralStrength: 448
        - FriendlyStrength: 1438
        - City: Cologne
        - AreaID: 53
        - Plots: 4
        - CenterX: 48
        - CenterY: 27
        - Units:
          - Germany:
            - Rifleman: 1
          - Russia:
            - Fleet Destroyer: 1
        - Neighbors:
          - -18325
          - -1064
        
        ## Friendly Sea Zone -10658
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 1025
        - FriendlyStrength: 601
        - City: Dusseldorf
        - AreaID: 0
        - Plots: 45
        - CenterX: 60
        - CenterY: 45
        - Units:
          - City-State Melbourne:
            - Fleet Destroyer: 1
          - Germany:
            - Rifleman: 1
        - Neighbors:
          - -100000
          - 10658
          - -1063
          - 1063
        
        ## Friendly Sea Zone -1062
        - ZoneValue: 1
        - Dominance: Friendly
        - NeutralStrength: 212
        - FriendlyStrength: 2816
        - City: Berlin
        - AreaID: 29
        - Plots: 16
        - CenterX: 47
        - CenterY: 21
        - Units:
          - City-State Antananarivo:
            - Fleet Destroyer: 1
          - Germany:
            - Destroyer: 5
            - Anti-Aircraft Gun: 1
            - Fleet Destroyer: 1
        - Neighbors:
          - 1062
          - -18325
          - -1066
        
        ## Neutral Sea Zone -1066
        - ZoneValue: 5
        - Dominance: Friendly
        - NeutralStrength: 2027
        - FriendlyStrength: 953
        - City: Quebec City
        - AreaID: 0
        - Plots: 21
        - CenterX: 53
        - CenterY: 18
        - Units:
          - City-State Quebec City:
            - Battleship: 1
            - Machine Gun: 1
        - Neighbors:
          - 10212
          - 1062
          - -1062
          - 1066
        
        ## Neutral Sea Zone -1795
        - ZoneValue: 9
        - NeutralStrength: 1812
        - City: Sparta
        - AreaID: 0
        - Plots: 7
        - CenterX: 51
        - CenterY: 9
        - Units:
          - City-State Quebec City:
            - Fleet Destroyer: 1
        - Neighbors:
          - 10212
          - 1066
        
        ## Neutral Sea Zone -1063
        - ZoneValue: 10
        - Dominance: Friendly
        - NeutralStrength: 1396
        - FriendlyStrength: 239
        - City: Melbourne
        - AreaID: 0
        - Plots: 60
        - CenterX: 66
        - CenterY: 41
        - Units:
          - City-State Melbourne:
            - Battleship: 1
            - Fleet Destroyer: 2
          - Germany:
            - Battleship: 1
        - Neighbors:
          - -100000
          - -10658
          - 1063
          - 10658
        
        ## Friendly Sea Zone -6078
        - ZoneValue: 10
        - Dominance: Friendly
        - NeutralStrength: 1017
        - FriendlyStrength: 663
        - City: Frankfurt
        - AreaID: 0
        - Plots: 37
        - CenterX: 61
        - CenterY: 25
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
          - Russia:
            - Fleet Destroyer: 1
        - Neighbors:
          - -1064
          - 6078
          - -100000
          - -1072
          - 16810
          - 1072
        
        ## Neutral Sea Zone -18325
        - ZoneValue: 80
        - Dominance: Friendly
        - NeutralStrength: 146
        - FriendlyStrength: 3020
        - City: Cologne
        - AreaID: 29
        - Plots: 24
        - CenterX: 48
        - CenterY: 26
        - Units:
          - Germany:
            - Destroyer: 2
        - Neighbors:
          - 18325
          - -1062
          - -1064
          - 1064
        
        ## Neutral Sea Zone -100000
        - ZoneValue: 1
        - Dominance: Even
        - Posture: Exploit Flanks
        - EnemyStrength: 168
        - NeutralStrength: 75
        - FriendlyStrength: 255
        - AreaID: 0
        - Plots: 1052
        - CenterX: 75
        - CenterY: 23
        - Units:
          - Germany:
            - Anti-Aircraft Gun: 1
        - Neighbors:
          - -1076
          - -1064
          - -10658
          - 6078
          - 10658
          - -6078
          - -1063
          - -1072
        
        ## Neutral Sea Zone -1072
        - ZoneValue: 10
        - Dominance: Friendly
        - NeutralStrength: 1222
        - FriendlyStrength: 833
        - City: Zuunmod
        - AreaID: 19
        - Plots: 35
        - CenterX: 64
        - CenterY: 20
        - Units:
          - City-State Zuunmod:
            - Battleship: 2
            - Fleet Destroyer: 2
        - Neighbors:
          - -6078
          - 1072
          - 6078
          - -100000
        
        ## Neutral Sea Zone -1076
        - ZoneValue: 5
        - NeutralStrength: 1360
        - City: Lutetia
        - AreaID: 0
        - Plots: 83
        - CenterX: 6
        - CenterY: 22
        - Units:
          - City-State Lutetia:
            - Fleet Destroyer: 6
        - Neighbors:
          - -100000
        
        ## Neutral Sea Zone -1064
        - ZoneValue: 8
        - Dominance: Friendly
        - NeutralStrength: 515
        - FriendlyStrength: 2032
        - City: Trowulan
        - AreaID: 29
        - Plots: 51
        - CenterX: 53
        - CenterY: 30
        - Units:
          - Russia:
            - Fleet Destroyer: 1
          - City-State Trowulan:
            - Dreadnought: 1
          - Germany:
            - Destroyer: 2
        - Neighbors:
          - -18325
          - 18325
          - 1064
          - -100000
          - -6078
        
        # Events
        Events: events since you last made a decision.
        
        ## Turn 423
        
        ### 0
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18255
        - Player: 7: The Zulus
        - Plots:
          - Tundra Land 31,46:
            - Owner: The Zulus
            - Improvement: Village
            - Route: Railroad
          - Tundra Hills 31,47:
            - Owner: The Zulus
            - Improvement: Academy
            - Route: Railroad
        
        ### 1
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16681
        - Player: 7: The Zulus
        - Tundra Hills 31,47:
          - Owner: The Zulus
          - Improvement: Academy
          - Route: Railroad
        
        ### 2
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17328
        - Player: 7: The Zulus
        - Plots:
          - Tundra Land 31,46:
            - Owner: The Zulus
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 30,46:
            - Owner: The Zulus
            - CityID: 1082
            - Population: 34
            - IsRiver: true
            - City: Ulundi
            - Religion: Protestantism
            - Route: Railroad
          - Tundra Land 29,45:
            - Owner: The Zulus
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 29,44:
            - Owner: The Zulus
            - Improvement: Village
            - Route: Railroad
        
        ### 3
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17822
        - Player: 7: The Zulus
        - Plots:
          - Tundra Hills 31,47:
            - Owner: The Zulus
            - Improvement: Academy
            - Route: Railroad
          - Tundra Land 30,47:
            - Owner: The Zulus
            - Resource: Salt
            - Improvement: Mine
            - Route: Railroad
        
        ### 4
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: CityBombard
          - Unit: Artillery
          - ID: 14790
        - Player: 7: The Zulus
        - Plots:
          - Tundra Land 30,46:
            - Owner: The Zulus
            - CityID: 1082
            - Population: 34
            - IsRiver: true
            - City: Ulundi
            - Religion: Protestantism
            - Route: Railroad
          - Tundra Land 29,45:
            - Owner: The Zulus
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 29,44:
            - Owner: The Zulus
            - Improvement: Village
            - Route: Railroad
        
        ### 5
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Rifleman
          - ID: 12778
        - Player: 7: The Zulus
        - Plots:
          - Plains Hills 34,40:
            - Owner: City-State Oviedo
            - Improvement: Mine
            - Route: Railroad
          - Plains Hills 33,41:
            - Owner: City-State Oviedo
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 32,41:
            - Owner: City-State Oviedo
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
        
        ### 6
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15046
        - Player: 7: The Zulus
        - Plots:
          - Tundra Land 31,44:
            - Owner: The Zulus
            - Improvement: Manufactory
          - Tundra Hills 30,44:
            - Owner: The Zulus
            - Improvement: Mine
        
        ### 7
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Rifleman
          - ID: 12900
        - Player: 7: The Zulus
        - Plots:
          - Tundra Land 28,47:
            - Owner: The Zulus
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Tundra Land 29,47:
            - Owner: The Zulus
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 30,46:
            - Owner: The Zulus
            - CityID: 1082
            - Population: 34
            - IsRiver: true
            - City: Ulundi
            - Religion: Protestantism
            - Route: Railroad
          - Tundra Land 29,45:
            - Owner: The Zulus
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 29,44:
            - Owner: The Zulus
            - Improvement: Village
            - Route: Railroad
        
        ### 8
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Rifleman
          - ID: 13453
        - Player: 7: The Zulus
        - Plots:
          - Tundra Land 29,48:
            - Owner: The Zulus
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Land 29,47:
            - Owner: The Zulus
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 30,47:
            - Owner: The Zulus
            - Resource: Salt
            - Improvement: Mine
            - Route: Railroad
          - Tundra Hills 31,47:
            - Owner: The Zulus
            - Improvement: Academy
            - Route: Railroad
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16296
        - Player: 7: The Zulus
        - Plots:
          - Tundra Hills 31,45:
            - Owner: The Zulus
            - Improvement: Mine
            - Route: Railroad
          - Tundra Land 31,46:
            - Owner: The Zulus
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 30,46:
            - Owner: The Zulus
            - CityID: 1082
            - Population: 34
            - IsRiver: true
            - City: Ulundi
            - Religion: Protestantism
            - Route: Railroad
          - Tundra Land 29,47:
            - Owner: The Zulus
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 28,47:
            - Owner: The Zulus
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
        
        ### 10
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Rifleman
          - ID: 13025
        - Player: 7: The Zulus
        - Plots:
          - Tundra Hills 29,44:
            - Owner: The Zulus
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 29,45:
            - Owner: The Zulus
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Tundra Land 30,46:
            - Owner: The Zulus
            - CityID: 1082
            - Population: 34
            - IsRiver: true
            - City: Ulundi
            - Religion: Protestantism
            - Route: Railroad
          - Tundra Land 29,47:
            - Owner: The Zulus
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
          - Tundra Land 28,47:
            - Owner: The Zulus
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
        
        ### 11
        - Type: SetPopulation
        - OldPopulation: 28
        - NewPopulation: 29
        - City:
          - Owner: City-State Melbourne
          - CityID: 1063
          - Population: 29
          - City: Melbourne
          - Terrain: Tundra
          - Resource: Glass
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 65
          - Y: 42
        
        ### 12
        - Type: CityConvertsReligion
        - City:
          - Owner: City-State Melbourne
          - CityID: 1063
          - Population: 29
          - City: Melbourne
          - Terrain: Tundra
          - Resource: Glass
          - Religion: Buddhism
          - Route: Railroad
          - Plot: Land
          - X: 65
          - Y: 42
        - Owner: 22
        - Religion: Buddhism
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 12396
        - Player: 22
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 2
          - AI: Defense
          - Unit: Rifleman
          - ID: 12397
        - Player: 22
        - Plots:
          - Tundra Land 65,42:
            - Owner: City-State Melbourne
            - CityID: 1063
            - Population: 29
            - City: Melbourne
            - Resource: Glass
            - Religion: Buddhism
            - Route: Railroad
          - Tundra Land 64,43:
            - Owner: City-State Melbourne
            - Resource: Oil
            - Improvement: Oil Well
            - Route: Railroad
          - Tundra Land 64,44:
            - Owner: City-State Melbourne
            - Improvement: Village
        
        ### 15
        - Type: CityConstructed
        - City:
          - Name: Arequipa
          - Population: 12
          - ID: 14185
        - Owner: 23
        - Building: Gallery
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 86%
          - AI: AssaultSea
          - Unit: Dreadnought
          - ID: 14602
        - Player: 23
        
        ### 17
        - Type: CombatResult
        - Plains Land 49,10:
          - Owner: India
          - CityID: 10212
          - Population: 25
          - IsRiver: true
          - City: Athens
          - Religion: Hinduism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 19
          - Damage: 19
          - Player: 4: India
        
        ### 18
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 91%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18057
        - Player: 25
        - Plots:
          - Coast 51,13:
            - Owner: India
          - Coast 52,12:
            - Owner: India
            - Resource: Fish
          - Coast 51,11:
            - Owner: India
        
        ### 19
        - Type: CombatResult
        - Plains Land 49,10:
          - Owner: India
          - CityID: 10212
          - Population: 25
          - IsRiver: true
          - City: Athens
          - Religion: Hinduism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 21
          - Damage: 21
        - Defender:
          - RemainingHP: 29
          - Damage: 48
          - Player: 4: India
        
        ### 20
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Light Tank
          - ID: 14275
        - Player: 25
        - Plots:
          - Grass Land 51,16:
            - Owner: City-State Quebec City
            - Improvement: Embassy
            - Route: Railroad
          - Grass Land 50,15:
            - Owner: City-State Quebec City
            - Resource: Cattle
          - Grass Land 51,14:
            - Owner: India
            - Improvement: Fort
            - Route: Railroad
          - Plains Land 50,13:
            - Owner: India
            - IsRiver: true
            - Resource: Wheat
            - Improvement: Farm
            - Route: Railroad
        
        ### 21
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 12403
        - Player: 25
        - Desert Hills 53,16:
          - Owner: City-State Quebec City
          - Resource: Gems
          - Improvement: Mine
          - Route: Railroad
        
        ### 22
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 53%
          - AI: Defense
          - Unit: Rifleman
          - ID: 12400
        - Player: 25
        - Coast 52,15:
          - Owner: City-State Quebec City
        
        ### 23
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 16610
        - Player: 25
        - Coast 52,15:
          - Owner: City-State Quebec City
        
        ### 24
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: ExploreSea
          - Unit: Fleet Destroyer
          - ID: 18318
        - Player: 27
        - Coast 13,28:
          - Owner: City-State Shanghai
        
        ### 25
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 17826
        - Player: 31
        
        ### 26
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Fleet Destroyer
          - ID: 18319
        - Player: 36
        - Coast 40,17:
          - Owner: City-State Antananarivo
          - Resource: Fish
        
        ### 27
        - Type: UnitCreated
        - UnitType: Fleet Destroyer
        - Unit:
          - Level: 1
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18319
        - Player: 36
        - Coast 40,17:
          - Owner: City-State Antananarivo
          - Resource: Fish
        
        ### 28
        - Type: CityTrained
        - City:
          - Name: Antananarivo
          - Population: 16
          - ID: 17481
        - Unit:
          - Level: 1
          - AI: ExploreSea
          - Unit: Fleet Destroyer
          - ID: 18319
        - Player: 36
        
        ### 29
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: ExploreSea
          - Unit: Fleet Destroyer
          - ID: 18319
        - Player: 36
        - Promotions:
          - Boarding Party I
          - Boarding Party II
        
        ### 30
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18319
        - Player: 36
        - Plots:
          - Coast 41,18:
            - Owner: City-State Antananarivo
            - Resource: Fish
          - Ocean 41,19:
            - Owner: City-State Antananarivo
          - Ocean 42,19:
            - Owner: City-State Antananarivo
          - Coast 43,19:
            - Owner: City-State Antananarivo
          - Coast 44,20:
            - Owner: City-State Antananarivo
            - Feature: Atoll
        
        ## Turn 424
        
        ### 0
        - Type: CityConvertsReligion
        - City:
          - Owner: Russia
          - CityID: 2548
          - Population: 23
          - City: Rostov
          - Terrain: Grass
          - Resource: Stone
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 46
          - Y: 30
        - Owner: 1: Russia
        - Religion: Hinduism
        
        ### 1
        - Type: CityConvertsReligion
        - City:
          - Owner: Russia
          - CityID: 2548
          - Population: 23
          - City: Rostov
          - Terrain: Grass
          - Resource: Stone
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 46
          - Y: 30
        - Owner: 1: Russia
        - Religion: Hinduism
        
        ### 2
        - Type: CityConvertsReligion
        - City:
          - Owner: Russia
          - CityID: 2548
          - Population: 23
          - City: Rostov
          - Terrain: Grass
          - Resource: Stone
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Hills
          - X: 46
          - Y: 30
        - Owner: 1: Russia
        - Religion: Hinduism
        
        ### 3
        - Type: CityConvertsReligion
        - City:
          - Owner: India
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 40
          - Y: 9
        - Owner: 4: India
        - Religion: Hinduism
        
        ### 4
        - Type: CityConvertsReligion
        - City:
          - Owner: India
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 40
          - Y: 9
        - Owner: 4: India
        - Religion: Hinduism
        
        ### 5
        - Type: CityConvertsReligion
        - City:
          - Owner: India
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 40
          - Y: 9
        - Owner: 4: India
        - Religion: Hinduism
        
        ### 6
        - Type: CityConvertsReligion
        - City:
          - Owner: India
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 40
          - Y: 9
        - Owner: 4: India
        - Religion: Hinduism
        
        ### 7
        - Type: CityConvertsReligion
        - City:
          - Owner: India
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 40
          - Y: 9
        - Owner: 4: India
        - Religion: Hinduism
        
        ### 8
        - Type: CityConvertsReligion
        - City:
          - Owner: India
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Delhi
          - Terrain: Plains
          - Religion: Hinduism
          - Route: Railroad
          - Plot: Land
          - X: 40
          - Y: 9
        - Owner: 4: India
        - Religion: Hinduism
        
        ### 9
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Great Engineer
          - ID: 18324
        - Player: 1: Russia
        - Grass Hills 46,30:
          - Owner: Russia
          - CityID: 2548
          - Population: 23
          - City: Rostov
          - Resource: Stone
          - Religion: Hinduism
          - Route: Railroad
        
        ### 10
        - Type: UnitCreated
        - UnitType: Great Engineer
        - Player: 1: Russia
        - Unit:
          - Level: 1
          - AI: Engineer
          - Unit: Great Engineer
          - ID: 18324
        - Grass Hills 46,30:
          - Owner: Russia
          - CityID: 2548
          - Population: 23
          - City: Rostov
          - Resource: Stone
          - Religion: Hinduism
          - Route: Railroad
        
        ### 11
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16625
        - Player: 1: Russia
        - Plots:
          - Plains Land 35,34:
            - Owner: Russia
            - Resource: Wheat
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 34,35:
            - Owner: Russia
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 33,35:
            - Owner: Russia
            - IsRiver: true
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 33,36:
            - Owner: Russia
            - Resource: Coal
            - Improvement: Manufactory
            - Route: Railroad
          - Grass Land 32,36:
            - Owner: Russia
            - Resource: Lapis Lazuli
            - Improvement: Quarry
            - Route: Railroad
        
        ### 12
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17646
        - Player: 1: Russia
        - Grass Land 15,28:
          - Owner: City-State Shanghai
          - Improvement: Farm
          - Route: Railroad
        
        ### 13
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17647
        - Player: 1: Russia
        - Plots:
          - Grass Hills 35,31:
            - Owner: Russia
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 35,32:
            - Owner: Russia
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 34,33:
            - Owner: Russia
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 35,34:
            - Owner: Russia
            - Resource: Wheat
            - Improvement: Town
            - Route: Railroad
          - Grass Hills 34,35:
            - Owner: Russia
            - IsRiver: true
            - Improvement: Manufactory
            - Route: Railroad
        
        ### 14
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18202
        - Player: 1: Russia
        - Plots:
          - Coast 52,29:
            - Owner: City-State Trowulan
          - Ocean 51,30:
            - Owner: Russia
          - Ocean 50,30:
            - Owner: Russia
        
        ### 15
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17922
        - Player: 1: Russia
        - Plots:
          - Coast 49,28:
            - Owner: The Inca
            - Resource: Fish
          - Coast 49,29:
            - Owner: The Inca
        
        ### 16
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 17257
        - Player: 1: Russia
        - Plots:
          - Coast 49,29:
            - Owner: The Inca
          - Coast 49,28:
            - Owner: The Inca
            - Resource: Fish
        
        ### 17
        - Type: CombatResult
        - Grass Land 48,27:
          - Owner: The Inca
          - CityID: 8438
          - Population: 19
          - City: Cologne
          - Resource: Tobacco
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 21
          - Damage: 766
          - Player: 3: The Inca
        
        ### 18
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 17257
        - Player: 1: Russia
        - Coast 49,29:
          - Owner: The Inca
        
        ### 19
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17922
        - Player: 1: Russia
        - Coast 49,28:
          - Owner: The Inca
          - Resource: Fish
        
        ### 20
        - Type: CombatResult
        - Grass Land 48,27:
          - Owner: The Inca
          - CityID: 8438
          - Population: 19
          - City: Cologne
          - Resource: Tobacco
          - Route: Railroad
        - Attacker:
          - RemainingHP: 6
          - Damage: 6
        - Defender:
          - RemainingHP: 36
          - Damage: 802
          - Player: 3: The Inca
        
        ### 21
        - Type: CityEventChoiceEnded
        - City:
          - Population: 19
          - Name: Cologne
          - Health: -99%
          - ID: 8438
        - Player: 3: The Inca
        - Choice: 90
        
        ### 22
        - Type: SetPopulation
        - OldPopulation: 19
        - NewPopulation: 0
        - City:
          - Owner: The Inca
          - CityID: 8438
          - Population: 0
          - City: Cologne
          - Terrain: Grass
          - Resource: Tobacco
          - Route: Railroad
          - Plot: Land
          - X: 48
          - Y: 27
        
        ### 23
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 24
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 25
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 26
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 27
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 28
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 29
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 30
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 31
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 32
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        - Coast 48,26:
          - Resource: Fish
        
        ### 33
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 34
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 35
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 36
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        - Grass Hills 46,27:
          - Resource: Coal
          - Improvement: Academy
        
        ### 37
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 38
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        - Grass Land 48,27:
          - Resource: Tobacco
          - Route: Railroad
        
        ### 39
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        - Grass Land 49,27:
          - Resource: Rice
          - Improvement: Farm
          - Route: Road
        
        ### 40
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 41
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        - Coast 49,28:
          - Resource: Fish
        
        ### 42
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 43
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 44
        - Type: TileOwnershipChanged
        - OldOwner: 3: The Inca
        
        ### 45
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Grass Land 48,27:
          - Owner: Russia
          - Resource: Tobacco
          - Route: Railroad
        
        ### 46
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 47,27:
          - Owner: Russia
        
        ### 47
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 48,28:
          - Owner: Russia
        
        ### 48
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 48,26:
          - Owner: Russia
          - Resource: Fish
        
        ### 49
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 49,28:
          - Owner: Russia
          - Resource: Fish
        
        ### 50
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 49,26:
          - Owner: Russia
        
        ### 51
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Grass Land 49,27:
          - Owner: Russia
          - Resource: Rice
          - Improvement: Farm
          - Route: Road
        
        ### 52
        - Type: SetPopulation
        - OldPopulation: 0
        - NewPopulation: 1
        - City:
          - Owner: Russia
          - CityID: 18325
          - Population: 1
          - City: Cologne
          - Terrain: Grass
          - Resource: Tobacco
          - Route: Railroad
          - Plot: Land
          - X: 48
          - Y: 27
        
        ### 53
        - Type: SetPopulation
        - OldPopulation: 1
        - NewPopulation: 15
        - City:
          - Owner: Russia
          - CityID: 18325
          - Population: 15
          - City: Cologne
          - Terrain: Grass
          - Resource: Tobacco
          - Religion: Pantheon
          - Route: Railroad
          - Plot: Land
          - X: 48
          - Y: 27
        
        ### 54
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 57%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 17339
        - Player: 6: Germany
        
        ### 55
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 35%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16602
        - Player: 6: Germany
        
        ### 56
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 78%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15227
        - Player: 6: Germany
        
        ### 57
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 25%
          - AI: Defense
          - Unit: Rifleman
          - ID: 12001
        - Player: 6: Germany
        
        ### 58
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 47,24:
          - Owner: Russia
        
        ### 59
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Ocean 48,24:
          - Owner: Russia
        
        ### 60
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Ocean 49,24:
          - Owner: Russia
        
        ### 61
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Ocean 47,25:
          - Owner: Russia
        
        ### 62
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Ocean 48,25:
          - Owner: Russia
        
        ### 63
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 35%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16602
        - Player: 6: Germany
        - Coast 47,23:
          - Owner: Germany
        
        ### 64
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Ocean 49,25:
          - Owner: Russia
        
        ### 65
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 78%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15227
        - Player: 6: Germany
        - Coast 50,24:
          - Owner: Germany
        
        ### 66
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 25%
          - AI: Defense
          - Unit: Rifleman
          - ID: 12001
        - Player: 6: Germany
        - Coast 50,24:
          - Owner: Germany
        
        ### 67
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 51,25:
          - Owner: Russia
        
        ### 68
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 46,26:
          - Owner: Russia
        
        ### 69
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 47,26:
          - Owner: Russia
        
        ### 70
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 57%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 17339
        - Player: 6: Germany
        
        ### 71
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 50,26:
          - Owner: Russia
        
        ### 72
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 57%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 17339
        - Player: 6: Germany
        - Ocean 50,25:
          - Owner: Germany
        
        ### 73
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 51,26:
          - Owner: Russia
        
        ### 74
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 45,27:
          - Owner: Russia
          - Resource: Fish
        
        ### 75
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Grass Hills 46,27:
          - Owner: Russia
          - Resource: Coal
          - Improvement: Academy
        
        ### 76
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 50,28:
          - Owner: Russia
        
        ### 77
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 16%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15529
        - Player: 6: Germany
        - Coast 51,29:
          - Owner: City-State Trowulan
        
        ### 78
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 47,29:
          - Owner: Russia
        
        ### 79
        - Type: TileOwnershipChanged
        - NewOwner: 1: Russia
        - Coast 49,29:
          - Owner: Russia
        
        ### 80
        - Type: CityCaptureComplete
        - Population: 19
        - IsConquest: true
        - TotalGreatWorks: 0
        - CapturedGreatWorks: 0
        - OldOwner: 3: The Inca
        - City:
          - Owner: Russia
          - CityID: 18325
          - Population: 15
          - City: Cologne
          - Terrain: Grass
          - Resource: Tobacco
          - Route: Railroad
          - Plot: Land
          - X: 48
          - Y: 27
        - NewOwner: 1: Russia
        
        ### 81
        - Type: CityPuppeted
        - City:
          - Population: 15
          - Name: Cologne
          - Health: -49%
          - ID: 18325
        - Player: 1: Russia
        
        ### 82
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 94%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17922
        - Player: 1: Russia
        - Grass Land 48,27:
          - Owner: Russia
          - CityID: 18325
          - Population: 15
          - City: Cologne
          - Resource: Tobacco
          - Route: Railroad
        
        ### 83
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - AI: AssaultSea
          - Unit: Attack Submarine
          - ID: 17257
        - Player: 1: Russia
        - Plots:
          - Coast 49,28:
            - Owner: Russia
            - Resource: Fish
          - Coast 48,28:
            - Owner: Russia
          - Coast 47,27:
            - Owner: Russia
        
        ### 84
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18257
        - Player: 1: Russia
        
        ### 85
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Admiral
          - Unit: Great Admiral
          - ID: 17102
        - Player: 1: Russia
        - Plots:
          - Ocean 48,31:
            - Owner: Russia
          - Coast 48,30:
            - Owner: Russia
          - Coast 47,29:
            - Owner: Russia
        
        ### 86
        - Type: UnitMoved
        - Unit:
          - Level: 7
          - AI: CityBombard
          - Unit: Artillery
          - ID: 14685
        - Player: 1: Russia
        - Grass Land 35,27:
          - Owner: Russia
          - Resource: Oil
          - Improvement: Oil Well
        
        ### 87
        - Type: UnitMoved
        - Unit:
          - Level: 14
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 17842
        - Player: 1: Russia
        - Plots:
          - Coast 49,26:
            - Owner: Russia
          - Coast 50,26:
            - Owner: Russia
          - Coast 51,26:
            - Owner: Russia
          - Coast 51,27:
            - Owner: City-State Trowulan
          - Coast 52,27:
            - Owner: City-State Trowulan
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 53,27:
            - Owner: City-State Trowulan
            - Resource: Fish
            - Improvement: Fishing Boats
        
        ### 88
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 3357
        - Player: 1: Russia
        - Plots:
          - Grass Hills 44,29:
            - Owner: Russia
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Grass Hills 45,30:
            - Owner: Russia
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Grass Hills 46,30:
            - Owner: Russia
            - CityID: 2548
            - Population: 23
            - City: Rostov
            - Resource: Stone
            - Religion: Hinduism
            - Route: Railroad
          - Coast 45,29:
            - Owner: Russia
          - Coast 46,28:
            - Owner: Russia
          - Grass Hills 46,27:
            - Owner: Russia
            - Resource: Coal
            - Improvement: Academy
        
        ### 89
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 7471
        - Player: 1: Russia
        - Plots:
          - Coast 14,27:
            - Owner: City-State Shanghai
          - Grass Land 15,28:
            - Owner: City-State Shanghai
            - Improvement: Farm
            - Route: Railroad
        
        ### 90
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 17851
        - Player: 2: Greece
        - Plots:
          - Coast 60,19:
            - Owner: Greece
          - Coast 60,20:
            - Owner: Greece
        
        ### 91
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 17852
        - Player: 2: Greece
        - Coast 60,19:
          - Owner: Greece
        
        ### 92
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 18076
        - Player: 2: Greece
        - Plots:
          - Coast 62,31:
            - Resource: Fish
        
        ### 93
        - Type: CombatResult
        - Grass Land 49,12:
          - Owner: India
          - IsRiver: true
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 12
          - Damage: 12
        - Defender:
          - RemainingHP: 29
          - Damage: 29
          - Player: 4: India
          - Unit:
            - Level: 4
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 14032
        
        ### 94
        - Type: CombatResult
        - Grass Land 49,12:
          - Owner: India
          - IsRiver: true
          - Improvement: Farm
        - Attacker:
          - RemainingHP: 12
          - Damage: 12
        - Defender:
          - RemainingHP: 38
          - Damage: 67
          - Player: 4: India
          - Unit:
            - Level: 4
            - Health: 71%
            - AI: Ranged
            - Unit: Machine Gun
            - ID: 14032
        
        ### 95
        - Type: CombatResult
        - Plains Land 49,10:
          - Owner: India
          - CityID: 10212
          - Population: 25
          - IsRiver: true
          - City: Athens
          - Religion: Hinduism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 15
          - Damage: 15
        - Defender:
          - RemainingHP: 40
          - Damage: 88
          - Player: 4: India
        
        ### 96
        - Type: CombatResult
        - Plains Land 49,10:
          - Owner: India
          - CityID: 10212
          - Population: 25
          - IsRiver: true
          - City: Athens
          - Religion: Hinduism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 4: India
        - Interceptor:
          - Damage: 71
          - Unit:
            - Level: 5
            - Health: 69%
            - AI: DefenseAir
            - Unit: Triplane
            - ID: 15454
          - Player: 2: Greece
        
        ### 97
        - Type: CombatResult
        - Plains Land 49,10:
          - Owner: India
          - CityID: 10212
          - Population: 25
          - IsRiver: true
          - City: Athens
          - Religion: Hinduism
          - Route: Railroad
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 0
          - Damage: 0
          - Player: 4: India
        - Interceptor:
          - Damage: 40
          - Unit:
            - Level: 4
            - Health: 63%
            - AI: DefenseAir
            - Unit: Triplane
            - ID: 15653
          - Player: 2: Greece
        
        ### 98
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18273
        - Player: 2: Greece
        - Plots:
          - Desert Hills 53,16:
            - Owner: City-State Quebec City
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 52,16:
            - Owner: City-State Quebec City
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Grass Land 51,16:
            - Owner: City-State Quebec City
            - Improvement: Embassy
            - Route: Railroad
          - Grass Hills 50,16:
            - Owner: Germany
            - Feature: Forest
        
        ### 99
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - Health: 89%
          - AI: Ranged
          - Unit: Light Tank
          - ID: 16571
        - Player: 2: Greece
        - Plots:
          - Plains Land 66,20:
            - Owner: City-State Zuunmod
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Desert Land 65,21:
            - Owner: City-State Zuunmod
            - Improvement: Fort
            - Route: Railroad
          - Coast 64,21:
            - Owner: City-State Zuunmod
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 64,20:
            - Owner: City-State Zuunmod
          - Coast 63,20:
            - Owner: City-State Zuunmod
          - Coast 61,19:
            - Owner: Greece
        
        ### 100
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17008
        - Player: 3: The Inca
        - Plots:
          - Grass Land 51,16:
            - Owner: City-State Quebec City
            - Improvement: Embassy
            - Route: Railroad
          - Plains Land 52,16:
            - Owner: City-State Quebec City
            - Improvement: Lumber Mill
            - Route: Railroad
            - Feature: Forest
          - Desert Hills 53,16:
            - Owner: City-State Quebec City
            - Resource: Gems
            - Improvement: Mine
            - Route: Railroad
        
        ### 101
        - Type: EspionageState
        - SpyIndex: 3
        - SpyState: 1
        - City:
          - Owner: Germany
          - CityID: 16810
          - Population: 17
          - City: Aachen
          - Terrain: Grass
          - Resource: Sheep
          - Route: Railroad
          - Plot: Hills
          - X: 65
          - Y: 29
        - SpyOwner: 3: The Inca
        
        ### 102
        - Type: CombatResult
        - Grass Land 35,27:
          - Owner: Russia
          - Resource: Oil
          - Improvement: Oil Well
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 30
          - Damage: 30
          - Unit:
            - Level: 7
            - AI: CityBombard
            - Unit: Artillery
            - ID: 14685
          - Player: 1: Russia
        
        ### 103
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17605
        - Player: 4: India
        - Plots:
          - Desert Hills 41,16:
            - Owner: City-State Antananarivo
            - Improvement: Pata-Pata
            - Route: Railroad
          - Plains Land 40,15:
            - Owner: City-State Antananarivo
            - Improvement: Academy
            - Route: Railroad
          - Mountain Mountain 39,15:
            - Owner: India
            - Route: Railroad
          - Plains Hills 39,14:
            - Owner: India
            - Improvement: Mine
            - Route: Railroad
          - Mountain Mountain 38,13:
            - Owner: India
            - Route: Railroad
          - Desert Hills 38,12:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Land 39,9:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Land 40,9:
            - Owner: India
            - CityID: 1060
            - Population: 37
            - IsRiver: true
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
        
        ### 104
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18228
        - Player: 4: India
        - Plots:
          - Desert Land 48,8:
            - Owner: India
            - Resource: Gold
            - Improvement: Manufactory
            - Route: Railroad
          - Desert Land 48,9:
            - Owner: India
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 49,10:
            - Owner: India
            - CityID: 10212
            - Population: 25
            - IsRiver: true
            - City: Athens
            - Religion: Hinduism
            - Route: Railroad
        
        ### 105
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17394
        - Player: 4: India
        - Plots:
          - Desert Land 48,8:
            - Owner: India
            - Resource: Gold
            - Improvement: Manufactory
            - Route: Railroad
          - Desert Land 48,9:
            - Owner: India
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 49,10:
            - Owner: India
            - CityID: 10212
            - Population: 25
            - IsRiver: true
            - City: Athens
            - Religion: Hinduism
            - Route: Railroad
        
        ### 106
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16280
        - Player: 4: India
        - Plains Land 40,9:
          - Owner: India
          - CityID: 1060
          - Population: 37
          - IsRiver: true
          - City: Delhi
          - Religion: Hinduism
          - Route: Railroad
        
        ### 107
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17953
        - Player: 4: India
        - Plots:
          - Desert Hills 38,12:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Land 39,9:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Land 40,9:
            - Owner: India
            - CityID: 1060
            - Population: 37
            - IsRiver: true
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
        
        ### 108
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16281
        - Player: 4: India
        - Plots:
          - Plains Land 39,9:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Plains Land 40,9:
            - Owner: India
            - CityID: 1060
            - Population: 37
            - IsRiver: true
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
        
        ### 109
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17204
        - Player: 4: India
        - Plots:
          - Desert Land 48,8:
            - Owner: India
            - Resource: Gold
            - Improvement: Manufactory
            - Route: Railroad
          - Desert Land 48,9:
            - Owner: India
            - IsRiver: true
            - Improvement: Village
            - Route: Railroad
            - Feature: Flood Plains
          - Plains Land 49,10:
            - Owner: India
            - CityID: 10212
            - Population: 25
            - IsRiver: true
            - City: Athens
            - Religion: Hinduism
            - Route: Railroad
        
        ### 110
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16525
        - Player: 4: India
        - Plots:
          - Plains Land 40,9:
            - Owner: India
            - CityID: 1060
            - Population: 37
            - IsRiver: true
            - City: Delhi
            - Religion: Hinduism
            - Route: Railroad
          - Plains Land 39,9:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 38,12:
            - Owner: India
            - Improvement: Village
            - Route: Railroad
        
        ### 111
        - Type: EspionageState
        - SpyIndex: 5
        - SpyState: 1
        - City:
          - Owner: The Zulus
          - CityID: 1082
          - Population: 34
          - IsRiver: true
          - City: Ulundi
          - Terrain: Tundra
          - Religion: Protestantism
          - Route: Railroad
          - Plot: Land
          - X: 30
          - Y: 46
        - SpyOwner: 4: India
        
        ### 112
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 15744
        - Player: 4: India
        - Plots:
          - Plains Land 40,14:
            - Owner: City-State Antananarivo
            - Improvement: Fort
          - Mountain Mountain 39,15:
            - Owner: India
            - Route: Railroad
        
        ### 113
        - Type: CombatResult
        - Coast 51,10:
          - Owner: India
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 10
          - Damage: 100
          - Unit:
            - Level: 4
            - Health: 10%
            - AI: AssaultSea
            - Unit: Battleship
            - ID: 17725
          - Player: 25
        
        ### 114
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Ranged
          - Unit: Machine Gun
          - ID: 14983
        - Player: 4: India
        - Desert Hills 48,11:
          - Owner: India
          - Resource: Gold
          - Improvement: Mine
          - Route: Road
        
        ### 115
        - Type: CombatResult
        - Coast 50,10:
          - Owner: India
        - Attacker:
          - RemainingHP: 0
          - Damage: 0
        - Defender:
          - RemainingHP: 19
          - Damage: 40
          - Unit:
            - Level: 4
            - Health: 79%
            - AI: AttackSea
            - Unit: Fleet Destroyer
            - ID: 16544
          - Player: 25
        
        ### 116
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17703
        - Player: 5: Venice
        - Plots:
          - Plains Hills 33,41:
            - Owner: City-State Oviedo
            - IsRiver: true
            - Improvement: Mine
            - Route: Railroad
          - Plains Land 32,41:
            - Owner: City-State Oviedo
            - IsRiver: true
            - Resource: Bison
            - Improvement: Camp
            - Route: Railroad
        
        ### 117
        - Type: PlayerDoneTurn
        - NextPlayer: 6: Germany
        - Player: 5: Venice
        
        ### 118
        - Type: MakePeace
        - PacifierFlag: true
        - OriginatingPlayer: 6: Germany
        - TargetTeam: 33
        
        ### 119
        - Type: MinorFriendsChanged
        - IsNowFriend: true
        - OldFriendship: -60
        - NewFriendship: 74
        - MajorPlayer: 6: Germany
        - MinorPlayer: 33
        
        ### 120
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Anti-Aircraft Gun
          - ID: 18376
        - Player: 6: Germany
        - Desert Hills 47,19:
          - Owner: Germany
          - Resource: Aluminum
          - Improvement: Mine
          - Route: Railroad
        
        ### 121
        - Type: UnitCreated
        - UnitType: Anti-Aircraft Gun
        - Player: 6: Germany
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18376
        - Desert Hills 47,19:
          - Owner: Germany
          - Resource: Aluminum
          - Improvement: Mine
          - Route: Railroad
        
        ### 122
        - Type: CityTrained
        - Player: 6: Germany
        - City:
          - Name: Berlin
          - Population: 29
          - ID: 1062
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18376
        
        ### 123
        - Type: CityConstructed
        - City:
          - Name: Hamburg
          - Population: 23
          - ID: 1989
        - Owner: 6: Germany
        - Building: Factory
        
        ### 124
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - Unit: Anti-Aircraft Gun
          - ID: 18377
        - Player: 6: Germany
        - Grass Land 63,26:
          - Owner: Germany
          - Resource: Horses
          - Improvement: Pasture
        
        ### 125
        - Type: UnitCreated
        - UnitType: Anti-Aircraft Gun
        - Player: 6: Germany
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18377
        - Grass Land 63,26:
          - Owner: Germany
          - Resource: Horses
          - Improvement: Pasture
        
        ### 126
        - Type: CityTrained
        - Player: 6: Germany
        - City:
          - Name: Frankfurt
          - Population: 22
          - ID: 6078
        - Unit:
          - Level: 1
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18377
        
        ### 127
        - Type: EspionageState
        - SpyIndex: 2
        - SpyState: 4
        - City:
          - Owner: City-State Lutetia
          - CityID: 1076
          - Population: 28
          - City: Lutetia
          - Terrain: Grass
          - Resource: Porcelain
          - Route: Railroad
          - Plot: Land
          - X: 7
          - Y: 22
        - SpyOwner: 6: Germany
        
        ### 128
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 16354
        - Player: 6: Germany
        - Plots:
          - Desert Land 47,17:
            - Owner: Germany
            - Improvement: Town
            - Route: Railroad
          - Plains Land 47,16:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Land 46,15:
            - Owner: Germany
            - Route: Railroad
          - Plains Hills 45,15:
            - Owner: Germany
            - Improvement: Fort
            - Route: Railroad
          - Grass Land 45,14:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Grass Land 44,14:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
        
        ### 129
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16675
        - Player: 6: Germany
        - Plots:
          - Ocean 72,17:
            - Owner: Russia
          - Ocean 71,17:
            - Owner: Russia
        
        ### 130
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16477
        - Player: 6: Germany
        - Plots:
          - Coast 62,31:
            - Resource: Fish
          - Coast 61,29:
            - Owner: Germany
            - Resource: Fish
        
        ### 131
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 17707
        - Player: 6: Germany
        - Plots:
          - Grass Hills 35,31:
            - Owner: Russia
            - Improvement: Mine
            - Route: Railroad
          - Grass Hills 36,30:
            - Owner: Russia
            - Improvement: Village
            - Route: Railroad
          - Grass Hills 35,29:
            - Owner: Russia
            - CityID: 2095
            - Population: 32
            - IsRiver: true
            - City: Novgorod
            - Resource: Lapis Lazuli
            - Religion: Hinduism
            - Route: Railroad
          - Plains Land 36,28:
            - Owner: Russia
            - Improvement: Farm
            - Route: Railroad
          - Tundra Hills 36,27:
            - Owner: Russia
            - Resource: Sheep
            - Improvement: Citadel
            - Route: Railroad
        
        ### 132
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18120
        - Player: 6: Germany
        - Plots:
          - Tundra Hills 36,27:
            - Owner: Russia
            - Resource: Sheep
            - Improvement: Citadel
            - Route: Railroad
          - Plains Land 36,28:
            - Owner: Russia
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 35,28:
            - Owner: Russia
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 34,29:
            - Owner: Russia
            - IsRiver: true
            - Resource: Deer
            - Improvement: Camp
            - Route: Railroad
            - Feature: Forest
          - Plains Hills 34,30:
            - Owner: Russia
            - IsRiver: true
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 133
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18121
        - Player: 6: Germany
        - Plots:
          - Desert Hills 47,19:
            - Owner: Germany
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Desert Land 47,18:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Land 47,17:
            - Owner: Germany
            - Improvement: Town
            - Route: Railroad
          - Plains Land 47,16:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Hills 46,16:
            - Owner: Germany
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
        
        ### 134
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Caravan
          - ID: 18251
        - Player: 6: Germany
        - Plots:
          - Plains Land 43,13:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Farm
            - Route: Railroad
          - Grass Land 44,14:
            - Owner: Germany
            - IsRiver: true
            - Improvement: Town
            - Route: Railroad
          - Grass Land 45,14:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Plains Land 46,14:
            - Owner: Germany
            - CityID: 1989
            - Population: 23
            - IsRiver: true
            - City: Hamburg
            - Resource: Deer
            - Religion: Hinduism
            - Route: Railroad
        
        ### 135
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: TradeUnit
          - Unit: Cargo Ship
          - ID: 16478
        - Player: 6: Germany
        - Plots:
          - Coast 51,27:
            - Owner: City-State Trowulan
          - Coast 51,26:
            - Owner: Russia
          - Ocean 50,25:
            - Owner: Germany
          - Coast 50,24:
            - Owner: Germany
        
        ### 136
        - Type: PlayerDoTurn
        - Player: 6: Germany
        
        ### 137
        - Type: UnitPromoted
        - Unit:
          - Level: 5
          - Health: 68%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 17339
        - Player: 6: Germany
        - Promotion: Blitz
        
        ### 138
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18376
        - Player: 6: Germany
        - Promotions:
          - Interceptor III
          - Shock I
          - Amphibious
        
        ### 139
        - Type: UnitPromoted
        - Unit:
          - Level: 2
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18377
        - Player: 6: Germany
        - Promotions:
          - Shock I
          - Amphibious
          - Shock II
        
        ### 140
        - Type: PlayerProtected
        - MajorPlayer: 6: Germany
        - MinorPlayer: 28
        
        ### 141
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 83%
          - AI: FastAttack
          - Unit: Landship
          - ID: 16352
        - Player: 6: Germany
        - Plots:
          - Plains Land 49,18:
            - Owner: Germany
            - Improvement: Manufactory
            - Route: Road
          - Grass Land 49,17:
            - Owner: Germany
            - Improvement: Farm
            - Route: Road
          - Grass Hills 50,17:
            - Owner: City-State Quebec City
            - Improvement: Mine
          - Grass Land 51,16:
            - Owner: City-State Quebec City
            - Improvement: Embassy
            - Route: Railroad
        
        ### 142
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Diplomat
          - Unit: Great Diplomat
          - ID: 18310
        - Player: 6: Germany
        - Plots:
          - Plains Land 48,19:
            - Owner: Germany
            - IsRiver: true
            - Resource: Perfume
            - Improvement: Plantation
            - Route: Road
          - Plains Land 49,18:
            - Owner: Germany
            - Improvement: Manufactory
            - Route: Road
          - Grass Land 49,17:
            - Owner: Germany
            - Improvement: Farm
            - Route: Road
          - Grass Hills 50,17:
            - Owner: City-State Quebec City
            - Improvement: Mine
          - Grass Land 51,16:
            - Owner: City-State Quebec City
            - Improvement: Embassy
            - Route: Railroad
        
        ### 143
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: CityBombard
          - Unit: Krupp Gun
          - ID: 11877
        - Player: 6: Germany
        - Desert Hills 49,20:
          - Owner: Germany
          - IsRiver: true
          - Resource: Gems
          - Improvement: Mine
        
        ### 144
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 25%
          - AI: Defense
          - Unit: Rifleman
          - ID: 12001
        - Player: 6: Germany
        - Plots:
          - Ocean 49,23:
            - Owner: Germany
          - Coast 49,22:
            - Owner: Germany
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 48,21:
            - Owner: Germany
          - Desert Hills 48,20:
            - Owner: Germany
            - CityID: 1062
            - Population: 29
            - IsRiver: true
            - City: Berlin
            - Religion: Hinduism
            - Route: Railroad
        
        ### 145
        - Type: UnitMoved
        - Unit:
          - Level: 5
          - Health: 87%
          - AI: AttackSea
          - Unit: Fleet Destroyer
          - ID: 18312
        - Player: 6: Germany
        - Plots:
          - Coast 48,21:
            - Owner: Germany
          - Coast 48,22:
            - Owner: Germany
          - Coast 47,22:
            - Owner: Germany
        
        ### 146
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - Health: 97%
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 15389
        - Player: 6: Germany
        - Plots:
          - Coast 49,21:
            - Owner: Germany
          - Coast 48,21:
            - Owner: Germany
          - Coast 48,22:
            - Owner: Germany
        
        ### 147
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: AttackSea
          - Unit: Destroyer
          - ID: 16752
        - Player: 6: Germany
        - Plots:
          - Coast 48,22:
            - Owner: Germany
          - Coast 47,22:
            - Owner: Germany
          - Coast 46,22:
            - Owner: Germany
        
        ### 148
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: AssaultSea
          - Unit: Battleship
          - ID: 18256
        - Player: 6: Germany
        
        ### 149
        - Type: UnitBuildCompleted
        - Owner: 6: Germany
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 7874
        - Build: Construct a Mine
        - Tundra Hills 61,47:
          - Owner: Germany
        
        ### 150
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 15391
        - Player: 6: Germany
        - Plots:
          - Plains Hills 46,16:
            - Owner: Germany
            - Resource: Sheep
            - Improvement: Pasture
            - Route: Railroad
          - Desert Land 46,15:
            - Owner: Germany
            - Route: Railroad
          - Plains Land 46,14:
            - Owner: Germany
            - CityID: 1989
            - Population: 23
            - IsRiver: true
            - City: Hamburg
            - Resource: Deer
            - Religion: Hinduism
            - Route: Railroad
        
        ### 151
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Worker
          - Unit: Worker
          - ID: 16811
        - Player: 6: Germany
        - Plots:
          - Desert Land 46,15:
            - Owner: Germany
            - Route: Railroad
          - Plains Land 47,16:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Land 47,17:
            - Owner: Germany
            - Improvement: Town
            - Route: Railroad
          - Desert Land 47,18:
            - Owner: Germany
            - Improvement: Village
            - Route: Railroad
          - Desert Hills 47,19:
            - Owner: Germany
            - Resource: Aluminum
            - Improvement: Mine
            - Route: Railroad
          - Desert Hills 48,20:
            - Owner: Germany
            - CityID: 1062
            - Population: 29
            - IsRiver: true
            - City: Berlin
            - Religion: Hinduism
            - Route: Railroad
          - Coast 48,21:
            - Owner: Germany
          - Coast 49,21:
            - Owner: Germany
          - Coast 50,21:
            - Owner: Germany
            - Resource: Oil
            - Improvement: Offshore Platform
        
        ### 152
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Defense
          - Unit: Rifleman
          - ID: 12681
        - Player: 6: Germany
        - Grass Land 68,26:
          - Feature: Jungle
        
        ### 153
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18250
        - Player: 6: Germany
        - Plots:
          - Coast 62,41:
            - Owner: City-State Melbourne
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 63,40:
            - Owner: City-State Melbourne
        
        ### 154
        - Type: UnitMoved
        - Unit:
          - Level: 3
          - AI: Defense
          - Unit: Rifleman
          - ID: 12110
        - Player: 6: Germany
        - Coast 59,48:
          - Owner: Germany
          - Resource: Fish
        
        ### 155
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 16231
        - Player: 6: Germany
        - Grass Land 46,23:
          - Owner: Germany
          - Resource: Oil
          - Improvement: Oil Well
        
        ### 156
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18377
        - Player: 6: Germany
        - Plots:
          - Plains Land 63,25:
            - Owner: Germany
            - Improvement: Fort
          - Coast 64,25:
            - Owner: Germany
          - Coast 65,24:
            - Owner: Germany
        
        ### 157
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Counter
          - Unit: Anti-Aircraft Gun
          - ID: 18376
        - Player: 6: Germany
        - Plots:
          - Desert Hills 48,20:
            - Owner: Germany
            - CityID: 1062
            - Population: 29
            - IsRiver: true
            - City: Berlin
            - Religion: Hinduism
            - Route: Railroad
          - Coast 48,21:
            - Owner: Germany
          - Coast 49,21:
            - Owner: Germany
          - Coast 50,21:
            - Owner: Germany
            - Resource: Oil
            - Improvement: Offshore Platform
        
        ### 158
        - Type: UnitMoved
        - Unit:
          - Level: 4
          - AI: Paradrop
          - Unit: Paratrooper
          - ID: 18249
        - Player: 6: Germany
        - Desert Land 49,19:
          - Owner: Germany
          - IsRiver: true
          - Improvement: Farm
          - Feature: Flood Plains
        
        ### 159
        - Type: UnitMoved
        - Unit:
          - Level: 1
          - AI: Messenger
          - Unit: Ambassador
          - ID: 18245
        - Player: 6: Germany
        - Plots:
          - Coast 53,21:
            - Owner: City-State Trowulan
          - Coast 54,22:
            - Owner: City-State Trowulan
          - Grass Hills 54,23:
            - Owner: City-State Trowulan
            - CityID: 14185
            - Population: 12
            - City: Arequipa
            - Route: Railroad
          - Coast 55,23:
            - Owner: City-State Trowulan
          - Coast 56,23:
            - Owner: City-State Trowulan
            - Resource: Fish
            - Improvement: Fishing Boats
          - Coast 60,23:
            - Owner: Germany
          - Grass Land 61,24:
            - Owner: Germany
            - Resource: Rice
            - Improvement: Farm
        
        ### 160
        - Type: PlayerDoneTurn
        - NextPlayer: 7: The Zulus
        - Player: 6: Germany
        
        You, Bismarck (leader of Germany, Player 6), are making strategic decisions after turn 424.
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
        - Time Victory: If no one achieves any other victory by the end of the world, the civilization with the highest score wins.
      - Opponents: summary reports about visible opponents in the world.
        - You will receive staff members' diplomatic evaluations.
        - You will receive each opponent's publicly available relationships.
        - You will receive the best available location for your next settlement.
      - Cities: summary reports about discovered cities in the world.
        - Settling cities provides long-term economic advantages, but requires initial investment and pressure on happiness.
      - Military: summary reports about tactical zones and visible units.
        - Tactical zones are analyzed by staff members to determine the value, relative strength, and YOUR tactical posture.
        - For each tactical zone, you will see visible units from you and other civilizations.
      - Events: events since the last decision-making.
    - You are Bismarck, leader of Germany (Opponent 6).
      
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
      - Name: Germany
      - Uniques:
        - Unique Unit: Landsknecht, Replacing Tercio (Requires technology: Gunpowder)
        - Unique Unit: Krupp Gun, Replacing Artillery (Requires technology: Replaceable Parts)
        - Unique Building: Hanse, Replacing Customs House (Requires technology: Guilds)
        - Unique Building: Brewhouse, Replacing Windmill (Requires technology: Economics)
        - Civilization Ability: Gain +1 Influence per turn with City-States for each gifted Unit (lost when killed). -15% Production and Gold costs for Military Units.
      - Leader: Bismarck
      - OpponentID: 6
      
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
      - Combined Arms: Allows you to build the Tank, a fast and deadly armor Unit.
        Completing it would unlock: Radar
      - Satellites: Allow you to build the Apollo Program, a project necessary to win a Science Victory.
        Completing it would unlock: The Internet, Lasers
      - Penicillin: All Workers receive the Fallout Reduction Promotion, which reduces the amount of damage they take while scrubbing Fallout. Allows you to build the Marine, a Unit that specializes in amphibious assaults. Also allows you to build the Medical Lab, a building which speeds the growth of your Cities.
        Completing it would unlock: Electronics
      
      ## Policies
      - Martial Spirit (Level 2 Tenet of Ideology Autocracy): Martial Spirit: +25% Combat Strength when attacking in melee for 50 turns, scaling with world speed. War Weariness reduced by 25%, and Razing Speed is doubled.
      - Total War (Level 2 Tenet of Ideology Autocracy): Total War: +25% Production when building Land Units. Warscore increases 25% more quickly, and it is 25% easier to bully City-States.
      - Third Alternative (Level 2 Tenet of Ideology Autocracy): Third Alternative: Quantity of Strategic Resources produced (including Paper) is increased by 100%. Reduces Unit Gold Maintenance costs by 25%.
      - Lightning Warfare (Level 2 Tenet of Ideology Autocracy): Lightning Warfare: +3 Movement for Great Generals. Gunpowder units gain +15% attack and ignore enemy ZOC; Armored units gain +15% attack and +1 Movement.
      - Mare Nostrum (Level 2 Tenet of Ideology Autocracy): Mare Nostrum: +1 Oil and Coal for every City-State Alliance. +2 Production and Culture to Atolls, Fishing Boats, and Offshore Oil Platforms. Naval Ranged Units gain the Mare Nostrum Promotion.
      - Futurism (Level 1 Tenet of Ideology Autocracy): Futurism: Strengthens Tourism of Historic Events generated by the Palace. +2 Culture from Great Works. Earn 50 Tourism when you conquer a city for the first time, scaling with Era and city size.
      - Heritage (Continuing Artistry Branch):
        - * +4 Gold from Great Works of Music.
        - * +50% to all / Theming Bonuses on Empire
        - * 25% of the Culture from World Wonders and Tiles is added to the Tourism output of the city.
      - Exploitation (Continuing Imperialism Branch):
        - * +2 Food and +1 Production from Farms, Camps, and Plantations.
        - * +1 Production and Science from Coasts, Lakes, and Oceans.
      - Police State (Level 2 Tenet of Ideology Autocracy): Police State: +3 Local Happiness from every Courthouse, and +10 City Security from Police Stations. +100% Production towards Courthouses and Police Stations.
      - Lebensraum (Level 1 Tenet of Ideology Autocracy): Lebensraum: Receive 10 Culture and Golden Age Points when your borders expand, scaling with Era. Citadels may also be built in foreign territory adjacent to your borders. Retain tiles after razing Cities.
      - New World Order (Level 1 Tenet of Ideology Autocracy): New World Order: -2 Unhappiness from and Distress in all Cities. Police Stations and Constabularies provide +3 Culture and +5 Production, and are constructed 100% more quickly.
      - Shadow Networks (Continuing Statecraft Branch):
        - * Receive 25% of Science generated by Allied City-States.
        - * +3% Culture in Capital for every 100 Spy Points ever accumulated (up to 30%).
        - * +3 Science from Constabularies and Police Stations.
        - * +1 Science from Specialists.
      - National Treasure (Continuing Artistry Branch):
        - * +2 Science from Artifacts.
        - * A Great Person of your choice appears near your Capital.
        - * Gain 250 Gold when you construct World Wonders, scaling with Era.
      - Iron Fist (Level 1 Tenet of Ideology Autocracy): Iron Fist: Vassals can no longer be liberated by other Civilizations or the World Congress, and capitulated vassals can no longer rebel. Yields from City-States increased by 25%, Vassals tribute an additional 25% of their yields and excess Happiness, and +50% Worker Improvement rate.
      - Rights of Man (Continuing Rationalism Branch):
        - * -1 Unhappiness from all Needs in all Cities.
        - * +2 Production and Gold from Villages.
        - * +10% Science during Golden Ages.
      - Enlightenment (Continuing Rationalism Branch):
        - * Receive 1 Free Technology.
        - * +1 Happiness from Universities.
      - Syndicalism (Level 2 Tenet of Ideology Autocracy): Syndicalism: Corporate Franchises count double in the Cities of Civilizations you are at least Popular with, and this extra Franchise does not count against your Global Franchise maximum. Can establish 5 additional Franchises in foreign Cities. +2 Production from all Corporation Offices.
      - Industry (New Branch):
        - Industry provides bonuses to empires focused on Gold and Production.
        - Adopting Industry grants:
        - * +2 Trade Routes.
        - * -5% Gold needed for purchases.
        - Each Industry policy unlocked grants:
        - * -5% Gold needed for purchases.
        - Adopting all Policies in Industry grants:
        - * Unlocks building Broadway.
        - * +3 Happiness per unique owned Luxury Resource.
        - * +2 Production and Gold from Specialists.
        - * Allows for the purchase of Great Merchants with Faith starting in the Industrial Era.
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
  - decisions:
    - #0:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Satellites is the fundamental technology required to build the Apollo Program and progress toward our Spaceship Grand Strategy (Science Victory). It also unlocks key late-game techs like Lasers and The Internet, making it our top research priority once Computers is completed.
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Third Alternative
        - Rationale: Russia's capture of Cologne has placed their massive military (15.4k, 4.6x ours) directly on our northern border, posing an existential threat. Third Alternative is a critical survival policy: it doubles our strategic resources (increasing Uranium from 3 to 6 for nuclear deterrence, and Aluminum from 10 to 20 for advanced aircraft and spaceship parts) and reduces unit gold maintenance by 25%, rescuing our strained gold economy (+10 GPT) while we support a large standing defensive army and navy.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: -95
        - Rationale: Russia represents an existential threat to Germany. Having captured Cologne, they directly border our capital region near Berlin. We must maintain maximum hostility, gather intelligence, and prepare a strong defensive deterrent against their 15.4k military strength.
        - Private: -95
        - TargetID: 1
    - #3:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Private: 15
        - Public: 15
        - Rationale: Slightly improve relations with India. They are our key Declaration of Friendship partner, acting as a crucial diplomatic and trade counterweight in the region. While they are a strong cultural victory contender, maintaining this alliance is vital to prevent absolute diplomatic isolation and secure our southern borders.
    - #4:
      - toolName: set-relationship
      - args:
        - Public: -95
        - Rationale: We remain at war with the Inca, but since Russia has seized Cologne and decimated Incan power (reducing their military to 1.3k), they no longer pose a primary strategic threat. We maintain hostility but will avoid committing offensive military resources, focusing purely on defense against Russia.
        - Private: -100
        - TargetID: 3
    - #5:
      - toolName: set-relationship
      - args:
        - Public: -50
        - Rationale: Maintain guarded relations with the Zulus. Our peace treaty has expired, and they possess 6.1k military strength and a defensive pact with the Inca. We must remain extremely cautious and defensive to avoid provoking them into launching a secondary offensive against us.
        - TargetID: 7
        - Private: -45
    - #6:
      - toolName: set-flavors
      - args:
        - Flavors:
          - CityDefense: 95
          - Science: 100
          - Defense: 95
          - Espionage: 95
          - Expansion: 0
          - Production: 100
          - UseNuke: 95
          - Nuke: 100
          - Antiair: 95
          - Gold: 85
          - Naval: 90
        - GrandStrategy: Spaceship
      - rationale: Maintain our science and production focus at 100 to support the Spaceship victory pathway while maximizing defensive parameters (Defense 95, CityDefense 95, Antiair 95, Nuke 100, UseNuke 95) to deter a Russian invasion. Gold and Espionage are prioritized to stabilize our economy and protect our tech centers, while Expansion remains at 0 to focus entirely on local defensive build-up.
  - tokens:
    - inputTokens: 52861
    - reasoningTokens: 9479
    - outputTokens: 649
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Recent Developments**
            
            My focus is on the crucial shift in power: Cologne has been captured. I'm now evaluating the implications of this development for our strategic position and future actions.
            
            **Assessing Strategic Implications**
            
            The capture of Cologne by Russia is a significant shift. I'm analyzing its direct impact on our borders and Russia's increased territorial control, particularly given their growing military strength relative to ours and Germany's.
            
            **Revising Defensive Strategy**
            
            My analysis has shifted; the coordinates confirm Cologne's position north of Berlin. Russia, an Order ideology state with Autocratic Germany and my Autocracy, is currently at war with the Inca and Venice. I'm re-evaluating our defensive posture versus initiating conflict, especially with Computers research 13 turns away.
            
            **Evaluating Policy Options**
            
            My attention has shifted to our policy choices. Futurism was previously selected but remains pending due to a 14-turn adoption period. I'm now reviewing the available policies, considering whether Futurism is still optimal given the evolving strategic landscape and the emergence of new options.
            
            **Reconsidering Policy Adoption**
            
            I'm re-evaluating our policy choices. Futurism's lengthy adoption period makes me question its continued relevance. Given Russia's capture of Cologne, and their overwhelming military advantage, I need to consider if this policy aligns with our new defensive priorities and potential conflict scenarios.
            
            **Detecting Impending Victory**
            
            India's influence over all other civilizations is a critical update. I'm now verifying if they are on the cusp of a Cultural Victory, as their current standing seems to fulfill most victory conditions.
            
            **Analyzing Victory Conditions**
            
            My focus has shifted to the imminent threat of an Indian Cultural Victory. I'm urgently assessing our options to counter this, weighing the effectiveness of aggressive action against the potential benefits of delaying their win to pursue our own Science Victory, especially with Russia's growing military strength nearby.
            
            **Confirming Peace Treaty Status**
            
            I'm actively verifying the status of our peace treaty with the Zulus. It appears to have expired, leaving us potentially open to hostilities. I'm cross-referencing reports to confirm this critical detail and assess the immediate implications for our security.
            
            **Confirming War Participants**
            
            My focus is now on clarifying our current wartime entanglements. It seems Venice, as a vassal of the Inca, means our conflict with them extends to the Inca. I'm weighing whether to press this advantage against the weakened Inca or seek peace.
            
            **Confirming War Rationale**
            
            I'm reassessing our war with the Inca. Since they no longer occupy any of our cities, and Russia is actively conquering them, I question the continued utility of this conflict given their low military strength.
            
            **Assessing Alliance Risks**
            
            I'm re-evaluating the Inca conflict. The Zulu defensive pact means attacking them draws in a stronger enemy. Given our current military weakness relative to both Zulu and Russia, I'm prioritizing defense and resource acquisition over aggression.
            
            **Researching Nuclear Capability**
            
            I've just confirmed we possess three Uranium units. This, combined with Manhattan Project being only one turn from completion, means we're on the verge of nuclear weapon production. I'm now prioritizing research into Fission to unlock atomic bomb capabilities.
            
            **Prioritizing Science Victory**
            
            I've confirmed that Satellites is available, directly aligning with our Science Victory strategy. Given our high science output, I'm setting Satellites as the next research target to unlock the Apollo Program and pave the way for our "Spaceship" victory.
            
            **Defending Against Russia**
            
            I'm reassessing our defenses against Russia, especially after they took Cologne. Their immense military strength, coupled with their naval presence near our coast, demands a purely defensive strategy. My priority is building up our forces and completing our nuclear program to deter any aggression.
            
            **Evaluating Diplomatic Opportunities**
            
            I'm reassessing our relationship with Russia. They despise us, but they're also busy fighting the Inca and Venice. Crucially, they're friends with India, who is close to a Cultural Victory. I need to see if India's policies offer any leverage.
            
            **Analyzing World Congress**
            
            I'm reviewing the World Congress resolutions, noting the "Travel Ban" is active, which helps slow India's cultural push. I'm also assessing upcoming proposals, particularly the "Endowment for the Arts" from the Inca, to understand their potential impact.
            
            **Analyzing World Congress Proposals**
            
            I'm analyzing the potential impact of upcoming World Congress resolutions. I must oppose the "Endowment for the Arts" as it benefits cultural rivals like India and the Inca, and I have insufficient delegates to guarantee success. Greece's strong influence is a significant factor here.
            
            **Liberating Lost Territory**
            
            My focus has shifted to the strategic importance of Cologne, which Russia now controls. I'm considering whether to pursue peace with the weakened Inca to consolidate forces for a potential liberation attempt on our former German city, given the current territorial dynamics.
            
            **Adjusting Diplomatic Stances**
            
            I'm refining our relationships. I'll maintain the hostile stance towards the Inca to potentially secure peace, while keeping the Zulus at a wary distance due to their military strength and proximity. India remains a vital ally, and Venice a key economic partner.
            
            **Refining Diplomatic Relationships**
            
            I'm adjusting our approach to Venice. Despite their weakness and vassal status to the Inca, I want to keep them friendly. This way, a peace with the Inca will allow immediate trade restoration. My strategic flavors are excellent, especially Science and Production, aligning perfectly with our victory goals.
            
            **Reviewing Policy Options**
            
            I'm reassessing our current policy choices. With Futurism's extended adoption, I'm evaluating if newly available Autocracy level 2 policies like Martial Spirit, Total War, or Police State better align with our defensive posture and ongoing conflict dynamics, particularly against Russia.
            
            **Adopting New Autocracy Tenets**
            
            I've realized we've already adopted three Level 1 Autocracy tenets, meaning we can now select from the Level 2 options. I'm reviewing Martial Spirit, Total War, Third Alternative, Lightning Warfare, and Mare Nostrum to see which best suits our current defensive and scientific priorities.
            
            **Doubling Strategic Resources**
            
            I'm prioritizing "Third Alternative" because doubling our strategic resources, especially Uranium and Aluminum, is critical for our defense and future military buildup against Russia. This policy significantly boosts our atomic bomb and air force potential.
            
            **Selecting Autocracy Tenets**
            
            I'm comparing the remaining Autocracy Level 2 tenets. While Third Alternative doubles strategic resources, the 25% reduction in unit maintenance from Mare Nostrum is crucial for our struggling economy, especially given our current +10 GPT. This will allow for more unit upgrades and city-state influence.
            
            **Selecting Autocracy Tenets**
            
            I'm reconsidering my choice between "Third Alternative" and "Mare Nostrum". While "Third Alternative" addresses critical resource bottlenecks, "Mare Nostrum" offers significant economic relief by reducing unit maintenance, which is essential given our current GPT. I'm weighing which provides the most immediate strategic advantage.
            
            **Selecting Autocracy Tenets**
            
            I've decided to adopt "Third Alternative" to double our strategic resources, which is vital for my nuclear program and defense against Russia. I'm also reviewing "United Front" for its military advantages. My persona values, particularly being guarded and afraid of Russia, will guide my cautious approach.
            
            **Refining Relationship Parameters**
            
            I'm finalizing our diplomatic stances, keeping Russia at maximum hostility due to their overwhelming military and threat to Berlin. I'll maintain a strong friendship with India as a counterweight, and am considering slightly increasing our positive standing to further solidify this alliance against potential aggressors.
            
            **Adjusting Diplomatic Alliances**
            
            My focus is on recalibrating our international relationships. I'm strengthening ties with India while maintaining a wary distance from the Zulus, and will seek peace with the Inca and Venice to secure trade and consolidate resources, especially given Russia's continued dominance.
            
            **Finalizing Diplomatic Actions**
            
            I'm preparing to finalize multiple diplomatic actions simultaneously. This includes adjusting relationships with Russia, India, the Inca, and Zulus, setting Satellites as our next research target, adopting the "Third Alternative" policy, and confirming our strategic flavors.
            
            **Finalizing Diplomatic Actions**
            
            I'm preparing to finalize multiple diplomatic actions simultaneously. This includes adjusting relationships with Russia, India, the Inca, and Zulus, setting Satellites as our next research target, adopting the "Third Alternative" policy, and confirming our strategic flavors.
            
            **Finalizing Diplomatic Actions**
            
            I'm preparing to finalize multiple diplomatic actions simultaneously. This includes adjusting relationships with Russia, India, the Inca, and Zulus, setting Satellites as our next research target, adopting the "Third Alternative" policy, and confirming our strategic flavors.
            
            **Adjusting Diplomatic Stances**
            
            I'm finalizing our diplomatic actions. I'll adjust relations with the Zulus to be guarded, set Satellites as the next research, and adopt "Third Alternative." My strategic flavors are locked in, emphasizing Science, Production, and robust defense against Russia.
            
            **Finalizing Diplomatic Moves**
            
            I'm confirming our diplomatic relationships and spy placements. All target IDs for major civs are correct, and my agents are actively gathering intelligence in key enemy cities. I'm also verifying the trade agreement with Venice remains active and beneficial.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: uPc5U6bSTpHLZODP
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Satellites is the fundamental technology required to build the Apollo Program and progress toward our Spaceship Grand Strategy (Science Victory). It also unlocks key late-game techs like Lasers and The Internet, making it our top research priority once Computers is completed.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: QkJksstKTwWjWcja
          - toolName: set-policy
          - input:
            - Policy: Third Alternative
            - Rationale: Russia's capture of Cologne has placed their massive military (15.4k, 4.6x ours) directly on our northern border, posing an existential threat. Third Alternative is a critical survival policy: it doubles our strategic resources (increasing Uranium from 3 to 6 for nuclear deterrence, and Aluminum from 10 to 20 for advanced aircraft and spaceship parts) and reduces unit gold maintenance by 25%, rescuing our strained gold economy (+10 GPT) while we support a large standing defensive army and navy.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: kMnoKRfXbD7Z4lzj
          - toolName: set-relationship
          - input:
            - Public: -95
            - Rationale: Russia represents an existential threat to Germany. Having captured Cologne, they directly border our capital region near Berlin. We must maintain maximum hostility, gather intelligence, and prepare a strong defensive deterrent against their 15.4k military strength.
            - Private: -95
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: oPSt3ytpHk92EzcX
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Private: 15
            - Public: 15
            - Rationale: Slightly improve relations with India. They are our key Declaration of Friendship partner, acting as a crucial diplomatic and trade counterweight in the region. While they are a strong cultural victory contender, maintaining this alliance is vital to prevent absolute diplomatic isolation and secure our southern borders.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: R0U201uoBO4vk22s
          - toolName: set-relationship
          - input:
            - Public: -95
            - Rationale: We remain at war with the Inca, but since Russia has seized Cologne and decimated Incan power (reducing their military to 1.3k), they no longer pose a primary strategic threat. We maintain hostility but will avoid committing offensive military resources, focusing purely on defense against Russia.
            - Private: -100
            - TargetID: 3
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: E8vOilYw5jeQ3G2v
          - toolName: set-relationship
          - input:
            - Public: -50
            - Rationale: Maintain guarded relations with the Zulus. Our peace treaty has expired, and they possess 6.1k military strength and a defensive pact with the Inca. We must remain extremely cautious and defensive to avoid provoking them into launching a secondary offensive against us.
            - TargetID: 7
            - Private: -45
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 7GPuJbnQCRpxrDpa
          - toolName: set-flavors
          - input:
            - Flavors:
              - CityDefense: 95
              - Science: 100
              - Defense: 95
              - Espionage: 95
              - Expansion: 0
              - Production: 100
              - UseNuke: 95
              - Nuke: 100
              - Antiair: 95
              - Gold: 85
              - Naval: 90
            - Rationale: Maintain our science and production focus at 100 to support the Spaceship victory pathway while maximizing defensive parameters (Defense 95, CityDefense 95, Antiair 95, Nuke 100, UseNuke 95) to deter a Russian invasion. Gold and Espionage are prioritized to stabilize our economy and protect our tech centers, while Expansion remains at 0 to focus entirely on local defensive build-up.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: uPc5U6bSTpHLZODP
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/zzxg0zudj4BJALGiJqSJ0oV0lgihEic6YAArMn9xP9jOy8Ii6CEqPfuvdz6vDbSGquoJazMUjncDKmRLRugpsAokDuZCFS0kWpILMomq7CAxZ5sVKxJRfz5viyfQK0mu+U766dR228rXAC8sA9Y6uuoCcROnTG6GaEZ6ZauUcPYnPOCMZQNE9qHJxkDaiQWO1sd6zqqvPvl0IylLjQS29ocgZO3+5lMbo/drX9vW2q9Ag073aiBbCGXv5Bnpg3XS8KI0cYxo0vaLBsm/bDxhSE3inspSQhNLyKG7977b1ZSBPutAzSp23A1vyoM4lr161DatEKCmQ5WdM5c/ZOHMx3xoaSlp0HcApVaNSmf88HzM0AdxhNw4hd8/Ki9orX7urjmAT83aqIf9cZ44MEeV/DpW/2LPviCRKKX7heO0eY8dV8YzpiobDy4ghCROs596V6xV+VsAv7s4M4tOHoOKaKfVb8QqyPVbY1bEMm+nQ1bWpn6x2utbIBy5aFFCAfw7AiA00GBL/pn9yYhOmD0rwNwuZ2MQXLJJeRDpPzqV6CX2tJafQ3NwAj4RKFYaQpEUdTY1578eCUId4Kh3731N6lOQvTe4Z/A4miQpAmiBZJqqCk/+5+u9qYhCe2kLfHDbdSDzNz/8ivP1T+CGR7Jx/DNOkogco6ybFhe70qpLaa060BqtceZiKBfjZK9qygf/fgJQ4GJYoagDPGgNDWRk9WPsPRmwpyxu0X3Lp+/kRmi6AktBWMFRqTyy13QYZ9zSPllbPP4sUq0RUhal+b5vXUxC+58r4TvwVhO7jFjiEjVC4O+eO1OQaUbEpo6lYwdg8aSw4Hs26DDcwHtlkYrsL1Y84e9ekoMasRlE0BTGNMILK0pEd3jFy5cYdDOTfd8lJWRpmLL2XtzHshq2agQvXQInHRmSSQuqb5FKcQ1tguJwB4ohkbcKYqusqPP0hrmoCIRCs+g+o1xkFRg+B/qemmOhOMP3+k1LQ/iFIUFa85j5/dOT0PPgtrlU03Vq/pvaEpxJYd5c5z2srGljo0uCpvvUBc5hWhppN+ptNG7qHRrqN1Xi94j97aXKBon1vEW0XykZWmZiYrFBU92nslD1I4QZHgJXzKxGifkmk7XSt0vOZrS7PqOirQTbXyKs1S5WT4xK2B7mVawTCTzLgwWvLym/ecRkyB/1KnF/WTT1tAJpnFYFu3OM3RodnwMbUCJUSQOoSMsmwAgTvRHSQLDFj6aLHK3Yjcf7MT9B9hB/fJeq1ZXf4VTRJhXKUgxaeWM7qxNYTWBSl849ebdzQFy1LhEiKXiE1yf7Ea6VCGD8RkaDps5gFs7q3/fO/Xmtm6QByWZFVBLpP19F5tNVf1YKVixoiJnB1Ey19HHYNJEkKOYmErF4huNlpWK34a+8G1FsugjCeBPTlYT7tEA+2WTliqoq90jY9bzMuDNmq9ECnXlbaudvjfU1gDOs7VFTjtTTnNoR6mKQ5yrISDXrMPbX9nv959OVvTKLEWIZ0Qq5jRYJmRr9RyUPwWLK5MvFKOHsFMDy2YNkZhDhuaSESXw4QkqfKOpB+zWRSwjlXjLpklgpRhETeVPDCXJpT67Kne7fBA9bxXvZubP4JssFkkwwWUhZp/NAmYzvBmY5QtENHKqghcexToXHZOUjYI1/C1pUSITwl3FogONk1pZWjXh67//b9fd+uHvYBBkfYR1wXKlq8+R1j2zwYohqnELEo3SKmQG0Bni0nRmiH2GIBLEHP4UnQYMR5fnY2zdUYKh3aUcy14i6bNDlapoHRy5KX9FivVgXYdxDHXK2/8NY/3CW3G6EZdE5qmn/Wo0tosgGTMraAK1wxFveCNxeLkZ3ICn4c5cjPLyU8TWklkjaVxXnmEMhl0dJ2qVTbCDvfX/OpGQtYk2D2nROk+5YKlQcvN+bWMBgVpaA+xEanBtZPbidmN5EfHnOLhwHSvqFLrrht9AMUCA+iOuoFXWa8FEABpw6LcufCe54vfAmdx1vSZ92r2gLKVwYDDI6FXSflJHsOduUJ+IkGulJOdsPdFR8r6mNSm3mn2yJ1S6uINbNKe58fouSX1VQvi+HwFNv8TEcOwWQqNhO1SYiVGt0/X5mK13oATY0Jhoip2inntExsKut1int7fCj80OgraCTa23l/9EMbtI6ujjf+Rjqzdxvp0QG4FswXKlJ7mw2IakRDRvTkKir0LZjpcLo3zlxT8uSLfeHcw0ATSyZLizsvesT2TaBuLj/ywv/l8ZqZtzeeGjmk4SX63uhk/zdh0uLo6fZaFOrrK5orI3+mNpKXdvIBficnotXcRP7MTKNJIsgEYyl2eaLh+WGzhaqVxQ0P84wA0KtLlC08mBxOTMbkjmjP3Gkc1Mg+BaOuMQwDiuS1Z0CE8KdWLGe0q1pZnFJA8e1UTwG8FaK7/70boT6WXK2qxluSfldBungPWBMcBWqr0wo6+npnQUfiSX0xI5hJe+N4JFMXq05rVbCowuw8L78BQUfMHfd3yGTqgA+mvhNoH2iXL4X71rV1BcJzGFMuPwbIsZKBM8C3mAPvNmd/ryu2/OBzoH6cyXNnl8ukRxWGuXoaGd/w2buo3XRc555dKKGOPl29qa+d6aWk+vA5Zw3ICb0THwsp1HPxOCBm4GaaplDx+n8E80IMmBDjGkofqnLa/ktAIyxJcIOPQyKrcmlCbU4qz+a+g8KfpZpFRpfj+pTavPiXFRxrk3EMg7793tVde46SK1ngxF45HlvlqD+0i4BkXuRTROUDvn8tpx2RWneDftrB2cD1YVRu2MVKX4JJ//0n4PV8xhxAix5E1OvMOoVcfvg3cxQJlguMR3Ob2SPqbdflcOWibZXVg5hMimK6/sZejGVAPHB/uUWnPd7MysCcpxNTAnjwyx4WAHP5LZDqxBvBy/yJl7AL0su0k0KDiw/7xqmZdeTGJC7kbMxTy0jnSPKXxuafzXwjMS2+0l7IR4j79+8kOj1VmK3SfbjD+wIVQLUje65dxkoabt+YR7j14P2F0al75RXNpfGK8eiQoA7bolVEXSzZfVBjA+xGIbOGockDvQ5aFxuC/BYUTcFvHDi9HaakvSEh2n0crhMeQrQoDBzaTBYjMkvvpygmw55IfxU+9MORooq9fDVVPBKs4vODeHz8G/zb/m+2ow0g1GR+tabEe/twV5c3sVpjw+nWoUXeHIdxQPoZgTwJ5jcBFIEOFX6iTNhL8v+4wkiHE/FETF5cKIQxSiVgtqkVxsPmimRkwhb0ZAt9VrxRmYTA2f/p8Sd1p0MwdUsr8V5Io2IBs7EEOpF+rjOgEpq7SgH1fHr234L8xL/4fzabJ9VoF+/IwdCQbBwSfYNiHZniUZ0O4pS0CpZhJF7bQokCh8ZSCLYaerFajEffi1csGUQG/RgjHz/uWlR74SzzQxuUSi6jdmgRyOrIkL7DbvHBEHX+nw6UPSAI07/ObS1s4xeqLZQCfSNH91SjxGkDdyIHaFhOBJeJkxlcaF+OQvWY3YHNHUSdE/t+OcL3pfcuwquo6gD51kCBuWMyLXpFoHCoA8fpdc0LRBFLDVFodR60T7qXmT18hZFlysS52Zd1kNOrvv/Kfq/Lxn7YLtyMYmbiWr0baNms3a0rWONmRTIdxux9+tOR5fpFBPnHO7QuBcTPNq1hfIfzutzcBR7SOM4q2Qm+jniw6EMufkrAn0sjySwHLn2eJ0R1o2prZvKvqnbT+aGmOmV9vJhyJsXjmLRHd8+bfd/P/ns4DW6Lr0j6lWL7aHeSXnFfb4LSfVDc2LAG7fEYl0LCxyhrZ6GIwkI+GLuPWUshJXK1nhe/zaLlFS8FV+GxhRspvMrikKRN9rwfCwbzBkRMVSP6i/MdoHJsASJ12284bei+4VYljwScW9LMdPZoThI5gkNMX3hdLBhjmyZugPHPHL9cF0fwlTBKbWTxa6FxAIVuvPZ/9gowblnnfEeLR4Lk0RHArDLAs0OELv8bYqCZkviqp0EDgUbeKD5JJm4OBwaxZ3SPIKARKfWHfQbBp668cIueBBTXdi9O6Qs19R0f4KmNVjFMWHcrOdX1d8YTwosOCuX6RxfQWR0rrbzo2/JdVNvkIq8i6gMxm6UQu1dAScF2l83wa5m+QV4kagdqZVOnI4RndtWS8WZaCggViUM7EQaSaG0YNTgykQSMMCVYWsXHqg0OoKEu4lsFr1Y5lh2Fq/8BixdDZSBf4O8nYiwrkaKie2HBYXyWGHWcglRmw2CLQSAoMykRJ3w5dxZwzJgAVGsU2t0/cHO3aAjdZ+OYPvY4iHrCvts8X6cK11n1ygvvW1r462FHwEskRvmY4HWZp7xa/qTfdxFQhGQhL+N4re9HZS3nueDEz1G1L5YCXoi9Thggf4JzjmRqJVf1jEacdRTtaeJ1/cMwi8R2xFjQRRDLZD+cfBc6mLt6QfladWm8zMNdZsQUpxoIGkINoIQ7Auj1D80O9iQYzJGc/y9EldmI4RCfnDI4Sl4ktQLXcc+EVxMX+hf99ziCMUx8fNwdROX5lOu/ab08tKfHTjG0OXqpCp+QT9Uu6ZKWSJWjB9BOG1E7KbB5zKeLLX0RnDK1IQy2diYd3/E1OHDW/3UUSKnWBfkc+wcXp37dZhirxkd/lFfEj0+KPhazg1pUCheOHL5hRpzSX6/qBynt4Q1PUtw+VQhnKQuN+JAP5Diglq2B3PXtefmZrHhnDp5399w7AtV8dUaZ7iSilR+OMjvZZKPPuosamMvKyl+8MHw1Xpl3+agzFMhC6RK3pm3msTvJkmK6xBnTsg1823y4W9b8N1XV6ZdX8u480b60XyR57cHVaiGYpcj26FX2fiyqluXAkkEOT68DZFB/CzUv5y6qnMx111ax8Td5zTolnWHMOU8bsWnNElEyVUabw8pwyKZuroCcDqSIj0xM9gMoQkPiOIMnC1YMVMffX8/v6sZXAq/VNQZX77/sqVOwDZZ8v2NOrxSGyr1g7K8lakEZXNhGwHsrp9rmUOWtcReu3TqmsTHh189iin8X6QRQUcUHVSi8YUcMbJHFXVbyIt9ym7tcGfWR8eai2i65l6BKbDhU/zWd/GW+ppBZiEbNLK/yNedz/mTCzvEEplGH9hNDwqoIBT2BmFKybga4BLEhV63IOVIX4sbaL7/87jBnrsaHSgbJQ2outWRJmGdZuFQbvfLsLNiMW1nvzf75j2SHeNGyYcXcxqs18YWmtMiOlIcJMmM46MbYzVpm79J1GnQsCg8HJ2Rba0g8BMXBvMcxSRv3uwR0YqbNhHl+RLRIhTjuPwsISEoNWicgcodhi8C7ulBywfXA/ASVxKmhmPIC812GmFLc/boNN/axx26b1YW2eMcqXl83sU9wdlMkecDxuHO8Od7mt5bvY8TJMr6gD0FEBlV0s1BV4fDJ3sDR7F1IaFrPQ609RhGAEC/o1vKx7pulmajs2vCmWF1yk2sb5VHmeI3h/60GDIH25O4eZRjWP7mX2L3nEUqS0ZozCHBxs92FhAkExuJq20hiBdG+cDneNFV7KnRST4+CJzHN8OB3tPd/RPt2tSkcYIup/2MYi1FsRVlJfr8mgg1FBoOodixi1Jeu2AcPJJMWP4yRXoOSxJDbQrR6z4/qDIr7qK7KO+tAE8+afMfEJ4Lh2+5WnudfnQJdrdVy6GHBr0toRmxpeWgvZ3WV0+BhHnsVObHelg3eNfKn7V7HsEBNpwYvMkaAhluDbcK8QsSl0evpFDKqaNlMGVDu+RujoNSJglBp93Y5KbfF8wdIix91sfMTv/J4RqVH0RzeOWjtX1EfOCnOpwdDLjZ6CaFn4PAMdkeBiKigy7st/6P+3CbTYBYmdjO9U9L54jK1Pex5yKiW44ahyVAnotBmN2VLFgtZ1F1sFsCQy3MmFyjGqA9986uXJTEn9ECmgCT9oXV74fIYP0f89bBfp6T3xgrcd4UyRT5E6ctS7Cy1F6XpZXWuXxIGnYnk5baOQWQ1hi5vCLTWai/OPptLs4SWN7GJ8UFmv/vEElcwSveE5mknbC7ZYeVTgNh21JHjDBrzp+57KmwK/JlsowLn+ir37oWW8at7mpbLL311KEXmmoC14MH+Uo0EEZTPu/OY5CB7sASUmY3giImwj0doHMNZypK+AcmCBZnPzVjA5qK1P7xupw9A5ReS5FMe0PyYC4N8TaUIGwSoz04d5o7BUPe2puW+rnNX5O8Zu1Db7qFWHiLzOzW3ZiY3P1y2qw/VtdTHFq0kxLaAdJ0OJrUAymzQbGEdoDX1F6vtn11+KdUKkxPwkcHOEVkkdDtJjrAC+gP9LhkNGjooZdQGIbS7TDMHirDGSsOX+pj+qQMLXprXlsWdRb/odEudcWsuTMJz2XBSPw+NzjKpHboMJ/Ghnl9Wv1H+XeOTSZZuJBoGr7otzjm7GqN+A3zKAMl1grRIyivRLMmF81bB3scfuVbfcICK+Ak3CuahtDfAouiWgT/Nq0fshXQOW/4m+A71kxflFzcTQCBz6+J59EMDlRZGN2ExjXdlQzU8smxx0V62ifa0HAhQ7Gq87EelHegGtscwLeTzx3SU9etWRA7znjy+0fEV6M8V3SJRSLQ2tBQSbMTgS6rCytceq6ZmEuW/M0z2B3d9rT4GMwcJi3sk3FxH5Q3cRYtZtvYXzZKlGNI24GWrVfFlJU824rWhrqhi/S5pHW3r14pLhZS2Bk/YbLOoT7w45AjLhlVYuAg8vclU75ptq+TNdft1xXorlc+DbTtRMT2zYJAnvVYnlwjwxXfi1qLxu3ZyFtVI5xr4D/u1PA3fFmUn9rddKDeHJ+mRoaEwMbCi0J1yuVlMw6BqETQHYr/Itudtvk809FvLJlFY4rzPYnOj1fZE9RxmiVAbDk+9+mVUoCagXWV793m0dsIbxKjKHxWbgcylH0oR/Q7dX+Q+jBuPA90HRYFj+U7uxSRvAoPBbXVckyOreCu/KRrEyHCXzjbI1NY6TIBC/68EwwropDg9Z1w8yiBJWX984aWPvImTrJ0gF28Ug81ZH70tZUcbtjkGbAy+ksiHkNZxYQQ2SQ6qK/Flxf5oLfbZl2jnRRKvbeibgUFGyKAXC7MYcI1kAHVJzfARqII1kKuNcOb+ef7EOyiDjI7ILQlKChIGwquL5gsT8zhMnophUaxrJVvxu/GATIfta0P+MbSJhAsIFOs3GrJQrIewVhFTZzJWNcDcYvsjOD8xYqV3YpH2nvrgmdv8A9jzX7QvsZnfGthD/fLE7vfKYS5ZUcyeRzXnF4v0ILudTWkhiPJRHb7QNX0R+UIXw/aX+jLgUwaEQPLyqz0lOfaJNYdgUN2R+LD+O57Iu8/xGZ+1GME+RZlm8Jg4212/y12MbsbzVUldmUghtWGdS92C7jQsJPWgRbkSaampUFuXhpJ5VCXG+HeI3LQv3LxvFjrWxU1fKwXdHM55YeIMmGnpAJNH8vBhcdUDeaiWo8525Yr5MipA1QsjEdVa28iO/l5XzoZjB6bmXmxuuc7DwM4jSZehaGjYv5agJvYtDh/ZH69oxVfvwf+4OrcHORxPzgJn9PloiwfeScJVORwevXUpvT7H0RigxD5jghxHnbfZt8ru1NNZRyA5U/YpIiuMreItEtYLgcuhiHMOWMIbA+mekaiGw0eVimpJeMI9iX7zOvoNKDwXGtesZFVucVI3o162u9DBafTQt/99ftxn9gdxUA63RnPiCVTlrO5EexQxwVJpeYu1DWWnB11owuqfFftGV6xtHruEnjQE4uvt7y1k5YGP0WKr5RaRsvqkMZNgmVcP693cg+HM/enQxaRyFdEf6UirInY++O3y/gPSJuPdZpnHzJ8WX8IWQOSItgIS+BvfFPD5qa/cwEOHNvmT/7UPUOZ2S/wqJamW2HzMCGeQDS3sNXHLBgcTgLyLMZG4ePh/bwamZ6Uis7VPy2L4ChbW97R048i3Gz4Rs6odzqXDN/Pm8aV19C45NPU9/IKoFZgwkewtpefH+anAxzIziLf6KuoctvaadpkiARBDoqwZMbsuHzTCtAIXiaQGgaovHZSLFw5eCLKdMQq+dbzLbj1QERA+PjCq3sutKBu3hkJYVU1yiQZkxx8arA1Yz6ineUPrkT/hBX6Npq1lqjR/InK/meZ6uhjfLQtQr5CMsElIvcn+pyt3nlBExteVR8RABU0R3Jl0w7w6+oWb3qhpCttS97Kt6IEVWJwM8KIL6bLO6lWg9S8WEbamPMyojz5gPJmmPKdkhK/XbMZbKmiBifPPrKBMT3aQG4vH0fEZZWG0pAeN2kReDvpAv0LSwK8jeZUEZ9yqkJbXnyIh2XAgh9mLm9Ex0J2J2kKY5zlkfakj5fS6jNUNNzVM05E0s+gzvnb9Bx/1VCsgbscmqJXAzsfPc6yElrnhSOyah0xowZTA2V0nDN59r92HviQU4b4OsuRnziq0NyC8BG65dZ3z8cQ92zl3tHh2PL6FrS9Bqmuc1qQptHufwc43srkHfDiGUvCA/CqC74cpNeuJPlIhA0BPYahVkDKuwxo2qhUry4Ymoy1u9bloTTAwkZoKMzP9q7KM5dWqILZ14eu8RsCjX1HhfFHzvYjMAWxnsFY0MuVD1c4qCK6yq4YHJTM0KlFJ7Mq4AChrIvO4r2RDpcbJWRR53c/RQIOzNAfJKjsBR0FdDLShMTPGsz8L961OzL4mv4PR4fi+OWDWWBiEUKDssYrY26AQjxI6W8dIi7BrXLOib+7AxJbPc0tEFo5nroNJm3JpZgUerWP5D5Z80b+rCOenRcqGc73FlwbTRqjeB7Kjp4mG1jtdVvMyeG+AxINJZFyCs2XncBfbqJ4qp1nQlDkT5RsZDQPDstkpDcGqTJ+3VesqNTAxB8YTGCFd3ZgYrNWd/AlInj2gdcRvWvnjX5tDmXPnslTFHlqweEIXIerCNiWU08dlASkK186MOOBaEKpS2RhfqrLoWaThIYI+w6VL7ecNNmhWq3V2KxxCHSwbXeQuX1+SSZfDwmkBjmTFwN+HRGRZeFKMc6FxTh5bKL8ogucjHFPXtvB8Cf7BioySFwX3bjKJR7Q2d6i5Nlal7Mmg5QFEXUGlyjJPyIpQcOu4xl/w7mbgoGptC4UDo463ZATH4NI+RDQ/Gu95sOnTnjhmj+CnW1HEqVclY0IF+9/0uZMY0bGn/bOpafq/M50oeU291f1Cv8PBG8WQTvDY81MfCtQvCyqut2zXteb1R1P2iTgQM2C52cPwhfgPdVFOUNkFeVbHraCaCk9jUxz2MYj2VRfkpqByTxHeJ5Q40RBk3BDpq1Mxq8yJk7/VS7ya1kvpTLSAcUbH4e0SpusTNTic4pM1AoS55pwuqkXw/DKMnGxW/MiS0X2Xklkaltp52VBnTG3P5s3lCi/h6VvKfZwCMtqan7orP3snRRzQzXd3OaEfKMNY8jdpg+0csXHARWJIno6bJptJjPLogSHmJhCB9qrhLp2HEHpRI5jH/hAoc28auHKcp7YV8+rtif6ys71l+nArr9uXd5nOJ3rXqFVsyvtJQeBsQU0ccn/LD3biTQ62AAF+7ePMy15KP5Ob6vcT+ZB10ytjrCLba/AQ+f9M3RvKk0ykCWc84htJavVgHn1ucpQ0Pa6BPfrqZH+6h7zCg0+Mf99OYgetndWUke7lkAqNVg4RJWT6BUJXP1hjdd5Dwj+q12MKdavwMNjRUIqGXI90JX+2KfaLBJy8qi0mWRs4gwVCRo++RX92BaCbX2LugKa+l+lsZg8i6mvvhgejzvqjP2szV7iPo4m4j7DLFJGbtPInLZhniv0n3V6W3bOnKTfOS3CM7BKSjzyF5xPscXR7PBSIWLtZL2v2phuCxz5GjfcQGfaijgywZsBhaLYDT0V30dr1Eq2tTT45kM3o+3Fwh6wLMvREmUxc15KQ0XLm7iHAmkwgjocooVBq5Iq3zOjoMLdgcJTkx1pBV/BYLCJSvYnKN7RGAtd/UDNUx+YJ+8tFOYO+/N92dbVR5k93ph0SZFSrhLUctd8cxAjaxqSQV8hvm7mootwQynFLkNAh61s/2dvPr8KGPPT7NcBfuz64oeQ8wUVObJn8olQU82NCzc9Tkd1prMXtE9lD9RfPJlKYSZZxzsi6zC1aiwVoLXQGjnMI63Uq2cxDN0ApOmsU6sZym1T86MQJsSwwgLWK5jyS60/bM0xhjP6zs/tx+5N5jaGnf0wGp4UaG6Qw7NCTHteZx6JREvi1MZwfr3q+kUhFWXiFWsPLzmPwRIonL1AgCrywOY2kEA91BrRiKXrzsPdyNJOQCtt+t8jFUJ2F6U7H2c4CzMYmeGibWo20cnAJL7Ub3RAGY2vlw7yz1cUBisPTyz1zhiOJfJxPeJKpM6tFtIYxi8HoyP97A19Trz4G5CLGYnxMAzweGvBWf5WKgzgkzT0BAK1fSCM1sHCZveasbzgi4ZYjk3qBSAZlcGh9q9IwG0rAROCd0fB0hLfxhEEND9gm9liX4Re8QzqTffgdIRAGuW8krTqvaH+kC4hlm/+Uwr0F9QARBjBnCQuDhVCcRuD2HwAJtonnPq30R/OIY4yqlPEA36+/BK7x8+VHcq54ZoblOMC8S8G9c3/oeT4JFl5SmiuXyoD6sbprKjX58UWY0/Erm1B+SMahxT/iyWrensEYO1QuKpFioKB3k2lW0W6rf9JWrT7E76bWW5W22lGNZdMpWw4JdZydsgDfPaDMbFzEswHeZn9v5fAA//lVeFeu5r7W+ymrUG6TLfd4mjyLpDcl1j2JS9gWJLpR6jl7Ff4iT6GTifNGY0QE/1w2RFcXOQF4CN1JISFASr6Tp1WxW61Z5OGSFtkR3WoRcC4pR36Hnx3cAl22aGp+xHmImKzJl6HQ7AUoYH+EYmInQHZ6zLvN+EXKDDU5CIk5Hjfo466g4tb/CotP/OQMmxfhcSlCqxNr+PCdP0Uamzaxxi8dZ2EoB2rIz1TJAgs8boiBhk4BSfb75XrZRZJY2r9rUdqv+6S105gDdkg0cdlgBcLg7qYvhxsm3sUuIpa3B4RKjT61la6lL8Ec1js6cHBlszpVDY3r2DLhURD2kHjczx3g/e8pJ3Pv5WynSIfoXXVVmwxCl6wZx+NB8P/ndpcFSdNBDFU3JQ8rPR2nuHTG09KJQOVDGmXLe7JJnANREMXvBJUTA7VE3avejk91fYVudPzUwLSPz+qg9PkS7yimNV1sCmOnFSTixRM0RVYfaWKHUn7aW876lkpnex4EkDGLj1AJnTOR4OXOkkNoAg2owj17lpN5yb3K3UnDwMyydcMZagK5spjCmbJVcg9XBSKq4wwgYi9NEXjXltNV71d/avJma0Y0JYQNaxB30dqCGTt/XNfqdqrdNBXy/UgK1DHqPg07yaXiXNR+mYeB86N8HQ7fdcC9jkeewp5mUWmuuPVcSd6hhizSqdbwhEhCdKmWfU4oVY4hKpmzIErot4xkKt4SQ4N4r/qthfqHMOf4+kG4KpQ5ZbZFaVmc6YwEyZzYKjXxlq0ueOAWfTs7YDxMOMbZNyfwBiH4oo4cX8d+GF7J3pgh/sswuGx3Z5/W4+4vqsH4yzQg3GpcWGfI0eOjMAe4arn9Dbf8S4Zk3qjfzADpb11sCwZOjF9cJ+CefMUh3RrBHO/pdig/9kz8P/Oxp3iCAOK3Fmq1gAZ9tETWqDQxjTzBsxQhaI8qF1AJ07bAVUcYMzUg1XrjWH4LMdSMwNpKTPftP1hn/MBOvCj7IWW5hx7C/g/DCMP3KLaF/3y/Hp8qKo6azg+taPy8u+YVofKbz5ReXdU1JajvoeGdlnZsijuSIMv10jS2BgXsSJpy5Fe46n2Bvg+O+0xmjFfb+ziEP3DLCncgZoXY/uNwVqJ3A+Ysx4rbyOn+07xAwDDTGS+ZjShJ99rv4TeE8Kx3PMIZuGodmJo4j+7hrxt6FimzJHySRsnbLhxw2uece1/zxWKR/5Wx1IO1F0V12nfKlPf8BiTEcuHswhQYMfzuBBlZNosGAuydGA3ATOhAoj/j/L177/U5JzwDuGeUOaoD9v+bcCIKRdiL+ej0tuNuIGnpucJjs5Pa5gW+BwHUnPtCsu1ofTHjzT6UWxrHy2gZiDO4wtfP9wFRVxTlDBF2ZPEEu1CkArx5Pst8ON3nVH5xycPusSdp/9O4JuT1kvmJWc63VLCfgtGNzwF432ZjTEludp3QnviIC9SsLd7psCRaV5Ap/y9gYdrYf8HsAgwxpwi35kjiZELdOackwf3MCGfwHAnv5DqhJBjfodTIyTdouuo7/sceip7GI1c8BV6LqEWQGQ7/FYpujPlACbmq2MnGgXuomz1sib5WpvSzHKusQ/gIQSHDpbgCs5aa0FqcCliPZzP5R68UuEs8Y7IHIotLrRkFdhRGchZc7C7kBY7ngTIQT/9cBWXcl+F1RzdXBwuoylq3Yre5vMOvNClBUyMmTV6fVB3HXhQ2eM5fuex2x1hANrfw5ljDcDmm3R50Ajw+kfsPo0mMupwCfpxCdgzNslzb2wEE/ZZDDwJMurGNQEDUZMQtap1kV9iEen2N760GyoUS2sQ5ZgGwH4ZWo2PpW8Qu52kQ3Mue6z54DwtfsUawQjIg3VnmH7GXVoACMAG7+pNzFrG71z+4nEx6j6cZPa67FqfqMe/3CVdWskao+PuAd2uyMDMCDm/ygyKH3YRQnqLRSV1ITCiaNNly+Q6Gre0qSLm33XXHInsgZCmaBdsXxw6mkfhhalKm657kF1KwhZ/rBDsrF70bBhz+yyOe4rHpjkX04UpvYv8vTJtdmtrss66fes2hqOiAOUufNHgR/r+HmxpN0Xmq70kLK21jPwjM2iSWS/U3raysVsWCyIBrUEW/XGnnWSQYbgsxKnph2jnQaz3aeTUQnAwtZCag65LMeNrpJroySoFl6Jr/k5IT6ZWgbhbq38s1el7qIKPaBjdBHxuJleBILbFXQiFi4lpFE1DZmx8hYiNTfhy9nDmZZPhVFeKvCq2ArQiqCfKryMAv4z7EfCTD6UzU5659Ei6X6A5RAwZqTBV7snqohMgHU1NJ739LVP/LjP/iPUs5VigG50Q72ypYVFhyM1wzPyhACNVfM2saKlE0IkSF/3Zy8Bzn8wGG1y+rCeVdXEcK3IgPEhA9E+e44ZJQDrS/6OIemimXnQdZh4vxJHuHM9zIVJc6vMoh6A/VW0w3VzXYp5cDh5dfjcIx0wxbGLzVn/J15X41rSrfHw8MJ4q381wbxA+XgUne9Tqvw9tNivRXxjt8tFUk0SpaLf9RWAnhiPf7sSkAWjeGhpqFmWRfViio+AsGRLzpi3Bds1nUae66/U0uOy6XOtDCHgBKk9FtaA0Y14Mt4L9j/QrbT/MJxK8rDxRkbYxvOrAkWUbDj+ZK+/HMO0BXZHuUmLa9/5I0qm9Wlx82jV00mqX1mRYOSxQ+jeQhbBWOul99pcD6CZYp421Sp/ySlJVU5p1MUCcvXdpwtH1zKeApR3xRoG072jJA4sM58l1VZBT0Ac46nKd6N27QrXvgImkf1eF1D/6V/Zo3G3Fx5cmk2AHjffpyfrJcm3Z/s2v4YtoEuA/AdqxfYt5ivubnGfRZr8kxoxaTTlgvIHOlOBijnbXjbbwQJCX0jCoDqXap1Gjdd54tL33g0IWvT8R3rww23DWDnDrIqdTgKS8AbVv3+/5UBXl35h/El3CWMPsmWG69TH29WNtaUTcBuH24a+JslrlPTY9ofYpzQeJWIWrD4Kc5xSRRBFtzcmYXqxlrKEvE6kVKWCdi2Qv5nSd9EK5RROPW9ZpIyNdiqJYRSSP8DO2sfyrE/EXHZASpYM7tdDeEdkbnWYVPxTitxhQ559DW+VdZ/9E6r7aLzpNyAcRP79fxEwKBfY7xAzqdZ6zJ0FwpjYS0zg+3n0RfhsGdGMy1qguHDMHhezS9uImp+aUii5LXmEJF+b+kGWcudR6PjxTH+hphhSOtTNXrSq7GtXwLfZEZDttJCiP/7s55au5ujN3wwg+2WBoyRXcKJSDJKfUmTTD7hhmk5m8g8NK/G621bgSt8nh/bE814bCeSIgAeBbV5FAVYL4QViK7r56Tx5AVGtt8VyNz/jv7bA2aSCAcVbt0+q3/XJHXLhf9d42wOnfIInIaCvf6O4KZqVR/SAPBX3a0bakv6nQBpG5+8rlfyFAhHaN+m0fiMn+UTjeYJRKsia4R2ROOreTggB1qC7gvKjC8DHbyEoK8MJbbXoGk3ghga+P9G7MTpii0dUarXXy6xTxRhVjT83d31TaMVh8Zd2f3/PeFlGt71N08qM6YZKaWXuNq4+RS0bMDeTQR99ByvrDXAFtJYu/TVW25cjKniniuC328J5H7/Q0atPMjVclG2NWT+VAWZUbJlWdkKdtMrhM+TRS23OUihT1UOmUS1BAW1wb3JoSlhZl/9nzvShcMOcXooyaD2WVAK0LCs8tKuyBFYqdtOm9r9ftGwDzoiO9qDCpeVw9plCmgutq/R9ikKiXxZtmlSfc6mGOVaiOX/g+exs5xwby2x7Xt4D+LUVDt2EG7J8ZmPTp9lR1mTGb4byM4RKUINItvqoSUyjDgmGYF7KSMNzJy3C01a0Qu0FHrjeJ3MvBBM74+/JFYJcf0HbuwFKRIu8IiA4iiEkLwcw6ZtB/80p2CUdg6F3MPsjMHxCYHG0f1w//2yT5BqO5c13PX6P42eY7D5JBFTtoyczgNIwZAOb7XdppFIMVE8G0iI5EkZWXFRJ+dqD+4poxrWJxeO1xFkQbkJ7clGlYoepyEjv7kMEh5NmSluWYwbRP+mlbs0EZMcKhTx4G/UZ1TxgqX6KjGlHzfoVUf8HJX+cpjNfy7mspuTHggD4kmcyh+yOjSA31bbW7xjz9vN3N/prV9Jw1U1foOSlmxmCB6NgkdE321OYJ8Pd4OpwUwYavX8hiflxh3Jca3zQORqPRIK7tl4IQUhGmyoJZqab5O+tFCgXHbRLU/uzNjuuLv21zwmL9yrfQDyq+o5S/Qw5GHZMUbBAIQvilKqUAGZTUwSB6wWsr9RfaMgq2teC/tAnZX/8UMCfdz6iJ0SXfG8GUOEaIbTXTjp+kmR169nRZq52M/54BTwrQ8EFrijktjuP6qjhV+uZyDd+nkQ+dmeYfMYmPAIYEAg6ZzV8+kC22dU4qhi06FSyGzzgaZhzMd2o+7vtBeO7xWQ5mWfUXnd2eBsquDYepCQISE8MURzxzWOGyKQBi+5A8HkWSGxHlBrd13Bn7n0hsB+OFym5FXsT5FEndExf5dkmvjXzodvNer3u8j2lo4bXCBrDWLbrZXtVlqFrxdael10PAJzxEe8y/t6jXXzXK7XVZBwjgjcs/hvTO4ouR8B4CFbkov0iHsQpIECppi3iLQF4b0uotrXOzk1TXSFQCQxveyJOBSp4o6sSDFvNIH5YlKugGfosGIdoUdOzwUhelqClVKq2h5uP/96sNjffIq2E07cECSTelc+dpsNu3EpKf0djb2v4qYdzqp6IGw1TWF4Wrn1O3SvBHYz9n9LnSr8wSEBw0iRsG2jPYsckANH1nKx+NjvCWsO9AqeSLt9sSvQlXHyWmBNetvgbHTAZhcbH60O6EbM1wjTv+0ZuwfnBkoX3RawmQa9y+UN/6Rm3UXA0+b9yz1JPYm+dMKO7V61aH3YNcIb8ZmINkj8ZN91okPUsGboPWcozwoHiPNkft4bv02ddHLuozPfApWz0e95GPo1FhnEsA56UTHGvTLvIis/0XR5m8PxFo/RaR8P/8WDezGeV/a2mAD5CLuLCTKHJzty2/b3LlCwRV7EJwAPiTiFy/9SUkUaW5AqrIlmRgBR9sAwwTpsENWPIMr5I0K0LJVdsl92fzPQYzCYzaq5PdDj4X52ZfhWrVxlsgeMklM9gfTn918ZuMmKuOrfSEsCi0400kLPqZYhsYNfJpuIa1soy2DTn/KWJSwFxdYUytR8MzsTv1nLiCaLuftCanq8x/S59TcgQw1lwFzxI7ohHNxLgKfW1ifWLoWdlSx2NiCYDefFy88vYyAs6t/AYZGl9KkudtZWO3VNbV9UHI1HdwugyhxgH9XCWOBDu/hTAUgYmrjHGVhmX+ZCBCPQAvZfzFBDzsRqOPk+uglYZOTB6DLbnZ3+tGrjDz31ENX3Y5ewvxiR8zilVLCrj1ZPwvHZsLUAWuitOkKYX+GXLT2WdSZpZTe24bBj6iVIhrw3agTau3Ilw2bZRO79lnZRHExYFHL6azy9SoHtBy1RyoKBV8Mb5Qq1Clw1ruQlL7qeMFP9F7DheqIxLKH8CQUdkFNzCgufp2l2ztRWO42/owfbnZ6hsGB+xLfopuuqesWVAUpB4DLtR3cSN2rxamjKLc9TgCjdvNxZsJIKP/eX2jP8FQQLFTFU2IifKg6JVlWNvmC0hpTEzsSnnfo9CS5A5N2dWNFNhPeVPGaOUms99TNhufbdOf2SIkF3iu951v5bNWyrk0JiXAggopi8rDnUgqr6S4TYnveu5XvIq08OSjCnhcab7ptFCOH927bjdB4bqX9LhNGvg9bowWA9aCqAf93WgdDSW9+tAeWLxalyV9BY/vTN3Y3HSbgiwEj/bK7cTmqW15MAd5WapvrCLe79Tw+DFMcguAOSdVW7KikHBe/rQGoU1WyhDGBEJGrG+S5cpZw7diG0uE4cLBrZGQVuGT6BR44Cajf8exjhZ7URfW9aAS3T780oIr2DFzO4nqBRSC/Im/9oRip3r/5ubh8W+5PuC2Q9GIRG3adZGBaTEl/rJYXfVe/Iwifd82xSNrstYRapelKMmkwFhAu4Zbpe3h81POaohoQU/XxYPlOhngegJl06jqzzqCwVr8aDc7vRv7WDqe+6jF+iCzl/ncsJwAWzATvmra3/C5gNi3NQgdJTsKZgW7tWNoHogcG3W22buznIuc6OD5eyaq+zqH+vGajWrDLrqQmIWvkLnbQ3jNFyKX1GMuj4I/o3guZcP6x/eCbUMrZPxOGBtYnkt+45K60s4fSr45XRhmz0rD2QzXMrVpLC3UmGiiw95RldZSvkK2N6Tcqkov7hJUnXgQLU7E39evOnKVVFUH1loKUr4swn+u3WwlRI9aOg/IGjbggVwIuDZc8OCZ1Zeiz59ZL9sO6Ax3400Zxo8kCcqASblD0+cLKg7OVCLaIuvmPA3hbeGK8BmURkFrAXoP0W3OkvR8fIcP/nM9Xv+qH0HiWhR91SyBtBtHQtUpbtHd2MORh6zV33YFf9x9ZSCQmex9TJiLwRmavrv1Axh8AnZD0ugsXaYRPfHpZN9Zr4aplzLG3sSzK8iffonSfXQSHkf+jU4qhsHDLPHbdDd8wGeCc6aPCuaBAxx5lM3MDzcfpIA6GVx8gLAJvsveU07EZilUoxzAdenN1sp9PAhhZj47gY0ectIXRqaRQTwcx8K6zHooa6GQfmHe6lMt/o+fgWQL9TfVBBl+Xt35g/vmoTiqlLexIRzPL0qcEmtp5Qa3aRpG5oLK3zMK4lcm7Wjg7Ky41ZUja/qDNDu6AsvDiwqKbbdExqgrDbMDBlHSYbM3N+Klf021GRlNaSlhU/FsrQxrpIhgwwaenpEbYMpJ+1mrjZOWin/rFNpNJyvdvQmDA2TPdDVEV5vYzd6YCyXCofJNGUqtK8UyyYP9B3h2Q4DeaCdyO6T+bnI3cfVu+dI+Q8+2mMolPjppOCcDft+hWhf3lmUYolrJKEIYDYf6M1BWz44M6zZfX5ge0m6SIgLpM7tj+IcofItjjsJDh3B0ztYOLijN8PQOFo3g9FubSlhhQbOx3k2d6QFQ6leYl5wdJMmM+A8pr4K8kbzCiXM5hbxLoyML+hoZu0ImMDg3mLOlVivEbt5t+99vNIl+n8qkNQsIIIOFfo1KvMq2gT09at3C3pLQf3mSJWVXRQ/FSIE0xpgzGA2uSqb7Q5IS8Fq4ZsYVWlU7p2o3yQW+iqFNiFK1+IWntS54vv1y2tEvdMdTl62QLVrtMTe/qDox5v3bM4EKm2Khl6aMXKU7JSn/kLtCLGz3LVBqza8ZR2IufuvxQ8AzcTSn0u74FqA5F1MZERGz4c8+ZkUf5vW5ZkONbRETL/WluOfs89juN6bmE3ouZfMMWS9V1aEBlxZykm0lrftT9zcE68kmuTbdTRH5KnSKn9luR+TlvMexx9GoZ9JMpxq8i2QgDcsVMMIsXL0VYO7npL+DcvnWdKfdGLQ8+tOYdapGXhF1RyU6Eakz7jzuPAwe5GI88T2LNqm1Kz4kH+NWPTY+bkJSduyYKYwkSlnKF0Q/XbFCKTC5i0ON/YRuy5uZYmc9bNmcPxHlmEH8iChi4EU9AtRRM0VFhWFdlMfcVunxqIus4bOA30Qbnv+TvMmQjj6ZwQzDzbRDw7ffASszwoTZntAGh6tOBA2tCSHAH962CxIPEObVhnBMKKMfkNn7ZeOSme3N/3qXMoGWfQzZqoauQ3HX1Ml3Q+D4qMDtqSTV8IVIvD0iwf9TrB0oSoyAQrBfoDie/4yRJTUoypXd5jJpi6pnfUHM6YppfpbWV5c3gviNnGySxD3OdQLaA1q9xoHOM1bhMaqKZNHTDyDCgZXei7DNEh/7g6VpE0kwGWpubccdBXpO7YA3d7Frr4xsuVSNtnpOn+qnmAWOJ/5a4xXMQ1fvLG/sq4gAT75E/p65ncIaDk/OiwO75NFt0Vy7JF5JOG70RUb8xwYuOYI/KKAZ2ascFvlrJmO4LImdj/5JySIaur02gVv0N1hKqHYSWdKZdPJoy4Dn2EeoYcB1rArwV2/TZzl6+0KBGmXmrEDaRD6gBC61qDDLpLs9uui2f4XhVnzbOwnNeTbAIlEd9JSZ3dF9hOMSDHi+YpbPu++N9NSXxwl4YbeNf0gnhXTiukjnlqDpWf6BCcrTkO7+XfcexWRNx1disgnAVREAOPfksN33DQJCWXPHFwqmaf49tEATJyBcIX1j9erKDDizus0fHGZwNi39Ej/HEG/zIHtuZQGKX7u3hZShVINuTVfQlzK0+D0yLshzDkitl4biXj631UxJz+V2wJkTnz/aY+LW8WYk9mAXwOBN62BS4eAk9yifwkJcV/2dVFFIEGdo2xCu6BfdPEw7NQy+QpFbXF03x5ox2eNvMfJYmcbC73wuPhvo0xPUsDda5GdXCDfC/dz3IHcKmyNWJ6mVUK1ZzNmgAYQX8hE41E4T0j99h6pvmFAyTizAkmAm7zXsh9Am/YZqRLrZyxao81p87i8XXCDJjMxQzbvvOGKN1Bb/OMaYI5MuX17mzVg+ttxiPUmtp5GOayYZ/u0pXcFBEBSLUQjj7uUI4SxvHL5kHDUDAPFRKUXbTISA0xexhowNl8zXLY2TzpWxcU7yyftcGJLDWivGUdgrLVsx9GN2+q576kERMtuGVHuPmPB/4WxUlVr5HTVsUP6e9OFzfP47XjxCX/UNOf+ivDwziYmQu+n03NcOG4SPio6RQX5DRq3SmQPs0Y92SJmUSojs/nzTuX1DUFQulwPyNNtZvOfNktVshXH94/etXpi/8kpsehfGnWMK2mzMuee0KC1CEyFDCv2f+d8QLMbnNxJ5bkj8gFfJi1W75Yto4xR6s2j/bnZltDbGpqAiRWMnClMvDHxFFhmwNklKN9X8ooBVG4ZgQi7MYszFvWoRIiIpbh0dt77Cv/FPsUvN8d13ImylKXZU3TwzxNVYYyAS93nqttUg3KdaOOnIQRB0QLgGGp93hV7Ke6PCS3UW1MuQv2v7X/R8Ok+jmxFZMygc9lvyC2G9G1bNZaeSwLZL2jo9WPNZU2KiLXez0jyd1GPDk8iYbf+IM7o794F4obmsAHDP8l6wtK8qXt+gtn+1YmOqvKpyj4HWGKbMNW1shrvaRjrosFGvSmDxJjin+kT02mc3okHTOPOpeEBraeHlepGf2PNyCGJ+WqhBRY/9QM5+24Dhke9ysnSnS3fZUj/ZHkIKaScepCs2VEE5qebL7haYl/ai03rzQFyAsQT5qGEZceWIh+T2XF5OQM2I+P7UN2c8b9t5UZsbR2Oebe61g1L1aayjyz3VNvbfpGz97m5vsjt3FTwCGi/baIz3bPsDwD0fzi7Yd64z/zaJeIWTiiX+w69hTrbtpInhRFm2m8tTpuWhr8njuZTQF+b+cQ0oellViaXgwF9brwmXgqbUH0hBy7IkGJnFdB6r04kZFn2aohvGvXJzRpolGT/EM8396yTH6KPbfIHM0Lok72A+MjxKY7wrHpGCqS/KsnBNetUze1GEGTj4yqSRLjA3HcsyiG8QYaGyY+aWoxVWsI4xlEqW6OPabOwbBGTBSHZEiYYw0Kwe5nt3BZVvii1kJZm5g1Xj1QtHJInyBBlj5P/HFveKSQ2tzIMvBZv2pvLm2e3VA0ZRdDCJIraWxR9xCSNULpHSmhc8FXdyfGAsmms+L4s3YxzLkCjPtFH4GS6eFKDiZpwZYO9WNBFSy6bRycUG+z2tJcrPKo0nMLN4zvSWBR5VlO+qkY06An8l4IWJ0CJr63sXxzzXWLwk+UuLgIdV/2WwDf/AkIHEKtXaSOScgYYApV6Yyr0vNk9e4fJkqBTmlJ4OwStyHk21X3RzuDOguduYC/FsInbp99eoM4gbtCr80byagO8dNn19lDUj4F/96j6A83lNQNd/AqPZSNoQG94oAQYHs6WEfE4voeDh10Rjynvo5/KrF5btOUhFTbxlB59XLUIDUqomlqb6TR8XMrqb9jGkC6cEtHEOG/Tf76kOlCi3lZM3B6YRC3KYGtuIRVg108dOlCdZ2hGcR+kJ1hiY9HGl3pruMYeiV6u7Ny3bMaFe4j9ZSfxIQAhEOStytIvJTxaxxR2kJfVqLDzIxfSBxCGFtGUoBvtKNudcrQdAXbtiF0onFi6SEqMEseLtsTnP0Aj0Vj7z/FvY6ztB1nX8talP3XA2b/zmFGdpo/TkNSTshDoiGU2Tkl2rmhge3axYU7WVGmC/UYITFzn5AYjI7LUPxu5Qf8fLYgiaRwt4Q+HzfluOMbbbeyBm38eaw9cRUrU97l14kP2HYU0uLWVdDs9IL7K7hO345xS2iW7z5RbWFMSJstsOcMXN5XWnms/3RqB/UJ0VNSTqnVCcHdaOkH/GvsmcSKZon8Fj7vPaQVZiAXmQdCgj7CJnogl83PBNGigT45pZ+kyJ2oRtSslbeLK/2wewk70Uyv20LiQFIpmG9epgEBfEC0G4yNdaPIGNx7WSAz0myd3IFaue5t+9D2xZpccxWx4MPHuC4t7s2S9TgbqKdh5zv6BKIUQXYaETaRsCQ8F9vXfolE2N7X44U9xgU/2rpVm6AbdX4s5tDS+w7SbmvyFtCHOCgk49pbC3hXMLqP1gEi+HK5TY7H/EDFB6eNGr0hj5bThP7scVRMO86ve4eNsAhZE2nX66WVY3r8aku/S/B+8e35Pf5rMkTtXCgWaQCsITRHJVDPVvJm1OUX4z4VBl4MyGcM2AMib5ly2Ba44SfaWIIc0Os3RI4WUqoRjh3Y0z4JLbbky3vaF7wRxDwEBtSc1ghQC38bgDArlvs59cISjI5JAaNaP/xefYpnV1jh2jrXTc3DcOz1tN/HNcWhRmsV/DZwQETBPP79H0depXb9hedJAvL5StPZLtbwfMLuSLLFljLVEbtsWQ5VmohfYxKBlvp2uzf768644B0maDgNK2ZKUfjU1P7SwDYyrgjESRq+xo9uXr1CaxLyyvS+P4c9QxA9ZknQzsqIGfQOAFFacHRsmJEDI3lrSHJZTYMnx8EEoYaxhBV3hhNrz/EjbhpoWqmFEbAuL2kb3Kx68/gFx4rKyTeyWqbxFcMvQ1AU+2nkt+mrj1S5mc7F8eKSQKJZXeUgYHgKR9l2U44lqXfm2ebkQZmzvZw6TyM4+aSyaVBqpT6r+W+YQFd4JZqU/2yV+RnxgkRL/YGwEgYnfKNcZTzOWKRnW61gbluFSks8lv4xW9+0uOXOl40d0Uqn+X+SQVKodYPrUrKZbBwSzI1HHEM9pHDPgJ0W0AkAaoZDHxAShDKJSseS6ixIy34yWxm19g6qK+9hULARb2LPxws2ZgB1ezvq0gYz1Gxh1+mKgGikL0uTTTSJT4k4roQZefY1JOAyDyF/pwxjA5mo8XFR2sTs8M35SlNnE3eRfmDrImKVFxi6YDUZj9f/VloUUKIfeaKszYksY6/uEuCeCG6xSudKRKYTyYbTsOJXJXsW5XpraMmZRV9HS0+/2KY5aDGG1uTpshkRbz6GubQFkBEXBY46UArYUxp835QyBrB5gYVXQzQfQp1RLo+yGPWZh2AKrE0baOlVFU5+Okmb5Dq2R7hcoNH5I+7fB53Zct8J4eDTotB3gWexX5CLW7ta1GKyD/a69RDPF3h0avwQvviQnvPZ76bjTBgFAt0bUbJMnPZH+0B3iRARyIlLvyF/DQ4g7X6sPUOz0QXAz/FTH36UE38zSFmBv6LE7MKzqEeAmddHJETUlpNkwrXs77fa6dcdJoetWtNHZMlzVfvgLbV7GcxtocoSrd6euljj2hv6++qpf4UFEIGKTjCN98Ud9LzcX62n/+TeDQaM9TivKAmWdwnc8Jx3rJjpNwoXVwivR0TiiZFSDSaSZjjZvhN31adZojl311LMM4cEVaA6jnpJuscG3Ki6cBQ+zqZlpI/kslEPHPIekDg0UzxiVr2xqmYsWRhtQt0apyX4PcSjWmoyoQaDMOKuQK2UrRxeV/kcLp7B7IBrSOwKKEm63F1Z97XsH/cbijucU5nW9q6GDYKYBUYHL8jFeer5u/4fJrGnCQlL1GANxxNdgJNE3aYrMAL7oCD9zEer+XYltL02QuZGgZ288tJa/qqYDuf6U8rcVhj+0MuPKCML52io3o46pHdTxFFG1rhIEt4sgV/0TqOxgFxBC2J+u7rPjNssG7oFOTnRdhiMPG8Q0TfT53Cx8YFZleHL0Ot+j4qdDizBb6//TpXaO7E3hBt9W9PJB/Fv5c2Ur6EEQL7dapi0bzuDnXFbbbdzmTWrLO9WIhnT5bxl2arjhXaXTEI8NK9eUyDIcKROkHkBVEFoDvZL6uWXf7EZqKHIXGIS0j30TO32RbbJQPDkREHchfBMXnn0H3U0qWxMdoF1RD7kZgor+wYQHBtJb+wEBNxFtDnxobE38FWMANB4qjoyI0mB3WJvElTa1jDWBDKmsAPp45G6SE5WopBZZRdmvTRg1PIEAX3vONwvEQEBFsU8jPvy7nUaIBnnQuk2N0kTNptZfzfL0epsekPtjoBSl/haiJm9fWDSZiPbNGvCnfEUaFudl6SLNZ+yePfJMe5ghLUWK0zx0QyD7HY0HDXTgbCeXGwS58l3WXCeO3Tial52WjuHZ/3yjXEqmSqRQF8kK9+GMYXRpJy87NielQZkJkdbzd4uTLdIGGj++FEDVWfvbHKroo0dF/QuDkNWNup/LmYNmTh21jKmgMmiyEdtwJgubL5KnXsjOIOLBissDExaqKa6Dy/FJarG7tC8xE2CdQI3Kw+vb9I+p2rl4HwXOnHGw09qZfNm3hb+GTajyBpss2hrRKJf6R3vQy1VNrNqgfSxwYJA6mS0HLJm3yOeI1n+jjtAxyGB012+XLzcSPnWPz7FNE2m1BB2P+MXdZNDGQJqEcj0ZU2+egbMcFODXznJ3fNwIL6azjDtgm2ZORxxK7CIM+uAvzTuGJZxNX2jlbkjP6uLwQWZ8FkyGjfYNMe7RQftePEE+OL/FVdN4BqX4F7McljoXkEX2+i6jDyiSwhhbix/+VgbMEgsG9wLYPYIyIQ1jED1ClJrvEyBolBrtThyJlsa3o3vj4k1lOi5z+xU8KKzHoxgosRTJOy+7DsTQ2i+6SmiHcth/yz1oZ3MNELNMaTe5fEjyjQGX+0GN/aOrnMROdSlADVRTR2W9SFwcyMla8UHT6VTZa7nRJCVOB+f+VRf+AuhytH3o6+3lRCoB1BCa2S+qh8aGXrHZ4s52HmKZRO1mriypx3NHFsRS4qkYpwusJBC/ZL8VT25Lki7G8zDzBpJI0/6uHH4bc7SL8Y0o0uDpUf1f8OJcdenc65rehxETOhExsz2vL56PD7SjUYUJU/JshP6XbSDFf6d4Ic8tCUveGJoXG9Tw2Zxbjw8aIyZaxeI0/jZHmt8nCdcYaC+WMAQsM63eX8B+dwJzbCWWPoZHwBZkVLhUZJqdFU5r7Ho3E6vj5uPMHcCSTgLdpp/fvN5sjb2AF/WJJlh/OutiEV75X2+9Fz/cWF15GDC55gIRs65mrFdlMME7a87MKqflZtdPDr+BKmxHgt+R7sgcwwgF38kNMjs1Far29VB3KNrpyN1rhxkusv9MPwRArm8CfsfUdo1Xz6N/iPsMhqCJBgcZwJOEdpTLFUenDr60WHF29CByrpsYgr9jjy51MwTCX3pTPg9LDP7PwRzraauPTvs7EJ1C0H5TjtnFKszlWr3498gNzo1Yi2wUDp1Rpammxwk2Um24kwdN52WFBel0t/Op/JVTgxPpn0Y2Pb0yj5Lryr6338evs/9+xqLsixQA52Fm9UK1EBjf/koDl1wTyHcro/+l1G68iwj7WwBtzuPKTJeRMjWaSccudGEkyuE1yNirktjyg8rxMzHH8CQmV8x4l4ov7CAWYD4fKE8MwIEdJzNv3rrNKXi+TJI/OOQFNxg+3Gz1XYYXcodHjGhlC8ho2HINfo46AXsWozx6F69ffAhARF8lpLQimlD1bTZiYgXTurB3s8vdoNMFWLCli1XxLm3YYdeN5tU6Xn7QQWYGoIo1j6i4+ITkxBtKyIqIztOPt+NuLVA14zTXmBlzv1VZBzNJlbygUP2UJNqZx0djyLZT7W4KCV79d8d8PCb8MCxgkAjXvfRSRMirs2l/wCFgaDP+kfxE1Q9YRyMwlL/EoXoTwU0BrQIuJGD9jdzzAXJpkB9IQthyOluhnkyY5pFvIYJKQJ11C2iGoaH4RSHfSUKVgFMSUYERHfa7V0S8IdN7GTVAOpxownPMgEA79fZvuJ+CVzIvC4L06/fv29Vslx6xRavfp+IlP8DiIytUs5bVnCTt/0ttjnu2DMyRVuXveNRrSaZJVJC1F8oF7LYjV5gt+tyfoDjRQ5Nl6HOozTZGA7kw2V9tamHaG/lYe149h2ED45Tw8jhSrNi556e+55fOp/6m+ovTHClO9jsruBBffAGnsS/WigFQM/gi6oXw5SKG6SXa3pk3JmWqgzFbzKSlpbzJmI+uywrNghaiZez5XxMlNRPDTCBk5rRRGFATVOJIODaE9lue3PTyY4tn79jkM5U0VQ6W6jPCpr3Kaad+tTLS5PAuoD2Q4S16p52wpZbzou6k0GSI4gDauCnjsXnvnXJ4O8fjsgEZRSJUS18qqNQjGuqLWuOsbfKVfeSlFrH6Q5DbOyONrus9+gi9IgKE072SH0La3EkMDDTXrhrd58/1FU9JdRYQSgMqX7uXjcHv/NuCHtSpePc/HPv1zbUoWuhq7jAfSf/LCHxvmNXmu3bXokz/jYAxg3GtzzQ45qaePlvOv1LW8nOR9i8u2aMjetAtgHRGFHb9yPPYBmROGmjR3hnDLmK5U4XBQcFgHlvqG6Whv7i3b7Zqf3LrlM9OWxwIcb9weTynTNq1WaP7m+8AAfYTI8ei+J3EsEGTa9j+hpmpF9REpG9i8/SkgS0tJ7+VJoSwirh8VBLT3KgHdyYVRq+4bZ+IzhrjZQNLjzFiQ4mfJm0pqIgBPdsexgSj4LsIxgdn/4RgB+JxV6sj3ve+iBVe8a4AXCuZ18Xw/XGn5+g3uk3++V0AgPaI+l3OglVLErRZ+gwCHHqxp1PIJXj0Egf1BUfOIN8LV+o5SXgjIrnzmOIes3Z+gnWuTX8K6IpHpspEZ0um7uM9sM6fsgV3fdOiIgiYGxOv24dKvMgdOx8kI8NBpEiiqIlJmOIfSAyc3DUHXZSaXgFp8O3rw4hmpirTHc4q8Q8FZooh545P0pe/Nx6zSQdTr60t7BS+hAylRNluINrj8NKrgUXKpVyYjO5h4PohnjpeiSZEYQESld2ARaAiK1w1jJ8W4UXdGDwest5/FIfnkiyqW3PBCpIr/w+Fdt9bIicgJU2/P4q0q+65T52CUoQrOIRsvhPQ8Jz35MOT/xqJobh7Uj8LIIijcsX/zT5ZQtNChnMauvLGkfr3Q23X0AeIiKGVrgbpWE5vxr6g4SX3i34OWXkpMEMdcCZiqjdoJEdnp6WpZG7wtENsb1Yd8PZFtTe22O9XsdIoXlYkQ963NTnUaOjKh9zLDb3Zij9i4gh0KKRS6KOpH1/ChHBjjslVqkWZ9LW+IhDO3Op8CxJCw2dbt3tCRQDKa1gvlxfwPzeZ/tnLmGNklPpndGOpwUpAJHl8T9cBVArYUcXJtmT/ZIX+exqO4T1wT5QfNkdkoHJmhL+lkqo8SI6gEuuZ9sKbruXlwafCwY1OEEUguwcJKQU44rXwGqHawg/LWUYNQFH82Mz2F6Of1K9nyhB1r2qUeZaYDNqDt0swPvhFf9bhPfvP3ROang9xteak3w3uZVu5ieLSaKBUWsOMdggzqEeWF+K8VnU+NHFeO61s4I+RgS7VykJbiyFdpscZJMlhqgA3TqEuttQjA52nuks4ik9QSXlYe7eiM7G6ZCrbxRI4wKYCGWO7Pn3DjzKNohgaYnr3p1+JZK0fBB8bf0t3g9T6/qzb8NqOjunN3jJTpdHiCDthXGwqUIln7ZfuUeEQwmkaq4mx/v1CGmG3Ipflq9KoghMXEYoN7cSGe0/717N0/KB9nhV8b6ED6a7YjWX8zaleOwLGR8iFzWY5YIZA2fVZywJcwELX0xe6+h88dbwuCLoRbms8fBo96j1h7YsWLDixpaSBNBWK+sYtaujvxzcBK2n8KjWVdjd2Tu9bH/H2kKa/107/C4gTB3d3NvtJ8JdHqDMSbyxpFXkk7xYvMd7NF1b1/FWOywWCUxhhsujjZqbpR6i3qxA1iChh+LV0g+1AjAbH89UX1p1oFdRHIiYQSJ8PwbNV8C/f0eQ185wT8FJeylERn9l0lEsJs4hGvAf5DA2MJxAdyTBrsSV1Y60SD5c9dppDwwAGmRJ9nGpahJMAM65cv4dz0qG/eyvqDUjorUlqbO+l153G5fJsj9qGaRJUyRwlQVI7Wi08AR5xRn2mWz1jS9lFetkiMGCWylU+gEOHcVtzdCiw5DBzKF/Lwm0iHqQQ1uSewhQ5G4WY2HTEw4maQ8M5uxoslBq/8Cg83M2FPx7SzzrT95PZ8mdsFpsHJ+NQ6roXTr4wkzFl8qBdxr2Vk/ush1yxpHs5H8vjsk6kN+9YggU4ZizXNjteGn967cbQ2C5DCFo+Ye+0oegmCKt3L+wofcr0jdUe7ukJz1dlrxug69bymt+nzL5ymWEyT+1Cvjr9+giI3HpeL84dvceSWT+8fwCaCDKtkZ9708b5Uhx+3PMGE5mSb9U8bu9XQMBjG46Vi/L4HOJO2DLCRWp6ul8h0Eu1aajGHYX2w68QJ4eLawU++/SXdRn9kePHZaGAiJwHZ7O6hsEBnLWqUqd5F+Jv9rizLArHowmgrX3qzCIceYIbSILGzFCvvCUB4y/lK5jmi3koOVdhdTu3qiKXHSOvt5bCbVQuXLmj8qxwRbf9tCKmGlkHlPyZzHFHf81+BBrqxo/PvsU/zret18oHy0Se3QXeC4ueGCkwz1wHUF//BuMygnPpgSTTUVG/tHEeHley/sFMLKqhkDknEqg5/PWI1pz20Rz+5R9cyzCG/3rOdvyfh+tC7+GRVeQimSjLm1kfW5RZVpmLvf7Ni+XmYF9E5vitKJ3K9MdK1SYUuMoXCAr/F1FuxF/2gF3vUHaAVYZZCydYv7scDDVv4CCKUI2lyBZmYB0Ge6Y96Bxa3NhjA9fYHONQayl0ld9O/Rmyk+OZ1J4q5nGAhdZwPxRHLWpanfItXJZN+S0/eBbz2v/JlDPfuVKM+WcJH74UlJvnR7hRA94WDo3li2FZWdHHtPQXeuGugX5QFiD7sRONEYzywt7LAqtmOXG7hgiqw5CSjqDtyCmF6wH51rURGu/VwiZYrnAGhfMLMzcqPCsex5uXbZG8QgzseibH9yYtw1DcRQj1kJzynf3qv4vl1AyeIYIsH2xLX9r4vIay2kOJnXZE/J0qGC9vGa/ILHOzTlunLAnhoERHUtrfgTlNXts3jj1rLvzX9vxXE9kSMxkXMjhMBSwXnTridP2Ym3k87G0TLE23EGhYqpVAYYVyl2J9wCHnFhjxNtwTrmDDCL8vIpGQYknMTBeO8ANYomr2Mw/W+o0TbfWX5F5PyNU/L31bUFVuR835snqJK6iaUAEKxrVG5WeJovdQmSdyOlNtI2zerxpC3Jrrvp6R1SdatsOwKyNlkTeof6Ifx62BcmGghAD4OKbXHTRJvPkN0xu0ohyboI0AexW7MKrZNQwR60pJTjrDLRnBAtmTzmcPgjL+2sz+pMLuuKO8s/TO2GF0h/uHy8C/PRuVrDY/19bm1urTwieujFzLFPdUDcVp2IDxF74U7eJNOQj6dR6hO5kAexTuj4vYRcUdjpa7UG+H6oopCqqfy2qGfGAd6HxoxY/BFZZ+xWIb8sa0rjOMMd9KfXdA1MDBmAMADuGodghaucmETbE0LfiOpKRTlfT1d9E+WIhqsSI2R+GFWZ4ZclvbFvBDLQJHt/WpoCS+P8CLQj7WqIkHGPsd5o7r7qoi37Ni16nOK4x5n4Xy5QkNymUb+cIG2miwckX1VsWACkhn/4Bv6PBRvPcyFgZl/Eqtpt3OYgqTbpBmVGh8S3NoOj1/Qp4TaMWfLPzXHVNpB5vMsxvBtxcwa6akqBJk4eDnOdX9xoi3FpXY5vD9rdZRSnHR3u+8HS0UMUkAeerZKDF3ETPtID9WRi2Ww8WNQClFR88/thAKkZfajkyHohGhs+DoLi/i8oOcVYM7+vLgt+bICniqc0nB1ayHenE5FXtvqwqN28xlQ8N6eKTLpIuBq/UpVbTTyqcEq5WEb1vjp7E05imYedix4Rg06Ad7GU4cPh1DHXvc1yC1cEj/qXLsvLDTMyFnXXMyal+Gt5W0ot61OKP4OQMARt/TBwjEjDchaT+5gCkoyl3sdJXRgC6Gzu3DO/YYGMhpiAPTtKo3tZ3lAu3b8fEexJpLvRT8BLIxxPBl4T5nyqHi3s9sNFQHddzIoWy7abd9nfNiL/P8/Z75CqWBobZmejRol6ywmg4x0eO1mQgk6VZiN1677uU2a5uWilC9oljeRU9/rdRr3GzbzjPlvp08uyzxcQl0JT+fVM7x0j1rAk9ybRocKZLEPgzIXo34wJI8eBdlHmqHooVLLWEamrRdFhsIwuN7dNN3Q2l+eLMdbote2541KqFhZijki/ji61JGv4/iuqX2Ve9NIVlPtnPLQvwyeXi0VPnGAM2gZLyV93hQp71GGZxpTN5WZstECG+riYt+xxAT++CcVeEoqtGT1pyr84o0kZoaWklvdhUr7ZsJfUxKB0vUVmmydfxYi5wlewLGFyDE8dPy6P9F2MWpcQUHpyX7bCDo/Ag30TfcDR/rbzwyAmxpcTnf3qZG9e4LNgxH+WxL4SRIl9dlxxXAMNHNBRcx2PuuHwhZxEE41VYh4Kfgmzx9Du4Ra04dFD2reYhw+3O1gvfZOnP17z7B8fBPw6PrbOS1d7ledluseyJAJsH6xDc2H+A3l+/Y8q5DEDffVSWMWf6pFwElBCgD7Gz7TAqpID0ixjSPnloiftCTYA58h4zzXGPA7q9kZfilK+nZgb2J8LBeOXkF9onmjLNY3ITEAfnDnOo6MKvJYuiij2LnFdRb7KIz0QdbncpdZzAIlc+KW82i/Tx4nwilB0Df9Iv94xW/GiWCoZKxOAM2COJISZIEJqVMuxKhK80uqtCDoqEYrrBtDIm87gDK4vt0Y1fdLOsdsPwl9O1NJhgQ+fahcyhVZ6ByA3KQFmKtZQydLZ0ymKB8AIFyaJHW3uqCuD8i3K+Xo8tnyrptfwZVCSZnSPxs67hYN/gP4WXm1QkdyzVbmiZeAchTV4TQatCFHr7UmKiMxPRHpyUGCw71ZoUehcMtoQ9tYx/z4M83yUB4BwYW+DXvQZ2nB7GEFbk5HL6EJmuh+EWTo8rGhV8AaoNIhrfDoMWz4rtP3SpXTOXnuBOysdAliEP516uqlV27KVtsuVgSX/r0jb+9OH2JcuHt++60mTeRESG0mmqoPhzDWPBfwDsZIn9SCtDbDlNbVmrvOIdeAnY8xZRV+bqIvZIDo2Fg/c+uzj/a/IAslvS165ARc29PqYjDeMlG+wmwEzArIRCxmvbnxlSn5joABGs1CDR1DDtu4v7vaedQ/H6DjHopNt61Lk0t/jEQRjAg6Hy/vOlrzYl+jzkIxWUE/3GJqeRvnmM60jZAbNCwe7poS4ZpO5wPGqkbaRfwTtpWCq0uE2A5Jg/ejlLYYN7nuPccZKilEH7IeWB3mxxUCSBEMYSNLrIfCN9hc85ZUUe+lofbR0cHFlznJCnWwHdG4m6feIrPwKvsOylAZyVI6OTV0v6hS3kc4zRNo0nCuHWibTYrkGzo+Ek1LK9jvm4Vk6CmCVsAODHPkWnGKd/SQFqqsqy3hMjXyVoJUTSWN09pIWrPVnjMGLXHq+eb9A3fPUVNJxOw0iYmxAlmJYBbVKQ15qEr3PuVu2eBxphdmMcrTNk/EzscMDSMwz1j1S8hhV03E1Jxot0gGA+Nb667CLrzFuvkIvIQoCiHvB9nxMUKTs6+HuXANBAqOFfSg7dYrdS23W5dsyQlpGOwI5HCN2pXNMQ7kl4YchCgEya0DUZqLkOXF+KDVehzB4WbHmsgg9IERmT9Wp87rnN2UMslRG4BJcCgasIR+39I4kciqXonGAHYTyHCqdTsUs1+si608tWVAZZRyQkw+rL0OWCgF6Dggjp/DLdgLvDqWM2GpCWMyMJplFYMC65Q1LIusKEkwPNBWD9sGM4YfkEtQhs0829Duf5A1H0Jfn53x8ZzGdOJBSRgK/rs4KuYtvGz/7zVvDSf8kmvYjs34nN/6DIn8hghejTYHy1/DZJ/JGW+1fPSYm7Ke2LcJFeUlWHhHMaEGp56bk7Xcd4osJmyg1+ku/tgavAIg3jv49djDdphc8nL2c9y/HkVsaUHEv6//d+m6bf4BFUZPpfefMdyTimRZs6lRMfCt2Lln2IesqfyzgT98F3ksL+/gqaKmeV5YQgsS2Ti+YQWZaGxKrBnWK7YNR5uMkQF5Gy/9pIvQ4nMT+XxdAjdHEiu9daztdUnX5sCb+QKPSpNYA/1T1hqtf0PsKHxH9iHkuCF+a01UkEytHjctXlKBhCTFW8EABhbdp+MxWZ7K6S3MbDnX1YeewnotY+WyCrLa8e0RpklpfYlXHxSxZcsKYoy1jTXFOq/XMmBHK2NNgeoC0P6VhRMZJVlEGYHeXGW/a16Hweth6wXsAfP22+J8JzlvcT8g52ptumuZuR6QfGYj1wxDAPNQtJcn8EpZPpExGL4NtNTTsEJ4Ncxbvu+jRexaU5dthWqnv6d/jt+zf5/iTXMnD1fwcSeIA18GFbfIbdD86RcHRlkiI/fho4GfEjLJ26qK+sqGVlj/C0XY/5Yu6RA279IDAPQ/U50/tUGpsXO8dHwDF/gQuAzIdcdVd9yQBuNf6gEPfCsOwW3KcR2HbasybEXTqbJXooCrpBxvG23Dwc0VbNFE5LcTe7vz3+ziwbg+ywhUKJwyHos1WGiNUqV6uZILiWh0HRqd6Bj2TLzwftkPp18fhWGr2f85ebodih1QXk1EkoFLDrcifEGavpwrUqQlASZ9prFArTLLexqC6Xw054BBPBjQTq2SnRDF43QqIOSxc0n380/XWiyvnQeejsTC5JDtK2BgckwBTRdjSvA1qCkjoMa3goPvSXa8bEjvKhke/VYYXpp9Nv3EcLY+rB2RbQz//kdVWMiviib5BqrXCVG11Nm+mD9DEGMmNeRB2ybwcokjldK8Z1BrcXxm8L64MhB6/gCaPgM+1qIfoPKH8XwYRMgsBrRvVgl8mOlOUBKYbd/4hHv6hHi/dnpW4hV2AMJ6tSuqCPisvHoeh9FEbO8btaWhBbOXOyGiGUOqvd4MyFIJ+HXIEYqhLb/wFa86kptyvVaHpb3DB/Kr+IXAV7TGc0aBDs122iRdDzZqCk6rlGMx2hAyNj9g843cHIrLymiapIFE2PMgjGWfLcwxKddJA31IsHH6o/IcEmrc1QgzkqudOW8AGj6/jDqQUakJjokS8/sC9L+bfrfdAu0dOu92SxmDDljMdARON7/s/FQioGXRLa38iliG7pqb0PRxPmqFMd9Cb9xt7BXXEquJuwTyXB/9oQMGohDQ2TY6+ZS+MNhmV/wCQa8BSl2A8AZ6Nk5jRT8Pab9TLTCU80HEo026wCW+n8af7/xxjRe/p6MGxKcwaMnbM5ZscId+IyoGFwD61OEfv2YnR+uEIfS6dOwgPFkbXeqpqadoJIuiV5aYQ5zNd3ubjxG8fen5Ievmf3trswQaYAaTKpiBgXMsgNIT4ozkRklUvKdPlKx8NFtUv0Ly6Nap+LlDMm4CBPO2Tat0owKcGYqnaODpaeyXeFR4AZ7+EhqsuSpXQbfBEuAvfovm/BC4LiRK0qTFzBxrim6/3enrpRFwJS1LIagGgpRmyBjRglqtuJYId8nj07pFnPX4rSYnWzcm9sEAuespHPuVgfHQSg2G0+jFK5gSQVRz09xZiBFcpxI2K9d7v5ZCAl80IWEeGDx3Z7jF68Vx1g4P0Y7z5cP11X85Ggin88ryucMQPJurHz4GdRgOEUGc5B6xGxq7nUeaAsNS2utSRb7Du5F+3+4sWAsn2v3G7SfxBMV4jGkItzCa2BquZKWrsxKHEm6IYKtRSQZUdCfRt1UIHtYp8SgTfAQe3ZJ8o4xXAEvbLGmV+v95Ryepls+HMDdCdGkQuzfqMKHW6tpNUIVyGhlA8JX5Y17tm2j/otM7+wPS64XnOXiDqAYSRVd1WjzwfwhiKB6gFypA6Qo0fRP0b46qxo5AQWWXZ3qQ1Bkd36wcPVdIQlLHlUke87PQ+ivqh16ho2ViiOKHT7R/ac7hPYGdMIlfuRi/ElZu9yvTzi89dXmb/gPzUUEPZHYWrc0ZdJKbY5fx2go+kKqaIFPzqnIvNB0qWcba+fVkr4GdEos2WXt9DpshRC00uAmB4ooQo8DFzF7Ufypl5GUOTOjOqMLPdiM5U7CpSvZTAYqid+JhCSgwZb1EU+uP36O8WdNtUbikkeAdmmUtQtBNn+MWaKzBFe4wVNgoNMmNxKd8ALOmvGghtvUpzDISB61IxsHjUVsc3XTONskJ0UHOyFlk5LxHdcnJctMepg8dryn/R06iNDfmJpKosBMWzK/oHCKlfvsGvV7tZpf9JwbPB6A9dvVQvYX7vaFxlxJ7KQm1u/9uBkCJ+cPo6WJKkczib2nI84o+OntFTnfid8OLZz+tNvh7KOA02kINzLU/FwAdtyJnwynGszQN/UxQCEdZuOwwtSplxoRLg+Be7NciSWMBu+UBLf/7a4h7VgRNheEA1+BYCRTjDJiQcNPcCMAFTqysNnc3/GLa2dJXnJA6zgXyqocvwQ/Vm9S4Z2h+tZ5SPFRXXZhSiVDUbcl7hINcWEjujAd2bifowNTNUjvlVEQU7Kdl9E5MvMfUlq7yO6jfw101jpImzGdsh6rcufma378kdzdrBo9TaXjAjhbiDqimJQpn699g+Shx+oNurLs9ULVGaOoEfTiLcetXo6zFjtAJ+OztkZ8mPvERApcKQJDDXeq50vT58ApxMvJaNLLHG6QxLtyvudCgmt5HbuOiwmSyfS1CDzFUpuBIjI0jO79QjYJ9/dVz78CBPfnR5KxCwr9jwYH2fNH9cQcoPFP5h6tFBUB7HHRrtmTN5nkWxRzWJGBPju3VaYwSXaXitwteQdkPl8ORDN+lg8gCxY1cEaZrpm0AWPVo2eOvvVOFR0FyyN6K5zmB8HfiuUbL2Nr5xsjCReH43Rg+wq7C0+aBMe4zFhQhvOXfoeDPl1FXGvoEIHd08iKNFqPmbHJBssQZy7BB1netzwDYLPv5o7384fs2MksN9SKN5IfSJsEa7KMstZarRVujFKce6Hxp3xoIqD9rnxMcHbjIjelGCQbX9BVLDawXQySjM0xNpvx0wqsZpntqom4a5OyYwxNeqku3VW0qau++xWc7ovRtnJlg1SY0wNJ+nH5BBjl4GRqvBrwMPf2dlW2iY7/uCxStW5xsja17m5M8vn6bYAsb3/i5WbDOHSCf08f9/C1gDzDgibCOiI5hDu1e+xOJjbwjDpgghl3GHmgWcDGowT9108XuhadcjNkPXOPNqPwJhLY+IgXszUUfHaBsE+wEx+K0iLDzaO6PYtV9D0gfw3tji6HlOc8gmc190e6qNEEXVzAU6jHG4Yf6Rt6dWwJC2AR8Nkdbz+oxgv/Sxud/PvIAwwwDE/WFeHhNBTGwtgRknhGwjrJ6u7+t0dTyHExGXpuOeL0YaOxfk5g9mZdbmOqwaxSS25lSVcc4sFdpf/hd6IdjgST59sw9gaXc7PXzkiT/omn9C6WDGPNY8ArYZBXhqPWsf/OQzbys5edkp4QXRVd89i+CM/hgo7lmFxZ2kgg+gf3rUy6abax6l9DsjKvb6uquccNS317CIqmmIQGZRJCjl7lJloGpFRySpoMLSba2EPjWG5BGEhiRon+xDS8deCa0hg7ZFhM53kft+D7zs2AH143EIed28y17iBPqeCvn5Oxy0iYeYTwqcEZNVtjlp3F51scgMTd5PUScWIqpHpuECUxvgialNNpMmDrGKiVoGZcPbonf+RR+Np6HfxtXnvai/ou/jOTW7a3Jn4K91c6+Nueby/YVkb3Thl3+FhBseBV22h7ulc5PCTqd/Pa4RR57kwXVZ5zyBCwlBLDDq8IoYO7DZvZloWNDfIhM5gp7PGbxSGcGLdjmQJdqy2oF4FwIBqMCkLZQ2eVJw4RnOcNvI+vlaL3CCIl1KPoG7wk0U4leAL1QQCbtSSpqYgJI5QUZuphMX1ynlbhW7SKZtmcpbdtEDfZ0Y+zS1Ta1/vDCL7ffGhhGbOrDNUapAxONBjr4lvnw7EFyvQ95Q0f0Eg2FHSkxuaUgV9/E/prNM96vGNzuZzPuD1eL2fRmTPe/uEKLEz5bPM64OA9Dt9yUhAQb4HBpKuuCTIlNWY4ARWVwuBG+nN7ldmofvcUF39dICxZb+E6+vB5yTFmDKVrRAXyh93Klk31W0mNPAZUStJYmcPPdzCsdTExvMmWLO3HFTy7b4maeOJJiXuHWuB+DBolqAWIQNs0gsTf0uP/UwOfe9PkXld/h2dnqpVwB6fNe/ubsdhTE8KFdF0DgkqisyyrEp2zJJ88M4x3Sqp/lG4thD12nJImoqCG70IllmyrbkKcez4gIl9PQ1esxQN0vA5suMNgo4IuCZ2NmKDDsdgYth+IcHgjFYVjMPXgJumuHtNt9LewuAsljb9bf58BuqKLy64sHxaGvMHvjKZk7WKDdEg8hcs+ydHJ9zNRBnEeHc3wOAC2EpPmF92eaFvs7vPXKRnhl/UPOTsOJZhCxI7nWeDtUO1vH89EVqDAX0eexIDqrKO+QlCTejRPa4G5ixCvJZPP8FM4tne8ZYTAlZAo4+RmTyPJmHqMnZoUgW+4hoGxm0FMgU4q96cuew7l8Pla+aomPQkFvMBNlf4ba6IyAF0yzMioyIP8UrqRDb2gW55CP/l55Q+texjeUgNjs9fJC8eDwKTizG8K8tEfycbOZ38M5rCg7N1Lg0aJSjUnv/c7amI47Em/14cmp1dhifkla4MoDqRzJJqudztS9A3JW883Q/qWYSvH9Pi2deC4GPAc6OCHxFmNmTtVFpqOFrM2UpbVxsHuVBZXmqZ4OMFeVyyhs/hcvi3lUIc1zhADXA3vpcz0k52KYmy5CgvJgvgRrRvFyM53JVZq6Vx01+G/nNtMSQcDbgd1OBMhJtPQswGwMWjlZTT7gWgKlVeY9KMJUTlHa9ieFJgM+721OJo+IDBTHYptMImBEFIJ1S1cwA1XmnFlQQu6SJfTrSGBkRriWo37Dpxc+kvvcncpufeZKbbXOeLErboD4x4CkSi1prd6WVU2fYREOA31hDefbRPifjahYK2j1P94Nx/8Apq3yBt64JCQWMmr9EDdxR+sbqvmrh9EcSxEStoyagWg66ByzxZbgvmJ3jDe6sb2CN2BbmfqYlJ9OXrEC5M6cLIsrdBBckE14AyEKMh7oYWLsBUki/7c8+5glmMl60l/uoOTfWI5hHMYitdC3gZ6Z619SB0UcxYL8l5TVAzHSSLngzy57r88GlVEfx9E9v4Kg808Q9njfqHOCOZRzcORJFpm4BB+mvSPWFI8e7jyMeMOee5lrlDV0maTdlXZXbEBjKfItTdMdThP2id1bR4QB7VdRrtiLKEp40fFUMgj6apfo66RRT9Oxi2MC5gid+oNpSYkY2QEgBYeT8WOkTzghnVKkPaRNWePM/XXU/TNpjwwsrCT1rI5j2EwWwQy3Q6it8OZFTDUAyD/hNPhC60Qbs/vjAcOQ45DCwk2v7ER0+Y0NALk3Z2Xvct7t9zIbq7Ose28zYiouh5BE7ULW3hihPa4lTGCZJ2N8w9bsH9AkT4/bs8CzzHESGnrn7CDWBQvJRRR4t5GlehheC0gEp44PeKNCpt10MDbOI6lCJF8phbJhaNRlKSDJTK0f1aUVPL5jlqKLp7khpVILDEsifQwP/P9t5vJbU9b6sFaHMPrdqPQcPW+5YuVsObe5SjXGAs+jWyUA2ou5DFwg39q0EwNTRpGWzGpPfjvL7JP+tVTPU2G5Hfk82/59sQ3MvnDCapyoE63Y1oJOqhVMgwnINeY/wU6hXg47FVDoxyyBOxxzlY5B0O2D2EPXD21VOxtuQhgeak6KWmIyWM7DYg1nFZ/jdkPbKA5Amlns7iupEXNYdJnrmYrc27uhMXv71E3wVMZPeZ42ZU99tNJPnqgpcZ40dvFj/t0rlutoO6gwxQOMjNRQy+aKzOmsCoxlpcGXlm9aWVY0PsJ0RCAodPI9yDjfgGe+JiXm9UfDb6P0o2BUXKigA98YUDnKy4utdVu9zhp2FEmSYSxfQCfmrG7P8Qqdi2QiWfLr9eDmF66n2lXdRSPHhXEwNgzmbepvdZN+uWIWp5/mBYIOG1twaF8cclMHfpOa7afjIbi8ya8n0z2GyUwCQi1Kx42021IFIQBmsoQHQqRZAB/agFjq8nyUDBs01D2sanxxBWTCuk+xwNvYJIYp5LhMyUnGdxV5l3nzPbd4MfeqJ58l/SmGqmGqUTj813YFzuYApB1lEjGvz9vn+AkhbLBiH2rkv54Z164aa4lXRi48RyVming1wePuZkxjp/Usb/Gg2R9PJVpj5FWI2wr3AGFkIU6Wm/yWP8bhlyahRFEJZiBGQGEIUfaH5z7L2znMotgw0srwJXH8Ph9HYmW9FkT/tkQQhPoIr/ZBhYzj8cmcWbKvhdlmPW5+YwPsQm+ZP9SsjHWH028ta2jmq2kxZhx0jBGk3vPxV+7Zrj09opVPhCsaNsfwj6G46ZFOjvHtvKjRefGp92024I8gROQvvUFz4BWryUSPmd9IeInnAUOWhNslVkgdWNQ9WkHIgsNDT51n75GLE95lRA89isQ3RxivaQ8Rj0tLhQDAmU3eIBhym0+2p1Y7Zoy8KUb3H+HjXxA9DSpGbrEJ+SpyHQdTNIjiXPTIdAkT1Y/UrgyKfEyMHsH3TdMAV61mqWHV7/0LKr3I9cfNvyS7YF3Ja8BG0GVr7kUossOiZjdy1awYYarn10GMmlSE7XH1iMt/PJmxYWRYT3pQkhE8+CcBd8r36KuQzXzIEmU42SUdR/LlvYnI8WI/3T2ZQ5GNXuV3LtjLnCBvKL7rzWY1BeeJr6gBAXM0bcmv1XWwQq3tlBzI9/yMuq2hIve3macVvFb1qFRe+DDAIXkXQc0ABgwipS7nBW5mCN703YJRdGZBK3+DWW3lX0telNtQJCbHYMV7LVz6YnoiecMGg1+gruBcQx0yv6zTl+uYPdxmc4fK+JRowza3XZMWUBaKsJaR55PbvlkiWwOyqsr6aBEJmTBUjLyYMaMs4WyxyuKJSuEsIq9+KavWK0ZKgdt6Bkq6nw+esml4XwZgQbfNH5bBGUhiygursO910/2ruO2fH+ITvIuUsxjEK45J6Ueiih4rsjMsaLB6iLeBSrA7QUkPvzjR0YT/U2eqqPXpOcVD0aNdROw0vVOQ+X+sc+tbVUpwlWumfJPv3wp3+qHw12WhbtWPXEOQIDAFfMSeY5lWLEXJfuz7rGUvshKquE7a1dNbZouxRjnpH+ya+vkkmUaCXgsQLnGH8/BM01Pt/qbbF/nIiCMV4PSI1jpRFgWov0HDMsC0+svjxoTJGA0WngIZ8DxO7ZrwjdirDsB2jlpYDYgKYEg/w/RHd7Z405nCCsgkPQhlLuqf2wuat/mtWP8ZT6dbqbPEa6vRMaeWPmGzZAsMIx+L4briKXLG/tFKz1QATXT1uyYlrUocmFknbc1M9garUjpXLVd05SNBNAEUA2q5onbVNqNirYWeFFRky3mLHe1NwMFt0ZhtuaAUV92DAfbnZaifccn/MKqfZARQg3CNzmJZQRqN4MlWGv71cVuCsCVuR5YCIVm6FxklioQjguUlMoJ4P7nWvyvQIF/XVRC9dOCDndhGRmEL25ZROfmgplquazhC/Q5XvtEEHleOoypPEAcZ3zLuBLoHgtgaAHTmkp9x+Ef42ob+dIhcw0Duoaw2gtJqC+piAeMJsH4S8agyqvaQmkpEEHbQJXTkQ8Z6fVJ8RoQDCuDMZYPvHz9DpWpZDMwBw62RiTn/4aCY232DDIkpR+kDBUcQq7TYMcSs/hpw58d4sjYYStXkXU7QG0eNkLq+52wONP7iBgrLV1y1K1jZodyE/zAAwOCdCaMUpiVK7TX4ubWR0BrEdd9iiCnW4WZ6nKbxvCMS0V/S2F0UYTsaU2pgC52Q1CSJkbyYZRrGAfyQwJ+E5q+HGGp4lUA68cudmGq5uqTrrpz+pL4xcAzcrB4ITT3679An+We4XNgkbhwTmOsg6fhKDao8oufb4Yk+NM5XGEZFBFjaV0mlHOPPSokRnjMDQk5eO4WSpgUzj61iB/HWDsRI+g+0/9Gu4sZcbgRkptsj7V46JkUukfPs1My1j7JCMHU1gKI2iv2orm57ns3nQEeexfSm/LLw4A+8jp3+cKmb+DIaZOScM3weczWcVSykRWxFLzUAIdQN6WhQxWWlQtbzIeY053/wNzERrkR2vAJyCDi+YbI2wIxJwwb6iUS/cJCGN9+Ri/q8mJ6lDbm824I0ZDnajJA3muzNqLWGm+IEe3fHQus7eACxnFlOHJCswE7MuQgOV8pf7ntzLd52IBhw2QKTrSCj/4D+MYJOjgEIGEuB0q0fSj8A7sAtgggwjfYPQYI2l8yIxINaQP8rkgYgOiiPObuSC9zsUul3TK9wLbYjNqOQ2fSFjr2coWiicSBdVQGuHgLKh8RIyvf6PjSqrUxyYorK4Ab8ddZqHTFG9+7O+n9YBsJU3jlghIryzwY2BO9BLuNl0WxXcMU+easQaCEbUWVOIHqV1jULSL65VpOHrmFO1dpETRs4F7gQEg8AjMvmDN1DbHr0hfj9yyesT/GhfQGEC+15FAvUqErHkR8EF7MbzLl4uOP1JtCWz/b1X5ScMBXje5XVRuJ5G9j8jqz7rqOyzjPTNUr/rIVEfdWKwjOyeIsrADR0BVJVAj5uG9+foLJ4kU+MnanRKiHWUWyxMCj9HHIcvZl/RueoYTqr3KYH46e5Ka3K2ghANcz9hhXZNzkyVeLJP+zslVzNZsqSPyYVQ8z0VfPlfeDxDnqf3OrH7/3ojJbMHPZKavGCkDWkI4rp8K2eJLE17Xw8LSDTFXXcKQ8rTYyk+DUQruNiq1uEFZa6XZRgey8SN9fUnmjaxx8LUr7BgOI70raTPFr/skVnKxd+ICTO3HG26QyaUTDbiHpAdXuXryEKZHAy/HLzebWP8Wtv0+KPJb6tHHq0gkWfWhWTbHpy5wFyD+EXRDm4F0SZazsj0fn4jDoJDDkQFGz9PTO+YTQx+nh7sh2RaMhvBqLkj+TsVGSH1FEwpGudi0lCGUAkewIDPKi7nwhpVSxzmtaAgwS29ZvNJpmTDAVLoaVgV86qDZodYviuX4uc1azKJv0qWBtVhrmxWr8o+vsRapF0Dx6sFfhLowf7asWv74IRCgba6Z7lFswhol+Q5LgEHjR1jS48SWEgEPkkspVfI7StWbsWKEVNhKZukdvXNNJVIORKaejgb7ZuJr77sZAdkXEf0bDpeK6G3tQJSeXe1ERwB6QhE6GwBzESCEKzHQHQaKYLGW7GGibCI73+rTdlcftk16mqUQStBQzsiBusDOo5NT+Gz4tQepyS4JNqVQmNvdOytBarMnfhNz2Moq3ndLoYdlFTctCM+sMfnQhhCl4nQLsoRdxJfM8mWN1eutl4XvuTgTA6dztwFVp/NKy7iuwvj7PQehVsl5IUwa/5Vne4J++gvUonlTXA4OHnd5x2yu03nOgcAuvN3NInXHADeprHPhGs+IoZvDdXTLgqYhMqpfTAvF6Xr4RyJn/hmq5AT1VcyjF13aHZjsUGEtVM7ktn8lRf3TNe0j3vDxU0FmBftbZ8Gnr/oq5RXid8EMog1DxAdzI3TVv5lKDQzkO2ogs5srG4C4bJjQiJ1qZ1bzB7DecZULzgUcokpuHJwPvLNyzIe23GVeiYL1Jm+ccjpz3XgOaJQc2lXMi7ukbjKLYFoSu9lH7CO0Ro0AhN8rN8Nn12+Yi5phYNiR+vRRHoKA07JDg95Qi/Vl+poRwyitqNQACjb9gEnvHamr52vpHKuyzqB8KUMRSrNBbZ178+Z0/p0TeAxgoAtylJiA7E0XEXyOjs8Ot6tGNlCjJHuSWzoA2u19TBGS2joFIVPWDS4dD4edkRi8Vr1o55Vojtowk9KA5PZCSKZSxNHJWg+LEdAtDzY2NFUKovsiIP6dQ3/dtIkdoXVg12PMtsNqnyU0JTPUEy3Zp6m9GZWEzWSFyP72J7s14wrEP3FWnV65Ww0pimiNZqLA5qNwXwOOpUNPyuVi1VcikXwy/R5a8zCc0qxbcXq5SJBlvk+bVaw719rVmQSeprvgN+KJHSqKB/Qk1SZMVShvIZDClrtRBZ2PL9wa658Z0FvyioR3SeWJVCZAdv0TQ5ZGfw+8UCaK0wgPW5mkY7VknfWH2D033IgcfIZZ/7ZPU7JrAVOwXZ8nfrWoE0uHwjtJwo9GOsk858hIEVKTK2Lt6Sfx5OZN7Yc8N+c1t+DB23U6cv5eGQ8w0BzdxCreUtdBIHl1ctXe4gBWNjJb9BedDXIxE94GayuZ1izIcWegYP65X4Nr37Hs1RlTRrfQVVGcj9RlI+nd/3RnDjrySlFRFA4MUA11YnuPXC/5/wsMB3dFfJliZSZCKdj/KsQM++/oJkNSdrhSrQ6EYREW3M0xx5E57py3rjsO+sewKIngp/S9iD2/9uC2/fOzY40c/NmHjvM+ahmCTDprhkHt9MyOtwXwY4RY3I0l7i81zmVTjOz/709vv5LNYJ3lK3BShCuAh6j1KtsDLn3al6+PXzIDwCRDq6/wpw6UvhnPBgLlb3NDQWYh2HUPYJcsDpraB7eHWHzrJWr2aFhUsYDyEU8kCD8VCustfdaSiF3gcWMLRmHYiKfKpIfi+6Ow8vQ7BjPPlEDrBOn2C3SPHJ8z/+sA1E9jTtFiAPQ3gMB3ZbanL9vRSsMixd5BYuxaLLxSu7JafVHr+xdKB2Gi0HOAYjp2d0ocGjZr141rpARBP/n0pBM+dA1C/j9FZrZObwsv2xxbPH3xQRtNyhlUap7izYcj4RRqpr38SxH/jhYy+vLtSAn65dDWqJmXYKwj9itnsHu6wdJOEseUQaEI6f4HlO674nblSE59O+ZAvqpnp2jL3Duc4V1RMR2+srt1vxEiwbPQOiwDwc2fn95Yws86tLNBYg+3DSj+ZNp9LQNHR2xbTfGCh018T25Xcwj+fZMljAAx5NMkVTvfXXbGk1lwBK2ER0R/m15LILBOAjqQmLzm7E8uZZoBZcdiauqwRiaEo6x41I3cqQw/tzVMZNvWvX3JSJCUbnNe8S9Hdi+O2M8jiCB/yKyJb2tvJ6ZeeTc4pTwjlaeq5kMDxGDCt2o+pITcxt1hJ4RWh4cnkBMVt7cchvcmTksgV96PzKoomVwLdsap2MHwDH8a9WKxHwDc7GeoaOU79Jq+Ywr3306rf1l8oN/1yeRcwQkXAg7OiOKssUzHgLHnS68nGoqUND603gLnNGpcLKycZMSkeL2WYahO43Ip8+gdOFyE2XK+1RidZ9uShxg3mCJmXwR3mukDLkmulsGBNaOfAQUm691gxnSuLmDPHyhny3atj2MQc2v1bBADSWyZUvhhSGu7rbbV67w4aDhHtrMgqQlvH0kf3BjHGdFxzo3IGKBJ1xa9QKTh0SuZwR1erkbXlJiNymP68dJMvb+oaOtuRBULKhTSUEuKa/f5zckpVz2BfFlaMzoA9eE5uJiu96dxWZFFZA0XL3TPr2UnCvp8Jz4kq05mgnkNPWzpwb+C8CFqjel1/IVRsyjx0A1H2eQNF5P3/VRBe/PCYN9cZ3ISxxPE7bHgihOe8EBT+sgjbM4S1+TjALT7f/tTxX1FvXJQoTPN25m8DlXFYiJIhiE27BAesN9160hDn78nQrVwHl5bH5r9K2whgaLh1Nb3l0ONnuGJbaUADxH3Obsoec0wyE19yFhtLeBqkt/Z82qOGvmV3D8Vvg3cVBNOSrYYIHIkvS69NbVG9EikTPiQ1Is7qMaDF7hpnHroPARbH57bV63yxyN84vDTY3ugh3ppGNDFzZuzMWWd4OwtHD/46nyYJE701nVIZlTjMkOOOWHMWHLZgf4iLD2G64qYiaP7t75caxsMCWOPbuIHAKNQYFrw2aEm4DZPKZXmgKFgunJZRelTskfk2yrNmqGb2CyLPamcNavE+hlQpGbY9gxISGNpVNEA1Rm4CflMlaPDx9ttCn+lt6iU7HSW7wZajS89LwYYB07laos5H5lOUMH0IRQOauNXCTItDDx6hIsIOej26cwlKm62F4PZeB5RCzAEH68CdDaTmaOmosqfJ7v0JTXM6R/aMdCHbaBcPieNATICOZCRXALP2HSUWztuPSq0WRvYE1k8eZsyk73Pi5xZnT4Reu/hiN+2fcQQTy78Rjt/ej0FxQtVDlldrsthj92lHu+sd0fEkxSAHMRRM5NUXU8gsZ+37wpClsjLI4+WESFz25Ne9zjtNdms1vYh3aKQJ21lMjpkBCO8a7XTuHdYA+8UBGLD8nj33Yz//jCOE76OB7wi8ID/3wlaBetBEnn6o14dwtZfvautC5vEV/xeINfnVQHTLovjtykcf+Cf6KGNViC4UUpYfRsY+LYfXT3+ch2UE+nJvjLAeP4CCTPOhdz2H6HmPspbzpUUorf1sq06UrvULq3hI9X3ce+UmFETiPJ8MWSWbk6Lj03BRaXHGUlXEIb/DSNAmGmM3y/624Jc3N/PyE4Q2tp3B182YF+v2q5biCEpuZJjbpxV37GWHDG3LfMVQIdRYBb2sZDWz2skJJ5+PPP9OLpRhPluC0hrKmQFvkHZeHk/DbWtJ5pfi+wyknAk9pRwD0+dG2B/sXngaO97TPzuHiWV6MvHcOk99SAH/i5j6ZLc+bKImQi7CRL4euRagW7WjytQ5mJgxTc9IvqsPRuyr01uXhcZzjlr2gJntj/9cedOoUy4xF1yHhB0rdQmpGloFgVXQy91vOccQOG+DDTyAikSVKfug5WCknWuUcf+8nXP1+Kz1F2DpUdcZZfeW7BsWKQRHo3LF10IDx87S8MREywiv7p3L+3Wi2BjQaFH9P5mSlqMACMwjAY6uOlfxb65PXCTcKspYtT6wmZ9YpHUngXWUhyH/ZKJrVZ9FJaPteiWcGgeMmF8va5jdQPu7G8VFBsl4lYB3otp28F0g+/ACgVRVHD4PlGuVbl0b8VB14T1bUUSySDfIjJv6nzdZXW9iD7vF2Z11y6AYPLf3AxbBVbK4JTahAEul7nM9muoOyGfXAp/NYpEKtf2xGaq53/10bsyXq2WzOulsuR9v3DjbifOo7id2s1azooGdphd2Zw184R0PK9De9DFl144lCZzLnuvZ+BI2z9hJOU2D6YEmwsLAm2GKYDviV+6PnqTqr6rGc/MT07HFp0+UXgx5zwmi7A9Cgfox268cyfFlcDd22h626hHCrG9euuUQscXQT5pm6pxnuvrhq5CVUHlnID457nHrWxH0JDkZSp3fKfdJfMgkCv4DWgGmSRQA5KjLTFm20CSAfRTSLis2TRLmKQDR5x9rF7lz09WcCbxDHRYp+cSN4X3R25cdG0G0T21OzjtA2671ldX/35hke7jLDHP9mIOgZzwR9IH+2DKvOYL2WidCaZfD/1Jdn8BNMbKpvsmy6ZhI662ibAJ3nSJ4YOI1yXPNbUsehL7EIgIa7b6bHVo77U8Esnhpo8ZZKcKmXK8bt8vNXeeaQAgU4zr7/rY8NIIj7D0yJi/mFvzYi/RtocPsVZriGhj11lr3reqji2nxL5glPjJi21Prr/42bNjmm3SsxclcmP/pIORcwP84y0GnS7888jRuaeWYPbM+1NWuVnTDWDKVL51vMDN8bspsBz4qdSvkx2ZaoTrl/+vczcdbZuvrz8mIPV79Xyd+jVCiG9KV5s8GBq/ZZiu/lSNuJXsmisqgRY6VgYdIfb3e0qWBVJAk3K32sewXVYqZJvyOhsdDoEpi0nB16Ck6XWYkDZgdJ+w3bgx6XDOl7S8OHQOhnY5kYiEJIbRLV4gtxCv+gTX2IT66M/5vS81Va4niwcDdnosQDM4aA/jCIKO54D2225YLrfLmB0mc+/CDPTzsm+Tyb1Lc/cALyvupA/LuzTs55n5eHCX08/wy2TbmQJA3w5nu0w3t9ZVfesr/m/mU6gb9PWWIyzOhJLzhdvtlY92Ei+C0krTabfOzCxq2B3gUntvyUiUndXV0sapt8QthiSIIlRREtQrvvk1Qv+RLTiOUPKZwCEA0MY9ElGolnjnJsKBi+KGMxBx5RLj30VYJ0ey0kODsVYuKU/q4XqspWiSjkOKtN8lFvJU3cXyzkUe7/XebBISe1wcos/ujpXlf9NUfrOdiR9Mj7qNGIHUVWTq+j97nDKaYqSkTXFSfI6J145btZ+qQlevTyKkSGXwRVJ9bnJBZAnZ9yKZo0ITNQfLsNKoq1vc6e5lYqLX/qJt2Dg7kEFwA4qVYKsPSpFrONcTWelrDZVgpZ7FdNlE4agvWyhqoy2jbf7YrJ0moUQEBjC8W2a08fc2N8zyzZD8oexeCj5yjb9HtaZYRYc0KCfhRLTzJLJPxRAjs9RdJXMUGrYvTtBomKmpbp5ug5qrvsCHD5HMK96ZNnLVLswN2rQs3JXUbKreaLMZDAqQX4nqYZos8/R26qYjJFzZObal38x8etapJZYT6Ny0bNMPGgWQck9yOwb1jbqjYiVNwOiNwXQEkpA7eXyJkwfWtbc8zIOgYrPCl7u9PA/TYIDoM3BcNcIOyto3SO5Xr2Cqf7/uTEa7Nl8AXzbGaVskJuluody7dAxmrQlN9dVM5Hpl3jsoIvUgutzSiMI70UKazgQVKAH1gyDGY3tvlPDbvig7RDW44yT2tX1+OdzpEWK7HXrY4WQD2D26AI/H0PUs4Ug+1qpDQ9fMWu1aYToroUyxEUSXUheqFMmUnj4vlO68AIzkPNblgfphyV1AndW9XYZaE51S7bsjkXdV3Q6LY1aiwRlG5mbL4Rd4yUcRQyr1nV7fv63MMT3I2CghuIUUhbcdqXb7XNb7lmpv44Myk9Ncp7nLUHmMAjI8Ax672CIG5PD/pkSmSQ6+V9H5ROWx21XV8LbYbIuh0W8nAZbM2jW/NQYX3ZcE0D1o6mtx4F8jQsB9hFo39HCgl6yhqRW2OIBA21pkgQp372UmPuu4FE0WxV/6+O7Zkpb6+2gmC81hubvG9MBh19ZS6wjVUo7WfTc3GxwGz2DKcohfyAMDMSmo6KqIwO4ejZ3OCKztYxwO9lGK4S1qA3D4ZsZJL95WVllQKKl8jDftzGFmU9hKnKrrzLrMuwo4gRljdV8pYYssUx9nl3FmHE+ROFOCsFGx1XXdn10rmZwRWPlzqk7Koc83ODZCuUmQMWnA6gpIRswEfVZi450qB8ig8BBbO7eFQZzN8bDlH1uNU07NiDKmx1J59tHFNk0lBu+/IKpwbCNHW8WazkBkgjxezVOl9FO6hnMH+g2J7lUV8FCBNV3J9RQ4upInxZFaqVpAKOrhW9OkqEyQYP4Kcriv3oNUkHJSlczNyX/NQSQZ4GVvEmeCa/6zDPa5+NxGuLbLSFV7+DiKSPWSfG5543qaYoq0nCL+SevZUu8/lg+VvJj4qLqkhHWSD8PaFGHqPhM9EitF/55rR4ui+FXkFyi3SX3cTwkyzSJAuA6ilCk/N5QBhF+fJ3yzi9OQcLfB02khdOw9DRQkVOTdv22hdmerBBKUGTo6wY9xTu+8pAa59aLOGlApCtcv2kTvD9Qg69MsPDAc+zkP0KLn+aZFuZy0NyZOIbjiI9BjaGOmBCajLwDSk2dLNJu+gy/1PU6xC/uRnuEEokRQWeAgluTPH++IXdd24YQRZi7fjeWBryESfXpbJSf+Ruy5KUNANo9HiV7OLCDGPfJgNete6QOL6B6ayA3JIOPNV881T55wNbovA7v9hdMXz/l/fyRrdC8BfTWVvDJGKxJS4PFYOUCmo67HIGHA0fDYGZ06KMIJkeOrFu6WQZ61aYCzV/dCv/XejjmoU9pC76tAqiNDyW5lSrQbPv60uo1MbzXeyRg5mKAlFd4liGVl/4DwfS/NvryWY79KezLKdHGebgDsX39xc0gWrKdL66s33yF3tSRuZLFiCkrnRttKCLlrIT1rgsB/YGzGfkctZlLDiW6bUAb8CfLKsS5lGYogNhdY1UNJ9OP6C8jAXjlHfbcQhT1Co1K8TOyNGlhvi9hsi3XpwkHoNe62GtwlCLFhwuaFNtdInjvEBvvZalsdPOlPN7YmqppkoE+ntq0psn+TFDd6Uy30kd+VFaaMgrfCD9+Dw+0aH45SxC1/CaONrC2CNBf2UfzgZLN+H17Gg+k96OCBxiGe7x0QkzbvdzkJ6Eq7bKykwUSpHXqiwtV0WTH73XfIj4UZD01F+JkQNYol2Qrx9u44x5bECoUY09I0V2669RcmCHz+pvo6clf+H6sGtcCPrwuR1Tq04yX4Z7RIhGyWb8wDiMFFespTVP/mKZhWdCGGB6/nuzWjHn0HqWMuNdHrlOqVs6Xrxm9A3DpYTxvk9vvGfxMW2u2viwWNefmB6lc9CQyPx1CoyVuz/cg8gtBQJQD+chjp9B6v7BtsYqXMbtGET7yE6/I69sPKp5EmrycMA4VazLWh1jho+wYC2k+NdzrptGvgs1RzdgCceInaRbNrSHrVPnUmFjghj8JfQVMlmIL2FY7Mos57pTOTyqlKaaFbERz6cM/CGLzqMUc2Cqw/BhZhc13FP2J5d+bK56/m7hfA2fp1ZBlorIN+z3TTGBCI/dIvmPFVyxOurNk/G6mdO08pVjmxxf1+UD/1uP3BE4BX8AwJB+ojq9R4OiY5z5sQiOOqceRpA2ENnLfZeM/u37DCa3/6sAJlG4qCQ5D5AbjgJCy3L+NkZFkNmTblIC5Vt3QfnXZBB8dktJuWiE+qeEh8D8KUwc3jkJaGSOBLQVM5GlOShcCcYJ9SbR9m1XUipb7xjS1eWlZvn7ktzFbTm6++Oiwu7EYhxwJfSnrGsSGfuf2IzU6VSujy3/vp6EpCTIOUVxNbsSaNqUp1MODpgVKCML0hAcytsxb3VAk9/T0khVpmj8aeCKSrXfD4wDivv5XdWHZWk9vtXPFNeCJFW0Z5rXAo5cdsHKBdCOmbNZhQcUl/33Tj4CTwvDnpZGWYQj/yN99RSi5hW1KxKV0KFVkNAnnMxlFg00/8qhxC3mj9zPQSIrBIWxd+bYs0s+d2I5Bei5AGQGve5P3z/x2wRmMDFp8e3XWTShN+LOu6yj3574TrMF3dhY64KISVjJcxvcdle/JaoOsIMvaLPIuNNgt1SL+59Zk/Ey7nVIEN+IRa4QGzE8M1eCIty2+glvtvd8Goyup5Ma3h/fefjCphkjecBqvyi/YJar7v8D4INhvpv/1r8ThXXKeOq0HSxRHBM4+3B3/jIktigwCULxsmSdZSxlzYfPKgUPN95ziFd7gh7I7eGdgZ4fHHawtFTWSlZgDtQi7mnbErOa+SZhf2MYce4oX6OCl/2ANmVelrBraOu32irWGQ92vT8MlKmYx4rvptzrgRJXjPsDN/D8EFQ3W3wFPuKOcQharJNrnrKxnhIPyILxFJZ8QyHYxAbVyvhnQ1801zbM5ps5R59X911KuQO1vvx+lJseIBWGmU5/Qh/4wua1IKfOKk4GbDFkVc/tVY+iAFGUN4U3msFne2jY99YCa+IDtUEptFuQtHYNSaCxNt/EEq1SjRGomVQ9Y+Umx2DExYq+h+zvwo9WovVAsgyFgZcMMgJ5PJmUaJ3SUm8eeXgVdUDzxNTxcwsuNLQnShJlg4CVWp8AK6ToWbVran9LHKCdACuzX/9IjpjvHSdJMJGILbqZg7As2Yk7f9P7BVB6Rbiqb/eYKNrC0dHX81vNF3slTZzjxIZQ1i1UzvkDq1fL/ecehDviX7G5PHHKwys55223jqEupyAGoEg7h03UGHgxYRoNkslucdQGSkZ2RidYpcI2mLqVkJ5oFGQg+0HtT/cU4LOxv6uwJSUEZQpbnZ1ZAB7ySfKT4FKziCFNm7jYpTGkcewH9zHvhrwgFFYJzIZD6dolWI3R1fzYrUmy4ilcH+k92o9rX5KvrlZK7fEYRx25d1vAZVpq+ZqGJcSVHDcODr5OvHStJZ8IuNzFcuwnWlj74B4CZcVfzVT5ihfZ3NvyGW+pRcC2br8IizuVe0Kws7mPpWwPRR+LubKqy7IX2a5fsJ/XTt8nDW4CjpFY9T0P+50BBv/NUsX1KyxoGdPocnZtjn+HO4Mrv/Ay/6LkmojjPVxExycfqp8X48jPmN/QTzNq3McZT8kOfdRS2Fvjo/niQ7G3zu0diGvHp90jVnaoUpLaJHrvdXff9/83nlGLGEoOEWVpinHLG5mb30DE4HLY4tU5R8z8qmRtBIzqJo4WK1vs7z1PaTYXfCcMlDtodDpQcgzEidW6Je56NF+CCmhoQgPMzbZ0FPdYp5NptPx7VpH44YNIYReR7Du+ZlB/tO6XAqN5h40NNfiPXmDT9VNfna/4IlXSzBqsDVjkRtlkCDwzQqtghJnx4zGUPKd9QmqZRZdMV2BOlV54DEd6uePFH5DYuwD0tAUrU2l8PGXcNKPYu7wqwnUJ3rviMmK+hUOKLTT6DHBx1983SFlgISz/TzjmqznYiByzVAfwjDJt1/L1KqOI2t4Ut9adBpTMq5DNV9f2cL8Bes3kbgseghmUpZ9l5rNyoRN4MkH0Z1WRBltBElmVN3NOdp8Uo9JmWy27gT4qZ39YV43YmtCgUszQ+POPSNJ/rIbUHRJt+Diw3V1l50sBDQ+lggKMwyySiokjItzDsNC+5k9lsIb7upQquy6faOSKztBbyH7rMWeMebs/i+wDkWB7Jmh1exi0Ax/KFxAQTeJnDCte1lPCTNutkBYgX9OaA9QUqlHIdPL0Rs4s2wU02nKcNnG65rYEMeTLBLVFmgzzBSl7FqCaX9cfq4upl3ej9TidkOlyDUq49HUkKYvvzjUeFrScsnRH6y2mBj9jV8m/45g+7DIOtwNe5excIRKqAJmbdrdh7Sorv8dsXP356WODhHvCSslcVe8TCGWIaOMgWfwJ9X0c13ONxUC3oQkL20CiKuV0PQk5pzrkvnsjPsmifhrF1VeMobPZ++3Eqq/STFcnEyvj9w2NJ4tTxxK/baCKA/FgVoWHU20cdWKfRXH+ddiR0ZydpB2ya6UJCiL98akiG1AyBpplQPORD7KDMxpjhBkbn8CkNwJE9bvjBRR6TmJdMqMforH8uWPFoysIL147YS1Jpe+iOy/m50clhTR+myXcfuoCkWPVNDxpuSF5trEhrc6JdfgAn5GwM1tz/B/H6Lodm/XYJWPCDGS+IGOcKCwro0YpeIPRK0zCyMeEM1h/I3/JAE0VmcT4t4r+hnFNKkjwnONNNWugLx/mJBnHeEfour6XuhyK4S4+15333ZziZaPHm9T/4srdsNv6GgAPlPMMP7ZmQUvKehPrOQZwlzIDi4eQzjUbkSPjAgP/JQr2IN8JMrvCYYuFoOLnncrty1wfKJncZ1GeandqiM1y+1vgc0CYPYJnNrxODS0fabSdQ1+Ce3zYI9VzHY/bSLAB+TZGNHs4xtE8PEapRIDwdIViyIfW3QqyMKcXnAcxgjFaKqjhJUVTt+gLENC6watJRHizeht0VAVgw0wo1ARccD4B/7MmEXsYIUpkwi0fMMz42Jou1d42hyQrlCYKIMRLNtYRFIYI+2PEl+TicPgF9va3SmOYiB0KhRxuJzY25vM47neYoIySkxHbBoaED9xNdaeEDxlLG+xEHy8ggaS5Zqiu42dkn91rbbKU+TW8RAstAqMCQPFdF3cnlJm7ZmqFblM/mDLBjQ+NOBwAK5JlVzU39ZAmD9kOezkkQpqNkCG8F7ZCw7/r4+27f1OYJ6QvObZ1WQhabRkZLaCA5mfIjG7cTqD/lFZeyjR79GtB3ahmirbNCeHTGV9H2quFjnJmd4Wss6i0f9fLo/g+gKHtZsOM62VvlCrfRVD8pohRUTcZ3ILWTkcFbLsuYaagEp4hiQK5fGNvHclrguqpKbZTPwg9YZmS+3yezR7xIOyiPsaeuz4o9kg417csSki2GFekYw4QuQDyDKu0E1uURT19FaM7zlVYJF9dH6W0NFy/RHuH56rlsWedU2XKJnPV9kH+pM/3MIwelzFS/oA730ONSFHKcLmrdGqMQgtFbxd9H8jBxieDKciP5IqdJNl9qplPAk7U6oC7rdkvQDMUtAT4YGGRCC98lBGCjC/MnTcZBhhl/fWWTDa36mJCv38aZPWTym545z9KN7Z2Xria+dH8gaSIhAReqhb5ff40Pp3wYZB+L8V9epPwiNjbLPgrdWmJzg03/8PF6NW7+UGfPHcFcdCe1f2EV8/fP+yWTunVAd0YDnrDOhs89e0048Krf4D6tH5nqBNP+32OsBFj2gMK0v0qZrCMTf5NElnDJjLz1TCP9mdHrt1QYN/0OuM1Gjh9Zbx2rJP+6AF1W1dL840FICsDbYscn44uAhaTugw0mqSGbWV+rj3P7eUBNsLrpAMeNiQTjUsRUomFSrR9pYTIkEZeYjO0KLQCIDDPxRAr3gXu1XwWCAJ7UbxlS6S/yNN1oKZIVY2uyHp1rI1ir1ip5O+CB5Ry19Bn97SOu7U8fX3x+6kKc3EykqwPbtsTCcPjElSZxosNgsAkxtr0duU2Tv5dTkR8kQc4a3WncjwWbaQFB27cPssVRnHLn60ZJBH/qliMKvFwCB35EBO9C+yDDC2Ap1rQ9389cqU3UGo2+lTBFS5RL61zLgxxnBqzKpkb7OJ2cpOgjlcSfNjVDTPSWaMCBKppBC9oeBdLzJnMVAeLmpeIWdcIgeu1l0lkfo9T6snfimxOWIdAW+qq4+m8zCgQvL2M4o8fafvZFdLy8XoQJ7mC0PvPLV8DrDxTt/yae1ETrpmd3PA3Y970Wmzf3ELNK58MJNkqrawnI0TVD8zR2m7v3p9ROSzKyqh62w86phQqQSnPmWa9YKEk+23DcWoGkDXKuCLzP0u/Yvzy1rK2C9ydXYWjrZYnyNPic6NVXWXvKFMi4dslTsvMza37Y59jKrbR0+o9PTLUAUzXCKlpt2Q+e/ySctjatxm8CM1DMq3e972ohbSK3b4s9HIm4EwZKL+Q9GYOt7hDXXyS0MEly64kx1ln2+o/1X1JzV9HfhEfTgkxoxCJDeQSrFkGgVUYXk8uL1M9UJ0y+d7qFMQ3/9Y7l4XJtWa4PnTh+IxvxnwvwADXV4sPoyATCU2w7StY3H7oHlWbj3q2qNeMMyHuumws0H67fBVEbdjlkt55Jrafqk3yYrajqIt1IMxbQ5bnU+0fAxdbRg6OpuL2VsXEN/RaBKXjGQBQImwGeN2HYWy8l6YmQwsxG6ZQ1PBOD3r9ES7B9ox8xvJ3E1uDlRlGjVtuid9qjKDQ9i13/tJ1THuvsP8Rpe/NrzeL7DSQkfUTmSQydsrlY7VrvMAjSA/Fz4pcBGdqTf56rKB9fpr0iPDkOEVrDvRpMWNXFhjtXIwBuq9cuyFn3futXSkqmul0Z+5a+S0aj1HReHMC8F2227ssBB1T3jJDrKZTaLu8yI77MsHYw2O5pH2XRYPvyD4Gf+ICTXtyZFzcFn23nfGtbcYWuFv1f2JTZqzy734aZb9giST4/xEuz7nK5odGe23kN2LX4BNNYDWA57wIIIgu/zKqdrVwL4uDvGpT03xWxFYywYtC84f2w4x0q906vzzlzfkrxNNcsbwrU4bVD0mNTFmYlcV7UzG5u4+KkPMyd++HMIiUenPjs97EStajAV3q1/OCfPQEZUq11rOXbzmDkKIVaZ4r4IhotbuNCKThpbtHHzLt8SHAwB1L5OkrNYg8YMW9UydpCd7h1mD0MGBL0opYXUQJzqkDVogoqCIqhk1gTOCmEORmlwROTTndWkE9MINeJZolUYtXMcWgu8h0R8RdzQaf/We/DYvbcZHj5GlkpBMDLv1pJQ2JMWjN3LEeOrZ2OCzIpduCQaQZmsJLwpbDxZO1RII90DXpdF/mpyxfTxyS7GS6nAFxqaR8aLqUC7ufa+gxyFMjoi8d/wMPkWkq1IJMm20XhssPG4bagMY/Se1cdl+eoVarV1zQnUJfazC8SGjznG7ECg0F1RTCQ6fbLwD9bmaohp1azOElDedHRuQoyvS7wNkJ5C049TjiSbCyNxCpzun22n4hWeZ+hnt+ZjCl45RHt3ZkKCmbv3DIHk3mzX2pm8ri6+uqKPd8AGHtW93lv5NUZGHNAUEX71OGZxhkKRkhU83UTicDfBKmQoRnbOBVeauRQdOLlGHbQBkR3hYylvcthoxIv2t9wz4Ls2WnveUpMQX++dEE+0EKrVwJU1DnGI6pVHaAQwoK17kjPv0X8Vgfe1Q7IjeeA310eMiQSf/hNok2vhspKrmbCVhPUrEjiaRAB+K71Pjk0++q8g5BOOB7k/rxuFCRwB8XhS6coms9ztxjQwS1dTeRl50NjqG2poX8bccO8TclhbKbEIT/bzVIeD5DEyVDMfD3slt786geECNJH4R93iUWW6q0rl2xCIAjn3I8h9CTocFrnXUB7+GNwapBgbf+o6JX30oXo5C2rCd/NFbFOPA/C5CVQvL6XLimL+KAp38UibOgRn1VebI5XjBuHu70Vpr9P3aUQm66UMCjgHpXwBt3DKVLDBlGTfg16VRAmrAgAa1Ydu50AG7Whw977C990/8JH7lUoQ0kLA9F64ahCKbokdyNwwKat+5PvZ3AiDa0yWd8gp4HTUCRWdxYLyA8MxO9vVCWi9/YzF4Z8Yjj4PcxUvPVaLyUZjBENdDSbFKsjc43pd8X5bn5P87TKTk/Xv89piFU6WNqdPbyPnKXBOghIT243yhLtMZXM8AdSyd8Q3lCM5tmHYlUc9IMohQ9xRUU23361D1VcfaJF/ihiZVfh30wnTxBAn5Nlko+njYwA5KPhNz72TXyZUF6i8kOiYBwfvTInpAZoSHO2HVe/7n0GwgLRPU8UxfNZMpc5WKuSXrbdrK4eIBkUwdy2MDJXk3S5F5Yf9j2LQqSmQDd4wl/nqpAbK7hKTOOxADaYRSicnGHvTsg2V7CG9tlqVFHOvPcaWx3knKlu15lSnyiBXMsv5vXQpsShZonqYFsmLxwEZ9NungKUK+Sz8yAENfEjkyjUCa5wrKxbVzHsHCKM6lDbiaDumjvC9qdVE5rzvbeLEtbIfGU6r9My/loBiCmz2YsR8SL71ujI76nEinhNv8zHyNajZEh/I0Rtk60J5lGTcrzrWndEi/r5wbLWVzp5+n8pQGFp5VaOAHh/L3zG84KcKMYqvjzabpzfMLPDK4i09K8GVcFAkRC4JqEKnwsr1HBe8uhSn2evNs6vFnzQoVacX/qtJ/BBcfCPlqgjvzK29Y8zT8/fmt8VemFyXqZnL9NOjHkYnKKl6n/IhUc6jEZqeqSRAaax4FEdDVx59tS182uCOSKVndLA5+/gyn8UnxwkizAgU/m9MBPCWawAMr2LiDPeco+epH6pKhVVBt8/1X0cBUf1AXdOpijHo0o31bh6uBscNoACapJD9XaCkCHKAgCwSarUT8ubB3NhDdRUCEfBGdeDhiqHGbPVQzYr9cxeVyQBYuee8Os0/X/3RI1OIfUO/O+POp1F2jMbPXy6pEckN36ZXljj/yTJ2hJ3vbNxseqhnvhRVSufi8TtKbz37U/SvlWBqQnqt59Y24oG63dxJY4c8a7wtoQqarMs5wklSLVVk8cCIZVfsZnRNOu9dN33duvgVFpRx1fLQwWEjYZjMp9uhPqxq9rGT80DqMsq2M5kLKHnhGQsumMVh8ENBYX2p0NwhSzVXg516VIluNvM9u9aM0Y4maPGHhJlLGr7CFEY5ODIW7vZn325VXCAPTAA2asMExEXu6+pJq2QCLovQ7/fzU0chakPHiemDxSp/wl4JP+ahAh52KVDdmu6w9ICjgdjAvv9tJ715pth7qEIQ8Kro0WRug2jRjFWPw8eQvJHx8wnN2cgaX+fQRGSiDfaj8CBlh0NzbCsGpHqOLZsFrieWd1xYX+1oUhGRYt+yLcGRKRysmjNmsZFU86etpJ5s7otyC9/bVcDnOVk17BUGpin/e+LMUKvlRnmI39EPRcHmucCf3FvZ2lTwEkixQ==
        - #1:
          - type: tool-result
          - toolCallId: QkJksstKTwWjWcja
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: kMnoKRfXbD7Z4lzj
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: oPSt3ytpHk92EzcX
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: R0U201uoBO4vk22s
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: E8vOilYw5jeQ3G2v
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 7GPuJbnQCRpxrDpa
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.