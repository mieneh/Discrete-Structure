import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def draw(A1, vertexs):
    G1 = nx.from_numpy_matrix(A1)
    pos = nx.spring_layout(G1)
    nx.draw_networkx(
        G1, pos=pos, with_labels=True, labels={a: b for a, b in enumerate(vertexs)}
    )
    edge_labels = nx.draw_networkx_edge_labels(G1, font_size=8, pos=pos, label_pos=0.5)
    plt.axis("equal")
    plt.show()

#Exercise 1:
#(a) Write function mPlus(A,B) to calculate the sum of two matrix A,B knowing that A + B = C where C(i,j) = A(i,j) + B(i,j)
def mPlus(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception("len A not equal len B")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("\nExercise 1a")
A = [[1, 2], [2, 3]]
B = [[3, 4], [5, 6]]
print(mPlus(A, B))
draw(np.array(mPlus(A, B)), "ab")
#(b) Write function mMinus(A,B) to calculate the difference of two matrix A,B knowing that A - B = C where C(i,j) = A(i,j) - B(i,j)
def mMinus(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception("len A not equal len B")
    return [[A[j][i] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("\nExercise 1b")
A = [[2, 2], [2, 3]]
B = [[1, 1], [3, 3]]
print(mMinus(A, B))
draw(np.array(mMinus(A, B)), "ab")
#(c) Write function mMultiply(A,B) to calculate the difference of two matrix A,B knowing that A * B = C where C(i,j) = Σ(A(i,j) * B(i,j))(n, k = 1) 
def mMultiply(A, B):
    if len(A[0]) != len(B):
        raise Exception("don't multiply matrix")

    C = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(C)):
        for j in range(len(C[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C
print("\nExercise 1c")
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print(mMultiply(A, B))
A = [[1, 4, 6, 10], [2, 7, 5, 3]]
B = [[1, 4, 6], [2, 7, 5], [9, 0, 11], [3, 1, 0]]
print(mMultiply(A, B))
#(d) Write function mTranspose(A) to calculate the transpose matrix of A where A(T, i,j) = A(i,j)
def mTranspose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
A = [[1, 2], [4, 3]]
print("\nExercise 1d")
print(mTranspose(A))
draw(np.array(mTranspose(A)), "ab")

#Exercise 2:
print("\nExercise 2a")
A = [[0, 0, 3, 0, 1], [0, 0, 5, 3, 0], [3, 5, 0, 1, 0], [0, 3, 1, 0, 2], [1, 0, 0, 2, 0]]
draw(np.array(A), "abcde")
print("\nExercise 2b")
A = [[0, 0, 0, 0, 1, 1], [0, 0, 5, 3, 0, 0], [0, 5, 0, 1, 0, 0], [0, 3, 1, 0, 2, 3], [1, 0, 0, 2, 0, 6], [1, 0, 0, 3, 6, 0]]
draw(np.array(A), "abcdef")

#Exercise 3:
def getVertexs(lines):
    vertexs = set()
    for source, dest, weight in lines:
        vertexs.add(source)
        vertexs.add(dest)
    return [v for v in vertexs]
#(a) [("A", "C", 5), ("A", "D", 3), ("B", "C", 3), ("B", "D", 2), ("C", "D", 1), ("C", "E", 3), ("D", "E", 1), ("D", "F", 3), ("E", "F", 4)]
print("\nExercise 3a")
lines = [("A", "C", 5), ("A", "D", 3), ("B", "C", 3), ("B", "D", 2), ("C", "D", 1), ("C", "E", 3), ("D", "E", 1), ("D", "F", 3), ("E", "F", 4)]
vertexs = getVertexs(lines)
vertexs.sort()
alphabet = "".join(vertexs)
mapAlphabet = {alphabet[i]: i for i in range(len(alphabet))}
n = len(alphabet)
A = [[0 for j in range(n)] for i in range(n)]
for line in lines:
    A[mapAlphabet[line[0]]][mapAlphabet[line[1]]] = line[2]
draw(np.array(A), "abcdef")
#(b) [("A", "C", 2), ("A", "D", 3), ("A", "E", 3), ("B", "C", 3), ("B", "D", 2), ("C", "D", 2), ("C", "E", 8), ("C", "F", 6), ("D", "F", 5), ("E", "F", 3)]
print("\nExercise 3b")
lines = [("A", "C", 2), ("A", "D", 3), ("A", "E", 3), ("B", "C", 3), ("B", "D", 2), ("C", "D", 2), ("C", "E", 8), ("C", "F", 6), ("D", "F", 5), ("E", "F", 3)]
vertexs = getVertexs(lines)
vertexs.sort()
alphabet = "".join(vertexs)
mapAlphabet = {alphabet[i]: i for i in range(len(alphabet))}
n = len(alphabet)
A = [[0 for j in range(n)] for i in range(n)]
for line in lines:
    A[mapAlphabet[line[0]]][mapAlphabet[line[1]]] = line[2]
draw(np.array(A), "abcdef")

#Exercise 4:
def toLoE(A):
    n = len(A)
    edgeList = [[] for i in range(n)]
    for i in range(n):
        listTemp = []
        for j in range(n):
            if A[i][j] != 0:
                listTemp.append(j)
        edgeList[i] = listTemp
    return edgeList
print("\nExercise 4")
A = [ [0, 0, 0, 0, 1, 1], [0, 0, 5, 3, 0, 0], [0, 5, 0, 1, 0, 0], [0, 3, 1, 0, 2, 3], [1, 0, 0, 2, 0, 6], [1, 0, 0, 3, 6, 0]]
edgeList = toLoE(A)
for i in range(len(edgeList)):
    print(i, "->", edgeList[i])

#Exercise 5:
print("\nExercise 5")
lists = ["Monkeys", "Apes", "Gorillas", "Primates", "Mice", "Squirrels", "Beavers", "Rodents", "Crocodiles", "Komodo dragons", "Lizards", "Reptiles", "Coconut trees", "Grasses", "Oaks", "Plants", "Mushrooms", "Molds", "Yeasts", "Fungi", "Mammals", "Animals", "Multicellular organisms", "Unicellular organisms"]
G = nx.Graph()
G.add_nodes_from(lists)
G.add_edges_from([("Monkeys", "Primates"), ("Apes", "Primates"), ("Gorillas", "Primates")])
G.add_edges_from([("Mice", "Rodents"), ("Squirrels", "Rodents"), ("Beavers", "Rodents")])
G.add_edges_from([("Crocodiles", "Reptiles"), ("Komodo dragons", "Reptiles"), ("Lizards", "Reptiles")])
G.add_edges_from([("Coconut trees", "Plants"), ("Grasses", "Plants"), ("Oaks", "Plants")])
G.add_edges_from([("Mushrooms", "Fungi"), ("Molds", "Fungi"), ("Yeasts", "Fungi")])
G.add_edges_from([("Primates", "Mammals"), ("Rodents", "Mammals")])
G.add_edges_from([("Mammals", "Animals"), ("Rodents", "Animals"), ("Reptiles", "Animals")])
G.add_edges_from([("Animals", "Multicellular organisms"), ("Plants", "Multicellular organisms"), ("Mushrooms", "Multicellular organisms"), ("Molds", "Multicellular organisms")])
G.add_edges_from([("Yeasts", "Unicellular organisms"), ("Rodents", "Animals"), ("Reptiles", "Animals")])
nx.draw(G, with_labels=True, node_size=10, linewidths=10)
plt.show()