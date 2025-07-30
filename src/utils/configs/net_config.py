from src.utils.configs import Config


class NetConfig(Config):
    def __init__(self, **net_data):
        super().__init__(name="Prism.net", alias="prism_config-net", **net_data)

