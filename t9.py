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
#    print(tree)
    return tree

##############################
def search_leaves(tree,results):
    for key,branch in tree.items():
        #print("Key:{}, typ_branch:{} {}".format(key,type(branch),branch))
        if key[0]== '$':
            #print("Appending to results: {} {}".format(key[1:],branch))
            results.append([key[1:],branch])

        if type(branch) == type({}):
            search_leaves(branch,results)
    #return results

#returns second element of resutls -> used for sorting of list.
def take_second(elem):
    return elem[1]

def search_branch(word,tree,results):
    #print("word: {} co: {}".format(word,complete_word))
    if len(word) > 0:
        if word[0] in tree.keys():
            search_branch(word[1:],tree[word[0]],results)
            #if type(tree[word[0]]) == type(str()):
            #    if tree[word[0]].startswith('$'):
            #        list_result.append(tree[word[0]])
            #else:
            #    search_word(word[1:],tree,list_result)
        else:
            pass
            #print("Scenario1: KeyNotFoundinTree: {} Return Tree: {}".format(word[0],tree))
            #search_leaves(tree,results)
    else:
        #print("Scenario0: KeyFoundinTree: {} Return Tree: {}".format(word[0],tree[word[0]]))
        #search_leaves(tree[word[0]],results)
        #print("Scenario0: KeyFoundinTree: {} Return Tree: {}".format(word,tree))
        search_leaves(tree,results)


keymap = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def search_by_number(numbers,search_word,tree,results):
    #print("numbers: {} search_word: {}".format(numbers,search_word))

    if len(numbers) > 0:
        my_digit=numbers[0]

        for letter in keymap[my_digit]:
            search_by_number(numbers[1:],search_word+letter,tree,results)
            #print("Number: {} Letter: {}".format(my_digit,letter))
        #if word[0] in tree:
        #    add_word(word[1:],complete_word+word[0],value,tree[word[0]])
        #else:
        #    tree[word[0]]= {}
        #    add_word(word[1:],complete_word+word[0],value,tree[word[0]])
    else:
        #print("I will be looking for: {}".format(search_word))
        search_branch(search_word,tree,results)

        #tree[word[0]]={''.join('$'+complete_word+word[0]):value}
        #print("Added: key:{} value:{}".format(word[0],tree[word[0]]))
        #return tree


def prediction(tree, numbers):
    results=[]
    match_string=[]

    search_by_number(numbers,"",tree,results)

    #search_string="b"
    #print("Searching for: {}".format(search_string) )
    #search_branch(search_string,tree,results)
    results.sort(key=take_second,reverse=True)
    #print("Results: {}".format(results))

    #print(results)
    return results

if __name__ == '__main__':
    content = helper.read_content(filename='ngrams10k.txt')

    # When you've finished implementing a part, remove the `gold.` prefix to check your own code.

    # PART 1: Parsing a string into a dictionary.
    words = parse_content(content)
    #print(words)

    # PART 2: Building a trie from a collection of words.
    tree = make_tree(words)

    predictions = prediction(tree, "222")
    print(predictions)
#    while True:
#        # PART 3: Predict words that could follow
#        numbers = helper.ask_for_numbers()
#        predictions = predict(tree, numbers)
#
#        if not predictions:
#            print('No words were found that match those numbers. :(')
#        else:
#            for prediction, frequency in predictions[:10]:
#                print(prediction, frequency)

#        response = input('Want to go again? [y/N] ')
#        again = response and response[0] in ('y', 'Y')
#        if not again:
#            break
