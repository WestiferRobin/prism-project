from uuid import UUID, uuid4
from src.utils.configs.net_config import NetConfig


def build_net_config(version: int, net_id: UUID = None) -> NetConfig:
    if net_id is None:
        net_id = uuid4()
    return NetConfig(
        version=version,
        config_id=net_id
    )

