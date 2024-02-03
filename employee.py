class Employee:
    def __init__(self, employee_id, employee_name, annual_salary):
        self.__employee_id = employee_id
        self.__employee_name = employee_name
        self.__annual_salary = annual_salary
        self.__loan_amount = 0  # Initialize with default value

    def get_employee_id(self):
        return self.__employee_id

    def get_employee_name(self):
        return self.__employee_name

    def get_annual_salary(self):
        return self.__annual_salary

    def get_loan_amount(self):
        return self.__loan_amount

    def set_loan_amount(self, loan_amount):
        self.__loan_amount = loan_amount

    def calculate_loan_amount(self):
        if self.__annual_salary >= 500000:
            self.__loan_amount = 0.4 * self.__annual_salary
        elif 300000 <= self.__annual_salary < 500000:
            self.__loan_amount = 0.3 * self.__annual_salary
        elif 150000 <= self.__annual_salary < 300000:
            self.__loan_amount = 0.2 * self.__annual_salary
        else:
            self.__loan_amount = 0

