# BRYANT RAY M. MANALAD
# ITELEC2
# Laboratory #15 - Guided Coding Exercise: While Loop for User Input with a Sentinel Value

def main():
    total_sum = 0

    while True:
        user_input = input("Enter a number (or 'stop' to finish): ")
        if user_input.strip().lower() == "stop":
            break  # Exit the loop
        try:
            number = float(user_input)
            total_sum += number
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'stop'.")

    print("The total sum is:", total_sum)

if __name__ == "__main__":
    main()
    
