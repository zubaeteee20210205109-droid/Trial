names = ['Zuabet', 'Ahmed', 'Tomal']
print(names)
names[0] ='Zubaet'
print(names)
print(names[1:])
print(names[1:2])
print(names[:])
print(names[-1])

numbers = [3,6,2,10,8,4]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#3x3 matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
for row in matrix:
    for item in row:
        print(item)

numbers = [5,2,1,7,4]
numbers.append(20)
print(numbers)
numbers = [5,2,1,7,4]
numbers.insert(0,10)
print(numbers)
numbers = [5,2,1,7,4]
numbers.remove(5)
print(numbers)
numbers = [5,2,1,7,4]
numbers.clear()
print(numbers)
numbers = [5,2,1,7,4]
numbers.pop()
print(numbers)
numbers = [5,2,1,7,4]
print(50 in numbers)
numbers = [5,2,1,5,7,4]
print(numbers.count(5))
numbers = [5,2,1,5,7,4]
print(numbers.sort())
numbers = [5,2,1,5,7,4]
numbers.sort()
print(numbers)
numbers = [5,2,1,5,7,4]
numbers.sort()
numbers.reverse()
print(numbers)
numbers = [5,2,1,5,7,4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)


numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)