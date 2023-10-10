def main():
    print("\nEnter What u want: ")
    want = input("Login: 1 | Register: 2   : ")
    
    if want=="2":
        Register()
    elif want=="1":
        Login()
    else:
        print("Invalid input :/\n\n\n")
        main()






""" MAIN FUNCTIONS """

def Register():
    fname = input("Enter First Name: ")
    check(fname, 5, 15)
    
    lname = input("Enter Last Name: ")
    check(lname, 8, 20)
    
    gmail = input("Enter Last Name: ")
    check(lname, 8, 20)
    



def Login():
    pass









""" MAIN CLASSES """
class Database:
    usersName = []
    
class User:
    def __init__(self, fname, lname, age, phoneNumber):
        self.fname = fname
        self.lname=lname
        self.age=age
        self.phoneNumber=phoneNumber






"""HELP FUNCTIONS"""

def check(var:str, minLen: int, maxLen: int):
    if len(var)>maxLen or len(var)<minLen:
        print("Name must be in range <5,15>")
        Register()   
    for _ in check:
        if _ in "1234567890`!@#$%^&*()-=_+[]{}\|;:'?/.>,<~" or _ in  '"':
            print("No numbers or special characters in name !")
            Register()
            


if __name__ == '__main__':
    main()