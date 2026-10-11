# opening
f = open('names.txt','r')
names = f.readlines()
f.close()

# user input
query = input("Enter name to search: ")

# found
found = 0

# if line matches query, treating everything as lowercase
for line in names:
    if line.strip().lower() == query.strip().lower():
        found = 1
        break


# save to new file if not found
if found:
    print("Located",query)
else:
    print("Could not locate",query)
    print("Added entry to new file")
    f = open('nofound.txt', 'w')
    f.write(query)
    f.close()