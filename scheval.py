#rudimentary evaluator
import schtoken
import operator

l_binary = ['+', '-', '*', '/'] #some initial operations to get started with
d_binary = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            'expt': operator.pow,
            '<': operator.lt,
            '>': operator.gt
            } 

def evals(expr, env):
  if(isinstance(expr, schtoken.Token)):
    if(expr.type == "number"):
      return expr.value
    elif(expr.type == "identifier"):
      return env[expr.value]

  elif(isinstance(expr, list)):
    if(expr[0].value in d_binary):
      f = d_binary[expr[0].value] #get a reference to the operator
      l_args = [evals(ex, env) for ex in expr[1:]]
      result = l_args.pop(0)
      while(l_args):
        result = f(result,l_args.pop(0))
      return result

class Env(dict):
  def __init__(self):
    pass
    #could implement this as a basic symbol table
