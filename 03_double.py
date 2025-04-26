def double(num: int):
    return num * 2

# There is no need to edit code beyond this point

def main():
    # ANSI escape codes for bold and italic
    BOLD_ITALIC = '\033[1m\033[3m'  # Bold and italic
    RESET = '\033[0m'  # Reset to normal text
    num = int(input("Enter a number: "))
    num_times_2 = double(num)

    # Displaying the result with bold and italic
    print(f"Double that is {BOLD_ITALIC}{num_times_2}{RESET}")

if __name__ == '__main__':
    main()