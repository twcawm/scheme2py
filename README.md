# scheme2py

goal: interpret a subset of the Scheme language.  implement in Python 3.
be able to run interactively (read-eval-print loop)

1. lexical analysis/scanning/tokenizing: transform Scheme string into a list of tokens/lexemes
2. parsing: transform list of tokens into syntax tree / abstract syntax tree
3. evaluation: execute the syntax tree by generating values from expressions.  note that this is not just a high-level explanation - it is essentially how we implement the evaluation procedure here, as well.

to handle variables, we need some implementation of a symbol table, or 'environment' as it is known in Scheme.

and to handle local variables (e.g. in functions) we allow environments to have a nested/linked structure (each environment has an "enclosing" environment).

this project is purely for educational/entertainment purposes so I probably do not aim to make this interpreter "complete" for the entire Scheme language.  We'll start with getting some simple things working and see how it goes.

the interpreter can currently handle user-defined first-class functions and closures.

many language details are left out for brevity - the main idea here is to demonstrate the function/closure semantics.

some attention to detail is needed to lex Scheme identifiers correctly - will have to do some research on those specifications.
in fact, we will basically allow all symbols, even ones like "+" or "-", to be identifiers of the same class that "varA, i" etc would be in most languages.  this is a more flexible definition, which simplifies the process of re-defining operators  as simply an instance of the general operation of defining a variable.
could also potentially update some of the builtin functions to accept the correct number of parameters. e.g. (+ 1 2 3) in scheme cannot be directly translated to operator.add since add only accepts 2 parameters, etc.
