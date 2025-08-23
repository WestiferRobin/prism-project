from src.api.builders.app_builders.tool_builders import build_prism_lab
from src.utils.constants import DEBUG_VERSION
from utils.validators.app_validators import validate_app


def test_prism_lab(version: int = DEBUG_VERSION):
    prism_lab = build_prism_lab(version=version)
    expected_app = build_prism_lab(version=version)
    validate_app(app=prism_lab, expected_app=expected_app)

