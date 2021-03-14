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
    print(tree)
    return tree

def prediction(tree,numbers):
    pass

def search_leaves(tree,results):
    for key,branch in tree.items():
        print("Key:{}, typ_branch:{} {}".format(key,type(branch),branch))
        if key[0]== '$':
            print("Appending to results: {} {}".format(key[1:],branch))
            results.append([key[1:],branch])

        if type(branch) == type({}):
            search_leaves(branch,results)
    return results

def take_second(elem):
    return elem[1]



words={
  'ban': 10,
  'band': 5,
  'bar': 14,
  'can': 32,
  'candy': 7,
  'dark' : 18,
  'dream': 7,
  'darker' : 15,
  'dreams' : 178
}

print(words)
print("_______________")
tree=build_tree(words)

print("Learning to climb trees.... ")
results=search_leaves(tree,[])
print(results)
results.sort(key=take_second,reverse=True)
print(results)
#drzewo=myTree()
