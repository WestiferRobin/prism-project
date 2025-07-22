from src.app.models.app_models.unit import Unit


class Mass(Unit):
    def __init__(self, **mass_data):
        super().__init__(**mass_data)

