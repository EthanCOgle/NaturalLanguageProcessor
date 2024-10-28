import random
allwords = []
uniquewords = []

def train(trainingData):
    # Read the training data and store all the words in a list
    f = open(trainingData, "r")

    story = f.read()
    f.close()
    for word in story.split():
        punctuation = None
        if word.endswith(".") or word.endswith(",") or word.endswith("!") or word.endswith("?"):
            punctuation = word[-1]
            word = word[:-1]
            
        word = word.lower()
        if word not in uniquewords:
            uniquewords.append(word)
        
        allwords.append(word)
        if punctuation != None:
            allwords.append(punctuation)
            if punctuation not in uniquewords:
                uniquewords.append(punctuation)

def stochasticMatrix():
    rows = len(uniquewords)
    stochastic = [[0 for x in range(rows)] for y in range(rows)]
    # Sum the amount of times each word appears after another word
    i = 0
    for word in allwords:
        if i == len(allwords) - 1:
            break
        row = uniquewords.index(word)
        col = uniquewords.index(allwords[i+1])
        stochastic[row][col] += 1
        i += 1
    # Normalize the matrix (sum of each row is 1)
    for row in range(rows):
        total = sum(stochastic[row])
        for col in range(rows):
            if total != 0:
                stochastic[row][col] /= total
    
    return stochastic

def printStochasticMatrix(stochastic):
    rows = len(uniquewords)
    temp = [[0.00 for x in range(rows)] for y in range(rows)]
    # Print the transpose of the matrix (for better readability)
    for row in range(len(temp)):
        for col in range(len(temp)):
            temp[row][col] = float(format(stochastic[col][row], '.2f'))
    
    print("Stochastic Matrix:")
    for row in temp:
        print(row)

def getStochasticMatrix(stochastic):
    # Get the transpose of the matrix
    rows = len(uniquewords)
    temp = [[0.00 for x in range(rows)] for y in range(rows)]
    for row in range(len(temp)):
        for col in range(len(temp)):
            temp[row][col] = float(format(stochastic[col][row], '.2f'))
    
    return temp

def capitalizeFirstLetter(s):
    return s[0].upper() + s[1:]

def getVector (word):
    # Create the correct basis vector for the word
    vector = [0 for x in range(len(uniquewords))]
    vector[uniquewords.index(word.lower())] = 1
    return vector

def matrixMultiply(matrix, vector):
    # Multiply the matrix by the vector 
    # (gets the probabilites of the next word)
    stochastic = getStochasticMatrix(matrix)
    result = []
    for row in stochastic:
        sum = 0
        for i in range(len(row)):
            sum += row[i] * vector[i]
        result.append(sum)
    return result

def nlp(initialword, stochastic, length):
    # Start with the initial word and generate a story of the specified length
    newStory = ""
    currWord = capitalizeFirstLetter(initialword)
    for i in range(length):
        # Get the next word based on the probabilities in the Stoachstic matrix
        vector = getVector(currWord)
        num = random.random()
        nextWordIndex = 0
        probabilities = matrixMultiply(stochastic, vector)
        for probability in range(len(probabilities)):
            if num < probabilities[probability]:
                nextWordIndex = probability
                break
            num -= probabilities[probability]
        nextWord = uniquewords[nextWordIndex]
        if currWord == "." or currWord == "!" or currWord == "?":
            nextWord = capitalizeFirstLetter(nextWord)
            newStory += currWord + '\n'
        elif nextWord == "." or nextWord == "!" or nextWord == "?" or nextWord == ",":
            newStory += currWord
        else:
            newStory += currWord + " "
        currWord = nextWord
    if newStory[length] != "." or newStory[length] != "?" or newStory[length] != "!" or newStory[length] != ",":
        newStory = newStory[:-2] + "!"
    return newStory     

trainingData = "combined.txt"
train(trainingData)
stochastic = stochasticMatrix()
#printStochasticMatrix(stochastic)
initialword = uniquewords[0]
length = 100
#print (uniquewords)
f = open("output.txt", "w")
f.write(nlp(initialword, stochastic, length))
