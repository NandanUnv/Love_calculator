# This code is only written based on some concepts based 

print("Welcome to love calculator")

x = input("Enter your name:")
y = input("Enter the other name:")

xy = x.lower()
yy = y.lower()

lis1 = ['t', 'r', 'u', 'e']
lis1_val = []
lis2 = ['l','o','v','e']
lis2_val=[]


for i in lis1:
    count=0
    for j in xy:
        if(j==i):
            count+=1

    for j in yy:
        if(j == i):
            count += 1
    lis1_val.append(count)

for i in lis2:
    count = 0
    for j in xy:
        if (j == i):
            count += 1

    for j in yy:
        if (j == i):
            count += 1
    lis2_val.append(count)

str1 = str(sum(lis1_val))
str2 = str(sum(lis2_val))

l_s = str1+str2
if(l_s<'10' and l_s>90):
    print(f'your love score is:{l_s}%, you go together like coke & mentos')
elif(l_s>'40' and l_s<'50'):
    print(f'your love score is:{l_s}%, you are alright together')
else:
    print(f'your love score is:{l_s}%')
