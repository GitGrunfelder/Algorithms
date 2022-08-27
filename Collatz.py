def collatz(number):
    
        if number != 1: # If you haven't reached 1,
            if number % 2 == 0: # If number is even,
                number = (number // 2) # Update number to result of expression
                print(number) # Print number - skips else - 
            else:
                number = (3 * number) + 1 # If number odd, assign var new expression result.
                print(number) # Print number
            (collatz(number)) # After conditional tree, call function on itself with new updated number variable. 
    
    
try: # Unless exception,
    number = int(input("Please enter a number: ")) # Get input and convert to integer.
    collatz(number) # Use input in function call.
except ValueError: # Unless a value that can't be converted to int is entered,
    print("Please enter an integer greater than or equal to 1 next time.") # In which case this message appears and program ends.

    