# METHOD 1
def using_if_statement():
    month = int(input("Enter a number:"))

    if (month == 1):
        print("JANUARY")
    elif (month == 2):
        print("FEBRUARY")
    elif (month == 3):
        print("MARCH")
    elif (month == 4):
        print("APRIL")
    elif (month == 5):
        print("MAY")
    elif (month == 6):
        print("JUNE")
    elif (month == 7):
        print("JULY")
    elif (month == 8):
        print("AUGUST")
    elif (month == 9):
        print("SEPTEMBER")
    elif (month == 10):
        print("OCTOBER")
    elif (month == 11):
        print("NOVEMBER")
    elif (month == 12):
        print("DECEMBER")
    else:
        print("Invalid month")

#METHOD 2
def using_dictionary():
    dic_month = {
        1:"JANUARY",
        2:"FEBRUARY",
        3:"MARCH",
        4:"APRIL",
        5:"MAY",
        6:"JUNE",
        7:"JULY",
        8:"AUGUST",
        9:"SEPTEMBER",
        10:"OCTOBER",
        11:"NOVEMBER",
        12:"DECEMBER"
    }

    while True:
        try:
            month = int(input("Enter the Number:"))
            if 1<=month<=12:
                name_of_the_month = dic_month[month]
                print("Month :" , name_of_the_month)
            else:
                print("Invalid month, Please enter a number between 1 - 12")
        except ValueError:
            print("The value must be in numeric.")

print("Method 1 , Using if statement")
using_if_statement()
print("______________________________________________")
print("Method 2 , using dictionary")
using_dictionary()

