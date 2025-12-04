check = False
while check == False:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    option = input("Please Select Preferred Function or Type 'Quit' To Exit: ").strip().lower()
    if option == "1" or option == "add":
        try:
            num1 = int(input("Enter Num 1: "))
            num2 = int(input("Enter Num 2: "))
            sum = num1 + num2
            print(f"The sum of {num1} and {num2} is {sum}")
        except ValueError:
            print("Not a proper value")
    elif option == "2" or option == "subtract":
        try:
            num3 = int(input("Enter Num 3: "))
            num4 = int(input("Enter Num 4: "))
            difference = num3 - num4
            print(f"The difference of {num3} and {num4} is {difference}")
        except ValueError:
            print("Not a proper value")
    elif option == "3" or option == "multiply":
        try:
            num5 = int(input("Enter Num 5: "))
            num6 = int(input("Enter Num 6: "))
            product = num5 * num6
            print(f"The product of {num5} and {num6} is {product}")
        except ValueError:
            print("Not a proper value")
    elif option == "4" or option == "divide":
        try:
            num7 = int(input("Enter Num 7: "))
            num8 = int(input("Enter Num 8: "))
            quotient = num7/num8
            print(f"The quotient of {num7} and {num8} is {quotient}")
        except ValueError:
            print("Not a proper value")
        except ZeroDivisionError:
            print("Can't divide by 0")
    elif option == "quit":
        check == True