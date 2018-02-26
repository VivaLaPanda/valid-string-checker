import numpy as np
from numpy import linalg as LA
from collections import deque
import sys


# This python script will perform the 'magic'
# matrix multiplication for problem 1 for the
# cs454 project 1.
# python2.7.10


def generateVectors(orientation):

    if orientation.lower() == "column":
        col = np.matrix( """1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            1;
                            0""",dtype=object)
        #col.itemset(37,1)
        #print col
        return col
    else:
        row = np.matrix('1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	',dtype=object)
        #row.itemset(0,1)
        #print row
        return row

def p1():

    dfa = np.matrix( """0	1	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	;
                        0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	1	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	2	;
                        0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	2	;
                        0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	3	""", dtype=object)

    #print("generating column vector: ")
    magicColumn = generateVectors("column")
    #print("generating row vecotr: ")
    magicRow = generateVectors("row")
    n = input("n= ")
    # code not working past this point.
    # need to make sure dimensions of all the matrices are correct
    # also need to double check that dot product is the correct operation.
    nPower = LA.matrix_power(dfa, n)
    magicSum = np.dot(magicRow, nPower)
    magicSum = np.dot(magicSum, magicColumn)

    words = "The number of strings of length " + str(n) + " is " + str(magicSum[0,0])
    print(words)



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


def main():
    while(True):
        text = int(raw_input("Problem 1 or 2. choose 3 to quit (Answer should be a digit): "))
        if (text == 1) :
            p1()
        elif (text == 2):
            x = int(raw_input("Input k: "))
            digitsAllowed = raw_input("Digits Permitted: ")
            digitsAllowed = map(lambda x: int(x), digitsAllowed.split(" "))
            digitsAllowed.sort()
            multipleOfX = shortestPathBFS(digitsAllowed, x)
            print "Shortest multiple of " + str(x) + " using " + str(digitsAllowed) + " = " + multipleOfX[::-1]
        elif (text == 3):
            quit()
        else:
            print "Please enter just 1 or 2 or 3"
            return



main()
