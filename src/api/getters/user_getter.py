from src.utils.constants import AVATAR_ID


def get_mvp_users() -> User:
    return [
        User(config=build_wes_config(), user_id=AVATAR_ID),
        User(config=build_emma_config()),
        User(config=build_mary_config()),
        User(config=build_max_config())
    ]

