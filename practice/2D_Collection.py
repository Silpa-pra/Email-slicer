fruits= ["litchi", "mango", "guava", "papaya"]
vegetables= ["potato", "zucchini", "spinat"]
meats= ["chicken", "fish", "pork"]

grocceries = [fruits, vegetables, meats]

#print(grocceries[0] [3])

for x in grocceries:
    #print(x)
    for food in x:
        print(food, end = " ")
    print()