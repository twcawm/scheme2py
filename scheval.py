#rudimentary evaluator
import schtoken
import operator

d_binary = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            'expt': operator.pow,
            '<': operator.lt,
            '>': operator.gt,
            'begin': lambda *l: l[-1] #this is tricky - inspired by norvig.com/lispy.html
                     #begin 
            } 

class Env(dict):
  def __init__(self, enclosing = None):
    self.enclosing = enclosing #reference to enclosing environment. for global env, this is None
  def lookup(self, name):
    if(name in self):
      return self[name]
    else:
      return self.enclosing.lookup(name)

def global_environment():
  #return a global environment
  genv = Env()
  genv.update(d_binary)
  return genv

genv = global_environment()

def evals(expr, env=genv):
  print("environment is " + str(env.keys()))
  if(isinstance(expr, schtoken.Token)):
    if(expr.type == "number"):
      return expr.value
    elif(expr.type == "identifier"):
      return env[expr.value]

  elif(isinstance(expr, list)):
    if(expr[0].value == "define"):
      (_define, ident, ex) = expr
      print("in define " + ident.value + str(ex.value))
      env[ident.value] = evals(ex, env) 
      print("after define, environment is " + str(env.keys()))
    elif(expr[0].value in env):
      #print("running procedure call")
      f = env[expr[0].value] #get a reference to the operator
      l_args = [evals(ex, env) for ex in expr[1:]]
      result = l_args.pop(0)
      while(l_args):
        result = f(result,l_args.pop(0))
      return result

