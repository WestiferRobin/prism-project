from pydantic import BaseModel

from utils.configs import PrismConfig


"""

Wes's Avatar and Team on Red Hawk

config:
    dna: UUID
    name: Wes Black
    gender: Male
    rank: Commander
    stats: PrismStats: WorkerStats
        - Intelligence: int
        - Charisma: int
        - Agility: int
        - Stamina: int
        - Will: int
        - Perception: int
        - Combat: int
        - Dexterity: int
        - Strength: int
        - Magic: sum(stats[:stats.length - 1]) / len(UUID)
    skills: List[PrismSkill]
        - ex.)
                LegionSkill
                BattleSkill
                TradeSkill
vitals:
    - parts: List[PrismPart]
        - total = 100%
        - head: brain at 100%
            - skin: int
            - mussel: int
            - bone: int
        - arms: 2 * 100%
        - legs: 2 * 100%
        - torso: at 4 * 100%
            - 2 lungs
            - 1 liver
            - 1 heart
            - 1 blatter
    - health: int = sum(parts)
    - effects: 
weapons:
    - primary_weapon: BattleRifle
    - secondary_weapon: Revolver
inventory:
    - items: ShieldPack, RepairPack, 2 FragGrenade

config:
    dna: UUID
    name: Max Grey
    gender: Male
    rank: Lieutenant
config:
    dna: UUID
    name: Tyler White
    gender: Male
    rank: Lieutenant
config:
    dna: UUID
    name: John Red
    gender: Male
    rank: Sergeant
"""

class Prism(BaseModel):
    config: PrismConfig

    def __init__(self, **prism_data):
        super().__init__(**prism_data)


