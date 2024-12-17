# def square(x):
#     return x**2
# print(square(10))

# square = lambda x:x**2
# print(square(10))

# calculation of compount interest and yearly analyisis of interest and principal amount

# year ---> starting balance --> interest --> ending balance

# CI = p*(1+r/t)^tn - p
# I = p*(1+r)^n   formula to calcute interest if it  is compound once per year 

p = 10000
r = 5 / 100  #interest rate (5% per year)
n = 7 # no of years
t = 1 # value of compound interest per year

def  compound_Interest(principle_amount , rateOFInterest , year,time):
    current_balance = principle_amount
    for i in range(1,year+1):
        total_balance = current_balance*pow((1+rateOFInterest/time),time*i) 
        I =total_balance - current_balance
        print(f"{i} ---> {current_balance:.3f} ---> {I:.3f} ---> {total_balance:.3f}")
        current_balance = total_balance


compound_Interest(p,r,n,t)