import math 


# Given
def is_number(n):
    try :
        float(n) # activation_fn - casting the string to ‘float ‘.
                    # If string is not a valid ‘float ‘ ,
                    # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def sigmoid(x):
    """
    Calculate sigmoid function 
    """
    output = 1 / (1 + math.e**(-x))
    return output 


def relu(x):
    """
    Calculate RELU function
    """
    output = max(0, x)
    return output


def elu(x, alpha):
    """
    Calculate ELU function
    """
    if x <= 0:
        x = alpha * (math.e**x - 1)
    return x


def excerise2(x, activation_fn, alpha=0.01):
    """
    Calculate one of activion functions {sigmoid, relu, elu}
    Input: x - input value
           alpha - parameter for elu function
           activation_fn - activation_fn of activation functions {sigmoid, relu, elu}
    Output: result from the chosen activation function
    """
    if not is_number(x):
        print('x must be a number')
        return None
    x = float(x)
    if activation_fn == 'sigmoid':
        output = sigmoid(x)
    elif activation_fn == 'relu':
        output = relu(x)
    elif activation_fn == 'elu':
        output = elu(x, alpha)
    else:
        print(f'{activation_fn} is not supported')
        return None
    print(f'{activation_fn}: f({x})={output}')
    return None


if __name__ == '__main__':
    x = input('Input x = ')
    activation_fn = input('Input activation Function ( sigmoid | relu | elu ): ')
    excerise2(x, activation_fn)