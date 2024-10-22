#khateeja khatoon
#oct 22 2024 
# this program prints  a message for multiples of 3, 5 or between 1 and 50

for num in range(1, 51):
    if num  % 3 == 0 and num  % 5 == 0:
       print("divisible by both")   
    elif num  % 3 == 0:
         print ("divisible by three")
    elif num % 5 == 0:
         print ("divisible by five")

    else: 
        print(num)          



































