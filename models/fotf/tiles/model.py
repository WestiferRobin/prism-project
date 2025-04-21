from enum import Enum

class BlockType(Enum):
    FLAT = "flat"     # Normal terrain
    RAMP = "ramp"     # Slope between elevations
    CLIFF = "cliff"   # Impassable steep height difference


class TerrainType(Enum):
    GRASS = "grass"
    DIRT = "dirt"
    WATER = "water"
    STONE = "stone"
    DESERT = "desert"
    SNOW = "snow"

class Tile:
    def __init__(self, x, y, terrain_type: TerrainType, elevation=1):
        self.x = x
        self.y = y
        self.terrain = terrain_type
        self.elevation = elevation
        self.block = self.determine_block_type()

    def determine_block_type(self):
        if self.terrain == TerrainType.WATER:
            return BlockType.FLAT
        elif self.elevation >= 3:
            return BlockType.CLIFF
        else:
            return BlockType.FLAT

