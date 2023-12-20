# open a file
# default mode is 'r' => read
f1 = open('test.txt','a+')
f1.write('applkes\n')
f1.write('iranges\n')
f1.writelines(['this is first line\n', 'this is second line\n'])
f1.close()
