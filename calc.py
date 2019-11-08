def calc(choice, x, y):
    if (choice == 'a'):
        add(x, y)
    elif (choice == 's'):
        sub(x, y)
    elif (choice == 'm'):
        mul(x,y)
    elif (choice == 'd'):
        div(x,y)


#  the below functions must display the output for the given arithmetic
# TODO 
def add(a, b):
  print(f'The summation is {a+b}')
  
def sub(a, b):
  print(f'The difference is {a-b}')
  
def mul(a, b):
  print(f'The product is {a*b}')
  
def div(a, b):
  print(f'The division is {a/b}')

def main():
    n=input('''input your choice \n"a" to add \n"s" to subtract \n"m" to multiply" \n"d" to divide' )
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    calc(n,a,b)
