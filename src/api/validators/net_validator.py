from src.api.builders.config_builders import build_net_config
from src.prism_net import PrismNet


def validate_prism_net(net: PrismNet, mvp_version: int) -> None:
    assert isinstance(net, PrismNet)
    assert net.version == mvp_version

    expected_config = build_net_config(
        version=mvp_version,
        net_id=net.id,
    )
    validate_net_config(config=net.config, expected_config=expected_config)

    if net.version == 0:



