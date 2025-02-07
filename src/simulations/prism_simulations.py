from src.models.drones.model import PrismCell, Prism, PrismDrone


def run_cell_simulations(source_cell: PrismCell):
    target_cell = PrismCell(source_cell.dna)
    if len(source_cell.dna.bytes) != len(target_cell.dna.bytes):
        return False
    for i in range(0, len(source_cell.dna.bytes)):
        if source_cell.dna.bytes[i] != target_cell.dna.bytes[i]:
            return False
    return True


def run_prism_simulations(model: Prism):
    for strand in model.dna_cells():
        for cell in strand:
            if not run_cell_simulations(cell):
                return False
    return True


def run_drone_simulations(drone: PrismDrone):
    run_prism_simulations(drone.brain)
