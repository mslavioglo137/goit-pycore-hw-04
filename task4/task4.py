def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()

    return cmd, *args


def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        return "Contact already exists."

    if phone in contacts.values():
        return "Phone number already exists."

    contacts[name] = phone

    return "Contact added."


def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        return "Contact not found."

    if phone in contacts.values():
        return "Phone number already exists."

    contacts[name] = phone

    return "Contact updated."


def show_phone(args, contacts):
    name = args[0]

    if name in contacts:
        return contacts[name]

    return "Contact not found."


def show_all(contacts):

    if not contacts:
        return "No contacts saved."

    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result.strip()


def main():

    contacts = {}

    print("Welcome to the assistant bot!")

    while True:

        user_input = input("Enter a command: ")

        if not user_input:
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            try:
                print(add_contact(args, contacts))

            except ValueError:
                print("Enter name and phone.")

        elif command == "change":
            try:
                print(change_contact(args, contacts))

            except ValueError:
                print("Enter name and phone.")

        elif command == "phone":
            try:
                print(show_phone(args, contacts))

            except IndexError:
                print("Enter name.")

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()