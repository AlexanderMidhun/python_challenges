# Assume you want to build two functions for discounting products on
# a website. Function number 1 is for student discount which discounts
# the current price to 10%. Function number 2 is for additional discount
# for regular buyers which discounts an additional 5% on the current
# student discounted price. Depending on the situation, we want to be
# able to apply both the discounts on the products. Design the above
# two mentioned functions and apply them both simultaneously on
# the price.

def apply_student_discount(price):
    student_discount = 0.10
    discounted_price = price - (price * student_discount)
    return discounted_price

def apply_additional_discount(price):
    additional_discount = 0.05
    discounted_price = price - (price * additional_discount)
    return discounted_price

#both discounts
original_price = int(input("Enter the amount : "))
student_discounted_price = apply_student_discount(original_price)
final_price = apply_additional_discount(student_discounted_price)

print("Original Price: Rs.", original_price)
print("Student Discounted Price: Rs.", student_discounted_price)
print("Final Price with Additional Discount: Rs.", final_price)
