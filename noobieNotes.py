# my noobie Python notes...
#   - quick reference

# -----------------------------------------------
# quick reference
#

# used for commenting

'''
  # used for multiline commenting/commenting out
'''

print("Hello world!") # outputs to console

a = "Hello world"
print(a)

name = input("Please, enter your name: ")
print(name)

valueInput("Please, enter a value: ")
print(valueInput) # no need to convert the value to a string as it is outputed on its own
print("The value you entered is " + str(valueInput))  # concatinating requires a string appended to a string;
                                                      # that the values to be appended must be converted strings

numValue = 10.122 # a float

newString = str(numValue) # converts float to a string
newInt = int(numValue) # converts float to an it; results in a value of 10
newRounded = round(numValue, 2) # rounds float value to two decimal places; results in 10.12

