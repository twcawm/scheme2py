import re

'''
note: I have found that combining regex can be quite tricky
for example:
tok.input is:
(+ 2 3)
 (+ 4 5) (+ .5 5.9)
when all we use is our number regex in isolation "\d*\.?\d+" , we get fine results:
lex element list:
['2', '3', '4', '5', '.5', '5.9']
but when we use this same number regex combined with the other regexes, we do not:
[\(\)\+\-]|[\w]+|\d*\.?\d+|"[^"\n]*"
lex element list:
['(', '+', '2', '3', ')', '(', '+', '4', '5', ')', '(', '+', '.5', '5', '.9', ')']

the 5.9 is incorrectly split into '5' and '.9', but only when the number regex is combined with OR | to the other regex.  this is confusing.

originally I tried to solve this is to use negative lookahead on the integer regex.

but I eventually found that the reason was completely different: the order in which I had combined the identifier and word regexes was the cause.  in particular, \w can match digits.  therefore \w was matching some decimal numbers, resulting in things like 5.9 being split into 5 and .9.  therefore I switched the order of identifier and word regexes in the combination.  my takeaway from this is that combining regexes into larger regexes is very tricky and error-prone.
'''


class Tokenizer:
  l_symbols = [r"(", r")", r"+", r"-"] #have to update this later
  re_symbol = r'[' +re.escape(r"".join(l_symbols)) + r']'
  re_identifier = r"[\w]+" #+ means at least 1.  \w means word character
  #re_number = r"[\d]+" #matches 1, 1., .1, 0.1, etc
  #re_number = r"[0-9]+\.?[0-9]*|\.[0-9]+"
  re_number = r"\d*\.\d+|\d+(?!\.)"
  re_number = r"\d*\.\d+|\d+(?!\.)"
  re_string_const = r'"[^"\n]*"' #starts with ".  [^...] denotes COMPLEMENT of a group. so match any number of anything except newlines and other ", then end with ".
  #instead of having a regex for keywords, we could just use identifier to capture keywords, then test all identifiers for keyword membership.

  re_lex_element = "|".join([re_symbol, re_number, re_identifier, re_string_const])
  
  #re_lex_element = re_number
  print(re_lex_element)
  compiled_lex_element = re.compile(re_lex_element)

  def __init__(self, filename = None):
    self.input = None
    self.l_tokens = None
    #later: what to do if filename is not None

   
  def set_input(self, input_string):
    self.input = input_string
    self.remove_comments()
    self.tokenize()


  def tokenize(self):
    self.l_lex_elements = self.compiled_lex_element.findall(self.input)

  # there are 2 types of comments in scheme: line and block comments https://web.mit.edu/scheme_v9.2/doc/mit-scheme-ref/Comments.html
  #line comments begin with a semicolon ;
  #block comments begin with #| and end with |#
  #note: block comments can also be nested.  but for now we will assume they are not.
  def remove_comments(self):
    i=0
    end=0
    i_eof = len(self.input) #index of 1 greater than the limit
    result = "" #text with comments removed
    while(i < i_eof):
      if(self.input[i] == '"'): #this ensures we skip all string literals
        end = self.input.find('"', i+1)
        result += self.input[i:end+1]
        i = end+1
      elif(self.input[i] == ";"):
        end = self.input.find('\n', i+1)
        if(end == -1): #newline was not found, end of input reached
          break
        i = end + 1
        result += " " #add white space in place of the comment

      elif((i+1) < i_eof and self.input[i:i+2] == "#|"):
        end = self.input.find('|#', i+2)
        i = end + 2 #since end points to | in |#, we want 1 past #, which is 2 past |
        result += " " #add white space in place of the comment
      else: #we're not in a string literal or a comment, so append the current char
        result += self.input[i]
        i += 1
    self.input = result
    return  
