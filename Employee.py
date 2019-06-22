class Employee:
    raise_up=1.04
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.email=fname+lname+'@gmail.com'
        self.pay=pay

    def display(self):
        print('Name:',self.fname+' '+self.lname)
        print('Email:',self.email)
        print('Pay   :',self.pay)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_up)

