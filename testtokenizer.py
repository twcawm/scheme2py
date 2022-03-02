import schtoken
import schparser

tok = schtoken.Tokenizer()
psr = schparser.Parser()

tok.set_input(("(+ 0 (+ 1 2)); hello there \n #|(+ 2 3)|#\n (+ 4 5) (+ .6 7.8)"
               "\n(define a 34.55)"))
print("tok.input is: ")
print(tok.input)
print("lex element list:")
print(tok.l_lex_elements)

psr.set_input(tok.l_lex_elements)
ast = psr.get_syntax_tree()
print("syntax tree:")
print(ast)
