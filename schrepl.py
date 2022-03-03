#basic read-eval-print loop for scheme2py
import schtoken
import schparser
import scheval

#initialize tokenizer and parser
tokenizer = schtoken.Tokenizer()
parser = schparser.Parser()

while(True):
  str_in = input("scheme2py:=> ")
  tokenizer.set_input(str_in)
  parser.set_input(tokenizer.l_tokens)
  abstract_syntax_tree = parser.get_syntax_tree()
  str_out = scheval.evals(abstract_syntax_tree)
  print(str_out)
