#This sample will request input from a user about an Employee.
#It will take all the input and output it in a format to the screen.

#Ask for the employees Last Name
last_name = input("What is the employee's Last name?")

#Ask for the employees First Name
first_name = input("What is the employee's First Name?")

#Ask for the employees age
age = input("What is the employee's age?")

#Ask for the eomployee's ID
employee_id = input("What is the employee's ID?")

#Output the information to the screen in a format.
#The \n means a newline
#The \t means a tab
#The {number} is how you are going to put your values in the print statement.
#Make sure to take notice of the .format() function call at the end of the print statement.
print ('Employee Information:\n\n \tFirst Name: {0}\n \tLast Name: {1}'
       '\n \tAge: {2}\n \tEmployee ID: {3}\n'
       .format(first_name,last_name,age,employee_id))
