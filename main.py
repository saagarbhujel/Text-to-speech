import os 

if __name__ == '__main__':
    print("Welcoem to Text-To-Speech")
    x = input("Enter the text :")
    command=f"say{x}"
    os.system(command)