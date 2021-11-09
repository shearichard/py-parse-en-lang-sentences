'''
More information about how this script is using the tags property may be found here :

https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob.tags
'''

import pprint

from textblob import TextBlob

def process_input(api_desc):
    '''
    api_desc: is a description of some data capture needs, for instance :

        'I would like to record the books borrowed by different users at all the libraries'

    '''
    wiki = TextBlob(api_desc)
    dic_tags = {}
    for w in wiki.tags:
        word = w[0]
        tag = w[1]
        #
        if tag not in dic_tags:
            dic_tags[tag] = [word]
        else:
            dic_tags[tag].append(word)
    #
    pprint.pprint(dic_tags)


def main():
    api_desc = input("Enter a description of the data you wish to use :")
    print("")
    if api_desc.strip() == "":
        raise Exception("Description must be input")
    else:
        process_input(api_desc)



if __name__ == '''__main__''':
    main()
