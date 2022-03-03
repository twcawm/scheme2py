import copy
import schtoken
class Parser:

  def __init__(self):
    self.input = None
    self.l_tokens = None
    self.token_tree = None #syntax tree of full tokens
    self.lex_tree = None #syntax tree of token values (lexemes)
    #later: possibly add capability to initialize with input
   
  def set_input(self, l_tokens): #initialize with list of tokens
    self.l_tokens = l_tokens

  def get_syntax_tree(self):
    toks = copy.deepcopy(self.l_tokens) #make copy since we will parse this using pop
        #todo: investigate - do we need deep copy here?  or can we just use list copy
    self.token_tree = self.parse(toks)
    self.lex_tree = self.tree_token2lex(self.token_tree)
    return self.token_tree

  def tree_token2lex(self, tree):
    if(isinstance(tree, list)):
      result = []
      for item in tree:
        if(isinstance(item,list)):
          result.append(self.tree_token2lex(item))
        elif(isinstance(item,schtoken.Token)): #not a list, so is a token
          result.append(item.value)
        else:
          print("error in tree_token2lex: something was not a list or a token")
      return result
    elif(isinstance(tree, schtoken.Token)):
      return tree.value

  def tree_token2tuple(self, tree):
    if(isinstance(tree, list)):
      result = []
      for item in tree:
        if(isinstance(item,list)):
          result.append(self.tree_token2tuple(item))
        elif(isinstance(item,schtoken.Token)): #not a list, so is a token
          result.append((item.type, item.value))
        else:
          print("error in tree_token2tuple: something was not a list or a token")
      return result
    elif(isinstance(tree, schtoken.Token)):
      return (tree.type, tree.value)

  def print_token_tree(self):
    tuple_tree = self.tree_token2tuple(self.token_tree)
    print(tuple_tree)
  
  def parse(self, toks): #we will implement this as essentially a "recursive descent" parser
    #inspiration taken from Peter Norvig's python implementation of scheme https://norvig.com/lispy.html
    if(not toks): #if the list is empty
      print("unexpected end of file")
    tok = toks.pop(0) #take leading element of tokens list
    if(tok.value == "("):
      l_expr = []
      #read expressions until a matching closing paren is read
      while toks[0].value != ")":
        l_expr.append(self.parse(toks)) #recursively parse expressions from remaining list
      toks.pop(0) #here, either list is empty (error: no matching closing paren) or
        #next item is ")" (the matching closing paren from the if condition)
      return l_expr #return the list formed by parsing expressions (a b ... (c ...) )
    elif(tok.value == ")"):
      print("unexpected )")
    else: #all expressions in scheme are either atoms or list expr (...).  here, we return the atom string
      return tok
    
    
