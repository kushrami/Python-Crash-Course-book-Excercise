#Employee:

class Employee():

    def __init__(self,firstname,lastname,annualsalary):

        self.firstname = firstname
        self.lastname = lastname
        self.annualsalary = annualsalary
    
    def give_raise(self,raiseamount=0):
        if raiseamount:
            raisesalary=5000+raiseamount
        else:
            raisesalary=5000
        self.annualsalary += raisesalary