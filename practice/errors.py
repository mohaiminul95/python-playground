while True:
    try:
        age = int(input("Please enter you age: "))
        print(age)
    except:
        print("Please enter numbers only.")
    else:
        print("Thank you!")     
        break   