import re


def welcome_msg():
    print(
        """
    ***********************************************************************
    **                                                                   **
    **                         Welcome to Mad Libs!                      **
    **                                                                   **
    ***********************************************************************
    **                                                                   **
    **   Mad Libs is a word game where players provide a list of words   **
    **   to substitute for blanks in a story before reading aloud.       **
    **                                                                   **
    ***********************************************************************
    **                                                                   **
    **   During the game, you'll be prompted to enter Adjectives, Nouns, **
    **   Verbs, Adverbs, and Numbers. Answer these prompts with any      **
    **   words you choose and this program will display your very own    **
    **   story!                                                          **
    **                                                                   **
    ***********************************************************************
    **                                                                   **
    **                   Type 'quit' at any time to exit                 **
    **                                                                   **
    ***********************************************************************"""
    )


# tests


def read_template(path):
    """takes in a path to text file and returns a stripped string of the file’s contents"""
    try:
        with open(path) as file:
            madlib_template = file.read()
            madlib_template = madlib_template.strip()

        return madlib_template
    # else:
    except:
        raise FileNotFoundError("File not found; No such file or directory")


def parse_template(madlib_template):
    """takes in a template string and returns a string with language parts removed and a separate list of those language parts"""

    # regex = r"[\{]+([^}]+)[}]+"
    regex = r"[^{\}]+(?=})"
    words_to_change = re.findall(regex, madlib_template)
    empty_template = re.sub(regex, "", madlib_template)
    # print(words_to_change)
    # print(empty_template)
    return words_to_change, empty_template


def user_words(words_to_change):
    """takes the language parts removed from the template, queries the user to input that type of word, and returns a tuple with the user words to input inot the story"""

    words_to_input = []

    for word in words_to_change:
        user_word = input(f"{word} please: ")

        if user_word.lower() == "quit":
            return print("The game is over. See you soon!")
        else:
            words_to_input.append(user_word.lower())
            # print(words_to_input)
    print(f"Here are your words for the story: {words_to_input} ")
    return words_to_input


def merge(madlib_template, words_to_input):
    print(madlib_template)
    for word in words_to_input:
        completed_template = re.sub(r"\{(.*?)\}", word, madlib_template)
    print(completed_template)


welcome_msg()
madlib_template = read_template("assets/dark_and_stormy_night_template.txt")
# madlib_template = read_template("assets/madlib.txt")
# madlib_template = read_template("assets/template.txt")
words_to_change, empty_template = parse_template(madlib_template)
madlib_words = user_words(words_to_change)
final_madlib = merge(empty_template, madlib_words)
