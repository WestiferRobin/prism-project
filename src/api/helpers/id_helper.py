from uuid import UUID

from src.utils.constants import ID_TEMPLATE


def create_user_id(token: chr) -> UUID:
    user_id = UUID(ID_TEMPLATE.replace('x', token))
    return user_id

