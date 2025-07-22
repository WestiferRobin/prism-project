from uuid import UUID


def build_droid(droid_id: UUID, name: str):
    return { "id": str(droid_id), "name": name }


def test_droid():

    droid = build_droid()

