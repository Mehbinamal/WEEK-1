# Load contacts from a text file
def loadContacts(filename):
    contacts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                if ':' in line:
                    name, phone = line.strip().split(':', 1)
                    contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

# Save contacts to a text file
def saveContacts(filename, contacts):
    with open(filename, 'w') as file:
        for name, phone in contacts.items():
            file.write(f"{name}:{phone}\n")

# Add a new contact
def addContact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print(f"Contact for {name} added.")

# View all contacts
def viewContacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Main program
def main():
    filename = 'May-7/contacts.txt'
    contacts = loadContacts(filename)

    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            addContact(contacts)
            saveContacts(filename, contacts)
        elif choice == '2':
            viewContacts(contacts)
        elif choice == '3':
            saveContacts(filename, contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid option.")

main()
