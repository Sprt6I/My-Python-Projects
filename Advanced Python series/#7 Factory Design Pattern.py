from abc import ABCMeta

class IPerson(metaclass=ABCMeta):
    
    def person_method():
        """ Inference Method """
        
        
class Student(IPerson):
    def __init__(self):
        self.name = 'Basic Student Name'
        
    def person_method(self):
        print("I am student")
        
        
class Teacher(IPerson):
    def __init__(self):
        self.name = 'Basic Teacher Name'
        
    def person_method(self):
        print('I am teacher')
        
        
class PersonFacotory:
    
    @staticmethod
    def BuildPerson_(personType: str):
        if personType=='Student':
            return Student()
        elif personType=='Teacher':
            return Teacher()
        print('Wrong input')
        raise ValueError('Wrong Input, must be: (Student) or (Teacher)')
    
    
if __name__=="__main__":
    choice = input('What u want to create: ')
    person = PersonFacotory.BuildPerson_(choice)
    person.person_method()
    