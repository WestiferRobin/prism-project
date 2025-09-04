
# Environments for AWS deployments and rapid development in order
DEBUG_VERSION = 0 # beta version
DEV_VERSION = DEBUG_VERSION + 1 # alpha version
TEST_VERSION = DEBUG_VERSION + 2 # lambda version
PROD_VERSION = DEBUG_VERSION + 3 # gamma version
FINAL_VERSION = DEBUG_VERSION + 4 # omega version

MVP_VERSIONS = [
    DEBUG_VERSION,
    DEV_VERSION,
    TEST_VERSION,
    PROD_VERSION,
    FINAL_VERSION
]
