#Exercises 1:
print(15 * 2 + 7 * 8)
print(20 - 15 + 15 * 2)
print(20 + 30 - 3 * 15 + 5 * 5**2)
print((4/6 + 2/6)/(5/2 + 1/2))
print(14/2 + 7)
print((5 * 2)/(5 - 20 * 3**2 + 30))

#Exercises 2:
print("20 - 15 + 15 * 2) = {}".format(20 - 15 + 15 * 2))
print("20 + 30 - 3 * 15 + 5 * 5^2 ) = {}".format(20 + 30 - 3 * 15 + 5 * 5 ^ 2))
print("((4 / 6) + (2 / 6)) / ((5 / 2) + (1 / 2)) ) = {}".format(((4 / 6) + (2 / 6)) / ((5 / 2) + (1 / 2))))
print("(14 / 2) + 7 ) = {}".format((14 / 2) + 7))
print("(5 * 2) / ( 5 - 20 * 3^2 + 30) = {}".format((5 * 2) / (5 - 20 * 3 ^ 2 + 30)))

#Exercises 3: 
def sumN(n):
    s = 0
    temp = ''
    if n > 0:
      for i in range(n):
         s += i
         temp += '{} + '.format(i)
      temp += '{} = {}'.format(n, s + n)
    else:
      for i in range(0, n, -1):
        s += i
        temp += '({}) + '.format(i)
      temp += '(-{}) = {}'.format(-n, s + n)
    return temp
print(sumN(2))
print(sumN(-5))

#Exercises 4:
a = input("Input your string: ")
print("a.", ''.join(a.split()))
print('b.', a.replace(' ', '_'))

#Exercises 5:
def cacl(_str):
  if(len(_str)==1):
    return "{} = {}".format(_str, _str)
  while " " in _str:
    _str = _str.replace(" ", "")
  n1 = int(_str[0])
  operator = _str[1]
  n2 = int(_str[2]) 
  if operator == "+":
    k = n1 + n2  
  elif operator == "-":
    k = n1 - n2  
  elif operator == "*":
    k = n1 * n2  
  elif operator == "/":
    k = n1 / n2  
  elif operator == "%":
    k = n1 % n2  
  elif operator == "^":
    k = n1 ** n2  
  return "{} {} {} = {}".format(n1, operator, n2, k)
_str = input("Input your epx: ")
print(cacl(str(_str)))

#Exercises 6:
def add(first, second):
  return first + second
def minus(first, second):
  return first - second
def time(first, second):
  return first * second
def divide(first, second):
  return first / second
def modulus(first, second):
  return first % second
def getOperatorIndex(epx = ""):
  for index, letter in enumerate(epx):
    if not letter.isnumeric():
      return index
  return -1
operators = {
        '+': add,
        '-': minus,
        '*': time,
        '/': divide,
        '^': pow,
        '%': modulus
}
_str = input("Input your epx: ")
while " " in _str:
    _str = _str.replace(" ", "")
i = getOperatorIndex(_str)
if i != -1:
  print("{} {} {} = {}".format(_str[0], _str[1], _str[2], operators[_str[i]](int(_str[:i]), int(_str[i + 1:]))))
else:
  print("{} = {}".format(_str, _str))

#Exercises 7:
def mSum(A, B):
  print("With a = {}, b = {}".format(A, B))
  C = [[0 for i in range(len(A[0]))] for j in range(len(A))]
  if len(A[0]) == len(B[0]) and len(A) == len(B):
    for i in range(len(A)):
      for j in range(len(A[0])):
           C[i][j] = A[i][j] + B[i][j]
  else:
    return "-> Matrix dimension error"
  return "-> C(i,j) = A(i,j) + B(i,j) = {}".format(C)
a = [[1], [2], [3]]
b = [[1], [2]]
print(mSum(a, b))
a = [[1, 0, 1],[4, 5, 6],[1, 2, 3]] 
b = [[1, 1, 1], [2, 3, 1], [1, 5, 1]]
print()
print(mSum(a, b))

#Exercises 8:
def mProd(A, B):
  print("With a = {}, b = {}".format(A, B))
  C = [[0 for i in range(len(B[0]))] for j in range(len(A))]
  if len(A[0]) == len(B):
    for i in range(len(A)):
      for j in range(len(B[0])):
        for k in range(len(A[0])):
           C[i][j] += A[i][k] * B[k][j]
  else:
    return "-> Matrix dimension error"
  return "-> C(i,j) = A(i,k) x B(k,j) = {}".format(C)
a = [[1], [2], [3]]
b = [[1], [2]]
print(mProd(a, b))
a = [[1, 2, 3],[4, 5, 6]]
b = [[2, 2],[2, 1],[3, 3]]
print()
print(mProd(a, b))

#Exercises 9:
def ithCombine(p, q):
  return 'if {}, then {}'.format(p, q)
def panqCombine(p, q):
  return '{} and {} not {}'.format(p, q[: q.find(" ")], q[q.find(" ") + 1:])
def npoqCombine(p, q):
  return '{} not {}, or {}'.format(p[: p.find(" ")], p[p.find(" ") + 1:], q)
p = 'it sunny'
q = 'I go camping'
print("(a)",ithCombine(p, q))
print("(b)",panqCombine(p, q))
print("(c)",npoqCombine(p, q))