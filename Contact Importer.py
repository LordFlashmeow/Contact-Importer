people = open('Adair Writers.csv', 'a')

while True:
    name = input("Enter the person's name \n")
    if name == "q":
        people.close()
        break
    email = input("Enter the person's email \n")
    combined = name + "," + email + "\n"
    people = open('Adair Writers.csv', 'a')
    people.write(combined)
    people.close()
    print("Submitted \n")
done = input("Press enter to quit")
