"""Multiplication quiz written without importing pyinputplus"""

import random
import time
import os

numberOfQuestions = 10
correctAnswers = 0

os.system("cls")
os.system("clear")

for questionNumber in range(numberOfQuestions):
    num1, num2 = random.randint(1, 9), random.randint(1, 9)
    prompt = "#%s: %s x %s = " % (questionNumber + 1, num1, num2)
    startTime = time.time()
    numberOfTries = 0
    while True:
        print()

        if numberOfTries == 3:
            print("Out of tries!")
            break
        try:
            response = int(input(prompt))
            nowTime = time.time()
            if nowTime >= startTime + 8:
                print("Out of time!")
                break
            elif response == (num1 * num2):
                correctAnswers += 1
                print("%s is correct!" % response)
                break
            elif response < 0:
                print("Error: Number must be positive.")
                numberOfTries += 1
            else:
                print("Incorrect!")
                numberOfTries += 1
        except ValueError:
            print("Error: The answer must be a number.")
            numberOfTries += 1

    time.sleep(1)  # Brief pause to let user see the result.
percentCorrect = (correctAnswers / numberOfQuestions) * 100
print(f"\nScore: {correctAnswers} / {numberOfQuestions} ({percentCorrect:.0f}%)\n")
