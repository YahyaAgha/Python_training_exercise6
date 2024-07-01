## Exercise 2 ...

with open('input_file.txt','a') as file:

    while True:
        input_user =input("Please enter your text to append to a file: Input_file.txt or 'stop' to exit: ")
        if input_user.lower() == 'stop':
            break
        file.write(input_user + "\n")


print ("File has been created with your text ^_^")
