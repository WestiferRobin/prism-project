from src.models.reaction import Reaction


class ReactionUnbalanceException(Exception):
    def __init__(self, reaction: Reaction):
        super().__init__(f"{reaction} is not balanced. check solution")
