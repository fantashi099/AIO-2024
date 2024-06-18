def count_chars(string: str):
    """
    Count each charater in a string
    """
    dictionary = {}
    for char in string:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    dictionary = dict(sorted(dictionary.items()))
    return dictionary


if __name__ == '__main__':
    string = input('Input string: ')
    print(count_chars(string))