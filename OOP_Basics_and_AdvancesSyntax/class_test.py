class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        
new_person = Person("Vivek","Khimani")
new_person.firstname = "Vivko"
print(new_person.firstname)
