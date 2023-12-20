import csv
f1 = open('products.csv','w')
fwriter = csv.writer(f1)
fwriter.writerow(['Id','Name','Description','price'])
fwriter.writerows([
    [1,'apples','delicious',120],
    [2,'banana','healthy',80],
    [3,'grapes','sweet and tasty',100],
    [4,'strawberries','organic farm',220],
])
f1.close()