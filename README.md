# 🎯 Word Guessing Game (Hangman Style)

This is a simple **command-line word guessing game**, similar to Hangman. A random word is selected from a predefined list, and the user must guess the word one letter at a time before running out of chances.

## 🕹️ How to Play

- A random word is selected from the word list.
- You are shown blank underscores for each letter.
- You have **10 incorrect guesses** allowed.
- Guess one letter at a time.
- If the letter is correct, it is revealed in all the correct positions.
- You win if you guess the entire word.
- You lose if you make 10 wrong guesses.


## 📂 File Structure

```
word_guess.py          # Main game script
wordlist.py            # File containing a list of words (list name: abcd)
README.md              # This file
```


## 🔧 Requirements

- Python 3.x
- A `wordlist.py` file containing a list named `abcd` with at least 2465 words.

Example `wordlist.py`:

```python
abcd = ["apple", "banana", "grape", "mango", "orange", "lemon", "peach", ...]
```


## ▶️ How to Run

1. Clone the repository or download the files.
2. Make sure `wordlist.py` is in the same directory as `word_guess.py`.
3. Run the game using:

```bash
python word_guess.py
```


## ✅ Sample Gameplay

```
_ _ _ _ _

Enter your guess: e
Correct guess!
_ _ _ _ e

Enter your guess: a
Wrong guess!
9 chances left!
```

You can type `quit` anytime to exit the game.


## 🧠 Logic Highlights

- Words are picked using `random.randint` from the custom list.
- Guesses are validated to avoid repeats.
- A simple helper function `indices()` is used to find all positions of a guessed letter.
- Game ends when the player either guesses the word or makes 10 incorrect attempts.


## 🔒 Rules

- Repeated guesses are not allowed.
- Only lowercase alphabet letters are valid.
- Typing `quit` exits the game.


## 📌 Future Improvements

* Add difficulty levels (easy, medium, hard).
* Add support for phrases or multi-word puzzles.
* Add a graphical interface (using Tkinter or Pygame).
* Show guessed letters so far.


## 📃 License

This project is open-source and free to use under the [MIT License](LICENSE).
