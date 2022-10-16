import random
import time

# get the start time
startTime = time.time()

answer = []
correctAnswer = [0, 0, 0, 0, 0, 0]
numGuess = 0
numTrials = 10

# iterate over the while loop for a certain number of trials
for i in range (numTrials):

    # randomly guess an answer for a set of six questions 
    # until a set has all six questions answered correctly
    while answer != correctAnswer:
        answer = [random.randint(0, 3) for i in range (0, 6)]
        print(answer)
        numGuess += 1
    
    # reset answer to empty to continue the iteration until 
    # the for-loop is complete
    answer = []

# wait for three seconds
time.sleep(3)

print("\nTotal Number of guesses: " + str(numGuess))

numGuessAverage = numGuess / numTrials
print("Average Number of guesses: " + str(numGuessAverage) + "\n")

theoreticalProbability = (0.25**6) * 100
experimentalProbability = ((1/numGuessAverage) * 100)

print("The theoretical probability of getting all six questions by blindly guessing is " + str(theoreticalProbability) + "%")
print("The experimental probability of getting all six questions by blindly guessing is " + str(experimentalProbability) + "%\n")

# get the end time
endTime = time.time()

# get the execution time
elapsedTime = endTime - startTime

print("Execution time: " + str(time.strftime("%H:%M:%S", time.gmtime(elapsedTime))))
print("Execution time: " + str(elapsedTime/60) + " minutes")
print("Execution time: " + str(elapsedTime) + " seconds")