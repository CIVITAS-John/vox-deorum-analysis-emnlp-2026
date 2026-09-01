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
  - systemModified: false
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
      - toolName: set-policy
      - args:
        - Policy: Third Alternative
        - Rationale: We have severe resource constraints (0 Oil surplus, low Coal/Uranium), and we have active military units consuming our strategic resources. Third Alternative (Level 2 Autocracy Tenet) will double all our strategic resource production (giving us a massive boost in Oil, Aluminum, Uranium, and Coal) and reduce our unit gold maintenance costs by 25%. This is critical for our defense against Russia's 15440-strength military and for fielding modern units (Tanks, Battleships, Bombers). It is far superior to Futurism since we are pursuing a Spaceship victory, not a Cultural victory, and survival is our absolute priority.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Combined Arms unlocks the Tank (a powerful mobile land unit) and leads directly to Radar (which unlocks advanced air defense and aviation). With Russia's massive military and bomber threat, upgrading our land forces to Tanks and securing advanced aviation/anti-air through Radar is our highest national security priority.
        - Technology: Combined Arms
    - #2:
      - toolName: set-relationship
      - args:
        - Private: -10
        - Rationale: The peace treaty with the Zulus has expired. The Zulus are currently distracted by their war with India and have denounced Russia. Since we both share the Autocracy ideology (+999 bonus), there is a strong strategic opportunity to form an anti-Russian Autocratic coalition. Moderating our manual hostility modifiers from -50/-45 to -10/-10 will allow the shared ideology bonus to naturally improve relations, paving the way for potential defensive agreements once the Inca war is resolved.
        - TargetID: 7
        - Public: -10
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: Russia has just captured and puppeted Cologne, which is immediately adjacent to Berlin's sea zone. This brings Russia's massive 15440 military right to our core border. Russia remains our supreme existential threat, possesses 19 Uranium, and has completed the Manhattan Project. We must maintain maximum hostility and absolute defensive vigilance.
        - Public: -95
        - TargetID: 1
        - Private: -95
    - #4:
      - toolName: set-relationship
      - args:
        - Private: -100
        - TargetID: 3
        - Public: -95
        - Rationale: Maintain maximum hostility while the war is active. We are winning the war (+32% score), and maintaining hostility ensures our AI will prosecute the war effectively and extract heavy concessions for peace.
    - #5:
      - toolName: set-relationship
      - args:
        - Private: 18
        - TargetID: 5
        - Public: 20
        - Rationale: Maintain positive modifiers. Venice is a puppet/vassal of the Inca, and once peace is achieved with the Inca, Venice will be a vital trade partner for gold and science.
    - #6:
      - toolName: set-relationship
      - args:
        - Public: 12
        - TargetID: 4
        - Rationale: Keep our top friendship with India active. India is a key buffer and counterweight in the region, despite their looming cultural victory threat.
        - Private: 12
    - #7:
      - toolName: set-relationship
      - args:
        - Private: -30
        - TargetID: 2
        - Public: -35
        - Rationale: Keep guarded hostility toward Greece as they are a major diplomatic competitor with 25 delegates and follow the Freedom ideology.
    - #8:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Antiair: 100
          - Growth: 60
          - TileImprovement: 20
          - Nuke: 100
          - Expansion: 0
          - Infrastructure: 95
          - Mobile: 80
          - Naval: 92
          - CityDefense: 100
          - Defense: 100
          - Mobilization: 85
          - Religion: 20
          - Diplomacy: 75
          - Airlift: 25
          - AirCarrier: 35
          - WaterConnection: 35
          - Happiness: 70
          - GreatPeople: 45
          - Spaceship: 100
          - Offense: 65
          - Gold: 85
          - Wonder: 5
          - UseNuke: 95
          - Ranged: 90
          - NavalTileImprovement: 0
          - Culture: 35
          - Air: 90
          - Espionage: 95
          - NavalRecon: 45
          - Recon: 70
          - Production: 100
          - MilitaryTraining: 90
          - Science: 100
          - NavalGrowth: 30
      - rationale: With Russia capturing Cologne and posing an immediate existential threat next to Berlin, we must maximize our defensive alertness. Increasing Defense, CityDefense, Antiair, and Mobilization to near maximum, while keeping Production, Science, and Spaceship at 100, ensures our empire focuses fully on survival and technological advancement. We also raise UseNuke to 95 to maximize our nuclear deterrent readiness.
  - tokens:
    - inputTokens: 52695
    - reasoningTokens: 11926
    - outputTokens: 903
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Reviewing Global Strategy**
            
            I'm currently assessing our geopolitical standing after the recent events. My focus is on identifying immediate threats and opportunities, and evaluating the shifting alliances that could impact our long-term objectives.
            
            **Analyzing Shifting Power Dynamics**
            
            The recent capture of Cologne by Russia, previously a German city under Inca occupation, is a significant development. This expansion, coupled with Russia's overwhelming military strength and technological advantage, presents an immediate and substantial threat that demands our urgent attention and strategic reassessment.
            
            **Evaluating Strategic Posture**
            
            The recent geopolitical shifts, particularly Russia's acquisition of Cologne and their advanced capabilities, require an immediate strategic reevaluation. I'm currently examining our relationships, noting active wars with the Inca, Venice, and Greece, while our friendship with India remains. I am also considering our research path, weighing options like Combined Arms or Satellites against our ongoing Computers research.
            
            **Assessing Research Options**
            
            I've been reviewing our current research focus on Computers, noting it's about 13 turns from completion. However, I'm considering the strategic implications of switching to technologies like Combined Arms for military advancements or Satellites for broader capabilities. My next policy decision is also 14 turns away, so there's time to weigh these research choices.
            
            **Deciding Next Policy**
            
            I'm re-evaluating our policy choices in light of our Spaceship grand strategy. Futurism is indeed our next adopted policy, as indicated in user strategies. I'm now comparing the remaining Autocracy Level 2 options, like Total War or Lightning Warfare, against other branches to best support our scientific pursuit and current geopolitical situation.
            
            **Reassessing Military and Research Priorities**
            
            I'm adjusting our focus to address the immediate threat from Russia, especially their capture of Cologne. Our military strength is significantly lower than theirs, so I'm prioritizing research like Combined Arms to bolster our defenses. I'm also re-evaluating policy choices, considering options that enhance our production and strategic resource availability to counter their overwhelming military might.
            
            **Securing Strategic Resources**
            
            I've identified a critical issue with our oil supply, impacting units like our Battleships and Bombers. The adoption of the "Third Alternative" policy presents a significant opportunity, as it would double our strategic resource production, including oil, and reduce unit maintenance costs. This seems like a vital step to address our current resource deficit and financial strain.
            
            **Adopting Third Alternative**
            
            I've decided to adopt the "Third Alternative" policy. This will significantly boost our strategic resource production, particularly oil, and reduce unit maintenance costs, directly addressing our current resource deficit and financial strain. This seems far more critical than Futurism given the current geopolitical climate.
            
            **Investigating Inca Relations**
            
            I'm re-examining our conflict with the Inca, noting their weakened state and Russia's territorial gains. I've realized our war with Venice is linked to our Inca conflict since Venice is an Inca vassal. I'm now considering if peace with the Inca is feasible and if it would resolve the Venetian war, while also contemplating a potential offensive against the diminished Inca.
            
            **Defending Border Territories**
            
            I'm reassessing our immediate defensive needs given Russia's proximity and overwhelming strength. Given our limited military capacity, I'm focusing on maintaining a purely defensive posture and avoiding any actions that could provoke them. Retaking Cologne is currently infeasible.
            
            **Considering Inca Peace Deal**
            
            I'm now weighing the benefits of ending our war with the Inca. Their weakness and Russia's expansion make this conflict less appealing, and peace could secure trade routes and allow full focus against Russia. I'm investigating if a peace agreement is even possible given our current negative relationship.
            
            **Leveraging World Congress**
            
            I'm re-evaluating the World Congress, specifically the "Sanction: Russia" resolution that is already enacted. This presents a strategic opportunity to coordinate actions against Russia. My current stance is to maintain maximum hostility towards them while adopting an extremely cautious and defensive posture, leaning into our guarded and afraid biases.
            
            **Analyzing World Congress Proposals**
            
            I'm reviewing the current World Congress proposals. The "Endowment for the Arts" from the Inca is detrimental to our science victory goals, so I will oppose it. I'm also considering the implications of the enacted sanctions and the current world ideology.
            
            **Refining Diplomacy with India**
            
            I'm reassessing my relationship with India, our supposed top friend, especially after realizing they also have a Declaration of Friendship with Russia. This dual alliance, coupled with India's strong progress towards a Cultural Victory, is a significant concern that requires immediate attention to prevent potential geopolitical complications and ensure our own victory path remains clear.
            
            **Revising Zulu Relations**
            
            My immediate focus is on our expired peace treaty with the Zulus. Given their significant military strength and shared Autocracy ideology, understanding our current relationship status and any lingering diplomatic ties is paramount to prevent an unintended conflict. I am actively investigating this oversight.
            
            **Assessing Zulu Alliance Potential**
            
            I've discovered our peace treaty with the Zulus has expired, and they possess considerable military strength and resources. Excellent news: they are at war with India and have denounced Russia, aligning with our own concerns. I am now investigating a potential future alliance with them, given our shared Autocracy ideology, and trying to understand why our public opinion of them is so negative.
            
            **Securing Western Border**
            
            I'm now prioritizing strengthening ties with the Zulus, given their shared Autocracy ideology and their current conflicts with both India and Russia. My goal is to establish a defensive pact to secure our western flank and create a unified front against Russia, despite past diplomatic strains.
            
            **Strengthening Zulu Ties**
            
            I'm reassessing our relationship with the Zulus, especially given our shared Autocracy ideology and their denunciation of Russia. However, a defensive pact with the Inca complicates things, as we are at war with them. My focus is now on improving our relations to potentially forge an alliance against Russia.
            
            **Clarifying Zulu-Inca Alliance Dynamics**
            
            I'm currently trying to understand how the Zulu's Defensive Pact with the Inca interacts with our ongoing war. I've reasoned that since our war with the Inca predates any potential Zulu DP, or the DP was signed after, it doesn't automatically pull them in. Making peace with the Inca should nullify this specific threat from the Zulus.
            
            **Adjusting Diplomacy and Threat Assessment**
            
            I'm re-evaluating my relationships with Greece and Venice. Greece is far away and currently occupied with India, so I'm maintaining our current negative relationship status. Venice, despite being an Inca vassal and at war with us, remains a positive trade partner, which is a peculiar but beneficial situation to preserve.
            
            **Leveraging Spy Network**
            
            I'm reviewing our spy network and discovered Agent Schimanski in Ulundi has an exceptionally high network score. This presents an immediate opportunity to potentially stage a coup or steal technology, which could significantly alter our strategic position, especially concerning the Zulus.
            
            **Utilizing Spy Assets**
            
            My spy network is a significant asset. Agent Schimanski in Ulundi has developed substantial network strength, positioning us to potentially steal advanced technology from the Zulus soon. This opportunity is critical for closing our technological gap and enhancing our strategic capabilities.
            
            **Adopting Crucial Policy**
            
            I've decided to adopt the "Third Alternative" policy. This critical shift will double our strategic resource production, particularly oil, and significantly reduce unit maintenance costs, directly addressing our severe resource deficits and financial strain. This is a far more pressing need than Futurism given our current geopolitical challenges and military requirements.
            
            **Forming Zulu Alliance**
            
            I'm leveraging our shared Autocracy ideology to improve relations with the Zulus. My current diplomatic maneuver involves reducing our hostility modifiers to allow our shared ideology to foster a stronger bond, aiming for a defensive pact to counter Russia's expansion and secure our western border, despite their defensive pact with the Inca.
            
            **Adjusting Diplomatic Strategies**
            
            I'm finalizing our diplomatic stance. I will maintain extreme hostility towards Russia due to their proximity and immense power. Venice will remain a friendly trade partner, and the Inca will face continued aggression as we press our advantage in our active war.
            
            **Updating Diplomatic and Flavor Settings**
            
            I'm solidifying our relationships, maintaining a strong friendship with India to counter regional threats, and keeping Greece at bay due to their diplomatic influence and ideology. My focus is now on refining our AI's strategic flavors to ensure continued prioritization of production, science, and nuclear capabilities, all aligned with our Spaceship grand strategy.
            
            **Prioritizing Defensive Measures**
            
            I'm significantly increasing our defensive readiness across the board, especially in city defense and anti-air capabilities, to counter Russia's immediate threat. Mobilization is also being boosted. This ensures our survival and continued focus on crucial scientific advancements for our Spaceship victory.
            
            **Securing Critical Policy**
            
            I have finalized the adoption of the "Third Alternative" policy. This strategic shift will significantly amplify our strategic resource output, particularly oil, and decrease unit maintenance expenses. This action directly addresses our dire resource shortages and financial pressures, which are far more urgent than pursuing Futurism given our current geopolitical landscape and military needs.
            
            **Forming Zulu Alliance**
            
            I am now actively pursuing an alliance with the Zulus, capitalizing on our shared Autocracy ideology and their current conflicts. My aim is to secure a defensive pact to counter Russia's growing influence, especially as they are at war with India and have denounced Russia, aligning with our own strategic interests.
            
            **Modifying Diplomatic Posture**
            
            I'm adjusting our relationships to reflect the evolving geopolitical landscape. My focus is on solidifying our alliance with the Zulus through reduced hostility, while maintaining maximum hostility towards Russia and the Inca due to their immediate threats. Venice will remain a positive trade partner.
            
            **Refining Grand Strategy Flavors**
            
            I am now fine-tuning our strategic priorities, emphasizing defense, mobilization, and offensive capabilities to counter immediate threats and advance our Spaceship victory. I'm also adjusting diplomatic stances, maintaining our strong friendship with India to leverage regional influence while keeping Greece guarded.
            
            **Adjusting Grand Strategy Flavors**
            
            I am now fine-tuning our AI's strategic priorities to emphasize defensive measures and production, alongside our ongoing focus on science for a Spaceship victory. This ensures we can effectively counter Russia's immediate threat and secure our long-term goals. I'm also adjusting diplomatic stances to maximize our advantages.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: g6dtJwplAwdygsio
          - toolName: set-policy
          - input:
            - Policy: Third Alternative
            - Rationale: We have severe resource constraints (0 Oil surplus, low Coal/Uranium), and we have active military units consuming our strategic resources. Third Alternative (Level 2 Autocracy Tenet) will double all our strategic resource production (giving us a massive boost in Oil, Aluminum, Uranium, and Coal) and reduce our unit gold maintenance costs by 25%. This is critical for our defense against Russia's 15440-strength military and for fielding modern units (Tanks, Battleships, Bombers). It is far superior to Futurism since we are pursuing a Spaceship victory, not a Cultural victory, and survival is our absolute priority.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Ye5C1NfOGs4z3y3w
          - toolName: set-research
          - input:
            - Rationale: Combined Arms unlocks the Tank (a powerful mobile land unit) and leads directly to Radar (which unlocks advanced air defense and aviation). With Russia's massive military and bomber threat, upgrading our land forces to Tanks and securing advanced aviation/anti-air through Radar is our highest national security priority.
            - Technology: Combined Arms
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: rtnHODHcNNbfzUKh
          - toolName: set-relationship
          - input:
            - Private: -10
            - Rationale: The peace treaty with the Zulus has expired. The Zulus are currently distracted by their war with India and have denounced Russia. Since we both share the Autocracy ideology (+999 bonus), there is a strong strategic opportunity to form an anti-Russian Autocratic coalition. Moderating our manual hostility modifiers from -50/-45 to -10/-10 will allow the shared ideology bonus to naturally improve relations, paving the way for potential defensive agreements once the Inca war is resolved.
            - TargetID: 7
            - Public: -10
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 3cFGSkp9KOxlqyWI
          - toolName: set-relationship
          - input:
            - Rationale: Russia has just captured and puppeted Cologne, which is immediately adjacent to Berlin's sea zone. This brings Russia's massive 15440 military right to our core border. Russia remains our supreme existential threat, possesses 19 Uranium, and has completed the Manhattan Project. We must maintain maximum hostility and absolute defensive vigilance.
            - Public: -95
            - TargetID: 1
            - Private: -95
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: XPPDE0JdnMDotU4H
          - toolName: set-relationship
          - input:
            - Private: -100
            - TargetID: 3
            - Public: -95
            - Rationale: Maintain maximum hostility while the war is active. We are winning the war (+32% score), and maintaining hostility ensures our AI will prosecute the war effectively and extract heavy concessions for peace.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: wV4UK35LBoqTnZg6
          - toolName: set-relationship
          - input:
            - Private: 18
            - TargetID: 5
            - Public: 20
            - Rationale: Maintain positive modifiers. Venice is a puppet/vassal of the Inca, and once peace is achieved with the Inca, Venice will be a vital trade partner for gold and science.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: BRtmuZ0McIfCvE6n
          - toolName: set-relationship
          - input:
            - Public: 12
            - TargetID: 4
            - Rationale: Keep our top friendship with India active. India is a key buffer and counterweight in the region, despite their looming cultural victory threat.
            - Private: 12
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: pWq8GfZMsPXsAjRO
          - toolName: set-relationship
          - input:
            - Private: -30
            - TargetID: 2
            - Public: -35
            - Rationale: Keep guarded hostility toward Greece as they are a major diplomatic competitor with 25 delegates and follow the Freedom ideology.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #9:
          - type: tool-call
          - toolCallId: DlkuNXrK9KxNJg1c
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: With Russia capturing Cologne and posing an immediate existential threat next to Berlin, we must maximize our defensive alertness. Increasing Defense, CityDefense, Antiair, and Mobilization to near maximum, while keeping Production, Science, and Spaceship at 100, ensures our empire focuses fully on survival and technological advancement. We also raise UseNuke to 95 to maximize our nuclear deterrent readiness.
            - Flavors:
              - Antiair: 100
              - Growth: 60
              - TileImprovement: 20
              - Nuke: 100
              - Expansion: 0
              - Infrastructure: 95
              - Mobile: 80
              - Naval: 92
              - CityDefense: 100
              - Defense: 100
              - Mobilization: 85
              - Religion: 20
              - Diplomacy: 75
              - Airlift: 25
              - AirCarrier: 35
              - WaterConnection: 35
              - Happiness: 70
              - GreatPeople: 45
              - Spaceship: 100
              - Offense: 65
              - Gold: 85
              - Wonder: 5
              - UseNuke: 95
              - Ranged: 90
              - NavalTileImprovement: 0
              - Culture: 35
              - Air: 90
              - Espionage: 95
              - NavalRecon: 45
              - Recon: 70
              - Production: 100
              - MilitaryTraining: 90
              - Science: 100
              - NavalGrowth: 30
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: g6dtJwplAwdygsio
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #1:
          - type: tool-result
          - toolCallId: Ye5C1NfOGs4z3y3w
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: rtnHODHcNNbfzUKh
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 3cFGSkp9KOxlqyWI
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: XPPDE0JdnMDotU4H
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: wV4UK35LBoqTnZg6
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: BRtmuZ0McIfCvE6n
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: pWq8GfZMsPXsAjRO
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #8:
          - type: tool-result
          - toolCallId: DlkuNXrK9KxNJg1c
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.