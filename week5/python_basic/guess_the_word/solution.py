import random
from typing import Final

MAX_GUESSES: Final = 26
UNKNOWN_LETTERS: Final = "_"


class HangMan:
    _words_list: list[str] = ["multiple", "words"]

    def __init__(self) -> None:
        self.remaining_guesses: int = 0
        self.word: str = random.choice(self._words_list).lower()
        self.false_tries: list[str] = []
        self.correct_tries: list[str] = []

    def get_num_of_guesses(self) -> int:
        while True:
            num: int = get_a_number("Enter the number of guesses you want")
            if self.is_valid_num_of_guesses(num):
                return num
            else:
                print("This was not a valid guess number, try again")

    def is_valid_num_of_guesses(self, num):
        return 0 < num < MAX_GUESSES

    def get_mask_word(self):
        word_to_print: list[str] = []
        for letter in self.word:
            if letter in self.correct_tries:
                word_to_print.append(letter)
            else:
                word_to_print.append(UNKNOWN_LETTERS)
        return "".join(word_to_print)

    def print_current_word(self):
        mask_word = self.get_mask_word()
        print("==================================")
        print(f"Currently discovered: {mask_word}")
        print(f"Already tried {self.false_tries}")
        print(f"{self.remaining_guesses} guesses remain")

    def win_msg(self):
        print("=====================")
        print("well done you made it")
        print(f"the word was: {self.word}")

    def lose_msg(self):
        print("=====================")
        print("Too bad you lost")
        print(f"the word was: {self.word}")

    def was_guessed_before(self, guess: str):
        return guess in self.correct_tries or guess in self.false_tries

    def handle_guess(self, guess: str):
        if self.was_guessed_before(guess):
            print("you already tried this letter")
            return
        if guess in self.word:
            self.correct_tries.append(guess)
            print("Success")
            return
        self.false_tries.append(guess)
        print("Failure")
        self.remaining_guesses -= 1

    def is_won(self):
        return UNKNOWN_LETTERS not in self.get_mask_word()

    def is_lost(self):
        return self.remaining_guesses == 0

    def run(self):
        self.remaining_guesses = self.get_num_of_guesses()
        while True:
            self.print_current_word()
            new_letter = get_a_lowercase_letter("Enter your new guess")
            self.handle_guess(new_letter)
            if self.is_won():
                self.win_msg()
                break
            if self.is_lost():
                self.lose_msg()
                break


def get_a_number(msg) -> int:
    while True:
        try:
            return int(input(f"{msg}: "))
        except ValueError:
            print("This was not a number, try again")


def get_a_lowercase_letter(msg):
    while True:
        letter = input(f"{msg}: ")
        if is_one_char(letter) and is_a_letter(letter):
            return letter.lower()
        print("Invalid, try again")


def is_one_char(item: str):
    return len(item) == 1


def is_a_letter(item: str):
    return item.isalpha()


def main() -> None:
    while True:
        game = HangMan()
        game.run()
        print("Game over")
        choice = input("Do you want another match?(yes/no): ")
        if choice != "yes":
            print("Good bye")
            break


if __name__ == "__main__":
    main()
