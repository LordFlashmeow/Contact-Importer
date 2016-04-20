fileName = input("Enter the name of the file to work with") + ".csv"

people = open(fileName, 'a')

while True:
    name = input("Enter the person's name \n")
    if name == "q":
        people.close()
        break
    email = input("Enter the person's email \n")
    combined = name + "," + email + "\n"
    people = open(fileName, 'a')
    people.write(combined)
    people.close()
    print("Submitted \n")
done = input("Press enter to quit")
