class Staff:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def display_info(self):
        return f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}"

class Teacher(Staff):
    pass
    
    


teach=Teacher("Director","Bugalter","1000","Fizika")
print(teach.display_info())
