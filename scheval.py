#rudimentary evaluator
import schtoken

def evals(expr, env):
  if(isinstance(expr, schtoken.Token)):
    if(expr.type == "number"):
      return expr.value
    elif(expr.type == "identifier"):
      return env[expr.value]

  elif(isinstance(expr, list)):
    if(expr[0].value == "+"):
      l_args = [evals(ex, env) for ex in expr[1:]]
      result = l_args.pop()
      while(l_args):
        result += l_args.pop()
      return result

class Env(dict):
  def __init__(self):
    pass
    #could implement this as a basic symbol table
