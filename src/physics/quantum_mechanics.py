import numpy as np
import matplotlib.pyplot as plt

class OrbitalVisualizer:
    def __init__(self, grid_size=400, extent=30):
        self.grid_size = grid_size
        self.extent = extent
        self.x = np.linspace(-extent, extent, grid_size)
        self.y = np.linspace(-extent, extent, grid_size)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.R = np.sqrt(self.X**2 + self.Y**2)
        self.theta = np.arctan2(self.Y, self.X)

    def compute_orbital(self, orbital_type):
        if orbital_type == "1s":
            psi = np.exp(-self.R)
        elif orbital_type == "2s":
            psi = (2 - self.R) * np.exp(-self.R / 2)
        elif orbital_type == "2p_x":
            psi = self.R * np.cos(self.theta) * np.exp(-self.R / 2)
        else:
            raise ValueError(f"Unsupported orbital type: {orbital_type}")
        return psi**2  # Return probability density |ψ|²

    def visualize(self, atom_orbitals):
        """
        atom_orbitals: List of (label, orbital_type) tuples.
        Example: [("Hydrogen", "1s"), ("Hydrogen", "2s"), ("Hydrogen", "2p_x")]
        """
        fig, axs = plt.subplots(1, len(atom_orbitals), figsize=(6 * len(atom_orbitals), 6))
        if len(atom_orbitals) == 1:
            axs = [axs]
        for ax, (label, orbital_type) in zip(axs, atom_orbitals):
            density = self.compute_orbital(orbital_type)
            ax.imshow(density, extent=(-self.extent, self.extent, -self.extent, self.extent), cmap='inferno')
            ax.set_title(f"{label} {orbital_type} Orbital")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
        plt.tight_layout()
        plt.show()

# Example usage
visualizer = OrbitalVisualizer()
visualizer.visualize([
    ("Hydrogen", "1s"),
    ("Hydrogen", "2s"),
    ("Hydrogen", "2p_x")
])
