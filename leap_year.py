year = input("Enter the year: ")
if len(year) < 4:
    print("The year entered should be a 4 digit number")
else:
    year = int(year)
    if ((year % 400) == 0) or ((year % 4) == 0) and ((year % 100) != 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a leap year")
