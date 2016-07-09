from src.pirate import Pirate


def create_app():
    pirate = Pirate()
    return pirate


app = create_app()
