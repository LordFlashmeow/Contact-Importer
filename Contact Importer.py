outputAuto = None
outputType = None
destination = None
personDict = {}


def autoOutput():
    global outputAuto
    global outputType
    global destination
    outputAuto = input("Do you want to automatically select the file type? (y/n) ")
    if outputAuto == "y":
        outputAuto = True
        print("What will this be imported into? Press 'o' for Outlook or 'g' for GMail.")
        destination = input("o/g")
        autoFormat()
    elif outputAuto == "n":
        outputAuto = False
        outputType = input("Enter the type of output file. (o/g/v) ")
        if outputType == "g":
            google(input("Enter the name of the file to work with ") + ".csv")
        """if outputType == "o":
            outlook(input("Enter the name of the file to work with") + ".csv")
        """
        if outputType == "v":
            vCard()
    else:
        print("Your input was not recognised. Please try again")
        autoOutput()


def google(fileName):
    while True:
        name = input("Enter the person's name \n")
        if name == "q":
            break
        email = input("Enter the person's email \n")
        combined = name + "," + email + "\n"
        people = open(fileName, 'a')
        people.write(combined)
        people.close()
        personDict[name] = [name, email]
        print("Submitted \n")


def vCard():
    while True:
        name = input("Enter the person's name \n")
        if name == "q":
            break
        email = input("Enter the person's email \n")
        combined = "BEGIN:VCARD" \
                   "\nVERSION:4.0\n" + "FN:" + name + "\n" + "EMAIL:" + email + "\n" + "END:VCARD"
        fileName = name + ".vcl"
        people = open(fileName, 'a')
        people.write(combined)
        people.close()
        personDict[name] = [name, email]
        print("Submitted \n")
        tempname = None


def autoFormat():
    global destination
    while True:
        name = input("Enter the person's name \n")
        if name == "q":
            break
        email = input("Enter the person's email \n")
        if destination == "g":
            personDict[name] = [name, email]
        elif destination == "o":
            splitname = name.split()
            first = splitname[0]
            last = splitname[-1]
            personDict[name] = [first, last, email]

    if len(personDict) > 10:
        print("Exporting as CSV \n")
        fileName = input("Enter the name of the output file \n") + ".csv"
        if destination == "g":
            with open(fileName, 'w') as f:
                [f.write('{0},{1}\n'.format(key, value)) for key, value in personDict.items()]
        elif destination == "o":
            for first, last, email in personDict.values():
                combined = first + "," + last + "," + email + "," + name + "\n"  # Format for outlook is "First Name",
                # "Last Name","E-mail Address","E-mail Display Name"
                people = open(fileName, 'a')
                people.write(combined)
                people.close()

    elif len(personDict) <= 10:
        for name, email in personDict.values():
            combined = "BEGIN:VCARD\nVERSION:4.0\n" + "FN:" + name + "\n" + "EMAIL:" + email + "\n" + "END:VCARD"
            fileName = name + ".vcl"
            people = open(fileName, 'a')
            people.write(combined)
            people.close()
            print("Created file for " + name)


autoOutput()

done = input("Press enter to quit")

""""Title","First Name","Last Name","E-mail Address","E-mail Display Name"""""
