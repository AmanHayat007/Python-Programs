class employee:
    ec=0
    def __init__(self,n,s):
        self.name=n
        self.salary=s
        employee.ec+=1
        def disp(self):
            print("Name=", self.name)      
            print("Salary=", self.salary)
            def empcount(self):
                print("Total employee: = %d" %employee.ec)
            emp1=employee("SUN",2000)
            emp1.disp()
            print("emp1.name")
            print("emp1.salary")
            emp2=employee("MOON",1000)
            emp2.disp()
            print("emp2.name")
            print("emp2.salary")