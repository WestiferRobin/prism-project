class Particle:
    def __init__(self, electrons: int, photons: int=0):
        self.electrons = electrons
        self.photons = photons

class Atom:
    def __init__(
        self,
        electrons: int,
        neutrons: int,
        protons: int
    ):
        self.particle = Particle(electrons)
        self.electrons = self.particle.electrons
        self.neutrons = neutrons
        self.protons = protons
