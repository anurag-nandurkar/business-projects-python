class Employee:
    def __init__(self,name,hours_worked,hourly_rate):
        """
        Initialize an Employee instance.
        
        :param name: Name of the employee
        :param hours_worked: Number of hours worked in a week
        :param hourly_rate: Hourly wage of the employee
        """
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    def calculate_salary(self):
        overtime_rate = 1.5 * self.hourly_rate
        regular_hours = min(self.hours_worked, 40)
        overtime_hours = max(self.hours_worked - 40, 0)
        regular_pay = regular_hours * self.hourly_rate
        overtime_pay = overtime_hours * overtime_rate
        return regular_pay + overtime_pay
        




class Payroll:
    
    def __init__(self):
        self.employees = []
    def add_employee(self,employee):
        self.employees.append(employee)
    def display_payroll(self):
        print("Payroll Report:")
        print("---------------")
        for employee in self.employees:
            salary = employee.calculate_salary()
            print(f"Employee: {employee.name}, Hours Worked: {employee.hours_worked}, Salary: ${salary:.2f}")
    def export_to_file(self, filename="payroll_report.txt"):
        with open(filename, "w") as file:
            file.write("Payroll Report:\n")
            file.write("---------------\n")
            for employee in self.employees:
                salary = employee.calculate_salary()
                file.write(f"Employee: {employee.name}, Hours Worked: {employee.hours_worked}, Salary: ${salary:.2f}\n")
        print(f"Payroll report exported to {filename}")
            
# Managing payroll
payroll = Payroll()
# User input to add employees
num_employees = int(input("Enter the number of employees: "))


for i in range(num_employees):
    print(f"\nEnter details for Employee {i + 1}:")
    name = input("Name: ")
    hours_worked = float(input("Hours Worked: "))
    hourly_rate = float(input("Hourly Rate: "))
    
    # Create an Employee instance and add it to payroll
    employee = Employee(name, hours_worked, hourly_rate)
    payroll.add_employee(employee)

# Display the payroll report
payroll.display_payroll()

# Export the report to a file
payroll.export_to_file()

        

    
