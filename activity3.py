def add(x, y):
    #this function is used for ading numbers
    return x+y
def subtration(x, y):
    #this function is used for subtracting two numbers
    return x-y
def multiply(x, y):
    #this function is used for multipling two numbers
    return x*y
def divide(x, y):
    #this function will divide two numbers
    return x/y

#now we will take inputs fron the user
print("please select the opperation")
print("a, add")
print("b, subtract")
print("c, multipy")
print("d, divide")

choice = str(input("please enter choice (a/b/c/d) :"))

num_1 = int(input("please enter the first number : "))
num_2 = int(input("please enter the second number : "))

if choice == 'a':
    print(num_1, " + ", num_2, " = ", add(num_2, num_1))

elif choice == 'b':
    print(num_1, "-", num_2, "=", subtration(num_1, num_2))

elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("this is an invalid input")
