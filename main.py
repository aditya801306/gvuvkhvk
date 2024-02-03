from employee_management import EmployeeManagement

def main():
    num_employees = int(input("Enter the number of employees: "))
    
    emp_management = EmployeeManagement()

    for _ in range(num_employees):
        emp_details = input("Enter employee details (employee_id:employee_name:annual_salary): ")
        emp_data = emp_details.split(":")
        emp_management.add_employee_details(emp_data[0], emp_data[1], float(emp_data[2]))

    loan_amount_limit = float(input("Enter the loan amount limit: "))
    employee_details = emp_management.view_employee_details(loan_amount_limit)

    if not employee_details:
        print("No employees found.")
    else:
        print("Employee id {}: - Loan Amount: {}".format(emp_data[0],loan_amount_limit))

if __name__ == "__main__":
    main()
