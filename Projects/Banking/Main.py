def main():
    print("\nEnter What u want: ")
    want = input("Login: 1 | Register: 2   : ")
    
    usr = All()
    
    if want=="2":
        All.Register()
    elif want=="1":
        All.Login()
    else:
        print("Invalid input :/\n\n\n")
        main()




""" REGISTER/LOGIN CLASS """
class All:
    """Class for Registration/Loggin into app
    """
    def fname_F(): #Input First Name
        All.fname = input("Enter First Name: ")
        while(All.check(All.fname, 5, 15)==-1):
            All.fname = input("Enter First Name: ")
        All.fname = All.fname[0].upper() + All.fname[1:].lower()
        
    def lname_F(): #Input Last Name
        All.lname = input("Enter Last Name: ")
        while(All.check(All.lname, 8, 20)==-1):
            All.lname = input("Enter Last Name: ")
        All.lname = All.lname[0].upper() + All.lname[1:].lower()
            
    def gmail_F(): #Input gmail
        All.gmail = input("Enter Gmail: ")
        while(All.check(All.gmail, 10, 40, typ=1)==-1):
            All.gmail = input("Enter Gmail: ")
            
    def Age_F(): #Input age
        while(True):
            All.age = input("Enter Age: ")
            if len(All.age)>3 or len(All.age)<1:
                print("Incorrect age")
                continue
            try:
                if int(All.age)<18 or int(All.age)>112:
                    print("Age between <18,112>")
                    continue
            except:
                print("Wrong Input !")
                continue
            break
        
    def PhoneNum_F(): #Input phone number
        All.PhoneNum = input("Enter Phone Number: ")
        while(All.check(All.PhoneNum, 9, 9, typ=2)==-1):
            All.PhoneNum = input("Enter Phone Number: ")
            
    
    def Register():
        """function for registration
        """
        global i
        i = 0
        
        All.fname_F()
            
        All.lname_F()
        
        All.Age_F()
        
        All.gmail_F()
        
        All.PhoneNum_F()
            
        print("You are now registered user !!!\n")
        Database.usersGmail.append(All.gmail) #Adds gmail to database, for later check (can't be 2 accounts with same gmail (at least here)) 
        Database.usersPhones.append(All.PhoneNum) #Same here (can't be 2 accounts with same phone)
        
        globals()[f"user{i}"] = User(i, All.fname, All.lname, All.age, All.gmail, All.PhoneNum) #Creates user with all given information | np user0, user1, user2
        eval('user'+i).Inf()
        main()
        i+=1

        
        
    def check(var:str, minLen: int, maxLen: int,typ:int=0) -> int:
        """Checks given variable in way u want, returns -1 if variable does not meet given requirements else None

        Args:
            var (str): variable to check
            minLen (int): minimum length of variable
            maxLen (int): max length of variable
            typ (int, optional): if set to 1 it will correct: variable like it's gmail | if set to 2 will correct as Phone Number. Defaults to 0.

        Returns:
            int: returns -1 if there is "error" in variable (its smaller than minimum length etc)
        """
    
        if len(var)>maxLen or len(var)<minLen: #Checks if length of given variable is in range <minLen, maxLen>
            print(f"{var} be in range <{minLen},<{maxLen}>")
            return -1
        
        if typ==0: #Checks First/Last Names
            for _ in var:
                if _ in "1234567890`!@#$%^&*()-=_+[]{}\|;:'?/.>,<~" or _ in  '"':
                    print("No numbers or special characters allowed !")
                    return -1
                
        elif typ==1: #Checks Gmails
            for _ in var:
                if _ in "`!#$%^&*()=+[]{}\|;:?/>,<~" or _ in  '"':
                    print("Used invalid special characters in gmail !")
                    return -1
            if '@gmail.com' not in var:
                print("There must be \'@gmail.com\' in gmail !")
                return -1
            for _ in Database.usersGmail:
                if _==var:
                    print("Gmail already in use !")
                    return -1
            
        elif typ==2: #Checks Phone Numbers
            for _ in var:
                if _ not in "1234567890":
                    print("Only numbers allowed !")
                    return -1
            for _ in Database.usersPhones:
                if _==var:
                    print("Phone number already in use !")
                    return -1
        
        else:
            raise Exception("typ must be in range 0-2 both included !")
        
        
        
    def Login():
        """ Function for loggin
        """
        print(Database.usersGmail)
        print(Database.usersPhones)
        
        gmail = input("Enter Gmail: ")
        phoneNum = input("Enter Phone Number: ")
        
        if gmail not in Database.usersGmail or phoneNum not in Database.usersPhones:
            print("Gmail OR Phone Numer is invalid !")
            main()

        print(eval('user'+str(Database.usersGmail.index(gmail))).Inf())
        print(f"Welcome !")
        
    






""" SYSTEM CLASSES """
class Database:
    usersGmail = []
    usersPhones = []
    
class User:
    UsersArr = []
    def __init__(self, indx:int, fname: str, lname: str, age: int, gmail: str, phoneNumber: str):
        self.fname = fname
        self.lname=lname
        self.age=age
        self.gmail=gmail
        self.phoneNumber=phoneNumber
        self.indx = indx
        User.UsersArr.append(f'{gmail}_{lname}')
        
    def Inf(self):
        print(f"First Name: {self.fname}, Last Name: {self.lname}, Age: {self.age}\nGmail: {self.gmail}, Phone Number: {self.phoneNumber}")




            


if __name__ == '__main__':
    main()