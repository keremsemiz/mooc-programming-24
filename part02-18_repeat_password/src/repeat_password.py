# Write your solution here
password = input("Password:")
repeatpassword = input("Repeat password:")

if password != repeatpassword:
    while True:
        print("They do not match!")
        repeatpassword = input("Repeat password:")
        if repeatpassword == password:
            print("User account created!")
            break
else:
    print("User account created!")