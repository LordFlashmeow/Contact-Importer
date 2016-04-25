outputAuto = None
outputType = None
def autoOutput():
    global outputAuto
    global outputType
    outputAuto = input("Do you want to automatically select the file type? (y/n) ")
    if outputAuto == "y":
        outputAuto = True
    elif outputAuto == "n":
        outputAuto = False
        outputType = input("Enter the type of output file. (c/v) ")
        if outputType == "c":
            fileName = input("Enter the name of the file to work with ") + ".csv"
    else:
        print("Your input was not recognised. Please try again")
        autoOutput()


def CSV():
    global outputType
    global outputAuto
    while outputType == "c" and outputAuto is False:
        name = input("Enter the person's name \n")
        if name == "q":
            break
        email = input("Enter the person's email \n")
        combined = name + "," + email + "\n"
        people = open(fileName, 'a')
        people.write(combined)
        people.close()
        print("Submitted \n")
def vCard():
    while outputType == "v" and outputAuto is False:
        name = input("Enter the person's name \n")
        if name == "q":
            break
        email = input("Enter the person's name \n")
        combined = "BEGIN:VCARD" \
                   "\nVERSION:4.0\n" + "FN:" + name + "\n" + "EMAIL:" + email + "\n" + "END:VCARD"
        tempname = name + ".vcl"
        people = open(tempname, 'a')
        people.write(combined)
        people.close()
        print("Submitted \n")
        tempname = None

while outputAuto is True:
    name = input("Enter the person's name \n")
        if name == "q":
            break
    email = input("Enter the person's email \n")



done = input("Press enter to quit")
