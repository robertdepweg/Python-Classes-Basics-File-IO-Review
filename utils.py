# First party imports
from employee import Employee


class CSVProcessor:
    """CSV Processor class to read and process an employee CSV"""

    # No constructor. Do not need any arguments. Same as UI.
    def import_csv(self, path_to_csv_file, employee_list):
        """Accept a path to a csv file then read the fue in and process it
        into a list of employee instances"""

        # With open of file
        with open(path_to_csv_file, "r", encoding="utf-8") as file:
            # Priming line read
            line = file.readline().replace("\n", "")
            # While the line is not None
            while line:
                # Process the line
                self.__process_line(line, employee_list)
                # Read next line.
                line = file.readline().replace("\n", "")

    def __process_line(self, line, employee_list):
        """Process a line from a CSV file"""
        # Split line by comma
        parts = line.split(",")

        # Assign each part to a var (in the real world, don't trust data)
        first_name = parts[0]
        last_name = parts[1]
        weekly_salary = float(parts[2])

        # Add a new employee to the list with the properties of what was read in.
        employee_list.append(Employee(first_name, last_name, weekly_salary))
