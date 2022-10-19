"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    def get_pay(self):
        return self.base_pay() + (self.commission.value if self.commission else 0)

    def __str__(self):
        return f"{self.name} works on a {self.desc()}" + \
               (f" and receives a {self.commission.description}" if self.commission else "" ) +\
               f". Their total pay is {self.get_pay()}."


class HourlySalary(Employee):
    def __init__(self, name, hours, hourlypay = 0, commission = 0):
        super().__init__(name, commission)
        self.name=name
        self.hours=hours
        self.hourlypay=hourlypay

    def base_pay(self):
        return self.hourlypay * self.hours

    def desc(self):
        return f"contract of {self.hours} hours at {self.hourlypay}/hour"

class MonthlySalary(Employee):
    def __init__(self, name, monthlypay = 0, commission = 0):
        super().__init__(name, commission)
        self.name = name
        self.monthlypay = monthlypay

    def base_pay(self):
        return self.monthlypay

    def desc(self):
        return f"monthly salary of {self.monthlypay}"

class BonusCommision:
    def __init__ (self, bonus = 0):
        self.description = f"bonus commission of {bonus}"
        self.value = bonus

class ContractCommission:
    def __init__(self,contractsLanded, commissionPerContract):
        self.description = f"commission for {contractsLanded} contract(s) at {commissionPerContract}/contract"
        self.value = contractsLanded * commissionPerContract



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlySalary('Billie', 4000 )

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlySalary('Charlie', 100 , 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlySalary('Renee', 3000, ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlySalary('Jan', 150, 25, ContractCommission(3,220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlySalary('Robbie', 2000, BonusCommision(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlySalary('Ariel', 120, 30, BonusCommision(600))
