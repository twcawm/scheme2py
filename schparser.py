import copy
class Parser:

  l_binary = ['+', '-', '*', '/'] #some initial operations to get started with
  #on second thought, we might not need these in the parser.  might use these for evaluating

  def __init__(self):
    self.input = None
    self.l_tokens = None
    self.syntax_tree = None
    #later: possibly add capability to initialize with input
   
  def set_input(self, l_tokens): #initialize with list of tokens
    self.l_tokens = l_tokens

  def get_syntax_tree(self):
    if(not self.syntax_tree):
      toks = copy.deepcopy(self.l_tokens) #make copy since we will parse this using pop
        #todo: investigate - do we need deep copy here?  or can we just use list copy
      self.syntax_tree = self.parse(toks)
    return self.syntax_tree
  
  def parse(self, toks): #we will implement this as essentially a "recursive descent" parser
    #inspiration taken from Peter Norvig's python implementation of scheme https://norvig.com/lispy.html
    if(not toks): #if the list is empty
      print("unexpected end of file")
    tok = toks.pop(0) #take leading element of tokens list
    if(tok == "("):
      l_expr = []
      #read expressions until a matching closing paren is read
      while toks[0] != ")":
        l_expr.append(self.parse(toks)) #recursively parse expressions from remaining list
      toks.pop(0) #here, either list is empty (error: no matching closing paren) or
        #next item is ")" (the matching closing paren from the if condition)
      return l_expr #return the list formed by parsing expressions (a b ... (c ...) )
    elif(tok == ")"):
      print("unexpected )")
    else: #all expressions in scheme are either atoms or list expr (...).  here, we return the atom string
      return tok
    
    
