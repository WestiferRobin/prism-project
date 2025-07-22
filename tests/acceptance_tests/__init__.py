from api.builders import build_prism_drone, build_arch_legion, build_solar_conquest, build_nexus_labs, build_prism_forge
from utils.version import Version


def test_prism_drone(version: Version):
    prism_drone = build_prism_drone(version)
    validate_prism_drone(prism_drone)


def test_arch_legion(version: Version):
    arch_legion = build_arch_legion(version)
    validate_arch_legion(arch_legion)


def test_solar_conquest(version: Version):
    solar_conquest = build_solar_conquest(version)
    validate_solar_conquest(solar_conquest)


def test_nexus_labs(version: Version):
    nexus_labs = build_nexus_labs(version)
    validate_nexus_labs(nexus_labs)


def test_prism_forge(version: Version):
    prism_forge = build_prism_forge(version)
    validate_prism_forge(prism_forge)


def test_prism_co(version: Version):
    test_arch_legion(version)
    test_solar_conquest(version)
    test_nexus_labs(version)
    test_prism_forge(version)
    test_prism_drone(version)

