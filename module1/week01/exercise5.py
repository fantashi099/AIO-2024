def cal_nroot(x,n):
    """
    Calculate the value of nth root
    """
    output = x ** (1/n)
    return output


def mean_different_nroot_error(target, predict, n, p):
    """
    Calculate the Mean Difference of nth Root Error
    """
    y = cal_nroot(target, n)
    y_hat = cal_nroot(predict, n)
    output = (y - y_hat) ** p
    return output


if __name__ == '__main__':
    target = input('y = ')
    predict = input('y_hat = ')
    n = input('n = ')
    p = input('p = ')

    target = float(target)
    predict = float(predict)

    n = int(n)
    p = int(p)

    output = mean_different_nroot_error(target, predict, n, p)
    print(output)