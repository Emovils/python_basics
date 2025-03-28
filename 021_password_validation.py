password = "python123"
while True:
    user = input("enter password: ")
    if user == password:
        print("Access granted")
        break
    else:
        print("Wrong access password, please try again!")
