# Write your solution here
year = int(input("Year"))
i = 0
leapyear = year

while i < 10:
    year += 1
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"The next leap year after {leapyear} is {year}")
        break