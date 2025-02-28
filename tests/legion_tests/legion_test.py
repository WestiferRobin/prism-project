"""

LegionArmada Tests:
    LegionArmada Base:
    - TerraBase for Earth and Mars Missions
    - LunaBase of Earth's Moon and Asteroids Missions
    - BaseStation for Venus Missions
    - ArmadaCamp for ArmadaShip to Gas Planets, Standard Planets, Dwarf Planets, and Asteroids and its moons Missions
    - StarStation for Galactic Missions in Interstellar Space
    - NexusStation for Nexus Missions in Light Space with Sovereign Devices
    Star Base: TerraBase
    - 1 Citadel on Earth on Admin and Vice Orders
    - 4 Bases on Planet on Admin Orders
    - 12 Cities on Planet on Arch Orders
    - 11 Towns on Planet on Colonel Orders
    - 10 Outposts on Planet on Major Orders
    - 8 Camps on Planet on Captain Orders
    Star LegionArmada:
    - Star Base has 1 LegionFleet but room for more
    - Does Missions for Trade, Military, Scouting, and Transporting

"""
from src.models.legions.legion import AdminLegion, ArchLegion

def validate_arch_legion(legion: ArchLegion):
    admin = legion.admin()
    if "Arch Admin Leader" != f"{admin}":
        return False

    armada = legion.armada
    if admin.id != armada.fleet_leader.id:
        return False

    dreadnought = armada

    return True

def validate_admin_legion(legion: AdminLegion):
    return False

def test_fotf_legions():
    print("Testing fotf-legions")

    federation_legion = AdminLegion(name="Solar Federation") # Chancellor Vao of Corusant with Taris, Naboo, Corellea
    empire_legion = AdminLegion(name="Ethereal Empire") # Emperor Palpatine of Exogal with Korriban, Malacore V, Dathomear
    pirate_legion = ArchLegion(name="Pirate Syndicate") # Domo Zorba the Hutt of NalHutta with Jabba, Ziro, Zorba
    raider_legion = ArchLegion(name="Raider Syndicate") # Jango of Clan Fett of Mandolore with clans Katan, Ordo, Vizsla
    drone_legions = (federation_legion, empire_legion, pirate_legion, raider_legion)

    try:
        test_grade = True
        test_results = {}
        for drone_legion in drone_legions:
            if drone_legion is ArchLegion:
                drone_grade = validate_arch_legion(drone_legion)
            elif drone_legion is AdminLegion:
                drone_grade = validate_admin_legion(drone_legion)
            else:
                drone_grade = False
            test_results[drone_legion.name] = { "grade": drone_grade }
            test_grade &= drone_grade
        print("Test Passed!" if test_grade else "Test Failed..." + ": ")
    except Exception as ex:
        print("Test Failed due to: " + str(ex))

if __name__ == "__main__":
    test_fotf_legions()
