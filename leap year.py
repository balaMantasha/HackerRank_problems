def is_leap(year):
    leap = False
    if(year%4==0) and (year%100 !=0) or (year%400==0):
    # Write your logic here
        leap = True
    return leap

year = int(input())