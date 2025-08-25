from enum import Enum

class DroneType(int, Enum):
    GPT = 0,
    PRISM = 1,


class AppType(int, Enum):
    Scribe = 0 # Mobile notebook with prism-forge as lite-version
    Lab = 0 # Simulation with Physics, Chemistry, Biology, and Engineering with Prism Drones in a Legion for Trade and War Projects in Legion Market
    Game = 1 # Simulation Legion vs Legion War in 2D Unity in a Galaxy Map of PrismDrones on Planets around Suns
    Studio = 2 # Books into Faceless Channels per Drone on Legion Network Team for Wisdom and Knowledge
    Forge = 3 # Automation Productivity for gpt-drone/prism-drone experience as Docs, Sheets, Scripts, Projects (github, gitlabs, office, google-drive all with chat-gpt with drone-bot)


class PlatformType(int, Enum):
    Terminal = 0 # ASCII Terminal of any AppType
    Web = 1 # React with Terminal as Game, Forge,
    Mobile = 2 # Unity and React Native as Game and CookBook
    VR = 3 # Unreal with C++ and Bots with C and Python and Assembly with GPUs and CPUs in Optimizations


class SubscriptionTier(float, Enum):
    Free = 0 # 1 Drone on prism-site as gpt and market place with model-api
    Basic = 10 # 3 Drone on prism-site with prism-cook and prism-labs
    Standard = 15 # 6 Drones on prism-site with prism-labs and prism-conquest simulations
    Premium = 25 # 9 Drones on prism-site with prism-studio for youtube, twitter, instagram with content media with 3d models
    God = 50 # 12 Drones with all apps and api usage with models on market-place

