Student_info = {
    "name": "Zubaet Ahmed",
    "age": 22,
    "is_verified": True
}
print(Student_info["name"])
print(Student_info["age"])
print(Student_info.get("birthdate"))
print(Student_info.get("birthdate","jan 2 2003"))

#or
Student_info["name"] = "Tomal"
Student_info["birthdate"] = "jan 2 2003"
print(Student_info["name"])
print(Student_info["birthdate"])


phone = input ("phone: ")
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
}
output = ""
for ch in phone:
   output+= digit_mapping.get(ch, "!") + ""
print(output)