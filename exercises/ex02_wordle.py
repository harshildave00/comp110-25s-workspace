"""My third exercise in COMP110!"""

__author__ = "730660220"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(any_string: str, char: str) -> bool:
    """Returns True if char is found in any_string, False otherwise."""
    assert len(char) == 1, f"len('{char}') is not 1"
    idx: int = 0
    while idx < len(any_string):
        if any_string[idx] == char:
            return True
        idx += 1
    return False


def emojified(guess_1: str, secret_1: str) -> str:
    """Given 2 params of the same length, will emojify the results of the guess."""
    assert len(guess_1) == len(secret_1), "Guess must be same length as secret"
    result: str = ""
    ind: int = 0
    while ind < len(guess_1):
        if guess_1[ind] == secret_1[ind]:
            result += GREEN_BOX
        elif contains_char(secret_1, guess_1[ind]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        ind += 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess and validates the number of characters."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    num_turns: int = 1
    maximum_turns: int = 6
    player_haswon: bool = False

    while num_turns <= maximum_turns and not player_haswon:
        print(f"=== Turn {num_turns}/{maximum_turns} ===")
        guess: str = input_guess(len(secret))
        emoji_output: str = emojified(guess, secret)
        print(emoji_output)

        if guess == secret:
            player_haswon = True
        else:
            num_turns += 1

    if player_haswon:
        print(f"You won in {num_turns} turns!")
    else:
        print("X6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
