from utils.validators.config_validators.net_configs import validate_net_config
from src.prism_net import PrismNet


def validate_prism_net(source_net: PrismNet, target_net: PrismNet) -> None:
    assert source_net is not None
    assert isinstance(source_net, PrismNet)
    validate_net_config(
        source_config=source_net.config,
        target_config=target_net.config,
    )



