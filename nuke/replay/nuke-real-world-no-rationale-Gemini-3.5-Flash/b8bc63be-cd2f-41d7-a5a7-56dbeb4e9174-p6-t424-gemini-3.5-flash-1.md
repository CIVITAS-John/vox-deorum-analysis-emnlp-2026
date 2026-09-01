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
  - activeToolsModified: true
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
        - Rationale: Prioritize Satellites to unlock the Apollo Program, which is a mandatory project for achieving a Science Victory.
        - Technology: Satellites
    - #1:
      - toolName: set-policy
      - args:
        - Policy: Enlightenment
        - Rationale: Adopting Enlightenment provides a free technology and extra happiness from universities, directly accelerating our progress towards a Science Victory.
    - #2:
      - toolName: set-relationship
      - args:
        - Public: 20
        - Rationale: Strengthen and maintain our friendly alliance with India, our top diplomatic friend, to secure our eastern flank.
        - Private: 20
        - TargetID: 4
    - #3:
      - toolName: set-relationship
      - args:
        - Public: 30
        - Private: 30
        - TargetID: 7
        - Rationale: Improve relations with Shaka of the Zulus to leverage our shared Autocracy ideology and form a strong defensive coalition against the massive threat of Russia.
    - #4:
      - toolName: set-flavors
      - args:
        - GrandStrategy: Spaceship
        - Flavors:
          - Diplomacy: 75
          - Espionage: 95
          - Defense: 95
          - Production: 100
          - Growth: 70
          - Ranged: 90
          - MilitaryTraining: 90
          - Gold: 95
          - CityDefense: 95
          - TileImprovement: 40
          - Science: 100
          - Spaceship: 100
          - Mobilization: 80
      - rationale: Maintain the Spaceship grand strategy. Boost Gold flavor to counter the Global Peace Accords maintenance tax, maximize Spaceship focus, and support tile development and population growth for a tall defensive science empire.
  - tokens:
    - inputTokens: 51265
    - reasoningTokens: 6732
    - outputTokens: 289
  - messages:
    - #0:
      - role: assistant
      - content:
        - #0:
          - type: reasoning
          - text: **Analyzing Current Situation**
            
            My focus is on assessing our current position, including our six cities and their populations, as well as our ongoing research efforts. This review is crucial for determining our next strategic moves.
            
            **Clarifying Research Direction**
            
            I'm analyzing our current technology path. It appears "Computers" is under research, but the available options list different technologies. I need to confirm if we can set the *next* research project to align with our Spaceship victory goal and verify our policy choice.
            
            **Evaluating Victory Paths**
            
            I am currently evaluating our potential victory paths, specifically focusing on how to counter India's cultural victory push. I am also analyzing our own current progress towards a Space victory, considering our research and resources.
            
            **Analyzing Global Conflicts**
            
            I'm trying to untangle the complex web of current wars. It appears India is involved in numerous conflicts, and I need to understand our exact standing and who our allies are in this shifting landscape.
            
            **Assessing Geopolitical Threats**
            
            I'm reviewing our current relationships and active conflicts. It appears we're at war with the Inca and Venice, and maintaining hostile relations with Greece. Russia, a major power, now holds a German city dangerously close to our territory.
            
            **Analyzing World Congress**
            
            I'm examining the World Congress resolutions and proposals. Freedom as the World Ideology is impacting us negatively due to our Autocracy stance, but the Travel Ban is a boon, hindering India's cultural push. I've flagged the Endowment for the Arts proposal as detrimental to our scientific progress.
            
            **Prioritizing Science Victory**
            
            I'm re-evaluating our research path. Satellites is now clearly the priority to advance our Spaceship victory goal, so I've adjusted our next research accordingly.
            
            **Adopting Enlightenment Policy**
            
            I've identified "Enlightenment" as the optimal next policy choice, its immediate free technology providing a significant boost to our Spaceship victory pursuit over other options like Futurism or Rights of Man. This aligns perfectly with our current scientific priorities.
            
            **Redirecting Trade Units**
            
            Several trade routes are ending soon, freeing up units. I'm prioritizing gold generation due to its importance for military maintenance, science, production, and city-state influence, while also considering our unique Hanse and Brewhouse buildings.
            
            **Securing Strategic Position**
            
            I'm reassessing our defensive posture against Russia, given their recent acquisition of Cologne and extreme hostility. Their expired peace treaty means we're vulnerable to a sudden war, making immediate defensive reinforcement paramount.
            
            **Clarifying War Alliances**
            
            I'm reassessing our ongoing conflicts. It appears Venice was automatically drawn into war with us due to their vassalage to the Inca. This makes the Inca and Venice conflicts quite manageable given their low military strengths.
            
            **Strengthening Key Alliance**
            
            I'm focusing on solidifying our alliance with India. Their friendly disposition is vital to deterring Russian aggression, so I'm enhancing our diplomatic standing with them. I'm also reviewing our relationship with the Zulus, noting a significant ideological alignment that offers a unique advantage.
            
            **Strengthening Ideological Bloc**
            
            I'm prioritizing diplomatic overtures to Shaka, aiming to leverage our shared Autocracy ideology. Improving our standing with the Zulus could forge a powerful defensive bloc against the Order and Freedom coalitions, significantly bolstering our geopolitical position.
            
            **Leveraging City-State Synergies**
            
            I'm discovering a powerful synergy between our Hanse buildings and city-state trade routes, generating significant production and gold. This, combined with our unique city-state influence bonus, strongly supports our diplomatic strategy and bolsters our position against aggressive AI.
            
            **Adjusting Defensive Stance**
            
            My current focus is on balancing our caution and fear. With AfraidBias at 9 and GuardedBias at 9, I believe our current persona perfectly supports a defensive, science-focused strategy, particularly in deterring premature conflict with Russia while we prepare.
            
            **Refining Strategic Priorities**
            
            I am now focused on optimizing our game settings. I've adjusted our offense flavor to 50 and increased gold to 95 to support unit maintenance and accelerate our Spaceship victory efforts, while keeping defense and science high.
            
            **Optimizing Victory Pursuits**
            
            I'm now fine-tuning our strategic flavors, significantly boosting science pursuit to 100 as we aim for the Information era. I'm also increasing tile improvement and growth rates to maximize our yields and city development, further accelerating our Spaceship victory efforts.
            
            **Refining Diplomatic Levers**
            
            I'm strengthening my diplomatic ties with the Zulus, aiming to use our shared Autocracy ideology to create a formidable defense against rival blocs, especially Russia. I'm also boosting science and gold flavors to support our Spaceship victory goals and manage the upkeep of our growing empire.
            
            **Finalizing Strategic Adjustments**
            
            I'm confirming our research targets are correct, specifically for India and the Zulus. I've also verified that Russia's hostility and our current wars with the Inca and Venice preclude immediate relationship adjustments there. Our focus remains on our alliances with India and the Zulus to deter Russia, leveraging our shared Autocracy ideology. The plan now solidifies our technology path, policies, and diplomatic efforts towards a Space victory.
            
            
          - providerOptions: undefined
        - #1:
          - type: tool-call
          - toolCallId: Y3NribVwCsLwWrZW
          - toolName: set-research
          - input:
            - Rationale: Prioritize Satellites to unlock the Apollo Program, which is a mandatory project for achieving a Science Victory.
            - Technology: Satellites
          - providerExecuted: undefined
          - providerOptions:
            - vertex:
              - thoughtSignature: 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
        - #2:
          - type: tool-call
          - toolCallId: Rf9y1PrVRO3Jbr2l
          - toolName: set-policy
          - input:
            - Policy: Enlightenment
            - Rationale: Adopting Enlightenment provides a free technology and extra happiness from universities, directly accelerating our progress towards a Science Victory.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #3:
          - type: tool-call
          - toolCallId: ptyzqHhTdqmbWLYq
          - toolName: set-relationship
          - input:
            - Public: 20
            - Rationale: Strengthen and maintain our friendly alliance with India, our top diplomatic friend, to secure our eastern flank.
            - Private: 20
            - TargetID: 4
          - providerExecuted: undefined
          - providerOptions: undefined
        - #4:
          - type: tool-call
          - toolCallId: 7kRIJYuwp18WyVDp
          - toolName: set-relationship
          - input:
            - Public: 30
            - Private: 30
            - TargetID: 7
            - Rationale: Improve relations with Shaka of the Zulus to leverage our shared Autocracy ideology and form a strong defensive coalition against the massive threat of Russia.
          - providerExecuted: undefined
          - providerOptions: undefined
        - #5:
          - type: tool-call
          - toolCallId: mMG4xeGziM7ONZZ4
          - toolName: set-flavors
          - input:
            - GrandStrategy: Spaceship
            - Flavors:
              - Diplomacy: 75
              - Espionage: 95
              - Defense: 95
              - Production: 100
              - Growth: 70
              - Ranged: 90
              - MilitaryTraining: 90
              - Gold: 95
              - CityDefense: 95
              - TileImprovement: 40
              - Science: 100
              - Spaceship: 100
              - Mobilization: 80
            - Rationale: Maintain the Spaceship grand strategy. Boost Gold flavor to counter the Global Peace Accords maintenance tax, maximize Spaceship focus, and support tile development and population growth for a tall defensive science empire.
          - providerExecuted: undefined
          - providerOptions: undefined
    - #1:
      - role: tool
      - content:
        - #0:
          - type: tool-result
          - toolCallId: Y3NribVwCsLwWrZW
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
          - toolCallId: Rf9y1PrVRO3Jbr2l
          - toolName: set-policy
          - output:
            - type: json
            - value:
              - message: Tool set-policy not executed in replay mode.
        - #2:
          - type: tool-result
          - toolCallId: ptyzqHhTdqmbWLYq
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #3:
          - type: tool-result
          - toolCallId: 7kRIJYuwp18WyVDp
          - toolName: set-relationship
          - output:
            - type: json
            - value:
              - message: Tool set-relationship not executed in replay mode.
        - #4:
          - type: tool-result
          - toolCallId: mMG4xeGziM7ONZZ4
          - toolName: set-flavors
          - output:
            - type: json
            - value:
              - message: Tool set-flavors not executed in replay mode.