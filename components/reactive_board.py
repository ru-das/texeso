from textual.app import ComposeResult
from textual.containers import Grid
from textual.reactive import reactive
from .card import Card


class ReactiveBoard(Grid):
    """ A Dummy Board to be shown during the Game Setup """

    DEFAULT_CSS = """
    ReactiveBoard {
        padding-bottom: 1;
        padding-right: 1;
        background: #1f1d2e;
    }
    """

    # To keep tracks of the rows and columns settings
    setrows = reactive(4, recompose=True)
    setcols = reactive(4, recompose=True)

    # Sets the Grid proprties
    def on_mount(self) -> None:
        self.styles.grid_size_rows = int(self.setrows)
        self.styles.grid_size_columns = int(self.setcols)
        self.styles.grid_rows = "1fr"
        self.styles.grid_columns = "1fr"

    # Shows the blank cards for visual purposes
    def compose(self) -> ComposeResult:
        for i in range(int(self.setcols)):
            for j in range(int(self.setrows)):
                yield Card("", i, j, int(self.setcols))

    # Changes the Grid rows if the row settings changes
    def watch_setrows(self, setrows_value):
        self.on_mount()

    # Changes the Grid columns if the row settings changes
    def watch_setcols(self, setcols_value):
        self.on_mount()