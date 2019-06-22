from MyModule import Employee as emp

class Devloper(emp.Employee):
    raise_up=1.10
    def __init__(self,fname,lname,pay,plang):
        #Employee.__init__(fname,lname,pay)
        super().__init__(fname,lname,pay)
        self.plang=plang
        
    def display(self):
        super().display()
        print('Plang:-',self.plang)
        

fname=input('Enter your first name:-')
lname=input('Enter your last name:-')
pay=int(input('Enter Employee pay:-'))
plang=input('Enter your programming lang:-')

obj=Devloper(fname,lname,pay,plang);

obj.display()
