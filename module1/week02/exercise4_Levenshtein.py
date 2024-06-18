def levenshtein_dist(string1: str, string2: str):
    """ "
    Calculate the distance of how many operators that need to perform to convert string1 into string2
    """
    matrix = [
        [float("inf") for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)
    ]

    for i in range(len(string1) + 1):
        matrix[i][len(string2)] = len(string1) - i

    for j in range(len(string2) + 1):
        matrix[len(string1)][j] = len(string2) - j

    for i in range(len(string1) - 1, -1, -1):
        for j in range(len(string2) - 1, -1, -1):
            if string1[i] == string2[j]:
                matrix[i][j] = min(
                    matrix[i + 1][j], matrix[i][j + 1], matrix[i + 1][j + 1]
                )
            else:
                matrix[i][j] = 1 + min(
                    matrix[i + 1][j], matrix[i][j + 1], matrix[i + 1][j + 1]
                )

    return matrix[0][0]


if __name__ == "__main__":
    string1 = input("Input string 1: ")
    string2 = input("Input string 2: ")

    distance = levenshtein_dist(string1, string2)
    print(distance)
