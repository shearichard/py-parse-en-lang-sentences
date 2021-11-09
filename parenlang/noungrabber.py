import nltk


def main():
    lines = 'I would like to record the books borrowed by different users at all the libraries'
    tokenized = nltk.word_tokenize(lines)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if(pos[:2] == 'NN')]
    print (nouns)


if __name__ == '''__main__''':
    main()
