import csv

with open('report.csv')as file:

    reader = csv.reader(file) # ReadFile
    #reader = csv.DictReader(file)# Read Dictionariy
     
    count = 0

    for row in reader: 
        print(row) #Reading Rows

        if count > 100: # Maximum Number of registers
            break

        count += 1
