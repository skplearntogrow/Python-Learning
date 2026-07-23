# Python Membership Operators
# in not in
# To check if a sequence is present in an object
#x in y
#x not in y
fruits= ["Banana","Orange","Apple"]
print("Banana" in fruits)
print("banana" in fruits)
print("Apple" in fruits)
print("Pineapple" not in fruits)
# Membership in Strings
txt= "Hello World"
print("H" in txt)
print("m" in txt)
print("W" in txt)
print("w" in txt)
print('o' in txt)
print('o' not in txt)
if "Banana" in fruits:
    print("Value is present in the Sequence")
else:
    print("Value is not present in the Sequence")