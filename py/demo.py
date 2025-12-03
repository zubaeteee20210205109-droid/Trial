# true false

is_hot = False

if is_hot:
    print("It's a hot day") # if ture then all show if false the only last line
print("Enjoy your day")

#another method

is_hot = False
if is_hot:
    print("It's a hot day")
    print("Enjoy your day")
else:
    print("Tt's a cold day")
    print("Wear a warm clothes")

# another2
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Enjoy your day")
elif is_cold:
    print("Tt's a cold day")
    print("Wear a warm clothes")
else:
    print("It's a lovely day")

# another 3
price = 100000
has_good_credit = True
if has_good_credit:
    down_payment = price * 0.9
else:
    down_payment = price * 0.2
print(f"down_payment: ${down_payment}")

# Logical operator
has_high_income = True
has_good_credit = False
if has_high_income and has_good_credit:
    print("Eligible for loan")
#L Or
has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("Eligible for loan")
# and not
has_high_income = True
has_good_credit = True
if has_high_income and not has_good_credit:
    print("Eligible for loan")

#
temp = 35
if temp > 30:           ##  !=  ==
    print("It's a hot day")
else:
    print("It's a cold day")
#
name = "Z"
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a maximum 50 characters")
else:
    print("Name looks good!")
#
weight = int(input('Weight  '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"Yoy are{converted} kilos ")
else:
    converted = weight /0.45
    print(f"Yoy are{converted} pounds ")

 # while loop
