list=[2,4,5,6]

for i in list:
    if(i==4):
        break
    print(i)


for i in list:
    if(i==4):
        continue
    print(i)

# empty for loop
for i in list:
    pass
print('End')
