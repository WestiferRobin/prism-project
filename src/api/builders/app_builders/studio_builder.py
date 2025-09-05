

def build_studio(config: StudioConfig) -> Studio:
    return Studio(config=config)



def build_prism_studio(platform: PlatformType = PlatformType.Web, version: int = 0) -> Lab:
    config = build_tool_config(
        version=version,
        tool_name="Prism Studio",
        tool_alias="prism-studio",
        platform=platform,
    )
    return build_studio(config=config)

