size = int(input("Enter the size of the list: "))
# nums = []
# for i in range(size):
#     nums.append(int(input()))  # Convert input to integers
nums = [int(input()) for _ in range(size)]  

def calculate_mex(subarray):
    """Calculate the Minimum Excluded Value (MEX) of a subarray."""
    mex = 1
    while mex in subarray:
        mex += 1
    return mex


# mex = []

all_mex = set()


# for j in range(size):
#     new_nums = []
#     for i in range(size - j):
#         new_nums.append(nums[i + j])
#     min_num = min(nums)
#     while min_num in new_nums:
#         min_num += 1
#     if min_num not in mex:
#         mex.append(min_num)


# Generate all subarrays and calculate their MEX
all_mex = set()
for i in range(size):
    for j in range(i, size):
        subarray = nums[i:j+1]  # Subarray from index i to j
        all_mex.add(calculate_mex(subarray))

mex_min = 1
while mex_min in all_mex:
    mex_min += 1

print("The minimum excluded value (MEX) is:", mex_min)