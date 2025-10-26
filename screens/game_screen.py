from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Button, Digits
from textual.containers import Horizontal, Center, Container, Grid
from components.game_board import GameBoard


GAME_TITLE = """
 ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖
▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌   
▐▌▝▜▌▐▛▀▜▌▐▌  ▐▌▐▛▀▀▘
▝▚▄▞▘▐▌ ▐▌▐▌  ▐▌▐▙▄▄▖
"""

OVER_TITLE = """
 ▗▄▖ ▗▖  ▗▖▗▄▄▄▖▗▄▄▖ 
▐▌ ▐▌▐▌  ▐▌▐▌   ▐▌ ▐▌
▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘▐▛▀▚▖
▝▚▄▞▘ ▝▚▞▘ ▐▙▄▄▖▐▌ ▐▌
"""


class GameScreen(Screen):
    DEFAULT_CSS = """
    #sidebar {
        dock: left;
        width: 25%;
        background: #68567a;
        align: center middle;

        &.-over {
            background: #907aa9;
        }
    }

    #title {
        text-align: center;
        content-align: center middle;
        margin-bottom: 2;
    }

    #moves, #matches {
        width: 80%;
        height: 6;
        grid-size: 1 2;
        grid-columns: 1fr;
        grid-rows: 1fr 5;
        margin-bottom: 2;
    }

    #moves_title, #matches_title {
        row-span: 1;
        column-span: 1;
        text-align: center;
        content-align: center middle;
        background: #524f67;
    }

    #moves_value, #matches_value {
        row-span: 1;
        column-span: 1;
        text-align: center;
        height: 5;
        background: #26233a;
        border-top: tall #26233a;
        border-bottom: tall #191724;
    }

    .new_game {
        color: $button-color-foreground;
        background: #5c9c85;
        border-top: tall #7fae9e;
        border-bottom: tall #234f42;

        &:hover {
            background: #3e826c;
            border-top: tall #5c9c85;
        }

        &.-active {
            background: #2f6a58;
            border-bottom: tall #7fae9e;
            border-top: tall #234f42;
        }
    }

    .end {
        color: $button-color-foreground;
        background: #990f02;
        border-top: tall #a91b0d;
        border-bottom: tall #420c09;

        &:hover {
            background: #710c04;
            border-top: tall #990f02;
        }

        &.-active {
            background: #610c04;
            border-bottom: tall #a91b0d;
            border-top: tall #420c09;
        }
    }

    Button {
        margin-bottom: 1;
    }
    """

    BINDINGS = [
        ("+", "app.switch_screen('setup')", "New Game"),
        ("q", "app.push_screen('end')", "End Game"),
        ("b", "app.switch_screen('main')", "Back"),
        ("h", "app.push_screen('help')", "Help"),
        ("?", "app.push_screen('help')", "Help"),
    ]

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        super().__init__()

    # To display the visual elements
    # The GameScreen is divided into two parts :-
    #     1. A Sidebar
    #     2. The GameBoard
    def compose(self) -> ComposeResult:
        with Horizontal():
            # The Sidebar
            with Container(id="sidebar"):
                with Center():
                    # To display a fancy title
                    yield Static(GAME_TITLE, id="title")
                with Center():
                    # To display the total number of moves made
                    with Grid(id="moves"):
                        yield Static("[b]TOTAL MOVES[/b]", id="moves_title")
                        yield Digits("0",id="moves_value")
                with Center():
                    # To display the total number of macthes made
                    with Grid(id="matches"):
                        yield Static("[b]TOTAL MATCHES[/b]", id="matches_title")
                        yield Digits("0",id="matches_value")
                with Center():
                    # To display a pause button to Pause the game
                    # This button also becomes the Resume button when the game is paused
                    # After the game is over, this button is used to start a new game
                    yield Button("PAUSE", classes="pause", variant = "primary")
                with Center():
                    # To display a button to end the current game and go back to the main screen
                    yield Button("(q) END GAME", classes="end", variant = "error")

            # The GameBoard
            yield GameBoard(self.rows, self.cols)

    # To change the total number of moves made
    def on_game_board_moves_changed(self, event: GameBoard.MovesChanged) -> None:
        self.query_one("#moves_value").update(str(event.moves))

    # To change the total number of matches made
    def on_game_board_matches_changed(self, event: GameBoard.MatchesChanged) -> None:
        self.query_one("#matches_value").update(str(event.matches))

    # To change some visual element when the game is over
    def on_game_board_game_over(self, event: GameBoard.GameOver) -> None:
        # Changes the fancy title from "GAME" to "OVER"
        self.query_one("#title").update(OVER_TITLE)
        # Changes the color of the sidebar to indicate the game is over
        self.query_one("#sidebar").add_class("-over")
        # Changes the "PAUSE" Button to "NEW GAME" Button
        self.query_one(".pause").toggle_class("new_game", "pause")
        self.query_one(".new_game").label = "(+) NEW GAME"
        self.query_one(".new_game").variant = "success"
        #Changes the "END GAME" Button to "BACK" Button
        self.query_one(".end").toggle_class("back", "end")
        self.query_one(".back").label = "(b) BACK"
        self.query_one(".back").variant = "default"

    # Handles the different button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.has_class("pause"):
            self.query_one(GameBoard).disable_board()
            event.button.toggle_class("resume", "pause")
            event.button.label = "RESUME"
        elif event.button.has_class("resume"):
            self.query_one(GameBoard).enable_board()
            event.button.toggle_class("pause", "resume")
            event.button.label = "PAUSE"
        elif event.button.has_class("new_game"):
            self.app.switch_screen("setup")
        elif event.button.has_class("end"):
            self.app.push_screen("end")
        elif event.button.has_class("back"):
            self.app.switch_screen("main")
