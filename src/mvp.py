from pydantic import BaseModel


class PrismMvp(BaseModel):
    version: int

    legion_drone: Prism
    legion_speeder: Speeder
    legion_shuttle: Shuttle
    arch_legion: Legion

    solar_conquest: Game
    nexus_labs: Tool

    prism_forge: App
    prism_studio: App
    prism_hive: App

