
def a_knows_b(graph, a, b):
    return graph[a-1][b-1] == 1


def celebrity(graph, people):
    if len(people) == 1:
        return people[0]

    a = people[0]
    b = people[1]

    # If a knows b, then a isn't the celebrity; otherwise, b isn't the celebrity
    if a_knows_b(graph, a, b):
        s = a
        people.remove(a)
    else:
        s = b
        people.remove(b)

    # find out the celebrity in people - {person not celebrity}  = S'
    # note that if there is no celebrity in S', then there is no celebrity in S
    # because we just remove a person who we knew that isn't a celebrity form S to get S'
    k = celebrity(graph, people)

    # if the supposed celebrity 'k', in S', knows s or s doesn't know k,
    # then k actually isn't a celebrity, and thus there is no celebrity
    if a_knows_b(graph, k, s) or (not a_knows_b(graph,s,k)):
        return 0

    return k



graph = [[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]]
people = list(range(1, len(graph) + 1))

names =['a', 'b', 'c', 'd']

print(names[celebrity(graph, people)-1])