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
  - decisions:
    - #0:
      - toolName: set-research
      - args:
        - Rationale: Russia's capture of Cologne (Turn 424) and their 4.6x military superiority makes advanced defensive tech critical. Combined Arms unlocks the Tank and leads directly to Radar (for advanced air defense and fighters), which is essential to defend against Russia and the Zulus once our peace treaty with Shaka expires in 9 turns.
        - Technology: Combined Arms
    - #1:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Science: 100
          - MilitaryTraining: 95
          - UseNuke: 95
          - Espionage: 95
          - Offense: 60
          - Infrastructure: 90
          - Production: 100
          - Antiair: 95
          - Happiness: 75
          - CityDefense: 95
          - Spaceship: 90
          - Gold: 80
          - Defense: 95
          - Ranged: 90
          - Mobilization: 90
          - Nuke: 100
          - Growth: 60
      - rationale: With Russia capturing Cologne, the threat to Germany has escalated significantly. We must maximize our defensive readiness, maintain high military mobilization, and prioritize science to narrow the technological gap. We will also focus on establishing a nuclear deterrent using our 3 available Uranium.
  - tokens:
    - inputTokens: 52731
    - reasoningTokens: 3575
    - outputTokens: 240
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Critical Event**
            
            My current focus is on the recent capture of Cologne by Russia on turn 424. I'm evaluating the immediate strategic implications of this event.
            
            **Assessing Immediate Threats**
            
            The recent Russian acquisition of Cologne, previously under Inca control, presents a significant geopolitical shift. This development places Russia, our primary adversary with overwhelming military might, directly adjacent to our territory. While we had previously considered liberating Cologne, its capture by Russia now complicates our strategic options, especially given our expired peace treaty and their current technological advantage.
            
            **Evaluating Alliance Viability**
            
            My primary concern is the Russian military advantage and India's complex relationship. I'm weighing the risks of a direct conflict versus leveraging our alliance with India, noting their DoF with Russia but strong friendship with us.
            
            **Considering Counter-Strategies**
            
            I am now assessing India's imminent cultural victory as a critical threat. I'm scrutinizing their influential status and exploring potential diplomatic and policy avenues to delay or halt their win, especially if they complete the Citizen Earth Protocol.
            
            **Developing Defensive Measures**
            
            My attention has shifted to bolstering our defenses. Given India's looming cultural victory and Russia's increasing proximity after their capture of Cologne, I'm reassessing our military needs and production. I'm exploring ways to increase our military strength while simultaneously considering how to counter India's progress or maintain our cultural standing.
            
            **Prioritizing Scientific Advancement**
            
            I'm now focusing on our next technological research. While Computers are still in progress, I'm evaluating Satellites as the most crucial next step, especially given its importance for a Science Victory and the potential for the Apollo Program. I'm also considering other policy options like Futurism or potentially "Lightning Warfare" to bolster our research and production capabilities.
            
            **Choosing Next Research**
            
            I am currently weighing the immediate need for defensive technologies like Tanks and Radar against the long-term pursuit of a Science Victory via the Apollo Program. Given Russia's overwhelming military strength and our precarious position, I am prioritizing "Combined Arms" to quickly bolster our defenses with Tanks and Radar-equipped aircraft.
            
            **Revising Defensive Stance**
            
            I am now reassessing our diplomatic landscape, particularly the implications of Russia's Cologne capture and the impending Zulu threat when our peace treaty expires. I need to ensure our persona reflects this heightened defensive necessity.
            
            **Reinforcing Research Focus**
            
            I'm currently reviewing our existing flavor settings, which are strongly skewed towards defense, science, and production. These appear to align well with our current strategic priorities. I'll be using the `set-flavors` command to ensure these crucial aspects remain robust, potentially with minor refinements.
            
            **Adjusting Flavor Priorities**
            
            I'm now refining our flavor settings to heavily emphasize Science, Production, Defense, Antiair, and crucially, Nuclear Deterrents, given our near completion of the Manhattan Project and available Uranium. I'm also setting our next research to "Combined Arms" to unlock Tanks and Radar, while retaining "Futurism" as our next policy for the remaining turns.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: PKXyu7e4rB4vVYUc
          - toolName: set-research
          - input:
            - Rationale: Russia's capture of Cologne (Turn 424) and their 4.6x military superiority makes advanced defensive tech critical. Combined Arms unlocks the Tank and leads directly to Radar (for advanced air defense and fighters), which is essential to defend against Russia and the Zulus once our peace treaty with Shaka expires in 9 turns.
            - Technology: Combined Arms
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a1/c7RiZARzOJEecBYM/qKxnBr7r7td60j9l/2XpxBEdfkyrNsC6nxRuRf5vLHoT4Euks9Mdrz7tMQ6PO08vudODIzmVzyM7To8cmb41ZQdwrEZPHy27RuzW8IoBhyCedEZM5ekMGjBO1UxTCyxQTW4R4gR/6TbwDhLioNm6zqAJxprM7Fff3ofmKC3X8YCDQd50jYtH9Sy+nhl3rHcnyVAiWwLP0H/Kf15DuFjG7Vk5u3eLj6IWANwovRHs/XyMDgEbZevuJeJkaXWnBWtA5I2uxY3irfBQBJGft9cvlApf63172uX4TJTDS+Tgn/ajb6QLd96aQYHFyVuDamW3Ebk4V1rXQ+kTLHSGvuCsETzQ8+1tN+oq7nmzE1jg/tXfDd8ehgzv2zuc3Vm80IcRxFih7iCMtR2YqjMkBAHu6raZHOi5Tgg7TpUftigTf0vlN9LrcGDduCVkuSk9D3qE7dD+3fHeHdFFb5UVp57TgrrC5UgAACJzDSBlqBHkS94lL/D8uCjYbRD6XYZwC11m1n5R8FPjxqUf/f96fjHxXQMHbt3z5uX45UzkbmZ0icq0RJc03NIrxketKCONHJgYAj3Q88B8WXDpUwdiXHColDX5niW8ppLRrjJjj1hdAQH1hrOhp3xSAN0JLc4I2d2OwWF7KruWjhtFvyOkc6rXRxE0ZB47vYYh2MtiluAdxLdZdcqTAeZitdezN3Ektx666eoJbUoabzeXvI2ziv+EYJhKTYYN17qkb12aoYZTnjn7NuAE3Pi10mJSK5LGenqz1X8kIiEM+R7PLBX7Uf7QlxvPxpSeWaOOyV41je4r0hB3xDHGOXgY9xGz/Yia1lkAzCpesuOwDBQ2cfWVSjn6kIw6Ziaiw9Rgy1Ih1bnqW1hWgwxer8uf7gErn/mrcbFe/YgiS1P18pryHZjwIH/CnKZiCmXPJnXzcDoYWI/FuZGduy1cXCdf/aA+9vGXUaVudGaPd/zBr3Crk+o2kFTMZWaejOC7WIriXsL62FUHaKEnL+P0LG9njlgcf4iv/5yN7lpCdqDe2ONYM4KiuceT7ebunKiF2vsC2blm5aCT5AChYKD0+c9CMA1fCCMZKJyV0lyD7vYlRY+cYstHXQoMsBJwVTOiyKg+6HYNm7iwXCkoO4k52GtGx5oHaXbpIA5b2pptB68xM14TTiOxHKZ9ZKljceE7Sp+/eOtP56lgNHQM4IM+wCYq4EClGA0uTqhr/IlVuLkkCTkQJn3CMuF6Oe7Ob55/VRKBUhgONUci8hg8wvD8Edp2KVhc54VHMwJC4rgxA4Q0jvOeuxvOT/6D0bWdOwa9iPifQQbRgNQXJVPoC22cXdF4iXwx6FneS+ld1pVNe5jAeAvwGQfIsOc4z83p4wWl++Pvu6W4wO5XZGBgUdfaDkD1D/7d/fTZp0QZJSttq82AJGWaTEBHmmc2GHtwdwLfpNFHCie+/pscTQB6bmdnXS04X3579XenPy8AObcDS8SzVbZVS/28JM9XFdw7BeJMcX9V0NS6Fm7faPso1/kQtcA+NpdEEeIWjLkzDVnQdM0xbmTs3VCOPdOHanf3otmw0+i8jPqLGtWu7Jd8rJvj7Py5RfAizsvQqtTrViQmCxSx1wwMSPBcjL4JXlWd9c6CaZ0B3ijy42q8TUjntHDVu52qMWLlhRk5C+1DaB8HXwmwQKCmp8rZy6lZEYaJx7/F7GvYzfrtHkwuM0XHAub34HKf7l2vvXdUUZrlIaCL8uFPissnF55Yb65ntO7fEKDSwIRRImjgYFg2x0qScVq4CXcdHvH/F0Cy7Sk+La58RnRHeMCHKTLDnr69zNJfjfKvXXURHdO8rXPGO8I006nGHg1SGpVlkYJ797yv+ufARIEMed4DBbj9uC7Q+mnkERxyjKg7F0iNwHyFxrMWyGG0LUMr8aw7ztM9FgZGbPOqqLoPC2HdjEUDp+pKxyWqhOiiSJhHNS12lkRhoKNGT9ifOs9H0GBoekaecqg1hLVjYXW+OF5a2Y84i54rNstKZCBsHFvAFDoKSbflaPpLdWLATEFT06y69IqvrQtuhpUHCd669x7IAJ9DEDFSAA2ZBX7U04b0Dt+agBKxKKPvqsMT0jXp+JPuKpnna2URk/fFxYD8XsC5LEAQTitP8PPxzdzUX3pp1xV+Il3B2+Xph3ybqPdUdOJUdanM+bnEiQ8nl0hKRMeimsovJGDls6irtH/GLqlQXtCuQmhj6oRJVqv82Ev80/GKiwOXt0gGVjb2eY+Q/hzsNFVnoh0r+dHlSwT0W0WXOcEDNoRsH9sXF7v7aODK7/p55ZJFYsi6lbtln6cZRg4DPbjNCC0pi3Z8sbF16zA3CHT32X7B8vKVH23M7dbxDG2rCJ5zA1iaftvkIlTjDqqix8IWtswBchF9pIBO5akS9N7cKxWnvnwOp11U5rJGrAdzDGG8QAJa7A+0+4TE6PzV/xv1KqIYrk57VgP6/3O86rQ8kebWVmak3rR8KqeFhCxmu/SETLfqyLvyp7KCAFYIf9gPzXKTt4vNVkpxtz0cB2/76qR1o0f1epD9XeMCw6pRP591J90LDPPhJRxsBGeb+5JDOI1Ap4O11l4Txh2gkvmWYnuOD+d8yJytv6qArJny9U1fR11zW3arkd16xfEGWWPOIjtnmkVz36bPnOW79ny2YXRJgfnLYfxdJ8dTXumGouy6jl7g7Z/tM1PCWPv51/wnIA4GMirSVt9BL7E7hPBfXcDnyRVJa73Mpti0XPCS53Jy5YkS6aKhQW5iaiMVQOMNbQ1G9rFBTp2Dv8dNhtWwExoo3Or6pdJQ1UB5R4GZwyiUoXZeWElik8DlfJQUShrToqQylLT3gQUBRbA4eW7KIYSlRFthceyZiXfkldsmpDMmTBVRB2FZOnoDUJiCD/+yOgTyLU3sZbQ6OpQm0OR3xopcxY5cTfjsdbDzewGlsU6Yrscc1jDMlws31cnK59Koqnwf0tNwF1c1kqV9JnSMEkJxnZQRgXvuvQJO0uMrPvav/P+mPAhvV0za61pZz+NX+Pjbaf0qfffp3iwYMEkaLzI/JMydafi1t98fEafDxOar+dowC2a1AaOYY6ivoy8P8rEQzXfGaFdsMYMc1+B2GVBjKziD8oscjn4X0RNf2jMT7DPtYNJhMMA/qPpmYusZ47e2XWPZutEvkIuJHJtawxa6l+B9rnhCIiGRjGm/EWCw9odWTTf710glxkLQp+GpgPeIBFIRjm5MHpNn4JgXwgWnOiy1h3e5KnPqWodVx7r5Nbpo24G+P0G7bp+dQ9nJ4azaneFtMe9gZLMvbDOAUzSmCipTzuTbI165nN1dJsGw/F4AwjHS9Rk5Nm2Cmu4kkEeNvBXrI/nsUeRcSf/VUBwDA6a2i7unVwOuMv2wsoaqrg1OULtu+0H27I0Kt6iZOV+SsLIP8yBa4BPXWNRTgMxE0X9mONyrLGO2QDTEmh8fWWHeb4FJ1HIGRaO/vproxDUTwmWG82f0JlIaP5GDTCSXPCUbiu5jLzUk3C1z5sH2ToFkLjuwwdN9G0ifWAkbGAcIj1X6TtxwVQpZ7hsz9OUWjUN2whiUZnZr8WyjCMpWOvgf66gbr6HHHeaY5tGVa7miixzweH+PetT504DvKXLljtkn5mEF7AbUhX/wIAzlTmBebyfDohrJ6U+QyJ7+f0DOUM4zx0fuPFT1fpLLvrgBImGJRdnK42EWZ+7787Jz8H2xytPkVyZHun8n8U4aai3nCbTQnAa47Akp6RzxiqyXzyNW8UoDuPyparseYi4P7IjYL57hiP0y+NXffPDuP955OqKK8pvsGQtvwyKUwTY4kbiovNWBKG9GtIoa73xxs8XlBDbCTkf9Zozi1F+5Vck2oW3LrUkzDkBFyWq38BpB5KltYxZTs/TzpWG2oiv/nMsdp9gma3XPAagcLjR2q1qgFV1RYL9SjfmbR7LgZkE5HeFazP3h0N9vGLlAcBfMvnjqnx3BEnoKdonnWobKWz1PbAss+wdSEzbKDDup5v4X9J6aINnoYIcEKrRhrLzvItqT4Fy5+8PE9WkiKMdi+4+2ppA+c3HWUXBB+P6bW4wd6OqN3KcULJ5xYapkYXYQoJOOuMvX+GLZTLJzUr/mNuk+XmUydi60eK5SoqTZ6Grwp8B+h7OpMuZrfnDzKAN2HKtN8YUYEG9Ul8I/ggzRjz/jHsPWKu80WhyNRr4ZmFgSDJlgT4NBKz/9urcrRLGetAdL33gPq4xoB9xd9mM5sHJgEadoww+lvJv1D9/RW3oBLndz1/SM2XZ/tF99CiffLiuZAgKDhI8HlaH7RtsW903SLwjMYlHU2I81+vLoEv4jpyc9QRKs4kv1KmGPwQ1W6nmqonjrTBgYBVp60wUywEohCsyIrS743/znRU7GypH11VSZfUFAar7Bl1mGE9+ZD1bOv1wh9wz/1zFVZt+oH2ycfdz95CPyBU76ixPB2DbgelqcwIW8kpaAGukHUU3ZQnrasTF/779rQL8GK6spsO8r/QGYDS7ZoYXb/Siq1BF/yg7A5MNVFNb7FVo7A//7xw28tlQT0eWWZQSXZEp3QJwfr2FHdhTcrPjOagYK29beCpiDWqdBKm2VyPKLjc9k7kvk2LE10zpuQhHtteKRXjsEgabrfNf7WFChD5L/EdmnNd6qYco+WTztjCTaBbCB3XD6HgiDWmOKAdhbqgpZZrnwYUcLbTQKTUUBLjTxu3ViUIYvMHDgLE0Qc8dvljTZLcH5VOfs/9Ul+x6vJUcznIqhEv4wy0cyIixS1toQtOO1pV4mug4RddOCJXluNz3Oo7lE6SJhUvmFsEadnIPfUism8PI6F2rFHVmRlqw9VOTrcX3KqPwFOOmoqmlycbmKk2UD2MpG+npoGw/pQzG99ZR+6u9KIQIJKxJE4dkZjyLhd460//yLreZnixJHDLVZZJ5bt1VP7vL7XkmkFu7EFm1eByph6J0r/PVMVsJzzylyOBI0kZUuhOkYmzOc+psdyqmGeTNpRoz9t4UvTg2Ef0pWIdUdu4nutpz6LjdWQAOUSosD+9W45VglFyH+dpctigRbQ0obOWzRUdXuX1z3chRQEWHL75a2UoqGoT5IVpSyGTMGBUN+ShQ1RwgDgRM2FBMDCvsJnM2py1IDN258juA9CnYFAfJe9oF5KDPd3VB6SN23nYyU1cE//Nr9tPZMgn/uSfVlgZe9e29mXEL1pksMFUhsmPaGjWuj5vMK2h0f3lORxOT3v31Ip2XdLBnzxSU4LsihfkhIkX0GYEr1gy205QMGQ+fQJZ6g/hwBZKLY03LZXzRDl+NZk4Vz28FCcmQuP90zFmnBjaXgrywKvkgOLfZJG0gaGQ9InPkOVtFK5mkfSUdzxzAcvP4exGuDTHoq7UlUL4YhpWdrcta5NxBH8rCmdYfZ6/8Jy6AS63odU+uP7a0Gqm1mbAKs5x2phNnevAAwiit3lvETp/qCKU1GHrTduZ3MKsYP8uIIJiAEvcJXE5ntM6ZzqEMwbzUnO2lNZGoAcXbQ7+RgL9j9Cc2Dp47ii85Tl6XZ2v+ES6wPiP3URavmL9l0rMZxoiZ4fnonbWZqZrly5Pwb24khIxvEQ4P/TVDwjR2leOOBpqYEjkQWbW5LtLjFjdFO8nZtxFV0AYhdGvvkOW7lmrjprcA73k/R9GHols8nMH8LkyWrif5p0r/FkrbnIup5AQg1hbhRR//j3u14s2Ga3YP3UtAq2m+2pYAZZwB/v2d+8nvEEbH8BshlS/ZpDWpQseGsmwgav6y/Z2czetK9J1ssnyOHKTgU85wFQqBQsfsniPJ434v9SQZHCoDqbqUBHIR/PxG7zzqWyTCbOwXwBFNSzrz3OT4poDeKZHRGXSXeTpBVlkgmZ8zV/Tav+lwdtjMk0XIOEziXPRZEJxvD4mR6oHpmhkbPxa4450Zux5vbRowmpHmeNp9xEZ0WLHruDER9rEinHv1aOwzr1+KBNQAS5W4BsdkC2Zeuf1O0MPJzkUPh/Kgy2CGnhaqT2goURF1NUvwmuGWkBVLKCAMsD0Go1M+//pmlK2wK1JDiGWuYr+UsxJIUqqrzxtw+JWxrsXazoU/2HF8mQEc9oe+XPVAD6DwlGq/4wzTdQHyFA1VsYnfD5nYMVA+5KC468t3D7U3QKo33MNf2hkQZwz3AceeT28F3wi5/IuylpHf14xfF2E2YNcms0e8lF4oxv7aofuqoCVLTZhfUZlH7fMevkVmujiesESnfbaKQ5I3EzV+8Bl791GICSpt5A11c3b8YcoUm6FWagGiHR14MH+3Sr1xt2PTa5A29p2ko33fhuwTBZmy8EP5TJsApxr0tF06tmApDV6fkJSWDGK/idW7V6hLU7F8Pa8AuivEtRZIC6AtoSsUavHgsRDflVws6eSLzKPPIAsFmggEZH/Ox/D2zKQ1dv3Je/OK0Cgdge1dSBxScI8TG7RwMCR+Wm6zAlzrnMP1OCxdyVkfEHNuvvXH2I2dORjUHIJPUC48+TE/e28kZ+etm3iri93s8uHZWL1kgi7/ZjKO03c/pbbgqwfCtiRH33rrTLPVj0vUjcSdUKukEI3Go7EfRZmRBe8rmgjEepTdJpf7zu7GrPlPmpNrvcVqLwjHtH/whPpQhNFDm0MjMzR/09ttLTSK7Qx+7oYCJzyUjnNj1xTbSyLOgBRIK/A9JdzGCZ+SdBfPw2G3uOV+7QtjA8ZgxTQRWAC/adhHlQTeCNRH+FHDB3l364Biqx3S6/3X8frRAI/aL9BYDnnRUAwaUcGMVbDnmgrK01BBzOebPi2i13G9Qvd8iMlyiSzQQbil/opcj3GYs6Fua0+zfEe5B2jcVtIB9Dq7X9WbonVwFLX1c5awae8PtHvQB6apR5nVJ53KAMRsJ58OLPjKo8OH8i8jCbYNC4nqvbXW3uhoaorzIV6Ki8VKOStHMEPq/jMB7kVseKAcUs425ppoKk3HScCW2n6yBRRzND9RFFFBFPI5fyWY3k4TZY9CGHho6XdwBNQieQaQwE3TECPI7j88URQkmuy20MTUN/wsgULhP1EENLi7ZD5Swcsg03GhhAlpad/MXUOVH0WR2dP2FgHqPpsZAb98T+D6CmpfWssgAqk7Q4aYB/8w8Db0/hnHFb6njef0I2Gbhn4q/qCN4tlHSqZ2FGjA0ABgoCsbxxDsur2f58JR/mU+V5rkuUYvtVao0Xr4mdutYevN5tVZEOWAecNWWqG0FqGfhF9tGZ1IdQ888Y9E5Ix/ioi0N+KR1e+pq9GIdY0nBaKOwyiRJfUeiisCjqA0TDcOAmLFQJTODISFND9YUyNPciKwXYamPt2K9HRaENHge+Lw+JIbm1gZ88basQS2a0C+y6ILXHeWsd9wwaBRs85Q1rVAC5BUA2NSD9EfubrPDVTin3W8DiKMs2QxvRwO5oQLnxkaGwUHLEwCdCnOMb1IVyNkN7x8imq+HlYrhtMH1RYV7FixmvfPvKsusPQXbU7ioLeLuO7iGoWwHtkvMeHr0qypA6rH02GrBFsLbFPPDBh9CQpeptO6L2ON1kML5s/Py3LpNeXjTgdm45JBzbZYqidw0fvapyC7/nrZXXV3tgQEFropEUNB6dt8x+cl1Wc/jLFT0Rce8DyvnWx+y57pw5kw1lHJppqKIKwa3O6pNxpze7U5EBEouT7faFjeW2/A2fuIhepok9OV0dcg2VDZiyfKxfHcbQLC3ArtBDmd8yGuOMFRlQq5FsNuXPhgi4AZWhjPouRc5fSWi5EYEJf+7cuT1baPTLhQkqoPeMa7sU/j4W4YG4eiVWOiPAnfsr464yTIkbwofFt0I4A29YxcmuZuQtowN6hUajXAQpxZCu8HxT2U/KpyVDEPd9Xw9JO5CzOqXoh/jVtVsdM2mpmV99f7QSRNIjdAAcz3FipF1k4wMzHDwRGR9Ht+GZ9A2mWkDlK6fFkSkrguL1zymZam0e7MjjGcKdJvoDP1M2htYkGhbIMroyDLnINicuxzAze6r6s3/tCbNlJXBOHWKZtFmAYQNrgPze1y4vQdSWo4KXiAHbJoVlFkUzAd/LJyp3WGAZv2HWoP9spkknhJnDs5d3w+e114uCRDfWWNsXW6ZUJML37HaKLBg7FIzegy/cEXAMeW8DK/Wh1sxgLQQ4+L2c/6p35LQQPskgPDN1iB32JS9oo39riFOfyoEx3evYhcyMOIn2fneC5lKjRjxn2mHjZSR5xtxvCWrdxqnqmZPVnwzpTxsqaYQD0tHfOP+/PzfxrLi3NGK1hg9XhlZbI4beie2zQQgdQJ5JjhUEdOetph1wxcIIH5JmLwVltg3aKw3GMS9Y34iqBdqxDHzIYDz2KdG2H50e4aLC0AVDCKZauW/KTbtSSa4My6T80NfTzW4Y8Brjkm0B5e+DuvYI+j94RuiSvJR/IE6B1Dtw78+k7k9DBsGBQyy21yLM41TiCNkzjHQJXT3nX9d+DKKEvd1ht0BfhwVGUqw1YpNsiIGDf/Hbb7zDLS58yUwyqaTQn5g9uXPF3/HSsbLT8vqrCI4seQ1byY1JKFg8qFTQOXE7sivdMsh7xaLhNhQPmeVilOBDbbGMUwBK1fUBlWxNZPu4B2gr4WUc5ntwkELZ6rzIM+V/PAJezPnPMms098z1rDiIfu+I9wX1aYEDv7hdj0r/y2GAcF6/tbXuwG4wUFBxYAv7Lneokbk+uS3kt0akUrYaXVws8g7eXvso2D2wzTuygpXIdHdI203WLWVp+m44BwZTHbjVE9kQQ+NBU4BUV95FK/U4B+hssu0CxADwrKv+EfQ2ieDW9S+lG6sgwOOkO8CmoBZ81E/0ksGv2kx8vR1+XyDc+dg3xuhnklnfrkDFAlDz/jyntF7avtKYr4N7ZAHzLp9YPqy5DcbHroY64M2ItVE9Fq2bT0S9aEL/h79NhMKbCwcNnCpPHtp7Pj9QyerufSJZQFcVnNjZFuI2LC4kZQJCiZK/uZMaF9OmtYMuv+4N53pHxN6ydWPfdgxEWW9SDZTTeQBHg1ov1EgZ4kCsdy5ptzrDNfrx1LgpmGYF4s+Ky4/9D5K+7oiby5YxrP3uXvFA2kp1yW8bJ5LZok8lZW2Is+fu14hEfxNPJDr5go69YyMXRHLWHguEhVSztMQ1xZkSzxA5Ry4zln7uYc8px53zB5Y96xkocHnSa+bEaDVSMJlDzeqXoJq9GtQ3Tv9taN7j6Bf8EjiMyv6Uu8De9ehVPnlYcd74yFJf0M8JKeARiWmdfk2BF8VQUMqDS+VghBfXE7YgwKnGhR02CyyIvkFcMSh6trBdrst0T4RCnUouPFMOMdK6pWn+/xNzCcj4OYSRUtcMh7/ZZtpM9n0VkZbPFvkGrSCDjFHB49BUB8fzB/kRNkPBss6hUamIG8Ye6ZBKUvDfyAp9rWQ3+8hsRf80HoPN2cmdluUip5egljSUVlhZ1HbvXzSpCiYy7124hUdb2EpiAnambvSV0ZwiSDzJ45+YCrz8nT6ca2B8/wvmnxgI8FW99zfZcVeKNYS9PSIlMy6ERtwlqojOvJYOF7rBvSzJ0uvN/SrBr7bBdrJEOtN2Rd3NsJ/AWrKhtSRXnJMIHf7SckcCncR3zWLBuJvFxkY/Zm8SUEyyTV/eh6JNTMdQQoLpclC8A/FgzQ1Leqs2GWxoKUoFBmfVd10hhqQ7Cc4QG2zltoA/HMSP7sGZXp4X5NWRBRcDnnqZAGD4W1vsG2IEJgOxOoKZPvbo9J843hTL1PgdiqxB7E8kK8dtOUXkDlAdRsVRX5My4z4Tot8wgHT1G2l6s5le01kXPHASrGy5ijjGH64EsFez+RGxE0/ZM0Dcj8QF0ok/kBinnkajNKfHHRbdd1HH/V63+NKgoqyoA3SwHQLQanpRcVAedX0WZZMD/6WPodYAT4QqoPO7LWc8iDEu6MGKIbwYusfkM2FpVLBWmT9G7BzRy3QUQ5F+9xDv9vWY+3LWhfLlsV0rAgirwVEimhMzN5khYjljE5Z+nl9W3b5BvZeXYMYodpdaqNH7/rDeOuUjylIpgDSj8MT4LR5ShOcZPt5x0pMgLp6bKjKzO3NJAK5unicn2ThopvzB6ByUVwgSIjFvAHamcMj6ub8gyHgGaIRTxWDjxErRh6/Mtw0m6kdR/PREE79G85hWRp9BbEsnY1NXKA9F+/2fRoRJ85+ZIfrGwvB3isviVLvQ7021evyOtLtTEn6cOWBtnjKRSWHkuSWbMmGe8LIa1M/qCqyKI0CQ9e6DQpVwvVzYaTJZsH1cu3AKZS6M3m2wPtLTmU7ERWPPB80HlcHYFruQ9ZoiPgyut4jym+xYbcPjksEwyPyQTJlBHRcF/iamOMklnfvgzVvNAjNwVJ76Isf/cNa/PBaIkHu/Xur6jocJPrObgEgEa4Gk7bDNBBfLw9YBU3jPk9ix1R4Hs6vBVGAjXydG1VtGsvGhFpFjRWjozsor+WrF/epGTe9z4e+aZVa0wqKguCOQ5PSOCeI0ZLZS8bbLg9jxOzIgqTJBPGqUaVdjWB2DQJfYvku14lZqfeZ48ubf0JLTQ0Kqcnp6V2qqMlATJGZMGcEtlrwekVpWX6J5BjjzndbX+MqsyYm2OiyMoqIkLON57PkICKNSxNIqRWz3mt+OtKkgvn7/VhTPaOlWjEnp3RHZyZNMbvj30ZVM1w6jC8HdO1N/K1JbQjcQxKAaCLF9E5y6BSwodSZkuKvmPTZ+7Lzv60FQ2/zIgPsTJNNFIfaP+/1yIBCycVfId1R0g43H2OfpUG+yJLtGnZg8+pmDtDlXbppewS8OTdU3SnVy85ETt0ZAmopwQR0QMkosePygjcKEVefpt3W85u0KUV+uy5FiNFGxxqQ0IldlrvWgbl47EbY/ueVm8sgctTvPjtZziyovoSEPRCKMcgYD1Hp2wtCls4mx+4al+taCLTguOFURIOP9g4E/JXBIjARX0+bqUKN/Op8qoPkjbtp0YgLMiv8dv4KkODJJJJQRtwMFMsM4sgn6ZdmfLOAD/vId91UGgtRqCiJoN9EJfXKZzORO+euzplMBxHpH9XkiMZoS7A+WUy5E2BP/MWF7/C+R+9fxFVvNl5qscVXGavKCH1WToYkV1diNGJ2XwlDi9KSB1ABKIrGUI3Vf+a9jP+4bL0/JTfGeLlXeG+X3AFXdMkJbY+aoOAc1knouhHpBwEOxcdaS2/TP+KgucynfgFTdElSIEO43QyQYOOOI+6OONG8Tk6fxIxLrfw+g6Jvb2SLlYexNtDYDkFCC88Spt0nMaNX/FQpZnjbDAfJ+OiJUIbqV8RHzfWbZZjXNxWCNQnELiNh0rnn96wAhABQlqEIO7GqAyRZlV9sOjM5i9hHahcVCUpYUJjRurnsAWHxRrpqlIljK0A3O05ToUzkKcli++E+tDS7cyF57pqM2SMNOb/aCw8mwLvb0UDe850Pr4+o1G7iUG8NizoMYN1OrksVrJ4N64PLpUFDLM+yuLfM7gHwU1EgMxSNKFphl7MZQfUoPH7yWt7IXt36IbcHLW+UGHenX4I1OAAYEz9F63a34oOkwHoQlPQTIBt0P63xyNR2yXCgZySuNZ3rTV/8zrgb2zxIthoX3WkJT2hkraIoVY3kkzywpMvspffgPj+flguNb3YTufP4pO1euUvQZ5GPOE9pD9Ch5002VCiYaBa+dycBMHijfPKPqAEql/0TyYfUSxuz2qwOLYzh8i5SbWNW3LoK3Txb8Zh25DjVOtzF+qFEABs3CQ903xGeikkCsDhVGOjxd8mw3LHLKNE+lXzkadf62tSy5mvtkQkIT/MXWMIhVSXSA27F9Qr7LhHbZRuVQUMwFrwP95waE5YSHi+ldUiTJhBdMSrHw19+wXocLrBzpuajax/4knFBQQtWKLFBomX244i7I9LMFKRDhBX925fqhzG0noE71k5DU4ZM3VTL6m4Q4UFxH+lSv0wak/9I236SIERakvPabcDHJZhTNS49Rt/Yb/lO3ca3n0vsFtT6maHqjbmY8nF28jCa5lOOSPAMETFvKwvTIwAKBtoN9APXil0VmAI+CvULC4rLOcLqC+FcVk3mxtyO/AtucuMEO3VU9IQaiifu+hj0IHd8C9uoYZXkPHeHAOumB7wWgT7ISivMVfeldirgK3eRln+pz6UYHdeqvHRWrErBW/4cbFqUiy5Kym4x3NIURktecFjDVaA7p+FX25aFIpEOxr+F9pUsDszfufCsKN4b7UohpPFKCcDAXmwlPwq5oXTCvToPutyac0wLn+nDoBht4H6V8gZA04MVS/98041pcr7yLFWanl5+vFwGg+ujIOy+WYPVHWA09KQuKO30M9eK4X56Iwo+YMOiXrQuj7hOMZanKyyxf4JD8x860Vz1Q0vKhigd98q0gPltGkMW3FcK3OjjDeiY+HHS1ifcYd2eRncD+wMpwtVq0UeArz5ojYrYxKL8hQ9rM+EGUFZrTyPc/5Op5xzX3efy8cH0gkfWWrQiFylF64SaPc7rHnTIZRKUK+vyd8NnLHWudzmDoxOCT+V/XkYYgHI4SvyPzCHoJG+BTpP/x2y2RMuHroQ7a1ZALykSizwtxXrDU+zggoG7yCp6d3OuRGYZ9mH7lp3QhVIMF0kwm12LayloFijXSNBlBh56rxve78+mKt8FyfldV2gHvUmMslscKDl06cC0TnBL93OwqQgOHePup6L0Ao2mO8feKOEuUuuU+RPocHTHHXf8EPJXBRPI+F9v6qpzc/hnjLyJJgynFSxd7EJQKaWZoFa7ImrwVplb+bpNZrQVYGzbnW5WiP2BmjAo+zOVp1x41ttBDk5ZN5bJ1mS02TYUwG7fcLdOzal1UlFuYJ1T6TrDakNUD7Z+ztvARgWf+WscMJ9cUt4hA7x5HMn4Zh+9RsCg9JMKfa+cfthvXVVLm9MKCBYS/tYq2X9v2yoYigz7U7zaxC8teW4zw7pPK55OoTYeCNSxP7TAxAzE3Pw+xQg9rgvrtgPRa94kAvPkS5YA2flPUxpdVg8xW2P9UXGoItsGRyoD8Pyc5pbJv3xuE9HqKkdLMAknqSuU0x9BroW363o7lV3MABmCEB3oJBk1Qrp6z2T25Rcu8e5cTc9PwyWrZrCYhp5E68/c70CXq/qQyq4+NM4uU8C9ci8z7jWfLOniJX0AC9KFk66jbDZ30QDVosCIcEXwJ96OGRJZpxOUrYOXegQU5OaO2rVzPHeSDtsUYPMIhtOOjCzsdJV4GLJEt5S9MCgrvE3ZWGfwwI5lyfC7N37BLMxWDohXnCUxYHgAO/IW0NYv0/QCQUdHghbE9CaR42LQbZxAmpwFQjyp0nv0N/MpyLe2ZABgrS7y0hQKZ3b49TLnzuoOi79Pd6m+1x9/NEWA9T1wKfhFuLqIFObES1s04zX4L4mT+/zGV+pl0H+LEgBx42DcIk+5xwdk97VBGckIi2fdatjxjCdbr06zNJGbg1FI8IaQeuxw0TNCVIk0DnZukIxOVLu33ceMJ9TAQs1SOkkpifM7RPAa2H2FS56yIkyl05weKmyBQTtzt/7ItLGmV5ni4t3ffWkkBIKyDEw+p2PganHPJwH0L4cZdoPe2FB/SUJs68Qae7mLHzU9Zelh73lT8E7A2D8YL9ouJWJSoLZQ9T3q2u93l384oDdI9Dv+QRAST4QhN87WjcIyTwyxApnpXXSakmRmofB6DOyC9eC7mGx6CkHx0lTL2ybslGdnvFzyXUZjMvL47d3v7WtXkNbPTNffIlSPAX2aKEIqNVd6lo72goUgHQXG2e5bDK/Bp6LI4q6/ufrGlkrqCNQiLcJCySchZO5dQRC6eY2/GByY94HhBGsjZzgK3FXkDJTI/rbl3Zb904hRMY1Ax2mRvcCRYC7ff8xElDkvSjdPJHs0q709smEyZs9RjMvmZkzb7Oje3X7JqndPSTVhVjM+CjeYxwRICFpsexodsxKQ+qNhLJD7bhEejXvmTlqyAsSlH/WWgvCJ3b0R8sLdaSYJC2A79mvR4j9rQyN5UOQGtSCVT40WWMS9JF5UbW4yaixQeShzrA2azVWoWuXtj5oULYAr5IpKsSyvTw3QU71HXeDZdEtnZJm16DLnzZyBZ/VypmMCGmoGW2xlT6YMADHF+H+GZUe6ATxVAKcSFTMzraHr1h/bwyq+OLtv1nKMNk+etCWGen4m9gclVrserTGRvvfJImdKDDCcEhxhlQNK7snPYFMuzn+phukwWTruFThYKKSwom2+MUrb5t39eCDjxLcD8woZk3LybzR1jvCqzZBVPjI50xEx9vBUrcA35wsw7pSt8MByLAydz+oyJxKRD827WTAwSl6ESab2bFrXphf/pVEpfdgkTZeGWmooPVvNtQQgJuPr5PbMBmYyGqI6Ukfatjg1MoGMbg2Z8FU5mAAxrau1NquJZEqohpw3v5lStYa7kjsDhVjMz9kXnV7fPTznAeSeDcICq5v9iY2GuUZFJglh2QPhA7DLjz+cEP4WosBxH3YdxUCtcUvxIwrZYjg6GTefG9BI9M4+pV0EpGNNdRTZ6yZVpYe93D1/5LxDyERCtcXEx/ZGZc0eN1up+waQi3l7t+DO8Cu9rC1XKRs3JU9lNXAfrp2AM3nQ4OnSvER6ipysI6odg9Tpem8RX95qCDpgWtTGrc/DhHVrcvSahVBI6W0KKeTxO+viVg5cLqS/gq61WyW0M6Qigd4O8PIUGbvvcdN3d0Jt8oeUUT1ib7HAWmJ8N1CJRtpYhJ3yh0VffnWTCyIejTnJxbQCCszxjhrhZFi0UV/TKmc2nwZ34MF2L5+IoaTdwXKAWTKbjszkYq1wfottb/eJLQbi8ELXkT75m6VBJLMDPxN1bt4ftPTKUqN3CVadZcJYdR2gfKvnFmmzAjFZuHPzaLbNwksmidN+mcSDfyDoj1+oELcxRLydgU7b8j9KpjMbu7fmfw650feU6d6+HW1BpNcGkgy1H6br6QbJG18p1lG67huPYgBlOmRN0CY9nSalfvvKAgvzZZci/rIGoRwQW9PHh0g9276BX3BhY32MUox7kOAx7bbAkfn+75UCacVh0wABvFx73L3RGtiTc/hU6A7Fy+7LppoKiOlIhzzzZzmaCcysTUvNTKLwwSC0RYKrXJU2i/zxM5aIgQfzncQ1OGwhkS56wdp4ugpTv5GzfF4OQfaZP2b803YZEsG+/09APRJpRKBX2GV1/rTrCNBEjz/06P4wsUM1NuyAfHtaIaH1sB0oJKm8kc/mBEeMsDJlVf8p71n0dVig5oGQD1XOPRKNkWYSSdoQ7VPmkyhbVAhk8MwjUhLNe3qwNUUQQCZAOYZxlf7FW2TQnLcI7y8GgV2jk6hq4+P/WsGhyajwC7x//Heup/5b6IeBKM6aMIOWrgpnbowJ8Fb/XSOJXGrTbxIV8CNU6zMChztc1qmHbdqyEHC8QyYl2BRHbwTqr58XlAiPiHqKuTHFLd6IniKJhykGJQ241jYFmpQ/u0k2sAiUDHJRmw6spffoGXW3Wa664scn4OHBk3vXtC10v7ogXgM2OwfIADFPQ9541eKGI7wCb/u9KnnMadnlgL/FClzHqbyUKaNRRAiJ/80RnRHTfc/EKhx0QGJ+xzVBH0wTUnL6gI8hFSKf8hSBt3rZGS1S95G96wrU3pMQD5B2/+kR9d//cgFP25zgD0Q49xmomf/evcP+ZGjrIPsAp0m7gjwiDnUy3WBT6Qd394Ypp5XlPyQE8YS3Gky2HrXRqNl7FMJYJDs1s0/4jYyQ5VMwkvgtoqAfOeKDo+M4FBiq2yOQonv+IUSkMzUFDdmcS5g6FDYtEGJpC7f5fJcHr5VVVtQkJW1hynXm6C3mdO5gb9YE6N/ACm+C7tu5VzKwZdOdfr4k/CCCfmsaDJBs9IfBx1wJkXETOeZxkTVDZbNEsFrvYVFg+p8I7Y3mdVBurNd+9tiTTTfDo6T6oicWqrek+f4PhROsHakhVS1SXtwLL0uoGZ7V/4+Bv/HLjpHpxM4VS+HqbyppkJoBbDar1ntDQQfmSuVVbQxipOaMkZ2axJYlHPy6CriinXgXq+fDXcK7eZFa5Dog8XdYKLh9CmUFp/c6qyC442pynTLpJm7+MtE88ApZr37W5NQley1Yi6vK+HvOxsE9zho+SzM/MKZqeAIT/N60ER6EWW2q1GMFrYlaMLUYXPSO/uyqeqOkJqX7IGvsjMglUlQarsppcz0qKFsdrHAinRZo/mZvy23VELamHA1gycIqFbGsI7SEaPmhtB7Lk5WPIjaebsPS78nV/1yZWYFuq9C5UMd2IJgE7VgSSl9LFsf81vP3fc/Yg5ryQ1i7Vkz2b6Vv7QKInAkfHT3zhg04E4oVvhccgUl7M7DKjHMUzKi34PMro4w8ibTDhwx82QZc2nUIGTkfz76VeuIy8Q+0tguoX300dm6789QLKNv/tiAlomibKMdWUwfqzeWUk6RpSssATTSTMqZ+UDN+K5nIssE6rYxzhyDPsBN3oMoP2siFfVAK7TdfjqyECk8gKX3x6Iss+oL2ZNFmzbtKuTB8bs1E+s1dG2BJNSGPpVoMYS3VOvjPOgrhRGaFlcz5EV0T7coLzDqDvTb6+36FbgXygU4Rf9VJqHgkFRZv2bm1YrLusvu+E7HKexkjc+kJ/m66BGuPltsXUfzViXtQX9SS/iYrTssa3jxifgkr05Eec8opAjX57qpRFleWaNcME1CO+6M5I4Q2sZkZM22tM1j9mdih4umov96dQUMJ3LuOn2M3fPapTpMT2osP/lAMMUGI/5f34+DsxW+vVtljoXXuSwKaaC1pmMinM+YSyHbDT1j34cT1e3+D+dyxkS8O8khZCrr5eAqrhDwuqQ4fCxbXwRsXGMbPkn5aHwxdKBfIiJV+N8wq6dZFN1wllrZnpu8BvkLG0y/C1/LNRebbSQqpZqH72XSe8F3FlCeG/qJJA0ftc7h6qypWcZcdmUEvdGxtYhgNeEBEVkwCR8HwM52BL1L0HgYE+LPzoW3pDMERQzHY2Wc9UQ9YsfZ3p8QaoUXDHDQLrv/k7ijvHFSQr7cNf7+A15NlynOiSKpHwzJ3fPzcv+V86uB+H1HztoNHOVrrayi4KOL0uU3OQ/Om1MMmfhVPv3oDXk51qEHeRCY+m4p7y/RQw2H5fKgd0zbFMhb9Tsv7kTQe1Mn8EE7OtI8hNiNcpiI+9akGP9N86CueoEH+yvPvTOFyWUL6gEuT3M0RUWJde6Un2uC4YgVtw7cN7P0yZzFPVtXH5sFoIyIWmWql/8KeLjWGBnK+KdatwiYYzWVNnSceSoh271c6Sf9uHfUbk4fThmqtNV7HmUmJDdn98CqNpssETv2YhHpa2mk19oMY9baYq0GkeYZ6aLBup5D+dvBwYKobZFgb+cCtGuRUh2/mW4AJfUcHLnfu3xIlk1KnRdsbgKqVBhER1fzMRQJpL6ITvpdwV4bRe0IYFZ23a4w+VtmSB3JE/8hgqxN1WiGDrCnTHNhVIZpPCf/nUiY9kg968OFJwXBcmbqpiAs89VVDmtFbSqar1d4h9qxqxtgQvYi6lFmbBZpWXMTZfGxqq9/6eHcVSe9m1/xS2VOuUmF5NquCOlnV4IfHSnJApPUeUtvZDvwmE2w2B+k5nw1AdlyIb5qPkWsOnngfHfy92y4goqCv6Gcv0Aav41EITLgGZG2oNI8JB84M5HwRScnMLzUNtIHi6IrVcpXZbZ7sGPzZOpnvxVTlgYH6M8VHU2PcI1HSYzvLyoA6msEik8gtLSxNPUmv7z5ywnJnyqDuuUV+OYUZpbgqDRdHoRNZ1+EKjxHmSH+F7PaEQtBFIpQx0xdI7qyAQXy03Vsf+75AIe5UPVrGHzve4236RFfDRHBszTk1N8jjT/e/pWG9wJj4/+Gxk3sSk1NvtnUmUct344zGdNF4ntErS9vXg+BQFa6+9gn3c7/G1Wl27vGnwGgwgaQlj7v9TZNz3RkIMWwLLWTUYQhZexTlBxq3T1a40Rx8E9/OVm3F8N1qYwagehU2nTf58CTXfyY9vl4J2MSmmKK831AuvomWy5Eqs3MMxrIAsBBykQO6J3S9MavpRakDt4wmrK4TrN2WmvcjXoUxJzMQFWM7xAVcB99CVtb/cduvFeA1UKR48hvkFU/5f+vNKYse/OBwaclIE4IptYwNaXdWB9jfOvoqp1D5X+568bidXh8cdAn3AK33cp4gdDsvdMKz6vAaJud0/rHJoxr1JhGoD32S6TwCQYdR7umRO81sJf0q06LXN27YZVoXGMDx6hFO3Csj0lcfL6hoGbfNjJpjdClH/k2gmo3McKDZ+hM/mxeVGwJ0A81XmCGZGbTmQgd/diGVfucj3/du5PmXnUtb+WNJNwCwStaorzNn/sBszL/qVpgQdKj+dCErP5YtbGS7esreS00SLdP09GaADKBVF+hwWChVIt3C+gSzmCmCeZNtFF9rOzMX2l8kD5bU14n4GABQzGIru1vX2khIxRc1m+KlbCTmvO6phTMKnPXEagN5McCFxrHvFZOUr3HMEf+EnPvS2o0nmYvOeyPxkM+qWG9qSenRch9AZcZsnlqkTNMc9Nq7SrwO8gLC9cyJYn59dF0SmyFlSfwI5RzFgdiJ76DtOEu6mBqHQzwVviGTKac9RhlBnBfPnbH9tcZAoNvQ/JxuP1E5aQ0vSeV6pMkSUaxbkPRGsffl4pjdrOXmGhcohmdwtqXaBJ+J/KLrQj0w21PcCWFgeoM06KluPNLvG7vAR4UjG8/LDDn3ti+TzHdDWQs74V7dvO8lJn97yr0YcgBWxUQsLAQ6cd6oewQammo8l6fEfVD9zNem2BxGeTpi7b/0tPdaGSxPef8lr/wM830OlhGRKySpZ/HvIZkbYYO9E/9uijy36CjsfE0UqLtR55cyFV3EN+8S+KIvQhF8HwmzJsD4iSJUnf0NzqCao6hkNIzk/GHad7mC3ZSUbT6KVu6JbJ5/ijxtU4wYpJlJpEt+SUomIDowmOTG843Q+EiWGsliyorUJMCcn4AXNzrhO4vLi40cUQzTNniBe7fyXnWpZf9TiQW1m77ejYheIxFUtZbo6VKZy1uDavXWY7EvYBVNUBFJwrZ3Ei2xlPZHnIA1FgsZ8kSKJjTgXlsTTO+79UgpIzkD3yLcGE4Oz6YBIc4cRT0xLOJ+vtjNsvn0zFYpgG9lW+D48Mnsu1mR11A32FR4lT+EclNfWvDtLlXomtzmvGl24+u0r14x0haEruIkP0ukcE7p9yl5OUzEmM8Mn4Vl8MxhjFZg+1ULgzNCZxju/qz7UONp5IIGHhOdsUhTgexT4wXGyfRpM52uZkHnbztGyeGxRiS/UBffWniApZEBChdPbqoLROwJ10PCHASPgd54qRZgcuwAT/c9dd1KuFVvmIoRniHAAahWLKzp+uXW2UlGC+C1qJcXtMhZpHE2AcomqzN7IbJB7tsgdR4w4UAHRRCwHRjDiI4z2Euk74vJR9McKoK0shO0Lky4odPd25C4Q/w3+Q0D1+20g1IB2GZRL6Y93R+k1dodQC0F0sjckyAHNe5+H4fTC86OLu8ucmOqAWvg2MZN0u0of4b0ebOEvXkiGW7c2+E4XPt2H0e1khgi7dlUBMjCaAn1uTWyvEvz058nYrXtIw56cG0LrkT00oLmToifURhbSNeefrFLXXKxg9e9R/wxV4apybBlOJcK1e7mkucqAtcJnLTNyqnXPrlEjUK+WEsPWYzV1c9i2uu7BhJ0xJsJ3jHwvLki34jJ8/Hpy4zkYdNaxiEUaud+n4FY6jwQVQmWNWJipHJ7lA0RFHELB/GvYTK7wgwnKd09UsRKT3F+mcL8V7u7+7ryCypU1QXrEYjyaNVr33kh/NRvqXlnVtbO9GrTXmHA7rLTgGa8sASmFsEjXzhQHk/fdN67Wm+1vIX1DihFyu8vl2c0nYj+fCqaZ4S+Vg1IfEXpTvTWQR01fyjEs7fe7dTwCL1Y2Pej+k+es4y2F00avRUuvJB90LixcAVSpVAXDFPfWZeRm9XHVvJoyu8NcoHC3F36rIBpqlOlP6+OjXec+6DDwTk0zoWOkEkvxOOVB21yRMQuYoC8yINt8oOm26dWZDpyRkWsnvFOrJaWrSJfGmWB0HGeHbNiHeC0EHmP1NOyVglIhCwrFUfAn06SOACp69qcgEzTwcEWA6cHpcAI0lZt1YCht0HR0P1Ugn38AIanLZwx4IjpCCkvsp3Uut51ULkPUV+JKdH23ibvVchQYuAurLwXjRDJki8l5zWczaBU4PDqSKULVqLzt1V+uoE=
        - #2:
          - type: tool-call
          - toolCallId: bBk8Z1w1aqxNr1MH
          - toolName: set-flavors
          - input:
            - Rationale: With Russia capturing Cologne, the threat to Germany has escalated significantly. We must maximize our defensive readiness, maintain high military mobilization, and prioritize science to narrow the technological gap. We will also focus on establishing a nuclear deterrent using our 3 available Uranium.
            - GrandStrategy: Spaceship
            - Flavors:
              - Science: 100
              - MilitaryTraining: 95
              - UseNuke: 95
              - Espionage: 95
              - Offense: 60
              - Infrastructure: 90
              - Production: 100
              - Antiair: 95
              - Happiness: 75
              - CityDefense: 95
              - Spaceship: 90
              - Gold: 80
              - Defense: 95
              - Ranged: 90
              - Mobilization: 90
              - Nuke: 100
              - Growth: 60
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: PKXyu7e4rB4vVYUc
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
          - toolCallId: bBk8Z1w1aqxNr1MH
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.