import os


def get_words(filename):
    with open(filename, encoding='utf-8') as file:
        text = file.read()
        text = text.replace('\n', '')
        text = text.replace(',', '').replace('.', '').replace('?', '').replace('!', '')
        text = text.lower()
        words = text.split()
        words.sort()
        return words


def get_words_dict(words):
    word_dict = dict()

    for word in words:
        if word in word_dict:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
    return word_dict


def main():
    filename = input('Enter the path to the file')
    if not os.path.exists(filename):
        print('Specified file does not exists')
    else:
        words = get_words(filename)
        word_dict = get_words_dict(words)
        print('Number of words: %d' % len(words))
        print('Number of unique words: %d' % len(word_dict))
        print('All words used: ')
        for word in word_dict:
            print(word.ljust(20), word_dict[word])


if __name__ == '__main__':
    main()

//lol
