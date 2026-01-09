class Employee:
# Employee Base Class
    def __init__(self, empid, empname, dept, desig, type = "Regular"):
        self.EmpID = empid
        self.EmpName = empname
        self.EmpDept = dept
        self.EmpDesig = desig
        self.EmpType = type # Defaulting to Regular

    def DisplayDetails(self):
        print(f"Employee ID: {self.EmpID}")
        print(f"Employee Name: {self.EmpName}")
        print(f"Department: {self.EmpDept}")
        print(f"Designation: {self.EmpDesig}")
        print(f"Employee Type: {self.EmpType}")


    def CalculateSalary(self):
        pass


class RegularEmployee(Employee):
    def __init__(self, empid, empname, dept, desig, type, basic, hra, esipf, vacdays ):
        super().__init__(empid, empname, dept, desig, type)
        self.Basic = basic
        self.HRA = hra
        self.ESIPF = esipf
        self.DaysOfVacation = vacdays

    def DisplayDetails(self):
        super().DisplayDetails()
        print(f"Basic: {self.Basic}")
        print(f"HRA: {self.HRA}")
        print(f"ESI & PF: {self.ESIPF}")
        print(f"Vacation Days: {self.DaysOfVacation}")

    def CalculateSalary(self):
        tempsalary = 0
        tempsalcut = 0
        tempsalary = self.Basic + self.HRA + self.ESIPF
        if self.DaysOfVacation < 0:
            tempsalcut = self.DaysOfVacation * basic % 22
        tempsalary = tempsalary - tempsalcut
        print(f"The salary for EMPID-{self.EmpID}, EMPNAME {self.EmpName} is {tempsalary}")

class ContractEmployee(Employee):
    def __init__(self, empid, empname, dept, desig, type, constartdt, conenddt, hourlycharge, workhours, conagency):
        (super().__init__(empid, empname, dept, desig, type))
        self.ContractStartDate = constartdt
        self.ContractEndDate = conenddt
        self.HourlyCharge = hourlycharge
        self.WorkHours = workhours
        self.ContractAgency = conagency

    def DisplayDetails(self):
        super().DisplayDetails()
        print(f"Contract Start Date: {self.ContractStartDate}")
        print(f"Contract End Date: {self.ContractEndDate}")
        print(f"Hourly Charges: {self.HourlyCharge}")
        print(f"Workhours: {self.WorkHours}")
        print(f"Contract Agency: {self.ContractAgency}")


    def CalculateSalary(self):
        tempwages = self.HourlyCharge * self.WorkHours * 6 # Rate per hour, no. of hours worked, 6 days work week
        print(f"The wages for Employee {self.EmpID}, {self.EmpName} is {tempwages}")


class EmployeeManager(Employee):

    def __init__(self, empid, empname, dept, desig, type, fixed , variable, carallowance, teamsize, directreports):
        super().__init__(empid, empname, dept, desig, type)
        self.Fixed = fixed
        self.VariablePay = variable
        self.VehicleAllowance = carallowance
        self.TeamSize = teamsize
        self.DirectReports = directreports

    def CalculateSalary(self):
        tempsalary = self.Fixed + self.VariablePay + self.VehicleAllowance
        print(f"The Salary of Manager {self.EmpID}, {self.EmpName}, is {tempsalary}")



Emp1 = Employee("E001", "Gayathri L", "HR", "Assistant", "Regular")
Emp1.DisplayDetails()
Emp2_con = ContractEmployee("E002", "Gayathri LN", "Manufacturing", "Machine Operator", "Contract", "1/1/2025", "31/12/2026", 500, 8, "BestManpower")
Emp2_con.DisplayDetails()
Emp2_con.CalculateSalary()
Emp3_con = RegularEmployee("E003", "L Gayathri", "Accounting", "Accountant", "Regular", 12000, 4000, 1200, 10)
Emp3_con.DisplayDetails()
Emp3_con.CalculateSalary()
Emp4_con = EmployeeManager("E004", "GayathriL", "TechHub", "Senior Manager", "Manager", 30000, 40000, 10000, 30, 15)
Emp4_con.DisplayDetails()
Emp4_con.CalculateSalary()