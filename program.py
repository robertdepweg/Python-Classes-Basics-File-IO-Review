"""Program code"""

# # System Imports
import os

# # First-party Imports
from employee import Employee
from user_interface import UserInterface
from utils import CSVProcessor


def main(*args):
    """Method to run program"""

    #     # Make a new instance of Employee class
    #     my_employee = Employee("David", "Barnes", 700.25)

    #     # Can't use this because constructor needs parameters
    #     # my_employee = Employee()

    #     # How to use the kwarg
    #     my_employee = Employee("David", "Barnes", 700.25, gets_bonus=True)

    #     # print entire instance of class. __str__ method will be called implicitly
    #     print(my_employee)

    #     # Show how to call a method on an instance
    #     print(my_employee.first_and_last_name())

    #     # Show how to call a property on an instance
    #     print(my_employee.formatted_yearly_salary)

    #     # Show how calling a private method will fall
    #     # print(my_employee.__format_decimal(23.45))

    #     # Call the apply percentage raise method. Then print new salary.
    #     my_employee.apply_percentage_raise(50)
    #     print(my_employee)

    # Make instance of UserInterface class.
    ui = UserInterface()

    # Make instance of CSV processor class.
    csv_processor = CSVProcessor()

    # We can make a list and add instances of employees to it.
    employees = []
    # employees.append(Employee("David", "Barnes", 853.00))
    # employees.append(Employee("James", "Kirk", 463.00))
    # employees.append(Employee("Jean-Luc", "Picard", 9999.00))
    # employees.append(Employee("Benjamin", "Sisko", 123456.00))
    # employees.append(Employee("Kathryn", "Janeway", 123.00))
    # employees.append(Employee("Charles", "McGill", 346.00))

    # Path to CSV file
    # path_to_csv_file = "../cis226-inclass-1-robertdepweg/employees.csv"
    path_to_csv_file = "employees.csv"

    # Reading the CSV file could raise exceptions. Be sure to catch them.
    try:
        # Call the import_csv method sending in out path to the csv
        # and the Employee list that needs to be populated
        csv_processor.import_csv(path_to_csv_file, employees)
    except FileNotFoundError:
        ui.print_file_not_found_error()
    except EOFError:
        ui.print_empty_file_error()

    # Get some input from the user
    selection = ui.display_menu_and_get_response()

    # While the choice they selected is not 2, continue to do work.
    while selection != ui.MAX_MENU_CHOICES:
        # see if the input they sent is equal to 1
        if selection == 1:
            # Create string for concatenation
            output_string = ""
            # Convert each employee to a string and add it to the output_string
            for employee in employees:
                output_string += f"{employee}{os.linesep}"

            # Use the UI class to print out the string
            ui.print_list(output_string)

        # Check for different choice here if there was one to check.

        # Lastly, re-prompt user for input on what to do.
        selection = ui.display_menu_and_get_response()
