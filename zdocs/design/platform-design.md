# Platform Idea: prism.net

- Goal: GPT, Nexus, and AI Tools integrated into everyday in productivity and play

## Design

- template repos with app, api, utils, and test including zdocs and dependencies
  - platform-service => FastAPI with JSON, Web, and XML support
  - app-service => SpringBoot and React with XHTML, Web, and JSON support
  - game-script => Unity and Unreal with Blender, GIMP, FL Support
  - platform-script => lives in prism-docs to be master library of all docs somehow including scripts

- platform-layer:
  - data-layer:
    - platform-user-service => Platform Users and Players
    - media-content-service => Results from content generation/import/export/deletion as Media Resource
    - platform-file-service => Results from content being imported and exported 
    - prism-drone-service => Where Prisms work
  - business-layer: goes by version for feature flag control of network
    - dev-layer:
      - version n - 2
    - test-layer:
      - version n - 1
    - production-layer:
      - version n 
    - infra-layer:
      - platform-notification-service => Notifications primarily for platform-layer
      - platform-auth-service => Proxy for platform to app and inner layer to layer
  - engine-layer:
    - lab-engine-service
    - studio-engine-service
    - forge-engine-service
- app-layer:
  - app-service:
    - lab-app-service
    - studio-app-service
    - scribe-app-service
    - tablet-app-service
    - forge-app-service
    - hive-app-service
  - apps:
    - game-apps:
      - solar-conquest for PC, Web, Mobile
      - fotf for PC, Mobile, VR
    - mobile-apps:
      - prism-todo lite version
      - prism-forge lite version
      - prism-hive lite version
    - web-apps:
      - prism-scribe with Prism and Word Interface
      - prism-forge with Prism and File Interface
      - prism-studio with Prism and Terminal Interface
      - prism-labs with Prism and Terminal Interface
      - prism-tablet with Prism and Excel Interface
      - prism-hive with Prism and Market Interface
    - bot-app: prism-app with API in C/C++, Python, and Java



