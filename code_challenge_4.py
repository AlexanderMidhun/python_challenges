# Write a function which would divide two numbers, design the
# function in a manner that it handles the divide by zero exception

def division(num1,num2):
    try:
        division_result = num1/num2
        return division_result
    except:
        print("Division by zero is not allowed.")
    finally:
        print("_____________________________________________")

number_1 = int(input("Enter the first number : "))
number_2 = int(input("Enter the second number : "))
result = division(number_1,number_2)
print(number_1,'/',number_2,'=',result)