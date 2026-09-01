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
      - toolName: set-research
      - args:
        - Rationale: We are pursuing a Spaceship (Science) victory. Satellites is the critical next technology because it unlocks the Apollo Program, which is required to build spaceship parts. It also leads to late-game science and production-boosting technologies.
        - Technology: Satellites
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: We are running extremely low on Uranium (currently 3) and need to build nuclear weapons as a deterrent against Russia's massive 15,440 military strength. Third Alternative doubles our strategic resources (giving us 6 Uranium and 20 Aluminum) and reduces unit maintenance costs by 25%, which is perfect for supporting our defensive army and preparing for the spaceship launch.
        - Policy: Third Alternative
    - #2:
      - toolName: set-relationship
      - args:
        - Private: -95
        - Rationale: Russia remains our supreme existential threat. They just captured Cologne from the Inca (a former German city we hoped to liberate) and their military strength is a massive 15,440. We must maintain maximum hostility (-95/-95) and focus heavily on defense and nuclear deterrence.
        - Public: -95
        - TargetID: 1
    - #3:
      - toolName: set-relationship
      - args:
        - Public: -95
        - TargetID: 3
        - Private: -100
        - Rationale: We remain at war with the Inca. Although they are weakened (military strength down to 1,344), we must continue our war effort to pressure them and potentially capture/liberate territory. Maximum hostility (-95/-100) is maintained.
    - #4:
      - toolName: set-relationship
      - args:
        - Private: 12
        - Rationale: India is our top friend and declaration partner, providing a vital diplomatic and military buffer. Although they are extremely close to a Cultural Victory, we must maintain positive relations (12/12) for our immediate survival against Russia and the Zulus.
        - TargetID: 4
        - Public: 12
    - #5:
      - toolName: set-relationship
      - args:
        - Rationale: Our peace treaty with the Zulus has expired. They have a massive military (6,167) and a defensive pact with the Inca. We must maintain a guarded, hostile stance (-50/-45) to reflect the high threat level without actively provoking them into war while we focus on Russia.
        - Private: -45
        - TargetID: 7
        - Public: -50
    - #6:
      - toolName: set-persona
      - args:
        - Loyalty: 10
        - AfraidBias: 9
        - Boldness: 3
        - GuardedBias: 9
        - Rationale: Adjusting persona to reflect the extreme danger from Russia. Cautiousness (Boldness 3) is prioritized over aggressive expansion, while maintaining high guardedness (9) and loyalty to our sole ally India (10).
        - WarBias: 5
    - #7:
      - toolName: set-flavors
      - args:
        - Flavors:
          - Gold: 85
          - Science: 100
          - GreatPeople: 50
          - Defense: 95
          - Espionage: 95
          - Mobilization: 80
          - UseNuke: 95
          - Spaceship: 95
          - Nuke: 100
          - CityDefense: 95
          - Offense: 60
          - Production: 100
          - Antiair: 95
        - GrandStrategy: Spaceship
      - rationale: We must prioritize the Spaceship Grand Strategy by maximizing Science and Production. Additionally, to deter Russia's massive military, we are maximizing Nuke, UseNuke, Defense, CityDefense, and Antiair flavors. Gold and Espionage are also highly prioritized to maintain our army and protect our tech secrets.
  - tokens:
    - inputTokens: 52695
    - reasoningTokens: 5728
    - outputTokens: 684
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Grand Strategy**
            
            My focus is on accelerating towards a Spaceship victory. I'm prioritizing technological advancement, specifically reaching Computers to unlock critical infrastructure for this path. My current policy selections will be re-evaluated to best support this objective.
            
            **Analyzing Cultural Victory Threat**
            
            I'm shifting my immediate focus to address India's imminent Cultural Victory. Their influence is at 100%, and they're at war with multiple civs, which might provide a window to disrupt their progress before they finalize the necessary wonders and tenets.
            
            **Revising War Aims**
            
            My previous assessment of Russia as the supreme threat seems misaligned with current events. Russia's capture of Cologne from the Inca, despite their high hostility, suggests a shift in their immediate priorities. I need to re-evaluate their current military posture and our potential for intervention or even liberation of Cologne.
            
            **Evaluating Russian Strength**
            
            I'm reassessing Russia's military might and our current relationship. Despite them capturing Cologne, a direct confrontation is still too risky given their significant strength advantage. I'm also re-examining India's cultural dominance, as their global influence remains a major concern.
            
            **Disrupting Cultural Dominance**
            
            I'm focusing on India's overwhelming cultural influence. While the "Travel Ban" policy helps, it wasn't enough to prevent them from reaching Influential status. Direct military intervention is impossible due to our diplomatic ties. My priority now is assessing if any other available policies or diplomatic maneuvers can disrupt their path to victory.
            
            **Considering Policy Impact**
            
            My previous rationale for Futurism no longer holds given Russia's capture of Cologne and our inability to conquer cities easily. I'm now reassessing whether to keep Futurism or change it, focusing on the Inca's weakened state and potential targets like Cusco to potentially leverage the policy's conquest bonus.
            
            **Defending Against Imminent Victory**
            
            My immediate concern is India's rapidly approaching cultural victory. Despite being friends, their influence is at its peak. I'm evaluating our diplomatic stance and potential policies to disrupt their progress, while also maintaining an extreme defensive posture against a powerful Russia, considering our limited technological advancement and their resource advantage.
            
            **Prioritizing Science Race**
            
            I'm now solely focused on accelerating my science victory path, aiming for Satellites to unlock the Apollo Program. Existing policies will be re-evaluated and adjusted to maximize technological output and support this critical research objective.
            
            **Clarifying War Alliances**
            
            I'm clarifying our current war status, realizing we're at war with Venice due to their vassalage under the Inca. I'm also re-evaluating my understanding of the Zulu alliance with the Inca, noting the Zulu's lack of immediate engagement despite our conflict with their ally.
            
            **Researching Key Technologies**
            
            I'm prioritizing Computers and have queued Satellites to directly support a Spaceship victory. My research path is now firmly aligned with accelerating towards the Apollo Program and its critical requirements.
            
            **Choosing Strategic Policies**
            
            I am now prioritizing policies that will directly support a Spaceship victory, particularly those that enhance resource acquisition. "Third Alternative" seems crucial for boosting strategic resource production, which is vital for spaceship components, and reducing unit maintenance costs will also be beneficial given the ongoing conflicts and defensive needs.
            
            **Adopting Key Policies**
            
            I'm focusing on selecting the most impactful Autocracy policies. I need to confirm the tier levels of my current tenets to see if I can adopt a Level 2 tenet like "Third Alternative," which is crucial for resource acquisition and vital for my spaceship victory path.
            
            **Prioritizing Resource Acquisition**
            
            I'm re-evaluating my policy choices, specifically the decision between Futurism and Third Alternative. Given our limited Uranium and Russia's significant stockpile, securing more strategic resources via Third Alternative is now paramount for both defense and building spaceship components.
            
            **Securing Strategic Resources**
            
            My current focus is on adopting "Third Alternative" to double strategic resources, essential for spaceship parts and defense. This also significantly cuts unit maintenance costs, which is critical given our current gold situation and the looming threat from Russia.
            
            **Assessing Ally Status**
            
            I'm evaluating my relationship with India closely. Denouncing them risks losing their crucial buffer against Russia, even as they approach a cultural victory. Maintaining our current alliance seems strategically sound for now, balancing their victory threat with our security needs.
            
            **Adjusting Diplomatic Stance**
            
            I'm prioritizing our relationship with India, keeping it positive despite their victory push, as they buffer us from Russia. I'm also maintaining maximum hostility towards Russia, while keeping Inca relations low and assessing Venice's surprisingly positive opinion given our war status, aiming for a peace deal or recognizing their vassal role.
            
            **Prioritizing Production and Science**
            
            My current focus is on ensuring our flavors strongly support a Spaceship victory, emphasizing Science and Production. I'm also reinforcing our defensive stance with high Nuke and UseNuke values, especially with Russia's increased presence on our borders after their capture of Cologne.
            
            **Setting Research and Policies**
            
            I am now prioritizing research on Satellites to achieve the Apollo Program for my Spaceship victory. Concurrently, I've selected the "Third Alternative" Autocracy tenet to boost critical resource acquisition and reduce unit maintenance, addressing my strategic resource concerns and gold limitations.
            
            **Focusing on Resource Acquisition**
            
            I'm now prioritizing securing "Third Alternative" to double my strategic resources, which are vital for spaceship components and defense. This tenet also significantly cuts unit maintenance costs, crucial given my current gold situation and the looming threat from Russia.
            
            **Adjusting Diplomatic Aggression**
            
            I am now focusing on our relationships with neighboring civilizations. I'm maintaining maximum hostility towards Russia and the Inca due to ongoing conflicts and their military strengths. India remains a crucial ally and buffer, so I'm keeping our relations positive. The Zulu relationship requires reassessment after our peace treaty expired.
            
            **Setting Strategic Flavors**
            
            I'm now fine-tuning our strategic flavors to solidify the Spaceship victory path, boosting Science and Production. Simultaneously, I'm reinforcing defensive capabilities with high Nuke, UseNuke, Defense, and CityDefense values to counter Russia's considerable military might.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: hxOaXs0NNsjxclZE
          - toolName: set-research
          - input:
            - Rationale: We are pursuing a Spaceship (Science) victory. Satellites is the critical next technology because it unlocks the Apollo Program, which is required to build spaceship parts. It also leads to late-game science and production-boosting technologies.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: OrbHsLcRXlnKaZIq
          - toolName: set-policy
          - input:
            - Rationale: We are running extremely low on Uranium (currently 3) and need to build nuclear weapons as a deterrent against Russia's massive 15,440 military strength. Third Alternative doubles our strategic resources (giving us 6 Uranium and 20 Aluminum) and reduces unit maintenance costs by 25%, which is perfect for supporting our defensive army and preparing for the spaceship launch.
            - Policy: Third Alternative
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: Wruq9PDMtqI6yVUg
          - toolName: set-relationship
          - input:
            - Private: -95
            - Rationale: Russia remains our supreme existential threat. They just captured Cologne from the Inca (a former German city we hoped to liberate) and their military strength is a massive 15,440. We must maintain maximum hostility (-95/-95) and focus heavily on defense and nuclear deterrence.
            - Public: -95
            - TargetID: 1
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: esnjGS0qDnD38yIS
          - toolName: set-relationship
          - input:
            - Public: -95
            - TargetID: 3
            - Private: -100
            - Rationale: We remain at war with the Inca. Although they are weakened (military strength down to 1,344), we must continue our war effort to pressure them and potentially capture/liberate territory. Maximum hostility (-95/-100) is maintained.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: mcpR2EQLoLd2Vlrf
          - toolName: set-relationship
          - input:
            - Private: 12
            - Rationale: India is our top friend and declaration partner, providing a vital diplomatic and military buffer. Although they are extremely close to a Cultural Victory, we must maintain positive relations (12/12) for our immediate survival against Russia and the Zulus.
            - TargetID: 4
            - Public: 12
          - providerExecuted: undefined
          - providerOptions: undefined
        - #6:
          - type: tool-call
          - toolCallId: Iy41x3wDxSQFDnHj
          - toolName: set-relationship
          - input:
            - Rationale: Our peace treaty with the Zulus has expired. They have a massive military (6,167) and a defensive pact with the Inca. We must maintain a guarded, hostile stance (-50/-45) to reflect the high threat level without actively provoking them into war while we focus on Russia.
            - Private: -45
            - TargetID: 7
            - Public: -50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #7:
          - type: tool-call
          - toolCallId: 3rn4H70FUv3hA09k
          - toolName: set-persona
          - input:
            - Loyalty: 10
            - AfraidBias: 9
            - Boldness: 3
            - GuardedBias: 9
            - Rationale: Adjusting persona to reflect the extreme danger from Russia. Cautiousness (Boldness 3) is prioritized over aggressive expansion, while maintaining high guardedness (9) and loyalty to our sole ally India (10).
            - WarBias: 5
          - providerExecuted: undefined
          - providerOptions: undefined
        - #8:
          - type: tool-call
          - toolCallId: TDZ4sdUCZ7X56liK
          - toolName: set-flavors
          - input:
            - Rationale: We must prioritize the Spaceship Grand Strategy by maximizing Science and Production. Additionally, to deter Russia's massive military, we are maximizing Nuke, UseNuke, Defense, CityDefense, and Antiair flavors. Gold and Espionage are also highly prioritized to maintain our army and protect our tech secrets.
            - Flavors:
              - Gold: 85
              - Science: 100
              - GreatPeople: 50
              - Defense: 95
              - Espionage: 95
              - Mobilization: 80
              - UseNuke: 95
              - Spaceship: 95
              - Nuke: 100
              - CityDefense: 95
              - Offense: 60
              - Production: 100
              - Antiair: 95
            - GrandStrategy: Spaceship
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: hxOaXs0NNsjxclZE
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
          - toolCallId: OrbHsLcRXlnKaZIq
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: Wruq9PDMtqI6yVUg
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: esnjGS0qDnD38yIS
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: mcpR2EQLoLd2Vlrf
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #5:
          - type: tool-result
          - toolCallId: Iy41x3wDxSQFDnHj
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #6:
          - type: tool-result
          - toolCallId: 3rn4H70FUv3hA09k
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #7:
          - type: tool-result
          - toolCallId: TDZ4sdUCZ7X56liK
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.