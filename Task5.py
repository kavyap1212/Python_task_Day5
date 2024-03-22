# 1. Output of Following code
data = [10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x: x > 4, data)
print(list(result))

# 2. Python code using Lambda function to check every element of a List for Int or Str
data1 = [10, 501, 'happy', 37, 100, 999, 'me', 351]
print("List taken is: ", data1)
result_int = list(filter(lambda x: isinstance(x, int), data1))
result_str = list(filter(lambda x: isinstance(x, str), data1))
print("Integers in the list are: ", result_int)
print("Strings in the list are: ", result_str)

# 3. Python Lambda function to create a fibonacci series from 1 to 50
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
result_fib = [fibonacci(i) for i in range(1, 5)]
print(result_fib)

# 4. Python function to validate the Regular Expression for the following:-
import re

# a) Email Address
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
print("Enter email address to validate : ")
email = input()
if(re.fullmatch(regex_email, email)):
        print("Valid Email")
else:
        print("Invalid Email")

# b) Mobile numbers of Bangaladesh
regex_bangladesh = r'^([01]|\+88)?\d{11}$'
print("Enter the number to check if its bangaladesh mobile number: ")
B_num = input()
if(re.match(regex_bangladesh, B_num)):
        print("Valid Bangladesh Mobile number")
else:
        print("Invalid Bangladesh Mobile number")
# c) Telephone numbers of USA
regex_USA = r'^([01]|\+1)?\d{10}$'
print("Enter the number to check if its USA number: ")
USA_num = input()
if(re.match(regex_USA, USA_num)):
        print("Valid USA number")
else:
        print("Invalid USA number")
# d) 16 character Alpha-Numeric password composed of alphabets of Uppercase,Lowercase,Special Characters,Numbers.
regex_pwd = r'[A-Za-z0-9@#$%^&+=]{16,}'

print("Enter the pwd: ")
pwd = input()
if(re.fullmatch(regex_pwd, pwd)):
        print("Valid Password")
else:
        print("Invalid passwod")