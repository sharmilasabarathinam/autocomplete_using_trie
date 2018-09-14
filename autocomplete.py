#!/usr/bin/python

#Spell correction reference: http://norvig.com/spell-correct.html
#                            https://routley.io/tech/2017/07/16/tries.html
#
#
#Try Benchmarking??



#####################
# Trie Data structure
#####################
class TrieNode:
  #Dictionary where,
  #key  : Character of a string
  #value: Pointer to the node containing next character in the string
  def __init__(self):
    self.children = dict();
    self.end = False;

  #Method to iteratively add all characters in a string to the Trie.
  def addString(self, word):
    #Start with the root node as the current.
    current = self
    #Iterate through the string char by char
    #If the Char exists in the dictionary, make the value corresponding to the char as current.
    #Else create a new node and add the character to the current node's dictionary and make the pointer to the new node as the value.
    #Make the new node the current node.
    #At the end of the iteration, assign the endofword variable as True.
    for char in word:
      if char in current.children:
        current = current.children[char]
      else:
        newNode = TrieNode()
        current.children[char] = newNode
        current = newNode
    current.end = True

  #Method to print all the words in the Trie datastructure.
  #Recursively call the printTrie to concatenate character by character.
  def printTrie(self, word=""):
    if(self.end == True):
      print word,

    for char in self.children.keys():
      self.children[char].printTrie(word + char)

  def suggest(self, prefix="", prev_node=None, prev_node_matching_string=""):
    if prev_node is not None:
      #print prev_node.children
      current = prev_node
      word = prev_node_matching_string
    else:
      current = self
      word = ""
    for char in prefix:
      if char in current.children:
        current = current.children[char]
        word = word + char
        prev_node = current
      else:
        break
    if(len(word) > 0):
      current.printTrie(word)
    else:
      print "Sorry nothing to suggest :("
      #print prefix
    return prev_node

####################
# Main function
####################
if __name__=="__main__":
  root = TrieNode()
  
  file = open('dictionary.txt', 'r')
  for word in file:
    root.addString(word)

  prev_txt = ""
  #print(root.children)
  #root.printTrie()
  #root.suggest("kal")

  # Enter q! to quit the loop
  # Enter prefix to search the dictionary for suggestions
  while True:
    print("Enter the string('q!' to quit):"),
    in_txt = raw_input()
    if(in_txt  == "q!"):
      break
    else:
      #If the previous search is not None and if the prev prefix is a subset of the current prefix,
      #start the search from the prev_node instead of the root of the Trie.
      if(prev_txt != "" and prev_txt == in_txt[:len(prev_txt)]):
        #print "Matching prefix:"+in_txt[:len(prev_txt)]+" "+in_txt[len(prev_txt):]
        prev_node = root.suggest(in_txt[len(prev_txt):],prev_node,prev_txt)
      else:
        #print "No matching prefix"
        prev_node = root.suggest(in_txt)
      prev_txt = in_txt
