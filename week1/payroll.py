from typing import Union

class Employee:

    def __init__ (self, fname, lname, id: Union[int,float], hourlyPay: float):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.hourlyPay = hourlyPay

    def Pay(self, hoursWorked: float):
        if hoursWorked <= 40 :
            salary= hoursWorked * self.hourlyPay
            return float(salary)
        else:
            totalPay = 40 * self.hourlyPay
            overTime = hoursWorked - 40
            oTRate = 1.5 * self.hourlyPay
            totalPay += overTime * oTRate
            return float(totalPay)  


firstName = input("Please enter your first name ")
lastName = input("Please enter your last name ")
hours = input("Please enter your hours worked ")
identification = input("Please enter your employee id ")
rate = input("Please input your hourly pay ")


employee1 = Employee(firstName, lastName, int(identification), float(rate)) 

# print(employee1.fname, employee1.lname, employee1.id, employee1.hourlyPay)

salary = employee1.Pay(float(hours))

print(firstName + " " + lastName + " Paycheck amount is " + str(salary))


# print(
# employee1['fname']
# employee1['lname']
# employee1['id']
# employee1['hourlyPay'])