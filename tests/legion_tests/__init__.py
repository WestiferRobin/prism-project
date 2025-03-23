

"""

Idea:
- Ships must exist on board is a legion_test that passes legion_game_tests for ship to base routes
- Players must battle Enemies on board is a legion_battle_test:
    - Ships must battle on board is a legion_battle_ship_test
    - Bases must battle on board is a legion_battle_base_test
- Players must trade NPCS on board is a legion_trade_test:
    - Ships must trade on board is a legion_trade_ship_test
    - Bases must trade on board is a legion_trade_base_test
- Players must trade and fight Enemies and NPCs on board is a legion_game_test:
    - LegionShip on trade route to Base that is Player Owned
    - LegionShip on trade route to Base that is NPC's Owned that are Allies
    - LegionShip on trade route to Base that is NPC's Owned that are Neutrals
    - LegionShip on battle route to Base that is NPC's Owned that are Neutrals
    - LegionShip on battle route to Base that is NPC's Owned that are Enemies
    - All ships are part of fleets of legion on the galaxy board is a legion_game_test
- Fotf Game is Player vs Enemy with 2 sub enemies or allies up to the player
    - TODO: Make this into legion_campaign_test with 2 Admin Legions or 2 Arch Legions
    - TODO: Federation is player as true-good and Empire is Enemy as true-evil
    - TODO: Mandolorian is neutral-good and Hutt is neutral-evil
    - TODO: Natives is true-neutral as Primitives, Industrials, Urbans, Elites issue items and vehicles
    - TODO: Consider making official factions with leaders matching lawful-neutral-chaotic
    - Prolog Trilogy: Episodes A, B, C, D
        - Mandolorian Wars: Revan's Fall
        - Infinity Wars: Revan's Rebirth
        - Reborn Wars: Revan's Reign
        - Sith Wars: Revan's Death
    - Trade Trilogy: Trade Wars
        - Naboo's Fall
        - The Fallen One
        - The Fall of the Federation
    - Civil Trilogy: Civil Wars
        - Deathstar's Fall
        - The Dark One
        - The Fall of the Empire
    - Remnant Trilogy: Remnant Wars
        - Coruscant's Fall
        - Illum's Fall
        - Syndicate's Fall
        - Emperor's Fall

"""