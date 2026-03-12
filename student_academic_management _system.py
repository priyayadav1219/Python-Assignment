class Student:
    TOTAL_FEE = 90000

    def __init__(self, sid, name, m1, m2, m3, birth_year, fee_paid):
        self.sid = sid
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.birth_year = birth_year
        self.fee_paid = fee_paid

    def calculate_average(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        print("Average Marks:", avg)
       
    def calculate_cgpa(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        cgpa=avg/10
        print("CGPA:", cgpa)
        
    def calculate_age(self): 
        age=2026-self.birth_year
        print("Age:", age) 

    def  fee_balance(self):  
        balance=Student.TOTAL_FEE-self.fee_paid
        print("Fee Balance:", balance)

    def display_student(self):
        print("Student ID:", self.sid)
        print("Name:", self.name)
        print("Marks:", self.m1, self.m2, self.m3)
        print("Fee Paid:", self.fee_paid)
        self.calculate_average()
        self.calculate_cgpa()
        self.calculate_age()
        self.fee_balance()
        print("------------------------")  

class College:
    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location
        self.students = []

    def register_student(self, student):
        self.students.append(student)

    def display_details(self):
        print("College Code:", self.code)
        print("College Name:", self.name)
        print("Location:", self.location)
        print("\n student Academic Report")
        print("===========================")

        for s in self.students:
            s.display_student()


# Main Program
college = College("ANIL", "ANITS College", "Visakhapatnam")

s1 = Student(46, "Priya", 85, 80, 92, 2006, 50000)
s2 = Student(170, "Lohith", 88, 92, 95, 2006, 45000)
s3 = Student(76, "Nani", 80, 75, 70, 2005, 20000)

college.register_student(s1)
college.register_student(s2)
college.register_student(s3)
college.display_details()
