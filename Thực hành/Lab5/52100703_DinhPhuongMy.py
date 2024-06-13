import math
import itertools

#Exercise 1:
print("--------------------- Exercise 1 ---------------------")
P = "You get good grade in the midterm exam"
Q = "You understand how to solve all the exercises in the book"
print("P: {}".format(P))
print("Q: {}".format(Q))
# (a) You get good grade in the midterm exam if you understand how to solve all the exercises in the book, and if you will get good grade in the midterm exam means you understand how to solve all the exercises in the book.
print("\n(a) You get good grade in the midterm exam if you understand how to solve all the exercises in the book, and if you will get good grade in the midterm exam means you understand how to solve all the exercises in the book.")
print("Q → P ∧ P → Q")
print("Q ↔ P")
#(b) You understand how to solve all the exercises in the book, but you did not get good grade in the midterm exam
print("\n(b) You understand how to solve all the exercises in the book, but you did not get good grade in the midterm exam")
print("Q ∧ ¬P (by Negation Q → P)")
#(c) By understand how to solve all the exercises in the book, you will get good grade in the midterm exam
print("\n(c) By understand how to solve all the exercises in the book, you will get good grade in the midterm exam")
print("Q → P")

#Exercise 2:
print("\n--------------------- Exercise 2 ---------------------")
print("P: {}".format(P))
print("Q: {}".format(Q))
#(a) You get good grade in the midterm exam if you understand how to solve all the exercises in the book, and if you will get good grade in the midterm exam means you understand how to solve all the exercises in the book.
print("\n(a) You get good grade in the midterm exam if you understand how to solve all the exercises in the book, and if you will get good grade in the midterm exam means you understand how to solve all the exercises in the book.")
print("Q ↔ P")
print("You get good grade in the midterm exam if, and only if you understand how to solve all the exercises in the book")
#(b) You understand how to solve all the exercises in the book, but you did not get good grade in the midterm exam
print("\n(b) You understand how to solve all the exercises in the book, but you did not get good grade in the midterm exam")
print("Q ∧ ¬P")
print("Q: you understand how to solve all the exercises in the book")
print("¬P: you did not get good grade in the midterm exam")
print("If you understand how to solve all the exercises in the book then you get good grade in the midterm exam")
#(c) By understand how to solve all the exercises in the book, you will get good grade in the midterm exam
print("\n(c) By understand how to solve all the exercises in the book, you will get good grade in the midterm exam")
print("Q → P")
print("If you understand how to solve all the exercises in the book then you will get good grade in the midterm exam")

#Exercise 3:
print("\n--------------------- Exercise 3 ---------------------")
notP = "You did not get good grade in the midterm exam"
notQ = "You do not understand how to solve all the exercises in the book"
print("P: {}".format(P))
print("Q: {}".format(Q))
print("¬P: {}".format(notP))
print("¬Q: {}".format(notQ))
#(a) You get good grade in the midterm exam if you understand how to solve all the exercises in the book, and if you will get good grade in the midterm exam means you understand how to solve all the exercises in the book.
print("\n(a) You get good grade in the midterm exam if, and only if you understand how to solve all the exercises in the book")
print("Negative:  Q ↔ P")
print("         ¬(Q → P ∧ P → Q)")
print("         ¬(Q → P) ∨ ¬(P → Q)")
print("           Q ∧ ¬P ∨ P ∧ ¬Q")
print("           You understand how to solve all the exercises in the book and you did not get good grade in the midterm exam or you get good grade in the midterm exam and you do not understand how to solve all the exercises in the book")
print("Converse: none")
print("Contrapositive: none")
#(b) You understand how to solve all the exercises in the book, but you did not get good grade in the midterm exam
print("\n(b) If you understand how to solve all the exercises in the book then you get good grade in the midterm exam")
print("The statements from: Q ∧ ¬P")
print("Negative: ¬(Q ∧ ¬P)")
print("            Q → P")
print("          If you understand how to solve all the exercises in the book then you will get good grade in the midterm exam")
print("Converse: none")
print("Contrapositive: none")
#(c) By understand how to solve all the exercises in the book, you will get good grade in the midterm exam
print("\n(c) If you understand how to solve all the exercises in the book then you will get good grade in the midterm exam")
print("The statements from: Q → P")
print("Negative: ¬(Q → P)")
print("            Q ∧ ¬P")
print("          You get good grade in the midterm exam and You do not understand how to solve all the exercises in the book")

print("Converse: P → Q")
print("          If you get good grade in the midterm exam then You understand how to solve all the exercises in the book")

print("Contrapositive: ¬P → ¬Q)")
print("                If You did not get good grade in the midterm exam then You do not understand how to solve all the exercises in the book")

#Exercise 4:
print("\n--------------------- Exercise 4 ---------------------")
print("\n(a) p = Phong has Visa")
print("    q = Phong can fly")
print("    r = Phong can speak English")
print("    t = Phong goes to America")
print("Given:")
print('S1 = "If Phong can fly, Phong will go to America"')
_4a_S1 = 'q → t'
print('S2 = "If Phong has Visa, Phong will go to America"')
_4a_S2 = 'p → t'
print('S3 = "If Phong can speak English, Phong will go to America"')
_4a_S3 = 'r → t'
print('C = "Phong goes to America"')
_4a_C = 't'
print ("\t{}\n\t{}\n\t{}\n\t.{}".format(_4a_S1, _4a_S2, _4a_S3, _4a_C))

print('\n(b) p = "An wake up late"') 
print('    q = "the traffic is flowing smooth"')
print('    q = "the traffic is heavy"')
print('    r = "school day"')
print('    s = "An have go to school"')
print('    v = "An is late for school"')
print('Given:')
print('S1 = "The traffic is always heavy on school day"')
_4b_S1 = 'r → ¬q'
print('S2 = "If An wake up late, he will be late for school on school day"')
_4b_S2 = 'p → (v ∧ r)'
print('S3 = "An only have to go to school on school day"')
_4b_S3 = 'r ↔ s'
print('S4 = "If An don’t have to go to school, An can’t be late for school"')
_4b_S4 = '¬s → ¬v'
print('C = "An is late for school"')
_4b_C = '¬v'
print ("\t{}\n\t{}\n\t{}\n\t{}\n\t.{}".format(_4b_S1, _4b_S2, _4b_S3, _4b_S4, _4b_C))

#Exercise 5:
print("\n--------------------- Exercise 5 ---------------------")
def lImplies(p, q):
    if p:
        return q
    return True
def lAnd(p, q):
    return p and q
def lOr(p, q):
    return p or q
def lXor(p, q):
    return p != q
def lNot(p):
    return not(p)
def lEquivalent(p, q):
    return p == q
def lLImplies(p, q):
    return [lImplies(p[i], q[i]) for i in range(len(p))]
def lLAnd(p, q):
    return [lAnd(p[i], q[i]) for i in range(len(p))]
def lLOr(p, q):
    return [lOr(p[i], q[i]) for i in range(len(p))]
def lLXor(p, q):
    return [lXor(p[i], q[i]) for i in range(len(p))]
def lLNot(p):
    return [lNot(p[i]) for i in range(len(p))]
def lLEquivalent(p, q):
    return [lEquivalent(p[i], q[i]) for i in range(len(p))]
print("\n(a)\t{}\n\t{}\n\t{}\n\t.{}".format(_4a_S1, _4a_S2, _4a_S3, _4a_C))
print("p\tq\tr\tt\t{}\t {}\t {}\t {}".format(_4a_S1, _4a_S2, _4a_S3, _4a_C))
print("-"*62)
for p, q, r, t in (list(itertools.product([False, True], repeat = 4))):
    print("{}\t{}\t{}\t{}\t{}\t {}\t {}\t {}".format(p, q, r, t, lImplies(q, t), lImplies(p, t), lImplies(r, t), t))
    
print("\n(b)\t{}\n\t{}\n\t{}\n\t{}\n\t{}".format(_4b_S1, _4b_S2, _4b_S3, _4b_S4, _4b_C))
print("p\tq\tr\ts\tv\t{}\t\t{}\t{}\t\t{}\t\t{}".format(_4b_S1, _4b_S2, _4b_S3, _4b_S4, _4b_C))
print("-"*109)
for p, q, r, s, v in (list(itertools.product([False, True], repeat=5))):
    print("{}\t{}\t{}\t{}\t{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(p, q, r, s, v, lImplies(r, lNot(q)), lAnd(v, r), lImplies(p, lAnd(v, r)), lEquivalent(r, s), lImplies(lNot(s), lNot(v)), lNot(v)))