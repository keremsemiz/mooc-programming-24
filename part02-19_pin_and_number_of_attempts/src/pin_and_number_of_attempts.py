# Write your solution here
attempts = 0
pin = int(input("PIN:"))
if pin == 4321:
    print("Correct! It only took you one single attempt!")
elif pin != 4321:
    while True:
        attempts += 1
        if pin != 4321:
            print("Wrong")
            pin = int(input("PIN:"))       
        
        elif pin == 4321:
            print(f"Correct! It took you {attempts} attempts")
            break