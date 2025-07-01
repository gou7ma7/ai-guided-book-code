'''
The usage of star unpacking and yield grammar in Python

For more context and summary of the book, please refer to:
https://gou7ma7.github.io/2025/05/25/book/Python_Cookbook_3rd_Edition/#star-unpacking

'''
# Python “star expressions” can be used to address this problem.
# So, what would happen if there are more than two arguments?
print("# star unpacking")
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)  # ['773-555-1212', '847-555-1212']

# name, email, *list_1, *list2 = record
#    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: multiple starred expressions in assignment

print('=' * 6, end='\n\n')
print('# yield use to split')
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


print('-' * 6, end='\n\n')
print('## if spilt end, yield end, cant call again')
def only_yield_once_generator():
    '''
        so ofcase if only one yield, it can be next() called only once
    '''
    yield 1

# 使用生成器
try:
    gen = only_yield_once_generator()
    print(next(gen))  # print: 1
    print(next(gen))  # StopIteration
    print(next(gen))  # StopIteration
except StopIteration:
    print('StopIteration')


print('=' * 6, end='\n\n')
print('# send to generator')

def once_echo_generator():
    received = yield  # yield on the right => get value from outter; yield on the left => post value to outter
    print(f"Received: {received}")
    yield received
    
gen = once_echo_generator()
next(gen)

next(gen) # Execute print(f"Received: {received}"): Received: None; then executen yield received, then return of next call()
# next(gen) # call() again StopIteration, beacause the once_echo_generator is ended below `yield received`

#print(gen.send("Hello"))

print('=' * 6, end='\n\n')
print('# Don\'t be confused by grammar')
print(' yield is an expression, the same as 3 + 2')
print(' so, easy to understand, that yeild and received = yield are same, they both split parts, only difference is the latter has a variable to store gen.send(value inner')
print('next(gen) == gen.send(None) outer')
print('-' * 6, end='\n\n')

def only_yield_on_right():
    print('will touch 1st yield')       '''part 1'''
    received = yield  # first yield but not send value, may be received will be None
    
    print(f"Received 1st: {received}")
                                       '''part 2'''
    print('will touch 2nd yield')
    
    
    received = yield  # send value in 2nd yield
    print(f"Received 2nd: {received}")   '''part 3'''
    
    
gen = only_yield_on_right()  # init a generator
print(type(gen))

gen.send(None)  # equal next(gen), and execute part 1 
print('as you can see yield split into 3 parts')
next(gen)  # will execute received = yield  # send value in 2nd yield, and which means execute the 2nd-last yield, and part 2

# next(gen)  if do not execute, the part 3 will never be executed, if execute, do part 3, and get stopiteration