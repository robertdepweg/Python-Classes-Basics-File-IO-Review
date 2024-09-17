"""User interface module"""


class UserInterface:
    """Class for doing all ui in the program"""

    # Menu choices constant
    MAX_MENU_CHOICES = 2

    # No constructor as we do not need to accept any parameters or set
    # any class level variables. but, this does not mean that we can't do
    # that in the event that we do need something.

    def display_menu_and_get_response(self):
        """Display menu and get response"""

        self._print_menu()
        self._print_prompt()

        # get user input
        selection = input()

        # while selection is not valid, re-get selection
        while not self._selection_is_valid(selection):
            # print error message
            self._print_menu_error()
            # reprint menu choices
            self._print_menu()
            self._print_prompt()
            # get user input again
            selection = input()

        # at this point we know the choice is a valid number of either
        # a 1 or 2. So, there is no need to put this in a try.
        return int(selection)

    def print_list(self, output_list):
        """Print list of employees"""
        print("Printing the list")
        print(f"{'First Name':<10} {'Last Name':<20} {'Weekly Salary':>14}")
        print(output_list)

    def _print_menu(self):
        """Print menu to user"""
        print("What would you like to do?")
        print("1. Print List")
        print("2. Exit")

    def _print_prompt(self):
        """Print main prompt"""
        print("> ", end="")

    def _print_menu_error(self):
        """Print menu choice error"""
        print("This is not a valid entry")
        print("Please make a valid choice")
        print()

    def _selection_is_valid(self, selection):
        """Verify selection is valid"""
        # Declare a return value variable and init to False
        return_value = False

        try:
            # Parse the selection into a choice var
            choice = int(selection)

            # if choice is between 0 and the MAX_MENU_CHOICES
            if choice > 0 and choice <= self.MAX_MENU_CHOICES:
                # Set the return va;ue to True
                return_value = True
        # If not a valid int, this exception will get raised.
        except ValueError:
            # Ensure return value is False. Should not need this.
            return_value = False

        # return the return_value
        return return_value
