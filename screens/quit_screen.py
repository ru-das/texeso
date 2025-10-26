from textual.app import ComposeResult
from textual.widgets import Static, Button, Label
from textual.containers import Center, Horizontal, Container
from textual.screen import ModalScreen


class QuitScreen(ModalScreen):
    """ A Confirmation Dialouge to Quit the Game """

    DEFAULT_CSS = """
    QuitScreen {
        align: center middle;
        content-align: center middle;
    }

    #quit_scr {
        width: 75;
        height: auto;
        padding: 4 4;
        background: #120f1a;
        outline: thick #120f1a 70%;
    }

    Label {
        margin-bottom: 2;
    }

    Horizontal {
        width: auto;
        height: auto;
    }

    Button {
        margin-left: 5;

        &#yes {
            margin-left: 0;
        }
    }
    """

    BINDINGS = [
        ("y", "app.quit", "Quit"),
        ("q", "app.quit", "Quit"),
        ("n", "app.pop_screen()", "Cancel")
    ]

    # To display the visual elements
    def compose(self) -> ComposeResult:
        with Container(id="quit_scr"):
            with Center():
                yield Label("Are you SURE you want to QUIT?")
            with Center():
                with Horizontal():
                    yield Button("(Y)es", id="yes", variant="success")
                    yield Button("(N)o", id="no", variant="primary")

    # Handles the "Yes" or "No" Button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.app.exit()
        else:
            self.app.pop_screen()
