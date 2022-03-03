# scheme2py

goal: interpret a subset of the Scheme language.  implement in Python 3.
be able to run interactively (read-eval-print loop) or on a file.

1. lexical analysis/scanning/tokenizing: transform Scheme string into a list of tokens/lexemes
2. parsing: transform list of tokens into syntax tree / abstract syntax tree
3. evaluation: execute the syntax tree by generating values from expressions

to handle variables, we need some concept of a symbol table, or 'environment' as it is known in Scheme.

and to handle local variables (e.g. in functions) we allow environments to "stack".

this project is purely for educational/entertainment purposes so I probably do not aim to make this interpreter "complete" for the entire Scheme language.  We'll start with getting some simple things working and see how it goes.

the interpreter can currently handle user-defined first-class functions and closures.

many language details are left out for brevity - the main idea here is to demonstrate the function/closure functionality.

todo: a few updates to lexical analysis are needed.  for example "circle-area" was not parsed as a single identifier.  some attention to detail is needed to lex identifiers correctly - will have to do some research on those specifications.
