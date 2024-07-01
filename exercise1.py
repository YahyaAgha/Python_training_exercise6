#EX1 Solution

with open('number_from_1_to_10.txt', 'w') as file:
    for i in range(1,11):
        file.write(f"{i}\n")