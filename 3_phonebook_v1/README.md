# Phonebook v1

A simple command-line phonebook application written in Python that allows users to manage contacts with multiple numbers and relations.

---

## Goal

Learn the fundamentals of programming logic through a contact management system:

- User input handling
- Classes and objects
- Linked lists for multiple phone numbers
- Conditional logic
- File handling (save/load)
- Functions for CRUD operations

---

## Features

- Add contacts with last name, first name, relation, and multiple phone numbers
- Display all contacts
- Search for a contact by name
- Edit contact details
- Delete a contact
- Save and load the directory to/from a file
- Relation categories: Friend, Family, Colleague, Other

---

## Requirements

- Python 3.x (tested on Python 3.7+)

---

## Installation

No external dependencies required. Simply clone and run!

```bash
git clone <your-repo-url>
cd 3_phonebook_v1
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

===== DIRECTORY =====
1. Add a contact
2. Show contacts
3. Search a contact
4. Edit a contact
5. Delete a contact
0. Exit (Save)
Choice : 1

Last name : Doe
First name: John
Relation (0=Friend, 1=Family, 2=Colleague, 3=Other) : 0
Phone number : 123456789
Add another number ? (Y/N) : N

✓ Contact added successfully!

===== DIRECTORY =====
1. Add a contact
2. Show contacts
3. Search a contact
4. Edit a contact
5. Delete a contact
0. Exit (Save)
Choice : 0

Directory saved in directory.txt
Goodbye!
```
---

## Data Storage

Contacts are saved in `directory.txt` in a simple text format. The file is automatically created on first save.

---

## Project Level

Beginner

---

## Limitations & Known Issues

- Only works with console input/output
- Does not support advanced search (like partial matches)
- Maximum relation types are fixed
- Phone numbers are stored as plain text, no validation
- Data is saved in a simple text file (directory.txt)
- No GUI

---

## Author

Steaven Mamizara

