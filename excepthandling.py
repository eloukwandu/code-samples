while True:
    try:
        personalNumber=int(input("What is your Personal Indetification Number?:\n"))
        result=(200/personalNumber)
        print(result)
        break

    except ValueError:
        print("Please enter ONLY number")

    except ZeroDivisionError:
        print("You entered a zero value, enter a number:")

    finally:
        print("You are done, thanks")

