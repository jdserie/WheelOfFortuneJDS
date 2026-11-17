"""Graphical practice mode backed by the same rules as the terminal game."""
import tkinter as tk
from tkinter import ttk


def play_graphical(practice_puzzle):
    root = tk.Tk()
    root.title('Phrase Wheel')
    root.minsize(430, 350)
    puzzle = practice_puzzle()
    art = tk.Canvas(root, height=108, background='#241d47', highlightthickness=0)
    art.pack(fill='x')
    colors = ['#f2bc65', '#a78bfa', '#62d9c1', '#f4778d']
    for position, color in enumerate(colors):
        art.create_arc(22, 16, 96, 90, start=position * 90, extent=90, fill=color, outline='#241d47', width=3)
    art.create_text(112, 53, text='PHRASE WHEEL', fill='#fff6df', font=('TkDefaultFont', 22, 'bold'), anchor='w')

    panel = ttk.Frame(root, padding=18)
    panel.pack(fill='both', expand=True)
    board = tk.StringVar()
    summary = tk.StringVar()
    feedback = tk.StringVar()
    ttk.Label(panel, textvariable=summary).pack(anchor='w')
    ttk.Label(panel, textvariable=board, font=('TkFixedFont', 16, 'bold')).pack(pady=13)
    ttk.Label(panel, text='Guess a letter or the whole phrase').pack(anchor='w')
    guess = ttk.Entry(panel)
    guess.pack(fill='x', pady=(2, 8))
    controls = ttk.Frame(panel)
    controls.pack(fill='x')
    ttk.Label(panel, textvariable=feedback, wraplength=400).pack(anchor='w', pady=8)

    def refresh():
        board.set(puzzle.board)
        tried = ' '.join(sorted(puzzle.letter_guesses)) or '—'
        summary.set(f'{puzzle.category} · {puzzle.attempts} misses left · Tried: {tried}')

    def submit(whole_phrase=False):
        feedback.set(puzzle.guess(guess.get(), whole_phrase=whole_phrase))
        guess.delete(0, 'end')
        refresh()

    def restart():
        nonlocal puzzle
        puzzle = practice_puzzle()
        feedback.set('')
        guess.delete(0, 'end')
        guess.focus()
        refresh()

    ttk.Button(controls, text='Guess letter', command=submit).pack(side='left')
    ttk.Button(controls, text='Solve phrase', command=lambda: submit(True)).pack(side='left', padx=5)
    ttk.Button(controls, text='Restart', command=restart).pack(side='right')
    guess.bind('<Return>', lambda event: submit())
    guess.focus()
    refresh()
    root.mainloop()
