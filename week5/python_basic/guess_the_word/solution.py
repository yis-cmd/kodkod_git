from random import choice


def main():
    num_of_guesses = int(get_valid_number())
    words_list = ["word", "and", "another"]
    tried_letters = []
    discovered_letters = []
    word = choice(words_list)
    is_successful = False
    for guess in range(num_of_guesses, 1, -1):
        print_word(word, discovered_letters, tried_letters)
        print(f"You have {guess} more guesses")
        new_letter = get_valid_letter()
        if new_letter in word:
            discovered_letters.append(new_letter)
        else:
            tried_letters.append(new_letter)
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
        if num.isdigit():
            return num
        print("That was not a letter, try again")


def print_word(word: str, discovered_letters: list[str], tried_letters: list[str]):
    print(f"you tried: {tried_letters}")
    for letter in word:
        if letter in discovered_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print()


def get_valid_letter():
    while True:
        letter = input("Enter your guess")
        if letter.isupper() or letter.islower():
            return letter
        print("That was not a letter, try again")


def completed_check(word: str, discovered_letters: list[str]):
    for letter in word:
        if letter not in discovered_letters:
            return False
    return True


if __name__ == "__main__":
    main()
