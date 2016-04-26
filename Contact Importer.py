outputAuto = None
outputType = None
personDict = {}


def autoOutput():
    global outputAuto
    global outputType
    outputAuto = input("Do you want to automatically select the file type? (y/n) ")
    if outputAuto == "y":
        outputAuto = True
        autoFormat()
    elif outputAuto == "n":
        outputAuto = False
        outputType = input("Enter the type of output file. (c/v) ")
        if outputType == "c":
            CSV(input("Enter the name of the file to work with ") + ".csv")
        if outputType == "v":
            vCard()
    else:
        print("Your input was not recognised. Please try again")
        autoOutput()


def CSV(fileName):
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
        email = input("Enter the person's name \n")
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
    while True:
        name = input("Enter the person's name \n")
        if name == "q":
            break
        email = input("Enter the person's email \n")
        personDict[name] = [name, email]
    if len(personDict) > 10:
        print("Exporting as CSV \n")
        fileName = input("Enter the name of the output file \n") + ".csv"
        with open(fileName, 'w') as f:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in personDict.items()]
    elif len(personDict) <= 10:
        keyValue = personDict[name]
        for keyValue in personDict:
            for key, value in personDict.iteritems():
                combined = "BEGIN:VCARD\nVERSION:4.0\n" + "FN:" + name + "\n" + "EMAIL:" + email + "\n" + "END:VCARD"
                fileName = name + ".vcl"
                people = open(fileName, 'a')
                people.write(combined)
                people.close()
                print("Created file for " + name)


autoOutput()

done = input("Press enter to quit")
