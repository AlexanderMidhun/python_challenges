#Simple Interest:(Principal * Rate * Time) / 100

def s_interest(p , r , t):
    return (p*r*t)/100

principal = int(input("Principal Amount: "))
rate = int(input("Interest Rate : "))
time = int(input("Time : "))

simple_interest = s_interest(principal , rate , time)
print("Simple Interest:" , simple_interest)