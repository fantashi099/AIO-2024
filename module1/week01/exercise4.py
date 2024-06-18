# Given
def is_number(n,type) :
    try :
        if type == 'float':
            float(n)
        elif type == 'int':
            int(n)
    except ValueError:
        return False
    return True


def cal_factorial(x):
    """
    Calculate the factorial of a number
    """
    output = 1
    for index in range(2, x+1):
        output *= index
    return output


def cal_sin(x,n):
    """
    Calculate the Sin of radian x with n loops
    """
    output = 0
    for index in range(n):
        output += ((-1)**index * (x ** (2*index + 1))) / cal_factorial(2*index + 1)
    return output


def cal_cos(x,n):
    """
    Calculate the Cos of radian x with n loops
    """
    output = 0
    for index in range(n):
        output += ((-1)**index * (x ** (2*index))) / cal_factorial(2*index)
    return output


def cal_sinh(x, n):
    """
    Calculate the Sinh of radian x with n loops
    """
    output = 0
    for index in range(n):
        output += (x ** (2*index + 1)) / cal_factorial(2*index + 1)
    return output


def cal_cosh(x, n):
    """
    Calculate the Cosh of radian x with n loops
    """
    output = 0
    for index in range(n):
        output += (x** (2*index)) / cal_factorial(2*index)
    return output


if __name__ == '__main__':
    x = input('Input x = ')
    n = input('Input n = ')

    if not is_number(x, 'float'):
        print('x must be float')
        quit()
    
    if not is_number(n, 'int'):
        print('n must be in')
        quit()

    x = float(x)
    n = int(n)

    type = input('Input function to calculate ( sin | cos | sinh | cosh ): ')
    if type == 'sin':
        output = cal_sin(x, n)
    elif type == 'cos':
        output = cal_cos(x, n)
    elif type == 'sinh':
        output = cal_sinh(x, n)
    elif type == 'cosh':
        output = cal_cosh(x, n)
    else:
        print('Function is not supported')
        quit()
    
    print(output)