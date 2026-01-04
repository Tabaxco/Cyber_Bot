from random import randint

def rolling(quantity: int = 1, faces: int = 20, operator = None, modifier = None):
    result = []

    for q in range(quantity):
        result.append(randint(1, faces))

    sumresult = sum(result)

    message = f'{sumresult} ⟵ {result} {quantity}d{faces}'

    if operator and modifier:
        if operator == '+':
            sumresult += modifier
            message += f' {operator} {modifier}'
        elif operator == '-':
            sumresult -= modifier
            message += f' {operator} {modifier}'

    return(f'{message}')
