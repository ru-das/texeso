from textual.widgets import Digits
from textual.message import Message
from functools import partial


# Didn't used the Button Widget because they don't seem to work so well
# (and tweaking was harder than to make something similar from scratch)
class Card(Digits):
    """ Individual Cards of the Game """

    DEFAULT_CSS = """
    Card {
        background: #26233a;
        margin-left: 1;
        margin-top: 1;
        width: 100%;
        height: 100%;
        text-align: center;
        content-align: center middle;


        &.-unmatched {
            background: #26233a;
            outline-top: tall #524f67;
            outline-bottom: tall #191724;

            &:hover {
                background: #26233a 50%
            }

            &.-active {
                background: #26233a 10%;
                outline-bottom: none;
                outline-top: tall #191724;
            }
        }

        &.-matched {
            background: #eb6f92;
            outline-top: tall #f6c0cd;
            outline-bottom: tall #b4637a;

            &:hover {
                background: #eb6f92 80%
            }
        }
    }
    """

    class Selected(Message):
        """ Message to be sent when a Card is Selected """

        def __init__(self, card: "Card") -> None:
            self.card = card
            super().__init__()

    def __init__(self, card_value, row_id, col_id, order) -> None:
        self.card_value = card_value
        self.card_id = ((row_id - 1)*order)+col_id # Make each card unique
        self.hidden_value = " "
        self.is_selected = False
        self.is_matched = False
        self.noclick = False
        super().__init__()
        self.expand = True

    def on_mount(self) -> None:
        self.add_class("-unmatched")
        self.update(f"{self.hidden_value}")

    # Reveals the Card's value when clicked / selected
    def reveal(self) -> None:
        self.is_selected = True
        self.update(f"{self.card_value}")

    # Hides the Cards' value if the two selected Cards does not match
    def hide(self) -> None:
        self.is_selected = False
        self.update(f"{self.hidden_value}")

    # Changes the look of the matched Cards
    async def matched(self) -> None:
        if self.is_matched:
            self.remove_class("-unmatched")
            self.add_class("-matched")
            self.refresh(layout=True, repaint=True)

    # To imitate the behaviour of a Button
    def press_animation(self) -> None:
        self.add_class("-active")
        self.set_timer(0.2, partial(self.remove_class, "-active"))

    # To compute what happens when the Card is clicked
    async def on_click(self) -> None:
        # If not disabled
        if not self.noclick:
            # If not matched
            if not self.is_matched:
                # If not already selected
                if not self.is_selected:
                    self.press_animation()
                    self.reveal()
                    self.post_message(self.Selected(self))
            else:
                pass # Removing this seemed to broke the Game
        else:
            pass # Removing this seemed to broke the Game
