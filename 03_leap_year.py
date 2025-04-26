# This is a Python file that checks if a given year is a leap year or not.
def main():
    print("Please enter a year to check if it's a leap year or not.")
    print("A leap year is a year that is evenly divisible by 4, except for end-of-century years.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()


## Solution

# Yeh code leap year check karne ke liye hai.
def main():
    # Get the year to check from the user
    year = int(input('Please input a year: '))

    if year % 4 == 0:  # Checking whether the provided year is evenly divisibly by 4
        if year % 100 == 0:  # Checking whether the provided year is evenly divisibly by 100
            if year % 400 == 0:  # Checking whether the provided year is evenly divisibly by 400
                print("That's a leap year!")
            else:  # (Not divisible by 400)
                print("That's not a leap year.")
        else:  # (Not divisible by 100)
            print("That's a leap year!")
    else:  # (Not divisible by 4)
        print("That's not a leap year.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
