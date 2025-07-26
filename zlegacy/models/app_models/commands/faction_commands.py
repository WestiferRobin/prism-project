from uuid import UUID

from src.utils.enums.faction_enums import FactionType
from zlegacy.models import Command


class FactionCommand(Command):
    faction_type: FactionType

class PrismCommand(Command):
    prism_id: UUID

class LeaderCommand(FactionCommand):
    colony_id: UUID
    fleet_id: UUID

class WorkerCommand(FactionCommand):
    worker_id: UUID
    company_id: UUID
    team_id: UUID

class TrooperCommand(FactionCommand):
    trooper_id: UUID
