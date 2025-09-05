from src.models.app import Tool
from src.api.validators.app_validators import validate_app


def validate_tool(tool: Tool):
    assert isinstance(tool, Tool)

    validate_app(tool, )
