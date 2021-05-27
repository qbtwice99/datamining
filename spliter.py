

def split_sentence(paragraph):
    punctuations = ('. ', '? ', '! ', '; ', ': ')

    sentence = []
    sentences = []
    words = [word.strip() + ' ' for word in paragraph.split(' ') if word]

    for word in words:
        sentence.append(word)
        if word.endswith(punctuations):
            sentences.append(''.join(sentence) + '\n')
            sentence = []

    return sentences


if __name__ == "__main__":
    pass
