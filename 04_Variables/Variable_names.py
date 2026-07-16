#Variable names in Python learning and practicing.
#Variable name must start with letter or underscore character.
#variable name can contain letters, numbers and alpha numberic and underscore characters.
#Variable name cannot start with number.
#Variable name cannot contain special characters other than underscore.
#Variable names are case sensitive meaning MYVar and myvar are two different variables.
#Variable names cannot be a reserved python keyword.
from tokenize import Name


my_var="TestCase 1"
print(my_var)
myVAR ="TestCase 2"
print(myVAR)
MY_VAR="TestCase 3"
print(MY_VAR)
_MY_VAR="TestCase 4"
print(_MY_VAR)
myvar2="TestCase 5"
print(myvar2)
#Camel case variable name: Each word except first word start with capital letter.
newVariableName="Testcase 10"
print(newVariableName)
myVariableName="TestCase 6"
print(myVariableName)
#Pascal case variable name: Each word start with capital letter.
MyVariableName="TestCase 7"
print(MyVariableName)
#Snake case variable name: Each word is separated by underscore character.
my_variable_name="TestCase 8"
MY_VARIABLE_NAME="TestCase 9"
print(type(my_variable_name))
print(MY_VARIABLE_NAME)
#Non-legal variable names.
#2MyVariableName="TestCase 11"
#print(2MyVariableName)
#10X="TestCase 12"
#print(10X)
#MyVariable-Name="TestCase 13"
#print(MyVariable-Name)
#_X-y="TestCase 14"
#print(_X-y)