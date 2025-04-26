def main():

    # It will ask the user to input a number.
    curr_value = int(input("Enter a number: "))

    # While loop to double the number until it's 100 or greater

    while curr_value < 100:
        print(curr_value, end=" ")  # Print the current value followed by a space
        curr_value = curr_value * 2  # Double the current value

    # It will print the value when it is 100 or greater
    print(curr_value)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()