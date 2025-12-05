import pandas as pd

df= pd.read_csv('massive.txt', sep=r'\s', header=None)
s1= pd.Series(df[0])
s2= pd.Series(df[1])
s3= pd.Series(df[2])
numbers= set(s1) & set(s2) & set(s3)

with open('one.txt', 'w') as f:
    for num in numbers:
        f.write(str(num)+ '\n')
print(s1)
print(s2)
print(s3)
print(numbers)