def main():
    print("\nEnter What u want: ")
    want = input("Login: 1 | Register: 2   : ")
    
    usr = All()
    
    if want=="2":
        All.Register()
    elif want=="1":
        Login()
    else:
        print("Invalid input :/\n\n\n")
        main()






""" MAIN FUNCTIONS """
class All:
    def fname_F():
        All.fname = input("Enter First Name: ")
        print(All.check(All.fname, 5, 15))
        while(All.check(All.fname, 5, 15)==-1):
            
            All.fname = input("Enter First Name: ")
        
    def lname_F():
        All.lname = input("Enter Last Name: ")
        while(All.check(All.lname, 8, 20)==-1):
            All.lname = input("Enter Last Name: ")
            
    def gmail_F():
        All.gmail = input("Enter Gmail: ")
        while(All.check(All.gmail, 10, 40, gmail=True)==-1):
            All.gmail = input("Enter Gmail: ")
    
    def Register():
        c = 0
        
        All.fname_F()
            
        All.lname_F()
        
        while(True):
            age = input("Enter Age: ")
            if len(age)>3 or len(age)<1:
                print("Incorrect age")
                continue
            elif int(age)<18 or int(age)>112:
                print("Age between <18,112>")
                continue
            break
        
        All.gmail_F()
        
        print("You are now registered user !!!")
        Database.usersGmail.append(All.gmail) #Adds gmail to database, for later check (can't be 2 accounts with same gmail (at least here)) 
        Database.usersPhones.append(111222333) #Same here (can't be 2 accounts with same phone)
        
        globals()[f"{All.fname}_{All.lname}"] = User(All.fname, All.lname, age, All.gmail, 111222333)
        print(globals()[f"{All.fname}_{All.lname}"].age)

        
        
    def check(var:str, minLen: int, maxLen: int,gmail:bool=False) -> int:
        """_summary_

        Args:
            var (str): variable to check
            minLen (int): minimum length of variable
            maxLen (int): max length of variable
            gmail (bool, optional): if set to True it will not correct: @ . 1234567890 ' . in variable. Defaults to False.

        Returns:
            int: returns -1 if there is "error" in variable (its smaller than minimum length etc)
        """
    
        if len(var)>maxLen or len(var)<minLen:
            print(f"Name {var} be in range <{minLen},<{maxLen}>")
            return -1
        if gmail==False:
            for _ in var:
                if _ in "1234567890`!@#$%^&*()-=_+[]{}\|;:'?/.>,<~" or _ in  '"':
                    print("No numbers or special characters allowed !")
                    return -1
        else:
            for _ in var:
                if _ in "`!#$%^&*()=+[]{}\|;:?/>,<~" or _ in  '"':
                    print("Used invalid special characters in gmail !")
                    return -1
    

def Login():
    pass









""" MAIN CLASSES """
class Database:
    usersGmail = []
    usersPhones = []
    
class User:
    def __init__(self, fname: str, lname: str, age: int, gmail: str, phoneNumber):
        self.fname = fname
        self.lname=lname
        self.age=age
        self.gmail=gmail
        self.phoneNumber=phoneNumber




            


if __name__ == '__main__':
    main()