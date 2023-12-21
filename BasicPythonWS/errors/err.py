'''
logical errors : python will not track
'''
#print(5+5) # logical error where i wanted * but used +

# syntax errors
# print(('akjsdh')

# error -> stack overflow/ out of memory/ 

# exception handling => try block, except
l1 = [1,2,3,4,5]

# try:
#     no = l1[1] # indexerror
#     print(no+2)
#     print(no/5) # division error
# except IndexError as e:
#     print('list index should be within {} - {}'.format(0,len(l1)-1))
# except ZeroDivisionError as e:
#     print('Denominator cannot be zero', e)
# except Exception as e:
#     print('something went wrong',e)
# finally:
#     print('that executes irrespective exception occurs or not')
#     print('is used to clean up')
# print('bye')

def fileOp():
    f1 = None
    try:
        f1 = open('test1.txt','r')
        return f1.read()
    except:
        print('cannot open file')
        raise Exception('Check if file exists')
    else:
        print('else clause is execute if no exception occurs')
    finally:
        print('file closing')
        if f1 is not None:
            print('f1 not none')
            f1.close() 
try: 
    data = fileOp()
except:
    print('error')
# print(data)