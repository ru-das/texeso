from textual.app import App, ComposeResult
from random import shuffle
from components.card import Card
from components.reactive_board import ReactiveBoard


class Texeso(App):
    """ A Textual App implementation of the Pexeso game """

    def on_mount(self) -> None:
        # Importing inside this function to prevent cirular imports
        from screens.main_screen import MainScreen
        from screens.setup_screen import SetupScreen
        from screens.quit_screen import QuitScreen
        from screens.end_screen import EndScreen
        from screens.help_screen import HelpScreen
        # Installing the screens to use them later easily
        self.install_screen(MainScreen(), name="main")
        self.install_screen(SetupScreen(), name="setup")
        self.install_screen(QuitScreen(), name="quit")
        self.install_screen(EndScreen(), name="end")
        self.install_screen(HelpScreen(), name="help")
        # Displaying the MainScreen from start
        self.push_screen("main")

    def compose(self) -> ComposeResult:
        # To provide a background
        # The screen seemed empty with the MainScreen only
        yield ReactiveBoard()


# To run the Textual App
def main() -> None:
    game = Texeso()
    game.run()


# To create the matrix for the grid of numbers to be displayed on the game
def create_matrix(rows: int, cols: int) -> list:
    if ((rows * cols) % 2) != 0:
        raise ValueError("rows * cols must be even")
    matrix = []
    array = [i for i in range((rows*cols)//2)]*2
    shuffle(array)
    for i in range(0, rows*cols, cols):
        matrix.append(array[i:(i+cols)])
    return matrix


# To determine if two Cards match or not
def is_match(card1: Card, card2: Card) -> bool:
    # If the same card is clicked, it does not match
    # The two cards must be unique
    if card1.card_id != card2.card_id:
        value1 = card1.card_value
        value2 = card2.card_value
        if value1 == value2:
            return True
        else:
            return False
    else:
        return False


# To determine if the game should end
def is_game_end(total_matches: int, max_matches: int) -> bool:
    if max_matches < total_matches:
        raise ValueError(
            "total_matches must be less than or equal to max_matches, not greater"
        )
    if total_matches == max_matches:
        return True
    else:
        return False


# Calls the main function when the file is runned directly
if __name__ == "__main__":
    main()
