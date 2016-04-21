outputType = input("Enter the type of output file. (c/v) ")
if outputType == "c":
    fileName = input("Enter the name of the file to work with ") + ".csv"


while outputType == "c":
    name = input("Enter the person's name \n")
    if name == "q":
        break
    email = input("Enter the person's email \n")
    combined = name + "," + email + "\n"
    people = open(fileName, 'a')
    people.write(combined)
    people.close()
    print("Submitted \n")


while outputType == "v":
    name = input("Enter the person's name \n")
    if name == "q":
        break
    email = input("Enter the person;s name \n")
    combined = "BEGIN:VCARD\nVERSION:4.0\n" + "FN:" + name + "\n" + "EMAIL:" + email +"\n" + "END:VCARD"
    tempname = name + ".vcl"
    people = open(tempname, 'a')
    people.write(combined)
    people.close()
    print("Submitted \n")
    tempname = None

done = input("Press enter to quit")
