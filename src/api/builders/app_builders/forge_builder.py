

def build_forge(config: ForgeConfig) -> Forge:
    return Forge(config=config)


def build_prism_forge(platform: PlatformType = PlatformType.Web, version: int = 0) -> Lab:
    config = build_tool_config(
        version=version,
        tool_name="Prism Forge",
        tool_alias="prism-forge",
        platform=platform,
    )
    return build_forge(config=config)

