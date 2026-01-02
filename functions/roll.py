from random import randint

def rolling(quantity: int = 1,faces: int = 20, modifier: int = 0):
    result = []
    operators = None

    if modifier < 0: 
        operators = '-'
    elif modifier >= 1:
        operators = '+'

    for n in range(quantity):
        result.append(randint(1, faces))

    sumresult = sum(result) + modifier


    return(f'{sumresult} -> {result} + {modifier}')

print(rolling(2, 20, -2))