#Exercise 1:
def thieves(x):
    if x <= 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2
    return x + thieves_sum(x - 1)
def thieves_sum(n):
    if n <= 0:
        return 0
    else:
        return thieves(n) + thieves_sum(n - 1)
def isSent(day, n = 40):
    if n - thieves_sum(day-1) - thieves(day) >= 0:
        return True
    return False
def maxDay(n = 40):
    day = 0
    while isSent(day, n):
        day += 1
    return day - 1
print("\nExercise 1")
thieve = 40
print("Mặc định số kẻ trộm là {}".format(thieve))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    thieve = int(input("Nhập tên trộm mới: "))
print("Ngày cuối có thể gửi lính đi là: ", maxDay(thieve))
for i in range(1,  maxDay(thieve) + 3):
    day = i
    print("Ngày thứ {} còn lại {} tên cướp phải sai đi {} sai đi {} còn lại {}".format(day, thieve - thieves_sum(day - 1),thieves(day), "được" if isSent(day, thieve) else "không", thieve - thieves_sum(day)))

#Exercise 2:
def rishest(x):
    if x == 0:
        return 0
    else:
        preRishest = rishest(x-1)
        return x if rishestMan[x] > rishestMan[preRishest] else preRishest
print("\nExercise 2")
rishestMan = [10, 5, 20, 30, 25, 15]
print("Mặc định người giàu nhất là: {}".format(rishestMan))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    n = int(input("Nhập số lượng người: "))
    rishestMan = []
    for i in range(n):
        asset = float(input("Nhập tiền của mọi người", i, ""))
        rishestMan.append(asset)
rank = 1
print("Mặc định xếp hạng là: {}".format(rank))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    while True:
        rank = int(input("Nhập thứ hạng mới: "))
        if rank < len(rishestMan):
            break
        else:
            print("Lỗi! Vui lòng nhập chính xác.")
print("Những người liều lĩnh nhất trong {} người đầu tiên là {} trong {}".format(rank, rishest(rank), rishestMan))

#Exercise 3:
def waytochoose(n, k):
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return waytochoose(n-1, k) + waytochoose(n-1, k-1)
print("\nExercise 3")
n = 50
print("Mặc định n = {}".format(n))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    n = int(input("Nhập mới số n = "))
way = 1000
print("Mặc định số cách = {}".format(way))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    way = int(input("Nhập số cách mới: "))
i = 0
while waytochoose(n, i) < way:
    i += 1
print("Cho {} số cách chọn gần bằng {} càng tốt.".format(i, way))
print("Với n = {}, cách = {}".format(n, way))

#Exercise 4:
def waytochooseP(n, k):
    if k == 0 or k == n:
        return 1
    if k == 1:
        return n
    return n * waytochooseP(n-1, k-1)
print("\nExercise 4")
n = 50
print("Mặc định n = {}".format(n))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    n = int(input("Nhập mới số n = "))
way = 10000
print("Mặc định số cách = {}".format(way))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    way = int(input("Nhập số cách mới: "))
i = 0
while waytochooseP(n, i) < way:
    i += 1
print("Cho {} số cách chọn gần bằng {} càng tốt.".format(i, way))
print("Với n = {}, cách = {}".format(n, way))

#Exercise 5:
def countCharacterAppeared(store):
    if store <= 1:
        return 1
    return 2*countCharacterAppeared(store-1)
print("\nExercise 5")
stories = 547
print("Mặc định câu chuyện = {}".format(stories))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    stories = int(input("Nhập mới câu chuyện = "))
print("Nhân vật xuất hiện trong {} những câu chuyện trong {}".format(stories, countCharacterAppeared(stories)))

#Exercise 6:
def F(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return n
    return F(n-1)+F(n-2)
print("\nExercise 6")
n = 10
print("Mặc đinh n = {}".format(n))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    n = int(input("Nhập mới số n = "))
for i in range(n+2):
    print(F(i), end = " ")
print("\nSố fibo thứ {} là: {}".format(n, F(n-1)))

#Exercise 7:    
def towerOfHanoi(step, s, t, mid):
    if step > 0:
        towerOfHanoi(step - 1, s, mid, t)
        t[1].append(s[1].pop())
        print("{}\n{}\n{}\n".format(A,B,C))
        towerOfHanoi(step - 1, mid, t, s)
print("\nExercise 7")
n = 3
print("Mặc đinh n = {}".format(n))
isChange = input("Gõ c nếu bạn muốn thay đổi: ")
if isChange == 'c':
    n = int(input("Nhập mới số n = "))
A = [['A'], [i for i in range(n, 0, -1)]]
B = [['B'], []]
C = [['C'], []]
towerOfHanoi(len(A[1]), A, C, B)