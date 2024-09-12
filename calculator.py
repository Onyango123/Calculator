#simple arithmetic calculator
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def div(x,y):
    return x/y

def mult(x,y):
    return x*y

#how to implement a read operation using ai
x = float(input('enter first value: '))
y = float(input('enter second value: '))

opp = int(input('Type 1 for addition, 2 for subtraction, 3 for division, 4 for multiplication '))

if opp == 1:
    print(add(x,y))
elif opp == 2:
    print(sub(x,y))
elif opp == 3:
    print(div(x,y))
elif opp == 4:
    print(mult(x,y))
else:
    print('operation unavailable')