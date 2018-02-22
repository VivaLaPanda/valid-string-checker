from collections import deque
import sys

def getNeighbors(state, validDigits, x):
    """
    Returns a list of all neighboring vertices
    :return: list of vertexes
    """

    return map(lambda input: ((int(state) * 10 + int(input)) % int(x), input), validDigits)

def shortestPathBFS(validDigits, x):
    """
    Shortest Path - Breadth First Search
    :param vertex: the starting graph node
    :return: does not return, changes in place
    """
    if validDigits is []:
        return

    if x is None:
        return

    state = (-1, "")
    queue = deque([])
    parent = {}
    visited = {}
    strBuffer = ""

    if 0 in validDigits:
        return "0"

    # We start be handling the first children specially. This prevents problems
    # with 0 as a starting state
    for neighbor in getNeighbors(0, validDigits, x):
        if neighbor[0] not in visited:
            queue.appendleft(neighbor)
            parent[neighbor[0]] = state
            visited[neighbor[0]] = True

    # BFS
    while len(queue) > 0:
        # Get the first node. We store a tuple of state and the edge that gets
        # us there
        statePair = queue.pop()
        strState = statePair[1]
        state = statePair[0]

        # We are in a terminal state, build the string
        if (state == 0):
            while not statePair[0] == -1:
                # print state
                strBuffer += str(statePair[1])
                statePair = parent[statePair[0]]
            return strBuffer

        # Enqueu next nodes in the graph
        for neighbor in getNeighbors(state, validDigits, x):
            if neighbor[0] not in visited:
                queue.appendleft(neighbor)
                parent[neighbor[0]] = statePair
                visited[neighbor[0]] = True

    return "No string exists"
