import uuid

from src.models.prisms import PrismDrone
from src.utils.enums.prism_enums import LegionRank


def create_child(female: PrismDrone, male: PrismDrone):
    child_dna = str()
    gender_cell_count = 0
    for dna_index in range(len(female.id.hex)):
        female_byte = int(female.id.hex[dna_index], 0xF + 1)
        male_byte = int(male.id.hex[dna_index], 0xF + 1)
        child_byte = hex((female_byte + male_byte) & 0xF)[2:]
        gender_cell_count += 1 if int(child_byte, 0xF + 1) % 2 == 0 else -1
        child_dna += child_byte
    gender = gender_cell_count > 0
    child_id = uuid.UUID(child_dna)
    return PrismDrone(prism_id=child_id, rank=LegionRank.Private, age=0, gender=gender)
