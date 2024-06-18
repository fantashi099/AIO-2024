import math
import random


def MAE(predicts, targets, n_samples):
    """
    Calculate Mean Absolute Error function 
    """
    output = 0
    for index in range(n_samples):
        print(f'sample-{index}')
        print(f'predict: {predicts[index]} - target: {targets[index]}')
        output += abs(targets[index] - predicts[index])
        print('loss: ', output)
    output /= n_samples
    return output


def MSE(predicts, targets, n_samples):
    """
    Calculate Mean  function 
    """
    output = 0
    for index in range(n_samples):
        print(f'sample-{index}')
        print(f'predict: {predicts[index]} - target: {targets[index]}')
        output += (targets[index] - predicts[index]) ** 2
        print('loss: ', output)
    output /= n_samples
    return output


def RMSE(predicts, targets, n_samples):
    output = 0
    for index in range(n_samples):
        output += (targets[index] - predicts[index]) ** 2
    output = math.sqrt(output / n_samples)
    return output


if __name__ == '__main__':
    n_samples = input('Input number of samples ( integer number ) which are generated: ')
    if not n_samples.isnumeric():
        print('number of samples must be an integer number')
        quit()
    n_samples = int(n_samples)
    loss_name = input('Input loss name: ')
    predicts = [random.uniform(0, 10) for _ in range(n_samples)]
    targets = [random.uniform(0, 10) for _ in range(n_samples)]

    print('loss name: ', loss_name)
    if loss_name.upper() == 'MAE':
        loss = MAE(predicts, targets, n_samples)
    elif loss_name.upper() == 'MSE':
        loss = MSE(predicts, targets, n_samples)
    elif loss_name.upper() == 'RMSE':
        loss = RMSE(predicts, targets, n_samples)

    print('final loss: ', loss)