import json

from src.models.atom import Atom, AtomStructure, AtomPhysical, AtomIdentity
from src.utils.constants import PERIODIC_TABLE_PATH


def load_periodic_table(json_path: str):
    with open(json_path, 'r') as file:
        data = json.load(file)

    table = {}
    for entry in data['elements']:
        identity = AtomIdentity(
            name=entry['name'],
            symbol=entry['symbol'],
            number=entry['number'],
            group=entry['group'],
            period=entry['period'],
            category=entry['category'],
            block=entry['block']
        )

        physical = AtomPhysical(
            atomic_mass=entry['atomic_mass'],
            density=entry.get('density'),
            melt=entry.get('melt'),
            boil=entry.get('boil'),
            phase=entry.get('phase'),
            molar_heat=entry.get('molar_heat')
        )

        structure = AtomStructure(
            electron_configuration=entry.get('electron_configuration', ''),
            shells=entry.get('shells', []),
            electronegativity=entry.get('electronegativity_pauling'),
            electron_affinity=entry.get('electron_affinity'),
            ionization_energies=entry.get('ionization_energies', [])
        )

        atom = Atom(identity=identity, physical=physical, structure=structure)
        table[atom.symbol] = atom

    return table

PERIODIC_TABLE = load_periodic_table(PERIODIC_TABLE_PATH)
