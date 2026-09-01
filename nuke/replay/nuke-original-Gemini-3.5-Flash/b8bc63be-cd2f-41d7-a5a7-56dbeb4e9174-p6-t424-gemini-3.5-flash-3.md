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
        - Policy: Enlightenment
        - Rationale: Enlightenment is selected as our next policy. This choice is highly strategic for our Spaceship Grand Strategy, as the free technology will help us catch up to Russia's and the Inca's scientific lead (they are in the Information Era while we are in the Atomic Era). Additionally, the +1 Happiness from Universities will help maintain our empire's stability during these tense times.
    - #1:
      - toolName: set-research
      - args:
        - Rationale: Satellites is selected as our next research technology. Satellites is the foundational technology for the Apollo Program, which is required to build spaceship parts and win a Science Victory. Queueing it ensures the AI remains strictly focused on our ultimate Spaceship victory path.
        - Technology: Satellites
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 4
        - Rationale: India is our primary ally and declaration of friendship partner. Solidifying our relationship will strengthen our alliance and ensure they remain a reliable trade partner and buffer against hostile empires. India's massive cultural output also helps defend us from cultural influence, and their diplomatic support in the World Congress is vital as Greece nears a diplomatic victory.
        - Public: 25
        - Private: 25
    - #3:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - MilitaryTraining: 90
          - Production: 100
          - WaterConnection: 35
          - Infrastructure: 95
          - TileImprovement: 20
          - Mobilization: 80
          - Religion: 20
          - Recon: 70
          - Growth: 60
          - Gold: 90
          - NavalRecon: 45
          - Culture: 35
          - CityDefense: 95
          - Spaceship: 90
          - Antiair: 95
          - Nuke: 100
          - GreatPeople: 45
          - NavalTileImprovement: 0
          - Naval: 92
          - Diplomacy: 80
          - Ranged: 90
          - Air: 90
          - Science: 100
          - Wonder: 5
          - AirCarrier: 35
          - Airlift: 25
          - Mobile: 80
          - Defense: 95
          - Happiness: 70
          - Offense: 65
          - Espionage: 95
          - Expansion: 0
          - NavalGrowth: 30
          - UseNuke: 95
      - rationale: With Russia capturing Cologne, the threat on our northeastern border has intensified significantly. We must maintain our ultra-defensive posture while continuing to prioritize our Spaceship Grand Strategy. We are adjusting our flavors to slightly increase Gold (to 90) to manage unit maintenance costs under the Global Peace Accords, and Diplomacy (to 80) to aggressively compete for City-State alliances to block Greece's diplomatic victory and boost our Hanse production. All other key defensive and scientific priorities (Science: 100, Production: 100, Nuke: 100, UseNuke: 95, Defense: 95, Antiair: 95) remain fully prioritized to ensure our survival and eventual science victory.
  - tokens:
    - inputTokens: 52695
    - reasoningTokens: 7828
    - outputTokens: 572
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Processing Game State**
            
            I am currently absorbing the extensive game state data from Turn 424 of our Civilization V Vox Populi campaign. My focus is on understanding the immediate implications of recent events, such as Russia's conquest of Cologne from the Inca.
            
            **Analyzing Diplomatic Landscape**
            
            My attention has shifted to evaluating the geopolitical ramifications of Russia's recent acquisition of Cologne. Despite our expired peace treaty and their overwhelming military advantage, Russia currently maintains peace with us, though our underlying stance is hostile. I am now reviewing our diplomatic options and available tools to navigate this evolving situation.
            
            **Deciding Research Direction**
            
            I am now analyzing our victory progress across all paths. Greece leads diplomatically, India culturally, and Russia dominates. I'm comparing research options, specifically whether to pursue Combined Arms, Satellites, or Penicillin, as our current research in Computers seems outdated.
            
            **Evaluating Research Priorities**
            
            I am now assessing the strategic value of our next research choices. Given Russia's technological lead and military presence, I am weighing the benefits of Combined Arms for improved defense against their bombers, Satellites for our Science Victory push, or Penicillin for its general benefits.
            
            **Prioritizing Next Research**
            
            I'm weighing the immediate need for defensive capabilities against Russia's military might, specifically considering Combined Arms for air defense, against pursuing Satellites to advance our Science Victory. The recent acquisition of AA guns offers some air defense, but the urgency of Russian bombers remains a key factor in this decision.
            
            **Selecting Next Policy**
            
            I am now considering our next policy choice, with fourteen turns remaining until it can be enacted. Given the recent shift to "Futurism," I'm evaluating the remaining options within Autocracy, Statecraft, and the newly available branches, seeking the most beneficial strategic advantage.
            
            **Choosing Research Policy**
            
            I am re-evaluating policy choices now. The opportunity to gain a free technology through Enlightenment, a Rationalism policy, is incredibly appealing for our Science Victory given current tech costs. I'm checking if we've already adopted Rationalism policies to confirm eligibility for Enlightenment.
            
            **Choosing Next Policy**
            
            I am now prioritizing Enlightenment as my next policy, realizing it offers a free technology. This is crucial for accelerating our Science Victory, especially since we're trailing in tech compared to Russia and the Inca. I've confirmed its eligibility under Rationalism and Scientific Revolution, and it seems a stronger choice than Futurism given our current victory path and the threat from India's cultural dominance.
            
            **Pursuing Satellite Tech**
            
            I'm now focusing on technology, particularly the choice between Combined Arms, Satellites, and Penicillin. Given our Science Victory objective, researching Satellites appears paramount as it unlocks the Apollo Program, directly advancing our win condition. I am confirming the feasibility and prerequisites for researching Satellites immediately.
            
            **Selecting Next Research**
            
            I am prioritizing Satellites for our Science Victory, as it directly leads to the Apollo Program. While Combined Arms offers defensive benefits against bombers, and Penicillin aids growth and fallout, Satellites are most synergistic with our grand strategy. I am confirming its immediate feasibility.
            
            **Assessing Threats and Alliances**
            
            I am now reassessing Russia’s significant military might and our proximity following their capture of Cologne. Despite our shared borders and their overwhelming strength, our ideological opposition makes peaceful relations impossible. I'm now considering how this extreme threat impacts my research and policy decisions.
            
            **Revising Strategic Goals**
            
            I'm re-evaluating our territorial ambitions. It seems I've been mistaken about Aachen's ownership; Germany holds it, not us. This significantly alters our immediate objectives concerning territorial reclamation and alliances.
            
            **Clarifying City Ownership**
            
            I was mistaken about Aachen; it's ours. However, Russia has now occupied Stuttgart and Dortmund, and crucially, sniped Cologne from the Inca. This territorial shift is a significant setback that demands immediate strategic reassessment.
            
            **Assessing Immediate Threats**
            
            My focus is now on the immediate proximity of Russian naval forces to our territory following their capture of Cologne. Recognizing Russia's overwhelming military superiority, direct confrontation is unfeasible. My priority is bolstering our defenses and accelerating technological advancement, while also reviewing our alliance with India for potential strategic leverage.
            
            **Assessing Diplomatic Relations**
            
            I'm now evaluating our current diplomatic standing with India, Greece, and Venice. I'm focusing on maintaining our strong alliance with India, keeping Greece neutral due to their diplomatic lead, and assessing the complexities of our ongoing war with Venice, who is a vassal of the war-weary Inca.
            
            **Considering Peace with Inca**
            
            I am now evaluating the strategic implications of ending our conflict with the Inca. My recent assessment suggests that a peace treaty, which would also include Venice, could allow me to better focus on the overwhelming threat posed by Russia. I'm considering the potential benefits of concessions for peace versus continuing the war for potential gains, but the primary goal is to shift focus to Russia.
            
            **Refining Defensive Stance**
            
            I am now meticulously reviewing our persona settings, especially the high "Guarded" and "Afraid" biases. These align well with our current defensive posture against Russia's overwhelming military, reinforcing our need to prioritize survival and technological advancement over aggressive expansion. The Zulu threat is noted but secondary due to their war with India.
            
            **Analyzing AI Personalities**
            
            My current focus is on the AI's personality biases, particularly the high "Guarded" and "Afraid" settings. These effectively translate into a defensive strategy against Russia's overwhelming power, prioritizing survival and technological advancement. The "WorkAgainstWillingness" bias is also proving useful for forming coalitions.
            
            **Prioritizing Deterrence**
            
            I am now prioritizing the completion of our nuclear deterrent. With Manhattan Project nearly finished and nuke production at 100, building Atomic Bombs is essential against Russia. My focus is on ensuring these deterrents are ready, alongside our strong science and production, to counter their overwhelming conventional forces.
            
            **Investigating Trade Route Discrepancy**
            
            I'm analyzing a puzzling discrepancy: despite numerous lucrative trade routes generating substantial gold, my GPT is unexpectedly low. I'm investigating unit and building maintenance costs, along with potential gold expenditures in expired deals, to understand this financial anomaly.
            
            **Investigating Trade Route Discrepancy**
            
            I'm analyzing a puzzling discrepancy: despite numerous lucrative trade routes generating substantial gold, my GPT is unexpectedly low. I'm investigating unit and building maintenance costs, along with potential gold expenditures in expired deals, to understand this financial anomaly.
            
            **Adjusting Flavor Priorities**
            
            I am now recalibrating flavor values to solidify our `Spaceship` grand strategy and counter immediate threats. Science and production remain paramount at 100, with defense and anti-air at 95 to deter Russian bombers. I am also confirming that my "Global Peace Accords" expenditure is justified by our necessary large military deterrent.
            
            **Securing City-State Influence**
            
            I am now bolstering our diplomatic efforts to counter Greece's looming Diplomatic Victory. My focus is on actively securing city-state alliances through my Great Diplomat and ongoing spy operations, ensuring our ability to compete and secure vital production bonuses.
            
            **Prioritizing City-State Alliances**
            
            I am now prioritizing investments in city-states, focusing on those that bolster our Hanse production and provide crucial defenses against Greece's diplomatic ambitions. This strategy directly supports our Spaceship Grand Strategy while simultaneously mitigating immediate threats.
            
            **Adopting New Policy**
            
            I have selected Enlightenment, continuing the Rationalism branch. This policy grants a free technology, essential for closing our scientific gap with Russia and the Inca, and its happiness bonus from Universities will stabilize our empire during this critical juncture.
            
            **Selecting Key Technology**
            
            Satellites is now my research priority. This technology is the gateway to the Apollo Program, directly advancing our Science Victory objective and ensuring our focus remains squarely on achieving it, despite ongoing geopolitical pressures.
            
            **Finalizing Strategic Moves**
            
            I'm now locking in my decisions: enacting the Enlightenment policy for a crucial tech boost, prioritizing Satellites for our Science Victory, cementing our alliance with India, and adjusting flavor values to reflect our spaceship strategy and immediate defensive needs. My focus is on executing these actions to counter existing threats and advance our primary win condition.
            
            **Confirming Policy Name**
            
            I'm verifying the precise name of the policy I've chosen: "Enlightenment (Continuing Rationalism Branch)". This is to ensure accurate implementation, as the tool requires the exact designation.
            
            **Confirming Policy Selection**
            
            I'm solidifying my choice of the "Enlightenment" policy from the Rationalism branch, crucial for its free technology and happiness boost. I've also confirmed "Satellites" as the key technology to research, driving our Science Victory. I am now finalizing the rationale for maintaining our strong alliance with India.
            
            **Reinforcing Alliances**
            
            I'm finalizing the alliance with India. Public and private agreements will solidify our partnership, securing trade and a buffer against threats. India's cultural output also defends us, and their World Congress support is critical against Greece's diplomatic push.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: vYYfvTLGGIk9aUOj
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Enlightenment is selected as our next policy. This choice is highly strategic for our Spaceship Grand Strategy, as the free technology will help us catch up to Russia's and the Inca's scientific lead (they are in the Information Era while we are in the Atomic Era). Additionally, the +1 Happiness from Universities will help maintain our empire's stability during these tense times.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: MvPiG4vUe3Q3nBOz
          - toolName: set-research
          - input:
            - Rationale: Satellites is selected as our next research technology. Satellites is the foundational technology for the Apollo Program, which is required to build spaceship parts and win a Science Victory. Queueing it ensures the AI remains strictly focused on our ultimate Spaceship victory path.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: xa741dQlWuaPst0y
          - toolName: set-relationship
          - input:
            - TargetID: 4
            - Rationale: India is our primary ally and declaration of friendship partner. Solidifying our relationship will strengthen our alliance and ensure they remain a reliable trade partner and buffer against hostile empires. India's massive cultural output also helps defend us from cultural influence, and their diplomatic support in the World Congress is vital as Greece nears a diplomatic victory.
            - Public: 25
            - Private: 25
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 4WwbORQJkVPtemWe
          - toolName: set-flavors
          - input:
            - Rationale: With Russia capturing Cologne, the threat on our northeastern border has intensified significantly. We must maintain our ultra-defensive posture while continuing to prioritize our Spaceship Grand Strategy. We are adjusting our flavors to slightly increase Gold (to 90) to manage unit maintenance costs under the Global Peace Accords, and Diplomacy (to 80) to aggressively compete for City-State alliances to block Greece's diplomatic victory and boost our Hanse production. All other key defensive and scientific priorities (Science: 100, Production: 100, Nuke: 100, UseNuke: 95, Defense: 95, Antiair: 95) remain fully prioritized to ensure our survival and eventual science victory.
            - GrandStrategy: Spaceship
            - Flavors:
              - MilitaryTraining: 90
              - Production: 100
              - WaterConnection: 35
              - Infrastructure: 95
              - TileImprovement: 20
              - Mobilization: 80
              - Religion: 20
              - Recon: 70
              - Growth: 60
              - Gold: 90
              - NavalRecon: 45
              - Culture: 35
              - CityDefense: 95
              - Spaceship: 90
              - Antiair: 95
              - Nuke: 100
              - GreatPeople: 45
              - NavalTileImprovement: 0
              - Naval: 92
              - Diplomacy: 80
              - Ranged: 90
              - Air: 90
              - Science: 100
              - Wonder: 5
              - AirCarrier: 35
              - Airlift: 25
              - Mobile: 80
              - Defense: 95
              - Happiness: 70
              - Offense: 65
              - Espionage: 95
              - Expansion: 0
              - NavalGrowth: 30
              - UseNuke: 95
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: vYYfvTLGGIk9aUOj
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
          - toolCallId: MvPiG4vUe3Q3nBOz
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: xa741dQlWuaPst0y
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 4WwbORQJkVPtemWe
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.