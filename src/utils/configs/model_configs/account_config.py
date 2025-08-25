from uuid import UUID

from src.utils.configs import Config
from src.utils.enums.platform_enums import SubscriptionTier


class AccountConfig(Config):
    sub_tier: SubscriptionTier

    @property
    def hour_cost(self) -> float:
        return self.day_cost / 24

    @property
    def day_cost(self) -> float:
        return self.week_cost / 7

    @property
    def week_cost(self) -> float:
        return self.month_cost / 4

    @property
    def month_cost(self) -> float:
        return self.sub_tier.value()

    @property
    def quarter_cost(self) -> float:
        return self.month_cost * 3

    @property
    def annual_cost(self) -> float:
        return self.quarter_cost * 4

    @property
    def user_id(self) -> UUID:
        return self.id

    @property
    def app_name(self) -> str:
        return self.name

    @property
    def app_alias(self) -> str:
        return self.alias

    def __init__(self,
        version: int,
        user_id: UUID,
        app_name: str,
        app_alias: str,
        sub_tier: SubscriptionTier
    ):
        super().__init__(
            version=version,
            config_id=user_id,
            name=app_name,
            alias=app_alias,
            sub_tier=sub_tier
        )

