print("_________Mini Calculator________")
print("Enter the first number:")
num1=int(input())
print("Enter the second number:")
num2=int(input())
# print(num1)
# print(num2)
print("These are the operators you can use:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
operator=input("Please choose an option from these (1,2,3,4,5):")
if operator == "1":
    print("This is an addition operation")
    print("the sum of the two numbers is :", num1+num2)
if operator == "2":
    print("This is an subtraction operation")
    print("the subtract of the two numbers is :", num1 - num2)
if operator == "3":
    print("This is an multiplication operation")
    print("the product of the two numbers is :", num1 * num2)
if operator == "4":
    print("This is an division operation")
    print("the divident of the two numbers is :", num1 / num2)
if operator == "5":
    print("This is an modulus operation")
    print("the mod of the two numbers is :", num1 % num2)






