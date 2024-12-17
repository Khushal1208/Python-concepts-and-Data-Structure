li = [1001,2152,3443,65,23542,121,3443,89,98,151,7997]

# Use a separate list to store palindrome numbers
filtered_list = []

for i in range( len(li)):
    a = li[i]
    original = a
    res= 0 
    while a != 0:
        rem = a%10
        a = a//10
        res = res*10 + rem
    if res == original:
        filtered_list.append(original)
        

filtered_list.sort()
print(filtered_list)

print(filtered_list[-1])




    
        