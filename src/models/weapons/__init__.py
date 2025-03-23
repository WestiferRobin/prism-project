"""

DroneWeapons:
    Primitive: Staff, Hammer, Knife
    Medieval: Spear, Sword, Axe, Bow, Shield
    Industrial: Vehicles, Guns, Rifles, Pistols
    Standard: Fighters, Ships

Primitive:
    Staff, Hammer, Knife
    Wood, Stone, Copper
    Fruit, Veggie, Meat

Medieval:
    Spear, Sword, Axe, Shield
    Bow, Mounts, Cross-Bow, Trebuchet
    Ore: [Iron, Platinum, Obsidian, Tungsten] Money: [Copper, Silver, Gold] Gem:[Dimond, Ruby, Sapphire, Emerald, Topaz, Amethyst]

Industrial:
    Tanks, Trucks, Cars, Cycles
    MachineGuns, ShotGuns, Rifles, Pistols
    Heat, Oil, Electricity, Water

Standard:
    Speeders, Fighters, Shuttles, Ships
    Packs, Stems, Explosives, Shields
    Bases, Ports, Stations, Energy

DroneOrder: AdminOrder
    - Leader: Admin Arch => Best PrismLeader Drone of all time of 12 years and decides to lead or retire
    - Vice: Vice Admin => Best PrismLeader as FleetLeader and BaseLeader voted in 2 terms of 12 years
    - Admiral: Admin Admiral => Best FleetLeader and incharge of all ship operations for Order
    - General: Admin General => Best BaseLeader and incharge of all base operations for Order

PrismLeader: Arch
    Best PrismManagers leaders of ship or base for Legion
    Best PrismTroopers fighters of ship or base for Legion
    Best PrismWorkers citizens of ship or base for Legion

PrismDirector: Major
    PrismManagers: Captain and Commander and Lieutenant
    PrismManagers: Captain and Commander and Sergeant
    PrismManagers: Commander and Lieutenant and Sergeant

PrismManager: Captain of CapitalShip of PrismDirector for 20 drones
    bridge-crew:
        vice_officer: Commander PrismTrooper
        tactical_officer: Lieutenant PrismTrooper
        science_officer: Lieutenant PrismWorker
        medical_officer: Lieutenant PrismWorker
        engineer_officer: Lieutenant PrismWorker
    standard-crew:
        - 1 Sergeant
        - 2 Ensigns
        - 3 Lances
        - 4 Corporals
        - 4 Privates
    ship-hanger: or carrier with 1 fighter-squadron
        - shuttle-squadron:
            - pilot: 1 Ensign
            - co-pilot: 1 Ensign
            - crew:
                - 1 Sergeant
                - 1 Lance
                - 2 Corporals
        - fighter-squadron:
            - 1 Lance
            - 1 Corporal
            - 2 Private
        - fighter-squadron:
            - 1 Lance
            - 1 Corporal
            - 2 Private

PrismManager: Lieutenant of CruiserShip of PrismDirector for 12 drones
    bridge-crew:
        vice_officer: Sergeant PrismTrooper
        tactical_officer: Sergeant PrismTrooper
        science_officer: Ensign PrismWorker
        medical_officer: Ensign PrismWorker
        engineer_officer: Ensign PrismWorker
    standard-crew:
        - 1 Lance
        - 2 Corporals
        - 3 Privates
    ship-hanger:
        - shuttle-squadron:
            - pilot: 1 Corporal
            - co-pilot: 1 Private
            - crew:
                - 1 Lance
                - 1 Corporal
                - 2 Privates

"""