from src.models.equations.mass import Mass


def verify_mass(mass: Mass) -> bool:
    try:
        assert mass is not None
        assert type(mass) is Mass
    except:
        return False

    return True

