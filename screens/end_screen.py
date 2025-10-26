from textual.app import ComposeResult
from textual.widgets import Static, Button, Label
from textual.containers import Center, Horizontal, Container
from textual.screen import ModalScreen


class EndScreen(ModalScreen):
    """ A Confirmation Dialouge to End the Ongoing Game """

    DEFAULT_CSS = """
    EndScreen {
        align: center middle;
        content-align: center middle;
    }

    #end_scr {
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
        ("y", ("app.pop_screen()", "app.switch_screen('main')"), "End"),
        ("q", "app.quit", "End"),
        ("n", "app.pop_screen()", "Cancel")
    ]

    # To display the visual elements
    def compose(self) -> ComposeResult:
        with Container(id="end_scr"):
            with Center():
                yield Label("Are you SURE you want to END the GAME?")
            with Center():
                with Horizontal():
                    yield Button("(Y)es", id="yes", variant="success")
                    yield Button("(N)o", id="no", variant="primary")

    # Handles the "Yes" or "No" Button presses
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.app.pop_screen()
            self.app.switch_screen("main")
        else:
            self.app.pop_screen()
