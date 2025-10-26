from textual import work
from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.containers import Center, Horizontal, Container
from textual.screen import ModalScreen
from components.title import Title


class MainScreen(ModalScreen):
    """ The Default Screen to be shown in the beginning """

    DEFAULT_CSS = """
    MainScreen {
        align: center middle;
        content-align: center middle;
    }

    #main_scr {
        width: 110;
        height: 20;
        padding-top: 4;
        padding-left: 5;
        padding-right: 5;
        background: #120f1a;
        outline: thick #120f1a 70%;
    }

    Title {
        margin-bottom: 2;
    }

    Horizontal {
        width: auto;
        height: auto;
    }

    Button {
        margin-left: 5;

        &.-first {
            margin-left: 0;
        }
    }

    #quit_game {
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
    """

    BINDINGS = [
        ("+", "app.switch_screen('setup')", "New Game"),
        ("q", "app.push_screen('quit')", "Quit"),
        ("?", "app.push_screen('help')", "Help"),
        ("h", "app.push_screen('help')", "Help"),
    ]

    # Shows the fancy "TEXESO" title, along with other buttons
    def compose(self) -> ComposeResult:
        with Container(id="main_scr"):
            with Center():
                yield Title()
            with Center():
                with Horizontal():
                    yield Button("(+) NEW GAME", id="new_game", classes="-first", variant="success")
                    yield Button("(q) QUIT", id="quit_game", classes="-quit", variant="error")
                    yield Button("(?) HELP", id="help", variant="warning")

    # Handles the different button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "new_game":
            # Shows the Game Setup Screen
            self.app.switch_screen("setup")
        elif event.button.id == "quit_game":
            # Shows a confirmation dialouge to quit the Game
            self.app.push_screen("quit")
        elif event.button.id == "help":
            # Shows the Help Text
            self.app.push_screen("help")