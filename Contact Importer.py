fileName = input("Enter the name of the file to work with")
outputType = input("Enter the type of output file. (csv/vcl)
if outputType = "csv":
    fileName = fileName + ".csv"
#elif outputType = "vcl":           vCards not yet implemented
#    fileName = fileName + ".vcl"



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
