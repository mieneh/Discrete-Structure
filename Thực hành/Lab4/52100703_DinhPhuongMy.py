import math

#Exxercise 1:
print("Exercise 1")
print("(a)")
print("P and S2 → C")
print("If Phong has Visa, Phong will go to America (by S2)")
print("Phong has Visa (by P)")
print("C: Phong goes to America (by Modus Ponens)")

print("(b)")
print("S1 and P → C1")
print("If it’s hot, it will rain the next day (by S1)")
print("It’s hot yesterday (by P)")
print("C1: It's rain today (by Modus Ponens)")
print("C1 and S2 → C2")
print("If and only if it’s not rain, Nam goes outside (by S2)")
print("if it's not rain, Nam goes outside ^ if Nam goes outside, it's not rain (by sepecialization)")
print("It's rain today (by C1)")
print("C2: Nam doesn't goes outside (by Modus Tollens)")

print("(c)")
print("S1 and R → C1")
print("The traffic is always heavy on school day (by S1)")
print("if it's school day, the traffic will be heavy (by S1)")
print("The traffic is flowing smooth (by R)")
print("C1: It is not school day (by Modus Ponens)")
print("S2 and C1 → C2")
print("If An don’t have to go to school, An can’t be late for school (by S4)")
print("It is not school day (by C1)")
print("C: An is not late for school (by Modus Ponens)")

#Exxercise 2:
print("\nExercise 2")
prove = "The given statement is correct when x equal to "
disprove = "The given statement is incorrect for all values x within the given domain."
#(a) ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 15^2 + 16^2
def _2a(n):
    for x in range(n + 1):
        if (x**2 == 15**2 + 16**2):
            return prove + str(x)
    return disprove
#(b) ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 12^2 + 16^2
def _2b(n):
    for x in range(n + 1):
        if (x**2 == 12**2 + 16**2):
            return prove + str(x)
    return disprove
#(c) ∃x ∈ Z, −50 ≤ x ≤ 50, x^2 ≥ 99*x
def _2c(n):
    for x in range(-n, n + 1):
        if (x**2 >= 99 * x):
            return prove + str(x)
    return disprove
#(d) ∃x ∈ Z, 50 ≤ x ≤ 100, x(x + 1)(x + 2)%6 != 0
def _2d(n):
    for x in range(-50, n + 1):
        if ((x * (x + 1) * (x + 2)) % 6) != 0:
            return prove + str(x)
    return disprove
#(e) ∃x, y ∈ Z, 0 ≤ x ≤ 100, √(x + y) = √x + √y
def _2e(n):
    for x in range(n + 1):
        for y in range(n + 1):
            if pow(x + y, 1 / 2) == pow(x, 1 / 2) + pow(y, 1 / 2):
                return prove + '[{}, {}]'.format(str(x), str(y))
    return disprove
print("(a) ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 15^2 + 16^2\n    -> {}".format(_2a(100)))
print("(b) ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 12^2 + 16^2\n    -> {}".format(_2b(100)))
print("(c) ∃x ∈ Z, −50 ≤ x ≤ 50, x^2 ≥ 99*x\n    ->{}".format(_2c(50)))
print("(d) ∃x ∈ Z, 50 ≤ x ≤ 100, x(x + 1)(x + 2)%6 != 0\n    -> {}".format(_2d(100)))
print("(e) ∃x, y ∈ Z, 0 ≤ x ≤ 100, √(x + y) = √x + √y\n    -> {}".format(_2e(100)))


#Exercise 3:
print("\nExercise 3")
prove = 'Prove'
disprove = 'Disprove'
#(a) ∀x ∈ Z, 0 ≤ x ≤ 100, x^3 ≥ x
def _3a(min, max):
    for x in range(min, max + 1):
        if not (x**3 >= x):
            return disprove
    return prove
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
#(b) ∀x ∈ Z, 0 ≤ x ≤ 100, and x is even, x*3 + 1 is a prime number
def _3b(min, max):
    for x in range(min, max + 1):
        if x % 2 == 0:
            if not (isPrime(x * 3 + 1)):
                return disprove
    return prove
#(c) ∀x ∈ Z, 1 ≤ x, y ≤ 100, and x is even, x*5 + 3 is a prime number
def _3c(min, max):
    for x in range(min, max + 1):
        if x % 2 == 0:
            if not (isPrime(x * 5 + 3)):
                return disprove
    return prove
#(d) ∀x ∈ Z; 0 < x ≤ 100; c % 4 = 0; ∃a, b ∈ Z+; c^2 = a^2 + b^2
def _3d(min, max):
    for c in range(min, max + 1):
        if c % 4 == 0:
            for a in range(min, max + 1):
                for b in range(min, max + 1):
                    if c**2 == a**2 + b**2:
                        return prove
    return disprove
#(e) ∀x ∈ Z; 0 < x ≤ 100; c % 5 = 0; ∃a, b ∈ Z+; c^2 = a^2 + b^2
def _3e(min, max):
    for c in range(min, max + 1):
        if c % 5 == 0:
            for a in range(min, max + 1):
                for b in range(min, max + 1):
                    if c**2 == a**2 + b**2:
                        return prove
    return disprove
#(f) ∃x ∈ Z; 0 < x ≤ 100; c^2 ≤ c
def _3f(min, max):
    for c in range(min, max + 1):
        if c**2 <= c:
            return prove
    return disprove
print("(a) ∀x ∈ Z; 0 ≤ x ≤ 100; x^3 ≥ x\n    -> {}".format(_3a(0, 100)))
print("(b) ∀x ∈ Z; 0 ≤ x ≤ 100; and x is even, x*3 + 1 is a prime number\n    -> {}".format(_3b(0, 100)))
print("(c) ∀x ∈ Z; 1 ≤ x, y ≤ 100; and x is even, x*5 + 3 is a prime number\n    -> {}".format(_3c(1, 100)))
print("(d) ∀x ∈ Z; 0 < x ≤ 100; c % 4 = 0; ∃a, b ∈ Z+; c^2 = a^2 + b^2\n    -> {}".format(_3d(0, 100)))
print("(e) ∀x ∈ Z; 0 < x ≤ 100; c % 5 = 0; ∃a, b ∈ Z+; c^2 = a^2 + b^2\n    -> {}".format(_3e(0, 100)))
print("(f) ∃x ∈ Z; 0 < x ≤ 100; c^2 ≤ c;\n    -> {}".format(_3f(0, 100)))

#Exxercise 4:
print("\nExercise 4")
#(a) Với [x, y] = [{0 -> 10}, {0 -> 10}], sum((x + y)^2)  > sum((x + 2y)^2)
def _4a(min, max):
    leftExp = 0
    rightExp = 0
    for x in range(min, max + 1):
        for y in range(min, max + 1):
            leftExp += (x + y)**2
            rightExp += (x + 2 * y)**2
    return prove if leftExp > rightExp else disprove
#(b) Với x = {0 -> 10}, 20! > sum(x!)
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
def _4b(min, max, rightExp):
    leftExp = 0
    for i in range(min, max + 1):
        leftExp += factorial(i)
    return prove if leftExp > rightExp else disprove
#(c) Với x = {0 -> 10}, sum(3x^2)  > 10^3
def _4c(min, max, rightExp):
    leftExp = 0
    for x in range(min, max + 1):
        leftExp += 3 * (x**2)
    return prove if leftExp >= rightExp else disprove
#(d) Với x = {0 -> 10}, sum(4x^3 + 6y^2 + 2x) > 10^4 + 2*10^3 + 10^2 - 5^4 - 2*5^3 - 5^2
def _4d(min, max, rightExp):
    leftExp = 0
    for x in range(min, max + 1):
        leftExp += (4 * (x**3) + 6 * (x**2) + 2 * x)
    return prove if leftExp > rightExp else disprove

print("(a) Với [x, y] = [{0 → 10}, {0 → 10}], sum((x + y)^2) > sum((x + 2y)^2)"+"\n    -> {}".format(_4a(0, 10)))
print("(b) Với x = {0 → 10}, 20! > sum(x!)"+"\n    -> {}".format(_4b(0, 10, factorial(20))))
print("(c) Với x = {0 → 10}, sum(3x^2) > 10^3"+"\n    -> {}".format(_4c(0, 10, 10**3)))
print("(d) Với x = {0 → 10}, sum(4x^3 + 6y^2 + 2x) > 10^4 + 2*10^3 + 10^2 - 5^4 - 2*5^3 - 5^2"+"\n    -> {}".format(_4d(0, 10, 11200)))

#Exxercise 5:
print("\nExercise 5")
print("(a) p → r")
print("    ¬p → q")
print("    q → s")
print("  ∴ ¬r → s")
print("Step 1: ¬p → q")
print("         q → s")
print("      ∴ ¬p → s (by Transitivity)")
print("Step 2: p → r")
print("      ∴ ¬r → ¬p (by Contrapositive)")
print("Step 3: ¬p → s")
print("        ¬r → ¬p")
print("      ∴ ¬r → s (by Transitivity)")
print("Prove")

print("\n(b) p → (q → r)")
print("    p V s")
print("    t → q")
print("    ¬s")
print("  ∴ ¬r → ¬t")
print("Step 1: p V s")
print("        ¬s")
print("      ∴ p (by Elimination)")
print("Step 2: p")
print("        p → (q → r)")
print("      ∴ q → r (by Modus Ponens)")
print("Step 3: t → q")
print("        q → r")
print("      ∴ t → r (by Transitivity)")
print("Step 4: t → r")
print("      ∴ ¬r → ¬t (by Contrapositive)")
print("Prove")

print("\n(c) p → q")
print("    ¬r V s")
print("    p V r")
print("  ∴ ¬q V s")
print("Step 1: p V r")
print("      ∴ ¬p → r (by representation of if-then as or)")
print("Step 2: ¬r V s")
print("      ∴ r → s (by representation of if-then as or)")
print("Step 3: p → q")
print("        ¬p → r")
print("      ∴ ¬q → r (by Transitivity)")
print("Step 4: ¬q → r")
print("        r → s")
print("      ∴ ¬q → s (by Transitivity)")
print("Prove")

print("\n(d) p")
print("    p → r")
print("    p → (q V ¬r)")
print("    ¬q V ¬s")
print("  ∴ s")
print("Step 1: p")
print("        p → r")
print("      ∴ r (by Modus Ponens)")
print("Step 2: p")
print("        p → (q V ¬r)")
print("      ∴ q V ¬r (by Modus Ponens)")
print("Step 3: q V ¬r")
print("      ∴ ¬q → ¬r")
print("Step 4: ¬q → ¬r")
print("        r")
print("      ∴ q (by Modus Ponens)")
print("Step 5: ¬q V ¬s")
print("      ∴ s → ¬q (by Contrapositive)")
print("Step 6: s → ¬q")
print("        q ")
print("      ∴ ¬s (by Modus Ponens)")
print("Disprove")
