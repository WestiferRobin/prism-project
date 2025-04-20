from models.prisms.model import PrismDrone
from models.fotf.legions.legionfleet import AdminFleet, LegionFleet
from models.fotf.ships.star_ships.star_ships import StarCruiser, StarFrigate, StarCapital
from utils.fotf_utils.unit_utils.armada_utils import find_armada_ship, find_armada_ships_by_type
from utils.enums.prism_enums import LegionRank
from utils.fotf_utils.population_utils import build_armada_population


class LegionArmada:
    def __init__(self, admin_leader: PrismDrone = None, vice_leader: PrismDrone = None, fleets: dict = None):
        if admin_leader is None:
            admin_leader = PrismDrone(name=f"Admin Leader", rank=LegionRank.Arch)
        if vice_leader is None:
            vice_leader = PrismDrone(name=f"Vice Leader", rank=LegionRank.Arch)
        self.__admin = admin_leader
        self.__vice = vice_leader

        if fleets is None:
            fleets = {
                self.admin().id: AdminFleet(self.admin(), self.vice())
            }
        else:
            if self.admin().id not in fleets:
                fleets[self.admin().id] = AdminFleet(self.admin(), self.vice())

        self.__fleets = fleets

    def admin(self):
        return self.__admin

    def vice(self):
        return self.__vice

    def fleets(self):
        return self.__fleets

    def ships(self):
        ships = []
        for fleet_id in self.fleets():
            fleet = self.fleets()[fleet_id]
            for ship in fleet.ships:
                ships.append(ship)
        return tuple(ships)

    def cruiser_ships(self):
        cruisers = find_armada_ships_by_type(self, StarCruiser)
        return cruisers

    def frigate_ships(self):
        frigates = find_armada_ships_by_type(self, StarFrigate)
        return frigates

    def capital_ships(self):
        capital_ships = find_armada_ships_by_type(self, StarCapital)
        return capital_ships

    def flag_ship(self):
        armada_ship = find_armada_ship(self, self.admin().id, self.vice().id)
        return armada_ship

    def leader_base(self):
        flag_ship = self.flag_ship()
        leader_base = flag_ship.home_base()
        return leader_base

    def bases(self):
        leader_base = self.leader_base()
        armada_bases = {leader_base.id: leader_base}
        for ship in self.ships():
            home_base = ship.home_base()
            if home_base.id in armada_bases:
                continue
            armada_bases[home_base.id] = home_base
        return armada_bases

    def population(self):
        return build_armada_population(self)


class AdminArmada(LegionArmada):
    def __init__(self,
                 admin_leader: PrismDrone = None,
                 vice_leader: PrismDrone = None,
                 admiral_leader: PrismDrone = None,
                 general_leader: PrismDrone = None
                 ):
        if admiral_leader is None:
            admiral_leader = PrismDrone(name=f"Admiral Leader", rank=LegionRank.Arch)
        if general_leader is None:
            general_leader = PrismDrone(name=f"General Leader", rank=LegionRank.Arch)
        self.__admiral = admiral_leader
        self.__general = general_leader
        super().__init__(admin_leader, vice_leader, {
            self.admiral().id: LegionFleet(self.admiral()),
            self.general().id: LegionFleet(self.general())
        })

    def admiral(self):
        return self.__admiral

    def general(self):
        return self.__general
