from src.api.services.user_service import get_users
from src.utils.constants import DEBUG_VERSION

if __name__ == '__main__':
    mvp_version = DEBUG_VERSION
    mvp_users = get_users(version=mvp_version)
    # mvp_apps = get_apps(version=mvp_version)
    # mvp_bots = get_bots(version=mvp_version)
    # mvp = build_mvp(
    #     version=mvp_version,
    #     users=mvp_users,
    #     apps=mvp_apps,
    #     bots=mvp_bots
    # )
    # print(mvp)

