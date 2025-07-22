# TODO(s)

- finish unit tests with mvc design on simulation as an engine-service 
  - Goal: Take any request and perform data and business requirements
  - Final: Full testing
    - unit: src
      - api
      - controller
      - service
      - view
- finish unit tests and project setup for fast-api, gpt-api, and torch/prism-api



## Backlog
- Implement a valid cleanup strategy:
  - update current prism-docs to be cleared
  - will start with following in prism-docs
    - README.md on how to operate PrismCo as a machine
    - TODO.md
      - First: Await B Grade from lab-engine-service
      - Final: Scripts to create PrismCo with Web and Template repos
        - FastAPI => Some Python API => Platform Service for integration, experimental, ai
        - SpringBoot => Some Java API => App Service for integration, performant, modular
        - Unity => Some C# API => Game Service for Unity Game Model with .obj and blender support 
        - React => Some TS API => UI Component with server support
        - Unreal => Some C++ API => AI Movie with .wav and .mp4 with FL, GarageBand, Notation, Audio Waves
  - clean up enums for those using (str, Enum) vs (Enum) vs (object, Enum) for all cases
  - rename mood to studio and rename nexus-lab-engine to lab-engine-service
  - Move Solar Conquest to solar-conquest-proto repo by test_solar_conquest
  - Make new branch "feature/official-draft" and merge into master
  - README.md has setup template from prism-docs
  - README.md is polished for lab-engine-service
- AC:
  - nexus-lab-engine and company-site with company-service and site-service are on aws
  - dev environment is Tier Iron and has Grade A
  - test environment is Tier Silver and has Grade A
  - prod environment is Tier Gold and has Grade A
  - Note: assume bi-weekley deployments
  
