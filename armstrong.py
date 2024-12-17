# num = int(input("enter the number : "))
# numStr = str(num)
# p = len(numStr)
# sum = 0

# for i in range(p):
#     n = int(numStr[i])
#     sum += pow(n,3)

# if sum == num:
#     print("true")

# else:
#     print("false")





number=input("enter the number:")

l=list(number)
sumOfDigit=0
for i in range(len(l)):
    sumOfDigit+=int(l[i])**3
if (int(number)==sumOfDigit):
    print("true it is an armstrong")
else:
    print("not an armstrong")