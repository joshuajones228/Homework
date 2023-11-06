import datetime as dt

x =dt.datetime.now()
print(x)

'''
def myfunction(fname,dayname):
    dayname = 'Sunday'
    fname = input('name here please:')
    print(f'hello {fname}!, Happy {dayname}')

myfunction("josh",'Saturday')
'''
'''
deprecated code, but saving for grins
var = 'anything'

def myfunction2(var):
    dayname = 'Sunday'
    fname = input('name here please:')
    print(f'hello {fname}!, Happy {dayname}')

myfunction2(var)

'''
'''
def myfunction3(fname,dayname ='Sunday'):
    #fname = input('name here please:')
    print(f'hello {fname}!, Happy {dayname}')

myfunction3("josh")
'''
num1= 5
num2 = 1

try:
    num1/num2
except:
    ZeroDivisionError
    print('you can\'t divide by zero, unless you\'re chuck norris')
else:
    print('good job dividing')
finally:
    print('you should try to divide by different numbers')




