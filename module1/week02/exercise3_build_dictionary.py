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


def build_dictionary(path: str):
    with open(path, 'r') as f:
        content = f.read().replace('\n', ' ').lower()

    output = count_chars(content.split(' '))
    print(output)


if __name__ == '__main__':
    build_dictionary('./P1_data.txt')