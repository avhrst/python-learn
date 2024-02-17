
def task3() -> None:
    
    try:
        file = open("sample.txt", "r")
        print(file.read())
        file.close()
    except Exception as e:         
        print(f"Error: {e}")
           
        

if __name__    == "__main__":
    print("Task 3") 
    task3()