from utils.version import Version


def test_alpha_version():
    alpha_version = Version(number=1)
    test_prism_co(alpha_version)


