# TEXESO
__TEXESO__ is a terminal implementation of the famous memory game _Pexeso_, built using Textual and Python.

#### _Video Demo: <https://youtu.be/qobZy0ShBc8>_

## Project Structure

Since keeping everything in one file was getting messy and hard to manage, I divided the project into smaller modules to make the code easier to navigate and maintain.

`project/`
- `project.py`

- `test_project.py`

- `requirements.txt`

- `components/`
    - `__init__.py`

    - `card.py`

    - `game_board.py`

    - `reactive_board.py`

    - `steppers.py`

    - `title.py`

- `screens/`

    - `__init__.py`

    - `main_screen.py`

    - `game_screen.py`

    - `help_screen.py`

    - `setup_screen.py`

    - `quit_screen.py`

    - `end_screen.py`

## Usage

Move into this project directory and install the required libraries using

```bash
pip install -r requirements.txt
```

then to run the game

```bash
python project.py
```

## Gameplay
1. **Select Your Layout**
    - Start with the default 4 × 4 layout, which includes a total of 8 matching pairs.
    - You can change the layout to increase or decrease the difficulty as you like.

2. **Start the Game**
    - The cards are laid out face-down in a grid.
    - Each card has a hidden matching pair somewhere on the board.

3. **Flip Two Cards**
    - Click on a card to reveal it.
    - Then, click on a second card to see if it matches the first.
    - If the cards match, they remain face-up.
    - If they don’t match, both cards flip back after a short delay... try to remember their positions!!

4. **Continue Playing**
    - Keep flipping cards and remembering positions until you’ve matched all pairs.
    - If you want, you can pause or quit the game in between.

## Working

The project contains
- 3 helper functions - `create_matrix()`, `is_match()`, `is_game_over()`
- 6 components or custom widgets created with the help of different in-built Textual widget classes and functions -  `Card`, `GameBoard`, `ReactiveBoard`, `RowStepper`, `ColumnStepper`, `Title`
- 6 custom screens created with the help of in-built Textual **Screen** or **ModalScreen** classes - `MainScreen`, `SetupScreen`, `GameScreen`, `QuitScreen`, `EndScreen`, `HelpScreen`

Let's discuss each of them briefly

#### Helper Functions

1. `create_matrix()`: It creates a **m x n matrix** with matching pairs of numbers, all in different positions, ensuring that the value of **m x n** is **even** to prevent forming an unpaired element.

2. `is_match()`: It checks whether two **`Card`s** have the same **`card_value`** or not, ensuring that both of the `Card`s are not the same **single `Card`** by comparing their **`card_id`s**.

3. `is_game_over()`: It checks whether the game has ended, by comparing the **current total number of matches** made with the **maximum number of matches possible**.

#### Components / Custom Widgets

1. `Card`: A widget to represent the individual cards of the game. Each `Card` has its own `card_value` and `card_id`. The `card_id` is used to make each card unique, so that the user can't click on the same card and make a match. It has the ability to hide and reveal its `card_value`. When matched with another `Card`, both of them change their color and becomes unclickable.

2. `GameBoard`: A widget to display a grid of `Card`s and handle the core game logic. It signals the `Card`s to reveal their values when selected, and then hide their values or change their color based on whether their values match or not. It also monitors the total number of moves and matches made in the game, and sends it to the `GameScreen` to display. Finally, it also sends a `Message` to the `GameScreen` when the game is over (using `is_game_over()`).

3. `ReactiveBoard`: Similar to the `GameBoard`, but a very stripped down version. It displays a grid of unclickable `Card`s. Its main purpose is to allow the user see the preview of the `GameBoard` before starting to play. It also changes its number of rows and columns based on the values of `RowStepper` and `ColumnStepper`.

4. `RowStepper`: A spinner/stepper widget to set the number of rows in the game. It allows the user to precisely increment or decrement the number or rows. It also ensures that the product of rows and columns in the game is always even to ensure all the elements have their pairs. When the row value is changed, it sends a `Message`.

5. `ColumnStepper`: Similar to `RowStepper`, but keeps track of columns in the game instead of rows.

6. `Title`: A widget to display the game name **TEXESO** in a fancy way. It is used by the `MainScreen` only.

#### Screens

1. `MainScreen`: The main screen of the game. It shows the `Title` as well as three buttons - **NEW GAME**, **QUIT**, **HELP**. Clicking the **NEW GAME** button takes the user to the `SetupScreen`. Clicking the **QUIT** button displays the `QuitScreen` and clicking the **HELP** button displays the `HelpScreen`. It contains a disabled `ReactiveBoard` as a background, to fill up the empty spaces.

2. `SetupScreen`: The setup/configuration screen of the game. It is divided into two parts - a sidebar and a `ReactiveBoard`.
The sidebar contains a fancy **SETUP** title, a `RowStepper`, a `ColumnStepper`, a **START** and a **BACK** button. The screen acts a medium to send the values of `RowStepper` and `ColumnStepper` to the `ReactiveBoard` to show a preview. When the **START** is clicked, it sends the final value of `RowStepper` and `ColumnStepper` to the `GameScreen` to start the game. Clicking the **BACK** button on the other hand takes the user back to the `MainScreen`

3. `GameScreen`: As the name suggests, it is the screen that allows the gameplay to take place. It is divided into two parts - a sidebar and a `GameBoard`. The `GameBoard` is created using the values of rows and columns received from the `SetupScreen`. The sidebar contains a fancy **GAME** title, counters for total moves matches made, and **PAUSE** and **END GAME** buttons. The screen receives the value of total moves and matches made from the `GameBoard` and displays it on their individual counters. The **PAUSE** button pauses the game by disabling the `GameBoard` (the button then changes its name from **PAUSE** to **RESUME** which is then used to resume the game). The **END GAME** displays the `EndScreen`. On receiving the message of game over from the `GameBoard`, the sidebar changes its color and some components, allowing the user to directly start a **NEW GAME** by going to the `SetupScreen` or return to the `MainScreen`.

4. `QuitScreen`: A confirmation screen asking the user whether they want to quit the game or not. It has two buttons **YES** or **NO**. Clicking **YES** quits the game, while clicking **NO** dismisses the screen.

5. `EndScreen`: Similar to `QuitScreen`, it is a confirmation screen asking the user whether they want to end the ongoing game or not. It has two buttons **YES** or **NO**. Clicking **YES** ends the game, while clicking **NO** dismisses the screen itself.

6. `HelpScreen`: A simple help screen that shows some information and instructions of the game using markdown text and Textual's in-built `MarkdownViewer` widget. It has only an **OKAY** button, clicking which dismisses the screen itself.

<hr>

> ### Made by Rupam Das
> Github Username: ru-das
<br>
> edX Username: RU_200721
<br>
> Email: rupam212007@gmail.com / rupam.das@outlook.com
<br>
> Location: Kolkata, West Bengal, India
