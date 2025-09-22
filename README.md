# The "Rock, Paper, Scissors" Game
A console based Python implementation of the "Rock, Paper, Scissors" game.

[Rock, Paper, Scissors](https://github.com/valerielashvili/RockPaperScissorsByValeri/blob/main/rock-paper-scissors.py) 
is a **two player game**, where each player makes a throw simultaneously, choosing either **rock**, **paper**, 
or **scissors** to determine the winner based on the game's rules:
- **Rock** crushes scissors.
- **Scissors** cuts paper.
- **Paper** covers rock.

The **winner** is determined by the player's choice which beats the choice of his opponent. If both players make the same
throw (e.g. rock), the game outcome is **draw**.

This basic implementation of the cherished game is an extra project in the [Data Types and Variables](https://softuni.bg/trainings/5092/programming-fundamentals-with-python-september-2025#lesson-96021) 
lesson which is part of the **Programming Fundamentals with Python** module from [SoftUni](https://softuni.bg/),
description of the practical exercise can be found [here](https://softuni.bg/downloads/svn/soft-tech/Sept-2025/Python/02-Data-Types-and-Variables/01-Project-Rock-Paper-Scissors/01-Rock-Paper-Scissors-Project-Description..pdf).

The goal of the project is to better learn Python and work with Git & GitHub.
The aim of the exercise is to resolve the problem with the accumulated until the moment knowledge.

## Input and Output
The player enters one of the following options:

- `r` for **rock**
- `p` for **paper**
- `s` for **scissors**

The computer choses a **random option** and the winner is determined. At the end of the game session a score board is printed:

```
Thank you for playing!

Latest Scores:

RANK  NAME      WINS  LOSSES
============================
1     user      3     1
----------------------------
2     computer  1     3
----------------------------
Draws: 2
```

## Additional Functionality
Following additional functionality was implemented:

- **Colored output** for computer moves and the result.
- **Restart the game**: the player is asked to play again.
- **Game session**: all scores are recorded within the same session.
- **Scoring system** improved to have player **ranks**.
- The **draws number** is accounted.
- A **score board** is printed at the end of the game.