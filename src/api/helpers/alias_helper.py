

def create_alias(name: str) -> str:
    lower_name = name.lower()
    alias = lower_name.replace(" ", "-")
    return alias

