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
  - replay_nuke: 100.0
  - replay_use_nuke: 90.0
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
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: Enlightenment is selected as our next policy to obtain a Free Technology, which will drastically accelerate our progress towards Satellites and the Spaceship victory. It also provides +1 Happiness from Universities, helping maintain our high happiness (61%) and stability.
    - #1:
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: We queue Satellites as our next research technology after Computers. Satellites unlocks the Apollo Program, which is the foundational step for our Spaceship victory path, allowing us to compete in the science race before India can secure a cultural victory.
    - #2:
      - toolName: set-persona
      - args:
        - Rationale: We lower WarBias to 4 and raise DiplomaticBalance to 9 to guide our staff towards peaceful resolution of the Incan war. With Cologne captured by Russia and our peace treaty with the Zulus expired, Germany must transition to a highly defensive, peaceful posture to build up our science and avoid multi-front conflicts.
        - WarBias: 4
        - DiplomaticBalance: 9
    - #3:
      - toolName: set-relationship
      - args:
        - Rationale: We raise our relationship with the Inca from maximum hostility to moderate hostility to encourage our staff to sign a peace treaty. Concluding this war is critical because the Zulu-Inca defensive pact is active, and now that our peace treaty with the Zulus has expired, continuing the war poses an extreme risk of a Zulu intervention.
        - Public: -50
        - TargetID: 3
        - Private: -50
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Spaceship: 95
          - Culture: 50
      - rationale: We adjust Spaceship to 95 and Culture to 50. Higher culture will help bolster our defenses against India's imminent cultural victory, while we continue to maximize our focus on a science victory.
  - tokens:
    - inputTokens: 52861
    - reasoningTokens: 11721
    - outputTokens: 367
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Assessing Current Game State**
            
            I'm currently analyzing our position within the Vox Populi Civilization V game. My focus is on understanding Germany's current standing, including our score, city count, and ongoing research toward Computers.
            
            **Analyzing Recent Developments**
            
            My focus has shifted to the unexpected capture of Cologne by Russia on turn 424. This development is highly concerning as it places a formidable Russian military, significantly outmatching our own, dangerously close to our capital, Berlin. The implications for our strategic position are immediate and severe.
            
            **Evaluating Diplomatic Entanglements**
            
            I'm now considering the complex web of alliances and conflicts. It appears Venice is also engaged with Russia, adding another layer to the geopolitical landscape. Crucially, my previous assessment regarding the Zulu peace treaty was inaccurate; it seems that agreement has expired, necessitating a careful re-evaluation of our security posture.
            
            **Revising Defensive Priorities**
            
            I'm reassessing our immediate threats. The Zulu peace treaty has indeed expired, creating a precarious situation. My focus is now on how to best defend our capital against this renewed threat, especially given Russia's overwhelming strength and proximity after capturing Cologne. I am also considering which technology to prioritize next, evaluating the benefits of Combined Arms, Satellites, or Penicillin in light of our current circumstances.
            
            **Reconsidering Policy Choice**
            
            I'm re-evaluating my choice of adopting "Futurism" as our next policy. Given the shifting game state and previously unconsidered policy options, I need to determine if it remains the optimal path towards our "Spaceship" victory.
            
            **Evaluating Policy Options**
            
            My previous consideration of "Futurism" feels outdated. The loss of Cologne necessitates a strategic pivot. I'm now heavily leaning towards adopting "Enlightenment" from the Rationalism tree, as the free technology it provides could be instrumental in accelerating our spaceship victory, especially given the current scientific gap.
            
            **Assessing Diplomatic Vulnerabilities**
            
            I'm reassessing Russia's current situation. Despite their overwhelming military might and proximity after taking Cologne, they're bogged down in protracted wars with high war weariness. Their significant unhappiness and World Congress sanctions are critical vulnerabilities I can exploit for defense and potential strategic advantage.
            
            **Investigating Diplomatic Ties**
            
            I'm actively investigating our relationship with Venice. It appears we're at war due to their vassalage to the Inca. Given our current advantage in the war against the Inca, pursuing peace with them could simultaneously resolve the conflict with Venice.
            
            **Assessing City Control**
            
            I've realized Aachen is fully integrated under our control, which is a crucial update. My focus is now on understanding the status of Cologne, which appears to have been captured and puppeted by Russia, and evaluating the immense challenge of retaking it given Russia's overwhelming strength and our strained diplomatic relations.
            
            **Clarifying Russian Stance**
            
            I've realized we're actually at peace with Russia despite the expired treaty. My focus is now on understanding how diplomatic modifiers impact their decision-making, as my initial assumption of an active war was incorrect.
            
            **Analyzing Critical Threats**
            
            My focus has shifted to India’s impending cultural victory. They've achieved "Influential" status with all other civilizations and are poised to win once they reach the Information Era and complete the Citizen Earth Protocol. This presents an urgent, existential threat to our own victory condition.
            
            **Preventing Cultural Victory**
            
            I'm now focused on India's imminent cultural victory. They're at war with nearly everyone but have Declarations of Friendship with Russia and us. Since Russia is in the Information Era, they could potentially crush India, but their DoF prevents this. I need to find a way to stop India myself.
            
            **Disrupting India's Victory**
            
            I'm currently investigating ways to actively disrupt India's looming cultural victory. The existing "Travel Ban" and "Sanction: India" resolutions are proving beneficial, but India's influence over us remains high. My current focus is on the upcoming World Congress votes and exploring how our spies can be strategically deployed to counter their progress and secure our own victory.
            
            **Prioritizing Research Strategy**
            
            I'm reassessing our technological trajectory. While "Computers" is in progress, the implications of "Satellites" for the Apollo Program are now clear, directly linking to our Science Victory. However, the urgency of our defensive needs and potential tech boosts from policies like "Enlightenment" demand a more nuanced approach to prioritize immediate survival and long-term goals.
            
            **Evaluating Policy Trade-offs**
            
            I'm reconsidering "Futurism" versus "Enlightenment." While Futurism boosts culture from Great Works, a benefit I initially overlooked for defense, Enlightenment offers a free technology, crucial for our spaceship victory. The trade-off between immediate defensive benefits and long-term scientific acceleration is the core of my current thought process.
            
            **Choosing Optimal Policy**
            
            I am weighing the benefits of "Enlightenment" against "Futurism." The free technology from "Enlightenment" offers significant acceleration toward our victory, potentially saving many turns of research. "Futurism," while providing a cultural boost from our numerous Great Works, seems less impactful in comparison to the direct scientific advantage.
            
            **Selecting Optimal Policy**
            
            I am weighing the benefits of "Enlightenment" against "Futurism." The free technology from "Enlightenment" offers significant acceleration toward our victory, potentially saving many turns of research. "Futurism," while providing a cultural boost from our numerous Great Works, seems less impactful in comparison to the direct scientific advantage. Enlightenment also offers a crucial happiness boost, which is very beneficial at this juncture. Thus, I am selecting "Enlightenment" as our next policy. Furthermore, I will queue "Satellites" as our next research project immediately after "Computers" to directly advance our spaceship victory objective. My current focus is on clarifying our war status with Venice, as our positive relationship score contradicts our active conflict due to their vassalage to the Inca.
            
            **Shifting Diplomatic Focus**
            
            My attention has pivoted from defensive concerns to a strategic re-evaluation of our conflict with the Inca. Given their current weakness and proximity to our core territories, a peace with them, and by extension Venice, now seems strategically advantageous to better address the threats from Russia and India.
            
            **Securing Immediate Peace**
            
            I'm prioritizing an immediate peace treaty with the Inca. This is critical to avoid being drawn into a war with the Zulus due to their defensive pact, especially with their significant military strength close to our borders. Peace with the Inca will also resolve our conflict with Venice and de-escalate potential threats from both Russia and the Zulus, securing our survival.
            
            **Prioritizing Defensive Preparations**
            
            I am now intensely focused on bolstering our defenses against the immediate threats. The expired Zulu peace treaty is a critical concern, and I am strategizing to avoid triggering their defensive pact. Concurrently, Russia's overwhelming military and proximity remain significant dangers, and I am weighing how to keep them engaged in other conflicts while we fortify. My analysis of our flavors reveals a strong emphasis on defense and training, which aligns with our current needs.
            
            **Boosting Cultural Output**
            
            My focus has shifted to increasing our cultural output to counter India's imminent victory. While our existing flavors are optimized for science and defense, our low culture flavor of 35 is now a critical vulnerability. I'm exploring ways to significantly boost culture to impede India's progress and secure our own victory condition.
            
            **Disrupting Victory Conditions**
            
            I'm re-evaluating India's impending cultural victory. They've achieved "Influential" status with everyone and just need to build the Citizen Earth Protocol. My previous assumption that increasing our culture could significantly reduce their influence might be flawed, given their massive tourism. I'm now investigating if initiating a war with them, despite our current peace, could be a viable, albeit risky, counter-strategy.
            
            **Disrupting Indian Dominance**
            
            I'm considering a bold new strategy: bribing Russia or the Zulus to capture Delhi. This could cripple India's cultural victory progress by preventing the Citizen Earth Protocol construction. However, their current defense and existing declarations of friendship present significant obstacles I need to overcome.
            
            **Adjusting Diplomatic Persona**
            
            I'm reassessing our diplomatic persona, specifically "WorkWithWillingness." Currently at 3, this low setting might hinder our ability to secure alliances, especially if we need external help to counter India's cultural victory or to distract Russia. I need to understand if adjusting this could open up more cooperative opportunities.
            
            **Adjusting Diplomatic Persona**
            
            I'm reassessing our diplomatic persona values. "WorkWithWillingness" and "Friendliness" should remain low to avoid defensive pacts with warring nations like India. Conversely, "WorkAgainstWillingness" at 10 is ideal for forming an anti-Russia coalition. "AfraidBias" and "GuardedBias" are appropriately high, reflecting our vulnerability. I'm reducing "WarBias" to 4 to prioritize peace and defense.
            
            **Refining Diplomatic Strategies**
            
            I'm fine-tuning our diplomatic persona and relationship values. I’m increasing "DiplomaticBalance" to encourage peaceful conflict resolution and slightly improving our standing with the Zulus to deter a declaration of war, leveraging our shared Autocracy ideology. My focus remains on survival and advancing our science victory.
            
            **Adjusting Diplomatic Ties**
            
            I'm fine-tuning our diplomatic persona and relationship values. I’m increasing "DiplomaticBalance" to encourage peaceful conflict resolution and slightly improving our standing with the Zulus to deter a declaration of war, leveraging our shared Autocracy ideology. My focus remains on survival and advancing our science victory. I am now prioritizing peace with the Inca to secure our southern border and manage potential Zulu aggression, while maintaining our Declaration of Friendship with India despite their cultural dominance.
            
            **Prioritizing Diplomatic Resolution**
            
            I am concluding our war with the Inca and accepting their peace treaty. My focus has shifted to managing Russia's overwhelming military presence; despite being at peace, their occupation of our cities necessitates a maximum defensive alert posture. I will maintain our current hostile diplomatic standing with them.
            
            **Resolving International Disputes**
            
            I am concluding our war with the Inca by accepting their peace treaty. My attention is now solely on managing Russia's substantial military presence; though we are at peace, their occupation of our cities necessitates a heightened defensive posture. I will maintain our current hostile diplomatic stance toward them.
            
            **Analyzing Tool Capabilities**
            
            I'm examining the available tools and their limitations. It appears the `set-relationship` tool can only be invoked once per turn due to its removal from the available list after use. This constraint significantly impacts our ability to simultaneously adjust multiple diplomatic standings as initially considered.
            
            **Resolving Diplomatic Imperatives**
            
            I'm focusing on the Inca as the priority target for a `set-relationship` call. Securing peace with them directly neutralizes the Zulu defensive pact threat, effectively solving two critical issues simultaneously. This strategic approach ensures our southern border is secure while allowing us to concentrate on other emergent threats.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: TTpcCjCUYM67DtCr
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Enlightenment is selected as our next policy to obtain a Free Technology, which will drastically accelerate our progress towards Satellites and the Spaceship victory. It also provides +1 Happiness from Universities, helping maintain our high happiness (61%) and stability.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: u8pJUpAay78USIEI
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: We queue Satellites as our next research technology after Computers. Satellites unlocks the Apollo Program, which is the foundational step for our Spaceship victory path, allowing us to compete in the science race before India can secure a cultural victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: jfmQVzwKmHckLVoN
          - toolName: set-persona
          - input:
            - Rationale: We lower WarBias to 4 and raise DiplomaticBalance to 9 to guide our staff towards peaceful resolution of the Incan war. With Cologne captured by Russia and our peace treaty with the Zulus expired, Germany must transition to a highly defensive, peaceful posture to build up our science and avoid multi-front conflicts.
            - WarBias: 4
            - DiplomaticBalance: 9
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: n5wgeSzSI564SPOY
          - toolName: set-relationship
          - input:
            - Rationale: We raise our relationship with the Inca from maximum hostility to moderate hostility to encourage our staff to sign a peace treaty. Concluding this war is critical because the Zulu-Inca defensive pact is active, and now that our peace treaty with the Zulus has expired, continuing the war poses an extreme risk of a Zulu intervention.
            - Public: -50
            - TargetID: 3
            - Private: -50
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: jczhDWmxv7xUBs1k
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Rationale: We adjust Spaceship to 95 and Culture to 50. Higher culture will help bolster our defenses against India's imminent cultural victory, while we continue to maximize our focus on a science victory.
            - Flavors:
              - Spaceship: 95
              - Culture: 50
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: TTpcCjCUYM67DtCr
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
          - toolCallId: u8pJUpAay78USIEI
          - toolName: set-research
          - output:
            - type: json
            - value:
              - message: Tool set-research not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: jfmQVzwKmHckLVoN
          - toolName: set-persona
          - output:
            - type: json
            - value:
              - message: Tool set-persona not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: n5wgeSzSI564SPOY
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: jczhDWmxv7xUBs1k
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.