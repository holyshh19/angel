import pandas as pd

fname= 'masiv.csv'
df= pd.read_csv('masiv.csv', header=None, names=['Name', 'Phone', 'City'])
name= input("Name")
result= df[df['Name'] == name]
if result.empty:
    print("Not found")
else:
    print("Information of user:")
    print(result.to_string(index=False))
