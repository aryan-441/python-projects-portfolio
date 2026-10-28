# Flash Cards App

A Tkinter vocabulary app that presents Spanish words, reveals the English translation, and removes known words from the remaining study list.

## How it works

The app reads `vocab_csv.csv` with pandas. It loads `words_to_learn.csv` when a progress file exists, otherwise it starts from the original vocabulary. Each card is selected at random. Marking a word known removes it from the current list and writes the remaining words back to CSV.

## Requirements and setup

Python 3, Tkinter, and pandas. From this folder, install pandas with `python -m pip install pandas`, then run `python main.py`. Keep the CSV and `images/` assets in the expected project structure.

## Limitations and attribution

This is a course capstone exercise. It expects the vocabulary columns `Spanish` and `English` and uses relative file paths. Confirm that the vocabulary data and images may be redistributed. Drive lists `main.py` as created 2026-06-01 and modified 2026-09-13; these are file metadata dates, not a verified project timeline.

No license has been selected.
