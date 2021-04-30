import Person
import sys

class Student(Person.Person)
    def __init__(self, name, id, gender, height, weight,department):
        super().__init__(name, id, gender, height, weight)
        self.department=department

    def showInfo:
        print(self.name,self.id,self.department)

    def setDepartment(self,newDepartment):
        self.department=newDepartment

    def getDepartment(self):
        return self.department

if __name__=="__main__"
    if len(sys.argv)>6:
        Student=Student(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
        student.showInfo("new student Id:  ")
        newName=input("new student Name:  ")
        newDepartment=input("new Department:  ")
        student.setID(setID)
        student.setName(setName)
        student.setDepartment(setDepartment)
        student.showInfo()
