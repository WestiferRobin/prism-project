from src.utils.exceptions.chemistry_exceptions.atom_exceptions import AtomNotFound
from src.utils.periodic_table import PERIODIC_TABLE
from src.models.atom import Atom

def get_atom_by_symbol(symbol: str) -> Atom:
    if symbol in PERIODIC_TABLE:
        return PERIODIC_TABLE[symbol]
    raise AtomNotFound(symbol)

def get_atom_by_number(number: int) -> Atom:
    for symbol in PERIODIC_TABLE:
        atom = PERIODIC_TABLE[symbol]
        if atom.atomic_number == number:
            return atom
    raise AtomNotFound(f"#{number}")

def get_atom_by_group_and_period(group: int, period: int) -> Atom:
    for symbol in PERIODIC_TABLE:
        atom = PERIODIC_TABLE[symbol]
        if atom.group_number == group and atom.period_number == period:
            return atom
    raise AtomNotFound(f"group #{group} and period #{period}")

def get_atoms(symbols: list[str]) -> list[Atom]:
    return [
        atom for atom in PERIODIC_TABLE.values()
        if atom.symbol in symbols
    ]

def get_alkali_metals() -> list[Atom]:
    alkali_metal_symbols = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
    return get_atoms(symbols=alkali_metal_symbols)

def get_alkali_earth_metals() -> list[Atom]:
    alkali_earth_symbols = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra']
    return get_atoms(symbols=alkali_earth_symbols)

def get_transition_metals() -> list[Atom]:
    transition_metals_symbols = [
        'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
        'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd',
        'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
        'Rf', 'Db', 'Sg', 'Bh', 'Hs'
    ]
    return get_atoms(symbols=transition_metals_symbols)

def get_post_transition_metals() -> list[Atom]:
    post_transition_metals_symbols = [
        'Al', 'Ga', 'In', 'Sn', 'Tl', 'Pb', 'Bi', 'Po', 'At'
    ]
    return get_atoms(symbols=post_transition_metals_symbols)

def get_metalloids() -> list[Atom]:
    metalloid_symbols = ['B', 'Si', 'Ge', 'As', 'Sb', 'Te']
    return get_atoms(symbols=metalloid_symbols)

def get_reactive_nonmetals() -> list[Atom]:
    nonmetal_symbols = ['H', 'C', 'N', 'O', 'F', 'P', 'S', 'Cl', 'Se', 'Br', 'I']
    return get_atoms(symbols=nonmetal_symbols)

def get_nobel_gases() -> list[Atom]:
    nobel_gas_symbols = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']
    return get_atoms(symbols=nobel_gas_symbols)

def get_lanthanides() -> list[Atom]:
    lanthanide_symbols = [
        'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
        'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu'
    ]
    return get_atoms(symbols=lanthanide_symbols)

def get_actinides() -> list[Atom]:
    actinide_symbols = [
        'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm',
        'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr'
    ]
    return get_atoms(symbols=actinide_symbols)

def get_unknowns() -> list[Atom]:
    unknown_symbols = [
        'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'Uue'
    ]
    return get_atoms(symbols=unknown_symbols)

if __name__ == "__main__":
    all_atoms = [
        get_alkali_metals(),
        get_alkali_earth_metals(),
        get_transition_metals(),
        get_post_transition_metals(),
        get_metalloids(),
        get_reactive_nonmetals(),
        get_nobel_gases(),
        get_lanthanides(),
        get_actinides(),
        get_unknowns()
    ]
    total = sum(len(row) for row in all_atoms)
    print(f"Total atoms: {total}/{len(PERIODIC_TABLE)}")
