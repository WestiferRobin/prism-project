from uuid import UUID


def configure_user_id(token: chr) -> UUID:
    user_id = UUID('xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'.replace('x', token))
    return user_id

