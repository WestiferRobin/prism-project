from src import PrismNet


def build_prism_net(version: int) -> PrismNet:
    return PrismNet(version=version)


def build_mvp(version: int) -> PrismNet:
    mvp = build_prism_net(version=version)
    return mvp

