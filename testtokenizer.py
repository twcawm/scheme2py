import schtoken

tok = schtoken.Tokenizer()
tok.set_input("(+ 0 1); hello there \n #|(+ 2 3)|#\n (+ 4 5) (+ .6 7.8)")
print("tok.input is: ")
print(tok.input)
tok.remove_comments()
print("tok.input is: ")
print(tok.input)
#l_tokens = tok.get_tokens()
#assert(l_tokens == [["symbol", "("], ["symbol", "+"], ["number", 2], ["number", 3], "symbol", ")"])
print("lex element list:")
print(tok.l_lex_elements)
