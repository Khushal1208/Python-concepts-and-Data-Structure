# reverse of given number using while

a = int(input("enter the nunber: "))
res = 0
while a != 0:
    rem = a%10
    a = a//10
    res = res * 10 + rem

print(res) 