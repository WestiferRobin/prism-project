from src.api.builders.config_builders.app_configs import  build_tool_config
from src.app.tool import Tool
from src.utils.configs.app_configs.tool_config import ToolConfig
from src.utils.enums.platform_enums import PlatformType


def build_tool(config: ToolConfig) -> Tool:
    return Tool(config=config)


def build_prism_lab(platform: PlatformType = PlatformType.Web, version: int = 0) -> Tool:
    config = build_tool_config(
        version=version,
        tool_name="Prism Lab",
        tool_alias="prism-lab",
        platform=platform,
    )
    return build_tool(config=config)


def build_prism_forge(platform: PlatformType = PlatformType.Web, version: int = 0) -> Tool:
    config = build_tool_config(
        version=version,
        tool_name="Prism Forge",
        tool_alias="prism-forge",
        platform=platform,
    )
    return build_tool(config=config)


def build_prism_studio(platform: PlatformType = PlatformType.Web, version: int = 0) -> Tool:
    config = build_tool_config(
        version=version,
        tool_name="Prism Studio",
        tool_alias="prism-studio",
        platform=platform,
    )
    return build_tool(config=config)

