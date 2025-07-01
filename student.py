from person import Person 

class Student(Person):
    def __init__(self, id, name, age, field_of_study, year_of_study, score_avg):
        super().__init__(id, name, age)
        self.field_of_study = field_of_study
        self.year_of_study = year_of_study
        self.score_avg = score_avg
        
    def getFieldOfStudy(self):
        return self.field_of_study
    
    def getYearOfStudy(self):
        return self.year_of_study
    
    def getScoreAvg(self):
        return self.score_avg
    
    def printStudent(self):
        print(self.getPersonString() + " The fiel of study " + self.getFieldOfStudy() +", the year of study " + str(self.getYearOfStudy()) +", the ave "+ str(self.getScoreAvg()) ) 

    # def getStudentString(self):
    #     return(self.getPersonString(), self.getFieldOfStudy(), self.getYearOfStudy(), self.getScoreAvg())
    def to_dict(self):
        data = super().to_dict()
        data["field of study"] = self.getFieldOfStudy()
        data["year of study"] = self.getYearOfStudy()
        data["score avg"] = self.getScoreAvg()
        return data

    def printMySelf(self):
        self.printStudent() 

    