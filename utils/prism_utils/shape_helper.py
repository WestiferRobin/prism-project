import torch

from configs.prism_config import MAX_CELL_SIZE


def generate_shape_input(shape_label):
    if shape_label == 0:  # Circle
        return torch.ones(MAX_CELL_SIZE * MAX_CELL_SIZE * 8) * 0.2
    elif shape_label == 1:  # Square
        return torch.ones(MAX_CELL_SIZE * MAX_CELL_SIZE * 8) * 0.5
    elif shape_label == 2:  # Triangle
        return torch.ones(MAX_CELL_SIZE * MAX_CELL_SIZE * 8) * 0.8
    else:
        raise ValueError("Invalid shape label")


def shape_to_target(shape_label):
    # Create constant target patterns matching output size (256)
    if shape_label == 0:  # Circle
        return torch.ones(256) * -1.0
    elif shape_label == 1:  # Square
        return torch.zeros(256)
    elif shape_label == 2:  # Triangle
        return torch.ones(256) * 1.0
    else:
        raise ValueError("Invalid shape label")