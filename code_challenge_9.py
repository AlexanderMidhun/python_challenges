# Calculate the value of mathematical expression x*(x+89)^7 where
# x= 3 using lambda expression

expression = lambda x: x * (x + 89) ** 7
result = expression(3)
print(result)
