from pydantic import BaseModel

from src.utils.enums.platform_enums import PlatformType


class Platform(BaseModel):
    type: PlatformType

