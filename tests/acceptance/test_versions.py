from acceptance.test_users import test_wes_black, test_emma_cyan, test_mary_gold, test_max_red, test_tyler_green, \
    test_payton_white
from unit.test_mvp import test_dev_version, test_demo_version


def test_initial_version(version: int = 0):
    test_wes_black(version=version) # labs, game
    test_mary_gold(version=version) # cook, studio


def test_alpha_version(version: int = 1):
    test_emma_cyan(version=version) # cook, labs
    test_max_red(version=version) # game, studio


def test_beta_version(version: int = 2):
    test_alpha_version(version=version)

    test_tyler_green(version=version) # game, studio
    test_payton_white(version=version) # game, studio
    test_brian_grey(version=version) # cook, labs


def test_final_version(version: int = 3):
    test_beta_version(version=version)
    test_dev_version()
    test_demo_version()
    test_final_version(version=version)
