
def input_number() -> int:
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def task1() -> None:
    
    num_1 = input_number()
    num_2 = input_number()
    
    try:
        num_result = num_1 / num_2  
    except ZeroDivisionError:    
        print("Error: Division by zero. Please enter a non-zero number.")
        return
    
    

if __name__ == "__main__":
    # Task 1
    print("Task 1") 
    task1()

        