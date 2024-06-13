from itertools import product

#Exercise 1:
print('Exercise 1:')
print('(a) logical implies r = lImplies(p, q)')
def lImplies(p, q):
    if p:
        return q
    return True    
print('→', lImplies(False, False))

print('(b) logical and r = lAnd(p, q)')
def lAnd(p, q):
    if p:
        return q
    return False    
print('→', lAnd(True, False))

print('(c) logical or r = lOr(p, q)')
def lOr(p, q):
    if p:
        return True
    if p==q:
        return False   
    return True     
print('→', lOr(False, False))

print('(d) logical xor r = lXor(p, q)')
def lXor(p, q):
    if p==q:
        return False
    return True
print('→', lXor(False, False))        

print('(e) logical not r = lNot(p)')
def lNot(p):
    if p:
        return False 
    return True
print('→', lNot(False)) 

print('(f) logical equivalent r = lEquipvalent(p,q)')
def lEquipvalent(p, q):
    if p==q:
        return True
    return False 
print('→', lEquipvalent(True, False))        

#Exercise 2:
print('\nExercise 2:')

P = [True,True,False,False]
Q = [True,False,True,False]

print('(a) logical implies R = lLImplies(P, Q)')
def lLImplies(P, Q):
    R = []
    for p, q in zip(P, Q):
        R.append(lImplies(p, q))
    return R
print('→', lLImplies(P, Q))

print('(b) logical and R = lLAnd(P, Q)')
def lLAnd(P, Q):
    R = []
    for p, q in zip(P, Q):
        R.append(lAnd(p, q))
    return R    
print('→', lLAnd(P, Q))

print('(c) logical or R = lLOr(P, Q)')
def lLor(P, Q):
    R = []
    for p, q in zip(P, Q):
        R.append(lOr(p, q))
    return R 
print('→', lLor(P, Q))

print('(d) logical xor R = lLXor(P,Q)')
def lLXor(P, Q):
    R = []
    for p, q in zip(P, Q):
        R.append(lXor(p, q))
    return R 
print('→', lLXor(P, Q))  

print('(e) logical not R = lLNot(P)')
def lLNot(P):
    R = []
    for p in zip(P):
        R.append(lNot(p))
    return R
print('→', lLNot(P))

print('(f) logical equivalent R = lLEquivalent(P, Q)')
def lLEquipvalent(P, Q):
    R = []
    for p, q in zip(P, Q):
        R.append(lEquipvalent(p, q))
    return R
print('→', lLEquipvalent(P, Q))        

#Exercise 3: 
print('\nExercise 3') 
table = product([True, False], repeat = 3)
print('(a) p ∧ q → r')
print('p\tq\tr\tp ∧ q\tp ∧ q → r')
print('-'*41)
for p, q, r in table:
    p_imp_q = lImplies(p, q)
    p_imp_q_imp_r = lImplies(p_imp_q, r)
    print('{}\t{}\t{}\t{}\t{}'.format(p, q, r, p_imp_q, p_imp_q_imp_r))
print('\n(b) r → p ∧ q')
print('p\tq\tr\tp ∧ q\tr → p ∧ q')
print('-'*41)
for p, q, r in table:
    p_imp_q = lAnd(p, q)
    r_imp_p_imp_q = lImplies(r, p_imp_q)
    print('{}\t{}\t{}\t{}\t{}'.format(p, q, r, p_imp_q, r_imp_p_imp_q))

#Exercise 4:
print('\nExercise 4')
print('(a) p ∨ q → p ∧ q → ¬p ∨ ¬q')
print('p\tq\tp ∨ q\tp ∧ q\t¬p ∨ ¬q')
print('-'*39)
for p, q in product([True, False], repeat = 2):
    p_or_q = lOr(p, q)
    p_and_q = lAnd(p, q)
    notp_or_notq = lOr(p_or_q,p_and_q)
    print('{}\t{}\t{}\t{}\t{}'.format(p, q, r, p_or_q, p_and_q, notp_or_notq))

print('\n(b) ¬p ∨ (q ∧ r) → r')    
print('p\tq\tr\t¬p\tq ∧ r\t¬p ∨ (q ∧ r)\t¬p ∨ (q ∧ r) → r')
print('-'*72)
for p, q, r in product([True, False], repeat = 3):
    Np = lNot(p)
    q_and_r = lAnd(q,r)
    qr_or_Np = lOr(Np,q_and_r)
    qr_or_Np_imp_r = lImplies(qr_or_Np, r)
    print('{}\t{}\t{}\t{}\t{}\t{}\t\t{}'.format(p, q, r, Np, q_and_r, qr_or_Np, qr_or_Np_imp_r))

print('\n(c) (p → q) ∧ (q → r)')
print('p\tq\tr\tp → q\tq → r\t(p → q) ∧ (q → r)')
print('-'*57)
for p, q, r in product([True, False], repeat = 3):
    p_imp_q = lImplies(p,q)
    q_imp_r = lImplies(q,r)
    p_imp_q_and_q_imp_r = lImplies(p_imp_q,q_imp_r)
    print('{}\t{}\t{}\t{}\t{}\t{}'.format(p, q, r, p_imp_q, q_imp_r, p_imp_q_and_q_imp_r))

print('\n(d) (p ∨ (q ∧ r)) ↔ ((p ∨ q) ∧ (p ∨ r))')
print('p\tq\tr\tq ∧ r\tp ∨ (q ∧ r)\tp ∨ q\tp ∨ r\t(p ∨ q) ∧ (p ∨ r)\tp ∨ (q ∧ r) ↔ (p ∨ q) ∧ (p ∨ r)')
print('-'*119)
for p, q, r in product([True, False], repeat = 3):
    q_and_r = lAnd(q,r)
    p_or_p_and_r = lOr(p,q_and_r)
    p_or_q = lOr(p,q)
    p_or_r = lOr(p,r)
    p_or_q_and_p_or_r = lAnd(p_or_q,p_or_r)
    n = lEquipvalent(p_or_p_and_r,p_or_q_and_p_or_r)
    print('{}\t{}\t{}\t{}\t{}\t\t{}\t{}\t{}\t\t\t{}'.format(p, q, r, q_and_r, p_or_p_and_r, p_or_q, p_or_r, p_or_q_and_p_or_r, n))

print('\n(e) p ∨ q → ¬r ∨ t')
print('p\tq\tr\tt\tp ∨ q\t¬r ∨ t\tp ∨ q → ¬r ∨ t')
print('-'*62)
for p,q,r,t in product([True, False], repeat = 4):
    p_or_q = lOr(p, q)
    Nr = lNot(r)
    Nr_or_t = lOr(Nr, t)
    n = lImplies(p_or_q, Nr_or_t)
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(p, q, r, t, p_or_q, Nr, Nr_or_t, n))

print('\n(f) p ∨ t → q → (r → t)')
print('p\tq\tr\tt\tp ∨ t\t(p ∨ t) → q\tr → t\tp ∨ t → q → (r → t)')
print('-'*83)
for p,q,r,t in product([True, False], repeat = 4):
    p_or_t = lOr(p,t)
    p_or_t_imp_q = lImplies(p_or_t,q)
    r_imp_t = lImplies(r,t)
    n = lImplies(p_or_t_imp_q,r_imp_t)
    print('{}\t{}\t{}\t{}\t{}\t{}\t\t{}\t{}'.format(p, q, r, t, p_or_t, p_or_t_imp_q, r_imp_t, n))

print('\n(g) (p ∨ (q ∧ r)) ↔ (((p ∨ q) ∧ (p ∨ r)) ∧ (t ∨ ¬t))')
print('p\tq\tr\tt\tq ∧ r\tp ∨ (q ∧ r\tp ∨ q\tp ∨ r\t(p ∨ q) ∧ (p ∨ r)\t¬t\tt ∨ ¬t\t((p ∨ q) ∧ (p ∨ r)) ∧ (t ∨ ¬t)\tp ∨ (q ∧ r) ↔ ((p ∨ q) ∧ (p ∨ r)) ∧ (t ∨ ¬t)')
print('-'*188)
for p, q, r, t in product([True, False], repeat = 4):
    q_and_r = lAnd(q, r)
    p_or_q_and_r = lOr(p, q_and_r)
    p_or_q = lOr(p, q)
    p_or_r = lOr(p, r)
    p_or_q_and_p_or_r = lAnd(p_or_q, p_or_r)
    Nt =lNot(t)
    t_or_Nt = lOr(t, Nt)
    p_or_q_and_p_or_r_and_t_or_Nt= lAnd(p_or_q_and_p_or_r, t_or_Nt)
    n = lEquipvalent(p_or_p_and_r, p_or_q_and_p_or_r_and_t_or_Nt)
    print('{}\t{}\t{}\t{}\t{}\t{}\t\t{}\t{}\t{}\t\t\t{}\t{}\t{}\t\t\t\t{}'.format(p, q, r, t, q_and_r, p_or_q_and_r, p_or_q, p_or_r, p_or_q_and_p_or_r, Nt, t_or_Nt, p_or_q_and_p_or_r_and_t_or_Nt, n))

#Exercise 5
print('\nExercise 5')

def isEquivalent(exp, equivalent):
    if equivalent:
        print(exp, 'equivalent')
    else:
        print(exp, 'inequivalent')

for p in (list(product([False, True], repeat = 1))):
    equivalent = True
    left = p
    right = lNot(lNot(p))
    if left != right:
        equivalent = False
        break
isEquivalent('p ≡ ¬(¬p) is', equivalent)

for p, q in (list(product([False, True], repeat = 2))):
    equivalent = True
    left = lAnd(lNot(lAnd(lNot(q), p)), lOr(q, p))
    right = q
    if left != right:
        equivalent = False
        break
isEquivalent('¬(¬q ∧ p) ∧ (q ∨ p) ≡ q is', equivalent)

for p in (list(product([False, True], repeat = 1))):
    equivalent = True
    left = lNot(lOr(p, q))
    right = lOr(lNot(p), lNot(q))
    if left != right:
        equivalent = False
        break
isEquivalent('¬(p ∨ q) ≡ (¬p ∨ ¬q)', equivalent)

for p, q, r in (list(product([False, True], repeat = 3))):
    equivalent = True
    left = lImplies(lOr(p, q), r)
    right = lAnd(lImplies(p, r), lImplies(q, r))
    if left != right:
        equivalent = False
        break
isEquivalent('(p ∨ q) → r ≡ (p → r) ∧ (q → r)', equivalent)

for p, q in (list(product([False, True], repeat = 2))):
    equivalent = True
    left = lNot(lAnd(p, q))
    right = lAnd(lNot(p), lNot(q))
    if left != right:
        equivalent = False
        break
isEquivalent('¬(p ∧ q) ≡ (¬p ∧ ¬q) is', equivalent)

for p, q in (list(product([False, True], repeat = 2))):
    equivalent = True
    left = lImplies(lOr(p, lNot(q)), lNot(p))
    right = lImplies(lOr(p, (lNot(q))), lNot(p))
    if left != right:
        equivalent = False
        break
isEquivalent('(p ∨ ¬q) → ¬p ≡ (p ∨ (¬p)) → ¬p', equivalent)

for p, q in (list(product([False, True], repeat = 2))):
    equivalent = True
    left = lNot(lOr(p, q))
    right = lOr(lNot(p), lNot(q))
    if left != right:
        equivalent = False
        break
isEquivalent('¬(p ∨ q) ≡ (¬p ∧ ¬q) is', equivalent)

#Exercise 6:
print('\nExercise 6')

print('(a) p → r \n    ¬p → q \n    q → s \n    ∴ ¬r → s')
for p, q, r, s in list(product([True, False], repeat = 4)):
    p1 = lImplies(p,r)
    p2 = lImplies(lNot(p),q)
    p3 = lImplies(q,s)
    conclussion = lImplies(lNot(r), s)
    if p1 and p2 and p3:
        if not conclussion:
            print("Invalid")		
print("Valid")

print("\n(b) p → (q → r) \n    p ∨ s \n    t → q \n    ¬s \n    ∴ ¬r → ¬t")
for p, q, r, s, t in list(product([True, False], repeat = 5)):
	p1 = lImplies(p,lImplies(q, r))
	p2 = lOr(p, s)
	p3 = lImplies(t, q)
	p4 = not s
	conclussion = lImplies(not r, not t)
	if p1 and p2 and p3 and p4:
		if not conclussion:
			print("Invalid")			
print("Valid")

print("\n(c) p → q \n    ¬r ∨ s \n    p ∨ r \n    ∴ ¬q → s")
for p, q, r, s in list(product([True, False], repeat = 4)):
	p1 = lImplies(p, q)
	p2 =lOr(not r, s)
	p3 = lOr(p, r)
	conclussion = lImplies(not q, s)
	if p1 and p2 and p3:
		if not conclussion:
			print("Invalid")					
print("Valid")

print("\n(d) p  \n    p → r\n    p → (q ∨ ¬r) \n    ¬q → ¬s\n    ∴ s")
for p, q, r, s in table:
	p1 = s
	p2 =lImplies(p, r)
	p3 = lImplies(p, lOr(q, not r))
	p4 = lOr(not q, not s)
	conclussion = s
	if p1 and p2 and p3:
	    if not conclussion:
		    print("Invalid")
print("Valid")