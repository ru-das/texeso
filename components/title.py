from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Static


letters = [
"""
▗▄▄▄▖
  █  
  █  
  █  
""",
"""
▗▄▄▄▖
▐▌   
▐▛▀▀▘
▐▙▄▄▖
""",
"""
▗▖  ▗▖
 ▝▚▞▘ 
  ▐▌  
▗▞▘▝▚▖
""",
"""
 ▗▄▄▖
▐▌   
 ▝▀▚▖
▗▄▄▞▘
""",
"""
 ▗▄▖ 
▐▌ ▐▌
▐▌ ▐▌
▝▚▄▞▘
"""
]


class Title(Horizontal):
    """ A Widget to Display the TEXESO in a fancy way """

    DEFAULT_CSS = """
    Title {
        width: 90;
        height: 7;
    }

    Static {
        text-align: center;
        content-align: center middle;
    }

    .normal {
        background: #26233a;
        outline-top: tall #524f67;
        outline-bottom: tall #191724;
        width: 14;
        height: 6;
        margin-left: 1;
        color: white;

        &:hover {
            background: #26233a 50%
        }
    }

    .highlight {
        background: #eb6f92;
        outline-top: tall #f6c0cd;
        outline-bottom: tall #b4637a;
        width: 14;
        height: 6;
        margin-left: 1;
        color: white;

        &:hover {
            background: #eb6f92 80%
        }
    }

    .first {
        margin-left: 0;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static(letters[0], classes="normal first", expand=True)
        yield Static(letters[1], classes="highlight", expand=True)
        yield Static(letters[2], classes="normal", expand=True)
        yield Static(letters[1], classes="highlight", expand=True)
        yield Static(letters[3], classes="normal", expand=True)
        yield Static(letters[4], classes="normal", expand=True)

