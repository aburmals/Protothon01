import os
import csv
import random
s=1
for i in range(1,10):
    x=open(f"file_0{i}.csv",'x')
    y=[["#","num1","num2","num3","num4","num5"]]
    while os.stat(f"file_0{i}.csv").st_size<2000:
        y.append([s,random.randint(1,500),random.randint(1,500),random.randint(1,500),random.randint(1,500),random.randint(1,500),random.randint(1,500)])
        s=s+1
        with open (f"file_0{i}.csv",'w') as randwrite:
            writer = csv.writer(randwrite)
            writer.writerow(y)
