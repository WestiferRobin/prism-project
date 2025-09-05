

def build_lab(config: LabConfig) -> Lab:
    return Lab(config=config)


def build_prism_lab(platform: PlatformType = PlatformType.Web, version: int = 0) -> Lab:
    config = build_tool_config(
        version=version,
        tool_name="Prism Lab",
        tool_alias="prism-lab",
        platform=platform,
    )
    return build_tool(config=config)

