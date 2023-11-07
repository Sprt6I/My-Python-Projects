class Person:
    
    def __init__(self, fname: str, lname:str, age: int | float):
        self.__fname = fname
        self.__lname = lname
        self.__age = round(age, 1)
        
    def Inf_(self):
        print(f'First Name: {self.__fname}\nLastName: {self.__lname}\nAge: {self.__age}')
        return [self.__fname, self.__lname, self.__age]
    
    @property
    def Name_(self):
        return self.__fname
    
    @Name_.setter
    def Name_(self, name):
        if self.check_(name)==-1: return -1
        
        self.__fname = name      
        return 0  
    
    @staticmethod
    def check_(value):
        if len(value)<3: return -1
        for i in value:
            if i in '12334567890':
                return -1
            
p1 = Person('Ja','hehe',123)
p1.Name_ ='Nie Ja1'
print(p1.Name_)