
class AtomNotFound(Exception):
    def __init__(self, message):
        super().__init__(f"Atom '{message}' wasn't found in Periodic Table")
