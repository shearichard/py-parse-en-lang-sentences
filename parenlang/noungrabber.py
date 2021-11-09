import nltk


def process_input(api_desc):
    '''
    api_desc: is a description of some data capture needs, for instance :

        'I would like to record the books borrowed by different users at all the libraries'

    '''
    tokenized = nltk.word_tokenize(api_desc)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if(pos[:2] == 'NN')]
    return nouns


def main():
    api_desc = input("Enter a description of the data you wish to use :")
    print("")

    if api_desc.strip() == "":
        raise Exception("Description must be input")
    else:
        nouns=process_input(api_desc)
        if nouns:
            print(f'''Nouns found in text input : {api_desc}\n''')
            for n in nouns:
                print(n)
        else:
            print(f'''No nouns found in text input : {api_desc}''')
        print("")


if __name__ == '''__main__''':
    main()
