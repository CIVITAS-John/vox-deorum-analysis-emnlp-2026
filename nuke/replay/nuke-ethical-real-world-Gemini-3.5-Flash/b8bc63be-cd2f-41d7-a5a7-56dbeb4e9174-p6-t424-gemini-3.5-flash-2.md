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
      - toolName: set-persona
      - args:
        - GuardedBias: 9
        - DiplomaticBalance: 8
        - DenounceWillingness: 6
        - VictoryCompetitiveness: 5
        - MinorCivWarBias: 1
        - MinorCivFriendlyBias: 4
        - FriendlyBias: 4
        - DeceptiveBias: 2
        - Forgiveness: 5
        - WorkAgainstWillingness: 10
        - Rationale: CAUTIOUS DEFENSIVE POSTURE STRONGLY MAINTAINED. A major escalation has occurred: Russia has captured the occupied German city of Cologne from the Inca, bringing their massive military forces (15,440 vs our 3,335) directly to our eastern borders. With the peace treaty expired for 21 turns, Russia is an immediate, existential threat. We must maintain high GuardedBias (9) and AfraidBias (9) to prioritize defensive safety, while holding WarBias (7) for our eventual liberation of Cologne, Stuttgart, and Dortmund. We also maintain high loyalty and look to coordinate with India against any potential Russian aggression.
        - HostileBias: 5
        - WonderCompetitiveness: 4
        - MinorCivHostileBias: 1
        - Friendliness: 5
        - NeutralBias: 4
        - Neediness: 6
        - Meanness: 4
        - WarmongerHate: 6
        - MinorCivCompetitiveness: 3
        - Boldness: 4
        - Loyalty: 9
        - WarBias: 7
        - MinorCivNeutralBias: 3
        - WorkWithWillingness: 3
        - AfraidBias: 9
        - Chattiness: 4
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Satellites is the foundational technology for our Spaceship Grand Strategy, as it unlocks the Apollo Program necessary for a Science Victory. Setting it as our next research ensures our empire stays focused on the primary victory path.
        - Technology: Satellites
    - #2:
      - toolName: set-policy
      - args:
        - Rationale: Adopting Enlightenment (from the Rationalism branch) grants Germany 1 Free Technology and +1 Happiness from Universities. This is an immense boost that can be used to immediately unlock or accelerate research on key late-game techs like Satellites or Penicillin. This is far superior to Futurism for our Spaceship Grand Strategy, as it directly speeds up our victory timeline while also providing a happiness boost to support our production centers.
        - Policy: Enlightenment
    - #3:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Mobilization: 80
          - Naval: 92
          - Offense: 65
          - Spaceship: 90
          - Happiness: 70
          - Antiair: 95
          - CityDefense: 95
          - Culture: 55
          - Nuke: 100
          - Infrastructure: 95
          - Espionage: 95
          - UseNuke: 90
          - Growth: 60
          - Mobile: 80
          - Ranged: 90
          - Defense: 95
          - Production: 100
          - Diplomacy: 85
          - MilitaryTraining: 90
          - Air: 90
          - Science: 100
        - GrandStrategy: Spaceship
      - rationale: Spaceship Grand Strategy is maintained. We are raising Diplomacy to 85 to contest city-states against Greece's diplomatic threat, and Culture to 55 to defend against India's cultural influence. We maintain maximum priorities on Science, Production, Defense, and Nuclear Deterrence to safeguard our empire from Russian aggression.
  - tokens:
    - inputTokens: 52729
    - reasoningTokens: 9027
    - outputTokens: 657
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            My current focus is on thoroughly assessing our position after the recent turns. I'm dissecting all impactful events to understand how they've shifted the landscape and to identify any emerging opportunities or threats for our German empire. This detailed review will inform my next strategic decisions.
            
            **Revising Strategy Based on Capture**
            
            My attention has shifted to Russia's capture of Cologne. This development, from the Inca's possession no less, presents a significant shift. I'm re-evaluating our naval and airborne deployments, considering how this changes our immediate strategic options and the territorial integrity of the German empire.
            
            **Reassessing Russian Advance**
            
            My thoughts are now consumed by Russia's unexpected acquisition of Cologne from the Inca. This complicates my liberation plans considerably. Given Russia's overwhelming military and resource advantage, coupled with their existing occupation of other German cities and their open border with us since our peace treaty expired, I'm urgently reviewing our diplomatic and strategic options, prioritizing immediate survival.
            
            **Evaluating Policy Options**
            
            My current focus is on scrutinizing our policy choices. I'm verifying the Futurism selection and exploring available Autocracy options like Martial Spirit and Total War, while also noting the potential of Shadow Networks and Heritage. This review aims to align our domestic direction with the immediate geopolitical realities.
            
            **Considering Policy Adjustments**
            
            I am now examining our policy choices, specifically whether to retain "Futurism" or explore alternatives like Syndicalism. My immediate concern is India's overwhelming cultural dominance, which appears to be positioning them for a cultural victory, threatening our own science-focused objectives.
            
            **Assessing India's Victory Push**
            
            I'm grappling with India's imminent cultural victory, especially given our DoF. They're close to unlocking Tier 3 tenets. I'm analyzing the Travel Ban resolution and the "Endowment for the Arts" proposal to see how these might be leveraged to slow them down or disrupt their plans.
            
            **Analyzing Diplomatic Maneuvers**
            
            I'm dissecting the implications of Venice's "Sphere of Influence" proposal and Greece's "Repeal" resolution, particularly in light of India's cultural surge. I'm also scrutinizing Russia's alliance with India, which presents a formidable challenge to our science-centric victory path, especially with their recent acquisition of Cologne.
            
            **Assessing Naval Threat**
            
            My immediate concern is the Russian fleet now positioned near our captured city of Cologne. Given their overwhelming military superiority and our strained relations, I'm evaluating the risk of a direct naval confrontation and considering potential defensive actions for our limited destroyers in the area.
            
            **Analyzing Inca Campaign**
            
            My current focus is on the Inca front, particularly the proximity of their cities Huamanga and Corihuayrachina to our key German cities Munich and Hamburg. This unexpected closeness, coupled with our ongoing war and the Inca's weakened state, presents a critical strategic consideration for future operations.
            
            **Analyzing Inca Weakness**
            
            I'm currently trying to understand why the Inca are so militarily weak. It appears they are suffering from being at war with multiple powers simultaneously, leading to significant war weariness. This dogpiled situation has allowed Russia to capture Cologne from them. I am investigating if we can now capture Huamanga or Corihuayrachina.
            
            **Leveraging Futurism for Tourism**
            
            I'm now evaluating the synergy between my current war with the Inca and the "Futurism" policy. Conquering their cities could generate substantial tourism, which, while secondary to my science victory goal, could bolster our cultural defenses against India's overwhelming influence. This might be a viable strategy to counter their impending victory.
            
            **Adopting Policies for Victory**
            
            I'm now assessing the impact of adopting "Enlightenment" for a free technology, crucial for my spaceship victory, and examining other policy options like "Lightning Warfare" for military strength and "New World Order" for stability. I need to verify if Rationalism is available to adopt Enlightenment.
            
            **Adopting Policies for Victory**
            
            I'm now assessing the impact of adopting "Enlightenment" for a free technology, crucial for my spaceship victory, and examining other policy options like "Lightning Warfare" for military strength and "New World Order" for stability. I need to verify if Rationalism is available to adopt Enlightenment.
            
            **Adopting Policies for Victory**
            
            I'm now assessing the impact of adopting "Enlightenment" for a free technology, crucial for my spaceship victory, and examining other policy options like "Lightning Warfare" for military strength and "New World Order" for stability. I need to verify if Rationalism is available to adopt Enlightenment.
            
            **Researching Next Technologies**
            
            I'm prioritizing "Satellites" as my next research target, recognizing it unlocks the Apollo Program, essential for my spaceship victory. I'm also assessing options like "Combined Arms" and "Penicillin" for future advancements, aiming to balance immediate strategic needs with long-term victory objectives.
            
            **Analyzing Relationships**
            
            I'm reassessing our diplomatic standing, particularly with Russia, who remains our primary threat with occupied German cities and significant military strength. Given their deep-seated animosity due to ideology and our past actions, improving relations is futile, necessitating a continued defensive stance. India remains our ally.
            
            **Maintaining Ally Relations**
            
            I am focusing on solidifying my alliance with India, our primary buffer and trading partner, despite their imminent cultural victory. My current objective is to maintain or slightly improve our relationship levels, ensuring this crucial partnership remains stable and beneficial as I navigate the geopolitical landscape.
            
            **Deploying Diplomat for Influence**
            
            My focus is on leveraging my Great Diplomat unit to counter Greece's overwhelming World Congress influence. I need to secure city-state alliances, particularly with Quebec City, to bolster our position and prevent Greece from achieving a diplomatic victory. This requires swift and strategic deployment.
            
            **Securing City-State Alliances**
            
            I'm now focused on strategically deploying my Great Diplomat to secure alliances with key city-states, particularly Quebec City, to counter Greece's growing influence and prevent their diplomatic victory. I'm also using spies to disrupt their control in other locations.
            
            **Securing City-State Influence**
            
            My focus is now on leveraging Germany's unique ability to gain persistent influence with city-states by gifting them units. I'm identifying which nearby city-states would benefit most from this, aiming to secure long-term alliances and bolster our diplomatic standing as a direct counter to Greece's growing influence.
            
            **Adjusting Strategic Values**
            
            I'm refining our strategic priorities based on current needs. With science, production, and air defense already at peak levels, I'm increasing our focus on diplomacy to secure city-state alliances and counter Greece's influence. This will bolster our defensive capabilities and trade opportunities.
            
            **Increasing Culture Production**
            
            I am now focusing on increasing our culture output to bolster our defenses against India's impending cultural victory. By slightly raising our culture focus and prioritizing cultural buildings, I aim to enhance our resistance to their tourism and secure our science-focused objectives.
            
            **Adjusting Persona Rationale**
            
            I'm focusing on optimizing my internal persona values, specifically adjusting the 'Rationale' to reflect the critical threat posed by Russia's capture of Cologne and their imminent border proximity. My core values of Boldness, WarBias, HostileBias, GuardedBias, AfraidBias, Loyalty, and Rationale will remain, ensuring a cohesive and adaptive strategic approach.
            
            **Updating Persona Rationale**
            
            My primary focus is on recalibrating our internal persona values, specifically refining the 'Rationale' to directly address the dire implications of Russia's capture of Cologne and their subsequent proximity to our borders. I've determined that maintaining existing GuardedBias and AfraidBias at 9 is sufficient for our defensive posture.
            
            **Analyzing City-State Quests**
            
            My current focus is on city-state quests, specifically the liberation of Singapore and the need for a highly experienced Light Tank for Shanghai. I'm also considering the archaeologist quest for Vienna and the Paratrooper requirement for Oviedo. My city production seems solid for now.
            
            **Refining Diplomatic Influence**
            
            I'm now concentrating on strengthening our position with city-states, aiming to secure alliances and counter Greece's diplomatic push. My immediate goal is to use my diplomat to secure Quebec City, while spies work to disrupt other city-state controls. I’ll also leverage gifting units for lasting influence.
            
            **Updating Persona Rationale**
            
            I am recalibrating our internal persona values, specifically refining the 'Rationale' to directly address the dire implications of Russia's capture of Cologne and their subsequent proximity to our borders. I've determined that maintaining existing GuardedBias and AfraidBias at 9 is sufficient for our defensive posture.
            
            **Updating Persona Rationale**
            
            I'm recalibrating my internal persona values, specifically refining 'Rationale' to address Russia's capture of Cologne and their border proximity. I've decided that GuardedBias and AfraidBias at 9 sufficiently support our defensive posture.
            
            **Researching Satellites**
            
            I'm prioritizing "Satellites" as my next research target, recognizing it unlocks the Apollo Program, essential for my spaceship victory. I'm also assessing options like "Combined Arms" and "Penicillin" for future advancements, aiming to balance immediate strategic needs with long-term victory objectives.
            
            **Adopting Enlightenment Policy**
            
            I'm now assessing the impact of adopting "Enlightenment" for a free technology, crucial for my spaceship victory, and examining other policy options like "Lightning Warfare" for military strength and "New World Order" for stability. I need to verify if Rationalism is available to adopt Enlightenment.
            
            **Adjusting Diplomatic and Cultural Focus**
            
            I'm refining our strategic approach, prioritizing diplomacy to counter Greece's city-state influence and enhancing culture to defend against India's tourism. Our spaceship victory remains paramount, but these adjustments are crucial for immediate survival and broader strategic success.
            
            **Adjusting Diplomatic and Cultural Focus**
            
            I'm refining our strategic approach, prioritizing diplomacy to counter Greece's city-state influence and enhancing culture to defend against India's tourism. Our spaceship victory remains paramount, but these adjustments are crucial for immediate survival and broader strategic success.
            
            **Updating Persona Rationale**
            
            I'm recalibrating our internal persona values, specifically refining the 'Rationale' to address Russia's capture of Cologne and their border proximity. I've decided that GuardedBias and AfraidBias at 9 sufficiently support our defensive posture.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: 0yesKZjuDfC4Z0du
          - toolName: set-persona
          - input:
            - GuardedBias: 9
            - DiplomaticBalance: 8
            - DenounceWillingness: 6
            - VictoryCompetitiveness: 5
            - MinorCivWarBias: 1
            - MinorCivFriendlyBias: 4
            - FriendlyBias: 4
            - DeceptiveBias: 2
            - Forgiveness: 5
            - WorkAgainstWillingness: 10
            - Rationale: CAUTIOUS DEFENSIVE POSTURE STRONGLY MAINTAINED. A major escalation has occurred: Russia has captured the occupied German city of Cologne from the Inca, bringing their massive military forces (15,440 vs our 3,335) directly to our eastern borders. With the peace treaty expired for 21 turns, Russia is an immediate, existential threat. We must maintain high GuardedBias (9) and AfraidBias (9) to prioritize defensive safety, while holding WarBias (7) for our eventual liberation of Cologne, Stuttgart, and Dortmund. We also maintain high loyalty and look to coordinate with India against any potential Russian aggression.
            - HostileBias: 5
            - WonderCompetitiveness: 4
            - MinorCivHostileBias: 1
            - Friendliness: 5
            - NeutralBias: 4
            - Neediness: 6
            - Meanness: 4
            - WarmongerHate: 6
            - MinorCivCompetitiveness: 3
            - Boldness: 4
            - Loyalty: 9
            - WarBias: 7
            - MinorCivNeutralBias: 3
            - WorkWithWillingness: 3
            - AfraidBias: 9
            - Chattiness: 4
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: dmpgzR4Bq66pFpOA
          - toolName: set-research
          - input:
            - Rationale: Satellites is the foundational technology for our Spaceship Grand Strategy, as it unlocks the Apollo Program necessary for a Science Victory. Setting it as our next research ensures our empire stays focused on the primary victory path.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: 9momb3ctpfKoZojr
          - toolName: set-policy
          - input:
            - Rationale: Adopting Enlightenment (from the Rationalism branch) grants Germany 1 Free Technology and +1 Happiness from Universities. This is an immense boost that can be used to immediately unlock or accelerate research on key late-game techs like Satellites or Penicillin. This is far superior to Futurism for our Spaceship Grand Strategy, as it directly speeds up our victory timeline while also providing a happiness boost to support our production centers.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: aNPZK8TnvNDqHZU6
          - toolName: set-flavors
          - input:
            - Flavors:
              - Mobilization: 80
              - Naval: 92
              - Offense: 65
              - Spaceship: 90
              - Happiness: 70
              - Antiair: 95
              - CityDefense: 95
              - Culture: 55
              - Nuke: 100
              - Infrastructure: 95
              - Espionage: 95
              - UseNuke: 90
              - Growth: 60
              - Mobile: 80
              - Ranged: 90
              - Defense: 95
              - Production: 100
              - Diplomacy: 85
              - MilitaryTraining: 90
              - Air: 90
              - Science: 100
            - Rationale: Spaceship Grand Strategy is maintained. We are raising Diplomacy to 85 to contest city-states against Greece's diplomatic threat, and Culture to 55 to defend against India's cultural influence. We maintain maximum priorities on Science, Production, Defense, and Nuclear Deterrence to safeguard our empire from Russian aggression.
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: 0yesKZjuDfC4Z0du
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
          - toolCallId: dmpgzR4Bq66pFpOA
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: 9momb3ctpfKoZojr
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: aNPZK8TnvNDqHZU6
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.