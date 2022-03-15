l = input("Enter words to search: ")

count = 0

with open("animals.txt", 'r')as file:
    
    for line in file:

        words = line.split()
        
        for i in words:

            if(i==l):

                count = count + 1

print("Count = ", count)
