from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button, Static
from textual.containers import Horizontal, Center, Container
from components.reactive_board import ReactiveBoard
from components.steppers import RowStepper, ColumnStepper
from .game_screen import GameScreen


SETUP_TITLE = """
 ▗▄▄▖▗▄▄▄▖▗▄▄▄▖▗▖ ▗▖▗▄▄▖ 
▐▌   ▐▌     █  ▐▌ ▐▌▐▌ ▐▌
 ▝▀▚▖▐▛▀▀▘  █  ▐▌ ▐▌▐▛▀▘ 
▗▄▄▞▘▐▙▄▄▖  █  ▝▚▄▞▘▐▌   
"""


class SetupScreen(Screen):
    """ A Screen to set the Rows and Columns of the Game """

    DEFAULT_CSS = """
    SetupScreen {
        content-align: center middle;
    }

    #sidebar {
        dock: left;
        width: 25%;
        background: #214d5f;
        align: center middle;
    }

    #title {
        text-align: center;
        content-align: center middle;
        margin-bottom: 2;
    }

    #start {
        margin-bottom: 1;
    }

    """

    BINDINGS = [
        ("b", "app.switch_screen('main')", "Back"),
        ("h", "app.push_screen('help')", "Help"),
        ("?", "app.push_screen('help')", "Help"),
    ]

    # To display the visual elements
    def compose(self) -> ComposeResult:
        with Horizontal():
            with Container(id="sidebar"):
                with Center():
                    yield Static(SETUP_TITLE, id="title")
                with Center():
                    yield RowStepper()
                with Center():
                    yield ColumnStepper()
                with Center():
                    yield Button("START", id="start")
                with Center():
                    yield Button("(q) BACK", id="back")

            yield ReactiveBoard()

    # Passes the current value of rows from RowStepper to the ReactiveBoard
    def on_row_stepper_changed(self, message: RowStepper.Changed) -> None:
        self.query_one(ReactiveBoard).setrows = message.value

    # Passes the value of columns from ColumnStepper to the ReactiveBoard
    def on_column_stepper_changed(self, message: ColumnStepper.Changed) -> None:
        self.query_one(ReactiveBoard).setcols = message.value

    # Handles the "START" or "BACK" Button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.switch_screen("main")
        elif event.button.id == "start":
            self.app.switch_screen(
                GameScreen(
                    int(self.query_one(ReactiveBoard).setrows),
                    int(self.query_one(ReactiveBoard).setcols)
                )
            )
