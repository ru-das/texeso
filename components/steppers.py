from textual.app import ComposeResult
from textual.containers import Grid, Center
from textual.widgets import Digits, Button, Static
from textual.reactive import reactive
from textual.message import Message


class RowStepper(Grid):
    """ A Stepper to select the number of Rows in the Game """
    DEFAULT_CSS = """
    RowStepper {
        width: 80%;
        height: 6;
        grid-size: 3 2;
        grid-columns: 1fr;
        grid-rows: 1fr 5;
        margin-bottom: 2;
    }

    Static {
        column-span: 3;
        width: 100%;
        row-span: 1;
        text-align: center;
        content-align: center middle;
        background: #524f67;
    }

    Button {
        column-span: 1;
        row-span: 1;
        border: none;
        min-width: 100%;
        min-height: 5;
    }

    #display {
        column-span: 1;
        row-span: 1;
        text-align: center;
        height: 5;
        background: #26233a;
        border-top: tall #26233a;
        border-bottom: tall #191724;
    }
    """

    # To keep track of the new row value
    rows = reactive(4)
    # To keep track of the previous row value
    old_rows = reactive(0)

    class Changed(Message):
        """ Message to be sent when the number of Rows changes """

        def __init__(self, value: int) -> None:
            self.value = value
            super().__init__()

    # Fixes the value of rows, if (rows * columns) is not even
    # or if the rows is less than 2
    def validate_rows(self, rows: int) -> int:
        parent = self.query_ancestor("SetupScreen")
        cols = parent.query_one("ColumnStepper").cols

        if rows <= 2:
            return 2
        elif (rows*cols) % 2 != 0:
            if self.old_rows < rows:
                return rows + 1
            else:
                return rows - 1
        else:
            return rows

    # To display the visual elements
    def compose(self) -> ComposeResult:
        yield Static("[b]S E T   R O W S[/b]")
        yield Button("-",id = "subtract")
        yield Digits(id="display")
        yield Button("+", id = "add")

    # Increments or Decrements the row value accordingly
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.old_rows = self.rows
        if event.button.id == "add":
            self.rows += 1
        elif event.button.id == "subtract":
            self.rows -= 1

    # Sends a message whenever the row value changes
    def watch_rows(self, rows_value: int) -> None:
        self.query_one("#display").update(str(rows_value))
        self.post_message(self.Changed(rows_value))


class ColumnStepper(Grid):
    """ A Stepper to select the number of Columns in the Game """

    DEFAULT_CSS = """
    ColumnStepper {
        width: 80%;
        height: 6;
        grid-size: 3 2;
        grid-columns: 1fr;
        grid-rows: 1fr 5;
        margin-bottom: 2;
    }

    Static {
        column-span: 3;
        width: 100%;
        row-span: 1;
        text-align: center;
        content-align: center middle;
        background: #524f67;
    }

    Button {
        column-span: 1;
        row-span: 1;
        border: none;
        min-width: 100%;
        min-height: 5;
    }

    #display {
        column-span: 1;
        row-span: 1;
        text-align: center;
        height: 5;
        background: #26233a;
        border-top: tall #26233a;
        border-bottom: tall #191724;
    }
    """

    # To keep track of the new column value
    cols = reactive(4)
    # To keep track of the previous column value
    old_cols = reactive(0)

    class Changed(Message):
        """ Message to be sent when the number of Columns changes """

        def __init__(self, value: int) -> None:
            self.value = value
            super().__init__()

    # Fixes the value of columns, if (rows * columns) is not even
    # or if the columns is less than 2
    def validate_cols(self, cols: int) -> int:
        parent = self.query_ancestor("SetupScreen")
        rows = parent.query_one("RowStepper").rows

        if cols <= 2:
            return 2
        elif (rows*cols) % 2 != 0:
            if self.old_cols < cols:
                return cols + 1
            else:
                return cols - 1
        else:
            return cols

    # To display the visual elements
    def compose(self) -> ComposeResult:
        yield Static("[b]S E T   C O L U M N S[/b]")
        yield Button("-",id = "subtract")
        yield Digits(id= "display")
        yield Button("+", id = "add")

    # Increments or Decrements the column value accordingly
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.old_cols = self.cols
        if event.button.id == "add":
            self.cols += 1
        elif event.button.id == "subtract":
            self.cols -= 1

    # Sends a message whenever the column value changes
    def watch_cols(self, cols_value: int) -> None:
        self.query_one("#display").update(str(cols_value))
        self.post_message(self.Changed(cols_value))
