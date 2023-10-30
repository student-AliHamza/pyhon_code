class students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade    

    def details(self):
        print("your name is",self.name)
        print("your age is",self.age)
        print("your grade is",self.grade)
    



name = input('enter your name')
age = int(input("enters your age"))
grade = input("enter your grade")
obj_students = students(name,age ,grade)
obj_students.details()