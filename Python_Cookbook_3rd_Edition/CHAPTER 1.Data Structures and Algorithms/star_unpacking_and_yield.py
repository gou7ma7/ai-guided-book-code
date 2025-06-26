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

def simple_generator():
    '''
        yield split parts, each times call next() only split part
    '''
    yield 1  # first time call next() only split 1
    print('run between 1 & 2 next() call')
    yield 2
    yield 3

# 使用生成器
gen = simple_generator()
print(next(gen))  # print: 1
print(next(gen))  # print: 2
print(next(gen))  # print: 3


def only_yield_once_generator():
    '''
        so ofcase if only one yield, it can be next() called only once
    '''
    yield 1

# 使用生成器
gen = only_yield_once_generator()
print(next(gen))  # print: 1
print(next(gen))  # StopIteration
print(next(gen))  # StopIteration

''''''