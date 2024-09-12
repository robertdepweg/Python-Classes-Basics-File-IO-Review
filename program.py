"""Program code"""

# System Imports
# None

# First-party Imports
from employee import Employee


def main(*args):
    """Method to run program"""

    # Make a new instance of Employee class
    my_employee = Employee("David", "Barnes", 700.25)

    # Can't use this because constructor needs parameters
    # my_employee = Employee()

    # How to use the kwarg
    my_employee = Employee("David", "Barnes", 700.25, gets_bonus=True)

    # print entire instance of class. __str__ method will be called implicitly
    print(my_employee)

    # Show how to call a method on an instance
    print(my_employee.first_and_last_name())

    # Show how to call a property on an instance
    print(my_employee.formatted_yearly_salary)

    # Show how calling a private method will fall
    # print(my_employee.__format_decimal(23.45))

    # Call the apply percentage raise method. Then print new salary.
    my_employee.apply_percentage_raise(50)
    print(my_employee)

    # We can make a list and add instances of employees to it.
    employees = []
    employees.append(Employee("David", "Barnes", 853.00))
    employees.append(Employee("James", "Kirk", 463.00))
    employees.append(Employee("Jean-Luc", "Picard", 9999.00))
    employees.append(Employee("Benjamin", "Sisko", 123456.00))
    employees.append(Employee("Kathryn", "Janeway", 123.00))
    employees.append(Employee("Charles", "McGill", 346.00))

    for employee in employees:
        print(employee)
