from textual.app import ComposeResult
from textual.containers import Grid
from textual.message import Message
from textual.reactive import reactive
from asyncio import sleep
from .card import Card
from project import create_matrix, is_match, is_game_end


class GameBoard(Grid):
    """ The Board to display all the Cards """

    DEFAULT_CSS = """
    GameBoard {
        padding-bottom: 1;
        padding-right: 1;
        background: #1f1d2e;

        &.-enabled {
            opacity: 1;
        }

        &.-disabled {
            opacity: 0.5;
        }
    }
    """
    
    # To keep track of total moves and matches
    total_moves = reactive(0)
    total_matches = reactive(0)

    class MovesChanged(Message):
        """ Message to be sent when the total_moves changes """
        def __init__(self, total_moves: int):
            self.moves = total_moves
            super().__init__()

    class MatchesChanged(Message):
        """ Message to be sent when the total_matches changes """
        def __init__(self, total_matches: int):
            self.matches = total_matches
            super().__init__()

    class GameOver(Message):
        """ Message to be sent when the Game is Over """
        pass

    def __init__(self, rows: int = 4, cols: int = 4) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix = create_matrix(self.rows, self.cols)
        self.card1 = None # To store the first selected Card
        self.card2 = None # To store thr second selected Card
        super().__init__()

    # To define the style of the Grid
    def on_mount(self) -> None:
        # Defining them in DEFAULT_CSS or an individual .tcss won't work
        # because the number rows and columns are not some constants
        self.styles.grid_size_rows = self.rows
        self.styles.grid_size_columns = self.cols
        self.styles.grid_rows = "1fr"
        self.styles.grid_columns = "1fr"

    # To show the Cards
    def compose(self) -> ComposeResult:
        for i in range(self.rows):
            for j in range(self.cols):
                yield Card(self.matrix[i][j], i, j, self.cols)

    # Sends a message whenever the total_moves changes
    def watch_total_moves(self, total_moves: int) -> str:
        self.post_message(self.MovesChanged(total_moves))

    # Sends a message whenever the total_matches changes
    def watch_total_matches(self, total_matches: int) -> str:
        self.post_message(self.MatchesChanged(total_matches))

    # Disables any click on the board, for when the Game is paused
    def disable_board(self) -> None:
        for card in self.query(Card):
            card.noclick = True
        self.remove_class("-enabled")
        self.add_class("-disabled")

    # Enables back the click on the board
    def enable_board(self) -> None:
        for card in self.query(Card):
            card.noclick = False
        self.remove_class("-disabled")
        self.add_class("-enabled")

    # Checks if two selected cards matches or not
    async def action_match(self) -> None:
        if is_match(self.card1, self.card2):
            # Visually changes the Cards if matched
            self.card1.is_matched = True
            self.card2.is_matched = True
            await self.card1.matched()
            await self.card2.matched()
            self.total_matches += 1
        else:
            # Hides the Cards if not matched
            await sleep(0.5)
            self.card1.hide()
            self.card2.hide()
        self.total_moves += 1
        self.card1 = None
        self.card2 = None

    # Stores the first and second selected Card, and matches them
    # After the final match is done, the Game ends
    async def on_card_selected(self, message: Card.Selected) -> None:
        if self.card1 == None:
            self.card1 = message.card
        else:
            self.card2 = message.card
            await self.action_match()
            if is_game_end(self.total_matches, self.rows*self.cols//2):
                self.post_message(self.GameOver())