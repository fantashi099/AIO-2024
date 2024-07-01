import streamlit as st


def main(vocabs):
    st.title('Word Correction using Levenshtein Distance')
    word = st.text_input('Word:')

    if st.button('Compute'):
        # compute levenshtein distance
        leven_dist = dict()
        for vocab in vocabs:
            leven_dist[vocab] = levenshtein_dist(word, vocab)
        
        # sorted by distance
        sorted_distances = dict(sorted(leven_dist.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distances)


def load_vocab(file_path: str):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


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
                matrix[i][j] = matrix[i+1][j+1]
            else:
                matrix[i][j] = 1 + min(
                    matrix[i + 1][j], matrix[i][j + 1], matrix[i + 1][j + 1]
                )

    return matrix[0][0]


if __name__ == '__main__':
    vocabs = load_vocab('./data/vocab.txt')
    main(vocabs=vocabs)