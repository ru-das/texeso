from textual.app import ComposeResult
from textual.widgets import Static, Button, Label, MarkdownViewer
from textual.containers import Center, Horizontal, Container
from textual.screen import ModalScreen


HELP_TEXT = """
```
▗▖ ▗▖▗▄▄▄▖▗▖   ▗▄▄▖
▐▌ ▐▌▐▌   ▐▌   ▐▌ ▐▌
▐▛▀▜▌▐▛▀▀▘▐▌   ▐▛▀▘
▐▌ ▐▌▐▙▄▄▖▐▙▄▄▖▐▌
```

Welcome to **TEXESO**, a terminal implementaion of the famous memory game, *Pexeso*!!


## Objective

Flip over cards and try to **find matching pairs**.
Once all pairs are found, you **win the game**!

---
## How to Play

1. **Select Your Layout**
    - You can start by playing with the default **4 x 4 Layout**, having a total of *8 Matching Pairs*.
    - You can change the **Layout** , to *increase or decrease the difficulty*, as per your choice.

2. **Start the Game**
   - The cards are laid out face-down in a grid.
   - Each card has a matching pair hidden somewhere on the board.

3. **Flip Two Cards**
   - Click or tap a card to reveal it.
   - Then, flip a second card to see if it matches the first.

3. **Check for a Match**
   - **If the cards match:** they remain face-up.
   - **If they don’t match:** both cards flip back after a short delay — try to remember their positions!

4. **Continue Playing**
   - Keep flipping cards and remembering positions until you’ve matched all pairs.

---
## Game End

- The game ends when **all pairs are found**.
"""


class HelpScreen(ModalScreen):
    """ A Simple Help Screen """

    DEFAULT_CSS = """
    HelpScreen {
        align: center middle;
        content-align: center middle;
    }

    #help_scr {
        width: 75%;
        height: auto;
        background: #120f1a;
        outline: thick #120f1a 70%;
    }

    Button {
        border: none;
        min-width: 100%;
    }

    """

    BINDINGS = [
        ("o", "app.pop_screen()", "Okay")
    ]

    # Shows the HELP_TEXT, along with an "OKAY" Button
    def compose(self) -> ComposeResult:
        with Container(id="help_scr"):
            yield MarkdownViewer(HELP_TEXT, show_table_of_contents = False, open_links= False)
            yield Button("(O)KAY", variant="primary", id="okay")

    # To quit the screen when the "OKAY" Button is pressed
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "okay":
            self.app.pop_screen()

