from person import Person 

class Employee(Person):
    def __init__(self,id, name, age, field_of_work, salary):
        super().__init__(id, name, age)
        self.fielf_of_work = field_of_work
        self.salary = salary
        
    def getFieldOfWork(self):
        return self.fielf_of_work
    
    def getSalary(self):
        return self.salary
    
    def printEmployee(self):
        print(self.getPersonString() + ", the field of work is " + self.getFieldOfWork() + ", the salary is " + str(self.getSalary())) 

    def to_dict(self):
        data = super().to_dict()
        data["field_of_work"] = self.getFieldOfWork()
        data["salary"] = self.getSalary()
        return data    
        
    def printMySelf(self):
        self.printEmployee()