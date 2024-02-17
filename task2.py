
class ValueTooHighError(Exception):
    """ Raised when the value is too high """
    
    def __init__(self, number,message=""):
        self.number = number
        if message == "":
            self.message = f"Value {number} is too high"
        else:    
            self.message = message
        super().__init__(self.message)

def input_number() -> int:
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def task2() -> None:
    
    num_1 = input_number()
    
    if num_1 > 100:
        raise ValueTooHighError(num_1)
    else:
        print(f"Number {num_1} is accepted.")    
    

if __name__ == "__main__":
    print("Task 2") 
    task2()

        