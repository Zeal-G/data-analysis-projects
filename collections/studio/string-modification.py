my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

my_string_slice = my_string[:3]
print(my_string_slice)

my_string_slice_new = my_string[3:10] + my_string_slice

# Use a template literal to print the original and modified string in a descriptive phrase.


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
