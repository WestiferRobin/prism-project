import uuid

# Constants
MAX_CELL_SIZE = 16
MAX_PRISM_SIZE = 64


def seed_id():
    return uuid.uuid4()


def hex_id(seed=None):
    return seed.hex if seed is not None else seed_id().hex


def str_id(seed=None):
    return str(seed) if seed is not None else str(seed_id().hex)


# Data Structure for Prism Cells
def build_data_byte(u_nibble=None, v_nibble=None):
    u_nibble = seed_id() if u_nibble is None else u_nibble
    v_nibble = seed_id() if v_nibble is None else v_nibble
    u_value = str_id(u_nibble)
    v_value = str_id(v_nibble)
    return {"u": u_value, "v": v_value}


def build_prism_cell(nexus_id=None, data=None):
    if nexus_id is None:
        nexus_id = seed_id()
    if data is None:
        data = build_data_byte()
    return {"id": nexus_id, "data": data}


def build_prism_nexus(nexus_id=None):
    nexus_id = seed_id() if nexus_id is None else nexus_id
    nexus_mass = []
    for i in range(MAX_CELL_SIZE):
        cells = []
        for j in range(MAX_CELL_SIZE):
            cells.append(build_prism_cell(nexus_id))
        nexus_mass.append(cells)
    return {"id": nexus_id, "cells": nexus_mass}

