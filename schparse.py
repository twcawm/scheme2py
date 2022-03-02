import copy
class Parser:

  l_binary = ['+', '-', '*', '/'] #some initial operations to get started with

  def __init__(self):
    self.input = None
    self.l_tokens = None
    #later: possibly add capability to initialize with input
   
  def set_input(self, l_tokens): #initialize with list of tokens
    self.l_tokens = l_tokens

  def parse(self): #we will implement this as essentially a "recursive descent" parser
    #inspiration taken from Peter Norvig's python implementation of scheme https://norvig.com/lispy.html
    toks = copy.deepcopy(self.l_tokens) #make copy since we will parse this using pop
      #todo: investigate - do we need deep copy here?  or can we just use list copy
    if(not toks): #if the list is empty
      pass
    
    
