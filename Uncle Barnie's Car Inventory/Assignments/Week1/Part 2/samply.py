# This sample will request input from a user about an Employee.
# It will take all the input and send it to a function to store the data.
# After the data is stored it will send a prompt to the user to either input more data or display the results.



def gather_input():
    """
        Gather the input from the user and prompt at the end to enter more data or exit to display data.
    """
    # Create variables to help
    employee_dict = {}

    # Ask for the employees Last Name
    employee_dict['last_name'] = str(input("What is the employee's Last name? "))

    # Ask for the employees First Name
    employee_dict['first_name'] = str(input("What is the employee's First Name? "))

    # Ask for the employees age
    employee_dict['age'] = str(input("What is the employee's age? "))

    # Ask for the eomployee's ID
    employee_dict['employee_id'] = str(input("What is the employee's ID? "))

    # Ask if there is another employee to be recorded.
    more_employees = str(input('Is there another employee to record? '
                           '\nPlease enter Yes to continue or No to exit and display employees.'))
    if more_employees == 'Yes' or more_employees == 'Y':
        print('Please continue with the following prompts to add another employee.')
        done = False
    elif more_employees == "No" or more_employees == "N":
        print('Displaying information and then exiting application.')
        done = True
    else:
        print('Displaying information and then exiting application.')
        done = True
    return employee_dict, done


def display_data(data):
    """
    This function will display the data to the screen.
    :param data: This will be the data passed from the user.
    :return: None
    """
    for employee_data in employee_data_list:
        print('Employee Information:\n')
        for key,value in employee_data.items():
            print (key + ': ' + value)

def store_data(data):
    """
    This function will store the information in a data structure
    :param data:
    :return:
    """
    employee_data_list.append(data)


if __name__ == '__main__':

    # create variable to store list of data inside.
    employee_data_list = []
    is_done = False

    # Check to see if we are done with adding employees.
    while not is_done:

        # call the function gather_input and return employee data.
        employee_data, is_done = gather_input()

        # store the data into our list from above.
        store_data(employee_data)

    display_data(employee_data_list)
