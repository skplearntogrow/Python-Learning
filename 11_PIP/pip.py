#  Python PIP. Python Package Install Manager.
# Install package, import package to your project
import camelcase
c= camelcase.CamelCase()
txt = "hello world!"
print(c.hump(txt)) # hump() is a third party case converter. Converting string to CamelCase.
xk= camelcase.CamelCase()
mytxt= "santosh kumar!"
print(c.hump(mytxt))