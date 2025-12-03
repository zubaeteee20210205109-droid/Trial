from functools import total_ordering


def greet_user():
    print("hi there")
    print("welcome aboard")


print("Start")
greet_user()
print("Finish")


def greet_user(first_name, last_name):
    print(f"hi {first_name, last_name}")
    print("welcome aboard")

print("Start")
greet_user(first_name="Zubaet", last_name="Ahmed")
greet_user(first_name="Tomal",last_name="Ahmed")
print("Finish")


def square(number):
    return number * number
print(square(3))

def square(number):
    print( number * number)
print(square(3))




def emoji_converter(messages):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "☹️"
    }
    output = " "
    for word in words:
        output += emojis.get(word, word) + " "
    return output
message = input (">")
print(emoji_converter(message))
