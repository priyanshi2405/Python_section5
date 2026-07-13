class employee:
    def __init__(self,name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age
    
    def get_salary(self):
        return self.salary , self.name , self.age

    def get_info(self):
        print(f"the name is {self.name} , salary is {self.salary} and the age is {self.age}.")


e1 = employee("jhon doe",34000 , 21)
e2 = employee(55000,"raj varma",22)
e1.get_salary()
e1.get_info()
e2.get_info()