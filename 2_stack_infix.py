from pythonds.basic.stack import Stack
import string

def infixToPostfix(infixexpr):
   prec = {}
   prec["^"] = 4
   prec["*"] = 3
   prec["/"] = 3
   prec["+"] = 2
   prec["-"] = 2
   prec["("] = 1
   opStack = Stack()
   postfixList = []
   tokenList = infixexpr.split()

   for token in tokenList:
      if token in string.ascii_uppercase or token in string.digits:
         postfixList.append(token)
      elif token == "(":
         opStack.push(token)
      elif token == ")":
         topToken = opStack.pop()
         while topToken != "(":
            postfixList.append(topToken)
            topToken = opStack.pop()

      else:
         while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
            postfixList.append(opStack.pop())
         opStack.push(token)

   while not opStack.isEmpty():
      postfixList.append(opStack.pop())
   return " ".join(postfixList)


def postfixEval(postfixExpr):
   operandStack = Stack()
   tokenList = postfixExpr.split()

   for token in tokenList:
      if token in string.digits:
         operandStack.push(int(token))
      else:
         operand2 = operandStack.pop()
         operand1 = operandStack.pop()
         result = doMath(token, operand1, operand2)
         operandStack.push(result)
   return operandStack.pop()

def doMath(op, op1, op2):
   if op == "*":
      return op1 * op2
   elif op == "/":
      return op1 / op2
   elif op == "+":
      return op1 + op2
   elif op == "^":
      return op1 ** op2
   else:
      return op1 - op2

print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))
print(postfixEval('5 3 4 2 - ^ *'))
#print(postfixEval('17 10 + 3 * 9 /'))
