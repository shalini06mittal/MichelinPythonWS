# default values for parameters in function. These are called as named arguments
# rest are called as positional arguments
'''
 default  arguments always should be in hte last and they should not be 
 followed by any positional arguments
 There can be any number of mix of positional and default arguments, BUT default 
 always come in the last
 '''
def takeOrder(item,drink='lemonade', desert: str | None ='vanialla icecream')-> str:
    print(item,'along with', drink,'and',desert,'is ready')
    return 10

# takeOrder( 'pizza', 'coke','muffin')
takeOrder('pizza')
takeOrder('burger','fanta')
takeOrder('sandwiches','blue lagoon','cookies')
# keyword arguments
takeOrder(drink='masala chaas',desert='rasgulla',item='dosa')
takeOrder('idli',desert=45,drink='masala chaas')
print('hey', end=10)
'''
create a function calculate that takes amount and discount as parameters
provide default discount as 5% if none provided and return the calculated amount
'''