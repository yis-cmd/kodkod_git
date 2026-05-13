from random import choice


def main():
    num_of_guesses = int(get_valid_number())
    words_list = ["word", "and", "another"]
    discovered_letters = []
    word = choice(words_list)
    is_successful = False
    for guess in range(num_of_guesses, 1, -1):
        print_word(word, discovered_letters)
        print(f"You have {guess} more guesses")
        new_letter = get_valid_letter()
        if new_letter in word:
            discovered_letters.append(new_letter)
        if completed_check(word, discovered_letters):
            is_successful = True
            break
    if is_successful == True:
        print("Congrats you won")
    else:
        print("To bad try again sometime else")


def get_valid_number():
    while True:
        num = input("Enter a number of guesses for the game")
        if not num.isdigit():
            print("That was not a letter, try again")
            continue
        break
    return num


def print_word(word: str, discovered_letters: list[str]):
    for letter in word:
        if letter in discovered_letters:
            to_print = letter
        else:
            to_print = "_"
        print(to_print, end="")


def get_valid_letter():
    while True:
        letter = input("Enter your guess")
        if not letter.islower() and not letter.isupper():
            print("That was not a letter, try again")
            continue
        break
    return letter


def completed_check(word: str, discovered_letters: list[str]):
    for letter in word:
        if letter not in discovered_letters:
            return False
    return True


if __name__ == "__main__":
    main()
