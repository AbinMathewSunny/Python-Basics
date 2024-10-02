class complex:
    def __init__(self,real=0,imaginary=0):
        self.real=real
        self.imaginary=imaginary

    def display(self):
        if self.imaginary >= 0:
            print(str(self.real) + " + " + str(self.imaginary) + "i")
        else:
            print(str(self.real) + " - " + str(-self.imaginary) + "i")
    def __add__(self,x):
        c=complex()
        c.real=self.real+x.real
        c.imaginary=self.imaginary+x.imaginary
        return c
    
A=complex(5,3)
A.display()
B=complex(2,3)
B.display()
sum=A+B
sum.display()