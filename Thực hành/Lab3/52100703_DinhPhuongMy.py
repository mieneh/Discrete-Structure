#Exxercise 1:
print("Exercise 1:")
def ex1 (D, P, formalFrom):
    print("D is '{}'".format(D))
    print("P is '{}'".format(P))
    print("Formal form:", formalFrom)
    return 

formExist = 'Exist x in D such that P(x)'
formForAll = 'For all x in D, P(x)'

# (a) For all fishes, they need water to survive.
print('(a) For all fishes, they need water to survive.')
ex1('fishes', 'need water to survive.', formForAll)

# (b) Exist a person, who is left handed
print('(b) Exist a person, who is left handed')
ex1('person','is left handed', formExist)

# (c) Exist an employee in the company, who is late to work everyday.
print('(c) Exist an employee in the company, who is late to work everyday.')
ex1('employees in the company', 'is late to work everyday', formExist)

# (d) For all fishes in this pond, they are Koi fish.
print('(d) For all fishes in this pond, they are Koi fish.')
ex1('fishes in this pond', 'are Koi fish.', formExist)

# (e) There is at least one creature in the ocean, it can live on land
print('(e) There is at least one creature in the ocean, it can live on land')
ex1('creatures in the ocean', 'can live on land', formExist)

# (f) Every students in class A did not pass the test
print('(f) Every students in class A did not pass the test')
ex1('students in class A', 'did not pass the test', formForAll)

#Exetcise 2:
print("\nExetcise 2:")
preFix = {'For all': 2, 'Exist': 1, 'There is at least one': 1, 'Every': 2, 'All': 2,'For every': 2}
irregularNouns = {
    'cactus': 'cacti',
    'child': 'children',
    'foot': 'feet',
    'goose': 'geese',
    'man': 'men',
    'mouse': 'mice',
    'person': 'people',
    'tooth': 'teeth',
    'woman': 'women'
}
def handlePreFix(s):
    for pre in preFix.keys():
        if s.startswith(pre):
            return s.find(pre) + len(pre) + 1
    return 0
def isExits(s):
    for pre, value in preFix.items():
        if s.startswith(pre):
            return value == 1
def changeNoun(d):
    firstWord = d[:len(d) if d.count(' ') == 0 else d.find(' ')]
    d = d[len(d) if d.count(' ') == 0 else d.find(' ') + 1:]
    if (firstWord in irregularNouns.keys()):
        return irregularNouns.get(firstWord) + d
    return firstWord + 's ' + d
def handleD(s):
    d = s[handlePreFix(s): s.find(',')]
    if(isExits(s) or (s.startswith('For every'))):
        if d.startswith('a '):
            d = d[2:]
        if d.startswith('an '):
            d = d[3:]
        d = changeNoun(d)
    return d
def handleP(s):
    s = s[s.find(','):]
    s = s[s.find(' ') + 1:]
    s = s[s.find(' ') + 1:]
    return s
def handleF(s):
    for entry in preFix.items():
        if s.startswith(entry[0]) and entry[1] == 1:
            return formExist
        if s.startswith(entry[0]) and entry[1] == 2:
            return formForAll
def formalConvert(s):
    D = handleD(s)
    P = handleP(s)
    F = handleF(s)
    return [D, P, F]

print(formalConvert('For all fishes, they need water to survive'))
print(formalConvert('Exist a person, who is left handed'))
print(formalConvert('Exist an employee in the company, who is late to work everyday.'))
print(formalConvert('For all fishes in this pond, they are Koi fish.'))
print(formalConvert('There is at least one creature in the ocean, it can live on land'))
print(formalConvert('Every students in class A, did not pass the test'))
print(formalConvert('All primes, it is odd.'))

#Exercise 3:
print("\nExercise 3:")
def ex3 (D, P, Q, formalFrom):
    print("D is '{}'".format(D))
    print("P is '{}'".format(P))
    print("Q is '{}'".format(Q))
    print("Formal form:", formalFrom)
    return 

formExistPQ = 'Exist x in D such that P(x) -> Q(x)'
formForAllPQ = 'For all x in D, P(x) -> Q(x)'

# (a) For all people, if they are blond then they are westerners.
print("(a) For all people, if they are blond then they are westerners.")
ex3("'people'", "'is blond'", "'is westerners'", formForAllPQ)

# (b) Exist a person, whose hair is black but is a westerner.
print("(b) Exist a person, whose hair is black but is a westerner.")
ex3("'person'", "'hair is black'", "'is a westerner'", formExistPQ)

# (c) For all students, if they study correctly then they have high score.
print("(c) For all students, if they study correctly then they have high score.")
ex3("'students'", "'study correctly'", "'has high score'", formForAllPQ)

# (d) For every mammal, if they live in the sea, they are either dolphins or whales.
print("(d) For every mammal, if they live in the sea, they are either dolphins or whales.")
ex3("'mammal'", "'lives in the sea'", "'is either dolphins or whales'", formForAllPQ)

# (e) For every bird, if they don't have wings and can swim then they are penguins.
print("(e) For every bird, if they don't have wings and can swim then they are penguins.")
ex3("'bird'", "'don't have wings and can swim'", "'is penguins'", formForAllPQ)

# (f) Exist a bird, who have wing but can't fly.
print("(f) Exist a bird, who have wing but can't fly.")
ex3("'bird'", "'has wing'", "'can't fly'", formExistPQ)


print('\nExercise 4:')
tuLamMoc = {'who ': 'but ','whose ': 'but ','if ': 'then '}
pluralVerb = {'are': 'is','have': 'has','were': 'was'}
def fixIfThen(s):
    return s.replace(', ', ' then ')
def handlePluralVerb(s):
    for verb in pluralVerb.items():
        if verb[0] in s:
            return s.replace(verb[0], verb[1])
    return s
def handlePluralNouse(s):
    verbs = {
        'fishes': 'fish',
        'students': 'student',
        'cries': 'cry',
        'flies': 'fly',
        'tries': 'try',
        'pushes': 'push',
        'catches': 'catch',
        'buzzes': 'buzz',
        'goes': 'go'
    }
    for verb in verbs.items():
        if (verb[0] in s):
            return s.replace(verb[0], verb[1])
    for verb in pluralVerb.items():
        if verb[1] in s:
            if (s[s.find(verb[1]) + len(verb[1]) + 1:][-1] == 's'):
                return s[:-1]
    return s
def handleIfThen(P, Q):
    P = P[P.find(' ')+1:]
    Q = Q[Q.find(' ')+1:]
    return [P, Q]
def handlePQ(s):
    s = s[s.find(', ') + 2:]
    for formExample in tuLamMoc.items():
        s = fixIfThen(s)
        if (formExample[0] in s and formExample[1] in s):
            P = s[s.find(formExample[0]) + len(formExample[0]): s.find(formExample[1])]
            Q = s[s.find(formExample[1]) + len(formExample[1]):]
            if (formExample == ('if ', 'then ')):
                [P, Q] = handleIfThen(P, Q)
            return [P, Q]
    return ['', '']
def handleFPQ(s):
    for entry in preFix.items():
        # 1 ∃
        if s.startswith(entry[0]) and entry[1] == 1:
            return formExistPQ
        # 2 ∀
        if s.startswith(entry[0]) and entry[1] == 2:
            return formForAllPQ
def formalConvertPQ(s):
    D = handleD(s).strip()
    [P, Q] = handlePQ(s)
    F = handleFPQ(s)
    P = handlePluralVerb(P)
    Q = handlePluralVerb(Q)
    P = handlePluralNouse(P).strip()
    Q = handlePluralNouse(Q).strip()
    return [D, P, Q, F]

print(formalConvertPQ("For all people, if they are blond then they are westerners"))
print(formalConvertPQ("Exist a person, whose hair is black but is a westerner"))
print(formalConvertPQ("For all students, if they study correctly then they have high score"))
print(formalConvertPQ("For every mammal, if they live in the sea, they are either dolphins or whales"))
print(formalConvertPQ("For every bird, if they don't have wings and can swim then they are penguins"))
print(formalConvertPQ("Exist a bird, who have wing but can't fly"))


print('\nExercise 5:')
def nega(s):
    [D, P, F] = formalConvert(s)
    noun = s[s.find(', ') + 2: s.find(P) - 1]
    if F == formForAll:
        return "-> Exist {} such that {} not {}".format(handlePluralNouse(D), noun, P)
    else:
        return "-> For all {}, {} not {}".format(handlePluralNouse(D), noun, P)
    return ''
print('(a) For all fishes, they need water to survive.')
print(nega('For all fishes, they need water to survive.'))
print('(b) Exist a person, who is left handed')
print(nega('Exist a person, who is left handed'))
print('(c) Exist an employee in the company, who is late to work everyday.')
print(nega('Exist an employee in the company, who is late to work everyday.'))
print('(d) For all fishes in this pond, they are Koi fish.')
print(nega('For all fishes in this pond, they are Koi fish.'))
print('(e) There is at least one creature in the ocean, it can live on land')
print(nega('There is at least one creature in the ocean, it can live on land'))
print('(f) Every students in class A, did not pass the test')
print(nega('Every students in class A, did not pass the test'))

print('\nExercise 6:')
print("(a) For all people, if they are blond then they are westerners")
print("Negation : There is a person, it is blond but is not westerners")
print("Contrapositive : For all people, if they are not westerners then they are not blond")
print("Converse : For all people, if they are westerners then they are blond")
print("Invert : For all people, if they are not blond then they are not westerners")

print("(b) Exist a person, whose hair is black but is a westerner")
print("Negation : For all people, whose hair is black but is not westerners")
print("Contrapositive : Exist a person, if they are not a westerner then they hair is not black")
print("Converse : Exist a person, if they is a westerner then they hair is black")
print("Invert : Exist a person, if they hair is not black, they is not a westerner")

print("(c) For all students, if they study correctly then they have high score")
print("Negation : There is a student, it studies correctly but has not high score")
print("Contrapositive : For all students, if they have not high score then they don't study correctly")
print("Converse : For all students, if they have high score, they study correctly")
print("Invert : For all students, if they don't study correctly then they have not high score")

print("(d) For every mammal, if they live in the sea, they are either dolphins or whales")
print("Negation : There is a mammal, it lives in the sea but is not not dolphins and not whales")
print("Contrapositive : For every mammal, if they are not either dolphins or whales then they don't live in the sea")
print("Converse : For every mammal, if they are either dolphins or whales, they live in the sea")
print("Invert : For every mammal, if they don't live in the sea, they are not dolphins and not whales")

print("(e) For every bird, if they don't have wings and can swim then they are penguins")
print("Negation : There is a bird, it don't have wings and can swim but is not penguins")
print("Contrapositive : For every bird, if they are not penguins then they have wings or can not swim")
print("Converse : For every bird, if then they are penguins then they don't have wings and can swim")
print("Invert : For every bird, if they have wings or can not swim then they are not penguins")

print("(f) Exist a bird, who have wing but can't fly")
print("Negation : For all birds, it have wing but can fly")
print("Contrapositive : Exist a bird, if they can fly then they have not wing")
print("Converse : Exist a bird, if they can't fly then they have wing")
print("Invert : Exist a bird, if they have not wing then can fly")