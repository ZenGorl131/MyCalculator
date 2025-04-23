my_first_number = int(input("Please enter your first number"))
my_operator = input("Please enter your operator")
my_second_number = int(input("Please enter your second number"))

if type(my_first_number) == int and type(my_operator) == str and type(my_second_number) == int:
    if my_operator == "+":
        print(my_first_number + my_second_number)
    elif my_operator == "-":
        print(my_first_number - my_second_number)
    elif my_operator == "*":
        print(my_first_number * my_second_number)
    elif my_operator == "/":
        print(my_first_number / my_second_number)
    else:
        print("Enter valid operator")
