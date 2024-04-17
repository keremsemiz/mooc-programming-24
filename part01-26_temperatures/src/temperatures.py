# Write your solution here
# C = (°F - 32) × 5/9
# Brr! It's cold in here!

temp = int(input("Please type in a temperature (F): "))
celcius = (temp - 32) * 5/9
print(f"{temp} degrees Fahrenheit equals {celcius} degrees Celsius") 

if celcius < 0:
    print("Brr! It's cold in here!")


