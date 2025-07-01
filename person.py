class Person:
    def __init__(self, id, name, age):
        self._id = id 
        self._name = name
        self._age = age 
        
    def getId(self):
        return self._id
    
    def getName(self):
        return self._name

    def getAge(self):
        return self._age
    
    def getPersonString(self):
        return ("The person with ID number "+ str(self.getId()) + " is named " + self.getName() + " and is " + str(self.getAge()) + " years old")
        
    def printMySelf(self):
        print(self.getPersonString())
        
    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "age": self._age
        }
        
if __name__ == "__main__":
    test_id = 10
    test_name = "test_name"
    test_age = 80
    person = Person(test_id,test_name,test_age) 
    if person.getId() != test_id:
        print("Error: id should be: " + str(test_id) + " but i got " + str(person.getId()))
    if person.getName() != test_name:
        print("Error: name should be: " + test_name + " but i got " + person.getName())
    if person.getAge() != test_age:
        print("Error: age should be: " + str(test_age) + " but i got " + str(person.getAge()))
        
        

