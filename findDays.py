# # finding the no of days in a months

# month = int(input("month: "))
# if(month == 2){
#     year  = int(input("year: "))
#     if(year%400 == 0 or(year%4==0 and year%100 != 0)){
#         print("29 days ")
#     }
#     else{
#         print("28 days")
#     }
# }
# list1 = [1,3,5,7,8,12]
# list2 = [4,6,9,11]
# if(month in list1){
#     print("31 days")
# }
# if(month in list2){
#     print("30 days")
# }

month = int(input("Enter month (1-12): "))

if month == 2:
    year = int(input("Enter year: "))
    # Check for leap year
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print("29 days")
    else:
        print("28 days")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
elif month in (4, 6, 9, 11):
    print("30 days")
else:
    print("Invalid month")
