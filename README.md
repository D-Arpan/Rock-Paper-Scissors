# Rock, Paper, Scissors Game

## Overview
This is a simple **Rock, Paper, Scissors** game implemented in Python. The user plays against the computer, which randomly selects a move. The game follows standard rules and runs in a loop until the user chooses to exit.

## How It Works
1. The user selects their move: **Rock, Paper, or Scissors**.
2. The computer randomly selects its move.
3. The winner is determined based on the following rules:
   - **Rock vs Rock → Tie**
   - **Rock vs Paper → Paper Wins**
   - **Rock vs Scissors → Rock Wins**
   - **Paper vs Paper → Tie**
   - **Paper vs Rock → Paper Wins**
   - **Paper vs Scissors → Scissors Wins**
   - **Scissors vs Scissors → Tie**
   - **Scissors vs Rock → Rock Wins**
   - **Scissors vs Paper → Scissors Wins**
4. The game continues until the user enters **'Exit'**.

## Installation
To run the game on your local machine:

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors.git
   ```
2. Navigate to the project folder:
   ```bash
   cd rock-paper-scissors
   ```
3. Run the script:
   ```bash
   python rock_paper_scissors.py
   ```

## Example Gameplay
```
ALLOWED MOVES ARE:
ROCK
PAPER
SCISSORS
EXIT - To leave the game

YOUR MOVE: Rock
You chose ROCK
Computer chose PAPER
Computer Won. Better luck next time.
```

## Possible Improvements
- Add a **score tracking system**.
- Implement a **GUI version** using Tkinter or Flask.
- Enhance the **user input validation**.

## Contributions
Contributions are welcome! Feel free to fork this repository and submit pull requests.

---
**Enjoy the game! 🎮**

