numbers = [12, 75, 150, 180, 145, 525, 50]

for items in numbers:
    if(items>150):
        continue
    elif(items>500):
        break
    elif(items%5==0):
        print(items)
    
