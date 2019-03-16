import os
import csv
import random
s=1
for i in range(1,10):
    x=open(f"file_0{i}.csv",'x') #creates new .csv file
    y=[["#","num1","num2","num3","num4","num5"]] #initialising for the header
    while os.stat(f"file_0{i}.csv").st_size<2000:
        y.append([s,random.randint(1,500),random.randint(1,500),random.randint(1,500),random.randint(1,500),random.randint(1,500),random.randint(1,500)])
        #to create the values to append to the .csv file at corresponding columns
        s=s+1
        with open (f"file_0{i}.csv",'w') as randwrite: #to write the .csv file
            writer = csv.writer(randwrite)
            writer.writerow(y) #appends the values to the cooresponding columns
