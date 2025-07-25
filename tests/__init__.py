from src.utils.constants import DEV_VERSION, DEMO_VERSION, FINAL_VERSION

def test_dev_version():
    # Always cooking out features
    prism_net = build_prism_net(version=DEV_VERSION)
    validate_mvp(prism_net)


def test_demo_version():
    # If here we go to deployment mode
    prism_net = build_prism_net(version=DEMO_VERSION)
    validate_mvp(prism_net)


def test_final_version():
    # Do official deployment with release strategy
    prism_net = build_prism_net(version=FINAL_VERSION)
    validate_mvp(prism_net)

