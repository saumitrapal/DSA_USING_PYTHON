#--------------------------------------------------Note---------------------------------------#
# Pointers: is a memory address of a variable. which actually store the memory address.
# Not variable value itself.

# Pointers for integers
num1 = 10
num2 = num1

#Before updating num2
print("Print Boolean value: ", id(num1) == id(num2))
print("Print memory address of num1", id(num1))
print("Print memory address of num2", id(num2))

#After updating num2
num2 = 20
print("Print Boolean value: ", id(num1) == id(num2))
print("Print memory address of num1: ", id(num1))
print("Print memory address of num2", id(num2))


# Pointers for dictonary
dict1 = {
    "value": 10
}
dict2 = dict1

# Before updating dict2
print("Print Boolean value: ", id(dict1) == id(dict2))
print("Print Boolean value: ", id(dict1['value']) == id(dict2['value']))
print("Print memory address of dict1", id(dict1))
print("Print memory address of dict2", id(dict2))

# After updating dict2 value
dict2['value'] = 20
print("Print Boolean value: ", id(dict1) == id(dict2))
print("Print Boolean value: ", id(dict1['value']) == id(dict2['value']))
print("Print memory address of dict1", id(dict1))
print("Print memory address of dict2", id(dict2))

