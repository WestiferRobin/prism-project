
class UnitManager:
    def __init__(self, units=None, speed=0.125):
        self.units = units or []
        self.unit_speed = speed
        self.unit_targets = {}

    def update_units(self):
        for i, unit in enumerate(self.units):
            target = self.unit_targets.get(i)
            if target:
                dx = target[0] - unit[0]
                dy = target[1] - unit[1]
                dist = (dx**2 + dy**2) ** 0.5
                if dist < self.unit_speed:
                    self.units[i] = target
                    del self.unit_targets[i]
                else:
                    self.units[i][0] += self.unit_speed * dx / dist
                    self.units[i][1] += self.unit_speed * dy / dist

    def set_target_for_selected(self, selected_unit_indexes, target_pos):
        for i in selected_unit_indexes:
            self.unit_targets[i] = target_pos

    def is_selected(self, index, selection_manager):
        return selection_manager.is_selected(index)
