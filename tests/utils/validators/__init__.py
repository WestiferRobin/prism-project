from utils.validators.net_validator import validate_prism_net
from src.prism_net import PrismNet


def validate_mvp(source_mvp: PrismNet, target_mvp: PrismNet):
    validate_prism_net(
        source_net=source_mvp,
        target_net=target_mvp,
    )

