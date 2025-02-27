"""COMP 110 Exercise 02: Wordle"""

__author__ = "730482808"


def contains_char(word: str, character: str) -> bool:
    """Function that searches for a character in a given string"""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    # Identifying an index and making sure variable doesn't exceed 1 character.
    while idx < len(word):
        if word[idx] == character:
            return True
        else:
            idx += 1
    return False
    # While loop to index through word to test if character is within it.


def emojified(guess: str, secret: str) -> str:
    """A function that displays colored boxes to indicate guess accuracy"""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    # Assigning variables for boxes for later.
    assert len(guess) == len(secret), "Guess must be same length as secret"
    index: int = 0
    boxes = ""
    while index < len(secret):
        if contains_char(secret, guess[index]) is True:
            if secret[index] == guess[index]:
                boxes = boxes + green_box
                # Adds green box if letter matches between guess and secret.
            else:
                boxes = boxes + yellow_box
                # Adds yellow box if letter is in both words but wrong space.
        else:
            boxes = boxes + white_box
            # White box if letter doesn't exist in both words.
        index += 1
    print(boxes)
    return boxes


def input_guess(num_char: int) -> str:
    """Function to accept or deny user guess"""
    entry = str(input(f"Enter a {num_char} character word:"))
    if len(entry) == num_char:
        return entry
    # Returns the entered result of input.
    else:
        print(f"That wasn't {num_char} chars! Try again:")
        return input_guess(num_char)
    # Repeats prompt if entry is too long.


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 0
    total_turns: int = 6
    while i <= total_turns - 1:
        print(f"=== Turn {i+1}/{total_turns} ===")
        # Prints turn.
        guess = input_guess(len(secret))
        # Establish variable for return value of prompt.
        emojified(guess, secret)
        # Calls emojified using return value of input_guess.
        if guess == secret:
            print(f"You won in {i+1}/{total_turns} turns!")
            # Victory message.
            return
        else:
            i += 1
            # Iterates to next turn.
        if i == total_turns:
            print("X/6 - Sorry, try again tomorrow!")
            # Losing message.
            return


if __name__ == "__main__":
    main(secret="codes")
