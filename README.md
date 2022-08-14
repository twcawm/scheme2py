# scheme2py

goal: interpret a subset of the Scheme language.  implement in Python 3.
be able to run interactively (read-eval-print loop)

example interactive interpreter usage:
```
<from source directory>$python schrepl.py #<-- start read-eval-print loop python program
scheme2py:=> (define twice (lambda (x) (* 2 x ))) ;<-- define a function to multiply the argument by 2
None
scheme2py:=> (define repeat (lambda (f) (lambda (x) (f (f x))))) ;<-- define a function to repeat another function
None
scheme2py:=> ( (repeat twice) 10) ;<-- we can pass the "twice" function to the "repeat" function, then apply that function to 10.  this will apply "twice" two times to the argument, yielding the equivalent of (twice (twice 10 ))
40.0
```

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
note that currently a special case of lambda (lambda x ...) is currently not supported.  this form of lambda supports variadic argument x.  currently this only supports (lambda (x) ...)
more detail: syntax: (lambda formals body1 body2 ...)
"If formals is a proper list of variables, e.g., (x y z), each variable is bound to the corresponding actual parameter."
"If formals is a single variable (not in a list), e.g., z, it is bound to a list of the actual parameters."
"If formals is an improper list of variables terminated by a variable, e.g., (x y . z), each variable but the last is bound to the corresponding actual parameter. The last variable is bound to a list of the remaining actual parameters. An exception with condition type &assertion is raised if too few actual parameters are supplied."
(and we only support the first of those 3 cases, as it's the most critical).

note also that the lexical scoping bug apparent in the current version of "scheme2hask" is not present here:
```
scheme2py:=> (define x 3)
None
scheme2py:=> (define f (lambda (n) (begin (define x n) x ) ) )
None
scheme2py:=> (f 5)
5.0
scheme2py:=> x
3.0
```
