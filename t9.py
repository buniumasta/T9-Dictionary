import helper
#import gold

def parse_content(content):
    lines=content.splitlines()
    my_lista=[]
    dictionary={}
    for line in lines:
        myline=line.strip()
        my_lista=myline.split()
        dictionary[my_lista[0]]=int(my_lista[1])
    return dictionary

def add_word(word,complete_word,value,tree):
    #print("word: {} co: {}".format(word,complete_word))
    if len(word) > 1:
        if word[0] in tree:
            add_word(word[1:],complete_word+word[0],value,tree[word[0]])
        else:
            tree[word[0]]= {}
            add_word(word[1:],complete_word+word[0],value,tree[word[0]])
    else:
        tree[word[0]]={''.join('$'+complete_word+word[0]):value}
        #print("Added: key:{} value:{}".format(word[0],tree[word[0]]))
        return tree


def make_tree(words):
    tree={}
    for word,value in words.items():
        my_tree=add_word(word,'',value,tree)
    print(tree)
    return tree

def predict(tree, numbers):
    return {}


if __name__ == '__main__':
    content = helper.read_content(filename='ngrams10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)
    print(words)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)

    while True:
        # PART 3: Predict words that could follow
        numbers = helper.ask_for_numbers()
        predictions = predict(tree, numbers)

        if not predictions:
            print('No words were found that match those numbers. :(')
        else:
            for prediction, frequency in predictions[:10]:
                print(prediction, frequency)

        response = input('Want to go again? [y/N] ')
        again = response and response[0] in ('y', 'Y')
        if not again:
            break
