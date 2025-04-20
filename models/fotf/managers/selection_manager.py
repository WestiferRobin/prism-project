import pygame


class SelectionManager:
    def __init__(self):
        self.selected_unit_indexes = []
        self.selection_box = None
        self.drag_start = None

    def start_selection(self, start_pos):
        self.drag_start = start_pos
        self.selection_box = pygame.Rect(start_pos, (0, 0))

    def update_selection(self, current_pos):
        if self.drag_start:
            x1, y1 = self.drag_start
            x2, y2 = current_pos
            self.selection_box = pygame.Rect(
                min(x1, x2), min(y1, y2),
                abs(x2 - x1), abs(y2 - y1)
            )

    def finalize_selection(self, unit_manager):
        self.selected_unit_indexes.clear()
        if self.selection_box:
            for i, unit in enumerate(unit_manager.units):
                unit_rect = pygame.Rect(unit[0] * 32, unit[1] * 32, 32, 32)
                if self.selection_box.colliderect(unit_rect):
                    self.selected_unit_indexes.append(i)
        self.selection_box = None
        self.drag_start = None

    def is_selected(self, unit_index):
        return unit_index in self.selected_unit_indexes

