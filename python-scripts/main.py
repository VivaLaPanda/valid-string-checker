import problem01
import problem2

def main():
    text = int(raw_input("Problem 1 or 2 (Answer should be a digit): "))
    if (text == 1) :
        print "Not yet implemented"
    elif (text == 2):
        x = int(raw_input("Input k: "))
        digitsAllowed = raw_input("Digits Permitted: ")
        digitsAllowed = map(lambda x: int(x), digitsAllowed.split(" "))
        multipleOfX = problem2.shortestPathBFS(digitsAllowed, x)
        print "Shortest multiple of " + str(x) + " using " + str(digitsAllowed) + " = " + multipleOfX
    else:
        print "Please enter just 1 or 2"
        return

if __name__ == "__main__":
    main()
