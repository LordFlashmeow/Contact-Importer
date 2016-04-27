import os
outputFolder = os.getcwd()
if not os.path.exists(outputFolder):
    os.makedirs("Output")

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
    os.chdir("Output")
    while True:
        name = input("Enter the person's name \n")
        if name == "q":
            break
        if name == "e":
            print(personDict[tempname])
            while True:
                choice = input("Do you want to edit the (n)ame or (e)mail or (q)uit?")
                if "n" in choice:
                    name = input("Enter the corrected name: \n")
                    nameedit = True
                if "e" in choice:
                    email = input("Enter the corrected email: \n")
                    if nameedit is True:
                        personDict[tempname] = [name, email]
                    else:
                        personDict[tempname] = [tempname, email]
                if "q" in choice:
                    personDict[name] = [name, email]
                    del personDict[tempname]
                    edited = True
                    name = None
                    email = None
                    break
                else:
                    print("Your input was not valid. Please try again. \n")
        if edited is False:
            email = input("Enter the person's email \n")
            tempname = name
            combined = name + "," + email + "\n"
            people = open(fileName, 'a')
            people.write(combined)
            people.close()
            personDict[name] = [name, email]
            print("Submitted \n")


def vCard():
    os.chdir("Output")
    while True:
        edited = False
        name = input("Enter the person's name \n")
        if name == "q":
            break
        if name == "e":
            print(personDict[tempname])
            while True:
                choice = input("Do you want to edit the (n)ame or (e)mail or (q)uit?")
                if "n" in choice:
                    name = input("Enter the corrected name: \n")
                    nameedit = True
                if "e" in choice:
                    email = input("Enter the corrected email: \n")
                    if nameedit is True:
                        personDict[tempname] = [name, email]
                    else:
                        personDict[tempname] = [tempname, email]
                if "q" in choice:
                    personDict[name] = [name, email]
                    del personDict[tempname]
                    edited = True
                    name = None
                    email = None
                    break
                else:
                    print("Your input was not valid. Please try again. \n")

        if edited is False:      # Check if contact has been edited
            email = input("Enter the person's email \n")
            tempname = name
            combined = "BEGIN:VCARD" \
                       "\nVERSION:4.0\n" + "FN:" + name + "\n" + "EMAIL:" + email + "\n" + "END:VCARD"
            fileName = name + ".vcl"
            people = open(fileName, 'a')
            people.write(combined)
            people.close()
            personDict[name] = [name, email]
            edited = False
            print("Submitted \n")
        edited = False


def autoFormat():
    os.chdir("Output")
    global destination
    edited = False
    while True:
        name = input("Enter the person's name \n")
        if name == "q":
            break
        if name == "e":
            print(personDict[tempname])
            while True:
                choice = input("Do you want to edit the (n)ame or (e)mail or (q)uit?")
                if "n" in choice:
                    name = input("Enter the corrected name: \n")
                    nameedit = True
                if "e" in choice:
                    email = input("Enter the corrected email: \n")
                    if nameedit is True:
                        personDict[tempname] = [name, email]
                    else:
                        personDict[tempname] = [tempname, email]
                if "q" in choice:
                    personDict[name] = [name, email]
                    del personDict[tempname]
                    edited = True
                    name = None
                    email = None
                    break
                else:
                    print("Your input was not valid. Please try again. \n")

        if edited is False:  # Check if contact has been edited
            email = input("Enter the person's email \n")
            tempname = name
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
        os.chdir("Output")
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
