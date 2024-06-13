#Exercise 1:
Andersen = {"The Emperor's New Clothes","The Little Mermaid","The Little Match Girl","The SnowQueen",}
print("\nExercise 1")
print("Andersen: {}".format(Andersen))

#Exercise 2:
Shakespeare = {"Romeo and Juliet","Hamlet","King Lear","Macbeth","A Midsummer Night's Dream","A Comedy of Errors",}
print("\nExercise 2")
print("Shakespeare: {}".format(Shakespeare))

#Exercise 3:
Tragedy = {"Medea","Octavia","Oedipus","Ur-Hamlet","Romeo and Juliet","Hamlet","King Lear","Macbeth",}
Comedy = {"The Three Musketeer","The Clouds","A Midsummer Night's Dream","A Comedy of Errors",}
Uncategory = {"Don Quixote", "Rapunzel", "Cinderella", *Andersen}
print("\nExercise 3")
print("Tragedy: {}".format(Tragedy))
print("Comedy: {}".format(Comedy))
print("Uncategory: {}".format(Uncategory))

#Exercise 4:
print("\nExericises 4")
Shakespeare_Tragedy = Shakespeare - Tragedy
print("Shakespeare_Tragedy: {}".format(Shakespeare_Tragedy))

#Exercise 5:
print("\nExercise 5")
Andersen_Comedy = Andersen & Comedy
print("Andersen_Comedy: {}".format(Andersen_Comedy))

#Exercise 6:
def getNameVariable(variable):
    for name in globals():
        if eval(name) == variable:
            return name
print("\nExercise 6")
authors = [Shakespeare_Tragedy, Andersen_Comedy]
works = [Andersen, Shakespeare, Tragedy, Comedy, Uncategory]
for author in authors:
    for work in works:
        print("{} is subnet {} is {}".format(getNameVariable(author), getNameVariable(work), author.issubset(work)))
        print("{} is superset {} is {}".format(getNameVariable(author), getNameVariable(work), author.issuperset(work)))
        print("{} is disjoint {} is {}".format(getNameVariable(author), getNameVariable(work), author.isdisjoint(work)))

#Exercise 7:
print("\nExercise 7")
Work = Andersen | Tragedy | Comedy | Uncategory
print("Work: {}".format(Work))

#Exercise 8:
print("\nExercise 8")
Author = {"Shakespeare", "Andersen", "Unknown"}
print("Author: {}".format(Author))

#Exercise 9:
def gAuthor(work):
    if work in Andersen:
        return "Andersen"
    if work in Shakespeare:
        return "Shakespeare"
    return "Unknown"
print("\nExercise 9")
Author_Of = {w: gAuthor(w) for w in Work}
for e in Author_Of.items():
    print("Author_Of [{}] is {}".format(e[0], e[1]))

#Exercise 10:
def writen_by():
    result = {}
    for work, author in Author_Of.items():
        if result.get(author) == None:
            result[author] = [work]
        else:
            result[author].append(work)
    return result
print("\nExercise 10")
for e in writen_by().items():
    print("Writen_By {} is {}".format(e[0], e[1]))

#Exercise 11:
print("\nExercise 11")
print("Work_Count: {}".format(len(Work)))

#Exercise 12:
questions = [
    """Han Christian Andersen is famous for fairy tales such as: "The Emperor's New Clothes", "The Little Mermaid", "The Little Match Girl", "The Snow Queen". Create a set in Python named Andersen and put his fairy tales' names as elements.""",
    """Shakespeare is mostly famous for his tragedies such as: "Romeo and Juliet", "Hamlet", "King Lear", "Macbeth". Meanwhile, he also wrote comedies such as: "A Midsummer Night's Dream" and "A Comedy of Errors". Create a set in Python named Shakespeare and put his plays names as elements.""",
    """Given the tragedies such as: "Medea", "Octavia", "Oedipus", "Ur-Hamlet". Comedies such as: "The Three Musketeer", "The Clouds". Meanwhile there are some stories that is hard to put in either comedies or tragedies such as: "Don Quixote", "Rapunzel", "Cinderella". Create 3 sets named Tragedy, Comedy and Uncategory then put the above works', included Andersen and Shakespeare's works, names in the right categories.""",
    """Create a set named Shakespeare_Tragedy by taking the difference of 2 related sets""",
    """Create a set named Andersen_Comedy by taking the intersection of 2 related sets""",
    """Determine the relationship of Andersen_Comedy and Shakespeare_Tragedy with Shakespeare, Andersen, Tragedy, Comedy, and Uncategory set. The relations needed to be test is: issubset, issuperset, isdisjoint.""",
    """Create a set named Work by combine all the above set""",
    """Create a set named Author taking authors' names and 'Unknown' as it's elements.""",
    """Using python Dict named Author_Of to represent the relation between Work and Author. Which mean, print(Author_Of['Hamlet']) should print Shakespeare.""",
    """Using python Dict named Writen_By to represent the invert relation of Author_Of.""",
    """Using python Dict named Work_Count to count how many sets each Work appeared.""",
    """Within the content of Exercise section count how many words are in this section of the Lab.""",
    """Count how many times each words appeared and sorted the word by number of times they appeared descending.""",
]
result = {}
i = 1
for question in questions:
    result["question " + str(i)] = len(question.replace('"', "").replace("' ", "").replace(".", "").split(" "))
    i += 1
print("\nExercise 12")
for e in result.items():
    print("Section count in {} is {}".format(e[0], e[1]))

#Exxercise 13:
def sortByTime(input):
    return input[1]
result = {}
for question in questions:
    for word in (question.replace('"', "").replace("' ", "").replace(".", "").split(" ")):
        if result.get(word) == None:
            result[word] = 1
        else:
            result[word] += 1
result = [r for r in result.items()]
result.sort(reverse=True, key = sortByTime)
print("\nExercises 13")
print("Time_Each_Word: {}".format(result))