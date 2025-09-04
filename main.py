from src.api.builders.company_builder import build_prism_co
from src.api.builders.config_builders.user_configs.wes_config import build_wes_config
from src.utils.constants import DEBUG_VERSION, DEV_VERSION, TEST_VERSION, PROD_VERSION, FINAL_VERSION

if __name__ == '__main__':
    mvp_version = DEBUG_VERSION
    prism_co = build_prism_co(
        version=mvp_version,
        leader_config=build_wes_config(version=mvp_version)
    )
    # print(prism_co)


    if mvp_version == DEBUG_VERSION:
        prism_co.run_game() # For PrismLLM model linked with prism-drone
    elif mvp_version == DEV_VERSION:
        prism_co.run_studio() # Media content generator using ai-agents as lite-drones or prism-drones
    elif mvp_version == TEST_VERSION:
        prism_co.run_hive() # Company site and marketplace of prism-drones linked to drive and studio
    elif mvp_version == PROD_VERSION:
        prism_co.run_labs() # Build LogoLLM, SilverOrb, Computation Experiments, etc in a vscode, notebook, and stem paradine
    elif mvp_version == FINAL_VERSION:
        prism_co.run_forge() # Google Drive and Microsoft Office with ChatGPT linked with prism-apps


