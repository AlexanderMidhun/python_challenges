# Create a function , and calculated using the formula:
# Final Price(FP) = (Product Price of of X )/(Product Price of Y)^2.
# Write python code which can accept the price X and price of Y of a
# Product and calculate the FP. Note: Make sure to use a function
# which accepts the X and Y values and returns the FP value.

def product_final_price(x,y):
    fp = x/(y**2)
    return fp

product_x = int(input("Enter the price of product x : "))
product_y = int(input("Enter the price of product y : "))
final_price = product_final_price(product_x,product_y)
print(final_price)