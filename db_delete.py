import os
from config import DATABASE_FILE

# Delete db if it exists


def dbdel():
    while True:
        user_delete = input("Would you like to clear db?(Y/N)?: ")
        if len(user_delete) == 1:
            if user_delete.upper() == "Y":
                try:
                    os.remove(DATABASE_FILE)
                    break
                except:
                    print("There is no db to be deleted")
            elif user_delete.upper() == "N":
                break
