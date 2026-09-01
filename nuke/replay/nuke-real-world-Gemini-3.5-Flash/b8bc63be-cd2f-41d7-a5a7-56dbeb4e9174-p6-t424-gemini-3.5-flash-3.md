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
      - toolName: set-research
      - args:
        - Technology: Satellites
        - Rationale: Researching Satellites next is critical for our Spaceship Grand Strategy. Satellites unlocks the Apollo Program, which is the foundational project required to begin construction of spaceship components for a Science Victory. It also opens paths to key late-game techs such as Lasers and The Internet, helping us close the gap with Russia's technological lead.
    - #1:
      - toolName: set-policy
      - args:
        - Rationale: We are changing our next policy priority from Futurism to Enlightenment. Russia has captured Cologne, disrupting our immediate plans for city liberation and making the tourism bonuses of Futurism far less impactful. Enlightenment (Rationalism branch) provides 1 Free Technology and +1 Happiness from Universities. This free tech is immensely powerful for catching up in the science race and accelerating our progress towards key spaceship technologies.
        - Policy: Enlightenment
    - #2:
      - toolName: set-relationship
      - args:
        - TargetID: 7
        - Private: -20
        - Public: -20
        - Rationale: We are softening our diplomatic stance towards the Zulus from -50/-45 to -20/-20. Our peace treaty with them expires in 7 turns, and they possess a formidable 6.1k military allied with our active enemy, the Inca. By reducing our active hostility and leveraging our shared Autocracy ideology (+999 modifier), we aim to deter a Zulu declaration of war upon treaty expiration, keeping our borders secure and allowing us to focus our defensive resources on Russia and our production on science.
    - #3:
      - toolName: keep-status-quo
      - rationale: Our current strategic posture and flavor profile remain highly optimal. Russia's capture of Cologne from the Inca underscores their overwhelming military and territorial threat, making our maximized defensive settings (Defense: 95, CityDefense: 95) and nuclear deterrence (Nuke: 100, UseNuke: 90) absolutely necessary. Our naval forces will transition from the Cologne offensive back to securing our domestic coastlines and Berlin. We will maintain our Spaceship Grand Strategy, supported by maximized Science (100) and Production (100) flavors, while utilizing our Great Diplomat in Quebec City to manage city-state relations.
  - tokens:
    - inputTokens: 52861
    - reasoningTokens: 7714
    - outputTokens: 445
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Strategic Developments**
            
            My current focus is on evaluating the immediate impact of Russia's capture of Cologne. I'm assessing how this significant shift alters our strategic positioning and what immediate tactical adjustments are necessary. The key is to quickly determine the most effective response given this new reality.
            
            **Assessing Strategic Realities**
            
            I've just confirmed Russia's capture of Cologne on Turn 424, a development that significantly impacts our operational plans. My immediate priority is re-evaluating our naval deployment and determining the most prudent course of action following this unexpected shift.
            
            **Reassessing Grand Strategy**
            
            The Russian capture of Cologne changes everything regarding local control. Declaring war on them is out given their overwhelming strength, forcing a complete re-evaluation of our naval objectives. I'm now prioritizing Satellites for our Science Victory goal.
            
            **Revising Ideological Path**
            
            My focus has shifted from Futurism due to the changed circumstances surrounding Cologne. India's imminent Cultural Victory is now the paramount concern; I'm exploring ways to counter their tourism dominance or pivot towards a different victory condition before they achieve it.
            
            **Evaluating Policy Options**
            
            My immediate thought is to accelerate culture growth to outpace India's tourism. However, upon reviewing available policies and realizing my next one is 14 turns away, I'm reconsidering Futurism. Given the loss of Cologne and the shifting geopolitical landscape, a shift to Rationalism policies like "Enlightenment" or "Rights of Man" for a science victory seems more strategic now.
            
            **Selecting New Policy**
            
            My current focus is on selecting the best policy, weighing the benefits of Autocracy's "Third Alternative" against Enlightenment's free technology. Given the changed strategic landscape and the necessity of a Science Victory, Enlightenment is the superior choice over Futurism.
            
            **Analyzing India's Victory**
            
            My current assessment reveals India is not as close to a Cultural Victory as initially feared; the necessary wonder requires an Information Era unlock. This gives me breathing room to consider how to counter their eventual push, rather than an immediate, drastic response.
            
            **Accelerating Science Progress**
            
            My analysis shows we have more time than initially thought to secure a Science Victory. While India isn't an immediate Cultural threat, I'm prioritizing maximizing both our science output and production to maintain a competitive edge against Russia and the Inca, keeping our current high flavors in Science, Production, and Spaceship.
            
            **Analyzing World Congress**
            
            I've just identified a critical threat in the World Congress: Greece's "Endowment for the Arts" proposal will severely hinder my Science Victory plans by reducing Great Scientist generation. Greece's overwhelming delegate count, bolstered by the Freedom ideology, makes this a serious challenge. I need to leverage my Great Diplomat in Quebec City to counter their influence.
            
            **Repositioning Naval Assets**
            
            My current focus is on our fleet's position near the recently captured Cologne. Given Russia's overwhelming military strength and our current lack of war, I need to decide whether to reposition or maintain defensive posture. The tactical staff will likely keep them defensively to protect our borders.
            
            **Choosing Next Technology**
            
            My immediate focus is on selecting "Satellites" as our next technology. This choice is critical for unlocking the Apollo Program, which directly supports our primary goal of achieving a Science Victory. This strategic decision aligns with our overarching Spaceship grand strategy.
            
            **Focusing on Technology**
            
            I'm prioritizing the "Satellites" technology, as it's essential for unlocking the Apollo Program and advancing our Science Victory. This choice also grants us access to crucial late-game technologies like Lasers and The Internet, ensuring we maintain momentum.
            
            **Adjusting Diplomatic Stance**
            
            I'm re-evaluating my relationship with the Zulus. With our peace treaty expiring soon and their alliance with the Inca, I'm exploring diplomatic adjustments to prevent a new conflict. Leveraging our shared Autocracy ideology, I'm easing our current hostility to maintain neutrality.
            
            **Refining Unit Prioritization**
            
            I'm recalibrating my unit priorities, noting that while offense can be slightly reduced given the current strategic landscape around Cologne, maintaining strong nuclear capabilities for deterrence against Russia is paramount. This ensures our defensive posture remains robust while pursuing our science victory.
            
            **Completing Key Projects**
            
            I've confirmed the completion of the Manhattan Project, securing a vital deterrent with our available Uranium. My focus is now on leveraging our excellent science, production, and espionage, while ensuring our tile improvements and infrastructure remain robust to support our science victory push.
            
            **Maintaining Strategic Focus**
            
            I've confirmed our current persona is optimized for a defensive, cautious approach, which is ideal for our science victory race while deterring Russia. No persona adjustments are needed. Our planned research of Satellites, policy shift to Enlightenment, and easing tensions with the Zulus remain the most strategic path forward.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: bw236JvsHEIrA02V
          - toolName: set-research
          - input:
            - Technology: Satellites
            - Rationale: Researching Satellites next is critical for our Spaceship Grand Strategy. Satellites unlocks the Apollo Program, which is the foundational project required to begin construction of spaceship components for a Science Victory. It also opens paths to key late-game techs such as Lasers and The Internet, helping us close the gap with Russia's technological lead.
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: AY89a18ba+Yltv2ZLaPHAOcXIT+Iqv8hKzzS8V3hokQ3rhewdJTVs+gSaaSn5MrNL/vqW7k/21y2SAwUPDxHn5JiMBE7W6qPGnrr+lnIZWTdAA+uDY2FekKCRbvr6jmxrq5HhWobPXyAHekY2RuRlB5pFLqNeVWbUEPhxGJV1NDb+Lo/kliFnpAy61XYGhnZ239F6B7IWpwN6XI4KwPZ7zcOKtioholYBkMqmtLXkkE8TbUDuTQI3WMrITZdK0sH0tLHJ5BBUn55Ea60iVycsZCdiZrUDWFcfTXaltPHZSmICjuQ8mcl0wonRkowyW3p2VD0fAt9Q6YORXZS0fxFKsZ52fOUWmEmcdihrjKmyNdws7pUfDHRyQpowdRNfNWvBo2CjKwBI5YAd+FkDaxzlwNcwp2rVjYk13LtbZfSBBbNzeagNpWRSzwChPNGkMtoq/68JB420zfb1GIOpp48e2rMy7tNjDUIW9nlJSOr47hv3sPGTEKaoUhOyl+6EGy2CKH/gQjP+XGgg8GTHWh4x28pox9Lfke9x/QU6+vF397mm3wDCHMSKzLAUc6wSotouuAgga9aYZbA0CbR/Ympp9nCmHQtzYv5Pal+A9dTg0tariOY1sGjTtuumdf5BW1pEkygCYXHsBmU+2V3b6qQnhGR1FuL7+/9I34hall+SjKHO3mD3Ws4LHlRIclyUvtCEVSthqQfmLoxgC1Wv19J0n+hOl/1+IRIO2H7DCuAHZ2crL1SLdhoa05thMO0cmAPNmgOiJ5c4xPY5Wkd76STDiD9iznqPcqj4XQZZJYemQ3Zo/VlSTjeI1qEkcRUws5kHjMvlcKIgbruvYUCLP/hBwRn0QLkF3D4uiGRPhsT/5mLDksh/I9KKA9zCquUcQNvgxcNiv+wiMxzJ1YIte5vhJIhm8tcbiJRRkv88nQteFZbo6kWpk35llifADAnHUWVW1ozYPMJFxIXCEIG6Xi4sH29T6AgACdmKjxqO6iAaM4nva86Yq1jQwqpUpufGkMhh48QSV2yOY6llkv7eHmr7SKQXVnhsFZRLYxzbFStOB99lT1zdIGtnZ93L7qfigb8OHWJ7+4bJXX564TfvszEmBktpjhT87HJnIjwKmC2kIl8YqdWV+XOzALBCNpeVblBFhuIm6D3aa1Qhzy2vYFAWLE8nXmUkaPnv6gooDLo626xUWC8dEKQ2jGaB+ngGq18AswDwKGgOaBZgbEGhW4EJxi8oMAmLt5Iha7KQO8efezsYynhjX2UVrpR1WbiMsKjZnGEaDLqsrDwDsv6A+gW0+2omlEkdBb3JpSwdGE7nLanKx1WSYlkJJn4pvMm3FydVHLIUqnDqTyI4PqrF6Vfmq5xsxipf+H8icihA1v/KgSeljf+g5yO6jGd3hM9dPdYw0LvcF4j1JJZGFtWXQRGeUXX0BQooZubnXWQcfNaIg1xQBq4rEmy9fb9CktO8e/W497SW37UVLyDsHKaO2QxsnEsMCXrDsiwP5mMJOWtwvNZ21S9o5XYktdJ+O6818KQisVbYqlUwiN/SeNVMgYK54ksLIjqf13Pk1Qg/+1q/EX2TD+YUeZTkGROHLvjE73cBmhupEXmKoU6K3WxWt6DAicVjvbnOcsUXX3AypwHEv9l2qBwOXizSWQVhd+TGw/cV58/jVgsL1StRLt6/i9d8Cb5sYdT/zJxtE+FEcyt9G8Vqk35VGuZ743+1TLl0UgBS2xRvkwhtxtljsJ0m3GA945QgM/OmsSbOp9jIBO1ir+k1lw34r8WizV1NJ/cWpUlrM1HlzdKomoDS9yNKoIGkffWbmc/RCgotDmljKwLhGh2sW5RWkfq4fKLsqO4mRwY8i0vhxYwewEgniChSnJZwzlrw8EPww19gZy4DUY2w6RZ+bO3uqO27sijRmz4F0jRhTKQ2HazeBrr/U4Lh+3HISOhHBLru2E+0//MXCVkYXUCH0l3aXXi5Xs828BBSKX0qCcxE3wd7GmDamuQu7e+Xo6EeeBEY5ExYt4TWQSzGU6RkS3d/s9ZC539wh5P9d+OzQZYaIBHSThqB2s/yiwfwBeGdIfWT9mwZEF7I4C5CpQjJTkXID0Z5YK0++ScMko6PY/kqpC5Wk1HLAJY8/T2agVeImBogNB821DkGXuyMegzYQjpIgRRfdklkIB0nUk9OzI6AXfjg0bl/9BQVrZoneumQN5iMO8YbBfV7UPyQ1ANltBEtTta/5Qv+ieWS+GzKkGrstkUSSon/9pq2fcuw5c3NUf3saTGe+JpVi0AMWuNz6kNwkrY2liZSrFuiHLzcOqyaBPxJ/Sl2F4Ul1auocTM4vP7cCXjsziS7K8GtQVY39m2cJH/iEETqQHVyw+2EPXzagUBHl9g6fg0KNi4xPrlcUJOJzLkRVNYgI5oENx6M5hAX+1Zo3FdlNPkuU/fK2/eM/l7P57ZPw6C1z3NObzk29yOkd1m8ZZH3dTVX2/kewzq3QB4BPcu+50OqJv2L/d3JEvM46ayB9hFuUAV7LzO6p0kTI0GQtAgWskAgwpVuziPajM7yzjdk0tKwH2jTcoWgQGpAVdkElw5YLweneNsb7gF4VauHykME9QbXq/Jt7P8swPs6/j9MMs/k5NED6KBJ84T/OsaSFPyMwch3edDWyuEjc8x4lTvkij5/Rf4wC9Q08o9rST1T0MpIlwecUUPu7zXhk0yfqXDaQZKFYk+0Yvr3+ufoG4e47AbwNoTzfPUYHTPX8nAQO1gw/N6ENOMh3vGYJUTUZ3d3cukJEu5/yKbh13vnXFwWziNINJmGpP9gM89WOSCT0FLf/TyTJCbpaV6sAd2+67tqOpZ+SHGrj0P0fH5e0HRUHhdSabpiUjPglKe1wJOZOANEQ54dwXN7e9RA8I8UHhzfx0G+dpoGk2mH2vkx1jCq756WG7j/jUcPykbZPQQ4vulBbB7vm4RTF9xCs2WnVwdZ9iaIYhEID5rteA26rMU5J8As0fY6ERYluvN9cn2Nivj8PrSSh/hcQG1ZyQ5eivle0oxcUAHu6kp+e7FBz9N+94lyoQ3ijVm0+So3f93UlCQlwbcbkeLkRn9fM2W00OmHz79NOHMZ5uSjY57AFeF9+u0XXK49Ps5QxNI+SiC4RvEMq/N2LaVH0WdS2KcJlJniewbwmPbxmyPfnE2b8BdBl9XbeRuzwisOuaiSCa/b4pRIRyLPd51HEIjU8OMKcFNlJxHYr0J1grnORlBjb+72WkC1a8CLWpb2De4+TzTJHXbdJ24FpjJ3a0oNWZzR5h+vy/PyccpDtjJBs1/cqizSH4guWUtFxhH5veb59q+osIPtw7opmGG+lQNy4/Zi6rzYq1WsYxlw1emRqAP2eG3wuKWatbVyKOIBc77cZbbN8NlQr8HkTn5mEgHPHYEo3ihIXROi5ajjGcn7IACyuupjLw/hTi6CKFoBk6Bv56VDm+n9UHvtAsAsILDbIVz6APNZ7XQh1bhpDSrlHxZaUo4jjrTIbCl8zjQKPsSc2xFl60ZX/alv90Gq+6iGoY96ZATr4RFP5iElIIH2KcOarRxUXo5FYYJUtdWQFr2WoMhS2OXHEfM1UK8VmfNBvBKlnPae7ShY0M/k2KCZenKZTnCDAbs6fCMzDKyTHCE2bK1uw07hlwQGsMpXSeJpZB4euWAkQG5i3CN4E0hFIOZWb+sQQ7xE4FbROMkag+islbRzoUDRusfvLYiT9SfLbWqBJIMvyo4Wr3VIkxu44jxt53UnIeni0yDZjaAquuoTZvmswx6+L61HCtc778wEErgRY6mflz9TH/IKRrgrTFae4VpCoEaBRT47rQw/onHZ/Faj8H6xwSqmM+RiYBO4kgHq2I2C5DcW9eg5sg32/X2HvpqvE1BwNm1yN88Rp6UDC6fVbGrvDJ/CkWlxNYTEcQ/Y5LDVfuNFsOXqEux1W4Stt4lJpmOKoDfAylg8c1RokF4xHLNE1jjdglLosXhfbvyGUtpjjhg5RGci6nlKY4eysU+bRu672xxycf6STO6F3TNI2NVVG+ipEwmu5E7guybV6WN2OtbNwN/egWk2oqWzSgH5qK52Guinj2OBp2OhzSlcSCQ5gqxH9ooQO5EV/g6TndHWtrxk+JX0ANLohnU+aKsH5TWrgdWrUsW6hVSrCrOcJP1ZFmFddozZZip0KnMEmZQusEpjhEJ8yFLHYa2Uq7yNwI7Sw72Nsr9bmAYC1F1i1VjEW5IRJxLigkyQF2GLqy1f21pFosC5OxWbzux2mYzG0uutghgIUAMC+1itnNjhui2Huv4H2vRUUxJ3gptOto+ABcDvs3SBVl+GDY6iepMtsQ8fP/6ENV1k8NHgonlkd+ORSQcYlAHSetuuse+8QxSb2SMSBwpq0BC+1ga9EtnWTj6Irf1dKUuGDT3SbWwBT8wXcLMQVF+QNwHtBSiP1s+IoZVFecKauFJKd+ZGolyI/CY4ba87smBeJC4WnF3xgobx6sslfhAlgteW7y/ofmX2HmKdczWmer2dR003rn0phesoqShONeWV7kmKxG7thjcL6SBipEaBk0WPrjZfKBiHiSXs91WyUOs3G77ejvFDosleSHKZlvLyifpeUfBOkjJV/fOWuIyxStVRLXIK0+iy6losW8aIe/RzNaNIwyUwMOMcgvcrCT85pGk8rQp2zU0QuznjTFzlYPsUsOLrX9ZD3RDnsDraCdVyObfEBzRXZyBSxlhESK6rP4EHhfMVtYS7ZOJx6xd6wUIRtEs9pCxmgBrewxMcv9OL+d8k//cG90oa0KsT2QHSeJam8ytiLMSlruWEr/qO4yPrWaBQaTqFva5KSst5/30szS9ZQvw59DZavzrRLzMbv5PJm7Q23xvEkfyco2COJi3srTee44JRHLMYG/KrtRQ1PTid2JKY1jdvII++VK7RUixHYs0HV3/fX43AEkebJm6QvRN/eBxutaYm+NyJ0F5YNFmuOy3Da312igfSWu2/nQrzSBG09oZCdhopiHz7db4ZDsr/dFe+D7uIdiEdF72v6O10siblEbFWrivjIKHX+K68uuPKL4/DjoX99LRJ7aD+WbrV7JhxJKs3FFVBQWKQia2pEWtccim0nJ6LpkA36yKqGYDqDuYWWm4riuIMuxMsT7Th4Dh6aZ7+kZxTvkGLzha9kLIO8OuH4ScPUg3vuBwrzukGfE1hnS6YKtB6/27re4eCuZp1dwj/g5gVGZUltBYmtESQYxHjf0FvV1lOpPE4uTNRcYDQx20m+4iRTIf/6sUr9NB47xAQjPXVk76QlLJd7tCyowY33lj4O3f/0aENFYC5VJC1fixZHrxwdlcZST5/azb89e+0kczaUoOOmo8OQx0IsSfRY8mVnIx2pMExhseOnNABGePHcb4ExcmlmvG/ldCWylWDlk42jYzEjCk0jGX8JLylU+g9+JmiKVyc+mtJlubiYi0upsJJJ8POuSPpzStScJfkSzGKPXdH1kg4gxAuXXdtzfKnYJA8ToG7a3jvECsrkpOgnalH/K+wD6E7FCr6WUYCgFNLNKuvYg9m28oAtIowCaX90RbWFns951x/ZVfF5pqFDAz+2DJQdeAe5P5JULyaILY5PK8GEAtguH6iLlkxnngkxfE7Czc4bGsXLpoDrHENV1Y3T3aW2NKTBULWdA38LQb9eqiTa+me2XkXj6HagFelpVJglcJytRdT5JdtSKgleOBN7zY3HSBF+SGJMpGP59BC52lxGfcwMt3MONml6q3VpVN4StJC/ACyaAOCDjYryIYd/UK1/bYN9DmDl/YqjrJ3r6oir9k9h4uKI1PJPG0CY8jFb7hCRX//tZ5A2ssLeGX+NAlUNMkOezfmUbjCb/433WmWBj+Yb4zeAZaowMlUfAoLNEv8XNKg30hzCsm2eDQoPdlJBPXb/xmEfEaU5G4h5KeUsVzKgpiVJgM6zXmTRZlp41e+4qLvHxA4/ETxIOTIrVjF+t7b8iVtAfSgYvgpItkVHhZLn8hW5Gh6smQwNoEhjBZ1utIMizACe6XG3zdD0Cp7oneuRiQw48+smoMZa8xcjrvAwrddtMEkQBeZMTS6nvu63TCb/z2/UkRvBpGNskx+kg40aYfJg2je0A4OHo6z29e8GdvUDGgzpWrUECho8zB7M5j2ozUroIax6tlsU81QaIoBzbKz3KRr02hpEyRz0LMFtH1zlfDs4GyN5okI5dQcDJ/QTV6kgDbCiPkpoLwVU2fCBba6UPt6go8Rjb+5aRsDp8BB6DBDHUv0pLpu9n1OgJzTDC3UaBWDdfRIO9rG9KIsFEkuUHGMeXRvvsCZbi6nKKPOL68RzBYhzfRbRcCQDANsJeHt2dz5T4uGRygc/yEx0NbMsrSe6agFlo+4vqMO/P6HHEB+RXAr+4PNxn8mM9NXQZ8BtSLoPLZ1zml5AY0L105Q+9bVs4JPIvqRlrlwoEnfWPMnIh2S6VUQ7nMQMfHVGQo7Rm50dZW84R9FpCL7M7EIIjyqtGz2X78/fOGpeDZImTOCEUDj3jiviFViFAEjJqQTYOgCDvry9Cn0vyWLdj0G64u4uIDpCovI887/OMJpq8NH0PSk3yf1ItgWa+GdVPYZ2R7Zx4P3Ejmf+whPTUwQ5NQrSTLW/FFvs2xGtNRYKCHim7LuSfNM4cY2X3DFAiZRndfm8tj1MjzbTZN1dS5uLUnuXGjzkuDnpkvJDDYwmbzsGU2ykF1Weq3ijwMHJUr3CVnvB9RTnCWBJYqvyFA89eXY27gSuP7ZGx5sLo9Caq2zDZiFY0qJKmBCAC/lrmJ0oY6vG7KoY0weHR5Wd4+VMRmH75eiyPwCm7nKpxz+C0YivnyVl9BBAQXEmlwIvZHVPARTaJmLd2I6gmLp/Mx5pdPqX9oQIoxbSl1/gKFxWM8LIknqxELrbarGFl2IEksLqmQo9srAVTSCYWwOUvZ7xbfG3Lo5rG+08tAoZto9ihEXpvX38SO2Arbu0khT9/Na9VHixRVPu2iKzaeQrDMuUltOkzdvUJM2cFoDKtlQKUkrTEHQ4IOiAFzVWlToimjR9jnaEG946dWOlv+Jcadiv60pU6U1tf+zSxJ9UU/BuTQFGgU1MaGPJfZ4gunQBEMmD8QhUStRjTPdkuFhvxcf/gE/h/M291Cz9z/SGSqiFD1DBLCE9N3avyG7Ftf+Hv7T8nu3ECENW8U1ebmmjNhWjIUdeqjAMYbLM1OLk0UK0EB5yrs54bZll0d+NjP+ysmR8QyvB96ZA/ewo/hINhm8RgO3U19iR+4/lZTZdFzUx4zx5l4kWWJ8vyjahUVySz96AobRDYFsRer4KwEjEL1bWWzAMMcvkfp9qiCypWyzfctC5ytvTutQhRrFJPvVIQ4P7lw5lpg4XpUXBC9YL7UfqNNo1rO8I3wSG1zvd+St7LQY7xd0Jy5lekzgZyfIFAxtj2DY29EW/aD618QB6P+WinFJvHfg8Dkp2nmc/KyKnB7iLsWCzhFsBzNHY6zsjGI9foa8CDeyiY6f1czt4VOjOHGd6y+DMS+Xif09y43W27RpLNbS3qP9GX5oVPJ1QKTPafs1kl3wODZ2lz/Xr33uBYb5WGdhYjOXhGt6G1RZmu+x9+ZYK5dlzSpAfCtLdP2R7rhyVgoEl16C9jnLA3WyeTon8xD/fNs1PcGd6gWHLYuSiMmd3xIE5yksPqEVC/3wJyHbakcc1uRw1fxECpt3P3wGuv0IGXw+59tTkPC5vt3Eo56JbIClZ6kLrEmGphLEKSNrGShX5DZuxTInLIQ5FRCDyMwsouikf45sezqc9lfkqDM8IKzSQp8pRbJWeE8rna8Xj7+ER+FVwKayK0QkDqo119VX4RG2I+Unlbe7MxvAH2T/TXXJN9kSCc1QbwyjjYQ5HOjQmZ2lFd5kmimp0RXk4CbF5J52kuKzH4CbH2Ur1AccIpbDuDXPOHpnS31rsRGmcolNdSeJ0DMJMY6CN9foqa3s6C0K1xGafWLiRm5d0u+hTBv5TZ8XIbtJbUpOVOCdvCj6bD8VUB16WJYrgq62d5sLfY88mId3qnZp+53BlaLri9GUeRowtIT2R+PdJlWgWIR58jskdzfkzD4cO35lPLNM43jDxb9BVxP1nBZHc2DeJNX1IRnrUKG8V8JCTE8o9FfyTnk0rI/W/of33fipOf/ZhhcYKPmdtvAPFxk2VPAPjnbk5zpti3/teumVa45FIDF/ST3GS+KPsFNw/w9lpA04xehClioKJCI52LHJHvLhxs1HJTe6EV+rfZTotXECl80MIaFdVkMFlLo9XMMTnbDh4DJnbyFN6LDCiRu6HF052zw1Fiaa7Xs5G8cBVhyAX2pTXVDhbDwCUZ4EvQonMwJa7zzIfPhpO4LJ5/ncwKjuI+dmZWpvTYUwfUnudSAImTU0bb0zo6orF2fj499/kg9isQIjQfQ9+N7CUXbzNq0HSoCafmuG52zbkdj0UuCV6k4e16ZTyvCmfUBD7BFdfyiK23wo0SiBMAoBTQnL3YEJY7ngsQSpBTOg6/fx8GQCUiVs2WcZrzhGtMBXNrjICtFzWaKaItUEXQtkU92HKdu/LZpS6c5QfQLNxXbdg69RXYEY1W+JWkS6JfhFYlm8t+YEbNkww05D16XxeUmZ1aw16AbziNrELll5/q9tC+21pf11lzp4H+fWyx2nDXRT8NN+rS3IcrkivyK3vReNkvWKgLGOSO8QriWqZti2bGDO8O6SrhVjknJMy6x/xfsBBbXkV4st7pkhysF4dQIQrRkjbWuPHslnBbWDemUeWJl31dfJZxz8icvp0fo3I1dvVuLcgBR00uz8Xj3wr8rb9dpLPEArUxkrtw+S1XYn1wpG6+jYCWvZhVw6o+lRWuDoUXR77WeDsv7LgyG37kdVSero3cTnAlvYOu3YY3PjMkWXRE2CsyU0eXEa3wWSfJC4ngGEqI8cZXPJv8vdZZ5cfnyN0IOwP2LPiWLSVTKy3NkhRNa9xA5VUNslQPuer4PuI0mRaypF9Hw+9HwGtKce+czm6p1V6N0KzNMFZZSUVioyqgoQX6J6dr5pW+IFO5nmfHDr2JBYbDWOQNKaEKyWXE4/KfVS+V6gz/RpRxoAxsreUREXnYRRkwZZLQEGaQD3kXrW1nORXF3wrpGBmqDA99vNoVDlz3Krw/iX0iAOmlt0UAIivHsdzZlP34Hpo9AlsEe/4b5pR3YQP4mnsnjA0VklSALXVfJXjXFX3Y0UEwsuPKBhvZF/7RLo1KEzsCZgV/Ib/lzA3gkXScXxlwuIvIg04LUuaEiR/Z+DgB5aFhg5R1lZNuHjgTO5jCAS4tlEfVOvuuxmqGQzxNO9xPFitWUSRQRC5OS9P/s5F7hrF2Ikz0T2chvsznQAoBlS+zKxbMO9oQgTrxai764re4ekJmtZ64HK9DuXKlzTUFUVUXPfZbCQRJ+UiKVxcmcwUooYmYx6t9Q78CVs62JVDKl2XlRiXVwFfOgWi38Xxm1CcAbHhto2DxqB20lYhHil4EI9vtESuXJfcAg0yikYxzQu1VKoFKfxa1TRKSn8ls3ESxDpjLTrm73bHW6HZQB6RcCypA/gOLwsRnLcmEznEbIGONpi4pCAA6X3ZED4ta//idGBfxiae/qE7ydMfaSNnaL6iD21F7EilPWk0i7cLLkCNTyzkf+Jxu3FXvYMCAjIRNfOUdDzzA8PSJtr+LeiVjraif5zE/quE3iiZrocqt6eYghS7ojjNcWzai+sf9zSuXvfYEH4FokbqK9p078Viq97yv9gPogMm87XHHV9UgUy6BSE9nzT3G0Odglmnm96YD+tfplAoezDhh3aCBSvsxt47eOqiggB23bqkIVF+l3RGN42Vg1Vv/nraM6Gk3C901cS2vy9tcu82di0ujzlLKaJ718Qb/qnpTkHurMtLX+JJ0YQwrRaPnq71gwUm1pe8ZBTT/Vzd0Jh6TZaqakGk8j8QgDTLNvGJUbNnDxVjFTE3BE5Hk4d0HSlrzPyInh91GOgTyDfIvtdAW/d0ihV6GvHcxl4RsptAYn0B+Yq0iZIQQ9RRI+8/y+RO0fy0h9TAfcItBKzMypPHEX2gHoDQ8Yg+aCIiYj23QwWOy64aYD8IygXQkUFkeJaLMka1f8j+3pgqq4WkKBopgdfKAU2rB3S67baOt7gSX+eseDCoHrAbZA5y5674E7khwUgSl1MFcGnPSxuAt9Np7QCRQ4U/FOUvWFuzlNITfEqlS+ktWBaAKwENMw+kMh7ta0rplos9TJ2KjQc37lx4OEdLzpKzsD/C54yjNiUE2ZMw9VAjKdylf19XlSip+QJVvsAV34XFdQNuujFOXMf7/aN+cYiryKNuzBLwKsQD3OR1mtSWDKZI4XA/nP/p10HNXelo6b5cv3bYle4hnDbcOUl3twvBTH+k9BO2EQJRrmfQEIMv5WR6n1Z9cvCYEKBDjntzD6sbhFvBouhpQH8xJrMu5QAH8NIeR2DFNTpy3TSPUjAz+v2wo+QuJJucMhs8r9jgMoKxq/P11P8MFYxHC1AwRKHhdvibjyVAIXIyWYoVy6fwt76pG7SQhvzqYzeJn0X1VdiHhjSlGnnxouIdqhiWiQpO8u2HcxlCYYMnvlkN6s8gYgixA9HVP6uSRUVpAbNGBb1dcOPmYcdrGoWBQsw0laE40brkvWn8GXuyV1sZYjnXrEoP8jedB67peYlg4uteEvxxGsthxy+1EBagcFT67raY195/OX7RKbtFPHMYd4YSDEbINBLyk/8TG+p3ETNygwODXqAdgwomec1kfWw8vqXQ7W8l/YUj+WxM7B8ycaRgcJFPzTIVG3Xmd+rt+XjLCrAT+uow9k1A4NP5d6HnIbZOm1RW/UC3KwS3b/g00F3Uqy6yAHpvacEADE+oC4A55iRsn+O1FRyJrwwppx2gNuz6s4HNA/zCRJWJnNbb0P1TN4AnI6IbkY/6o2mYX/LWLFhwGIH1/1AIb2RsTVqBkNGNwaNUhfTj4Xk8QKa/zIHXGftNY+16wW4zq+yZAXCllinX601pT9CvvQRDNdDUHQrrZF18j8g05b+ave1Xb0LiujXlz41Eo3ncq/N2+WY7hhaT9KzjpyT5dB4qIng+OYB0yDnRS77vdhQ7H6UPpJR5NkomGyR1s4KwjEspEQpuWy93+wz4q0S/AV3yvuph4FJdZxMzipJn4fzFF0oXYZf55OKgJ+jFf4I8BQgoTyEZcwL+6zY5O/fp7qxD6MsspQPqPJlSPfo5dyQwtAQFhYqBXMMh2YDlGCXfBUCZDiOMZAyeGX2tZ4KCvVwX/fCO9IY6pxz/sIzY8v2w5WtO9gs45YosSeG5QNt/CvBZPpd/wjbLp8nlDDlR7wJO+FolHAQJ8COl8RIod9FZoTumhamBrzpDyoQ3tU+n/6/oOG1doxhhcPH4Z7nZVLLn7wLg/uedTAOKLxR/sBuTaCLrFA3RLKNTpDiF1H3dK52o0Iq5W+9Of+7gVuaV60wFBK/7fVkQY7wi1Umt+z0u8sfEjIdLa7RUPnYnxgLILMhtGB11+889mPiDrbI4tdvA+GQIxwyvQChpsOtffS7UAJXeQPIYepTZaVYoLfy/KkhSEZlDCEz9YJ6d1n4IzJ2MCadZSUUP1a5g1ZLrYI4SSJUFnc50sJTtW3J8EDHKZHcSJq/keG9ZM63gw0lL8dGFvaHPwlFa5cNO1l5ksawzW6Wmw/ByMSA9YAH16wjx7HP6zA2WifKpiY8F7AKYozuvJTjBwmFyKN8cNrQXZTUaankz8jAMLJVzhntxy9cWxYY0mpy0os0imUY4Vn5I5Gc1+unlxplDh+iiSkEPAOiNec1f0nwlExZIglD/tFcnrWAJ2VtbkDB2nWnt1N0bSnFdFOdWI8fr+Wc3pZsiYEJ6TadmGoFZjr/JYR3V5+s+btxUm6/RMnjoptOaLqZBPjyhuin2SANFCChDifHU2wQbyy+yVOYdXkRHy0OhErS1MXiODMbZzg+X0EF+TkFMZD4zQdBTgVrBNeACJrVAS4kpD3ORZi7iyhG1frSqquF6uMaRBwIJ/Td5HzOV4XG0M3+EeS4Ma9dwd+DADZ6E+oleKolswJ1033nWP1cWQzcdU+spi9NNf+5+ovA8QOgpphUu0hJpjAJbpQxcSoU2yAgBm1/5mGvs0omJ5NWT8D9upPcx3cEZIoCDGo8MyB2wYf+c0EdpStxUnftaPNvi5QGCoNuY36qH2FTM+aHNczL4BWaXn0wnlkaOdFi/uW3TcF5EsUPMwks8V7CtvKQ/a1KVjdSknv700Zx1GDz0KaaWTdCyZymPxLkSzcWAdB+yFKTGyQYGT+xpJDqfcNrjZ4zPKoAjnfI+eiX/1c+8UO10SuOieOV7EcwZ7CU/571BlVd9hnO8D8hFDBMTwtFNPzSvR5iI8vA9rXVwsXCKpENFvDLADvyCESMyuMUBiZOLWqBfdD16Ig8CdHuICuyROQDh9RTP765a//5INKKLLOoyKXcK4F24JJ9x6wbFzu2YjMGrVD3DfxRBFOK+KZVkqfq1eaXWaV4lz4aSKZYUMHJpVGOo1F5onznxfhc1ib3cA9Du3DGt/cKh88/sSoNAwwCNsOqYYzf8G18yTTCmTBOoIRN6Jks7RFctcJrWhoXy60eYz1tdYRqma6FDrlshIGzVRex3R8bEMPjjN9ljDa7SOJ45vxMvB5hNTiqZ4SRI6O8w6cvmrjx87dApp0yWgxNH8ogt7BR1cjeKoR5tSJK9v7GrLngV1+BzcEuJntTZf3ZpkaH2oYQMXSNKbWpiNRB/uvwTYdqpSY+GxvAWiUgvTRe+k2f5uiY91UwzWeHk+Np7/pXJmS2uDX5PEyQzzCrOqqgu45hr/HplivccuKEEMzaTcbdIy9ivwOmxvIq8Tyn9NETVMf2xIxXMVcv95FwPbrj0P3PRGytC2agOHh/JnTzK/W+gBtAEKGY+PELGic9jlkKvIvnnwhXgVUprFsELuwgpLH8lBzfOt92T6Dvvs+ese6pJGFVj5s2gLfKqHnLn6Bo/tEUSq7lQPn0NnfObxFD1do5/4Mj0RHdA1wgLvoJJx2YwhBVK0MeJ3iI0cqPQeOI+pJuBAIdldp8oFm0uNwfZSf6yqPFT3jFeiZV7nSFnRHYdoKgNDVQgbnaCOy1qQ1CLgfy/APsS2AAPW81/kJoQsR1AQN9LbTI4r6ypYfL055Mpi7DM9tIsNz6jXPWdUDJsrJBjHGGJptWQKBXDdRIcgiOz03HRc99Q/u3njnhc8A9UkbEYbQWC0C2jQ4VHo5jHgMPuxzp5mUtIKda6gOrtHSkqRPU8AvpwTcMwzez4a+MC4OVtITBery1mjJX9Qp3uQg+U2QzUuDP8C9mweVa1xjWf0vrSZpCKJHnxROIFVYS3rM4bVd3LcCx5R3jA55lLjtvrOU/UjCVCjbD6fxuigSuXMWjq/rYye6dBgANMczo8Ejd/005uCde/PKNuiiy0Zj0WcTgy3ER7cB7Yx8K13v23L8pt13www+gjrADaK2Q5/TjSmwPgf1g+TWGn28IJ+fBNQ54ElCGkUSva7EBYdc0U6PtSiLaCgkRJS6EuV2GUgVHFW977qxVPDc/6Xlv8CC9nlcHmeWb5I/jNqZh7/lCFxzHW9Vi+0XDPOmHLHRW689R5RrFXNj2PlVDntZ2Yx2BKBb1nqOuWXRNfwVBYaVXDUK/9OJDaWy8aL0zMDoHzUDwVcx4oUdjV1jOnvDAjey+Jd+Z6YGiOYMLj9kKWm6Gdz25NtlzFbNQMmQ7k1Qsf+iIQuYocnJx13RZqv2W3RR8fjJHgMUvpTUEkYyGKZOvTCt8bS2mafHwNgjqNvaD2kB5gWJ3PUX9p+OmjZSK5nllBzDsAgsyJpNoEGc/ABtcwHwTNFO5rzlYypj8jE6MKUeNTTDyE/jm94xo82N7scQP6h0XSkZLx5rlhZxeV9y1RJvqpro708Eo2HSGI1Iw3QCUnwcvbsV36FJX7rU5zrH6AK3U1fJnYUWQjALGLllinaYRLPOhlsUFMxh8pW2RhMenGU3qNynr3haApLIV7o0Mkkg3nEpAt3lijsqKFsejLTb0CENjcfWNQwjMwrKrVPE+dSwUAS4kMsg1jLrCdT7NXM/rfYZv9DWod5WkxU4DGCcyHGUrBDWBPcsk9dtM+mBNi0g6R9d3Wi/kbF470YD633xC4jvl7HXui7qKCcn87CEdEqP2pZe/HebfWxcBQ88lT+y6c/PDabzwQ0XnXo6Z9RX8DTZiaPK/EXrzRHIIgpKsnMJ+RcDRxbovmDF3qfYzW6R/G0tfvZIs1vsbB+59ka+DIJMIl4KWHMBpXXlRXHTvvzgQfORgVv3M9vbiglzi7I3Oe56q7WNAAWWjwZsGQLyTH1hr7Qr7aMtOYp66iKoanIppR/XbhV61p+VVHZp/uJzlI4K1+hm2mXdT9LX7Oo3jlrkooiTOMOqlpnh0it7i+jBc/yeIltz1jcIRkZ3/4LEwucm54Tl2WdxRpea+1h0PX1xYHfzxRHwuotqEAqh1hDnQv+0+Dyp8hh7KOpzt8rUBZjuUw1jbSGLNI5O06uLBbmKMEt5EOMHvURvyP8ATqKsts9xQrad+/Kan8mf+n2liD3BZjOwUrNqCxbCMQY6rVS74nkjpSeiCZ0TCbirogMPV4tjY5AAlSRCdgRubQWGzsuhM8BxCIKr2IzLC3GK5+3J4koIEkEW6TSMwK86UBgXDYOAHnvR7JnWhjPA9LRKcIBVzsnlq+XMaz3T46zrca8KdlHav/EE5ILwRr2nixnJFBjCHLeNWBPBU56xTBxs2yM3B2a0u90scukix4ji9VeWWY06r5UtKtAVUsSws2vKAIdFVpuNOdZk0vD2aQbvOyGpV1vXs8mrhCY+a8bbw577smZaWMiXybdDGdo1jEFB6NnfZ8W9kvBAKpchVye/EUYjXOln/0aLWZriK3JfhJYmaNeOi7l1nguo8Y4qGveLiJYx0uTXhlUpnANK3kXVwzEUJgDpoauieCfaXxocDOKhFBH2ASi0I+HT9M63nAV30Wox8Iu/PVM+cuyYGFfH6TY3Vn7ObdHUxXruJlrLGoQ5L+AFdY/39to2SkqIvKHxugL3/9Y46gyeSj1O4wkSbM8MpBLnBf0a8ZBa5RGOsKKmuM4V4UpWJRHPfb5jF8hi8BySWIAGl2xK5yIlswJ0+wqmwOcZsm2KFBR9cpW0vsq8KBxM9C//a9nN+FbBEswxVdUHoIjwTEOixWXAM7FH89drTc4P2aRDQtyKYL8DTAoiu/bkk+jDkFJ/SFzQzHha4Q+J9a9eBwp8CgEo6rByBwU6ZfPGj4Iy7X607e4duiQb7TW3QRf2F/QEIWn8YIYwPxpVxqu3WZ8SCx47z/T/yoh3lkenRInfem991HekMvzuqpuIc9szxMfpYS5NvXSXXIpOqniwVyJp0Hpr/joHLF9ZdVSPinnezSIaZHlYUfopIw2T6rZUhbYVKJPFmXoNyOXIZ0nNGVdtKog3q84FkYz+OjMkRbjliTjAthICar20rRWoQfESVBT9E9T2D0y6vWc2nMfebybrb/95c3AKHLG11V6EP4wpuBD9CXerEvCBRJadU4UTMQkimll2t8gm17gclKkfm3d30atmKt9qcMC7YJMeR4HySGGcpDsh7AjloQL/TkwkDyumGUVlMgHCov+Yp9Kxm2YH0DS2sQ/Z98R14Jqt8gmBbj49AehQP8NXCe4TJxBqj1mVFpz/zfwHgJFcUDVL1qX2nQAuu/qKy5SkEZ1lJnAVidAJKTrsd58SwTMMT0p8H/3le6UBa6/ApOcJ+rJCwPeNG7L+urc1iaSlxtc9xse5+6M5sinb9zG/4mSDEsr9S/WOkHXVX2IjSqJW3mZGOGN+KlIozVowfW+j/8Jf4aQZtNIrpo2GoZaNGLyo947d6lZNOfAVEvU1SU/1yBI85WiaoNK9vZV/Fc7DZJcrPLBpmmJ+lOI+1OtYQD9BaDuQpbhEtjGmPBlZMtp72geFbfN0t487RVmG+krA8z78uAMcs2iVS5ndPJrqp7SciF+A9u4QxyBE2aS22bx4wyPdxk4SgR3xVCHaGCidzKmcFbsEzssaJ2h1oPt0LXY7c4MP2AVMBSdmSdqRmCZc0hc+0HaP6qH4SOUickdIdUkTIunBoM1p1v3GvSrji+ILO9Mf9FFsYwl+DimFBNmN7IDEu8SdBABSisggRFgvjI+qTqWgs3XlJh2oA0tluuV3ocq1oSdoX680gZu1W8zx+z6tFFgkmdq00BUjYRhtLciY/dpbCKay4+HbY0kdGwCuXYbQr/qOdNb6+qVFZJpkcVOQ4L8roo9QugOYsHxqOJmtHZKQ51IuMN7785qPdgFvaeF7t8lTcLLRkFB1Yj6b7iDn1lHsfagwXYUxSx8A1uVOF+B3lmnssaGSLpx4ZmRH7nRddY0dYNp3p34zXazq2VjJ9b5GWblYi4HH8uDrTeWIz97fRi162OnUiDEmHTdpG/SvmaXiYPFOmoSt7rAkNgqmVCpsJA1W1xOnJO8Xd4Hea5MO7o5c7CRQxmQEbrf+JOQT2+KhSmSxc0E6oN/dK2VufGxr/Xrwj7kyxuZaPjIr8cj0OwKRFsLMd62CukUIx4WxWdx/UYs10AWxjTSIJk88ZkfNJsB48Udr7Hu/l7eIQxRVpCKu6bMTRssPnnU8ZxMCi7K2pfCqI84PGfw+OBB/949bEQo7dn6ticUeHMfP1qH1V/FPebACn49cyqpNmWvqTN0Yo3smVEEmuhZPwvPtqCNFts6VqpzNcvF4395FTeGZqtmfwYwJ1BLzuHBOMpJadWDyWQpl5ZZU2zZiKKb5by58qLAb+WNeBAneAG2GvKv26LQIiGsJd6erJ/a6Cs7ytjrQFNgW4s9Tyu4QIbnV+GsQxxtPZVYCzOhVGfqFGee92tcgMFPotFY+LwTiTEGAGEhp9Me+qWZozFYfItqABBR7bDF8ZKxoUyERqUxjOJAmFbn4St9UkCKkWziSGvC0o2574uDJoZAKaqRG15Q0F7lH0aAkIgZlHRW6IAzpNunrerkazvtuT6bLL9BQtu6aaYKMGvBqzWPoG1zwbPxgESzhsUlAuv3GIgret3uhaYGdPqeuezK0yrwB6I65yBo/RrH9m7mz7+1ZbciEHHIJSDJ0MVw2w15/VU6XaWlQcG1hFGdgdy+WZCYB6TOCGlQ/oRY4tSkAXmhZMii+gbPgM1tya+nvYkOHtWUDq4ubGXx8a6DJ361DIHjHVGBokgg77DZa2zNSCwgmIp+xsMruWhffs7xAtcXibDTBGEpTK5I33LxVwiwL1F59qLrK0lCIEAv2W/G1/dbMnQ5t1LL5ovtxTTJZZZi5X1lv+ITkhP0PijIURt5z8m7Z3qimcXPQhRsZ2417gpNkd5ILUWUqvkHXiebUlS5KRR0wZEkJRb9/yq2BY3TzOacNW8TAoAJrtScZ9RcWvd2b8lPptI8XJEddcvVtWq13HKNSpjQyWaA7KgUkp5s41uRFo/uDCObuQ5cHdomJNfIxnaGWF2PFaCVgATtJ2UjVIDfyBVcL2vF5AEHJWCqAu75yTIuS5asTG88bGjUq00YBrMpaotNASbSPr+zAbDkvmIzpC0VJRNbeMoDWz0gpq18Wg6SOxSHO44Vd3EiCGL1CdbMA+kUa2OSCyFzMNL0zjQIqphih4cUcawmVckfANQpTv4NYVvcFu+SxUCzVJHBbdK7xhR8tzJgyTlcg20BvM69GrgYN8I56Q6E/c6iWsxkupnm83CxRC3wSiNbI5cFNP2B4ExB6BZ21wBdpuCDiJvuO6ZoaLt+sIWCZkbOuYm0nz92ai3SH6zqHDOiG/dZkGbetu2K31bMkMEDKCoJmazcYWtPa7J3Yi7wNE9K8fd4lsj5SFGE6A8JtmxXUdM9K5B1Ej7R3BxRnT4PyRVummlur4+HOkW6OVgh+M/G0AiPGQtdGBkDcek+Q3zd1AywdzAgxVjL6at9tgIfROODIIaHU6qWmoFVD0ZK8jF+xi9/zvE9kL1xqpuMGaTe1TfX77uVNwVBQw96Q4FnbN8AOL3o3IojJNGJbEX92pHkbprXbTowqsk4MIOI31bmdhlkRyjAGEJUIki41g4kli3esb3bxc2WMbnCOz/s4VHMnO3mcEPgGwwJLHNuDlrmAjk5/TuC5nHAWFEiTaYEvde7Rt/3fh0BVG8aw7flB30or91NZpDv9nT6tLiblIkaPz8GCmAxGO8dSgzabiELZ9ysU2chWNF0Qyu69MijYmJYPTqb3Z+r3pNMCUokd+Jld5Ys3J7jMxBp+oZse1zxt/QcO9l7QbVvqOtJdqUHa+V8anL0H5f3KfVoA60gOjA3b3lwNCLIGBtaKwKnq3Oy3BDRdggwFEXE+S5sffLgPlz6YIv7GCBHX3fWyXxau6od6JL3E7Knz4iavNfq7rNqxD2Csb4izdpWe40n018UrlPDjaCdy1ryPQfzsaFMF7d/+o3NlmBgXjydhh5Xw45k6HNpecghGxHUryiDkK+mYvhNVaiulCM4KXbfc07ISnwWAXe3wz2jPmC4/HwtMBzSudMkfj+QitE5n8v+Mvb77yzZCLXi4aDaajbp6fVlFbqidGWraG5Hrf3eo3zKOGSBTPrYDvgTX9ss98IU5KySRKQtGtQH6adbJfh2M2/mAWuM2TmkmG6mH7+fd0E80AdvpGI7TluDBEbD2PopV39u4WyEs//wKyvjjhOuFCeKaSrIOq2YT03wIxLj7dNhagppvoN26OwkW30vI/kNIyieQxo2f55ZRCH2F8GpDlCYuvmrYgM0yOwZG1UdJWlDqfNUbGbvAoiG6HzslntsBctxylF9s4tggLOU4ajIL9YG98YkUwHN6SNFce0J4mAu0gPF5WFnEQqZuFx1uSGXdUe+xMjwkHR0h8n241azrMWdE+H4mf1tgnDXkhmGGVhYG4Ubn1LF2rzkU/ZnIdgvL5TbixMmzWLtLdaz0mzgDE8jX2stkOFfcsjY2EbbXOQof09EFOlhT7mYJOqSRjz/3KbbNe0gUp/zeOxcjMhWi25pkC+T27euIIpch1YYLGkxGcriUGj/e1ZIKkMqs2ijwHPWWydeQowkNiQkvomc/A7IPw8aifGx/tNS1NtTqb8fOVubtC+XIhK7EVRUjRcBA0F/n3TvdJMVFaalZaAQk3y3GjeeycPuvR/3kkAZZU2NmEkb+qnrGQZMvNZKnjS4qsB9iw2dfEC6PBZMj0RSrGQcmPd4QnjUv9l4OdgdAKvGP66wdMnKcPE8O3UK41QQwNFXfeob+zWwRUsgfUacTXdV1fqKiKKdF/PliKke7CJ5RqK6tf9Q2gczpnWEfVIXYlrQLYBKSABnbzNLilt5ch1C9sg8OdX5xeAJz6uqyJxBSKe5zrgQT7PbIzLWWYmLLN4XhzVirwRvG+XjZAN9iJz9SmxSUOxVzZ+xIosB8/UX93Rz39U92a6QSTxBcKmSlXBJU9ctOgVRJ1oh9xSbM4rMzMutwbzOlmB3xNqHIHFyCbTbdoD1diE2/hr+FRmOs1dKj80/63ZDljr9uT0LAJJfHZQ7wNbHrcAPIacVq+gkK10/4giptAtMDEf7+cxNqqX9rGtzBtTWPWFx8Sc2GFg2sg1R1p/mwz7GthcAVwd3tK8hd+V+GXrRqaHM5Ms6UZ8rRfZSMceFnCiGOH9XWghsYuhK8wX+nI3zUzM71TaqMeaPTVA1rUmXJ+dJ7u8QFTwLbTSh05NUxow2OzD2kO2j7vA9LxHdSY/AXYdQMzHs5UuXbQRT9cQweLKTRm2o7SU6kIRvVi6kP11MjzwgqNXhjGYaQJu6Dj9wD7imZAwjq1+LD87mPeLlSsfnf4xrkn1RgRy5KoTi7W05N0HVjEpS9+m3GlDANoNpJTutpQx1dE6voI21G8FZ8a0Y/NfTqGKjFc96wnH/4KSFzf/0eheKVIkdiN92E3aqT5Wd5AEgWrxNx4XGepXdfZsggekPusS/JJ6/V0tfIvvS8VFmRcle+RGJedAVykVrV2+81Ccco2gPma0IRfu4L1TpML9za6S6NdWb1ciI1HpaL9//Dd54mCZquDOc4MXdmg3dAX4RC3ayPcB8bEuXfw581Dx9aJglNIMx7s3w7nnGp6er8W0r78FijQu3DODqouJTeoTkNAVWhe1JFA3OvuNY9RqlneEexjFMwxkc7YRaV0WyF4Wg8Q0mG/2fH7nktBX1FCZT0oghZqSuv2xOQeoAyRUfLBDARS+84kjdtLmVYM9fXnkAvMX6heF5HiFhHZ0G8ta1GiwJ92NAxgCodc3czybpUJy3fDsuTVTw9fiTpNEgDz/W9MviXKM7pzWeDlgAJ1mRodIW8ALtb1Jv4vfC1draFN4/fYIs/63RJR4BWWONOqwZoa4qq+gSWfebKoLqQ7Mj2W187H2sD8pQd9+wxhbU0njjXnNLeT+4iiytpLG4WwHYlYTbCc8m3STAV6yBMREOPz+HVTnfYD5WvqaiP6Ln5Qf3+g7FqqszYSRYM1n4syaIOYJb5boQS4T1XVvEfaGnnuKBvOGKQe8Zecpd/O3QVJqz+s0P1zU5F7iDg9jQYjhxvFl93v1aqpU+NveGSkqm7M3c10yO0PcyoIEE8Y2mIGmVuvklprGxG0fmFEHYAtmVHw2mOntg9kJf2SKRc1zI2kn/WJ+TSEVDWUt9GjlMnO+l0tC3KQslcDjrTBNBzVqato8fvABu2Qp/j348/iv0VSURkJupaUAP0vXD5jVoOnVVuh36tbtpvQcfWh/yRLM6evBilCIONaP1iLgP1D+EBnuvOQfbcsnC9UBSEJlFMqIV9/Z37WSjaxWvMRKEBtMqXWYXmCUA9YCXRc25vnzG38otwGti7QX/sQvs0TaVbI3W1NCn9JiDu0qjQyCDYEWZXdCje4z7xj+Y6GLktlxlhasIp0/ERhtxXSpVY0CfTUa85xMG8Mhge+kq21WlCSjVdai+dLfZ7UFmzpM8Ae89BVzRa/78mcaPfa8PO8MnlberRdE/R7r+Q84H8Yav+Kuu5c1aNGjSFlhz69dOaGLPUH5pLd7n5Vc0EsEHsGAjjyVUBZDvrC/lfPK71wuFF4KnqHVCdt+TJIECB+LOFAZUnADpUXOlbDJv4DrGY8A0gnnbqyP81iO7b74xHcGetX+mAkEmH6lDIM33EUoillVJdvWV9kLl0aSlHAw99rsJ/BQ9N9dgicvhTSHBIMgDJUdSd4v7HvduMcqLCu84y5umkyDgO0JujuHaJpD2qEz1MBHauEC62wZIgrmG7COpbI/p7OlGJ00TpJDBwEynfeA+vt07+pSD6Lp9WA+hlTMqMMqi8aWn1fv500rC2I30mCdmNhQb3lhMQoikhJGsFz5i1ShYBJeZk5bRyXKHPqPF2Jq+JUDrkdZugkRU1m+rPekxaUYFcd5I1zRIZa9c4aBAFeNHuHn4XjVpxHXPyuLIAlhKFRIa42x9iimcbf/za27J8UBNQqaVG7NSDODPMBYyg+tyxlNdM29Ysv+LMPLJJzg7s1ZtDIyzqGOiv7+5+qWqY8j0TZXBVej6mX9w+UelKHz2n5+4q4cCtrav4Cf7d0ucnQujqPXdS6Dv3vc+RThx7OkuxDfSvgnu7NIFbk+yG1kWWGqRirjzrbTmMm2mQGHTrVXBUN6YBcrY2y2EsZKo+y7EnnvbuvKYp8XyC5uzbksG4Ezncj+8KIYvb18mRF4iMoDL3Lv49v2NvZ01umQ3eCdKpqNBNz/cqMm2xtcM+4DjpHUohpmDI4rhW8MXcyV4N5OJvi/YWTk+ctcrKouIgDbuUUWX4//rImyqQ0qrBDUTdf6tvX0T/sSOA8IQ9KEU3hVJ2ZuWma8yQxbgu8e8qhr1sV2MPgcf3oXgA+RU4LRWk3yhN8uZkYq6Wm35yIsFudub8IcvbwXBu1dQK+a6tmULPyvoKS4H1WSs4AXpbTaoGseWkNT6a3y/aql8/uMPhy1oPZF4Jhpn0NujtH3BrOwhH3yv5vfevdXXJ8PaYnBpJO4KdIYr5lYfdElOAYV5ZZYzsl7BNd4PfObBlYCz6Ca5mZjLscMHjWKxsa2tNT7r2qMgbH9xoGTojfiwJgr6xfTxzOarFb/XQWKqX4ISGZxsDRvKxwzaLUEZ9mzECPPqdIXkbsFzl5Wjl6Jb6o4WTWxcYzHsoCR5/zcsKkISM/XP+HfIt+uSVRQTX29oK0XBhztYl5RWK99VK/sdUJu3xMZb7E8KRcyE4NXegoqnmcsqppiuwj/of1RS+XzT8Le//HmR7AIA3PoTBgdrGKCMSeuwrcgtZCKo7UB9pQUgVlBLmMWl1oSzEGUYcDNF0yIdWKU30RIbldVTxJ+xoq46gnR91OZTjj0w1aM/odJ1t1JAJhN3Uv5OfDqQu5r728QzN9RNxnQxnapVPikh2XZhrQiW3uZtlAsp9PQEZF+v4HMBmyMs3Sh5KI3+AJ5lHavUzMaFd7GjWw3XrwiX9/8cOFgCK0kCbckRf2yaHcKV5+t7h/DF2t0NMNBUDtMDG1r1E5jsDWGMAaw+nvm/DcS978zWt2rDo5VcCvKLiVTaNIjZXQW5AD9p9TCKy2IK+OOreyk1j00YdgoIX5cxp4ohlo93GOKtpyuKEv2CMBpCj2OaWzQp5LYwmbDGhJTol176tINQpAEdgaVXG6DYnYR13wo7MbMDRiCqmtjtGow834NSUVqVMmhD9ioF1C1f8f0fgTBklvFWeKZtrc+jVRQf06nzV1MSQ1Z9MsxvSDQNIe+rrXGOrI7yDaW5AEUKDMaRA34ORnCI516KnXmcrpCwzgtOl4WS0ro0vwSig0SgOkA3jvQdXCYW5HvpnPErW/uWligGQs8hqbddqElD4GOuoGXbvbDoAUsgMMtMn8qubHlq7Iq/ApOm5CaXhIc9scViYhFp9PSpjx7lzVs2Y4j8jkrKRcnwVhKiswG84SwKp9b6wts1R5pMlcJFEr1I4sZikHd+hrbrjTmbHZb/dkYHypmDra8Wxsg0eBMwfBZVKaG28gODLoe7gazx7cN0n/IIwgg2YnqCiYmo27Tf69XaCMypIvoLRQz09cz7UE+WOIa43zs/x48I5dXBVzlbn2NNCV1MYge1FCvSJ6WQbU3EnQq3RnGrtyX+Fu8L3xJtQhYEd5Zi2edpZl6yjexa6NIJFJ6pmF3JWuPHzDJ0KBoWow9WLRgCHDeMcJNtx9ELjGdnbRwlbPzVkQAYun1kvv9SYBioL1CzPr+/4HfRbFR4h0+loy6Sb7ztp1VOr99wo3M/ZVlvhmXhpg3G7TDwolVC4ysrcgfG6sskaht5Be6mezxQhDC9pLp3Nau8oMikYYZqc5Ba4OudX6MhkZQXtTsXXYRHvSJzmVc1G+K88g3LT1CRRVS7eFE9jv5Pezbq8o3oycMIZoJP8vYG3eyJsZ2YVbx+q3sOnb4XpGc+YDjrD9nnmGrmFLYog70RkiuNkL6z8aXG9Yg7HLtiB2tEe2WjqKynVC40ynTlgzgZ1aWsFhZj7T99KUGWwVLCcBIxgiIXAWMTPvUmgvNTDKVvWJx3qlmv8y5LwMUeew1ptD4qeAaZGdML4Q2ZvdConmLNie1mel1RP2BKLVE4PL91xfOcVWFtxjnyFtGzeWsl0nYKTlGRSzdrHKEZTjutCHcXquVB9m2X2LiOqY3c00MO7vw81X9nYQpVB82eguymJAbY/PR+NurRnUExrFzcyTk7fSjyZM4JE9buWeXrpEHiclScwoUb/IP5OYC9Cu/ZLyTKw0jQUv0ia4CJcTmXr8hM4ikQyikssJYvWzBxOo+OUMGCblFHHRCOAWtRHMf37FOZ6AdazEguqWjtbm+ecygWxTfapoZz88S1XBY4FbI488DveEwBBNn6MLtWxghRKXpNShBsfKLwPnS8mV/5Lo3m3wpzgpqJRQy6M0ooiOxnZlEA/bf5ikFaXAggA/+7uI96iZLvW2vPHdPfoA8H3WQy4jDwHTcTfMOPtF2aUrfgzyg/Xdoi/RizbGragX64Q9BVTWmXzR1zWuNyGwSMOp8cTF6RlXT6NzCVnFq3MQdiNWMEu4xpKf5bbdFWFlYupM+cKFf9HWH+/FQGwbo5iZIaOBWHyFH3X93bYzUimxwtZHBmGK9fUOyIpAL3W39chpJPNrYbzlYfJ8wGIpkd1KzNn8XSkGsL1bEmmMuvIO/oi06OgBOV1GVxukafpdDQL2w/LUZt1pOkkrNnNkg5BQPRldS7VYejuLSdvWsZct6le3X3IbICYkapjDvCdlBgXeg42BuL5UXYQi2dqjT1N8MPd4r+ntIAFlKfhUVlLzoOwjYc9zYxrEHZOxCvjn//TqKJEZb6Y3/iHTTcghHmAV5+AcR1PQNUOxfi/ui386hdJCSt5jc0QAXldw+2CpI8XlkIKmatxoU+W0r1t4gjkk9ag1a2NRStQfhUz3hXMfOXjU03NGaXPbtaXPlVk7DNPRFm/41CanzfCsjqbkWrDp56P9RkQX+gNy+e6D7tcE+1EtXEp5qhe1I0FEEEus6A69SQKJv1warkdOWSFBkD/UAJ4230qU9FUEwDnzhI2xgKICg54LcfLHF8vy0wC9F/LvUMMIjNJRHrLM8LKeH0qFUQKmKCXz2500cz6D8+yo7F24Z5bgcBOde7f946HjqkNF/9BdNsvJKhsU8QQRaQgsnoW9xhbYOSfJakjwu06mjs+Gze04txGXQir8/AVDyl8PF7QeaRzx8eRDN1643uuK241Cz1gbvWTKtgXz5NQi11uMIlyzj3XMq21iW/uAy28LiFmMYsB0I7rOd5reHBx9wnAWjeplfDu5zdCfaK7x/7/xfgHqY4+8RKLgB0224tZnh8bX/hh3wcGPo67KUZVJsRHNQ4w5jK73b7b/icLT4/rcnes9RssBa+CxEXemDqBbiyu8p4MyMbY4Yv8P5Z004jnKofYqQ6cG6OZC0C3rbKfiNaBT8kS3tkUYfO/Ajo6uGzpg38ALw4t5WZLZUysLmlYTa9o/ZrFXMxU7h7Nk0WcrqywAm44RtqIMLXOdHd8QcknhwfrcuLJlFClszdCuNMDmmduSGy64DQk1Q6c1hAxD6t4i0PZ+Kl02wNqZ72cYcBBfQp84lkciyJa66lLcAwWTon2N5I8V3/RLhavKcd2IZnns2wIJYX8A6Ncxee0/L0C/zQ+4dDEkGxcFUk2+voJF+n7PfNgXE0iQJpVPPdtQmCMdingo+9Njh+pun4Ab93ll76jqnwlNjEYXqHpxh1UdN+TsZ15z/aZL7U29uLk4h/UM/3KBkVqL7UzgFgjd2AZPq68TlJMPmikupHTl7SOGTrmLZHlaVQTlQ3vTpFhvcRszfXTmoscyYGWhIsTIHBgbY45e2Xx++qSXGis9j9KySrluDyq7znd0zPc6TOGVdCOOkMAyHeuj6SDED6TLs/XlXRWVQ7spJdQeLR/FzNEgEfGg7mf8ShDgifl3u8NJpmnMnievnuB4Z9nX0p76vXr+7uBfQ3D40gB+GHk5MlaPNJ1TvaqCcOZkxTk9Fd1HhifB7qp6DDUs+KIsmiWlEncxoT5bxD8nbCZa2V7aCbSfAuP34WYpbqcjlpdfVCGUjtH15X8x8+Nhh+ChDunefrbvndsi3JIlKxRJ+hNsrBNqA9cb3eVdSpMntsgvFAW6eTSTUXE7fnC9o5ZmOwaJ4lSyxfm54yF4JRt+PdpvkRrfLrLlSZeO7XALY7O5S3mwaIooYrfH12n6YJCYlfGBVivyPSAdFU/hrMBSY6GMm0e7bUSo1LAWXuVLXJNh1/Lfzkz2Oq0w0J/MQ3bEgiGITr9t+Tin3DVCSsOb7zxSTw7NWrQQeQuPDt6XgewgVZYXnLd0p1p8mgyrHPBuK7UgqsTQT6eYbXPuprCrEq8s371KS78+jQzHO47kBbb8dB1vFzdv5+Y+qIIA9Sl4kmkQ5dKuHGpNb4mBqa5fMPhEn5iU9Y/fTi0wmYSTbiDySPw2tZPlhcxq7nWsInhF/qjRTdG9+ABcCSeyaC0HS9nr52rwTHdPS7+vhaPFkI1ETgUZOiRGHteEwr8P+eEvUI2AH7v4getM0zuKbOamnliIA/Hsy4h6JduDF4p9oYP8JVK+FfKBgpOTJ+EJ9HoAYlbhjYpDGLQ2DgKijrdm772i45qUlQ+kZ9DbUibFU6QYM1cMeAvBBCqN4MFpm2iY3CHXXpUJGyKS2m36U+E1gghLMP9ssNwaLD/9z12SWoKDC5vGL6j82JW57gfBaovKEnRvrisnCV9hKpoBQNXPbfYhZh9CsutqWyFcSI+CaOaEcreNTP07m2DJj3bOPjJ+XN6tdFQWSKosfz117NEWIGF/1G/kw4akINQHDN2XGETcYhJkOrNdgNrwSQEeBDF0ocpIjkSHXBiSTTETdpZa9YbN6Drpr4uArpci6+w5X6rb/dOlsa8AUIebhSmHI46U9RbMHSIk0Un75GaJoQy6VLHILGyyIc7ryQD1N7p2EjHwhj6Yr9Ww82yTIVjB/iH2CLbBL9RIFgNC6uSFgyMy6a9f8FyHqh9+Lf8YuQMGfM3jTNKttol6xuhf6lOi3EqCIMojWZo3feCwCfGOCaWcKnfw7vSqIMwtSeovfv6j/VMcdsZZP9pKUHc2z9vSCouPXi9T/BIcdm5bs2tyA0LB5TGJYJNebFaJYPNH0S3I3s7fWk/I5WD6YGrok9iXLoKgBKsHmoq37TcdFSB730CBaDeWa3JytW0pYNfFtYbbH+dNAqhM/IXZSl0by83vG/JkmXj1nPCx3YbvSnjkQM3ppQm3qM/OLL1DT8HSl1e3RSeUPe8tCdJ4rG85nLbdm0NHwphL39sXaLqyE9+Xd/aynNvzxXOxVJPeVPGFxv+LwDOmFCyBbCeW0/nZXdpaLDn676i2tCk9s/pOTV6/7NEsBmjFdathhuFc/smZ9hI5qLc+L9/2LoZ7J8Ozb35uiRN9DQ1JEaDfNXnqGf8cQK4DwMNpHtrRzTWv3TWEw8a+9SyWuHE/DYWJemGJG/0V7XNujPo2HN2Zq/yDjhPC3QqdT7cXPCTzFQefk8uzcpmBnUZsUrCiPYN+3nfiGrewFSXtgwXyzIdrAeaRcmQwFjk8in6E+vL4jmFxB2SwOR3Kwgz7IDpUUM9NzXJYzSeWbGyKTtiY6845IRC7EqMcdI5QRL3KYK5m54fkBjpHUb7+ZTFegVwY/SLiGMndBfE/QbZYld+/nuXFVghiqg6u26KQpFViuD+ti/epqVvKxUPomDCN0EwVHcC1eJ40jxyDklcP2/GnWOd6mQ/PcDuY7ortkQmVjvSqZLBj+rXAEGgXq6si2Gwl0K5bJTMNl4r6ulGk2wSxrze9qvtpxc9fMSHVqK1UF5AkNVoo8twgCWLxo+/TPz9NG/5WctMn7Tz+Hq7AbwEgWsmNis/fQEts1jHOI85ZyIuKEfihbfqZdi/vmig33j9oOIXTpSkG5Dy88vUyLYBZxb6vOSChd7nJ85uSjqwGFOn752Nf92fnXCZvAMaYoGzfN7SOnU7YXLtJi/t7EmHpqMO79oapK39kNkcg0iztAHF+H05R3Ofa1ntcy3UN2+qSkrkFH7doOas86DyocDgr5xvMHaja7l3tBoTlSoeujZd4pNQtu7k7/soQJyGauXJQuJANuWExl5R6NWCWTghyaDI/VwtrLYJ4oQbG+Fh0ba6euzXkIOeZTIh1Ido5CxGILL5lmoW43jeJW3IFA/Q43vcUzmNpuEXH5vT2HiGvTbdt4Al1rJfmtDItI2vpGw5Bz2lz/Wpn92fQg4HARnFUKECPnAC9T+abHVPuzLenIb2Cq0PQa7mg1XKq4Ei93Uk/3ddQepl0BFUbZs+XxO6DhnMNqn2jL23ZpunXHodEUvbCpGTu56T5Ojjg/Rl6Z7wmRNIs07/nDDlxCyuU4XhaEJ0KHv+12ul2XlkFLTFqGAoR1fm80CnQA7fqDanzGzKbj9/p4z/M16V7Tr8Hu5HKZZav6TcyEhw6BnDmSc4nBMWobWqstcA9Yr7XnsaN7aIOeTIm9Tq3GlA3E/QAEiHzDJ0O7LY8/lJEsdtcQpBm67FyadnhZoRoGxh9bGEcQ+RUaaOMp0uslbOTAJMzlQrTXQSC9ZW/w4H+9iIy81hBk+mJv3hiWEfzoIk1GyEuBtkMzEy7bR66hz2L+TvA1lv+1qkoUeLlgoq6CmImJxLy7u0MlEuZFNty1InFmw2W6GfqM/ghd+r5QeRuLvN+zPaENdrI/fYys0DjMVlx+OdF1It1C7XPcjZtDpVSOE+Zt97PgS0MJANHgHGySFhD7hUqU0pJ+brri8r48KKik7snr8TRALRXj7MIkXNnzve3L9zbI0sLvXpHm973Sd27XbYQah6hZ4qzPsWVX1Cq9se+JFXGAnAMCuU6YH44oz3mRde52VZnLZk8qRLlkoKv78TsMEOmKhpRYaF8amlmcNj5PkPxGQ0YGpySOqLq8UeLkiC7QHtKjOfes7hmxzV2aaaJjyOA0pfurhIvER3JB7djq4p00Dz5alOKZWhRvqyMQo0+sdK6QoUyzUovRtsyG7PJDCHUuIEn7ZXS0cKNBfYUIddiCR0speKhxhs6KCHHwM9Ketj0T3balM3CRyHWR/JggQA6ri2znCCpfYyH6Jyvj1hekI5PJxR9/o/vk5O8719bDxp9iJQ8dCUnqam4zleevdIsnPjdT63Bsr4fwbkRGctp+q76xKdecAcMUazonm+t/m0cWOoIC0DityoArXbHZArpeeD615t0GUnfd2J9N6fmfRr/Ldpm80QMmE4dHXrv6DbsUZitwLf/3Gx5++8mY9176x7isLfz5cgu1gRpsjESdsirFaCaqt0KkjXz6BJNI3XYkppifXBNamRUMAnzhmrzLON1Gg2S1FNPg44F4LdDwk8nwOvvONNd8XP48H/ZIWD+1vsliEJjgH6LFbaQStgyseIJPqLMAfyCThn79LDrP1D5nfnuukaIy82JQ4Focxe3KHhZfsSO5UpEwc3hXvoQuvWOtGb7EKL8RawX4LDTTcR3CkdRxKXsivHdHEWplsUn94fiJQy595xKb9bStTBHgUdGyPFYhsagQUxp4JIkttxXaCeVTRIAtYXLLC29coBUmG4C8+e8aDfr2CMjS7lKFatiTVgR8otST+/z/IUAA0KTEw8KOZsV+zrNfH3VGLGpca6Fl63dUwbfhpUV9PlXMmTMItQqirAKL7iMQDNaXOjF6OJQXX/pupbLzEN6Y6eE9O+CQfnAU44pDLe7KwBG8XbukvZttzTDQWv2y0LZGwSGFGNJx5F5x8zPs0BhTA8zqofy9MsIEEXYJ+gLZqy3JaHdFKlAQhoh7ZNYwpQkENdtueceggOMGIeVjAaZtWodY5h1pzFFtOt/cufjLONLbiAj0xg+Gg+XaL45+rT2lpx9TUOVuKQuAnquWpkdA0Z/yFB1gT2FlSKigTamuCZ5KWMHA7BykSKABxtRXKf/W+ql2NXXCXSMRPjWn//hf9/SUifXAVpHm1wP7ngM3PsCubCnaH+mYQQn3R6jkLnHILji2atJ9M93kX5MrBO/lVCJcBUKp99ovfXKNSe8+C1jAjJw88diUOi1p/JnE5VxugbDZinjDJTTTZ6wFfFR0i5FdRt9LxVjDWdG+DE3E3/YtsH4+Qx27jR1g1Z4QIzG7KbrzM6Jb1mcLKuqvDzv+FVl553ePNt/mBj0eyCdEpFVQufnXqJdG2XkjdIbzySJx3pKhJ5SaQPbc6sWq2GSgcF7zRL/MIBG0DmOql/YBuXy/Du/uygN3wQKtefuaINnGvtzEtvgSwoiEknaQ7w9KQbdDopk8iXFJ8JSg07GAwaQbTF32J0K/DHuNbhSx0o6QJLeoBt6Sxn5eKy9nFX0SfOVyDmVe3rhVJJbrLtfEtIW+Eyab8dbzsJ9SqizgQ2+d4vCqw74HEQf/PVpVTENcdUolq9eAWlNql8G3rLOsh0fkV/+UMdeRwpuC9WK6OQYEKx0vjgixss4Lb9kPZviW3lUDdcoD6pz3NL8DzLKX7lhhRCZBbMjNgcl/bxihGSAY0hKIORFvCXOqlmu8ncqmzmXXExzoimm18bFO9uk3WfUzAmCYyuAs2sTXO8SMC33kB8BsavH7vHBJcb2i+shDsHPNQCkmLVeMu3glJ7XqY3wT/CGdIGHSr+VhHtAft0z0MEaqqEVi83BIcHb2pxYtqDIMPsWw0qpaovEimS5LSVcgYgY3JiyJ3axR2j+WBq+/s7yu66iVGXPSsmZSuN39d4Rg7nc8jjhGj7KVkyVeC/hsywVkLwMnRELrkcTnknG/yx/gcQK7kKR00tfOQOSVYQWeoWo9DWr5xAN5jvkjd8usmEfPz54aUH0mWkX7UpF+PjJJPZp9A6SR8Rk8+pzhD1dixrkziv6IzYg/ImoE2hLiIsSwc3lq6+G4RSqBUxYD1XaA4P+y1gWfoCYuS1KNN3JDEnASTceHj5MO0d6GfZmewpLDLeMXjkXEgQ3khCHt56ykKEkkF6Kw0tc437JQ6PQs5l58DGVMWBdkmIBVW7NCu6bhIiJ5WVdo2q5mmj0n6ag1Gc0Gg1g2PqzwJMH+oINgBIo+RL7xMHowMRP+TrHcGtoDnsmh7HFEu3IAhxYzyZoAZNj4xoZha5Jj7HLEnx6/OVLMW2XRv+2K5NDYhmdmBVncd6Rq27lbDp+iRpE42+heFFqukOW3sLb+v52U5jrdCtKFPkogHM/23s3uCxv7e1WqDj94/50+T14FbJuIO4FbOWtJcN7gS/fTpV3b8Js7ImNEgl8VH2U4psqsCapN6cU+cF5UaSX44yL16ntnr9ryYur7RPBzKSGB3vbWMgnUAZrqP1h0m7VmRZsoBAPtlbFkOBzkA+eGMM5P4zqO2GRjfseufe8RU57oEG+wDlBLFrPaZy0qbvb2Sw3kR2X19lkmTv88O3qvf+AsB1Zo38sTUNJ4XAk4VVazIyqrekQiqnQTd/WqvJxQ/P3OWVoEKIxCHarryk+PieGEUXpJLkGeKJG0qRX+OVKKIXlR13qwOrhkrycACsB4Us+0NZ7EN80qxL8AhoiqWWFJnGjZfCNGOpfYMkTWvXYtp7XNaZe2i9GKDP0Sw7zQPpcLFF5TLYIyaX1Faf7GAhSBpTF6p+2P4SGgmfOrDv5MrfetRbcMWXfd7uldUUcy8pawQHKqB7+JBEXWPcxcKm/beEnwb7offC9b5KbdjcKYzHiR/PJGurW2/MvglKCSY41vf0eeqemOeIx1w/EbuxdK1WHRmffsIv0ycNQxhkHZ+XNoZiMrQtkW7xnKB2VHY98XdM6TxxaXpMBcz6l4B8e6MtnTuozGbOi+mRCB95M8TK8bvxmEXPf5B1kXmCtlHhNz5tWzbgQynovx8HFo7lkWSxyyZN4WB4URZor9sI1jSSCe7G6Ld1xICgi5foFeRSa7404U243fCUjO05yDqUoJXQPWMijU3V9k78pG4Lw0XsBkOAqpsELnXeAp8siLOC0jJPRXfXb/G1APYQK04t/TwSwLF1UI+Xjimj2mkwrELtUnXlecO2TaG5DQ0pB04a1u9Bxc6Z5keC2x3EUTji2W+5Eu+w4dPamg9Rk+bBZiugS0hfN4XZaUfSdYUTlCFP4qzVW/iyeOkFZys01Mn6fVF8uCt5ptpLijX6383wJa5z3Nap15kDplxq6e5YGPW6mChKEtV//DSvtN3vetioRZy7WlWj6pWqGPhHt1EV9YuyDOWs9XxTW53JWuBjAc+aKenU7Dl/ESBZUbkqGxd9GPCaFJkiwoTG4QnQULNav8KbYav5Gwo+kb/o9xXlD7CqoA10nENhvmvx55lKP060yu/jakEqgDsceqw3pBotflDw4KVRLFtJERaTxgDqVAGpb9kX8XrKVVN9gSNVDqNxA/PPdDik7Nd4RGP67AGJG2oS5a6iEwAMPf90vqXr0N+ti+/RFg7r7wbyV39YoVf1tExN+GbH7IVyo+FpXjxqLH6rU90yjsBegtWzMk0eFoExsUvqWZHcGquw15RX0TzNvUJjEE+n+fkjCqKcB4XM6zkcuAj0kZHxAAre3RwvjbrLISZLRK4EQIbcQs4y8gM0vn4pAl1nGoaJ7keTpHwP15+EJ0aoA43MVydmBbsamlsmRY7g/29411DRJinyaxg6j70pN15R/ZNAbGUmqMkZkaukfZuwbhEnTQfqF6Wvsv+IUrZPPqu0yzXwCB8MK0wAiadn27x1JCRjOVCcP63vLVqcRMrhM5Fu18F+Fk05mdFeOTHwNjbEoqJSvSuWH/JJGNxvHUlwUYOLokWYsJQqXQUdQO/7cu+RUrH/XvngdFFneV5Cu+VdjOxAsI+iNVgiwn5Y+S+OvHrKbI+67Pqxe+IiWKg3R3b2aEvKk1ycnuME3jxHv+th+d2BMgruKHoMh2pegZhPoXCPDFo8RYfPk0vFRyTCrGX9c7AD8EbIZrR/GT6duXfqDrv5sfmb1kmPG7pJwpr1hVx5GQSHgqd4JuTfIOmpDLKlMmwadrfbl8jkQcWKo4bJJUu44RhknPawjKGanHEQYNuSKAHEQpPfkSewdj9qC3Lgidb0audcy+9W9IFHOa8yuaUmsVFSXYDpWXZNAEsUDfDId5YgpkNR7gkMipZOo05vfbk9NqF/m2hGvf+EmhQ36NnDb/BZtN/SOKyOcXJ3Oc6lJfBIRFm58HqeZ06t3NTu6sshWO+zrCo0KzswGL/rtUh5jpE5m0u7+/zjhZCBvY0RpeQU+rQVQH27TdMpjQ7CtUDtzjGTwqI/v+4v9oMIlUe6WUp0DZogGEkgWdWPOtSoGMRjOK5y8FLv7zKEyLEhOgRJaQU/2fRlin9pPWeHzWfDJky2nYFGQotRCXBAKmtRDf9JvaCaSphNdRD63OvyrCL1DIz3fnk5uUQqs+Gr1cE6m5rakgCBOnuEnuOzCcbxi85xcKdXL2/EPgQQJNavZ71mMEOqYhluXavYEMpYsKxR+AX2HzlWvOTznQ0dbyxg8YSQ+l18/BwLAvpiQS2qr73jPKc36lh1i+lOnWr7k39Jy1GNB5TMqi+oc8yzZ6ZxBWBqQ6fWIGyeiJgecEiYGtXTo95o3RZrw69ScoyWWs8SPQjl451bITDkzgT9QR7stXSlOBL3wtF2feXVWDyqNYZF0uXjej27qNSG8v6/oxu5LvLOxJguNr3o3Ny5K/ba+J0bWCC98R5qRZ+AYMdlv0Qr5egrC8zTMQCy38r6mST5SXBmf0jld98wR2g02fYZ8FY5vpplsxuc6PWRUxc+1UEqKeuU7CTYpYa5/8uEBZkI8V5+PLxFMn4wk5VOWZwquyxAWrW8yd6fp4UHfMqihhRy4Hl2vnnQjS65ugdAGlA1bY/Ib7IlSN59/2RxJcJiPzB0TurTH3ZReSKjQo4v2+YB2QDuecwA7c5RoKWHpZ5SB9mTHupp2FtPghy6S9H2FhQomA4ae9+P6p1bc6PKbzPzA8n7neWFumInaj+w6BwLUQmy1voGb8McndCTYU5NmB5O1/HlGj5HwQwRomds+Ktj5IpIXp3Fs4uoQpJS9NkbETNOgaykfZv0eoXIIzRV1dy99GiNjirKNkw4CGzH2rSo4o4UE2WPpwpjT/d24xhkI5T6L78yErmnvAxu8YYEaDqZpK1dwaoig2n2o4v4WmY26x0qe6CEjH0fqnG5SfSoswM7jrCU75R2ZXEoRhkUJHtYK3JjFhErvIiaeZnGIVVlfBiA1eLi5SbqP77ErVBKJuB1wknWl0dAKHsGbJPVwFTnqbMKvMPyOIrOAWw+1n2j/3uY1LzsiwnqKhWKt6fqq1nALeVDmk5bmSz/arKLnEt3CmjzVu7vmY6HXYIFWgDg6UsEpuzqnJOyV9lJ4n4v2JiDGpr9kJ2qHpM0GA3bziApOC71/liLCOHxKlKNPP3Gq1Wu8R6Hvzz9YpSVWTUnbCpzz8nPsCvX49225RSO4+RI+/3aH2YIiJkPGtV/Cql2ZjbiOzEyy27ooecpsrO3yya+400l8bjugn/HhrnvxWJSLKAdg7M5H9T4cVLGRR6XvI/9XqFBHY5T8CqEmRj7DYVhTN4PTXOVlEsvJLUW2FhtrqMhjRv6bcYcJZeNYwCQ/QxXjYXE9fmYi1qBqP1OfYh5B/S5b59zFIM6/D3/BbopZPm/XuD+zYSR4FTbDhL39bvkxJCgckdbxGVDN4emlkpfUJtDpy0q+PV8Hvq+pIEn3lOVYDU6LlnDHECw2XdWvjRPVZvj8DTySUBSSnQJ0QGay5WxW9Gr1SRhVH35qR9hLCzX2ImE0r29dqqZpiNoOfIRGn4cRpnzgbVBSiff4ZIh8VhOVbgNuATzuRskdAnfJjRfRuRWFrB6+vgAmwM+kQQNUMZ8Uoj5sS5OIzZzzuBNiWnwa3Y2TLLadav9jWiROd9LQXvZn97qLs8ap8HSYIyOViHW4sTRLddkDCLcmbP+arCK5iVcaaqJVbDjJrj3FKSFEYcTN0CXdZ8TVvZ+Oiqu2wZdvi021oqC5snbw7zNzmiTf1L8Fr/V7KCh29pzLKBdzyKrZWUylXBtZ0xqGwhSi9XI1EO8c6j/Y0zWqENft6Pe3rbsxIDdwE8aJXCkg4IBvhL1lE0KAF3ZtsKmtYWfibOE+WSLilMj5D1f2BQJU7IBjkctE9bf0aLZ7mZiYpyxtTpEQLZr0n1L8v6xxdFn3lHLu31NuyqIYq5/e5QpEI43VPEefT10h1F2K+Q3KDtUeRksGXRZRhFXaVJRqztDvI1pP/4Bb6+LKChz5+2fn8OFbYyAi/TiX/YtyUL0xcUX3PlitIA1iYpdBQiXNLMZ0PsydqBeifTICmRZdFbn47mVQlArCI5xU+b89rA/3yEjgh/sXqAB1Dg7vorytulW0O3w3Ce7CGQjNIRhDWWx/gGxcNr6nFTXtNpnM3Xqr1xrMGB5bkXJ9E5OvTTcGxZHZm4BwGyFSbL0c7a4t2/G8bFnNA7dAjurhUFtdfZiqkfX/4PCxV7zIblRPZLzsn7BPjaPlNRfTFnUpE2QBqTVX7O0n+Q94COx4A+fpElBEO5me5+Skwy/sgwQabfBL7lSiJi0VsgC99CR+aKvkg5X6wAAWFmfKAXok9HljbtWgMoslBMfTxWZ/Y9o0NMP1DXrWZQc+ae/BL3xNCLK0bmBIuF6qyCVlsUUzC49NzASWyGqtdKlrj+JevUteOhidmypy+3jnaQw6cGuVtr/Ke5odC5jT6D5uLIn2XO0c4FhoZJ8wwybdC89SCYgaiRaiFx/YePt+StISD0g5tmBlbBU8WkWW26ayk3v347zMTHYp+ruVTj0EQjLfEYKbw2LNmyhhDp3yETOs7IgiPV7R4AquzYZfDevKrCpbM4GXTuAG40SxbUr0KscdpWrgkYt/C+Ex5TuOEBNPar1UjfnLKqg9OrnRyPoH3e1+BD/NmnmdP+ydAQSzn5fsfLGG3iUczTy1a9EDv5Tr2P3v3jRy2Of6amHjm9rxC98MBaMsP2BUDOFqXuVyqEnZGCNv0P0tVqGTvUjvVBhlFpDprIQ0iovUu1DKcdK2lkSVRGsEyotsv6Ln5KiJWKvepltTAb7sBAZZiwpVkXn9XpmkuzQ07kUKhPgXmukG7UCNs5GSjI3Fw9RJTYw2r0zouoVndJxbYPaBF2XD1zrDvF20wV1EnPLS+HV1R/b/oDm12ZkJaXv+XjW51sjdNHzT+hSWEVBwTJa1mHVU+v4w3DRki/My6Qio4wtXZbg07gWbQ8DJSDvd5Mpcr5trUiU5J8qZrJJpNiapeylh7d86X0mfhVB9oByF1kDdRAHb9+M36MYWHRTOXHeTWZEydFyE+9EYRd83mAPuHsObUy+750VwhtWfU2erjScKAIRcWHylhpcNUhqffb00MtlF+YW+/s+yWXWpTfBRyXbMXXIFkXQSstGxtEuAKeX+LK4cB4c8Pncz1mij/So1AqgSfa1wrMN5G0T4ECFGzvTmQY8jQtU7WkewcKaRRnnlxnt3vGNbKgZlfqZGM5yzNMysGanWL/1Hv+59aOeSBJzYvcPAwq7rbg62AVlC/YPVtJtNdWvS5jxhuIBvET7Dcey4UqpXT7+fjesAU5BM1BWQA23POTZaoNwlqCxB+3cHbnkjaveaA98LEQ04m2+50NX4g6WraTaiI1mlQcwZSc6lsyDDlXNKlYPXWmFKjBTWHbg6M6NtFqRNF0MTN1NeGD+/txeEMONUpsBKd8DLHfM0XitywiDrPDpikucTMQllxygo4UIESRfnbyOmF35kEkTpj+8qxcZqtQoDSxvUsdG62RF73iJ9Md0V38Dvz8JE1Pc6Hcg7yBbtuyiOxUxbNmyggBgJ7Qdprx73b2ULwXPYZZtjxXdlrXUpelqbFTMMlOuUkVBmzYGV19DPXPb7/KUwCvyQS7+vDXAVNJOBFnfn2WT2KMkBaJbrbAoQTiZoYose7gCq7IyqsI/68bndwvNP75uAnTK4SJC51xH+Msw/zvGp/V94kW4UDNEYmLc9d0jG1oLYAxvnykts6hsqRgqYFQ5umGYAhfRnw2cpLue+JyR60+F6Wa2nIoyC3u8zczkSSG+N5CTLgL673WiXkOzYkGzLpCZjxmRy9zfefsFjyYCJ3lwdBX5Ypwum2IHa6+9qMlOiK6svvR8gr/CZTRoLAb40RCEARiQC9QuKgHDqRcjlLkEZNZ2vCaWdb6yh0TtUy+CuJcvaJ1f7FMArE9XF6NslQZFT2NECCnH4Hvtrt3s26aiZYNmxNDRFcgpn+esgdNsSsKqjPX2wL4sZa0557sDqjD+AA3in3E+dpfHetTKsNwfJIIGShryTfF0VLhZpr20i+9dQgO3U7xoHfBgwHIkHhx12eaj3TTH8BT/IvvQL2VdeG1PWxSulVeOF9K2PLXWPTgSswigjN2Khbt4x5o5Kdc+jq+IzAZKdzYyv41obdwptFFcYrKetnccKhFM4LChsiOnmBGwaqzIambtbDTSf8I2IzLUTst0rrZ6V5mHkekmCMHAsHX5Y3v+qDu4q0rAn4gbtPKDXFsxgT0XS7RlZFnUvi+JVvhZ6qXunXwojfym42oHe0+MJ7FZwtNa0iPKNWKwYRkJKdwca7NtBM6f/x9IeRDYKdyR/LR7QvmqLjB3FeoAKXuw7sMSIhl0wJDUt2XFRm8+ieT41GVEVqAg1hVzi2FrGo86sO/nEQ75tYhtA89wAV3cYfetZJy8ww1VQZ7OhYFCuI2l4kRZYQo5iMQAmtNLJ+jbuwHMJeeBCQr479Wn+Vwg1ebpzT0p4kRBFvywDwPVxvvfyRmuNX2sRG8uBH70kTa6yLXcxdDjx24Rsh6t6WPlxF6v1XAZkxRbuI1roSHM+YKSW+lxq829DskurZkWxuoBAxwNOY4skvOFDv2mwRE/2/9h9kejQvFTWtoZnlgU/O9RmQQrdXRMmTfAEC7v05AyPebSbi521AfO4CZqGM0/tmwT7g+p7nmhDc9dpsGhEKkTPr5oOdXOawg8MOT1RErIK6hCXeihww0M4sR9V46DePwv9rUQ8QP12vouYDWKAx7rdf15KGaynzcOBEi/NNcils30+U2LlG9al9IwfmLVEv6/e8JDEEbU9FHauq6/3jdway1Vs8fvXE/93v3AJxYm67XAAUb4DtwEkPZ3x8gz+mhVpYJjDXXvKlY8ySm/FTN9pU1E4ngZRu+UkLD//2dM278iLUKVOBPSXrXjp7yHZx09aGqDruiKYtXrZ9wkJr2pXmupAmH7X2WaLPMFvN2uiX7q+Yw80cqI5whkGXS/YEYXPi0CMCp5QYeL1wt7iN5o7lty1ETXUF4E6yob0enhr7oe04RJ/UqvXWx6GMTZwYoNLLu14lwYrPf8FTBu4SeZS9GecIgaHRnKdpXfPilMHwDnLRwUFSQ2dK4vcLj2ApaoGP7aekNTvL6tXZvDWhiE727CfpRzuSS7DcvN1SKRWPgMh4TMlTPIBbr9yg7tPiHImEQapnWikhRQymnWhKHGYJk8vLvUlcuKiiWOOkdnuva6t7NrGba/kudNNLJal92TDLlR1oCgMQyVoG02MjM+tkzGcWAXhjKmVZLFYPOHTV16Ms5Xuhl4oMSDXOTyD2YaTQxF/yMyysNRAWWIkKcq8DF/DDf/sa7mVNbGQoeJ6a7639yLHLpohcJgg7l89hRI89iycCS/v+alNf4jkIxtQiIx/BYEGSuJuqkp5TCEstOHUulwgJoBjgUfX+iCm5ZLhz/ex8NPX15hAi6V17afUPJmW+sEeBLvBIsVKg1Bd4av96gB0NRxafkq/LXO7uNGoV/XOJ3w3tDpacynWV9Tt828JV8+hi4TqSF3gzqPi2xX3mXmXb2YlZEHAqzAYmhoQod2XWv4tg5tgMTiZLGUDqWFbJbfFjrNL+3T5YWomLYgIa4RYy6TuG/zg/4cs+3EeZ7zaN+y6ekyCIimZSJGnSywakOzrNKrOfI+/p9dd9FUyuNIdj1dx1cZmbrqmq0JiccGOoXDKf3ig+aREno6lYATCKNMUFF234sJkq4NlhXZ2JyPC7zVMPRminnGbc5RaqlMSFFJs2yB//7cYe/2/h2NsrkbgXnjQImD+fXHVfoIGOCwnTmlNrrHH1oI9SBQj5gfup/mrWDCeJzmtKaYo9iKS9coppvA4nN8M9QzEje/SPP8TwTehxPr9+SPaBq0oNGs3BHeUsEFEsynmptmKxhStpVugtXk2o4Yrkli6Hwtt/lHsBLFRGiAbgbGyTHBi4+1L1C3Zf5Rg7lCpG/l2uTZwv3frNThQXk24vdkcLYdjmTOOvTlxplZvcs47vJWO9EICHjymTLuYa8D8YAnTaJ2FIgQnV8FHSRYQkIBNYDry3j0w62jwq3YWv5K3VP69eWyuJIlvHxK/TeUErZmHYDiXWZId3jzx4+2px4PQBawee4VFftiaJCMYjkgn0GWE0qibB2g60nHLp63AafeOVBRlid3kBSkQzsIaftiOwc81QR58it+u5UMXvZ84ujOG6u/4EQC6YeNYb3nMR31dqMHTGYGHTIwT70+YjoDfstzAMD4sPtw5HUI2iwA+gNEBFI6ls8hu7xUWF25wo/a2rNw0pi8kwdbX/4kq1ikmC/eNiC34+w/tY0Gw1DYm1ZgdGh2JqgzpMYWK2Inh3dEqOz2YrSHaBEug9bMNTZK5OLQOWtDMuF+rrrE3Mek5WCMN9uy73Yb1gcPElPV6uc+F9dOZQJJZmP1oV3nzBbn9Ucn/6rev8YZsESOWFXSKhZpjRN0yQx7nzgq1EEeNsvx87Kg5NjleAdU4M+tuUkdQu06VRGPriX9saqjTTsPgjCXLZ0WBwb3bfDp07+KLVLRs4prc/LbFbYXvR8V3KzmrN63mslLm1CwxHg/F6TkGdw4OLNq9ix8IxYVG9DNSVELGm//dzFDXlN+joQ0lQar4sgdXMe8gK/NzLHzLJD+FvcobodDYOobCxo2PtPU9hl8Xyflo8NtpKAxX7ia3nbORGwCxGjVuhLxfDqsPutlBCs7GGaESker2z7J8+DcZ7Tl/fqnH1h4jfDPAB8NUnq4RVzb4BA7N5ryjk1AQr6EyQESf1/QQKB0DvQfhZ986Cq39R8Z6VMsjy1RIuZz8su3aNOUdfn2wsv6zNhXiN9CNZP/9hOaqwqpJ9P1cYShvxRb/fjzhsYAEXuwPJ1KO7FbVrugQFujxGORbA16Ld31OP1nQzlefHaboFB8M8zfKduukTlMO9/YIZ/ls5Zu+yfUuq6I+fgvhUSXvI7lvF8oUEV7sZsRaCGFcpp4uxImkdSCdsCAYYDccxnkWObgaVpPVuTj3xCbV4x79eJSk6vDEy4ucSr8xpeWZnsP/4V3ALF8F2c3gsfib+V6EZpnUUb2lMA+7r3Sp77y6sdlZxymxhhzw/yqEYxY2W7oJm6U565JHRWFzOuBF5ZRXf9uzyct5zakmQiccLjNKkuu0yIR2mF69tZuS02KVD6qtCHf+CKSDTa/S2N1jmRUw5LAy3zhqxrw/EQXtzXtOD65CAr2xoKwUpQwaaXwvWzL4DYT6Gly6ktpn1PNcFKdMfOFWpqarXAMBpdohI7iIPnUDkMDEjQr0VA9z+42kuwX5mVg3EoXtijvaai+esBl3pQTRqdC6zu0SphzUsU91vQxcbuJ961kPjvdi0jYUTs4OC+MetoIuNJs4r9ddFaNFL5YRjVbb3i57yIM2xyCELFpNvI+DJOycL9zKBPK+m4pXrl0/ux0eHP/W/OjXDbRVPCwhJVVU/nF3/xR1D54akBRNZyd2fD94tYjn481Q+YUxtHxoO20gX9lCq3G8W3zjZASs3v5RxUp8qRx9fI/c6pGk9yv4RA5deTx+1ZNPkVsChVxANHO7NwU0gBjkwN10jdjhb7ppRRW+FRMFP14WPdTNKOURDvmhxP4YheQFvh+YOJl+uv1pkgMkNXgMLg/YgPpdDLEB/4/5IosMdlJ6dx2DUg2h54obuuIqZ7W1qep84dw0DpheC8BRgMeUGLptqwPtEq8hNFPX1CmZ2tl8u0ow+bmZumquSUwgv9yak1PQ7IHS/+yll02edc5P93DzAOa/3Vxp7um2s7ftJb6Z9AQXOi+gXEaAhjy9vBoQizAdFnMaTy2NiIYFFtX88a4QBcZ1PCIMaz00uV+kghd9qbEQEQtB0iuVJJG9G8dbHv9FyXij/JBqXf6uLK0bzl56Rapsmer4bGE/y+IeiHKF1DzddEQ3JE6nR9HoEeglnLCKfeGT2yCfoC5kYU1R9zfigRqhi5hBCv9GxAHm1Zt4+otX0J4uMR4kiMUxHQ30TX4S7HJWJ+dqz7ICk9YgJLQim+0TvzJzncR3J+GgeUWdzq2v5hLd9MIzSbtPRB3a1dnc+o0RCr0mf28KnaEpEdsBbA7Nrd+I5h9PwJRLvMd/98dymklly6E/A39TbimGHQRm+adeNWCPaK0Hhf1l904baIEmfiaE8Vs9iK3bl70bpnB3gFc3YeTFei+tMqBD3tBtEaDh9Xib70T1fUWii3OmDl2sAjw5miX03TjHuYUmb0CsWu9BWS/IT4xB4kwHZlRmYK6DdPCriEjPhxHXdUCyrL+uxvcl90svUd/e67LeQCiATo7+TMmzhPPVsyVMnBO/YCa2nnClbzKeu6hdRz19CzhhSKVk+uh26fUDBQpIqNI07sMtzubsw6XfhctQ4EUJLSiQUmyhDJhRpmbNCOoFAtFQEyWONQ4f49vAnt9FkVXzg3ccZoK5zoaioR0sZFzG7GIYs9/12AT0r2NgfB6kkip59FR4gDS+N+Xpw0FADeTtwKJIwoBo7kylZ9QM3NzK0iH25vE6O3bGEcK37DukxHI+b3SPY3qfOegE5XlKC3NsMM0yE4Xly11ADyJ8RGcAIW8bGknKCk7yem6YVmJ/sTSMCliZwjfoWIOQnBveLu28pNbtN8CfNJI8P0+DWZ0MkresB0ww6xVBDceeByeHCc9DOMK03Gjndo1X54eM7YsXpTpbJ+215o+KxrRzKYW1VTbFp9G06088lGVtEXTzucj+/pJjoYP7tCWqoOxFmQ99tkOZaDM0amsMq6R/eKjXfGBFoFjBQS1Pxfh8e49fg8p8CX8aELlqt0EBios5BicpQvmCxnQqOKWZhay6KR5KQdQYS8qxtULkIvcL7m4W+FDAY5z7+VoZuH74rmHRYNndbcnd5Tyeyz6yHBWKHGAI1BGIVPuDhWMNLeOHPGMVMUxowUxbFkI/EDNBVlx8b+KzGCcGyKW37VDbqWBsidNRpZ+yr8WrAR4z2k6lGNK2egBDvV8XB1DtiAuZZNz/jx+VZMmdzlZnTHCVWjpPGqJ8iDkctT17/FLFZTV5YUmcoS2r4MTPxN2R70bb+e8kkL1v4tzrjYzzg7eIRAGUWNNHfV1R//DdWFMfHQj0SHILVzTliumJrcHmcdoEnmeFerobRn/0Pal3rG612sCodMWhn3mAW+RWC6vqZdCr35R0k1gvtBddQmJH18OcZI4s7u0zKvOs0OmaaxhaRXY0FxbuZMJqHGCkv9Tv66VVj0uRmTzp9WCo2Xz162GIR4JSUTzWkwvnzSKSMPuLA7MPdgmyMNXVMu8H43WDXEWVWmRXatfePIuTpIjlDM0exDrLw5YjCAamHtN43kZpDVExG7/66WS/S2+xQ5lbFQ/nklWlDIb8mT7NtF3nf3r2Cyycf03gRS/qMJA8sYnhZ0ggbOzc4s+P68RAGhWiSiL49PZ605T1n4qDR6l0dfIR/a/qBIHw6CToP8Vqq2Ud2ViJPqqeYDuM1P1ArF24l3DXjwaHhgMTgcHI2seKR8W+4gNtKj+rYLPvJYsBUL8M1UXOzdKUAnVbofHP9KzVrJf1RajprGypMmsIZYG8zrwgLkuHKw+KiQAhXBEh6+CGvdBpa73uyIdTptogU+RMGcdhm7w4vFYw2IuPXBm1y8AR5PbrCjGikeqc+EQmKApa1hXrywlqNCHQqG5jr+aFnWfT6PpKVf+R4alZQpkOh89Obo7GQE5AqA3uTPrux/uV94oXLeDKUjq9g5qLCmCfnS7GUOOPrRtgj1tRTJ3Kw+YUgMYd6ST4fEsFjyUzPI2AOMjqDO82JAzyECx5MT0jQdjLRznJyLrUjN4kwLDRSSSmu2g2OXWUQIdM7wtbG1msrA32wUQbHJ21v9h3rSZ32qm8jI71GFSww0E3Iq113C+qwb/6UKj70Ln94swMWkpwRncHf0miIMBsDycS7m0wXPgHwMF/0galc58Vr1G4yxKWPWA/n2c7aRiA0iWBHls7UszntGFNcXIyi55DA+ELLnR4dJRTrAmNuW67pcDQ3hhhtk2m89KQSksFpUSQY04MLyZDTa1FbJxYozzwikK4WTnhk87LJT23q3ih1a5JZRaNOxO/C8iWVy4BOKWd1057yBAFVkUmkTUjqfYpCiOY65hbnoqsynr9yN0ne6eS2iSLHbbpiibrKF7uv0ZRU4izRnYrW1bBQI7mdHpm69nKLhV0ZkAdIh5kGjSoUM+5ip9wvZ9pqS48MpTvac0XeF8MNDbHctVQsP0PfTWyK3TUYxcyScK47I/QMzrIkQQC6BunzoQ1PzVC6Uh0eKu9MwN5yaWS6Xtfqn7zhU8/jvuz2yLd91qVcOuGitNpkJHrKZ4veoRSfCKpu3mVP8GfPx7N+65/nzIL5PkDZbNcZtqw262/7Fh28ML8Avb/NmqzJ5uSfUG6P3yM8mx/3NVQLxCq+04zqrIWuU8F9q7Ryz7fMwopvDQCyJQpRezsl4KiRQlUh6lp81QR7WkN0jev8ciOFGNMm2k3h16+USGc+PeMP1tr1YVcAjCWsBY+alL+AsHXg8ANWLYOIXpkTbnmPEuNMDiuOU2RzjarGcjOwBtxFbXq4oQEgPiWO1oY3HVapHMKaNFzuO7+/udm52kzkfaNskavddcl5+mlONRDhflWq3xPD4hm5AwXSAypYbgshNXu/Y0C/ruvN1+21y/PKOVhCJOmNYmYW6eqAbMZLbLvXz0tF74yp1ga/QxDtgKxrVoP5Xec6B/hg5Z+4n2d/XSr3C+mDOayLiYwIEqj3Y4qMIBATtK4mtbdtlo/+x2VLnOCNXzSLGv5o+ujIN3i0Y9S2trzUIFPpfzY34PqxsZu+w+6KtJOiuiZFvknQp6uu5RdTBJ/yEEWE6kmkr4RTwQhDf30Gk8hbdrRPOzQg0lRJRBSaq4hndxv+1Yflweex7GQNI+jywwF+Z43wMUm+6nwQjhwYKLap1UTpntDcVxxxudV/mNjqXAQ99aTfYCqyUVCVw6iAfXkZQMu8y+js8MOr6Q7Qb2/0mSlrO6W8uKUwM9dvOy22Wz2wHxZOTsIRjOggb1Xt5FwbKNhQ/ACbmKyouOzZbyYdwNjw3X2yEHdLXyx+1XsPDr/cz0l2BnhkRUbHQU2BLO2RoOj8mozY10mX3Stw0pAiJ87hdm+WMlAsOLAD1uhQ6l7UDvEz8fHJMfv8/XMKgKWBFzcMRQJPP/cq0/tmiCmHnjaA5na64Jfuj7M9hKmk78zok+RTK0TvrycioR2rftRrKvEcw9MqanE9C9udbhKjzhQ7SedXeGfpmrQEzaYksxciFD1Wh9rSGB9CHVPg4F/gSwW16Gk0oty9s29dbCKQjkBBRwjuHWYxvisojb3RWcyuyEcmRbH2NEMgEgfaNGRFLHF/XRbeKToUJjggxXQ63hKJQrbuhMkhDqRmdq7Z0d22P3A+yIfLxcV5LlrdeDhjR5Xxsng6YeLoeAbJrRFSJzwZ40glUQY+SwXzyLwhvfgNL8gkqcVYbt+PLZqIje8iWJlcw1qW+KqjtibYj8YlZ4ZdnW+D5hudgeX4zcxDAunGySIabxSXs/HBzC8YsuhHge1ziP8390spbkMAIBhU2D2UA7eGLLsUMx7pQY5B7j8BetFcT0xOvpx2M/PlYEOgMZwO0w4zP49DoR12OFytm0ddU//vemew+szRhkxMbjPBm2gISDaRNqXGK+/doLSx/iLfqZRph/efx6wWNUt11I6uWCs9EX4FiKZBX+rKcRn9RVXPTNEW+4SVp8yHDbHS8clIvMim/0HdLE5ZaBmpXgXRF5nF3UAu5QmVlNPCqQUiAGGMMmA8b+T99fiI4zH5tCEJL87ujWBeCFcphF1j0tHQMewcgato+M8Q+wP2YRAj2eOs656uUsKhpcJvE+6OqrwDo6eUDuu2FB7JTuseV7lTGzh+oYVpSEFwE4EzQhgEU4LHIh2L+fJnHdAXCvLeOOEhOpChXowH9DME95QKVLjGqKY0UAAccGJgzHpkdv6rSLOkbDiIDvfzm0bDjgkxFxBKNF1/eENJ2Dtsyc9yP92EjUacWZszeZJ4W3h7ZRznJHW3pivZQbk56ctAxJP7c4GY3cRONGfLAiMmr5FkEp7rm89qQy6zGX9xNsoesln527433KGpjgDen6guotlri6lO5mTErW2nBHdShXPcBAnwf1nqAz+/v95cjHuaszBqlDnL8MOhKB+iY9LzyeXwNdZ3oS7x3Rp9ZoYgww0zxmx/TsFBFKsnQgLdlAphkI2pdwDBrZTZAMwfgu5XuJopqnu3YyoRCOJGCcYUcXpL4lCWtADqqQEqJCmKIhW41ohXJejxLy209Vs9oz5vijkCEqSVTeToOzjLHqhW/Nw/RMuoy/EF+wS82yIoYqlzOLHKaNxpnBhvKBduzm6uEQEpwmjr9YnqZKW8abdVBr3SS2W91H0M6N5TQYBecY1oWKQxFrNk+gVjlvHvrrNZLOJqICejgKzS9Xnx4yvc/bbhoIBv3ZxfUqGuQN0ogbmabLPUnl9cppKB4vuXHpBsFaq7tOQs7nAASZ9rY7OzdFnN7qE6d324QNTkx3X8Yecf43ZZw+H7/HcJLoTLVAKA6QTwcKlsVNU0lMgQaEIJEH/WM3gcggMVKVjcZxRaXXzpX2om5aKmaTafzhMdfngKJtZfde1j71KVqe0W3SuTm/cHsnHUOZoqt/fbeZUjmQLGSASjcsEwKH5ReCG8aFczyKjybW0ksZ5qifHaBTWUhcBc1iVzy7ujYAcJSJW5qrIbNWenzHc+MyaTFjtqP/AS9uoYeZc0mhwDWAAyUUvEWDlM+BdcMZe+lEANf+OQBh1xtwn0Mld7QWWmtk0hNk0mQg69r2mlpGmUl3a6cUu6fsHAJuSMol/2NXmYDOdYMvK9L1/Z90N7GnddY3sQa2GSpK77n3kLj2UrgJus8OgIFmxuCD7RYXBjC6Pkps3LX2Lmo/EW/LO0uYS0vFY3gzx4F00waU5t2wXdh8rfKcyWtbcTvqLGNS0qABs4hnxOcT8EIfPRoRe/eLB/V5UlfzRyHdIwj2h/cnoJW1Gpu2N2PtD3x6Nlc701EPxy1DNfAPJzLLQfIamtLJArBhgJ3yqtOyKHPaD4Gu+Zkol+MVXj9KDfDLbLfVjnGcVynJfGXezKsPWynpXB1nE2A19WzrqgqZbaFNdBd1iGIyypSjI4S2PDirEKaskbCLEEvuTN9UhXZDVKqeb/zdz000/E2wOeBZhuEK2osMCaQbue+KO0VgoUYOYaH9aoiPdmRoZUmkQXKluxI/GEsfelEw/MK0/J9gnxFvHNJcanrMFmHQXpwUkILesFllC3A4lRxrvUZu7pB/hJCCdRWdp7IF/hdqvGk4x0gcYeEsW3jF9YN+OelP7KQJklDGJMcAkW2CDQ7vHj5/hyzh4L+NZvywFEBM94CmWmolH5kE5qHahPMkpBdp4NIlBrnrM+3HlggoPtDeVMoJzC45Ou3mJCY8pb7sUMm6RIaX3gs1Ulroe4gx8oSYkHVbwR9vioZ2T/Q8Ize1CU2B3SjVIfHi
        - #2:
          - type: tool-call
          - toolCallId: lMLIpnOc9afb6Kev
          - toolName: set-policy
          - input:
            - Rationale: We are changing our next policy priority from Futurism to Enlightenment. Russia has captured Cologne, disrupting our immediate plans for city liberation and making the tourism bonuses of Futurism far less impactful. Enlightenment (Rationalism branch) provides 1 Free Technology and +1 Happiness from Universities. This free tech is immensely powerful for catching up in the science race and accelerating our progress towards key spaceship technologies.
            - Policy: Enlightenment
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: uJkhKiONtvh43s7n
          - toolName: set-relationship
          - input:
            - TargetID: 7
            - Private: -20
            - Public: -20
            - Rationale: We are softening our diplomatic stance towards the Zulus from -50/-45 to -20/-20. Our peace treaty with them expires in 7 turns, and they possess a formidable 6.1k military allied with our active enemy, the Inca. By reducing our active hostility and leveraging our shared Autocracy ideology (+999 modifier), we aim to deter a Zulu declaration of war upon treaty expiration, keeping our borders secure and allowing us to focus our defensive resources on Russia and our production on science.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 3yiDpA6VAsKYKrcD
          - toolName: keep-status-quo
          - input:
            - Rationale: Our current strategic posture and flavor profile remain highly optimal. Russia's capture of Cologne from the Inca underscores their overwhelming military and territorial threat, making our maximized defensive settings (Defense: 95, CityDefense: 95) and nuclear deterrence (Nuke: 100, UseNuke: 90) absolutely necessary. Our naval forces will transition from the Cologne offensive back to securing our domestic coastlines and Berlin. We will maintain our Spaceship Grand Strategy, supported by maximized Science (100) and Production (100) flavors, while utilizing our Great Diplomat in Quebec City to manage city-state relations.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: bw236JvsHEIrA02V
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
          - toolCallId: lMLIpnOc9afb6Kev
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: uJkhKiONtvh43s7n
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 3yiDpA6VAsKYKrcD
          - toolName: keep-status-quo
          - output:
            - type: json
            - value:
              - message: Tool keep-status-quo not executed in replay mode.