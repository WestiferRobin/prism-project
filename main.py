from simulations.main_simulation import run_simulation

if __name__ == "__main__":
    lab_versions = {
        0: (0,)
    }
    for version in lab_versions:
        for sub_version in lab_versions[version]:
            run_simulation(version, sub_version)
