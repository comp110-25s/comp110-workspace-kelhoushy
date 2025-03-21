"""COMP 110 Exercise 03: Dictionary"""

__author__ = "730482808"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values in a dictionary"""
    new_dictionary: dict[str, str] = {}
    for word in dictionary:
        # Goes through each word found in the dictionary
        if dictionary[word] in new_dictionary:
            # Checks if the current value is a key in the new dictionary
            raise KeyError("Keys are not unique!")
            # If so, raises an error
        new_dictionary[dictionary[word]] = word
        # Adds the key from the original dictionary as a value for the new dictionary
    return new_dictionary


def count(list: list[str]) -> dict[str, int]:
    """Turns a list into a dictionary and counts number of repeats"""
    i: int = 0
    # Initialize index
    new_dictionary: dict[str, int] = {}
    # Create empty dictionary
    while i < len(list):
        if list[i] in new_dictionary:
            # Checks if current string in list is a key already in the new dictionary
            new_dictionary[list[i]] += 1
            # If so, adds 1 to the value to show iteration
        else:
            new_dictionary[list[i]] = 1
            # If not, adds the string as a new key with a value of 1
        i += 1
    return new_dictionary


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the color that appeared most frequently"""
    colors: list[str] = []
    # Creates an empty list
    for name in dictionary:
        colors.append(dictionary[name])
        # Adds color (value) from dictionary to the empty list
    color_frequency: dict = count(colors)
    # Uses count function to count frequency of a color in list
    max: int = 0
    fav_color: str = ""
    # Initialize empty values
    for color in color_frequency:
        if color_frequency[color] > max:
            # If current value in dictionary is greater than the present mode
            max = color_frequency[color]
            # Establishes value as mode
            fav_color = f"{color}"
            # Assigns value of key to variable
    return fav_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings into a dictionary based on word length"""
    i: int = 0
    # Initialize index
    temp: dict[str, int] = {}
    # Creates empty dictionary
    while i < len(strings):
        temp[strings[i]] = len(strings[i])
        # Assigns value in dictionary where key is the string and the value is its len
        i += 1
    word_list: set[str] = set()
    # Initializes empty set
    binned_temp: dict[int, set[str]] = {}
    # Initializes empty dictionary that will be returned
    for words in temp:
        word_list.add(f"{words}")
        if temp[words] in binned_temp:
            word_list.update(binned_temp[temp[words]])
        binned_temp[temp[words]] = word_list
        word_list = set()
    return binned_temp
