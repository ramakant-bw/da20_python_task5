
def doOperation(val1, val2, operation):
    if operation == 'sub':
        result = f'operation = {operation}   val1 = {val1},  val2 = {val2} and (val1 - val2) = {val1 - val2}'
    
    elif operation == 'mul':
        result = f'operation = {operation}   val1 = {val1},  val2 = {val2} and (val1 * val2) = {val1 * val2}'

    elif operation == 'div':
        result = f'operation = {operation}   val1 = {val1},  val2 = {val2} and (val1 / val2) = {val1 / val2}'

    elif operation == 'add':
        result = f'operation = {operation}   val1 = {val1}, val2 = {val2} and (val1 + val2) = {val1 + val2}'
        
    else:
        result = f'your operation did not match operation = {operation}'

    return result



op = doOperation(5,2, 'div')

print('op', op)