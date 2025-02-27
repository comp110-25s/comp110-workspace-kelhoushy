"""COMP 110 Exercise 02: Wordle"""

__author__ = "730482808"


def contains_char(word: str, character: str) -> bool:
    """Function that searches for a character in a given string"""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    while idx < len(word):
        if word[idx] == character:
            return True
        else:
            idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """A function that displays colored boxes to indicate guess accuracy"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"
    index: int = 0
    boxes = ""
    while index < len(secret):
        if contains_char(secret, guess[index]) is True:
            if secret[index] == guess[index]:
                boxes = boxes + GREEN_BOX
            else:
                boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
        index += 1
    print(boxes)
    return boxes


def input_guess(num_char: int) -> str:
    """Function to accept or deny user guess"""
    entry = str(input(f"Enter a {num_char} character word:"))
    if len(entry) == num_char:
        return entry
    else:
        print(f"That wasn't {num_char} chars! Try again:")
        return input_guess(num_char)


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 0
    total_turns: int = 6
    while i <= total_turns:
        print(f"=== Turn {i}/{total_turns} ===")
        guess = input_guess(len(secret))
        emojified(guess, secret)
        if guess == secret:
            print(f"You won in {i}/{total_turns} turns!")
            return
        else:
            i += 1
        if i > total_turns:
            print("X/6 - Sorry, try again tomorrow!")
            return


if __name__ == "__main__":
    main(secret="codes")
