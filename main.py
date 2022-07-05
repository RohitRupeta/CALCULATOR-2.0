print("--==[ CALCULATER ]==--\n\n")
i = 0
while i < 1:

    # Taking Operator Input
    print("What do you want to do?\n"
          "[a] '+' Addition\n"
          "[b] '-' Subtraction\n"
          "[c] '*' Multiplication\n"
          "[d] '/' Divide\n"
          "[e] '^2' Square\n"
          "[f] '^3' Cube\n"
          "[g] '|x|' Modulus or Absolute Function\n"
          "[h] 'n!' Factorial\n"
          "[i] 'SI' Simple Interest")
    ope = input()
    print("")
    # Addition, Subtraction, Multiplication, Divide
    if (ope == 'a') or (ope == 'b') or (ope == 'c') or (ope == 'd'):

        # Two numbers Input
        num1 = float(input("Enter the Number 1 : "))
        num2 = float(input("Enter the Number 2 : "))
        print("")

        # Addition
        if ope == 'a':
            print("= ", num1 + num2)

        # Subtraction
        elif ope == 'b':
            print("= ", num1 - num2)

        # Multiplication
        elif ope == 'c':
            print("= ", num1 * num2)

        # Divide
        elif ope == 'd':
            print("= ", num1 / num2)

    # Square, Cube, Modulus, Factorial
    elif (ope == 'e') or (ope == 'f') or (ope == 'g') or (ope == 'h'):

        # One Number Input
        num = float(input("Enter the Number : "))
        print("")

        # Square
        if ope == 'e':
            print("= ", num * num)

        # Cube
        elif ope == 'f':
            print("= ", num * num * num)

        # Modulus
        elif ope == 'g':
            if num > 1:
                print("= ", num)
            elif num == 0:
                print('0')
            elif num < 1:
                print("= ", -1 * num)

        # Factorial
        elif ope == 'h':
            fact = 1
            for i in range(1, int(num) + 1):
                fact = fact * i
            print("= ", fact)

    # Simple Interest
    elif ope == 'i':
        # Taking Input of Principal, Rate of Interest, Time Period
        p = float(input("Enter the value of Principal : "))
        r = float(input("Enter the value of Rate of Interest : "))
        t = float(input("Enter the value of Time(in year) : "))
        print("")
        si = (p * r * t) / 100
        print("Interest = ", si)
        print("Total Amount = ", si + p)

    # Invalid Inputs
    else:
        print("\nInvalid Input by the User!\n")

    # Restart Loop or not
    print("\nDo you want to run it again?\n"
          "[y] for YES & [n] for NO")
    yes_no = input()

    # Yes
    if (yes_no == 'Y') or (yes_no == 'y'):
        print("")
        continue

    # No
    elif (yes_no == 'N') or (yes_no == 'n'):
        print("\nThank you for using this program")
        i = 1
        break
    # Invalid Input
    else:
        print("\nInvalid input by the user!\n"
              "This program will be restarting again!\n")
        continue

# Exit
exit_pr = input("Press 'ENTER' key to exit!")
