'''
text = 'HELLOS MAY I SIT HERE SIR FELLOW GENT'
words = text.split()
print(words)
'''

def fib(n):
    a,b = 1,1
    print(a)
    print(b)
    for i in range(n-1):
        a,b = b,a+b
        print(b)
    return a



def smallest_num(args):

    x=0
    for i in range(0,5):
        x += min(args)
        print(x)

smallest_num([2,3,4,5,6,7,8,8])
