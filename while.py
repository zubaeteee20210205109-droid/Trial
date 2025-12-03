
Gues =1
while Gues < 10:
    print('*' * Gues)
    Gues = Gues + 1
if Gues == 10:
    print()

#
#Guess:1
#Guess:2
#Guess:3
#Sorry you failed!
#Guess:9
#You win!
number = 9
Guess_count = 0
Guess_limit = 3
while Guess_count < Guess_limit:
    Guess = int(input("Guess: "))
    Guess_count += 1
    if Guess == number:
        print("You won!")
        break
else:
    print("Sorry you failed")
    