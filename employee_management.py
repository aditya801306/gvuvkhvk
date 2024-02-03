from employee import Employee
class EmployeeManagement:
    def __init__(self):
        self.__employee_list = []

    def add_employee_details(self, employee_id, employee_name, annual_salary):
        employee = Employee(employee_id, employee_name, annual_salary)
        employee.calculate_loan_amount()
        self.__employee_list.append(employee)

    def view_employee_details(self, loan_amount):
        result_dict = {}
        for employee in self.__employee_list:
            if employee.get_loan_amount() > loan_amount:
                result_dict[employee.get_employee_id()] = employee.get_loan_amount()
        return result_dict
