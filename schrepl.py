# basic read-eval-print loop for scheme2py
import schtoken
import schparser
import scheval

repl_commands = {}


# some commands will be built in to the repl rather than the eval-apply loop
def run_file(filename):
    with open(filename) as f:
        f_lines = f.readlines()
        for fl in f_lines:
            print(fl)
            tokenizer.set_input(fl)
            parser.set_input(tokenizer.l_tokens)
            abstract_syntax_tree = parser.get_syntax_tree()
            str_out = scheval.evals(abstract_syntax_tree)
            print(str_out)


repl_commands[":run"] = run_file
for cmd in [":quit", ":q", ":e", ":exit"]:
    repl_commands[cmd] = exit

# initialize tokenizer and parser
tokenizer = schtoken.Tokenizer()
parser = schparser.Parser()

while True:
    str_in = input("scheme2py:=> ")
    pre_parse = str_in.split()
    if preparse[0] in repl_commands:
        print("going to call " + str(repl_commands[preparse[0]]) + " with arguments " + str(pre_parse[1:]))
        repl_commands[pre_parse[0]](*(pre_parse[1:]))
        continue
        # repl_commands[pre_parse[0]](pre_parse[1:])
    else:
        pass
    tokenizer.set_input(str_in)
    parser.set_input(tokenizer.l_tokens)
    abstract_syntax_tree = parser.get_syntax_tree()
    str_out = scheval.evals(abstract_syntax_tree)
    print(str_out)
