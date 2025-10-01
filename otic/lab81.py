s1=input("???  ")
sum=0
dob=1
for i in s1.split():
    if i.isdigit():
        sum+=int(i)
        dob*=int(i)
    else:
        continue

print("Сума:", sum)
print("Добуток:", dob)