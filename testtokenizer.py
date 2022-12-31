import schtoken
import schparser
import scheval

tok = schtoken.Tokenizer()
psr = schparser.Parser()

# tok.set_input("(+ 1 2)") #works
# tok.set_input("(begin (define twice (lambda (x) (* 2 x))) (define repeat (lambda (f) (lambda (x) (f (f x))))) ( (repeat twice) 10))") #works
# tok.set_input("(define area- (- 3 4))")
# tok.set_input("(begin (define circle-area (lambda (r) (* pi (* r r)))) (circle-area 3))" )
# tok.set_input("true") #boolean works
# tok.set_input("#f") # hashed boolean val now works
#tok.set_input("(begin (define a 1) (define b a) (eq? a b))")
#tok.set_input("(begin (define f1 (lambda (x y) (* x y))) (apply f1 (4 5)))")
tok.set_input("(define a -5.)")
# tok.set_input("(begin (define twice (lambda (x) (* 2 x))) (twice 5))") #works
# tok.set_input("(begin (define fds (lambda (x) (+ x 1))) (fds 3))") #works
# tok.set_input("((lambda (x) (+ x 1)) 2)") #fixed! works
# tok.set_input(("(begin (define  a 1.1 ) (define b (+ 2 3)) (* a b)) (begin (+ 0 (+ (- 2 3 4 ) 5))); hello there \n #|(+ 2 3)|#\n (+ 4 5) (+ .6 7.8)")) #works
# tok.set_input("(< 4 5)") #works
print("input is: ")
print(tok.input)
print("lex element list:")
print(tok.l_lexemes)
print([(t.type, t.value) for t in tok.l_tokens])

print([t.value for t in tok.l_tokens])

psr.set_input(tok.l_tokens)
ast = psr.get_syntax_tree()
print("syntax tree:")
print(psr.lex_tree)
# psr.print_token_tree()

print("value: " + str(scheval.eval_expr(ast)))
