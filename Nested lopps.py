#(x,y)
#(0,0)
#(0,1)
#(0,2)
#(1,0)
#(1,1)
#(1,2).....

#for x in range (4):
#    for y in range (3):
#        print(f"({x},{y})")

#for x in range(5):
#    if x == 0 or x == 2:
#       for y in range (5):
#         print("x", end="")
#    else:
#        for y in range (2):
#           print("x", end="")
#    print()
numbers = [5,2,5,2,2]
for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)


