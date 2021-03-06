#rudimentary evaluator
import schtoken
import operator
import math
import schparser #for testing purposes

psr = schparser.Parser()

def fbegin(*l): #fbegin here is defined out of convenience to fit the same format as other operators
  return l[-1]

d_binary = {'+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            'expt': operator.pow,
            '<': operator.lt,
            'begin': fbegin, #this is tricky - inspired by norvig.com/lispy.html
            '>': operator.gt,
            '=': operator.eq
            } 

d_builtins = {'pi': math.pi}

#we need the varadic parameter because of how we make use of this as an operator.
# typically in this implementation we call operators with fbegin(old_result, new_arg) 
# for the special case of fbegin, we expect to return the result new_arg, ignoring old_result.

class Env(dict):
  def __init__(self, enclosing = None):
    self.enclosing = enclosing #reference to enclosing environment. for global env, this is None
  def lookup(self, name):
    if(name in self):
      #print("found " + name + " in current env")
      return self[name]
    else:
      #print("didn't find " + name + " in current env")
      return self.enclosing.lookup(name)

def global_environment():
  #return a global environment
  genv = Env()
  genv.update(d_binary)
  genv.update(d_builtins)
  return genv

genv = global_environment()

class Closure(object): #user-defined procedure (lambda)
  def __init__(self, params, body, env):
    self.params = params
    self.body = body #store the actual syntax tree
    self.env = env #store the environment at the time of definition! this creates a closure
  def __call__(self, *l_args):
    clos = Env(enclosing = self.env) #create a closure environment with encloding environment env
    clos.update(zip(self.params, l_args)) #update the closure environment with parameter-argument (formal param, actual param/argument) pairs
    return evals(self.body, clos) 

def evals(expr, env=genv):
  #print("environment is " + str(env.keys()))
  if(isinstance(expr, schtoken.Token)):
    if(expr.type == "number"):
      return expr.value
    elif(expr.type in ["identifier", "symbol"]):
      return env.lookup(expr.value)

  elif(isinstance(expr, list)): #it might be possible to clear up the conditional logic here / refactor
    if((not isinstance(expr[0],list)) and expr[0].value == "define"):
      (_define, ident, ex) = expr
      #print("in define " + ident.value + str(ex))
      env[ident.value] = evals(ex, env) 
      #print("after define, environment is " + str(env.keys()))
    elif((not isinstance(expr[0],list)) and expr[0].value == "lambda"):
      (_lambda, params_tok, body) = expr
      params = [p.value for p in params_tok] #get (formal) parameter names out of the list of tokens
      return Closure(params, body, env) #closure is stored as an instance of Closure, which is callable.
    elif((not isinstance(expr[0],list)) and expr[0].value == "if"):
      (_if, condition, ptrue, pfalse) = expr
      if(evals(condition, env)):
        runexp = ptrue
      else:
        runexp = pfalse
      return evals(runexp, env)
    else:#(expr[0].value in env): #run a procedure call
      #print("running procedure call")
      if(isinstance(expr[0], list)):
        f = evals(expr[0], env) #recurse til expr[0] is a token (with a value)
      else: #is not a list, so is a token
        #f = env.lookup(expr[0].value) #get a reference to the operator
        #print("about to call f=evals(expr[0]..) where expr is " + str(psr.tree_token2tuple(expr)) + " and expr[0] is " + str(expr[0]))
        f = evals(expr[0], env)
      #print("evaluating " + str(f))
      l_args = [evals(ex, env) for ex in expr[1:]]
      #print("l_args is " + str(l_args))
      result = f(*l_args) #call the python procedure representing the scheme procedure
        #note: this ties into how we defined 'begin'.
        #  we unpack the list of evaluated argument expressions
        #  for begin, this means we evaluate the arguments in order, but only return the result of the final one.  this is the desired behavior
      return result
      '''
      result = l_args.pop(0)
      while(l_args):
        result = f(result,l_args.pop(0))
      return result
      '''

