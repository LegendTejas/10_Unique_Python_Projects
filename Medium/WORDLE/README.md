# WORDLE (A Terminal Game)

A Python implementation of the popular word game Wordle. Guess the hidden 5-letter word in 6 attempts with color-coded feedback!

## Game Instructions

- Guess the WORDLE in 6 tries
- Each guess must be a valid 5-letter word
- After each guess, the color of the tiles will change to show how close your guess was

### Color Meaning:
- 🟩 **Green** - Letter is in the word and in the correct spot
- 🟨 **Yellow** - Letter is in the word but in the wrong spot  
- ⬜ **Gray** - Letter is not in the word

Type `h` for help to see keyboard status during gameplay.

## How to Play

1. Run `main.py` to start the game
2. Enter a 5-letter word guess when prompted
3. The game will provide color-coded feedback:
   - Green letters are correct and in the right position
   - Yellow letters are in the word but wrong position
   - Gray letters are not in the word at all
4. Use the feedback to make your next guess
5. Type `h` at any time to see which letters you've already tried
6. Win by guessing the word within 6 attempts!

## Features

- Color-coded terminal output
- Keyboard tracking to show which letters you've used
- Input validation for 5-letter words
- Help system with keyboard status
- Clean, visually appealing interface

## Requirements

- Python 3.x
- No external dependencies required

## Getting Started

```bash
python main.py
