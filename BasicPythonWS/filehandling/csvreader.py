import csv
f1 = open('products.csv')
freader = csv.reader(f1)
i = 0
for product in freader:
    if i==0:
        for header in product:
            print(header, end=' ')
        print()
        i+=1
        continue
    for prod in product:
        print(prod, end=' ')
    print()
f1.close()

