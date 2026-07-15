# Oxyan Bot

A simple rule-based chatbot built in Python. Oxyan matches user input against a dictionary of predefined questions and answers, and includes an admin mode for adding, deleting, and modifying its training data at runtime.

Developed by Mehul Sehgal.

## Features

- **User mode** – chat with Oxyan using a set of built-in questions and answers (greetings, small talk, general knowledge, jokes, etc.)
- **Admin mode** – add new question/answer pairs, delete existing ones, or modify them on the fly
- **Feedback mode** – rate the bot out of 10 and leave comments
- **Help menu** – explains how each mode works
- **Colored terminal output** via `colorama` and `termcolor`

## Requirements

- Python 3.x
- [colorama](https://pypi.org/project/colorama/)
- [termcolor](https://pypi.org/project/termcolor/)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running the bot

> **Note:** The script was originally written for a Jupyter/Google Colab cell — the first line (`!pip install colorama`) is Colab/Jupyter shell-magic syntax, not standard Python. If you run this as a plain `.py` script from the terminal, either:
> - remove/comment out that line and install dependencies via `requirements.txt` first, or
> - run the script inside a Jupyter notebook or Google Colab, where `!pip install` works as-is.

To run in Colab/Jupyter, just paste the code into a cell and run it.

To run as a standalone script (after removing the `!pip install` line):

```bash
python oxyan_bot.py
```

## Usage

On launch, you'll see a menu with five options:

1. **Admin** – train the bot by adding, deleting, or modifying question/answer pairs
2. **User** – chat with Oxyan (type `hi` to start, `bye` to exit; type in lowercase for best results)
3. **Help** – see an explanation of each menu
4. **Feedback** – rate your experience (0–10) and leave a comment
5. **Exit** – close the bot

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
