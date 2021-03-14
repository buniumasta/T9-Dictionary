import helper

#Parsing Data

def parse_content(content):
    """ Fucntion returns dictionary of pairs: work/frequency"""
    lines=content.splitlines()
    my_lista=[]
    dictionary={}
    for line in lines:
        myline=line.strip()
        my_lista=myline.split()
        dictionary[my_lista[0]]=int(my_lista[1])
    return dictionary

#Building Search dictionary - recusrive method is used

def add_word(word,complete_word,value,tree):
    """ Function adds word into the tree """
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
    """ functions goes through collections of words and add it into the tree """
    tree={}
    for word,value in words.items():
        my_tree=add_word(word,'',value,tree)
#    print(tree)
    return tree

# Prediction #####################################################################################################
def search_leaves(tree,results):
    "Search for all Leaves in the tree, and adds them into results."
    for key,branch in tree.items():
        #print("Key:{}, typ_branch:{} {}".format(key,type(branch),branch))
        if key[0]== '$':
            #print("Appending to results: {} {}".format(key[1:],branch))
            results.append([key[1:],branch])

        if type(branch) == type({}):
            search_leaves(branch,results)


#returns second element of resutls -> used for sorting result list.
def take_second(elem):
    return elem[1]

def search_branch(word,tree,results):
    """Function chooses the best tree branch which match the word """
    #print("word: {} co: {}".format(word,complete_word))
    if len(word) > 0:
        if word[0] in tree.keys():
            search_branch(word[1:],tree[word[0]],results)
        else:
            pass
            #print("Scenario1: KeyNotFoundinTree: {} Return Tree: {}".format(word[0],tree))
    else:
        #print("Scenario0: KeyFoundinTree: {} Return Tree: {}".format(word,tree))
        search_leaves(tree,results)


def search_by_number(numbers,search_word,tree,results):
    """Function build all possible words based on sequence of numbers and then run search """
    #print("numbers: {} search_word: {}".format(numbers,search_word))
    if len(numbers) > 0:
        my_digit=numbers[0]

        for letter in helper.keymap[my_digit]:
            search_by_number(numbers[1:],search_word+letter,tree,results)
            #print("Number: {} Letter: {}".format(my_digit,letter))
    else:
        #print("I will be looking for: {}".format(search_word))
        search_branch(search_word,tree,results)


def prediction(tree, numbers):
    """Function finds all words and sorts them with according to the best fit"""
    results=[]
    match_string=[]

    search_by_number(numbers,"",tree,results)
    results.sort(key=take_second,reverse=True)

    return results

# Main funciton #####################################################################################################

if __name__ == '__main__':
    content = helper.read_content(filename='ngrams10k.txt')

    # PART 1: Parsing a string into a dictionary.
    # Recursive structure & recurcive method used
    words = parse_content(content)


    # PART 2: Building a trie from a collection of words.
    # Recursive structure & recurcive method used
    tree = make_tree(words)

    predictions = prediction(tree, "222")
    print(predictions)
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
