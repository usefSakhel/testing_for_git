name = (input("Enter your name : "))
note = (input("Please enter some notes that you want to save : "))
with open("file.txt", "w")as f:
    f.writelines(name + "\n")
    f.writelines(note)
    
    
with open("file.txt", "r")as f:
    print(f.read())