import datetime as dt

x =dt.datetime.now()
print(x)

fname = 'anything'
dayname = 'anything'

def myfunction(fname,dayname):
    dayname = 'Sunday'
    fname = input('name here please:')
    print(f'hello {fname}!, Happy {dayname}')

myfunction(fname,dayname)

var = 'anything'

def myfunction2(var):
    dayname = 'Sunday'
    fname = input('name here please:')
    print(f'hello {fname}!, Happy {dayname}')

myfunction2(var)