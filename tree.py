#(band ,ban, bar, can)
#Aim of file is build funcion building tree.

#class myTree:
#    tree={}
#    def __init__(self):
#        pass
#
#    def build_tree(self, words):
#        for word,number in words:
#            self.add_(word,number)
#
#    def add_word(self, word, number):
#        for letter in word:
#            if letter not in self.lookup:
#                    lookup[key] = set()
#                lookup[key].add(word)



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


def build_tree(words):
    tree={}
    for word,value in words.items():
        my_tree=add_word(word,'',value,tree)
    #print(tree)
    return tree

def prediction(tree,numbers):
    pass

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

words={
  'ban': 10,
  'band': 5,
  'bar': 14,
  'can': 32,
  'candy': 7,
  'dark' : 18,
  'dream': 7,
  'darker' : 15,
  'dreams' : 178,
  'canada' : 35
}

#print(words)
#print("_______________")
tree=build_tree(words)

results = prediction(tree, "2263")
#print(predicitons)

#print("Learning to climb trees.... ")
#results=search_leaves(tree,[])
#print(results)
#sorting results to the highest likelyhood
#results.sort(key=take_second,reverse=True)
print("Final Results {}".format(results))
#search_by_number
#drzewo=myTree()
