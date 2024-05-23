"""Code Demo 14/05 03:00
Bardia Ahmadi Dafchahi
"""

class Employee:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id: int, name: str, weekly_salary: float) -> None:
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class CommisionEmpoyee(SalaryEmployee):
    def __init__(self, id: int, name: str, weekly_salary: float, comission: int) -> None:
        super().__init__(id, name, weekly_salary)
        self.comission = comission

    def calculate_payroll(self):
        return self.weekly_salary + self.comission


class PayrollSystem:
    def __init__(self, employees: list) -> None:
        self.employees = employees

    def calculate_payroll(self):
        for employee in self.employees:
            print(f"id: {employee.id},name: {employee.name}, payroll details: {employee.calculate_payroll()}")


def main():
    salEmp = SalaryEmployee(1, 'John Smith', 1500)
    comisionemp = CommisionEmpoyee(2, 'Kevin Bacon', 1000, 250)
    employees = [salEmp, comisionemp]
    system = PayrollSystem(employees)
    system.calculate_payroll()


if __name__ == '__main__':
    main()
