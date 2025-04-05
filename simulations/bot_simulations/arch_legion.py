from models.fotf.legions.model import ArchLegion, AdminLegion


def run_arch_legion():
    print("Arch Legion of Drones")
    user_legion = ArchLegion("Wes's Legion")
    master_legion = AdminLegion("Other Legion")
    print(f"{user_legion.name} {master_legion.name}")
