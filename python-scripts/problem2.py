from collections import deque

def getNeighbors(state, validDigits, x):
    """
    Returns a list of all neighboring vertices
    :return: list of vertexes
    """

    return map(lambda input: (int(state) * 10 + int(input)) % int(x), validDigits)

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

    state = 0
    queue = deque([])                               # our queue is a list with insert(0) as enqueue() and pop() as dequeue()
    queue.extendleft(getNeighbors(state, validDigits, x))
    parent = {}
    visited = {}
    strBuffer = ""

    if 0 in validDigits:
        return "0"

    while len(queue) > 0:
        state = queue.pop()

        # We are in a terminal state, build the string
        if (state == 0):
            while state in parent:
                print state
                # print state
                strBuffer += str(state)
                state = parent[state]
            return strBuffer

        # Enqueu next nodes in the graph
        if state not in visited:
            for neighbor in getNeighbors(state, validDigits, x):
                queue.appendleft(neighbor)
                parent[neighbor] = state
        visited[state] = True

    return "FATAL ERROR"
