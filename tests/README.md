# Test Strategy: Acceptance Tests

- Idea:
  - Drone => Prism(GPT or Torch)
  - Legion => Drones, Speeders, Shuttles, Ships
  - Prism Conquest => Legion and LegionDrone
  - Prism Labs => Legion and PrismDrone
  - Prism Studio => Labs and Conquest
  - Prism Forge => Labs and Studio
  - Prism Hive => Forge

## MVP: Prism.net

mvp: prism.net (infrastructure to support drones, apps, and bots)

bots:
- hedron_server: 1 prism_drone in a server as a bot (ex. alexia with gpt)
- bot_drone: prism_drone in a bot blueprint data model (ex. droids)
- bot_speeder: prism_drone in a speeder blueprint data model (ex. uap)
- bot_legion: Wes uses a drone legion blueprint data model (ex. droids and uaps with ai and vr)

apps:
- web_apps: pc_apps
    - prism_hive: social media and market for drones and products for prism.net
    - prism_forge: literally Google Drive but with a twist
        - tools: can be used as separate repo as well (aka why docs on separate site due to repo?)
            - prism_lab: simulation tool for programing and computational experiments
                - build and deploy web-app
                - build and run cli-app
                - build and run lab-experiment
                - build and run table-experiment
            - prism_studio: media generation tool for books, comics, videos, music, samples, movies, shows, podcasts
                - text media
                - image media
                - audio media
                - video media
            - prism_scribe: literally word with gpt/drone
                - send pages to book
                - send outline to comic-book
                - send lyrics to song
                - send script to episode of video, show, and movie
            - prism_tables: literally excel with gpt/drone
- mobile_apps:
  - prism_cook: mobile app for cooking with drone
  - prism_reflect: mobile app for therapy with drone
  - prism_forge: lite version of prism_forge
    - prism_scribe
    - prism_tables
  - prism_hive: social media and market
    - has a bank of drones
    - has a feed and linked to all app accounts
    - has groups, messages, and media

games:
- solar_conquest: top-down management survival on pc and mobile
- fotf: pc and vr game of battlefront, valorant, and sw-squadrons
