# TwitConnect4: Play Connect 4 on Twitter

TwitConnect4 is a Twitter bot that enables users to play the classic game of Connect 4 through tweets. You can challenge your friends or other Twitter users to a game of Connect 4 and enjoy the competitive gameplay right on the Twitter platform.

## Project Overview

TwitConnect4 utilizes the Twitter API and game logic to create a bot that facilitates Connect 4 gameplay on Twitter. The project consists of the following files:

- `main.py`: This file contains the main logic for interacting with the Twitter API and handling user commands.
- `game.py`: This file implements the game logic and functions for Connect 4.
- `gameboard.txt`: This file stores the current state of the game board.
- `gamenumber.txt`: This file keeps track of the number of games played.
- `newboard.txt`: This file contains the representation of a new game board.

## How to Play

Connect 4 is a two-player game played on a 6x7 grid. The objective is to be the first player to connect four of their colored discs in a row, either horizontally, vertically, or diagonally.

To play Connect 4 on Twitter using TwitConnect4:

1. Follow the TwitConnect4 bot on Twitter.
2. Start a game by mentioning the bot's username (@TwitConnect4) in a tweet.
3. The bot will respond and provide you with instructions and the current game board.
4. Make your moves by replying to the bot's tweet with the column number (1-7) where you want to drop your disc.
5. The bot will update the game board and respond with the updated board.
6. Continue taking turns with your opponent until one player connects four discs or the game ends in a draw.
7. The bot will declare the winner or indicate a draw once the game concludes.

## Setup and Usage

To set up and use TwitConnect4, follow these steps:

1. Clone the project repository:

   ```bash
   git clone https://github.com/nguyenttleo/TwitConnect4.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure you have the necessary libraries installed, including `tweepy` and `itertools` for interacting with the Twitter API and game logic, respectively.

3. Obtain Twitter API credentials:

   - Create a Twitter Developer account and create a new application to obtain your API key, API secret key, Access token, and Access token secret.

4. Configure the API credentials in `main.py`. Replace the placeholder values with your actual Twitter API credentials.

5. Customize the bot's username, commands, and messages in `main.py` to fit your preferences.

6. Run the `main.py` script to start the TwitConnect4 bot:

   ```bash
   python main.py
   ```

   Make sure your bot account is authenticated and has the necessary permissions to read and send tweets.

7. Enjoy playing Connect 4 with other Twitter users using the TwitConnect4 bot!

## Requirements

The following dependencies are required for the TwitConnect4 project:

- tweepy
- itertools

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

Ensure that you have the necessary dependencies installed before running the project.

Now, challenge your friends and engage in thrilling Connect 4 battles right on Twitter with TwitConnect4!

Let the disc-dropping and tweet-replying begin!
