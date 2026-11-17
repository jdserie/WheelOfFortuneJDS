"""Two-player word guessing game with a built-in solo practice puzzle."""
import argparse
import getpass
import re
from dataclasses import dataclass, field

LETTER_POINTS = {
    **dict.fromkeys('AEIORST', 1),
    **dict.fromkeys('DLNU', 2),
    **dict.fromkeys('GHY', 3),
    **dict.fromkeys('BCFMPW', 4),
    **dict.fromkeys('KV', 5),
    **dict.fromkeys('X', 8),
    **dict.fromkeys('JQZ', 10),
}


@dataclass
class Puzzle:
    phrase: str
    category: str
    attempts: int = 6
    letter_guesses: set[str] = field(default_factory=set)
    phrase_guesses: set[str] = field(default_factory=set)
    solved: bool = False

    def __post_init__(self):
        self.phrase = self.phrase.strip().upper()
        if not re.fullmatch(r"[A-Z '-]+", self.phrase) or not any(c.isalpha() for c in self.phrase):
            raise ValueError("Use letters, spaces, apostrophes, and dashes in the puzzle.")

    @property
    def board(self):
        return ' '.join(
            char if self.solved or not char.isalpha() or char in self.letter_guesses else '_'
            for char in self.phrase
        )

    @property
    def points(self):
        return sum(LETTER_POINTS.get(char, 0) for char in self.phrase)

    def guess(self, value, *, whole_phrase=False):
        if self.solved or self.attempts <= 0:
            return 'This round is complete.'
        value = value.strip().upper()
        if whole_phrase:
            if not re.fullmatch(r"[A-Z '-]+", value) or not any(c.isalpha() for c in value):
                return 'Enter a phrase.'
            guesses = self.phrase_guesses
            correct = value == self.phrase
        else:
            if not re.fullmatch('[A-Z]', value):
                return 'Enter a single letter.'
            guesses = self.letter_guesses
            correct = value in self.phrase
        if value in guesses:
            return 'You already tried that.'
        guesses.add(value)
        if not correct:
            self.attempts -= 1
        self.solved = correct and (whole_phrase or all(
            not c.isalpha() or c in self.letter_guesses for c in self.phrase
        ))
        if self.solved:
            return f'Solved for {self.points} points.'
        if not self.attempts:
            return f'The answer was {self.phrase}. Host earns {max(0, 45 - self.points)} points.'
        return 'Correct.' if correct else 'Try again.'


def practice_puzzle():
    return Puzzle('ON THE FAIRWAY', 'Sport')


def play(puzzle):
    print('\n== PHRASE WHEEL ==')
    while not puzzle.solved and puzzle.attempts:
        print(f"\nCategory: {puzzle.category} · {puzzle.attempts} misses left")
        print(puzzle.board)
        print('Tried:', ' '.join(sorted(puzzle.letter_guesses)) or '—')
        value = input('Guess a letter, or enter /solve followed by the phrase: ').strip()
        command, _, phrase = value.partition(' ')
        if command.lower() == '/solve':
            print(puzzle.guess(phrase, whole_phrase=True))
        else:
            print(puzzle.guess(value))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--demo', action='store_true', help='Play a built-in practice puzzle.')
    parser.add_argument('--gui', action='store_true', help='Open the graphical edition.')
    args = parser.parse_args()
    try:
        if args.gui:
            from graphical import play_graphical
            play_graphical(practice_puzzle)
            return
        if args.demo:
            play(practice_puzzle())
            return
        while True:
            try:
                phrase = getpass.getpass('Host: enter a secret phrase: ')
                puzzle = Puzzle(phrase, input('Category: ').strip() or 'Open category')
            except ValueError as error:
                print(error)
                continue
            play(puzzle)
            break
    except (EOFError, KeyboardInterrupt):
        print('\nRound ended.')


if __name__ == '__main__':
    main()
