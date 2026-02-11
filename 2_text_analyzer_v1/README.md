# Text Analyzer v1

A simple command-line text analyzer written in Python that allows users to perform basic text cleaning and statistical analysis.

---

## Goal

Learn the fundamentals of programming logic through text processing:

- User input handling
- String manipulation
- Lists and loops
- Functions
- Dictionaries for counting
- Basic statistics

---

## Features

- Clean text (trim spaces, lowercase, remove punctuation)
- Count characters (excluding spaces)
- Count words
- Count sentences
- Calculate letter frequency
- Calculate word frequency
- Display results in a structured format

---

## Requirements

- Python 3.x (tested on Python 3.7+)

---

## Installation

No external dependencies required. Simply clone and run!

```bash
git clone <your-repo-url>
cd 2_text_analyzer_v1
```

---

## How to Run

```bash
python main.py
```
---

## Example Usage

```
$ python main.py

=== Text Analyzer V1 ===

Enter your text:
>> Hello world! This is a test.

=======[ General Statistics ]=======
- Number of characters: 22
- Number of words: 6
- Number of sentences: 2

=======[ Frequencies ]=======

- Letter frequency:
    | h | 2
    | e | 2
    | l | 3
    | o | 2
    | w | 1
    | r | 1
    | d | 1
    | t | 3
    | i | 2
    | s | 3
    | a | 1

- Word frequency:
    - "hello" : 1
    - "world" : 1
    - "this" : 1
    - "is" : 1
    - "a" : 1
    - "test" : 1
```
---

## Project Level

Beginner

---

## Limitations & Known Issues

- Only works with plain text input
- Punctuation removal is basic and predefined
- No support for special characters or emojis
- Does not handle advanced linguistic features (like stemming, lemmatization)
- Output is printed to the console only
- No GUI

---

## Author

Steaven Mamizara

