from src.app.tools import Tool
from utils.validators.app_validators import validate_app


def validate_tool(tool: Tool):
    assert isinstance(tool, Tool)

    validate_app(tool, )
