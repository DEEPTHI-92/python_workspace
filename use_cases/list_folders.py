import os

folders = input("please provide list of folder names with spaces inbetween: ").split()

for folder in folders :
    try:
       files = os.listdir(folder)
       print ("-----listing files for folder :   " + folder)
       for file in files :
        print (file)

    except FileNotFoundError:
        print ("please provide a valid input  " + folder )

    except PermissionError:
        print ("permission denied:   " + folder)
    break





