import uuid

from src.utils.enums.prism_enums import LegionRank

# Constants
MAX_CELL_SIZE = 16
MAX_PRISM_SIZE = 64


# Data Structure for Prism Cells
def build_data_byte(u_nibble=None, v_nibble=None):
    u_value = uuid.uuid4() if u_nibble is None else u_nibble
    v_value = uuid.uuid4() if v_nibble is None else v_nibble

    if len(u_value.bytes) != len(v_value.bytes):
        raise Exception("build_data_byte in prism_utils.py isn't working here. ")

    uv = str()
    vu = str()
    vv = str()
    uu = str()
    for index in range(0, len(u_value.hex)):
        u = int(u_value.hex[index], 0xF + 1)
        v = int(v_value.hex[index], 0xF + 1)
        uv += hex((u + v) & 0xF)[2:3]
        vu += hex((u * v) & 0xF)[2:3]
        vv += hex((v - u) & 0xF)[2:3]
        uu += hex((u - v) & 0xF)[2:3]

    uv_value = uuid.UUID(hex=uv)
    vu_value = uuid.UUID(hex=vu)
    uu_value = uuid.UUID(hex=uu)
    vv_value = uuid.UUID(hex=vv)

    a = str()
    b = str()
    c = str()
    d = str()
    e = str()
    f = str()

    for index in range(0, len(u_value.hex)):
        u = int(u_value.hex[index], 0xF + 1)
        v = int(v_value.hex[index], 0xF + 1)
        uv = int(uv_value.hex[index], 0xF + 1)
        vu = int(vu_value.hex[index], 0xF + 1)
        vv = int(v_value.hex[index], 0xF + 1)
        uu = int(v_value.hex[index], 0xF + 1)
        a += hex((u * uu + v + vv + uv + vu) & 0xF)[2:]
        b += hex((u + uu + v * vv + uv + vu) & 0xF)[2:]
        c += hex((u + uu + v + vv + uv * vu) & 0xF)[2:]
        d += hex((u + uu + v * vv + uv * vu) & 0xF)[2:]
        e += hex((u * uu + v + vv + uv * vu) & 0xF)[2:]
        f += hex((u * uu + v * vv + uv * vu) & 0xF)[2:]

    a_value = uuid.UUID(hex=a)
    b_value = uuid.UUID(hex=b)
    c_value = uuid.UUID(hex=c)
    d_value = uuid.UUID(hex=d)
    e_value = uuid.UUID(hex=e)
    f_value = uuid.UUID(hex=f)

    # TODO: Solve this please.....
    return {
        "u": u_value,
        "v": v_value,
        "uv": uv_value,
        "vu": vu_value,
        "uu": uu_value,
        "vv": vv_value,
        "a": a_value,
        "b": b_value,
        "c": c_value,
        "d": d_value,
        "e": e_value,
        "f": f_value
    }


def build_prism_cell(nexus_id, data=None):
    if data is None:
        data = build_data_byte(nexus_id)
    return {"id": nexus_id, "data": data}


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



