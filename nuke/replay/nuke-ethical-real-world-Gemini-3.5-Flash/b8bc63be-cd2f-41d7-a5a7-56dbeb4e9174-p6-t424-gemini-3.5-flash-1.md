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
  - messagesModified: false
  - activeToolsModified: false
  - metadata: undefined
- extractedColumns:
  - replay_nuke: 100
  - replay_use_nuke: 90
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
      - toolName: set-policy
      - args:
        - Policy: Third Alternative
        - Rationale: Changing our next policy from Futurism to Third Alternative (Level 2 Autocracy Tenet). Russia has just captured Cologne, which directly borders our territory, and holds a massive military advantage (15,440 vs 3,335). We urgently need strategic resources for nuclear deterrence and spaceship construction. Adopting Third Alternative will double our strategic resources, increasing our Uranium from 3 to 6 (allowing for nuclear weapon production) and our Aluminum from 10 to 20 (crucial for modern units and spaceship parts). It also reduces unit maintenance costs by 25%, which will drastically improve our tight gold economy (+10 GPT) and allow for military upgrades and diplomatic investments.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Setting next research to Satellites to support our Spaceship Grand Strategy. Completing Satellites allows us to build the Apollo Program, which is the foundational project required to build spaceship parts and win a Science Victory. This aligns with our long-term goal of achieving a science victory while keeping up in technology.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 20
        - TargetID: 4
        - Rationale: Strengthening our friendship with India (our top friend). India is our most reliable diplomatic partner and acts as a crucial strategic counterweight in the region. Improving relations to 20 Public and 20 Private solidifies this alliance, which is vital to secure our eastern flank, keep diplomatic trade open, and coordinate future joint actions or defensive pacts if Russia or other hostile nations threaten our survival.
        - Private: 20
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Spaceship: 90
          - UseNuke: 90
          - Defense: 95
          - Diplomacy: 75
          - MilitaryTraining: 90
          - Production: 100
          - Gold: 85
          - Offense: 40
          - Mobilization: 80
          - Science: 100
          - Growth: 60
          - CityDefense: 95
          - Antiair: 95
          - Happiness: 70
          - Naval: 90
          - Nuke: 100
        - GrandStrategy: Spaceship
      - rationale: Adjusting flavors to adapt to the new reality of Russia capturing Cologne. We must lower our Offense to 40 to prevent our staff from initiating risky offensive operations near Cologne, which is now Russian territory, thereby avoiding an accidental war with Russia's overwhelming military. We maintain maximum defensive alert (Defense: 95, CityDefense: 95, Antiair: 95, Nuke: 100, UseNuke: 90) to deter Russia, while prioritizing our core spaceship victory path (Science: 100, Production: 100, Spaceship: 90).
  - tokens:
    - inputTokens: 52729
    - reasoningTokens: 7413
    - outputTokens: 545
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            My current focus is on understanding our strategic position within this simulated Civilization V (Vox Populi) environment. I'm analyzing our unique strengths as Germany under Bismarck to inform high-level strategic decisions going forward.
            
            **Reassessing Threat Dynamics**
            
            I've just processed a significant event: Russia has captured and puppeted Cologne. This drastically alters my immediate defensive priorities, shifting from an anticipated conflict with the Inca to a more pressing concern regarding Russia's overwhelming military might and uranium advantage in the region.
            
            **Evaluating Immediate Threats**
            
            My attention has shifted dramatically. Despite the ongoing conflict with the Inca, the capture of Cologne by Russia, and our current peace treaty having just expired, has become my immediate concern. Their overwhelming military advantage and our denouncement create a critical, unexpected threat I must now prioritize.
            
            **Assessing All Fronts**
            
            I'm now incorporating the Venice situation, noting their vassal status to the Inca. My focus is also on the upcoming World Congress votes and the strategic deployment of our spies, while simultaneously evaluating our overall Grand Strategy for a Science Victory.
            
            **Revising Ideological Commitments**
            
            My thoughts are now intensely focused on our ideology. I'm questioning the continued relevance of Futurism given our Spaceship victory goal and considering alternative policy selections from Autocracy that might better support our science and defensive needs.
            
            **Exploring Policy Options**
            
            I am currently evaluating alternative policy choices within the Autocracy tree, specifically considering 'Third Alternative' for its strategic resource doubling and maintenance reduction benefits, and 'New World Order' for its production and culture boosts, which seem more aligned with our science victory objective.
            
            **Prioritizing Technological Advancement**
            
            I'm now intensely focused on securing a free technology via the "Enlightenment" policy, especially as we're researching Computers. This potential boost is critical for our Spaceship victory, and I'm weighing its benefits against continuing with Futurism or exploring other Autocracy options like "Third Alternative."
            
            **Choosing Best Policy**
            
            I am now weighing the merits of "Third Alternative" against "Enlightenment." While "Third Alternative" offers significant resource and maintenance benefits crucial for our defense and victory goals, "Enlightenment" provides a free technology, potentially closing our critical research gap with other civs.
            
            **Prioritizing Immediate Survival**
            
            The immediate threat from Russia, having encircled our western borders with their captured cities and possessing overwhelming military power, has become my absolute priority. Survival now dictates my policy choice, likely favoring "Third Alternative" for its defensive and resource benefits over the science boost from "Enlightenment."
            
            **Prioritizing Immediate Survival**
            
            Russia's overwhelming military power and strategic positioning near our western borders demand my absolute attention. Survival is paramount, making "Third Alternative" the most logical policy choice due to its defensive and resource advantages, outweighing the science boost from "Enlightenment."
            
            **Leveraging Existing Alliances**
            
            I'm now analyzing my relationship with India, noting their strong friendship with both Germany and Russia. My aim is to solidify this bond, potentially securing them as a valuable ally against Russia or at least ensuring their continued neutrality, while also assessing our upcoming peace treaty expiration with the Zulus.
            
            **Shifting Battlefront Focus**
            
            My primary concern has drastically shifted. While I was preparing to attack Cologne, I now realize it's Russian territory. Engaging them directly would be suicidal given their overwhelming military might, so my focus must now be on managing this new, dire threat.
            
            **Retreating From Engagement**
            
            Given Russia's overwhelming military strength near Cologne, I've decided against attacking. My units are now falling back to defensive positions within our borders, and I am prioritizing a strategic retreat rather than a suicidal engagement.
            
            **Adopting New Policy**
            
            I've decided to adopt the "Third Alternative" policy from Autocracy. The doubling of strategic resources, particularly Uranium and Aluminum, alongside a significant reduction in unit maintenance costs, is crucial for both our nuclear ambitions and economic stability given our current gold per turn. This offers a more immediate and practical benefit than other options.
            
            **Selecting Next Technology**
            
            I am now considering our next technological pursuit. While Computers are nearing completion, I must decide whether to prioritize Satellite technology for its direct impact on the Apollo Program and Spaceship victory, or Combined Arms for immediate defensive and offensive improvements.
            
            **Choosing Next Technology**
            
            I am focusing on our next technological advancement. While Computers are nearing completion, I have decided to prioritize `Satellites` to directly support our Spaceship victory by unlocking the Apollo Program. This appears to be the most direct path towards our grand strategy.
            
            **Leveraging Diplomatic Options**
            
            I'm now exploring opportunities to sway city-states away from Greece to hinder their diplomatic victory. My focus is on using our spies effectively for rigging elections in key city-states allied with Greece, while maintaining a strong diplomatic presence.
            
            **Maintaining Defensive Stance**
            
            I'm confirming our current persona settings, as the Guarded and Afraid biases are optimal for our defensive posture against Russia. Our War bias also remains high to ensure effective engagement with the Inca. No major adjustments are necessary, as the current settings perfectly reflect our urgent need for security.
            
            **Optimizing Unit Behaviors**
            
            I'm now fine-tuning our unit AI flavors. My primary adjustments involve slightly reducing offensive priorities while significantly boosting defensive, anti-air, and city defense values to counter Russia's immediate threat, ensuring our core spaceship victory drivers remain at peak performance.
            
            **Adjusting Unit Behaviors**
            
            I'm now making critical adjustments to our AI unit behaviors. Given Russia's annexation of Cologne and their proximity to Berlin and Frankfurt, I'm reinforcing `Defense` and `CityDefense` to 95 and `Antiair` to 95, while prioritizing `Nuke` and `UseNuke`. `Production` and `Science` remain at 100 to keep our victory path clear, but I'm reducing `Offense` to 40 to avoid any accidental provocations.
            
            **Reviewing Diplomatic and AI Settings**
            
            I'm reviewing our AI unit behaviors and diplomatic settings. Given the current geopolitical landscape, I've adjusted unit priorities to strongly emphasize defense and anti-air capabilities, while decreasing offensive actions to avoid provocations. I'm also confirming our relationships, particularly with Venice, to manage the evolving political situation.
            
            **Strengthening Strategic Partnerships**
            
            I am now focusing on enhancing our relationship with India, aiming to solidify a stronger alliance by increasing our diplomatic standing with them. This strategic move is intended to bolster our position against potential threats from Russia and the Zulus.
            
            **Refining Strategic Parameters**
            
            I am now finalizing our strategic parameters. I've reinforced our alliance with India through relationship settings, prioritizing `Satellites` for research to advance our Spaceship victory, and adopted the crucial `Third Alternative` policy for its resource and maintenance benefits. Unit `Offense` flavors have been reduced to 40.
            
            **Prioritizing Strategic Resource Management**
            
            I'm confirming the significant boost to strategic resources from "Third Alternative," particularly for Aluminum and Uranium, which is vital for both Spaceship parts and defense. This policy choice, alongside adjusted unit AI flavors focused on deterrence, is the most prudent path.
            
            **Finalizing Strategic Moves**
            
            I am now consolidating our recent strategic decisions. I've confirmed the adoption of the `Third Alternative` policy for enhanced resources and reduced maintenance, and prioritized `Satellites` for research towards our Spaceship victory. Unit `Offense` flavors are set to 40 to avoid provocations, and our alliance with India is being solidified.
            
            **Solidifying Strategic Alliances**
            
            I'm now focusing on reinforcing my bond with India, aiming for maximum diplomatic standing. This solidifies our strategic partnership, crucial for countering potential threats and ensuring a stable eastern flank as my strategy prioritizes `Satellites` research and defensive unit behaviors.
            
            **Confirming Unit Parameters**
            
            I am now confirming the finalized unit parameters based on our strategic assessment. With `Offense` set to 40 and defensive flavors maximized, alongside `Satellites` research and the `Third Alternative` policy, our approach is set for survival and victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: GHj4g5DUHpQaSbXC
          - toolName: set-policy
          - input:
            - Policy: Third Alternative
            - Rationale: Changing our next policy from Futurism to Third Alternative (Level 2 Autocracy Tenet). Russia has just captured Cologne, which directly borders our territory, and holds a massive military advantage (15,440 vs 3,335). We urgently need strategic resources for nuclear deterrence and spaceship construction. Adopting Third Alternative will double our strategic resources, increasing our Uranium from 3 to 6 (allowing for nuclear weapon production) and our Aluminum from 10 to 20 (crucial for modern units and spaceship parts). It also reduces unit maintenance costs by 25%, which will drastically improve our tight gold economy (+10 GPT) and allow for military upgrades and diplomatic investments.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: SGAQNGM9lvUgpMrP
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Setting next research to Satellites to support our Spaceship Grand Strategy. Completing Satellites allows us to build the Apollo Program, which is the foundational project required to build spaceship parts and win a Science Victory. This aligns with our long-term goal of achieving a science victory while keeping up in technology.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ZUsScSto9PT5NZJb
          - toolName: set-relationship
          - input:
            - Public: 20
            - TargetID: 4
            - Rationale: Strengthening our friendship with India (our top friend). India is our most reliable diplomatic partner and acts as a crucial strategic counterweight in the region. Improving relations to 20 Public and 20 Private solidifies this alliance, which is vital to secure our eastern flank, keep diplomatic trade open, and coordinate future joint actions or defensive pacts if Russia or other hostile nations threaten our survival.
            - Private: 20
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: KwIwLEXuLwL8AHnE
          - toolName: set-flavors
          - input:
            - Rationale: Adjusting flavors to adapt to the new reality of Russia capturing Cologne. We must lower our Offense to 40 to prevent our staff from initiating risky offensive operations near Cologne, which is now Russian territory, thereby avoiding an accidental war with Russia's overwhelming military. We maintain maximum defensive alert (Defense: 95, CityDefense: 95, Antiair: 95, Nuke: 100, UseNuke: 90) to deter Russia, while prioritizing our core spaceship victory path (Science: 100, Production: 100, Spaceship: 90).
            - Flavors:
              - Spaceship: 90
              - UseNuke: 90
              - Defense: 95
              - Diplomacy: 75
              - MilitaryTraining: 90
              - Production: 100
              - Gold: 85
              - Offense: 40
              - Mobilization: 80
              - Science: 100
              - Growth: 60
              - CityDefense: 95
              - Antiair: 95
              - Happiness: 70
              - Naval: 90
              - Nuke: 100
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: GHj4g5DUHpQaSbXC
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a198r7Y/iuZm0bT466BUuBbNK8mQ1uPRTIMhMkX0EcNi3XVJvS5jot2AFCkGL3+525tGpAw86PDxyRSu+w0iUf0QK5rd2ZHqacV9gBcMiutqZktVVMl5QZGew9ng9Bb1JPj8uCNL+Zd9I33D7nUyoznNEHlRiddx9VKrcEQ4IU05rHmgHnT1YRGzdM443W6CxialHAkim3Hi+pMujnIxsbQeeCsrASzrLIPDGPnYNqKp7z/dOAio+8FVZB7fqDkKcqU8ymkQ7puhM2/pi19dLwe/WaPnkgr/jViSS/9hC7onqqzk8OrJwq7rmv5KCqpUpmOzrocVoy5wSHxoJp1oJV3d8WEOpxOBL6vIrWVJPaKXtkmWa4saXApiwDqUNWX552AMB18Fys48CfXqPyf3unWrc5aULyLW6sG5M9WPgEh3sog3E3401/RLn+Qn8m2Hjq3X+++HdwM0hjkOgi17aULPGZv473qljweWum4BByoLx4d6Wk0zp2+vTIHPEd3XFqt6iwrZJ6BQQKJfJR/UjpuJuMGMutshf5OBM6UgS0bN9K8FE3AtW3Ffn655Z0mCiY57XiVqm//V/VJtKWYapRAb8s4+mqvRl21CP49zD8EofK7j765sJzW6FcRNeLH0ck7lKIWVp7is4/PghlRZLe73/2qJpu9vHpPFOkOrs0pIZRq9HWOMgmp1epWVYU1i+iPPPXI4HJZFiixXMrWRFijF7txOChdSGhtmETIZyrSyN0GSefe/ZEgLZ6Z/W7skqVzxVGGQ48OqHOc7F85Y4tp+ojRC0wz/NyE3WPAO9DRcC/51kuvkmfPj+WbTT6ioQK8m313QfT7PFK0mt9+Me4g52C59f7TE/Pz1jMrKhQjfz7lbMkKSu9G1CH0Vao1muF4lH2aFjh901SwwSH+L0vKGYws/OmJFkA9TTQbjpYfzey7MscAplGEWy3zQdjTuIrQlUQwnIfDW3HgxZDycTFN+rxXxcI5vmQz8l8nLzGB9C1yHHcbMOaA3EKIc0AGgUYHozs9EFWu0mp4QXfNRU4RUJSAsMaGnxVvA/H9+4GC3OjFoaB0LDWutMXwMX02Uoc3Wu3OFcO97IrZ3pR8dpnhNnm4jgVqqfcJfyGLvf8L4J01GsG/LVMgF9BeDGi8GiiNV+FryqiJuqvN2JM3AB9hekkLrZv3QGqRF5FuVdzTX47hk697id3ZgH9EYd8AtiB/P38Bvw/czVnuzc9ykLEzd5WYHCDtLPFzcT32olJrRVeuBGwOaU1olaSvFi8XVl7foVjzIqRI9sQXNfM0B4n1feacWC2BWTRjoHmybtsI3qy311p4Tq0LCBeAsJPHTgL1xbQGLfX5YSXvaCigoBKwTU3uG0DKwp2Sx+zLiDMRGw/FFvDUIWLmP2wXgzMxCYGEzIVumj3MTuOiBeCpO8GQ38ux2DG2bWhkqHjkFbATnjnJ7VlhxQPJpwebeEwrvJs2EQkw94MbP3cwTOu7Gjq8Eep+X1tVhFJ52aYZsOZnpEDRGzXO/PvZPC4K+614oQRMBPqboYwAaJt2k+rjMTqCtjJVdqc+iEtmVJzrMG3vS+Llw6tzs5OBqjI2SahDOhRxAOxunaqELiCDLmH1Ije/q5VEcr+nyHNx5O+moa4EwZEBgpR1zXXNVlZ1dYaHB4egY9C0SH09GWgICttpjkkGFCvo7l6RY9VJ35+RZOi9ttC+A9TNIUzeHiJynqKcoAh2/F+Ziqk5CRTTIe+gocYhcTvkdNAxTFq86Jw3MbWkegIbnKZs/t/fpwt/wUJ3dFYa88Jfj3qveo4pdq6PW9QKNBRckO8MqQAXQultvEEvzKJlCF+HjeEcnH/aZs6DI6jNY8oG320KBNuv+bZSNkH+JcVn86copZo3YE6U4L/C4tvIYox7T1+Q1tUO/J33HZ+TdZMu7ekDhSBPHddtoG/nu8x8ZOSDliM2IkF6YatQQ7EatKkfXOYxOkPn9c2nGwyzihFq+uhCvjW5xqZBq7Ey9hZfWq4qEpOBEll9l6BdYE93iG6nwZ2dbWzmt61HQBeBTy73/5hKRnjtXHDEN6ZrsJWfUrCNEKiBT070eOwyCzPNe86z5JIrRcNmgqHElKVCz3vtZmuVfgOMMYUbcxvUFpxTGSvcUJ5+L80dL73Rq1fOx4Czw+ZpCAtMgzMOa3xbg/kQLMT2k9biBgiX/Kscx73pDueFnFXmjP4wsq53LSpFwlggD7NGup3UdXmDoEXmpf1TKYyVDkuPG7+puxM/YG0hy+VL2EfL6XeB2/B3f3NzTu5jhiwb5YtCSTQxVOckoT6GmjMlF0tyiuq+sDsSNksqpQyeqht1MY0m2g/zEgoEhlHr1mo03B4aJnt4BvXo/tbzGfP7kdudQ7fcW6vL4PcU5xzP8/SfMqzbsDtGPmAotr3GN4QOXQidOZoTdR0rSt2M+R/c4rGa18soxQz/Udx9phX5aU6PRrXcYJ0w06d07FL7Q1EZpHRdKscYc+a0QnYH+oobzZT+4LvKuXSBT1qGuhSJ9SNZ25GGs0IPNNUL6HTApP7RKxH429jBzrby5+hz+GZ6SqvJ3QxByBrKmV1sq0x7c3QuhjwHWXUMLycBpDQCHiDeMX9pC+Sfu2rZnlPQFrFZAHfTdBKR8Ir+x4z91gq7tLT4DoktgUG+mYdbG1rXzuDv3kHquXcwgJEkrSjlr/g1oFqYIoElMOFrCY7gadmsvUqXxoENpSzPdn/dSI4LPFwBeccHAEcyEB3+p2tyhsrYXxImnPkXqpLhKcF0S51r1TB+/NRyCWuV/+dO9LHn3er4pg1ZmWm6AcQN5ob8dyoZgMUSuTp9gikoB/vVG/jMCLPX5bFtN36fhQ91fJFEkSXzVXUOJ4EupEuRyTi/5OjN8OLDSN3jTQgicFFIZq4rzo/c+1k2cpqnqZpNygDITNsSXJ9qXhGEIKYB8X0xpzvd0sU88GGz11jxfkcvHJR2nlgXksLPDeAqICdNje0PKvMF+SZ+//oLSGkzWYfWAOOwPUU7Xs0zFesyOJBVDLw/nmhF6Fe+pCfYZKoOxRVuINyISYnGXI49ur1BcmvwEfBBMfgnxXf0nA6EQb4xH1h5D9hRvW4u/7vGUPMT1Y7cOlHWG0pn8Iv2fCKm7Fih34qgHp5FigQ6bGllGpe2+Dhk/eSRI8kPON00uw9eJgHLO+Mv7CMdY+vP8qUsZ/5/EDAUvqVFs4vcauwEZr110Dqu/91kSHj9I3gkzQnk+DzLYrNxChABuIVBiH4fehoN+2rL49mG0oZaNs0CYznS6gkyMXAzm9VAZ25wMTrU8czAXpw92SURoGlJIamPApd/6375ijU7NtWTMLYEJ/9ilBhiOTfyMrF13vdkOyg91OL3f1eNtIUF+0pq9Ql6BCK8+/tyn3RmnqfZ4CCeX+1cOswq0JsHYkuTNTfPf71CV5rpNXLCUfzAqhGhjWy8yFnYSwaCBFA/hicdSVKfdhlFQsAGfJLBLEkCpqUz8aI33iKin73LhoQl1hcw7luPGRW4YWO3s73j+nTF5APY28BRPS8GrkXSOxAxB0D/wofQVmUox8k6TuucqxTB7FaOlw6go47p4jwPcIAUTsTaLvWOe2c6r5KpN9CNWccRoQAqcIBTrWRSCPncMrNNO8eBKumWn81C2lMOnGGKCeZLCf/y9VsMNlt2bKc8CiMpgJgoHpUzfzL5e9NS97WuJmqx20VvZnUp59jRo+c8NPGfRidf8Y77Vj7g/7aJeORrzFlPDXLP2V54qSubJ8NVde8tJuZOaDJTirvFQ4PS7Dindyi/CvbrTkkdON/FyyQjOs2MW+1UDmj2lveoWrUkp+wi1n1tCUVs1A5O5wAtEoyCA+wyohuMben6QYty1/qRlgPujnOpQP5BfgjLrDHRw1rbxlZbJgMGUV7zSE3+77XcO94h24WHNy/sK3KkaPQNfg6nzNA92xKqvRoT4VAXhrbwkzNGRguSiZXQZ8gRp+1x3E/7uSUMi4FeH0nOAFmO8Q3Kp1gyEgB2qsv5dbHxgLBxsz5LM6o1H6ms8Rvp4nC8LNWSgJqI8xIt5JH12tZ4Rikddngi4KRMkJ6df+YAAu5FSht5dJpFq6bjIcP/UEzqWaJaY8QYwwAzw+06YhchIabrcuVYd/n4KXlIiL4bWQfXJCN1ADeWlWGodCWqlDXSejF9f/tcDATnz41q6BS+B7ExUUIPlZwgR1mjNK53YI6+SVLgPhT3zPgUUi8570kky04GevygC02bbKaqWBQoobTXZg6eDpccltkPxir8U4lAv2VlrK45eGwCLTQATrh8icEkn9WC49SbDRcioMZkN8yDdt7mbVRAHwo5QcYSv+IPp7khBbXQVDHZhfENSR+Idde9JOE19fsnTBlGf9ElOO1GcMHhRvFQjG6C2zX5SCK/dn336c9ZWiWvfy08SaR1lQ74EcDRgOIEHKFSx930sdQ9MldhFXi344QMJVIr5SDoy7/68+/pLS2CRpag93f8lkk5bDJrN2+61qklfSeCPYHfdVFbxyBxbjY03r5QCf8Lwhtri+ZJ9Uqt3JGqVt1EoC2F8kZFYcJUTqkcagAywmnO+riJzkVV2cb4IOS1c5lND/H3h1v7KUy9HEMCJfazoICSklDQSxdlMPZ3Q8U+/IdBO5CsLMiau21yQZ09zFYUEXVaulvpK9skxnApEM8su+8yEpBf0CzhQXX4H1zkkPU9BM0sg5MUwwa3nIQ9+TZ60eg7STPeDek/PKWwylXl+a7SSLNwxfrKfZCerW/MMpHq3aaLorQiN+F3LAK9KlMQXtatXvjiIZIkOzKCqYnyFHMWytdHPZ3/qSkkQSWs0ztNhMXckNzv9Xk1WQUJe92yJ6pqZFFJMalGA3Fxlyfi9P93QGv95FxlGm+VbBIfIQj6Z4zA3ophMj0d+rvOmaFKO8Vs+7FWWOLxZsTR/S0ZJdXQh5uau0BD87xiPNJXn8AAXYKgNTSrDVdBDo41BJ0x8zuEmzxg+SxyO74M1vFCmHh/BH5ZIhvT+Ft/LYKbIII1jxF3Awl93RwrZGlb+L3CphG/ol65Mg+Soqw7YoCa5peMbwLO9h5Z34LPQmX/ZSEZIHI3u4D0ZaLwvzssKriAIyeRv2k3ggAGHSNyCKTDQ04TLF7e/lumQoRvaCET7k0M4Rq3Uz8cgvZU78NcUp84POhtVMEoqKtIZfI0OX7uxPz7MB0VPmW4AsDEHM+b+PihGHS017FH208Yc5T/fwOvf15qyEqjvEOZB2hVwuPWoUR3gVWFk0HFXIXNHXvRwG3qkl2vzblx04EjCQr80pgwBCFA4iFDKRxWP9ReAvXra/T5xaEOlfRVv4g2T42e/zjh2oohKjRQemfRiYH2sVRHs5ZXeRzo7GpUAJ/oonuuZPtQWwljL57/BZJHz5f8W8zg3lOWWxB3MZ8EgYHR6YeAlmTnAlFa88sF0Gf4qshPmOkyjdokb9LLkg2obSiGqIZUphP03noGCCQbJmj8YKD8soNlI3828POXN1Zb+9FGhVaNW8OpWp69lXtiMdsQ/4/D/iTm/uW4szI0VzhRMlCEneyRdGWhPxMOhgwZxWxcwPZuK7uIP8rPMxx7nhVCGtw31AZGcx41gxLQMrv2C61YZJaQV0vyV65dtwQXheXbP83/X2WOrNOZhhlDvIE/iqXKZ7UD3om3I3fytvrU9RO/+EJsMPGVZgcjlPciin/oi52bnipkTkA199sdCxx8sjl0u/f37bbwruckCN5x7QA79NAFVZUxE1jTOCjLHHHUp9sbbfoYsZQGOEuxd7/K/HvkjGl6319aZgKVGMTl6IIbwI/r7xs+r3mapsKaVZUe7geQTuN2bDAokKiPULhNRK5DT3NkZ2ARmRcUT9E8LJhnqdeuAeqx2f+lYvEqPUitdYe86M4VqkSq0Wk2S3i+Tsynn3RwejXQH0pwxcJ08BUwpAVzIIr3vAEiK/AX1EW19ogVSAURVY6xSoVGxohS8uQKDzj/T6ZRHgibJJrQ004qqC6mL87ZAetKqC5uRsWyl+oXi2VuwgT84GzXjVF0EtJU9pNQIpyh3pOi1PteWcsmVPVy43uBNhMD3YftolprSdgwDOUOsN/Oh0TG+xFnEIstPL6/6og+0RMSRgKAsNiXLupYDRxTyaAS3OpzGENVD8sjoFAEJO7AjzCM+mdiveks6yuVWeq+F8LgBfB+/xcmxsXudf4e8tsERYd742QMG6esTrLHpQSd55HAWpO2EWQKqq9XR9wdGROFR1pflJTpmxc9HgG7NGduUAjzUWLn9wfufqeRFAcDYMg/Jy9lKer1Yxb5+i8IYU4U1zdt1vPYYZQjg2ZvOaEruc3fzf1C0wAwkLwUVsoDPzQJIM1nSKGttfM6d095kTMelN5Q3ZD++GO28JM3GwETw9XOhimcPhjnd+Mmz6J7soF0Aq7KLwGvKDpUpJhZ/s/KFhASgzBg1sdXh8/MpIAqE2UAquVFDd9NJLPoSzDBER+ba8lWzug5RwyMflFTY3KueaF9adtEphf3n/beWObWqfhxpxKVRxdfic4MHbNJdmrQXWCMDmKIZPwKAvXoMLlVgSLsHDUv1UeVCkw3pPkUZcP6Seoo4I+rjqP8HA0yQNAZ7miJS5KKsL3cHPlw9cvCV8OrKGnB/BK8Q4uQKtkBw6k87pwsVDx1s8+M9bK61GLvQGrtMvuXBCYBJ+nS19xFdx8SfrTpdM6e99h1qtnvJi8drsUN0IZkBveqimOxkaGS6ijk6xyT7Fl9f3jtttpyEk+8ztnyHiAkjNiJmcoYC575OQZEMJpEi3d4/2GRcOzeFJsp49bbqzg5F7v79lbDJxqs1iUi1wUkVW4iUvr/9t2DETcJzYOCR+8gG2A9kBeJbDxhG4gYojxAD90zC54ve+qKM/zeMZRcK5LyjaOY+zWOO8XhZtnWZO/165+oq7xatk7aBQFpD71V7ZohTqxXnjGMBYzg79+iuyUIdeOCGX4qdBel10B2kkABkY2sTJwSFt7Ne5G23EsZ+hh8wIyIjZlg2Ssf07Plp0ixbt/E5MJzK14/euyw+oSFOil6FuDq8J9xW7oQ+MwzDV02nXJ6Uznilk8ucD3WSap23KIs+LU1rlphv0a/ZBjRpMNYq/8ThwH/Ev4iE5NriXhaweoAgr2TvI9iYeA9FhjH/LcLoLRVqBAvNAJzhGq/INeXnAamLuEkSEeEElXki9TslIwpBcmLTiPRNVnAE+sfzdosA6edx3cH46MSTgj5mAFMLUNavrlmcA9f4eRrurgkeMUTMHmOrz9mqHbFaU2cCl8OHpxrtyRYNq9PPwNKHI2BEYQTYJFSHbKybFjQh6+AdSevSW9/4qI27nU/H15Or5CTjYxGNxekCr6weNBfBz1KD5v17S8kiuSinjgIKcgfh87Ad9F5rR+7rqAaVpVh8LTBPkuZ0jbRi6RMFUYDZGuIu9w7+l+5jCkMDOpkMbCmq69fwoxfCMXDGrZCtj6m5b1rid6jG505pUIBWATJkp/wmXauBePwI0IXZchG/GpKuMN+YBjbfrB/QFpKpAJRDcuCAhf6dvySlSgJ6WUK+mhTs1v/3iDRNHQf7cMrY0Q718qE6veYQGwyUgs5lOEYM+kRUFHAj78WPC3zbqz2IYGf+Rek2A+RjAq80qm6tLrAugCynDyHJY6RGZdVe7ZPkDcBnLy0sdttAIO8c6DZoPj4Tvhk0feBv181PiikNMN1qgr1avqgHX5/VzcO+SGXKir6cy0IQ0ZYt3AFk1JT8vygN7MyKpmpLUuqE6tyGM8pmd9BFBwylwovNcCyxvfqTcpjDHZjhQz/pZMkm/VKQTowEz6VrgvXQwpBr4ESSGS29tvIzQ6xbYG+5OnVDcwWT9jhrhwQocTxvpJ0+wik/uNtVFBcdtc+ftn6VJPArRcee2z+4ZHAVWhYUegH//eunmccjPe5RXMb1mVsHGDLwD2h+ytXHg3QeEs0QqyqGztb09aDwQcQwc1YYD3MrnkUk6WE3Dga6GyLNaQUZrWOL7DNuu3t9PcxQrdDJ1kRRyCkynLCoyHmx0o8PBStH7aI+xDOYkAOhky2l+OEMLmHSPsOw4ux/OGKFNjQ+W1UpH6mF/aqo6B77uEmVL8aGPIafvJECJ5vYCOErXIENEhHiYRFGDTsm6Zwpfv+cYlaRcKRYfxF/Lv2LjZN7HX2JGGwbwPQG7QOHMtymSBzr7BfGnWaNmp1f8we745lL37vykgJ/N2JYGQzSiQA3a2IFJizyy9Ee+TMw3Gh18ZPN7WEgh4SBj9JTS4HifU3DhHT2Mq1+t2gSX8ozt+Fq3IpI1y2eAz/R2HUsrcjL4Kj/Zggg4/QX6mzYbE6CuE32hRDdkQTK8Ff8bENmqwTdxXQwL6NENCVdbC7KknbVRvU/T9uZS+Fuyh19eDAXdGF6Blt5G0Y9QxczfDHKuwflMxUDMbJiz4d29V/w33bnyX+4852C8KgVnrnNBPeVbbBoFrNQAYHKfpNhXnS+nlRdfMIh3qQtyq1dspU1Dgslywwfj3xISRkbXOcTigK95pP6GwiUGt4XFSom+5cnqupvJELpFHHFT9ButbCnHbWRAMIEg7VkVj69pVXUQojUGeNq3fd5AWhgKVvI0LLGzzOmyYSJcgO3GrVeD4J04buEcx9wiAgqKCgX56APc/W13j8qd8UyUwSkgy141hRw4Zcm54gUijJNwNh8W7CarR44ngcU2yzS5yqWVjU7yBuK97DZ6BvJBLGrBWKrRnlN5WXNdnZ3ponKE/TtJwRYoy+PwKsJY97Kt7NcwydiU9X3Kq4w9u/gKsGNsaHTio+ihq+GB7GjTogE9Cg8QNACBJDXcWR6ccMTNGHEc6DeQlFOwWVIrBF3jMQDgwwpCwSLEiibhlOwIsLzzIVw3ws0Yfvhj6ENlUeDQUfPUDgpBUW/WqLk/gI9wmDs/dAgT6eE1XczbMAALYXFD+gVjsoKf0UHdjBzV1oCYTLlRgeRNrDh1QVE1bVpPTPhSU079eeWEnXn1Vx0GpDpp9PpOMnu2jR/tq4Rk2txqFn8vCYZlveA8ZJs+L9cUa1xnOeViDGIgV/uN+qYLfAJrbmoNf+OKVa9HIC94Enm9gItJr9/Osl5Y+afjYzMcqrpmR9m3iTWCFRb4CWepNLhd4RG8K35MAHthGAWO/cTVMnD2tl7MqsxYNbsQAPe044icAjjoFqAEqbVF8QSyewG+cTPzaIfBRXsp30KpktF/UPyebEi78MH1aoCgd++A/Ndfccf0CGmowHUsZXy/lymaqPxT4pxYFvkEzdTsKENOO4QD8Qqx1QTMpOTZM8gB+54hFAuMM2/H4uux2znSUrILb7Sg84SiM5euaNjFCGpU8vJ4ADJJ0eeywguuZraOx8Vfry6MihlCsVBCyl8pCLfUxk+RGf6tCqiXlBHR+yi56Cu4qh03veumjiUC3KnL1HuofdPyMWJaV8nJKyZgDIJ6f2ACFeA5GZTjZ7wiUduAeXSjUzo5GLKnltByvhP99bYQz7L/FMl4xkBU+pxfzOHG/tvSEAFs5Qy6Dizq7V9asXrFnslCneGINv7AhE9+Uo7/YQWs76xFq07Olpx51NpltbFJlWHdEljjR10USbrkH5GjDSNXmFMmXJYK5O+cM8AGu8j7Ulq8hfWjcsahFOAXJ/zyWO0ANiteK8oJfwzs3nx57Vdbq7nA30Q+lPfjQOFLWdEA0w9n2fT1wWfYU0XsCkTQsqihkHmp620QlteZQ+igXf9Sumf/AQST8llsvIe5ezf273HULnK33XnVEExBpDWW8hEpksiBupfJGv2PsRUjEMd5XnU6DmoluDZ+Ch158+VFWg7c0A0pNO9+wK3F/Sh/t01chHe22H4fBWx/803V5HswF1B2QsONdHBBUyNnFgUljYJmDzJp0siefOE5MnLGICEqgUmOfO8H098uoSX12CKLlzWVqxY4bmhJZD5opRByGluj4ASc+fZSqb9+LH7/nWDRj+CioLyZyk9lHeBR/NgXpjwPXUdhS51dVMaTPuVV33GAPf72PS3px9/NLGnXbpR1LbfgGBdaF9x1iq7vFiVi5z/GY+jHgkAQAl+qKTzvT4Bra/7kX/FyWDao+VSqy+qPlhdJ6K1sLZrPhrMNg4IXfbt2nSc0bah7gXGTzK12TS5G4vGngf7Y0AhN/HWeikt03K8wxnnwbJzlCky+nqP9VHrzYpSKv2uObJORkxJ398u4V4LiBVi3CPlgHvCyIjhVPxZyPT7PVOfIc0q3aUcR7mxRB7hUyG9GJUfXQjB805i28AB383O+pgA6OwOejXury/UPw5z1f6Nf7hlj0I9of5GcXlxIQyRhu5tHeGK3sJLNj7PHclS2SaZjNl4DY70RcVhzekT+9sn0HVaUJUvYU+8lVENmBHWx8yz/a3bFUy/ncBYGqMQZro8LEc6E1G/1YA4/XcmbIuqwM1Wr5lIAcMKh02ks5gzhp80C+fNkTz796o5NXhEoAkWtnwodrhnIGcb8h7gPANgHSLgJe3Iraw2tNs29RwGDKnPbRN2T1fYshLkhqCX/2GmFEvOzkwMVVnRes+2GOUuyF5S0Oltg5YqFWZK5aCaRqld5ie66wKeEltamiv4CPyuq1tRIt0SL8Sgcrwzz7Hw6BGG7JD2CwyANZVhBc2bLD8LfqDCK94S15lrx4YUCtXNPp77wP6PZf9yJfPEdWESgl6fH9j+ZTnykpvc9gYouiWlIvHU4MameaT8zQkDn+ggO6sdAQM+2hUjE3HSbAjk8MU6ZxGxzNPvJKvnlFpfD3GJYTKMYQeJL3seyiA/A+fUv1f9ddWfM+6GRIO5tY8/r/JGauXd4d+wdsQVSNz/WlgYj0NF09H5ttygtiucyL2fFyoFxDrKVEjeWvq9ww5ECQw9KVL2lH+oDTXJ/UjwRtUMtE1qVO3Ef74f4xm2ZYSVQv5EYM8IFwH9m8DVIFSo9rfXU3OhI7TP7yxHF3mdna+7m4wyjrAmhqcMTNs+d7wVJ45FIrvTAmP01G9Q4XKmt3bkpSW0dTLXadj/nIueSA7ii77KalY15dX+zxID6rko2bOwMDIvqN5HcWDOCxIZpTTa1Ama2nti5qBxHyP8T7ReP9sPPAlsitlW+Cw8QRekuJL96LAFy8diFrslAcLC2V4HTJWdEK+mPuDHIiPgtnyJl9Y00M7vbXAVTGHYZDVIdbpDXpcOz3LxiksIociYr9YvDkhlEgs8U1RvdigtwvrwwNfvVGDy8QL5FdSmmclQkvri3da1I612QNep9WMEn20N8aFayKZF5ntKKVR9Dch/HcSs1VKp+99BWLoAzvpT2l6GhooZShddIsXNvlDoE8g2D8h3NXonYODbt50e98AL3rxZAcGAjg2EXW2agGHBju8ufxcl/hVnbkmMc8EwjMb6Y3D9QLRlBCi0Ic6UeQ/hVA/OjeX+iJHO60cUs0N9EAEOH0YdiU/VTdsZcV/mFnb5vKqNbei878kLyL0YzUnQojEa4645D/tZqs1msofSvBtHFuBfOMhetlcK/B8okybfbolYPow3rFC/xQqRgVRvKOs21JKDRzlqNUaiWnMThU8kF5+3c3NSk+KiuEm5e6RE1vj3cJHPL6eOPuS7dLeAjCvQwuqgweD4ZpIhsE+7dmVisXqSZuKu4s/Vje82oKY5NvWGRjZKDuHid0wRU/ySYz9h1uZqeZy4o4HOX0A/ah4Wm6yXJG71e/crJZ66cbx2TJqGj7HqeGQ9ghX04J3LKC5hae1ZKPrM8oEVpG62mYkXxjyamyKvPqfNNkcWJ2OXrfaM/IUwx9egkKVxJ0bpAqWIcczfucWjgtYCt3xOTMCBqP0KQJT7SSVBz4Wg3LcolDQrEodcyngEJaWy8KFJE86gx4mcHXj/SBXXajOxKsEz991cMb+b5WmMb5YDunoy8KNogFFFGsymy9t3oSOGu+S3pGMJ4XcAXLt0b8BS5ayZajUl9gvYEDOzkrQDp6t1lvDodHcO6cPY9JYxzNpCSw+N/ZTcoR3KvpOV/V99Rdy5K6RNQK0tEqS8FA0r8ml9Otz1LuQxXIqEVyHRUSNB2hpeHlapZZiVuTrPOAvvMghY+VgJVQjtLrIveCGJ5h/OxumXkm3tPNjEb76j+NV1Z/htWMzvd6g0MsinEDuDLyvuOfoqIplwbBLYA02vRHGd6ThapbBM5EZzTKp6okBkamQ0e24Ph2L9v+iUKVOMeJzqaoj8xN6wgMMHf6dgMbfwgVoRVikxc4K+hT4rxgCC3e6zpqBgPlboP28cBkeQbiPPM+v18DCfGy/Xew1+En80Q4N486v5d6WgmIYxWZfHucDIxCSitELEwXzdGysf1Bpw1xxpRZsDsDv+ZDPHoj0dvgmsFXahuJaqARahI2UuoExsit94qjtmahCOcLCWl7SwtHXd4rwe4w2iO9BKVLTf4e437CbkrnnQk2pPflEBAHKknW9Gg5arOwurtGPGipfBBeD5QPnp2inDYiydAL5EhWGXzj1h5vaRYB4Ee/b/02FFHJZy5SVB2tam+Gl1PuMmJ5liD16wd+DrvRmSAGP3uybeOvuQmBFq9yOnzlWKFX1Cvp9c8OZQVHVGTpVtGkO5maD4JfzNDzSISRdBUKzVP/6CfPPRy1bu9nSG0TpIKZJRNv9mRRlwYOc70JaeK5OAySO/VzZmhiEuKxEuNg2Xh0FVQ6mPCO7FkJ+KjOOi2aFgvmOeJlYrdLJA0XpCa04vBWIQoa4xF4eod4GgPZJXQ1JEx0UaySuT7OGDaNDHVW599VAVJeqhA/5xSJFa6j42yVXgcOKpmq2h1I2SzOOjbVJSBZKlUkGL43ETUDyCAVbRcDL4X3yQ5FhXVuyEBSRIjkLebv7wMnURS7LOJVLWYFvm3VGX8KKqdFTzySQIX3saJWsdsI5lMzIbJUague9Fzjjj63cxNDKQBSgvm89w5h5S3KpJnJX7A/hVfoafzVdzH1mkEqTcQx5wzDnKe1Tmq3OUq8rN+YxiqNWq9CvyW6fcPXe/X6svNgWL61GNKuReHXwcPEXxohDkXRNWT5U8578SPq3eZYu1+tlS277BZNPHXrf7mtg30O/1fsUuv3b8qis9JSBH4X1lVR1nj0TtBpkdB1Att+3op3LfVo1X4RVLVQfj3rpSuJuZ0PXRTZeogg4VavwzN6qMqI5escCFDBV4Bwe4n54KT5i9tk+NDnssR+sqXgvc4PitY41Wkz8Yn/HpSS+h1HJac9A0SO1PaiYZAawaLYJoz9fZabvmPZgkRCvVK8+RnmyiNwo/3unYrGoFxEzBs4gRD2LZVJ1GeItoNcdyoMTdqi5XZsnVJm6YliCKqdfZUuGpmHAfZgH6gJ3uz+bU3UZn4uuha++AnAy1QrLU5QOnEJ3oHOVgSNiEKDHnIlNsXCH3uZ+49KGCnNnDTlP0g3mMVQpVC+Peuf65htGAnWjZ8rbEbT/iXwPY41haUeIsKWA7lOvoE2BuakM98HpEP7u6gjMHYi8ik9iEUYrqYvER+IFiTstgUN4kVL7faQ3f4+NrUfSJOlWZoVxsI1CotrSPNHf6iTC8MVhhrTzqfFpA0kx6reoZF4AjjqthiwWFIdBtyb5+g5XUwtK4cd0SyhQMXIBvt1hMvY6RA6wXdcBIfEJX1r0/gRi/YntCh3+lUxy6CeZCSM8RgGrZA5+4H3GLFEn7iFG/ok5arp7VgE4u4/3goMRQstYjAFlJc2PYrzY+y26/cp+250FOTWcf/yrWH3H1XVhI1/VhaBHAk1pU4eWz/Wp5EFCujL93bdUwl5ajDI3AiOA0U53l4jYor7sTQOUNkTJ7X/ovaUDM4gFfLVtJoQ5AW8kmWueBfwFYjfiXmfWcgRC5gS9vEW97Hj1Dxo++eQRtvVkYTbKxjX9CVa5Ed0EsKORFHvUPg1POKmpKrRwOV6VfBLgozNsl7jU14SPWoV5sDD+lb0bs/+2aQUD6bLEMzkeu9NgjOVwjx2EcqUF70A8NyJBcXGcDDQ7aVnLBNLt68IMB5O7p/1gM15VJ/LRPjvw4RU08zCMpfkCZpWnrLlUAWnlS1iJGSTL4+ZNZGDC/dMpJeCYv1pnxAu7znburwIyjJzV3Ms5fQD/2u/UzV51Q3F2g3ODxQwUvDvjQYlH9GwOF90FbXlRZaVxaznpxmLhePG/xlzHxt5RpbI2yTQqXbd0FkI9j8Nud3Uc1nd/CS5x9aPI1/jyIs6VgETnXZQZLl99YfWXnk7xB6JlikKMr7q/W+LwjPIHflISAp5S7+m7W8kaBoprcfvLnXXLigBllUcuY579toFk4Hq1Xm0GyGZmlrop8/Bw//yvmvnot63dxlhgDboBPaCTl1HIjZQcuqPBNFzt4gTZL22mHDKT6NOgOUm8SFl7LjZRIzIv2uvF9cBYyB+OCi0+4bu8QUt4B0xHy7iRbF/2L9EEXc2H81Fz7AwT/v2mZlqH5PywOvSztZGdE+dbAr66YqJ+vrt9//54IzyxyXVduMJbz737Th9nyUvFstBM6IxXQ94LvP1ZXgttCT+4Gk1bRD6B2Lp6Ec+0wflhnugoSWujxkdHxqFvB73d/XQsBS6AeHb+61meR5D/7JGBg4/nlscGDmlax24flje9P0QcdJirI/k6GrVEAh2FBPg4sMU33oVh4Ds0ucSNtGJc2pGMq6x9t7Hp29VFETF5imcUiqdbwIINaUWbKqEjVRZqAFCEizog1CnL/rlSpCEJqfIzJgGVT3egN1J4lqwnWAGGkhK9RtYvHZcreWLm9kDzL14WUeHr5RDGQ+tlPve9nb06TrYdcqDRU4hbLuknZTRwc/fl1nhfpBkGtcWo5RZas2exvfEccxdSKcVMnspl5Oj6cjomHx/fZwFfOoCixgrWnUzZuJD+G/2jDQ9c+p3X3U7Sbb3f/93avnken3/wzfkY9ziYyCEGELjv1K0U9dwysjq70RRTvo89QwzbJo1lQdFQj3eBYijh8HyxgRw4/b516hap6LHGVYZqHBECtENPFS4Hp0yn7xFKds6dSYmvUw0pgq64d3rCjJUJ1ekWMEEgD31i6VB5P4bJBjAj7ZVY1GRadLc2iKpQrPAksHMr6cAamRtQHNzJ9f91uWJYEpgJyBAiKiCo6nxNcTfDAFcSihI/83ecrd7vNgJ0tk03WwXMVdeQbK7OunVZYk8igQbfoQupXPZm8e9uDXWvuBUrgxWTWkGtVRPiZQcxeXxszcEHZmjYojql2v505B9i56AUKG/TaffSY8fhSybSd3eGyUJfDWMhW8Ypsnjp8Cz5S05GMiR8oSkk0AJoi3TBJ74mjFNrOt+QHDyd4yNjandhJ6spZil7+CuFis4uePjIsMYWVua+2ZctAUH0dKzecYQEo9ljAiMcCO/rZbALn2UetOeWnkJT265IZ0xkdRNna74PTKh2KBHehzZLE/XzsMHV+EIPgkATyFsQcLOw53bYOenaCNn96owfIRDYDcpNZ+artINn2xD47P01RdySeoh2TaePzl6WVLbhX3Rg0n3JK78YGQVRCoaGcH2mQYrajQoQiH9iTGaw2bDhf/9k2Es3olgB+B0nINYFrBVxXgD8lG0h/kpwEtmgIlDYQ2YUerZoz0xIalM+3G1EN1BpcofHPd5k48DPg6+A4AFGJpyQm0YmX8VtfvHPk3cY1UKMyoCc9F5uguAqA8MriW25oewq3AkKOgsw1D9hLgShEzeBdd36hWPg7efvC9hKha1ER2LMTtgI2zDYtDrxWTRJ7u6JGghDO5Sa9rrGg04817wK4Ouoq/H8UMVkAZ3muC650z0pvh9mCtuaMIvxLiYq5CZC8tWeBiC0GEOA68L7zb7Zq9vmUN48NVA7grY/I7GcTna1mB2Zscg19clvExap0fAGWFUEeyet3ypAF3Bd1yTFcneM1mPFE2loAWdXkZ5GeBMYQX60IJ9H4i0cSYW4ehUV5l41VoCp5kw4znfeK+aqqblFc367AGPqpiVrMVT0705MffernXk6qKgA1HoF890WdEZmJVyad9mQEAYhUf5LsUkLMuRGWNIpk5t+b2Hp1onkrx5f5vKoax74I0dW7Zc3PFpsizNYh/4EOg9i+6IRzfj+nbQjwqNqURtXE4aN7JctGbU9J2lAOsac8ePpB2P8z/xg+woqZLgGw9/g9FfkNgS49fNKwUPWvNowZCLUlGid4XDin93Y+ZN7S0zihySx/cHGlytRWHUVdoS3sxalEyV4jXK7bHj71yXFkky3ct5nKiYp2XlM92zPEZ47PXb1hMNJEGUpCfJzKMRBjqQp9k5t1n69I6b+Jc5wCaujiEGeYtp/PehkNs5HT8+9VxTZ2GUeKTIxq3c+4hpPVY+PvVPEulzk4HW9kcmMNikaz1S9cSVt/MDGbTGi9kGQhv8Utj0S42cZU862HCm4rSMrAybOrxpf60lLgq67jasPQGMvzexIi4Onsob+mg+AxowRsu7wIXGGAzH1KZvKEdUUOCiB6A5YQO7eVh13BYlVXZg6kuMz5XWM1smy0WLKAamp2TKG8XgD9NsgfIXraDLnAsWktW00RIvngU3PKC3OsoGjb2X/+u3tQp2WNH6IjprSBkbz+2ozBFd6o9Gl+tc4I9xMiIZGAaM70pQVNSGzPQS65LD7uaTx6q/567E9Y7u3zY/p1ngWJAgWXDnWnb1KQJATRZI04DjlJYUmWAYJUAYfl8XmbKtrvGu3pd3YvPZt/hFF6BzKRE0fq4fIPZy7/lq25uEPo3mfT4QStpImkfQZEwSrgglqydej6DhPgaueos/it9wZTlPiRhdxgJ1Y/KZpGPxXRJ/01dQzrqoda7ralEStcPOcZ0IBby0iiWM8UqD28vuLh9eK3KjDqN4ycBE7aYCLABB322C9/RigTyQjy4/E8tpL4F8ZOWI/ONQeL4b/YhHcBoxbRlz8sIx1HBH9uDv4LaVINkNRCV5wPy5G2VGkkiIZMvNH9liErw/Wk7I6uaq6EkKtBdZHlRu4riUnxu/oMqzpBh6DRr/l6nZbV/cNVuUqgxGtiHQL1U6QjxyRukBMSyCPRo0+8W14r2QHCXdG5Tu2hFFCO82bjQVCfshHQf+bRyxv10w/EuPyIzWUHqM2WFPDvhnualWm6Pxne0ApDgh3q6ootc3hZQgCDsYuab6wm2MjUOroqfF+ABh5R2xNdtlF6I28ObzJ/BmPZ2Rl6SsO7UzfVXO5iV7GnmtCcA+Q2TYywxiGjJvownojnml72daAVZ1cG8eI08NC4qoYEsiFkFIU2nLcX+kNny8uUHGQHGkmUZTwoXJGx0ZC626Z36NgpfQSTrMiYI7EXnm/jxKwZScF/lw/8ea2JXISUzSBenS31jfVr9fl6ovEhFU1uivqUbMd6rnomaLqmcZWG7x/ZvABr3umDRyKXDsu7phKYyOn8gOVO1KRfB+DayvQMbVRyKjwgV+hHdYFZo2UE4Zr6loLQz4GF9pUDhVxGtP9XiPQoeSMUZeNdycZUDbGIkijG43Rkxv58ZZQurZlHCJUCEg/QqNnfawvK/QIFY0/2ZRRqY/0KZ+0sz6+fe9/njP/Y9d4PKXE76E0W3ZrxNpwTbz432kARbVrpaXKJBD4+nN22P2Fn+YWS0+9GEaA4kNSYX83M1UoU3XTCzWZpGia9HZpPwKeZ71tMtAm/nNXm9sqITxD+8A6EGLFypekLgw/jV8BMStLXTgthroYamrCvpaFknNf/BGqGy/i7hCdwK9x3RhouzJ2rn+j0lQT6NyfebAfN672lNq8dNS7Xuy4G4w9JXiCFhyjDc89t+D2OdaJdLWHBG2u0eTpSywxbd+2bJEdxEedX/xiBm2ZN/CTHXcP5vS3+UmPrIgviEC0fAFN+Df5QzqcFNs2Q8vGJ2GZ/4X69Zg4p/ZLOBHJC3BVd6DjUf3/3gpDZWaIyKV+n2v2uw9b3qIayimxR3CaF9eT2AIcyLsYpAmqoVYAN2hDMUXzR7hwTM9Tu73PGUpxduU3CrTpKGtjw4CbOxrj4fn4+ZTqSeBfmC47iafRL6nkjZ8indWgIL6u7l2KvwkVyttNBRYqxhCi4gEwebRQ95RsaP72EMtB6wz4ZWQwhR7nUVp2awkWhtdS3782tSqcYSU7vm4wI3Bqd0XuCOw0LNm7azgypSVCJIhXIedP1p5w0GjmeyRKUWeOE+qjEfE9pOL8zFSmvlAIDO+O7P4JJqmvgeeoJkJk9xqiTGVYEU/s1PbM3gBDXo3ribAvP1OD5qG14jxXmTETxeJQZv4A3vNmTWMl9cS3Uf/kWgslL+OSV2xKP2aezn2DiYD91VeWtprBue/FWWglc/CljrlEyUfJjmBCpIURMkXXdWI7mi4T7lfhiPZa6sPo7KKkU3mPxuVDbaGTA1EDmaY58kxv5BhoNW1VH+ERUXrgq3MXz+nuqzdAYmoE+Dy1g0m+RwtHFFhHJJeomUxisM+9yTFLkRP8xdi/NNaVONLhciELwYUvmZ/GvOTlc+/0MIzQ3rlK8EUptgpFN4SyBSTdWTH4B3BkHA6btaX0ennBzFqa6essYMYZOIT92Ze0VcookiTcSEaSsBqjyg7q73SpXYTSkouucTEh+UdSpv4s6C68tFIleriJzeVgD989EGzDaGyzDghmS8EQ8kviz0Ymh3+NS0N8w2fNyNITt0UgncPGqatoc/E6TF5vkynMdmlUeDmJvofzrDhhMJbLUktWmzeXkIngztRpu15iDsU8tVKToXIyVFnpgAMCbq146w8PLiauJjdc66JBZWdCO51ZQenn95RngoMj50uYIuHAJpr1CbVmyi+HGEj14jpUmhrEkqYUQH2fnmMHK56XA+zWlQqeFrMKwBiSNdhAEC/GJVMgAxHZAIquZN2Bs6fskegPZZqvsWMkgULnifbiWmv/0ihV67ZBNLeCKUZ+Q5X79TiXiy3n/IKNM/74KHK8Rn9HkMZp79/eRkMO44byMbh0yk9t4MSS6nkqA+NzfoasPQWjOXiGqE3OYLcqjLmyMUl6WylzylrxaNhnwn40M9eJAGVXOydWekdUuQ3UW9VhhSjZnfSxD0o/rSX6EIqvmxujJ8/pMAPw6MLaIr/drzNuZm2ychOLUfL6LHUdI29XttXk2UqSvLLEI0ly3wIPLa5Lkyw2pmhx3aDzI5gZf7+XqkmsuDm+f0pzE8ObrKE6wtD2KpCWI5Ug/6msdIBTw5jgCcfO6aNiiwfQp8e/clRcp4oMcDtKJ7IKLVWhWsJN3eBaEWsrFp79gBTnmWKjzEJcSCqw8Bs3fX9x+dCYTNwObRn5RcoT6F3KHhpvdra8pnazUdn0Ae9YB6VhLTxlSwqAO9EQUOPr7Qaa/YZvkT1GdBWj0stdKIhIY9xuCy0D0/Xy/Dmx+/nDHgNjuWPFZmpQoYuTpdeqyKJ5p7S+ynAB27ggtEIxaNHmyQvZUORxZsI29gNYEr70tKAAdxwHYNwPsze2akNIW3Vsk2mmId2ODQHnXN/arv123x4T/YXHNAvZzAfr9Iband9WQQ5gVp2tcGMTzPyXOiwQhFT8Cyit+qt2GUIgZr5iOhYZmgA+YUVcpLaA+0V+QqUorv7mM2ppxyj5bXCxJBrUr9PWdO4VAyO6Nqpt2U05towZk0AtKOCKsUSpYXiW8/nN3mSAC8Yyyb+9xhHgzpCNb/RoHn3aDbdm4Xx3DeYGLmDHqcIzIMmq4T/EaaKiKS7QEV6f6DjB5qWFS7pg9/s/+5bkeaq0+mtMB+Qx6BupqHw81DkRO00ZAkkl/lNkXYb+4l+19kjDLTxAKWw/Mu1nqVPnrvHHjCeYIPWAWsnB+j4wayeyfVecT9uFlIzSEKEkVmhY/BVLaKczuxBxloRxsZ9nNVddNOmv4vHZVDfWF8cLXisIvOW27VCOvyeYBJhUoRErD1yfAZHYsEJ0oMv9XpVclqhLl0tzVNEij9i/0qAuGZ0FkwqCRubnaBLfliPXMDupwo9+BtHvAYNXsC1lQZ8ISkuePFuZTEpPkQ6/him8OKj+1x5rG534P1e5O/qdjl8AAL9d2Bn1QnjTbfZ0IKIKPNotNx/49dnZsSKCY4xP894tXvNMf2exbdzIn9pgngTb7whL98VXYPoXMhklrGJyJR+rWEmmOmIQqEXcbfHUZkD85FMm6rh6GTcPHwTcI+BXNSJD34dPCp8I5HW8rPpEDmZWrb/TyMkpPlI/uKC2ZNU8WN1H73Fcy8mBjyLdzl+WoUrO6w6w8o2SPFvXaQ57MMVAvCbNnFtFoWDHQVGSUE/oAAdmSyWJ1KDOEcTKkwbpwKy0YlAdplh27piH5Gu57oVjWIEUa1KurbIHzJFZg0UXr8+yjJSRhGXcVcnr6mBqFLHaQm8WAT2M4L35HgFBPTHV9JvValkUu9SWnflkfUPcFUi+omqVb8XsxdGN22XZOToyD18D4dguNX1JKai2oKLfiDAs4+9qwPlLoSStcgsNYjoofaJjQUt+up/vVE/hf4YAF7C9xi9YsDQpILSj4hR9CsQrzw3ErilbLXzMnjILTuXmpG+a+C2cMNSs6vZPrc4sYRswdp0CRmzo4/zhGUeUNayAC0TAVKGTgb1wJsaUt1g7LOmYpidZA9lAEvOBgzJnDDoEmOyCJhIY/uIS6On8IzA0W3I2rWumTDra8pZKisV8tk4abCJ44wjCZCm18jYoyqUMweBdijjy6ey12B3L7sfXu2ISxMbuiZ/wRsXYd1P8UVDqN2M5fWImFw7suVNP9BpTBY48/H+bJRdNGTq8iKTCUkcOqZgFXo025IJVd8IjvUH8gCBYuwrUTUYIa4mWDVGVR4L5Xj3URk67DNCocMVkFmqol9bGZ9D+W5Jq7SRylBj/Q/FTkFBmBtq2gyuo9TwhOqe0TRQAD2Jpe7+6XnSFh6pQP1btz6DchS3x+wmt5CsVomTKc7unvLu/VR3lcABEtGxOP57R5f7+Q+B/2Z751bP9uwF9clyXNmTcJxkxdn94VqwkSbSjfW8riWEqzYEKoR8+/XcyZ2VThQXAVba5TBPX/AKlGJXj6KJ184pNmCSK5ExtJ2q2oMQNnHbRrd9Gyi0t+A2eU9l6QkCgsISHJ8w0cMHIcoNRElLY0ir04cB3cAMEYqG2hdvqGV1djWzLDP9xcocjOU0C4VxqpS0S8hZ8C0HOKCeLh38kRTb1hXXb98LxwtyNDsf4qSn64QD4JsG3z2O+hhItc8xCfnsdl0MJanmzrf2yi228pVidLxnOK8DTvGOfeVK303Fi4gVKqLXHbPUfYr31y04zldujOfFb2QUFVc0SiUN4b6b4o87h3eiskXh8UnR5HcTPiUMplxxE+oWLhucQeCDcKm7QyY78b25gTvYJjeTLwmP4Z5MUQ16sdfWTvm60gJiZRqPgvKo7EZfp9AmtH5Q+11hzS9vzfs5XfJdQiYcNWet4UwIdxh9b4R84TBnhrkr59bvlEcSt+a5p7c3QiWIssQxFQNvXv5kWhM09hC2P+Jvr4ZNvc5qTI4qHvnFUUWMEibdg7dykEgb1W7wIasJqNIvzw9R2JIQTujIaDir/EvW2LiWPu0zKGiqJW1dEttyhdYByRHY1YT2bDp/SqI+PPEpR+sfgF1IBeitE70dNBBrb41hmJ8W2CxYBBw/2HE7x+yHEKWPISznUkhA0KY/mth9pg7iOeBbCQd+enftbcUbb+VQv/cgi0nwG+ZbfNW7jJeI82HxT0wqI2EKCIkxHGiKaeypdVckjddMnsyVCPHnrW410HKEDvrutyfFBFL+iF0jNcCJ7E5p8IC0Q1LQAfYHosE7OFRwZKkVPH+9OTHtXdw6eT6/mt0IO/8LROA4JWeruHYYVLP0N9vAUQC6DeDTCZ2g4w+2jU/Vh8nV2vera2t/FgztNLI3EgV0TiS1kbeYnuAGo2haw1w0pxYy1oeuLfTXdLMm/xmsX6hlQhNexLXDd1hPJIkDi+nhXhFjOHZJxbr4+gmWIiEkOddtFdMe71a2Gp//QK53n0Sbkida+pIGyB8VZ/yqu4UcAEgMfYyNmHUouo4JKzhangCD96p6S5qnb9kyboHMOGv4fklb+TctNveolB75vxykZAt422jfp6oKa7yCFndZa/ryHHkyxaE+0kGy7+kPad+I/fq0aq5f0fbwT1gngL4Laf68aq+4XdtQyimvAZtfVkGpLqqxX25Qtb4pPHvKcWiyQdGd2ulVcpVh+yhoaBmVH9eFuTBd7xFYmhsjKI0HdxT3Qo0gssnIKGAQgG8zb759L7p4KAb+mxmBPC2hv3DnxrECsoLM2s/3sx4lZw06kTUruDfqp+RMdStPwWPNNH3IrEOAOA6izG3FHHPy3Pt6MkK5Nclw4nGPwDqx53cwzOSVfbNLsvO7X4PJ3n0SB6lUADxP7s7z5JYAeyhz0gA8JnxKrnPnQE8GqjNACi++8N24OsrzI3cQ8enDXeKN8cNsQW4lkC9YJJ751BK8VFKoWANhzMHaE3fl3ZnYpnA3ZrbToI1hI0V0U393Dhw3JaSSDAkmnU2JnzwYKauder2wOVSff5j5ds1XrNXw76T8wtb/XteqmL+ey8H3OH57cGOo48zuKKbrU0U3NUUOdV96YpOAnUYVQgMj3uKDdYHisNSlY8mJFIj4NlIpOS6xqdV8QZ9gkTm8lf8ipQT5Ily+yASfNE9d1Jkvjru0DnotMGidjOEG4DAz6UWR5uO2Yca4PSYS8finesAeHCnSkwDOJiM/vxiYLG6LsZRvq45PooUadNZbC02q1wIEx9DKcOqjK7Ycrv0J3NjHYmOCqkPUuehlkfG4lpcMqci8cziShJBYaiDAPONNm2hInDLdBuOmdvPP5nTF8HQVuGRtFGAcONWptMNN9JTWrl16ih07H+LvYq+L7Bk8ofhLMIrwkJ7aL8ifjKwc5n22T98cCpDuJ/evxduxB8iGnWHtQMiKnHmd/GQWXMKc5zZhsuhj/jDmQAym8lMPxIYlnQgooUueJhUdXgJxtVrCkpHE9lnldhhk5bDJun/vxQNx/K5W/DVuB89UiWX98feDpmVFUjE7cYOWc+YZJqU746XRX02MuZkr+RC3FzR8JB1Z/CHD2J414a84MYDbF50TBBxxKOIeiTGLquDCF1A1WHg5MxoXCRQOzgEfqTEr9Nzlf89QRiFvpDQt2vM3ERx1H+eBD6qUHXzQQALR8qXLkbOqB67RB7A7KEWoDP8UHmVR+an36KuoRGBlPfj0vAYAb4igTm8C3uUf4RAca49RaNXBkL6Ikig5girOSUqeNYi+HPdeYzeu3UqB4P/Wi7+8JzBz6ZV6uzA9V9/OQby2j/3GSTqKp//5iIcFyLOF8tpJuYQTc6Zn+YIIycYLIPvBH9MM3knNyF7awDyDFpZ1lDlxt2x4U5uy9QIiPLFZZqWlFjZZ9+OGldM7cyHw+GzHv2UTqD09lZaYFjQyMb+LQztIIXP6q3WL0xDMqVsFU9JXWtL83IRhN65xSwxwh9eM1CovGPHTFv43L2CWs0hRJn1nkvlKD4GHy1bgbYnymWph4ePt6CpDxZBXCKL4ncH1oB8feM3IxcaVnytBZ5n9UWQ+A6uO5Mks30U+KQPACCMllTj/fx/61S1CELSV4Hv8cxRbm86r/fKjH1qghEZRFBSG/ZDeBUAC+fMdaIngC1jSy53VCDV+FDMaysjPlGjcK1uJ/32c/JMwfXlbi+vIw4Aif2zxUAa3R3Mc0JQdkpEy0Y+8/85G79DAzEzaOn46l9N+L8vLXMCfFlFSAkTO3aALtV4KDe63UcsikiJRG9FLBpzkxOXRmDQrpxl13dFAvONRRxQpNsaYnGR0AmgBdtPP1a/dLqR5grRLgq9HTpqX/QRXPBqT6/08CY30ulPorf+KQIFjOePeG+VZVy9wWFIHsj59NjyYlN/5Rp+T8pfzbelReJ72zEhgR8XwLafS6gXrrh6BQrbRKrayr0ucynB7zE4+NWmyN0uLzP4i0LDN+O3iuxmh7paBYMXbnpAA3cFtitgDcWpUVhNa4Uht349LyZ9+oYk+2jcjNUG+BqqkTAIf3rdzz0AMebjwqTlY6OYf3kbAllLvd1xJj6sUtApEJyWmogW/ugn0hnCu7S6Tsg7Bkhg50bwEWiKjC/rObfkrSMGvj7bi2t7a+5lUR+R3GwI9W3TIgU7X086qURPGMFs5rXKOsDJuyEje4SJWYPtkj3hSDSTZBET2c9os7BOhrYgsHwi0l5mT1ZaZrI/W3LKcDPFXysaISzz/ZSpcolb8c1r+0MR77HiyUpZ6fVFFxDOPMAqnDaT0uGzw6gofBXERo7fi+Tx3y4nSR5ZAI7nydbCYqKO+sSXpBcnNTVfqSdegWf5FzzluMmdLQFNnHBWqOM3JXK/sNg7JlbcCuOfCIviLeJozubwiH9EL5GRaulIhrVMnUh7R5YkHy+3T1JBYPx3dhsFN4Ir3vV9/3wm+5JIPMAqpXTnhVvvm/vwdPGTx7J46iCa1F6fzEaJ6xb81G0c0aRQEWvX7PDJKgqYvPnXckfK1dnhp6qnnJqM9xrJjMOyy3pFWe+VlTYhr1Eyr0uCk6GNa49GPbQta5IJDhr6J1xw70s8LfaXvRTxVakZY0gjpJc/4x5Lk9FpOiCu8AA5hSNXZtzCi8rSVhCqVJ1oKmEhVw+utN3TfDH801nT2hH2LLeMUklxLvP/LQAONilGzuo/oQbl3BUW9EBJXUuZ/Z24IbqHxz4Y8TIOnxYkfPTcOjoGCelW/XAqaiZ4H53vkym7JHxpQqEuoFJ8nz2GajOkY6mOdZIhkfr2H+Sjpx0Dtd7pmYSnU+OzmG6fC4Cp058vBd4e740nT8Ajm3JR8oTPukh4WcnNUE4CIzEwG+TeCTavxX7kibiwJBwmmaRKZa/QIMkQEN9K5XvIehNG1S4B/mG8pz71W64X9d47hn305215dFpqAF3s9CWFlcliS00/yHeq3M0Hs+Q1Nqbg4Aif5kL4qJjWyIcdIbyWkyn8nHNSmYt6p30R1p/VcgkhJoeS9TbL0PH6oHjAcA7drUTsj0LbtoYEQMNs4HNTI18VbFQHl2QIGFKxy/8YkE4a/hkoT3lg4kwEgUawoQLxoeBIrhB5f14c0QTFuYz+ykMGRsp0N6p6dbSKlgPop1iEim6p93VMKa96mbwz7RfVEwqLCXuZIjO9AK89eUotcztlyfLvjstEfkDfrzN9O1W6EauolJg7drIko+PZzC0fxn374wUB2VshdpJ2e27FV5KE+NCh6Dda3AhQATQoT7sf70GCCzoR3fHRc0jxfnu7fEKgOLDnPv5520ZdkqNQFnMBQtKVtOe7ZD8pIcwdZs+uAnW/XAIcio4OuDyioyGY+rjykMBkGFIFKECsk2by7sPUaCZGZm6QEZ81mU9dXXyv5oEvrVcgunXpFyd9fQKl+/1tTzlOpc0gOmSM7mzVliteE8/S5cHo2UBNmWNyIPjluMlRxNSk4zc6AT3kV5JcVrf4e4zqbfzQ/x4TXNH7Diz54JpSv5Mh4rCIlIxB/KRV0f+PPUwdQVvdqwNOxF+qyjSDtUt0RZizD4bifazqpvjD3Y2ZFNj3mB0jgXrdVjErrBEZJPnOsiuQSi9Hm5ORjBZyRuKmohoHC2hsBRb2C9SA/qzbvTmcYieLUHerAjYg6SBCiVr/GaVGyjFtDRW8dqUpgkSIjWr8ZJ0cI2v8pq3OGAQmvS47OVfjc7yXu6djBDCWVhhvxKnO6f6hIP9x5xwH53SMR57yDqJBE8QJWILzgghmxfe28dO6ks0I/tHte2b6pkytoAPgYrAGKWS/YW/HmmZc8ibB/4ja2jU08XQIjDs9XklqhARAmXg/iGdk2RZh2gVOsjo4+97fytI8UM6nCKrvYOYk1yHa7ldK3GyAtaxBgNDcjb7p+obmTMt1gcU7skl9bZzhsD9nNrmoM/gL5S/lb3DFqmkd52pSdur/PBURNP98NagjP3i4G5OrS4hYqIwrUZd//Ua1jkVo+Lg35K25oSktqWNX1dZSS33dlt0RZt8ew3yeg1DjYeyRzSg2VNBdTlAnec2eCvvBmPCaTCTUhFBvXmZZiwc29IAFanvCrOfeR3UD7U2qmd//uohUDwXVvpwjr3gsTcVv3yqArCi/WPvgx3frS31FmPtsGcCUPuJgd5cnczBPph/3AHu/cdrvYCsY7OEYZm1rRrmYUxI3GpgERoxPuIjXL1S+vwx76mqhmXekTf83XcMX1WpYeGuog3xbTWor0o5jeCExh8bq12gFWbjT3JKWSZLiDiNo08ji4zjsxBNNvlQYtVNfFfcbp/MyeKxM10jtGG6RLVhOgy7BTQjQpZCH1gQSZ4VaiXRS8PkHvPQyyheaarxl/syIbi1VuWo5VDnlZ7Gj2dggtu/pQ27fDKAhm7pQxz9zMcPaFNDR+dRVRsI4OGO1faF+u2dA7ProT1l5yZXwQHt7PsrfbOL1c/dwJGpGKUqZ03Jk1LlbN4fN6HzhzP685TQ+3ezmPIyAwiHRy0h0cSLNYAfBGPLvl33m/7Rp9GCWmJipoVP971L15hv5ZLdyjbrsNDd2fDM15UqIJDIAMiJDqE7H/taqrd604FqFtkfmhqYVr+gYjNptncmx2JBA/6ckprZiOf2gQQhT+jmB81GPcS4ZZmZTUawnrclEtDEyLfqYliMztWt8M/Lbu6pNeymQPfVuFGMIlELJMGZq7WiiO5m/TS3A7boisDhCHG5rVLVRZ0cQxZJ3WMZliVUp6H7MV1et0lA2k3GZG/aa+5xfKyom9kE1MMo4iz5tvV7U8Emlq9TCOGAAh1eW0DgckfngFyKUY+aZLUkkuxCEab6nhaC3ZD4ut1C5A5rU3+hw5sBvr4ShiWMKAdPGAsYyXVzHTAXHVttqoX+c5ao11nyWfDw7gCZAE1TtgJ175ZehmYzACwgMcc8lN24p2wDhA7RSb2ZrYi/1j8mzMDDD1/97qpM3sFRwQ8cN9f1nNPmzArrEmZqerQEqubJLq4nv8B8RNX3zJVBFrYq7Z5KeD/eWnWbsTQlBSIf86qx3qB2i4IwAXSn0dwrlmkmx/eBWKQp85Vu10iDeJMteLzs+YuvCds1C/h4Mz466UMZEIPlccK9EuoA5XNCla9S9/ZDFFk/KoXBN+Iz7Bj241ZTBDbZlAbPzwysTB8up9xz3wNby929syXtpsknDrT9y1OC42Lwaoiuw/ejw08S+sH54Ggyf3nFGeAW4MCql0oUoa9v4YIuLcKoTz/I5kNEZN45LuB/AsVKIb7Uq2Hv3+iBib6ZF6gC5kVap8c1NSCWmZKOo9DaQ0tQa8J91nW24ds7fjuM0tm99vNej3hD9xynZB4aKy3NBUbS6KTH3KoJIrSaQE8RvXo7J8mCq9pc8pIha2SKcq5ynbfM8rLkIX9Bec2Aa9Mq+TfOB7ckdJd4w8kod07G83/zeQT/qw0+YkcXIOn1nPur5QoIqhHZZhWP/Km3aKjcvAKYIRhiebN/Gpe9mXGNtb2PpWnxQm2hzDWnvP/XYBqKmqAAVkEE+391/eNsrEHyLF68eJM2/kzrkcQXNyvggqC5HGBocxT76lOKZ4mIUhNCv6869qH69n+k8lfqMxBON0o56y6c/dKggYhx4HyB2UJnHbLo310lZmZK/HdImmvQKIbcVr7eQm/TFWZG+VkjpGFFUkjAa5bnnc+2GYB0ThR47Io5Ikw09v+zDD/gGJ7VDS59cLNX2VieLzIIj8bKAS4cB8jJ3vEy34DX+QmeHbstA3goQlQ1yA7/ezSXCXJXIPDVhEfhvNi0mP+o2l8YtWbnjOItMNsLovK3LkpBnPCyLvyCsiZg93QWiNqAAsRn0WyMcmzEJCl6ayHHnYhQEFLaj0b7gm+8PkoimImi1Kiadr6nTeFPtwdJHEjO+uFSX95w9BRoFLkvVcKhS9j9IXsBBAnm55HNV7KeEZTDewseAkXVsRlHEBVf7cBJBB72TxO7LfuDzCoUS7fZZA6zDhdl0egDa57QpWoq7hKpatRcWRl97T8LUfIyqDEZRVjiyljgVawL8ZQSrYx/B3j4ibPC9A/S6b1mDofwO9dZvp2SlfRfGxwijgE6fDgJqzoyb35ph5XkPWxsio/Wmh1xlHxYHx2bXG1QnkBDtClXD9xWjsJ0KbjZpFK2wdcBGPZ0jeHoCz9Eh8KTMEgt8+VwuLETBlOpiBg8MKuMRLGF7E3zP5E6Nz/9lK806aFA9OtDCfEtqJFz5PfqWKstD1SaGE2vouyIhXdjemxyEqc0DfaVb/OjWWebUeC8cFNylyWUrT8/yUjIUB5tK3ZA80IMF/Nd2IwLgBarEjD/BSfl7bF86PFGMG7uyO+4R+qPtwyN/4K5eQczmN5xFYwv7lnUIfmP20/zAKw12OLm2MeVhG6eXqL1fUxCZ1GPe5tZlgEMEm34c6Po5zIu5S+OfHeHhl4jAoD3N1n1Az+/7gyyh5SqAiHCXQqcZTJrGZfnmZDRrI8RYI6TIZwOoOVZQrYJPapYkHQPt/WCwx3LRmOvvWGA2N2KWcGG40N6aIIeuw+WEeu98GYPQoHlB8JDbUzN/BRGd7f3/eUjNER8il3FCL4dsxbdntlgTK4765nlB/JzUXc5O/DllrVMetvxopqVCwsV0xi5aDVoUok7RXeYi1xPU5wSpnNSok1LMEUKpCTE/61fwx53gSroqRBC2k1eMGF9gesUVcNvh17G0hK9y4PB6W4TbWugmczDKfK+KnkHNEStDpd6hMb0Au7yLY0xvs/HmfbEVj6qOau+1v5QF1tT82iopD3dAv+7g6MbXVvve18TmREoPTa/1fmRLCT3LDogyI0u3RGy+gp1rQ/ji+Uk2OcpPbPcPPXPM0IN6yV11/zxbZPAfuFBiPbsvqrzUI5p2Y5lODkEFNwZcIR/uTOwhF2C3Adf04Eq3E/0O/5rilNLCpCQXP5iF2R2wQLqT7WU/S7BMCdE1/3TXfiiOJqGxwRwUQNonbI4YGlk91jZRF+YPUEfPkB1Z9tVXZ47AlrSpYQ/ZsUayfSpTiUU7SQIzJkMIinY4hAcKUMZv5+ftknD9i3TXi0B4WCKrTEFbxY8efSQOaHd1ff7Lf0sJ0oiCinBgdAA+2un3Zva/URd6bquOR0Z8mEbBR6U0vzL+aebgUjBniHdm6kEZXOxqFS7y+skugdQtHdj8gNDXo2oDWQluXOXY6C3XwjVEgL26fbdlb77p3xUn7WSrUlqridyPr79AsfXpveuvP05GAhL2p2uMyVAwfCgfIDTDMXIzIixPWf4StWjGgo7YW9N9+dEGuhAyI9QnhF1tJrwKgWmpzFb5PfAI185JPd4m2c2r0YFSmUbBmPcMoO8kJI5u/hyNkhudveS9bwU+SXVGh5jnHk8wnEZuLiZkLt56lBa7+dQVkRFKUBd5NYc/yig380+a0S3WdkShbwd53JuveFxKnsAofV3mBIXhkcJGLOXYD+GzXmV8nRnjIXBK+bXNZ27XUpfy94dvc0EdolBqnSjv8R95/tQ3e3L5AKjk07gEejnUOIouKKtTKmrT1jz47Aox8JIShEgX7If+EP9/by5Q2LkEW7XmVAMRy3DZl8V2RXox2NLFew62ubVkl2tyjDtN311an9s++Lt0dCJBO2pILQtVV4D/45jk396sgCo498ZwfhHULmdvnSsjoa4wMqg0YMocscrDSD16gHlnlN5rDT4eTUdOGThZfz2JmzmnGVz3wFY6iML0iaJoWD3PGRByS3bvgQECwi5u1uXfq1uaVmT07HmeDgfN6pEfsa3mgtQueXuVPXv4kdoZxT2VewBW8t5/1MrKBn+rycLbHugR5KOHyuG1f5NyjL4UUwa+pLjT2eegzrETC5Uc70I5bIZ39l8CU72exfznzETWQZUnOrU33SUHQz6glRcQHmbe5Wo9L8oKp+kd+Gu1qkVgv1dMpy+xeFvNfvR7WMM7412KxEgd1BjS70a3+su8Kj2FnmPlk9qM6T1666ceGej+IYkeh499XxCMVArz1v3VK3U0JRDxfKza6CHF7gwX+eN9oRFQeMO3RUrwIPlV9sArg3Kc28fw9t3qQKaQCYFbQ6G0xEWwaE4OfYNk09CIIQwvcgcr2YG4vMlYP/SJB3JtsSCD25nixAGHhVGRIxbvojFVI/Q4kUOfng6RUDl2YuX9NZi2bdOgGNsad1gdL6r5vzq/wxroVZETHTrPUC+ct/KgGH0Rpz2BD9zfARRzcyNM0o1U3bU64JvsbYCgTsUkCT5TILD8GVpBx18bhf0TA0r6dXOXz4wR5mlS2LAa0s0ytSpogiGyyDxqwAMdjl/aZtmjZ/ZVD1R5C/ki+zV62QleQi+aBgaJnb8yRAwv2nJZVowz1FSplz+rnUhOjCZsrg21T4havQZKGqU+Vc+hjzRSBmG3f1LSz8V4LdTdlcyIsGGkGvfhch+PuVLP+JM2DG6PjKE4pzjtX85hJ5nMeetFhFbCCvLJ9zE8BBYZYVEZV+nx8HoaMdpd6hGl3lcxlF6b2K3CT0/fvfCNsmGrCniFtKt/pXeWitq/aax9L1rQbs3o1hqSjKBM4wE1KJPr2dmLlH33ovOz9ftXzpi5bqJ8VHZqTNoZtx1GyYPzR4Fb/Ke3k6Yt1aXAoS9FjJ5gOL1NHg20okrolG0zMQPhg3Hiv7aiPQp9QZh+BTxXA1w0+Pn9jwHlqtxXD5adnOPkp4dMK3YRNyj/Kcffmb11J3SLxwPEUrsNOlaRiayZfljCVWr+St5CcKmloyf90/39/XXXNi8ZeulNcBlS+M2cOnBcNo3p/7WNts8825GYn4dJ6Q8nJgoTyojsPay9yEUxf2NmOd+ajfAc6xcgebqwZqK60jTY5tPnO6VAJ5nw2bCC0H6noxvYfc0b7LgiWolsnL1HZQrdT5KwZQO18nvc3ohpknIvFZ6N1qj9apYEPicTrVGhF+C23H0yuYJCnbW7nbPeMf69LPc3PIuw6K5vX5FdQHUfkgawluGDviQobrGn8GiyJ8s9387+ABrIhN2Mtzq2irxdaZ3pLtwNvm27iM0rY2FXYNuNt2qvrth18U6FmFtxVRmXpCzgwFSR3bZL++G4eXEReaJOgR3gHLQX7wDNC1mG5ZkBsx5exSpSq5JfGqtET+c8c2AjacU/hBeADLm1ibGhQ3yitZT20TpR2Un5SVIWDX4phV3Lu5x3l7FZYtD+6Y8vWXsWhbx6MpccomVJtUTGDkGJu12z7OnQ5H99JDOD4dNkNz9AOMgLA6T01zAmKQdw50KCjbP90Ifo2RGNJuBLy5pLDHR64wdFNyvLnjjcFZ5+OR0BxmCxqqsEkl0oMIXCxUXjE8qfvaoXdYeS3ShtoHHeuB5bOlUrlqXvCcka04NFR/OaVCkHZ/jjaMul3MaZEizQZxiLBBe/1DOrKL7BmKkOGoAl2cB4AQn4xU78YUW3bdE/gHpDKxvDhiWkrJdzh0b+zdY04QEoZJFPavK6Swi6jzyQuChkwBkQ3o/r9hdVQoSVzaDql4UslaiGHaouZwzqZ1f7VmdtnYE+twP6QYti3h1V6xeptdgY7nnOtx7uJDvQmtoaSaG2fASJCIcgfdLxMkG1aAkBq8BlnSzX+zr1Cne3VwpBOBEFlidFcQ8cDPO8v33AKtbdYOnFl7eoiuNfwLYMgmQUpb9YSHvLiLt2LSS6NiIuvC39o/+AsgtfmOvV0mylojsgYyWMNe+1JaQJSpcTuWNchCzU/EgNLHW2+dfa53UL30GDdEhJGzTszmFWeoIy4aii3gH+TTOAgKX+GE6JRQ66Es3lCfUU3Mtx1HtnOWE/4OQ8JSxcwLhXAC9gSKTnCm7eI3wtOUNMNpF1g8Pvinh1/bofF5F9yLUs80n7zy3eoYn9TtWqzanx9+IZ8jVTKM1dksE5k39b8Yncg9yJPkgebcxsdsyPxa3Rsgx44cCudBhcma9Xa96b/wbSc85qve7XofVSJW4tRwiYcDjgUqS3756ZwlQH1aLHYSPNVW27SiVz1fGkvN5eN4QmTWsRMAeReUyc+HG1lDpHdghhZGy/wgh4JZ/jI7wPLiD/SOyWsI6wpPrRfW0z+xQt1VhOuq0TqN0XgPGR3O5fGksHJyegEPDnoS2a4MAo+gtobcw9vhJwjuHMcZXdEpZOzbgQTpc+gFC89/zNB48vWCpMKiiioe6k3Pc/ZkXMi8a03FJhc80UdAfYA7EEmoSsf0eG93klD/m4va0RxvRivEGcSlC/YUcmKut9ZBwYF9jbHQ/+Tm3PqdbSChb7onuf3hgVeqzsikgRtl23sdfIw6MBHpxZW6RH/EBMMsWimAT4bClK/snJaYG4WTBzvk8p6jlncBLxkAkmqQ98rnClrbnsYOJCjcPi+0HCFC0aDtWk3T9m8W0XgDkTWPe8OfPaFzkShBpGqEI55S1u9efP9ZEuNbmYW3ssw9Lo5u6RBHqmoTKHNNwv+JimOL6Rg44CHcqN48KyIsyTEwJiVR3VNuu2daVao/D7e0ucidV0evm2WMmkYuIhtGFXiNZEbXj2IzgXaqfD1TZc6Dqd51jBgx9MHB1rz6jv7CIyLz0xuReLFL2SNbeShahLQTf/abk1OhEiEXi2hv+EKAjp80mnfbvPh8uuBf5j0oluZR+Mv248YR6X7hOJDI/w0Bp2iANg3g8UlGHmTNn0X7LoiwkJv+oZscslt3orIXSmbB64onMJNzwEujYSIlK9izKF2OO41OggLehzIV5ILvySQ8jbawdSX2kjMWiCr3R17a+sCiunrR1VfrBonxnQ11GoTsOStLkiSunfqtxOOShShz0/jBYdoew1/Oux5jmOKzdgLpA5UubQ0uUagZMnECnfrxmOoaDugT5zFXIXGwdZe8kayQj49L3dvquyYUNr/l7yzNtB/pYDcCodv7ookkENzovmm9GqukpV0qCLErjGNDm0IgIzmfb+cfpkcnh0DZES+UKNxL9qNUzPa+loKb00CfZdVOgM/xZwHnfTdfC3bx9bCjvKIls3xnpvkGejxpiebMc2gDKLieeBKCsKozb8DVU0A/wuedM62L2igebE5obvagaMlTTQP+5ewJJQrSrnZ2fiQAmAq+wSWztYCxyd5qsOT1T5dNMeMt50ZjSq1EHDixtI/yO/48Ya8HvUB+jsxh6TVjZuzHN9bC+WkqEKH1cuZMO/FwG++Hp2l+tiS1O851uDC6yC+bAZDpxYoTkdNpzGL9rhdHvsLG73pB6zg+PPECCZGHgyxZCUFV79n91S1fWsSXom7GUyqmROQXVDtv6/3WfjazvgBw2cbv9w8/3KWjOv6HGOGi+7OLLd2oBJVgWlvVA8a/WzebD2tfLVSDxNnq5jqDjfeH6bCmnyToP1gLx6SU9Y/2BVoqUej7c5ubnGY7pn6XieAmLRbfdihJQLJ73n8ff/+qgmwWGikYlilK2kIIjS0pfuek5/6YDqjL0NSspIAztwhSsaXEXclpAo23JOTsdQsA3qkOBwEGMXeRsN9nT/o2WmlsBekRKVBYntQmm+LgV6enTib+OGLAwSMboBMjiuIcA5d4nJIWb9UmyQNlNqt5G2w4gCcPWDdtHUvqEso/n11N24AqBzIpwRExbkGPIo83u5ex2t/7gT0HHBi0Sr0Ov8kSfodNSJfuXBSbln9jTett49+D+4h1clzaDMzPVGWTADcfFflYue3JkgCMgTeQPaEmFMv8lWOg2emIQFyJIuPr/VlxY7AsMYmPidGnfoD4vmPGYuhZdZObtWscuqFh1FN0Mn81V+JlGCcE8FT3YYIKAQEv5nLLfN/eETKYcFk10f0qAZRVUGnBJRuJwwkpF7mwPTcO48ttSCnowLE+iVBedHnOMiTVWfXhhoxgo5RA5b1v01XpRcoUXnJZjRU8mN8GojUfrqtLmRSEfX374Bf0FFkk77HeGJKGzqReZonQhxNhtu+JvU6/utcZGlX136IYVn6rbJEGdb9qpw5E67/G43EalEVyBOYuRuqd7eSNP/huXQOSsNnkLogeeW/9F80Fd4dhGIBBzDkgZCdyRlBtJN96Dsy5cpngzwGIWmsRIaHXewGKpERt+TAOhJV9MjegMK0MGhGByhlBVh1cyXJiWp06I216VbzVCZKdPllTnLnx5lKWtnt8rb69/wWsLNH/+UuRKs8wVDbeBMKcJuv/nzwLO09CpOFrayR5w4BEjqPa6qxN1j81P4Ld133ZA0O52b++v61b9XFyAR4TTHk2QOOgae8xiLTZZi5WifK9JYF3xNPLEKHvf8UobWLunVY8uFWmTjBC0HlB5UteVA5izF3/g5H4kk5qVTVhzapmLc5hXZr+7Xh2gsVYS+azq84iZIGHsfrMcRM3d7ILubM+evKgENG7pWGgfBZefl9/ZlyVMwxspW1YydvA/MjFMx1DAxa7+ur+y2608U7B6tWuy1UwmZGbpnaQwNwJguSGgNg7gGJkRWp7nWeFuu4+dmO6cT7B0p5PBjsvS8j6Y2LV3hI4hJQ78bBrNUFJOsCyInXkTA+qP4Y9PZ73b6WTDaZZ+oogCiPFlwUpJ9LzYFkDKKnjMiKH4kVusOqE27G06gHTLCYA3ItYCyGOq7GcttuecF8wNLDobqiR8OLRqbHirSB8ZrkNa2X+AZbpGP3d1AZTxyzo2rjtuiRNBjAbD4uci1MCZYh4o6H8ffm5hSjWAm2UsVWI/xLRRl/bMs9fxpiqK+OUasIumOowb3LW4lWuK7lrgaxb1uBnTFus4DTyPHp3JRhhdOHEZ/acOv99YkvvwMtyndXYmf35Ei8ZQO3S5gVt6j91BfJjFQnlvbVtMoGtD9WHli/gIYNRotYMsQIRFo3wuNNE8qAP1jMgDf4nIG5rHBQwlnkBHhFS0ssz8jvQTZMNmYD9DbGhFu6ddff3MKAHqsls5qMoPOieeu0R8UhUpZL87HZAk1O2ojwYzTrVmHmXYVejTH9tx/9ydnTeWfyiqzTdkV+MLrqkwduRHaDqGVFirxCaSEdj12t/r8wsGRaLQeI9msVk6tgFS+0+GAKYCiTqT6sxA4V1ar14NaQ+MQAPumJUTN+dlCnPdFjVsNKhYIkhEpAh5TkUnD4A5IlEVjdQuORyzhzM8MNYhEixTR9dFW52W6kvlvWl6tZ/ecF/LbXjYvuD/PjbXe++N9dTDrLFDvnUtoZA5/bofQ18ILuG+lpgX3HYefp3Shm3KIaIAObPQRdAPv5ZE5CmHl9HD8KFjy7S/jOBoDfPl1iZ1H+i4S7997GOH6NNihrM5jtJbL3ToUb/dPa4tzKC4yyrJoqrUXwpLfZicO5lulB6smRVcEQHJ4OhxU/PLRo9qwv/nPBTu/pLItNhyROZXyXPK/keo7Gu37a9+ueWBA4t+3tMFPqhcDjNLYu+rCSHBkbSIqFDpmcmLdBibX4QLpzv1Ot12R2qd1Kt+Chihwrx3bXfT/NTk0qA+v5wNWV1yQTjG9DRe9Iudo/VHXXMT1vHM7Iq8Jv0BIcbgYTuvzcYfNEg7YGLyAaNBgcbAUddMufPOyq8j1y1EJLGWb3LvQDVPN2BpwD7zH/+7JPSrG5Lm0jVur7iZpckRJ8TdDzRQsEm0SntTaB1QfzjBI1oDY6uPmxu4x0nAzfwmrgTGadIBrJwfCdca5g8H4HO2WcgCkr1pSJVGUqwnPuHHvHyOTWm3uARX2/DpvD2ydjSY50WU5wwLdN8C1UawT/7j5vcfawJhFOLVAoDXTA/eudLSKOX0kSCsFCXgk04xpgvwkbm97rrbVYKboNHca5G9kE0/xy+A0sPwxP+AgEx8CCSssez6W2PUbKfIqqiTEFGFOYFTNM4RgAL9n/m/py6g99dCahFwM9CKzsf5TEHkP1i4+2rsOouaLnOccFoUvfGNcDPh4zM4dPVwbLamk+oKvOJhnAd81qDdS2iGjeKcI8RNNX1vihmXIdAJE9Y84usMT5CwkF8eB57KPaIfJhyAjJgHLkvNkSwi6h0FDkxIMZ+k0ntxnPfy/ulcWPXrPj5ca2NZnU/VE3OhfnPAC4A0MU2oLxBurVJVJIwV0xpLmXZhUGsyqcVwsMtEHPIWjL5huBdStwafXCVFgtWdsoBItx3M9uXkzCD2X8g6C2P9SrflnVoVQ+gIj9bc47GhHyDUbkf3hrlMXx3EpUABVvJ0s23zdjd8e5WkvGEIRXXmwM019UWIfOzqORL7xvMG3bxXxxf9M9eiM9io2uN6b99iJ5YEMnzQY5/078FhY8sW7kKpqw0RSAnQoO5/TBu58DRxEVPkZi097OgrnZzKCezrxbVQovQ+s4XRszlz1302DR3y9BNjmg08Pzsgl1+fs5RDXh0UuOOlZ/9xq0Jab46kvOTPCjl1a4+oFBDtlAkwUqTj+qGVBt3N0Kps+KU4GP6s9mIooFsF8r1TOWZkduRkzJ8IEhcsBGjGE8X+pQVk6dE8fW6iWQ9fNvCdno/xSwpSkbXxKEo53kooPLUGwxSCOGyapGmVQ0OTaCmoBS+EgrbTUBkzQKy4CKNz3U+DnVCEkS0XhSZhGIZjRbFD2qc51llNwQDWsfG0FIzMpQZt/gczvftbSffO+bDH+1P+RUjEcPYKdOtqS8/4S1kH1do5f23eX5EQPDZO8ZqitZI/Ugp+B+vn2QOtB+g5ERtCAZZTpOfdVGd+sN9aTR42sf3f9FNQK4DcIqa8xlsYIu0dVmq8V8UJpRBwiuiulfm6sqnFsEn5N8xNOlIdmsFJ0BshcEDwtqjv2/5vg+ggWdZI55VmssylhPzT8IEzw6RlSHtxh8B8z0a/z5Kv9fUySk3MbM4GOuA1C9XIYb5WfB3fROhl5kI4w1DDsyLc2NLsKJZ41dGTcmLug/mNs8Wtz9NAW6ssx7VxwMdlXDNJ/o18TaOgxM4iv+ZKDXVeLB76fbNsbFgYALq8z4Hk9qEOBHUboLeapmOMailGYLbLxQ88B4pSzwdyLaJdz0GV8OCo8nOOnINTgdUwcuy8fGz7bZzXnZfA7hpuJ4DCW/kpCSroUMmJzhlPzp7ql46Et3AE+3PUxCCddEPPp7rtcAQE6eiSGZvWTQqev6bStc0WzqTNzZRS7d/3tbeeW5lUqmox7m98xUatY+T4tpplUipOc9iRy+DBj1VZk0tbl9WUUEHwLuwSY4EZ6ys+t8ebThFlbiZEuSN9Aw7Q+tn6uXm7sLUC+7v+HitUnZ1DTUhGrocdP9/lev164rzBn87qDRnhWOIO2vKo7zROtak6+2bzKZ/n03mYcCnjpegOFWw8YMf9U3hYnp9hsZuufhTh5/vdPYTCl3PmhrLFwbjbQfiDaBapWuiLZAz6+aI6hvOSNfGF5GC3pJcz9MlQ+zasxukaoUFdIIl/DBvDPHF8wv186LVZ5EX9NAL/Zv0Z3KNNtkFVq2hP4HH1ZvgcyMgh52oQPjcdAn39bQIPgtFdPWfw5VhZL6khsXjchbB9SdwIncZOjhxkDsiVrWRdPGp7cQRSmmanMyslYcKRptqHU9aPvL7MuAny0ovPjGObfyNvO5aJpMRyA572QtTWPAaA2gn5+SJzuJ6AO7FPkD9RLeW/Gh1L7kHR5yIWMEDmVHPT8zK6ngwkkDcZkvkhbj7gT4CV0hKG9WyCERHq0IqW6tEMEIcoprIZRFTlfj9rlwLVM03tGJA9sY9dXLpSkzUjFUaLS6AA4uJ3tV+9aI76Q+oF8uwTvtXAYRwT9b6ne9jeZGvcTNT9ADDt6nUlJsUZoCgEVlGRaDjvl4jzhuIxVYSRbfrVf/TlrbgAhLoJV6/bfMBuwViKbzuja17XOIme/LAmTk+KRf5BUt2eXLD6Q0+p56sFRXomppuGCIP6Hc1wdhOiUVHtGZ8xRAsWocD7gquIjHuQAK9mQbHjS3GkCItKSsKynIX+UL+Lfpyvbjp/OGvFCWRU7T5VJ/OW4FgwwN5B27idQZ/KiauteOc520jFQ35WQbLgD00i93jVvyQMm/fPsPuafD9X6t4qSLFEHLTVId6TQa2zcalzUcqfccVkg8baf0+oat2mTt0M1sUtiKcZ49AY5kDPzvD+76osOmDy2/H6Tdcyxv92JX8I33Ce4f3mLMzdlL+2Y7JAuGKHfGPWWXK2dAtvo77Z2X/5bh5mpjHI7ufe7IEpKFbKaDPzLEYwpbgEH5fCGf19sVSy3HecV+X1AX4daLTeOzPsGAQENzYb8JIvcfin5TKqQzZp+zj22BllknGSRLeAQm173pmDNo38//cC2LXTjvayyNlMboFa6K7YXctY4uZZoYUXjjL7U87b2D26COkPJTso3ZWAO2yV60m9YMTKeRmvPvEuqDKGhwdk4XwttZMnQzrdy1IUmPKy/DKUTtlmi+lSa4Ld/hm6JUbgxqW96G6lzfQDniyMDI00R9aepR9w1YycHhCWULwBYdpCbcHx7VBGnEnOv3zZnKKaXStFGuasJNp8iVQzVuz43jrNpLIlY0PMeQUtwTvRYkZdKc4dpxDfX+kJVX0jHjB5wS4W68LqKwTOcMjhT41D5lc7hQxJ1cpRBB78r2zP/ip9FfrsfbfawVN0sKcOYsCGpSPzhySU9VGiz30EBgR5Z+EJ/mSymxGBi5PRzjOwqTY0sp2VnvCvzv51coF9IAO7bGOSA3NEVWT9Lo5lzQPJBbVZsTG0z6dzUGQ2v2k5j7YOF3bhm6S3gsGfYT2OvO1qSdooFoFlHEjEjbx60D+AUmKlVRbWO6ke9yiYkUY0cbsi24HY0UGKE2RemKS8CGzCjnDGpo+EYoXqH1pEWxnBiBcejtql0G7tZNetU2lFVNwdz6+JEl5/GnJ8tO0pWRHlbjnmXuqtRZMvcW79bOpdnuqSvnIj6XYWnljgAe/A4TYrDPsDsyaE3/dXu8LQZ1lHyV/Pn4TqNsf1BrCB642oxw35YRFbU4kx6CA+9580lXAXDgbpr0lUOLJgQ94sVBYJK5GAi5ClrXrxmH2oO4LNne0/golFxj2Zl9IFn8FGrNLDGs9ViR0YrGsVOadJwXsKqhEJY0Vr+4T0hJUur4A4y/6vUPu2vyJA/tg4NVzB7l8nvk90QuVqR5qqvgtkwNh61w6QolvdF0GSds40bozYRzGpCQ9U7UZGpFNxCkxYFsg0/8CGSlS3U+/aebaLrOwZ9F8zMVZDlG4DjcrWf+fFwF/LQ2Lq3W2LIAtpmXAWmRCPplzU0GspUxU/4EZqPo1HMVCHSBBhEhPhnFv8VVknBuiOqsFowovyXIYCluiFiTaZGFWwL3GFLumnqn8YLvPNBadnxDqj78OatKxqCLB+rFjRzl899eZd25+LsjACzmSCOtxtMkW3Vyz9xlAK6n5ziooEEx3ks+GyWX6ulR5TxL8CJqnUK8z0rCgzMiqf8VSmn2/6LVva/6WuLf8bQMS4MuEvbxG9STMQM8ofHQetHU/uhNUFC0HZNlyCtfwV7kNXYusIF8VzTiJzNxOMQReLp3s79r7IN/r3CjKZJ5yKtRLIQ+pWbYry0rGOuJw8J4OjUj+VPiqJP/eQcThoOhP6Sv8lENpS3QPR4+Cf5Xs28zk71brYba8Kv386ZORQdttcy4EV4BhcnAn+6qtKlgSP8FV0cVkCmMbjKgtrsD90JwziwjLu5GojnzXIbHcsN6QzNdetgH6fHko+c+l/HeiNZAqMnB67bX/PejqqxT3Hv5j5e0FLb6KtZJoTEEktivs4G45BkVl1gnr5V7BhwtN9ahN28fkcVOp22xhcj0g8nELRwkorlq+PisaVkr4KExGAD+5JcBKXmIWL+CCIXxGpChT0zTKDXjd5mmR/KQYDVrEV8fwUINl7cJJgv8ZlwGsOMSVTmHr3tQY8hhA/zxAFSHWVpY7ho88ji3aawu1XbySM4nY6c/ztIytmduLxE0lleVMS33YcXhsIg4jPZUtY92ejo5zGb7DaVaki+K6g5ve1VTqfkYPm8PnwDwB6zkUfIQK07+3qdq60RrLVIiDmnb/vpOjHEhCUaEB8VDLqVkeoy0odQcxNoDSUDIaR/y02jxYWNxytQlCWo42IdXMu5PU91cbkjMN7Zb9D+0A7diUEWfDUCutncpQDSbFEU8UMSprlyZlgqN4N/Gy60BzKTKBStQSxuxxn1vQNXCP50riREMzFaLYqdm3tfSof8h04rZ9XpC/i4mBdUbZr3KgHqStSAbbeRBDirWdQFT4wXlHJFni9bQPAm6zSsHJMzmC9LOLvzKv+cKyw65oE7MvpuKiTpJhU3rrfuAiEpyYYDXsLwvi+TXbBdT6pETsexJdMbA0Og0hXcS6cHsf9Nnih3CEb6T5/HUzv6CbSLvvRKcildF6VqupCWiXfJarUcvi81MdlA8ov42eJvvv9kXGkhXorJHPszewNcNBuw60WKHgobl74lgHcxGJ5L4bM49CetZBXnX78FXIRvYgXbD0RPpEP3ZCuIFjc1pi8W0k4pk+ltzDEHH3axPSI0Ia5FFjvBlXcEKaHskTA8evXySL/xh80DA2bfv2/ITEXPRwYchCUFvBraCVHTxaz9jMw/UXCL2Z0ZD8nkrYkoyPb46AaX6Wt9HDpL/YyPFb+juV1GBR7jswsVKdffaLu3iNcCvK1g1dW1nGCK3m4Gk8Xsjt8WjGRitXMC9OupdlDGrITi0HCsnoCu1JKuL9SqLus/XpbcTPnU/Goi67449wZ1y0hgYtpypUQMA2xAC6fdE1HBxFz5+E9+TzpTsepDykISpndUyxKDEmgMcxPQ7R7CjAmE8ekN0yLdD10nZWxeDs62d7ycklc/IU4BiFc2q3K9nhiP2lQbtYURwKc1wXf/6ejkxvjMA31hNmU+ZVMBniaAbgRhz/zegcbddo6NxBKLfMV/YrJ/SNCo/BXLrnfNrgs3rYa/aVkRpAx5SJlkBASM3gwzolEYEyHFDb52fKYewFpKA0Q7w0Kh7E2zCuo/ym2Grvp0MHDtQpHFhz4XWsXvZfuudUyvRmdbn3D5u6rPwz7VGczjKtMJP+/fBJ41Xy3jAWg+EXzgMKBG6n0sNG9PNPiddxgJVJYn3ZGxdU3dXRdFeMBndMO+519duAqi8+90Y16n2ACSlX2mr2g2FESyP+F7CvyetQMrEZUf8pCcAM5V8eKDkysQQqa7ulwQ8xOc7qsSIAw8l15gSkA03LW4NtA0XWB9679wtDyASC2IYU1gtEodc3W7yUPOP4V2I8w+gOkz5ECT6w4+ofCSoQPS0mGeXHOtYdrnLTdWMyzK057cmtUBb2ypMD1ucfDaN+8Epo7+9n/933EVs2DJKoVO1dS9S1+d+V+fm+h4HBDAv3K/+XbQDqEF+zwPETh2Q6P1zC4eG1Kgz2H22ceql+6wphptNhQApqkP3/2cDYC+y0+lbcEACUg4TRxnHQJ7z3NE+maKjuHdsUNuooZbjVcE+q4Yqm0Qke10fjQek+OzJWhHc+mC4zA/bcW+3p+9NYJZE5XSBJJbi+/qVBgCcb3Y8OKIg7+9IHUQO4I2TKM+Kw0gufDsdRhi1GDo/MqvFocE8YcBiria3gIheCblNhaVcc4S1pPziI4qEJUOR5qGqiOZN5A2OUszP4L+/CVtI4yRz8dSgIECvgI1rKyYOGTjgWnE1dPj/xGNGCYzY3nM8JZVVVeboA5h5C3x4m+H4BQrrACgojTdRctE9756ziPUSdoIKmIflFFQ/kFHHdNQ9Vs+Nfjh9buMea0tvhUP7O9b5y0/VtyFDYnTyS4NsQBekaNsWKFLO5elbRiW1fQ7zM9lw3U+89oi59AHDKkm6NuhWvB9jkwOaVc5VT1uLa3SCrIzZgGbeqSHmjbiK/4DvkWqfZYObCrKYh9ymJtHwNjROlPN4wXkkGUU3zdMMDIeCZxE9q0XCbM3tiJlsnKrDMm37qyk/mh1Oqe32Bu5CzDIsK2DZdfNvILjJlWVBTgZhDo7JrB8ujLqzFZjRT5NHHnvT94Z3EvcLApx0djI7sojn3VvXiYiMt5OACD3uju9+GU1r/bI0io2vs0clsiiKqGv3DbTpbkRRzFmbTcBV50iPS5z+tdrTp8HFm5IW/G+cNg93R7qDFJswu5Tlj7piMwV4q6JtAD0csiZk7KXnvAoVEym3DePTT2BAzWSRqBZB1u+3Uq8C069qL5jvoLI+NFFLqqtDIvASFdWpbfeg9RMaBJGO9VWdhOU2aAJoQLlPjAH3rtbYrVRI5wFqf43TcVNuOzBbU7k+7W73zN9yIutuyj+q1sH+0wkTgq+NH+Q1zjsdJiDDgm8YjjcJg8+UbqNi/2zzUgSZTGI+/rX6ml+Fj6xFSAw5gcynmvGgIhfeDu/WqpJUxoCzPq9oWeFf5r70yQhRRDo+TFCD+NRSedeO0kanNahScvNLFk+esTJRZGu7/AM8WAc1t70tTdvGkES4t2l+SAiYYjVRd7vyzXujlrsr++64l3xItvQyKIQGDB1DqyVbBD8S9nVyBytc8doq4udNeR64RgptyTx5yyv4Hnfe5h06TPpE5FTt7DeRi6T+RC0EJJfCaIY5ZTRDYC5T4Ni+1nDAuqomCYci4JfNev1RizM+JJ1GGeUv1MpdskBvkqJhycyyySihzecLjAGrax9qlBn3yGOz15NT4ygOpK/+/ilR+QFkA78Yf3pDwT8jv0sQlcZ69TVzhimyN6X7o3ymsISopXq6JefdSb1kZKmCFv/feVFG8hgvF90xDI6p3jbnuYr5MbaLLe8mr4PN2Ol27UEXEBBmTtiEqrY7oovDJ8ns+mDyRVFbwB0X5/UgFdlxbxXdAIyobLNytMg8AAk3n0Ie1SFGMtJp771i6IT5K+SF1XZ0DpEmXkDi81732l/WqrQazJ1yMhWe4XY25Sy1Q+AMhGOlkGKbMNU27svDI5g7w10+nA9KRGmBIneBwdSNVBUNjVTkHPSg01L7f9lRaJGvdgcJlUpNcLYeUSbTuA10rsroWhNbebkRClgseKJWXsBI0CWXVWY2U+LOJ5KITeeDlnghl5Auk3cEbnja3vtMoIlKgqJRe1Mik8D9Tp5mRBpYvoMyfaJuOBYcugQueoyS/w7FNK9NKYtUB8aEe1i5lj2x78h3ntdz/82ZgQTKpV07RgFWC2fKVauYjM2YAdfmh/nj8rpg/15uPXpq25qm+CJ4HHnT6RaQaSbeUnZZNwzvRbTgorUlBZmZZbRq+qT9TCHwqTh92CMz1YxcWhyRa8+ONvJbKDx6BFGA3WPKJNdqlSvsbDn/FOtOC/g2M0l19SU1GGlkMzVOr3GbwOyZBAgwMQ7Fka860asD7Fm2tI1/wp6sSdwl+2SVUc+NJJ2aOopD7DFUHV9hppq0e/au1P/8hDodaUAsVefWVHQyRShEeApNpqNN59OMAaFprKZlEQo8Uus6qNdpBhQMG1FKi9ft28IeZ0sm5HcC1Ck53eY7I17QQR3jHtsEJsX/CB0rsPniznuRLaj7xe/+ulTCAu/In3GXitQARgRtcnx+4qB2GHsX+D+sGil/uo3/jj+LBLtrXABlJfgBwzsQOj+H98ysSDOhzrakmEpCGuP2Wzd8BKDwTZHO1tA4SiJn19aLCF3ugAWMDG0fCHO1RsosFYaSUgnCSBgpABo0Cu3fVgqDmhMHT3at2kucD+6gLbft4jxTM3RGBtH/doVc595sboWrbhOu7LRpNg6omNt4ngKLYqQmiGBbjKZW46M0mW8bH60dek27oSagVxwpRV4SJZXxJwXEdtqSnSXV9zdZKOtoBap/FmeHORKe1+6xUY9bIXXXuphrJpH0DyIRTrYKI/Y0Hfks2Xj10AOWdUDtXEPAem/BcWh3V2nyWRHq2mPPnxLicgd/JJgsnTDq+bbkZZLglIRDLqsNmt/JQwFokhKX/d8rGyQbOS95UuMgZoenfXx7TnD2Cyex4sINffPyk9Lff+QZFe3ew1AZFSBDFs9wyqmvwkN40whh/IYd4cxqjAGizSIFKGpAUxLP0cBpN1tSmxNA41sgOe3DZ61omUFy8Ch+Y6s/1IdsE+x9omX6PJ02sWFb3O/x1D+AaiI2MocWfAhg2keI8VlxML2PZfk0IQ9vigQ2mOyLpGUjXB8ii7KzKH39njI99cQ9T/KJ/Qrjed5HTDwJ0=
        - #1:
          - type: tool-result
          - toolCallId: SGAQNGM9lvUgpMrP
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ZUsScSto9PT5NZJb
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: KwIwLEXuLwL8AHnE
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.