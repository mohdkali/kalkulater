num1=int(input('Enter the first number '))
num3=input('Enter the opration ')
num2=int(input('Enter the Second number '))
a='+'
b='-'
c='*'
d='/'

def add(num1,num2):
    return(num1+num2)

def sub(num1,num2):
    return(num1-num2)

def mul(num1,num2):
    return(num1*num2)

def div(num1,num2):
    return(num1/num2)

if num3 in a:
    print('The value of the opration is '+str(add(num1,num2)))

if num3 in b:
    print('The value of the opration is '+str(sub(num1,num2)))

if num3 in c:
    print('The value of the opration is '+str(mul(num1,num2)))

if num3 in d:
    print('The value of the opration is '+str(div(num1,num2)))


else:
    print('please enter a valid opration')    