class AtomIdentity:
    def __init__(self, name, symbol, number, group, period, category, block):
        self.name = name
        self.symbol = symbol
        self.number = number
        self.group = group
        self.period = period
        self.category = category
        self.block = block

class AtomPhysical:
    def __init__(self, atomic_mass, density, melt, boil, phase, molar_heat):
        self.atomic_mass = atomic_mass
        self.density = density
        self.melt = melt
        self.boil = boil
        self.phase = phase
        self.molar_heat = molar_heat

class AtomStructure:
    def __init__(self, electron_configuration, shells, electronegativity, electron_affinity, ionization_energies):
        self.electron_configuration = electron_configuration
        self.shells = shells
        self.electronegativity = electronegativity
        self.electron_affinity = electron_affinity
        self.ionization_energies = ionization_energies


class Atom:
    def __init__(self, identity: AtomIdentity, physical: AtomPhysical, structure: AtomStructure):
        self.identity = identity
        self.physical = physical
        self.structure = structure
        self.ion_charge = 0
        self.isotope_charge = 0

    @property
    def symbol(self) -> str:
        return self.identity.symbol

    @property
    def atomic_number(self) -> int:
        return self.identity.number

    @property
    def period_number(self) -> int:
        return self.identity.period

    @property
    def group_number(self) -> int:
        return self.identity.group

    @property
    def atomic_mass(self) -> float:
        return self.physical.atomic_mass

    @property
    def protons(self) -> int:
        return self.atomic_number

    @property
    def electrons(self) -> int:
        return self.atomic_number + self.ion_charge

    @property
    def neutrons(self) -> int:
        return round(self.atomic_mass - self.atomic_number) + self.isotope_charge

