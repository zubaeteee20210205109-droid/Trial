age = int(input("Enter your age: "))
print(age)

try:
    age = int(input("Enter your age: "))
    print(age)
except ValueError:
    print("invalid value")

try:
    age = int(input('Enter your age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be divided by zero')
except ValueError:
    print('invalid value')