from enum import IntEnum

# ================= TYPES =================

class Relation(IntEnum):
    Friend = 0
    Family = 1
    Colleague = 2
    Other = 3

RELATION_STR = ["Friend", "Family", "Colleague", "Other"]


class Number:
    def __init__(self, phone: str):
        self.phone = phone
        self.next = None   # logical pointer


class Contact:
    def __init__(self):
        self.last_name = ""
        self.first_name = ""
        self.relation = Relation.Other
        self.numbers = None   # head of linked list
        self.next = None      # logical pointer


class Directory:
    def __init__(self):
        self.head = None


# ================= TOOLS =================


def read_string(prompt: str = "") -> str:
    return input(prompt).strip()


# ================= NUMBERS =================


def add_number(contact: Contact, phone: str):
    n = Number(phone)
    n.next = contact.numbers
    contact.numbers = n


# ================= CONTACT =================


def create_contact() -> Contact:
    c = Contact()

    c.last_name = read_string("Last name : ")
    c.first_name = read_string("First name : ")

    try:
        choice = int(read_string("Relation (0=Friend, 1=Family, 2=Colleague, 3=Other) : "))
    except ValueError:
        choice = 3

    if choice < 0 or choice > 3:
        choice = 3

    c.relation = Relation(choice)

    answer = "Y"
    while answer.lower() == "y":
        phone = read_string("Phone number : ")
        add_number(c, phone)
        answer = read_string("Add another number ? (Y/N) : ")

    return c


# ================= DIRECTORY =================


def add_contact(directory: Directory, contact: Contact):
    if directory.head is None:
        directory.head = contact
        return

    p = directory.head
    while p.next:
        p = p.next
    p.next = contact


# ================= DISPLAY =================


def display_contact(c: Contact):
    print("\n--- Contact ---")
    print(f"Last name : {c.last_name}")
    print(f"First name: {c.first_name}")
    print(f"Relation  : {RELATION_STR[c.relation]}")
    print("Numbers   :")

    n = c.numbers
    if not n:
        print("  (No numbers)")

    while n:
        print(f"  - {n.phone}")
        n = n.next


def display_directory(d: Directory):
    if not d.head:
        print("\nDirectory is empty.\n")
        return

    p = d.head
    while p:
        display_contact(p)
        print()
        p = p.next


# ================= SEARCH =================


def search_contact(d: Directory, last_name: str, first_name: str):
    p = d.head
    while p:
        if p.last_name == last_name and p.first_name == first_name:
            return p
        p = p.next
    return None


# ================= EDIT =================


def edit_contact(c: Contact):
    c.last_name = read_string("New last name : ")
    c.first_name = read_string("New first name : ")

    try:
        choice = int(read_string("New relation (0=Friend,1=Family,2=Colleague,3=Other) : "))
    except ValueError:
        choice = 3

    if choice < 0 or choice > 3:
        choice = 3

    c.relation = Relation(choice)
    print("Contact updated.\n")


# ================= DELETE =================


def delete_contact(d: Directory, last_name: str, first_name: str):
    p = d.head
    prev = None

    while p:
        if p.last_name == last_name and p.first_name == first_name:
            if prev:
                prev.next = p.next
            else:
                d.head = p.next
            print("Contact deleted.\n")
            return

        prev = p
        p = p.next

    print("Contact not found.\n")


# ================= SAVE =================


def save_directory(d: Directory, file="directory.txt"):
    with open(file, "w", encoding="utf-8") as f:
        c = d.head
        while c:
            line = f"{c.last_name}|{c.first_name}|{int(c.relation)}|"
            n = c.numbers
            while n:
                line += f"{n.phone};"
                n = n.next
            f.write(line + "\n")
            c = c.next


# ================= LOAD =================


def load_directory(d: Directory, file="directory.txt"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) < 4:
                    continue

                c = Contact()
                c.last_name = parts[0]
                c.first_name = parts[1]
                c.relation = Relation(int(parts[2]))

                nums = parts[3]
                for phone in nums.split(";"):
                    if phone:
                        add_number(c, phone)

                add_contact(d, c)
    except FileNotFoundError:
        pass


# ================= MENU =================


def main():
    d = Directory()
    load_directory(d)

    while True:
        print("\n===== DIRECTORY =====")
        print("1. Add a contact")
        print("2. Show contacts")
        print("3. Search a contact")
        print("4. Edit a contact")
        print("5. Delete a contact")
        print("0. Exit (Save)")

        choice = read_string("Choice : ")

        if choice == "1":
            add_contact(d, create_contact())

        elif choice == "2":
            display_directory(d)

        elif choice == "3":
            last_name = read_string("Last name : ")
            first_name = read_string("First name : ")
            c = search_contact(d, last_name, first_name)
            if c:
                display_contact(c)
            else:
                print("Contact not found.\n")

        elif choice == "4":
            last_name = read_string("Last name : ")
            first_name = read_string("First name : ")
            c = search_contact(d, last_name, first_name)
            if c:
                edit_contact(c)
            else:
                print("Contact not found.\n")

        elif choice == "5":
            last_name = read_string("Last name : ")
            first_name = read_string("First name : ")
            delete_contact(d, last_name, first_name)

        elif choice == "0":
            save_directory(d)
            print("Directory saved in directory.txt")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()

