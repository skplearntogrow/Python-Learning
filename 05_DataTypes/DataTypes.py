# Dictionary Practice
Student = {"Student_Name": "Santosh", "Student_Age": 40, "Student_RollNo": 265}
for key, value in Student.items():
    print(f"{key}: {value}")
print(type(Student))

Fruits = {"Fruit1": "Mango", "Price1": 100,"Fruit2": "Orange","Price2": 90}
print("Key Details", list(Fruits.keys()))
print("Value Details",list(Fruits.values()))
print("All details", list(Fruits.items()))
for key, value in Fruits.items():
    print(f"{key}: {value}")