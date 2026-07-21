**Topics Covered:**

Python - Strings:
1. Strings in python are surrounded by either by single quotation marks or double quotation marks
2. "hello" is same as 'hello'
3. You can display a string literal with print() built-in function
4. Quotes inside Quotes. For ex print("This is 'Beautiful'"), print('This is "AI Era"')
5. Assigning a String to a Variable.
6. Multiline Strings using double quotes. For ex: a = """ This is AI era 
#and Python is crucial to learn
#and be ready to adapt to this AI era"""
7. Multiline strings using single quotes.
a= '''This is an AI era
and Python is crucial to learn
and be ready to adapt to this AI era'''
8. Strings are Arrays. Like many Programming languguages, Strings are array of unicode characters. Python does not have char data type so a single character in python is string with a length of 1. For ex: a= "Hello World", print(a[1])
9. Looping through a String. For ex: for x in "Banana", print(x)
Again in Python, a single character in a string is a string with a length of 1.
10. Python String is an array of unicode characters. ex: a= "Hello World". a[1],a[2],a[3],a[4],a[5],a[],a[7],a[8],a[9],a[10],a[11],a[12]
11. String Length. Ex: x= "Hello World", print(len(x))
12. Check String. To check if a particular character is present or not present in a string, in python we use in keyword
13. "in" keyword. ex: x= "Hello World", print("World" in x); print("Hello" in x); print("llo" in x)
14. Use "in" keyword in if statement. ex: M= "Hello World", if "World" in M: print("World is present in Text")
15. Check if NOT. To check if a certain phrase or character is not present, use "not in".
16. "not in" keyword. ex: txt= "The Best things in life are free", print("expensive" not in txt)
17. "not in" another example using if statement: txt= "The Best things in life are free", if "expensive" not in txt: print("Expensive word is not in txt variable")

**Key points:**
-> Single & Double Quotation string.
-> Assigning string to a Variable
-> Multiline Strings
-> Strings as an Array
-> Looping through a String. Loop through the letters in the word "banana". for x in "Banana": print(x[2])
-> String Length. x = "Banana" print(len(x))
-> Check String, to check if a certain phrase or character is present in a String. "in" keyword. x= "Banana has lot of vitamins" print("Vitamins" in x). if "Banana" in x: print("Yes, 'Banana' is present in x")
-> Check if not, to check if a certain character or phrase is not present in a string. "not in" keyword. print("Random" not in x). if "Random" not in x: print('"Random" word is not available in X')


Python - Slicing Strings:
1. Return range of characters by using slice syntax. b= "Banana" print(b[2:5]). Specify start index, and the end index seperated by colon to retrieve specific characters in a string. end index[not included] in the output.
2. Slice from Start. By leaving start index. The range start from first character in string print(b[:5]).
3. Slice to the end. By leaving out end index, the range will go to the end. print(b[2:])
4. Negative Indexing. Use negative indexs to start range from end of the string. b= "Hello World!" print(b[-5:-2])

Python - Modifying Strings:
Python has certain built-in methods to modify a string
1. Upper Case: The upper() method returns string in upper case. a= "Hello, World" print(a.upper())
2. Lower Case: The lower() method returns string in lower case. print(a.lower())
3. Remove White spaces: strip() method to remove white spaces at the beginning or at the end. print(a.strip())
4. Replace String: replace() method will replace a string with another string. print(a.replace("H","J"))
5. Split String: split() method splits string into a sub strings if it find a seperator in the string. print(a.split(,))

Python - String Concatenation:
To concatenate or combine two strings , use + Operator
1. Merge variable a with Variable b into Variable c.
2. To add space between them , add a " ".

Python - Format Strings:
As we learned in Python Variables chapter, we cannot combine String and Numeric with + operator as in below age= 36 txt= "My name is john,i am" +16 print(txt)
Cannot combine String with numeric with + Operator

But we can combine Strings and Numbers with f-strings. f-strings were introduced in Python 3.6

1. To specify a String as f-string, just put f before string literal and add {} as placeholder for variables and other operations.#age= 36 txt= "I am John and my age is {age}" print(txt)
2. syntax: f"...{placeholder}"
3. Placeholder: A placeholder can contain variables, opertions, functions and modifiers to format the value.
        ex: price= 60 txt= "The price is {price) dollars"} print(txt)
4. A placeholder can include a modifier to format the value. A modifier is included by adding : followed by legal formatting type like .2f which means fixed point number with 2 decimals
        ex: price= 59 txt= "The Price is {price:.2f} dollars" print(txt)
5. A placeholder can contain math operations txt= "The Price is {5*8} dollars"
Impt: We can combine a String with a number using f-string. A f-string is mentioned as f"string {placeholder to format value}". A placeholder can be a variable, function, operations and a modifier.





