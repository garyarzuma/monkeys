import random


def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ''
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res


def score(goal, teststring):
    numSame = 0
    for i in teststring:
        if i == goal[teststring.find(i)]:
            numSame = numSame + 1
    return [numSame, goal, teststring]


def main():
    max1 = 0
    closestString = ''
    for i in range(100000):
        scoreTemp = score("methinks it is like a weasel", generateOne(28))
        if scoreTemp[0] > max1:
            max1 = scoreTemp[0]
            closestString = scoreTemp[2]
    print("The closest string was", closestString + ". It got", max1, "letters correct.")


main()
