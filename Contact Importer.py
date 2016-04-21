outputType = input("Enter the type of output file. (csv/vcl) ")
if outputType == "csv":
    fileName = input("Enter the name of the file to work with ") + ".csv"


while outputType == "csv":
    name = input("Enter the person's name \n")
    if name == "q":
        break
    email = input("Enter the person's email \n")
    combined = name + "," + email + "\n"
    people = open(fileName, 'a')
    people.write(combined)
    people.close()
    print("Submitted \n")


while outputType == "vcl":
    name = input("Enter the person's name \n")
    if name == "q":
        break
    email = input("Enter the person;s name \n")
    combined = "BEGIN:VCARD\nVERSION:4.0\n" + "FN:" + name + "\n" + "EMAIL:" + email + "END:VCARD"
    tempname = name + ".vcl"
    people = open(tempname, 'a')
    people.write(combined)
    people.close()
    print("Submitted \n")
    tempname = None

done = input("Press enter to quit")


"""BEGIN:VCARD
VERSION:4.0
N:Gump;Forrest;;;
FN:Forrest Gump
ORG:Bubba Gump Shrimp Co.
TITLE:Shrimp Man
PHOTO;MEDIATYPE=image/gif:http://www.example.com/dir_photos/my_photo.gif
TEL;TYPE=work,voice;VALUE=uri:tel:+11115551212
TEL;TYPE=home,voice;VALUE=uri:tel:+14045551212
ADR;TYPE=work;LABEL="100 Waters Edge\nBaytown, LA 30314\nUnited States of A
 merica":;;100 Waters Edge;Baytown;LA;30314;United States of America
ADR;TYPE=home;LABEL="42 Plantation St.\nBaytown, LA 30314\nUnited States of
 America":;;42 Plantation St.;Baytown;LA;30314;United States of America
EMAIL:forrestgump@example.com
REV:20080424T195243Z
END:VCARD"""
