def parse_input(user_input):
    """Parses the entered command and its arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """Adds a new contact."""
    if len(args) < 2:
        return "Invalid command. Please provide a name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Changes the phone number for an existing contact."""
    if len(args) < 2:
        return "Invalid command. Please provide a name and new phone number."
    name, phone = args
    if name not in contacts:
        return f"Contact {name} not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    """Displays the phone number for the specified contact."""
    if len(args) < 1:
        return "Invalid command. Please provide a name."
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        return f"Contact {name} not found."

def show_all(contacts):
    """Displays all saved contacts and their numbers."""
    if not contacts:
        return "No contacts saved."
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
