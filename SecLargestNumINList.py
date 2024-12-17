li = [5,3,8,4,2]
n = len(li)
# for i in range (n):
#     for j in range (0,n-i-1):
#         if(li[i] > li[i+1]):
#            li[j] , li[j+1] = li[j+1] , li[j]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):  
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]  
                swapped = True
        if not swapped:
            break

    return arr

print(bubble_sort(li))
print(li[len(li)-2])



