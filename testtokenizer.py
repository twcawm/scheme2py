import schtoken

tok = schtoken.Tokenizer()
tok.set_input(("(+ 0 1); hello there \n #|(+ 2 3)|#\n (+ 4 5) (+ .6 7.8)"
               "\n(define a 34.55)"))
print("tok.input is: ")
print(tok.input)
print("lex element list:")
print(tok.l_lex_elements)
