from authentications.login import Login
from strategy.under2 import Under2
from config.config import MOBILE_NUMBER, PASSWORD
from controllers.game_controller import GameController
from config.settings import browser

class Main:
    def __init__(self) -> None:
        Login.login(MOBILE_NUMBER, PASSWORD)
        Login.start()
        GameController.get_all_teams()
        GameController.statistics()
        GameController.check_h2h(4)

        # return browser   

if __name__ == "__main__":
    Main()