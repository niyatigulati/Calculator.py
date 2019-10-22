def calc(choice, x, y):
    if (choice == 1):
        add(x, y)
    elif (choice == 2):
        sub(x, y)
    elif (choice == 3):
        mul(x,y)
    elif (choice == 2):
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


# TODO 
# main function here 
# Display options on what a calculator can do to perform (1 for add, 2 for sub and so on... )
# This must be in a while loop
