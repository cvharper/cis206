def display_company(): # display by company
    companies = [] # list

    for person in people:
        companies.append(person)

    companies.sort(key=lambda person: person[1])

    for person in companies:
        print("Customer ID:", person[0])
        print("Company:", person[1])
        print("Contact:", person[2])
        print()


def display_contact(): # display by contact
    contacts = [] # list

    for person in people:
        contacts.append(person)

    contacts.sort(key=lambda person: person[2])

    for person in contacts:
        print("Customer ID:", person[0])
        print("Company:", person[1])
        print("Contact:", person[2])
        print()


def search_company(): # search company
    search = input("Enter company name: ")

    for person in people:
        if search.lower() in person[1].lower(): # making both lowercase and checking
            print("Customer ID:", person[0])
            print("Company:", person[1])
            print("Contact:", person[2])
            print()


def search_contact(): # search contact
    search = input("Enter contact name: ")

    for person in people:
        if search.lower() in person[2].lower(): # making both lowercase and checking
            print("Customer ID:", person[0])
            print("Company:", person[1])
            print("Contact:", person[2])
            print()


# opening the file
f = open("northwind_data.txt")

# there is a header, so we skip it
f.readline()

# this is our list
people = []

for line in f:
    data = line.strip().split(",")

    people.append(data)

# closing file so we dont have a memory leak
f.close()


# intro
print("Welcome to the Northwind Data searching tool!")
print("")

# menu so they can select what they want to do
while True:
    print("1. Display customers sorted by company name")
    print("2. Display customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")
    print("")
    
    choice = input("Enter your choice: ") # choice selection

    if choice == "1":
        display_company()
    elif choice == "2":
        display_contact()
    elif choice == "3":
        search_company()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        print("Goodbye!")
        print("")
        break
    else:
        print("")
        print("Invalid choice. Please try again.")
        print("")
