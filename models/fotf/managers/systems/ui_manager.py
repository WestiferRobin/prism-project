
class UIManager:
    def __init__(self):
        self.panels = {}
        self.active_panel = None

    def toggle_panel(self, panel_name):
        if self.active_panel == panel_name:
            self.active_panel = None
        else:
            self.active_panel = panel_name

    def draw(self, screen):
        # Draw UI overlays or panels
        pass

