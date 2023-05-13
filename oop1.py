class employee:
    
    def __init__(self,n,s,a):
        self.name=n
        self.salary=s
        self.age=a
       
    def disp(self):
        print("Name=", self.name)      
        print("Salary=", self.salary)
        print("Age=",self.age)
            
emp1=employee("SUN",2000,35)
emp1.disp()
print(f"emp1 {emp1.name}")
print(f"emp1 {emp1.salary}")

print(f"emp1 {emp1.age}")
            
            