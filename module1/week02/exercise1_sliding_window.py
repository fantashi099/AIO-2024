def slide_window(array: list, k: int):
    """
    Calculate the maximum value of sliding window array 
    """
    output = []
    for index in range(len(array) - k + 1):
        if index + k > len(array):
            index = len(array) - k
        max_neighbor = max(array[index : index+k])
        output.append(max_neighbor)
    return output


if __name__ == '__main__':
    array = input('Input list of array (e.g: 3 4 5 1 -44 5 10 12 33 1): \n')
    k = int(input('Size of sliding window: '))
    if k < 1:
        print('k must higher or equal 1')
        quit()
    array = [int(x) for x in array.split(' ')]
    output = slide_window(array, k)
    print(output)