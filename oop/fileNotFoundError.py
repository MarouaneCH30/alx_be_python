import os

def search_file():

    files = os.listdir()
    find_file = input("Enter the file you want to search:")
    try:
        if not find_file in files:
            
            raise FileNotFoundError
    except FileNotFoundError:
        print("The file is not available in your directories")
    except Exception:
        print("Invalid input")
    
    else:
        print(f"The file youve entered, {find_file} is available \n")
    finally:
        print(f"These are the available files in your directory \n {files}")
        print("\nBye!")

search_file()
    