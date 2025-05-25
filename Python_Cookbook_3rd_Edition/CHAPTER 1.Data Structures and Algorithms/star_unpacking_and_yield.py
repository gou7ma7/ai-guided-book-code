'''
The usage of star unpacking and yield grammar in Python

For more context and summary of the book, please refer to:
https://gou7ma7.github.io/2025/05/25/book/Python_Cookbook_3rd_Edition/#star-unpacking

'''
# Python “star expressions” can be used to address this problem.
# So, what would happen if there are more than two arguments?
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)  # ['773-555-1212', '847-555-1212']

# name, email, *list_1, *list2 = record
#    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: multiple starred expressions in assignment

