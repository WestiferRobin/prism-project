from typing import cast

from src.exceptions import EngineException
from src.models import Model
from src.models.vehicles import Speeder, Shuttle


def print_speeder(speeder: Speeder) -> None:
    print(f"We're ready for the Speeder! {speeder.name}")


def print_shuttle(shuttle: Shuttle) -> None:
    print(f"We're ready for the Speeder! {shuttle.name}")


def print_model(model: Model) -> None:
    try:
        if isinstance(model, Speeder):
            print_speeder(cast(Speeder, model))
        elif isinstance(model, Shuttle):
            print_shuttle(cast(Shuttle, model))
        else:
            raise EngineException(f"{model.name} isn't a valid model to simulate")
    except EngineException as ex:
        print(ex)

