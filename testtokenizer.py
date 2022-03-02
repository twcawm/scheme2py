import schtoken
import schparser
import scheval

tok = schtoken.Tokenizer()
psr = schparser.Parser()

tok.set_input(("(begin (define a 1) (+ a a) (* (- 1 2) a)) (begin (+ 0 (+ (- 2 3 4 ) 5))); hello there \n #|(+ 2 3)|#\n (+ 4 5) (+ .6 7.8)"
               "\n(define a 34.55)"))
print("tok.input is: ")
print(tok.input)
print("lex element list:")
print(tok.l_lexemes)
print([(t.type, t.value) for t in tok.l_tokens])

print([t.value for t in tok.l_tokens])

psr.set_input(tok.l_tokens)
ast = psr.get_syntax_tree()
print("syntax tree:")
print(psr.lex_tree)
psr.print_token_tree()

print(scheval.evals(ast))
