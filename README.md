# Phrase Wheel

![Phrase Wheel cover](docs/cover.webp)

A Python phrase-guessing game by Joshua Serie. Reveal letters, solve the phrase, and keep track of six chances and the original point scoring. The terminal version lets one player enter a hidden puzzle for another player. The graphical edition has a built-in practice puzzle.

| Mode | Run from this folder |
| --- | --- |
| Two players | `python WheelOfFortune_final.py` |
| Terminal practice | `python WheelOfFortune_final.py --demo` |
| Graphical practice | `python WheelOfFortune_final.py --gui` |

Use Python 3.10 or newer. The terminal game uses the standard library. The graphical edition also needs Tkinter, which ships with many Python installers and may be a separate OS package on Linux. Use a single letter or `/solve YOUR PHRASE` in the terminal.

## Project history

Joshua Serie’s [original March 2019 project](https://github.com/jdserie/WheelOfFortuneJDS/commit/08cd3e77962208ae163e512e450965ce0892ae45) is preserved in Git history. The later AI-assisted portfolio refresh separates game logic from the interface and adds a graphical practice mode, input validation, and setup instructions.
